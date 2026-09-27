"""A1, ED-MB-0067 Part A (proposals/2026-09-25-squad-engagement-synthesis.md) — waypoint routes.

`Subunit.route`/`_route_idx` (hierarchy/units.py) + `_resolve_route_goal` (composed on
`_resolve_maneuver_goal`, checked ahead of its enemy-cells gate so a route is followed with no
enemy in sight) + `check_orders`' path-length clamp (core/contact.py, `0.5*speed*max-ticks`,
ROUTE_BUDGET_TICKS/ROUTE_WAYPOINT_EPS in config.py). Also pins the two integration fixes this needed:
`_node_advance`'s target_centroid gate (hierarchy/units.py) and `run_battle`'s moving_a/moving_b
atom selection (orchestration.py), both widened with an `or` clause for an unfinished route.

Default route=() on every existing Subunit -> every assertion here is about a NEWLY-exercised path;
byte-exactness for the untouched default is covered separately by bat.py --check (no BATTERY row
sets a route).

Waypoints below are built OFFSET FROM THE SUB-UNIT'S OWN LIVE `_node_anchor` (read right after
construction), never guessed from `starting_position` -- a first version of this file assumed the
anchor coincided with the raw spawn coordinate, which is FALSE (the anchor is the centroid of the
whole footprint, offset by the shape's own layout: verified here as (+1 row, +2 col) for a Line
tier-2 body, not (0, 0)) -- a review caught two tests whose stated distances were wrong (the
assertions still happened to pass by margin, but the comments were fabricated numbers). Building
from the live anchor makes every distance in this file exact by construction, not approximate.
"""
import math

import pytest

import systems.mass_battle.sim.hierarchy.units as _hu
import systems.mass_battle.sim.orchestration as _orch
from systems.mass_battle.sim.config import (SIDE_A_START_ROW, SIDE_B_START_ROW, TICKS_PER_PHASE,
                                             MB_CAVALRY_SPEED_MULT, ROUTE_BUDGET_TICKS)
from systems.mass_battle.sim.core.contact import check_orders
from systems.mass_battle.sim.hierarchy.units import Order, Subunit, Unit
from systems.mass_battle.sim.orchestration import run_battle
from systems.mass_battle.sim.resolution import start_trace, get_trace


def _bare_subunit(faction='A', col=25, troop_type='infantry', target_condition=None):
    sr = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    return Subunit(shape='Line', troop_type=troop_type, tier=2,
                   starting_position=(sr, col), advance_dir=(-1 if faction == 'A' else 1),
                   stance='balanced', unit_type='melee', target_condition=target_condition)


def _route_unit_from_offsets(col_offsets, faction='A', target_condition=None, col=25):
    """Build a disc-5 (disc_mult=1.0) single-subunit Unit whose ONE 'immediate' order sets a route
    of waypoints along the sub-unit's own anchor ROW, each `col_offsets[i]` columns to the side of
    its LIVE anchor column (not the raw starting_position column -- see module docstring). Returns
    (unit, subunit, anchor, route) so a test can assert against the exact, already-known distances
    (each waypoint is exactly `abs(col_offsets[i] - col_offsets[i-1])` from the previous one, and
    `abs(col_offsets[0])` from the anchor -- Manhattan == Euclidean here since every point shares
    the anchor's row)."""
    probe = _bare_subunit(faction=faction, col=col)
    ar, ac = probe._node_anchor
    route = tuple((ar, ac - off) for off in col_offsets)
    su = _bare_subunit(faction=faction, col=col, target_condition=target_condition)
    su.orders = (Order('immediate', {'route': route}),)
    u = Unit(name=f'{faction}_route', faction=faction, power=4, command=4,
             discipline=5, discipline_start=5, morale=6, morale_start=6, subunits=[su])
    assert u.subunits[0]._node_anchor == (ar, ac), "control: two identically-constructed Subunits must anchor identically"
    return u, su, (ar, ac), route


def test_route_is_an_order_safe_field():
    """Regression pin: Order may set `route` (and `_route_idx`) without raising -- confirms both
    are in _ORDER_SAFE_FIELDS."""
    Order(trigger='immediate', behavior={'route': ((1.0, 2.0),), '_route_idx': 0})


def test_check_orders_fires_the_immediate_route_order():
    # offsets 2, 4 from the anchor -> waypoint-to-waypoint distance 2, cumulative 4 -- comfortably
    # inside the 9.0 budget verified below.
    u, su, anchor, route = _route_unit_from_offsets((2, 4))
    assert su.route == () and su._order_idx == 0
    check_orders(u, 1, [])   # 'immediate' fires regardless of enemy_cells (here: empty)
    assert su._order_idx == 1, "the immediate order must fire on the first check"
    assert su.route == route, \
        "both waypoints are within the path budget (cumulative distance 4 <= 9.0) -- neither should be clamped"


