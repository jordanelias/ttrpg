# VALORIA — MASS BATTLE SYSTEM v4
## Version: v4.4 (PP-106 applied: HBl Dmg Mod +5→+3, Artillery sight-line rule, personal combat projectile reference)
## Status: WORKING DESIGN — no appendix sections. Read straight through.
## Three-mode: TTRPG/Hybrid (Part A); Board Game (Part B); Hybrid Handoff (§B.5)
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

**Design axiom: Generalship dominates.** Coherence Rating asymmetry is intentional. A Coherence Rating=7
general versus a Coherence Rating=1 general produces a near-certain outcome before a die is
rolled. The general is the battle.

---

### A.2 WEAPON EFFECTIVENESS REFERENCE

| Attacker | vs None | vs Light | vs Medium | vs Heavy |
|---|---|---|---|---|
| LightCut | ✓ | ✗ | ✗ | ✗ |
| HeavyCut | ✓✓ | ✓✓ | ✓ | ✗ |
| LightBlunt | ✓ | ✗ | ✗ | ✗ |
| HeavyBlunt | ✓✓ | ✓✓ | ✓✓ | ✓✓ |
| LP — Light Pierce (arrows) | ✓ | ✓ | ✗ | ✗ |
| HP — Heavy Pierce (bolts) | ✓✓ | ✓✓ | ✓ | ✗ |
| LBl — Light Blunt (sling) | ✓ | ✗ | ✗ | ✗ |
| HBl — Heavy Blunt Siege | ✓✓ | ✓✓ | ✓✓ | ✓✓ |

HeavyBlunt and HBl (siege) are the only weapon classes effective against Heavy
armour. LP (arrows) penetrate light armour; HP (crossbow bolts) penetrate
medium; LBl (sling) are anti-unarmoured only. Force composition determines
outcome more than tactics. [EDITORIAL: ED-061 — confirm 4-category split and
sub-unit types for Ranged (archer/crossbow/slinger)]

**Personal combat projectile weapons:** LP, HP, and LBl are also defined for
individual fighters in personal combat. See references/params_combat.md §Ranged
Combat Rules (PP-105). HBl has no personal combat equivalent (siege crew fight as
melee/unarmed). The DR values above apply to both mass combat (unit scale) and personal
combat (individual scale, same formula).

---

### A.3 BATTLE SCALE

| Scale | 1 Strength = | Thread scale (see A.10) |
|---|---|---|
| Skirmish | ~10 soldiers | Personal |
| Company | ~100 soldiers | Object |
| Battle | ~500 soldiers | Territorial |
| Campaign | ~1,000 soldiers | Territorial |
| War | ~5,000 soldiers | Structural |

Scale is narrative only — no mechanical change except Thread Thread Sensitivity minimums.

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
Coherence Rating, Military ceiling above).

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
Requires general's Coherence Rating ≥ current Cohesion + 1.
Coherence Rating=1 general cannot restore Cohesion to any unit — all degradation is
permanent for that battle. *[NEW-P2-05 — confirmed as intended Coherence Rating asymmetry]*

**Morale** (1–7) — rout threshold. Starting = general's Coherence Rating + unit quality
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

> **Clarification:** "Application order: Apply all non-general Morale changes first, capping the total at −3 from these sources. Then apply Stage 2 general death −2 additionally (this −2 is separate and not subject to the cap). Maximum total Morale loss in one Cascade Phase: −5 (−3 capped + −2 general kill)."

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

**Coherence Rating = ⌈(Presence + Cognition) ÷ 2⌉** *[confirmed]*

Coherence Rating governs:
1. Sub-unit limit (max simultaneous commanded = Coherence Rating; TTRPG hard cap: 3)
2. Cohesion ceiling
3. Morale starting value and floor (= 1 while general present)
4. Tactic execution (Coherence Rating dice vs Ob per tactic)

**Non-Player Character generals:** Coherence Rating assigned directly (1–7) as a narrative stat without
Pres+Cog derivation. *[Coherence Rating-P2-02]*

**General two-stage death:** *[P1-02]*
- Stage 1 (incapacitated): −1 Morale all units, Coherence Rating halved, Morale floor
  suspended. Stabilise in Phase 5 with Medicine Ob 2 (1-turn window).
- Stage 2 (killed): Stage 2 fires at start of following turn's Phase 5
  if not stabilised. −2 Morale (outside cap), Coherence Rating = 0, all units uncommanded.
  *[NEW-P2-02 — Stage 1 → 2 timing confirmed]*

**General in personal combat:** suspends all Coherence Rating effects. Re-establish command
with Coherence Rating check Ob 2 in Phase 1 of any subsequent turn. *[P2-10]*

