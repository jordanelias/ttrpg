# VALORIA — Integration Audit: Bridging Player and World
## Full Audit of the Integration Proposal Against All Nine Supporting Documents
## Focus: Companions, Non-Standard Actors, World Connection, Immersion Architecture
## Date: 2026-04-15-21-36

---

# EXECUTIVE SUMMARY

The integration proposal (valoria_integration_proposal.md) is the project's best single document precisely because it names the core failure honestly: two complete design layers — world physics and player physics — that have never been formally bridged. Its three proposed mechanisms (Domain Echo, Scene Slate, Dialogue Lattice) are the correct answer to that problem, and its formal Domain Echo Reference Table and Priority Recommendations are exactly what the project needs next.

What the integration proposal does not address, and what this audit exists to supply, is a third design layer that sits between the player and the world's formal political machinery: the layer of *personal relationship with worldly actors who are not factions in the parliamentary sense.* The Ministry, the Guilds, Niflhel, the Wardens, the Restoration Movement — and the question of whether the player can travel with companions, form their own political entity, or engage with these institutions through channels other than factional alignment — these are not edge cases. They are the texture of the world as the player will actually experience it.

The holistic audit rates Scale Transitions as ○/○/◐ — the weakest system. The RSE critique correctly identifies that only five Zoom In triggers exist for 120+ arcs. But the root cause of both failures is the same: the game currently only knows how to generate personal scenes from formal faction events. When the Guilds do something that matters, the player gets a reported intelligence entry. When Niflhel moves, there is no personal scene generated at all because Niflhel has no Scene Slate architecture. When the Wardens need help, the player finds out by accident or not at all. When the Ministry delays a Domain Action, the player sees a stat change with no human face.

This audit proposes a **Universal Actor Engagement Architecture** — a single coherent system that generates personal engagement with every named worldly actor regardless of their formal faction status, the player's faction alignment, or the political register at which those actors normally operate. It does not add systems; it extends existing ones.

The companion question is the emotional center of this architecture. Companions transform the game from a solo protagonist navigating a political world into something more akin to what Tyranny, Dragon Age, and Planescape: Torment discovered: that the richest political drama happens in the space between the protagonist and the people who travel with them. The Valoria design already has all the mechanical infrastructure for companions — Knots, Disposition, multi-character fieldwork, group combat, the Corroboration mechanic in Contests. What is missing is the specification that names what a companion IS and how the player forms and manages one.

**Five structural additions this audit proposes:**

1. **The Companion Specification** — a formal definition of what it means for an NPC to be a traveling companion, with action economy, scene integration, arc contribution, and combat/fieldwork rules derived entirely from existing mechanics.

2. **The Player Network Formation pathway** — a progression from independent operative to informal network leader, distinct from both faction membership and full faction creation, allowing players to build an organization from the bottom up.

3. **The Non-Standard Actor Engagement protocols** — specific, concrete interaction pathways for Ministry, Guilds (individual guild leaders), Niflhel (as a service network), and the Wardens (as a Thread-competence hierarchy), each with its own access mechanism, standing track, and Scene Slate generation.

4. **The Scene Slate Expansion** — twenty additional Zoom In trigger categories covering all worldly actors not currently represented, closing the gap from five to twenty-five-plus triggers without creating new mechanical vocabulary.

5. **The Immersion Continuity Specification** — a set of presentational rules ensuring that every mechanic in the game, regardless of the scale at which it operates, has a visible face: a person, a place, a conversation, a consequence the player can see.

Everything proposed here is derived from mechanics already in the design. Nothing requires a new resolution system, a new track, or a new dice mechanic. The game is complete. What it needs is connection.

---

# PART 1: WHAT THE INTEGRATION PROPOSAL GETS RIGHT (AND MUST NOT CHANGE)

Before identifying gaps, it is essential to affirm what the integration proposal correctly specifies. These are the fixed points around which the rest of this audit builds.

## 1.1 The World State Model as Substrate

The proposal's identification of the World State Model as the shared substrate for all systems is architecturally correct and must be protected. The three-scale model (Personal, Territory, Peninsula) is already implicit in the game's design — the proposal makes it explicit, which is what enables the integration architecture to function. Every new mechanic in this audit will declare its scale reads and writes against this model, as the proposal prescribes.

## 1.2 Domain Echo Directionality

The proposal correctly establishes that Domain Echo flows upward (personal → strategic) and that the strategic layer reaches the personal layer through Scene Slate and Zoom In triggers. This directionality is not merely organizational — it is phenomenologically correct. The player experiences the world as a consequence of their actions, not as a deterministic script. The player acts; the world responds. Reversing this channel (the world acting on the player through the same Echo mechanism) would make the game feel like it is telling the player what to do, which is precisely what the agency system exists to prevent.

## 1.3 The Sincerity Gate, PP-632, Evidence Track Thresholds, Three-Axis Thread Ob

The integration proposal correctly identifies these as protected elements. This audit agrees entirely. Every proposed mechanism in this document works within these foundations rather than around them.

## 1.4 The Formal Domain Echo Reference Table (Part 8 of Integration Proposal)

This table is correct and should be committed immediately. This audit extends it — it does not revise it. Extensions are clearly marked as additions, not substitutions.

## 1.5 The Priority Recommendations B-1 through B-5

All five blocking recommendations in the integration proposal are accurate and must be addressed. This audit adds further blocking items and high-value items in their appropriate priority tiers.

---

# PART 2: THE COMPANION SPECIFICATION

## 2.1 The Design Vacuum

Across all fifteen documents, there is no specification of what it means for an NPC to be a traveling companion of the player character. The NPC Recruitment procedure (npc_behavior_v30 §9.5) specifies how to recruit an NPC into a faction. The Knot system (PP-632, fieldwork_v30 §5.6) specifies the deep relational bond a player character can form with an NPC. The multi-character fieldwork rules (fieldwork_v30 §3.2) specify how multiple characters can cooperate in exploration. None of these three systems specify whether a Knot-bonded, faction-recruited NPC can physically accompany the player character through scenes and, if so, what they contribute.

This matters because the player's loneliness is the game's most significant experiential risk. The world is populated by NPCs with fully specified conviction triangles, arc maps, and compromise profiles. But the player currently experiences all of them as interlocutors, not as co-travelers. The difference between talking to Maret Vossen and traveling with Maret Vossen — between an NPC as a node in your investigation graph and an NPC as someone whose Beliefs you witness firsthand — is the difference between a political game and a story.

Dragon Age: Origins solved this by making companions react to world events through approval shifts, personal quest triggers, and party banter. Planescape: Torment made companions access unique scene content — Fall-from-Grace could enter social spaces others could not; Morte could contribute in undead contexts. Tyranny designed companions with their own factional loyalties that could conflict with the player's choices, creating a constant low-grade tension between personal relationship and political necessity. Valoria's design already has richer mechanical foundations than any of these predecessors. What it lacks is the formal specification.

## 2.2 Definition: What Is a Companion

A companion is a Knot-bonded NPC who has accepted an invitation to co-travel with the player character for a specified arc or indefinitely. The companion definition has three layers:

**Relational prerequisite:** The NPC must have reached Knot formation with the player character (maximum Disposition per PP-632). Knot formation already requires Disposition at floor(Bonds/2)+1, which means a player with Bonds 4 can form Knots with NPCs up to Disposition +3, while a player with Bonds 6 can form Knots at Disposition +4. The relational investment is not trivial. Companions are not recruited — they are earned.

**Acceptance condition:** The player offers co-travel as a distinct social action (Charisma pool, Ob 2, flavored as invitation rather than recruitment). The NPC's response is governed by their Conviction and active Beliefs. An NPC whose Belief directly aligns with the player's current arc accepts without resistance. An NPC whose Belief conflicts with the player's likely activities may accept conditionally or refuse. The refusal is not a failure state — it is character expression and generates an NPC arc update ("the player asked; I said no; why, and can that change?").

**Capacity constraint:** The player can have at most floor(Bonds/3)+1 active companions (minimum 1). This means a Bonds 3 character can have two companions; a Bonds 6 character can have three. This is not a party size cap in the RPG sense — it is a statement about relational carrying capacity. A person can only sustain a small number of genuinely close, co-traveling relationships simultaneously. The Bonds attribute already encodes relational depth and count via PP-632; the companion cap is a direct extension of that same principle.

## 2.3 The Companion Action Economy

The critical design question is: do companions consume the player's scene action budget? The answer must be no, for the same reason that an ally present in a scene does not consume the player's actions in any other game that has done this well. A companion contributes to scenes as a distinct actor within the scene's time budget. The player's scene action budget (3-5 per season per Agency System §6.1) governs the player character's activity; companions contribute through a separate but constrained mechanism.

**The Companion Scene Contribution (CSC) system:**

Each companion has one Contribution per scene, drawn from the following options. The companion's Primary Attribute and dominant Conviction govern which Contributions are available to them.

