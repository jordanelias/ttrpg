# Valoria — Current Canonical Surface · **Generation v40**

**The index of which head is live, per subsystem — and nothing else.** Each row names the head and
where its status and open items live. **This file restates no count, figure, ruling text or dated
narrative:** those have owners (the ledger row, the lane handoff, the instrument), and a copy here
goes stale the commit after it is written. Jordan: *"anything that gets pulled up frequently cannot
be hard coded with numbers/values/dates."* Add a pointer, never a paragraph.

Machine-readable twins: `references/canonical_sources.yaml` (SHA-pinned; check it with
`python tools/freshness_gate.py`) and `registers/mechanics_index.yaml`. Heads touched since the
stamp: `python tools/currency_consistency_check.py` (it exits 0 either way — read its output).
Old paths resolve through `references/restructure_ledger.md` via `python tools/pathres.py`. A
ledger id's LAST row is its current state. History of this file: `git log -p CURRENT.md`.

_Last reconciled: 2026-09-22 (rewritten to pointer form; every head re-checked for existence and supersession)._

Design prose is quarantined in `.designs/` (ED-IN-0231). A row that names such a document gives its
**bare filename only**, deliberately: it is reference, not a head, and not to be opened as authority.

| Subsystem | Head | Status and open items |
|---|---|---|
| **THE SEASON LOOP (game code)** | `engine/season/` — RATIFIED, ED-IN-0204 | `python -m engine.season.harness.register --requirements`; runtime registries `engine/season/data/`; Layer-1 conformance ED-IN-0206; lane `registers/handoffs/HANDOFF_IN.md` |
| **THE CODE ARCHITECTURE (Layer 1)** | `architecture/` — RATIFIED, ED-IN-0204 | `skills/layer-conformance/SKILL.md` (Lens B checks `engine/season/` against `architecture/meta/04_CODE_ARCHITECTURE.md`) |
| **The plan** | `workplans/2026-09-18-governance-settlement-behaviour-plan.md` — the single plan, ED-IN-0253 | its §3.1; unit detail `workplans/2026-09-13-work-order.md`; master workplan `workplans/valoria_master_workplan_v7.md` (ED-IN-0216) |
| **Character model / decision layer** | `proposals/2026-09-20-pursuit-basis-worksheet.yaml` — ruled, ED-IN-0261 | ED-IN-0261; conviction split ED-IN-0251 |
| **Personal combat** | `systems/combat/combat_engine_v1/`; typed export `engine/engine_params/combat_engine_v1.json` (round-trip checked in CI) | `registers/handoffs/HANDOFF_PC.md`; design reference `combat_reference_v1.md`, lineage `combat_currency_v1.md` |
| **Mass battle** | `mass_battle_v30.md` + `mass_battle_integration_v30.md` | `registers/handoffs/HANDOFF_MB.md` |
| **Social contest** | `social_contest_v30.md`; kernel `systems/social_contest/sim/contest/` | successor `proposals/2026-09-05-proceedings-subsystem/` is PROPOSED, held back; ownership ruled ED-SC-0033; `registers/handoffs/HANDOFF_SC.md` |
| **Faction / political** | `faction_canon_v30.md`, `faction_layer_v30.md`, `faction_behavior_v30.md`, `faction_state_authoring_v30.md`, `faction_politics_v30.md` | `registers/handoffs/HANDOFF_FA.md`; ED-FA-0008..0023 |
| **Settlement / territory** | `settlement_layer_v30.md` + `settlement_adjacency_v30.md`, `territory_temperaments_v30.md`, `geography_v30.md` | `registers/handoffs/HANDOFF_SE.md`; proposed redesign `governance_play_redesign_v1.md`; hierarchy ruling `scale_hierarchy_v1.md` |
| **Clocks & tracks** | `clock_registry_v30.md` | Truth → Conviction ED-IN-0251 (supersedes ED-IN-0075 for the per-character axis); no code reads the axis yet |
| **Threadwork** | `threadwork_v30.md` + `thread_horizontal_integration_spec.md` | in scope, applications adopted as companion — ED-WR-0010 (last row); `registers/handoffs/HANDOFF_WR.md` |
| **Fieldwork / Investigation** | `fieldwork_v30.md` + `investigation_systems_v30.md` | Interview merge ED-FI-0004; `registers/handoffs/HANDOFF_FI.md` |
| **Scale transitions** | `scale_transitions_v30.md` | ED-IN-0016 |
| **Player agency** | `player_agency_v30.md` | ED-IN-0016 |
| **Articulation** | `articulation_layer_v30.md` | — |
| **NPC behaviour** | `npc_behavior_v30.md` | — |
| **Holonic doctrine** | `holonic_container_doctrine_v1.md` — ED-1083 | — |
| **Propagation spec** | `propagation_spec_v1.md` — ED-1093 | the doc's own §5; `engine_clock` home is ED-1051 |
| **Narrative engine** | `narrative_engine_design_v2_churn.md` — ED-IN-0011 | — |
| **Dice / resolution** | in code: `engine/autoload/dice_engine.py` (`degree_from_net`) | prose tables EVACUATED to the frozen capture `engine/engine_params/params_tables.yaml` (fork ref `c451bcb`) — reference, not the formula |
| **Board game** | EVACUATED to `engine/engine_params/params_tables.yaml` (fork ref `c451bcb`) | — |
| **Godot conversion** | `godot/godot_conversion_strategy_v1.md` — PROPOSED | ED-GO-0001; Gate-0 waits on ED-1051; `registers/handoffs/HANDOFF_GO.md` |
| **Decision policy** | `decision_policy_v1.md` — DRAFT FOR RULING | ED-IN-0113 |
| **Campaign driver** | ⛔ `engine/mc_v18.py` SUPERSEDED by `engine/season/` — do not build here | ED-IN-0226, ED-IN-0227; importer roster `tests/valoria/test_mc_v18_is_deprecated.py` |
| **Key substrate** | ⛔ RETIRED — `FORK:c6e82105` | ED-IN-0232; exact rows in `references/restructure_ledger.md` |
| **Repository state armature** | ⛔ RETIRED — `FORK:1e4c6f4` | ED-IN-0194 |
| **Status dashboard** | ⛔ RETIRED — `FORK:1e4c6f4` | milestone signal is `python tools/m1_acceptance.py --summary` |
| **`deprecated/` tree** | ⛔ RETIRED — `FORK:baf29d5` | frozen ledger fragments live in `registers/archive/` |

**Versioning is not currency.** `_v30` filenames, in-file `## Version:` lines and the `v40`
generation marker are independent axes; only this file and a head's `## Status:` line say what is
current (`CLAUDE.md` §4).
