# Valoria — Current Canonical Surface · **Generation v40**

**Pointer index: the live head per subsystem, and where its status lives.** Restate no count, figure,
ruling text or dated narrative here; add a pointer, never a paragraph.

Pins: `python tools/freshness_gate.py` (over `references/canonical_sources.yaml`); also
`registers/mechanics_index.yaml`. Heads moved since the stamp: `python tools/currency_consistency_check.py`
(read its output). Old paths: `python tools/pathres.py` (over `references/restructure_ledger.md`). A
ledger id's LAST row is its current state.

_Last reconciled: 2026-10-01._

A row naming a quarantined `.designs/` document gives its **bare filename only**: reference, not a head.

| Subsystem | Head | Status and open items |
|---|---|---|
| **THE SEASON LOOP (game code)** | `engine/season/` — RATIFIED, ED-IN-0204 | `python -m engine.season.harness.register --requirements`; runtime registries `engine/season/data/`; Layer-1 conformance ED-IN-0206; lane `registers/handoffs/HANDOFF_IN.md` |
| **THE CODE ARCHITECTURE (Layer 1)** | `architecture/` — RATIFIED, ED-IN-0204 | `skills/layer-conformance/SKILL.md` (Lens B checks `engine/season/` against `architecture/meta/04_CODE_ARCHITECTURE.md`) |
| **The plan** | `workplans/valoria_master_workplan_v9.md` (+ `_part2`…`_part8`) — RATIFIED, `ED-IN-0286`; the one active plan for every lane; no carve-out | its state index (§3); batches `_part3` §B; ratified and held items `_part8` §K; Jordan items `_part5` §J.2; THE NINE: `python -m engine.season.harness.register --requirements` |
| **Character model / decision layer** | `proposals/2026-09-20-pursuit-basis-worksheet.yaml` — ruled, ED-IN-0261 | ED-IN-0261; conviction split ED-IN-0251 |
| **Personal combat** | `systems/combat/combat_engine_v1/`; typed export `engine/engine_params/combat_engine_v1.json` (round-trip checked in CI) | `registers/handoffs/HANDOFF_PC.md`; design reference `combat_reference_v1.md`, lineage `combat_currency_v1.md` |
| **Mass battle** | `mass_battle_v30.md` + `mass_battle_integration_v30.md` | `registers/handoffs/HANDOFF_MB.md` |
| **Social contest** | `social_contest_v30.md`; kernel `systems/social_contest/sim/contest/` | successor `proposals/2026-09-05-proceedings-subsystem/` ratified as intent (ED-SC-0039; ownership ED-SC-0033), build v9 SC-01; `registers/handoffs/HANDOFF_SC.md` |
| **Faction / political** | `faction_canon_v30.md`, `faction_layer_v30.md`, `faction_behavior_v30.md`, `faction_state_authoring_v30.md`, `faction_politics_v30.md` | `registers/handoffs/HANDOFF_FA.md`; ED-FA-0008..0023 |
| **Settlement / territory** | `settlement_layer_v30.md` + `settlement_adjacency_v30.md`, `territory_temperaments_v30.md`, `geography_v30.md` | `registers/handoffs/HANDOFF_SE.md`; proposed redesign `governance_play_redesign_v1.md`; hierarchy ruling `scale_hierarchy_v1.md` |
| **Clocks & tracks** | `clock_registry_v30.md` | Truth → Conviction: ED-IN-0251 (supersedes ED-IN-0075 for the per-character axis) |
| **Threadwork** | `threadwork_v30.md` + `thread_horizontal_integration_spec.md` | ED-WR-0010 (last row); `registers/handoffs/HANDOFF_WR.md` |
| **Fieldwork / Investigation** | `fieldwork_v30.md` + `investigation_systems_v30.md` | Interview merge ED-FI-0004; `registers/handoffs/HANDOFF_FI.md` |
| **Scale transitions** | `scale_transitions_v30.md` | ED-IN-0016 |
| **Player agency** | `player_agency_v30.md` | ED-IN-0016 |
| **Articulation** | `articulation_layer_v30.md` | — |
| **NPC behaviour** | `npc_behavior_v30.md` | — |
| **Holonic doctrine** | `holonic_container_doctrine_v1.md` — ED-1083 | — |
| **Propagation spec** | `propagation_spec_v1.md` — ED-1093 | the doc's own §5; `engine_clock` home is ED-1051 |
| **Narrative engine** | `narrative_engine_design_v2_churn.md` — ED-IN-0011 | — |
| **Dice / resolution** | in code: `engine/dice_engine/dice_engine.py` (`degree_from_net`) | prose tables EVACUATED to the frozen capture `engine/engine_params/params_tables.yaml` (fork ref `c451bcb`) — reference, not the formula |
| **Board game** | EVACUATED to `engine/engine_params/params_tables.yaml` (fork ref `c451bcb`) | — |
| **Godot conversion** | `godot/godot_conversion_strategy_v1.md` — PROPOSED | ED-GO-0001; Gate-0 waits on ED-1051; `registers/handoffs/HANDOFF_GO.md` |
| **Campaign driver** | ⛔ RETIRED — `FORK:5c5d8ec6` (`engine/mc_v18.py`, deleted at plan position `28-iii`); the head is `engine/season/` | ED-IN-0226, ED-IN-0227 |
| **Decision policy** | `decision_policy_v1.md` — DRAFT FOR RULING | ED-IN-0113 |
