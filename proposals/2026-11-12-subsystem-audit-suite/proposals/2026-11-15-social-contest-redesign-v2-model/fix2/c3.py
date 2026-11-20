"""C3: the rig's price; every rig level best somewhere; arranger tilt from power; resentment and appeals follow the
grievance; the weak party's options (D1); the loser's acts (D3)."""
from common import *
from sc2 import acts
N = int(sys.argv[1]) if len(sys.argv) > 1 else 400
FLOOR = ("crowd",)
def cast_with(a_rung=None, b_rung=None, fa="Crown", fb="Crown"):
    pp = F.mid_people()
    pp["a"]["faction"], pp["b"]["faction"] = fa, fb
    if a_rung is not None: pp["a"]["office"] = F.seat(a_rung, fa)
    if b_rung is not None: pp["b"]["office"] = F.seat(b_rung, fb)
    pp["j2"]["layers"] = dict(relationships={"a": 0.6})
    pp["j3"]["layers"] = dict(relationships={"b": 0.6})
    return pp

H(f"C3.1 a (for) arranges against b (no office): tilt, seats, watchers, turns, P(a carried), the price (n={N})")
print("  gap | rig | tilt | presiding | watchers | turns | P(a)  | price (legitimacy) ")
res = {}
for rung in (None, 1, 4):
    pp = cast_with(a_rung=rung)
    for rig in (0.0, 0.5, 1.0):
        inp, card = host.build(pp, "trial", M, bench=BENCH, floor=FLOOR, effort=3, arranger="a", rig=rig)
        p = carried(pp, "trial", M, N, "c3a", bench=BENCH, floor=FLOOR, effort=3, arranger="a", rig=rig)
        gap = host.power(pp["a"]) - host.power(pp["b"])
        res[(rung, rig)] = (p, host.rig_price(card.tilt))
        print(f"  {gap:3.0f} | {rig:.1f} | {card.tilt:.2f} | {[q.id for q in inp.room if q.decides]} | {sum(q.weight for q in inp.room if q.side is None and not q.decides):3d} | {card.turns} | {p:.3f} | {host.rig_price(card.tilt):.3f}")

H("C3.2 every rig level best somewhere: the arranger's reckoning 2 x stake x P(carried) - price, by his case and his stake (gap 5)")
for ra in (1, 4, 7):
    pp = cast_with(a_rung=4); pp["a"]["attributes"]["reason"] = ra
    ps = {rig: carried(pp, "trial", M, N, "c3b", bench=BENCH, floor=FLOOR, effort=3, arranger="a", rig=rig) for rig in (0.0, 0.5, 1.0)}
    pr = {rig: host.rig_price(host.build(pp, "trial", M, bench=BENCH, floor=FLOOR, effort=3, arranger="a", rig=rig)[1].tilt) for rig in ps}
    best = {st: max(ps, key=lambda r: 2 * st * ps[r] - pr[r]) for st in (0.5, 1.0, 2.0, 4.0)}
    print(f"  a Reason {ra}: P(a) by rig {', '.join(f'{r}: {ps[r]:.3f}' for r in ps)}; best rig at stake 0.5/1/2/4: {list(best.values())}")

H("C3.3 who arranges: tilt from power, not from a tie (the accused, rung 4, arranges against a commoner accuser)")
for tie_ in (-0.1, 0.0, 0.3):
    pp = cast_with(b_rung=4); pp["b"]["layers"] = dict(relationships={"a": tie_})
    inp, card = host.build(pp, "trial", M, bench=BENCH, floor=FLOOR, effort=3, arranger="b", rig=1.0)
    print(f"  b's tie to a {tie_:+.1f}: tilt {card.tilt}, tilted against `{card.tilted_against}`, card names {card.arranged_by}")
inp, card = host.build(cast_with(), "trial", M, bench=BENCH, effort=3, arranger="a", rig=1.0)
print(f"  equals, a arranges at rig 1: tilt {card.tilt}, the card names {card.arranged_by!r}")

H(f"C3.4 after a rigged loss: who resents whom; who may appeal (gap 5, rig 1; n={N})")
pp = cast_with(a_rung=4)
pp["lord"] = F.P("lord", office=F.seat(6, "Crown"), layers=dict(relationships={"a": 0.8}))
rows = Counter(); regd = defaultdict(list)
for i in range(N):
    for arr in ("a", "lord"):
        inp, card, out, b = sit(pp, "trial", M, ("c3d", arr, i), bench=BENCH, floor=FLOOR, effort=3, arranger=arr, rig=1.0)
        w = host.new_world(); band, _ = host.fold(w, pp, inp, card, out, M)
        act, opts = acts.after(w, pp, inp, card, out, M, band)
        a_lost = band not in CARRIED
        if band == "partial": continue
        rows[(arr, "a lost" if a_lost else "b lost", act)] += 1
        loser, winner = ("a", "b") if a_lost else ("b", "a")
        regd[(arr, "loser->winner", "a lost" if a_lost else "b lost")].append(w["regard"].get((loser, winner), 0.0))
        regd[(arr, "loser->judge", "a lost" if a_lost else "b lost")].append(w["regard"].get((loser, inp.room[[q.decides for q in inp.room].index(True)].id), 0.0))
for k in sorted(rows): print(f"  arranger {k[0]:4s} {k[1]:7s} -> the loser {k[2]}: {rows[k]}")
for k in sorted(regd): print(f"  arranger {k[0]:4s} {k[1]:14s} when {k[2]}: mean regard {sum(regd[k])/len(regd[k]):+.3f} (n={len(regd[k])})")

H(f"C3.5 D1: the weak party's options before a tilted forum (gap 5): what he is shown and what he takes (n={N // 4})")
for alt in ((), ("c1", "c2")):
    for rig in (0.5, 1.0):
        for stb in (0.0, 0.5, 1.0):
            pp2 = cast_with(a_rung=4); pp2["b"]["layers"] = dict(pursuits={"x": stb}, convictions={"x": 5 * stb}) if stb else {}
            m5 = dict(M, bears={"x": -1.0})
            act, r2, dk, opts = acts.before(pp2, "trial", m5, arranger="a", rig=rig, alt_bench=alt, bench=BENCH, floor=FLOOR, effort=3)
            print(f"  {'another authority sits' if alt else 'no other forum'}; rig {rig}; what the charge costs b {stb}: {[(o[0], round(o[1], 3)) for o in opts]} -> {act}")
