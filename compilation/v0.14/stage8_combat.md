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
- Wounds: −1D per Wound to the Combat Pool (cumulative)
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

Each Wound reduces the Combat Pool by −1D (cumulative). A fighter with 2 Wounds fights with −2D. Incapacitation occurs at the wound threshold — the pool reduction means fighters near incapacitation are materially degraded, not just on the edge of collapse.

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

Mass combat uses the same dice engine as personal combat, with two key changes:
**Size** (headcount health pool) and **Combat Power** (fighting effectiveness per
soldier) are separate stats. Both are 1–7.

**Effective Combat Pool = min(CP, current Size)**

As Size drops from casualties, the pool shrinks — fewer soldiers means fewer
dice regardless of individual quality.

**Design axiom: Generalship dominates.** CR asymmetry is intentional. The
general is the battle.

---

### Unit Stat Block

**Size** (1–7): headcount at declared scale. Health pool. At 0: destroyed.

**Combat Power (CP)** (1–7): fighting effectiveness per soldier. Equipment +
training. Sets the combat pool ceiling.

| CP | Tier |
|---|---|
| 1 | Levy |
| 2 | Militia |
| 3 | Professional |
| 4 | Veteran |
| 5 | Elite |
| 6–7 | Exceptional/Peerless |

**Military stat governs unit quality:** A faction's Military stat sets the
maximum CP and Cohesion ceiling for units it fields (1:1 direct mapping).

**Speed:** Slow / Standard / Fast.

**Cohesion** (1–7): formation integrity. Starting value = min(general's CR,
faction Military). Deterministic check: if total Size lost this turn exceeds
Cohesion rating, Cohesion degrades by 1. All checks fire at Phase 5 regardless
of damage source.

| Cohesion | CP penalty |
|---|---|
| 5–7 | None |
| 3–4 | −1D |
| 1–2 | −2D |
| 0 | Formation broken; cannot attack |

Cohesion ceiling applies at deployment only, not retroactively. Military floor = 1.

**Morale** (1–7): rout threshold. Starting = general's CR + unit quality
modifier (cap 7). Degradation triggers (all fire at Phase 5, cap −3/phase):
Size below 50%: −1. Size below 25%: −1 additional. Cohesion broken: −1.
Allied unit routed in zone: −1. General incapacitated Stage 1: −1. General
killed Stage 2: −2 (outside cap). Flanked and lost: −1. Idle army (no
engagement 2+ turns): −1. Morale floor = 1 while general present. At
Morale 0: unit routs. Rout contagion braked at 1 per turn.

**Weapon Type and DR:** Inherits personal combat tables unchanged. Projectile
DR = LightCut values.

| Armour | LightCut | HeavyCut | LightBlunt | HeavyBlunt | Projectile |
|---|---|---|---|---|---|
| None | 0 | 0 | 0 | 0 | 0 |
| Light | 2 | 1 | 1 | 0 | 2 |
| Medium | 4 | 3 | 2 | 1 | 4 |
| Heavy | 6 | 5 | 3 | 1 | 6 |

---

### Weapon Effectiveness Reference

| Attacker | vs None | vs Light | vs Medium | vs Heavy |
|---|---|---|---|---|
| LightCut | ✓ | ✗ | ✗ | ✗ |
| HeavyCut | ✓✓ | ✓✓ | ✓ | ✗ |
| HeavyBlunt | ✓✓ | ✓✓ | ✓✓ | ✓✓ |
| Projectile | ✓ | ✗ | ✗ | ✗ |

HeavyBlunt is the only weapon effective against Heavy armour. Projectile
units are anti-unarmoured only. Force composition determines outcome.

---

### Battle Scale

| Scale | 1 Size = | Thread scale |
|---|---|---|
| Skirmish | ~10 soldiers | Personal |
| Company | ~100 soldiers | Object |
| Battle | ~500 soldiers | Territorial |
| Campaign | ~1,000 soldiers | Territorial |
| War | ~5,000 soldiers | Structural |

Scale is narrative only — no mechanical change except Thread TS minimums.

---

### Command Rating (CR)

