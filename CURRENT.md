# Valoria — Current Canonical Surface

**This is the single human-readable index of what is live.** When in doubt about whether a doc
is current, start here. Machine-readable source of truth: `references/canonical_sources.yaml`
(SHA-pinned) and `canon/mechanics_index.yaml`. Superseded exploration lives under `archives/`
and `deprecated/` — present for history, *not* canonical.

_Last reconciled: 2026-06-28 (deprecation & currency sweep). Every row is the head of its lineage;
predecessors are archived._

| Subsystem | Current head |
|---|---|
| **Personal combat** | `designs/scene/combat_engine_v1/` (resolver package; ED-900–904, re-ratified ED-904; D1–D9 ED-1029) |
| **Mass battle** | `designs/provincial/mass_battle_v30.md` (+ `mass_battle_integration_v30.md`) |
| **Social contest** | `designs/scene/social_contest_v30.md` (+ `_index`, `_infill`; `params/contest.md`) |
| **Faction / political** | `designs/provincial/faction_canon_v30.md` + `faction_layer_v30.md` + `faction_behavior_v30.md` + `faction_state_authoring_v30.md` (overview: `designs/factions/faction_systems_overview_v30.md`) |
| **Settlement / territory** | `designs/territory/settlement_layer_v30.md` (+ `settlement_adjacency_v30.md`, `territory_temperaments_v30.md`, `designs/world/geography_v30.md`) |
| **Threadwork** | `designs/threadwork/threadwork_v30.md` (+ `thread_horizontal_integration_spec.md`) |
| **Architecture / Key substrate** | `designs/architecture/key_substrate_v30.md` (+ `key_type_registry_v30.md`) |
| **Articulation** | `designs/articulation/articulation_layer_v30.md` |
| **NPC behaviour** | `designs/npcs/npc_behavior_v30.md` |
| **Master workplan** | `designs/audit/2026-06-11-orchestration/valoria_master_workplan_v4.md` (CANON, ratified 2026-06-12) |
| **Godot conversion** | `designs/audit/2026-06-10-godot-conversion-strategy/godot_conversion_strategy_v1.md` (Lane-C governing spec) |
| **Board game** | `params/board_game.md` + `params/bg/*` governing tables |
| **Dice / resolution** | `params/core.md` + Decision-E continuous/quasi-binomial + d+σ resolver (canonized 2026-05-15) |

## Naming / versioning note

The `_v30` suffix marks the **current** generation of each subsystem — it is not a stale tag.
There is no blanket `v40` rename planned; a new version number is earned by the *next actual major
revision* of a system (e.g. a future combat-engine leap), not by find-and-replace. Keeping the
`_v30` names avoids churning ~136 co-filed pairs, hundreds of `v30 §x` citations, and every
`canonical_sha__*` pin.

See `designs/audit/2026-06-28-deprecation-currency-sweep/deprecation_currency_plan.md` for the
full sweep, the archive rationale, and what was deferred (combat-themed audit folders, pending the
active combat-engine work).
