# Valoria — Full Campaign Simulation Readiness Report

**Date:** 2026-04-19
**Scope:** Assessment of whether the Valoria design canon is sufficient to simulate a full campaign covering the entire game.
**Verdict:** **DESIGN COMPLETE.** Runnable-sim-harness WORK REMAINING.

---

## §1 Executive Summary

The 17 systems required by `sim_gate('full_stack')` are all specified by canonical design documents, and the `references/canonical_sources.yaml` `systems:` block now maps every system to its authoritative source (commit 393e76e3, 2026-04-19). All cross-system interactions documented in the narrative simulation corpus (sim_x_01 through sim_x_36+, plus sim_var_01 through sim_var_06 and arc simulations 31-35) are reproducible by a human GM or a newly-written simulation harness.

**The game can be run in full.** What cannot yet be done without additional engineering work is an automated Python simulation that executes seasons of play end-to-end without human input. That is a separate deliverable (a simulation program), not a design gap.

---

## §2 System-by-System Readiness (full_stack preset, 17 systems)

| System | Canonical Source | Status |
|---|---|---|
| core_engine | designs/architecture/complete_systems_reference.md · params/core.md | CANONICAL |
| combat | params/combat.md | CANONICAL |
| threadwork | designs/threadwork/threadwork_v30.md · params/threadwork.md | CANONICAL |
| clocks | params/bg/clocks.md | CANONICAL |
| factions | designs/provincial/factions_personal_v30.md · params/factions.md · params/factions/stats_1_7_scale.md | CANONICAL (ED-717 substrate-postures added 2026-04-19) |
| victory | designs/provincial/victory_v30.md · params/bg/victory.md | CANONICAL |
| territories | designs/territory/settlement_layer_v30.md · designs/territory/settlement_adjacency_v30.md · designs/provincial/fractional_province_ownership_v30.md | CANONICAL |
| mass_combat | designs/provincial/mass_battle_v30.md · params/mass_combat.md | CANONICAL |
| social_debate | params/contest.md | CANONICAL |
| scale_transitions | designs/architecture/scale_transitions_v30.md · params/scale_transitions.md | CANONICAL |
| faction_layer | designs/provincial/faction_layer_v30.md | CANONICAL |
| military_layer | designs/provincial/military_layer_v30.md | CANONICAL |
| tc_political | designs/provincial/ci_political_v30.md | CANONICAL (ED-721 Option A locked 2026-04-19 — T9 CI cap uniform) |
| peninsular_strain | designs/provincial/peninsular_strain_v30.md | CANONICAL |
| settlement_layer | designs/territory/settlement_layer_v30.md | CANONICAL |
| campaign_architecture | designs/architecture/campaign_architecture_v30.md | CANONICAL |
| derived_stats | params/factions/stats_1_7_scale.md | CANONICAL |

**17 of 17 systems have canonical sources. No design gaps.**

---

## §3 Supporting Systems (Also Required for Full Campaign)

| System | Canonical Source | Status |
|---|---|---|
| NPC behavior + arcs | designs/npcs/npc_behavior_v30.md · designs/npcs/npc_character_analyses_v30.md | CANONICAL (Royal Assassination fuse propagated 2026-04-19) |
| Conviction Track | params/factions/npc_stance_triangles.md | CANONICAL |
| Faction Succession Split | designs/provincial/faction_succession_split_v30.md | CANONICAL |
| Royal Assassination Fuse | params/bg/royal_assassination.md | CANONICAL (Session C 2026-04-19) |
| Tensions Deck | params/bg/tensions_deck.md | CANONICAL (Session C 2026-04-19) |
| Conflict Architecture | designs/architecture/conflict_architecture_proposal.md | CANONICAL (Session B 2026-04-18 — Niflhel dissolution + Löwenritter graduated autonomy) |
| Character Creation | designs/world/character_histories_v30.md | CANONICAL |
| Worldbuilding | designs/world/worldbuilding_v30.md | CANONICAL |
| Throughlines Framework | references/throughlines_meta.md · references/throughlines_meta_infill.md | CANONICAL (PP-672, PP-674) |
| Shadow Renown | designs/provincial/faction_politics_v30.md §2.2b.i | CANONICAL (ED-632 approved 2026-04-19) |
| Deniability Debt | designs/provincial/faction_politics_v30.md §2.2b.ii | CANONICAL (ED-633 approved 2026-04-19) |

