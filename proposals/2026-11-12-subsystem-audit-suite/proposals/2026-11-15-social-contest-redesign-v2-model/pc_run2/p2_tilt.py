"""P2.3-5: tilt vs power gap x rig; equal and weaker arrangers; mirror; is the rig seen and priced (fold)."""
import sys
from collections import Counter
from common import *

N = int(sys.argv[1]) if len(sys.argv) > 1 else 600
M = F.matter()
BENCH = ("j1", "j2", "j3")
FLOOR = ("crowd",)


def cast_with(a_rung=None, b_rung=None, fa="Crown", fb="Crown"):
    pp = F.mid_people()
    pp["a"]["faction"], pp["b"]["faction"] = fa, fb
    if a_rung is not None: pp["a"]["office"] = F.seat(a_rung, fa)
    if b_rung is not None: pp["b"]["office"] = F.seat(b_rung, fb)
    pp["j2"]["layers"] = dict(relationships={"a": 0.6, "b": -0.0})
    pp["j3"]["layers"] = dict(relationships={"b": 0.6})
    return pp


def arm(pp, arranger, rig, side_of_arr, n=N, regime="crown", tag=""):
    car = 0; legit = 0.0; app = 0; rg = 0; card0 = None; regard_loser = 0.0; lost_arr = 0; app_when_arr_side_lost = 0
    for i in range(n):
        inp, card, out, b = sit(pp, "trial", M, ("tilt", tag, i), bench=BENCH, floor=FLOOR, effort=3, arranger=arranger, rig=rig, regime=regime)
        card0 = card0 or card
        won_for = b[0] in CARRIED
        arr_won = won_for if side_of_arr == "for" else not won_for
        car += arr_won
        w = host.new_world(); band, wr = host.fold(w, pp, inp, card, out, M)
        legit += sum(v for k, v in w["legitimacy"].items() if k == pp[card.arranged_by].get("faction")) if False else 0
        # isolate the rig price: the write tagged legitimacy- for the arranger's faction from the rigged-forum clause
        app += any(d[1] == "appeal" for d in w["docket"])
        if not arr_won:
            app_when_arr_side_lost += any(d[1] == "appeal" for d in w["docket"])
            lost_arr += 1
        rg += sum(1 for l in w["ledgers"].values() for e in l if e[0] == "rigged")
    return card0, car / n, app / n, rg / n, (app_when_arr_side_lost, lost_arr)


def rig_price(card, pp):
    """the fold's rig clause, read off directly: tilt * min(1, seen/12) with seen = room weight less the arranger."""
    seen = sum(w for pid, role, pw in card.room for w in [pp[pid].get("weight", 1)] if pid != card.arranged_by)
    return card.tilt * min(1.0, seen / 12.0), seen


print(f"n={N} per arm; trial, bench j1..j3 (Crown rung 3; j2 tied to a +0.6, j3 tied to b +0.6), floor crowd (weight 30), effort 3")
print("== P2.3/P2.4 sweep: a (for) arranges; b holds no office. gap = power(a)-power(b)")
print(" a_rung | gap | rig | tilt | presiding | floor | turns | P(a's side carried) +- se | rig price (tilt*seen/12) | seen | rigged claims/sitting | appeal rate")
base = {}
for a_rung in (None, 0, 1, 2, 4, 6):
    pp = cast_with(a_rung=a_rung)
    gap = host.power(pp["a"]) - host.power(pp["b"])
    for rig in (0.0, 0.5, 1.0):
        card, p, app, rg, _ = arm(pp, "a", rig, "for", tag=(a_rung, rig))
        price, seen = rig_price(card, pp)
        fl = sum(1 for x in card.room if x[1] == "attends")
        print(f"  {str(a_rung):5} | {gap:3.0f} | {rig:.1f} | {card.tilt:.2f} | {card.decided_by} | {fl} | {card.turns} | {p:.3f}+-{se(p,N):.3f} | {price:.3f} | {seen} | {rg:.2f} | {app:.2f}")

print("\n== equal power (both rung 3), and the weaker arranging (b rung 0 arranges against a rung 4)")
pp = cast_with(a_rung=3, b_rung=3)
for rig in (0.0, 1.0):
    card, p, app, rg, _ = arm(pp, "a", rig, "for", tag=("eq", rig))
    print(f"  equal, a arranges, rig {rig}: tilt {card.tilt} P(a) {p:.3f}+-{se(p,N):.3f} appeal {app:.2f} rigged/sitting {rg:.2f}")
pp = cast_with(a_rung=4, b_rung=0)
for rig in (0.0, 1.0):
    card, p, app, rg, _ = arm(pp, "b", rig, "against", tag=("weak", rig))
    print(f"  weaker b arranges vs a rung 4, rig {rig}: arranged_by {card.arranged_by} tilt {card.tilt} P(b) {p:.3f}+-{se(p,N):.3f}")

print("\n== MIRROR: the powerful party arranges, on side `for` vs side `against` (rung 4 vs none); effect = P(arranger's side | rig) - P(| rig 0)")
for lab, pp, arr, side in (("for powerful", cast_with(a_rung=4), "a", "for"), ("against powerful", cast_with(b_rung=4), "b", "against")):
    r = {}
    for rig in (0.0, 0.5, 1.0):
        card, p, *_ = arm(pp, arr, rig, side, tag=("mir", lab, rig)); r[rig] = (p, card.tilt)
    d5, d1 = r[0.5][0] - r[0.0][0], r[1.0][0] - r[0.0][0]
    print(f"  {lab:17} P(arr side) rig0 {r[0.0][0]:.3f} rig.5 {r[0.5][0]:.3f} (tilt {r[0.5][1]}) rig1 {r[1.0][0]:.3f} (tilt {r[1.0][1]}) | effect .5 {d5:+.3f} 1 {d1:+.3f} (band +-{2*math.sqrt(2*0.25/N):.3f})")

print("\n== third-party arranger: the presiding seat's superior j? use a Crown rung-6 lord 'lord' tied to a")
pp = cast_with()
pp["lord"] = F.P("lord", office=F.seat(6, "Crown"), faction="Crown", layers=dict(relationships={"a": 0.8}))
for rig in (0.0, 1.0):
    card, p, app, rg, (al, lost) = arm(pp, "lord", rig, "for", tag=("lord", rig))
    print(f"  lord arranges for a, rig {rig}: tilt {card.tilt} P(a) {p:.3f}; appeals docketed when a (the FAVOURED side) lost: {al}/{lost}")

print("\n== who resents whom after a rigged loss: arranger a (rung 4) loses at rig 1 -> regard(a->b) 'lost to him'")
pp = cast_with(a_rung=4)
for rig in (0.0, 1.0):
    vals_arr_lost, vals_weak_lost = [], []
    for i in range(N):
        inp, card, out, b = sit(pp, "trial", M, ("res", rig, i), bench=BENCH, floor=FLOOR, effort=3, arranger="a", rig=rig)
        w = host.new_world(); band, wr = host.fold(w, pp, inp, card, out, M)
        lost = [x for x in wr if x[0].startswith("regard") and x[3] == "lost to him"]
        if b[0] in CARRIED:
            vals_weak_lost.append(w["regard"].get(("b", "a"), 0.0))
        else:
            vals_arr_lost.append(w["regard"].get(("a", "b"), 0.0))
    m = lambda xs: sum(xs) / max(1, len(xs))
    print(f"  rig {rig}: weak b lost (n={len(vals_weak_lost)}): regard b->a {m(vals_weak_lost):+.3f}; arranger a lost (n={len(vals_arr_lost)}): regard a->b {m(vals_arr_lost):+.3f}")
