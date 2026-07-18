"""
sim/autoload/npc_ai.py — NPC priority trees, action selection, faction AI dispatch

Canon source: designs/architecture/complete_systems_reference.md Part 1 (NAMED NPCs)
Game Design constraints applicable: GD-2
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17 (priority-stack contents may contain contamination per Jordan diagnosis 2026-05-17 — audit pending before content authoring)]

Dependencies:
  - sim/autoload/game_state
  - systems/factions/sim/faction_action

Entry points:
  - select_action(actor_id: str, world: GameState) -> Action
  - evaluate_priority_stack(actor_id: str, world: GameState) -> list[Action]

"""
from __future__ import annotations

# [PROVISIONAL — Pass 2l armature stub; implementation pending against canonical source]


def select_action(actor_id: str, world: GameState):
    raise NotImplementedError("sim/autoload/npc_ai.py — Pass 2l armature stub")


def evaluate_priority_stack(actor_id: str, world: GameState):
    raise NotImplementedError("sim/autoload/npc_ai.py — Pass 2l armature stub")

