"""
sim/provincial/treaty.py — Crown Treaties + Treaty Expiration (90-95%/arc lapse per v12c)

Canon source: designs/audit/2026-05-14-balance-audit/faction_balance_convergence_v12c_2026-05-14.md §4.5; designs/provincial/treaty_expiration_v30.md (canon authoring pending Pass 2h)
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17]

Dependencies:
  - sim/autoload/dice_engine
  - sim/autoload/season_manager

Entry points:
  - propose_treaty(parties: list, terms: dict, world: GameState) -> TreatyResult
  - process_treaty_expirations(world: GameState) -> list[ExpirationResult]

"""
from __future__ import annotations

# [PROVISIONAL — Pass 2l armature stub; implementation pending against canonical source]


def propose_treaty(parties: list, terms: dict, world: GameState):
    raise NotImplementedError("sim/provincial/treaty.py — Pass 2l armature stub")


def process_treaty_expirations(world: GameState):
    raise NotImplementedError("sim/provincial/treaty.py — Pass 2l armature stub")
