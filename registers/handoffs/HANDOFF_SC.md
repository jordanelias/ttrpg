# Handoff — SC (Social Contest)

**Pointer index.** Every row names where its fact lives — a ledger id (its LAST row governs), a
`path` or `path:line`, or a command to run. Restate no count, status or date of state here.
Narrative: `registers/handoffs/HANDOFF_SC_history.md`; finished work: `HANDOFF_SC_closed.md`.

## Open

| item | where it lives | next step |
|---|---|---|
| Proceedings subsystem owns all social contests; the design is ratified AS INTENT (`ED-SC-0039`); build is v9 SC-01, then SC-02 | `ED-SC-0033`..`ED-SC-0035`, `ED-SC-0039`; `proposals/2026-09-05-proceedings-subsystem/21_RECONCILIATION.md` PHASE 2–4; `workplans/valoria_master_workplan_v9_part6.md` (SC-01, SC-02) | Build SC-01 (`22` steps 11–16 and the fired-slot step, batch B-N, `workplans/valoria_master_workplan_v9_part3.md` §B), then SC-02 |
| PROC-A residue (SC-04) | `world_q.judging_set`, `arrangements.yaml` and its loader `data/arrangements.py` (its production reader is v9 SC-08, riding SC-01); `workplans/valoria_master_workplan_v9_part6.md` SC-04 | SC-04: the unseeded games, `standing_routes` and the unmoved stress cases — a transcription |
| Social-contest code retirement (`ED-SC-0033` clause 2): the stub is gone (`contest_legacy_stub.py`, retired before adoption); the kernel `systems/social_contest/sim/contest/` (`2-ii`) is v9 SC-05 | `ED-SC-0033` clause 2; `workplans/valoria_master_workplan_v9_part6.md` SC-05; `workplans/valoria_master_workplan_v9_part5.md` A-24 | SC-05: Jordan's lean is to adopt (the proceedings subsystem owns all social contests; the orphaned `contest/` code retires) [medium]; only the TIMING is held, asked at B-N after SC-01's measurement; no deletion is scheduled |

## Standing orders — do not re-raise, do not do

| order | source |
|---|---|
| Proceedings subsystem build must not refer to prior social-contest work (`systems/social_contest/`, the 2026-09-04 branches proposal) | scope ban recorded at `proposals/2026-09-05-proceedings-subsystem/README.md` |
| Do not read `contest_legacy_stub.py` / the retired kernel as live until the retirement wave actually runs | `ED-SC-0033` clause 2 (ruled, unexecuted) |
| A port/oracle disagreement is fixed via the ledger + re-export, never a hand-edit into `.gd` | `CLAUDE.md` §6 (ED-1050) |
