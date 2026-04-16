# VALORIA — Comprehensive System Audit
## Agency System · Investigation Systems · Scalability · Domain Echoes
## Date: 2026-04-15
## Scope: Player Agency Proposal + Investigation Systems Proposal, audited against each other, against the holistic audit, against the How to Play document, and against a wide reference library of precedent games.
## Method: Six-axis system audit (Coherence, Consistency, Creativity, Elegance, Connectivity, Robustness) → precedent game analysis → domain echo enshrinement audit → scalability audit → prioritised recommendations.

---

# EXECUTIVE SUMMARY

Both proposals are architecturally sound and philosophically grounded. The Agency System correctly identifies the core motivation problem and solves it with three interlocking systems whose design quality is high. The Investigation Systems proposal extends the existing fieldwork/NPC architecture without redundancy and produces the most significant advance in the project to date: the Ontological Ledger as shared conversational substrate is an elegant solution to a problem that most games of this complexity solve badly or not at all.

**The chief risk in both proposals is not design quality — it is incompleteness at the edges.** The central flows (Belief → Scene Slate → Scene Action → Domain Echo; utterance → five-filter chain → outcome → Ledger/Genome update) are tightly specified. The edge cases — sparse Slates, Certainty threshold ambiguity, Scene Graph contamination, filter stacking, Fieldwork resource cost — are underspecified, and in a game of this systemic density, edge cases are where fragility lives.

**The chief opportunity across both proposals** is importing more of what the referenced games do *viscerally* well. Valoria's mechanical architecture is rigorous. What it doesn't yet have is the felt quality of a great investigation or the felt weight of a great consequence — the Case of the Golden Idol's synthesis moment, Shadows of Doubt's sense of a world moving independently of you, Disco Elysium's inner argument about what the scene means. These are designable. This audit proposes how.

**On scalability:** The RimWorld/Dwarf Fortress lesson is that Valoria already has the right instincts — NPC conviction wounds, faction AI priority stacks, territory ecology — but hasn't fully committed to the principle. The world should generate pressure on the player as consistently as the player generates pressure on the world. Several Scene Slate slots and NPC behaviors currently orient too heavily toward the player's significance. The fix is structural, not additive.

**Priority recommendations:** Thirteen structural proposals, ordered. Six are revisions to existing specifications (closing gaps). Seven are new mechanics derived from the precedent game analysis. None require adding new data structures from scratch — all are extensions or reframings of existing systems.

---

# PART 1: AGENCY SYSTEM AUDIT

## 1.1 Coherence

The Beliefs / Duties / Scene Slate triangle is coherent. Each component addresses a different dimension of the motivation problem without overlap: Beliefs are internal (player-authored narrative drive), Duties are external (institutionally assigned obligation), and the Scene Slate is environmental (world-state made into opportunity). The interactions between them are correctly identified — Duty and Belief tension is the engine, Scene Slate is the fuel.

**Coherence gap C-1: Standing 3 resolution mechanism.** The Counselor tier grants the right to "negotiate or refuse" Duties and to argue for different faction priorities via social contest. But the contest outcome isn't specified. If the player wins the social contest against the faction leader, does the Duty change? Does the faction's AI priority stack shift? Does the faction leader's Conviction Wound advance? The negotiation is described as possible, but the mechanical output of a won negotiation is absent. This isn't a small gap — it's the scene that a Counselor character will have every single season, and it's currently unresolved.

**Proposed resolution:** A won Duty negotiation produces one of three outcomes based on margin: Partial victory (Duty modified — same objective, different method or target), Full victory (Duty replaced by player-proposed alternative, faction leader Conviction Wound +1 from yielding to subordinate), Overwhelming victory (leader changes their stated position publicly, +2 Standing from demonstrating superior judgement). A lost negotiation produces: Duty unchanged, Disposition with leader −1 (overstepped), and the scene generates +1 to the leader's next NPC arc pressure vector ("subordinate challenged my authority").

**Coherence gap C-2: Independent player's Scene Slate generation.** The independent path is specified as receiving no Duties and generating scene opportunities from Beliefs only. But the Scene Slate has five priority levels — an independent character would only receive Priority 3 (Beliefs), 4 (Territorial), and 5 (Ambient). That reduces the Slate size significantly. Does an independent character have a compensating scene action bonus? Does the faction-independent status grant access to cross-faction Priority 3 scenes that a faction-aligned character would lose Disposition for pursuing? This is under-specified and the independent path needs its own Scene Slate parameters.

**Proposed resolution:** Independent characters receive +1 scene action per season (representing the freedom of not serving assigned objectives). Their Scene Slate Priority 2 slot is replaced by a "Factional Observation" slot — one scene per season that reflects the dominant faction activity in the player's current territory. This gives independents situational awareness of the faction layer without being beholden to it.

**Coherence gap C-3: Belief fulfillment trigger conditions.** Fulfillment "may trigger a character development moment (Certainty shift, NPC arc trigger, or Domain Echo if the fulfillment had Sufficient Scope)." The word "may" is doing work that should be done by a condition. When does fulfillment trigger a Certainty shift? When does it not? What makes a fulfillment have "Sufficient Scope"?

**Proposed resolution:** Belief fulfillment triggers are conditional on the Belief's scope at the moment of fulfillment. A Belief targeting a named NPC ("I will prove to Almud that the Thread is real") triggers an NPC arc moment for that NPC. A Belief targeting a system or institution ("I will build a network of Thread-aware allies before the Church finds me") triggers a Domain Echo proportional to the number of Disposition relationships involved. A Belief targeting the Thread substrate ("I will Mend the Gap at Askeheim before the next MS band break") triggers an MS-level Echo. The "Sufficient Scope" threshold for a Domain Echo is: a Belief whose fulfillment affects more than one named NPC, or a territory, or a clock. The current Belief fulfillment grant (+2 Momentum) remains; the Echo triggers on top of it.

---

## 1.2 Consistency

The scene action budget (3–5 per difficulty) is internally consistent and its modifiers (+1 from Standing 4, −1 from Stamina 0 or 2+ Wounds) follow the established modifier logic. The Duty completion table uses the same terminology (Standing track, thresholds, consequences) as the Standing specification in §5.

**Consistency gap CS-1: Scene Slate generation — "scanning Belief text" for NPC names.** The proposal states the game scans Belief text for NPC names, faction references, territory references, and system keywords to generate Belief-aligned opportunities. In the videogame, this requires either runtime natural language processing or tagged Belief construction. Runtime NLP is fragile and inconsistent; untagged free text will miss references and produce incorrect Slate generation silently.

**Proposed resolution:** Believe construction in character creation uses a structured template with free-text composition but mandatory tag fields. When writing a Belief, the player also assigns up to three tags from available categories: [NPC: name], [Territory: name], [Faction: name], [System: Thread/Church/Parliament/Military/RM]. The tags are the search keys for Scene Slate generation; the Belief text is narrative expression only. Player experience is identical (they write a sentence), but the implementation is robust.

**Consistency gap CS-2: Belief-gated utterances bypass the Sincerity Gate (from the investigation proposal, DL integration §3).** This creates an asymmetry: a player pursuing a Belief is assumed to be sincere, bypassing the 37% Spirit check failure. But a player can write a manipulative Belief ("I will befriend Haelgrund in order to extract his secrets") and receive the bypass on what is mechanically an instrumental connection. The bypass should be conditional on the *nature* of the Belief's intent, not the existence of the Belief tag.

**Proposed resolution:** Belief-gated Sincerity bypass applies only to Beliefs that are about the relationship itself (e.g., "I will protect Torben...," "I will prove to Almud...") and not to Beliefs that use a relationship instrumentally. The investigation proposal's Dialogue Lattice already distinguishes [SINCERE] vs [INSTRUMENTAL] utterance tags — the Belief gate should inherit this distinction. An [INSTRUMENTAL] Belief-tagged utterance still triggers the Sincerity Gate.

**Consistency gap CS-3: Standing collapse and functional independence.** If Standing falls to −1, "the faction stops assigning Duties — the player is functionally independent." But functional independence differs from chosen independence (§5.3): the collapse-independent character has no Domain Action influence, no faction intelligence, no safe harbor — identical to chosen independence. The Standing collapse path isn't punished differently than elective independence, which means there's no mechanical reason to care about Standing collapse beyond the loss of faction services. More fundamentally: a faction that has fired a member would realistically treat them as a potential liability, not just as a non-member. The collapse path should have at least one consequence the chosen-independent path doesn't.

**Proposed resolution:** A character whose Standing collapsed to −1 receives a "Burned" flag with their former faction. Burned characters generate +1 Exposure per season in territories controlled by that faction (the faction is watching for them), and one of their former faction's NPCs begins an arc vector of "retrieve or neutralize former asset" (Disposition toward player locked at −2 minimum, cannot be improved above 0 without specific condition: Standing rebuilt via third-party testimony to the faction leader). This makes faction separation consequential without making it catastrophic.

---

## 1.3 Creativity

The Beliefs system is solidly in the tradition of Burning Wheel's Beliefs architecture (Luke Crane, 2002–2018) and that lineage is appropriate for a game with this level of philosophical ambition. The structure — three declarative sentences with an obstacle implied — is correct. The Momentum reward for pursuing Beliefs is the equivalent of BW's Artha. The design is not derivative; it is a purposeful selection from a design tradition that has proven the model at the table.

**What's missing from the BW tradition: Instincts.** Burning Wheel's third character-statement layer — alongside Beliefs and Goals — is the Instinct: a short conditional statement ("When surprised, I always draw my weapon"; "I always note the exits in any room I enter"). Instincts fire automatically when their condition is met, without consuming a scene action. They cost nothing but can create problems — an Instinct can fire at inconvenient moments and generate consequences. This is character texture that costs nothing to add and nothing to track, and it creates memorable moments (the player who has "I always speak the truth, even at cost" finds themselves in exactly the scene that makes that Instinct matter).

