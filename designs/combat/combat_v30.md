<!-- SKELETON — mechanical spec only — atomized 2026-04-13 from designs/combat/combat_v30.md -->
<!-- Infill: designs/combat/combat_v30_infill.md -->
<!-- DO NOT add prose. Rationale/examples live in the infill file. -->

<!-- v30 baseline — renamed from designs/combat/combat_design_v1.md on 2026-04-13 -->
# VALORIA — COMBAT DESIGN (v1)
## Date: 2026-04-02
## Version: v1.6 (PP-238, PP-239, PP-247 applied; PP-232: weapon system rebuild, wound penalty, initiative, Health/Stamina, Stage 1/2 struck; PP-210–218: audit gap fixes — Health formula, Critical Hit, Feint timing, Tie Up, Rescue, Dodge, Fibonacci, Anti-Armour, PP-086)
## Status: WORKING DESIGN — not compiled. This is the design-layer source for personal combat.
## Authority: Philosophical Foundations → this document → compilation (when ready)
## Mode applicability: ALL (TTRPG baseline; scales to Hybrid and Board Game via params)
## Patches incorporated: PP-086–092, P2-B11 series (from sim_combat_batch_11.md), PP-172 (SIM-001 ranged subtypes), PP-210–218 (audit gap fixes 2026-04-03)
## Source checkpoint: compilation/v0.14/stage8_combat.md (for reference values)

---

## THREE-MODE FRAMING

All combat mechanics are stated as TTRPG baselines.
Translation rules for each scale are noted inline.

| TTRPG | Hybrid | Board Game |
|-------|--------|------------|
| Full personal combat (pool split, wound tracking, stamina) | Personal combat for named characters; mass combat abstraction for units | Unit-based abstraction (Martial/Cohesion/Morale); no individual tracking |
| Zone-based (no maps or grids) | Zone-based for personal scenes; operational zones for mass combat | Territory-adjacency map; zone-based mass combat within territory |
| All 10 attributes active | Player Character attributes active; Non-Player Character stats simplified | Faction stats (Military, Wealth, etc.); no personal attributes |


---

## 1. COMBAT POOL

**TTRPG:**
Combat Pool = (Agility × 2) + Relevant History + 3 (minimum 5)


Modifiers:
- Wounds: −1D per wound (cumulative)
- Fibonacci group bonus: +dice to Offence allocation only (see §8)
- Stamina Out of Breath: −2D to all rolls until recovery action taken


**Hybrid:** Player Character uses full TTRPG pool. Non-Player Character units use Martial stat.

---

## 2. ROUND STRUCTURE

Phase-based. Priority list within each phase:
1. Movement declarations
2. Range establishment (reach priority — see §5)
3. Action declarations (simultaneous, blind)
4. Resolution (per priority order within declared actions)
5. Damage application (simultaneous where relevant)
6. Stamina/wound tracking

Round duration: 6–10 seconds narrative.

**Board Game:** Single roll per engagement per turn. No phase structure.

---

## 3. INITIATIVE (PP-232)


**Subsequent rounds:** Initiative transfers to the exchange winner.
**Tie result:** No damage to either side; initiative stays with current holder.

**Declaration order each round:**
1. Lower initiative holder declares Offence/Defence split first.
2. Higher initiative holder sees that split, then declares their own.


---

## 4. ACTIONS

**Combat action priority order (PP-247):** Lower number = resolves first within a round.

| Priority | Action |
|----------|--------|
| 1 | Strike |
| 2 | Feint |
| 3 | Disarm, Tie Up, Retrieve |
| 4 | Establish Distance, Escape |
| 5 | Leap (Thread — full-round) |
| — | Full Guard, Take a Breath, Dodge, Rescue (reactive; trigger-timed) |


