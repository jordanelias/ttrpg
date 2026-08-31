# SESSION PROVENANCE — the ideal unified code shape (2026-08-31)

## Status: PROVENANCE. Working files, committed **unedited**, so the suite's claims can be audited
## against what produced them. **Nothing here is a design document and nothing here ratifies.**
## The deliverable is `proposals/2026-08-31-unified-code-shape/`.

Same posture as this repository's existing provenance directories: committed **as they stood at
session end, including their errors**, because a provenance record that has been tidied is not
provenance.

| file | size | what it is |
|---|---|---|
| `cites.json` | 264 KB | every `path:line` claim harvested from the fourteen trace logs of PR #345, with the log and line that made it. The input to the trace compiler's verification pass |
| `cites2.json` | 323 KB | the second harvest, widened after the first pass under-collected — kept separately rather than merged, so the widening is visible |
| `dossier.txt` | 285 KB | the claim-by-claim dossier: each harvested claim printed against the **actual source lines** at the cited path, which is how DRIFTED and FALSE verdicts were reached |

## What is deliberately NOT here

**A 42 MB, 1,442-file checkout of the repository at an earlier ref**, which the trace compiler made as
a comparison copy. It is not committed. It is recoverable with one `git` command, and committing it
would put a duplicate of the repository inside its own history — the shape this repo's own doctrine
refuses, since *a graveyard nothing visits is just a second copy of `git log`*.

## The one thing worth reading here

`dossier.txt` is the artifact behind the register's central discipline: **every citation was checked by
printing the cited path's real lines beside the claim.** Prior sessions' citations had drifted by 2–20
lines, and one was fabricated outright. That is not a fact a reader should have to take on trust, so
the evidence is committed rather than summarised.
