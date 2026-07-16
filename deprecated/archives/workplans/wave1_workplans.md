# Wave 1 Workplans — P1, P3, P9, P10, P21

**Purpose.** Atomization-oriented workplans for the five G-core N-direct proposals identified in `gameplay_assessment.md` §2 Wave 1 schedule. Each workplan takes a proposal from synthesis-level specification to atomization-ready specification by enumerating: (a) canonical anchors, (b) pre-implementation decisions required, (c) implementation-unit breakdown, (d) cross-proposal dependencies, (e) verification criteria.

**Status.** Proposal. No commits. Each workplan requires editorial approval before individual PP entries are drafted for atomization register.

**Editorial sequence.** Each workplan becomes a design-workplan document after the v3.1 synthesis + registry additions + meta-throughline additions commit. Workplan commit order: (1) dependencies-upstream proposals first, (2) proposals with fewest open decisions next, (3) broadest-scope proposals last. Under this rule, commit order is: P1 → P3 → P10 → P9 → P21.

**Reference baselines.**
- `rigorous_audit_synthesis_s1_s7_v3_1.md` — synthesis-level proposal.
- `mechanical_implementation_revised.md` §1, §4, §5, §6, §8 — mechanical specification.
- `mechanical_implications_revised.md` — decision architecture + feedback loops.
- `gameplay_assessment.md` — G-tier + contribution analysis.

---

## §1 P1 Workplan — Leap UX as Two-Decision Player Surface

### §1.1 Canonical anchors

- canon/02 Am 1: reflexive facing suspends; outward facing persists; layer 1 spooling continues.
- canon/02 Am 2: directional knot formation below reflexive-access threshold.
- canon/02 Am 3: operation-type determines Coherence cost.
- canon/02 Am 6: knot-profile four mechanical consequences.
- threadwork_v30 §2.3: Leap Roll mechanic, Thread Fatigue, Focus role.
- threadwork_v30 §2.4: operations, Ob tables.
- threadwork_v30 §3.2: Coherence reduction table + FR surcharge PP-196.

### §1.2 Pre-implementation decisions required

Blockers for atomization:
- `[DECISION P1-1]` Surprise/prone Ob modifier for attacks on submerged character body. Requires review of canonical combat defense modifiers.
- `[DECISION P1-2]` Multi-sentinel stacking: cap or accumulate. Proposal: cap at +2D total (matches canonical History-bonus cap pattern). Requires editorial confirmation.
- `[DECISION P1-3]` Conditional exit trigger complexity: single-variable or compound. Proposal: single-variable (Fatigue %, Coherence accumulated cost, or operation count). Requires editorial confirmation.

Non-blockers (can proceed without):
- Weaving Fatigue rate (4/round proposed per Mending parallel) — separate canonical inconsistency resolution.
- Retention Roll Partial and Failure degree parameters — inferred from canonical degree-framework; requires atomization-level confirmation only.

### §1.3 Implementation-unit breakdown

Unit 1: Entry-commit UX (player-facing).
- Target selection from currently-perceivable configurations at character's TS band.
- Operation-sequence builder: ordered list up to (Focus − 1) operations.
- Pre-declared exit-condition selector.
- Leap Roll resolution display (canonical Pool / TN / Ob / degree).
- Commit-lock confirmation; warning that mid-contact modification is unavailable.

Unit 2: Contact-phase execution (system-facing, player reads).
- Sequence-operation resolver iterating through declared operations.
- Fatigue accumulator with threshold monitoring.
- Scene-clock continuance with above-water event resolution around submerged character.
- Conditional-exit evaluation at each inter-operation moment.
- Voluntary-exit input surface (single-button or menu; minimal UX footprint).

Unit 3: Sentinel action (player-facing, pre-contact).
- Scene-round pre-contact Sentinel declaration by non-submerging party member.
- +1D bonus on Sentinel's perception/awareness rolls on behalf of submerged practitioner.
- Pre-agreed signal system for interruption (canonical collective-operation pattern §2.5).

Unit 4: Retention Roll resolution.
- Degree-differentiated outcome application per §1.2 mechanical specification.
- Rendering Crisis check on Failure (Spirit TN 7 Ob = Coherence-loss magnitude).
- Fractured Fallout roll trigger on Crisis failure per canonical §3.6.

