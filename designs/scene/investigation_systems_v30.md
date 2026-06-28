# VALORIA — Investigation Systems Proposal
## Systems: NPE · Investigation Interface · Dialogue Lattice · Response Matrix
## Status: CANONICAL — approved 2026-04-17 (editorial batch acceptance)
## Date: 2026-04-15-21-07
## Affects: S10 NPC Behavior, S14 Fieldwork, S12 Social Contests, S16 Emergent Arcs, S17 Scale Transitions, S03 Geography, S18 Characters
## Canon compliance: P-01 (co-movement), P-03 (consciousness-performed rendering — player's perceptual horizon defines available scenes), P-15 (three-layer being-persistence — Certainty is personal, Conviction is cultural-ethical, Thread substrate is metaphysical)

---

## ARCHITECTURE

Four interlocking systems sharing one data substrate:

```
TERRITORY ECOLOGY
      │
      ▼
[1] NPC POPULATION ENGINE ──────────────────────────┐
      │ generates actors for                         │ NPC Genome
      ▼                                              │ persists and
[2] INVESTIGATION INTERFACE (spatial scene graph)   │ shifts between
      │ places player in proximity                   │ scenes
      ▼                                              │
[3] DIALOGUE LATTICE ◄── Ontological Ledger         │
      │ player utterances gated by character state   │
      ▼                                              │
[4] RESPONSE RESOLUTION MATRIX ◄────────────────────┘
      │ NPC response gated by NPC Genome
      ▼
 OUTCOMES → modify both Ledger and Genome
      │
      ▼
 Evidence Track · Disposition · Conviction Wounds · Arc Vectors
```

**Shared substrate: the Ontological Ledger.** Both the Dialogue Lattice (what the player can say) and the Response Matrix (what the NPC can respond) read from a common record. The Ledger is not a new system — it is the player's existing character state made explicit as an input:

| Ledger Field | Source | Range |
|---|---|---|
| Certainty | Character creation + shifts | 0–5 |
| Thread Sensitivity | Encounter/exposure | 0–100 |
| Beliefs | Player-authored (§2 of Agency proposal) | 3 active |
| Evidence | Fieldwork Evidence Track, per investigation | Tagged discoveries |
| Histories | Character creation, cap = Recall | Named tags |
| Disposition | Per NPC, from Fieldwork/Socializing | −5 to +5 (ED-912 — flat; was −4 to floor(Bonds/2)+1) |
| Conviction Wounds | Per NPC, from contest outcomes | 0 / 1 / 2+ |
| Standing | Per faction, from Duty completion | 0–5 |

Nothing in this table is new. The proposal makes explicit that these values are the direct inputs to conversation resolution.

---

## SYSTEM 1: NPC POPULATION ENGINE (NPE)

### What exists / what's missing

S10 NPC Behavior specifies 13 named NPCs with full conviction, pressure point, ethical framework, and priority stacks. It does not specify how scenes are populated with unnamed / minor NPCs, nor does it give territories distinct social texture beyond faction control. The holistic audit flags this: "stance triangles for Lenneth, Elske, Haelgrund" (Priority 3) are the named-NPC version of a broader gap — territories feel underpopulated because only named actors have behavioral specs.

### Territory Social Ecology

Each territory has a **social ecology** — a weighted distribution of worldview and affiliation tendencies derived from its existing tracked stats:

| Territory Stat | Ecology Effect |
|---|---|
| Piety 4–5 | +2 weight to Church-aligned worldviews; Certainty 4–5 most common |
| Piety 0–1 | +2 weight to Thread-aware or RM-sympathetic worldviews; Certainty 1–2 possible |
| Accord 0–1 | +2 weight to resentment/survival-first worldviews; Volatility +1 to all generated NPCs |
| Accord 4–5 | +1 weight to institutional-trust worldviews; Volatility −1 to all generated NPCs |
| Prosperity 4–5 | +2 weight to trade/guild affiliations; Compromise Profile biases toward economic exchange |
| Prosperity 0–1 | +1 weight to desperation/extraction worldviews; Compromise Profile biases toward survival needs |
| Faction Control | Controlling faction's ethical framework is the default for 60% of generated NPCs |

