"""
sim/autoload/victory.py — Victory check — peninsular_sovereignty is the SOLE victory function per GD-1

Canon source: canon/02_canon_constraints.md §B GD-1; designs/provincial/victory_v30.md §0
Game Design constraints applicable: GD-1
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17 (GD-1 enforcement boundary: this module is the only place in sim that returns a game-end faction-victory result)]

Dependencies:
  - sim/autoload/game_state

Entry points:
  - peninsular_sovereignty(faction_id: str, world: GameState) -> VictoryResult
  - check_all_factions(world: GameState) -> list[VictoryResult]

"""
from __future__ import annotations

# [PROVISIONAL — Pass 2l armature stub; implementation pending against canonical source]


def peninsular_sovereignty(faction_id: str, world: GameState):
    raise NotImplementedError("sim/autoload/victory.py — Pass 2l armature stub")


def check_all_factions(world: GameState):
    raise NotImplementedError("sim/autoload/victory.py — Pass 2l armature stub")

