"""Attribute SUM and mirror/swap: a all-x vs b all-y, every context, auto choosers; blank and rich cast."""
import sys
from common import *
n = int(sys.argv[1]) if len(sys.argv) > 1 else 600
def setall(p, x):
    for k in ATTRS: p["attributes"][k] = x
for fx in ("blank", "rich"):
    print(fx)
    for ctx in CTX:
        row = []
        for ax, bx in ((7, 1), (7, 4), (4, 4), (4, 7), (1, 7), (1, 4), (4, 1), (1, 1), (7, 7)):
            pp = blank() if fx == "blank" else rich(); setall(pp["a"], ax); setall(pp["b"], bx)
            c = sum(sit(pp, ctx, mat(fx), ("sum", i))[3][0] in CARRIED for i in range(n)) / n
            row.append(f"a{ax}b{bx}:{c:.3f}")
        print(f"  {ctx:12} " + " ".join(row))
