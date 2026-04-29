<!-- [PROVISIONAL: 2026-04-28 session — d964fd13158349fa] -->
<!-- STATUS: PROVISIONAL — design exploration, not canonical mechanic -->
<!-- TITLE: Ground-Up Mechanical Proposal -->
<!-- POSITION IN ARC: see designs/audit/2026-04-28-political-dynamics-session/00_session_index.md -->
<!-- VETTING: see 07_armature_system_vetting.md for canonical framework assessment -->

# NPCs as Autonomous Actors: Ground-Up Mechanical Proposal

## Part 1: The Proposal

### 1.1 Scope

This specifies the engine-level architecture for treating named NPCs as autonomous political actors in Valoria. It replaces the implicit "AI priority tree responds to player actions" model with an explicit inner-state architecture that produces NPC behavior independent of player involvement.

The proposal covers:
- Per-NPC data structures (Identity, State, Relations, Memories, Hooks)
- Five engine procedures (Mood, Concerns, Projects, Opinions, Interactions)
- Integration with existing Valoria systems (Disposition, Convictions, Beliefs, Scars, Standing, Domain Actions, Scene Slate)
- Computational budget (what runs at what frequency for how many NPCs)

### 1.2 NPC Tier Stratification

Not all NPCs need full inner-state architecture. Three tiers:

| Tier | Population | Inner state |
|---|---|---|
| **Active** | ~35 named NPCs (existing soft cap) | Full architecture: all data structures, all procedures |
| **Passive** | ~50 minor named NPCs (parish priests, settlement mayors, junior officers) | Lite architecture: Conviction, Disposition, 1 Concern, 1 Opinion of player, 3 Memories |
| **Population** | All others (anonymous townsfolk, soldiers, merchants) | Statistical only: faction Disposition averages, Order/Prosperity contribution |

**Why stratification matters:** Without it, the system either dies at the settlement layer (no minor NPCs with inner state means cascades stop) or becomes computationally intractable (full state for hundreds of NPCs). Lite architecture lets minor NPCs participate in cascades without overwhelming the engine.

### 1.3 Per-NPC Data Structures

#### Identity (static, set at NPC creation)

```
Conviction_primary: one of {Faith, Order, Reason, Equity, Precedent, Autonomy, Continuity}
Conviction_secondary: one of the above (or None)
Backstory_tags: 5–8 tags (e.g., "lost-sibling-eshlund", "trained-by-ehrenwall", 
                "second-son", "stillhelm-survivor")
Personality:
    risk_tolerance: −2 to +2
    social_warmth: −2 to +2  
    intellectual_rigor: −2 to +2
    institutional_deference: −2 to +2
```

Personality is set at NPC creation and does not change. It modifies how the NPC interprets identical events. A high-rigor NPC investigates ambiguous information; a low-rigor NPC accepts the most emotionally satisfying explanation.

#### State (dynamic, updated each season)

```
mood: one of {Steady, Anxious, Confident, Grieving, Vindicated, Humiliated, 
              Distracted, Resolved}
mood_duration: seasons remaining at current state
beliefs: existing system (2-3 per NPC)
scars: existing system (count of revised Beliefs)
disposition_with_player: existing system (-3 to +5)
certainty: existing system (0-5, optional per NPC)
ts: existing system (Thread Sensitivity, optional per NPC)
```

#### Concerns (1-3 active per NPC)

```
Concern:
    question: text (e.g., "Why did Almud agree to the Varfell alliance?")
    source_event: ref to event that generated the Concern
    salience: 1-5 (decays -1 per season unless reinforced)
    ttl: seasons until forced resolution
    seeking: tag describing what would resolve it 
             (e.g., "evidence-about-treaty-counsel")
    resolution: when satisfied, becomes a Belief or modifies an Opinion
```

Concerns generate when:
- Faction-level event affects the NPC's domain
- Another NPC's behavior contradicts an existing Belief
- Player action is ambiguous from the NPC's frame
- A Project hits an obstacle

When salience reaches 0, the Concern resolves with whatever information the NPC has accumulated. The resolution may be wrong.

#### Projects (1-2 active per NPC)

```
Project:
    goal: text (e.g., "Train Torben to be a war-leader before Almud dies")
    progress: 0-10
    blockers: list of conditions preventing advancement
    accelerators: list of conditions enabling rapid advancement  
    horizon: short/medium/long (1-3 / 4-8 / 9+ seasons)
    visible_actions: actions the NPC takes when advancing this Project 
                     (these are what the player observes)
    completion_effect: what happens when Project succeeds
    failure_effect: what happens when Project fails
```

Projects are seeded at NPC creation (1 starting Project per Active NPC) and replaced as they complete or fail. Active NPCs may also generate new Projects in response to major life events (Conviction Scar, succession of mentor, settlement transformation).

#### Opinions (one per politically-relevant other NPC, ~5-10 per Active NPC)

```
Opinion of <NPC_id>:
    affect: text descriptor (e.g., "wary, slightly contemptuous")
    affect_axis: -3 to +3 (numeric for engine logic)
    story: text (the narrative this NPC tells about the other)
    evidence: list of Memory refs supporting the Opinion
    confidence: 1-5 (how strongly held; affects hysteresis)
    last_updated: season ref
```

