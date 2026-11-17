"""F16 the petitioner holds the senior seat (stress lane A repro_onechar); fractional weights (A11).
PREDICTION after: an unopposed audience where the petitioner is the senior lawful seat seats the next lawful seat; with
no other seat, a keyed refusal; weights 0.5 and 1.9 refused `bad_weight`, 30 and 30.0 sit.  python -B f16_seat_weight.py"""
from common import *
m = dict(id="m", parties={"for": "a"}, bears={})
H("F16a the petitioner is the senior seat")
pp = {"a": F.P("a", office=F.seat(5, "Crown"), faction="Crown"), "j1": F.P("j1", office=F.seat(3, "Crown"), faction="Crown")}
print("  audience, bench (a, j1):", attempt(lambda: host.build(pp, "audience", m, bench=("a", "j1"), effort=2)[1].decided_by))
print("  audience, bench (a,) alone:", attempt(lambda: host.build(pp, "audience", m, bench=("a",), effort=2)[1].decided_by))
H("F16b weights on the floor of a trial")
mp, M = F.mid_people(), F.matter()
for w in (0, 0.5, 1.9, 30, 30.0, -3):
    q = copy.deepcopy(mp); q["crowd"]["weight"] = w
    print(f"  weight {w!r}:", attempt(lambda: [p.weight for p in host.build(q, "trial", M, bench=BENCH, floor=("crowd",), effort=2)[0].room if p.id == "crowd"]))
