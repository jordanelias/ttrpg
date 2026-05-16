# v16 Gap Analysis — Canonical Mechanics Missing from Strategic Sim
**Date:** 2026-05-15
**Baseline:** mc_v16.py (v15 architecture + v12c RM/Altonian/params)
**Method:** Pattern search against canonical design docs across all 5 workstreams

## Result: 2 present, 27 missing

## D: Settlement Infrastructure
**Sources:** settlement_layer_v30.md §1.2–§1.7, §3, §4.3

| # | Mechanic | Status | Canonical Source | Impact |
|---|---|---|---|---|
| 1 | Religious Buildings (Chapel/Church/Cathedral PT generation) | ✗ MISSING | settlement_layer_v30 §1.5 Axis 1 | **Critical** — Church has no PT counterweight to RM erosion |
| 2 | Templar Stations (+1 CI/season per territory) | ✗ MISSING | settlement_layer_v30 §1.5 Axis 2 | **Critical** — Church CI growth has no PT-independent path |
| 3 | Inquisitor Bases (RM governance +1 Ob) | ✗ MISSING | settlement_layer_v30 §1.5 Axis 3 | High — RM faces no resistance in governed territories |
| 4 | Church Governor (de facto Church territory) | ✗ MISSING | settlement_layer_v30 §1.5 Axis 4 | High — Church has no sub-provincial territorial control |
| 5 | Settlement Order/Prosperity/Population stats | ✗ MISSING | settlement_layer_v30 §1.3 | High — no sub-provincial granularity |
| 6 | Settlement → Province Accord aggregation | ✗ MISSING | settlement_layer_v30 §4.3 | High — settlement instability doesn't feed territory state |
| 7 | Parish Social Services (Stability bonus from Church buildings) | ✗ MISSING | settlement_layer_v30 §1.6 | Medium — Geneva trap mechanic absent |
| 8 | Seizure Ob = 10 − PT − infrastructure modifiers (floor 1) | ✗ MISSING | victory_v30 §3.2, settlement_layer_v30 §1.5 | **Critical** — Mass Seizure uses wrong Ob formula |
| 9 | Pastoral Assumption (Ob 1 governor install in vacuum) | ✗ MISSING | settlement_layer_v30 §1.7 | Medium — Church can't fill governance vacuums |
| 10 | RM Cell Resilience (+1 Ob suppress at 3+ settlements) | ✗ MISSING | settlement_layer_v30 §4.3 | Medium — RM suppression has no distributed-cell modifier |

## A: CI Political
**Sources:** ci_political_v30.md §1–§3, victory_v30.md §3.2

| # | Mechanic | Status | Canonical Source | Impact |
|---|---|---|---|---|
| 11 | Spiritual Weight (SW) per territory | ✓ PRESENT | ci_political_v30 §1 | — |
| 12 | SW-weighted CI generation (Piety Yield × SW factor) | ✗ MISSING | ci_political_v30 §1 | High — CI generation ignores territory ecclesiastical importance |
| 13 | CI milestone 55 (Institutional Reach: +1 Ob to anti-Church) | ✗ MISSING | ci_political_v30 §2 | Medium — Church has no mid-game political protection |
| 14 | CI milestone 80 (Church Ascendant: Seizure −1, PT drift +1) | ✓ PRESENT | ci_political_v30 §2 | — |
| 15 | CI 100 Theocracy Unification Attempt | ✗ MISSING | ci_political_v30 §2.2, victory_v30 §3.2 | **Critical** — Church win condition incomplete |
| 16 | Seizure Ob modifiers from settlement infrastructure | ✗ MISSING | victory_v30 §3.2 | **Critical** — see #8 |

## B: Mass Battle
**Sources:** mass_battle_v30.md §B.2–§B.3, params/mass_combat.md

| # | Mechanic | Status | Canonical Source | Impact |
|---|---|---|---|---|
| 17 | 6-step BG resolution sequence | ✗ MISSING | mass_battle_v30 §B.3 | **Critical** — Military Conquest uses single opposed roll |
| 18 | Unit roster (active: Levy, LightInf, HeavyInf) | ✗ MISSING | mass_battle_v30 §B.2 | **Critical** — no unit composition in battles |
| 19 | Tactic cards (attacker/defender declaration) | ✗ MISSING | mass_battle_v30 §B.3 step 1 | High — no tactical choice in battle |
| 20 | Unit Martial/Endurance/Discipline stats | ✗ MISSING | params/mass_combat.md | High — battle pool construction missing |
| 21 | Fort dice in defense | ✗ MISSING | mass_battle_v30 §B.3 | Medium — fortifications have no battle effect |
| 22 | Territory transfer on battle win | ✗ MISSING | mass_battle_v30 §B.3 step 6 | High — battle outcomes don't change map |

## A: Faction Actions (complete set)
**Sources:** faction_canon_v30.md, victory_v30.md §3.1, peninsular_strain_v30.md §5

| # | Mechanic | Status | Canonical Source | Impact |
|---|---|---|---|---|
| 23 | Crown Initiative 3 modes (Royal Progress / Great Work / Coronation Renewal) | ✗ MISSING | victory_v30 §3.1 | High — Crown has no unique strategic actions |
| 24 | Church Absolution (+1 to target faction at Mandate cost) | ✗ MISSING | faction_canon_v30 Church §3 | Medium — Church diplomacy tool absent |
| 25 | RM Uprising mechanics | ✗ MISSING | victory_v30 §3.4 | High — RM win path incomplete |
| 26 | Varfell Colonist/Transformation | ✗ MISSING | faction_canon_v30 Varfell | Medium — Varfell expansion missing unique action |
| 27 | Hafenmark Trade Network | ✗ MISSING | faction_canon_v30 Hafenmark | Medium — Hafenmark economic engine incomplete |

## C: Personal Combat API
**Sources:** combat_v30.md

| # | Mechanic | Status | Canonical Source | Impact |
|---|---|---|---|---|
| 28 | resolve_pc_action for PC-present battles | ✗ MISSING | combat_v30 §3 | Low for balance sim — affects narrative, not faction outcomes |
| 29 | Pool/Ob from combat_v30 action set | ✗ MISSING | combat_v30 §2 | Low for balance sim |

## Summary by Impact

| Impact | Count | Examples |
|---|---|---|
| **Critical** | 7 | Religious Buildings, Templar Stations, Seizure Ob formula, CI 100, 6-step battle |
| High | 11 | SW-weighted CI, unit roster, territory transfer, Crown Initiative, RM Uprising |
| Medium | 7 | Inquisitor Bases, Parish Services, Church Absolution, Fort dice |
| Low | 2 | PC combat API (narrative layer, not balance-affecting) |

## Structural Diagnosis

Church at 0% win rate traces to gaps #1, #2, #8, #12, #15: no PT counterweight to RM, no PT-independent CI growth, wrong Seizure Ob, and incomplete win condition.

Varfell at 0% traces to gaps #17–22 (mass battle absent — Varfell's military expansion path resolves through a single opposed roll that favors defenders) and #26 (Colonist/Transformation absent).

Hafenmark at 75% (overperformance) traces to gaps #17–22 (single-roll Military Conquest favors the faction with highest Military stat) and #27 (Trade Network absent — Hafenmark wins through military dominance because its economic path isn't modeled).
