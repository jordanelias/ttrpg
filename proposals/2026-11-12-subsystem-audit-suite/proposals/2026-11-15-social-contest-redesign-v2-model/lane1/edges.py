"""Probes 2-5: blend table edges, saturation, degenerate numbers, draw discipline. Deterministic checks.
usage: PYTHONHASHSEED=0 python lane1/edges.py"""
import sys, os, math, copy, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harness import sitting, base_people, SCEN, mid
from scmodel import dials, proceeding as P, dice
from scmodel.dice import weighted_tenth, net_boost, _cap, MU_PER_DIE
from scmodel.records import Choice
from scmodel.rng import Draw
from engine.dice_engine.sigma_leverage import soft_cap

S = dials.shipped()

print("== (2) blend: k per (content class, venue) at shipped")
from scmodel import data
for row in data.ROW_IDS:
    ks = {c: min(10, max(0, round(10 * w) + round(10 * S['reason_bias'][row]))) for c, w in S['content_w_reason'].items()}
    raw = {c: round(10 * w) + round(10 * S['reason_bias'][row]) for c, w in S['content_w_reason'].items()}
    clipped = [c for c in ks if ks[c] != raw[c]]
    print(f"  {row:30} k={ks} clipped={clipped}")
print("  banker's rounding in weighted_tenth (s=4.25 vs 4.35 at k=10):", weighted_tenth((4.25, 0), (10, 0)),
      weighted_tenth((4.35, 0), (10, 0)), " (half-up would give 4.3, 4.4)")
print("  round(10*c) at c=0.25 (banker):", round(10 * 0.25), " c=0.35:", round(10 * 0.35))

print("\n== (2) proof_weight exactly 0 and 1: does anything refuse? (full legal_trial, bench room overridden)")
for pw in (0.0, 1.0):
    ar = {k: dict(v) for k, v in S['audience_room'].items()}
    for k in ar:
        ar[k]['proof_weight'] = pw
    D = dials.shipped(audience_room=ar)
    try:
        inp, out, band = sitting("bench_full", base_people(), D, ("pw", 0))
        print(f"  pw={pw}: ran, band={band}")
    except Exception as e:
        print(f"  pw={pw}: {type(e).__name__}: {e}")

print("\n== (3) saturation: soft-cap marginal sech^2(sigma/1.5) at the speech sigma reached")
def speech_sigma(scen, people, D, ground="evidence"):
    row, form, sc, _ = SCEN[scen]
    from scmodel.host import build_input
    inp = build_input(people, row, form, "argue", actor="a", dials=D, effort=2, **sc)
    st = P._start(inp)
    T, j = P._target(inp, 0)
    x, lv, pre, h = P._speech_input(inp, 0, st.sides[0], T, P._move_by_id(inp, "argue"), ground, True)
    return x.leverage, lv, x.pool
for label, kw, proofs in (("all-mid, proofs 2", {}, 2.0), ("Reason 7 Presence 7 Grace 7, proofs 4", dict(reason=7, presence=7, grace=7), 4.0)):
    for scen in ("private_abr", "bench_full", "crowd_full"):
        pp = base_people(proofs=proofs); pp["a"]["attributes"].update(kw)
        sig, lv, pool = speech_sigma(scen, pp, S)
        marg = 1 - math.tanh(sig / 1.5) ** 2
        print(f"  {label:38} {scen:12} sigma={sig:+.3f} soft_cap={soft_cap(sig):.3f} marginal={marg:.3f} pool={pool:.2f} "
              f"levels={[(n, round(f,3), round(a,3)) for n,f,a in lv if f or a]}")
# ballot: full track + lean + modifier
print("  ballot sigma at track +3 (0.9) with a hostile hearer stance -1 (lean -1.0):", 0.9 - 1.0,
      "; with friendly +1:", 0.9 + 1.0, "-> soft_cap", round(soft_cap(1.9), 3))