Opinions update from new Memories. Strong Opinions (confidence 4+) require accumulated contradicting evidence to flip. Weak Opinions (confidence 1-2) flip on single events.

#### Memories (5-10 high-salience records)

```
Memory:
    timestamp: season ref
    event_type: tag (e.g., "promotion", "betrayal", "shared-crisis", "insult")
    participants: list of NPC ids and (optionally) player ref
    affect: text descriptor + numeric (-3 to +3)
    salience: 1-5 (decays -1 per 4 seasons unless reinforced)
    detail: short text (the specific thing remembered)
```

When a new high-salience Memory would exceed the cap (10), the lowest-salience existing Memory is either dropped or merged ("another disappointment from the Crown" — collapses several similar Memories into a generalization).

#### Behavioral Hooks (computed, not stored)

These are the engine outputs that connect inner state to player-facing behavior:

- **Decision modifier:** Active Concerns and current Mood adjust the NPC's AI priority tree at decision time. Default priority weights ±1 per relevant Concern and ±1 per Mood category.
- **Outreach generator:** Concerns and Projects with player-relevant tags can generate Scene Slate entries (existing §8.11, augmented).
- **Dialogue tone:** Mood determines which dialogue variant is selected when the NPC speaks to or about the player.

### 1.4 Engine Procedures

Five procedures, each with a defined trigger and frequency.

#### Procedure A: Mood Update

**Trigger:** every event resolution (scene end, Domain Action result, Accounting)

**Logic:** 
- Significant events change Mood per a transition table. Examples:
  - Successful Domain Action proposal → Confident (1-2 seasons)
  - Treaty contradicting primary Conviction → Anxious or Humiliated based on advocacy involvement
  - Knot partner death → Grieving (2-4 seasons)
  - Conviction Scar acquired → Distracted (1 season)
- Each Accounting, Mood decays 1 step toward Steady unless reinforced this season.
- Personality modifies decay rates: high social_warmth recovers from negative Moods faster; high intellectual_rigor stabilizes faster from Vindicated to Steady.

#### Procedure B: Concern Generation and Resolution

**Trigger:** event resolution (generation), Accounting (resolution check)

**Generation:**
- Treaty signed, Conviction-misaligned: Concern "Why did this happen?" generated for relevant NPCs
- Player observed in unexpected context (cross-faction meeting, etc.): Concern "What is the player doing?" 
- NPC's Belief contradicted by event: Concern "Was I wrong about X?"
- Project blocker discovered: Concern "How do I bypass this?"
- Personality modifies Concern generation: high intellectual_rigor generates more Concerns; high institutional_deference suppresses Concerns about superiors

**Resolution:**
- At each Accounting, each Concern checks its seeking tag against accumulated evidence
- If sufficient evidence: Concern resolves to a Belief or Opinion update. The resolution may be incorrect — it reflects what the NPC concluded from available information, not objective truth
- If salience reaches 0: forced resolution with whatever evidence exists (often produces wrong conclusions, which generates Beliefs that cause future political problems)

#### Procedure C: Project Advancement

**Trigger:** Accounting

