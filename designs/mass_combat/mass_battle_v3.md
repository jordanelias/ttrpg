# VALORIA — MASS BATTLE SYSTEM v3
## All P1/P2/P3 patches applied. Gaps filled. Editorial notes flagged.
## Status: PROPOSAL — awaiting approval before GitHub push

---

## PART A: TTRPG MASS BATTLE

### A.1 OVERVIEW

Mass battle uses the same dice engine as personal combat. Pool split into
Offence/Defence, simultaneous resolution, TN-based successes, DR applied to
damage. Two stats unified in personal combat split here:

- **Strength** — headcount. Health pool. Casualties reduce it directly.
- **Combat Power (CP)** — fighting effectiveness per soldier. Equipment and
  training. Determines dice rolled.

**Effective Combat Pool = min(CP, current Strength)**

As Strength drops, the pool shrinks — fewer soldiers means fewer dice
regardless of individual quality. CP is the ceiling; Strength determines
whether you reach it.

**Design axiom: Generalship dominates.** CR asymmetry is intentional. A CR=7
general versus a CR=1 general produces a near-certain outcome before a die is
rolled. The general is the battle.

---

### A.2 WEAPON EFFECTIVENESS REFERENCE

| Attacker | vs None | vs Light | vs Medium | vs Heavy |
|---|---|---|---|---|
| LightCut | ✓ | ✗ | ✗ | ✗ |
| HeavyCut | ✓✓ | ✓✓ | ✓ | ✗ |
| LightBlunt | ✓ | ✗ | ✗ | ✗ |
| HeavyBlunt | ✓✓ | ✓✓ | ✓✓ | ✓✓ |
| Projectile | ✓ | ✗ | ✗ | ✗ |

HeavyBlunt is the only weapon effective against Heavy armour. Projectile units
are anti-unarmoured only. Deploying the wrong weapon against wrong armour deals
zero expected damage. This is not recoverable mid-battle. Force composition
determines outcome more than tactics.

---

### A.3 BATTLE SCALE

| Scale | 1 Strength = | Thread scale (see A.10) |
|---|---|---|
| Skirmish | ~10 soldiers | Personal |
| Company | ~100 soldiers | Object |
| Battle | ~500 soldiers | Territorial |
| Campaign | ~1,000 soldiers | Territorial |
| War | ~5,000 soldiers | Structural |

Scale is narrative only — no mechanical change except Thread TS minimums.

---

### A.4 UNIT STAT BLOCK (all 1–7)

**Strength** — health pool (headcount). At 0: destroyed.

**Combat Power (CP)** — dice pool ceiling.

| CP | Tier |
|---|---|
| 1 | Levy |
| 2 | Militia |
| 3 | Professional |
| 4 | Veteran |
| 5 | Elite |
| 6–7 | Exceptional/Peerless |

**Military stat → unit quality** [EDITORIAL: confirm mapping] *[FACTION-P2-01 fix]*
A faction's Military stat sets the CP ceiling and starting Cohesion ceiling
for units it fields. A Military=3 faction cannot field CP=5 units.

| Military | Max unit CP | Starting Cohesion ceiling |
|---|---|---|
| 1 | 1 | 2 |
| 2 | 2 | 3 |
| 3 | 3 | 4 |
| 4 | 4 | 5 |
| 5 | 5 | 6 |
| 6 | 6 | 7 |
| 7 | 7 | 7 |

**Speed** — Slow / Standard / Fast (3 tiers).

**Cohesion** (1–7) — organisational integrity. Starting value = min(general's
CR, Military ceiling above).

**Cohesion check — DETERMINISTIC:** *[P1-04]*
When total Strength lost this turn (all sources, applied at Phase 5) exceeds
Cohesion rating: Cohesion degrades by 1. All checks fire at Phase 5 regardless
of damage source (Volley, melee, environmental). *[P2-06]*

| Cohesion | Effective CP penalty |
|---|---|
| 5–7 | None |
| 3–4 | −1D |
| 1–2 | −2D |
| 0 | Formation broken; cannot attack; must reform or rout |

Cohesion restoration: Reform Phase only (unit not engaged), +1 Cohesion.
Requires general's CR ≥ current Cohesion + 1.
CR=1 general cannot restore Cohesion to any unit — all degradation is
permanent for that battle. *[NEW-P2-05 — confirmed as intended CR asymmetry]*

