"""[ED-MB-0041] `unit.hp` and `sum(cell_troops)` must not diverge.

The adversarial audit found two ledgers feeding DIFFERENT mechanics:
  hp    -> _lanchester_strength, recalc_size, the single-subunit cohesion fast path
  cells -> pair_pool_contribution, troop_total()'s SUBUNIT_ROUT_FLOOR check
Divergence sources: (a) the pursuit and freed-attacker paths mutated hp with NO cell write at all;
(b) `distribute_casualties`/`apply_to_subunit` open-coded a single clamped pass that DISCARDED any
share a cell could not absorb, while hp took the damage in full. Only the cellwise variant had a
spill loop. All three now share `_apply_with_spill`.
"""
import os, sys
_SIM = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sim'))
if _SIM not in sys.path:
    sys.path.insert(0, _SIM)

import pytest
from mass_battle.engine import build_army, SIDE_A_START_ROW
from mass_battle.percell import distribute_casualties, _apply_with_spill


class _FakeAtom:
    def __init__(self, d):
        self.cell_troops = dict(d)


def _unit(troops=600.0):
    return build_army([{'shape': 'Line', 'troop_type': 'infantry', 'troops': troops,
                        'concentration': 100.0, 'starting_position': (SIDE_A_START_ROW, 9)}], 'A', 'A')


def _drift(u):
    return abs(sum(a.troop_total() for a in u.subunits) - u.hp)


def test_pursuit_style_damage_keeps_ledgers_in_step():
    """hp-only mutation was the pursuit/freed-attacker bug; both must mirror onto cells."""
    u = _unit()
    assert _drift(u) == pytest.approx(0.0, abs=1e-6)
    for dmg in (150.0, 200.0):
        u.hp = max(0, u.hp - dmg)
        distribute_casualties(u, dmg, [])
        u.recalc_size()
        assert _drift(u) == pytest.approx(0.0, abs=1e-6), (
            f"hp/cell ledgers diverged by {_drift(u)} after {dmg} damage")


def test_spill_conserves_damage_under_non_uniform_weights():
    """The real divergence case. With UNIFORM weights the old clamped pass and the spill agree (both
    empty everything). With NON-UNIFORM weights — which is exactly the facing-weighted cellwise path and
    concentrated fire — the old pass discarded the excess. Measured: 81.8 of 200 lost."""
    atom = _FakeAtom({('c', 0): 100.0, ('c', 1): 100.0})
    applied = _apply_with_spill([(atom, ('c', 0), 10.0), (atom, ('c', 1), 1.0)], 200.0)
    assert applied == pytest.approx(200.0, abs=1e-6), (
        f"spill conserved only {applied} of 200 — the excess-discard bug is back")
    assert sum(atom.cell_troops.values()) == pytest.approx(0.0, abs=1e-6)


def test_spill_shortfall_is_genuine_not_silent():
    """When damage genuinely exceeds every living troop, the shortfall is real and reported."""
    atom = _FakeAtom({('c', 0): 50.0})
    applied = _apply_with_spill([(atom, ('c', 0), 1.0)], 500.0)
    assert applied == pytest.approx(50.0, abs=1e-6)
    assert sum(atom.cell_troops.values()) == pytest.approx(0.0, abs=1e-6)
