"""v9 SE-03 (rides IN-28) -- `MW-5`, ONE OF THE TWO FALSIFIERS r2 `04_MATTER_AND_WORKS.md` §D.1 NAMES
FOR THE BODY'S BANDS (`:1838`), WRITTEN AND RUN ON A HAND-BUILT WORLD THROUGH THE REAL MATTER BARRIER.
The other, `MW-11` (`:1844`, an upward body-band crossing emits), is RED at this tree for two causes
outside IN-28's lane and is recorded, measured, on `engine/season/hole_register.yaml` `H-211`; it is
not in this file because a red test may not be skipped or xfailed (v9 §0.5).

MW-5's claim, r2's words: *"every declared body band is occupied for at least one season"* before
death -- and *"IT GOES RED AT THE `declared` ARM AND AT `doubled`, AND THAT IS THE POINT ... Control:
the `halved` arm, where it goes green. The row exists so the arm is chosen by arithmetic rather than by
preference."* So it is a test OVER THE ARMS, and both outcomes are asserted, each observed:
  * the arms are `H-125`'s own `sweep:` row, read off the register (the shipped `body_step` is the
    control, `0`, under which no body moves and nobody dies, so MW-5 is vacuous there and is not run);
  * a BAND is a value of `decision/budget.py::body_band_penalty` -- the one reader of
    `band_floors["body"]` a person's budget pays -- `0` at full operations, `+1` per floor fallen below;
  * the world: one cohort (only a cohort eats, `24f`) housed in a settlement with no stores and no
    site, so every season it is short by the whole of its want. The per-season loss is
    `body_step x (its unmet units)`, and whether a band can be stepped over is that loss against the
    band's width. Both are read, not typed: the want off `subsistence_weight`, the floors off
    `band_floors`.
MEASURED at the build (2026-10-16): at `body_step = 10` the cohort loses 60 a season and occupies all
four bands before it dies; at `body_step = 67` it loses 402 a season, falls from `withdrawal_only`
straight to death, and the bottom band (penalty 3) is never occupied -- MW-5 RED at that arm, exactly
r2's reading of its own `declared` arm. So a live `body_step` that keeps the lowest band in play is one
whose loss per season stays under the narrowest band (`band_floors.body.withdrawal_only`, 100 wide).
MUTATIONS, run at the build 2026-10-16 (`loop/matter.py`'s body pass), each restored byte-exact after:
  * the body write's `max(0, ...)` widened to `max(150, ...)` (a body that stops falling short of
    death) -> both arms RED (the cohort never dies in the window).
  * ⚠ NOT CAUGHT, said rather than implied: the loss DOUBLED (`lost = 2 * step * ...`). At arm 10 the
    cohort then loses 120 a season, more than the narrowest band, and still happens to land in every
    band (1000, 880, 760, ... 160, 40), so the arm-10 branch stays green on an arithmetic the test did
    not predict. The test reads occupancy; it is not a guard on the loss magnitude.
"""

from __future__ import annotations

import pytest

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import Step, WriteClass
from ..decision.budget import body_band_penalty
from ..harness import register as REG
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..state.carriers import Person, Rung, Tenure
from ..state.world import World

TOWN, COHORT = "set_famine", "p_famine_folk"
# [JUSTIFIED: a test-fixture size, not a game value -- the smallest weight that is a cohort (S9: weight > 1)]
WEIGHT = 2
H125 = next(r for r in REG.load()["rows"] if r["id"] == "H-125")
CONTROL_ARM = DEFAULT_FIXTURES.get("body_step")
LIVE_ARMS = [arm for arm in H125["sweep"] if arm != CONTROL_ARM]


def _famine(step: int) -> World:
    """A realm > territory > settlement chain holding NOTHING, no Site (so no yield), and one cohort
    housed in the settlement: short by its whole want every season."""
    w = World(0, DEFAULT_FIXTURES.sweep("body_step", step))
    for rid, kind in (("r_realm", "realm"), ("terr_famine", "territory"), (TOWN, "settlement")):
        w.rungs[rid] = Rung(rid, kind)
    w.add_tenure(Tenure("t_in_0", "terr_famine", "r_realm", "contain", 0))
    w.add_tenure(Tenure("t_in_1", TOWN, "terr_famine", "contain", 0))
    w.persons[COHORT] = Person(COHORT, "the famine folk", weight=WEIGHT)
    w.rungs[COHORT] = Rung(COHORT, "person")
    w.add_tenure(Tenure("t_folk_in", COHORT, TOWN, "contain", 0))
    w.add_tenure(Tenure("t_folk_home", COHORT, TOWN, world_q.RESIDE_KIND, 0))
    return w


def _bands_until_death(w: World, limit: int = 60) -> tuple:
    """The penalty the cohort stands at after each MATTER barrier (and at the start), until it dies,
    and whether it died within `limit` seasons."""
    d = SeasonDriver(w)
    seen = [body_band_penalty(w.persons[COHORT], w.fixtures)]
    for _ in range(limit):
        w.step = Step.MATTER
        d.matter(mint_token(w, WriteClass.MATTER), [])
        w.tick += 1
        if COHORT not in w.persons:
            return seen, True
        seen.append(body_band_penalty(w.persons[COHORT], w.fixtures))
    return seen, False


def _loss_per_season(w: World) -> int:
    want = sum(wt * WEIGHT for wt in w.fixtures.get("subsistence_weight").values())
    return w.fixtures.get("body_step") * want


def _narrowest_band(w: World) -> int:
    floors = sorted(w.fixtures.get("band_floors")["body"].values())
    return min([floors[0]] + [b - a for a, b in zip(floors, floors[1:])])


@pytest.mark.parametrize("arm", LIVE_ARMS)
def test_every_body_band_is_occupied_before_death(arm):
    """MW-5, at each live `H-125` arm. Where the loss per season is under the narrowest body band,
    every band (`body_band_penalty` 0..3) is occupied for a season before death -- GREEN. Where it is
    not, the band it steps over is never occupied and the cohort dies from the band above -- MW-5 RED
    at that arm, asserted as observed so the arm is chosen by arithmetic (r2's own words)."""
    assert LIVE_ARMS, "H-125 declares no live arm; MW-5 would pass vacuously"
    w = _famine(arm)
    bands = len(w.fixtures.get("band_floors")["body"]) + 1
    seen, died = _bands_until_death(w)
    assert died, f"at body_step {arm} the cohort did not die in the window: {seen}"
    occupied = set(seen)
    if _loss_per_season(w) < _narrowest_band(w):
        assert occupied == set(range(bands)), (arm, seen)
    else:
        assert occupied != set(range(bands)) and max(occupied) < bands - 1, (arm, seen)


def test_mw5_both_outcomes_are_reached_by_the_shipped_sweep():
    """THE CONTROL r2 asks for: the sweep holds an arm where MW-5 is green AND one where it is red, so
    the test above observes both outcomes on today's register (a sweep all of whose arms fell on one
    side would leave one branch unasserted)."""
    sides = {_loss_per_season(_famine(a)) < _narrowest_band(_famine(a)) for a in LIVE_ARMS}
    assert sides == {True, False}, (LIVE_ARMS, sides)
