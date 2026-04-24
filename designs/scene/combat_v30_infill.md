<!-- INFILL — prose, rationale, examples extracted from designs/combat/combat_v30.md -->
<!-- Skeleton: designs/combat/combat_v30.md -->
<!-- Does not contain mechanical values. Reference skeleton for all values. -->

# VALORIA — COMBAT DESIGN (v1)
## Date: 2026-04-02
## Version: v1.6 (PP-238, PP-239, PP-247 applied; PP-232: weapon system rebuild, wound penalty, initiative, Health/Stamina, Stage 1/2 struck; PP-210–218: audit gap fixes — Health formula, Critical Hit, Feint timing, Tie Up, Rescue, Dodge, Fibonacci, Anti-Armour, PP-086)
## Status: WORKING DESIGN — not compiled. This is the design-layer source for personal combat.
## Authority: Philosophical Foundations → this document → compilation (when ready)
## Mode applicability: ALL (TTRPG baseline; scales to Hybrid and Board Game via params)
## Patches incorporated: PP-086–092, P2-B11 series (from sim_combat_batch_11.md), PP-172 (SIM-001 ranged subtypes), PP-210–218 (audit gap fixes 2026-04-03)
## Source checkpoint: compilation/v0.14/stage8_combat_deprecated.md (for reference values)
## THREE-MODE FRAMING
TTRPG is always the most granular layer. Hybrid uses TTRPG rules when a named Player Character is present. Board Game uses abstracted equivalents.
## 1. COMBAT POOL
Pool split: allocate between Offence and Defence before any dice are revealed. This split IS the action economy — no separate action declaration needed.
**Board Game equivalent:** Unit Martial stat replaces Combat Pool. No split — Martial dice used for both attack and defence (abstracted).
## 2. ROUND STRUCTURE
## 3. INITIATIVE (PP-232)
Initiative determines declaration order, not action speed. Higher initiative = more information.
**Exchange 1:** Higher Attunement acts last (highest information advantage). **Tiebreaker — equal Attunement (PP-239):** higher Agility acts last. If Agility is also equal: GM determines or coin flip.
**Mixed outcome (PP-276):** When both combatants succeed in the same exchange at different priorities (e.g. opponent lands a Strike at Priority 1 while PC lands a Feint at Priority 2), initiative stays with the current holder. No decisive momentum shift occurred — both sides scored their intended outcome.
Initiative replaces the prior range-priority system. Positional advantage from weapon reach is handled by the weapon TN matrix (§5). Longer weapon user must manoeuvre at disadvantage to re-establish distance.
## 4. ACTIONS
A practitioner declaring Leap (Priority 5) may be struck at Priority 1 before contact. Consistent with mass battle ruling: a declared attacker targeting a practitioner in their Leap round makes the Leap ineligible.
**Incapacitation timing:** Complete currently-resolving action. Fall at end of that priority step. Later-declared actions do not resolve.
Note: Stage 1/Stage 2 in personal combat are the same framework as general incapacitation in mass battle (§A.5), applied at personal scale.
## 5. WEAPON SYSTEM
### Weapon TN Matrix (PP-232)
**"Blade"** encompasses cutting, piercing, and stabbing weapons. **"Blunt"** encompasses bludgeoning weapons.
### Ranged Weapons (retained from prior system, pending ED-129)
### Damage Resolution (PP-232)
### Degree Table (for combat outcomes requiring degree, e.g. Feint, Disarm)
### Reach Rules
- Short vs Long at **Melee range**: Short weapon has priority. Long weapon user must manoeuvre at disadvantage to re-establish Long weapon range.
- Long vs Short at **Ranged distance**: Long weapon has priority. Short weapon user must close at disadvantage.
- Ranged weapons (LP/HP/LBl/HBl): require Far zone to attack. At Close zone, ranged weapons cannot make an Offence roll. Melee weapons cannot retaliate against a ranged attack from Far zone.
- Sling at Close zone: LBl and HBl slingers who are forced to Close zone are assumed to carry a melee weapon (typically a knife, Light Cut). May draw it as a Retrieve Weapon action.
- HP crossbow reload: after firing, HP user must take a full-round Reload action before firing again. No other action may be taken during Reload.
- Ranged vs closing melee: closing character must take a Move action each round. While closing, they are exposed to ranged fire and cannot allocate dice to Defence against it.
### Environmental Factors (Ranged Combat)
Melee users must close to reach a ranged attacker. Terrain affects the number of rounds of exposure and imposes penalties.
Cover (a physical obstacle between attacker and defender) adds DR to the defender:
Cover must be declared in Phase 1 (Movement) to take effect. Cover does not move with the defender. The Game Master determines whether a physical obstacle is present in the zone. A character who does not declare Cover in Phase 1 receives no DR benefit that round, even if physically behind an obstacle. [PROVISIONAL — ED-098]
## 6. ARMOUR
### Armour (PP-232)
### Ranged DR
**Ranged DR design note:** LP (arrows) are deflected by plate at high angles — Heavy armour DR 5 reflects this. HP (bolts) penetrate all armour tiers best — Heavy armour DR only 3. LBl (stone) follows same curve as LP (blunt impact degrades similarly). HBl (lead) is anti-armour: uniquely flat DR curve (0/0/1/2) — non-deflecting dense mass transfers energy through armour. Heavy armour + cover stacks: DR totals apply cumulatively.
## 7. WOUNDS AND STAMINA
### Wounds
### Stamina
## 8. GROUP COMBAT
### Zone Collapse
### Fibonacci Group Bonus
Bonus only applies when target has no allies in the zone (unsupported). Supported target uses standard pool split against each attacker.
### Rescue
One ally may interpose against one incoming attack. Rescuer must specify which attacker is being contested. Declare in Phase 1 before resolution. Requires adjacent zone. Fails silently if no incoming attack was declared — action lost.
- **Rescuer wins (net ≥ attacker net):** Attack redirects to rescuer. Redirected attack resolves against rescuer's armour DR only — contest dice are expended and unavailable for Defence against this attack. Rescuer may be wounded by both the redirected attack (DR only) and their own engagement's attacker (pool−N Defence applies).
- **Rescuer loses (net < attacker net):** Attack resolves against original target. Rescuer's N dice are wasted. Remaining (pool−N) dice still defend the rescuer's own engagement normally. No wounds from the contested attack.
- **Rescuer Momentum (PP-406):** Gains **2 Momentum** on successful intercept (rescuer struck by ≥1 wound from any source — own engagement or redirected attack). Capped at 2 Momentum per Rescue round regardless of number of wounds taken.
- **Martyr Rule (PP-407):** If Rescue attempt **fails** AND the rescuer takes ≥1 wound from their own engagement in the same round → **+1 Momentum**. Distinct from successful intercept payoff. Failed intercept with no rescuer wound: no Momentum return.
- **Rescued actor (successful intercept only):** Exempt from Fibonacci group penalty this round; cannot be targeted by any other attacker this round.
**Rescuer incapacitated before resolution (PP-290):** If the rescuer is incapacitated at Priority 1 before the contest resolves, the Rescue fails. The attack reverts to the original target. No Momentum is granted.
### Multi-Engagement (3v2, 4v3)
Each combatant is engaged in one primary pairing per round. Extras choose which pairing to support (Fibonacci bonus) or maintain their own engagement.
## 9. MASS COMBAT (TTRPG SCALE)
### Unit Stat Block (1–7 unless noted)
**Effective CP = min(CP, current Strength).** As Strength drops, fewer dice regardless of quality.
### PP-086 — Base Damage Formula (mass combat)
### PP-087 — Formation Break Ob Stacking
### PP-088 — Siege Assault Linkage
### PP-091 — Artillery Bombard
### PP-089/PP-090 — Hybrid Phase Order and Mode-Switch
## 10. THREAD IN COMBAT
## 11. FACTION UNIT ROSTERS (from MT-01, 2026-03-30)
> **[PROVISIONAL] Coup Counter — successor rule:** If the Löwenritter Grandmaster is killed (personal combat, mass battle, or other means) while the Coup Counter is ≥ 1: the Löwenritter council immediately selects the highest-Coherence Rating surviving named officer as acting Grandmaster. The Coup Counter resets to 0. The coup attempt is treated as disrupted — the new acting Grandmaster's first action is to consolidate the Order rather than pursue the coup. If no named officers remain, the Löwenritter enter a leaderless state (all units −1D to all rolls until a new Grandmaster is appointed through narrative play).
Upgrade to elite: 2 consecutive successful Govern orders in territory + Wealth ≥ 4.
> **[PROVISIONAL] Theocracy Counter seasonal cap:** Theocracy Counter cannot change by more than ±3 per season from Domain Actions alone. All Theocracy Counter sources combined (Domain Actions, Mending Stability-driven cascade, Thread operations, military outcomes) cannot produce more than ±5 Theocracy Counter change per season. Changes exceeding the cap are discarded. This prevents runaway Theocracy Counter spirals from multi-action stacking.
> **[PROVISIONAL] Stability recovery:** A faction with Stability ≤ 3 that receives no hostile Domain Actions targeting its Stability in a season gains +1 Stability at Accounting. This represents institutional resilience — factions recover slowly if left alone. Factions at Stability ≥ 4 do not recover this way (they are stable already). Maximum recovery from this rule: +1 per season.
## 11.5 FIELDWORK TRANSITIONS
Fieldwork scenes interact with combat at two defined handoff points (scale_transitions_design_v1.md §3.9):
- Exposure accumulated during fieldwork converts to ambusher Initiative advantage when combat triggers from fieldwork discovery or surveillance failure.
## 12. DESIGN NOTES AND OPEN ITEMS
### From sim_x_06 (confirmed working)
### From sim_combat_batch_11 P2 series (all clarifications, see §4 and §9)
### Pending editorial
