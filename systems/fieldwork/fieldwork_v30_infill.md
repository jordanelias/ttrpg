<!-- INFILL — prose/rationale extracted from fieldwork_v30.md -->
<!-- Skeleton: fieldwork_v30.md -->

# VALORIA — FIELDWORK SYSTEM v1.1
## Exploration / Investigation / Socializing
## Status: DESIGN — approved for commit. Review corrections: 2026-04-13 (v1.1), PP-628 (canon guard), PP-630 (three-axis Ob, Warden Emergence fix, ED-NEW harvest).
## Mode applicability: ALL (TTRPG baseline; Hybrid bridging; Board Game abstraction; Godot video game)
## Canon compliance: P-01 (inseparability — applied to Thread-Read operations, not passive discovery), P-03 (rendering = consciousness-performed), P-05 (three emergence modes — Mode 1/2 distinction added to §3.1), P-07 (Calamity = rendered-side mechanism), P-08 (epistemological barrier), P-14 (all modes express inseparability), P-15 (three-layer being-persistence)
## Cross-references: params_core.md, social_contest_v30.md, combat_design_v1.md, threadwork_redesign_v25.md, geography_design.md, calamity_radiation.md, clock_registry.md
## Review applied: fieldwork_review.md (2026-04-13). All 11 required corrections + 8 recommended additions incorporated.
## CORE PRINCIPLE: INTELLIGIBILITY GRADIENT
Combat resolves physical conflict. Social Contest resolves formal social conflict. Fieldwork resolves the character's engagement with the world outside of structured conflict — the acts of moving through space, assembling knowledge, and building relationships.
Fieldwork's organising metaphor is the **Intelligibility Gradient**. The thread-substrate is not uniformly accessible to consciousness. Near settled centres, intelligibility is dense — the world is fully given to consciousness as coherent, reliable experience. At the periphery (the Southernmost, Einhir ruins, Calamity zones), intelligibility thins. What can be perceived, understood, and related to depends on the perceiver's epistemic capacity.
The rendering itself is always total. A non-sensitive character's world is fully real — their consciousness renders completely. The gradient is in what the substrate makes available to that rendering. Thread configurations that exceed a character's epistemic capacity are not hidden from them; they are ontologically unavailable — the rendering has nothing to process.
2. **Rendering strain on deep encounter.** Encountering Thread-adjacent phenomena at depth strains the character's rendering capacity. The character's consciousness confronts configurations that approach or exceed what it can process. This is not co-movement (which requires a Thread operation per P-01) — it is the rendering's encounter with its own limits.
This is the system's philosophical claim: exploration, investigation, and socialising are acts of rendering. The character's consciousness extends into the world — not because the ground has agency (P-07), but because rendering at depth tests the relationship between finite consciousness and the substrate's constitutive structure.
## §1 DEPTH AXIS
- **Exploration depth** = how far from the settled intelligibility you have moved, physically or metaphysically.
- **Social depth** = how far past public presentation you have reached into another person's inner world.
## §2 FIELDWORK POOL
### §2.2 Core Engine Integration
**Let It Ride:** A failed fieldwork action on a specific target (a specific POI, a specific NPC, a specific evidence source) cannot be reattempted in the same scene. Circumstances must change before the character can try again — new information, new approach, passage of time, or intervention by another character. A different character may attempt the same target in the same scene. This applies per action type: failing an Examine does not prevent an Interview on the same investigation.
### §2.1 Primary Attribute by Activity
### §2.3 System Transition Rules
Fieldwork interacts with Combat, Contest, and Mass Battle. These handoff rules supplement stage11 §11.3 (Eight Handoff Rules).
**Mass Battle → Fieldwork:** Battle concludes; Zoom Out fires (stage11 §11.2). Fieldwork resumes from frozen state. Post-battle investigation of the battlefield (examining bodies, equipment, terrain) constitutes one fieldwork scene, consuming one time unit. The battle itself does not consume fieldwork time units.
### §2.4 Threadwork During Fieldwork
**Co-movement applies to all Thread operations.** Every Thread operation in this table — Weaving, Pulling, Past-Oriented Pulling (POP), Locking, Dissolution, Mending, Collective — produces co-movement per P-01 via threadwork_redesign_v25.md §3.2. The three-dimensional auto-effects (temporal, epistemic, actualized) fire for every operation performed, including when performed during fieldwork scenes. Investigative yield (table above) is additional to these auto-effects, not a substitute for them.
- **Lock forensics:** A configuration that resists Lock reveals its internal structure through the resistance pattern. A Lock Failure is itself diagnostic. A successful Lock freezes evidence for repeated examination without degradation.
- **Distance:** Thread contact requires presence at the site OR a Knot connection to the target. Knot-mediated Thread-Read: the practitioner perceives the Knotted NPC's Thread configuration remotely. Each use: +1 Knot strain (the relationship bears force from being used as an intelligence channel).
- **Breadth (Collective):** Collective Thread-Read pools practitioners' dice, extending reach to Structural scale — the deepest possible perception. This is the Einhir's capability in miniature and carries the Einhir's costs.
**One Thread operation per scene action.** Thread-Read and other Thread operations are mutually exclusive within a single action (both require active Leap contact for incompatible purposes). The practitioner chooses which operation to perform each action.
**Mending arcs as investigation.** When a Locked Zone or Gap blocks access to deeper content, Mending IS investigation. Each successful Mending reduces the barrier's severity by one step (Locked → Catastrophic → Entrenched → Standard → Micro → Closed). Each reduction reveals more Thread configuration through the thinned barrier (Thread-Read at progressively lower Ob). Evidence yield per severity reduction: +1 (first reduction, faint impressions), +2 (second/third, increasing detail), +3 (final reduction, full access). A multi-season Mending arc with investigation milestones at each reduction creates built-in campaign structure.
**Leap vulnerability at transition.** When combat interrupts a Thread-Read, the Leap vulnerability window applies only if the interruption occurs DURING the Leap (before resolution). If the Thread-Read has resolved and the interruption follows from its consequences (e.g., an actualized auto-effect alerting a hostile), the vulnerability window has closed.
### §2.5 Domain Echo from Investigation
A resolved fieldwork Finding with faction-level scope fires Domain Echo per stage11 §11.5. The GM recognises scope and announces the echo. The Domain Echo may trigger NPC arc events (Discovery Events, Loyalty shifts, clock advances, Coalition triggers). The investigator does not control which arcs fire — the consequences follow from the Finding's content and the current game state. Investigation is a cause; Domain Echo is the effect; NPC arc cascades are the consequence.
**NPC Disposition after investigation reveals their secrets:** When a Finding concerns a named NPC's hidden information, that NPC's Disposition toward the investigator shifts −2 if the NPC learns they were investigated. Exception: NPCs who wanted the truth found (e.g., Vaynard pursuing knowledge, Torben seeking legitimacy) gain Disposition +1.
### §2.6 Knot-Mediated Remote Investigation
### §2.7 Non-Sensitive Partners and Dissonance
When a non-sensitive character (TS < 10) accompanies a practitioner during Thread operations, they are exposed to co-movement consequences. Per PP-607/PP-610: Spirit check TN 7 vs Dissonance Factor (1 for brief nearby op; 2 for significant op; 3 for POP affecting their memories; 4 for extended Foundational zone exposure).
**Field team rotation:** Sustained deep investigation (Depth 3+) with repeated Thread operations erodes non-sensitive partners. Optimal strategy: rotate non-sensitive team members every 3-4 Thread-adjacent scenes. This creates a logistics dimension to investigation — the practitioner needs multiple colleagues for sustained operations.
### §2.8 Threadcut Being Social Fieldwork
Social fieldwork actions (Read, Converse, Connect) work on threadcut beings. Social interaction is rendering-level, and threadcut beings maintain a rendering through continuous Thread work. Disposition tracks apply normally.
At Disposition +3 or higher, a threadcut being may volunteer testimony about its origin, the nature of the tear, or what lies beyond the rendering boundary. This testimony is **uniquely valuable**: it is a first-person account from a being that exists in a mode alien to organic consciousness, delivered in communicable form (ontical, not ontological). Evidence tag: **Testimonial** — transmissible to non-sensitives. The epistemological barrier (P-08) does not block this pathway because the being itself performs the translation from ontological to ontical.
## §3 EXPLORATION
### §3.1 Points of Interest (POI)
Each territory contains discoverable Points of Interest categorised by Depth. POIs are the atomic unit of exploration content. A territory's POI list is fixed at game setup (TTRPG: GM prepares; BG: printed on territory cards; Godot: authored in scene data).
**POI per territory:** A territory has between 2 and 6 POIs depending on size and narrative density. Southern territories (high Proximity Rating) have more Remnants and Anomalies. Northern territories have more Resources and Secrets. Askeheim (T15) is entirely Anomaly/Breach territory.
### §3.2 Discovery Procedure
1. **Declare intent.** The character states what they are looking for (a specific type of POI, general survey, or a named objective). The GM determines which POI category is relevant and its Depth.
2. **Check perception gate.** If the character does not meet the perception prerequisite for the POI's Depth, discovery is impossible. The character perceives nothing — the POI is not hidden from them; it is ontologically unavailable to their rendering. Inform the player that nothing further is found at their current capacity. No roll wasted.
### §3.3 Movement and Time
**Exploration within a territory:** Each exploration action (one Discovery Procedure) consumes approximately one scene of in-game time. A character can make 2–3 exploration actions per season before Exposure accumulates meaningfully.
**Hybrid:** TTRPG timing applies during Personal Phase. Movement between territories during Strategic Phase is handled by BG March/movement rules.
**Board Game:** No personal movement. Territory-level exploration abstracted via Survey action (§8.1).
**Godot:** Movement is real-time or area-transition depending on scale. Each territory is a navigable map region with POI nodes. Discovery triggers when the player-character enters a POI's activation radius, subject to perception gates.
### §3.4 Rendering Strain at Depth 3+
When a character discovers a Remnant (Depth 3), Anomaly (Depth 4), or Breach (Depth 5), the encounter strains their rendering capacity. This is **not** co-movement — co-movement requires a Thread operation per P-01 (Inseparability applies to "manipulations of threads," not to passive perception). Rendering strain is the consequence of consciousness encountering configurations that approach or exceed its processing capacity, as described in the Foundations §4.1 (monstrosity as surfeit of being confronting a finite rendering).
**Thread-Read is the exception.** When a character performs a Thread-Read action (§4.5), they are in active Thread contact via perceptive Leap. This IS a Thread operation. P-01 fires: three-dimensional co-movement auto-effects apply (temporal, epistemic, actualized). Thread-Read is the only fieldwork action that produces co-movement.
**Non-sensitive characters at Depth 3+:** A non-sensitive character (TS < 10) accompanying a sensitive explorer cannot perceive Thread-adjacent POIs directly. They experience: vague unease (TS 0-9 per observation table, params_threadwork.md). They observe the sensitive character's reaction. Any Thread-level information communicated to them becomes Inert Knowledge (per P-08, stage11 §11.6). Non-sensitive characters have a compensating advantage: they generate **+0 Exposure** from encountering Depth 3+ POIs (the Church does not flag non-sensitive presence near Thread sites, because non-sensitive characters are institutionally invisible as Thread investigators). Sensitive characters present at Depth 3+ POIs generate +1 Exposure from their perceptual engagement.
## §4 INVESTIGATION
### §4.1 Evidence Track
**Resolved investigation produces a Finding.** The Finding's reliability equals its strongest constituent evidence tag. A Finding can be cited in a Contest as a complete argument — the orator references a coherent body of evidence, not individual clues. A Finding containing only Thread-verified evidence is admissible only to TS ≥ 30 audiences (and remains Inert Knowledge for non-sensitives). A Finding containing Documentary or Verified evidence alongside Thread-verified evidence uses the non-Thread tag for admissibility (the Thread-verified components are treated as supporting context, not the evidentiary foundation).
### §4.2 Investigation Actions
Each investigation action represents one scene of focused inquiry. A character can perform 1–2 investigation actions per scene. Each action is a roll.
### §4.3 Evidence Quality and the Epistemological Barrier
**Investigative asymmetry, both directions:** Sensitive characters access deeper layers but generate more Exposure and produce institutionally inadmissible evidence. Non-sensitive characters are capped at Depth 2 without social mediation but generate lower Exposure at Depth 3+ POIs (+0 vs +1) and produce universally admissible evidence. The optimal investigation team contains both.
### §4.4 Desperate Trail (Fail Forward)
- **Exposure doubles** on failed rolls (+2 base becomes +4; +1 becomes +2). The character is now pressing into places and asking questions that attract serious attention.
- **The GM introduces a complication** — a new obstacle that is itself consequential. The witness who could help is under Church surveillance. The archive is guarded by someone with their own agenda. The site is inside a territory that just changed hands. The complication is not a wall; it is a new situation that must be navigated, producing its own story.
- **Evidence progress on Partial improves to +2** (from +1). The desperation itself produces insight — every remaining action that lands, lands harder, because the investigator is now operating at the edge of what is accessible.
**Desperate Trail persists through Compromised.** If doubled Exposure triggers Compromised (scene ends, must leave territory or go to ground), the Desperate Trail state does not clear — going to ground is not a breakthrough. The character emerges from ground still on Desperate Trail. Leaving the territory resets Exposure but does not clear Desperate Trail (the investigation is still desperate). Only a successful roll on this investigation, or a new season, resets conditions.
**Design principle:** Investigation failures should never produce "nothing happens." A failed Examine reveals that the evidence has been tampered with (who tampered with it?). A failed Interview means the informant was frightened by something (what frightened them?). A failed Research discovers the relevant archive section has been removed (by whom?). Every failure is a clue about the forces working against the investigation.
### §4.5 Thread-Read as Perceptive Leap
Thread-Read is a **perceptive Leap** — the practitioner enters active Thread contact (per threadwork_redesign_v25.md Leap procedure) to perceive Thread-level configurations rather than to manipulate them.
1. Declare Thread-Read. Requires TS ≥ 30. The practitioner must not be in melee with a declared attacker.
2. **Leap.** Follow standard Leap procedure: full-round action (Priority 5 in combat time; one scene action in fieldwork time). Vulnerability window applies — the practitioner is in Thread contact and exposed.
**Three-axis Ob alignment.** Thread-Read Ob values (§1 Depth Axis: 1/2/3/5/8 for Depths 1–5) equal the threadwork three-axis Ob system at fieldwork defaults: Single Breadth (+0 Ob) and Contact/Knot Distance (+0 Ob). Standard Thread-Read against one entity at the investigator's location uses Depth Ob alone. At greater breadth (targeting multiple entities simultaneously) or at physical distance without a Knot, add Breadth Ob and Distance Ob per params_threadwork.md §Three-Axis Ob System. Knot-mediated remote Thread-Read (§2.6) sets Distance Ob = 0 because the Knot constitutes Contact-range Thread connection regardless of physical separation. (PP-630)
**Thread-Read is the only fieldwork-defined action that produces co-movement.** All other fieldwork-defined actions (Examine, Interview, Research, Surveil, Reconstruct, social actions) are rendering-level activities that do not enter Thread contact and do not trigger P-01. Weaving, Pulling, Dissolution, Locking, Mending, and other Thread operations performed during fieldwork (catalogued in §2.4) are not fieldwork-defined actions — they are Thread operations governed by threadwork_redesign_v25.md §3.2 and also produce co-movement per P-01 when performed in a fieldwork context.
### §4.6 Contested Investigation
When two parties are investigating the same question (or one party is investigating while another is concealing), the investigation becomes **contested.**
## §5 SOCIALIZING
### §5.1 Disposition Track
Every named NPC holds a **Disposition** toward each player character. Disposition measures the NPC's willingness to engage, share, and cooperate — outside of formal Contest structures.
**Disposition is asymmetric:** NPC A's Disposition toward PC B ≠ NPC A's Disposition toward PC C. Each relationship is tracked independently.
### §5.2 Social Actions (Non-Contest)
**Not all social interaction is a social action.** Unrolled conversation — where no specific outcome is sought — is roleplay. It may inform the GM's Disposition adjustments but does not require a roll. Characters sharing a meal, swapping stories, or commiserating do not need mechanical resolution. The system models purposeful social engagement, not all human contact.
**Disposition decay:** Disposition ≥ +3 decays by −1 per season if not maintained (no social action directed at this NPC). Disposition ≤ +2 is stable indefinitely. This reflects the difference between casual acquaintance (stable) and deep trust (requires ongoing investment).
**Disposition ≤ −2 recovery:** Requires a significant narrative event (gift, rescue, shared danger, public vindication) before social actions can be attempted. A character cannot talk their way out of Hostile through Charisma alone.
### §5.3 Sincerity Gate
If a character's stated Belief contradicts genuine engagement with the NPC — the character is instrumentally building trust to extract information — the GM may call a **Sincerity Check** when the player declares a Connect or Converse action.
The Sincerity Gate is not a punishment for strategic play. It is a mechanical expression of the NPC's rendering of the character's intentions. Consciousness renders other consciousnesses; people perceive bad faith. The GM should use this sparingly — only when the player's stated approach is clearly at odds with their character's Beliefs.
### §5.4 Information Gates
### §5.5 Socializing and Beliefs
When a social action aligns with or challenges a character's stated Belief, mechanical consequences apply:
- **Social action that requires betraying a Belief:** Truth pressure — GM marks potential Truth shift. Does not fire automatically; resolves at session end per accumulated pressure.
### §5.6 Knot Integration
At Disposition +5 (Bonded), the NPC becomes a Knot candidate per existing threadwork rules. Forming a Knot with a Bonded NPC follows standard Knot procedures (threadwork_redesign_v25.md §8).
### §5.7 Contest Escalation and Negotiate Boundary
**Negotiate** applies only when: (a) parties share a goal but disagree on method (not formally opposed), or (b) the outcome is not consequential enough for full Contest. If the situation meets Contest initiation conditions (social_contest_v30.md §1: "two or more parties with opposed positions AND outcome is uncertain and consequential"), the interaction is a Contest, not a Negotiate. The GM does not offer a choice — the situation's structure determines the mechanic.
When a social action fails at Disposition ≤ 0, or when the NPC has strong reason to resist, the GM may declare **escalation**. The interaction transitions from fieldwork to a formal Contest (social_contest_v30.md). This is a Register Shift (stage11 §11.2).
### §5.8 Niflhel Social Toolkit Extension
Niflhel cannot participate in Formal or Grand Contests (per social_contest_v30.md §9.7). Their fieldwork social toolkit is equally restricted:
- **Available actions:** Read, Connect, Negotiate. One-on-one only (Niflhel cannot operate in group social settings).
- **Unavailable actions:** Impress (no institutional social presence), Rumour (excluded from social networks).
## §6 EXPOSURE
Exposure tracks how much attention the character has drawn through their fieldwork activities — both physical (being seen, leaving traces) and social (asking the wrong questions, contacting the wrong people).
### §6.1 Cover (Derived Value)
### §6.2 Exposure Track
### §6.3 Exposure Sources
### §6.4 Exposure Reduction
### §6.5 Exposure and Church Attention Pool
**Cap:** A single character's Exposure contributes at most +1 AP per territory per season. Multiple characters' Exposure in the same territory stacks to a maximum of +2 AP per territory per season from fieldwork sources. This prevents fieldwork-heavy campaigns from generating unbounded TC acceleration through the AP → Heresy Investigation → TC pipeline.
## §7 DERIVED VALUES SUMMARY
## §8 BOARD GAME MODE
At Board Game scale, fieldwork is abstracted into faction-level actions using existing card types plus one new action variant.
### §8.1 New BG Action: Survey (Consul Inward variant)
**Survey** represents a faction directing resources to explore and develop a territory's hidden assets.
- **Effect on Overwhelming:** Reveal POI + gain +1 Influence (the discovery enhances the faction's knowledge base).
### §8.2 Existing Actions as Fieldwork
**No new card types.** Survey uses Consul Inward. All other fieldwork maps to existing actions. This preserves the BG action economy.
### §8.3 BG Social Interaction
## §9 HYBRID MODE
### §9.1 Hybrid Fieldwork Procedure
   - Social: NPC Disposition shifted → at high enough Disposition, NPC provides faction-level intelligence or support (Domain Echo).
### §9.2 Hybrid Fieldwork Timing
Fieldwork scenes occur during Personal Phase. If a Strategic Phase order triggers a fieldwork opportunity (e.g., a Tribune Investigate reveals something that demands personal follow-up), the GM may grant a bonus Personal Phase scene for the follow-up. This bonus scene does not extend the seasonal cap — it replaces one of the standard 2–3 Personal Phase scenes.
## §10 GODOT VIDEO GAME IMPLEMENTATION
### §10.1 Exploration Map Architecture
Each territory is a navigable area containing POI nodes. POI nodes exist in the scene tree at authoring time but are conditionally visible based on the player-character's perception gates.
**Perception gate implementation:** Each POI node has an `is_perceivable(character)` method that checks the character's TS, Cognition, Truth, and relevant Histories against the POI's depth requirements. POI nodes that fail the perception check are not rendered — they do not exist in the character's world.
**Conditional POI gates:** POIs gated by RS band, season, faction control, or prior discovery are evaluated dynamically. A Remnant that becomes perceivable when RS drops below 60 appears in-world at the moment RS crosses the threshold — the world changes because the substrate's intelligibility has changed.
### §10.2 Intelligibility Gradient Visualisation
The Intelligibility Gradient is the system's signature visual feature. The Godot implementation makes the character's rendering capacity visible — not as a filter over a single objective world, but as the character's genuine experiential reality.
**There is no neutral visual layer.** The Thread configuration constitutes a different experiential reality depending on how the observer's consciousness renders it. The Godot implementation uses different visual presentations for different characters, but this is not a "filter" — each visual is the world as that character genuinely inhabits it. The relationship between rendering and world is constitution/experience (Foundations §3.1), not appearance/reality.
The same POI constitutes a different world for characters at different Truth values. This is not interpretation or opinion — it is the world as given to that consciousness:
- **Truth 5 (Orthodox):** Thread phenomena constitute a world where demonic intrusion is real. The visual language uses Church iconography — hellfire palette, sin-associated imagery. The character's rendering genuinely produces this world.
- **Truth 3 (Questioning):** Thread phenomena constitute an ambiguous world. Undefined shimmer, neutral colour shifts. The character's rendering is uncertain — the world itself is uncertain.
- **Truth 0 (Accepted):** Thread phenomena constitute a world where the substrate is natural. Calm, structural, the fabric of reality experienced directly. Beauty rather than horror.
### §10.3 Investigation Journal System
**Inert Knowledge UI:** When a non-sensitive character receives Thread-verified evidence, the journal displays it with a distinctive visual treatment — grayed out, slightly blurred, with a tooltip: "Your character knows this was said, but cannot fully grasp its implications." The player can *read* the information (maintaining player agency) but the character cannot act on it mechanically (maintaining the epistemological barrier).
### §10.4 Disposition and Dialogue
**Dialogue option gating:** Conversation options are filtered by current Disposition + character attributes. A Bond-focused dialogue option requiring Disposition +3 simply does not appear at Disposition +1. The player sees what their character could plausibly say in this relationship.
**NPC memory:** NPCs remember prior interactions. A failed social action at Disposition −1 that drops Disposition to −2 should be reflected in dialogue — the NPC references the prior misstep. This is not mechanical complexity; it is authored content gated by state.
### §10.5 Dice Visualisation
Net successes displayed prominently. Degree announced with audio cue and screen flash (Failure: dull red; Partial: amber; Success: blue; Overwhelming: gold pulse).
### §10.6 Season and Clock Integration
- Each season has a budget of 4–6 time units (configurable; represents the available daylight/travel time).
## §11 THREE-MODE SUMMARY TABLE
## §12 OPEN ITEMS AND EDITORIAL FLAGS
### New editorial items
### Items resolved by PP-580 extended threadwork simulation (2026-04-13)
### Items resolved by PP-579 ontological correction (2026-04-13)
### Items resolved by PP-578 threadwork transition simulation (2026-04-13)
### Items resolved by PP-577 transition simulation (2026-04-13)
### Items resolved by PP-576 audit (2026-04-13)
### Simulation debt
### Propagation status
