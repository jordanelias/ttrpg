"""
engine/dice_engine/draw.py -- the ONE keyed draw. A leaf: it imports `hashlib` and `fmath` only. Pure.

A `Draw` is a uniform source that is a function of a key and an ordinal and of nothing else: no generator state to
record, no stream to replay, so the same key gives the same values in any language that implements the mix. The
n-th uniform of a key is the draw keyed `(H(seed, tick, subject, purpose), n)` (`H` is the id mint in
`engine/season/state/ids.py`; this module takes its 16-hex result as `key`).

THE MIX. n = 0: the word is the key itself, read as a 64-bit integer. n >= 1: the word is `H2(key, n)` read as a
64-bit integer, `H2` = blake2b(f"v1d|{key}|{n}", digest_size=8) in lowercase hex. The uniform is the 53 high bits of
the word over 2**53, so it lies in [0, 1).

THE SURFACE. `u()` is the only primitive; `random`, `below`, `die`, `pick`, `normal` and `beta` are functions of
`u()`. `Draw` has no `randint`, `randrange`, `gauss`, `choice`, `betavariate`, `shuffle` or `sample`: calling one is
an AttributeError at the site, which is how a stray stdlib call announces itself.

REFUSAL (ASSUMPTION; low; revert: return a clamped value instead of raising). `below` and `pick` (and `die`, which
rides on `below`) refuse an empty range with a `ValueError` whose message names the argument ("below: n must be >= 1",
"pick: seq must not be empty", "die: hi must be >= lo"). The source says "refuses" and names no form. A refusal is
raised before any uniform is taken, so it moves no stream.

THE ALGORITHMS (ASSUMPTION; low; revert: the other algorithm, one more re-pin). A tuning-free choice with no game
reading; each is named here with the uniforms it consumes, in order, so a port reproduces it from `u()` alone. The
square root is `fmath.sqrt` (`draw.py` may not import `math`); every other transcendental is `fmath`'s.
"""
import hashlib

from engine.dice_engine import fmath

_TWO53 = 9007199254740992.0  # [GROUNDED: 2**53, the span of a binary64 mantissa; `u` keeps the top 53 bits of a 64-bit word]
_TWO_PI = 6.283185307179586  # [GROUNDED: 2*pi, the angle Box-Muller's cosine takes]


def H2(key_hex: str, n: int) -> str:
    """The re-mix of a key at ordinal n >= 1: blake2b(f"v1d|{key_hex}|{n}", digest_size=8), 16 lowercase hex digits.
    Its one home."""
    # [JUSTIFIED: 8 bytes = the 64-bit word `u` slices; the mix is the keyed-draw owner's own choice (A-30)]
    return hashlib.blake2b(f"v1d|{key_hex}|{n}".encode(), digest_size=8).hexdigest()


