"""
sim/world/restoration_movement.py — Restoration Movement world-level PT decay + emergence

Canon source: designs/audit/2026-05-14-balance-audit/faction_balance_convergence_v12c_2026-05-14.md §4.2 (PT decay validated N=1000); designs/provincial/restoration_movement_v30.md (canon authoring pending Pass 2d)
Game Design constraints applicable: GD-3
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17 (Pass 2d canon authoring pending. v12c mechanic: 0.35 chance/arc per non-Church / non-Inquisitor-held territory, PT -1; Varfell-cooopt multiplier (validated N=1000))]

Dependencies:
  - sim/autoload/game_state
  - sim/world/insurgency_pipeline

Entry points:
  - process_rm_pt_decay(world: GameState) -> list[PTDecayEvent]
  - check_rm_emergence_trigger(world: GameState) -> RMEmergenceResult

"""
from __future__ import annotations

# [PROVISIONAL — Pass 2l armature stub; implementation pending against canonical source]


def process_rm_pt_decay(world: GameState):
    raise NotImplementedError("sim/world/restoration_movement.py — Pass 2l armature stub")


def check_rm_emergence_trigger(world: GameState):
    raise NotImplementedError("sim/world/restoration_movement.py — Pass 2l armature stub")
