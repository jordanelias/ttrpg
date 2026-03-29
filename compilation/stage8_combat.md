# PART EIGHT: COMBAT

Combat in Valoria uses a simultaneous pool-split system derived from historical fighting manuals — Fiore dei Liberi, George Silver, the Liechtenauer tradition, Talhoffer, Meyer. Every round, each fighter divides their Combat Pool between Offence and Defence. All pools resolve simultaneously. The core tactical decision is commitment: overcommit to offence and you are exposed; overcommit to defence and your opponent acts freely.

The system operates at two scales: **personal combat** (individual characters, §8.1–8.7) and **mass combat** (military units, §8.8). Both use the same dice engine. The mass combat system is a direct abstraction of the personal combat mechanics at unit scale.

---

## 8.1 Combat Pool

**Combat Pool = (Agility × 2) + Relevant History + 3 (minimum 5)**

**Stamina = Endurance + Relevant History + 1** (modified by armour — see §8.5)

**Health = Endurance** (per wound; resets on wound. Armour provides Damage Reduction rather than bonus Health — see §8.5)

Modifiers to Combat Pool:
- Armour: no pool penalty (armour affects DR and Stamina only)
- Wounds: no direct pool reduction (wounds are dramatic thresholds, not cumulative debuffs)
- Fibonacci group bonus: adds to Offence allocation specifically (see §8.7)

---

## 8.2 Round Structure

Each round proceeds in three phases:

**Declaration:** fighters announce action type in ascending Agility order. The initiative holder declares last — they hear the opponent's declared action type before committing their own pool split.

**Pool Division:** each fighter secretly allocates dice between Offence and Defence. Minimum 1 die on each side unless committing fully to one (Full Guard = all Defence; reckless attack = all Offence, rarely advisable).

**Resolution:** all pools roll simultaneously. Hits, damage, and consequences apply simultaneously — fighters can incapacitate each other in the same round.

---

## 8.3 Initiative

Initiative determines declaration order. The holder declares last — a genuine tactical advantage.

