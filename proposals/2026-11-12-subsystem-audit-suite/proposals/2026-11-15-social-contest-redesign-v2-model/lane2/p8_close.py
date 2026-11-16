"""P8: the close per disposal.
(a) G13: bench Success+ by final track, shipped judging pool vs a control judging pool through pool_of (the hearer's base
    construction), same keys; and the abridged form of the same row.
(b) G39: mutual (negotiation) act margin = actor's last drawn exchange: how often it is a press; Success+ with track < 0;
    and the correlation of the act band with the track.
(c) declared: veto rate given the presiding seat Success+, by bench size; presiding-alone vs majority disagreement.
(d) hearers: rally weight-mean dominated by a cohort.
    PYTHONHASHSEED=0 python lane2/p8_close.py [n]
"""
import sys, random
from collections import Counter, defaultdict
from common import *
from scmodel import host as H
from scmodel.dice import pool_of

N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
D = dials.shipped()
SUC = ("success", "overwhelming")


def rnd_people(i):
    r = random.Random(i)
    P = people()
    for pid in P:
        P[pid]["attributes"] = {k: r.randint(1, 7) for k in ATTRS}
    return P


def bucket(t):
    return "<=-2" if t <= -2 else ("(-2,0)" if t < 0 else ("[0,2)" if t < 2 else ">=2"))


orig = H._judging
for label, fn in (("shipped judging pool", orig),
                  ("control: pool_of(judging, 0, pool_add, pool_floor)",
                   lambda p, D: pool_of(orig(p, D), 0, D["pool_add"], D["pool_floor"]))):
    H._judging = fn
    by = defaultdict(Counter)
    pools = Counter()
    for i in range(N):
        inp = build_input(rnd_people(i), "legal_trial", "full", actor="a", addressed="b", bench=("pol0", "pol1"),
                          effort=2, dials=D)
        o = proceed(inp, draw(("g13", i), "a", "g"), None)
        m, _ = act_margin(o, inp.type, inp)
        by[bucket(o.state.track)][degree(m) in SUC] += 1
        pools[inp.deciders[0].pool] += 1
    print(f"(a) legal_trial, {label}: presiding pool {dict(pools)}")
    for k in ("<=-2", "(-2,0)", "[0,2)", ">=2"):
        c = by[k]
        print(f"      track {k:7s}: n={c[True] + c[False]:5d} for carried {c[True] / max(1, c[True] + c[False]):.3f}")
H._judging = orig
ab = Counter()
for i in range(N):
    inp = build_input(rnd_people(i), "legal_trial", "abridged", actor="a", bench=("pol0", "pol1"), effort=2, dials=D)
    o = proceed(inp, draw(("g13", i), "a", "g"), None)
    m, _ = act_margin(o, inp.type, inp)
    ab[degree(m) in SUC] += 1
print(f"    abridged legal_trial (speak): Success+ {ab[True] / N:.3f}")

# (b) G39
lastpress = suc_against = suc = 0
by = defaultdict(Counter)
for i in range(N):
    inp = build_input(rnd_people(i), "negotiation", "full", actor="a", addressed="b", effort=2, dials=D)
    o = proceed(inp, draw(("g39", i), "a", "g"), None)
    m, _ = act_margin(o, inp.type, inp)
    last = next(x for x in reversed(o.exchanges) if x.mover == "a" and x.terms)
    s = degree(m) in SUC
    lastpress += last.move == "press"
    suc += s
    suc_against += s and o.state.track < 0
    by[bucket(o.state.track)][s] += 1
print(f"(b) negotiation: act from a press {lastpress}/{N}; Success+ {suc}/{N}; Success+ with track<0 {suc_against}/{N}")
for k in ("<=-2", "(-2,0)", "[0,2)", ">=2"):
    c = by[k]
    print(f"      track {k:7s}: n={c[True] + c[False]:5d} Success+ {c[True] / max(1, c[True] + c[False]):.3f}")

# (c) declared
for nb in (1, 2, 3, 5):
    stats = Counter()
    for i in range(N):
        bench = tuple(f"ch{k}" for k in range(nb))
        inp = build_input(rnd_people(i), "excommunication_deliberation", "full", actor="a", addressed="b", bench=bench,
                          effort=2, dials=D)
        o = proceed(inp, draw(("dec", i), "a", "g"), None)
        m, veto = act_margin(o, inp.type, inp)
        pres = degree(m) in SUC
        nfor = sum(degree(v) in SUC for _, v in o.verdicts)
        stats["presiding Success+"] += pres
        stats["vetoed given presiding Success+"] += pres and veto
        stats["majority for, act failure"] += (nfor * 2 > nb) and not pres
    print(f"(c) declared, {nb} church seats (quorum 2): {dict(stats)}")

# (d) rally to a cohort plus one hearer
cnt = Counter()
for i in range(N):
    inp = build_input(rnd_people(i), "rally", "full", actor="a", addressed="cohort", present=("h1",), effort=2, dials=D)
    o = proceed(inp, draw(("r", i), "a", "g"), None)
    m, _ = act_margin(o, inp.type, inp)
    vs = dict(o.verdicts)
    cnt["act band == cohort band"] += degree(m) == degree(vs["cohort"])
    cnt["room"] = inp.room.audience
print(f"(d) rally cohort(30)+h1: {dict(cnt)} of {N}")
