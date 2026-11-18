"""
engine/tests/test_draw.py -- B06.03: `engine.dice_engine.draw.Draw`, the ONE keyed draw. `u()` is the only primitive and
a function of (key, n) by the owned mix; every other method is this class's own function of `u()`.

THE CLAIM, AND WHAT WOULD SHOW IT WRONG:
  * `u()` IS A FUNCTION OF (key, n) AND NOTHING ELSE: the n-th uniform of a key is the key itself at n = 0 and
    `H2(key, n)` re-mixed at n >= 1, 53 high bits over 2**53. Twelve (key, n) -> u vectors (IEEE-754 hex) fix it,
    including n = 0, n = 1 and keys at or above 2**63; a changed shift, mix string or digest size moves one.
  * EACH SAMPLER CONSUMES THE UNIFORMS ITS DOCSTRING STATES, in that order, and returns the stated function of them.
    `test_samplers_match_their_vectors` runs a SECOND implementation (the `REFERENCE` section, written from the
    docstrings alone, over a plain list of uniforms and `math`, never importing `draw`) against the vector table and
    against `Draw`; a sampler that consumes a different number of uniforms than its vector states fails on the vector
    row's `consumed` and so would diverge at the first later draw.
  * `Draw` exposes none of the stdlib names (`randint`, `gauss`, `choice`, `betavariate`, `shuffle`, `sample`,
    `randrange`): a tenth site announces itself as an AttributeError.
  * `draw.py` IS A LEAF: it imports `hashlib` and `fmath` only (the AST check below, the item's GATE).

EXPECTED RED UNTIL B06.05: `test_no_random_Random_in_runtime_code`. It scans runtime code (`engine/season`,
`engine/dice_engine`, `modules`, tests excluded) for a `random.Random(...)` construction and fails while any remains;
B06.04 converts the sites and B06.05 removes the fallbacks, after which it passes. It is not marked xfail: red is its
honest reading until then.
"""
import ast
import hashlib
import math
import pathlib
import struct

import pytest

from engine.dice_engine.draw import H2, Draw, seeded

_ROOT = pathlib.Path(__file__).resolve().parents[2]
_TWO53 = 9007199254740992.0


def _bits(x: float) -> str:
    return struct.pack(">d", x).hex()


# --- REFERENCE BEGIN: a second implementation, from the docstrings alone. Plain list of uniforms, `math`, no import of
# draw. `H2` here is blake2b(f"v1d|{key}|{n}", digest_size=8) as its docstring says.
def ref_u(key: str, n: int) -> float:
    word = int(key, 16) if n == 0 else int(hashlib.blake2b(f"v1d|{key}|{n}".encode(), digest_size=8).hexdigest(), 16)
    return (word >> 11) / 9007199254740992.0


class _Stream:
    """The uniforms of a key from ordinal n0 on, counting what a sampler takes."""

    def __init__(self, key, n0):
        self.key, self.n0, self.taken = key, n0, 0

    def u(self):
        v = ref_u(self.key, self.n0 + self.taken)
        self.taken += 1
        return v


def ref_normal(s, mu, sigma):
    # Box-Muller, two uniforms, no cache: z = sqrt(-2 ln(1 - u1)) * cos(2 pi u2); mu + sigma * z
    u1 = s.u()
    u2 = s.u()
    z = math.sqrt(-2.0 * math.log(1.0 - u1)) * math.cos(6.283185307179586 * u2)
    return mu + sigma * z


def ref_gamma(s, k):
    # Marsaglia-Tsang. k < 1: g = gamma(k + 1), then one uniform v, result g * (1 - v) ** (1 / k).
    if k < 1.0:
        g = ref_gamma(s, k + 1.0)
        v = s.u()
        return g * ((1.0 - v) ** (1.0 / k))
    d = k - 1.0 / 3.0
    c = 1.0 / (3.0 * math.sqrt(d))
    while True:
        x = ref_normal(s, 0.0, 1.0)            # two uniforms
        t = 1.0 + c * x
        if t <= 0.0:
            continue                           # no further uniform is taken on this pass
        t3 = t * t * t
        w = 1.0 - s.u()                        # one uniform, in (0, 1]
        x2 = x * x
        if w < 1.0 - 0.0331 * (x2 * x2) or math.log(w) < 0.5 * x2 + d * (1.0 - t3 + math.log(t3)):
            return d * t3


