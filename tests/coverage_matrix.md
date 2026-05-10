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

## Recent Sims (2026-05-03)

| Sim | Scope | Result |
|-----|-------|--------|
| sim_telemetry_substrate_2026-05-03 (v2) | Phase 5a session 3.5 telemetry substrate (mandatory zoom-in frequency + SA-budget saturation, arc-driven correlation) | 4 personas × 100 campaigns × 40 seasons = 16k season-runs. v1 (independent triggers): 0% mandatory overflow across personas; mandatory p90 ~1.6. v2 (arc correlation: stability_crisis→revolt+succession, mass_battle→revolt, leader_removal→companion_arc, heresy→knot_crisis): mandatory overflow 0% Narrative/Normal, **0.4% Hard** (1 in 250 seasons under correlation); mandatory p90 lifts to 2.0 (+26%). Saturation unchanged: 96% Normal / 100% Hard / 36% Narrative. Per-system minutes use tabletop §12.3 placeholder durations — flagged [ASSUMPTION]. |


---

> **Historical batches archived.** All sim findings from 2026-04-17 to 2026-04-19 (inclusive) moved to `tests/coverage_matrix_archive_2026_04_19.md` per ED-786 archival sweep 2026-05-02. This active file tracks only unresolved findings, active P1 EDs, and the most-recent session summary.

## Vocabulary Sweep (2026-05-08)
All test/sim files updated: TC→CI, Peninsular Strain→Turmoil, Conviction Track→Piety Track, contest Initiative→First to Speak.

## Recent Sims (2026-05-08)

| Sim | Scope | Result |
|-----|-------|--------|
| ners_stress_01 (manifest) | NERS stress test — randomized starting conditions, all directions, Mode G | Module manifest committed. Module 1 (randomization layer) pending. Module 2 (NERS evaluation + batch) pending. |

### ners_stress_01 Module 1 (2026-05-08)
Module 1 randomization layer: 5 smoke tests PASS. Status: verified.

### ners_stress_01 Module 2 (2026-05-08)
NERS batch: 300 runs. No P1/P2 findings. All NERS signals >= 0.60. All 4 factions win. 52-67% ongoing at s60 — Tier A AI conservative strategy.
## Recent Sims (2026-05-09)

| Sim | Scope | Result |
|-----|-------|--------|
| combat_arch_residual_stress_01 (manifest) | Combat videogame architecture R1–R10 residual-risk sweep, Mode G + Mode A/B/D per module. Pressure-tests the 2026-05-01 EXPLORATORY composite stack residual risks (wound permanence, skill input in C, mass three-mode reframe, hero participation, wager stake range, Fibonacci cap, friendly fire, fieldwork-tempo shift, two-arch sufficiency, IP-gauge threshold). | Module 0 manifest committed. Modules R1–R10 pending. PP-684 collision resolved (4/18 set renumbered to PP-711..715 per fce5953); registry drift on combat/derived_stats design_doc fields documented. |
### combat_arch_residual_stress_01 Module 1 R1 wound permanence (2026-05-09)
NERS at full grain, 4 candidates × 24 cells = 96 cells. C1.1 pure canonical: PASS (5/6 N+R, 6/6 E+S; ⚠ Horizontal narrative-weight gap). **C1.2 catastrophic-permanent: REJECT** — categorical R-fail (Pool floor 5D reverses canonical resilience hierarchy: 12D pool→5D over 7 wounds vs 5D pool→5D zero loss; Threadwork +1 Ob unfloored produces practitioner extinction over 5–10 sessions) and S-fail (contradicts canonical "Wounds clear at session end" R1-L06). C1.3 Knot-tagged: PASS 24/24 — uses existing Conviction Scar channel (P1) per derived_stats §Conviction. C1.4 all-permanent: REJECT (multi-axis categorical fail). **Recommendation: C1.3** — preserve canonical session-end clearance; route narrative permanence through existing Scar apparatus. Surfaced findings: (a) Pool floor 5D is load-bearing for asymmetry analysis; (b) Threadwork penalty unfloored is independent stress-test candidate; (c) fieldwork_v30 §3 line 364 has stale PP-684 citation needing post-renumber update.

### combat_arch_residual_stress_01 Module 1 R1 — SUPERSEDED 2026-05-09 (PP-716)
The Module 1 R1 finding (commit 45c693e2) was authored against pre-PP-716 canon (Vitality = End × 10; Threadwork +1 Ob per Wound). Both formulations reverted by PP-716. Banner added to r1_wound_permanence.md. Decision-shape recommendation (C1.3 Knot-tagged via Conviction Scar) needs re-derivation: the Pool floor 5D asymmetry argument may survive (Combat Pool floor unchanged), but the Threadwork extinction cascade argument is no longer applicable (wounds give −1D Pool, not +Ob, and Thread Pool has its own floor 5). Module 1 R1 to be redone in subsequent session.

