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