**Proposal A-I (Instincts):** Add one Instinct to character creation. One sentence, conditional format ("When [condition], I always [action]"). The Instinct fires automatically when the game state matches the condition — this is the Scene Slate's job to detect. When an Instinct fires, it happens before the scene action decision, representing the character's automatic behavior. It may consume no scene action (reflexive) or one (if the Instinct action is substantial, like "I always read the room before speaking" triggering a free Appraise check). It cannot be voluntarily suppressed without rolling Conviction against the player's Spirit Ob 2. Instinct fulfillment grants +1 Momentum; Instinct suppression costs −1 Momentum.

**Creative strength of the Duty system:** The "Exceeding" mechanic (Standing +2 instead of +1) is the best feature in the Agency proposal. It correctly identifies that the most interesting space is not duty compliance but duty transcendence — doing what was asked and more. This is what separates a mechanical obligation from a meaningful story beat. The named examples (discovering a conspiracy, turning an enemy NPC, generating Casus Belli) are all excellent. This should be explicitly specified in the TTRPG rules, not just the videogame implementation.

---

## 1.4 Elegance

The scene action budget as pacing lever is elegant in principle. Five priorities of Scene Slate generation is slightly complex but navigable. The table format of Duty types (Table 3.3) is clean and mirrors the factional AI structure.

**Elegance concern E-1: Belief tagging (see CS-1 above).** Solved by structured tag fields.

**Elegance concern E-2: The Scene Slate's Priority 4/5 slots feel residual.** They're defined as "territorial" and "ambient" — events in the player's territory, low-priority texture. In practice, they will be the most common Slate entries for characters who don't have pressing Duty or Belief conflicts in their current location. A system that leaves 2 of its 5 priority layers as "texture" is leaving half its opportunity architecture as decoration.

**Proposal A-II (World Pressure Slots):** Priority 4 and 5 are renamed to "Territorial Events" and "World Momentum" respectively. Priority 4 (Territorial Events) is generated from the NPE with no reference to player Beliefs or Duties — events happening in the territory because the territory has its own state (a Piety 4 territory generates a religious enforcement scene; a Prosperity 1 territory generates a food shortage scene; an Accord 1 territory generates a political dispute scene). These are things the player walks into, not things that come to them. Priority 5 (World Momentum) surfaces one event from the peninsula-level state that has nothing to do with the player but is in their vicinity — a passing trade delegation, a Church courier en route to a decision that will affect the whole peninsula, a Warden on a mission the player may or may not understand. These slots are explicitly non-player-centric: they represent the world's own momentum. Pursuing them is optional and may have no relation to Beliefs or Duties — but they're where unexpected story comes from.

---

## 1.5 Connectivity

The integration table (§7) is thorough. The connections to board_game_v30, fieldwork_v30, scale_transitions_v30, and npc_behavior_v30 are correctly specified.

**Connectivity gap V-1: Thread system and Coherence have no agency-system integration.** A Thread practitioner character can write Beliefs about Thread operations ("I will Mend the Gap at Askeheim before the next MS band break") and Duties include Thread Operations as a type. But there's no specification for how a Thread practitioner's Coherence state affects their Scene Slate or their Duty compliance. A practitioner at Coherence 3 (Dissonant) is mechanically impaired — should they be able to receive a Thread Operation Duty? Should their low Coherence produce a Scene Slate Priority 1 event (personal crisis as crisis event)?

**Proposed resolution:** Add to Scene Slate Priority 1 (crisis events): "Coherence ≤ 3 and the player is a practitioner." A Dissonant practitioner's instability is a personal crisis that generates a Zoom In scene — not a combat or governance challenge, but a Thread-reality scene where the character's perceptual coherence is tested. The outcome (Mending, Anchoring via a Knot, or resisting without resolution) has mechanical effects (Coherence ±1) but also Belief fulfillment potential (a Belief about Thread mastery or self-understanding).

**Connectivity gap V-2: Combat outcomes with Sufficient Scope have no specified Domain Echo pathway in the agency proposal.** The how-to-play document explains Domain Echo correctly. But a Belief like "I will defeat the Church's Inquisitor in single combat before he reaches the Southernmost" — when fulfilled through combat — doesn't have a specified Echo. Combat Beliefs are likely to be common, and their fulfillment should have the same Echo architecture as investigation and Thread Beliefs.

**Proposed resolution:** Add a row to the Domain Echo table (when formally written): "Personal combat with a named NPC or faction commander: Overwhelming Victory → faction stat −2 for the defeated NPC's faction; Success → −1; Partial → narrative disruption to NPC's arc only; Failure → +1 Disposition to NPC (they've proven their superiority, player character is in their debt)."

---

## 1.6 Robustness

**Robustness gap R-1: Sparse Scene Slate.** The proposal doesn't address what happens when a player is in a remote territory with no active crises, no NPCs they have relationships with, and Beliefs that reference NPCs/territories they're not near. Priority 1–3 could all produce zero entries. Priority 4–5 would only produce entries if the territory has state variation. A sparse Slate (0–2 entries) combined with a 3-action budget means the player has almost nothing to do for a season.

**Proposed resolution:** Minimum Slate guarantee. Priority 5 (World Momentum) always produces at least 1 entry regardless of other conditions — the peninsula is always moving. If Priorities 1–4 produce fewer than 2 entries, the game automatically generates 1 additional Territorial Event from the player's current territory (per NPE) and 1 faction activity summary (the faction's most recent Domain Action creates a scene the player witnessed from their location — they saw the trade caravan arrive, heard the Parliament vote's outcome from a passing rider, observed troops muster at the nearest fort). This prevents dead seasons without adding artificial urgency.

**Robustness gap R-2: Leadership challenge failure mechanics.** Standing 4+ can initiate a leadership challenge. Failure drops Standing to 2 and Disposition to −4 with the leader. But what does the faction council do? A faction council that watched a senior member publicly challenge the leader and lose now has information: they know the challenger is ambitious and failed. This should have arc consequences beyond Disposition — the council NPCs have updated information states, and some of them may have secretly supported the challenger (their arc vectors shift).

**Proposed resolution:** A failed leadership challenge generates a "Succession Tension" arc vector for each faction council NPC, evaluated against their conviction: Order-convicted council members move toward the leader (the challenge destabilized them); Autonomy-convicted members become covert supporters of the challenger (they respect the attempt); Loyalty-convicted members are now in crisis (torn between institutional loyalty and personal). The faction as a whole gains +1 Political Stability (a visible challenge has been suppressed, which raises tension system-wide).

---

# PART 2: INVESTIGATION SYSTEMS AUDIT

## 2.1 Coherence

The four-system architecture (NPE → Investigation Interface → Dialogue Lattice → Response Matrix) coheres around the Ontological Ledger as shared substrate. This architectural choice is sound: it means all four systems read from and write to the same record rather than maintaining separate state. The Ledger's eight fields are all drawn from existing character state, which means the proposal adds no new data — it makes existing data structurally explicit. This is the investigation proposal's greatest design achievement.

