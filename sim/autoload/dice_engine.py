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
    """Determine degree of success from net successes and Ob.

    Canon: params/core.md §Degrees of Success
      Overwhelming: net >= 2*Ob AND net >= 3 (PP-232 floor)
      Success: net >= Ob
      Partial: net > 0 but < Ob
      Failure: net <= 0
      Ob 20 exception: Overwhelming unavailable; Partial requires net >= 10
    """
    if ob >= 20:
        # Ob 20 exception
        if net >= ob:
            return Degree.SUCCESS
        elif net >= 10:
            return Degree.PARTIAL
        elif net > 0:
            return Degree.FAILURE  # net > 0 but < 10 at Ob 20 = Failure, not Partial
        else:
            return Degree.FAILURE
    # Standard degrees
    if net >= 2 * ob and net >= 3:
        return Degree.OVERWHELMING
    elif net >= ob:
        return Degree.SUCCESS
    elif net > 0:
        return Degree.PARTIAL
    else:
        return Degree.FAILURE
