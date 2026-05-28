---
name: valoria-resolution-diagnostic
description: >
  Three-stage NERS-compliance wrapper for any Valoria mechanical system: (1) runs the
  resolution-and-balance diagnostic (Phase 0–6) to locate where a system fails under
  stress, (2) tests each finding against the six scoped design lessons, and (3) produces
  a per-system NERS (Necessary / Robust / Smooth / Elegant) verdict with lesson-mapped
  remediation. A fourth validation stage re-tests proposed fixes against the same pipeline.
  ALWAYS use this skill when checking whether a system is NERS-compliant,
  diagnosing balancing or resolution problems, stress-testing small pools, checking for
  death spirals / runaway loops, threshold cliffs, or non-uniform modifiers. Trigger on:
  "is this NERS compliant", "diagnose this system", "stress test", "small pool problem",
  "resolution audit", "balance audit", "death spiral", "runaway loop", "cliff check",
  "does this scale", or when the orchestrator routes a resolution/balance diagnosis.
---

**Prerequisite:** Bootstrap complete — `assert_bootstrap()` via `quick_bootstrap()` before invoking. This skill reads canonical mechanics; never diagnose from memory or project-file copies. Fetch the target system's canonical design doc (via `references/canonical_sources.yaml` lookup) and `canon/02_canon_constraints.md` (P-01–P-15) this session before running.

**Model:** Opus (multi-system cross-referencing + quantitative reasoning).

**Relationship to `valoria-mechanic-audit`:** that skill checks *internal consistency* (formulas, gaps, redundancy). This skill checks *resolution and balance fitness under stress*, and ends in an explicit NERS verdict. Run consistency first if the system is unverified; run this when the question is "does it hold up at its extremes, and is it NERS-compliant."

---

## WHY THIS SKILL EXISTS

Valoria's resolution engine is a d10 success-counting pool; its probability response is an **S-curve**, and the marginal value of a die scales with `1/√N`. Consequently the engine does its **worst work at small pools** (faction bare 1–7D, depleted units, low-stat actors), where variance is high, a single die swings outcomes violently, and the continuous (Normal) approximation is inaccurate below ~5D. Balancing and resolution defects concentrate at these stress points. This skill finds them and maps each to its fix.

**The primary fix for small-pool defects is architectural** — one of the six lessons below. Parameter-level adjustments (fractional TN, continuous-engine μ/σ calibration, probit-axis modifier remapping) are valid complementary fixes but do not substitute for architectural corrections when the defect is structural.

---

## INPUT

The operator provides:
1. **Target system name** (e.g., "faction action layer," "personal combat," "mass battle").
2. **Scope** — full system or specific sub-component (e.g., "the CI accounting pipeline only").
3. The canonical design doc path is resolved via `references/canonical_sources.yaml`; the operator need not know it.

The skill fetches the canonical doc, `canon/02_canon_constraints.md`, and any cross-referenced system docs needed for Phase 4 (cross-system loops).

---

## THE THREE MECHANIC CATEGORIES (read first — load-bearing)

Every Valoria quantity is one of three kinds. The lessons apply differently to each; conflating them produces false findings.

