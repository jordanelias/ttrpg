<!-- SKELETON — mechanical spec only — atomized 2026-04-13 -->
<!-- Infill: mass_battle_v30_infill.md -->

<!-- v30 baseline — renamed from designs/mass_combat/mass_battle_v3.md on 2026-04-13 -->
# VALORIA — MASS BATTLE SYSTEM v4
## Version: v4.8 — PP-240,241,245,249,250,256 applied;
##  PP-232 (renames: Strength→Size, CP→Power, Cohesion→Discipline, CR→Command) + PP-233 (core formula) propagated.
## Status: WORKING DESIGN — no appendix sections. Read straight through.
## Three-mode: TTRPG/Hybrid (Part A); Board Game (Part B); Hybrid Handoff (§B.5)
## All P1/P2/P3 patches applied. Gaps filled. Editorial notes flagged.
## Status: CANONICAL — approved 2026-04-17 (editorial batch acceptance)

---

## PART A: TTRPG MASS BATTLE

### A.1 OVERVIEW

Mass battle uses the same dice engine as personal combat. Pool split into
Offence/Defence, simultaneous resolution, TN-based successes, DR applied to
damage. Two stats unified in personal combat split here:

- **Size** — headcount. Health pool. Casualties reduce it directly.
- **Power** — fighting effectiveness per soldier. Equipment and
  training. Determines dice rolled.

**Effective Combat Pool = min(Size, Command) + Command** (PP-233)

As Size drops, the pool shrinks — fewer soldiers means fewer dice
regardless of individual quality. Command caps both Size and Power contributions. (PP-233) Size determines
whether you reach it.

**Design axiom: Generalship dominates.** Command asymmetry is intentional. A Command=7
general versus a Command=1 general produces a near-certain outcome before a die is
rolled. The general is the battle.

---

### A.2 WEAPON EFFECTIVENESS REFERENCE

| Attacker | vs None | vs Light | vs Medium | vs Heavy |
|---|---|---|---|---|
| LightCut | ✓ | ✗ | ✗ | ✗ |
| HeavyCut | ✓✓ | ✓✓ | ✓ | ✗ |
| LightBlunt | ✓ | ✗ | ✗ | ✗ |
| HeavyBlunt | ✓✓ | ✓✓ | ✓✓ | ✓✓ |
| Piercing — Bow (arrows) | ✓ | ✗ | ✗ | ✗ |
| Piercing — Crossbow (bolts) | ✓✓ | ✓✓ | ✓✓* | ✓* |
| Blunt — Throwing | ✓ | ✗ | ✗ | ✗ |
| Blunt — Sling (clay) | ✓ | ✗ | ✗ | ✗ |
| Blunt — Sling (rock) | ✓ | ✓ | ✗ | ✗ |
| Blunt — Sling (metal) | ✓✓ | ✓✓ | ✓ | ✗ |
| Blunt — Sling (lead) | ✓✓ | ✓✓ | ✓✓ | ✗ |
| HBl — Heavy Blunt Siege | ✓✓ | ✓✓ | ✓✓ | ✓✓ |

*Crossbow vs Medium/Heavy: post-DR flat bonus applies if hit (+1 Med+Heavy). Scaled ÷2 from personal +2 (PP-189).

HeavyBlunt and HBl (siege) are the only weapon classes fully effective against Heavy armour. Piercing/Bow penetrates Light; Piercing/Crossbow reaches Medium and Heavy via post-DR bonus. Clay sling: anti-levy. Rock sling: anti-light. Metal sling: anti-medium. Lead sling: anti-heavy. (PP-189 4-ammo split.) Force composition determines outcome more than tactics. [EDITORIAL: ED-061 — confirm 4-category split and
sub-unit types for Ranged (archer/crossbow/slinger)]

**Personal combat projectile weapons:** Piercing (Bow/Crossbow) and Blunt (Throwing/Sling) are defined for individual fighters in personal combat (PP-188, PP-189). See references/params_combat.md §Ranged Combat Rules. **HBl distinction:** HBl at personal scale = lead shot sling (individual weapon, PP-172 DR 0/0/1/2). HBl at mass/siege scale = Artillery unit (PP-091/PP-106, sight-line rule, Bombard action). Siege crew fight as melee/unarmed, but individual slingers may carry lead shot. The ranged DR values above apply at both unit scale (Volley Phase) and personal scale (individual ranged attacks).

---

### A.3 BATTLE SCALE

| Scale | 1 Size = | Thread scale (see A.10) |
|---|---|---|
| Skirmish | ~10 soldiers | Personal |
| Company | ~100 soldiers | Object |
| Battle | ~500 soldiers | Territorial |
| Campaign | ~1,000 soldiers | Territorial |
| War | ~5,000 soldiers | Structural |

Scale sets **block_size** for TroopCount derivation (ED-694):

| Scale | block_size |
|-------|-----------|
| Skirmish | 10 |
| Company | 100 |
| Battle | 500 |
| Campaign | 1,000 |
| War | 5,000 |

**TroopCount = Size × block_size** (set at muster). Size becomes a computed integer: `Size = floor(TroopCount / block_size)`. All combat formulas reference Size unchanged. Output scaling: `effective_damage = floor(successes × (1 + Power) × TroopCount / max_TroopCount)`, capped at ratio 1.0. Player sees: "Heavy Infantry — 4,428 / 5,000 (Size 4)".

Thread Sensitivity minimums per scale still apply.

---

### A.4 UNIT STAT BLOCK (all 1–7)

**Size** — computed from TroopCount: `Size = floor(TroopCount / block_size)`. At Size 0 (TroopCount < block_size): destroyed. TroopCount is the granular health pool; Size is the integer used by combat formulas. (ED-694)

**Power** — dice pool ceiling.

| Power | Tier |
|---|---|
| 1 | Levy |
| 2 | Militia |
| 3 | Professional |
| 4 | Veteran |
| 5 | Elite |
| 6–7 | Exceptional/Peerless |

**Military stat → unit quality** [EDITORIAL: confirm mapping] *[FACTION-P2-01 fix]*
A faction's Military stat sets the Power ceiling and starting Discipline ceiling
for units it fields. A Military=3 faction cannot field Power=5 units.

| Military | Max unit Power | Starting Discipline ceiling |
|---|---|---|
| 1 | 1 | 2 |
| 2 | 2 | 3 |
| 3 | 3 | 4 |
| 4 | 4 | 5 |
| 5 | 5 | 6 |
| 6 | 6 | 7 |
| 7 | 7 | 7 |

**Speed** — Slow / Standard / Fast (3 tiers).

**Discipline** (1–7) — organisational integrity. Starting value = min(general's
Command, Military ceiling above).

**Discipline check — DETERMINISTIC (PP-502, propagating PP-251):** *[P1-04]*
Discipline degrades by 1 when BOTH conditions are met (checked at Phase 6 Step 2):
(1) Total Size lost this turn > current Discipline rating
(2) This unit's Size loss exceeds the opposing unit's Size loss by ≥ 1
Symmetric losses do NOT trigger degradation. All checks fire at Phase 6 Step 2. *[P2-06, PP-251, PP-502]* *(PROVISIONAL marker stripped per editorial approval 2026-04-30.)*

| Discipline | Effective Power penalty |
|---|---|
| 5–7 | None |
| 3–4 | −1D |
| 1–2 | −2D |
| 0 | Formation broken; cannot attack; must reform or rout |

Discipline restoration: Reform Phase only (unit not engaged), +1 Discipline.
Requires general's Command ≥ current Discipline + 1 **AND Command ≥ 2 (PP-241)**. The explicit Command=1 prohibition takes precedence over the formula.
Command=1 general cannot restore Discipline to any unit — all degradation is
permanent for that battle. *[NEW-P2-05 — confirmed as intended Command asymmetry]*

