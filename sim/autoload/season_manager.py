"""
sim/autoload/season_manager.py — Season-loop orchestration

Canon source: designs/architecture/campaign_architecture_v30.md; mc_v17.py L691-710
Status: [CANONICAL — Phase 1 implementation 2026-05-17]

Arc structure: 4 seasons per arc (mc_v17 L694: season % 4 == 1 triggers new arc).

Dependencies:
  - sim/autoload/game_state

Entry points:
  - advance_season(world) -> SeasonResult
  - check_arc_boundary(season: int) -> bool
"""
from __future__ import annotations

from dataclasses import dataclass


SEASONS_PER_ARC = 4


@dataclass
class SeasonResult:
    season: int
    arc: int
    new_arc: bool


def advance_season(world) -> SeasonResult:
    """Advance the world by one season. Returns season metadata."""
    world.season += 1
    new_arc = (world.season % SEASONS_PER_ARC == 1)
    if new_arc:
        world.arc += 1
        # Reset per-arc faction flags
        for f in world.factions.values():
            f.reset_arc()
    # Reset per-season faction flags
    for f in world.factions.values():
        f.reset_seasonal()
    return SeasonResult(season=world.season, arc=world.arc, new_arc=new_arc)


def check_arc_boundary(season: int) -> bool:
    """True if this season is the first of a new arc."""
    return season % SEASONS_PER_ARC == 1
