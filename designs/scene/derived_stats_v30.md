# VALORIA — Derived Stat System Specification
## Date: 2026-04-18
## Status: PROPOSAL — supersedes prior derived_stats_v30.md
## Scope: Unified derived value system across personal, unit, settlement, and faction scales
## Principle: Stats are what your faction/character CAN do. Derived values are what they HAVE right now.

---

## §1 — Core Architecture

Every 1–7 stat remains the dice pool for its resolution system. No change to the dice engine. Each stat additionally produces a **derived value** — a granular resource the player tracks and the engine consumes.

**Derivation formula:** `derived_value = attribute × multiplier`

One attribute per derived value. No multi-attribute combinations. History and equipment modify drain/recovery rates, never the base pool size. The multiplier is an integer constant, calibrated to the interaction frequency of the system.

Stats change rarely (structural capability). Derived values change frequently (current state). The two-layer split exists because stats serve the resolution engine (small integers for dice pools) while derived values serve the state engine (large integers for resource tracking). These are different jobs requiring different scales.

**Output scaling** (TroopCount only): `output = floor(integer_result × derived_value / max_derived_value)`, capped at ratio 1.0. Applied only to active capacity outputs (TroopCount → damage dealt). Not applied to survival resources (Vitality, Composure) — a depleted survival pool makes you easier to kill, not weaker at killing.

---

## §2 — The Problem

The 1–7 stat system was designed for a board game where stats ARE dice pools. For a videogame, it creates three problems:

1. **Granularity.** ±1 on a 1–7 scale is a 14–100% change in capability. You can't express "a modest drain."
2. **Feedback.** The player sees "Wealth 4 → 3" and must mentally calculate implications. No visceral feedback.
3. **Conflation.** "How capable is my faction" (capacity) and "what resources do I have" (state) are one number.

Resolution: stats remain 1–7 (correct pool range for d10 probability curves). Derived values provide granularity, feedback, and state tracking. Small numbers for decisions, big numbers for consequences.

---

## §3 — Multiplier Tiers

| Tier | Multiplier | Systems | Rationale |
|------|-----------|---------|-----------|
| High | ×10 | Vitality | Combat has most interactions per scene (5–8+ rounds). Fine granularity for gradual degradation, wound thresholds, equipment differentiation. |
| Medium | ×5 | Stamina, Thread Fatigue | Action economy resources deplete per-round/per-operation. Variable action costs (3–10 per action) without inflating numbers. |
| Low | ×3 | Composure, Concentration | Social contests are 1–5 exchanges. Lower multiplier gives equipment modifiers proportionally more impact. |
| Faction | ×10–100 | Treasury, Legitimacy, Reputation, Cohesion | Seasonal interaction frequency (1–5 events/season). Each calibrated independently. |

---

## §4 — Personal Scale: Combat Resources

### 4.1 Vitality (survival resource)

