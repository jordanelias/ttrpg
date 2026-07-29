"""
systems/factions/sim/infrastructure_reclamation.py — Church Infrastructure-Backed Reclamation — invasion bonus from existing Church infrastructure + piety

Canon source: designs/provincial/infrastructure_reclamation_v30.md (canon authoring pending Pass 2f)
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17 (Pass 2f canon authoring pending faction contamination audit. Jordan 2026-05-17 directive: when Church invades territory with existing Religious Buildings / Templar Stations / Inquisitor Bases, attacker pool +(infra_count + max(0, PT-3)), defender pool -min(3, floor(bonus/2)))]

Dependencies:
  - sim/provincial/massbattle
  - systems/settlements/sim/infrastructure

Entry points:
  - compute_reclamation_bonus(target_territory: str, world: GameState) -> ReclamationBonus

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


def compute_reclamation_bonus(target_territory: str, world: GameState):
    return stubwire.stub_resolve(
        'systems.factions.sim.infrastructure_reclamation',
        'compute_reclamation_bonus(target_territory: str, world: GameState) -> ReclamationBonus',
        reason='Pass 2l armature stub, design-gated on Pass 2f canon authoring pending faction '
               'contamination audit; OI-17, ED-IN-0091 plan §2.2')
