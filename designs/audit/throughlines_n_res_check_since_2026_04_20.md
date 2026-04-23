# N-check + Res-check — Throughlines Introduced Since 2026-04-20

**Scope:** 16 throughlines + 5 meta-throughlines introduced in the 2026-04-20 → 2026-04-22 work window.
**Sources:** `session_master_2026_04_20.md` (T-26..T-30), `rigorous_audit_synthesis_s1_s7_v3_1.md` (T-31..T-41, М-7..М-11).
**Methodology:**
- **N-check (necessity):** Does this throughline carry load no other throughline already carries, and is its absence materially detrimental to the design? Pass / Fail / Qualified.
- **Res-check (resolution):** Does it have (a) canonical home, (b) mechanical surface, (c) verifiable closure criteria? Full pass = all three. Partial = 1–2. Fail = none.
- Per-item: identifiers, chain summary, N verdict + rationale, Res verdict + rationale, gap/warning/flag as applicable.

---

## §1. Novel Throughlines (T-26..T-41) — 16 items

### T-26: Recursion as Setting Structure

**Chain.** Solmund threadwork → Church misidentifies as miracle → Church founded on misidentification → Mending/RWCE in present → misidentified again → new scripture/Heresy Investigation on the same error.

**N-check: PASS.** Recursion is structural, not narrative. No other throughline captures the *reproduction* of the founding error under prophylaxis. T-08 (Church rendering) describes the misidentification mechanism at a single beat; T-26 is about its iteration across generations. Without T-26, Miracle Investigation arcs lack the "same error, new surface" dramatic shape that distinguishes them from one-off investigations. Absence would flatten the Church's political-theological stakes into static doctrine enforcement.

**Res-check: PARTIAL.**
- Home: ✓ (RWCE cascade + Church priority tree).
- Mechanical surface: ✓ (POI Seam Text discovery; Miracle Investigation arcs; Certainty revision).
- Closure criteria: ✗ (no stated condition for "recursion stops when prophylaxis cracks" — long-run variable but no threshold or trigger specified).

**Flag.** Closure criteria should reference T-29 (Baralta prophylaxis crack) as the mechanical path; without that link, T-26 reads as a description of the setting rather than a playable dynamic.

---

### T-27: Effects Real, Explanation Wrong

**Chain.** Real observable effect → only institutionally-load-bearing explanation available → faction acts on wrong explanation → effect continues producing consequences under wrong frame → incompatible explanations produce triple-interpretation conflict.

**N-check: PASS.** This is the epistemic engine of the entire faction-interpretation system. No sibling throughline generalizes the pattern across factions. T-08 and T-29 are instances of T-27 applied to specific factions. Absent T-27, the triple-interpretation system lacks a stated principle; designers would implement ad-hoc per faction and drift.

**Res-check: FULL PASS.**
- Home: ✓ (faction AI priority trees).
- Mechanical surface: ✓ (Seam Text TS-gating, Filter chain, Conviction track).
- Closure criteria: ✓ (Conviction Scar targeting on specific effect/explanation mismatches — noted as "pending" but criterion type is clear).

**Flag.** Implementation item listed as "pending Conviction Scar targeting" — Wave 1 workplan should confirm this maps to a specific PP entry.

---

### T-28: Confrontation / Leap / Operation Triad

**Chain.** Confrontation (perceptual) → TS development → Leap (layer-2 suspension) → Operation (restorative/manipulative/destructive) → knot-profile accumulation → bidirectional substrate-events.

**N-check: PASS.** Load-bearing three-layer distinction the Church conflates into a single suspect category. Without this triad split, the Mending-no-cost/manipulation-some-cost/destruction-catastrophic asymmetry has no rationale; the Coherence system collapses to flat cost-per-op. No other throughline makes this distinction; T-12 (practitioner arc) describes lived experience but not the categorical split.

**Res-check: FULL PASS.**
- Home: ✓ (`canon/02_foundations_amendment_leap_mechanism.md` canonical; `threadwork_v30` §2.3, §31 implement).
- Mechanical surface: ✓ (Coherence costs differentiated per operation type; knot-profile character sheet specified).
- Closure criteria: ✓ (foundations committed, knot-profile pending Godot — concrete implementation item).

