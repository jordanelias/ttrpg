"""Re-measure N's speaker table (V2 part3 'The speaker's six') in a re-implementation of its stated setting:
listeners b/j1/crowd with layers (pursuit p, conviction c), matter with no bearing; tell; trial bench j1..j3 effort 3
floor crowd; rally (one party) effort 3 floor crowd. auto choosers. n per level from argv."""
import sys, copy
from common import *
n = int(sys.argv[1])
rp = blank()
for q, cr in (("b", dict(pursuits={"p": 0.9}, convictions={"c": 1})), ("j1", dict(pursuits={"p": 0.2}, convictions={"c": 5})), ("crowd", dict(pursuits={"p": 0.9}, convictions={"c": 1}))):
    rp[q]["layers"] = cr
M = F.matter(); ral = dict(id="m", parties={"for": "a"}, bears={})
from sc2.engine import proceed
for scen, rite, m, kw in (("tell", "conversation", M, dict(form="abridged")), ("trial", "trial", M, dict(bench=("j1", "j2", "j3"), effort=3, floor=("crowd",))), ("rally", "rally", ral, dict(floor=("crowd",), effort=3))):
    row = []
    for a in ATTRS:
        r = {}
        for x in (1, 7):
            pp = copy.deepcopy(rp); pp["a"]["attributes"][a] = x
            c = 0
            for i in range(n):
                inp, card = host.build(pp, rite, m, **kw); out = proceed(inp, draw(("nrep", i), "act", rite))
                c += host.act_band(inp, out)[0] in CARRIED
            r[x] = c / n
        dd = r[7] - r[1]; s = math.hypot(se(r[1], n), se(r[7], n))
        row.append(f"{a[:4]} {r[1]:.3f}->{r[7]:.3f} ({dd:+.3f}, z {dd/s:+.1f})")
    print(f"{scen:6} " + " | ".join(row))
