# Mechanical Implementation Proposals — Revised

**Date:** 2026-04-22
**Companion to:** `rigorous_audit_synthesis_s1_s7_v3.md`, `gameplay_assessment.md`
**Supersedes:** `mechanical_implementation_proposals.md` (prior iteration) — §1 Leap pipeline rewritten; §4 Confrontation restructured; §6 four-faction interpreter reframed; Thread-Read-as-operation removed throughout; water-metaphor audit-extensions stripped back to canonical waterline-language only (canon/01 Am 3 explicit).
**Status:** Proposal. No commits. Requires editorial decisions flagged `[DECISION]`. Values flagged `[NEW]` are first-pass derivations from canonical baselines; atomization review required per mechanic.

**Canonical baselines re-verified.**
- canon/00 §4.3 Confrontation; §9 Perceptual Prophylaxis; §10 Epistemological Barrier; §13.2 Orphaned Configurations.
- canon/01 Am 1 three layers of being-persistence; Am 2 Leap as suspension of layer 2 for access to layer 3; Am 3 Coherence = layer 2 integrity, orthogonal to TS; Am 3 explicit: *"TS measures how much of the below-waterline Thread-substrate the practitioner can perceive and deliberately operate upon"*; Am 4 Coherence 0 TS-gated outcomes.
- canon/02 Am 1 reflexive facing suspends, outward facing persists, layer 1 continues; Am 2 knots permanent, directional, at substrate depth below reflexive access threshold; Am 3 operation-type (restorative / manipulative / destructive) determines Coherence cost by alignment with substrate tendency; Am 6 knot-profile four mechanical consequences including seismographic awareness as *intelligence mechanic available at all TS levels for knotted territories only*.
- threadwork_v30 §2.3 Leap Roll, Thread Fatigue thresholds, Focus role; §2.4 operation Ob tables; §3.2 Coherence Reduction by operation type and scale (with FR surcharge exemption PP-196); §3.5 Recovery pathways; §6.2 Observer-Dependent Rendering.

**Conventions for this document.**
- *Waterline / below-waterline*: canonical per canon/01 Am 3. Used as canonical terminology, not as extended audit metaphor. *Submerged / dive / beach / diver* etc. are stripped.
- *Receptive capacity*: TS expansion is expansion of what can be received from what is given (not different givens for different observers). Four-faction interpreter dynamic operates on what was received, not on different givens.
- *Perception is continuous*: Thread-Read as distinct operation is not canonical. What §2.3 framed as Thread-Read is attentional investment within a perceptual channel the practitioner's TS band already has open — sustained attention, not a Leap operation on the substrate.
- *Two-decision Leap surface*: entry commit and exit timing are the player's mechanical decisions. Diagnosis, Declaration, Roll, Contact-execution, Retention, and Knot-registration are resolution and bookkeeping, not phases in the player-facing sense.

---

## §1 Leap Pipeline (revised) — P1 + P8

**Canonical anchors.**
- canon/02 Am 1 (reflexive facing suspends; outward facing persists; layer 1 continues)
- canon/02 Am 2 (directional knot formation below reflexive access threshold)
- canon/02 Am 3 (operation-type determines Coherence cost)
- threadwork §2.3 Leap Roll, Thread Fatigue, Focus role; §2.4 operations; §3.2 Coherence costs

**What changes from canonical.** Canonical §2.3 specifies the Leap Roll mechanic. The implementation proposal adds: (a) explicit player-facing two-decision structure, (b) above-water world-state continuation formalised as sentinel/diver geometry, (c) full operation sequence declared at entry, preserved through contact, resolved at exit.

### §1.1 Player-facing surface: two decisions

**Decision 1 — entry commit.** The practitioner commits to engaging a configuration. Perception of the configuration is already present at the practitioner's TS band (canon/01 Am 3); pre-entry information is whatever the TS band's receptive capacity yields about the target through ordinary attention, including sustained attention over time. No diagnostic action precedes commit.

At commit, the player declares:
- Target configuration (from what the practitioner perceives at their TS band).
- Operation sequence: an ordered list of up to `Focus − 1` operations (threadwork §2.3 Focus cap). Each operation has operation-type (Weaving / Pulling / Locking / Dissolution / Mending per §2.4), scale, and scope.
- Exit conditions: pre-declared triggers (e.g. "exit after first operation if Coherence cost exceeds 2"; "exit when Fatigue reaches 70% of threshold"). Conditional exits are permitted; mid-contact modification of the sequence is not (see §1.3 canonical rationale).

