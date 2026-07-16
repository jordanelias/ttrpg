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

Status: Tier 0 stub infill in progress per proposals/stub_infill_plan.md.
17 modules implemented (Phase 7 mass battle + Crown/Church faction-unique +
autoload); Tier 0 lands the next 14 (terr/settlement, thread/coherence,
cross_scale/{handoff_rules, zoom_in_out, domain_echo}, peninsular/{ms_track,
season}, provincial/{treaty, charter_liberties, varfell_mandate_action},
world/{insurgency_pipeline, npe}, autoload/npc_ai, sim root). Tier 1+ and
canon-gated stubs remain.
"""