**Morale** (1–7) — rout threshold. Starting = general's CR + unit quality
modifier (cap 7).

Morale degradation triggers:
- Str dropped below 50% of max: −1
- Str dropped below 25%: −1 additional
- Cohesion broken this turn: −1
- Allied unit routed in same zone: −1
- General incapacitated (Stage 1): −1
- General killed (Stage 2): −2
- Flanked and lost exchange: −1
- No engagement for 2+ consecutive turns (idle army): −1 *[P2-02/P2-04]*

**Morale cap: −3 per Cascade Phase.** General killed (Stage 2) deals −2
separately, not subject to the cap. *[P1-03]*

While general is present: Morale floor = 1. At Morale 0: unit routs.

**Rout contagion brake:** Rout causes −1 Morale to adjacent units, but this
secondary loss cannot itself cause further routs until the next turn. *[P1-02]*

**Weapon Type** — (hit TN, def TN, damage modifier). Inherits personal combat
table unchanged.

**Armour Tier / DR table** — inherits personal combat table plus Projectile
column (= LightCut values). *[P2-07]*

| Armour | LightCut | HeavyCut | LightBlunt | HeavyBlunt | Projectile |
|---|---|---|---|---|---|
| None | 0 | 0 | 0 | 0 | 0 |
| Light | 2 | 1 | 1 | 0 | 2 |
| Medium | 4 | 3 | 2 | 1 | 4 |
| Heavy | 6 | 5 | 3 | 1 | 6 |

---

### A.5 COMMAND RATING

**CR = ⌈(Presence + Cognition) ÷ 2⌉** *[confirmed]*

CR governs:
1. Sub-unit limit (max simultaneous commanded = CR; TTRPG hard cap: 3)
2. Cohesion ceiling
3. Morale starting value and floor (= 1 while general present)
4. Tactic execution (CR dice vs Ob per tactic)

**NPC generals:** CR assigned directly (1–7) as a narrative stat without
Pres+Cog derivation. *[CR-P2-02]*

**General two-stage death:** *[P1-02]*
- Stage 1 (incapacitated): −1 Morale all units, CR halved, Morale floor
  suspended. Stabilise in Phase 5 with Medicine Ob 2 (1-turn window).
- Stage 2 (killed): Stage 2 fires at start of following turn's Phase 5
  if not stabilised. −2 Morale (outside cap), CR = 0, all units uncommanded.
  *[NEW-P2-02 — Stage 1 → 2 timing confirmed]*

**General in personal combat:** suspends all CR effects. Re-establish command
with CR check Ob 2 in Phase 1 of any subsequent turn. *[P2-10]*

**Wounds carry over:** Wounds from personal combat add +1 Ob to CR tactic
execution rolls. A 2-wound general has tactic success probability halved.
*[D3-P2-01 — confirmed intended]*

**Mass battle pauses during personal combat.** If general enters personal
combat, mass battle holds at current state. Resume at Phase 1 of next mass
battle turn after personal combat resolves. *[D3-P2-02]*

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

**Formation counter logic:** Wedge beats Line. Shield Wall negates Wedge but
cannot advance. No formation is universally dominant. *[P2-01]*

**Units beyond CR limit** fight at Line formation, Cohesion = 1 floor,
no tactics available. *[P3-03]*

---

### A.7 BATTLE TURN STRUCTURE

**Phase 1 — Strategy Declaration** (simultaneous, secret)
General declares: sub-unit assignments (max 3 for TTRPG), formation per
sub-unit, tactical action, and Thread intent (public). *[P1-01]*

Threadweaving: Diagnosis occurs in Phase 1 (public declaration = rendering
the configuration). Leap resolves in Phase 5. Configuration change between
Phase 1 and Phase 5 is covered by §4.2.2 (practitioner may revise before
Leap at no cost if configuration has changed significantly). *[THREAD-P2-03]*

**Phase 2 — Volley**
Projectile units fire. Roll Effective CP vs TN 6. Net successes − DR
(Projectile column) = Strength loss. Prepared Defence: declare in Phase 1;
half Effective CP as passive DR bonus (+1 per 2 dice). Volley Str loss
recorded for Phase 5 Cohesion check — does not fire immediately. *[P2-06]*

