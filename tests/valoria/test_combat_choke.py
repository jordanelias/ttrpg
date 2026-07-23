"""Polearm choke counterbalance — U5 / ED-PC-0019, ACTIVATED + re-homed U10 / ED-PC-0022.

consolidation_v1.md §6 U5 + audit/2026-07-04-weapon-morphology-granularity/u10_activation_v1.md.

Choking UP a head-heavy pole (grip_position>0) to counterbalance its forward mass costs CONTROL: the gathered
posture telegraphs and the shortened rear lever lets the point be beaten off-line. U5 originally split that cost
across two channels — an accuracy/legibility term (systems.choke_counterbalance -> CHOKE_ACCURACY_K) AND a thrust-
authority term mis-parked in weapon_physics.phi_grip (CHOKE_THRUST_K). U10/ED-PC-0022 RE-HOMED the thrust cost:
choking a rigid shaft does NOT reduce axial-thrust FORCE (the ratified D2 grip-invariant-thrust principle is
physically correct and stays byte-identical), so the whole choke cost now lives in the SINGLE control/legibility
channel where it belongs, and CHOKE_THRUST_K is retired. These tests pin: the D2 force-invariant holds
UNCONDITIONALLY, the accuracy channel is live and tradition-modulable, the counterbalance derivation, and the
half-sword exemption.
"""
import os
import sys

import pytest

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)
pytest.importorskip("numpy")

import weapon_physics as WP  # noqa: E402
import combat_systems as S  # noqa: E402
import ability_primitives as ABIL  # noqa: E402
from combatant import WEAPONS, Combatant  # noqa: E402
from config import CFG  # noqa: E402


def test_thrust_force_grip_invariant_unconditional():
    """The D2 first principle now holds by CONSTRUCTION, not by a K=0 pin: an axial thrust (point head) delivers
    grip-invariant FORCE (phi_grip==1.0) at EVERY grip, because a rigid shaft transmits axial compression
    independent of hand position. CHOKE_THRUST_K is retired — there is no constant that can break this (U10/ED-PC-0022).
    The choke's real cost is CONTROL, captured in the accuracy channel below, not in the force multiplier."""
    assert not hasattr(WP, 'CHOKE_THRUST_K'), "CHOKE_THRUST_K should be retired (re-homed to the accuracy channel)"
    for g in (0.0, 0.25, 0.5, 0.75, 1.0):
        assert WP.phi_grip(WEAPONS['spear'], g, 'point') == 1.0, g
        assert WP.phi_grip(WEAPONS['bear_spear'], g, 'point') == 1.0, g
        assert WP.phi_grip(WEAPONS['yari'], g, 'point') == 1.0, g


def test_choke_accuracy_active():
    """The accuracy/legibility channel is now LIVE (CHOKE_ACCURACY_K>0) — it carries the WHOLE choke cost after the
    thrust-side re-home."""
    assert CFG['CHOKE_ACCURACY_K'] > 0.0


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


def test_choke_accuracy_live_no_global_mutation():
    """The choke telegraph is live (a gathered poleaxe reads MORE legible) — proven via a LOCAL cfg override, never a
    raw module-global write. This closes the U9 review-hazard: the old test mutated weapon_physics.CHOKE_THRUST_K and
    leaked 0.0 to later test modules; the constant is now gone and the channel is exercised with cfg + equipped state.
    The 'choke_control' mitigation hook is reachable and inert-safe (factor 1.0 with no ability equipped)."""
    pole = Combatant('A', weapon='poleaxe'); pole.grip_position = 1.0
    l_off = S.legibility(pole, 3, dict(CFG, CHOKE_ACCURACY_K=0.0))    # channel off (local cfg, no global write)
    l_on = S.legibility(pole, 3, CFG)                                 # channel on -> more legible (telegraph)
    assert l_on > l_off
    assert ABIL.ability_factor(pole, 'choke_control') == 1.0          # surface exists, inert-safe by default