**Wounds carry over:** Wounds from personal combat add +1 Ob to Coherence Rating tactic
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

> **Clarification:** "Roll a number of d10s equal to the opposing general's Coherence Rating score, against Ob 2, to recognise the Feigned Retreat as a feint rather than a genuine withdrawal. Success: the pursuing side is not deceived; the Feigned Retreat has no effect this turn. Failure (or no roll if the opposing general is killed): pursuing side pursues normally and suffers the Cohesion check."

> **Clarification (PP-MB-04):** "Reserve commitment at Phase 3 of Turn N+1 makes the unit immediately available for Phase 4 engagement in that same turn (Turn N+1). Commitment does not delay the unit to Turn N+2. Summary: declare Reserve in Phase 3 of Turn N → unit commits at Phase 3 of Turn N+1 → unit may engage in Phase 4 of Turn N+1."

> **Clarification (PP-MB-07):** "Three-sided encirclement example: Front, Left flank, Right flank simultaneously. Shield Wall negates one declared flank (say, Left). Front attack is fully defended (+2D Def). Right flank attack applies normally (full flanking bonus to attacker). The defender faces two unmitigated engagements and one defended — this is the intended design ceiling for Shield Wall. Coherence Rating = 3 maximum means a force cannot be attacked from more than three directions simultaneously."

**Formation counter logic:** Wedge beats Line. Shield Wall negates Wedge but
cannot advance. No formation is universally dominant. *[P2-01]*

**Units beyond Coherence Rating limit** fight at Line formation, Cohesion = 1 floor,
no tactics available. *[P3-03]*

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
Projectile units fire. Roll Effective CP vs TN 6. Net successes − DR
(Projectile column) = Strength loss to record.
Prepared Defence: declare in Phase 1; half Effective CP as passive DR
against Volley attacks this turn (rounded down, min 0).

**Artillery sight-line rule (PP-106):** HBl (Artillery) units require unobstructed
line of sight. A unit in Line formation positioned between the Artillery and its
target blocks the shot. Artillery must target units in an unobstructed zone.
Primary counter to Artillery: maintain a screening formation in front of your
vulnerable units, then flank to threaten Artillery directly.
bonus (+1 per 2 dice).
**Volley Strength loss is recorded but NOT applied until Phase 6 Step 1.**
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

A unit whose Strength is reduced to 0 by Phase 4 Thread effects is removed
at Phase 6 Step 1 and does not participate in Phase 5 Engagement.
Configuration changes between Phase 1 declaration and Phase 4 resolution:
practitioner may revise target at no cost if the declared configuration has
changed significantly (unit destroyed, routed, or repositioned). *[THREAD-P2-03]*

Practitioner rarity note: Phase 4 fires only when a practitioner is present.
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
1. Effective Pool = min(CP, current Str as of Phase 3 end) − Cohesion penalty
2. Apply Formation modifier
3. Split into Offence / Defence (both sides simultaneously)
4. Roll. Net hits = Offence succs − Defence succs
5. Damage = max(0, net hits + weapon modifier − DR)
6. Critical hit (net hits ≥ 3): weapon modifier doubled
7. Engagement damage recorded. NOT applied until Phase 6 Step 1.
8. Mutual destruction (both to 0) is valid — Pyrrhic outcomes possible *[P2-02]*

> **Clarification (PP-MB-01):** "Effective CP is calculated at the start of Phase 4 using Strength as of Phase 3 end. All damage within Phase 4 is applied simultaneously at Phase 5 Step 1. CP does not change within a single Phase 4 — a unit that takes damage mid-Phase 4 does not recalculate its Effective CP until Phase 5."

Mass Mismatch Penalty: Light weapon defender vs Heavy weapon attack − 1
defensive success (min 0). Exempt: Shield Wall.

**Phase 6 — Cascade** (strict order)

1. Apply ALL recorded Strength damage simultaneously:
   Volley (Phase 2) + Offensive Thread (Phase 4) + Engagement (Phase 5).
   Units reduced to 0 Strength are destroyed. Pyrrhic mutual destruction valid.
2. Cohesion checks (deterministic — per §A.4)
3. Morale checks (triggers + cap per §A.4; PP-082 general kill separate)
4. General action (one): Rally / Reinforce Cohesion / **Support Threadweave**
   (Weaving, Mending — see below) / Personal combat / Stabilise incapacitated
   general
5. Support Thread Leap resolves (if declared in Phase 1 as support intent)

