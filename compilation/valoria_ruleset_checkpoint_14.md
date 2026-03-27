---
*All mechanics derive from the Philosophical Foundations. Where this document conflicts with the Foundations, the Foundations govern.*
---

# VALORIA RULESET — CHECKPOINT 14
## Complete Edition · Phase 2 Compilation
### Stage 17 Canon Guard Passed · Hybrid Gaps Resolved · 2026-03-26

---

# VALORIA TTRPG RULESET
## Complete Edition — Compilation Draft
### Phase 2 Assembly · All 16 Stages

*All mechanics derive from the Philosophical Foundations document.*
*Where this ruleset conflicts with the Foundations, the Foundations govern.*
*Where this ruleset conflicts with Mechanics.docx, Mechanics.docx governs.*

---

**HOW TO USE THIS DOCUMENT**

New players: read Parts 1–4 first. Play your first session. Everything else comes up as needed.

GMs: read all parts before Session Zero. Keep Part Fourteen (GM Tools) and the Game Sheet at hand during play.

Board game mode: read Parts 1, 6, 7, 8, and Part Twelve (Campaign Modes, §12.2).

---



# VALORIA TTRPG RULESET — COMPILATION DRAFT

*All mechanics derive from the Philosophical Foundations. Where this document conflicts with the Foundations, the Foundations govern.*

---

# PART ONE: CORE ENGINE

## 1.1 Dice

Roll a pool of d10s.

| Result | Effect |
|--------|--------|
| 7–9 | One success |
| 10 | One success + roll one bonus die (chains indefinitely) |
| 1 | Subtract one success from net total |
| 2–6 | No effect |

Net successes = total successes minus total 1s rolled (including bonus dice).

## 1.2 Target Numbers

The Target Number (TN) sets the threshold for what counts as a success on each die. The default is TN 7; situational modifiers shift it.

| Situation | TN | When |
|-----------|-----|------|
| Controlled | 6 | Prepared, unhurried, favourable conditions |
| Standard | 7 | Default for most rolls |
| Desperate | 8 | Duress, hostile environment, exhaustion, existential threat |

Combat uses **Weapon TN** (see §8.3). Thread operations use TN 7 (Standard) or TN 8 (Desperate-equivalent for Forced Resolution and Past-Oriented Pulling).

TN and Ob are independent difficulty axes. TN governs per-die success probability; Ob governs the number of successes required.

## 1.3 Obstacles

The Obstacle (Ob) is the number of net successes required to achieve the intended outcome.

| Ob | Difficulty | Example |
|----|-----------|---------|
| 1 | Routine | Asking a willing friend for help; climbing a low wall |
| 2 | Moderate | Picking a standard lock; persuading a sceptical merchant |
| 3 | Difficult | Breaking into a guarded archive; swaying a hostile crowd |
| 5 | Entrenched | Opposing Church doctrine publicly; crossing a militarised border |
| 8 | Structural | Usurping a political institution; performing Dissolution at Territorial scale |
| 10 | Foundational | Restructuring history; challenging a faction's core identity |

**Maximum Ob: 10.** No roll may have effective Ob above 10 regardless of modifier stacking. Success at Ob 10 is a genuine miracle warranting exceptional narrative treatment.

**Ob stacking:** When multiple modifiers increase Ob (Wounds, terrain, scale, zone conditions), they stack additively but cap at Ob 10.

## 1.4 Degrees of Success

| Degree | Condition | Effect |
|--------|-----------|-------|
| Overwhelming | Net ≥ 2× Ob | Exceptional outcome; +1 Momentum |
| Success | Net ≥ Ob | Goal achieved as intended |
| Partial | Net > 0 but < Ob | Goal achieved with a complication |
| Failure | Net ≤ 0 | Goal not achieved; complication occurs |

**Ob 10 exception:** Overwhelming is unavailable at Ob 10. Partial requires net ≥ 5. Below 5 = Failure.

## 1.5 Let It Ride

Once a roll resolves a situation, the result stands. No re-attempts unless circumstances have significantly changed. Neither player nor GM may call for a re-test of the same situation.

## 1.6 Fail Forward

Failure does not halt the narrative. Partial success: the goal is achieved but an unwanted complication accompanies it. Failure: the goal is not achieved and a complication occurs. In both cases, the story moves forward.

The GM should consult the Hard Moves table (§13.5) for structured complication options rather than improvising consequences.

## 1.7 Momentum

Momentum tracks a character's accumulated advantage. Range: 0–4.

**Gain:** +1 on Overwhelming success. +1 when a Belief is achieved.

**Spend:** Before any non-Thread roll, spend Momentum to add automatic successes (1 Momentum = 1 success). Any amount may be spent in a single roll.

**Reset:** Momentum resets to 0 at the start of each session. It does not carry between sessions.

Momentum cannot be spent on Thread operation rolls. Thread operations have their own economy (see §4).

## 1.8 Beginner's Luck

When a character attempts a task with no applicable History, they may roll at **double Ob** using only their raw attribute dice (no History bonus). A success at Beginner's Luck earns the first mark toward establishing a new History (see §10.2).

A character cannot use Beginner's Luck for: Thread operations (require Approach Training), combat proficiency rolls (require at least basic weapon familiarity), or faction Domain Actions (require institutional standing).

## 1.9 Fibonacci Group Bonus

When multiple characters declare actions against a single unsupported opponent in the same round, they receive bonus dice following the Fibonacci sequence:

| Attackers | Bonus Dice (each) |
|-----------|-------------------|
| 2 vs 1 | +1D each |
| 3+ vs 1 | +2D each |
| 5+ vs 1 | +3D each |
| 8+ vs 1 | +5D each |

The bonus applies to each attacker's offence pool. The defender splits their defence pool across all incoming attacks (dividing defence dice among attackers before resolution).

An opponent is "unsupported" if no ally is engaging any of the attackers.

---

# PART TWO: ATTRIBUTES

## 2.1 The Ten Attributes

Attributes range from 1 to 7. A score of 3 is the human average. 1 is severely limited; 7 is the mortal maximum.

### Physical

| Attribute | Abbreviation | Governs |
|-----------|-------------|---------|
| **Agility** | Agi | Speed, precision, reflexes; combat pool base; dodge; initiative |
| **Endurance** | End | Stamina, vitality, resilience; Health derivation; Breather recovery |
| **Strength** | Str | Raw physical force; weapon handling requirements; carrying capacity |

### Mental

| Attribute | Abbreviation | Governs |
|-----------|-------------|---------|
| **Cognition** | Cog | Perception, reasoning, analysis; Thread Leap and Weaving base; investigation |
| **Memory** | Mem | Knowledge, experience, retention; per-History point cap; Weaving pool contribution |
| **Focus** | Foc | Concentration, discipline, precision under pressure; Thread operation sustained attention; resisting distraction mid-task |

### Social

| Attribute | Abbreviation | Governs |
|-----------|-------------|---------|
| **Attunement** | Att | Empathy, perception of others, emotional reading; detecting deception; Reading pool base |
| **Bonds** | Bon | Relational depth, trust capacity; Knot strain cap; collective operation stability |
| **Presence** | Pres | Influence, command, charisma; social pools (Appeal, Circles); faction actions |

### Metaphysical

| Attribute | Abbreviation | Governs |
|-----------|-------------|---------|
| **Spirit** | Spi | Will, existential resilience, inner coherence; Certainty derivation; Confrontation checks; Intelligibility resistance; maximum Inspiration value |

## 2.2 Attribute Creation

**Point pool at creation:** 31 points distributed across 10 attributes.

**Constraints:**
- Minimum 1 per attribute
- Maximum 5 at creation (one attribute may be 5; all others ≤ 4)
- Maximum 7 through advancement

## 2.3 Derived Scores

| Score | Formula | Range | Notes |
|-------|---------|-------|-------|
| Health | Endurance + 6 | 7–13 | Damage buffer before Wounds |
| Composure | Presence + 6 | 7-13 | Social damage buffer before Rattled |
| Combat Pool | Agility + weapon proficiency History (points + 3) | Variable | Split between Offence and Defence each round |
| Contact Rounds | Focus | 1–7 | Maximum rounds maintaining Thread contact (practitioners only) |
| Certainty | Spirit (starting and maximum value) | 0–7 | Existential coherence; at 0, rendering crisis |
| Coherence | 10 (starting value); countdown to 0 | 0–10 | Measures how legible reality remains to the character |

**Contact Rounds** uses Focus because sustained Thread contact is an act of concentration, not willpower.

---

# PART THREE: COMBAT ENGINE (Pool Split)

## 3.1 Overview

Combat uses a simultaneous pool-split system. Each round, combatants secretly divide their Combat Pool between Offence and Defence dice. All pools are revealed and resolved simultaneously.

This means: every combat exchange carries genuine risk. Over-committing to offence leaves you exposed. Over-committing to defence lets opponents act freely. The division decision is the core tactical choice.

## 3.2 Initiative

At combat start, each combatant rolls Agility (TN 7, Ob 1).

The **winner declares their pool division last** each round after seeing opponents' announced action types (but not their die allocations). This is the information advantage: you know whether opponents are attacking, defending, manoeuvring, or operating before committing your own split.

Ties: re-roll. Initiative holds for the entire combat unless a specific Manoeuvre (Reorient, §8.6) changes it.

## 3.3 Round Structure

Each round has three phases:

**Phase 1 — Declaration (ascending Initiative order):** Each combatant announces their action type: Attack, Full Defence, Manoeuvre, Thread Operation, Move, or Withdraw. Thread operation declarations are public. Declarations are not binding on pool split — only on action type.

**Phase 2 — Division (ascending Initiative order; initiative winner divides last):** Each combatant secretly divides their Combat Pool between Offence and Defence dice. Minimum 1 die in each if engaging in both attack and defence. A combatant may commit all dice to Offence (reckless — no defence this round) or all to Defence (full guard — no attack).

When a practitioner declares a Thread operation, their full Combat Pool is available for Defence. They cannot allocate Offence dice; their next offence is one full round away.

**Phase 3 — Resolution (simultaneous):** All pools are rolled simultaneously. Hits, damage, and consequences are calculated and applied simultaneously.

**Simultaneous damage:** If both combatants land hits, both take damage at the same moment. A combatant incapacitated by a simultaneous hit still has their own hit apply — the blow lands as they fall. This creates lethal exchanges where over-committing is genuinely dangerous.

## 3.4 Combat Pool Construction

**Combat Pool = Agility + weapon proficiency History (points + 3).**

Pre-calculate and record on the character sheet.

**Minimum Combat Pool:** 5 dice. Characters with a calculated pool below 5 receive 5 dice but roll at -1D effective (maximum 4 dice contribute to successes). This prevents the pool-split decision from becoming meaningless at low values.

**Modifiers to Combat Pool:**
- Wounds: no direct pool reduction (Wounds add +1 Ob to all rolls instead)
- Armour: no pool penalty (armour provides damage reduction only)
- Fibonacci group bonus: adds to Offence allocation specifically
- Terrain/zone: GM may impose +1 Ob for adverse terrain; does not reduce pool

## 3.5 Attack Resolution

**Offence dice** roll at **Weapon TN** (see §8.3).

**Defence dice** roll at **TN 7** (Dodge) or **Weapon Parry TN** (Parry — must be declared during Division phase).

**Hit determination:** Attacker's offence net successes vs. defender's defence net successes. If attack net > defence net: hit. Margin = excess attack successes used in damage calculation.

**Damage = Weapon Bonus + excess attack successes − Armour Rating** (minimum 0).

Strength does not add directly to damage. Accuracy (Agility via pool size) determines damage through excess successes. Weapons have a Strength minimum to wield (see §8.3).

## 3.6 Reach

Weapons fall into three reach categories:

| Reach | Examples |
|-------|---------|
| Short | Daggers, knives, unarmed, short swords, hand axes |
| Long | Longswords, spears, halberds, staves, greatswords |
| Projectile | Bows, crossbows, pistols, thrown weapons |

**Starting distance:** Combatants never begin at short melee range unless already standing side by side. Default starting distance is long range.

**Short vs Long at short range:** Short weapon has priority. Long weapon user must manoeuvre at disadvantage without being hit to re-establish long range.

**Long vs Short at long range:** Long weapon has priority. Short weapon user must manoeuvre at disadvantage without being hit to close to short range.

**Projectile range:** Melee weapons cannot attack back at projectile range. Projectile weapons cannot be used at short or long melee range. A character must successfully dodge the ranged weapon user's fire to close distance. Narrative spatial conditions apply (height, obstacles, cover).

**Reach advantage:** While the longer-reach combatant maintains appropriate distance, the shorter-reach combatant's offence dice are wasted unless they first perform a Close manoeuvre (see §8.6).

## 3.7 Zone-Based Positioning

TTRPG combat uses zones, not grids or maps. A zone is a narratively coherent area: "the courtyard," "the balcony," "the corridor." Maps are illustrative only; they are never tactical grids.

**Movement:** Moving within a zone is free. Moving between adjacent zones costs either the character's full action (pure movement — faster, arrives immediately) or can be combined with an attack (arrives at the new zone but acts at −1D to offence that round).

Movement has priority within a phase until an opponent has a combatant in weapon range. Once engaged, disengaging requires a Manoeuvre (see §8.6).

## 3.8 Wounds and Incapacitation

**Health = Endurance + 6.** Damage reduces Health.

When Health reaches 0:
1. Take a **Wound** (Health resets to full)
2. All subsequent rolls: **+1 Ob per Wound** (cumulative, all roll types)
3. Excess damage carries over into reset Health

**Single-hit cap:** No single hit inflicts more than 2 Wounds. Damage exceeding 3× Health is treated as 3× Health.

**Wound incapacitation thresholds:**

| Endurance | Incapacitated at |
|-----------|-----------------|
| 1–3 | 2 Wounds |
| 4–5 | 3 Wounds |
| 6–7 | 4 Wounds |

An incapacitated character is unconscious or otherwise unable to act. They are not dead unless the narrative demands it or a Coup de Grâce is performed.

## 3.9 Stamina and Recovery

**Stamina:** Equal to Endurance + 1. Decreases by 1 for every melee round in a row ehere a character has Moved, Manoeuvred or Attacked. Once Stamina reaches 0, the character must Catch Breath. A character may elect to take a Breather before Stamina reaches 0.

**Catch Breath:** A character's Combat Pool is divided by 2 (rounded up). They can only commit their Combat Pool to Defence Dice. Stamina is restored to full afterwards.

**Breather:** A character's Combat Pool can only be committed to Defence Dice. Stamina is restored to full afterwards.

**Quick Rest:** Between scenes (minutes to hours of downtime). Restores Health to maximum and removes 1 Wound.

