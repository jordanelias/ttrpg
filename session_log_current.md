# Valoria Session Log - Current

> Resuming instance: read ONLY this file. Archive is in session_log_archive.md.

---

session_close: 2026-03-26-checkpoint14
phase: 2
status: Checkpoint 14 compiled and committed

completed_this_session:
  - Stage 17 canon guard pass (all P1-P14 constraints verified)
  - 6 mechanical patches applied to valoria_ttrpg_complete.md
  - 17 hybrid gaps resolved (G-075, G-079–G-095)
  - §12.3 Hybrid Mode rewritten with all resolved gap content
  - §12.9 Hybrid Consequence Rules added (new section)
  - Checkpoint 14 exported: compilation/valoria_ruleset_checkpoint_14.md

commits:
  - stage17_canon_guard.md: 8526e934
  - valoria_ttrpg_complete.md (stage 17 patches): f318f7ee
  - designs/hybrid_gaps_resolved.md: 6e543b5c
  - valoria_ttrpg_complete.md (hybrid additions): 38a0fe31
  - compilation/valoria_ruleset_checkpoint_14.md: 2115df16

canonical_decisions_locked:
  thread_op_pools:
    Leap: Attunement + History bonus
    Contact_Duration: Focus score (rounds)
    Wound_disruption: Focus check TN 7 Ob 1
    All_ops_Weave_Pull_FR: Spirit + History bonus
  composure: Presence + 6 (range 7-13)
  debate_pool: Cognition + History bonus
  battle_engine: Officer Cognition (attack) + Presence (cohesion/rally); initiative Cognition
  personal_combat_manoeuvres: Agility
  inspiration_cap: Spirit score (no derived name)
  coherence_track: individual 10-0 (10=fully coherent, 0=monstrous NPC)
  thread_stability: campaign-arc 20-0 (20=stable, 0=crisis)
  hybrid_session_structure: Personal (90-150min) → Strategic → Cascade
  hybrid_pacing: 1 session minimum per season
  hybrid_fog_of_war: 4 qualitative states; exact for own faction; Intel always hidden
  hybrid_handoffs: batch to Cascade; GM ledger
  hybrid_zoom_in: player-involved only
  hybrid_cascade: 5-step sequence, GM-only
  hybrid_resources_wealth: threshold = 2x rolled; below = stressed
  hybrid_flashback: Personal phase only
  hybrid_pc_death: Crisis penalty; take over loyal NPC or succession; no new characters
  hybrid_faction_collapse: continue as personal character; lose faction dice bonuses
  hybrid_downtime: concurrent with Strategic phase
  hybrid_advancement: board game successes generate CP
  hybrid_knot_gating: gated by in-scene discovery

editorial_pending:
  - Renown permission table (tiers 1-10)
  - Varfell Private Collection transfer
  - Niflhel primus inter pares
  - Revolution named elder NPC
  - Territory names (batch_e placeholders)
  - Varfell victory condition tuning
  - 10 remaining seasonal event cards
  - Named Restoration NPCs
  - E-01 assassination perpetrator
  - E-03 AG calendar name
  - Niflhel named NPC stat blocks (Rolf Dunmark, Solvind Brak)
  - Revolution named NPC stat blocks (Edith Varn)

next_action:
  recommended: Board game mode compilation (Phase 2 remaining deliverable) OR Phase 3 simulation
  model: Sonnet 4.6
  note: G-093 Resources/Wealth formula (2x vs 2x-1) flagged for Phase 3 stress testing

model_routing_notes: Sonnet 4.6 throughout — canon guard, hybrid gap resolution, compilation
