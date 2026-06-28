# Valoria - Deprecation & Currency Sweep (2026-06-28)

> **Status: WORKING PLAN - for Jordan review. Nothing moved/committed yet.** Produced by a full multi-agent corpus sweep (anchor truth-sheet + 14 subsystem finders + deterministic `git grep` inbound-reference verification). Source data: `tasks/sweep_enriched.json` (128 classified candidates). Every action below is Jordan-vetoable.

Purpose: lock in the *current canonical surface* (what Godot is built from), and archive/deprecate the superseded material around it - so "is combat-proposal-v32 still live?" stops being a question.

## 1. The current canonical set - *this is what Godot builds from*

| Subsystem | Current head |
|---|---|
| **Personal combat** | `designs/scene/combat_engine_v1/  (package; ED-900-904, re-ratified ED-904; D1-D9 ED-1029)` |
| **Mass battle** | `designs/provincial/mass_battle_v30.md  (+ mass_battle_integration_v30.md)` |
| **Social contest** | `designs/scene/social_contest_v30.md  (+ _index, _infill; params/contest.md)` |
| **Faction / political** | `designs/provincial/faction_canon_v30.md + faction_layer_v30.md + faction_behavior_v30.md + faction_state_authoring_v30.md  (overview: designs/factions/faction_systems_overview_v30.md)` |
| **Settlement / territory** | `designs/territory/settlement_layer_v30.md  (+ settlement_adjacency_v30.md, territory_temperaments_v30.md, designs/world/geography_v30.md)` |
| **Threadwork** | `designs/threadwork/threadwork_v30.md  (+ thread_horizontal_integration_spec.md)` |
| **Architecture / Key substrate** | `designs/architecture/key_substrate_v30.md  (+ key_type_registry_v30.md)` |
| **Articulation** | `designs/articulation/articulation_layer_v30.md` |
| **NPC behaviour** | `designs/npcs/npc_behavior_v30.md` |
| **Master workplan** | `designs/audit/2026-06-11-orchestration/valoria_master_workplan_v4.md  (CANON, ratified 2026-06-12)` |
| **Godot conversion** | `designs/audit/2026-06-10-godot-conversion-strategy/godot_conversion_strategy_v1.md  (Lane-C governing spec)` |
| **Board game** | `params/board_game.md  + params/bg/* governing tables` |
| **Dice / resolution** | `params/core.md  + Decision-E continuous/quasibinomial + d+sigma resolver (canonized 2026-05-15)` |

Everything else in a lineage is, by definition, a predecessor. The job below is to make that legible.

## 2. What the sweep found

- **128** flagged files across the corpus (68 dated `designs/audit/` folders are the main proliferation surface).
- **2** ready to deprecate *right now* (already recorded + bannered, just never physically moved).
- **78** superseded exploratory records - safe to archive (referenced only by ledgers / the observability dashboard / generated indexes - *no live citation*).
- **15** look stale but are referenced by live sim/Godot/canon code -> **leave in place**.
- **3** were mis-flagged - they are current heads (`articulation_layer_v30`, `settlement_layer_v30_index`, `faction_politics_v30`) -> **leave**.
- **29** already carry SUPERSEDED banners / are intentional frozen records -> no action.
- **1** stray build artifact (`.pyc`) -> gitignore + delete.

## 3. Bucket A - execute now (safe, tiny, already-decided)

These are recorded as superseded in `canon/supersession_register.yaml` and already carry in-file DEPRECATED banners (added 2026-06-19). Only the physical move (LB-13) was deferred. Inbound refs are register/sim/observability only - safe.

| File | Action | Destination |
|---|---|---|
| `designs/proposals/combat_v31_proposal.md` | git mv | `deprecated/proposals/` |
| `designs/proposals/combat_v32_proposal.md` | git mv | `deprecated/proposals/` |
| `designs/audit/2026-05-28-combat-reframe/ners_verdict_combat_v32.md` | keep (bannered record) | - |

