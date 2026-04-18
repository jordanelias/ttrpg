# SIM-002/003 — Mass Combat & BG Ranged Weapons
## Date: 2026-04-02
## Modes: G1 (mass combat), G5 (BG), K1 (cross-mode delta)
## Patches: PP-173

Test ID: SIM-002
Mechanics: PP-173 mass combat ranged DR | Mode: TTRPG | Temporal: PRES
Tracks: Strength, Cohesion, Morale | Factions: All | NPCs: Generic
Archetypes: Archer unit (LP), Crossbow unit (HP), Stone sling (LBl), Lead sling (HBl)

Test ID: SIM-003
Mechanics: BG military resolution | Mode: BG/Hybrid | Temporal: PRES
Tracks: Military stat | Factions: All | NPCs: Generic
Archetypes: All unit types

---

## SIM-002: Mass Combat Volley Phase — Ranged Subtypes

### Mode G1: Expected Strength Loss (net successes − DR, no Ob deduction for uncontested Volley)

**CP = 3 (Professional), TN 6:**
| Unit type | vs None | vs Light | vs Med | vs Heavy |
|-----------|---------|----------|--------|----------|
| LP (archer) | 1.2 | 0 | 0 | 0 |
| HP (crossbow) | 1.2 | 0.2 | 0 | 0 |
| LBl (stone) | 1.2 | 0.2 | 0 | 0 |
| HBl (lead) | 1.2 | 1.2 | 0.2 | 0 |

**CP = 5 (Elite), TN 6:**
| Unit type | vs None | vs Light | vs Med | vs Heavy |
|-----------|---------|----------|--------|----------|
| LP (archer) | 2.0 | 0 | 0 | 0 |
| HP (crossbow) | 2.0 | 1.0 | 0 | 0 |
| LBl (stone) | 2.0 | 1.0 | 0 | 0 |
| HBl (lead) | 2.0 | 2.0 | 1.0 | 0 |

### Delta vs Old Projectile Column (LightCut DR = 0/2/4/6), CP = 5:
| Unit | Δ vs Light | Δ vs Medium |
|------|-----------|-------------|
| LP | +0.00 | +0.00 |
| HP | +1.00 | +0.00 |
| LBl | +1.00 | +0.00 |
| HBl | +2.00 | +1.00 |

**Finding F1 (P1):** Old single Projectile column (LightCut DR) was wrong. HP and HBl units were massively undervalued vs Light+ armour. Corrected by splitting into 4 columns.

### Prepared Defence Interaction (CP 5 attacker vs CP 4 target, Light armour):
| Unit | Base DR | + Prepared Defence (DR 2) | Total | E[dmg] |
|------|---------|--------------------------|-------|--------|
| LP | 2 | +2 | 4 | 0 |
| HP | 1 | +2 | 3 | 0 |
| LBl | 1 | +2 | 3 | 0 |
| HBl | 0 | +2 | 2 | 0 |

**Finding:** Prepared Defence is effective against all ranged types at Light armour vs CP5. HBl barely survives (0 damage). Confirms Prepared Defence is a meaningful counter to ranged.

### HBl Distinction (Finding F2):
- HBl (Artillery/siege): unit-level, PP-091/PP-106, sight-line rule, Bombard = flat Str damage
- HBl (personal/lead sling): individual weapon, PP-172, DR 0/0/1/2
Mass combat doc incorrectly stated "HBl has no personal combat equivalent." Corrected by PP-173.

### LBl anti-levy finding (P3):
LBl vs Light armour (CP3): E[Str loss] = 0.2 (practical 0 in discrete unit damage).
LBl units are mechanically useless vs any armoured force. Clarifying note added.

---

## SIM-003: Board Game — Ranged Weapons (Mode G5)

BG uses Military stat pool for all combat. No weapon type differentiation at BG scale.
Ranged unit types (LP/HP/LBl/HBl) do not appear as distinct BG mechanics.
Artillery (HBl siege) applies only at TTRPG/Hybrid scale via PP-091.

**Finding:** BG correctly abstracts above weapon-type level. No changes needed.

**ED-087 raised:** Should ranged-specialist factions get BG Military modifier? Provisional: No.

### Mode K1: Cross-Mode Delta
| Property | TTRPG Personal | TTRPG Mass Combat | Board Game |
|----------|----------------|-------------------|------------|
| Weapon types | LP/HP/LBl/HBl distinct TN/mod | LP/HP/LBl/HBl distinct DR | Abstracted to Military |
| Range mechanic | Zone-based (Far/Close) | Volley Phase (Phase 2) | None |
| DR | 4×4 matrix | 4×4 matrix (ranged) | None |
| LBl dead choice? | Med+ armour only | Light+ armour | N/A |
| HP dominance | vs armoured targets | vs Light-Medium armour | N/A |

---

## Findings Summary

| ID | Sev | Description | Resolution |
|----|-----|-------------|------------|
| F1 | P1 | Old Projectile DR (LightCut) wrong — HP/HBl undervalued | PP-173 applied |
| F2 | P2 | HBl personal vs Artillery distinction needed in mass_battle | PP-173 applied |
| F3 | P3 | LBl anti-levy clarification | PP-173 applied |
| F4 | editorial | BG ranged-specialist faction modifier | ED-087 provisional |

---

## Propagation Complete After This Commit
- designs/combat/combat_design_v1.md ✓ (PP-172, d30e47b)
- references/params_combat.md ✓ (PP-172)
- designs/mass_combat/mass_battle_v3.md ✓ (PP-173, this commit)
- references/params_mass_combat.md ✓ (PP-173, this commit)
- designs/board_game/ — no changes needed (BG correctly abstracted)