Unit 5: Knot registration (system-facing, bookkeeping).
- Per-operation knot creation per canon/02 Am 6.
- Knot parameters (operation type, target, formation context) stored to knot-profile.
- Notification to player (not to character — reflexive access unavailable).

### §1.4 Cross-proposal dependencies

- P5 (per-band Coherence phenomenology, Wave 2): Retention-degree Coherence effects consume P5 band-transition logic.
- P6 (four-factor Coherence recovery, Wave 3): Protection-window mechanic defined in P1 consumed by P6 recovery formula.
- P15 (knot-profile layers, Wave 2): Knot registration produces entries consumed by P15 UX.
- P3 (four-faction interpreter, Wave 1): Retention aftermath observed by faction NPCs; dialogue per P3 frames.

Wave 1 internal dependency: P1 produces the Leap event that P3, P9, P10, P21 all reference. P1 should commit first within Wave 1.

### §1.5 Verification criteria

Implementation of P1 is verified complete when:
1. Canonical Leap Roll (Pool / TN / Ob / degree) produces canonically-correct outcomes.
2. Entry-commit locks operation sequence; mid-contact modification surface is structurally unavailable (tested by attempting modification, which should be rejected).
3. Above-water scene continuance during contact produces scene-state events that reach the character on re-arrival (tested by scripted NPC-action during contact).
4. Retention Roll degree-differentiation produces distinct Coherence-outcome and Rendering-Crisis-check outcomes (tested across all four degrees).
5. Knot registration produces knot-profile entries with canonical operation-type + target + formation-context parameters.
6. Sentinel action produces canonical +1D bonus and interruption-pathway with Partial retention degree outcome.

---

## §2 P3 Workplan — Four-Faction Interpreter Machinery

### §2.1 Canonical anchors

- canon/00 §9: Perceptual Prophylaxis formation-structural.
- canon/00 §10: Epistemological Barrier.
- canon/02 Am 5: Church conflation as structural category-identification error.
- T-27 (existing canon throughline): effects real, explanations wrong.
- T-29 (existing canon throughline): Baralta partial prophylaxis-crack.

### §2.2 Pre-implementation decisions required

Blockers:
- `[DECISION P3-1]` Frame-crack-points threshold (5 proposed). Requires calibration-check against expected Baralta-community residence durations across campaign scenarios.
- `[DECISION P3-2]` Forced-attention interaction cost to NPC. Proposal: social-trust cost (NPC registers forced attention as aggressive frame-intrusion). Requires editorial confirmation.
- `[DECISION P3-3]` Cross-faction event log UI surface: four-panel simultaneous, sequential navigation, hybrid. Proposal: hybrid (simultaneous-four-summary + sequential-deep-read). Requires editorial confirmation.

Non-blockers:
- Faction taxonomy per-category vocabulary (Church miracle / demonic / saintly / heretical / divine; Varfell pragmatic-operational; Baralta direct-communion + substrate-adjacent; RM Einhir-heritage). Atomization-level detail only.
- Observer-receptive-capacity gating logic. Mechanical surface; derived from canonical §9 Prophylaxis + TS band reception-threshold.

### §2.3 Implementation-unit breakdown

Unit 1: Faction-AI modules (four).
- Church interpreter: receives event content; applies Church-taxonomy; produces Church-framed output.
- Varfell interpreter: pragmatic-operational taxonomy.
- Baralta interpreter: direct-communion + partial prophylaxis-crack taxonomy.
- RM interpreter: Einhir-heritage + historical-lineage taxonomy.

Unit 2: Receptive-capacity gating.
- Pre-interpreter filter: TS band + formation determines what content enters observer's receptive capacity.
- Non-sensitive observers (low TS + canon §9 Prophylaxis) receive nothing; dialogue continues pre-event content without modification (attention-architectural absence).
- Sensitive observers receive content at TS-band capacity; interpreter-module processes received content.

Unit 3: Dialogue-generator constraint.
- Framework-level conversion rejected at dialogue-tree layer (no branch produces frame-shift).
- Within-frame assessment-shifts permitted (same taxonomy, different specific judgment).
- Frame-crack accumulation: Baralta-community residence, Einhir substrate-adjacency produce frame-crack-points; threshold 5 proposed.

