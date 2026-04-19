## Victory Conditions — Pointer
**Canonical source: `designs/board_game/victory_v30.md`** (all victory conditions, co-victory pairings, shared loss conditions).

The Deed-based victory system has been dissolved for ALL factions including Löwenritter (PP-427). Victory = Territory Consolidation Value (PV) thresholds + faction-specific political conditions, sustained for 2 consecutive Accounting steps.

### Summary (see victory_v30.md §3 for full conditions)

| Faction | Primary Victory | Key Thresholds |
|---------|----------------|----------------|
| Crown | Peninsula Sovereignty | PV ≥ 16 + suppress all rivals + Invasion Pressure (IP) < 60 + Parliament Integrity (PI) ≥ 3 |
| Church of Solmund | Solmundan Orthodoxy | PV ≥ 8 + PT ≥ 3 all held territories. Graduated Seizure: Pool = Influence + floor(CI/15), Ob = 10 − PT − infra (floor 1) (PP-494) |
| Hafenmark | Parliamentary Sovereignty | PV ≥ 12 + Mandate ≥ 4 + PI ≥ 5 + Crown Mandate ≤ 3 |
| Varfell Path A | Intelligence Hegemony | PV ≥ 10 + Vaynard Thread Mastery (VTM) ≥ 3 + 2 rival stats revealed + expansion |
| Varfell Path B | Southernmost Dominion | PV ≥ 8 + VTM ≥ 3 + T13 control + T15 presence + Warden's Accord (WA) ≥ +1 |
| Varfell Path C | Thread Supremacy | PV ≥ 10 + VTM = 5 + Rendering Stability (RS) ≥ 50 |
| Restoration Movement (RM) | Cultural Revolution (Hybrid only, post-Founding) | Phase 1: PT ≤ 1 in ≥ 8/15 territories. Phase 2: Cultural Uprising of T9 Himmelenger. Win: T9 held + Phase 1 × 2 Accounting. No faction stats. (PP-460, PP-478) |
| Löwenritter | Regency Establishment | PV ≥ 10 + Thread Consciousness (CI) < 50 + IP < 60 + RS > 40 + PI ≥ 4 + successor |

**Universal Victory — Peninsular Sovereignty (all factions):** All 15 playable territories (T1–T14, T17) controlled directly or via effective hegemony (Treaty-bound, Submitted, or institutionally dominated rivals). Accord ≥ 2 in all directly-controlled territories. Peninsular Strain ≤ 6. Held 2 consecutive Accountings. Faction-specific victories above are retained as alternate (easier) paths. See peninsular_strain_v1.md §6.

**Peninsular Partition (Co-Victory, multiplayer):** Both factions collectively control all 15 territories. Each PV ≥ 10. Accord ≥ 2 everywhere. No inter-faction battle preceding 4 seasons. Strain ≤ 6. Both Mandate ≥ 3. See peninsular_strain_v1.md §6.3.

### Territory Consolidation Values (PV)
Per victory_v30.md §1. Total PV = 33 (T16 Schoenland not in territorial play, T15 Askeheim PV = 0).

| T# | Territory | PV | Starting Controller |
|----|-----------|-----|---------------------|
| T1 | Valorsplatz | 5 | Crown |
| T8 | Gransol | 4 | Hafenmark |
| T9 | Himmelenger | 5 | Church of Solmund |
| T12 | Sigurdshelm | 4 | Varfell |
| T3 | Lowenskyst | 3 | Crown |
| T10 | Spartfell | 1 | Hafenmark |
| T14 | Ehrenfeld | 3 | Crown |
| T2 | Kronmark | 1 | Crown |
| T4 | Grauwald | 1 | Varfell |
| T5 | Feldmark | 1 | Crown |
| T6 | Stillhelm | 1 | Crown |
| T7 | Rendstad | 1 | Hafenmark |
| T11 | Halvardshelm | 1 | Varfell |
| T13 | Oastad | 1 | Varfell |
| T17 | Halvarshelm | 1 | Hafenmark |

Starting PV: Crown 14, Hafenmark 7, Varfell 7, Church 5.

### Co-Victory Pairings
Per victory_v30.md §4. All require 2 consecutive Accounting steps except Church+Hafenmark Partition (immediate on mutual agreement).

| Pair | Key Conditions |
|------|---------------|
| Crown + Hafenmark | Crown PV ≥ 12, Hafenmark PV ≥ 12, PI ≥ 7, CI < 50, Crown Mandate ≥ 4, Hafenmark Mandate ≥ 4 | *(PP-561)* |
| Crown + Varfell | Crown PV ≥ 12, Varfell PV ≥ 8, VTM ≥ 3, RS ≥ 50 |
| Varfell + RM | VTM ≥ 4, WA ≥ +2, ≥ 4 territories PT ≤ 1, RS ≥ 40 |
| Hafenmark + RM | Hafenmark PV ≥ 10, ≥ 4 territories PT ≤ 2, PI ≥ 4, RS ≥ 40 |
| Löwenritter + Hafenmark | Löwenritter PV ≥ 8, Hafenmark PV ≥ 8, PI ≥ 4 |
| Church + Hafenmark (Partition) | Crown Mandate ≤ 1, CI ≥ 50, Church ≥ 2 territories, Hafenmark ≥ 3, no military conflict |