| Contribution Type | Attribute Pool | Effect | Available When |
|---|---|---|---|
| Assist Investigation | Primary Attribute × 2 | +1 Evidence Track progress on success (per existing multi-character exploration rule, fieldwork_v30 §3.2) | Any investigation scene |
| Contest Corroboration | Companion's Contest pool | +1D to player's Argue roll for one exchange | Social contest scene |
| Combat Support | Companion's Combat Pool | Companion fights as a named NPC combatant (existing named NPC combat rules apply) | Combat scene |
| Thread Assist (TS 30+) | Companion's Thread pool | Collective Thread operation (existing collective operation rules, fieldwork_v30 §2.4) | Thread operation scene |
| Social Access | Companion's Charisma | Companion's Disposition with a scene NPC provides bonus Disposition offset to player: if companion has Disposition +2 with target NPC, player gains −1 Ob on first social action | Social scenes with shared NPCs |
| Knowledge Contribution | Companion's Recall | Companion reveals one piece of their own lore relevant to scene (GM grants as free information, no roll required) | Any scene where companion's History is relevant |
| Watchkeeping | Companion's Attunement | Companion monitors for Exposure; player gains −1 Exposure per scene from companion's surveillance of approach routes | Stealth/Investigation scenes |

**One Contribution per companion per scene.** The player may suggest a contribution type, but the companion chooses based on their Conviction and what they find compelling about the scene. An Order-convicted companion will suggest Watchkeeping in an infiltration because maintaining safety is their instinct. A Reason-convicted companion will gravitate toward Knowledge Contribution because information is their currency. The companion's agency within their Contribution choice is what makes them feel like a character rather than a tool.

**Companions can also act independently.** On a roll of 5-6 on a d6 at each scene's opening (the GM rolls, or the game evaluates), the companion takes a self-directed action — pursues their own active Belief within the scene without being asked. This is the Dragon Age banter mechanism made mechanical: sometimes companions do what they want to do. The independent action consumes the companion's Contribution for the scene.

## 2.4 Companion Beliefs and Arc Contribution

Every companion retains their full NPC specification — Conviction triangle, active Beliefs, Compromise Profile, Arc Map — while traveling with the player. The companion's arc does not pause while they travel. In fact, co-travel is the fastest way to advance a companion's arc because the player character is physically present for the pressures that drive it.

**Three arc interaction types during co-travel:**

**Type 1 — Shared scene as arc moment.** When a scene touches a companion's active Belief directly (the player investigates the Church, and the companion is a latent Faith/Crisis type; the player defends a Restoration community, and the companion holds Equity conviction), the GM evaluates whether the scene constitutes an arc moment. If yes: the companion's Conviction engages, their Wound count may change, and the player has an additional social action opportunity within the scene — not an extra scene action, but a mid-scene conversational beat — to engage with the companion's shifting state. This is Disco Elysium's Kim Kitsuragi model: the companion reacts to what they witness, and the player can respond to that reaction within the ongoing scene.

**Type 2 — Companion Belief fulfillment.** When the player helps the companion fulfill their own active Belief (by choosing scene actions that serve the companion's goal, by presenting evidence the companion needed, by interceding in a social context the companion couldn't access alone), the companion's Belief progresses. Companion Belief fulfillment grants the companion +1 Conviction Wound resistance (they become harder to shake in their convictions, having been affirmed) and grants the player +1 Momentum from the relational investment, distinct from the player's own Belief mechanics.

**Type 3 — Companion Belief contradiction.** When the player takes actions that directly contradict the companion's Conviction or active Belief (betraying an RM community when the companion has Equity conviction; destroying evidence to protect a Church ally when the companion is a Reason-convicted skeptic), the companion's Disposition with the player shifts downward by −1 and a Conviction Wound activates in the direction of resentment rather than revelation. If Disposition drops below 0 through Belief contradiction, the companion stops traveling — not as a punishment mechanic, but as character expression. They have watched you do something they find intolerable. They leave. This is Baldur's Gate 3's most honest design insight: companions who can leave are companions who mean something.

## 2.5 Companion Combat Contribution

In personal combat, a companion fights as a named NPC combatant using their established stat profile. They have their own Combat Pool ((Agility × 2) + History + 3), their own Wounds threshold, their own initiative. They are not controlled directly by the player — the GM or game AI controls them through their Conviction-weighted behavior (an Order companion positions defensively; an Autonomy companion looks for escape routes or opportunistic strikes; a Faith companion may prioritize protecting a symbolic or spiritually significant target). The player can Issue Commands to their companion as a Priority 1 action in combat (before any other action), which modifies the companion's behavior for that round at Ob 1 (Charisma-based). Success = companion executes the commanded action. Failure = companion follows their own instinct.

The Fibonacci group combat bonus (combat_v30 §8) applies to companions as additional attackers. A player character with one companion fighting at the same target generates a +1D Fibonacci bonus on Offense. This is not a buff the game grants — it is the existing rule recognizing that group combat dynamics change with more participants.

