# Valoria Coverage Matrix
# Full historical findings: see tests/sim_batch_*_2026-04-16.md
# This file tracks open findings and recent confirmations only.

## Open Findings (all batches)

| ID | Source | Description | ED |
|----|--------|-------------|-----|
| SIM3-04 | NPC-03 | Arc state vs Priority 6 at Mandate < 3 | ED-586 |
| SIM3-07 | Zoom In | Stability Crisis Zoom In trigger absent | ED-587 |
| SIM4-01 | ST-14 | RM Phase 2 T9 holding condition unreachable | ED-588 |
| SIM4-02 | ST-14 | RM Presence marker mechanics undefined | ED-589 |
| SIM5-01 | ST-21 | No Parliamentary block on Tribune actions | ED-616 |
| SIM5-02 | ST-22 | Grand Contest Recall: once-per-source fix | ED-617 |
| SIM5-04 | ST-23 | Torben Conviction window: S1-8 formal def | ED-618 |
| SIM5-13 | ST-28 | 3-Obligation GM advisory cap | ED-619 |

## Active P1 EDs Requiring Design Action

| ED | Description |
|----|-------------|

## Resolved This Session (summary)

15 items resolved. See sim_batch archives for details.
Key: ED-588/589 (RM), ED-612 (Guilds), AUD-SET/VIC/NPC, SIM-DEBT-03/04,
ED-577-01-04, SIM-POL-R01-R05, ED-684, ED-590, ED-572, ED-545+.


> **Historical batches archived.** This sweep moved: 2026-05-03 telemetry sim, Vocabulary Sweep + ners_stress_01 Modules 1–2 (2026-05-08), and combat_arch_residual_stress_01 R1–R6 (2026-05-09; superseded by D-module summary below) to `tests/coverage_matrix_archive_2026_05_10.md`. Earlier sweeps: ED-786 (2026-05-02) → `tests/coverage_matrix_archive_2026_04_19.md`; initial → `tests/coverage_matrix_archive.md`; pre-v3 → `deprecated/sim_coverage_matrix_legacy.md`. This active file tracks unresolved findings, active P1 EDs, and recent (2026-05-09 manifest + 2026-05-10) session summaries.

## Recent Sims (2026-05-09)

| Sim | Scope | Result |
|-----|-------|--------|
| combat_arch_residual_stress_01 (manifest) | Combat videogame architecture R1–R10 residual-risk sweep, Mode G + Mode A/B/D per module. Pressure-tests the 2026-05-01 EXPLORATORY composite stack residual risks (wound permanence, skill input in C, mass three-mode reframe, hero participation, wager stake range, Fibonacci cap, friendly fire, fieldwork-tempo shift, two-arch sufficiency, IP-gauge threshold). | Module 0 manifest committed. Modules R1–R10 pending. PP-684 collision resolved (4/18 set renumbered to PP-711..715 per fce5953); registry drift on combat/derived_stats design_doc fields documented. |
### combat_arch_residual_stress_01 Module 7 R7 — verified 2026-05-10 (PP-716 canon)
Friendly fire & ranged in melee. Canon currently silent — implicit no-FF default. **Recommendation: C7.4 (FF on stress only — ≥1 Wound OR Composure ≤3 OR environmental degradation).** Leverages existing canonical wound/Composure/environmental channels; no new dice mechanic. Thematically consistent with PP-716 wound-penalty universality. **Fallback: C7.1 (no FF, preserve canon-silence)** if Jordan determines stress-spec work isn't justified. C7.2 (FF on every miss) marginal — per-miss adjudication overhead. C7.3 (separate d10 roll) marginal — non-canonical dice channel, stylistically inconsistent. Spec gap (P1): stress threshold criteria need explicit enumeration on adoption.
### combat_arch_residual_stress_01 Module 8 R8 — verified 2026-05-10 (PP-716 canon)
Fieldwork↔combat tempo shift. **Synthesis premise was a spec-gap that doesn't exist** — combat_v30 §11.5 already specifies the tempo model completely. **Recommendation: C8.2 (partial freeze — current canon).** One-way state coupling: Exposure propagates forward at entry (R8-L01); fieldwork state persists across combat (R8-L03); combat doesn't consume fieldwork time (R8-L02); battle-site investigation = 1 post-combat fieldwork scene (R8-L05); Evidence decays +1 Ob/season at fled sites (R8-L06). C8.1 full-freeze rejected (contradicts Exposure / Evidence propagation). C8.3 continuous-tempo categorical reject (contradicts R8-L02; dual-clock bookkeeping; time-laundering exploit).
### combat_arch_residual_stress_01 Module 9 R9 — verified 2026-05-10 (PP-716 canon)
Two-architecture sufficiency. **Recommendation: C9.1 (A+C only)** — synthesis Q5 reduction holds. B-shaped encounter shapes (corridor ambush, dungeon room, tavern brawl) all map to A+S7-hybrid via zone-size + actor-count parameters. C9.2 (restore B) marginal — three combat UIs, B-as-orphan-mid-tier. C9.3 (B-shape presentation flag) PASS as optional UX refinement: presentation-only contrast for fixed-position-set-piece encounters without mechanical bifurcation.
### combat_arch_residual_stress_01 Module 10 R10 — verified 2026-05-10 (PP-716 canon)
IP-gauge legibility / actor-count threshold. **Recommendation: C10.2 (collapse at ≥6 actors; player + named NPCs retain individual gauges; mooks aggregate into faction-bands or position-bands).** Threshold aligns with Fibonacci zone-collapse trigger R10-L08 (3+ = group combat). At 6+ actors individual interrupt-timing decisions become rare anyway. C10.1 always-full UX failure at scale. C10.3 hide-at-≥8 too aggressive. C10.4 adaptive-zoom marginal — benefits achievable via C10.2 + zoom cosmetics without spec coupling.