Ecology weights are not binary — they shift the probability distribution, not the outcome. A high-Piety territory still generates some heterodox NPCs. The deviation roll (below) handles that.

### NPC Genome Record

Every generated NPC (named or procedural) has five axes:

**1. Stance** — Position on active political/metaphysical issues. Each active issue (Thread reality, Church authority, Altonian threat, RM legitimacy, Varfell autonomy) gets a 1–5 rating:
- 1 = strongly opposed / in denial
- 3 = neutral / unformed
- 5 = strongly committed / aware

**2. Worldview** — 1–2 core convictions drawn from the existing conviction taxonomy (Faith, Order, Reason, Justice, Survival, Loyalty, Truth, Power). These are the NPC's load-bearing beliefs. Worldview is what the NPC will defend in argument.

**3. Affiliation** — Faction membership (0–3 loyalty weight) plus any hidden allegiance (separate field, not player-visible at generation). Loyalty weight determines how faction pressures modulate their behavior.

**4. Compromise Profile** — What the NPC will exchange, under what conditions, to whom:
- Economic (gold, goods, trade access)
- Informational (secrets, documents, names)
- Political (votes, endorsements, silence)
- Personal (protection, safe passage, emotional support)
- Nothing (principled refusal — NPCs with high Conviction Wound resistance and Loyalty weight 3)

**5. Volatility** — How much the NPC shifts under pressure (1–5):
- 1 = immovable; will not change stance regardless of evidence or social pressure
- 3 = moves with sustained, credible engagement
- 5 = highly susceptible; shifts on a single strong interaction

### Two-Tier Generation

**Tier 1 — Archetype seed:** Scene specification declares density and composition (e.g., "3 NPCs: 1 authority-aligned, 1 neutral, 1 affiliation unknown"). The ecology weights for the territory are sampled to fill each slot. This produces an NPC whose axes reflect local norms.

**Tier 2 — Deviation roll:** Each NPC receives a d6 deviation score at generation. On 5–6: one axis is rolled against the opposite extreme of the ecology's distribution. This produces the outlier — the orthodox believer in the Thread-aware territory, the secret RM sympathizer in the Church stronghold. Deviation ≥ 5 also makes the NPC eligible to become an arc vector (see Integration below).

### Persistence

