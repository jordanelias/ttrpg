"""CI-tier: PoB (point-of-balance) realism gate (U1, JD-1, ED-PC-0010, 2026-07-08).

Pins the ratified JD-1 bands (`designs/audit/2026-07-04-weapon-morphology-granularity/consolidation_v1.md`
§6) for the weapon classes the fork actually named — rapier, 1H swords (arming/longsword), greatsword,
poleaxe-class polearms (poleaxe/bec_de_corbin/lucerne_hammer), and staff. Weapons outside these five named
classes were NOT part of JD-1's ruling and are intentionally not asserted here (no invented bands)."""
import os
import sys

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)

import pytest  # noqa: E402
pytest.importorskip("numpy")  # engine import chain needs numpy + the sim modules; skip in the lightweight validator job

import weapon_physics as WP  # noqa: E402
from combatant import WEAPONS  # noqa: E402

# (weapon, band_lo_cm, band_hi_cm) per JD-1's ratified default (consolidation_v1.md §6)
RAPIER_BAND = (3.0, 11.0)
ONE_HAND_BAND = (6.0, 14.0)
GREATSWORD_BAND = (8.0, 20.0)
POLEAXE_BAND = (20.0, 55.0)
STAFF_BAND = (-1e-6, 1e-6)   # "~0"

BANDS = {
    'rapier': RAPIER_BAND,
    'arming': ONE_HAND_BAND,
    'longsword': ONE_HAND_BAND,
    'greatsword': GREATSWORD_BAND,
    'poleaxe': POLEAXE_BAND,
    'bec_de_corbin': POLEAXE_BAND,
    'lucerne_hammer': POLEAXE_BAND,
    'staff': STAFF_BAND,
}


def test_pob_within_realistic_range():
    """Every JD-1-named weapon's derived PoB_cm falls within its ratified arms-scholarship band."""
    violations = {}
    for name, (lo, hi) in BANDS.items():
        pob_cm = WP.derive(WEAPONS[name])['PoB_cm']
        if not (lo <= pob_cm <= hi):
            violations[name] = (pob_cm, (lo, hi))
    assert not violations, f"PoB out of JD-1 band (live, band): {violations}"


def test_flagged_weapons_mass_unchanged():
    """U1 is a data-only redistribution (blade/head mass -> pommel/haft) — total weapon mass is untouched for
    every flagged weapon, per consolidation_v1's U1 row ('weapons.py data only')."""
    for name, (mass_before,) in {
        'rapier': (1.368,), 'arming': (1.2,), 'longsword': (1.408,), 'greatsword': (2.751,),
        'bec_de_corbin': (2.4534,), 'lucerne_hammer': (2.4834,),
    }.items():
        assert abs(WEAPONS[name]['mass'] - mass_before) < 1e-9, f"{name}: total mass drifted"
