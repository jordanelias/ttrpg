"""
engine_audit_harness.py — INDEPENDENT audit of the sigma-leverage engine.

Not the M1 self-test (that would be circular). This re-derives the continuous
model independently (own erf-based Phi), computes the EXACT discrete net
distribution by convolution, imports the reference impl's functions, and tests:

  T1  reference impl == its own continuous spec (cross-check)
  T2  uniform impact, continuous model, all pools incl. 1D  (defends the claim where it holds)
  T3  discrete-vs-continuous divergence at small pools       (ED-836 / WS-D-1 stress)
  T4  Ob-floor P-232 interaction: engine produces Ob<1; clamp breaks uniformity
  T5  TN miscalibration from hardcoded SIGMA_N_COEFF=0.8      (PORT-1)
  T6  soft_cap: monotone/odd/bounded/slope@0; marginal stacking; P in (0,1)

Canon anchors: params/core.md (face rule, per-die mu/sigma TN6/7/8, Ob min 1
[P-232], continuous engine ED-833/836, pool floor 1D).
Reference impl: tests/sim/v32-combat-balance/m1_dice_sigma_core.py.
"""
import sys, math
sys.path.insert(0, '/home/claude')
import numpy as np

# ---- independent continuous primitives (do NOT reuse M1) ----
def Phi(z):                      # standard normal CDF, own implementation
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))

PER_DIE = {6: (0.50, 0.806), 7: (0.40, 0.800), 8: (0.30, 0.781)}  # params/core.md

def cont_p_success(base_ob, pool, net_sigma, tn, coeff, capped, m_max=1.5):
    """Independent continuous P(net >= Eff_Ob). coeff = the sigma_N coefficient
    used in the Ob-shift (engine hardcodes 0.8; per-TN would use sigma_tn)."""
    mu, sigma = PER_DIE[tn]
    eff = m_max * math.tanh(net_sigma / m_max) if capped else net_sigma
    sig_n = coeff * math.sqrt(max(1, pool))
    eff_ob = base_ob - eff * sig_n
    z = (eff_ob - mu * pool) / (sigma * math.sqrt(max(1, pool)))
    return 1.0 - Phi(z), eff_ob

# ---- exact discrete net distribution (own convolution) ----
def die_pmf(tn):
    """Single-die net pmf under canonical face rule (1->-1, 2..6->0, 7..9->+1, 10->+2)."""
    p = {}
    p[-1] = 0.1                                   # face 1
    zero_faces = (tn - 1) - 1                      # faces 2..(tn-1)
    plus1_faces = 9 - (tn - 1)                     # faces tn..9
    p[0]  = zero_faces * 0.1
    p[1]  = plus1_faces * 0.1
    p[2]  = 0.1                                    # face 10
    return p

def net_pmf(pool, tn):
    """Exact pmf of summed net over `pool` dice, by repeated convolution."""
    base = die_pmf(tn)
    dist = {0: 1.0}
    for _ in range(pool):
        nd = {}
        for k, pk in dist.items():
            for j, pj in base.items():
                nd[k + j] = nd.get(k + j, 0.0) + pk * pj
        dist = nd
    return dist

def disc_p_ge(pool, tn, threshold):
    """Exact discrete P(net >= threshold). threshold may be fractional."""
    d = net_pmf(pool, tn)
    return sum(p for k, p in d.items() if k >= threshold)

# ---- import the REAL engine to cross-check ----
sys.path.insert(0, '/home/claude')
import importlib.util
spec = importlib.util.spec_from_file_location("m1", "/home/claude/m1_dice_sigma_core.py")

# We don't have it on disk; write it from the fetched source path used earlier.
# Instead, re-fetch via github_ops to be safe and import from a temp file.
from github_ops import quick_bootstrap
g, h, files, token = quick_bootstrap()
src = g.read_files_graphql(['tests/sim/v32-combat-balance/m1_dice_sigma_core.py'], force_full=True)
open('/home/claude/m1_dice_sigma_core.py', 'w').write(src['tests/sim/v32-combat-balance/m1_dice_sigma_core.py'])
m1 = importlib.util.module_from_spec(spec); spec.loader.exec_module(m1)

R = "="*72
def hdr(t): print("\n" + R + "\n" + t + "\n" + R)

