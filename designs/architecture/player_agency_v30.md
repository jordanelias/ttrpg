# VALORIA — Player Agency System
## Design Proposal — PP-TBD
## Status: CANONICAL — approved 2026-04-17 (editorial batch acceptance)
## Date: 2026-04-15
## Scope: Player motivation, scene generation, conviction system, faction role, moment-to-moment decision loop
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

## §2 — CONVICTIONS

### 2.1 Definition

A Conviction is a player-authored statement of what their character intends to do, values, or wants to discover. It is not a quest (there is no quest-giver and no guaranteed resolution). It is a declared stance that the game tracks and the player pursues.

**Vocabulary unification:** Player Convictions and NPC Convictions (npc_behavior_v30 §1.2) share the same name because they serve the same function — driving action and creating vulnerability. Both are targetable via Resonant Styles (npc_behavior §1.3). When an NPC's argument targets a player's Conviction successfully (Contest victory using the correct Resonant Style), the player marks a Conviction strain. Three strains on one Conviction: it must transform or be abandoned. This symmetry means the world affects the player the same way the player affects the world.

### 2.2 Structure

Three Convictions at any time. Each Conviction is one sentence: a subject, an action or stance, and an implicit obstacle.

Good Convictions: "I will discover what Haelgrund is hiding from the Church." "I will protect Torben from becoming an Altonian pawn." "I will prove to Almud that the Thread is real without destroying his authority." "I will build a network of Thread-aware allies before the Church finds me."

Bad Convictions (too vague, too passive, no obstacle): "I want to help my faction." "I believe in justice." "I will see what happens."

### 2.3 Mechanical Integration

**Creation:** During character creation, write 3 Convictions. One should relate to a personal goal, one to a faction concern, one to a relationship or NPC.

**Scene generation:** The Scene Slate (§4) prioritizes opportunities that intersect with active Convictions. If the player has "I will discover what Haelgrund is hiding," scenes involving Haelgrund, Church internal politics, and secret Thread sensitivity surface more frequently.

**Momentum:** Pursuing a Conviction in a scene grants +1 Momentum. The action must be a genuine step toward the Conviction, not a retroactive justification. Momentum is spent for +1D or to invoke a Stunt.

**Fulfillment:** When a Conviction is achieved or fundamentally abandoned, the player writes a new Conviction. Fulfillment grants a one-time +2 Momentum and may trigger a character development moment (Certainty shift, NPC arc trigger, or Domain Echo if the fulfillment had Sufficient Scope).

**Resolution States (campaign_architecture_v1 §7.3):** When a Conviction resolves, it enters one of four states:

| State | Condition | Narrative Effect |
|-------|-----------|-----------------|
| **Fulfilled** | The player achieved what the Conviction stated. | +2 Momentum. Certainty may shift toward the value the Conviction expressed. Portrait records this as an accomplished belief. |
| **Failed** | The player pursued the Conviction but circumstances prevented achievement. | +1 Momentum (the attempt mattered). Certainty may shift away from the value. Portrait records this as a tested and broken belief. |
| **Transformed** | Through play, the Conviction evolved into something different from what was originally written. | +2 Momentum. The player writes the transformed Conviction as a new Conviction (it does not count against the 3-Conviction cap for one season). Portrait records the transformation arc. |
| **Unresolved** | The Conviction was abandoned without pursuit — the player lost interest or events overtook it. | No Momentum. Portrait does not record this — it simply fades. If all 3 Convictions are simultaneously Unresolved, the player receives a "drift" warning: "Your character has no active purpose." |

**Sufficient Scope gating:** A Conviction resolution (any state except Unresolved) only counts for Portrait and retirement purposes if the player took ≥ 2 scene actions pursuing or responding to the Conviction. This prevents trivial resolutions from qualifying for Portrait Retirement.

**Portrait Retirement trigger:** At any season transition after the player has resolved at least 2 of 3 starting Convictions (any resolution state except Unresolved), the option "Conclude this story" appears. Selecting it fires the Portrait Sequence. The player can also continue indefinitely — the option is always available once unlocked, never forced.

**Draft Portrait:** Available from the main menu at any time. Shows what the Portrait would say if the campaign ended now — Conviction resolution states, Knot history, faction standing, Thread relationship, world state. This is the in-play feedback mechanism for "A Life in Valoria" players.

[EDITORIAL: ED-686 — Conviction resolution states, Portrait Retirement, Draft Portrait. Source: campaign_architecture_v1 §7.]

**Contradiction:** If a Conviction directly contradicts a Duty (§3), the player must choose which to pursue in any scene where both are relevant. This choice is the game's central tension for non-leader characters — personal meaning vs institutional obligation.

### 2.4 Why Convictions Work

Convictions solve the "why does my character get out of bed" problem without railroading. The player decides what matters. The game responds by generating relevant opportunities. The player executes using the existing mechanical systems (combat, contest, fieldwork, Thread). The outcome feeds back into clocks, NPC states, and territory conditions. The cycle repeats.

Convictions also solve the "creative player" problem: a player who writes "I will forge a secret alliance between Varfell and the Restoration Movement" has invented a strategic objective that no NPC priority stack would generate. The game doesn't need to anticipate this — it needs to present scenes where the player can pursue it (meetings with Vaynard, meetings with Vossen, territories where both factions have Presence, contests where both factions' interests align).

---