**Register hygiene:** v3 master workplan is superseded by v4 but that fact lives only in v3's in-file banner + `lane_assignments.yaml` - add an explicit `supersession_register.yaml` entry (`valoria_master_workplan_v3.md -> v4`) so `supersession_check()` can see it.

## 4. Bucket B - archive candidates (superseded exploratory records)

Conclusions already consolidated into the current heads; inbound references are noise-zone only (editorial ledger, observability dashboard, generated `valoria_index.sql` / collation reports). **Recommended mechanism: relocate whole dated folders into an `archives/` subtree (`git mv`), not per-file banners** - the repo itself deferred bulk-bannering because prepending banners to large legacy files risks tripping the CI `forbidden_token_gate` (LB-13 note). A folder move is one operation, edits no file content, and preserves history.

**architecture-key-substrate** (2)
- `designs/architecture/canonical_registry.md`
- `designs/architecture/integration_proposal_v30.md`

**balance-sim-validation-audits** (8)
- `designs/audit/2026-05-01-stage-8-sim`
- `designs/audit/2026-05-14-balance-audit/handoff_2026-05-15_v15.md`
- `designs/audit/2026-05-25-r6-death-spiral-reconciliation/findings.md`
- `designs/audit/2026-05-26-pt-treaty-build-readiness/findings.md`
- `designs/audit/2026-05-28-consolidation/24h_work_consolidation.md`
- `designs/audit/2026-05-28-sql-index-and-ners`
- `designs/audit/2026-06-04-attributes-derived-ners`
- `designs/audit/2026-06-05-scale-atomization/scale_atomization_audit.md`

**combat-personal** (14)
- `designs/audit/2026-05-17-scene-combat-contest/battlecon_extraction.md`
- `designs/audit/2026-05-17-scene-combat-contest/planning_v0.md`
- `designs/audit/2026-05-28-combat-reframe/combat-v32-historical-grounding-test.md`
- `designs/audit/2026-05-28-combat-reframe/combat_mechanical_armature.md`
- `designs/audit/2026-05-28-combat-reframe/reframe_blueprint.md`
- `designs/audit/2026-05-28-engine-replacement/engine_replacement_audit.md`
- `designs/audit/2026-05-28-resolution-diagnostic/ners_verdict_combat.md`
- `designs/audit/2026-05-28-resolution-diagnostic/resolution_diagnostic_combat.md`
- `designs/audit/2026-06-06-weapon-physics-ners/weapon_physics_ners_reconciliation.md`
- `designs/proposals/pc_formation_system.md`
- `designs/proposals/weapon_physics_and_concentration_model.md`
- `designs/scene/combat_c4_draft_v0.md`
- `designs/scene/combat_design_v1.md`
- `designs/scene/combat_design_v1_index.md`

**godot-facing** (2)
- `designs/godot/implementation_sequence.md`
- `designs/videogame/godot_architecture_specification.md`

**mass-battle** (7)
- `designs/audit/2026-05-15-mb-comparative-audit/sim/wp1_emit_events.py`
- `designs/audit/2026-05-29-massbattle-sim-foundation`
- `designs/audit/2026-05-29-massbattle-sim-foundation/00_HANDOFF_current.md`
- `designs/audit/2026-06-01-massbattle-stub-wiring/cavalry_shock_design.md`
- `designs/audit/2026-06-01-massbattle-stub-wiring/mb_engine_workplan.md`
- `designs/audit/2026-06-01-massbattle-stub-wiring/resume_audit_workplan.md`
- `designs/audit/2026-06-09-massbattle-comprehensive/massbattle_comprehensive_analysis.md`

**proposals-loose-sessionlogs** (12)
- `designs/arcs/narrative_scenario_chains.md`
- `designs/audit/2026-05-16-multi-session-workplan/workplan.md`
- `designs/proposals/2026-05-16-PC-4.4-unified-success-stress.md`
- `designs/proposals/2026-05-16-faction-audit-followup-plan.md`
- `designs/proposals/2026-05-25-mechanics-integration-v3_1.md`
- `designs/ui/valoria_ui_ux_v4_1_max_audit.md`
- `designs/ui/valoria_ui_ux_v4_2_workplan.md`
- `designs/workplans/valoria_workplan_v3_consolidated.md`
- `designs/workplans/wave1_workplans.md`
- `designs/world/solmund_master_document.md`
- `session-handoff-2026-05-06.md`
- `session_log_archive.md`

