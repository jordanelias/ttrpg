"""v9 SC-01 step 14 -- THE OBSTACLE CEILING (`workplans/valoria_master_workplan_v9_part6.md` §SC-01, the
CARRIED block's *Step 14*: Contradiction 3 resolved -- take the obstacle CEILING, its value injected and
swept, never a pool floor; the seam's own obstacle site is deleted, ED-SC-0033 clause (3), one owner).

WHAT IS BUILT, and where each piece is read:
  * THE OWNER. `modules/social_contest/roll.py::obstacle` composes a social contest's obstacle -- the
    opposition's score halved, the `obstacle_default` stand-in where there is no score, bounded above
    by the ceiling. The host input builder (`seam/wrappers/sigma.py::contest_input`) carries the raw
    operands in `SocialContestInput` and composes nothing: the record has no `ob` field to put a
    second site's value in.
  * THE CEILING. `Fixtures obstacle_ceiling` (`H-213`), injected into the record, swept [1, 2, 3].
    `None` is the CONTROL arm (no ceiling, the tree before this step).
  * ED-SC-0038's PICK, made here: PER MATTER. One injected value bounds the obstacle of EACH matter's
    draw independently; there is no aggregate obstacle over a bundle of matters (`H-213`'s `default:`).

M-7 (`proposals/2026-09-05-proceedings-subsystem/19_PLAN.md` M-7; run at `21_RECONCILIATION.md`'s
PHASE 0 result): at the 1D pool floor against the maximum plausible composed obstacle, `p_success`
must not be effectively zero. "EFFECTIVELY ZERO" is named here, not left to a reader:
`EFFECTIVELY_ZERO = 0.001`, because the reconciliation's own table calls its Ob-3 row (0.0006) the
point where the floor "reaches zero". The quantity is `sigma_leverage.p_success(ob, pool=1)` with
`ob = obstacle(record)` for a requested obstacle of 4..11 (`opposition = 2 x Ob`), plus the EXACT
discrete chance of a non-Failure band at 1D through the real module entry and the real ladder (each
of the ten d10 faces forced in turn).

THE FALSIFIERS (each seen red before the build, 2026-10-16: the record had no `opposition` /
`obstacle_ceiling` field, `DEFAULT_FIXTURES` no `obstacle_ceiling`, `sigma` still held `_obstacle_of`):
  * M-7 at the floor clears Ob >= 4 with the ceiling, and FAILS on the control arm (no ceiling).
  * the sweep straddles M-7's boundary: the arm at 3 fails it, so the test can observe a failure.
  * the seam has no second obstacle site: the obstacle on a resolved act FOLLOWS the module's
    function when that function is replaced (a call, not a copy).
  * the ceiling is injected: changing the fixture changes the act's obstacle and its band
    distribution through the real seam on a hand-built world.
"""

from __future__ import annotations

import importlib
import random
from dataclasses import fields

import pytest

from engine.dice_engine.dice_engine import DEGREE_LABEL, Degree
from engine.dice_engine.sigma_leverage import LEVEL_SIGMA, p_success
from engine.substrate import composition

from ..data.fixtures import DEFAULT_FIXTURES
from ..harness import probes as P
from ..harness import register as REG
from ..loop.driver import SeasonDriver
from ..queries.inputs import SocialContestInput
from ..seam import ladder
from ..seam.wrappers import sigma

EFFECTIVELY_ZERO = 0.001
FLOOR = 1                       # the 1D pool floor (`sigma_leverage.roll_net`, `p_success`)
M7_OBS = range(4, 12)           # requested obstacles 4..11 (11: the reconciliation's own pool sweep)
FAILURE = DEGREE_LABEL[Degree.FAILURE]
ROW = "H-213"


def _module():
    """The `social_contest` module, found the way the host finds it: by the composition row's target
    string (`engine/` never imports module code by name)."""
    target = composition.ROLES["social_contest.roll"]["target"]
    return importlib.import_module(target.split(":", 1)[0])


def _record(opposition, ceiling, *, pool=FLOOR, leverage=0.0):
    return SocialContestInput(
        pool=pool, opposition=opposition,
        obstacle_default=DEFAULT_FIXTURES.get("obstacle_default"),
        obstacle_ceiling=ceiling,
        obstacle_refusal_multiple=DEFAULT_FIXTURES.get("obstacle_refusal_multiple"),
        leverage=leverage)