**CR = ⌈(Presence + Cognition) ÷ 2⌉.** NPC generals: CR assigned directly (1–7).

CR governs: sub-unit count cap (max = CR), Size cap per unit (max Size = CR),
Cohesion ceiling, Morale starting value and floor (= 1 while general present),
tactic execution (CR dice vs Ob). Combat pool bonus: +1D per 2 CR.

**General death — two-stage:**
- Stage 1 (incapacitated): −1 Morale all units, CR halved, Morale floor suspended.
  Stabilise Phase 5 with Medicine Ob 2 within 1 turn or Stage 2 fires.
- Stage 2 (killed): −2 Morale (outside cap), CR = 0, all units uncommanded.

Leader defeat: if leader's unit is defeated, leader rolls Agility vs Ob =
attacker net successes. Failure: captured. Failure by 3+: attacker may
choose to kill.

General in personal combat: Phase 5 action consumed each turn until resolved.
Mass battle continues at reduced command efficiency. CR suspended.

---

### Formation Types

| Formation | Off dice | Def dice | Special |
|---|---|---|---|
| Line | Normal | Normal | Standard |
| Shield Wall | −1D | +2D | Cannot advance. Negates flanking from one declared side/turn. Second flank applies normally. |
| Wedge | +2D | −1D | Negated if opponent uses Shield Wall |
| Skirmish | Normal | Normal | Cannot be flanked. −1D vs Heavy infantry |
| Column | Cannot engage | Cannot engage | +1 Speed tier, movement only |
| Reserve | Cannot engage | Cannot engage | Commits at Phase 3 start of NEXT turn |

Wedge beats Line. Shield Wall negates Wedge. No formation universally dominant.
Units beyond CR limit fight at Line, Cohesion floor = 1, no tactics.

---

### Battle Turn Structure

**Phase 1 — Strategy Declaration** (simultaneous, secret)
Assignments (max 3 engagements TTRPG), formation per unit, tactical action,
Thread intent (public). Thread Diagnosis occurs here (public declaration =
rendering the target configuration).

**Phase 2 — Volley and Combat Thread**
Projectile units fire. **Combat Thread operations** (Dissolution, offensive
Pulling) also fire here — declared Phase 1, fire before Engagement.
Volley: CP vs TN 6, net successes − DR = Size loss. Size loss recorded;
Cohesion check deferred to Phase 5.

**Phase 3 — Manoeuvre** (Fast → Standard → Slow)
Environmental modifiers apply. Reserve commitment declared (fires next turn).

**Phase 4 — Engagement** (max 3 simultaneous, TTRPG)
Per engagement: (1) Effective Pool = min(CP, Size) − Cohesion penalty +
Formation modifier. (2) Split Offence/Defence (both sides simultaneous).
(3) Damage = max(0, net hits + weapon modifier − DR). Critical (net ≥ 3):
weapon modifier doubled. Both sides take Size damage simultaneously.
Mutual destruction valid. Mass Mismatch Penalty: Light vs Heavy weapon
attack: −1 defensive success (min 0). Exempt: Shield Wall.

**Phase 5 — Cascade** (strict order)
1. Apply all Size damage (Volley + Combat Thread + Engagement).
2. Cohesion checks (deterministic, all sources combined).
3. Morale checks (triggers + cap −3/phase, Stage 2 general death outside cap).
4. **Support Thread operations** (Weave, Mend, Lock) resolve here.
5. General action: Rally / Reinforce Cohesion / Support Threadweave /
   Personal combat exchange / Stabilise incapacitated general.

**Phase 6 — Reform**
Non-engaged units: restore Cohesion, recover 1 Morale, merge sub-units.
Idle army: if no engagements Phase 4 this turn AND previous turn, both
sides lose 1 Morale.

---

### Tactics

