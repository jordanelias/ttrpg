# VALORIA — EMERGENT SCENARIO MAP

*Maps the principal causal chains, feedback loops, and multi-system collisions in the game. Not an exhaustive state machine — a navigator for the most consequential interaction paths. All values per compiled ruleset (Stage 1–12).*

---

## READING THIS DOCUMENT

Each section traces a scenario *root* → *chain* → *terminus states*. Branches are labelled by roll outcome or player decision. Where a chain feeds another chain, a cross-reference is marked **→ [SCENARIO X]**.

Termini are labelled:
- **STABLE** — sustainable campaign state
- **PRESSURE** — generates escalating clock movement
- **THRESHOLD** — a clock crosses a band; new rules activate
- **CAMPAIGN EVENT** — irreversible; restructures the game
- **RUPTURE** — shared loss condition

---

## SCENARIO 1: PRACTITIONER ENTERS COMBAT

```
Practitioner has Approach Training + TS 30+
│
├─ DECLARE Thread operation (Priority 5)
│   │
│   ├─ Opponent declares Attack this round?
│   │   ├─ YES → Practitioner INELIGIBLE for Leap
│   │   │         Must fight normally OR Withdraw
│   │   └─ NO  → ELIGIBLE → proceed to Diagnosis
│   │
│   ├─ DIAGNOSIS (Priority 4, round prior OR same round pre-Leap)
│   │   └─ GM describes: actualization, Gap proximity, temporal weight
│   │
│   └─ LEAP ROLL (Attunement + History + TPS, TN 7)
│       │
│       ├─ OVERWHELMING → Contact clean; next Operation Ob −1; +1 TS
│       ├─ SUCCESS      → Contact established; proceed
│       ├─ PARTIAL      → Unstable; Operation Ob +1; −2 Composure
│       └─ FAILURE      → No contact this scene; −4 Composure; Rattled
│
└─ CONTACT ESTABLISHED (Focus rounds remaining)
    │
    ├─ Practitioner TAKES WOUND during contact
    │   └─ Attunement check TN 7 Ob 1
    │       ├─ PASS → contact holds; −1D to remaining operations
    │       └─ FAIL → contact drops; operation = Failure
    │
    ├─ Practitioner reaches INCAPACITATION threshold during contact
    │   └─ Contact drops immediately; operation = Failure → [SCENARIO 3]
    │
    └─ OPERATION RESOLVES → [see SCENARIO 2]
```

---

## SCENARIO 2: THREAD OPERATION CONSEQUENCES

```
Operation declared and rolled
│
├─ WEAVING (Spirit + History + TPS, TN 7)
│   │
│   ├─ OVERWHELMING → Full effect; RS +1 (Rel+); +1 TS
│   │                  Over-actualisation if Relational+: subsequent Ob +1 for season
│   ├─ SUCCESS      → Full effect; substrate stable
│   ├─ PARTIAL      → Partial effect; RS −1; Coherence check harder
│   └─ FAILURE      → Interaction collapses; RS −2; Coherence −1 harder
│                      If RS ≤ 40: Shifting Object forms
│                      If RS ≤ 20: Gap opens → [SCENARIO 6]
│
├─ PULLING (Spirit + History + TPS, TN 7)
│   │
│   ├─ OVERWHELMING → Full effect; extended duration; RS unchanged
│   ├─ SUCCESS      → Full effect; standard duration
│   ├─ PARTIAL      → Partial effect; RS −1; Coherence retention harder
│   └─ FAILURE      → Snap-back; 1 Wound (no armour); RS −2; Coherence harder
│
├─ FORCED RESOLUTION — LOCK (Spirit + History, TN 7, min Ob 4)
│   │
│   ├─ OVERWHELMING → Target locked; RS −1; +1 TS
│   ├─ SUCCESS      → Target locked; RS −1
│   │                  Chronic drift begins: RS −1/season from season 2
│   ├─ PARTIAL      → Partial lock; RS −2; Coherence −1
│   └─ FAILURE      → Collapse onto practitioner; 2 Wounds; RS −3; Coherence −1
│                      Adjacent configs: +1 Ob for season
│
├─ FORCED RESOLUTION — DISSOLUTION (Spirit + History, TN 7, min Ob 4)
│   │
│   ├─ OVERWHELMING → Target dissolves; RS −3; Micro-Gap (closes this scene)
│   ├─ SUCCESS      → Target dissolves; RS −5; Gap forms (closes 1 scene)
│   ├─ PARTIAL      → Shifting Object; RS −6; Gap remains
│   └─ FAILURE      → Full Gap; RS −8; Monstrous Incursion; Practitioner Incapacitated
│                      → [SCENARIO 6] + [SCENARIO 3]
│
└─ CO-MOVEMENT FIRES on every operation regardless of outcome
    ├─ Temporal auto-effect: Object/Personal = narrative only (no Coherence)
    │                         Relational+ = Coherence retention roll
    ├─ Epistemic auto-effect: per degree table (social Ob shifts)
    └─ Actual d6: random consequence (cannot be predicted or traced)

    COHERENCE RETENTION ROLL (at end of full Leap contact window)
    Pool: Spirit + History + TPS, TN 7
    Ob:   sum of all operation Obs this Leap
    ├─ PASS → Coherence unchanged
    └─ FAIL → Coherence −1 → [SCENARIO 7]
```

