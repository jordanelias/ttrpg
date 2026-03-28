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

Roll Agility dice, Ob 2. Higher net wins. The winner **declares last** — they hear the opponent's plan before committing. Ties: re-roll. Combatants entering an ongoing combat roll initiative immediately on entry and are inserted into the existing declaration order at their result.

### Starting Range

Engagements open at the range appropriate to the distance between combatants at the moment of declaration:

- **Ranged weapons present:** engagement opens at projectile range. Melee combatants must close before any melee exchange is possible.
- **No ranged weapons, combatants not already adjacent:** engagement opens at **Long** range.
- **Combatants already adjacent (grapple, ambush from close quarters, etc.):** engagement opens at **Short** range — narratively determined.

**Ambush**: Ob = ambusher's Tactics History + environment modifier (Ob 1–3). The defender's highest-Cognition character detects. On failure: attackers get one free Priority 2 round and initiative. On success: Agility vs Agility; defender's bonus successes from detection apply.

### Priority Table

| Priority | Action |
|---|---|
| **1** | Instant events; Thread operation effects manifesting from prior rounds |
| **2** | Ranged attacks (in order: arquebus, then crossbow, then drawn bow) |
| **3** | All melee attacks and manoeuvres (sub-rules below) |
| **4** | Standard actions (Diagnosis; draw backup weapon; non-combat single actions) |
| **5** | Full-round actions (the Leap; Locking or Snapping; sustained movement) |
| **6** | Second actions; reload after firing |

#### Priority 3 Sub-Rules

**A — Manoeuvres resolve before attacks.** Disarm, Trip, Tie Up, Rescue, Reorient, Defend!, and Withdraw all resolve before standard attacks within Priority 3.

**B — Range bands.** Every melee weapon has a Reach classification: **Short** or **Long** (see §8.2). The current range band of an engagement is a shared state tracked each round.

- **Wrong range = cannot attack.** A Short weapon fighter at Long range cannot strike. A Long weapon fighter at Close range cannot swing. The offensive action must be spent on Reorient or Withdraw to change the band.
- **Same range:** both fighters may attack. Weight/speed determines attack order (Fast before Standard before Slow).
- **Contested range change:** the opponent may spend their own offensive action to contest a Reorient or Withdraw (Agility vs Agility). Winner sets the range band for this round. Loser may not attack.
- **Versatile weapons** (see §8.2) may attack at either range band at −2D to the offensive pool without repositioning. The opponent's ability to contest via manoeuvre is unaffected.

**C — Rescue limitation.** Rescue redirects melee attacks and Priority 4+ attacks only. It cannot redirect Priority 2 (ranged) attacks — those resolve before Priority 3. To absorb a ranged attack for an ally, physically interpose (declare yourself the target through positioning).

### Attacks

**Attack pool** = Combat History pool (primary attribute included). Use the pre-printed pool number.

