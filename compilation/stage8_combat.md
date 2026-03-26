# PART EIGHT: COMBAT

Combat in Valoria uses simultaneous declaration with sequential priority resolution. Skill dominates over equipment. The system operates at two scales: **personal combat** (individual characters) and **mass combat** (military units). Both use the same dice engine. Thread operations interact with combat at Priority 1 (effects manifest) and Priority 5 (operations initiated).

---

## 8.1 Personal Combat

### Declaration Structure

Each round opens with a **Planning Phase**: each character declares one offensive action and one defensive posture simultaneously before any resolution occurs. Offensive actions resolve at their Priority; defensive postures apply reactively to all incoming attacks.

- No offensive action declared → character may declare two defensive postures instead.
- Move action as primary offensive → Dodge Backwards is the default defensive posture.
- Ranged character engaged in melee with no melee weapon drawn → defend at Coordination only, Ob 2; draw backup weapon at Priority 4; use it at Priority 6.

### Initiative

Roll Coordination dice, Ob 2. Higher net wins. The winner **declares last** — they hear the opponent's plan before committing. Ties: re-roll.

**Ambush**: Ob = ambusher's Tactics History + environment modifier (Ob 1–3). The defender's highest-Cognition character detects. On failure: attackers get one free Priority 2 round and initiative. On success: Coordination vs Coordination; defender's bonus successes from detection apply.

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
| Dodge Backwards | Coordination − armour penalty | Standard evasion |
| Duck and Weave | Coordination − armour penalty | Higher-stakes evasion; Partial produces a complication |
| Parry | Combat History pool | Melee only. If Parry declared and ranged attack received: automatically switches to Dodge Backwards |
| Shield | Coordination | Shield bonus applies |

### Damage

**Power + weapon damage bonus + excess attack successes − armour (minimum 0)**

Excess attack successes = attacker's net − defender's net (minimum 0).

*Example: Attacker net 5, defender net 3 → 2 excess. Power 3 + weapon +1 + 2 excess = 6 damage before armour.*

**Exploding damage**: A damage die showing 10 → re-roll. Failure on re-roll: +1 damage. Success: +2 damage and re-roll again. Continue until failure.

### Combat Manoeuvres (Priority 3A — all use Combat History pool)

| Manoeuvre | Versus | Effect |
|---|---|---|
| Defend! | Coordination | Hold at bay; deny target's move action next round |
| Disarm | Coordination vs Coordination | Target drops weapon |
| Trip | Coordination vs Coordination | Target prone: −2D attack, attacks vs prone +2D, double cost to stand |
| Tie Up | Power | Lock weapons; no damage to either this round |
| Rescue | Endurance | Redirect melee / Priority 4+ attack from ally to self |
| Reorient | Cognition | Manipulate relative positioning; may establish or deny reach advantage |
| Withdraw | Coordination | Sacrifice offensive action; re-establish reach advantage |

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
- Officer **Coordination**: adds dice to unit attack rolls.
- Officer **Heart**: adds dice to unit Cohesion checks.
- Officer **Memory**: allows one conditional order per round beyond standard declaration.

### Declaration Structure

Same simultaneous declaration as personal combat. Both sides declare:
1. **Disposition** (Balanced / Defensive / Offensive / Brutal)
2. **Manoeuvre** (Advance / Hold / Withdraw / Flank / Bombard)

### Disposition Interaction Table

Read: attacker's row, defender's column. Apply Ob and pool modifier to the attacker's pool (Martial + Commander Coordination ± modifier).

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

**Routed**: Cannot take ordered actions. Rally requires an officer with Coordination 4+ to spend their action (Heart roll, Ob 2).

Units that survive a battle gain +1 to a randomly selected stat, once per campaign season (veteran bonus).

### Three-Way Mass Combat

1. All three sides declare dispositions simultaneously.
2. Determine primary conflict (who is fighting whom); resolve secondary force declarations.
3. Apply disposition table for each attacking pair independently.
4. Resolve all attacks simultaneously using the standard priority table.
5. **Three-way initiative**: all three sides roll Coordination. Highest net declares last. Second highest declares second-to-last. Lowest declares first with least information.

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
