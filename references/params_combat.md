<!-- version: v0.14-AUD5 | sources: designs/combat/combat_design_v1.md (PP-188) | last_updated: 2026-04-02 -->
<!-- CANONICAL SOURCE: combat_design_v1.md supersedes stage8_combat.md (has PP-086-092, MT-01, three-mode framing) -->
<!-- PATCHES APPLIED: PP-086, PP-087, PP-088, PP-091, PP-092, PP-165, PP-172, PP-174 (remove stale HBl no-personal note; fix Damage Formula; ED-092 provisional on STR) -->
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
| Piercing — Bow | 6 | 8† | +2 | Shortbow, longbow, recurve |
| Piercing — Crossbow | 5 | 8† | +2‡ | Light crossbow, heavy crossbow |
| Blunt — Throwing weapon | 7 | 8† | +1 | Javelin, thrown rock, dart |
| Blunt — Sling | 8 | 8† | §ammo | Sling, staff sling |

†Def TN 8: at Close zone, full pool to Defence only. No Offence split.
‡Crossbow base +2. If hit (net hits > 0 after DR): +2 flat vs Medium, +3 flat vs Heavy.
§Sling: −2D from Combat Pool. Ammo: Clay +1 / Stone +2 / Metal +3 / Lead +4.

Ranged weapons have no Def TN — targets cannot allocate Defence dice against them.
Damage (ranged) = net successes + weapon modifier (STR not added — arm strength already in modifier/TN).

## Ranged Combat Rules (PP-188)

**Zone:** Ranged weapons (Piercing and Blunt) require Far zone to make an Offence roll. At Close zone: cannot attack. See Ranged Defence below.

**No parry (Far zone):** When attacker is at Far zone, target cannot allocate Defence dice against ranged attacks. Armour Damage Reduction (DR) applies normally.

**Ranged Defence at Close zone (new — PP-172):** If a ranged-weapon user is forced into Close zone by a melee attacker, they may defend at Def TN 8 using their full pool. No Offence allocation permitted. This is an emergency defence only.

**Cover:** If defender declared Cover in Phase 1 of Movement: cover DR applies. Cover requires a physical obstacle. Cover does not move with the defender.

| Cover type | vs Piercing | vs Blunt |
|------------|------------|---------|
| Soft (trees, wagon, bale) | +2 DR | +2 DR |
| Hard (stone wall, fortification) | Blocks shot | Blocks shot |

**Environmental approach (melee closing):**
| Terrain | Rounds to close | Penalty to closer |
|---------|----------------|-------------------|
| Open ground | 1 round | None |
| Difficult (marsh, rubble, slope) | 2 rounds | +1 Ob to movement actions |
| Shallow river / ford | 2 rounds | +1 Ob, −2D combat while crossing |
| Deep river | 3 rounds + Swim (Ob 2) | Fail = swept back |
| Wall or rampart | Climb (TN 8 Ob 1) | Action lost if climb fails |

**Establish Distance (defender option):** Costs combat action. Attacker loses shot this round. Target moves beyond range.

**Fire rate:**
- Bow and throwing weapons: fire every round. No reload.
- Crossbow: fire every other round. Reload action (full round, no other action) required after each shot.
- Sling: fire every other round. Wind-up action (full round) required after each shot.

**Ranged vs ranged (mirror):** Initiative rules apply (higher Presence declares first). Both attacks resolve simultaneously at round end. [PROVISIONAL — GAP-PROJ-01]

**STR minimums:**
| Weapon | Min STR | Penalty if 1 below |
|--------|---------|-------------------|
| Bow | 2 | −1D |
| Crossbow | 1 | — |
| Throwing weapon | 1 | — |
| Sling | 1 | — |

**Sling at Close zone:** Slingers are assumed to carry a knife (Light Cut) or other melee weapon. May draw it as a Retrieve Weapon action if forced to Close zone.

**HBl personal vs siege distinction:** HBl at personal scale = lead shot sling (PP-172). HBl at siege/mass scale = Artillery unit (PP-091/PP-106, sight-line rule). These are distinct: personal HBl uses Ranged DR 0/0/1/2; Artillery Bombard uses flat Strength damage formula.

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
Damage = max(0, net hits + weapon modifier − DR)
Critical Hit (net hits ≥ 3): weapon modifier doubled
[PROVISIONAL ED-092: STR appeared in a prior formula version; design doc (canonical) does not include STR in damage. Confirm whether STR is intended as a damage addition or only as a minimum-wield requirement.]

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

## Ranged Damage Reduction (DR) by Armour Tier
| Armour | vs Piercing | vs Blunt |
|--------|------------|---------|
| None | 0 | 0 |
| Light | 2 | 1 |
| Medium | 3 | 2 |
| Heavy | 5 | 3 |

**Crossbow armour penetration (post-DR):** If crossbow attack hits, add flat bonus after DR: +2 vs Medium, +3 vs Heavy.
**Sling:** −2D pool. Ammo mod (Clay +1 / Stone +2 / Metal +3 / Lead +4) applied before roll. DR applied normally.
**Fibonacci group bonus:** Does not apply to ranged attacks.
Cover DR stacks additively with armour DR.

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
