from common import *
exec(open("c3.py").read().split('H(f"C3.1')[0].split("N = int")[1].split("\n",1)[1])
pp = cast_with(a_rung=4)
for seed in ("c3a","c3b","x"):
    print(seed, [round(carried(pp, "trial", M, 1500, seed, bench=BENCH, floor=("crowd",), effort=3, arranger="a", rig=r),3) for r in (0,0.5,1)])
