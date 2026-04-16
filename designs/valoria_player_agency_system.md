# VALORIA — Player Agency System
## Design Proposal — PP-TBD
## Status: PROPOSAL — requires approval before integration
## Date: 2026-04-15
## Scope: Player motivation, scene generation, belief system, faction role, moment-to-moment decision loop
## Affects: character creation (params_core), season structure (board_game_v30), fieldwork (fieldwork_v30), scale transitions (scale_transitions_v30), NPC behavior (npc_behavior_v30)
## Canon compliance: P-03 (consciousness-performed rendering — player's perceptual horizon defines available scenes), P-15 (three-layer being-persistence — Beliefs are personal, Duties are cultural, Convictions are metaphysical)

---

## §0 — THE PROBLEM

Every system in Valoria specifies *how* a player acts. No system specifies *why* a player acts or *what options are presented to them*. A faction leader has an implicit motivation (win the game) and an implicit decision loop (play Domain Actions strategically). A non-leader character — which is most starting characters and the default videogame protagonist — has neither.

The result: a mechanically complete game with no player-facing motivation architecture. The player has 14 combat actions, 6 fieldwork actions, 7 Thread operations, 4 contest styles, and no answer to "what should I do this season?"

This proposal establishes three interlocking systems that generate player motivation at every stature level:

1. **Beliefs** — what the player's character wants (self-authored goals)
2. **Duties** — what the player's faction needs (externally assigned objectives)
3. **Scene Slate** — what the world is offering (generated opportunities)

---

## §1 — PRECEDENT ANALYSIS

### 1.1 Romance of the Three Kingdoms (Officer Mode)

ROTK's officer mode solves the "non-leader" problem directly. An officer character serves a lord and receives assignments (develop a city, train troops, conduct diplomacy) but retains personal ambition. The officer can follow orders, exceed them, or subtly work toward personal goals that may conflict with their lord's interests. Promotion is earned through merit and faction standing — an officer who performs well eventually becomes a governor, then potentially a lord themselves.

**What Valoria takes:** The duty assignment loop. A non-leader character receives faction objectives but retains personal agency to exceed, reinterpret, or subvert those objectives. Performance is tracked — success builds standing, failure erodes it. Promotion is a real mechanical possibility that changes the player's relationship to the faction layer.

### 1.2 Crusader Kings III (Vassal Play)

CK3's vassal gameplay creates motivation through the tension between personal ambition and feudal obligation. A vassal has their own domain, their own dynastic goals, their own council position — but operates under a liege's laws and expectations. The vassal's moment-to-moment decisions involve: fulfilling liege obligations (military levy, taxes), pursuing personal schemes (seduction, murder, fabricating claims), managing their own territory, and navigating the social web of their peer vassals.

**What Valoria takes:** The dual-agenda structure. The player always has two simultaneous motivation tracks — what their faction expects and what they personally want. These tracks sometimes align (investigating a rival serves both personal curiosity and faction intelligence needs) and sometimes conflict (befriending Edeyja serves personal Thread knowledge but antagonizes Church-aligned faction leadership). The friction between tracks is where gameplay lives.

### 1.3 Disco Elysium

DE's protagonist is propelled not by quests but by the world's density of interactable meaning. Every object, person, and location offers interpretive engagement. The player's skills (conceptual, physical, social, psychic) are not just tools but perspectives — they argue with each other about what matters, what to investigate, what to care about. Progress comes from following threads of meaning rather than completing objectives.

**What Valoria takes:** The scene opportunity as interpretive invitation, not directive. When the game presents "Haelgrund wants to meet secretly," it is not issuing a quest — it is offering a thread of meaning. The player chooses which threads to pull based on what their character finds significant. The Belief system formalizes this: Beliefs are what the character finds significant, and the game generates opportunities that intersect with those significances.

### 1.4 Mount & Blade / Manor Lords

M&B's protagonist starts as a nobody with a sword and a horse. Agency comes from small-scale tangible action — fight bandits, trade goods, recruit villagers — that compounds into political relevance. The player is never told "become king." They accumulate capability and reputation until political agency becomes available. Manor Lords adds the territorial dimension: the player governs a settlement whose prosperity they can see, building by building.

**What Valoria takes:** The stature progression as emergent possibility, not scripted path. The player starts as an operative. Through accumulated Disposition with faction leaders, through evidence gathered and leveraged, through territory governance demonstrated, through Thread knowledge earned — the player's stature within the faction grows mechanically. The game never says "you are now the leader." The player's accumulated standing, relationships, and capabilities reach a threshold where leadership becomes mechanically available.

### 1.5 Pathologic 2

