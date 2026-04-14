# VALORIA — FIELDWORK SYSTEM v1.1
## Exploration / Investigation / Socializing
## Status: DESIGN — approved for commit. Review corrections applied 2026-04-13.
## Mode applicability: ALL (TTRPG baseline; Hybrid bridging; Board Game abstraction; Godot video game)
## Canon compliance: P-01 (inseparability — applied to Thread-Read operations, not passive discovery), P-03 (rendering = consciousness-performed), P-07 (Calamity = rendered-side mechanism), P-08 (epistemological barrier), P-14 (all modes express inseparability), P-15 (three-layer being-persistence)
## Cross-references: params_core.md, social_contest_system_v2.md, combat_design_v1.md, threadwork_redesign_v25.md, geography_design.md, calamity_radiation.md, clock_registry.md
## Review applied: fieldwork_review.md (2026-04-13). All 11 required corrections + 8 recommended additions incorporated.

---

## CORE PRINCIPLE: INTELLIGIBILITY GRADIENT

Combat resolves physical conflict. Social Contest resolves formal social conflict. Fieldwork resolves the character's engagement with the world outside of structured conflict — the acts of moving through space, assembling knowledge, and building relationships.

Fieldwork's organising metaphor is the **Intelligibility Gradient**. The thread-substrate is not uniformly accessible to consciousness. Near settled centres, intelligibility is dense — the world is fully given to consciousness as coherent, reliable experience. At the periphery (the Southernmost, Einhir ruins, Calamity zones), intelligibility thins. What can be perceived, understood, and related to depends on the perceiver's epistemic capacity.

The rendering itself is always total. A non-sensitive character's world is fully real — their consciousness renders completely. The gradient is in what the substrate makes available to that rendering. Thread configurations that exceed a character's epistemic capacity are not hidden from them; they are ontologically unavailable — the rendering has nothing to process.

The Intelligibility Gradient produces two mechanical consequences:

1. **Perception gates.** What a character can discover at a given depth depends on their Thread Sensitivity (TS), their Certainty, and their Coherence. Two characters standing in the same location inhabit genuinely different experiential worlds — not filtered views of one world.
2. **Rendering strain on deep encounter.** Encountering Thread-adjacent phenomena at depth strains the character's rendering capacity. The character's consciousness confronts configurations that approach or exceed what it can process. This is not co-movement (which requires a Thread operation per P-01) — it is the rendering's encounter with its own limits.

This is the system's philosophical claim: exploration, investigation, and socialising are acts of rendering. The character's consciousness extends into the world — not because the ground has agency (P-07), but because rendering at depth tests the relationship between finite consciousness and the substrate's constitutive structure.

---


---

## SUBSYSTEM FILES

This document is the skeleton core. Mode-specific and system-specific content is in separate files:

| File | Content |
|------|---------|
| `designs/fieldwork/fieldwork_exploration.md` | §3 Exploration (POI, Discovery Procedure, Movement, Rendering Strain) |
| `designs/fieldwork/fieldwork_investigation.md` | §4 Investigation (Evidence Track, Actions, Epistemological Barrier, Desperate Trail, Thread-Read, Contested) |
| `designs/fieldwork/fieldwork_socializing.md` | §5 Socializing (Disposition, Social Actions, Sincerity Gate, Information Gates, Beliefs, Knot Integration, Contest Escalation, Niflhel) |
| `designs/fieldwork/fieldwork_exposure.md` | §6 Exposure (Cover, Exposure Track, Sources, Reduction, Church Attention Pool) |
| `designs/fieldwork/fieldwork_bg.md` | §8 Board Game Mode (Survey action, Existing actions as fieldwork, BG Social Interaction) |
| `designs/fieldwork/fieldwork_hybrid.md` | §9 Hybrid Mode (Hybrid Fieldwork Procedure, Timing) |
| `designs/fieldwork/fieldwork_godot.md` | §10 Godot Implementation + §10 Validation Findings (2026-04-13) |
| `designs/fieldwork/fieldwork_summary.md` | §11 Three-Mode Summary Table |
| `designs/fieldwork/fieldwork_editorial.md` | §12 Open Items and Editorial Flags |
| `designs/fieldwork/fieldwork_rationale.md` | §13 Design Rationale Index |

---

## §1 DEPTH AXIS

All fieldwork operates on a shared **Depth Axis** — a graduated scale from fully-intelligible to epistemically inaccessible. Depth determines base Obstacle (Ob), perception prerequisites, and risk.