**Morale** (1–7) — rout threshold. Starting = general's Command + unit quality
modifier (cap 7).

Morale degradation triggers:
- Size dropped below 50% of max: −1
- Size dropped below 25%: −1 additional
- Discipline broken this turn: −1
- Allied unit routed in same zone: −1
- General incapacitated (Stage 1): −1
- General killed (Stage 2): −2
- Flanked and lost exchange: −1
- No engagement for 2+ consecutive turns (idle army): −1 *[P2-02/P2-04]*

**Morale cap: −3 per Cascade Phase.** General killed (Stage 2) deals −2
separately, not subject to the cap. *[P1-03]*

> **Clarification:** "Application order: Apply all non-general Morale changes first, capping the total at −3 from these sources. Then apply Stage 2 general death −2 additionally (this −2 is separate and not subject to the cap). Maximum total Morale loss in one Cascade Phase: −5 (−3 capped + −2 general kill)."

> **Encirclement exception (PP-683, MB-08):** A unit with no valid retreat path — flanked from 3 simultaneous directions, OR all retreat zones occupied by enemy units — has the −3 Morale cap removed for that Cascade Phase only. Cap restored next turn if retreat path opens. Models historical catastrophic collapse (Cannae, Lake Trasimene) where encircled armies routed beyond what normal cohesion could absorb. Stage 2 general kill remains additive on top.

> **Artillery cascade ruling (PP-198):** Multiple simultaneous HBl unit destructions in one Cascade Phase each trigger Morale −1 (allied unit routed). Total non-general Morale loss still capped at −3. No runaway cascade possible from Artillery alone.

While general is present: Morale floor = 1. At Morale 0: unit routs.

**Rout contagion brake:** Rout causes −1 Morale to adjacent units, but this
secondary loss cannot itself cause further routs until the next turn. *[P1-02]*

**Weapon Type** — (hit TN, def TN, damage modifier). Inherits personal combat
table unchanged.

**Armour Tier / DR table** — inherits personal combat tables. Melee and ranged DR are distinct. *[PP-173]*

**H is computed once at battle start** from the unit's opening Discipline and Command values, then frozen for the battle's duration. Discipline degradation at Phase 6 Step 2 modifies the Effective Power penalty table only — it does not recalculate H or Total Health. *(Resolves MATH-FAIL-02)*

**Melee DR:**
| Armour | LightCut | HeavyCut | LightBlunt | HeavyBlunt |
|---|---|---|---|---|
| None | 0 | 0 | 0 | 0 |
| Light | 2 | 1 | 1 | 0 |
| Medium | 4 | 3 | 2 | 1 |
| Heavy | 6 | 5 | 3 | 1 |

**Ranged DR (Volley Phase) — MASS COMBAT SCALE [PP-188]:**
Scaled (÷2 rounded up) from personal combat DR. Crossbow post-DR bonus applied after table.

| Armour | vs Piercing | vs Blunt |
|---|---|---|
| None | 0 | 0 |
| Light | 1 | 1 |
| Medium | 2 | 1 |
| Heavy | 3 | 2 |

Crossbow post-DR bonus (if net hits > 0): +1 vs Medium and Heavy. Scaled ÷2 from personal +2 (PP-189).
Sling: effective Power −2D; ammo modifier per unit table above.


**Ranged unit roles:** Archer units effective vs None/Light armour. Crossbow units: modest base, post-DR bonus makes them the anti-armour ranged choice. Sling clay: anti-levy. Sling rock: anti-light. Sling metal: anti-medium. Sling lead: anti-heavy. All sling: −2D pool penalty. HBl (Artillery/siege) follow PP-091/PP-106 — distinct unit type.

---

### A.5 COMMAND RATING

**Command = ⌈(Charisma + Cognition) ÷ 2⌉** *[confirmed]*

Command governs:
1. Sub-unit limit (max simultaneous commanded = Command; TTRPG hard cap: 3)
2. Discipline ceiling
3. Morale starting value and floor (= 1 while general present)
4. Tactic execution (Command dice vs Ob per tactic)

**Non-Player Character generals:** Command assigned directly (1–7) as a narrative stat without
Cha+Cog derivation. *[Command-P2-02]*

**Command applies in full to each sub-unit (PP-504):** The general's full Command value applies to each commanded sub-unit's pool independently. Command is not divided across sub-units. Sub-unit limit (max = Command, TTRPG cap: 3) governs count, not distribution. Note: §A.8 splitting guidance is under revision — see ED-358. *(PROVISIONAL marker stripped per editorial approval 2026-04-30.)*

**General two-stage death:** *[P1-02]*
- Stage 1 (incapacitated): −1 Morale all units, Command halved (floor, minimum 1), Morale floor suspended. Stabilise in Phase 5 with Medicine Ob 2 (1-turn window). *(Command halving: floor(Command÷2), min 1. A Stage 1 general retains at least 1 Command, preserving the Stage 1 / Stage 2 distinction.)*
- Stage 2 (killed): Stage 2 fires at start of following turn's Phase 5
  if not stabilised. −2 Morale (outside cap), Command = 0, all units uncommanded.
  *[NEW-P2-02 — Stage 1 → 2 timing confirmed]*

**General in personal combat:** suspends all Command effects. Re-establish command
with Command check Ob 2 in Phase 1 of any subsequent turn. *[P2-10]*

**Bilateral general personal combat (PP-506):** If both generals enter personal combat
simultaneously in Phase 5, mass battle does not freeze. Both armies fight uncommanded:
PP-273 floor (1D minimum per unit), Line formation, no tactics available. Mass battle
continues turn-by-turn until each general resolves their personal combat and re-establishes
Command (Ob 2 check Phase 1, following turn). Sequencing within the bilateral personal
combat: simultaneous initiative per standard personal combat rules. *(ED-355 resolved 2026-04-XX; PROVISIONAL marker stripped per ED-767.)*

**Wounds carry over:** Wounds from personal combat add +1 Ob to Command tactic
execution rolls. A 2-wound general has tactic success probability halved.
*[D3-P2-01 — confirmed intended]*

**Coherence does not affect Command (PP-249):** Coherence is a Thread perceptual track; Command is tactical effectiveness. Dissonance impairs Thread operations only. No Coherence penalty applies to Command tactic rolls.


**Mass battle pauses during personal combat (unilateral).** If one general enters personal combat, mass battle holds at current state. Resume at Phase 1 of next mass battle turn after personal combat resolves. **Exception (PP-506 bilateral):** if both generals enter personal combat simultaneously, mass battle does NOT freeze — both armies continue uncommanded (PP-273 floor, Line formation, no tactics) until each general re-establishes Command (Ob 2, Phase 1 of the following turn). *[D3-P2-02, PP-506]*

---

### A.6 FORMATION TYPES

| Formation | Off dice | Def dice | Special |
|---|---|---|---|
| Line | Normal | Normal | Standard |
| Shield Wall | −1D | +2D | Cannot advance. Negates flanking from one declared side per turn. Second flank from opposite side applies normally. *[P2-08]* |
| Wedge | +2D | −1D | Negated if opponent uses Shield Wall |
| Skirmish | Normal | Normal | Cannot be flanked. −1D vs Heavy infantry |
| Column | Cannot engage | Cannot engage | +1 Speed tier, movement only |
| Feigned Retreat | — | — | See Tactics |
| Reserve | Cannot engage | Cannot engage | Commits at Phase 3 start of NEXT turn *[P3-02]* |

> **Clarification:** "Roll a number of d10s equal to the opposing general's Command score, against Ob 2, to recognise the Feigned Retreat as a feint rather than a genuine withdrawal. Success: the pursuing side is not deceived; the Feigned Retreat has no effect this turn. Failure (or no roll if the opposing general is killed): pursuing side pursues normally and suffers the Discipline check."

