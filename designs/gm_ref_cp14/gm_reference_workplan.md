<!-- DERIVED FROM: Checkpoint 14 (compilation/valoria_ruleset_checkpoint_14.md, 2026-03-26) -->
<!-- SESSION: 2026-03-30 / 2026-03-31 — see session_log_archive.md -->
<!-- STATUS: Pre-release reference tool. Not valid against any post-CP14 ruleset. -->

# VALORIA — GM REFERENCE SUITE WORKPLAN

*Goal: Produce a complete GM reference suite that offsets ~80–90% of tracking/accounting burden and ~70–75% of co-movement narration burden. Based on analysis in `valoria_emergent_narrative_analysis.md` and preceding design conversation.*

*Model assignments: Claude = mechanical/structural work. Opus = narrative/philosophical content requiring philosophical judgment.*

---

## DELIVERABLE MAP

| # | Deliverable | Pages | Model | Phase |
|---|-------------|-------|-------|-------|
| D-01 | Cascade Consequence Reference | 1 | Claude | 1 |
| D-02 | Seasonal Accounting Form | 1 | Claude | 1 |
| D-03 | GM Dashboard | 1 | Claude | 1 |
| D-04 | Gap Escalation Table | 0.5 | Claude | 1 |
| D-05 | Coherence Band Track Reference | 0.5 | Claude | 1 |
| D-06 | Thread Operation Resolution Card | 1 | Claude | 1 |
| D-07 | NPC State Card Templates | 1 | Claude | 1 |
| D-08 | Knot Registry Template | 0.5 | Claude | 1 |
| D-09 | Co-movement Matrix Skeleton | 2 | Claude | 1 |
| D-10 | Framing Process — Structural Frame | 0.5 | Claude | 1 |
| D-11 | Co-movement Matrix — Narrative Cells | 2 | Opus | 2 |
| D-12 | Framing Process — Philosophical Content | 0.5 | Opus | 2 |
| D-13 | Annotated Examples (8–12, split-register) | 4–6 | Opus | 2 |
| D-14 | Counter-examples (4–6) | 2–3 | Opus | 2 |
| D-15 | Assembled GM Reference Suite | ~16 | Claude | 3 |

**Total estimated pages: ~16 formatted reference pages across all deliverables.**

---

## PHASE 1 — MECHANICAL INFRASTRUCTURE (Claude)

All tasks in this phase are purely mechanical: table construction, procedure codification, structural skeleton-building from compiled ruleset. No narrative content. No editorial decisions. Executable without user approval.

Source documents required (all in canon/ or compilation/ or designs/):
- `compilation/valoria_ruleset_checkpoint_14.md` — canonical values
- `designs/valoria_emergent_scenarios.md` — scenario chains and clock values
- `designs/valoria_narrative_scenario_chains.md` — NPC stat blocks

---

### TASK 1.1 — Cascade Consequence Reference (D-01)

**What:** Single-page table. All active clock cross-effects by threshold. GM keeps on screen every session.

**Content:**
- RS thresholds (55, 40, 20, 1) → active cross-clock effects
- TC thresholds (40, 60, 80) → active cross-clock effects  
- IP thresholds (30, 45, 60, 75, 100) → triggers
- All spontaneous Gap probabilities by RS band
- Faction Stability check triggers by RS band
- Session cap reminders (RS ±10/season net)

**Source:** Scenario 8 (clock interactions), Scenario 9 (terminal decline), compiled Stage 6 (factions).

**Output:** `gm_ref/d01_cascade_consequence_reference.md`

---

### TASK 1.2 — Seasonal Accounting Form (D-02)

**What:** Step-by-step offline processing worksheet. GM fills out between sessions. Arrives at table with resolved state.

**Content:** Fixed-order checklist:
1. RS passive drift (−1 Winter; active Gap drain −4/Gap; Lock chronic drift −1 to −2/Lock)
2. RS threshold cross-effects (check if any threshold crossed this accounting)
3. TC adjustments (RS cross-clock; Church Domain Action effects; seasonal TC generation)
4. IP adjustments (RS/TC cross-clocks; event-driven changes)
5. Faction Stability checks (if RS ≤ 19: Ob 1; resolve Mandate drops and Fracture triggers)
6. Knot strain increments (by Coherence band of each practitioner)
7. Coherence recovery (full season non-practice = +1; Anchoring Scenes this season)
8. NPC clock advances (Torben Loyalty if covert contact failed; Vaynard TK if Private Collection used; Klapp CE if handling Locks; Ehrenwall Counter if trigger conditions met)
9. Domain Action resolutions (any pending seasonal effects)
10. State record (write new values to GM Dashboard)

