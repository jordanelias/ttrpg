"""
sim/provincial/units.py — Unit classes — Levy, LightInf, HeavyInf, Cavalry with Martial / Endurance / Discipline stats

Canon source: designs/scene/combat_v30.md §11 (Faction Unit Rosters); designs/provincial/mass_battle_v30.md
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17]

Dependencies:
  - sim/autoload/dice_engine

Entry points:
  - spawn_unit(faction: str, unit_type: str, size: int) -> Unit
  - apply_casualties(unit: "Unit", losses: int) -> "Unit"

"""
from __future__ import annotations

# [PROVISIONAL — Pass 2l armature stub; implementation pending against canonical source]


def spawn_unit(faction: str, unit_type: str, size: int):
    raise NotImplementedError("sim/provincial/units.py — Pass 2l armature stub")


def apply_casualties(unit: "Unit", losses: int):
    raise NotImplementedError("sim/provincial/units.py — Pass 2l armature stub")