**Logic:**
- For each Active NPC, evaluate their primary Project
- If priority tree has discretionary capacity (no faction-mandated action this season, or NPC's Standing permits private action), advance Project by 1 progress
- Project advancement actions are *visible* to observers — the action the NPC takes is the visible_actions field, which appears in the world (a meeting, a research trip, a private conversation)
- If Project hits a blocker, generate a Concern about how to bypass it
- If Project completes, fire completion_effect (Opinion shifts, faction stat changes, new Beliefs)

**Project conflict resolution:** when an NPC's faction priorities conflict with their Project, faction priorities win. But sustained suppression (Project blocked for 4+ seasons) generates a Conviction-tension Concern: "Is this institution still my home?"

#### Procedure D: Opinion Drift

**Trigger:** Accounting

**Logic:**
- For each Opinion held by each Active NPC:
  - Check Memories created this season involving the Opinion's subject
  - If new Memory aligns with current Opinion: confidence +0 to +1 (Opinion strengthens)
  - If new Memory contradicts current Opinion: 
    - If confidence ≤ 2: Opinion shifts (affect updates, story updates, confidence resets)
    - If confidence ≥ 3: cognitive dissonance; Opinion holds but a Concern is generated ("Is X who I thought they were?")
    - If confidence is 4-5 and contradiction is acute: Mood shifts to Distracted, Opinion holds but with a Memory tagged "complication"
- Personality modifies: high intellectual_rigor lowers confidence threshold for Opinion shift; high institutional_deference raises it for superiors

#### Procedure E: NPC-NPC Off-Screen Interaction

**Trigger:** Accounting

**Budget:** Each Active NPC participates in up to 2 off-screen interactions per season. Total interaction budget: ~70 events per season across all Active NPCs.

**Selection:**
- Engine prioritizes pairs with: (a) shared Concerns, (b) intersecting Projects, (c) recent Memory involving both, (d) RP-equivalent (mutual affect_axis sum ≥ +4 or ≤ −4).
- Selected pairs each generate one off-screen interaction.

**Resolution:**
- Each interaction has a *type* (private conversation, shared scene, professional collaboration, public confrontation) determined by their respective Projects/Concerns
- Outcome modifies both NPCs' Opinions of each other (small Memory + Opinion drift)
- Outcome may generate gossip (information that propagates to other NPCs through their Concerns about the participants)
- Outcome is summarized as a one-line event log entry that the player may discover via investigation, gossip, or Knot-mediated counsel

**Example interaction selection:**
- Cardinal Klapp's Concern "Where is the Stillhelm Codex?" + Marshal Ehrenwall's backstory tag "stillhelm-survivor" → engine generates a private conversation; Klapp asks Ehrenwall what she remembers about the documents recovered after the battle. Ehrenwall's Mood and her Opinion of Klapp determine her response.

### 1.5 Integration Points

| Existing system | Integration |
|---|---|
| **Disposition track** (-3 to +5) | Unchanged. Represents player ↔ NPC relationship state. Affected by Opinion of player. |
| **Conviction Scars** | Unchanged. Triggers Mood: Distracted; generates Concerns; updates Opinions of those who advocated for the contradicting argument. |
| **Beliefs** | Unchanged. Resolved Concerns may produce new Beliefs (potentially incorrect). |
| **NPC Outreach (§8.11)** | Augmented. Concern-driven Outreach added. NPCs with active Concerns about the player generate Outreach scenes asking about the Concern's subject. |
| **Standing ladder** | Unchanged. Promotion events generate Memories and Opinion shifts in observing NPCs. |
| **Domain Actions** | Unchanged. Failed Domain Actions generate Concerns ("Why did this fail?"); successful Domain Actions advance the proposing NPC's relevant Project. |
| **Scene Slate** | Augmented. Concern-generated Outreach added at Priority 3. NPC-NPC interaction outcomes can spawn Priority 4 settlement events. |
| **Read/Appraise actions** | Augmented. Read reveals current Mood and one Concern. Appraise (Overwhelming) reveals one Opinion (with story content). |

### 1.6 Computational Budget

Per-Accounting compute estimate:
- 35 Active NPCs × 5 procedures × ~10ms each = ~1.75s per Accounting (acceptable)
- 70 off-screen interactions × ~50ms each = ~3.5s per Accounting (acceptable)
- 50 Passive NPCs × 2 lite procedures × ~5ms each = ~0.5s per Accounting (acceptable)
- Per-season total: ~6 seconds, well within Godot 4.6 frame budgets if spread across loading

Per-NPC storage estimate:
- Active NPC: ~3KB (state + 10 memories + 10 opinions + 3 concerns + 2 projects)
- Passive NPC: ~500 bytes
- Total state: ~150KB for full campaign roster (trivial for 2026 hardware)

---

## Part 2: Bidirectional Testing

Each test poses a specific scenario and traces what the proposal produces, identifying gaps where the dynamic fails or pattern-matches.

### Test 1: Vertical Down (Faction → Settlement → Personal)

**Scenario:** Crown signs military alliance with Varfell at Year 2, Season 8.

**Trace:**

*Faction level (Year 2 S8):* Treaty fires. Procedure B generates Concerns in Crown inner-circle NPCs:
- Confessor: "Who counseled this?" (high salience: contradicts his primary Conviction of Faith)
- Marshal Ehrenwall: "What military commitments did we make?" (medium salience: Project-relevant)
- Spymaster Kolbrun: "What do the Varfell envoys know about us?" (medium salience: Project-relevant — her Niflhel-broker Project is now complicated)

Procedure A updates Moods:
- Confessor: Anxious (Conviction-contradicting event)
- Cardinal Klapp: Confident (his Project gains political space)

*Settlement level (Year 2 S9):* Crown-controlled border settlement S-022 "Stenholm" hosts Varfell observer team per treaty. Stenholm has a Passive parish priest (Father Eyvind) and a Passive militia captain (Hilde).

- Eyvind's lite Concern: "Are these Varfell people heretics?" 
- Hilde's lite Concern: "Are they here to count our defenses?"

These minor NPCs generate observable behaviors: Eyvind preaches a cautious sermon about "discernment in difficult times" (heard by player if present in settlement). Hilde quietly increases watch rotations.

*Personal level (Year 2 S10):* Player as Crown Lieutenant in Stenholm encounters the Varfell observer team leader, a named Passive NPC (Lt. Estren of Varfell).

Estren has lite inner state: Conviction Reason, Concern "Are the Crown locals going to cooperate with our observation duties?", Opinion of Crown personnel ("formally polite, internally hostile").

The player's interaction with Estren is shaped by Estren's Concern and Opinion. Player choice (cooperative, neutral, obstructive) updates Estren's Opinion, which propagates back through reports.

**Diagnosis:** Vertical-down works. ✓

**But:** Issue identified — Eyvind and Hilde's Concerns don't currently feed back into the system. They generate atmospheric behavior but their state changes don't propagate. A Eyvind whose Concern resolves to "yes, heretics" produces nothing — there's no mechanism for a Passive NPC's Belief to become a faction-level signal.

### Test 2: Vertical Up (Personal → Settlement → Faction)

**Scenario:** Player wins Total Victory Contest against Cardinal Klapp on a scholarly question at Year 3 Season 5. Klapp acquires Conviction Scar.

**Trace:**

*Personal level:* Klapp's Belief "Honest scholarship is a path to understanding" becomes Scar. New Belief forms accommodating the loss. Procedure A: Mood → Distracted (1 season). Procedure B: Concern generated "Was I wrong about the path I've been on?"

Procedure D: Klapp's Opinion of the player updates. Memory created: "Lost a Contest to the player on a question I thought I understood." Affect: complicated — admiration for player's argument, grief at own error.

*Settlement level:* Klapp governs parish settlement S-008 "Verdmuld." His Distracted Mood reduces Project advancement (his scholarly Project pauses) and reduces governance attention.

**Issue identified:** No explicit mechanism converts "Distracted Mood" into "settlement Order decay." The narrative implies it; the mechanic doesn't specify.

**Required edit:** Mood states need explicit mechanical effects on governance. Distracted Mood: governor's seasonal governance action takes +1 Ob. Grieving Mood: governor's governance action may auto-fail if not pursued (Spirit check Ob 1 to maintain focus). 

*Faction level:* If Verdmuld's Order drops, Procedure B triggers a Concern in Confessor: "What is happening at Verdmuld?" Confessor investigates (sends an agent, asks Klapp directly, or in extreme case opens an internal review).

Klapp's response to Confessor's investigation depends on Klapp's current state. Distracted Klapp may be evasive (Confessor's investigation Concern intensifies). Grieving Klapp may confess his recent Scar to the Confessor (which could either deepen Confessor's protectiveness or trigger a Heresy Investigation depending on Confessor's current Mood and Opinion of Klapp).

