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
import random
import sys

import pytest

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'designs', 'scene', 'combat_engine_v1')
sys.path.insert(0, ENGINE)


class _Rng:
    """Engine rng factory — the contract is a stdlib random.Random since the ED-1085 numpy
    de-leak (core resolves through engine.autoload.sigma_leverage; rng.gauss/betavariate/randrange).
    Wrapped so a future substrate change is a one-line re-point here, and bands re-baseline
    with a recorded reason per the module docstring."""
    default_rng = staticmethod(lambda seed: random.Random(seed))


def _engine():
    import combatant as C
    import wrapper as W
    from config import CFG
    return _Rng, C, W, CFG


@pytest.mark.parametrize("wa,wb,armor,trad", [
    ('longsword', 'spear', 'medium', 'german'),
    ('arming', 'arming', 'light', 'none'),
    ('mace', 'rapier', 'heavy', 'italian'),
])
def test_seeded_determinism(wa, wb, armor, trad):
    """Same seed + same setup -> byte-identical outcome sequence. A wrapper that leaks state across fights or
    reorders an rng draw (the failure mode an incomplete de-leak risks) breaks this."""
    np, C, W, CFG = _engine()   # np is the rng factory shim (stdlib contract, ED-1085)

    def run():
        rng = np.default_rng(20260630)
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
    np, C, W, CFG = _engine()   # np is the rng factory shim (stdlib contract, ED-1085)
    rng = np.default_rng(424242)
    n = 300
    a_wins = 0
    for _ in range(n):
        a = C.Combatant('A', weapon=weapon, armor='light')
        b = C.Combatant('B', weapon=weapon, armor='light')
        if W.fight(a, b, CFG, rng) == 1:
            a_wins += 1
    rate = a_wins / n
    assert 0.40 <= rate <= 0.60, f"mirror {weapon} A-winrate {rate:.3f} outside [0.40,0.60] — role-symmetry break?"


@pytest.mark.parametrize("weapon", ['dagger', 'spear', 'poleaxe', 'longsword', 'mace', 'arming'])
def test_heavy_mirror_fair_and_decisive(weapon):
    """HEAVY-armour mirror — symmetry AND non-degeneracy. The Gate-1 audit + the gap game (2026-06-30) exposed a latent
    artifact the light-only `test_mirror_fairness` never covered: pre-gap-game, pure-thrust weapons vs plate produced
    ~65-80% DRAWS (no mode could defeat the harness), so the tiny decided population was first-mover-dominated and a
    naive mirror read far from 50. This guards BOTH: (a) win-share among decided fights ~50/50 (role-symmetry), and
    (b) the DECIDED fraction stays healthy (>=0.40) — a regression that re-breaks armour-defeat (every mode failing vs
    plate -> draw-stalemate) trips (b). Seeded -> deterministic. Current engine decides ~0.98-1.00; the old broken
    state was ~0.17-0.35 — the 0.40 floor sits robustly between."""
    np, C, W, CFG = _engine()   # np is the rng factory shim (stdlib contract, ED-1085)
    rng = np.default_rng(20260630)
    n = 300
    a_wins = decided = 0
    for _ in range(n):
        a = C.Combatant('A', weapon=weapon, armor='heavy')
        b = C.Combatant('B', weapon=weapon, armor='heavy')
        r = W.fight(a, b, CFG, rng)
        if r != 0:
            decided += 1
            a_wins += (r == 1)
    frac_decided = decided / n
    win_share = a_wins / decided if decided else 0.5
    assert frac_decided >= 0.40, (
        f"heavy mirror {weapon}: only {frac_decided:.2f} decided — draw-stalemate (armour-defeat broken vs plate?)")
    assert 0.38 <= win_share <= 0.62, (
        f"heavy mirror {weapon} A win-share {win_share:.3f} outside [0.38,0.62] — role-symmetry break?")
