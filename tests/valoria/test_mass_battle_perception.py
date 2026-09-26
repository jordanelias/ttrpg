"""A2, ED-MB-0067 Part A (proposals/2026-09-25-squad-engagement-synthesis.md) — order conditions
limited to what the unit can know.

`core/contact.py`'s `enemy_range:` trigger read every enemy cell unconditionally; `_visible_enemy_cells`
now filters through a facing cone (angle-to-facing <= FOV_HALF_DEG (105 deg) -- all of GREEN (<45)
and YELLOW (45-90) PLUS 15 degrees of RED; NOT the GREEN+YELLOW boundary itself (90 deg) -- a first
version of this docstring claimed the two were the same, corrected after review) before `enemy_range:`
ever measures a distance. Composed on the SAME MB_FACING_MODEL/MB_FACING_FOV_GATE flags every other
facing-gated mechanic in this engine already uses -- with either off, every enemy cell counts as
visible (no distance axis at all: a first version added a standalone MB_SIGHT_RANGE, removed as
provably dead by construction -- see config.py's own comment). Control for `build_refused_flank`'s
oblique-row digest (bat.py) not moving is run separately (see the session report) since it needs the
full battery/hashing harness, not a unit-level pytest.
"""
import pytest

import systems.mass_battle.sim.hierarchy.units as _hu
from systems.mass_battle.sim.config import FOV_HALF_DEG
from systems.mass_battle.sim.core.contact import _visible_enemy_cells, check_orders
from systems.mass_battle.sim.hierarchy.units import Order, Subunit, Unit


def _facing_unit(facing):
    """A lone Line subunit with its node facing pinned to a known unit vector (bypassing the
    tick-by-tick facing-update machinery entirely -- this test is about the PERCEPTION filter, not
    about how facing itself comes to be set)."""
    su = Subunit(shape='Line', troop_type='infantry', tier=2,
                 starting_position=(25, 25), advance_dir=1, stance='balanced', unit_type='melee')
    su._node_facing = facing
    u = Unit(name='observer', faction='A', power=4, command=4, discipline=5, discipline_start=5,
             morale=6, morale_start=6, subunits=[su])
    return u, su


def test_visible_enemy_cells_facing_cone_directly():
    """Value-level control on the filter itself, independent of check_orders: a cell dead ahead of
    facing (1,0) is visible; a cell dead behind (angle 180, RED, past FOV_HALF_DEG=105) is not."""
    u, su = _facing_unit((1.0, 0.0))
    my = su.centroid()
    ahead = (my[0] + 5.0, my[1])
    behind = (my[0] - 5.0, my[1])
    assert _visible_enemy_cells(su, [ahead]) == [ahead]
    assert _visible_enemy_cells(su, [behind]) == []
    assert _visible_enemy_cells(su, [ahead, behind]) == [ahead]


def test_visible_enemy_cells_falls_back_to_advance_dir_when_facing_unset():
    """Default _node_facing is None at construction (never yet slewed by a tick) -- falls back to
    (advance_dir, 0), the same fallback find_contacts' head_a/head_b already use."""
    su = Subunit(shape='Line', troop_type='infantry', tier=2,
                 starting_position=(25, 25), advance_dir=1, stance='balanced', unit_type='melee')
    assert su._node_facing is None
    my = su.centroid()
    ahead = (my[0] + 5.0, my[1])   # advance_dir=1 -> facing (1,0) -> "ahead" is +row, same as above
    assert _visible_enemy_cells(su, [ahead]) == [ahead]


def test_enemy_range_does_not_fire_for_an_enemy_outside_the_facing_cone():
    u, su = _facing_unit((1.0, 0.0))
    my = su.centroid()
    behind = (my[0] - 5.0, my[1])   # in range (5 <= 10) but behind facing
    su.orders = (Order('enemy_range:10', {'stance': 'hold'}),)
    check_orders(u, 1, [behind])
    assert su._order_idx == 0, "enemy_range: must not fire for an enemy outside the facing cone"
    assert su.stance == 'balanced'


