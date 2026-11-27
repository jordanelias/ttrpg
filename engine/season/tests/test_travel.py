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
from ..data import geography as geo_data
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.rosters import SEASONS_OF_YEAR, settlement_rung_id
from ..data.verbs import EVENT_KINDS
from ..harness.populated import run
from ..harness.probes import about
from ..queries import world_q
from ..queries.inputs import RoadInput
from ..seam.wrappers.pool import faculty
from ..state.carriers import Event, Person, Rung, Tenure
from ..state.ids import ROOT, draw_factory
from ..state.world import World

JOURNEYS = 40     # the source's forty
POOL = faculty(World(0), Person("p_road", "a traveller"), "move")      # one person kind (PROXY): his pool as `road_input` reads it, the `move` faculty


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


# -- B12b.09: who is on the road, and their odds -- a hand-built road of three territories, S-001 to S-013 (the card's four-point journey) --------------------------

START, STOP = settlement_rung_id("S-001"), settlement_rung_id("S-013")


def _road_world() -> World:
    """The six settlements the journey passes, two to a territory under one realm (the settlements are the geography's own ids; the territories are planted),
    with three people: `p_far` who set out from S-001 at tick 2 and stands in S-013, `p_near` who moved inside the first territory, and `p_home` who holds no
    leg. `w.tick` is 3. The weather draw is at its control."""
    w = World(0, DEFAULT_FIXTURES.sweep("road_hazard", "on"), event_kinds=EVENT_KINDS)
    path = [settlement_rung_id(s) for s in geo_data.route_over("S-001", "S-013")[0]]
    assert len(path) == 6 and path[0] == START and path[-1] == STOP
    w.rungs["r_realm"] = Rung("r_realm", "realm", stores=None)
    n = 0
    for i, territory in enumerate(("terr_a", "terr_b", "terr_c")):
        w.rungs[territory] = Rung(territory, "territory", stores=None)
        w.add_tenure(Tenure(f"t_in_{n}", territory, "r_realm", "contain", 0))
        for rid in path[2 * i: 2 * i + 2]:
            n += 1
            w.rungs[rid] = Rung(rid, "settlement", stores={})
            w.add_tenure(Tenure(f"t_in_{n}", rid, territory, "contain", 0))
        n += 1
    for pid in ("p_far", "p_near", "p_home", "p_soldier"):
        w.persons[pid] = Person(pid, pid)
    w.tick = 3
    w.add_tenure(Tenure("t_far0", "p_far", START, "contain", 0, until=2))
    w.add_tenure(Tenure("t_far1", "p_far", STOP, "contain", 2))
    w.add_tenure(Tenure("t_near0", "p_near", path[0], "contain", 0, until=2))
    w.add_tenure(Tenure("t_near1", "p_near", path[1], "contain", 2))
    w.add_tenure(Tenure("t_home", "p_home", STOP, "contain", 0))
    w.add_tenure(Tenure("t_soldier", "p_soldier", path[2], "contain", 0))
    w.persons["p_far"].travel_leg = [STOP]
    w.persons["p_near"].travel_leg = [path[1]]
    return w


def test_road_input_obstacle_counts_borders_bad_weather_and_war(monkeypatch):
    """Only a traveller whose last journey crossed a border is in the input; his obstacle is `road_base`'s level plus `road_step_ob` for the journey's four points,
    for each crossed territory whose season landed Failure and for each a field was fought in this tick or the last, and his pool is his `move` faculty."""
    fx = DEFAULT_FIXTURES
    base, step = fx.get("difficulty_ob")[fx.get("road_base")], fx.get("road_step_ob")
    w = _road_world()
    (pid, pool, obstacle, key), = world_q.road_input(w).travellers          # p_near crossed no territory, p_home holds no leg: only p_far
    assert pid == "p_far" and pool == faculty(w, w.persons["p_far"], "move")
    assert obstacle == base + 4 * step, "the control: four points of distance, no weather draw, no war"
    assert key == draw_factory(0, lambda: 3)("p_far", "road:0").key
    w.log.append(Event("ev_old", "field.lost", [about(w, "p_far")], [ROOT], 0))          # a field three ticks old, in terr_c where the journey ended
    assert world_q.road_input(w).travellers[0][2] == base + 4 * step, "a field three ticks old is not on the road"
    w.log.append(Event("ev_war", "field.won", [about(w, "p_soldier")], [ROOT], 2))       # a field fought last tick in terr_b, a territory the journey entered
    assert world_q.road_input(w).travellers[0][2] == base + 5 * step
    # the weather arm on, every season so hard that the draw lands Failure in each territory (pool 6 against an obstacle of 100): the two territories entered
    w.fixtures = w.fixtures.sweep("season_factor_draw", ((1.0,),) * len(SEASONS_OF_YEAR))
    monkeypatch.setattr(world_q, "SEASON_TERMS", {s: {**t, "hardship": 100} for s, t in world_q.SEASON_TERMS.items()})
    assert world_q.road_input(w).travellers[0][2] == base + (4 + 2 + 1) * step


# -- B12b.10: what a journey appends to `travel_leg` -----------------------------------------------------------------------------------------------

def test_legs_appended_equal_leg_price():
    """`route_pricing` `on`: a journey appends as many entries as the points of its price (`geography.leg_price`, equal to the world-side `leg_points` from a
    settlement), and one entry where the price is one; `off`, `[dest]` whatever the distance. Read over every settlement from S-001."""
    import copy
    from ..loop.effects_migration import _relocate
    from ..state.carriers import Act
    here, checked, realm = settlement_rung_id("S-001"), 0, build_realm(0)
    for on in (False, True):
        for sid in sorted(geo_data.geography()["settlements"]):
            dest = settlement_rung_id(sid)
            if dest == here:
                continue
            w = copy.deepcopy(realm)
            if on:
                w.fixtures = w.fixtures.sweep("route_pricing", "on")
            pid = next(i for i in sorted(w.persons) if world_q.home_of(w)[i] == here)
            _relocate(w, Act("a_t", pid, "move", payload={"to": dest}), dest)
            price = geo_data.leg_price(here, dest, geo_data.geography(), leg_unit=w.fixtures.get("leg_unit"))
            assert w.persons[pid].travel_leg == [dest] * (price if on else 1), (on, sid)
            checked += 1
    assert checked >= 60
