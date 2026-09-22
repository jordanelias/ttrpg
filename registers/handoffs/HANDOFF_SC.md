# Handoff — SC (Social Contest)

**Pointer index.** Every row names where its fact lives — a ledger id (its LAST row governs), a
`path` or `path:line`, or a command to run. This file restates no count, status or date of state:
open or run the pointer. The narrative this file used to carry is verbatim in
`registers/handoffs/HANDOFF_SC_history.md` (and finished work in `HANDOFF_SC_closed.md` where
that exists).

## Open

| item | where it lives | next step |
|---|---|---|
| Proceedings subsystem owns all social contests (ruling); build is PROPOSED, held back | `ED-SC-0033`, `ED-SC-0034`, `ED-SC-0035`; `proposals/2026-09-05-proceedings-subsystem/README.md` | execute `19_PLAN.md` steps 1, 2, 4, 22 before anything else stands on it |
| Proceedings stress-suite findings (deposit/writer gaps, stale count table, etc.) | `ED-SC-0036`; `proposals/2026-09-05-proceedings-subsystem/20_STRESS_TESTS.md` | resolve the 5 findings that survived adversarial attack before Stage 4 |
| Orphaned social-contest code retirement — ruled, NOT executed | `ED-SC-0033` clause 2; `systems/social_contest/sim/contest_legacy_stub.py` still on disk | delete, `FORK:` row per file, repoint inbound sites, confirm gates green |
| Personal-scale contest dispatch onto the promoted kernel (distinct from the faction-scale vote) | `ED-SC-0011` | build the personal party bridge |
| Combat's degree ladder (the one remaining hold; cross-lane with MB) | `tests/valoria/test_degree_ladder_single_owner.py` (`RULINGS`) | land the Ob-derivation-from-defender mechanism, then abolish the 40% ceiling |
| `contest_legacy_stub.py` dead-compare-model vs. live per-side kernel — design fork, not a bug | `proposals/2026-09-04-social-contest-branches/11_FOUR_GAMES_AUDIT_AND_PLAN.md` §8 E1 | rule which model canon describes |
| Which provider resolves a social contest until proceedings lands | `ED-SC-0037` (ruled — read the row for the disposition before assuming either option A or B) | confirm the ruled option is wired at the seam call site |

## Standing orders — do not re-raise, do not do

| order | source |
|---|---|
| Proceedings subsystem build must not refer to prior social-contest work (`systems/social_contest/`, the 2026-09-04 branches proposal) | scope ban recorded at `proposals/2026-09-05-proceedings-subsystem/README.md` |
| Do not read `contest_legacy_stub.py` / the retired kernel as live until the retirement wave actually runs | `ED-SC-0033` clause 2 (ruled, unexecuted) |
| A port/oracle disagreement is fixed via the ledger + re-export, never a hand-edit into `.gd` | `CLAUDE.md` §6 (ED-1050), repo-wide, applies to any SC export |