## §3 — DUTIES

### 3.1 Definition

A Duty is a faction-assigned objective that the player's character is expected to pursue. It represents what the faction needs from the player this season. Duties are generated by the faction's current strategic state and issued by the faction leader (NPC or fellow player).

### 3.2 Generation

At the start of each season, the player's faction leader evaluates the faction's AI priority stack and assigns one Duty to the player character based on the highest-priority unaddressed need that matches the player's capabilities. Duty assignment considers:

- **Player's location:** Duties are assigned in territories the player can reach.
- **Player's skills:** Investigation duties for high-Cognition characters, diplomatic duties for high-Charisma characters, Thread duties for practitioners.
- **Faction urgency:** Survival-tier priorities (Stability ≤ 2) generate urgent defensive Duties. Expansion-tier priorities generate offensive Duties.

**Standing 0 carve-out (PP-661):** Duty assignment requires Standing ≥ 1. At Standing 0 (Petitioner), the player receives the **Initiation Duty** only — a faction-specific scene arc specified in faction_politics_v30 §1 that must be completed before standard Duty generation begins. The Initiation Duty is a fixed narrative gate, not drawn from the faction AI priority stack. Successful completion transitions the player to Standing 1 and activates the Duty system as defined below. See throughline_resolutions_v1 §2 for full reconciliation.

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

**Success:** Standing +1 (faction-specific track, 0–7 per faction_politics_v30 §1). Rank thresholds unlock (PP-661 revision):
- Standing 2 — faction intelligence access (rival stats, territory conditions)
- Standing 3 — council observation, specialty branch selection, Formal Recognition Event required
- Standing 4 — NPC officer sub-commands, +1 scene action
- Standing 5 — treaty-level standing, inner-circle adjacency
- Standing 6 — inner-circle voting, +2 scene actions, Hall Tier residency (see settlement_layer §1.4)
- Standing 7 — succession-eligible, Regent-Designate authority

**Failure:** Standing −1, floor-protected above Standing 1. A player who fails a Duty at Standing 1+ drops by 1 step but cannot fall below Standing 1 once initiated — the faction membership is durable absent explicit dismissal (see ED-647 for dismissal mechanics). A player at Standing 0 (Petitioner) who fails the Initiation Duty remains at Standing 0 until they retry, complete it, or declare for a different faction.

**Exceeding:** Completing the Duty AND producing additional value (discovered a conspiracy, turned an enemy NPC, generated Casus Belli). Standing +2 instead of +1.

### 3.5 Duty vs Conviction Tension

The game's richest moments emerge when Duty and Belief conflict. Examples:

- **Duty:** "Investigate Church activity in Gransol." **Conviction:** "I will prove to Almud that the Thread is real." The investigation might reveal Church corruption — useful for the Belief — but acting on that evidence publicly might destabilize the faction's Church relationship, failing the implicit diplomatic goal behind the Duty.

- **Duty:** "Protect Torben from Altonian influence." **Conviction:** "I will build a network of Thread-aware allies." Spending a scene action on Torben protection means one fewer action for network-building. The player must triage.

The game does not resolve this tension. The player does. And their choice defines their character.

---

## §4 — SCENE SLATE

### 4.1 Definition

At the start of each season's Personal Phase, the game generates a **Scene Slate**: a set of available scene opportunities drawn from the current game state. The player chooses which to pursue with their limited scene actions (3–5 per season, set by game difficulty).

### 4.2 Generation Algorithm

At the start of each season's Personal Phase, the game executes the following steps to produce the Scene Slate. Generation is deterministic — the same game state produces the same Slate.

**Settlement anchoring (per settlement_bridge_unification C-01):** Every Scene Slate entry specifies a settlement, not just a province. Province-level events (clock thresholds, faction crises) anchor to the province's Seat settlement by default. NPCs reside in specific settlements per NPC roster. Travel within a province is free; travel between provinces costs 1 scene action per province traversed.

**Step 1 — Mandatory Crisis (Priority 0 — cannot be declined):**

For each condition TRUE, generate one mandatory scene entry:
- Player is in or adjacent to a territory at Accord 0 (Revolt)
- Player is the target of an active Heresy Investigation
- A mass battle is occurring in the player's territory
- Player's faction leader is assassinated, overthrown, or incapacitated this season

Mandatory scenes consume 1 scene action each and cannot be deferred.

**Internal priority ordering** (when 2+ mandatories fire in same season — player chooses attendance order; revised per stress-test ED-761 to cover all §4.3.2 mandatory triggers):
1. Faction Leader Removal (succession-eligibility window may close).
2. Heresy Investigation Target (institutional jeopardy with deadline pressure).
3. Stability Crisis (faction-scale collapse; faction enters mandatory Crisis at all settlements).
4. Mass Battle in player's territory (single-event finality; aftermath scene per mass_battle §D.1 mandatory).
5. Knot Partner in Crisis (high-relational-stakes; arc-fork moment).
6. Companion Arc Trigger (narrative pivot; companion transformation).
7. Settlement Revolt / Accord 0 territory (governance failure with finite recovery window).
8. Rank Advancement Recognition Event (positive event, but constrained by inner-circle/rival presence per scale_transitions §4.3.2).

Player may override this ordering by explicit declaration. The ordering is a UX hint for triage, not a hard sequence.

**Mandatory overflow — Witness Mode (when mandatory count > scene action budget):**

