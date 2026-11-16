"""Probe 6/7: ends, marks, presses per type and effort; max marks per side; press decision drivers.
usage: PYTHONHASHSEED=0 python lane1/ends.py [n]"""
import sys, os, math
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harness import sitting, base_people, SCEN, CARRIED
from scmodel import dials
from scmodel.demo import default_people, run_one

N = int(sys.argv[1]) if len(sys.argv) > 1 else 4000


def se(p, n):
    return math.sqrt(max(p * (1 - p), 1e-12) / n)


def tally(label, gen):
    ends, maxmarks, presses, moves, car = Counter(), Counter(), 0, Counter(), 0
    n = 0
    for inp, out, band in gen:
        n += 1
        ends[out.ended] += 1
        for s in out.state.sides:
            maxmarks[s.marks] += 1
        for x in out.exchanges:
            moves[x.move] += 1
        car += band in CARRIED
    yb = (ends["yielded"]) / n; br = ends["broken"] / n
    print(f"{label:48} n={n} yielded={yb:.3f}±{se(yb,n):.3f} broken={br:.3f}±{se(br,n):.3f} "
          f"budget={ends['budget']/n:.3f} rested={ends['rested']/n:.3f} carried={car/n:.3f}±{se(car/n,n):.3f} "
          f"marks/side={dict(sorted(maxmarks.items()))} moves={dict(moves)}")


def _r1(r):
    return r[0], r[1], r[3]


if __name__ == "__main__":
    for Dn, D in (("shipped", dials.shipped()), ("rd", dials.rd_shipped())):
        for eff in (0, 2, 4):
            for row in ("conversation", "legal_trial", "questioning", "negotiation", "arbitration"):
                tally(f"{Dn} {row} default_people(rand) eff={eff}",
                      (_r1(run_one(row, seed=("ends", i), D=D, people=default_people(i), effort=eff))
                       for i in range(N)))
        for scen in ("private_full", "bench_full", "question_full"):
            tally(f"{Dn} {scen} all-mid eff=2", (sitting(scen, base_people(), D, ("ends", i)) for i in range(N)))
