# SIM-PROJ-01: Projectile Weapon Categories — Cross-Mode Stress Test
## Date: 2026-04-02
## Modes: A + K1 + D + J + L + I
## Status: COMPLETE

---

## 7-DIMENSION TAG
Test ID: SIM-PROJ-01
Mechanics: LP/HP/LBl/HBl projectile categories (PP-104), mass combat Volley, personal combat ranged
Mode: TTRPG (personal + mass) + BG
Temporal: PRES
Tracks: Unit Strength, DR, Morale, Cohesion, Health/Wounds
Factions: Generic
NPCs: Generic unit archetypes
Archetypes: Ranged skirmisher, siege crew, armoured infantry, cavalry

---

## MODE A — ISOLATION: Expected Strength loss per Volley exchange

TN 6, E[net]: 2D=0.80, 3D=1.20. Formula: max(0, net + Dmg Mod − DR).

| Type / Target | vs None | vs Light | vs Medium | vs Heavy |
|--------------|---------|----------|-----------|---------|
| LP (3D, +2, DR 0/1/4/7) | 3.20 | 2.20 | 0 | 0 |
| HP (3D, +4, DR 0/1/3/5) [PROV] | 5.20 | 4.20 | 2.20 | 0.20 |
| LBl (3D, +1, DR 0/2/4/6) [PROV] | 2.20 | 0.20 | 0 | 0 |
| HBl (2D, +5 OLD) | 5.80 | 5.80 | 4.80 | 3.80 — ONE-SHOTS ALL |
| HBl (2D, +3 POST-PP-106) | 3.80 | 3.80 | 2.80 | 1.80 |
| HBl with Prepared Def (HI, +2DR) | 3.80 | 3.80 | 0.80 | — |

---

## MODE K1 — CROSS-MODE DELTA

| Property | TTRPG Personal | TTRPG Mass | BG |
|----------|---------------|------------|-----|
| LP stats | AUD2 (PP-105) | DR 0/1/4/7, +2 | NONE (F-PROJ-03→ED-064) |
| HP stats | AUD2 (PP-105) | [PROV] DR 0/1/3/5, +4 | NONE |
| LBl stats | AUD2 (PP-105) | [PROV] DR 0/2/4/6, +1 | NONE |
| HBl stats | Not applicable (siege only) | DR 0/0/1/2, +3 (PP-106) | NONE |
| Defence vs ranged | No Defence allocation | Prepared Defence (½ CP) | N/A |
| Dominant strategy | Establish Distance / Cover | Sight-line screening (PP-106) | N/A |
| Dead choice | LBl vs LP (ED-065) | LBl vs LP (ED-065) | All same |

---

## FINDINGS

### P1
| ID | Description | Patch |
|----|-------------|-------|
| F-PROJ-01 | HBl +5 one-shots all units (E[Dmg] 3.8–5.8) | PP-106: +5→+3 |
| F-PROJ-03 | 4 categories zero effect in BG | ED-064 |
| F-PROJ-04 | No personal combat projectile stats | PP-105 |
| F-PROJ-08 | Cavalry cannot intercept Artillery pre-Volley | PP-106: sight-line rule |

### P2
| ID | Description | Action |
|----|-------------|--------|
| F-PROJ-02 | LBl dominated by LP in all scenarios | ED-065 |
| F-PROJ-05 | Artillery morale cascade cap ambiguity | ED-066 |
| F-PROJ-06 | HP Reload action missing | PP-105 (Reload added) |
| F-PROJ-07 | Slinger at Close zone: no viable action | PP-105 (knife default) |

### Structural
| ID | Description |
|----|-------------|
| GAP-PROJ-01 | Ranged vs ranged initiative (simultaneous?) — PROVISIONAL applied |

---

## PATCHES APPLIED
- PP-105: Personal combat LP/HP/LBl stats + ranged rules + Reload action
- PP-106: HBl +3 + Artillery sight-line rule
- params_combat → v0.14-AUD2
- params_mass_combat → ST6
- mass_battle_v3 → v4.4
