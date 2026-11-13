# R2d_APPLIED — repair lane R2d (Opus): the open findings of CHK_K7..K10 (parts 29 to 43) and part 2 §4

## Status: WORK RECORD (one round; a record of edits to `master/workplan_v12/`; resolves nothing at runtime, CLAUDE.md §0.05; deleted with the suite when v12 is adopted)

Appended finding by finding as each is applied (a restart resumes from the last row written). Form: finding id → what was done (edit / re-checked already fixed / for Jordan / no action, with the reason) · file:handle.

## K7 (parts 29 to 32)

- **F-1** edit · `workplan_v12_part30.md` B20.10: `stand_draw` EXISTS-IN-TREE → `V12 B19.54` (tree grep: no `stand_draw` in `engine/`, `modules/`; B19.54 creates it, part 27 row; B19 is in B20's after-list); MNV §3's "units and orders" column (`26_MASS_BATTLE_maneuver_orders.md:105-116`) copied into step 1, eleven rows, the head's lexicon corrections applied (S-1 commander, S-6 centre, S-7 depth); the free trigger operands `N`, `D`, `F` marked `[ASSUMPTION]` (the source gives none); SOURCE no longer says "copied by reference".
- **F-2** edit · `workplan_v12_part30_cont.md` B25.20: `rosters.yaml: task_fraction` EXISTS-IN-TREE → `V12 B07.02` (tree grep: absent; B07.02 creates the roster and `TASK_FRACTION`, `workplan_v12_part10_cont2.md:80`). `teller_weight` re-checked present (`decision/options.py:1770`).
- **F-3** edit · `workplan_v12_part32.md` B37.14: GATE's whole-file arm now deselects the two `BASE_BUILD`/`BASE_SEASON` tests by `-k` (their names read in `test_cr87_violence_contexts.py:377`, `:396`); the K7 `EXPECTED RED UNTIL` line kept and its "author's or orchestrator's to reconcile" clause replaced by the `-k` note.
- **F-4** re-checked, already fixed by R1 repair 4: B25 (`part30_cont.md:33`), B27 (`part31.md:36`), B37 (`part32.md:43`) each carry the batch `EXPECTED RED UNTIL` line; B27.99's "named in its item's commit body" now reads alongside it. No edit.
- **F-6** edit · `part30.md` B20.12: `V12 B20.19` removed from DEPENDS ON and written as a note ("not a dependency": `auto` with no decider is the delegated battle until B20.19).
- **F-7** edit (precedent, ladder step 4) · `workplan_v12_part2.md` §1.1 (outside my parts; one sentence): §1.1 already rules that a HELD row pointing at a later batch is what HELD means; B11F2.10 is named there now, with its TRIGGER's §7.9 clause (it becomes an item of B21s when it fires). No edit to part 32_cont: its TRIGGER line already says so.
- **F-8**, **F-9** no action (K7: recorded, handled by H2 HD-08; a forward note with its control).
- **F-10** edit · `part29.md` B21d SERIAL EDGES "with other batches" and PARALLEL (B41 removed from S15; HD-10 cited); B41 PARALLEL rewritten to S18 (B21s, B23, B30, B35), its shared-file clause re-read as "B19, B12c closed before B41 opens"; B41 SERIAL EDGES' two "S15" clauses corrected.
- **F-11** edit · `part30_cont.md` B25 head: COST and EST moved after PARALLEL (§5.2 order); B25's and B20's `SERIAL EDGES (written after the position table, E-11):` labels → `SERIAL EDGES:`.
- **F-12** edit, partly · `part29.md` B21d.08, B21d.09: SOURCE, FALSIFIER and CONTROL and GATE written out (were "as B21d.07"). The other THIN cells (GLOSSARY, ADVANCES, DEPENDS ON) and B27.27's READING fields: no action — K7 found none blocks execution, and a READING carries no body (§5.3).
- **F-13** edit, partly (design document, ladder step 3: `V12_STRUCTURE_part2.md` §5.3's closed list `edit, small build, build, wide mechanical, calibration, content, design, reading`): 17 COST lines across K7 and K10 now open with a listed class, the author's phrase kept in brackets (B11F1.04, B20.99, B25.99, B20.10, B41.11, B41.14, B41.08, B27.99, B11F2.05; K10 #17's B38.13, B38.76, B38.85, B38.88, B38.99, B39.37, B40.29, B39.99). The 15 POINTER/READING/HELD items without a tier: no action — §5.3 gives a READING no body and E-5 asks a POINTER for "what it does, target files and symbols, the gate", no COST line; they commit nothing.
- **F-14** edit · `PYTHONHASHSEED=0` prefixed on 13 item-level seeded commands (B41.07; B20.12; B20.21 ×3; B25.03, .14, .15; B37.05, .10, .16 (`boot.realm`); B11F2.03; B11F2.05 `loops`; `register --check` left unprefixed: it reads no seed); B20.06 and B20.14's "moved or equal, recorded" arms rewritten so the hash's move is tied to a condition read off the report/tallies (can now be wrong); B27.12's `modules/social_contest` arm (no test there: `ls` → `__init__.py`, `roll.py`) → `engine/season/tests/test_sc_hearing_evidence.py` (B24.19's test of `standing`) and `tests/valoria -m social_contest` (`pytest.ini:60`). B27.08's grep-count equality: no action (a registry code reads; it can be wrong).
- **F-15**, **F-16** already fixed by K7.
- **F-17** re-checked, no cut: B27.01 (11.6 KB, the largest of K7's list) opened line by line — every line is SOURCE/INSTRUCTION edit text, test bodies, gate commands; no finding or evidence prose. E-12 permits an over-budget item whose body is only the exact edit text; cutting it would remove executable text (§5.4). The same holds for the K7 list by K7's own reading ("their text is the copied edit"). Not widened: a size scan of parts 29–43 finds 70 items over 6 KB; not in any finding, not trimmed.
- **F-18** edit · `part29_cont.md` B41.11 WHERE and GATE: the fallback `test_names_vocabulary.py` / `test_export_names.py` (absent) → the existing `tests/valoria/test_names_chain.py`, run in the GATE.
- **F-19** edit (ladder step 1, superseded) · `part29.md` B21d DIALS: the four CI bands' open question marked decided by part 2 §4 rows 51, 52 and B98.42 (`BLOCKED (A-114)`, B99 quotes).
- **F-5** B20.10: fixed with F-1. B20.17: re-checked, already copied (B20.17's INSTRUCTION holds CHO "Data rows" verbatim, `27_MB_D_the_commander_as_chooser.md:200-202`, with U-9's `centre`). No edit.

## K8 (parts 33 to 35)

## K9 (parts 36 to 39)

- **#2** edit (encoding mover) · `workplan_v12_part38.md` B33.05 heading, position row, FALSIFIER control, GATE, HASH MOVERS; B33's RE-PIN line; `workplan_v12_part38_cont.md` B33.99 step (3) and the FILE CENSUS `carriers.py` entry; `workplan_v12_part2.md` §1.3 B33 row (encoding 7 → 8), §1.3 totals sentence (22 encoding movers), §3 B33 row (05 added). Basis read: `state/world.py::_object_head` (`:260-268`) encodes every dataclass field name and the field count, `_encode_into` folds no absent field; `Office` is a dataclass in `World.offices` (`carriers.py:1019`, comment `:1034-1036`); B32 leaves both fields to B33 (`workplan_v12_part34.md:99`). The control is now read on act tallies, since the source's "every hash is the base hash" cannot hold.
- **#6** edit · `workplan_v12_part38.md` B33 head: its `EXPECTED RED UNTIL B33.99` line said "none beyond each item's own line" while no B33 item carries one; rewritten in R1's batch-line form naming `_realm_goldens.py` and `test_go07_canonical_digest.py`, first mover B33.01. B35, B23, B30, B36, B31: re-checked, R1 repair 4's batch lines present (`part36.md:46`, `part37.md:43`, `part37_cont.md:34`, `part39.md:41`, `part39_cont.md:32`).

## K10 (parts 40 to 43)

## Part 2 §4 against part 44

## For Jordan