1. Player chooses which mandatory scenes to attend personally (one per available scene action).
2. Remaining mandatory scenes resolve in **Witness Mode**: the player is present but cannot direct outcomes. Per Witness scene the player receives:
   - One free Read or Appraise action — **single roll required, not auto-success** (clarified per stress-test ED-761). Pool per standard Read/Appraise per fieldwork rules; Ob 1 (light, standard); cost: 0 scene actions (the "free" refers to scene-action cost, not roll outcome). Failure means the Witness's perception is unreliable; the player learns the surface event but not its undercurrents.
   - One narrative input opportunity at scene resolution (one sentence, GM may incorporate or reject; videogame: pre-scripted dialogue branch tagged to player Conviction). **[ED-WR-0007, 2026-07-08 — DISTILL]** This is a tabletop-GM mechanic ("GM may incorporate or reject") never re-derived for the engine's *no-GM* invariant — and because the scene's mechanical resolution has already proceeded via NPC AI (next bullet) before the sentence is offered, a branch-pick here changes no world-state outcome (Flavor-only). Fold the narrative-colour beat into the Read/Appraise outcome above: a Read/Appraise *success* additionally unlocks one flavour-tagged dialogue line at the next scene involving that NPC. No separate GM-less "narrative input" mechanic need be invented.
   - The scene's mechanical resolution proceeds via NPC AI as if the player had declined to engage.
3. Witness Mode does NOT generate Domain Echo (player did not act with Sufficient Scope per scale_transitions §7).
4. Witness Mode does NOT consume Momentum or Coherence.
5. The player learns scene outcomes the same season; the events do not become retrospective scenes (those fire only when player is fully absent — see §4.4 Where Were You).

[EDITORIAL: ED-745 — Mandatory overflow ('present but overwhelmed') state defined as Witness Mode. Internal priority ordering added. Source: 2026-04-24 audit completion §3.2 and §3.8.]

**Step 2 — Crisis Events (Priority 1 — presented, optional):**

For each condition TRUE, generate one scene entry:
- Any territory within 2 adjacencies of player at Accord ≤ 1
- Any NPC with Disposition ≥ +1 toward player has Scar count ≥ 2 (conviction crisis)
- Any NPC Knotted to the player has arc branch trigger condition met
- Any global clock crossed a band threshold this season (MS, CI, IP)
- Any NPC with Disposition ≥ +2 has an active Conviction that conflicts with their faction's current priority

**Step 2b — Thread-State Scenes (ED-674, Priority 1–3):**

Check local thread state (MS band × territory proximity per calamity_radiation_v30):

| Condition | Scene | Priority |
|---|---|---|
| MS ≤ 20 (Critical) in current territory | Thread Crisis: substrate instability manifests per radiation matrix | 1 (mandatory) |
| MS dropped below threshold band since last Slate | Threshold-Crossing: world visibly changes per radiation band | 2 |
| Active Gap in current territory | Investigation/Mending Opportunity at Gap site | 2 |
| Active Lock in current territory | Governance Rigidity: frozen policy/relationship manifests as obstruction | 3 |
| WC advanced since last Slate | Warden Cooperation: new Thread resources, new Warden NPC relationships | 3 |

Max 1 Thread-State scene per Slate. Highest priority fires.

**Step 3 — Duty-Aligned (Priority 2):**

Parse current Duty type. Generate 1–2 scenes matching Duty requirements:
- Investigate → scene in target territory with relevant NPC or location
- Diplomacy → scene with target NPC
- Governance → scene in target territory with local NPCs
- Protection → scene with threatened NPC or asset
- Other types → map to most relevant fieldwork activity

**Step 4 — Conviction-Aligned (Priority 3):**

For each active Conviction, scan for intersection with:
- **Named NPCs** (exact name match in Conviction text).
- **Faction references** (faction name match: Crown, Hafenmark, Varfell, Church, Löwenritter, Guilds, Restoration Movement, Wardens).
- **Territory references** (territory name match across all 17 territories T1-T17, plus colloquial names: Valorsplatz, Gransol, Himmelenger, Sigurdshelm, Lowenskyst, Ehrenfeld, etc.).
- **System keywords (~25):** Thread, Mending, Coherence, Heresy, Knot, Mandate, Order (capitalized = settlement Order or faction stat), Restoration, Warden, Southernmost, Confessor, Parliament, Dynasty, Regency, Occupation, Accord, Treaty, Investigation, Einhir, Calamity, Church, Crown, Hafenmark, Varfell, Standing, Renown.
- **Role references** (resolve to canonical NPC): "the king" → Almud; "the Confessor" → Himlensendt; "the duchess" → Baralta; "the duke" → Vaynard (or Maret Uln post-succession); "the queen" → Lenneth; "the prince" → Torben; "the princess" → Elske; "the grandmaster" → Ehrenwall; "the spymaster" → Thale; "the lord treasurer" → Reichard; "the royal marshal" → Voss.

**Validator (extended per ED-766):** at character creation and at each Conviction revision, scan the new Conviction text for matches across all five categories.

**Match severity classification:**
- **Strong match:** capitalized exact-name (e.g., "Almud", "Crown", "Thread") — high confidence the player intended the system-keyword reading.
- **Weak match:** lowercase form of a system keyword that is ambiguous with common-English usage (e.g., "order" vs "Order", "crown" vs "Crown"). Could be incidental rather than intentional reference.
- **No match:** zero candidates in any category.

