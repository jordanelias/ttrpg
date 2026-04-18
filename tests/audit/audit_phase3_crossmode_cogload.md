# VALORIA PHASE 3 AUDIT — CROSS-MODE TRANSITIONS + COGNITIVE LOAD + REMAINING SYSTEMS
## Date: 2026-04-04
## Scope: Cross-mode transition fidelity, cognitive load scoring, remaining compilation stages
## Status: Phase 3 of 3 — AUDIT COMPLETE

---

## SUMMARY

| Severity | Count |
|----------|-------|
| P1 | 2 |
| P2 | 4 |
| P3 | 3 |

All PP-232/PP-234 terminology propagation across compilation stages: COMPLETE (committed dfa0e6b).

---

## A. REMAINING SYSTEMS — COMPILATION STAGES

| Stage | Status | Findings |
|-------|--------|----------|
| stage1_core_engine | CLEAN | — |
| stage2_characters | FIXED | 1 Memory→Recall |
| stage4_southernmost | FIXED | 2 Memory→Recall, 1 Cohesion→Discipline. ED-048 (Ceiral) still open. |
| stage5_clocks | EMPTY | Stub file. |
| stage6_factions | CLEAN | — |
| stage7_territories | CLEAN | — |
| stage10_advancement | FIXED | 1 Memory→Recall, 2 Presence→Charisma |
| stage11_scale_transitions | FIXED | 1 Coherence Rating→Command |
| stage12_campaign_modes | CLEAN | — |
| stage13_npcs | FIXED | 7 Presence→Charisma. 1 "Coordination" flagged stale. |
| stage14_gm_tools | CLEAN | — |
| stage15_spell_catalog | EMPTY | Stub file. |

### AUD-P2-09: stage13 NPC "Coordination" attribute
NPC stat block lists "Coordination 4, Power 4" — not defined attributes. Likely Agility and Strength. Flagged inline.

---

## B. CROSS-MODE TRANSITION FIDELITY

### Eight Handoff Rules

| # | Transition | Procedure Complete? | Gaps |
|---|-----------|--------------------|----|
| 1 | Personal → Thread | ✓ | — |
| 2 | Personal → Faction | ~✓ | "Same roll" ambiguity (minor) |
| 3 | Personal → Scene | ✓ | — |
| 4 | Scene → Faction | ✓ | ED-071 Domain Echo cap provisional |
| 5 | Thread → Faction | ✓ | — |
| 6 | Thread → Mass | ✓ | PP-191 Lock phase provisional |
| 7 | Mass → Personal | ✓ | Clean (Command suspension, 5-exchange cap) |
| 8 | Scene → Mass | **Underspecified** | See AUD-P1-15 |

### AUD-P1-15: Scene → Mass transition underspecified
Rule says "apply to mass combat opening state before next round declaration" but doesn't specify: which stats change (faction only or unit?), whether Domain Echo fires immediately or queues, or whether Composure damage affects Command. Needs procedural definition.

### AUD-P1-16: 17 Hybrid gap resolutions not integrated
hybrid_gaps_resolved.md has 17 resolved gaps not in stage11. Integration pending (~0.5 session).

---

## C. COGNITIVE LOAD SCORING

| System | Decisions/round | Tracked Vars | Score | Rating |
|--------|----------------|-------------|-------|--------|
| Personal Combat | 3 | 4 | 7.7 | Moderate |
| Thread Operations | 4 | 6 | 12.8 | Heavy |
| Social Contest | 4 | 5 | 11.0 | Heavy |
| Mass Combat (3 units) | 12 | 13 | 14.5 | Very Heavy |
| BG Turn (per faction) | 4 | 6 | 8.6 | Moderate-Heavy |
| **Thread in Mass Combat** | **8+** | **8** | **19.4** | **EXTREME** |

**Peak load:** Thread Operations during Mass Combat (score 19.4). Practitioner-general in Phase 4 tracks both Thread state and mass battle state simultaneously. PP-201 campaign-impact warning addresses awareness; mechanical tracking burden remains extreme.

### Optimization Recommendations (no texture loss)

| ID | Optimization | Load Reduction | Effort |
|----|-------------|----------------|--------|
| OPT-01 | Pre-printed ×3 RS cost sheet for mass battle Thread | −1.0 score | Low |
| OPT-02 | Strain table reference card for social contest | −0.75 score | Low |
| OPT-03 | Unit stat cards with degradation tracking | −1.0/unit | Low |
| OPT-04 | GM mode-transition flowchart | −1.0 at boundaries | Medium |

---

## D. CRUNCH CASCADE FINAL ASSESSMENT

No unbounded cascades. All cascade chains properly bounded by caps or floor rules. Thread RS drain in mass combat (×3) is campaign-ending by design with mandatory GM disclosure (PP-201/PP-204).

---

## E. EDITORIAL ITEMS REQUIRING USER DECISIONS

| ID | Description | Options |
|----|------------|---------|
| ED-139 | Community Weaving triple spec | A: Two separate actions — rename. B: PP-195 supersedes — strike older. C: Merge. |
| ED-140 | Discipline degradation asymmetry | A: Add Power-diff precondition. B: Remove asymmetry constraint from PP-231. |
| ED-142 | BG Overwhelming threshold | A: 2×Ob (PP-179). B: Ob+1 (ED-031). State floor explicitly either way. |

---

## F. FULL AUDIT SUMMARY

### Commits This Session (5)
| SHA | Description |
|-----|------------|
| d72fb57 | Phase 1 — 18 term fixes + ED-139–142 |
| 251ea34 | Phase 2 — audit reports + stale warnings |
| 671325f | PP-232/PP-233 propagation — 4 canonical design docs |
| dfa0e6b | PP-232/PP-234 propagation — 5 compilation stages |
| [pending] | Phase 3 report |

### Total Work
- 1 P0 resolved (canonical source integrity)
- 8 P1 mechanical fixes applied
- 7 P2 fixes applied
- 4 canonical design docs rebuilt/updated
- 5 compilation stages corrected
- ~110 individual terminology corrections across 14 files
- Cross-mode transition audit (8 handoff rules, 2 gaps found)
- Cognitive load scored (6 systems, peak identified)
- Crunch cascade analysis (6 chains, all bounded)

### Remaining Open
| Type | Items |
|------|-------|
| Editorial (user decision) | ED-139, ED-140, ED-142 |
| Integration | AUD-P1-16 (17 Hybrid gaps) |
| Tooling | ED-141 (contest reference card) |
| Underspecified | AUD-P1-15 (Scene→Mass procedure) |
| Sim debt (deferred) | SIM-DEBT-03, SIM-DEBT-04 |
