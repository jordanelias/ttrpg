"""
sim/personal/conviction.py — Conviction Scar tracking, Conviction shifts, Belief integration

Canon source: designs/scene/conviction_track_v30.md (sections 1-3 + 5 remain canonical post-GD-1)
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17 (sections 4.2, 4.3, 6, 7 of conviction_track_v30 SUPERSEDED-BY GD-1; this module implements only the surviving conviction-tracking mechanics)]

Dependencies:
  - sim/personal/beliefs

Entry points:
  - apply_conviction_scar(actor, source: str, magnitude: int) -> ScarRecord
  - check_conviction_threshold(actor) -> ConvictionState

"""
from __future__ import annotations

# [PROVISIONAL — Pass 2l armature stub; implementation pending against canonical source]


def apply_conviction_scar(actor, source: str, magnitude: int):
    raise NotImplementedError("sim/personal/conviction.py — Pass 2l armature stub")


def check_conviction_threshold(actor):
    raise NotImplementedError("sim/personal/conviction.py — Pass 2l armature stub")
