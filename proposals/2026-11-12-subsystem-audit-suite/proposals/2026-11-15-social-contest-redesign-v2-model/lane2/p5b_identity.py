"""P5b: rows that are only a name. Same draw key per seed (row-independent), people with random attributes for the
parties and IDENTICAL seats across authorities (so pol/ch benches match); arm 1 shipped; arm 2 shipped with
reason_bias equalised to 0 on every row. Pairs whose sittings AND act bands are identical on >= 90% of seeds.
    PYTHONHASHSEED=0 python lane2/p5b_identity.py [n]"""
import sys, random
from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 300
def ppl(i):
    r = random.Random(i); P = people()
    for pid in ("a", "b"):
        P[pid]["attributes"] = {k: r.randint(1, 7) for k in ATTRS}
    return P
def scene(row):
    pre = AUTH_PREFIX[data.ROWS[row]["authority"]]
    addressed = "cohort" if row == "rally" else ("b" if data.RITES[data.ROWS[row]["rite"]]["against"] else None)
    return dict(addressed=addressed, bench=(f"{pre}0", f"{pre}1"), present=("h1",))
for label, D in (("shipped", dials.shipped()), ("shipped, reason_bias 0 everywhere", dials.shipped(reason_bias={k: 0.0 for k in data.ROW_IDS}))):
    sig = {}
    for row in data.ROW_IDS:
        L = []
        for i in range(N):
            inp = build_input(ppl(i), row, "full", actor="a", dials=D, effort=7, **scene(row))
            o = proceed(inp, draw(("id", i), "a", "id"), None)
            m, v = act_margin(o, inp.type, inp)
            L.append((tuple((x.move, round(x.margin, 9)) for x in o.exchanges), o.ended, degree(m)))
        sig[row] = L
    print(f"[{label}]")
    rows = list(data.ROW_IDS)
    for a in range(len(rows)):
        for b in range(a + 1, len(rows)):
            A, B = sig[rows[a]], sig[rows[b]]
            sx = sum(p[0] == q[0] for p, q in zip(A, B)); sb = sum(p[2] == q[2] for p, q in zip(A, B))
            pref = sum(p[0][:2] == q[0][:2] for p, q in zip(A, B))
            if sx >= 0.3 * N or pref >= 0.9 * N:
                print(f"  {rows[a]:28s} ~ {rows[b]:28s} whole sitting equal {sx}/{N}, first two exchanges equal {pref}/{N}, act band equal {sb}/{N}")
