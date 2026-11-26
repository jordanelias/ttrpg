"""B12b.01 (CP-T10-03) -- THE SEASON OF THE YEAR'S TERMS (`rosters.yaml: season_terms`, `data/rosters.py::SEASON_TERMS`).

WHAT IS ASKED, each on a hand-built town (one settlement, one cohort of weight 2, a larder) and the real MATTER barrier:
  * `want` scales the per-head weight WHERE THE DRAW IS PROJECTED (`world_q._larder_parts`), so the Query (`demanded`), REM-50's `hunger` and
    MATTER's draw read one number: a weight-2 cohort wants grain 6 at a winter tick and 4 at tick 0, and a salt weight of 1 under 1.5 is 2;
  * `yield` multiplies `season_factor_of`'s drawn return, and only when the draw table is non-empty;
  * at the SHIPPED terms (every multiplier 1.0) the projection is the bare weights at every tick.
The swept arm (winter yield 0.25, want 1.5, illness 2.0: CP-T10-03's `[ASSUMPTION]`) is planted here and shipped nowhere; its mutation is the
falsifier: apply `want` in MATTER instead and `demanded` and the draw disagree.
"""

from __future__ import annotations

from fractions import Fraction

import pytest

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import Step, WriteClass
from ..data.requires import SHORTFALL_PREDICATE
from ..data.rosters import SEASONS_OF_YEAR, SEASON_TERMS
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..state.carriers import Person, Rung, Tenure
from ..state.world import World

WEIGHTS = DEFAULT_FIXTURES.get("subsistence_weight")
TOWN, COHORT = "set_town", "p_town_folk"
WINTER = len(SEASONS_OF_YEAR) - 1
# CP-T10-03's swept arm, `[ASSUMPTION; medium; Jordan to correct]`: winter only.
SWEPT = {s: {"yield": 1.0, "want": 1.0, "illness": 1.0, "hardship": 0} for s in SEASONS_OF_YEAR}
SWEPT[SEASONS_OF_YEAR[WINTER]] = {"yield": 0.25, "want": 1.5, "illness": 2.0, "hardship": 0}


def _town(weight: int = 2, stores=None, tick: int = 0, fixtures=DEFAULT_FIXTURES) -> World:
    w = World(0, fixtures)
    for rid, kind, st in (("r_realm", "realm", None), ("terr_town", "territory", None),
                          (TOWN, "settlement", dict(stores if stores is not None else {"grain": 20, "salt": 20}))):
        w.rungs[rid] = Rung(rid, kind, stores=st)
    w.add_tenure(Tenure("t_in_0", "terr_town", "r_realm", "contain", 0))
    w.add_tenure(Tenure("t_in_1", TOWN, "terr_town", "contain", 0))
    w.persons[COHORT] = Person(COHORT, "the town folk", weight=weight)
    w.rungs[COHORT] = Rung(COHORT, "person")
    w.add_tenure(Tenure("t_folk_in", COHORT, TOWN, "contain", 0))
    w.add_tenure(Tenure("t_folk_home", COHORT, TOWN, world_q.RESIDE_KIND, 0))
    w.tick = tick
    return w


def _weights(w) -> dict:
    return dict(world_q.larder_input(w).weights)


def test_winter_want_scales_the_projection(monkeypatch):
    """The card's falsifier: a weight-2 cohort wants grain 6 at a winter tick and 4 at tick 0 (swept arm planted)."""
    monkeypatch.setattr(world_q, "SEASON_TERMS", SWEPT)
    assert world_q.demanded(_town(tick=0), TOWN)["grain"] == 2 * WEIGHTS["grain"] == 4
    assert world_q.demanded(_town(tick=WINTER), TOWN)["grain"] == 6, "the winter want did not reach the Query"


