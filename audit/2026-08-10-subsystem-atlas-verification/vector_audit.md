# Vector audit re-derivation — structural facts per subsystem

Sources: `audit/2026-08-06-vector-audit/structure_audit/structure_register.md`,
`data/structure_metrics.json`, `data/g_code.json`, `data/g_l2.json`,
`00_index.md`, `02_weakness_register.md`, `03_validation_report.md`,
`references/execution_map.json`, `references/execution_trace.json`.
Method: whole-file Read + `python -c json.load` structural summarisation only. No Grep/grep/rg used.
Did NOT open any `*_flow_skeleton_v1.md` file.

## A. Headline scorecard (quoted exactly from `structure_register.md` line 7)

> code-modules=271, import-edges=408, import-cycles=3, code-cut-vertices=21, code-orphans=63,
> cli-entries=89, stub-wired=24; l2-modules=27, wiring-edges=103 raw (45 simple/deduped — the
> cycle/cut-vertex/locality metrics run on the simple graph), l2-cycles=2,
> l2-contract↔code-correspondence=JOINED(13 joined, 13 none, 0 unresolvable, 1 undeclared / 27),
> phantom-producers=0(+0 notional), dangling-emits=1, cross-scale-fraction=0.511.

From `data/structure_metrics.json` `findings.dangling_emit` (3 raw rows, register shows only the
1 canon-grade / non-notional one): `peninsular_strain emits env.crisis` (canon, notional=False);
plus two lower-confidence rows filtered from the prose (`engine_clock` → `mechanical.season_change`,
`scenario_authoring` → `env.crisis`, both `notional=True`, doc:null modules).

## B. Per-subsystem table

Bucketed by import-path prefix from `structure_metrics.json`'s `code` block (orphans/cli/stub_wired/cut_vertices)
and by `doc:` path in `execution_map.json.modules` for L2 attribution. `tools/` and bare package roots
(`systems`, `engine`) are out of scope of "subsystem" but reported where they interleave.