Commit locks the sequence. Canonical §2.3 Leap Roll resolves at commit:
- Pool: `(Spirit × 2) + History bonus + TPS` (TPS = TS ÷ 10; canonical PP-619, PP-624)
- TN: 7
- Ob: TS 30–49 = 2, TS 50+ = 1; +1 per Wound
- Degree outcomes per §2.3 Leap Roll table, unchanged.

**Decision 2 — exit timing.** During contact, the player monitors scene state (above-water scene continuance per §1.2) and character state (Fatigue, Coherence cost accumulation). Player may elect exit at any inter-operation moment — between operations in the declared sequence, or after a completed operation before the next declared one begins. Involuntary exit occurs when Fatigue reaches `Spirit × 5` threshold (canonical §2.3).

Voluntary early exit and pre-declared conditional exit resolve to Retention Roll (below). Involuntary-Fatigue exit resolves to Retention Roll at Partial or worse degree (re-arrival under structural pressure).

### §1.2 System-facing resolution: contact execution, retention, knot registration

These are not player decisions. They are consequences of the committed sequence executing.

**Contact execution.** Sequence operations resolve in declared order. Canonical §2.4 Ob tables apply per operation. Each operation produces its Coherence cost per canon/02 Am 3 and threadwork §3.2. Fatigue accumulates per §2.3:
- Leap entry (one-time): 3
- Passive sensing: 2/round
- Mending: 4/round
- Pulling: 5/round
- Locking: 7/round
- Dissolution: 10/round
- Weaving: **4/round** [NEW — parallel to Mending; canonical §2.3 table omits explicit Weaving rate, which is an identified inconsistency pending separate editorial resolution]

**Above-water world-state continuance.** Canon/02 Am 1: outward facing persists; practitioner remains locatable to external observers during contact. Mechanical expression: the scene-clock runs during contact. NPC actions, environmental events, allied responses resolve per scene-rules. Character body is not absent from the scene; the reflexive facing is suspended, which means the practitioner's reflexive access to scene-events is suspended, not their physical presence.

The player, as external to the character's reflexive self-rendering, retains scene-level awareness (T-30). Above-water scene events are visible to player. Character is not perceiving them in the reflexive mode that would yield decision-relevant awareness.

If above-water scene-events affect character body during contact:
- Attacks on character body: character at Ob penalty on defense roll equivalent to prone/surprised state per canonical combat-rules `[DECISION P1-1: which specific canonical modifier]`. Cannot dodge, parry, or react.
- Non-combat scene-rounds pass without character participation.

**Sentinel action (pre-contact).** Any non-Leaping party member may take the Sentinel action at the scene-round preceding practitioner's Leap entry. Sentinel maintains above-water awareness on behalf of submerged practitioner:
- +1D to Sentinel's perception/awareness rolls on behalf of practitioner [NEW — parallels canonical collective operation pattern in §2.5].
- Sentinel can interrupt contact via pre-agreed signal (sound, physical contact). Interruption forces Retention Roll immediately at Partial degree.
- Sentinel cannot declare operations on the practitioner's behalf; practitioner's sequence commit persists.

**Retention Roll.** Resolves exit. Degree-differentiated per §2.3 Leap Roll table applied to reintegration:
- Overwhelming: smooth reintegration. No additional Coherence cost beyond operation-sequence costs. Reduces next Leap Ob by 1 (canonical).
- Success: standard reintegration. Canonical operation-sequence costs apply.
- Partial: stuttering reintegration. +2 Composure strain. Coherence −1 additional beyond operation-sequence costs. [NEW — parallels threadwork §2.4 Partial operation Coherence cost of −1.]
- Failure: fragmented reintegration. Coherence −2 additional. Rendering Crisis check (Spirit TN 7, Ob = magnitude of additional Coherence loss). On Crisis-check failure: Fractured Fallout roll per §3.6. [NEW derivation from canonical Fractured Fallout trigger conditions.]

**Knot registration.** Per canon/02 Am 6. Knot(s) registered to practitioner's knot-profile — one per operation executed during contact. Parameters: operation-type, target, formation context. Knot registration is automatic and bookkeeping-level; not a player decision.

