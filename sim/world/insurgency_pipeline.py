"""
sim/world/insurgency_pipeline.py — Revolt → Insurgency → Faction emergence pipeline (GD-3)

Canon source: canon/02_canon_constraints.md §B GD-3; designs/world/insurgency_pipeline_v30.md (canon authoring pending Pass 2i)
Game Design constraints applicable: GD-3
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17 (GD-3 enforcement boundary. Insurgency state machine: disorganized → emergent → extra-parliamentary | parliamentary)]

Dependencies:
  - sim/autoload/game_state
  - sim/territory/adjacency

Entry points:
  - check_insurgency_triggers(world: GameState) -> list[InsurgencyEvent]
  - check_insurgency_promotion(insurgency_id: str, world: GameState) -> PromotionResult

"""
from __future__ import annotations

# [PROVISIONAL — Pass 2l armature stub; implementation pending against canonical source]


def check_insurgency_triggers(world: GameState):
    raise NotImplementedError("sim/world/insurgency_pipeline.py — Pass 2l armature stub")


def check_insurgency_promotion(insurgency_id: str, world: GameState):
    raise NotImplementedError("sim/world/insurgency_pipeline.py — Pass 2l armature stub")