---

## SCENARIO 3: COMBAT WOUND CHAIN

```
Fighter takes damage
│
├─ Damage = excess successes + STR + weapon modifier − Armour DR
│
├─ Damage < current Health → subtract; no further effect
│
└─ Damage ≥ current Health → WOUND TRIGGERS
    │
    ├─ Health resets to full
    ├─ Carry excess damage into new Health pool
    ├─ Wound count +1 → −1D to Combat Pool (cumulative)
    │
    ├─ SINGLE HIT CAP: max 2 Wounds per hit (excess damage discarded)
    │
    ├─ INCAPACITATION CHECK (by Endurance)
    │   ├─ End 1–3: incapacitated at 2 Wounds
    │   ├─ End 4–5: incapacitated at 3 Wounds
    │   └─ End 6–7: incapacitated at 4 Wounds
    │
    ├─ NOT INCAPACITATED → continue fighting at −1D/Wound
    │   └─ Stamina drain still applies → possible Out of Breath → [see below]
    │
    └─ INCAPACITATED
        ├─ Cannot act (not dead unless narrative demands or Coup de Grâce)
        ├─ If Practitioner: Contact drops; operation = Failure
        └─ Recovery options:
            ├─ Quick Rest (minutes–hours): Health full; remove 1 Wound
            └─ Full Rest (full night): all Health and all Wounds removed

STAMINA DRAIN CHAIN
│
├─ Stamina = Endurance + History + 1 (modified by armour)
├─ Depletes 1/round when: Move, Manoeuvre, or Attack
├─ Stamina 0 → FORCED Out of Breath
│   ├─ Half pool; Defence only
│   └─ Opponent: +2D Offence
└─ Take a Breath action OR Out of Breath → Stamina restored to full
```

---

## SCENARIO 4: SOCIAL CONFLICT TO FACTION CONSEQUENCE

```
Social scene opens
│
├─ READING EXCHANGE available (first round only)
│   Pool: Attunement + History, TN 7 Ob 1
│   ├─ OVERWHELMING → full emotional state + tells; +1D on first 2 exchanges
│   ├─ SUCCESS      → emotional state + 1 tell; +1D on first exchange
│   ├─ PARTIAL      → surface affect only
│   └─ FAILURE      → no info; opponent aware of scrutiny
│
├─ APPEAL (single roll, Presence + History)
│   Ob = Disposition of target (Friendly 1 → Contemptuous 5)
│   ├─ OVERWHELMING → persuaded; disposition improves 1–2 steps; bonus consequence
│   ├─ SUCCESS      → persuaded
│   ├─ PARTIAL      → requires additional condition
│   └─ FAILURE      → unmoved; may harden
│
├─ DEBATE (Cognition + History, simultaneous exchanges)
│   Stakes determine exchange count: Casual 1 / Formal 3 / Grand 5
│   │
│   Per exchange:
│   ├─ Higher net successes wins
│   ├─ Loser: +1 Composure strain (normal) or +2 (Overwhelming loss)
│   │
│   ├─ INSPIRATION ATTACK: Character Style + name specific Inspiration
│   │   If defender net ≤ 0: Inspiration loses 1 point → [SCENARIO 5]
│   │
│   ├─ COMPOSURE hits zero → RATTLED
│   │   ├─ −1D to all social rolls per Rattled mark
│   │   └─ UNMASK option:
│   │       ├─ All strain clears; Rattled clears
│   │       ├─ Player reveals something true
│   │       └─ Debate cannot resume → scene becomes personal confrontation
│   │
│   └─ Grand Debate 5–0 total loss: +1 Ob social vs that faction for 1 season
│
└─ DOMAIN ECHO (GM calls automatically when personal roll crosses scales)
    ├─ Faction-level consequence fires from same roll
    ├─ Domain Ob = target faction's relevant stat (1–7)
    ├─ Seasonal cap: ±2 per faction stat per season
    └─ Examples:
        ├─ Debate victory against Church representative → Church Mandate −1
        ├─ Successful Appeal to Parliament → Crown Influence +1
        └─ Evidence scene exposing Niflhel → TC −3 (Church-Niflhel complicity)
```