def test_route_speed_budget_matches_the_ruled_formula():
    """Value-level control on _route_speed_budget itself: 0.5*speed*max-ticks with speed=1 (Line,
    geometry.cell_speed) and max-ticks=ROUTE_BUDGET_TICKS=3*TICKS_PER_PHASE=18 -- 9.0, independent
    of the clamping test below (which only checks the clamp's EFFECT, not this number directly)."""
    su = _bare_subunit()
    assert TICKS_PER_PHASE == 6, "budget derivation assumes the shipped 3-phases-of-6 engagement; re-check ROUTE_BUDGET_TICKS's basis if this ever changes"
    assert su._route_speed_budget() == pytest.approx(9.0)


def test_path_budget_clamps_a_too_long_route():
    """B is 5 from the anchor (within the 9.0 budget); B->C is a further 10 (cumulative 15, past
    the budget) -- C must be dropped, and the route ends one waypoint short, not zero (a partial
    clamp, not an all-or-nothing rejection)."""
    u, su, anchor, (B, C) = _route_unit_from_offsets((5, 15))
    check_orders(u, 1, [])
    assert su.route == (B,), f"expected only B to survive the 9.0 budget, got {su.route}"


def test_route_waypoint_is_passed_before_the_next_is_chased():
    """'Done when a sub-unit ordered through waypoint B passes B before reaching C' -- drive
    advance_cells directly (bypassing run_battle) with target_centroid=None and enemy_cells=None,
    the exact case _node_advance's widened gate exists for (fact 1a of the brief)."""
    u, su, anchor, (B, C) = _route_unit_from_offsets((2, 4))   # both within the 9.0 budget
    check_orders(u, 1, [])
    assert su.route == (B, C), "both waypoints are within the 9.0 budget -- sanity check before the march"

    # Record the first tick the anchor comes within ROUTE_WAYPOINT_EPS of B and of C independently
    # of _route_idx's own bookkeeping (which increments at the START of the tick AFTER arrival, so
    # checking it directly against the anchor position at the same instant is off-by-one-tick and
    # was the first, wrong version of this test) -- the anchor-distance record is what "passes B
    # before reaching C" actually means.
    tick_at_b = tick_at_c = None
    for tick in range(1, 21):
        su.advance_cells(su.eff_discipline, None, enemy_cells=None)
        ar, ac = su._node_anchor
        if tick_at_b is None and math.hypot(ar - B[0], ac - B[1]) <= 1e-6:
            tick_at_b = tick
        if tick_at_c is None and math.hypot(ar - C[0], ac - C[1]) <= 1e-6:
            tick_at_c = tick
        if tick_at_c is not None:
            break
    assert tick_at_b is not None, "the sub-unit never reached B at all"
    assert tick_at_c is not None, "the sub-unit never reached C at all"
    assert tick_at_b < tick_at_c, f"B must be passed strictly before C is reached (tick_at_b={tick_at_b}, tick_at_c={tick_at_c})"
    # _route_idx's own increment happens at the START of the tick AFTER the anchor arrives (it is
    # read fresh from the PREVIOUS tick's end position -- see _resolve_route_goal), so one more
    # call is needed before the cursor itself reflects "C reached, route exhausted".
    su.advance_cells(su.eff_discipline, None, enemy_cells=None)
    assert su._route_idx == 2, f"route must be fully consumed once C is reached, got _route_idx={su._route_idx}"


def test_route_moves_a_subunit_with_no_enemy_in_sight():
    """Integration control for fact 2 (orchestration.py's moving_a/moving_b + cached_centroids.get
    fix): a full run_battle with the route-holder's target_atom held None throughout (target_
    condition='in_range:1', enemy starts ~19 rows away) -- 'no enemy in sight' in the brief's own
    words. Without the orchestration.py fix this atom is excluded from moving_a entirely and never
    calls advance_cells at all."""
    ua, sa, spawn, _route = _route_unit_from_offsets((2, 4), faction='A', target_condition='in_range:1')
    ub, _sb, _spawn_b, _route_b = _route_unit_from_offsets((), faction='B')   # plain far-side unit; no route of its own
    run_battle(ua, ub, max_turns=6)
    assert sa.target_atom is None, "control: the enemy must still be out of the in_range:1 gate after 6 ticks"
    assert sa._route_idx >= 1 or sa._node_anchor != spawn, \
        "the route-holder never moved: run_battle's moving_a/moving_b must have excluded it"