**Structural:** the fighter at correct range (their weapon's preferred zone) holds initiative automatically. If only one fighter can attack, they hold it.

**Transfer on hit:** at matched range, the fighter who hits and is not hit gains initiative.

**Transfer via Feint:** a successful Feint grants initiative next round (see §8.6).

**Transfer via Establish Distance:** successful range change grants initiative.

**Contested** (both hit or both miss at matched range): each fighter rolls Agility Ob 2. Winner takes initiative. Ties go to higher Agility; further ties reroll.

---

## 8.4 Actions

A fighter declares exactly one action per round.

| Action | Available When | Effect |
|---|---|---|
| Strike | Correct range, Stamina > 0 | Roll Offence vs opponent Defence. Hit if your successes > theirs. Damage = excess + STR + weapon modifier. |
| Establish Distance | Wrong range, Stamina > 0 | Roll Offence dice at TN 7. Succeed if successes ≥ opponent's Offence successes AND not hit. On success: range shifts, you gain initiative. Auto-succeeds if opponent not attacking (Ob = 0). |
| Feint | Correct range, Stamina > 0 | Roll Offence at hit TN − 1 vs opponent Defence. Success: gain initiative next round. Fails if hit. Direct contest vs Establish Distance: feint successes vs TN 7 successes, tie goes to feint. |
| Take a Breath | Any range, Stamina > 0 | Roll Offence dice at TN 7. Each success restores 1 Stamina (capped at maximum). Fails if hit. |
| Full Guard | Any range, Stamina > 0 | All dice to Defence. Opponent gains +2D Offence. Represents voiding — not meeting force with force. Exempt from mass mismatch penalty. |
| Disarm | Correct range, Stamina > 0 | Roll Offence vs opponent Defence. Success: opponent loses weapon, fights as Unarmed next round. Opponent may Retrieve or continue Unarmed. |
| Retrieve Weapon | Disarmed only | Roll Offence at TN 7 vs opponent Offence successes. Success: weapon recovered; fighter is at wrong range with no initiative next round. |
| Out of Breath | Stamina = 0 (forced) | Stamina restores to maximum. Half pool, Defence only. Opponent gains +2D Offence. |

When opponent is disarmed, the only available actions are Strike or Take a Breath — all other actions are illogical.

---

## 8.5 Weapon System

Weapons are defined by two independent binary axes — **weight** (Light/Heavy) and **type** (Cut/Blunt) — plus **reach** (Short/Long). This is grounded directly in the historical manuals, which consistently organise around fast/slow and sharp/blunt as the primary distinctions.

### Weapon Statistics

| Type | Hit TN | Def TN | Damage Modifier | Examples |
|---|---|---|---|---|
| Light Cut | 5 | 6 | +1 to +2 | Dagger, knife, short sword, spear |
| Heavy Cut | 6 | 7 | +4 to +5 | Longsword, axe, glaive |
| Light Blunt | 6 | 7 | +1 to +2 | Hand axe, short club, sap |
| Heavy Blunt | 7 | 8 | +4 to +5 | War hammer, mace, pollaxe, military pick |
| Unarmed | 8 | 9 | +0 | Fists, grappling, improvised |

Reach (Short/Long) is independent of the above. A dagger is Short Light Cut. A spear is Long Light Cut. A longsword is Long Heavy Cut. A war hammer is Short or Long Heavy Blunt.

### Strength Minimums

| Weapon Weight | Minimum STR | Penalty if 1 below |
|---|---|---|
| Light Cut / Light Blunt | 1 | — |
| Heavy Cut | 3 | −1D Combat Pool |
| Heavy Blunt | 4 | −1D Combat Pool |

Cannot wield if 2 or more below minimum.

### Range and Reach

Range is binary: **Close zone** (Short reach) or **Far zone** (Long reach). A fighter's weapon determines their preferred zone. Fighting outside your preferred zone:

- Short weapons cannot attack at Far zone.
- Long weapons cannot attack at Close zone — but may fight at Close zone at **−1D Offence and half damage** (rounded up), representing choked-up technique (half-swording, butt strikes, shaft leverage). Weapon type is unchanged.

Range is tracked **per fighter pair** in group combat. A fighter pair has an independent zone state.

### Damage Resolution

**Damage = excess successes + STR + weapon modifier**

On a **Critical Hit** (excess ≥ 3): weapon modifier is doubled.

**Damage = excess + STR + (weapon modifier × 2)**

Apply Damage Reduction from the defender's armour (see below). Minimum damage after DR is 0.

### Mass Mismatch Penalty

When a **Light weapon defender splits their pool** against a **Heavy weapon attack**, their defensive successes are reduced by 1 (minimum 0).

Exempt: Full Guard (voiding, not meeting force with force). Exempt: Long weapon at Close zone (heavy weapon already compromised by wrong range).

Grounded in the manuals: Silver and Fiore both note that evasion and geometry are always available answers to a heavier weapon. The penalty applies when the light weapon user chooses to stand and deflect.

---

## 8.6 Armour

Armour provides **Damage Reduction (DR)** per hit rather than bonus Health. DR varies by the attacker's weapon type — heavier and blunter weapons defeat armour more effectively.

### Armour Statistics

| Armour | STR Min | Stamina Mod | vs Light Cut | vs Heavy Cut | vs Light Blunt | vs Heavy Blunt |
|---|---|---|---|---|---|---|
| None | — | +0 | 0 | 0 | 0 | 0 |
| Light | 2 | +0 | 2 | 1 | 1 | 0 |
| Medium | 3 | −1 | 4 | 3 | 2 | 1 |
| Heavy | 4 | −2 | 6 | 5 | 3 | 1 |

Key relationships:
- Light Cut weapons (daggers) against Heavy armour: DR 6 against base damage of 1–2. Effectively useless for damage. Find the gap through manoeuvre or abandon the attempt.
- Heavy Blunt weapons against Heavy armour: DR 1. Near-full damage through. The war hammer and pollaxe were designed specifically to defeat plate.
- Heavy Cut against Heavy armour: DR 5. Requires crits or high excess to deal significant damage — half-swording techniques represent this.

---

## 8.7 Wounds and Stamina

### Wounds

**Health = Endurance** per wound. When Health reaches 0, the fighter takes a Wound and Health resets to full. Maximum wounds before incapacitation:

| Endurance | Max Wounds |
|---|---|
| 1–3 | 2 |
| 4–5 | 3 |
| 6–7 | 4 |

Wounds are dramatic thresholds. A fighter who takes a wound continues at full capacity until incapacitated. There is no wound penalty to the Combat Pool.

### Stamina

**Stamina = Endurance + Relevant History + 1** (modified by armour Stamina Mod).

Stamina depletes by 1 each round any action is taken. At 0, the fighter is **Out of Breath** (forced): Stamina restores to maximum, half pool, Defence only, opponent +2D Offence.

**Take a Breath** (voluntary): restores Stamina before hitting zero, at the cost of forfeiting an attack round.

**Full Guard and Out of Breath** both give the opponent +2D Offence — both represent a fighter who is not threatening their opponent and can therefore be attacked more freely.

---

## 8.8 Group Combat

### Zone Collapse

Range is tracked per fighter pair. When at least one ally has already established Close zone against a target, subsequent Short-reach fighters **enter Close zone automatically** without an Establish Distance roll. The first fighter's presence has collapsed the zone — the heavy weapon can no longer be used at full extension.

Long-reach fighters in the same engagement remain at Far zone and attack from there with full effectiveness.

### Fibonacci Group Bonus

When multiple fighters attack a single unsupported opponent in the same round, each attacker receives bonus Offence dice. The defender **splits their Defence pool across all incoming attacks** before resolution.

| Attackers vs 1 | Bonus Dice (each attacker) |
|---|---|
| 2 vs 1 | +1D each |
| 3 vs 1 | +2D each |
| 5 vs 1 | +3D each |
| 8 vs 1 | +5D each |

An opponent is **unsupported** if no ally is engaging any of the attackers.

**Simulation findings (N=2,000 per matchup):**
- 3v1 is universally decisive (99–100% resolution) regardless of weapon or armour.
- 2v1 is the tactically interesting zone — weapon type, armour, and positioning all affect outcomes.
- Light Cut vs Heavy armoured defender at 2v1: 56% attacker win rate (genuinely contested).
- Heavy Blunt vs Heavy armoured defender at 2v1: 94% — correct weapon type is decisive.
- Tipping point is 3v1, not 2v1.

### Rescue

A fighter may declare **Rescue** as their action. Their current opponent gains +2D Offence this round (the fighter's attention shifts away — equivalent to Full Guard logic). Next round, the rescuing fighter is in their ally's engagement with Fibonacci bonus applied. No roll required.

**Rescue timing:** simulation confirms the viable rescue window is **rounds 1–3**. After round 3, 75–80% of losing fighters have already fallen. Rescue declared at round 5 saves the ally only 43–45% of the time — often too late.

**Rescue beats pile-on:** redirecting to a losing fight is almost always better than piling onto a winning fight. In 3v2 scenarios, rescue produces 86–96% side win rates vs 39–62% for pile-on.

### Multi-Engagement (3v2, 4v3)

In uneven group engagements, decompose into parallel engagements plus a free fighter.

**3v2:** A1+A2 vs B1 (2v1), A3 vs B2 (1v1). A3 joins B1 fight after B2 falls — or rescues A if losing. Both engagements typically resolve at median 3–5 rounds. High draw rate (40–87%) — parallel engagements often resolve simultaneously. The free fighter's **engagement quality** (rescue vs pile-on) matters more than having the free fighter at all.

**4v3:** 2v1 + 1v1 + 1v1. Numerical advantage does not compound reliably unless the free fighter rescues. Three parallel 1v1s where one side has an extra fighter produces only marginal advantage — the extra fighter must be actively committed to a losing engagement to matter.

---

## 8.9 Mass Combat

Mass combat uses the same dice engine as personal combat, abstracted to unit scale. Unit stats map directly from individual combat mechanics.

### Unit Statistics

| Stat | Derived from | Notes |
|---|---|---|
| Weapon Type | Primary weapon type of unit | Light Cut / Heavy Cut / Light Blunt / Heavy Blunt |
| Armour Tier | Unit armour | None / Light / Medium / Heavy |
| Combat Pool | Unit cohesion and training | Equivalent to individual pool; larger for elite units |
| DR | Armour tier vs attacker weapon type | Same table as personal combat |
| Stamina | Unit endurance | Depletes per engagement; OOB = unit is spent |

### Mass Combat Resolution

Each engagement: attacker pool vs defender pool (split by number of attacking units), Fibonacci bonus applied to outnumbering units, DR applied to damage per weapon type vs armour tier. Same critical hit threshold (excess ≥ 3). Same wound structure (units take wounds before breaking).

### Mass Battle Abstractions

**Fibonacci → Flanking modifier.** A flanked unit splits its Defence pool across all attacking units. 3-unit assault on 1 unit breaks that unit within approximately 3 battle turns in almost all configurations.

**Zone collapse → Formation break.** When one unit breaches a formation, adjacent enemy units lose their positional coherence. Subsequent allied units engage without a formation check. Historical basis: Leuctra (371 BC), Cannae (216 BC) — one breach collapses the line.

**Rescue → Reserve commitment.** A reserve unit breaking away from its engagement (costs the enemy +2D that turn) to reinforce a collapsing flank. The 2–3 round survival window maps directly: a unit that has taken one wound needs relief within 2 battle turns or it breaks.

**Weapon type → Unit specialisation.**
- Light Cut units (light infantry, skirmishers): effective in harassment, pursuit, 1v1 engagements. Weak against armoured units.
- Heavy Cut units (line infantry, men-at-arms with swords): dominant in 1v1, effective generally. The strongest general-purpose unit type.
- Heavy Blunt units (billmen, halberdiers, men-at-arms with hammers): specialist anti-armour. Weak against unarmoured light units; decisive against heavy armoured units. Requires numerical support (2v1 minimum) to overcome hit rate disadvantage.

**Armour DR → Unit armour rating.** A Heavy armoured elite unit can hold a 2v1 engagement against Light Cut attackers 44% of the time. It requires either 3v1 or Heavy Blunt attackers to break it reliably. This is the historical basis for elite heavy cavalry and men-at-arms as anchor units.

**Draw rate in 3v2 → Attritional engagement.** When flanks are roughly matched, the battle centre decides. The high draw rate in parallel engagements (40–87%) reflects historical attritional battles where local numerical advantage is neutralised by matched quality.

[EDITORIAL: Mass combat unit stat values (specific pool sizes, cohesion thresholds, morale mechanics) require design confirmation before compilation. The framework above is derived from simulation data and is mechanically sound. Specific numbers need playtesting at unit scale.]

---

## 8.10 Design Notes

This system was developed through extensive simulation testing (406 matchups, 2,000–5,000 fights per matchup) and validated against historical fighting manuals.

**What the system captures from the manuals:**
- Range control, initiative, tempo — the strategic layer of the manuals — correctly modelled.
- Commitment decisions, the decisive blow, stamina as a real constraint — correctly abstracted.
- Feint as tempo seizure (not damage tool), disarm as a legitimate technique — both grounded in Fiore and Silver.

**What is intentionally abstracted:**
- The bind (*Krieg* in Liechtenauer) — too granular for the game's scope.
- Grappling integration — represented narratively through Disarm and Close zone dynamics.
- Void vs parry as distinct defensive choices — Full Guard covers voiding; split pool covers parrying.

**Historical weapon balance:**
- Light Cut weapons dominate 1v1 in most contexts (75% vs Light Cut mirror, correctly). In most historical combat contexts (unarmoured or lightly armoured opponents), faster weapons with better hit rates were genuinely more effective.
- Heavy Blunt weapons are situationally powerful, not generally dominant. Against unarmoured opponents in single combat: weak. Against armoured opponents in group combat: decisive. This matches the historical record — war hammers and pollaxes were specialist tools, not standard issue.
- Heavy Cut weapons (longswords) are the strongest general-purpose choice — effective across all matchups, dominant in 1v1.

**Offence allocation and winning:** simulation shows near-zero correlation (r ≈ 0.01) between offence percentage and winning across 5,000 randomised characters. No single allocation strategy dominates — outcomes are determined by matchup, range management, and dice variance.
