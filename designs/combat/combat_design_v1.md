# VALORIA — COMBAT DESIGN (v1)
## Date: 2026-04-02
## Version: v1.3 (ED-098: cover declaration timing clarification)
## Status: WORKING DESIGN — not compiled. This is the design-layer source for personal combat.
## Authority: Philosophical Foundations → this document → compilation (when ready)
## Mode applicability: ALL (TTRPG baseline; scales to Hybrid and Board Game via params)
## Patches incorporated: PP-086–092, P2-B11 series (from sim_combat_batch_11.md), PP-172 (SIM-001 ranged subtypes)
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

TTRPG is always the most granular layer. Hybrid uses TTRPG rules when a named Player Character is present. Board Game uses abstracted equivalents.

---

## 1. COMBAT POOL

**TTRPG:**
Combat Pool = (Agility × 2) + Relevant History + 3 (minimum 5)

Pool split: allocate between Offence and Defence before any dice are revealed. This split IS the action economy — no separate action declaration needed.

Modifiers:
- Wounds: −1D per wound (cumulative)
- Fibonacci group bonus: +dice to Offence allocation only (see §8)
- Stamina Out of Breath: −2D to all rolls until recovery action taken

**Board Game equivalent:** Unit Martial stat replaces Combat Pool. No split — Martial dice used for both attack and defence (abstracted).

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

## 3. INITIATIVE

Structural initiative from range:
- Long weapon at Far zone: has priority over Short weapon at Far zone
- Short weapon at Close zone: has priority over Long weapon at Close zone
- Equal range: Agility contest (Ob 1, TN 7) to determine first mover

Initiative transfers on: hit (attacker maintains), feint success, distance change (new range = new priority structure).

**P2-B11-02 clarification:** "Same range" occurs when shorter weapon closes to their optimal zone. Shorter weapon then has priority. Longer weapon user must manoeuvre at disadvantage to re-establish distance.

---

## 4. ACTIONS

| Action | Description |
|--------|-------------|
| Strike | Allocate pool split, roll, apply damage |
| Feint | Offence-only roll vs opponent Ob 2. Success: opponent loses −2D Defence next exchange. |
| Establish Distance | Move to preferred range. Contested Agility if opponent opposes. |
| Take a Breath | No combat action. Recover Stamina by Endurance score. Cannot if in immediate melee contact. |
| Full Guard | All dice to Defence. Cannot Attack. |
| Disarm | Offence roll vs opponent's Strength+Agility Ob. Success: weapon dropped. Requires Close range. |
| Retrieve | Pick up dropped weapon/item. Opposed Agility if in melee contact. |
| Tie Up | Close range. Offence roll. Success: both parties at disadvantage next round; opponent cannot use reach advantage; escape requires Strength contest. Blocks escape for one round. |
| Escape | Agility contest vs opponent. Requires not being Tied Up. |
| Rescue | Declare before opponent's attack resolves. Interpose. Requires adjacent zone. Fails if no incoming attack declared — action lost. |
| Stunt | Declared with Strike. +N dice to Offence from environmental/positional narrative (Game Master sets N, max 5). Chain dice (10s) chain normally, independent of Stunt effect. |

**Incapacitation timing:** Complete currently-resolving action. Fall at end of that priority step. Later-declared actions do not resolve.

---

## 5. WEAPON SYSTEM

### TN Table (d10, TN = minimum to count as success)

| Type | Hit TN | Def TN | Dmg Modifier | Reach |
|------|--------|--------|-------------|-------|
| Light Cut | 5 | 6 | +1 | Short or Long |
| Heavy Cut | 6 | 7 | +4 | Long |
| Light Blunt | 6 | 7 | +1 | Short |
| Heavy Blunt | 7 | 8 | +4 | Short or Long |
| LP — Light Piercing (arrow) | 6 | 8† | +2 | Projectile only |
| HP — Heavy Piercing (bolt) | 5 | 8† | +4 | Projectile only |
| LBl — Light Blunt ranged (clay/stone sling) | 7 | 8† | +1 | Projectile only |
| HBl — Heavy Blunt ranged (lead/metal sling) | 8 | 8† | +3 | Projectile only |
| Versatile (Light) | 5 | 6 | +1 | Short or Long (choose per round) |
| Versatile (Medium) | 6 | 7 | +2 | Short or Long |
| Versatile (Heavy) | 7 | 8 | +4 | Short or Long |