### §1.3 Why the two-decision structure — canonical rationale

Canon/02 Am 1 states that reflexive facing suspends during Leap. The reflexive facing is specifically the mode of access by which the practitioner produces their own intelligibility to themselves — *I am this person, in this time, in this world*. Declaration of intent, commitment to operation-sequence, modification of commitment mid-operation — these are reflexive acts requiring the facing canon/02 Am 1 specifies is suspended.

Consequently: mid-contact re-declaration is structurally unavailable to the practitioner during Leap. The commitment-set declared at entry persists through suspension because the reflexive facing that would modify it is absent. This is why canon/02 Am 2 describes knots as forming along "the operation's channel — the path from the practitioner's own configuration to the target configuration" with the operation's intentionality bound at entry.

The full-sequence-at-entry structure preserves canon/02 Am 1 cleanly. A structure with mid-contact re-declaration would soften Am 1's commitment and require a mechanical account of how reflexive access partially reasserts during contact to permit declaration.

### §1.4 Integration points

- **Coherence system (§2, §3):** Retention-degree Coherence effects and operation-type Coherence costs per canon/02 Am 3 and threadwork §3.2.
- **Thread Fatigue:** canonical threshold, canonical rates, canonical recovery.
- **Knot-profile (§5):** canonical registration per canon/02 Am 6.
- **Environmental parameters (§8):** site substrate character parameter (consolidated composite) modifies operation Ob via existing canonical environmental modifiers.
- **Faction interpretation (§6):** observers of the practitioner's reintegration produce faction-specific interpretations of the aftermath per T-27.

### §1.5 Open decisions

- `[DECISION P1-1]` Surprise/prone modifier for attacks on character body during contact: which canonical defense-state modifier applies?
- `[DECISION P1-2]` Sentinel-bonus stacking: multiple sentinels on one submerged practitioner — bonuses stack or cap?
- `[DECISION P1-3]` Pre-declared conditional exit: how complex can triggers be? Single-variable thresholds only (Fatigue %, Coherence cost), or compound conditions (Fatigue AND Coherence)? Favor single-variable for elegance.

---

## §2 Per-Band Coherence Phenomenology — P5

Unchanged from prior iteration. Canonical §3.3 thresholds table and canon/01 Am 3 external observables preserved intact. Implementation fills in inner register, language register, observer-response register, expressive-output register per band. See prior `mechanical_implementation_proposals.md` §2 for band-by-band specifications; corrections from that iteration required only in the "Severed (1)" and "Coherence 0" subsections to ensure language consistency with receptive-capacity framing (see §7 below).

---

## §3 Coherence Recovery Four-Factor Formula — P6

Unchanged from prior iteration. Canonical §3.5 pathways preserved. Four-factor formula with site-restorative-quality composite, companion presence, protection-window status. See prior `mechanical_implementation_proposals.md` §3.

Career-residue variable remains **blocked pending Coherence career floor editorial decision** per `rigorous_audit_synthesis_s1_s7_v3.md` §3 pending-editorial-decisions.

---

## §4 Confrontation, Integration, Contemplative Practice (revised) — P7 + P9 + P10

**Canonical anchors.**
- canon/00 §4.3 Confrontation as Constitutive Finitude
- canon/00 §14 cultivated perceptual expansion through repeated felt confrontation held rather than fled
- canon/01 Am 2 Leap as distinct from confrontation; confrontation does not require Leap
- canon/02 Am 3 operation-type alignment; confrontation is not an operation

**What changes from canonical.** Canon §14 commits to confrontation as the developmental driver but leaves mechanical form unspecified. Canon §4.3 distinguishes confrontation (perceptual opening, no substrate cost) from operation (substrate engagement, differential cost). Implementation proposal: confrontation as player-facing moment-of-choice that is *not a Leap*, integration-supportive conditions as measurable post-event activity, contemplative practice as four-function mechanical surface.

### §4.1 Confrontation event structure (revised)

**Trigger conditions.** Character encounter with one of:
- Excess-being at moderate-or-higher amplitude (per §8 site substrate character parameter).
- Monstrosity encounter at any amplitude sufficient to rendering-pressure.
- Gap-proximate or Locked-Zone-boundary traversal.
- Post-First-Leap exposure to framework-truth content exceeding current interpretive-frame (canonical Thread Revelation Curve §5.6 accelerator events).
- Threadcut being encounter above practitioner's TS band's passive-recognition threshold.

