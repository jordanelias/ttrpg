"""G04: would the plan's gate see the ballot `resist` sign? (the literal pair-net reading ADDS +r toward `for`).
And: a hearer's lean (stance x regard_step, up to 1.0 sigma) vs a fully carried track (0.9 sigma).
usage: PYTHONHASHSEED=0 python lane1/g04_lean.py [n]"""
import sys, os, inspect, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harness import sweep, sitting, base_people, CARRIED
from scmodel import dials, proceeding as P
N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
S = dials.shipped()
src = inspect.getsource(P._ballot_input).replace("+ pres + ends - resist", "+ pres + ends + resist")
assert "+ ends + resist" in src
ns = dict(vars(P)); exec(src, ns); flipped = ns["_ballot_input"]
orig = P._ballot_input
for lab, fn in (("model (- r)", orig), ("pair-net literal (+ r)", flipped)):
    P._ballot_input = fn
    for scen in ("private_abr", "crowd_full", "private_full"):
        who = "dec" if scen != "private_full" else "b"
        r = sweep(scen, who, "will", n=N, D=S)
        print(f"{lab:24} {scen:12} {who} will slope={r['slope']:+.4f} se={r['se']:.4f}")
P._ballot_input = orig
# lean vs track: full conversation, b (decider and opponent) regard for a in {-1, 0, +1}; carried among sittings ending track >= 2.9
for st in (-1.0, 0.0, 1.0):
    pp = base_people(); pp["b"]["regard"] = {"a": st}
    tot = car = 0
    for i in range(N * 3):
        inp, out, band = sitting("private_full", pp, S, ("lean", i))
        if out.state.track >= 2.9:
            tot += 1; car += band in CARRIED
    p = car / max(tot, 1)
    print(f"conversation, hearer stance {st:+.0f}: sittings with track >= +2.9: {tot}; carried {p:.3f}±{math.sqrt(p*(1-p)/max(tot,1)):.3f}")
