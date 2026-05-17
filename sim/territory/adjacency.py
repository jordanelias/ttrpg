"""
sim/territory/adjacency.py — Territory adjacency graph queries

Canon source: designs/territory/settlement_adjacency_v30.md; designs/territory/valoria_geography_v30.yaml
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17]

Dependencies:
  - none — root data

Entry points:
  - adjacent_territories(territory_id: str) -> list[str]
  - is_adjacent(t1: str, t2: str) -> bool
  - contiguous_owned(faction_id: str, world: GameState) -> list[list[str]]

"""
from __future__ import annotations

# [PROVISIONAL — Pass 2l armature stub; implementation pending against canonical source]


def adjacent_territories(territory_id: str):
    raise NotImplementedError("sim/territory/adjacency.py — Pass 2l armature stub")


def is_adjacent(t1: str, t2: str):
    raise NotImplementedError("sim/territory/adjacency.py — Pass 2l armature stub")


def contiguous_owned(faction_id: str, world: GameState):
    raise NotImplementedError("sim/territory/adjacency.py — Pass 2l armature stub")
