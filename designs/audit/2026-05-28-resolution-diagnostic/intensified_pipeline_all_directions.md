# Intensified Pipeline Analysis — All Directions · All Scales · All Scopes

**Date:** 2026-05-28
**Task:** Intensify the resolution analysis to granular, computed, cross-cutting detail — running the *logic pipelines* across the full scale ladder (all scales), the cross-scale propagation paths (all scopes), and the six analytic directions, rather than per-system at the system grain.
**Method:** Four Monte-Carlo pipelines (120k/cell dice; 6k/cell combat fights), authoritative die rule (face 1 = −1, 7–9 = +1, 10 = +2; TN 7), validated μ = 0.40/die. This run **computes** the things prior passes asserted or flagged as sim-only.
**Bias:** `[SELF-AUTHORED — bias risk]` — extends my own diagnostic/armature work; §8 turns the critique on the combat sim's own assumptions.
**What's genuinely new here:** Pipeline 2 closes `derived_stats_audit`'s explicit `[GAP: cross-axis offense-vs-survival — sim-only]`; Pipelines 1/3/4 quantify ER-3 (pool-size shock), the Domain-Echo propagation magnitude, and the intent_of_game loop gain — none of which existed as numbers before.

---

## Pipeline 1 — Scale ladder, granular per rung (ALL SCALES)

The canonical ladder raises Ob with scope (Object 1 → Personal 2 → Relational 3 → Territorial 4 → Structural 5+ → Foundational 8+; `params/scale_transitions.md`). Running the *same* actor pools against each rung's Ob:

| Rung | Ob | 2D | 5D | 8D | 12D | 18D | A1 flat-mod swing |
|---|---|---|---|---|---|---|---|
| Object | 1 | 58% | 80% | 89% | 94% | 98% | n/a (Ob 1) |
| Personal | 2 | 26% | 60% | 77% | 88% | 96% | 20%@5D → 2%@18D |
| Relational | 3 | 7% | 38% | 61% | 79% | 92% | 22%@5D → 4%@18D |
| Territorial | 4 | **1%** | 20% | 44% | 68% | 86% | 18%@5D → 6%@18D |
| Structural | 5 | **0%** | 8% | 28% | 53% | 79% | 11%@5D → 8%@18D |
| Foundational | 8 | **0%** | **0%** | 3% | 17% | 46% | 1%@5D → 12%@18D |

**Findings (computed):**
- **Foreclosure is scale-gated.** A 2D bare pool is fine at Object/Personal (58%/26%) but **forecloses (≤1%) from Territorial up.** The bare-stat pathology (faction F1 / ER-1) is therefore *specifically a high-rung phenomenon* — because Ob climbs with scope while a bare stat pool does not. This is the granular mechanism behind the faction-layer's failure: faction Domain Actions live at Territorial/Structural (Ob 4–5), exactly where small pools die.
- **ER-3 "pool-size shock" quantified.** A fixed 5D actor degrades 80% → 60% → 38% → 20% → 8% → 0% across the ladder. The same competence is *routine* at Object and *impossible* at Foundational. This is the cross-scale non-uniformity, now numeric per rung — and it is **engine-invariant** (any resolver mapping a 1–7 stat across this Ob range shows it; not a dice artifact).
- **A1 non-uniformity is itself scale-shaped.** Flat-modifier swing peaks at small-pool-mid-rung (22%@5D Relational) and *inverts* at Foundational (1%@5D vs 12%@18D) — at the top rung small pools are already ~0, so a flat mod barely moves them while it matters to large pools. The A1 fix (σ-space / aggregation) matters most at the mid rungs where small pools are live-but-fragile.

---

## Pipeline 2 — Cross-axis sim: +1 Agility (offense) vs +1 Endurance (survival) — CLOSES THE SIM-ONLY GAP

`derived_stats_audit` §5 flagged this as unanswerable by derivation: *"does a point of Agility (offense, via Pool) matter as much as a point of Endurance (survival, via Health)? ... only combat simulation answers. [GAP — sim-only]."* Running a minimal faithful combat sim (Pool = Agi×2+3 split off/def; Health = (End+6)(MW+1); simultaneous net-hit damage ×(1+Power); wound −1D; first to 0 loses):

| Matchup | Win rate vs (Agi 3, End 3) |
|---|---|
| Even (3,3) — sanity | 48.4% (≈50% ✓) |
| **+1 Agility** (Agi 4, End 3) | **73.0%** |
| **+1 Endurance** (Agi 3, End 4) | **71.5%** |
| +1 Both (Agi 4, End 4) | 88.5% |

**At the low/typical band, offense and survival are balanced** — a point of Agility (+2.5pp over a point of Endurance) ≈ a point of Endurance. The cross-axis trade the derivation couldn't settle is **balanced at baseline.** Reassuring, and previously unknown.

**But the balance breaks at high builds — and the cause is the MW cap:**

