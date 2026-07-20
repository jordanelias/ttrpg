# Stage 10 Articulation Simulation — Evaluation

**Date:** 2026-05-01
**Session:** 2026-05-01-stage-10-validation
**Sim:** `sims/stage10_articulation_sim.py` (seed=42, 30 seasons ≈ 7.5 years)
**Output:** `sims/stage10_articulation_sim_output.txt`
**Target:** PP-688 (PROVISIONAL)
**Battery:** PP-688 §8 A1–A6
**Predecessor in session:** lateral cross-system sim (commit bb5e293, 9/9 PASS)

---

## §1 Purpose

Validate PP-688 articulation layer (Tier 2 cut scenes + Tier 3 chronicle) against §8 battery A1–A6. Generate a deterministic 30-season reference Key log, run the significance function + 8-trigger ruleset against it, and verify cut scenes + chronicle are produced as specified.

---

## §2 Battery Results

| # | Test | Expected | Observed | Result |
|---|---|---|---|---|
| A1 | Significance vs authored ground truth | Top-10 ≥80% precision | 9/10 = 90% | PASS |
| A2 | 8-trigger firing rate | 1.5–4 cut scenes/season | 1.60/season (48 over 30) | PASS |
| A3 | Chronicle paragraphs/year | ≥5 per year, no missing years | min=5, 7/7 years | PASS |
| A4 | K/B/I integration | Knot fires + Belief in top-sig + Inspirations engaged | 17 knot cut scenes; belief in top-sig; 6 inspiration scenes | PASS w/ finding |
| A5 | Determinism | Same seed → identical cut scenes + chronicle | hash match; cut sets match; chronicle text match | PASS |
| A6 | Cross-faction clustering | Observation supports Phase B 9th-trigger decision | corr +0.937, signal DETECTABLE | PASS (decision-support) |

**Overall: 6/6 PASS.**

`total_keys=886`  ·  `cut_scenes=48`  ·  `elapsed≈45ms`  ·  `log_hash=3bc292dd43ca40b0`

---

## §3 Test details

### §3.1 A1 — significance vs authored ground truth

Top-10 trigger-matched Keys ranked by significance:

| Rank | sig_t2 | type | season | author beat |
|---|---|---|---|---|
| 1 | 10 | mechanical.mission_shift | s10 | ✓ |
| 2 | 9 | state.succession (contested) | s20 | ✓ |
| 3 | 9 | state.coup_attempted | s28 | ✓ |
| 4 | 9 | meta.knot_formed (K/B/I) | s3 | ✓ |
| 5 | 9 | meta.knot_formed (K/B/I) | s10 | ✓ |
| 6 | 9 | meta.knot_formed (K/B/I) | s17 | ✓ |
| 7 | 9 | meta.knot_formed (K/B/I) | s24 | ✓ |
| 8 | 7 | da.covert_betrayal exposed | s7 | ✓ |
| 9 | 7 | meta.knot_ruptured | s14 | ✓ |
| 10 | 7 | da.covert_betrayal exposed | s9 |   |

Precision: 9/10 = 90% (≥ 80% threshold). The single non-author entry at rank 10 ties on significance with the author beat at rank 9 (both sig=7). Salience tiebreak puts the slightly-higher-salience author beat ahead.

