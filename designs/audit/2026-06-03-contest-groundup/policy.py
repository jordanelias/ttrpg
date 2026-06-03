"""
policy.py — decoupled policies. A policy sees a read-only ContestView and returns a Move.
It never touches a module's internals. Distinct policies let tests show each defeat-condition
firing and honest play prevailing, without entangling "how one plays" with "how it resolves".
"""
from dataclasses import dataclass
from resolver import Move
from primitives import Stasis, Appeal

@dataclass(frozen=True)
class ContestView:
    live_ground: str
    committed: str
    appeal_axis: tuple
    my_standing: float
    opp_standing: float
    can_hard: bool
    reserve_frac: float
    i: int
    n: int
    leading: bool
    audience_learned: bool
    audience_hostile: bool

def honest_advocate(v):
    """Stays on the live ground, honest tactics, regroups when low. Incurs no defeat-condition."""
    if v.reserve_frac < 0.3:
        return Move("support")
    return Move("advance", Appeal.LOGOS, v.live_ground)

def fallback_ladder(v):
    """Honest, but climbs to a stronger stasis ground when losing — the strongest-tenable-rung defence."""
    if v.reserve_frac < 0.3:
        return Move("support")
    if not v.leading:
        idx = Stasis.LADDER.index(v.live_ground)
        if idx + 1 < len(Stasis.LADDER):
            return Move("shift", Appeal.LOGOS, Stasis.LADDER[idx + 1])
    return Move("advance", Appeal.LOGOS, v.live_ground)

def off_ground_chancer(v):
    """Argues off the live ground every other beat — courts the evasion clinch."""
    if v.i % 2 == 1:
        other = next(g for g in Stasis.LADDER if g != v.live_ground)
        return Move("advance", Appeal.LOGOS, other)
    return Move("advance", Appeal.LOGOS, v.live_ground)

def overreacher(v):
    """Reaches for a hard device regardless of licence — courts the barred-device clinch."""
    return Move("hard", Appeal.PATHOS, v.live_ground)

def staller(v):
    """Passes — courts the silence clinch."""
    return Move("pass")

POLICIES = {"honest": honest_advocate, "fallback": fallback_ladder,
            "off_ground": off_ground_chancer, "overreacher": overreacher, "staller": staller}
