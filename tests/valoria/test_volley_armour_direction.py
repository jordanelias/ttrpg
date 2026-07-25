"""[ED-MB-0041] Armour must REDUCE missile casualties, never increase them.

The adversarial audit found two compounding defects in the volley phase:
  1. `volley_hp_scale = max(1, (h_per_size + 1) // 2)` with
     `h_per_size = max(1, min(discipline, command) + dr)` — so better armour, discipline or command
     STRICTLY INCREASED the missile casualties that unit suffered (dr 1 -> x3, dr 3 -> x4).
  2. `net_after_dr = max(0, net - RANGED_DR_DEFAULT)` used a GLOBAL constant, so a target's real
     armour never reduced incoming fire at all.
Together: armour was strictly harmful against archery. These tests pin the correct direction.
"""
import os, sys
_SIM = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sim'))
if _SIM not in sys.path:
    sys.path.insert(0, _SIM)

import random
import pytest
from mass_battle.engine import build_army, SIDE_A_START_ROW, SIDE_B_START_ROW, resolve_battle

ANCHOR = {('Line', 3): 9}


def _unit(name, faction, dr=1, unit_type='melee', stance='balanced', row=None):
    if row is None:
        row = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    u = build_army([{'shape': 'Line', 'troop_type': 'infantry', 'unit_type': unit_type,
                     'troops': 600.0, 'concentration': 100.0, 'stance': stance,
                     'starting_position': (row, 9)}],
                   name, faction, dr=dr, stance=stance)
    u.dr = dr
    for a in u.subunits:
        a.dr = dr
    u.recalc_size()
    return u


def _volley_loss(dr, n=12):
    """ISOLATE the volley. Calling resolve_battle and measuring total hp loss does NOT isolate it —
    melee also consumes `eff_dr`, and that melee protection masks the volley inversion (my first version
    of this test passed against the known-buggy code for exactly that reason). Drive volley_phase
    directly and read its own reported loss."""
    from mass_battle.orchestration import volley_phase
    total = 0.0
    for s_ in range(n):
        random.seed(1_000_000 + s_)
        shooters = _unit('A', 'A', dr=1, unit_type='ranged', stance='hold', row=20)
        target = _unit('B', 'B', dr=dr, row=15)   # distance 5 <= VOLLEY_MAX_RANGE
        vol = volley_phase(shooters, target)
        total += vol.get('loss_b', 0.0)
    return total / n


def test_armour_is_monotonically_protective_against_missiles():
    """Heavier armour must not increase missile casualties. Pre-fix this was strictly increasing."""
    c0 = _volley_loss(0)
    c1 = _volley_loss(1)
    c3 = _volley_loss(3)
    assert c1 <= c0, f"dr 1 ({c1:.1f}) took MORE than dr 0 ({c0:.1f}) — armour inversion is back"
    assert c3 <= c1, f"dr 3 ({c3:.1f}) took MORE than dr 1 ({c1:.1f}) — armour inversion is back"
    assert c3 < c0, f"dr 3 ({c3:.1f}) should be strictly better protected than dr 0 ({c0:.1f})"


def test_volley_scale_is_independent_of_target_quality():
    """The Size->troops volley conversion must not read the target's own stats."""
    from mass_battle.config import VOLLEY_LETHALITY_SCALE
    assert isinstance(VOLLEY_LETHALITY_SCALE, (int, float))
    # A unit's own discipline/command/dr must not appear in the conversion factor.
    import inspect
    from mass_battle import orchestration
    src = inspect.getsource(orchestration.run_battle)
    assert 'volley_hp_scale = lambda u: VOLLEY_LETHALITY_SCALE' in src, (
        "volley_hp_scale must be a flat constant; a per-target expression reintroduces the inversion")
