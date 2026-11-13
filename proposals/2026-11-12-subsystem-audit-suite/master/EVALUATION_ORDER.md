# Evaluation of workplan v11 and the gap register — work order (stage 5 of `STAGES.md`)

## Status: WORK ORDER (resolves nothing at runtime; deleted when v12 is adopted)

**What it is.** Jordan (2026-11-12): *"The penultimate step will be to read and evaluate the entirety of workplan v11 and gap register."* Every position of `workplans/valoria_master_workplan_v11.md` and `_part2`..`_part17`, and every row of `engine/season/hole_register.yaml` (352 rows), gets **exactly one recorded disposition**, so that nothing is dropped silently when v12 replaces v11 (`STAGES.md` stage 6: *a v11 item survives if nothing from this session supersedes it, and is folded in carefully; it does not survive if something supersedes it*; on any conflict this session's content wins; `(RULED)` positions are never revised by an agent).

**Lanes (read directly; no separate transcription pass, because the dispositioning lane reads each position anyway — share the reading).**

| lane | source | output |
|---|---|---|
| E1 | `workplans/valoria_master_workplan_v11.md` (head), `_part2`, `_part3`, `_part17` | `master/eval/E1.md` |
| E2 | `_part4`, `_part5` | `master/eval/E2.md` |
| E3 | `_part6`, `_part7`, `_part8`, `_part9` | `master/eval/E3.md` |
| E4 | `_part10`, `_part11`, `_part12`, `_part13` | `master/eval/E4.md` |
| E5 | `_part14`, `_part15`, `_part16` | `master/eval/E5.md` |
| E6 | `engine/season/hole_register.yaml` rows 1 to 117 in file order | `master/eval/E6.md` |
| E7 | rows 118 to 234 | `master/eval/E7.md` |
| E8 | rows 235 to 352 | `master/eval/E8.md` |

(Count a row as each top-level list entry with an `id:`; lines 1 to the first row are the register's header: read it for what a row means.)

**The dispositions (exactly one per position or row).**
- **DONE-IN-CODE**: the behaviour or artifact exists in the tree now. Evidence: `file:symbol` opened, or a test that exercises it (named). Cheap probe allowed (short seeded run, `PYTHONHASHSEED=0`; no long `aperture`, no pytest).
- **SUPERSEDED**: a session item replaces it: cite the proposal file and section, the batch handle (`unified/U3_DEPENDENCY_ORDER.md`), the ruling (`unified/DECISIONS_ANSWERED.md` A-n), or the instruction-suite item (`master/instructions/IS_*`). It is not carried into v12 in any form; say what exactly replaces it.
- **WRONG**: its premise is false at the tree or contradicted by `audits/25_GROUNDING_ENGINE.md`, or its own gate cannot observe what it claims. Evidence.
- **STILL-NEEDED**: nothing from this session supersedes it, and it is not done. It is carried into v12 as its own item: name the lane tag (MB PC FI SC FA WR IN GO SE), the U3 batch it should join (or a new batch with dependencies), its edit set, its gate (an execution artifact), whether it moves hashes, tier, and copy its content-owner entry verbatim in an appendix block so the v12 author need not reopen v11. If only part is superseded, split: the superseded part gets SUPERSEDED, the rest STILL-NEEDED (two rows).
- **MISSING-DEP**: needed, but a dependency does not exist in the tree or in any proposal; name it and the owner.
- **RULED-CONFLICT**: a `(RULED)` position or a Jordan-ruled gap row conflicts with session content: do not decide; give the two options for `master/eval/EVAL_FOR_JORDAN.md` in the form of `unified/DECISIONS_FOR_JORDAN.md`.

**How to find what supersedes.** Grep `proposals/`, `unified/` and `master/` for the position's ids (`CR-nn`, `CP-Tnn-nn`, `B10-nn`, `H-nnn`, `ED-...`, `PP-...`): the suite cites them heavily, and a citation is the cheapest decisive lead. Then read `unified/U5_FINDINGS_CLOSURE_*` rows for the subject, `unified/U4_TRACEABILITY.md`, and the proposal itself. Open the cited section before writing SUPERSEDED (a pointer you have not opened is marked UNVERIFIED).

**Output form.** Each lane file: a head (counts per disposition, files read in full, what you could not check), then one table row per position or hole row: `| id | one-line gist | disposition | evidence / cite | v12 target (for STILL-NEEDED / MISSING-DEP: lane, batch, gate) |`, in source order, no row skipped; STILL-NEEDED and MISSING-DEP carry-forward blocks (the content-owner text) appended after the table under `## Carry-forward blocks`. Write the head and the first part early and append (CLAUDE.md §10). Words: use `unified/U1_GLOSSARY.md` (A-98: attribute, skill, skill score, martial skill, derived score; `unified/MB_LEXICON.md` for armies).

**Read first (all lanes).** `CLAUDE.md`; `STAGES.md` (stage 5 and 6, the v12 rules); `unified/DECISIONS_ANSWERED.md` (A-1..A-99 govern); `unified/U3_DEPENDENCY_ORDER.md` (the batches and what each proposal lands); `unified/U4_TRACEABILITY.md`; `master/instructions/IS_A_NINE.md` and `_part2` for the requirements; `.claude/skills/methodology-execute/SKILL.md` §BATCHES only for the forms. Then every position or row of your source, in full.

**Rules.** Read-only except your own `master/eval/E<k>.md`. No code, canon, registry, ruling or Layer 1 edit; no commit; no pytest. Nothing deterministic (draws are drawn; runs are reproducible); ground every claim in a file you opened; do not guess; mark assumptions `[ASSUMPTION: ... — basis]`. One round. Receipt (<= 150 words): counts per disposition, rows or positions read, items for Jordan, what you could not check.
