"""CI-tier: commitment = recoverability (the physical commitment axis).

systems.recoverability_factor makes the overcommit cost scale with how hard an action is to terminate/retract —
the weapon's forward moment (mass**MOMENT_MASS_EXP * pob_frac, NON-LINEAR in weight). These tests pin the physics:
a hand-balanced rapier retracts (low multiplier — it can feint), a forward-heavy mace/poleaxe cannot (high
multiplier), longsword is the 1.0 reference, and the multiplier is floored so it never flips sign.
"""
import os
import sys

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'designs', 'scene', 'combat_engine_v1')
sys.path.insert(0, ENGINE)

import systems as S  # noqa: E402
from combatant import WEAPONS, Combatant  # noqa: E402
from config import CFG  # noqa: E402


def _r(name):
    return S.recoverability_factor(Combatant('x', weapon=name), CFG)


def test_recoverability_ordering_by_static_moment():
    """A hand-balanced light weapon retracts (low irrecoverability); a forward-heavy one can't (high)."""
    assert _r('rapier') < _r('longsword') < _r('mace') < _r('poleaxe')
    assert _r('dagger') < 1.0 and _r('greatsword') > 1.0


def test_longsword_is_the_reference():
    assert abs(_r('longsword') - 1.0) < 1e-9


def test_recoverability_is_floored():
    for n in WEAPONS:
        assert S.recoverability_factor(Combatant('x', weapon=n), CFG) >= 0.3


def test_moment_off_reproduces_flat():
    """EXPOSE_MOMENT_K=0 -> the multiplier is 1.0 everywhere (the pre-recoverability behaviour)."""
    cfg = dict(CFG); cfg['EXPOSE_MOMENT_K'] = 0.0
    for n in ('rapier', 'mace', 'poleaxe'):
        assert abs(S.recoverability_factor(Combatant('x', weapon=n), cfg) - 1.0) < 1e-9
