"""
systems/world/sim/restoration_movement.py — Restoration Movement world-level PT decay + emergence

Canon source: designs/audit/2026-05-14-balance-audit/faction_balance_convergence_v12c_2026-05-14.md §4.2 (PT decay validated N=1000); designs/provincial/restoration_movement_v30.md (canon authoring pending Pass 2d)
Game Design constraints applicable: GD-3
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17 (Pass 2d canon authoring pending. v12c mechanic: 0.35 chance/arc per non-Church / non-Inquisitor-held territory, PT -1; Varfell-cooopt multiplier (validated N=1000))]

Dependencies:
  - sim/autoload/game_state
  - systems/world/sim/insurgency_pipeline

Entry points:
  - process_rm_pt_decay(world: GameState) -> list[PTDecayEvent]
  - check_rm_emergence_trigger(world: GameState) -> RMEmergenceResult

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


def process_rm_pt_decay(world: GameState):
    return stubwire.stub_resolve(
        'systems.world.sim.restoration_movement',
        'process_rm_pt_decay(world: GameState) -> list[PTDecayEvent]',
        reason='Pass 2l armature stub, Pass 2d canon authoring pending '
               '(designs/provincial/restoration_movement_v30.md); OI-17, ED-IN-0091 plan §2.2')


def check_rm_emergence_trigger(world: GameState):
    return stubwire.stub_resolve(
        'systems.world.sim.restoration_movement',
        'check_rm_emergence_trigger(world: GameState) -> RMEmergenceResult',
        reason='Pass 2l armature stub, Pass 2d canon authoring pending '
               '(designs/provincial/restoration_movement_v30.md); OI-17, ED-IN-0091 plan §2.2')