def ref_beta(s, a, b):
    x = ref_gamma(s, a)
    y = ref_gamma(s, b)
    return x / (x + y)


def ref_below(s, n):
    return int(s.u() * n)


def ref_die(s, lo, hi):
    return lo + ref_below(s, hi - lo + 1)


def ref_pick(s, seq):
    return seq[ref_below(s, len(seq))]


_REF = {"below": ref_below, "die": ref_die, "normal": ref_normal, "beta": ref_beta}
# --- REFERENCE END


# twelve (key, n) -> u vectors, u as IEEE-754 binary64 hex: n = 0 (the key itself), n = 1 (one re-mix), later n, and
# keys at or above 2**63.
U_VECTORS = [
    ("0000000000000000", 0, "0000000000000000"),
    ("0000000000000001", 0, "0000000000000000"),
    ("0123456789abcdef", 0, "3f723456789abc80"),
    ("8000000000000000", 0, "3fe0000000000000"),
    ("ffffffffffffffff", 0, "3fefffffffffffff"),
    ("9e3779b97f4a7c15", 0, "3fe3c6ef372fe94f"),
    ("0000000000000000", 1, "3f9b5fec957df0a0"),
    ("0123456789abcdef", 1, "3fd363ce7c4624b4"),
    ("8000000000000000", 1, "3fee2fcc61f6470e"),
    ("ffffffffffffffff", 1, "3feecb108b34ec0d"),
    ("9e3779b97f4a7c15", 2, "3fd0cb1475b468ea"),
    ("c2b2ae3d27d4eb4f", 1000000, "3fd469e086983a0c"),
]

# per sampler: (key, n0, method, args, uniforms consumed, output) -- output IEEE-754 hex for a float, an int for an int.
SAMPLER_VECTORS = [
    ('0123456789abcdef', 0, 'below', (10,), 1, 0),
    ('0123456789abcdef', 3, 'die', (-3, 3), 1, 0),
    ('0123456789abcdef', 0, 'beta', (2.5, 1.5), 6, '3fe07816de10b907'),
    ('0123456789abcdef', 3, 'beta', (0.5, 0.5), 8, '3f7016ca45a2124d'),
    ('0123456789abcdef', 0, 'beta', (3.0, 4.0), 6, '3fd5e6cbe17ac49c'),
    ('0123456789abcdef', 0, 'beta', (8.0, 0.3), 7, '3fefffe8d5c1ab83'),
    ('fedcba9876543210', 3, 'die', (1, 10), 1, 5),
    ('fedcba9876543210', 0, 'normal', (50.0, 12.5), 2, '40271fefc5c757b8'),
    ('fedcba9876543210', 0, 'beta', (0.5, 0.5), 11, '3fd3725da2dadf16'),
    ('9e3779b97f4a7c15', 3, 'below', (1099511627783,), 1, 709316490898),
    ('9e3779b97f4a7c15', 0, 'normal', (0.0, 1.0), 2, '3ff29dd826949407'),
    ('9e3779b97f4a7c15', 3, 'beta', (1.0, 1.0), 6, '3fe4372e82af5925'),
    ('c2b2ae3d27d4eb4f', 3, 'below', (10,), 1, 5),
    ('c2b2ae3d27d4eb4f', 0, 'die', (-3, 3), 1, 2),
    ('c2b2ae3d27d4eb4f', 3, 'beta', (2.5, 1.5), 6, '3fe09fe27f367ed1'),
    ('8000000000000000', 0, 'die', (1, 10), 1, 6),
    ('8000000000000000', 3, 'normal', (50.0, 12.5), 2, '40521432ddfb0c46'),
    ('8000000000000000', 3, 'beta', (1.0, 1.0), 9, '3fe6a8e74095ee50'),
    ('243f6a8885a308d3', 0, 'below', (1099511627783,), 1, 155682769030),
    ('243f6a8885a308d3', 3, 'normal', (0.0, 1.0), 2, 'bfb1d4ecb5047fc2'),
    ('243f6a8885a308d3', 3, 'beta', (3.0, 4.0), 6, '3fe5950c6feb5645'),
    ('a4093822299f31d0', 0, 'normal', (50.0, 12.5), 2, '404a5df0073dd969'),
    ('a4093822299f31d0', 0, 'beta', (0.5, 0.5), 8, '3feab1246926a46b'),
    ('a4093822299f31d0', 3, 'beta', (8.0, 0.3), 7, '3fefffe7b46b850f'),
]


