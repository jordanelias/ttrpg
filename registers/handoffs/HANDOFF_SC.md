# Handoff — SC (Social Contest)

**Pointer index.** Every row names where its fact lives — a ledger id (its LAST row governs), a
`path` or `path:line`, or a command to run. This file restates no count, status or date of state:
open or run the pointer. The narrative this file used to carry is verbatim in
`registers/handoffs/HANDOFF_SC_history.md` (and finished work in `HANDOFF_SC_closed.md` where
that exists).

## Open

| item | where it lives | next step |
|---|---|---|
| Proceedings subsystem owns all social contests (ruling); build is PROPOSED, held back; ratification of the design itself is a separate, unexecuted action | `ED-SC-0033`..`ED-SC-0035`; `proposals/2026-09-05-proceedings-subsystem/21_RECONCILIATION.md` PART C/D (supersedes `19_PLAN.md`'s step text — corrected 2026-09-26, was mis-cited as PART H steps 1/2/4/22) | of the four PART C steps: step 1 executed (`ED-IN-0205`), step 2 superseded by R8.1's struct (`21_RECONCILIATION.md:97-101`), step 22 (`Tenure.term`, edge half only — the document half rides `Record.ttl` per C-10) remains open. Step 4 (`told_by`) is PARTLY built, not open whole: `engine/season/loop/witness.py:369-371` already mints `told_by` at the teller's own confidence for a telling event (part c) — what's actually missing is parts (a)/(b), the (person, channel) precedence walk and the document/remit→`told_by` source map (`witness.py:182` still returns only `firsthand`/`firsthand_via_knot`). PART H's five Jordan-decisions are all ruled, and PART H's own text says nothing further is genuinely his — but D-6/D-7 (the `speech_kinds` roster default) are separately unresolved, `19_PLAN.md:952-960` |
| Social-contest code retirement — ruled, NOT executed; this session's reading of "orphaned" excludes two live files, not itself ruled (corrected 2026-09-26, the ruling's inbound-reference list is stale) | `ED-SC-0033` clause 2 (D-1, measures the whole 47-file tree, "delete the tree") | `contest_legacy_stub.py` (zero live callers in code outside the tree — but referenced by exported artifacts `engine/engine_params/sim_params.json` and `value_pointer_links.json`, so deletion moves an export, not free) and the kernel `systems/social_contest/sim/contest/` (unreached by the game loop — `engine/season/requirements.yaml:88-90` — but alive in CI's blocking `sim-regression` job) retire together; deleting the stub also resolves the `contest_legacy_stub.py` compare-model-vs-per-side-kernel design fork in favour of the per-side kernel (`06_RESOLUTION.md`, `ED-SC-0034`'s pool-only model) since the compare model's only code (`resolve_exchange:132-190`) is what's being deleted — not before. `parliamentary_vote.py`/`parliamentary_stay.py` are NOT in scope — live FA-lane callers (`systems/factions/sim/parliamentary_action.py`, `parliamentary_transfer.py`) — re-measure inbound references before executing |
| Which provider resolves a social contest until proceedings lands, and the M-7 obstacle remedy it's tied to | `ED-SC-0037` (ruled, wired — `engine/season/seam/wrappers/sigma.py:125`, `tests/valoria/test_season_providers_are_registered.py` confirms); `21_RECONCILIATION.md` step 14 (M-7 failed at the 1D floor, remedy undecided: obstacle ceiling vs. pool floor) | the wiring is done; the M-7 remedy choice is a genuine open call (not the *only* one — D-6/D-7 above and `told_by` parts a/b are also open) — informed by `13_PARLIAMENT_FOLD_AND_RECALIBRATION.md`'s bounded-δσ evidence for moving bench reception out of the obstacle |
| Two of Jordan's 2026-09-04 rulings (multi-matter/conditional adjudication; binding-in-scene) bind all twelve proceeding rows, not just negotiation | `ED-SC-0038` | before `21_RECONCILIATION.md` step 14's bar runs: decide per-matter vs. single-margin outcome; re-examine `19_PLAN.md` PART I item 1 and P-14/D-8 against the verbatim rulings |

## Standing orders — do not re-raise, do not do

| order | source |
|---|---|
| Proceedings subsystem build must not refer to prior social-contest work (`systems/social_contest/`, the 2026-09-04 branches proposal) | scope ban recorded at `proposals/2026-09-05-proceedings-subsystem/README.md` |
| Do not read `contest_legacy_stub.py` / the retired kernel as live until the retirement wave actually runs | `ED-SC-0033` clause 2 (ruled, unexecuted) |
| A port/oracle disagreement is fixed via the ledger + re-export, never a hand-edit into `.gd` | `CLAUDE.md` §6 (ED-1050), repo-wide, applies to any SC export |
