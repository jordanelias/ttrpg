"""
systems/factions/sim/charter_liberties.py — Hafenmark Charter of Liberties

Canon source: systems/factions/faction_canon_v30.md §6
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17]

Dependencies:
  - sim/autoload/dice_engine

Entry points:
  - attempt_charter(world: GameState) -> CharterResult

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


def attempt_charter(world: GameState):
    return stubwire.stub_resolve(
        'systems.factions.sim.charter_liberties',
        'attempt_charter(world: GameState) -> CharterResult',
        reason='Pass 2l armature stub, implementation pending against canonical source '
               '(systems/factions/faction_canon_v30.md §6); OI-17, ED-IN-0091 plan §2.2')
