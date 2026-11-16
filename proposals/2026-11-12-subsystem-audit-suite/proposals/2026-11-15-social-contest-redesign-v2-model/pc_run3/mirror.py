"""Per-attribute mirror/swap: P(for carried) at a=7,b=1 vs a=1,b=7 vs 4/4 (blank cast, auto), n per arm."""
import sys
from multiprocessing import Pool
from common import *
n = int(sys.argv[1])
def job(args):
    attr, ctx = args; r = {}
    for ax, bx in ((7, 1), (4, 4), (1, 7)):
        pp = blank(); pp["a"]["attributes"][attr] = ax; pp["b"]["attributes"][attr] = bx
        r[(ax, bx)] = sum(sit(pp, ctx, mat("blank"), ("mir", attr, ctx, i))[3][0] in CARRIED for i in range(n)) / n
    return attr, ctx, r
with Pool(4) as P:
    for attr, ctx, r in P.map(job, [(a, c) for a in ATTRS for c in CTX]):
        up, mid, dn = r[(7, 1)], r[(4, 4)], r[(1, 7)]
        print(f"{attr:10} {ctx:12} a7b1 {up:.3f}  4/4 {mid:.3f}  a1b7 {dn:.3f}  swing {up-dn:+.3f}±{math.hypot(se(up,n),se(dn,n)):.3f}")