---

## §4 Existing Simulation Artifacts

### §4.1 Narrative simulations (runnable by human GM)

- **tests/sim/sim_x_01 through sim_x_22** — atomic cross-system interaction simulations (combat-thread, debate-thread, mass-battle-thread, seasonal cascades, etc.).
- **tests/sim/sim_x_23 through sim_x_36+** — batch cross-mode protocols (personal combat, hybrid domain, BG multifaction, three-season cascades).
- **tests/sim/sim_var_01 through sim_var_06** — variant scenarios (RM path, RS crisis, debate clash, Löwenritter, hybrid Crown, mass combat wounds).
- **tests/sim/sim_ttrpg_batch_sonnet46.md** — TTRPG-mode batch sim.
- **tests/sim/sim_warden_tc_reclaim.md** — Warden/TC reclamation scenario.
- **tests/sim/simulation_report_arcs_31_33.md** — full arc-level simulation narrative (5+ seasons per arc; cross-faction).
- **tests/sim/sim_tw_01.md** — threadwork-focused simulation.

These simulations collectively exercise every canonical system and every major cross-system interaction. A human GM with this canon can run a complete campaign.

### §4.2 Narrow Python stress tests

- **tests/sim/stress_derived_stats_v2.py** — automated stress test for derived-stats subsystem. Only the derived-stats subsystem has a runnable Python harness.

### §4.3 Audits (confirmations of mechanical consistency)

Thirty-plus audit reports under `tests/audit/` confirm cross-system consistency, label integrity, throughline coverage, and editorial resolution passes. Notably:
- tests/audit/engine_audit_2026-04-18.md (engine-level consistency)
- tests/audit/audit_cross_system_2026_04_06.md (cross-system)
- tests/audit/audit_phase3_crossmode_cogload.md (cog-load across modes)
- tests/audit/throughline_synthesis_holistic.md (throughline coverage)

---

## §5 Gap: Automated Full-Campaign Python Simulator

A runnable Python program that simulates an entire campaign end-to-end (season-by-season, all systems, no human input) **does not exist**. To create one, the following work is required:

1. **Sim harness design** — a `valoria_full_campaign_sim.py` orchestrator executing the seasonal loop, faction domain-actions, NPC priority trees, clock advancement, contest resolution, scale transitions, and victory checks.
2. **Verification ledger** — `/home/claude/sim_verification_ledger.json` mapping every mechanical constant in the sim to its canonical source (per `valoria_hooks.sim_gate` requirements).
3. **Test corpus** — deterministic seeds exercising each variant scenario (RM-led campaign, Church-dominant, Löwenritter split, Varfell conquest, Thread revelation cascade, etc.).
4. **Output format** — machine-readable per-season state dumps plus human-readable narrative reports (mirroring the sim_x_NN format).

Estimated scope: 2-4 focused sessions (or a single larger one with substantial context budget). Not blocked by any design gap. Not blocked by any open P1 editorial item.

---

## §6 Verdict

**Design completeness for full-campaign simulation: ✅ COMPLETE.**

- All 17 full_stack systems canonically specified.
- All supporting systems (NPCs, arcs, fuses, decks, throughlines) canonically specified.
- Zero P1 editorial blockers (ED-632, ED-633, ED-717 all closed 2026-04-19; ED-721 locked to Option A).
- Narrative simulation corpus proves rules interact correctly.

**Automated simulator: ⏳ WORK REMAINING.**

- Runnable harness not yet written.
- Verification ledger not yet built.
- Test corpus not yet designed.
- This is a separate engineering deliverable, not a design question.

The canon is ready. Write the sim when ready to run it.
