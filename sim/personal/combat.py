"""
sim/personal/combat.py — Personal combat resolution

Canon source: designs/scene/combat_v30.md
Params source: params/combat.md
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17]

Dependencies:
  - sim/autoload/dice_engine
  - sim/cross_scale/handoff_rules

Entry points:
  - resolve_combat_round(participants: list, scene: CombatScene) -> RoundResult
  - resolve_action(actor, target, action_type: str) -> ActionResult

"""
from __future__ import annotations

# [PROVISIONAL — Pass 2l armature stub; implementation pending against canonical source]


def resolve_combat_round(participants: list, scene: CombatScene):
    raise NotImplementedError("sim/personal/combat.py — Pass 2l armature stub")


def resolve_action(actor, target, action_type: str):
    raise NotImplementedError("sim/personal/combat.py — Pass 2l armature stub")