print("\n== (3) usable proofs cap vs Reason (proofs held 4, bench pw .75): proofs sigma")
for r in range(1, 8):
    print(f"  Reason {r}: {P._proofs_source(type('S', (), dict(proofs=4.0, reason=r))(), type('R', (), dict(proof_weight=0.75))(), S)[0]:.3f}", end=";")
print()
print("  shield/account/cover at attribute 7 and 1:",
      [P._shield(type('S', (), dict(will=w))(), S) for w in (1, 7)], [P._account(type('S', (), dict(reason=w))(), S) for w in (1, 7)],
      [P._cover(type('S', (), dict(grace=w))(), S) for w in (1, 7)])
print("  heard at crowd (attention 5) Presence 1..7:", [P._heard(type('S', (), dict(presence=p))(), type('R', (), dict(attention=5.0))(), type('T', (), dict(order='alternating'))(), S) for p in range(1, 8)])

print("\n== (4) obstacle cap vs refusal multiple 2*pool: min over p in [1,40] of 2p - cap(p) (ceiling 2):",
      round(min(2 * p / 10 - _cap(p / 10, 2.0, True) for p in range(10, 400)), 3),
      "; obstacle() reads obstacle_refusal_multiple:", "obstacle_refusal_multiple" in dice.obstacle.__code__.co_names)
print("  heard floor below pool_floor: min pool = pool_floor*heard_floor =", S['pool_floor'] * S['heard_floor'])
print("  bench seat pool (rank 1): judging =", max(1, S['pool_default']), "; hearer base pool =", dice.pool_of(2, 0, 6, 5))
# rally to nobody
try:
    from scmodel.host import build_input
    inp = build_input(base_people(), "rally", "full", actor="a", addressed=None, present=(), dials=S, effort=2)
    out = P.proceed(inp, Draw(0))
    print("  rally with nobody present: ran", out.ended)
except Exception as e:
    print(f"  rally with nobody present: {type(e).__name__}: {e}")
# NaN / negative scan over many sittings at extremes
bad = 0; cnt = 0
for v in (1, 7):
    pp = base_people(); [pp[i]["attributes"].update({k: v for k in pp[i]["attributes"]}) for i in pp]
    for scen in SCEN:
        for i in range(300):
            inp, out, band = sitting(scen, pp, S, ("nan", i))
            for x in out.exchanges:
                cnt += 1
                if not math.isfinite(x.margin) or any(not math.isfinite(t) for _, t in x.terms):
                    bad += 1
            for s in out.state.sides:
                if s.pull < 0 or s.marks < 0 or not math.isfinite(s.resolve):
                    bad += 1
print(f"  NaN/inf/negative-pull scan at all-1 and all-7 people, 6 scenarios x 300: {bad} bad of {cnt} exchanges")

print("\n== (5) draw discipline: determinism and offset independence")
def logged_run(decide=None, key=("dd", 3)):
    vals = []
    class LD(Draw):
        def normal(self, mu=0.0, sd=1.0):
            v = super().normal(0.0, 1.0); vals.append(v); return mu + sd * v
    row, form, sc, _ = SCEN["bench_full"]
    from scmodel.host import build_input
    inp = build_input(base_people(), row, form, actor="a", dials=S, effort=4, **sc)
    out = P.proceed(inp, LD(key, "a", "x"), decide)
    return vals, out
v1, o1 = logged_run()
def pressy(view):
    return Choice("press", "evidence") if "press" in view.legal else Choice(view.legal[0], None)
v2, o2 = logged_run(pressy)
G = 4
k = min(len(o1.exchanges), len(o2.exchanges))
same = all(v1[e * (G + 5):(e + 1) * (G + 5)] == v2[e * (G + 5):(e + 1) * (G + 5)] for e in range(k))
print(f"  argue-policy vs press-policy, same key: exchanges {len(o1.exchanges)} vs {len(o2.exchanges)}; "
      f"first {k} exchanges' normal blocks identical: {same}")
h = hashlib.sha256(repr([(x.mover, x.move, round(x.margin, 12)) for x in o1.exchanges]).encode()).hexdigest()[:16]
print(f"  outcome hash (compare across PYTHONHASHSEED): {h}")
