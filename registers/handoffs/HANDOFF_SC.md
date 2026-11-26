# Handoff — SC (Social Contest)

**Pointer index.** Every row names where its fact lives — a ledger id (its LAST row governs), a
`path` or `path:line`, or a command to run. Restate no count, status or date of state here.
Narrative: `registers/handoffs/HANDOFF_SC_history.md`; finished work: `HANDOFF_SC_closed.md`.

## Open

| item | where it lives | next step |
|---|---|---|
| Batch B24-sc-hearing — IN FLIGHT | `workplans/valoria_master_workplan_v12_part22.md` and `_part22_cont.md`; open 8142371d09003f65c368d67d4ccdfd6ea05174d1 | built B24.01, B24.02, B24.03, B24.04, B24.05, B24.07, B24.06, B24.08, B24.09, B24.10, B24.11, B24.12, B24.13, B24.14, B24.15, B24.17, B24.18, B24.16, B24.19, B24.20, B24.22, B24.21, B24.23, B24.24, B24.25, B24.26, B24.27, B24.28, B24.29, B24.30, B24.31, B24.36, B24.41, B24.32, B24.34, B24.33, B24.35, B24.44, B24.43, B24.37, B24.39, B24.38, B24.99 · close none · B24.01 to B24.99 |
| Closed batches B-J, B-N, B-O (first sub-batch) and B-P | `HANDOFF_SC_closed.md`, the section "Moved from Open" (rows verbatim; the commits are the record) | next: the batch `git grep -n 'SC-0' workplans/valoria_master_workplan_v12*.md` names; none open here |
| Proceedings subsystem owns all social contests; the design is ratified AS INTENT (`ED-SC-0039`); build is v9 SC-01 (built, B-N), SC-08 and SC-03b (built, B-O's first sub-batch), SC-02 and SC-04 (built, B-P, `HANDOFF_SC_closed.md`; their residue is held) | `ED-SC-0033`..`ED-SC-0035`, `ED-SC-0039`; `proposals/2026-09-05-proceedings-subsystem/21_RECONCILIATION.md` PHASE 2–4; `FORK:1b7c2f87:workplans/valoria_master_workplan_v11_part4.md` (SC-02) | SC-01, SC-08, SC-03b, SC-02 and SC-04 are built (`HANDOFF_SC_closed.md`); SC-02's re-source build is HELD in B10-Z on its design's approval |
| PROC-A residue (SC-04) | `world_q.judging_set`, `arrangements.yaml` and its loader `data/arrangements.py` (its production readers are `state/gate.py` and `loop/effects_information.py`; SC-08 pinned them with tests); `FORK:1b7c2f87:workplans/valoria_master_workplan_v11_part3.md` §1's B10-13 paragraph | SC-04's negotiation row landed `bc5d987a`; its residue: the other unseeded games, the `succession` row (CR-35's, H-217) and the un-re-hosted stress cases |

## Standing orders — do not re-raise, do not do

| order | source |
|---|---|
| A port/oracle disagreement is fixed via the ledger + re-export, never a hand-edit into `.gd` | `CLAUDE.md` §6 (ED-1050) |