**Validator behavior by match type:**
- **0 matches:** display non-blocking warning "This Conviction will not generate scenes via Step 4 unless you reference a specific NPC, faction, territory, system topic, or role. Refine?"
- **Weak match only:** display an explicit confirmation prompt — "Did you mean the system entity **[System keyword X]** (this will generate Step-4 scenes about it), or the everyday sense (no Step-4 scenes)?" Player picks *system entity* → strong match, fires Step 4; picks *everyday sense* → no Step-4 firing for that match. **[ED-WR-0007, 2026-07-08 — REFINE]** This replaces the former capitalization-as-signal heuristic ("capitalize it if you meant Order"): encoding intent through punctuation was a second-order rule not restatable in one breath with the core scan-and-match rule (Q-elegant fail), and a lowercase "the crown on his head" would silently never fire Step 4 with only a non-blocking hint as the tell. The explicit prompt makes intent a direct choice, not a convention the player must already know.
- **Strong match (any):** no warning. Step 4 fires for the matched topic.

This prevents both false-negative (zero-match Conviction missed) and false-positive (incidental keyword match firing wrong scenes) at character creation. The disambiguation is an explicit yes/no confirmation at Conviction-write time (ED-WR-0007), where the player has the most context to clarify intent — not a silent capitalization convention.

For each intersection found, generate one scene entry with the matching NPC/location. Maximum 3 Conviction-generated scenes.

[EDITORIAL: ED-746 — Step 4 keyword list expanded from 6 to ~25 terms; role-reference resolution table (11 mappings); validator added. Source: 2026-04-24 audit (scene_slate §2.1 P2 #2).]

**Step 5 — NPC Outreach (Priority 3):**

For each named NPC where ALL hold: Disposition ≥ +2 toward player, NPC has active Conviction relevant to player's location or faction, NPC's priority tree fired an action this season that could benefit from player involvement — generate one scene: "[NPC] seeks to meet with you. [Agenda description]."

For each named NPC where ALL hold: Disposition ≤ −2 toward player, NPC holds institutional authority over player's territory, NPC's priority tree fired an action targeting player's faction — generate one scene: "[NPC] has summoned you. [Demand description]." Declining a demand: Disposition −1 with the NPC, +1 Exposure in their territory.

**Step 6 — Territorial Texture (Priority 4):**

Generate 1–2 scenes from the player's current territory: trade/economic event, military movement.

**[ED-WR-0007, 2026-07-08 — pessimist-action audit MERGE + one clause CUT]** Two of this Step's former sub-rules are folded into more rigorous siblings, leaving Step 6 as "Territorial Texture" (the two genuinely-novel ambient-political sub-rules above): **NPC arrival → MERGE into Step 5 (NPC Outreach)**, which gates the same "an NPC shows up" content on Disposition thresholds + a fired priority tree (Step 6's version was ungated duplicate coverage). **Thread phenomenon (MS ≤ 60) → CUT**, not merged: Step 2b (Thread-State Scenes) already owns the local-MS-band condition with a stricter trigger *and* an explicit max-1-per-Slate discipline Step 6 lacked — a second undisciplined Thread row would either be dead weight or violate Step 2b's "max 1" rule. (The clause is CUT rather than merged specifically to protect Step 2b's scarcity discipline.) Step 6 also absorbs Step 7's backfill role, below.

**Step 7 — Ambient (Priority 5):**

Generate 1 ambient scene: unstructured encounter offering low-stakes information or minor relationship opportunity.

**[ED-WR-0007, 2026-07-08 — DISTILL]** Ambient's own §4.5 consequence entry is "No consequence. The world moved on." — as-specified it is a Flavor-only Step (a dedicated priority tier, pruning-table row, and consequence-table row for a mechanic that by its own text changes nothing). Its one real function — never surfacing an emptier Slate than the difficulty band's floor — is **distilled into a backfill clause on Step 6 (Territorial Texture)**: when Steps 1–6 underfill the Slate, Step 6 backfills to the band floor with a low-stakes encounter. No standalone Ambient Step, priority tier, or consequence row is required. (Retained as a numbered anchor here until a Scene-Slate rebuild renumbers §4.2/§4.3/§4.5; the decision binds now.)

### 4.2b Slate Presentation

Each entry shows: NPC name and location, one-sentence description, tag(s) indicating which Conviction/Duty/game-state condition generated this entry, and priority level (visible to the player).

### 4.3 Scene Slate Size

The Slate presents more opportunities than the player can pursue:
- At game difficulty Normal: 5–7 opportunities per season, 4 scene actions.
- At game difficulty Hard: 7–9 opportunities, 3 scene actions.
- At game difficulty Narrative: 4–5 opportunities, 5 scene actions.

The surplus is the point. Opportunities not pursued resolve through NPC AI and clock advancement — the revolt you didn't attend to resolves based on garrison strength alone. The NPC whose arc moment you missed makes their decision based on their conviction, without your input. The Thread instability you didn't Mend persists and worsens.

**Cross-step pruning algorithm (deterministic):**