Unit 4: Forced-attention interaction.
- Player-directed NPC attention to substrate event.
- Partial receipt; frame-integration fails; receipt dissolves.
- NPC social-trust decrement per `[DECISION P3-2]`.

Unit 5: Cross-faction event log.
- Simultaneous four-faction interpretation rendering at substrate-event scenes.
- Player-with-framework-access view: substrate reality + four frame-processed accounts.
- UI surface per `[DECISION P3-3]`.

Unit 6: High-TS diagnostic-observation register.
- At practitioner TS 70+: character-dialogue permits recognising other-faction interpreter output as interpreter output.
- Not conversion; mutual-recognition-of-frames.

### §2.4 Cross-proposal dependencies

- P1 (Leap UX, Wave 1): Leap aftermath is substrate event observed by faction NPCs; consumes P3.
- P9 (confrontation/integration, Wave 1): Frame-crack pathways converge with confrontation-under-integrative-conditions per P9.
- P12 (Seam Text dual-mode, Wave 2): Faction taxonomies drive Church doctrinal-text generator per T-39.

Wave 1 internal: P3 depends on P1 (Leap events) but not vice versa for interpretation-machinery implementation. P3 can be developed in parallel with P1.

### §2.5 Verification criteria

Implementation verified complete when:
1. Four faction-AI modules produce frame-consistent interpretations of identical substrate-event inputs.
2. Non-sensitive low-TS NPCs produce pre-event continuity dialogue; forced attention produces partial-receipt-then-dissolve with social-trust decrement.
3. Framework-level conversion attempts at dialogue trees reject; within-frame assessment-shifts succeed.
4. Baralta-community-residence accumulates frame-crack-points; at threshold, NPC produces Baralta-frame-shift or substrate-aware register.
5. Cross-faction event log produces four simultaneous interpretations per substrate event.
6. High-TS practitioner dialogue includes diagnostic-observation register when faction NPCs are present.

---

## §3 P9 Workplan — Confrontation Moment of Choice + Integration-Supportive Conditions

### §3.1 Canonical anchors

- canon/00 §4.3: Confrontation as Constitutive Finitude — perceptual opening, not substrate engagement.
- canon/00 §14: cultivated perceptual expansion through repeated felt confrontation held rather than fled.
- canon/01 Am 2: Leap distinct from confrontation; confrontation does not require Leap.
- canon/02 Am 3: operation-type alignment; confrontation is not an operation.

### §3.2 Pre-implementation decisions required

Blockers:
- `[DECISION P9-1]` Hold vs Turn-Away terminology confirmation per canon §14.
- `[DECISION P9-2]` TS progress-point threshold (10 proposed). Requires calibration against expected campaign-operation rate.
- `[DECISION P9-3]` Framework-PTSD-analog flag cap. Proposal: no cap per canon §14 binary-choice framing.
- `[DECISION P10-1]` Contemplative-crisis Ob derivation. Proposal: scaled by (practice_sessions − beach_scenes) per season.

Non-blockers:
- Integration-supportive conditions Ob-reduction modifiers (per trusted companion, per ART-qualifying site, per skilled mentor, per safe-return context; each −1 Ob; floor 1).
- Integration-supportive activities residue-reduction rates (one flag per activity: contemplative retreat one week, ritual participation, skilled-mentor conversation, community-witness scene, Seam Text composition per P12).

### §3.3 Implementation-unit breakdown

Unit 1: Confrontation event trigger.
- Scene-engine detection: excess-being at moderate+ amplitude; monstrosity at any amplitude; Gap or Locked-Zone traversal; post-First-Leap framework-truth exposure; threadcut encounter above TS band.
- Amplitude tier determination per site substrate character parameter.

Unit 2: Hold vs Turn-Away UX.
- Moment-of-choice prompt at trigger event.
- No time-pressure display; interruptive interaction.
- Player choice commits to one binary arm.

Unit 3: Hold resolution check.
- Spirit TN 7 Ob = 1 + amplitude tier.
- Integration-supportive-conditions modifiers (−1 Ob each; floor 1).
- Degree-differentiated outcome with TS progress + residue flag application.

Unit 4: Turn-Away resolution.
- No roll; fragmentary residue flag; no TS progress for this event.

