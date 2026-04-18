# Valoria — Comprehensive Workplan (Final)
## Derived from Complete System Audit (2026-04-18)
## All review amendments integrated
## Target: Godot 4.3 videogame implementation

---

# HOW TO USE THIS DOCUMENT

**Execution order matters.** Items sequenced by dependency. Cross-references to audit flags (AUD-*), editorial items (ED-*), simulation debt (SIM-*), and propagation map entries enable verification.

**Canon compliance is non-negotiable.** Before any design decision in Phase 1-3, read `canon/00_philosophical_foundations_rules.md`. Every change verified against the 15+ principles. The principle does not bend.

**Standard commit protocol (every commit):**
1. Update `references/propagation_map.md` per Step A-D
2. Update `references/canonical_sources.yaml` SHAs
3. Update `canon/editorial_ledger.yaml` for resolved/raised EDs
4. Include canonical_sources.yaml (co-file compliance)
5. Use `h.safe_commit()` only

**Five inconsistency lenses (check regularly):**

| Lens | Location | Catches |
|------|----------|---------|
| Propagation Map | `references/propagation_map.md` | Unpropagated changes. Run `tools/broken_dependency_checker.py`. |
| Session Log | `session_log_current.md` | Acknowledged but uncommitted work. Status mismatches vs ledger. |
| Editorial Ledger Summary | `canon/editorial_ledger_summary.yaml` | Definitive blocker list. Cross-ref `external_blockers` for sim_debt. |
| Coverage Matrix | `tests/coverage_matrix.md` | Open findings. SIM-DEBT items. Any "Open - ED-NNN" not in active ledger = inconsistency. |
| File Index | `references/file_index_summary.md` | Propagation-pending count. Stale sync gaps. |

**Session-start sweep:**
1. Bootstrap
2. Ledger open items vs coverage_matrix findings - flag mismatches
3. Session log open_items vs ledger - flag items in one but not other
4. `tools/broken_dependency_checker.py`
5. File_index propagation-pending count
6. Ledger summary p1_blocker_count vs actual P1 count in active ledger

---

# PHASE 0: HOUSEKEEPING

1 session. No design decisions.

**0.1** Rebuild editorial_ledger_summary.yaml (stale since 2026-04-17).
**0.2** Deduplicate ED-663 in active ledger (two entries exist).
**0.3** Update file_index_summary propagation-pending count (read full 446-line index).
**0.4** Run broken_dependency_checker (3 known broken deps in deprecated compilations).
**0.5** Verify session_log open_items against editorial_ledger.
**0.6** Triage P0 blockers ED-668-672 (Thread horizontal integration). Read threadwork_audit_register. For each: archive, escalate to Phase 1, or reclassify.
**0.7** Params file staleness audit. Compare every params_*.md against its canonical source doc. Refresh stale values. Clear KNOWN STALE SYNC GAPS. This is a Phase 4 prerequisite.

---

# PHASE 1: P1 BLOCKERS

2-3 sessions. Design decisions required. Canon compliance gate on every item.

**1.1 Knot Formation During Play** [AUD-NPC-01]
Solidarity Resonant Style blocked for all post-creation NPCs. Define videogame Knot formation: Disposition +5, TS >= 30, Spirit TN 7 Ob 2. Canon check P-12 (relational contagion). Affects npc_behavior, fieldwork, companion_specification. Resolve ED-391.

**1.2 Accord Propagation to Settlement Order** [AUD-SET-02]
Settlement layer changed Accord derivation (floor of mean settlement Order). 15-25 references across 6+ docs still use direct Accord modification. Audit and update each. Canon check P-03 (rendering). Large propagation footprint.

**1.3 Derived Stats Numerical Calibration** [AUD-DS-01]
All multipliers PROVISIONAL. Per-faction economic model. Seasonal income vs drain, time-to-zero, stat damage frequency. Depends on 1.2. Simulation: tests/sim_derived_stats_calibration.md.