**Output:** `gm_ref/d02_seasonal_accounting_form.md`

---

### TASK 1.3 — GM Dashboard (D-03)

**What:** Single-page live-state reference. All variables the GM needs during play. Updated after each Seasonal Accounting.

**Content:**
- World clocks: RS / TC / IP (current value + active threshold band)
- Faction attribute grid: all 7 factions × Mandate/Stability/Military/Wealth/Influence/Intel (or faction-specific equivalents)
- NPC clock positions: Torben Loyalty (0–8) / Vaynard TK (0–5) / Klapp CE (0–5) / Ehrenwall Counter (0–3) / Almud TS proximity
- Active threshold effects: checkboxes for each currently-active cross-clock effect
- Active Gaps: territory + severity + seasons open
- Active Locks: territory + TS of locked config + chronic drift registered
- PC Coherence positions: per-practitioner band (Stable/Dissonant/Fragmented/Fractured/Severed)
- PC Knot strain: per-practitioner active Knot count + strain level

**Output:** `gm_ref/d03_gm_dashboard.md`

---

### TASK 1.4 — Gap Escalation Table (D-04)

**What:** Half-page reference. RS value at Gap formation → entity severity. Seasons unaddressed → Mend Ob increase.

**Content:**
- RS value at Gap formation → severity (Shifting Object / Weak entity / Full entity / Full + Shifting Objects in adjacent territories)
- Gap age → Mend Ob (Shifting Ob 2 → Fresh Gap Ob 3 → Entrenched Ob 6 → Catastrophic Ob 7)
- RS seasonal drain per Gap (−4/season active)
- Mending degree outcomes (Overwhelming/Success/Partial/Failure → RS change + Coherence cost)
- Special cases: Collective Mending ceiling (Ob 8); Catastrophic prerequisites (TS 70+ lead + 2× TS 20+)

**Source:** Scenario 6 (Gap formation and incursion), Stage 3 (thread operations).

**Output:** `gm_ref/d04_gap_escalation_table.md`

---

### TASK 1.5 — Coherence Band Track Reference (D-05)

**What:** Half-page formatted track. Coherence value → active penalties + recovery options. Replaces GM having to recall band effects mid-scene.

**Content:**
- Track: 10 → 8 (Stable) → 7–5 (Dissonant) → 4–3 (Fragmented) → 2 (Fractured) → 1 (Severed) → 0 (Rendering Crisis)
- Per band: mechanical penalties (dice penalties, Ob increases, social consequences)
- Per band: Knot strain rate
- Per band: Certainty max modifier
- Per band: trigger events (Fallout rolls, Belief co-authorship onset, dissociation checks)
- Recovery paths: full season non-practice / Anchoring Scene (Bonds TN 7 Ob 2) / cannot exceed 10 / no CP purchase
- Coherence loss sources: retention roll fail / residue use / operation failure degree tables

**Source:** Scenario 7 (Coherence degradation), Stage 3 §3.3.

**Output:** `gm_ref/d05_coherence_band_track.md`

---

### TASK 1.6 — Thread Operation Resolution Card (D-06)

**What:** Single-page procedure checklist. Step-by-step for every thread operation. GM runs through it in sequence.

**Content:**
- Pre-operation checks: TS threshold met? Contact mode (Leap or originary)? Combat eligibility check?
- Leap procedure: Priority → Diagnosis → Roll (pool + TN) → degree outcome
- Operation roll: pool by operation type + TN + current Ob modifiers
- Co-movement fires: [PLACEHOLDER — narrative cells filled by D-11]
- Post-operation: Coherence retention check trigger conditions / RS cost applied / TS growth check
- Quick-reference pools by operation type:
  - Leap: Attunement + History + TPS, TN 7
  - Weaving: Spirit + History + TPS, TN 7
  - Pulling: Spirit + History + TPS, TN 7
  - Lock: Spirit + History, TN 7, min Ob 4
  - Dissolution: Spirit + History, TN 7, min Ob 4
  - Mending: Attunement + Focus + TPS, TN 7