### combat_arch_residual_stress_01 Module 1 R1 v2 — verified 2026-05-09 (PP-716 canon)
Module 1 redone against PP-716 corrected canon. r1_wound_permanence_v2.md supersedes v1 (commit 45c693e2). NERS at full grain (96 cells, PP-716 ledger), Mode B (5 chains, Chain 2 Threadwork rewritten under −1D Pool floor 5D model), Mode D (15 edge cases — practitioner-extinction cascade EC-D1.C-01 REMOVED; multiple P1→P2/P3 downgrades). **Recommendation UNCHANGED: C1.3 (Knot-tagged via existing Conviction Scar channel).** Pool asymmetry argument bounded by MW under PP-716 (3D gap vs v1's 7D); ambiguity argument intact; canon contradiction intact. Ready to proceed to Module 2 (R2 skill input layer in Architecture C).
### combat_arch_residual_stress_01 Module 2 R2 — verified 2026-05-09 (PP-716 canon)
Architecture C (duel) skill-input layer. NERS full grain (96 cells), Mode A probability tables across pool 4D-15D and stat-vs-skill matrix. **Recommendation: C2.1 (pure dice, cognitive layer only) — Pirates! E5 + Sekiro E7 already adopted carry C-distinctiveness; no real-time motor-skill needed.** C2.2 (cap +1 net hit) viable fallback if genre-expectation gap unacceptable. C2.3 (cap +2) marginal — stat relevance halved at 4D pool. C2.4 (uncapped) categorical reject — contradicts TTRPG-baseline scaling (R2-L02), inverts stat hierarchy (Section 5: low-stat with skill 5.15 vs high-stat without 3.96), nullifies Combat Pool math. Open: spec the Stunt-style tabletop fallback in C2.2 implementation if Jordan adopts.
### combat_arch_residual_stress_01 Module 3 R3 — verified 2026-05-09 (PP-716 canon)
Mass-battle three-mode reframe. Coverage analysis. Key finding: synthesis premise partially obsolete — v30 canon already merged TTRPG and Hybrid into Part A (R3-L01 "Three-mode: TTRPG/Hybrid (Part A); Board Game (Part B); Hybrid Handoff (§B.5)") on 2026-04-17 (R3-L07). No mechanical restructure needed. **Recommendation: C3.3 (preserve canonical structure + add I-tier↔Part phase-mapping table to top of mass_battle_v30)** — single doc edit, ~30 lines. C3.2 cosmetic rename rejected (high propagation cost for cosmetic clarity over already-resolved structure).
### combat_arch_residual_stress_01 Module 4 R4 — verified 2026-05-09 (PP-716 canon)
Hero participation default. Three-tier model: Tier 0 absent (BG + Where-Were-You), Tier 1 present-strategic (commander, default), Tier 2 present-scene (Zoom In opt-in via §B.5 phase-lock). **Recommendation: C4.2 (default-off; Tier 1 baseline).** Canon-aligned per §B.5 framing (R4-L01). C4.1 categorical reject (contradicts §B.5; per-battle overhead; starves named-officer Disposition R4-L03). C4.3 deferred pending T-trigger spec.
### combat_arch_residual_stress_01 Module 5 R5 — verified 2026-05-09 (PP-716 canon)
Wager stake range. **Re-asked** against actual canon: synthesis premise partially obsolete — canon's Wager Obligation per §6.1.1 (post-ED-778) is mature; stake severity encoded structurally via contest type (R5-L01) rather than via parallel stake-magnitude tag. **Recommendation: C5.1 (preserve canonical).** C5.2 stake-severity tag rejected (redundant with contest-type hierarchy). C5.3 voluntary stake escalation deferred — genuine player-agency value but substantial cross-system coupling; recommend treating as separate design initiative. Cosmetic-stake gap (tavern games, dueling purses) routed to fieldwork-Socializing, not Wager.
### combat_arch_residual_stress_01 Module 6 R6 — verified 2026-05-09 (PP-716 canon)
Fibonacci Group Bonus cap. **Recommendation: C6.1 (preserve canonical +5 cap at 8+ attackers).** R6-L01 table mature per PP-216. Δ-net +1.65 at saturation produces tactically significant advantage without breaking defender Pool relevance. C6.3 no-cap categorical reject (certain-victory regime at 13+ attackers; mass-scale uncapped collapses resolution math entirely). C6.4 asymptotic reject (fractional dice contradicts integer-dice convention). C6.2 raise-cap marginal (rare problem, moderate cost).
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
