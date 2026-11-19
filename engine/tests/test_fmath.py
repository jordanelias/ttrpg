"""
engine/tests/test_fmath.py -- B06.01: `engine.dice_engine.fmath.ltr_sum`, the ONE accumulation rule for a float sum on
the game path: ((0 + x0) + x1) + ..., each `+` one IEEE-754 binary64 addition. B06.02 (below the `VECTORS` banner): the
one owner of each transcendental, and the vector table a port reads.

THE CLAIM, AND WHAT WOULD SHOW IT WRONG:
  * `ltr_sum` IS THE EXPLICIT LEFT-TO-RIGHT FOLD, BIT FOR BIT, in any order of the operands. CPython 3.12 made the
    builtin `sum()` of floats Neumaier-compensated, so `sum()` and the fold read one ULP apart on 3.12+ and agree on
    3.11. The list below is one whose compensated sum (`math.fsum`, correctly rounded, the value any compensated
    accumulation lands on) and left-to-right sum differ in the last bit in all three orderings, so an
    implementation that delegated to `sum()` or `fsum` fails here on 3.13 and passes by luck on 3.11; the
    `_DIFFERS` control asserts the list still separates the two rules, so the test cannot go vacuous.
"""
import math
import struct

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


# ---------------------------------------------------------------------------------------------------------------------
# B06.02 -- THE VECTORS: one table, one row per (function, input bits) -> output bits, all IEEE-754 binary64 as 16 hex
# digits (sign|exponent|mantissa). The inputs cover the operand ranges the call sites reach (the Gumbel `log` of a
# uniform, the guard's decaying `exp`, `tanh`'s soft caps, `erf` of a z-score, the mass-battle turn angles and
# distances, the percussion `powf` at PERC_EXP = 0.30). The outputs are `math`'s on the oracle's interpreter (the
# platform libm: the cpython 3.11 and 3.13 builds read the same here). A port reads this table at ULP_BOUND; a
# mismatch names the function and the input, which a bare hash divergence cannot.
#
# STATED BOUND: `ltr_sum` and the IEEE-754-exact operations are bit-equal (0 ulp); the transcendentals
# (log, exp, tanh, erf, sin, cos, atan2, powf) are within ULP_BOUND ulp of the oracle on the port's libm. `hypot` is
# held to the same bound (its correct rounding is not guaranteed across libms).
# ---------------------------------------------------------------------------------------------------------------------
ULP_BOUND = 1
EXACT = ("ltr_sum",)

