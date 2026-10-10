# Handoff — SE (Settlements)

**Pointer index.** Every row names where its fact lives — a ledger id (its LAST row governs), a `path` or `path:line`, or a command to run. Restate no count, status or date of state here. Narrative: `registers/handoffs/HANDOFF_SE_history.md`.

## Open
| item | where it lives | next step |
|---|---|---|
| Batch B-F — IN FLIGHT | `workplans/valoria_master_workplan_v9_part3.md` §B.1 (the B-F row) and §B.2 (its card); `open 0c666b69` | built IN-21, SE-01 · IN-22 live arm NOT BUILT (H-160); IN-34 FALSIFIED, reverted (H-206) · close 2 · Phase 3 next |
| Matter/works proposal (`nearest_store`, body gate, `works`/`found`) — RATIFIED AS INTENT (`ED-SE-0053`); the residue is v9 SE-03 and IN-28 | `ED-SE-0053`; `workplans/valoria_master_workplan_v9_part6.md` SE-03; `workplans/valoria_master_workplan_v9_part5.md` IN-28 | build IN-28 (`found`/`build`: a cost, a holder, a closer); nothing in the proposal exists until it is built with its test |
| Built-world ontology proposal (Site/Rung fabric-address, fortification bands) — superseded in part by `ED-SE-0053` and absorbed (fortification is `Site.condition`) | `ED-SE-0052`; `ED-SE-0053` | nothing to rule; SE-03 carries the residue |
| MW-11 / MW-5 falsifiers RED (crossing predicate downward-only; `withdrawal_only`/death same-season collision) | `ED-SE-0053` | resolve if/when the proposal is authored into canon (v9 SE-03, `workplans/valoria_master_workplan_v9_part6.md`: re-run at IN-28; the red is [UNVERIFIED]) |

## Standing orders — do not re-raise, do not do
| order | source |
|---|---|
| Do not re-propose `band_floors.person` as new — `band_floors["body"]` already exists and is live-read | `ED-SE-0052` |
| Do not re-propose hearth larders or any delivery move across a `contain` edge — matter moves only by `transfer` | `ED-SE-0053` |
| Do not cut `fort_level` / `facility_tier` as a side effect of another position: both stay declared in `references/descriptor_registry.yaml` behind the blocking `export_descriptors.py --check`, so a cut is an `ID-13` change of its own. `ED-SE-0052`'s named live readers are gone (`engine/autoload/game_state.py` deleted at `29b`; `systems/settlements/sim/registry.py` at `29c`). The season reads fortification as `Site.condition` through `world_q.fortification_of` | `ED-SE-0052` |
| Do not cite line numbers into a dated handoff section as stable — cite by heading text; a rewrite moves the body | `HANDOFF_SE_history.md` |
| Do not point at `systems/**` paths for SE design docs — `systems/` holds no `.md`; use `CURRENT.md`'s Settlement row (bare filename) | `ED-IN-0231`, CLAUDE.md §1 |