Unit 5: Framework-PTSD-analog state.
- Residue-flag tracking on character sheet.
- Intrusive-content generation at rest scenes (scales with flag count).
- Somatic-reactivity +1 Ob on social rolls in contexts resembling un-integrated events.
- No TS progress until flags clear.

Unit 6: Integration-supportive activities.
- Contemplative retreat, ritual participation, skilled-mentor conversation, community-witness scene, Seam Text composition.
- Each reduces one residue flag per application.
- Season-bound availability (one retreat per season; ritual per faction appropriate frequency; etc.).

Unit 7: TS progress-point system.
- 10 progress points = +1 TS per canonical Overwhelming Leap +1 analog.
- Points accumulate across Hold-under-support events.
- Threshold-crossing (TS 30, 50, 70, 90) triggers Event Scene.

### §3.4 Cross-proposal dependencies

- P1 (Leap, Wave 1): Post-First-Leap exposure is one confrontation trigger.
- P10 (contemplative practice, Wave 1): Function 3 integration practice consumes P9 integration-supportive activity mechanics.
- P21 (map-UI, Wave 1): Threshold-crossing Event Scenes activate overlay layers.
- Environmental-quality three-composite (Wave 1 prerequisite): site restorative quality determines integration-supportive-condition availability.

Wave 1 internal: P9 depends on P1 for Leap-consequence integration. P9 can develop in parallel with P1.

### §3.5 Verification criteria

Implementation verified complete when:
1. Confrontation triggers fire at canonically-specified conditions (amplitude, encounter type, scene-context).
2. Hold vs Turn-Away prompt interrupts play without time-pressure display.
3. Hold resolution check applies correct Ob modifiers per integration-supportive conditions present.
4. Degree-differentiated outcomes produce correct TS progress + residue flag combinations.
5. Framework-PTSD-analog state produces intrusive content and social-roll modifiers as specified.
6. Integration-supportive activities reduce residue flags at specified rates.
7. TS progress-point accumulation crosses band thresholds at correct accumulations; Event Scenes fire.

---

## §4 P10 Workplan — Contemplative Practice Mechanical Surface

### §4.1 Canonical anchors

- canon/00 §14: cultivated perceptual expansion.
- canon/00 §10.2: inner-tradition Scripture as gesturing register.
- threadwork_v30 §2.3: *"Meditation reduces [Thread Fatigue] by Spirit score."*
- canon/02 Am 6: knot-profile seismographic awareness.
- ED-738 cartographic-contemplative lineage specification.

### §4.2 Pre-implementation decisions required

Blockers:
- `[DECISION P10-1]` Contemplative-crisis Ob derivation (shared with P9 §3.2).

Non-blockers:
- Function-1 bonus magnitudes (+1 confrontation-retention bonus per practice; cap 5). Derived from canonical History-bonus pattern.
- Function-2 beach-infrastructure rate (consumed by P6 four-factor recovery). Defined in P6.
- Function-4 Seam Text composition mechanics (consumed by P12). Defined in P12.

### §4.3 Implementation-unit breakdown

Unit 1: Function 1 — TS-developmental accelerator.
- Meditation scene-action: Thread Fatigue −Spirit per canonical.
- Confrontation-retention bonus point: +1 per session, cap 5; spent on next Hold Resolution as −1 Ob.
- Knot-profile signal-clarity post-practice window: one scene at +1 to any Am 6 seismographic perception.
- Ambient narrative-self reduction: one scene post-practice at reduced inner-monologue generation.

Unit 2: Function 2 — Beach-infrastructure Coherence recovery.
- Canonical §3.5 recovery pathway (full season non-practice +1 Coherence).
- Extended: Anchoring Scene via Close Knot (canonical Bonds TN 7 Ob 2 +1 Coherence); late-campaign Einhir-technique +1 Coherence.
- Site restorative quality composite (consolidated parameter) modulates recovery rate via P6 formula.

Unit 3: Function 3 — Integration practice.
- Per P9 Unit 6 activities: contemplative retreat, ritual, skilled-mentor conversation, community-witness, Seam Text composition.
- Each reduces one residue flag.
- Season-bound frequencies.

Unit 4: Function 4 — Expressive practice.
- Seam Text composition scene (per P12).
- One residue flag reduction per composition.
- Requires Coherence 4+, non-hostile environment, recent Leap.

