"""IN-08 H9 (`workplans/valoria_master_workplan_v9_part5.md`) -- the CRISIS READER, THRESHOLD 2 ONLY:
a person whose scar count on a pursuit has reached 2 gives that pursuit's weight up to the others,
as the swept `Fixtures` arm `scar_weight_shift` (control `0`, shipped), read where `choose` scores.

THE PLAN'S FALSIFIER: fork divergence at the `total` arm rises above the baseline while the control
arm is unmoved. ⚠ THE BASELINE IS A PROXY, NOT ED-IN-0261'S. It is the W-D NPC-088 slice, one seed
(29 genuine / 6 diverged at `observation_deposit_mode=total`; the arm at 1 reads 32/10). ED-IN-0261's
own figure (2,403 forks reconverge 100%, later-decision divergence ~4%) is a corpus figure and was
NOT re-taken here, so this test does not say the arm closes that loop. And 6 -> 10 is not a rate over
the same forks: the genuine population moves too (29 -> 32), so read diverged/genuine as a pair or a
rate (6/29 -> 10/32). Each clause is an executed test below that can fail:
  * the control (`0`) is the unmodified read -- `crisis_weights` returns `Person.pursuits` ITSELF, and
    the `W-D` slice at `total` reads the baseline pair `test_season_shape.py` pins (29 genuine, 6
    diverged) when the arm is `0`;
  * the non-zero arm moves it: diverged at `total` rises above that baseline (a vacuous arm -- one
    nobody's scar reaches -- would leave it at 6, so the assertion can fail);
  * the arm is a READER: it writes no `Person` field and moves no scar;
  * a one-season populated world is moved by the arm (hash differs from the control) and holds
    people the shift can act on -- at the threshold, with another pursuit to give weight to.
"""
from __future__ import annotations

import pytest

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.pursuits import to_axes
from ..decision.options import project
from ..harness import corpus_run as C
from ..harness import run_cases as R
from ..harness.populated import build_realm, run
from ..queries.person_q import SCAR_WEIGHT_SHIFT_AT, crisis_weights
from ..state.carriers import Person
from .test_season_shape import _wd_arm9

# `W-D`'s `total` arm at the control, as `test_season_shape.py::test_wd_a_fork_changes_a_later_
# decision_...` pins it: [GROUNDED: measured at IN-08 H3's base (bf3c3810), NPC-088 slice, seed 0,
# 4 seasons at 2 slots -- genuine/diverged `total` 29/6, `none` 37/4, `actor` 35/9]. A one-slice,
# one-seed PROXY for ED-IN-0261's corpus figure, which was not re-taken.
# ⚠ 29/6 -> 26/6, v9 IN-11 (#453 §10.4 step 2), the same move `test_season_shape.py`'s W-D pins
# record: `_eff_utter` opens the utterer's `hold`, so the fork population moved and the divergence
# count did not. A re-record of the control, read off this test's own failing assertion.
_BASELINE_TOTAL = (26, 6)


def _person(pursuits: dict, scar: dict) -> Person:
    p = Person(id="p_h9", name="p_h9")
    p.pursuits = dict(pursuits)
    p.scar = dict(scar)
    return p


def test_h9_threshold_two_shifts_that_pursuit_down_and_the_others_gain_proportionally():
    p = _person(dict(virtue=0.6, honour=0.3, wealth=0.1), {"virtue": SCAR_WEIGHT_SHIFT_AT})
    w = crisis_weights(p, 0.5)
    assert w["virtue"] == pytest.approx(0.3)
    assert w["honour"] == pytest.approx(0.3 + 0.3 * 0.75)
    assert w["wealth"] == pytest.approx(0.1 + 0.3 * 0.25)
    assert sum(w.values()) == pytest.approx(1.0), "the shift must conserve total weight"
    assert p.pursuits == dict(virtue=0.6, honour=0.3, wealth=0.1), "the reader wrote Person.pursuits"
    assert p.scar == {"virtue": SCAR_WEIGHT_SHIFT_AT}, "the reader wrote Person.scar"


def test_h9_below_threshold_and_at_control_the_read_is_the_unmodified_one():
    pursuits = dict(virtue=0.6, honour=0.3)
    one_short = _person(pursuits, {"virtue": SCAR_WEIGHT_SHIFT_AT - 1})
    assert crisis_weights(one_short, 1.0) == pursuits, "threshold 2 fired at a count of 1"
    scarred = _person(pursuits, {"virtue": 5})
    assert crisis_weights(scarred, 1.0) != pursuits, "a count of 5 did not shift: the arm is inert"
    # the control: the arm at 0 hands back the person's own mapping, not an equal copy
    assert crisis_weights(scarred, 0) is scarred.pursuits
    assert project(scarred, 0) == project(scarred) == to_axes(pursuits)
    assert project(scarred, 1.0) != project(scarred), "the shift does not reach the projection"


