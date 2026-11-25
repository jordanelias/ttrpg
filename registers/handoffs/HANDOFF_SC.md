# Handoff — SC (Social Contest)

**Pointer index.** Every row names where its fact lives — a ledger id (its LAST row governs), a
`path` or `path:line`, or a command to run. Restate no count, status or date of state here.
Narrative: `registers/handoffs/HANDOFF_SC_history.md`; finished work: `HANDOFF_SC_closed.md`.

## Open

| item | where it lives | next step |
|---|---|---|
| Batch B24-sc-hearing — IN FLIGHT | `workplans/valoria_master_workplan_v12_part22.md` and `_part22_cont.md`; open 8142371d09003f65c368d67d4ccdfd6ea05174d1 | built B24.01, B24.02, B24.03, B24.04, B24.05, B24.07, B24.06, B24.08, B24.09, B24.10, B24.11, B24.12, B24.13, B24.14, B24.15, B24.17, B24.18, B24.16 · close none · B24.01 to B24.99 |
| Closed batches B-J, B-N, B-O (first sub-batch) and B-P | `HANDOFF_SC_closed.md`, the section "Moved from Open" (rows verbatim; the commits are the record) | next: the batch `git grep -n 'SC-0' workplans/valoria_master_workplan_v12*.md` names; none open here |
| Proceedings subsystem owns all social contests; the design is ratified AS INTENT (`ED-SC-0039`); build is v9 SC-01 (built, B-N), SC-08 and SC-03b (built, B-O's first sub-batch), SC-02 and SC-04 (built, B-P, `HANDOFF_SC_closed.md`; their residue is held) | `ED-SC-0033`..`ED-SC-0035`, `ED-SC-0039`; `proposals/2026-09-05-proceedings-subsystem/21_RECONCILIATION.md` PHASE 2–4; `FORK:1b7c2f87:workplans/valoria_master_workplan_v11_part4.md` (SC-02) | SC-01, SC-08, SC-03b, SC-02 and SC-04 are built (`HANDOFF_SC_closed.md`); SC-02's re-source build is HELD in B10-Z on its design's approval |
| PROC-A residue (SC-04) | `world_q.judging_set`, `arrangements.yaml` and its loader `data/arrangements.py` (its production readers are `state/gate.py` and `loop/effects_information.py`; SC-08 pinned them with tests); `FORK:1b7c2f87:workplans/valoria_master_workplan_v11_part3.md` §1's B10-13 paragraph | SC-04's negotiation row landed `bc5d987a`; its residue: the other unseeded games, the `succession` row (CR-35's, H-217) and the un-re-hosted stress cases |
| Social-contest code retirement (`ED-SC-0033` clause 2): the stub is gone (`contest_legacy_stub.py`, retired before adoption); the kernel `systems/social_contest/sim/contest/` (`2-ii`) is SC-05 | `ED-SC-0033` clause 2; `FORK:1b7c2f87:workplans/valoria_master_workplan_v11_part5.md` SC-05 (carries SM-2, SM-15 and A-24's wording) | SC-05: Jordan's lean is to adopt (the proceedings subsystem owns all social contests; the orphaned `contest/` code retires) [medium]; only the TIMING is held, asked in the B-N report after SC-01's measurement (the interim roll kept, the kernel not adopted: `modules/social_contest/roll.py`'s docstring); no deletion is scheduled |

## Standing orders — do not re-raise, do not do

| order | source |
|---|---|
| Do not read `contest_legacy_stub.py` / the retired kernel as live until the retirement wave actually runs | `ED-SC-0033` clause 2 (ruled, unexecuted) |
| A port/oracle disagreement is fixed via the ledger + re-export, never a hand-edit into `.gd` | `CLAUDE.md` §6 (ED-1050) |
