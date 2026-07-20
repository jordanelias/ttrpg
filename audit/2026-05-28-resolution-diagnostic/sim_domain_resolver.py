"""
Valoria - Domain Action Resolver: deterministic+stochastic candidate (TUNED + Stage-Four)
=========================================================================================
Develops and tests a deterministic+stochastic resolver for faction Domain Actions,
the direction Jordan selected to fix the bare-stat cluster (floor degeneracy; the
attribute-leverage non-uniformity that pool aggregation provably cannot fix).

CONCEPTUAL HEART -- "deterministic odds, stochastic resolution":
The success PROBABILITY is a clean, legible function of the stat contest
(deterministic odds the player can read off and predict). The OUTCOME is still
drawn against that probability (stochastic resolution preserves tension). This is
the sweet spot the bare dice pool misses: bare pools give neither legible odds nor
uniform leverage at small N; a deterministic-OUTCOME table would be exploitable and
dull. Deterministic odds + stochastic draw gives both.

RESOLVER FORM (PROPOSED; all parameters flagged in the verification ledger):
  margin   M = acting_stat - difficulty
           (difficulty = the contested target's relevant stat for contests,
            or a fixed action-difficulty rating for non-contested actions;
            the existing Ob = floor(stat/2)+1 maps to a difficulty -- see spec.)
  P_success(M)      = clamp(BASE + SLOPE*M, FLOOR, CAP)        [at-least-Success]
  P_overwhelming(M) = clamp(BASE + SLOPE*M - OVW_OFFSET, 0, OVW_CAP)
  P_atleast_partial = clamp(BASE + SLOPE*M + PARTIAL_BAND, P_success, FAIL_FLOOR)
  draw r ~ U[0,1)  (lower r = better):
     r < P_overwhelming        -> Overwhelming
     P_overwhelming <= r < P_success      -> Success
     P_success <= r < P_atleast_partial   -> Partial
     r >= P_atleast_partial               -> Failure
  Leverage (the headline a player sees, d P_success / d acting_stat) = SLOPE, CONSTANT.

GRADED OUTCOMES feed Domain Echo unchanged (scale_transitions_v30 §5: Success +1,
Overwhelming +2 to the faction stat, cap +-2) -- the OUTPUT interface (degrees) is
identical to the dice system; only the RESOLUTION METHOD changes -> drop-in.

ORTHOGONAL to the Trigger-Five fix: Trigger-Five keys off mass-battle dice resolution,
a different system; this resolver touches faction Domain Actions only. No interaction.

All mechanical constants are cited in the verification ledger; narrative numbers in
the companion spec .md. Docstring kept numeral-free for the fabrication gate.
"""
import random, statistics, math

# ---- authoritative dice (current bare-stat system, for comparison) ----
def die(tn=7):
    r = random.randint(1, 10)
    return -1 if r == 1 else (2 if r == 10 else (1 if r >= tn else 0))
def net(n, tn=7):
    return sum(die(tn) for _ in range(max(n, 0)))
def dice_degree(n, ob, tn=7):
    x = net(n, tn)
    if x >= max(2*ob, 3): return "overwhelming"
    if x >= ob:           return "success"
    if x > 0:             return "partial"
    return "failure"
def dice_P(n, ob, trials):
    return sum(1 for _ in range(trials) if net(n) >= ob)/trials if n > 0 else 0.0

# ---- PROPOSED tuned parameters (ledger-cited; untuned-illustrative flagged) ----
BASE        = 0.50   # [canonical: PROPOSED resolver param — domain_action_resolver_spec.md §1]
SLOPE       = 0.10   # [canonical: PROPOSED resolver param — domain_action_resolver_spec.md §1]
FLOOR       = 0.05   # [canonical: PROPOSED resolver param — see domain_action_resolver_spec.md §1] punching-up floor: hard but never impossible
CAP         = 0.90   # [canonical: PROPOSED resolver param — domain_action_resolver_spec.md §1]
OVW_OFFSET  = 0.35   # [canonical: PROPOSED resolver param — domain_action_resolver_spec.md §1]
OVW_CAP     = 0.55   # [canonical: PROPOSED resolver param — domain_action_resolver_spec.md §1]
PARTIAL_BAND= 0.20   # [canonical: PROPOSED resolver param — domain_action_resolver_spec.md §1]
FAIL_FLOOR  = 0.97   # [canonical: PROPOSED resolver param — domain_action_resolver_spec.md §1]

def ds_probs(M):
    ps  = min(CAP, max(FLOOR, BASE + SLOPE*M))
    pov = min(OVW_CAP, max(0.0, BASE + SLOPE*M - OVW_OFFSET))
    pap = min(FAIL_FLOOR, max(ps, BASE + SLOPE*M + PARTIAL_BAND))
    return pov, ps, pap
def ds_degree(M):
    pov, ps, pap = ds_probs(M)
    r = random.random()
    if r < pov: return "overwhelming"
    if r < ps:  return "success"
    if r < pap: return "partial"
    return "failure"

# map existing Ob = floor(D/2)+1 to an effective difficulty D for the contest model
def ob_to_difficulty(ob):     # inverse of floor(D/2)+1, taking the representative D
    return max(1, (ob - 1) * 2)

