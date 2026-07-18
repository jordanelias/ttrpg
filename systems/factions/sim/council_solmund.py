"""
systems/factions/sim/council_solmund.py — Council of Solmund — rare 1/arc gathering

Canon source: designs/audit/2026-05-14-balance-audit/part10_crown_initiative_design_2026-05-14.md §5.1
Game Design constraints applicable: GD-2 (Church faction-unique action)
Status: [PROVISIONAL — Phase 5/9 integration 2026-05-17. 1/arc cooldown via
         Faction.council_used_this_arc flag (reset by season_manager.advance_season
         when SeasonResult.new_arc). Cardinal Focus effect logged but not state-
         mutating — Cardinal Focus track not in v18 schema.]

Dependencies:
  - sim/autoload/dice_engine
  - sim/autoload/game_state
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field

from engine.autoload import dice_engine
from engine.autoload.dice_engine import Degree


_MULTS_L = 20  # [canonical: params/factions.md]
_TN = 7        # [canonical: params/core.md]

COUNCIL_OB_BASE = 2  # [canonical: part10 §5.1 — "floor(CI / 30) + 2"]


def council_ob(world) -> int:
    """Ob = floor(CI / 30) + 2 — easier when CI high [part10 §5.1]."""
    ci = world.clocks.get('CI', 0.0)
    return math.floor(ci / 30) + COUNCIL_OB_BASE


@dataclass
class CouncilResult:
    status: str
    degree: Degree | None = None
    pool_size: int = 0
    ob: float = 0.0
    net: int = 0
    rival_l_drop_target: str | None = None
    rolls: list[int] = field(default_factory=list)
    effects_applied: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)


def attempt_council(church, world, rng) -> CouncilResult:
    """Council of Solmund — Mandate +1/+2, optional rival L-1 on OW.

    1× per arc; tracked via Faction.council_used_this_arc.
    """
    if church.name != 'Church':
        return CouncilResult(status='invalid_not_church')
    if getattr(church, 'council_used_this_arc', False):
        return CouncilResult(status='invalid_used_this_arc')

    church.council_used_this_arc = True
    pool = int(church.L)  # [canonical: §5.1 — "Pool | Mandate"]
    ob = council_ob(world)

    res = dice_engine.roll_pool(pool_size=pool, tn=_TN, ob=ob, rng=rng)
    result = CouncilResult(
        status='resolved', degree=res.degree,
        pool_size=res.pool_size, ob=float(ob), net=res.net, rolls=res.rolls,
    )

    deg = res.degree
    if deg == Degree.OVERWHELMING:
        church.adjust('L', 2 * _MULTS_L)
        # Pick highest-L rival; "formal censure" -1 L
        rivals = [(fn, f) for fn, f in world.factions.items()
                  if fn != church.name and getattr(f, 'parliamentary', True)
                  and len(f.territories) > 0]
        if rivals:
            target_name, target_f = max(rivals, key=lambda kv: kv[1].L)
            target_f.adjust('L', -1 * _MULTS_L)
            result.rival_l_drop_target = target_name
            result.effects_applied.append(f"{target_name}.L -1.0 stat-tier [§5.1 OW formal censure]")
        result.effects_applied.append("Church.L +2.0 stat-tier [§5.1 OW]")
        result.notes.append("[PROVISIONAL] §5.1 'choose a Cardinal Focus permanent' not modeled — Cardinal Focus track not in v18 schema")
    elif deg == Degree.SUCCESS:
        church.adjust('L', 1 * _MULTS_L)
        result.effects_applied.append("Church.L +1.0 stat-tier [§5.1 Success]")
        result.notes.append("[PROVISIONAL] §5.1 'one Cardinal Focus permanent for this campaign' not modeled")
    elif deg == Degree.PARTIAL:
        result.effects_applied.append("Cost paid, no effect [§5.1 Partial — M6_ASSUMPTION_FIVE]")
    else:  # FAILURE
        result.effects_applied.append("Cost paid, no effect [§5.1 Failure]")

    return result
