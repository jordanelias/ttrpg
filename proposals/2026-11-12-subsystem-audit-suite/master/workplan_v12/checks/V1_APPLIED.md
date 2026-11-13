# V1 — repairs applied from `V12_VERDICT.md` (one round; not re-audited)

## Status: WORK NOTE (resolves nothing; deleted when v12 is adopted)

| repair | what | file:handle |
|---|---|---|
| D1 | B02.38 no longer writes R-03.c (row replaced by a note; the `unread` rule kept for non-`met` rows); GATE states B02.13's refusal rule on R-01..R-03; COST line and Reading 1's last sentence no longer have B02.38 write `status:`; R-06.c's "(as R-03.c)" reworded | `workplan_v12_part3_cont.md` B02.38 (R-03 table note, GATE, COST), Reading 1; R-06 note |
| D1 | B02 REQUIREMENT line and B02.13 step 2's example drop R-03.c | `workplan_v12_part3.md` B02 REQUIREMENT, B02.13 step 2 |
| D1 | R-03.c added by B08.99 (not B08.02: B08.02 creates `test_scene_sequence.py` but reads 4 of 5, so a `met` row would be refused there); conjunct text/argv copied whole into B08.99; GATE adds `register --requirements` exit 0, R-03 `met 3 of 3`; WHERE/TESTS/DEPENDS ON; B08.02 ADVANCES points to it | `workplan_v12_part23.md` B08.99, B08.02 |
| D5 | BATCH GATE golden-modes line adds B98.04 and B98.61 | `workplan_v12_part44.md` B98 BATCH GATE |
| D5 | `ROW(<file>, <key>)` and `SYM(<module>, <name>)` reads defined beside `FIX`; the 20 BLOCKED gates (B98.22, .30, .32, .40, .41, .42, .43, .44, .52, .57, .63, .64, .65, .66, .68, .69, .78, .79, .81, .83) each given a read command; B98.57 says "no gate: the row ships nothing" where B22.01's design lists no term; four carry an `[ASSUMPTION]` on the owner file (.40, .66, .78) | `workplan_v12_part44.md`, `_cont.md`, `_cont2.md` those items' GATE |
| D5 | The short item form stated in part 44's head (ADVANCES/WHERE/GLOSSARY omitted; BLOCKED also FALSIFIER/HASH MOVERS/REVERT; why) | `workplan_v12_part44.md` head, after `FIX` |
| D5 | PRE-FLIP RULE added | B98.04, B98.11 (`_part44.md`), B98.76 (`_cont2.md`) |
| D5 | `opus` reader added to the 12 flips' COST and TIER | B98.11, .47, .48, .62, .71, .74, .76, .77, .82, .84, .85, .86 |
| D3 | B99.01 step 0: re-points every capped conjunct `argv` to its source horizon; table of 11 (R-01.a, R-04.a, R-04.c6, R-05.a, .b, .c, R-06.a, R-08.a, R-09.b, R-09.c; R-04.c2 noted as written at 8), built by script (`scratchpad/v1/caps.py`, `captable.py`) from the `[v12: …]` notes; done by script with an asserted count; step 2 "no `argv` edited beyond step 0"; WHERE adds `argv`; U2 reads after step 0 | `workplan_v12_part44_cont3.md` B99.01, B99 UNDECIDED (U2) |
| D3 | Head §3.B "the corpus reading" points at B99.01 step 0 | `workplan_v12.md` §3.B |
| D2 | §7 point 7: merge-commit rule (never squash/rebase-and-merge), why, the driver alternative, `[ASSUMPTION: merge setting … J-05]` | `workplan_v12.md` §7 point 7 |
| D2/Q1 | New §2.1 "Where v12's text differs from the skill's": (a) BLOCKED/HELD/READING/POINTER not queued, the unmet-gate stop read as applying to built positions; (b) READING/POINTER never in `built`; (c) P16 (4) timing vs skill Phase 2, difference stated; (d) "rebase" read as the skill's merge (skill's rule chosen); (e) merge commit vs skill's squash | `workplan_v12.md` §2.1 |
| Q1 | §1: one paragraph on which positions the 0.2 loop runs; §7 point 4's "rebases" points at §2.1 (d) | `workplan_v12.md` §1 (after Item states), §7 point 4 |
| D4 | Head §0 "Where the plan's decisions are" and §9's opening rewritten to point at `V12_FOR_JORDAN.md` and its open rows J-03..J-07 | `workplan_v12.md` §0, §9 |
| D4 | §11.2 rows added: J-03..J-07; B03.70's Layer 0/1 hunks; B03.71 (HELD); B41.03 step 4 (HELD); B41.06's workflow line; B98's 47 BLOCKED; the Layer 1 row's B11.04/B41.03 text updated | `workplan_v12.md` §11.2 |
| D4 | B03.71 made HELD (cause: re-words `04` on an assumed ruling; needs an `L1-A*` node or Jordan's word; trigger J-07): table row, heading, HELD line, LANDS IT; B03's HELD BACK line adds B03.71 and B03.70's hunks | `workplan_v12_part5.md` B03 table, B03.71, HELD BACK line |
| D4 | ED-IN-0300 opened (`registers/editorial_ledger_in.jsonl:77`): names CR-29 → B11.04 covered, unchanged; names neither A1-81 nor GO-10 → B41.03's step 4 HELD (steps 1-3 proceed by the item's own rule), WHERE marked | `workplan_v12_part29.md` B41.03 |
| D4 | B41.06: workflow line not edited, named in PR body (B03g precedent, CODEOWNERS owns `/.github/workflows/`) | `workplan_v12_part29.md` B41.06 Wiring, WHERE |
| D4 | Part 2's Layer 1 table: B03.71 HELD, B41.03 hunk HELD, B11.04's coverage stated as explicit; addition (3) updated | `workplan_v12_part2_cont2.md` Layer 1 table |
| D4 | `V12_FOR_JORDAN.md`: B03.69 "settled" row now says BLOCKED; new J-05 (merge commits), J-06 (large batches, Q8), J-07 (B03.71, B41.03 step 4) | `V12_FOR_JORDAN.md` |
| Q2 | B16.10 (POINTER): `grep -c` of the proposal dropped; "GATE: none of its own", the pointed gates named | `workplan_v12_part23.md` B16.10 |
| Q2 | B35.01, B35.02: gate commands added (`test -f`, `git show --stat`, `grep -c falsifier`; B35.02 a `git grep` per strain kind) | `workplan_v12_part36.md` B35.01, B35.02 |
| Q2 | B21d.07: GATE names `harness.clocks 2 0 1 2` on/off and `harness.strife 2 0 1 2` | `workplan_v12_part29.md` B21d.07 |
| Q2 | B21d (CR-88 item) falsifier: v11's "`aperture 3 0`" P10 replaced by two seasons, longer reading B99's | `workplan_v12_part29.md` the CR-88 item's FALSIFIER |
| Q3 | R-05.a added to B35's REQUIREMENT line, read off its own instrument (the BATCH GATE's `corpus_run --seasons 2` seed-0 run) | `workplan_v12_part36.md` B35 REQUIREMENT |
| Q3 | Part 2 requirement map: M5 row reads R-01 to R-09 (B40 re-reads every conjunct), not "R-01, R-09"; R-05's row names B35 for .a/.b/.c and B40 | `workplan_v12_part2_cont2.md` §10 milestone table (M5 row), row table (R-05) |
| Q9 | Head §5 "about 354 h" marked superseded by 390.5 h; §8 steps table moves B41 from S15 to S18 (part 2 §1.2) | `workplan_v12.md` §5, §8 |
| Q8 | No batch re-cut; J-06 added (B98, B10, B03, B38, B11, B21 with positions, movers, hours from part 2's batch table; B10's verified cut B10.01-.50 \| .54-.. after B10.51-.53; others unverified) | `V12_FOR_JORDAN.md` J-06 |
| C-17 | Closed by ladder step 1 rather than a creating step: the source (`16_PESSIMIST_WR_D`, edit 2's Gate) says `tests/test_referent_class_stamps.py` "is not a file in the tree" and gates on `test_in12_step9.py`, which B36.10 uses; no item needs the old name | `workplan_v12_part2_cont2.md` tests table row, §11.1 C-17 |

**Not done / stated departures.** (1) R-03.c enters at B08.99, not B08.02 (the file's creator reads 4 of 5 tests, and a `met` row with a non-`yes` conjunct is refused). (2) Q1's list of positions the 0.2 loop does not run excludes `CONTENT`: CONTENT positions land `Item:` commits (`workplan_v12_part18_cont.md` BA1.01 LANDS IT). (3) B41.03: only its step 4 (the Layer 1 paragraph) is HELD; the code steps proceed by the item's own rule. (4) C-17 closed as a stale name, not given a creating step. (5) Part 2's and the head's position-state counts are not recomputed for B03.71 BUILD → HELD (one position). (6) No pytest, no instrument run; `python tools/ci_naming_check.py` → clean. Nothing committed by this lane (the orchestrator's checkpoint loop committed the tree while it ran).
