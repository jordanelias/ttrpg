# Social Contest — Robust Testing Matrix v1 (factor-isolation / sensitivity design)

**Date:** 2026-06-23 · **Purpose:** isolate the marginal contribution of *every* factor that flows through the social-contest system — venue, adjudicator, faction allegiance, character attribute/stat/derived score, and all dice/resolution/propagation variables — so each contributor's performance can be measured independently and in interaction.
**Harness:** `tests/sim/social_contest_matrix_harness.py` (operationalizes this matrix). **Method:** design-of-experiments — baseline + one-factor-at-a-time (OFAT) main effects + per-unit marginal curves + curated factorial interaction cells, with common-random-number (CRN) variance reduction.

---

## 0. Method

1. **Baseline (the control).** A fully matched configuration — same faculty, same policy, neutral adjudicator, symmetric venue. A correct system must return **~50/50** here; any skew is a bug (symmetry is test #1, not an assumption).
2. **OFAT main effects.** Vary **one** factor across its levels, hold everything else at baseline. The change in the response metric vs baseline is that factor's **isolated main effect**.
3. **Per-unit marginal curves.** For ordinal factors (faculty 1–7, standing, evidence count, panel size, pressure, resistance), sweep the whole range to get the **performance-per-unit** curve (e.g. Δwin-rate per +1 attribute point — the "+10%/pt" claim; Δ per +1D-equivalent — the CR6 uniform-impact claim).
4. **Factorial interaction cells.** Cross the factor pairs where the system is expected to *ripple* (venue×adjudicator, faculty-gap×win-condition, allegiance×venue-boost, standing×split, evidence×proof-weight, pressure×discipline). Interaction = main-effect-A under level-B differs from under baseline-B.
5. **CRN.** Reseed `random.seed(base + replicate_index)` each replicate so the *same* replicate index draws the *same* stream across factor levels — paired comparison, large variance reduction. N = 1500–2500 per cell (400 in `--quick`).

---

## 1. Engine map — which model can isolate which factor

| Layer | Model | Factors it can isolate | Status |
|---|---|---|---|
| **A — resolution architecture** | groundup engine (`designs/audit/2026-06-03-contest-groundup/`, 36/36 tests) | venue, adjudicator/panel, faculty (primary attribute), standing, evidence (relevance/corroboration), policy/appeal (style), institutional & public pressure, win-condition, defeat-catalogue (faults), genre/tense weighting, faction-layer votes/succession/coalition | **runnable now** |
| **B-skeleton** | reduced sim (`sim/personal/contest.py`) | primary attribute, History, audience resistance, exchange count, starting track, wounds, Contest-Fatigue gating → win / decisive / total-victory rates | **runnable now** (pool→track→win only; see banner) |
| **B-full** | canonical reference impl — `tests/sim/social_contest_reference.py` (clean-room) | the derived-resource economy (Composure/Concentration/Rattled/Spent/strain), the canonical bonus-dice stack (genre +1D / orientation +1D / Recall +2D / Findings / Resonant +1D / Momentum), interaction types CLASH/REINFORCE/CROSS/TIE, resistance erosion, Doubt Marker, **+ ripple flags** (Obligation/Domain Echo/MS/Scar/Fatigue) | **runnable** (reference model of the *patched* canonical rules; distinct from the groundup σ-engine — treat as canonical-rule sensitivities, not shipping balance) |
| **Ripple** | faction/thread/NPC layers | Obligation generation, Domain Echo, MS co-movement, Conviction-Scar production, NPC-priority-tree constraint | **metrics spec'd; require B-full + cross-layer hooks** |

> The matrix is engine-agnostic by design. All three layers now run: Layer A on the groundup engine, B-skeleton on the reduced sim, and **B-full on `social_contest_reference.py`** — a clean-room reference of the *patched* canonical rules (success-count d10, TN 7), separate from the groundup σ-engine. Read B-full numbers as canonical-rule sensitivities (and as a differential check against the groundup engine), not as shipping balance.

---

## 2. Factor inventory (factors × levels × baseline)

**Character (the contributor whose "performance per point" we most want):**

| Factor | Levels | Baseline | Engine | Canon mapping |
|---|---|---|---|---|
| Primary attribute (faculty) | 1,2,3,4,5,6,7 | 4 | A, B-skel | Cognition/Charisma/Attunement by adjudicator type (§3); Argue pool = (Primary×2)+History+3 |
| History bonus | 0,3,6,9 | +3 | B-skel | pool depth |
| Standing | 0,2,5,7,9 | 5 (mid) | A | ascribed rank / institutional weight |
| Charisma (→ Composure, Cha-mod) | 1..7 | 4 | B-full | Composure = Cha×3; strain Cha-mod = max(0,⌊(Cha−3)/2⌋)×3 |
| Focus + Spirit (→ Concentration, Foc-def) | Foc 1..7 × Spi 1..7 | 4 / 3 | B-full | Concentration = (3×Focus)+(2×Spirit); Foc-def = ⌊Foc/2⌋×3 |
| Recall (→ Appraise pool, citation) | 1..7 | 3 | B-full | Appraise = Att+Recall; +2D citation |

**Venue / adjudicator / allegiance:**

| Factor | Levels | Baseline | Engine |
|---|---|---|---|
| Venue | disputation, court, assembly, appeal, + cross-cultural (public_oration, inquisition_hearing, excommunication_court, imperial_petition, secret_council, memorial_remonstrance) + institutional (fused_arbiter, deliberative_body, scholastic_disputation); canon: Formal/Grand/Royal Audience/Tribunal/Guild/Casual/Negotiation/Appeal/BG-Vote/Hybrid | disputation | A |
| Win-condition | ThresholdRace, TallyAtClose, ProofBar (defender-favoured), GraceThreshold, VoteAtClose, **PersuasionTrack** (canon committee/decisive/total bands) | ThresholdRace(5) | A |
| Adjudicator character | NEUTRAL, logos-judge, pathos-judge (crowd), ethos-judge, low-tension | NEUTRAL | A |
| Adjudicator structure | single, Panel(3), Panel(5), Panel(7) | single | A |
| Allegiance / boost axis (proof weights) | ethos-dominant, pathos-dominant, logos-dominant, balanced — = the faction boost (Church Obscuring/Faith; Crown Revealing/Virtue; Varfell Projection; Hafenmark Memory; Restoration Revealing; …) | balanced | A |
| Orator style / policy | logos, pathos, ethos, build-then-close, exploiter, overreacher, staller | logos | A |
| Institutional pressure | 0, .25, .5 toward A | 0 | A |
| Public pressure (crowd unlock) | 0, .35, .7 | 0 | A |
| Genre/tense register | past-weighted, neutral, future-weighted × start-ground FACT/QUALITY/CONSEQUENCE | neutral / QUALITY | A |
| Defeat catalogue | full faults, no device-bar, no-evasion, none | full | A |
| Evidence (Recall/Findings) | 0,1,2,3 relevant items; irrelevant-only | 0 | A |

**Resolution / track variables (B-full unless noted):**

| Factor | Levels | Baseline | Engine |
|---|---|---|---|
| Audience resistance | 0,1,2 | 1 | B-skel, B-full |
| Resistance erosion (ED-864) | on / off | on | B-full |
| Exchange count | 1,3,5 | 3 | B-skel |
| Starting track | 3,5,7 (and Tribunal-7) | 5 | B-skel |
| Interaction type | CLASH, REINFORCE, CROSS, TIE | CLASH | B-full |
| Bonus-dice source | genre +1D, orientation +1D, Recall +2D, Findings +1/+2D, Resonant +1D, Momentum | none | B-full |
| Rattled level | 0,1,2 (→ −1D/level) | 0 | B-full |
| Spent | off / on (−2D, opp +1D) | off | B-full |
| Corroboration | none, Knot Ob1, non-Knot Ob2 | none | B-full |
| First-to-speak | rolled (ED-581) | rolled | B-skel |
| Coalition size (shared Concentration) | solo, 2, 3 | solo | B-full |
| Temporal-axis conflict (PP-351) | none / fires (±1 Track) | none | B-full |
| Practitioner weaving | TS 0/30/60/90 (+⌊TS/30⌋D) | 0 | B-full |

**Faction-layer (BG):** coalition mandate split (pro-sum vs anti-sum), abstainers (resistance), lobby offset (0/±1/±2); succession faculty gap; censure proposer strength.

---

## 3. Response metrics

**Outcome (primary):** p(A win), p(B win), p(draw); for PersuasionTrack: p(committee), p(decisive), p(total). Derived: **A-advantage = pA − pB** (the paired effect-size axis); **symmetry deviation |pA−pB|** at matched config.
**Process:** mean accumulated advantage `adv[A]`; mean margin; **clinch/fault rate** (by fault type); exchanges-to-resolution; **Spent frequency**, **Rattled frequency**, mean strain dealt/taken (B-full); turning-point distribution, decisive-appeal mix (narrative layer).
**Ripple / propagation (B-full + cross-layer):** P(Decisive→Obligation); P(Memory-win→Mandate +1) & P(Projection-win→Domain-Action +1D); P(genre-win→MS +1); P(Resonant-win→Conviction Scar); count of NPC-priority-tree actions blocked by a live Obligation. These quantify how far, and how often, a contest outcome *ripples* outward.

---

## 4. The matrix (blocks)

- **Block 0 — Symmetry/baseline (control).** Matched fa=fb, pa=pb, NEUTRAL adj, balanced venue, each win-condition. **Pass = |pA−pB| < 0.06.** Run this for every win-condition; a fail here invalidates that venue's downstream cells.
- **Block 1 — OFAT main effects.** One table per factor in §2; each row = a level, columns = the §3 outcome metrics + Δ(A-adv) vs baseline. Isolates each contributor's standalone pull.
- **Block 2 — Per-unit marginal curves.** Faculty 1–7 (vs fb=4) → win-rate curve + Δ/point (monotone? diminishing?); standing 0–9; evidence 0–3 (+corroboration diminishing); panel 1–7 (variance/aggregation); pressure 0–.7; resistance 0–2. Each curve is one contributor's transfer function.
- **Block 3 — Interaction cells (curated 2-way).** venue×adjudicator (does a pathos judge flip a logos venue?); faculty-gap×win-condition (does ProofBar damp skill gaps more than ThresholdRace?); allegiance×venue-boost (boost-match advantage); standing×split-flag (fused lends force / split does not); evidence×proof-weight; public-pressure×adjudicator-discipline (crowd unlock). Interaction present ⇔ effect-A differs across B-levels.
- **Block 4 — Faction layer (BG).** coalition pro/anti/abstain/lobby → pass/fail/committee bands; succession matched(split)/lopsided(unified) + §7.2.1 ratios; censure proposer-strength.
- **Block 5 — Ripple/propagation (B-full, deferred).** For each outcome class, the §3 ripple metrics. Tables ready; executor pending.

---

## 5. Controls, rigor, and acceptance diagnostics

- **CRN seeding** (paired across factor levels), **N ≥ 1500** per cell, fixed master seed for reproducibility.
- **Symmetric baseline gate** (Block 0) before trusting any asymmetric cell.
- **Diagnostics tied to the project's NERS criteria:**
  - **Robust:** no accidental cliff — marginal curves (Block 2) should be smooth/monotone except at *intended* bands (win/compromise thresholds, Tribunal-7).
  - **Smooth / uniform-impact (CR6 F1):** a +1D-equivalent bonus should shift win-rate by an approximately **constant** Δ across pool sizes 5D→18D. A bonus whose Δ collapses as the pool grows reproduces the flat-dice non-uniformity the redesign targets. (Run the bonus-source sweep at faculty 2,4,6.)
  - **ProofBar defender-favour:** matched play under ProofBar should give the defender > ~0.6 (burden of proof).
  - **Adjudicator dominance:** a strongly-charactered single judge should be *softened* by a panel (monotone in panel size).
  - **Spent reachability (post ED-890/DEP):** under the patched (3×Focus)+(2×Spirit), −5/−5, Spent should fire within 3–5 exchanges for average Focus/Spirit, and *not* be inert at high stats. (B-skel/B-full.)

---

## 6. How to run

```
python tests/sim/social_contest_matrix_harness.py            # full (groundup Layers A) + reduced-sim (B-skeleton)
python tests/sim/social_contest_matrix_harness.py --quick     # N=400 smoke
python tests/sim/social_contest_matrix_harness.py --block 2   # one block (0|1|2|3|4|bfull|sim)
python tests/sim/social_contest_matrix_harness.py --block bfull # derived economy + interaction types + ripple
python tests/sim/social_contest_reference.py                  # reference-engine self-check
python tests/sim/social_contest_matrix_harness.py --n 4000    # tighten CIs
```
Output: per-block tables of outcome distributions and Δ(A-adv) effect sizes, plus the Block-0 symmetry gate and the Block-2 diagnostic flags.

---

## 7. Coverage matrix (every contributor accounted for)

| Contributor | Isolated in | Engine | Status |
|---|---|---|---|
| Venue / proceeding type | Block 1, 3 | A | ✅ |
| Win-condition (incl. PersuasionTrack bands) | Block 0, 1, 3 | A | ✅ |
| Adjudicator character & structure (panel) | Block 1, 2, 3 | A | ✅ |
| Faction allegiance / boost axis | Block 1, 3 | A | ✅ |
| Primary attribute (faculty) | Block 2 | A, B-skel | ✅ |
| History / pool depth | Block 1 | B-skel | ✅ |
| Standing (+ split flag) | Block 2, 3 | A | ✅ |
| Evidence / Recall / Findings | Block 1, 2, 3 | A | ✅ |
| Orator style / policy | Block 1 | A | ✅ |
| Institutional & public pressure | Block 1, 2, 3 | A | ✅ |
| Genre / tense register | Block 1, 3 | A | ✅ |
| Defeat catalogue (faults) | Block 1 | A | ✅ |
| Resistance (+ erosion) | Block 2 | B-skel / B-full | ◑ (erosion = B-full) |
| Exchange count / starting track | Block 1 | B-skel | ✅ |
| Composure / Concentration / Rattled / Spent / strain | Block bfull; diagnostics §5 | B-full ref | ✅ (reference) |
| Bonus-dice stack (genre/orient/Recall/Findings/Resonant/Momentum) + uniform-impact | Block bfull (CR6 diag) | B-full ref | ✅ (reference) |
| Interaction type (CLASH/REINFORCE/CROSS/TIE) | Block bfull | B-full ref | ✅ (reference) |
| Coalition / shared Concentration | Block 1, 4 | A (votes) / B-full ref (Concentration) | ✅ |
| Ripple: Obligation / Domain Echo / MS / Scar / Fatigue | Block bfull | B-full ref (flags) → cross-layer | ✅ (reference flags) |
| Faction-layer votes / succession / censure | Block 4 | A | ✅ |

✅ runnable now · ◑ partial · ◻ spec'd. With `social_contest_reference.py` added, every contributor is now exercisable — Layer A on the groundup engine, B-skeleton on the reduced sim, B-full on the canonical reference. The remaining cross-layer step is wiring the ripple flags into the live faction/thread/NPC ledgers (currently emitted as per-contest flags).