**Defense options** (all defensive pools roll against Ob = attacker's net successes):

| Option | Pool | Notes |
|---|---|---|
| Dodge Backwards | Agility | Standard evasion |
| Duck and Weave | Agility | Higher-stakes evasion; Partial produces a complication |
| Parry | Combat History pool | Melee only. If Parry declared and ranged attack received: automatically switches to Dodge Backwards |
| Shield | Agility | Shield bonus applies |

### Damage

**Weapon damage bonus + excess attack successes − armour damage reduction (minimum 0)**

Excess attack successes = attacker's net − defender's net (minimum 0).

*Example: Attacker net 5, defender net 3 → 2 excess. Power 3 + weapon +1 + 2 excess = 6 damage before armour.*

**Exploding damage**: A damage die showing 10 → re-roll. Failure on re-roll: +1 damage. Success: +2 damage and re-roll again. Continue until failure.

### Combat Manoeuvres (Priority 3A — all use Combat History pool)

**Manoeuvre and attack are mutually exclusive.** Declaring any manoeuvre is your offensive action for the round.

#### Defensive Manoeuvres

**Defend!**
Full defensive posture. Your entire Combat Pool shifts to Defence this round — no Offence allocation. Opponent must roll their full Offence against your full pool. On Overwhelming success (your net ≥ opponent net by 3+): opponent is held at bay and loses their offensive action next round. On Success: opponent cannot close range or reposition this round. On Partial: you hold but take a complication (stumble, ground loss). Use when outnumbered or outmatched — buying time costs nothing but the offensive initiative.

**Rescue**
Redirect a melee or Priority 4+ attack targeting an ally to yourself. Roll Endurance vs Ob = incoming attack net successes. Success: you absorb the hit; ally is unaffected. Failure: both of you take the hit (split excess successes between targets). Cannot redirect Priority 2 (ranged) attacks — physically interpose instead by declaring yourself the target during Planning Phase.

---

#### Reach Management Manoeuvres

**Reorient**
Change the active range band (Short ↔ Long). Contested: Agility vs Agility. Winner sets the range band for this round; loser may not attack. Ties: Long range holds. Either fighter may initiate; opponent may spend their offensive action to contest or concede (and attack freely at current range). Can be used to exploit terrain features — see Exploit Terrain below.

**Withdraw**
Sacrifice offensive action to re-establish preferred reach advantage without contesting. If unopposed: automatic success. If opponent contests (spends their offensive action): resolve as Reorient. Used when you cannot risk a contested roll.

---

#### Offensive Manoeuvres

**Disarm**
Knock, lever, or strip the weapon from the opponent's grip. Agility vs Agility, Ob = opponent's net successes. On Success: weapon lands 1d3 feet away in a random direction; opponent must spend a Priority 5 action to retrieve it or draw a backup weapon at Priority 4. On Overwhelming: you catch or control the weapon — your choice whether to pocket it, throw it, or press it back against them. If the opponent has no backup weapon: they are unarmed and may only Grapple, Shove, or Flee.

**Trip**
Knock the opponent off their feet. Agility vs Agility. On Success: target is prone.
- Prone attacker: −2D to Combat Pool
- Attacks against a prone target: +2D to Combat Pool
- Standing from prone: costs a full Priority 5 action (cannot attack that round)
- A prone character may crawl (half speed) or attempt to roll clear (Agility Ob 2; failure = remain prone)

**Tie Up**
Lock weapons together, preventing either from attacking this round. Power vs Ob = opponent's net successes. On Success: both weapons are locked; neither deals damage this round. On Overwhelming: you control the bind — you may immediately transition to Grapple (see below) without spending another action. On Failure: your weapon is locked but opponent's is not; they attack at +1D this round.

**Grapple**
Seize the opponent bodily — closing past their weapon to control their body. Requires Close range. Power vs Power. On Success: opponent is Grappled.
- Grappled: cannot attack with Long weapons; Short weapon attacks at −1D; cannot Reorient or Withdraw
- Grappler: may deal unarmed damage (Power − opponent armour DR, minimum 0) each round as a free action; no weapon attack
- Escape: Power vs Grappler's Power, costs offensive action
- A Grapple can be initiated directly from a successful Tie Up (Overwhelming) or from Close range after winning a Reorient

**Shove**
Drive the opponent backward through raw momentum. Power vs Agility. On Success: opponent is pushed one range band away from you (Short → Long or out of melee entirely). On Overwhelming: opponent is pushed into a terrain feature — GM assigns a complication (stumble, blocked path, environmental hazard). On Failure: you overextend; opponent may attack you at +1D this round. Shove does not deal damage but disrupts positioning — useful to break a Grapple, push an opponent off a ledge, or create space for a ranged ally.

**Called Shot**
Declare a specific target location before rolling. +Ob 2 to the attack. On hit, apply the standard damage plus the location effect:

| Target | Effect on hit |
|---|---|
| Weapon arm | Opponent's Combat Pool −2D next round; Overwhelming = Disarm (no separate roll) |
| Legs | Opponent's movement halved; Overwhelming = Trip (no separate roll) |
| Head | Opponent takes Composure damage equal to excess successes; Overwhelming = Stunned (lose next offensive action) |
| Weapon hand | Opponent's grip weakened; −1D to their next attack |

Called Shots cannot be declared against opponents in Heavy armour on the targeted location — the coverage negates the precision effect (damage still applies, location effect does not).

---

#### Psychological Manoeuvres

**Feint**
A committed false attack designed to draw and waste the opponent's defensive allocation. Declare during Planning Phase as your offensive action. Resolution: roll Combat History pool vs opponent's Cognition (Ob = their net successes). On Success: opponent's defensive dice allocation this round is treated as misdirected — their effective Defence pool is halved (rounded down) against your *next* attack (following round). On Overwhelming: their Defence pool is negated entirely for one attack next round. On Failure: opponent reads the feint; they gain +1D to their defensive pool next round.

A Feint costs this round's offensive action and pays off next round — it is a setup, not an immediate attack. Opponents aware of a Feint pattern (same character feinting twice in three rounds) may call it: Cognition check Ob 2 to identify and pre-empt, negating the advantage.

**Intimidate**
Weaponise presence, reputation, or a decisive moment (killing a companion, landing a brutal hit) to shake the opponent's nerve. Presence + relevant History vs opponent's Composure (current value as Ob). Declare during Planning Phase; resolve at Priority 3A.

- Success: opponent loses 2D from their Combat Pool next round (fear and hesitation)
- Overwhelming: opponent loses 2D and must pass a Composure check (Ob 2) or spend their next offensive action on Defend! or Withdraw
- Failure: no effect; this opponent cannot be Intimidated again this combat (they've steeled themselves)
- Cannot Intimidate and attack in the same round
- Devout characters with intact Certainty: +2D resistance to Intimidate

---

#### Environmental Manoeuvres

**Exploit Terrain**
Use the environment as a tactical resource — high ground, narrow corridor, slippery surface, furniture, fire. Cognition vs Ob set by GM (1–3 depending on terrain complexity). Declare during Planning Phase; resolve at Priority 3A.

- Success: gain +1D to Combat Pool next round, or deny opponent a specific action (their choice of which) next round
- Overwhelming: both — +1D and deny one action
- Failure: you've committed to a position that didn't pay off; opponent may exploit your overextension (+1D to their next attack)

Terrain features are declared by the GM at scene start or discovered mid-combat. Exploiting the same feature twice requires a new roll at +1 Ob (diminishing returns — the opponent adapts).

### Group Attacks

See §1.9 (Fibonacci Group Bonus) for the canonical group attack bonus table. Bonus dice apply to each attacker's Offence allocation.

**Defence splitting:** When defending against multiple attackers simultaneously, the defender distributes their defence dice across attackers as they choose. This allocation must be declared simultaneously with attackers' pool divisions and cannot be changed after Offence pools are revealed.

### Escaping Combat

A character who wishes to exit an ongoing combat entirely (not just reposition): **Agility check, TN 7, Ob = opponent's Cognition** (their awareness of your intent to flee; minimum Ob 1). Declare intent at Phase 1.

- **Success:** Character exits combat. They arrive at the scene's edge at Priority 6, Stamina set to 0.
- **Failure:** Opponent gets one free Priority 3 attack against the fleeing character before they exit. Character still exits on failure — they are not trapped.
- **Group flight:** Each character rolls separately. Failure on any character does not prevent others from succeeding.

### Stunts

Player sets their own critical success range (up to 11–20); the critical failure range expands by the same amount. A result in neither zone: Partial, with a GM-assigned complication. Stunts are a player tool — the GM does not impose them.

---

## 8.2 Weapons and Armour

Weapons and armour provide modest modifiers. History pool (skill) dominates over equipment. This is intentional — a novice with a great sword loses to a skilled soldier with a knife.

### Weapons

Weapons have two independent axes: **Weight** (governs damage bonus and speed) and **Reach** (governs which range band the weapon can attack from).

**Weight**

| Weight | Damage Bonus | Speed |
|---|---|---|
| Light | +1 | Fast |
| Medium | +2 | Standard |
| Heavy | +4 | Slow |

**Reach**

| Reach | Attack Band | Notes |
|---|---|---|
| Short | Close range only | Cannot attack at Long range |
| Long | Long range only | Cannot attack at Close range |
| Ranged | Projectile range only | Fires at Priority 2. At Close range: locked out — must Withdraw to re-establish distance before firing. Reload at Priority 6. |

**Valid profiles (Weight × Reach):** all nine combinations are legal. Weapon archetype determines the combination — no single axis constrains the other.

**Weapon TN (d10 dice pool — success = die result ≥ TN):**

| Weight | Attack TN | Parry TN |
|---|---|---|
| Light | 5 | 6 |
| Medium | 6 | 7 |
| Heavy | 7 | 8 |

Ranged weapons use their weight's Attack TN. Ranged weapons have no Parry TN — cannot parry. Dodge always TN 7 regardless of weapon.

**Strength minimums:**

| Weight | Str Minimum | 1 Below Minimum | 2+ Below Minimum |
|---|---|---|---|
| Light | None | — | — |
| Medium | 3 | −1D Combat Pool | Cannot wield |
| Heavy | 4 | −1D Combat Pool | Cannot wield |

Strength does not add to damage. It gates access to heavier weapons only.

**Damage bonus by Weight:** +1 (Light) / +2 (Medium) / +4 (Heavy).  
**Attack order when same range:** Fast before Standard before Slow.

### Armour

Armour provides damage reduction and has Strength requirements. It does not penalise dodge, agility, or acrobatics rolls.

| Armour | Damage Reduction | Str Minimum | 1 Below Minimum | 2+ Below Minimum | Stamina Maximum |
|---|---|---|---|---|---|
| None | 0 | — | — | — | End + 1 |
| Light | 1 | None | — | — | End + 1 |
| Medium | 2 | 3 | −1D Combat Pool | Cannot wear | End |
| Heavy | 3 | 4 | −2D Combat Pool | Cannot wear | End − 2 |

**Stamina maximum** is reduced by armour weight as above. A character wearing Heavy armour with End 3 has Stamina max 2 — they exhaust rapidly in sustained melee. Stamina minimum is 1 regardless of armour.

**Strength minimum** applies to Medium and Heavy armour only. Light armour has no Strength requirement and no pool penalty — it is available to any character. Heavy armour penalty is −2D (not −1D).

**Special properties:**
- **Versatile:** May attack at either Short or Long range without repositioning, at −2D to the offensive pool. The opponent's ability to contest range via Reorient or Withdraw is unaffected — Versatile means the weapon can reach, not that positioning has been won.
- **Thread-locked item:** Fixed stats; cannot be degraded or destroyed through ordinary means.

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
- Officer **Agility**: adds dice to unit attack rolls.
- Officer **Spirit**: adds dice to unit Cohesion checks.
- Officer **Memory**: allows one conditional order per round beyond standard declaration.

### Declaration Structure

Same simultaneous declaration as personal combat. Both sides declare:
1. **Disposition** (Balanced / Defensive / Offensive / Brutal)
2. **Manoeuvre** (Advance / Hold / Withdraw / Flank / Bombard)

### Disposition Interaction Table

Read: attacker's row, defender's column. Apply Ob and pool modifier to the attacker's pool (Martial + Commander Agility ± modifier).

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

**Routed**: Cannot take ordered actions. Rally requires an officer with Agility 4+ to spend their action (Spirit roll, Ob 2).

Units that survive a battle gain +1 to a randomly selected stat, once per campaign season (veteran bonus).

### Three-Way Mass Combat

1. All three sides declare dispositions simultaneously.
2. Determine primary conflict (who is fighting whom); resolve secondary force declarations.
3. Apply disposition table for each attacking pair independently.
4. Resolve all attacks simultaneously using the standard priority table.
5. **Three-way initiative**: all three sides roll Agility. Highest net declares last. Second highest declares second-to-last. Lowest declares first with least information.

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

### Fortification Construction

**Build Fortification (Domain Action):** Roll Wealth vs Ob = current Fortification level + 1 (minimum Ob 1). One season. Cannot construct while under active siege. Maximum Fortification: 5.

| Degree | Effect |
|---|---|
| Overwhelming | Fortification +1. Prosperity unchanged. |
| Success | Fortification +1. Prosperity −1. |
| Partial | Incomplete. Re-roll next season at Ob −1. |
| Failure | Fails. Prosperity −1. Retry next season. |

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


