"""
sim/provincial/faction_action.py — AI action dispatch — GD-2 mandatory pass + stochastic candidate generation

Canon source: canon/02_canon_constraints.md §B GD-2; designs/provincial/faction_canon_v30.md
Params source: params/factions.md
Game Design constraints applicable: GD-2
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17 (GD-2 enforcement boundary: mandatory_actions() runs before stochastic candidate generation. Up to 3 mandatories per faction per season)]

Dependencies:
  - sim/autoload/npc_ai
  - sim/autoload/game_state

Entry points:
  - mandatory_actions(faction_id: str, world: GameState) -> list[Action]
  - select_actions(faction_id: str, world: GameState) -> list[Action]

"""
from __future__ import annotations

# [PROVISIONAL — Pass 2l armature stub; implementation pending against canonical source]


def mandatory_actions(faction_id: str, world: GameState):
    raise NotImplementedError("sim/provincial/faction_action.py — Pass 2l armature stub")


def select_actions(faction_id: str, world: GameState):
    raise NotImplementedError("sim/provincial/faction_action.py — Pass 2l armature stub")
