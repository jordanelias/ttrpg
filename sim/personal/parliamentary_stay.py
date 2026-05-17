"""
sim/personal/parliamentary_stay.py — Parliamentary Stay procedure (motion-pause mechanism)

Canon source: designs/scene/social_contest_v30.md §10.1 ED-631
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17]

Dependencies:
  - sim/personal/parliamentary_vote

Entry points:
  - invoke_stay(motion: Motion, invoker_id: str, world: GameState) -> StayResult
  - resolve_stay_lift(stay: StayResult, world: GameState) -> bool

"""
from __future__ import annotations

# [PROVISIONAL — Pass 2l armature stub; implementation pending against canonical source]


def invoke_stay(motion: Motion, invoker_id: str, world: GameState):
    raise NotImplementedError("sim/personal/parliamentary_stay.py — Pass 2l armature stub")


def resolve_stay_lift(stay: StayResult, world: GameState):
    raise NotImplementedError("sim/personal/parliamentary_stay.py — Pass 2l armature stub")
