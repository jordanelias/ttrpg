session_id: 2026-04-28-phase0-phase1
session_close: 2026-04-28
phase: editorial + infrastructure
status: in-progress
last_stage: >
  Phase 0 completion (12/13 exit criteria met, LICENSE pending) + Phase 1 partial.
  This session commits (ttrpg):
    4547737 — propagation_map broken dep fix
    052b82d — bootstrap wiring (compliance_check + freshness_gate)
    7f640e5 — F2 verification batch ED-745/746/747/748 resolved
    ba7497d — PP-666 trio vetting block
  This session commits (valoria-game):
    f9ed815 — GameMode strip broken ref followup (prior session continuation)
    600c5cf — CI workflow
    e4a62db — conversion_ledger + design_sync status reconciliation
    c41688c — README rewrite
  Prior session commits carried forward:
    3d7e46b — register truthfulness
    3edf7f0 — threadwork P0 triage
    8be75e5 — GameMode strip (7 files)
    6dadbe2 — compliance_check auto-fetch
    b07c459 — freshness_gate regex fix + SHA population
    b5ca0a7 — ttrpg README
next_action:
  skill: editorial
  description: >
    DECISION PENDING (Jordan):
    (1) Restore Intelligence as 6th faction stat? Review at designs/audit/faction_stats_renaissance_review.md
        - If yes: starting values Crown 3, Church 4, Hafenmark 3, Varfell 5, Loewenritter 2, Guilds 4
        - Fixes Spy Ob formula (currently broken), Varfell Path A re-gate, Varfell stat identity
        - If no: need replacement Spy Ob formula + Varfell Path A re-gate + Varfell differentiation
    (2) LICENSE decision (GOV-08) — proprietary/MIT/Apache/CC BY-NC/custom
    PHASE 1 REMAINING (after Intelligence decision):
    (3) 1.1 Knot Formation During Play — design decision
    (4) 1.2 Accord Propagation to Settlement Order — 15-25 rules need settlement targeting
    (5) 1.3 Derived Stats Calibration — depends on 1.2
    (6) 1.4 Faction Politics Sim — depends on 1.3
    (7) 1.8 Varfell Path A editorial rewrite — depends on Intelligence decision
    PHASE 0 RESIDUAL:
    (8) compliance_check atomizer dep — auto-fetch wired but atomizer.py not in fetch list
    (9) canonical_sources.yaml at 4670/5000 tokens — approaching threshold
  priority: "Intelligence decision unblocks Path A + Spy Ob + Varfell identity. Then 1.1/1.2 design decisions."
blockers:
  - "Intelligence stat decision (Jordan)"
  - "LICENSE decision (Jordan)"
  - "1.1 Knot Formation design (Jordan)"
  - "1.2 Accord Propagation design (Jordan)"
notes:
  - "Faction stats Renaissance review committed as designs/audit/faction_stats_renaissance_review.md"
  - "All P3 EDs resolved (745-748). Active ledger now 2 open (ED-710/711, both P2)"
  - "Phase 0 exit: 12/13 criteria met. Only LICENSE remains."
  - "Threadwork P0 triage: 7 resolved, 15 Jordan-decision, 4 mechanical, 2 reclassify"