†Def TN 8 applies only when inside attacker's melee range (Close zone). Cannot split pool for Offence when using ranged weapon defensively at melee range.

### Damage Resolution
Net hits = Offence successes − Defence successes (minimum 0).
Damage = max(0, net hits + weapon damage modifier − DR).

### Degree Table (for combat outcomes requiring degree, e.g. Feint, Disarm)
| Net Successes | Degree |
|---|---|
| 0 | Failure |
| 1 | Partial |
| 2 | Success |
| 3+ | Overwhelming |

No catastrophic outcome category. Majority-1s produces standard Failure.

### Reach Rules
- Short vs Long at Short range: Short weapon has priority. Long weapon user must manoeuvre at disadvantage to re-establish Long range.
- Long vs Short at Long range: Long weapon has priority. Short weapon user must close at disadvantage.
- Ranged weapons (LP/HP/LBl/HBl): require Far zone to attack. At Close zone, ranged weapons cannot make an Offence roll. Melee weapons cannot retaliate against a ranged attack from Far zone.
- Ranged defence at Close zone: a character carrying a ranged weapon may defend at Def TN 8 if forced into Close zone by a melee attacker. The full pool is allocated to Defence; no Offence allocation is permitted. This represents using the weapon as a physical barrier or emergency grapple resist.
- Sling at Close zone: LBl and HBl slingers who are forced to Close zone are assumed to carry a melee weapon (typically a knife, Light Cut). May draw it as a Retrieve Weapon action.
- HP crossbow reload: after firing, HP user must take a full-round Reload action before firing again. No other action may be taken during Reload.
- Ranged vs closing melee: closing character must take a Move action each round. While closing, they are exposed to ranged fire and cannot allocate dice to Defence against it.

### Environmental Factors (Ranged Combat)
Melee users must close to reach a ranged attacker. Terrain affects the number of rounds of exposure and imposes penalties.

| Terrain | Rounds to close | Penalty to closer |
|---------|----------------|-------------------|
| Open ground | 1 round | None |
| Difficult (marsh, rubble, slope) | 2 rounds | +1 Ob to all movement-linked actions |
| Shallow river / ford | 2 rounds | +1 Ob, −2D to all combat rolls while crossing |
| Deep river | 3 rounds + Swim check (Ob 2) | Ob 2 to cross; failure = swept back |
| Wall or rampart | Climb action (TN 8 Ob 1) per obstacle | Action lost if climb fails |

Cover (a physical obstacle between attacker and defender) adds DR to the defender:

| Cover | vs LP | vs HP | vs LBl | vs HBl |
|-------|-------|-------|--------|--------|
| Soft (trees, wagon, bale) | +2 DR | +1 DR | +2 DR | +2 DR |
| Hard (stone wall, fortification) | Blocks shot | Blocks shot | Blocks shot | Blocks shot |

Cover must be declared in Phase 1 (Movement) to take effect. Cover does not move with the defender. The Game Master determines whether a physical obstacle is present in the zone. A character who does not declare Cover in Phase 1 receives no DR benefit that round, even if physically behind an obstacle. [PROVISIONAL — ED-098]

**Board Game:** Weapon types map to BG Anti-Armour keyword and unit type. No TN variation — unit uses Martial stat pool vs standard TN 7.

---

## 6. ARMOUR

### Melee DR
| Tier | DR vs Light Cut | DR vs Heavy Cut | DR vs Light Blunt | DR vs Heavy Blunt | Stamina modifier |
|------|----------------|----------------|------------------|------------------|-----------------|
| None | 0 | 0 | 0 | 0 | +0 |
| Light | 2 | 1 | 1 | 0 | −0 |
| Medium | 4 | 3 | 2 | 1 | −1 |
| Heavy | 6 | 5 | 3 | 1 | −2 |