---

## SCENARIO 5: BELIEF / INSPIRATION CHAIN

```
Belief is active (character has 3 Beliefs at any time)
│
├─ BELIEF PURSUED in meaningful scene → +2 CP
├─ BELIEF CHALLENGED by events → +2 CP
├─ BELIEF GENUINELY REVISED in response to events → +4–5 CP
│
├─ BELIEF CONTESTED (creates tension with another character's Belief)
│   └─ Cannot pursue for CP until tension scene makes one character choose
│
└─ BELIEF COMPLETED
    └─ Option: convert to Inspiration at 1 point (no CP; conversion is the reward)

INSPIRATION CHAIN
│
├─ Inspiration = active at full value → Spend to add auto-successes (non-Thread)
│   1 Inspiration point = 1 auto-success before roll
│
├─ INSPIRATION ATTACK (Debate, Character Style)
│   Defender net ≤ 0 → Inspiration −1
│   If Inspiration reaches 0: focus lost; character loses the mechanical resource
│
├─ FOCUS DESTROYED/LOST
│   ├─ Inspiration drops to 0 immediately
│   └─ GRIEF SCENE: Spirit TN 7 Ob 2
│       ├─ SUCCESS → new Inspiration at (old value −1), thematically linked
│       └─ FAILURE → Inspiration lost entirely
│
├─ MOMENTUM tracks accumulated advantage (0–4)
│   ├─ Gain: +1 on Overwhelming success; +1 when Belief achieved
│   ├─ Spend: before non-Thread roll; 1 Momentum = 1 auto-success
│   └─ Reset to 0 at session start
│
└─ ADVANCEMENT via CP
    Attribute +1: Current score × 3 CP (narrative training required)
    History +1: 3 CP (capped at Memory score total)
    Inspiration +1: 3 CP (cap = Spirit score)
```

---

## SCENARIO 6: GAP FORMATION AND MONSTROUS INCURSION

```
GAP OPENS (from: Dissolution failure, Weaving failure at RS ≤ 20,
            Past-Oriented Pull, operation failure at RS threshold)
│
├─ RS CONSEQUENCES BY CURRENT RS VALUE at Gap formation
│   ├─ RS < 40  → Shifting Object forms
│   ├─ RS 40–59 → Weak monstrous configuration
│   ├─ RS 60–79 → Full monstrous entity
│   └─ RS 80+   → Full entity + Shifting Object in each adjacent territory
│
├─ SHIFTING OBJECT stage (pre-Gap or from Partial operations)
│   └─ Mend (Ob 2, TS 50+) can close before it escalates
│
├─ GAP PERSISTS (not Mended this scene)
│   └─ RS −4 per season (active Gap drain)
│       │
│       └─ After 1+ seasons: Entrenched Gap (Mend Ob 6, TS 70+)
│          After 3+ seasons: Catastrophic Gap (Mend Ob 7; Einhir ritual or collective)
│
├─ MENDING ATTEMPT (Attunement + Focus + TPS, TN 7)
│   Ob = Gap severity (Shifting 2 → Catastrophic 7)
│   │
│   ├─ OVERWHELMING → Gap closes; RS +2; Coherence −1; Mended zone +1 Ob to Gap formation for 1 season
│   ├─ SUCCESS      → Gap closes; RS +1; Coherence −1
│   ├─ PARTIAL      → Gap reduced 1 severity category; second Mending needed
│   └─ FAILURE      → Gap unchanged; Coherence −1; RS −2
│
├─ MONSTROUS INCURSION
│   ├─ Treated as narrative/combat encounter in TTRPG
│   ├─ Increases Church Credibility Evidence (Inquisitor's investigation pool)
│   ├─ Contributes to TC rise (Thread events read as divine warning if RS < 55)
│   └─ RS < 40 active: Monstrous Incursion risk in all territories with Gaps
│
└─ MULTI-SEASON UNADDRESSED GAP CHAIN
    RS active drain: −4/season per Gap
    Lock chronic drift: −1–2/season
    Winter passive drift: −1/season
    Combined: −6 to −10+/season without intervention
    → If this exceeds Mending output → RS terminal decline → [SCENARIO 9]
```

