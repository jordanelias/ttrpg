"""F11 a third party's rig and the rally's resentment (stress lane B probe_rig, grid1's 'tilt between equals', B8).
PREDICTION after: a third party with no tie to either side tilts nothing and is not named; tied to one side he leans
to it; a rally's opposing party (no moves) rigged against and losing resents the arranger.  python -B f11_third.py N"""
from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 400
H("F11a a third party t (r5M) arranges a trial between a and b (both r2) at rig 1")
for lab, lay in (("no tie", {}), ("tied to b +0.6", dict(relationships={"b": 0.6})), ("tied to a +0.6", dict(relationships={"a": 0.6}))):
    pp = castB(pa="r2", pb="r2", pt="r5M", seat_fac="Parliament"); pp["t"]["layers"] = lay
    inp, card = host.build(pp, "trial", mat(), bench=BENCH, arranger="t", rig=1.0, effort=2)
    k = sum(sit(pp, "trial", mat(), ("tp", i), bench=BENCH, arranger="t", rig=1.0, effort=2)[3][0] in CARRIED for i in range(N))
    print(f"  {lab:16} tilt {card.tilt} arranged_by {card.arranged_by} against {card.tilted_against} | P(for) {pc(k, N)}")
H("F11b a rally: a (r5M) urges, b (r2) the opposing party with no moves; b's regard for the arranger after a loss")
for who in ("a", "b"):
    pp = castB(pa="r5M", pb="r2", seat_fac="Parliament") if who == "a" else castB(pa="r2", pb="r5M", seat_fac="Parliament")
    other = "b" if who == "a" else "a"
    row = []
    for rig in (0.0, 0.5, 1.0):
        g = n_ = 0
        for i in range(N):
            inp, card, out, b = sit(pp, "rally", mat(), ("rr", who, rig, i), floor=("crowd", "o1"), arranger=who, rig=rig, effort=2)
            w = host.new_world(); band, wr = host.fold(w, pp, inp, card, out, mat())
            g += w["regard"].get((other, who), 0.0); n_ += 1
        row.append(f"rig {rig}: regard({other}->{who}) {g/n_:+.3f}")
    print(f"  arranger {who}: " + " | ".join(row))