1. Generate all entries from Steps 1–7 + 2b. Tag each with `(step_number, internal_index_within_step)`.
2. Mandatory entries (Step 1 + Step 2b at MS ≤ 20) cannot be pruned. Add all to slate.
3. Compute `slate_target_size` from difficulty (4-5 Narrative / 5-7 Normal / 7-9 Hard). Compute `remaining_slots = slate_target_size − count(mandatory)`.
4. If `remaining_slots ≤ 0`: slate is mandatory-only. Witness Mode applies per §4.2 Step 1.
5. Otherwise: from non-mandatory entries, sort by `(step_number ascending, internal_index ascending)`. Take first `remaining_slots`.
6. `internal_index_within_step` is deterministic per step:
   - Step 2 (Crisis Events): proximity to player (closest first), then trigger order in spec.
   - Step 2b (Thread-State): condition priority order in §4.2 Step 2b table.
   - Step 3 (Duty-Aligned): single Duty per player, so internal index = 0; if 2 entries, ordered by target territory proximity.
   - Step 4 (Conviction-Aligned): Conviction declaration order at character creation/revision (Conviction #1 first, etc.).
   - Step 5 (NPC Outreach): NPC Disposition descending (highest first), then Renown descending.
   - Step 6 (Territorial): trigger condition order in §4.2 Step 6.
   - Step 7 (Ambient): single entry, internal index = 0.

Generation is deterministic — same game state produces same Slate. Pruning is deterministic — same entry-set produces same final Slate.

[EDITORIAL: ED-747 — Cross-step pruning algorithm specified. Source: 2026-04-24 audit completion §3.1.]

### 4.4 Scene Resolution

Each scene opportunity, when selected, places the player in a specific location with specific NPCs and specific initial conditions. The player then uses the existing mechanical systems:

- Scene involves a hostile NPC → combat or social contest, player's choice.
- Scene involves information → investigation actions.
- Scene involves an NPC relationship → socializing actions (Connect, Read).
- Scene involves Thread phenomena → Thread operations (if capable) or observation (if not).
- Scene involves a territory → governance, stealth, or exploration.

A single scene may involve multiple systems. Interviewing a reluctant NPC might require: Read (Appraise to identify pressure point), Connect (improve Disposition first), then Interview (extract information) — three fieldwork actions consuming one scene action if the player is efficient, or stretching across multiple scene actions if the NPC is resistant.

### 4.5 Opportunities Not Pursued

Unpursued opportunities produce consequences. The world does not pause for the protagonist.

| Entry Source | Resolution When Not Pursued |
|-------------|---------------------------|
| NPC arc moment (Priority 1) | NPC resolves based on their Conviction and AI priority. Conviction Scar may occur without player influence. Player's Disposition with NPC unchanged (they were not involved). |
| Territory crisis (Priority 0–1) | Faction AI handles via Govern roll at faction stat level. Accord adjusts based on result. |
| Clock threshold (Priority 1) | Effects propagate normally. No player mitigation. |
| Duty-aligned (Priority 2) | Duty not completed. Standing −1 at Accounting. |
| NPC Outreach (Priority 3) | NPC acts without player. Disposition −1 if NPC Disposition was ≥ +3 (NPC feels ignored). |
| NPC Demand (Priority 3) | Disposition −1 with NPC. +1 Exposure. Potential escalation (Heresy Investigation, military action) at NPC discretion per priority tree. |
| Territorial (Priority 4) | Event resolves through ambient systems. Opportunity lost permanently. |
| Ambient (Priority 5) | No consequence. The world moved on. |

The player cannot prevent the world from moving. They can only choose where to be when it does.

---

## §5 — STATURE PROGRESSION

### 5.1 Stature Levels (revised 2026-04-17, PP-660)

The player's relationship to the faction layer changes as they accumulate Standing. The Standing ladder runs 0–7, with faction-specific titles specified in faction_politics_v30.md §1:

| Standing | Stature | Faction Relationship |
|----------|---------|---------------------|
| 0 | Petitioner | Pre-initiation status. No Duty assignment yet. Sees public faction state only. Must complete an Initiation Duty (see §3.3) to advance. |
| 1 | Operative | Receives Duties. Sees public faction state. |
| 2 | Agent | Receives Duties. Sees faction intelligence (rival faction stats, territory conditions). Can suggest Domain Actions to leader (non-binding). |
| 3 | Counselor | Receives Duties but can negotiate or refuse. Invited to faction council — sees the leader's priority evaluation and can argue for different priorities via social contest. Specialty branch unlocks (faction-specific — see expansion §1). |
| 4 | Lieutenant | Can issue sub-commands to NPC officers (direct minor NPC actions). Duty becomes a strategic directive rather than a specific task. One bonus scene action per season from faction resources. |
| 5 | Senior | Council voting member. May speak in faction's name in limited negotiations. Inner-circle-adjacent (sees inner-circle deliberation). |
| 6 | Prince/Chancellor/Senior-Jarl/Cardinal | Inner-circle voting member. May initiate Ministry reforms. Two scene actions per season. Nomination authority for junior ranks. |
| 7 | Regent-Designate | Succession-eligible. May act in leader's name in their absence (with Legitimacy Token damage per POW-03). At this level, the player can initiate a leadership challenge OR succeed on leader vacancy. |

Full rank specification (titles, initiation gates, hall tier, livery, mentor, demotion) per faction in faction_politics_v30.md §1.

### 5.2 Leadership Acquisition

When a faction leader is removed (Almud overthrown by Coup, Himlensendt's Crisis of Faith, Baralta's succession, Vaynard's death), the game evaluates succession:

- If the player is Standing 7 in that faction: they are offered leadership (per the Regent-Designate role). Accepting transforms them from operative to leader — they now issue Domain Actions directly, play the faction's card hand, and lose the Duty system (replaced by faction AI evaluation as their "advisor").
- If the player is Standing 5–6: succession contest per SUC-01 through SUC-03 (see faction_politics_v30.md, section correspondence not verified — its Part 2 is Sub-Office Rank Ladders, not succession; the succession-contest material now appears to live in Part 1's rank tables and Part 6's Baralta-outcome cascades instead). <!-- [flag: section correspondence not verified, ED-IN-0016] --> Inner-circle support determines outcome.
- If the player is below Standing 5: succession follows the canonical NPC rules (Torben inherits Crown, Cardinals contend for Church, Maret Uln may inherit Varfell, Baralta's succession under Option A/B per baralta_crown_claim_v30).

Leadership can also be seized: a Standing 4+ character can call a leadership challenge at any time via social contest against the current leader, with the faction council as expert adjudicator (Cognition-based). Success: player becomes faction leader. Failure: Standing drops to 2, Disposition with deposed leader drops to −4.

[EDITORIAL: ED-634 — Ladder rewrite per faction_politics_v30.md §1. Faction-specific titles and full progression gates specified there.]

### 5.3 Staying Independent

A player can choose to refuse faction alignment entirely or abandon their faction. An independent character:
- Receives no Duties.
- Generates their own scene opportunities from Convictions only.
- Has no faction stat pool for Domain Actions — until Renown 7+ (see §5.4).
- Cannot participate in Parliament or faction military.
- CAN pursue Thread operations, fieldwork, and personal combat freely.
- CAN build relationships with NPCs across all factions without factional Disposition penalties.

This is the Disco Elysium path — the player is an investigator, a Thread practitioner, a wanderer. Their impact on the game world comes through personal-scale actions and their Domain Echoes, not through institutional authority. At low Renown, this path is harder. At Renown 7+, the player's personal authority substitutes for institutional backing (see §5.4).

### 5.4 Renown Track (Cross-Faction Personal Authority)

Standing (0–5) measures the player's relationship with one faction. Renown (0–10) measures the player's personal significance across the peninsula. Renown persists across faction changes and survives faction collapse.

**Renown Sources:**

| Source | Renown Gained | Condition |
|--------|--------------|-----------|
| Conviction resolved (Fulfilled or Transformed per §2.3) | +1 | Per ED-793. Failed and Unresolved states do NOT grant Renown (Failed grants +1 Momentum only per §2.3; Unresolved grants nothing). |
| Duty exceeded | +1 | Duty completed with Exceeding result per §3.4 |
| Domain Echo produced | +1 | Any personal-scale action that fires Domain Echo per scale_transitions §5 |
| NPC arc influenced | +1 | Player action causes NPC Conviction Scar per npc_behavior §3.2 |
| Investigation resolved (Complex+) | +1 | Evidence Track threshold 5+ reached per fieldwork §4.1 |
| Mass battle participated | +1 | Player present for mass battle resolution |
| Territory Accord improved | +1 | Player governs territory and Accord increases during tenure |
| Knot formed | +1 | New Knot established with named NPC |

**Cap:** +2 Renown per season maximum. Renown does not decay naturally.

**Governance Responsibility (derived_stats_v1 §8.3):** Players at Standing ≥ 3 who hold governance positions risk Renown from governance failures. Accord drops in governed territory, faction Treasury reaching 0, or battle losses in governed territory each cost Renown −1 (cap: −2/season). Leadership is earned through the Renown track and risked through governance stakes.

**Renown Thresholds and Governance Scope:** See settlement_layer_v30 §6.1 for the unified stature ladder mapping Renown thresholds to settlement governance scope, faction emergence stages, and ROTK/CK3 parallels. Renown is the quantitative axis; settlement control is the qualitative axis.

**Renown effects that are independent of governance scope:**

| Renown | Effect |
|--------|--------|
| 3+ | NPCs at neutral Disposition start at +1 instead of 0. |
| 5+ | +1D on Impress actions. Cross-faction Domain Action suggestions. |
| 7+ | Independent Domain Action: floor(Renown ÷ 2) as pool. |
| 9+ | May call Grand Contest at any time. All factions evaluate player at Priority 2. |

**Standing and Renown are independent.** Standing 5 / Renown 3 = faction insider without cross-faction reputation. Standing 0 / Renown 8 = independent operator with personal authority. Both are viable.

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

- **Standing 4–5 (Lieutenant/Senior):** +1 scene action from faction resources.
- **Standing 6–7 (Inner Circle/Regent-Designate):** +2 scene actions from faction resources.
- **Knot with a local NPC:** +1 scene action in that NPC's territory (the relationship opens doors that save time).
- **Out of Breath (Stamina 0):** −1 scene action (physical exhaustion limits your capacity).
- **Wounded (2+ Wounds):** −1 scene action (injuries slow you down).

### 6.3 Scene Action Economy

One scene action = one scene opportunity pursued. A scene contains 1–3 mechanical interactions (a fieldwork action, a social roll, a combat exchange, a Thread operation). Scenes that require extended engagement (multi-exchange social contest, complex investigation, sustained Thread operation) may consume 2 scene actions.

The scene action budget is the game's primary pacing lever. It determines how much the player can influence per season, and therefore how quickly the game converges toward victory or shared loss.

---

## §7 — INTEGRATION WITH EXISTING SYSTEMS

### 7.1 Character Creation (params_core)

Character creation steps (revised PP-661 for caste + Initiation integration):

1. **Write 3 Convictions** (per §2.2). One should relate to a personal goal, one to a faction concern, one to a relationship or NPC.
2. **Choose caste background** (new PP-661 step): Northern Einhir / Central Einhir / Southern Einhir. See faction_politics_v30 §3.1 for caste definitions.
3. **Review Viability Matrix** (new PP-661 display): 4-faction × 3-caste × specialty-branch grid showing which combinations play at Favored (★★★), Standard (★★), Gated (★), or Closed (✕) difficulty. See throughline_resolutions_v1 §1.3 for the canonical matrix.
4. **Choose faction alignment** (or independent) — with the Viability Matrix visible.
5. **If faction member:** the specialty branch (where applicable — Crown, Hafenmark, Varfell, Church) is selected at Standing 3 via in-game Formal Recognition Event, not at character creation. At character creation the player may only *indicate* intent for GM use.
6. **Derived: Starting Standing = 0 (Petitioner)** for faction members; independent characters have no Standing. *(Change from prior spec which derived Standing = 1 — PP-660 introduced the Standing 0 Petitioner state with Initiation Duty; character creation now aligns.)*
7. **Display Initiation Duty preview** — the first-season scene the faction-aligned character will play. See faction_politics_v30 §1 for per-faction Initiation Duties.

**Advisory text (canonical, display to players):**

> Valoria's caste system is not a difficulty setting. It is a structural feature of the peninsula's politics. A Southern Einhir character facing the Crown is not playing a harder version of the same game — they are playing a different game, one where covert paths (Riskbreakers, Niflhel, Wardens) are structurally open while overt institutional advancement is structurally difficult. A Northern Einhir character facing Varfell's Cultural branch faces the mirror challenge. If this is your first Valoria campaign, a Standard (★★) or Favored (★★★) pairing is recommended. A Gated (★) or Closed (✕) pairing is a deliberate thematic commitment, not a mistake. Both produce valid stories.

[EDITORIAL: ED-659 — Character creation caste + viability onboarding applied PP-661.]

### 7.2 Season Structure (board_game_v30)

Revise the three-phase season:
- **Phase 1a — Duty Assignment.** Faction leader evaluates priority stack, assigns Duty to player character.
- **Phase 1b — Scene Slate Generation.** Game generates 4–9 opportunities from five sources.
- **Phase 1c — Personal Phase.** Player chooses and resolves scene actions.
- **Phase 2 — Strategic Phase.** Domain Actions as existing.
- **Phase 3 — Accounting.** As existing, plus: Standing update (Duty success/failure), Conviction review (player may revise Convictions).

### 7.3 Fieldwork (fieldwork_v30)

No changes to mechanics. Scene generation integrates fieldwork as the primary personal-phase activity type.

### 7.4 Scale Transitions (scale_transitions_v30)

Scene Slate Priority 1 (crisis events) provides the missing Zoom In triggers. When a clock threshold is crossed or an NPC arc moment fires, the game generates a scene opportunity that the player can pursue — this IS the Zoom In moment. The Slate does not force the player into the scene (unlike a mandatory Zoom In). It offers the scene. The player decides whether to spend a scene action on it. If they don't, the crisis resolves through NPC AI.

This solves ED-545 (only 5 Zoom In triggers) structurally: the Scene Slate IS the Zoom In trigger system. Any game state change that would be interesting to experience personally becomes a scene opportunity in the Slate.

### 7.5 NPC Behavior (npc_behavior_v30)

NPC faction leaders generate Duties by evaluating their AI priority stack. The Duty is the highest-priority item that the player character could plausibly address. This gives the NPC AI a new output: not just "what action does the faction take" but "what mission does the faction assign to the player."

### 7.6 Emergent Arcs

Convictions function as player-authored arc vectors. They have a source (the player), a direction (the Belief statement), and conditions that modulate their strength (NPC relationships, territory access, system knowledge). They integrate with the existing vector-based arc architecture: player Convictions are active pressures that intersect with NPC arc pressures and clock pressures to produce emergent narrative.

---

## §8 — WHAT THIS SOLVES

| Problem | Solution |
|---------|----------|
| "Why does my character act?" | Convictions provide self-authored motivation. Duties provide faction-assigned motivation. |
| "What are my options?" | Scene Slate presents 4–9 opportunities per season, generated from game state. |
| "Why can't I do everything?" | Scene action budget (3–5) forces triage. Unpursued opportunities resolve without player input. |
| "How do I gain political influence?" | Standing track (0–5) represents faction trust, earned through Duty completion. |
| "Can I become the faction leader?" | Standing 5 enables succession or leadership challenge. |
| "What if I don't want to serve a faction?" | Independent path sacrifices faction resources for cross-faction freedom. |
| "Why does investigation matter?" | Evidence feeds Corroboration, Casus Belli, NPC arc triggers, and Conviction fulfillment. |
| "How do I know what's happening in the world?" | Scene Slate surfaces world events relevant to the player's location, Beliefs, and Duties. |
| ED-545 (Zoom In triggers) | Scene Slate Priority 1 IS the Zoom In system — any game state change generates a scene opportunity. |
| ED-546 (RM actor) | An independent player aligned with RM pursues RM Beliefs without faction infrastructure. RM Community Organizing is a scene opportunity in territories with Piety ≤ 1. |
| ED-547 (Fieldwork resource cost) | Scene action budget IS the fieldwork cost — each investigation scene costs a scene action that could have been spent elsewhere. |

---

## §9 — RESOURCES (Throughline T2)

Personal economic capacity. Range: 0–5. Cap: 5.

| Resources | Meaning |
|-----------|---------|
| 0 | Destitute. Cannot afford lodging, equipment, or services. |
| 1 | Subsistence. Basic needs met. |
| 2 | Comfortable. Equipment, travel, modest bribes. |
| 3 | Prosperous. Fund small operations, hire agents, maintain household. |
| 4 | Wealthy. Military equipment, sponsorships, settlement investment. |
| 5 | Magnate. Faction-level economic influence. |

**Starting Resources:** Crown officer: 2. Hafenmark merchant: 3. Varfell scholar: 2. Church functionary: 2. RM organizer: 1. Independent: 1.

**Sources:** Faction salary (+1/season at Standing 2+, +2 at Standing 4+). Settlement governance (+1/season per settlement with Prosperity ≥ 3). Guild contracts (+1 to +3, one-time — includes trade ventures in Port/City settlements, Ob varying by the settlement's Trade stat). Loot (+1 per valuable). Gifts received (+1).

**Uses:** Equipment (1). Bribe/gift (1). Hire agent for 1 season (2). Military equipment upgrade (3). Economic Leverage via personal Resources (3).

**[ED-SE-0005, 2026-07-08 — SE subtractive-action reconciliation.]** Three former §9 economic verbs are consolidated per the ratified pessimist-action audit (`designs/audit/2026-07-08-pessimist-action-audit/`, ED-IN-0027): the standalone **Trade** income roll is PRUNED (personal-only, mechanically indistinct from the other income sources) and folded into *Guild contracts* as its Port/City trade case (above); **Fund settlement development +1D** is MERGED into the `Develop` governance verb's funding structure (the Treasury method in `governance_play_redesign_v1`), rather than carried as a parallel flat dice-bonus purchase; and the free **Sponsor settlement event** (Order +1, no downside) is retired into the single canonical **Sponsor** governance verb, which carries a recurring **Debt** obligation (`governance_play_redesign_v1` §1.3) — closing the dominant-strategy duplication in which the free version strictly dominated the obligation-bearing one.

---

## §10 — CONVICTION LEGACY (Throughline T8)

When a player character retires or dies, the player designates one active Conviction as a Legacy Conviction. The new character inherits it transformed:

- Unfulfilled goal "I will [X]" → "I will complete what [predecessor] began" or "I will understand why [predecessor] failed"
- Fulfilled goal "I will [X]" → "I will protect [predecessor]'s achievement" or "I will surpass what [predecessor] built"
- Relationship "I will [NPC]" → "I will honor [predecessor]'s bond with [NPC]" (if alive) or "I will carry [predecessor]'s grief" (if dead)

Legacy Conviction occupies 1 of 3 Conviction slots. Can be revised normally. Renown inherited: floor(predecessor ÷ 2). Dispositions: predecessor's allies (+3) start at +1; enemies (−2) start at −1; others at 0. Knotted NPCs: Knot does not transfer but +1D on first Connect (Knot scar). Settlement governance transfers to designated protégé automatically.

---

## §11 — LINEAGE ACTS

When a character retires (via Portrait Retirement, §2.3) or dies, the player may start a new character in the same world. Lineage Acts determine what carries over. Three types:

### 11.1 Mentorship

**What carries over:** Skills at 60% of predecessor's values, Founded Organization membership, 1 Close Knot (Disposition −2 from predecessor's value).

**How established:** Scene: Designate a mentee. Must be an existing NPC with Disposition ≥ +3. The mentee becomes the new player character.

### 11.2 Succession

**What carries over:** Social standing, titles, faction affiliation, estates. Settlement governance transfers automatically.

**How established:** Automatic if the character has declared an heir through dialogue or scene during the campaign. If no heir was declared, succession follows canonical NPC rules (faction-specific).

### 11.3 Thread Legacy

**What carries over:** Warden Recognition (WR) at half (rounded down), Thread knowledge (operations known), Knot Legacy embedded in substrate.

**How established:** Scene: Embed knowledge into a Knot. Requires WR ≥ 2. The embedded Knot is discoverable by a future practitioner — this is what the Wardens do. The successor character can find the Knot Legacy through fieldwork investigation (Evidence Track threshold 3 at the embedding site).

### 11.4 No Lineage Act

If no Lineage Act was established before death or retirement: the player starts a new character with no mechanical inheritance. The predecessor's Portrait is recorded. The world continues. Death without preparation is a clean break, not a punishment.

### 11.5 Lineage and §10 Conviction Legacy Interaction

Lineage Acts and Conviction Legacy (§10) are independent systems that fire simultaneously. A retiring character designates both a Legacy Conviction (§10) AND a Lineage Act (§11). The new character inherits both: the transformed Conviction occupies one slot, and the Lineage Act determines what mechanical state carries over.

[EDITORIAL: ED-687 — Lineage Acts. Source: victory revision proposal v2 §1.7.1, analysis §1.5.]
