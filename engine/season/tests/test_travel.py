"""B12b.08 (`16_PESSIMIST_WR_A_the_road_is_drawn` edits 1-3, CP-T10-02) -- the road's draw: `settlements.exposure` on a typed `RoadInput`, and the arm that ships off.

WHAT IS ASKED: that a journey's arrival is a draw that the state of the road sets (not every traveller arrives alike, a road of four borders fails more than a road of
one, two seeds read two different tallies), and that with `road_hazard` off the season is the base season (the three calibration rows read by nothing). The records are
built here as `world_q.road_input` (B12b.09) will: a declared obstacle from the road's fixtures, the key of the keyed draw `(world_seed, tick, pid, "road:<leg index>")`.
The two tests that need the travel pass itself (`test_hurt_traveller_is_tended_in_some_seed`, `test_one_leg_ends_per_barrier`) are written with B12b.11 and B12b.12,
which build what they read.
"""

from __future__ import annotations

from collections import Counter

from engine.dice_engine.dice_engine import Degree
from engine.substrate import composition

from ..boot.realm import build_realm
from ..data.fixtures import DEFAULT_FIXTURES
from ..harness.populated import run
from ..queries.inputs import RoadInput
from ..state.ids import draw_factory

JOURNEYS = 40     # the source's forty
POOL = 6          # one person kind (PROXY): a traveller's pool, a test constant until B12b.09 reads the person's `move` faculty


def _road(seed: int, borders: int, n: int = JOURNEYS) -> Counter:
    """The tally of degrees over `n` journeys of `borders` borders, at seed `seed`, through the registered entry."""
    exposure = composition.require("settlements.exposure")      # the registered row, as the host reaches it
    keyed = draw_factory(seed, lambda: 0)
    ob = DEFAULT_FIXTURES.get("difficulty_ob")[DEFAULT_FIXTURES.get("road_base")] + borders * DEFAULT_FIXTURES.get("road_step_ob")
    rows = exposure(RoadInput(tuple((f"p{i}", POOL, ob, keyed(f"p{i}", "road:0").key) for i in range(n)))).rows
    assert len(rows) >= JOURNEYS, "the loop read fewer than forty journeys"
    return Counter(degree for _pid, degree in rows)


def test_road_degrees_not_all_equal_over_forty_journeys():
    """Forty journeys of three borders by one person kind: the degrees are not all equal, and the tally differs between two seeds."""
    zero, one = _road(0, 3), _road(1, 3)
    assert len(zero) > 1 and len(one) > 1, (zero, one)
    assert zero != one, (zero, one)
    assert set(zero) | set(one) <= set(Degree)


def test_four_borders_fail_more_than_one():
    """State sets the odds: over the same forty at two seeds, a journey of four borders ends in Failure more often than a journey of one."""
    for seed in (0, 1):
        assert _road(seed, 4)[Degree.FAILURE] > _road(seed, 1)[Degree.FAILURE], seed


def test_road_hazard_off_hash_equal():
    """The control: `road_hazard` ships `off`, and the three rows that size the draw are read by nothing there, so the realm at seed 0 after one season
    reads the same content hash with them swept to other values as with them shipped."""
    base, swept = build_realm(0), build_realm(0)
    assert base.fixtures.get("road_hazard") == "off"
    for name, value in (("road_base", "hard"), ("road_step_ob", 2), ("road_step", 150)):
        swept.fixtures = swept.fixtures.sweep(name, value)
    run(1, 0, w=base)
    run(1, 0, w=swept)
    assert base.content_hash() == swept.content_hash()