| Action | Description |
|--------|-------------|
| Strike | Allocate pool split, roll, apply damage |
| Feint | Player chooses commit: allocate N dice (minimum 3) to Offence for the feint; remaining dice available for Defence this round. **Versus roll (PP-294):** roll N dice (TN 7) vs opponent's Defence pool (TN 7) — sequential per initiative, not fixed Ob. If A's net > B's net: B loses [margin] dice from total pool next round (affects both Offence and Defence allocation). Pool reduction floor: minimum 1D (PP-294). Payoff scales with margin — more commit increases both P(success) and expected reduction magnitude. **Non-stacking (PP-293):** successive Feints always reset pool reduction to current margin; effects do not accumulate. **Expires on incapacitation (PP-293):** pool reduction expires if Feinting actor cannot act in the reduction round. (PP-212, PP-238, PP-277, PP-291, PP-293, PP-294) |
| Establish Distance | Move to preferred range. Contested Agility if opponent opposes. |
| Take a Breath | No combat action. Recover Stamina by Endurance score. Cannot if in immediate melee contact. |
| Full Guard | All dice to Defence. Cannot Attack. |
| Disarm | Offence roll vs opponent's STR+Agility Ob. Success: weapon dropped. Requires Close range. |
| Retrieve | Pick up dropped weapon/item. Opposed Agility if in melee contact. |
| Tie Up | Close range. Offence roll. Success: both parties suffer −2D to Combat Pool for one round; opponent cannot use reach advantage; escape requires Strength contest. Blocks escape for one round. (PP-213) |
| Escape | Agility contest vs opponent. Requires not being Tied Up. |
| Rescue | **Exclusive action** — declare in Phase 1 before opponent's attack resolves. **Eligibility (PP-290):** rescued actor must be outnumbered at declaration (2+ attackers, no supporting ally). Ineligible Rescue fails silently — action lost. Requires adjacent zone. **Commit:** rescuer allocates N Offence dice to contest the redirect (minimum 1); remaining dice available for Defence against own engagement's attacker only. **Contest (PP-292):** rescuer rolls N dice (TN 7) vs attacker's Offence roll. If rescuer wins: attack redirects to rescuer — resolves against rescuer's armour DR only (contest dice are expended; no Defence dice available against the redirected attack). If rescuer loses: attack resolves against original target; rescuer's N dice wasted; remaining dice still defend own engagement. **On successful intercept (PP-292):** rescuer gains 2 Momentum (PP-406); rescued actor is exempt from Fibonacci group penalty and cannot be targeted by any other attacker this round. Exemptions expire at round end. **Rescue chain block (PP-290):** a character who declared Rescue this round cannot be the target of another Rescue. **Incapacitation before resolution (PP-290):** rescuer incapacitated at Priority 1 — Rescue fails, attack reverts to original target, Momentum not granted. (PP-214, PP-285, PP-286, PP-290, PP-292) |
| Dodge | Ranged attacks only. Forfeit all offensive action this round. Allocate full Combat Pool as passive Defence against one incoming ranged attack. Armour DR applies normally. (PP-215) |
| Stunt | Declared with Strike. +N dice to Offence from environmental/positional narrative (Game Master sets N, max 5). Chain dice (10s) chain normally, independent of Stunt effect. |


**Incapacitation stages — personal combat (PP-269):**
- **Stage 1 (Incapacitated/Down):** Health reaches 0 at max Wounds. Character is unable to act. Can be stabilised with a Medicine roll (Ob 2) within the same scene. Stabilised characters survive but cannot participate further this scene. **Recovery (PP-284/ED-177):** Stabilised characters may return to action after one full scene of rest. Wounds clear at end of session (or after extended rest per GM). Stabilised characters retain all Wounds until rest.
- **Stage 2 (Dying):** If not stabilised by scene end, or if **any attack dealing at least 1 net hit lands on a downed Stage 1 character** (PP-284/ED-178): Stage 2. Downed characters cannot defend (Defence = 0); any landed strike is potentially finishing. Will die without intervention. Medicine Ob 3 within one scene; failure = death.

---

