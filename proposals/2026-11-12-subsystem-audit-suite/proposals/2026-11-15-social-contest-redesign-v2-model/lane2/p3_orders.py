"""P3: orders. (a) rank: ties, an outranking respondent, a passed-over speaker; (b) scripted asymmetry: the same pair
under `questioned`+scripted vs `contest`+alternating on the same row (hearers: questioning; bench: interrogation);
(c) written_only vs free on `audience`; (d) free with two speakers.
    PYTHONHASHSEED=0 python lane2/p3_orders.py [n]
"""
import sys, random, copy
from collections import Counter
from common import *

N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
D = dials.shipped()


def rnd_people(i):
    r = random.Random(i)
    P = people()
    for pid in P:
        P[pid]["attributes"] = {k: r.randint(1, 7) for k in ATTRS}
    return P


# (a) rank
P = people()
inp = build_input(P, "legal_trial", "full", actor="a", addressed="b", bench=("pol0",), effort=7, dials=D)
o = proceed(inp, draw(1, "a", "o"), None)
print("(a) rank, precedence tie (0,0):", [x.mover for x in o.exchanges], o.ended)
P2 = people(); P2["b"]["seat"] = {"rung": "duchy", "faction": "Crown"}
inp = build_input(P2, "legal_trial", "full", actor="a", addressed="b", bench=("pol0",), effort=7, dials=D)
o = proceed(inp, draw(1, "a", "o"), None)
print("    rank, respondent outranks:", [x.mover for x in o.exchanges], o.ended)
P3 = people("mid", "lo");
inp = build_input(P3, "legal_trial", "full", actor="a", addressed="b", bench=("pol0",), effort=7, dials=D)
seqs = Counter()
for s in range(300):
    o = proceed(inp, draw(s, "a", "o"), None)
    seqs[("".join(x.mover for x in o.exchanges), o.ended)] += 1
print("    rank, Will-1 respondent (resolve 2.5): sequences", seqs.most_common(5))

# (b) scripted asymmetry
def arm(row, rite, order, n):
    saved = copy.deepcopy(data.ROWS[row])
    data.ROWS[row]["rite"], data.ROWS[row]["order"] = rite, order
    try:
        bands, tr, presses, nx = Counter(), 0.0, Counter(), 0
        for i in range(n):
            Pp = rnd_people(i)
            sc = dict(addressed="b", bench=(("pol0", "pol1") if row == "interrogation" else ()))
            inp = build_input(Pp, row, "full", actor="a", dials=D, effort=2, **sc)
            o = proceed(inp, draw(("b", i), "a", "b"), None)
            m, v = act_margin(o, inp.type, inp)
            b = degree(m)
            bands[b] += 1
            tr += o.state.track
            nx += len(o.exchanges)
            for x in o.exchanges:
                if x.move == "press":
                    presses[x.mover] += 1
        return bands, tr / n, presses, nx / n
    finally:
        data.ROWS[row] = saved

for row in ("questioning", "interrogation"):
    for rite, order in (("questioned", "scripted"), ("contest", "alternating")):
        b, t, p, nx = arm(row, rite, order, N)
        sp = (b["success"] + b["overwhelming"]) / N
        print(f"(b) {row:13s} rite={rite:10s} order={order:11s}: questioner Success+ {sp:.3f}  mean track {t:+.3f} "
              f"nx {nx:.2f} presses {dict(p)} bands {dict(b)}")

# (c) written_only vs free on audience
for order in (None, "written_only"):
    bands = Counter(); mar = 0.0
    for i in range(N):
        Pp = rnd_people(i)
        inp = build_input(Pp, "audience", "full", actor="a", bench=("pol0",), present=("crowd12",), effort=2, dials=D,
                          order=order)
        o = proceed(inp, draw(("c", i), "a", "c"), None)
        m, _ = act_margin(o, inp.type, inp)
        bands[degree(m)] += 1
        mar += sum(x.margin for x in o.exchanges) / len(o.exchanges)
    print(f"(c) audience order={order or 'free'}: bands {dict(bands)}  mean speech margin {mar / N:+.3f}")

# (d) free with two speakers (conversation order override)
inp = build_input(people(), "conversation", "full", actor="a", addressed="b", effort=7, dials=D, order="free")
o = proceed(inp, draw(3, "a", "o"), None)
print("(d) free, two speakers:", [x.mover for x in o.exchanges], o.ended)