def test_h9_a_person_with_nobody_to_gain_is_unshifted_not_drained():
    everything = _person(dict(virtue=0.6, honour=0.4), dict(virtue=3, honour=2))
    assert crisis_weights(everything, 1.0) == everything.pursuits
    assert crisis_weights(_person({"virtue": 1.0}, {"virtue": 9}), 1.0) == {"virtue": 1.0}


def _wd_total(shift):
    A9 = _wd_arm9()
    case = C.apply_rescale(next(c for c in R.load_cases("NPC") if c["id"] == "NPC-088"))
    fx = (DEFAULT_FIXTURES.sweep("scene_budget", 2).sweep("interactions_per_scene", 1)
          .sweep("observation_deposit_mode", "total").sweep("scar_weight_shift", shift))
    r = A9.fork_case(case, 0, 4, fixtures=fx)
    assert r["ok"], r.get("why")
    real = [f for f in r["forks"] if f.get("status") in ("DIVERGED", "RECONVERGED")]
    return len(real), sum(1 for f in real if not f["reconverged"])


def test_h9_fork_divergence_at_total_rises_above_baseline_and_the_control_arm_is_unmoved():
    """THE PLAN'S FALSIFIER. [GROUNDED: measured on this tree (H9), NPC-088 slice, seed 0, 4 seasons
    at 2 slots, `total` deposit arm -- genuine/diverged `scar_weight_shift` 0 -> 29/6 (the baseline,
    UNMOVED), 0.5 -> 29/6, 1 -> 32/10. At 0.5 the `total` arm does not move on this slice; the
    arm is swept at {0, 0.5, 1}, and the verdict that flips across the sweep is the finding.]
    A PROXY for ED-IN-0261's corpus figure (2,403 forks, 100% reconverge, ~4% later-decision
    divergence), which this test did not re-take; and 6 -> 10 is not a rate over the same forks,
    since the genuine count moves as well (29 -> 32): the pair is 6/29 -> 10/32, about 21% -> 31%.
    [GROUNDED: re-measured at v9 IN-11 -- `scar_weight_shift` 0 -> 26/6 (the re-recorded baseline),
    0.5 -> 28/6, 1 -> 32/10: the shifted arm is unmoved and still rises above the control.]"""
    control = _wd_total(0)
    assert control == _BASELINE_TOTAL, (
        f"the control arm moved the `total` fork pair: {control} != {_BASELINE_TOTAL}")
    shifted = _wd_total(1)
    assert shifted[1] > _BASELINE_TOTAL[1], (
        f"the weight shift at 1 left `total` divergence at {shifted} (baseline {_BASELINE_TOTAL}): "
        "no scarred person's ranking reached a later decision, so the arm is inert here")


def test_h9_the_arm_moves_a_populated_season_and_has_someone_to_act_on():
    """One populated season, the control against `scar_weight_shift` 1. [GROUNDED: measured on this
    tree (H9) -- control `c0c161b8`, the hash the base (bf3c3810) gives; `0.5` -> `36be6f6d`, `1` ->
    `cbfb0139`.] The shifted run differs from the control. And at the control there are people AT the threshold with another held
    pursuit below it -- otherwise `crisis_weights` returns them unshifted and a differing hash
    would have to come from somewhere else."""
    hashes, actable, held = {}, 0, 0
    for shift in (0, 1):
        w = build_realm(0)
        w.fixtures = w.fixtures.sweep("scar_weight_shift", shift)
        run(seasons=1, seed=0, w=w)
        hashes[shift] = w.content_hash()
        if shift == 0:
            people = [p for p in w.persons.values() if p.pursuits]
            held = len(people)
            actable = sum(1 for p in people if crisis_weights(p, 1.0) != p.pursuits)
            at_two = sum(1 for p in people
                         if any(c >= SCAR_WEIGHT_SHIFT_AT for c in p.scar.values()))
            print(f"\n  H9 -- one season, control: {held} persons hold pursuits, {at_two} at/over "
                  f"threshold {SCAR_WEIGHT_SHIFT_AT} on >=1 pursuit, {actable} the shift can move")
    assert actable > 0, "nobody is at the threshold with an heir: the arm has nothing to read"
    assert hashes[0] != hashes[1], "the arm at 1 left the season's hash unmoved"