## 5. WEAPON SYSTEM

### Weapon TN Matrix (PP-232)

Weapons are defined by three binary axes. Base TN = 7. TN modifiers:

| Axis | Option A | Modifier | Option B | Modifier |
|------|----------|----------|----------|----------|
| Reach | Short | −1 | Long | +0 |
| Weight | Light | −1 | Heavy | +0 |
| Type | Blade | +0 | Blunt | +1 |

Final Hit TN = 7 + reach modifier + weight modifier + type modifier.

**STR minimums:** Each "Heavy" or "Long" axis adds +1 to minimum STR.
| Combination | Min STR |
|-------------|---------|
| Short Light (either type) | 1 |
| Short Heavy or Long Light | 2 |
| Long Heavy (either type) | 3 |
| Long Heavy Blunt | 4 |

Penalty if 1 below minimum: −1D Combat Pool. Cannot wield if 2+ below minimum.


| Combination | TN | Examples |
|-------------|-----|---------|
| Short Light Blade | 5 | Dagger, knife |
| Short Light Blunt | 6 | Sap, hand axe |
| Short Heavy Blade | 6 | Short sword, arming sword |
| Long Light Blade | 6 | Spear, light lance |
| Short Heavy Blunt | 7 | Club, mace (short) |
| Long Heavy Blade | 7 | Longsword, axe, glaive |
| Long Light Blunt | 7 | Staff, walking stick |
| Long Heavy Blunt | 8 | War hammer, pollaxe |
| Unarmed | 8 | Fists, grappling, improvised |

[EDITORIAL: ED-129 — Ranged weapon TN integration into this matrix pending.]

### Ranged Weapons (retained from prior system, pending ED-129)

| Weapon | TN | Notes |
|--------|-----|-------|
| LP — Light Piercing (bow) | 7 | Min STR 2 |
| HP — Heavy Piercing (crossbow) | 6 | Min STR 1; full-round Reload after each shot |
| Sling (all ammo) | 8 | Min STR varies by ammo |

Sling ammo modifier (vs medium and heavy armour only):
| Ammo | Dmg mod vs med/heavy |
|------|----------------------|
| Clay | +0 |
| Rock | +1 |
| Metal | +2 |
| Lead | +3 |

### Damage Resolution (PP-232)
Net hits = Offence successes − Defence successes (minimum 0).
Damage = net hits + STR + weapon modifier vs armour tier (see table below).
Critical Hit: net hits ≥ 3 → weapon modifier doubled before applying armour reduction. (PP-211)

STR is confirmed as a damage addition (PP-232).

**Weapon modifier vs armour tier:**
| Weapon Class | vs None | vs Light | vs Medium | vs Heavy |
|--------------|---------|----------|-----------|----------|
| Light Blade | +3 | +2 | +1 | +0 |
| Heavy Blade | +6 | +4 | +2 | +0 |
| Light Blunt | +3 | +3 | +3 | +3 |
| Heavy Blunt | +5 | +5 | +5 | +5 |

[EDITORIAL: ED-131 — Exact modifier values require playtesting confirmation.]

### Degree Table (for combat outcomes requiring degree, e.g. Feint, Disarm)
| Net Successes | Degree |
|---|---|
| 0 | Failure |
| 1 | Partial |
| 2 | Success |
| 3+ | Overwhelming |

No catastrophic outcome category. Majority-1s produces standard Failure.

### Reach Rules
**Zone terminology (PP-268):** Close zone renamed **Melee range**; Far zone renamed **Ranged distance** throughout. These plain-language terms replace 'Close' and 'Far' to align with the Short/Long weapon reach matrix.

- Ranged defence at Close zone: a character carrying a ranged weapon may defend at Def TN 8 if forced into Close zone by a melee attacker. The full pool is allocated to Defence; no Offence allocation is permitted. This represents using the weapon as a physical barrier or emergency grapple resist.

### Environmental Factors (Ranged Combat)