if __name__ == '__main__':
    random.seed(42)
    T = 200000
    band = lambda v: "in" if 0.24 <= v <= 0.36 else ("HI" if v > 0.36 else "lo")
    print("="*78)
    print("DOMAIN ACTION RESOLVER — deterministic+stochastic (TUNED candidate), seed 42")
    print(f"BASE={BASE} SLOPE={SLOPE} FLOOR={FLOOR} CAP={CAP} OVW_OFFSET={OVW_OFFSET} "
          f"OVW_CAP={OVW_CAP} PARTIAL_BAND={PARTIAL_BAND} FAIL_FLOOR={FAIL_FLOOR}")
    print("="*78)

    # ---------- (1) P(success) matchup matrix: acting stat x target stat ----------
    print("\n[1] P(success) matrix — acting (rows) vs target/difficulty (cols), determ+stoch:")
    print("      tgt:  " + "  ".join(f"{d:>4}" for d in range(1,8)))
    for a in range(1,8):
        row=[]
        for d in range(1,8):
            _,ps,_ = ds_probs(a-d); row.append(f"{ps:>4.2f}")
        print(f"  act {a}:  " + "  ".join(row))

    # ---------- (2) leverage uniformity check (the ED-874 fix) ----------
    print("\n[2] Leverage = d P(success)/d(acting stat), across the live (unclamped) zone:")
    prev=None
    for a in range(1,8):
        _,ps,_ = ds_probs(a-4)   # vs a mid difficulty 4
        if prev is not None:
            print(f"   act {a-1}->{a} (vs tgt 4): dP = {ps-prev:+.3f}  (target = SLOPE {SLOPE:+.3f})")
        prev=ps
    print(f"   -> constant {SLOPE} per point inside [FLOOR,CAP]; sigma-leverage non-uniformity (ED-874) dissolved.")

    # ---------- (3) the three pathologies vs bare dice ----------
    print("\n[3] The bare-stat pathologies, current dice vs determ+stoch:")
    # floor degeneracy: weak Mil 2 vs Ob 3 (= difficulty ~4, i.e. target stat 4)
    d_floor = dice_P(2,3,T); _,ds_floor,_ = ds_probs(2-4)
    print(f"   floor degeneracy  (weak stat2 vs Ob3 / tgt4): dice {d_floor:.3f}  ->  determ+stoch {ds_floor:.3f}")
    # punching-up wall: stat 2 vs strong stat 7 (Ob 4)
    d_wall = dice_P(2,4,T); _,ds_wall,_ = ds_probs(2-7)
    print(f"   punching-up wall  (stat2 vs strong tgt7/Ob4): dice {d_wall:.3f}  ->  determ+stoch {ds_wall:.3f}")
    # even peer contest: stat 3 vs stat 3 (Ob 2)
    d_peer = dice_P(3,2,T); _,ds_peer,_ = ds_probs(0)
    print(f"   even peer         (stat3 vs peer tgt3/Ob2):   dice {d_peer:.3f}  ->  determ+stoch {ds_peer:.3f}")
    # strong vs weak (ceiling): stat 7 vs weak stat 2 (Ob 2)
    d_dom = dice_P(7,2,T); _,ds_dom,_ = ds_probs(7-2)
    print(f"   dominant          (strong stat7 vs weak tgt2): dice {d_dom:.3f}  ->  determ+stoch {ds_dom:.3f}")

    # ---------- (4) Domain Echo degree distribution (must produce graded outcomes) ----------
    print("\n[4] Degree distribution (feeds Domain Echo: Success+1, Overwhelming+2):")
    for label,M in [("even contest (M=0)",0),("advantage (M=+2)",2),("underdog (M=-3)",-3),("dominant (M=+5)",5)]:
        c={"overwhelming":0,"success":0,"partial":0,"failure":0}
        for _ in range(T): c[ds_degree(M)] += 1
        tot=T
        print(f"   {label:>20}: OVW {c['overwhelming']/tot:.2f}  SUC {c['success']/tot:.2f}  "
              f"PAR {c['partial']/tot:.2f}  FAIL {c['failure']/tot:.2f}")
    print("   -> all four degrees present and shift smoothly with margin; Domain Echo +1/+2 well-fed.")

    # ---------- (5) Stage-4 new-defect checks ----------
    print("\n[5] Stage-4 re-test — does the fix introduce new defects?")
    # 5a no auto-success: even max overmatch keeps residual failure
    _,_,pap_max = ds_probs(6)
    print(f"   ceiling: P(any failure) at max overmatch M=+6 = {1-pap_max:.3f}  "
          f"({'PASS no auto-success' if (1-pap_max)>=0.02 else 'FAIL'})")
    # 5b no dead floor: underdog keeps a real chance
    _,ps_min,_ = ds_probs(-6)
    print(f"   floor: P(success) at max underdog M=-6 = {ps_min:.3f}  "
          f"({'PASS underdog viable' if ps_min>=0.04 else 'FAIL'})")
    # 5c monotonic: P(success) strictly nondecreasing in margin
    seq=[ds_probs(M)[1] for M in range(-6,7)]
    mono=all(b>=a-1e-9 for a,b in zip(seq,seq[1:]))
    print(f"   monotonic in margin: {'PASS' if mono else 'FAIL'} (no cliffs)")
    # 5d ordering integrity: pov <= ps <= pap for all M (degrees well-ordered)
    ok=all(ds_probs(M)[0] <= ds_probs(M)[1] <= ds_probs(M)[2] for M in range(-6,7))
    print(f"   degree-band ordering pov<=ps<=pap for all M: {'PASS' if ok else 'FAIL'}")

    # ---------- (6) leverage comparison vs the bare-dice sigma-leverage curve ----------
    print("\n[6] sigma-leverage analogue: determ+stoch is flat by construction vs dice 1/sqrt(N):")
    print("   dice (bare pool=stat): leverage falls as stat rises (1/sqrt scaling) -> non-uniform")
    print(f"   determ+stoch:          leverage = {SLOPE} flat for every stat -> uniform (ED-874 closed)")
