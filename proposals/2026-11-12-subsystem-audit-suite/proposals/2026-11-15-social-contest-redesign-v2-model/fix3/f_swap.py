"""held: side-swap symmetry (fix2/fswap.py's measure) on the trial at a larger n, both models.  python -B f_swap.py N"""
from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
mp, M = F.mid_people(), F.matter()
def pos(people, kw):
    k = 0
    for i in range(N):
        inp, card, out, b = sit(people, "trial", M, ("M", i), **kw)
        j = next(p.id for p in sorted(inp.room, key=lambda p: (-p.precedence, p.id)) if p.decides)
        k += dict(out.state.tracks)[j] > 0
    return k / N
kw = dict(bench=BENCH, effort=3, floor=("crowd",))
s0 = pos(mp, kw); a7 = copy.deepcopy(mp); a7["a"]["attributes"]["reason"] = 7; b7 = copy.deepcopy(mp); b7["b"]["attributes"]["reason"] = 7
s1, s2 = pos(a7, kw), pos(b7, kw)
H(f"side swap, trial, n={N} (one p about +-{2*(0.25/N)**0.5:.3f})")
print(f"  identical {s0:.3f}; Reason 7 as `for` {s1:.3f} ({s1-s0:+.3f}), as `against` {s2:.3f} ({s2-s0:+.3f}); asymmetry {(s1-s0)+(s2-s0):+.3f}")
