"""Probe 1: R2 role sweeps. usage: PYTHONHASHSEED=0 python lane1/roles.py [n] [shipped|controls|rd]"""
import sys, os
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harness import sweep, monotone, ATTRS, SCEN
from scmodel import dials

N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
DS = sys.argv[2] if len(sys.argv) > 2 else "shipped"
D = {"shipped": dials.shipped, "controls": dials.controls, "rd": dials.rd_shipped}[DS]()

JOBS = []
for scen in SCEN:
    for a in ATTRS:
        JOBS.append((scen, "a", a))
    if scen in ("private_full", "bench_full", "question_full"):
        for a in ATTRS:
            JOBS.append((scen, "b", a))
    for a in ATTRS:
        if scen in ("private_abr", "bench_abr", "crowd_full", "bench_full") or a in ("reason", "focus", "attunement"):
            if not (scen in ("private_full", "question_full")):
                JOBS.append((scen, "dec", a))


def job(j):
    scen, who, attr = j
    r = sweep(scen, who, attr, n=N, D=D)
    return j, r


if __name__ == "__main__":
    with Pool(4) as p:
        res = p.map(job, JOBS)
    print(f"dials={DS} n={N} keys per level, CRN; slope = d(carried share)/d(attribute point)")
    for (scen, who, attr), r in res:
        z = r["slope"] / r["se"] if r["se"] > 0 else float("inf") if r["slope"] else 0.0
        sgn = 1 if r["slope"] >= 0 else -1
        bad = monotone(r, sgn)
        flag = "INERT" if abs(z) < 2 else ""
        sh = " ".join(f"{r['share'][x]:.3f}" for x in sorted(r["share"]))
        print(f"{scen:13} {who:3} {attr:10} slope={r['slope']:+.4f} se={r['se']:.4f} z={z:+6.1f} {flag:5} "
              f"nonmono={bad} shares[1..7]={sh}")