| Category | Examples | Behaviour rule | Governed by |
|---|---|---|---|
| **Continuous resource** | pools, Health, TroopCount, Composure, Stamina, Coherence (10→0, variable-cost depletion) | Degrade **smoothly**; uniform-impact steps; no accidental cliffs. | Lessons 2, 6 |
| **Discrete accumulator** | clocks/trackers — Evidence (3/5/8), Persuasion (0–10), CI (0–100), Morale thresholds, MS (0–100) | **Legitimately 100% linear and stepped.** Equal increments are correct; multiple thresholds are intended and legible. | Lesson 4; **exempt** from Lessons 2 and 6 |
| **Base parameter** | integer stats (1–7) — Military, Charisma, Stability, Cognition, Attunement, etc. | Feed pools and derived values. Change by ±1 at accounting or structural events. Source of the small-pool problem when used as bare pools. | Lesson 2 applies (±1 impact is non-uniform at different stat levels); Lesson 3 applies (don't roll them bare at high stakes) |

Classify every quantity before judging it. A linear clock is not a Lesson-2 violation; a multi-threshold tracker is not a Lesson-6 violation; a base parameter is not a pool.

---

## STAGE 1 — THE DIAGNOSTIC (Phase 0–6)

Run in order. Phase 0 routes which later phases apply.

### Phase 0 — Decompose into resolution components
Do **not** classify the system as a single type. Instead, identify which **components** are:
- **Dice-resolved** (a pool is rolled for an outcome)
- **Deterministic-accounting** (values computed from formulas/ledgers, no roll)
- **Clock-driven** (an accumulator advances by increments toward thresholds)

Most Valoria systems are composites: social contest is dice (exchange rolls) + clock (Persuasion Track); mass battle is dice (engagements) + deterministic (TroopCount output scaling) + clock (Morale thresholds). Tag each component; run the applicable phases on each.

### Phase 1 — Locate the stress point (not just the floor)
- **1a.** For dice components: smallest pool **by design** (stat range) AND smallest pool **after degradation** (penalties dragging a healthy pool down). Two distinct sources. For deterministic components: the steepest point on the response curve or the most extreme input combination. For clocks: the shallowest clock (fewest segments to threshold).
- **1b. Exposure frequency:** how often is the stress point actually reached, and under what conditions? Estimation methods (use one or more):
  - **Condition enumeration:** list the specific game states that produce the floor (e.g., "Military 1–2 faction under occupation with −1 penalty"). How many factions / actors / scenarios reach this?
  - **Degradation path count:** how many penalty sources stack toward the floor (wounds + fatigue + environment + …)? More paths = higher exposure.
  - **Canon frequency signals:** does the design doc flag the stress case as "rare," "edge," or "routine"? (e.g., faction collapse is designed as rare; low-stat starting factions are routine.)

### Phase 2 — Characterize what the stress point decides
- **2a. Outcome type:** binary verdict / **graded magnitude** / clock increment. For clocks, record **depth** (segments to threshold) — a shallow clock (one roll ≈ one segment) is a disguised binary. Graded-magnitude outcomes at a small pool are *also* dangerous (magnitude swings violently).
- **2b. Stakes & reversibility:** low / recoverable / irreversible-load-bearing.
- **2c. Preliminary risk profile** (qualitative composite — not arithmetic):

  | Dimension | Low | Medium | High |
  |---|---|---|---|
  | Impact | magnitude swing small; outcome non-critical | swing moderate; outcome affects one track | swing large; outcome flips state or is load-bearing |
  | Exposure | stress point reached only in extreme/rare states | reached in a minority of play scenarios | reached routinely or by design |
  | Irreversibility | outcome retryable or Fail-Forward | recoverable within 1–2 seasons | permanent or structurally compounding |

  Rank as (H/M/L, H/M/L, H/M/L). Any dimension at H is a flag; two or more H dimensions is a candidate finding. Carry forward.

### Phase 3 — Check the effect curves
- **3a. Impact uniformity (dice-resolved and base-parameter components only):** is a fixed modifier's **impact** uniform across scale? The goal is uniform *impact*, not the *form* "proportional" — proportional-in-dice is still non-uniform-in-probability via √N. *(Does not apply to deterministic-accounting or clock components.)*
- **3b. Threshold cliffs (all components):** does a continuous input cross a discrete boundary that jumps the outcome? Do multiple unrelated cliffs **stack** at one point (e.g., Size = Command firing pool-drop + morale + discipline together)? *Intended, spaced clock thresholds are not cliffs in this sense.*
- **3c. Role conflation (all components):** does one variable carry more than one independent role (capacity AND cohesion AND collapse)?

### Phase 4 — Check the loops (highest severity; all components)
- **4a.** Identify feedback loops, **including cross-system / cross-scale couplings** (e.g., combat death → faction Stability → muster → combat). Per-system reading alone is blind to these — list inter-system edges explicitly. Fetch cross-referenced system docs if needed.
- **4b.** For each loop: **damper present?** (gain < 1 per iteration of the loop's natural cycle — where "cycle" = one complete traversal of the loop's causal chain, e.g., one season for an accounting loop, one battle turn for a combat loop, one exchange for a social loop) and **cap present?** (hard bound on the variable being amplified) — two separate checks. The defect is a loop that is **both undamped and unbounded.**

### Phase 5 — Intent gate (applied to every candidate finding)
For each candidate finding: is the discontinuity / asymmetry / absolute-effect / loop **serving a deliberate design purpose**?

Evidence of intent (require at least one):
- Explicit design-doc statement naming the effect and its purpose (e.g., "encirclement removes the −3 cap — models Cannae").
- The effect has a paired safeguard explicitly designed for it (e.g., the −3 cap itself is the safeguard for morale loss).
- Designer confirmation (Jordan) in conversation or editorial annotation.

If intent is underdetermined (no evidence in either direction): flag as `[INTENT UNDETERMINED]` and carry forward as a candidate finding with a note. Do not guess intent.

Safeguard adequacy: a safeguard is adequate if it bounds the loop/cliff to a recoverable state within the system's natural recovery timescale (e.g., a cap that prevents rout in one turn is adequate if Morale can recover in Reform phase).

- Deliberate **with** adequate safeguard → pass.
- Deliberate **without** adequate safeguard → true finding (the intent is good but the execution is unsafe).
- Accidental or intent-undetermined → true finding.

### Phase 6 — Score & triage
Per system, output a risk profile using the same three dimensions as Phase 2c (impact / exposure / irreversibility), ranked worst-first. Carry each true finding forward to Stage 2.

**Stage 1 output:** `resolution_diagnostic_<system>.md`
```
| Finding | Component | Stress point | Outcome@floor | Impact | Exposure | Irreversibility | Intent | Phase | Severity |
```

---

## STAGE 2 — TEST FINDINGS AGAINST THE SIX LESSONS

Each true finding from Stage 1 maps to **one or more** corrective lessons. Multi-defect systems will have findings across phases, each mapping to its lesson; a compound defect (e.g., small-pool + non-uniform + unlooped) legitimately requires several lessons acting together. The lessons are **scoped conditions, not universals** — apply only within the stated scope.

| # | Lesson (scoped) | Scope | Fixes finding type |
|---|---|---|---|
| **1** | **One variable, one role.** Split a variable only where it genuinely carries two independent jobs. *(Apply minimally — over-splitting harms Elegance.)* | All components | Phase 3c role conflation |
| **2** | **Continuous resources and base parameters take uniform-*impact* steps.** Effects on a resolution pool, capacity, or stat should have scale-invariant impact. **Exempt:** accumulators (linear is correct) and deliberate, legible absolute effects. | Continuous resources; base parameters | Phase 3a non-uniform impact |
| **3** | **Dice only on healthy pools, for graded/recoverable outcomes.** Keep dice off small-pool, load-bearing, binary decisions. *(Master lesson.)* | Dice components; base parameters used as bare pools | Phase 1+2 small-pool load-bearing roll |
| **4** | **Route unavoidable small rolls through a clock deep enough to average.** A shallow clock (one roll ≈ one segment) is a disguised binary and does not count. | Dice → clock routing | Phase 2 binary@small-pool that must remain a roll |
| **5** | **No loop — including cross-system — both undamped and unbounded.** One safeguard, sized to the loop's gain per cycle. *(Doubly critical: `intent_of_game` is itself a positive feedback loop.)* | Any component with feedback | Phase 4 undamped+unbounded loop |
| **6** | **Continuous quantities degrade continuously; never stack accidental cliffs at one point.** Intended, spaced thresholds — especially clock thresholds — are exempt and may be multiple. | Continuous resources | Phase 3b stacked/accidental cliffs |

**Mapping rule:** if a finding maps to no lesson, either it is not a real resolution/balance defect (recheck Phase 5 intent) or a seventh lesson is needed — surface that explicitly rather than forcing a fit. If a finding maps to multiple lessons, list all that apply; compound remediation is expected for multi-defect systems.

**Stage 2 output:** append lesson mapping to each finding row:
```
| Finding | ... | Lesson(s) | Remediation |
```

---

## STAGE 3 — NERS VERDICT

Convert the lesson-tested findings into the canonical NERS criteria (`canon/definitions.yaml`). A system is **NERS-compliant** only when it passes all four. State the verdict per criterion with the specific defect, severity, and the lesson whose application closes it.

| Criterion | Pass test (resolution/balance lens) |
|---|---|
| **Necessary (N)** | No variable or roll is redundant; nothing here could be removed without worsening play. Watch the inverse: a Lesson-1/Lesson-5 fix that *adds* apparatus must itself be necessary — do not over-engineer. |
| **Robust (R)** | Holds at its extremes: small-pool floor produces no fragile binary; modifiers are uniform-impact; no unstated exceptions; loops bounded. "Fully formed, error-free, complete." |
| **Smooth (S)** | Degrades and transitions cleanly across scales; calculations consistent with sibling systems; no friction at category boundaries (continuous vs accumulator vs base parameter handled correctly). |
| **Elegant (E)** | The system as-is is logically simple with no unnecessary overhead; player can intuit outcomes. If remediations are proposed, they must preserve or improve elegance — a fix that bolts on structure the system does not need fails E. |

**Verdict format** (review discipline: verdict first, severity-ranked, no false balance):
```
SYSTEM: <name>   COMPONENTS: <dice | deterministic | clock> per Phase 0
VERDICT: NERS-compliant | non-compliant — <one-line reason>

N: pass/fail — <defect, severity, lesson>
R: pass/fail — <defect, severity, lesson>
S: pass/fail — <defect, severity, lesson>
E: pass/fail — <defect, severity, lesson>

REMEDIATION (worst-first):
  <severity> <finding> → Lesson <n>: <concrete fix>
```
**Output:** `ners_verdict_<system>.md`. P1/P2/P3 findings that are canonical gaps append to `canon/editorial_ledger.yaml` (subject to commit gate; if blocked, stage inline and flag `[DRIFT]`).

---

## STAGE 4 — RE-TEST PROPOSED FIXES

After Stage 3 produces remediations, run the diagnostic (Stage 1 Phases 1–6) on the **proposed fix** — not the original system — to verify the fix does not introduce new defects.

Common re-test failures:
- Lesson 1 fix (split variable) → creates a redundant variable (fails N) or over-engineers (fails E).
- Lesson 3 fix (remove roll, route to accounting) → one accounting variable now carries two roles (fails Lesson 1 / Phase 3c).
- Lesson 5 fix (add damper/cap) → the damper itself creates a new threshold cliff (fails Lesson 6 / Phase 3b).

If the re-test surfaces new findings: revise the remediation and re-test again. Iterate until clean or flag the remaining tension as an `[OPEN TRADE-OFF]` requiring a design decision.

**Stage 4 output:** append to `ners_verdict_<system>.md`:
```
RE-TEST: <pass | new findings>
  <any new findings and revised remediation>
```

---

## GUARDRAILS

- **Never defend prior output.** If diagnosing a system you (or a prior session) designed, prepend `[SELF-AUTHORED — bias risk]` and actively surface the criticism an independent reviewer would raise. Treat all work as external.
- **No false universals.** Every lesson is scoped. A linear clock, a multi-threshold tracker, and a deliberate absolute effect are NOT violations — check the category (three-category table) and Phase 5 intent before flagging.
- **Over-engineering is a defect.** Lessons 1 and 5 add structure; apply only where the failure they prevent is actually present and live (Phase 1b exposure). An added variable or safeguard that isn't necessary fails NERS-N and NERS-E.
- **Goal over form.** Target uniform *impact*, bounded *loops*, smooth *approach* — not the surface form ("proportional", "one cliff"). Proportional-in-dice ≠ uniform-in-probability.
- **Small pools are primarily architectural.** Route through Lessons 3/4 (don't roll it, or clock it) or aggregate the pool. Parameter-level adjustments (fractional TN, μ/σ calibration, probit remapping) are valid complements, not substitutes.
- **Ground every claim.** Loops, intent, frequency — cite the canonical mechanism or flag `[UNGROUNDED]`. Do not assert from memory.
- **RuntimeError from any hook = hard halt.** Report verbatim, stop.

---

## WORKED EXAMPLE — Faction Action Layer

*(Abbreviated; a real run produces the full output tables.)*

- **Phase 0 (decompose):** two components — (A) deterministic accounting (CI economy, Treasury/Legitimacy ledgers), (B) dice-resolved discrete actions (Assert, Suppress, Parliamentary Vote using bare faction stat 1–7D as pool).
- **Phase 1:** Component B floor = 1–2D (low-stat faction under occupation with penalty). Exposure: routine — weak/occupied factions are a standard game state, not an edge case. Component A: steepest response at CI near seizure thresholds (60, 100).
- **Phase 2:** Component B: a bare 2D roll delivers a **binary verdict** on pivotal outcomes (seizure, vote). Stakes: irreversible-load-bearing. Risk profile: (H, H, H) — three-high, candidate finding.
- **Phase 3a:** Component B: stat damage is absolute (−1 Military). Impact at Military 2: −31% relative P(success); at Military 6: −9%. Non-uniform. **3b:** Stability-0 collapse is a single cliff (check if others stack at the same point). **3c:** Stability carries both "political health" and "collapse trigger" — role conflation candidate.
- **Phase 4:** Cross-system loop identified: faction collapse → territory loss → reduced muster → weaker military → further collapse. Canonical mechanism: `faction_layer_v30 §1.5 Faction Collapse Exit Procedure` + `military_layer_v30 §1.5 Muster Prerequisites` (Military stat gates muster quality). Damper: Stability recovery exists (§1.3, +1 per season under conditions). Cap: Stability floor = 0 (collapse), which is a termination, not a bound. **Loop is damped (slow recovery) but the terminal state is irreversible collapse — no cap short of extinction.** True finding.
- **Phase 5:** The bare-stat roll for faction actions: `[INTENT UNDETERMINED]` — no design doc states "faction actions intentionally roll bare stats at high stakes." The TTRPG-era design predates the videogame-only pivot; inherited without explicit re-evaluation. True finding.
- **Stage 2 mapping:** Finding 1 (small-pool binary on pivotal outcome) → **Lesson 3** (route consequence through deterministic accounting; aggregate pool when roll is needed) + **Lesson 4** (clock the action instead of pass/fail). Finding 2 (non-uniform stat damage) → **Lesson 2** (uniform-impact). Finding 3 (role conflation) → **Lesson 1** (split if genuine dual role confirmed). Finding 4 (undamped terminal loop) → **Lesson 5** (add a bound short of extinction, or a recovery path from collapse).
- **Stage 3 verdict:** **Non-compliant.** Fails R (fragile small-pool binary on pivotal, irreversible outcomes), S (dice resolution inconsistent with the deterministic layer it sits on), and E (the bare-stat roll adds complexity without strategic depth — a roll the player cannot meaningfully influence).

---

## INITIAL HYPOTHESES (untested — validate by running the pipeline)

These are starting assessments based on session analysis, **not** pipeline-confirmed results. Each must be validated by a full Stage 1–4 run before being treated as a verdict.

- **Investigation / fieldwork** — likely compliant: deterministic five-filter chain owns decisions; dice only feed the Evidence clock.
- **Social contest** — likely compliant, healthy contested case: fully layered, pools 5–18D.
- **Mass battle** — likely compliant, well-bounded spiral: small pools exist but the state machine carries the weight; loops appear damped.
- **Faction action layer** — likely **non-compliant**, priority target (worked example above).
- **Personal combat** — likely mostly compliant; watch the flat −1D wound at the 5D floor (Lesson 2 candidate).
- **Peninsula / victory** — likely compliant: deterministic clocks, no dice.
- **Threadwork** — likely compliant for operations; Coherence is a **depleting resource** (continuous, variable-cost) — validate that its depletion and threshold effects satisfy Lessons 2 and 6.
