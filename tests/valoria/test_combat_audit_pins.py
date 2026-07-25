"""Regression pins for the defects found by the 2026-07-24 four-dimension read-only audit.

Every assertion here corresponds to a bug that ACTUALLY SHIPPED and was found by an auditor rather than by CI. The
audit's own adversarial review of the first remediation batch made the point sharply: the same gate had produced TWO
state-carryover bugs in two days (ED-PC-0033 grip_position, ED-PC-0034 sel_head) and nothing in the suite pinned
against a third. These are those pins.

Full account: audit/2026-07-24-combat-four-dimension-audit/ (index + infill). EDs: ED-PC-0034, ED-PC-0035.
"""
import os
import sys

import pytest

ENGINE = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                      'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)

import combat_systems as S  # noqa: E402
import contact as CT  # noqa: E402
import core  # noqa: E402
import tradition as TR  # noqa: E402
from combatant import WEAPONS, Combatant  # noqa: E402
from config import CFG  # noqa: E402

# Every field the wrapper writes onto a combatant per beat. The represent gate must be blind to ALL of them.
_CIRCUMSTANCE = ('sel_head', 'sel_gap', 'sel_perc', 'sel_pc', 'sel_eff', 'grip_position', 'range_avail', 'lunge_depth')


def _corrupt(c, armor):
    """Write a full set of CLOSED-phase circumstance onto `c`, exactly as a prior engagement's final beat would."""
    dm, head, gap, perc, pc, eff = S.select_mode(c, armor, True, CFG, measure_gap=0.0)
    c.sel_head, c.sel_gap, c.sel_perc, c.sel_pc, c.sel_eff = head, gap, perc, pc, eff
    c.grip_position, c.range_avail, c.lunge_depth = 1.0, 0.1, 1.0


@pytest.mark.parametrize('weapon', ['guisarme', 'katana', 'guandao', 'hook_sword', 'spear', 'yari',
                                    'poleaxe', 'partisan', 'ranseur', 'staff', 'longsword', 'estoc', 'odachi'])
@pytest.mark.parametrize('armor', ['medium', 'heavy'])
def test_represent_measure_p_is_path_independent(weapon, armor):
    """ED-PC-0034 (F1). The re-presentation gate is evaluated at ENGAGEMENT START, outside the per-beat loop that
    refreshes sel_*, so any read of live circumstance makes it depend on what the PRIOR engagement happened to leave
    behind — and on engagement 1, on the bare native head. Measured before the fix: a multi-mode weapon whose native
    head is a cutter read as maximally crowded on the first engagement and quite differently later (katana
    0.000 -> 0.274, guisarme 0.092 -> 0.236, hook_sword 0.000 -> 0.425) for the identical matchup.

    The gate must therefore be a pure function of (weapon, opponent armour, opening gap, stats) alone. This pins that:
    corrupting EVERY circumstance field the wrapper writes must not move it by one ulp."""
    a = Combatant('A', weapon=weapon, armor=armor)
    b = Combatant('B', weapon='arming', armor=armor)
    before = S.represent_measure_p(a, b, CFG, TR, measure_gap=1.67)
    _corrupt(a, armor)
    after = S.represent_measure_p(a, b, CFG, TR, measure_gap=1.67)
    assert before == pytest.approx(after, abs=1e-12), (
        f"{weapon}@{armor}: represent_measure_p is path-dependent ({before:.4f} -> {after:.4f} after a prior "
        f"engagement's closed-phase state) — the ED-PC-0033/0034 state-carryover bug class has returned")


def test_represent_gate_reads_the_point_not_the_cut():
    """ED-PC-0035 (adversarial review of batch 1). The gate's whole fiction is whether a closing opponent still
    RESPECTS THE POINT, so it must grade the mode the weapon would actually present at the opening measure. The first
    revision pinned room=1.0 — a geometry the engine never occupies here (its real beat-1 room is
    range_utilization(gap) ~ 0.48 at this gap) — which made select_mode grade the guisarme's BILL-CUT instead of its
    point and cost the matchup ~4pp. Pin the honest geometry."""
    a = Combatant('A', weapon='guisarme', armor='medium')
    room = S.range_utilization(a, 1.67, CFG)
    assert room < 1.0, "the opening room at a realistic gap must not be the counterfactual 1.0"
    head = S.select_mode(a, 'medium', False, CFG, measure_gap=1.67, grip=0.0, room=room)[1]
    assert head == 'point', f"the guisarme should present its POINT at open measure, not {head!r}"