Not every substrate-adjacent scene is a confrontation event. Confrontation requires amplitude threshold per site-parameter, or narrative designation (key story-moment).

**Moment-of-choice interaction.** Player prompt: **Hold** or **Turn-Away**.

Pre-correction note: the prior iteration framed this as "Hold vs Flee." *Flee* implies tactical withdrawal, which is a combat-action category — distinct from the phenomenological act canon §14 names. Canon §14's actual distinction is between *remaining in what one is seeing* and *turning away from it*. Turn-away is not cowardice in combat-terms; it is the refusal to receive what the encounter presents. Relabel accordingly.

No time-pressure display (stat-watching trap). The interaction interrupts play.

**Hold outcomes.**
- Resolution check: Spirit TN 7, Ob = 1 + amplitude tier (moderate 0, severe +1, extreme +2). Integration-supportive-conditions modifiers apply (see §4.2).
- Overwhelming: full integration. +1 TS immediate. No residue.
- Success: standard integration. +1 TS progress point (see §4.3). No residue.
- Partial: partial integration. +1 progress point. One residue flag.
- Failure: held without integration. No progress. Two residue flags. Framework-PTSD-analog state entered (§4.4).

**Turn-away outcomes.** No roll. Character refuses the encounter. Fragmentary residue marker applied (one flag). Confrontation cannot yield TS for this event regardless of subsequent action.

Confrontation is *not* a Leap. No reflexive suspension. No knot formation. No Coherence cost from the confrontation itself. Canon §4.3 is explicit on this pivot: confrontation is perceptual opening without substrate engagement.

### §4.2 Integration-supportive conditions (unchanged)

See prior iteration. Ob-reduction modifiers for Hold Resolution per trusted companion, ART-qualifying site, skilled mentor, safe-return context. Activities for post-Hold residue reduction per prior §4.2.

### §4.3 TS progress system (unchanged)

Per canonical 0–100 integer range. 10 progress points = +1 TS. Threshold-crossing Event Scenes at TS 30, 50, 70, 90.

**Correction from prior iteration:** threshold-crossings trigger what canon/00 §14 describes as *expansion of receptive capacity*. The iceberg's waterline on the practitioner's side lowers, bringing more of the substrate-iceberg into what can be received through the practitioner's ordinary perception. Not: the substrate iceberg grows, or different observers encounter different givens. This is a canon/01 Am 3 specification: TS as *how much the practitioner can receive*, not what is given to them specifically.

Taxonomic expansion (T-40) and map-UI overlay layers (§8 P21) are surface-manifestations of this receptive-capacity expansion. The map's substrate layers were always there in what-is-given; the practitioner's TS band previously lacked the receptive capacity to read them.

### §4.4 Framework-PTSD-analog state (unchanged)

Per prior iteration. Residue flag tracking; intrusive content; somatic-reactivity triggers; no TS progress until flags cleared.

### §4.5 Contemplative practice four functions (unchanged)

Per prior iteration. Function 1 TS-developmental accelerator; Function 2 beach-infrastructure Coherence recovery; Function 3 integration practice; Function 4 expressive practice.

### §4.6 Open decisions (corrected set)

- `[DECISION P9-1]` Hold vs Turn-Away terminology: Turn-Away preferred over Flee per canon §14. Confirm.
- `[DECISION P9-2]` TS progress point threshold: 10 proposed. Requires calibration check against expected campaign-operation rate.
- `[DECISION P9-3]` Framework-PTSD-analog flag cap: favor no cap per canon §14 binary-choice framing.
- `[DECISION P10-1]` Contemplative-crisis Ob derivation: scaled by (practice_sessions − beach_scenes) proposed.

---

## §5 Knot-Profile Layers — P15

Unchanged from prior iteration in mechanical surface. Clarifications:

- Layer 1 (diagnostic panel, player-facing). Per canon/02 Am 2, knots lodge below reflexive-access threshold; the character cannot introspect them. The player, external to the character's reflexive self-rendering, holds this information on the character's behalf. Not a canon violation; the player is not a mode of the character's self-rendering.
- Layer 2 (ambient somatic, character-facing). Per canon/02 Am 6 canonical seismographic awareness: *intelligence mechanic available at all TS levels for knotted territories only, no dice roll*. This is the cross-threshold channel for what reflexive self-rendering cannot access.
- Layer 3 (enhanced substrate perception in knotted territories) — held for gameplay-contribution prototype test per prior iteration. Unchanged.

