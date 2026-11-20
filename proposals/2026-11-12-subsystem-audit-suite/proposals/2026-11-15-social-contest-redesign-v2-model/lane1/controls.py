"""Control arms for the role sweeps. usage: PYTHONHASHSEED=0 python lane1/controls.py [n]"""
import sys, os
from multiprocessing import Pool
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness
from harness import sweep, sitting, base_people, CARRIED
from scmodel import dials, host

N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
S = dials.shipped()


def job(j):
    tag, scen, who, attr, over, judge_hearer = j
    if judge_hearer:   # control: the bench seat ballots on the hearer's pool_of(untrained, 0, pool_add, pool_floor) (RD C.7)
        host._judging = lambda p, D: host._base_pool(D)
    r = sweep(scen, who, attr, n=N, D=dials.shipped(**over))
    return j, r

JOBS = []
for attr in ("reason", "presence", "grace", "focus", "will", "attunement"):
    JOBS.append(("bench pool=8 (C.7 hearer pool)", "bench_full", "a", attr, {}, True))
JOBS.append(("bench pool=8", "bench_full", "dec", "reason", {}, True))
JOBS.append(("bench pool=8", "bench_full", "b", "will", {}, True))
for attr in ("reason", "attunement"):
    JOBS.append(("fit off (fit/misfit None)", "private_abr", "dec", attr, dict(fit_level=None, misfit_level=None), False))
    JOBS.append(("fit off", "crowd_full", "dec", attr, dict(fit_level=None, misfit_level=None), False))
    JOBS.append(("sense_step 0", "crowd_full", "dec", attr, dict(sense_step=0.0), False))

if __name__ == "__main__":
    with Pool(4) as p:
        res = p.map(job, JOBS)
    print(f"n={N} keys/level CRN, shipped unless overridden")
    for (tag, scen, who, attr, over, jh), r in res:
        z = r["slope"] / r["se"] if r["se"] else 0.0
        sh = " ".join(f"{r['share'][x]:.3f}" for x in sorted(r["share"]))
        print(f"{tag:32} {scen:12} {who:3} {attr:10} slope={r['slope']:+.4f} se={r['se']:.4f} z={z:+6.1f} shares={sh}")
    # band shares at all-mid, per scenario (DOMINANT)
    for scen in harness.SCEN:
        c = Counter(sitting(scen, base_people(), S, ("bands", i))[2] for i in range(4000))
        print(f"bands all-mid {scen:13} " + " ".join(f"{k}={v/4000:.3f}" for k, v in sorted(c.items(), key=str)))
