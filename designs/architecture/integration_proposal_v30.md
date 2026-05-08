# VALORIA — Holistic Critique & Integration Architecture
## Synthesis of All Nine Design Documents
## Date: 2026-04-15-09-19

---

# EXECUTIVE SUMMARY

After reading all nine documents in their entirety, the diagnosis is this: Valoria has two complete, internally rigorous design layers that have never been formally bridged. The V30 documents (faction_layer, fieldwork, social_contest) describe *world physics* — how the world moves, resists, and responds. The newer documents (player_agency, investigation_systems, and the audits) describe *player physics* — how players learn what they want, discover what the world is doing, and feel consequential within it. Both halves are of exceptional quality. The gap between them is the project's central unresolved design problem.

The bridge between the two halves is built from three mechanisms: Domain Echo (personal actions producing faction consequences), the Scene Slate (faction events producing personal opportunities), and the Dialogue Lattice (the intermediate space between investigation and confrontation). All three are specified in different documents, never unified in one place, and none is formally canonical. The primary recommendation of this document is that these three mechanisms should be consolidated into a single **Transition Layer specification** that is as rigorous as the V30 documents themselves.

The second major finding: the investigation systems proposal and the player agency system were written in parallel and have not been reconciled with each other. They share vocabulary, share some mechanical concepts (Scene Slate, Beliefs, the [SINCERE]/[INSTRUMENTAL] distinction), but they weren't written as a unified architecture. Unifying them removes redundancy and closes several gaps that are currently papered over by the audits' patchwork recommendations.

The third finding: for a videogame, the most important design work remaining is not mechanical — it is presentational. The game's richness must be discoverable through play rather than front-loaded through exposition. Almost every system is well-calibrated for computation; none has been fully designed for progressive revelation to a player who has never read a design document. This document proposes a layered information architecture that introduces complexity only as the player earns the capacity to engage with it.

---

# PART 1: DOCUMENT TOPOLOGY — WHAT EACH DOCUMENT IS FOR

Understanding the documents' relationships prevents misreading any single document as complete.

## The V30 Substrate: World Physics

The three V30 documents describe what the world does when forces act upon it. They are not player-facing systems — they are the engine beneath the player's experience.

**faction_layer_v30** defines the political physics of the peninsula: five stability triggers, occupation duration rules, treaty ratification procedures, parliament vote mechanics. It answers: "If X happens at the faction level, what changes?" It is complete and detailed. Its weakness is that it operates entirely at the strategic layer — no player character appears in it anywhere. The player character's relationship to this layer is unspecified by the document itself.

**fieldwork_v30** defines the epistemic interface between a character and the world: how deep beneath a territory's surface a character can perceive, what actions produce what evidence, how exposure accumulates. It answers: "If a character does X in a territory, what do they learn, and what is the cost?" It is the most simulation-validated document in the set. Its weakness is that it is written as a mechanical specification rather than a player experience — the Depth Axis and Evidence Track are correct as designs, but the *experience* of discovering something buried (the reward, the revelation, the felt consequence) is not designed.

**social_contest_v30** defines the adversarial resolution mechanism for formal argument: exchange structure, genre/orientation system, Composure mechanics. It answers: "When two parties press their positions against each other, how does it resolve?" It is cleanly structured. Its weakness is what the RSE critique correctly identifies — 30+ seconds of cognitive processing per exchange decision creates a steep asymmetry between mechanical understanding and felt engagement.

**What V30 collectively establishes:** The world is a political system with physics. It has weights, resistances, trigger thresholds. It responds to force according to consistent rules. These rules are, taken together, a complete simulation of a peninsula in political crisis. They are not a complete description of how to *play* in that peninsula.

## The Experience Layer: Player Physics

The newer documents describe how players move through and act within the world the V30 documents define.

**valoria_how_to_play** is the most important document in the set for videogame design purposes, because it is the only document written from the player's perspective. It describes what a player does, season by season, and why. Its description of Domain Echo (§3.3) and the season loop (§2) is clearer and more player-legible than any design document. It should be treated as the target experience description — the gold standard against which design decisions are measured. Every design gap that prevents the how-to-play from being fully implemented is a critical gap.

**valoria_player_agency_system** solves the motivational problem: why does a character act? Its three-system answer (Beliefs, Duties, Scene Slate) is architecturally sound and draws from the right precedents. Its weakness is that it was written without reference to the V30 documents — it doesn't specify how Beliefs intersect with stability triggers, how Duties map to the specific action vocabulary of fieldwork_v30, or how Scene Slate generation consumes faction_layer_v30 events. It describes a motivation architecture without grounding it in the world's physics.

**valoria_investigation_systems_proposal** solves the social richness problem: how does a character interact with the world's inhabitants in ways that are investigatively and narratively rich? Its four-system architecture (NPE → Investigation Interface → Dialogue Lattice → Response Matrix) is the most intellectually ambitious system in any of the documents. Its weakness is symmetrical with the agency system: it was written without reference to faction_layer_v30's treaty and parliament mechanics, without explicit integration with the social_contest_v30 escalation procedure, and without specifying how its outputs (Conviction Wounds, Case Board entries) produce Domain Echo.

**The three audits** (RSE critique, comprehensive system audit, holistic audit) correctly identify most of the gaps between these layers and propose targeted fixes. They are essential reading but their patchwork structure — 13 proposals here, 7 there, table after table of pending decisions — obscures a simpler underlying need: a unified architecture that these documents approach from different angles without naming directly.

---

# PART 2: THE CORE TENSION AND WHY IT MATTERS FOR VIDEOGAME

Before the integration architecture, it is worth naming what makes Valoria's design challenge distinctive.

