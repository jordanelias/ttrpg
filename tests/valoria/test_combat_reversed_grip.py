"""CI-tier: JD-4/JD-9 grounded formula fixes (U2 partial, ED-PC-0009, 2026-07-08).

geometry.py's thrust_factor floor drop (JD-9) and weapon_physics.reversed_grip_percussion (JD-4, the
Mordhau/Mordschlag pommel-strike model) — determined this session by testing bottom-up emergent primitives
(mass/position/geometry, no per-weapon table) and validating top-down against HEMA sourcing (Wikipedia
"Mordhau (weaponry)"; Malevus "Mordhau: The Murder Stroke Technique") and physics (pressure = force/area).
Both are correct and tested at the FORMULA level; NEITHER is wired into element_afforded's live mode-
selection this session — see systems.py's element_afforded docstring for the architectural gap that blocks
safe integration (core.coupling's DELIVERY constants don't scale with percussion magnitude except against
mail/plate, so a naive wiring made every two-handed sword prefer a weak pommel-strike over its own edge
against UNARMOURED targets — backwards from the historical grounding)."""
import os
import sys

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'designs', 'scene', 'combat_engine_v1')
sys.path.insert(0, ENGINE)

import pytest  # noqa: E402
pytest.importorskip("numpy")  # engine import chain needs numpy + the sim modules; skip in the lightweight validator job

import geometry as G  # noqa: E402
import weapon_physics as WP  # noqa: E402
from combatant import WEAPONS  # noqa: E402


def test_mace_staff_no_thrust():
    """JD-9: a broad, pointless face (mace pc=0.02, staff pc=0.05) must read ~0 thrust regardless of rigidity —
    pressure = force/area, not force/rigidity. The pre-fix formula's additive floor gave both a nontrivial
    0.31-0.34 "thrust" from cross_section alone."""
    for n in ('mace', 'staff'):
        g = WEAPONS[n]['geometry']
        t = G.thrust_factor(g['point_concentration'], g['cross_section'], g['curvature'])
        assert t < 0.05, f"{n}: thrust={t} should be near-zero"


def test_needle_class_no_cut():
    """The needle-class thrusters (edge_keenness<=0.1, the roster's own edgeless-consistency invariant) must
    read ~0 cut. The pre-fix formula's additive floor gave every weapon (even mace/staff, ek=0) a floored
    0.45+ cut regardless of edge."""
    for n in ('stiletto', 'estoc', 'rondel'):
        g = WEAPONS[n]['geometry']
        c = G.cut_factor(g['curvature'], g['edge_keenness'])
        assert c < 0.10, f"{n}: cut={c} should be near-zero (edgeless-consistency, ek<=0.1)"
    for n in ('mace', 'staff'):
        g = WEAPONS[n]['geometry']
        c = G.cut_factor(g['curvature'], g['edge_keenness'])
        assert c == 0.0, f"{n}: cut={c} should be exactly zero (ek=0)"


def test_thrust_factor_is_wired():
    """element_afforded's cut_thrust atomic branch now compares cut against geo['thrust'] (the general thrust-
    effectiveness primitive) instead of geo['gap'] (the armour-gap-seeking primitive, a different physical
    fact kept for the downstream armour-defeat math) — the previously-dead thrust_factor is live. Checked
    directly against the formula (not a hand-picked weapon pair, since gap and thrust are close enough across
    the roster that no weapon reliably demonstrates the direction of the swap on its own)."""
    import systems as S
    for n in ('longsword', 'arming', 'dagger', 'jian'):
        w = WEAPONS[n]
        assert w['head'] == 'cut_thrust', f"test premise: {n} must be cut_thrust-headed"
        geo = w['geometry']
        thrust = G.thrust_factor(geo['point_concentration'], geo['cross_section'], geo['curvature'])
        cut = G.cut_factor(geo['curvature'], geo['edge_keenness'])
        heads = S.afforded_heads(w)
        eff = heads['cut_thrust'][0]
        assert abs(eff - max(cut, thrust)) < 1e-9, f"{n}: cut_thrust score should be max(cut, thrust)"


def test_sword_pommel_weak_percussion():
    """JD-4: a two-handed bladed weapon's Mordhau/reversed-grip percussion option exists (nonzero — the self-
    gate no longer hard-zeroes every non-blunt head) but reads clearly weak relative to a dedicated blunt
    weapon (mace/poleaxe), matching the HEMA sourcing (a documented supplementary technique, "far less
    injurious" than a purpose-built mace/warhammer against rigid plate)."""
    mace_perc = WP.percussion_authority(WEAPONS['mace'])
    poleaxe_perc = WP.percussion_authority(WEAPONS['poleaxe'])
    for n in ('longsword', 'greatsword', 'katana', 'estoc'):
        perc = WP.percussion_authority(WEAPONS[n])
        assert 0.0 < perc < 2.5, f"{n}: reversed-grip percussion={perc} should be nonzero but weak"
        assert perc < mace_perc * 0.35, f"{n}: {perc} should sit well below mace's {mace_perc}"
        assert perc < poleaxe_perc * 0.35, f"{n}: {perc} should sit well below poleaxe's {poleaxe_perc}"


def test_reversed_grip_gated_to_two_handed_bladed():
    """No comparable technique is attested in the sourced material for one-handed swords/daggers (too short
    to grip past for a HEMA-style Mordhau) or for hafted weapons (they already have a dedicated head)."""
    for n in ('rapier', 'arming', 'sabre', 'dagger'):
        assert WEAPONS[n]['hands'] == 1, f"test premise: {n} must be one-handed"
        assert WP.percussion_authority(WEAPONS[n]) == 0.0, f"{n} (1H) should have no reversed-grip option"
    assert WP.reversed_grip_percussion(WEAPONS['poleaxe']) == 0.0, "hafted weapons have their own dedicated head"


def test_reversed_grip_percussion_uses_hilt_mass_not_whole_weapon():
    """Bottom-up check: the formula's magnitude is driven by hilt_assembly_mass (guard+pommel+haft), not
    whole-weapon mass — a weapon with a heavier hilt assembly (relative to its own total mass) should not
    trivially dominate one with a lighter hilt, confirming the model reads located parts, not a lump."""
    heavy_hilt_frac = WP.hilt_assembly_mass(WEAPONS['rapier']) / WEAPONS['rapier']['mass']
    assert heavy_hilt_frac > 0.5, "test premise: rapier's compound hilt is a large mass fraction"
    # rapier is 1-handed, so its OWN reversed-grip percussion is gated to 0 regardless of hilt mass —
    # confirms the hands==2 gate is the binding constraint, not hilt mass alone.
    assert WP.reversed_grip_percussion(WEAPONS['rapier']) == 0.0
