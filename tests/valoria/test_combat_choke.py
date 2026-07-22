"""Polearm choke counterbalance — U5 / ED-PC-0019.

consolidation_v1.md §6 U5. Choking UP a head-heavy pole (grip_position>0) to counterbalance its forward mass trades
a shallow, floored loss of thrust authority (weapon_physics.phi_grip, CHOKE_THRUST_K) and of fine precision (a
gathered pole telegraphs -> systems.choke_counterbalance -> legibility, CHOKE_ACCURACY_K). Both K=0 at landing, so
the grip-invariant-thrust first principle and every outcome are byte-identical until the U9 recalibration flips them.
Half-sword forms are exempt. These tests pin the K=0 byte-identity, the counterbalance derivation, the exemption,
and that both channels are live-not-dead.
"""
import os
import sys

import pytest

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)
pytest.importorskip("numpy")

import weapon_physics as WP  # noqa: E402
import combat_systems as S  # noqa: E402
from combatant import WEAPONS, Combatant  # noqa: E402
from config import CFG  # noqa: E402


def test_thrust_grip_invariant_at_k_zero():
    """The first principle holds exactly at K=0: an axial thrust (point head) is grip-invariant (phi_grip==1.0) at
    EVERY grip — CHOKE_THRUST_K=0 preserves it byte-identically."""
    assert WP.CHOKE_THRUST_K == 0.0
    for g in (0.0, 0.25, 0.5, 0.75, 1.0):
        assert WP.phi_grip(WEAPONS['spear'], g, 'point') == 1.0, g


def test_choke_accuracy_k_zero():
    """The accuracy/legibility channel is inert at landing (CHOKE_ACCURACY_K=0), so legibility is byte-identical."""
    assert CFG['CHOKE_ACCURACY_K'] == 0.0


def test_choke_counterbalance_derivation():
    """choke_counterbalance is 0 at the open measure (grip=0), rises with grip, and is stronger for a head-heavy pole
    (high rear_clearance) than a compact weapon — reusing the rear-clearance delta, no new primitive."""
    for n in ('poleaxe', 'spear', 'arming', 'dagger'):
        c = Combatant('x', weapon=n); c.grip_position = 0.0
        assert S.choke_counterbalance(c, CFG) == 0.0, n            # 0 at the open measure
    pole = Combatant('x', weapon='poleaxe'); pole.grip_position = 1.0
    compact = Combatant('x', weapon='dagger'); compact.grip_position = 1.0
    assert S.choke_counterbalance(pole, CFG) > S.choke_counterbalance(compact, CFG)   # pole counterbalances more
    assert 0.0 < S.choke_counterbalance(pole, CFG) <= 1.0


def test_halfsword_form_exempt():
    """A *_halfsword form is exempt (its grip is the blade-grip, a different mechanic) — choke_counterbalance is 0
    even fully gathered."""
    c = Combatant.__new__(Combatant)
    c.weapon = 'longsword_halfsword'; c.grip_position = 1.0
    assert S.choke_counterbalance(c, CFG) == 0.0


def test_both_channels_live_not_dead():
    """Both K=0 terms move when their constant is flipped (in the physically-correct direction) — non-vestigial."""
    # thrust: a choked spear thrust degrades below 1.0 once CHOKE_THRUST_K>0
    import importlib
    base = WP.phi_grip(WEAPONS['spear'], 1.0, 'point')
    WP.CHOKE_THRUST_K = 0.3
    try:
        assert WP.phi_grip(WEAPONS['spear'], 1.0, 'point') < base
    finally:
        WP.CHOKE_THRUST_K = 0.0
    # legibility: a choked poleaxe reads MORE legible once CHOKE_ACCURACY_K>0
    pole = Combatant('A', weapon='poleaxe'); pole.grip_position = 1.0
    l0 = S.legibility(pole, 3, CFG)
    lk = S.legibility(pole, 3, dict(CFG, CHOKE_ACCURACY_K=0.4))
    assert lk > l0
