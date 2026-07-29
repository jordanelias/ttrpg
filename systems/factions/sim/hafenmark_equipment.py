"""
systems/factions/sim/hafenmark_equipment.py — Hafenmark faction-specific equipment (Wagenburg + Bombards tactic cards)

Canon source: (pending — hafenmark_equipment_v30.md not yet authored)
Params source: params/factions.md (Hafenmark section)
Game Design constraints applicable: GD-1
Status: [PROVISIONAL — Pass 3 follow-up stub 2026-05-17 (content pending contamination audit per HAFENMARK-TACTIC-EXTENSION-CONTENT-001)]

Dependencies:
  - sim/provincial/tactic_cards — tactic card pool integration

Entry points:
  - apply_hafenmark_equipment(faction_state) -> EquipmentResult

"""
from __future__ import annotations

from engine.substrate import stubwire

# [PROVISIONAL — Pass 3 follow-up stub; content pending Hafenmark contamination audit]
#
# OI-17 (ED-IN-0091 plan §2.2/§3 Wave 1): converted from an unconditional
# `raise NotImplementedError` to the single-owner stub-wire primitive (engine/substrate/stubwire.py,
# plan §2.1) — a typed no-op instead of a crash, visible to structure_audit's `stub_wired`
# attribute and review_core's `stubs.count` ratchet by construction (greppable import, no second
# registry). `io_contract` below cites this module's own docstring "Entry points" declaration.
# Design gate: content pending contamination audit (HAFENMARK-TACTIC-EXTENSION-CONTENT-001).


def apply_hafenmark_equipment(faction_state):
    return stubwire.stub_resolve(
        'systems.factions.sim.hafenmark_equipment',
        'apply_hafenmark_equipment(faction_state) -> EquipmentResult',
        reason='Pass 3 follow-up stub, content pending Hafenmark contamination audit '
               '(HAFENMARK-TACTIC-EXTENSION-CONTENT-001); OI-17, ED-IN-0091 plan §2.2')
