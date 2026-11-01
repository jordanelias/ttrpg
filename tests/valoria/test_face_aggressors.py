"""A cell under attack turns toward its aggressors (hierarchy.units.turn_to_face_aggressors).

The rule, Jordan: a cell under attack rotates to face its aggressor, unless it is caught between two, in which case it
faces the averaged position. Per cell, rate-limited by _slew_facing, run once at the end of every tick. Before it
existed a cell in contact was halted and a body on `hold` returned early, so neither wrote a facing: the octagon zone
was judged against a facing that never followed the fight (measured on the walkthrough example, ticks 8 to 11).

Each test builds two units, parks every cell far apart, then places only the cells under test. The control
(`test_the_step_is_what_turns_the_cell`) turns the step off and asserts the cell did not turn, so the other tests'
"it turned" is something the step did and not a default.
"""
import math

import pytest

import modules.mass_battle.hierarchy.units as _hu
import modules.mass_battle.orchestration as _orch
from systems.mass_battle.sim import validators as _val
from systems.mass_battle.sim.engine import build_unit


@pytest.fixture
def field_path():
    saved = [(m, m.FIELD_MOVEMENT, m.MB_NODE_COHESION) for m in (_hu, _orch)]
    _val._set_movement_path('node')
    try:
        yield
    finally:
        for m, fm, nc in saved:
            m.FIELD_MOVEMENT = fm
            m.MB_NODE_COHESION = nc


def _park(unit, row0):
    """Every cell of `unit` to its own spot, 5 pitches from any other, far from the cells under test."""
    for atom in unit.subunits:
        for k, cid in enumerate(sorted(atom._node_pos)):
            atom._node_pos[cid] = (row0 + 5.0 * (k // 5), 5.0 * (k % 5))


def _setup(enemy_offsets, facing=(-1.0, 0.0)):
    """A's first cell at (10, 10) with `facing`; one B cell at each (10 + dr, 10 + dc) in `enemy_offsets`."""
    a = build_unit('Line', 3, 'A', 'A', 9)
    b = build_unit('Line', 3, 'B', 'B', 9)
    _park(a, 100.0)
    _park(b, 200.0)
    sa, sb = a.subunits[0], b.subunits[0]
    a_cid = sorted(sa._node_pos)[0]
    sa._node_pos[a_cid] = (10.0, 10.0)
    sa.cell_facing_vec[a_cid] = facing
    for cid, (dr, dc) in zip(sorted(sb._node_pos), enemy_offsets):
        sb._node_pos[cid] = (10.0 + dr, 10.0 + dc)
    return a, b, sa, a_cid


def _bearing_error(vec, target):
    """Degrees between the facing `vec` and the direction `target`."""
    return math.degrees(abs(math.atan2(vec[0] * target[1] - vec[1] * target[0], vec[0] * target[0] + vec[1] * target[1])))


def test_the_cell_turns_toward_an_aggressor_at_a_rate_not_instantly(field_path):
    a, b, sa, cid = _setup([(0.0, 1.0)])               # aggressor beside it: 90 degrees off a facing of -row
    assert sa.eff_discipline >= 5, "the 60-degree figure below assumes full discipline"
    start = _bearing_error(sa.cell_facing_vec[cid], (0.0, 1.0))
    assert start == pytest.approx(90.0)
    assert _hu.turn_to_face_aggressors(a, b) >= 1
    after_one = _bearing_error(sa.cell_facing_vec[cid], (0.0, 1.0))
    assert after_one == pytest.approx(90.0 - _hu.MB_FACING_SLEW_BASE, abs=1e-6), "one tick turns by the slew rate, no more"
    _hu.turn_to_face_aggressors(a, b)
    assert _bearing_error(sa.cell_facing_vec[cid], (0.0, 1.0)) == pytest.approx(0.0, abs=1e-6)


def test_the_step_is_what_turns_the_cell(field_path, monkeypatch):
    """Control: with the step off the same cell keeps its facing, so the test above observes the step."""
    monkeypatch.setattr(_hu, 'MB_FACING_ATTENTION', False)
    a, b, sa, cid = _setup([(0.0, 1.0)])
    assert _hu.turn_to_face_aggressors(a, b) == 0
    assert sa.cell_facing_vec[cid] == (-1.0, 0.0)


def test_a_cell_between_two_aggressors_faces_their_average(field_path):
    a, b, sa, cid = _setup([(0.0, 1.0), (-1.0, 1.0)], facing=(0.0, 1.0))   # at +col and at (-row, +col)
    for _ in range(3):
        _hu.turn_to_face_aggressors(a, b)
    avg = (-0.5, 1.0)                                                       # the mean of the two offsets
    assert _bearing_error(sa.cell_facing_vec[cid], avg) == pytest.approx(0.0, abs=1e-6)


def test_a_cell_between_aggressors_on_opposite_sides_holds_its_facing(field_path):
    a, b, sa, cid = _setup([(0.0, 1.0), (0.0, -1.0)], facing=(-1.0, 0.0))
    _hu.turn_to_face_aggressors(a, b)      # the two B cells each turn toward A's cell; A's cell has balanced aggressors
    assert sa.cell_facing_vec[cid] == (-1.0, 0.0)


def test_a_cell_does_not_turn_toward_an_aggressor_it_cannot_see(field_path):
    a, b, sa, cid = _setup([(1.0, 0.0)])               # directly behind a facing of -row: inside the rear blind arc
    _hu.turn_to_face_aggressors(a, b)
    assert sa.cell_facing_vec[cid] == (-1.0, 0.0)


def test_a_body_on_hold_still_turns(field_path):
    a, b, sa, cid = _setup([(0.0, 1.0)])
    sa.stance = 'hold'
    assert sa.eff_stance == 'hold'
    assert _hu.turn_to_face_aggressors(a, b) >= 1
    assert _bearing_error(sa.cell_facing_vec[cid], (0.0, 1.0)) < 90.0


def test_the_grid_oracle_is_untouched(field_path):
    _val._set_movement_path('grid')
    a = build_unit('Line', 3, 'A', 'A', 9)
    b = build_unit('Line', 3, 'B', 'B', 9)
    assert _hu.turn_to_face_aggressors(a, b) == 0
