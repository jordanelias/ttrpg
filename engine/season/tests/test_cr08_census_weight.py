"""B12b.35 (`07_SE_population_census` §4 (a), H-305): THE BODY LOSS IS PER HEAD, behind the fixture `hunger_loss`.

WHAT IS ASKED: on a hand-built world of two settlements with empty larders, one holding a cohort at weight 2 and one at weight 20, each short its
whole want (so the same per-head shortfall), `settlements.subsist` falls the weight-20 body ten times the weight-2 body's fall at `per_cohort` (the
shipped control, H-305's defect) and the same fall at `per_head`, which is half of what the weight-2 cohort lost at the control.
Observed through `world_q.subsist_input`, so the fixture's projection is read, not only the module's arithmetic. `hunger_severity_draw` is off so
the step is the fixed one (no draw rides on it).
"""
from __future__ import annotations

from ..boot.realm import place_person
from ..data.fixtures import DEFAULT_FIXTURES
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
