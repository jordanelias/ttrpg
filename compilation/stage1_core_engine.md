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

**Minimum pool:** No combination of penalties may reduce a pool below 1D. If penalties would reduce a pool to 0 or below, the character rolls 1D. Additional Ob penalties still apply normally.

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
| Resolve | Spirit | 1–7 | Maximum total Inspiration value |

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
- Wounds: −1D per Wound to the relevant action pool (cumulative)
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
2. All subsequent rolls: **−1D per Wound** to the relevant action pool (cumulative)
3. Excess damage carries over into reset Health

**Single-hit cap:** No single hit inflicts more than 2 Wounds. Damage beyond 2 Health resets is discarded. (Damage exceeding 2× Health triggers 2 Wounds and excess is lost — the 3× reference is the theoretical maximum input, not the output.)

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