**social-contest-debate** (3)
- `designs/audit/2026-05-28-resolution-diagnostic/ners_verdict_social_contest.md`
- `designs/audit/2026-05-28-resolution-diagnostic/resolution_diagnostic_social_contest.md`
- `designs/scene/social_contest_system_v2_index.md`

**supporting-infra** (7)
- `params/threadwork_superseded.md`
- `references/restructure_ledger.md`
- `references/valoria_canonical_definitive_r2.md`
- `references/valoria_complete_systems_r2.md`
- `references/valoria_cross_conversation_review.md`
- `references/valoria_interdoc_audit.md`
- `references/valoria_simulation_review.md`

**terminology-geography** (9)
- `designs/audit/2026-04-30-geography-audit/00_audit_report.md`
- `designs/audit/2026-04-30-geography-audit/01_coord_transform.py`
- `designs/audit/2026-04-30-geography-audit/01_phase2_workplan.md`
- `designs/audit/2026-04-30-geography-audit/04_workplan_reconciliation.md`
- `designs/audit/2026-04-30-terminology-vector-audit/00_workplan.md`
- `designs/audit/2026-04-30-terminology-vector-audit/01_methodology.md`
- `designs/audit/2026-04-30-terminology-vector-audit/02_weakness_register.md`
- `designs/audit/2026-04-30-terminology-vector-audit/03_validation_report.md`
- `designs/audit/2026-05-10-canonical-index-audit/canon_coverage_drift.yaml`

**v30-canonical-integrity** (7)
- `designs/npcs/npc_behavior_system_v1_index.md`
- `designs/scene/combat_design_v1.md`
- `designs/scene/combat_design_v1_index.md`
- `designs/scene/social_contest_system_v2_index.md`
- `designs/ui/valoria_ui_ux_v4_1_max_audit.md`
- `designs/ui/valoria_ui_ux_v4_2_workplan.md`
- `designs/workplans/valoria_workplan_v3_consolidated.md`

**workplan-orchestration** (7)
- `designs/audit/2026-05-16-multi-session-workplan/workplan.md`
- `designs/audit/valoria_systems_workplan.md`
- `designs/audit/valoria_systems_workplan_index.md`
- `designs/audit/valoria_workplan_final.md`
- `designs/audit/valoria_workplan_final_index.md`
- `designs/workplans/valoria_workplan_v3_consolidated.md`
- `designs/workplans/wave1_workplans.md`

## 5. Keep / do-not-touch (looks stale, is load-bearing)