Incompatible: Crown + Church, Crown + Löwenritter, Church + Varfell, Church + RM.

### Shared Loss Conditions
Per victory_v30.md §5. RS = 0 (Rupture), IP ≥ 100 + Altonian External Relationship (AER) ≤ 1 (Altonian Conquest), or all factions Stability 0 (Total Institutional Collapse).

### Hollow Victory — DISSOLVED
The Hollow Victory modifier system (Deed-count penalties) has been dissolved with the Deed system (PP-427). In Hybrid mode, BG victory without personal arc resolution is a narrative qualifier per P-32 (see victory_v30.md §9.3).

### Public Instability (PI) Thresholds (PP-501, ED-361 resolved)
PI measures popular dissatisfaction with monarchical governance. Higher PI benefits Hafenmark (PI ≥ 5 required for their victory). PI hurts Crown.

| PI Range | Effect |
|----------|--------|
| 0–4 | Stable. No mechanical effect. |
| 5–9 | Tensions. Crown Domain Actions +1 Ob in territories with PI markers. Hafenmark Parliamentary Manoeuvre −1 Ob. |
| 10–14 | Unrest. Crown Stability check Ob +1 at Accounting. Popular demonstrations — flavour. |
| 15–19 | Revolt. Crown loses 1 territory per season (lowest PV, becomes Uncontrolled after 1-season Political Vacuum per PP-500). Löwenritter coup check if Coup Counter ≥ 2. |
| 20+ | Collapse. Crown elimination at next Accounting unless PI reduced below 20 before then. |

PI advances per existing IP/PI interaction rules. PI markers placed in territories where relevant events fire.
[EDITORIAL: ED-361 — resolved provisionally. Thresholds designed so PI 5 (Hafenmark victory condition) is achievable without triggering Crown crisis. PI 15+ is catastrophic for Crown. Flagged for simulation.]


### Summary (see victory_v30.md §3 for full conditions)

| Faction | Primary Victory | Key Thresholds |
|---------|----------------|----------------|
| Crown | Peninsula Sovereignty | PV ≥ 16 + suppress all rivals + Invasion Pressure (IP) < 60 + Parliament Integrity (PI) ≥ 3 |
| Church of Solmund | Solmundan Orthodoxy | PV ≥ 8 + PT ≥ 3 all held territories. Graduated Seizure: Pool = Influence + floor(CI/15), Ob = 10 − PT − infra (floor 1) (PP-494) |
| Hafenmark | Parliamentary Sovereignty | PV ≥ 12 + Mandate ≥ 4 + PI ≥ 5 + Crown Mandate ≤ 3 |
| Varfell Path A | Intelligence Hegemony | PV ≥ 10 + Vaynard Thread Mastery (VTM) ≥ 3 + 2 rival stats revealed + expansion |
| Varfell Path B | Southernmost Dominion | PV ≥ 8 + VTM ≥ 3 + T13 control + T15 presence + Warden's Accord (WA) ≥ +1 |
| Varfell Path C | Thread Supremacy | PV ≥ 10 + VTM = 5 + Rendering Stability (RS) ≥ 50 |
| Restoration Movement (RM) | Cultural Revolution (Hybrid only, post-Founding) | Phase 1: PT ≤ 1 in ≥ 8/15 territories. Phase 2: Cultural Uprising of T9 Himmelenger. Win: T9 held + Phase 1 × 2 Accounting. No faction stats. (PP-460, PP-478) |
| Löwenritter | Regency Establishment | PV ≥ 10 + Thread Consciousness (CI) < 50 + IP < 60 + RS > 40 + PI ≥ 4 + successor |

**Universal Victory — Peninsular Sovereignty (all factions):** All 15 playable territories (T1–T14, T17) controlled directly or via effective hegemony (Treaty-bound, Submitted, or institutionally dominated rivals). Accord ≥ 2 in all directly-controlled territories. Peninsular Strain ≤ 6. Held 2 consecutive Accountings. Faction-specific victories above are retained as alternate (easier) paths. See peninsular_strain_v1.md §6.

**Peninsular Partition (Co-Victory, multiplayer):** Both factions collectively control all 15 territories. Each PV ≥ 10. Accord ≥ 2 everywhere. No inter-faction battle preceding 4 seasons. Strain ≤ 6. Both Mandate ≥ 3. See peninsular_strain_v1.md §6.3.


### Territory Consolidation Values (PV)
Per victory_v30.md §1. Total PV = 33 (T16 Schoenland not in territorial play, T15 Askeheim PV = 0).

| T# | Territory | PV | Starting Controller |
|----|-----------|-----|---------------------|
| T1 | Valorsplatz | 5 | Crown |
| T8 | Gransol | 4 | Hafenmark |
| T9 | Himmelenger | 5 | Church of Solmund |
| T12 | Sigurdshelm | 4 | Varfell |
| T3 | Lowenskyst | 3 | Crown |
| T10 | Spartfell | 1 | Hafenmark |
| T14 | Ehrenfeld | 3 | Crown |
| T2 | Kronmark | 1 | Crown |
| T4 | Grauwald | 1 | Varfell |
| T5 | Feldmark | 1 | Crown |
| T6 | Stillhelm | 1 | Crown |
| T7 | Rendstad | 1 | Hafenmark |
| T11 | Halvardshelm | 1 | Varfell |
| T13 | Oastad | 1 | Varfell |
| T17 | Halvarshelm | 1 | Hafenmark |

