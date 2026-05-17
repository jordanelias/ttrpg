"""
sim/territory/infrastructure.py — Territory infrastructure — Religious Buildings, Templar Stations, Inquisitor Bases, Forts

Canon source: designs/territory/settlement_layer_v30.md; tests/sim/v17-integration/gap_analysis.md (canon-declared, not implemented)
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17 (Tier 2 gap per gap_analysis.md — canon-declared, implementation pending)]

Dependencies:
  - sim/territory/settlement

Entry points:
  - build_infrastructure(territory_id: str, infra_type: str, world: GameState) -> BuildResult
  - count_infrastructure(territory_id: str, infra_type: str | None, world: GameState) -> int

"""
from __future__ import annotations

# [PROVISIONAL — Pass 2l armature stub; implementation pending against canonical source]


def build_infrastructure(territory_id: str, infra_type: str, world: GameState):
    raise NotImplementedError("sim/territory/infrastructure.py — Pass 2l armature stub")


def count_infrastructure(territory_id: str, infra_type: str | None, world: GameState):
    raise NotImplementedError("sim/territory/infrastructure.py — Pass 2l armature stub")