| Higher band | Win rate |
|---|---|
| +1 Agility (6,5) vs (5,5) | **71.7%** |
| +1 Endurance (5,6) vs (5,5) | **52.0%** |

At End 5→6, MaxWounds is already capped at 3 (reached at End 4), so the Endurance point buys only a flat +4 Health (~9%) while the Agility point still buys +2D pool. **Endurance's win-rate leverage collapses from ~+22pp (low band) to ~+4pp (post-cap); Agility's holds at ~+23pp throughout.** Confirmed directly:

| +1 Endurance step | Win rate vs (3,3) |
|---|---|
| End 3→4 (MW 2→3, *across* step) | 49% → **71%** (+22pp) |
| End 4→5 (MW capped) | 71% → **76%** (+5pp) |

**This is the major result.** It promotes `derived_stats` D1 from "Health *points* are non-uniform" to a **win-rate finding: the MaxWounds cap (End 4) breaks offense/survival parity at high builds** — past End 4, every point goes to Agility because Endurance has stopped buying survival. A min-maxer caps Endurance at 4 (the last MW step) and dumps everything into Agility. The MW-step non-uniformity isn't just a Health-curve wrinkle; it distorts the *entire high-build attribute economy* toward offense.

---

## Pipeline 3 — Cross-scale propagation gain (ALL SCOPES / diagonal)

Does low-scale play meaningfully move high-scale state? Tracing the canonical propagation paths:

**Domain Echo** (personal Overwhelming = +2 faction stat; `params/scale_transitions.md` PP-108/109) → effect on the faction's *next* Domain Action:

| Faction stat | P(action) before → after +2 | gain |
|---|---|---|
| 2 → 4 | 25.9% → 51.2% | **+25.3pp** |
| 3 → 5 | 40.3% → 59.9% | +19.6pp |
| 4 → 6 | 51.2% → 67.1% | +15.9pp |

**Scene → Mass** (social/combat win = +1D unit Command, 1 turn; PP-261/ED-151):

| Command | P(exchange) before → after +1D | gain |
|---|---|---|
| 2 → 3 | 28.0% → 46.8% | **+18.8pp** |
| 3 → 4 | 46.8% → 61.4% | +14.6pp |
| 4 → 5 | 61.4% → 72.0% | +10.7pp |

**Findings:**
- **Propagation is substantial, not cosmetic.** A single personal Overwhelming swings the faction's next action by **+15–25pp**; a scene win swings a mass exchange by +11–19pp. Low-scale play genuinely moves high-scale outcomes — the cross-scale currency (degree → stat) carries real weight, validating the "personal play matters strategically" design intent with numbers.
- **The lever is a rubber-band (gain decays with strength).** +25pp for a weak faction (stat 2) down to +16pp for a stronger one (stat 4) — the same √N saturation. This is *good* design: cross-scale wins help the underdog most, naturally rubber-banding the strategic layer without an explicit catch-up mechanic.

---

## Pipeline 4 — intent_of_game loop gain (TOP-DOWN): self-damping, proven

The project's core design is a *positive feedback loop* (win → Domain Echo +1 faction stat → bigger pool → higher win-P → …). Lesson 5 flags it "doubly critical." Is it runaway or damped? Marginal dP(win)/d(stat) along the loop:

| stat (pool) | P(win) @ Ob 2 | marginal/pt |
|---|---|---|
| 1 (1D) | 10.1% | — |
| 2 (2D) | 25.9% | +15.8pp |
| 3 (3D) | 39.9% | +13.9pp |
| 4 (4D) | 51.3% | +11.5pp |
| 5 (5D) | 59.8% | +8.5pp |
| 6 (6D) | 66.8% | +7.0pp |
| 7 (7D) | 72.7% | +5.9pp |
| 8 (8D) | 77.1% | +4.4pp |

**The marginal gain shrinks monotonically (+15.8 → +4.4pp).** The loop is **self-damping by the dice S-curve itself** — each win raises the stat, but the next point's benefit shrinks, so wins cannot compound explosively. **The resolution engine's √N saturation IS the Lesson-5 damper for the intent_of_game loop.** This is the computed proof that the project's central positive-feedback loop is mathematically bounded at the resolution layer — independent of any system-specific cap. (System-specific terminal states — faction Stab-0 — are a *separate* unboundedness, on the loss side, addressed in ED-868; the *gain* side is self-damping, shown here.)

---

## §6 — All-directions synthesis (the six directions, each now computed)

| Direction | Pipeline | Computed result |
|---|---|---|
| **Bottom-up** (die mechanics) | P1 | Per-rung P(success); foreclosure scale-gated (≤1% at Territorial+ for 2D) |
| **Vertical** (stat→pool→outcome) | P1 + P4 | Fixed pool degrades 80%→0% up the ladder; marginal stat value saturates (+15.8→+4.4pp) |
| **Diagonal** (cross-system) | P3 | Domain Echo +15–25pp; Scene→Mass +11–19pp; rubber-banded |
| **Top-down** (intent_of_game loop) | P4 | Self-damping via S-curve; gain-side bounded at the engine |
| **Lateral** (peer parity) | P2 | Offense ≈ survival at low builds (73% vs 71.5%); breaks at high builds (72% vs 52%) |
| **Horizontal** (TTRPG↔videogame) | (prior) | Discrete↔continuous equivalent ≥5D w/ continuity correction (ED-873); below 5D the high-rung foreclosures of P1 are engine-shared |

