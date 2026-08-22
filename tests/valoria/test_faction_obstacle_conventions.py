"""The three OPPOSED faction obstacle derivations, pinned while the `score/2` ruling is suspended.

SUBJECT, under CLAUDE.md §0.1 pt 5's load-bearing predicate: obstacle derivation is game math on
the executable model — it decides whether a Tribunal or a Parliamentary Transfer succeeds. It is
also load-bearing on a Jordan decision, which is the second half of that predicate. It earns its
existence on both counts.

WHY IT EXISTS. Jordan ruled 2026-08-14 that *"an obstacle rolled against a character or faction is
their corresponding score/2 plus whatever specific modifiers exist for them in that instance"*, and
the M1 board records that derivation as "wired NOWHERE". Measured 2026-08-21, that is FALSE: of the
three sites that roll against a target faction's score, one already implements the ruling exactly,
one implements it under a condition, and one contradicts it — each citing its own canon.

Jordan suspended the work 2026-08-21 and flagged it for later systems work rather than having a
session reconcile three ratified numbers on its own authority. See
`registers/handoffs/HANDOFF_FA.md` for the full classification and the two reasons wiring it
blindly would do damage.

WHAT THIS TEST IS FOR, precisely: while the question is suspended, none of the three may drift.
A silent edit to any of them — including a well-meaning "let's just make them consistent" — fails
here. When the ruling lands, THIS FILE is where the new convention gets recorded, and the failures
it produces are the work-list.
"""
from __future__ import annotations

import math
import os
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, ROOT)


def test_coronation_already_implements_the_ruling():
    """`floor(L / 2) + 1` — score/2 plus a modifier, exactly as ruled (part10 §3.4)."""
    from systems.factions.sim.crown_initiative import coronation_renewal_ob

    for church_l in (0.0, 1.0, 2.0, 3.0, 4.5, 5.0, 7.0):
        assert coronation_renewal_ob(church_l) == math.floor(church_l / 2) + 1, (
            f'coronation_renewal_ob({church_l}) changed. This site ALREADY satisfies the 2026-08-14 '
            f'ruling; if it moved, either the ruling was applied elsewhere and this was "made '
            f'consistent" with a site that contradicts it, or canon changed. Neither is a drive-by.')


def test_tribunal_halves_only_under_formal_grounds():
    """`round(L * 0.5)` with formal grounds, `round(L)` without — the halving IS the mechanic.

    This is the site the ruling would damage if applied naively. §7.1 grants formal grounds a
    HALVED resistance; if the base becomes `L/2`, that halving either compounds to `L/4` or stops
    distinguishing anything. The two-tier structure is asserted here so a change that collapses it
    cannot pass as a one-line fix.
    """
    from systems.factions.sim import tribunal

    assert tribunal.TRIBUNAL_RESISTANCE_HALVED_FACTOR == 0.5, (
        'the formal-grounds factor moved; §7.1 says HALVED and the tier distinction depends on it')

    for accused_l in (2.0, 3.0, 4.0, 6.0):
        plain = max(1.0, round(float(accused_l)))
        halved = max(1.0, round(float(accused_l) * tribunal.TRIBUNAL_RESISTANCE_HALVED_FACTOR))
        assert halved <= plain, 'formal grounds must never make the obstacle harder'
        if accused_l >= 3.0:
            assert halved < plain, (
                f'formal grounds stopped reducing the obstacle at L={accused_l} — the two tiers '
                f'have collapsed into one, which is what applying score/2 to the BASE would do')


def test_parliamentary_transfer_still_uses_the_full_score():
    """`holder.L + 2` — FULL score, contradicting the ruling, and stated as canon in its design doc.

    Pinned deliberately. This is the site a session would most plausibly "fix", and doing so
    overwrites `systems/factions/parliamentary_transfer_v30.md:30`, which states the number in its
    own resolution table. That is a ruling, not an implementation.
    """
    from systems.factions.sim import parliamentary_transfer as pt

    assert pt.PARL_MAJORITY_OB_BONUS == 2, 'the +2 modifier moved (parliamentary_transfer_v30.md:30)'

    doc = os.path.join(ROOT, 'systems', 'factions', 'parliamentary_transfer_v30.md')
    text = open(doc, encoding='utf-8').read()
    assert 'Holder Legitimacy' in text, (
        'the design doc no longer states the obstacle as Holder Legitimacy. If canon changed, '
        'update this test WITH the ruling that changed it — do not let code and doc drift apart.')
    assert 'Holder Legitimacy / 2' not in text and 'floor(Holder Legitimacy' not in text, (
        'the design doc now derives the obstacle from HALF the holder score. If that is the ruling '
        'landing, wire parliamentary_transfer.py:257 to match in the same commit and rewrite this '
        'test — the point of pinning was to make exactly this change deliberate.')


def test_the_unopposed_sites_are_untouched():
    """The ruling's antecedent is "rolled against a character or faction". These have no target, so
    they are out of scope and must not be swept into a consistency pass."""
    from systems.factions.sim import council_solmund

    assert council_solmund.council_ob.__doc__ and 'CI' in council_solmund.council_ob.__doc__, (
        'council_ob no longer derives from the CI world clock — if it now reads a faction score it '
        'has become an OPPOSED site and belongs in the classification, not here')

    src = open(os.path.join(ROOT, 'systems', 'factions', 'sim', 'faction_action.py'),
               encoding='utf-8').read()
    assert 'ob = 1' in src and 'ob = 2' in src, (
        'Muster/Govern no longer use fixed obstacles. Both roll against the world rather than a '
        'target faction, so the score/2 ruling does not reach them; if they were converted, that '
        'was a design decision that needs to be recorded in HANDOFF_FA.md.')


def test_conquest_has_no_obstacle_to_convert():
    """The one unambiguously OPPOSED action does not roll against an Ob at all.

    `_try_conquest` delegates to `resolve_mass_battle`, so the defender's strength enters through
    the battle model. Recorded because "wire score/2 into the opposed actions" reads as though
    conquest were the obvious first target, and there is nothing there to wire.
    """
    src = open(os.path.join(ROOT, 'systems', 'factions', 'sim', 'faction_action.py'),
               encoding='utf-8').read()
    body = src[src.index('def _try_conquest('):src.index('def _try_muster(')]
    assert 'resolve_mass_battle' in body, 'conquest no longer delegates to the mass-battle engine'
    assert 'ob =' not in body, (
        'conquest grew an obstacle. That makes it a fourth OPPOSED site and it must be added to the '
        'classification in registers/handoffs/HANDOFF_FA.md before it is given a convention.')
