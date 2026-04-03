# params_mass_combat — Patch History
## Container: references/params_mass_combat.md
## Auto-maintained by valoria-orchestrator

---

## PATCH SUMMARY (ST-MB series, applied to mass_battle_v3.md on 2026-04-02)

### ST-MB-03 — Effective CP Timing
Effective CP calculated at Phase 3 end. All Phase 4 damage simultaneous at Phase 5 Step 1.
CP does not change within Phase 4.

### ST-MB-04 — Morale Cap + General Kill Order
Apply non-general Morale changes first (cap −3), then Stage 2 general death −2 separately.
Maximum total Morale loss per Cascade Phase: −5.

### ST-MB-05 — CR=0 Uncommanded
All units at Line formation, Cohesion floor 1, no tactics. Morale floor suspended.

### ST-MB-06 — Reserve Timing
Commit at Phase 3 Turn N+1 → available for Phase 4 that same turn.

### ST-MB-07 — Shield Wall Three-Sided
Negates one declared flank. Front + opposite flank both apply normally.

### ST-MB-08 — Feigned Retreat Recognition
Roll CR dice (d10s equal to CR score) vs Ob 2 to recognise feint.

### ST-MB-09 — Mixed TS Forces in Southernmost
Reduce Strength proportionally to TS-capable fraction. Only Restoration+Varfell VTM≥2 viable.

### ST-MB-10 — Woven Unit Shifting Object
Shattered Woven unit fights at Line/Cohesion 1 for battle; Shifting Object status registers post-battle only.

### ST-INT-06 — BG Unit TS (Southernmost)
Church Templar: TS=0. Restoration with Weaver marker: TS=30. Varfell VTM≥2: TS=30.
All others: TS=0 (cannot operate in Southernmost).

### ST-INT-09 — Military Loss Timing
TTRPG: immediate. BG: queues to Accounting. Hybrid: TTRPG timing during battle.


## ALTONIAN UNIT STATS — PROVISIONAL PLACEHOLDER (ED-036)
## Status: PROVISIONAL — requires user approval for final values
## [PROVISIONAL: all values below]

| Unit | Strength | CP | Cohesion | Morale | Weapon | Armour | Notes |
|------|----------|----|----------|--------|--------|--------|-------|
| Vanguard (standard) | 5 | 4 | 4 | 5 | HeavyCut | Medium | Standard Altonian professional infantry |
| Elite Guard | 4 | 5 | 5 | 5 | HeavyCut | Heavy | Command unit; general typically attached |
| Thread Corps | 3 | 3 | 4 | 4 | LightCut | Light | TS 40 (Southernmost-capable); Thread operations each turn |

Altonian forces deploy at IP ≥ 68 (Vanguard) or IP ≥ 75 (Elite Guard + Thread Corps).
Altonian general CR: 4 (provisional).

## ED-037 — Volley TN 6 (PROVISIONAL CONFIRMED AS INTENTIONAL)
## [PROVISIONAL: TN 6 for Volley is an explicit exception to universal TN 7]
Volley Phase 2: Roll Effective CP vs TN 6 (not TN 7).
Rationale: coordinated massed ranged fire has structural advantage over individual melee.
This is documented as an intentional exception. Review during playtesting.
In hybrid mode, Volley by BG Ranged units converted to TTRPG uses TN 6.

## ED-038 — Coherence in Mass Battle (RESOLVED)
Coherence referenced in §A.10 = practitioner's personal Coherence track (10→0, from threadwork Part 3).
Starting value: 10 (full). Severed threshold: Coherence 1 (→ +2 Ob to all Thread ops in battle).
At Coherence 0: no Thread operations possible (per threadwork P-27).
auto-cost −1/op: each Thread operation in mass battle depletes personal track by 1.

## PENDING EDITORIALS
- ED-033: Commander bonus formula (P1) — still open
- ED-037: Volley TN — PROVISIONAL: TN 6 confirmed as intentional exception
- ED-038: Coherence — RESOLVED: personal track from threadwork Part 3
- ED-039: Military seasonal cap pooling (P2)
- ED-036: Altonian unit stats BLOCKER

## PP-173 (2026-04-02) — Ranged DR Table Split
Source: SIM-002
Changes:
- Unit table: single 'Ranged | LP | +2' row expanded to 4 rows (LP/HP/LBl/HBl)
- DR table: Projectile column (LightCut) replaced with 4-column Ranged DR table
  LP: 0/2/3/5 | HP: 0/1/2/3 | LBl: 0/1/2/3 | HBl (lead sling): 0/0/1/2
- HBl personal combat cross-reference updated
- LBl anti-levy clarification added
Editorials: ED-087 (BG ranged modifier)
