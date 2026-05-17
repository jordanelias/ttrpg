"""
sim/autoload/victory.py — Victory check — peninsular_sovereignty is the SOLE victory function per GD-1

Canon source: canon/02_canon_constraints.md §B GD-1; designs/provincial/victory_v30.md §0
Game Design constraints applicable: GD-1
Status: [CANONICAL — Phase 1 implementation 2026-05-17]

GD-1 enforcement: this module is the only place in sim that returns a game-end
faction-victory result. No other victory function may be registered.

Victory condition (GD-1):
  Control 11+ of 15 territories, Accord >= 2 in all held, Political Stability <= 6,
  sustained for 2 consecutive seasons.

Dependencies:
  - sim/autoload/game_state

Entry points:
  - check_peninsular_sovereignty(faction_id, world) -> VictoryResult
  - check_all_factions(world) -> list[VictoryResult]
"""
from __future__ import annotations

from dataclasses import dataclass, field


VICTORY_THRESHOLD = 11   # 11 of 15 territories
ACCORD_MIN = 2.0
PS_MAX = 6.0
SUSTAIN_SEASONS = 2


@dataclass
class VictoryResult:
    faction_id: str
    won: bool
    held: int
    qualifies_this_season: bool
    consecutive_qualifying: int
    reason: str = ""


# Track consecutive qualifying seasons per faction (module-level, reset per campaign)
_qualifying_streak: dict[str, int] = {}


def reset():
    """Reset victory tracking for a new campaign."""
    _qualifying_streak.clear()


def check_peninsular_sovereignty(faction_id: str, world) -> VictoryResult:
    """Check if faction meets GD-1 peninsular sovereignty victory.

    Canon: 11/15 territories held, Accord >= 2 in all, PS <= 6, sustained 2 seasons.
    """
    from sim.autoload.game_state import ALL_PLAYABLE_15

    faction = world.factions.get(faction_id)
    if faction is None:
        return VictoryResult(faction_id=faction_id, won=False, held=0,
                             qualifies_this_season=False, consecutive_qualifying=0,
                             reason="faction not found")

    held_tids = [tid for tid in ALL_PLAYABLE_15
                 if tid in world.territories and world.territories[tid].owner == faction_id]
    held = len(held_tids)

    # Check all conditions
    territory_count_ok = held >= VICTORY_THRESHOLD
    accord_ok = all(world.territories[tid].accord >= ACCORD_MIN for tid in held_tids) if held_tids else False
    # Political Stability is a world clock
    ps = world.clocks.get('Turmoil', 0.0)  # PS mapped to Turmoil clock
    ps_ok = ps <= PS_MAX

    qualifies = territory_count_ok and accord_ok and ps_ok

    if qualifies:
        _qualifying_streak[faction_id] = _qualifying_streak.get(faction_id, 0) + 1
    else:
        _qualifying_streak[faction_id] = 0

    consecutive = _qualifying_streak.get(faction_id, 0)
    won = consecutive >= SUSTAIN_SEASONS

    reason = ""
    if not territory_count_ok:
        reason = f"held {held}/{VICTORY_THRESHOLD}"
    elif not accord_ok:
        reason = "accord < 2 in some territories"
    elif not ps_ok:
        reason = f"political stability {ps} > {PS_MAX}"
    elif not won:
        reason = f"qualifying {consecutive}/{SUSTAIN_SEASONS} seasons"

    return VictoryResult(
        faction_id=faction_id, won=won, held=held,
        qualifies_this_season=qualifies, consecutive_qualifying=consecutive,
        reason=reason,
    )


def check_all_factions(world) -> list[VictoryResult]:
    """Check all factions for victory. Returns list of results, winners first."""
    results = []
    for faction_id in world.factions:
        r = check_peninsular_sovereignty(faction_id, world)
        results.append(r)
    results.sort(key=lambda r: (-int(r.won), -r.held))
    return results
