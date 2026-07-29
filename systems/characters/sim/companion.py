"""
sim/personal/companion.py — Companion scene resolution

Canon source: godot/scene_tree_architecture.md (CompanionScene)
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17]

Dependencies:
  - sim/personal/contest
  - sim/personal/fieldwork

Entry points:
  - run_companion_scene(scene) -> CompanionResult

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


def run_companion_scene(scene):
    return stubwire.stub_resolve(
        'systems.characters.sim.companion',
        'run_companion_scene(scene) -> CompanionResult',
        reason='Pass 2l armature stub, implementation pending against canonical source '
               '(godot/scene_tree_architecture.md CompanionScene); OI-17, ED-IN-0091 plan §2.2')
