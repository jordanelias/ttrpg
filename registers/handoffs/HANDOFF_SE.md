# Handoff — SE (Settlements)

**Pointer index.** Every row names where its fact lives — a ledger id (its LAST row governs), a `path` or `path:line`, or a command to run. Restate no count, status or date of state here. Narrative: `registers/handoffs/HANDOFF_SE_history.md`.

## Open
| item | where it lives | next step |
|---|---|---|
| Matter/works proposal (`nearest_store`, body gate, `works`/`found`) — RATIFIED AS INTENT (`ED-SE-0053`); IN-28's cost and holder and SE-03's MW-5 landed at B-K (`c8d1db3a`); the closer (`raze`) landed at B-R (`68eaaa41`); the residue is the works' producer | `ED-SE-0053`; `engine/season/hole_register.yaml` H-166 (limit 3), H-228 (`raze`'s limits), H-165; `registers/editorial_ledger_in.jsonl` ED-IN-0297 (needs_jordan, where a works comes from) | the producer waits on ED-IN-0297; nothing else in the proposal exists until built with its test |
| Built-world ontology proposal (Site/Rung fabric-address, fortification bands) — superseded in part by `ED-SE-0053` and absorbed (fortification is `Site.condition`) | `ED-SE-0052`; `ED-SE-0053` | nothing to rule; H-166 limit 3 and H-211 carry the residue |
| MW-11 RED (crossing predicate downward-only; nothing raises a body); MW-5 is a test over H-125's arms | `ED-SE-0053`; `engine/season/hole_register.yaml` H-211 (MW-11), H-125; `engine/season/tests/test_se03_body_bands.py` (MW-5) | MW-11 is measured, not in the tree (a red test may not be skipped); r2 section A.4's signed body step and an upward check in `_crossings` are its fix, a position of their own |
| B-T CLOSED `2c6684e6` (commits `befce041..2c6684e6`, PR #503) | `engine/season/hole_register.yaml` H-170 (the two arms' readings), H-171 (`Rung.envelope` stopped at its design step), H-241 (`field_provisioning`, shipped OFF; the decisions owed at the flip); `modules/settlements/` (eight entries); `engine/season/tests/test_levy_feed.py`, `engine/season/tests/test_settlements_module.py`; `workplans/valoria_master_workplan_v10_part4.md` IN-44 (the `Rung.envelope` row) | IN-07 E1 `befce041`, E2 `cd1e234c`, E3 `da4a864d`, E4-E6 `5099cb24`, SE-04 (a) `dd0a1c5a`, IN-52 shipped OFF `128bc9db` landed; SE-04 (b) stopped at design, (c) held; IN-52's flip ON not built; hash: `build_realm(0)` 8e4032a2, one season b2464a6c, two seasons 5301d6b6 EQUAL across the batch (old-tree/new-tree control equal on scarce.build, scarce.governed, build_realm(0)); residues: the corpus cannot observe `march` so the OFF arm was read on a base-vs-edited fold; the ON arm needs `requisition` executing in computed play; next: IN-52's flip and SE-04 (b)/(c) per `workplans/valoria_master_workplan_v10_part3.md` §1 (B10-16) |

## Standing orders — do not re-raise, do not do
| order | source |
|---|---|
| Do not re-propose `band_floors.person` as new — `band_floors["body"]` already exists and is live-read | `ED-SE-0052` |
| Do not re-propose hearth larders or any delivery move across a `contain` edge — matter moves only by `transfer` | `ED-SE-0053` |
| Do not cut `fort_level` / `facility_tier` as a side effect of another position: both stay declared in `references/descriptor_registry.yaml` behind the blocking `export_descriptors.py --check`, so a cut is an `ID-13` change of its own. `ED-SE-0052`'s named live readers are gone (`engine/autoload/game_state.py` deleted at `29b`; `systems/settlements/sim/registry.py` at `29c`). The season reads fortification as `Site.condition` through `world_q.fortification_of` | `ED-SE-0052` |
| Do not cite line numbers into a dated handoff section as stable — cite by heading text; a rewrite moves the body | `HANDOFF_SE_history.md` |
| Do not point at `systems/**` paths for SE design docs — `systems/` holds no `.md`; use `CURRENT.md`'s Settlement row (bare filename) | `ED-IN-0231`, CLAUDE.md §1 |