---

## SCENARIO 7: COHERENCE DEGRADATION

```
COHERENCE starts at 10 (all practitioners)
│
├─ COHERENCE LOSS triggers
│   ├─ Retention roll fail at end of Leap (primary source)
│   ├─ Dissolution residue use: automatic −1 (in addition to retention roll)
│   ├─ Operation Failure degree tables: +1 Ob to retention roll this Leap
│   └─ No passive recovery — requires deliberate action
│
├─ COHERENCE 10–8: STABLE — no mechanical penalty
│
├─ COHERENCE 7–5: DISSONANT
│   ├─ Narrative flickers (wrongness, déjà vu, events slightly out of sequence)
│   └─ Close Knots sense wrongness (+1 strain/3 sessions)
│
├─ COHERENCE 4–3: FRAGMENTED
│   ├─ −1D all social rolls
│   ├─ −1D Memory-based rolls
│   ├─ GM may present character recollection differently from others' recall
│   ├─ All Knots at +1 strain/2 sessions
│   ├─ +1 Ob on all Thread operations including Leap (rendering reasserts harder)
│   └─ Roll FRAGMENTED FALLOUT (d6) on entering this band
│
├─ COHERENCE 2: FRACTURED
│   ├─ −2D social and Memory rolls
│   ├─ All Knots +1 strain/session
│   ├─ Once/scene with Thread op: Spirit TN 7 Ob 1 or lose 1 round (dissociation)
│   ├─ Certainty max −1 per Coherence level below 3
│   ├─ BELIEF CO-AUTHORSHIP begins (GM and player rewrite Beliefs to reflect
│   │   dissolving perceptual categories)
│   └─ Roll FRACTURED FALLOUT (d6) on entering this band
│
├─ COHERENCE 1: SEVERED
│   ├─ −2D social, −2D Memory
│   ├─ Dissociative episodes: once/scene regardless of operations (scene start)
│   ├─ +2 Ob on all Thread operations including Leap
│   ├─ All Knots +2 strain/session
│   └─ Practitioner's rendering barely holds; self/world distinction dissolving
│
└─ COHERENCE 0: RENDERING CRISIS
    ├─ Campaign event
    ├─ Practitioner must resolve narratively (relational anchoring, withdrawal)
    └─ If unresolved by season end → NPC

COHERENCE RECOVERY
├─ Full season non-practice (no Thread ops): +1 Coherence
├─ Close Knot Anchoring Scene (Bonds TN 7 Ob 2): +1 Coherence; costs Knot +1 strain
└─ Cannot exceed 10; cannot be purchased with CP
```

---

## SCENARIO 8: FACTION CLOCK INTERACTIONS

```
Three clocks run simultaneously: RS (100→0), TC (0→100), IP (0→100)
Starting values: RS 28 (Stirring), TC 22, IP 20
│
├─ RS FALLS BELOW 55
│   ├─ TC +1/season
│   └─ IP +1/season
│
├─ RS FALLS BELOW 40
│   ├─ TC +2/season (total, replaces the +1)
│   ├─ IP +2/season (total)
│   └─ Gaps may open spontaneously: 1d10/season; on 1–2 → Gap in lowest-Prosperity territory
│       → [SCENARIO 6]
│
├─ TC RISES ABOVE 40
│   └─ IP +1/season (Church mediation gives Merchant Consortium political cover)
│
├─ TC RISES ABOVE 60
│   ├─ IP +2/season (Altonia: Church expansion violates Secession Wars clauses)
│   └─ If IP > 45 simultaneously:
│       ├─ IP +2/season additional
│       └─ Almaic Kyriakos begins formal documentation for Altonian Emperor
│
├─ TC > 60 AND RS < 40 SIMULTANEOUSLY
│   └─ Both clocks accelerate at maximum rate → fast path to dual CAMPAIGN EVENTS
│
├─ ALL THREE CLOCKS ABOVE MIDPOINT SIMULTANEOUSLY
│   └─ Campaign enters ENDGAME PHASE
│
├─ RS THRESHOLD EFFECTS (activate/deactivate at Accounting)
│   ├─ RS 59–40 (Fragile): Shifting Objects spontaneously form in Thread territories
│   │   one random Shifting Object/season; Thread ops +1 Ob in affected territories
│   ├─ RS 39–20 (Fractured): Gaps may open spontaneously; Monstrous Incursion risk
│   │   non-practitioners experience rendering failures
│   └─ RS 19–1 (Critical): +1 Ob all Thread ops worldwide; faction Stability checks Ob 1/season
│       Fail → Mandate −1 (min 0); at Mandate 0 fail → Faction Fracture (sub-faction splinters)
│
└─ FACTION INTERACTIONS (Domain Actions, seasonal)
    ├─ Crown vs Church: Sovereignty axis (TC brake via Sovereign Authority Doctrine)
    ├─ Church vs all:   Excommunication, Territory Seizure at TC 60+
    ├─ Guilds:          Economic friction; Thread operations visible → TC +1/event
    ├─ Revolution:      Community Weaving (RS −2/season if sustained); loses Mending
    │                   at Mandate 0 → feedback loop severs RS recovery
    └─ Niflhel:         Residue harvesting (RS +0.5/season); Church-Niflhel exposure → TC −3
```