| Subsystem | Orphans | In an import cycle? | Cut-vertex (code)? | Stub-wired | L2 module(s) & status | Reached in real run? |
|---|---|---|---|---|---|---|
| `combat` | 15 | no | no | 0 | `personal_combat` — JOINED | **No.** `executes:false`. mc_v18 never dispatches a combat scene (0/29 slots in the seeded trace) |
| `mass_battle` | 3 | **yes** — `massbattle ↔ units` | **yes** — both cycle members are cut-vertices | 0 | `mass_battle` — **UNDECLARED** (only one of 27) | **Yes** — `executes:true`, 481,653 calls in `loop.s2.factions` (98.7% of all traced calls) |
| `social_contest` | 3 | **yes** — 9-node `contest.*` cycle | 1 (`parliamentary_vote`) | 4 | `social_contest` — JOINED | **Yes** — `executes:true`, but only reached via `emergency_council`; Agon kernel is 1 of 4 games built |
| `factions` | 8 | no | 1 (`faction_action`) | 8 (highest of any subsystem) | `faction_state` JOINED · `faction_politics`, `npc_behavior`, `ci_political` — all NONE | Code executes heavily (1,215+131 calls) but L2 contract `faction_state.executes = False` — a map/trace divergence (see C) |
| `settlements` | 3 | no | 1 (`registry`) | 0 | `settlement_layer` — JOINED | Executes at boot + `loop.s3` (75 + 1,908 calls) though L2 flag says `executes:false` |
| `overview` | 2 | no | 2 (`ms_track`, `season`) | 2 | `peninsular_strain` JOINED · `clock_registry` NONE | Not observed as its own bucket in the trace |
| `world` | 4 | no | no | 2 | `miraculous_event` — JOINED | Executes at `loop.s3` (108 calls) via `insurgency_pipeline`/`npe` — files with **no L2 contract at all** |
| `threadwork` | 6 | no | no | 1 | `threadwork` — JOINED | **No.** `executes:false`, not present in trace |
| `characters` | 3 | no | no | 1 | `territorial_piety`, `piety_track` — both JOINED | `territorial_piety` shows 1+228 calls in `by_contract`, but its code lives under `systems/overview/sim/ci_track.py`, not `systems/characters/` — doc/code split |
| `fieldwork` | 1 | no | no | 2 | `fieldwork_knots` — JOINED | Not observed in trace |
| `articulation` | 0 | no | no | 0 (engine-side `engine.cross_scale.articulation` is stub-wired, see below) | `articulation_layer` — JOINED (code = `engine/cross_scale/articulation.py`) | Not observed (`articulation` L2 row `executes:false`) |
| `npcs` | 0 | no | no | 0 | none (`npc_behavior`'s doc lives in `factions/`, `npc_memory` doc:null) — no folder-native L2 module | No code exists here at all (doc-only subsystem) |
| `ui` | 0 | no | no | 0 | none | No code exists here (doc-only subsystem) |
| `_architecture` | 0 | no | no | 0 | `campaign_architecture` — NONE | No code |
| `victory` | 0 | no | no | 0 | `victory` — JOINED (code = `engine/autoload/victory.py`) | **Yes**, `executes:true`, 384 calls in `loop.victory` |
| `engine` (core) | 1 (`autoload.npc_ai`) | no | **5** (`game_state`, `echo_transport`, `scene_dispatch`, `mc_v18`, `substrate.keys`) | 4 (`npc_ai`, `cross_scale.articulation`, `cross_scale.scene_dispatch`, `mc_v18`) | cross-scale bridges: `combat_bridge`,`parliamentary_bridge`,`echo_transport`,`domain_echo`,`zoom_in_out` all `executes:true` (gated); `handoff_rules`,`scene_dispatch` `executes:false` | Heavily executed (dice_engine, keys, echo_transport, domain_echo all in trace) |
| `tests/sim/mass_battle` (canon MB engine, J2) | 2 | **yes** — 5-node `core.exchange ↔ geometry ↔ hierarchy.units ↔ percell ↔ resolution` cycle | **5** (`equipment`, `hierarchy.units`, `orchestration`, `troop_types.registry`, `workbench.server`) | n/a (not in stub-wired list) | n/a (not an L2 contract path) | **No** — per `execution_trace.json`, the campaign runs `systems/mass_battle/sim/massbattle.py` (the small tree), NOT this canon tree, even though J2 (2026-08-03) ruled the canon tree should be the only one kept |

## C. Named findings a per-subsystem description would be wrong to omit

1. **The dangling emit**: `peninsular_strain` emits Key `env.crisis` with **no consumer anywhere** (canon-grade, not notional) — belongs to `overview`.
2. **Cycle 1** (code, mass_battle): `systems.mass_battle.sim.massbattle ↔ systems.mass_battle.sim.units` — both nodes are *also* cut-vertices, i.e. the whole live battle engine is a 2-node SCC where removing either node disconnects the graph.
3. **Cycle 2** (code, social_contest): 9-node cycle `contest ↔ contest.appraise ↔ contest.armature ↔ contest.dictionaries ↔ contest.faction ↔ contest.modes ↔ contest.resolver ↔ contest.rhetoric ↔ contest.wrapper`.
4. **Cycle 3** (code, tests/sim/mass_battle — the canon MB tree per J2): 5-node cycle `tests.sim.mass_battle.core.exchange ↔ geometry ↔ hierarchy.units ↔ percell ↔ resolution`.
5. **L2 cycle A**: `faction_state ↔ npc_behavior ↔ piety_track ↔ social_contest` — spans factions/npcs(doc-only)/characters/social_contest at the contract-wiring level.
6. **L2 cycle B**: `personal_combat` — a single-node self-referential wiring entry (combat).
7. **Every named cut-vertex** must be attributed correctly: engine core owns 5 (`engine.autoload.game_state`, `engine.cross_scale.echo_transport`, `engine.cross_scale.scene_dispatch`, `engine.mc_v18`, `engine.substrate.keys`); mass_battle owns 2 (`massbattle`, `units` — the cycle members themselves); factions owns 1 (`faction_action`); overview owns 2 (`ms_track`, `season`); settlements owns 1 (`registry`); social_contest owns 1 (`parliamentary_vote`); tests/sim/mass_battle owns 5 (`equipment`, `hierarchy.units`, `orchestration`, `troop_types.registry`, `workbench.server`); `tools.sim_harness.*` owns 4 out of scope; plus L2-layer cut-vertices `faction_state`, `game_director` (doc:null), `npc_behavior` (doc:null).
8. **`mass_battle` is the only one of 27 L2 contracts UNDECLARED** (no `sim_module:` field at all) — the register calls a nonzero UNDECLARED count "itself a regression," but `00_index.md` finding #4 independently verifies against commit `f03357d` that `mass_battle` simply never got the field when the other 26 did — the register's own regression-vs-pre-existing classification is **wrong** for this specific row.
9. **J2 non-execution**: J2 (2026-08-03) ruled `systems/mass_battle/sim/` retired in favor of the `tests/sim/mass_battle/` canon tree, but `execution_trace.json` proves the campaign still runs the small, "retired" `systems/mass_battle/sim/massbattle.py` tree (404,699 + 76,952 calls), not the canon one — every MB-lane balance result is measured on a tree the campaign never executes.
10. **`combat`/`personal_combat` is fully built and ported but structurally unreachable**: 2 of 11 EngineModules GDScript-ported, typed-exported, JOINED at L2 — yet `executes:false` because `combat_bridge` never receives a combat-type scene (all 29 traced scene slots are `contest`); the blocker is a missing *trigger* (canon authorship), not a wiring bug (ED-IN-0123).
11. **`faction_state` executes despite `executes:false`**: the L2 flag says false, but `execution_trace.json`'s `by_contract`/`by_subsystem_path` show `faction_state` firing 6+60+63+7+362 = 498 times and `factions` code firing 1,215+131 times across the seeded run — a direct contradiction between the static map's declared flag and the measured trace that a subsystem description must flag, not silently inherit one source over the other.
12. **`territorial_piety` doc/code split**: its design doc lives in `systems/characters/conviction_track_v30.md` but its code is `systems/overview/sim/ci_track.py` — a cross-subsystem home mismatch, and it *does* execute (1 + 228 calls) despite the L2 map listing `executes:false`.
13. **`world` code executes with no L2 contract routing it at all**: `insurgency_pipeline.py`/`npe.py` fire 108 times in `loop.s3`, but neither module appears as an L2 contract — they run ad hoc, outside the module_contracts.yaml layer entirely (corroborated by the independent 2026-08-08 world-churn audit: insurgency pipeline is "implemented, invoked every season, and STRUCTURALLY UNREACHABLE" because nothing sets `Territory.owner = None`).
14. **`factions` owns the largest stub-wired count (8)**: `charter_liberties`, `hafenmark_equipment`, `home_sanctuary`, `infrastructure_reclamation`, `treaty`, `tribunal`, `varfell_mandate_action`, `varfell_territorial_acquisition` — every one of these routes through `engine.substrate.stubwire`, i.e. explicitly-flagged not-built call sites, not silent stubs.
15. **`combat` owns the largest orphan count (15)**, entirely `combat_engine_v1.*` internals — none imported by anything else in the scanned graph, despite being CLI-runnable (13 of combat's cli_entries are `workbench.*` scripts).
16. **npcs/ui/_architecture have zero code footprint** — confirmed doc-only subsystems (npcs/articulation/ui were the P4-slice-1 "no sim, RULED 1:1" folders); `_architecture`'s only L2 contract, `campaign_architecture`, is `NONE` (disclosed absence, not undeclared).
17. **Phantom producers = 0** — none of the 27 L2 modules consumes a Key that nothing emits (canon-grade).

## D. Staleness caveat — what could have drifted vs. what still holds

**Verified directly**: I diffed git history from 2026-08-06 (the audit's stated date) to today
(2026-08-10). Five commits touched the repo in that window. Of files under the four scanned
code roots (`engine/`, `systems/`, `tools/`, `tests/sim/mass_battle/`), only **two `tools/` files**
changed: `tools/audit_staleness.py` (13-line edit) and the new `tools/observability/build_glossary.py`.
**Zero files changed under `engine/`, `systems/`, or `tests/sim/mass_battle/`.**
`references/module_contracts.yaml` (the L2 source) was last touched 2026-07-29 — before the audit
ran — and `references/execution_map.json` / `execution_trace.json` were last touched 2026-08-03,
also pre-audit. All three postdate the prior (2026-07-22) refresh but predate this one, so this
audit's numbers were already current against them.

**Conclusion: the code-graph numbers (A, B, C above) for every `systems/`, `engine/`, and
`tests/sim/mass_battle/` finding are almost certainly still exactly correct today** — the scanned
trees are byte-identical to what the audit measured. The only drift risk is in the `tools/` bucket
(out of scope for this task's per-subsystem table; `tools.observability.build_glossary` is a new
module not reflected in the 271/89/63/24/21 counts, so the true current tools-side counts are off
by roughly +1 module and possibly +1 CLI entry — immaterial to any `systems/`/`engine/` row).

**What is NOT structural and could be stale regardless**: the L1 vector-layer prose-corpus numbers
(199 design docs, 14,062 cite-edges, P1 FAIL, etc.) — five new commits since 08-06 added substantial
new design prose (`audit/2026-08-08-world-churn-audit/`, `audit/2026-08-06-social-contest-three-lens-audit/`,
`references/glossary/`, and — same-day, 2026-08-10 — 15 new `*_flow_skeleton_v1.md` files under
`systems/`), which the L1 corpus-breadth count (199 of 465 `.md`) would not have counted. That
scorecard is dated and directional only, not re-verified here (out of this task's structural scope,
and per the audit's own disclosure it wasn't whole-repo coverage even on 08-06).

**What is durable by construction, not just by luck**: cycle membership, cut-vertex status, and
stub-wired status are properties of the import graph among files that did not change, so they hold
exactly. The L2 contract↔code join counts (13/13/0/1) hold because `module_contracts.yaml` is
unchanged. The `executes` flags and trace call-counts are pinned to a specific seed
(`trace_seed: 20260803`, 12 seasons) and are reproducible facts about that seed on unchanged code —
they would only be invalidated by a wiring or code change, of which there were none in-scope.
