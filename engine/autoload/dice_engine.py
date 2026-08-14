"""
sim/autoload/dice_engine.py — d10 dice pool, TN values, degree of success, continuous engine

Canon source: params/core.md (Die Rule, TN Values, Degrees of Success, Continuous Engine Decision E)
Params source: params/core.md
Status: [CANONICAL — Phase 1 implementation 2026-05-17]

Dependencies:
  - none — root primitive

Entry points:
  - roll_pool(pool_size: int, tn: int, rng=None) -> RollResult
  - continuous_engine_sample(pool: float, tn: int, rng=None) -> float
  - degree_from_net(net: int | float, ob: int | float) -> Degree
"""
from __future__ import annotations

import math
import random
from dataclasses import dataclass
from enum import Enum


class Degree(Enum):
    OVERWHELMING = "overwhelming"
    SUCCESS = "success"
    PARTIAL = "partial"
    FAILURE = "failure"


# Several subsystems carry the four bands as Title-Case strings rather than the enum. ONE map, so a
# string-speaking module still resolves its bands through the owner instead of re-deciding them.
DEGREE_LABEL: dict["Degree", str] = {
    Degree.OVERWHELMING: "Overwhelming",
    Degree.SUCCESS: "Success",
    Degree.PARTIAL: "Partial",
    Degree.FAILURE: "Failure",
}


@dataclass
class RollResult:
    pool_size: int
    tn: int
    rolls: list[int]
    net: int
    degree: Degree | None  # None if no Ob provided
    ob: int | float | None


# Canonical die rule (params/core.md §Die Rule, PP-246):
#   1 = -1 success, 2-6 = 0, 7-9 = +1 success, 10 = +2 successes. No chain.
def _die_result(face: int) -> int:
    if face == 1:
        return -1
    elif face <= 6:
        return 0
    elif face <= 9:
        return 1
    else:  # 10
        return 2


# Per-die EV table (params/core.md §Expected Value):
#   TN 6: μ=0.50, σ=0.806
#   TN 7: μ=0.40, σ=0.800
#   TN 8: μ=0.30, σ=0.781
_CONTINUOUS_PARAMS: dict[int, tuple[float, float]] = {
    6: (0.50, 0.806),
    7: (0.40, 0.800),
    8: (0.30, 0.781),
}


def roll_pool(pool_size: int, tn: int = 7, ob: int | float | None = None,
              rng: random.Random | None = None) -> RollResult:
    """Roll pool_size d10s under the canonical face rule. Pool minimum 1D."""
    if rng is None:
        rng = random.Random()
    effective_pool = max(1, pool_size)  # params/core.md §Pool Minimum
    rolls = [rng.randint(1, 10) for _ in range(effective_pool)]
    net = sum(_die_result(face) for face in rolls)
    deg = degree_from_net(net, ob) if ob is not None else None
    return RollResult(pool_size=effective_pool, tn=tn, rolls=rolls, net=net, degree=deg, ob=ob)


def continuous_engine_sample(pool: float, tn: int = 7,
                             rng: random.Random | None = None) -> float:
    """Sample net successes from Normal(μ·N, σ·√N) per Decision E continuous engine.

    Canon: params/core.md §Continuous Engine — statistically equivalent to discrete.
    Pool may be fractional (enables fractional Ob / TN modifiers).
    """
    if rng is None:
        rng = random.Random()
    if pool <= 0:
        return 0.0
    mu, sigma = _CONTINUOUS_PARAMS.get(tn, _CONTINUOUS_PARAMS[7])
    mean = mu * pool
    std = sigma * math.sqrt(pool)
    return rng.gauss(mean, std)


def degree_from_net(net: int | float, ob: int | float) -> Degree:
    """THE degree ladder. Single owner for every scale of the game (Jordan ruling, 2026-08-14).

    The ladder reads the MARGIN — how far the dice cleared the obstacle — never the obstacle's
    own size:

        margin = net - ob

        margin >= 3        Overwhelming   "3 or more is always overwhelming"
        margin >= 1        Success        cleared it by at least one whole success
        0 <= margin < 1    Partial        the obstacle is MET but not EXCEEDED
        margin <  0        Failure        fell short

    Both operands may be fractional. `net` already is — the continuous engine returns fractional
    nets. `ob` is RULED to become fractional (Jordan, 2026-08-14: an obstacle rolled against a
    character or faction is "their corresponding score/2 plus whatever specific modifiers exist for
    them in that instance") but ⚠ THAT DERIVATION IS IMPLEMENTED NOWHERE — every call site in the
    tree still passes a hand-set Ob. An earlier draft of this paragraph stated it as an accomplished
    fact; it is a ruling awaiting execution, and the distinction matters here more than anywhere
    else, because this is the function a reader consults to learn what an obstacle IS.
    The Partial band is a whole-success-wide window rather
    than the single point `margin == 0`, which is what the same rule reduces to on integers
    (`floor(margin) == 0`) — the two readings agree everywhere the game rolls whole dice, and
    only the windowed one survives contact with fractional obstacles, where exact equality
    essentially never occurs and Partial would otherwise vanish.

    RULED OUT, explicitly, by the same ruling (all three were live here until 2026-08-14):
      * Ob-scaled Overwhelming (`net >= 2*Ob`) — Overwhelming no longer depends on difficulty.
      * The separate PP-232 `net >= 3` floor — subsumed; the margin bar IS 3.
      * The Ob-20 exception (Overwhelming unavailable, Partial needing net >= 10) — "always"
        admits no ceiling case.

    Behaviour change, stated rather than buried (CLAUDE.md 0.1 point 4): the Partial band was
    `0 < net < Ob`, so a roll that cleared zero but fell far short of a hard obstacle read as a
    Partial. It now reads as a Failure. Partial is the near-miss-by-nothing outcome, not the
    tried-and-failed one. Measured deltas are in the ED-IN-0187 ledger entry.
    """
    margin = net - ob
    if margin < 0:
        return Degree.FAILURE
    if margin < 1:
        return Degree.PARTIAL
    if margin >= 3:
        return Degree.OVERWHELMING
    return Degree.SUCCESS


def degree_label(net: int | float, ob: int | float) -> str:
    """`degree_from_net` in the Title-Case string vocabulary. Convenience, not a second ladder."""
    return DEGREE_LABEL[degree_from_net(net, ob)]