**Diagnosis:** Vertical-up works once the Mood-to-governance link is specified. ✓ (with edit)

### Test 3: Lateral NPC ↔ NPC (No Player)

**Scenario:** Marshal Ehrenwall and Cardinal Klapp, both Crown inner circle, at Year 2 Season 12 (post-treaty, mid-campaign).

**Trace:**

Procedure E selection check at Accounting:
- Shared Concerns? Ehrenwall has "What military commitments did we make?" Klapp has "Are Reason-aligned scholars now politically tolerable?" — no obvious intersection.
- Intersecting Projects? Ehrenwall trains Torben. Klapp seeks Stillhelm Codex. No intersection.
- Recent Memory? They were both at the treaty signing. Both have Memory of that event. ✓
- RP-equivalent affect? Ehrenwall's Opinion of Klapp: "tolerable scholar, not a political threat" (affect_axis +1). Klapp's Opinion of Ehrenwall: "honorable but rigid; she would not understand what I'm doing" (affect_axis +1). Mutual sum +2. Not at threshold.

→ No interaction generated this season.

**Issue identified:** The interaction selection criteria are too restrictive. NPCs in the same inner circle should have *some* low-frequency interaction baseline even without strong triggers. Real courts have routine social contact — meals, council preliminaries, ceremonial appearances.

**Required edit:** Add a baseline "ambient contact" mechanism. Each season, for each pair of NPCs in the same inner circle, 30% chance of a low-stakes interaction that produces small Memory (+0.1 affect drift) without major political consequence. This represents the gradual accumulation of personal acquaintance. Strong trigger interactions still occur per existing criteria.

**Re-trace with edit:** Ehrenwall and Klapp have a 30% baseline. Suppose this season they roll a hit. The engine generates a small interaction: they speak briefly during a council recess. The interaction's content reflects their current states — Ehrenwall asks Klapp about scholarly reactions to the treaty (her Concern). Klapp gives a measured answer that reveals more than he intended (he's still Confident from the treaty's political implications). 

Memory created for both. Affect drift: Ehrenwall's Opinion of Klapp gains evidence "more thoughtful about politics than I gave him credit for" (affect_axis +0.2). Klapp's Opinion of Ehrenwall gains evidence "she's listening more carefully than I expected" (affect_axis +0.2).

Three more seasons of similar low-stakes contact and these two NPCs have shifted from Indifferent to Mildly Collegial — without player involvement, without any explicit faction event. ✓

**Issue identified (deeper):** Even with ambient contact, the resulting state isn't *visible* to the player. The player has no way to know Ehrenwall and Klapp have started cooperating informally unless they specifically investigate.

**Required edit:** Off-screen interactions with significant outcomes (affect drift > 0.5 cumulative) generate gossip — an information item that propagates through other NPCs. Other NPCs whose Concerns or Projects intersect with the gossiped pair receive the gossip and update their Opinions. The player can learn the gossip via Read action, NPC-initiated Outreach (if a gossiping NPC has high Disposition with player), or intelligence operations.

### Test 4: Diagonal Down (Faction → Personal via Settlement)

**Scenario:** Hafenmark passes constitutional amendment at Year 4 Season 3 restricting Crown taxation in Hafenmark territories. Player is Crown Lieutenant in S-016 "Niedmark," a Crown enclave inside Hafenmark territory.

**Trace:**

*Faction level:* Amendment fires. Procedure B generates Concerns:
- Crown leaders: "How do we respond?"
- Hafenmark leaders: "Will the Crown comply?"
- Niedmark's Crown governor (NPC, Standing 4): "What is my legal authority now?"

*Settlement level:* Niedmark contains Passive NPCs: a Crown-loyal merchant (Petra), a Hafenmark-loyal magistrate (Bjorn), a parish priest who is loyal to the Church but lives under Hafenmark legal jurisdiction (Father Magnus).

