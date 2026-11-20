import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")
from sc2 import host, fixtures as F
from sc2.lab import rate, BENCH
from checks_v3_helpers import only
mp, M = F.mid_people(), F.matter()
for seed in ("f7", "f7b"):
    print(seed, [round(rate(mp, "trial", M, 800, seed, bench=BENCH, effort=3, deciders=({"a": d} if d else None)), 3) for d in (only("argue"), None, only("rest"))])