def test_u_is_a_function_of_the_key():
    """Same key, same sequence; the draw holds no state but (key, n); resuming at ordinal k equals the k-th of a run."""
    seq = []
    a = Draw("0123456789abcdef")
    for _ in range(6):
        seq.append(a.u())
    b = seeded("0123456789abcdef")
    assert [b.u() for _ in range(6)] == seq
    assert a.n == 6 and b.n == 6
    checked = 0
    for k in range(6):
        assert Draw("0123456789abcdef", k).u() == seq[k]
        checked += 1
    assert checked == 6
    # a different key is a different stream (n = 0 reads only the key's 53 high bits, so the low 11 bits show from n = 1)
    assert seeded("1123456789abcdef").u() != seq[0]
    other = seeded("0123456789abcdee")
    other.u()
    assert other.u() != seq[1]
    assert len(set(seq)) == 6 and all(0.0 <= x < 1.0 for x in seq)


def test_n_zero_is_the_key_itself():
    checked = 0
    for key in ("0000000000000000", "0000000000000001", "0123456789abcdef", "8000000000000000", "ffffffffffffffff"):
        want = (int(key, 16) >> 11) / _TWO53
        assert Draw(key).u() == want == ref_u(key, 0)
        checked += 1
    assert checked == 5
    assert Draw("ffffffffffffffff").u() < 1.0          # 53 high bits over 2**53 never reaches 1


def test_n_one_remixes_with_h2():
    assert H2("0123456789abcdef", 1) == hashlib.blake2b(b"v1d|0123456789abcdef|1", digest_size=8).hexdigest()
    assert len(H2("0123456789abcdef", 1)) == 16
    assert H2("0123456789abcdef", 1) != H2("0123456789abcdef", 2) != H2("0123456789abcdee", 2)
    checked = 0
    for key in ("0123456789abcdef", "8000000000000000", "ffffffffffffffff"):
        d = Draw(key)
        d.u()
        got = d.u()
        assert got == (int(H2(key, 1), 16) >> 11) / _TWO53 == ref_u(key, 1)
        checked += 1
    assert checked == 3


def test_twelve_u_vectors_reproduce_bit_for_bit():
    assert len(U_VECTORS) == 12
    assert any(n == 0 for _, n, _ in U_VECTORS) and any(n == 1 for _, n, _ in U_VECTORS)
    assert any(int(k, 16) >= 2 ** 63 for k, _, _ in U_VECTORS)
    checked = 0
    for key, n, hexbits in U_VECTORS:
        assert _bits(Draw(key, n).u()) == hexbits, f"u({key!r}, n={n})"
        assert _bits(ref_u(key, n)) == hexbits
        checked += 1
    assert checked == 12


def test_samplers_match_their_vectors():
    """Draw's samplers == the second implementation == the recorded vector, uniforms consumed included."""
    assert len(SAMPLER_VECTORS) >= 12
    seen = set()
    checked = 0
    for key, n0, method, args, consumed, out in SAMPLER_VECTORS:
        d = Draw(key, n0)
        got = getattr(d, method)(*args)
        s = _Stream(key, n0)
        want = _REF[method](s, *args)
        for name, v in (("Draw", got), ("reference", want)):
            rec = _bits(v) if isinstance(v, float) else v
            assert rec == out, f"{name}.{method}{args} on ({key}, {n0})"
        assert d.n - n0 == consumed == s.taken, f"{method}{args} on ({key}, {n0}): uniforms consumed"
        seen.add(method)
        checked += 1
    assert checked == len(SAMPLER_VECTORS)
    assert seen == {"below", "die", "normal", "beta"}
    # at least one beta vector took more uniforms than its minimum (a gamma with k >= 1 takes 3 at least, k < 1 takes
    # 4: gamma(k + 1) then one), so a rejection pass is observed, not assumed
    least = lambda k: 3 if k >= 1 else 4
    assert any(m == "beta" and c > least(a[0]) + least(a[1]) for _, _, m, a, c, _ in SAMPLER_VECTORS)
    # pick and random ride on the vectors above
    d = Draw("0123456789abcdef")
    assert d.pick(["a", "b", "c", "d"]) == ref_pick(_Stream("0123456789abcdef", 0), ["a", "b", "c", "d"])
    assert Draw("0123456789abcdef").random() == ref_u("0123456789abcdef", 0)


