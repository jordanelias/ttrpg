"""
sim/autoload/game_state.py — Global mutable state container — factions, territories, world tracks, season counter

Canon source: designs/architecture/complete_systems_reference.md (Part 7 + Part 8)
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17]

Dependencies:
  - none — root primitive

Entry points:
  - get_state() -> GameState
  - reset_state(seed: int | None = None) -> GameState
  - serialize_state(state: GameState) -> dict
  - restore_state(snapshot: dict) -> GameState

"""
from __future__ import annotations

# [PROVISIONAL — Pass 2l armature stub; implementation pending against canonical source]


def get_state():
    raise NotImplementedError("sim/autoload/game_state.py — Pass 2l armature stub")


def reset_state(seed: int | None = None):
    raise NotImplementedError("sim/autoload/game_state.py — Pass 2l armature stub")


def serialize_state(state: GameState):
    raise NotImplementedError("sim/autoload/game_state.py — Pass 2l armature stub")


def restore_state(snapshot: dict):
    raise NotImplementedError("sim/autoload/game_state.py — Pass 2l armature stub")

