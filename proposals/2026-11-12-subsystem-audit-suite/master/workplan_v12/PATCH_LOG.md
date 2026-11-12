# Workplan v12 — patch log of the cross-part patch lane (P)

## Status: WORK FILE (resolves nothing at runtime; deleted when v12 is adopted)

One row per patch. `H2_NOTES` = the line of `H2_NOTES.md` the patch answers. Every edited site carries the
marker `Patched: P-nn`; `grep -n 'Patched: P-nn' workplan_v12_part*.md` lists them. P-01 to P-23 were applied
by the first run of this lane (killed by a container restart before it wrote this log); their rows were
reconstructed from the markers in the parts, each site opened. P-24 was half-applied by that run (the
position row only) and finished by the second run.

| id | H2_NOTES | part, handle | what changed |
|---|---|---|---|
| P-01 | :20 (A11: `U5c_VERBS_residue_and_governance_owner` §3 owed to B11); :12 (A16: VRES §3 step 2 reads `present_persons`) | part 17: NEW B11.83 (steps 1, 3), NEW B11.84 (step 2); its position rows, SERIAL EDGES; part 17_cont B11.99 DEPENDS ON | the whole of §3 (VRES §3) added to B11 as two items after B11.61 (CP-T06-04's deposit) and the first half's FRES §1 item (`present_persons`, B11.08) |
| P-02 | :35 (A27: B30 must take the stand draw's officer-felled call) | part 37_cont: NEW B30.10; RE-PIN, SERIAL EDGES, position row | the trigger table's officer row (`26_MASS_BATTLE_rout_pursuit_and_giving_ground` §1, MGR §7) added as B30.10 after B30.03 |
| P-03 | :39 (A28: B22 must keep the settlement-only restriction on `migrate`) | part 33: B22.06 step 3, GATE, DEPENDS ON | a step keeping B12c.14's stamper restriction; B12c.14's test added to the gate |
| P-04 | :27 (A24: B22 holds A2's `mustered` gate arm) | part 33_cont: B22.35 TESTS, GATE, DEPENDS ON | the mustered-prisoner arm of `14_VERBS_PHYSICAL_A` A2's gate added; edge on B29 named |
| P-05 | :20 (A11: the fatigue half of the `Drawn` write to B22) | part 33: B22.04 step 5, TESTS | the per-part `last_field` write on a `Drawn` field for both sides, with its test |
| P-06 | :24 (A10: the `"a task"` prize row moved to B22) | part 28: B12c.08 step 5, WHERE, GATE; part 10_cont2 B07.03 note; part 37 B23.04 DEPENDS ON | the row lands with the first shape-(b) row in v12's order, `sabotage` (B12c, S15), not `move` (B22, S17); both other parts point at B12c.08 |
| P-07 | :46 (A38: BYZ_B gate 3 to B40) | part 43: B40.04 step 6 | BYZ_B gate 3 copied into the item that builds the `roga` case file |
| P-08 | :46 (A38: VEN_D scenario to B40); :41 (A43: the Counting-House gate) | part 43: NEW B40.29; UNDECIDED (U11), position row; part 43_cont B40.27 note, B40.99 DEPENDS ON, SERIAL EDGES | B33.44 was a POINTER leaving the case file to B40 and B40 had only the gate (B40.09): the case file and report rows land at B40.29, before B40.09 |
| P-09 | :45 (A41: the `minority` row and retiring `troubled` belong to B39) | part 42_cont: B39.27 step 5; part 41 batch head UNDECIDED 7 | `minority` row carried at B39.27; retiring `troubled` not carried (no source orders it; `30_WR_A` keeps it in `era_conditions`), said in both parts |
| P-10 | :44 (A39: `entry_stamina`/`lull_recover` back edge, B19 ledger step 3) | part 26: NEW B19.28; B19.01, B19.08 notes; position row; part 26_cont B19.22 note, SERIAL EDGES; part 33 B22.03 step 5; part 39_cont UNDECIDED (2) | step 3 of `16_PESSIMIST_MB_one_stamina_ledger` and the `fatigue.lull_recover` row land in B19.28; B22.03 joins the one `fatigue` block; B31.06/.07 become the remainder |
| P-11 | :24 (A10: B21 must delete its verbs from `contest_owed`) | part 14: B21.09 step 5 (`establish`); B21.14 step 7 (`confer`, `revoke`, `succeed`) | each commit that gives a row its `contests:` deletes it from B07's roster |
| P-12 | :24 (A10); :33 (A37: `seize` stays until B26) | part 33_cont: B26.11 step 6 | `seize` deleted from `contest_owed` in the commit that gives it `contests:` |
| P-13 | :15 (A09: CAP Part B rows B5–B7 restate items written in full); task brief (B05 CAP rows in parts 8 and 9) | part 9: batch head UNDECIDED (1) | resolved at the merge: B7 already a POINTER in part 8 (B05.13); B5 split, not doubled (B05.14 social, B05.58 combat); B6 only in B05.60; no state changes, the AT OPEN steps stay |
| P-14 | :23 (A08: A09 has a duplicate equal-ranks test) | part 9: UNDECIDED (5); B05.51 GATE | the owner is part 8's B05.23 (`test_u1_two_inputs.py::test_equal_trained_ranks_at_plain_are_even`); B05.51 and B05.59 write none |
| P-15 | :17 (A13: B10.69's test may duplicate the first half's) | part 13_cont: B10.69 | resolved: B10.11 writes no beneficiary test, so B10.69 is the one owner; nothing dropped |
| P-16 | :45 (A41: B38.14 expects a duplicate test) | part 40: B38.14 TESTS | `test_routine_release_…` is not written; B12a.05's test is the one owner; B38.54 a POINTER reads it at B38.99 |
| P-17 | :46 (A38: overlap with B32 on SYN_A owners); :30 (A34) | part 38_cont: B33.35 | B32.03 owns the `debt` record rows; B33.35 adds only its note and its own steps |
| P-18 | :46; :30 | part 38: B33.19 | B32.31 (`audits_due`) and B32.27 (`Office.audit_at_exit`) land first; B33.19 writes only its own steps |
| P-19 | :18 (A04: B03 an encoding mover; B03.99's re-pin); :21 (A05: B03.86 a behaviour mover) | part 4: B03 batch head RE-PIN | the one re-pin records both movers; B03.99's commit text governs |
| P-20 | :12 (A16: the two `p1` tests already landed in A16's half) | part 17: B11.59 TESTS, GATE; B11.62 POINTER body | the two tests are read from B11.08's `test_fi_referents.py`, not written a second time |
| P-21 | :12 (A16: FI_A edit 5's tiers landed in A16's half) | part 17: B11.52 | resolved: B11.09 writes FRES §6's roster text; B11.52 wires the two tier members only |
| P-22 | :12 (A16: the flip item owed by A17's half) | part 17: NEW B11.85; position row | the telling ships `unshared_first` and `seen_since_move` (FRES §6; `08_FI_02` edits 4–5) |
| P-23 | :12 (A16: B11.99 carries `08_FI_01` edit 7 as reading records) | part 17: B11.99 position row; part 17_cont B11.99 step 2 | edit 7 copied into B11.99's reading records |
| P-24 | :6 (A15: (b)'s union stays in B21b, A21 must know); :26 (A21 reads it as B21's) | part 15: NEW B21.79 (row and item), UNDECIDED (U3), "Not in this half", B21.57 DEPENDS ON, B21.99 row; part 15_cont SERIAL EDGES, FILE CENSUS, B21.99 DEPENDS ON | conflict: neither part carried CP-T09-07 (b)'s `sides_of` union. Ladder step 4 (precedent: the intake `:246` and AM-F-13 put it with `IS-B3-FA-05`; B21b.02 and B21b.04 need it first): lands in B21 as B21.79, before B21.57 |
| P-25 | :17 (A13: the ARC-47 gate moves to B39) | part 42: NEW B39.37 (row, item); SERIAL EDGES; B39.99 row; part 42_cont B39.99 DEPENDS ON | no part carried `test_arc47_on_arm_off_arm_and_lie_arm` or ARC-47's case on the realm; the gate, its case file (seed content) and its test added after B39.14 |
| P-26 | :20 (A11: B21 owes `01_CORE_predicates_name_their_clause` step two's four keyed rows) | part 15: NEW rows B21.80 to B21.83, B21.99 row; part 15_cont: NEW items B21.80 to B21.83, SERIAL EDGES, B21.99 DEPENDS ON | one item per row (`confer`, `establish`, `revoke`, `oblige`), the source's "one commit per row"; kind spelling follows an existing keyed typed row (ladder step 4, marked) |
| P-27 | :24 (A10: CP-T03-06 moved to B15, POINTER in B14) | part 18: NEW B15.14 (row, item); B15.99 row | B15 had no item for it; the measure-then-cut-or-design item added, the build HELD on the design |
| P-28 | :39 (A28: CR-61's citation clause belongs to B28; A35 must carry) | part 35: NEW B28.33 row, B28.99 row; part 35_cont: NEW item B28.33, B28.99 DEPENDS ON | the citation (a `dispensation` served by `give`) added after B28.32; STOPS IF B24a not on base; edge B24a → B28 proposed (H2_DECISIONS HD-16) |
| P-29 | :21 (A05: §I's falsifier moves to B34's gate; B21 and B34 call `faction_q.standing`) | part 15_cont: B21.72 step 7; part 25_cont: B34.04 instruction and WHERE; B34 BATCH GATE | neither caller nor the moved falsifier was carried; added as the source's two callers and its grep |
| P-30 | :17 (A13: content left for BA1 includes the `unaware:` marks) | part 18_cont: NEW BA1.12 (row, item); BA1.99 row and DEPENDS ON; part 13 B10 DIALS line | BA1 had the alignment cells (BA1.04), relation rows (BA1.08) and manner offsets (BA1.02) but not the two marks; added |
| P-31 | :45 (A41: part 40's dials line says the second half sets `stamp_own_side`) | part 41: batch head UNDECIDED 1 | resolved by reading part 40: its DIALS lines name no setter; part 41's line stands; no edit to part 40 |
| P-32 | :19 (A06: B04 re-runs the exporters after its rebase in S6) | part 7: B04 PARALLEL line | the merge order and the two exporter runs written into B04's block |
| P-33 | duplicate found by script (B19 split across parts 26/27) | part 27: B19.55 TESTS | `test_no_commander_reads_the_literal_four` is written once by B19.02; B19.55 reads it |
| P-34 | :30 (A34: SYN_A gate 3's `comply` arm moves to B33) | part 38_cont: B33.27 GATE | the arm copied into the item that lands PAP_D edit 7 (`forborne`) |

## Checked and needing no edit (class (a) notes whose target already carries the item)

Each was opened in the named part: U5d_FA §3 in B32 (B32.21); M8, §1b-3, A2-14 (B21.77 POINTER → B21c, A25's B21c.04/.05); CR-22, H-11, H-125, IN-52, DEF-7, CL-EVENTS, CP-T10-01/-02/-03, CP-T08-06, H-171 in B12b (part 24 position rows); G-05, CR-49, CP-T08-01/-03/-04, CR-40, CP-T08-08, P14 in B12c (part 28); CR-67 in B24a (B24a.02); CP-T08-05 in B12c (B12c.17, HELD); the recovery half of `U5d_WR_owed_edits` §3 (B37p.05); A16/A17 overlap on `IS-B2-FI-02`, the CP-T06 cards and `IS-B2-FI-07` (part 16 carries none of them as items: its B11.01 is the FI-07 design and B11.68 the build; no duplicate); B11.74's moved arm (B25.07 READING); VRES §4 (B07 POINTER → B21.07); `06_FA_decree_binds` edit 4 only at B21.23; `IS-B2-CHAR-02` step 6 (`played_by`, B34.15 with `01_CORE` edit 2); B03c's re-point of CI-05's reader (B03c item step 7); B19 NAMES for `between_turn_recovery`, `base_combat_pool` (part 26); `derive_command` retires at B19.55; `U5b_MB_residue` §5, §9 R-29 (B20.13, B20.07); `contest_owed` deletions by B23.14, B25.14, B28.06, B28.09, B32.26; `wrapper.fight`'s signature (part 10_cont UNDECIDED (3): kept once, B06 first); `IS-MB-B1` (B22.01); `world_q.passage_granted` (B23.05); nesting cap and A-72 (B30.02, one setting); B19.52 (B20.08); UMR §5 (B31.11); G-14, TL-B4.2 (B28.31, B28.32); CR-74 with PAP-A edit 5 (B21s.02); PAP-G item 1 (B32, part 43 line 73); SYN_B gates 2, 4 (B39.32); SYN_A gate 4 (B33's COL_B item SOURCE); Hafenmark's heir-title row (parts 14/15 place nothing in B32); W-2 (B36; B39.33 a non-carry POINTER); `body_mend` (B37p.05); the `case` kind's two writers (B25.09's SITE step writes one row); B38.14/B38.53's `test_stamp_own_side…` (one writer, B38.53); B11.09/B11.85's two-hop tests (B11.85 reads them); SYN_B gate 5 (rides on B32.10, BLOCKED: no move possible until it unblocks); CR-63's writ rows (B24a.08's STOPS IF moves a row to B28 only when its writ path is absent; no B28 item owed in advance).

## Classification of every line of `H2_NOTES.md`

(a) a body-part patch or check; (b) a head decision for H2 (`H2_DECISIONS.md`, HD-nn); (c) a question for
Jordan (`V12_FOR_JORDAN.md`, J-nn). A line holds several notes; counts are per note.

| line | author | (a) | (b) | (c) |
|---|---|---|---|---|
| :1–:4 | header | — | — | — |
| :5 | A23 | 0 | 7 (HD-01, HD-02, HD-32, HD-33; the dial) | 0 |
| :6 | A15 | 3 (P-24; U5d §3 checked; M8 POINTERs checked) | 5 (HD-03, HD-23; three dials) | 0 |
| :7 | A07 | 0 | 4 (HD-35, HD-20, HD-33; the dial) | 0 |
| :8 | A03 | 0 | 4 (two dials, HD-36, `cast_attributes` noted) | 0 |
| :9 | A33 | 1 (`passage_granted` checked) | 3 (dials, two STOPS IF noted, IS-MB-05) | 0 |
| :10 | A20 | 4 (four routings checked) | 3 (dials, HD-26, fixtures noted) | 0 |
| :11 | A17 | 2 (overlap checked; B11.74 arm checked) | 4 (dials, HD-23, HD-33, CR-94 noted) | 0 |
| :12 | A16 | 5 (P-01, P-20, P-21, P-22, P-23; cards checked) | 2 (dials, HD-22) | 0 |
| :13 | A19 | 3 (placements checked) | 3 (dials, HD-23, keywords noted) | 0 |
| :14 | A14 | 4 (VRES §4, decree edit 4, B21.06, `:231` checked) | 3 (dials, BIND_C, `fa_probe` noted) | 0 |
| :15 | A09 | 1 (P-13) | 4 (dials, HD-21, order and carrier noted) | 0 |
| :16 | A18 | 0 | 3 (HD-23; stops and joins noted) | 0 |
| :17 | A13 | 4 (P-15, P-25, P-30; CHAR-02 step 6 checked) | 4 (HD-34, HD-20, dials, BA1 content) | 0 |
| :18 | A04 | 2 (P-19; CI-05 reader checked) | 3 (HD-20, HD-23, UNDECIDED noted) | 0 |
| :19 | A06 | 1 (P-32) | 6 (HD-18, HD-23 ×2, HD-33, CI-02, CI-09 files) | 0 |
| :20 | A11 | 6 (P-01, P-05, P-26; B19 NAMES, `derive_command`, B20 checked) | 4 (HD-23 ×2, HD-26, dials) | 0 |
| :21 | A05 | 2 (P-19, P-29) | 3 (HD-20, HD-24, HD-23) | 0 |
| :22 | A22 | 0 | 4 (dials, HD-33, KERN_B, ids) | 0 |
| :23 | A08 | 1 (P-14) | 3 (HD-21, dials, `stakes_ob`) | 0 |
| :24 | A10 | 7 (P-06, P-11, P-12, P-27; deletions, signature, IS-MB-B1 checked) | 3 (HD-27, HD-32, dials) | 0 |
| :25 | A12 | 0 | 4 (HD-20, HD-26, dials, U5a §4 noted) | 0 |
| :26 | A21 | 1 (P-24) | 3 (HD-04, HD-33, ids) | 0 |
| :27 | A24 | 2 (P-04; U5d_SE §2, §7 checked) | 2 (dials, `body_mend` checked) | 1 (J-01) |
| :28 | A26 | 1 (`derive_command` checked) | 2 (HD-30, dials) | 0 |
| :29 | A25 | 3 (IS-MB-01 step 4, A-72, M8 checked) | 3 (HD-05, HD-20, dials) | 0 |
| :30 | A34 | 8 (P-17, P-18, P-34; B32.18, SYN_B, Hafenmark, PAP-G, `body_mend` checked) | 5 (HD-06, HD-20, HD-27, HD-33, the dial) | 0 |
| :31 | A36 | 0 | 3 (HD-25, HD-21, dials) | 0 |
| :32 | orchestrator note | — | — | — |
| :33 | A37 | 2 (B23.14, nesting cap checked) | 4 (HD-07, HD-19, HD-29, dials) | 0 |
| :34 | A31 | 1 (G-14, TL-B4.2 checked) | 3 (HD-08, dials, VERD file noted) | 0 |
| :35 | A27 | 3 (P-02; B19.52, UMR §5 checked) | 2 (HD-09, six-arm note) | 0 |
| :36 | A29 | 0 | 6 (HD-10, HD-26, HD-22, HD-32, HD-37, dials) | 0 |
| :37 | A40 | 0 | 3 (HD-20, HD-31, dials) | 0 |
| :38 | A32 | 0 | 6 (HD-28, HD-11, HD-23, HD-31, HD-26, dials) | 0 |
| :39 | A28 | 3 (P-03, P-28; CR-63 checked) | 3 (HD-33 ×2, dials) | 1 (J-02) |
| :40 | A30 | 1 (`case` kind checked) | 3 (HD-12, HD-20, dials) | 0 |
| :41 | A43 | 1 (P-08) | 4 (HD-20, HD-13, HD-33 ×2) | 0 |
| :42 | A42 | 1 (W-2 checked) | 4 (dials, HD-30, HD-21, `majority_age`) | 0 |
| :43 | A35 | 2 (deletions, CR-74 checked) | 4 (HD-14, HD-33, HD-35, dials) | 0 |
| :44 | A39 | 2 (P-10; W-2 checked) | 5 (HD-20, HD-15, HD-33, NM-W5, dials) | 0 |
| :45 | A41 | 3 (P-09, P-16, P-31) | 4 (HD-34, HD-33, HD-23, dials) | 0 |
| :46 | A38 | 3 (P-07, P-08, P-17/P-18) | 3 (HD-13, HD-30, dials) | 0 |
| :47 | MF | — | — | — |
| **total** | | **83** notes, answered by 34 patches (P-01 to P-34; P-01, P-08, P-17, P-18, P-19 and P-24 each answer notes on two lines) and the checked list above | **151** | **2** |

"dials" in a (b) cell means the line's `DIALS AT CONTROL` members, which H2's table of settings (§7.8) collects
from every part's DIALS line by script; none was edited here.
