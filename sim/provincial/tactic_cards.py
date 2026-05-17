"""
sim/provincial/tactic_cards.py — Tactic cards — pool modifiers, conditional effects, faction-restricted cards

Canon source: designs/provincial/mass_battle_v30.md; tests/sim/v17-integration/m6_faction_actions.py FACTION_TACTIC_CARD_POOL_MODIFIERS
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17 (card pool contents may include Claude-overreach contamination per Jordan diagnosis 2026-05-17 — audit pending before content authoring)]

Dependencies:
  - sim/provincial/massbattle

Entry points:
  - available_cards(faction: str, context: dict) -> list[TacticCard]
  - apply_card(card: "TacticCard", battle_state: dict) -> dict

"""
from __future__ import annotations

# [PROVISIONAL — Pass 2l armature stub; implementation pending against canonical source]


def available_cards(faction: str, context: dict):
    raise NotImplementedError("sim/provincial/tactic_cards.py — Pass 2l armature stub")


def apply_card(card: "TacticCard", battle_state: dict):
    raise NotImplementedError("sim/provincial/tactic_cards.py — Pass 2l armature stub")
