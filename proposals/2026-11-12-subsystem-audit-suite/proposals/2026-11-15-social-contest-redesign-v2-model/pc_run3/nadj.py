"""N's adjudicator figures re-measured with the scripts N states (argue/argue; argue/rest), trial, bench j1..j3."""
import sys
from common import *
n = int(sys.argv[1]) if len(sys.argv) > 1 else 600
def d(lo, hi): return f"d={hi-lo:+.3f}±{math.hypot(se(lo,n),se(hi,n)):.3f}"
def run(lbl, setup, attr, dec, **kw):
    r = {}
    for x in (1, 7):
        pp = blank(); setup(pp)
        for j in ("j1", "j2", "j3"): pp[j]["attributes"][attr] = x
        r[x] = sum(sit(pp, "trial", mat("blank"), ("nadj", lbl, i), deciders=dec, bench=("j1", "j2", "j3"), **kw)[3][0] in CARRIED for i in range(n)) / n
    print(f"  {lbl:60} judge {attr} 1 vs 7: {r[1]:.3f} -> {r[7]:.3f} {d(r[1], r[7])}")
A, R = forced("argue"), forced("rest")
run("sound-plain a (R7 G2) vs polished b (R1 G7), argue/argue", lambda pp: (pp["a"]["attributes"].update(reason=7, grace=2), pp["b"]["attributes"].update(reason=1, grace=7)), "reason", {"a": A, "b": A})
run("for wanders (Focus 1, famine), a argues, b rests", lambda pp: pp["a"]["attributes"].update(focus=1), "focus", {"a": A, "b": R}, strife="famine")
run("a strained liar argues, b rests", lambda pp: (pp["a"].update(believes={"m": -1.0}), pp["a"].update(rattled_ago=(0, 0))), "attunement", {"a": A, "b": R})