---

## SCENARIO 9: TERMINAL Rendering Stability DECLINE — THE EINHIR PATH

```
RS ENTERS CRITICAL BAND (19–1)
│
├─ AUTOMATIC PRESSURES per season (cumulative unless resolved)
│   ├─ Active Gaps: −4/Gap
│   ├─ Active Locks chronic drift: −1 to −2/Lock
│   ├─ Winter passive drift: −1
│   ├─ Spontaneous Gaps: 1d10; on 1–4 → new Gap
│   └─ Thread ops +1 Ob worldwide (all sources)
│
├─ FACTION STABILITY CHECKS Ob 1/season
│   ├─ Fail → Mandate −1
│   └─ At Mandate 0 fail → Faction Fracture (sub-faction splits)
│
├─ MENDING as only RS recovery path
│   Best single Mending: RS +1 (Success) or +2 (Overwhelming)
│   At RS 1: most operations risk Rupture on Failure
│   Success rate at Ob 5–7: ~17–58% even at maximum pool
│   Net seasonal RS change with active Mending: typically −8 to −15 still
│
├─ STRUCTURAL EXIT REQUIREMENTS (all must occur)
│   ├─ 1. Remove all active Locks (eliminate drift): Pull at Ob = (Lock TS ÷ 10) − 2
│   ├─ 2. Mend all active Gaps (eliminate per-season drain)
│   ├─ 3. Operate exclusively Object/Personal scale going forward
│   └─ 4. Sustained cross-faction practitioner cooperation (Collective Operations)
│          → Collective Pool: Anchor + helper floor(Cog ÷ 2) per helper
│             Conflicting Beliefs: non-chaining or requires pre-Leap Spirit check
│
├─ COLLECTIVE OPERATION FAILURE at RS 1
│   └─ Operation Failure → RS −8 (Dissolution) minimum
│      At RS 1: RS 1 − 8 = RS ≤ 0 → THE RUPTURE
│
└─ THE RUPTURE (RS = 0)
    ├─ Campaign event — not loss in the conventional sense
    ├─ No faction wins
    ├─ Ein Sof erupts through failed substrate: too much being for consciousness to render
    └─ The world does not end — it becomes unintelligible
```

---

## SCENARIO 10: THREADCUT BEING IN PLAY

