# VALORIA — Player-World Bridge: System-by-System Integration Overview
## Date: 2026-04-16
## Scope: Full mechanical review of all systems. Focus: how does the player experience the world's physics, and how does the world register the player's agency?
## Method: Every system evaluated on two axes — (1) does the world surface itself to the player through this system? (2) does the player's action in this system propagate back into the world? Gap identification, precedent critique, consolidation proposals.
## Status: WORKING DOCUMENT — launchpad for revision work

---

# PART 0: THE DIAGNOSIS

Valoria has two complete, internally excellent design layers. They are not connected.

**Layer 1 — World Physics.** The faction layer, conviction track, peninsular strain, clocks, NPC priority trees, military layer, calamity radiation, territory ecology. These systems describe a world that moves according to its own logic. Factions pursue priorities. Clocks tick. Territories change hands. NPC convictions shift under pressure. The world is alive and it does not care about the player.

**Layer 2 — Player Physics.** Player agency (Beliefs, Duties, Scene Slate), fieldwork (investigation, socializing, exploration), combat, social contests, Thread operations. These systems describe what a player *does* — how they fight, talk, investigate, and manipulate the metaphysical substrate.

**The gap:** Layer 1 generates events. Layer 2 generates actions. The translation layer between them — how events become opportunities and how actions become consequences — exists in fragmentary form across six documents written in parallel, never unified, and partially contradictory. The three proposed bridge mechanisms (Domain Echo, Scene Slate, Dialogue Lattice) are each specified in different places at different levels of completeness. Domain Echo has the most rigorous specification (scale_transitions_v30 §5). Scene Slate has a complete proposal (player_agency_v30 §4) but is not yet canonical. The Dialogue Lattice exists only in the investigation systems proposal and has no v30 skeleton.

The consequence for a player: **the game tells them how to swing a sword, how to argue in parliament, how to investigate a conspiracy, and how to Weave a Thread — but it does not reliably tell them what happens to the world when they succeed, or what happens to them when the world moves.** A faction collapses; the player learns about it through a clock change. An NPC's conviction shifts; the player finds out when the NPC behaves differently in the next social encounter, if the player happens to be present. A territory revolts; the garrison AI handles it unless the player was already standing there.

**What great games do instead:** Crusader Kings III delivers faction-level events as personal stories — your vassal rebels, and the rebellion has a face, a grievance, a history with you. Disco Elysium makes world-state legible through the protagonist's internal monologue — the world changes and you feel it changing through your skills' commentary. Pathologic 2 makes the world's indifference visceral — you can see the clock ticking, you know you cannot be everywhere, and the consequences of your absence arrive as dead patients. Valoria has all the mechanical infrastructure to do this. It has not yet designed the presentational layer that makes it happen.

---

# PART 1: SYSTEM-BY-SYSTEM BRIDGE AUDIT

## 1.1 Faction Layer (faction_layer_v30) — World → Player: WEAK | Player → World: MODERATE

**What the system does well:** Five stability triggers, occupation rules, treaty mechanics, parliament — all mechanically rigorous. The Accord system (peninsular_strain_v1) adds per-territory governance texture. NPC priority trees (npc_behavior_v30 §8) produce autonomous faction behavior.

**Where the bridge fails:**

The faction layer generates events (stability trigger fires, treaty proposed, parliament convened) but has no specification for how those events reach the player as experiences. A stability crisis in Hafenmark is a number change. There is no scene generated, no NPC messenger arriving at the player's camp, no moment where the player sees the consequence unfolding in the street. The Scene Slate (player_agency_v30 §4.2, Priority 1) is supposed to surface these events, but the Slate's generation algorithm is described abstractly ("scenes involving Church NPCs in Gransol"). It does not specify which NPC shows up, what they say, or what the player can do about it.

**Player → World** is better served: Domain Echo (scale_transitions_v30 §5) translates personal victories into faction consequences. But Domain Echo requires "Sufficient Scope" (§7), which means the personal action must involve a faction leader or challenge institutional authority. A player investigating corruption in a border town — the most natural RPG activity — does not fire Domain Echo unless it reaches faction-leader level. The gap between "I discovered something important" and "the faction layer registers what I discovered" is unreliable.

**Precedent critique:** In CK3, every faction event generates a notification with a character portrait, a choice, and a consequence preview. The player always knows what happened, who did it, and what they can do about it. Valoria's faction events generate stat changes. The player must be told about the stat change by the GM (TTRPG) or notice it in the UI (videogame). This is the difference between "your vassal is plotting against you" and "Stability: 4 → 3."

