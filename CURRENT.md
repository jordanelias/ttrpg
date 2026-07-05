# Valoria — Current Canonical Surface · **Generation v40**

> **Generation v40** = the consolidated, contracts-bound, Godot-ready generation: the v30 per-system
> flatten **+** universal Key substrate (PP-687) **+** contracts spine v3 (schema-2) **+** combat-engine
> ratification (ED-900–904) **+** descriptor registry **+** master-workplan v4 orchestration. "v40" is a
> *generation marker*, not a filename suffix — the `_v30` files remain (renaming 138 files / ~16k
> citations buys no clarity). Currency is carried here + by each head's `## Status:` line, enforced by
> `tools/ci_generation_consistency.py`.

**This is the single human-readable index of what is live.** When in doubt about whether a doc
is current, start here. Machine-readable source of truth: `references/canonical_sources.yaml`
(SHA-pinned) and `canon/mechanics_index.yaml`. Superseded exploration lives under `archives/`
and `deprecated/` — present for history, *not* canonical.

_Last reconciled: 2026-07-05 (NERS qualitative audit RATIFIED, 12 lane EDs filed, MERGED PR #77;
narrative-engine v1 + v2 "Churn Engine" designs + master workplan v6 + steering reconciliation
ED-IN-0006/ED-IN-0009 — roadmap_state retired to `deprecated/references/`, v5 archived, decision
queue snapshotted — PR #78; previous reconcile 2026-07-04 scene-combat R2 MERGED PR #72 + R3
plan-of-record RATIFIED; 2026-07-02 ED-1083 doctrine + ED-1093 propagation-spec + ED-1094
merge-ratifies convention; 2026-07-01 month-overview + architecture consolidation; 2026-06-28
deprecation & currency sweep + v40 generation declaration). Every row is the head of its lineage;
predecessors are archived._

| Subsystem | Current head |
|---|---|
| **Personal combat** | `designs/scene/combat_engine_v1/` (resolver package; ED-900–904, re-ratified ED-904; D1–D9 ED-1029). **R2 closing-distance/facing/grip/contact redesign (I0–I8) MERGED to main (PR #72, 2026-07-04)** per `designs/audit/2026-07-02-scene-combat-closing-distance-redesign/plan_r1_RATIFIED.md` (+ `i8_capstone_audit.md`). **Next phase: R3 weapon-model consolidation — `designs/audit/2026-07-04-weapon-morphology-granularity/consolidation_v1.md` (RATIFIED plan-of-record; U0→U9 + T-P2 + T5; JD-1…JD-8 open), implementing on PR #76.** Typed Class-C export: `references/engine_params/combat_engine_v1.json` — GENERATED from `config.py` via `tools/export_engine_params.py`, round-trip-checked blocking in CI (ED-1052 seed); the Godot port regenerates from it, never hand-edits |
| **Mass battle** | `designs/provincial/mass_battle_v30.md` (+ `mass_battle_integration_v30.md`) |
| **Social contest** | `designs/scene/social_contest_v30.md` (+ `_index`, `_infill`; `params/contest.md`) — ⚠️ a staged **contest_rebuild** is in flight (Gate 0 ratified 2026-06-30; reserved ED 1055–1079 / PP 800–809; Stage 1a σ-kernel landed as `sim/autoload/sigma_leverage.py`); this row remains the head until a rebuild stage supersedes it |
| **Faction / political** | `designs/provincial/faction_canon_v30.md` + `faction_layer_v30.md` + `faction_behavior_v30.md` + `faction_state_authoring_v30.md` (overview: `designs/factions/faction_systems_overview_v30.md`) |
| **Settlement / territory** | `designs/territory/settlement_layer_v30.md` (+ `settlement_adjacency_v30.md`, `territory_temperaments_v30.md`, `designs/world/geography_v30.md`) |
| **Threadwork** | `designs/threadwork/threadwork_v30.md` (+ `thread_horizontal_integration_spec.md`) |
| **Architecture / Key substrate** | `designs/architecture/key_substrate_v30.md` (+ `key_type_registry_v30.md`) |
| **Architecture / Holonic doctrine** | `designs/architecture/holonic_container_doctrine_v1.md` — CANONICAL (ratified 2026-07-02, ED-1083/ED-1094); cross-maps the container/wrapper/propagation vocabulary onto module_contracts/sim-ladder/Key-substrate/Key-log-parity. Does NOT itself author the propagation-spec transform — see next row |
| **Architecture / Propagation spec** | `designs/architecture/propagation_spec_v1.md` — CANONICAL (ratified 2026-07-02, ED-1093/ED-1094; workplan v5 J-38). Ordering/determinism, aggregate-up, distribute-down, and termination (TERMINATION-ONLY — cross-tick convergence NOT proven) transforms; supplies `engine_clock`'s candidate home doc, but the `doc: null`/[ASSUMPTION] grade in `module_contracts.yaml` stays unflipped until ED-1051 is separately resolved. Open flags tracked in the doc's own §5 (OF-7/OF-B1, D.6/OF-D6, `decay()`, RNG-MODEL-COLLISION, cap constants, ORD-3/ORD-4) |
| **Articulation** | `designs/articulation/articulation_layer_v30.md` |
| **NPC behaviour** | `designs/npcs/npc_behavior_v30.md` |
| **Master workplan** | `designs/workplans/valoria_master_workplan_v6.md` (CANON-PROPOSED 2026-07-05, ED-IN-0009; supersedes v5 → `archives/workplans/` with banner; v4 stays the frozen 06-11/06-22 record. North-Star milestones M1/M2/M3 + tiered decision register §5 — the live decision surface, superseding the 2026-07-01 decision-queue snapshot) |
| **Narrative engine** | `designs/audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md` (PROPOSED 2026-07-05; supersedes-in-part v1 in the same folder — v1 + spec chapters s1–s5 stay normative as amended by `spec/churn_amendments.md`. ⚠️ The F-F/fork-8 Light-Function decision is HELD BACK from merge-ratification — explicit Jordan sign-off required. Executes ED-IN-0003/0004; stages sequenced in workplan v6 §3) |
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