| Terrain | Rounds to close | Penalty to closer |
|---------|----------------|-------------------|
| Open ground | 1 round | None |
| Difficult (marsh, rubble, slope) | 2 rounds | +1 Ob to all movement-linked actions |
| Shallow river / ford | 2 rounds | +1 Ob, −2D to all combat rolls while crossing |
| Deep river | 3 rounds + Swim check (Ob 2) | Ob 2 to cross; failure = swept back |
| Wall or rampart | Climb action (TN 8 Ob 1) per obstacle | Action lost if climb fails |


| Cover | vs LP | vs HP | vs LBl | vs HBl |
|-------|-------|-------|--------|--------|
| Soft (trees, wagon, bale) | +2 DR | +1 DR | +2 DR | +2 DR |
| Hard (stone wall, fortification) | Blocks shot | Blocks shot | Blocks shot | Blocks shot |


**Board Game:** Weapon types map to BG unit type. No TN variation — units use Martial stat pool vs standard TN 7. Anti-Armour keyword (PP-217): units with HP (crossbow) or HBl (lead sling) weapon type carry the Anti-Armour keyword. When an Anti-Armour unit attacks, reduce target unit's effective armour tier by 1 for that engagement (e.g. Heavy → Medium DR applies). Does not stack from multiple attacking units.

---

## 6. ARMOUR

### Armour (PP-232)

| Armour | STR Min | Stamina Mod |
|--------|---------|-------------|
| None | — | +0 |
| Light | 2 | +0 |
| Medium | 3 | −1 |
| Heavy | 4 | −2 |

Cannot wear armour if it would reduce Stamina to 1 or below (PP-232).
Damage Reduction (DR) is subsumed into the weapon modifier vs armour tier table (see Damage Resolution above).

### Ranged DR
| Tier | DR vs LP (arrow) | DR vs HP (bolt) | DR vs LBl (stone) | DR vs HBl (lead) |
|------|-----------------|----------------|------------------|-----------------|
| None | 0 | 0 | 0 | 0 |
| Light | 2 | 1 | 1 | 0 |
| Medium | 3 | 2 | 2 | 1 |
| Heavy | 5 | 3 | 3 | 2 |


DR is subtracted from damage after net hits + weapon modifier.

---

## 7. WOUNDS AND STAMINA

### Wounds
Health = Endurance + 6 (range 7–13). Damage accumulates each round against Health. At 0 Health: take one Wound, Health resets to full. (PP-210)

**Max wounds formula: floor(Endurance ÷ 2) + 1** (PP-263)

| Endurance | Max Wounds before incapacitation |
|-----------|----------------------------------|
| 1 | 1 |
| 2–3 | 2 |
| 4–5 | 3 |
| 6–7 | 4 |

At max Wounds: incapacitated. Health track runs to 0 = incapacitated. No staged incapacitation states. (PP-232, ED-130 resolved)
Each Wound: −1D Combat Pool only (cumulative). No Ob penalty from wounds. (PP-232, replaces PP-165)

### Stamina
Stamina = Endurance + Relevant History + 1 − armour modifier. **Minimum 2. Maximum = base value (PP-275).** (PP-232) Take a Breath restores Endurance score, capped at base Stamina value. Cannot wear armour whose Stamina modifier would reduce Stamina to 1 or below. (PP-232)
Depletes by 1 per round of active combat.
At 0: Out of Breath. −2D to all combat rolls. Recovery: Take a Breath action.

**Hybrid:** Wound Ob penalties carry into TTRPG mass battle Command checks (PP-232) (see stage11 PP-089 and mass_battle_v3 §A.5). Do NOT reduce BG commander bonus.

---

## 8. GROUP COMBAT

### Zone Collapse
When 3+ combatants in a zone: combat becomes group combat. Fibonacci bonus applies.

### Fibonacci Group Bonus
Each additional attacker beyond the first against a single unsupported target adds dice to Offence allocation. (PP-216)