Most games at this level of complexity choose one of two approaches: they either hide their simulation from the player (Crusader Kings III's politics are deeply simulated but the player sees a social facade), or they expose their simulation directly and let the player engage with numbers (Dwarf Fortress mode). Valoria is attempting a third thing: a game where the simulation and the narrative *are the same thing* — where tracking that Haelgrund has a Conviction Wound at depth 1 of his Faith conviction IS understanding his story, where knowing that T6 has Accord 2 and Piety 3 IS knowing what the town feels like to walk through.

This is the game's most ambitious design claim, and it's partially earned. The Sincerity Gate — a single Spirit roll with 37% failure that fires when you try to befriend someone for instrumental reasons — is a perfect example of simulation and narrative being identical. The number (37% failure) is not a balance decision; it is a phenomenological claim about what genuine social connection requires. You cannot simulate sincerity by performing sincerity.

But the claim is only partially earned, because the bridge from world simulation to player narrative is incomplete. The player feels the Sincerity Gate because it fires in the moment of a social action. They do not yet feel the Parliament mechanics because those fire at a scale and distance too far from their character's experience. The integration architecture's job is to close that distance — to make the world's physics feel personal.

In a videogame specifically, this means designing *revelation moments*: the instant when the player understands that the territory they're governing is collapsing in Accord not because of a number on a screen but because of the NPCs they've watched and the conversations they've had. The mechanical truth and the narrative truth must coincide. This is harder than it sounds, and no document in the set has yet specified how it happens.

---

# PART 3: THE INTEGRATION ARCHITECTURE

The integration architecture consists of three formal mechanisms with one shared substrate.

## The Shared Substrate: The World State Model

Every system in Valoria reads from and writes to the World State Model — the totality of tracked values across all scales. This isn't new; it's what the simulation already is. But it hasn't been named as a design constraint: **every mechanic should be specifiable as a read from or write to the World State Model, with an explicit declaration of which values are read and which are written.**

This matters for videogame implementation because the World State Model IS the game state, and every system that modifies it without declaring what it modifies creates state corruption risk. The faction_layer_v30 is exemplary in this regard — it specifies exactly which stats change under each trigger. The investigation systems proposal is less rigorous — "the outcomes modify both Ledger and Genome" is a correct statement that doesn't specify which Ledger fields and which Genome fields change under which filter outcomes.

For integration purposes, the World State Model has three scales that are already named in the game:

**Personal Scale**: Character attributes, Coherence, Wounds, Exposure per territory, Disposition per NPC, Certainty, TS, active Beliefs, Standing per faction, Evidence Tracks, Case Board entries, active Duties.

**Territory Scale**: Accord, Piety, Prosperity, Fort Level, Occupation status, active investigations, NPC Genome states, Spiritual Weight.

**Peninsula Scale**: MS, CI, IP, Political Stability, faction stats (Mandate, Influence, Wealth, Military, Stability) per faction, card cooldowns, active treaties, Parliament state, Casus Belli pool.

The integration architecture is the specification of how information moves between these three scales. There are exactly two canonical directions, and they need to be treated as first-class design systems.

## Mechanism 1: Domain Echo (Personal → Territory/Peninsula)

Domain Echo is the game's most important cross-scale mechanic, and it has never been formally specified. It exists as examples in the how-to-play, implications in the agency system, and an excellent proposed table in the comprehensive audit. That table should be canonized immediately as a formal specification.

**The core principle of Domain Echo**: Personal actions that have Sufficient Scope change World State at Territory or Peninsula scale. "Sufficient Scope" is not a vague concept — it is a binary determination based on whether the action's primary consequence writes to Territory Scale or Peninsula Scale values. Actions that only write to Personal Scale values (taking a wound, losing Coherence, gaining Exposure) never have Sufficient Scope. Actions that primarily write to Territory Scale values (improving Accord through governance, damaging Piety through investigation) have Sufficient Scope at Territory level. Actions that primarily write to Peninsula Scale values (changing a faction stat, advancing a clock) have Sufficient Scope at Peninsula level.

**The magnitude calibration for videogame** needs one adjustment from the comprehensive audit's proposed table. The ±1/±2 magnitudes are correct for isolated actions. But in a videogame session where a player may complete 4–5 scene actions per session, cumulative Domain Echo can aggregate to 4–10 faction stat changes per session. The V30 documents already specify a ±2 faction stat seasonal cap. This cap IS the videogame's safeguard against Echo spam. What's needed is explicit specification that the seasonal cap applies cumulatively across all Domain Echoes from a single character — so if the player has already produced a +2 Domain Echo on faction Influence through investigation, their subsequent successful Contest doesn't produce another +2 Echo to the same stat within the same season.

**The V30 integration of Domain Echo**: The faction_layer_v30's stability triggers fire when certain conditions are met. The Agency System's Domain Echo fires when personal actions have Sufficient Scope. These are two different systems that currently have no specified interaction. The interaction should be: when a personal action produces a Domain Echo that writes to a value monitored by a V30 stability trigger, and that write crosses a trigger threshold, the stability trigger fires additionally. Example: if the player's investigation reveals evidence of Varfell's covert operations, the Domain Echo writes +1 to the player's faction's Influence. If that influence gain changes the balance of power enough to affect Stability — specifically if it accelerates Trigger 2 (unfavorable treaty terms) or Trigger 4 (major subterfuge) — those triggers fire. The Echo is the input; the trigger is the subsequent consequence. This makes personal-scale investigation feel genuinely consequential at faction scale.

## Mechanism 2: The Scene Slate (Peninsula/Territory → Personal)

The Scene Slate from the Agency System and the Investigation Interface from the Investigation Systems Proposal are describing the same mechanism from two different angles. The Agency System describes *how the Scene Slate is generated* (five priority levels, sources). The Investigation Interface describes *what the Scene Slate delivers* (a spatial scene graph with nodes). These need to be formally unified as one specification: the Scene Slate is the generation system; the Scene Graph is the delivery format; they are two phases of the same mechanism.

**The unified Scene Slate / Scene Graph specification:**

Generation (per Agency System §4.2) remains unchanged: five priority levels, evaluated in order, drawing from World State events. This is correct and needs no revision.

Delivery: every Scene Slate entry, when the player selects it, instantiates a Scene Graph — a spatial representation of the scene with 4–9 nodes organized by type (Anchor, Evidence, Drift, Access, Observation). This is the Investigation Interface's contribution. The Scene Graph specification doesn't change how Scene Slate entries are generated; it specifies what the player *enters* when they choose to pursue an entry.

**The V30 integration of Scene Slate generation**: This is the most underspecified integration in the entire system, and it's one of the most important. The faction_layer_v30 specifies five stability triggers that fire based on world events. The Agency System specifies a Priority 1 (crisis events) Scene Slate generation. These should be formally linked:

- Trigger 1 (Occupation or Territory Loss) in a territory where the player is present or adjacent → Priority 1 Scene Slate entry: a scene in the occupied/contested territory where the player witnesses the occupation's human consequences (NPC NPE generated from the displaced population, Accord crisis scene graph).
- Trigger 2 (Unfavorable Treaty Terms) affecting the player's faction → Priority 1 or Priority 2 entry depending on severity. A Capitulation-tier treaty generates Priority 1 (existential); a Minor Cession generates Priority 2 (Duty-aligned opportunity to renegotiate or gather leverage).
- Trigger 3 (Antagonistic Parliamentary Vote) against the player's faction → Priority 2 entry if player is Standing 1–2, Priority 1 entry if Standing 3+ (because Standing 3+ players have the capacity to respond through the Counselor contestation pathway).
- Trigger 4 (Major Subterfuge) against the player's faction → Priority 1 if player is the intelligence actor, Priority 2 if another character is executing it.
- Trigger 5 (Failed Military Engagement) → Priority 1 if a named NPC the player has Disposition with is attached; Priority 2 if purely strategic.

This mapping doesn't create new game mechanics — it specifies which existing events generate which Scene Slate entries, closing the gap that currently leaves a large portion of V30 world events without player-facing representation.

## Mechanism 3: The Dialogue Lattice (Personal ↔ Personal)

The Dialogue Lattice is the only mechanism that operates entirely within the Personal Scale — it mediates interaction between the player character and NPCs. It is the most novel system in the investigation proposal and the one that most directly addresses the gap the RSE critique identifies in Social Contests: "30+ seconds per exchange decision creates a steep asymmetry between mechanical understanding and felt engagement."

The Dialogue Lattice should be understood as the *pre-resolution* space. It handles the conversation that leads up to a resolution — investigation, relationship-building, understanding. The Social Contest (from social_contest_v30) handles the resolution itself — formal adversarial argument, high stakes, full mechanical engagement. The fieldwork Interview action handles the mechanically efficient middle ground — one roll, one evidence point, no decision tree needed.

The Lattice sits between Interview (too simple for rich NPC interaction) and Contest (too mechanically demanding for exploratory conversation). This is exactly the right framing, and the investigation proposal's five-filter chain correctly captures what happens in that intermediate space.

**The integration with social_contest_v30**: When a Dialogue Lattice session reaches an Escalation Trigger outcome (the player has pressed a position the NPC actively resists), the handoff to Contest should carry:

1. **Conviction state**: the NPC's current Wound count, established through the filter chain.
2. **Disposition state**: the current Disposition, which maps to Piety Track starting position (±1 per 2 Disposition points, capped at ±2 per existing fieldwork rule §2.3).
3. **Evidence pre-load**: any Case Board nodes the player has established in this scene, which can be declared as Contest Corroboration at contest setup.
4. **Momentum**: if the player gained Momentum from Belief-aligned Lattice utterances during the exploratory phase, those carry into the Contest.

This is already partially specified in fieldwork_v30 §2.3 (Fieldwork → Contest transition) and the social_contest_v30 §9.1 (Findings as contest preparation). What's missing is explicit specification that a *Dialogue Lattice session* is a form of pre-Contest fieldwork — that the Lattice outputs count as pre-loaded investigation for the Contest that follows.

**The integration with the Sincerity Gate**: The fieldwork_v30's Sincerity Gate (Spirit TN 7 Ob 1) and the investigation proposal's [SINCERE]/[INSTRUMENTAL] tagging are the same system from two angles. The tagging is the categorization; the roll is the mechanical enforcement. These should be formally unified: [SINCERE] utterances never trigger the Sincerity Gate; [INSTRUMENTAL] utterances always trigger it; [SINCERE, BELIEF-GATED] utterances never trigger it because the Belief is evidence of genuine investment. This is already largely stated but scattered across two documents — consolidating it into one rule eliminates ambiguity about whether the gate fires in specific edge cases.

---

# PART 4: THE EXPERIENCE DESIGN — PROGRESSIVE REVELATION

For a videogame, the integration architecture is necessary but not sufficient. The architecture specifies how systems connect; experience design specifies how players *encounter* those connections in a way that builds understanding rather than creating friction.

## The Information Hierarchy Problem

Across all documents, the game has a flat information hierarchy — every system is presented at full complexity. The V30 documents specify the faction layer completely from the first page; the fieldwork document introduces all six investigation actions at once; the social contest document presents the full 2×2×4 tactical space immediately. This is appropriate for design documents. It is fatal for player onboarding.

The videogame needs an information hierarchy that introduces complexity as the player demonstrates (not declares) the capacity to engage with it. The mechanism for this is already present in the game: the player's own character state limits what they can perceive and do. A character with TS 0 cannot see Thread gates in the Dialogue Lattice. A character with Certainty 5 cannot access Thread-referencing utterances. A character at Standing 1 cannot access Parliament. These gates already exist — they just haven't been formally treated as an *onboarding architecture*.

**The progressive revelation sequence for videogame:**

Stage 0 (Character Creation through first season): The player sees Personal Scale only. Attributes, Histories, Beliefs, Wounds, Disposition with starting NPCs. The faction layer exists as background information — the player is told which faction they serve, who their immediate superior is, and what their first Duty is. Nothing about clocks, parliament, territory mechanics, or faction stats is presented yet.

Stage 1 (Seasons 2–4, first year): The Scene Slate reveals its Priority 3 and 4 entries first — Belief-aligned opportunities and territorial events. Priority 1 events are held until they organically fire (the player will see their first crisis in this period). The Duty system is active. Domain Echo begins firing silently (outcomes happen, the player can observe them, but the mechanical bridge isn't explained until Stage 2).

Stage 2 (Year 2): The player is shown the connection between their personal actions and faction stat changes — the first time a Domain Echo fires as a visible event (with animation, UI notification, explanatory tooltip). The Territory Scale is now visible: Accord, Piety, Prosperity become readable on the territory map. Standing 2 is achievable in this period, which unlocks faction intelligence.

Stage 3 (Year 3+): Parliament, Treaty mechanics, and the full Peninsula Scale become visible and actionable. By this point, the player has experienced enough world events to understand why these mechanics exist — they've seen territories Revolt, they've watched factions lose influence, they've felt the clock pressure of CI advancing. The mechanics arrive in the context of already-felt experience.

This is not a tutorial system — there are no tutorial prompts. It is a *revelation architecture* where the game's information complexity matches the player's accumulated experience.

## The Three Visibility Modes

In the videogame, every World State value exists in one of three visibility modes for the player:

**Dark**: The value exists and changes but is not visible to the player. The player can only learn about it by discovering it in play. An NPC's Conviction Wound count is Dark until the player has sufficient Disposition (at Disposition +2, Appraise reveals it per comprehensive audit's Proposal RW-I). A territory's Spiritual Weight is Dark unless the player invests in Research about Church territorial history.

**Perceived**: The value is visible but its meaning is not labeled. The territory map shows Accord as a color gradient without calling it "Accord" until the player has investigated enough to name it. NPC Genomes are perceived through conversational behavior before they're named in the UI. This is the Lacuna lesson — space is information before explanation is offered.

**Named**: The value is visible with its label and mechanical definition. These are the values the player has earned the right to see by engaging with the systems that produce them. Named values are what the player's Growing Standing gives access to: at Standing 2, faction stats become Named; at Standing 3, NPC priority stacks become partially Named (the faction leader's top three priorities are visible).