**Proposal:**
- Every stability trigger should name an NPC face and generate a Scene Slate entry. "Hafenmark lost a territory" becomes "Baralta's aide arrives with urgent news — she is convening an emergency parliament session."
- Domain Echo's Sufficient Scope should be lowered for investigation. A completed Complex investigation (Evidence Track 5) that names a faction's institutional acts should fire Domain Echo regardless of whether a faction leader was personally involved. The evidence is the scope — not the meeting.
- Treaty events should generate mandatory Scene Slate Priority 1 entries for all players present in affected territories. A treaty is not a stat change; it is a political earthquake with personal consequences for everyone living under the affected institutions.

---

## 1.2 Conviction Track & Church Mechanics (conviction_track_v30) — World → Player: VERY WEAK | Player → World: MODERATE

**Where the bridge fails:**

The Conviction Track (0–5 per territory, Piety axis) is one of Valoria's most important systems — it determines Church seizure eligibility, cultural identity, and eventually territory control. But it operates entirely at the faction-strategic layer. A territory's CV changing from 3 to 4 means something profound — the Church's institutional authority is deepening, local Einhir heritage is being suppressed, people's lived relationship to their spiritual tradition is shifting. None of this reaches the player as experience.

The Church Attention Pool is the closest thing to player-facing Church pressure, and it works: the player's Exposure feeds the AP, the AP can trigger Heresy Investigation. But the AP is reactive — it responds to what the player does, not what the Church does. When the Church preaches in a territory and CV rises, when Suppress Heresy fires and backlashes, when TC hits milestones — these are world events that reshape the player's environment without the player ever witnessing them.

**Precedent critique:** In Pentiment, the Church's institutional power is visible in every conversation, every building, every ceremony. The player sees the Church acting — not in stat changes but in the priest's sermon becoming more militant, in the abbot's questions becoming more pointed, in the townspeople whispering differently. The Church is a *presence*, not a number. Valoria's Church is mechanically excellent and experientially invisible.

**Proposal:**
- CV changes should trigger territory-level flavor events visible to any player present. CV 3→4: "The bells ring longer in the morning. The priest's sermon cites the Solmund Codex directly for the first time in months." CV 2→1: "Einhir songs are being sung openly in the market for the first time in years."
- Church Attention Pool should have a player-facing indicator — not the number, but its consequence. At AP 1: "You notice a clerk in Church vestments watching the market from the belltower." At AP 3: "The Inquisitor's seal appears on a public notice in the town square." This is the Disco Elysium approach — world state becomes internal monologue or environmental detail.
- Heresy Investigation should be a Scene Slate Priority 1 event, not something that happens at Accounting. The moment the investigation targets the player, the player should experience it as a scene — an interrogation, a search, a confrontation.

---

## 1.3 Fieldwork (fieldwork_v30) — World → Player: STRONG | Player → World: MODERATE

**What the system does well:** This is Valoria's best-designed bridge system. The Depth Axis is a genuine innovation — it ties what the player can perceive to who they are (TS, Certainty, Coherence), not just what they do. The Intelligibility Gradient is philosophically grounded and mechanically elegant. Investigation with Evidence Tracks produces tangible, persistent progress. Socializing with Disposition tracks creates real NPC relationships. Exploration with POIs creates territory-specific content.

The Sincerity Gate (§5.3) deserves special mention — it is one of the few mechanics in any RPG that makes the player's *intent* mechanically relevant. Instrumentally socializing with an NPC risks detection, and the risk comes from the player's own Spirit attribute, not from the NPC's perception. This is Disco Elysium's Inland Empire made into a dice mechanic.

**Where the bridge still fails:**

Fieldwork → World propagation is reliable only through Domain Echo, which requires Sufficient Scope. A player who spends three seasons building Disposition +5 with a minor NPC does not fire Domain Echo. A player who discovers a Resource POI does not change the faction layer. The personal-scale investment has no guaranteed strategic payoff.

More critically: **the world does not fieldwork back.** NPC behavior during fieldwork is entirely reactive — the player approaches, the NPC responds. NPCs do not independently seek out the player, do not bring information the player didn't ask for, do not show up at the player's camp with problems. The NPC priority trees (npc_behavior_v30 §8) drive faction-level actions but do not generate personal-level outreach. Edeyja does not send a message. Vossen does not appear at a Community Weaving site looking for help. Vaynard does not show up at the player's investigation site with competing evidence.

**Precedent critique:** In Shadows of Doubt, NPCs have schedules, routines, relationships, and secrets that the player discovers through environmental interaction — but the NPCs also act independently, creating new evidence, destroying old evidence, and changing the investigation's landscape without the player's involvement. The world investigates the player as much as the player investigates the world. In Case of the Golden Idol, the "synthesis moment" — where accumulated evidence clicks into a unified picture — is the game's emotional peak. Valoria has Evidence Tracks but no synthesis mechanic. The track fills up and the investigation "resolves." There is no moment of assembly, no player-facing realization event.

