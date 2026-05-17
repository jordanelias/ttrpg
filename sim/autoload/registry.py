"""
sim/autoload/registry.py — mechanics_index.yaml loader and mechanic-by-id dispatch

Canon source: canon/mechanics_index.yaml (pending Pass 2j)
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17]

Dependencies:
  - none — root primitive

Entry points:
  - load_index(path: str = "canon/mechanics_index.yaml") -> MechanicsIndex
  - get_mechanic(name: str) -> MechanicEntry
  - mechanics_by_scale(scale: str) -> list[MechanicEntry]
  - mechanics_by_faction(faction: str) -> list[MechanicEntry]

"""
from __future__ import annotations

# [PROVISIONAL — Pass 2l armature stub; implementation pending against canonical source]


def load_index(path: str = "canon/mechanics_index.yaml"):
    raise NotImplementedError("sim/autoload/registry.py — Pass 2l armature stub")


def get_mechanic(name: str):
    raise NotImplementedError("sim/autoload/registry.py — Pass 2l armature stub")


def mechanics_by_scale(scale: str):
    raise NotImplementedError("sim/autoload/registry.py — Pass 2l armature stub")


def mechanics_by_faction(faction: str):
    raise NotImplementedError("sim/autoload/registry.py — Pass 2l armature stub")