Unit 5: Contemplative-crisis category.
- Detection: >= 3 practice sessions per season without >= 1 beach-infrastructure scene.
- Crisis check at season end: Spirit TN 7 Ob = (practice_sessions − beach_scenes).
- On failure: Coherence −1, residue flag +1. On success: no effect.
- Dark-night-analog narrative framing.

Unit 6: Faction-alignment access differentiation.
- Warden tradition: native access to all functions; chapter-house high-ART-quality.
- Baralta: direct-communion access; alternative tradition but similar mechanical access.
- Edeyja: ritual-tradition access; lineage-based.
- Church-formed: structural handicap; Church cathedrals ART-fail for contemplatively-oriented work; seeking non-Church practice triggers T-29 Baralta-crack dynamic.
- RM: pending canonisation.

### §4.4 Cross-proposal dependencies

- P9 (Wave 1): Function 3 IS integration practice.
- P6 (Wave 3): Function 2 feeds recovery formula.
- P12 (Wave 2): Function 4 feeds Seam Text mechanics.
- Environmental-quality three-composite (Wave 1 prerequisite): site restorative quality determines function-2 viability per site.

Wave 1 internal: P10 depends on P9 residue-flag mechanics. P10 commits after P9 for clean dependency.

### §4.5 Verification criteria

Implementation verified complete when:
1. Function 1: meditation session produces canonical Fatigue recovery + bonus-point accumulation + signal-clarity window + narrative-self reduction.
2. Function 2: canonical recovery pathways produce +1 Coherence per season.
3. Function 3: integration activities reduce residue flags at specified rates.
4. Function 4: Seam Text composition reduces residue + produces artifact.
5. Contemplative-crisis check fires at over-practice + under-beach conditions; produces Coherence/flag outcomes on failure.
6. Faction-alignment access differentiation: Church-formed characters produce structural-handicap outcomes at Church cathedrals vs non-Church sites.

---

## §5 P21 Workplan — Map-UI TS-Keyed Overlay Layers

### §5.1 Canonical anchors

- canon/01 Am 3: TS as receptive-capacity measure of below-waterline Thread-substrate.
- threadwork_v30 §2.3: Thread Operation Visibility table.
- threadwork_v30 §5.6: Thread Revelation Curve.
- threadwork_v30 §6.2: Observer-Dependent Rendering.
- T-02: Rendering Is Consciousness-Performed (existing canon throughline — P21 is T-02 implementation at UI layer).
- T-40: TS as Taxonomic Expansion.

### §5.2 Pre-implementation decisions required

Non-Wave-1 blockers (but relevant for scope):
- `[DECISION P21-1]` Knot-connection visual language: node-link overlay, glow-connection, partial-opacity layering. Proposal: partial-opacity layering.
- `[DECISION P21-2]` Replay-at-higher-TS scope: full, scoped, minimal. Proposal: scoped (10–20 key substrate-significant sites).

Wave 1 blocker: neither of the above blocks Wave-1 overlay-layer implementation. They are Wave 5 ambitious sub-features.

Wave 1 implementation scope:
- TS-keyed overlay layers (TS 0 / 30+ / 50+ / 70+ / 90+): core Wave 1.
- Non-Euclidean rendering (knot connections between distant territories): Wave 5.
- Replay-at-higher-TS: Wave 5.

### §5.3 N-tier note (important for scoping)

P21 is T-02 implementation at UI layer per v3.1 synthesis §3 correction. It does not establish a new N-direct throughline. Editorial framing should reflect this: P21 is a T-02-implementation specification, not a standalone throughline-producing mechanic. The workplan commits to UI implementation of an existing canonical throughline.

### §5.4 Implementation-unit breakdown

Unit 1: Overlay layer data model.
- Per-region substrate-data structure: MS state, knot positions, recent thread operations (with seasonal decay), substrate topology, Accord-institution state, historical-residue.
- Data model populated at world-construction time; TS-overlay renders subset per character TS band.

