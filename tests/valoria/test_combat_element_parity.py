"""Element-model PARITY HARNESS — the Phase-A gate of the morphology re-architecture.

Locks the derived statistics of every weapon so a refactor cannot silently drift them. The fixture
(golden_element_parity.json) was ORIGINALLY generated at commit e725cc62 from values proven byte-identical
(1e-9) to the PRE-keystone engine (single-C_HEAD-lump derive): the keystone rewrote derive() to a positional
sum over located parts with a synthesized single reproduction element per weapon, and this harness was the
proof it stayed identical while the Phase-A plumbing (bake extension, element-union afforded_heads,
sel_element threading) landed.

PROVENANCE, CURRENT: the fixture was last regenerated at base commit f03357d for **E2b / M9 / ED-PC-0048
(2026-07-29)** — `percussion_element_authority`'s lever moved from `abs(elem_x)/Lt` (exactly 0 for any element
mounted AT the working hand) to the same `weapon_physics.strike_point_lever` E2a shipped, called with the
DELIVERED mass so it reduces to the geometric `(STRIKE_HAND_LEVER + |x|)/(STRIKE_HAND_LEVER + Lt)`. Moved:
`afforded['blunt']` effectiveness on the 3 located-blunt-element weapons (poleaxe 7.6131→7.7689, bec_de_corbin
6.5099→6.7760, lucerne_hammer 7.0549→7.3124) and the 9 two-handed blades reaching `reversed_grip_percussion`
(longsword +8.8% … changdao +2.6%), all upward, all from the hand-floor that IS the repair.
**Unlike E2a, this batch DOES move affordance token sets and selection**, deliberately and minimally:
`hook_sword` gains the `blunt` token its record has always authored (the defect — the crescent was dead data),
and exactly two weapons change a `select_mode` (damage_mode, head) pair — `hook_sword` at light/medium/heavy
(→ percussion/blunt, keeping native curved_cut unarmoured) and `bec_de_corbin` at heavy (puncture/point →
percussion/blunt, rejoining its sibling lucerne_hammer, which already struck blunt at medium and heavy).

PRIOR: regenerated at base commit 8ab21b3 for **E2a / M1 / ED-PC-0047** — percussion_authority's lever moved
from the whole-weapon CoM offset (`PoB_frac`, which a rear counterweight could cancel to exactly zero) to
`weapon_physics.strike_point_lever`, moving `perc_auth` on the four blunt-native weapons whose forward moment
differs from their centre of balance (staff 0.0→5.6290, poleaxe 7.4843→8.0, bec_de_corbin 6.3629→7.4872,
lucerne_hammer 6.5392→7.5897); no weapon changed which mode it selects in that batch.

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

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)

GOLDEN = os.path.join(os.path.dirname(__file__), 'golden_element_parity.json')
TOL = 1e-9
DERIVE_KEYS = ('PoB_m', 'PoB_frac', 'm_head', 'MoI', 'static_moment', 'length_m')
TIERS = ('none', 'light', 'medium', 'heavy')


def _mods():
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
