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
