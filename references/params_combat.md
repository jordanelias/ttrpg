<!-- version: v0.14-ST2 | sources: designs/combat/combat_design_v1.md | last_updated: 2026-04-02 -->
<!-- CANONICAL SOURCE: combat_design_v1.md supersedes stage8_combat.md (has PP-086-092, MT-01, three-mode framing) -->
<!-- PATCHES APPLIED: PP-086 (base damage), PP-087 (Formation Break stacking), PP-088 (assault linkage), PP-091 (Bombard), PP-092 (P2-B11 personal combat clarifications) -->
<!-- STALE CHECK: If current ruleset version ≠ v0.14, halt and flag before using. -->

# params_combat.md — Personal Combat

## Pool Formula
Combat Pool = (Agility × 2) + Relevant History + 3 (minimum 5)
Stamina = Endurance + Relevant History + 1 (modified by armour)
Health = Endurance (per wound; resets on wound)

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
Strike / Establish Distance / Feint / Take a Breath / Full Guard / Disarm / Retrieve Weapon / Out of Breath (forced at Stamina 0)

## PATCH SUMMARY (PP-086–092, applied 2026-04-02)

### PP-086 — Mass Combat Base Damage
Damage = max(0, net_successes_over_Ob + disposition_modifier)
Disposition modifiers: Offensive +2 flat, Defensive +4 flat (add to base).

### PP-087 — Formation Break Ob Stacking
+1 Ob per break, cumulative, persists through rally. Cap: 3 breaks = Dispersed (permanent rout).
All attachments lost on any Formation Break.

### PP-088 — Siege Assault Linkage
Mass combat win during declared Assault = Fortification −1.
Overwhelming win = Fortification −2.
Field victory ≠ breach — must declare Assault next season.

### PP-091 — Artillery Bombard
Roll Artillery CP vs Ob (Short=1, Med=2, Long=3). No melee exchange.
Success = flat 1 Str damage. Overwhelming = flat 2.
Cannot Bombard at melee range.

### PP-092 — Personal Combat Clarifications (P2-B11 series)
- Defence split: defender allocates blind before any attacker declares
- "Same range" = shorter weapon at Close zone = Short range achieved
- Stunt + chain die: both effects independent, apply simultaneously
- Tie Up: blocks escape for one round only
- Rescue fails with no incoming attack (action lost)
- Incapacitation: complete resolving action, fall at end of that priority step
- Commander in personal combat: cannot also Rally/order same round
- Routed units hold position during scene resolution

## PENDING EDITORIALS AFFECTING THESE PARAMS
- ED-033: Commander bonus formula (three conflicting formulas — BG/TTRPG/Hybrid)
- ED-037: Volley TN 6 vs TN 7 (mass combat)
- ED-038: Coherence stat definition in mass battle
- ED-040: Artillery Balanced disposition lock (intentional?)
