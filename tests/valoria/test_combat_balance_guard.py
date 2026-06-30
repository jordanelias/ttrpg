"""Behavioral regression guards for the scene-combat engine (the guard the Gate-1 audit found missing).

The state-graph tests check the graph SHAPE; these check the engine's load-bearing BEHAVIORAL invariants —
the ones a refactor (e.g. the Phase-2/3 wrapper de-leak) must preserve, and whose absence let an incomplete
de-leak land unnoticed:

  · DETERMINISM — same seed + same setup -> identical outcome (guards rng-order / wrapper purity: a de-leak that
    reorders an rng draw or leaks state breaks this).
  · MIRROR FAIRNESS — identical fighters resolve ~50/50 (guards the A/B role-symmetry the wrapper's fixed-object
    identity design exists to protect; the recurring role-inversion bug class shows up here as a skewed mirror).

These are SEEDED, so they are deterministic (never flaky) yet still fail loudly if behavior or symmetry drifts.
A deliberate re-baseline updates the bands with a recorded reason; an accidental regression trips them.
"""
import os
import sys

import pytest

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'designs', 'scene', 'combat_engine_v1')
sys.path.insert(0, ENGINE)
sys.path.insert(0, os.path.join(ENGINE, 'tests', 'sim', 'v32-combat-balance'))


def _engine():
    pytest.importorskip("numpy")  # the engine resolves via r8 -> numpy; skip cleanly where numpy is absent
    import numpy as np
    import combatant as C
    import wrapper as W
    from config import CFG
    return np, C, W, CFG


@pytest.mark.parametrize("wa,wb,armor,trad", [
    ('longsword', 'spear', 'medium', 'german'),
    ('arming', 'arming', 'light', 'none'),
    ('mace', 'rapier', 'heavy', 'italian'),
])
def test_seeded_determinism(wa, wb, armor, trad):
    """Same seed + same setup -> byte-identical outcome sequence. A wrapper that leaks state across fights or
    reorders an rng draw (the failure mode an incomplete de-leak risks) breaks this."""
    np, C, W, CFG = _engine()

    def run():
        rng = np.random.default_rng(20260630)
        out = []
        for _ in range(60):
            a = C.Combatant('A', weapon=wa, armor=armor, tradition=trad)
            b = C.Combatant('B', weapon=wb, armor=armor, tradition='none')
            out.append(W.fight(a, b, CFG, rng))
        return out

    assert run() == run()


@pytest.mark.parametrize("weapon", ['arming', 'longsword', 'spear', 'mace', 'dagger'])
def test_mirror_fairness(weapon):
    """Identical fighters (same stats, weapon, armour, tradition) must resolve close to 50/50. The wrapper assigns
    aggressor/defender per beat over fixed A/B objects precisely so neither label is privileged; a leak that ties a
    mechanic to raw A/B shows up as a skewed mirror. Seeded -> deterministic. Band [0.40, 0.60] is generous around
    the observed ~0.45-0.55 spread so only a real asymmetry (not noise) trips it."""
    np, C, W, CFG = _engine()
    rng = np.random.default_rng(424242)
    n = 300
    a_wins = 0
    for _ in range(n):
        a = C.Combatant('A', weapon=weapon, armor='light')
        b = C.Combatant('B', weapon=weapon, armor='light')
        if W.fight(a, b, CFG, rng) == 1:
            a_wins += 1
    rate = a_wins / n
    assert 0.40 <= rate <= 0.60, f"mirror {weapon} A-winrate {rate:.3f} outside [0.40,0.60] — role-symmetry break?"
