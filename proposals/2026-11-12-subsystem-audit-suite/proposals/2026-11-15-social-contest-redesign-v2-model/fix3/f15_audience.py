"""F15 an audience with no opponent (stress lane A g_solo). Petitioner a (no office) before one judge.
PREDICTION after: with nobody opposite the judge's station is no obstacle: P(for) equals the gap_step-0 arm, and does
not fall with the judge's rung (awe still acts on the petitioner's composure).  python -B f15_audience.py N"""
from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
m = dict(id="m", parties={"for": "a"}, bears={})
H(f"F15 audience, no opponent; P(for), n={N}")
for lv in ("r2", "r5M"):
    row = []
    for lab, D in (("shipped", host.dials()), ("gap_step 0", host.dials(gap_step=0.0))):
        pp = {"a": F.P("a"), "j1": F.P("j1", office=office(lv, "Crown"), faction="Crown")}
        k = sum(sit(pp, "audience", m, ("so", i), bench=("j1",), effort=2, D=D)[3][0] in CARRIED for i in range(N))
        row.append(f"{lab} {pc(k, N)}")
    print(f"  judge {lv}: " + " | ".join(row), flush=True)
H(f"F15 control: the tell, where the one addressed IS the man opposite (a power-6 respondent; Presence dice only); n={N // 3}")
from sc2.engine import Choice as _C
def sol(v, me):
    o = max((o for o in v.options if o.move == "argue" and o.ground == "solidarity"), key=lambda o: o.ev); return _C(o.move, o.ground, o.item, o.relation)
for lab, D in (("shipped", host.dials()), ("gap_step 0", host.dials(gap_step=0.0))):
    row = []
    for rs in (1, 7):
        pp = F.mid_people(); pp["b"]["office"] = F.seat(4, "Crown", "moderate"); pp["a"]["attributes"]["reason"] = rs
        k = sum(sit(pp, "conversation", F.matter(), ("sw", i), form="abridged", D=D, deciders={"a": sol})[3][0] in CARRIED for i in range(N // 3))
        row.append(f"Reason {rs} {pc(k, N // 3)}")
    print(f"  {lab:10}: " + " | ".join(row))
