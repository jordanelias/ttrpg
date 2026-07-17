"""
sim/provincial/absolution.py — Church Absolution faction-unique action

Canon source:
  - designs/provincial/faction_canon_v30.md §8.2 (Recovery paths — Church Absolution +1 Stab to target)
  - designs/provincial/faction_canon_v30.md §8.3 Stability Profile ("at cost of 1 Mandate")
  - tests/sim/v17-integration/m6_faction_actions.py (M6_ASSUMPTION_ONE — Pool=I, Ob=3)
Game Design constraints applicable: GD-2 (Church faction-unique action)
Status: [PROVISIONAL — Phase 5/9 integration 2026-05-17. §8.2 canon specifies the
         +1 Stability effect; Pool/Ob/cost are M6_ASSUMPTION_ONE values. Surface
         for ratification.]

Dependencies:
  - sim/autoload/dice_engine
  - sim/autoload/game_state
"""
from __future__ import annotations

from dataclasses import dataclass, field

from engine.autoload import dice_engine
from engine.autoload.dice_engine import Degree


# ── Granular conversion ───────────────────────────────────────────────────────
_MULTS_L = 20    # [canonical: params/factions.md]
_MULTS_STA = 10  # [canonical: params/factions.md]
_TN = 7          # [canonical: params/core.md]


# ── M6_ASSUMPTION_ONE constants ──────────────────────────────────────────────
ABSOLUTION_OB = 3  # [M6_ASSUMPTION_ONE: faction_canon §8.2 specifies +1 Stab effect, M6 declares Ob=3]
ABSOLUTION_CHURCH_L_COST = -1  # [canonical: faction_canon §8.3 — "at cost of 1 Mandate"]
ABSOLUTION_TARGET_STA_BONUS = 1  # [canonical: faction_canon §8.2 — "+1 to target"]


@dataclass
class AbsolutionResult:
    status: str
    degree: Degree | None = None
    target_name: str | None = None
    pool_size: int = 0
    ob: float = 0.0
    net: int = 0
    rolls: list[int] = field(default_factory=list)
    effects_applied: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)


def attempt_absolution(church, target_faction, world, rng) -> AbsolutionResult:
    """Church Absolution — recovery action granting +1 Stability to target.

    Pool = Church.I. Ob = 3 [M6_ASSUMPTION_ONE]. Cost = Church.L -1 regardless.
    """
    if church.name != 'Church':
        return AbsolutionResult(status='invalid_not_church')
    if target_faction is None or not getattr(target_faction, 'parliamentary', True):
        return AbsolutionResult(status='invalid_no_target')
    if target_faction.name == church.name:
        return AbsolutionResult(status='invalid_no_target',
                                notes=["Cannot absolve self"])

    pool = int(church.I)
    res = dice_engine.roll_pool(pool_size=pool, tn=_TN, ob=ABSOLUTION_OB, rng=rng)
    result = AbsolutionResult(
        status='resolved', degree=res.degree, target_name=target_faction.name,
        pool_size=res.pool_size, ob=float(ABSOLUTION_OB), net=res.net, rolls=res.rolls,
    )

    # Cost paid regardless (institutional capital spent on ceremony)
    church.adjust('L', ABSOLUTION_CHURCH_L_COST * _MULTS_L)
    result.effects_applied.append(f"Church.L -1.0 stat-tier [§8.3 cost]")

    deg = res.degree
    if deg == Degree.OVERWHELMING:
        # M6: doubles to +2 Stab on OW
        target_faction.adjust('Sta', 2 * _MULTS_STA)
        result.effects_applied.append(f"{target_faction.name}.Sta +2.0 stat-tier [§8.2 OW]")
    elif deg == Degree.SUCCESS:
        target_faction.adjust('Sta', ABSOLUTION_TARGET_STA_BONUS * _MULTS_STA)
        result.effects_applied.append(f"{target_faction.name}.Sta +1.0 stat-tier [§8.2 Success]")
    elif deg == Degree.PARTIAL:
        result.effects_applied.append("Cost paid, no target effect [Partial]")
    else:  # FAILURE
        church.standing -= 1
        result.effects_applied.append("Church.standing -1 [Failure: public ceremony failed]")

    return result


def select_absolution_target(church, world, rng):
    """Heuristic: pick the lowest-Stability non-Church parliamentary faction
    that is NOT excommunicated (excomm targets cannot be absolved without lifting
    excomm first per §9 reversal rules; v18 simplification).
    """
    candidates = [
        f for fn, f in world.factions.items()
        if fn != church.name
        and getattr(f, 'parliamentary', True)
        and not getattr(f, 'excommunicated', False)
        and len(f.territories) > 0
    ]
    if not candidates:
        return None
    candidates.sort(key=lambda f: f.Sta)
    return candidates[0]