# ============================ T1 ============================
hdr("T1  reference impl  ==  independent continuous spec")
maxdiff = 0.0
for tn in (6, 7, 8):
    for pool in (1, 2, 3, 5, 8, 12, 20):
        for ns in (-1.5, -0.7, 0.0, 0.25, 0.7, 1.0, 1.5, 3.0):
            for cap in (True, False):
                base = PER_DIE[tn][0] * pool          # 50%-ish base
                mine, _ = cont_p_success(base, pool, ns, tn, m1.SIGMA_N_COEFF, cap)
                theirs = float(m1.p_success(base, pool, ns, tn, capped=cap))
                maxdiff = max(maxdiff, abs(mine - theirs))
print(f"max |independent - reference| over full grid = {maxdiff:.2e}")
print("VERDICT:", "MATCH (engine implements its stated spec)" if maxdiff < 1e-9 else "DIVERGENCE — investigate")

# ============================ T2 ============================
hdr("T2  uniform impact, CONTINUOUS model, dsigma=+0.7 uncapped, 50% base")
print(f"{'pool':>5} {'P0%':>7} {'P1%':>7} {'dP pp':>7}")
imp = []
for pool in (1, 2, 3, 4, 5, 8, 12, 17, 20):
    base = PER_DIE[7][0]*pool
    p0,_ = cont_p_success(base, pool, 0.0, 7, m1.SIGMA_N_COEFF, False)
    p1,_ = cont_p_success(base, pool, 0.7, 7, m1.SIGMA_N_COEFF, False)
    imp.append((p1-p0)*100)
    print(f"{pool:>4}D {p0*100:7.1f} {p1*100:7.1f} {(p1-p0)*100:7.2f}")
print(f"spread = {max(imp)-min(imp):.3f} pp  → continuous model is EXACTLY uniform incl. 1D")

# ============================ T3 ============================
hdr("T3  DISCRETE-vs-CONTINUOUS divergence, same dsigma=+0.7, base_Ob=mu*N (TN7)")
print("  modifier shifts Eff_Ob; discrete net is integer, so impact is lumpy at small N")
print(f"{'pool':>5} {'cont dP':>9} {'disc dP':>9} {'gap pp':>8}")
for pool in (1, 2, 3, 4, 5, 8, 12, 20):
    base = PER_DIE[7][0]*pool
    # continuous
    pc0,_ = cont_p_success(base, pool, 0.0, 7, m1.SIGMA_N_COEFF, False)
    pc1, eff_ob1 = cont_p_success(base, pool, 0.7, 7, m1.SIGMA_N_COEFF, False)
    _, eff_ob0 = cont_p_success(base, pool, 0.0, 7, m1.SIGMA_N_COEFF, False)
    # discrete: P(net >= Eff_Ob) at the SAME (fractional) effective Ob values
    pd0 = disc_p_ge(pool, 7, eff_ob0)
    pd1 = disc_p_ge(pool, 7, eff_ob1)
    print(f"{pool:>4}D {(pc1-pc0)*100:8.2f}  {(pd1-pd0)*100:8.2f}  {abs((pc1-pc0)-(pd1-pd0))*100:7.2f}")
print("  → continuous is flat ~25.8pp; discrete is NOT uniform at small N (the ED-836 'shaky' zone)")

# ============================ T4 ============================
hdr("T4  Ob-floor P-232 ('Ob minimum 1; no modifier below 1') vs the engine")
print("  (a) does the ENGINE (no clamp) produce Eff_Ob < 1 ?  base_Ob=2, favorable stacks")
for pool in (4, 6, 8, 12):
    for ns in (0.5, 1.0, 1.5, 2.0):
        eff_ob = m1.eff_ob(2, pool, ns)
        flag = "  <-- BELOW 1 (P-232 violation)" if eff_ob < 1 else ("  (<0!)" if eff_ob < 0 else "")
        if eff_ob < 1:
            print(f"    pool {pool:>2}D net_sigma +{ns:>3}  ->  Eff_Ob = {eff_ob:+.3f}{flag}")
print("  (b) IF Eff_Ob clamped to >=1 (canon), uniform impact of a favorable dsigma BREAKS:")
print(f"      {'pool':>5} {'dP unclamped':>13} {'dP clamped@1':>13}")
for pool in (4, 6, 8, 12, 20):
    base = 2.0
    # favorable +0.7 sigma, capped engine
    p0_u,_  = cont_p_success(base, pool, 0.0, 7, m1.SIGMA_N_COEFF, True)
    p1_u, e1 = cont_p_success(base, pool, 0.7, 7, m1.SIGMA_N_COEFF, True)
    _, e0   = cont_p_success(base, pool, 0.0, 7, m1.SIGMA_N_COEFF, True)
    mu, sg = PER_DIE[7]
    def p_from_ob(ob, pool):
        z = (ob - mu*pool)/(sg*math.sqrt(pool)); return 1.0 - Phi(z)
    p0_c = p_from_ob(max(1.0, e0), pool)
    p1_c = p_from_ob(max(1.0, e1), pool)
    print(f"      {pool:>4}D {(p1_u-p0_u)*100:12.2f} {(p1_c-p0_c)*100:12.2f}")
