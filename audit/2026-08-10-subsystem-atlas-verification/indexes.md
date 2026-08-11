# Independent re-derivation: systems/ subsystem homing from the three registries

Method: whole-file Read of `registers/mechanics_index.yaml` (1037 lines), `references/canonical_sources.yaml`
(479 lines), `CURRENT.md` (183 lines) — no grep, no pattern search. No `*_flow_skeleton_v1.md` file was
opened.

Actual mechanic-entry count in `mechanics_index.yaml`'s `mechanics:` map, counted by hand while reading:
**90** (primitives 12, services 6, personal 13, thread 13, provincial 26, territory 4, peninsular 7,
world 5, cross_scale 4). The file's own `drift_report.mechanics_total: 70` is stale — consistent with
the file's own `freshness_note` admission that the combat entry was hand-patched without a file-wide
re-authoring pass. This mismatch is itself a finding: even the registry's self-reported count cannot be
trusted.

## Per-subsystem derivation

For each of the 15 `systems/` folders: canonical head doc(s) named (from `canonical_sources.yaml`
`systems:`/top-level entries, cross-checked against `CURRENT.md`'s table), mechanic count attributed by
`mechanics_index.yaml` (counting a mechanic to a folder when its `canon_sources` and/or `sim_module`
path resolves into `systems/<folder>/`), whether `canonical_sources.yaml` itself names any non-doc
code/sim pointer (as opposed to a bare `design_doc` + SHA pin), and whether `CURRENT.md`'s head-row
table carries a row for it.

| Folder | canonical_sources.yaml head doc(s) | mechanics_index count (canon-doc / sim-in-folder) | canonical_sources.yaml code pointer? | CURRENT.md row? |
|---|---|---|---|---|
| `_architecture` | complete_systems_reference, campaign_architecture(+index), scale_transitions, derived_stats, conflict_architecture, key_substrate, key_type_registry, holonic_container_doctrine, propagation_spec, player_agency(+index), videogame_mode_spec(+index) | 9 mechanics cite an `_architecture` doc as canon (game_state_service, season_manager_service, scene_slate_service, npc_ai_service, domain_echo, zoom_in_out, handoff_rules, season_loop, accounting_cascade) — **but every one of their `sim_module` paths points to `engine/autoload/` or `engine/cross_scale/`, never into `systems/_architecture/`** (no such sim dir is ever referenced) | No — only `design_doc` + SHA pins throughout | Yes — multiple rows (Key substrate, Holonic doctrine, Propagation spec, Scale transitions, Player agency, Repository state armature, Decision policy) |
| `articulation` | articulation_layer_v30.md | 1 primary (articulation_layer); 2 more (beliefs, knots) cite it as one of several canon fragments. articulation_layer's own `sim_module` is `engine/cross_scale/articulation.py` — outside the folder | No | Yes — "Articulation" row |
| `characters` | conviction_track(+index), faction_succession_split(cross-listed), character_generation_questionnaire, character_histories(+index+infill), conviction_taxonomy, conviction_migration_roster, conviction_axis_matrix | 4 cite a characters doc as canon (conviction_scar full; ci_track, mass_seizure, restoration_movement partial/multi-doc). Separately, 3 mechanics (certainty_track, companion, beliefs) have `sim_module` **inside** `systems/characters/sim/` despite their canon doc living in `engine/params/core.md`, `godot/scene_tree_architecture.md`, and fieldwork/social_contest/articulation respectively | No | **No row.** No "Characters"/"Conviction" row anywhere in the head-row table — conviction content is only referenced in passing inside the "Clocks & tracks (cross-cutting)" row (the Truth-Track rename note) |
| `combat` | combat_reference_v1.md (+ resolution_engine field) | 1 (combat) — fully specified: canon `systems/combat/combat_engine_v1/`, params `config.py`, sim `systems/combat/combat_engine_v1/`, `godot_home`, `test_status: validated_pc` | **Yes** — the only subsystem where `canonical_sources.yaml` itself names a code path: `resolution_engine: "systems/combat/combat_engine_v1/"` + `resolution_engine_canonical_status` | Yes — "Personal combat" row (longest in the table) |
| `factions` | faction_systems_overview, faction_layer, tc_political(ci_political), faction_behavior, faction_state_authoring, political_dynamics_keys_migration, faction_canon_consolidation, faction_politics(+index), faction_succession_split, factions(factions_personal), fractional_province_ownership | ~21 mechanics have `sim_module` inside `systems/factions/sim/` (royal_progress, great_work, coronation_renewal, excommunication_action, absolution, council_solmund, charter_of_liberties, varfell_mandate_action, varfell_territorial_acquisition, infrastructure_reclamation, home_sanctuary_t9, mass_seizure, crown_treaty, treaty_expiration, parliamentary_transfer, faction_action_dispatch, govern, muster, excommunication_tribunal, military_conquest) — several of these (`hafenmark_equipment`≠factions actually mass_battle; `royal_progress`/`great_work`/`coronation_renewal`/`varfell_*`/`treaty_expiration`/`parliamentary_transfer`) cite `audit/2026-05-14-balance-audit/...` as canon, not a `systems/factions/` doc — the registry has not caught up to the docs `canonical_sources.yaml` shows as since-ratified (`parliamentary_transfer_v18`, `treaty_expiration_v18`) | No | Yes — "Faction / political" row |
| `fieldwork` | investigation(+index), fieldwork(+index+infill+bg+bg_infill+hybrid+hybrid_infill+editorial+exploration+exposure+godot+investigation+rationale+socializing+summary) | 5 (fieldwork, investigation_npe, disposition_track, evidence_track, knots — knots' `unified_canon_target` resolves its 9-fragment canon spread to `systems/fieldwork/knots_v30.md`) | No | Yes — "Fieldwork / Investigation" row |
| `mass_battle` | mass_combat(mass_battle_v30+index+infill), military_layer, mass_battle_integration | 5 sim-in-folder (mass_battle, units, tactic_cards, altonian_reinforcements, hafenmark_equipment) | No | Yes — "Mass battle" row |
| `npcs` | character_canon_consolidation, npc_relational_graph, companion_spec, edeyja_npc, npc_roster(+index+infill), npc_behavior(+index+infill), baralta | **0** — no mechanic in `mechanics_index.yaml` cites any `systems/npcs/` path in either `canon_sources` or `sim_module`. `npc_ai_service` (the mechanic that conceptually should be "NPC AI") is canon'd to `systems/_architecture/complete_systems_reference.md#part-1` and sim'd to `engine/autoload/npc_ai.py` — neither touches `systems/npcs/` | No | Yes — "NPC behaviour" row (doc-covered, but zero mechanics-registry linkage) |
| `overview` | clock_registry(+infill), peninsular_strain(+index) | 7 sim-in-folder (ms_baseline_decay, season_loop, accounting_cascade, ci_track, rs_track, ms_track, ip_track) — of these, only `ip_track` and `ms_baseline_decay`/`ms_track` have a canon doc that is itself in `overview` or `engine`; `season_loop`/`accounting_cascade` canon to `_architecture`, `ci_track` canons to `characters`, `rs_track` canons to `threadwork`. overview is structurally a **sim-implementation folder for mechanics canon'd elsewhere** | No | Yes — "Clocks & tracks (cross-cutting)" row |
| `settlements` | territories(settlement_layer+political_hierarchy+index+adjacency+fractional+march_layer), settlement_layer, territory_temperaments | 4, fully consistent canon+sim (settlement_state, infrastructure, territory_adjacency, territory_temperaments) | No | Yes — "Settlement / territory" row |
| `social_contest` | **No `sources:` entry at all** — a large comment block (lines ~143–152) documents SHA-pin *provenance conventions* for "social_debate"/`social_contest_v30_index.md` but there is no actual `design_doc:`/SHA-pin entry for social_contest anywhere in the file | 3 sim-in-folder (social_contest, parliamentary_vote, parliamentary_stay). A 4th, `excommunication_tribunal`, canons to social_contest but sims to `systems/factions/sim/tribunal.py` | No | Yes — "Social contest" row (extensive) |
| `threadwork` | threadwork_v30.md, thread_horizontal_integration_spec(+index) | 15 sim-in-folder, fully consistent canon+sim (coherence_zero_transition, ed_301_orthogonality, thread_leap, thread_weaving, thread_pulling, thread_past_pulling, thread_locking, thread_dissolution, thread_mending, collective_thread_operations, opposing_thread_operations, coherence_track, co_movement, rendering_stability, threadcut_beings) | No | Yes — "Threadwork" row |
| `ui` | ui_ux_v4.md (+ `_1`) | **0** — no mechanic cites any `systems/ui/` path | No | **No row.** No "UI" row anywhere in the head-row table |
| `victory` | victory_v30.md | 2 cite it as (partial) canon (victory_check_service, peninsular_sovereignty) — **both have `sim_module` in `engine/autoload/victory.py`, never in `systems/victory/`** — no sim path under the folder is ever named | No | Yes — no dedicated "Victory" row as such, but GD-1/victory content is folded into other rows' prose (mass_seizure canon cites `systems/victory/victory_v30.md#section-3-2`; the doc itself is never a row header) — **reassessed: there is in fact no row titled "Victory"/"Peninsular sovereignty" in the table; it is absent** |
| `world` | ms_trajectory, narrative_voice_canon, solmund_voice, solmund_philosophy, solmund, solmund_artifacts, miraculous_event, baralta(cross-listed npcs), calamity_radiation(+infill), geography(+infill, cross-listed under territories) | 4 sim-in-folder (restoration_movement, miraculous_event, insurgency_pipeline, npe) + 1 explicit orphan (scenario_authoring: canon `[]`, sim `null`) housed at `scale: world` but pointing nowhere | No | **No row.** No "World" row in the head-row table; `geography_v30.md` is cited only parenthetically inside the "Settlement / territory" row |

## A. Fully-homed (head doc + mechanics + code pointer, code living inside the folder)

**8 subsystems:** `combat`, `threadwork`, `fieldwork`, `social_contest`, `factions`, `mass_battle`,
`settlements`, `overview`.

(`combat` is the only one where `canonical_sources.yaml` itself names the code path explicitly via
`resolution_engine:`; the other 7 qualify only through `mechanics_index.yaml`'s per-mechanic
`sim_module` field pointing into `systems/<folder>/sim/`.)

## B. Doc-only (no code pointer named inside the folder anywhere)

**5 subsystems:** `_architecture`, `articulation`, `victory`, `ui`, `npcs`.

- `ui` and `npcs`: zero mechanics-index entries at all — no code pointer of any kind, in or out of the
  folder.
- `_architecture`, `articulation`, `victory`: each has mechanics whose *canon doc* lives in the folder,
  but every one of those mechanics' `sim_module` redirects **out** of the folder — to `engine/autoload/`,
  `engine/cross_scale/`, or (for victory) `engine/autoload/victory.py`. Structurally these three folders
  are doc-homes for code that actually lives under `engine/`.

## C. No CURRENT.md row, and/or cross-registry disagreement

**4 subsystems have no CURRENT.md head row at all:** `characters`, `ui`, `npcs`, `world`. (`ui` and
`npcs` are also in bucket B; `characters` and `world` both have real per-folder sim code but no row.)

**Mechanic-level canon-doc-vs-sim-module disagreements found** (canon_sources folder ≠ sim_module
folder for the same mechanic):
1. `excommunication_tribunal` — canon `systems/social_contest/...`, sim `systems/factions/sim/tribunal.py`.
2. `military_conquest` — canon `systems/mass_battle/mass_battle_v30.md`, sim `systems/factions/sim/faction_action.py`.
3. `npe` — canon `systems/fieldwork/investigation_systems_v30.md`, sim `systems/world/sim/npe.py`.
4. `season_loop` / `accounting_cascade` — canon `systems/_architecture/campaign_architecture_v30.md`, sim `systems/overview/sim/`.
5. `ci_track` — canon `systems/characters/conviction_track_v30.md`, sim `systems/overview/sim/ci_track.py`.
6. `rs_track` — canon `systems/threadwork/threadwork_v30.md`, sim `systems/overview/sim/rs_track.py`.
7. `beliefs` — canon spans fieldwork + social_contest + articulation, sim in `systems/characters/sim/beliefs.py`.
8. `companion` — canon `godot/scene_tree_architecture.md` (outside `systems/` entirely), sim `systems/characters/sim/companion.py`.
9. `parliamentary_transfer` / `treaty_expiration` — `mechanics_index.yaml` still cites the pre-ratification
   `audit/2026-05-14-balance-audit/...` path as canon, while `canonical_sources.yaml` shows both were
   subsequently canonized to proper `systems/factions/` docs (`parliamentary_transfer_v18`,
   `treaty_expiration_v18` entries) — the two registries disagree about currency, not just folder.
10. `social_contest` itself — `mechanics_index.yaml` and `CURRENT.md` both treat `social_contest_v30.md`
    as the live head, but `canonical_sources.yaml` carries no actual `sources:` entry for it at all
    (only a comment block) — the machine-readable registry that's supposed to be *the* SHA-pinned
    source of truth is silent on this subsystem's head doc.

## D. Orphan mechanics — unattributable to any of the 15 `systems/` folders

**10 mechanics** whose `canon_sources` and `sim_module` both resolve outside every `systems/` subfolder
(into `engine/`, `registers/`, or nowhere):

- The 8 dice/pool primitives: `die_rule_d10`, `tn_values`, `obstacle_scale`, `degrees_of_success`,
  `continuous_engine_quasibinomial`, `pool_minimum`, `net_successes_floor`, `momentum` — canon
  `engine/params/core.md`, sim `engine/autoload/dice_engine.py`.
- `mechanics_registry_service` — canon `registers/mechanics_index.yaml` (the file citing itself), sim
  `engine/autoload/registry.py`.
- `scenario_authoring` — canon `[]` (explicitly empty — "no home doc exists"), sim `null` (explicitly
  "zero code presence anywhere"); scaled `world` but functionally homeless by the entry's own admission.

These primitives/services are the base substrate the mechanics-index's own `scales:` reference block
calls `primitive`/`service` — by the schema's own design they were never meant to belong to a
subsystem folder, but the task asks for exactly this: they are real orphans relative to the 15-folder
partition.
