"""P4: resume. (a) feed out.state back in: does the sitting continue (n, track, resolve, strikes carry) or restart?
(b) a resumed state at n == exchanges max: how many exchanges does the second sitting get? (c) A.2's recompute of the
track from the recorded margins (each clipped, the running sum clamped) vs the module's own track, with and without
concedes (a decide callback concedes with p=0.3).
    PYTHONHASHSEED=0 python lane2/p4_resume.py
"""
import random
from dataclasses import replace
from collections import Counter
from common import *
from scmodel.records import Choice

D = dials.shipped()
P = people()
inp = build_input(P, "legal_trial", "full", actor="a", addressed="b", bench=("pol0", "pol1"), effort=7, dials=D)
# (a)+(b)
res = Counter()
for s in range(300):
    o1 = proceed(inp, draw(("r", s), "a", "s1"), None)
    o2 = proceed(replace(inp, state=o1.state), draw(("r", s), "a", "s2"), None)
    res[(o1.ended, len(o1.exchanges), o2.ended, len(o2.exchanges), o2.state.n)] += 1
print("(a/b) legal_trial [2,5], effort 7: (end1, nx1, end2, nx2, n2) counts:")
for k, v in res.most_common(12):
    print("   ", k, v)
# a yielded sitting resumed: does the non-yielded side get a free extra exchange?
yres = Counter()
for s in range(2000):
    o1 = proceed(inp, draw(("y", s), "a", "s1"), None)
    if o1.ended != "yielded":
        continue
    o2 = proceed(replace(inp, state=o1.state), draw(("y", s), "a", "s2"), None)
    yres[(len(o2.exchanges), o2.ended)] += 1
print("    yielded sittings resumed -> (exchanges in resumed sitting, end):", dict(yres))
# fresh-state resume: host builds fresh sides but carries the track: compare to n carried
o1 = proceed(inp, draw(("r", 0), "a", "s1"), None)
print("    o1.state.n", o1.state.n, "sides resolve", [round(x.resolve, 2) for x in o1.state.sides])

# (c) recompute track from exchanges
def recompute(inp, exchanges, clip=3.0):
    side = {S.id: (1.0 if S.side == "for" else -1.0) for S in inp.speakers}
    t = 0.0
    for x in exchanges:
        if x.move in ("argue", "deceive") and x.terms:
            t = max(-clip, min(clip, t + side[x.mover] * max(-clip, min(clip, x.margin))))
    return t

inp2 = build_input(P, "conversation", "full", actor="a", addressed="b", effort=7, dials=D)
for label, pc in (("no concede", 0.0), ("concede p=.3", 0.3)):
    mism = tot = 0
    for s in range(500):
        r = random.Random(s)
        def dec(view):
            if "concede" in view.legal and r.random() < pc:
                return Choice("concede", None)
            g = max((k[7:] for k, _ in view.read if k.startswith("target:")), key=lambda g: dict(view.read)["target:" + g])
            return Choice("argue", g)
        o = proceed(inp2, draw(("c", s), "a", "c"), dec)
        tot += 1
        mism += abs(recompute(inp2, o.exchanges) - o.state.track) > 1e-9
    print(f"(c) {label}: recomputed track != module track in {mism}/{tot}")
