<!-- DEPRECATED: 2026-04-09 — OUTDATED compilation stage. Canonical source: designs/combat/combat_design_v1.md. Do not use for mechanical references. -->

# PART EIGHT: COMBAT
## Version: v0.14-ST2 — PP-086–092 applied in-place; Part Eleven appendix eliminated

Combat in Valoria uses a simultaneous pool-split system derived from historical fighting manuals — Fiore dei Liberi, George Silver, the Liechtenauer tradition, Talhoffer, Meyer. Every round, each fighter divides their Combat Pool between Offence and Defence. All pools resolve simultaneously. The core tactical decision is commitment: overcommit to offence and you are exposed; overcommit to defence and your opponent acts freely.

> **Multi-attacker timing:** In multi-attacker scenarios (3+), defender allocates pool blind before any attacker declares their offence split.

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

> **Same range definition:** 'Same range' occurs when shorter weapon closes to its optimal zone. Shorter weapon has priority; longer weapon user must re-establish distance at disadvantage.

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

> **Tie Up clarification (P2-B11-05):** Tie Up blocks escape for one round only. The affected character may attempt Escape the following round.

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

> **Base damage formula (PP-086):** Base damage for a mass combat engagement = net successes on the attack roll (successes over Ob). Disposition modifiers (Offensive +2 flat; Defensive +4 flat) add to this base. Minimum 0.

As Size drops from casualties, the pool shrinks — fewer soldiers means fewer
dice regardless of individual quality.

**Design axiom: Generalship dominates.** Coherence Rating asymmetry is intentional. The
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

**Cohesion** (1–7): formation integrity. Starting value = min(general's Coherence Rating,
faction Military). Deterministic check: if total Size lost this turn exceeds
Cohesion rating, Cohesion degrades by 1. All checks fire at Phase 5 regardless
of damage source.

| Cohesion | CP penalty |
|---|---|
| 5–7 | None |
| 3–4 | −1D |
| 1–2 | −2D |
| 0 | Formation broken; cannot attack |

> **Break stacking (PP-087):** Formation Break Ob stacking: each break adds +1 Ob to all subsequent Cohesion checks (cumulative, persists through rally). Cap: 3 breaks = Dispersed (permanent rout). All attachments lost on any Formation Break.

Cohesion ceiling applies at deployment only, not retroactively. Military floor = 1.

**Morale** (1–7): rout threshold. Starting = general's Coherence Rating + unit quality
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

Scale is narrative only — no mechanical change except Thread Thread Sensitivity minimums.

---

### Command Rating (Coherence Rating)

**Coherence Rating = ⌈(Presence + Cognition) ÷ 2⌉.** Non-Player Character generals: Coherence Rating assigned directly (1–7).

Coherence Rating governs: sub-unit count cap (max = Coherence Rating), Size cap per unit (max Size = Coherence Rating),
Cohesion ceiling, Morale starting value and floor (= 1 while general present),
tactic execution (Coherence Rating dice vs Ob). Combat pool bonus: +1D per 2 Coherence Rating.

**General death — two-stage:**
- Stage 1 (incapacitated): −1 Morale all units, Coherence Rating halved, Morale floor suspended.
  Stabilise Phase 5 with Medicine Ob 2 within 1 turn or Stage 2 fires.
- Stage 2 (killed): −2 Morale (outside cap), Coherence Rating = 0, all units uncommanded.

Leader defeat: if leader's unit is defeated, leader rolls Agility vs Ob =
attacker net successes. Failure: captured. Failure by 3+: attacker may
choose to kill.

General in personal combat: Phase 5 action consumed each turn until resolved.
Mass battle continues at reduced command efficiency. Coherence Rating suspended.

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
Units beyond Coherence Rating limit fight at Line, Cohesion floor = 1, no tactics.

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

> **Artillery Bombard (PP-091):** Bombard (Artillery only): Roll Artillery CP vs Ob by distance (Short=1, Med=2, Long=3). No melee exchange. Success = flat 1 Size damage. Overwhelming = flat 2. Cannot Bombard at melee range. Artillery locked to Balanced disposition by default. [EDITORIAL ED-040: intentional?]

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
| Feigned Retreat | Disengage; pursuer Cohesion check; re-engage next turn with flank | 3 | Coherence Rating Ob 2 to recognise |
| Ambush | First engagement: defender no Defence allocation | 4 | Scouting (Game Master) |
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

| Battle scale | Thread scale | Min Thread Sensitivity | Ob | Coherence cost |
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
configuration) is Personal scale. Effect: enemy Coherence Rating −1 for battle duration.
[EDITORIAL: confirm this is an intended tactical option]

Site-anchored collective Weave: Active site −1 Ob; Major site −2 Ob.
Brittleness exempt on Success if site-anchored. Solo Territorial Weave
always carries brittleness risk.

Co-movement at mass battle scale: Temporal result = general loses Phase 5
action for d3 turns. Epistemic = Coherence Rating −1 for d3 turns. Actual = 1 Wound.

Coherence=0: practitioner exits rendered existence. Cannot initiate actions
or Thread operations. Recovery: 1 season non-practice + Close Knot
Anchoring Scene (Bonds Ob 2) → Coherence restored to 1.

---

### Southernmost

Non-Thread-sensitive units (Thread Sensitivity < 30) cannot operate in Southernmost.
They dissolve without awareness on entry. Remove from battle map: no
casualties, no Morale trigger, no Cohesion check. All individuals in a
force operating in Southernmost must personally have Thread Sensitivity ≥ 30.
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

> **Siege linkage (PP-088):** Siege assault linkage: mass combat win during declared Assault = Fortification −1. Overwhelming = −2. Field victory (not declared Assault) does not breach — Assault must be declared next season.


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