- Footnotes: scale RS cost modifiers (Object ×1 / Personal ×1 / Relational ×2 / Territorial ×3)

**Note:** Co-movement narration section (middle of card) will have placeholder boxes filled by D-11 (Opus task). Card is functional for procedure without those boxes — GM can run mechanics; co-movement narration is the enhancement.

**Output:** `gm_ref/d06_thread_operation_resolution_card.md`

---

### TASK 1.7 — NPC State Card Templates (D-07)

**What:** Standardised card format for each significant NPC. Flipped face-up when NPC enters scene. Populated from Stage 13 content.

**Structure per card:**
- Name / Faction / Role
- Faction stat block (Mandate/Stability/Influence etc. — NPC-specific subset)
- Personal: TS / Conviction / Resonant Style / Active Beliefs (3)
- Clock position (if applicable): current value + trigger conditions
- Impression Track: current value (if applicable)
- Destabilisation trigger (if defined)
- Scene notes: characteristic approach / failure mode

**NPCs to card (from Stage 13 + narrative chains):**
- Almud (Crown)
- Baralta (Hafenmark)
- Vaynard (Varfell)
- Lenneth (Revolution)
- Himlensendt (Church)
- Klapp (Church — CE track)
- Olafsson (Church — Intel)
- Ehrenwall (Löwenritter — Coup Counter)
- Torben (Crown — Loyalty Clock)
- Elske (Altonian court)
- Vaynard secondary NPCs as applicable

**Output:** `gm_ref/d07_npc_state_cards.md`

---

### TASK 1.8 — Knot Registry Template (D-08)

**What:** Half-page per-PC form. Player-maintained with GM copy. Tracks significant Knots and their current state.

**Content per Knot entry:**
- Connected entity (name/place/community/object)
- Knot strength (deliberate / organic / wrapping)
- Current strain (0–3, with threshold effects noted)
- Last Anchoring Scene (season + outcome)
- Strain rate (by Coherence band of practitioner)
- Severance threshold and consequence

**Also includes:** brief reminder of strain-by-Coherence-band table (cross-reference to D-05).

**Output:** `gm_ref/d08_knot_registry_template.md`

---

### TASK 1.9 — Co-movement Matrix Skeleton (D-09)

**What:** 2-page fold-out matrix. Rows: operation type × scale (6 rows). Columns: degree outcome (3 columns — Overwhelming/Success/Partial). Each cell has three sections: Temporal beat [OPUS], Epistemic beat [OPUS], d6 table [OPUS]. This task builds the skeleton with mechanical content filled and narrative sections clearly marked as Opus-fill placeholders.

**Mechanical content per cell (Claude fills now):**
- Temporal auto-effect classification: narrative-only vs Coherence retention trigger
- Epistemic auto-effect: specific social Ob modifier (from compiled degree tables)
- RS cost: exact value by operation type and degree
- Coherence retention Ob: accumulated Obs this Leap
- Any special flags (e.g., "Relational+ scale: retention roll required regardless of degree")

**Rows (6):**
1. Weaving — Object/Personal scale
2. Weaving — Relational+ scale
3. Pulling — Object/Personal scale
4. Pulling — Relational+ scale
5. Lock (all scales — Lock is always significant)
6. Mending (all scales — presented here for completeness; Dissolution/Past-Pull excluded as rare/campaign events)

**Columns (3):** Overwhelming / Success / Partial
(Failure: excluded from matrix — handled as improvised narrative given dramatic weight)

**Placeholder format for Opus cells:**
```
[TEMPORAL BEAT — OPUS]
Non-sensitive (TS 0–29): ___
Practitioner (TS 30–49): ___
Advanced (TS 50+): ___

[EPISTEMIC BEAT — OPUS]
Observation: ___
Social consequence: ___

[d6 PROMPT TABLE — OPUS]
1: ___  2: ___  3: ___
4: ___  5: ___  6: ___
```