> **Feigned Retreat Discipline check Ob (PP-256):** The pursuing-side Discipline check is **Ob 1**. Discipline-4 unit: ~87% success. Discipline-1 unit: ~40% success.

> **Feigned Retreat Discipline check Ob (PP-256):** The pursuing-side Discipline check is **Ob 1**. Pursuing a fleeing enemy is a natural impulse; Ob 1 reflects the difficulty of halting momentum. Discipline-4 unit: ~87% success. Discipline-1 unit: ~40% success.

> **Clarification (PP-MB-04, PP-499 text fix):** "Reserve commitment at Phase 3 of Turn N+1 makes the unit immediately available for Phase 5 Engagement in that same turn (Turn N+1). Commitment does not delay the unit to Turn N+2. Summary: declare Reserve in Phase 3 of Turn N → unit commits at Phase 3 of Turn N+1 → unit may engage in Phase 5 (Engagement) of Turn N+1."

> **Reserve first-engagement Off/Def split:** A unit committing from Reserve at Phase 3 of Turn N+1 had no Phase 1 declaration window for that turn. Default split applies to its first engagement: equal split (round down to Offence). The unit may declare normally in Phase 1 of Turn N+2 and all subsequent turns.

> **Clarification (PP-MB-07):** "Three-sided encirclement example: Front, Left flank, Right flank simultaneously. Shield Wall negates one declared flank (say, Left). Front attack is fully defended (+2D Def). Right flank attack applies normally (full flanking bonus to attacker). The defender faces two unmitigated engagements and one defended — this is the intended design ceiling for Shield Wall. Command = 3 maximum means a force cannot be attacked from more than three directions simultaneously."

**Formation counter logic:** Wedge beats Line. Shield Wall negates Wedge but
cannot advance. No formation is universally dominant. *[P2-01]*

**Shield Wall +2D Def — simultaneous engagements (PP-500):** The +2D Def bonus applies to all defensive pools in all simultaneous engagements, including unmitigated flanks. Blanket formation modifier. *(PROVISIONAL marker stripped per editorial approval 2026-04-30.)*

**Units beyond Command limit** fight at Line formation, Discipline = 1 floor,
no tactics available. *[P3-03]*

**Minimum unit combat pool (PP-273):** After all penalties (Discipline modifier, Command limit effects), the effective combat pool has a minimum of **1 die**. A unit at Discipline 1 with −2D penalty and pool 2 fights at 1 die, not 0. The only condition that removes all attacking capability is Discipline 0 (Formation Broken — unit cannot attack). When the general dies and Command = 0, all units are beyond the Command limit and fight at 1 die minimum until Formation Broken or routed.

---

### A.7 BATTLE TURN STRUCTURE
## Revised 2026-04-02 — ED-050 resolved (Option D): offensive Thread own phase between Manoeuvre and Engagement.
## Volley and offensive Thread damage deferred to Cascade Phase 6 step 1 (simultaneous with Engagement damage).

**Phase 1 — Strategy Declaration** (simultaneous, secret)
General declares: sub-unit assignments (max 3 for TTRPG), formation per
sub-unit, tactical action, and Thread intent (public).

**Offence/Defence pool split** declared here for each sub-unit. Any allocation
is valid (minimum 1D each side). If not declared: default = equal split
(round down to Offence). Split is secret; revealed simultaneously at Phase 5.
[PROV: PP-104 — resolves PARAMS-GAP-04]

Thread declaration: Practitioners publicly declare intent (offensive or
support) and target. Diagnosis occurs here (public declaration = rendering
the configuration). *[P1-01]*

**Phase 2 — Volley**
Projectile units fire. Roll [Power stat] dice vs TN 6. Power stat = unit quality tier (1–7). Distinct from engagement pool formula (PP-233) — ranged output is governed by unit quality, not generalship. Net successes − DR (Projectile column) = Size loss to record. (PP-503) *(PROVISIONAL marker stripped per editorial approval 2026-04-30.)*
Prepared Defence: declare in Phase 1; half Effective Power as passive DR
against Volley attacks this turn (rounded down, min 0).

**Design rationale (Volley Power-only formula, ED-753):** Volley uses Power dice (1-7) instead of Effective Combat Pool (PP-233) intentionally. Ranged units are supplementary force projection — concentrated effect, narrow window. Volley as a tactic generates initial damage; Engagement (Phase 5) is where decisive force resolves. A pure-ranged force underperforms equivalent-Military melee force at parity Military stat — this is correct: ranged dominance requires combined-arms (e.g., crossbow + Heavy Infantry), not pure-ranged composition. The asymmetry between Volley pool (Power only) and Engagement pool (Power + Command, capped by Size) is the mechanism that ranks generalship as the dominant battle factor while preserving tactical relevance for ranged unit composition.

**Artillery sight-line rule (PP-106):** HBl (Artillery) units require unobstructed
line of sight. A unit in Line formation positioned between the Artillery and its
target blocks the shot. Artillery must target units in an unobstructed zone.
Primary counter to Artillery: maintain a screening formation in front of your
vulnerable units, then flank to threaten Artillery directly.
bonus (+1 per 2 dice).
**Volley Size loss is recorded but NOT applied until Phase 6 Step 1.**
*[P2-06, ED-037 provisional: TN 6 intentional exception]*

