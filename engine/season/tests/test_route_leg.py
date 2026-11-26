"""B12b.02 (CP-T10-01) -- `world_q.route` / `leg_points`: a journey's path and price over the settlement graph.

WHAT IS ASKED: on the built realm, what a journey between two settlements costs (the card's two worked prices), that a journey out of the
realm is still a blocked travel, and that the ground of a settlement is read through the one owner of terrain at a point
(`mass_battle.terrain_type_at`): a settlement planted in a pass nested in the mountain costs the pass's 2.0, one planted in the mountain's
interior may not be entered. Nothing in the loop calls `route` while `route_pricing` is `off`, so these tests are the only reader.
"""

from __future__ import annotations

import copy

import pytest

from ..boot.realm import build_realm
from ..data import geography as geo_data
from ..data.rosters import settlement_rung_id
from ..loop.effects_migration import _eff_move
from ..queries import world_q
from ..state.carriers import Act
from ..state.gate import NO_CHANGE

S = settlement_rung_id


@pytest.fixture(scope="module")
def realm():
    return build_realm(0)


@pytest.fixture
def planted(monkeypatch):
    """`plant(sid, point)`: the geography the route reads, with settlement `sid`'s coords moved to `point` (a deep copy; the shared mapping is
    never written, and `monkeypatch` puts the cache back)."""
    geo = copy.deepcopy(geo_data.geography())
    monkeypatch.setattr(geo_data, "_CACHE", geo)

    def plant(sid, point):
        geo["settlements"][sid]["coords"] = list(point)
    return plant


def test_adjacent_pair_prices_one_point(realm):
    path, cost = world_q.route(realm, S("S-001"), S("S-002"))
    assert path == (S("S-001"), S("S-002")) and cost == 1.0
    assert world_q.leg_points(realm, S("S-001"), S("S-002")) == 1


def test_aschenbach_prices_four_points(realm):
    """The card's probe: S-001 -> S-013 is five edges at cost 7.0, `ceil(7.0 / 2.0)` = 4 points."""
    path, cost = world_q.route(realm, S("S-001"), S("S-013"))
    assert len(path) == 6 and path[0] == S("S-001") and path[-1] == S("S-013") and cost == 7.0
    assert world_q.leg_points(realm, S("S-001"), S("S-013")) == 4


def test_a_journey_inside_one_settlement_or_above_settlement_kind_costs_the_floor(realm):
    assert world_q.route(realm, S("S-001"), S("S-001")) == ((), 0.0)
    assert world_q.route(realm, "terr_T1", S("S-002")) == ((), 0.0)
    assert world_q.leg_points(realm, S("S-001"), S("S-001")) == 1


def test_journey_into_t16_is_still_travel_blocked(realm):
    """Schoenland's root is a territory, a rung only an arriving army is placed at (`rosters.yaml: arrival_only_kinds`): `_eff_move` declines
    the journey, which the fold publishes as `travel.blocked`. Pricing a route does not lift it (`route` is read by no effect)."""
    mover = next(p for p in sorted(realm.persons) if world_q.home_of(realm).get(p) is not None)
    act = Act("a_t16", mover, "move", payload={"to": "terr_T16"})
    assert realm.rungs["terr_T16"].kind == "territory"
    assert _eff_move(realm, act) is NO_CHANGE


def test_nested_mountain_pass_costs_two_not_999(realm, planted):
    """A settlement inside a `mountain_pass` polygon nested in a `mountain` reads the smaller polygon (`terrain_type_at`'s smallest-area
    match), so entering it costs the matrix's 2.0 and the journey is not blocked."""
    planted("S-002", (1400, 150))
    path, cost = world_q.route(realm, S("S-001"), S("S-002"))
    assert path == (S("S-001"), S("S-002")) and cost == 2.0


def test_route_through_mountain_interior_is_none(realm, planted):
    """Inside the mountain and outside both passes the ground costs the matrix's `mountain` entry: the settlement may not be entered, so
    the route is `None` (and `leg_points` with it)."""
    planted("S-002", (800, 150))
    assert world_q.route(realm, S("S-001"), S("S-002")) is None
    assert world_q.leg_points(realm, S("S-001"), S("S-002")) is None