**Separate half-page:** Relational+ supplement skeleton — same structure for the 2 Relational+ rows, with additional field for "who is knotted and what do they feel" (placeholder for Opus).

**Output:** `gm_ref/d09_comomovement_matrix_skeleton.md`

---

### TASK 1.10 — Framing Process — Structural Frame (D-10)

**What:** Half-page generative procedure. The 4-step process the GM runs when improvising co-movement consequences outside the matrix. Structural content only — philosophical framing and examples are Opus tasks (D-12, D-13).

**Content:**
```
STEP 1: IDENTIFY PRIMARY DIMENSION
  What was the practitioner's intended target?
  → Primarily temporal: the operation moves something in time
  → Primarily epistemic: the operation changes how something is known/perceived
  → Primarily actualized: the operation changes something's physical/factual state

STEP 2: IDENTIFY CURRENT STATE OF THE OTHER TWO DIMENSIONS
  For this specific configuration:
  → Temporal: how deep is its temporal accumulation? (recent = shallow; ancient = deep)
  → Epistemic: how accessible is it currently? (hidden = low; prominent = high)
  → Actualized: how stable is it currently? (fragile = low; robust = high)

STEP 3: CO-MOVEMENT DIRECTION AND MAGNITUDE
  The other two dimensions move in the same direction as the primary effect.
  → Magnitude: proportional to how directly the primary dimension was targeted
  → A primarily-actualized Weave: minor temporal shift + minor epistemic shift
  → A primarily-temporal Past-Pull: major actualized displacement + major epistemic disruption

STEP 4: NARRATE AT APPROPRIATE TS TIER
  → TS 0–29: ontical surface only — what changes in the observable, sensory world
  → TS 30–49: ontical + partial ontological — what changes + faint sense of the mechanism
  → TS 50+: full ontological — what changes + explicit awareness of all three dimensions moving
```

**Footnotes (mechanical, Claude):**
- "Temporal shift is not the target aging — it is a displacement of when this configuration belongs in the causal chain"
- "Epistemic shift is not forgetting — it is a change in how accessible this configuration is to consciousness"
- "Actualized shift is not destruction — it is a change in the configuration's factual properties"

**[PHILOSOPHICAL FRAMING — D-12 OPUS PLACEHOLDER]**

**Output:** `gm_ref/d10_framing_process_skeleton.md`

---

## PHASE 1 HANDOFF SPECIFICATION

Before Phase 2 begins, the following files must be complete and committed to GitHub:
- D-01 through D-10 in `gm_ref/` directory
- All mechanical values verified against CP14
- All Opus placeholder sections clearly marked with content requirements

Phase 2 Opus tasks receive as input:
- `canon/Valoria_Philosophical_Foundations.md` (canonical metaphysics)
- `designs/valoria_emergent_scenarios.md` (scenario context)
- `compilation/valoria_ruleset_checkpoint_14.md` (mechanical values)
- `gm_ref/d09_comovement_matrix_skeleton.md` (skeleton to fill)
- `gm_ref/d10_framing_process_skeleton.md` (skeleton to complete)

---

## PHASE 2 — NARRATIVE CONTENT (Opus)

All tasks in this phase require philosophical judgment: producing narration that is consistent with the Foundations' metaphysical framework, tonally appropriate, and demonstrably derived from the system's logic rather than generic fantasy flavor. Claude cannot execute these tasks — the co-movement consequences are philosophically load-bearing (incorrect narration teaches players a false model of the world).

**Execution method:** Each Opus task is a separate artifact (Opus-tier passthrough). Tasks are sequenced: D-11 before D-13 (examples depend on the matrix being complete).

---

### TASK 2.1 — Co-movement Matrix Narrative Cells (D-11)

**Opus task summary:** Fill all narrative sections of the D-09 skeleton. For each of the 18 cells (6 rows × 3 degree columns), produce:
- Temporal beat: 2–3 sentences, TS-split into three tiers (TS 0–29 / TS 30–49 / TS 50+), [TARGET] placeholder retained
- Epistemic beat: 1–2 sentences, [CONTEXT] placeholder retained for GM-specific detail
- d6 prompt table: 6 seeds, thematically consistent with operation type, each deliverable in one sentence

