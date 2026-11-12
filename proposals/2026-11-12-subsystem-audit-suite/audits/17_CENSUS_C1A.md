# Census C1A — unreferenced symbols in the season loop's core packages

## Status: REFERENCE (a census verdict; resolves nothing at runtime) — IN PROGRESS, partial file

## Read at: d7bd4ab (working tree)

Partition: every row of `census/C1_unreferenced_symbols.md` whose file is under
`engine/season/{loop,state,seam,manifest,decision,queries,data}/`, plus the two top-level files
`engine/season/epistemic.py` and `engine/season/gaps.py`. **187 rows.**

## 0. Verdict (preliminary; the final verdict replaces this paragraph)

The C1 list is almost entirely a list of private helpers, and private helpers are used in their own file:
that is what `file-local only` means, and it is not a defect. A reachability closure over the 187 rows
(each row's in-file users followed upward until a name another game file uses, a module-level statement
run at import, or a registering decorator) leaves a short list of real leads; each is then read at its
call site below.

First-pass closure (name-based, to be confirmed row by row):

| closure result | rows |
|---|---|
| reached from another game file through its in-file users | 163 |
| run by a module-level statement at import (a loader refusal) | 10 |
| registered by a decorator (`_context`, `effect_for`, `requirement_form`) | 7 |
| named by tests/tools only | 5 (`cast.name_of`, `files.loop_source`, `files.decision_modules`, `sheet.take_ranked`, `seam/wrappers/combat.load_error`) |
| named by nothing | 2 (`gaps.Ineligible`, `state/world._encode_object`) |

Instrument: `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/reach2.py`
(read-only AST closure; not in the tree, not proposed for it).

(The row table, the cluster findings and the extension follow; appended as verified.)