### combat_arch_residual_stress_01 (D module) — ALL 10 R-MODULES COMPLETE 2026-05-10
Final decisions: R1 C1.3 / R2 C2.1 / R3 C3.3 / R4 C4.2 / R5 C5.1 / R6 C6.1 / R7 C7.4 (or C7.1 fallback) / R8 C8.2 / R9 C9.1 / R10 C10.2. PP-716 wound correction landed mid-task; R1 redone as v2. Synthesis premises corrected on R3/R5/R8 (canon already mature). Ready to proceed: A (conviction_stress_01) → F (personal-scale lifecycle bundle) → G (setup & ignition).
### combat_arch_residual_stress_01 — D-Stress Test COMPLETE 2026-05-10
All 10 R-modules verified against PP-716 canon. Manifest cleaned: M4-M10 row status updated (pending → verified with SHAs); redundant appended notes stripped; D-stress completion summary added. Recommendations: R1 C1.3, R2 C2.1, R3 C3.3, R4 C4.2, R5 C5.1, R6 C6.1, R7 C7.4 primary/C7.1 fallback, R8 C8.2, R9 C9.1, R10 C10.2. Synthesis-canon discrepancies surfaced for R3 and R5 (canon already mature; synthesis premise partially obsolete). Deferred refinements: R4 C4.3 (T-trigger spec), R5 C5.3 (voluntary stake escalation), R7 stress threshold enumeration, R8 partial-freeze ticker selection, R9 routine-encounter B reservation. Next: A module (conviction_stress_01).
### conviction_stress_01 — A-module verified 2026-05-10 (PP-684 canon)
Conviction Taxonomy + Axis Matrix stress test. Single-module Mode A coverage across 4 dimensions (96 cells): taxonomy completeness, axis matrix coherence, Self-Other orthogonality, structured concentration tractability. **Recommendation: A1 (preserve PP-684 13-Conviction taxonomy + 52-cell axis matrix).** All four NERS dimensions pass; no categorical fail. **P1 drift defect surfaced:** `npc_behavior_v30 §1.2` redirects readers to stale `conviction_track_v1.md` (9-Conviction set) rather than canonical PP-684 13-Conviction `conviction_taxonomy_v30.md`. Recommended follow-up PP to fix redirect + verify Scar accumulation mechanic interacts with structured concentration. Five ⚠ deferred refinements: Community/Identity collinearity, Order/Authority collinearity, 5th-axis trigger spec, Self-Other UI display, cultural template count.
### fieldwork_lifecycle_stress_01 — F-module verified 2026-05-10 (PP-684/ED-773 canon)
Personal-scale lifecycle bundle. **F2 Knot Lifecycle verified focal analysis** (12 ledger entries, 24-cell NERS, 5 Mode B chains, 8 Mode D edge cases). Recommendation: F2.1 (preserve canonical; no mechanical changes). Knot Lifecycle is mature post-ED-773; R1 v2 C1.3 recommendation grounded by F-L10 (FR Dissolution → +1 Wound + Knot rupture) + F-L11 (Close Knot break → Conviction Scar +1 both). One spec ambiguity flagged (EC-F2.A-01 sustained Disposition reduction definition). **F1 Wager covered in R5** (no further analysis). **F3 Heresy Investigation DEFERRED** to follow-up session. **F4 Mending DEFERRED** to follow-up; PP-716 −1D Pool with floor 5D already validated in R1 v2 Chain 2 (no extinction cascade).
### setup_ignition_stress_01 — G-module verified 2026-05-10
Setup & ignition state audit across three sub-modules: B4 Tensions Deck, B17 Geography Phase 2, B19 Niflhel dissolution. Per-sub-module recommendations: **B4 Tensions Deck NOT YET DESIGNED** — substantial design initiative requiring Jordan's authoring direction (separate session). **B17 Geography Phase 2 COMPLETE** per ED-779 / PP-710 (28,319-byte valoria_geography_v30.yaml at canonical 1920×2880; 17 territory anchors, 36 settlements, 26 adjacency edges, 20 terrain polygons); ED-780 Phase 3 (settlement_adjacency rewrite + march_layer) and ED-781 Phase 4 stress tests are standing carryovers. **B19 Niflhel dissolution DONE in core canon** (npc_behavior §2.12 STRUCK; conflict_architecture_proposal); ED-777 standing (5 arcs require reframe per Jordan's 2026-05-09 decision: ARC-S11, S54, S55, NPC-ARC-VIR, T25). NERS coherence analysis: 17/24 ✓, 7 ⚠ — most ⚠s tied to B4 Tensions Deck gap. **D-A-F-G stress sweep COMPLETE.** Consolidated next-session priorities documented in setup_ignition_stress_01.md §5.
### setup_ignition_stress_01 — AMENDMENT 2026-05-10
**B4 Tensions Deck correction:** original G-module (commit `cab3bd85`) found B4 "NOT YET DESIGNED" — this was incorrect due to incomplete source survey. Subsequent canonical-source check found `params/bg/tensions_deck.md` (CANON per `conflict_architecture_proposal.md` 2026-04-18) with full 6-card spec + fuse model. **Revised verdict: B4 Tensions Deck COMPLETE.** No design initiative needed. Setup pipeline now fully canonical; remaining work is ED-777 (arcs), ED-780 (Phase 3 geography), ED-781 (Phase 4 stress tests). G module amended with §7 amendment block + ledger annotation.
### fieldwork_lifecycle_stress_01 F3 Heresy Investigation — verified 2026-05-10
F3 Heresy Investigation lifecycle audit. 10 ledger entries; 24-cell NERS; 5 Mode B chains; 8 Mode D edge cases. **Recommendation: F3.1 (preserve canonical lifecycle).** Lifecycle mature post-ED-625 (Excommunication Tribunal) / ED-670 (extra-territorial jurisdiction) / PP-349 (Church self-investigation exception). 22/24 NERS pass; 2 ⚠ on Horizontal (PC severity scaling — intentional sword-of-Damocles per F3-L10). One editorial defect surfaced: PP-349's "collaborating with Niflhel" example stale post-Jordan's 2026-05-09 dissolution decision (G-L03); PP-722 follow-up flagged.
### fieldwork_lifecycle_stress_01 F4 Mending — verified 2026-05-10
F4 Mending lifecycle audit + PP-716 propagation re-validation. 13 ledger entries; 24-cell NERS; 5 Mode B chains; 8 Mode D edge cases; PP-716 propagation re-validation (4 sub-chains). **Recommendation: F4.1 (preserve canonical Mending lifecycle; no mechanical changes).** 22/24 NERS pass; 2 ⚠ Horizontal (Critical-band endgame intentional Einhir Catastrophe Mechanism + board-game discoverability via Investigate Thread). **PP-716 −1D Pool with floor 5D propagation through Mending operations produces friction loop, not extinction** — R1 v2 Chain 2 verdict reaffirmed. Mending Coherence-zero asymmetry preserved under PP-716. Cross-mode aggregation (TTRPG Mending + board-game Mend order) at Accounting clean. **F-bundle COMPLETE:** F1 covered in R5 (commit d46ad908); F2 Knot Lifecycle (commit ddccbf9a); F3 Heresy Investigation (commit 8de82dbb); F4 Mending this commit.
### geography_phase4_stress_01 — Phase 4 stress tests verified 2026-05-10 (ED-781 closure)
Three scenarios queued by ED-781 executed:
1. **Mountain Pass (T10↔T11 Halvardshelm-area)** — Phase 3 mechanics produce coherent narrow-pass-clamp emergence; defender +3D differential; no spec gaps (calibration playtest recommendation only).
2. **Open-field cavalry (T2 Kronmark plains)** — Phase 3 mechanics produce coherent declaratory-flanking + geometry-restricted resolution; cavalry +1.5× march budget + plains-flanking +1D; no spec gaps.
3. **Coastal landing (Schoenland T16 → T13 Oastad)** — **P1 spec gap surfaced: no canonical sea-zone adjacency** between non-T1 coastal territories. Phase 4 surfaces what Phase 2 didn't include and Phase 3 doesn't provide. **ED-055 (naval) scope must populate sea-zone polygon+adjacency definition** before amphibious operations are canonically resolvable. Affected: any Schoenland-pivot scenarios assuming sea projection.

**ED-781 closure:** Phase 3 verified for land-based mass battle; Phase 4 reveals P1 substrate gap blocking coastal operations on ED-055. 10 ledger entries; 3 scenarios; 6 Mode D edge cases; cross-scenario synthesis.