---

### T-29: Baralta as Accidental Prophylaxis Cracker

**Chain.** Baralta's direct-communion theology → contingency into essentialist cognitive frame → weakened Prophylaxis in populations under her influence → higher per-capita confrontation retention → slow TS development rate lift in Hafenmark → eventual breach of Church's prophylactic closure.

**N-check: PASS.** Only throughline providing a mechanism by which T-26's recursion stops. Strategic value: makes Hafenmark a structurally different long-game territory in ways the player can influence. Absence would mean prophylaxis is a fixed world parameter rather than a player-influenceable variable.

**Res-check: PARTIAL.**
- Home: ✓ (NPC §6 Baralta theology canonical).
- Mechanical surface: ✗ (prophylaxis-as-variable mechanic is *pending*; no current design specifies territorial prophylaxis rating or its inputs).
- Closure criteria: ◐ (implicit: "breach of prophylactic closure in Hafenmark territories" — threshold unspecified).

**Flag.** Largest design gap in this batch. Prophylaxis-as-variable is referenced by T-26, T-29, and implicitly T-32/T-33. Needs a dedicated design doc — currently it's distributed across implementation-status notes. Suggest: `designs/world/prophylaxis_mechanic.md` or extension to threadwork.

---

### T-30: Information Asymmetry as Core Mechanic

**Chain.** Player POV (full framework) → Character POV (perception-bounded) → gap → player decisions inform character choices that character would not make with character-only information → triple-interpretation compounds.

**N-check: PASS.** Explicit statement of the central UX principle. Every POV-related system (Filter chain, TS visibility tables, chronicler divergence, Conviction Scene UX) presupposes this throughline. Absent T-30, designers have no stated principle for when to expose framework-level information to the player vs hide it behind character perception.

**Res-check: FULL PASS.**
- Home: ✓ (investigation_systems Filter chain, TS visibility tables).
- Mechanical surface: ✓ (all four systems named are implemented or specified).
- Closure criteria: ✓ (chronicler divergence specified-not-coded; Conviction Scene UX must preserve asymmetry — both verifiable).

---

### T-31: Reflexive Suspension

**Chain.** canon/02 Am 1 → TS-band receptive capacity → entry commit locks sequence up to (Focus − 1) → Leap Roll → reflexive facing suspends, outward persists, layer 1 Ein Sof spools → sequence executes committed → exit (voluntary or Fatigue-threshold) → Retention Roll → reflexive reasserts, knots register below reflexive-access threshold.

