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
## Source checkpoint: compilation/v0.14/stage8_combat_deprecated.md (for reference values)

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

****THIS DOESN'T MAKE SENSE RE PRIORITY. IT'S ALL SIMULTANEOUS****
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

[ED-129 RESOLVED: Ranged weapons are a distinct weapon category, not integrated into the 3-axis melee matrix. Rationale: ranged weapons do not share the Reach (Short/Long) or Weight (Light/Heavy) characteristics that define melee combat profiles. A bow is neither Short nor Long in the melee sense; a crossbow has no meaningful Reach axis. The 3-axis matrix applies to melee only. Ranged weapons use the dedicated table below. For Godot implementation: melee and ranged are separate weapon-type enums with independent TN lookups.]

### Ranged Weapons (distinct category — ED-129 resolved)

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

### Wounds (ED-548 correction, 2026-04-16)

**Wound Interval = Endurance + 6** (range 7–13). Damage accumulates against the current wound's interval. At Wound Interval damage: take one Wound, damage counter resets to zero, continue accumulating toward the next Wound. (PP-210, structural correction applied)

**Max Wounds = floor(Endurance ÷ 2) + 1** (PP-263)

| Endurance | Wound Interval | Max Wounds | Total Damage Capacity = WI × (MW + 1) |
|-----------|----------------|------------|---------------------------------------|
| 1 | 7 | 1 | 14 |
| 2–3 | 8–9 | 2 | 24–27 |
| 4–5 | 10–11 | 3 | 40–44 |
| 6–7 | 12–13 | 4 | 60–65 |

Total damage capacity before incapacitation = Wound Interval × (Max Wounds + 1). The final Wound Interval (the one after the maximum number of Wounds) is the incapacitation threshold — filling it is what pushes the character past Max Wounds. At Max Wounds + 1 Wound accrued: incapacitated. No staged incapacitation states. (PP-232, ED-130 resolved; ED-548 corrects prior formula.)

Each Wound: −1D Combat Pool only (cumulative). No Ob penalty from wounds. (PP-232, replaces PP-165)

**Design note:** the prior formulation ("Health = Endurance + 6, resets to full on Wound") produced a cliff effect — Wounds always appeared at the same perceived threshold, and the Combat Pool penalty stacked at a uniform rate regardless of the character's actual resilience. The corrected formulation scales total capacity with both Endurance (via Wound Interval) and Max Wounds (via the multiplier), producing a smooth curve. A high-Endurance character absorbs more total damage AND accrues Wounds more slowly. The −1D per Wound penalty now reflects a genuine resource depletion, not a ticking clock to inevitable incapacitation.

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

**Canonical mass battle melee damage: mass_battle_v30 §A.7 Phase 5.** The formula below (PP-086) applies to personal-scale mass combat abstraction only (when the engine resolves a skirmish without entering full mass battle). For full mass battle engagement damage, use:

> Damage = max(0, net hits + weapon modifier − DR)

where net hits = Offence successes − Defence successes, weapon modifier per §A.2, DR per unit armour tier. Critical hit (net hits ≥ 3): weapon modifier doubled. (ED-578 resolution)

**Personal-scale mass combat abstraction (PP-086, retained for hybrid/simplified resolution):**
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
See compilation/v0.14/stage11_scale_transitions_deprecated.md §11.8.

---

## 10. THREAD IN COMBAT

Combat is thread-configurations in violent restructuring (Foundations A1). A wound is a thread disruption at the actualized dimension. Death is a configuration ceasing to cohere. The body's damage impedes substrate-level work (+1 Ob per Wound to all Thread operations — threadwork_v30 §2.3). These are not metaphors; per A1, everything is constituted from threads.

**Full Thread operation rules:** designs/ttrpg/threadwork_v30.md.

### 10.1 Practitioner Interface

