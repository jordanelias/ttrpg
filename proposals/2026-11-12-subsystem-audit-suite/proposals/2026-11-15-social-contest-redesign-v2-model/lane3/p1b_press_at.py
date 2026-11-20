"""P1b: does `press_at` ever hold a press back? Record, at every automatic decision where the mover is behind and may
press, the policy's believed product p_land*(1-steady_odds) and whether it pressed; across builds (random 1..7).
Also the spiral: a side that presses while behind -- does the track ever turn its way afterwards?
    PYTHONHASHSEED=0 python lane3/p1b_press_at.py [n]"""
import random
import sys
from collections import Counter

from harness import proceed2, person, bench_people, scene_kw, P, dialmod, build_input, draw, ATTRS
from scmodel.records import Choice
from scmodel.dice import p_at_least

n = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
D = dialmod.shipped()
rec = []


def spy(inp, state, i, reading, spoken, legal):
    ch = P._auto(inp, state, i, reading, spoken)
    S = inp.speakers[i]
    behind = P.SIGN[S.side] * state.track < 0
    if behind and "press" in legal:
        mv = "press"
        g_o = P._argmax(reading, "other:", list(inp.grounds)) or P._argmax(reading, "target:", list(inp.grounds))
        p_land = 1.0 - P.exchange_odds(inp, state, i, Choice(mv, g_o))[0]
        r = dict(reading)
        blow = D["blow_gain"] * (D["press_base"] + 1.0) * (1.0 + D["sore_gain"] * r.get("other:" + g_o, 0.0))
        steady = p_at_least(P._P(D, D["attribute_mid"]), P._even(D) + r["strain"] + blow)
        rec.append((p_land, 1 - steady, p_land * (1 - steady), ch.move == "press", inp.type.id))
    return ch


for row in ("conversation", "legal_trial", "arbitration", "questioning"):
    for t in range(n):
        rnd = random.Random(hash(("p1b", row, t)))
        A = person("a", {k: rnd.randint(1, 7) for k in ATTRS}, rank=rnd.randint(0, 3), proofs=rnd.choice([0, 1, 2, 3]),
                   pursuits={"x": rnd.random()}, convictions={"c": rnd.randint(0, 5)})
        B = person("b", {k: rnd.randint(1, 7) for k in ATTRS}, rank=rnd.randint(0, 3), proofs=rnd.choice([0, 1, 2, 3]),
                   pursuits={"x": rnd.random()}, convictions={"c": rnd.randint(0, 5)})
        people = {"a": A, "b": B}
        people.update(bench_people())
        inp = build_input(people, row, "full", "argue", actor="a", dials=D, effort=rnd.randint(0, 4), **scene_kw(row))
        proceed2(inp, draw(("p1b", row, t), "a", "r"), {0: spy, 1: spy})

for row in ("conversation", "legal_trial", "arbitration", "questioning"):
    R = [r for r in rec if r[4] == row]
    if not R:
        print(row, "no behind-and-may-press decisions"); continue
    pressed = sum(r[3] for r in R)
    prods = sorted(r[2] for r in R)
    one_minus = sorted(r[1] for r in R)
    pl = sorted(r[0] for r in R)
    q = lambda xs, f: xs[int(f * (len(xs) - 1))]
    print(f"{row:13} decisions={len(R)} pressed={pressed} ({pressed / len(R):.3f}); product min/p10/med/max="
          f"{prods[0]:.3f}/{q(prods, .1):.3f}/{q(prods, .5):.3f}/{prods[-1]:.3f}; 1-steady min/max={one_minus[0]:.3f}/"
          f"{one_minus[-1]:.3f}; p_land min/med/max={pl[0]:.3f}/{q(pl, .5):.3f}/{pl[-1]:.3f}")
