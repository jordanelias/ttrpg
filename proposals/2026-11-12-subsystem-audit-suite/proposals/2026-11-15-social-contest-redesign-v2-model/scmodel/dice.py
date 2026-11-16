"""Dice primitives: LIVE ones imported from the tree; the ones the spec names and the tree lacks DERIVED from the
plan's own text (each quoting its source line). Gaps: G11-G16 in ../SPEC_GAPS.md.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Optional

import scmodel  # noqa: F401  (puts the repo on sys.path)
from engine.dice_engine import sigma_leverage as SL          # LIVE
from engine.dice_engine.dice_engine import degree_from_net  # LIVE (the one ladder)

LEVEL_SIGMA = SL.LEVEL_SIGMA          # LIVE: minor .25 moderate .5 strong .75 major 1.0
MU_PER_DIE = SL.MU_PER_DIE            # LIVE: 0.40
SD_PER_DIE = SL.SD_PER_DIE            # LIVE: 0.800
OB_MIN = SL.OB_MIN                    # LIVE: 1
net_boost = SL.net_boost              # LIVE: soft_cap(sigma) * 0.8 * sqrt(max(1, pool))
roll_net_continuous = SL.roll_net_continuous   # LIVE: rng.gauss(0.4 p, 0.8 sqrt p), pool floored at 1


def level(name: Optional[str]) -> float:
    """LIVE `sigma_leverage.level`, with the plan's rule 'a level whose setting is `None` is 0' (B24p.12)."""
    return 0.0 if name is None else SL.level(name)


# --- B04.24 (workplans/valoria_master_workplan_v12_part7.md:499-503), not in the tree -------------------------
def opposed_ob(score: float, rate: float) -> float:
    # B04.24: "def opposed_ob(score: float, rate: float) -> float: return float(rate) * max(0.0, float(score))"
    return float(rate) * max(0.0, float(score))


def even_line(pool_add: float) -> float:
    # B04.24: "def even_line(pool_add: float) -> float: return MU_PER_DIE * float(pool_add)"
    return MU_PER_DIE * float(pool_add)


def pool_of(score: float, addends: float, pool_add: float, pool_floor: float) -> float:
    # B04.24: "`pool_of(score, addends, pool_add, pool_floor) -> int` = `max(pool_floor, score + addends + pool_add)`"
    # B05.25 item 5: "`pool_of`'s `-> int` annotation, B04.24, becomes `-> float`" -- fractional, never rounded (R8). G11.
    return max(pool_floor, score + addends + pool_add)


# --- B05.25 / B24p.07 (part8.md:303; part22_b24p.md:193), not in the tree -----------------------------------
def governing_mean(scores) -> float:
    # B05.25 item 4: "`(20 * sum(scores) + n) // (2 * n) / 10` for `n = len(scores)`, refusing n outside 1 to 3"
    n = len(scores)
    assert 1 <= n <= 3 and all(s >= 0 for s in scores)
    return (20 * sum(scores) + n) // (2 * n) / 10


def weighted_tenth(scores, tenths) -> float:
    # B24p.07 item 3: "`(2 * sum(t * round(10 * s) for s, t in zip(scores, tenths)) + 10) // 20 / 10` with
    # `sum(tenths) == 10` asserted, refusing a negative score or tenth"
    assert sum(tenths) == 10, tenths
    assert all(s >= 0 for s in scores) and all(t >= 0 for t in tenths)
    return (2 * sum(t * round(10 * s) for s, t in zip(scores, tenths)) + 10) // 20 / 10


# --- B05.02 closed form (part8.md:124-131), not in the tree ---------------------------------------------------
def _phi(z: float) -> float:
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def p_at_least(pool: float, threshold: float, boost: float = 0.0) -> float:
    """P(roll_net_continuous(pool) + boost >= threshold) on the sampler's own Normal (B05.02 row 2 ASSUMPTION: mean
    MU_PER_DIE x pool plus the boost, s.d. SIGMA_PER_DIE x sqrt(pool)). The LIVE sampler floors the pool at 1; B05.02
    row 5 removes that floor. Pools here are >= pool_floor (5) except a bench seat's (G13), so the floor is read as
    the live sampler reads it (max(1, pool)) to stay equal to the draw actually taken."""
    p = max(1.0, float(pool))
    return 1.0 - _phi((threshold - boost - MU_PER_DIE * p) / (SD_PER_DIE * math.sqrt(p)))