T-36 load-bearing extensions per canon/01 Am 4 relational-persistence outcome. Unchanged.

### §5.1 Receptive-capacity clarification (new)

The knot-profile mechanical surface is not about receptive-capacity differentiation between player and character. It is about canon/02 Am 2's structural claim: reflexive self-rendering specifically cannot reach substrate-depth knot formations, regardless of TS-band waterline. At TS 90+, the practitioner's waterline lowers substantially, but the reflexive-access threshold is a separate canonical floor. Knots lodge below it in all practitioners.

The player holding knot information on the character's behalf is mechanically coherent because the player is not operating through the character's reflexive self-rendering mode. Layer 2 somatic awareness is the canonical within-character channel. The two channels (player-external; character-somatic) are complementary, not redundant — each reaches what the other cannot.

---

## §6 Four-Faction Interpreter Machinery (revised) — P3

**Canonical anchors.**
- canon/00 §9 Perceptual Prophylaxis as formation-structural
- canon/00 §10 Epistemological Barrier
- canon/02 Am 5 Church conflation as structural category-identification error
- T-27 effects real, explanations wrong

**What changes from canonical.** Canonical T-27 grounds the structure. Implementation: faction-specific interpretation taxonomies; propositional-correction failure encoded as dialogue-system constraint.

### §6.1 Receptive-capacity vs given-content framing (corrected)

Prior iteration framing: four factions render substrate events through different interpretive frames, producing four sincere-but-divergent accounts of the same event.

Corrected framing: four factions *receive the same given* through different interpretive-frames. The substrate event is the given, identical across observers. What differs is receptive capacity and interpretive-frame processing. Church receives the event through doctrinal-taxonomy frame; Varfell through pragmatic-operational frame; Baralta through direct-communion frame with partial prophylaxis-crack; RM through Einhir-heritage frame.

The distinction matters because:
- Non-sensitive low-TS observers do not receive the event (attention-architectural absence, canon §9). Their "smooth-past" dialogue is not denial or interpretation; the event did not enter receptive capacity.
- Sensitive observers receive the event within their TS-band capacity, then process through faction-formation interpretive-frame. Different frames produce different interpretations of the received content.
- Argument at framework-level cannot convert the frame because the frame is formation-structural (canon §9), not propositional.
- Frame-shift pathways require either confrontation-under-integrative-conditions (expanding receptive capacity; shifting what is received) or Baralta-crack sustained exposure (partial prophylaxis reduction) or Einhir substrate-adjacency (receptive-capacity development).

### §6.2 Faction interpretation taxonomies (unchanged from prior iteration)

Per prior §6.1. Church / Varfell / Baralta / RM taxonomic maps and registers preserved.

### §6.3 Dialogue-generator constraint (unchanged)

Per prior §6.2. No framework-level conversion via argument; within-frame assessment-shifts permitted.

### §6.4 Non-sensitive NPC continuity (revised framing)

Prior iteration: "smooth-past dialogue" — NPCs continue pre-event conversational content without modification.

Corrected: the event did not enter the NPC's receptive capacity. Their dialogue continues not because they deny the event but because the event was not received. Attention-architectural absence, canon §9.

Forced-attention scene mechanics per prior iteration: player can direct NPC attention; NPC produces momentary-unintegrated acknowledgment; returns to prior frame. Phrasing: the forced attention elicits *partial receipt without frame-integration* — the NPC briefly registers something was there, cannot place it within their frame, and the receipt dissolves.

### §6.5 Cross-faction event logging (unchanged)

Event log renders each faction's interpretation of substrate events. Player-with-framework-access sees four interpretations alongside substrate-reality.

### §6.6 Integration points

- **TS system (§4):** high-TS threshold (70+) unlocks diagnostic-observation dialogue register where character recognises other-faction interpreter-output as interpreter-output per T-27.
- **Confrontation system (§4):** frame-crack-point accumulation through sustained Baralta-community residence or Einhir substrate-adjacency is the canonical pathway to belief-landscape shift.
- **Text system (§7 P12):** faction taxonomies drive doctrinal-text generator.

