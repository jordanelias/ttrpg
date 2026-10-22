# Handoff — SE (Settlements)

**Pointer index.** Every row names where its fact lives — a ledger id (its LAST row governs), a `path` or `path:line`, or a command to run. Restate no count, status or date of state here. Narrative: `registers/handoffs/HANDOFF_SE_history.md`.

## Open
| item | where it lives | next step |
|---|---|---|
| Matter/works proposal (`nearest_store`, body gate, `works`/`found`) — RATIFIED AS INTENT (`ED-SE-0053`); IN-28's cost and holder and SE-03's MW-5 landed at B-K (`c8d1db3a`); the closer (`raze`) landed at B-R (`68eaaa41`); the residue is the works' producer | `ED-SE-0053`; `engine/season/hole_register.yaml` H-166 (limit 3), H-228 (`raze`'s limits), H-165; `registers/editorial_ledger_in.jsonl` ED-IN-0297 (needs_jordan, where a works comes from) | the producer waits on ED-IN-0297; nothing else in the proposal exists until built with its test |
| Built-world ontology proposal (Site/Rung fabric-address, fortification bands) — superseded in part by `ED-SE-0053` and absorbed (fortification is `Site.condition`) | `ED-SE-0052`; `ED-SE-0053` | nothing to rule; H-166 limit 3 and H-211 carry the residue |
| MW-11 RED (crossing predicate downward-only; nothing raises a body); MW-5 is a test over H-125's arms | `ED-SE-0053`; `engine/season/hole_register.yaml` H-211 (MW-11), H-125; `engine/season/tests/test_se03_body_bands.py` (MW-5) | MW-11 is measured, not in the tree (a red test may not be skipped); r2 section A.4's signed body step and an upward check in `_crossings` are its fix, a position of their own |

## Standing orders — do not re-raise, do not do
| order | source |
|---|---|
| Do not re-propose `band_floors.person` as new — `band_floors["body"]` already exists and is live-read | `ED-SE-0052` |
| Do not re-propose hearth larders or any delivery move across a `contain` edge — matter moves only by `transfer` | `ED-SE-0053` |
| Do not cut `fort_level` / `facility_tier` as a side effect of another position: both stay declared in `references/descriptor_registry.yaml` behind the blocking `export_descriptors.py --check`, so a cut is an `ID-13` change of its own. `ED-SE-0052`'s named live readers are gone (`engine/autoload/game_state.py` deleted at `29b`; `systems/settlements/sim/registry.py` at `29c`). The season reads fortification as `Site.condition` through `world_q.fortification_of` | `ED-SE-0052` |
| Do not cite line numbers into a dated handoff section as stable — cite by heading text; a rewrite moves the body | `HANDOFF_SE_history.md` |
| Do not point at `systems/**` paths for SE design docs — `systems/` holds no `.md`; use `CURRENT.md`'s Settlement row (bare filename) | `ED-IN-0231`, CLAUDE.md §1 |
