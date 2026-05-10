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