class Draw:
    """One keyed draw. `u()` is the only primitive, a function of (key, n) by an owned mix (A-30); every other method
    is this class's own function of `u()`, so the same key gives the same values in any language that implements the
    mix. The index `n` is part of the key: the n-th uniform is the draw keyed `(H(seed, tick, subject, purpose), n)`,
    so A-30's "one draw per key" holds with the index counted in the key, and no uniform depends on anything but its
    key. No recorder: there is nothing to record.

    `key` is the 16-hex H(seed, tick, subject, purpose); `n` counts the draws taken from this key (a `Draw` built at
    `n = k` resumes the stream at its k-th uniform)."""

    __slots__ = ("key", "n")

    def __init__(self, key: str, n: int = 0):
        self.key = key
        self.n = n

    def u(self) -> float:
        """The n-th uniform of this key, in [0, 1): the first (n = 0) is the key itself, later ones re-mix it with n
        through `H2`; the 53 high bits of the 64-bit word over 2**53. Consumes one ordinal."""
        # [GROUNDED: base 16 is the hex of the key and of `H2`]
        word = int(self.key, 16) if self.n == 0 else int(H2(self.key, self.n), 16)
        self.n += 1
        # [GROUNDED: 64 - 53 = 11 low bits dropped, so the 53 high bits are the uniform's mantissa]
        return (word >> 11) / _TWO53

    def random(self) -> float:
        """Alias of `u`, so the existing `.random()` sites are unedited."""
        return self.u()

    def below(self, n: int) -> int:
        """int(u() * n): an integer in [0, n). One uniform. Refuses n < 1 (ValueError naming `n`)."""
        if n < 1:
            raise ValueError(f"below: n must be >= 1, got {n!r}")
        return int(self.u() * n)

    def die(self, lo: int, hi: int) -> int:
        """lo + below(hi - lo + 1): an integer in [lo, hi], inclusive. One uniform. Refuses hi < lo (ValueError
        naming `hi`)."""
        if hi < lo:
            raise ValueError(f"die: hi must be >= lo, got lo={lo!r}, hi={hi!r}")
        return lo + self.below(hi - lo + 1)

    def pick(self, seq):
        """seq[below(len(seq))]: one element. One uniform. Refuses an empty seq (ValueError naming `seq`)."""
        if len(seq) < 1:
            raise ValueError("pick: seq must not be empty")
        return seq[self.below(len(seq))]

    def normal(self, mu: float, sigma: float) -> float:
        """Box-Muller, two uniforms in order, no cache (the sine half is discarded): u1 = u(); u2 = u();
        z = sqrt(-2 * ln(1 - u1)) * cos(2*pi * u2), 2*pi = 6.283185307179586, sqrt = fmath.sqrt, ln and cos
        from fmath; returns mu + sigma * z. `1 - u1` lies in (0, 1], so the log is finite. Always consumes two."""
        u1 = self.u()
        u2 = self.u()
        z = fmath.sqrt(-2.0 * fmath.log(1.0 - u1)) * fmath.cos(_TWO_PI * u2)
        return mu + sigma * z

    def beta(self, a: float, b: float) -> float:
        """Beta(a, b) as X / (X + Y), X = gamma(a) then Y = gamma(b), each by Marsaglia-Tsang. Refuses a <= 0 or
        b <= 0 (ValueError naming the argument). gamma(k):
          k < 1: g = gamma(k + 1); v = u(); return g * powf(1 - v, 1/k)        (g's uniforms first, then one)
          k >= 1: d = k - 1/3; c = 1 / (3 * sqrt(d)); loop:
              x = normal(0, 1)                                                  (two uniforms)
              t = 1 + c*x; if t <= 0: next pass                                 (no further uniform on this pass)
              t3 = t*t*t; w = 1 - u()                                           (one uniform; w in (0, 1])
              x2 = x*x; accept if w < 1 - 0.0331*(x2*x2) or ln(w) < 0.5*x2 + d*(1 - t3 + ln(t3))
              on accept return d * t3
        The number of uniforms consumed varies with the rejections; it is a function of the key."""
        if a <= 0:
            raise ValueError(f"beta: a must be > 0, got {a!r}")
        if b <= 0:
            raise ValueError(f"beta: b must be > 0, got {b!r}")
        x = self._gamma(a)
        y = self._gamma(b)
        return x / (x + y)

    def _gamma(self, k: float) -> float:
        if k < 1.0:
            g = self._gamma(k + 1.0)
            v = self.u()
            return g * fmath.powf(1.0 - v, 1.0 / k)
        d = k - 1.0 / 3.0
        c = 1.0 / (3.0 * fmath.sqrt(d))
        while True:
            x = self.normal(0.0, 1.0)
            t = 1.0 + c * x
            if t <= 0.0:
                continue
            t3 = t * t * t
            w = 1.0 - self.u()
            x2 = x * x
            # [GROUNDED: Marsaglia & Tsang (2000), 'A simple method for generating gamma variables': the squeeze 0.0331]
            if w < 1.0 - 0.0331 * (x2 * x2) or fmath.log(w) < 0.5 * x2 + d * (1.0 - t3 + fmath.log(t3)):
                return d * t3


def seeded(key_hex: str) -> Draw:
    """The ONE constructor: a Draw at n = 0 on the 16-hex key H(seed, tick, subject, purpose)."""
    return Draw(key_hex)
