"""
sim/ — Valoria modular simulation armature

Mirrors the Godot scene tree (designs/godot/scene_tree_architecture.md) so that
each canonical mechanical system has a 1:1 sim-module home. Replaces the
monolithic tests/sim/v17-integration/mc_v17.py orchestrator pattern.

Subpackages:
  - autoload/    — global services (dice, state, season loop, victory)
  - personal/    — character-scale resolution (combat, contest, fieldwork, …)
  - thread/      — Thread layer operations
  - provincial/  — mass battle + faction-action layer
  - territory/   — settlement + infrastructure layer
  - peninsular/  — strategic / world-track layer
  - world/       — background processes (RM, insurgency, miraculous)
  - cross_scale/ — handoff/echo/zoom transitions between scales

Top-level orchestrator: sim/mc_v18.py

Status: [PROVISIONAL — Pass 2l armature scaffold 2026-05-17 — all modules are
stubs raising NotImplementedError; implementation work follows in subsequent
passes against canonical source docs]
"""