**Coherence gap I-1: Certainty 3 — the threshold problem.** The Certainty Gate specification identifies Certainty 3 as "the middle ground — neither set of utterances is fully available." But "neither fully available" means different things depending on implementation: does the character at Certainty 3 have degraded access (lower-yield versions of both sets), partial access (a subset of each), or genuinely no access (they're in a gap between two worldviews)? The "epistemically in transition" framing is philosophically correct but mechanically underspecified.

**Proposed resolution:** Certainty 3 ("Uncertain") is the most mechanically interesting state and should be the most expressively rich, not the most impoverished. A Certainty 3 character can access one utterance from each Certainty-gated set per conversation (lowest-commitment Orthodox utterances, lowest-commitment Thread-aware utterances), but these utterances are tagged [UNCERTAIN] and produce modified responses through Filter 1 — the NPC perceives the character's ambivalence, which is itself information about the character's state. High-Certainty NPCs read this as doubt (and may attempt conversion); Low-Certainty NPCs read this as openness (and may offer Thread disclosure). This makes Certainty 3 the most interpersonally productive state — the character who is genuinely unsure produces more NPC reactions than the character who is fully committed in either direction. This aligns with P-15's three-layer being-persistence: Certainty 3 is the visible expression of a Belief layer in transition.

**Coherence gap I-2: Case Board persistence across investigations.** Evidence Track persists across seasons (confirmed correct, existing rule). Case Board nodes persist correspondingly. But when does a Case Board entry expire? When an investigation's subject NPC dies or leaves the territory? When a clock threshold passes and makes the evidence obsolete? The Case Board is described as persistent but the conditions under which nodes become invalid or irrelevant are not specified.

**Proposed resolution:** Case Board nodes are tagged with a validity condition at generation: [Valid until: NPC alive], [Valid until: Season end], [Valid until: Clock threshold X], [Permanent]. Most evidence nodes are Permanent (a document exists, a wound was inflicted, a conversation was had). NPC-testimony nodes are Valid until: NPC alive. This means a Case Board can accumulate dead evidence as NPCs die — historical facts that no longer have living witnesses, which are still usable as Casus Belli (factual) but not as Corroboration in a live Contest (no witness to call).

**Coherence gap I-3: The Case Board and the Reconstruct action.** The proposal correctly identifies Reconstruct as the action that draws connections between Case Board nodes. But the existing Fieldwork specification of Reconstruct is a pool roll that produces a finding. If the Case Board is the visual Evidence Track, then Reconstruct is both an action and a mechanic that produces a visual output. The integration should make Reconstruct explicitly the Case Board connection action rather than an abstract Evidence Track advancement roll — the player selects two nodes and the roll determines whether the connection is valid. A failed Reconstruct doesn't add a false connection (which would create cascading confusion); it reveals that the player cannot yet see how the nodes connect (they lack the intermediate evidence to bridge them).

---

## 2.2 Consistency

The five-filter chain processes NPC responses in a consistent order (Information → Conviction → Disposition → Compromise → Ethics). The order is logical: comprehension failures (Filter 1) are more fundamental than willingness failures (Filter 3) which are more fundamental than ethical-style mismatches (Filter 5). Each filter's outputs (pass/modify/block/escalate) are defined.

**Consistency gap IS-1: Dual system collision in the same scene.** The existing 3-step NPC Domain Action decision procedure (Institutional Filter → Conviction Filter → Decision Fork) governs NPC strategic behavior. The Response Matrix governs NPC conversational behavior. In a scene involving a named NPC, both systems are active simultaneously — the NPC is both reacting to the player's utterances (Response Matrix) and potentially executing a Domain Action (Priority Stack). The proposal notes they are separate systems, but doesn't specify whether a Domain Action priority can interrupt or terminate a Dialogue Lattice session. Can an NPC mid-conversation suddenly receive and act on a high-urgency institutional priority (Survival tier: Stability ≤ 2)? If so, what does that look like mechanically?

**Proposed resolution:** Priority tier governs interruption. During a Dialogue Lattice session, NPC Domain Action priorities are frozen at their current evaluation unless a Survival-tier event fires (new Priority-1 trigger during the scene). If a Survival-tier trigger fires mid-scene (e.g., the NPC receives news of an imminent faction collapse), it produces an Escalation outcome in the Dialogue Lattice — the conversation is interrupted not by player choice but by world event. The NPC's response is "forced-end" (specific dialogue node: the NPC terminates the conversation to address the emergency). This creates memorable emergent scenes: the conversation you were building toward suddenly cut short by the world moving.

**Consistency gap IS-2: Filter stacking vs capping.** Pending decision RR-01 asks whether Filters 1 and 5 hostile modifiers stack or cap. The proposal recommends stacking with a cap at Disposition −2. But Filter 2 (Conviction) also produces hostile modifiers (Wound 0 produces active defense/pushback depending on Disposition). Three concurrent hostile modifiers — Information Filter (interpretive mismatch), Conviction Filter (active defense), Ethical Framework Filter (resisted approach) — could produce a response state where the NPC is simultaneously interpreting the utterance incorrectly, defending their conviction, and hostile to the approach. Is this the right outcome, or should extreme incompatibility produce a simpler result: complete communicative failure?

**Proposed resolution:** When three or more filters produce concurrent hostile or blocking modifiers, the result simplifies to Communicative Failure — the NPC doesn't engage with the content of the utterance at all. They respond to the social act (someone speaking to them) but not to the substance. This produces a specific outcome type not currently in the outcome list: **Social Non-Encounter** — a response that gives the player no evidence, no Disposition shift, no Conviction engagement, but confirms that this particular approach channel is entirely closed with this NPC at this arc point. The player learns something about what doesn't work, which is investigative information. This prevents the five-filter chain from producing incoherent compound results and adds a sixth outcome type to the Dialogue Lattice.

---

## 2.3 Creativity

The Investigation Interface's scene-as-graph concept is the most creative element of the proposal and is underexplored. The node types (Anchor, Evidence, Drift, Access, Observation) correctly identify the main categories of investigative encounter, and the temporal dimension (Drift NPCs moving on time cycles) is the right implementation of spatial-temporal investigation.

**What the graph concept hasn't yet incorporated: path-level information.** Currently, information is at nodes. Moving between nodes costs time but reveals nothing. Lacuna (Monokel, 2021) and Shadows of Doubt (ColePowered Games, 2023) both operate on the principle that space itself is information — not just the things at locations, but what you can see between locations. A player walking from the Archive node to the Chapel node in a Church territory passes through a corridor. That corridor might have a guard patrol schedule, a locked door, a suspicious absence of a clerk who should be present. None of these are nodes; all of them are investigative data. The transit between nodes should be possible information.

**Proposal I-I (Path-Level Information):** Edges between nodes can carry optional information payloads, triggered by the Surveil action during transit. If the player uses Surveil while moving (costing +1 Exposure as specified), they may observe edge-level information: patrol schedule, absence of expected persons, ambient evidence of recent activity (disturbed dust, a discarded letter, a door that should be locked but isn't). These don't advance the Evidence Track directly but add Case Board nodes tagged [Contextual] — they provide connective tissue for Reconstruct without being primary evidence themselves. Implementation note: edge information is generated from scene graph templates at scene instantiation, not dynamically — it's authored, not procedural.

**What the NPE hasn't yet incorporated: off-screen social activity.** The proposal specifies that at season end, NPCs with shared worldview and adjacent Stance positions make a Volatility check and may shift toward each other. This is an excellent seed of off-screen social dynamics. But it models only horizontal peer influence. Missing: vertical influence (authority NPCs shift subordinate NPCs' worldviews through institutional pressure, regardless of Volatility) and adversarial influence (high-Volatility NPCs with opposing Stances don't just drift toward each other — they argue, which can produce Conviction Wounds even off-screen).

**Proposal I-II (Off-Screen Social Pressure):** At season end, in addition to the existing peer-influence Volatility check: each territory generates one "dominant NPC social event" derived from the controlling faction's ethical framework and the territory's current Accord/Piety state. High-Piety territories under Church control produce a catechism event (+1 Certainty weight for all NPEs in the territory). Low-Accord territories produce a grievance event (all NPE Worldview Conviction resistances reduced by 1 — the population is less committed to institutional worldviews under stress). These are not new scenes — they don't generate Zoom In moments. They're season-end ecology updates that modify the next season's social landscape before the player arrives.

---

## 2.4 Elegance

The five-filter chain risks cognitive overhead in implementation and in play. The full chain (five sequential filters, each with up to four possible outcomes, modifying a response along multiple axes) is powerful but potentially opaque to the player who is trying to understand why the NPC responded as they did.

**Elegance concern: filter chain visibility.** If an NPC responds with hostility, the player needs to understand which filter produced the hostility to know how to address it. "The NPC is hostile because they misunderstood (Filter 1)" requires a different player response than "hostile because I violated their ethics (Filter 5)." In the TTRPG, the GM informs the players. In the videogame, the UI must make the filter output legible.

**Proposal I-III (Response Attribution):** Each NPC conversational response is accompanied by a brief attribution tag — not mechanical notation, but narratively expressed signal. "She responds as if you've accused her" (Filter 1 modification — Certainty interpretive filter). "He speaks carefully, with effort" (Filter 2 — Conviction Wound 1 strained response). "She doesn't look at you" (Filter 3 — Disposition −2 defensive response). These are authored response flavors, not procedural labels, but they reliably correspond to specific filter states. In the videogame, the player can develop the skill of reading these signals as investigative data — learning which filter is responsible is itself a form of NPC intelligence. The attribution tag is narrative, not mechanical; it doesn't add to the information display load.

**The Compromise Profile is the filter with the most untapped design space.** Currently it identifies five categories (Economic, Informational, Political, Personal, Nothing). But the conditions under which a Compromise Profile activates — "only exchanges information to faction-aligned actors" being the example — aren't generalized. Each NPC's Compromise Profile should have both a category and a condition, and the conditions should vary in ways that are discoverable through play. The condition is part of the NPC's Genome (known to the game, not the player) and discovering it is a form of investigation.

**Proposal I-IV (Discoverable Compromise Conditions):** Compromise Profile conditions are Genome fields that function like hidden Genome components. The player discovers a condition by either: (a) successfully Appraising the NPC (Attunement roll reveals the NPC's primary Compromise category — Economic, Political, etc.); (b) attempting an exchange that matches the category but violates the condition (the NPC refuses for a specific reason that reveals the condition); (c) through a trusted third-party NPC's intel. This makes NPC intelligence-gathering a multi-stage process: first discover the category, then discover the condition. A Structural-threshold investigation might fully map a named NPC's Compromise Profile before the player ever directly approaches them — which means a well-prepared player enters a conversation knowing what will and won't work. This rewards thoroughness.

---

## 2.5 Connectivity

The cross-system integration table at the proposal's close is the most complete connectivity specification in either proposal. The connection between the NPE and the Season-end ecology (Piety drift → ecology weight shift) is correctly specified and requires no new data.

**Connectivity gap IC-1: NPC stance convergence and the arc system.** When two NPEs' Stances converge off-screen (season-end Volatility check), this should create a latent arc vector, but the proposal only says that "deviation ≥ 5 NPCs become latent arc vectors." Stance convergence between NPEs is a different and underspecified arc trigger — the two NPEs becoming ideologically aligned without player intervention represents an off-screen organizing process that should be detectable and consequential.

**Proposed resolution:** When two or more NPEs in the same territory achieve Stance convergence (same issue, adjacent values, Volatility check passed), they are flagged as a "Coalition embryo." The arc evaluator checks whether the coalition's shared Stance is on an active political issue. If yes: a latent arc vector fires — "Community [Territory Name] organizing around [Issue]." This becomes a Priority 4 scene opportunity in the following season (the player can investigate who is organizing, why, and with what effect on faction politics). At Structural threshold, a Coalition can become a formal RM Community (if Thread/Piety-aligned) or a political bloc (if governance-aligned), generating Domain Echo and potentially creating a new minor faction actor.

**Connectivity gap IC-2: Case Board and Social Contest Corroboration.** The existing Social Contest mechanic specifies that gathered evidence can be used as Corroboration (+1D). The Case Board is the visual Evidence Track. These should be the same thing, but the investigation proposal doesn't explicitly unify them. A player who has Case Board nodes should be able to select specific nodes as Corroboration in a Contest (not just "Evidence Track ≥ threshold = +1D available," but "I'm using this specific piece of evidence").

**Proposed resolution:** Corroboration is upgraded to Case Board Citation. When the player elects to Corroborate in a Social Contest, they select a specific Case Board node (a named piece of evidence). The value of the Citation depends on the node's investigation type and the Contest's adjudicator: Expert Judge Cognition adjudicator → Documentary evidence (Research-derived nodes) is worth +1D, Testimony evidence (Interview-derived nodes) is worth +2D if the witness is present; Crowd Charisma adjudicator → the reverse. This connects the investigation system to the contest system specifically and meaningfully — different investigation approaches produce different contest advantages, creating strategic synergy between fieldwork and debate.

**Connectivity gap IC-3: Thread Sensitivity and scene graph access.** The Investigation Interface correctly identifies that some nodes require specific conditions for access. But TS gates on scene graph nodes aren't specified beyond the Dialogue Lattice's TS gate. A Thread Wound formation scene — one of the Zoom In trigger categories — should have scene graph nodes that are entirely inaccessible to TS 0 characters. A Thread-blind character at a Gap formation site is in a spatial scene that is semantically entirely different from what a TS 30+ character experiences at the same nodes. The scene graph needs to account for this.

**Proposed resolution:** Scene graphs generated by Thread-related Zoom In triggers are annotated with TS access layers. Each node has a Primary Layer (available to all characters) and optionally a Thread Layer (available to TS 1+ characters, representing perception of wrongness without understanding) and a Practitioner Layer (available to TS 30+ characters, representing Thread-direct observation). The Primary Layer contains physical evidence; the Thread Layer contains perceptual anomalies; the Practitioner Layer contains Thread-direct evidence. A character's TS level determines which layers they can access at each node, and a scene that is mundanely uninformative (the field looks empty) may be Thread-rich (the substrate here is violently disrupted) or even Practitioner-critical (a Gap is forming at Depth 5, breadth is expanding). This unifies the Thread operations system with the investigation scene architecture.

---

## 2.6 Robustness

**Robustness gap IR-1: NPE persistence ceiling and relationship continuity.** The pending decision NPE-02 proposes a cap of 3 persistent minor NPCs per territory per year, with oldest retired if exceeded. The problem is relationship continuity: a player who has built Disposition +2 with a minor NPC over two seasons would lose that relationship if the NPC is retired. Disposition is the core social currency of the game, and losing it due to a population cap mechanism would feel arbitrary.

**Proposed resolution:** NPE retirement is "soft exit" — a retired NPC doesn't cease to exist, they move to a low-persistence state. They retain their Genome and their Disposition with the player but no longer appear as scene participants in their home territory. They can still appear in other scenes: as a reference ("The merchant you knew in Gransol sent a letter"), as a Priority 4 event in adjacent territories ("The merchant from Gransol has relocated to Harvik with news"), or as a triggered re-entry if the player visits their new territory. Effectively, the cap governs active scene participants, not social memory. NPCs with Disposition ≥ +2 or with Conviction Wounds from player interaction are never fully retired — they persist as part of the player's social history even if no longer scene-active.

**Robustness gap IR-2: The Investigation Interface and dead ends.** A scene graph may have Access nodes that require conditions the player cannot currently meet (Cognition 3 needed, player has Cognition 2; requires Evidence [Church-Lab] not yet gathered). In a session where the player chose to pursue this scene with their available capabilities, reaching an inaccessible Access node and finding no other paths to the scene's core evidence is a dead end. The player has spent a scene action with no Evidence Track advancement.

**Proposed resolution:** Scene graphs are designed with "bypass paths" — alternative routes to key evidence that require different capabilities. An Access node blocked by Cognition 3 might have an alternative Surveil approach (Agility-based, Ob higher) or an NPC Drift node approach (the NPC carrying the access key arrives at a different time, requiring waiting). A player who maps all accessible nodes in a scene and finds no path to a central Access node should always find at least one alternative path that costs more time (additional scene action or Exposure) but requires different attributes. No scene graph should have a single required Access node with no bypass.

---

# PART 3: DOMAIN ECHO ENSHRINEMENT AUDIT

## 3.1 Current State

Domain Echo appears in:
- How to Play §3.3 (examples, not a formal specification)
- Agency Proposal §7.7 (Beliefs as arc vectors, Echo mentioned for "Sufficient Scope" fulfillments)
- Investigation Proposal §2 Integration (scene graph as Zoom In trigger, Echo implied)

It does not appear in the investigation proposal's outcome table. It does not have a formal specification table with input conditions, output magnitudes, and directionality.

**Finding:** Domain Echo is the game's most important cross-scale mechanic — it is the bridge between personal play and the strategic layer, the mechanism that makes the player feel that their personal actions matter at the faction level. It is described in examples and implied in several proposals, but it has never been formally specified as a standalone system. This is the largest single gap in the system's enshrinement.

## 3.2 Formal Domain Echo Specification (Proposed)

**Trigger condition: Sufficient Scope.** A personal action has Sufficient Scope if it affects one or more of: (a) a named NPC's arc (conviction wound, major Disposition shift, death, conversion), (b) a territory's tracked stats (Accord, Piety, Prosperity, Fort Level), (c) a clock (MS, CI, IP, TC, RS), (d) a faction's strategic position (intelligence gain, Casus Belli generated, alliance state change). Personal actions that affect only the player's own state (Coherence, Wounds, Stamina, Exposure) never have Sufficient Scope for Domain Echo.

**Magnitude table:**

| Outcome Degree | Domain Echo Magnitude |
|---|---|
| Overwhelming | ±2 faction stat OR ±2 clock magnitude |
| Success | ±1 faction stat OR ±1 clock magnitude |
| Partial | Narrative shift only (NPC arc update, territory flavor change — no stat change) |
| Failure | −1 faction stat for the player's faction (or the faction whose interest the player was serving) |

**Directionality:** Domain Echo is always upward (personal → strategic). The strategic layer affects the personal layer through Zoom In triggers and Scene Slate generation, not through Domain Echo. These are distinct channels — Echo is bottom-up; Slate/Zoom is top-down.

**Per-system Echo outputs:**

| Action Type | Sufficient Scope Condition | Echo Target |
|---|---|---|
| Investigation — Structural threshold | Named NPC arc evidence OR territory intelligence | Faction Influence ±1 (if delivered to faction) OR Casus Belli generated (political leverage) |
| Social Contest — Grand Contest | Against named NPC on political issue | Conviction Wounds → NPC arc trigger → faction stat change per existing arc rules |
| Thread Operation — Mending | MS restoration | MS ±1 to +2 (existing; confirmed Sufficient Scope) |
| Thread Operation — Dissolution | Gap creation | MS −1 (existing); IP +1 from destabilization |
| Personal Combat — Defeat of named NPC | NPC removed from faction | Faction Mandate/Influence −1 (loss of key actor) |
| Belief Fulfillment — relationship Belief | Deep Disposition change with named NPC | NPC arc trigger (see Belief fulfillment resolution in §1.1) |
| Belief Fulfillment — systemic Belief | Affects territory or clock | Domain Echo per achievement scope |
| Duty Completion — Investigate | Evidence Track ≥ Complex threshold | Faction Intelligence +1 (faction now knows what the player discovered) |
| Duty Completion — Subversion | Territory Accord reduced | Territory Accord −1 in target territory (existing domain action outcome) |
| Governance — sustained | Territory Accord maintained | Accord +1 if player spent 2+ consecutive seasons governing |
| NPE Coalition → formal faction | Territory organizing arc | Piety or Accord +1 (local), new minor faction actor |

**This table is proposed as a standalone Domain Echo Reference (DE-REF-01) to be committed as a formal specification.**

## 3.3 Scalability of Domain Echoes

**The current Echo magnitude (±1 or ±2 to faction stats) is calibrated for personal-scale actions.** As the player's stature increases (Standing 3–5), their actions should produce larger Echoes — a faction leader's personal defeat of a rival general should Echo differently than an operative's assassination of a minor functionary.

**Proposal DE-I (Stature-Scaled Domain Echo):** Echo magnitude is modified by the player's Standing:

| Standing | Echo Modifier |
|---|---|
| 0–1 (Operative) | Echo as base table |
| 2 (Agent) | +0 (no modifier — still establishing) |
| 3 (Counselor) | Partial outcomes now generate stat changes (not just narrative) |
| 4 (Lieutenant) | Success outcomes generate ±2 instead of ±1 |
| 5 (Successor) / Leader | Overwhelming outcomes generate ±3; personal combat victory over rival faction leader generates Victory Condition relevant outcomes |

This means the player's growing stature is not just a permission tree — it literally amplifies what their actions mean to the strategic layer. A Standing 5 character is more consequential per action than a Standing 1 character, which is both realistic and motivating.

---

# PART 4: PRECEDENT GAME ANALYSIS — GAMES NOT IN THE PROPOSALS

The agency and investigation proposals draw on five games (ROTK, CK3, Disco Elysium, Mount & Blade, Pathologic 2, Pentiment). The following games were specified for this audit and are not yet incorporated.

---

## 4.1 Lacuna (Monokel, 2021)

Lacuna is a science-fiction point-and-click investigation game notable for two design decisions: (1) investigation proceeds entirely through spatial attention and environmental interpretation, with minimal NPC dialogue, and (2) the player's ability to intervene in a scene is constrained by where they physically are when events unfold.

**What Lacuna does exceptionally well:** Investigation as spatial attention economy. The player cannot be in two places at once, and being in the right place at the right time — knowing where to watch, not just what to find — is the core investigative skill. Information is continuous, not discrete: you don't "find clue #3," you observe a location long enough to notice its patterns.

**What Valoria's investigation proposal captures:** The Drift NPC mechanic and temporal dimension are directly Lacuna-influenced, and correctly so. The "player must be at the right node at the right time" is the essential Lacuna mechanic transplanted into the scene graph.

**What Valoria's investigation proposal doesn't yet capture:** Lacuna's sense that the space itself is a document. In Lacuna, you read a room before you interact with it — the arrangement of furniture, the absence of expected objects, the thing slightly out of place, all before speaking to anyone. This is environmental evidence that precedes conversational evidence. In Valoria, the scene graph has Evidence nodes (discoverable objects/documents/states) but these are defined as "yields nothing without correct Fieldwork action." They're not passive — you have to act on them. Lacuna suggests they should be passable without action: entering a node, without doing anything, should convey some ambient information. The presence of an Anchor NPC who is nervous tells you something. The locked cabinet where no lock should be tells you something. These aren't Fieldwork actions — they're the ambient layer that rewards player attention.

**Proposal L-I (Ambient Node Layer):** Each scene graph node has a passive ambient description that the player always receives on arrival — this is the "what you notice when you enter" layer. The ambient description is authored, not rolled, and contains one or two observational facts. Some ambient facts are consistent with the cover story (confirming nothing suspicious); some are anomalies (a fact that doesn't fit). Noticing an anomaly doesn't advance the Evidence Track, but it can mark a node as "Suspicious" — which unlocks a specific targeted Fieldwork action ("Examine the cabinet — something's wrong here") that the player wouldn't have known to perform without the ambient layer. This gives investigation a pre-Fieldwork "attention pass" that rewards players who read carefully before acting.

---

## 4.2 Between Horizons (Application Systems, 2023)

Between Horizons is a science-fiction mystery game set on a generation ship. Its chief innovation is the **incomplete-information commitment mechanic**: the player must decide what happened before they have all the information, and the act of deciding commits them to an investigative frame that shapes what they subsequently find and what they miss. Acting on a partial theory is not just a weaker version of the full-solution — it is a genuinely different epistemic act.

**What Between Horizons does exceptionally well:** It makes the *act of concluding* a mechanical event, not just a narrative one. The player's declared theory changes the investigation state — confirming the theory generates one set of evidence, while contradicting it forces a reframe that reveals different evidence (things you couldn't see while you were committed to the wrong theory).

**What Valoria's investigation proposal captures:** The Evidence Track thresholds (Simple = 3, Complex = 5, Structural = 8) do approximate incomplete-information action: the player can act on a Simple theory, present a Complex theory as leverage, and build a Structural proof. But these are additive stages — each threshold is a stronger version of the previous. Between Horizons suggests they should be *qualitatively different epistemic states with different investigative consequences*.

**Proposal BH-I (Theory Commitment and Evidence Reframing):** When the player reaches Simple threshold (3 Evidence points) and elects to Reconstruct a named Theory (declaring a specific claim: "Church Official X authorized Thread experiment Y in location Z"), the Theory enters a Committed state. Evidence gathered subsequent to the Theory commitment is now evaluated against it: Corroborating evidence (consistent with the theory) advances the track normally (+1 point). Contradicting evidence (inconsistent with the theory) does not advance the track — instead, it adds a [Contradicts: Theory X] tag to the Case Board node. Three [Contradicts] tags invalidate the committed Theory and force a Reframe (the theory is abandoned, the player returns to an uncommitted state). But: the Reframe reveals one additional piece of evidence that was invisible while the player was committed to the wrong theory — something that only becomes legible when the original interpretive frame is abandoned.

This creates a meaningful cost-benefit: committing early means potentially faster progress toward action, but locks you into an interpretation. Being wrong costs time but reveals new evidence. Being right rewards decisiveness.

---

## 4.3 The Case of the Golden Idol (Color Gray Games, 2022)

Golden Idol is the most analytically demanding investigation game in recent memory. Its central mechanic: the player assembles a solution by filling in named blanks (who, how, why) from a field of discovered words. The solution isn't discovered — it's *synthesized*. The player gathers fragments and must construct the complete narrative, naming every element.

**What Golden Idol does exceptionally well:** It requires the player to *name* the theory, not just accumulate evidence toward it. This is qualitatively different from Evidence Track advancement: naming forces synthesis, forces the player to hold multiple interpretive elements simultaneously and produce a coherent account. The act of naming is harder and more rewarding than the act of finding.

**What Valoria's investigation proposal captures:** The Reconstruct action is the closest analogue — it's the "piece together a narrative" action. But in the current specification, Reconstruct is a roll that produces a finding, not a synthesis act that requires the player to construct the narrative.

**Proposal GI-I (Named Theory Synthesis):** The Reconstruct action is bifurcated into two mechanics. **Automatic Reconstruct** (existing, unchanged): the roll-based action that draws connections between Case Board nodes and advances the Evidence Track by representing a character's analytical capability (Cognition pool). **Named Theory Synthesis** (new): at any point after reaching Simple threshold, the player can attempt a Named Theory — selecting Case Board nodes and explicitly naming: the Actor (who), the Method (how), the Location (where), the Motive (why). Named Theory Synthesis does not require a roll — it requires the player to supply correct node selections. If the selections are valid (the evidence actually supports the named elements), the Investigation advances directly to the next threshold (Simple → Complex, or Complex → Structural). If the selections are invalid, the game reveals which element is unsupported ("Your evidence doesn't establish the method") without advancing. This creates a skill-test for the player, layered on top of the skill-test for the character. Players who correctly synthesize faster progress faster; players who cannot synthesize must rely entirely on the character's Cognition roll to advance. This is the game making the Reconstruct action available at two registers of difficulty — mechanical and epistemic.

---

## 4.4 Shadows of Doubt (ColePowered Games, 2023)

Shadows of Doubt is a procedurally generated detective noir in which every citizen of the city has a schedule, relationships, employment, and behavior. The investigation is not a curated puzzle — it's a genuine system query. The player learns the system's rules and applies them. Most critically: the world doesn't stop for the investigation. Schedules proceed, citizens interact, crimes can be committed while you're solving the previous one. The city is indifferent to your investigation.

**What Shadows of Doubt does exceptionally well:** (1) The world's independence from the player's investigation creates genuine immersion — the player is an observer/interloper in a system that doesn't know they're watching. (2) Investigation contamination: visiting a scene changes it. Citizens see you. Evidence gets disturbed. (3) The procedural city feels inhabited because everyone is doing something for a reason.

**What Valoria's investigation proposal captures:** The NPE's Drift NPCs (on time cycles) and the "NPCs talk to each other" season-end mechanic are the Shadows of Doubt elements in Valoria. These are correct and should be developed further.

**What Valoria doesn't yet capture:** Scene contamination. In Shadows of Doubt, your presence is evidence. In Valoria, the Surveil action adds Exposure (+2 Church Attention Pool), which is the detection-risk version of contamination. But physical investigation (Examine, Research actions) doesn't contaminate the scene. In a world where institutional investigation is a threat (Church Heresy Investigation, Altonian intelligence), the player's investigative activity in a territory should leave traces that NPC investigators can find.

**Proposal SoD-I (Investigation Contamination):** Scene graph nodes entered by the player gain a [Disturbed] state after a Fieldwork action is performed. Disturbed nodes:
- Remain disturbed until the following season (season-end accounting includes "scene state decay").
- Are detectable by NPC investigators if those NPCs enter the node (generated via NPE with Investigation or Surveillance Worldview, or as Priority 2 events for Church/hostile-faction characters).
- Produce +1 Exposure per Disturbed node visited in a Church-controlled territory (the player's investigation footprint is detectable).
- If an NPC investigator reaches a Disturbed node the player has been to, they gain Intelligence (a Conviction Wound source for the player character, flagged "faction suspect" in that territory).

The exception: Mending operations don't disturb the scene — they restore it. A practitioner who Mends while investigating leaves less trace than a practitioner who Pulls or Weaves. This creates a strategic asymmetry: the most careful investigators are the most restorative ones.

**Proposal SoD-II (NPC Schedules as Investigation Resource):** Anchor NPCs at major scene types (Church officials, Warden contacts, faction agents) have brief, discoverable schedules: three or four states across a season's time (at archive in the morning, at chapel at noon, at residence at evening, at private meeting at night — location and activity, not mechanical data). Discovering an NPC's schedule is the output of a successful Surveil action (not an Interview — observation, not questioning). Knowing the schedule tells the player when the NPC is unguarded, when they're accessible, when the Archive is unattended. This transforms Surveil from a mechanical action (roll for +2 Evidence, +2 Exposure) into an investigative planning tool. The Exposure cost is front-loaded on the observation; subsequent actions in the schedule's gaps cost less Exposure because they exploit known patterns rather than stumbling in blind.

---

# PART 5: LEARNINGS FROM PLAYER AGENCY GAMES

## 5.1 Kenshi (Lo-Fi Games, 2018)

Kenshi is a sandbox survival-RPG in which factions are physical entities in physical space — they patrol territories, attack on sight based on faction relationship, and respond to player actions based on local reputation, not peninsula-wide reputation. A character can be hated by the Holy Nation but trusted in a specific Holy Nation town if they've done the local leader a service.

**The critical Kenshi insight:** Reputation is spatially granular. The game tracks relationship with a faction at the *settlement level*, not just the global level. This creates situations where a faction's local representatives behave differently from the faction's aggregate stance toward the player — because the local representatives have local information.

**What this means for Valoria's Standing system:** Standing is currently a single 0–5 track per faction. It represents peninsula-wide reputation with the faction. But a character who has done significant work in Gransol should have a different relationship with the Church's Gransol administration than with the Church's central leadership — even if they've never met Himlensendt, the Gransol priests know them.

**Proposal K-I (Territorial Reputation):** Standing is bifurcated into two tracks: **Faction Standing** (peninsula-wide, the existing 0–5 track, modified by Duty completion and major actions visible to faction leadership) and **Local Reputation** (per territory, derived from the player's recent actions in that territory, 0–4, decaying −1 per season of absence). Local Reputation modifies NPC Disposition in the territory: a Local Reputation 3 character receives +1 Disposition from all NPEs generated in that territory regardless of faction alignment (the locals know you, and knowing someone is better than not knowing them). Local Reputation also modifies Exposure: high Local Reputation in a Church territory means the Church's local agents know who you are — you're visible, which cuts both ways (less hostile surprise, more targeted surveillance).

This doesn't add a new mechanical system — it adds a territorial modifier to existing Disposition and Exposure calculations. Implementation note: Local Reputation is generated from the count of positive interactions (Fieldwork actions, NPC Disposition improvements) minus negative interactions (Exposure triggers, conflict scenes) in the territory over the past two seasons.

---

## 5.2 Fallout: New Vegas (Obsidian Entertainment, 2010)

New Vegas is the finest implementation of faction reputation as active narrative generator. The core insight: reputation doesn't just open doors — at specific thresholds, it actively dispatches the world toward the player. Vilified with the Legion? Assassins appear. Idolized by the NCR? Soldiers help you in combat. Reputation is an attractor state — it shapes what the world sends at you.

**New Vegas also has the richest attribute expression in dialogue of any RPG.** High Intelligence doesn't just unlock "smart" dialogue — it provides a genuinely different interpretive frame. A high-Intelligence character interprets the same scene differently from a high-Charisma character, and the game makes both interpretations available as distinct dialogue options with distinct outcomes. The player's build choice is a character voice choice, not just a stat optimization.

**Proposal FNV-I (Standing as Attractor):** At Standing 3 (Counselor) and above, the player's faction generates unsolicited Scene Slate entries — faction-derived Priority 2 scenes that appear on the Slate without being assigned as Duties. These represent: (3) faction intelligence flowing to a trusted agent (a scene where a faction ally shares information they've gathered); (4) faction assets responding to the player's presence (a garrison commander at Standing 4 territory offers cooperation, unlocking a combat asset); (5) succession pressures generating unsolicited meetings (faction council members approach the player privately at Standing 5 to position themselves for the leadership transition). These are not Duties — they're the faction's relationship with the player becoming active rather than transactional.

At negative Standing (faction hostile), the equivalent fires adversarially: faction agents generate unsolicited Priority 1 hostility entries — surveillance, confrontation, interference with the player's scene investigations. The faction's Standing is tracking the player and responding to them across the peninsula.

**Proposal FNV-II (Attribute Voice in the Dialogue Lattice):** Attribute gates in the Dialogue Lattice should express character voice, not just option unlocking. A Cognition 4+ utterance shouldn't just be "available to Cognition 4 characters" — it should sound like a Cognition 4 character speaks: analytical, referential, structured. A Charisma 4+ utterance should sound like a Charisma 4 character: emotionally perceptive, socially aware, relationship-centered. The gate is the same; the flavor of the unlocked utterance expresses the attribute. This requires authorship (the dialogue writing must express attribute voice), not mechanics — but it's a specification that should govern how the Dialogue Lattice's utterance content is written.

---

## 5.3 Crusader Kings III (Paradox Development Studio, 2020) — Extended

The agency proposal correctly references CK3's dual-agenda structure. The deeper CK3 mechanic is the Scheme.

**CK3 Schemes:** A Scheme is a long-duration, background operation with a probability-per-month (based on your stats and your agent network), a secrecy rating (opponents can discover and counter), and an outcome state (success/detection/abandonment). Schemes run in parallel with your normal gameplay without consuming your immediate action budget — they're the medium-term consequence of your network investment.

**What Valoria's Beliefs partially capture:** A Belief like "I will forge a secret alliance between Varfell and the Restoration Movement" is structurally a scheme — it's a multi-season personal project. Currently, pursuing it requires spending scene actions directly. There's no background-process equivalent.

**Proposal CK3-I (Belief Schemes):** A player can optionally convert a Belief into an active **Scheme** once they have Disposition ≥ +2 with at least one NPC relevant to the Belief. A Scheme adds passive monthly advancement (automatic per-season probability check, Ob = standing obstacle) that doesn't consume scene actions but produces small incremental Evidence Track or Disposition gains. It also adds a counter-Scheme risk: if the Scheme's activities are perceptible to opposed NPCs, those NPCs may launch counter-Schemes that generate scene opportunities for them and potential Exposure for the player. A Scheme's progress is tracked on the Case Board as a long-duration investigation type. Activating a Scheme costs 1 scene action (the player formally begins the covert operation). It then runs in the background — the player can accelerate it with scene action investment but doesn't have to. This gives medium-term Belief pursuit a passive dimension that rewards player network investment without demanding scene action expenditure every season.

---

## 5.4 TTRPG Permanence-Emergence Mechanics

**Burning Wheel (Luke Crane, 2002):** The most directly relevant TTRPG. BW's Beliefs/Instincts/Goals architecture is the ancestral system for Valoria's Beliefs proposal. BW's key insight beyond structure: **Beliefs must face obstacles, and the player must pursue them under pressure, not when convenient.** The Artha (equivalent to Momentum) reward fires specifically when the character's Belief leads them into *danger* — a Belief pursued safely produces nothing. Valoria's Momentum award for "a genuine step toward the Belief" should have a difficulty calibration: the more costly the scene action (measured in Exposure, Wounds, Standing risk, or Relationship cost), the greater the Momentum yield.

**Proposal TTRPG-I (Belief Difficulty Scaling):** Belief Momentum rewards scale with cost:

| Belief pursuit context | Momentum yield |
|---|---|
| Pursued with no opposition | +0 (not a genuine test — the world didn't push back) |
| Pursued against opposition (a hostile NPC, a contested roll) | +1 (as proposed) |
| Pursued at personal cost (Wound taken, Exposure +2+, scene action that failed) | +2 |
| Pursued when it directly conflicts with active Duty | +2 (the tension itself is the game's engine) |
| Pursued in a scene where it produces visible negative consequence | +3 |

This makes the tension between Beliefs and Duties not just narratively interesting but mechanically incentivized — the player who allows their Belief to cost them something is rewarded with more Momentum than the player who safely separates their Belief from their Duty.

**Blades in the Dark (John Harper, 2017):** BitD's "position and effect" system — every action takes a Position (controlled/risky/desperate) and produces an Effect (limited/standard/great) — gives players precise information about what they're risking and what they're buying. Valoria's contest system (roll pool, degree of success, outcome table) does something similar but the "what am I risking right now" is sometimes buried in system knowledge.

**Proposal TTRPG-II (Scene Position Signal):** When the player enters a scene and selects a Fieldwork or Contest action, the UI/GM presents a brief Position/Effect summary: "Position: Risky (NPC is hostile, Disposition −1). Effect: Standard (you will gain 1 Evidence on success, partial evidence on partial success)." This is not a new mechanical system — it's a presentation layer that surfaces the existing success table in a more immediately legible format. In the videogame, this is the action preview UI. In the TTRPG, it's the GM's obligation to clearly state stakes before dice are rolled.

**Ironsworn (Shawn Tomkin, 2018):** Ironsworn's Vows are structurally closest to Valoria's Beliefs. The key Ironsworn insight: **progress tracks for Vows are separate from scene resolution.** You can advance your Vow progress without making a roll — by making decisions that commit you, by accumulating narrative justification. When you finally "Fulfill Your Vow," the roll is a climactic resolution that acknowledges all the progress you've made. This is different from Valoria's current Belief model where fulfillment is declared when it's achieved — there's no distinction between "I'm making progress" and "I've arrived."

**Proposal TTRPG-III (Belief Progress Track):** Each Belief has a three-step progress track (Established → Developing → Near Fulfillment) that advances independently of scene action outcomes. Advancing the track requires the player to declare: "This season's action advanced my Belief in [specific way]." The GM or game adjudicates whether the advance is valid (did the action genuinely move toward the Belief's obstacle?). At Near Fulfillment, the player triggers a Belief Resolution scene — a specific Zoom In moment where the Belief's test occurs. This scene's outcome determines Fulfillment (full Momentum + Echo) or Contradiction (Belief is revised with narrative acknowledgment of why it failed). The track makes Belief pursuit visible over time and prevents both premature fulfillment claims and indefinitely deferred Beliefs.

---

# PART 6: SCALABILITY — DWARF FORTRESS AND RIMWORLD

## 6.1 The Core Lesson

Both Dwarf Fortress (Bay 12 Games, 2006–present) and RimWorld (Ludeon Studios, 2018) are studied in game design primarily for one emergent property: **they generate stories that feel authored despite being entirely procedural.** The mechanism is identical in both: simple rules applied consistently to all actors at all scales, without exception.

DF doesn't have "interesting dwarves." It has dwarves with needs, memories, relationships, and skills who follow consistent behavioral rules. Interestingness emerges. RimWorld doesn't have "dramatic events." It has a colonist-state tracker, a world-state simulator, and a pacing AI that applies difficulty rules to the real-world state. Drama emerges.

The design implication for Valoria: **emergence requires that the rules apply to everyone, not just the player.** When a system produces special behavior only for the player, it is a scripted system wearing emergence's clothing.

## 6.2 Dwarf Fortress Lessons

**The Z-level depth principle:** DF's underground isn't just harder than the surface — it's categorically different. Different biomes, different threats, different resources, different physical laws (magma doesn't behave like water; certain ores only exist at certain depths). Depth in DF is a qualitative distinction, not just a quantitative one.

Valoria's Thread Depth axis (Fibonacci: 1, 2, 3, 5, 8, 13) is correctly structured as a scale, but its qualitative differences are underdeveloped. Higher Depth = higher Ob, which is correct. But *what is happening* at Depth 8 that is categorically different from Depth 2?

**Proposal DF-I (Qualitative Thread Depth Differentiation):** Thread operations at different Depth levels have qualitatively different properties and side effects beyond obstacle difficulty:

| Depth Range | Qualitative Domain | Side-Effect Profile |
|---|---|---|
| 1–2 (Surface) | Physical/material — objects, structures, somatic states | Local, reversible, fast-resolving. Weaving a surface thread stabilizes an object or body. Dissolution at this level is cosmetic. |
| 3–5 (Relational) | Social/institutional — relationships, roles, collective beliefs, memory | Medium-range, community-affecting, season-scale persistence. Weaving at this level affects the social fabric: an NPC's relationship with their community, an institution's coherence, a territory's cultural memory. Dissolution can unmake a relationship or a collective belief. |
| 8–13 (Primordial) | Consciousness/time/causality — the Einhir Catastrophe's substrate | Peninsula-wide, permanent without counter-operation. Touching these threads changes the peninsula's fundamental state. Weaving at Depth 8+ can prevent or accelerate the Catastrophe's recurrence. Dissolution at this level is what caused the original Catastrophe. POP operations at Depth 8 don't move individual events — they shift when entire epochs of consciousness began. |

This makes Thread depth a genuine strategic decision about what *kind* of operation the player is undertaking, not just how hard the operation will be. A practitioner choosing between Depth 3 and Depth 8 is choosing between affecting social fabric and affecting reality's foundations — a choice with fundamentally different consequences regardless of success degree.

**The fortress-as-character principle:** In DF, the fortress is an actor. Its population, its wealth, its history make it a presence that the world responds to. Long-running fortresses attract different threats than new ones; famous fortresses attract migrants, traders, and sieges.

**Valoria equivalent:** Territories under long-running player governance should become "known" — their reputation should attract different scene types. A Prosperity 4 territory the player has governed for three seasons should generate trade-alliance approaches (NPEs arriving with commercial interests) and rival-faction destabilization attempts (hostile faction agents targeting a visible success). The territory's history IS its attractor state, in the same way a DF fortress's fame is.

This is already partially specified: the agency proposal's Priority 4 (Territorial) and Priority 5 (World Momentum) generate scenes from territory state. The DF lesson is to make this more aggressive — a territory that has been significantly shaped by the player should generate significantly different Scene Slate entries than a neutral territory.

## 6.3 RimWorld Lessons

**The needs-as-narrative engine:** RimWorld colonists have needs (food, rest, recreation, social contact, beauty). These needs generate mood states. Mood states generate behavior. Behavior generates stories. The player doesn't experience "a colonist went berserk" as an event — they experience it as the consequence of accumulated neglect of a specific need over specific time. The story has a root cause that the player could have addressed, which makes it feel authored (they could have prevented it) without being scripted.

**Valoria equivalent:** NPC Conviction Wounds are already doing this correctly. A conviction wound is the accumulated consequence of sustained pressure on an NPC's worldview. Haelgrund's crisis (if it comes) is the result of accumulated contradictions between his hidden TS and his institutional role — not a scripted event. The design is correct. The challenge is making the accumulation visible enough that players feel the approaching crisis without it feeling telegraphed.

**Proposal RW-I (Conviction Wound Visibility):** NPC Conviction state is visible at different levels of Disposition depth. At Disposition 0–1, the player sees only the NPC's public position (Conviction unpenetrated). At Disposition +2, the player can Appraise (existing action) to reveal the NPC's Conviction Wound count and primary conviction. At Knot level, the player perceives the NPC's Conviction state directly — without an Appraise roll, because a Knot represents deep enough understanding that this knowledge is felt, not deduced. This is already philosophically consistent with P-15 (three-layer being-persistence) and PP-632 (Knot as the deepest relationship state).

**The pacing AI principle:** RimWorld's Cassandra Classic doesn't script events — she applies a time-weighted probability rule to the world state. When the colony is thriving, she increases the probability of harder events. When the colony is struggling, she slightly reduces it. The result is a consistent sense of escalating challenge that nevertheless feels responsive to the colony's specific situation.

**Valoria's equivalent:** The faction AI priority stack, combined with clock advancement, already provides something like RimWorld pacing. The existential question ("can anyone win before everyone loses?") is the design's Cassandra rule built into the clock mechanics. The holistic audit notes the correct calibration concern: Church wins 53% of simulations. This isn't a Cassandra problem — it's a faction balance problem. But the pacing architecture is correct.

**The colony composition principle:** In RimWorld, the colony's specific composition of colonists (their traits, their skills, their relationships to each other) creates the specific texture of each playthrough. No two colonies feel alike because no two compositions are alike.

**Valoria equivalent:** The NPC population at campaign start (which named NPCs are present in the player's starting territory, what their conviction states are, what their Disposition toward the player's starting faction is) should vary enough between campaigns to produce genuinely different starting textures. Currently, named NPCs have fixed starting states. The NPE generates variable minor NPCs but the named NPCs are static.

**Proposal RW-II (NPC Starting State Variation):** Named NPC starting states have a ±1 range on their Conviction Wound count and a ±1 range on their Starting Certainty (within a defined envelope that preserves their characterization). Haelgrund always starts with hidden TS and Church institutional role — but his Certainty might start at 4 or 5 (one notch of variation), and his first Conviction Wound may or may not be present at campaign start (one notch of variation). This produces four possible "versions" of Haelgrund at campaign start — all recognizably Haelgrund, but in different phases of his arc. Across 13 named NPCs with 2-bit starting variation, this produces 8,192 possible starting configurations — sufficient to make each campaign feel distinct without requiring procedural generation of the named characters.

---

# PART 7: SYSTEM-WIDE CONCERNS AND CROSS-PROPOSAL ISSUES

## 7.1 Cognitive Load Assessment

Both proposals are dense. The agency proposal introduces three new systems (Beliefs, Duties, Scene Slate) with full mechanical specifications. The investigation proposal introduces four (NPE, Investigation Interface, Dialogue Lattice, Response Matrix). An onboarding player encountering all seven systems simultaneously would have significant cognitive overhead.

**The proposals sequence correctly:** The agency systems are presented first and are simpler to understand (Beliefs = what I want; Duties = what I'm told; Slate = what's available). The investigation systems extend existing fieldwork and social mechanics. A new player could learn the agency systems in the first session without encountering the investigation systems at all.

**Critical concern:** The Dialogue Lattice's seven gate types are the highest cognitive load element of the investigation proposal. In the TTRPG, the GM can simplify on the fly. In the videogame, the player needs to understand what each gate means, what conditions unlock each category, and why some options are hidden while others are visible-locked. This is the UI/UX challenge most likely to produce friction and slowdown.

**Proposed mitigation:** Introduce Dialogue Lattice gates progressively. In the game's opening scenes, conversations use only Attribute and Disposition gates (the two most intuitive: do I have the stat, and do they like me enough). Evidence gates are introduced with the first investigation scene. Certainty and TS gates are not introduced until the player has encountered Thread reality (TS > 0). History gates are introduced when a character's History first becomes directly relevant in conversation. Belief gates are introduced when a Belief is first fulfilled. This is a tutorial-design consideration, not a mechanical change — the full system exists from the start, but the player only encounters complexity as their character's state expands into it.

## 7.2 The Fieldwork Resource Cost Gap

The holistic audit (§3.3) correctly identifies that Fieldwork has no health/resource parallel. Combat has Wounds/Stamina. Contests have Composure/Concentration. Thread has Coherence. Fieldwork has... Exposure (detection risk), which is not personal cost — it's external risk. A character can investigate indefinitely within a season with no personal depletion.

**Proposal FW-I (Investigation Fatigue):** Add **Acuity** as a fieldwork resource: (Cognition + Focus), recovered fully between seasons. Each Fieldwork action costs 1 Acuity. At Acuity 0: the character is Mentally Fatigued (+1 Ob to all cognitive fieldwork actions — Examine, Research, Reconstruct). At −3 Acuity (going negative through some impairment): Cognitive Overload (cannot perform Reconstruct, Evidence Track cannot advance until Acuity is restored). Social fieldwork actions (Interview, Connect) drain Composure instead of Acuity (social interaction is emotionally exhausting, not cognitively). Physical fieldwork (Surveil, Sneak) drains Stamina.

This completes the health/resource parallel table:

| System | Active resource | Fatigue state | Collapse |
|---|---|---|---|
| Combat | Stamina (End+1) | Out of Breath (−1 scene action) | Incapacitation |
| Social | Composure (Cha+6) | Rattled (+1 Ob) | Spent |
| Thread | Coherence (10→0) | Dissonant (Spirit check) | Rendering Crisis |
| Fieldwork | Acuity (Cog+Focus) | Fatigued (+1 Ob cognitive) | Cognitive Overload |

The amounts are calibrated so a full season of fieldwork (4 scene actions × 3 fieldwork actions per scene = 12 potential Fieldwork actions) depletes approximately half of a typical character's Acuity (Cognition 3 + Focus 2 = 5, so ~5 actions before fatigue begins). This means investigation is sustainable over a season but not unlimited — heavy investigators need rest scenes or social scene breaks, which is the natural rhythm of a real investigation.

---

## 7.3 The RM Actor Problem

The holistic audit (§4.5, ED-546) identifies that the Restoration Movement has no BG mechanical actor. The agency proposal's §8 notes that "an independent player aligned with RM pursues RM Beliefs without faction infrastructure." This is a partial solution: it specifies the player can be the RM actor, but it doesn't solve NPC-RM's lack of Domain Action capacity.

Both proposals acknowledge this without fully resolving it. The fullest resolution requires a decision: is RM a latent faction that the player/game activates, or is it a permanent minor faction present from the start? This is a Jordan-level design decision (J-3). But the investigation proposal's NPE Coalition embryo mechanic (Proposal IC-1 above) provides the mechanical substrate: if NPE Stance convergence produces Coalition embryos that can become formal Community Weaving actors, then RM formalizes organically from territory-level Piety drift and player/NPC-RM activity. RM doesn't need a permanent Domain Action hand — it needs the Coalition mechanic to fire when the conditions are met.

**This is the correct resolution and should be forwarded as a design decision recommendation:** RM emerges from the NPE Coalition system, not from a fixed faction structure. It is the only faction that is generated rather than given. This is philosophically consistent with P-15 (three-layer being-persistence) — RM is the cultural memory layer becoming organizational, not an institutional actor. The RM victory condition (Cultural Revolution: Piety ≤ 1 in 8+ territories, MS ≥ 40) becomes achievable when enough Coalition embryos have formalized and the player (if RM-aligned) has produced sufficient Domain Echoes from personal-scale RM activity.

---

# PART 8: WHAT MUST NOT CHANGE

Several elements of the existing design are excellent and should be insulated from modification. Identifying what to protect is as important as identifying what to improve.

**Do not change: The Sincerity Gate (Spirit TN 7 Ob 1, 37% failure).** This is the game's finest social mechanic. It is philosophically grounded, mechanically elegant, simulation-validated, and produces genuine player decisions. The investigation proposal's integration (tagging utterances [SINCERE]/[INSTRUMENTAL]) is the correct extension. The Sincerity Gate should not be softened, capped, or made optional.

**Do not change: Three-axis Thread Ob (Depth + Breadth + Distance).** This is the game's finest mechanical design achievement. It converts an abstract difficulty number into a meaningful statement about what the practitioner is attempting. The Depth Differentiation proposal (DF-I) extends it qualitatively without changing its structure.

**Do not change: The Conviction-to-AI Integration.** The three-step decision procedure (Institutional Filter → Conviction Filter → Decision Fork) is simple, deterministic, and produces emergent behavior. It is the game's cleanest example of the RimWorld/DF design principle. The Response Matrix extends it for conversational resolution — this is correct. The underlying procedure should not be complicated.

**Do not change: Domain Echo magnitudes (±1/±2).** These are small enough to ensure personal-scale actions don't dominate the faction layer, large enough to make personal play feel consequential. The Stature-Scaled Echo proposal amplifies at high Standing; the base magnitudes for early-game play are correctly calibrated.

**Do not change: The Knot system.** PP-632 is the best single design patch in the project's history. Disposition ceiling as floor(Bonds/2)+1, Knot as the maximum-Disposition deep relationship with remote Thread-Read and Coherence anchoring — this is mechanically elegant, philosophically grounded, and sim-validated. Any new proposal that touches relationships should work within this framework rather than around it.

**Do not change: Evidence Track thresholds (Simple 3 / Complex 5 / Structural 8).** These are well-calibrated and represent meaningful investigative stages. The Named Theory Synthesis proposal (GI-I) and Theory Commitment proposal (BH-I) work within these thresholds rather than replacing them.

---

# PART 9: PRIORITISED RECOMMENDATIONS

Ordered by: design integrity risk if not addressed (P1) → design quality opportunity (P2) → creative enrichment (P3).

## P1 — Structural Gaps (required before integration)

**P1-A: Resolve Counselor negotiation output (C-1).** Specify what a won/lost Duty negotiation produces in terms of Duty modification, Standing change, and NPC arc consequence. Without this, the Counselor tier is a dead end.

**P1-B: Formal Domain Echo Reference Table (DE-REF-01).** Write and commit a standalone Domain Echo specification with trigger conditions, magnitude table, and per-action-type outputs. This is the system's central cross-scale bridge and it has never been formally specified.

**P1-C: Belief tag structure (CS-1).** Replace "scan Belief text" with structured tag fields (up to three tags from [NPC], [Territory], [Faction], [System] categories). This is a 5-minute implementation decision with significant downstream robustness consequences.

**P1-D: Sparse Slate minimum guarantee (R-1).** Specify minimum Scene Slate composition: Priority 5 always produces ≥1 entry; if Priorities 1–4 produce <2 entries, add 1 NPE territorial event and 1 faction activity summary. Prevents dead seasons.

**P1-E: Investigation Contamination (SoD-I).** Specify [Disturbed] node state, its season-end decay, its detection by NPC investigators, and its Exposure consequence. This closes the Fieldwork-has-no-cost gap at the scene level and creates stealth/investigation tradeoffs.

**P1-F: Acuity resource for Fieldwork (FW-I).** Complete the health/resource parallel table. Fieldwork currently has no personal cost beyond Exposure (detection risk). Acuity (Cog + Focus), drained by cognitive fieldwork, fatigue state and collapse, recovers between seasons. This is one formula addition and one resource parallel, not a new system.

## P2 — Quality Improvements (high value, implement soon)

**P2-A: Add Instincts to character creation (A-I).** One conditional statement, automatic behavior, +1 Momentum for correct firing, -1 for voluntary suppression. This is a character-texture addition that costs nothing mechanically and produces memorable emergent moments.

**P2-B: World Pressure Slots (A-II).** Rename Priority 4/5 to Territorial Events and World Momentum. Priority 4 is generated from NPE without reference to player Beliefs or Duties. Priority 5 surfaces one peninsula-level event in the player's vicinity. Minimum 1 Priority 5 per season, non-player-centric. Addresses the "world orbits the player" risk.

**P2-C: Standing as Attractor (FNV-I).** At Standing 3–5, faction generates unsolicited Scene Slate entries (ally intelligence, asset cooperation, succession approach). At negative Standing, faction generates hostile Slate entries (surveillance, interference). Standing is an attractor state, not just a permission tree.

**P2-D: Named Theory Synthesis (GI-I).** Bifurcate the Reconstruct action into automatic Reconstruct (existing roll) and Named Theory Synthesis (player selects nodes and names Actor/Method/Location/Motive). Correct synthesis bypasses to next Evidence Track threshold; incorrect synthesis reveals which element is unsupported. Adds player-skill layer to investigation without replacing character-skill layer.

**P2-E: Ambient Node Layer (L-I).** Each scene graph node produces a passive ambient description on arrival. Anomalous ambient facts can mark a node [Suspicious], unlocking targeted Fieldwork actions. Pre-Fieldwork observation pass rewards careful play.

**P2-F: Theory Commitment and Evidence Reframing (BH-I).** At Simple threshold, player can commit to a named Theory. Subsequent evidence corroborates (track advances) or contradicts (tagged [Contradicts]). Three [Contradicts] tags invalidate the theory but reveal hidden evidence invisible under the wrong frame. Rewards decisiveness; makes being wrong valuable.

**P2-G: NPC Schedule Discovery as Surveil Output (SoD-II).** Surveil action can reveal NPC schedule (location × activity × time of day). Knowing a schedule is an investigation planning tool: it tells the player when to act, when to wait, which nodes are accessible at which times. Transforms Surveil from a mechanical Evidence grind into a scene-planning resource.

## P3 — Creative Enrichment (worthwhile, implement after P1/P2)

**P3-A: Qualitative Thread Depth Differentiation (DF-I).** Thread operations at Depth 1–2 affect physical/material. Depth 3–5 affect social/relational. Depth 8–13 affect consciousness/causality. Beyond Ob, what you're touching and what side effects you risk should differ categorically.

**P3-B: Belief Progress Track (TTRPG-III).** Three-step progress track (Established → Developing → Near Fulfillment) that advances independent of scene action outcomes, based on player declaration validated by GM/game adjudication. At Near Fulfillment, triggers a Belief Resolution Zoom In scene with climactic Stakes.

**P3-C: Belief Difficulty Scaling for Momentum (TTRPG-I).** Belief Momentum scales with the cost of pursuit: 0 (no opposition), +1 (opposed), +2 (personal cost), +2 (conflicts with active Duty), +3 (produces negative visible consequence). Mechanically incentivizes the tension between Beliefs and Duties.

**P3-D: Territorial Reputation as Local Reputation Track (K-I).** Per-territory Local Reputation (0–4, decays −1/season of absence) derived from recent interactions. Modifies Disposition for all NPEs in territory and Exposure calculation. Locates reputation in space rather than abstracting it to a peninsula-wide track.

**P3-E: RM via NPE Coalition emergence (resolves J-3 / ED-546).** RM formalizes from the NPE Coalition embryo mechanic rather than requiring a fixed faction structure. When NPE Stance convergence produces Coalition embryos on Thread/Piety issues, and the coalition exceeds a size threshold, RM gains formal faction status with Community Weaving as its Domain Action. This is the philosophically correct resolution: RM is cultural memory becoming organizational.

**P3-F: Case Board Citation in Social Contests (IC-2).** Upgrade Corroboration to Case Board Citation: player selects a specific Case Board node as evidence. Node type (Documentary vs Testimony) and Contest adjudicator type (Expert/Crowd) interact to determine Citation value (+1D or +2D). Different fieldwork approaches produce different contest advantages.

**P3-G: NPC Starting State Variation (RW-II).** ±1 range on named NPC Conviction Wound count and Starting Certainty at campaign start. Preserves characterization while creating ~8,192 distinct starting configurations across 13 named NPCs. Sufficient variation for distinct campaigns without procedural generation.

---

# APPENDIX: CONSOLIDATED PENDING DECISIONS

Items carried forward from the proposals, integrated with audit findings:

| ID | Decision | Urgency | Recommendation |
|---|---|---|---|
| NPE-01 | Ecology weight formula (continuous vs step-function) | Medium | Continuous. Step-function is simpler but loses information at midpoints (Piety 3 behaves identically to Piety 4 in a step model). |
| NPE-02 | Persistence ceiling for minor NPCs | Medium | 3 per territory per year, but soft-exit (not deletion) for NPCs with Disposition ≥ +2 or Conviction Wounds from player interaction. |
| DL-01 | Hidden vs visible-locked threshold | Medium | Attribute/Evidence/History/Disposition gates: always visible-locked. Certainty gates: hidden at >2 distance, visible-locked at ≤2 distance. TS gates: hidden at TS 0 (player shouldn't know these options exist before discovering Thread reality), visible-locked once any TS is acquired. |
| DL-02 | Lattice node count per conversation | Low | 3–5 utterances per node, 2–4 nodes per conversation. These are correct as proposed. |
| RR-01 | Filter hostile modifier stacking | Medium | Three concurrent hostile modifiers produce Social Non-Encounter (new outcome type — see IS-2 resolution). Two or fewer stack. |
| C-1 (new) | Counselor negotiation output | **P1** | Win = Duty modified/replaced + leader Conviction Wound +1. Loss = Duty unchanged + Disposition −1 + Succession Tension arc vectors. |
| DE-REF-01 (new) | Formal Domain Echo specification | **P1** | Commit as standalone reference per table in §3.2. |
| J-3 | RM actor resolution | Medium | RM emerges from NPE Coalition mechanic. Defer fixed faction structure. |
| J-4 | Lenneth/Elske/Haelgrund stance triangles | **P1** (existing) | These are editorial decisions; the Genome structure from the investigation proposal provides the format. Prioritize Haelgrund (39/40 spec, most mechanically active), then Lenneth (28/40, lowest spec, most undercharacterized). |

---

*End of audit. All proposals are in PROPOSAL status — this document does not canonize any recommendation. Each recommendation requires explicit approval before integration.*
