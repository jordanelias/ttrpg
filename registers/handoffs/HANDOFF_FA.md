# Handoff — FA (Faction Actions)

**Pointer index.** Every row names where its fact lives — a ledger id (its LAST row governs), a `path` or `path:line`, or a command to run. Restate no count, status or date of state here. Narrative: `registers/handoffs/HANDOFF_FA_history.md`.

## Open
| item | where it lives | next step |
|---|---|---|
| Batch B21b-fa-war — IN FLIGHT (the remainder: B21b.05–.27, .99) | `workplans/valoria_master_workplan_v12_part21.md`; open `42e35ac05` | built B21b.05 B21b.06 B21b.07 B21b.08 B21b.10 B21b.11 B21b.12 B21b.13 B21b.14 B21b.16 B21b.17 · close none · B21b.01–.04 landed @ac899f123 |
| B21 acceptance not met at close | `python -m engine.season.harness.register --requirements` (R-04.a, R-04.c2); `engine/season/hole_register.yaml` H-615; `python tools/m1_acceptance.py --summary` | read H-615; the plan's B23 block / B21b own the follow-up |
| Seat faction heads and let a head act (#445 P-3; FORCE-FOREIGN's cast) | FA-01 (`FORK:1b7c2f87:workplans/valoria_master_workplan_v11_part5.md`); `engine/season/offices.yaml`, `engine/season/harness/populated.py` | Mechanism landed at B-J with no data edit: `engine/season/tests/test_fa01_head_seats.py` (the plan's `aperture 4 0` EXIT was run once: reading in commit `98c7bea2`'s body, taken before the IN-48 revert, which changes no `engine/` byte but the new test) (the six authored heads hold own-faction seats; the Restoration head's seat acts refuse on purview, see its docstring). Content, the plan's recommendation (#457 D4, RS-21 item 4, [medium; Jordan to correct]): one foreign faction, two seats, in `references/npc_registry.yaml`, built at B-V (closed `b1eabf5d`); the Schoenland trade demand's one copy is FA-01's (G-6) and it is UNBUILT: its input never reaches a foreign prefect, `ED-IN-0298` (needs_jordan), H-234 |
| Insurgency and an emerged faction (H-186); vassalage (H-101) | IN-30 (`FORK:1b7c2f87:workplans/valoria_master_workplan_v11_part5.md`) and IN-40 (landed `3f320093`) | IN-30: stopped at B-U; see `engine/season/hole_register.yaml` H-186; IN-40 (landed `3f320093`): H-101 answered [medium; Jordan to correct], `under` is derived (rung containment plus a seat-holder's `oblige`), never a stored parent |

## Standing orders — do not re-raise, do not do
| order | source |
|---|---|
| Do not author faction-roster content assuming the old territory-nesting model — local/provincial/national tiers are independent, people-based | ED-IN-0047 (B12) |