Generated NPCs persist across scenes in the same territory. They:
- Remember interactions with the player (Disposition changes carry forward)
- Talk to each other: at season end, NPCs with shared worldview and adjacent Stance positions make a Volatility check. On pass: both shift toward each other's Stance by 1. This simulates off-screen social pressure without GM intervention.
- Can die, leave, or be arrested through NPC AI and arc outcomes (treated as named NPCs for arc purposes once they've had a player interaction)

### Named NPC Stance Triangles

[EDITORIAL: requires user approval — the specific stance positions for Lenneth, Elske, and Haelgrund on each active issue must be authored, not generated. The Genome structure provides the format; the content is editorial. Propose this as a separate deliverable once this system is approved.]

### Integration

| Paired System | Integration |
|---|---|
| S03 Geography | Territory stats → ecology weights. No new data fields needed. |
| S10 NPC Behavior | Generated NPCs use a simplified 2-step decision procedure (Conviction Filter → Compromise Check) instead of the full 7-level priority stack. Named NPCs retain full stacks. |
| S16 Emergent Arcs | NPCs with deviation ≥ 5 are flagged as latent arc vectors. If the player interacts with them and produces a Conviction Wound or Disposition change, the arc system evaluates whether an arc fires. |
| S04 Clocks | Season-end Piety drift (existing mechanic) updates ecology weights for the following season. As territories shift Piety/Accord, their NPC populations gradually shift. |
| Player Agency §4 Scene Slate | Priority 4 (territorial opportunities) and Priority 5 (ambient events) in the Scene Slate are now populated by NPE-generated NPCs, giving those priority levels specific actors with Genomes. |

---

## SYSTEM 2: INVESTIGATION INTERFACE

### What exists / what's missing

Fieldwork (S14) specifies six investigation actions with attribute pools and Evidence Track thresholds (Simple 3, Complex 5, Structural 8). The RSE critique rates Fieldwork Smooth as ◐ specifically because there is no resource depletion and because the transition to the faction layer lacks integration (ED-547). Scale Transitions (S17) are the weakest system (○/○/◐) because only 5 Zoom In triggers exist for 120+ arcs (ED-545, P1).

The Investigation Interface addresses both: it provides the spatial architecture for investigation scenes (solving the Zoom In trigger gap) and frames the scene action budget as the natural depletion mechanic for Fieldwork.

### Scene-as-Graph

Each investigation scene is a **spatial graph** of 5–9 nodes. The graph represents the scene's meaningful locations — not an abstraction, a navigable space.

**Node types:**

| Type | Description | Default Access |
|---|---|---|
| **Anchor** | Fixed NPC — always present, always willing to receive approach | Open |
| **Evidence** | Discoverable object, document, or physical state | Open (but yields nothing without correct Fieldwork action) |
| **Drift** | NPC or object that moves between nodes on a time cycle | Present at certain times only |
| **Access** | Location or NPC gated by prior condition | Locked until condition met |
| **Observation** | Surveil point — player can watch without interacting | Open; grants Surveil action |

**Graph size scales with investigation complexity:**
- Simple investigation (threshold 3): 4–5 nodes
- Complex investigation (threshold 5): 6–7 nodes
- Structural investigation (threshold 8): 8–9 nodes

### Traversal Economy

Moving between nodes costs **time** (not a new resource — it is the scene action budget expressed spatially). The player has their scene action budget per season. Within a scene, they have a **scene time budget** (3 standard, adjustable by Stamina and Wounds per the Agency proposal). Each node interaction costs 1 time unit. Moving across the graph (more than 2 nodes apart) costs 1 additional time unit.

Some transitions also cost **Exposure**: moving through a guarded Access node, entering a Church-controlled space while Heresy Investigation is active, or attempting Surveil in a node with an Anchor NPC present. Exposure integrates with the existing Church Attention Pool.

### The Case Board

Evidence discovered in nodes appears on a **visual Case Board** — a map of connected facts. This is the player-facing representation of the Evidence Track.

- Each discovered piece adds a node to the Case Board
- Connections between nodes are drawn when the player Reconstructs (existing Fieldwork action)
- Simple threshold (3): the board has enough nodes to form a theory — the player can act on it but cannot prove it
- Complex threshold (5): the board has enough to present to an NPC as leverage (Corroboration in contest) or to the faction as intelligence
- Structural threshold (8): the board constitutes proof — usable as Casus Belli, Heresy evidence, or arc-triggering revelation

The Case Board is persistent across seasons (existing rule: Evidence Track carries forward). The visual representation makes the accumulation of evidence tangible, not abstract.

### Case Board Thread Layer (ED-680)

When a PC with TS ≥ 30 opens the Case Board, a toggle enables the **Thread Layer**:

**Thread Layer ON:** Each evidence node shows dual-depth information:
- **Rendered level** (always visible): physical evidence, testimony, documents
- **Substrate level** (TS ≥ 30): thread-configuration data from Thread-Read operations

Evidence from Thread-Read and evidence from mundane investigation that describe the same event are **linked**. The link is the constitutive insight: the physical trace and the substrate disruption are the same event at different depths.

**Insight bonus:** When a player connects rendered evidence to substrate evidence for the same event, Evidence Track advances +1 (max 1 insight bonus per investigation).

**Below TS 30:** Substrate evidence appears as "something is wrong here" — no linkage, no insight bonus.

### Temporal Dimension

Drift NPCs create a temporal puzzle: the player must be at the right node at the right time. Time-of-day matters for:
- Which Anchor NPCs are present (a merchant is at their stall, not at home)
- Whether Drift NPCs are accessible (a Church official moves between the archive and the chapel)
- Whether certain Evidence nodes are exposed (a document is only unattended when the clerk is at prayer)

This is Lacuna-style spatial attention — the player watches the scene, learns its rhythms, and intervenes at the moment of opportunity. It does not require new mechanics: it is the existing Surveil action given spatial expression.

### Zoom In Triggers

The Investigation Interface IS the Zoom In system (per the Agency proposal's §7.4 resolution of ED-545). When the Scene Slate generates a scene opportunity, the game places the player at the entry node of the corresponding scene graph. The 20–30 Zoom In triggers required are the 20–30 scene graph templates that the Scene Slate can instantiate.

**Proposed trigger categories (covering the minimum 20–30):**

| Category | Count | Examples |
|---|---|---|
| NPC arc moments | 8 | Conviction wound moment for each named NPC (Lenneth, Elske, Haelgrund, Himlensendt, Almud, Baralta, Vaynard, Maret) |
| Territory state thresholds | 6 | Accord 0 (Revolt), Accord 4 (Celebration/Stability event), Piety 0, Piety 4, Prosperity 0, Prosperity 4 |
| Clock milestones | 6 | MS band transitions (80/60/40/20), CI milestones (40/55/65/80) |
| Discovery events | 6 | Thread Wound formation, Gap sighting, Warden contact, Church evidence of Thread activity, Varfell Thread lab, Haelgrund TS revelation |
| Player Belief intersection | Variable | Generated when a Belief-tagged NPC or location appears in Scene Slate |

[EDITORIAL: requires user approval — specific scene graph content for each trigger category. This is worldbuilding and narrative. Only the trigger taxonomy and count are mechanical decisions.]

### Integration

| Paired System | Integration |
|---|---|
| S14 Fieldwork | Each node interaction = one Fieldwork action (Examine, Interview, Research, Surveil, Thread-Read, Reconstruct). No new action vocabulary. |
| S17 Scale Transitions | Scene graph = the Zoom In destination. Solves ED-545 structurally. |
| Player Agency §6 Scene Action Budget | Scene time budget within a scene mirrors the season-level scene action budget. Player is always triaging — which nodes to visit, which to skip. |
| S05 Calamity | Territories in the Calamity radiation zone have Thread-Read as accessible Observation action at any node. Thread phenomena are ambient — the player doesn't have to seek them. |
| NPE (System 1) | Named and generated NPCs populate Anchor and Drift nodes. Their Genomes determine what they yield to each Fieldwork action. |

---

## SYSTEM 3: DIALOGUE LATTICE

### What exists / what's missing

The existing social architecture has two modes: the Fieldwork Interview action (roll Charisma pool, advance Evidence Track) and the Social Contest (formal adversarial exchange with full genre/orientation/style decision tree). The RSE critique identifies the Contest as experientially complex (30+ seconds per exchange decision). The Fieldwork Interview is mechanically thin (one roll, no decision tree).

There is no intermediate system for investigative dialogue — the kind of conversation where the player is learning, probing, and building toward confrontation rather than executing it. Disco Elysium's core insight is that this intermediate space is where character expression lives. The Dialogue Lattice fills it.

**Design principle:** The Dialogue Lattice handles exploratory dialogue. Social Contests handle adversarial resolution. A conversation that starts as exploration escalates to a Contest when the player commits to a position the NPC actively resists. The transition is clean: the Lattice identifies the confrontation point; the Contest resolves it.

### Gate Types

Each utterance in the Lattice has zero or more gates — conditions that must be met for the utterance to be available. Seven gate types:

**1. Attribute Gate** — minimum attribute score required
- Triggers intellectual approaches ("The inconsistency in your testimony suggests…" requires Cognition ≥ 3)
- Triggers emotional approaches ("I can see this is costing you something" requires Attunement ≥ 4)
- Triggers physical presence ("I've been where you're describing" requires a relevant History tag)

**2. Evidence Gate** — specific discovery required
- Tagged by investigation ID: [Evidence: Church-Thread-Lab], [Evidence: Haelgrund-TS-12]
- Enables confrontation ("I know about the experiments in Gransol")
- Enables corroboration ("The documents confirm what you're telling me")
- Enables accusation ("Your name is in the Inquisitor's report")

**3. Belief Gate** — active Belief must match the NPC or topic
- Not a hard gate — a soft gate that unlocks an additional layer of investment
- "I've been watching this for weeks" is available if any active Belief references this NPC
- Produces a different Disposition response when used: the NPC reads genuine investment, not mere inquiry
- Integrates with Sincerity Gate: Belief-gated utterances pass the Sincerity check automatically (the investment is genuine)

**4. Certainty Gate** — player's Certainty must fall within a range
- Certainty ≥ 4: orthodox utterances available ("As the Church teaches…", "The Solmundian texts confirm…")
- Certainty ≤ 2: Thread-referencing utterances available ("The threads here are damaged", "I can feel what happened in this place")
- Certainty 3: the middle ground — neither set of utterances is fully available; the character is epistemically in transition
- **This is the ontological status gate.** A character who has seen the Thread cannot honestly speak pure orthodoxy. A character who hasn't cannot honestly claim Thread knowledge. The game enforces this.

**5. History Gate** — requires named History background
- [History: Warden]: "Edeyja taught me to read these signatures"
- [History: Church-Scholar]: "The Ecclesiastical Archives have records from before the Catastrophe"
- [History: Merchant-Guild]: "I know which ledgers aren't shown to inspectors"

**6. Disposition Gate** — relationship depth threshold
- Disposition ≥ +2: trust-signaling utterances available ("I'm telling you this because I trust you")
- Disposition ≤ −2: only confrontational or distant utterances available
- At maximum Disposition (Knot): one unique utterance available per NPC — something only someone who truly knows them could say

**7. Thread Sensitivity Gate** — TS threshold
- TS ≥ 30 (Leap capable): Thread-direct utterances available ("I can feel what you've done to this place", "The thread here has been pulled")
- TS 1–29 (aware but not capable): perceptual observations available ("Something feels wrong here", "The air is different")
- TS 0 (unaware): no Thread-referencing utterances available regardless of Certainty

### Visibility Rules

Gates fall into two visibility categories:

**Visible-locked:** The utterance is shown but greyed. A brief hint indicates the condition:
- "Requires: Evidence [name]"
- "Requires: Cognition 4+"
- "Requires: Disposition +2"

This tells the player what to pursue to unlock the option. It is the game making explicit that investigation, relationship-building, and attribute investment have conversational payoffs.

**Hidden:** The utterance does not appear at all. Hidden gates are used for:
- Thread-sensitivity utterances when TS = 0 (the player shouldn't know these options exist before discovering Thread reality)
- Certainty-specific utterances at the far end of the range from the player's current position (a Certainty 5 character doesn't see the Thread-claiming options; a Certainty 0 character doesn't see the orthodox options)
- Disposition-gated Knot-level utterances (the intimacy of the option shouldn't be visible until the relationship is there)

### Outcome Types

Each utterance, when selected, produces one or more outcomes:

| Outcome | Effect |
|---|---|
| **Evidence yield** | Advances Evidence Track by 1. Available from factual utterances that prompt NPC disclosure. |
| **Disposition shift** | ±1 Disposition. Genuine engagement (Belief-gated, non-instrumental) shifts positively. Instrumental approaches trigger Sincerity Gate first. |
| **Conviction engagement** | Utterance touches the NPC's Worldview conviction. Routes into the Response Matrix (System 4) for resolution. May produce Conviction Wound. |
| **Information reveal** | NPC discloses something not on the Evidence Track — a name, a location, a relationship. Adds to Case Board without advancing the track. |
| **Escalation trigger** | The exchange has reached a confrontation point. Transition to Social Contest. The Lattice session ends; the Contest begins with the current Conviction/Composure state. |
| **Arc trigger** | The utterance activates an NPC arc moment — the conversation has pushed the NPC to a crisis point. Fires the arc vector. |

### Sincerity Gate Integration

The existing Sincerity Gate (Spirit TN 7 Ob 1, 37% failure) fires when the player selects an utterance that is instrumental — pursuing evidence or Disposition gain with concealed intent. The Lattice makes this automatic: utterances tagged [INSTRUMENTAL] trigger the gate before the utterance resolves. Belief-gated utterances are tagged [SINCERE] and bypass the gate.

This gives the Sincerity Gate its proper mechanical expression: it's not a random obstacle, it's a filter on intentionality. The player's choice of utterance signals intent; the Lattice reads that intent; the Gate fires accordingly.

---

## SYSTEM 4: RESPONSE RESOLUTION MATRIX

### What exists / what's missing

S10 NPC Behavior's 3-step decision procedure (Institutional Filter → Conviction Filter → Decision Fork by wound count) governs NPC Domain Actions. It is not a conversational response system — it routes the NPC's strategic behavior, not their reaction to a specific utterance.

What's needed: a filter chain that takes a player utterance (from the Dialogue Lattice) and a specific NPC (with their Genome, conviction state, and current context) and produces a differentiated, character-driven response. The same words should land differently with different NPCs and differently with the same NPC at different arc points.

### The Five-Filter Chain

Every NPC response to a player utterance passes through five filters in sequence. Each filter can: **pass** (response proceeds unmodified), **modify** (response character changes), **block** (response is impossible — NPC cannot engage), or **escalate** (response triggers arc moment or Contest).

**Filter 1 — Information Filter**

*Does the NPC have the conceptual framework to understand what the player is saying?*

The NPC's Certainty and Thread Sensitivity determine their interpretive framework:
- A Certainty 5 NPC receiving a Thread-reality utterance ("The thread here is unstable") does not have a framework for this. They interpret it through orthodoxy: heresy, delusion, or metaphor. Their response is filtered through that interpretation, not through the literal meaning of the utterance.
- A Certainty 0 NPC receiving an orthodox utterance ("The Church's doctrine on the Catastrophe explains…") interprets it with skepticism or as social performance.
- A Thread-aware NPC (TS 30+) receiving a TS-gated utterance from a player who also has TS 30+ is receiving it on a different channel than a non-aware NPC receiving the same words.

**Effect of Information Filter:** Responses that pass unmodified are direct engagement. Responses that are modified by the Filter are indirect — the NPC is engaging with their interpretation of what was said, not what was said. This produces the authentic experience of talking past each other — and of the rare moment when genuine comprehension occurs.

**Filter 2 — Conviction Filter** (extends existing S10 step 2)

*Does the utterance engage the NPC's Worldview conviction?*

If yes: the NPC's conviction wound count routes the response:
- Wound 0: NPC defends their conviction actively. Response is pushback, argument, or dismissal depending on Disposition.
- Wound 1: NPC engages but with visible strain. They cannot fully commit to their defense. Response may include an involuntary reveal (partial evidence disclosure, emotional crack).
- Wound 2+: NPC is in crisis. The utterance may produce Escalation (Contest) or Arc trigger. The NPC's response is no longer their "official" position — it is their actual one.

If no: pass through to Filter 3.

**Filter 3 — Disposition Filter**

*Is the NPC willing to engage at all?*

| Disposition Range | Response Character |
|---|---|
| −4 to −3 | Block. NPC refuses engagement. Dismisses, insults, or ignores. |
| −2 to −1 | Modified. NPC engages defensively. Every response is guarded, minimal, or deflecting. |
| 0 to +1 | Pass. Neutral engagement. Response is factual and measured. |
| +2 | Pass. Engaged response. NPC offers more than asked. |
| +3 to max | Pass + bonus. NPC responds with full transparency within their Compromise Profile. May volunteer the Knot-level utterance unprompted. |

**Filter 4 — Compromise Filter**

*If the utterance is implicitly or explicitly an offer, is the NPC willing to receive it?*

This fires when the player's utterance contains an offer (explicit: "I can ensure your archive access continues"; implicit: "I'm asking you to trust me"). The NPC's Compromise Profile determines:
- If the offer type matches a profile category they'll trade: Modified pass. Response acknowledges the offer and may counter.
- If the offer type is outside their profile (offering money to an NPC whose profile is Principled Refusal): Block on the offer; pass on the remainder of the utterance.
- If the NPC's Compromise Profile requires specific conditions (e.g., only exchanges information to faction-aligned actors): check player Standing before resolving.

**Filter 5 — Ethical Framework Filter**

*Does the player's approach (from the Dialogue Lattice's utterance style) align with the NPC's epistemological commitments?*

Each utterance carries an implicit style (matching the Social Contest taxonomy: Revealing/Obscuring × Precedent/Prospect). The NPC's ethical framework modifies response warmth:

| NPC Framework | Aligned Approach | Resisted Approach | Effect |
|---|---|---|---|
| Church (Faith) | Precedent + Revealing (doctrine, scripture, precedent) | Prospect + Revealing (Thread truth, empirical evidence) | Thread-true utterances produce hostility even if factually correct (+1 hostile modifier) |
| Crown (Virtue) | Revealing + Prospect (principled action, future consequences) | Obscuring (concealment, manipulation) | Obscuring utterances detected more easily; Disposition cost on use |
| Hafenmark (Categorical Imperative) | Precedent + Revealing (legal, consistent, universal) | Ad hoc/situational reasoning | Situational arguments get reduced Disposition yield even when persuasive |
| Varfell (Utility-driven) | Prospect + either (outcomes, effects, results) | Deontological appeals | "It's the right thing regardless of outcome" produces skepticism |
| Unaligned / RM | Variable by NPC Worldview | Institutional appeals | Faction-authority utterances produce automatic distrust modifier |

### Full Chain Example

Player utterance: "I know about the Thread experiments in Gransol" [Evidence-gated: Church-Thread-Lab]. Target NPC: a Church-aligned senior official, Certainty 4, Conviction (Faith) Wound 1, Disposition −1.

- Filter 1 (Information): Certainty 4 — the NPC understands "Thread experiments" as heretical practice. Their interpretive frame is threat assessment, not acknowledgment. Modified: they hear this as an accusation of Church heresy, not a neutral disclosure.
- Filter 2 (Conviction): Faith conviction, Wound 1. The utterance engages their conviction. Wound 1 response: defensive engagement with involuntary reveal. They do not deny the experiments — they argue for their doctrinal legitimacy. This is the crack: they've implicitly confirmed the experiments exist.
- Filter 3 (Disposition −1): Defensive response character. They confirm without admitting. Minimal disclosure.
- Filter 4 (Compromise): No offer in this utterance. Pass.
- Filter 5 (Ethical Framework — Faith): The utterance is Revealing + Prospect (empirical knowledge of heretical activity). This is the resisted approach. Hostility modifier applied to the response tone.

**Result:** The NPC responds defensively, with hostile tone, but with an involuntary confirmation of the facts — their Wound 1 prevents full suppression. The player gains 1 Evidence point (involuntary yield from Conviction Wound 1), the NPC's Disposition moves to −2 (hostile modifier from Filter 5), and the scene is now poised for escalation (the player has confirmed the experiments; the NPC has confirmed they know about them; the relationship has entered a new phase).

Without the filter chain, this would be a binary roll. With it, the resolution reflects the specific character of this specific NPC at this specific arc point.

### Bidirectionality and the Interdependency Matrix

The matrix is bidirectional. The player's Ontological Ledger gates what they can say; the NPC's Genome filters what response is produced; the outcome of the response modifies both:

- Player's Ledger: Disposition changes, Evidence Track advances, Case Board updates, potential Certainty shift (if NPC reveals Thread truth)
- NPC's Genome: Conviction Wound state may change, Volatility may shift (sustained engagement either entrenches or erodes), hidden Affiliation may be revealed, Compromise Profile may activate

This creates genuine interdependency: as both parties change, the conversation's possibility space changes. The options available in round 3 of a conversation are not the same as those available in round 1, because both Ledger and Genome have shifted.

**Axes of interdependency (full matrix):**

The player's approach interacts with NPC axes as follows:

|  | NPC Certainty 4–5 | NPC Certainty 2–3 | NPC Certainty 0–1 |
|--|---|---|---|
| **Player Certainty 4–5** | Orthodox alignment; smooth channel | Partial comprehension; interpretive gap | Full blockage on Thread-content; purely political channel only |
| **Player Certainty 2–3** | NPC reads uncertainty; moderate engagement | Both in transition; unpredictable; high Volatility sensitivity | Thread-aware NPC reads the hesitation; may attempt to pull player toward lower Certainty |
| **Player Certainty 0–1** | Complete mismatch; NPC routes to heresy framing | NPC partially follows; sensitive to Thread utterances | Full alignment; Thread channel open; most direct conversation possible |

The same interaction matrix applies for TS levels, Disposition ranges, and Conviction wound states — producing a multi-axis space of conversational possibility that is not a lookup table but an emergent result of the five-filter chain.

---

## CROSS-SYSTEM INTEGRATION TABLE

| Existing System | What Stays Unchanged | What Changes |
|---|---|---|
| S10 NPC Behavior | Named NPC priority stacks; 3-step Domain Action decision procedure | Decision procedure extended with Response Matrix for conversational resolution; generated NPCs use simplified 2-step version |
| S14 Fieldwork | All six action types; Evidence Track thresholds; Sincerity Gate | Interview action now routes through Dialogue Lattice + Response Matrix instead of single Charisma roll; Surveil action gains spatial context in scene graph |
| S12 Social Contests | Full contest mechanics unchanged | Contest is the escalation target from Dialogue Lattice, not the only social resolution mode. Lattice handles exploratory dialogue; Contest handles adversarial resolution. Lattice session can pre-load Contest with Conviction/Composure modifications from filter outcomes. |
| S16 Emergent Arcs | Vector format; 120+ arc vectors | NPE deviation ≥ 5 NPCs become latent arc vectors; Dialogue Lattice arc-trigger outcomes fire arc vectors; Response Matrix Conviction Wound changes update arc evaluator |
| S17 Scale Transitions | Domain Echo formula | Scene graph IS the Zoom In trigger system; scene graph templates address ED-545 |
| Player Agency Proposal | Beliefs, Duties, Scene Slate, scene action budget | Scene Slate Priority 4/5 now populated by NPE-generated NPCs with Genomes; Belief-gate in Dialogue Lattice directly references active Beliefs; Belief-gated utterances bypass Sincerity Gate |
| S18 Characters | All attributes; Certainty range; Histories | Certainty and TS now explicit gates in Dialogue Lattice, not just pool modifiers; Histories function as named tags that unlock History-gated utterances |
| S04 Clocks | No changes to clock mechanics | Season-end ecology updates (Piety drift → ecology weight shift) flow through existing accounting phase |

---

## PENDING DECISIONS (not editorial — mechanical gaps requiring resolution)

| ID | Decision | Impact |
|---|---|---|
| NPE-01 | Confirm ecology weight formula. Current proposal derives weights directly from territory stat values (Piety 4 = +2 Church weight). Alternative: step-function (Piety ≥ 3 = Church dominant, Piety ≤ 2 = contested). | Affects generation smoothness vs categorical clarity |
| NPE-02 | Persistence ceiling. How many generated NPCs can a territory hold before earlier ones are retired? Propose: cap at 3 persistent minor NPCs per territory per year; oldest retired if cap exceeded. | Prevents unbounded state accumulation |
| DL-01 | Hidden vs visible-locked threshold. At what distance from a gate condition does an utterance become hidden vs shown-locked? Propose: Attribute/Evidence/History gates always visible-locked (player can pursue these). Certainty/TS gates are hidden at extreme distance (more than 2 Certainty points away), visible-locked when close. | Affects pacing of discovery vs information |
| DL-02 | Lattice node count per conversation. Propose: 3–5 utterances available per Lattice node, 2–4 nodes per conversation before natural exit or escalation trigger. | Balances expressiveness against complexity |
| RR-01 | Filter failure handling. If Filters 1+5 both produce hostile modifiers, should they stack or cap? Propose: stack (maximum hostility reflects genuine incompatibility), cap at Disposition −2 (absolute floor for the round — the NPC is still present). | Affects ceiling of conversational failure states |

---

## EDITORIAL DECISIONS REQUIRED

[EDITORIAL: requires user approval — Territory cultural flavor. Each territory's social ecology needs authored descriptors: what is the typical worldview distribution, what is the emotional texture of the population. The weight formula is mechanical; what the weights represent in lived terms is editorial.]

[EDITORIAL: requires user approval — Named NPC Stance Triangles for Lenneth, Elske, and Haelgrund. Their positions on each active issue (Thread reality, Church authority, Altonian threat, RM legitimacy, Varfell autonomy) are character authorship decisions.]

[EDITORIAL: requires user approval — Dialogue Lattice utterance content. The gate types and outcome types are mechanical. The actual words available at each node are narrative authorship. This is the highest-volume editorial task in this proposal.]

[EDITORIAL: requires user approval — Scene graph content for each Zoom In trigger template. The node types and count are mechanical. What each node contains (which NPCs, what evidence, what time-of-day dependencies) is worldbuilding.]

[EDITORIAL: requires user approval — Compromise Profile content for named NPCs. What each named NPC will and won't trade, under what conditions, is character authorship. The Compromise Profile structure is mechanical; the values are editorial.]
