# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_SIM_PROJ_01
phase: Phase 11c — SIM-PROJ-01 (projectile category cross-mode stress test)
status: CLOSED

completed:
  - SIM-PROJ-01: Modes A + K1 + D + J + L + I. Commit: d293184
  - PP-105: TTRPG personal combat projectile weapons (LP/HP/LBl). Ranged combat
    rules: no Defence allocation, Far zone, Close zone penalty, Cover DR, Reload
    (HP), simultaneous ranged-vs-ranged provisional, sling knife default.
  - PP-106: HBl Dmg Mod +5→+3 (one-shot fix). Artillery sight-line rule (LoS
    required; Line formation screens block shots).

p1_findings_resolved:
  - F-PROJ-01: HBl one-shot → PP-106
  - F-PROJ-04: No personal projectile stats → PP-105
  - F-PROJ-08: No Cavalry intercept window vs Artillery → PP-106 sight-line
  - F-PROJ-03: BG projectile abstraction → ED-064 (design decision pending)

p2_findings_open:
  - F-PROJ-02: LBl dominated by LP → ED-065
  - F-PROJ-05: Artillery morale cascade cap → ED-066
  - ED-067: Dodge action for personal ranged combat (P3)

structural_gaps:
  - GAP-PROJ-01: Ranged vs ranged initiative (PROVISIONAL: simultaneous, high Presence first)

document_versions:
  - mass_battle_v3.md: v4.4
  - params_combat.md: v0.14-AUD2
  - params_mass_combat.md: ST6

next_action:
  task: "Resolve ED-064 (BG projectile abstraction — design decision). Then ED-065 (LBl differentiation). Then address remaining open EDs from prior sessions."
  note: "All P1 projectile gaps resolved. Personal combat and mass combat now have complete provisional projectile parameter sets. BG intentionally abstracted pending ED-064 decision."
```