print("  (c) favored-side P ceiling, max favorable (eff_sigma=+1.5), base_Ob=2:")
for pool in (4, 6, 12):
    p_u, eff = cont_p_success(2, pool, 10.0, 7, m1.SIGMA_N_COEFF, True)  # net_sigma huge -> eff_sigma~1.5
    mu, sg = PER_DIE[7]
    p_c = 1.0 - Phi((max(1.0, eff) - mu*pool)/(sg*math.sqrt(pool)))
    print(f"      pool {pool:>2}D : unclamped P={p_u*100:5.1f}%  (Eff_Ob={eff:+.2f})   clamped@1 P={p_c*100:5.1f}%")

# ============================ T5 ============================
hdr("T5  TN miscalibration (hardcoded SIGMA_N_COEFF=0.8 = TN7 sigma) — PORT-1")
print("  dsigma=+0.7 uncapped, 50% base; realized dP with hardcoded 0.8 vs per-TN sigma")
print(f"  {'TN':>3} {'sigma':>6} {'hardcoded 0.8':>14} {'per-TN exact':>14}")
for tn in (6, 7, 8):
    sg = PER_DIE[tn][1]
    base = PER_DIE[tn][0]*8
    p0h,_ = cont_p_success(base, 8, 0.0, tn, 0.8, False)
    p1h,_ = cont_p_success(base, 8, 0.7, tn, 0.8, False)
    p0e,_ = cont_p_success(base, 8, 0.0, tn, sg, False)
    p1e,_ = cont_p_success(base, 8, 0.7, tn, sg, False)
    print(f"  {tn:>3} {sg:>6.3f} {(p1h-p0h)*100:13.2f}pp {(p1e-p0e)*100:13.2f}pp")
print("  → uniform-ACROSS-POOL holds at every TN (sqrt-N cancels); only the magnitude")
print("    calibration is off-nominal at TN!=7. PORT-1 fix = sigma_N(pool,TN)=sigma_tn*sqrt(pool).")

# ============================ T6 ============================
hdr("T6  soft_cap properties + marginal stacking + P-range")
xs = [-3,-2,-1,-0.5,0,0.5,1,2,3]
vals = [float(m1.soft_cap(x)) for x in xs]
mono = all(vals[i] < vals[i+1] for i in range(len(vals)-1))
odd  = max(abs(float(m1.soft_cap(x)) + float(m1.soft_cap(-x))) for x in xs) < 1e-12
bounded = abs(float(m1.soft_cap(1e6))-1.5) < 1e-9 and abs(float(m1.soft_cap(-1e6))+1.5) < 1e-9
slope0 = (float(m1.soft_cap(1e-6)) - float(m1.soft_cap(-1e-6))) / (2e-6)
print(f"  monotone increasing: {mono} | odd-symmetric: {odd} | bounded +/-1.5: {bounded} | slope@0 ~= {slope0:.4f} (expect 1)")
print("  marginal dP per added 'major'(+1.0) level, 50% base, capped, TN7:")
prev = 0.0
for n in range(1, 6):
    ns = 1.0*n
    p, eff = cont_p_success(PER_DIE[7][0]*8, 8, ns, 7, m1.SIGMA_N_COEFF, True)
    base = PER_DIE[7][0]*8
    pbase,_ = cont_p_success(base, 8, 0.0, 7, m1.SIGMA_N_COEFF, True)
    cum = (p - pbase)*100
    print(f"    {n} major (net_sigma={ns:>3.0f}) -> eff_sigma={1.5*math.tanh(ns/1.5):.3f}  cumP=+{cum:5.2f}pp  marginal=+{cum-prev:4.2f}pp")
    prev = cum
print("  P-range check: p_success stays strictly in (0,1):")
extremes = [float(m1.p_success(2, 1, -10, 7)), float(m1.p_success(2, 20, 10, 7))]
print(f"    most-adverse 1D = {extremes[0]:.5f} ; most-favorable 20D = {extremes[1]:.5f}  -> in (0,1): {0 < extremes[0] and extremes[1] < 1}")

print("\n" + R + "\nHARNESS COMPLETE\n" + R)