- **Leap round:** Practitioner commits all pool to Defence during Leap. ~60% hit probability from any opponent who can attack. Real tactical cost.
- **Coherent Strike (W-24):** Viable only with range protection during Leap.
- **Rally the Broken (W-33):** Effective only for CP ≥ 3 units.
- **Wound penalties:** +1 Ob per Wound to all Thread operations (threadwork_v30 §2.3).
- **Mass battle:** Coherence −1 per Thread operation. See mass_battle_v30 §A.10.

### 10.2 Thread Perception in Combat

Practitioners and TS-sensitive observers perceive combat events through the Thread. Per threadwork_v30 §2.3 visibility table (extended by ED-677):

| Observer TS | Combat Wound | Death |
|---|---|---|
| 0–9 | Normal perception | Normal grief |
| 10–29 | Vague unease at violence | Sense of loss beyond normal grief |
| 30–49 | Perceives thread disruption at wound site | Perceives configuration ceasing to cohere |
| 50+ | Identifies structural depth of wound | Perceives full thread-state dissolution |

This perception provides investigative information (fieldwork_v30 §2.4) and feeds Confrontation Development (Foundations A10).

### 10.3 Cross-System Fire from Combat

| Combat Event | Consequence | System |
|---|---|---|
| Killing named NPC | Knot rupture + Conviction Scar on witnesses | §13.3 Death Cascade; npc_behavior_v30 §3.4 |
| Practitioner Dissolution in combat | RS cost + Scar on all witnesses with engaged Conviction | threadwork_v30 §5.2; npc_behavior_v30 §3.4 |
| Practitioner Dissolution witnessed by companion | Companion Thread violation departure if Faith/Order/Equity Conviction | companion_specification_v30 §6.1 |
| Thread operation witnessed by adjudicator in formal proceeding | Certainty-indexed adjudicator response | social_contest_v30 §9.4b |

**Board Game:** Thread operations abstracted to Co-Movement cards and faction Thread orders. See threadwork_v30 §7.1.

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


**Combat → Fieldwork (Fled/Retreated) (ED-576):**
- If the player fled or retreated from combat, no post-combat fieldwork scene is available at the battle site. The player forfeited scene control by leaving.
- The battle site becomes a standard POI (fieldwork §3.1) discoverable in a future season. Evidence degrades: +1 Ob to investigation per season elapsed since the battle.
- Fleeing combat does NOT reset the player's fieldwork state — any active investigation or social engagement in the territory continues from where it was when combat interrupted.
- Exposure from the fled combat still applies per F-TRANS-01/09 (quiet +1, conspicuous +2, public +3). Flight does not reduce Exposure — witnesses saw the player arrive, even if they left.

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

---

## 13. COMBAT WORLD BRIDGE (NEW)

### §13.1 Combat Domain Echo

Combat against named NPCs who hold faction office (officer, cardinal, commander, agent, faction leader) fires Domain Echo per scale_transitions_v30 §7 condition 5. The combat IS an institutional event — violence against a faction representative challenges that faction's authority.

| Combat Outcome | Domain Echo |
|---------------|-------------|
| Player defeats faction officer (incapacitation or surrender) | Acting faction: relevant stat +1. Target faction: Stability −1. |
| Player kills faction officer | Acting faction: relevant stat +1. Target faction: Stability −1, Mandate −1. |
| Player is defeated by faction officer | Target faction: Mandate +1 (authority demonstrated). Player's faction: no stat change (the defeat is personal). |
| Player kills faction leader | All consequences of officer death above. Additionally: faction enters Succession per npc_behavior_v30 §5.2 arc profiles. |

**Combat Domain Echo fires at scene end**, not mid-combat. If the player initiates combat with a faction officer, they should know that the consequences will propagate.

### §13.2 Combat Reputation Cascade

Public combat accumulates a Combat Reputation that modifies NPC behavior toward the player.