# ─── Adversarial-review round 2 fixes ────────────────────────────────────────

def test_route_order_does_not_crash_on_the_legacy_lattice_arm():
    """Regression: a route order at MB_NODE_COHESION=0 (the legacy lattice arm -- documented
    elsewhere in this codebase, bat.py's own comment, as "not a way the game can be played", kept
    only as the byte-exact grid regression oracle) used to raise
    `AttributeError: 'Subunit' object has no attribute '_node_anchor'` the instant check_orders
    tried to clamp the route (_clamp_route_to_budget dereferenced _node_anchor unconditionally).
    Must now be an explicit, harmless no-op: check_orders completes, the route is left unclamped
    (dead data -- _resolve_route_goal is unreachable on this arm via the normal call chain), and
    a direct advance_cells call on the legacy path with a route set also does not crash."""
    saved = _hu.MB_NODE_COHESION
    _hu.MB_NODE_COHESION = False
    try:
        su = _bare_subunit()
        su.orders = (Order('immediate', {'route': ((30, 20),)}),)
        assert not hasattr(su, '_node_anchor'), "control: this Subunit must genuinely be on the legacy (non-node) arm"
        u = Unit(name='A', faction='A', power=4, command=4, discipline=5, discipline_start=5,
                 morale=6, morale_start=6, subunits=[su])
        check_orders(u, 1, [])   # must not raise
        assert su.route == ((30, 20),), "unclamped (no node position to measure a budget from), but present -- not silently discarded either"
        su.advance_cells(su.eff_discipline, (30, 20), enemy_cells=None)   # must not raise
    finally:
        _hu.MB_NODE_COHESION = saved


def test_cavalry_route_budget_is_larger_than_infantrys():
    """A cavalry sub-unit's budget must include MB_CAVALRY_SPEED_MULT (3.0x by default), not the
    shape-table floor every troop type shares -- otherwise a cavalry route is bounded as if it
    marched at infantry pace, too short to reach a deployed enemy line at all."""
    su_inf = _bare_subunit(troop_type='infantry')
    su_cav = _bare_subunit(troop_type='cavalry')
    assert su_inf._route_speed_budget() == pytest.approx(9.0)
    assert su_cav._route_speed_budget() == pytest.approx(9.0 * MB_CAVALRY_SPEED_MULT)


def test_dropped_waypoint_is_traced_not_silent():
    """A waypoint beyond the budget must leave an observable record (this engine's existing
    observe-only trace seam, resolution.trace_event -- zero cost when tracing is off), not just a
    silently shorter route."""
    u, su, anchor, (B, C) = _route_unit_from_offsets((5, 15))   # B within budget; cumulative to C is not
    start_trace(True)
    try:
        check_orders(u, 1, [])
        events = [e for e in get_trace() if e.get('cat') == 'route_clamped']
    finally:
        start_trace(False)
    assert su.route == (B,)
    assert len(events) == 1, f"expected exactly one route_clamped trace event, got {events}"
    assert events[0]['dropped'] == 1 and events[0]['kept'] == 1


def test_dropped_waypoint_is_not_traced_when_nothing_is_dropped():
    """Control: a route that fits entirely within budget must NOT emit a route_clamped event --
    otherwise the trace would be noise, not a diagnostic."""
    u, su, anchor, route = _route_unit_from_offsets((2, 4))
    start_trace(True)
    try:
        check_orders(u, 1, [])
        events = [e for e in get_trace() if e.get('cat') == 'route_clamped']
    finally:
        start_trace(False)
    assert events == []


def test_reissuing_a_route_resets_the_cursor():
    """A caller that sets a NEW `route` without ALSO explicitly resetting `_route_idx` must not
    silently inherit the prior route's cursor position (e.g. resuming a brand-new route already
    'finished', or partway through, purely because of a stale index left over from the last one)."""
    u, su, anchor, (B, C) = _route_unit_from_offsets((2, 4))
    check_orders(u, 1, [])
    assert su.route == (B, C) and su._order_idx == 1
    su._route_idx = 2   # simulate having fully consumed this route already
    new_wp = (anchor[0], anchor[1] - 7)   # distance 7 from the anchor -- still within the 9.0 budget
    # A second order re-routes the sub-unit. The queue already advanced past index 0, so append a
    # tick:1 order (fires immediately at t=1, same as 'immediate' would here) as the SECOND order.
    su.orders = su.orders + (Order('tick:1', {'route': (new_wp,)}),)
    check_orders(u, 1, [])
    assert su._order_idx == 2, "the second (re-routing) order must also have fired"
    assert su.route == (new_wp,)
    assert su._route_idx == 0, "a fresh route must reset the cursor, not inherit the previous route's index"