**Phase 3 — Manoeuvre**
Fast → Standard → Slow. Environmental modifiers applied. Reserve commitment
declared here (takes effect next turn's Phase 3). *[P3-02]*

**Phase 4 — Offensive Thread Operations**
Practitioners with declared offensive intent execute their Leap and operation.
Offensive operations: Dissolution, Pulling, Locking targeting enemy units or
configurations.

Resolution:
1. Leap resolves (Coherence check if applicable — see threadwork_redesign_v25.md §2.3)
2. Operation rolls (pool vs Ob per operation type and scale)
3. Effects recorded but NOT applied until Phase 6 Step 1 (simultaneous
   with Volley and Engagement damage)

A unit whose Size is reduced to 0 by Phase 4 Thread effects is NOT removed before 
**Overwhelming Size Advantage (PP-530):** When a unit's Size is ≥ 2× the opposing *general's* Command score, the larger unit may add +1D to its Offence pool once per Battle Turn, applied at Phase 5 Engagement (not Phase 4). This bonus does not apply when the larger unit is in Defensive formation or executing defensive orders (Hold, Fortify). *(PP-530 corrected: moved from Phase 4 to Phase 5; "opposing unit's Command" clarified as opposing general's Command — units have no Command stat.)*

Phase 5.
Simultaneous-damage rule governs: damage is recorded in Phase 4 but applied at Phase 6 Step 1.
The unit's current Size during Phase 5 is its Phase 3-end Size (pre-Thread damage) and it
participates in Phase 5 Engagement normally. It is removed at Phase 6 Step 1 when all damage
applies simultaneously. (PP-505) *(ED-354 resolved; PROVISIONAL marker stripped per ED-767.)*
Configuration changes: practitioner may revise target at no cost if the declared configuration
has changed significantly (unit destroyed, routed, or repositioned). *[THREAD-P2-03]*

In most battles it is skipped entirely. Board game: no Phase 4 (faction Thread
orders abstracted to Co-Movement cards at strategic scale, not battle scale).

**Practitioner positioning — Rear vs Front Line (PP-101):**
Practitioners in rear position (Reserve formation or not assigned to an engaged
unit) resolve Phase 4 safely. Their Leap and operation fire before Phase 5
Engagement begins. They face no personal combat during Phase 4.

Practitioners embedded in a front-line unit (not in Reserve, in or adjacent to
an engaged unit) cannot safely act in Phase 4 — they are subject to Phase 5
Engagement as normal fighters. For these practitioners: Leap resolves at the
start of Phase 5, concurrent with Engagement, at the practitioner's initiative
priority. A declared attacker targeting them in Phase 5 makes them ineligible
for Leap per standard eligibility rules.

Summary:
- Rear/Reserve practitioner → Phase 4 Leap: safe, guaranteed window.
- Front-line practitioner → Phase 5 Leap: conditional on no declared attacker.

**Phase 5 — Engagement** (max 3 simultaneous, TTRPG) *[P1-01]*

Per engagement:
1. Effective Pool = min(Size, Command) + Command − Discipline penalty (PP-233; Size as of Phase 3 end)
2. Apply Formation modifier
3. Split into Offence / Defence (both sides simultaneously)
4. Roll. Net hits = Offence succs − Defence succs
5. Damage = max(0, net hits + weapon modifier − DR)
6. Critical hit (net hits ≥ 3): weapon modifier doubled
7. Engagement damage recorded. NOT applied until Phase 6 Step 1.
8. Mutual destruction (both to 0) is valid — Pyrrhic outcomes possible *[P2-02]*. **Mutual total destruction — all units both sides to 0 simultaneously (PP-240, PP-507):** draw; no territory change; both factions Stability check Ob 1 at Accounting. This Ob 1 check REPLACES the §A.13 battle-lost Stability check — a draw produces no loser, so no battle-lost consequence fires. Each faction takes exactly one Ob 1 Stability check at Accounting. [PROVISIONAL — ED-357 resolved]


Mass Mismatch Penalty: Light weapon defender vs Heavy weapon attack − 1
defensive success (min 0). Exempt: Shield Wall.

**Phase 6 — Cascade** (strict order)

1. Apply ALL recorded Size damage simultaneously:
   Volley (Phase 2) + Offensive Thread (Phase 4) + Engagement (Phase 5).
   Units reduced to 0 Size are destroyed. Pyrrhic mutual destruction valid.
2. Discipline checks (deterministic — per §A.4)
3. Morale checks (triggers + cap per §A.4; PP-082 general kill separate)
4. General action (one): Rally / Reinforce Discipline / **Support Threadweave**
   (Weaving, Mending — see below) / Personal combat / Stabilise incapacitated
   general
5. Support Thread Leap resolves (if declared in Phase 1 as support intent)

Support Thread operations (Phase 6 step 4–5): Weaving (Discipline bolster,
unit hardening), Mending (Size restoration), Rally (W-33). These fire
after casualties are known — practitioners respond to what the battle has done.

**Phase 7 — Reform**
Non-engaged units: restore Discipline, recover 1 Morale, merge sub-units.
Idle army clock: if no engagements in Phase 5 this turn AND previous turn, both sides lose 1 Morale in Phase 7. *[P2-02, P2-04]* **Terrain exception:** this does not fire for a side that was unable to initiate engagement due to terrain constraint (defender behind Walls with no available advance; either side in Narrow Pass with no approach path). Voluntary inaction only.

---

### A.8 TACTICS

| Tactic | Effect | Ob | Counter |
|---|---|---|---|
| Envelopment | Attempt all-flank; requires Fast | 2 | Refused Flank |
| Feigned Retreat | Disengage; pursuer Discipline check; re-engage next turn with flank | 3 | Command Ob 2 to recognise |
| Ambush | First engagement: defender no Defence allocation | 4 | Scouting (engine check) |
| Concentration | All sub-units on one target; max Fibonacci | 1 | Flanks exposed |
| Refused Flank | Wing anchors on terrain; immune to that flank | 1 | Sacrifices offence |
| Hammer & Anvil | Shield Wall holds; Fast unit envelops | 3 | Break Anvil first |

Splitting doctrine (PP-508 — replaces P2-14 note, ED-358): Splitting is structurally
across simultaneous engagements. Simulation results:
- Split dominates concentration by +9% to +45% win-rate depending on Command matchup.
- Only cases where split advantage is negligible (<5%): attacker heavily outcommands defender
  (Att Cmd=4-5 vs Def Cmd=2) and concentration already approaches win-rate ceiling.

Splitting is suboptimal ONLY when:
1. Terrain prevents simultaneous engagements (Narrow Pass: 1 engagement per side — hardest counter)
2. Sub-unit Size drops so far below Command that each sub-unit pool approaches floor (Size=1 edge)

The primary counter to enemy splitting is NOT matching their split — it is Narrow Pass terrain
or Feigned Retreat to disengage and re-concentrate. *(ED-358 resolved; PROVISIONAL marker stripped per ED-767.)*

---

### A.9 ENVIRONMENTAL MODIFIERS

| Terrain | Effect |
|---|---|
| River crossing | −1 Speed tier; −1D Off; Discipline check (treat Size lost = 1) |
| Uphill | Defender +1D Def; attacker −1D Off |
| Forest / broken | Cavalry → Standard; flanking impossible |
| Walls / fortifications | Defender +3 DR; no flanking; Slow cannot advance |
| Narrow pass | 1 engagement per side; Fibonacci impossible |
| Open flat | No modifiers |

---

### A.10 THREAD OPERATIONS IN MASS BATTLE

**Corrected scale mapping:** *[THREAD-P1-01 fix]*

| Battle scale | Thread scale | Min Thread Sensitivity | Thread Ob | Coherence auto-cost |
|---|---|---|---|---|
| Skirmish | Personal | 30 | 2 (total three-axis Ob) | 0 |
| Company | Object | 30 | 1 (total three-axis Ob) | 0 |
| Battle | Territorial | 50 | 4 (total three-axis Ob) | −1/op |
| Campaign | Territorial | 50 | 4 (total three-axis Ob) | −1/op |
| War | Structural | 70 | 5 (total three-axis Ob) | −2/op |

All Coherence loss is automatic (no check, no Ob) per threadwork_v30 §3.2. The Coherence
cap (−1 per operation, threadwork_v30 §3.2 per-operation cap) applies. No additional surcharge. *[THREAD-P1-02, THREAD-P2-01]*

**Coherence depletion warning (PP-501):** A practitioner operating every turn of a 7-turn battle loses 7 Coherence. From full (10): Coherence=3 after 7 turns — Dissonant, not Severed. Severance (Coherence=1) requires ≥9 consecutive operations from full. Battles ≥9 turns with constant operation produce Severance. *[THREAD-P2-02 — corrected PP-501]* *(PROVISIONAL marker stripped per editorial approval 2026-04-30.)*

**Diagnosis timing:** Phase 1 (public declaration = rendering the target
configuration). Leap phase: Phase 4 (rear practitioner) or Phase 5 (front-line
practitioner) — see §A.7 PP-101 positioning rule. *[THREAD-P2-03 revised by PP-101]*

**Combat-type operations** (offensive targeting): resolve Phase 4, no Defence
allocation unless embedded Threadweaver present. Counter = contested roll
per existing Thread contest rules. *[P2-09]*

**Non-combat operations**: resolve Phase 5 or 6 per operation type.

**Command cost:** general who Threadweaves cannot declare a tactical action
same turn.

**Co-movement at mass battle scale:** *[COMOVE-P2-01 fix]*
- Temporal result: general loses Phase 5 action for d3 turns
- Epistemic result: Command −1 for d3 turns (command confusion)
- Actual result: general takes 1 Wound

**Collective Thread operations:** viable if helpers are in Reserve (not
engaged). Helpers lose 1 Coherence per collective op. Full-battle collective
operations destroy all participating practitioners' Coherence at the same rate
as solo work. *[COLLECT-P2-01 — document explicitly]*

**Devout general:** cannot use Thread actions, cannot counter enemy Thread
operations. Enemy embedded Threadveavers operate freely against Devout-led
units. *[EDGE-01]*

**Severed (Coherence 1) general:** +2 Ob to all Thread operations. Dissociative
episode in mass battle = loses Phase 5 action for that turn. *[EDGE-02]*

**First Leap during battle:** Discovery Events during mass battle resolve at
Phase 6, not immediately. Unit unaffected. Failed First Leap (Dissociation):
character unavailable for remainder of battle. *[EDGE-03]*

**Thread Gaps from battle:** Gaps created during mass battle are registered
on the territory card at battle resolution. Standard Gap Mending Stability drift applies.
*[EDGE-05]*

---

### A.11 SOUTHERNMOST

Non-Thread-sensitive units (Thread Sensitivity < 30) cannot operate in Southernmost. They
dissolve without awareness on entry — no casualties, no Morale trigger, no
Discipline check. Remove from battle map. This is why Southernmost was never
conquered. *[confirmed — replaces all prior Discipline check variants]*

> **Clarification (PP-MB-06, revised PP-703 2026-04-30):** "The requirement 'all individuals must have Thread Sensitivity ≥ 30' applies at the individual level: any individual in a unit who lacks Thread Sensitivity ≥ 30 dissolves on entry to the Southernmost, without awareness, with no Morale trigger for surviving unit members. For unit-level accounting: reduce the unit's Size proportionally to the fraction of individuals who lack Thread Sensitivity ≥ 30. A unit with 40% Thread Sensitivity-capable individuals enters at 40% Size (round down to minimum 1 if any Thread Sensitivity-capable individuals remain, or 0 if none). Recalculate Effective Power from the reduced Size. **Practical constraint:** No faction can field a conventional military force in the Southernmost. The Forgetting (calamity_radiation_v30 §Forgetting) is universal — every individual entering Askeheim must have personal Thread Sensitivity ≥ 30 or dissolves on entry. Faction militaries are composed overwhelmingly of non-practitioners; they cannot operate as armies there. Only Restoration communities (whose membership cultivates TS through their cultural project) and ad-hoc expeditions composed entirely of TS ≥ 30 individuals (PCs, named-NPC practitioner-generals, hand-selected practitioner cohorts) can field viable forces. Askeheim was never conquered — not by Crown, not by Varfell, not by anyone — because the Forgetting does not respect faction. Faction-property exemptions are impossible by mechanism. *(Revised 2026-04-30: previous draft referenced VTM ≥ 2 as Varfell exemption — VTM struck per params/bg/core L6, and the Forgetting framing was incorrect.)*"

All individuals in a military force operating in Southernmost must personally
have Thread Sensitivity ≥ 30. No exceptions.

---

### A.12 ROUT AND PURSUIT

Routing: Slow/Standard cannot fight back. Fast may rearguard at −2D Off.
Pursuit: Fast units only. Routing unit loses Size equal to pursuer net
Offence successes (no Defence) each turn. Recall: Command Ob 2.
Over-pursuing exposes flanks. *[confirmed]*

**Morale Cascade (NEW — historical_precedents_warfare §1.3c):** When a unit routs (Morale reaches 0), at Phase 6 Step 3 (Morale checks), all friendly units in the same engagement make a Discipline check (Ob 1). Failure: Morale −1. Multiple simultaneous routs each trigger a separate cascade check; all fire together at Step 3. Multiple simultaneous routs compound — each triggers a separate cascade check. This models the historical reality where battles were lost when one section of the line broke and panic spread (Cannae, Hastings). The check is Ob 1 — Discipline 4 units pass ~87% — so cascades primarily threaten low-Discipline formations (Levy, militia), which is historically correct.

[EDITORIAL: ED-688 — Morale Cascade. Source: historical_precedents_warfare.md §1.3c.]

**Rout vs Destroyed (definitional boundary):** *Rout* = Morale reaches 0; unit flees and cannot fight back (§A.12 cascade fires). *Destroyed* = Size reaches 0; unit eliminated at Phase 6 Step 1. These are distinct states with distinct trigger chains. §A.12 Morale Cascade fires only on Morale rout, not on Size destruction. Artillery-caused unit elimination (Size→0) triggers the Morale −1 "allied unit routed in same zone" entry in §A.4 and PP-198 as a separate enumerated trigger — this does NOT fire the §A.12 Discipline check cascade.


**Stalemate Break (PP-297):** If 3 consecutive Battle Turns produce 0 total damage across all engagements (no Health loss on either side), both armies execute Tactical Withdrawal. Effects: no Piety Track movement, no pursuit, no Rout. Each side's general rolls Command Ob 1 to maintain formation during withdrawal; failure = −1 Discipline on one unit (disorderly retreat). The battle ends as inconclusive. Neither side claims victory. Accounting consequences: IP +1 (military posturing without resolution).

---

### A.13 REINFORCEMENT (between battles) *[editorial items]*

Natural: +1 Size per campaign season.
Accelerated: 1 Faction Resource per additional Size point.
Maximum: cannot exceed original Size at army creation.
Destroyed units (Size 0) cannot be restored — must raise new unit at full
Resource cost. Thread effects on units (over-actualisation, Locks) persist
across battle boundaries unless cleared. *[EDGE-08]*

**Morale reset between battles (PP-711, MB-03):** Morale resets to its starting formula (general's Command + unit quality modifier, cap 7) at the start of each new battle. Morale degradation does not persist across battle boundaries. Rationale: persistent Morale snowballs toward deterministic rout in long campaigns regardless of player decisions; campaign fatigue is a separate (future) mechanic at faction layer, not unit-level Morale.

**Discipline persists between battles (PP-712, MB-04):** Discipline does NOT auto-recover at battle end. Degradation accumulated in battle persists. Recovery requires a Muster action on the existing unit (military_layer_v30 §1.7), representing retraining and equipment replacement. Strategic consequence: burning Discipline through Reform-Phase tactics has multi-battle cost — Discipline is a depletable resource until garrison/Muster restores it. Wealth-Zero degradation per §1.7 stacks with battle degradation.

### A.14b CAMPAIGN SUPPLY (NEW — historical_precedents_warfare §1.3a)

Any faction with military units stationed in hostile territory (territory NOT controlled by the unit's faction) pays **Treasury −100/season** at Accounting (derived_stats_v1 §3.1). This is a flat cost regardless of how many units are deployed — it represents the logistical overhead of maintaining supply lines into hostile territory. Treasury depletion to 0 triggers Wealth −1 at the following Accounting (structural economic damage).

Units in friendly territory cost nothing (the population supports them).

**Attrition in devastated territory:** Units in any territory with Prosperity 0 lose **Size −1/season** from attrition — starvation, disease, desertion. Applies regardless of territorial control. A faction that devastates a territory's economy to conquer it cannot then garrison it effectively.

**Altonian exception:** Altonian Vanguard forces do NOT pay Campaign Supply in territories they occupy (they control supply through the invasion corridor). Valorian factions operating offensively in occupied zones DO pay.

**Design rationale:** Historical armies could not exist indefinitely in hostile territory without economic support. One flat cost creates economic pressure to conquer quickly or consolidate — the player feels their treasury draining without tracking per-unit logistics.

[EDITORIAL: ED-687 — Campaign Supply (simplified from per-unit table). Source: historical_precedents_warfare.md §1.3a.]

### A.14c LEVY RESTRICTION (NEW — historical_precedents_warfare §1.3b, simplified)

Levy units **cannot be used for offensive operations outside their home territory.** They defend the territory where they were mustered. They can be moved to adjacent friendly territories for defensive positioning but cannot March into hostile territory or participate in offensive Battle declarations.

Professional units (Light Infantry and above) have no such restriction — they campaign wherever the faction sends them, subject to Campaign Supply costs (§A.14b).

**Design rationale:** Feudal levies historically served close to home for limited terms. Rather than tracking service counters per unit, this rule captures the same strategic truth in one sentence: if you want to project force, you need professionals. Levies hold the line. This makes army composition a genuine choice — levies are free but defensive, professionals cost Wealth but can conquer.

**Battle outcome → faction consequences:** *[FACTION-P2-02 — proposed, EDITORIAL]*
**Battle outcome → peninsular consequences (PP-647, peninsular_strain_v1.md §3):**
- Each Battle resolved on Valorian soil: MS −1 (Campaign/War scale: MS −2). Immediate.
- Each season with inter-faction battle: IP +2 (checked at Accounting step 4e).
- Each season with inter-faction battle: Turmoil +1 (checked at Accounting step 4d).
- Popular Uprising (Accord 0 territory): MS −1. Does NOT trigger IP +2 or Strain +1 (not inter-faction).
- Altonian Vanguard battle: MS −1. Does NOT trigger IP +2 (Altonia's own operation) or Strain +1.
- Territory conquered by military victory: Accord set to 1 (peninsular_strain_v1.md §2.4).
- Unit destroyed: faction Military −1 (subject to ±2/season cap)
- Battle lost (defending force routed): Discipline −15 (derived_stats_v1)
- Campaign-scale defeat: Discipline −30 (derived_stats_v1). Mandate −1 (structural — campaign-scale defeats are major events)
[EDITORIAL: confirm Military stat change on unit destruction and Stability
check thresholds]

**Muster output (per Muster action):** *[FACTION-P2-03 — proposed, EDITORIAL]*
A Muster action produces 1 unit with Size = 2, Power = floor(faction Military / 2) + 1. Deploys following season. Multiple Muster actions stack.
[EDITORIAL: confirm Size=2 and Power derivation from Military stat]

---

### A.14 CROSS-SYSTEM NOTES

**Woven units — brittleness:** Thread-Woven Discipline or Morale boosts are
subject to threadwork_v30 §2.4 brittleness rules (MS ≤ 40 → Shifting Object trigger). Taking Size loss > Discipline in a single
turn qualifies as a non-Thread event of sufficient severity — engine resolves
the Woven configuration shattering into a Shifting Object. A Woven unit can be
simultaneously more and less resilient than an unworked unit. *[EDGE-07]*


must be converted to Mending Stability with inversion (Thread Tension +N → Mending Stability −N). *[EDGE-06 — P1,
requires separate compilation pass on stage5_clocks.md]*

---

## PART B: BOARD GAME MASS BATTLE

### B.1 DESIGN PRINCIPLE

BG battles resolve in a single Priority 2 slot. Total resolution time: 3–5
minutes. Strategic depth lives in preparation (unit composition, order
choice, tactic card selection), not in turn-by-turn execution.

The BG uses pre-existing unit stats (Martial / Endurance / Discipline / Health).
This proposal extends those stats with tactic cards and a clean TTRPG
compatibility bridge.

---

### B.2 BG UNIT STATS (pre-printed on unit tokens)

Inherits from B6 (existing BG unit table). No changes to existing stats.
TTRPG equivalence added for hybrid translation:

| BG Unit | Martial | Endur | Discipline | Health | TTRPG Power | TTRPG Size [PROV] | TTRPG Morale [PROV] | TTRPG Weapon | TTRPG Armour | Dmg Mod [PROV] |
|---|---|---|---|---|---|---|---|---|---|---|
| Levy | 1 | 1 | 1 | 7 | 1 | 3 | 2 | LightCut | None | +1 |
| Light Infantry | 3 | 3 | 3 | 9 | 3 | 4 | 4 | LightCut | Light | +2 |
| Heavy Infantry | 4 | 4 | 4 | 10 | 4 | 5 | 5 | HeavyCut | Medium | +4 |
| Cavalry | 4 | 3 | 5 | 9 | 5 | 4 | 5 | HeavyCut | Heavy | +5 |
| Archer | 3 | 2 | 3 | 8 | 3 | 3 | 3 | Piercing/Bow | Light | +0 |
| Crossbow | 3 | 2 | 3 | 8 | 3 | 3 | 3 | Piercing/Crossbow | Light | +0 base (+1 vs med+heavy post-DR) |
| Sling | 2 | 2 | 2 | 8 | 2 | 3 | 3 | Blunt/Sling | Light | by ammo (−2D) |
| Artillery | 2 | 2 | 2 | 8 | 2 | 3 | 3 | HBl (siege) | None | +3 |
| Knights Templar | 5 | 5 | 6 | 11 | 5 | 6 | 6 | HeavyBlunt | Heavy | +5 |

Size corrected: user audit −2 all units, −3 Ranged and Artillery (PP-104).
Dmg Mod (BG): used in BG battle formula. [EDITORIAL: ED-062 — BG values provisional]

**TTRPG Dmg Mod (PP-245):** TTRPG mass battle uses ⌈BG Dmg Mod ÷ 2⌉. BG unscaled values collapse TTRPG battles to one exchange (SIM-DEBT-05). Scaled values produce multi-exchange battles consistent with the 7-phase structure.

| Unit | BG Dmg Mod | TTRPG Dmg Mod |
|------|-----------|---------------|
| Levy | +1 | +1 |
| Light Infantry | +2 | +1 |
| Heavy Infantry | +4 | +2 |
| Cavalry | +5 | +3 |
| Archer | +0 | +0 |
| Crossbow | +0 (+1 vs med/heavy post-DR) | +0 (+1 vs med/heavy post-DR) |
| Sling | by ammo (−2D) | by ammo (−2D) |
| Artillery | +3 | +2 |
| Knights Templar | +5 | +3 |

Ranged: LP (arrows) default. Artillery: HBl (siege), Volley keyword, no melee.
Morale values: [PROVISIONAL] — ED-062 scope.

**Anti-Armour keyword** (HeavyBlunt units): +2D when targeting Heavy Infantry,
Cavalry, or Knights Templar. Pre-printed on Artillery and Knights Templar
tokens. *[replaces per-exchange DR lookup for BG]*

**Volley keyword** (Ranged, Artillery): fires in Priority 1 before melee.
Ranged cannot attack in melee same turn they Volley.

---

### B.3 BG BATTLE RESOLUTION

The existing disposition table (B6) is retained. Tactic cards replace open
disposition declaration.

**Step 1 — Tactic card play.**
Each side selects one tactic card from their hand and places it face-down.
Reveal simultaneously. Tactic cards map to the disposition table plus
provide additional modifiers. *[tactic card deck defined in B.4]*

**Step 2 — Disposition table.**
Read attacker's row (from tactic card disposition), defender's column.
Apply Ob and dice modifier.

**Step 3 — Roll.**
Pool = sum of all engaged unit Martial values + commander bonus.
Commander bonus = floor(faction Military / 2). *[PP-555]* TN 7. Ob from table.
Net successes = damage dealt to opposing units.

**Step 4 — Determine outcome by margin (PP-104):**

| Margin | Outcome | Effect |
|--------|---------|--------|
| Attacker net ≥ Defender net + 2 | Attacker wins | Territory captured; Defender Military −1 |
| Margin ≤ 1 either direction | Partial | No territory change; Attacker Discipline −15 (commitment cost, derived_stats_v1) |
| Defender net ≥ Attacker net + 2 | Defender wins | No territory change; Attacker Military −1 |

**Accord consequence (PP-645):** Territory gained via BG Battle: Accord set to 1 (Resistant). Defender loses Accord −1 in defended territory (war came to their home). See peninsular_strain_v1.md §2.4.

Partial reflects a costly inconclusive engagement — forces committed, ground unchanged.
*[PP-195 — confirmed: margin ≤1 = Partial; Attacker Discipline −15 (renamed from Cohesion per PP-232; Discipline is the derived stat = Stability × 10 per derived_stats_v30 §8). ED-705.]*

**Step 5 — Apply damage.** Reduce Health per Step 3 net successes × unit damage modifier − DR.
Formation Break at Health 0.

**Step 6 — Morale.** Formation Break → Discipline check Ob 2 → Route on fail.

**Thread in BG battles:** handled by Co-Movement cards per existing rules.
At Mending Stability < 20: T-03 fires — both sides draw 1 Co-Movement card per battle.
*[P3-c confirmed]*

---

### B.4 TACTIC CARDS

Each faction receives a hand of 6 tactic cards at game start (4 shared + 2
faction-specific). Cards refresh each season.

**Shared tactic cards (4):**

| Card | Disposition | Additional effect |
|---|---|---|
| Standard Advance | Offensive | No additional effect |
| Disciplined Defence | Defensive | If opponent plays Offensive or Brutal: +1D Defence this engagement |
| Feigned Retreat | Balanced | On loss: opponent's winning units are Overextended (−2D next season in same territory) |
| Concentrated Strike | Offensive | One unit of your choice rolls +2D this engagement |

**Faction-specific cards (2 per faction):** *[EDITORIAL: design faction cards]*
[EDITORIAL: confirm faction-specific tactic card designs. Proposed below for
approval — each reflects the faction's military doctrine.]

| Faction | Card 1 | Card 2 |
|---|---|---|
| Crown | Royal Guard (Elite unit +3D) | Ducal Call (summon 1 unit from adjacent territory) |
| Church | Crusade Fervour (Brutal + Discipline check exempt this turn) | Inquisitor's Mark (target unit −2D, any opponent) |
| Hafenmark | Mercenary Surge (pay 1 Wealth: +2 units this engagement) | Sovereign Authority (immune to Disposition table Ob penalties this engagement) |
| Varfell | Stratagem (read opponent's tactic card before locking yours — see Resolution below) | Calculated Retreat (withdraw without Overextended penalty) |
| Guilds | Paid Off (opponent unit −1D; costs 1 Wealth) | Logistics Mastery (Strained units fight at full this engagement) |
| Niflhel | Assassination (target opponent commander; −1D all opp. units) | Disappear (withdraw all units; opponent cannot pursue this season) |
| Löwenritter | Iron Discipline (immune to Route this engagement) | Martial Law (after winning: territory gains Martial Law next season) |
| Revolution | People's Courage (Discipline +1 all units this engagement) | Ambush (first engagement in Oastad or Stillhelm: opponent no Defence roll) |

**Tactic cards confirmed canonical (PP-283):** All faction-specific cards above are confirmed as canonical defaults. Content may be revised narratively without patch; mechanical effects require patch.

**Stratagem resolution (PP-690, supersedes Shadow Intel naming from PP-713):** At Phase 1 tactic-card resolution, the Varfell general's read of the battlefield triggers first: opposing tactic card is revealed face-up to Varfell. Varfell may then revise their own tactic card from hand once before both reveal simultaneously and resolve normally. Mechanically this is an initiative inversion at the tactic-card layer — Varfell becomes higher-initiative regardless of Speed/Command for that one card resolution. Doctrine grounding: classical battlefield reading — Hannibal at Trasimene, Belisarius reading Persian commitments, Vaynard's celebrated practice of identifying enemy standards and march-discipline before committing his own line. The opposing commander is *out-thought*, not deceived. UI: opposing tactic card flips face-up to Varfell only; Varfell's hand prompts revise-or-keep; both reveal on confirm. *(Renamed from Shadow Intel 2026-04-30 — see PP-690. Faction-secrecy framing replaced with prestige-doctrine framing per Vaynard's commonly-recognized-stratagem disposition.)*

---

### B.5 HYBRID HANDOFF

**No Player Character in battle:** BG resolution fires. Territory control applies. Faction
stat consequences (Military, Stability) apply at Accounting. Mending Stability changes from
any Thread orders apply at Accounting.

**Zoom In — Phase-Lock Protocol (PP-103):**
Zoom In may only fire at one of three legal phase-lock points:
- **After Phase 1** (orders placed, nothing resolved — cleanest entry)
- **After Phase 3** (manoeuvre complete, pre-Engagement)
- **After Phase 6 Step 1** (all damage applied, no ghost units)

If a Zoom In trigger occurs mid-phase, it is held and fires at the **next legal phase-lock point** — not the end of the current phase (PP-250). A trigger during Phase 5 Engagement defers to After Phase 6 Step 1 (not end-of-Phase-5, which preserves ghost-unit state). A trigger during Phase 2 defers to After Phase 3. A trigger within Phase 6 pre-Step-1 defers to After Phase 6 Step 1. This eliminates ghost-unit state (ED-057).

**BG → TTRPG unit conversion:** Translate BG unit tokens using §B.2. The table
provides TTRPG Power, Size (provisional), Morale (provisional), weapon, and armour
for each unit type. See the Zoom In/Out Reference Card (designs/gm_ref_cp14/)
for the one-page summary.

**Player Character faction leader present in contested territory:** BG resolution defers to
TTRPG mass battle rules for that engagement. The Player Character's Command and tactical decisions
play out in full. BG territory and stat consequences still apply at resolution.
Clock changes still batch to Accounting.

**Stat translation (TTRPG ↔ BG):**
- TTRPG unit Size → BG unit Health (Size × 1.5, round up — Health scale
  is 8–11, Size is 1–7; Size 4 ≈ Health 9)
- TTRPG general Command → BG commander bonus = floor(Military / 2)
- TTRPG Discipline → BG Discipline (direct, same scale)
- TTRPG Morale (rout) → BG Discipline check (rout equivalent)

---

## PART C: EDITORIAL ITEMS — RESOLVED (Phase 2.7, 2026-04-18)

All items below approved and confirmed canonical (ED-689).

| ID | Item | Resolution | Status |
|---|---|---|---|
| Command-EDIT-01 | Military stat → unit Power/Discipline ceiling (§A.4) | CONFIRMED: table in §A.4 is canonical | ✓ |
| Command-EDIT-02 | Battle outcome → faction stat consequences (§A.13) | CONFIRMED: −1 Military/unit destroyed; Stability checks per §A.13 | ✓ |
| Command-EDIT-03 | Muster → unit stats (§A.13) | CONFIRMED: Size=2, Power = floor(Military/2)+1 | ✓ |
| BG-EDIT-01 | Commander bonus formula (§B.3) | CONFIRMED: floor(Military/2) per PP-555 | ✓ |
| BG-EDIT-02 | Faction-specific tactic cards (§B.4) | CONFIRMED: 8 faction cards as specified | ✓ |
| CLOCK-EDIT-01 | IP 75+ Altonian invasion unit stats | DEFERRED: requires Phase 4 simulation for calibration | ⏳ |
| CLOCK-EDIT-02 | Church military victory → CI change | CONFIRMED: No CI change from military victory alone. CI changes from institutional actions only. | ✓ |
---

#
### Army Morale (Derived Composite — derived_stats_v1 §8.2)

Army Morale = floor(average unit Morale) + Command modifier + Discipline modifier. Gives the player a single legible indicator. Thresholds: 6+ Resolute (rout contagion blocked), 4–5 Steady, 2–3 Shaken (−1D Morale checks, Command check Ob 2 each phase), 1 Wavering (−2D, Command Ob 3 or Withdrawal), 0 Routed (army-level retreat, battle lost). See derived_stats_v1 §8.2 for full specification.

# PART D: MASS COMBAT WORLD BRIDGE (NEW)

### §D.1 Post-Battle Consequence Scenes

After every mass battle, the player receives a mandatory Scene Slate entry (Priority 0 per player_agency_v30 §4.2 Step 1 if present in province; Priority 1 per scale_transitions_v30 §4.3.3 if adjacent). The post-battle scene does not cost a scene action — it is the aftermath, and it is always worth experiencing.

**Settlement anchoring (per settlement_bridge_unification C-09):** The aftermath scene occurs at the specific settlement that was assaulted, besieged, or defended. Stat effects target that settlement's Prosperity/Defense/Order, not province Accord directly.

**Aftermath scene structure:**

The player arrives at or remains at the battle settlement after the battle resolves. The scene presents three choice points (the player selects one — the others resolve through NPC AI):

| Choice | Action | Mechanical Consequence |
|--------|--------|----------------------|
| Tend the wounded | Endurance or Attunement check, Ob 2 | Success: 1 surviving unit recovers +1 Size (casualties saved). Disposition +1 with all surviving unit officers. Overwhelming: Settlement Order +1 (compassion as governance). |
| Survey the damage | Cognition check, Ob 1 | Success: reveals exact casualties, territory infrastructure damage, and one hidden consequence (NPC death, Accord shift, or evidence planted during the chaos). Overwhelming: +1 Momentum (tactical understanding). |
| Address the population | Charisma check, Ob 2 | Success: Settlement Order +1 (speech as governance). Failure: Settlement Order −1 (the population needed comfort and received platitudes). Overwhelming: +1 Renown. |

**If the player was not present for the battle:** The aftermath scene is replaced by a "Where Were You?" retrospective scene per scale_transitions_v30 §4.4. The player learns about the battle's outcome through their social network. The three aftermath choices are not available — the moment has passed.

### §D.2 Named Unit Officers

Each mustered unit has one named officer NPC. The officer is generated at Muster with a minimal profile:

| Attribute | Value |
|-----------|-------|
| Name | Generated from territory of muster (GM or procedural). |
| Conviction | Inherited from faction (one of the faction's two Conviction values per npc_behavior_v30 §2). |
| Disposition toward player | Starting: +1 (the player's faction mustered them). |
| Resonant Style | Same as faction leader's primary Resonant Style. |

**Officer Disposition shifts:**
- Player issues a tactically sound command (Battle turn where player's choice contributes to victory): +1
- Player orders a retreat or sacrifice that saves the unit: +1
- Player orders the unit into a situation that costs Size ≥ 2: −1
- Player is absent from a battle where the unit fights: −1

**Officer death (recalibrated per ED-754, scoped per ED-765):** Roll once per battle resolution, not per Size-loss event. Computation: total Size lost in battle by the unit → roll 1d20. On result ≤ total Size lost, the officer is killed. Example: unit loses 2 Size in volley + 3 in engagement = 5 total → officer killed on 1-5 (25% rate). Per-battle resolution is significantly cleaner than per-event: it produces a known-bounded probability, doesn't double-count multi-stage attrition, and surfaces a single named-officer death moment per battle for narrative clarity.

Prior calibration (1d10) produced 50% officer death at routine 5-Size loss — campaigns lost all named officers in 4-6 battles. The 1d20 + per-battle calibration preserves narrative jeopardy (catastrophic losses still kill officers reliably) while permitting named officer NPCs to persist across multiple campaign battles.

**Death consequences:**
- Player receives notification: "Captain [Name] fell at [location]."
- If Disposition was ≥ +2: player's Conviction may be strained (same mechanic as combat death cascade in combat_v30 §13.3).
- If the unit had been with the player for 3+ seasons: +1 Renown (the loss is publicly mourned — the player's leadership is noted).

**Officer as settlement governor:** After a battle, a named officer at Disposition ≥ +2 may be assigned as governor of the battle settlement or any garrisoned settlement (per settlement_layer_v30 §3.2). The military officer transitions to civil administrator — the ROTK post-conquest appointment.

**Officer at Disposition +3:** The officer becomes eligible for companionship (per companion_specification_v30 §2.1). A unit officer who travels with the player as a companion still commands their unit in battle — dual role. If the companion-officer is killed in battle, the departure scene fires as a combat death, not a social departure.

### §D.3 Player Morale Effect

Units in the player's current territory gain +1 Discipline while the player is physically present during battle. This bonus applies whenever the player is in the territory, including during a personal combat pause (the player is still present; Command suspension and Discipline bonus are independent effects). If the player is wounded (2+ wounds) or incapacitated during the battle, all friendly units in the battle take −1 Discipline immediately (morale shock). This is the Mount & Blade effect — the player's presence on the battlefield matters to the soldiers.

**Board Game adaptation:** If a PC is embedded in a territory during battle (per scale_transitions_v30 §9 PC Faction Embedding), friendly units gain +1D on the first battle roll. This stacks with Commander bonus but is capped at +1D total from PC presence.


## PART E: BATTLE CONSEQUENCES (CANONICAL — ED-542)

Every Battle resolved on Valorian soil carries systemic costs beyond the immediate tactical outcome. These consequences are automatic — they do not require a roll and cannot be mitigated by the battle's outcome.

### §E.1 Immediate Consequences (at Battle resolution)

| Consequence | Trigger | Value |
|------------|---------|-------|
| Substrate Fracture | Any inter-faction Battle | MS −1 (Campaign/War scale: MS −2) |
| Accord erosion — conquered territory | Attacker conquers via Battle | Accord set to 1 (Category A: all settlements reset to Order 1) |
| Accord erosion — defender's territory | Battle occurs in a territory the defender controls | Order −1 in settlement nearest battle site (Category B per §2.5) |

### §E.2 Accounting Consequences (revised per ED-743)

Battle-occurrence is no longer a direct IP or Strain trigger. Battles produce Accord erosion at the *territory* level (§E.1). IP and Strain consequences fire downstream from that Accord erosion — the Accounting *after* a conquest, the conquered territory's Accord ≤ 1 status contributes to peninsula-wide IP and Strain counts.

| Consequence | Trigger | Mechanism |
|------------|---------|-----------|
| Substrate Fracture (immediate) | Any inter-faction Battle | MS −1 (Campaign/War scale: MS −2). See §E.1. |
| Accord erosion (immediate) | Conquest or defender's territory | See §E.1. |
| Vulnerability Signal (deferred) | Conquered/contested territories at Accord ≤ 1 at next Accounting | IP advance per peninsular_strain §3.2 (territory-count thresholds: 2-3 → +1; 4-5 → +2; 6+ → +3). |
| Turmoil (deferred) | Conquered/contested territories at Accord ≤ 1 at next Accounting | Strain advance per peninsular_strain §4.1 (+1/territory, cap +3/season). |

A faction that conquers AND rapidly governs the conquered territory to Accord ≥ 2 (typically 1-2 seasons via Govern actions) avoids both IP and Strain advance from that conquest. A faction that conquers and leaves territories at Accord 1 indefinitely pays sustained IP and Strain. **The cost is in the holding, not the conquest.**

[EDITORIAL: ED-743 — Battle-occurrence redirected to deferred Accord-based mechanism. ED-623 (+2 → +3 IP per battle-season) superseded; the IP mechanism itself relocated to peninsular_strain §3.2. Battle-season immediate costs (MS, Accord erosion) retained.]

### §E.3 Exceptions

- Covert operations (Niflhel sabotage, Church Seizure of ungarrisoned territories): no MS/IP/Strain cost.
- Altonian Vanguard battles: MS −1 (siege) only; no IP or Strain from these.
- Popular Uprisings (Accord 0 garrison combat): MS −1 only; no IP or Strain.
- Löwenritter Coup activation battles: Strain +1 only for first 2 seasons; no IP (per peninsular_strain §4.3 exemption).

### §E.4 Cumulative caps per season

Maximum MS change from battles: −3 per season (regardless of battle count within season). IP and Strain advancement caps now live in peninsular_strain §3.2 / §4.1 (territory-count-based, not battle-count-based). IP from territory-instability: cap +3/season (territory-count threshold). IP from CI ≥ 60: +2/season (independent track). Strain from territory-instability: cap +3/season. Strain from faction elim and Revolt: uncapped (discrete events). Battle-occurrence itself does not advance IP or Strain in the current ruleset (ED-743).

*Sources: peninsular_strain_v1.md §3, military_layer_v30.md §2.2b, victory_v30.md §0.4, board_game PP-647. This section consolidates those references into one canonical location.*