VECTORS = (
    ('log', ('3fe0000000000000',), 'bfe62e42fefa39ef'),
    ('log', ('3e112e0be826d695',), 'c034b927f32bffb8'),
    ('log', ('3fefffffca501acb',), 'be7ad7f2b1049b9f'),
    ('log', ('3fbf9add3739635f',), 'c000bc233add5d72'),
    ('log', ('3ff0000000000000',), '0000000000000000'),
    ('log', ('4005bf0a8b145769',), '3ff0000000000000'),
    ('log', ('4042c00000000000',), '400cfea67585803d'),
    ('log', ('01a56e1fc2f8f359',), 'c085963447f87fb5'),
    ('exp', ('0000000000000000',), '3ff0000000000000'),
    ('exp', ('bf8930be0ded288d',), '3fef9bdb0562bf4c'),
    ('exp', ('bfe8000000000000',), '3fde3b40ebefcd7e'),
    ('exp', ('c00c000000000000',), '3f9eec1018e4ff66'),
    ('exp', ('c028800000000000',), '3ed411fb0da07713'),
    ('exp', ('bfd5555555555555',), '3fe6edd3122f2ea5'),
    ('exp', ('3ff8000000000000',), '4011ed3fe64fc541'),
    ('exp', ('3fe999999999999a',), '4001cde866fe46e9'),
    ('tanh', ('0000000000000000',), '0000000000000000'),
    ('tanh', ('3fa999999999999a',), '3fa99424e535f6f9'),
    ('tanh', ('3fd3333333333333',), '3fd2a4dda7d914fa'),
    ('tanh', ('3feccccccccccccd',), '3fe6ebe982d6605d'),
    ('tanh', ('3ffb333333333333',), '3fedeedf00d3e7f5'),
    ('tanh', ('bfe3333333333333',), 'bfe12f8292d2ccfc'),
    ('tanh', ('4010000000000000',), '3feffa81708a0b42'),
    ('tanh', ('4023000000000000',), '3feffffff9fbea41'),
    ('erf', ('0000000000000000',), '0000000000000000'),
    ('erf', ('3fb999999999999a',), '3fbcca5ea24fb334'),
    ('erf', ('3fe0000000000000',), '3fe0a7ef5c18edd2'),
    ('erf', ('3ff3333333333333',), '3fed214ac7b2d067'),
    ('erf', ('bfe6a09e667f3bcd',), 'bfe5d897a241a6fb'),
    ('erf', ('4002666666666666',), '3feff6a295bcd35c'),
    ('erf', ('c00f333333333333',), 'bfefffffed523094'),
    ('erf', ('4016000000000000',), '3fefffffffffffbe'),
    ('sin', ('0000000000000000',), '0000000000000000'),
    ('sin', ('3fb999999999999a',), '3fb98eaecb8bcb2c'),
    ('sin', ('3fe921fb54442d18',), '3fe6a09e667f3bcc'),
    ('sin', ('3ff921fb54442d18',), '3ff0000000000000'),
    ('sin', ('c003333333333333',), 'bfe59d64f5c3d19b'),
    ('sin', ('400921fb54442d18',), '3ca1a62633145c07'),
    ('sin', ('bf3a36e2eb1c432d',), 'bf3a36e2df61dcd8'),
    ('cos', ('0000000000000000',), '3ff0000000000000'),
    ('cos', ('3fb999999999999a',), '3fefd712f9a817c1'),
    ('cos', ('3fe921fb54442d18',), '3fe6a09e667f3bcd'),
    ('cos', ('3ff921fb54442d18',), '3c91a62633145c07'),
    ('cos', ('c003333333333333',), 'bfe798bab490d185'),
    ('cos', ('400921fb54442d18',), 'bff0000000000000'),
    ('cos', ('bf3a36e2eb1c432d',), '3fefffffd50ce245'),
    ('atan2', ('0000000000000000', '3ff0000000000000'), '0000000000000000'),
    ('atan2', ('3ff0000000000000', '3ff0000000000000'), '3fe921fb54442d18'),
    ('atan2', ('bff0000000000000', '3ff0000000000000'), 'bfe921fb54442d18'),
    ('atan2', ('4004000000000000', 'bfe8000000000000'), '3ffdcbc9edcbd8da'),
    ('atan2', ('c008000000000000', 'c010000000000000'), 'c003fc176b7a8560'),
    ('atan2', ('3e112e0be826d695', '3ff0000000000000'), '3e112e0be826d695'),
    ('atan2', ('0000000000000000', 'bff0000000000000'), '400921fb54442d18'),
    ('atan2', ('bfd3333333333333', '0000000000000000'), 'bff921fb54442d18'),
    ('hypot', ('4008000000000000', '4010000000000000'), '4014000000000000'),
    ('hypot', ('3ff0000000000000', '3ff0000000000000'), '3ff6a09e667f3bcd'),
    ('hypot', ('0000000000000000', '0000000000000000'), '0000000000000000'),
    ('hypot', ('c004000000000000', '3fe8000000000000'), '4004e16fdacff937'),
    ('hypot', ('3e45798ee2308c3a', '3ff0000000000000'), '3ff0000000000000'),
    ('hypot', ('4028000000000000', 'c014000000000000'), '402a000000000000'),
    ('hypot', ('3fb999999999999a', '3fc999999999999a'), '3fcc9f25c5bfedda'),
    ('hypot', ('4197d78400000000', '3e45798ee2308c3a'), '4197d78400000000'),
    ('powf', ('3fe0000000000000', '3fd3333333333333'), '3fe9fdf8bcce533e'),
    ('powf', ('4000000000000000', '3fd3333333333333'), '3ff3b2c47bff8329'),
    ('powf', ('3f847ae147ae147b', '3fd3333333333333'), '3fd0137987dd704c'),
    ('powf', ('400d99999999999a', '3fd3333333333333'), '3ff7b0db08b44be4'),
    ('powf', ('3eb0c6f7a0b5ed8d', '3fd3333333333333'), '3f903ab3d12bc2c5'),
    ('powf', ('3fe999999999999a', '3ff8000000000000'), '3fe6e5b7d16657e2'),
    ('powf', ('4000000000000000', 'bfe0000000000000'), '3fe6a09e667f3bcd'),
    ('powf', ('4022000000000000', '3fe0000000000000'), '4008000000000000'),
    ('ltr_sum', ('3fcb020c49ba5e35', '3fc1eb851eb851ec', '3f6040bfe3b03e21', '3fcccccccccccccd', '3ffb7ced916872b0', '3f6244a6223e186a'), '400262be0589acbc'),
    ('ltr_sum', ('3f6244a6223e186a', '3ffb7ced916872b0', '3fcccccccccccccd', '3f6040bfe3b03e21', '3fc1eb851eb851ec', '3fcb020c49ba5e35'), '400262be0589acbc'),
    ('ltr_sum', ('3f6040bfe3b03e21', '3f6244a6223e186a', '3fc1eb851eb851ec', '3fcb020c49ba5e35', '3fcccccccccccccd', '3ffb7ced916872b0'), '400262be0589acbc'),
)