Support Thread operations (Phase 6 step 4–5): Weaving (Cohesion bolster,
unit hardening), Mending (Strength restoration), Rally (W-33). These fire
after casualties are known — practitioners respond to what the battle has done.

**Phase 7 — Reform**
Non-engaged units: restore Cohesion, recover 1 Morale, merge sub-units.
Idle army clock: if no engagements in Phase 5 this turn AND previous turn,
both sides lose 1 Morale in Phase 7. *[P2-02, P2-04]*

---

### A.8 TACTICS

| Tactic | Effect | Ob | Counter |
|---|---|---|---|
| Envelopment | Attempt all-flank; requires Fast | 2 | Refused Flank |
| Feigned Retreat | Disengage; pursuer Cohesion check; re-engage next turn with flank | 3 | Coherence Rating Ob 2 to recognise |
| Ambush | First engagement: defender no Defence allocation | 4 | Scouting (Game Master) |
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

| Battle scale | Thread scale | Min Thread Sensitivity | Thread Ob | Coherence auto-cost |
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
- Epistemic result: Coherence Rating −1 for d3 turns (command confusion)
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
on the territory card at battle resolution. Standard Gap Rendering Stability drift applies.
*[EDGE-05]*

---

### A.11 SOUTHERNMOST

Non-Thread-sensitive units (Thread Sensitivity < 30) cannot operate in Southernmost. They
dissolve without awareness on entry — no casualties, no Morale trigger, no
Cohesion check. Remove from battle map. This is why Southernmost was never
conquered. *[confirmed — replaces all prior Cohesion check variants]*

> **Clarification (PP-MB-06):** "The requirement 'all individuals must have Thread Sensitivity ≥ 30' applies at the individual level: any individual in a unit who lacks Thread Sensitivity ≥ 30 dissolves on entry to the Southernmost, without awareness, with no Morale trigger for surviving unit members. For unit-level accounting: reduce the unit's Strength proportionally to the fraction of individuals who lack Thread Sensitivity ≥ 30. A unit with 40% Thread Sensitivity-capable individuals enters at 40% Strength (round down to minimum 1 if any Thread Sensitivity-capable individuals remain, or 0 if none). Recalculate Effective CP from the reduced Strength. Practical constraint: Only Restoration communities and Varfell forces with VTM ≥ 2 can field meaningful units in the Southernmost. Crown, Church, Hafenmark, Guilds, and Niflhel cannot field viable military forces there."

All individuals in a military force operating in Southernmost must personally
have Thread Sensitivity ≥ 30. No exceptions.

---

### A.12 ROUT AND PURSUIT

Routing: Slow/Standard cannot fight back. Fast may rearguard at −2D Off.
Pursuit: Fast units only. Routing unit loses Strength equal to pursuer net
Offence successes (no Defence) each turn. Recall: Coherence Rating Ob 2.
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
turn qualifies as a non-Thread event of sufficient severity — Game Master may rule
the Woven configuration shatters into a Shifting Object. A Woven unit can be
simultaneously more and less resilient than an unworked unit. *[EDGE-07]*

> **Clarification:** "A Woven unit configuration that shatters (Str loss in a single turn > current Cohesion) does not become a Shifting Object during the battle. For the remainder of the battle, it fights at Line formation, Cohesion 1. The Shifting Object status is registered for post-battle Thread consequences — the Game Master tracks this and applies it in the narrative aftermath. This prevents mid-battle stat volatility while preserving the Thread consequence."