class _Face:
    """An rng whose d10 always shows `face` -- so the ten faces of a 1D roll can be enumerated
    EXACTLY through the real entry (`roll_net` -> `dice_engine.roll_pool` -> `rng.randint`)."""

    def __init__(self, face):
        self.face = face

    def randint(self, a, b):
        assert (a, b) == (1, 10), (a, b)
        return self.face


def _discrete_hits(mod, rec) -> int:
    """How many of the ten 1D faces the real entry + the real ladder grade above Failure."""
    return sum(ladder.degree_of(mod.roll(rec, _Face(f))) != FAILURE for f in range(1, 11))


def _m7(mod, ceiling) -> dict:
    """M-7 at the 1D floor for each requested obstacle in `M7_OBS`, on one ceiling arm."""
    out = {}
    for ob in M7_OBS:
        rec = _record(2 * ob, ceiling)
        eff = mod.obstacle(rec)
        out[ob] = (eff, p_success(eff, FLOOR), _discrete_hits(mod, rec))
    return out


def test_m7_at_the_1d_floor_clears_ob_4_and_above_under_the_ceiling_and_fails_without_it():
    mod = _module()
    shipped = DEFAULT_FIXTURES.get("obstacle_ceiling")
    assert shipped is not None, "the shipped arm is the control; the ceiling is not wired"
    before, after = _m7(mod, None), _m7(mod, shipped)
    checked = 0
    for ob in M7_OBS:
        eff0, p0, hits0 = before[ob]
        eff1, p1, hits1 = after[ob]
        # CONTROL: with no ceiling the composed obstacle IS the requested one, and M-7 fails --
        # the reconciliation's measurement, reproduced through the owner rather than cited.
        assert eff0 == ob, (ob, eff0)
        assert p0 < EFFECTIVELY_ZERO and hits0 == 0, (
            f"control arm: Ob {ob} at 1D gave p_success {p0:.6f} and {hits0}/10 faces -- M-7 "
            f"should FAIL without a ceiling; if it passes, the instrument cannot see the failure")
        # THE CLAIM: the ceiling bounds the obstacle, and the floor-pool speaker keeps a chance.
        assert eff1 == shipped, (ob, eff1)
        assert p1 >= EFFECTIVELY_ZERO and hits1 >= 1, (
            f"Ob {ob} at the 1D floor under ceiling {shipped}: p_success {p1:.6f}, {hits1}/10 "
            f"faces -- M-7 still fails (`EFFECTIVELY_ZERO` = {EFFECTIVELY_ZERO})")
        checked += 1
    assert checked == len(M7_OBS)
    # CONTROL 2: an obstacle BELOW the ceiling is untouched -- the ceiling bounds, it does not shift.
    for ob in (1, 2):
        if ob <= shipped:
            assert mod.obstacle(_record(2 * ob, shipped)) == mod.obstacle(_record(2 * ob, None)) == ob
    # M-7's second clause: without the ceiling, BUYING ADVANTAGE does not rescue Ob 4 at the floor
    # (remedy (a) refuted, `21_RECONCILIATION.md`) -- every rostered level stays effectively zero.
    for lv, s in LEVEL_SIGMA.items():
        assert p_success(4, FLOOR, s) < EFFECTIVELY_ZERO, (lv, p_success(4, FLOOR, s))
        # and under the ceiling the σ-channel is live again, monotonic in the level bought.
        assert p_success(shipped, FLOOR, s) > p_success(shipped, FLOOR, 0.0), lv


