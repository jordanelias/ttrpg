"""
policy.py — decoupled policies. A policy sees a read-only ContestView (from contract) and returns a
Move (from contract). It imports no resolver internals — the contract module breaks the old cycle.
"""
from contract import Move, ContestView
from primitives import Stasis, Appeal

def honest_advocate(v):
    """Stays on the live ground, honest logos, regroups when low. Incurs no defeat-condition."""
    if v.reserve_frac < 0.3:
        return Move("support")
    return Move("advance", Appeal.LOGOS, v.live_ground)

def tactician(v):
    """Build standing (ethos) and the room (pathos) early, then close on logos — a build-then-close."""
    if v.reserve_frac < 0.3:
        return Move("support")
    if v.i < v.n // 2:
        return Move("advance", Appeal.ETHOS if v.i % 2 == 0 else Appeal.PATHOS, v.live_ground)
    return Move("advance", Appeal.LOGOS, v.live_ground)

def pure_ethos(v):
    """Only ethos — never advances the verdict; used to show the appeal axis is live."""
    return Move("advance", Appeal.ETHOS, v.live_ground)

def fallback_ladder(v):
    """Honest; climbs to a stronger stasis ground when losing — the strongest-tenable-rung defence."""
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
        other_g = next(g for g in Stasis.LADDER if g != v.live_ground)
        return Move("advance", Appeal.LOGOS, other_g)
    return Move("advance", Appeal.LOGOS, v.live_ground)

def overreacher(v):
    """Reaches for a hard device regardless of licence — courts the barred-device clinch."""
    return Move("hard", Appeal.PATHOS, v.live_ground)

def staller(v):
    """Passes — courts the silence clinch."""
    return Move("pass")

POLICIES = {"honest": honest_advocate, "tactician": tactician, "pure_ethos": pure_ethos,
            "fallback": fallback_ladder, "off_ground": off_ground_chancer,
            "overreacher": overreacher, "staller": staller}
