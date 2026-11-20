# Wave 3 — rewrite lanes: apply the unification decisions to the proposals

## Status: WORK ORDER (applies `UNIFICATION_BRIEF.md` after waves 1 and 2; resolves nothing at runtime; deleted when the stage closes)

Seven Opus lanes, each owning a disjoint set of proposal files (so no two lanes edit one file). A lane edits **only the files in its set**. An edit that a ledger row asks for in a file outside your set is listed in your receipt under "for another lane" and left.

| lane | files under `proposals/` | read-lane file |
|---|---|---|
| W3-1 | the R1 set: `03_*`, `04_*`, `10_*`, `11_*`, `26_*`, `27_*`, `29_*`, `30_GO_*`, `U5b_PC_*`, `U5b_MB_*`, `U5a_DICE_*`, `U5d_GO_*` | `unified/work/R1_READ.md` |
| W3-2 | the R2 set: `01_*`, `02_*`, `05_*`, `08_*`, `12_*`, `13_*`, `19_*`, `28_*`, `U5a_CHAR_*`, `U5a_CORE_*`, `U5a_capability_home_and_two_inputs.md`, `U5a_tests_digest_additions.md`, `U5c_FI_*`, `U5c_SC_*` | `R2_READ.md` |
| W3-3 | the R3 set: `06_*`, `07_*`, `09_*`, `30_WR_*`, `31_*`, `U5d_FA_*`, `U5d_SE_*`, `U5d_WR_*`, `U5d_STORY_*` | `R3_READ.md` |
| W3-4a | verbs: `14_*`, `U5b_VERBS_*`, `U5c_VERBS_*` | `R4_READ.md` |
| W3-4b | institutions: `15_*` | `R4_READ.md` |
| W3-5a | pessimist: `16_*` | `R5_READ.md` |
| W3-5b | `17_*`, `18_*`, `20_*`, `21_*`, `22_*`, `23_*` | `R5_READ.md` |

## What to read

`CLAUDE.md`; `UNIFICATION_BRIEF.md`; `unified/DECISIONS_ANSWERED.md` (A-1 to A-91, governing); `unified/UNIFICATION_RUN.md`; your read-lane file's sections 1, 2, 7, 7b (and 8 where present) **for your files**; `unified/U1_OWNERS_AND_VOCABULARY.md` (the decisions D-U1-01..11 and the ledger rows that touch your files), `unified/U1_GLOSSARY.md`, `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md`; `unified/U3_CONFLICT_LEDGER.md` (every row whose losing document is in your set), `unified/U3_DEPENDENCY_ORDER.md` (the batch handle, lane tag, dependencies and hash movers of each of your files), `unified/U3_JORDAN_CALLS.md` (the assumption to build under until Jordan answers: J-U3-01 is built as Option 1 with its dial at zero, and P-1 pending); `unified/OWED_TO_UNIFICATION.md`. Then each of your files, in full, before editing it.

## What to do to each file

1. Apply every Layer 1 rewrite of the read lane's section 1 that has verdict VIOLATES or AMBIGUOUS, in the conforming form chosen there or by U1/U3 (the decision wins over the read lane where they differ; say so).
2. Apply every ruling-check row (section 2): a body that still carries text a ruling or a head superseded is **made to follow the head**; the stale text is removed, not left beside the new (a `Reconciled:` line records it).
3. Apply the U1 vocabulary and owner decisions (the removal edit of each ledger row that touches the file) and the U3 conflict-ledger edit for the file as the losing document; dependency order and cycle edge cuts go in as an explicit `Depends on:` / `Lands in batch:` lines using the U3 handles.
4. **Test 9.** For each INCOMPLETE item whose missing part is decidable from the repository, write it in (exact files and symbols, order of edits, schema, call sites, named tests, the gate as an execution artifact with the expected reading, the falsifier and control, declared hash movers, dependencies, what lands it, cost class and tier). Use the read lane's section 7b text where written, after checking it against the tree. A gate that names a scratch probe not in the tree becomes a step that first writes the probe in the named file, with its expected output. What is not decidable: leave it marked INCOMPLETE at the item with the blocking reason.
5. Keep the author's authorship line; add one `Reconciled:` line at the head (date, the ledger rows applied, what changed). Never delete another lane's finding; a finding you consider wrong is marked DISPUTED with your evidence. Change what the rows require, nothing else: this is reconciliation, not recomposition. No new proposals, no new ledgers, no second audit.
6. Where a row is wrong at the tree (the cited symbol or line does not exist or says otherwise), do not apply it blindly: open the tree, correct the row in your receipt, and write the true text.

## Rules

Edit only your set's files. No commit, no pytest, no edits of tracked files outside the suite. Run `python tools/ci_naming_check.py` after finishing (the canonical name is Solmund; a Bash scripted replacement bypasses the naming guard). Nothing deterministic; ground every claim in a file you opened; do not guess; mark assumptions `[ASSUMPTION: ... — basis]`. A resolution that would overwrite ratified canon, a `(RULED)` item or a ratified Layer 1 row is written as a proposal and listed in your receipt for the owed list, never applied. One round: do not recurse, do not audit your own edits further than one reread of each edited section. Write the ordered list of files finished to `unified/work/W3_<lane>_DONE.md` as you go (file; rows applied; rows not applied and why), so a stop loses nothing. Receipt (<= 200 words): files edited (count), rows applied, rows not applied, items for another lane, items for Jordan.