def test_the_ceiling_is_swept_and_the_sweep_straddles_m7():
    """`H-213` declares the sweep; each point is RUN, not listed. A verdict that flips across the
    sweep is itself the finding S42.2.1 asks for: the arm at 3 fails M-7, so this test can observe
    a failure, and the shipped arm passes."""
    rows = {r["id"]: r for r in REG.load()["rows"]}
    row = rows.get(ROW)
    assert row is not None, f"{ROW} (the ceiling's register row) is missing"
    assert row["grade"] == "assumption", row["grade"]
    assert "obstacle_ceiling" in row["site"] and "roll.py::obstacle" in row["site"], row["site"]
    sweep = row["sweep"]
    assert len({str(x) for x in sweep}) >= 3, sweep
    assert DEFAULT_FIXTURES.get("obstacle_ceiling") in sweep, sweep
    mod = _module()
    verdict = {}
    for c in sweep:
        m = _m7(mod, c)
        verdict[c] = all(p >= EFFECTIVELY_ZERO and hits >= 1 for _, p, hits in m.values())
        assert all(eff == c for eff, _, _ in m.values()), (c, m)   # each arm reaches the record
    assert verdict[DEFAULT_FIXTURES.get("obstacle_ceiling")], verdict
    assert not all(verdict.values()), (
        f"every sweep point passes M-7 ({verdict}); the sweep cannot observe the failure")


def test_the_seam_has_no_second_obstacle_site(monkeypatch):
    """ED-SC-0033 clause (3): one owner. The host's record has no field an obstacle could travel in,
    the host builder holds no obstacle function, and a resolved act's obstacle is whatever the
    module's `obstacle` returns -- replace that function and the act follows it."""
    assert "ob" not in {f.name for f in fields(SocialContestInput)}, (
        "the host record carries an `ob`: a host-derived obstacle can reach the roll again")
    assert not hasattr(sigma, "_obstacle_of"), "the seam's own obstacle site is back"
    mod = _module()
    w = P.tiny_world(DEFAULT_FIXTURES)
    SeasonDriver(w)                                  # the registrar fills MODULE_ENTRIES
    w.persons["p_mid"].capability = {"copying": 3}
    seen = sigma.resolve(w, ["p_low"], ["c"], "a standing", verb="tell", subject="p_mid",
                         rng=random.Random(0))
    assert seen["status"] == "RESOLVED" and seen["ob"] == 1.5, seen
    monkeypatch.setattr(mod, "obstacle", lambda inp: 1.25)
    moved = sigma.resolve(w, ["p_low"], ["c"], "a standing", verb="tell", subject="p_mid",
                          rng=random.Random(0))
    assert moved["ob"] == 1.25, (
        f"the act's obstacle did not follow the owner ({moved}): something else composes it")


def _arm(ceiling):
    w = P.tiny_world(DEFAULT_FIXTURES.sweep("obstacle_ceiling", ceiling))
    SeasonDriver(w)
    # roster-exempt: TEST FIXTURE capabilities -- one matter far over every sweep point, one under.
    w.persons["p_mid"].capability = {"copying": 10}       # score/2 = 5
    w.persons["p_other"].capability = {"copying": 3}      # score/2 = 1.5
    return w


@pytest.mark.parametrize("subject,want", [("p_mid", {2: 2.0, 3: 3.0}),
                                          ("p_other", {2: 1.5, 3: 1.5}),
                                          ("p_king", {2: 2.0, 3: 2.0})])
def test_the_ceiling_is_injected_and_bounds_each_matter_on_its_own(subject, want):
    """Through the real seam on a hand-built world: the fixture's value is what bounds the act's
    obstacle (2 -> 2.0, 3 -> 3.0 for a subject whose score/2 is 5), an obstacle under the ceiling is
    untouched (1.5), and the no-score stand-in (`obstacle_default` 2) is bounded the same way.
    PER MATTER (ED-SC-0038): each subject's draw is bounded on its own; nothing aggregates them."""
    for c, ob in want.items():
        out = sigma.resolve(_arm(c), ["p_low"], ["c"], "a standing", verb="tell", subject=subject,
                            rng=random.Random(0))
        assert out["status"] == "RESOLVED" and out["ob"] == ob, (c, out)


def test_changing_the_ceiling_changes_the_outcome():
    """The band distribution over the same seeds moves when only the fixture moves."""
    hits, differ = {}, 0
    worlds = {c: _arm(c) for c in (2, 3)}
    for s in range(300):
        bands = {c: ladder.degree_of(sigma.resolve(w, ["p_low"], ["c"], "a standing", verb="tell",
                                                   subject="p_mid", rng=random.Random(s)))
                 for c, w in worlds.items()}
        for c, b in bands.items():
            hits[c] = hits.get(c, 0) + (b != FAILURE)
        differ += bands[2] != bands[3]
    assert differ > 0 and hits[2] > hits[3], (hits, differ)