**Combat Reputation Sources:**
- Public combat victory (3+ witnesses): +1 Combat Reputation
- Killing a named NPC in combat: +1 Combat Reputation
- Overwhelming victory: +1 additional Combat Reputation
- Public combat defeat: −1 Combat Reputation (minimum 0)

**Combat Reputation Effects:**

| Reputation | Effect |
|-----------|--------|
| 0–1 | No effect. The player is not known as a combatant. |
| 2–3 | NPCs at Disposition ≤ 0 are less likely to initiate combat (NPC evaluates: is this fight worth it?). +1 Ob to Intimidate equivalent (Impress with hostile intent). |
| 4–5 | NPCs at Disposition ≤ −2 avoid direct confrontation (prefer ambush, institutional action, or proxy violence). Church Attention Pool +1 in territories where combat occurred (violence draws institutional notice). |
| 6+ | The player is feared. All first-meeting NPC Dispositions shift −1 (fear, not respect). Faction leaders evaluate the player as a military threat at Priority 6 (Reactive) of their trees. |

Combat Reputation decays: −1 per year of no public combat.

### §13.1b Economic Actions in Settlements (Throughline T2)

Player Resources (0–5) interact with combat context: loot from combat (+1 Resources per valuable recovered). Equipment purchases (1 Resource) follow existing weapon/armor lists. Military equipment upgrades (3 Resources) provide +1 effective Power to one unit for one battle. Full Resources specification: player_agency_v30 §9. Trade action (Cognition + History, Port/City settlements): player_agency_v30 §9.

### §13.2b Settlement-Level Combat Consequences (NEW — per settlement_bridge_unification C-07)

Combat in a settlement produces settlement-level consequences on top of province-level effects:

| Combat Context | Settlement Effect |
|---------------|------------------|
| Public combat in a settlement (3+ witnesses) | Order −1 in that settlement |
| Combat against the settlement's governor | Order −2 in that settlement |
| Killing a named NPC who resides in the settlement | All NPC Dispositions in that settlement toward the killer: −2 |

These effects are immediate and stack with existing Domain Echo and reputation effects from §13.1 and §13.2.

**Garrison Strength feedback (derived_stats_v1 §8.4):** When the player personally defends a settlement, combat outcome modifies Garrison Strength: victory +10, Overwhelming victory +20 + Public Order +5, defeat −10, settlement falls → Garrison Strength 0 + Defense stat check Ob 2. This cascade (personal combat → settlement derived value → faction income) is the most direct personal→faction feedback loop.

### §13.3 Death Cascade

Killing a named NPC in combat triggers the following cascade:

1. **Immediate:** All NPCs Knotted to the dead NPC suffer Knot rupture (per threadwork_v30 Knot strain rules). Rupture produces: Disposition toward the killer −3, Conviction Scar if the dead NPC was central to the Knotted NPC's active Conviction.
2. **Scene Slate:** All NPCs with Disposition ≥ +2 toward the dead NPC receive a Priority 1 Scene Slate entry next season — their grief, their response, their reckoning. These are the people who will remember what the player did.
3. **Faction:** If the dead NPC was a faction officer: Stability trigger per faction_layer_v30 §1.2. If faction leader: Succession fires per npc_behavior_v30 §5.2.
4. **Exposure:** Killing a named NPC in combat generates Exposure per §11.5 (quiet +1, conspicuous +2, public +3). Additionally: +2 Exposure in every territory where the dead NPC had Disposition ≥ +2 with local NPCs (the news spreads through the dead NPC's relational network).
5. **Player Conviction test:** If the player has an active Conviction that the dead NPC was relevant to (e.g., "I will protect Torben" and Torben is killed), the Conviction is immediately strained. If the killing was the player's action: the player must revise the Conviction (the goal has failed or transformed). If the killing was another NPC's action: the player may keep the Conviction but it transforms — "I will protect Torben" becomes "I will avenge Torben" or "I will ensure Torben's death was not meaningless."
