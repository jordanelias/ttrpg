# Evaluation of workplan v11: one settled disposition per position, and what v12 takes from it

## Status: EVALUATION RECORD (stage 5 of `STAGES.md`, the settle-and-merge of lanes E1 to E5; reference, resolves nothing at runtime, CLAUDE.md §0.05; not canon; deleted when workplan v12 is adopted)

## Read at: the working tree of 2026-11-12 (the lanes read HEAD `a248c67`; this pass re-opened the tree where it says so). Producer: the settle lane (Opus), one round, no sub-agents (the judgments here are the settling of disputed calls, which one reader holding all eight lane files can make; a second reader would have re-read the same rows).

**What this is.** Jordan (2026-11-12): *"The penultimate step will be to read and evaluate the entirety of workplan v11 and gap register."* Every position of `workplans/valoria_master_workplan_v11.md` and `_part2` to `_part17` has one recorded disposition (`master/EVALUATION_ORDER.md`'s six: DONE-IN-CODE, SUPERSEDED, WRONG, STILL-NEEDED, MISSING-DEP, RULED-CONFLICT). Five lanes filed them (`master/eval/E1.md` to `E5.md`); this file settles them: it applies Jordan's answers A-100 to A-114, applies the mass-battle abstraction's supersession table, re-checks the weakest calls, gives each id one disposition across the lane files, and hands stage 6 the carried items (`master/eval/V12_INTAKE.md`). The gap register's evaluation is the companion `GAP_REGISTER_EVALUATION.md`. Words follow `unified/U1_GLOSSARY.md` (A-98: attribute, skill, skill score, martial skill, derived score; `unified/MB_LEXICON.md` for armies; **lap** for the season's scene-budget round, A-101, where v11 says "round" in that sense).

## 0. The parts

| part | what | how made |
|---|---|---|
| this file | counts, what was settled and why, the rules, findings for stage 6 | written |
| `_part2` | the settlement ledger (every row of E1 to E5 this pass changed or re-cited, keyed `E<k>:<line>`) and the one-disposition-per-id table for v11 ids | generated from the settle record |
| `_part3` to `_part6` | lane E1's table (the head, `-02`, `-03`, `-12`) and its carry-forward blocks | copied by script, byte for byte |
| `_part7` to `_part9` | lane E2's table (`_part4`, `_part5`) and blocks (with its §3 carried v9 entries) | copied |
| `_part10` | lane E3's eight tables (`_part6` to `_part9`) and blocks | copied |
| `_part11` to `_part14` | lane E4's table (`_part10` to `_part13`) and blocks | copied |
| `_part15` | lane E5's tables (`_part14` to `_part16`) and blocks | copied |

The copies keep each lane's own call as the record; where the ledger (`_part2`) changes a row, the ledger governs. The lane files themselves are untouched. Every copied part was checked by script against its source range (equal bytes).

## 1. Counts

Rows are the lanes' rows (a position the evidence splits has two rows; `EVALUATION_ORDER.md`). Counted by script from the tables, before and after this pass.

**Workplan v11 (lanes E1 to E5)**

| | rows | DONE-IN-CODE | SUPERSEDED | WRONG | STILL-NEEDED | MISSING-DEP | RULED-CONFLICT |
|---|---|---|---|---|---|---|---|
| as filed | 1,692 | 724 | 296 | 75 | 586 | 6 | 5 |
| settled | 1,692 | 693 | 350 | 67 | 565 | 17 | 0 |

**By source file, settled** (as filed in brackets where different)

| source | rows | DONE-IN-CODE | SUPERSEDED | WRONG | STILL-NEEDED | MISSING-DEP | RULED-CONFLICT |
|---|---|---|---|---|---|---|---|
| E1 (head, `-02`, `-03`, `-12`) | 229 | 13 (12) | 71 (63) | 1 | 141 (148) | 3 (1) | 0 (4) |
| E2 (`_part4`, `_part5`) | 117 | 21 (22) | 35 (30) | 0 | 59 (63) | 2 (1) | 0 (1) |
| E3 (`_part6` to `_part9`) | 574 | 352 (392) | 131 (124) | 9 (5) | 78 (53) | 4 (0) | 0 |
| E4 (`_part10` to `_part13`) | 642 | 284 (278) | 78 (43) | 54 (69) | 221 (251) | 5 (1) | 0 |
| E5 (`_part14` to `_part16`) | 130 | 23 (20) | 35 (36) | 3 (0) | 66 (71) | 3 | 0 |

**Both deliverables together (2,052 rows: 1,692 here and 360 in the gap register):** settled DONE-IN-CODE 843, SUPERSEDED 507, WRONG 71, STILL-NEEDED 609, MISSING-DEP 22, RULED-CONFLICT 0 (as filed: 879, 452, 81, 621, 14, 5). The carried rows (631) collapse to **273 v12 intake items** once the same position seen in several v11 parts and register rows is merged (`master/eval/V12_INTAKE.md`).

**What moved (both deliverables; 177 of the changes are in lanes E1 to E5).** 192 rows changed disposition and 32 more were re-cited (same disposition, new reason): 13 changed and 24 re-cited by Jordan's answers or by the ladder settling an item that was his; 2 changed and 7 re-cited by the mass-battle supersession; 17 WRONG calls reversed; 7 E7 extract rows changed and 1 re-cited on a full re-read; 153 changed to give one id one disposition across the files (87 of them E3 rows, 69 of those the hole rows v11 parts 8 and 9 list, which E3's own convention 6 left to the register lanes). The ledger (`_part2` §1) lists every one with its reason.

## 2. Jordan's answers applied (A-100 to A-114)

Every row whose call rested on a question Jordan has now answered was re-dispositioned with the answer cited. The for-Jordan list is `master/eval/EVAL_FOR_JORDAN.md`; it now holds **no open question**.

- **A-114 (EVAL-1).** v11 P10 (no probe or batch close past two seasons) and P16 clause (1) **stand** as v12 head rules, with one exception: the longer re-take of THE NINE runs **once, as the plan's very last item, after M5**. The RULED-CONFLICT on P10 becomes STILL-NEEDED (carried as a head rule). The four-season `measure:` strings of R-04, R-05 and R-09 (the `-02` rows, SUPERSEDED by the instruction suite) are re-cited: read at two seasons, or left as they stand until the end-of-plan re-take; IS-A-13's per-milestone re-take does not run.
- **A-103 (EVAL-3 = J-E2-01 = J-E3-1).** CR-91's claim gate on `march` (part 3) is SUPERSEDED; the carrier (parts 1, 2, 4, 5) is STILL-NEEDED as occasion and as context for regard and legitimacy; IN-36's cap of one march per season into a territory stays. E1's and E2's RULED-CONFLICT rows are settled; M10 (E3, SUPERSEDED on the same reading) is confirmed; the residue rows §1a-M1res and V9-14 are re-cited (the cap and `guards` ON only).
- **A-104 (E-3, M31 (b)).** Management orders cost no scene budget and may prompt scenes: M31 (b) and E-3 SUPERSEDED; CL-MGMT's M31 hold lifted (four rows re-cited).
- **A-108 (E-4).** Stored manner offsets allowed: E-4 SUPERSEDED; M34 becomes STILL-NEEDED (E3 had it 'as shipped, no offset'); CL-PERSON's E-4 hold lifted (four rows re-cited).
- **A-111 (H-1).** The owed ledger rows are written as relayed: H-1 stays STILL-NEEDED, re-cited.
- **A-110 (J-E3-2).** A1-80 SUPERSEDED: `RemoteTrigger` is not added; E3 Block 8 (a) is dropped.
- **A-112 (combat reads skill scores through the skill table; `faculty` dropped).** No v11 row is changed by it: CR-85 (a), the landed `faculty` input, stays DONE-IN-CODE as a fact of the tree, and A-112 is a session item that replaces it in the PC batches; the question that held CR-85's design (ED-IN-0351, *"reopened with `faculty`'s role"*) is answered by it, and CR-85's hooks half (ED-IN-0331) stays carried.
- **A-102, A-106, A-107, A-113.** A search of every carried row for their subjects (`boot`, a skill lapse, `moved_by_*`/traits, equipment matchups) found no v11 row they decide; A-102's batch is U3's B03c, A-113's is U3's B31.
- **Settled by the ladder, recorded in `EVAL_FOR_JORDAN.md`:** EVAL-2 (the army verbs' menu door) Option B, so CR-46's clause and CR-52 are SUPERSEDED (step 2, irrelevant: the barred list it bridged is removed by `14_VERBS_MILITARY_C_the_muster.md:210` and `_D:185`, and `IS_A_NINE.md` §6 counts only chooser-formed acts); J-E3-3 (v11's "4.6"): M13 and A1-44 stay WRONG (step 1: ED-GO-0002 rules the 4.7 series and is the one owner; v12 writes no version number); J-E3-4 (the common-fact store): A1-48 stays DONE-IN-CODE (steps 3 and 4: AX-7 and v11's own option (a); no store is built).

## 3. The mass-battle abstraction (A-100) and the round (A-101) applied

`master/mb_abstraction/MBA_DESIGN_part3.md` §8.2 lists the v11 positions and register rows it touches. Applied: **CR-12** (three rows) and **ED-MB-0045's melee item** are re-cited to MBA-04 (they were SUPERSEDED already, by `04_MB_cr12_linear_law.md`, whose steps 2 and 3 MBA-04 itself supersedes; CR-12's step 1 instrument repair is carried as that proposal's step 1); **MB-07r** (two rows, DONE-IN-CODE) becomes SUPERSEDED (retired with `POOL_QUALITY_SCALE`, which MBA-04 deletes); **ED-1043** (two rows) stays STILL-NEEDED, re-targeted: its trigger fires at MBA-04 step 0 in B19. CP-T04-04, CP-T04-10, MB-08 and CL-TROOP are untouched (§8.2: "none touches the contact"). The register rows (H-361 narrowed; H-150, H-97, H-348 stand) are in the companion file.

A-101: `master/pc_round/PC_ROUND_SPEC.md` and `_part2` supersede no v11 position by content (the only handles they name are F-PC-04 and ED-PC-0033, neither a v11 row). Its effect on v11 is vocabulary: where v11 says "round" for the season's scene-budget round (A1-50's "more rounds", CP-T04-04's "a round after it is declared"), the prose word is now **lap**.

## 4. One disposition per id: the rules this pass applied

The lanes read different v11 parts, and v11 restates a position in several of them (the state index in `-03`, the entries in `-04`, the carried v9 table in part 12, the amendments in part 14, the hole rows in parts 8 and 9). **167 ids** were dispositioned differently by two or more lane files (found by script). Each now has one settled disposition, or one per part where the evidence splits the position (37 ids are carried in parts: a landed part and a residue, a superseded part and a carried part). `_part2` §2 lists them; the register ids are in the companion's `_part2` §2. The rules, applied in this order:

1. **Session content wins, but only where it was opened** (`STAGES.md` stage 6). A SUPERSEDED call whose replacing section a lane opened beats a STILL-NEEDED call that rested on 'unbuilt' alone (E4's B10-18b rows, for example, carried one generic evidence cell; E1 and E2 had opened `06_FA_decree_binds`, `14_VERBS_MILITARY_B_train`, `14_VERBS_MATERIAL_D_paper`). A SUPERSEDED call resting on a proposal's head only (E3's `[head only]`, several E5 `UNVERIFIED`) loses to lanes that opened a session text saying the position **stands** (WR-01, GO-05, IN-18, IN-52, SC-07, PC-08).
2. **A session item that carries a position "as written" does not supersede it**; it schedules it. Where it restates the whole body (IS-B3-FA-05 for CP-T09-08: WHERE, FALSIFIER, GATE), it does.
3. **A tree artifact beats a citation.** A test file or symbol that exists (IN-12's nine `test_in12_*.py`, CP-T03-11 composed into IN-59, `odds_of` for M32) settles DONE-IN-CODE.
4. **The lane that read the text governs its rows.** Part 14's amendments were read by E5 and copied unjudged by E4 (E4's head says so); part 15's M22 to M40 design lanes were read by E5, part 6's questions by E3; for an M-number, a live part-15 design lane carries the id (M36, M39, M40's horizon term).
5. **A register row is governed by the register lanes** (E6 to E8 read every field; E3's convention 6 defers to them), except where the register lane called a row a record while v11's 'what closes it' still owes work no session item supersedes (H-11, H-125 with CR-22; H-173; H-199; H-222; H-224 with CR-29; H-217 with CR-35), and except where a 'missing' dependency is in fact a v11 position (H-47, H-62 with CP-T07-02; H-90 with CR-35 to CR-38; H-181 with CR-32).
6. **WRONG means the premise is false at the tree, or the gate cannot observe what it claims.** A v11 cut whose asked thing is already in the tree is DONE-IN-CODE; one whose remaining build a session item carries is SUPERSEDED; one v11's own ladder found to rest on a false N-line stays WRONG (§5).

**Merged items (one item, several ids).** H-145 with NM-W9 (b); H-101 with CR-09; H-214 with CR-29 (and H-224's measurement, A2-43, ED-IN-0298); H-25 and H-106 with CR-98; H-89 with CR-07; H-108 (b) with IN-48; H-47 and H-62 with CP-T07-02; H-181 with CR-32; H-217 with CR-35 (and SC-04's residue); H-11 and H-125 with CR-22; H-90 with CR-38; H-222 with A1-87; H-314 with CP-T06-03/-04; H-325 with H-326 (r). The list with lanes and batches is `V12_INTAKE.md` §1.

**Two lane conventions reconciled.** E3 filed a closed ask whose decided state is the tree (a fixture, a refusal to build) as DONE-IN-CODE; E4 filed v11's cut, declined and dropped rows as WRONG ('do not carry'). Rule 6 applies one meaning: of E4's 69 WRONG rows, 54 keep WRONG (false premise or v11's false N-line), 15 are reversed (§5).

## 5. The weakest calls, re-checked

**Every WRONG call was opened (81 as filed).** 64 confirmed, 17 reversed; a reversed WRONG is a finding.

- *Confirmed, with the evidence re-run:* E1's CP-T09-06 (a) (`offices.yaml:206` `conferral: null`, not `appointed`); E3's M13 and A1-44 (ED-GO-0002 read: the 4.7 series), SC-03b's residue and CT-4 (v11 part 8 :140, :182: the corpus observable cannot be met as worded), ER-C8 (part 8 :222: a figure its own arithmetic does not reproduce); E4's rows on subjects absent from `engine/` and `modules/` (re-grepped: no Seizure Accord, Recognition Ceremony, Case Board, Intelligence Embargo, out-of-bounds rule, `params/` tree; Institutional Pressure, Popular Will, Disposition Track appear only in `references/` registries; Turmoil only as a display name in `engine_params/names.json`; Coup Counter and Niflhel only as `[STRUCK-MECHANIC]` case lines), the Key-adjudicator rows (retired, ED-IN-0232), the ladder-rejected arc conditioners, and v11's own false-N-line cuts (CP-T06-06, REM-51, REM-45 on the dead `history` term, TL-B5.1, CP-T04-09, DEC-3, DEC-4 and DEC-6 to DEC-11).
- *Reversed:* G-25 → SUPERSEDED (`12_ARCS_arcs_as_staged_goals.md` §Resolution 1 to 4, opened: a case's counter becomes stages of the holder's goal); REM-20, REM-40, REM-41 (and their amendment rows) → DONE-IN-CODE (`fold_kinds`, `EVENT_KINDS` and `_act_events` exist: 3 and 13 hits); CP-T02-08 → DONE-IN-CODE (`odds_of` at `seam/wrappers/sigma.py:350`); CP-T05-05 → SUPERSEDED (`14_VERBS_SOCIAL2_C_case_question_confession.md` builds the question route); CP-T02-04 → SUPERSEDED (A-35 and `14_VERBS_BINDING_C_turnover`); CP-T07-02's HR-7 → STILL-NEEDED (a rider on the host, E5); DEC-1 and DEC-12 → SUPERSEDED (their owners H-187 and H-111 are superseded). The register's H-209 and H-225 are in the companion file.
- *E4's correction (b) of v11 is itself reversed:* ED-417 cites `loop/census.py:39` 'NO CLOCK GENERATES ANYTHING'; the text is there, wrapped across lines 39 and 40, so E4's grep for the whole phrase on one line found nothing. The cite holds.

**SUPERSEDED calls resting on a closure row only.** This pass opened the cited section behind 30 of them, 27 in the register (listed in the companion file) and 3 here: CP-T05-01 and CP-T05-02 (i) at `05_SC_playable_hearing_B.md:171` with closure G-11 (`U5_FINDINGS_CLOSURE_U5c.md:80`), and CP-T10-08 at `23_STORY_B_a_house_continues.md` (a marriage is an instrument formed by `covenant`, no `marry` verb). All held; the three v11 rows also won their id conflicts under §4 rule 1.

## 6. Errors in v11 the lanes found (verified here)

- **Part 12's batch column is stale** after the closes of B10-10b, B10-11, B10-11b, B10-13, B11-S2 to S5 and most of B10-12 (E4's head; the tree's test files agree). The tree, not the label, was used.
- **ED-MB-0070 and ED-MB-0071 cite deleted closing tests.** `tests/valoria/test_mass_battle_byte_exact.py` and `test_rout_contagion.py` are absent from the tree, removed by commit `add960c` (#552, in this clone); those closures now rest on `bat.py`/`config.py` and the CI step.
- **Two LEAVE triggers have fired.** ED-SC-0001's ('CP-T03-03 or CP-T03-04 builds'): `test_cp_t03_03_kit.py` and `test_cp_t03_04_arms.py` exist; carried as a measurement item in B15. ED-1043's: fires at MBA-04 step 0 (B19).
- **Stale entries:** CR-85's 'moves to B10-Z as HELD' (the build is in the tree, E2); CR-07's '13 rows' (15 now); CP-T09-06's 'replacing `appointed`' (the value is `null`).
- **Dangling canonical cites found while checking ED-930:** `modules/mass_battle/core/state.py:26,28` and `core/exchange.py:46` cite `params/factions/stats_1_7_scale.md` as canonical; the file is not in the tree (forked). A comment fix for B03's hygiene items.

## 7. For stage 6 (the fold)

1. Take the carried items from `master/eval/V12_INTAKE.md`, not from the lane tables: it is deduplicated, placed by lane and batch, and points at each carry-forward block by lane file and line.
2. Nine new batches are proposed there (§3), each once, with their dependencies, reconciled from the 21 batch names the lanes proposed (E1 5, E2 3, E4 4, E5 5, E6 4; three not taken); the graph with U3's batches is acyclic, and the new FA and SC batches lie on a critical path of 22 batches.
3. Retired items do not enter v12 in any form; each has its reason in the ledger. Items carried as v12 head rules (22: P1 to P16, V1 to V4, three `-00` risks) are not batch items.
4. Where a carried row's text predates an answer (CL-PERSON's 'HELD on E-4', P16's 'waits on EVAL-1', CR-91's gate), the ledger's reason governs; the intake prints it beside the entry.
5. The fold must keep one owner of `world_q.hearing` (CP-T05-02 (i) and `08_FI_05_evidence-interface_B` both name it; U3 §6.3), and must drop CR-94 from IS-B2-FI-02's B11 list (§4 rule 1; `[ASSUMPTION]` recorded in the ledger).

## 8. What this pass could not check

- **The lane tables were not re-read row by row in full.** The 2,052 rows were parsed by script, every changed and every conflicting row was read with its evidence, every WRONG row was read, and the heads and for-Jordan sections of all eight files were read in full; the 1,800-odd rows that no rule, answer or conflict touched keep the lane's call unread by this pass beyond the script's parse.
- **The carry-forward blocks** (about 1.9 MB) were copied, not re-read; where a block's text predates an answer, the ledger and the intake say so, but a block may still contain a sentence the answers overtake.
- No test, seeded run or `aperture` was run (the order bars them); DONE-IN-CODE rests on a symbol or test file existing. The clone is shallow; commit SHAs older than its boundary do not resolve.
- E2's extra dependencies for the arc batch (B23, B36) and the CR-48 → CR-49 edge were not confirmed from v11's entries; both are marked in the intake.
- Three of the 37 E7 rows re-read (H-166, H-170, H-222) were read to their first 2,600 characters of `cite:`, not to the end.
