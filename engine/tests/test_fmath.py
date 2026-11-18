"""
engine/tests/test_fmath.py -- B06.01: `engine.dice_engine.fmath.ltr_sum`, the ONE accumulation rule for a float sum on
the game path: ((0 + x0) + x1) + ..., each `+` one IEEE-754 binary64 addition.

THE CLAIM, AND WHAT WOULD SHOW IT WRONG:
  * `ltr_sum` IS THE EXPLICIT LEFT-TO-RIGHT FOLD, BIT FOR BIT, in any order of the operands. CPython 3.12 made the
    builtin `sum()` of floats Neumaier-compensated, so `sum()` and the fold read one ULP apart on 3.12+ and agree on
    3.11. The list below is one whose compensated sum (`math.fsum`, correctly rounded, the value any compensated
    accumulation lands on) and left-to-right sum differ in the last bit in all three orderings, so an
    implementation that delegated to `sum()` or `fsum` fails here on 3.13 and passes by luck on 3.11; the
    `_DIFFERS` control asserts the list still separates the two rules, so the test cannot go vacuous.
"""
import math

from engine.dice_engine import fmath

# a list whose compensated and left-to-right sums differ in the last bit under each of the three orderings below
_XS = [0.211, 0.14, 0.001984, 0.225, 1.718, 0.00223]
_ORDERINGS = (_XS, _XS[::-1], sorted(_XS))


def _fold(xs):
    """The explicit ((0 + x0) + x1) + ... , written out here and nowhere imported."""
    total = 0
    for x in xs:
        total = total + x
    return total


def test_control_the_list_separates_compensated_from_left_to_right():
    differing = sum(1 for xs in _ORDERINGS if _fold(xs) != math.fsum(xs))
    assert differing == len(_ORDERINGS), "the planted list no longer separates the two accumulation rules"


def test_ltr_sum_is_left_to_right_on_three_orderings():
    checked = 0
    for xs in _ORDERINGS:
        got = fmath.ltr_sum(xs)
        assert got.hex() == _fold(xs).hex()
        assert got != math.fsum(xs)
        checked += 1
    assert checked == 3


def test_ltr_sum_takes_a_generator_and_an_empty_input():
    assert fmath.ltr_sum(x for x in _XS).hex() == _fold(_XS).hex()
    assert fmath.ltr_sum([]) == 0
