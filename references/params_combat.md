<!-- version: v0.14-AUD2 | sources: designs/combat/combat_design_v1.md (PP-105) | last_updated: 2026-04-02 -->
<!-- CANONICAL SOURCE: combat_design_v1.md supersedes stage8_combat.md (has PP-086-092, MT-01, three-mode framing) -->
<!-- PATCHES APPLIED: PP-086 (base damage), PP-087 (Formation Break stacking), PP-088 (assault linkage), PP-091 (Bombard), PP-092 (P2-B11 personal combat clarifications), PP-165 (Health formula fix, Stamina minimum, O/D procedure) -->
<!-- STALE CHECK: If current ruleset version ≠ v0.14, halt and flag before using. -->

# params_combat.md — Personal Combat

## Pool Formula
Combat Pool = (Agility × 2) + Relevant History + 3 (minimum 5)
Stamina = Endurance + Relevant History + 1 (modified by armour)
Health = Endurance + 6 (total damage buffer; reduces to 0 → take Wound, Health resets to full)

Pool modifiers:
- Wounds: −1D per wound (cumulative)
- Fibonacci group bonus: +dice to Offence allocation only (see below)

## Weapon Statistics
| Type | Hit TN | Def TN | Dmg Modifier | Examples |
|------|--------|--------|-------------|---------|
| Light Cut | 5 | 6 | +1 to +2 | Dagger, knife, short sword, spear |
| Heavy Cut | 6 | 7 | +4 to +5 | Longsword, axe, glaive |
| Light Blunt | 6 | 7 | +1 to +2 | Hand axe, short club, sap |
| Heavy Blunt | 7 | 8 | +4 to +5 | War hammer, mace, pollaxe |
| Unarmed | 8 | 9 | +0 | Fists, grappling, improvised |
| LP — bow | 6 | — | +2 | Shortbow, longbow |
| HP — crossbow | 5 | — | +4 | Light crossbow, heavy crossbow |
| LBl — sling | 7 | — | +1 | Sling, staff sling |

Ranged weapons have no Def TN — targets cannot allocate Defence dice against them.
Damage (ranged) = net successes + weapon modifier (STR not added — arm strength already in modifier/TN).

## Ranged Combat Rules (PP-105)

**Zone:** Ranged weapons require Far zone. At Close zone: −3D to attacker pool. Sling cannot be used at Close zone (use as Unarmed or draw melee weapon — Reload action).

**No parry:** Target cannot allocate Defence dice against ranged attacks. Armour DR applies normally.

**Cover:** If defender declared Cover in Phase 1: +2 DR vs LP/LBl; +1 DR vs HP. Cover requires a physical obstacle (wall, tree, wagon). 

**Establish Distance (defender option):** Costs combat action. Attacker loses shot this round. Target moves beyond range.

**Reload (HP crossbow only):** After each shot, HP user must take Reload action before firing again. Reload = full round, no other action. LP and LBl fire every round.

**Ranged vs ranged (mirror):** Initiative rules apply (higher Presence declares first). Both attacks resolve simultaneously at round end. [PROVISIONAL — GAP-PROJ-01]

**STR minimums:**
| Weapon | Min STR | Penalty if 1 below |
|--------|---------|-------------------|
| LP (bow) | 2 | −1D |
| HP (crossbow) | 1 | — |
| LBl (sling) | 1 | — |

**Sling at Close zone default:** Slinger is assumed to carry a knife (LightCut). May draw knife as Retrieve Weapon action if forced to Close zone.

**No personal HBl:** Artillery (HBl) is a mass combat unit — no personal combat equivalent. Individual siege crew members fight as unarmed or with melee weapons.

## Strength Minimums
| Weight | Min STR | Penalty if 1 below |
|--------|---------|-------------------|
| Light Cut / Light Blunt | 1 | — |
| Heavy Cut | 3 | −1D Combat Pool |
| Heavy Blunt | 4 | −1D Combat Pool |

Cannot wield if 2+ below minimum.

## Reach / Range
- Range: Close zone (Short reach) or Far zone (Long reach)
- Short weapons: cannot attack at Far zone
- Long weapons at Close zone: −1D Offence + half damage (rounded up)

## Damage Formula
Damage = excess successes + STR + weapon modifier
Critical Hit (excess ≥ 3): weapon modifier doubled

## Mass Mismatch Penalty
Light weapon defender splits pool vs Heavy weapon attack: defensive successes −1 (min 0).
Exempt: Full Guard; Long weapon at Close zone.

## Armour (Damage Reduction by attacker weapon type)
| Armour | STR Min | Stamina Mod | vs LC | vs HC | vs LB | vs HB |
|--------|---------|-------------|-------|-------|-------|-------|
| None | — | +0 | 0 | 0 | 0 | 0 |
| Light | 2 | +0 | 2 | 1 | 1 | 0 |
| Medium | 3 | −1 | 4 | 3 | 2 | 1 |
| Heavy | 4 | −2 | 6 | 5 | 3 | 1 |

## Wounds / Incapacitation
Health = Endurance per wound. At 0 Health → take Wound, Health resets.
| Endurance | Max Wounds before incapacitation |
|-----------|----------------------------------|
| 1–3 | 2 |
| 4–5 | 3 |
| 6–7 | 4 |

Wound Ob penalty: +1 Ob per wound (all rolls). Incapacitated: Stage 1 (down) or Stage 2 (dying, −2 Morale to any witnessing unit/ally).

## Fibonacci Group Bonus (Offence dice only)
| Attackers | Bonus Dice |
|-----------|-----------|
| 1 | 0 |
| 2 | +1 |
| 3 | +2 |
| 4–5 | +3 |
| 6–7 | +4 |
| 8+ | +5 |

## Actions Summary
Strike / Establish Distance / Feint / Take a Breath / Full Guard / Disarm / Retrieve Weapon / Reload (HP crossbow only) / **Dodge** (ranged only — forfeit attack; allocate full pool as passive Defence vs incoming ranged attack this round; armour DR still applies) / Out of Breath (forced at Stamina 0)

**Dodge (ED-067 resolved — provisional):** Defender may Dodge a ranged attack instead of being unable to respond. Full pool = passive Defence dice vs attacker's Offence. Cover DR still applies additionally. Costs the defender's full combat action this round. [PROVISIONAL]

## Stamina Minimum (PP-165)
Stamina minimum: **1**. If Endurance + History + 1 − armour modifier ≤ 0, Stamina = 1.
Heavy armour (−2 mod) on Endurance 1, no History: raw Stamina = 0 → floored to 1.

## Offence / Defence Allocation Procedure (PP-165)
At the start of each combat round, each combatant secretly allocates their Combat Pool between Offence and Defence.
1. Each player writes (or holds) their split privately.
2. Both reveal simultaneously.
3. Offence dice roll against opponent's Defence dice (compare successes). Defender wins ties.
4. Fibonacci Group Bonus applies to Offence allocation only.
Minimum 0D to either allocation (full pool to one side permitted).

## Wound Dual Penalty — Quantified (PP-165)
Each Wound applies: −1D to Combat Pool AND +1 Ob to all rolls.
At 3 Wounds (Endurance 4–5 character): −3D pool, +3 Ob. Effective combat pool ≈ half starting; Ob on most rolls ≈ doubled.
At max Wounds before incapacitation: character is mechanically non-functional in combat (correct by design — incapacitation is imminent).

<!-- patch_history: references/params_combat_history.md -->

<!-- canonical_sources: references/canonical_sources.yaml -->