| Property | Value |
|----------|-------|
| Formula | Endurance × 10 |
| Range | 10–70 |
| Direction | Drains down from max |
| Depleted at | 0 (incapacitated) |
| Equipment | Armor adds flat Vitality (+4 leather, +6 chain, +8 plate). Consumables restore on rest (+4 rations, +8 healer's kit). Poisons drain per round. |

**Wound Interval = Endurance + 6** (unchanged). Wounds accrue at each interval of cumulative damage: `wounds_taken = floor(total_damage / Wound_Interval)`. Each wound = −1D Combat Pool (unchanged).

Wound Interval checks use raw post-DR damage, not Vitality-scaled damage. Equipment Vitality bonuses affect total capacity before incapacitation; they do not change wound accrual rate. Armor DR still reduces incoming damage before both Vitality deduction and Wound Interval accumulation.

**Vitality cap:** `max_Vitality = Endurance × 10 + equipment_bonus`. Healing and recovery cannot exceed max_Vitality. If equipment is destroyed mid-combat, max drops but current Vitality is retained until next healing attempt (same pattern as faction Treasury when Wealth drops).

**Eliminates:** Max Wounds as a stored stat. Health formula `(End+6)×(floor(End/2)+1)`.

| Endurance | Current Health | Vitality (×10) | Wounds before incap (current → new) |
|-----------|---------------|----------------|--------------------------------------|
| 1 | 14 | 10 | 2 → 1 |
| 2 | 24 | 20 | 3 → 2 |
| 3 | 27 | 30 | 3 → 3 |
| 4 | 40 | 40 | 4 → 4 |
| 5 | 44 | 50 | 4 → 4 |
| 6 | 60 | 60 | 5 → 5 |
| 7 | 65 | 70 | 5 → 5 |

Low-End characters become slightly more fragile (correct — minimal attribute investment should not be padded). Mid-to-high matches exactly or gains slightly.

### 4.2 Stamina (action economy resource)

| Property | Value |
|----------|-------|
| Formula | Endurance × 5 |
| Range | 5–35 |
| Direction | Drains down from max |
| Depleted at | 0 (Out of Breath: −2D all combat rolls) |
| Recovery | Take a Breath: restores (Endurance + relevant combat History) × 2, capped at max |
| Equipment | Heavy armor: +2 drain per action. Medium: +1. Light/none: +0. |

**Variable action costs:**

| Action | Stamina Cost |
|--------|-------------|
| Standard attack | 5 |
| Heavy/special attack | 8 |
| Defensive stance | 3 |
| Dodge/disengage | 4 |
| Special maneuver (Feint, Disarm, etc.) | 6–10 |
| Movement (per zone) | 2 |

End 4: Stamina 20. Standard attacks at 5/round: 4 rounds before Out of Breath. Heavy armor (+2): effective 7/round, ~3 rounds. Take a Breath with History 3: restores (4+3)×2 = 14.

**Eliminates:** Current formula `End + History + 1 − armour_mod`. History moves to recovery. Armour moves from base reduction to drain modifier (Battle Brothers precedent: armor adds to per-action fatigue cost, doesn't reduce max fatigue).

**Precedent:** Battle Brothers fatigue system. Variable action costs create pre-combat decisions (loadout) and in-combat decisions (burst vs sustain). Viable in videogame because UI handles math.

**UI note:** Equipment screen should display "Estimated combat rounds: N" based on loadout weight and Endurance. No hard Endurance gate for armor — the Stamina math IS the gate.

---

## §5 — Personal Scale: Social Contest Resources

### 5.1 Composure (survival resource)

| Property | Value |
|----------|-------|
| Formula | Charisma × 3 |
| Range | 3–21 |
| Direction | Strain accumulates toward threshold; Rattled when strain ≥ Composure |
| Depleted at | Rattled: +1 Ob per Rattled level to all contest rolls (cumulative) |
| Recovery | Full restore at scene change (unchanged) |
| Equipment | Court attire +2, Crown regalia +4, formal robes +3. Emotional state: +3 in own court, −3 confronting personal enemy. |

Strain per exchange: rescaled ×3.
Charisma modifier (attacker): `max(0, floor((Cha−3)/2)) × 3`. Range 0–6.
Focus defense (defender): `floor(Foc/2) × 3`. Range 0–9.

**Eliminates:** Current formula `Cha + 6`. Removes the +6 constant. Low-Cha characters become appropriately fragile in social contests.

### 5.2 Concentration (action economy resource)

| Property | Value |
|----------|-------|
| Formula | Focus × 3 |
| Range | 3–21 |
| Direction | Drains down from max |
| Depleted at | 0 (Spent: −2D next exchange, opponent +1D; then resets to max) |
| Depletion rate | −3 per exchange; −3 additional on exchange loss |
| Recovery | Regroup forfeit action: restores to max (Focus × 3) |

**Eliminates:** Current formula `Focus + Recall`. Recall removed — has no conceptual connection to sustained mental focus. Recall already provides +2D citation bonus in the Argue step (correct role for knowledge/memory). Concentration is sustained focus under pressure, governed by Focus alone.

---

## §6 — Personal Scale: Thread Resources

### 6.1 Thread Fatigue (action economy resource)

| Property | Value |
|----------|-------|
| Formula | Spirit × 5 (threshold) |
| Range | Threshold 5–35 |
| Direction | **Counts up from 0** toward threshold |
| Threshold reached | Thread exhaustion: contact breaks involuntarily, cannot re-establish until rested |
| Recovery | Full rest: resets to 0. Meditation: reduces by Spirit score. |
| Equipment | Thread-conductive artifact: −1 fatigue/round. Einhir proximity: +3/round. Stimulant herbs: threshold +5 temporarily. |

**Per-operation fatigue costs:**

| Operation | Fatigue/Round |
|-----------|--------------|
| Leap (entry cost, one-time) | 3 |
| Passive sensing | 2 |
| Mending | 4 |
| Pulling | 5 |
| Locking | 7 |
| Dissolution | 10 |

**Focus role change:** Focus no longer sets contact duration. Contact Rounds eliminated. Focus sets maximum operations per contact session, preserving current `Focus − 1` cap:

| Focus | Max Operations per Session |
|-------|---------------------------|
| 1 | 0 (experience only) |
| 2 | 1 |
| 3 | 2 |
| 4 | 3 |
| 5+ | 4+ |

Spirit 6 / Focus 2: high threshold (30), sustained contact, but only 1 operation — endurance without skill. Spirit 2 / Focus 6: low threshold (10), exhausts quickly, but 5 operations if endurance allowed — skill without staying power.

**Coherence** (survival resource): unchanged. 10→0 countdown. Not a derived value — a permanent degradation track.

---

## §7 — Unit Scale: TroopCount

| Property | Value |
|----------|-------|
| Formula | Size × block_size (set at muster) |
| Direction | Drains down |
| Depleted at | TroopCount < block_size (Size = 0, unit destroyed) |

**block_size by battle scale** (canonicalizes A.3 narrative table):

| Scale | block_size |
|-------|-----------|
| Skirmish | 10 |
| Company | 100 |
| Battle | 500 |
| Campaign | 1,000 |
| War | 5,000 |

**Size** (1–7) becomes a computed integer: `Size = floor(TroopCount / block_size)`. All combat formulas reference Size unchanged: `Pool = min(Size, Command) + Command`.

**Output scaling:** `effective_damage = floor(successes × (1 + Power) × TroopCount / max_TroopCount)`, where `max_TroopCount = Size_at_muster × block_size`. Ratio is always ≤ 1.0 (capped — reinforcement above muster grants pool dice via Size increase, not output bonus). Damage degrades smoothly as troops are lost. No discontinuities at Size boundaries. A unit at 4,600 / 5,000 deals 92% damage; at 3,000 / 5,000 deals 60% damage. The pool die loss at Size thresholds provides the cliff drama; output scaling provides the continuous degradation between cliffs.

**Health layer (engine-only):** `Total Health = Size_at_muster × H`, where `H = min(Discipline, Command) + DR`. Unchanged. TroopCount = `floor(current_Health × block_size / H)`.

Player sees: **"Heavy Infantry — 4,428 / 5,000 (Size 4)"**

---

## §8 — Faction Scale

| Stat | Derived Value | Derivation | What It Represents |
|------|--------------|------------|-------------------|
| Mandate | **Legitimacy** | Mandate × 20, starting = stat × 20 | Popular/institutional trust capital |
| Wealth | **Treasury** | Wealth × 100, starting = stat × 100 | Accumulated economic resources |
| Military | **Levies Available** | Military × 2 (ceiling) | Force projection capacity — not spendable, constrains active unit count |
| Influence | **Reputation** | Influence × 15, starting = stat × 15 | Political capital across factions |
| Stability | **Cohesion** | Stability × 10, starting = stat × 10 | Internal faction unity |

### 8.1 Income and Drain

Each derived value has **seasonal income** (automatic at Accounting) and **drains** (from actions, events, ongoing costs).

**Treasury (from Wealth):**
- Seasonal income: Σ(Prosperity of controlled settlements) × 10 gold/season
- Trade Success: +Wealth × 25 gold (one-time)
- Trade Overwhelming: +Wealth × 50 gold
- Haushalt Competence bonus: +Competence × 25 gold/season (Competence 0–3). Cap: Haushalt Competence income cannot exceed Wealth × 50 per season. (ED-663 resolution)
- Campaign Supply (units in hostile territory): −100 gold/season
- Siege (attacker): −100 gold/season per active siege
- Muster (Levy): −50 gold
- Muster (Professional): −150 gold
- Muster (Heavy Infantry/Cavalry): −300 gold
- Muster (Artillery): −500 gold
- Unit upkeep (professional units, per season): −25 gold per unit
- Construction (Fortify, infrastructure): −200 gold per action

**When Treasury reaches 0:** Faction cannot Muster, Fortify, or perform gold-cost actions. Professional units begin Discipline degradation (−1/season). At NEXT Accounting where Treasury is still 0: **Wealth −1** (structural economic damage). Only routine path from derived value depletion to stat damage.

**When Wealth stat drops:** Treasury maximum drops (new max = Wealth × 100). Current Treasury retained. Recovery requires Trade actions.

**Legitimacy (from Mandate):**
- Seasonal income: +5 per territory at Accord ≥ 2
- Successful Govern action: +Mandate × 5
- Consensus Delay override (RM): −20
- Emergency authority invocation: −30
- Unpopular Domain Action (drops Accord): −15
- Battle in own territory: −10
- Peninsular Strain Mandate check failure: Legitimacy −25 AND Mandate −1

**When Legitimacy reaches 0:** Mandate check at Accounting (Ob 2). Failure: Mandate −1. Accord −1 in all territories.

**Reputation (from Influence):**
- Seasonal income: +5 per diplomatic relationship at Disposition ≥ +2
- Successful Intel/Spy: +Influence × 5
- Successful Diplomacy: +Influence × 10
- Failed diplomatic initiative: −15
- Exposed Niflhel/Altonian operation: −50
- Church Attention triggered: −10
- Casus Belli declared against faction: −20

**When Reputation reaches 0:** Diplomatic and Intel actions +1 Ob. At next Accounting still at 0: Influence −1.

**Cohesion (from Stability):**
- Seasonal income: +10 per peaceful season
- Successful Govern: +5
- Battle loss: −15
- Accord drops to 0 in any territory: −20
- Faction leader death/succession: −30
- Coup (Löwenritter): −50
- Internal faction schism: −40

**When Cohesion reaches 0:** Stability check at Accounting (Ob 1). Failure: Stability −1. Cohesion drain at Stability ≤ 2 triggers faction collapse checks.

**Levies Available (from Military):** Ceiling, not spendable. Military × 2 = max active units. If Military drops, ceiling drops — disband excess units.

### 8.2 Stat Damage Only From Structural Failure

**No game event directly modifies a 1–7 stat except through derived value depletion or explicit major events.**

Events that SHOULD still directly modify stats (major structural shifts): faction collapse triggers, coup, CI=100 Mass Seizure, Altonian Occupation, Parliamentary Outlawry, Generational Shift, Peninsular Strain ≥7, Trade/Govern Overwhelming, decisive battle loss (margin ≥2), unit destruction.

The dividing line: "bad quarter" (derived drain) vs "fundamentally weakened" (stat damage).

---

## §9 — Settlement Scale (PENDING)

Architecture supports settlement-level derived values:

| Settlement Stat | Derived Value | Derivation |
|----------------|---------------|-----------:|
| Prosperity | **Local Economy** | Prosperity × 50 |
| Defense | **Garrison Strength** | Defense × 20 + Fort Level × 30 |
| Order | **Public Order** | Order × 20 |

Multipliers and interaction design pending settlement_v30 development. Not canonicalized.

---

## §10 — Cross-Scale Bridges

### 10.1 Disposition Cap by Bonds Attribute

Disposition ceiling = Bonds (PP-684). Bonds is structural capability (how deep relationships CAN go). Disposition is current state (how deep this relationship IS). Pattern identical to Wealth→Treasury.

Companion formation (Disposition ≥ +3) requires Bonds ≥ 5. Knot candidacy (Disposition +5) requires Bonds ≥ 5 (achievable at creation).

Cross-reference: fieldwork_v30 §5.1, params_core §Bonds (PP-632/PP-684), companion_specification §2.1.

### 10.2 Army Morale (Mass Combat Derived Composite)

**Army Morale = floor(average unit Morale) + Command modifier + Cohesion modifier**

| Component | Source | Range |
|-----------|--------|-------|
| Average unit Morale | mean of active units' Morale, floored | 1–7 |
| Command modifier | +1 if Command ≥ 4; −1 if Command ≤ 2 | −1 to +1 |
| Cohesion modifier | +1 if faction Cohesion ≥ 75% of max; −1 if ≤ 25% | −1 to +1 |

Thresholds: 6+ Resolute, 4–5 Steady, 2–3 Shaken (−1D Morale checks, Command check Ob 2 each Cascade), 1 Wavering (−2D, Withdrawal unless rally Ob 3), 0 Routed (army-level rout, battle lost).

### 10.3 Renown ↔ Derived Value Bridge

When player holds governance position (Standing ≥ 3), faction derived value drains from governance failures apply Renown penalties:

| Event | Derived Value Drain | Renown Consequence |
|-------|--------------------|-------------------|
| Accord drops in governed territory | Cohesion −20 | Governor: Renown −1 |
| Treasury reaches 0 while faction officer | Wealth −1 at Accounting | Counselor+: Renown −1 |
| Battle loss in governed territory | Cohesion −15 | Governor: Renown −1 |
| Faction Stability reaches 0 | Faction collapses | Member: Renown −2 |

Renown governance penalties cap at −2 per season. Does not decay below 0.

### 10.4 Settlement Combat Defense Feedback

| Combat Outcome | Garrison Strength Effect |
|----------------|------------------------|
| Player wins defense (repels attacker) | Garrison Strength +10 |
| Player wins with Overwhelming | Garrison Strength +20 + Public Order +5 |
| Player loses defense | Garrison Strength −10 |
| Settlement falls during player defense | Garrison Strength → 0, Defense stat check Ob 2 at next Accounting |

Personal combat outcome → settlement derived value → faction derived value income: the most complete personal→faction feedback loop.

---

## §11 — Stat Modification Conversion Registry (PP-680)

Audit of all 51 stat ±1/±2 references. Classified as CONVERT (routine → derived drain) or KEEP (structural → direct stat modification).

### Converted to Derived Value (routine fluctuations):

| Original | Converted To | Files Affected |
|----------|-------------|----------------|
| Campaign Supply: Wealth −1/season | Treasury −100/season | mass_battle_v30 |
| Battle Partial: Stability −1 | Cohesion −15 | mass_battle_v30, military_layer_v30 |
| Battle loss (routed): Stability check Ob 1 | Cohesion −15 | mass_battle_v30 |
| Campaign defeat: Stability check Ob 2 | Cohesion −30 | mass_battle_v30 |
| Siege supply: Wealth −1/season | Treasury −100/season | military_layer_v30 |
| Siege failure: Stability −1 | Cohesion −15 | military_layer_v30 |
| Siege parley rejected: Stability −1 | Cohesion −15 | military_layer_v30 |
| Assert failure: Stability −1 | Cohesion −15 | tc_political, victory_v30 |
| Suppress failure: Stability −1 | Cohesion −15 | tc_political, victory_v30 |
| Govern failure at Prosperity 0: Stability −1 | Cohesion −15 | tc_political |
| Trade Success: Wealth +1 | Treasury +Wealth×25 | tc_political |
| Strain 3–4: Mandate check → Mandate −1 | Legitimacy −25 | tc_political, peninsular_strain |
| Seizure failure: Stability −1 | Cohesion −20 | peninsular_strain |
| Proclamation failure: Stability −1 | Cohesion −20 | peninsular_strain |
| Cultural Reformation failure: Stability −1 | Cohesion −20 | peninsular_strain |
| IP 90 inter-faction Battle: Stability −1 | Cohesion −20 | victory_v30 |
| Settlement expansion: Wealth −3 | Treasury −300 | settlement_layer |
| Mine surplus: Wealth +1 | Treasury +50/season | settlement_layer |

### Kept as Direct Stat Modification (structural events):

| Event | Stat Change | Rationale |
|-------|-----------|-----------|
| Battle loss (margin ≥2): Military −1 | KEEP | Decisive loss IS structural military damage |
| Unit destroyed: Military −1 | KEEP | Permanent force loss |
| Campaign defeat: Mandate −1 | KEEP | Major political event |
| Crown Treaty: target Mandate −1 | KEEP | Diplomatic victory — structural |
| Appease (Institutional Mandate): Mandate −1 | KEEP | Deliberate institutional sacrifice |
| Parliamentary Censure/Outlawry: Mandate −1/−2 | KEEP | Formal political action |
| Crown-break: Stability −2, Mandate −1 | KEEP | Treaty betrayal — structural crisis |
| RM Uprising: Church Mandate −2/−1 | KEEP | Loss of territory — structural |
| Dynastic Proclamation success: target Mandate −1 | KEEP | Major political act |
| Trade Overwhelming: Wealth +1 | KEEP | Exceptional success = structural improvement |
| Govern OW in capital: Mandate +1 | KEEP | Exceptional governance = structural |
| Faction collapse triggers | KEEP | Terminal events |
| Coup, Occupation, Generational Shift | KEEP | Campaign-altering events |
| Peninsular Strain ≥7: Mandate check | KEEP | Existential crisis level |

---

## §12 — What Changes from Current Systems

| Current System | Change | Rationale |
|---------------|--------|-----------|
| Health = (End+6) × (floor(End/2)+1) | → Vitality = End × 10 | Simpler, eliminates Max Wounds, opens equipment space |
| Max Wounds = floor(End/2)+1 | → Eliminated | Wounds computed on the fly: floor(damage / Wound_Interval) |
| Stamina = End + History + 1 − armour | → Stamina = End × 5; History → recovery; armour → drain modifier | Single-attribute base, variable action costs, BB precedent |
| Composure = Cha + 6 | → Composure = Cha × 3 | Removes +6 constant, opens social equipment space |
| Concentration = Focus + Recall | → Concentration = Focus × 3 | Removes Recall (wrong attribute), single-attribute derivation |
| Contact Rounds = Focus | → Thread Fatigue threshold = Spirit × 5; Focus → max ops per session | Separates duration (Spirit) from skill (Focus), variable costs |
| Size (1–7 stored stat) | → TroopCount = Size × block_size; Size computed | Sub-Size visibility, output scaling, reinforcement decisions |
| A.3 scale table (narrative only) | → block_size canonicalized | Required for TroopCount derivation |

## §13 — What Does NOT Change

- Dice engine: d10, TN 6/7/8, integer pools, integer Ob, degree table
- Combat Pool: (Agi × 2) + History + 3, split offense/defense
- Wound Interval: End + 6
- Wound penalty: −1D per wound (cumulative)
- DR / armor damage reduction tables
- All faction stat → dice pool relationships
- All mass combat formulas (Pool, H, damage per success)
- Coherence (10→0 countdown), Certainty (0–5), Momentum (0–4)
- Social contest: Argue pools, genre/orientation, Conviction Track, interaction types
- Thread operations: Leap procedure, operation types, co-movement, Ob values
- Disposition Track, Renown Track, Standing
- TC, PT, Accord, RS, IP — already distinct tracked values

---

## §14 — Complete Derived Value Map

| Scale | Stat | Derived Value | Multiplier | Direction |
|-------|------|--------------|-----------|-----------|
| Personal | Endurance | **Vitality** | ×10 | Drains down |
| Personal | Endurance | **Stamina** | ×5 | Drains down |
| Personal | Charisma | **Composure** | ×3 | Drains down |
| Personal | Focus | **Concentration** | ×3 | Drains down |
| Personal | Spirit | **Thread Fatigue** | ×5 (threshold) | Counts up |
| Unit | Size | **TroopCount** | ×block_size | Drains down |
| Faction | Mandate | **Legitimacy** | ×20 | Drains down |
| Faction | Wealth | **Treasury** | ×100 | Drains down |
| Faction | Military | **Levies Available** | ×2 | Ceiling |
| Faction | Influence | **Reputation** | ×15 | Drains down |
| Faction | Stability | **Cohesion** | ×10 | Drains down |
| Settlement | Prosperity | **Local Economy** | ×50 | PENDING |
| Settlement | Defense | **Garrison Strength** | ×20+Fort | PENDING |
| Settlement | Order | **Public Order** | ×20 | PENDING |

[EDITORIAL: ED-694 — Derived stat system v2. Architectural redesign for videogame layer. Supersedes prior PROPOSAL. Extends personal-scale derived values (Vitality, Stamina, Composure, Concentration, Thread Fatigue), adds unit-scale TroopCount with output scaling, preserves all faction-scale values and PP-680 registry. Does not modify existing dice engine or resolution mechanics.]
