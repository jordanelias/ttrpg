# Handoff

**Pointer index for continuity.** Every row names where its fact lives: a path, a ledger id (its
LAST row governs), or a command to run. **This file restates no count, status, figure or date of
state.** Jordan: *"anything that gets pulled up frequently cannot be hard coded with
numbers/values/dates."* If you are about to write a number or a status here, write the pointer to
its owner instead. Nothing surfaces this file automatically: read it, and your lane's file, yourself.

Everything this file said before it became an index is verbatim in
`registers/handoffs/HANDOFF_archive.md` under *"Pre-pointer body of root HANDOFF.md"*.

## Next actions — where they live

**This heading is load-bearing:** `tools/currency_consistency_check.py` reports drift without it.

| you want | open or run |
|---|---|
| **the ordered work — start here** | the lane's one active plan, named in `CURRENT.md`'s "The plan" row (every earlier plan is retired, `FORK:0671283`) |
| your lane's open items | `registers/handoffs/HANDOFF_<LANE>.md` (`MB PC FI SC FA WR IN GO SE`) |
| which head is canonical | `CURRENT.md` |
| does the milestone run | `python tools/m1_acceptance.py --summary` |
| the season loop against the nine requirements | `python -m engine.season.harness.register --requirements` |
| holes, verb coverage, unrepresentable cases | `python -m engine.season.harness.corpus_run` |
| the verb aperture per holder, per source, on the populated realm (not the corpus) | `python -m engine.season.harness.aperture [seasons] [seed]` |
| measured holes before you re-derive one | `engine/season/hole_register.yaml` |
| rows awaiting Jordan | `grep -c '"needs_jordan": true' registers/editorial_ledger*.jsonl` counts ROWS; an id's last row decides whether it is still open |
| what landed recently | `git log --oneline -20` and the ledgers' last fortnight of rows |

**Do not append a dated bullet here.** Ordered work goes in the plan; lane work in its lane file;
the narrative of what happened goes in the commit message and the PR body.

## Before you start

| do not | because |
|---|---|
| build a guard over process | `CLAUDE.md` §0.1 pt 5 |
| re-derive a measured hole | check `engine/season/hole_register.yaml` and the requirement's `measured:` block first |
| start without reading the ledgers' recent rows | work has been redone that a ruling two days earlier had already answered — `registers/editorial_ledger*.jsonl` |
| run the full suite after each edit | `CLAUDE.md` §0.4 |
| cache a count in any file read at session start | run the instrument instead |
| write a tracked data file from a test and restore it in a `finally` | under `pytest -n` another worker that builds a realm inside the window reads the doctored file: `b12f1e4a` (the NPC-roster test; it showed up as a claim count 30 short in an unrelated test). Point the loader at a `tmp_path` copy. Only `engine/season/tests` was searched for this; `tests/valoria` was not |
| edit `architecture/holonic_ARCHITECTURE.md` and assume `register --check` is the gate | the `#353 :NNN` line cites in `engine/season/hole_register.yaml` (H-04, H-20, H-37) move when lines are added above them, and `register --check` does not read them: run `pytest engine/season/tests/test_season_shape.py -k test_w1` after any edit to that file, and re-point each cite to the EXACT line, not within the six-line tolerance |
| debug `tests/valoria/test_forked_status.py` on a shallow clone | `cat .git/shallow` — its `FORK:` rows name commits the clone cannot reach |

## Rulings — do not re-raise

The bodies are in `registers/handoffs/HANDOFF_archive.md`; search for the heading.

| ruling or standing prohibition | heading in the archive |
|---|---|
| ruled and landed | `### Ruled and landed — do not re-raise` |
| the ruling agenda is closed | `### The ruling agenda is CLOSED` |
| resolver architecture | `### Resolver architecture — RULED` |
| faction stats | `### ✅ PARTLY RULED 2026-08-23 — faction stats` |
| apparatus work withdrawn | `### ⛔ WITHDRAWN 2026-08-19` |
| ID allocation | `CLAUDE.md` §4 and `references/id_reservations.yaml` — read `next_free`, allocate, bump, co-commit |

## Archive

`registers/handoffs/HANDOFF_archive.md` holds the root file's dated narrative;
`registers/handoffs/HANDOFF_<LANE>_history.md` and `_closed.md` hold each lane's.
They grow by archival and are not read at session start.
