# Combat Videogame Architecture — Stress Test (2026-05-01)

**Author:** Claude (orchestrator session)
**Status:** EXPLORATORY — not canon. Output of stress-testing the canonical scene-combat system against videogame-medium variants.
**Trigger:** Jordan asked for extensive stress testing of scene combat in videogame setting (turns/phases/real-time, duels vs group, geography/buildings, multi-character, equipment) — then expanded scope: "we just want to test many ideas many ways using our core engine and rules as their basis. a videogame makes more possible, and moving away from the abstract zone of ttrpg means we have a lot to figure out for both ttrpg and mass battle. also do NERS all directions."

## Method

Each idea evaluated NERS-all-directions:
- **NERS** — Necessary, Elegant, Robust, Smooth (project-canonical criteria)
- **All-directions** — top-down · bottom-up · vertical · diagonal · lateral · horizontal (project-canonical lenses)

Total grid per idea = 6 directions × 4 NERS = 24 cells.

## Chunks

| # | File | Scope |
|---|---|---|
| 01 | `01_variants_acclaimed.md` | Survey of 30+ shipped systems mapped to canonical mechanics. Pirates! / Sekiro / Grandia / XCOM / DD / etc. with adoption fit per architecture. Top-10 picks. |
| 02 | `02_q1_timeshape.md` | Q1 — time-shape of scene combat. 8 candidates (turn-based, phase-locked, RTwP, active-time, real-time, perfect-info, BLiTZ hybrid, Pirates!-stance). |
| 03 | `03_q2_spatial.md` | Q2 — spatial substrate. 5 primary candidates (continuous, square grid, hex, slot, zoned-but-mapped) + S5/S6/S8 extensions. The central question Jordan flagged. |
| 04 | `04_q3_scene_mass.md` | Q3 — scene↔mass battle interface. 8 patterns (pause-zoom, continuous-zoom, hero-as-unit, parallel scenes, commander view, three-mode, post-battle-only, scripted beats). |
| 05 | `05_q4_q5_q6.md` | Q4 action economy · Q5 duel-vs-group architecture trigger logic · Q6 fieldwork bridge. |
| 06 | `06_synthesis.md` | Composite stack, canon impact (~6 rewrites + 8 net-new + 5 extensions + 10 unchanged), phased Godot implementation path, 10 residual risks for Jordan. |

## Headline finding

**Canonical resolution math survives every videogame-medium variant tested.** Combat Pool, weapon TN matrix, damage formula, Wound Interval, Stamina, Threadwork — all preserved.

What breaks is the **TTRPG zone abstraction scaffolding** around the math: zone-mode-switching between scales, modal fieldwork↔combat transitions, three-architecture splits, separate phase models per scale. The cleanest stack drops the scaffolding rather than papering over it.

## Composite stack recommended

| Layer | Choice |
|---|---|
| Time-shape | T2+T4 — canonical phase visualized as Grandia IP gauge, same clock for scene + mass |
| Spatial substrate | S7-hybrid — canonical zones at world scale, sub-zone continuous at scene scale |
| Scene↔mass interface | I1 (MVP) → I4 (v0.2) → I2 (v1.0) phased ship path |
| Combat architectures | A (general) + C (duel). B (DD-slot) dropped. |
| C trigger logic | 6 conditions: Wager / Cultural / Boss / Thread / Hero-Officer / Honor-call |
| Action economy | Canonical pool + Stamina (E1) + Stamina-banking (E6) + posture-as-yield in C only (E7) |
| Fieldwork bridge | F2+F3 — same map continuous + stealth-graduated Exposure ramp |

## Residual risks (require Jordan judgment before canonization)

R1 wound permanence · R2 skill input layer in C · R3 mass three-mode reframe · R4 hero participation default · R5 wager stake range · R6 Fibonacci cap at high attacker counts · R7 friendly fire · R8 fieldwork-tempo shift mechanism · R9 two-architecture sufficiency · R10 IP-gauge actor-count threshold

Detail in `06_synthesis.md §4`.

## Status

EXPLORATORY. None of this is canon. If Jordan ratifies, the canon refactor is described in `06_synthesis.md §2` (file-by-file impact). The TTRPG zone-abstraction removal is the single largest decision; every other decision in the stack is a consequence of that move.

## Cross-references

- `designs/scene/combat_v30.md` — canonical baseline that was tested
- `designs/scene/derived_stats_v30.md` — canonical derived stats used in math
- `designs/provincial/mass_battle_v30.md` — mass-scale canonical baseline; Part A/B/D referenced
- `designs/scene/fieldwork_v30.md` — fieldwork system that bridges via F2+F3