Pathologic's protagonist operates under a hard time constraint (12 days) with more needs than can be fulfilled. Every hour spent on one objective is an hour not spent on another. The player must triage: which patients to save, which errands to run, which leads to pursue. The game's emotional core is the cost of choosing.

**What Valoria takes:** The scene action budget as triage mechanism. The player has 3–5 scene actions per season. There are always more opportunities than actions. Choosing is the gameplay — not executing, but deciding what to attend to and what to let pass. Opportunities not pursued do not wait — they resolve through NPC AI and clock advancement without player input, often in ways the player would not have chosen.

### 1.6 Pentiment

Pentiment's protagonist investigates in a community. Every conversation changes both the protagonist's understanding and the community's understanding of the protagonist. Time is finite — you cannot interview everyone. Choosing who to talk to determines not just what you learn but what people think you're doing and why. Investigation is social performance.

**What Valoria takes:** Investigation as social act with social cost. Interviewing an NPC about Church corruption in Valoria isn't free — it costs Exposure (+1 Church Attention Pool if observed), it shifts your Disposition with the interviewee (they now know you're asking questions), and it commits a scene action you could have used elsewhere. The information gained is valuable, but the act of gaining it has consequences in every other system.

---

## §2 — BELIEFS

### 2.1 Definition

A Belief is a player-authored statement of what their character intends to do, values, or wants to discover. It is not a conviction (that's an NPC system tracking ethical commitments). It is not a quest (there is no quest-giver and no guaranteed resolution). It is a declared intention that the game tracks and the player pursues.

### 2.2 Structure

Three Beliefs at any time. Each Belief is one sentence: a subject, an action or stance, and an implicit obstacle.

Good Beliefs: "I will discover what Haelgrund is hiding from the Church." "I will protect Torben from becoming an Altonian pawn." "I will prove to Almud that the Thread is real without destroying his authority." "I will build a network of Thread-aware allies before the Church finds me."

Bad Beliefs (too vague, too passive, no obstacle): "I want to help my faction." "I believe in justice." "I will see what happens."

### 2.3 Mechanical Integration

**Creation:** During character creation, write 3 Beliefs. One should relate to a personal goal, one to a faction concern, one to a relationship or NPC.

**Scene generation:** The Scene Slate (§4) prioritizes opportunities that intersect with active Beliefs. If the player has "I will discover what Haelgrund is hiding," scenes involving Haelgrund, Church internal politics, and secret Thread sensitivity surface more frequently.

**Momentum:** Pursuing a Belief in a scene grants +1 Momentum. The action must be a genuine step toward the Belief, not a retroactive justification. Momentum is spent for +1D or to invoke a Stunt.

**Fulfillment:** When a Belief is achieved or fundamentally abandoned, the player writes a new Belief. Fulfillment grants a one-time +2 Momentum and may trigger a character development moment (Certainty shift, NPC arc trigger, or Domain Echo if the fulfillment had Sufficient Scope).

**Contradiction:** If a Belief directly contradicts a Duty (§3), the player must choose which to pursue in any scene where both are relevant. This choice is the game's central tension for non-leader characters — personal meaning vs institutional obligation.

### 2.4 Why Beliefs Work

Beliefs solve the "why does my character get out of bed" problem without railroading. The player decides what matters. The game responds by generating relevant opportunities. The player executes using the existing mechanical systems (combat, contest, fieldwork, Thread). The outcome feeds back into clocks, NPC states, and territory conditions. The cycle repeats.

Beliefs also solve the "creative player" problem: a player who writes "I will forge a secret alliance between Varfell and the Restoration Movement" has invented a strategic objective that no NPC priority stack would generate. The game doesn't need to anticipate this — it needs to present scenes where the player can pursue it (meetings with Vaynard, meetings with Vossen, territories where both factions have Presence, contests where both factions' interests align).

---

## §3 — DUTIES

### 3.1 Definition

A Duty is a faction-assigned objective that the player's character is expected to pursue. It represents what the faction needs from the player this season. Duties are generated by the faction's current strategic state and issued by the faction leader (NPC or fellow player).

### 3.2 Generation

At the start of each season, the player's faction leader evaluates the faction's AI priority stack and assigns one Duty to the player character based on the highest-priority unaddressed need that matches the player's capabilities. Duty assignment considers:

- **Player's location:** Duties are assigned in territories the player can reach.
- **Player's skills:** Investigation duties for high-Cognition characters, diplomatic duties for high-Charisma characters, Thread duties for practitioners.
- **Faction urgency:** Survival-tier priorities (Stability ≤ 2) generate urgent defensive Duties. Expansion-tier priorities generate offensive Duties.