**Also:** Relational+ supplement — same structure for both Relational+ rows, plus one additional field per cell: "what does a knotted entity feel?" (one sentence, TS-split)

**Philosophical constraints for Opus:**
- Temporal beats must reflect Temporal Disjunction (§1.3, §19.2), not simply time-passage
- Epistemic beats must reflect epistemic inaccessibility (§1.2, §10.1), not simply confusion or forgetting
- TS tier differences must reflect genuine ontological/ontical distinction (§17), not just information quantity
- d6 seeds must be surprising but traceable to the operation type's logic — not arbitrary
- Failure degree is excluded from the matrix by design; Opus should not add it

**Input files:** D-09 skeleton + Foundations §1.1–1.3, §3.2, §17, §19

**Output:** `gm_ref/d11_comovement_matrix_complete.md` (D-09 skeleton with all placeholders filled)

---

### TASK 2.2 — Framing Process — Philosophical Content (D-12)

**Opus task summary:** Complete the D-10 skeleton by adding:
- One paragraph framing *why* the 4-step process works — what in the Foundations justifies this specific procedure
- Two "common error" footnotes: the most frequent philosophical mistakes GMs make when improvising co-movement, and why they're wrong
- One closing note on the relationship between the process and the examples (D-13) — how to use them together

**Philosophical constraints:**
- The process framing must derive from Inseparability (§1.1) and the Dual Consequence (§3.2)
- Common errors must be specific and correctable — not vague warnings
- Tone: instructional, not mystical; this is a craft document

**Input files:** D-10 skeleton + Foundations §1.1, §3.2

**Output:** `gm_ref/d12_framing_process_complete.md`

---

### TASK 2.3 — Annotated Examples (D-13)

**Opus task summary:** Write 8–12 worked examples of co-movement narration. Each example must be written in split-register format.

**Required coverage across examples:**
- At minimum 1 example per operation type (Weaving, Pulling, Lock, Mending)
- At minimum 2 examples at Relational+ scale
- At minimum 2 examples showing Partial degree (not just Overwhelming/Success)
- At minimum 1 example involving a non-practitioner observer
- At minimum 1 example involving a threadcut being as subject of operation

**Per example structure:**
```
EXAMPLE [N]: [Operation type], [Scale], [Degree]
SITUATION: [2-sentence scene setup — generic enough to be reusable]
WHAT THE GM KNOWS: [mechanical consequence from matrix — RS cost, Coherence trigger, Ob shift]
NON-SENSITIVE OBSERVER HEARS: [GM narration, ontical tier]
PRACTITIONER (TS 30–49) HEARS: [GM narration, partial ontological tier]
ADVANCED PRACTITIONER (TS 50+) HEARS: [GM narration, full ontological tier]
WHY THIS WORKS: [1–2 sentences — which principle from the Foundations this narration enacts]
```

**Philosophical constraints:**
- Each example must be traceable to specific Foundations principles (cite section)
- "Why this works" annotations are the highest-value content — they teach the process, not just the output
- All examples must use [TARGET] and [CONTEXT] placeholders to remain generic
- No example should require knowledge of specific Valorian factions/NPCs to be useful

**Input files:** D-11 complete + Foundations full + D-12 complete

**Output:** `gm_ref/d13_annotated_examples.md`

---

### TASK 2.4 — Counter-examples (D-14)

**Opus task summary:** Write 4–6 "what went wrong" examples showing philosophically incorrect co-movement narration and explaining the error.

**Required coverage:**
- At minimum 1 counter-example showing a temporal beat narrated as simple time-passage (error: conflating temporal displacement with aging/duration)
- At minimum 1 counter-example showing an epistemic beat narrated as simple forgetting (error: conflating epistemic inaccessibility with memory loss)
- At minimum 1 counter-example showing a Weaving narrated as only affecting the actualized dimension (error: violating Inseparability)
- At minimum 1 counter-example showing TS tiers as simple information quantity (error: missing the ontical/ontological distinction)

**Per counter-example structure:**
```
COUNTER-EXAMPLE [N]: [Operation type], [Error type]
WHAT THE GM SAID: [incorrect narration, 2–3 sentences]
WHY IT'S WRONG: [specific Foundations principle violated]
WHAT THE PLAYER NOW BELIEVES: [the false model this narration teaches]
CORRECTED VERSION: [correct narration in same situation]
```

