"""B12b.35 (`07_SE_population_census` §4 (a), H-305): THE BODY LOSS IS PER HEAD, behind the fixture `hunger_loss`.

WHAT IS ASKED: on a hand-built world of two settlements with empty larders, one holding a cohort at weight 2 and one at weight 20, each short its
whole want (so the same per-head shortfall), `settlements.subsist` falls the weight-20 body ten times the weight-2 body's fall at `per_cohort` (the
shipped control, H-305's defect) and the same fall at `per_head`, which is half of what the weight-2 cohort lost at the control.
Observed through `world_q.subsist_input`, so the fixture's projection is read, not only the module's arithmetic. `hunger_severity_draw` is off so
the step is the fixed one (no draw rides on it).

B12b.36 (`07_SE_population_census` (b), (c)): A STARVING COHORT THINS BEFORE IT DIES, behind the fixture `famine_loss`. Observed on `harness/scarce.build` (a
cohort at `set_hungry`, its larder drained), run by the real season driver with no chooser (so no `tend` raises the body back), the cohort's weight and body
planted. Each season is read from the world's own people and log, so the writer is observed reaching `Person.weight` and its readers (`world_q.demanded`).
"""
from __future__ import annotations

from ..boot.realm import place_person
from ..data.fixtures import DEFAULT_FIXTURES
from ..harness import probes as P
from ..harness import scarce
from ..loop.driver import SeasonDriver
from ..queries import world_q
from ..state.carriers import Rung, Tenure
from ..state.world import World
from engine.substrate import composition

BODY, LIGHT, HEAVY = 1000, 2, 20


def _falls(hunger_loss):
    """`{pid: body lost}` for the two cohorts planted, from the real `subsist` entry over the real projection."""
    fx = DEFAULT_FIXTURES.sweep("hunger_severity_draw", False)
    fx = fx if hunger_loss is None else fx.sweep("hunger_loss", hunger_loss)
    w = World(world_seed=0, fixtures=fx)
    w.rungs["R"], w.rungs["T"] = Rung("R", "realm"), Rung("T", "territory")
    w.add_tenure(Tenure("t_T", "T", "R", "contain", since=0))
    for pid, weight in (("light", LIGHT), ("heavy", HEAVY)):
        sid = f"set_{pid}"
        w.rungs[sid] = Rung(sid, "settlement")
        w.add_tenure(Tenure(f"t_{sid}", sid, "T", "contain", since=0))
        place_person(w, pid, pid, sid, weight=weight, body=BODY)
    out = composition.require("settlements.subsist")(world_q.subsist_input(w))
    lost = {f.pid: BODY - f.body_after for f in out.falls}
    assert set(lost) == {"light", "heavy"}, "a cohort was not short: the arm cannot observe the loss"
    return lost


def test_per_head_halves_the_loss_at_weight_two():
    control, per_head = _falls("per_cohort"), _falls("per_head")
    assert per_head["light"] * LIGHT == control["light"], (control, per_head)       # halved at the shipped weight 2
    assert per_head["heavy"] == per_head["light"] > 0, per_head                     # a weight-20 cohort loses what a weight-2 one does


def test_per_cohort_is_the_control():
    control = _falls("per_cohort")
    assert _falls(None) == control, "the shipped arm is not `per_cohort`"
    assert control["heavy"] == control["light"] * (HEAVY // LIGHT), control          # H-305's defect, visible at the control


def _famine(weight, body, seasons, famine_loss):
    """`scarce.build` under `hunger_loss per_head` with the one cohort's weight and body planted and the drained-larder draw's loss fixed (no severity draw),
    run `seasons` seasons with no chooser. Returns `(world, [(weight, body, demanded units) or None per season])`; `None` is a cohort that is gone."""
    fx = (DEFAULT_FIXTURES.sweep("famine_loss", famine_loss).sweep("hunger_loss", "per_head")
          .sweep("hunger_severity_draw", False))
    w = scarce.build(0, fx)
    w.persons[scarce.POPULACE].weight, w.persons[scarce.POPULACE].body = weight, body
    d, seen = SeasonDriver(w), []
    for _ in range(seasons):
        d.season(P.NOCHOOSE, question=None, contest_max_depth=w.fixtures.get("contest_max_depth"))
        p = w.persons.get(scarce.POPULACE)
        seen.append(None if p is None else (p.weight, p.body, sum(dict(world_q.demanded(w, scarce.HUNGRY)).values())))
    return w, seen


def _caused_by_a_body_write(w, kind):
    by_id = {e.id: e for e in w.log}
    rows = [e for e in w.log if e.kind == kind]
    return rows, all(e.causes and e.causes[0] in by_id and by_id[e.causes[0]].kind == "body.changed" for e in rows)


def test_hungry_cohort_thins_ten_five_three():
    w, seen = _famine(10, 90, 2, 500)                                     # 90 stands under `withdrawal_only` (100)
    assert [s[0] for s in seen] == [5, 3], seen                           # 10 -> 5 -> 3
    assert seen[1][2] < seen[0][2] < 30, seen                             # `demanded` falls with the weight (a weight-10 cohort wants 30 units)
    rows, caused = _caused_by_a_body_write(w, "weight.changed")
    assert len(rows) == 2 and caused, "a thinning was not written, or not caused by the body write that stands under the floor"
    over, over_seen = _famine(10, 500, 2, 500)                            # the same famine over the floor: no thinning
    assert [s[0] for s in over_seen] == [10, 10] and not [e for e in over.log if e.kind == "weight.changed"], over_seen


def test_cohort_at_weight_three_thins_to_one_and_dies_only_there():
    w, seen = _famine(3, 5, 2, 500)
    assert seen[0][:2] == (2, 0), seen                                    # body 0 at weight 2: thinned, NOT dead
    assert seen[1] is None, "the cohort was not removed at weight 1 and body 0"
    tick1 = [e.kind for e in w.log if e.emitted_at == 1]
    assert tick1.index("weight.changed") < tick1.index("person.died"), tick1   # it thinned to 1 first, then died


def test_famine_loss_zero_is_the_control():
    w, seen = _famine(3, 5, 1, 0)
    assert seen == [None], "at `famine_loss` 0 a cohort at body 0 did not die as it does today"
    assert not [e for e in w.log if e.kind == "weight.changed"]