**Proposal:**
- Add NPC-initiated social fieldwork: NPCs with Disposition ≥ +2 and active Beliefs relevant to the player should generate Scene Slate entries where the NPC approaches the player. "Haelgrund is waiting at the archive and wants to speak privately." This is not a quest — it is the NPC's own agenda intersecting with the player's existence.
- Add an Investigation Synthesis mechanic: when the Evidence Track reaches threshold, the player must Reconstruct (already exists as an action, §4.2) to complete the investigation. The Reconstruct roll determines the quality of the conclusion. Failure: the evidence is assembled but the conclusion is wrong. Partial: correct conclusion but missing context. Success: full picture. Overwhelming: full picture plus one implication the evidence does not explicitly state. This is the Golden Idol moment — you have all the pieces, now assemble them.
- Lower Domain Echo threshold for sustained relationship investment: reaching Disposition +4 with any named NPC should fire Domain Echo (the relationship itself is strategically significant). Reaching Bonded (+5) should fire a stronger Echo.

---

## 1.4 Social Contests (social_contest_v30) — World → Player: MODERATE | Player → World: STRONG

**What the system does well:** The exchange structure, Conviction Track, Composure/Concentration mechanics, and Resonant Style system are excellent. The integration with NPC stance triangles means that social confrontation is mechanically meaningful — the player must know the NPC's conviction and vulnerability to be effective. This rewards investigation (fieldwork) before confrontation (contest), creating a natural progression.

**Where the bridge fails:**

Social contests are isolated events. They begin, they resolve, they end. The Conviction Track resets. The only persistent consequences are: Domain Echo (if sufficient scope), Disposition changes (winner +1, loser −1 with adjudicator), and Rattled marks (which clear at scene end). A devastating argument that shatters an NPC's conviction produces a Belief Scar — but the Scar system is entirely internal to the NPC behavior system. The player does not experience the scar. They do not see the NPC struggling with what they said. They see a stat change on the NPC's sheet, if they Appraise again later.

More fundamentally: **contests do not chain.** A real political drama is a sequence of escalating confrontations where the outcome of each shapes the next. CK3's scheme system does this — each step in a murder plot changes the social landscape. Burning Wheel's Duel of Wits produces lasting compromises that reshape subsequent scenes. Valoria's contests are one-shots. The player wins a parliamentary debate, receives Domain Echo (+1 Mandate), and the next contest starts fresh with a reset Conviction Track.

**Precedent critique:** Burning Wheel's Duel of Wits produces a binding result — the loser must honor the compromise for a specified duration, and breaking the compromise has mechanical consequences. The contest's outcome persists in the game world as an obligation, not just a stat change. Valoria's contests produce outcomes that propagate through Domain Echo but do not create binding obligations or relationship consequences beyond Disposition ±1.

**Proposal:**
- Contest outcomes should create Obligations — mechanical commitments that persist across seasons. A won parliamentary debate about Church expansion should produce an Obligation: "Church must not Preach in [territory] for 2 seasons" or "Crown commits to Suppress Heresy in [territory]." Obligations are tracked like clocks. Violating an Obligation triggers a stability event.
- Belief Scars should be player-visible. When the player's argument produces a Scar on an NPC, the player should receive notification: "Something changed in Himlensendt's expression. His certainty has cracked." This is not a stat reveal — it is a narrative signal that the world registered what the player said.
- Chain contests: if a contest produces a compromise (Conviction Track 4–6), the unresolved tension should generate a Scene Slate entry for the following season. The argument is not over; it is deferred. The NPC will come back. The compromise will be tested.

---

## 1.5 Combat (combat_v30) — World → Player: WEAK | Player → World: WEAK

**Where the bridge fails:**

Combat is the system with the weakest bridge in both directions. The player fights; they win or lose; they take wounds or deal wounds. The consequences are personal (wound penalties, Stamina depletion, incapacitation). Combat does not reliably produce faction-level consequences, territory-level consequences, or NPC relationship consequences.

A player who defeats a faction officer in combat does not fire Domain Echo unless the combat occurred during a Zoom In from the faction layer. A street fight with a Church Templar that the player initiated does not register on the faction layer. A player who kills a named NPC in combat — one of the most dramatic events in any RPG — produces a stat change on the NPC roster and nothing else unless the NPC was a faction leader.

**Precedent critique:** In Banner Saga, every combat has narrative consequences — soldiers die and morale changes, tactical choices reveal character, retreat has strategic cost. Combat is never mechanically isolated from the story. In Mount & Blade, combat produces reputation changes, relationship shifts, prisoner captures, and territory control changes. Combat is the primary mechanism by which the player's personal actions reshape the strategic landscape.