def test_salt_weight_one_under_one_and_a_half_is_two(monkeypatch):
    """E5 C29: the scaled weight is a whole number rounded half up, never 1.5 (a salt weight of 1 under 1.5 is 2)."""
    monkeypatch.setattr(world_q, "SEASON_TERMS", SWEPT)
    assert WEIGHTS["salt"] == 1
    scaled = _weights(_town(tick=WINTER))
    assert scaled["salt"] == 2 and all(isinstance(v, int) for v in scaled.values()), scaled
    assert world_q.demanded(_town(tick=WINTER), TOWN)["salt"] == 2 * 2, "a cohort of two wants 4 salt, not the unrounded 3"


def test_demanded_and_matter_agree_at_a_winter_tick(monkeypatch):
    """`demanded(w, S)` and MATTER's delivered + short agree at a winter tick: the larder short of grain by 2 is drained by exactly what
    `delivered` said, and the shortfall MATTER records is `demanded - delivered`."""
    monkeypatch.setattr(world_q, "SEASON_TERMS", SWEPT)
    w = _town(stores={"grain": 4, "salt": 10}, tick=WINTER)
    want, got = world_q.demanded(w, TOWN), world_q.delivered(w, TOWN)
    assert want == {"grain": 6, "salt": 4} and got == {"grain": 4, "salt": 4}, (want, got)
    before = dict(w.rungs[TOWN].stores)
    w.step = Step.MATTER
    events = SeasonDriver(w).matter(mint_token(w, WriteClass.MATTER), [])
    spent = {k: before[k] - w.rungs[TOWN].stores.get(k, 0) for k in before}
    assert spent == got, "MATTER drew other than the Query said"
    short = [(o.subject, o.value) for e in events for o in e.observed
             if str(o.predicate).partition(":")[0] == SHORTFALL_PREDICATE]
    assert short and sum(1 for _ in short) >= 1, "MATTER recorded no shortfall at the tick the Query reads short"
    assert {k: want[k] - got[k] for k in want if want[k] > got[k]} == {"grain": 2}


def test_hunger_cover_falls_in_winter_on_unchanged_stores(monkeypatch):
    """CP-T10-03's falsifier, read through REM-50: the same stores cover fewer seasons of want at a winter tick (cover = stores / want)."""
    monkeypatch.setattr(world_q, "SEASON_TERMS", SWEPT)
    stores = {"grain": 12, "salt": 8}
    spring = world_q.hunger(_town(stores=stores, tick=0), TOWN)[1]
    winter = world_q.hunger(_town(stores=stores, tick=WINTER), TOWN)[1]
    assert isinstance(spring, Fraction) and spring > winter > 0, (spring, winter)
    assert winter == Fraction(sum(stores.values()), 6 + 4)


def test_yield_term_scales_the_drawn_factor_only_when_the_draw_is_on(monkeypatch):
    """`yield` multiplies `season_factor_of`'s drawn return; an empty `season_factor_draw` returns the bare `season_factor` whatever the season says."""
    monkeypatch.setattr(world_q, "SEASON_TERMS", SWEPT)
    on = DEFAULT_FIXTURES.sweep("season_factor_draw", ((1.0,),) * len(SEASONS_OF_YEAR))
    assert world_q.season_factor_of(_town(tick=0, fixtures=on)) == 1.0
    assert world_q.season_factor_of(_town(tick=WINTER, fixtures=on)) == 0.25
    assert world_q.season_factor_of(_town(tick=WINTER)) == DEFAULT_FIXTURES.get("season_factor")


def test_shipped_terms_are_the_identity():
    """At the shipped row every multiplier is 1.0 and `hardship` 0, so the projection is the bare `subsistence_weight` at every tick of the year."""
    assert all(t["yield"] == t["want"] == t["illness"] == 1.0 and t["hardship"] == 0 for t in SEASON_TERMS.values())
    for tick in range(len(SEASONS_OF_YEAR)):
        assert _weights(_town(tick=tick)) == dict(WEIGHTS), tick