| Attackers | Bonus Offence Dice |
|-----------|-------------------|
| 1 | +0 |
| 2 | +1 |
| 3 | +2 |
| 4–5 | +3 |
| 6–7 | +4 |
| 8+ | +5 (cap) |


### Rescue

**Eligibility (PP-290):** Rescue may only be declared if the rescued actor is outnumbered at Phase 1 declaration — facing 2+ attackers with no supporting ally (subject to Fibonacci bonus this round). Assessed at declaration only; mid-round incapacitations do not retroactively qualify. Ineligible Rescue fails silently — action lost.


**Commit and contest (PP-292):** Rescuer allocates N Offence dice (minimum 1) to contest the redirect. Remaining dice (pool − N) are available for Defence against the rescuer's own engagement's attacker only.

Rescuer rolls N dice (TN 7) vs the target attacker's Offence roll (contested):

**Weapon speed note:** Attacker TN affects contest difficulty. Light/fast weapons (TN 5–6) roll more net successes on average — harder to intercept. Heavy weapons (TN 7–8) are slower and easier to redirect. Rescuers should commit more dice against fast attackers.

**Rescue payoffs (PP-292, PP-295, PP-406, PP-407):**

Rescued actor exemptions expire at round end.

**Rescue chain block (PP-290):** A character who has declared Rescue this round cannot themselves be the target of another Rescue declaration.


### Multi-Engagement (3v2, 4v3)

**Multi-engagement pool split (PP-274):** A target facing multiple attackers in separate pairings declares one Offence/Defence split for the round. All attackers roll against the same Defence allocation independently. The target cannot declare a different split against each attacker. This forces the target to choose a single defensive posture, accepting vulnerability to one attacker while defending against another.

**P2-B11-08:** If two parties rout simultaneously in a three-way engagement, the surviving party wins and receives veteran bonus.

---

## 9. MASS COMBAT (TTRPG SCALE)

*For full mass combat rules, see designs/mass_combat/mass_battle_v3.md.*
*This section provides the interface between personal and unit scales.*

### Unit Stat Block (1–7 unless noted)
- **Strength:** Headcount/health pool. At 0: destroyed.
- **Combat Power (CP):** Dice pool ceiling.
- **Cohesion:** Organisational integrity.
- **Morale:** Rout threshold.
- **Speed:** Slow / Standard / Fast.
- **Weapon Type:** Inherits personal combat TN table (above).
- **Armour Tier:** Inherits DR table (above).


### PP-086 — Base Damage Formula (mass combat)
Damage = max(0, net successes − Ob) + disposition_modifier. (PP-218 clarification)
"Net successes − Ob" = total net successes minus the Obstacle value. Floor of 0 applies to the bracketed term before adding disposition modifier. Partial success (0 < net < Ob) → bracket is negative → floored to 0; disposition modifier still adds. Example: net 1, Ob 2, Offensive (+2) → max(0, 1−2)+2 = 0+2 = 2 damage.
Disposition modifiers: Offensive +2 flat; Defensive +4 flat.

### PP-087 — Formation Break Ob Stacking
+1 Ob per break. Cumulative. Persists through rally. Cap: 3 breaks = Dispersed (permanent rout).
All attachments lost on any Formation Break.

### PP-088 — Siege Assault Linkage
Mass combat win during declared Assault = Fortification −1. Overwhelming = −2.
Field victory alone does not breach — must declare Assault next season.

### PP-091 — Artillery Bombard
Roll Artillery CP vs Ob (Short=1, Med=2, Long=3). No melee exchange. Success = flat 1 Str damage. Overwhelming = flat 2. Cannot Bombard at melee range.

### PP-089/PP-090 — Hybrid Phase Order and Mode-Switch
See compilation/v0.14/stage11_scale_transitions.md §11.8.

---

## 10. THREAD IN COMBAT

See designs/ttrpg/threadwork_redesign_v25.md for full Thread operation rules.