**Philosophical constraints:**
- "What the player now believes" is the most important field — it identifies downstream consequence of the error
- Corrections must follow the same TS-split format as D-13
- Errors should be plausible mistakes, not obvious ones — the kind a thoughtful GM would make

**Input files:** D-13 complete + Foundations full

**Output:** `gm_ref/d14_counter_examples.md`

---

## PHASE 3 — INTEGRATION (Claude)

### TASK 3.1 — Assemble GM Reference Suite (D-15)

**What:** Combine all Phase 1 and Phase 2 outputs into a single structured reference document organized for table use.

**Structure:**
```
SECTION A: LIVE STATE REFERENCES (print and laminate)
  D-03 GM Dashboard
  D-01 Cascade Consequence Reference
  D-05 Coherence Band Track Reference
  D-04 Gap Escalation Table

SECTION B: PROCEDURE CARDS (print and laminate)
  D-06 Thread Operation Resolution Card
  D-11 Co-movement Matrix (2-page fold-out)
  D-10/D-12 Framing Process (complete)

SECTION C: SESSION TOOLS (print fresh each session or maintain digitally)
  D-02 Seasonal Accounting Form
  D-07 NPC State Cards
  D-08 Knot Registry Template

SECTION D: GM TRAINING MATERIAL (read before campaign; not at table)
  D-13 Annotated Examples
  D-14 Counter-examples
```

**Format decisions:**
- Section A/B items: formatted for print; no prose; maximum visual clarity
- Section C items: form-style with blank fields; fillable
- Section D items: prose document; reference manual format

**Commit:** All files to `gm_ref/` directory on GitHub. Assembled suite to `gm_ref/valoria_gm_reference_suite.md`.

**Update:** `session_log_current.md` with workplan completion and next action.

---

## SEQUENCING AND DEPENDENCIES

```
Phase 1 tasks: parallel (no interdependencies)
  1.1 → 1.2 → 1.3 → 1.4 → 1.5 → 1.6 → 1.7 → 1.8 → 1.9 → 1.10
  (can be executed sequentially in one session)

Phase 2 tasks: sequential (each depends on prior)
  2.1 (D-11) → must complete before 2.3 (D-13)
  2.2 (D-12) → must complete before 2.3 (D-13)
  2.3 (D-13) → must complete before 2.4 (D-14)
  
  Note: 2.1 and 2.2 can run in parallel (independent inputs)

Phase 3: after all Phase 2 tasks complete
  3.1 assembles all outputs
```

---

## OPUS PASSTHROUGH NOTE

Passthrough templates (`opus-passthrough.html`) not found in current session. Claude will construct Opus API calls directly using the documented pattern. Each Phase 2 task will be instantiated as a separate artifact with:
- Full Foundations text as context
- Relevant skeleton file as input
- Precise task specification from this workplan
- JSON-only output instruction for structured cells (D-11)
- Prose output for D-12, D-13, D-14

Each Opus artifact is self-contained and produces a single output file. User approves each output before it is committed to GitHub.

---

## SCOPE BOUNDARIES

**In scope:** Everything listed above.

**Out of scope (for this workplan):**
- The digital companion app (G-009, deferred) — would supersede some of these tools but is not a prerequisite
- Formatting for print layout / graphic design — outputs are structured markdown; layout is a separate production task
- Board game specific references — the matrix and tracking tools are TTRPG-mode only; board game equivalents are a separate workplan
- Any gap register items — this workplan is reference tooling only, not ruleset expansion

---

## ESTIMATED SESSION COST

| Phase | Tasks | Est. Claude tokens | Est. Opus calls |
|-------|-------|-------------------|----------------|
| Phase 1 | 10 tasks | ~15–20k | 0 |
| Phase 2 | 4 tasks | ~2k (artifact setup) | 4 artifacts |
| Phase 3 | 1 task | ~3–5k | 0 |
| **Total** | **15 tasks** | **~20–27k Claude** | **4 Opus artifacts** |

*Phase 1 executable immediately. Phase 2 requires user approval of each Opus artifact output before commit. Phase 3 follows Phase 2 completion.*
