"""F1 resume (stress lane C, repro_resume.py; fuzz): a changed room, an abridged resume, a spent sitting.
PREDICTION after: each is a keyed refusal; resuming the same room with more turns runs. Before: two crashes and a
spent sitting whose close is drawn again (its band changes).  python -B f01_resume.py N"""
from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 300
mp, M = F.mid_people(), F.matter()
H("F1 resume")
o1 = proceed(host.build(mp, "conversation", M, form="abridged")[0], draw(1, "a", "r"))
print("  resume an abridged tell:", attempt(lambda: proceed(host.build(mp, "conversation", M, form="abridged", state=o1.state)[0], draw(2, "a", "r")).ended))
o1 = proceed(host.build(mp, "trial", M, bench=("j1",), effort=1)[0], draw(1, "a", "r"))
print("  resume a trial before another seat:", attempt(lambda: proceed(host.build(mp, "trial", M, bench=("j2",), effort=3, state=o1.state)[0], draw(2, "a", "r")).ended))
print("  CONTROL resume before the same seat, more turns:", attempt(lambda: proceed(host.build(mp, "trial", M, bench=("j1",), effort=3, state=o1.state)[0], draw(2, "a", "r")).ended))
o1 = proceed(host.build(mp, "debate", M, bench=BENCH, effort=1)[0], draw(1, "a", "r"))
print("  resume a debate with a crowd newly on the floor:", attempt(lambda: proceed(host.build(mp, "debate", M, bench=BENCH, floor=("crowd",), effort=3, state=o1.state)[0], draw(2, "a", "r")).ended))
moved = refused = ran = 0
for i in range(N):
    inp, card = host.build(mp, "audience", M, bench=("j1",), effort=3)
    o = proceed(inp, draw(("sp", i), "a", "r")); b0 = host.act_band(inp, o)[0]
    if o.ended == "yielded":
        continue
    r = attempt(lambda: host.act_band(host.build(mp, "audience", M, bench=("j1",), effort=3, state=o.state)[0],
                                      proceed(host.build(mp, "audience", M, bench=("j1",), effort=3, state=o.state)[0], draw(("sp2", i), "a", "r")))[0])
    if r.startswith("ok"):
        ran += 1; moved += r[4:] != str(b0)
    elif r.startswith("refused[spent]"):
        refused += 1
print(f"  resume a spent audience (n={N}): ran {ran} (band changed {moved}), refused[spent] {refused}")
