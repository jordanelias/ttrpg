"""Numbers quoted in SPEC_GAPS (readings, not assertions)."""
import scmodel  # noqa
from scmodel import dials, proceeding as P
from scmodel.demo import run_one, default_people
from scmodel.dice import degree
S = dials.shipped()
n = 1000
# G39: negotiation (mutual) act band vs track
hi_neg = sum(1 for i in range(n) if (lambda r: r[3] in ("success", "overwhelming") and r[1].state.track < 0)(
    run_one("negotiation", seed=("g39", i), D=S, people=default_people(i))))
print(f"G39 negotiation: act band >= success while track < 0 (against the actor): {hi_neg}/{n}")
# G44: yields by attrition (no press) and by the leading side
y = lead = nopress = 0
for i in range(n):
    inp, out, m, b = run_one("legal_trial", seed=("g44", i), D=S, people=default_people(i))
    if out.ended == "yielded":
        y += 1
        k = next(k for k, s in enumerate(out.state.sides) if s.resolve <= 0)
        sgn = 1 if inp.speakers[k].side == "for" else -1
        lead += int(sgn * out.state.track > 0)
        nopress += int(out.state.sides[k].marks == 0)
print(f"G44 legal_trial effort 2: yielded {y}/{n}; the yielding side was LEADING the track in {lead}; "
      f"had taken no mark in {nopress}")
# G13: bench ballot carried share at track +3 vs hearer
for row in ("legal_trial", "conversation"):
    car = tot = 0
    for i in range(n):
        inp, out, m, b = run_one(row, seed=("g13", i), D=S, people=default_people(i))
        if out.state.track >= 2.9:
            tot += 1
            car += int(b in ("success", "overwhelming"))
    print(f"G13 {row}: sittings ending with track >= +2.9: {tot}; carried for `for`: {car}")
inp, out, m, b = run_one("legal_trial", seed=0, D=S)
for d in inp.deciders:
    print(f"   bench seat {d.id}: pool {d.pool} score {d.score}; hearer base pool would be 8")
# G42: min exchanges never enforced
inp, out, m, b = run_one("parliamentary_debate", seed=1, D=S, effort=0)
print(f"G42 parliamentary_debate (exchanges [3,5]) at act effort 0: {len(out.exchanges)} exchanges, ended {out.ended}")
