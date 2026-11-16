"""P3b: is press access an asset or a liability? questioning (hearers close, b decides) and conversation, same pairs and
keys, rites: questioned (for may press), nopress (nobody may press), contest (both may), b_only (only b may press).
    PYTHONHASHSEED=0 python lane2/p3b_press.py [n]"""
import sys, random, copy
from collections import Counter
from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
D = dials.shipped()
data.RITES["nopress"] = {"for": ("argue", "rest"), "against": ("argue", "concede", "rest"), "bench": (), "faults": ()}
data.RITES["b_only"] = {"for": ("argue", "rest"), "against": ("argue", "press", "rest"), "bench": (), "faults": ()}
def ppl(i):
    r = random.Random(i); P = people()
    for pid in P:
        P[pid]["attributes"] = {k: r.randint(1, 7) for k in ATTRS}
    return P
for row in ("questioning",):
    saved = copy.deepcopy(data.ROWS[row])
    for rite in ("questioned", "nopress", "contest", "b_only"):
        data.ROWS[row]["rite"] = rite
        data.ROWS[row]["order"] = "scripted"
        suc = 0; tr = 0.0; marks_b = 0; yb = 0
        for i in range(N):
            inp = build_input(ppl(i), row, "full", actor="a", addressed="b", effort=2, dials=D)
            o = proceed(inp, draw(("pb", i), "a", "pb"), None)
            m, _ = act_margin(o, inp.type, inp)
            suc += degree(m) in ("success", "overwhelming"); tr += o.state.track
            marks_b += o.state.sides[1].marks
        print(f"{row} rite={rite:10s}: questioner Success+ {suc/N:.3f} (SE {((suc/N)*(1-suc/N)/N)**.5:.3f}) mean track {tr/N:+.3f} marks on b {marks_b/N:.3f}")
    data.ROWS[row] = saved
