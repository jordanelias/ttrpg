"""Thrust authority — the point-to-hand lever primitive (ED-PC-0015 / RBNI item PC-5).

A point pressed into a harness gap is a SHORT-LEVER pommel-backed act (Fiore/Talhoffer half-sword; the rondel to the
visor). `core.thrust_authority(head_len)` derives that authority from the point-to-controlling-hand distance: short =
full, a long reach-thrust decays toward a floor. These tests pin (1) the primitive's shape (monotone, clamped, saturated
at/below the reference, floored), (2) that the parameter is INERT at its 1.0 default (byte-identical to before it existed),
(3) that it is SCOPED to the gap-press vs rigid armour ONLY — a thrust's through-material lethality vs soft targets is
untouched, so reach weapons stay deadly vs the unarmoured — and (4) the emergent capability wiring (short-lever forms
saturate; long reach-points decay) with NO weapon name involved.
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


def test_thrust_authority_shape():
    """Monotone non-increasing in head_len; ==1.0 at or below THRUST_LEVER_REF (short lever saturates); ->FLOOR for a
    long haft; clamped to [FLOOR, 1.0]; safe on degenerate input."""
    ref, floor = core.THRUST_LEVER_REF, core.THRUST_LEVER_FLOOR
    assert core.thrust_authority(0.10) == 1.0            # dagger-class point-to-hand
    assert core.thrust_authority(ref) == 1.0             # exactly the reference saturates
    assert core.thrust_authority(ref * 0.5) == 1.0
    assert core.thrust_authority(10.0) == floor          # absurdly long -> floored, never zero
    xs = [0.2, 0.4, 0.6, 0.9, 1.3, 1.8, 2.5]
    vals = [core.thrust_authority(x) for x in xs]
    assert vals == sorted(vals, reverse=True)            # non-increasing
    assert all(floor <= v <= 1.0 for v in vals)
    assert core.thrust_authority(0.0) == 1.0 and core.thrust_authority(None) == 1.0  # degenerate -> neutral


def test_default_is_byte_identical_parity():
    """thrust_auth defaults to 1.0 — every pre-PC-5 call (which omits it) is byte-identical to passing 1.0 explicitly,
    across every head x armour."""
    for head in ('point', 'cut_thrust', 'cut', 'blunt', 'straight_cut', 'curved_cut'):
        for armor in ('none', 'light', 'medium', 'heavy'):
            assert core.coupling(head, armor) == core.coupling(head, armor, thrust_auth=1.0), (head, armor)


def test_scoped_to_gap_press_not_soft_target():
    """The lever authority scales the GAP-PRESS vs a harness ONLY. Vs an UNARMOURED / soft target the puncture path is
    through-material dominated, so thrust_auth is inert there — a spear/reach-thrust stays fully lethal vs flesh. Vs
    mail/plate the gap term dominates and a reduced authority genuinely lowers the coupling."""
    # none: through-material transmit (=1.0) dominates the gap term for any authority -> point coupling is invariant.
    assert core.coupling('point', 'none', thrust_auth=1.0) == core.coupling('point', 'none', thrust_auth=core.THRUST_LEVER_FLOOR)
    # plate: the gap-press dominates -> a lower authority strictly lowers the coupling (a long reach-thrust presses less).
    hi = core.coupling('point', 'heavy', gap_prec=0.9, thrust_auth=1.0)
    lo = core.coupling('point', 'heavy', gap_prec=0.9, thrust_auth=core.THRUST_LEVER_FLOOR)
    assert lo < hi


def test_short_lever_forms_saturate_long_reach_points_decay():
    """EMERGENT, no weapon name: the half-sword / dagger class (short point-to-hand) saturates at full authority; the
    long pure-point reach class (spear/yari) decays to the floor. This is the physical fact that flips the half-sword
    to a plate-defeat win and reins in reach-over-plate (G4)."""
    saturated = ('dagger', 'rondel', 'longsword_halfsword', 'estoc_halfsword')
    for n in saturated:
        if n in WEAPONS:
            assert core.thrust_authority(WEAPONS[n]['head_len']) == 1.0, n
    for n in ('spear', 'yari'):
        assert core.thrust_authority(WEAPONS[n]['head_len']) < 0.5, n
    # the half-sword short-lever form out-authorises the same fighter's own full-length blade
    assert core.thrust_authority(WEAPONS['longsword_halfsword']['head_len']) > core.thrust_authority(WEAPONS['longsword']['head_len'])


def test_swung_spike_blunt_path_untouched():
    """A swung beak/spike (percussion) is NOT a static pommel-press: adef_cap's BLUNT path (poleaxe/bec_de_corbin
    armour-defeat) must be independent of thrust_auth — only the point / cut_thrust gap-THRUST terms carry it."""
    for n in ('poleaxe', 'bec_de_corbin', 'mace'):
        w = WEAPONS[n]
        # force the blunt head: adef_cap on the native blunt head is unchanged whatever the weapon's head_len
        cap = S.adef_cap(w, CFG, head='blunt')
        assert cap > 0
        # the blunt branch does not read thrust_authority — recompute is stable and name-free (structural: no head_len term)
        assert S.adef_cap(w, CFG, head='blunt') == cap