def band_odds(pool: float, ob: float, boost: float = 0.0) -> tuple:
    """B05.02 row 2: "`band_odds(pool, ob, ...)` keeps its name and signature and returns the four band shares from
    the Normal closed form of the same sampler". The LIVE `band_odds` is still the discrete enumeration (G12).
    Band edges: the live ladder's (`degree_from_net`: margin <0 F, [0,1) P, [1,3) S, >=3 O)."""
    p0 = p_at_least(pool, ob + 0.0, boost)
    p1 = p_at_least(pool, ob + 1.0, boost)
    p3 = p_at_least(pool, ob + 3.0, boost)
    return (1.0 - p0, p0 - p1, p1 - p3, p3)


# --- B05.14 composer and record (part8_cont.md:7-23), not in the tree ----------------------------------------
@dataclass(frozen=True)
class Margin:
    """`queries/inputs.py::Margin` as B05.14 item 3 extends it: "`Margin` gains `terms: tuple`"."""
    net: float
    ob: float
    terms: tuple = ()


@dataclass(frozen=True)
class SocialContestInput:
    """The record as B05.14 item 3 leaves it: `obstacle_operands`, `difficulty`, `pool_default`, `pool_add`,
    `opposition_rate`; `obstacle_default` removed. Only the fields the composer reads are kept (G14)."""
    pool: float
    opposition: Optional[float]
    leverage: float
    difficulty: float
    obstacle_operands: tuple          # ((name, raw, step), ...) in roster order (B05.14 item 3)
    pool_default: float
    pool_add: float
    opposition_rate: float
    obstacle_ceiling: Optional[float]
    ceiling_per_pool: bool
    obstacle_refusal_multiple: float = 2.0


def _cap(pool: float, ceiling: float, per_pool: bool) -> float:
    """H-213's cap. B05.02 row 3: "`_chance_floor_cap` -- solved on the closed form (the pool's cap is the obstacle at
    which Partial-or-better equals the one-pool chance at the fixed ceiling)". On the Normal that is
    cap(p) = MU p + sqrt(p) (ceiling - MU) (one die: cap = ceiling). Row 3's second sentence ("with a signed channel the
    floor is solved at the largest lawful disadvantage") is NOT implemented: unspecified (G15)."""
    if not per_pool or pool < 1:
        return float(ceiling)
    return MU_PER_DIE * pool + math.sqrt(pool) * (float(ceiling) - MU_PER_DIE)


def obstacle(inp: SocialContestInput) -> tuple:
    """B05.14 item 4 (copied):
         hard  = even + difficulty + opposed_ob(opposition if a person opposes else pool_default, opposition_rate)
                 + sum raw_i x step_i
         ob    = max(OB_MIN, min(hard, cap(pool)))
         terms = ((name, value), ...) in roster order, + ("ceiling", -clip) and ("floor", +lift) where a bound acted
       "Every `raw_i x step_i` >= 0; a negative roster term raises `ValueError`; `terms` sum exactly to `ob`.\""""
    even = even_line(inp.pool_add)
    opp = inp.opposition if inp.opposition is not None else inp.pool_default
    terms = [("even", even), ("difficulty", float(inp.difficulty)),
             ("opposition", opposed_ob(opp, inp.opposition_rate))]
    for name, raw, step in inp.obstacle_operands:
        v = float(raw) * float(step)
        if v < 0:
            raise ValueError(f"negative obstacle term {name}={v}")
        terms.append((name, v))
    hard = sum(v for _, v in terms)
    ob = hard
    if inp.obstacle_ceiling is not None:
        cap = _cap(inp.pool, inp.obstacle_ceiling, inp.ceiling_per_pool)
        if ob > cap:
            terms.append(("ceiling", cap - ob))
            ob = cap
    if ob < OB_MIN:
        terms.append(("floor", OB_MIN - ob))
        ob = float(OB_MIN)
    return ob, tuple(terms)


def roll(inp: SocialContestInput, rng) -> Margin:
    """`roll.py::roll` as B05.02 row 1 makes it: "`roll_net(pool, rng)` -> `roll_net_continuous(pool, rng)`; the margin
    is `net + net_boost(leverage, pool) - obstacle`". ONE normal from `rng`. The LIVE roll.py still deals discrete
    d10s (`roll_net`, one randint per whole die) and composes the pre-B05.14 obstacle (G12)."""
    ob, terms = obstacle(inp)
    net = roll_net_continuous(inp.pool, rng=rng) + net_boost(inp.leverage, inp.pool)
    return Margin(net=net, ob=ob, terms=terms)


def degree(m: Margin) -> str:
    """The host's grading (`seam/ladder.py::degree_of` -> LIVE `degree_from_net`)."""
    return degree_from_net(m.net, m.ob).value      # "failure" | "partial" | "success" | "overwhelming"