| Tactic | Effect | Ob | Counter |
|---|---|---|---|
| Envelopment | Attempt all-flank; requires Fast | 2 | Refused Flank |
| Feigned Retreat | Disengage; pursuer Cohesion check; re-engage next turn with flank | 3 | CR Ob 2 to recognise |
| Ambush | First engagement: defender no Defence allocation | 4 | Scouting (GM) |
| Concentration | All sub-units on one target; max Fibonacci | 1 | Flanks exposed |
| Refused Flank | Wing anchors on terrain; immune that flank | 1 | Sacrifices offence |
| Hammer & Anvil | Shield Wall holds; Fast unit envelops | 3 | Break Anvil first |

---

### Environmental Modifiers

| Terrain | Effect |
|---|---|
| River crossing | −1 Speed tier; −1D Off; Cohesion check (Str lost = 1) |
| Uphill | Defender +1D Def; attacker −1D Off |
| Forest/broken | Cavalry → Standard; flanking impossible |
| Walls/fortifications | Defender +3 DR all types; no flanking; Slow cannot advance |
| Narrow pass | 1 engagement per side; Fibonacci impossible |

---

### Thread in Mass Combat

| Battle scale | Thread scale | Min TS | Ob | Coherence cost |
|---|---|---|---|---|
| Skirmish | Personal | 30 | 2 | 0 |
| Company | Object | 30 | 1 | 0 |
| Battle | Territorial | 50 | 4 | −1/op |
| Campaign | Territorial | 50 | 4 | −1/op |
| War | Structural | 70 | 5 | −2/op |

Coherence loss is automatic per §5.2.2, capped at −1/op (§5.2.3).
Weaving a unit's Cohesion is Territorial scale (collective formation).
Weaving a general's personal attributes is Personal scale (the person's
configuration, not the unit's). Weaving the general = Personal (Ob=2, 0
Coherence); Weaving the unit = Territorial (Ob=4, −1 Coherence).

**Pulling an enemy general's command capacity** (Presence/Cognition
configuration) is Personal scale. Effect: enemy CR −1 for battle duration.
[EDITORIAL: confirm this is an intended tactical option]

Site-anchored collective Weave: Active site −1 Ob; Major site −2 Ob.
Brittleness exempt on Success if site-anchored. Solo Territorial Weave
always carries brittleness risk.

Co-movement at mass battle scale: Temporal result = general loses Phase 5
action for d3 turns. Epistemic = CR −1 for d3 turns. Actual = 1 Wound.

Coherence=0: practitioner exits rendered existence. Cannot initiate actions
or Thread operations. Recovery: 1 season non-practice + Close Knot
Anchoring Scene (Bonds Ob 2) → Coherence restored to 1.

---

### Southernmost

Non-Thread-sensitive units (TS < 30) cannot operate in Southernmost.
They dissolve without awareness on entry. Remove from battle map: no
casualties, no Morale trigger, no Cohesion check. All individuals in a
force operating in Southernmost must personally have TS ≥ 30.
This is why Southernmost was never conquered.

---

### Reinforcement

Natural: +1 Size per campaign season. Accelerated: 1 Faction Resource per
additional Size point. Maximum: original Size at army creation. Destroyed
units (Size 0) cannot be restored. Thread effects on units persist across
battle boundaries unless cleared.

Battle outcome → faction consequences:
- Battle lost (defending force routed): Military −1, Stability check Ob 1.
- Campaign-scale defeat: Military −1, Stability check Ob 2, Mandate −1.
Military floor = 1. Cohesion ceiling applies at deployment only.

Muster: produces 1 unit of chosen type. Size=2 at deployment (next season).
CP determined by unit type choice, subject to Military ceiling.


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


---

# PART ELEVEN: STRESS TEST PATCHES — BATCH 11 + SIM-X SERIES
## Sources: tests/sim_combat_batch_11.md, tests/sim_x_01_combat_thread.md, tests/sim_x_06_combat_wounds_npcs.md
## Applied: 2026-04-02
## PP-086 through PP-091 (P1), P2-B11 series

---

## PP-086 — Mass Combat Base Damage Definition
**Fixes P1-B11-01: §8.9 disposition table adds to undefined base**

Add to §8.9 Mass Combat, Battle Turn Structure, Phase 4 damage resolution:

> "**Base damage** for a mass combat engagement = net successes on the attack roll (successes over Ob). This is the baseline before disposition modifiers. Disposition modifiers (offensive: +2 flat; defensive: +4 flat per prior compiled text) are added to this base. Minimum base damage = 0 (cannot deal negative damage). Formula: Damage = max(0, net_successes + disposition_modifier)."

---

## PP-087 — Formation Break Ob Stacking
**Fixes P1-B11-02: §8.9 Formation Break — two valid interpretations produce radically different attrition**

Add to §8.9 Formation Types, Formation Break section:

> "**Ob stacking on repeat breaks:** Each time a unit suffers a Formation Break, it accumulates +1 Ob to all subsequent Cohesion checks (cumulative, persists until battle end — rally actions do not clear the accumulated Ob penalty). A unit that has broken twice faces +2 Ob on all Cohesion checks. **Cap:** At 3 Formation Breaks, the unit is Dispersed — it routes permanently regardless of Morale. All attachments are lost on any Formation Break. The 3-break cap prevents indefinite rally-loop exploitation."

---

## PP-088 — Siege Assault vs Mass Combat Linkage
**Fixes P1-B11-03 and P2-B11-15: §8.4 assault outcome vs §8.9 mass combat outcome conflated**

Add to §8.9, end of Battle Outcome section, and cross-reference in §8.4 (Domain Actions):

> "**Siege assault linkage:** When a season's Domain Action is an Assault (siege offensive action), the Assault's outcome is determined by the mass combat resolution if a battle is fought:
> - Attacker wins mass combat: Fortification −1 (breach made).
> - Attacker loses mass combat: no Fortification change. Attacker may attempt again next season.
> - Attacker wins with Overwhelming (net ≥ 2×Ob): Fortification −2.
> Mass combat won in a field engagement (not an Assault declaration) does not change Fortification — only declared Assaults can breach fortifications. A field victory allows the attacker to declare an Assault next season."

---

## PP-091 — Artillery Bombard Resolution
**Fixes P1-B11-06: §8.9 Artillery Bombard manoeuvre has no resolution mechanic**

Add to §8.9 Tactics (Artillery section) or Weapon Effectiveness Reference:

> "**Bombard (Artillery tactic):** Artillery units may declare Bombard instead of a standard melee engagement. Bombard is a ranged action — the Artillery unit does not enter melee and is not subject to melee retaliation that round.
> Resolution: Roll Artillery CP vs distance-based Ob (Short = Ob 1, Medium = Ob 2, Long = Ob 3). Success = flat 1 Strength damage to target. Overwhelming = flat 2 Strength damage. Failure = no effect. Bombard may not be used at melee range (enemy unit in same zone).
> Artillery units in Bombard have Balanced disposition by default (no melee exchange). If an enemy unit closes to melee range without being intercepted, Artillery loses the Bombard action for that turn and must defend."

---

## P2-B11 SERIES — Personal Combat Clarifications

### P2-B11-01 — Defence Split Timing (8+ Attackers)
Add to §8.1 Combat Pool, Pool Split section:
> "In multi-attacker scenarios (3+ opponents), the defender allocates their pool before any attacker declares their offence split. The defender's allocation is blind — they cannot see how attackers split. Attackers declare simultaneously after the defender's split is set."

### P2-B11-02 — 'Same Range' Definition for Reach Priority
Add to §8.5 Range and Reach:
> "'Same range' occurs when a combatant using a shorter weapon has successfully closed to their optimal range (Close zone for Short weapons). At this point the shorter weapon has priority; the longer weapon user loses range priority and must manoeuvre at disadvantage to re-establish Far zone. Closing to melee range (touching distance from narrative standpoint) counts as Short range regardless of zone descriptor."

### P2-B11-03 — Stunt and Chain Die Interaction on Crit Success
Add to §8.4 Actions, Stunt:
> "Chain dice triggered by 10s on a Stunt roll still chain (produce additional dice on 10s) as normal. A Stunt's critical success range (the stunt range value) determines narrative outcome severity, not dice chain behaviour. Both effects are independent and apply simultaneously."

