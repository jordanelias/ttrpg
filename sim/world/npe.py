"""
sim/world/npe.py — NPC Population Engine

Canon source: designs/scene/investigation_systems_v30.md (NPE)
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17]

Dependencies:
  - sim/autoload/game_state

Entry points:
  - generate_npc(faction: str | None, role: str | None, world: GameState) -> NPC
  - simulate_npc_actions(world: GameState) -> list[NPCAction]

"""
from __future__ import annotations

# [PROVISIONAL — Pass 2l armature stub; implementation pending against canonical source]


def generate_npc(faction: str | None, role: str | None, world: GameState):
    raise NotImplementedError("sim/world/npe.py — Pass 2l armature stub")


def simulate_npc_actions(world: GameState):
    raise NotImplementedError("sim/world/npe.py — Pass 2l armature stub")