```
Threadcut being present (e.g., Solmund-type)
│
├─ OBSERVER PERCEPTION varies by TS
│   ├─ TS 0–9   → nothing, or vague unease
│   ├─ TS 10–29 → unstable image, details shift
│   ├─ TS 30–49 → coherent but wrong in inarticulable ways
│   ├─ TS 50–69 → fully rendered; self-sustaining work visible as hum
│   └─ TS 70+   → perceives the continuous effort holding the being in place
│
├─ BEYOND-CEILING RENDERING (being renders itself more intensely)
│   └─ Cost: +1 Rendering Strain/scene of beyond-ceiling rendering
│
├─ EXTERNAL THREAD OPERATIONS (being directs intentionality outward)
│   ├─ No Leap required (already in originary state)
│   ├─ Standard operation pool (Spirit + History + TPS) vs standard Ob
│   └─ Cost: +1 Rendering Strain per external operation
│
├─ WOUNDS
│   └─ Each Wound costs 1 additional point of sustained Thread work
│       (rather than conventional Ob penalty)
│
├─ DE-ACTUALISATION TRIGGER (either of these independently)
│   ├─ Rendering Strain = Health
│   └─ Wounds reach Rendering Threshold (Health ÷ 2)
│       │
│       ├─ Round 1: Intelligible face dissolving; all ops +2 Ob
│       │   └─ Stabilisation attempt: Weave on self, Ob = Wounds + Rendering Strain
│       ├─ Round 2: Perceivable only by TS 50+; ops +4 Ob; second stabilisation
│       └─ Round 3+: Configuration returns to unintelligible ground
│                    Micro-Gap forms (closes this scene)
│                    Dissolution residue remains
│
├─ PAST-ORIENTED PULLING targeting threadcut being
│   └─ Auto-produces a Gap (no temporal thread; no accumulated past)
│       → [SCENARIO 6]
│
└─ VOLUNTARY CESSATION
    └─ Being stops sustaining itself; De-Actualisation without Ob penalties
        The Solmund Choice: act and begin to cease, or preserve existence at
        cost of inaction
```

---

## SCENARIO 11: ALTONIAN INTERVENTION CHAIN

```
IP RISES (various sources)
│
├─ PUBLIC THREAD USE observed by Altonian agents → IP +2/event
├─ SUCCESSION DELAY past 2 campaign arcs → IP +2
├─ RS < 55 → IP +1/season (cross-clock)
├─ TC > 40 → IP +1/season
├─ TC > 60 → IP +2/season
│
├─ IP 30+ → TUTORING DEMAND triggers (Prince Torben)
│   └─ Crown must respond; delay feeds TC and IP simultaneously
│
├─ IP 45–59: HOSTILE
│   ├─ Border skirmishes
│   ├─ Vassalage demands through diplomatic channels
│   └─ Church offers Altonian theological mediation → TC +1/season
│
├─ IP 60–74: WARLIKE
│   ├─ Invasion preparations begin
│   └─ Altonian factions (3 internal) begin applying direct pressure
│       to Valorian factions separately — factional unity required
│
├─ IP 75–99: INVASION IMMINENT
│   └─ Merchant Consortium's position collapses
│       (primary internal Altonian brake removed)
│
├─ IP 100: INVASION
│   └─ CAMPAIGN EVENT — Altonian forces enter Valoria
│
└─ IP DECREASE PATHS
    ├─ Unified Valorian diplomatic front (all factions cooperative): IP drift halts 1 season
    ├─ Schoenland trade alliance: IP −2/year; removes Merchant Consortium political cover
    └─ Grand Diplomatic Scene victory (requires: faction dominance + Church Mandate > 5
        + RS > 50): IP frozen; peace treaty available
```

---

## SCENARIO 12: SUCCESSION CRISIS PATHS

```
Crown faces succession question (Torben / Elske / Parliament / coup)
│
├─ TUTORING DEMAND (IP 30+)
│   ├─ Accept: Crown legitimacy preserved; Torben leaves Valoria temporarily
│   │   └─ Altonian influence over heir grows; future complication seeded
│   └─ Refuse: IP +2 immediately; RS < 55 means TC also rises this season
│
├─ TORBEN PATH
│   ├─ Torben established as heir: Crown Mandate stable; Church monitoring
│   ├─ Torben dies or is removed: succession vacuum → IP +2; TC +2 (Church offers stability)
│   └─ Torben reveals Thread sensitivity: → [SCENARIO 1] + Church Credibility Evidence surge
│
├─ ELSKE PATH
│   ├─ Elske as heir: Varfell support; Church opposition (heresy risk)
│   ├─ Elske pursues Thread practice openly: TC +1–2/event; → [SCENARIO 2]
│   └─ Elske and Thread operation conflicts: cross-ref Stage 13 NPCs (SIM8-F-02)
│
├─ PARLIAMENTARY PATH
│   ├─ Parliamentary Vote (Debate structure, 3 exchanges, faction pools)
│   ├─ Church contests → TC rise via demand unmet
│   └─ Hafenmark supports constitutional resolution → Ob reduced (Categorical Imperative)
│
├─ COUP PATH
│   ├─ Any faction Stability 0 → Faction Fracture risk (RS ≤ 19)
│   ├─ NPCs with coup trigger conditions: RS ≤ 10 → +1 to trigger check pool
│   └─ Successful coup: Crown Mandate collapses; IP surge; TC surge if Church-aligned
│
└─ ROYAL DECREE (Crown Unique Action, 1/season)
    Roll: Mandate vs Ob 2
    ├─ SUCCESS → one faction attribute ±1 takes effect immediately (not at Accounting)
    ├─ FAILURE → Mandate −1 (overreach)
    └─ Consecutive seasons: +1 Ob per consecutive use (decree fatigue)
```