**The cross-cutting story:** Valoria's engine behaves *cleanly in the middle of every axis* (healthy pools, mid rungs, low/typical builds, gain-side loops) and *strains at every axis's extreme* (small pools at high rungs → foreclosure; high builds → offense/survival parity breaks at the MW cap; loss-side terminal states). The strains are not random — they cluster at **(a) small-pool × high-scope** (faction/mass at Territorial+) and **(b) post-cap attribute economics** (Endurance ≥ 5). Both have known fixes (aggregate the pool; smooth the MW cap), and both are *calibration*, not paradigm.

---

## §7 — New findings & reconciliation

| # | Finding (computed this run) | Status vs prior |
|---|---|---|
| **I-1** | Cross-axis: offense ≈ survival at low builds; **MW cap (End 4) breaks parity at high builds** (Agi +23pp vs End +4pp post-cap) | **NEW — closes derived_stats `[GAP: sim-only]`.** Promotes D1 to a win-rate / build-economy finding. |
| **I-2** | Foreclosure is scale-gated: 2D forecloses (≤1%) from Territorial up; fine at Object/Personal | **NEW granular** — explains *why* faction (Territorial+) fails where personal combat (Personal) doesn't, beyond "bare pool." |
| **I-3** | ER-3 pool-size shock quantified per rung (5D: 80%→0% across ladder) | **Quantifies** the previously-qualitative ER-3. |
| **I-4** | Domain Echo propagation = +15–25pp; Scene→Mass = +11–19pp; rubber-banded | **NEW** — cross-scale currency weight measured; validates "personal play matters strategically." |
| **I-5** | intent_of_game loop is self-damping via S-curve saturation (gain-side bounded at engine) | **NEW** — computed proof of the "doubly critical" loop's gain-side bound; complements ED-868 (loss-side terminal). |

**Reconciliation:** every prior verdict holds; this run adds the *quantities* and closes the one gap explicitly marked sim-only. The headline (I-1) is the most consequential: it gives the **MW-cap smoothing decision (derived_stats D1 / option c) a concrete cost** — leaving it unfixed means high-build characters rationally cap Endurance at 4, distorting the attribute economy toward Agility.

---

## §8 — Self-critique on the combat sim & limits

The cross-axis result (I-1) rests on a **minimal** combat model — an independent reviewer would press:
- **Even off/def split assumed.** Real players optimize the split per round; an Agility-heavy fighter might press offense, changing the balance. The sim uses a fixed 50/50.
- **History 0, Power 2 fixed.** No weapon skill, no weapon variety, no Feint/Stamina/initiative/reach. These are the v32 combat-layer mechanisms; the sim tests *only* the Agi-pool vs End-Health axis in isolation. The full combat sims (`i17_simulation_prep`, `v32_bout_structural_sanity_sim`) are the authority on integrated combat; mine is a clean cross-axis *probe*, not a combat model.
- **Implication:** I-1's *direction* (Endurance leverage collapses post-MW-cap) is robust — it follows directly from the cap being at End 4 and is visible in raw Health (+71%/+48% steps → +8%). The *magnitude* (52% vs 72%) is sim-specific and should be confirmed against the full combat sim before the MW-smoothing decision is finalized. `[CONFIDENCE: high on direction, medium on magnitude.]`

`[CONFIDENCE: high]` — P1, P3, P4 (closed-form / large-MC dice, sanity-checked μ). `[CONFIDENCE: high-direction / medium-magnitude]` — P2 (model assumptions above).

**Ledger candidates (staged, not filed — consolidation handoff active):**
- I-1 → augment derived_stats D1 (ED candidate): MW-cap breaks high-build offense/survival parity; gives the smoothing decision a quantified cost. Recommend the continuous Health option (`(End+6)(End/2+1)`, no MW step) be re-evaluated against this.
- I-2/I-3 → augment ER-3 / ED-865: foreclosure is scale-gated; the faction fix (aggregate) is most urgent at Territorial+ rungs specifically.
- I-4/I-5 → informational (no defect): propagation weight healthy; loop gain-side self-damping. File as positive findings.

**Context status:** `[CTX: >75% | this turn: >75%]` — this session has run long (resolution diagnostic → engine reconciliation → armature → this intensification). The empirical gaps named across the session are now closed (cross-axis, propagation, loop gain, scale-ladder). Further intensification (full per-system × per-rung × per-direction matrices, or integrated multi-system sims) would be higher-quality in a fresh session with a clean context budget — flagging per token discipline rather than degrading the work here.