### §6.7 Open decisions

- `[DECISION P3-1]` Frame-crack-points threshold: 5 proposed. Calibration needed against expected Baralta-community residence durations.
- `[DECISION P3-2]` Forced-attention interaction cost to NPC: none versus social-trust cost versus Composure cost. Proposal: social-trust cost (NPC registers the forced attention as aggressive-intrusion at framework level).
- `[DECISION P3-3]` Cross-faction event log UI surface: four-panel simultaneous, sequential navigation, or hybrid.

---

## §7 Seam Text Dual Textual Mode — P12

Unchanged from prior iteration. Inner-tradition cartographic-contemplative grammatical features; Church doctrinal-mode grammatical features; observer response by TS-band; player-character composition as integration practice.

### §7.1 Terminology correction

Prior iteration used *dive-log register* for inner-tradition post-Leap content. Canon/01 Am 3 uses *below-waterline Thread-substrate* as the perception-territory. ED-738 specifies *cartographic contemplative* as the tonal-model register.

Revised terminology: *below-waterline cartographic register* for practitioner descriptions of substrate-content at TS-band receptive-capacity. Or, if single-word handle preferred: *cartographic register*. The practitioner describes what was received in the band during operational contact, at specificity-conditions-gated resolution.

Dive-log, submerged, surface-reassertion, diver, beach — audit-extensions of water metaphor beyond canonical waterline-language — stripped throughout.

---

## §8 Map-UI with TS-Keyed Overlay Layers — P21

Unchanged from prior iteration in overlay specification. Canon/01 Am 3 explicit on receptive-capacity framing: higher TS = more of the below-waterline substrate-iceberg receivable at ordinary perception.

### §8.1 Overlay activation as receptive-capacity expansion (revised framing)

Overlay layers activate at TS threshold crossings not because the map gains content but because the character's receptive capacity expands. The substrate layers were always present in what-is-given; the character's TS band previously lacked capacity to read them.

This framing preserves canon/01 Am 3's orthogonality commitment (TS is a receptive-capacity axis, not a given-content axis) and T-40 taxonomic-expansion through the same mechanism.

### §8.2 Other sub-specifications (unchanged)

Non-Euclidean rendering, legibility variance, collective-operation shared-topology, replay-at-higher-TS — per prior iteration.

### §8.3 N-tier note

P21 map-UI implementation falls below N-direct in the strict Renaissance-political-leadership specification (per throughlines_meta §0). P21 is T-02 implementation (rendering-is-consciousness-performed) at the UI layer, not a modeled dynamic in its own right. It is G-core from gameplay-contribution analysis but implements an existing throughline rather than establishing a new one. Editorial framing should reflect this: P21 is a T-02 implementation specification, not a standalone throughline-producing mechanic.

---

## §9 Other proposals — mechanical surface summaries (unchanged)

§9.1 P2 TS band-label rendering; §9.2 P7 monstrosity encounter; §9.3 P11 ambient narrative self; §9.4 P13 voluntary-involuntary UX; §9.5 P18 Accord substrate perception; §9.6 P17 threadcut dialogue tiers; §9.7 P19 solastalgia register; §9.8 P20 orphaned-configuration register; §9.9 P14 non-sensitive continuity.

Each per prior `mechanical_implementation_proposals.md` §9 with terminology-corrections per §7.1 above (below-waterline cartographic register; receptive-capacity framing; no dive-log-as-separate-term).

---

## §10 Implementation wave schedule (unchanged)

Per `gameplay_assessment.md` §4 wave recommendations. Wave 1 (G-core N-direct): P1, P3, P9, P10, P21-overlays. Wave 2 (G-support N-direct): P2, P4, P5, P7, P8, P12, P13. Wave 3 (commitments + storytelling): P6, P11. Wave 4 (post-editorial): P14, P16, P17, P18. Wave 5 (conditional / optional): P15 Layer 3, P21 ambitious sub-features, P22 ending content.

### §10.1 N-tier sharpening

