"""Point-token thrust-magnitude scaling — THRUST_AUTH_REF (ED-PC-0012 / RBNI item PC-4).

The second, structurally identical gap to the one CUT_AUTH_REF closed for 'cut': core.coupling credited
DELIVERY['point']=1.45 IN FULL to a weak incidental point on a dedicated slasher, so every cutter with any
secondary point token eventually switched to 'point' vs armour on the fixed constant alone (a floor-locked
artifact — the sabre/scimitar/falchion spurious plate-switch). The fix scales DELIVERY['point'] by the
SELECTED point's own derived thrust magnitude (eff) vs THRUST_AUTH_REF, anchored just below the weakest
NATIVE pointer (bear_spear 0.53) so every dedicated thruster clamps to 1.0 and only incidental points are
discounted. These tests pin: (1) the clamp/scale shape, (2) native pointers untouched, (3) the slashers no
longer spurious-switch, (4) the ED's flagged voulge edge-gate residual.
"""
import os
import sys

import pytest

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)
pytest.importorskip("numpy")

import core  # noqa: E402
import combat_systems as S  # noqa: E402
from combatant import WEAPONS, Combatant  # noqa: E402
from config import CFG  # noqa: E402

_TIERS = ('none', 'light', 'medium', 'heavy')


def test_anchor_below_weakest_native_pointer():
    """THRUST_AUTH_REF sits just below the weakest NATIVE point-headed weapon's point magnitude (bear_spear ~0.53),
    so every dedicated thruster clamps to ratio 1.0 and is unaffected — the CUT_AUTH_REF/hook_sword principle."""
    native_point_eff = [S.afforded_heads(w).get('point', (None,))[0]
                        for n, w in WEAPONS.items() if 'base' not in w and w.get('head') == 'point']
    native_point_eff = [e for e in native_point_eff if e is not None]
    assert core.THRUST_AUTH_REF <= min(native_point_eff) + 1e-9, (core.THRUST_AUTH_REF, min(native_point_eff))


def test_point_delivery_scales_by_magnitude_and_clamps():
    """A weak incidental point is discounted by eff/THRUST_AUTH_REF; a dedicated point (eff>=ref) clamps to 1.0 and is
    byte-identical to the pre-fix (eff=None) coupling. Scoped to 'point' only."""
    for armor in _TIERS:
        base = core.coupling('point', armor)                          # pre-fix behaviour (no scaling)
        assert core.coupling('point', armor, eff=0.61) == base, armor  # rapier-class: clamps to 1.0, unchanged
        assert core.coupling('point', armor, eff=1.0) == base, armor   # any eff>=ref clamps
        if base > 0:                                                   # scimitar-class: strictly discounted
            assert core.coupling('point', armor, eff=0.16) < base, armor
    # the scale is exactly the ratio, mirroring CUT_AUTH_REF
    assert abs(core.coupling('point', 'light', eff=0.26) - core.coupling('point', 'light') * (0.26/core.THRUST_AUTH_REF)) < 1e-9


def test_native_pointers_selection_unaffected():
    """Every native point-headed weapon selects the SAME head at every tier as it would with no magnitude scaling —
    the fix must not perturb a dedicated thruster (its point clamps to 1.0)."""
    for n, w in WEAPONS.items():
        if 'base' in w or w.get('head') != 'point':
            continue
        for ar in _TIERS:
            assert S.select_mode(Combatant('x', weapon=n), ar, False, CFG)[1] in (w['head'], 'blunt', 'point'), (n, ar)
    # concretely: the pure thrusters never leave 'point' off-Mordhau
    for n in ('rapier', 'spear', 'yari', 'bear_spear'):
        heads = {S.select_mode(Combatant('x', weapon=n), ar, False, CFG)[1] for ar in _TIERS}
        assert heads == {'point'}, (n, heads)


def test_slashers_no_spurious_point_switch():
    """The ED-PC-0012 target: the dedicated one-handed slashers (+ podao) no longer switch to a floor-locked 'point'
    vs armour — they select their own cut at EVERY tier."""
    for n in ('sabre', 'scimitar', 'falchion', 'podao'):
        heads = {S.select_mode(Combatant('x', weapon=n), ar, False, CFG)[1] for ar in _TIERS}
        assert 'point' not in heads, (n, heads)
        assert heads <= {'curved_cut', 'straight_cut', 'cut_thrust', 'blunt'}, (n, heads)


def test_voulge_affords_no_cut_token():
    """ED-PC-0012 flagged residual: voulge's rear thrusting-heel-spike carries edge_keenness=0.15, sitting EXACTLY on
    MODE_EDGE_MIN — only the strict '>' gate keeps it from affording a spurious 'cut'. Pin that it affords none."""
    assert 'cut' not in S.afforded_heads(WEAPONS['voulge'])
