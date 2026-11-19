"""
engine/dice_engine/fmath.py — the float operations the game path shares with the port, each with ONE owner.

THE RULE, STATED ONCE: a float sum goes through `ltr_sum`. The builtin `sum()` is not the rule: CPython 3.12
changed it to Neumaier-compensated summation for floats, so `sum()` of the same operands reads one ULP apart on
3.11 and on 3.12+ (CR-01: bind_sigma for bear_spear). `ltr_sum` is the pre-3.12 value on every interpreter, and a
port reproduces it by adding left to right. Integer sums are left alone (their addition is exact).

THE SECOND RULE, STATED ONCE: a transcendental goes through this module. `log`, `exp`, `tanh`, `erf`, `sin`, `cos`,
`atan2`, `hypot` and `powf` (`x ** y` for a FLOAT exponent) are each ONE call to `math`, and a game-path module calls
these, never `math.*` -- so a port has ONE list of functions to reproduce, and `engine/tests/test_fmath.py`'s vectors
name the function and the input when it does not. These are the platform's libm, not an IEEE-754-exact operation: the
test states the ulp bound a port must meet. `sqrt` is exact too (IEEE-754 requires it correctly rounded): call sites keep `math.sqrt`, and `fmath.sqrt` exists only because
`draw.py` may import `fmath` and not `math`. `floor`, `ceil`, `fabs`, `fsum`, `isfinite`, `degrees`, `pi` and the like are exact and stay on `math`. An integer power (`x ** 2`) is
left alone: CPython evaluates `float ** int` through the platform's `pow`, so it carries the libm bound above, not an exact one.

SCOPE, STATED ONCE: both rules are met on the season path (`engine/`) and the combat and social-contest modules the loop
reaches; `modules/mass_battle/`'s field arithmetic still holds builtin float `sum()`, `** 0.5` and `math.acos`, and is
converted by the batch that owns that module (B17). Until then its golden digests (`systems/mass_battle/sim/bat.py`)
read differently on 3.11 and 3.13, and are recorded on 3.11, CI's interpreter.

A leaf: it imports `math` only. Pure.
"""
import math
from functools import reduce as _reduce
from operator import add as _add


def ltr_sum(xs) -> float:
    """Left-to-right float accumulation: ((0 + x0) + x1) + x2 ... — each `+` is one IEEE-754 binary64 addition,
    correctly rounded on every platform, so the ACCUMULATION is bit-identical everywhere (an operand's own `**` or
    transcendental is the platform's libm and is not controlled here). An empty input is the integer 0, as `sum()`
    gives."""
    return _reduce(_add, xs, 0)


def log(x: float) -> float:
    """Natural logarithm: one call to `math.log`."""
    return math.log(x)


def exp(x: float) -> float:
    """e ** x: one call to `math.exp`."""
    return math.exp(x)


def tanh(x: float) -> float:
    """Hyperbolic tangent: one call to `math.tanh`."""
    return math.tanh(x)


def erf(x: float) -> float:
    """Error function: one call to `math.erf`."""
    return math.erf(x)


def sin(x: float) -> float:
    """Sine of an angle in radians: one call to `math.sin`."""
    return math.sin(x)


def cos(x: float) -> float:
    """Cosine of an angle in radians: one call to `math.cos`."""
    return math.cos(x)


def atan2(y: float, x: float) -> float:
    """Angle of the point (x, y) in (-pi, pi]: one call to `math.atan2`."""
    return math.atan2(y, x)


def hypot(x: float, y: float) -> float:
    """Euclidean length of (x, y): one call to `math.hypot` (two operands, as every game site passes two)."""
    return math.hypot(x, y)


def powf(x: float, y: float) -> float:
    """`x ** y` for a float exponent: the operator itself, so it is `float.__pow__` (libm `pow`) exactly as the site
    it replaces. Not `math.pow`, which differs from `**` on a negative base and raises where `**` returns complex."""
    return x ** y


def sqrt(x: float) -> float:
    """`math.sqrt`: IEEE-754 requires it correctly rounded, so it is bit-identical on every platform. It is here only
    for `draw.py`, a leaf that may import `fmath` and not `math`; `powf(x, 0.5)` is libm `pow` and carries no such
    guarantee, so a sampler never takes a root that way."""
    return math.sqrt(x)
