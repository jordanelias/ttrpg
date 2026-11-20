"""P1d: bench rows. Does the bench verdict respond to play at all? Shipped vs a planted bench whose seat pool goes through
pool_of (8 dice, as a hearer's; G13's alternative). For: auto / argue_best / rest; against: auto / rest; and the
for speaker all-7 vs all-1.
    PYTHONHASHSEED=0 python lane3/p1d_bench.py [n]"""
import sys
from dataclasses import replace

import harness
from harness import run, person, ATTRS, dialmod, P

n = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
MOV = dict(pursuits={"x": 0.6}, convictions={"c": 3})
orig_close = P._close


def planted_close(inp, *a, **k):
    pool = P._P(inp.dials, inp.dials["pool_default"])  # pool_of(2,0,6,5) = 8
    inp = replace(inp, deciders=tuple(replace(d, pool=pool) for d in inp.deciders))
    return orig_close(inp, *a, **k)


for arm in ("shipped", "planted_pool8"):
    P._close = planted_close if arm != "shipped" else orig_close
    for row in ("legal_trial", "arbitration"):
        mid = person("m", **MOV)
        cells = []
        for sf, sa in (("auto", "auto"), ("argue_best", "rest"), ("rest", "auto"), ("rest", "rest")):
            r = run(row, mid, mid, sf, sa, n=n, label=f"p1d:{row}:{sf}:{sa}")
            cells.append(f"{sf}/{sa}={r['carry']:.3f}(trk {r['track']:+.2f})")
        s7 = person("s", {k: 7 for k in ATTRS}, rank=3, proofs=3, **MOV)
        s1 = person("w", {k: 1 for k in ATTRS}, rank=0, proofs=0, **MOV)
        r = run(row, s7, s1, n=n, label=f"p1d:{row}:71")
        cells.append(f"all7-vs-all1={r['carry']:.3f}")
        print(f"{arm:14} {row:12} " + "  ".join(cells))
P._close = orig_close