**Phase 3 — Manoeuvre**
Fast → Standard → Slow. Environmental modifiers applied. Reserve commitment
declared here (takes effect next turn's Phase 3). *[P3-02]*

**Phase 4 — Engagement** (max 3 simultaneous, TTRPG) *[P1-01]*

Per engagement:
1. Effective Pool = min(CP, Str) − Cohesion penalty
2. Apply Formation modifier
3. Split into Offence / Defence (both sides simultaneously)
4. Roll. Net hits = Offence succs − Defence succs
5. Damage = max(0, net hits + weapon modifier − DR)
6. Critical hit (net hits ≥ 3): weapon modifier doubled
7. Both sides take Strength damage simultaneously
8. Mutual destruction (both to 0) is valid — Pyrrhic outcomes possible *[P2-02]*

Mass Mismatch Penalty: Light weapon defender vs Heavy weapon attack − 1
defensive success (min 0). Exempt: Shield Wall.

**Phase 5 — Cascade** (strict order)

1. Apply all Strength damage (Volley + Engagement)
2. Cohesion checks (deterministic — per §A.4)
3. Morale checks (triggers + cap)
4. General action (one): Rally / Reinforce Cohesion / Threadweave / Personal
   combat / Stabilise incapacitated general
5. Thread Leap resolves (if declared Phase 1)

**Phase 6 — Reform**
Non-engaged units: restore Cohesion, recover 1 Morale, merge sub-units.
Idle army clock: if no engagements in Phase 4 this turn AND previous turn,
both sides lose 1 Morale in Phase 6. *[P2-02, P2-04]*

---

### A.8 TACTICS

| Tactic | Effect | Ob | Counter |
|---|---|---|---|
| Envelopment | Attempt all-flank; requires Fast | 2 | Refused Flank |
| Feigned Retreat | Disengage; pursuer Cohesion check; re-engage next turn with flank | 3 | CR Ob 2 to recognise |
| Ambush | First engagement: defender no Defence allocation | 4 | Scouting (GM) |
| Concentration | All sub-units on one target; max Fibonacci | 1 | Flanks exposed |
| Refused Flank | Wing anchors on terrain; immune to that flank | 1 | Sacrifices offence |
| Hammer & Anvil | Shield Wall holds; Fast unit envelops | 3 | Break Anvil first |

Split strategy note: Splitting only helps if defender must split too. Attacker
splitting Str=6 into 3+3 against undivided Str=5 defender is disadvantageous
— defender's full pool exceeds each sub-engagement. *[P2-14]*

---

### A.9 ENVIRONMENTAL MODIFIERS

| Terrain | Effect |
|---|---|
| River crossing | −1 Speed tier; −1D Off; Cohesion check (treat Str lost = 1) |
| Uphill | Defender +1D Def; attacker −1D Off |
| Forest / broken | Cavalry → Standard; flanking impossible |
| Walls / fortifications | Defender +3 DR; no flanking; Slow cannot advance |
| Narrow pass | 1 engagement per side; Fibonacci impossible |
| Open flat | No modifiers |

---

### A.10 THREAD OPERATIONS IN MASS BATTLE

**Corrected scale mapping:** *[THREAD-P1-01 fix]*

| Battle scale | Thread scale | Min TS | Thread Ob | Coherence auto-cost |
|---|---|---|---|---|
| Skirmish | Personal | 30 | 2 | 0 |
| Company | Object | 30 | 1 | 0 |
| Battle | Territorial | 50 | 4 | −1/op |
| Campaign | Territorial | 50 | 4 | −1/op |
| War | Structural | 70 | 5 | −2/op |

All Coherence loss is automatic (no check, no Ob) per §5.2.2. The Coherence
cap (−1 per operation, §5.2.3) applies. No additional surcharge. *[THREAD-P1-02, THREAD-P2-01]*

**Coherence depletion warning:** A practitioner operating every turn of a
7-turn battle loses 7 Coherence. From full (10): Severed after 9 total
operations. Full-battle Threadweaving is a practitioner self-destruction event.
*[THREAD-P2-02 — document explicitly]*

**Diagnosis timing:** Phase 1 (public declaration = rendering the target
configuration). Leap in Phase 5. *[THREAD-P2-03]*

**Combat-type operations** (offensive targeting): resolve Phase 4, no Defence
allocation unless embedded Threadweaver present. Counter = contested roll
per existing Thread contest rules. *[P2-09]*

**Non-combat operations**: resolve Phase 5 or 6 per operation type.

**Command cost:** general who Threadweaves cannot declare a tactical action
same turn.

**Co-movement at mass battle scale:** *[COMOVE-P2-01 fix]*
- Temporal result: general loses Phase 5 action for d3 turns
- Epistemic result: CR −1 for d3 turns (command confusion)
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
on the territory card at battle resolution. Standard Gap RS drift applies.
*[EDGE-05]*

---

### A.11 SOUTHERNMOST

Non-Thread-sensitive units (TS < 30) cannot operate in Southernmost. They
dissolve without awareness on entry — no casualties, no Morale trigger, no
Cohesion check. Remove from battle map. This is why Southernmost was never
conquered. *[confirmed — replaces all prior Cohesion check variants]*

All individuals in a military force operating in Southernmost must personally
have TS ≥ 30. No exceptions.

---

### A.12 ROUT AND PURSUIT

Routing: Slow/Standard cannot fight back. Fast may rearguard at −2D Off.
Pursuit: Fast units only. Routing unit loses Strength equal to pursuer net
Offence successes (no Defence) each turn. Recall: CR Ob 2.
Over-pursuing exposes flanks. *[confirmed]*

---

### A.13 REINFORCEMENT (between battles) *[editorial items]*

Natural: +1 Strength per campaign season.
Accelerated: 1 Faction Resource per additional Strength point.
Maximum: cannot exceed original Strength at army creation.
Destroyed units (Str 0) cannot be restored — must raise new unit at full
Resource cost. Thread effects on units (over-actualisation, Locks) persist
across battle boundaries unless cleared. *[EDGE-08]*

**Battle outcome → faction consequences:** *[FACTION-P2-02 — proposed, EDITORIAL]*
- Unit destroyed: faction Military −1 (subject to ±2/season cap)
- Battle lost (defending force routed): Stability check Ob 1
- Campaign-scale defeat: Stability check Ob 2, Mandate −1
[EDITORIAL: confirm Military stat change on unit destruction and Stability
check thresholds]

**Muster output (per Muster action):** *[FACTION-P2-03 — proposed, EDITORIAL]*
A Muster action produces 1 unit with Strength = 2, CP = faction Military ÷ 2
(round up). Deploys following season. Multiple Muster actions stack.
[EDITORIAL: confirm Str=2 and CP derivation from Military stat]

---

### A.14 CROSS-SYSTEM NOTES

**Woven units — brittleness:** Thread-Woven Cohesion or Morale boosts are
subject to §4.3.4 brittleness rules. Taking Str loss > Cohesion in a single
turn qualifies as a non-Thread event of sufficient severity — GM may rule
the Woven configuration shatters into a Shifting Object. A Woven unit can be
simultaneously more and less resilient than an unworked unit. *[EDGE-07]*

**TT references in stage5_clocks.md:** Compilation error — all TT references
must be converted to RS with inversion (TT +N → RS −N). *[EDGE-06 — P1,
requires separate compilation pass on stage5_clocks.md]*

---

## PART B: BOARD GAME MASS BATTLE

### B.1 DESIGN PRINCIPLE

BG battles resolve in a single Priority 2 slot. Total resolution time: 3–5
minutes. Strategic depth lives in preparation (unit composition, order
choice, tactic card selection), not in turn-by-turn execution.

The BG uses pre-existing unit stats (Martial / Endurance / Cohesion / Health).
This proposal extends those stats with tactic cards and a clean TTRPG
compatibility bridge.

---

### B.2 BG UNIT STATS (pre-printed on unit tokens)

Inherits from B6 (existing BG unit table). No changes to existing stats.
TTRPG equivalence added for hybrid translation:

| BG Unit | Martial | Endur | Cohesion | Health | TTRPG CP equiv | TTRPG Weapon | TTRPG Armour |
|---|---|---|---|---|---|---|---|
| Light Infantry | 3 | 3 | 3 | 9 | 3 | LightCut | Light |
| Heavy Infantry | 4 | 4 | 4 | 10 | 4 | HeavyCut | Medium |
| Cavalry | 4 | 3 | 5 | 9 | 5 | HeavyCut | Heavy |
| Ranged | 3 | 2 | 3 | 8 | 3 | Projectile | Light |
| Artillery | 2 | 2 | 2 | 8 | 2 | HeavyBlunt | None |
| Knights Templar | 5 | 5 | 6 | 11 | 5 | HeavyBlunt | Heavy |

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
Commander bonus = faction Military ÷ 3, round down (min 0, max +2D).
[EDITORIAL: confirm commander bonus formula] TN 7. Ob from table.
Net successes = damage dealt to opposing units.

**Step 4 — Apply damage.** Reduce opposing unit Health. Formation Break at 0.

**Step 5 — Morale.** Formation Break → Cohesion check Ob 2 → Route on fail.

**Thread in BG battles:** handled by Co-Movement cards per existing rules.
At RS < 20: T-03 fires — both sides draw 1 Co-Movement card per battle.
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
| Church | Crusade Fervour (Brutal + Cohesion check exempt this turn) | Inquisitor's Mark (target unit −2D, any opponent) |
| Hafenmark | Mercenary Surge (pay 1 Wealth: +2 units this engagement) | Sovereign Authority (immune to Disposition table Ob penalties this engagement) |
| Varfell | Shadow Intel (see opponent's tactic card before revealing yours) | Calculated Retreat (withdraw without Overextended penalty) |
| Guilds | Paid Off (opponent unit −1D; costs 1 Wealth) | Logistics Mastery (Strained units fight at full this engagement) |
| Niflhel | Assassination (target opponent commander; −1D all opp. units) | Disappear (withdraw all units; opponent cannot pursue this season) |
| Löwenritter | Iron Discipline (immune to Route this engagement) | Martial Law (after winning: territory gains Martial Law next season) |
| Revolution | People's Courage (Cohesion +1 all units this engagement) | Ambush (first engagement in Oastad or Stillhelm: opponent no Defence roll) |

---

### B.5 HYBRID HANDOFF

**No PC in battle:** BG resolution fires. Territory control applies. Faction
stat consequences (Military, Stability) apply at Accounting. RS changes from
any Thread orders apply at Accounting.

**PC faction leader present in contested territory:** BG resolution defers to
TTRPG mass battle rules for that engagement. The PC's CR and tactical decisions
play out in full. BG territory and stat consequences still apply at resolution.
Clock changes still batch to Accounting.

**Stat translation (TTRPG ↔ BG):**
- TTRPG unit Strength → BG unit Health (Str × 1.5, round up — Health scale
  is 8–11, Str is 1–7; Str 4 ≈ Health 9)
- TTRPG general CR → BG commander bonus (CR ÷ 2, round down)
- TTRPG Cohesion → BG Cohesion (direct, same scale)
- TTRPG Morale (rout) → BG Cohesion check (rout equivalent)

---

## PART C: OPEN EDITORIAL ITEMS

All items below require user approval before compilation.

| ID | Item | Proposed resolution |
|---|---|---|
| CR-EDIT-01 | Military stat → unit CP/Cohesion ceiling (§A.4) | Table above — confirm |
| CR-EDIT-02 | Battle outcome → faction stat consequences (§A.13) | −1 Military/unit destroyed; Stability checks as above |
| CR-EDIT-03 | Muster → unit stats (§A.13) | Str=2, CP = Military÷2 |
| BG-EDIT-01 | Commander bonus formula (§B.3) | Military ÷ 3, round down |
| BG-EDIT-02 | Faction-specific tactic cards (§B.4) | 8 faction cards above |
| CLOCK-EDIT-01 | IP 75+ Altonian invasion unit stats | See simulation report |
| CLOCK-EDIT-02 | Church military victory → TC change | No TC change from military victory alone (confirm) |

---

# PART D: STRESS TEST PATCHES — v3-ST
## Source: designs/board_game/valoria_bg_v05_stress_test_report.md
## Applied: 2026-04-02

---

## ST-MB-01 — Volley TN 6 vs Universal TN 7
**[EDITORIAL: requires user approval — ST-MB-01 Volley TN]**
§A.7 Phase 2 states "Roll Effective CP vs TN 6." All other rolls use TN 7. Volley is therefore 25% more accurate per die than melee.
Confirm: (a) TN 6 for Volley is intentional (representing structural advantage of massed ranged fire vs melee chaos — if yes, add a sentence documenting this as an explicit exception), or (b) update Volley to TN 7 for consistency.

---

## ST-MB-02 — Coherence Undefined
**[CRITICAL GAP — ST-MB-02]**
§A.10 references "Coherence" extensively as a practitioner-specific stat (auto-cost −1/op, Severed at Coherence 1, depletion warning). This stat is not defined in mass_battle_v3, does not appear in the unit stat block (§A.4), and does not match any other stat in the compiled v0.14 checkpoint.
§A.10 is unplayable until Coherence is defined. Required:
1. Starting value formula
2. Where it appears on character/unit sheets
3. What happens when it reaches 0 (beyond the noted "Severed (Coherence 1): +2 Ob")
**[EDITORIAL: requires user approval — Coherence stat definition]**
Note: Coherence may be the practitioner's personal Coherence track (the renamed Intelligibility/Taint from the TTRPG, currently 10→0 countdown). If so, "Coherence auto-cost −1/op" means each Thread operation in mass battle costs 1 from the practitioner's personal Coherence track. Confirm and align with stage5_clocks.md.

---

## ST-MB-03 — Effective CP Timing with Simultaneous Damage
**[PATCH MB-01]**
Add to §A.7 Phase 4 before the damage application step:

> "Effective CP is calculated at the start of Phase 4 using Strength as of Phase 3 end. All damage within Phase 4 is applied simultaneously at Phase 5 Step 1. CP does not change within a single Phase 4 — a unit that takes damage mid-Phase 4 does not recalculate its Effective CP until Phase 5."

---

## ST-MB-04 — Morale Cap and General Kill Application Order
**[PATCH MB-02]**
Add to §A.4 (Morale) or wherever the −3 Morale cap is stated:

> "Application order: Apply all non-general Morale changes first, capping the total at −3 from these sources. Then apply Stage 2 general death −2 additionally (this −2 is separate and not subject to the cap). Maximum total Morale loss in one Cascade Phase: −5 (−3 capped + −2 general kill)."

---

## ST-MB-05 — CR=0 Uncommanded Units
**[PATCH MB-03]**
Add the following example to §A.5 (Command Rating) after the CR=0 definition:

> "Example: A general is killed (Stage 2). CR drops to 0. All units in the force are now uncommanded — each fights at Line formation, Cohesion floor 1, with no tactics available (no cards may be played). This is severe but survivable for units with strong base stats. Note: Stage 2 death also suspends the Morale floor, so uncommanded units may rout on any subsequent Morale trigger without a floor to catch them."

---

## ST-MB-06 — Reserve Commitment Timing
**[PATCH MB-04]**
Add to §A.6 Reserve definition and to §A.7 Phase 3:

> "Reserve commitment at Phase 3 of Turn N+1 makes the unit immediately available for Phase 4 engagement in that same turn (Turn N+1). Commitment does not delay the unit to Turn N+2. Summary: declare Reserve in Phase 3 of Turn N → unit commits at Phase 3 of Turn N+1 → unit may engage in Phase 4 of Turn N+1."

---

## ST-MB-07 — Shield Wall vs Three-Sided Encirclement
**[CONFIRMED — add example only]**
Add to §A.6 Shield Wall:

> "Three-sided encirclement example: Front, Left flank, Right flank simultaneously. Shield Wall negates one declared flank (say, Left). Front attack is fully defended (+2D Def). Right flank attack applies normally (full flanking bonus to attacker). The defender faces two unmitigated engagements and one defended — this is the intended design ceiling for Shield Wall. CR = 3 maximum means a force cannot be attacked from more than three directions simultaneously."

---

## ST-MB-08 — Feigned Retreat Recognition Pool
**[PATCH MB-05]**
Revise §A.8 Tactics entry for Feigned Retreat. Replace "CR Ob 2 to recognise" with:

> "Roll a number of d10s equal to the opposing general's CR score, against Ob 2, to recognise the Feigned Retreat as a feint rather than a genuine withdrawal. Success: the pursuing side is not deceived; the Feigned Retreat has no effect this turn. Failure (or no roll if the opposing general is killed): pursuing side pursues normally and suffers the Cohesion check."

---

## ST-MB-09 — Mixed TS Forces in Southernmost
**[PATCH MB-06]**
Replace or supplement the current §A.11 Southernmost entry with:

> "The requirement 'all individuals must have TS ≥ 30' applies at the individual level: any individual in a unit who lacks TS ≥ 30 dissolves on entry to the Southernmost, without awareness, with no Morale trigger for surviving unit members.
> For unit-level accounting: reduce the unit's Strength proportionally to the fraction of individuals who lack TS ≥ 30. A unit with 40% TS-capable individuals enters at 40% Strength (round down to minimum 1 if any TS-capable individuals remain, or 0 if none). Recalculate Effective CP from the reduced Strength.
> Practical constraint: Only Restoration communities and Varfell forces with VTM ≥ 2 can field meaningful units in the Southernmost. Crown, Church, Hafenmark, Guilds, and Niflhel cannot field viable military forces there."

---

## ST-MB-10 — Woven Unit Shifting Object Timing
**[PATCH MB-07]**
Replace the current §A.14 Woven unit shattering rule with:

> "A Woven unit configuration that shatters (Str loss in a single turn > current Cohesion) does not become a Shifting Object during the battle. For the remainder of the battle, it fights at Line formation, Cohesion 1. The Shifting Object status is registered for post-battle Thread consequences — the GM tracks this and applies it in the narrative aftermath. This prevents mid-battle stat volatility while preserving the Thread consequence."

---

## ST-INT-01 — BG vs TTRPG Pool Incompatibility (see also BG doc Part 13)
Patch text is in BG doc PART THIRTEEN, ST-INT-01 (PATCH P-38). Add cross-reference to §B.5:
> "See BG document P-38 for the explicit statement that BG and TTRPG battle pool systems are intentionally non-equivalent and produce different expected outcomes."

---

## ST-INT-03 — Volley TN in Hybrid Mode
**[EDITORIAL: contingent on ST-MB-01 resolution]**
Once ST-MB-01 is resolved (Volley TN confirmed as 6 or corrected to 7), add to §B.5:
> "In hybrid mode, Volley attacks by BG Ranged units transitioning to TTRPG use [TN confirmed by ST-MB-01 resolution]. TTRPG mass battle rules govern all rolls in hybrid mode."

---

## ST-INT-04 — Military Stat Loss Cap: Battle vs Domain Actions
**[EDITORIAL: requires user approval — ST-INT-04 seasonal cap pooling]**
Confirm: does the ±2/season Military cap from §A.13 (FACTION-P2-02) apply separately from, or pooled with, Domain Action Military changes?
If pooled: a faction losing 2 units in battle (−2 Military, cap reached) cannot be further weakened by Domain Actions targeting Military that season.
If separate: faction can lose up to −4 Military in one season (−2 battle + −2 Domain).

---

## ST-INT-06 — BG Unit TS (see also BG doc Part 13, PATCH P-40)
> Cross-reference added. Bridge rule for BG unit TS in Southernmost is in BG doc PATCH P-40.

---

## ST-INT-09 — Military Loss Timing (see also BG doc Part 13, PATCH P-41)
> Military timing rule (immediate in TTRPG, Accounting in BG, TTRPG timing in hybrid) is in BG doc PATCH P-41.

---

## PART D SUMMARY — Outstanding Items

| ID | Status |
|----|--------|
| ST-MB-01 (Volley TN) | EDITORIAL — confirm before distribution |
| ST-MB-02 (Coherence) | CRITICAL GAP + EDITORIAL — blocks §A.10 |
| ST-INT-02 (Commander bonus) | EDITORIAL — see BG doc |
| ST-INT-04 (Military cap pooling) | EDITORIAL |
| ST-INT-07 (Ceiral Ritual scale) | EDITORIAL — see BG doc |
| ST-INT-08 (Muster BG token) | EDITORIAL — see BG doc |
| ST-INT-12 (Altonian unit stats) | EDITORIAL BLOCKER — see BG doc |
