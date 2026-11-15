# Handoff — GO (Godot)

**Pointer index.** Every row names where its fact lives — a ledger id (its LAST row governs), a `path` or `path:line`, or a command to run. Restate no count, status or date of state here. Narrative: `registers/handoffs/HANDOFF_GO_history.md`.

## Open
| item | where it lives | next step |
|---|---|---|
| Batch B03g-go-early-landings — IN FLIGHT | `workplans/valoria_master_workplan_v12_part6.md`, the batch's block; open 0d5bf6aa0655ab1abfc88442c0343ea1cf880bc2 | built B03g.01 · close none · B03g.02 to B03g.04, then B03g.99 |
| port gate (B10-20) | `FORK:1b7c2f87:workplans/valoria_master_workplan_v11_part3.md` §1, the B10-20 card | B10-03b (GO-07) is CLOSED (closing commit `8a80c4fc`; the item is `15593ac4` on `main`); the card's entry gate is B10-18 merged, with every batch before it closed |

## Standing orders — do not re-raise, do not do
| order | source |
|---|---|
| A port never corrects its oracle in place — fix canon via the ledger and re-export, never hand-edit a value into the `.gd` side | `CLAUDE.md` §6 |
| Do not build from `godot/godot_architecture_specification.md` (STALE REFERENCE, pre-d+σ) | `CLAUDE.md` §6 |
| The player surface is specified by the oracle's readings (`decision/sheet.py`, `harness/play_surface.py`); the UI design set and the stale architecture specification are intent only | `11_GO_design_reference_disposition` (workplan v12 B03.21) |