**Spec interpretation note:** PP-688 §8 wording "Top-10 significance Keys overlap ≥80% with author-marked beats" parsed as **precision** (% of top-10 that are author beats), not recall. Precision better matches the design intent — surfacing intended beats as cut scenes — and matches the threshold semantically (a recall metric across all author beats including non-trigger-matched scene.dialogues couldn't reach 80% under any function, since non-trigger Keys cannot become cut scenes regardless of significance).

### §3.2 A2 — firing rate

48 cut scenes over 30 seasons → 1.60 / season; within [1.5, 4.0] target. Per-season distribution skews toward the 1–3 band (no spikes ≥5/season, no empty seasons). Default thresholds at sim parameters:

| Routine source | rate/season | trigger types |
|---|---|---|
| state.scar_acquired | 0.70 | #1 (when actor in tracked set) |
| da.covert_betrayal | 0.45 | #5 (always exposed=True) |
| meta.knot_formed/ruptured | 0.45 | #6 / #7 |
| env.peninsular_strain_shock | 0.10 (moderate, no-trigger) | none |

Authored beats (12 trigger-firing): 8 narrative-arc beats (less state.belief_revised which doesn't trigger) + 4 K/B/I knot_formed events.

### §3.3 A3 — chronicle paragraphs/year

Min 5, max 6 paragraphs/year across 7 years. Structure per §4.4 honored: peninsula opening + per-faction movements (2 factions) + notable individuals + knots/beliefs (when present) + protagonist paragraph. No missing years.

Sample (Year 3):

> Peninsula. The year turned with mechanical.mission_shift (consolidation); its weight set the year's tempo.
> Crown. 28 events shaped its course; the most defining was mechanical.mission_shift (sig=10).
> Hafenmark. 32 events shaped its course; the most defining was env.peninsular_strain_shock (sig=8).
> Notable. Among individuals, haf_leader accumulated narrative weight 153 this year.
> Knots and beliefs. 1 bond/belief inflections this year, including meta.knot_formed.
> The protagonist. 9 events directly involved the protagonist.

Prose is illustrative-shape; production rendering is Phase 5a Godot scope (per PP-688 §8 Phase 5a +1 session for chronicle paragraph generator).

### §3.4 A4 — K/B/I integration (with finding)

| Component | Result |
|---|---|
| `meta.knot_formed/ruptured` fires cut scenes | 17 cut scenes (4 K/B/I authored + 13 routine knots) |
| `state.belief_revised` fires cut scenes | **0** — not in 8-trigger ruleset |
| `state.belief_revised` in top-significance | YES — sig=7 (mid-tier, would qualify if added as trigger) |
| Inspirations engagement Keys | 6 scene.dialogue Keys with `inspirations_engaged_for[protagonist]` payload |

**§3.4 finding (P2):** PP-688 §3.1 8-trigger ruleset omits `state.belief_revised`. The §3.5 K/B/I integration routes belief engagement through payload **bumps** to scene_event significance, not direct triggers. This means a belief-revision Key on its own — without an accompanying scene_event — does not fire a cut scene.

Two interpretations are reconcilable with the spec:
1. **As written** — Belief revisions are surfaced via the chronicle (Tier 3) and via scene_event payload bumps when relevant; direct cut scenes only fire for the 8 listed triggers. A4 passes via the second-order routing (sim observed: belief_revised at s24 has sig=7, top-tier among trigger-matched non-fired Keys).
2. **9th trigger candidate** — Add `state.belief_revised` as trigger #9 (parallel to D10's Phase B 9th-trigger placeholder for cross-faction clustering). Justification: belief revision is a singular protagonist-internal narrative beat that warrants articulation regardless of whether a scene engages it.

Recommendation: defer to Phase B alongside the cross-faction clustering 9th-trigger decision; both are P2 trigger-set extensions. A4.B passes on the "in top-sig" branch.

### §3.5 A5 — determinism

Two runs with seed=42 produce identical Key log hashes (`3bc292dd43ca40b0`), identical cut scene sets (48 scenes each), and byte-identical chronicle text across all 7 years. Confirms PP-688 §8 A5 plus extends PP-687 §6.1–6.3 determinism guarantee through the articulation layer.

### §3.6 A6 — cross-faction clustering (decision support)

Crown β-fid mean 0.854 (var 0.012); Hafenmark β-fid mean 0.802 (var 0.012); cross-faction correlation **+0.937** over 30 samples. Signal classified DETECTABLE (|corr| ≥ 0.30).

**Recommendation for Phase B 9th-trigger (cross-faction clustering, per integration plan §3.4 D10):**

ADD as 9th trigger. Clustering is reliably detectable in 30-season horizon under the test fixture (factions sharing peninsula-scale environmental drivers exhibit synchronous β-fidelity drift). Calibration thresholds for trigger firing should be:

- Detection window: 30 seasons (~7.5 years)
- Correlation threshold: ≥ 0.40 (above MARGINAL band 0.15–0.30 to avoid false positives from coincidental synchronization in short windows)
- Trigger fires once per detection window (not per season) when the correlation criterion is met; emit a `mechanical.cross_faction_clustering` Key (Class B addition to PP-687 type registry)

**Sim-fixture caveat:** the test fixture deliberately encodes a shared peninsula-scale driver via `env.peninsular_strain_shock` distribution. In production play with truly independent faction trajectories, correlation may be lower; calibrate against actual gameplay traces before promoting the trigger threshold.

---

## §4 Findings

### §4.1 P2 — `state.belief_revised` not in 8-trigger ruleset

§3.4 above. Recommended for Phase B trigger-set extension alongside cross-faction clustering. Not blocking promotion.

### §4.2 Tier 3 chronicle structure honors §4.4

All 5 paragraph types from §4.4 produced when source data present. Empty-data fallbacks ("year passed without a defining peninsula-scale event") implemented. Production rendering (Phase 5a) will replace illustrative prose with engine-generated copy from Key payload contents.

### §4.3 Determinism preserved end-to-end

Hash match across substrate Key emission, articulation pass, and chronicle generation. PP-687 §6 determinism extends through PP-688 cleanly.

### §4.4 Significance function calibration is gameplay-dependent

The accumulator cap (max +3 per §3.3) and the K/B/I bumps (§3.5) are calibration-sensitive. Sim-internal values (cap //4, bump magnitudes from §3.5) match spec literally. Production calibration should re-evaluate after Phase 5a Godot integration with actual scene-event distributions; this sim assumes uniform routine generation, which production will not match.

### §4.5 Author-beat density assumption

The 8 narrative-arc beats over 30 seasons (~1 every 3-4 seasons) reflects an assumed authored cadence. Real campaigns may have higher or lower density depending on scenario design. Significance function performance on A1 should be re-evaluated when actual scenario-author beat plans are written.

---

## §5 Decision

**Recommendation:** PP-688 lifts to STRONG-validated. Articulation layer claims at Tier 2 and Tier 3 hold under §8 battery A1–A6.

Combined with the lateral cross-system sim (bb5e293, 9/9 PASS), all sim-testable Stage 10 verification items now pass for PP-684/685/686/687/688:

| Spec | Battery | Status |
|---|---|---|
| PP-687 §9 V1–V6 | PP-687 sim + lateral sim multi-peer | PASS |
| PP-687 §9 V7–V8 | UNVERIFIED (production engine measurement, Phase 5a) |
| PP-686 v2 lateral integration | lateral sim L1–L4, V6 | PASS |
| PP-688 §8 A1–A6 | this sim | PASS |
| PP-684/685 axis matrix | embedded in lateral + articulation sims | PASS (consumed correctly by both sims) |

PROVISIONAL → canonical promotion gates lift on Stage 10 sims; remaining items are:
- §4.1 belief_revised trigger decision (Phase B, P2, not blocking)
- §4.2 substrate visibility-aware subscription (Phase B, P2, not blocking — from lateral sim §4.1)
- §3.6 cross-faction clustering 9th trigger (Phase B, decision now supported by A6 data)

**Promotion ready** pending Jordan signoff on the lifted PROVISIONAL artifacts and the params propagation pass (params/bg/core.md Ethical Framework Modifiers strike, params/factions[_personal].md L+PS fields, faction Mission/cascade/temperament authoring).

---

## §6 Stage 10 Battery Coverage — Final

| # | Property | Source spec | Status |
|---|---|---|---|
| V1 | Cycle-freeness | PP-687 §9 | PASS (PP-687 sim) |
| V2 | Salience monotonicity | PP-687 §9 | PASS (PP-687 sim) |
| V3 | Visibility correctness | PP-687 §9 | PASS (lateral sim, finding §4.1) |
| V4 | Replay determinism | PP-687 §9 | PASS, multi-peer + articulation |
| V5 | Cross-system propagation | PP-687 §9 | PASS, exact + wildcard, multi-peer |
| V6 | PP-686 §3.4/§3.5 formula | PP-687 §9 | PASS, 1e-3 epsilon |
| V7 | Memory query performance | PP-687 §9 | UNVERIFIED — Phase 5a |
| V8 | Walk performance | PP-687 §9 | UNVERIFIED — Phase 5a |
| A1 | Significance vs ground truth | PP-688 §8 | PASS (90% precision) |
| A2 | Trigger firing rate | PP-688 §8 | PASS (1.60/season) |
| A3 | Chronicle paragraphs/year | PP-688 §8 | PASS (≥5, no gaps) |
| A4 | K/B/I integration | PP-688 §8 | PASS w/ §4.1 finding |
| A5 | Articulation determinism | PP-688 §8 | PASS |
| A6 | Cross-faction clustering | PP-688 §8 | PASS (DETECTABLE — supports trigger #9 ADD) |

12/14 PASS. V7/V8 require production engine; not blocking.

---

## §7 Carry-forward

- **§4.1 belief_revised trigger** — Phase B P2 decision; sim suggests ADD as #9 with belief or clustering.
- **§3.6 cross-faction clustering trigger** — Phase B; sim supports ADD as #9 with corr ≥0.40 threshold.
- **Substrate visibility-aware subscription** — Phase B P2 (from lateral sim §4.1).
- **Production calibration** — re-evaluate accumulator cap and K/B/I bump magnitudes against actual scene-event distributions in Phase 5a Godot.
- **Params propagation** — next phase: strike Ethical Framework Modifiers (params/bg/core.md), add L+PS fields (params/factions[_personal].md), author Mission/cascade/temperament for 6 factions + 30-50 territories.
- **Promotion sweep** — PP-684/685/686/687/688 PROVISIONAL → canonical; ED-750..764 + PP-297/351/653 PROVISIONAL→canonical sweep.