**Proposal:**
- Combat should always produce Exposure. The fieldwork system already specifies combat Exposure codification (quiet +1, conspicuous +2, public +3, per §2.3). This should be emphasized as a primary bridge: every fight the player has makes them more visible to the faction layer.
- Combat victories against named NPCs should always fire Domain Echo, regardless of Sufficient Scope. Defeating a faction officer IS sufficient scope — the act of violence against an institutional representative is an institutional event.
- Combat should produce reputation changes. A player who fights publicly accumulates a combat reputation (already partially specified in the character system). This reputation should have mechanical consequences: NPCs with Disposition ≤ 0 become less willing to confront the player; NPCs with Authority resonant style become more susceptible; Church Attention Pool increases if violence was public.
- Deaths in combat should cascade. Killing a named NPC should trigger: (a) immediate Scene Slate Priority 1 entries for all NPCs Knotted to the dead NPC, (b) faction stability trigger if the NPC was a faction officer, (c) Disposition −3 with the dead NPC's faction for all players involved, (d) potential Conviction crisis for NPCs whose Beliefs referenced the dead NPC.

---

## 1.6 Thread Operations (threadwork_v30) — World → Player: STRONG | Player → World: STRONG

**What the system does well:** Thread operations are the game's best-bridged system. P-01 (inseparability) guarantees that every Thread operation produces three-dimensional consequences — temporal, epistemic, and actualized co-movement. The player cannot touch a Thread without the world changing. This is Valoria's core design achievement.

The co-movement table ensures bidirectionality: Thread operations affect Mending Stability (world clock), Coherence (player state), Certainty (epistemic state), and potentially territory conditions. The scale table (scale_transitions_v30 §2) grades consequences by scope. The mass battle Thread multiplier (×3 MS cost) makes strategic-scale Thread use genuinely costly.

**Where the bridge still fails:**

Thread operations are experienced as dice rolls with stat consequences. The phenomenology — what it feels like to Weave a Thread, to perceive a Gap, to Mend a scar in the rendering — is described in the philosophical foundations but not in the mechanical specifications. The Intelligibility Gradient visualization (fieldwork_v30 §10.2) is a Godot implementation spec, not a TTRPG/Hybrid experience spec.

More critically: **the world does not Thread back.** Thread phenomena happen — Gaps open, Shifting Objects appear, Snapped Zones oscillate — but these events are generated by clock advancement (MS band transitions) and presented as environmental descriptions. They are not active antagonists. A Gap does not pursue the player. A Shifting Object does not make demands. The rendering's instability is passive — it is weather, not enemy.

**Precedent critique:** In Disco Elysium, the protagonist's internal skills are not passive — they interrupt, argue, demand attention, and occasionally take control. The Inland Empire sees things the player did not ask to see. The Shivers tells the player things about the city that no one told it. In Valoria, Thread perception is always player-initiated (Thread-Read requires a deliberate Leap). The Thread does not speak unbidden.

