"""
sim/autoload/npc_ai.py — NPC priority trees, action selection, faction AI dispatch

Canon source: designs/architecture/complete_systems_reference.md Part 1 (NAMED NPCs)
Game Design constraints applicable: GD-2
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17 (priority-stack contents may contain contamination per Jordan diagnosis 2026-05-17 — audit pending before content authoring)]

Dependencies:
  - sim/autoload/game_state
  - systems/factions/sim/faction_action

Entry points:
  - select_action(actor_id: str, world: GameState) -> Action
  - evaluate_priority_stack(actor_id: str, world: GameState) -> list[Action]

"""
from __future__ import annotations

from engine.substrate import stubwire

# [PROVISIONAL — Pass 2l armature stub; implementation pending against canonical source]
#
# OI-17 (ED-IN-0091 plan §2.2/§3 Wave 1): converted from an unconditional
# `raise NotImplementedError` to the single-owner stub-wire primitive (engine/substrate/stubwire.py,
# plan §2.1) — a typed no-op instead of a crash, visible to structure_audit's `stub_wired`
# attribute and review_core's `stubs.count` ratchet by construction (greppable import, no second
# registry). `io_contract` below cites this module's own docstring "Entry points" declaration.
#
# Status note carried forward unchanged: priority-stack contents may contain contamination per
# Jordan diagnosis 2026-05-17 — audit pending before content authoring.


def select_action(actor_id: str, world: GameState):
    return stubwire.stub_resolve(
        'engine.autoload.npc_ai',
        'select_action(actor_id: str, world: GameState) -> Action',
        reason='Pass 2l armature stub, implementation pending against canonical source '
               '(designs/architecture/complete_systems_reference.md Part 1); OI-17, ED-IN-0091 plan §2.2')


def evaluate_priority_stack(actor_id: str, world: GameState):
    return stubwire.stub_resolve(
        'engine.autoload.npc_ai',
        'evaluate_priority_stack(actor_id: str, world: GameState) -> list[Action]',
        reason='Pass 2l armature stub, implementation pending against canonical source '
               '(designs/architecture/complete_systems_reference.md Part 1); OI-17, ED-IN-0091 plan §2.2')

