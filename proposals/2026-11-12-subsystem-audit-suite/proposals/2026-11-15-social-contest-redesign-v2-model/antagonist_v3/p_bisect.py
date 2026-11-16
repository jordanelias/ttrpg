import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")
from sc2 import host, fixtures as F
from sc2.lab import rate, sit, BENCH
from checks_v3_helpers import only
mp, M = F.mid_people(), F.matter()
f7 = lambda: round(rate(mp, "trial", M, 300, "f7", bench=BENCH, effort=3, deciders={"a": only("argue")}), 3)
print("fresh", f7())
step = sys.argv[1]
if step == "d2":
    C = host.controls()
    for i in range(5): sit(mp, "conversation", M, ("d2", i), form="abridged", D=C)
if step == "d5":
    host.RITES["trial"]["bears"] = "against"; rate(mp, "trial", M, 5, "d5", bench=BENCH, effort=3); host.RITES["trial"]["bears"] = "for"
if step == "d1":
    rate(mp, "trial", M, 5, "d1", bench=BENCH, effort=3, D=host.dials(track_step=0.0))
if step == "ex":
    rate(mp, "excommunication_deliberation", M, 5, "x", bench=("c1","c2","c3"), effort=2)
if step == "q":
    rate(mp, "questioning", M, 5, "f2", effort=3)
print(step, f7())
