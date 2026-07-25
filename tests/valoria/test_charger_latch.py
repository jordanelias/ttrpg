"""[ED-MB-0041 Tier-2] The braced-wall repel must survive the charge becoming an impulse.

`a_mom > b_mom` is how the engine identifies WHO the charger is; it is not the cause of the recoil. The
cause is a mounted body pressed onto a hedge of set poles, and a wall does not stop repelling after one
tick. Once momentum became an impulse (a halted cell records 0), the differential is true only on the
tick of impact — so re-deriving the charger role from it every tick reduced the repel to a single tick
and collapsed the pike-vs-cavalry retention margin from >0.02 to 0.0035.

The role is therefore latched at impact and held while the pair stays in contact. These tests pin the
latch's lifecycle: it is set, it survives the differential going flat, it is released when the bodies
part, and it does not leak into the next battle.
"""
import os, sys
_SIM = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sim'))
if _SIM not in sys.path:
    sys.path.insert(0, _SIM)

from mass_battle.engine import build_army, SIDE_A_START_ROW, SIDE_B_START_ROW
from mass_battle.orchestration import _expire_charger_latches, reset_morale_between_battles


def _unit(faction, col=20, troop_type='cavalry'):
    row = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    return build_army([{'shape': 'Line', 'troop_type': troop_type, 'troops': 300.0,
                        'concentration': 100.0, 'starting_position': (row, col)}],
                      faction, faction)


def _pair(a, b):
    return {'atom_a': a, 'atom_b': b,
            'a_cells': list(a.cells()), 'b_cells': list(b.cells())}


def test_latch_survives_while_the_pair_stays_in_contact():
    """The whole point: the differential goes flat after impact, the role must not."""
    ua, ub = _unit('A'), _unit('B', troop_type='pike')
    a, b = ua.subunits[0], ub.subunits[0]
    a._pressing = {id(b)}                       # as set on the impact tick

    _expire_charger_latches(ua, ub, [_pair(a, b)])
    assert id(b) in a._pressing, \
        "a charger still in contact with its target must keep the role after its momentum is spent"


def test_latch_is_released_when_the_bodies_part():
    """Otherwise a body that charged one wall arrives at the NEXT one already flagged as its charger."""
    ua, ub = _unit('A'), _unit('B', troop_type='pike')
    a, b = ua.subunits[0], ub.subunits[0]
    a._pressing = {id(b)}

    _expire_charger_latches(ua, ub, [])          # no contact pairs this tick
    assert id(b) not in a._pressing, \
        "the charger role must not outlive the contact that created it"


def test_latch_is_released_only_for_opponents_actually_left():
    """A body charging two enemies keeps the role against the one it is still touching."""
    ua = _unit('A')
    ub1, ub2 = _unit('B', col=20, troop_type='pike'), _unit('B', col=40, troop_type='pike')
    a = ua.subunits[0]
    b1, b2 = ub1.subunits[0], ub2.subunits[0]
    a._pressing = {id(b1), id(b2)}

    _expire_charger_latches(ua, ub1, [_pair(a, b1)])
    assert id(b1) in a._pressing, "still in contact with b1"
    assert id(b2) not in a._pressing, "no longer in contact with b2"


def test_latch_is_cleared_at_the_battle_boundary():
    """Per-engagement state, like every other transient reset_morale_between_battles clears."""
    ua, ub = _unit('A'), _unit('B', troop_type='pike')
    a, b = ua.subunits[0], ub.subunits[0]
    a._pressing = {id(b)}

    reset_morale_between_battles(ua)
    assert not a._pressing, \
        "a body that charged a wall last battle must not open the next one flagged as its charger"
