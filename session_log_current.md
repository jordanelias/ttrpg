session_id: 2026-04-19-provisional-mechanics-arc-test
session_close: 2026-04-19
phase: 0
status: complete
last_stage: PP-666 provisional mechanics arc test — 4 scenarios × 3 seeds, committed 6ea1f3e
next_action:
  skill: engine_v4 rebuild — Phase 0 canon audit
  description: >
    Start Phase 0 of the engine rebuild workplan at
    tests/sim_framework/workplan_rebuild_2026-04-19.md (commit 13b8f30).
    Phase 0 is a canon audit only — no engine changes. Full reads of:
    mass_battle_v30, settlement_layer_v30, faction_layer_v30, faction_politics_v30,
    factions_personal_v30, npc_behavior_v30, params/bg/* (all 15+ files),
    threadwork_v30, calamity_radiation_v30, southernmost_v30.
    Output: tests/sim_framework/canon_audit.md listing every system + source +
    gap flag. Six gaps already flagged in workplan as editorial blockers:
    mine income rate, food vulnerability mechanic, Crown Einhir suppression action,
    RM activation trigger, Thread ops in mass battle, subnational faction emergence.
    Phase 0 confirms whether these gaps are real or exist in canon sections
    not yet read. After audit, Phase 1 (substrate — territory graph + settlement
    sublayer + Calamity radiation state) starts.
    NOTE: Arc test surfaced 8 additional gaps in PP-666 mechanics — see
    tests/sim_framework/arc_test_results.md. Two design issues flagged:
    (1) Secession oscillation loop in fractional_province_ownership_v30 — needs cooldown.
    (2) Splinter viability at Mandate 1 unclear in faction_succession_split_v30.
    These should be resolved before PP-666 mechanics are canonized.
  blockers:
    - settlement_adjacency_map.yaml not authored — blocks adjacency mechanic canonization
    - fractional_province_ownership_v30 Secession cooldown gap — produces oscillation loop
commits:
  - 6ea1f3e: PP-666 arc test — 4 scenarios, 8 gap flags, secession loop + splinter viability issues
session_highlights:
  - Ran targeted simulation of three PROVISIONAL PP-666 mechanics: settlement_adjacency_v30,
    fractional_province_ownership_v30, faction_succession_split_v30.
  - Settlement adjacency fires correctly. Path-constrained invasion → partial capture →
    fractionalization works as designed.
  - Succession split produces meaningful seed-to-seed variance (clear vs narrow outcomes
    drive divergent arcs). RM backing interaction (+1 Influence on partial success) is
    well-designed.
  - Fractional province oscillation bug: no Secession cooldown in spec. Settlement
    seceeds → consolidates → seceeds in consecutive seasons indefinitely. Needs 2-season
    post-Consolidation cooldown added to fractional_province_ownership_v30.
  - Splinter faction at Mandate 1 is non-functional: collapses in ~4 seasons. Spec
    unclear whether splinter is "chaos token" or "durable rival".
  - Dominant emergent arc across all scenarios: RM ascent from Varfell political fracture.
    Vaynard dies → succession split → Eastern Varfell at Mandate 1 fails fragmentation
    checks → Grauwald/Oastad secede to RM → RM reaches Stage 3 by mid-game.
    This arc is mechanically grounded and design-intent-aligned but may be too fast
    (Stage 3 by S02 in degraded-Order scenarios).
  - Full seed-determinism in Arc 3 (no succession event) — dice pools too static,
    no real variance without high-variance events. Engine_v4 needs dynamic Influence.
  - Crown and Church are passive across all arcs. Expected for this simulation scope;
    confirms engine_v4 needs Crown suppression AI and Church Mass Seizure to be active actors.
open_items:
  - ED-706 VTM strike — Varfell victory paths A/B/C need rewrite (P2)
  - ED-707 Cultural Reformation strike — faction_actions, Varfell ladder, NPC priority trees need rewrite (P2)
  - Six canon gaps from workplan (mine income rate, food vulnerability, Einhir suppression action,
    RM activation trigger, Thread ops in mass battle, subnational faction emergence)
  - Eight new gap flags from arc test — see tests/sim_framework/arc_test_results.md
  - coverage_matrix at 4537/5000 tokens — warning threshold
  - editorial_ledger at 1652/2000 tokens — warning threshold
  - ED-671 Thread-perception census (P1)
  - ED-666 Path B speed-run calibration (P1) — note: Path B itself pending rewrite after VTM strike
  - ED-667 Coup Counter readiness gap (P1)
  - ED-632 Shadow Renown mechanic (P1)
  - ED-633 Deniability Debt (P1)
  - ED-629 Heresy Proceedings auth loop (P1)
  - ED-663 Wealth cap (P1)
  - PP-666 fractional_province_ownership_v30 — Secession cooldown gap (new, from arc test)
  - PP-666 faction_succession_split_v30 — splinter viability at Mandate 1 unclear (new, from arc test)
  - PP-666 settlement_adjacency_map.yaml — not authored, blocks canonization (new, from arc test)
