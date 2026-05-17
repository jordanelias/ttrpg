"""
sim/thread/coherence.py — Coherence 10→0 track per Foundations P-10, P-15

Canon source: designs/threadwork/threadwork_v30.md Part 3; canon/02_canon_constraints.md §A P-10 / P-15
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17]

Dependencies:
  - sim/autoload/game_state

Entry points:
  - apply_coherence_delta(actor: str, delta: int, source: str, world: GameState) -> CoherenceState
  - check_coherence_zero_transition(actor: str, world: GameState) -> ZeroTransitionResult

"""
from __future__ import annotations

# [PROVISIONAL — Pass 2l armature stub; implementation pending against canonical source]


def apply_coherence_delta(actor: str, delta: int, source: str, world: GameState):
    raise NotImplementedError("sim/thread/coherence.py — Pass 2l armature stub")


def check_coherence_zero_transition(actor: str, world: GameState):
    raise NotImplementedError("sim/thread/coherence.py — Pass 2l armature stub")
