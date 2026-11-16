"""Reason inversion via the decider-party's own track, under the NPC policy (both auto) and with a speaking."""
import sys
from common import *
n = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
def d(lo, hi): return f"d={hi-lo:+.3f}±{math.hypot(se(lo,n),se(hi,n)):.3f}"
for ctx in ("conversation", "questioning"):
    for bset in (dict(reason=7, grace=1), dict(reason=7), dict(reason=6, grace=3)):
        for lbl, dec in (("both auto", {}), ("a argues every turn, b argues", {"a": forced("argue"), "b": forced("argue")})):
            r = {}
            for x in (1, 4, 7):
                pp = blank(); pp["a"]["attributes"]["reason"] = x; pp["b"]["attributes"].update(bset)
                r[x] = sum(sit(pp, ctx, mat("blank"), ("inv2", ctx, str(bset), lbl, i), deciders=dec)[3][0] in CARRIED for i in range(n)) / n
            print(f"  {ctx:12} b {str(bset):28} {lbl:30} a Reason 1/4/7: {r[1]:.3f} {r[4]:.3f} {r[7]:.3f} {d(r[1], r[7])}")
