# Valoria — Current Canonical Surface · **Generation v40**

**Pointer index: the live head per subsystem, and where its status lives.** Restate no count, figure,
ruling text or dated narrative here; add a pointer, never a paragraph.

Pins: `python tools/freshness_gate.py` (over `references/canonical_sources.yaml`); also
`registers/mechanics_index.yaml`. Heads moved since the stamp: `python tools/currency_consistency_check.py`
(read its output). Old paths: `python tools/pathres.py` (over `references/restructure_ledger.md`). A
ledger id's LAST row is its current state.

_Last reconciled: 2026-11-15._

A row naming a quarantined `.designs/` document gives its **bare filename only**: reference, not a head.

| Subsystem | Head | Status and open items |
|---|---|---|
| **THE SEASON LOOP (game code)** | `engine/season/` — RATIFIED, ED-IN-0204 | `python -m engine.season.harness.register --requirements`; runtime registries `engine/season/data/`; lane `registers/handoffs/HANDOFF_IN.md` |
| **THE CODE ARCHITECTURE (Layer 1)** | `architecture/` — RATIFIED, ED-IN-0204 | indexes `architecture/00_ADOPTION_README.md`, `architecture/meta/README.md`; scope: `architecture/meta/04_CODE_ARCHITECTURE.md`'s Status line; check: `skills/layer-conformance/SKILL.md` (Lens B) |
| **The plan** | `workplans/valoria_master_workplan_v12.md` (+ `_part2`…`_part44`, with their `_cont` files) — ratified on merge, `ED-IN-0362`; the one active plan for every lane; no carve-out; what it holds back: its §11.2 | batch → file: the head's §14; the batch table, serial-edge table and file census: `_part2` and its continuations; the open questions: `proposals/2026-11-12-subsystem-audit-suite/master/workplan_v12/V12_FOR_JORDAN.md`; run a batch: `/methodology-execute Batch <handle>`; where it stands: the lane handoff's in-flight row (`registers/handoffs/HANDOFF_IN.md`); v11 and v10 and their v11 handles: `FORK:` and `MOVED` rows in `references/restructure_ledger.md`; THE NINE: `python -m engine.season.harness.register --requirements` |
| **Strife flows (design)** | `proposals/2026-11-04-strife-flows/00_MASTER.md` (the master) + `proposals/2026-11-04-strife-flows/01_STRIFE_KINDS_DRAFT.md` (the kind list) — RATIFIED, ED-IN-0316; reference, not a mechanism | instrument `python -m engine.season.harness.strife <seasons> <seed> ...` (`engine/season/harness/strife.py`, `strife_moves.yaml`; `--strands` adds the world-reading block; the readings: `engine/season/queries/world_q.py`, `rosters.yaml: strife_kinds`); build positions CR-72 to CR-80: v11's `_part16` at `FORK:3f443bab:workplans/valoria_master_workplan_v11_part16.md`, their v12 items by `git grep -n 'CR-7' workplans/valoria_master_workplan_v12*.md`; lane `registers/handoffs/HANDOFF_IN.md` |
| **Character model / decision layer** | `proposals/2026-09-20-pursuit-basis-worksheet.yaml` — ruled, ED-IN-0261 | ED-IN-0261; conviction split ED-IN-0251 |
| **Personal combat** | `modules/combat/`; typed export `engine/engine_params/combat_engine_v1.json` (round-trip checked in CI) | `registers/handoffs/HANDOFF_PC.md`; design reference `combat_reference_v1.md`, lineage `combat_currency_v1.md` |
| **Mass battle** | `mass_battle_v30.md` + `mass_battle_integration_v30.md` | B10-12's held residue (CR-12, CP-T04-04, CP-T04-10) in v11's B10-Z (`FORK:1b7c2f87:workplans/valoria_master_workplan_v11_part3.md`), their v12 items by `git grep -n 'CR-12' workplans/valoria_master_workplan_v12*.md`; CR-12's design `proposals/2026-11-08-cr12-melee-attrition-design.md`; `registers/handoffs/HANDOFF_MB.md` |
| **Social contest** | `social_contest_v30.md`; kernel `systems/social_contest/sim/contest/` | successor `proposals/2026-09-05-proceedings-subsystem/` ratified as intent (ED-SC-0039; ownership ED-SC-0033), SC-01 built, its residue is carried by v12's Batch B24p-sc-proceeding and Batches B24 to B28 (`git grep -n 'SC-0' workplans/valoria_master_workplan_v12*.md`; v11's text at `FORK:1b7c2f87:workplans/valoria_master_workplan_v11_part4.md` and `_part3.md`); `registers/handoffs/HANDOFF_SC.md` |
| **Faction / political** | `faction_canon_v30.md`, `faction_layer_v30.md`, `faction_behavior_v30.md`, `faction_state_authoring_v30.md`, `faction_politics_v30.md` | `registers/handoffs/HANDOFF_FA.md`; ED-FA-0008..0023 |
| **Settlement / territory** | `settlement_layer_v30.md` + `settlement_adjacency_v30.md`, `territory_temperaments_v30.md`, `geography_v30.md` | `registers/handoffs/HANDOFF_SE.md`; proposed redesign `governance_play_redesign_v1.md`; hierarchy ruling `scale_hierarchy_v1.md` |
| **Clocks & tracks** | `clock_registry_v30.md` | Truth → Conviction: ED-IN-0251 (supersedes ED-IN-0075 for the per-character axis) |
| **Threadwork** | `systems/threadwork/sim/` (the oracle; Coherence per ED-WR-0010); design intent `threadwork_v30.md` (Part 3 superseded), `threadwork_applications.md`, `thread_horizontal_integration_spec.md` | ED-WR-0010 (last row); `registers/handoffs/HANDOFF_WR.md` |
| **Fieldwork / Investigation** | `fieldwork_v30.md` + `investigation_systems_v30.md` | Interview merge ED-FI-0004; `registers/handoffs/HANDOFF_FI.md` |
| **Scale transitions** | `scale_transitions_v30.md` | ED-IN-0016 |
| **Player agency** | `player_agency_v30.md` | ED-IN-0016 |
| **Articulation** | `articulation_layer_v30.md` | — |
| **NPC behaviour** | `npc_behavior_v30.md` | — |
| **Wrapper doctrine (ARCHIVED, Key-based)** | `holonic_container_doctrine_v1.md` — ED-1083 | — |
| **Propagation spec** | `propagation_spec_v1.md` — ED-1093 | the doc's own §5; `engine_clock` home is ED-1051 |
| **Narrative engine** | `engine/season/harness/` — `storybar.py`, `chronicle.py`, `strife.py`, `arc.py` (readings over the log, never carriers: ED-IN-0225); design intent `proposals/2026-11-04-strife-flows/00_MASTER.md` | ED-IN-0011 (history); ED-IN-0232; `registers/handoffs/HANDOFF_WR.md` |
| **Dice / resolution** | in code: `engine/dice_engine/dice_engine.py` (`degree_from_net`) | prose tables EVACUATED (fork ref `c451bcb`); the capture `engine/engine_params/params_tables.yaml` was retired (`FORK:` row) — not the formula |
| **Board game** | EVACUATED (fork ref `c451bcb`); the capture `engine/engine_params/params_tables.yaml` was retired (`FORK:` row) | — |
| **Godot conversion** | `architecture/meta/04_CODE_ARCHITECTURE.md` §C.12 (RATIFIED, the Godot mapping); the port gate: batch `B41-go-port-gate` of the active master workplan; `godot/godot_conversion_strategy_v1.md` — PROPOSED, intent only | ED-GO-0001; ED-GO-0002 (the engine version); `registers/handoffs/HANDOFF_GO.md` |
| **Campaign driver** | ⛔ RETIRED — `FORK:5c5d8ec6` (`engine/mc_v18.py`, deleted at plan position `28-iii`); the head is `engine/season/` | ED-IN-0226, ED-IN-0227 |
| **Decision policy** | `decision_policy_v1.md` — DRAFT FOR RULING | ED-IN-0113 |