@pytest.mark.parametrize('tradition', ['english', 'german', 'italian', 'spanish', 'japanese', 'none'])
@pytest.mark.parametrize('commit', [2.0, 2.5, 3.0, 4.0, 5.0])
def test_overcommit_exposure_never_negative(tradition, commit):
    """ED-PC-0034 (F2). `max(0.0, ...)` wrapped only the FIRST term, so a balanced/disciplined fighter at shallow
    commit returned a negative exposure (-0.37 measured). The wrapper guards its initiative/poise loss with `if > 0`
    but fed the un-floored value straight into RIPOSTE_ON_FAIL/ON_NEUTRALIZE, silently pushing the defender's riposte
    BELOW its configured base — a mechanic the docstring said could not exist. Not over-committing means you are not
    EXTRA exposed; it must never make you harder to riposte than the base contemplates."""
    for agi in (2, 3, 4, 5):
        for strength in (2, 4, 6):
            c = Combatant('X', weapon='arming', tradition=tradition)
            c.agi, c.strength = agi, strength
            assert S.overcommit_exposure(c, commit, 0.0, CFG, TR) >= 0.0


def test_grab_hazard_never_rewards_a_trained_grappler():
    """ED-PC-0034 (F3). Skills are documented uncapped ("positive = trained bonus"), so `(1 - skill('grab'))` went
    NEGATIVE past 1.0 and flipped the term's sign: seizing an opponent's LIVE double edge bare-handed then IMPROVED
    the grab, scaling with how sharp the grabbed blade is. A trained grappler may become immune to the hazard; they
    must never be rewarded by it. Pinned as monotone-non-decreasing in skill, then flat."""
    a, b = Combatant('A', weapon='dagger'), Combatant('B', weapon='flamberge')  # live-edge opponent
    vals = []
    for sk in (0.0, 0.25, 0.5, 0.75, 1.0, 1.5, 3.0, 10.0):
        a.skills = {'grab': sk}
        vals.append(CT.grab_sigma(a, b, CFG))
    assert all(y >= x - 1e-12 for x, y in zip(vals, vals[1:])), f"grab_sigma not monotone in grab skill: {vals}"
    assert vals[-1] == pytest.approx(vals[4], abs=1e-12), "the hazard must CLAMP at skill 1, not keep paying out"


@pytest.mark.parametrize('lever,weapons', [
    ('LEGIB_EDGELINE_K', ('katana', 'arming')),
    ('BIND_SPINE_K', ('flamberge', 'katana')),
    ('GRAB_EDGE_K', ('dagger', 'flamberge')),
    ('CHOKE_ACCURACY_K', ('poleaxe', 'longsword')),
    ('FACING_REGIME_K', ('longsword', 'arming')),
])
def test_each_morphology_lever_is_individually_live(lever, weapons):
    """ED-PC-0035 (adversarial review of batch 1). `test_levers_add_texture_without_shifting_balance` measures the
    UNION of the five morphology levers, and the review proved that union can pass while four of the five are dead:
    with only LEGIB_EDGELINE_K alive the metric still read ~10% (over the 5% floor), whereas BIND_SPINE_K alone read
    0.5%, CHOKE_ACCURACY_K 0%, FACING_REGIME_K 0-0.5%, GRAB_EDGE_K 2-2.5%. The pinned matchups structurally cannot
    excite bind/choke/facing at all.

    So liveness is pinned HERE, per-lever and at the MECHANISM level, in a matchup chosen to excite that lever: zeroing
    the constant must change the quantity it feeds. That catches "a lever went dead" precisely — which is the property
    the fight-level union metric cannot see — without demanding fight-outcome divergence a small lever should not
    have."""
    wa, wb = weapons
    a, b = Combatant('A', weapon=wa), Combatant('B', weapon=wb)
    for c, opp in ((a, b), (b, a)):
        dm, head, gap, perc, pc, eff = S.select_mode(c, opp.armor, True, CFG, measure_gap=0.0)
        c.sel_dmg, c.sel_head, c.sel_gap, c.sel_perc, c.sel_pc, c.sel_eff = dm, head, gap, perc, pc, eff
        c.grip_position = 1.0 if lever == 'CHOKE_ACCURACY_K' else 0.0
    off = dict(CFG, **{lever: 0.0})

    if lever in ('LEGIB_EDGELINE_K', 'CHOKE_ACCURACY_K'):
        on_v, off_v = S.legibility(a, 4.0, CFG), S.legibility(a, 4.0, off)
    elif lever == 'BIND_SPINE_K':
        on_v, off_v = S.bind_sigma(a, b, CFG, TR), S.bind_sigma(a, b, off, TR)
    elif lever == 'GRAB_EDGE_K':
        on_v, off_v = CT.grab_sigma(a, b, CFG), CT.grab_sigma(a, b, off)
    else:  # FACING_REGIME_K
        on_v, off_v = S.facing_target(a, True, CFG), S.facing_target(a, True, off)

    assert on_v != pytest.approx(off_v, abs=1e-12), (
        f"{lever} is DEAD: zeroing it does not change the quantity it feeds ({wa} vs {wb}). "
        f"on={on_v!r} off={off_v!r}")