def test_emergent_yield_abandons_a_route_rather_than_resuming_it_later():
    """[REVERSED at adversarial-pass round 2 -- this is the OPPOSITE assertion from round 1's
    now-deleted 'suspend' test, per Jordan's own correction of round 1's ruling.] `yield_active`
    can flip back to False because eff_discipline DROPS below D_YIELD (core/state.py's
    discipline-degradation check) -- the body getting WORSE, not recovering -- so 'resume once
    yield ends' resumed the route at exactly the moment the body was MORE disordered than when
    yield began. _resolve_route_goal must instead CLEAR the route (self.route=(), _route_idx=0)
    the moment yield_active is detected, and it must stay cleared even after yield_active later
    goes False."""
    u, su, anchor, (B,) = _route_unit_from_offsets((5,))   # within the 9.0 budget
    check_orders(u, 1, [])
    assert su.route == (B,)
    su.yielding = True
    assert su.yield_active, "control: yield_active must actually be True for this test to mean anything"
    start_trace(True)
    try:
        assert su._resolve_route_goal() is None, "the route must not be offered as a goal while yield_active"
        events = [e for e in get_trace() if e.get('cat') == 'route_abandoned']
    finally:
        start_trace(False)
    assert su.route == () and su._route_idx == 0, "the route must be CLEARED (abandoned), not merely suspended"
    assert len(events) == 1 and events[0]['reason'] == 'yield', f"expected one route_abandoned/yield event, got {events}"
    su.yielding = False
    assert not su.yield_active
    assert su._resolve_route_goal() is None, \
        "an abandoned route must NOT resume once yield_active ends -- it is gone, not paused"
    assert su.route == (), "route data must stay cleared"


def test_retreat_stance_abandons_a_route_rather_than_resuming_it_later():
    """[REVERSED at adversarial-pass round 2] stance=='retreat' has no engine writer anywhere in
    this package (grep-confirmed) -- it is only ever set by an explicit order, i.e. already a
    commanded override, not a transient condition worth resuming through later. Must abandon the
    route (clear it) exactly like the yield case, not merely suspend it."""
    u, su, anchor, (B,) = _route_unit_from_offsets((5,))
    check_orders(u, 1, [])
    assert su.route == (B,)
    su.stance = 'retreat'
    start_trace(True)
    try:
        assert su._resolve_route_goal() is None, "the route must not be offered as a goal while stance=='retreat'"
        events = [e for e in get_trace() if e.get('cat') == 'route_abandoned']
    finally:
        start_trace(False)
    assert su.route == () and su._route_idx == 0, "route data must be CLEARED (abandoned), not merely suspended"
    assert len(events) == 1 and events[0]['reason'] == 'retreat'
    su.stance = 'balanced'
    assert su._resolve_route_goal() is None, "an abandoned route must NOT resume once stance leaves 'retreat'"
    assert su.route == ()


# ─── Adversarial-review round 2 fixes (F2/F4/F5/F6/F11) ─────────────────────

def test_a_stalled_waypoint_is_dropped_after_the_route_budget_in_ticks():
    """F2: a waypoint has no general progress guarantee even once yield/retreat are handled
    correctly -- e.g. one placed where _node_advance's per-cell edge-clamping leaves the
    ACHIEVABLE anchor permanently more than ROUTE_WAYPOINT_EPS away from it. Since a pending route
    pre-empts every other _resolve_maneuver_goal branch unconditionally, an unreachable waypoint
    would otherwise lock the sub-unit forever. This drives _resolve_route_goal directly (not a full
    edge-clamp reproduction -- that is a much larger apparatus to construct) to isolate the
    stall-breaker's OWN bound: the anchor never actually moves closer to B across repeated calls,
    simulating 'no progress being made' regardless of cause."""
    u, su, anchor, (B, C) = _route_unit_from_offsets((5, 8))
    check_orders(u, 1, [])
    assert su.route == (B, C)
    for _ in range(int(ROUTE_BUDGET_TICKS) - 1):
        goal = su._resolve_route_goal()
        assert goal == B, "must keep offering the SAME unreached waypoint while under the tick bound"
    assert su._route_idx == 0, "control: cursor must not have moved yet"
    start_trace(True)
    try:
        goal = su._resolve_route_goal()
        events = [e for e in get_trace() if e.get('cat') == 'route_waypoint_stalled']
    finally:
        start_trace(False)
    assert su._route_idx == 1, "the stalled waypoint must be force-dropped once the tick bound is reached"
    assert goal == C, "the goal must now be the NEXT waypoint (the route continues, it does not abort)"
    assert len(events) == 1 and events[0]['idx'] == 0, f"expected one route_waypoint_stalled event at idx 0, got {events}"


