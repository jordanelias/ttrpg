session_id: 2026-04-19-batch2-arc-test
session_close: 2026-04-19
phase: 0
status: complete
last_stage: PP-666 arc test Batch 2 — 5 variants, bugs fixed, committed acfe32d
next_action:
  skill: engine_v4 rebuild — Phase 0 canon audit
  description: >
    Start Phase 0 of the engine rebuild workplan at
    tests/sim_framework/workplan_rebuild_2026-04-19.md (commit 13b8f30).
    Phase 0 is a canon audit only — no engine changes. Full reads listed
    in the workplan. Output: tests/sim_framework/canon_audit.md.
    NOTE: Three spec fixes now required before PP-666 mechanics can be
    canonized — see tests/sim_framework/arc_test_batch2_results.md.
  blockers:
    - PP-666 spec fix 1: fractional_province_ownership §2.6 — RM→RM Secession candidate bug
    - PP-666 spec fix 2: faction_succession_split §4 — RM emergence threshold Order=0 clarification
    - PP-666 spec fix 3: faction_succession_split §2.4 — splinter Influence split decision required
commits:
  - acfe32d: arc test batch 2 — 5 variants, 3 sim bugs fixed, 5 design findings, 3 spec fixes
session_highlights:
  - Batch 2 ran 5 design variants against Batch 1 findings. Three sim bugs fixed first:
    (1) RM Inf incrementing on RM→RM no-op seceessions; (2) same-season Consolidation
    race overwriting just-seceeded settlements; (3) succession triggers not firing due
    to session state loss.
  - B2-1 (secession cooldown): cooldown fix has zero effect. Root cause was wrong —
    oscillation is RM→RM secessions on already-RM settlements, not Consolidation churn.
    Spec fix needed: Secession candidates must be restricted to national-faction-held
    settlements (not subnational/RM).
  - B2-2 (RM emergence threshold): Order=0 is correct. Order<=1 produces deterministic
    RM growth (7 settlements, low variance). Order=0 produces 4-5 settlements with genuine
    seed variance and RM growing via political leverage (succession split momentum) rather
    than settlement accumulation — matches design intent.
  - B2-3 (splinter Mandate floor): floor has zero effect. Splinter Influence is unsplit
    (spec §2.4 explicitly). Mandate floor is not the survival lever. Design decision needed:
    split Influence 60/40 same as Mandate if durable rival splinters are intended.
  - B2-4 (Crown suppression): suppression AI backfires. Spending Influence on Ob+1 to
    fragmentation checks adds Ob to Crown's OWN province defense, not rivals'. Crown PV
    drops from 20.0 to 18.2 (seed 42). Crown Influence exhausted by S05. Suppression
    cannot be modeled as fragmentation Ob modifier — needs Mandate/Influence drain on
    target faction in engine_v4 Phase 4 political AI.
  - B2-5 (mutual fractionalization): most interesting arc. Hafenmark-Varfell cold-war
    standoff where both hold stakes in each other's territory. Less RM growth than
    single-fractionalization. T13 fractionalizes as secondary effect of distracted Varfell.
    Consider treaty mechanic for diplomatic resolution of mutual fractionalization.
open_items:
  - ED-706 VTM strike — Varfell victory paths need rewrite (P2)
  - ED-707 Cultural Reformation strike — faction actions need rewrite (P2)
  - Six canon gaps from workplan (mine income, food vulnerability, etc.)
  - PP-666 spec fix 1: fractional_province_ownership §2.6 Secession candidates restriction
  - PP-666 spec fix 2: faction_succession_split §4 RM emergence threshold Order=0
  - PP-666 spec fix 3: faction_succession_split §2.4 splinter Influence split decision
  - PP-666 settlement_adjacency_map.yaml still not authored
  - ED-671 Thread-perception census (P1)
  - ED-666 Path B speed-run calibration (P1)
  - ED-667 Coup Counter readiness gap (P1)
  - ED-632 Shadow Renown mechanic (P1)
  - ED-633 Deniability Debt (P1)
  - ED-629 Heresy Proceedings auth loop (P1)
  - ED-663 Wealth cap (P1)