| Depth | Name | Content | Perception Gate | Base Ob |
|-------|------|---------|-----------------|---------|
| 0 | Surface | Common knowledge, visible terrain, public spaces, obvious landmarks | None | Auto |
| 1 | Settled | Local knowledge, institutional records, established social networks, territorial resources | Cognition ≥ 2 or local History | 1 |
| 2 | Hidden | Concealed evidence, restricted archives, private relationships, guarded locations | Cognition ≥ 3 or Attunement ≥ 3 | 2 |
| 3 | Buried | Suppressed knowledge, Einhir traces, Thread scars, faction secrets, deep personal truths | TS ≥ 10 (exploration/investigation) or Disposition +3 (social) | 3 |
| 4 | Liminal | Active Thread phenomena, Calamity boundary zones, oscillating configurations, ontological structures | TS ≥ 30 | 5 |
| 5 | Unintelligible | The rendering's edge. What exists here exceeds human rendering capacity. The character does not perceive the unintelligible ground. They perceive their rendering's dissolution — the boundary where consciousness encounters what it cannot process. | TS ≥ 50; Coherence check Ob 2 on encounter | 8 |

**Depth applies to all three fieldwork activities:**
- **Exploration depth** = how far from the settled intelligibility you have moved, physically or metaphysically.
- **Investigation depth** = how far beneath the surface of a question you have dug.
- **Social depth** = how far past public presentation you have reached into another person's inner world.

**Ob modifiers (cumulative with base Ob):**
- Hostile faction controls territory or institution: +1 Ob
- Character is foreign to territory (no relevant History): +1 Ob
- Allied faction provides support: −1 Ob
- Character is local resident with relevant History: −1 Ob
- Calamity radiation: +1 Ob per RS band below 60 at current Proximity Rating (see calamity_radiation.md)
- Active Heresy Investigation in territory: +1 Ob to investigation/social actions involving Thread-adjacent topics

Ob floor: 1 (per core engine).

---


## §2 FIELDWORK POOL

**Pool = (Primary Attribute × 2) + History bonus**

Same construction as Contest Pool (social_contest_system_v2.md §3: Primary Attribute × 2 + History bonus). History bonus = relevant History points + 3 (per params_core.md §4.1 character creation).

**[RESOLVED: ED-NEW-11 — Pool formula ×2 confirmed canonical by PP-615 (params_core.md). The doubled formula (Primary Attribute × 2) is consistent across Combat (PP-615), Contest (PP-234), and Fieldwork. Ob calibration is correct as-is.]**

TN: 7 (Standard). TN 6 (Controlled) when unhurried with preparation. TN 8 (Desperate) under duress, exhaustion, or active Calamity exposure.

**History selection:** One History per action, selected by the player, confirmed by GM. The History must be narratively defensible for the specific action (a History of "Einhir Architecture" applies to Examine at a Remnant; it does not apply to Rumour in a tavern). If no History is relevant: pool = (Primary Attribute × 2) + 3 (the base constant without History points).

### §2.2 Core Engine Integration

**Degree table:** Fieldwork uses the core engine degree table (params_core.md). Overwhelming requires net ≥ 2×Ob AND net ≥ 3 (PP-232/PP-249). At Ob 1, Overwhelming requires net ≥ 3 (not net ≥ 2).

**Let It Ride:** A failed fieldwork action on a specific target (a specific POI, a specific NPC, a specific evidence source) cannot be reattempted in the same scene. Circumstances must change before the character can try again — new information, new approach, passage of time, or intervention by another character. A different character may attempt the same target in the same scene. This applies per action type: failing an Examine does not prevent an Interview on the same investigation.

**Wounds:** Physical wounds (−1D per wound, cumulative) apply to fieldwork rolls that require physical exertion: Endurance-based exploration, Surveil. Social and cognitive fieldwork (Examine, Interview, Research, Read, Converse, Connect, Impress, Negotiate, Rumour, Reconstruct) is unaffected by physical wounds. Rattled marks (from Contest, per social_contest_system_v2.md §4 Step 6) apply +1 Ob per mark to social fieldwork actions for the remainder of the scene.

**Inspiration spend:** Before rolling any fieldwork action, a character may spend 1 Inspiration to reduce the Ob by 1 (minimum 1). This follows the same pattern as Inspiration spend for scope shift (stage11 §11.4). A character pursuing their Beliefs through fieldwork can leverage emotional conviction to press through resistance.

