"""Probe 7: A-79's centre (25% carried) in the abridged conversation, all-mid, per difficulty level and dial set.
usage: PYTHONHASHSEED=0 python lane1/centre.py [n]"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harness import sitting, base_people, CARRIED
from scmodel import dials
N = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
for dn, D in (("controls", dials.controls()), ("shipped", dials.shipped()), ("rd", dials.rd_shipped())):
    for lab, pp in (("rank1 proofs2", base_people()), ("untrained proofs0 unknown", base_people(rank=0, proofs=0.0, known=False))):
        row = []
        for lvl in ("plain", "routine", "demanding", "hard"):
            c = sum(sitting("private_abr", pp, D, ("ctr", i), difficulty_level=lvl)[2] in CARRIED for i in range(N)) / N
            row.append(f"{lvl}={c:.3f}±{math.sqrt(c*(1-c)/N):.3f}")
        print(f"{dn:8} {lab:26} " + " ".join(row))