### P2-B11-05 — Escape During Tie Up
Add to §8.4 Actions, Tie Up:
> "A character subjected to Tie Up cannot declare Escape that round. They may attempt Escape the following round as their declared action. Tie Up prevents escape for one round only — the defender is not permanently restrained."

### P2-B11-06 — Rescue Against Non-Attack Action
Add to §8.8 Group Combat, Rescue:
> "Rescue is valid only when an incoming attack is declared against the target. If no attack is declared against the rescue target this round, the Rescue action fails and the action is lost. The rescuer may not redirect their Rescue to a different target mid-declaration."

### P2-B11-07 — Incapacitation Timing
Add to §8.7 Wounds:
> "A character reduced to 0 Health during action resolution completes their currently-resolving action (if declared and in the same priority step). They fall incapacitated at the end of that priority step. Actions declared for later priority steps do not resolve."

### P2-B11-08 — Three-Way Combat Simultaneous Rout
Add to §8.8 Multi-Engagement:
> "If two parties in a three-way engagement rout simultaneously (both reach 0 Health or Morale 0 in the same resolution step), the surviving party wins the engagement and receives the standard veteran bonus. No tiebreaker required — the last party standing wins."

### P2-B11-09 / P2-B11-10 — Commander in Personal Combat During Mass Battle
Add to §8.9 Command Rating:
> "A commander in personal combat (Priority 8 duel or contested personal action) may not simultaneously take a mass combat Rally, Tactics, or Memory conditional order action in that same round. Their unit dice contribution remains active (orders already issued before personal engagement), but the commander cannot issue new orders while personally combating."

### P2-B11-11 — Routed Unit Drift During Scene Resolution
Add to §8.9 Rout and Pursuit:
> "Routed units hold position during any inter-round scene resolution (contested figures, Thread operations, personal combats between rounds). Routed units resume drift at the start of the next round's Declaration Phase."

### P2-B11-12 — Named NPC Incapacitation and Unit Morale
Add to §8.9 Unit Stat Block, Morale section:
> "When a named NPC who is the commanding officer of a unit is incapacitated (personal combat, Thread consequence, or other means), that unit loses its Commander Contribution for the remainder of the battle. The unit continues with the general's CR but at 0 commander bonus dice."

### P2-B11-13 — Artillery Balanced Disposition
Add to §8.9 Formation Types:
> "[EDITORIAL: requires user approval — ST-B11-13 Artillery disposition lock] Artillery is currently locked to Balanced disposition in all contexts. Confirm whether this is intentional (Artillery is never purely offensive or purely defensive — it provides fire support from a fixed position) or whether Artillery should be permitted to declare Offensive disposition at point-blank range when defending against a closing enemy."

### P2-B11-17 — Cross-Mode Seasonal Cap Tracking
Add to §8.9 Reinforcement (or cross-reference to stage11):
> "The ±2 seasonal cap for faction Military stat applies across all mode interactions within a single season. GM tracks the cap explicitly on a faction summary sheet updated after both Strategic Phase and Personal Phase each season. If a result would breach the cap, the excess is discarded."

### P2-B11-19 — TT 80+ Effect in Mass Battle
Add to §8.9 Thread in Mass Combat:
> "[EDITORIAL: requires user approval — P2-B11-19 TT 80+ mass battle effect] The current text does not define what happens in mass battle when the world TT/RS reaches the 80+ threshold. Define: (a) does high TT produce adverse Thread effects on non-practitioner units (suggested: Coherence checks for any practitioner attached to a unit, Morale −1 for all non-Thread-sensitive units in Southernmost-adjacent territories), or (b) TT threshold has no mass battle mechanical effect beyond what is already defined in the RS track?"

---

## SIM-X-06 FINDINGS — Personal Combat Validation Notes

These findings confirm the system is working as designed (no patches needed):

- **F-23 (Wounds, −1D system):** Wound degradation is smooth with no single-wound cliff effect. Confirmed working.
- **F-24 (Range control decisive):** Range mismatch is more fight-determining than pool size or wounds. Intended design — range management is the primary tactical layer.
- **F-25 (CE accumulation pacing):** Inquisitor CE track accumulates correctly at ~1-2 events per multi-session trajectory. No patch needed.
