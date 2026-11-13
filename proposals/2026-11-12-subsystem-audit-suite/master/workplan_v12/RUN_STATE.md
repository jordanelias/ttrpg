# Workplan v12 — run state (resume point after a compaction or container restart)

## Status: WORK NOTE (resolves nothing; deleted when v12 is adopted)

**Done and committed on `ccr-62958c70-0kjhsw` (PR #602):** head `workplan_v12.md`; body parts 3 to 43 (+ continuations); part 2 (`workplan_v12_part2*.md`, tables, 59 batches); `PATCH_LOG.md`, `H2_DECISIONS.md`, `COVERAGE.md`, `V12_FOR_JORDAN.md`.

**Update (after the lanes returned):** A44 and K1..K10 are done and committed. R1 (Opus, scripted global repairs, receipt `checks/R1_APPLIED.md`) is running; then four item-level repair lanes R2a..d (each reads its CHK files, fixes the open findings by the ladder, lists the rest for Jordan): R2a = K1+K2, R2b = K3+K4, R2c = K5+K6, R2d = K7+K8+K9+K10; then K11, compaction, the Fable verdict. Text below on running lanes is superseded.

**Update (2026-11-13): R1, R2a..d and H3 are done.** H3 (Opus, one round) closed the head parts: (1) part 2's totals recomputed by the appendix scripts (part 2 §0, §1.1–§1.3; the head's §5 and parts line): 1,455 positions, 442/21/6 movers, 526 edges, 25 waves, 390.5 h critical path, 748.5 h serial; (2) re-pin baselines of 24 batches set to part 2 §3's merge order (each edit tagged "lane H3"; §3's Checks paragraph lists them); (3) the names table and the symbols-with-no-carrier table, `workplan_v12_part2_cont3.md` (§12, §13; one symbol with no carrier, `stakes_ob`, C-26); (4) B35.30, the `knot` design item (HD-25), B35.28 HELD on it; (5) `V12_FOR_JORDAN.md` J-03 (`release`, R2d's J-1) and J-04 (the 6 KB cap, 160 items over); (6) part 2 §11.2, 15 gates that read a document; (7) part 2 §11's C-26..C-28 and §11.1's closing status of C-01..C-28 (8 open). The scripts are in the appendix (16 to 21) and `scratchpad/h3/`. The "Running at the last write" text below is superseded.

**Running at the last write (relaunched after the container restart of 2026-11-13):**
- A44: `workplan_v12_part44*.md` (B98-dials, B99-nine-retake). If the file is absent or has no boundary row for B99, relaunch from the brief in this session's transcript (input: `workplan_v12_part2.md` §4, 105 settings rows).
- Check lanes K1..K10 (Sonnet), briefs at `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/chk_<k>.txt` (the scratchpad may be gone: the brief is `V12_STRUCTURE_part3.md` §10.1, checks 1 to 11, parts ranges 3-6, 7-11, 12-15, 16-20, 21-24, 25-28, 29-32, 33-35, 36-39, 40-43); output `checks/CHK_K<k>.md`. A lane with no closing section in its CHK file did not finish.
- A local checkpoint loop (`scratchpad/checkpoint.sh`, every 4 minutes) commits and pushes this directory with `[skip ci]`.

**Decided, to apply by one script once A44, K5 and K8 have returned (so no Edit collides):** `register --check` exits 1 at the tree today (verified 2026-11-13: G6 3 violations H-47, H-48, H-59; R2 27 per K4), so every gate line reading `register --check` → exit 0 (about 240 lines in parts 3 to 44, K4 F1) is rewritten to B03's form (`workplan_v12_part5.md:105`): the per-check violation counts do not rise from the batch's opening reading, both quoted (ladder step 4: precedent). A gate on a row the batch itself edits keeps its own sentence.

**Next, in order (one round each; CLAUDE.md §0):**
1. ~~Read the receipts; repair lanes R1, R2a..d; lane H3~~ — done (above). Left for the orchestrator by H3 (one Edit each, not Jordan's): C-26 (B33.38's `stakes_ob.debt` arm `BLOCKED (v12: a carrier is owed)`), C-14 (ED-507 in B39), C-11 (B31's re-check of B20.09), C-23 (`master/MASTER_FINDINGS.md:65`); optionally the 15 gates of part 2 §11.2 rewritten to `test -f` + `git diff --stat`.
2. K11's report on part 44 (running in parallel with H3): read it; fix by the ladder; list the rest in `V12_FOR_JORDAN.md`.
3. Compact context, then one read-only Fable verdict (`valoria-critic`, questions in `V12_STRUCTURE_part3.md` §10.2).
4. Sonnet agonist/antagonist write-up of the master suite and v12 (Stage E).
5. Update PR #602 body (remove the 'not subscribed' line; held-back list: canon rewordings A-17, strife master A-84, A-60 directive, the `CLAUDE.md` preamble sentence on the engine-version owner, GO-09 workflow line, remaining Layer 1 items, content Jordan owes, `YIELD_OB` / `mortal_wound_ob` picks, B03.69 seat `off_npc_084`; Layer 1 edits and ED rows are in this PR and merging ratifies them, ED-1094). Stop the checkpoint loop.
6. Adoption of v12 into `workplans/` (retire v11 with `FORK:` rows) is Jordan's call; not done.


**Closed 2026-11-13:** Stage E done (`../AGONIST_ANTAGONIST.md` Parts A to C; lane E repairs `checks/E_REPAIR.md`); the Fable verdict repaired (`checks/V1_APPLIED.md`); PR #602 body rewritten; checkpoint loop stopped. Nothing in v12 has been run. Remaining and Jordan's: J-03 to J-08 (`V12_FOR_JORDAN.md`), adoption of v12 into `workplans/` (retires v11, `FORK:` rows), the repository's merge setting (J-05), merge of PR #602.
