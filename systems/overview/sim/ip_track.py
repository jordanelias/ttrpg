"""
sim/peninsular/ip_track.py — Altonian Imperial Pressure world-track

Canon source: designs/provincial/peninsular_strain_v30.md
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17]

Dependencies:
  - sim/autoload/game_state
  - sim/provincial/altonian_reinforcements

Entry points:
  - apply_ip_delta(delta: int, source: str, world: GameState) -> int
  - check_phased_occupation_threshold(world: GameState) -> bool

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


def apply_ip_delta(delta: int, source: str, world: GameState):
    return stubwire.stub_resolve(
        'systems.overview.sim.ip_track',
        'apply_ip_delta(delta: int, source: str, world: GameState) -> int',
        reason='Pass 2l armature stub, implementation pending against canonical source '
               '(designs/provincial/peninsular_strain_v30.md); OI-17, ED-IN-0091 plan §2.2')


def check_phased_occupation_threshold(world: GameState):
    return stubwire.stub_resolve(
        'systems.overview.sim.ip_track',
        'check_phased_occupation_threshold(world: GameState) -> bool',
        reason='Pass 2l armature stub, implementation pending against canonical source '
               '(designs/provincial/peninsular_strain_v30.md); OI-17, ED-IN-0091 plan §2.2')