**Full Rest:** Extended downtime (a full night's rest or equivalent). Restores all Health and removes all Wounds.

---

*End of Stage 1 compilation. Parts Four onward continue in subsequent stages.*




---



# PART FOUR: CHARACTERS

## 4.1 Histories

Histories replace skills. Each is a meaningful life chapter — lived experience, not a category. A History named "Mountaineer in the Löwenpass" is not interchangeable with "Alpine Guide" — the specificity of the experience matters narratively and mechanically.

Each History specifies a **primary attribute** (the attribute most relevant to that life experience).

**Pool = Primary Attribute + (History points + 3).** Pre-calculate and record on the character sheet.

**Starting Histories:** 3 Histories, each at 2 points. Players name and describe each during Session Zero.

**Per-History cap:** A History can never hold more points than the character's **Memory score**. This is the binding constraint — Memory limits how deeply experience consolidates into reliable capability.

**Social rolls:** Presence (for Appeal, Circles) or Cognition (for Debate, investigation) replaces the History's primary attribute as the base dice. History bonus dice (points + 3) are always added. If the social attribute equals the History's primary attribute, the total is unchanged.

**Fork Rule:** When a second History is relevant and the player narrates the connection, add **+1D per 3 full points** in the secondary History (minimum +1D if any points exist). Maximum one Fork per roll. Fork cannot be used when acting as Anchor in a collective operation.

*Example:* A character with "Einhir Scholar" (5 points) Forks into a Debate roll where their scholarship is relevant: +1D (3 points = +1D; 6 points = +2D). Their primary roll uses Cognition + Debate History bonus.

**Advancement (test track):** Mark *Challenged* when you succeed at Ob ≥ your raw primary attribute score. Mark *Exceeded* when you achieve Overwhelming at Ob ≥ your current History point total + 2. When both marks are filled: +1 point, clear marks.

## 4.2 Beliefs

Each character holds 2–3 Beliefs. A Belief is an active intention with a specific plan — not a passive value. "I believe in justice" is not a Belief. "I will expose the Church's role in the Harbour District murders" is.

| Belief Event | CP Earned |
|-------------|-----------|
| Pursuing a Belief in a meaningful scene | +1 |
| Belief challenged by events (player engages the challenge) | +1 |
| Belief achieved | +2 (rewrite the Belief) |
| Belief genuinely revised in response to events | +2 |

Beliefs drive the campaign. The GM builds situations that challenge, intersect with, and pressure Beliefs. A session where no Belief is tested is a session where the GM missed the mark.

A completed Belief may be converted to an Inspiration focus at 1 point (see §4.4).

## 4.3 Inspirations

Total Inspiration value ≤ **Spirit score**. Individual Inspirations rated 1–N; sum may not exceed Spirit.

Each Inspiration has a named **focus**: a person, place, ideal, or object that gives the character determination.

**Spend (value 1+, once per scene per Inspiration):** When the focus is relevant, roll Spirit score in bonus dice. Add results to pool normally.

**Stunt (value 2+):** Narrate connection to action. Add automatic successes equal to relevant attribute (no roll for those). Roll Spirit dice as bonus (chain on 10). Roll remaining pool normally. Stunt auto-successes replace rolled dice for collective operations — helpers' contributed dice do not apply to a Stunt.

### Acquiring New Inspirations (Mid-Campaign)

1. Player declares intent and names the focus.
2. Two scenes where the character actively engages with the focus (GM confirms engagement is genuine).
3. After each scene: Spirit check TN 7, Ob 1.
   - Both succeed: Inspiration established at 1 point.
   - One succeeds, one fails: Inspiration established at 1 point, with a **Complication Tag** (GM assigns a narrative condition — e.g., "contingent on Lenneth's approval," "only while in Valorsplatz").
   - Both fail: Focus not yet crystallized. Player may retry next season with new scenes.
4. **CP shortcut:** 4 CP + one scene of genuine engagement + one Spirit check. On success: established at 1 point, no Complication Tag. On failure: 4 CP spent, retry next season.

An NPC whose Impression Track reaches 5 can become an Inspiration focus (connects the relationship system to the Inspiration economy).

### Recovery (from Reduced Value)

- Full scene engaged with the focus: +1 point. No roll required.
- If focus is physically present and uncontested: automatic +1, no roll.
- Maximum recovery per season: 2 points per Inspiration.

### Focus Destroyed or Permanently Lost

Inspiration drops to 0 immediately. The player may convert to a new Inspiration through a **Grief Scene**: one scene of genuine reckoning + Spirit check TN 7 Ob 2.

- Success: new Inspiration at the old value −1 (minimum 1). New focus must relate to the loss.
- Failure: Inspiration lost entirely. CP refunded at half value (round down).

[EDITORIAL: Half-CP refund on Grief failure confirmed in S4. Verify this is still intended.]

## 4.4 Thread Sensitivity (TS)

Hidden score, 0–100, tracked by the GM. Cannot be purchased. Grows only through held confrontation.

| TS Range | State | Capacity |
|----------|-------|----------|
| 0–9 | Inert | No Thread perception. Cannot Leap. |
| 10–29 | Dormant | Passive awareness; no Thread operations |
| 30–49 | Stirring | May Leap (requires Approach Training). Object/Personal scale. |
| 50–69 | Attuned | Full operations. Relational scale. |
| 70–89 | Sensitive | Structural scale. Past-Oriented Pulling. |
| 90–100 | Resonant | Full range. Involuntary Leap risk. |

### Passive Perception (Automatic)

| TS Range | Automatically Perceives |
|----------|------------------------|
| 10–29 | Wrongness near Gaps, Shifting Objects, Intelligibility 3- practitioners; source unidentifiable |
| 30–49 | Active Thread operations in the scene; dissolution residue at touch; Originary Locks when touched |
| 50–69 | Thread operations in the same building; residue in the room; Threadcut status; practitioner Intelligibility levels |
| 70–89 | Thread operations within a city block; thread-configuration of individuals; Originary Locks in the room |
| 90–100 | Thread operations across the district; significant operations → involuntary Leap risk (Focus check TN 7 Ob 1) |

### TS Growth

Through **held confrontation** only. Qualifying events: surviving a monstrous incursion, handling an Originary Lock, witnessing a Gap, entering a Locked Zone, extended proximity to a Resonant practitioner.

On qualifying event: **Spirit check + relevant Belief bonus (if applicable), TN 7, Ob 1.**

- Success: character holds the confrontation. **+5 TS.**
- Failure: character represses. No growth. GM notes the event; the next encounter of equal or lesser intensity fires automatically (the repression breaks).
- Fleeing before completion: no check, no growth.

### Approach Training

Required to perform the Leap. Cannot be purchased directly.

**Acquisition paths:**

1. **Mentorship:** TS 50+ practitioner spends a full season with a TS 30+ character who has held at least one confrontation and witnessed at least one operation.
2. **Spontaneous Breakthrough:** During a Discovery Event where TS reaches 30+, make additional Spirit check TN 7 Ob 2. Success: Approach Training acquired simultaneously.
3. **Einhir Texts:** A character with TS 30+ studies a relevant primary text for a full season. Cognition + Memory (Ob 3). Success: Approach Training. Overwhelming: Approach Training + +1 thread-knowledge.
4. **CP purchase:** 8 CP. Requires TS ≥ 30, having witnessed ≥1 Thread operation, and narrating the training. Does not bypass the TS threshold — the character must already perceive Threads.

### The Devout Constraint

A character with an active essentialist theological Belief (Church doctrine, fixed divine determinism) cannot attempt TS growth checks — the Belief forecloses the perceptual stance required. Discovery Events bypass this for the initial check (the experience is involuntary).

After a Devout character's successful Discovery Event: immediate **Theological Dissonance Event** (Spirit check TN 7 Ob 1):
- Success: framework holds. Constraint re-engages. Certainty −1.
- Failure: framework cracks. Character gains a *Dissonance Mark*. Certainty −2.

At 3 Dissonance Marks: Devout Constraint collapses regardless of Belief status. Belief must be revised or lost.

**Devout characters receive +2D on Certainty-resist checks against monstrous encounters.** Their theology provides a framework that reduces existential shock, even if that framework is wrong about causation. However, Devout characters cannot gain long-term TS development from such encounters (the theological framework absorbs the confrontation).

### Scholarly TS Path (Lenneth Variant)

A character with access to Einhir scholarship and no essentialist theological Belief may pursue TS growth through sustained intellectual engagement with Thread-related texts and artifacts. This functions identically to the standard confrontation path, except the qualifying events are scholarly rather than experiential: deep study of Thread-operation records, analysis of temporal anomalies, decoding Originary inscriptions.

The Spirit check is still required — intellectual understanding alone does not produce sensitivity. The scholar must risk genuine perceptual shift.

## 4.5 Intelligibility

Intelligibility replaces the Coherence track. It measures how legible reality remains to a character engaged in Thread operations. Range: 10 (fully coherent) to 0 (reality unreadable).

**Starting value:** 10 (all characters).

**Reduction triggers:**
- Each Thread operation at Relational+ scale: −1 Intelligibility
- Past-Oriented Pulling: −1 Intelligibility (additional, cumulative with operation cost)
- Forced Resolution (any scale): −1 Intelligibility
- Extended proximity to a Structural-scale Gap: −1 Intelligibility per season of exposure

**Effects by Intelligibility level:**

| Intelligibility | State | Effect |
|-----------------|-------|--------|
| 10–8 | Coherent | No penalty. Reality legible. |
| 7–5 | Strained | Occasional perceptual slippage. Non-practitioners in Close Knots begin sensing wrongness. |
| 4–3 | Fragmented | −1D to all social rolls (difficulty maintaining normal presentation). Close Knots at wrongness threshold. Regular Knots begin sensing wrongness. |
| 2–1 | Fractured | −2D to all social rolls. All Knots at wrongness threshold. Involuntary perceptual events (GM describes Thread-level reality bleeding through). |
| 0 | Illegible | Reality as commonly rendered is no longer accessible to the character. Permanent condition unless reversed through specific Thread intervention. Character becomes an NPC unless reversed. |

**Recovery:** Intelligibility does not recover passively. Recovery requires:
- Full season of non-practice (no Thread operations): +1 Intelligibility
- A Close Knot voluntarily anchoring the practitioner through a dedicated Anchoring Scene (Bonds check TN 7, Ob 2): +1 Intelligibility (costs the Knot +1 strain)
- Certain Einhir techniques (GM discretion, late-campaign): +1–2 Intelligibility

**Knot strain from Intelligibility:** Replaces the Coherence strain accumulation from prior editions.
- Intelligibility 7–5: +1 strain to all Knots per 3 sessions
- Intelligibility 4–3: +1 strain to all Knots per 2 sessions
- Intelligibility 2–1: +1 strain to all Knots per session

## 4.6 Certainty

**All characters track Certainty.** Starting value = Spirit score. Maximum = Spirit score.

**Certainty loss triggers:**
- Successful Leap: −1
- Non-consensual Thread work on sentient being: −1
- Witnessing a monstrous entity: −1 (Spirit check TN 7 Ob 1 to resist; Devout characters: +2D to this check)
- Intelligibility reaching 4 or below: −1 to Certainty maximum per Intelligibility level below 5

**Certainty 0 — Rendering Crisis:** A scene event, not a passive state. The character's rendering of reality has become unstable. They must resolve the dissonance narratively: revise a Belief, withdraw from Thread-active situations, or find a new framework for what they have experienced. Rendering Crisis is the primary mechanism for character development in practitioners.

**Certainty recovery:**
- Full season of non-practice and stable relationships: +1 (max Spirit)
- Belief achievement that reaffirms worldview: +1
- Certainty cannot be purchased with CP

## 4.7 Knots — Relational Bonds

Each character tracks up to **Bonds score** significant Knots. Established at creation (minimum 3, maximum = Bonds); develop through play.

**Knot types by closeness:**

| Type | Wrongness Threshold | Crisis Threshold | Examples |
|------|---------------------|------------------|----------|
| Close | 3 strain | 6 strain | Family, sworn ally, beloved |
| Regular | 5 strain | 10 strain | Colleague, community member, mentor |
| Distant | 8 strain | 16 strain | Institutional, place, ancestral |

**Wrongness:** When strain reaches the wrongness threshold, the connected entity begins perceiving something is off about the character. The nature of the wrongness depends on the source: Intelligibility strain manifests as uncanniness; social strain manifests as emotional distance; Thread-related strain manifests as inexplicable dread.

**Crisis:** When strain reaches double the wrongness threshold (Crisis threshold), the relationship enters Crisis. A Crisis Knot cannot be Called or used as Composure buffer. The connected entity takes action — confrontation, departure, or betrayal. Resolution requires a dedicated scene.

### Strain Sources

- **Intelligibility decay:** See §4.5 (replaces Coherence strain).
- **Composure buffer:** When absorbing Composure strain through a Knot (see §9), +1 strain per use.
- **Call a Knot:** +2 strain per use (see below).
- **External events:** Territory conquest affecting the Knot's entity, faction collapse, Thread operations targeting the entity.

### Call a Knot

When making any roll related to a Knot's relationship, the character may Call the Knot: spend +2 strain to gain **+3D** on the roll. The character draws on the relationship's emotional weight — and damages it in the process.

A Knot at or above its wrongness threshold may still be Called (at significant narrative cost). A Knot in Crisis cannot be Called.

### Strain Recovery

- Close: −1 strain per season of active, positive engagement
- Regular: −1 strain per 2 seasons
- Distant: −1 strain per 4 seasons

Recovery requires the relationship to be actively maintained. A Knot ignored during recovery does not heal.

### New Knots

New Knots may be declared mid-campaign when a relationship reaches sufficient significance (GM judgment). If the character already has Bonds-score Knots, one existing Knot must be demoted to narrative-only status (no longer tracked mechanically).

Establishing a new Knot via CP: 2 CP. Formalizes a relationship the player wants tracked.

## 4.8 Circles

Circles represents the character's social network — the people they can find when they need help, information, or services.

**Pool:** Presence + highest applicable History bonus. The History must connect to the social sphere being accessed. "Court Connections" gives full bonus for Crown/Church circles; "Street Network" gives full bonus for Guilds/Revolution/Niflhel circles. A History that doesn't connect to the target faction provides no bonus — raw Presence only.

**TN:** 7. **Ob:**

| Ob | Contact Type |
|----|-------------|
| 1 | Common; widely known in the community |
| 2 | Specialists; moderately connected individuals |
| 3 | Secretive; criminal networks; underground contacts |
| 4 | Intelligence assets; Church inner circle; faction leadership |
| 5+ | Resonant practitioners; inner tradition keepers; Einhir scholars |

**Faction linkage:** Each Circles roll is implicitly or explicitly within a faction's social sphere. Positive Reputation with that faction: +1D per 2 Reputation points. Negative Reputation: −1D per 2 Reputation points.

| Degree | Result |
|--------|--------|
| Overwhelming | Contact found; immediately useful; becomes potential Knot |
| Success | Contact found with one relevant capability or piece of information |
| Partial | Contact exists but wants something, is compromised, or unreliable |
| Failure | No contact; someone is actively preventing the connection |

**Network Damage:** When a Circles contact is burned (betrays, is killed, is exposed through your actions), mark one Network Damage within that faction. At 3 Network Damage within a faction: −1D permanent to Circles within that faction. Network Damage clears at rate of 1 per season of non-hostile activity within that faction.

**Advancement:** Test-track system, tracked per-faction. Each faction's Circles advances independently through use.

**CP purchase:** 4 CP for +1D permanent (max bonus = Presence score). Represents deliberately expanding your social network.

## 4.9 Resources

Resources represents the character's economic capacity — wealth, access to goods, ability to procure through whatever channels available.

**Pool:** Presence + highest applicable History bonus. "Merchant Guild Member" → full bonus. "Soldier" → no bonus for economic transactions.

**TN:** 7. **Ob:**

| Ob | Scale |
|----|-------|
| 1 | Night's stay, common supplies, basic equipment |
| 2 | Quality equipment, minor official bribe, hiring labour |
| 3 | Significant bribe, hiring a professional, quality armour |
| 4 | Major investment, bribing a Church official, funding an expedition |
| 5 | Mercenary company, funding a covert operation, major property |

**Faction linkage:** Faction leaders may roll faction Wealth instead of personal Resources for faction-appropriate expenditure. Non-leaders may access faction Resources at +1 Ob if they have positive Reputation with the faction.

**Tax (degradation on failed rolls):**
- Partial at any Ob: −1D to next Resources roll this season (temporary strain).
- Failure at Ob 3+: −1D permanent until recovered.
- Failure at Ob 5: −2D permanent. Economic standing seriously damaged.

**Recovery:** One successful Resources roll at Ob ≤ 2 during seasonal accounting restores 1 lost die. Alternatively: a full season of commerce-focused activity (no other Domain Actions) restores all lost dice.

**External degradation:** Territory conquered → all characters with Resources tied to that territory lose 1D permanent. Faction collapse → all characters with Resources tied to that faction lose 2D permanent.

**CP purchase:** 4 CP for +1D permanent (max bonus = Presence score). Represents improving economic standing.

## 4.10 Advancement — CP Spending Menu

Character Points (CP) are earned through Belief engagement (§4.2) and spent on character improvement.

| Purchase | Cost | Constraint |
|----------|------|-----------|
| Attribute +1 | Current score × 3 CP | Max 7 per attribute |
| History +1 (beyond test track) | 3 CP | Cap = Memory score |
| New History at 0 points | 5 CP | Must narrate origin scene; requires GM scene |
| New Inspiration at 1 point | 4 CP | Total Inspiration ≤ Spirit; must name focus + one engagement scene + Spirit check |
| Inspiration +1 point | 3 CP | Individual cap = Spirit; total ≤ Spirit |
| New Knot (establish) | 2 CP | Total significant Knots ≤ Bonds score |
| Knot +1 strain capacity | 3 CP | Max strain capacity per Knot = 5 above base threshold |
| Circles +1D (permanent) | 4 CP | Max bonus = Presence score |
| Resources +1D (permanent) | 4 CP | Max bonus = Presence score |
| Remove 1 Wound | 6 CP | Between seasons only; requires narrative (healer, rest, Thread intervention) |
| Approach Training | 8 CP | TS ≥ 30; must have witnessed ≥1 Thread operation; replaces mentorship/breakthrough paths |

**Design constraints:**
- All purchases have narrative requirements — CP alone is never sufficient.
- No CP purchase for TS growth, Intelligibility recovery, or Certainty recovery. These are play-driven.
- CP costs scale: cheap (2–3) for relationship/social investment, moderate (4–5) for capability expansion, expensive (6–8) for recovery and rare unlocks.

## 4.11 Composure and Social Damage

**Composure = Presence + 6.** Social damage (from Debates, Appeals, public humiliation, Thread-related social strain) reduces Composure.

When Composure reaches 0:
1. Character becomes **Rattled** (Composure resets to full).
2. All subsequent social rolls: +1 Ob per Rattled level (cumulative).
3. Excess damage carries over.

**Rattled incapacitation:** At 2 Rattled marks, the character is socially incapacitated — they cannot participate in formal social scenes (Debates, Appeals) until recovered. Informal conversation is still possible.

**Composure Recovery:**
- Scene change (new location, new interlocutors): restores Composure to maximum.
- Rattled: clears 1 mark per full scene of non-social activity or rest.
- Knot as Composure buffer: redirect Composure damage to a Knot (+1 strain per use). Prevents Rattled but accelerates Knot decay.

---

*End of Stage 2 compilation. Part Five (Thread Operations) continues in Stage 3.*




---



# PART FIVE: THREAD OPERATIONS

Thread operations are how practitioners interact with the constitutive ground of being. Every operation produces consequences across all three dimensions — actual, temporal, and epistemic — simultaneously. This is the inseparability principle at work: you cannot touch one dimension without moving the others.

## 5.1 Approach Training

A character with TS 30+ may undertake Approach Training as a downtime arc: one full campaign season devoted to learning how to initiate and sustain contact. During this season the character is unavailable for Domain Actions and military service but may participate in scenes.

At season's end, the character gains the **Approach Training** tag permanently. This is not a roll — it is a narrative commitment confirmed at seasonal accounting.

## 5.2 The Leap — Entering Contact

The Leap is the practitioner's transition from ordinary perception to Thread contact. It is always risky, always costly, and never routine.

### Eligibility (verify before rolling)

- Approach Training tag ✓
- TS 30+ ✓
- TT ≥ 20 ✓
- Not currently engaged in melee with an opponent who has declared an attack this round ✓
- Not at or above incapacitation Wound threshold ✓

The Leap is a **full-round action (Priority 5)**. No attack, no movement, no manoeuvres in the same round. Only defence available: Parry or Dodge Backwards (character's choice when declaring).

### The Leap Roll

**Pool:** Attunement + relevant History bonus (e.g., "Einhir Scholar": points + 3)
**TN:** 7
**Ob:** TS 30–49 = 2 · TS 50+ = 1 · +1 Ob per Wound

Pre-calculate the Leap pool on the character sheet as a named entry separate from History pools.

| Degree | Outcome |
|---|---|
| Overwhelming | Clean contact. Next Operation's Ob reduced by 1 (minimum 1). Practitioner gains 1 TS. |
| Success | Contact achieved. Proceed to operation. |
| Partial | Unstable contact. Operation Ob +1. Take 2 Composure strain. |
| Failure | Rendering snaps back. Take 4 Composure strain. Rattled for the scene. No Thread operation this scene. |

**Overwhelming cascade:** The Ob reduction applies only to the immediately following operation. If the operation is already at Ob 1, the reduction has no further mechanical effect but the TS gain still fires. This cascade is exclusive to Thread operations.

### The First Leap (Event Scene)

The first time a character attempts the Leap, it is run as a full event scene rather than a standard roll. The GM describes the approach and the perceptual limit phenomenologically. On success: TS score is revealed to the player; Practitioner designation granted. On failure: **Dissociation** — the character is present in the world and can participate in scenes for one season, but cannot attempt Thread operations and their TS is frozen. They may attempt again next season.

### Contact Duration

Once the Leap succeeds, contact is maintained automatically for a number of rounds equal to the practitioner's **Focus score**. The Leap round itself counts as Round 1. At Round (Focus + 1), contact drops naturally.

The window is time-based — it counts down whether or not the practitioner acts within it.

Standard sequence (Focus 3 or more):
- Round 1: Leap (Priority 5) — contact established
- Round 2: Diagnosis (Priority 4, free, does not shorten window)
- Round 3: Operation (Priority 4 or 5)

At Focus 2: only Rounds 1 and 2 are covered — Diagnosis is possible but the operation requires re-Leaping.

**Wound disruption during maintained contact:** When the practitioner takes a Wound while contact is established, make a Focus check immediately: Focus score in d10s, TN 7, Ob 1. Failure: contact drops. Damage that does not produce a Wound does not trigger this check.

### Thread Operation Visibility

Operations are invisible to characters with TS 0–9. Detection by tier:

| Observer TS | Perception |
|---|---|
| 0–9 | Nothing perceived |
| 10–29 | Vague unease; cannot locate source |
| 30–49 | Senses an operation in the scene; general direction identifiable |
| 50–69 | Identifies operation type and approximate target |
| 70+ | Perceives the full configuration being worked |

Physical effects (a wound closing, an object moving) are visible to all.

**Concealing from TS 30+ observers:** Roll Cognition only (no History), TN 7, Ob = observer's TS ÷ 30 (round up). Success: reads as ambient Thread background. Failure: observer identifies the practitioner as source and operation type.

**CE note:** An active Thread operation performed *on* an observer counts as +2 CE — the most intense form of exposure.

### Wound Penalties and Thread Operations

The +1 Ob per Wound penalty applies to all Thread operation rolls — Leap, Weaving, Pulling, and Forced Resolution. A practitioner with 2 Wounds faces +2 Ob on every operation, applied before scale Ob. Combat-wounded practitioners are significantly compromised in Thread work.

## 5.3 Diagnosis

Spend one contact round sensing a target's thread configuration. **No roll** — this is a structured GM exchange.

**Timing:** Priority 4 standard action, Round N+1 or later after a successful Leap. Diagnosis is free — it does not shorten the contact window.

The practitioner states what they are sensing. The GM describes:
- How tight or loose the actualization is (sets Operation Ob)
- Whether threads have been previously worked (residue of prior operations)
- Whether a Gap is forming (critical safety information)
- Coherence trace, if the configuration has been touched by a transforming practitioner
- For past-oriented operations: the temporal weight of the configuration

**Mandatory before Forced Resolution.** Skipping Diagnosis before FR: +2 Ob and automatic Gap creation on Failure regardless of degree.

**Mandatory before Past-Oriented Pulling.** Skipping Diagnosis before Past-Oriented Pulling: +3 Ob and a temporal Gap rather than a standard Gap on Failure.

**Diagnosis on monstrous entities** reveals: mode, approximate Health, configuration type (useful for FR targeting).

## 5.4 Weaving — Things Cohere

**Foregrounded dimensions:** Actuality toward coherence; temporality toward persistence. Things cohere, connect, stabilise. Effects are potentially permanent. Healing through Weaving accelerates natural temporal progression — the wound resolves as it would, but faster. Scars are real; the world is consistent. No paradox.

**Requirements:** TS 30+ · Approach Training tag
**Pool:** Spirit + relevant History bonus
**TN:** 7

Pre-calculate the Weaving pool on the character sheet.

**Ob by scale (TS minimum required):**

| Scale | Example | Ob | Min TS |
|---|---|---|---|
| Object | Close a wound; reinforce a cracking blade | 1 | 30+ |
| Personal | Stabilise a dying character; accelerate injury healing | 2 | 30+ |
| Relational | Bind a diplomatic agreement; reinforce trust | 3 | 50+ |
| Territorial | Raise a faction's Stability by 1; stabilise a Shifting Object region | 4 | 50+ |
| Structural | Permanent reinforcement of a fortification, institution, or law | 5 | 70+ |

A practitioner below the required TS cannot attempt that scale — they cannot individuate those configurations as distinct threads.

| Degree | Outcome |
|---|---|
| Overwhelming | Full effect. TT −1 (Relational scale or above only). Practitioner gains 1 TS. The effect exceeds the stated goal — a wound closes without scarring; a bound agreement develops genuine trust beyond its terms. |
| Success | Full effect. TT unchanged. |
| Partial | Partial effect (GM sets scope). TT +1. ThS −1. |
| Failure | Weave collapses. TT +2. ThS −1. At TT ≥ 60: Shifting Object forms. At TT ≥ 80: Gap opens. |

**Partial Health restoration:** Weaving at Personal scale or above can restore Health that has not yet triggered a Wound. On Success: restore up to 4 lost Health points (does not heal Wounds). On Overwhelming: restore full Health and heal 1 Wound.

**Temporal Weaving (TS 50+):** When healing, the practitioner may foreground the temporal dimension — accelerating the wound's natural healing rather than altering its configuration. The healed state is more stable and persistent than natural healing would produce.

**Overweaving:** Each Weaving after the first in the same scene: +1 Ob (cumulative). A collapsed overweaved configuration: TT +3 and a local Shifting Object may form. For Overweaving purposes, "same scene" means the same dramatic unit — from scene establishment to conclusion. A Register Shift does not reset the Overweaving counter.

### Representative Weaving Examples

**W-01 Wound Closure** (Object, Ob 1): Temporal acceleration — the wound resolves as it would naturally, but now.
**W-02 Blade Reinforcement** (Object, Ob 1): Object threads drawn toward structural coherence.
**W-03 Binding Word** (Relational, Ob 3): Agreement threads woven; breaking it creates a local rendering failure.
**W-04 Territorial Calm** (Territorial, Ob 4): Regional thread-configuration stabilised for a season.
**W-05 The Locked Archive** (Structural, Ob 5): Building's integrity woven so knowledge persists even if material form is destroyed.
**W-06 Dissolving a Monstrous Configuration** (Ob 3–5): Entity destroyed; Gap partially closed.
**W-07 Rekindling** (Personal, Ob 2): Restores Composure strain and may replenish an Inspiration.

## 5.5 Pulling — Things Open

**Foregrounded dimensions:** Actuality toward potential; temporality toward loosening. Draws a thread toward potential — loosens what is fixed, opens what is closed. Effects are inherently temporary: pulled threads re-actualise to their natural configuration.

**Requirements:** TS 30+
**Pool:** Spirit + relevant History bonus
**TN:** 7

Pre-calculate the Pulling pool on the character sheet.

**Ob by actualization level (TS minimum required):**

| Actualization | Example | Ob | Min TS |
|---|---|---|---|
| Loosely actualised | Thread already drifting; minimal resistance | 1 | 30+ |
| Normally actualised | Standard state; typical target | 2 | 30+ |
| Firmly actualised | Strong configuration; deliberate or old | 3 | 50+ |
| Previously Woven | Another practitioner's work resists | 4 | 50+ |
| Foundational | Deep structural thread; institutional or geological | 5 | 70+ |

**Duration by surplus successes beyond Ob:**
- 0 surplus: end of scene
- 1 surplus: end of session
- 2+ surplus: until next seasonal accounting

**Natural expiry:** When a Pull's duration expires, the thread re-actualises without consequence — no TT change, no Wound, no notification. The effect simply ends.

**Uncontrolled snap-back** (from Failure or contact loss during Pull): 1 Wound (armour does not apply) + TT +2.

| Degree | Outcome |
|---|---|
| Overwhelming | Full effect. Extended duration. TT unchanged. |
| Success | Full effect. Standard duration. TT unchanged. |
| Partial | Partial effect or reduced duration. TT +1. ThS −1. |
| Failure | Snap-back. 1 Wound (no armour). TT +2. ThS −1. |

**Perception Pulling:** Targeting a character's awareness/perception removes their defensive action for one round.

### Representative Pulling Examples

**P-01 Unlock** (Object, Ob 1): Lock's threads loosened; mechanism opens.
**P-02 Attention Diversion** (Personal, Ob 2): Target's awareness loosened; removes defensive action for one round.
**P-03 Dissolving Conviction** (Personal Firm, Ob 3): Held belief loosened; target becomes open to revision.
**P-04 Loosening the Crowd** (Territorial, Ob 3): Collective momentum pulled toward potential; unit Cohesion checks at +1 Ob.
**P-05 Opening the Wound** (Personal, Ob 2): Reversed healing; inflicts 1 Wound (bypasses armour).
**P-06 Memory Dissolution** (Personal Firm, Ob 3–4): Specific memory loosened; content becomes uncertain.
**P-07 Thinning the Veil** (Relational, Ob 3): Rendering surface thinned; non-sensitive characters experience rendering failures; Thread-locked objects revealed.
**P-08 Temporal Shimmer** (Past-Oriented, Object, Ob 3): Burned letter readable; broken object briefly whole; window into prior configuration.

## 5.6 Past-Oriented Pulling

**Foregrounded dimension:** Temporality toward the past — drawing a thread back so a prior event never fully actualised. This produces a **Temporal Disjunction**: physical facts are removed, but memories remain intact. The past event "never fully actualised" but everyone who experienced it retains the memory.

**Requirements:** TS 70+ · TT ≥ 40 · Diagnosis mandatory
**Pool:** Spirit + relevant History bonus
**TN:** 7

**Ob by recency:**

| Recency | Ob |
|---|---|
| Same scene (within last round) | 3 |
| Same session | 4 |
| Same week | 5 |
| Same season | 6 |
| Prior seasons | 7+ (escalates) |

**TT:** +3 minimum regardless of degree.
**ThS:** Automatic +3 additional (on top of any other ThS costs).

**Co-Movement:** Past-Oriented Pulling produces secondary consequences in *both* remaining dimensions. The GM determines consequences for the actual and epistemic dimensions — not just one.

**The Fraying Bane:** A practitioner who performs Past-Oriented Pulling (or FR Dissolution) three or more times in one season gains the Fraying bane. Effects drawn from the Fraying table (see §5.8).

## 5.7 Forced Resolution — Collapse to One Pole

FR collapses a thread entirely to one of its two poles. **Lock** drives it toward full actualization — permanent, unchangeable. **Dissolution** drives it toward the unintelligible pole — the thread's contribution to the rendered world dissolves. Both are irreversible without directly addressing the same thread. Both are catastrophic at scale.

**Requirements:** TS 50+ · Diagnosis immediately preceding (mandatory)
**Pool:** Spirit + relevant History bonus
**TN:** 7
**Minimum Ob:** 4 regardless of target

Pre-calculate the FR pool on the character sheet. It uses the same formula as the Weaving pool.

**Declare direction before rolling:** Lock or Dissolution.

**Ob by scale (TS 50+ required for all FR):**

| Scale | Ob |
|---|---|
| Object | 4 |
| Personal | 5 |
| Relational / Process | 6 |
| Territorial | 7 |
| Structural / Foundational | 8+ |

**FR is a full-round action (Priority 5)**. The practitioner commits entirely to the collapse.

**TS 70+ Tier Reduction:** Sensitive and Resonant practitioners reduce all FR TT costs by 1 (minimum 1). This does not apply to ThS costs.

### Lock Results

| Degree | Outcome |
|---|---|
| Overwhelming | Target permanently locked. TT +2. Practitioner gains 1 TS. |
| Success | Target locked. TT +2. |
| Partial | Partial lock (GM sets scope). TT +3. ThS −2. |
| Failure | Collapse onto practitioner. Take 2 Wounds (armour does not apply). TT +4. ThS −2. |

### Dissolution Results

| Degree | Outcome |
|---|---|
| Overwhelming | Target dissolves cleanly. TT +3. Micro-Gap forms and closes within the scene. |
| Success | Target dissolves. TT +5. Gap forms, lasts one scene, closes. |
| Partial | Target becomes a Shifting Object. TT +6. Gap does not close without Weaving. ThS −2. |
| Failure | Full Gap tears open. TT +8. Monstrous Incursion occurs immediately. Practitioner is Incapacitated. ThS −2. |

### Representative FR Examples

**FR-L-01 The Permanent Lock** (Object, Ob 4): Gate permanently open or closed. Wound locked as permanent scar.
**FR-L-02 Sealing a Mind** (Personal, Ob 5): Thread sensitivity sealed; conviction made unrevise-able; injury effects permanent.
**FR-L-03 The Locked Institution** (Structural, Ob 8+): Fundamental law permanently embedded; institution incapable of reform.
**FR-D-01 Dissolution of Evidence** (Object, Ob 4): Document ceases to exist as a coherent thing.
**FR-D-02 Dissolving a Wound** (Personal, Ob 5): Wound never actualized; safer than Weaving but catastrophic on failure.
**FR-D-03 Dissolving a Relationship** (Relational, Ob 6): Alliance, loyalty, or debt ceases to exist as a configurational weight.
**FR-D-04 Unmaking** (Territorial, Ob 7): Territory loses configurational coherence; Fraying risk to practitioner.

### The Fraying Bane

A practitioner who performs FR Dissolution or Past-Oriented Pulling three or more times in one season gains the Fraying bane. While Fraying is active:
- All Thread operations: +1 Ob
- Contact duration reduced by 1 round (minimum 1)
- Partial results on any Thread operation produce involuntary micro-Gaps (TT +1 each)

Fraying clears at the end of a season in which the practitioner performs no FR Dissolution and no Past-Oriented Pulling.

## 5.8 Three-Dimensional Co-Movement (Version C)

Every Thread operation produces consequences across all three dimensions simultaneously. This is not optional — it is the inseparability principle expressed mechanically. The GM does not choose whether co-movement fires; it fires on every operation, every time.

Version C replaces the prior d12 Co-Movement Prompt Table with a deterministic system: two automatic effects (temporal and epistemic) plus one random actual effect (d6).

### Automatic Temporal Co-Movement

Fires on **every** operation. The temporal dimension always moves.

| Operation Type | Temporal Auto-Effect |
|---|---|
| Weaving (any degree) | ThS −1. The target's temporal axis compresses — the present contains a healed or stabilised version earlier than natural. Observers with TS 10+ perceive the target as "clearer" or "more vivid" for 1 scene. |
| Pulling (any degree) | ThS −1. The loosened thread's temporal anchoring frays. Any social roll citing the Pulled target as historical precedent: +1 Ob until publicly reaffirmed (R40). |
| FR Lock | ThS −2. The locked configuration's temporal axis freezes. No further temporal movement is possible for that thread — it exists in a permanent present. |
| FR Dissolution | ThS −2. The dissolved configuration leaves a temporal void. All present characters feel the present as denser — temporal weight redistributed across the scene. |
| Past-Oriented Pull | ThS −3 additional. The altered past creates an epistemic paradox for witnesses: anyone who remembers the original event retains both memories. The paradox is unresolvable without Thread-level understanding. |

### Automatic Epistemic Co-Movement

Fires on **every** operation. How things can be known changes.

| Operation Type | Epistemic Auto-Effect |
|---|---|
| Weaving (Success/Overwhelming) | Target becomes MORE intelligible — partially clarified. Observers with TS 10+ perceive the target as clearer for 1 scene. Non-sensitives may notice something but cannot articulate it. |
| Weaving (Partial/Failure) | Target becomes LESS intelligible — partially occluded from rendering. Testimony about the target: +1 Ob for 1 session. |
| Pulling (any degree) | The loosened thread becomes epistemically unstable. Witnesses disagree about details. Investigation or Circles rolls involving this target: +1 Ob until seasonal accounting (R39). |
| FR Lock | The locked configuration becomes opaque to further Thread perception. Diagnosis on this target: +2 Ob. The Lock seals the thread from epistemic access. |
| FR Dissolution | Epistemic void. Non-practitioners present experience "something is missing that should be here." **Certainty check** for all non-practitioners present: Spirit TN 7 Ob 1. Failure: Certainty −1. Cap: once per scene regardless of number of Dissolutions (R36). |
| Past-Oriented Pull | Witnesses who remember the original event retain both memories (the original and the altered). Inert Knowledge of the paradox forms: they know something is wrong but cannot determine what. |

**Stacking cap:** The epistemic investigation modifier (R39) and temporal precedent modifier (R40) do not stack on the same roll. Use the higher; effective cap is +1 Ob per roll from co-movement effects.

### Actual Co-Movement (d6)

The GM rolls d6 on every operation. This is the one random element in the co-movement system.

| d6 | Effect |
|---|---|
| 1 | Knot strain ±1 (target's or practitioner's — GM choice) |
| 2 | Nearby object enters partial potentiality (minor Shifting Object risk; self-corrects in 1d3 days unless area remains Thread-active) |
| 3 | Physical residue at operation site |
| 4 | Target's physical configuration overshoots intended scope |
| 5 | Environmental texture shifts (temperature, light, sound — detectable by TS 10+) |
| 6 | Delayed manifestation (1d3 scenes later) |

### History Resonance (R37)

When a Thread operation's temporal co-movement fires, the GM checks whether the practitioner has a History relevant to the operation's context. If yes: the History **resonates**.

Next use of that History: the practitioner rolls 1 bonus die (d10). This represents the accumulated past briefly amplifying the present. If the bonus die shows a **1**: ThS −1 (the temporal connection deepened the disjunction).

**Constraints:**
- Only one Resonance active per History at a time
- Resonance persists until discharged (the bonus die is rolled)
- History Resonance fires approximately 1–2 times per session at typical play rates
- Expected campaign ThS from Resonance: ~4–5 additional ThS over 30 sessions (mathematically minor but narratively persistent)

### Practitioner Flashback Temporal Anchoring (R38)

When a practitioner uses a Flashback (Inspiration spend to declare a retroactive scene), their Thread sensitivity means the retroactive declaration partially actualises the past scene. If the Flashback involves Thread-relevant content — locations with Thread history, people with TS 30+, Originary Locks, dissolution residue — the GM may rule: **ThS −1**.

This cost applies **only to practitioners**, not to non-practitioner Flashbacks. It is GM discretion, not automatic — mundane Flashbacks are unaffected.

## 5.9 Thread Stability (ThS) — 20 to 0

Thread Stability tracks the coherence of the practitioner's configuration relative to the world's rendered state. As a practitioner works threads, their own configuration becomes less stable across all three dimensions — intelligibility, actuality, and temporality. High Thread Stability means the practitioner's rendering is intact; low Thread Stability means it is fraying.

ThS is a **campaign-arc resource**, not a per-session meter. It starts at 20 and decreases across the campaign.

### ThS Loss

ThS decreases through Thread operations (from co-movement auto-effects), History Resonance risk dice, and practitioner Flashback anchoring. The primary sources:

| Source | ThS Loss |
|---|---|
| Object scale operation (any result) | +1 (from temporal auto-effect) |
| Personal scale (Success/Overwhelming) | +1 (from temporal auto-effect) |
| Personal scale (Partial/Failure) | +1 (auto-effect) + additional from degree table |
| Relational scale (any result) | +1 (auto-effect) + additional from degree table |
| Territorial scale (any result) | +1 (auto-effect) + additional from degree table |
| FR Lock or Dissolution | +2 (auto-effect) + additional from degree table |
| Past-Oriented Pull | +3 additional (on top of Pulling auto-effect) |
| History Resonance risk die (shows 1) | +1 |
| Practitioner Flashback anchoring | +1 (GM discretion; Thread-relevant content only) |

### Recovery

+2 ThS at the end of any season in which the practitioner's final session contained no Thread operations.

### ThS Thresholds and Fallout

| ThS | State | Effect |
|---|---|---|
| 20–16 | Dissonant | Narrative only — flickers of wrongness, momentary déjà vu, sense of events being slightly out of sequence. |
| 15–11 | Fragmented | Configuration unreliable. −1D to all Memory-based rolls. GM may present the character's recollection differently from what others remember. Roll Fragmented Fallout on entering this band. |
| 10–6 | Fractured | −2D to Memory-based rolls. Once per scene in which a Thread operation is performed: Spirit TN 7 Ob 1 or lose 1 round to a dissociative episode. Roll Fractured Fallout on entering this band. +1 Ob on all Thread operations. +1 Ob on testimony about Thread events. |
| 5–1 | Severed | −3D to Memory-based rolls. Dissociative episodes once per scene regardless of operations. |
| 0 | Crisis | Campaign event. The character must resolve the disjunction narratively — sustained engagement with the world's rendered state — or withdraw from practice until ThS rises above 5. |

**Fragmented Fallout (d6):**

1. You vividly remember a conversation others recall differently
2. A specific skill-memory requires Memory check Ob 2 to access correctly
3. Your sense of timing this scene is wrong — you feel you arrived at a different moment
4. Someone you have not seen recently feels as though you just spoke to them
5. Something you said this session feels like it was said last session
6. A Knot's emotional valence briefly reverses

**Fractured Fallout (d6):**

1. A vivid memory of an event the world no longer contains — you do not know it is orphaned
2. Your most recent History advancement feels uncertain — borrowed, not learned
3. A named Knot briefly does not recognise you, or vice versa. Lasts one scene.
4. You perform an action you do not remember. GM describes the gap.
5. Your Inspiration refresh this scene feels already spent
6. A Belief reads, briefly, as belonging to someone else

## 5.10 Transformation and Epistemic Seduction — Coherence Track

Dissolution residue use reduces Coherence. Transformation is a **perceptual shift**, not a corruption mechanic. The character's sense of what is real and normatively binding changes — this is epistemic seduction, not moral decay.

*Coherence track: individual, 10 (fully coherent) to 0 (monstrous configuration). Starts at 10.*

**Coherence loss:** −1 per use of dissolution residue (declared before rolling). Maximum one use per contact window. Subsequent uses from the same source: +1 Ob per prior use (residue depletion).

| Coherence | Effect |
|---|---|
| 7–9 | +1D to Thread operations. Other practitioners with TS 50+ in the same scene sense the instability. Knot strain begins (+1 per 3 sessions per Knot). |
| 4–6 | +2D to Thread operations. −1D to social rolls. Rendering contingency increasingly perceptible. Distinctions between the intelligible and unintelligible soften. GM recontextualises one Knot to clinical "configuration" language. Knot strain pace increases to +1 per 2 sessions. |
| 2–3 | +3D to Thread operations. −2D to social rolls. NPCs react with unease. Character functions as minor monstrous presence — rendering strain for those in proximity. All Knots +1 strain per session. Maximum Certainty −1 per Coherence level below 4. **Belief co-authorship** (see below). |
| 1 | Character perceives the "human"/"monstrous" distinction as a rendering artifact. Corrective Weaving is possible but the character does not perceive it as desirable. Player chooses: accept correction (restore Coherence to 5, take 2 Wounds from reconfiguration) or continue. |
| 0 | Monstrous configuration. Character becomes NPC under GM control. All Knots receive final pulse of rendering strain. |

### Belief Co-Authorship (Coherence 7+)

GM presents the transformed perspective as the character's internal voice. Player must rewrite each Belief to reflect this perspective. GM veto: rewrites that do not authentically reflect the transformation. Player veto: rewrites that eliminate all character intentionality.

If agreement is unreachable within the scene: Belief marked **Contested** — cannot be pursued for CP until dramatised in a future scene where the tension between old and new perspective is explicit.

### Community Intervention

At Coherence 4–6: Corrective Weaving (Ob 3, another practitioner) restores Coherence by 1 per season.

Below Coherence 4: requires the transforming character's active cooperation — which epistemic seduction makes increasingly unlikely.

## 5.11 Dissolution Residue — Thread Materia

Objects carrying the ontological signature of monstrous configuration dissolution. Compressed potential oriented toward the unintelligible ground.

### Sources

Mode 1 dissolution (1 unit). Mode 2 dissolution (1d3 units). Entrenched Shifting Object edges (trace; TS 30+ passive at touch distance). Niflhel Southernmost operations. Failed FR sites.

### Handling

Non-practitioners: CE +1 per extended handling session. Practitioners: immediate passive perception of orientation (TS 30+).

### Using Residue as Power Source

A practitioner may draw on dissolution residue to power a Thread operation. Add bonus dice equal to the residue's Potency rating (1–5, GM-determined) to the operation pool. These bonus dice explode on **9–10** rather than 10 only — the compressed potential is volatile.

Declare before rolling. −1 Coherence per use. Maximum one use per contact window. Same source: +1 Ob per prior use (depletion).

### Storage and Detection

Lead-lined or thread-sealed containers preserve residue. Unstopped: inert after 1 season. Originary Locks function as natural seals.

Detection: TS 30+ passive at arm's reach. Inquisitors with CE 2+: feel wrongness near residue even without TS.

## 5.12 Thread-Locked Objects

### Category One — Intentional Locks

Objects a practitioner has performed FR Lock upon. They persist after the practitioner's death without maintenance. The quality of the Lock reflects the practitioner's capacity.

**Investigating an Intentional Lock (TS 50+, one full scene):** Diagnosis reveals the approximate TS of the creating practitioner (±10), whether the Lock was placed under duress or calmly, and a rough sense of when it was made (within a decade). This is practitioner forensics.

**Resistance to Pulling:** Ob = creating practitioner's TS ÷ 10 (round up). A Lock made by a TS 62 practitioner resists at Ob 7.

### Category Two — Originary Locks

Objects present at or interacted with during a monstrous entity's arrival, or at the moment of emergence from the unintelligible ground. Extraordinarily rare. The Church possesses several from Galbados's emergence.

**Properties:** Cannot be Pulled, Woven, or subjected to standard FR. They can be sensed, Diagnosed, and held, but not worked.

**Handling an Originary Lock (TS 50+ required):** When a practitioner handles an Originary Lock for one full scene, they receive a revelation experience: +10 TS gain immediately, plus a Spirit check (TN 8, Ob = current Wounds + 1) or take 2 Wounds (armour does not apply). The experience is permanent and cannot be unfelt. A practitioner who has handled an Originary Lock from Galbados's emergence has felt the shape of the third mode — the arriving that holds itself together.

### Category Three — Dissolution Residue

See §5.11.

## 5.13 Shifting Objects, Gaps, and Monstrous Entities

### Shifting Objects

Configuration that has partially escaped normal actualization — oscillating between presence, absence, and distortion.

**Trigger:** An object in a territory where multiple Thread operations have been performed, or where TT has been above 40 for 2+ seasons.

**Certainty cost:** −1 on first witnessing (Spirit check TN 7 Ob 1 to resist).

**Deterioration:** Worsens to Gap within 1d3 seasons without intervention. Dissolution residue forms at edges each season it persists.

**Stabilisation:** Weaving (Object scale, Ob 2) arrests deterioration. Overwhelming restores full actualization.

### Gaps

Wound in the rendered world's fabric.

**Certainty cost:** −1 per scene near a Gap (no Spirit check to resist).

**Thread operations within range:** +1 Ob (stacks with other penalties).

**Seasonal escalation:** Every season a Gap remains open: TT +4.

**Monstrous Incursion risk:** Start of each scene near a Gap, roll 1d10. On 1–2: Mode 1 incursion manifests.

**Closure by FR (Dissolution):**

| Gap Age | Scale | Ob |
|---|---|---|
| Micro-Gap (same scene) | Personal | 3 |
| Standard (1 session old) | Relational | 5 |
| Entrenched (1+ seasons) | Territorial | 6 |
| Catastrophic (3+ seasons) | Structural | 7; requires Einhir ritual framework |

**TT consequences when a Gap opens:**

| TT at Time of Gap | Consequence |
|---|---|
| Below 40 | A Shifting Object forms in the territory |
| 40–59 | A weak monstrous configuration |
| 60–79 | A full Monstrous entity |
| 80+ | A full Monstrous entity + a Shifting Object in each adjacent territory |

### Monstrous Entities

Immune to social influence. Physical damage halved. Never rout.

**Territory effects:** −1 Stability per season; Thread operations +1 Ob.

**Mode 1 — Ordinary Incursion:** Health 6, Martial 3, Cohesion 1. No intelligence; disrupts what is nearest. Certainty −1 all in scene. −1 Health per round without attack (rendering refuses to sustain). Dissolves in 1d6 rounds; leaves dissolution residue.

**Mode 2 — Providence:** Health 10, Martial 4, Cohesion 3. Organised; apparent purpose. Certainty −1 all in scene. −1 Health per scene (slower). Resists Pulling (Ob +2). Leaves dissolution residue on dissolution.

**Mode 3 — Threadcut Being:** Varies; always has Threadcut tag. No deterioration while Thread work continues. Past-Oriented Pulling auto-produces a Gap. Wounds cost additional sustained Thread work rather than conventional incapacitation. Coherence track does not apply. Can communicate; may have comprehensible goals.

**Defeating monstrous entities:**
- Conventional combat: destroys current configuration. Gap persists. New configuration in 1d4 seasons.
- Weaving (TS 60+, Ob 4): destroys entity AND partially closes Gap (TT −2).
- FR Dissolution (Ob 4): destroys entity but creates second Gap on failure.

**Stabilised entities** (3+ seasons active): Health doubled, resistance increased; must be destroyed before Gap can be closed.

### Divine Providence

Cannot be triggered by practitioners. Represents genuine emergence from the unintelligible ground — not a Thread operation gone wrong. Practitioners with TS 50+ present at a Providence event feel it as profound settledness. This is the only mechanical evidence that the unintelligible pole may contain organised content.

## 5.14 Collective Thread Operations

When multiple practitioners work the same configuration, their threads knot into a lattice.

**Anchor:** Highest TS practitioner. Rolls their full operation pool.

**Helper contribution:** Each assisting practitioner contributes **floor(Cognition ÷ 2)** bonus dice to the Anchor's pool. Each helper must have maintained their own Leap and have an active contact window.

**Constraints:**
- Helpers cannot Fork; Anchor cannot Fork when acting as Anchor
- If a helper's contact drops before the roll: remove their contributed dice. If total pool drops below half the Anchor's solo pool: +1 Ob (lattice fracture)
- Conflicting Beliefs: dissenting participant's dice cannot chain on 10 — they contribute pool but prevent bonus cascades
- Stunt in collective operations: Anchor's auto-successes replace rolled dice; helpers' contributed dice do not apply to a Stunt

**Co-movement in collective operations:** Secondary consequences scale with participant count. A 4-practitioner lattice produces correspondingly significant co-movement effects across all three dimensions.

## 5.15 Threadcut and Organic Beings

**Organic beings** persist through continuous Ein Sof spooling — temporal depth accumulated through lived experience.

**Threadcut beings** maintain themselves through continuous Thread work. They radically *are* without *becoming*.

**Mechanical distinctions:**
- Past-Oriented Pulling against a threadcut being: auto-produces a Gap (no temporal thread to pull against)
- Wound effects: each Wound costs 1 additional point of sustained Thread work rather than the conventional incapacitation Ob penalty
- Coherence track does not apply to threadcut beings

## 5.16 Einhir Texts

Primary Einhir Texts are works in which Thread technique is encoded at the configurational level, not merely described in words.

A character with TS 30+ who reads a primary Einhir text: **+5 TS** (once per text). This also triggers TT +1 (dormant patterns activate in the area) and grants immediate Leap eligibility if Approach Training is already complete.

Each primary text teaches one **named Thread operation technique**: a specific effect that functions at +1D when used, beyond normal pool size. These techniques are specific and idiosyncratic.

Example techniques:
- **Binding** (Weaving) — draws two configurations into accord. +1D when Weaving to establish or reinforce social agreements, bonds of loyalty, or diplomatic arrangements.
- **Loosening** (Pulling) — progressive release of mechanical actualization with precision. +1D when Pulling to open physical locks, loosen restraints, or release captives.
- **Settledown** (Weaving) — targeted re-actualization of oscillating objects. +1D when Weaving to stabilise Shifting Objects specifically.
- **Clearseeing** (Pulling) — loosening of perceptual filters. +1D when Pulling to allow someone to perceive what their rendering has been suppressing.

GMs create techniques specific to each text's cultural origin and content. A technique should be narrowly scoped and feel like a practitioner's professional specialisation.

## 5.17 Co-Movement Quick Reference Card

For table use. Print or display during play.

**On EVERY Thread operation, apply all three:**

| Dimension | Source | How |
|---|---|---|
| Temporal | Automatic | Read from §5.8 temporal table by operation type. ThS always accumulates. |
| Epistemic | Automatic | Read from §5.8 epistemic table by operation type and degree. Investigation/testimony Ob modifiers apply. |
| Actual | Random (d6) | Roll on §5.8 actual table. One consequence per operation. |

**Then check:**
- History Resonance? (Relevant History → bonus die on next use; risk die on 1 = ThS −1)
- Practitioner Flashback this scene? (Thread-relevant content → ThS −1, GM discretion)

---

*End of Stage 3 compilation. Part Six (The Southernmost) continues in Stage 4.*




---



# PART SIX: THE SOUTHERNMOST

The Southernmost is the peninsula where the Einhir catastrophe occurred. Its Thread configurations have never recovered: three distinct zone-types persist from the collapse, each reflecting a different mode of configurational failure.

**Snapped zones**: Threads wound to maximum potential. Objects crumble on contact; configurations disrupt with proximity. Presence here is actively dangerous to physical integrity.

**Locked zones**: Threads frozen at the exact moment of catastrophe. Cities stand intact. Bodies are undecayed. The Einhir moment is preserved in amber. Most historically significant for research.

**Oscillating zones**: Threads cycling without rest — no stable actualization ever completing. Continuous Gap formation. The most dangerous zone-type and the most significant for practitioners seeking to understand the original wound.

---

## 6.1 The Forgetting

The Southernmost's danger cannot be rendered by those without Thread sensitivity. The rendering engine prioritises what it can process. The threads encoding the nature and scale of the danger are too close to the unintelligible ground to hold stable in consciousness — so they are simply not retained.

This is not a psychological defence or a failure of courage. It is a structural limitation of how consciousness renders experience. A non-practitioner who spends a day in the Southernmost will leave knowing they were somewhere hostile and strange. The specific knowledge — *what* it is, *why* it matters, *what* the stakes are — does not survive the return to ordinary rendering.

**Forgetting Check**: roll Cognition + Memory, TN 8.

| Exposure | Ob |
|---|---|
| Boundary zone (< 1 hour) | 1 |
| Interior (1–4 hours) | 2 |
| Deep interior (4+ hours) | 3 |
| Einhir core sites | 4 |

**TS modifier**: TS ÷ 20, rounded down, as bonus dice.

| Degree | Knowledge retained |
|---|---|
| Overwhelming | Full retention. TS 40+ retain ontological understanding (what the Southernmost *is*); others retain facts only (that it is dangerous, what was seen). |
| Success | Facts retained; threat context partially dissolved. The character knows what they observed; the weight of what it means fades. |
| Partial | Emotional impressions only. Dread, unease, urgency — without content. |
| Failure | Nothing operational. The character knows they were in a strange place and feels affected; cannot report anything actionable. |

Full understanding of the ontological nature of the threat — that it is a rendering failure, that the wound is in the constitutive ground, that it cannot be addressed through political or military means — requires TS 40+, even on an Overwhelming result.

**Momentum**: Momentum may be burned on Forgetting checks. (R17)

**Testimony Ob penalty**: Non-practitioners (TS below 40) using Southernmost knowledge in Appeals or Debates: +1 Ob for Boundary exposure, +2 Ob for Interior, +3 Ob for Deep Interior or Core. This penalty decreases as exposure depth increases — paradoxically, those who have spent more time in the Southernmost are more credible, because the Forgetting mechanism leaves emotional weight even when it strips content, and that weight reads as conviction.

---

## 6.2 Southernmost Awareness (Faction Stat)

Scale: 0–7 (where applicable) or 0–10 for factions with active research infrastructure.

Awareness represents the faction's institutional understanding of the Southernmost — not just that it exists, but what it is, what its configurations mean, and what intervention might require. Awareness advances through:

- Practitioner reports from successful expedition (Diagnosis results converted to Awareness points)
- Study of Einhir primary texts (each text: +1 Awareness, one-time)
- Diagnosis at Einhir core sites (requires expedition access; automatic for TS 50+, Ob 3 below)
- Dedicated research arcs by practitioner officers

**Starting Awareness by faction** (game start, 45 AG):

| Faction | Starting Awareness | Basis |
|---|---|---|
| Crown | 0 | No investment in Southernmost research |
| Church | 0 | Institutionally suppresses Einhir knowledge |
| Hafenmark | 1 | Maritime presence; traders have noted anomalies |
| Varfell | 2 | Road into the Southernmost; Maret Uln's presence |
| People's Revolution (NPC) | 3 | Highest Awareness of any NPC faction; ideological interest in the pre-Church world |

**Awareness floor**: Each faction has a permanent Awareness floor equal to the number of primary Einhir texts it holds. A faction holding the Ceiral Text cannot have Awareness drop below 1 while retaining that text, because the text itself preserves some comprehension independent of active research.

**Ceiral Ritual penalty**: Ceiral Ritual attempted without Awareness 5+: +2 Ob.

---

## 6.3 Expedition Procedures

Expeditions to the Southernmost are extended actions — the officer leading the expedition is unavailable for other Council Phase actions during any season they are engaged. The faction leader's two actions are independent and may be freely allocated regardless of officer expedition status.

### Prerequisites

- **TT ≥ 40**: The Southernmost is dormant below this threshold. Thread configurations are insufficiently active to diagnose or engage. Expedition at lower TT is possible but yields nothing actionable.
- **Practitioner officer, TS 30+**: Required to perceive Thread structures at all.
- **Relevant History**: Einhir Scholar, Natural Philosophy, or Expedition Leader. Expedition planning roll: Ob 3. On failure: expedition departs unprepared (+1 Ob to all zone checks Season 2 onward).
- **Resources**: Ob 3 for expedition supplies (hostile terrain, multi-season commitment).
- **Military escort**: Recommended. At least 1 unit. The Southernmost contains hostile configurations; escort provides combat options if encounter resolution requires mass combat scale.

### Expedition Structure (Multi-Season Extended Action)

| Season | Phase | Procedure |
|---|---|---|
| 1 | Approach | Travel to Southernmost border territory. Military escort (if present): Cohesion check Ob 1 (Thread proximity unsettles troops; failure = escort −1 Cohesion for the expedition). Practitioner with TS 30+: automatic Discovery Event — the lead practitioner perceives Thread anomalies at the boundary; first Forgetting Check fires here. |
| 2 | Exploration | Enter the Southernmost proper. Zone-based traversal: three zones to cross to reach the primary site. Each zone: one encounter (Thread phenomenon, hostile entity, or environmental hazard — see §6.4). Resolution per combat rules or Thread operation rules as appropriate. |
| 3 | Discovery | Reach the primary site (the locus of the original Einhir catastrophe). Practitioner TS 50+: Diagnosis fires automatically — the nature of the damage is fully apparent. Below TS 50: Diagnosis Ob 3. On success: partial understanding. On Partial: the practitioner understands something is deeply wrong; specific nature requires TS 50+. On Failure: Forgetting mechanism prevents retention entirely. |
| 4+ | Repair (optional) | Extraordinary Repair Weaving per §6.6. Each season of successful Repair: TT −2 permanent (Southernmost contribution removed). |

### Zone Hazard Table

| Zone | Type | Primary Hazard | Resolution |
|---|---|---|---|
| Border zone | Snapped | Shifting Objects: thread configurations at maximum tension; objects around the expedition behave unpredictably | Thread operation (Weaving Ob 2 to stabilise) or Agility Ob 2 to avoid. Failure: 1 Wound per exposed character. |
| Inner zone | Oscillating | Gap incursion: continuous Gap formation produces monstrous entities | Monstrous entity encounter (Mode 1 or 2; see §5.13). Scale determines combat procedure: personal or mass. |
| Core zone | Locked | Configuration instability: the frozen moment of catastrophe exerts pressure on present-state consciousness | All non-practitioners: Spirit check Ob 2 per round of exposure or Certainty −1. Practitioners: Contact duration halved (Thread density saturates the working space). Forgetting Check fires at full Ob for Core Sites (Ob 4). |

### Expedition Failure

If the military escort routes (Cohesion 0) or all practitioners are incapacitated: expedition retreats. Consequences:
- All participants: Certainty −1
- TT +1 (disturbing the Southernmost without completing stabilisation work leaves configurations more agitated)
- Retreat from Core zone: Agility Ob 2 or an additional encounter fires before the party exits

### Expedition Success Indicators

- **Diagnosis complete**: The Southernmost's Thread signature is understood by at least one practitioner. This is the prerequisite for any Extraordinary Repair Weaving or Ceiral Ritual attempt — the practitioners must understand what they are working on.
- **Awareness gain**: Successful expedition Diagnosis: +1 Southernmost Awareness for the faction (applied at seasonal accounting).
- **Research access**: After successful expedition reaching the primary site, a practitioner officer with TS 50+ may take Research actions in the Locked Zones in subsequent seasons (see §6.6).

---

## 6.4 Encounter Reference

Encounters fire once per zone during Exploration (Season 2). The GM selects or rolls; encounters should reflect the zone type.

**Thread phenomenon** (any zone): A practitioner must identify and navigate a live Thread configuration. Weaving or Pulling check; Ob by zone (Border 2, Inner 3, Core 4). On Partial or Failure: ThS −1 for lead practitioner; TT +1.

**Hostile entity** (Inner zone typical): Monstrous entity emerges from active Gap. Combat. On failure to contain: Gap remains open; TT +2 this season.

**Environmental hazard** (Border or Core): Physical consequence of Thread instability. Endurance or Agility check; Ob 2–3. On Partial or Failure: 1 Wound per character in the zone.

**Discovery Event** (Approach, automatic): Lead practitioner perceives the boundary configurations. No roll. GM delivers a brief description of what Thread sight reveals at the Southernmost's edge. This scene counts as the character's first exposure for Forgetting Check purposes.

---

## 6.5 The Ceiral Ritual

The Ceiral Ritual is the canonical method for stabilising the Southernmost's wound. It requires specific knowledge (the Ceiral Text), high practitioner competence, and Awareness sufficient to identify what is actually being addressed.

### Requirements

- Ceiral Text (in faction possession)
- Southernmost Awareness 5+ (faction stat); without this: +2 Ob
- Lead practitioner: TS 60+
- Two additional participants: TS 20+ each
- One full season preparation: the lead practitioner and participants are unavailable for other actions during the preparation season. The faction leader's two actions remain free.

### The Ritual Roll

Lead practitioner's Weaving pool. Ob 5. Each participant with TS 20+ adds +1D (maximum +4D total bonus from participants).

| Degree | Result |
|---|---|
| Overwhelming | The wound stabilises permanently. TT −10. The Southernmost becomes settleable — territory may be developed and inhabited. |
| Success | Temporary stabilisation. TT −6. The Southernmost is accessible without expedition prerequisites for 5 seasons. The Ritual may be re-attempted after this window. |
| Partial | Partial stabilisation. TT −3. Forgetting Ob −1 permanently (the wound is slightly less incomprehensible). The lead practitioner cannot attempt the Ritual again; a new lead is required. |
| Failure | The outer winding tears. TT +8. A monstrous entity of Mode 3 emerges at the primary site. The lead practitioner is Incapacitated. |

---

## 6.6 Extraordinary Repair Weaving

Extraordinary Repair Weaving is the technical procedure discovered through deep research in the Locked Zones. It is not a single ritual but a multi-season working — sustained configurational surgery rather than a one-time intervention.

### Access Requirements

- Southernmost Awareness 8+ (faction stat)
- Successful expedition reaching the primary site (§6.3 completed)
- Practitioner officer with TS 50+ assigned to Research in the Locked Zones
- Research roll: Memory + Einhir Scholar History, Ob 4. On success: the full collapse technical record is read; the practitioner learns the specific structural repair procedure required.

### Repair Procedure

After completing the Research roll (above), the practitioner may begin Repair seasons. Each season of Repair Weaving:

- **Roll**: Lead practitioner's Weaving pool, Ob 3 (Repair is less acute than the Ceiral Ritual but more technically demanding than ordinary Weaving at this scale; the -1D contact penalty for Core zone is in effect)
- **Success or Overwhelming**: TT −2 permanent (Southernmost contribution removed). +1 Awareness for faction.
- **Partial**: TT −1 (partial reduction). Practitioner: ThS −1. May continue next season.
- **Failure**: No progress. TT +1 (disturbing the wound without completing the work). ThS −2 for practitioner.

After 4–5 successful Repair seasons: the Southernmost is fully stabilised. The wound is closed; configuration dynamics return to normal Thread behaviour; Gap formation ceases. The Southernmost becomes a historically significant but no longer active hazard.

**Note**: Extraordinary Repair Weaving and the Ceiral Ritual are not mutually exclusive. A faction may pursue both paths simultaneously with different officers. The TT reductions stack.

---

## 6.7 Southernmost Crisis Timeline

The outer Einhir winding — the large-scale configurational structure that has been containing the catastrophe since 0 AG — is not stable indefinitely. As TT rises, the pressure on the winding increases.

### Crisis Trigger (Patched — replaces season-based counter)

The crisis fires based on TT level and absence of stabilisation work, not a fixed campaign season:

1. **TT reaches 50**: The outer winding begins showing signs of strain. A visible faction-facing event fires: practitioners in adjacent territories report pressure; the boundary configurations are degrading. This event is the player's warning.

2. **TT 50 sustained for 3 consecutive seasons without stabilising Weaving**: The outer winding begins to crack. A second event fires: visible map effect; +1 TT per season from Southernmost (in addition to other sources) begins accumulating.

3. **Cracking continues for 3 more seasons without a Ceiral Ritual attempt**: The outer winding fails. TT +2 per season from the Southernmost, automatic and unremovable until the Ritual succeeds or Extraordinary Repair Weaving completes.

**Stabilising Weaving** (to pause the cracking clock): Any practitioner performing a Ritual action targeting the Southernmost's outer winding (Ob 3, TS 40+) pauses the cracking counter for that season. This is a delaying action only — it does not reverse cracking already underway.

### Design Rationale

This replaces the original Season 17 fixed trigger. Players who aggressively manage TT can delay the crisis indefinitely. Players who neglect TT management trigger the crisis earlier. The crisis is tied to player decisions, not to a campaign timer that may not match the campaign's pace.

---

## 6.8 Southernmost in Board Game Mode

In Board Game mode, Southernmost mechanics are abstracted to the faction-level:

- **Expedition Action**: Available as an extended Council Phase action (officer unavailable for Season). Prerequisite: TT ≥ 40. Outcome: Southernmost Awareness +1 for acting faction.
- **Research Action** (as standard Domain Action table): Awareness +1, Complexity Ob 1–4, risk: Church attention.
- **Ceiral Ritual**: Available as a multi-season action. Uses faction's Mandate pool as proxy for practitioner TS. Requirements as TTRPG mode; Ob set against faction's accumulated Awareness level.
- **Crisis Timeline**: Fires per §6.7. Represented as a track on the board — visible to all players.

---

*End of Stage 4 compilation. Stage 5 (Clocks: TT/TC/IP, threshold events, interaction rules) follows.*




---



# PART SEVEN: THE THREE CLOCKS

Three public clocks run simultaneously throughout the campaign. All are displayed permanently on the table dashboard. Players always know all three values.

**TT** (Thread Tension) measures the configurational stress of the thread-substrate. It rises from thread operations and falls from sustained repair work. It is the campaign's metaphysical pressure gauge.

**TC** (Theocracy Clock) measures the Church of Galbados's structural conquest of Valorian civil and political life. TC is not a measure of the Church's goodness — it is a measure of how much of the peninsula's governance has been absorbed into its institutional framework.

**IP** (Altonian Pressure) measures the external threat of Altonian intervention. It is driven primarily by Valoria's internal instability and by TT/TC conditions that alarm the three Altonian factions for different reasons.

All clock rates are **per season**. One campaign year = 4 seasons (approximately 16 sessions at standard play pace). (MI-3)

---

## 7.1 Thread Tension (TT) — 0 to 100

**Starting value:** 28 (Stirring).

**TT is public.** Displayed permanently on the table dashboard.

**TT rises from specific causes only.** Ordinary action — political manoeuvring, military operations without Thread involvement, social scenes — does not strain the substrate.

### TT Rise Sources

| Source | TT Change |
|---|---|
| Partial Weaving | +1 |
| Failed Weaving | +2 |
| Partial Pulling | +1 |
| Failed Pulling | +2 |
| Overwhelming Lock | +1 |
| Successful Lock | +2 |
| Partial Lock | +3 |
| Failed Lock | +4 |
| Overwhelming Dissolution | +2 |
| Successful Dissolution | +4 |
| Partial Dissolution | +5 |
| Failed Dissolution | +6 |
| Past-Oriented Pull (any degree) | +3 additional (stacks with operation cost) |
| Mass combat Thread operation | All above costs ×3 (floor), capped at +15 per operation (M-1) |
| Destruction of Einhir site | +3 |
| Significant mass battle | +2 |
| Active Gap, per season | +4 |
| Passive drift | +1 per 4 seasons |
| Niflhel Southernmost harvesting | +0.5 per season |
| Involuntary Leap | +1 per event |

### TT Decrease Sources

| Source | TT Change |
|---|---|
| Overwhelming Weaving (Relational scale or above) | −1 (MI-1: Relational minimum required) |
| Preserving Einhir site, per season | −1 |
| Sustained community Weaving, full season | −2 |
| Gap closed with reconstructed Einhir ritual | −4 |
| All major factions at Stability 5+ at seasonal accounting | −1 |
| Ceiral Ritual (Success) | −6 |
| Ceiral Ritual (Overwhelming) | −10 |
| Extraordinary Repair Weaving (Success or Overwhelming, per season) | −2 |

### TT Thresholds

| TT | State | World Symptoms | Mechanical Effects |
|---|---|---|---|
| 0–19 | Dormant | Thread practice is folklore. | Leap fails automatically. Practitioners cannot function. |
| 20–39 | Stirring | Practitioners surface. Shifting Objects reported. | Leap becomes available. |
| 40–59 | Wakening | Practitioners are open rumour. Monstrous Incursion in one territory. Church investigates. | — |
| 60–79 | Fracturing | Multiple practitioners active. Gaps form. Thread operations conspicuous. | Thread operations: +1 Ob to all rolls. |
| 80–99 | Rupturing | Magic enters battlefields. Entities establish territory. Einhir becomes political. | Thread operations: +2 Ob to all rolls. |
| 100 | The Rupture | Campaign event. The relationship between the rendered world and the thread-substrate changes permanently. | Not a loss state — a narrative threshold. What this means is determined by the current state of the world. |

### TT Consequences When a Gap Opens

| TT | Consequence |
|---|---|
| Below 40 | Shifting Object forms |
| 40–59 | Weak monstrous configuration |
| 60–79 | Full monstrous entity |
| 80+ | Full entity + Shifting Object in each adjacent territory |

### TT Threshold Events

When TT crosses a threshold, the GM determines a narratively appropriate consequence from the current situation. No event deck is used. The current political, social, and thread-level state of the world generates the threshold consequence organically.

*Example: TT crossing 40 (into Wakening) while the Church has an active Inquisitor investigation produces a different threshold event than TT 40 crossing during a period of factional cooperation. The threshold is the trigger; the event is the current world state colliding with that trigger.*

---

## 7.2 The Theocracy Clock (TC) — 0 to 100

**Starting value:** 22.

*(Canonical value per timeline. Reflects 45 years of post-independence institutional accumulation building on centuries of Altonian colonial-era Church establishment. Earlier document values of 15 are superseded.)*

**TC is public.** Displayed alongside TT and IP.

TC represents the Church of Galbados's slow structural conquest of Valorian civil and political life. At TC 100, the Church does not invade — it has made itself the state. Whether the Crown survives and in what form is the players' decision.

### TC Rise Sources

| Source | TC Change |
|---|---|
| Church demand formally unmet by Crown or nobility | +1 |
| Knights Templar deployed without ducal or Crown authorisation | +2 |
| Heresy conviction of a prominent public figure | +2 |
| Inquisitor operation in Crown territory without Crown authorisation | +1 |
| Church Mandate reaches 9–10 at seasonal accounting | +1/season |
| TT > 45 (Thread events read as divine warning requiring Church leadership) | +1/season |
| TT > 60 (Thread crisis provides theological justification for authority expansion) | +2/season (total, not additive to above) |
| Player characters use Thread abilities in Church-observed contexts | +1 per event |
| Cardinal of Fortitude mobilises Knights Templar for internal enforcement | +3 |
| Heresy investigation opened against a sitting noble | +2 |
| Baralta's Mandate drops below 5 (primary secular TC brake removed) | +1/season |
| IP > 45 (Church offers Altonian theological mediation as Crown alternative) | +1/season |

### TC Decrease Sources

| Source | TC Change |
|---|---|
| Crown publicly overturns a Church legal ruling | −1 |
| Baralta invokes Sovereign Authority doctrine (§9.1) | −2 |
| Cross-ducal coalition formally contests Church institutional expansion | −2 |
| Confessor Himlensendt suffers political setback (Mandate −2 or more in one season) | −1 |
| Church found complicit in Niflhel operations (evidence presented publicly) | −3 |
| Successful Grand Debate ruling against Church on civil authority claim | −2 |
| Kingdom-wide average Mandate across all factions ≥ 6 at seasonal accounting | −1 (M-6) |

**Church Stability brake:** When Church Stability falls to 5 or below at seasonal accounting, TC generation ceases that season regardless of Church Mandate. Cardinals competing publicly suppresses institutional momentum. (M-6)

### TC Thresholds

| TC | State | World Symptoms |
|---|---|---|
| 0–19 | Institutional Pressure | Church lobbies Crown and nobility through requests, not demands. Charities and scholarship expand with quiet institutional intent. |
| 20–39 | Ecclesiastical Consolidation | Church assumes authority over specific civil domains: marriage law, inheritance disputes, educational standards. Cardinal of Justice's rulings carry near-Crown legal weight. |
| 40–59 | The Ultimatum | Confessor formally demands Crown recognition of Church supremacy over spiritual governance — defined broadly enough to cover education, civil morality, and all Einhir cultural materials. A specific demand is placed before Parliament. |
| 60–79 | Schism Politics | Church publicly declares the Crown spiritually compromised. Excommunication threats against specific nobles. Knights Templar movement becomes openly political. |
| 80–99 | Theocratic Seizure | Cardinals claim co-governance authority. Knights Templar occupy key institutional positions. Confessor issues writs superseding Crown administrative decisions in specific territories. |
| 100 | The Holy State | Campaign event. Confessor Himlensendt declares Valoria a Holy State under Church governance. This is the culmination of a two-century institutional project. |

**TC 80 — Church Territorial Seizure:** At TC 80, the Church may attempt to seize territories through institutional claim rather than military force. Per-territory roll vs variable Ob. Counter-play options available. (See Faction section for full procedure.)

---

## 7.3 Altonian Pressure (IP) — 0 to 100

**Starting value:** 20 (Dormant).

**IP is public.** Displayed alongside TT and TC.

IP measures the threat of Altonian military and political intervention. Altonia is not a monolithic actor — three internal factions shape its policy toward Valoria and they are not in agreement. Players discover this through play.

### IP Thresholds

| IP Range | State | Effect |
|---|---|---|
| 0–29 | Dormant | Trade continues. Altonian spies monitor internal conditions. |
| 30–44 | Aggressive | Economic sanctions. Proxy disruption of Valorian factional politics. |
| 45–59 | Hostile | Border skirmishes. Vassalage demands made through diplomatic channels. Tutoring Demand for Prince Torben triggers at IP 30+. |
| 60–74 | Warlike | Invasion preparations begin. Internal Valorian factions face direct Altonian pressure. |
| 75–99 | Invasion Imminent | Altonian military units on the border. Merchant Consortium's position collapses. |
| 100 | Invasion | Campaign event. Altonian forces enter Valoria. |

### IP Direct Triggers

The following specific events cause immediate IP changes outside the cross-clock linkage system:

| Trigger | IP Change |
|---|---|
| Public Thread use (observed by Altonian agents or diplomatic contacts) | +2 per event |
| Succession ratification delayed past two campaign arcs | +2 (Almaic Kyriakos documents instability) |
| Schoenland active trade alliance with Valoria | −2/year (naval support against Altonian aggression) |
| Grand Diplomatic Scene — victory | IP frozen; peace treaty available |

*Note: A comprehensive standalone IP rise/fall table is not fully specified in current design documents. The linkage table below covers the primary IP drivers. Additional direct triggers should be developed as play reveals further cases. [GAP: IP direct rise/fall table incomplete — register for Phase 3 attention.]*

### IP Decrease Sources

IP decreases primarily through diplomatic and political actions that reduce Altonia's strategic incentive to intervene:

- Valoria presenting a **unified diplomatic front** (all major factions at cooperative disposition or better): IP passive drift halts for that season
- **Schoenland trade alliance** secured: −2 IP/year, and Altonian Merchant Consortium's political cover is removed
- **Grand Diplomatic Scene** victory (endgame; requires faction dominance + Church Mandate > 5 + TT < 50): IP frozen, peace treaty possible

---

## 7.4 Cross-Clock Interactions

All rates per season. Interactions are cumulative unless marked (total).

| Condition | Effect |
|---|---|
| TT > 45 | TC +1/season; IP +1/season |
| TT > 60 | TC +2/season (total); IP +2/season (total) |
| TC > 40 and IP > 45 | IP +1/season (Church offers theological mediation; Almaic Kyriakos rejects but gives Merchant Consortium political cover) |
| TC > 60 | IP +2/season (Altonia interprets Church dominance as violating Secession Wars' religious exclusivity clauses) |
| TC > 60 and IP > 45 simultaneously | IP +2/season; Almaic Kyriakos begins formal documentation of Church expansion for the Altonian Emperor |
| TT > 60 and TC > 60 simultaneously | Both clocks accelerate at maximum rate |
| All three clocks above their midpoints simultaneously | Campaign enters endgame phase |
| TT > 45 and TC > 40 simultaneously | TC +1/season (compounding; both conditions must persist each season) |

**Note on (total) entries:** When TT > 60, the TC and IP costs are +2/season total — not +1 (from TT > 45) + 1 (from TT > 60) = +2. The higher threshold replaces, not adds to, the lower threshold's contribution.

### Structural Tension Summary

TT and TC are in positive feedback. Rising TT produces Thread events the Church interprets as theological warrant for expanded authority. TC pressure produces internal instability that allows TT to rise faster. IP is the external constraint — it accelerates when internal conditions are worst.

Players have access to the only tools that can directly address TT (thread operations reducing configurational stress) and the only investigative capacity that can address TC's hidden structural driver (the Church-Niflhel connection). They are structurally positioned as the campaign's repair mechanism.

---

## 7.5 Passive Drift

At each seasonal accounting, apply passive drift before any other clock adjustments:

| Clock | Passive Drift | Condition |
|---|---|---|
| TT | +1 per 4 seasons (i.e., +1 per campaign year) | Always |
| TC | +1 per season | When Church Mandate ≥ 7 at accounting |
| IP | +1 per season | Baseline; Altonian Martial Senate monitoring |

Passive drift represents background pressure that players must actively counteract. A campaign in which players do nothing deteriorates: TT +1/year, TC +1/year (Church steady pressure), IP +1/year (Martial Senate baseline). The world deteriorates at a rate the players can observe but did not choose.

---

## 7.6 Board Game Mode — Clock Representation

In Board Game mode, all three clocks run as visible tracks on the board. Rules are identical to TTRPG mode with the following adjustments:

- TT and TC advance triggers fire at **seasonal accounting** (Phase 5), not continuously. Clocks do not advance mid-round. (R18, R19)
- **TC threshold override**: When TC threshold events would override a player's planned Domain Action, only player-chosen Domain Actions are deferred. Reactive checks (Stability checks, NPC responses) still fire immediately. (R19)
- All three clocks are player-visible at all times. No hidden tracking.
- Board tracks: TT on shared track, TC on shared track, IP on shared track. Threshold markers placed at 20/40/60/80/100.

---

*End of Stage 5 compilation. Stage 6 (Factions: 7 factions with asymmetric powers, ethical tendencies, leader separation) follows.*




---



# PART EIGHT: FACTIONS

Valoria's political landscape is contested by eight factions, six with full mechanical presence. Each faction has a distinct ethical framework that modifies how its Domain Actions resolve, a Unique Action only it can perform, and a two-layer structure distinguishing institutional tendency from leadership deviation.

---

## 8.1 Faction Mechanics

### Faction Stats (6-stat, 1–7 scale)

| Stat | Represents |
|---|---|
| Mandate | Public legitimacy and popular support |
| Influence | Political reach and diplomatic weight |
| Wealth | Economic capacity |
| Military | Armed force and unit capacity |
| Intel | Intelligence network and covert operations |
| Stability | Internal cohesion and crisis resistance |

**Partial sheets:** Niflhel (no Mandate, no Military), Revolution (Influence, Stability, Intel only), Lowenritter (no Mandate, no Wealth — Military, Intel, Influence, Stability only).

**NPC personal pools** (used in social scenes and investigations) are separate from faction stats. Named NPCs use the canonical 10-attribute set. Faction stats represent institutional capacity; NPC attributes represent personal capability.

### Starting Values

| Faction | Mandate | Influence | Wealth | Military | Intel | Stability |
|---|---|---|---|---|---|---|
| Crown | 5 | 5 | 4 | 4 | — | 4 |
| Church | 5 | 6 | 5 | 4 | — | 5 |
| Hafenmark | 4 | 4 | 5 | 3 | — | 4 |
| Varfell | 4 | 4 | 4 | 4 | — | 4 |
| Guilds | 3 | 4 | 6 | 2 | — | 5 |
| Niflhel | — | 5 | 4 | — | — | 4 |
| Revolution | — | 3 | — | — | — | 3 |
| Lowenritter | — | 3 | — | 5 | 3 | 5 |

*Schoenland is not a faction — it is a spoiler actor. See §8.10.*

### Domain Actions

When a personal action has faction-level scope, the GM recognises it as a Domain Action. The personal roll resolves both the personal outcome and the faction effect simultaneously.

**Domain Ob:** Target faction's relevant stat ÷ 2 (round up). On a 1–7 scale this yields Ob 1–4.

**NPC faction rolls:** When a faction acts without a player character driving it, the GM rolls the relevant faction stat as a dice pool (d10s, TN 7) against the Domain Ob. For contested actions, both roll; higher net successes wins. Ties go to the defender.

**Seasonal cap:** ±2 per stat per season.

### Ethical Framework Modifiers

Each faction's ethical framework modifies Domain Action rolls. Frameworks are modifiers, not a separate system.

- **−1 Ob:** Actions aligned with the faction's ethical framework
- **+1 Ob:** Actions that contradict or strain the framework
- **+2 Ob:** Church only — actions that would reveal Thread truth (institutional perceptual prophylaxis)

### Leader vs Institution

**Institutional Tendency:** What the faction does without active PC direction. Represents the faction's default priorities and the direction NPC AI applies.

**Leadership Deviation:** When a faction leader acts against the institutional tendency, a Stability check fires at next seasonal accounting. Ob varies by faction. Deviation is not forbidden — it is costly.

### Nine Political Axes

The nine political axes generate campaign events, NPC motivations, and faction conflicts. They are **not tracked numerically** — they are qualitative GM tools for scene generation.

| Axis | Pole A | Pole B | Primary Factions |
|---|---|---|---|
| 1. Sovereignty | Crown authority | Church authority | Crown vs Church |
| 2. Knowledge | Thread truth accessible | Thread truth suppressed | Varfell/Revolution vs Church |
| 3. Legitimacy | Constitutional monarchy | Theocratic governance | Crown/Hafenmark vs Church |
| 4. Cultural identity | Einhir recovery | Colonial settlement | Revolution vs Crown/Church |
| 5. Economic control | Guild autonomy | State/Church taxation | Guilds vs Crown/Church |
| 6. Military authority | Ducal/Crown command | Templar independence | Hafenmark/Crown vs Church |
| 7. Information | Transparency | Secrecy | Revolution vs Niflhel/Varfell |
| 8. External threat | Accommodation of Altonia | Resistance | Crown (split) vs all |
| 9. Ontological | The world is what it appears | The world is more | Church vs practitioners |

**Using the axes:**
1. Every named NPC has a position on 2–3 axes — determines Resonant Style vulnerability and Belief content
2. When two factions interact, identify which axes are in tension — the scene's conflict is about that axis
3. War justification (casus belli) maps to axes
4. Domain Echo content is described in terms of the relevant axis
5. Axes can be active, dormant, or resolved over the campaign — Axis 9 resolves when Thread truth becomes public

---

## 8.2 Faction 1: The Crown (Monarchy)

**Ethical Framework: Virtue Ethics**

The institution evaluates actions by whether they demonstrate virtuous character — courage, justice, temperance, prudence — regardless of outcomes.

- Public, visible, virtuous actions (defending the weak, upholding law, honouring treaties): **−1 Ob**
- Covert, expedient, or morally ambiguous actions: **+1 Ob**

The Crown is structurally weakest at covert operations. Its strength is open, honourable action.

**Institutional Tendency:** Maintain treaties. Defend held territory. Suppress disorder. Follow constitutional procedure. Will not initiate aggression, break treaties, or support Thread operations.

**Leadership Deviation:** Acts against tendency (breaks treaty, supports practitioners, ignores Parliament): Stability check **Ob 2** at next accounting.

**Unique Action — Royal Decree**

Once per season, the Crown issues a unilateral political act that bypasses normal Domain Action timing.

| | |
|---|---|
| **Roll** | Mandate vs Ob 2 |
| **Success** | One faction attribute change (any faction, ±1) takes effect immediately rather than at seasonal accounting |
| **Failure** | Mandate −1 (overreach) |
| **Constraint** | Cannot target Intel — decrees are public acts |
| **Limit** | 1/season; consecutive seasons: +1 Ob per consecutive use (decree fatigue) |

**Default Leader: King Almud Almqvist**
- Conviction: Order/Reason · Resonant Style: Consequence · TS: 28 (near Stirring; unrecognised)
- Privately sympathises with the Restoration. Governs through the post-war settlement that suppressed it. Institutional tendency and personal beliefs in direct conflict.

---

## 8.3 Faction 2: The Church of Galbados

**Ethical Framework: Divine Command**

Correctness is determined by institutional authority, not outcome or character. Actions are evaluated by whether they conform to Galbados's revealed will as interpreted by the hierarchy.

- Doctrine-aligned actions (suppressing heresy, expanding Piety, enforcing moral law): **−1 Ob**
- Actions contradicting doctrine or undermining Church authority: **+1 Ob**
- Actions revealing Thread truth (supporting practitioners, Southernmost investigation): **+2 Ob**

**Institutional Tendency:** Expand Piety. Suppress heresy. Accumulate civil authority. Deploy Templars against perceived threats. Pursues theological conquest, not territorial.

**Leadership Deviation:** Confessor acts against doctrine: Stability check **Ob 3**. Hardest deviation cost of any faction — theological coherence is the Church's structural strength.

**TC Relationship:** Church Mandate 5+ at accounting: TC +1/season. Stability ≤ 4: TC generation pauses (Cardinals competing). *(On 1–7 scale, Mandate 5 = strong institutional position; Stability 4 = mid-range.)*

**Unique Action — Excommunication**

| | |
|---|---|
| **Roll** | Church Mandate vs target's Mandate (faction leader) or Ob 2 (non-leader) |
| **Overwhelming** | Target loses Circles bonus with Church contacts; target faction Mandate −1; target barred from public office and Church-loyal command; personal Reputation −1 with all factions |
| **Success** | As Overwhelming minus the Reputation penalty |
| **Failure** | Church Mandate −1; target gains Mandate +1 (sympathy martyr) |
| **Constraint** | Requires Church Mandate ≥ 3 (on 1–7 scale: institutional authority threshold) |
| **Reversal** | Grand Debate (5 exchanges) or appointment of a new Confessor |

**Default Leader: Confessor Arne Himlensendt**
- Conviction: Faith · Resonant Style: Evidence · TS: 0 (theologically foreclosed)
- Sincerely devout. Zero awareness of Galbados's actual nature. Not cynical — wrong.

---

## 8.4 Faction 3: Hafenmark (Duchy)

**Ethical Framework: Categorical Imperative**

Actions are evaluated by whether they could be universalised — would this remain coherent if every actor in this position did the same? The institution values consistency, precedent, and rule of law above outcomes.

- Actions based on legal precedent, constitutional authority, established procedure: **−1 Ob**
- Ad hoc, situational, or precedent-breaking actions: **+1 Ob**

Hafenmark excels at procedural power (parliamentary manoeuvres, legal challenges, constitutional arguments) and struggles with improvisation.

**Institutional Tendency:** Maintain constitutional order. Defend ducal prerogative. Resist Church encroachment through legal means. Follow established procedure. The institution conserves rather than innovates.

**Leadership Deviation:** Baralta acts against tendency (extralegal action, breaking with Parliament, allying with Niflhel): Stability check **Ob 1**. Low cost — Baralta IS the institution. Her personal authority is so thoroughly embedded that deviation costs are minimal. This is her structural advantage.

**Unique Action — Sovereign Authority Doctrine**

Once per campaign arc, Baralta invokes the constitutional claim that her authority to rule Hafenmark is a direct divine grant, superseding Church jurisdiction.

| Degree | Result |
|---|---|
| **Overwhelming** | TC −3. Church Mandate −1. Heresy Investigation blocked this season. +1D social vs Church for the arc. |
| **Success** | TC −2. Church Mandate −1. Heresy Investigation opens against Baralta (Ob 4 to pursue). |
| **Partial** | TC −1. Heresy Investigation opens immediately. Church Influence +1. |
| **Failure** | TC +1. Heresy Investigation immediate. Baralta's Mandate −1. |

*Roll: Mandate vs Ob 4. Once per campaign arc.*

*Heresy Investigation consequence:* Grand Debate (5 exchanges). If it succeeds without player intervention: Mandate −2, TC +3, TC suppression removed.

**TC Suppression:** While Baralta's Mandate remains 4+ (on 1–7 scale), she suppresses TC at −1/season. If Mandate drops below 4, suppression disappears. If excommunicated: TC +4 immediately.

**Default Leader: Duchess Inge Baralta**
- Conviction: Order · Resonant Style: Evidence · TS: 0 (essentialist theology forecloses development)
- Her faith and her politics are structurally incompatible. She holds both without experiencing contradiction. This is her strength and her vulnerability.

---

## 8.5 Faction 4: Varfell (Duchy)

**Ethical Framework: Consequentialist Pragmatism**

Actions are evaluated purely by outcomes. Means are irrelevant if ends are achieved. The institution is structurally amoral — it rewards success and punishes failure without moral weight.

- Actions with measurable outcomes within one season (concrete, verifiable results): **−1 Ob**
- Actions with uncertain or long-term payoff (ideological campaigns, relationship-building, cultural investment): **+1 Ob**

Varfell is strongest at short-term tactical play and weakest at institution-building. They win battles and lose peace.

**Institutional Tendency:** Maximise information advantage. Acquire resources including Thread-related materials. Avoid public commitments. Keep options open. Defaults to intelligence operations and economic positioning over military or social action.

**Leadership Deviation:** Vaynard acts against tendency (public ideological commitment, open Restoration support, military aggression without intelligence preparation): Stability check **Ob 2**. The institution expects its leader to be clever, not bold.

**Unique Action — The Private Collection**

Vaynard maintains a collection of Einhir artefacts and Thread-locked objects. Once per season, he deploys an item for a specific purpose.

| | |
|---|---|
| **Roll** | Intel vs Ob 2 |
| **Success (choose one)** | +2D to one Thread-related Domain Action this season; *or* reveal one hidden faction attribute; *or* −1 Ob to one Einhir Research action this season |
| **Failure** | Artefact's Thread signature detected by a practitioner. Church Intel gains +1D vs Varfell for 1 season. TT +1. |
| **Long-term cost** | Each use: +1 to Vaynard's hidden TS. At TS 14+ (his starting value), each use triggers Spirit check TN 7 Ob 1 for a Discovery Event. |

**PC takeover — Collection Discovery Event:** If a non-Vaynard PC takes over Varfell, the Private Collection transfers as an institutional asset (the artefacts exist physically). However, encountering the collection for the first time triggers a mandatory Discovery Event: the new leader finds Vaynard's research notes alongside Thread-locked objects of obvious significance. Spirit check TN 7 Ob 1. Success: the player understands what they have inherited and gains TK 1 immediately. Failure: the weight of the collection lands without context — Certainty −1 and a new Belief is offered from behind a position of ignorance.

**Default Leader: Duke Magnus Vaynard**
- Conviction: Reason · Resonant Style: Consequence · TS: 14 (Dormant; unrecognised)
- Pursuing Thread knowledge through acquisition rather than experience. His consequentialist framework treats Thread reality as a resource to be managed rather than a truth to be confronted.

**Thread Investigation Track (TK) — 0 to 5**

Vaynard's TK measures his understanding of Thread metaphysics, the Calamity's mechanism, and the Church's concealment.

| TK | Campaign Effect |
|---|---|
| 1–2 | Informed questions. Acute awareness, not understanding. No TC effect. |
| 3 | Structural theory (wrong in detail, correct in structure). Succession leverage formally linked to Southernmost access terms. TC +1. |
| 4 | Urgency. Willing to offer collection access (including originary locks) for Thread education and Southernmost partnership. TC +2. |
| 5 | Dangerous knowledge — understands what Galbados was structurally. Seeks capability, not further knowledge. TC +3. |

TK advances through: practitioner relationship (sustained season, cap ×2); originary lock examination with practitioner context (cap ×1); Church archive access via Niflhel channels (+1/archive); players sharing Thread-level knowledge directly (+1–2 by depth); Discovery Event triggering TS 30 (+2 immediately).

---

## 8.6 Faction 5: The Guilds

**Ethical Framework: Moral Relativism**

The institution recognises no universal moral principles. Each guild evaluates actions by the standards of its own craft, community, and economic interest. The institution is inherently pluralistic — what is right for one guild may be wrong for another.

- Actions benefiting trade, economic stability, or guild autonomy: **−1 Ob**
- Actions requiring moral consistency across contexts (enforcing a single law, demanding uniform behaviour, ideological campaigns): **+1 Ob**

The Guilds are powerful as an economic bloc and weak as a political actor. They cannot project unified political will.

**Institutional Tendency:** Protect commerce. Maintain guild autonomy. Avoid military entanglements. Resist taxation. The institution defaults to economic self-interest in each territory independently.

**Leadership Deviation:** The Guilds are governed by a rotating Guildmaster Council — no single leader. Redirecting Guild policy requires convincing the Council: Influence vs Ob 3 as a Domain Action. Guilds are slow to change course but resistant to disruption from the top.

**Unique Action — Economic Leverage**

The Guilds apply economic pressure to any faction present in a territory where Guild Favour ≥ 5 (on the 1–7 territory-level track).

| | |
|---|---|
| **Roll** | Wealth vs target faction's Wealth |
| **Overwhelming** | Target loses 1 Wealth + 1 Prosperity in one territory (full economic warfare) |
| **Success** | Target faction loses 1 Wealth for 1 season (trade disruption, supply price increases, labour withdrawal) |
| **Failure** | Guild Favour −1 in that territory (backlash against perceived extortion) |
| **Constraint** | Cannot target factions in territories where Guild Favour < 5 |

**Leader: Guildmaster Council (NPC collective)**
- No single conviction axis. Council decisions reflect the majority interest of the strongest guilds in the current season.
- Individual guild leaders can be recruited, bribed, or threatened independently (treat as officers). The Guilds' vulnerability is that they are a coalition, not an institution.

---

## 8.7 Faction 6: Niflhel (Shadow Network)

**Ethical Framework: Amoral Consequentialism**

No moral framework. Actions are evaluated by operational effectiveness only. This is not consequentialism with a utilitarian goal — it is pure instrumentality.

- Covert Domain Actions (intelligence, sabotage, assassination, smuggling): **−1 Ob**
- Public Domain Actions (anything requiring Niflhel to act openly or claim credit): **+2 Ob**

Niflhel cannot build Mandate because it cannot be seen. It is the strongest covert actor and the weakest public one.

**Partial sheet:** No Mandate. No Military. (Influence, Wealth, Intel, Stability only.)

**Institutional Tendency:** Acquire resources. Sell services. Avoid exposure. Intelligence operations, smuggling, and opportunistic service provision. Does not pursue political goals — pursues survival and profit.

**Leadership Deviation:** Four-arm decentralised structure (Dockworkers, Reckoners, Burned, Quiet). No single leader can deviate without the other arms' consent. Redirecting any arm requires Intel vs Ob 3 within Niflhel. Failure: the arm acts independently against the redirecting leader's interests.

**Unique Action — The Quiet Network**

Niflhel deploys the Quiet (its intelligence and assassination arm) against any target. Choose mode before rolling.

**Intelligence mode:**
- Roll: Intel vs target's Intel
- Success: learn one hidden faction attribute or one NPC's active Belief
- Overwhelming: learn two

**Sabotage mode:**
- Roll: Intel vs target's Stability
- Success: target Stability −1
- Failure: operative exposed — Niflhel Intel −1 for 1 season; target gains Grievance Marker

**Assassination mode:**
- Roll: Intel vs target's Intel +2
- Overwhelming: named NPC eliminated; no evidence trail
- Success: named NPC eliminated; evidence trail exists
- Partial: target wounded, not killed; evidence trail
- Failure: operative captured; full exposure; Niflhel Stability −2

**Long-term cost:** Each Quiet deployment in a season: TT +0.5 (cumulative). Niflhel's Southernmost harvesting supply chain disturbs the Thread-configurational environment. They do not know this.

**Leader:** None. The four arm heads are treated as officers, not faction leaders. A PC who infiltrates or takes over one arm controls that arm only.

**Structure is permanent:** Niflhel has no primus inter pares and will not acquire one. A PC who wants to direct Niflhel must control each arm independently. This is intentional — Niflhel's headlessness is a structural feature, not a gap. Full network control requires four separate influence operations, one per arm.

---

## 8.8 Faction 7: The People's Revolution (Restoration Movement)

**Ethical Framework: Rawlsian Social Contract**

Actions are evaluated by whether they would be chosen from behind a veil of ignorance — whether they benefit the least advantaged members of society. The institution values equity, access, and the dismantling of unjust privilege.

- Actions demonstrably benefiting the common population (reducing taxation, expanding access, challenging noble privilege, protecting Einhir cultural practice): **−1 Ob**
- Actions concentrating power, benefiting elites, or suppressing popular expression: **+1 Ob**

The Revolution is strongest when it acts for the people and weakest when it tries to build institutional power for itself. The moment it becomes an establishment, its own framework turns against it.

**Partial sheet:** No Mandate (rejects the legitimacy of the system that confers Mandate). No Military. No Wealth (operates through informal economies). Influence, Stability, Intel only.

**Institutional Tendency:** Spread pamphlets. Undermine elite Mandate. Protect practitioners. Recover Einhir cultural knowledge. Defaults to information warfare and cultural advocacy.

**Leadership Deviation:** No formal leader — a movement. Directing it requires Influence vs Ob 2 within the movement (easier than Niflhel due to ideological coherence). Directing the Revolution toward violence, authoritarianism, or elite alliance triggers Stability check **Ob 3** (the movement fractures if it betrays its own principles).

**Unique Action — Community Weaving**

The Revolution's connection to Einhir cultural continuity allows collective Thread operations that reduce TT.

| | |
|---|---|
| **Roll** | Influence vs Ob = TT ÷ 20 (round up) |
| **Overwhelming** | TT −2 |
| **Success** | TT −1 |
| **Partial** | TT unchanged; Stability −1 (working strained the community) |
| **Failure** | Stability −1; TT +1 (attempt disturbed what it tried to heal) |
| **Constraint** | Requires at least one practitioner with TS 30+ affiliated with the Revolution |
| **Co-movement** | Draw a Co-Movement Card. Even beneficial Thread work has consequences. (P-01) |

**Leader:** None formal. Named figures exist (intellectuals, pamphlet writers, southern community elders) but none has institutional authority. A PC who affiliates must build personal authority through play.

[EDITORIAL: Should one named Revolution figure be established as the default NPC contact point? Suggested profile: southern Einhir elder holding fragmentary inner-tradition knowledge, partially obscured by the Forgetting.]

---

## 8.9 Faction 8: The Löwenritter (Military Order)

**Partial sheet:** Military 5 · Intel 3 · Influence 3 · Stability 5. No Mandate, no Wealth.

The Löwenritter are not an independent political faction — they are an institutional instrument of the Crown. They hold territory (the fortress at the northern border), maintain military capacity, and act as the Crown's deniable covert arm. Their loyalty is to the Crown as an institution, not to any specific monarch.

**Coup Threshold:** Grandmaster Ehrenwall is keeping count of Almud's compromises. When the Löwenritter's internal assessment of the Crown's institutional integrity drops to a threshold (tracked as a private GM counter), a coup trigger is possible. See NPCs section for full Ehrenwall mechanics.

**Martial Law Capacity:** If the coup trigger fires, the Löwenritter can impose Martial Law on Crown territories — suspending normal Domain Action resolution and replacing it with Military-based Stability enforcement. This is a campaign-level event, not a standard Domain Action.

**Riskbreakers:** The extralegal arm of the Löwenritter. Operations are not recorded in official documents. See §9.3.

---

## 8.10 Schoenland (Spoiler Actor)

Not a faction. Not player-controllable. A neutral trade port that profits from sustained tension on the peninsula.

**Orientation:** Pro-war (arms sales), anti-conquest (benefits from feuding, not resolution). Actively stokes tensions without triggering settlement.

**Board game representation:** Territory 15. Modifies Trade orders. GM-driven.

**Diplomatic path:** If Valoria presents as a stable trading partner early, Schoenland becomes an ally providing naval support against Altonian aggression: IP −2/year through trade agreements. If Valoria is fragmented, Schoenland hedges toward Altonia.

---

## 8.11 Parliamentary Vote

When a political matter reaches Parliamentary scale (Crown choosing whether to defend Vaynard; Grand Debate ruling on Church authority; Baralta invoking Sovereign Authority institutionally), resolve as a Parliamentary Vote:

1. Both sides roll relevant faction pools (typically Mandate for legitimacy claims, Influence for procedural contests)
2. Ob = opponent's relevant stat ÷ 2 (round up)
3. Best of **3 exchanges.** First side to win 2 exchanges wins.
4. If neither side wins 2 of 3 (draws possible when both meet Ob): motion fails by abstention — TT +1 and TC +1 (institutional paralysis)
5. Player characters may substitute personal pools for faction pools when personally representing the faction. Use the higher.

---

## 8.12 Seasonal Accounting — Faction Phase

At the end of each campaign season (~4 sessions):

1. Apply pending Domain Action outcomes
2. Each faction rolls **Stability check**: pool = Stability score (d10s, TN 7)

| Situation | Stability Check Ob |
|---|---|
| Quiet season, no major events | 1 |
| One active threat (military, political, or economic) | 2 |
| Two concurrent threats | 3 |
| Active attack on Mandate or Wealth | 4 |
| Campaign-level crisis (war, heresy investigation, economic collapse) | 5 |

- Failure: Stability −1
- Overwhelming (net ≥ 2× Ob): Stability +1 (max 7)
- **Anti-death-spiral floor:** Faction at Stability 2 or lower is treated as Ob 4 regardless of actual pressure. Prevents immediate cascade; gives players a window to intervene.

3. Apply TT drift and all TT-lowering events
4. Check floors (Stability 0 = collapse event) and ceilings (Mandate or Stability 7 = dominance event)
5. Award CP for Domain Actions and personal goals
6. Apply TC changes from threshold conditions

---

*End of Stage 6 compilation. Stage 7 (Territories: zone-based for TTRPG, territory properties shared with board game) follows.*




---



# PART SEVEN: TERRITORIES

Valoria comprises fifteen territories arranged in a roughly north-south layout, connected by an adjacency graph (not a hex map). Territories are the primary unit of control in board game and hybrid modes, and the geographic backdrop for TTRPG scenes. Each territory has a Prosperity score, a Fortification level, a starting controller, and at least one special property.

---

## 7.1 Territory Properties

Each territory tracks four attributes:

| Attribute | Scale | Meaning |
|---|---|---|
| Prosperity | 1–7 | Economic output; affects mustering Ob, Wealth generation, and population mood |
| Fortification | 0–3 (0–4 at Ehrenfeld) | Defense bonus; Fortification 2+ required for a siege to be declared |
| Control | Faction or Neutral | Which faction controls this territory and receives its benefits |
| Special Property | Fixed | Unique mechanical effect; does not change unless specifically altered |

**Control** transfers when one faction has the only military units present, or wins the most recent battle. Contested (multiple factions with units): no control benefits for anyone until resolved.

---

## 7.2 Territory Map

| # | Territory | Starting Control | Prosperity | Fort | Special Property | Adjacent |
|---|---|---|---|---|---|---|
| 1 | Valorsplatz (Capital) | Crown | 6 | 2 | Royal Court: Crown Decree −1 Ob here. Parliament: Hafenmark Influence −1 Ob here. | 2, 3, 5, 6 |
| 2 | Kronmark (Crown heartland) | Crown | 5 | 1 | Garrison: +1D Muster here. | 1, 3, 4 |
| 3 | Himmelstift (Cathedral city) | Church | 5 | 2 | Grand Cathedral: TC +1 per season Church controls this. Church Excommunicate −1 Ob here. | 1, 2, 6, 7 |
| 4 | Border Pass | Crown | 3 | 2 | Altonian Border: IP threshold events trigger here first. Invasion entry point. | 2, 5, 15 |
| 5 | Ehrenfeld (Military heartland) | Crown / Lowenritter garrison | 4 | 3 | Lowenritter Fortress: Lowenritter Martial Law −1 Ob here. Fortification maximum 4 (not 3). | 1, 4, 9 |
| 6 | Hafenstadt (Hafenmark capital) | Hafenmark | 6 | 1 | Ducal Court: Hafenmark Sovereign Authority may be invoked here. Major port. | 1, 3, 7, 8 |
| 7 | Sternhaven (Northern port) | Hafenmark | 5 | 0 | Trade Hub: all Trade orders +1D here. Schoenland sea route terminus. | 3, 6, 8 |
| 8 | Grauwald (Forest region) | Guilds | 4 | 0 | Timber and Mining: Guilds Trade +1D here. Difficult terrain: March costs 2 movement (not 1). | 6, 7, 10, 11 |
| 9 | Eisengrund (Southern highlands) | Varfell | 4 | 1 | Varfell Seat: Private Collection usable here only. Einhir ruins: Revolution Community Weaving −1 Ob. | 5, 10, 12, 13 |
| 10 | Schwarzmarkt (Underground trade) | Niflhel | 3 | 0 | Black Market: Niflhel Quiet Network −1 Ob here. All factions Trade here at +1 Ob (illicit goods). | 8, 9, 11 |
| 11 | Feldmark (Farming plains) | Guilds | 5 | 0 | Breadbasket: +1 Prosperity recovery per season if uncontested. Muster Ob −1 (willing recruits). | 8, 10, 14 |
| 12 | Sudwald (Southern forest) | Uncontrolled | 3 | 0 | Thread Wound: TT threshold events trigger here at TT −10 (earlier than elsewhere). Revolution informal presence. | 9, 13, 14 |
| 13 | Askeheim (Southernmost border) | Uncontrolled | 2 | 0 | Southernmost Access: required for Southernmost Expedition. Thread proximity: all non-Thread orders +1 Ob. TS 30+ characters: automatic Discovery Event per season present. | 9, 12 |
| 14 | Korntal (Southern farmland) | Revolution (informal) | 4 | 0 | Einhir Heartland: Revolution Influence −1 Ob here. Church Influence +1 Ob here (cultural resistance). | 11, 12 |
| 15 | Schoenland (Altonian trade port) | Neutral (Altonian trade) | 5 | 1 | Altonian Trade: +1 Wealth per season to any faction with Trade order here while route is open. Altonian spies: Intelligence orders here reveal results to Altonia. At IP 75+: Altonian vanguard deploys here. | 4, 7 |

---

## 7.3 Adjacency Notes

- **Valorsplatz (1)** is the most connected territory (4 adjacencies). Political hub; changes hands are maximum-consequence.
- **Schoenland (15)** connects to Border Pass by land and Sternhaven by sea. The sea route is severed when Schoenland trade suspends (IP 75+).
- **Askeheim (13)** is a dead end — only two connections. It is expedition territory, not strategic chokepoint.
- **Ehrenfeld (5)** is the Lowenritter's primary position. Its anomalous Fortification cap (4 instead of 3) reflects the order's entrenched presence.

---

## 7.4 Territory Control Mechanics

### Control Benefits (TTRPG/Hybrid)

A controlling faction treats the territory's Prosperity as a Domain Action resource. Controlled territories contribute to seasonal Wealth accounting and allow Muster actions.

A territory changes control when:
- A faction moves units in and no enemy units are present.
- A battle resolves with the defending faction's units destroyed or routed.
- A Govern order succeeds in an uncontrolled territory (first Govern = claim).

### Prosperity Dynamics

Prosperity changes through:
- Muster: −1 per muster action (labor and resources diverted).
- Conquest: −1 immediately (war damage).
- Govern Overwhelming success in own territory: +1.
- Breadbasket property (Feldmark): +1 per season if uncontested.
- Mine Collapse event: −1 permanent until Govern restores.
- Extended siege: −1 Endurance per season for garrisoned units; territory Stability affected.

Prosperity recovery rate (no active effects): +1 per season of peace if territory is controlled and not at Prosperity cap (7).

### Fortification

Built with Fortify orders. Maximum 3 for standard territories; 4 for Ehrenfeld only. Fortification level determines siege Ob and attack bonus for defenders (+1D per level to relevant defense rolls).

Fortification 2+ is required for a siege to be declared. Territories at 0–1 are assaulted directly.

---

## 7.5 Thread-Significant Territories

Three territories have Thread significance beyond their political properties:

**Sudwald (12):** A Thread Wound in the southern forest. TT threshold events fire here 10 TT points earlier than elsewhere. The Revolution's informal presence here is not coincidental — Einhir practitioners recognized the site's significance.

**Askeheim (13):** Proximity to the Southernmost creates ambient Thread pressure. All non-Thread orders suffer +1 Ob. This is the only territory from which the Southernmost Expedition can be launched (see §4.7, Southernmost).

**Eisengrund (9):** Einhir ruins beneath the Varfell highlands. The Revolution's Community Weaving is easier here (−1 Ob) because the configurational substrate retains resonance. Varfell's Private Collection access is tied to this site.

---

## 7.6 TTRPG Zone-Based Movement

In TTRPG mode, territories are not tracked with unit tokens. They function as named locations with associated properties. Movement between territories is narrative, not mechanical — the GM determines journey time based on terrain and circumstance.

For overland journeys of consequence (expeditions, supply runs, military marches), use the territory adjacency graph as a rough distance guide. Standard overland travel: one territory per day under normal conditions; Grauwald costs two days (difficult terrain).

Thread-significant territories require awareness: entering Askeheim or the Sudwald Thread Wound zone triggers the relevant passive effects on practitioners (automatic Discovery Events, TS growth checks) when applicable.




---



# PART EIGHT: COMBAT

Combat in Valoria uses simultaneous declaration with sequential priority resolution. Skill dominates over equipment. The system operates at two scales: **personal combat** (individual characters) and **mass combat** (military units). Both use the same dice engine. Thread operations interact with combat at Priority 1 (effects manifest) and Priority 5 (operations initiated).

---

## 8.1 Personal Combat

### Declaration Structure

Each round opens with a **Planning Phase**: each character declares one offensive action and one defensive posture simultaneously before any resolution occurs. Offensive actions resolve at their Priority; defensive postures apply reactively to all incoming attacks.

- No offensive action declared → character may declare two defensive postures instead.
- Move action as primary offensive → Dodge Backwards is the default defensive posture.
- Ranged character engaged in melee with no melee weapon drawn → defend at Agility only, Ob 2; draw backup weapon at Priority 4; use it at Priority 6.

### Initiative

Roll Agility dice, Ob 2. Higher net wins. The winner **declares last** — they hear the opponent's plan before committing. Ties: re-roll.

**Ambush**: Ob = ambusher's Tactics History + environment modifier (Ob 1–3). The defender's highest-Cognition character detects. On failure: attackers get one free Priority 2 round and initiative. On success: Agility vs Agility; defender's bonus successes from detection apply.

### Priority Table

| Priority | Action |
|---|---|
| **1** | Instant events; Thread operation effects manifesting from prior rounds |
| **2** | Ranged attacks (in order: arquebus, then crossbow, then drawn bow) |
| **3** | All melee attacks and manoeuvres (sub-rules below) |
| **4** | Standard actions (Diagnosis; draw backup weapon; non-combat single actions) |
| **5** | Full-round actions (the Leap; Forced Resolution; sustained movement) |
| **6** | Second actions; reload after firing |

#### Priority 3 Sub-Rules

**A — Manoeuvres resolve before attacks.** Disarm, Trip, Tie Up, Rescue, Reorient, Defend!, and Withdraw all resolve before standard attacks within Priority 3.

**B — Reach priority.** When a shorter weapon closes against a longer weapon, the longer weapon gets one priority attack before the shorter can reach. Hit: shorter weapon stops at 10'. Miss: shorter weapon closes regardless. Once both are at the same range, weapon speed determines order.

**C — Rescue limitation.** Rescue redirects melee attacks and Priority 4+ attacks only. It cannot redirect Priority 2 (ranged) attacks — those resolve before Priority 3. To absorb a ranged attack for an ally, physically interpose (declare yourself the target through positioning).

### Attacks

**Attack pool** = Combat History pool (primary attribute included). Use the pre-printed pool number.

**Defense options** (all defensive pools roll against Ob = attacker's net successes):

| Option | Pool | Notes |
|---|---|---|
| Dodge Backwards | Agility − armour penalty | Standard evasion |
| Duck and Weave | Agility − armour penalty | Higher-stakes evasion; Partial produces a complication |
| Parry | Combat History pool | Melee only. If Parry declared and ranged attack received: automatically switches to Dodge Backwards |
| Shield | Agility | Shield bonus applies |

### Damage

**Power + weapon damage bonus + excess attack successes − armour (minimum 0)**

Excess attack successes = attacker's net − defender's net (minimum 0).

*Example: Attacker net 5, defender net 3 → 2 excess. Power 3 + weapon +1 + 2 excess = 6 damage before armour.*

**Exploding damage**: A damage die showing 10 → re-roll. Failure on re-roll: +1 damage. Success: +2 damage and re-roll again. Continue until failure.

### Combat Manoeuvres (Priority 3A — all use Combat History pool)

| Manoeuvre | Versus | Effect |
|---|---|---|
| Defend! | Agility | Hold at bay; deny target's move action next round |
| Disarm | Agility vs Agility | Target drops weapon |
| Trip | Agility vs Agility | Target prone: −2D attack, attacks vs prone +2D, double cost to stand |
| Tie Up | Power | Lock weapons; no damage to either this round |
| Rescue | Endurance | Redirect melee / Priority 4+ attack from ally to self |
| Reorient | Cognition | Manipulate relative positioning; may establish or deny reach advantage |
| Withdraw | Agility | Sacrifice offensive action; re-establish reach advantage |

### Group Attacks

| Attackers | Bonus |
|---|---|
| 2 | +2D |
| 3 | +3D |
| 4 | +5D |
| 5 | +8D |

### Stunts

Player sets their own critical success range (up to 11–20); the critical failure range expands by the same amount. A result in neither zone: Partial, with a GM-assigned complication. Stunts are a player tool — the GM does not impose them.

---

## 8.2 Weapons and Armour

Weapons and armour provide modest modifiers. History pool (skill) dominates over equipment. This is intentional — a novice with a great sword loses to a skilled soldier with a knife.

### Weapons

| Weight | Damage Bonus | Reach | Speed | Notes |
|---|---|---|---|---|
| Light | +0 | Adjacent | Fast | Daggers, knives. Fastest in melee. |
| Medium | +1 | Adjacent / 5' | Standard | Swords, spears, maces. Baseline. |
| Heavy | +2 | 5'–10' | Slow | Greatswords, halberds. Reach priority advantage. |
| Ranged | +0 to +2 | Weapon-specific | — | Reload: Standard Action after firing (Priority 6). |

Weapon speed determines who resolves first when both are at the same range: Fast before Standard before Slow.

### Armour

| Type | Damage Reduction | Pool Penalty |
|---|---|---|
| None | 0 | — |
| Light | 1 | None |
| Medium | 2 | −1D Dodge / Acrobatics |
| Heavy | 3 | −2D Dodge; −1D Acrobatics |

**Special properties:**
- **Reach advantage** (spear, halberd): Functions as the longer weapon in all reach matchups, even against medium weapons.
- **Thread-locked item**: Fixed stats; cannot be degraded or destroyed through ordinary means.

---

## 8.3 Mass Combat

Mass combat operates at unit scale. Units are military formations with aggregate stats.

### Unit Sheets

| Stat | Scale | Meaning |
|---|---|---|
| Martial | 1–7 | Fighting effectiveness |
| Endurance | 1–7 | Staying power and morale under attrition |
| Cohesion | 1–7 | Willingness to take ordered actions rather than routing |

**Health = Endurance + 6.** Damage reduces aggregate Health; individual casualties are narrated, not tracked.

**All mass combat rolls: TN 5** (standard professional difficulty, regardless of weapon type or unit type).

### Standard Unit Types (on successful muster)

| Type | Martial | Endurance | Cohesion | Notes |
|---|---|---|---|---|
| Light Infantry | 3 | 3 | 3 | Default muster result |
| Heavy Infantry | 4 | 4 | 4 | Requires Prosperity 5+; Wealth Ob 2 |
| Cavalry | 4 | 3 | 5 | Requires Prosperity 6+ or relevant History; Wealth Ob 3 |
| Ranged | 3 | 2 | 3 | Requires relevant History or officer with Ranged proficiency |
| Artillery | 2 | 2 | 2 | Requires Wealth Ob 4 + 1 season construction |
| Knights Templar | 5 | 5 | 6 | Church asset only; not muster-raised; immune to Brutal morale effects; +1D Cohesion vs Thread events |

### Commander Contribution

The commanding officer's attributes directly modify unit rolls:
- Officer **Cognition**: adds dice to unit attack rolls.
- Officer **Presence**: adds dice to unit Cohesion checks.
- Officer **Memory**: allows one conditional order per round beyond standard declaration.

### Declaration Structure

Same simultaneous declaration as personal combat. Both sides declare:
1. **Disposition** (Balanced / Defensive / Offensive / Brutal)
2. **Manoeuvre** (Advance / Hold / Withdraw / Flank / Bombard)

### Disposition Interaction Table

Read: attacker's row, defender's column. Apply Ob and pool modifier to the attacker's pool (Martial + Commander Cognition ± modifier).

| Attacker \ Defender | Balanced | Defensive | Offensive | Brutal |
|---|---|---|---|---|
| **Balanced** | Ob 1, ±0 | Ob 2, ±0 | Ob 1, +2D | Ob 1, +1D |
| **Defensive** | Ob 1, −2D | Ob 2, −2D | Ob 1, ±0 | Ob 1, −1D |
| **Offensive** | Ob 1, +2D | Ob 2, +2D | Ob 1, +2D | Ob 1, +3D |
| **Brutal** | Ob 1, +2D +2 dmg | Ob 2, +2D +2 dmg | Ob 1, +2D +2 dmg | Ob 1, +3D +4 dmg |

*Ob 2 applies only when defender is Defensive. Brutal adds +2 flat damage on any success. Ob minimum 1. Each side attacks simultaneously using their own row-column result.*

### Formation Constraints

- **Defensive** requires Cohesion 3+ (green troops panic when ordered to hold).
- **Offensive** requires Martial 3+ (poorly armed troops cannot charge effectively).
- **Brutal** requires Cohesion 4+ (troops must be disciplined enough to commit atrocities on command). Brutal against a civilian population: automatic TC +1 if Church observes.
- **Flank manoeuvre** requires 2+ friendly units in the same engagement (one pins, one flanks).

### Unit Attachments (Optional Layer)

Attachments add one modifier per attachment without creating a sub-system. GM may omit this layer for minor engagements.

| Attachment | Effect | Requirement |
|---|---|---|
| Shield wall trained | +1D Cohesion checks when Defensive | Heavy Infantry only; 1 season training |
| Mounted scouts | May reveal enemy disposition before declaration | Cavalry only |
| Sappers | May attempt Fortification damage (see §8.4, Siege) | Wealth Ob 2; 1 season training |
| Practitioner attached | +1D Cohesion near Thread events; may perform Thread ops during battle | TS 30+ officer assigned |
| Banner bearer | +1D Rally attempts | Any unit; costs 1 officer slot |

On Formation Break: all attachments are lost for the remainder of the battle. A rallied unit regains base stats but not attachments.

### Formation Breaks and Routing

**Formation Break**: Unit's aggregate Health reaches 0. Health resets immediately; all subsequent actions at +1 Ob. Cohesion check required (Cohesion dice, Ob 2). Failure: unit **Routes**.

**Routed**: Cannot take ordered actions. Rally requires an officer with Cognition 4+ to spend their action (Presence roll, Ob 2).

Units that survive a battle gain +1 to a randomly selected stat, once per campaign season (veteran bonus).

### Three-Way Mass Combat

1. All three sides declare dispositions simultaneously.
2. Determine primary conflict (who is fighting whom); resolve secondary force declarations.
3. Apply disposition table for each attacking pair independently.
4. Resolve all attacks simultaneously using the standard priority table.
5. **Three-way initiative**: all three sides roll Cognition. Highest net declares last. Second highest declares second-to-last. Lowest declares first with least information.

A unit declaring Defensive that is not attacked by any force takes no damage and does not roll.

### Personal Actions During Mass Combat

Individual characters may take **Personal Actions** (duels, espionage, Thread operations) during a mass combat round. These resolve at **Priority 8** (after the round's main resolution) and are limited to **one resolved exchange** per mass combat round.

If the action requires more than one exchange, it continues as a scene after the mass combat round concludes.

**Contested Figures**: A named NPC rendered non-threatening through a personal action (Disarmed, Tripped) but not yet incapacitated becomes a Contested Figure. Both sides have a claim. Fate resolves as a scene after the mass combat round concludes.

**Social actions in mass combat**: Parleys, surrenders, and ultimata use the standard social rules. Default disposition for an enemy commander approached mid-battle: Cool (Ob 3). Adjust from there if prior relationship exists.

### Thread Operations in Mass Combat

Thread effects from prior rounds manifest at Priority 1 in the round they complete. Operations initiated at Priority 5 produce effects the following round.

TT multiplier for mass combat Thread operations: ×3 flat (replaces scale-based multiplier). TT gain from any single mass combat Thread operation is **capped at +15** regardless of calculation. Excess converts to narrative consequence (regional site destabilisation, Locked zone expansion) at GM discretion.

---

## 8.4 Siege

Sieges are multi-season extended actions. A siege may only be declared against a territory with Fortification 2+. Fortification 0–1 territories are assaulted directly using the standard mass combat procedure.

**Siege declaration**: An attacking force with Military ≥ defender's garrison Military may declare siege. Once declared, both sides enter the siege procedure.

### Siege Phases (One per Season)

Both sides choose one action per season:

**Attacker options:**

| Action | Roll | Effect on Success |
|---|---|---|
| Starve | Military vs Ob = Fortification level | Defender: −1 Endurance to garrison; −1 Stability to controlling faction |
| Assault | Military vs Ob = Fortification level + 2 | Success: breach attempt, mass combat at standard Ob. Overwhelming: walls breached, mass combat at −1 Ob for attacker |
| Sappers | Intelligence vs Ob = Fortification level + 1 | Fortification −1 (undermining). Detected on Partial/Failure: defender gets free Sortie |
| Negotiate | Influence vs defender's Mandate | Success: conditional surrender. Overwhelming: unconditional |
| Thread bombardment | Practitioner Weaving, Relational+ scale | Ob = Fortification level. TT +2 regardless. Success: garrison Cohesion −2. Overwhelming: Fortification −1. Failure: practitioner TD +3 |

**Defender options:**

| Action | Roll | Effect on Success |
|---|---|---|
| Hold | Cohesion Ob 1 | Garrison holds; no losses |
| Sortie | Military vs Ob = attacker garrison ÷ 2 | Success: attacker loses 1 unit or −2D to next siege action. Failure: sortie force destroyed |
| Relief call | Circles / Influence Ob 3 | Summons allied force; arrives in 1–2 seasons |
| Counter-negotiate | Influence vs attacker's Stability | Success: attacker accepts terms. Overwhelming: attacker withdraws (their Mandate −1) |
| Sabotage | Intelligence vs Ob = attacker Military ÷ 2 | Success: attacker supply disrupted; −1D to next action |

### Siege End Conditions

- Defender Stability reaches 0: garrison surrenders.
- Fortification reaches 0: walls breached; mass combat resolves immediately.
- Attacker withdraws (voluntary or forced by Relief).
- Negotiated settlement: both parties agree on terms.

### Co-Movement During Siege

Each season of siege: TT +1 (concentrated suffering and disruption).
Einhir site within the fortification: +1 additional TT per siege season.

### Personal-Scale During Siege

**PCs inside** may: run espionage (Intelligence Domain Action), negotiate with besiegers (Social scene), attempt escape (Agility + relevant History, Ob = Fortification level), or perform Thread operations (siege does not prevent contact).

**PCs outside** may: infiltrate (Agility/Intelligence, Ob = Fortification level + garrison commander bonus), join the assault, or perform Thread operations against the walls.

---

## 8.5 Supply Lines

Supply status is checked at seasonal accounting for each unit.

| Status | Condition | Effect |
|---|---|---|
| Supplied | Within 2 territories of friendly-controlled Prosperity 3+ | No penalty |
| Strained | 3 territories from supply, or supply territory Prosperity 1–2 | −1D to all rolls next season |
| Cut Off | No connected friendly territory with Prosperity 1+, or route blocked | −1 Endurance per season (cumulative); Cohesion check Ob 1 or −1 Cohesion |

**Supply route interdiction (Domain Action)**: Intelligence vs defender's Military ÷ 2. Success: one enemy supply route blocked 1 season. Overwhelming: blocked and undetected. Failure: detected; defender may reinforce.

**Foraging (officer Domain Action)**: Relevant History (Survival, Campaign Veteran, etc.). Ob 2 in fertile territory; Ob 3 poor; Ob 4 winter/mountain. Success: supply improves one step for 1 season. Failure: territory Prosperity −1, potential Revolution Influence +1.




---



# PART NINE: SOCIAL SYSTEMS

Social conflict in Valoria uses two primary structures: **Appeals** (one-roll persuasion targeting an audience) and **Debates** (multi-exchange formal contests between two orators). Both are shaped by Rhetoric style, Dispositions, and the Composure wound track. A third tool, the **Reading Exchange**, allows social perception before formal contest begins.

---

## 9.1 Composure and the Rattled State

**Composure = Presence + 6.** This is the social wound threshold. Strain accumulates during social conflict; it is not reduced between exchanges within the same scene unless Unmask occurs.

**Rattled** triggers the moment accumulated strain **first equals or exceeds** Composure. Stop tracking strain at that point — Rattled replaces the number.

- Rattled effect: −2D on all social rolls (Presence, Cognition, and Attunement pools).
- Combat is unaffected by Rattled.
- Persists until: Unmask, the scene ends, or the character rests.

**Unmask** is a player choice available at any point during a social scene:

- All strain clears; Composure restored to full.
- The character reveals something true — the player declares it, the GM confirms it is not already public.
- If mid-Debate: the current incomplete exchange is voided. Subsequent direct action in that scene: Ob = exchange deficit + 1 (minimum 1).
- The formal register breaks. The scene changes nature — a Debate cannot resume after Unmask; it becomes a personal confrontation or collapses.

---

## 9.2 Dispositions

Dispositions are qualitative relationship descriptors between two characters or between a character and an audience. They are **not modifiers** — they inform the GM's Ob-setting but do not add or subtract dice.

| Disposition | Approximate Ob |
|---|---|
| Friendly / Warm | 1–2 |
| Neutral | 2 |
| Cool | 3 |
| Hostile | 4 |
| Contemptuous | 5 |

Default disposition for an unestablished relationship: **Neutral (Ob 2)**. An enemy commander encountered mid-battle: **Cool (Ob 3)** — professional adversaries, not personal enemies.

Dispositions shift through play outcomes. An Overwhelming social success causes the GM to name a one- or two-step improvement in the target's disposition toward the speaker.

---

## 9.3 Rhetoric Framework

All social rolls belong to one of three rhetorical styles. The style applied must match the argument being made.

| Style | Domain |
|---|---|
| **Evidence Style** | Past actions, facts, records, historical precedents, accusations |
| **Character Style** | Present virtue, reputation, worth, shame, identity |
| **Consequence Style** | Future outcomes, what should be done, stakes of inaction |

**Style mismatch**: arguing a past-accusation using Consequence Style, or making a character attack using Evidence Style, is a categorical error. Apply −2D (minimum 1D remains). Stylistic creativity and unusual framings are not penalised — only clear categorical violations.

Orators may change style freely between exchanges. Mid-exchange style changes are not permitted.

### Resonant Style Tags

Each named NPC has one resonant tag (Evidence, Character, or Consequence) that reflects their dominant mode of reasoning. Addressing that NPC using their resonant style earns +1D.

Resonant tags are **not on player-facing materials.** Characters must discover them through investigation, prior social scenes, or Histories with relevant background. GMs should treat tags as a reward for preparation, not as a hidden penalty for guessing wrong.

---

## 9.4 Reading Exchange

A Reading Exchange is a social perception action available in the **first round of social contact only**. Once formal Debate positions are declared, Reading is no longer available.

**Pool**: Attunement + relevant History bonus. Attunement replaces the History's primary attribute for this roll only.

**TN**: 7 (standard).

**This is not a Debate Exchange**: it does not count toward exchange tally, does not produce Composure strain, and cannot be targeted by Inspiration attacks.

| Degree | Result |
|---|---|
| Overwhelming | GM describes opponent's emotional state, tells, and assessment confidence in detail. +1D on the first two formal Exchanges in the same scene. |
| Success | GM describes opponent's emotional state and one tell. +1D on the first formal Exchange in the same scene. |
| Partial | GM describes surface affect only (calm, nervous, defensive). No Exchange bonus. |
| Failure | No information. The opponent notices the scrutiny — they are aware of being read. |

**Note on pool construction**: The Reading Exchange uses Attunement as the base attribute. If using pre-printed History pools (which include a primary attribute), replace the primary attribute component with Attunement. The History bonus (points + 3) is unchanged.

---

## 9.5 Appeals

An Appeal is a single-roll persuasion attempt targeting an audience or individual. It does not use the exchange structure.

**Pool**: Presence + History bonus.

**Ob**: Set by the audience's resistance (use Disposition table in §9.2 as the primary guide; GM adjusts for situation).

| Degree | Result |
|---|---|
| Overwhelming | Audience persuaded; disposition improves one step; GM names one additional consequence in the speaker's favour |
| Success | Audience persuaded |
| Partial | Partial persuasion; audience requires something additional before acting |
| Failure | Audience unmoved; may harden against further Appeals |

**Appeal vs Debate interaction**: A successful Appeal does not reverse a Debate loss from the same scene. The Debate Compromise Rule (§9.6) applies only within Debates; Appeals and Debates occupy different social registers.

---

## 9.6 Debates

A Debate is a formal exchange of positions. Both orators roll simultaneously; each exchange is resolved independently.

**Pool**: Cognition + History bonus.

**Exchange counts by stakes:**

| Stakes | Exchanges |
|---|---|
| Casual | 1 |
| Formal | 3 |
| Grand Debate | 5 |

**Resolution per exchange**: both orators roll. More net successes wins the exchange. Loser takes Composure strain:
- +1 strain on a normal loss.
- +2 strain on an Overwhelming loss (opponent's net ≥ 2× loser's net, or loser rolls 0).

**Inspiration attack**: In an exchange where the attacker declares Character Style and names a specific Inspiration as target — if the defending orator achieves **net ≤ 0** (actual Failure, not merely losing), the named Inspiration loses 1 point. Losing the exchange with a positive net result does not trigger this. The targeted Inspiration must be known to the attacker; discovering Inspirations requires prior investigation or Overwhelming social success.

**Debate Compromise Rule**: A lost Debate does not reverse a prior Appeal from the same scene. These resolve on separate social registers.

**Domain Echo**: The winning orator's position generates any Domain Echo (see §11 on Domain Actions). The loser's position does not.

**Grand Debate total loss (5–0)**: The losing faction or character takes +1 Ob to social actions with the opposing faction for one season.

### Parliamentary Vote

When a political matter requires an institutional decision, resolve it as a Parliamentary Vote (see §8 Factions, §8.9). Parliamentary Votes use the Debate exchange structure (best of 3 exchanges), with faction pools substituting for personal pools. Players personally representing their faction may use the higher of their personal pool or their faction's pool.

---

## 9.7 Social Scale Summary

| Tool | Attribute | Structure | Strain | Scope |
|---|---|---|---|---|
| Reading Exchange | Attunement | Single roll, pre-contact | None | Perception only |
| Appeal | Presence | Single roll | None | Audience persuasion |
| Debate (Casual) | Cognition | 1 exchange | +1/+2 | Personal dispute |
| Debate (Formal) | Cognition | 3 exchanges | Cumulative | Institutional contest |
| Grand Debate | Cognition | 5 exchanges | Cumulative | Faction-level |
| Parliamentary Vote | Mandate / Reach | 3 exchanges (best of) | None (institutional) | Political decision |

---

## 9.8 Social Pools — Quick Reference

All social rolls use the standard pool construction (attribute + History bonus), with the following attribute substitutions:

| Roll Type | Base Attribute |
|---|---|
| Debate | Cognition |
| Appeal, Circles, Resources | Presence |
| Reading Exchange | Attunement |

If the History's primary attribute differs from the social attribute, use the social attribute as the base. The History bonus (points + 3) is unchanged regardless.




---



# PART TEN: ADVANCEMENT

Characters advance through two parallel systems: **Test Track** (automatic from play) and **Character Points (CP)** (awarded by the GM for Beliefs, Maxims, and domain-level achievements, spent on a structured menu). A third long-arc indicator, **Renown**, tracks cumulative dramatic achievement and unlocks narrative permissions without granting mechanical bonuses.

---

## 10.1 Test Track Advancement

Every History has a test track with two marks: **Challenged** and **Exceeded**.

**Challenged**: Earned when you succeed at a roll where Ob ≥ your base attribute score (not full pool). The threshold is against raw attribute, not pool size — a large pool doesn't make advancement harder, only failure does.

**Exceeded**: Earned on an Overwhelming success at the same or harder Ob threshold.

When both marks are filled: History advances +1 point. Both marks clear. Repeat.

**Test track is the primary advancement path.** CP spending on History advancement (§10.3) is a supplementary path for targeted growth, not the default.

---

## 10.2 CP Awards

The GM awards CP at seasonal accounting and at significant scene conclusions. CP is awarded for Beliefs and Maxims — never for session attendance or routine success.

### Belief Awards

| Belief Event | CP |
|---|---|
| Pursuing a Belief in a meaningful scene | +2 |
| Belief challenged by events | +2 |
| Belief genuinely revised in response to events | +4–5 (highest standard) |

Belief-revised awards (4–5 CP) require genuine revision — a character who held a Belief and was forced by events to change it in a way that costs them something. The GM judges this standard; players do not self-award.

**Completing a Belief**: Write a new Belief, or convert it to a new Inspiration at 1 point (no CP awarded on conversion — the conversion is the reward).

**Contested Beliefs**: If a Belief's pursuit creates a genuine tension with another character's Belief (player or named NPC), the GM may mark the Belief **Contested**. It cannot be pursued for CP until a scene makes the tension explicit and one character chooses a position. This is not a penalty — it is narrative pressure.

### Maxim Awards

| Maxim Event | CP |
|---|---|
| Maxim honoured at genuine personal cost | +1 |
| Broken Maxim re-established through reckoning scene | +2 |

A violated Maxim is marked broken. No CP for subsequent violations of the same Maxim while broken. Re-establishing requires a full scene of genuine reckoning — the character confronts what they did and why.

### Domain Action Awards

At seasonal accounting, the GM reviews Domain Actions and personal goals pursued during the season. No fixed amount — GM judgment. Guideline: 1–2 CP for a season of active engagement with faction goals; 3–4 CP for a season that genuinely altered the political situation.

---

## 10.3 CP Spending Menu

All purchases have narrative requirements. CP alone is insufficient — every purchase must be grounded in play. The GM confirms that the narrative requirements are met before the purchase takes effect.

| Purchase | Cost | Constraint | Narrative Requirement |
|---|---|---|---|
| Attribute +1 | Current score × 3 CP | Maximum 5 per attribute | Training, mentorship, or extended practice narrated |
| History +1 (beyond test track) | 3 CP | Total cap = Memory score | Identify specific experiences that built this skill |
| New History at 0 points | 5 CP | Must not duplicate existing History function | Origin scene with GM; establishes eligibility only (0 points = no pool bonus) |
| New Inspiration at 1 point | 4 CP | Total Inspiration value ≤ Spirit score | Name focus; narrate two scenes of genuine pursuit |
| Inspiration +1 point | 3 CP | Individual cap = Spirit score; total ≤ Spirit | Scene of sustained engagement with focus this season |
| New Knot (establish) | 2 CP | Total significant Knots ≤ Bonds score | Relationship must have been played this season |
| Knot +1 strain capacity | 3 CP | Max strain capacity per Knot = 5 | The relationship has been tested and endured |
| Circles +1D (permanent) | 4 CP | Max permanent bonus = Presence score | A season of active social investment in that faction |
| Resources +1D (permanent) | 4 CP | Max permanent bonus = Presence score | A season of commerce or estate management |
| Remove 1 Wound | 6 CP | Between seasons only | Narrated treatment: healer, rest, or Thread intervention |
| Approach Training | 8 CP | TS ≥ 30; must have witnessed ≥1 Thread operation | Replaces mentorship/breakthrough paths as CP-gated alternative |

**No CP purchase for**: TS growth, Intelligibility recovery, Certainty recovery, Thread Stability recovery. These are play-driven; they cannot be purchased.

**Approach Training note**: The 8 CP cost is intentional. Acquiring Thread sensitivity through CP should feel like a campaign milestone. Characters who qualify will have witnessed Thread operations and lived with the knowledge of the Thread's existence for at least one season before spending.

---

## 10.4 Inspiration Acquisition and Recovery

### New Inspiration (mid-campaign)

1. Player declares intent and names the focus.
2. Two scenes where the character actively engages with the focus (GM confirms engagement is genuine, not incidental).
3. After each scene: Spirit check TN 7, Ob 1.
   - Both succeed: Inspiration established at 1 point.
   - One succeeds, one fails: Inspiration established at 1 point with a **Complication Tag** (GM assigns a narrative condition — e.g., *"only while in Valorsplatz"* or *"contingent on Lenneth's survival"*).
   - Both fail: focus not yet crystallised. Retry next season with new scenes.

**CP shortcut (G-053):** 4 CP + one scene of genuine engagement + one Spirit check. Success: Inspiration at 1 point, no Complication Tag. Failure: 4 CP spent; retry next season.

### Recovery (from reduced value)

- Full scene engaged with the focus: +1 point. No roll required.
- Focus physically present and uncontested: automatic +1, no check. (Seeing a loved one safe after battle restores the Inspiration without requiring a scene structure.)
- Maximum recovery per season: 2 points per Inspiration. Full restoration in one season is not possible.

### Focus Destroyed or Permanently Lost

When an Inspiration's focus is permanently destroyed, captured, or fundamentally changed such that engagement is no longer possible:

1. Inspiration drops to 0 immediately.
2. Player may convert to a new Inspiration through a **Grief Scene**: one scene of genuine reckoning with the loss + Spirit check TN 7 Ob 2.
   - Success: new Inspiration at old value −1 (minimum 1). New focus must thematically connect to the loss.
   - Failure: Inspiration lost entirely.

**CP conversion**: Completing a Belief converts it to an Inspiration at 1 point without cost. An NPC whose relationship with the character reaches significant depth (GM discretion) may become an Inspiration focus.

---

## 10.5 Renown

Renown is a campaign-long counter that tracks a character's growing reputation. It accumulates through dramatic Belief resolution and significant public actions. It unlocks narrative permissions — access that would otherwise require Circles rolls against high Ob.

**Renown does not grant mechanical bonuses.** It does not add dice, reduce Ob, or replace any other system. It grants social access.

### Accumulation

Renown increases by +1 when:
- A Belief is completed through dramatic action visible to a significant audience (a court, a battle, a public declaration).
- A Domain Action produces a result that changes the political situation and is publicly attributed to the character.
- A named NPC with faction standing publicly acknowledges the character's role in an event.

Renown does not increase from private actions, successful but quiet operations, or Belief revision.

### Permissions

[EDITORIAL: Full permission table requires design — only one data point exists (Renown 6 = Audience with the Monarch bypasses Circles). The table from Renown 1 to Renown 10 needs to be established, specifying what access each tier unlocks for each faction.]

**Confirmed ruling (from stress test):** Renown grants social permissions (bypasses bureaucratic access rolls) but does not replace Circles. A character with Renown 10 can request an audience with the monarch without a Circles roll but still needs Circles to locate an unknown contact. These are different social functions.

---

## 10.6 Advancement Summary

| System | Driver | Pace | Output |
|---|---|---|---|
| Test Track | In-play success at difficult Obs | Session | History +1 point |
| CP Awards | Belief pursuit, Maxims, Domain Actions | Season | CP pool |
| CP Spending | Player choice from menu | As available | Attributes, Histories, Inspirations, Knots, Access |
| Renown | Public dramatic achievement | Campaign arc | Narrative permissions |

### Seasonal Accounting Checklist (Advancement Steps)

At end of each season, in order:
1. Check test tracks — advance qualifying Histories.
2. Award CP (GM): Belief events this season, Maxim events, Domain Action recognition.
3. Process any CP purchases declared before accounting (attribute/History/Inspiration).
4. Award Renown for qualifying public actions this season.
5. Check Renown permission unlocks (if any new tier crossed).




---



# PART ELEVEN: SCALE TRANSITIONS

Valoria operates across five scales simultaneously. A single session may move from personal combat to Thread operations to faction-level consequences within the same scene. The transition system provides vocabulary and eight formal handoff rules to manage these crossings without losing mechanical coherence.

---

## 11.1 Scale Table

| Scale | Example | Base Ob | TT Multiplier (Thread operations) |
|---|---|---|---|
| Object | One item; one wound; a mechanism | 1 | ×1 |
| Personal | One person; a character | 2 | ×1 |
| Relational | Small group; a social agreement; an officer and their unit | 3 | ×2 |
| Territorial | A duchy; a district; a settlement | 4 | ×3 |
| Structural | A kingdom; an institution; a lasting constitutional arrangement | 5+ | ×5 |

Base Ob applies when a Thread operation targets configurations at that scale. TT multiplier applies to TT gain from the operation.

---

## 11.2 Vocabulary

These terms are used consistently throughout the rules. Each names a specific moment of scale-crossing:

**Zoom In** — the GM narrows focus from a larger scale to a smaller one:
*"Dav, you spot the Niflhel officer in the Templar formation. You have one exchange. Zoom in."*

**Zoom Out** — the GM widens focus back to the larger scale after smaller-scale resolution:
*"The duel ends. Zoom out — the battle has continued while you fought."*

**Register Shift** — a social scene changes its fundamental nature:
*"Serena's Unmask breaks the formal register. We're no longer in a Debate — the King is your audience now."*

**Domain Echo** — the moment when a personal success ripples up into a faction-level consequence. No separate roll or action required:
*"That testimony lands. Domain Echo — Church Mandate drops to five."*

---

## 11.3 Eight Handoff Rules

| Transition | Handoff Rule |
|---|---|
| Personal → Thread | The Leap action triggers the transition. Contact duration begins on the round the Leap succeeds. |
| Personal → Faction | The GM recognises faction-level scope and resolves a Domain Action from the same roll. Personal Ob resolves first; Domain Action Ob second. |
| Personal → Scene | A personal roll made before an audience may serve as the opening move of a social scene, or as the Appeal itself. |
| Scene → Faction | An Appeal or Debate that succeeds at sufficient scope produces a faction-attribute change via Domain Echo. |
| Thread → Faction | When a Thread operation targets a faction-level configuration, it resolves as a Domain Action using the Thread pool and appropriate Ob. No separate roll. |
| Thread → Mass | Thread effects manifest at Priority 1 in the round they complete, regardless of when the roll was made. |
| Mass → Personal | Any character may take a Personal Action at Priority 8. Limit: one exchange per mass combat round. Non-incapacitated named targets become Contested Figures. |
| Scene → Mass | Social scene outcomes in combat contexts affect the mass combat's opening state; applied before the next round's declaration phase. |

---

## 11.4 Scope Shift

A character may shift scope once per round, declared at the start of their turn. Verbal declaration only — no roll.

One action per round per scope. Taking an additional action in a different scope within the same round costs +1 Inspiration (spend before rolling).

---

## 11.5 Domain Actions

When a personal action has faction-level scope, the GM recognises it as a Domain Action. The personal roll resolves the personal outcome; the same roll simultaneously resolves the faction-level effect.

**Domain Ob** = target faction's relevant stat (1–7 scale, no division). A personal Debate against a faction representative uses the faction's Mandate as Ob for the faction-level consequence, even though the personal roll uses Disposition Ob for the interpersonal outcome.

**Domain Echo** fires automatically from any roll that crosses scales. Players do not declare it — the GM recognises scope and announces the echo.

**Seasonal cap**: Faction attributes may not change by more than ±2 per season regardless of how many Domain Actions or Domain Echoes target them. This cap is shared across TTRPG and board game modes in hybrid play.

---

## 11.6 Inert Knowledge

When a Thread-sensitive character explains Thread-level reality to a non-sensitive character, the non-sensitive character gains the information propositionally but cannot act on it with Thread-level precision.

Mark such information as **Inert Knowledge** on the non-sensitive character's sheet. They can recite it but it has no mechanical consequence until they develop sufficient sensitivity to render it as genuine knowledge.

This is not a punishment — it is a mechanical expression of the epistemological barrier the Foundations establish. The information is real; the capacity to use it is what's missing.

---

## 11.7 Mode-Specific Scale Behaviour

| Scale Context | TTRPG | Board Game | Hybrid |
|---|---|---|---|
| Mass combat resolution | Zone-based operational; Zoom In/Out for personal moments | Disposition table, single roll per battle | Board game resolution; Zoom In to TTRPG for key named-NPC moments |
| Siege resolution | Multi-season procedure with scenes (§8.4) | Siege order vs Fortification (single roll) | Board game roll; TTRPG scenes for infiltration or breakout |
| Domain Actions | Implicit — GM recognises scope from personal roll | Explicit — Order Set with placement and resolution | Strategic Phase uses board game orders; Personal Phase uses TTRPG Domain Echoes |
| Thread → Faction transitions | Standard handoff rule (Thread pool, faction-scale Ob) | Faction-card Thread orders (Weave/Investigate/Harvest) | Personal Phase: TTRPG. Strategic Phase: board game. Both count toward seasonal TT. |

**Key principle for hybrid**: Where a rule exists in both modes, the seasonal cap is shared. A faction attribute cannot change by more than ±2 per season regardless of how many sources target it in either phase.




---



# PART TWELVE: CAMPAIGN MODES

Valoria is designed to be played in three distinct modes. Each mode uses the same faction stats, three clocks, Thread mechanics, and setting. What differs is the resolution layer, the dominant scale of action, and the time-per-session rate.

---

## 12.1 TTRPG Mode

### Session Structure

A TTRPG session covers one dramatic arc, typically one or two scenes within a season. Seasons are not compressed — they are zoomed into, explored through personal scenes, and resolved through Domain Echoes at seasonal accounting.

**Typical session flow:**

| Phase | Duration | Content |
|---|---|---|
| Opening | 10 min | Recap, clock positions, active Beliefs reviewed |
| Scene 1 | 60–90 min | Primary dramatic scene (combat, social, Thread operation, investigation) |
| Scene 2 (optional) | 45–60 min | Secondary scene driven by Scene 1 consequences |
| Accounting | 15 min | Apply Domain Echoes, advance clocks, assign CP |

**Season pacing**: One season typically spans 1–2 sessions. GMs may compress quiet seasons (no active Beliefs pursued, no clock thresholds crossed) into a single accounting beat without running scenes.

**Campaign scale**: A full TTRPG campaign of 10–15 seasons runs 15–25 sessions.

### Session Zero Protocol

1. Answer 10–15 Editorial Questions establishing sensory texture, NPC motivations, and faction starting postures.
2. Set Safety Tools.
3. Create Characters: 3 Histories at 2 points each; 18 attribute points; declare 3–5 Knots.
4. Set clocks: TT 28, TC 15, IP 20.
5. Review the Action Economy and Scope Shift procedure.
6. Confirm the campaign's primary structural questions: which clocks are the PCs best positioned to address, and in which direction?

### TTRPG Endgame

There is no explicit victory condition. The TTRPG campaign ends when the GM and players agree the central dramatic questions have been resolved or exhausted. Endgame is emergent, not mechanical.

**Endgame indicators (GM guidance — not triggers):**
- All PCs have resolved or abandoned their central Beliefs.
- TT has been reduced below 20 or has exceeded 80 (the world is saved or doomed).
- The succession crisis has resolved (Torben, Elske, Parliament, or coup).
- The Church's authority is broken or triumphant (TC below 20 or above 80).
- Altonia has invaded or been permanently deterred.
- At least one PC has died, retired, or fundamentally transformed.

The GM should signal endgame 2–3 sessions before the final session: *"We're approaching the end of this story. What does your character want to resolve?"*

---

## 12.2 Board Game Mode

### Session Structure

The board game covers 3–5 seasons per session. A full 10-season campaign plays in approximately one session of 2–4 hours.

**Typical session flow:**

| Phase | Duration | Content |
|---|---|---|
| Setup | 10–15 min | Faction assignment, starting stats, clock positions, first-season orders |
| Season loop × 3–5 | 25–40 min each | Planning → Resolution → Accounting |
| Endgame check | 5 min | Victory condition evaluation |

### Board Game Endgame

Victory conditions are checked at the end of each season's accounting phase.

**Shared loss condition (all modes):** TT reaches 100. The Rupture. No faction wins.

**Additional endgame triggers:**
- Season 10 reached: highest point total wins.
- 3+ factions collapse (Stability 0): remaining factions share a diminished victory.

**Tiebreak:** Stability — the most internally coherent faction endures.

---

## 12.3 Hybrid Mode

### Session Structure

One hybrid session covers one in-game season, minimum. A season may span multiple sessions if scene volume warrants; seasonal accounting fires at the end of the session in which the season closes, not mid-session.

Each session runs three phases in sequence:

| Phase | Duration | Content |
|---|---|---|
| Personal Phase | 90–150 min (scene-dependent) | TTRPG scenes. Board game paused. |
| Strategic Phase | 20–30 min | Board game orders placed and resolved. TTRPG paused. Downtime actions declared and resolved concurrently. |
| Cascade Phase | 10–20 min | Domain Echoes applied, Thread consequences, clock threshold checks, seasonal accounting (if end of season), board state update. |

**Quiet season:** GM may compress to Strategic + Cascade only (~30 min) when no TTRPG scenes are dramatically necessary.

**Extended season:** GM may split one season across 2 sessions when TTRPG scene volume demands it. Strategic Phase defers to session 2.

### Pacing Controls

**Zoom In is player-initiated.** Any board order that resolves entirely between NPCs does not generate a TTRPG scene. The GM narrates the outcome so players have the information before their next scene.

**Scene trigger conditions.** An order generates a mandatory TTRPG scene if:
- A PC is the target or perpetrator of the order's primary action
- A PC's named Knot or Inspiration focus is directly affected
- A clock threshold is crossed as a direct result and a PC is present in the affected territory

**NPC-order sequencing.** Within the Strategic Phase, NPC-only orders resolve first. Their outcomes are narrated before player-involved scenes begin. This ensures player scenes impacted by prior NPC action occur in the correct narrative order.

### Information Asymmetry (Fog of War)

All faction stats are displayed to non-owning players in four qualitative states:

| Display | Underlying value |
|---|---|
| In ruins | 1 |
| Poor | 2–3 |
| Good | 4–6 |
| Excellent | 7 |

**Boundary ambiguity (value 4):** Roll 1d6 at point of observation — 1–3 = Poor, 4–6 = Good. Result is fixed for that scene; re-rolled at next observation.

**Faction-leader PCs** see their own faction's exact numerical values at all times.

**Intelligence stat** is always hidden for rival factions regardless of display tier. Revealed only through successful Intelligence Domain Actions or TTRPG scene discoveries.

### Cross-Mode Handoffs

**Default:** All TTRPG personal-scene consequences batch to the Cascade Phase. GM tracks on a ledger during Personal Phase and applies in bulk. An inline exception is permitted for single-stat changes with no threshold risk — GM discretion only, not a player option.

**Thread operations in hybrid:** Personal-scale Thread operations during the Personal Phase resolve as TTRPG narrative consequences. Clock and tracker effects (TT, ThS, Coherence, co-movement) are noted by the GM and batched to Cascade. A faction-scale Thread order (Weave/Investigate/Harvest on the board) represents a collective premeditated operation — it resolves under board game rules and generates a Co-Movement Card draw, not personal co-movement effects. The two tracks are parallel.

**Flashbacks** are Personal Phase only. A Flashback may not alter any board game state resolved in the Strategic Phase of the same or any prior session.

**Resources/Wealth interaction.** When a PC spends Resources during a TTRPG scene, evaluate at Cascade:
- Faction Wealth ≥ 2× Resources rolled → no faction Wealth impact.
- Faction Wealth < 2× Resources rolled → Faction Wealth **stressed** (−1, recovers next season).

Same threshold logic applies to Circles vs. Influence. Flag for stress testing: 2×−1 variant may be needed at edge values.

### Siege Protocol

Sieges run at board game scale across multiple seasons. TTRPG scenes fire during a siege when:
1. **Players seek contact** — players choose to engage a named opponent (hunting a general, attempting to negotiate surrender). Generates a mandatory TTRPG scene at player initiative.
2. **Mechanical trigger** — a named NPC's mass battle unit attacks a PC's mass battle unit. Generates a mandatory Zoom In.

All other siege activity resolves at board game scale without Zoom In.

### Southernmost Expeditions in Hybrid

Only relevant if the expeditioning PC is a faction leader.

If another PC can proxy: that PC executes faction orders during the Strategic Phase for the expedition duration. The absent PC retains faction leadership narratively.

If no PC can proxy: the faction runs on NPC AI logic. The absent faction leader may send one Belief-level directive per season, which the AI prioritises unless it conflicts with faction survival logic.

The expedition PC continues Personal Phase scenes normally throughout.

### Cascade Phase — Full Procedure

The Cascade Phase is GM-controlled. Players do not take actions. Work through in order:

1. **Domain Echoes** — apply all TTRPG personal-scene consequences from the GM ledger to faction stats on the board.
2. **Thread consequences** — apply co-movement clock/tracker effects from any Thread operations this session (TT changes, ThS loss, Coherence changes).
3. **Clock checks** — check TT, TC, IP against thresholds. Fire threshold events in order: TT first, TC second, IP third. Queue institutional responses for next Personal Phase.
4. **Seasonal accounting** *(end of season only)* — faction stat changes from board orders, Knot strain ticks, ThS recovery (+2 if no Thread ops this season), Coherence recovery (Corrective Weaving results), CP awards, test track advances.
5. **Board state update** — GM updates the board to reflect all of the above. This is the final state visible at the start of the next Strategic Phase.

The Cascade Phase is not skippable. If nothing fires in steps 1–3 and it is not end of season, steps 4–5 abbreviate to board update only.

### Clock Synchronisation

All three clocks (TT, TC, IP) advance only in the Cascade Phase. No clock advances mid-Personal Phase or mid-Strategic Phase. All clock changes batch to Cascade step 3.

### Hybrid Endgame

Victory requires satisfying both personal and strategic conditions simultaneously.

**Hybrid victory:** A faction achieves its board game primary victory condition AND the faction leader PC has resolved their central Belief arc in a way that supports the victory. If the board game condition is met but the PC's Belief arc contradicts it, the victory is **hollow**.

**Hollow victory:** Player may accept (mechanical win, narrative loss) or reject (continue until personal arc resolves, risking mechanical erosion). Player choice, not a rule.

**Hybrid loss:** TT 100, or faction collapse with no personal resolution.

---

## 12.4 Hybrid Timing Reference Table

| Measure | TTRPG | Board Game | Hybrid |
|---|---|---|---|
| 1 real session (~3–4 hrs) | 2–4 scenes (1 season or less) | 3–5 seasons | 1 season (all four phases) |
| 1 game season | 1–2 sessions | ~15–20 min | 1 session |
| Full campaign (10 seasons) | 15–25 sessions | 1 session (2–4 hrs) | 10–15 sessions |

---

## 12.5 Mode-Specific Rule Branching

Where the three modes diverge mechanically:

### Combat

| Rule | TTRPG | Board Game | Hybrid |
|---|---|---|---|
| Personal combat | Pool split, priority table, reach, maneuvers | Not applicable | TTRPG rules during Personal Phase |
| Mass combat | Zone-based operational; Zoom In/Out for personal moments | Disposition table, single roll per battle | Board game resolution; Zoom In to TTRPG for named-NPC moments |
| Siege | Multi-season procedure with scenes (§8.4) | Siege order vs Fortification (single roll) | Board game roll; TTRPG scenes for infiltration or breakout |

### Social

| Rule | TTRPG | Board Game | Hybrid |
|---|---|---|---|
| Debate/Appeal | Full social combat (exchanges, Composure, rhetoric) | Not applicable | TTRPG rules during Personal Phase |
| Negotiation | Roleplay + social roll | Treaty order (mechanical) | Treaty order triggers TTRPG social scene if both parties are PCs |
| Excommunication | Grand Debate (5 exchanges) | Single roll (Church Mandate vs target) | Board game roll; TTRPG scene for the trial if desired |

### Faction

| Rule | TTRPG | Board Game | Hybrid |
|---|---|---|---|
| Domain Actions | Implicit — GM recognises faction-scope from personal roll | Explicit — Order Set with placement and resolution | Strategic Phase uses board game orders; Personal Phase uses TTRPG Domain Echoes |
| Stability checks | Triggered by Domain Echo consequences | Triggered at Accounting | Batched to Cascade Phase |
| Seasonal cap | ±2 per attribute per season | ±2 per attribute per season | Shared — applies across both phases |

### Thread

| Rule | TTRPG | Board Game | Hybrid |
|---|---|---|---|
| Thread operations | Personal-scale (Weaving, Pulling, Leaps) with full narrative | Faction-scale (Weave/Investigate/Harvest orders) with Co-Movement Card | Personal Phase: TTRPG Thread ops. Strategic Phase: board game Thread orders. Both count toward seasonal TT. |
| Co-movement | Version C (automatic deterministic + actual d6) | Co-Movement Card deck (15 cards) | Personal Phase: Version C. Strategic Phase: Co-Movement Cards. |
| Discovery Events | Full narrative scene | Attribute change only (no scene) | TTRPG scene triggered by board game Discovery Event |

### Advancement

| Rule | TTRPG | Board Game | Hybrid |
|---|---|---|---|
| CP spending | Full menu (§10.2) | Not applicable — faction attributes change, not character skills | TTRPG CP spending during Personal Phase only |
| Faction attribute changes | Domain Echoes at seasonal accounting | Order resolution at Accounting | Both — cumulative, shared seasonal cap |
| Renown | Tracked per character | Not tracked (faction Mandate substitutes) | TTRPG Renown tracked; informs board game Mandate via Cascade Phase |

### Clocks

| Rule | TTRPG | Board Game | Hybrid |
|---|---|---|---|
| TT/TC/IP advance | At seasonal accounting | At Accounting | At Accounting (Cascade Phase) — identical |
| Threshold events | GM narrates and runs scenes | Event card or table lookup | Board game trigger; GM may run TTRPG scene for narratively significant thresholds |

**Key principle:** Where a rule exists in both modes, the seasonal cap is shared. A faction attribute cannot change by more than ±2 per season regardless of how many Domain Echoes (TTRPG) and orders (board game) target it. This prevents hybrid mode from doubling attribute velocity.

---

## 12.6 The GM as Rendering Engine

For non-sensitive characters, the GM presents the ontical world — things as they appear. For sensitive characters, the GM layers ontological information beneath the ontical presentation: faint thread-structures visible beneath surfaces, distortions around monstrous presences, warmth or tension at knot-points.

The information asymmetry is the mechanic. It mirrors the epistemological barrier the Foundations establish as metaphysically principled, not institutional.

**Inert Knowledge.** When a sensitive character explains thread-level reality to a non-sensitive character, the non-sensitive character gains the information propositionally but cannot act on it with thread-level precision. Mark such information as *Inert Knowledge* on the non-sensitive character's sheet — they can recite it but it has no mechanical consequence until they develop sufficient sensitivity to render it as genuine knowledge.

### Co-Movement at the Table

When a thread operation resolves, the GM:
1. Describes the primary intended effect.
2. Determines one secondary consequence in an untargeted dimension (two consequences for Past-Oriented Pulls).
3. Narrates the secondary consequence as part of the scene.

This is not optional. The inseparability principle is the framework's foundational mechanical claim. Every operation has co-movement. It need not always be mechanically weighty — a small temporal flicker, a slight epistemic shift in how something is remembered — but it must always be present.

### TT Threshold Events

When TT crosses a threshold, the GM determines a narratively appropriate consequence from the current situation. No event deck. The current political, social, and thread-level state of the world should generate the threshold consequence organically.

---

## 12.7 The TD Track as Campaign Arc

The Temporal Disjunction track is not a per-session tactical resource. It accumulates over the course of the campaign. Thresholds represent campaign stages:

| TD | Stage | Character experience |
|---|---|---|
| 1–5 | Dissonant | Early-campaign. Unsettling but manageable. |
| 6–10 | Fragmented | Mid-campaign cost of active practice. Memory becomes unreliable. |
| 11–15 | Fractured | Late-campaign pressure. Significant price for continued practice. |
| 16–19 | Severed | Endgame condition. Approaching the limits of what continued work costs. |
| 20 | Crisis | The practitioner must choose: withdraw, resolve, or accept the consequences. |

An active practitioner working at Relational+ scale through a full campaign will reach Fragmented by mid-campaign and approach Fractured by the end. This is the game's structural statement about the cost of sustained Thread work.

---

## 12.8 Running the Noble-Church Triangle

The three-way relationship between Baralta (Church-devout, anti-overreach), Vaynard (anti-Church, knowledge-seeking), and Confessor Himlensendt (theocratic consolidation) generates political action without requiring predetermined outcomes. Track seasonal accounting. Apply triggers consistently. Outcomes emerge from the configuration.

**The excommunication scenario.** If Olafsson opens a Heresy Investigation against Baralta: Grand Debate, 5 exchanges. Church represented by Olafsson (Composure 7, pool: Church Reach 7 + Ecclesiastical Law). If it succeeds: Mandate −2, TC +3, TC suppression removed. If players defend her or supply documentary evidence: the investigation can be derailed or reversed.

**The Vaynard revelation.** When a practitioner tells Vaynard what his TS 14 means: structured social scene. Vaynard makes a Reading Exchange (pool: Cognition 4D, TN 7). If the practitioner wins or presents corroborating evidence: Vaynard accepts and enters his TK-level response. If Vaynard wins: he files the claim as unverified but highly interesting and begins watching the practitioner.

**The Crown's choice when Vaynard is exposed.** Resolved as a Parliamentary Vote (§7.4):
- Defend Vaynard: TC +2; Crown-Church relations fracture; Baralta must choose sides.
- Yield to Church justice: TC −1; Crown loses intelligence asset; Southernmost access collapses; Vaynard's succession leverage dissolves unpredictably; Baralta's Church-boundary cooperation secured for the following arc.




---



## 12.9 Hybrid Consequence Rules

### PC Death and Faction Succession

On PC death: the faction enters **Crisis** (−1 to all faction stats for one season; no floor during Crisis).

Player chooses one of three succession options — resolved within the same Cascade Phase:

1. **Take over an existing faction-loyal NPC.** That NPC becomes a full PC with their existing stat block. No newly generated characters.
2. **Designate another PC as successor** (requires that player's agreement). The dying player then begins a new personal character unaffiliated with the faction.
3. **Faction passes to a named NPC** (GM-controlled). Dying player begins a new personal character unaffiliated with that faction.

If no option is chosen within the Cascade Phase, option 3 defaults automatically.

### Faction Collapse and Personal Characters

A PC whose faction collapses continues as a personal character. They lose all dice bonuses derived from that faction (Circles dice tied to the faction, any faction-stat-derived pool modifiers). Personal attributes, Histories, Knots, Inspirations, and Beliefs are unaffected. Founding or joining a successor faction is a narrative path available through play.

### Downtime in Hybrid

Downtime activities (training, Inspiration recovery, Knot repair, Approach Training practice) run concurrently with the Strategic Phase. PCs may declare and resolve downtime actions during the Strategic Phase without consuming Personal Phase time.

### Advancement from Board Game Play

Board game successes generate CP and personal advancement. The character performed those actions; zoom level does not affect whether the experience counts. CP awards use the same criteria as TTRPG play (Belief engagement, significant Domain Action, Maxim expression). GM adjudicates at Cascade Phase seasonal accounting.

### Knot and Inspiration Consequences from Board Events

Mechanical consequences to Knots and Inspirations from board events are **gated by information**. They do not apply until the PC learns about the event in a TTRPG scene.

**Exception:** If the very next TTRPG scene after the board event is directly and immediately connected to that event (PC witnesses the death, or the scene opens in the immediate aftermath), the consequence applies at scene open. Time has not passed; the gating condition is met by the scene itself.

In all other cases — subsequent sessions, time skip implied — the consequence applies at the moment of in-scene discovery.


# PART THIRTEEN: NAMED NPCs AND INSTITUTIONAL ACTORS

Every named NPC in Valoria has a **Resonant Style** tag (Evidence, Character, or Consequence). Using that style earns +1D on social rolls targeting them. Tags are not listed on player-facing materials — discover them through investigation, observation, or prior scenes.

Named NPCs follow their Beliefs regardless of wound state. They do not withdraw when outmatched unless their Beliefs permit it.

---

## 13.1 Named NPCs — Crown

---

### King Almud Almqvist
*"The Golden Lion" · "The Golden King"*

**TS:** 28 (high Dormant; near Stirring threshold). Does not know the name for what he experiences. Attributes felt impressions to spiritual intimation. A Discovery Event would be the most destabilising moment of his reign.

**Social Profile:**
- Composure: 11 (Presence 5 + 6)
- Dominant Conviction: Order — legitimate authority through proper institutional channels
- Resonant Style: Consequence — long-horizon thinking; past injustice moves him less than future structural risk

**Beliefs:**
1. *"Valoria's survival depends on the trade relationship with Altonia. I will hold it open regardless of what it costs me."*
2. *"The informal caste against southern Einhir is wrong. I cannot act on that conviction without destroying the coalition that holds the kingdom together. I will not act until I find a path that doesn't require choosing between justice and the monarchy."*
3. *"My son must be ratified before the succession becomes a weapon."*

**The Sovereign Constraint.** Almud's inaction on the Einhir question is structural, not weakness. Acting requires him to simultaneously contradict Church doctrine (TC +3), alienate northern Einhir nobility (Mandate −2), and invite Altonian diplomatic challenge. The constraint erodes only when one or more of these costs is removed by events.

**TS at the table.** In scenes with Thread-significant objects or practitioners at Coherence 7 or below, the GM may privately note that Almud experiences an impression he cannot name. TS 30+ practitioners who succeed on a passive perception check notice the King's threads register faint sensitivity. He does not know they see it.

---

### Queen Lenneth Almqvist

**TS:** 0 (Inert). Not foreclosed — simply never confronted.

**Social Profile:**
- Composure: 10 (Presence 4 + 6)
- Dominant Conviction: Liberty — the concrete political conditions under which people can act without requiring institutional permission
- Resonant Style: Consequence

**Hidden networks.** Maintains a third-party cultural foundation funding People's Revolution academic work (including Edith Varn's project) through a retired magistrate. The paper trail does not reach the Crown. She has sea-republic archive access to a pre-Altonian coastal survey — a document a TS 50+ practitioner would recognise as a first-person thread-perception account from approximately 180 years ago.

---

### Prince Torben Almqvist — Heir, Early Teens

**TS:** 8 (near-Inert). Has had three unexplained experiences in five years but has no framework for them.

**Starting state:** In Valoria. Becomes available for Altonian education demand at IP 30.

**Torben Loyalty Clock.** Starting value: 8 (loyal to Valoria). See §7.x (Succession Mechanic) for full procedure.

| Loyalty | State | Mechanical Effect |
|---|---|---|
| 8–6 | Homesick, resistant | No effect. Retrieval straightforward. |
| 5–4 | Adapting | Crown Mandate −1. Retrieval requires Altonian consent or covert extraction. |
| 3–2 | Altonia-aligned | Crown Mandate −1 again (cumulative −2). Löwenritter coup trigger #2 arguably met. |
| 1 | Altonian puppet | If he inherits: Crown becomes Altonian vassal state. Coup trigger #2 definitively met. |

---

### Princess Elske Almqvist

**Starting state:** Married to an Altonian Duke holding territory adjacent to Border Pass. Embedded in Altonian society. Not working for any faction at campaign start.

**Conviction:** Family (she loves her brother and father) vs. Self-Determination (she wants to matter on her own terms, not as someone's dynastic piece).

**Resonant Style:** Evidence. Show her concrete proof of what's happening to Torben, or concrete proof that Valoria needs her. Abstract appeals to patriotism will not move her.

**Recruitable by any faction** via Circles Ob 3 (she's in Altonian territory), then a social scene (Appeal or Debate, 3 exchanges) targeting Family or Self-Determination conviction.

---

## 13.2 Named NPCs — Church

---

### Confessor Arne Himlensendt
*Head of the Holy Church of Galbados*

**TS:** 0. Sincerely devout, institutionally effective, and completely without knowledge of what his institution is or what it was built to do. He is the most thorough product of Galbados's theological engineering in the kingdom. His certainty is not the certainty of someone who has considered doubt and rejected it — it is the certainty of someone who has never been given the perceptual tools to approach the question differently.

**Social Profile:**
- Attributes: Presence 6, Cognition 5
- Composure: 12 (Presence 6 + 6)
- Dominant Conviction: Faith
- Resonant Style: Consequence (what this situation produces for the Church's mandate)

**Histories:** Theology (3), Political Negotiation (2)

**Belief:** *"The Church must complete Galbados's mandate on the peninsula before the Altonian schism reaches us."*

**Destabilisation trigger.** He would be the most destabilised person in the kingdom if he discovered the truth about Galbados's nature. The Church's relics include originary Locks — objects present at Galbados's actual emergence from the unintelligible ground. Three Cardinals who handled these objects during restricted ceremonies subsequently requested to be relieved of their duties. Their requests were granted without public explanation.

---

### Cardinal Arnlod Olafsson — Justice
*Cardinal of Justice; oversees the Inquisitors and Grand Adjudicator*

**Niflhel connection:** Active. His use of Niflhel resources to suppress specific texts and individuals represents — without his understanding of this — the precise function the Inquisitors were designed to perform.

**Social Profile:**
- Composure: 7
- Dominant Conviction: Order (institutional Church integrity)
- Resonant Style: Evidence

**Domain action pool (Heresy Investigation):** Church Reach 7 + Ecclesiastical Law History bonus.

**Olafsson's vulnerability.** Baralta holds circumstantial evidence of the Olafsson-Niflhel connection. If players supply corroborating evidence (Solvind Brak's testimony or documentary records), Baralta launches a Domain action against Church Stability: Ob 3, pool Mandate 7 + Reach 5 + player evidence bonus. Success: Church Stability −2, TC −3, Olafsson's Inquisitor operations suspended.

---

### Cardinal Magnus Klapp — Scholarship
*Controls Church universities, monasteries, and the archive of identified Einhir texts*

**TS:** 31 (approaching Stirring threshold, unknown to anyone).

**CE track:** 4. Archive work has brought him into sustained contact with Einhir records and two originary lock objects. Trajectory B (Fracture), moving toward C (Conversion). One more sustained encounter with a Thread-significant object will trigger a TS growth check. If it succeeds: the head of the Church's entire educational apparatus develops Thread sensitivity.

---

### Cardinal Osten Jarnstal — Military
*Commands the Knights Templar*

**Belief:** *"The Knights Templar should be independent of all political authority."*

This is a structural fault line. Jarnstal is drifting toward unilateral action. His relationship with Confessor Himlensendt grows cooler each season.

---

## 13.3 Named NPCs — Hafenmark

---

### Duchess Inge Baralta
*"The Hammer" · "The Black Ram"*

**TS:** 0 (Inert). Essentialist theology has completely foreclosed TS development. She has no awareness this foreclosure exists.

**Social Profile:**
- Attributes: Cognition 4, Endurance 4, Presence 5
- Composure: 11 (Presence 5 + 6)
- Dominant Conviction: Order — structured, hierarchical, institutional authority
- Resonant Style: Evidence — legal precedent, documented history, institutional argument

**Histories:** Military Command (2), Maritime Trade (2), Court Law (1)

**Beliefs:**
1. *"My authority in Hafenmark is granted directly by God — not mediated by the Church, not conditional on the Confessor's approval. I will not yield one principle of it."*
2. *"The Church is holy, but it is not the state. I will hold that line in Parliament, in court, and in blood if necessary."*
3. *"The succession must be settled before Vaynard turns it into his instrument."*

**TC Contribution.** While Baralta's Mandate remains above 5, she suppresses TC at −1/season. If Mandate falls below 5 this suppression disappears. If she is excommunicated: TC +4 immediately.

**The Sovereign Authority Doctrine.** *Usable once per campaign arc as a Domain action against Church Reach (Ob 4; pool: Mandate 7 + Reach 5):*

| Degree | Result |
|---|---|
| Overwhelming | TC −3. Church Mandate −1. Heresy Investigation cannot advance this season. Baralta +1D on social actions vs Church reps for the arc. |
| Success | TC −2. Church Mandate −1. Heresy Investigation opens (Ob 4 to pursue). |
| Partial | TC −1. Heresy Investigation opens immediately. Church Reach +1. |
| Failure | TC +1. Heresy Investigation opens immediately. Baralta's Mandate −1. |

---

## 13.4 Named NPCs — Varfell

---

### Duke Magnus Vaynard
*"The White Wolf"*

**TS:** 14 (Dormant). Does not know he has Thread sensitivity.

**Social Profile:**
- Composure: 10 (Presence 4 + 6)
- Dominant Conviction: Reason — truth as instrument; genuine high weight on acknowledged uncertainty
- Resonant Style: Consequence — forward-looking analysis of what situations will produce

**Beliefs:**
1. *"Valoria's future belongs to whoever understands the Southernmost. I will establish that understanding before the Church buries the last answer."*
2. *"The Church's prohibition on Thread knowledge is self-serving concealment. I will know what they are hiding."*
3. *"The succession ratification is my leverage with the Crown. I will not surrender it without Southernmost access terms."*

**Thread Investigation Track (TK) — 0 to 5**

| TK | Campaign Effect |
|---|---|
| 1–2 | Informed questions. Acute awareness rather than understanding. No TC effect. |
| 3 | Structural theory (wrong in detail, correct in structure). Succession leverage formally linked to Southernmost access terms. TC +1. |
| 4 | Urgency. Willing to offer collection access (including originary locks) in exchange for Thread education and Southernmost partnership. TC +2. |
| 5 | Dangerous knowledge — knows what Galbados was structurally. Seeks capability, not knowledge. TC +3. |

**The Discovery Event.** If Vaynard is present during a Thread event of sufficient intensity, the GM may call a Discovery Event. Spirit check TN 7 Ob 1. On success: TS advances to 30 (Stirring), and the world reorganises itself for him.

---

### Scholar Maret Uln — Varfell's Wild Card

**TS:** Unknown; practitioner-level (confirmed). Not a loyal Varfell character. Pursuing his own Belief: *"I will reconstruct the Ceiral Ritual before the Inquisitors find the text."* People's Revolution-adjacent.

**Starting Loyalty to Varfell:** 4.

Vaynard knows this and is calculating: Maret is the most valuable person on the peninsula for the Southernmost problem, and also a liability to Varfell's Church relationships. What the Duke does with Maret defines much of the faction's mid-game.

---

## 13.5 Named NPCs — Löwenritter

---

### Grandmaster Sigrid Ehrenwall

**Social Profile:**
- Dominant Conviction: Duty — obligation to the office, not the person
- Resonant Style: Consequence (show her what happens to Valoria if she doesn't act)
- Age/background: Late 50s. Career soldier. Served under Almud's father and Almud. Remembers pre-settlement Valoria.

**Beliefs:**
1. *"My oath is to the Crown as institution, not the man who holds it. I serve until the institution itself has failed Valoria."*
2. *"Almud is surrendering sovereignty incrementally. I am keeping count."*

**Relationship to Almud:** Respect without affection. Decent man governing badly. She will follow his orders until the day she doesn't, and the transition will be instantaneous.

**Coup threshold.** Ehrenwall has not yet concluded the Crown has failed the nation. When she does, she will act without hesitation or remorse. She is the most dangerous NPC in the game: patient, competent, and commanding an army.

**Relationship to the heir.** Views Torben's potential removal to Altonia as a direct sovereignty threat. If Almud surrenders the heir, coup trigger condition #2 is met.

**Relationship to the Church.** Cold contempt. The Löwenritter predates the Church of Galbados in Valoria. She will not challenge it theologically, but will never cede military authority to Templars.

---

## 13.6 Institutional Actors

---

### Royal Investigators — Crown Instrument

Legitimate investigative apparatus. Operations produce public evidentiary records.

**NPC pool.** Crown Reach dice at TN 7. Ob = target faction's Reach ÷ 2 (round up).

**Thread exposure risk.** Royal Investigators assigned to Niflhel, Southernmost, or active practitioner cases will encounter Thread-level phenomena they cannot process. The GM imposes −1D on affected investigators for the remainder of that investigation.

---

### Riskbreakers — Crown's Deniable Instrument

Extralegal arm of the Löwenritter. Operations are not recorded in Ministry of Law documents.

**Deniability Debt track (0–5).** Each exposed operation the Crown denies: Debt +1.

| Debt | Effect |
|---|---|
| 3 | Parliament's institutional trust erodes. All Crown Domain actions against non-Crown factions +1 Ob. |
| 5 | Parliamentary inquiry opens. Grand Debate (5 exchanges) — Crown's Reach and Mandate at stake. |

**Riskbreaker Cumulative Exposure (CE) — per operative:**

| Event | CE |
|---|---|
| Handling dissolution residue evidence | +1 |
| Direct witness to thread operation | +2 |
| Encounter with monstrous configuration | +2 |
| Extraction assignment with active practitioner | +1 |

At CE 3+: qualifies for TS growth check (Cognition TN 7, Ob 1) on the next confrontation event.

---

### The Inquisitors — Cardinal of Justice's Instrument

The Inquisitor Confrontation Arc. An Inquisitor who builds a successful file on a practitioner must, at some point, get close enough to observe what the practitioner is. The theology says it is the sin that caused the Calamity. Thread-level reality says otherwise.

**Inquisitor CE track:**

| Event | CE |
|---|---|
| Reviewing physical evidence from a Thread operation site | +1 |
| Interrogating a practitioner who performs passive perception in their presence | +1 |
| Witnessing a Thread operation directly | +2 |
| Handling an originary lock or dissolution residue object as evidence | +2 |
| Extended interrogation of a Resonant-tier practitioner | +3 |

At CE 3: TS growth check — Cognition TN 7, Ob 2 (essentialist formation raises the Ob). Success: develops TS toward Dormant. This is a **crisis of faith event**, not a benefit.

**Three trajectories at CE 3+ with TS development:**

- *Doubling Down:* Interprets the felt sense as evidence of the Arrogance's continuing temptation. Pursues practitioners with increased conviction. Becomes functionally a low-sensitivity Thread-detector without knowing it. TC +1.
- *Fracture:* Cannot reconcile the felt sense with doctrine. Stops functioning. Requests reassignment. Church loses investigative capacity; this Inquisitor may become an ally who knows operational procedure from the inside.
- *Conversion (rare):* TS development exceeds institutional formation's capacity to contain. Seeks out a practitioner to understand. The Church has a suppression protocol for this that Inquisitors themselves are not told about.

**Investigation procedure (3 stages):**

| Stage | Roll | Notes |
|---|---|---|
| 1. File Building | Church Reach, Ob 3 | Player obstruction at Ob 2. |
| 2. Formal Accusation | Church Reach, Ob 4 | Requires completed File. Accused may call Grand Debate (5 exchanges; pool: Cognition + relevant History). |
| 3. Conviction Hearing | Grand Debate finale | Conviction: TC +2. Accused faces imprisonment or exile. |

---

### The Knights Templar — Church Military

Church military arm, commanded by Cardinal Jarnstal. Deployable without royal authorisation when Piety is high. Cannot be used in a territory where Crown Mandate exceeds Church Mandate without provoking a Sovereignty Dispute.

**Thread exposure.** Templars assigned to Monstrous Incursion suppression missions accumulate CE on the same table as Inquisitors. Unlike Inquisitors, they have no institutional trajectory framework for managing it — Templar CE crises are personal, sudden, and unmanaged.

**Constraint:** Cannot accept orders that subordinate the Löwenritter militarily. If Cardinal Jarnstal orders Templar deployment into Löwenritter-held territory, this generates a Faction Tension event between Church and Löwenritter (Stability check for both factions, Ob 2).

---

## 13.7 NPC Faction Pools (Generic)

When a faction acts through institutional NPC capacity rather than a named leader:

**Pool construction:** Faction's relevant attribute score as dice pool. TN 7. Ob = opposing faction's relevant attribute ÷ 2, rounded up.

**Named NPC override.** When a named leader is personally involved in a Domain action, use their personal pool (attribute + History bonus) rather than the generic institutional pool. Named NPC personal pools are typically larger but narrower in scope.

---

## 13.8 NPC Style Discovery

Each named NPC has one Resonant Style tag: **Evidence**, **Character**, or **Consequence**.

| Style | Approach that earns +1D |
|---|---|
| Evidence | Legal precedent, documented facts, institutional history |
| Character | Who the person is; what they value; direct truth about oneself |
| Consequence | Forward-looking analysis; what happens if this path is taken |

Tags are not listed on player-facing materials. Discover them through investigation, observation, or prior scenes in which the NPC responded visibly to one approach over another.




---



# PART FOURTEEN: GM TOOLS

This part contains operational references for the GM: the Session Zero procedure with Editorial Questions, the Ob calibration guide, Hard Move tables, the three-clock feedback model, and the seasonal accounting checklist.

For the co-movement procedure and the Co-Movement Prompt Table, see §5.17. For Thread Hard Moves, see §5.3. For the TD track as campaign arc, see §12.7. For the Rendering Engine procedure, see §12.6.

---

## 14.1 Session Zero

### Checklist

- [ ] Answer Editorial Questions (§14.2)
- [ ] Set Safety Tools (Lines, Veils, or equivalent)
- [ ] Create Characters: 3 Histories at 2 pts each; 18 attribute points; 2–3 Beliefs; 0–2 Maxims; minimum 3 Knots
- [ ] Set opening clock values: TT 28, TC 15, IP 20, Parliament Integrity 7
- [ ] Write 1–2 Impression Tracks for the first NPCs players will meet
- [ ] Establish which clocks each PC is best positioned to address — and in which direction
- [ ] Review: split-pool combat, Leap procedure, Domain Echo trigger, Scope Shift

**Parliament Integrity** starts at 7. All Parliamentary Votes are standard Ob from the start. It degrades through events — track it on the Game Sheet.

**Clock starting values reflect Year 102 AG, campaign start.** If beginning mid-campaign or at a different historical moment, adjust per the canonical timeline.

---

## 14.2 Editorial Questions

Answer these collectively before first play. These are not rules — they are the table's shared fiction decisions. Answers shape tone, NPC behavior, and which dramatic questions are live.

**World texture (sensory and atmospheric):**
1. When Valoria feels right — stable, familiar, governed — what does it smell and sound like? When it feels wrong, what changes?
2. Is the campaign's dominant register cold court politics, hot personal drama, or existential dread? All three coexist — which is loudest?
3. What is the one image or scene that captures the setting for your table?

**Thread and metaphysics:**
4. Is the Thread visible, audible, felt, or something else entirely to practitioners at this table? How does the GM describe it without overdescribing it?
5. When a practitioner fails and TT rises, does the world deteriorate visibly and immediately, or does it accumulate silently? Which kind of horror fits the table?
6. Is the Forgetting melancholy, terrifying, or both? How should it feel when knowledge dissolves on exit from the Southernmost?

**Factions and politics:**
7. Which factions are the PCs likely to encounter first, and what does encounter with those factions look, feel, and sound like?
8. How does Almud carry himself in a room — what is the texture of his authority?
9. Is Baralta someone players might admire, fear, or despise? The answer shapes how she enters scenes.
10. At what point in the Theocracy Clock does the Church become visibly dangerous rather than merely powerful?

**Characters and stakes:**
11. What does Valoria mean to these characters? What would make them fight for it, leave it, or burn it down?
12. What is the line between political maneuvering the table finds entertaining and political betrayal the table finds genuinely distressing?
13. Are the PCs potential agents of the Restoration, potential opponents, or indifferent?
14. Is there a named NPC who the table wants to protect, and one they want to destroy?

**Endgame and pacing:**
15. Does the table want the campaign to end at a defined horizon (10 seasons, 20 sessions) or to run to natural conclusion? Which clocks are most likely to drive the ending?

No answer is wrong. The questions are generative. GMs may substitute or add questions as the table's needs dictate.

---

## 14.3 Ob Calibration Guide

All difficulty in Valoria is expressed through Ob. This guide gives the GM a reference framework for setting Ob across the five action categories. The goal is consistency: the same quality of opposition should produce the same Ob regardless of scene type.

### The Five-Point Scale

| Ob | Label | The situation is... |
|---|---|---|
| 1 | Routine | Prepared; unhurried; opponent willing or absent; no meaningful resistance |
| 2 | Standard | Professional difficulty under stakes; trained opposition; some resistance |
| 3 | Hard | Significant resistance; expert opposition; hostile environment; disadvantaged position |
| 4 | Severe | Elite opposition; deeply embedded resistance; baseline for Forced Resolution |
| 5+ | Structural | Territorial, institutional, or civilisational targets; the best possible opposition |

**Ob minimum is always 1.** No modifier reduces Ob below 1.

### Ob by Action Category

**Social actions (Debate, Appeal, Circles, Negotiate):**

| Situation | Ob |
|---|---|
| Willing party, private setting | 1 |
| Neutral party; professional context | 2 |
| Resistant party with competing interest | 3 |
| Firmly opposed; formal institutional resistance | 4 |
| Grand Debate against maximum institutional opposition | 5 |

The NPC's Resonant Style applies: using the style earns +1D, not a lower Ob. The difficulty reflects their actual position; the Style bonus reflects the quality of the approach.

**Combat (attack vs. defence):**
Combat uses versus rolls, not fixed Ob. The defender's net successes become the attacker's Ob for that exchange. Set position (Ob penalty from terrain, wounds, disadvantage) rather than the base roll difficulty.

**Thread operations:**
Thread Ob is set by scale (Object: 1, Personal: 2, Relational: 3, Territorial: 4–5, Structural: 6+) and actualization level. See §5 for full tables. Do not adjust Thread Ob for social or political factors — Thread difficulty is configurational, not situational.

**Investigation and information-gathering:**

| Situation | Ob |
|---|---|
| Publicly available, no opposition | 1 |
| Restricted but accessible with right contacts | 2 |
| Actively concealed; hostile territory | 3 |
| State-level intelligence with active counter-surveillance | 4 |
| Niflhel-grade operational security or Church archive access | 5 |

**Domain Actions (faction-level):**

| Situation | Ob |
|---|---|
| Unopposed faction action in own territory | 1 |
| Contested territory; moderate faction resistance | 2 |
| Opposed faction with equal or greater relevant stat | 3 |
| Strongly opposed; target faction has structural advantage | 4 |
| Structural institutional change; civilisational scope | 5 |

Domain Ob can also be set directly from the opposing faction's relevant attribute (stat score ÷ 2, round up). This is the default for Domain Echoes where the GM needs a fast Ob without deliberation.

### Common Ob Mistakes

**Setting Ob too high for ordinary professionals.** A skilled blacksmith, experienced soldier, or practiced merchant operates at Ob 2, not Ob 3. Ob 3 is hard — reserve it for genuinely difficult circumstances.

**Setting Ob too low for institutional opposition.** The Church, Crown, or major faction acting through institutional channels is Ob 3 minimum. Their resources and procedural depth are the resistance.

**Treating "important" as equivalent to "high Ob."** A dramatically significant scene is not inherently a high-Ob scene. The stakes are narrative; the Ob reflects the actual difficulty of the task. A crucial negotiation with a willing ally is Ob 1. A trivial errand against active Inquisitor interference is Ob 3.

---

## 14.4 Hard Moves

When a player rolls a Failure, the GM makes a Hard Move. Roll d12 or choose the most appropriate for the current fiction.

| d12 | Hard Move |
|---|---|
| 1 | **A door closes** — an opportunity, ally, or path that was open is now shut |
| 2 | **It costs something** — the goal is achieved but something valuable is lost |
| 3 | **You're noticed** — someone now knows what you were doing and who you are |
| 4 | **It escalates** — a minor problem becomes a significant one |
| 5 | **Separated** — the group is split, a companion is out of reach |
| 6 | **Resource depleted** — something finite is now gone (ammunition, an ally's goodwill, a contact) |
| 7 | **Worse position** — you achieved nothing and are now more vulnerable than before |
| 8 | **Evidence** — your failure left proof of your presence, intent, or nature |
| 9 | **Cascade** — the failure triggers a secondary event |
| 10 | **Time** — the delay costs a season or critical window |
| 11 | **Direct harm** — someone is hurt; Wound, Certainty loss, or Knot strain as appropriate |
| 12 | **The worst thing** — GM makes the most narratively appropriate severe consequence |

**Principles for Hard Moves:**
- Follow logically from the fiction. The move should feel inevitable in retrospect.
- Never repeat the same move twice in a row against the same character.
- Advance something in the world — create a new problem, do not merely punish.
- Failure is not the end of the story. Partial success is not failure.

For Thread-specific Hard Moves (failure on Leap, Weaving, Pulling, FR), see §5.3.

---

## 14.5 The Three-Clock Feedback Loop

The three clocks are not independent. They form a structural feedback loop that tightens as the campaign progresses.

**The loop:**
- Rising TT produces Thread events the Church reads as theological warrant for authority → TC rises.
- TC pressure produces political instability → factions conflict → battles → TT rises further.
- Rising TT and TC together create instability that Altonia reads as strategic opportunity → IP rises.
- Rising IP forces Crown to make concessions → Crown weakens → TC and TT exploitation accelerates.

**The players' structural position.** PCs hold the only tools that can directly address TT (Thread operations reducing fabric tension) and the only investigative capacity to address TC's hidden structural driver (the Church-Niflhel connection and the truth about Galbados). They are the campaign's repair mechanism. Whether they act as such is entirely their choice.

**If the table does nothing actively:** TT drifts +1 per year at year-end accounting. TC grows from Church Mandate at approximately +3–5 per year at current starting values. IP grows at +2 per season base. A 10-season passive campaign ends near TT 42, TC 50–60, IP 40. These are livable but increasingly constrained positions.

**The table can measure the deterioration.** This is intentional. The clocks are not hidden. Players who engage with the system understand what it costs to ignore any dimension.

---

## 14.6 Discovery Events

When a character with TS 10–39 is present during a Thread operation of sufficient intensity, the GM may call a Discovery Event.

**Triggers:**
- Weaving or Pulling at Relational scale or above: always triggers.
- Forced Resolution: always triggers.
- Monstrous entity encounter: triggers at scene end (not mid-scene, unless the entity directly engages the observer's threads).
- Extended proximity to an originary Lock object (handling, not passing): triggers after one full scene.

**Procedure:**
Private Spirit check (TN 7, Ob 1). Success: TS advances per the standard growth table (see §5). Failure: character is *primed* — the next Discovery Event of equal or lesser intensity triggers automatically without a check.

**Presenting Discovery Events.** A Discovery Event is not dramatic by default. The GM should describe it as a perceptual intrusion that doesn't fit the rendering: a moment where the world seems to hold still, where distance collapses, where a sensation arrives with no source. What the character interprets this as (spiritual intimation, madness, a trick of the light) is their own business. The GM does not announce that TS is changing.

---

## 14.7 Seasonal Accounting Checklist

At the end of each season, resolve in order:

- [ ] Apply all pending Domain Action outcomes (succeeded orders, failed orders, Domain Echoes)
- [ ] Advance NPC CE tracks; resolve TS growth checks for any NPC at CE 3+
- [ ] Faction Stability checks for any faction that suffered attribute loss this season (Ob from stability table; floor Ob 4 at Stability ≤ 2)
- [ ] TT passive drift: +1 per four seasons (i.e., once per full year, at Winter accounting)
- [ ] Apply TT-lowering events (Overwhelming Weavings at Relational+; preserved Einhir sites; sustained community Weaving; Ceiral Ritual)
- [ ] Apply the faction attribute seasonal cap: no attribute may have changed by more than ±2 from this season's accounting. If cumulative changes exceed ±2, cap them. Log excess as pending for the following season.
- [ ] CP awards: +2 per Belief pursued in a meaningful scene; +2 per Belief challenged by events; +4–5 per Belief genuinely revised; +1 per Maxim honoured at cost; +2 per Maxim violated and reckoned with; +1 per stated Goal pursued; +2 per Ordeal survived; +1 per Domain Action completed.
- [ ] TC threshold conditions: TC pauses if Church Stability ≤ 5 this season. Cross-faction Mandate average ≥ 6: TC −1 this season.
- [ ] Parliament Integrity update: adjust per events (Thread event in session: −1; stable Crown-Hafenmark cooperation: recovers +1 per season).
- [ ] Orphaned configuration deterioration: each orphaned configuration makes an Endurance check (TN 7, Ob 1) at accounting. Failure: configuration fragments (TT +1; perceptible wrongness at TS 30+).
- [ ] Season marker advances. At Winter: year-end accounting (TT annual drift, annual events).
- [ ] Check TTRPG endgame indicators if applicable (see §12.1). If board game or hybrid: check victory conditions.

---

## 14.8 GM Game Sheet Reference

The following tracks require active GM management throughout the campaign. Keep these visible.

**World Clocks:**

| Clock | Starting Value | Thresholds |
|---|---|---|
| Thread Tension (TT) | 28 | 20 (Stirring), 40 (Wakening), 60 (Fracturing), 80 (Rupturing), 100 (The Rupture) |
| Theocracy Clock (TC) | 15 | 20 (Ecclesiastical), 40 (Ultimatum), 60 (Schism), 80 (Seizure), 100 (Holy State) |
| Altonian Pressure (IP) | 20 | 30 (Aggressive), 45 (Hostile), 60 (Warlike), 75 (Imminent), 100 (Invasion) |
| Parliament Integrity | 7 | 7–10 (Normal), 5–6 (+1 Ob all Votes), 3–4 (Supermajority required), 1–2 (Recess), 0 (Dissolved) |

**NPC Tracking (starting values):**

| NPC | TS | CE | TK | Notes |
|---|---|---|---|---|
| Baralta | 0 | — | — | Devout foreclosed; TC suppressor |
| Vaynard | 14 | — | 0 | Discovery Event potential |
| Almud | 28 | — | — | Discovery Event potential |
| Lenneth | 0 | — | — | Not foreclosed |
| Klapp | 31 | 4 | — | Trajectory B → C |
| Himlensendt | 0 | — | — | Sincerely devout |
| Olafsson | 0 | 1 | — | Niflhel connection active |

**TT penalties to Thread operations (all operations):**
- TT 60–79: +1 Ob
- TT 80–99: +2 Ob
- TT 100: campaign event




---



# PART FIFTEEN: THREAD SPELL CATALOG

Thread operations are generated from first principles using the Three-Step procedure (§5.2–5.7). This catalog provides representative examples across all operation types and scales. Use these to calibrate Ob expectations and illustrate what each operation type can achieve; do not treat them as an exhaustive list.

For full mechanics: Weaving (§5.4), Pulling (§5.5), Past-Oriented Pulling (§5.6), Forced Resolution (§5.7), Co-Movement (§5.8).

---

## 15.1 Weaving Operations

*Foregrounds: actuality toward coherence; temporality toward persistence. Things cohere, stabilise, persist.*

| Code | Name | Scale | Ob | Min TS | Description |
|---|---|---|---|---|---|
| W-01 | Wound Closure | Object | 1 | 40 | Temporal acceleration — wound resolves as it would naturally, but now. Memories are consistent; no paradox. |
| W-02 | Blade Reinforcement | Object | 1 | 40 | Weapon threads drawn toward structural coherence. Weapon gains +1 damage bonus for the scene. |
| W-03 | Binding Word | Relational | 3 | 60 | Agreement threads woven to mutual coherence. Breaking the agreement produces a local rendering failure in both parties (+1 ThS, Certainty check). |
| W-04 | Territorial Calm | Territorial | 5 | 60 | Regional thread-configuration stabilised. All Thread operations in the territory at −1 Ob for one season. TT −1 on Overwhelming. |
| W-05 | The Locked Archive | Structural | 6 | 80 | Building's integrity woven so knowledge persists even if the physical form is damaged. Documents within survive destruction as configurational memory. |
| W-06 | Dissolving a Monstrous Configuration | Variable | 3–5 | 60 | Entity destroyed; Gap partially closed (TT −2 on Success; −4 on Overwhelming). Ob varies with entity's configuration depth. |
| W-07 | Rekindling | Personal | 2 | 40 | Restores Composure strain up to Ob value. On Overwhelming: also replenishes one Inspiration whose value is ≤ Ob. |
| W-08 | Healing Acceleration | Personal | 2 | 40 | Restore Health up to 4 points (not yet at Wound). Overwhelming: restore full Health + heal 1 Wound. |
| W-09 | Stabilising a Gap | Territorial | 4 | 60 | Gap stops widening for one season. Does not close it. Requires sustained contact (full scene). TS growth: +4 on success. |

---

## 15.2 Pulling Operations

*Foregrounds: actuality toward potential; temporality toward loosening. Things open, loosen, dissolve toward possibility.*

| Code | Name | Scale | Ob | Min TS | Description |
|---|---|---|---|---|---|
| P-01 | Unlock | Object | 1 | 40 | Lock threads loosened; mechanism opens. Duration: end of scene. |
| P-02 | Attention Diversion | Personal | 2 | 40 | Target's awareness threads loosened; removes one defensive action for one round. |
| P-03 | Dissolving Conviction | Personal (firm) | 3 | 60 | Held belief loosened; target becomes open to revision for the scene. Does not change the belief — opens the door. |
| P-04 | Loosening the Crowd | Territorial | 3 | 60 | Collective momentum pulled toward potential. Unit Cohesion checks +1 Ob for one round. |
| P-05 | Opening the Wound | Personal | 2 | 40 | Reversed healing; inflicts 1 Wound (bypasses armour). Certainty check Ob 1 for practitioner immediately after. |
| P-06 | Memory Displacement | Personal (firm) | 3–4 | 60 | Specific memory loosened toward potential; content becomes uncertain or inaccessible for duration. Absence detectable by TS 30+ Diagnosis. |
| P-07 | Thinning the Veil | Relational | 3 | 60 | Rendering surface thinned in an area; non-sensitive characters experience minor rendering failures; Thread-locked objects briefly visible to TS 10+. |
| P-08 | Temporal Shimmer | Object (Past-Oriented) | 3 | 80 | Burned letter readable; broken object briefly whole; glimpse of the object's prior state. Duration: one round. Produces TD +1. |

---

## 15.3 Forced Resolution Operations

*Collapses a thread configuration to one pole permanently. Lock = collapsed toward full actualisation. Dissolution = collapsed toward full potential (ceases to exist as a coherent thing).*

All FR operations require TS 50+. All FR operations add TD. Diagnosis mandatory before any FR; skipping adds Ob +2 and risks auto-Gap on failure.

| Code | Name | Type | Scale | Ob | Min TS | Description |
|---|---|---|---|---|---|---|
| FR-L-01 | The Permanent Lock | Lock | Object | 4 | 50 | Gate permanently sealed; wound locked as permanent scar; object fixed in exact state. |
| FR-L-02 | Sealing a Mind | Lock | Personal | 5 | 60 | TS sealed at current value; one Belief made permanently unrevised-able; specific injury effect made permanent. Non-consensual: Certainty −2 practitioner. |
| FR-L-03 | The Locked Institution | Lock | Structural | 7 | 80 | Fundamental law permanently embedded in a faction's configurational structure; institution becomes incapable of reform in the Locked domain. |
| FR-D-01 | Dissolution of Evidence | Dissolution | Object | 4 | 50 | Document, object, or physical fact ceases to exist as a coherent configuration. Memories of it remain; the Temporal Disjunction is immediate. |
| FR-D-02 | Dissolving a Wound | Dissolution | Personal | 5 | 60 | Wound never fully actualised. Safer than Weaving (no Temporal Disjunction if person is present). Catastrophic on failure: wound deepens + Gap risk. |
| FR-D-03 | Dissolving a Relationship | Dissolution | Relational | 6 | 70 | Alliance, loyalty bond, or institutional debt ceases to exist as a configurational weight. Both parties experience the Disjunction. |
| FR-D-04 | Unmaking | Dissolution | Territorial | 7 | 80 | Territory loses configurational coherence. Fraying Bane risk to practitioner (§5.7). TT +6 minimum regardless of outcome. |

---

## 15.4 Operation Scale Reference

| Scale | Ob | TT Multiplier | Min TS |
|---|---|---|---|
| Object | 1 | ×1 | 40 |
| Personal | 2 | ×1 | 40 |
| Relational | 3 | ×2 | 60 |
| Territorial | 4–5 | ×3 | 60 |
| Structural | 6–7 | ×5 | 80 |

**Mass combat Thread operations:** Replace scale TT multiplier with flat ×3. Total TT gain from any single mass combat Thread operation capped at +15. Excess converts to narrative consequence (regional site destabilisation, Locked zone expansion) at GM discretion.




---



# PART SIXTEEN: REFERENCE MATERIALS

---

## 16.1 Glossary

| Term | Definition |
|---|---|
| **Actuality** | The degree to which a thread configuration is fully realised. Fully actualised = present and stable. Pure potential = exists as possibility only, no rendered presence. |
| **Approach Training** | One full campaign season of Thread study. Prerequisite for all active Thread operations. Grants permanent tag; not a roll. |
| **Beliefs** | Three statements of conviction that drive character action and CP accumulation. Revised through play, not purchase. |
| **Body of Argument (BoA)** | Social health track in Grand Debates. Equal to Presence or Cognition score. Whittled by losing exchanges. |
| **ThS** | Coherence Degradation. Per-practitioner 0–20 track measuring the growing disjunction between the practitioner's configuration and the rendered world. Not a resource — a campaign-arc cost of sustained practice. |
| **CE** | Confrontation Exposure. Per-NPC 0–5 track. At CE 3, triggers a TS growth check — a crisis, not a benefit. |
| **Circles** | Social access network tied to a specific community or institution. Used for Appeal and information-gathering. History-based; degradable. |
| **Co-Movement** | The principle that every Thread operation produces consequences in all three dimensions (intelligibility, actuality, temporality) simultaneously. The practitioner's intention foregrounds one; the others move automatically. |
| **Composure** | Social wound track. Equal to Presence + 6 (range 7–13). Strain reduces it; reaching 0 means Rattled. |
| **Confrontation** | A felt encounter with what exceeds the rendering's capacity. The primary developmental mechanism for Thread Sensitivity in non-practitioners. |
| **CP** | Character Points. Earned through Beliefs, Maxims, and Ordeals. Spent on advancement (attributes, Histories, Circles, Resources, Boons). |
| **Devout Constraint** | Essentialist theological formation that forecloses TS development. Cannot be overcome through confrontation alone — requires sustained doctrinal rupture. |
| **Diagnosis** | Step 2 of Thread operation. No roll; structured GM exchange. Mandatory before Forced Resolution. |
| **Domain Action** | A personal roll that the GM recognises as having faction-level scope. The personal Ob resolves the personal outcome; a second Ob resolves the faction-level consequence. |
| **Domain Echo** | When a personal success automatically produces faction-level effects without a second roll. Fires on GM recognition of scope; players do not declare it. |
| **Ein Sof** | Infinite positive being that exceeds all attributes and human categories. The source from which threads are continuously spooled. Epistemically inaccessible, not ontologically void. |
| **Epistemic Seduction** | The process by which increasing TS dissolves the normative categories that would motivate a transforming practitioner to seek correction. The rendering shifts; what once seemed monstrous seems clarified. |
| **Forgetting, The** | The rendering's refusal to sustain Southernmost knowledge in non-sensitives upon exit. Not amnesia — the knowledge dissolves into emotional residue without propositional content. |
| **FR** | Forced Resolution. Advanced Thread operation collapsing a configuration permanently to Lock (fully actualised) or Dissolution (ceases to exist). Requires TS 50+. |
| **Gap** | A wound in the rendered world's fabric through which the unintelligible ground presses. Produces monstrous configurations and configurational instability in the territory. |
| **History** | A meaningful life chapter representing skill and experience. Provides dice pool bonus and the test-track advancement mechanism. |
| **Impression Track** | 0–5 relationship scale with a named NPC. Advances through meaningful scenes; at 5, triggers a significant NPC action on the character's behalf. |
| **Inert Knowledge** | Information a non-sensitive character can recite but cannot act on with Thread-level precision. Marked on the sheet; unlocks mechanically when TS develops. |
| **Inspiration** | A named, valued relationship, conviction, or commitment. Spent as bonus dice. Recovered through roleplay. Sum of all Inspiration values cannot exceed Spirit. |
| **Intelligibility** | The dimension of Thread operation foregrounding the rendered ↔ unintelligible axis. Operations in this dimension affect what can be perceived, known, or understood. |
| **IP** | Altonian Pressure. A 0–100 track measuring the Altonian Empire's aggression toward Valoria. Hidden from players; expressed through events. |
| **Knot** | A significant relational bond between a character's threads and another entity (person, place, community, object). Provides bonus dice when Called; accumulates Strain under relational stress. |
| **Let It Ride** | No re-attempts on a failed roll unless circumstances significantly change. Partial = done with complication. Failure = not done AND complication. |
| **Maxims** | 0–2 short behavioural commitments. Honoured at cost or violated and reckoned with: both earn CP. |
| **Momentum** | 0–6 session resource. Builds on exceptional combat and social successes. Burns to add automatic successes to non-Thread rolls. |
| **Ob** | Obstacle. The number of net successes required. Ob 1 = routine; Ob 5+ = structural/institutional. Always minimum 1. |
| **Ontical** | Pertaining to the rendered world: particular beings, facts, everyday experience as given to consciousness. |
| **Ontological** | Pertaining to Being as such: thread-constitution, conditions of possibility, the structures that make beings possible. |
| **Orphaned Configuration** | A present state whose causal history has been removed by Past-Oriented Pulling. Cause removed; effect persisting. Deteriorates faster than grounded configurations. |
| **Practitioner** | A character with Approach Training and TS 40+. Can perform active Thread operations. |
| **Providence Event** | When the Ein Sof's fullness arrives in a form the rendering can hold — briefly and perfectly. Cannot be triggered. A consequence of perfect alignment at mortal risk at TT ≤ 20. |
| **Push** | Re-roll all failed dice once after any non-Thread roll. Costs −1 Certainty. Once per roll. |
| **Rendering** | The always-already process by which consciousness presents the thread-substrate as experienceable reality. Not a filter — the condition of possibility for experience. |
| **Resources** | Material or institutional assets. History-based; degradable. Used for procurement and material-scale influence. |
| **Scope Shift** | Changing the scale of one's action within a round. Free; verbal declaration. One action per scope per round; +1 Inspiration for additional scope within same round. |
| **Shifting Object** | A configuration oscillating between presence, absence, and distortion. Signals elevated TT. Stabilised by Weaving (Ob 2); destabilised by failure into Gap risk. |
| **TC** | Theocracy Clock. A 0–100 track measuring the Church of Galbados's institutional conquest of Valorian governance. |
| **TD** | Temporal Disjunction. The gap between retained experience and altered factual history produced by Past-Oriented Pulling. Also a per-practitioner track (0–20) for sustained Thread work cost. |
| **Temporality** | The dimension of Thread operation foregrounding the past-anchored ↔ future-open axis. Operations in this dimension affect what has happened, what persists, and what has potential. |
| **Thread Sensitivity (TS)** | Hidden 0–100 score tracking a character's capacity to perceive and work threads. Cannot be purchased with CP. Develops through confrontation and practice. |
| **Threadcut** | A being or configuration not continuously spooled by the Ein Sof. Radically *is* without *becoming*. Requires active maintenance to persist. |
| **TK** | Thread Knowledge. Per-NPC 0–5 track for characters who understand Thread metaphysics intellectually (not experientially). |
| **TN** | Target Number. The minimum a die must show to count as a success. Standard TN is 7. |
| **TT** | Thread Tension. A 0–100 track measuring cumulative strain on the rendered world's configurational substrate. Default start: 28. |

---

## 16.2 Character Sheet Fields

The following fields appear on a complete Valoria character sheet. Pre-calculate pools before play — players do not reconstruct formulas at the table.

**Identity**
- Name, Faction affiliation, Background descriptor
- TS (GM tracks; not shown to player)

**Attributes (1–7 each)**
- Physical: Agility, Endurance, Strength
- Mental: Cognition, Memory, Focus
- Social: Attunement, Bonds, Presence
- Metaphysical: Spirit

**Derived Scores**
- Health = Endurance + 6
- Composure = Presence + 6
- Certainty = current value / Spirit (maximum)

**Histories (pre-calculated)**
- Name, point allocation, primary attribute
- Pre-calculated pool = primary attribute + (points + 3)
- Test Track: Challenged / Exceeded checkboxes

**Thread Pools (practitioners only — pre-calculated)**
- Leap: Cognition + Focus + Scholar History bonus
- Weaving: Cognition + Memory + Scholar History bonus
- Pulling: Cognition + Attunement + Scholar History bonus
- FR: Cognition + Memory + Scholar History bonus
- ThS track: current / 20, with stage markers (Dissonant / Fragmented / Fractured / Severed / Crisis)

**Beliefs (2–3)**
- Statement text
- Status checkboxes: Pursued / Challenged / Achieved / Revised

**Maxims (0–2)**
- Statement text

**Inspirations**
- Name, value (1–Spirit cap for sum), Used checkbox

**Knots**
- Person/Place/Thing, closeness tier (Close/Regular/Distant), current Strain, threshold, Contesting checkbox

**Impression Tracks**
- NPC name, 0–5 track, Dormant checkbox

**Combat**
- Weapon name, Reach, pre-calculated Combat Pool, Offence TN, Parry TN
- Armour type, Damage Reduction, Pool Penalty

**Health and Wounds**
- Current Health / Maximum Health
- Wound boxes (up to 4), incapacitation threshold

**Resources**
- CP total
- Circles (name, rating)
- Resources (name, rating)

---

## 16.3 Faction Sheet Fields

Full-sheet factions track six attributes. Partial-sheet factions (Revolution, Niflhel, Löwenritter in peacetime) track the subset relevant to their operational profile.

| Attribute | Scale | Function |
|---|---|---|
| Mandate | 1–7 | Institutional legitimacy; determines Domain Action pool base |
| Reach | 1–7 | Intelligence, information networks, investigative capacity |
| Wealth | 1–7 | Economic resources; army maintenance; Domain Action support |
| Military | 1–7 | Armed forces; unit mustering; battle resolution pool |
| Intel | 1–7 | Covert operations; espionage; Niflhel-equivalent capacity |
| Stability | 1–7 | Institutional coherence; checks faction collapse; floor for Mandate degradation |

**Seasonal cap:** No attribute may change by more than ±2 per season from any combination of Domain Actions, Domain Echoes, and board game orders. Excess is held pending next season.

**Faction collapse (Stability 0):** All attributes freeze; Mandate drops to 0; GM determines collapse within one season; reconstitution requires Circles Ob 4 + Stability rebuilt above 2.

---

## 16.4 Quick Reference: Clock Starting Values and Thresholds

| Clock | Start | Thresholds |
|---|---|---|
| Thread Tension (TT) | 28 | 20 Stirring · 40 Wakening · 60 Fracturing · 80 Rupturing · 100 The Rupture |
| Theocracy Clock (TC) | 15 | 20 Ecclesiastical · 40 Ultimatum · 60 Schism · 80 Seizure · 100 Holy State |
| Altonian Pressure (IP) | 20 | 30 Aggressive · 45 Hostile · 60 Warlike · 75 Imminent · 100 Invasion |
| Parliament Integrity | 7 | 7–10 Normal · 5–6 +1 Ob Votes · 3–4 Supermajority req. · 1–2 Recess · 0 Dissolved |

**TT penalties to all Thread operations:**
- TT 60–79: +1 Ob
- TT 80–99: +2 Ob

---

## 16.5 Quick Reference: Degree of Success

| Net Successes | Degree | Outcome |
|---|---|---|
| ≥ 2× Ob | Overwhelming | Exceptional outcome + bonus beyond the goal |
| ≥ Ob | Success | Goal achieved cleanly |
| > 0, < Ob | Partial | Goal achieved with complication or cost |
| ≤ 0 | Failure | Goal not achieved AND complication occurs |

Net zero is Failure. Ob minimum is always 1.

---

## 16.6 Quick Reference: CP Award Table

| Activity | CP |
|---|---|
| Pursuing a Belief in a meaningful scene | +2 |
| Belief challenged by events | +2 |
| Belief genuinely revised in response to events | +4–5 |
| Maxim honoured at personal cost | +1 |
| Maxim violated and reckoned with | +2 |
| Pursuing a stated Goal | +1 |
| Surviving an Ordeal | +2 |
| Completing a Domain Action | +1 |

| Spend | CP Cost |
|---|---|
| Attribute +1 | Current score × 3 (narrative justification required above 5; 7 is absolute maximum) |
| History +1 | 3 |
| New Boon | 3–8 (GM and player agree) |
| Remove a Bane | ~equal to benefit the bane was inflicting |
| Circles or Resources +1 | 2 |




---




---

# APPENDIX A — PATCH LOG (Since Checkpoint 13)

| Patch | Stage | Description |
|-------|-------|-------------|
| Stage 17-P1 | Canon Guard | §5.9 Coherence Degradation → Thread Stability (ThS); campaign-arc track direction inverted to 20→0; all CD references updated |
| Stage 17-P2 | Canon Guard | §5.10 Taint Track → Coherence Track; individual track inverted 10→0 (10=fully coherent, 0=monstrous NPC); all Taint/taint references updated |
| Stage 17-P3 | Canon Guard | Heart attribute removed: Leap pool → Attunement + History; Contact Duration → Focus; all Thread operation rolls → Spirit + History; Inspiration checks → Spirit; Discovery Event and Originary Lock checks → Spirit; CE-triggered TS growth checks → Cognition |
| Stage 17-P4 | Canon Guard | Poise removed; Composure = Presence + 6 everywhere; Debate pool → Cognition; NPC Composure values recalculated against Presence + 6 |
| Stage 17-P5 | Canon Guard | Coordination removed: §8.1 personal combat manoeuvres → Agility; §8.3 mass combat Officer attack pool → Cognition; mass combat initiative → Cognition; Rally → Cognition threshold / Presence roll |
| Stage 17-P6 | Canon Guard | Resolve derived score row removed from §2.3; Inspiration cap reads "Spirit score" directly throughout |
| Stage 17-P7 | Hybrid | §12.3 Hybrid Mode rewritten with all resolved gap content (G-075, G-079, G-080, G-081, G-083, G-085, G-091, G-092, G-093, G-094, G-095) |
| Stage 17-P8 | Hybrid | §12.9 Hybrid Consequence Rules added (G-086, G-087, G-088, G-089, G-090) |

---

# APPENDIX B — OPEN ITEMS (P1 and P2)

## Editorial Decisions Pending

| Item | Description |
|------|-------------|
| Renown permission table | Tiers 1–10 fully defined; only Renown 6 data point exists |
| Varfell Private Collection transfer | PC takeover scenario — transfer conditions |
| Niflhel primus inter pares | Leadership structure decision |
| Revolution named elder NPC | Optional contact for Revolution faction |
| Territory names | batch_e placeholders need canonical names |
| Varfell victory condition tuning | Current conditions may be over-powered |
| 10 remaining seasonal event cards | 10 of 20 total cards unwritten |
| Named Restoration NPCs | Not yet designed |
| E-01 assassination perpetrator | Identity unresolved |
| E-03 AG calendar name | Name unresolved |
| Niflhel named NPC stat blocks | Rolf Dunmark, Solvind Brak |
| Revolution named NPC stat blocks | Edith Varn |

## Mechanical Gaps Pending (P1/P2)

| Gap | Description | Priority |
|-----|-------------|----------|
| G-093 stress test | Resources/Wealth threshold formula (2× vs 2×−1) needs Phase 3 validation | P2 |
| Board game compilation | Board game ruleset not yet compiled — Phase 2 deliverable | P1 |
| Hybrid supplement | Standalone hybrid timing/transition guide — Phase 2 deliverable | P2 |
| Phase 3 simulation | 56 mechanics untested against coverage matrix | P1 |

---

*Checkpoint 14 — 2026-03-26 — Phase 2 TTRPG compilation complete with hybrid gaps resolved*