**Proposal:**
- Add involuntary Thread perception for high-TS characters. At TS 30+, the player should occasionally receive unbidden Thread impressions — perceiving a configuration shift without initiating a Thread-Read. This fires when a Thread operation occurs within the player's territory (another practitioner is working, or MS decline triggers spontaneous phenomena). The impression is free (no Coherence cost) but Exposing (+1 Exposure as the character's reaction is visible). This is the Shivers mechanic — the Thread reaches the player.
- Thread phenomena should be active, not passive. When MS drops below a band threshold in the player's territory, the player does not merely observe a stat change — they experience a Rendering Event. A Shifting Object manifests in their immediate environment. A configuration they relied on destabilizes. The ground shifts. This should be a Scene Slate Priority 1 entry — a crisis that demands response.
- Community Weaving (the RM's group Thread practice) should be an experience the player can witness, not just a stat operation. If the player is present in a territory where Community Weaving occurs, they should receive a scene: ordinary people participating in a practice that the Church condemns, the Thread substrate visibly brightening, the social dimension of a metaphysical act. This is where Thread operations connect to political meaning.

---

## 1.7 Player Agency System (player_agency_v30) — World → Player: STRONG (PROPOSED) | Player → World: MODERATE (PROPOSED)

**What the system does well:** The Beliefs/Duties/Scene Slate triangle is the right architecture. Beliefs provide self-authored motivation (Burning Wheel). Duties provide institutional obligation (ROTK Officer Mode). Scene Slate provides world-generated opportunity (Pathologic 2). The scene action budget creates triage. The stature progression creates emergent leadership. All correct.

**Where the bridge fails:**

The system is a proposal, not canonical. Nothing in the v30 skeleton set references it. No other system is designed to feed into it or receive from it. The Scene Slate generation algorithm (§4.2) describes five priority levels but does not specify: how many NPCs appear in each scene, what the scene's initial conditions are, what happens if the player does nothing (the "opportunity not pursued" resolution is described abstractly but not mechanically), or how the Slate interacts with the Duty assignment system when Duty and Belief conflict in the same scene.

More critically: **the stature progression (§5) is linear and faction-locked.** Standing 0→5 is a single track within one faction. There is no cross-faction reputation, no independent standing, no way for the player to accumulate political capital outside the faction system. The "independent" path (§5.3) strips the player of faction resources without providing an alternative power structure. This is not the Disco Elysium path — it is the punishment path.

**Precedent critique:** In Crusader Kings III, a vassal accumulates prestige, piety, gold, and dynasty renown — resources that persist across faction boundaries and can be leveraged to change factions, found new institutions, or declare independence with accumulated power. The vassal is not choosing between "faction member with resources" and "independent without resources." They are accumulating personal power that can eventually exceed institutional power. Valoria's Standing track has no personal-power equivalent.

**Proposal:**
- **Canonize the system.** It is the single most important missing piece.
- **Add a personal Renown track (0–10).** Renown accumulates from: Belief fulfillment (+1), Duty exceeding (+1), Domain Echo produced (+1), NPC arc influenced (+1), investigation resolved (+1). Renown persists across faction changes. Renown 5+ unlocks cross-faction influence (the player can suggest Domain Actions to any faction at Renown 5, not just their own). Renown 8+ unlocks independent political action (the player can declare a Domain Action using their own Renown as the pool, without faction backing). Renown 10 is the Crusader Kings "found a new dynasty" moment — the player has accumulated enough personal authority to function as a political entity.
- **Scene Slate generation should be mechanical, not narrative.** Each Season, the game evaluates: (a) all clock thresholds within 1 of transition, (b) all NPC Belief Scars at 2+, (c) all territories at Accord ≤ 1 in the player's location or adjacent, (d) all active Beliefs and their keyword intersections with the NPC roster, (e) all Duty requirements. Each qualifying condition generates one Scene entry. The player sees the list. The system is deterministic, auditable, and fair. No GM discretion in generation — only in scene execution.

---

## 1.8 NPC Behavior (npc_behavior_v30) — World → Player: MODERATE | Player → World: STRONG

**What the system does well:** The Stance Triangle (Conviction + Resonant Style + Ethical Framework) is the project's second-best design achievement after P-01. It makes every named NPC a mechanical puzzle — the player must discover the NPC's conviction, identify their vulnerability, and craft arguments that exploit it. This rewards investigation before confrontation and produces meaningful social gameplay.

The arc profiles (§5.2) are well-designed: each NPC has 2–3 arc branches determined by game-state conditions, and each branch produces different mechanical consequences. Almud can reform, fortress, or be overthrown. Himlensendt can zealot, crisis, or confront. These are emergent, not scripted.

**Where the bridge fails:**

NPCs are reactive. They respond to player actions and game-state conditions, but they do not independently seek out the player. The NPC priority trees (§8) drive faction-level actions but produce no personal-level output. When Vaynard's priority tree fires "Tribune Investigate," the player does not see Vaynard investigating — they see a stat change on the target faction's Intel value. When Himlensendt's priority tree fires "Heresy Investigation," the player might see the investigation if it targets them, but otherwise it is invisible.

The NPC recruitment procedure (§9.5) is well-specified but entirely player-initiated. NPCs do not recruit the player. There is no system for an NPC to approach the player with an offer, a demand, or a threat. This is backwards — in a political drama, the most important interactions are the ones that come to you, not the ones you seek out.

**Precedent critique:** In Tyranny, NPCs have their own agendas and approach the player with proposals, ultimatums, and requests. The player's reputation determines which NPCs approach and what they offer. The world's human actors are proactive, not passive. In Crusader Kings III, courtiers scheme independently, forming factions, seeking favors, and making demands — the player's inbox is always full. Valoria's NPCs wait to be interacted with.

**Proposal:**
- **NPC Outreach system.** Each named NPC with Disposition ≥ +1 toward the player and an active Belief relevant to the player's situation should evaluate, each season, whether to initiate contact. The NPC's priority tree already determines their strategic intent — extend it to determine whether the player is a useful ally for that intent. If yes: generate a Scene Slate entry where the NPC initiates contact. "Vaynard's agent seeks you in the market quarter. The Duke has a proposition."
- **NPC demands.** NPCs at Disposition ≤ −2 with active threats should generate hostile Scene Slate entries. "Himlensendt has summoned you to the Cathedral. Attendance is not optional." These are not quests — they are demands with consequences for refusal (Disposition −1 with the NPC's faction, potential Heresy Investigation acceleration).
- **NPC independent action visibility.** When an NPC priority tree fires an action relevant to the player's active Beliefs or location, the player should receive a narrative signal. Not the mechanical outcome — the signal that something is happening. "You hear that the Church is conducting Preach operations in Gransol this season." The player can then choose to investigate, intervene, or ignore. The information cost is zero; the action cost is a scene action.

---

## 1.9 Scale Transitions (scale_transitions_v30) — World → Player: WEAK | Player → World: MODERATE

**What the system does well:** The eight handoff rules are well-specified. The Zoom In/Out protocol (§4) correctly handles state transfer between scales. Domain Echo (§5) provides the primary Player → World bridge. Coherence initialization (§6.4) prevents free Coherence resets between Zoom cycles.

**Where the bridge fails:**

Scale transitions are the system that should be the primary bridge, and it is the weakest. The RSE critique (from previous sessions) correctly identified that only five Zoom In triggers exist for 120+ arcs. The player_agency proposal argues that Scene Slate Priority 1 IS the Zoom In system — but this has not been formalized. The Arc-Specific Zoom In Triggers (§4.3) list only two examples (Haelgrund Defection, Consecration Crisis).

The fundamental problem: **Zoom In is optional.** The player (or GM) decides whether to zoom in on a faction event. If they don't zoom, the event resolves through faction AI. This means the most dramatic moments in the game — the coup, the Church seizure, the Altonian invasion — can pass without the player experiencing them personally. The game's greatest moments are opt-in.

**Precedent critique:** In CK3, certain events force the player into a personal-scale decision — a battle, a feast, a council vote. The player cannot abstain from their own coronation. The world's pivotal moments are mandatory experiences, not optional sidequests. In Valoria, the player can theoretically sit in a tavern in Gransol while the Crown collapses in Valorsplatz. The game permits this, but it should not be the default.

**Proposal:**
- **Mandatory Zoom In triggers.** Certain events should force a Scene Slate Priority 0 (above Priority 1) that cannot be declined without explicit cost. If the player is in a territory that goes to Revolt: Zoom In is mandatory. If the player's faction leader is assassinated: Zoom In is mandatory. If the player is the target of a Heresy Investigation: Zoom In is mandatory. The player cannot opt out of events that directly affect them.
- **The "Where Were You?" system.** For major world events that the player was not present for, the game should generate a retrospective Scene Slate entry the following season. "Everyone is talking about the fall of Valorsplatz. Where were you when it happened?" The player gets a scene that is not about the event itself — it is about their relationship to the event. Did they hear about it from a friend? An enemy? Did they read a broadsheet? Did they Thread-Read the aftermath? This is the Pentiment approach — the player's position in the community determines how they experience even distant events.

---

## 1.10 Peninsular Strain & Accord (peninsular_strain_v1) — World → Player: VERY WEAK | Player → World: WEAK

**Where the bridge fails:**

Peninsular Strain is the game's universal victory condition — it is the most important strategic system. And it is entirely invisible to the player at the personal scale. Strain (0–10) is a number. Accord (0–3 per territory) is a number. The player cannot see Strain. They cannot feel Accord. They cannot touch Peninsular Tension.

Accord is specified as a per-territory attribute with four levels (Aligned, Compliant, Resistant, Revolt). These levels have mechanical consequences (Effective Prosperity modification, garrison requirements, Revolt). But the player's ability to affect Accord is limited to one Domain Echo pathway: "PC publicly governs/administers a territory — Overwhelming/Success → Accord +1" (scale_transitions_v30 §5.5). This is a single action type producing a single outcome. The player has no other way to improve Accord.

Meanwhile, the player has 14 combat actions, 7 Thread operations, 6 fieldwork actions, 4 contest styles — and exactly 1 way to affect the victory condition. The most important system is the least interactive.

**Proposal:**
- **Accord should be player-experienceable.** When the player enters a territory, they should see Accord — not as a number, but as environmental texture. Accord 3: "The market is busy. People greet the patrol warmly." Accord 1: "Shops are shuttered by midday. The patrol is followed by sullen eyes." Accord 0: "A barricade blocks the main road. Someone has painted 'Go Home' on the faction hall."
- **Multiple pathways to Accord change.** Successful social fieldwork (building Disposition with local NPCs) should generate Accord +1 potential. Successful investigation that resolves a local concern should generate Accord +1. Successful Community Weaving in a territory should generate Accord +1 if it aligns with local Conviction. Failed military action or public violence should generate Accord −1. The player should have as many ways to affect Accord as they have ways to affect NPC Disposition.
- **Strain should be a felt pressure, not a number.** As Strain increases, the player should experience consequences: travel becomes harder (+1 Ob to movement through high-Strain corridors), NPC Dispositions start lower (−1 starting Disposition in territories with Strain ≥ 4), social contests become harder (audience resistance +1 at Strain ≥ 6). Strain is the peninsula tearing itself apart — the player should feel the tear.

---

## 1.11 Mass Combat (mass_battle_v30) — World → Player: WEAK | Player → World: MODERATE

**Where the bridge fails:**

Mass combat is designed as a unit-level abstraction. The player's personal involvement is limited to General Duel (§3.7 of scale_transitions) — one personal combat exchange per battle turn, maximum 5 exchanges. Thread operations are available in Phase 4 but at ×3 MS cost. The player's primary role in mass combat is issuing commands (Command Rating = ⌈(Charisma + Cognition) ÷ 2⌉).

The problem: **mass combat is the game's most dramatic event and the player is mostly a spectator.** They issue commands and watch units resolve. The personal-scale experience of being in a battle — the fear, the confusion, the moral weight of ordering people to die — is not mechanically expressed. Mount & Blade solves this by putting the player on the battlefield as a combatant. Total War: Three Kingdoms solves this by making the general's personal combat decisive. Banner Saga solves this by making every casualty feel personal through named characters with limited health.

**Proposal:**
- **Morale system tied to player presence.** Units within the player's territory should gain +1 Discipline while the player is present. If the player is wounded or incapacitated, units take −1 Discipline. The player's physical state is the army's morale.
- **Post-battle consequence scenes.** After every mass battle, the player should receive a mandatory Scene Slate entry: the aftermath. Wounded soldiers, dead NPCs, burning buildings, displaced civilians. The player makes choices about what to attend to — heal the wounded (Endurance check), comfort the bereaved (Attunement check), survey the damage (Cognition check). These choices affect Accord in the territory and Disposition with surviving NPCs.
- **Named unit characters.** Each mustered unit should have one named officer NPC with a Disposition track and a minimal Stance Triangle. When the unit takes casualties, the officer may be killed (GM rolls on Size loss). The player's relationship with unit officers creates personal stakes in unit survival.

---

# PART 2: CROSS-CUTTING PROBLEMS

## 2.1 The Legibility Problem

Valoria has ~50 tracked values (5 global clocks, 6 faction stats × 4+ factions, 17 territory Conviction values, 17 territory Accord values, per-NPC Disposition/Conviction/Scar counts, personal Coherence/Certainty/TS, Evidence Tracks, Exposure per territory). The cognitive load document correctly identifies this as the game's greatest risk.

But the legibility problem is not about cognitive load — it is about information architecture. The player does not need to know all 50 values. They need to know: what changed since last season, what is about to change, and what they can do about it. The companion app design note (companion_app_design_note_2026-04-04) correctly identifies the computation/experience split. Extend it: the app does not just track numbers — it generates a "State of the Peninsula" briefing each season that highlights the 3–5 most significant changes in natural language. "The Church is expanding in the north. Hafenmark is losing ground. Varfell is quiet — too quiet. The southern territories are becoming unstable."

## 2.2 The Companion Gap

The integration audit series (v1, v2, v3) identifies the companion question as the emotional center of the player experience. The audit is correct. The game currently has no companion specification — no definition of what it means for an NPC to travel with the player. Every precedent game that handles political drama well (Dragon Age, Tyranny, Planescape: Torment, Baldur's Gate 3) treats companions as the primary vehicle for world-to-player translation. The companion reacts to world events, argues about the player's choices, reveals information through personal conversation, and creates stakes through relationship investment.

Valoria has all the mechanical infrastructure for companions: Knots, Disposition, multi-character fieldwork, group combat, Corroboration in contests. What is missing is the specification that names what a companion IS.

**Proposal:** A companion is an NPC at Disposition +3 or higher who has been formally invited to travel with the player. Maximum 2 companions (cognitive load constraint). Companions generate one free social fieldwork action per season (the player does not need to spend a scene action to talk to their companion — conversations happen during travel). Companions react to Scene Slate entries by stating their opinion (aligned with their Conviction and Beliefs). Companions participate in combat using their own stats. Companions accumulate Knot strain normally and may depart if strained beyond their Bonds capacity.

## 2.3 The Consolidation Opportunity

The game currently has 18+ systems. Many overlap. The fieldwork system contains social mechanics that partially duplicate the social contest system. The NPC behavior system contains faction priority trees that duplicate the board game faction AI. The investigation systems proposal introduces an Ontological Ledger that duplicates the Evidence Track. The player agency system introduces Beliefs that parallel NPC Convictions.

**Consolidation targets:**
- **Merge the investigation systems proposal's Dialogue Lattice into the social contest system.** The Lattice is a five-filter chain for NPC responses; the social contest system already has Appraise, Argue, and Resolve steps. The Lattice should be the investigation-mode version of the contest — same pool construction, same degree table, different interaction structure (iterative rather than exchange-based).
- **Merge NPC Outreach into the Scene Slate.** Do not create a separate NPC Outreach system — extend the Scene Slate generation algorithm to include NPC-initiated entries alongside world-state entries.
- **Merge Obligations into the faction layer.** Do not create a separate Obligation tracking system — extend the treaty/agreement mechanics in faction_layer_v30 to cover personal-scale agreements.
- **Unify Beliefs and Convictions.** Player Beliefs and NPC Convictions serve the same function (motivating action and creating vulnerability). The vocabulary should be unified. Players have Convictions (player-authored). NPCs have Convictions (system-authored). Both are targeted through Resonant Styles. Both produce arc movement when challenged.

---

# PART 3: THE INTEGRATION BLUEPRINT

## 3.1 The Season Cycle (Revised)

Every season should follow this sequence for the player:

**Phase 0 — Briefing.** The game/GM presents the State of the Peninsula: 3–5 most significant changes. The companion app generates this. The player knows what happened.

**Phase 1a — Duty Assignment.** Faction leader evaluates priority stack, issues Duty. Player receives it as a personal communication, not a system message. "Baralta needs you in Gransol. The Church is moving."

**Phase 1b — Scene Slate Generation.** Deterministic generation from game state. The player sees 4–9 opportunities, ordered by priority. Each opportunity has: a named NPC, a location, a one-sentence description, and a tag indicating which Belief/Duty it intersects.

**Phase 1c — Personal Phase.** 3–5 scene actions. Each scene uses existing systems (fieldwork, combat, contest, Thread). Each scene produces consequences that queue to Phase 3.

**Phase 2 — Strategic Phase.** Domain Actions, military movements, faction AI. The world moves.

**Phase 3 — Accounting.** Clock advancement, Domain Echo resolution, Accord checks, Duty evaluation (Standing ±1), Belief review (player may revise), Renown update. End-of-season state snapshot.

**Phase 4 — Aftermath.** Companion conversation (free, no action cost). The companion reacts to what happened this season. The player reflects.

## 3.2 The Bridging Principle

Every system should satisfy this test: **can the player see the world through this system, and can the world see the player through this system?**

If a system fails one direction, add the missing bridge. If a system fails both directions, ask whether the system is necessary or whether its function can be absorbed by a system that already bridges.

## 3.3 Priority Order for Revision Work

| Priority | System | Work Required | Impact |
|----------|--------|---------------|--------|
| 1 | Player Agency | Canonize. Add Renown track. Mechanical Scene Slate generation. | Highest — solves the motivation problem |
| 2 | Companion Specification | New document. 2–3 pages. Uses existing mechanics. | High — creates emotional center |
| 3 | NPC Outreach | Extend NPC behavior §8 priority trees to generate personal-level output. | High — makes the world proactive |
| 4 | Scale Transitions | Add mandatory Zoom In triggers. "Where Were You?" retrospective scenes. | High — prevents dramatic events from being invisible |
| 5 | Fieldwork | Add NPC-initiated social entries. Investigation Synthesis mechanic. | Medium — improves an already-strong system |
| 6 | Social Contests | Add Obligations. Scar visibility. Chain contests. | Medium — adds persistence |
| 7 | Accord | Add player pathways. Environmental legibility. | Medium — connects player to victory condition |
| 8 | Combat | Domain Echo on named NPC combat. Reputation cascade. Death cascade. | Medium — bridges an isolated system |
| 9 | Conviction Track | Player-facing indicators. Heresy Investigation as scene. | Low — presentation layer |
| 10 | Mass Combat | Post-battle scenes. Named unit officers. | Low — system already functional |

---

# PART 4: WHAT THE GAME SHOULD FEEL LIKE

When all bridges are working, a season of Valoria should feel like this:

The player begins with a briefing. The Church has been preaching aggressively in the north. Hafenmark's treasury is strained. A Gap opened near Stillhelm last season and no one Mended it. The player's companion mutters something about the Church overreaching.

The player receives a Duty: investigate Church financial irregularities in Himmelenger. The player's Beliefs are: "I will prove to Almud that the Thread is real," "I will protect the Einhir heritage in Grauwald," and "I will earn Edeyja's trust."

The Scene Slate presents seven opportunities:
- Himlensendt is conducting a public Preach in Himmelenger (Priority 1 — clock event)
- Baralta's aide wants to discuss the treasury crisis (Priority 2 — Duty-aligned)
- A trader in Gransol claims to have Einhir artifacts (Priority 3 — Belief-aligned)
- Haelgrund sent a message requesting a private meeting (Priority 3 — NPC-initiated)
- A Gap is expanding near Stillhelm (Priority 1 — Thread crisis)
- Edeyja's warden sent word that the Southernmost needs help (Priority 3 — Belief-aligned)
- A tavern fight between Crown soldiers and Varfell merchants in Ehrenfeld (Priority 5 — ambient)

The player has four scene actions. They cannot do everything. The Gap and the Preach are both urgent. The Duty and the Beliefs pull in different directions. The companion argues for investigating the Church — "Follow the money, that's where the corruption is." The player decides.

This is the game. Every choice costs something. Every inaction has consequences. The world moves whether you watch or not. And when you act, the world remembers.

---

*End of document.*
