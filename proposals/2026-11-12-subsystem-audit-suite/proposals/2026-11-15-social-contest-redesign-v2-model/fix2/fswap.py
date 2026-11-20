"""F the mirror/swap, as the premise-check measured it: P(the presiding seat's track > 0) with identical sides (about 0.5),
and with a Reason-7 man as `for` and as `against`, which should mirror about it."""
from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 600
H(f"F the mirror/swap (n={N}; band at p=.5 about +-{2 * (0.25 / N) ** 0.5:.3f})")
def pos(people, rite, kw):
    k = 0
    for i in range(N):
        inp, card, out, b = sit(people, rite, M, ("M", i), **kw)
        j = next(p.id for p in sorted(inp.room, key=lambda p: (-p.precedence, p.id)) if p.decides)
        k += dict(out.state.tracks)[j] > 0
    return k / N
for rite, kw in (("trial", dict(bench=BENCH, effort=3, floor=("crowd",))), ("debate", dict(bench=BENCH, effort=3, floor=("crowd",))), ("conversation", dict(effort=3))):
    s0 = pos(mp, rite, kw)
    a7 = copy.deepcopy(mp); a7["a"]["attributes"]["reason"] = 7
    b7 = copy.deepcopy(mp); b7["b"]["attributes"]["reason"] = 7
    s1, s2 = pos(a7, rite, kw), pos(b7, rite, kw)
    print(f"  {rite:12s} identical sides: P(track > 0) {s0:.3f}; Reason 7 as `for` {s1:.3f} ({s1 - s0:+.3f}), as `against` {s2:.3f} ({s2 - s0:+.3f}); asymmetry {(s1 - s0) + (s2 - s0):+.3f}")
