"""P5: the 13 rows as distinct kinds. Same people, same draw key (independent of the row) per seed; per row:
exchanges, presses by side, diverts/concedes/rests, room, deciders, ends, bands. Then pairwise: rows whose sittings
(exchange sequence) are identical on every seed, and whose act bands are identical.
    PYTHONHASHSEED=0 python lane2/p5_rows.py [n]
"""
import sys, random
from collections import Counter, defaultdict
from common import *

N = int(sys.argv[1]) if len(sys.argv) > 1 else 400
D = dials.shipped() if "--controls" not in sys.argv else dials.controls()


def rnd_people(i):
    r = random.Random(i)
    P = people()
    for pid in P:
        P[pid]["attributes"] = {k: r.randint(1, 7) for k in ATTRS}
    return P


def scene(row):
    auth = data.ROWS[row]["authority"]
    pre = AUTH_PREFIX[auth]
    bench = tuple(f"{pre}{k}" for k in range(3))
    addressed = "cohort" if row == "rally" else ("b" if data.RITES[data.ROWS[row]["rite"]]["against"] else None)
    return dict(addressed=addressed, bench=bench, present=("h1", "crowd12"))


stats = {}
sig = defaultdict(list)
for row in data.ROW_IDS:
    st = dict(nx=0, press=Counter(), moves=Counter(), ends=Counter(), bands=Counter(), room=None, dec=None, sp=None)
    for i in range(N):
        P = rnd_people(i)
        inp = build_input(P, row, "full", actor="a", dials=D, effort=2, **scene(row))
        out = proceed(inp, draw(("p5", i), "a", "p5"), None)
        m, veto = act_margin(out, inp.type, inp)
        b = None if m is None else degree(m)
        if veto and b in ("success", "overwhelming"):
            b = "failure"
        side = {S.id: S.side for S in inp.speakers}
        st["nx"] += len(out.exchanges)
        for x in out.exchanges:
            st["moves"][x.move] += 1
            if x.move == "press":
                st["press"][side[x.mover]] += 1
        st["ends"][out.ended] += 1
        st["bands"][b] += 1
        st["room"] = (inp.room.audience, inp.room.attention, inp.room.proof_weight)
        st["dec"] = tuple(d.id for d in inp.deciders)
        st["sp"] = tuple((S.id, S.side) for S in inp.speakers)
        sig[row].append((tuple((x.mover, x.move, x.ground, round(x.margin, 9)) for x in out.exchanges), b))
    stats[row] = st
for row, st in stats.items():
    print(f"{row:29s} sp={st['sp']} dec={st['dec']} room={st['room']}\n    nx={st['nx']/N:.2f} moves={dict(st['moves'])} "
          f"press_by_side={dict(st['press'])}\n    ends={dict(st['ends'])}\n    bands={dict(st['bands'])}")
print("\nPAIRS with identical sittings on every seed (exchange sequences equal):")
rows = list(data.ROW_IDS)
for a in range(len(rows)):
    for b in range(a + 1, len(rows)):
        A, B = sig[rows[a]], sig[rows[b]]
        same_x = sum(1 for p, q in zip(A, B) if p[0] == q[0])
        same_b = sum(1 for p, q in zip(A, B) if p[1] == q[1])
        if same_x >= N * 0.5:
            print(f"  {rows[a]} ~ {rows[b]}: sittings equal {same_x}/{N}, bands equal {same_b}/{N}")