def test_enemy_range_fires_once_the_same_enemy_is_brought_into_the_cone():
    u, su = _facing_unit((1.0, 0.0))
    my = su.centroid()
    ahead = (my[0] + 5.0, my[1])     # same distance (5), now in front instead of behind
    su.orders = (Order('enemy_range:10', {'stance': 'hold'}),)
    check_orders(u, 1, [ahead])
    assert su._order_idx == 1, "enemy_range: must fire once the same-distance enemy is inside the cone"
    assert su.stance == 'hold'


def test_enemy_range_still_respects_its_own_distance_bound_inside_the_cone():
    """A2 adds a facing filter; it must not turn enemy_range: into an unconditional cone-only
    trigger -- an enemy inside the cone but beyond D must still not fire (enemy_range:'s OWN
    distance test, unaffected by A2, is a separate axis from the facing filter)."""
    u, su = _facing_unit((1.0, 0.0))
    my = su.centroid()
    far_ahead = (my[0] + 8.0, my[1])   # inside the cone, but beyond D=5
    su.orders = (Order('enemy_range:5', {'stance': 'hold'}),)
    check_orders(u, 1, [far_ahead])
    assert su._order_idx == 0
    assert su.stance == 'balanced'


# ─── Adversarial-review round 2: flag composition ────────────────────────────

def test_facing_filter_is_a_noop_when_the_facing_model_is_off():
    """Composed on MB_FACING_MODEL/MB_FACING_FOV_GATE (the SAME flags orchestration.py's own
    existing FOV-blind-arc gate already uses), not a parallel always-on check. With the facing
    model off (its FIELD_PINS value in every golden-battery mode), a cell behind facing must count
    as visible -- the mechanism must not silently keep filtering in a configuration where every
    OTHER facing-gated mechanic in this engine is a deliberate no-op."""
    saved_model, saved_gate = _hu.MB_FACING_MODEL, _hu.MB_FACING_FOV_GATE
    _hu.MB_FACING_MODEL = False
    try:
        u, su = _facing_unit((1.0, 0.0))
        my = su.centroid()
        behind = (my[0] - 5.0, my[1])
        assert _visible_enemy_cells(su, [behind]) == [behind], \
            "MB_FACING_MODEL=False must make the facing filter a no-op"
    finally:
        _hu.MB_FACING_MODEL = saved_model
        _hu.MB_FACING_FOV_GATE = saved_gate


def test_facing_filter_is_a_noop_when_only_the_fov_gate_is_off():
    """The composition is an AND of both flags -- MB_FACING_MODEL on but MB_FACING_FOV_GATE off
    must also disable the filter, matching orchestration.py's own existing gate's exact condition."""
    saved_model, saved_gate = _hu.MB_FACING_MODEL, _hu.MB_FACING_FOV_GATE
    _hu.MB_FACING_MODEL = True
    _hu.MB_FACING_FOV_GATE = False
    try:
        u, su = _facing_unit((1.0, 0.0))
        my = su.centroid()
        behind = (my[0] - 5.0, my[1])
        assert _visible_enemy_cells(su, [behind]) == [behind]
    finally:
        _hu.MB_FACING_MODEL = saved_model
        _hu.MB_FACING_FOV_GATE = saved_gate


def test_facing_filter_is_live_when_both_flags_are_on():
    """Control: with both flags at their (default-ON) shipped values, the filter is live -- the two
    tests above are demonstrating a real gate, not a mechanism that never filters anything."""
    assert _hu.MB_FACING_MODEL and _hu.MB_FACING_FOV_GATE, \
        "control: both flags must default ON for the no-op tests above to mean anything"
    u, su = _facing_unit((1.0, 0.0))
    my = su.centroid()
    behind = (my[0] - 5.0, my[1])
    assert _visible_enemy_cells(su, [behind]) == []
