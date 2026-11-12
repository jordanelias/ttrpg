# Workplan v12 — coverage: does v12 carry every RESOLVED-BY finding and every v11 intake id?

## Status: WORK FILE (lane: coverage, one round; answers Jordan's two questions of 2026-11-12; resolves nothing at runtime, CLAUDE.md §0.05; deleted when v12 is adopted)

## Read at: the working tree of 2026-11-12 (branch `ccr-62958c70-0kjhsw`), with the body parts `workplan_v12_part3.md` .. `_part43_cont.md` as they stood when this lane read them (a patch lane was editing the same directory at the same time; a handle cited here was re-read in its part before it was cited).

**The two questions (Jordan, 2026-11-12).** (1) The master-findings lane "could not place 132 RESOLVED-BY rows in a batch" and 77 findings have no parseable severity: does that mean those findings are not part of the workplan and will not be built? (2) Does v12 fold in all the non-superseded items of workplan v11?

**The rule this file checks** (`UNIFICATION_BRIEF.md`, closure): every finding has one disposition; RESOLVED-BY means a proposal carries the exact edit and a gate. So a RESOLVED-BY row is built only if a v12 item carries its proposal's edit, and a v11 intake id is built only if a v12 item carries its carry-forward block.

**Classes used below.**

| class | meaning |
|---|---|
| COVERED | a v12 item (`Bnn.mm`) carries the carrier's edit; the handle is given |
| POINTER-ONLY | the closure row names no edit of its own ("none owed", an ordering input, a pointer to another closure row or a ruling); nothing is owed to v12 beyond what the pointed row's item carries |
| SUPERSEDED | a ruling or a later item replaces the carrier; cited |
| HELD-TABLE | an intake entry v12 does not build by design: it sits under the intake's held headings, which are H2's held table (`V12_STRUCTURE_part2.md` §5.6, "A held entry is not an item (§7.9)") |
| CONTENT-OWED | the edit is content (values for Jordan's correction) owed by a named item or batch |
| UNCARRIED | no item carries it; §C below says what this lane did about each |

**Method.** The script in Appendix A (run from the suite root, reads only) parses every RESOLVED-BY row of the four closure tables, resolves each carrier name to a proposal file by the closure tables' own abbreviation paragraphs, the v12 parts' own short-name lines and the authors' family aliases (BYZ_D, PAP_B, HAP_C, S1-C, CAP, MAP, UPR, HEAR_B, ...), and maps each proposal (and, where the carrier names one, its edit or section) to the v12 items whose heading, `SOURCE:` line or position-table row names it. Rows the script cannot resolve were resolved by hand (§A.2). The same index answers the intake (§B), the instruction suite and the codebase items (§D).
