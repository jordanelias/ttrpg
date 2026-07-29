"""
sim/provincial/home_sanctuary.py — Church T9 Home Sanctuary — protected build-up period at game start

Canon source: designs/provincial/home_sanctuary_t9_v30.md (canon authoring pending Pass 2f)
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17 (Pass 2f canon authoring pending faction contamination audit. Jordan 2026-05-17 directive: T9 invasion Ob +4 for first 12 seasons; ends on Church PT<3 / Church L<2.5 / any faction holds CB vs Church)]

Dependencies:
  - sim/autoload/game_state

Entry points:
  - t9_invasion_modifier(world: GameState) -> int
  - check_sanctuary_active(world: GameState) -> bool

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
# Design gate: canon authoring pending Pass 2f faction contamination audit.


def t9_invasion_modifier(world: GameState):
    return stubwire.stub_resolve(
        'systems.factions.sim.home_sanctuary',
        't9_invasion_modifier(world: GameState) -> int',
        reason='Pass 2l armature stub, design-gated on Pass 2f canon authoring pending faction '
               'contamination audit; OI-17, ED-IN-0091 plan §2.2')


def check_sanctuary_active(world: GameState):
    return stubwire.stub_resolve(
        'systems.factions.sim.home_sanctuary',
        'check_sanctuary_active(world: GameState) -> bool',
        reason='Pass 2l armature stub, design-gated on Pass 2f canon authoring pending faction '
               'contamination audit; OI-17, ED-IN-0091 plan §2.2')