### Ranged DR
| Tier | DR vs LP (arrow) | DR vs HP (bolt) | DR vs LBl (stone) | DR vs HBl (lead) |
|------|-----------------|----------------|------------------|-----------------|
| None | 0 | 0 | 0 | 0 |
| Light | 2 | 1 | 1 | 0 |
| Medium | 3 | 2 | 2 | 1 |
| Heavy | 5 | 3 | 3 | 2 |

**Ranged DR design note:** LP (arrows) are deflected by plate at high angles — Heavy armour DR 5 reflects this. HP (bolts) penetrate all armour tiers best — Heavy armour DR only 3. LBl (stone) follows same curve as LP (blunt impact degrades similarly). HBl (lead) is anti-armour: uniquely flat DR curve (0/0/1/2) — non-deflecting dense mass transfers energy through armour. Heavy armour + cover stacks: DR totals apply cumulatively.

DR is subtracted from damage after net hits + weapon modifier.

---

## 7. WOUNDS AND STAMINA

### Wounds
Health = Endurance score. One Wound per contact that deals damage ≥ Health threshold (typically 3+).
Max Wounds = 3. At max Wounds: incapacitated.
Each Wound: −1D to all combat rolls (cumulative).

### Stamina
Stamina = Endurance + Relevant History + 1 − armour modifier.
Depletes by 1 per round of active combat.
At 0: Out of Breath. −2D to all combat rolls. Recovery: Take a Breath action.

**Hybrid:** Wound Ob penalties carry into TTRPG mass battle Coherence Rating checks (see stage11 PP-089 and mass_battle_v3 §A.5). Do NOT reduce BG commander bonus.

---

## 8. GROUP COMBAT

### Zone Collapse
When 3+ combatants in a zone: combat becomes group combat. Fibonacci bonus applies.

### Fibonacci Group Bonus
Each additional attacker beyond the first against a single unsupported target adds dice to Offence allocation:
- 1st attacker: normal
- 2nd: +1D Offence
- 3rd: +2D Offence
- 4th: +3D Offence
- 5th+: +5D Offence (cap)

Bonus only applies when target has no allies in the zone (unsupported). Supported target uses standard pool split against each attacker.

### Rescue
One ally may interpose against an incoming attack. Declare before resolution. Requires adjacent zone.
Fails silently if no incoming attack was declared — action is lost.

### Multi-Engagement (3v2, 4v3)
Each combatant is engaged in one primary pairing per round. Extras choose which pairing to support (Fibonacci bonus) or maintain their own engagement.

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

**Effective CP = min(CP, current Strength).** As Strength drops, fewer dice regardless of quality.

### PP-086 — Base Damage Formula (mass combat)
Damage = max(0, net_successes_over_Ob + disposition_modifier).
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

> **[PROVISIONAL] Coup Counter — successor rule:** If the Löwenritter Grandmaster is killed (personal combat, mass battle, or other means) while the Coup Counter is ≥ 1: the Löwenritter council immediately selects the highest-Coherence Rating surviving named officer as acting Grandmaster. The Coup Counter resets to 0. The coup attempt is treated as disrupted — the new acting Grandmaster's first action is to consolidate the Order rather than pursue the coup. If no named officers remain, the Löwenritter enter a leaderless state (all units −1D to all rolls until a new Grandmaster is appointed through narrative play).

**Mustering:** Muster order raises 1 new unit per success (up to Military cap) at standard stats.
Upgrade to elite: 2 consecutive successful Govern orders in territory + Wealth ≥ 4.

> **[PROVISIONAL] Theocracy Counter seasonal cap:** Theocracy Counter cannot change by more than ±3 per season from Domain Actions alone. All Theocracy Counter sources combined (Domain Actions, Rendering Stability-driven cascade, Thread operations, military outcomes) cannot produce more than ±5 Theocracy Counter change per season. Changes exceeding the cap are discarded. This prevents runaway Theocracy Counter spirals from multi-action stacking.

> **[PROVISIONAL] Stability recovery:** A faction with Stability ≤ 3 that receives no hostile Domain Actions targeting its Stability in a season gains +1 Stability at Accounting. This represents institutional resilience — factions recover slowly if left alone. Factions at Stability ≥ 4 do not recover this way (they are stable already). Maximum recovery from this rule: +1 per season.

---

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