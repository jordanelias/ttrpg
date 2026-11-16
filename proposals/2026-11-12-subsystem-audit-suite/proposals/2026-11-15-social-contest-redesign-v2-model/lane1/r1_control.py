"""Reading R1 (B24p.21) at controls: 'Reason alone reads a slope' in each of the five readings? track_step is 0 at control,
so a balloted type's verdict cannot see the speeches. usage: PYTHONHASHSEED=0 python lane1/r1_control.py [n]"""
import sys, os
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harness import sweep
from scmodel import dials
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
JOBS = [(s, a) for s in ("private_abr", "private_full", "crowd_full", "bench_full", "question_full") for a in ("reason", "presence", "focus")]
def job(j):
    return j, sweep(j[0], "a", j[1], n=N, D=dials.controls())
if __name__ == "__main__":
    with Pool(4) as p:
        for (s, a), r in p.map(job, JOBS):
            print(f"controls {s:13} a {a:9} slope={r['slope']:+.4f} se={r['se']:.4f} share@4={r['share'][4]:.3f}")
