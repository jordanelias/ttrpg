"""P4 lopsidedness + P7 emergence. (a) rank curve: `for` rank 1+d vs `against` rank 1, everything else mid, abridged and
full; band shares between equals (A-79: carry 25 / half 16 / fail 59 on routine). (b) random builds (attrs 1..7, ranks
0..3, proofs 0..3, effort 0..4), auto both sides: carry by binned attribute-sum difference; aggregate bands/ends/marks.
    PYTHONHASHSEED=0 python lane3/p4_curve.py [n]"""
import math
import random
import sys
from collections import Counter, defaultdict

from harness import run, person, ATTRS, dialmod, P, proceed2, build_input, bench_people, scene_kw, draw, degree, CARRIED

n = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
D = dialmod.shipped()
MOV = dict(pursuits={"x": 0.6}, convictions={"c": 3})

print("(a) rank curve: P(for carried) [bands F/P/S/O] ; for rank 1+d vs against rank 1")
for row in ("conversation", "negotiation", "questioning", "legal_trial"):
    for form in ("abridged", "full"):
        if form == "abridged" and row in ("negotiation", "questioning"):
            continue
        line = []
        for d in (-2, -1, 0, 1, 2, 4):
            A = person("a", rank=max(0, 1 + d) if d >= -1 else 0, **MOV)
            B = person("b", rank=1 if d >= -1 else 1 - d - 1, **MOV)
            if d < 0:
                A = person("a", rank=1, **MOV)
                B = person("b", rank=1 - d, **MOV)
            else:
                A = person("a", rank=1 + d, **MOV)
                B = person("b", rank=1, **MOV)
            people = {"a": A, "b": B}
            people.update(bench_people())
            inp = build_input(people, row, form, "argue", actor="a", dials=D, effort=2,
                              **({"addressed": "b"} if form == "abridged" and row != "legal_trial" else scene_kw(row)))
            bands = Counter()
            for t in range(n):
                out, _ = proceed2(inp, draw(("p4a", row, form, d, t), "a", "r"), {})
                m, veto = P.act_margin(out, inp.type, inp)
                bands[None if m is None else degree(m)] += 1
            c = (bands["success"] + bands["overwhelming"]) / n
            fr = "/".join(f"{bands[b] / n:.2f}" for b in ("failure", "partial", "success", "overwhelming"))
            line.append(f"d={d:+d}:{c:.3f}[{fr}]")
        print(f"  {row:12} {form:8} " + " ".join(line))

print("\n(b) random builds, auto both sides; carry by (for attr-sum - against attr-sum) bin; and aggregates")
for row in ("conversation", "negotiation", "questioning", "legal_trial", "arbitration"):
    bins = defaultdict(lambda: [0, 0])
    bands, ends, endside = Counter(), Counter(), Counter()
    marks = Counter()
    lead_yield = 0
    for t in range(n):
        rnd = random.Random(hash(("p4b", row, t)))
        A = person("a", {k: rnd.randint(1, 7) for k in ATTRS}, rank=rnd.randint(0, 3), proofs=rnd.randint(0, 3),
                   pursuits={"x": rnd.random()}, convictions={"c": rnd.randint(0, 5)})
        B = person("b", {k: rnd.randint(1, 7) for k in ATTRS}, rank=rnd.randint(0, 3), proofs=rnd.randint(0, 3),
                   pursuits={"x": rnd.random()}, convictions={"c": rnd.randint(0, 5)})
        people = {"a": A, "b": B}
        people.update(bench_people({k: rnd.randint(1, 7) for k in ATTRS}))
        inp = build_input(people, row, "full", "argue", actor="a", dials=D, effort=rnd.randint(0, 4), **scene_kw(row))
        out, es = proceed2(inp, draw(("p4b", row, t), "a", "r"), {})
        m, veto = P.act_margin(out, inp.type, inp)
        b = None if m is None else degree(m)
        if veto and b in CARRIED:
            b = "failure"
        diff = sum(A["attributes"].values()) - sum(B["attributes"].values()) + 2 * (A["ranks"]["argue"] - B["ranks"]["argue"])
        k = max(-4, min(4, round(diff / 4)))
        bins[k][0] += b in CARRIED
        bins[k][1] += 1
        bands[b] += 1
        ends[out.ended] += 1
        if es is not None:
            sd = inp.speakers[es].side
            endside[(out.ended, sd)] += 1
            if out.ended == "yielded" and P.SIGN[sd] * out.state.track > 0:
                lead_yield += 1
        for S, s in zip(inp.speakers, out.state.sides):
            marks[s.marks] += 1
    curve = " ".join(f"{4 * k:+d}:{v[0] / v[1]:.2f}(n{v[1]})" for k, v in sorted(bins.items()))
    print(f"  {row:12} curve {curve}")
    print(f"  {'':12} bands={ {k: round(v / n, 3) for k, v in bands.items()} } ends={ {k: round(v / n, 3) for k, v in ends.items()} }"
          f" endside={dict(endside)} yielder-was-leading={lead_yield} marks-per-side-dist={dict(sorted(marks.items()))}")