| File | Why keep |
|---|---|
| `designs/provincial/faction_politics_v30.md` | currently canonical; merge-vs-faction_state is open decision J-5 (workplan v4 row#5) — NOT deprecate |
| `designs/territory/settlement_layer_v30_index.md` | index of current head settlement_layer_v30 (canonical_sources L139) |
| `designs/articulation/articulation_layer_v30.md` | current head (canonical_sources L332) |
| `designs/audit/2026-05-17-scene-combat-contest/decisions.md` | referenced by live code: contest.md |
| `designs/audit/2026-05-28-combat-reframe/modifier_system_spec.md` | referenced by live code: orchestration.py,resolution.py,m1_dice_sigma_core.py |
| `designs/audit/2026-05-28-combat-reframe/v32_bout_structural_sanity_sim.md` | referenced by live code: m1_dice_sigma_core.py |
| `designs/audit/2026-05-31-percell-combat/ners_verdict_percell_resolution.md` | referenced by live code: orchestration.py |
| `designs/audit/2026-05-15-mb-comparative-audit/audit.md` | referenced by live code: engine.py,batch_500seed_runner.py |
| `designs/audit/2026-05-15-mb-comparative-audit/plan.md` | referenced by live code: __init__.py,game_state.py,weapon_v2_distance_sim.py |
| `designs/audit/2026-06-01-massbattle-stub-wiring/mb_engine_completeness_audit.md` | referenced by live code: engine.py |
| `designs/audit/2026-06-01-massbattle-stub-wiring/mb_lanchester_design.md` | referenced by live code: config.py,engine.py,lanchester_signature.py |
| `designs/architecture/complete_systems_reference.md` | referenced by live code: 02_canon_constraints.md,mechanics_index.yaml,canonical_sources.yaml |
| `designs/audit/2026-05-14-balance-audit` | referenced by live code: mechanics_index.yaml,altonian_reinforcements.py,council_solmund.py |
| `designs/audit/2026-05-01-stage-10-validation` | referenced by live code: stats_1_7_scale.md |
| `designs/godot/data_serialization_spec.md` | referenced by live code: weapon_resource.gd,module_contracts.yaml |
| `session_log_current.md` | referenced by live code: sim_mass_battle_SIM-MB-04.py,sim_mass_battle_SIM-MB-05.py |
| `session_logs/index.md` | referenced by live code: canonical_sources.yaml,module_contracts.yaml |
| `designs/proposals/stub_infill_plan.md` | referenced by live code: __init__.py,game_state.py |

*MIXED audit folders* (combat-reframe, mb-comparative-audit, massbattle-stub-wiring, percell-combat, scene-combat-contest, stage-10-validation, balance-audit) contain a file the live **sim layer** cites - leave these folders in place until the sim layer is ported for Godot, or move-and-repoint as part of that port.

## 6. The "v40" question - recommendation: **do not mass-rename; ship a CURRENT manifest instead**

Renaming the ~136 `*_v30.md` files to `v40` would touch every co-filed pair (tripping the CI co-file + naming checks), break hundreds of `v30 SS x` citations, and force re-pinning every `canonical_sha__*` in `canonical_sources.yaml`, `mechanics_index.yaml`, and `module_contracts.yaml` - enormous churn, and the v30 docs are *already* the current heads, so it buys no real currency. The legibility you want (one glance -> "what is live?") is delivered far more cheaply by a single human-readable **`CURRENT.md`** manifest (the section 1 table) at repo root, layered over the machine-readable `canonical_sources.yaml`. Reserve **v40 as an earned label** for the next *actual* major revision of a system (e.g. when the combat engine takes its next leap), not a blanket find-and-replace.

## 7. The "stale branch" question - recommendation: **in-tree `archives/` + a pre-cleanup tag, not an off-tree branch**

"Move to a stale branch" decomposes in git into *delete-on-main + keep-a-snapshot* - it does not shrink history, and it would strand the dense web of cross-references (the register's `files_to_recheck`, `git log --follow`, ED citations) that the whole deprecation system relies on. It also contradicts the repo's own rule: *nothing silently deleted; superseded originals stay in git; make currency legible.* Keep stale material in-tree under `archives/` (clearly labelled, still greppable, Godot simply ignores it) and cut a **pre-cleanup snapshot tag** (`git tag pre-deprecation-2026-06-28`) as the one-checkout safety net. That gives the clean-`main` feel without breaking anything.

## 8. Recommended execution sequence

1. **Snapshot:** `git tag pre-deprecation-2026-06-28` (+ work on a branch, not `main`).
2. **Bucket A:** `git mv` combat_v31/v32 proposals -> `deprecated/proposals/`; add the v3->v4 register entry; repoint the ~3 non-noise refs. (1 small commit.)
3. **CURRENT.md manifest:** write the section 1 head table to repo root. (Cheap legibility win - do before Godot.)
4. **Bucket B:** relocate the archive-candidate audit folders -> `archives/audit/<date>/` in staged batches by subsystem; regenerate `valoria_index.sql` / collation reports after. Skip MIXED/keep folders.
5. **Cleanup:** gitignore + remove the stray `.pyc`.
6. Leave Bucket-C/keep items; the open J-5 (faction_politics merge) and combat post-ED-904 residuals stay with the workplan, not this sweep.