**Companion wounds and recovery:** Companions track Wounds exactly as player characters do. At maximum Wounds: incapacitated (per combat_v30 Stage 1 incapacitation). A player character can Rescue a companion (existing Rescue action applies). An incapacitated companion cannot contribute to scenes until stabilized (Medicine Ob 2). Companion death is permanent: Wound maximum reached and not stabilized within scene = companion death, full NPC death mechanics apply (their arc ends, their Knot severs, the player character takes Coherence −1 from relational rupture per PP-632's established Knot severance consequences). This makes protecting companions a real tactical concern, not a softened RPG convention.

## 2.6 The Companion Dialogue Access Extension

The most valuable companion mechanic is also the most understated: a companion opens dialogue gates that would otherwise be unavailable to the player character.

In the Dialogue Lattice, utterances gated by History require the player character to have the relevant named History (fieldwork_v30 §5 Gate Type 5). But a companion with a relevant History standing at the player's side changes this. If the companion has History: [Church-Scholar] and the player does not, the companion can contribute the History-gated utterance directly — voiced in the scene as the companion speaking — as their Contribution for the scene. This requires Social Access or Knowledge Contribution as the Contribution type. The companion's History is not transferred to the player; the companion simply speaks.

This is mechanically simple and experientially transformative. It means bringing Maret Vossen into a territory with Piety 3 and Accord 2 doesn't just give the player a combat ally — it gives them access to Equity-conviction utterances in NPC dialogues that a player with Certainty 4 and no RM History would never see. The player's strategic decision of which companion to bring on which mission is itself a form of scene preparation, exactly as in Planescape: Torment.

---

# PART 3: PLAYER NETWORK FORMATION — THE PATH FROM OPERATIVE TO FOUNDER

## 3.1 The Design Gap

The player agency system (player_agency_v30.md §5) specifies a stature progression from Operative (Standing 0-1) to Successor (Standing 5) within an existing faction. The independent path (§5.3) allows the player to refuse faction alignment and pursue Beliefs alone. But neither path addresses the case that many players will naturally pursue: building their own organization from scratch, not by climbing an existing hierarchy, but by creating a new center of gravity in the world.

This is the Mount & Blade: Bannerlord experience: you start as a nobody, accumulate renown, build an army, establish territory, and eventually declare your own kingdom — not through a scripted story beat but through accumulated capability reaching a threshold where the world recognizes you as a political entity. Pathfinder: Kingmaker made this into a literal game layer: the player builds a barony, administers its territory, appoints advisors, and watches its Stability and Economy metrics as the kingdom grows.

Valoria already has every mechanical piece needed for this path. What it lacks is the formal specification that names it as a designed experience and connects the pieces into a coherent progression.

## 3.2 The Network Formation Progression

The path from independent operative to network founder proceeds through three stages. These are not levels in a game-mechanical sense — they are thresholds at which the player's accumulated relational capital produces emergent political recognition.

**Stage 1 — The Inner Circle (Personal Scale):** The player has at least two Knot-bonded companions (per the companion specification above) who share a common Belief or Conviction alignment with each other and the player. This is recognizable to the world as a nascent group with a shared purpose. It generates no faction mechanics — it is simply a social reality. NPE-generated NPCs who encounter the group read them through their ecology weights and assign a collective Disposition that may differ from their individual Disposition with the player character alone.

**Stage 2 — The Network (Territory Scale):** The player has Disposition ≥ +2 with at least five NPCs (named or NPE-generated, across at least two territories) who share a common Conviction or whose Beliefs align with the player's own. These relationships have produced at least one NPE Coalition embryo (per comprehensive audit Proposal IC-1: Stance convergence in a territory). At this threshold, the game generates a new Scene Slate Priority 3 entry each season: "Your network is becoming visible." This is not a scripted scene — it is a Priority 3 opportunity that reflects the NPE Coalition's social reality becoming legible. The scene offers the player a choice: acknowledge the network (accept a coordination scene with 2-3 network members) or continue operating diffusely (no scene, no acknowledgment, no network formalization).

**Stage 3 — The Founded Organization (Faction Emergence):** The player has maintained Stage 2 for three consecutive seasons AND has completed at least one Structural-threshold investigation (Evidence Track 8) whose subject directly concerns the organization's purpose AND has at least one territory where their network has ≥ 3 active Disposition +2 relationships. At this threshold, the NPE Coalition conversion fires: the network becomes a formal organizational actor with domain actions available.

The founded organization is not a full faction. It does not have a hand of six cards. It does not compete in Parliament by right. What it has is:

**One Domain Action per season:** chosen from a restricted list based on the organization's founding Conviction. A Reason-convicted organization can Survey and Investigate. An Equity-convicted organization can Organize (equivalent to Community Weaving at territory scale). An Order-convicted organization can Fortify and Govern in territories where they have established Presence.

**A Mandate track (0-3):** derived from the network's collective Disposition weight across territories. This Mandate can be used as voting power in Parliament only when the motion directly concerns the organization's domain. A Reason-based network can vote on intelligence-related motions. An Equity-based network can vote on motions affecting common population welfare.

**Standing conversion:** The player's existing Standing with the faction most closely aligned with their organization's Conviction transfers at half value (rounded down) to the new organization. A player who built Standing 4 with Crown before going independent and founding a Reason-based investigation network starts their network at Mandate 2.

**The ceiling:** Founded organizations cannot achieve the Universal Victory condition independently. They lack territory-based military and the full Domain Action suite. They can, however, become critical to another faction's victory — providing intelligence, managing Accord in territories others cannot reach, or destabilizing a rival at critical moments. Their strength is the strength of all non-hierarchical networks: adaptive, distributed, and genuinely hard to decapitate.

---

# PART 4: THE NON-STANDARD ACTORS — EVERY PATH HAS A DOOR

## 4.1 The Core Problem

The faction layer (faction_layer_v30) and the board game mechanics specify eight formal factions with priority trees: Crown, Church, Hafenmark, Varfell, Guilds, Niflhel, Löwenritter, and Restoration Movement. But the world of Valoria contains at least five additional institutional actors that are named in the design documents but have no formal player engagement pathway:

The **Ministry** (§7.6 of npc_behavior_v30) is defined in two sentences. It acts as a procedural bureaucratic friction mechanism. A player character has never been specified to be able to work for, subvert, access, or engage the Ministry in any personal scene.

The **Guild individual leaders** (§2.11 of npc_behavior_v30) are mentioned as a possibility ("Individual guild leaders can be recruited as sub-NPCs with their own Convictions") but never specified. No Genome structure is provided. No engagement pathway is defined.

The **Wardens** (§8.10 of npc_behavior_v30) have a full priority tree and a passing reference to "Warden Cooperation (WC) track" but that track is never defined, its advancement conditions are never specified, and the player's path to accessing Warden knowledge is reduced to "visit the Southernmost and survive."

**Niflhel** as a service network (vs. Niflhel as a player faction) has no engagement pathway for non-Niflhel players. The social_contest_v30 notes that Niflhel "cannot participate in Formal or Grand Contests" and has a "social toolkit" (§9.7) that is marked [EDITORIAL: ED-041 — full Niflhel social toolkit pending design]. This is one of the most important pending items in the entire design — Niflhel is the world's foremost intelligence and covert action network, and there is no mechanism by which a non-Niflhel player can hire them, buy information from them, sell information to them, or be approached by them with a service offer.

The **Schoenland/Altonian Vanguard** have priority trees (§7.7/§7.8 of npc_behavior_v30) but no personal scene architecture. A player character who visits Schoenland's trading posts or encounters the Vanguard in the field has no formal engagement pathway.

The following sub-sections specify each actor's engagement protocol in full.

## 4.2 The Ministry: Bureaucracy as a Force

**What the Ministry is:** A procedural NPC faction that can delay or obstruct Domain Actions via Procedural Objection (§7.6). It has Mandate ≥ 2 as the condition for firing, and defaults to "Routine Administration" otherwise. It is, in design terms, the civil service — the institutional friction that exists between the political will of factions and their actual execution.

**What the Ministry needs:** Three things. First, a face — named Ministry officers who generate NPE entries in the capital territory (T1, Valorsplatz). Second, an engagement pathway for players who want to work with or within the Ministry. Third, a set of specific service transactions that any player can access regardless of faction alignment, because bureaucracy serves everyone (at a price).

**The Ministry Engagement Protocol:**

Ministry officers are generated by the NPE with a fixed template: Order-convicted (primary), Precedent-convicted (secondary), Compromise Profile: Political (exchange formal procedure for political consideration) or Informational (grant access to records in exchange for other records). Their Genome has one fixed field that no other NPE type has: a **Procedural Access Level (PAL 0-3)** representing their authority within the Ministry hierarchy.

Players engage the Ministry through three routes:

**Route 1 — Public Service:** Any player character can present themselves at a Ministry office in a Crown-controlled territory and request access to public records (archives, property records, land grants, military musters, historical documents). No roll required for Surface and Settled depth (Depth 0-1). Research action (existing fieldwork mechanic) required for Hidden depth (Depth 2). This is the Ministry as it actually functions — a public institution that provides public services. The player doesn't need faction alignment to access it. They need to show up and ask.

**Route 2 — Restricted Access:** Ministry records at Buried depth (Depth 3) require a PAL 2+ officer's authorization. Obtaining this authorization is a social scene: Interview (Attunement pool) against the officer's Ob, modified by the player's faction's Mandate relative to the Ministry's home territory. A player from a faction with Mandate ≥ 4 gets Ob −1. An independent player with no faction Standing gets Ob +1. The Ministry is not ideologically neutral — it exists within the political structure and responds to political weight. But it is not impossible for independents to access. It is simply harder.

**Route 3 — The Ministry as Ally:** A player who completes a Complex-threshold investigation touching Ministry corruption, inefficiency, or institutional failure, and presents the findings to a PAL 3 Ministry officer, triggers an arc vector: "Ministry Internal Reform Pressure." This arc can produce Domain Echo at Peninsula scale (Ministry restructuring affects all factions' ability to obstruct each other's Domain Actions via Procedural Objection) and generates a Scene Slate Priority 2 entry for 1-2 seasons: the Ministry officer who received the evidence is now a named NPC with a specific Conviction Wound and will appear as an Anchor node in subsequent Ministry-territory scenes.

**Scene Slate generation from Ministry activity:** Ministry Procedural Objections generate Priority 4 entries ("The Ministry has delayed your faction's Domain Action for one season — there may be a way to address this personally"). Ministry records that contain investigation-relevant material generate Priority 3 entries aligned with active Beliefs targeting institutional or historical subjects.

## 4.3 The Guilds: Individual Leaders as Sub-NPCs

**The structural problem:** The Guildmaster Council is specified as a collective with "no single leader" and "Moral Relativism" as its ethical framework. This is politically correct — the Guilds are a coalition of commercial interests, not an autocracy. But it makes personal engagement with "the Guilds" feel like engaging with an abstraction rather than a person.

**The solution:** Individual guild leaders are distinct sub-NPCs, each governing a specific commercial domain. Each has their own Conviction triangle, their own Beliefs, and their own Compromise Profile. The Council's Moral Relativism is the aggregate of these individual positions, not any single leader's conviction. This means that approaching "the Guilds" as a monolith produces Moral Relativism responses (Consequence-resonant, economically framed). But approaching a specific guild leader produces an individuated Conviction response.

**The Guild Leader NPC Template:**

Five guild leaders are specified (covering the five major trade domains of Valoria). Each follows the standard Genome format with a fixed Compromise Profile of Economic (primary) and either Informational or Personal (secondary, determined by the leader's Conviction).

| Guild Domain | Typical Conviction | Access Condition | Special Offering |
|---|---|---|---|
| Maritime (Hafenmark-adjacent) | Autonomy (trade freedom) | Port territory Disposition +1 with any merchant NPC | Navigation Intelligence — routes, schedules, cargo manifests |
| Textile & Agricultural | Equity (fair exchange) | Rural territory Disposition +1 with any farmer/artisan NPC | Supply chain information — who produces what, where it goes |
| Arms & Metals | Order (contract law) | Military territory or faction Military ≥ 3 in player's territory | Equipment access — purchasing weapons and armor outside normal acquisition |
| Scholarly & Archive | Reason (knowledge access) | Research action Overwhelming in any territory with an Archive POI | Restricted archival access — Depth 2 records at reduced Ob |
| Shadow (covers smuggling, information, gray market) | Autonomy (operational freedom) | Niflhel Disposition +1 OR Tribune Spy action Success in any major city territory | Under-the-table services — see §4.4 Niflhel crossover |

**Engaging Individual Guild Leaders:**

Individual guild leaders generate NPE entries in their primary territory. They are treated as Drift NPCs (on a seasonal schedule rather than daily — they travel between territories for trading purposes, discoverable via Surveil in trade route territories). Once found, they are Anchor NPCs for the duration of their presence in the territory.

The player engages them through standard fieldwork Socializing actions (Connect, Negotiate, Read). The guild leader's Compromise Profile makes them straightforwardly transactional: they want something in return for what the player wants. The economic exchange doesn't require a social contest — it requires a Negotiate action (Attunement pool, Ob = floor(leader's highest stat / 2) + 1) where the player declares their offer and the game adjudicates whether the offer matches the leader's Profile.

**Domain Echo from Guild leader engagement:** Successfully negotiating with a guild leader and providing a service of value to them (delivering information, completing an escort duty, resolving a threat to their supply chain) produces a Guild Favour token — a named, specific institutional debt from that guild domain. Guild Favour tokens can be spent in place of Wealth for Domain Action Ob reduction in that domain's primary territory (+1D to Trade Domain Actions), or presented to Parliament as evidence of commercial backing (when the player or their faction has a parliamentary motion, presenting a Guild Favour token gives +1 to the vote weight in that motion, representing commercial interest alignment). Guild Favour is not a permanent faction stat — it decays at the rate of −1 per two seasons if not renewed through ongoing relationship. Guilds are transactional; so is their goodwill.

## 4.4 Niflhel: The Information Economy

**The central failure:** Niflhel is currently a faction that players can align with or face as an adversary. But Niflhel's most important function in the real world — and in the world's political ecology — is as a service provider to everyone. Information brokers don't serve one side. They serve whoever is paying. The Holistic Audit notes that Niflhel's AI Priority Tree (§8.8) has the NPC operating as a seller of services. But there is no buying-side specification. The player can commission Church intelligence through the Tribune Investigate card. They cannot commission Niflhel intelligence through any formal mechanism.

**The Niflhel Engagement Protocol:**

Niflhel operates through three access tiers, each requiring different conditions.

**Tier 1 — Open Market (Exposure 0-2 in any major city):** The player character has heard that certain taverns, certain couriers, certain gray-market merchants act as conduit points for the Quiet network. Rumour (social fieldwork action, Charisma pool, Ob 2 in any city territory) produces a lead to a Niflhel contact point. This is not yet access — it's a map reference. The contact point is an Evidence node in the city's scene graph.

**Tier 2 — Brokerage Contact:** At the contact point, the player initiates contact with a Niflhel intermediary. The intermediary's Genome is fixed: Autonomy-convicted, Compromise Profile: Economic and Informational. The player can purchase one of three service types per contact:

| Service | Cost | Mechanical Output |
|---|---|---|
| Intelligence Purchase | 1 Wealth (player's faction) or 1 Domain Echo sacrifice (one season's Echo result is surrendered to Niflhel as payment in kind) | One Tribune Spy result against a faction of the player's choice, delivered as a named intelligence package — specific stat values revealed |
| Covert Access | 1 Wealth OR Complete a Minor Cession-equivalent social task for Niflhel within the season | −2 Ob on one Expose action in a specified territory for one season |
| Disinformation | 2 Wealth OR Provision of genuine intelligence about a rival faction | Niflhel plants false information in a specified rival faction's intelligence network — that faction's next Tribune Investigate returns false results |

**Tier 3 — Arm Contact (Named Actor Access):** The player has completed at least two Tier 2 transactions with positive outcomes (no Exposure resulting) AND has a Niflhel Disposition track of +2 through repeated reliable dealing. At this tier, an Arm Leader — a named sub-NPC within Niflhel's four-arm structure — makes themselves available. The Arm Leader functions as a full named NPC with a Genome (Autonomy primary, Continuity secondary, Evidence and Consequence as Resonant Styles). The Arm Leader offers Tier 3 services (Assassination, Disappear — the two Niflhel-specific faction card actions described in mass_battle_v30 §B.4) as personal-scale equivalents, and can become a companion candidate (if Disposition +4 is reached through sustained reliable dealing — a near-impossible bar given Niflhel's default wariness, but not theoretically foreclosed).

**Niflhel Scene Slate generation:** Niflhel generates Scene Slate Priority 1 entries only when the player is in immediate danger from a Niflhel operation (the NPC Priority Tree §8 Priority 6 fires: Exposure containment). Otherwise, Niflhel generates Priority 5 entries ("Someone has been asking questions about you in [territory]") that the player can pursue or ignore. The player never knows for certain whether the questioner is Niflhel or another faction. This ambiguity is Niflhel's fundamental design principle: they are invisible, and invisibility is the service.

**The crucial asymmetry:** When the player purchases Niflhel services, they generate Exposure in the territory where the contact point is located (+2 per transaction, existing rule). They also generate an entry in Niflhel's intelligence file about their own operations — they become a known quantity to the network. This is the shadow cost of the information economy: using it means being in it. A player who regularly buys from Niflhel is in Niflhel's records. If an opposing faction ever gets access to those records (via their own Tribune Spy action against Niflhel, an unlikely but possible outcome), they will find the player character listed as a recurring buyer.

## 4.5 The Wardens: Thread Competence as Currency

**The design failure:** Edeyja has a full arc map and a priority tree. Warden Cooperation (WC) is mentioned in fieldwork_v30 §8.1 (Survey action can trigger WC +1 when WR ≥ 2) and in npc_behavior_v30 §8.4 (Varfell Priority Tree references "Warden Cooperation track WC" and "Warden Recognition WR"). But neither the WC nor WR tracks are formally defined anywhere. What do they measure? What do they require? How does a player advance them? What do they unlock?

**The Warden Engagement Protocol:**

The Wardens operate on a single economy: Thread competence. They have no interest in political allegiance, wealth, or institutional standing. Their only measure of a person is what they can do with threads and whether they have the discipline not to make things worse. This makes them the most meritocratic institution in the game and the most philosophically consistent with the Foundations — they are defined entirely by their relationship to the Thread substrate, not by politics.

**Warden Recognition (WR, 0-5):** The WR track measures how aware the Wardens are of the player character as a Thread practitioner of note. It advances through demonstrated Thread competence in territories where Wardens operate.

| WR Threshold | Condition | Effect |
|---|---|---|
| WR 0 | Default | Wardens treat the player as an unknown potential threat |
| WR 1 | Surviving a Southernmost approach (any territory adjacent to T15 with TS ≥ 20) | Wardens know the player exists; Edeyja's priority tree notes the approach |
| WR 2 | Completing a Mending operation (Success or better) in any territory at Depth 3+ | Wardens recognize Thread-restorative practice; Warden NPCs in that territory shift Disposition from neutral to +1 |
| WR 3 | Completing a Structural investigation whose subject is Thread phenomena; OR surviving a Breach (Depth 5) encounter without losing Coherence | Warden Cooperation becomes available — Wardens will cooperate on shared operations |
| WR 4 | Physical presence in Southernmost (T15) and surviving at least 2 scenes; TS must be ≥ 30 | Edeyja's arc enters "Assessment" phase — she is actively evaluating the player |
| WR 5 | Edeyja's personal Assessment (a dedicated Social Contest in the Southernmost, with Edeyja as sole adjudicator, Evidence-resonant, Thread demonstration required as Corroboration) — Success or better | Full Warden Recognition; player character acknowledged as a practitioner worth training |

**Warden Cooperation (WC, 0-3):** WC measures the operational relationship between the player character and the Warden group. It is distinct from WR (awareness vs. partnership).

| WC Level | Access Granted |
|---|---|
| WC 0 | No cooperation; Wardens operate independently |
| WC 1 | Wardens share intelligence about Gap sites and Thread Tension accumulations in territories the player is in or adjacent to (Priority 4 Scene Slate entries) |
| WC 2 | Cooperative operations: a Warden joins the player's Thread operation as a supporting practitioner (existing Collective Thread operation rules apply); the Warden's TS bonus contributes to the collective pool |
| WC 3 | Full partnership: Edeyja makes herself available as a companion candidate (requires WR 5 and player Coherence ≥ 7 — she will not travel with someone who is already near their rendering's edge); Warden knowledge transfer becomes a Scene action type (Teach: Edeyja transfers Thread understanding, advancing player TS by 10 per scene, maximum two advances from teaching) |

WC advances through completed cooperative operations (any joint Thread op at WC 1+ that achieves Success). WC decays −1 if the player creates a Gap through Dissolution in any territory the Wardens maintain — they observe this and it costs the relationship. WC never advances above the player's WR level (you cannot be a Warden partner before you are recognized as a competent practitioner).

**Scene Slate generation from Warden activity:** At WR 1+, Warden activity in the Southernmost-adjacent zone generates Priority 4 entries during MS band transitions. At WR 3+, Warden emergency response to a Gap formation generates Priority 1 entries (the world is in crisis, the Wardens are responding, the player can be part of that response). At WR 5, Edeyja herself generates Priority 2 entries (the senior practitioner alive has things she wants to discuss) — these are never urgent but always significant.

## 4.6 The Restoration Movement: The Leaderless Faction

**The known gap (J-3 / ED-546):** RM has victory conditions but no mechanical actor in BG mode. The player agency system notes that "an independent player aligned with RM pursues RM Beliefs without faction infrastructure." The integration proposal's resolution (IC-1: RM emerges from NPE Coalition) is philosophically correct but mechanically incomplete.

**What needs to be specified:** The comprehensive audit's IC-1 proposal (NPE Coalition embryo → formal faction) provides the emergence trigger. What's missing is the specification of how RM operates for a player who is aligned with it before formal emergence, during emergence, and after.

**The RM Player Path:**

**Before RM emergence:** A player aligned with RM operates as an independent (per Agency System §5.3) but with one addition: the RM Community Weaving action (from threadwork documentation) is available as a scene action whenever the player is in a territory with Piety ≤ 1 AND at least three NPE-generated NPCs who have Equity or Continuity conviction. The Community Weaving scene is a multi-character fieldwork scene (one leader + up to two assistants per existing multi-character rules) where the player leads a collective Thread restoration. This does not require the player to have TS 30+ — Community Weaving is the one Thread operation that is accessible to non-practitioners (per the philosophical grounding in P-15: cultural practice, not individual Thread manipulation). Non-practitioner players use a Charisma pool instead of Spirit for Community Weaving, reflecting the social dimension of collective cultural memory rather than individual Thread contact.

**RM emergence activation:** When the NPE Coalition embryo threshold is reached (Stance convergence in a territory, per IC-1), and the player is a Standing-0 operator in RM alignment, the player IS the Founding Agent — the person whose accumulated relationships and demonstrated commitment to the community's welfare is the catalyst for the coalition's formalization. The Founded Organization mechanics (Part 3 of this audit) apply, but with the RM's specific Equity/Continuity Conviction profile governing available Domain Actions: Community Weaving, Organize (Presence marker expansion), and Founding Speech (equivalent to Senator Outward with pool derived from the player's Charisma + Belief track progress rather than faction Mandate).

**After RM emergence:** The founded RM organization has Mandate 1 and one Community Weaving Domain Action per season. The player character is simultaneously a personal-scale operative AND a political actor for an organization they created. This is the only case in the game where the player's personal achievements (Belief fulfillment, Disposition with community NPEs, successful Community Weavings) directly create faction-layer capability rather than echoing upward to a faction they serve. The Domain Echo for RM players is reversed: their faction-layer actions (Organize, Community Weaving at faction scale) generate downward effects (territory Accord improvements that the player then witnesses as scenes) rather than upward effects. The player controls the organization; the organization serves the community; the community generates scenes the player inhabits. This is the Rawlsian social contract expressed as game architecture.

## 4.7 Schoenland and the Altonian Vanguard

These are not permanent actors the player engages with throughout a campaign — they are conditional actors whose engagement becomes relevant at specific clock thresholds (IP ≥ 40 for Schoenland diplomatic pressure, IP ≥ 75 for Altonian Vanguard deployment).

**Schoenland:** A Schoenland trading post is an Anchor node available in port territories (any territory with maritime trade access). At IP < 40, the Schoenland traders are mundane commercial contacts (Compromise Profile: Economic, no political dimension). The player can buy, sell, gather market Rumours, and build Disposition. At IP ≥ 40, the Schoenland traders become political contacts: their Conviction shifts from Autonomy (trade freedom) to Order (maintaining the Accord they are party to), and a diplomatic conversation becomes available where the player can receive early intelligence about Altonian intentions. This is the game's only warning system for Altonian invasion — it can only be accessed through sustained Schoenland relationships, not through faction intelligence.

**Altonian Vanguard:** When the Vanguard deploys (IP ≥ 75), they generate Priority 1 Scene Slate entries in their deployed territory. An individual Vanguard commander is a named sub-NPC (Conquest-convicted, Evidence-resonant — he responds to demonstrations of military incapacity or capability). The player can engage the Vanguard commander through the Social Contest system (Cognition-primary, Expert Judge adjudicator, Projection-primary genre: the conversation is about what will happen if they advance or withdraw). A successful Grand Contest against the Vanguard commander generates a one-season Truce and reduces IP by 3 — a personal diplomatic achievement with peninsula-scale consequences.

---

# PART 5: THE SCENE SLATE EXPANSION — TWENTY-FIVE ZOOM IN TRIGGERS

The holistic audit identifies five Zoom In triggers as the most critical gap. The RSE critique rates Scale Transitions at ○/○/◐. The integration proposal correctly notes that the Scene Slate IS the Zoom In system. What follows is a complete taxonomy of Zoom In trigger categories, expanding from five to twenty-five, with the generator condition and scene type for each.

Note: These are not twenty-five separate scripted events. They are twenty-five trigger categories, each of which can produce any number of specific scene graph instantiations based on the current world state. The trigger defines what type of scene fires; the world state determines what specific NPCs, territories, and stakes populate it.

## 5.1 Trigger Taxonomy

**Category 1-5 (Existing — retained unchanged):**
The integration proposal's five existing triggers (NPC arc moment, territory crisis, clock threshold, discovery event, player-initiated) are retained as Priority 1 entries and are correct.

**Category 6 — Occupation Territory Scene:**
*Generator:* A territory the player's faction controls enters Occupation status (Trigger 1 in faction_layer_v30 §1.2).
*Scene type:* Resistance Scene (per integration proposal Part 5 Gap 2 — specified correctly there; included here for completeness in the full taxonomy).

**Category 7 — Parliamentary Vote Affecting Player:**
*Generator:* A Parliamentary Motion names the player's faction, and the vote will resolve next Accounting.
*Scene type:* Lobbying opportunity — the player can spend a scene action meeting with undecided faction representatives to shift the vote. Social Contest (Charisma-primary) against the representative's Conviction generates a Lobbying Offset (±1 to the vote, per existing Parliamentary Offset mechanics).

**Category 8 — Ministry Procedural Obstruction:**
*Generator:* Ministry Procedural Objection fires against the player's faction's Domain Action.
*Scene type:* Bureaucratic Engagement — the player can meet the Ministry officer responsible (a PAL 1-2 NPC, procedurally generated) and resolve the obstruction through evidence (Research action revealing the procedural basis for the objection) or social action (Negotiate, Ob 2, to reach an administrative resolution). Success removes the obstruction. Failure means the obstruction stands for the season.

**Category 9 — Guild Leader Commercial Disruption:**
*Generator:* A relevant guild's commercial interests are threatened by the current political situation (Parliamentary Blockade affecting trade, battle in a trade territory, treaty terms restricting commercial routes).
*Scene type:* Commerce Crisis — the player can meet the relevant guild leader (now elevated to Priority 2 urgency) and either negotiate a mutual protection arrangement (Guilds provide Domain Echo support in exchange for player intervention) or simply gather intelligence about what has disrupted commercial flow (Examine or Research action revealing territorial economic information).

**Category 10 — Niflhel Operation Detected:**
*Generator:* A Tribune Spy action (player's faction or NPC faction) reveals a Niflhel Quiet operation in the player's territory.
*Scene type:* Intercept opportunity — the player can pursue the evidence trail to identify the Niflhel operative (Investigation scene, Evidence Track 3) before Niflhel covers it, potentially establishing a forced negotiation (if the operative is cornered, Niflhel offers information in exchange for the player's silence — this IS a Tier 2 transaction initiated by Niflhel rather than the player).

**Category 11 — Warden Emergency:**
*Generator:* Gap formation in any territory, OR MS drops below a band boundary, AND the player has WR ≥ 2.
*Scene type:* Warden Response — the player is contacted by a Warden (the contact is generated as an Anchor NPC in the player's current territory, having traveled to find a practitioner) with urgent intelligence about the Thread situation. This scene always generates WC advancement opportunity if the player cooperates with the Warden's assessment.

**Category 12 — Companion Belief Crisis:**
*Generator:* The player's traveling companion has reached a Conviction Wound from an in-world event the companion witnessed (even off-screen, per the "Reported Layer" in the companion's experience).
*Scene type:* Companion arc moment — the companion initiates a conversation (in the player's current territory) about what they've seen or heard. This scene uses the Dialogue Lattice with the companion as the primary NPC, and the player's choices affect the companion's arc direction. This is the Dragon Age companion personal quest mechanic expressed through the existing Dialogue Lattice system.

**Category 13 — NPC Coalition Convergence:**
*Generator:* NPE Stance convergence produces a Coalition embryo (per audit IC-1) in a territory where the player has Disposition +1 with at least two of the converging NPCs.
*Scene type:* Organization moment — the player witnesses (or is invited into) the social coalescence. This is the scene where a new political actor is being born at the grassroots level. The player can accelerate it (committing their own Belief and spending a scene action to formally lead the conversation) or observe it (gaining intelligence about the emerging coalition without committing). Leading the conversation may make the player the de facto founding figure; observing produces Priority 4 entries for the next 2 seasons as the coalition continues to develop.

**Category 14 — Certainty Crisis:**
*Generator:* The player character's Certainty shifts by 2+ in a single season (a rapid ontological transition from Thread encounter, a decisive social contest victory/defeat on a Thread-relevant topic, or witnessing a Threadcut being).
*Scene type:* Rendering Moment — the player's character needs to process what they have experienced. The scene is not a combat or investigation scene — it is a contemplative scene where the player can choose one of three responses: Anchor (seek out a Knot-bonded companion or NPC; succeeds in stabilizing Certainty at the new value without further movement); Resist (Spirit roll Ob 2; success = Certainty returns by 1 toward its previous value; failure = Certainty moves further in the direction of the shift); Accept (no roll; Certainty settles at its new value and the character gains +1 Thread Pool Score from the integration). This is the game's most philosophical scene type — it acknowledges that changing what you believe about reality is its own experience, not just a stat change.

**Category 15 — Belief Near-Fulfillment:**
*Generator:* The player's Belief Progress Track (per comprehensive audit Proposal TTRPG-III) reaches Near Fulfillment.
*Scene type:* Belief Resolution Zoom In — the climactic scene in which the Belief is tested. The scene graph is specifically generated around the Belief's subject: if the Belief names an NPC, that NPC is an Anchor node; if it names a territory, the scene is in that territory; if it names a system (Thread, Church, Parliament), the scene involves a representative of that system in active confrontation with the player's position. This is the most player-authored Zoom In trigger — it fires because of what the player decided to pursue.

**Category 16 — Founding Organization First Test:**
*Generator:* The player's Founded Organization completes its first Domain Action.
*Scene type:* Organization consequence — the Domain Action's result is presented to the player as a personal scene. If the Organization Organized in a territory, the player is present in that territory when the Organizing's effects become visible (new NPE-generated NPCs with shifted conviction weights; existing NPEs whose Disposition to the player shifts based on the Organization's actions). The player didn't just push a button — they see what their organization did.

**Category 17 — Schoenland Diplomatic Warning:**
*Generator:* IP crosses 40.
*Scene type:* Intelligence scene — a Schoenland trading contact (existing Tier 1 relationship) initiates contact with information about Altonian preparations. If the player has Disposition +1 with at least one Schoenland NPC, this scene is Priority 2. If the player has no Schoenland relationships, this scene is Priority 4 and more vague.

**Category 18 — Vanguard Command Encounter:**
*Generator:* IP crosses 75 and the Altonian Vanguard deploys.
*Scene type:* Border scene — the player's character is in or adjacent to T10 (Spartfell) or T3 (Lowenskyst) during the Vanguard's advance. The Vanguard commander generates as an Anchor NPC. This is the only scene that can produce a Truce through personal diplomacy.

**Category 19 — Thread Debt Threshold:**
*Generator:* The player's own Thread Debt reaches a threshold value (drawn from threadwork_v30, Thread Debt mechanics).
*Scene type:* Thread consequence — a co-movement result from a previous Thread operation manifests in a way that demands personal attention. The scene is generated from the specific actualized auto-effect that was deferred from the operation (per threadwork_redesign_v25 §3.2 three-dimensional auto-effects). The player cannot choose to ignore this scene; it appears as Priority 1.

**Category 20 — Riskbreaker Activity:**
*Generator:* Löwenritter Coup Counter reaches 1 or 2.
*Scene type:* Covert contact — Torsvald (the active Riskbreaker) generates as a Drift NPC in the player's territory. If the player has TS ≥ 20, Torsvald is recognizable through Thread perception. If not, he appears as an ordinary traveler whose Anchor behavior is slightly anomalous (the Ambiguity Node Layer per Lacuna audit Proposal L-I). Torsvald's Compromise Profile includes Political (information about Crown's internal instability) — he is willing to share if the player demonstrates credibility.

**Category 21 — Elske Hostage Arc Moment:**
*Generator:* Crown Stability ≤ 2 AND Löwenritter Military ≥ 5 (hostage situation potential).
*Scene type:* Diplomatic intervention scene — Elske (hostage NPC, audit score 24/40, zero characterization) generates as an Anchor NPC in a Löwenritter-adjacent territory. This is the scene that should define Elske as a character rather than a stat. Her conviction (undetermined but developable through play) is revealed through a Dialogue Lattice session. The player's intervention can produce either a Solidarity-resonant personal arc for Elske or a Consequence-resonant change in how both Crown and Löwenritter perceive the player character's role.

**Category 22 — Cardinal Schism:**
*Generator:* Church Stability ≤ 2 (internal schism potential per §2.13 of npc_behavior_v30).
*Scene type:* Church internal scene — one of the four Cardinal sub-NPCs (Fortitude, Justice, Prudence, Temperance) generates as an Anchor NPC in Church territory. Each Cardinal approaches the player with different Conviction (per §2.13 table) and different agenda. The Cardinal of Temperance is most likely to offer genuine information about Thread-adjacent scholarly findings. The Cardinal of Justice is most likely to threaten. The player can engage any Cardinal through the standard Dialogue Lattice. A successful social scene with any Cardinal during a Church schism event produces Priority 2 Domain Echo for two seasons (the schism's resolution is influenced by what the player learns and with whom they share it).

**Category 23 — Vaynard Arc B Epistemic Seduction:**
*Generator:* Vaynard's TS crosses 30 (active practitioner threshold) from environmental exposure and he has not been directly engaged by the player.
*Scene type:* Intelligence crisis — Vaynard's Thread awakening without guidance produces the AUD-NPC-02 Knot strain propagation (§5.0b of npc_behavior_v30) in any NPCs Knotted to Vaynard. The scene presents the player with a situation in Varfell territory where the Thread substrate is showing signs of unguided practitioner activity. This is the scene that, if the player investigates, leads to the Vaynard Arc B discovery and the subsequent opportunity to guide or oppose his awakening.

**Category 24 — Himlensendt's Crisis Evidence:**
*Generator:* Church Attention Pool ≥ 5 in any territory AND the player has a Complex-threshold investigation into Church activities.
*Scene type:* Cardinal of Temperance produces scholarly findings (AER ≥ 3 condition per Himlensendt Arc B). The player can encounter this evidence — presented as an Archive POI access scene — and recognize that it represents a genuine Crisis of Faith opportunity for Himlensendt if delivered correctly. This scene connects the player's investigation (existing Evidence Track) to a named NPC arc that can reshape the Church's political trajectory.

**Category 25 — Founding Game-End:**
*Generator:* Any faction reaches Victory Condition threshold, or any shared loss clock reaches terminal value.
*Scene type:* Convergence scene — the game's climax is always a personal scene, not a stat screen. The player is in a territory when the decisive moment occurs: Crown Treaty ratified (the player witnesses the ceremony, or hears about it through a companion, or is in the territory where the final combat resolved it). Church Theocracy declared (the player watches the Graduated Seizure of the final territory — or fights it). Rupture beginning (the player character witnesses the Thread substrate failing in the Southernmost, and must choose their final personal action in a world that is ending). Every victory condition should resolve as a scene the player's character inhabits, not as a game-over screen. The design already has the architecture for this; the scene graph for the end state needs to be authored.

---

# PART 6: THE DOMAIN ECHO REFERENCE TABLE — EXTENDED FOR ALL ACTORS

The integration proposal's Part 8 table is correct. The following extensions cover actions involving non-standard actors that are missing from the original table. Add these rows to DE-REF-01.

| Action Type | Sufficient Scope Condition | Echo Target | OW | Success | Partial | Failure |
|---|---|---|---|---|---|---|
| Ministry access — Buried depth records | Records reveal faction-level intelligence | Faction Influence (discovery delivery determines recipient) | +2 Influence to delivering faction | +1 Influence | Narrative: player knows; faction doesn't | Record access burned; Ministry officer marked Suspicious to player |
| Guild Favour acquisition | Guild Leader negotiation succeeded | Commercial domain resonance | +2D to next Trade Domain Action in guild's primary territory | +1D to next Trade Domain Action | Favour token held; no active bonus | Favour offered was rejected; leader Disposition −1 |
| Niflhel intelligence purchase | Purchased intel is faction-level (stat revelation or covert operation) | Faction Intelligence (purchasing faction) | Exact stat value + one hidden Domain Action revealed | Stat value revealed | Approximate stat range | False intelligence purchased; player faction acts on bad data |
| Warden cooperative Mending | Joint operation at WC 2+ | MS | +2 MS (joint operation amplifies existing Mending magnitude) | +1 MS | No MS change; WC maintenance | Mending fails; −1 WC |
| RM Community Weaving | Piety ≤ 1 territory scene with community participants | Piety drift acceleration; Accord | Piety −1 immediate; Accord +1 in territory | Piety drift rate +1 (accelerated next season's calculation) | Territory NPE ecology weight shifted toward Equity/Continuity | Player character Exposure +3 if Church territory; investigation flagged |
| Companion Belief fulfillment | Player action directly enables companion's Belief | NPC arc trigger; companion Conviction state | Companion arc advances; player gains +2 Momentum; NPC related to companion shifts Disposition +1 | Companion arc updates; +1 Momentum | Companion's Belief progress +1; no external effect | Companion arc stalls; Disposition −1 with companion |
| Founded Organization Domain Action | Organization completes its first successful action | Territory state (per action type) | Organization's Domain Echo equivalent to Standing 3 (per Stature-Scaled Echo) | Standard OW magnitudes | Narrative shift in territory | Organization Mandate −1; founding momentum loses credibility |
| Schoenland diplomatic scene | Player talks Vanguard commander into Truce | IP | IP −3; Truce established for 1 season | IP −1; Altonian advance delayed | No mechanical effect; player has met the commander | Vanguard commander hostile; IP +1 (perceives weakness in opposition) |
| Niflhel covert access (Tier 2) | Player uses purchased access for an investigation action | Investigation Exposure (reduction) | −3 Exposure from the Niflhel-assisted scene; evidence gathered at Ob −2 | −2 Exposure; standard evidence gathering | −1 Exposure; no Ob benefit | Access compromised; player Exposure +2; Niflhel aware of failure |
| Cardinal Schism engagement | Player successfully engages a Cardinal during Church Stability ≤ 2 | Church Stability; TC | Engaged cardinal's Conviction Wound advances; Church Stability −1 next season; TC advance halted this season | Cardinal's arc updates; TC advance slowed next season | NPC arc information gained; no mechanical effect | Cardinal reports the approach; player Exposure in Church territory +3 |

---

# PART 7: THE IMMERSION ARCHITECTURE — HOW EVERYTHING FEELS PERSONAL

## 7.1 The Integration Proposal's Core Achievement

The integration proposal's statement in Part 13 is the design's north star: "A player should be able to pick up Valoria and experience, within the first four hours: someone they've met and cared about making a decision that has consequences they can see. A territory they've moved through changing in a way that reflects what they've done in it. An investigation revealing something that reframes everything they understood about a character. A conversation that starts as exploration and becomes confrontation because the world has weight and meaning and doesn't simply yield when pushed."

Everything in this audit exists in service of extending that statement to the game's full cast of actors. A player who engages the Ministry should feel the same thing: I met a person who works in that institution. I did something. It mattered. A player who buys information from Niflhel should feel: I was in that tavern. I spoke in low tones to someone who knew things. The transaction was mutual and slightly dangerous.

## 7.2 The Three Presence Rules

Every worldly actor, regardless of formal faction status, must satisfy three presence rules in the game's design. These are not mechanical specifications — they are authorial specifications. They govern how the design is written.

**Rule 1 — Every institution has a face.** No Domain Action resolves without a person attached to it. The Ministry's Procedural Objection is an officer named in the scene. The Guild's commercial leverage is a guild leader with a Conviction triangle. Niflhel's intelligence purchase is an intermediary with physical presence. This is not a simulation overhead — it is the game insisting that politics is always made of people. The player doesn't fight the Ministry; they argue with the officer. The player doesn't buy from Niflhel; they transact with a face that exists in the world.

**Rule 2 — Every consequence has a scene.** Domain Echo fires as a stat change, but stat changes must be anchored to witnessed events. When the player's faction Influence increases from a successful investigation, the player should be able to see that increase in a world event — even if they don't directly witness the Domain Action, the Reported Layer (per integration proposal Part 7) delivers the event in human terms. "Baralta used the evidence you delivered in Parliament. Himlensendt's motion failed." The stat changed because of what the player did, and the player knows it.

**Rule 3 — Every actor has a tempo.** Faction priority trees fire at Accounting. NPE season-end events fire at Accounting. But worldly actors are present throughout the season, not just at accounting moments. This is the Shadows of Doubt principle: everyone has a schedule. A Schoenland trader visits port territories quarterly. A Ministry officer processes applications on a weekly cycle that the player can Surveil to learn. A Warden moves between Gap sites on a patrol schedule the player can discover through Research in the Southernmost-adjacent territories. The discovery of an actor's tempo is itself investigative information — and using that information to be in the right place at the right time is the game's core skill.

## 7.3 The Companion as Immersion Engine

The single most powerful immersion tool available to the game is a well-specified companion. Not because companions are combat helpers (they are) or investigation assistants (they are) or dialogue-gate openers (they are). But because a companion is a continuous, present, reacting witness to everything the player does.

When the player reads a Territory's Accord as 2 on a stat screen, they understand something abstract. When their Maret Vossen companion witnesses a militia checkpoint detain an unarmed farmer and says something that reflects her Equity conviction — unprompted, as a companion independent action — the player understands something felt. The mechanic and the experience are the same thing. This is what the design has been building toward.

The companion specification in Part 2 of this audit is therefore not a quality-of-life feature. It is the immersion architecture made concrete. The companion is the world's commentary on the player's choices, delivered in real time, by a character with their own convictions. No tutorial prompt, no UI notification, no stat change explains what the world thinks of what you just did as clearly as a companion who turns to you after the scene and says, through their conviction and their history, what it meant.

## 7.4 The Visibility Model Extended for Non-Standard Actors

The integration proposal specifies three visibility modes (Dark, Perceived, Named) for World State values. This model extends directly to non-standard actor engagement:

**Ministry activities:** Dark by default. Perceived as bureaucratic friction ("your Domain Action was delayed — someone in the capital is objecting"). Named only when the player meets a Ministry officer directly or completes a Research investigation into the specific obstruction.

**Guild movement:** Dark for individual guild leaders' locations and schedules. Perceived as market fluctuations (Prosperity changes in trade territories, visible on the territory map without explanation). Named when the player has Disposition +2 with any guild leader and has met them in person.

**Niflhel operations:** Dark always at Tier 0. Perceived only as anomalies in scene ambiance (the Ambient Node Layer per audit Proposal L-I: in a tavern scene, a patron leaves earlier than their schedule would suggest; a document has been moved from where it was yesterday; an Anchor NPC is nervous without visible cause). Named only at Tier 2+ contact and only for the specific arm the player has dealt with.

**Warden presence:** Dark below WR 1. Perceived as Thread substrate anomalies visible to characters with TS ≥ 10 (the Thread layer in the Investigation Interface shows Mending traces — someone has been working in this territory). Named at WR 2+ when direct contact occurs.

**Schoenland:** Perceived from any port territory (trade goods, merchant ships are visible). Named through active social engagement.

This tiered visibility ensures that the world always communicates with the player, but always at the right depth for what the player has earned the right to understand.

---

# PART 8: GAPS IN THE INTEGRATION PROPOSAL — SPECIFIC CORRECTIONS AND EXTENSIONS

## 8.1 Part 3 Gap 3 (Parliament + Personal Layer) — Extension for Non-Standard Actors

The integration proposal's resolution is correct (Standing 3+ players can declare Parliamentary Intent). It is incomplete in one respect: the Guilds and Ministry are parliamentary actors that the current specification doesn't address.

**Extension:** Guild Favour tokens (specified in §4.3 of this audit) function as parliamentary capital. When the player presents a Guild Favour token as evidence of commercial backing during a Parliamentary session, it modifies the vote distribution: the relevant guild's Mandate weight shifts by +1 toward the player's faction's position for that specific motion. The Ministry's Procedural Objection mechanic can be invoked by any faction that has successfully engaged the Ministry as an ally (through Route 3 in §4.2 of this audit). A player who has achieved Ministry ally status can direct one Procedural Objection per season against any faction's Domain Action without consuming a scene action — the Ministry acts on its own institutional logic, informed by the player's facilitation.

## 8.2 Part 3 Gap 6 (NPE → Named NPC Interface) — Extension for Niflhel

The integration proposal specifies Named NPCs as Ecology Anchors (their conviction shifts ecology weights). Niflhel has a special case: their Named NPCs (Arm Leaders) are deliberately invisible in the ecology, not anchors. The Niflhel Arm Leader's ecology contribution is negative ecology weight for Niflhel-aligned worldview expressions — Niflhel's very presence in a territory suppresses visible Niflhel activity. Instead, Niflhel Arm Leaders shift ecology weights toward higher Volatility across all worldview types (the hidden power creates social instability even when invisible). This means territories where Niflhel is active are slightly more socially volatile — NPCs are slightly more susceptible to conviction shifts — regardless of which direction those shifts take. Niflhel doesn't create a worldview; it creates conditions for worldview destabilization.

## 8.3 Part 4 (Investigation Experience) — Extension for Companion Investigation

The integration proposal's three investigation registers (Physical, Social, Thread) each gain a companion dimension. A companion with relevant History can contribute to Physical investigation through the Knowledge Contribution action (free information from their background). A companion with high Attunement provides automatic Appraise assists in Social investigation (the companion's read of the NPC is available to the player before the player's own Appraise roll). A companion with TS ≥ 30 can extend the Thread investigation register (their Thread perception adds to the collective Thread-Read, per existing collective operation rules). The companion doesn't eliminate the need for the player's own investigation — they expand the space of what's investigable.

## 8.4 Part 9 (Social Contest in Videogame) — Extension for Non-Standard Actors

The integration proposal's Style Decision UI (four options in plain language) is correct and must be implemented. The extension for non-standard actors: each non-standard actor has a specific default Style preference that the player can discover through prior Appraise actions.

| Actor | Default Style Preference | Discovery Method |
|---|---|---|
| Ministry officers | Cite the record (Citation) | Research action in their territory reveals administrative procedure preference |
| Guild leaders | Show the future (Vision — economic consequences) | Rumour action in any trade territory reveals guild commercial orientation |
| Niflhel contacts | Anchor the fear (Insinuation) | Cannot be reliably predicted — Niflhel contacts read their interlocutor, not the other way around |
| Warden Edeyja | Cite the record (Citation) — but only Thread-verified evidence counts; she ignores testimonial evidence | WR 4 assessment scene reveals her evidentiary standards |
| Schoenland traders | Show the future (Vision — commercial futures) | Disposition +1 with any Schoenland NPC reveals their commercial-outcomes orientation |

## 8.5 Part 12 Priority Recommendations — Additional Items

The following items are additions to the integration proposal's Priority list, slotted into their appropriate tiers.

**Blocking (B tier) additions:**

**B-6: Companion specification commit.** The companion specification (Part 2 of this audit) must be committed as a standalone formal specification before videogame integration of any NPC relationship system. The action economy, arc contribution, and combat rules are all derived from existing mechanics — this is an organizational and editorial task, not a design task. But without the formal specification, every system that touches NPC relationships will implement companions differently or not at all.

**B-7: Warden track formal definition.** WR and WC tracks must be specified with advancement conditions, decay conditions, and unlock effects before the Southernmost can be implemented in the videogame. Currently the Southernmost has no formal player engagement pathway beyond "visit and survive."

**B-8: Niflhel service protocol formal specification (ED-041 resolution).** The social_contest_v30 flags ED-041 as "full Niflhel social toolkit pending design" at P2 priority. Given Niflhel's centrality to the game's intelligence economy and its unique ability to serve any faction, this is blocking for a well-connected game world. The Tier 1/2/3 protocol in §4.4 of this audit is the proposed specification; it requires formal approval and commit.

**High Value (H tier) additions:**

**H-7: Ministry face specification.** Define three named Ministry officers (one per authority tier: PAL 1, 2, 3) with Genome entries. These are the Ministry's permanent NPE Anchor nodes in T1. Without specific named Ministry NPCs, the Ministry remains an abstraction despite the Protocol specification.

**H-8: Guild leader Genome entries.** The five guild leader templates in §4.3 of this audit need their Genome fields filled with specific Conviction choices, active Beliefs, and Compromise Profile details. This is authorial work, not mechanical design.

**H-9: Individual companion compatibility matrix.** For each named NPC who is a companion candidate (those who can reach maximum Disposition with a player character under any faction alignment), specify whether the companion's Conviction will generate tension with specific player faction alignments. A Church-aligned player traveling with Vaynard (Reason conviction) will experience constant companion friction on Thread-adjacent choices. This friction is not a bug — it is the game's richest design space. It needs to be explicitly designed rather than emergent from unspecified conviction interactions.

**Creative Enrichment (E tier) additions:**

**E-6: Niflhel companion arc.** Reaching Niflhel Tier 3 and Arm Leader Disposition +4 is the most unlikely deep relationship in the game. If it occurs, the Arm Leader companion has the most distinctive arc of any companion: their Autonomy conviction creates constant tension between their institutional service obligation and their personal relationship with the player. When the player asks them to do something that violates Niflhel operational security, the companion has a genuine choice — their institution or their Knot. This is the game's most morally complex companion arc and should be explicitly designed as such.

**E-7: Community Weaving as a companion-led scene.** A Maret Vossen companion (RM-aligned, Equity conviction) who is in a territory with Piety ≤ 1 can initiate a Community Weaving as their independent action (companion's companion Belief alignment with the RM cause). This means the player can witness a Community Weaving without leading it — they can assist someone else's Thread-cultural practice, which is a qualitatively different experience from their own and reflects P-03's claim that Thread operations are consciousness-performed. What does it feel like to watch someone else perform Thread work you can barely perceive?

**E-8: The Warden deathwatch arc.** npc_behavior_v30 §8.10 specifies that "Warden count reaches 0" is an Arc C trigger for Edeyja. If the player has WR 5 and traveling companions with Thread capability, this means the player witnesses the last Warden standing — and potentially becomes a Warden themselves, the first outsider to join the order. This is not a designed event in any current document. It should be. It is the most narratively significant Thread outcome in the game: the moment the world's only Thread containment system passes from one generation to the next.

---

# PART 9: THE ELEGANT RESOLUTION — ONE SYSTEM, ALL ACTORS

The game's design vision — that the simulation and the story are the same thing — is best expressed in a single sentence: **every named actor in Valoria should be reachable by any player character through some path of genuine engagement, and every genuine engagement should produce a consequence the player can see.**

The systems in this audit — companions, non-standard actor protocols, Scene Slate expansion, Domain Echo extension — are not additions to the game's complexity. They are the game's existing mechanics applied consistently to every actor in the world rather than only to the eight formal factions. The Ministry is engaged through Research and Negotiate actions, exactly as any NPC is. Niflhel is engaged through Rumour and contact-point fieldwork, exactly as any secret organization would be. The Wardens are engaged through demonstrated Thread competence, exactly as a master-student relationship should work. Guild leaders are engaged through economic exchange, exactly as commercial relationships function.

The companion specification adds no new mechanic. It names the Knot relationship as a traveling relationship and specifies how existing fieldwork, combat, and contest rules apply to a companion who is physically present. The Founded Organization path adds no new mechanic. It identifies the threshold at which the player's accumulated Disposition network constitutes a political reality, and specifies the moment at which existing Domain Action mechanics become available to that reality.

What this audit adds is not complexity. It adds completeness. The game has a hundred doors. This audit builds the paths that lead to all of them.

---

# PART 10: CONSOLIDATED RECOMMENDATIONS

## Priority 1 — Blocking (implement before videogame integration)

**B-1 through B-5** (per integration proposal): Domain Echo Reference Table, Scene Slate/Scene Graph unification, Dialogue Lattice → Contest handoff, stability trigger → Scene Slate coupling, J-7 territory scale resolution. All remain correct.

**B-6:** Companion specification formal commit.

**B-7:** Warden WR/WC track formal definition.

**B-8:** Niflhel service protocol formal specification (ED-041 resolution).

## Priority 2 — High Value

**H-1 through H-6** (per integration proposal): all retained.

**H-7:** Ministry named officers specified (three NPCs, PAL 1-2-3).

**H-8:** Guild leader Genome entries filled.

**H-9:** Companion compatibility matrix for faction-alignment tensions.

**H-10:** Twenty-five Zoom In trigger taxonomy committed (per Part 5 of this audit).

## Priority 3 — Creative Enrichment

**E-1 through E-5** (per integration proposal): all retained.

**E-6:** Niflhel Arm Leader companion arc explicitly designed.

**E-7:** Companion-led Community Weaving scene type specified.

**E-8:** Warden deathwatch / succession arc authored.

---

# APPENDIX: THE QUESTION OF PLAYER-FORMED FACTIONS — DESIGN RECOMMENDATION

The user's question is: should players be able to form their own factions? The answer is yes, and the mechanism is the Founded Organization pathway in Part 3 of this audit. But the answer comes with a crucial design caveat.

Player-formed factions that compete symmetrically with established factions (Crown, Church, etc.) would require the player to spend years of in-game seasons building from Mandate 1 to the parliamentary weight needed to contend for Universal Victory. This is Mount & Blade: Bannerlord's endgame: possible, but time-consuming to the point of being a specific game mode choice rather than a natural character arc.

The more immediate and more interesting possibility is **the player as network leader rather than faction founder** — an organization that is indispensable to others' victories rather than capable of its own. A well-run Founded Organization with Mandate 2-3 and deep territory relationships is a kingmaker, not a king. The player who builds one is playing a different game than the player who serves a faction, and a different game than the player who goes fully independent. It is the game that Disco Elysium wanted to tell — the self-made person of no institutional standing who nevertheless changes everything — expressed through Valoria's political simulation rather than a single-city mystery.

The formal faction question (reaching Mandate 5, competing for universal victory) is a late-game path that the Founded Organization architecture makes mechanically possible but intentionally difficult. The design does not need to make it easy. It needs to make it *real* — and a real path to power for a player who builds genuine relationships, completes genuine investigations, and accumulates genuine capability over the course of a full campaign is exactly what the Founded Organization pathway provides.

The answer to "can players form their own factions?" is: yes. The game calls it a Founded Organization. It grows from your Knots, your Beliefs, and your relationships. It is limited enough to be compelling — not a cheat code to victory, but a lever on the world that no pre-established faction gives you. And it is entirely made of the people you chose to walk alongside.

---

*This audit is a design critique and proposal. All new specifications are in PROPOSAL status and require explicit approval before integration into canonical documents. The Domain Echo table extensions (Part 6), Non-Standard Actor Protocols (Part 4), and Companion Specification (Part 2) are proposed as the primary actionable deliverables alongside the integration proposal's own B-1 through B-5 priority recommendations.*

*End of audit.*
