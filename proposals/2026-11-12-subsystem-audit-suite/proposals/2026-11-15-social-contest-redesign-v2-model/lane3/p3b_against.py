"""P3b: the `against` speaker's Reason / Presence in conversation: auto vs argue_best (never press); common seeds.
Also AR-49/50 under a patched gallery room (no seeded two-sided row has an open floor without a bench), with the
profile speaker's final esteem.
    PYTHONHASHSEED=0 python lane3/p3b_against.py [n]"""
import math
import sys
from dataclasses import replace

import harness
from harness import run, person, dialmod, P, proceed2, build_input, bench_people, scene_kw, draw, degree, CARRIED

n = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
MOV = dict(pursuits={"x": 0.6}, convictions={"c": 3})
mid = person("m", **MOV)
for row in ("conversation", "negotiation"):
    for pol in ("auto", "argue_best"):
        line = []
        for a in ("reason", "presence"):
            for v in (1, 4, 7):
                r = run(row, mid, person("b", {a: v}, **MOV), "auto", pol, n=n, label=f"p3b:{row}")
                line.append(f"{a[:4]}{v}={r['carry']:.3f}")
        pr = r["moves"]
        print(f"{row:12} against={pol:10} " + " ".join(line) + f"  se~{r['se']:.3f}  against moves(last cell)="
              f"{ {k[1]: v for k, v in pr.items() if k[0] == 'b'} }")

print("\nAR-49/50 (RD B.5): 2-sided, routine standard, room patched to the gallery row of audience_room")
D = dialmod.shipped()
g = D["audience_room"]["gallery"]
for row in ("conversation", "negotiation"):
    for side in ("for", "against"):
        res = {}
        for nm, at in (("P6G2", {"presence": 6, "grace": 2}), ("P2G6", {"presence": 2, "grace": 6})):
            prof = person("x", at, **MOV)
            people = {"a": dict(prof if side == "for" else mid, id="a"), "b": dict(mid if side == "for" else prof, id="b")}
            inp = build_input(people, row, "full", "argue", actor="a", dials=D, effort=2, **scene_kw(row))
            inp = replace(inp, type=replace(inp.type, standard=D["standard_demand"]["routine"]),
                          room=replace(inp.room, audience="gallery", attention=g["attention"],
                                       distraction=g["distraction"], proof_weight=g["proof_weight"]))
            k = 0 if side == "for" else 1
            c = 0
            est = []
            for t in range(n):
                out, _ = proceed2(inp, draw(("p3b", row, side, t), "a", "r"), {})
                m, _ = P.act_margin(out, inp.type, inp)
                c += (m is not None and degree(m) in CARRIED)
                est.append(out.state.sides[k].esteem)
            me = sum(est) / n
            se = math.sqrt(sum((e - me) ** 2 for e in est) / (n - 1) / n)
            cr = c / n
            win = cr if side == "for" else 1 - cr
            res[nm] = (win, math.sqrt(cr * (1 - cr) / n), me, se)
        a, b = res["P6G2"], res["P2G6"]
        print(f"  {row:12} profile as {side:7}: P(profile prevails) P6G2={a[0]:.3f}±{a[1]:.3f} P2G6={b[0]:.3f}±{b[1]:.3f}"
              f" | end esteem P6G2={a[2]:+.3f}±{a[3]:.3f} P2G6={b[2]:+.3f}±{b[3]:.3f}")