Each generates a lite Concern:
- Petra: "Will my Crown taxation status change?"
- Bjorn: "Should I begin enforcing the amendment immediately?"
- Magnus: "Whose authority do I recognize when these conflict?"

*Personal level:* Player encounters Bjorn, who is preparing to enforce the amendment. Scene slate generates Priority 2 entry: "Magistrate Bjorn requests a meeting about jurisdictional changes."

Player choice space:
- Cooperate with Bjorn (acknowledge Hafenmark jurisdiction)
- Refuse (assert Crown authority, possible incident)
- Negotiate (find compromise — Settlement-level agreement that doesn't trigger broader incident)
- Stall (delay decision; loss of momentum to Hafenmark)

Each choice has consequences:
- Cooperate: Petra's Opinion shifts negatively ("the Lieutenant betrayed us"). Crown leadership Opinion of player shifts negatively if they hear about it.
- Refuse: Bjorn's Opinion shifts ("hostile Crown agent"). Hafenmark leadership generates Concern "Is the Crown going to comply with the amendment?"
- Negotiate: depends on player's Cha and prior Disposition with Bjorn; success creates Memory for both ("we found a way through") and softens Hafenmark's Concern.

**Diagnosis:** Vertical-down works. ✓

**But:** Issue identified — the player's choice and outcome need to *propagate up*. Currently the Memory in Bjorn (a Passive NPC) doesn't have a clear path to faction-level Hafenmark NPCs.

**Required edit:** Passive NPCs aggregate their Memories into a "settlement signal" at Accounting. Passive NPCs in a settlement with strongly negative Memories about the player generate a settlement-level Concern that propagates to the controlling faction's relevant inner-circle NPC. Strongly positive Memories produce vouching gossip. This gives Passive NPCs a propagation path without requiring full Active state.

### Test 5: Diagonal Up (Personal → Faction via Settlement)

**Scenario:** Player builds Disposition +5 with Father Magnus (parish priest, Passive) over Year 1-2. Magnus has been hearing confessions and possesses information about a Hafenmark intelligence operative working in Niedmark.

**Trace:**

*Personal level:* Player has Disposition +5 with Magnus. Knot formation possible if either has TS 30+ (Magnus typically does not). Without Knot, Magnus is at maximum non-Knot trust.

At Disposition +5, Magnus shares Buried information per the Disposition Information Gates table. He tells the player about the Hafenmark operative.

**Issue identified:** The current design lets Magnus share information at Disposition +5, but doesn't model *what Magnus knows* explicitly. There's no system tracking which NPCs possess which information about which other NPCs/factions.

**Required edit:** Add to NPC inner state a **Knowledge** structure for Active NPCs and Passive NPCs in information-rich roles (priests, innkeepers, merchants who travel, scribes):

```
Knowledge:
    fact: text or structured tag (e.g., "hafenmark-operative-in-niedmark")
    source: ref to how this NPC learned it (memory, conversation, observation)
    salience: 1-5 (decays slowly)
    sensitivity: 1-5 (how guarded the NPC is about sharing it)
```

NPCs share Knowledge based on Disposition level and sensitivity:
- Settled (Disposition +1): facts at sensitivity 1
- Hidden (+2): sensitivity 2
- Buried (+3): sensitivity 3
- Liminal (+4): sensitivity 4
- Bonded (+5): sensitivity 5

This formalizes information topology. The player's social investment with Magnus becomes politically valuable not abstractly but specifically — Magnus knows things the player needs.

*Settlement level:* Player acts on Magnus's information. Investigation reveals the Hafenmark operative's identity. The player can: report to Crown court (faction value), confront privately (settlement-level resolution), or use as leverage.

*Faction level:* If reported to Crown court, the player's Renown gains. The Spymaster Kolbrun's Opinion of the player updates ("operationally competent — has assets I don't"). Kolbrun's Concern about the Niflhel-successor brokers gains a tangential lead. Crown's Intel stat may improve if the operative is captured.

**Diagnosis:** Vertical-up works with Knowledge structure addition. ✓ (with edit)

### Test 6: Lateral Faction-to-Faction (NPC ↔ NPC across factions)

**Scenario:** Crown court hosts Hafenmark diplomatic mission at Year 5 Season 2. Marshal Ehrenwall (Crown) meets her counterpart, Hafenmark's military advisor Eluf Magnusson, for joint defense planning.

Both are aging soldiers. Both are dealing with succession concerns about their respective leaders. Both are pragmatists with low institutional_deference.

**Trace:**

Procedure E doesn't naturally fire cross-faction interactions (it operates within inner circles). The diplomatic event is the trigger.

The meeting itself is engine-generated content:
- Ehrenwall's Concerns and Project shape what she asks
- Magnusson's Concerns and Project shape what he says
- Both have personality similarities (low institutional_deference, pragmatist)

Outcome:
- They recognize each other as similar. Memory created for both, affect positive ("met a real soldier across the table").
- Each forms an Opinion of the other: Ehrenwall's Opinion of Magnusson "competent, not a fool, possibly someone I could work with." Magnusson's Opinion of Ehrenwall similar.

**Issue identified:** Cross-faction NPC relationships have no procedural support outside one-shot events. After the diplomatic mission, Ehrenwall and Magnusson don't have ongoing contact. Their mutual Opinions stagnate.

**Required edit:** Cross-faction NPCs who have established Memory (any prior interaction) and active mutual Opinion (affect_axis ≥ +1 or ≤ −1) qualify for a separate **Distant Contact** off-screen interaction track. 

Distant Contact runs at much lower frequency (10% per season versus 30% for inner-circle ambient) and represents private correspondence, indirect contact through intermediaries, or crossed paths during travels. It produces small Memory updates and slow Opinion drift.

This lets cross-faction relationships develop or atrophy over the campaign without requiring direct meetings.

**Re-trace:** Over Years 5-7, Ehrenwall and Magnusson exchange occasional letters. Each exchange produces small affect updates. By Year 7, their mutual Opinions have grown: "trusted counterpart across the border."

This becomes politically significant when, at Year 8, the Crown and Hafenmark face a shared external threat (Altonian invasion). Ehrenwall's Opinion of Magnusson means she trusts his intelligence; her advice to Almud reflects this trust. Cross-faction cooperation becomes possible *because of* the personal relationship developed laterally.

**Diagnosis:** Lateral cross-faction works with Distant Contact addition. ✓ (with edit)

### Test 7: Emergence — Multiple Stressors Simultaneously

**Scenario:** Year 6, Season 4. The Crown court is processing:
1. Almud's Generational Shift (highest attribute reduced)
2. A Hafenmark constitutional amendment passed last season  
3. The player has been observed twice in private conversation with Vaynard
4. Cardinal Klapp's Stillhelm Codex Project is approaching completion

**Trace:**

Each NPC is processing all four stressors simultaneously through their inner state.

**Confessor (Year 6 S4):**
- Mood: Anxious (treaty + amendment)
- Active Concerns: "Why did Almud agree to the treaty?" (salience 4, ongoing); "What is the player doing with Vaynard?" (salience 5, new); "Is the amendment a Hafenmark theological challenge?" (salience 3, new)
- Projects: institutional Project — defend Church doctrine. Now strained by multiple fronts.
- Opinions: Almud "diminished, possibly being manipulated"; Player "deeply suspicious — I was wrong about them"; Klapp "scholarly, currently distracted by his own work" (Confessor doesn't know about the Codex Project specifically).

The Confessor's behavior this season prioritizes addressing his strongest Concern: the player. He generates an Outreach scene — but its tone is shaped by his Anxious Mood. The Outreach is not a friendly inquiry; it's a Demand-adjacent confrontation.

**Marshal Ehrenwall (Year 6 S4):**
- Mood: Steady (none of the events directly threatens her domain or Project)
- Active Concerns: "How is Torben handling the political pressure?" (Project-relevant)
- Projects: train Torben. Progressing but Torben needs new lessons (the player-Vaynard situation is teachable material — princes need to learn how to read divided courts)
- Opinions: Player "promising but their judgment in cross-faction matters is suspect"; Almud "fading — I need to accelerate Torben's preparation"

Ehrenwall generates no Outreach this season. She continues her Project. Her quiet absence from court drama is itself a political signal — observers wonder where she is.

**Cardinal Klapp (Year 6 S4):**
- Mood: Vindicated (Project nearing completion)
- Active Concerns: "What will Himlensendt do when he sees the Codex evidence?"
- Projects: Stillhelm Codex (progress 9/10, one season to completion)
- Opinions: Player "potential ally in scholarly matters but they're being reckless with Vaynard contacts"; Confessor "still my mentor; I owe him a careful confrontation, not a public defeat"

Klapp's Project completion is imminent. His Mood drives him toward action. He may generate an Outreach scene to the player — to seek the player's support for the upcoming confrontation with Himlensendt.

**Player (Year 6 S4):** receives multiple competing Outreach scenes:
- Confessor (confrontational, demanding explanation about Vaynard)
- Klapp (alliance-seeking, requesting support for scholarly confrontation)
- Possibly Almud (concerned about court fragmentation)
- Possibly Ehrenwall (absent — but if player visits her, she'll discuss Torben)

The player's choices ripple: attending Confessor's Outreach without attending Klapp's may cost Klapp's alliance offer (Klapp's Opinion updates: "the player isn't ready to commit to this fight"). Attending Klapp's first may further inflame Confessor's Concerns about player loyalty.

**Emergence achieved.** The political environment is producing:
- Competing demands on the player from NPCs with different Projects
- NPCs whose internal states constrain each other (Klapp's Project completion contains an implicit confrontation with Confessor; the player's choice of which to support is a real political act)
- Outcomes that depend on the order and combination of player choices, not on a single threshold
- NPC behaviors that are legible (the player can understand why each NPC is doing what they're doing) but not predetermined

**Issue identified (procedural ordering):** When Klapp's Project completes, what fires first — the Project completion_effect (Klapp confronts Himlensendt publicly), or the Confessor's reaction Concern (Confessor responds to confrontation)? The order matters because Confessor's response shapes the confrontation scene's setup.

**Required edit:** Specify procedure ordering at Accounting:
1. Procedure A (Mood updates from prior season's events)
2. Procedure C (Project advancement and completions; completion_effects fire here as Domain-Action-equivalent events)
3. Procedure B (Concern generation from this season's events; resolution checks)
4. Procedure D (Opinion drift)
5. Procedure E (Off-screen interactions, including reactions to this season's events)
6. Scene Slate generation for next season

This ordering means: Klapp's Project completes (Step 2). The completion fires a public scholarly challenge to Himlensendt. Confessor's Concern ("how do I respond to this?") generates in Step 3. Confessor's response is queued for next season's Outreach generation. The player has one season's lead time to react before Confessor's countermeasure fires.

**Issue identified (player overload):** With 4+ Outreach scenes per season at intense moments, players may face decision paralysis. Existing Scene Slate budget (3-5 actions) constrains how many they can attend.

**Required edit:** When multiple Active NPCs generate competing Outreach scenes in the same season, the engine evaluates which are *displaced* by player non-attendance. NPCs whose Outreach is ignored update their Opinions of the player based on personality:
- Patient personality (high institutional_deference, low risk_tolerance): "they're busy; I'll try again." Small Opinion negative drift.
- Impatient personality (low institutional_deference, high risk_tolerance): "they're avoiding me." Larger Opinion negative drift; may generate a Concern about the player's loyalties.

This means missing Outreach scenes is a real political cost, but the magnitude depends on who was missed. The player can't attend everyone, and choosing whom to skip is itself a political act. ✓

### Test 8: Player Absence (Long Expedition)

**Scenario:** Player departs for Southernmost expedition at Year 7 Season 1. Returns Year 8 Season 1. Four seasons absent.

**Trace:**

During absence, all procedures continue running for all NPCs. The political environment evolves without the player:
- Mood updates
- Concerns generated and resolved (some incorrectly, producing wrong Beliefs)
- Projects advance (some complete, some fail)
- Opinions drift based on accumulated Memories
- Off-screen interactions produce gossip and relationship development

When the player returns, they encounter:
- NPCs whose Moods have shifted
- NPCs whose Projects have advanced or completed (changing the political landscape)
- NPCs whose Opinions of the player have drifted (mostly toward neutral or negative — absence is rarely positive)
- Gossip the player can investigate

**Issue identified (information asymmetry):** The player returns and Read actions on familiar NPCs may reveal entirely changed inner states. Without explicit handling, the player faces a sudden information cliff.

**Required edit:** Returning player's first Read action on each previously-known NPC is at +0 Ob (free re-acquaintance). Subsequent Reads at standard Ob. NPCs the player has Disposition +3 with at departure offer a "catch up" Outreach in their first interaction — they tell the player what they've been doing and what's changed.

**Issue identified (NPC-NPC relationships during absence):** Without the player as catalyst, NPC-NPC relationships continue developing. The player may return to find:
- Two NPCs who were Indifferent are now Collegial (formed a Bloc against a third NPC)
- An NPC who was the player's ally has gained a new Project that conflicts with the player's interests
- An NPC has acquired a new Knowledge item about the player's past actions that they're now sharing

This is correct behavior, but requires explicit reporting to the player on return. **Required edit:** "Where Were You" expansion (player_agency §4.4): on return from absence ≥ 3 seasons, the player receives a structured catch-up briefing with NPC-state highlights. Critical changes (faction-leader arc transitions, Project completions, succession events) are summarized; minor drift is presented as gossip the player can pursue.

**Diagnosis:** Player absence works with information-cliff handling. ✓ (with edit)

---

## Part 3: Issues Compiled and Edits

### Issues identified across tests:

1. **Passive NPC state propagation (Test 1):** Lite-state NPCs generate Concerns but their resolutions don't propagate.
2. **Mood → governance link (Test 2):** No explicit mechanical effect of NPC Mood on Domain Action / governance performance.
3. **Inner-circle ambient contact (Test 3):** Off-screen interaction selection is too restrictive; courts have routine social contact baseline.
4. **Off-screen outcomes invisible (Test 3 follow-up):** Significant NPC-NPC relationship changes produce no player-discoverable signals.
5. **Information topology (Test 5):** No structured tracking of which NPCs know which facts.
6. **Cross-faction relationship continuity (Test 6):** No procedural support for ongoing cross-faction NPC relationships.
7. **Procedure ordering (Test 7):** Five procedures with implicit ordering; explicit sequence needed.
8. **Player Outreach overload (Test 7):** Multiple competing Outreach scenes need cost specification for missed attendance.
9. **Information cliff on return (Test 8):** Absence-induced information loss needs handling.
10. **NPC-NPC absence dynamics (Test 8):** "Where Were You" briefing must cover NPC-state evolution.

### Edited proposal — additions to §1.4 Procedures and §1.3 Data Structures:

**Edit A — Settlement Signal aggregation (resolves Issue 1):**

At Accounting, each settlement aggregates its Passive NPCs' Memories into a Settlement Signal. The Signal is a structured summary: "predominant local sentiment toward player: positive/neutral/negative; top 2 local concerns; relationship state with controlling faction." Settlement Signals propagate to controlling faction's relevant Active NPCs (governor's superior, faction leader if Standing 4+ governance, faction's Intel-handler) as input to their Concerns.

**Edit B — Mood mechanical effects on governance/Domain Actions (resolves Issue 2):**

| Mood | Effect on actions taken by this NPC |
|---|---|
| Steady | No modifier |
| Anxious | +1 Ob to social and political actions; -1 Ob to defensive/security actions |
| Confident | -1 Ob to action this NPC initiates; +1 Ob if action requires caution |
| Grieving | Major actions auto-fail without Spirit check Ob 1; minor actions at standard Ob |
| Vindicated | -1 Ob to action aligned with the vindicating event's themes |
| Humiliated | +2 Ob to public actions (this NPC avoids visibility); -1 Ob to private actions (retaliation, plotting) |
| Distracted | +1 Ob to all actions; Project advancement halts |
| Resolved | -1 Ob to action consistent with the resolution; +1 Ob to actions inconsistent |

**Edit C — Inner-circle ambient contact (resolves Issue 3):**

Procedure E expanded: each season, for each pair of Active NPCs in the same inner circle, 30% chance of ambient interaction (small affect drift, small Memory). This runs in addition to triggered interactions.

**Edit D — Gossip propagation (resolves Issue 4):**

Off-screen interactions with cumulative affect drift > 0.5 generate a Gossip Item. Gossip Items are stored at the inner-circle level and propagate through NPCs whose Concerns or Opinions involve the participants. The player can discover Gossip via: Read action on a knowing NPC (Ob 2), NPC-initiated Outreach (free if knowing NPC has Disposition +3 with player), Surveillance fieldwork action.

**Edit E — Knowledge structure (resolves Issue 5):**

Add to Active NPC and information-rich Passive NPC inner state:
```
Knowledge[]:
    fact: structured tag or text
    source: how the NPC learned it
    salience: 1-5
    sensitivity: 1-5 (controls Disposition gate for sharing)
```
Knowledge updates from event observations and gossip propagation. Sharing follows Disposition Information Gates table.

**Edit F — Distant Contact track (resolves Issue 6):**

Procedure E expanded: cross-faction NPCs with prior Memory and active mutual Opinion (≥|1|) qualify for Distant Contact track at 10% per season. Produces small Memory updates and Opinion drift representing private correspondence or indirect contact.

**Edit G — Procedure ordering (resolves Issue 7):**

Accounting sequence specified:
1. Procedure A (Mood updates from prior season's events)
2. Procedure C (Project advancement and completions; completion_effects fire as Domain-Action-equivalents)
3. Procedure B (Concern generation from this season's events; resolution checks)
4. Procedure D (Opinion drift)
5. Procedure E (Off-screen interactions, including ambient + triggered + Distant Contact)
6. Settlement Signal aggregation
7. Gossip propagation
8. Scene Slate generation for next season

**Edit H — Outreach displacement cost (resolves Issue 8):**

When multiple Active NPCs generate Outreach in the same season exceeding the player's scene action budget, ignored NPCs update their Opinions of the player based on personality. Patient personalities: small negative drift. Impatient personalities: larger drift, may generate a Concern about the player's loyalties.

**Edit I — Returning player handling (resolves Issues 9 & 10):**

Player absence ≥ 3 seasons triggers: (1) free first Read action on each previously-known NPC at return; (2) "Where Were You" structured catch-up briefing covering critical changes (arc transitions, Project completions, succession events) plus 3-5 gossip items the player can pursue; (3) NPCs at Disposition +3 with player at departure offer a catch-up Outreach in their first interaction.

---

## Part 4: Diagnostic Summary

### What the proposal achieves

- NPCs operate autonomously: Concerns generated, Projects advanced, Opinions drifted, off-screen interactions produced — all without player involvement.
- Multi-directional dynamics: vertical down/up, lateral within and across factions, diagonal cross-scale, all functional with edits applied.
- Emergence: combinations of Mood + Concerns + Projects + Opinions produce outcomes not specified by any individual proposal.
- Computational tractability: ~6 second compute per Accounting, ~150KB total state — well within Godot 4.6 budget.
- Player experience: NPCs feel like persons because their behavior is shaped by their inner states, not by reaction to player actions.

### Where the proposal still requires further specification

1. **Personality dimension calibration:** The four personality dimensions (risk_tolerance, social_warmth, intellectual_rigor, institutional_deference) need per-NPC value assignment for each Active NPC. ~35 NPCs × 4 values = 140 values to set during character creation phase.

2. **Concern seed templates:** Engine needs a library of Concern templates that generate from each event type. Treaties, Conviction Scars, observed cross-faction contacts, Project blockers — each event type maps to a Concern template per Conviction. This is content authorship, not engine work.

3. **Project library:** Each Active NPC needs ≥1 starting Project at character creation. ~35 Projects to author.

4. **Opinion seeding:** At campaign start, each Active NPC needs Opinions of the other politically-relevant Active NPCs. ~35 × ~10 = ~350 starting Opinions to author. (Many can be terse: "respectful, distant" with no story until events generate one.)

5. **Knowledge seeding:** Each information-rich NPC needs starting Knowledge items. Variable count, probably ~5-10 per relevant NPC.

6. **Gossip propagation rules:** The specifics of which Concerns trigger which Gossip propagation, and how fast information spreads through the NPC network, need calibration via simulation.

These are content-authoring tasks, not engine tasks. The architecture supports them; the work is filling in the specific instances.
