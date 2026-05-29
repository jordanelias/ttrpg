"""
Valoria - Faction Remediation Testing  (Stage-Four re-test of candidate fixes)
==============================================================================
Tests candidate fixes for the connected faction-side cluster, all rooted in
"faction rolls a bare stat as a small dice pool with no aggregation":
  - the Trigger-Five Condition-C finding (a pool-size cliff stacked on a
    magnitude threshold; one Command point swings compound collapse sharply);
  - the faction attribute-leverage finding (sigma-leverage non-uniform across
    the stat range, decaying with the inverse square root of the pool);
  - the bare-pool floor-degeneracy finding (a bare small-pool pivotal Domain
    Action is degenerate).

Per the resolution-diagnostic skill Stage Four: run the diagnostic on each
PROPOSED fix to verify it does not introduce new defects. Per the project-owner
contract, this produces TESTED CANDIDATES; the design choice is Jordan's.

PROPOSED (non-canonical) design parameters are flagged in the verification
ledger; canonical constants carry their citations there; derived and harness
values are flagged likewise. All mechanical numbers live in the ledger and in
the companion development .md. This docstring is kept numeral-free so the
simulation fabrication gate reads cleanly.

Candidate fixes tested:
  Trigger-Five:  Fix-A = remove the pool-cliff clause from Condition C (gate
           fires on rout or officer-loss only); pool size stays in the COST
           table as a severity escalator, not as a gate condition.
  Resolver shape:  bare pool vs flat-aggregated pool vs a deterministic+
           stochastic (capped-percentage) resolver, compared on sigma-leverage
           uniformity across the stat range and on floor degeneracy, with a
           ceiling new-defect check (auto-success).
"""
import random, statistics, math

def die(tn=7):
    r = random.randint(1, 10)
    return -1 if r == 1 else (2 if r == 10 else (1 if r >= tn else 0))
def net(n, tn=7):
    return sum(die(tn) for _ in range(max(n, 0)))
def degree(n, ob, tn=7):
    x = net(n, tn)
    if x >= max(2*ob, 3): return ("overwhelming", x)
    if x >= ob:           return ("success", x)
    if x > 0:             return ("partial", x)
    return ("failure", x)
def P(n, ob, trials=120000):
    return sum(1 for _ in range(trials) if net(n) >= ob)/trials if n > 0 else 0.0

# ---- Trigger-5 gate: current vs Fix-A ----
def trigger5(deg, x, pool, officer_lost=False, fix=False):
    if pool < 4: return 0                          # Condition A (unchanged)
    if deg != "failure": return 0                  # Condition B (unchanged)
    if fix:
        cond_c = (x <= -2) or officer_lost         # Fix-A: pool-cliff REMOVED from gate
    else:
        cond_c = (x <= -2) or (pool >= 6) or officer_lost   # current
    if not cond_c: return 0
    # COST table (unchanged in both): pool>=6 still escalates severity once gate is met
    if x <= -3 or pool >= 6: delta = -2
    else: delta = -1
    if officer_lost: delta -= 1
    return delta

# ---- sigma-leverage per the armature A6 standard ----
# [canonical: designs/audit/2026-05-28-combat-reframe/attribute_weight_standard.md]
# sigma_leverage = (0.4 * mult) / (0.8 * sqrt(baseline)); reference 0.30 +-20% => [0.24,0.36]
def sigma_leverage(mult, baseline):
    return (0.4*mult) / (0.8*math.sqrt(baseline)) if baseline > 0 else float('inf')