This three-tier visibility system costs nothing mechanically — it's a UI/presentation decision. But it fundamentally changes how complexity lands: the player discovers richness rather than confronting it.

---

# PART 5: SPECIFIC INTEGRATION GAPS AND RESOLUTIONS

The following gaps are the most consequential integration failures across the nine documents. Each is specified with a concrete resolution.

## Gap 1: The Counselor Negotiation Output (C-1 from comprehensive audit)

**What's missing**: When a Standing 3 player wins a social contest against the faction leader about Duty assignment or faction priorities, what changes?

**The V30 connection**: faction_layer_v30 §3 (Treaty Mechanics) and §5 (Parliament) both specify how formal argument produces faction-level outcomes. A player arguing with their faction leader is a smaller-scale version of the same process — one party with authority, one party with standing, an argument about institutional priorities.

**Resolution**: A won Counselor negotiation produces a **Faction Priority Adjustment** — a one-season modification to the faction AI's Priority Stack. If the player wins (Success): the faction's Duty assignment for the following season uses Priority Level N-1 instead of N (the leader downweights the contested priority by one level for one season). Overwhelming win: the Priority Stack adjustment persists for two seasons, and the leader's Conviction in their assessed priority gains Wound 1 (they yielded to a subordinate's argument — their confidence is shaken). A lost negotiation: Duty unchanged, Disposition −1 with leader, and the leader's next Domain Action receives +1D from increased institutional confidence (the challenge was rebuffed publicly, reinforcing their authority). This makes the Counselor tier's negotiation not just dramatically interesting but mechanically consequential — winning an argument with your faction leader literally changes the faction's behavior.

