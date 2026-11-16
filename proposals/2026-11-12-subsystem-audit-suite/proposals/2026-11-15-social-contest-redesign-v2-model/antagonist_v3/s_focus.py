import sys, os, copy, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/snap")
from sc2 import fixtures as F
from sc2.lab import rate, se, BENCH
from checks_v3_helpers import only
mp, M = F.mid_people(), F.matter(); n = 800
for lab, kw in (("pressed every turn, famine", dict(strife="famine", deciders={"b": only("press")})), ("pressed every turn, peace", dict(deciders={"b": only("press")}))):
    r = {}
    for x in (1, 7):
        pp = copy.deepcopy(mp); pp["a"]["attributes"]["focus"] = x
        d = dict(kw["deciders"]); d["a"] = only("argue")
        r[x] = rate(pp, "trial", M, n, "fo", bench=BENCH, effort=3, strife=kw.get("strife", "peace"), deciders=d)
    print(f"speaker Focus 1->7, trial, {lab}: {r[1]:.3f}->{r[7]:.3f} ({r[7]-r[1]:+.3f}, z {(r[7]-r[1])/math.hypot(se(r[1],n), se(r[7],n)):+.1f})")
