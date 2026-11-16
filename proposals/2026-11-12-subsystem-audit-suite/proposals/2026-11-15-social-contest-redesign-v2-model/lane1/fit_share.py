"""Share of argue speeches drawing the full `fit` (+strong) vs misfit, by speaker Attunement, abridged conversation, all-mid
decider (moved_by = evidence .5, consequence 0, authority 0, solidarity .5). usage: PYTHONHASHSEED=0 python lane1/fit_share.py [n]"""
import sys, os, copy
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harness import sitting, base_people
from scmodel import dials
N = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
S = dials.shipped()
for att in (1, 4, 7):
    pp = base_people(rank=0, proofs=0.0, known=False); pp["a"]["attributes"]["attunement"] = att
    full = mis = 0
    for i in range(N):
        inp, out, band = sitting("private_abr", pp, S, ("fit", i))
        lv = dict((n, (f, a)) for n, f, a in out.exchanges[0].levels)["fit"]
        full += lv[0] >= 0.75 - 1e-9; mis += lv[1] > 0
    print(f"speaker Attunement {att}: full fit {full/N:.3f}  misfit {mis/N:.3f}")
