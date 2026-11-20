"""A man who says NOTHING (a rests every turn; a does not decide): do his Will / Reason change how the deciding
party b is moved by b's OWN speeches? conversation and questioning; b argues every turn."""
import sys
from common import *
n = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
def d(lo, hi): return f"d={hi-lo:+.3f}±{math.hypot(se(lo,n),se(hi,n)):.3f}"
for ctx in ("conversation", "questioning"):
    for attr, bset in (("will", {}), ("reason", dict(reason=7, grace=1)), ("reason", dict(reason=1, grace=7)), ("focus", {}), ("attunement", {}), ("presence", {}), ("grace", {})):
        r = {}
        for x in (1, 7):
            pp = blank(); pp["a"]["attributes"][attr] = x; pp["b"]["attributes"].update(bset)
            r[x] = sum(sit(pp, ctx, mat("blank"), ("sil", ctx, attr, i), deciders={"a": forced("rest"), "b": forced("argue")})[3][0] in CARRIED for i in range(n)) / n
        print(f"  {ctx:12} silent a's {attr:10} 1 vs 7 (b {bset or 'mid'}): {r[1]:.3f} -> {r[7]:.3f} {d(r[1], r[7])}")