---

## SCENARIO 13: COLLECTIVE THREAD OPERATION

```
Multiple practitioners target same configuration
│
├─ COLLECTIVE DIAGNOSIS (shared GM exchange before Leap)
│   All practitioners listen to same description; set shared intentionality
│
├─ ANCHOR designated (highest TS) — sets primary intentionality
│
├─ ALL PRACTITIONERS ROLL LEAP simultaneously (Priority 5)
│   │
│   ├─ ANCHOR FAILS → collective lattice does not form
│   │   ├─ Helpers who succeeded: individual contact; no pool bonus; their own Ob applies
│   │   └─ Individual results apply; collective benefit lost
│   │
│   ├─ ANCHOR SUCCEEDS, some helpers FAIL
│   │   └─ Remove failed helpers' dice; if remaining pool < half Anchor solo pool → +1 Ob
│   │
│   └─ ALL FAIL → all take individual Leap failure consequences
│
├─ CONTACT ESTABLISHED (lattice active)
│   ├─ Each helper contributes floor(Cog ÷ 2) bonus dice to Anchor's pool
│   ├─ Helpers cannot Fork; Anchor cannot Fork while Anchoring
│   │
│   ├─ CONFLICTING BELIEFS
│   │   ├─ Tangentially conflicting → helper's dice do not chain on 10
│   │   └─ Directly opposing → helper must pass Spirit TN 7 Ob 1 pre-Leap
│   │       ├─ PASS → participates with non-chaining dice
│   │       └─ FAIL → drops out before Leap
│   │
│   ├─ HELPER CONTACT DROPS mid-operation
│   │   └─ If pool drops below half Anchor solo pool → +1 Ob (lattice fractures)
│   │
│   └─ CO-MOVEMENT SCALES WITH PARTICIPANT COUNT
│       More configurations interacting → proportionally greater consequences
│       → [SCENARIO 2] for each operation rolled; all Coherence costs apply individually
│
└─ COLLECTIVE MENDING (for Catastrophic Gaps / Locked Zones)
    └─ As above, targeting substrate absence rather than thread
        Mend Ob ceiling: 8 (applies even to stacked collective modifiers)
        Required for: Catastrophic Gap (Ob 7), Locked Zone border (Ob 8+)
        → Only structural exit from RS terminal decline → [SCENARIO 9]
```

---

## SCENARIO 14: SCALE TRANSITION — PERSONAL TO MASS COMBAT

```
Personal combat occurring during a mass battle
│
├─ COMBATANT declares Personal Action at Phase 5 (Priority 8)
│   ├─ Limit: 1 exchange per battle turn
│   ├─ Named NPC targets become CONTESTED FIGURES
│   └─ Commander taking Personal Action: CR suspended this turn
│       (mass battle continues at reduced command efficiency)
│
├─ THREAD OPERATION during mass combat
│   │
│   ├─ OFFENSIVE (Dissolution, offensive Pull targeting enemy units)
│   │   └─ Fires Phase 2 (before Engagement), simultaneous with Volley
│   │       Declared Phase 1; RS costs ×3 floor, capped +15/operation
│   │
│   └─ SUPPORT (Weave, Mend, Lock, non-offensive Pull)
│       └─ Fires Phase 5 (Cascade), after Engagement
│           Declared Phase 1; Leap resolves at Phase 5
│
├─ SOCIAL SCENE IN COMBAT CONTEXT
│   └─ Social scene outcomes apply before next round's declaration phase
│       (a pre-battle appeal can alter opening combat state)
│
├─ DOMAIN ECHO from mass combat outcome
│   ├─ Major battle → RS +2 (significant mass battle source)
│   ├─ Thread op in mass combat → RS ×3 floor cost
│   └─ Einhir site under siege stress → RS −1 additional/season
│
└─ ZOOM IN / ZOOM OUT vocabulary
    ├─ Zoom In: GM narrows from mass scale to personal duel within battle
    ├─ Zoom Out: returns to mass battle after personal resolution
    └─ Zone-based spatial system: movement is zones, not grid
        Moving between zones = full action OR attack at −1D Offence
```

