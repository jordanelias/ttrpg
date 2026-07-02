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

import pytest  # noqa: E402
pytest.importorskip("numpy")  # engine import chain needs numpy + the sim modules; skip in the lightweight validator job

import systems as S  # noqa: E402
from combatant import WEAPONS, Combatant  # noqa: E402
from config import CFG  # noqa: E402


def _r(name):
    return S.recoverability_factor(Combatant('x', weapon=name), CFG)


def test_recoverability_ordering_by_static_moment():
    """A hand-balanced light weapon retracts (low irrecoverability); a forward-heavy one can't (high)."""
    assert _r('rapier') < _r('longsword') < _r('mace') < _r('poleaxe')
    assert _r('dagger') < 1.0 and _r('greatsword') > 1.0


def test_anchor_is_near_one():
    """The 2H cut-thrust anchor (a ~1.4kg longsword-class blade) sets the scale -> recoverability ~1.0. The refs
    (REC_I_REF/REC_S_REF) are rounded [SIM-CALIBRATE] constants, so it is ~1.0, not exactly 1.0.
    [PHASE-C FLAG, 2026-07-02] morphology-rearch Phase B's real per-part longsword MoI (grip/pommel/guard at
    their true measured positions, not the old formula's residual-lump) reads meaningfully higher than the
    Phase-A reproduction, pushing this anchor to ~1.29. The ordering test above (still green) shows the STRUCTURE
    survives; REC_I_REF/REC_S_REF need Phase C's balance-harness re-tune against the now-grounded MoI, not a
    per-weapon mass fudge."""
    assert abs(_r('longsword') - 1.0) < 0.03


def test_recoverability_is_floored():
    for n in WEAPONS:
        assert S.recoverability_factor(Combatant('x', weapon=n), CFG) >= 0.3


def test_gathering_a_pole_lowers_irrecoverability():
    """Grip-aware (Phase-3 Stage 2): a tipped pole that GATHERS IN (grip_position 0->1) slides toward its working
    balance, dropping the forward static moment -> more recoverable. The spear gathered to balance retracts freely."""
    s = Combatant('x', weapon='spear')
    open_grip = S.recoverability_factor(s, CFG)          # grip_position 0 (butt-grip, committed reach)
    s.grip_position = 1.0
    assert S.recoverability_factor(s, CFG) < open_grip   # gathered to balance: far more recoverable


def test_lunge_raises_irrecoverability():
    """The body-extension (lunge) axis — the best-grounded leg (Silver true-times) — raises irrecoverability."""
    c = Combatant('x', weapon='longsword')
    base = S.recoverability_factor(c, CFG)
    c.lunge_depth = 1.0
    assert S.recoverability_factor(c, CFG) > base
