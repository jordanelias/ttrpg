"""P2b: dead settings. For each setting, flip it alone (shipped->control on a shipped base; control->shipped on a
control base; and shipped->RD-literal for the three G17 settings) and compare every run's full signature (exchange
sequence + verdict margins + ended) to the base on the same key, across a matrix of rows x forms x scenes x seeds.
A setting that changes no signature anywhere in BOTH directions is dead in this matrix.
    PYTHONHASHSEED=0 python lane2/p2_dead.py [seeds]
"""
import sys, random
from common import *
from scmodel import dials as DM

SEEDS = int(sys.argv[1]) if len(sys.argv) > 1 else 30
KEYS = sorted(DM._CONTROL)


def rnd_people(i):
    r = random.Random(i)
    P = people()
    for pid in P:
        P[pid]["attributes"] = {k: r.randint(1, 7) for k in ATTRS}
        P[pid]["proofs"] = r.choice([0.0, 1.0, 2.5, 5.0])
        P[pid]["knows"] = ["a", "b"]
        P[pid]["operands"] = [("rank_gap", 1.0, 0.5, "reason")]
        P[pid]["marks_season"] = r.choice([0, 1, 2])
    P["a"]["regard"] = {"b": -0.6}; P["b"]["regard"] = {"a": -0.6}
    return P


def cases():
    for row in data.ROW_IDS:
        pre = AUTH_PREFIX[data.ROWS[row]["authority"]]
        addressed = "cohort" if row == "rally" else ("b" if data.RITES[data.ROWS[row]["rite"]]["against"] else None)
        for form in ("full", "abridged"):
            for present in ((), ("h1", "crowd12")):
                for eff in (0, 3):
                    moves = ("argue", "deceive") if form == "abridged" else ("argue",)
                    for mv in moves:
                        yield row, form, mv, dict(addressed=addressed, bench=(f"{pre}0", f"{pre}1"), present=present,
                                                  effort=eff)


def sigs(D):
    out = []
    for row, form, mv, sc in cases():
        for s in range(SEEDS):
            P = rnd_people(s)
            inp = build_input(P, row, form, mv, actor="a", dials=D, **sc)
            o = proceed(inp, draw((row, form, mv, s, str(sc)), "a", "p2"), None)
            out.append((o.ended, tuple((x.mover, x.move, x.ground, round(x.margin, 9)) for x in o.exchanges),
                        tuple((i, round(m.net, 9), round(m.ob, 9)) for i, m in o.verdicts if m is not None)))
    return out


baseS, baseC = sigs(DM.shipped()), sigs(DM.controls())
n = len(baseS)
print(f"runs per arm: {n}")
dead = []
for k in KEYS:
    a = sigs(DM.shipped(**{k: DM._CONTROL[k]}))
    b = sigs(DM.controls(**{k: DM._SHIPPED[k]}))
    ca = sum(1 for p, q in zip(baseS, a) if p != q)
    cb = sum(1 for p, q in zip(baseC, b) if p != q)
    flag = "DEAD" if ca == 0 and cb == 0 else ("dead-on-shipped-base" if ca == 0 else ("dead-on-control-base" if cb == 0 else ""))
    if DM._CONTROL[k] == DM._SHIPPED[k]:
        flag = "(control == shipped)"
    print(f"  {k:20s} shipped->control changed {ca:5d}/{n}   control->shipped changed {cb:5d}/{n}   {flag}")
print("\nG17: shipped -> RD literal")
for k, v in (("strike_level", "minor"), ("presumption_level", "minor"), ("reading_kept", True)):
    a = sigs(DM.shipped(**{k: v}))
    print(f"  {k:20s} changed {sum(1 for p, q in zip(baseS, a) if p != q)}/{n}")
