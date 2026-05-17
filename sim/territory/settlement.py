"""
sim/territory/settlement.py — Settlement-level state — Order, Prosperity, Population

Canon source: designs/territory/settlement_layer_v30.md
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17]

Dependencies:
  - sim/autoload/game_state

Entry points:
  - compute_settlement_state(settlement_id: str, world: GameState) -> SettlementState
  - aggregate_to_province(province_id: str, world: GameState) -> ProvinceState

"""
from __future__ import annotations

# [PROVISIONAL — Pass 2l armature stub; implementation pending against canonical source]


def compute_settlement_state(settlement_id: str, world: GameState):
    raise NotImplementedError("sim/territory/settlement.py — Pass 2l armature stub")


def aggregate_to_province(province_id: str, world: GameState):
    raise NotImplementedError("sim/territory/settlement.py — Pass 2l armature stub")
