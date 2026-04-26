# VALORIA — Clock Registry Staleness Report
## Addendum to Holistic Audit
## File: designs/systems/clock_registry_v30.md (106 lines)
## Last updated on GitHub: 2026-04-13 — but content is stale relative to April 14 work

---

## Summary: 23 discrete stale items across 6 categories

---

## Category 1: Shared Clocks (4 items)

| # | Current | Should Be | Source |
|---|---------|-----------|--------|
| 1 | CI: "0–75 (freeze ceiling)" | 0–100 (no freeze; Unification at 100) | tc_political_redesign_v30 §0 — **status PROPOSAL** |
| 2 | CI source: "victory_architecture_v1.md §7" | tc_political_redesign_v30.md / peninsular_strain_v1.md | File renamed + system redesigned |
| 3 | IP start: 5 | 20 | peninsular_strain_v1 §4 (confirmed, committed) |
| 4 | PI row exists (0–20, start 7) | **STRIKE entire row.** Replace with Political Stability (0–10, start 0, ↑ bad) | peninsular_strain_v1 §4 (PP-403 repealed) |

**Note:** Item 1 depends on tc_political_redesign_v30 acceptance. If still PROPOSAL, flag as provisional.

## Category 2: Struck Tracks (4 items)

| # | Track | Status | Source |
|---|-------|--------|--------|
| 5 | AER (Altonian Ecclesiastical Accord) | STRUCK | canonical_definitive_r2 §Struck |
| 6 | Intel Advancement Counter | STRUCK | canonical_definitive_r2 §Struck |
| 7 | Popular Will (PW) | STRUCK | canonical_definitive_r2 §Struck |
| 8 | Intelligence stat row | STRUCK — Intel replaced by fieldwork Investigation + VTM | canonical_definitive_r2 §3.1 |

## Category 3: Missing Tracks (5 items)

| # | Track | Range | Start | Source |
|---|-------|-------|-------|--------|
| 9 | Political Stability | 0–10 | 0 | peninsular_strain_v1 §4 |
| 10 | Accord (per territory) | 0–4 | Capitals 4, home 2, conquest 1 | peninsular_strain_v1 §2 |
| 11 | Territory Value | 0–5 (Askeheim = 0) | Crown 12 total, Hafenmark 6, Church 5, Varfell 6 | peninsular_strain_v1 §1 |
| 12 | Spiritual Weight (per territory) | 0–5 | Fixed per territory (T9=5, T8=3, T14=3, others 1–2, T15=0) | tc_political_redesign_v30 §1 |
| 13 | Knot count (personal) | 0–floor(Bonds/2)+1 | 0 | PP-632, params_threadwork §Knots |

## Category 4: Incorrect Values (5 items)

| # | Track | Current | Correct | Source |
|---|-------|---------|---------|--------|
| 14 | MS start | "TTRPG: 60 / BG: 72" | 72 (single value — videogame only) | Jordan directive: videogame only |
| 15 | Disposition range | "−3 to +5" | −4 to floor(Bonds/2)+1 | PP-632 |
| 16 | Stamina formula | "Endurance + History + 1 − armour" | End + 1, min 2 (History STRUCK per PP-611) | PP-611, params_combat |
| 17 | Piety range | "0–5" | 0–4 (per J-7 if confirmed) or remains 0–5 | J-7 PENDING |
| 18 | Prosperity range | "1–7" | 0–4 (per canonical_definitive_r2) | canonical_definitive_r2 §2.1 |

## Category 5: Stale Source References (4 items)

| # | Current Reference | Correct Reference |
|---|------------------|-------------------|
| 19 | victory_architecture_v1.md | victory_v30.md + peninsular_strain_v1.md |
| 20 | fieldwork_design_v1.md | fieldwork_v30.md |
| 21 | bg_v05 §Standing | board_game_v30.md |
| 22 | geography_design.md | geography_v30.md |

## Category 6: Mandate Floor (1 item)

| # | Current | Correct | Source |
|---|---------|---------|--------|
| 23 | Mandate: "1–7 (BG: floor 1)" | 0–7 (0 = subjugated) | canonical_definitive_r2 §3.1 |

---

## Recommended Action

**Safe to commit now** (confirmed canonical changes): Items 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 16, 19, 20, 21, 22, 23 (17 items).

**Requires J-7 decision first:** Items 17, 18 (territory scale).

**Requires tc_political_redesign acceptance:** Items 1, 2, 11, 12 (CI ceiling, source, TV, Spiritual Weight).

---

## Interdependency Map

```
clock_registry_v30.md depends on:
├── peninsular_strain_v1.md (Political Stability, Accord, IP start, PP-403 repeal)
├── tc_political_redesign_v30.md (CI ceiling, Spiritual Weight, CI milestones)  [PROPOSAL]
├── PP-632 (Disposition, Knots)  [APPLIED]
├── PP-611 (Stamina History struck)  [APPLIED]
├── victory_v30.md (Territory Value, victory conditions)
├── fieldwork_v30.md (Exposure, Cover, Evidence Track)
├── params_core.md (all personal track formulas)
├── params_combat.md (Stamina, Wounds)
└── J-7 decision (territory scale 0–4 vs 0–5)
```