**Thread Tension references in stage5_clocks.md:** Compilation error — all Thread Tension references
must be converted to Rendering Stability with inversion (Thread Tension +N → Rendering Stability −N). *[EDGE-06 — P1,
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

| BG Unit | Martial | Endur | Cohesion | Health | TTRPG CP | TTRPG Str [PROV] | TTRPG Morale [PROV] | TTRPG Weapon | TTRPG Armour | Dmg Mod [PROV] |
|---|---|---|---|---|---|---|---|---|---|---|
| Levy | 1 | 1 | 1 | 7 | 1 | 3 | 2 | LightCut | None | +1 |
| Light Infantry | 3 | 3 | 3 | 9 | 3 | 4 | 4 | LightCut | Light | +2 |
| Heavy Infantry | 4 | 4 | 4 | 10 | 4 | 5 | 5 | HeavyCut | Medium | +4 |
| Cavalry | 4 | 3 | 5 | 9 | 5 | 4 | 5 | HeavyCut | Heavy | +5 |
| Ranged | 3 | 2 | 3 | 8 | 3 | 3 | 3 | LP (arrows) | Light | +2 |
| Artillery | 2 | 2 | 2 | 8 | 2 | 3 | 3 | HBl (siege) | None | +3 |
| Knights Templar | 5 | 5 | 6 | 11 | 5 | 6 | 6 | HeavyBlunt | Heavy | +5 |

Str corrected: user audit −2 all units, −3 Ranged and Artillery (PP-104).
Dmg Mod: used in Phase 5 damage formula (max(0, net hits + Dmg Mod − DR) = Str loss). [EDITORIAL: ED-062]
Ranged weapon: LP (arrows) default — see ED-061 for sub-type split (archer/crossbow/slinger).
Artillery weapon: HBl (siege) — Volley keyword, no melee.
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
Commander bonus = faction Military ÷ 3, round down (min 0, max +2D).
[EDITORIAL: confirm commander bonus formula] TN 7. Ob from table.
Net successes = damage dealt to opposing units.

**Step 4 — Determine outcome by margin (PP-104):**

| Margin | Outcome | Effect |
|--------|---------|--------|
| Attacker net ≥ Defender net + 2 | Attacker wins | Territory captured; Defender Military −1 |
| Margin ≤ 1 either direction | Partial | No territory change; Attacker Stability −1 (commitment cost) |
| Defender net ≥ Attacker net + 2 | Defender wins | No territory change; Attacker Military −1 |

Partial reflects a costly inconclusive engagement — forces committed, ground unchanged.
[PROVISIONAL — ED-063: confirm Partial threshold and Stability cost]

**Step 5 — Apply damage.** Reduce Health per Step 3 net successes × unit damage modifier − DR.
Formation Break at Health 0.

**Step 6 — Morale.** Formation Break → Cohesion check Ob 2 → Route on fail.

**Thread in BG battles:** handled by Co-Movement cards per existing rules.
At Rendering Stability < 20: T-03 fires — both sides draw 1 Co-Movement card per battle.
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

**No Player Character in battle:** BG resolution fires. Territory control applies. Faction
stat consequences (Military, Stability) apply at Accounting. Rendering Stability changes from
any Thread orders apply at Accounting.

**Zoom In — Phase-Lock Protocol (PP-103):**
Zoom In may only fire at one of three legal phase-lock points:
- **After Phase 1** (orders placed, nothing resolved — cleanest entry)
- **After Phase 3** (manoeuvre complete, pre-Engagement)
- **After Phase 6 Step 1** (all damage applied, no ghost units)

If a Zoom In trigger occurs mid-phase (e.g., during Phase 5 Engagement), it
is held and fires at the end of the current phase — not immediately. This
eliminates mid-phase ghost-unit state (ED-057) and ensures the TTRPG scene
always opens with a clean, fully-resolved BG state.

**BG → TTRPG unit conversion:** Translate BG unit tokens using §B.2. The table
provides TTRPG CP, Str (provisional), Morale (provisional), weapon, and armour
for each unit type. See the Zoom In/Out Reference Card (designs/gm_ref_cp14/)
for the one-page summary.

**Player Character faction leader present in contested territory:** BG resolution defers to
TTRPG mass battle rules for that engagement. The Player Character's Coherence Rating and tactical decisions
play out in full. BG territory and stat consequences still apply at resolution.
Clock changes still batch to Accounting.

**Stat translation (TTRPG ↔ BG):**
- TTRPG unit Strength → BG unit Health (Str × 1.5, round up — Health scale
  is 8–11, Str is 1–7; Str 4 ≈ Health 9)
- TTRPG general Coherence Rating → BG commander bonus (Coherence Rating ÷ 2, round down)
- TTRPG Cohesion → BG Cohesion (direct, same scale)
- TTRPG Morale (rout) → BG Cohesion check (rout equivalent)

---

## PART C: OPEN EDITORIAL ITEMS

All items below require user approval before compilation.

| ID | Item | Proposed resolution |
|---|---|---|
| Coherence Rating-EDIT-01 | Military stat → unit CP/Cohesion ceiling (§A.4) | Table above — confirm |
| Coherence Rating-EDIT-02 | Battle outcome → faction stat consequences (§A.13) | −1 Military/unit destroyed; Stability checks as above |
| Coherence Rating-EDIT-03 | Muster → unit stats (§A.13) | Str=2, CP = Military÷2 |
| BG-EDIT-01 | Commander bonus formula (§B.3) | Military ÷ 3, round down |
| BG-EDIT-02 | Faction-specific tactic cards (§B.4) | 8 faction cards above |
| CLOCK-EDIT-01 | Institutional Pressure 75+ Altonian invasion unit stats | See simulation report |
| CLOCK-EDIT-02 | Church military victory → Theocracy Counter change | No Theocracy Counter change from military victory alone (confirm) |