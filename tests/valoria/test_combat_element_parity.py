"""Element-model PARITY HARNESS — the Phase-A gate of the morphology re-architecture.

Locks the pre-rearchitecture derived statistics of every weapon so the located-part refactor cannot silently
drift them. The fixture (golden_element_parity.json) was generated at commit e725cc62 from values proven
byte-identical (1e-9) to the PRE-keystone engine (single-C_HEAD-lump derive): the keystone rewrote derive()
to a positional sum over located parts with a synthesized single reproduction element per weapon, and this
harness is the proof it stays identical while the Phase-A plumbing (bake extension, element-union
afforded_heads, sel_element threading) lands.

Covers, per weapon: the derive() mass family (PoB_m/PoB_frac/m_head/MoI/static_moment/length_m), the
downstream dynamics (agility, percussion_authority), the baked gap, the afforded_heads token->(eff, dmg_mode)
map, and select_mode across all four armour tiers.

LIFECYCLE: this harness must stay green through ALL of Phase A. When Phase B lands multi-element physical
per-part masses and the de-leak derivations (an INTENTIONAL balance move), the fixture is REGENERATED
deliberately with the change reasons recorded in the commit (plan Phase D discipline) — never patched
piecemeal to make a failure go away.
"""
import json
import os
import sys

import pytest

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)
sys.path.insert(0, os.path.join(ENGINE, '..', '..', '..', 'tests', 'sim', 'v32-combat-balance'))

GOLDEN = os.path.join(os.path.dirname(__file__), 'golden_element_parity.json')
TOL = 1e-9
DERIVE_KEYS = ('PoB_m', 'PoB_frac', 'm_head', 'MoI', 'static_moment', 'length_m')
TIERS = ('none', 'light', 'medium', 'heavy')


def _mods():
    pytest.importorskip("numpy")
    import combatant as C
    import combat_systems as S
    import weapon_physics as WP
    from config import CFG
    return C, S, WP, CFG


def _golden():
    with open(GOLDEN, encoding='utf-8') as f:
        return json.load(f)


def test_fixture_covers_full_roster():
    """Every weapon in the live dictionary is pinned; a new weapon must be added to the fixture DELIBERATELY."""
    C, S, WP, CFG = _mods()
    golden = _golden()
    assert set(golden) == set(C.WEAPONS), (
        f"fixture/roster drift — missing from fixture: {set(C.WEAPONS) - set(golden)}; "
        f"stale in fixture: {set(golden) - set(C.WEAPONS)}")


def test_derive_mass_family_parity():
    """The located-part derive() reproduces the pinned PoB/MoI/m_head/static_moment/length for every weapon."""
    C, S, WP, CFG = _mods()
    golden = _golden()
    for n, g in golden.items():
        d = WP.derive(C.WEAPONS[n])
        for k in DERIVE_KEYS:
            assert abs(d[k] - g[k]) <= TOL, f"{n}.{k}: {d[k]!r} != golden {g[k]!r}"


def test_downstream_dynamics_parity():
    """agility + percussion_authority (both read derive()) reproduce the pinned values."""
    C, S, WP, CFG = _mods()
    golden = _golden()
    for n, g in golden.items():
        w = C.WEAPONS[n]
        assert abs(WP.agility(w) - g['agility']) <= TOL, f"{n}.agility"
        assert abs(WP.percussion_authority(w) - g['perc_auth']) <= TOL, f"{n}.perc_auth"
        assert abs(w['gap'] - g['gap']) <= TOL, f"{n}.gap"


def test_afforded_heads_parity():
    """The afforded token set AND each token's (effectiveness, damage_mode) reproduce the pinned map."""
    C, S, WP, CFG = _mods()
    golden = _golden()
    for n, g in golden.items():
        af = S.afforded_heads(C.WEAPONS[n])
        assert set(af) == set(g['afforded']), f"{n}: afforded tokens {set(af)} != golden {set(g['afforded'])}"
        for tok, vals in af.items():                 # vals is the widened (eff, dm, gap, perc, pc, ref) tuple (I2/M2)
            eff, dm = vals[0], vals[1]
            geff, gdm = g['afforded'][tok]
            assert abs(eff - geff) <= 1e-6, f"{n}.{tok} effectiveness {eff} != {geff}"
            assert dm == gdm, f"{n}.{tok} damage_mode {dm} != {gdm}"


def test_select_mode_parity_all_tiers():
    """select_mode reproduces the pinned (damage_mode, head) at every armour tier (pure, rng-free)."""
    C, S, WP, CFG = _mods()
    golden = _golden()
    for n, g in golden.items():
        for tier in TIERS:
            got = list(S.select_mode(C.Combatant('x', weapon=n), tier, False, CFG))
            assert got == g['select_mode'][tier], (
                f"{n} vs {tier}: select_mode {got} != golden {g['select_mode'][tier]}")