**Perception gates:** Gates based on TS are hard — they represent the epistemological barrier (P-08), which is metaphysical, not skill-based. A character below the TS gate cannot perceive what lies at that depth; no amount of effort or penalty will change this. Gates based on attributes (Cognition ≥ 2 for Depth 1, Cognition ≥ 3 for Depth 2) are also hard — they represent the minimum cognitive capacity to process the information. Characters below the gate cannot attempt the action. This is not a Beginner's Luck situation; the gate is about capacity, not training.

### §2.1 Primary Attribute by Activity

| Activity | Sub-type | Primary Attribute | Reasoning |
|----------|----------|-------------------|-----------|
| Exploration | Terrain / navigation | Cognition | Structural analysis, pathfinding, cartography |
| Exploration | Thread-aware | Attunement | Sensing Thread phenomena, reading the substrate |
| Exploration | Endurance-based | Endurance | Forced marches, exposure, harsh terrain |
| Investigation | Physical evidence | Cognition | Examining objects, documents, architecture, forensics |
| Investigation | Witness / informant | Attunement | Reading people, sensing deception, calibrating trust |
| Investigation | Lore / research | Recall | Archives, oral histories, institutional records, precedent |
| Investigation | Thread-Read | Attunement | Perceiving Thread-level configurations via perceptive Leap (§4.5). TS ≥ 30 required. |
| Socializing | Read | Attunement | Determining NPC's true state, hidden motivation |
| Socializing | Impress | Charisma | Making a favourable impression, projecting authority |
| Socializing | Connect | Bonds | Building genuine trust, deepening a relationship |
| Socializing | Rumour | Charisma | Gathering unverified intelligence through social networks |
| Socializing | Negotiate | Attunement | Reaching informal agreement (below Contest threshold — see §5.7) |

### §2.3 System Transition Rules

Fieldwork interacts with Combat, Contest, and Mass Battle. These handoff rules supplement stage11 §11.3 (Eight Handoff Rules).