**Key interface points:**
- Leap round: practitioner commits all pool to Defence during Leap. ~60% hit probability from any opponent who can attack. Real tactical cost.
- W-24 (Coherent Strike): viable only with range protection during Leap.
- W-33 (Rally the Broken): effective only for CP ≥ 3 units.
- Coherence −1 per Thread operation in mass battle. See ST-TW-03.

**Board Game:** Thread operations abstracted to Co-Movement cards and faction Thread orders. See bg_v05_simulation_and_patches.md §7 and threadwork_redesign_v25.md §7.1.

---

## 11. FACTION UNIT ROSTERS (from MT-01, 2026-03-30)

Default unit stats (board game / mass combat):
- Standard unit: Martial 2, Cohesion 3
- Elite unit: Martial 3–4, Cohesion 4–5

| Faction | Military | Starting Units | Notes |
|---------|---------|---------------|-------|
| Crown | 4 | 4 | Mixed infantry + cavalry. Standard formation. |
| Church | 4 | 4 | 2 Templar (elite: Cohesion 5, Martial 4) + 2 garrison (Cohesion 3, Martial 2). Templars deploy free at Theocracy Counter ≥ 40 in Himmelstift. |
| Hafenmark | 3 | 3 | 1 ducal guard (elite: Cohesion 4, Martial 3) + 2 militia. |
| Varfell | 4 | 4 | Highland infantry. Cohesion 4. Home territory bonus: +1D in Eisengrund. |
| Guilds | 2 | 2 | Hired mercenaries. Cohesion 3, Martial 2. High Wealth allows rapid replacement. |
| Niflhel | 0 | 0 | No standing units. Cannot hold territory by force. |
| Revolution | 0 | 0 | No standing units. Community defence possible via Community Weaving. |
| Löwenritter | 5 (→6 post-coup) | 5 (→6) | All units elite: Cohesion 5, Martial 4. +1 unit from Crown transfer post-coup. |


**Mustering:** Muster order raises 1 new unit per success (up to Military cap) at standard stats.



---

## 11.5 FIELDWORK TRANSITIONS


**Fieldwork → Combat (F-TRANS-01/09):**
- Combat Exposure codified: quiet engagement +1, conspicuous +2, public +3 Exposure to the fieldwork-active character. Applied before the combat scene opens, not during it.
- Reference: fieldwork_exploration.md §3.2, fieldwork_investigation.md §2.3.

**Combat → Fieldwork (F-TRANS-12):**
- Post-combat investigation of battle site = 1 fieldwork scene. The battle itself does not consume fieldwork time; only the post-combat investigation does.
- Evidence of battle events (attacker identity, force composition, timing) follows standard Evidence Track rules.

**Let It Ride in combat (clarification):**
Standard attack actions are NOT subject to Let It Ride — re-attempting the same attack against the same opponent each round is the core mechanic (round structure handles iteration through pool depletion and Stamina). Let It Ride DOES apply to declared manoeuvres (Feint, Rescue, Disarm, Tie Up): each may only be declared once per round. PP-293 (Feint non-stacking) is the operative implementation. A failed manoeuvre cannot be re-declared in the same round; circumstances must change between rounds.

## 12. DESIGN NOTES AND OPEN ITEMS

### From sim_x_06 (confirmed working)
- Wound degradation (−1D system): smooth curve, no single-wound cliff. ✓
- Range control: more fight-determining than pool size or wounds. Intended. ✓
- Combat Endurance accumulation (Inquisitor): slow multi-session trajectory. ✓

### From sim_combat_batch_11 P2 series (all clarifications, see §4 and §9)
All P2-B11 clarifications incorporated above.

### Pending editorial
- ED-033: Commander bonus formula conflict (three formulas).
- ED-040: Artillery Balanced disposition lock — intentional?
- [EDITORIAL: P2-B11-19 Thread Tension 80+ effect in mass battle — define or confirm no effect]