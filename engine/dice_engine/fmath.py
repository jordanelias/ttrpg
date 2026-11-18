"""
engine/dice_engine/fmath.py — the float operations the game path shares with the port, each with ONE owner.

THE RULE, STATED ONCE: a float sum goes through `ltr_sum`. The builtin `sum()` is not the rule: CPython 3.12
changed it to Neumaier-compensated summation for floats, so `sum()` of the same operands reads one ULP apart on
3.11 and on 3.12+ (CR-01: bind_sigma for bear_spear). `ltr_sum` is the pre-3.12 value on every interpreter, and a
port reproduces it by adding left to right. Integer sums are left alone (their addition is exact).

A leaf: it imports nothing from the repository (`math` only, when B06.02 adds the transcendentals). Pure.
"""


def ltr_sum(xs) -> float:
    """Left-to-right float accumulation: ((0 + x0) + x1) + x2 ... — each `+` is one IEEE-754 binary64 addition,
    correctly rounded on every platform, so the ACCUMULATION is bit-identical everywhere (an operand's own `**` or
    transcendental is the platform's libm and is not controlled here). An empty input is the integer 0, as `sum()`
    gives."""
    total = 0
    for x in xs:
        total += x
    return total