### 3.3 Duty Types

| Duty | Assigned When | Success Condition | Failure Consequence |
|------|--------------|-------------------|---------------------|
| Investigate | Faction suspects rival activity | Complete investigation (Evidence Track reaches threshold) | Rival action proceeds undetected |
| Diplomacy | Faction needs alliance or treaty | Improve Disposition with target NPC to threshold | Diplomatic window closes; NPC AI acts independently |
| Governance | Territory Accord declining | Maintain or improve Accord in assigned territory | Territory may Revolt |
| Protection | NPC or asset under threat | Prevent assassination, arrest, or seizure | NPC lost, asset captured |
| Reconnaissance | Faction lacks intelligence | Survey territory, identify threats | Faction acts on incomplete information |
| Subversion | Faction wants to destabilize rival | Reduce target territory Accord or target NPC Disposition | Player's cover blown; Exposure consequences |
| Thread Operation | Faction needs Thread intervention (Crown/Varfell only) | Mend Gap, restore MS, or advance VTM | MS continues declining; Thread opportunity lost |
| Escort | Key NPC or asset needs safe passage | Move NPC/asset to destination territory without interception | NPC captured or killed; faction consequences |

### 3.4 Duty Completion

**Success:** Standing +1 (faction-specific track, 0–5). High Standing unlocks: access to faction intelligence (Standing 2), invitation to faction council discussions (Standing 3), authority to issue sub-commands to NPC officers (Standing 4), candidacy for faction leadership succession (Standing 5).

**Failure:** Standing −1. Below Standing 0: the faction stops assigning Duties — the player is functionally independent but loses faction support (no Domain Action influence, no faction intelligence, no territorial safe harbor).

**Exceeding:** Completing the Duty AND producing additional value (discovered a conspiracy, turned an enemy NPC, generated Casus Belli). Standing +2 instead of +1.

### 3.5 Duty vs Belief Tension

The game's richest moments emerge when Duty and Belief conflict. Examples:

- **Duty:** "Investigate Church activity in Gransol." **Belief:** "I will prove to Almud that the Thread is real." The investigation might reveal Church corruption — useful for the Belief — but acting on that evidence publicly might destabilize the faction's Church relationship, failing the implicit diplomatic goal behind the Duty.

- **Duty:** "Protect Torben from Altonian influence." **Belief:** "I will build a network of Thread-aware allies." Spending a scene action on Torben protection means one fewer action for network-building. The player must triage.

The game does not resolve this tension. The player does. And their choice defines their character.

---

## §4 — SCENE SLATE

### 4.1 Definition

At the start of each season's Personal Phase, the game generates a **Scene Slate**: a set of available scene opportunities drawn from the current game state. The player chooses which to pursue with their limited scene actions (3–5 per season, set by game difficulty).

### 4.2 Generation Sources

Scene opportunities are drawn from five sources, evaluated in priority order:

**Priority 1 — Crisis events (mandatory presentation):**
- Territory at Accord 0 (Revolt) where player is present or adjacent.
- NPC arc moment (conviction wound, loyalty threshold, Certainty shift) involving an NPC the player has Disposition ≥ +1 with.
- Clock threshold crossed (MS band transition, CI milestone, IP threshold).
- Active threat to the player (Heresy Investigation targeting the player, assassination attempt, military confrontation in player's territory).

**Priority 2 — Duty-aligned opportunities:**
- Scenes that advance the current season's Duty. If Duty is "Investigate Church activity in Gransol," scenes involving Church NPCs in Gransol, Church records, and Church-aligned territory residents are generated.

**Priority 3 — Belief-aligned opportunities:**
- Scenes that intersect with one or more active Beliefs. The game scans Belief text for NPC names, faction references, territory references, and system keywords (Thread, Church, treaty, etc.) and surfaces scenes containing those elements.

**Priority 4 — Territorial opportunities:**
- Events in the player's current territory or adjacent territories: NPC arrivals, trade caravans, military movements, Thread phenomena, RM community gatherings, Calamity radiation effects.

**Priority 5 — Ambient world events:**
- Low-priority scenes that add world texture: overheard conversations, rumors, environmental details, minor NPC interactions. These cost scene actions to pursue but may reveal unexpected leads.

### 4.3 Scene Slate Size

The Slate presents more opportunities than the player can pursue:
- At game difficulty Normal: 5–7 opportunities per season, 4 scene actions.
- At game difficulty Hard: 7–9 opportunities, 3 scene actions.
- At game difficulty Narrative: 4–5 opportunities, 5 scene actions.

The surplus is the point. Opportunities not pursued resolve through NPC AI and clock advancement — the revolt you didn't attend to resolves based on garrison strength alone. The NPC whose arc moment you missed makes their decision based on their conviction, without your input. The Thread instability you didn't Mend persists and worsens.

### 4.4 Scene Resolution

Each scene opportunity, when selected, places the player in a specific location with specific NPCs and specific initial conditions. The player then uses the existing mechanical systems:

- Scene involves a hostile NPC → combat or social contest, player's choice.
- Scene involves information → investigation actions.
- Scene involves an NPC relationship → socializing actions (Connect, Read).
- Scene involves Thread phenomena → Thread operations (if capable) or observation (if not).
- Scene involves a territory → governance, stealth, or exploration.

A single scene may involve multiple systems. Interviewing a reluctant NPC might require: Read (Appraise to identify pressure point), Connect (improve Disposition first), then Interview (extract information) — three fieldwork actions consuming one scene action if the player is efficient, or stretching across multiple scene actions if the NPC is resistant.

### 4.5 Opportunities Not Pursued

This is the design's sharpest edge. Unpursued opportunities produce consequences:

- An NPC arc moment you missed: the NPC resolves their crisis based on their conviction and AI priority, without player influence. Haelgrund's secret TS is discovered by the Church instead of by you — and the Church responds with Heresy Investigation rather than the nuanced conversation you might have had.
- A territory crisis you didn't attend: the faction AI handles it (Govern roll at faction stat level). Succeed or fail, you had no say.
- A Thread event you didn't respond to: MS takes the hit. The Gap persists. The radiation zone may expand.

The player cannot prevent the world from moving. They can only choose where to be when it does.

---

## §5 — STATURE PROGRESSION

### 5.1 Stature Levels

The player's relationship to the faction layer changes as they accumulate Standing:

| Standing | Stature | Faction Relationship |
|----------|---------|---------------------|
| 0–1 | Operative | Receives Duties. No faction-layer input. Sees public faction state only. |
| 2 | Agent | Receives Duties. Sees faction intelligence (rival faction stats, territory conditions). Can suggest Domain Actions to leader (non-binding). |
| 3 | Counselor | Receives Duties but can negotiate or refuse. Invited to faction council — sees the leader's priority evaluation and can argue for different priorities via social contest. |
| 4 | Lieutenant | Can issue sub-commands to NPC officers (direct minor NPC actions). Duty becomes a strategic directive rather than a specific task. One bonus scene action per season from faction resources. |
| 5 | Successor | Eligible for faction leadership if the current leader is eliminated, incapacitated, or overthrown. At this level, the player can initiate a leadership challenge (social contest against current leader, with faction council as adjudicator). |

### 5.2 Leadership Acquisition

When a faction leader is removed (Almud overthrown by Coup, Himlensendt's Crisis of Faith, Baralta's succession, Vaynard's death), the game evaluates succession:

- If the player is Standing 5 in that faction: they are offered leadership. Accepting transforms them from operative to leader — they now issue Domain Actions directly, play the faction's card hand, and lose the Duty system (replaced by faction AI evaluation as their "advisor").
- If the player is below Standing 5: succession follows the canonical NPC rules (Torben inherits Crown, Cardinals contend for Church, Maret Uln may inherit Varfell, Baralta's succession is undefined).

Leadership can also be seized: a Standing 4+ character can call a leadership challenge at any time via social contest against the current leader, with the faction council as expert adjudicator (Cognition-based). Success: player becomes faction leader. Failure: Standing drops to 2, Disposition with deposed leader drops to −4.

### 5.3 Staying Independent

A player can choose to refuse faction alignment entirely or abandon their faction. An independent character:
- Receives no Duties.
- Generates their own scene opportunities from Beliefs only.
- Has no faction stat pool for Domain Actions.
- Cannot participate in Parliament or faction military.
- CAN pursue Thread operations, fieldwork, and personal combat freely.
- CAN build relationships with NPCs across all factions without factional Disposition penalties.

This is the Disco Elysium path — the player is an investigator, a Thread practitioner, a wanderer. Their impact on the game world comes through personal-scale actions and their Domain Echoes, not through institutional authority. It is a viable but harder path.

---

## §6 — SCENE ACTION BUDGET

### 6.1 Base Budget

| Difficulty | Scene Actions / Season | Opportunities / Slate |
|-----------|----------------------|----------------------|
| Narrative | 5 | 4–5 |
| Normal | 4 | 5–7 |
| Hard | 3 | 7–9 |

**Narrative** is about comfort — you can pursue most opportunities. **Hard** is about triage — you can pursue barely a third. The game's tension scales with the gap between opportunities and actions.

### 6.2 Modifiers

- **Standing 4+ (Lieutenant):** +1 scene action from faction resources.
- **Knot with a local NPC:** +1 scene action in that NPC's territory (the relationship opens doors that save time).
- **Out of Breath (Stamina 0):** −1 scene action (physical exhaustion limits your capacity).
- **Wounded (2+ Wounds):** −1 scene action (injuries slow you down).

### 6.3 Scene Action Economy

One scene action = one scene opportunity pursued. A scene contains 1–3 mechanical interactions (a fieldwork action, a social roll, a combat exchange, a Thread operation). Scenes that require extended engagement (multi-exchange social contest, complex investigation, sustained Thread operation) may consume 2 scene actions.

The scene action budget is the game's primary pacing lever. It determines how much the player can influence per season, and therefore how quickly the game converges toward victory or shared loss.

---

## §7 — INTEGRATION WITH EXISTING SYSTEMS

### 7.1 Character Creation (params_core)

Add to character creation:
- Step: Write 3 Beliefs.
- Step: Choose faction alignment (or independent).
- Derived: Starting Standing = 1 (faction members) or 0 (independent).

### 7.2 Season Structure (board_game_v30)

Revise the three-phase season:
- **Phase 1a — Duty Assignment.** Faction leader evaluates priority stack, assigns Duty to player character.
- **Phase 1b — Scene Slate Generation.** Game generates 4–9 opportunities from five sources.
- **Phase 1c — Personal Phase.** Player chooses and resolves scene actions.
- **Phase 2 — Strategic Phase.** Domain Actions as existing.
- **Phase 3 — Accounting.** As existing, plus: Standing update (Duty success/failure), Belief review (player may revise Beliefs).

### 7.3 Fieldwork (fieldwork_v30)

No changes to mechanics. Scene generation integrates fieldwork as the primary personal-phase activity type.

### 7.4 Scale Transitions (scale_transitions_v30)

Scene Slate Priority 1 (crisis events) provides the missing Zoom In triggers. When a clock threshold is crossed or an NPC arc moment fires, the game generates a scene opportunity that the player can pursue — this IS the Zoom In moment. The Slate does not force the player into the scene (unlike a mandatory Zoom In). It offers the scene. The player decides whether to spend a scene action on it. If they don't, the crisis resolves through NPC AI.

This solves ED-545 (only 5 Zoom In triggers) structurally: the Scene Slate IS the Zoom In trigger system. Any game state change that would be interesting to experience personally becomes a scene opportunity in the Slate.

### 7.5 NPC Behavior (npc_behavior_v30)

NPC faction leaders generate Duties by evaluating their AI priority stack. The Duty is the highest-priority item that the player character could plausibly address. This gives the NPC AI a new output: not just "what action does the faction take" but "what mission does the faction assign to the player."

### 7.6 Emergent Arcs

Beliefs function as player-authored arc vectors. They have a source (the player), a direction (the Belief statement), and conditions that modulate their strength (NPC relationships, territory access, system knowledge). They integrate with the existing vector-based arc architecture: player Beliefs are active pressures that intersect with NPC arc pressures and clock pressures to produce emergent narrative.

---

## §8 — WHAT THIS SOLVES

| Problem | Solution |
|---------|----------|
| "Why does my character act?" | Beliefs provide self-authored motivation. Duties provide faction-assigned motivation. |
| "What are my options?" | Scene Slate presents 4–9 opportunities per season, generated from game state. |
| "Why can't I do everything?" | Scene action budget (3–5) forces triage. Unpursued opportunities resolve without player input. |
| "How do I gain political influence?" | Standing track (0–5) represents faction trust, earned through Duty completion. |
| "Can I become the faction leader?" | Standing 5 enables succession or leadership challenge. |
| "What if I don't want to serve a faction?" | Independent path sacrifices faction resources for cross-faction freedom. |
| "Why does investigation matter?" | Evidence feeds Corroboration, Casus Belli, NPC arc triggers, and Belief fulfillment. |
| "How do I know what's happening in the world?" | Scene Slate surfaces world events relevant to the player's location, Beliefs, and Duties. |
| ED-545 (Zoom In triggers) | Scene Slate Priority 1 IS the Zoom In system — any game state change generates a scene opportunity. |
| ED-546 (RM actor) | An independent player aligned with RM pursues RM Beliefs without faction infrastructure. RM Community Weaving is a scene opportunity in territories with Piety ≤ 1. |
| ED-547 (Fieldwork resource cost) | Scene action budget IS the fieldwork cost — each investigation scene costs a scene action that could have been spent elsewhere. |
