# Grounding 3 — Threadwork surface map (declared + silent junctures)

## Status: PROPOSED (audit grounding — Jordan review)
_Explorer output, 2026-07-04 planning phase (sonnet lane). Verified against the working tree at
commit `cb227cf`._

## 1. Core mechanics (brief)

Practitioner (Thread Sensitivity ≥30, Approach Training) **Leaps** (`threadwork_v30.md` §2.3) to
perform: **Weaving**, **Pulling**/**Past-Oriented Pulling**, **Locking** (FR), **Dissolution**
(FR), **Mending** (only Coherence-free op). Pool `(Spirit×2)+History+TPS` (PP-616/618/619,
canonical in `params/threadwork.md`). Every op fires **Co-Movement** (§4). Gating tracks:
**Coherence** (10→0, Rendering Crisis §3.7, ED-681) and the world track — named **MS (Mending
Stability)** in threadwork_v30 §5 but **RS (Rendering Stability)** in the newer canonical
`params/threadwork.md` (same track, inconsistent name). `params/threadwork.md` supersedes the
single-axis Ob tables with **Three-Axis Ob** (Depth×Breadth×Distance, PP-622/623). Calamity
consequences graduated geographically by `designs/world/calamity_radiation_v30.md`.
Player-facing decisions: op scale vs Coherence spend; Weave-brittleness vs Pull-transience;
concealment vs Church Attention/CV; Rendering-Crisis recovery gamble (perma −1 TS).

## 2. Declared junctures (file + section)

- **Combat (superseded layer)** — `combat_v30.md` §10 (Leap as Priority-5 full-round, thread
  perception, death/dissolution → Knot rupture; cross-refs companion §6.1, social §9.4b, npc §3.4).
- **Social contest** — `social_contest_v30.md` §9.3 (Weaving in contests, R-65), §9.4 temporal
  axis conflict (PP-351), §9.4b adjudicator thread response (ED-667).
- **Mass battle** — `mass_battle_v30.md` §A.7 (Phase-4 offensive ops, PP-101) + §A.10
  (scale-mapped Ob/Coherence table, EDGE-01–06).
- **Investigation** — `investigation_systems_v30.md` Case Board Thread Layer (ED-680);
  Thread-Read as fieldwork action (TW-05/TW-10, `fieldwork_v30.md` §2.3/§4.5).
- **NPC/conviction** — `npc_behavior_v30.md` §3.4 (→ conviction_track Thread-Event×Scar matrix),
  §4.3 (ED-665 NPC practitioner Coherence thresholds), §8.5/§8.10 priority trees (§8.8 Niflhel
  STRUCK).
- **Faction/political** — conviction_track §1.3b PT drift (ED-676); scale_transitions §3.5/§3.6/
  §5.6 (ED-673); player_agency Step 2b thread-state scenes (ED-674); faction_layer Priority-5
  Thread Domain Action + RS in seasonal clock.
- **Settlement/territory** — settlement_layer §4.4 (thread ops at settlement level), §4.9
  (thread exploitation sites); calamity_radiation matrix; governance_play "Thread" event family.
- **Chargen** — character_histories (Formation 2F mentorship, Catalyst 4E First Leap, Approach
  Training ladder) — implements ED-678's intent, not its literal table.
- **Knots** — knots_v30 + params/threadwork Knot Mechanics (ED-912/773): thread-bonded
  relationships ↔ Coherence recovery/rupture.

## 3. Silent / absent junctures

- **`combat_engine_v1/` (the ratified head)** — zero threadwork; §10 lives only on the
  superseded combat_v30 layer. **ED-911 (open, P1).** No Leap-during-engine-combat, ranged, or
  group combat counterpart.
- **`articulation_layer_v30.md`** — zero Thread/Coherence/Calamity mentions despite being the
  narrative-surfacing layer; no Key/trigger for Gap manifestation, Rendering Crisis, or
  Dissolution witnessing (narratively load-bearing per ED-681).
- **`faction_behavior_v30.md`** — one incidental mention; no mechanical hook into faction AI.
- **`territory_temperaments_v30.md`** — Calamity-adjacency flavor only; no thread-state →
  temperament mechanics.
- **`insurgency_pipeline_v30.md`** — single hit (Community Weaving); founding/presence machinery
  has no thread hooks.
- **Exploration-as-traversal** — passive sensing has a cost (fatigue 2/round, ED-694) but no
  procedure; no travel-mode toggle.

## 4. Horizontal integration spec — promise vs implementation

`thread_horizontal_integration_spec.md` (ED-673–681) targets paths that no longer exist
(`designs/hybrid/`, `designs/systems/`, …). By content: ED-673/674/676/677/680 propagated;
ED-675 implemented as different content; ED-678 concept landed, not the literal table (and the
ED-678 hits in faction_layer are an unrelated reuse of the same number — non-unique ED
numbering); **ED-679 (Thread Warfare NPC AI doctrine) never propagated** and its target faction
(Niflhel) was dissolved. The spec's own "Depends" citations (ED-670–672) have drifted from the
actual sections (now ED-663/664/665).

## 5. Open ledger flags

- **ED-911** (open, P1) — combat resolver thread gap (§3).
- **ED-1010** (open, P1) — per-op Coherence cap homeless; contradicted by mass_battle §A.10
  War-scale −2/op row.
- **ED-1011** (open, P1) — Coherence-0→NPC rule split (params/core PP-261 dead pointer vs
  threadwork §3.7 [PROVISIONAL]); no-Close-Knot case unstated.
- **ED-913** (open, P1) — Thread-Read attribute stale (Attunement vs canonical Spirit pool) in
  params/fieldwork + fieldwork_investigation.
- **ED-414** (open) — Debate co-movement MS+1 timing unconfirmed.
- **ED-931** (open) — dangling clock-registry path citing struck worldbuilding §4.3.
- Archived cross-system verdicts
  (`archives/audit/2026-06-11-threadwork-resolution-diagnostic/…crosssystem_mapping…`): social =
  clean; mass battle + investigation = full-but-record-defective; **scene combat = structural
  gap (ED-911)**.
