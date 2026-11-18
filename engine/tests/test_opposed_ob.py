"""
engine/tests/test_opposed_ob.py -- the pool rule, the opposition and the even line
(`engine.dice_engine.sigma_leverage.pool_of`, `opposed_ob`, `even_line`).

Pure functions, no caller yet. The operand of `opposed_ob` is a skill score, never a pool.
"""
from __future__ import annotations

import os
import sys

import pytest

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from engine.dice_engine import dice_engine  # noqa: E402
from engine.dice_engine import sigma_leverage as SL  # noqa: E402


def test_opposed_ob_at_half_is_score_over_two_exactly():
    checked = 0
    for k in range(0, 41):                 # scores 0 to 20 in halves
        score = k / 2
        assert SL.opposed_ob(score, 0.5) == score / 2   # exact: no approx
        checked += 1
    assert checked == 41


def test_opposed_ob_clamps_a_negative_score_to_zero():
    assert SL.opposed_ob(-3.0, 0.5) == 0.0
    assert SL.opposed_ob(-0.5, 1.0) == 0.0


def test_opposed_ob_refuses_a_missing_rate():
    with pytest.raises(TypeError):
        SL.opposed_ob(4.0)  # type: ignore[call-arg]


def test_even_line_is_the_owner_mean_times_the_base():
    assert SL.even_line(6) == dice_engine.MU_PER_DIE * 6
    assert SL.even_line(0) == 0.0


def test_pool_of_is_the_max_of_floor_and_sum():
    checked = 0
    for score in (0, 1, 3, 7):
        for addends in (-5, 0, 2):
            for pool_add in (-2, 0, 1):
                for floor in (0, 1, 4):
                    got = SL.pool_of(score, addends, pool_add, floor)
                    assert got == max(floor, score + addends + pool_add)
                    checked += 1
    assert checked == 4 * 3 * 3 * 3
    assert SL.pool_of(0, 0, 0, 1) == 1      # the floor binds
    assert SL.pool_of(5, 1, 1, 1) == 7      # the sum binds