**1.4 Faction Politics Simulation** [AUD-FP-01]
947 lines unsimulated. SIM-POL-R01-R05. Standing reachability, Ministry Competence decay, caste viability, branch differentiation, rank balance. Depends on 1.3. Simulation: tests/sim_faction_politics.md.

**1.5 Coverage Matrix P1 EDs** [ED-588, ED-589, ED-612]
ED-588: RM Phase 2 T9 PT <= 1 unreachable. ED-589: RM Presence markers undefined. ED-612: Guilds no solo victory. These affect simulation accuracy.

---

# PHASE 2: P2 CALIBRATION

3-5 sessions.

**2.1** Social Contest re-simulation [AUD-SC-02/03]. SIM-DEBT-03/04. Test CROSS at Resistance 2+. Test deadlock stall-break.

**2.2** Co-Movement Card Calibration [ED-577-*]. **HARD DEPENDENCY FOR PHASE 4.** Define CM-13 (TS 15, 1 scene, passive). Define reshuffle (global, on exhaustion). Simulate RS variance (90 draws). Scope CM-06.

**2.3** NPC Stat Gaps [AUD-NPC-02]. Ehrenwall TS 0/Cert 4. Torben TS 0/Cert 4. Maret Uln TS 35/Cert 2. Resolve ED-392-398.

**2.4** NPC Priority Tree Cross-Faction Sim [AUD-NPC-03]. 10-season 4-faction AI. Depends on 2.3.

**2.5** Settlement Economy Sim [AUD-SET-01/03]. 36-settlement model. Order-to-Accord. Siege attrition. Depends on 1.2, 1.3.

**2.6** RM Victory Probability [AUD-VIC-02]. RM vs 4 AI over 30 seasons. Depends on 2.4.

**2.7** Mass Battle Editorial Items [AUD-MB-02]. 7 Part C items. Accept/modify.

**2.8** Combat Ranged TN Integration [AUD-COM-04, ED-129]. Integrate or formalize separate.

**2.9** Threadwork Foundation Text [AUD-TW-01]. Write section 4.1/4.2 prose.

**2.10** UI/UX Integration [AUD-UI-01/02]. Derived stats display + settlement map. Depends on 1.3.

**2.11** Generational Transition Throughline. Complete state transition spec for PC death/retirement.

**2.12** params_threadwork Ob Alignment [AUD-TW-02]. Compare three-axis Ob between design doc and params.

---

# PHASE 3: P3 POLISH

2-3 sessions. Items marked SIM are sim-relevant - complete before Phase 4 if possible.

3.1 SIM Combat action priority resolution [AUD-COM-01]
3.2 SIM Combat section 9 stat name propagation [AUD-COM-02]
3.3 Combat section 9 deprecated doc reference [AUD-COM-03]
3.4 Stamina merge proposal [AUD-COM-05]
3.5 Social Contest section 1 Core Principle [AUD-SC-01]
3.6 N-Way Opposing Operations graduated collapse [AUD-TW-03]
3.7 Independent player path documentation [AUD-PA-02]
3.8 Conviction crisis table weighting [AUD-NPC-04]
3.9 SIM CV-to-PT terminology unification [AUD-CT-01]
3.10 Coherence-Recall-skill access verification [AUD-CH-01]
3.11 SIM Clock Registry settlement derived tracks [AUD-CK-01]
3.12 Mass Battle section A.5 deduplication [AUD-MB-01]
3.13 T6 throughline tag assignment
3.14 Domain Echo cap verification [AUD-ST-01]
3.15 Fieldwork Demand deflection Ob [AUD-FW-01]
3.16 Thread-Read investigation superiority [AUD-FW-02]
3.17 Victory Accord rule consolidation [AUD-VIC-01]
3.18 NPE Volatility convergence [AUD-INV-01]

---

# PHASE 4: FULL-CAMPAIGN SIMULATION FRAMEWORK

8-12 sessions. Hard deps: Phase 1, Phase 2.2, Phase 0.7.

