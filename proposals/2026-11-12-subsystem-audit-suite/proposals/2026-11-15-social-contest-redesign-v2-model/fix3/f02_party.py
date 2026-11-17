"""F2 a party who also decides (stress lane A pj2/pj3/yieldseat/det, lane C roles R-a..R-c).
PREDICTION after: a party who is the one seat has a stake toward his own side (>= PARTY_STAKE), is recorded partial
and priced when he rules his way; with a backup seat he steps down; a seated party's yield is one vote, so his yield
rate sits near an unseated party's and P(for) near the neutral bench. Before: stake 0, no ledger, a seated party
yields ~20 %.  python -B f02_party.py N"""
from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 600
pp = castB(pa="r3", pb="r3", fac_person=False)
m = mat()
H("F2a a party who is the one seat (trial)")
for bench in (("j1",), ("a",), ("b",), ("a", "j1")):
    inp, card = host.build(pp, "trial", m, bench=bench, effort=3)
    d = [p for p in inp.room if p.decides][0]
    car = part = paid = 0
    for i in range(N):
        inp, card, out, b = sit(pp, "trial", m, ("pj", i), bench=bench, effort=3)
        w = host.new_world(); band, wr = host.fold(w, pp, inp, card, out, m)
        car += band in CARRIED; part += any(x[0] == "partial" for L in w["ledgers"].values() for x in L); paid += any(x[0] == "partial_paid" for x in wr)
    print(f"  bench {str(bench):12} decided {card.decided_by} recused {card.recused} stake {tuple(round(x, 2) for x in d.stake)} start {d.start:+.2f} | P(for) {pc(car, N)} | partial on a ledger {part}/{N} | priced {paid}/{N}")
H("F2b a seated party's yield on a shared close (debate, quorum 2; tribunal)")
for rite in ("debate", "tribunal"):
    for bench in (("j1", "j2"), ("b", "j1"), ("a", "j1"), ("j1", "j2", "j3"), ("b", "j1", "j2")):
        try:
            host.build(pp, rite, m, bench=bench, effort=3)
        except ValueError as e:
            print(f"  {rite:8} bench {str(bench):16} {str(e)[:40]}"); continue
        car = yb = ya = 0
        for i in range(N):
            inp, card, out, b = sit(pp, rite, m, ("ys", i), bench=bench, effort=3)
            car += b[0] in CARRIED; yb += out.ended == "yielded" and out.ended_by == "b"; ya += out.ended == "yielded" and out.ended_by == "a"
        print(f"  {rite:8} bench {str(bench):16} seats {card.decided_by} recused {card.recused} | P(for) {pc(car, N)} | b yields {yb/N:.3f}, a yields {ya/N:.3f}")
H("F2c the season driver's worths read the bearing's floor (acts._stake)")
print(f"  a flat matter: stake of a {acts._stake(pp, 'a', m):.2f}, of b {acts._stake(pp, 'b', m):.2f}; effort_of a {host.effort_of(pp['a'], m, pp)}")
