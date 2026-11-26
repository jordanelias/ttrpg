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


# --- B12b.04: the leg's price reaches the chooser -----------------------------------------------------------------------------------------------

def _settler(realm):
    """A person who stands in a settlement rung (a hearth-dweller prices every journey at the floor: `geography.leg_price`'s docstring) and that rung."""
    from ..decision.options import containing_rung_of
    for pid in sorted(realm.persons):
        where = containing_rung_of(realm.persons[pid])
        if where in geo_data.settlement_by_rung(geo_data.geography()):
            return realm.persons[pid], where
    raise AssertionError("no person of the realm stands in a settlement rung")


def _journey_scenes(realm, fx, dest, budget=10):
    """What the shipped packer returns for `move` to `dest` from a settlement-dweller, through `release` with the loaded geography handed beside `fx`."""
    from ..decision.choose import release
    from ..state.carriers import Candidate, Question
    p, _ = _settler(realm)
    return release(p, [Candidate("move", dest)], budget, fx, lambda a, b, c: f"{a}:{b}:{c}", Question("q:b12b04", "need", (dest,)), None, geo_data.geography())


def test_leg_price_is_pure_and_equals_route_points(realm):
    """`leg_price` is the world-side `leg_points` without a World: equal over every pair it can resolve (the card's 4 among them), the same twice, and
    it writes nothing into the geography it is handed."""
    geo = geo_data.geography()
    before = copy.deepcopy(geo)
    assert geo_data.leg_price(S("S-001"), S("S-013"), geo, leg_unit=2.0) == world_q.leg_points(realm, S("S-001"), S("S-013")) == 4
    checked = 0
    for b in sorted(geo["settlements"]):
        want = world_q.leg_points(realm, S("S-001"), S(b))
        got = geo_data.leg_price(S("S-001"), S(b), geo, leg_unit=2.0)
        assert got == (1 if want is None else want), b          # a blocked journey reads the floor: the fold, not the price, refuses it
        assert got == geo_data.leg_price(S("S-001"), S(b), geo, leg_unit=2.0)
        checked += 1
    assert checked >= 30 and geo == before


def test_off_arm_charges_one_point(realm):
    """`route_pricing` `off` (shipped): a journey to the far end of the realm is one scene point, as it was, and carries no `leg`."""
    from ..state.carriers import leg_of
    _, here = _settler(realm)
    far = max(geo_data.settlement_by_rung(geo_data.geography()), key=lambda r: world_q.leg_points(realm, here, r) or 0)
    assert realm.fixtures.get("route_pricing") == "off" and world_q.leg_points(realm, here, far) > 1
    (scene,) = _journey_scenes(realm, realm.fixtures, far)
    assert scene.cost(realm.fixtures.get("extended_scene_cost")) == 1 and leg_of(scene.acts[0]) == 1


def test_on_arm_prices_a_far_move_above_a_near_one(realm):
    """`on`: the journey costs its leg's points from the scene budget (the world-side `leg_points` is the oracle); a person who cannot afford it leaves
    it undone rather than being handed a scene over his remainder."""
    on, geo = realm.fixtures.sweep("route_pricing", "on"), geo_data.geography()
    _, here = _settler(realm)
    ext = on.get("extended_scene_cost")
    by_points = {r: world_q.leg_points(realm, here, r) for r in sorted(geo_data.settlement_by_rung(geo)) if r != here}
    near = next(r for r, n in by_points.items() if n == 1)
    far = max(by_points, key=lambda r: by_points[r] or 0)
    (near_scene,), (far_scene,) = _journey_scenes(realm, on, near), _journey_scenes(realm, on, far)
    assert near_scene.cost(ext) == 1
    assert far_scene.cost(ext) == by_points[far] > near_scene.cost(ext)
    assert _journey_scenes(realm, on, far, budget=by_points[far] - 1) == []
