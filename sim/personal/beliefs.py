"""
sim/personal/beliefs.py — Belief revision system

Canon source: designs/scene/fieldwork_v30.md §5.5; designs/scene/social_contest_v30.md §9.5; designs/articulation/articulation_layer_v30.md §3.5
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17 (cross-doc system — unification target similar to knots; defer to a future synthesis pass)]

Dependencies:
  - sim/personal/conviction

Entry points:
  - revise_belief(actor, belief_id: str, new_position: str, evidence) -> RevisionResult
  - get_active_beliefs(actor) -> list[Belief]

"""
from __future__ import annotations

# [PROVISIONAL — Pass 2l armature stub; implementation pending against canonical source]


def revise_belief(actor, belief_id: str, new_position: str, evidence):
    raise NotImplementedError("sim/personal/beliefs.py — Pass 2l armature stub")


def get_active_beliefs(actor):
    raise NotImplementedError("sim/personal/beliefs.py — Pass 2l armature stub")