## Gap 2: Occupation State + Fieldwork/Scene Generation

**What's missing**: A territory under Occupation (faction_layer_v30 §2) has different physics than a controlled or uncontrolled territory. The fieldwork system adds +1 Ob for "hostile faction controls territory" but doesn't model occupation specifically.

**The V30 connection**: An Occupied territory has stripped TCV, reduced Wealth flow, and an active Stability drain on the displaced faction. The player character may be the displaced faction's operative operating in their own occupied territory — a very specific and dramatically interesting situation.

**Resolution**: Occupied territories generate a distinct Scene Slate sub-type: Resistance Scenes. These are Priority 1 entries for any character of the displaced faction operating in an Occupied territory. The Scene Graph for a Resistance Scene always includes: one Anchor node (a local resistance figure, using NPE generation with +2 Volatility, Accord ≤ 1, displaced-faction affiliation), one Evidence node (documentation of occupation abuses or collaborative activity), one Observation node (occupying garrison's patrol pattern — if Surveil is used here, the output is schedule information per SoD-II from the comprehensive audit), and one Access node gated by displacing faction Mandate (entering the administrative building requires disguise or combat). The Resistance Check (faction_layer_v30 §2.5) can be initiated by the player from within a Resistance Scene as a free Accounting action — the personal scene IS the Resistance Check.

## Gap 3: Parliament + Personal Layer (the missing civic bridge)

**What's missing**: The Parliament mechanics (faction_layer_v30 §5) are detailed and rich but exist entirely at faction scale. There is no specified pathway by which a personal-scale player character participates in or influences Parliament.

**The V30 connection**: Parliamentary Motions are declared as Senator (Social) actions in Phase 4. A player character is a senator-equivalent when Standing ≥ 3.

**Resolution**: Standing 3+ players can declare **Parliamentary Intent** as a scene action during the Personal Phase. This is not a Domain Action (it doesn't consume a card from the faction hand) but it modifies the faction's parliamentary options. A player who successfully runs a scene that gathers Evidence against a rival faction (Evidence Track → Complex threshold) can flag that evidence for Parliamentary use — when the faction plays its Senator card for a Parliamentary Motion next season, the evidence adds +1D to the Ratification roll (Corroboration in Parliament, mirroring the Contest Corroboration mechanic). A player who successfully runs a Diplomacy scene with a neutral faction's representative produces a Positioning Roll bonus (+1D to the faction's Diplomacy pool in any Treaty initiated this season). This makes the Investigation Interface and Social Contest mechanics feel politically consequential — the player's conversations become the faction's diplomatic capital.

## Gap 4: The Resource Symmetry Question

**What's missing**: The RSE critique identifies that Fieldwork has no personal depletion resource. The comprehensive audit proposes "Acuity" as a new resource.

**The existing answer**: The Agency System's §7.4 explicitly resolves ED-547: "Scene action budget IS the fieldwork cost." This resolution is correct and should not be overridden. Introducing Acuity as an additional resource would double-penalize investigation — once through the scene action budget and once through the Acuity drain. The asymmetry the RSE critique notes is real, but it exists only *within* a scene. Once you're in a scene, there's no depletion forcing you to stop investigating.

**Resolution**: The within-scene resource for investigation is **Exposure**, not a new resource. Exposure is already personal cost — it limits how long the player can safely operate in a territory before triggering institutional response. The within-scene equivalent is the [Disturbed] node state from the comprehensive audit's SoD-I proposal: every Fieldwork action at a scene node marks that node Disturbed, which increases Exposure accumulation. A player who investigates thoroughly in one session does so at the cost of visibility. The scene action budget handles the between-scene resource limit. Exposure handles the within-scene limit. No new resource is needed, and Acuity should not be introduced. The symmetry table (Combat → Wounds/Stamina, Contest → Composure/Concentration, Thread → Coherence, Fieldwork → Scene Actions/Exposure) is complete as-is.

## Gap 5: The Dialogue Lattice Filter Chain Transparency

**What's missing**: The five-filter chain is powerful but potentially opaque. If an NPC responds with hostility, the player needs to understand which filter produced the hostility.

**The V30 connection**: NPC behavior's three-step decision procedure (Institutional Filter → Conviction Filter → Decision Fork) already routes NPC strategic behavior visibly through the faction layer. The Dialogue Lattice's five-filter chain is the personal-scale extension of this procedure.

**Resolution**: Don't expose the filter chain mechanically — expose it narratively through NPC characterization. Each filter failure has a distinct conversational register that players learn to read:

- Filter 1 failure (Information mismatch): NPC responds to their interpretation of what was said, not what was said. The response is *adjacent* to the topic — they heard something you didn't say. "That's what they always claim" in response to a factual observation reveals they've filed your utterance under their pre-existing framework.
- Filter 2 failure (Conviction engagement): NPC responds with effort. There's visible strain in the response — they're defending a position they know is under pressure. "The Church's position on this has always been clear" from a Wound-1 NPC sounds different from the same sentence from a Wound-0 NPC.
- Filter 3 failure (Disposition): NPC's response is minimal and guarded. They answer the question and immediately redirect. No volunteering, no elaboration.
- Filter 4 failure (Compromise): The offer is ignored or deflected specifically. The NPC doesn't say "no" — they respond as if the offer wasn't made.
- Filter 5 failure (Ethical framework): The response has a specific quality of rejection of your *approach* rather than your content. They disagree with how you're arguing, not what you're arguing.

These are UI/writing specifications, not new mechanics. In the videogame, they're achieved through voice acting direction and dialogue writing guidelines rather than new systems. The player learns to read these signals through accumulated experience — this is the investigation layer of the conversation itself.

## Gap 6: The NPE → Named NPC Interface

**What's missing**: The NPE generates procedural minor NPCs. The NPC Behavior system specifies 13 named NPCs with full Genome specs. How do named NPCs relate to the territory ecology the NPE generates?

**The V30 connection**: Named NPCs are always physically in territories (Haelgrund in Himmelenger, Baralta in Gransol, etc.). Their presence should affect the territory's social ecology — an NPC with Certainty 4 and high Mandate living in a territory should shift that territory's ecology weights toward their worldview.

**Resolution**: Named NPCs function as **Ecology Anchors**. Each named NPC contributes their own conviction and ethical framework to the territory's ecology weights as a fixed offset: a named NPC with Faith conviction weight 3 and Certainty 4 in a territory adds +1 to the Church-aligned worldview weight for the territory's NPE generation, regardless of that territory's baseline Piety/Accord. This means territories feel inhabited by their named NPCs — Haelgrund's presence in Himmelenger is perceptible in the population's tone before the player has discovered him specifically. When the player discovers Haelgrund and his hidden TS, the retroactive reframing of the territory's social ecology (the source of the subtle Thread-awareness in the population's conversations) is a revelation moment of the first order.

## Gap 7: The Scene Slate + Faction_Layer_V30 Recovery Mechanic

**What's missing**: faction_layer_v30 §1.3 specifies an "Institutional Consolidation" recovery path: a faction with no Stability triggers fired this season receives +1 Stability. The agency system doesn't generate any Scene Slate content for what a "clean" season feels like from the player's perspective.

**Resolution**: When a faction has a clean season (no Triggers 1–5 fired), Priority 5 (Ambient World Events) should generate a consolidation scene — not a crisis, but a moment of institutional coherence. This might be: the faction leader holds a review, an NPC officer approaches the player to acknowledge their contribution, or a territory celebration reflects stable governance. These scenes are not mechanically mandatory (they're Priority 5, the lowest priority), but they make institutional health feel tangible rather than abstract. When the player hasn't pursued any Priority 1–3 scenes in a season, Priority 5 consolidation scenes ensure the player still has something to experience — quiet competence, not just crises. This directly addresses the Robustness gap R-1 (Sparse Slate) from the comprehensive audit.

---

# PART 6: THE INVESTIGATION EXPERIENCE — SYNTHESIS ACROSS SYSTEMS

The investigation experience is the game's most distinctive contribution to the genre. No other referenced game combines the depth of the Evidence Track, the social richness of the Dialogue Lattice, and the Thread-level perception system. Getting this experience right is where the most design work remains.

## The Three Registers of Investigation

The fieldwork_v30, social_contest_v30, and investigation_systems_proposal collectively define three registers of investigation. A well-designed investigation in Valoria will use all three, at the player's pace.

**Register 1 — Physical Investigation**: Examine, Research, Surveil. These actions interact with the world as a set of facts. Evidence is physical, archival, or observed. The Case Board fills with documents, witnesses, and observed behaviors. This is the Case of the Golden Idol register — discrete facts that can be named, connected, and synthesized. The Reconstruct action is the synthesis tool. The Named Theory Synthesis (from the comprehensive audit's GI-I proposal) bifurcates Reconstruct correctly: the character's Cognition pool automates one kind of reconstruction; the player's synthesis skill executes another.

**Register 2 — Social Investigation**: The Dialogue Lattice with its five filters. NPCs as nodes in the investigation's social graph. Conviction Wounds as evidence of prior pressure on a worldview. This is the Disco Elysian register — facts that emerge from the world's inhabitants, colored by their worldview, filtered through their fear and loyalty and self-interest. The Sincerity Gate is what separates this from mere Charisma farming: genuine social investment is its own reward, instrumentalism has its own cost.

**Register 3 — Thread Investigation**: Thread-Read as perceptive Leap. The Evidence Track advancing when operations reveal investigation-relevant configurations. This is the register no other game has, and it should be experienced as genuinely different from the other two — not just harder, but categorically different in what it reveals. A Depth 4 Thread-Read doesn't reveal more facts; it reveals facts that exist at a different ontological level from what the first two registers can access. The Certainty system makes this register exclusive to characters who have moved toward Thread-awareness — it's a gate, not just a difficulty modifier.

The richest investigations in the game will weave all three registers. The Church-Thread-Lab investigation example in the investigation proposal is a perfect template: physical examination of the archive reveals documents, social investigation of the official reveals the Conviction Wound that produces the involuntary confirmation, and Thread investigation of the site reveals the substrate damage that proves what the documents only imply. Three registers, one investigation, convergent evidence that lands with full weight because all three lines agree.

## The Investigation as Narrative Engine

The comprehensive audit's Between Horizons proposal (BH-I — Theory Commitment and Evidence Reframing) is correct and important. A committed theory is not just a mechanical state — it is a narrative commitment. The player has declared what they think happened. The world then responds: evidence that corroborates or contradicts the theory is legible in a way it wasn't before, because the player has a position to test.

This is also where the Belief system and the Investigation system most deeply integrate. A Belief like "I will discover what Haelgrund is hiding from the Church" IS a committed theory in the Between Horizons sense — the player has declared a direction before they have sufficient evidence. Pursuing a Belief through investigation is effectively the same as committing to a theory and watching the evidence accumulate. When the Belief is fulfilled (Haelgrund's TS 12 confirmed through a Structural investigation), the Belief fulfillment mechanics fire (comprehensive audit §1.1 Coherence Gap C-3 resolution: the scope of the Belief determines the type of Echo). The unified experience is: Theory = Belief = Investigation Commitment = Resolution = Domain Echo. These are not four different systems; they are the same narrative arc at different levels of abstraction.

---

# PART 7: THE FACTION LAYER IN THE VIDEOGAME — WHAT THE PLAYER SEES

The RSE critique correctly identifies value proliferation as the faction layer's primary tension: 100+ tracked values are manageable for a computer, but the player must still hold enough in mind to make meaningful decisions. The solution is not to simplify the simulation — it is to design the player's window into the simulation.

## The Two-Layer Visibility Model

At any given moment, the player sees the faction layer through two layers:

**The Witnessed Layer**: What the player's character has personally observed. A Govern action the player participated in. A Parliament vote the player's investigation influenced. A battle the player character was present for. These are felt as narrative events, not statistics. The player doesn't need to know that Mandate changed by +1 because they experienced the scene that produced it.

**The Reported Layer**: What the player's faction intelligence feed delivers. This is Standing 2's unlock — the faction's intelligence summary, delivered as narrated events rather than stat changes. "Himlensendt's Censure motion passed Parliament with 8 Mandate votes to 4. Your faction's Stability declined. Baralta filed a counter-motion for rescission." The player knows what happened without having been there. They did not experience it; they were informed of it.

The gulf between Witnessed and Reported is where player agency lives. Events in the Reported layer might have been in the Witnessed layer if the player had chosen differently. The Season Slate they passed on, the scene they didn't pursue — those are now items in the intelligence report instead of memories. This makes the reporting system feel like consequence rather than tutorial.

**What the player never sees directly**: The simulation's raw values. Mandate is never shown as a number until Standing 3 (when the player earns the right to understand the faction's institutional health quantitatively). Stability is never shown as a number until the player has enough faction context to interpret it. This is not hiding information from the player — it is controlling the frame through which information is encountered.

## The Faction Layer as the Game's Clock

The how-to-play document is correct to frame the shared loss conditions as existential: "The game's existential question is always: can anyone win before everyone loses?" MS declines every year. CI advances every year. IP accumulates with every battle. Political Stability climbs with violence and descends with peace. These four clocks are always moving. The player's job is not to stop them — it is to shape the world's trajectory faster than the clocks converge on catastrophe.

In videogame terms, this means the clock information should be present but never urgent until it crosses a threshold. The persistent HUD displays the four clocks as ambient environmental information — the way weather displays temperature without demanding action. The player learns to glance at MS the way sailors glance at the sky. When a clock approaches a threshold, the visual presentation changes — not a red alert, but a shift in the world's ambient tone. The territories near the Southernmost look different at MS 40 than MS 80. The political spaces look different at CI 55 than CI 30. The game world is the clock display, and the player reads the world rather than reading numbers.

---

# PART 8: THE DOMAIN ECHO REFERENCE TABLE (Formal Specification)

This table is the single most important deliverable that does not yet exist as a canonical document. It should be committed immediately.

| Action Type | Sufficient Scope Condition | Echo Target | OW | Success | Partial | Failure |
|---|---|---|---|---|---|---|
| Investigation (Complex threshold) | Subject is named NPC or faction secrets | Faction Intelligence | +2 standing dice next Senate action on subject | +1 standing dice | Narrative update only | −1 faction Influence if cover blown |
| Investigation (Structural threshold) | Any | Faction Influence ±1, Casus Belli if relevant | ±2 Influence; CB generated | ±1 Influence | NPC arc trigger | −1 Influence (investigation compromised) |
| Social Contest (Grand, named NPC) | Named NPC in institutional role | Conviction Wound → faction stat | NPC arc trigger + faction stat −1 (opponent) | NPC Wound +1 | NPC arc update | Disposition −2; opponent faction stat +1 |
| Thread Op — Mending | Gap repaired or MS site | MS | +2 MS (existing canonical) | +1 MS | MS stable | No effect |
| Thread Op — Dissolution | Gap created | MS, IP | −1 MS; IP +1 | −1 MS | MS −1 | −2 MS (gap larger than intended) |
| Personal Combat — named NPC defeated | Faction officer eliminated | Faction Mandate | Mandate −2 + NPC arc trigger | Mandate −1 | NPC wounded: Stability −1 next season | No Echo; combat outcome only |
| Belief Fulfillment — NPC relationship | Deep Disposition change with named NPC | NPC arc trigger | Arc fires; Domain Echo per NPC arc resolution | Arc updated | Disposition shift only | Belief fails; −1 Momentum cap this season |
| Belief Fulfillment — systemic | Territory or clock affected | Per action type above | Amplified: ±2 instead of ±1 | Standard Echo | Narrative shift | Standard failure Echo |
| Duty Completion — Investigate | Evidence Track ≥ Complex on faction subject | Faction Intelligence +1 | Intelligence feeds Parliament OR Casus Belli | Intelligence shared | Player knows; faction doesn't yet | Rival faction learns the investigation occurred |
| Duty Completion — Governance | Territory Accord maintained or improved | Territory Accord | +1 Accord | Accord stable | Accord decay halted for 1 season | Accord −1 |
| Governance — sustained | 3+ consecutive seasons player-governed | Territory Accord long-term | +1 Accord permanent cap raise | +1 Accord | Accord floor raised to 1 | — |
| NPE Coalition → formal faction | NPE Stance convergence threshold reached | Piety or Accord ±1 | New minor faction actor emerges | Piety/Accord shifts | Coalition latent arc fires | — |

**Standing Modifier (comprehensive audit Proposal DE-I)**: At Standing 3, Partial outcomes generate stat changes (not just narrative). At Standing 4, Success outcomes generate ±2 instead of ±1. At Standing 5, Overwhelming generates ±3. This amplification means the player's growing stature is not just a permission tree — it is a consequence amplifier.

**Seasonal Cap**: ±2 per faction stat per season from all combined Domain Echo sources from a single character. The cap is cumulative, not per-action.

---

# PART 9: THE SOCIAL CONTEST IN THE VIDEOGAME

The RSE critique's assessment of the Social Contest (◐ Robust, ◐ Smooth, ◐ Elegant) is accurate. The system is intellectually elegant but experientially demanding. The videogame needs to close this gap through UI design, not mechanical simplification.

## The Style Decision UI

The central cognitive load of the contest system is the genre × orientation × style matrix. The player chooses from 16 combinations every exchange. In a TTRPG, this takes 30+ seconds. In a videogame, this must take under 5 seconds — or the decision must be genuinely felt rather than calculated.

The solution is to present the decision not as a matrix but as a single axis: **What are you trying to do to the audience's understanding?** Four options, each corresponding to one of the four styles, each described in plain language rather than mechanical terminology:

- **Cite the record** — You show them what happened, what was established, what is known. (Citation: Memory + Revealing)
- **Show the future** — You paint what will happen if your position holds. (Vision: Projection + Revealing)
- **Raise the doubt** — You undermine their certainty in the opponent's position. (Suppression: Memory + Obscuring)
- **Anchor the fear** — You name the worst version of the alternative. (Insinuation: Projection + Obscuring)

The dice mechanics behind each choice remain identical to social_contest_v30. The presentation removes jargon. The Appraise result tells the player which style the audience/adjudicator will respond to best: "The crowd is responding to demonstrations of past precedent" maps to "Cite the record is advantaged." The player can follow the hint or take a risk. The strategic depth of the 16-cell matrix is preserved; the cognitive overhead of naming it is eliminated.

## The Dialogue Lattice Escalation Moment

The Dialogue Lattice's Escalation Trigger is the most important UX moment in the social systems. This is the moment when an exploratory conversation becomes a formal confrontation — when the player has pressed a point the NPC cannot yield on, and both parties know it. In the TTRPG, this moment is narrated by the GM. In the videogame, it needs visual and audio expression that signals: *the stakes just changed*.

The transition should not be mechanical (a pop-up saying "Combat Mode: Social Contest"). It should be environmental: the camera angle shifts slightly. The NPC's idle animation changes. The ambient sound drops. The dialogue options update to show the Contest framing instead of the Lattice framing. The shift is legible to an attentive player without being labeled.

---

# PART 10: THE THREAD SYSTEM AND PLAYER EXPERIENCE

Thread operations are the most technically successful system in the design — the three-axis Ob is genuinely elegant — and the least experientially designed. The game knows what Thread operations do mechanically; it doesn't fully specify what they *feel like* to perform.

## The Videogame's Thread Experience Challenge

Thread operations are described as "consciousness-performed" (P-03). This philosophical claim has a direct videogame consequence: Thread operations should feel different from physical or social actions not because of a different UI panel, but because the camera and world presentation change in a way that reflects the consciousness-performed nature of the act.

Fieldwork_v30 §10.2 specifies the TS-based visual presentation (TS 0 = default rendering, TS 30+ = Thread mesh overlay, TS 50+ = persistent substrate layer). These visual descriptions are correct but incomplete as an experience specification. They describe what the player *sees* without specifying what they *do* with what they see. The Thread visual layer needs to be actionable — the Thread mesh overlay at TS 30 should highlight not just that threads exist but *which threads are relevant to the current investigation*. The Depth-awareness that the comprehensive audit's DF-I proposal identifies (Depth 1–2 = physical/material, Depth 3–5 = social/relational, Depth 8–13 = consciousness/causality) should be expressed visually: threads at different Depths have different visual qualities (thickness, color, stability, warmth). A practitioner looking at a scene through Thread-sight sees a layered world where the physical substrate, the social fabric, and the primordial consciousness-ground are visually distinguishable.

## The Coherence Economy and Personal Stakes

The comprehensive audit's existing Coherence economy is correct (PP-632 derived, war-scale = 7-turn battle produces Coherence 3 after ~7 operations). What it doesn't fully specify is what Coherence degradation *feels like* to the player.

The fieldwork §3.4 rendering strain table is the template: at different Coherence levels, the protagonist's rendering changes. At Coherence 7+, the world appears as the character's consciousness renders it — consistent, complete. At Coherence 5–6 (Strained), slight visual instability at Thread-adjacent locations. At Coherence 3–4 (Dissonant), the Thread layer intrudes into the normal visual presentation even at TS 0 — the character is perceiving the substrate involuntarily. At Coherence 1–2 (Critical), the physical world and Thread layer oscillate — the character cannot hold a consistent rendering.

This visual degradation is the Coherence economy made legible. The player doesn't track Coherence as a number — they see their protagonist's perception of reality destabilizing. The mechanical value and the experiential reality are the same thing, which is exactly what P-03 requires.

---

# PART 11: WHAT MUST NOT CHANGE

The following elements of the existing design are either formally complete, philosophically irreplaceable, or both. They must be protected from modification by future integration work.

**The Sincerity Gate (Spirit TN 7 Ob 1).** 37% failure rate on instrumental connection. The finest single mechanic in the design. Philosophically grounded (genuine connection requires genuine openness), mechanically elegant (one roll, one decision), simulation-validated. The Dialogue Lattice's [SINCERE]/[INSTRUMENTAL] tagging is the correct extension. Nothing else should touch it.

**The Three-Axis Thread Ob (Depth + Breadth + Distance).** The best single mechanical design in the project. It converts a difficulty number into a statement about what you're attempting. Every proposed extension (DF-I's qualitative depth differentiation) works *with* this structure, not against it.

**The Accord Gate on Conquest.** The requirement that occupied/conquered territories have Accord 1 and cannot contribute to Universal Victory is the game's most elegant balance mechanic. It makes conquest require governance without a "no attacking" rule. It must not be softened, bypassed, or made optional.

**The Conviction-to-AI Integration.** The three-step decision procedure (Institutional Filter → Conviction Filter → Decision Fork by wound count) is simple enough to be deterministic, rich enough to be emergent. Every new NPC behavior proposal must work within this architecture rather than alongside it.

**PP-632 (Disposition/Knot via Bonds).** One formula (floor(Bonds/2)+1), two applications (Disposition ceiling and Knot capacity), philosophically grounded, simulation-validated. This is the gold standard for how mechanics should be derived in Valoria. Future mechanics should match this standard.

**The Evidence Track Thresholds (Simple 3 / Complex 5 / Structural 8).** Correctly calibrated. The Named Theory Synthesis (GI-I from comprehensive audit) and Theory Commitment (BH-I) both work within these thresholds. They should not be changed.

**The Seasonal Cap (±2 faction stat per season from Domain Echo).** Small enough that personal-scale actions don't dominate the faction layer, large enough to make personal play feel consequential. The Stature-Scaled Echo proposal amplifies at high Standing without violating the cap's purpose.

**Domain Echo directionality (personal → strategic only).** Echo always flows upward. The strategic layer affects the personal layer through Scene Slate generation and Zoom In triggers (top-down), not through Echo. Confusing these channels would make the system circular and unpredictable.

---

# PART 12: PRIORITY RECOMMENDATIONS — CONSOLIDATED

These are ordered by: (1) blocking vs. not blocking, (2) impact if unaddressed.

## Blocking (required before videogame integration)

**B-1: Commit the Domain Echo Reference Table** as a canonical standalone specification. The table in Part 8 of this document is the proposed canonical form. Without this table, every system that produces personal-scale outcomes cannot specify what faction-level changes follow.

**B-2: Formally unify the Scene Slate and Scene Graph specifications.** The Agency System's generation logic and the Investigation Interface's delivery format are two halves of the same mechanism. Write a single specification that covers: how entries are generated (from Agency System §4.2), how each entry is delivered as a Scene Graph (from Investigation Interface §2), and how the player's scene action budget governs scene access. This is an editorial consolidation, not a mechanical design task.

**B-3: Specify the Dialogue Lattice → Social Contest handoff.** Write a single specification (three paragraphs, not a full document): what state transfers from a completed Lattice session to a Contest that follows it. Conviction Wound count, Disposition-as-Conviction-Track-offset, Evidence-as-Corroboration-preload, Momentum carry. The mechanic already exists; only the formal specification is missing.

**B-4: Write the stability trigger → Scene Slate coupling.** Specify which V30 stability triggers (1–5) generate which Scene Slate priority entries under which conditions. The mapping proposed in Part 3 of this document (Mechanism 2) is the proposed canonical form.

**B-5: Resolve J-7 (0–4 territory scale) and propagate.** This is still blocking because it affects every formula that uses territory tracks. Resolve as 0–4, and update every formula that currently uses 0–5.

## High Value (implement in next design sprint)

**H-1: Named NPC as Ecology Anchor.** Part 5 Gap 6. Costs nothing mechanically; transforms how territories feel. Named NPCs' convictions shift territory social texture before the player discovers the NPC.

**H-2: Counselor Negotiation Output.** Part 5 Gap 1. The Priority Stack Adjustment specification. Currently every Counselor-tier conversation has an undefined outcome; this gives it formal consequence.

**H-3: Occupation → Resistance Scene generation.** Part 5 Gap 2. Closes the gap between the faction_layer's occupation rules and the personal-scale experience of occupation. Turns an abstract mechanical state into a specific scene type.

**H-4: Progressive Revelation sequence.** Part 4. Specifies when each category of World State information becomes visible to the player. Prevents front-loading complexity at onboarding.

**H-5: Parliament + Personal Layer bridge.** Part 5 Gap 3. Standing 3+ can produce Parliamentary Intent as a scene action, with evidence as parliamentary capital.

**H-6: The Style Decision UI for Social Contests.** Part 9. Reduces the 30-second exchange decision to a 5-second choice without removing strategic depth. Required before the game is playable by anyone not already fluent in the contest system.

## Creative Enrichment (implement after above)

**E-1: Instincts (from comprehensive audit Proposal A-I).** One conditional statement at character creation, auto-firing behavior, ±1 Momentum. Zero mechanical overhead, significant character texture.

**E-2: Ambient Node Layer (from comprehensive audit Proposal L-I).** Pre-Fieldwork passive observation at each scene node. Rewards attentive players; makes investigation feel like entering a space rather than rolling a die.

**E-3: NPC Schedule Discovery as Surveil Output (SoD-II).** Surveil produces schedule information, not just Evidence progress. Transforms a mechanical grind action into a planning tool.

**E-4: Theory Commitment and Reframing (BH-I).** At Simple threshold, commit to a named Theory. Subsequent contradicting evidence reveals what was invisible under the wrong frame. Mechanically minimal; experientially transformative.

**E-5: Belief Progress Track (TTRPG-III, extended to videogame).** Three-step progress track per Belief, advances via player declaration validated by the game's adjudication of "is this a genuine step." Triggers a Belief Resolution Zoom In scene at Near Fulfillment. Makes Belief pursuit visible as accumulation, not just binary fulfillment.

---

# PART 13: THE CORE EXPERIENCE STATEMENT

A player should be able to pick up Valoria and experience, within the first four hours:

Someone they've met and cared about making a decision that has consequences they can see. A territory they've moved through changing in a way that reflects what they've done in it. An investigation revealing something that reframes everything they understood about a character. A conversation that starts as exploration and becomes confrontation because the world has weight and meaning and doesn't simply yield when pushed.

These experiences are not dependent on the player understanding the mechanics that produce them. They are dependent on the mechanics being correctly connected so that they produce these experiences without requiring the player to consciously orchestrate them.

That is what the integration architecture is for. Not to add complexity — the game already has enough complexity to reward years of play. But to ensure that the complexity the player earns through attention produces felt consequences rather than statistical updates. To make the simulation and the story the same thing, as the game's philosophy has always promised they would be.

Everything in this document exists in service of that statement.

---

*This document is a design critique and proposal. All recommendations require explicit approval before integration into canonical specifications. The Domain Echo Reference Table in Part 8 and the priority list in Part 12 are proposed as the primary actionable deliverables.*