**Mode:** Hybrid (Godot videogame primary mode).

## 4.0 Architecture

120-season loop modeling every gameplay feature. Season structure: Briefing (read all state) -> Duty Assignment (faction AI priority tree) -> Scene Slate Generation (player_agency section 4.2, Steps 1-7, Priority 0-5) -> Personal Phase (player policy selects scenes: fieldwork, combat, contest, Thread, mass battle, governance, companion) -> Strategic Phase (faction AI with card-hand constraint, conditional faction activation for Lowenritter/RM/Altonian/Wardens, priority trees, Domain Actions, military orders, Framework Drift, card refresh) -> Accounting (13 steps: derived values, stat damage, Domain Echoes, TC, PT with Calamity Drift, Accord recalculation, Strain, IP, RS, NPC arcs, NPC death/replacement with roster cap, Obligations, victory check, Exposure reset, clock ticks, Coherence recovery, seasonal events per settlement d6, Knot strain) -> Aftermath (Conviction revision, companion scene, Standing, Renown, retrospective, Portrait Retirement, character death with Legacy).

## 4.1 State Initialization

All values from canonical sources. Validation step: every loaded value compared against canonical design doc. Discrepancies flagged, design doc authoritative. Includes: 4 global clocks, 4 faction stat blocks with derived values and card hands, 36 settlements, 15 territory tracks, 14 named NPCs, configurable PC, conditional faction dormant states.

## 4.2 Season Resolution Engine

10 player policies (Investigator, Warrior, Diplomat, Practitioner, Governor, Balanced, Independent, Aggressive, Theocrat, Restorationist) x 5 random seeds = 50 campaign runs.

## 4.3 Feature Coverage Checklist

130+ items across 12 categories: Personal Combat (11), Fieldwork (13), Social Contest (14), Threadwork (16), Mass Battle (14), Scale Transitions (8), Player Agency (10), NPC Behavior (9), Settlement and Governance (10), Victory and Endgame (12), Derived Stats (8), Companion and Knot (8), Character Lifecycle (5). Every feature fires at least once across 50 runs.

## 4.4 Output and Analysis

Per-run: state logs, clock trajectories, faction trajectories, NPC arcs, victory proximity, PC lifecycle, coverage bitmap. Cross-run targets: victory timing S60-100, RS crisis S40-80, NPC arcs at least 4/14 by S60, 100% feature coverage, no death spirals before S30, no 10-season stasis windows.

## 4.5 Stress Tests (8)

Church Theocracy Rush. Military Conquest Death Spiral. Practitioner Coherence Arc. Five-Faction Race (BALANCE-001: each wins 20-30%). Altonian Invasion. NPC Cascade (3 NPCs x 3 Scars in 3 seasons). Settlement Economic Engine (govern 3 settlements, 20 seasons). Long Campaign NPC Turnover (120 seasons, recognizable cast at S100?).

## 4.6 Calibration Report and Issue Triage

THE GATE DOCUMENT. Contains multiplier adjustments, clock tuning, priority tree corrections, coverage gaps. Issue triage: balance-affecting = P1 (resolve before Phase 5), system-specific = P2 (during implementation), cosmetic = P3 (track).

## 4.7 Regression Testing

After any calibration adjustment: re-run Balanced x5. Verify all checks pass. Iterate if regression. Exit criterion: clean pass after final adjustments.

## 4.8 Infrastructure

Python. 16 modules: engine, state, init_validator, faction_ai, scene_slate, combat, fieldwork, contest, threadwork, mass_battle, domain_echo, accounting, npc_arcs, seasonal_events, player_policies, analysis/coverage. File structure under tests/sim_framework/. Output to tests/sim_results/.

---

# PHASE 5: GODOT IMPLEMENTATION PREP

3-4 sessions. Gate: Phase 4 calibration accepted.

**5.1** GM-to-Engine Rule Conversion. Deterministic rules for all GM references across 7 systems (contest ledger, Scar progression, Stunt modifier, Lock domain type, investigation threshold, partial outcome narration, Belief revelation).