---

## SCENARIO 15: BOARD GAME / HYBRID MODE THREAD ORDER COLLISION

```
TTRPG practitioner (Personal Phase) and Board Game order (Strategic Phase)
target same configuration with OPPOSING INTENTIONALITIES
│
├─ Flag at Personal Phase declaration
├─ Both operations HELD
├─ Resolve simultaneously at CASCADE PHASE (opposing operations procedure §5.1.4)
│
├─ TTRPG practitioner's roll: stands as input from Personal Phase
├─ Board game order roll: made at Cascade Phase
│
├─ Outcome determines which intentionality wins
│   ├─ Both succeed: higher net successes prevails; loser's RS cost still applies
│   ├─ One succeeds, one fails: succeeding side prevails; failing side's RS cost applies
│   └─ Both fail: neither effect; both RS costs apply → net RS loss with no gain
│
├─ RS CHANGES: both Personal and Strategic Phase applied at Accounting
│   Seasonal cap: ±10 net per season (cap applies to net after all sources)
│
├─ COHERENCE: PC practitioner leading a Strategic Phase Thread order
│   └─ Declare leadership at start of Cascade Phase (one PC per order)
│       ├─ PC declares leadership → full Coherence cost applies to that PC
│       └─ No PC declares → no Coherence cost (NPC-led; no personal Leap)
│
└─ LOCK CHRONIC DRIFT: registered on territory card at Cascade Phase
    Drift begins next Accounting: RS −1/season per locked territory
```

---

## CROSS-SCENARIO FEEDBACK LOOPS

*The most dangerous emergent states arise from multiple loops firing simultaneously.*

### Loop A — The Einhir Spiral (most common campaign-ending pattern)
```
Practitioner ambition (large-scale operations)
→ RS loss per operation
→ RS crosses threshold → +1 Ob worldwide
→ Operations harder → more Partial/Failure outcomes
→ More RS loss per failed operation
→ Gaps open → Monstrous Incursion → Church Credibility Evidence rises
→ TC rise → IP rise → factional instability
→ Factional instability → Domain Actions misfiring → Mandate drops
→ Revolution loses Community Mending access (Mandate 0)
→ RS loss unaddressed → RS Critical → [SCENARIO 9]
```

### Loop B — Church Dominance Lock
```
TC rises above 55 (RS < 55 cross-clock)
→ TC +2/season; IP +1/season
→ IP > 45: Church offers theological mediation
→ TC +1/season additional
→ Church Mandate climbs → Excommunication threats
→ Nobles defect or are silenced → Crown Mandate −1
→ Crown Mandate loss → fewer anti-TC options
→ TC > 60: IP +2/season; Almaic Kyriakos documents
→ IP 75: Merchant Consortium collapses
→ IP 100: INVASION
```

### Loop C — Practitioner Coherence Cascade
```
Practitioner uses Dissolution Residue (Coherence −1 guaranteed)
→ Retention roll at end of Leap (another possible −1)
→ Coherence 4–3: +1 Ob on ALL Thread operations including Leap
→ Harder operations → more Partial/Failure → more retention failures
→ Coherence 2: Belief Co-Authorship; dissociation risk
→ Coherence degradation → social penalties → Knot strain accelerates
→ Knot strain → relational support eroding
→ No Anchoring Scenes possible if Knots broken
→ No Coherence recovery path
→ Coherence 0: Rendering Crisis → practitioner becomes NPC
```

### Loop D — Revolutionary Thread Access Window
```
RS rises (world destabilising)
→ RS 40+: Leap becomes available (Stirring/Wakening)
→ Previously dormant TS characters can Leap
→ New practitioners emerge; Thread practice visible
→ Church TC rise (visible Thread use +1/event)
→ TC rise → IP rise → factional instability
→ BUT: if Revolution Community Weaves successfully:
    RS −2/season; factional Stability pressure relieved
→ IF Revolution Mandate drops to 0 (RS Critical → faction Stability checks):
    Community Mending blocked → RS accelerates
→ Window closes precisely when it's needed most
```

---

*Document reflects compiled ruleset through Stage 12 / checkpoint 14. Open gaps per valoria_gap_register_consolidated.md are not resolved here — see gap register for P1/P2 items.*
