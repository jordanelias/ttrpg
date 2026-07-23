"""Tradition-modulation surface for the morphology levers — U10 / ED-PC-0022.

audit/2026-07-04-weapon-morphology-granularity/u10_activation_v1.md.

The U9 capstone left the six U3/U5/U7 morphology levers wired but at K=0, and found no lever robustly moves
AGGREGATE field winrate. That finding is correct but incomplete: flat physics cancels in a mirror-ish field, and —
more to the point — the levers had NO tradition-modulation surface, so they were pure rote physics equal for every
fighter. U10 (a) re-homes the mis-parked choke-thrust cost (keeping the D2 force-invariant), (b) activates the
levers to small grounded baselines, and (c) — the substantive fix — routes each lever through
ability_primitives.ability_factor(c, <channel>) so a school that SPECIALIZES in a lever turns a situational
primitive into a decisive in-context edge (efficacy BEYOND rote physics).

These tests pin the SURFACE (every lever site reaches ability_factor; default 1.0 = inert-safe) and the correct
INSTRUMENT for a situational lever: the per-matchup specialist-vs-nonspecialist edge — NOT aggregate field winrate.
"""
import os
import random
import sys

import pytest

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)
pytest.importorskip("numpy")

import ability_primitives as ABIL  # noqa: E402
import combat_systems as S  # noqa: E402
import contact as CT  # noqa: E402
import tradition as TR  # noqa: E402
import wrapper as W  # noqa: E402
from combatant import Combatant  # noqa: E402
from config import CFG  # noqa: E402


def _duel_winshare(spec, plain, weapon, armor='medium', n=1200, seed0=99):
    """Position-swapped decisive win-share of a SPECIALIST (equipped ability) vs an identical PLAIN fighter of the
    same weapon/armour. >0.5 means the tradition ability confers a real edge."""
    aw = dec = 0
    for i in range(n):
        rng = random.Random(seed0 + i)
        swap = i >= n // 2
        A = Combatant('A', weapon=weapon, armor=armor, tradition=(plain[0] if swap else spec[0]), equipped=(plain[1] if swap else spec[1]))
        B = Combatant('B', weapon=weapon, armor=armor, tradition=(spec[0] if swap else plain[0]), equipped=(spec[1] if swap else plain[1]))
        r = W.fight(A, B, CFG, rng)
        if swap:
            r = -r
        if r == 1:
            aw += 1; dec += 1
        elif r == -1:
            dec += 1
    return aw / dec if dec else 0.5


def test_surface_exists_and_is_inert_by_default():
    """Every lever channel is reachable via ability_factor, and with NO ability equipped every channel is exactly 1.0
    (the levers stay pure physics until a tradition attaches) — so the surface is inert-safe."""
    plain = Combatant('x', weapon='arming')
    for ch in ('edge_read', 'spine_press', 'edge_grab', 'choke_control', 'facing_regime'):
        assert ABIL.ability_factor(plain, ch) == 1.0, ch


def test_every_new_ability_targets_a_live_channel():
    """The four U10 abilities each target one of the five morphology-lever channels (no typo'd/dead lever)."""
    live = {'edge_read', 'spine_press', 'edge_grab', 'choke_control', 'facing_regime'}
    for name in ('winden', 'zwerchhau', 'ringen_am_schwert', 'guardia'):
        assert ABIL.ABILITIES[name]['lever'] in live, name


def test_winden_spine_specialist_wins_the_mirror_duel():
    """The DECISIVE deliverable, on the correct instrument: a German bind-specialist (Winden) beats an IDENTICAL
    katana fighter with no such training — the single-edge spine-press it amplifies wins enough binds to tip the
    fight. Aggregate field winrate is the wrong instrument (the U9 finding); the specialist-vs-nonspecialist duel is
    the right one."""
    ws = _duel_winshare(('german', ['winden']), ('none', []), 'katana')
    assert ws > 0.51, f"Winden specialist should out-bind an identical plain katana (win-share {ws:.3f})"


def test_ringen_mitigates_the_grab_self_hazard():
    """Ringen am Schwert (the 'edge_grab' mitigator) lets a grappler seize a live double edge with less self-injury:
    grab_sigma vs an edged opponent is HIGHER (less negative) with Ringen equipped."""
    grabber = Combatant('A', weapon='dagger')
    grappler = Combatant('A', weapon='dagger', tradition='german', equipped=['ringen_am_schwert'])
    opp = Combatant('B', weapon='arming')                       # double-edged, grab_hazard 1.0
    assert CT.grab_sigma(grappler, opp, CFG) > CT.grab_sigma(grabber, opp, CFG)


def test_guardia_amplifies_facing_regime():
    """The Italian single-time profile (guardia) commits the facing regime harder — a larger facing_target for the
    same stance/grip/weapon."""
    plain = Combatant('a', weapon='sabre'); plain.grip_position = 0.5
    ital = Combatant('a', weapon='sabre', tradition='italian', equipped=['guardia']); ital.grip_position = 0.5
    assert abs(S.facing_target(ital, True, CFG)) > abs(S.facing_target(plain, True, CFG))


def test_ability_inert_when_weapon_lacks_the_feature():
    """A tradition ability modulates a PHYSICAL lever — it does nothing when the weapon has no such feature: Winden on
    a double-edged (spineless) arming sword adds no spine bind edge (spine==0)."""
    spineless = Combatant('A', weapon='arming', tradition='german', equipped=['winden'])
    spineless0 = Combatant('A', weapon='arming')
    defr = Combatant('B', weapon='longsword')
    assert S.bind_sigma(spineless, defr, CFG, TR) == S.bind_sigma(spineless0, defr, CFG, TR)