**Fieldwork → Combat:** When hostile contact interrupts fieldwork, the current fieldwork action resolves (degree applied, Evidence/Exposure updated). Combat then begins per combat_design_v1.md §3 (initiative by Attunement). If the character was at Exposure ≥ Noticed when interrupted, the interrupting hostile party gains +1D on their first exchange Offence (positional awareness from the character's conspicuousness). Evidence gathered before the interruption is retained regardless of combat outcome.

**Fieldwork → Contest (Escalation):** Per §5.7. Current Disposition maps to Conviction Track offset (±1 per 2 Disposition, cap ±2). Evidence from fieldwork may be cited in the Contest for +2D Recall bonus (per social_contest_system_v2.md §4 Step 3). Evidence cited in a Contest is not consumed — the Evidence Track and its contents persist. The investigation continues after the Contest.

**Fieldwork → Mass Battle (Suspension):** Mass battle suspends all active fieldwork. Evidence Tracks freeze at their current value. Battle actions (including Thread operations in Phase 4) do not consume fieldwork time units. Thread-Read during mass battle: resolves in Phase 4 window, classified as intelligence (not offensive). Co-movement fires. May advance an Evidence Track if the Thread-Read targets an investigation question. Fieldwork resumes after the battle at its frozen state.

**Combat → Fieldwork:** Combat ends; fieldwork resumes as a new scene. Wounds persist (−1D to physical fieldwork per wound, per §2.2). Combat generates Exposure in the current territory: +1 for a quiet fight (subdued, no witnesses), +2 for a conspicuous fight (noise, damage, witnesses), +3 for a public battle (multiple combatants, civilian observers).

**Contest → Fieldwork:** Contest ends; fieldwork resumes. Information gained through a Contest Appraise action (social_contest_system_v2.md §4 Step 1) may be applied to an active Evidence Track as +1 progress (Partial quality, Testimonial tag). This is automatic — no additional fieldwork action required. Post-Contest Disposition update: adjudicator's Disposition shifts +1 toward the Contest winner, −1 toward the loser.

**Mass Battle → Fieldwork:** Battle concludes; Zoom Out fires (stage11 §11.2). Fieldwork resumes from frozen state. Post-battle investigation of the battlefield (examining bodies, equipment, terrain) constitutes one fieldwork scene, consuming one time unit. The battle itself does not consume fieldwork time units.

**Combined Findings in Contest:** Multiple resolved Findings on related topics may be presented as a combined argument. The combined argument uses the strongest constituent reliability tag. Each additional Finding beyond the first adds +1D to the Argue roll (max +2D from combined Findings).

### §2.4 Threadwork During Fieldwork

**Every Thread operation may advance investigation.** Per the Foundations §1, threads constitute all that is experienceable. There is no configuration excluded from Thread operations, and no Thread operation that cannot produce investigatively relevant consequences. The Evidence Track advances when an operation's consequences reveal something relevant to an active investigation, regardless of operation type. The GM determines whether the consequences yield investigation-relevant information.

**Thread Operation Investigative Yield:**

| Operation | Primary Effect | Investigative Yield | Typical Evidence Progress |
|-----------|---------------|--------------------|--------------------|
| Thread-Read | Perception of Thread configuration | Direct: the practitioner perceives what is there | +2 (Success), +3 (Overwhelming) |
| Weaving | Cohering a configuration | Co-movement may reveal adjacent structures; stabilised configs are easier to examine | +1 if co-movement reveals (GM) |
| Pulling (standard) | Opening a configuration | The pulled state reveals what was hidden, frozen, or compressed | +2 (Success), +3 (Overwhelming) |
| Past-Oriented Pulling | Displacing temporal config | The displaced past reveals what was overwritten; orphaned config is evidence | +2 (Success), +3 (Overwhelming) |
| Locking | Freezing a configuration | Preserves evidence against tampering; resistance to Lock reveals internal structure | +1 (preservation); +2 if resistance reveals structure |
| Dissolution | Destroying a configuration | Gap topology IS forensic evidence; concealment destroyed reveals hidden content; Weaver's Thread signature readable from Gap | +2 if concealment destroyed; +1 from Gap topology |
| Mending | Repairing substrate damage | Repairing a Gap reveals original configuration; Mending a Locked boundary opens access | +1 (reveals original); +2 if opens access |
| Collective | Pooled operation (any type) | Same as base type at achieved scale | Same as base type |

**Forensic applications:**

- **Dissolution forensics:** A fresh Gap's topology reflects the structure of what was dissolved. Thread-Read of the Gap (same scene, Ob 3) reveals the original configuration. Additionally, a Woven concealment dissolved by Dissolution reveals both the hidden content AND the concealer's Thread signature — triple evidence (what was hidden, who hid it, when).
- **Lock forensics:** A configuration that resists Lock reveals its internal structure through the resistance pattern. A Lock Failure is itself diagnostic. A successful Lock freezes evidence for repeated examination without degradation.
- **POP forensics:** The paradox window (PP-193) produces simultaneous perception of past and present states — the practitioner sees what changed and how. The paradox window is the investigation's most powerful perceptual moment.

**Scale, distance, and breadth:**

- **Scale** (stage11 §11.1): Higher scale = broader investigative reach, higher Ob, higher Coherence/RS cost. Territorial Thread-Read perceives an entire settlement's substrate (TS 50+, Coherence −1).
- **Distance:** Thread contact requires presence at the site OR a Knot connection to the target. Knot-mediated Thread-Read: the practitioner perceives the Knotted NPC's Thread configuration remotely. Each use: +1 Knot strain (the relationship bears force from being used as an intelligence channel).
- **Temporal reach (POP only):** Accesses past configurations. Same-session (Ob 3) is the viable investigative range. Generational (Ob 7+) is near-impossible (<0.1% success).
- **Breadth (Collective):** Collective Thread-Read pools practitioners' dice, extending reach to Structural scale — the deepest possible perception. This is the Einhir's capability in miniature and carries the Einhir's costs.

**One Thread operation per scene action.** Thread-Read and other Thread operations are mutually exclusive within a single action (both require active Leap contact for incompatible purposes). The practitioner chooses which operation to perform each action.

**Mending arcs as investigation.** When a Locked Zone or Gap blocks access to deeper content, Mending IS investigation. Each successful Mending reduces the barrier's severity by one step (Locked → Catastrophic → Entrenched → Standard → Micro → Closed). Each reduction reveals more Thread configuration through the thinned barrier (Thread-Read at progressively lower Ob). Evidence yield per severity reduction: +1 (first reduction, faint impressions), +2 (second/third, increasing detail), +3 (final reduction, full access). A multi-season Mending arc with investigation milestones at each reduction creates built-in campaign structure.

**Wounds and Thread operations:** Physical wounds do not apply −1D to Thread operation pools (Thread operations are consciousness-performed per P-03). Instead, wounds apply +1 Ob to Thread operations requiring Leap — pain disrupts concentration needed to sustain contact.

**Leap vulnerability at transition.** When combat interrupts a Thread-Read, the Leap vulnerability window applies only if the interruption occurs DURING the Leap (before resolution). If the Thread-Read has resolved and the interruption follows from its consequences (e.g., an actualized auto-effect alerting a hostile), the vulnerability window has closed.

### §2.5 Domain Echo from Investigation

A resolved fieldwork Finding with faction-level scope fires Domain Echo per stage11 §11.5. The GM recognises scope and announces the echo. The Domain Echo may trigger NPC arc events (Discovery Events, Loyalty shifts, clock advances, Coalition triggers). The investigator does not control which arcs fire — the consequences follow from the Finding's content and the current game state. Investigation is a cause; Domain Echo is the effect; NPC arc cascades are the consequence.

**NPC Disposition after investigation reveals their secrets:** When a Finding concerns a named NPC's hidden information, that NPC's Disposition toward the investigator shifts −2 if the NPC learns they were investigated. Exception: NPCs who wanted the truth found (e.g., Vaynard pursuing knowledge, Torben seeking legitimacy) gain Disposition +1.

### §2.6 Knot-Mediated Remote Investigation

A practitioner Knotted to an NPC may Thread-Read that NPC's Thread configuration remotely through the Knot connection, without physical presence. The Knot IS the connection — distance does not add Ob.

**Pool:** Standard Thread-Read pool. **TN:** 7. **Ob:** Personal scale (Ob 2).
**Cost per use:** +1 Knot strain. The relational thread bears force from being used as an intelligence channel. The Knotted party may detect the intrusion: Spirit check TN 7, Ob = practitioner's Cognition ÷ 2 (round down, min 1). If the Knotted party detects: Disposition −3 (betrayal of relational trust). The Knot itself does not break — Knots are constitutive, not contractual — but the relationship may be destroyed.

**Evidence yield:** Thread-verified. Inert Knowledge for non-sensitives. Advances Evidence Track normally.

### §2.7 Non-Sensitive Partners and Dissonance

When a non-sensitive character (TS < 10) accompanies a practitioner during Thread operations, they are exposed to co-movement consequences. Per PP-607/PP-610: Spirit check TN 7 vs Dissonance Factor (1 for brief nearby op; 2 for significant op; 3 for POP affecting their memories; 4 for extended Foundational zone exposure).

**Failure:** Spirit −1D for remainder of scene. Multiple failures in a season compound — each failure makes subsequent checks harder. Non-sensitive partners degrade over sustained Thread exposure. Recovery: penalty clears at scene end. No permanent damage.

**Field team rotation:** Sustained deep investigation (Depth 3+) with repeated Thread operations erodes non-sensitive partners. Optimal strategy: rotate non-sensitive team members every 3-4 Thread-adjacent scenes. This creates a logistics dimension to investigation — the practitioner needs multiple colleagues for sustained operations.

### §2.8 Threadcut Being Social Fieldwork

Social fieldwork actions (Read, Converse, Connect) work on threadcut beings. Social interaction is rendering-level, and threadcut beings maintain a rendering through continuous Thread work. Disposition tracks apply normally.

At Disposition +3 or higher, a threadcut being may volunteer testimony about its origin, the nature of the tear, or what lies beyond the rendering boundary. This testimony is **uniquely valuable**: it is a first-person account from a being that exists in a mode alien to organic consciousness, delivered in communicable form (ontical, not ontological). Evidence tag: **Testimonial** — transmissible to non-sensitives. The epistemological barrier (P-08) does not block this pathway because the being itself performs the translation from ontological to ontical.

**Counter-investigation:** A threadcut being perceives Thread-Reads directed at it (it is always in the originary state). It may respond with its own Thread operations: concealing its configuration, Pulling the investigator's memory, or Weaving misdirection. Contested investigation (§4.6) applies. The Evidence Track is player-level knowledge — if the being Pulls the investigator's memory of a prior Thread-Read, the Evidence Track does not reverse (the knowledge persists in notes, allies, and physical records). The character loses conscious access; the investigation's accumulated state persists.

---


## §7 DERIVED VALUES SUMMARY

| Value | Formula | Range | Parallel |
|-------|---------|-------|---------|
| Fieldwork Pool | (Primary Attribute × 2) + History bonus | Variable | Combat Pool; Argue Pool |
| Exploration Ob | Depth base + modifiers | 1–10+ | Ob scale per params_core.md |
| Investigation Threshold | GM-set (3/5/8 by scope) | 3–8 | Clock-style progress track |
| Disposition | Starting value ± social actions | −3 to +5 | Asymmetric per-NPC per-PC |
| Cover | Cognition + most relevant History | 2–14 | Composure (Cha + 6); Stamina (End + Hist + 1) |
| Exposure | 0 + accumulation vs Cover-derived thresholds | 0–10+ | Strain toward Composure threshold |

---