**5.2** Godot Implementation Sequence. Core engine -> State management -> Season loop -> Fieldwork -> Combat -> Contest -> Threadwork -> Mass Battle -> NPC AI -> Settlement -> Victory -> UI/UX progressive disclosure.

**5.3** Data Serialization Specification. Markdown design docs to Godot .tres/.res. Templates: faction_data, settlement_data, npc_data, weapon_data, clock_data, territory_data. Schema reference: sim_framework state.py.

**5.4** Godot Scene Tree Architecture. 14 UI states to Godot scene tree. Reference UI/UX v4.1 Appendix E.

**5.5** Cross-Repo Propagation Protocol. ttrpg to valoria-game bridge. [GODOT-IMPACT: system] commit tags. design_sync.md in valoria-game tracking current ttrpg SHA.

---

# PHASE 6: ONGOING MAINTENANCE

Permanent during Godot implementation.

**6.1** Session start: inconsistency sweep (6 steps).
**6.2** After design changes: sim regression (Phase 4.7 protocol).
**6.3** Per commit: standard commit protocol + [GODOT-IMPACT] tag if implementation-relevant.
**6.4** New issues: ED triage P0/P1/P2/P3. P0/P1 gate further implementation.
**6.5** Quarterly: full 50-run simulation baseline. Compare against prior calibration. Flag metric drift.

---

# FLAG INDEX

## P0 (5 items - Phase 0.6 triage)
ED-668, ED-669, ED-670, ED-671, ED-672 (Thread horizontal integration)

## P1 (7 items - Phase 1)
AUD-NPC-01 (Knot formation), AUD-SET-02 (Accord propagation), AUD-DS-01 (derived stats calibration), AUD-FP-01 (faction politics sim), ED-588 (RM Phase 2), ED-589 (RM Presence), ED-612 (Guilds victory)

## P2 (13 items - Phase 2)
AUD-SC-02/03, ED-577-01/02/03/04, AUD-NPC-02, AUD-NPC-03, AUD-SET-01/03, AUD-VIC-02, AUD-MB-02, AUD-COM-04, AUD-TW-01, AUD-UI-01/02, AUD-TW-02

## P3 (18 items - Phase 3)
AUD-COM-01/02/03/05, AUD-SC-01, AUD-TW-03, AUD-PA-02, AUD-NPC-04, AUD-CT-01, AUD-CH-01, AUD-CK-01, AUD-MB-01, AUD-ST-01, AUD-FW-01/02, AUD-VIC-01, AUD-INV-01

---

# EFFORT ESTIMATES

| Phase | Items | Sessions | Dependencies |
|-------|-------|----------|------------|
| 0 Housekeeping | 7 | 1 | None |
| 1 P1 Blockers | 5 | 2-3 | 1.2 -> 1.3 -> 1.4 |
| 2 P2 Calibration | 12 | 3-5 | 2.2 hard dep for Phase 4 |
| 3 P3 Polish | 18 | 2-3 | SIM items before Phase 4 |
| 4 Full-Campaign Sim | 8 sub-items | 8-12 | Phase 1 + 2.2 + 0.7 |
| 5 Godot Prep | 5 | 3-4 | Phase 4 calibration |
| 6 Ongoing | Permanent | - | - |
| **Total** | **55+** | **19-28 sessions** | |

---

# CRITICAL PATH

Phase 0 -> Phase 1.2 -> 1.3 -> 1.4 -> Phase 2.5 -> Phase 4.0 -> 4.2 -> 4.4 -> 4.6 -> 4.7 -> Phase 5

Minimum critical-path sessions: **~16**.

**Phase 4 is the gate.** No Godot implementation until calibration confirms: no death spirals, no stasis, victory S60-100, 100% feature coverage, RS crisis S40-80, NPC arcs >= 4/14 by S60, player impact measurable. P1 issues loop back to Phase 1/2 then re-gate. The gate does not open until the game works on paper.