@pytest.mark.parametrize('weapon', [n for n, r in WEAPONS.items() if r.get('head') == 'cut_thrust'])
@pytest.mark.parametrize('armor', ['none', 'light', 'medium', 'heavy'])
def test_cut_thrust_label_matches_the_arm_actually_paid(weapon, armor):
    """ED-PC-0035 (F12). `coupling` resolves a cut-and-thrust weapon as max(cut arm, half-sword thrust arm), and
    `select_mode` reports the damage-mode that legibility scores (thrust reads HARD 0.80, swing EASY 1.25). Those two
    were decided INDEPENDENTLY and contradicted each other: the thrust arm won at every tier — the pre-max blended
    DELIVERY['cut_thrust']=1.35 could never beat point's 1.45, since shear-resist >= puncture-resist everywhere — so a
    sword was damaged as a thrust while being read as a swing, and the advertised "versatile max" never once selected
    the edge across 76 weapon x tier cells.

    Both now come from core.cut_thrust_arm, their single owner. This pins that they agree for every cut_thrust weapon
    at every tier — the property, not the values, so a future re-grading of DELIVERY/RESIST stays free to move which
    arm wins as long as the label follows it."""
    c = Combatant('X', weapon=weapon)
    dm, head, gap, perc, pc, eff = S.select_mode(c, armor, True, CFG, measure_gap=0.0)
    if head != 'cut_thrust':
        pytest.skip(f"{weapon} selects {head!r} at {armor}, not the versatile head")
    _value, mode = core.cut_thrust_arm(core.TIER2MAT[armor], 'full', gap, eff,
                                       core.thrust_authority(c.w['head_len']))
    assert dm == mode, (f"{weapon}@{armor}: select_mode reports {dm!r} but coupling pays the {mode!r} arm — "
                        f"the damage path and the read contest disagree about what the fighter did")


def test_cut_thrust_versatility_is_not_decided_by_constant_ordering():
    """ED-PC-0035 (F12). The whole point of the versatile head is an ARMOUR-CONDITIONAL shift. If one arm wins in every
    cell, the max() is decorative and the shift is a constant ordering wearing physics' clothes — which is exactly what
    the audit found. Pin that BOTH arms win somewhere across the tier range for a well-edged sword."""
    c = Combatant('X', weapon='arming')
    modes = set()
    for armor in ('none', 'light', 'medium', 'heavy'):
        dm, head, gap, perc, pc, eff = S.select_mode(c, armor, True, CFG, measure_gap=0.0)
        modes.add(core.cut_thrust_arm(core.TIER2MAT[armor], 'full', gap, eff,
                                      core.thrust_authority(c.w['head_len']))[1])
    assert modes == {'shear', 'puncture'}, (
        f"the cut/thrust contest resolved to {modes} across all four armour tiers — one arm is structurally dead")


def test_cut_thrust_coupling_respects_weapon_quality():
    """ED-PC-0035 (F12). The versatile branch IGNORED its `eff` argument, so coupling('cut_thrust', ...) returned an
    identical value whether the weapon's derived edge/point quality was 0.1 or 0.9 — silently discarding the graded
    quality of all 19 cut_thrust weapons (sel_eff spans 0.63-1.14) and making near-identical swords read identically."""
    poor = core.coupling('cut_thrust', 'none', eff=0.1)
    good = core.coupling('cut_thrust', 'none', eff=0.9)
    assert poor < good, f"weapon quality is inert on the cut_thrust path (eff 0.1 -> {poor}, eff 0.9 -> {good})"
