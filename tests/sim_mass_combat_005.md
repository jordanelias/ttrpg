# SIM-005/006 — Mass Combat & BG Full Battle Scenarios
## Date: 2026-04-02
## Modes: G1 (mass combat), G5 (BG), K1 (cross-mode)
## Patches: PP-175

Test ID: SIM-005
Mechanics: PP-173/PP-175 mass combat ranged DR | Mode: TTRPG | Temporal: PRES
Tracks: Strength, Cohesion, Morale | Factions: Crown/Church/Varfell/Hafenmark | NPCs: Generic
Archetypes: LP Archer unit, HP Crossbow unit, LBl/HBl Sling unit, Heavy Infantry

Test ID: SIM-006
Mechanics: BG military resolution | Mode: BG | Temporal: PRES
Tracks: Military stat | Factions: Crown/Church | NPCs: Generic

---

## SIM-005 Scenarios

### Scenario A: Crown LP Archers (CP4) vs Church Heavy Infantry (CP4, Heavy armour)
Phase 2 Volley: LP vs Heavy DR5 (unscaled) = 0. LP vs Heavy DR3 (PP-175 scaled) = 0.
(Heavy armour resists LP even at scaled DR — by design.)
Phase 5 Engagement: Church Offensive HC attack on Crown light armour.
E[dmg to Crown] = 4.4 Str loss. Crown Strength 4 → 0. Destroyed in one turn.
Finding: LP archers cannot engage heavy infantry directly. Need HP units or terrain screen.

### Scenario B: Varfell HP Crossbow (CP4) vs Hafenmark Medium Infantry (CP3)
Phase 2 Volley: HP vs Medium DR1 (PP-175) = E[0.6 Str loss]. Vs DR2 (unscaled) = 0.
PP-175 makes HP unit viable vs medium armour. Previous table made this impossible.
Phase 5 Engagement: Ranged unit sidearm (LC, provisional ED-095) vs HC.
Ranged units destroyed in melee — must hold Skirmish formation.

### Scenario C: HBl Lead Sling (CP3) Volley effectiveness (PP-175 scaled)
| Armour | Scaled DR | E[Str loss CP3] |
|--------|-----------|-----------------|
| None | 0 | 1.2 |
| Light | 0 | 1.2 |
| Medium | 1 | 0.2 |
| Heavy | 1 | 0.2 |
HBl now damages Light AND Medium armour at all CP tiers. Only weapon with this profile.

### Scenario D: Prepared Defence counter to ranged
LP (CP4) vs Church Heavy (CP4, PD bonus +2, scaled Heavy DR3):
Total DR = 3+2=5 → E[dmg] = max(0, 1.6-5) = 0.
HP (CP4) vs same: Total DR = 2+2=4 → E[dmg] = 0.
HBl (CP4) vs Heavy (scaled DR1, +PD2 = DR3): E[dmg] = max(0,1.6-3) = 0.
Finding: Prepared Defence + heavy armour negates all ranged at CP≤4.

### P1 Finding (PP-175):
Unscaled mass combat ranged DR (= personal combat DR) made LP/LBl zero damage vs Light armour at ALL CP tiers. PP-175 scales DR ÷2 (rounded up). PROVISIONAL pending ED-096.

---

## SIM-006: Board Game — Ranged (Mode G5)
Crown (Military 4) vs Church (Military 4). Both roll 4D+1D commander = 5D TN7.
E[net] ≈ 1.5 each. E[margin] ≈ 0 → Partial/Draw most likely.
Ranged unit composition invisible at BG scale. Confirmed: no changes needed.

---

## Findings Summary

| ID | Sev | Description | Resolution |
|----|-----|-------------|------------|
| F1 | P1 | Mass combat unscaled DR renders LP/LBl anti-levy-only | PP-175 provisional |
| F2 | P2 | HP crossbow mass combat reload ruling | ED-094 provisional |
| F3 | P2 | Ranged units in Engagement weapon type | ED-095 provisional |
| F4 | editorial | Mass combat DR scaling confirmation | ED-096 provisional |
| F5 | confirmed | BG abstraction correct — no ranged differentiation at BG scale | No change |
