# Valoria Strategic Sim v16 → v17 Module Manifest
**Date:** 2026-05-15
**Scope:** Integrate all missing workstream content into strategic faction balance sim
**Reason:** v16 (v15 + v12c mechanics) structurally fails — Church 0%, Varfell 0% — because the v15 engine lacks load-bearing canonical mechanics from settlement layer, CI political, mass battle, and expanded faction actions.

## Background

Phase 1a (dice calibration) complete. Phase 1b (parameter sweep on v16) cannot converge because the engine is structurally incomplete. 27 canonical mechanics missing from v16. Church's 0% win rate traces to missing settlement infrastructure (Religious Buildings for PT generation, Templar Stations for CI growth, Inquisitor Bases for RM resistance). Mass battle absent (single-roll Military Conquest instead of 6-step BG resolution). Settlement → territory aggregation absent.

Jordan directive: incorporate all missing workstream content before attempting balance sweep.

## Module Decomposition

### Module 1 — Church Settlement Infrastructure
**Dependencies:** none (foundational)
**Canonical sources:**
- `settlement_layer_v30.md §1.5` (4-axis infrastructure)
- `settlement_layer_v30.md §1.6` (Parish Social Services)
- `settlement_layer_v30.md §1.7` (Pastoral Assumption)
- `ci_political_v30.md §1` (Spiritual Weight)
- `victory_v30.md §3.2` (Seizure Ob formula)

**What it adds:**
- Per-territory Church infrastructure state: Religious Building tier (none/Chapel/Church/Cathedral), Templar Station (bool), Inquisitor Base (bool), Church Governor (bool)
- Starting infrastructure from canonical settlement registry (37 settlements mapped to 15 territories)
- PT generation per season from Religious Buildings: Chapel +0.5, Church +1.0, Cathedral +2.0 (+0.5 adjacent)
- CI generation from Templar Stations: +1 CI/season per territory with Templar
- RM Ob modifier from Inquisitor Bases: +1 Ob to RM governance actions
- Seizure Ob = 10 − PT − infrastructure_modifiers (Chapel −0, Church −1, Cathedral −2, Templar −1, Inquisitor −1, Governor −2; cap −4/territory; floor 1)
- Spiritual Weight (SW) per territory (fixed attribute)
- SW-weighted CI generation replacing v15's simple piety_yield

**Estimated session budget:** 1 session
**Status:** pending

### Module 2 — CI Political Revision
**Dependencies:** Module 1 (infrastructure state for CI generation)
**Canonical sources:**
- `ci_political_v30.md §1–§3`
- `victory_v30.md §3.2` (milestones + Mass Seizure)

**What it adds:**
- CI milestones: 55 (Institutional Reach: +1 Ob to anti-Church actions), 80 (Church Ascendant: Seizure −1 global, PT drift +1), 100 (Theocracy Unification Attempt)
- Revised Mass Seizure: targets all territories with Church buildings, individual Ob per territory
- CI cap ±5/season from all sources, ±3 from player Domain Actions
- Hafenmark suppress (−1 CI if Hafenmark L ≥ 4) — already in v15, verify

**Estimated session budget:** 0.5 session (smaller module, depends on M1)
**Status:** pending

### Module 3 — Mass Battle Resolution
**Dependencies:** Module 4 (unit state)
**Canonical sources:**
- `mass_battle_v30.md §B.3` (6-step BG resolution)
- `mass_battle_v30.md §B.2` (unit roster)
- `params/mass_combat.md` (unit stats, tactic cards)

**What it adds:**
- `resolve_battle()` replacing single-roll Military Conquest for inter-faction battles
- 6-step BG resolution: tactic declaration → disposition lookup → pool construction → roll → margin → outcome
- Active unit classes: Levy, LightInf, HeavyInf (3 initially; 6 reserved)
- Tactic cards: attacker/defender selection from canonical set
- Fort dice in defense
- Battle outcome: territory transfer, unit losses, Accord/Stability triggers

**Estimated session budget:** 1.5 sessions
**Status:** pending

### Module 4 — Unit State Management
**Dependencies:** none (foundational)
**Canonical sources:**
- `mass_battle_v30.md §B.2` (unit classes)
- `params/mass_combat.md` (unit stats)
- `integration_plan_v3 §5 Phase 2c` (unit-token state)

**What it adds:**
- Per-faction unit roster: `defaultdict(lambda: defaultdict(int))` per integration plan
- Active classes: Levy, LightInf, HeavyInf with Martial/Endurance/Discipline
- Muster action: mint Levy tokens in territory
- Commit to battle: tokens from adjacent territory (model b per plan recommendation)
- Unit losses from battle reduce roster
- Serialization for JSONL logging

**Estimated session budget:** 0.5 session
**Status:** pending

### Module 5 — Settlement-Territory Aggregation
**Dependencies:** Module 1 (settlement state)
**Canonical sources:**
- `settlement_layer_v30.md §4.3` (Order → revolt)
- `settlement_layer_v30.md §3` (governance)
- Integration plan v3 §5 (settlement → territory)

**What it adds:**
- Settlement Order → Province Accord aggregation at arc boundary
- Settlement events (revolts at Order 0, famine, Domain Echoes) feed territory state
- RM Cell Resilience: +1 Ob to suppression when RM presence in ≥3 settlements
- Economic effects: settlement Prosperity → territory Wealth modifiers

**Estimated session budget:** 1 session
**Status:** pending

### Module 6 — Faction Action Expansion
**Dependencies:** Modules 1-5 (uses infrastructure, units, settlements)
**Canonical sources:**
- `faction_canon_v30.md` (complete faction sheets)
- `victory_v30.md §3.1` (Crown Initiative)
- `peninsular_strain_v30.md §5` (expanded action set)

**What it adds:**
- Crown Initiative 3 modes: Royal Progress / Great Work / Coronation Renewal
- Church Absolution (recovery action for other factions at Mandate cost)
- RM Uprising mechanics (from victory_v30)
- Updated AI scoring for all new/revised actions
- Verify existing actions match canonical specs

**Estimated session budget:** 1 session
**Status:** pending

### Module 7 — Integration + Balance Sweep
**Dependencies:** Modules 1-6 verified
**What it does:**
- Wire all modules into mc_v17.py
- N=1000 balance sweep across parameter grid
- Wilson CI check: all factions [20%, 30%] at 95%
- Sensitivity analysis
- JSONL output

**Estimated session budget:** 1-2 sessions
**Status:** pending

## Summary

| Module | Name | Sessions | Dependencies |
|---|---|---|---|
| 1 | Church Settlement Infrastructure | 1 | — |
| 2 | CI Political Revision | 0.5 | M1 |
| 3 | Mass Battle Resolution | 1.5 | M4 |
| 4 | Unit State Management | 0.5 | — |
| 5 | Settlement-Territory Aggregation | 1 | M1 |
| 6 | Faction Action Expansion | 1 | M1-5 |
| 7 | Integration + Balance Sweep | 1.5 | M1-6 |
| **Total** | | **~7 sessions** | |

**Critical path:** M1 → M2 → M6 → M7 (Church viability). Parallel: M4 → M3 (mass battle).

## Supersedes

Integration plan v3 Phases 1b through 5. Phase 1a (dice calibration) stands. Phase 3 (doc propagation) unaffected. Phase 6+ horizon unchanged.