**N-check: QUALIFIED PASS.** Describes mechanical flow of the Leap, not a constitutive chain. Overlaps substantially with T-28 (Leap is the middle step of T-28's triad). Distinction: T-28 is the category split (Leap vs Confrontation vs Operation); T-31 is the internal structure of the Leap itself. Qualifies as necessary because the two-decision commitment structure (entry + exit only, no mid-contact modification) is the specific UX commitment that distinguishes Leap from generic action resolution.

**Res-check: PARTIAL.**
- Home: ✓ (canon/02 Am 1 + threadwork_v30 §2.3).
- Mechanical surface: ◐ (entry-commit UX + contact-phase execution + retention degree + knot-profile two-layer UX — all named, all proposed).
- Closure criteria: ✗ (no stated "how we know this is implemented correctly" criterion; Wave 1 P1 is named but workplan atomization is pending).

**Warning.** T-31 is almost entirely implementation-spec dressed as a throughline. If T-28 is present, T-31's load is carried by P1 workplan entries, not by throughline registry. Not a fail, but the redundancy is worth flagging — may be cleaner to demote T-31 to workplan-level spec.

---

### T-32: Sincere Structural Closure

**Chain.** canon §9 → observer confronts excess-being → receptive capacity gates reception → formation auto-generates motor-plausible explanation → no residual dissonance → propositional argument cannot crack → only confrontational experience under integrative conditions produces cracking.

**N-check: PASS.** States the principle that Church position on threadwork is not delusion or cynicism but formation-structural anosognosia. Without T-32, Church dialogue writers default to either "Church knows it's wrong and is cynical" or "Church is ignorant and can be educated" — both wrong. No other throughline carries this load.

**Res-check: PARTIAL.**
- Home: ✓ (canon §9 referenced).
- Mechanical surface: ✓ (Church NPC dialogue generator; canon §9; faction formation; Baralta partial prophylaxis per T-29).
- Closure criteria: ◐ (Wave 1 P3 named; no verification criterion for "dialogue correctly refuses propositional-argument cracks").

**Flag.** Verification criterion should be testable — e.g. "Church NPC dialogue-generator trees have no argument-path that updates faction priority weights absent confrontation event." Without that, it's a design intention.

---

### T-33: TS as Developmental Arc

**Chain.** canon §14 → confrontation held under integration-supportive conditions → cumulative receptive-capacity development → band threshold crossings at TS 30/50/70/90 → practitioner waterline lowers → more of substrate-iceberg receivable per canon/01 Am 3.

**N-check: PASS.** Specifies that TS is a receptive-capacity axis, not a power axis. Substantial consequence: invariant substrate-iceberg across observers; higher TS receives more of the same given at ordinary perception. T-12 (practitioner arc) describes progression lived experience; T-33 specifies the *mechanism* of that progression. Both needed.

**Res-check: FULL PASS.**
- Home: ✓ (canon §14; canon/01 Am 3 explicit).
- Mechanical surface: ✓ (TS track; Certainty track; band-crossing Event Scenes; dialogue registers; ambient content differentiation).
- Closure criteria: ✓ (Wave 1 P2/P9/P10 named as implementation waves; band thresholds numerically specified).

---

### T-34: Distal Interoception through Knot Tethers

**Chain.** Practitioner forms knot → knot persists at substrate depth below reflexive-access threshold → tethered post-surface → continuous seismographic signal via canon/02 Am 6 intelligence-mechanic (no dice roll; somatic) → signal reports MS state, vulnerability, affective valence of knotted territories.

**N-check: PASS.** Only throughline establishing a *within-character* information channel for what canon/02 Am 2 says reflexive self-rendering cannot access. This is the diegetic answer to "how does the practitioner character know what their player knows about knotted territories." Absent T-34, the player-character information gap becomes literal gameplay problem (how does the character reference knotted territories at all?).

**Res-check: PARTIAL.**
- Home: ✓ (canon/02 Am 6 referenced).
- Mechanical surface: ◐ (knot-profile diagnostic panel + ambient somatic layer + vulnerability-trigger cues + signal clarity variable — all proposed, Wave 2 P15 Layer 2).
- Closure criteria: ✗ (no stated signal-clarity rubric; no specification of what "signal" means in UI terms — visual? audio? text ticker?).

**Flag.** This is a player-facing UI commitment without a UI spec. Not blocking, but P15 Layer 2 workplan should include UX decision: how does the game represent seismographic signal without collapsing into text?

---

### T-35: Unified Uncanny Capacity Synthesis

**Chain.** Observer encounters category-resistant entity or Fragmented-band practitioner → receptive capacity (observer TS band) gates received content → observer formation + frame processes received content → frame-consistent uncanny register emerges per observer-TS.

**N-check: QUALIFIED PASS.** Mostly covered by T-27 (effects real, explanation wrong) + T-30 (information asymmetry) + T-33 (TS as developmental arc). T-35's unique contribution: explicit commitment that the *same entity* produces *different uncanny registers* in different observers based on TS band + formation. Without T-35, dialogue writers might make monstrosity-perception uniform across observers; T-35 forbids that.

**Res-check: PARTIAL.**
- Home: ✓ (distributed across dialogue generator, threadcut rendering §6.2, Fragmented-band, Providence-being).
- Mechanical surface: ◐ (observer-TS branching named; specific register-per-band table not specified).
- Closure criteria: ✗ (no test for "uncanny registers correctly differ across observers").

**Warning.** T-35 is load-bearing for dialogue and monstrosity UI but has the thinnest resolution of the T-31..T-41 batch. Wave 4 P17 workplan needs to deliver the observer-TS × entity-type register table.

---

### T-36: Relational Ontological Identity (TS 50–69 Coherence 0)

**Chain.** Career operations → cumulative Coherence depletion → Coherence 0 at TS 50–69 → layer 2 self-rendering ceases → canon/01 Am 4 TS-gated outcome: companion knots become load-bearing → identity sustained through named bonds → knot severance produces structural disassembly → isolation is categorically lethal.

**N-check: PASS.** Specifies an ending-trajectory outcome no other throughline carries. The "Coherence-career-floor" editorial flagged in the 2026-04-21 handoff is this throughline's dramatic core. Without T-36, long-career Warden endings default to either death or retirement — T-36 specifies a third option (relational survival) that is trajectory-conditional.

**Res-check: PARTIAL.**
- Home: ✓ (canon/01 Am 4 TS-gated outcome).
- Mechanical surface: ✓ (companion system; knot-profile load-bearing state flag; dialogue generator companion-indexed registers).
- Closure criteria: ✗ (Wave 3 P22 named; "Coherence-career-floor" editorial still open per handoff — unresolved prerequisite).

**Flag.** Blocked on the pending Coherence-career-floor editorial. Cannot fully close until that lands.

---

### T-37: Stimulus Resistance Triplet

**Chain.** Substrate-adjacent stimulus → resistance mode by integration-failure type → predication resistance (naming fails); grammaticalisation resistance (relational grammar fails); categorisation resistance (taxonomic placement fails).

**N-check: QUALIFIED PASS.** Carries load no other throughline carries — three distinct modes of integration-failure for substrate-adjacent stimuli. Qualifies because the mechanical surface (three-register dialogue templates) has significant overlap with T-35's observer-TS branching. Distinction: T-37 is about *stimulus* (what fails to integrate), T-35 is about *observer* (who fails to integrate). Both needed but they'll often co-fire; writer discipline required.

**Res-check: PARTIAL.**
- Home: ◐ (distributed across dialogue three-register templates, environmental substrate-excess amplitude, Seam Text vs Church text generator).
- Mechanical surface: ✓ (NPC dialogue templates; Seam Text vs Church; unified category-resistance register).
- Closure criteria: ◐ (Waves 2+4 P7/P12/P17 named; no explicit test for "three resistance modes correctly distinguished in output").

---

### T-38: Real as Continuous Amplitude (Within the Renderable)

**Chain.** Substrate is excess at all times → every location has substrate-excess amplitude (ordinary/moderate/mid-high/high/extreme) → TS development expands predicate set; extreme amplitude remains beyond highest TS predicate sets.

**N-check: PASS.** Critical commitment: there is no substrate-quiet location. This has consequences for environmental design, shader scaling, audio registers, monstrosity UX. Without T-38, designers implicitly assume "normal world plus substrate incidents" — T-38 forbids that. No sibling throughline makes this commitment.

**Res-check: PARTIAL.**
- Home: ◐ (distributed across environmental design amplitude per region, shader/audio registers, NPC dialogue amplitude-keyed, monstrosity UX).
- Mechanical surface: ✓ (five-level amplitude scale specified; Gap-proximity gradient named).
- Closure criteria: ✗ (no specification of *which* territories get *which* amplitude; environmental-quality composite consolidation P13 + P21 named but not atomized).

**Flag.** The territory-by-territory amplitude map is a content task, not a design task. But without it, T-38 cannot be fully resolved. Suggest: add to a worldbuilding workplan distinct from the mechanical waves.

---

### T-39: Textual Mode Typology

**Chain.** In-world expressive output → four production modes: below-waterline cartographic (inner-tradition); Church doctrinal; Coherence-degraded; other-faction doctrinal (Varfell/Baralta/RM) → observer receptive capacity (TS + formation) determines legibility.

**N-check: PASS.** No other throughline commits to four in-world textual modes with distinct grammatical structures. Consequence for text generators, environmental storytelling, historical corpus. Without T-39, in-world documents drift toward single-register "fantasy scripture" flavor.

**Res-check: PARTIAL.**
- Home: ◐ (distributed across text generator templates, dialogue faction-AI variants per T-27, historical corpus).
- Mechanical surface: ◐ (four-mode templates named; per-faction generators named; TS-correlated text rendering named; actual grammatical specs not written).
- Closure criteria: ✗ (Wave 2 P12 core named; no specification of what distinguishes the four grammatical structures).

**Flag.** This is the hardest-to-verify throughline in the batch. "Distinct grammatical structures" is a content-creation discipline; closure requires either explicit grammar rules or sample text per mode validated against the rules.

---

### T-40: TS as Taxonomic Expansion

**Chain.** Confrontation retention → TS band thresholds → new framework-taxonomic categories admitted. TS 30+ substrate-effect. TS 50+ relational thread-structure, threadcut mode. TS 70+ structural reality, Accord as institution. TS 90+ full substrate topology, environmental-strain awareness.

**N-check: QUALIFIED PASS.** Overlaps with T-33 (TS as developmental arc). Distinction: T-33 is the *rate/mechanism* of TS development; T-40 is the *content* admitted at each band. Both needed because a designer asking "what does this character perceive at TS 52" needs T-40's category list, not T-33's arc.

**Res-check: PARTIAL.**
- Home: ✓ (band thresholds specified numerically).
- Mechanical surface: ✓ (band-threshold Event Scenes; map UI TS-keyed overlays; dialogue generator high-TS taxonomy; text rendering shift).
- Closure criteria: ◐ (Wave 1 P21 + Wave 2 P2 named; no complete category table).

**Flag.** Need the exhaustive "what categories unlock at what band" table — currently four examples are given but not exhaustive.

---

### T-41: Damaged Substrate Is Non-Agential

**Chain.** Substrate damage (Gap, dissolution residue, Calamity residue, wounded territory, threadcut de-actualisation) → rendering effects (distortion, Coherence pressure, solastalgia) → without moral agency, corruption, demonism, malice, qelippot analog → art direction: desaturation/coldness/absence/wrongness → NPC response: non-moralising recognition or T-27 interpreter output → player response: contain/flee/survive; never defeat via damage.

**N-check: PASS.** Strong ontological commitment: framework refuses demonology. Consequence for art direction, monstrosity UX, Church demonic framing (which becomes T-27 interpreter output, not reality). Without T-41, designers default to JRPG-style corruption-as-antagonist; T-41 forbids that.

**Res-check: PARTIAL.**
- Home: ◐ (distributed across monstrosity art direction, damaged-substrate zones environmental design, Gap manifestation UX, solastalgia vulnerability triggers, Church demonic framing).
- Mechanical surface: ✓ (multi-proposal Wave 1 P7 + Wave 2 P5 + Wave 3 P14 solastalgia + art direction design guidance).
- Closure criteria: ◐ ("never defeat via damage" is a design discipline; verification requires no combat action has damage-zone as opponent).

**Flag.** Verification discipline should be an explicit rule in action/combat design docs: "no damage-zone is a combat opponent." Without that rule, drift is likely.

---

## §2. Novel Meta-Throughlines (М-7..М-11) — 5 items

### М-7: Borrowings Are Operational Extensions

**Pattern.** Every scholarly-lineage concept the framework adopts contributes a component to a composite operational assembly. Each component is structurally continuous with its source; each is deployed within framework's architecture rather than preserved in source-native register.

**N-check: PASS.** Critical meta-pattern. Without М-7, borrowings (Husserl epoché, Metzinger PSM, Kierkegaard leap, Lurianic tzimtzum, clinical phenomenology, Gibsonian ecological, etc.) would each need individual justification and might fragment into pastiche. М-7 states the pattern and provides the audit criterion: composite is framework-original in assembly; components have clean precedent. No sibling meta-throughline carries this.

**Res-check: PARTIAL.**
- Home: ◐ (canonical acknowledgment pending per ED-738 §8 — canon/00 §1.2 extension).
- Mechanical surface: ○ (М-7 is a design-discipline meta-pattern; it doesn't have a mechanical surface in the game world, it has a review surface in the design process).
- Closure criteria: ◐ (25+ instance cells across Sessions 1–7 catalogued; pending canon acknowledgment).

**Flag.** Canon/00 §1.2 extension is the landing strip for М-7 and is pending. Until landed, М-7 is an audit finding not canon.

---

### М-8: Access Is Vertical-Position Gated (Within the Renderable)

**Pattern.** What any being can receive is gated by position relative to waterline of ordinary rendering: ordinary perception above; reflexive+outward facing at; below-waterline content receivable during Leap or at TS-cultivated receptive capacity. Renderable terminates at Ein Sof structural wall for all beings.

**N-check: PASS.** Generalizes across T-27, T-30, T-31, T-32, T-33, T-35, T-37, T-40. Without М-8, these T's share a pattern with no stated principle. М-8's contribution: the waterline metaphor + Ein Sof terminus unifies every TS-gating and observer-capacity commitment the framework makes.

**Res-check: FULL PASS.**
- Home: ✓ (canon/01 Am 3 explicit; ED-738 §5 correction).
- Mechanical surface: ○ (meta-pattern; its surface is the TS visibility tables, Filter chain, Seam Text gating already implemented or pending per its child T's).
- Closure criteria: ✓ (9+ T-level instances catalogued; dependencies mapped: М-8 → М-4).

**Note.** М-8 is the cleanest pass in this batch — it does meta-pattern work without attempting to be a mechanical spec.

---

### М-9: Ontological Inversion of Clinical Phenomenology

**Pattern.** Framework adopts clinical trauma-phenomenology vocabulary while inverting causal direction: condition is real in the world (substrate ontological), not delusional in the patient (perceiver pathology).

**N-check: PASS.** Critical discipline-setting meta-pattern. Without М-9, designers borrowing clinical terminology risk pathologizing characters rather than depicting substrate reality. М-9 states the inversion rule explicitly. No sibling meta-throughline carries this.

**Res-check: FULL PASS.**
- Home: ✓ (derived from Sessions 1–7 Observation 7; 12+ instances documented).
- Mechanical surface: ○ (meta-pattern; surface is the dialogue generator and faction framing decisions that instantiate it).
- Closure criteria: ✓ (12 instance pairings explicit: Prophylaxis ↔ anosognosia, Fragmented band ↔ Capgras, etc.; dependency М-9 → М-7 stated).

---

### М-10: Environment as Constitutive Medium (Bounded by the Renderable)

**Pattern.** Environment is constitutive of practitioner capacity, not backdrop. Integrates 4E cognition at substrate-ontological register. Per ED-738: М-10 operates within the renderable; Ein Sof is not an environment.

**N-check: PASS.** No sibling meta-throughline makes the "environment is constitutive, not backdrop" commitment. Consequence for level design, exploration mechanics, knot-profile environmental tethering, ART restorative environments supporting TS development. Without М-10, environment defaults to setting-flavor; М-10 forbids that.

**Res-check: PARTIAL.**
- Home: ◐ (five-cell convergence S6-C32..C36; ED-738 positioning note exists).
- Mechanical surface: ○ (meta-pattern; surface is T-33/T-38/T-16/T-34/T-40 mechanical instantiations).
- Closure criteria: ◐ (five-instance convergence + supplementary evidence; dependencies stated: М-10 → М-3, М-10 → М-2).

**Flag.** Weakest resolution among the meta-throughlines. Depends on T-34 (distal interoception) and T-38 (continuous amplitude), both of which are themselves partially resolved. Recursive dependency means М-10 cannot fully close until those T's close.

---

### М-11: Voluntary and Involuntary Capacity Duality

**Pattern.** Same structural phenomenological capacity yields opposite valences depending on agency and context. Capacity neutral; mode of engagement (chosen+cultivated vs undergone without support) determines developmental trajectory. Integration-supportive conditions is the mechanism by which involuntary encounters become cultivated capacities.

**N-check: PASS.** Central UX-discipline commitment: the game must distinguish voluntary and involuntary registers for phenomenologically similar states. Without М-11, DPDR (voluntary opacity practice vs involuntary Coherence-degraded distress), dissociation (trauma vs training), meta-awareness (degraded vs cultivated) collapse into single categories. Pedagogy → structural mechanism is the design principle М-11 supplies.

**Res-check: FULL PASS.**
- Home: ✓ (five-instance convergence Sessions 1/3/5/7).
- Mechanical surface: ○ (meta-pattern; surface is UX-register distinctions in dialogue, state-machine flags, Event Scene framing).
- Closure criteria: ✓ (five instances explicitly paired: DPDR, peritraumatic dissociation, meta-awareness, automatic expression, below-waterline perceptual relocation; dependency М-11 → М-6).

---

## §3. Summary Table

### Throughlines (T-26..T-41) — 16 items

| ID | N-check | Res-check | Primary flag |
|---|---|---|---|
| T-26 | PASS | PARTIAL | Closure criteria ← T-29 link needed |
| T-27 | PASS | FULL | Confirm Conviction Scar PP entry |
| T-28 | PASS | FULL | Knot-profile Godot pending |
| T-29 | PASS | PARTIAL | Prophylaxis-as-variable design gap — largest in batch |
| T-30 | PASS | FULL | Conviction Scene UX preservation pending |
| T-31 | QUALIFIED | PARTIAL | May be workplan-spec, not throughline |
| T-32 | PASS | PARTIAL | Needs testable verification criterion |
| T-33 | PASS | FULL | — |
| T-34 | PASS | PARTIAL | UI spec for seismographic signal missing |
| T-35 | QUALIFIED | PARTIAL | Observer-TS × entity-type register table needed |
| T-36 | PASS | PARTIAL | Blocked on Coherence-career-floor editorial |
| T-37 | QUALIFIED | PARTIAL | Distinct from T-35 in principle, co-fires in practice |
| T-38 | PASS | PARTIAL | Territory-by-territory amplitude map needed |
| T-39 | PASS | PARTIAL | Grammatical specs for four modes missing |
| T-40 | QUALIFIED | PARTIAL | Exhaustive band category table needed |
| T-41 | PASS | PARTIAL | "No damage-zone combat opponent" rule needed in combat design |

**Distribution:** 12 PASS / 4 QUALIFIED / 0 FAIL · 4 FULL / 12 PARTIAL / 0 FAIL.

### Meta-throughlines (М-7..М-11) — 5 items

| ID | N-check | Res-check | Primary flag |
|---|---|---|---|
| М-7 | PASS | PARTIAL | Canon/00 §1.2 extension pending (ED-738 §8) |
| М-8 | PASS | FULL | Cleanest pass |
| М-9 | PASS | FULL | — |
| М-10 | PASS | PARTIAL | Recursive dependency on T-34, T-38 |
| М-11 | PASS | FULL | — |

**Distribution:** 5 PASS / 0 QUALIFIED / 0 FAIL · 3 FULL / 2 PARTIAL / 0 FAIL.

---

## §4. Aggregate Findings

**N-check aggregate.** 17/21 unconditional pass; 4/21 qualified pass; 0 fail.

The qualified items are T-31, T-35, T-37, T-40 — all throughlines whose load is real but partially carried by a sibling. Recommendation: hold them but flag the overlap in the registry to guide writers on which to invoke when.

**Res-check aggregate.** 7/21 full pass; 14/21 partial; 0 fail.

The partial rate is high because the batch is *new*. All 11 post-atomization throughlines and 4/5 meta-throughlines come from the rigorous audit synthesis and carry Wave 1–4 workplan dependencies. "Partial" here overwhelmingly means "landed as design; implementation/verification pending." This is expected.

**Largest concrete gaps:**

1. **T-29 prophylaxis-as-variable mechanical design** — blocker for T-26 closure and T-32 partial closure. Suggest dedicated design doc. *(High priority — covers multiple throughlines.)*
2. **T-36 Coherence-career-floor editorial** — already flagged in 2026-04-21 handoff. *(Was already queued.)*
3. **М-7 canon/00 §1.2 extension** — flagged in ED-738 §8. *(Was already queued.)*

**Recommendations.**

1. Resolve prophylaxis-as-variable gap via a dedicated design doc — it's referenced by four items and has no owner.
2. Demote T-31 to workplan-spec unless there's a specific reason to keep it throughline-level. Currently it reads as P1 Wave 1 pre-materialized.
3. T-39 (textual mode typology) needs either grammatical specs or validated sample text; otherwise resolution will stall indefinitely.
4. Add "no damage-zone is a combat opponent" as explicit rule in combat design docs to resolve T-41's verification discipline gap.

**No items fail outright.** Every throughline introduced since Monday has merit and a designated (if pending) landing. The work is load-bearing; the gaps are implementation not principle.

---

*End N-check + Res-check.*