def test_draw_exposes_no_stdlib_sampler():
    checked = 0
    for name in ("randint", "randrange", "gauss", "choice", "betavariate", "shuffle", "sample", "choices", "uniform"):
        assert not hasattr(Draw("0123456789abcdef"), name), name
        with pytest.raises(AttributeError):
            getattr(seeded("0123456789abcdef"), name)
        checked += 1
    assert checked == 9
    for name in ("u", "random", "below", "die", "pick", "normal", "beta"):
        assert callable(getattr(Draw, name))


def test_below_pick_and_die_refuse():
    """The refusal form is a ValueError naming the argument (B06.03's ASSUMPTION, recorded in the docstring)."""
    d = Draw("0123456789abcdef")
    for call, arg in ((lambda: d.below(0), "n"), (lambda: d.below(-3), "n"), (lambda: d.pick([]), "seq"),
                      (lambda: d.die(5, 4), "hi")):
        with pytest.raises(ValueError, match=arg):
            call()
    assert d.n == 0, "a refusal consumes no uniform"
    assert Draw("0123456789abcdef").below(1) == 0
    assert 3 <= Draw("0123456789abcdef").die(3, 3) <= 3
    for k in ("0123456789abcdef", "ffffffffffffffff", "8000000000000000"):
        assert 1 <= Draw(k).die(1, 10) <= 10 and 0 <= Draw(k).below(7) < 7


def test_draw_is_a_leaf():
    """The item's GATE: draw.py imports `hashlib` and `fmath` only."""
    t = ast.parse((_ROOT / "engine" / "dice_engine" / "draw.py").read_text())
    # the gate's own form: the first imported name of each import statement
    names = sorted({a.names[0].name for a in ast.walk(t) if isinstance(a, (ast.Import, ast.ImportFrom))})
    assert names == ["fmath", "hashlib"], names


def _runtime_files():
    out = []
    for root in ("engine/season", "engine/dice_engine", "modules"):
        for p in sorted((_ROOT / root).rglob("*.py")):
            parts = p.relative_to(_ROOT).parts
            if "tests" in parts or "__pycache__" in parts or p.name.startswith("test_"):
                continue
            out.append(p)
    return out


def test_no_random_Random_in_runtime_code():
    """EXPECTED RED UNTIL B06.05: every runtime generator is a keyed `Draw`, so no `random.Random(...)` remains in
    `engine/season`, `engine/dice_engine`, `modules` (tests excluded). Red until B06.04 converts the sites and B06.05
    removes the fallbacks; not xfail."""
    files = _runtime_files()
    assert len(files) > 100, "the scan found too few files to mean anything"
    hits = []
    for p in files:
        tree = ast.parse(p.read_text(encoding="utf-8"))
        from_random = {a.asname or a.name for n in ast.walk(tree)
                       if isinstance(n, ast.ImportFrom) and n.module == "random" for a in n.names if a.name == "Random"}
        for n in ast.walk(tree):
            if not isinstance(n, ast.Call):
                continue
            f = n.func
            if (isinstance(f, ast.Attribute) and f.attr == "Random" and isinstance(f.value, ast.Name)
                    and f.value.id == "random") or (isinstance(f, ast.Name) and f.id in from_random):
                hits.append(f"{p.relative_to(_ROOT)}:{n.lineno}")
    assert not hits, "random.Random( constructions remain in runtime code: " + ", ".join(hits)