_FUNCTIONS = ("log", "exp", "tanh", "erf", "sin", "cos", "atan2", "hypot", "powf")


def _from_bits(h):
    return struct.unpack(">d", struct.pack(">Q", int(h, 16)))[0]


def _to_bits(x):
    return "%016x" % struct.unpack(">Q", struct.pack(">d", x))[0]


def _ordered(h):
    """The bit pattern as an integer that increases with the float's value (so the difference of two is their distance
    in ulps, across zero too)."""
    n = int(h, 16)
    return (1 << 63) - (n & ((1 << 63) - 1)) if n >> 63 else n + (1 << 63)


def _ulps(got_bits, want_bits):
    return abs(_ordered(got_bits) - _ordered(want_bits))


def _call(fn, name, ins):
    xs = [_from_bits(h) for h in ins]
    return fn(xs) if name == "ltr_sum" else fn(*xs)


def _failures(module):
    """Every vector `module` fails, as (name, input bits, got bits, want bits, ulps, bound)."""
    bad = []
    for name, ins, want in VECTORS:
        got = _to_bits(_call(getattr(module, name), name, ins))
        bound = 0 if name in EXACT else ULP_BOUND
        if _ulps(got, want) > bound:
            bad.append((name, ins, got, want, _ulps(got, want), bound))
    return bad


def test_control_the_vectors_cover_every_function_and_the_sum():
    assert {v[0] for v in VECTORS} == set(_FUNCTIONS) | set(EXACT)
    assert all(sum(1 for v in VECTORS if v[0] == f) >= 7 for f in _FUNCTIONS)
    assert sum(1 for v in VECTORS if v[0] == "ltr_sum") == 3


def test_every_vector_reproduces_bit_for_bit():
    """On the oracle's own libm every vector is bit-equal (0 ulp); a port's libm is held to ULP_BOUND by `_failures`."""
    checked = 0
    for name, ins, want in VECTORS:
        got = _to_bits(_call(getattr(fmath, name), name, ins))
        assert got == want, f"fmath.{name}{ins}: got {got}, want {want}"
        checked += 1
    assert checked == len(VECTORS) >= 70
    assert _failures(fmath) == []


def test_a_planted_change_of_one_function_fails_and_names_it():
    class Planted:
        """`fmath` with `tanh` one ulp off at every input (a planted change of one function's body)."""
        def __getattr__(self, name):
            fn = getattr(fmath, name)
            if name != "tanh":
                return fn
            return lambda x: struct.unpack(">d", struct.pack(">Q", struct.unpack(">Q", struct.pack(">d", fn(x)))[0] + 2))[0]

    bad = _failures(Planted())
    assert bad and {b[0] for b in bad} == {"tanh"}
    assert all(b[4] > b[5] for b in bad)


def test_ulp_distance_is_symmetric_across_zero():
    assert _ulps(_to_bits(0.0), _to_bits(-0.0)) == 0
    assert _ulps(_to_bits(math.nextafter(0.0, 1.0)), _to_bits(math.nextafter(0.0, -1.0))) == 2
    assert _ulps(_to_bits(1.0), _to_bits(math.nextafter(1.0, 2.0))) == 1
    assert _ulps(_to_bits(math.nextafter(1.0, 0.0)), _to_bits(math.nextafter(1.0, 2.0))) == 2


def test_each_function_is_one_call_to_math():
    """`fmath.<f>` is `math.<f>` on every input of the table (the control the realm hash reading rests on)."""
    for name in _FUNCTIONS:
        if name == "powf":
            continue
        for n, ins, _ in VECTORS:
            if n == name:
                xs = [_from_bits(h) for h in ins]
                assert _to_bits(getattr(fmath, name)(*xs)) == _to_bits(getattr(math, name)(*xs))


def test_powf_is_the_power_operator_not_math_pow():
    assert fmath.powf(2.0, 0.3) == 2.0 ** 0.3
    assert isinstance(fmath.powf(-8.0, 1.0 / 3.0), complex)   # `**` goes complex on a negative base; math.pow raises
