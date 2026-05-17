"""
sim/provincial/infrastructure_reclamation.py — Church Infrastructure-Backed Reclamation — invasion bonus from existing Church infrastructure + piety

Canon source: designs/provincial/infrastructure_reclamation_v30.md (canon authoring pending Pass 2f)
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17 (Pass 2f canon authoring pending faction contamination audit. Jordan 2026-05-17 directive: when Church invades territory with existing Religious Buildings / Templar Stations / Inquisitor Bases, attacker pool +(infra_count + max(0, PT-3)), defender pool -min(3, floor(bonus/2)))]

Dependencies:
  - sim/provincial/massbattle
  - sim/territory/infrastructure

Entry points:
  - compute_reclamation_bonus(target_territory: str, world: GameState) -> ReclamationBonus

"""
from __future__ import annotations

# [PROVISIONAL — Pass 2l armature stub; implementation pending against canonical source]


def compute_reclamation_bonus(target_territory: str, world: GameState):
    raise NotImplementedError("sim/provincial/infrastructure_reclamation.py — Pass 2l armature stub")
