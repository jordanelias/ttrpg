"""[ED-MB-0041 Tier-2] A body ordered to HOLD must stop reading as a charger.

`cell_last_speed` feeds `_momentum_speed`, which drives puncture, the du Picq charge-shock and the
braced-wall recoil. Both movement paths return early on `stance == "hold"`, skipping the arithmetic that
would have written a speed — and `STANCE_SPEED_MOD['hold']` is -99, i.e. that arithmetic would have
produced 0. So a subunit that closed at speed and was then ordered to hold kept its approach speed in
the map forever, and `_momentum_speed` went on reading a stationary braced wall as though it were still
charging. Both paths now zero the map on the hold branch.

**Scope note — the wider momentum-at-halt question is deliberately NOT settled here.** A cell halted by
contact (rather than by a hold order) also keeps a frozen speed. Both obvious repairs were built and
measured, and both break a historical anchor: recording 0 collapses the pike-vs-cavalry retention margin
from >0.02 to 0.0035 (the braced-wall repel becomes a one-tick event), while recording the current
intended step sends gauge row C1 — cavalry against a steady unbraced line — from 48.3% to 85.0%, far
outside its 35-55 band. The shared cause is that the engine has no charge/recoil/re-charge cycle, so
every per-tick momentum semantics is standing in for a mechanism that does not exist. That is recorded
as a Tier-3 design call. `hold` is the unambiguous sub-case and is the only part fixed.
"""
import os, sys
_SIM = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sim'))
if _SIM not in sys.path:
    sys.path.insert(0, _SIM)

import pytest
from mass_battle.engine import build_army, SIDE_A_START_ROW
from mass_battle.orchestration import _momentum_speed


def _subunit():
    army = build_army([{'shape': 'Line', 'troop_type': 'infantry', 'troops': 300.0,
                        'concentration': 100.0, 'starting_position': (SIDE_A_START_ROW, 20)}],
                      'A', 'A')
    return army.subunits[0]


def _close(su):
    """Advance once so the body records real, non-zero cell speeds."""
    target = (su.centroid()[0] + 30, su.centroid()[1])
    su.advance_cells(5, target)
    return target


def test_a_closing_body_records_momentum():
    """Control: the quantity under test is non-zero to begin with, so the assertions below mean something."""
    su = _subunit()
    _close(su)
    assert _momentum_speed(su, list(su.cells())) > 0


def test_hold_zeroes_pressing_speed_on_the_live_node_path():
    su = _subunit()
    target = _close(su)
    if not hasattr(su, '_node_pos'):
        pytest.skip("node/field path not active in this configuration")
    su.stance = 'hold'
    su.advance_cells(5, target)
    assert _momentum_speed(su, list(su.cells())) == 0, \
        "a body ordered to hold must stop registering as pressing"


def test_hold_zeroes_pressing_speed_on_the_legacy_grid_path():
    su = _subunit()
    su.stance = 'aggressive'
    if hasattr(su, '_node_pos'):
        del su._node_pos                     # force the legacy grid branch
    target = _close(su)
    if not any(su.cell_last_speed.values()):
        pytest.skip("legacy grid path recorded no motion in this configuration")
    su.stance = 'hold'
    su.advance_cells(5, target)
    assert all(v == 0 for v in su.cell_last_speed.values()), \
        "the legacy path must zero on hold too — same early return, same rule"