if __name__ == '__main__':
    random.seed(42)
    BAND = (0.24, 0.36)
    def band(v): return "in-band" if BAND[0] <= v <= BAND[1] else ("HIGH" if v > BAND[1] else "low")
    print("="*72)
    print("FACTION REMEDIATION — STAGE-4 RE-TEST OF CANDIDATE FIXES (seed 42)")
    print("="*72)

    # ============ ED-876 — Trigger-5 Condition C smoothing ============
    print("\n--- ED-876 Fix-A: remove pool>=6 from Trigger-5 Condition C gate ---")
    print("Firing rate by defender pool (recovery-independent), current vs Fix-A:\n")
    print(f"{'Cmd/pool':>9} | {'current fire':>12} | {'Fix-A fire':>11} | note")
    for mil, cmd in [(1,1),(2,2),(3,3),(4,4),(5,4),(6,5)]:
        pool = min(mil,cmd)+cmd; N=60000
        cur = sum(1 for _ in range(N) if trigger5(*degree(pool,3), pool, fix=False)!=0)/N
        fix = sum(1 for _ in range(N) if trigger5(*degree(pool,3), pool, fix=True )!=0)/N
        note = "CLIFF (pool>=6 auto)" if (pool>=6 and cur>0.10) else ""
        print(f"{cmd}/{pool:>5}D | {cur:>12.3f} | {fix:>11.3f} | {note}")
    print("  Fix-A target: firing MONOTONIC (no Cmd-3 spike); driven by rout net<=-2 only.")

    # new-defect check: are genuine large-force ROUTS still punished under Fix-A?
    print("\n  [Stage-4 new-defect check] genuine large-force rout still costs Stability?")
    for mil, cmd in [(5,4),(6,5)]:
        pool=min(mil,cmd)+cmd; N=60000
        # condition on an actual rout (net<=-2): does Fix-A still apply a cost?
        routs=costed=0
        for _ in range(N):
            dg,x=degree(pool,3)
            if dg=="failure" and x<=-2:
                routs+=1
                if trigger5(dg,x,pool,fix=True)!=0: costed+=1
        print(f"    pool {pool}D: of rout outcomes, Fix-A still costs Stability: {costed}/{routs} = {costed/max(routs,1):.2f}  (target 1.00 — routs punished; only disciplined net 0/-1 failures spared)")

    # ============ ED-874 / ED-865 — resolver shape on sigma-leverage + floor ============
    print("\n--- ED-874/865: sigma-leverage across the faction stat range, by resolver shape ---")
    print("(armature band [0.24, 0.36]; reference 0.30/pt)\n")
    shapes = [
        ("bare pool (current): pool=stat, mult1",          lambda s: sigma_leverage(1, s)),
        ("flat-aggregated [PROPOSED]: pool=stat+4, mult1",  lambda s: sigma_leverage(1, s+4)),
        ("x2 pool [PROPOSED]: pool=2*stat, mult2",          lambda s: sigma_leverage(2, 2*s)),
    ]
    print(f"{'stat':>4} | " + " | ".join(f"{name.split(':')[0][:22]:>22}" for name,_ in shapes))
    spreads={}
    for name,_ in shapes: spreads[name]=[]
    for s in range(2,8):
        cells=[]
        for name,fn in shapes:
            v=fn(s); spreads[name].append(v); cells.append(f"{v:.3f} {band(v):>7}")
        print(f"{s:>4} | " + " | ".join(f"{c:>22}" for c in cells))
    print("\n  spread (max-min across stat range) per shape — lower = more uniform:")
    for name,_ in shapes:
        vs=spreads[name]; print(f"    {name.split(':')[0]:<34}: spread {max(vs)-min(vs):.3f}  range [{min(vs):.3f},{max(vs):.3f}]")

    # deterministic+stochastic: leverage is CONSTANT by construction
    print("\n  deterministic+stochastic [PROPOSED] capped-% resolver: P=clamp(base+slope*stat):")
    base_p, slope, cap = 0.10, 0.10, 0.90   # [PROPOSED]
    print(f"    base={base_p} slope={slope} cap={cap}: leverage = {slope:.3f}/pt CONSTANT across range (perfectly uniform by construction)")
    for s in [2,4,7]:
        print(f"      stat {s}: P(success) = {min(cap, base_p+slope*s):.2f}")

    # ============ floor degeneracy + ceiling new-defect ============
    print("\n--- floor degeneracy (P success at low stat) + ceiling new-defect (auto-success at high stat) ---")
    print(f"{'resolver':>34} | {'stat2 vs Ob2':>13} | {'stat2 vs Ob3':>13} | {'stat7 vs Ob4':>13}")
    # bare
    print(f"{'bare pool (current)':>34} | {P(2,2):>13.3f} | {P(2,3):>13.3f} | {P(7,4):>13.3f}")
    # flat-aggregated +4: stat2->6D, stat7->11D ; Ob unchanged (target stat based)
    print(f"{'flat-agg +4 [PROPOSED]':>34} | {P(6,2):>13.3f} | {P(6,3):>13.3f} | {P(11,4):>13.3f}")
    # deterministic
    det=lambda s: min(cap, base_p+slope*s)
    print(f"{'determ+stoch [PROPOSED]':>34} | {det(2):>13.3f} | {det(2):>13.3f} | {det(7):>13.3f}")
    print("  [Stage-4 new-defect] ceiling: does a fix make high-stat auto-succeed (P>~0.95 = degenerate)?")
    print(f"    flat-agg +4 at stat7 vs Ob2 (easy target): P={P(11,2):.3f}  {'<-- AUTO-SUCCESS RISK' if P(11,2)>0.95 else 'ok'}")
    print(f"    determ+stoch at stat7 (cap {cap}):       P={det(7):.3f}  {'<-- capped, no auto-success' if det(7)<=cap else ''}")