Unit 2: TS-threshold layer activation.
- TS 0–29: political-geographic layer only.
- TS 30+ activation: substrate-effect legibility layer (recent operations, MS boundaries coarse resolution, known Gap locations).
- TS 50+ activation: relational thread-structure layer (knot connections, lattice traces, Einhir site-network traces).
- TS 70+ activation: structural-reality layer (full MS gradient, Accord-institution presence per P18, Locked-Zone exact boundaries).
- TS 90+ activation: full substrate topology (peninsula-wide lattice, environmental strain awareness, historical residue layering).

Unit 3: Legibility variance.
- Per-site substrate character parameter determines per-region rendering fidelity.
- Chronic Strain territories: partial legibility.
- Gap-proximate territories: illegible in substrate layers even at TS 90+.
- Locked-Zone boundaries: exact-boundary illegible.
- Askeheim approach: increasing illegibility gradient.

Unit 4: Collective-operation shared-topology UX.
- During lattice-operations per threadwork §2.5: map renders co-operating practitioners' positions, operation vectors, shared lattice structure.
- Available during collective-operation scenes; collapses back to individual view on scene end.

Unit 5: Receptive-capacity framing in UI language.
- Overlay layer activation at threshold-crossing Event Scene rendered as *the character can now perceive* rather than *the map has new content*.
- Receptive-capacity expansion per canon/01 Am 3 framing, not content-addition framing.

Deferred to Wave 5:
- Unit 6: Non-Euclidean knot-connection rendering per `[DECISION P21-1]`.
- Unit 7: Replay-at-higher-TS location-specific TS-differentiated content per `[DECISION P21-2]`.

### §5.5 Cross-proposal dependencies

- P1 (Leap, Wave 1): Leap operations produce substrate-effect data consumed by overlay layers.
- P9 (confrontation, Wave 1): Threshold-crossing Event Scenes activate overlay layers.
- P3 (faction interpreter, Wave 1): High-TS diagnostic-observation dialogue register consumes overlay-layer receptive-capacity framing.
- Environmental-quality three-composite: site substrate character parameter drives legibility variance.
- P18 (Accord substrate perception, Wave 3): TS 70+ Accord-institution visibility.
- P15 (knot-profile, Wave 2): Knot connections rendered in TS 50+ layer.

Wave 1 internal: P21 depends on P1 for Leap-operation data. P21 commits after P1, P9 within Wave 1 for clean dependency.

### §5.6 Verification criteria

Implementation verified complete when:
1. Per-region substrate-data model populated for all playable regions.
2. TS-threshold activation produces canonically-correct overlay-layer additions at TS 30, 50, 70, 90.
3. Legibility variance produces appropriate per-site fidelity (stable-MS full legibility; Gap-proximate illegible in substrate layers regardless of TS).
4. Collective-operation scenes render shared topology; collapse back on scene end.
5. UI language at threshold-crossing Event Scenes renders as receptive-capacity expansion per canonical framing.
6. Overlay-layer data updates as world-state changes (MS shifts, new operations, seasonal decay).

---

## §6 Wave 1 commit sequence

Per workplan dependencies:
1. **P1** — foundational; produces Leap events consumed by others.
2. **P3** — parallel to P1; consumed by others' observer-dialogue surfaces.
3. **P10** — depends on P9 residue mechanics; commits after P9.
4. **P9** — depends on P1 post-First-Leap exposure; commits after P1.
5. **P21** — depends on P1, P9, environmental-quality composite; commits last.

Rearranged commit order: P1 → P3 → P9 → P10 → P21.

---

## §7 Shared prerequisites

All Wave 1 workplans depend on:
- ED-738 editorial commit per v3.1 synthesis §5 editorial-ledger-action-list item 10.
- Environmental-quality three-composite parameter specification (from v3.1 synthesis §3 consolidation).
- v3.1 synthesis commit.
- T-31..T-41 throughline registry additions.
- М-7..М-11 meta-throughline registry additions.

All six prerequisite commits must precede first Wave 1 workplan commit.

---

## §8 What these workplans are not

- Not atomization-ready specifications. Each requires per-unit PP-entries with vetting blocks per PP-674, plus engineering-level specification of data structures, UI components, and integration tests.
- Not committing to specific implementation sequences within units. Unit breakdown is order-agnostic except where dependencies noted.
- Not canonical until editorial approval + safe_commit completion.
- Not final. Session 8 synthesis may produce further revisions requiring workplan updates.

---

*End Wave 1 workplans.*