Per throughlines_meta §0, N-direct status for Renaissance-political-leadership grounding:
- P1 Leap pipeline: passes — models practitioner-as-leader operational surface.
- P3 four-faction interpreter: passes — models faction-belief-dynamics.
- P9 confrontation/integration: passes — models leader development under pressure.
- P10 contemplative practice: passes — models religious-institutional / lay-developmental axis.
- P21 map-UI overlay: passes via T-02 implementation route, not as standalone N-direct. Editorial framing must reflect T-02-implementation status.

Remaining Wave 1 proposals are canonically-warranted and gameplay-central; all are proceed-with-editorial-decision status.

---

## §11 Open decisions consolidated (revised)

| ID | Decision | Wave | Priority |
|---|---|---|---|
| P1-1 | Surprise Ob penalty for attack on contact-character body | 1 | high |
| P1-2 | Multiple-sentinel stacking | 1 | medium |
| P1-3 | Conditional exit trigger complexity | 1 | medium |
| P5-1 | Observer-variability randomised vs deterministic | 2 | high |
| P5-2 | Band-transition Event Scene policy | 2 | medium |
| P6-1 | Coherence career floor (blocker for career residue) | — | blocker |
| P6-2 | Site restorative quality tiers vs continuous | 2 | medium |
| P6-3 | Stochastic variation display | 2 | low |
| P9-1 | Hold vs Turn-Away terminology | 1 | confirm |
| P9-2 | TS progress point threshold (10 proposed) | 1 | high |
| P9-3 | Framework-PTSD-analog flag cap | 1 | medium |
| P10-1 | Contemplative-crisis Ob derivation | 1 | medium |
| P15-1 | Layer 3 gameplay-contribution prototype test | 5 | blocker for Wave 5 |
| P22-1 | Pre-cognitive cue duration | 2 | medium |
| P22-2 | Load-share calculation for T-36 knots | 3 | medium |
| P3-1 | Frame-crack-points threshold | 1 | medium |
| P3-2 | Forced-attention interaction cost | 1 | low |
| P3-3 | Cross-faction event log UI surface | 1 | medium |
| P14-1 | Non-sensitive NPC continuity rendering | 4 | blocker for Wave 4 |
| P12-1 | Seam Text composition: free vs generator-guided | 2 | medium |
| P12-2 | TS-correlated text rendering scope | 5 | blocker for Wave 5 |
| P12-3 | Historical Seam Text corpus scope | 3 | low |
| P21-1 | Knot-connection visual language | 5 | blocker for Wave 5 |
| P21-2 | Replay-at-higher-TS scope | 5 | blocker for Wave 5 |
| P18-1 | Accord perception strength | 3 | high |
| P7-1 | Wardline material gating | 2 | medium |
| P2-1 | TS band-label naming convention | 2 | low |

---

## §12 Corrections summary

Changes from `mechanical_implementation_proposals.md` (prior iteration):

1. **§1 Leap pipeline rewritten.** Six-phase structure collapsed to two-decision player surface. Canonical rationale per canon/02 Am 1 added. Full-sequence-at-entry declaration with pre-declared conditional exits.

2. **§4 Confrontation restructured.** No "Diagnosis" phase. Confrontation is continuous-perception moment, not preparation. Hold vs Turn-Away terminology (canon §14 alignment). Canonical clarification that confrontation is not a Leap.

3. **§5 Knot-profile receptive-capacity clarification added.** Layer 1 player/character split explained as mode-of-access distinction per canon/02 Am 2, not receptive-capacity differential.

4. **§6 Four-faction interpreter reframed.** Same-given-different-received, not different-givens-per-observer. Non-sensitive continuity as attention-architectural-absence-from-receptive-capacity, not denial or ignoring.

5. **§7 Terminology correction.** Dive-log register replaced by below-waterline cartographic register. Water-metaphor audit extensions (submerged, surface-reassertion, diver, beach) stripped. Canonical waterline terminology (canon/01 Am 3 explicit) retained.

6. **§8 Map-UI reframed.** Overlay activation at TS thresholds as receptive-capacity expansion, not content-addition to the map.

7. **§10.1 N-tier sharpened.** P21 flagged as T-02 implementation rather than standalone N-direct.

8. **Thread-Read removed as separate operation throughout.** Canonical §2.3 Thread-Read description interpreted as using "Leap" loosely to mean deep engagement; attentional investment is the revised framing for what that description was pointing at. Leap operations remain the five canonical: Weaving / Pulling / Locking / Dissolution / Mending.

---

*End revised mechanical implementation proposals.*
