"""P6 strain carried across sittings: a season of S sittings between the same two people (auto both sides), r rest
scenes between sittings. B24p.06: strain_carried = max(0, marks_season - strain_rest*scenes_since_last_mark)*press_base.
Control: per-mark recovery (each mark clears after 1/strain_rest scenes on its own; v30 'a mark clears per scene').
    PYTHONHASHSEED=0 python lane3/p6_season.py [n_seasons] [S]"""
import sys
from dataclasses import replace

from harness import person, bench_people, scene_kw, P, dialmod, build_input, draw, degree, CARRIED, proceed2
from scmodel.host import strain_carried

N = int(sys.argv[1]) if len(sys.argv) > 1 else 500
S = int(sys.argv[2]) if len(sys.argv) > 2 else 12
D = dialmod.shipped()
MOV = dict(pursuits={"x": 0.6}, convictions={"c": 3})

for row in ("legal_trial", "questioning", "conversation"):
    for r in (1, 2):
        for rule in ("B24p.06", "per-mark"):
            strain_in = [[0.0, 0.0] for _ in range(S)]
            marks_k = [[0, 0] for _ in range(S)]
            carry = [0] * S
            for s in range(N):
                M = [0, 0]
                since = [0, 0]           # scenes since the last mark (B24p.06)
                ages = [[], []]          # per-mark: scenes since each mark (control)
                for k in range(S):
                    st = []
                    for q in range(2):
                        if rule == "B24p.06":
                            st.append(strain_carried(M[q], since[q], D) if M[q] else 0.0)
                        else:
                            st.append(sum(max(0.0, 1 - D["strain_rest"] * a) for a in ages[q]) * D["press_base"])
                    people = {"a": person("a", **MOV), "b": person("b", **MOV)}
                    people.update(bench_people())
                    inp = build_input(people, row, "full", "argue", actor="a", dials=D, effort=2, **scene_kw(row))
                    sp = tuple(replace(Sp, strain=st[q]) for q, Sp in enumerate(inp.speakers))
                    inp = replace(inp, speakers=sp)
                    out, _ = proceed2(inp, draw(("p6", row, r, rule, s, k), "a", "r"), {})
                    m, veto = P.act_margin(out, inp.type, inp)
                    carry[k] += (m is not None and degree(m) in CARRIED and not veto)
                    for q in range(len(inp.speakers)):
                        mk = out.state.sides[q].marks
                        strain_in[k][q] += st[q]
                        marks_k[k][q] += mk
                        if mk:
                            M[q] += mk
                            since[q] = 0
                            ages[q] += [0] * mk
                    for q in range(2):
                        since[q] += r
                        ages[q] = [a + r for a in ages[q]]
            print(f"{row:12} rest={r} {rule:8}: sitting  " + " ".join(f"{k + 1:>5}" for k in range(0, S, 2)))
            print(f"{'':12} strain-in for/against " + " ".join(f"{strain_in[k][0] / N:.2f}/{strain_in[k][1] / N:.2f}" for k in range(0, S, 2)))
            print(f"{'':12} marks     for/against " + " ".join(f"{marks_k[k][0] / N:.2f}/{marks_k[k][1] / N:.2f}" for k in range(0, S, 2)))
            print(f"{'':12} P(for carried)        " + " ".join(f"{carry[k] / N:9.3f}" for k in range(0, S, 2)))