def test_route_only_atom_is_excluded_from_movement_on_the_legacy_arm():
    """F5: a route-only atom (no target_atom, no escort) must NOT be included in run_battle's
    moving_a/moving_b list on the legacy-lattice arm (MB_NODE_COHESION=0) -- advance_cells' legacy
    no-target branch (`else: cell_offsets[...] += actual_speed`) does not hold position, it marches
    the atom full-speed along advance_dir forever, so inclusion there was not the harmless no-op
    round 1's own docstring claimed (see orchestration._is_moving_atom's own docstring)."""
    saved = _hu.MB_NODE_COHESION
    _hu.MB_NODE_COHESION = False
    try:
        su = _bare_subunit()
        su.route = ((10.0, 10.0),)
        assert not hasattr(su, '_node_anchor'), "control: this must be the legacy arm"
        assert su.target_atom is None and su.escort_of is None, "control: genuinely no other movement goal"
        assert _orch._is_moving_atom(su) is False, \
            "a route-only atom on the legacy arm must be excluded from moving_a/moving_b"
    finally:
        _hu.MB_NODE_COHESION = saved


def test_route_only_atom_is_included_when_the_node_path_is_active():
    """Control for the above: the SAME route-only atom, on the node path (MB_NODE_COHESION default
    True here), must still be included -- this is the case _resolve_route_goal actually consumes as
    a real steering goal, so excluding it there would silently un-fix A1 entirely."""
    su = _bare_subunit()
    su.route = ((10.0, 10.0),)
    assert hasattr(su, '_node_anchor'), "control: this must be the node path"
    assert su.target_atom is None and su.escort_of is None
    assert _orch._is_moving_atom(su) is True, \
        "a route-only atom on the node path must still be included in moving_a/moving_b"


def test_resume_partway_escape_hatch_does_not_spend_budget_on_already_passed_legs():
    """F6: an order resuming a route partway (`_route_idx` set alongside `route` in the SAME
    behavior dict -- the escape hatch check_orders' own comment documents) must have its budget
    measured ONLY over the waypoints it will actually walk (route[_route_idx:]), never through
    whatever the array holds before that index -- those are legs the caller's own resume intent
    says are already behind the sub-unit. Built so the contrast is stark: waypoint 0 sits 20 away
    from the anchor (comfortably beyond the 9.0 budget on its own), waypoints 1 and 2 sit close to
    the anchor and to each other (well within budget if measured fresh)."""
    u, su, anchor, (wp0, wp1, wp2) = _route_unit_from_offsets((20, 3, 6))
    # Direct control: clamping from index 0 (the pre-fix default) really does drop everything --
    # confirms this scenario is a genuine test of the fix, not a vacuous one.
    assert su._clamp_route_to_budget((wp0, wp1, wp2), start_idx=0) == (), \
        "control: measuring from index 0 must blow the budget on wp0 alone (20 > 9.0) and drop the whole route"
    su.orders = (Order('immediate', {'route': (wp0, wp1, wp2), '_route_idx': 1}),)
    check_orders(u, 1, [])
    assert su._route_idx == 1, "the explicit resume index must be honored"
    assert su.route == (wp0, wp1, wp2), \
        f"resuming at index 1 must measure the budget only from wp1 onward (well within 9.0) -- got {su.route}"


def test_route_rejects_a_bare_coordinate_pair_instead_of_a_tuple_of_waypoints():
    """F11: `{'route': (30, 20)}` (a single coordinate pair, not wrapped in an outer tuple of
    waypoints) must fail loudly at Order construction -- it used to unpack as two waypoints `30`
    and `20` and crash deep inside _clamp_route_to_budget on the tick the order fires, far from
    where the mistake was made."""
    with pytest.raises(ValueError, match="waypoint"):
        Order(trigger='immediate', behavior={'route': (30, 20)})


def test_route_rejects_a_non_numeric_waypoint():
    with pytest.raises(ValueError, match="waypoint"):
        Order(trigger='immediate', behavior={'route': (('a', 'b'),)})
