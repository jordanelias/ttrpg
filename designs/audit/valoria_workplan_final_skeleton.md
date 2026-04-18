<!-- SKELETON: designs/audit/valoria_workplan_final.md -->
<!-- canonical: designs/audit/valoria_workplan_final.md -->
<!-- Generated: 2026-04-18 (post-restructure) -->

# Valoria — Comprehensive Workplan (Final)
## Derived from Complete System Audit (2026-04-18)
## Organized by priority tier → dependency order → estimated effort
## All 19 review amendments integrated
## Target: Godot 4.3 videogame implementation
---
# HOW TO USE THIS DOCUMENT
---
# PHASE 0: HOUSEKEEPING (prerequisite to all other work)
## 0.1 — Rebuild editorial_ledger_summary.yaml
## 0.2 — Deduplicate ED-663 in active ledger
## 0.3 — Update file_index_summary.md propagation-pending count
## 0.4 — Run broken_dependency_checker against propagation_map
## 0.5 — Verify session_log open_items against editorial_ledger
## 0.6 — Triage P0 blockers ED-668–672
## 0.7 — Params file staleness audit
---
# PHASE 1: P1 BLOCKERS — DESIGN GAPS (blocks implementation)
## 1.1 — Knot Formation During Play [AUD-NPC-01]
## 1.2 — Accord Propagation to Settlement Order [AUD-SET-02]
## 1.3 — Derived Stats Numerical Calibration [AUD-DS-01]
## 1.4 — Faction Politics Simulation [AUD-FP-01]
## 1.5 — Resolve Coverage Matrix P1 EDs [ED-588, ED-589, ED-612]
---
# PHASE 2: P2 ITEMS — SIMULATION DEBT & CALIBRATION
## 2.1 — Social Contest Re-simulation [AUD-SC-02, AUD-SC-03]
## 2.2 — Co-Movement Card Calibration [ED-577-01/02/03/04] ⚠ HARD DEPENDENCY FOR PHASE 4
## 2.3 — NPC Stat Gaps [AUD-NPC-02]
## 2.4 — NPC Priority Tree Cross-Faction Simulation [AUD-NPC-03]
## 2.5 — Settlement Economy Simulation [AUD-SET-01, AUD-SET-03]
## 2.6 — RM Victory Probability [AUD-VIC-02]
## 2.7 — Mass Battle Editorial Items [AUD-MB-02]
## 2.8 — Combat Ranged TN Integration [AUD-COM-04, ED-129]
## 2.9 — Threadwork Foundation Text [AUD-TW-01]
## 2.10 — UI/UX Integration: Derived Stats + Settlement Map [AUD-UI-01, AUD-UI-02]
## 2.11 — Generational Transition Throughline
## 2.12 — params_threadwork Ob Alignment [AUD-TW-02]
---
# PHASE 3: P3 ITEMS — CLEANUP, PROPOSALS, POLISH
## 3.1 — Combat §4 Action Priority Resolution [AUD-COM-01] ⚠ SIM-RELEVANT
## 3.2 — Combat §9 Stat Name Propagation [AUD-COM-02] ⚠ SIM-RELEVANT
## 3.3 — Combat §9 Deprecated Doc Reference [AUD-COM-03]
## 3.4 — Stamina Merge Proposal [AUD-COM-05]
## 3.5 — Social Contest §1 Core Principle [AUD-SC-01]
## 3.6 — N-Way Opposing Operations [AUD-TW-03]
## 3.7 — Independent Player Path [AUD-PA-02]
## 3.8 — Conviction Crisis Table Weighting [AUD-NPC-04]
## 3.9 — CV→PT Terminology Unification [AUD-CT-01] ⚠ SIM-RELEVANT
## 3.10 — Coherence → Recall → Skill Access [AUD-CH-01]
## 3.11 — Clock Registry: Settlement Derived Tracks [AUD-CK-01] ⚠ SIM-RELEVANT
## 3.12 — Mass Battle §A.5 Deduplication [AUD-MB-01]
## 3.13 — T6 Throughline Tag Assignment
## 3.14 — Simultaneous Domain Echo Cap Verification [AUD-ST-01]
## 3.15 — Fieldwork Demand Deflection Ob [AUD-FW-01]
## 3.16 — Thread-Read Investigation Superiority [AUD-FW-02]
## 3.17 — Victory Accord Rule Consolidation [AUD-VIC-01]
## 3.18 — NPE Volatility Convergence [AUD-INV-01]
---
# PHASE 4: FULL-CAMPAIGN SIMULATION FRAMEWORK
---
## 4.0 — Framework Architecture
---
## 4.1 — State Initialization
---
## 4.2 — Season Resolution Engine
---
## 4.3 — Feature Coverage Checklist
### Personal Scale (11 items)
### Fieldwork (13 items)
### Social Contest (14 items)
### Threadwork (16 items)
### Mass Battle (14 items)
### Scale Transitions (8 items)
### Player Agency (10 items)
### NPC Behavior (9 items)
### Settlement & Governance (10 items)
### Victory & Endgame (12 items)
### Derived Stats Economy (8 items)
### Companion & Knot (8 items)
### Character Lifecycle (5 items)
---
## 4.4 — Simulation Output & Analysis
---
## 4.5 — Stress Tests (8 scenarios, run after baseline calibration)
### 4.5.1 — Church Theocracy Rush
### 4.5.2 — Military Conquest Death Spiral
### 4.5.3 — Thread Practitioner Coherence Arc
### 4.5.4 — Five-Faction Simultaneous Race
### 4.5.5 — Altonian Invasion
### 4.5.6 — NPC Cascade
### 4.5.7 — Settlement Economic Engine
### 4.5.8 — Long Campaign NPC Turnover
---
## 4.6 — Calibration Report & Issue Triage
---
## 4.7 — Regression Testing
---
## 4.8 — Simulation Infrastructure
---
# PHASE 5: GODOT IMPLEMENTATION PREP
## 5.1 — GM-to-Engine Rule Conversion
## 5.2 — Godot Implementation Sequence
## 5.3 — Data Serialization Specification
## 5.4 — Godot Scene Tree Architecture
## 5.5 — Cross-Repo Propagation Protocol
---
# PHASE 6: ONGOING MAINTENANCE PROTOCOL
## 6.1 — Session Start
## 6.2 — After Design Doc Changes
## 6.3 — Per Commit
## 6.4 — New Issues
## 6.5 — Quarterly Review
---
# COMPLETE FLAG INDEX
## P0 (5 items — Phase 0.6 triage)
## P1 (7 items — Phase 1)
## P2 (13 items — Phase 2)
## P3 (18 items — Phase 3)
---
# EFFORT ESTIMATES
---
# CRITICAL PATH