Starting PV: Crown 14, Hafenmark 7, Varfell 7, Church 5.


### Co-Victory Pairings
Per victory_v30.md §4. All require 2 consecutive Accounting steps except Church+Hafenmark Partition (immediate on mutual agreement).

| Pair | Key Conditions |
|------|---------------|
| Crown + Hafenmark | Crown PV ≥ 12, Hafenmark PV ≥ 12, PI ≥ 7, CI < 50, Crown Mandate ≥ 4, Hafenmark Mandate ≥ 4 | *(PP-561)* |
| Crown + Varfell | Crown PV ≥ 12, Varfell PV ≥ 8, VTM ≥ 3, RS ≥ 50 |
| Varfell + RM | VTM ≥ 4, WA ≥ +2, ≥ 4 territories PT ≤ 1, RS ≥ 40 |
| Hafenmark + RM | Hafenmark PV ≥ 10, ≥ 4 territories PT ≤ 2, PI ≥ 4, RS ≥ 40 |
| Löwenritter + Hafenmark | Löwenritter PV ≥ 8, Hafenmark PV ≥ 8, PI ≥ 4 |
| Church + Hafenmark (Partition) | Crown Mandate ≤ 1, CI ≥ 50, Church ≥ 2 territories, Hafenmark ≥ 3, no military conflict |

Incompatible: Crown + Church, Crown + Löwenritter, Church + Varfell, Church + RM.


### Shared Loss Conditions
Per victory_v30.md §5. RS = 0 (Rupture), IP ≥ 100 + Altonian External Relationship (AER) ≤ 1 (Altonian Conquest), or all factions Stability 0 (Total Institutional Collapse).


### Hollow Victory — DISSOLVED
The Hollow Victory modifier system (Deed-count penalties) has been dissolved with the Deed system (PP-427). In Hybrid mode, BG victory without personal arc resolution is a narrative qualifier per P-32 (see victory_v30.md §9.3).


### Public Instability (PI) Thresholds (PP-501, ED-361 resolved)
PI measures popular dissatisfaction with monarchical governance. Higher PI benefits Hafenmark (PI ≥ 5 required for their victory). PI hurts Crown.

| PI Range | Effect |
|----------|--------|
| 0–4 | Stable. No mechanical effect. |
| 5–9 | Tensions. Crown Domain Actions +1 Ob in territories with PI markers. Hafenmark Parliamentary Manoeuvre −1 Ob. |
| 10–14 | Unrest. Crown Stability check Ob +1 at Accounting. Popular demonstrations — flavour. |
| 15–19 | Revolt. Crown loses 1 territory per season (lowest PV, becomes Uncontrolled after 1-season Political Vacuum per PP-500). Löwenritter coup check if Coup Counter ≥ 2. |
| 20+ | Collapse. Crown elimination at next Accounting unless PI reduced below 20 before then. |

PI advances per existing IP/PI interaction rules. PI markers placed in territories where relevant events fire.
[EDITORIAL: ED-361 — resolved provisionally. Thresholds designed so PI 5 (Hafenmark victory condition) is achievable without triggering Crown crisis. PI 15+ is catastrophic for Crown. Flagged for simulation.]


## Crown Victory Condition — Redesign (ED-109 resolved 2026-04-03)
Crown must make Varfell AND Hafenmark submit OR own their territories outright.
3 pre-met deeds stand unchanged. 2 remaining deeds require active play against other major factions.
[Propagation: update Deed table when design doc revised.]


## Total Domination Victory Path (ED-318 RESOLVED)
Available to all playable factions. Alternate path, no PV requirement met via normal faction path.

| Condition | Threshold |
|-----------|-----------|
| PV held | ≥ 28 (all controllable territory) |
| All rival factions | Stability 0 (eliminated) OR formally Submitted |

**Submission mechanics:** Any faction at Stability 0 that has not been eliminated may formally Submit (declared at Accounting). Submitted faction: removed from victory competition, remains on board as vassal (NPC-controlled, all stats halved rounded down, no independent actions). The Total Domination faction must hold all non-Submitted, non-eliminated rivals at Stability 0 simultaneously for 2 consecutive Accounting steps.

---


## Hollow Victory Mechanics — DISSOLVED (PP-427)
Deed system and Hollow Victory modifiers dissolved. See victory_v30.md §9.3 for Hybrid mode narrative qualifier (P-32).


## Solo/Co-Victory Declaration Priority (PP-524)
If a faction's solo victory conditions and a co-victory pairing conditions are both met simultaneously at the same Accounting step: the declaring faction chooses which path to claim at the start of Accounting Step 12. Choice cannot be changed during that Accounting step. The 2-consecutive-step requirement applies to the declared path.
