# Evaluation of workplan v11, part 2: the settlement ledger and the one-disposition-per-id table

## Status: EVALUATION RECORD, generated (stage 5 of `STAGES.md`; reference, resolves nothing at runtime, CLAUDE.md §0.05; deleted when workplan v12 is adopted)

**What this part is.** Every row of lanes E1 to E5 whose disposition this settle pass changed or re-cited, keyed by the lane file and line (`master/eval/E<k>.md`; the verbatim copies in parts 3 to 15 keep the lane's call as the record), then every v11 id that two or more lane files dispositioned differently, with the settled call. Register ids (H-) are in `GAP_REGISTER_EVALUATION_part2.md`.

**Kinds.** ANSWER: re-dispositioned or re-cited by a Jordan answer (A-100 to A-114). LADDER: a for-Jordan item settled by the five-step ladder (CLAUDE.md §0). MBA: the A-100 supersession table (`master/mb_abstraction/MBA_DESIGN_part3.md` §8) applied. WRONG-R: a WRONG call reversed after its evidence was opened. REREAD: an E7 extract-only row re-read in full and changed. RECON: one disposition per id across the lane files. A row whose settled disposition equals its lane disposition was re-cited only. The table is generated from `overrides.py`/`recon.py` (the settle record, scratch) by script; the rule each RECON row follows is in the head file §4.

## 1. Settlement ledger, lanes E1 to E5

| source row | id | lane disposition | settled | kind | reason / cite |
|---|---|---|---|---|---|
| E1:38 | P10 | RULED-CONFLICT | **STILL-NEEDED** | ANSWER | A-114 (EVAL-1, Option A as amended): P10 STANDS as a v12 head rule: no probe and no batch close runs past two seasons; the single exception is the longer re-take of THE NINE, run once as the plan's very last item (after M5). |
| E1:44 | P16 | STILL-NEEDED | **STILL-NEEDED** | ANSWER | A-114: P16 clause (1) STANDS with the same single end-of-plan exception; clauses (2)-(4) as E1 found. |
| E1:72 | -02 §5 R-04 | SUPERSEDED | **SUPERSEDED** | ANSWER | re-cited, A-114: R-04's `aperture 4 0` `measure:` string is read at two seasons or left as it stands until the end-of-plan re-take; IS-A-13's per-milestone re-take does not run. |
| E1:73 | -02 §6 R-05 | SUPERSEDED | **SUPERSEDED** | ANSWER | re-cited, A-114 (R-05's four-season `measure:` read at two seasons or left until the end-of-plan re-take); EVAL-2 settled B (no menu door). |
| E1:77 | -02 §10 R-09 | SUPERSEDED | **SUPERSEDED** | ANSWER | re-cited, A-114 (R-09's four-season `measure:` read at two seasons or left until the end-of-plan re-take). |
| E1:78 | -02 §11 | SUPERSEDED | **SUPERSEDED** | ANSWER | re-cited: IS-A-13 replaces the re-take procedure, narrowed by A-114 to ONE end-of-plan re-take after M5. |
| E1:88 | CP-T03-11 | SUPERSEDED | **DONE-IN-CODE** | RECON | CP-T03-11: cut and composed into IN-59 (landed; `test_in59_audience.py`, E4). |
| E1:119 | CP-T08-07 | STILL-NEEDED | **MISSING-DEP** | RECON | CP-T08-07: its gate H-163 limit 3(a) has no owner in the tree or any proposal (E5:48); owner FA/SE; the tithe and tax kit files wait on it. |
| E1:139 | CP-T09-06b | STILL-NEEDED | **SUPERSEDED** | RECON | CP-T09-06 (b): the data edit `null -> inheritance` is `U5d_FA_owed_edits.md` §7 / `16_PESSIMIST_FA_A` edit 1 (`U5_FINDINGS_CLOSURE_U5d.md:93`; IS_B3 :170). |
| E1:144 | IN-48 | SUPERSEDED | **STILL-NEEDED** | RECON | IN-48: `U5_FINDINGS_CLOSURE_U5d.md:75,77` name IN-48 the owner of delegation (A-10, A-22 fix whom a seat commands); one item with H-108b; E1's BYZ_C reading was an [ASSUMPTION]. |
| E1:147 | CR-91 | RULED-CONFLICT | **STILL-NEEDED** | ANSWER | A-103 (J-E2-01 = EVAL-3 = J-E3-1, Option B): the claim gate CR-91 (3) is SUPERSEDED (no `requires_typed` conjunct on `march`); the carrier CR-91 (1)(2)(4)(5) is STILL-NEEDED as occasion and as context for regard and legitimacy; IN-36's cap stays. |
| E1:167 | CR-46b | RULED-CONFLICT | **SUPERSEDED** | LADDER | EVAL-2 settled by the ladder, Option B (E1's lean and default): step 2 (irrelevant) - the menu door bridged a withheld list the session removes (`14_VERBS_MILITARY_C_the_muster.md:210`, `_D:185`), and IS_A_NINE.md §6 counts only chooser-formed acts; a second path to 'built out' is two ladders for one quantity (CLAUDE.md §0.06 S). |
| E1:168 | CR-52 | RULED-CONFLICT | **SUPERSEDED** | LADDER | EVAL-2 Option B: CR-52 (the menu door) is not built; the army verbs count when the chooser forms them (B22). |
| E1:177 | CR-57 | STILL-NEEDED | **SUPERSEDED** | RECON | CR-57: `14_VERBS_SOCIAL2_B_a_word_with_content.md` §3 `petition` (:137-151) replaces it; IS-B2-SC-10's 'nothing supersedes' covers CR-58..CR-64 only. |
| E1:209 | GO-06 | STILL-NEEDED | **MISSING-DEP** | RECON | GO-06: needs a `valoria-game` checkout (another repository); owner the GO lane on Jordan's side (E2:124, E5 H-5). |
| E1:212 | NM-W5 | SUPERSEDED | **STILL-NEEDED** | RECON | NM-W5: `09_WR_B_chronicle_that_tells.md:63`: 'The journal NM-W5 owes ... is not built here'. |
| E1:226 | CL-OPEN | STILL-NEEDED | **SUPERSEDED** | RECON | CL-OPEN: its build is `21_PROCEDURAL_D_world_cards_and_churn.md` PG-6 ('the one widening ... the plan assigns to CL-OPEN's build'). |
| E1:227 | CL-PERSON | STILL-NEEDED | **STILL-NEEDED** | ANSWER | re-cited: CL-PERSON's E-4 hold is lifted by A-108 (stored offsets allowed); the build stays held on M35-M37, M40 as v11 states. |
| E1:228 | CL-MGMT | STILL-NEEDED | **STILL-NEEDED** | ANSWER | re-cited: CL-MGMT's M31 hold is lifted by A-104 (orders cost no scene budget; they may prompt scenes). |
| E1:235 | FA-07 | STILL-NEEDED | **SUPERSEDED** | RECON | FA-07: each restated row now has an owner (CR-89's clock fold; A-88..A-90 with `30_WR_G`/`31_WR_A`; CR-38; claims), E2:121. |
| E1:237 | MB-08b | STILL-NEEDED | **SUPERSEDED** | RECON | MB-08: who marches where is scheduled (B20/B22); the map generator is ruled out by A-55 (a fixed map) [ASSUMPTION: A-55's 'fixed map' excludes a generated map; E2's reading]. |
| E1:238 | PC-06 | STILL-NEEDED | **SUPERSEDED** | RECON | PC-06: K-1, K-3 landed; K-5 by `03_PC_loadout_and_carry.md` (B18). |
| E1:244 | CR-80 | STILL-NEEDED | **SUPERSEDED** | RECON | CR-80: `21_PROCEDURAL_D_world_cards_and_churn.md` (e) specifies the deck as `family: strife` rows on PG-6's receiver (B39); the rows' content stays Jordan's. |
| E1:251 | CP-T05-01 | STILL-NEEDED | **SUPERSEDED** | RECON | CP-T05-01: re-sourced by HEAR edit 2 (`U5_FINDINGS_CLOSURE_U5c.md` G-11, line 80; `05_SC_playable_hearing_B.md:171`). |
| E1:252 | CP-T05-02 | STILL-NEEDED | **SUPERSEDED** | RECON | CP-T05-02 (i): re-sourced by HEAR edit 2 (as CP-T05-01); (ii)(iii) landed. The fold must keep one owner of `world_q.hearing` (`08_FI_05_evidence-interface_B`, U3 §6.3). |
| E1:253 | CR-12 | SUPERSEDED | **SUPERSEDED** | MBA | re-cited, A-100: SUPERSEDED by MBA-04 (`master/mb_abstraction/MBA_DESIGN_part3.md` §8.2), with CR-12's step 1 instrument repair carried as `04_MB_cr12_linear_law.md` step 1 (the exponent check becomes MBA-04's falsifier). |
| E2:22 | CR-07 | STILL-NEEDED | **MISSING-DEP** | RECON | CR-07: IS-B2-CORE-06 BLOCKED (DEP-v11): the pre-flight needs `off_npc_084`'s rung, content the plan may not author; owner Jordan (the seat's rung) or A1-46's revert; one item with H-89. |
| E2:25 | CR-12 | SUPERSEDED | **SUPERSEDED** | MBA | re-cited, A-100: SUPERSEDED by MBA-04 (`master/mb_abstraction/MBA_DESIGN_part3.md` §8.2), with CR-12's step 1 instrument repair carried as `04_MB_cr12_linear_law.md` step 1 (the exponent check becomes MBA-04's falsifier). |
| E2:39 | CR-91a | STILL-NEEDED | **STILL-NEEDED** | ANSWER | re-cited, A-103: the carrier is built as occasion, not gate; moved to B21b (before B22, whose `Field` formation reads the WAR Proposition). |
| E2:40 | CR-91b | RULED-CONFLICT | **SUPERSEDED** | ANSWER | A-103: no claim gate on `march`; IN-36's one-march-per-season-per-territory cap stays as the ruled test limit; `30_WR_A_the_era_is_a_named_period.md:65` is corrected by A-103. |
| E2:48 | NM-W1 | STILL-NEEDED | **SUPERSEDED** | RECON | NM-W1: `09_WR_B_chronicle_that_tells.md` (B36) carries the chronicle remainder (fields `about`, `era`, `story`, `left`; A-49). |
| E2:60 | CL-EVENTS (2) | SUPERSEDED | **STILL-NEEDED** | RECON | CL-EVENTS (2): `U5_FINDINGS_CLOSURE_U5d.md:579` carries 'plan B10-18 CL-EVENTS (2) with `09_WR_B_weather_with_memory_and_the_year`' (amended by A-54), so the plan position survives. |
| E2:62 | CL-EVENTS (4) | STILL-NEEDED | **SUPERSEDED** | RECON | CL-EVENTS (4): `21_PROCEDURAL_D_world_cards_and_churn.md:138-146` makes commit (4)'s six cards six `scenario: true` pool rows; their content stays Jordan's. |
| E2:68 | CL-PERSON | STILL-NEEDED | **STILL-NEEDED** | ANSWER | re-cited: CL-PERSON's E-4 hold is lifted by A-108 (stored offsets allowed); the build stays held on M35-M37, M40 as v11 states. |
| E2:69 | CL-MGMT | STILL-NEEDED | **STILL-NEEDED** | ANSWER | re-cited: CL-MGMT's M31 hold is lifted by A-104 (orders cost no scene budget; they may prompt scenes). |
| E2:70 | CR-46 | STILL-NEEDED | **SUPERSEDED** | RECON | CR-46: the R-05 definition is IS-A-06's BUILT OUT block (`IS_A_NINE_part2.md`, opened by E1); the menu-door clause falls with EVAL-2 Option B. |
| E2:76 | CR-52 | STILL-NEEDED | **SUPERSEDED** | LADDER | EVAL-2 Option B (as E1:168). |
| E2:120 | FA-03 | DONE-IN-CODE | **SUPERSEDED** | RECON | FA-03: A-10 (no governance module; the faction game stands as a scenario on the season loop); nothing under `engine/` reads `action_vocabulary` (E2's grep) [E1's ASSUMPTION carried]. |
| E3:43 | M13 | WRONG | **WRONG** | LADDER | confirmed, J-E3-3 settled by the ladder step 1: ED-GO-0002 (resolved 2026-10-09) rules the 4.7 series and is the one owner (CLAUDE.md head); v12 writes no version number and points at ED-GO-0002. |
| E3:64 | M34 | DONE-IN-CODE | **STILL-NEEDED** | ANSWER | A-108 reverses 'as shipped (no stored offset)': M34 is built with CL-PERSON. |
| E3:66 | M36 | DONE-IN-CODE | **STILL-NEEDED** | RECON | M36: part 15 carries a design lane (the beneficiary column has no owner since REM-44), E5:122. |
| E3:69 | M39 | DONE-IN-CODE | **STILL-NEEDED** | RECON | M39: part 15's design-first item (post-freeze mover; A-76 stand-in only), E5:125. |
| E3:70 | M40 | DONE-IN-CODE | **STILL-NEEDED** | RECON | M40: the horizon term has no session author (E5:127); the risk term is `02_CHAR_what_an_act_risks.md` (E5:126). |
| E3:74 | §1a-M1res | STILL-NEEDED | **STILL-NEEDED** | ANSWER | re-cited, A-103: only IN-36's cap (one march per season per territory) and `guards` ON after CP-T09-07 (b)'s union survive; no casus-belli gate (B21b). |
| E3:139 | A1-44 | WRONG | **WRONG** | LADDER | confirmed, as E3:43 (A1-44). |
| E3:143 | A1-48 | DONE-IN-CODE | **DONE-IN-CODE** | LADDER | confirmed, J-E3-4 settled by the ladder: step 3 (AX-7, `canon`/`01_AXIOMS.md:113-120`: no unmediated world truth) and step 4 (v11's option (a), the channels are the shared ledger; no session proposal builds a store); no store is built. |
| E3:145 | A1-50 | STILL-NEEDED | **SUPERSEDED** | RECON | IN-14 / A1-50: retired by C3-L8 (`U3_CONFLICT_LEDGER.md:73`; `U5a_CORE_owed_edits.md` §H: `budget_office_bonus` removed); E3 Block 7 is dropped. ('Rounds' here is the season's lap, A-101.) |
| E3:175 | A1-80 | STILL-NEEDED | **SUPERSEDED** | ANSWER | A-110 (J-E3-2): `RemoteTrigger` is not added to `REQUIRED_DENY` or the deny-list until a session is observed arming a routine through it; CLAUDE.md §11's standing rule governs; E3 Block 8 (a) is dropped. |
| E3:258 | H-187 | DONE-IN-CODE | **SUPERSEDED** | RECON | register row governs (E7:85 SUPERSEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:260 | H-189 | SUPERSEDED | **DONE-IN-CODE** | RECON | register row governs (E7:87 DONE-IN-CODE); E3 convention 6 defers the register row to E6-E8. |
| E3:262 | H-191 | DONE-IN-CODE | **MISSING-DEP** | RECON | register row governs (E7:89 MISSING-DEP); E3 convention 6 defers the register row to E6-E8. |
| E3:263 | H-192 | DONE-IN-CODE | **SUPERSEDED** | RECON | register row governs (E7:90 SUPERSEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:264 | H-193 | DONE-IN-CODE | **SUPERSEDED** | RECON | register row governs (E7:91 SUPERSEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:266 | H-195 | STILL-NEEDED | **SUPERSEDED** | RECON | register row governs (E7:93 SUPERSEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:268 | H-197 | SUPERSEDED | **DONE-IN-CODE** | RECON | register row governs (E7:95 DONE-IN-CODE); E3 convention 6 defers the register row to E6-E8. |
| E3:269 | H-198 | DONE-IN-CODE | **MISSING-DEP** | RECON | register row governs (E7:96 MISSING-DEP); E3 convention 6 defers the register row to E6-E8. |
| E3:271 | H-200 | DONE-IN-CODE | **SUPERSEDED** | RECON | register row governs (E7:98 SUPERSEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:274 | H-203 | DONE-IN-CODE | **SUPERSEDED** | RECON | register row governs (E7:101 SUPERSEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:277 | H-206 | SUPERSEDED | **DONE-IN-CODE** | RECON | register row governs (E7:104 DONE-IN-CODE); E3 convention 6 defers the register row to E6-E8. |
| E3:286 | H-215 | DONE-IN-CODE | **SUPERSEDED** | RECON | register row governs (E7:113 SUPERSEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:289 | H-218 | DONE-IN-CODE | **SUPERSEDED** | RECON | register row governs (E7:116 SUPERSEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:290 | H-219 | SUPERSEDED | **STILL-NEEDED** | RECON | register row governs (E7:117 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:292 | H-221 | SUPERSEDED | **DONE-IN-CODE** | RECON | register row governs (E7:119 DONE-IN-CODE); E3 convention 6 defers the register row to E6-E8. |
| E3:296 | H-225 | STILL-NEEDED | **SUPERSEDED** | RECON | register row governs (E7:123 SUPERSEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:300 | H-229 | SUPERSEDED | **STILL-NEEDED** | RECON | register row governs (E7:127 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:305 | H-234 | STILL-NEEDED | **SUPERSEDED** | RECON | register row governs (E7:132 SUPERSEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:306 | H-235 | SUPERSEDED | **DONE-IN-CODE** | RECON | register row governs (E7:133 DONE-IN-CODE); E3 convention 6 defers the register row to E6-E8. |
| E3:308 | H-237 | SUPERSEDED | **WRONG** | RECON | register row governs (E7:135 WRONG); E3 convention 6 defers the register row to E6-E8. |
| E3:310 | H-239 | DONE-IN-CODE | **SUPERSEDED** | RECON | register row governs (E7:137 SUPERSEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:345 | IN-12 | SUPERSEDED | **DONE-IN-CODE** | RECON | IN-12: nine `test_in12_*.py` files exist (E2, E4); the residue rows are dispositioned by the register lanes. |
| E3:346 | IN-14 | STILL-NEEDED | **SUPERSEDED** | RECON | IN-14 / A1-50: retired by C3-L8 (`U3_CONFLICT_LEDGER.md:73`; `U5a_CORE_owed_edits.md` §H: `budget_office_bonus` removed); E3 Block 7 is dropped. ('Rounds' here is the season's lap, A-101.) |
| E3:347 | IN-18 | SUPERSEDED | **STILL-NEEDED** | RECON | IN-18: held; re-measure M0e after CR-29 (E2:92); E3's three proposals were cited, not opened. |
| E3:352 | IN-44 | SUPERSEDED | **STILL-NEEDED** | RECON | IN-44 rows 2-15: re-derive each anchor against the A-97-amended `04` (E2:95); row 1 done, row 16 superseded. |
| E3:356 | IN-48 | SUPERSEDED | **STILL-NEEDED** | RECON | IN-48: `U5_FINDINGS_CLOSURE_U5d.md:75,77` name IN-48 the owner of delegation (A-10, A-22 fix whom a seat commands); one item with H-108b; E1's BYZ_C reading was an [ASSUMPTION]. |
| E3:357 | IN-52 | SUPERSEDED | **STILL-NEEDED** | RECON | IN-52: `U5d_SE_owed_edits.md:61` keeps 'plan IN-52's flip entry'; three lanes carry it. |
| E3:362 | SC-04 | STILL-NEEDED | **DONE-IN-CODE** | RECON | SC-04: closed in B10-13 (v11 head §4); its H-217 residue is carried with CR-35. |
| E3:365 | SC-07 | SUPERSEDED | **STILL-NEEDED** | RECON | SC-07: waits on CR-36/CR-37 (`U5_FINDINGS_CLOSURE_U5c.md` row 108); E3's cite was a head read. |
| E3:369 | MB-07r | DONE-IN-CODE | **SUPERSEDED** | MBA | A-100: MB-07r is retired with its constant (`POOL_QUALITY_SCALE` deleted by MBA-04; §8.2). |
| E3:373 | PC-08 | SUPERSEDED | **STILL-NEEDED** | RECON | PC-08: a named residue with `U5b_PC_residue.md` §6 item 1's clause; 'A-1, A-4' do not carry it. |
| E3:376 | WR-01 | SUPERSEDED | **STILL-NEEDED** | RECON | WR-01: three lanes and IS-B3-WR-01 carry it (after `09_WR_B_threadwork_session_and_practitioner` edits 1-2); E3's cite was a head read. |
| E3:378 | GO-05 | SUPERSEDED | **STILL-NEEDED** | RECON | GO-05: an early landing in B03 (`11_GO_port_gate_order_and_coverage.md` §2 drops its GO-01 edge); E3's cite was a head read. |
| E3:379 | GO-06 | SUPERSEDED | **MISSING-DEP** | RECON | GO-06: needs a `valoria-game` checkout (another repository); owner the GO lane on Jordan's side (E2:124, E5 H-5). |
| E3:382 | FA-03 | STILL-NEEDED | **SUPERSEDED** | RECON | FA-03: A-10 (no governance module; the faction game stands as a scenario on the season loop); nothing under `engine/` reads `action_vocabulary` (E2's grep) [E1's ASSUMPTION carried]. |
| E3:391 | CT-1 | STILL-NEEDED | **SUPERSEDED** | RECON | CT-1: follows A1-50, retired by C3-L8. |
| E3:448 | H-10 | STILL-NEEDED | **SUPERSEDED** | RECON | register row governs (E6:40 DONE-IN-CODE, E6:41 SUPERSEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:456 | H-25 | DONE-IN-CODE | **STILL-NEEDED** | RECON | register row governs (E6:49 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:461 | H-30 | DONE-IN-CODE | **SUPERSEDED** | RECON | register row governs (E6:54 SUPERSEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:468 | H-37 | SUPERSEDED | **DONE-IN-CODE** | RECON | register row governs (E6:61 DONE-IN-CODE); E3 convention 6 defers the register row to E6-E8. |
| E3:470 | H-39 | DONE-IN-CODE | **STILL-NEEDED** | RECON | register row governs (E6:63 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:471 | H-40 | DONE-IN-CODE | **SUPERSEDED** | RECON | register row governs (E6:64 SUPERSEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:478 | H-47 | SUPERSEDED | **STILL-NEEDED** | RECON | register row governs (E6:71 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:479 | H-48 | DONE-IN-CODE | **SUPERSEDED** | RECON | register row governs (E6:72 SUPERSEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:483 | H-52 | DONE-IN-CODE | **WRONG** | RECON | register row governs (E6:76 WRONG); E3 convention 6 defers the register row to E6-E8. |
| E3:490 | H-59 | DONE-IN-CODE | **SUPERSEDED** | RECON | register row governs (E6:84 SUPERSEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:493 | H-62 | SUPERSEDED | **STILL-NEEDED** | RECON | register row governs (E6:87 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:494 | H-63 | DONE-IN-CODE | **SUPERSEDED** | RECON | register row governs (E6:88 SUPERSEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:513 | H-86 | DONE-IN-CODE | **SUPERSEDED** | RECON | register row governs (E6:116 SUPERSEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:514 | H-87 | DONE-IN-CODE | **WRONG** | RECON | register row governs (E6:117 WRONG); E3 convention 6 defers the register row to E6-E8. |
| E3:516 | H-89 | STILL-NEEDED | **MISSING-DEP** | RECON | register row governs (E6:119 MISSING-DEP); E3 convention 6 defers the register row to E6-E8. |
| E3:517 | H-90 | SUPERSEDED | **STILL-NEEDED** | RECON | register row governs (E6:120 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:519 | H-92 | STILL-NEEDED | **SUPERSEDED** | RECON | register row governs (E6:122 SUPERSEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:524 | H-97 | DONE-IN-CODE | **SUPERSEDED** | RECON | register row governs (E6:127 SUPERSEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:525 | H-98 | DONE-IN-CODE | **SUPERSEDED** | RECON | register row governs (E6:128 SUPERSEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:530 | H-103 | DONE-IN-CODE | **SUPERSEDED** | RECON | register row governs (E6:131 SUPERSEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:533 | H-106 | DONE-IN-CODE | **STILL-NEEDED** | RECON | register row governs (E6:134 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:535 | H-108 | SUPERSEDED | **STILL-NEEDED** | RECON | register row governs (E6:136 DONE-IN-CODE, E6:137 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:538 | H-111 | DONE-IN-CODE | **SUPERSEDED** | RECON | register row governs (E6:140 SUPERSEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:546 | H-119 | DONE-IN-CODE | **SUPERSEDED** | RECON | register row governs (E7:40 SUPERSEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:554 | H-127 | DONE-IN-CODE | **SUPERSEDED** | RECON | register row governs (E6:106 SUPERSEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:557 | H-130 | DONE-IN-CODE | **STILL-NEEDED** | RECON | register row governs (E6:143 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:559 | H-132 | DONE-IN-CODE | **STILL-NEEDED** | ANSWER | A-105, as E6:145 (the register row governs, CR-25's landing is the base). |
| E3:560 | H-133 | DONE-IN-CODE | **STILL-NEEDED** | RECON | register row governs (E6:146 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:562 | H-135 | DONE-IN-CODE | **STILL-NEEDED** | RECON | register row governs (E6:148 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:564 | H-137 | DONE-IN-CODE | **STILL-NEEDED** | RECON | register row governs (E6:150 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:565 | H-138 | DONE-IN-CODE | **STILL-NEEDED** | RECON | register row governs (E6:151 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:566 | H-139 | DONE-IN-CODE | **STILL-NEEDED** | RECON | register row governs (E6:152 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:568 | H-141 | DONE-IN-CODE | **STILL-NEEDED** | RECON | register row governs (E7:26 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:569 | H-142 | DONE-IN-CODE | **STILL-NEEDED** | RECON | register row governs (E7:27 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:570 | H-143 | DONE-IN-CODE | **STILL-NEEDED** | RECON | register row governs (E7:28 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:572 | H-145 | DONE-IN-CODE | **STILL-NEEDED** | RECON | register row governs (E7:30 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:573 | H-146 | DONE-IN-CODE | **SUPERSEDED** | RECON | register row governs (E6:108 SUPERSEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:580 | H-153 | DONE-IN-CODE | **STILL-NEEDED** | RECON | register row governs (E7:50 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:581 | H-154 | DONE-IN-CODE | **STILL-NEEDED** | RECON | register row governs (E7:51 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:583 | H-156 | DONE-IN-CODE | **SUPERSEDED** | RECON | register row governs (E7:53 SUPERSEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:585 | H-158 | SUPERSEDED | **DONE-IN-CODE** | RECON | register row governs (E7:55 DONE-IN-CODE); E3 convention 6 defers the register row to E6-E8. |
| E3:587 | H-160 | SUPERSEDED | **DONE-IN-CODE** | RECON | register row governs (E7:57 DONE-IN-CODE); E3 convention 6 defers the register row to E6-E8. |
| E3:591 | H-164 | DONE-IN-CODE | **SUPERSEDED** | RECON | register row governs (E7:62 SUPERSEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:594 | H-168 | SUPERSEDED | **WRONG** | RECON | register row governs (E7:66 WRONG); E3 convention 6 defers the register row to E6-E8. |
| E3:595 | H-169 | DONE-IN-CODE | **STILL-NEEDED** | RECON | register row governs (E7:67 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:596 | H-170 | DONE-IN-CODE | **SUPERSEDED** | RECON | register row governs (E7:68 SUPERSEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:597 | H-171 | SUPERSEDED | **STILL-NEEDED** | RECON | register row governs (E7:69 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:601 | H-175 | SUPERSEDED | **DONE-IN-CODE** | RECON | register row governs (E7:73 DONE-IN-CODE); E3 convention 6 defers the register row to E6-E8. |
| E3:605 | H-180 | DONE-IN-CODE | **STILL-NEEDED** | RECON | register row governs (E7:78 STILL-NEEDED); E3 convention 6 defers the register row to E6-E8. |
| E3:628 | V9-14 | STILL-NEEDED | **STILL-NEEDED** | ANSWER | re-cited, A-103 (as §1a-M1res). |
| E4:139 | ED-1043 | STILL-NEEDED | **STILL-NEEDED** | MBA | re-targeted, A-100: ED-1043 STANDS; its trigger fires at MBA-04 step 0 (MBA-04 edits `orchestration.py`); MB, B19-mb-field-calibration, step 0. |
| E4:159 | ED-MB-0045 (melee attrition item) | SUPERSEDED | **SUPERSEDED** | MBA | re-cited, A-100: ED-MB-0045's 'melee attrition back to the linear law' is SUPERSEDED by MBA-04 (§8.2); its CellTable owner and item 4 stay LEAVE. |
| E4:211 | G-25 | WRONG | **SUPERSEDED** | WRONG-R | G-25: the gap is real (termini are prose); `12_ARCS_arcs_as_staged_goals.md` §Resolution 1-4 (opened) authors a case's counter as stages of the holder's goal, predicates over his own ledger; B10. |
| E4:235 | CL-MGMT | STILL-NEEDED | **STILL-NEEDED** | ANSWER | re-cited: CL-MGMT's M31 hold is lifted by A-104 (orders cost no scene budget; they may prompt scenes). |
| E4:237 | CL-PERSON | STILL-NEEDED | **STILL-NEEDED** | ANSWER | re-cited: CL-PERSON's E-4 hold is lifted by A-108 (stored offsets allowed); the build stays held on M35-M37, M40 as v11 states. |
| E4:238 | CL-SLICE | STILL-NEEDED | **SUPERSEDED** | RECON | CL-SLICE: `01_CORE_one_scene_contract.md`, `11_GO_player_surface_contract_B.md` §6 (B34) [E1's ASSUMPTION carried]. |
| E4:289 | CP-T06-08 | STILL-NEEDED | **SUPERSEDED** | RECON | CP-T06-08: `14_VERBS_MATERIAL_D_paper.md` §5 (:127-129) releases `destroy_record` on a paper that names its holder (H-156 option (b)); JA-1 is answered by it. |
| E4:307 | CP-T08-07 | STILL-NEEDED | **MISSING-DEP** | RECON | CP-T08-07: its gate H-163 limit 3(a) has no owner in the tree or any proposal (E5:48); owner FA/SE; the tithe and tax kit files wait on it. |
| E4:318 | CP-T09-08 | STILL-NEEDED | **SUPERSEDED** | RECON | CP-T09-08: IS-B3-FA-05 carries `_eff_dispatch` in full (WHERE, FALSIFIER, GATE), B21. |
| E4:321 | CP-T10-02 | STILL-NEEDED | **SUPERSEDED** | RECON | CP-T10-02: `16_PESSIMIST_WR_A_the_road_is_drawn.md:23,105-113` decides its shape (a road draw); the band residue stays E5:62. |
| E4:328 | CP-T10-08 | STILL-NEEDED | **SUPERSEDED** | RECON | CP-T10-08: `23_STORY_B_a_house_continues.md` (opened): 'a marriage as an instrument' formed by `covenant`, no `marry` verb (B39). |
| E4:336 | CR-07 | STILL-NEEDED | **MISSING-DEP** | RECON | CR-07: IS-B2-CORE-06 BLOCKED (DEP-v11): the pre-flight needs `off_npc_084`'s rung, content the plan may not author; owner Jordan (the seat's rung) or A1-46's revert; one item with H-89. |
| E4:337 | CR-08 | STILL-NEEDED | **SUPERSEDED** | RECON | CR-08: `07_SE_population_census.md` is 'CR-08's CENSUS writer, specified' (opened by E1, E2). |
| E4:341 | CR-12 | SUPERSEDED | **SUPERSEDED** | MBA | re-cited, A-100: SUPERSEDED by MBA-04 (`master/mb_abstraction/MBA_DESIGN_part3.md` §8.2), with CR-12's step 1 instrument repair carried as `04_MB_cr12_linear_law.md` step 1 (the exponent check becomes MBA-04's falsifier). |
| E4:375 | CR-46 | STILL-NEEDED | **SUPERSEDED** | RECON | as E2:70 (CR-46). |
| E4:377 | CR-48 | STILL-NEEDED | **SUPERSEDED** | RECON | CR-48: A-21 and `06_FA_decree_binds.md` edits 1-3 / `14_VERBS_SOCIAL1_B` §1. |
| E4:379 | CR-50 | STILL-NEEDED | **SUPERSEDED** | RECON | CR-50: `14_VERBS_MILITARY_B_train.md:49`, `14_VERBS_PHYSICAL_B_field_and_ruin.md:28,66` replace both cells (B22). |
| E4:381 | CR-52 | STILL-NEEDED | **SUPERSEDED** | LADDER | EVAL-2 Option B (as E1:168). |
| E4:382 | CR-53 | STILL-NEEDED | **SUPERSEDED** | RECON | CR-53: `14_VERBS_MATERIAL_D_paper.md:127-129` takes H-156 option (b). |
| E4:383 | CR-54 | STILL-NEEDED | **SUPERSEDED** | RECON | CR-54: `06_FA_decree_binds.md` edit 5 with A-35 and `14_VERBS_BINDING_C_turnover`. |
| E4:386 | CR-57 | STILL-NEEDED | **SUPERSEDED** | RECON | CR-57: `14_VERBS_SOCIAL2_B_a_word_with_content.md` §3 `petition` (:137-151) replaces it; IS-B2-SC-10's 'nothing supersedes' covers CR-58..CR-64 only. |
| E4:420 | CR-91 | STILL-NEEDED | **STILL-NEEDED** | ANSWER | re-cited, A-103: CR-91 carried without its gate (3); carrier first item of B21b. |
| E4:423 | CR-94 | STILL-NEEDED | **SUPERSEDED** | RECON | CR-94: `18_DETERMINISM_task_draw_for_uncontested_verbs.md:126-128,143` and `14_VERBS_MATERIAL_D_paper.md:75-76` replace it (forger's skill through the task draw; quality by band); its score/2 rests on the half-score ruling A-26 overrides. [ASSUMPTION: IS-B2-FI-02's 'nothing supersedes any of the nine' is overtaken for CR-94 by these; stage 6 drops CR-94 from B11's list.] |
| E4:451 | FA-03 | STILL-NEEDED | **SUPERSEDED** | RECON | FA-03: A-10 (no governance module; the faction game stands as a scenario on the season loop); nothing under `engine/` reads `action_vocabulary` (E2's grep) [E1's ASSUMPTION carried]. |
| E4:452 | FA-07 | STILL-NEEDED | **SUPERSEDED** | RECON | FA-07: each restated row now has an owner (CR-89's clock fold; A-88..A-90 with `30_WR_G`/`31_WR_A`; CR-38; claims), E2:121. |
| E4:455 | GO-06 | STILL-NEEDED | **MISSING-DEP** | RECON | GO-06: needs a `valoria-game` checkout (another repository); owner the GO lane on Jordan's side (E2:124, E5 H-5). |
| E4:479 | MB-07r | DONE-IN-CODE | **SUPERSEDED** | MBA | A-100: as E3:369. |
| E4:480 | MB-08 | STILL-NEEDED | **SUPERSEDED** | RECON | MB-08: who marches where is scheduled (B20/B22); the map generator is ruled out by A-55 (a fixed map) [ASSUMPTION: A-55's 'fixed map' excludes a generated map; E2's reading]. |
| E4:482 | NM-W1 | STILL-NEEDED | **SUPERSEDED** | RECON | NM-W1: `09_WR_B_chronicle_that_tells.md` (B36) carries the chronicle remainder (fields `about`, `era`, `story`, `left`; A-49). |
| E4:485 | NM-W4 | STILL-NEEDED | **SUPERSEDED** | RECON | NM-W4: `14_VERBS_SOCIAL2_B_a_word_with_content.md` §1 `utter` (B25). |
| E4:492 | PC-06 | STILL-NEEDED | **SUPERSEDED** | RECON | PC-06: K-1, K-3 landed; K-5 by `03_PC_loadout_and_carry.md` (B18). |
| E4:537 | SE-04 | STILL-NEEDED | **SUPERSEDED** | RECON | SE-04: (a) landed, (b)(c) superseded (C3-C4: keep the field and give it a reader; A-56), per E2:104-105. |
| E4:538 | SE-06 | STILL-NEEDED | **SUPERSEDED** | RECON | SE-06: the conviction half is `31_WR_B_the_revival_gathers.md` commit 2 with `31_WR_A` (A-87..A-91; needs CR-107); the pursuit half landed (E3:368). |
| E4:544 | §2 CP-T06-08 | STILL-NEEDED | **SUPERSEDED** | RECON | CP-T06-08: `14_VERBS_MATERIAL_D_paper.md` §5 (:127-129) releases `destroy_record` on a paper that names its holder (H-156 option (b)); JA-1 is answered by it. |
| E4:556 | §2 REM-20 | WRONG | **DONE-IN-CODE** | WRONG-R | REM-20: the comment at `verb_table.yaml:89-91` (opened) describes the shipped `rosters.yaml: fold_kinds` and `data/verbs.py::EVENT_KINDS`; nothing left to fold. |
| E4:558 | §2 REM-41 | WRONG | **DONE-IN-CODE** | WRONG-R | REM-41: `data/verbs.py::EVENT_KINDS` (3 hits) and `loop/resolve.py::_act_events` (13 hits) exist; the thing asked is in the tree (agrees with E5:77). |
| E4:559 | §2 REM-40 | WRONG | **DONE-IN-CODE** | WRONG-R | REM-40: shipped as `rosters.yaml: fold_kinds` (3 hits); agrees with E5:76. |
| E4:561 | §2 CP-T02-08 | WRONG | **DONE-IN-CODE** | WRONG-R | CP-T02-08: restates CP-T01-03, built (`seam/wrappers/sigma.py:350 def odds_of`); agrees with E5:72. |
| E4:562 | §2 CP-T05-05 | WRONG | **SUPERSEDED** | WRONG-R | CP-T05-05: the N-line failed for want of `interrogate`; `14_VERBS_SOCIAL2_C_case_question_confession.md` (B25; 15 mentions of `interrogate`) builds the question route; B25's gate adds the 'one kind per band' check (E5:73). |
| E4:565 | §2 CP-T02-04 | WRONG | **SUPERSEDED** | WRONG-R | CP-T02-04: its remaining build (a vacancy motive for `revoke`) is carried by A-35 (resistible draw) and `14_VERBS_BINDING_C_turnover` (B21), with CR-54's supersession by `06_FA_decree_binds.md` edit 5 (E5:71). |
| E4:566 | §2 ED-1043 the mass-battle god-file spl… | STILL-NEEDED | **STILL-NEEDED** | MBA | re-targeted as E4:139. |
| E4:575 | §2 H-207's vacancy motive (`revoke`'s o… | STILL-NEEDED | **SUPERSEDED** | RECON | H-207's vacancy motive: A-35 and `14_VERBS_BINDING_C_turnover` (B21), `06_FA_seat_terms_and_turnover` (E3, E7). |
| E4:598 | DEC-1 | WRONG | **SUPERSEDED** | WRONG-R | DEC-1: its owner H-187 is SUPERSEDED by `U5a_CHAR_owed_amendments.md` §8 (ordered flips of the dormant readers; E7:85). |
| E4:609 | DEC-12 | WRONG | **SUPERSEDED** | WRONG-R | DEC-12: its owner H-111 is SUPERSEDED by A-81 and `16_PESSIMIST_CORE_a_refusal_is_remembered.md` (B09; E6:140). |
| E4:666 | CP-T07-02 · HR-7 | WRONG | **STILL-NEEDED** | WRONG-R | CP-T07-02 HR-7: a rider on the still-needed host (E5:34, which read part 14's text; E4 copied it unjudged). |
| E4:679 | CP-T08-07 · AM-E-18 | STILL-NEEDED | **MISSING-DEP** | RECON | CP-T08-07: its gate H-163 limit 3(a) has no owner in the tree or any proposal (E5:48); owner FA/SE; the tithe and tax kit files wait on it. |
| E4:692 | CP-T10-02 · AM-F-08 | STILL-NEEDED | **SUPERSEDED** | RECON | CP-T10-02: `16_PESSIMIST_WR_A_the_road_is_drawn.md:23,105-113` decides its shape (a road draw); the band residue stays E5:62. |
| E4:698 | CP-T10-08 · AM-C-07 | STILL-NEEDED | **SUPERSEDED** | RECON | CP-T10-08: `23_STORY_B_a_house_continues.md` (opened): 'a marriage as an instrument' formed by `covenant`, no `marry` verb (B39). |
| E4:699 | CP-T10-08 · AM-F-09 | STILL-NEEDED | **SUPERSEDED** | RECON | CP-T10-08: `23_STORY_B_a_house_continues.md` (opened): 'a marriage as an instrument' formed by `covenant`, no `marry` verb (B39). |
| E4:701 | CP-T02-04 · AM-B-10 | WRONG | **SUPERSEDED** | WRONG-R | CP-T02-04: its remaining build (a vacancy motive for `revoke`) is carried by A-35 (resistible draw) and `14_VERBS_BINDING_C_turnover` (B21), with CR-54's supersession by `06_FA_decree_binds.md` edit 5 (E5:71). |
| E4:702 | CP-T02-08 · AM-B-14 | WRONG | **DONE-IN-CODE** | WRONG-R | CP-T02-08: restates CP-T01-03, built (`seam/wrappers/sigma.py:350 def odds_of`); agrees with E5:72. |
| E4:703 | CP-T05-05 · AM-D-06 | WRONG | **SUPERSEDED** | WRONG-R | CP-T05-05: the N-line failed for want of `interrogate`; `14_VERBS_SOCIAL2_C_case_question_confession.md` (B25; 15 mentions of `interrogate`) builds the question route; B25's gate adds the 'one kind per band' check (E5:73). |
| E4:706 | REM-40 · AM-A-02 | WRONG | **DONE-IN-CODE** | WRONG-R | REM-40: shipped as `rosters.yaml: fold_kinds` (3 hits); agrees with E5:76. |
| E4:707 | REM-41 · AM-A-01 | WRONG | **DONE-IN-CODE** | WRONG-R | REM-41: `data/verbs.py::EVENT_KINDS` (3 hits) and `loop/resolve.py::_act_events` (13 hits) exist; the thing asked is in the tree (agrees with E5:77). |
| E5:69 | P14 CP-T10-08 LIMIT (AM-F-09) | STILL-NEEDED | **SUPERSEDED** | RECON | CP-T10-08: `23_STORY_B_a_house_continues.md` (opened): 'a marriage as an instrument' formed by `covenant`, no `marry` verb (B39). |
| E5:74 | P14 CP-T06-06 CUT (AM-D-12) | SUPERSEDED | **WRONG** | RECON | CP-T06-06: v11's false N-line (a key name only) is the decisive reason; A-98 agrees; E4 WRONG confirmed. |
| E5:78 | P14 REM-51 CUT (AM-A-03) | SUPERSEDED | **WRONG** | RECON | REM-51: v11's own NERS cut (no producer in the realm; reopen trigger CR-22's exit census) stands; E5's A-56 supersession was UNVERIFIED. |
| E5:85 | P14 REM-45 (AM-A-23) | SUPERSEDED | **WRONG** | RECON | REM-45: ED-IN-0330 (a pre-session ledger row) retired the rolled `history` term, so the premise is false at the tree (E4:527 WRONG confirmed); not a session supersession. |
| E5:95 | P14 CP-T06-08 (AM-D-15) | STILL-NEEDED | **SUPERSEDED** | RECON | CP-T06-08: `14_VERBS_MATERIAL_D_paper.md` §5 (:127-129) releases `destroy_record` on a paper that names its holder (H-156 option (b)); JA-1 is answered by it. |
| E5:117 | P15 M31 | STILL-NEEDED | **SUPERSEDED** | ANSWER | A-104 (M31 (b) = E-3): management orders are not scenes and cost no scene budget; performing one may prompt a scene, which costs as any scene. (a) was closed. The build is A-104's v12 item (a declared hash mover). |
| E5:118 | P15 M32 | SUPERSEDED | **DONE-IN-CODE** | RECON | M32: `seam/wrappers/sigma.py:350 odds_of` (mode (a)) is in the tree; `10_DICE_believed_odds_have_a_prior` extends it. |
| E5:119 | P15 M33 | SUPERSEDED | **DONE-IN-CODE** | RECON | M33: answered by ratified `04` §C.11; nothing to build. |
| E5:120 | P15 M34 | STILL-NEEDED | **STILL-NEEDED** | ANSWER | re-cited, A-108: stored manner offsets are allowed; M34's design is CL-PERSON's build with offsets. |
| E5:123 | P15 M37 | SUPERSEDED | **DONE-IN-CODE** | RECON | M37: answered 'no manner axis feeds the refusal gate'; `data/fixtures.py:862` `refusal_axis=None`. |
| E5:131 | P15 CL-PERSON | STILL-NEEDED | **STILL-NEEDED** | ANSWER | re-cited: CL-PERSON's E-4 hold is lifted by A-108 (stored offsets allowed); the build stays held on M35-M37, M40 as v11 states. |
| E5:132 | P15 CL-MGMT | SUPERSEDED | **STILL-NEEDED** | RECON | CL-MGMT: three lanes carry it; A-104 lifts its M31 hold; the scene-list part E5 cites (`28_CORE_scene_access_*`, `01_CORE_one_scene_contract`) does not build the batched management front end. |
| E5:137 | P15 E-3 | STILL-NEEDED | **SUPERSEDED** | ANSWER | A-104 (E-3). |
| E5:138 | P15 E-4 | STILL-NEEDED | **SUPERSEDED** | ANSWER | A-108 (E-4): a person may carry a stored offset on each manner axis; ED-IN-0261 narrowed; the build is CL-PERSON's (neutral-control gate reproduces today's hashes at zero offset). |
| E5:141 | P15 H-1 | STILL-NEEDED | **STILL-NEEDED** | ANSWER | re-cited, A-111 (H-1): v12 carries the owed ledger rows (M31, M32) as relayed, marked 'Jordan's words relayed, not recorded'; the menu-budget part is superseded by A-104. |
| E5:156 | P16 CR-80 | STILL-NEEDED | **SUPERSEDED** | RECON | CR-80: `21_PROCEDURAL_D_world_cards_and_churn.md` (e) specifies the deck as `family: strife` rows on PG-6's receiver (B39); the rows' content stays Jordan's. |

## 2. One disposition per id (v11 ids found in two or more lane files with different calls)

An id 'in parts' is a position the evidence splits (a superseded part and a carried part, or a landed part and a residue); each part has one disposition.

| id | rows (lane disposition → settled) | settled for the id |
|---|---|---|
| CL-EVENTS | E1:158 CL-EVENTS (2) STILL-NEEDED→STILL-NEEDED; E1:159 CL-EVENTS (3)(4) SUPERSEDED→SUPERSEDED; E2:59 CL-EVENTS (1) DONE-IN-CODE→DONE-IN-CODE; E2:60 CL-EVENTS (2) SUPERSEDED→STILL-NEEDED; E2:61 CL-EVENTS (3) SUPERSEDED→SUPERSEDED; E2:62 CL-EVENTS (4) STILL-NEEDED→SUPERSEDED; E4:232 CL-EVENTS (1: per-ter… DONE-IN-CODE→DONE-IN-CODE; E4:233 CL-EVENTS (2: live we… STILL-NEEDED→STILL-NEEDED; E4:234 CL-EVENTS (3)(4: Tens… SUPERSEDED→SUPERSEDED | in parts: DONE-IN-CODE / STILL-NEEDED / SUPERSEDED |
| CL-MGMT | E1:228 CL-MGMT STILL-NEEDED→STILL-NEEDED; E2:69 CL-MGMT STILL-NEEDED→STILL-NEEDED; E4:235 CL-MGMT STILL-NEEDED→STILL-NEEDED; E5:132 P15 CL-MGMT SUPERSEDED→STILL-NEEDED | one: STILL-NEEDED |
| CL-OPEN | E1:226 CL-OPEN STILL-NEEDED→SUPERSEDED; E2:67 CL-OPEN SUPERSEDED→SUPERSEDED; E4:236 CL-OPEN SUPERSEDED→SUPERSEDED; E5:130 P15 CL-OPEN SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| CL-SLICE | E1:225 CL-SLICE SUPERSEDED→SUPERSEDED; E2:66 CL-SLICE SUPERSEDED→SUPERSEDED; E4:238 CL-SLICE STILL-NEEDED→SUPERSEDED; E5:133 P15 CL-SLICE SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| CL-THRUST | E1:220 CL-THRUST-a SUPERSEDED→SUPERSEDED; E1:221 CL-THRUST-b STILL-NEEDED→STILL-NEEDED; E2:64 CL-THRUST (landed) DONE-IN-CODE→DONE-IN-CODE; E2:65 CL-THRUST (held) STILL-NEEDED→STILL-NEEDED; E4:240 CL-THRUST DONE-IN-CODE→DONE-IN-CODE | in parts: DONE-IN-CODE / STILL-NEEDED / SUPERSEDED |
| CP-T05-01 | E1:251 CP-T05-01 STILL-NEEDED→SUPERSEDED; E4:278 CP-T05-01 SUPERSEDED→SUPERSEDED; E4:651 CP-T05-01 · AM-D-03 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| CP-T05-02 | E1:252 CP-T05-02 STILL-NEEDED→SUPERSEDED; E4:279 CP-T05-02 (ii)(iii) DONE-IN-CODE→DONE-IN-CODE; E4:280 CP-T05-02 (i) SUPERSEDED→SUPERSEDED; E4:652 CP-T05-02 · AM-D-01 SUPERSEDED→SUPERSEDED; E4:653 CP-T05-02 · AM-D-02 DONE-IN-CODE→DONE-IN-CODE | in parts: DONE-IN-CODE / SUPERSEDED |
| CP-T07-02 | E1:101 CP-T07-02 STILL-NEEDED→STILL-NEEDED; E4:291 CP-T07-02 STILL-NEEDED→STILL-NEEDED; E4:664 CP-T07-02 · AM-E-02 STILL-NEEDED→STILL-NEEDED; E4:665 CP-T07-02 · HR-6 STILL-NEEDED→STILL-NEEDED; E4:666 CP-T07-02 · HR-7 WRONG→STILL-NEEDED; E5:32 P14 CP-T07-02 REPAIR … STILL-NEEDED→STILL-NEEDED; E5:33 P14 CP-T07-02 REPAIR … STILL-NEEDED→STILL-NEEDED; E5:34 P14 CP-T07-02 RESEQUE… STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| CP-T08-02 | E1:116 CP-T08-02 STILL-NEEDED→STILL-NEEDED; E4:302 CP-T08-02 STILL-NEEDED→STILL-NEEDED; E4:675 CP-T08-02 · AM-E-13 STILL-NEEDED→STILL-NEEDED; E5:44 P14 CP-T08-02 LIMIT (… SUPERSEDED→SUPERSEDED | in parts: STILL-NEEDED / SUPERSEDED |
| CP-T09-02 | E1:131 CP-T09-02 STILL-NEEDED→STILL-NEEDED; E4:312 CP-T09-02 STILL-NEEDED→STILL-NEEDED; E4:683 CP-T09-02 · AM-F-10 STILL-NEEDED→STILL-NEEDED; E4:684 CP-T09-02 · AM-F-11 STILL-NEEDED→STILL-NEEDED; E5:52 P14 CP-T09-02 RESEQUE… SUPERSEDED→SUPERSEDED; E5:53 P14 CP-T09-02 LIMIT (… STILL-NEEDED→STILL-NEEDED | in parts: STILL-NEEDED / SUPERSEDED |
| CP-T10-02 | E1:155 CP-T10-02 SUPERSEDED→SUPERSEDED; E4:321 CP-T10-02 STILL-NEEDED→SUPERSEDED; E4:692 CP-T10-02 · AM-F-08 STILL-NEEDED→SUPERSEDED; E5:61 P14 CP-T10-02 REPAIR … SUPERSEDED→SUPERSEDED; E5:62 P14 CP-T10-02 REPAIR … STILL-NEEDED→STILL-NEEDED | in parts: STILL-NEEDED / SUPERSEDED |
| CP-T10-03 | E1:156 CP-T10-03a SUPERSEDED→SUPERSEDED; E1:157 CP-T10-03b STILL-NEEDED→STILL-NEEDED; E4:322 CP-T10-03 (`year_leng… SUPERSEDED→SUPERSEDED; E4:323 CP-T10-03 (`season_te… STILL-NEEDED→STILL-NEEDED; E4:693 CP-T10-03 · AM-F-04 STILL-NEEDED→STILL-NEEDED; E5:63 P14 CP-T10-03 REPAIR … STILL-NEEDED→STILL-NEEDED | in parts: STILL-NEEDED / SUPERSEDED |
| CP-T02-04 | E4:565 §2 CP-T02-04 WRONG→SUPERSEDED; E4:701 CP-T02-04 · AM-B-10 WRONG→SUPERSEDED; E5:71 P14 CP-T02-04 CUT (AM… SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| CP-T05-05 | E4:562 §2 CP-T05-05 WRONG→SUPERSEDED; E4:703 CP-T05-05 · AM-D-06 WRONG→SUPERSEDED; E5:73 P14 CP-T05-05 CUT (AM… SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| CP-T06-06 | E4:563 §2 CP-T06-06 WRONG→WRONG; E4:704 CP-T06-06 · AM-D-12 WRONG→WRONG; E5:74 P14 CP-T06-06 CUT (AM… SUPERSEDED→WRONG | one: WRONG |
| CP-T09-06 | E1:138 CP-T09-06a WRONG→WRONG; E1:139 CP-T09-06b STILL-NEEDED→SUPERSEDED; E4:316 CP-T09-06 SUPERSEDED→SUPERSEDED; E5:100 P14 CP-T09-06 (AM-F-1… SUPERSEDED→SUPERSEDED | in parts: SUPERSEDED / WRONG |
| CP-T08-07 | E1:119 CP-T08-07 STILL-NEEDED→MISSING-DEP; E4:307 CP-T08-07 STILL-NEEDED→MISSING-DEP; E4:679 CP-T08-07 · AM-E-18 STILL-NEEDED→MISSING-DEP; E5:48 P14 CP-T08-07 RESEQUE… MISSING-DEP→MISSING-DEP | one: MISSING-DEP |
| CP-T09-07 | E1:133 CP-T09-07a SUPERSEDED→SUPERSEDED; E1:134 CP-T09-07b STILL-NEEDED→STILL-NEEDED; E4:317 CP-T09-07 STILL-NEEDED→STILL-NEEDED; E4:689 CP-T09-07 · AM-F-15 STILL-NEEDED→STILL-NEEDED; E5:58 P14 CP-T09-07 REPAIR … STILL-NEEDED→STILL-NEEDED | in parts: STILL-NEEDED / SUPERSEDED |
| CP-T02-08 | E4:561 §2 CP-T02-08 WRONG→DONE-IN-CODE; E4:702 CP-T02-08 · AM-B-14 WRONG→DONE-IN-CODE; E5:72 P14 CP-T02-08 CUT (AM… DONE-IN-CODE→DONE-IN-CODE | one: DONE-IN-CODE |
| CP-T06-08 | E1:99 CP-T06-08 SUPERSEDED→SUPERSEDED; E4:289 CP-T06-08 STILL-NEEDED→SUPERSEDED; E4:544 §2 CP-T06-08 STILL-NEEDED→SUPERSEDED; E5:95 P14 CP-T06-08 (AM-D-1… STILL-NEEDED→SUPERSEDED | one: SUPERSEDED |
| CP-T07-08 | E1:109 CP-T07-08 STILL-NEEDED→STILL-NEEDED; E4:297 CP-T07-08 STILL-NEEDED→STILL-NEEDED; E4:671 CP-T07-08 · AM-E-08 STILL-NEEDED→STILL-NEEDED; E5:39 P14 CP-T07-08 NARROW … SUPERSEDED→SUPERSEDED; E5:40 P14 CP-T07-08 NARROW … STILL-NEEDED→STILL-NEEDED | in parts: STILL-NEEDED / SUPERSEDED |
| CP-T09-08 | E1:136 CP-T09-08 SUPERSEDED→SUPERSEDED; E4:318 CP-T09-08 STILL-NEEDED→SUPERSEDED; E5:101 P14 CP-T09-08 (AM-F-1… SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| CP-T10-08 | E1:163 CP-T10-08 SUPERSEDED→SUPERSEDED; E4:328 CP-T10-08 STILL-NEEDED→SUPERSEDED; E4:698 CP-T10-08 · AM-C-07 STILL-NEEDED→SUPERSEDED; E4:699 CP-T10-08 · AM-F-09 STILL-NEEDED→SUPERSEDED; E5:68 P14 CP-T10-08 RESEQUE… DONE-IN-CODE→DONE-IN-CODE; E5:69 P14 CP-T10-08 LIMIT (… STILL-NEEDED→SUPERSEDED | in parts: DONE-IN-CODE / SUPERSEDED |
| CP-T06-09 | E1:91 CP-T06-09 STILL-NEEDED→STILL-NEEDED; E4:290 CP-T06-09 STILL-NEEDED→STILL-NEEDED; E4:662 CP-T06-09 · AM-D-16 STILL-NEEDED→STILL-NEEDED; E4:663 CP-T06-09 · AM-D-17 STILL-NEEDED→STILL-NEEDED; E5:30 P14 CP-T06-09 LIMIT (… STILL-NEEDED→STILL-NEEDED; E5:31 P14 CP-T06-09 RESEQUE… SUPERSEDED→SUPERSEDED | in parts: STILL-NEEDED / SUPERSEDED |
| CP-T04-10 | E1:255 CP-T04-10a SUPERSEDED→SUPERSEDED; E1:256 CP-T04-10b STILL-NEEDED→STILL-NEEDED; E4:276 CP-T04-10 (levy / dis… SUPERSEDED→SUPERSEDED; E4:277 CP-T04-10 (larder sto… STILL-NEEDED→STILL-NEEDED | in parts: STILL-NEEDED / SUPERSEDED |
| CP-T03-11 | E1:88 CP-T03-11 SUPERSEDED→DONE-IN-CODE; E4:265 CP-T03-11 DONE-IN-CODE→DONE-IN-CODE; E4:542 §2 CP-T03-11 DONE-IN-CODE→DONE-IN-CODE | one: DONE-IN-CODE |
| CR-07 | E1:246 CR-07 MISSING-DEP→MISSING-DEP; E2:22 CR-07 STILL-NEEDED→MISSING-DEP; E4:336 CR-07 STILL-NEEDED→MISSING-DEP | one: MISSING-DEP |
| CR-08 | E1:161 CR-08 SUPERSEDED→SUPERSEDED; E2:23 CR-08 SUPERSEDED→SUPERSEDED; E4:337 CR-08 STILL-NEEDED→SUPERSEDED | one: SUPERSEDED |
| CR-46 | E1:166 CR-46a SUPERSEDED→SUPERSEDED; E1:167 CR-46b RULED-CONFLICT→SUPERSEDED; E2:70 CR-46 STILL-NEEDED→SUPERSEDED; E4:375 CR-46 STILL-NEEDED→SUPERSEDED | one: SUPERSEDED |
| CR-48 | E1:171 CR-48 SUPERSEDED→SUPERSEDED; E2:72 CR-48 SUPERSEDED→SUPERSEDED; E4:377 CR-48 STILL-NEEDED→SUPERSEDED | one: SUPERSEDED |
| CR-50 | E1:169 CR-50 SUPERSEDED→SUPERSEDED; E2:74 CR-50 SUPERSEDED→SUPERSEDED; E4:379 CR-50 STILL-NEEDED→SUPERSEDED | one: SUPERSEDED |
| CR-51 | E1:173 CR-51a SUPERSEDED→SUPERSEDED; E1:174 CR-51b STILL-NEEDED→STILL-NEEDED; E2:75 CR-51 SUPERSEDED→SUPERSEDED; E4:380 CR-51 STILL-NEEDED→STILL-NEEDED | in parts: STILL-NEEDED / SUPERSEDED |
| CR-52 | E1:168 CR-52 RULED-CONFLICT→SUPERSEDED; E2:76 CR-52 STILL-NEEDED→SUPERSEDED; E4:381 CR-52 STILL-NEEDED→SUPERSEDED | one: SUPERSEDED |
| CR-53 | E1:175 CR-53 SUPERSEDED→SUPERSEDED; E2:77 CR-53 SUPERSEDED→SUPERSEDED; E4:382 CR-53 STILL-NEEDED→SUPERSEDED | one: SUPERSEDED |
| CR-54 | E1:176 CR-54 SUPERSEDED→SUPERSEDED; E2:78 CR-54 SUPERSEDED→SUPERSEDED; E4:383 CR-54 STILL-NEEDED→SUPERSEDED | one: SUPERSEDED |
| CR-57 | E1:177 CR-57 STILL-NEEDED→SUPERSEDED; E2:81 CR-57 SUPERSEDED→SUPERSEDED; E4:386 CR-57 STILL-NEEDED→SUPERSEDED | one: SUPERSEDED |
| CR-61 | E1:181 CR-61 STILL-NEEDED→STILL-NEEDED; E2:85 CR-61 STILL-NEEDED→STILL-NEEDED; E4:390 CR-61 (docket item na… SUPERSEDED→SUPERSEDED; E4:391 CR-61 (`case` Record … STILL-NEEDED→STILL-NEEDED | in parts: STILL-NEEDED / SUPERSEDED |
| CR-80 | E1:244 CR-80 STILL-NEEDED→SUPERSEDED; E4:409 CR-80 SUPERSEDED→SUPERSEDED; E5:156 P16 CR-80 STILL-NEEDED→SUPERSEDED | one: SUPERSEDED |
| CR-85 | E1:249 CR-85 STILL-NEEDED→STILL-NEEDED; E2:34 CR-85a DONE-IN-CODE→DONE-IN-CODE; E2:35 CR-85b STILL-NEEDED→STILL-NEEDED; E4:414 CR-85 DONE-IN-CODE→DONE-IN-CODE | in parts: DONE-IN-CODE / STILL-NEEDED |
| CR-91 | E1:147 CR-91 RULED-CONFLICT→STILL-NEEDED; E2:39 CR-91a STILL-NEEDED→STILL-NEEDED; E2:40 CR-91b RULED-CONFLICT→SUPERSEDED; E4:420 CR-91 STILL-NEEDED→STILL-NEEDED | in parts: STILL-NEEDED / SUPERSEDED |
| CR-94 | E1:90 CR-94 SUPERSEDED→SUPERSEDED; E4:423 CR-94 STILL-NEEDED→SUPERSEDED | one: SUPERSEDED |
| FA-03 | E1:234 FA-03 SUPERSEDED→SUPERSEDED; E2:120 FA-03 DONE-IN-CODE→SUPERSEDED; E3:382 FA-03 STILL-NEEDED→SUPERSEDED; E4:451 FA-03 STILL-NEEDED→SUPERSEDED | one: SUPERSEDED |
| FA-07 | E1:235 FA-07 STILL-NEEDED→SUPERSEDED; E2:121 FA-07 SUPERSEDED→SUPERSEDED; E3:383 FA-07 SUPERSEDED→SUPERSEDED; E4:452 FA-07 STILL-NEEDED→SUPERSEDED | one: SUPERSEDED |
| GO-05 | E1:205 GO-05 STILL-NEEDED→STILL-NEEDED; E2:123 GO-05 STILL-NEEDED→STILL-NEEDED; E3:378 GO-05 SUPERSEDED→STILL-NEEDED; E4:454 GO-05 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| GO-06 | E1:209 GO-06 STILL-NEEDED→MISSING-DEP; E2:124 GO-06 MISSING-DEP→MISSING-DEP; E3:379 GO-06 SUPERSEDED→MISSING-DEP; E4:455 GO-06 STILL-NEEDED→MISSING-DEP | one: MISSING-DEP |
| GO-12 | E1:201 GO-12a SUPERSEDED→SUPERSEDED; E1:202 GO-12b STILL-NEEDED→STILL-NEEDED; E2:110 GO-12a SUPERSEDED→SUPERSEDED; E2:111 GO-12b SUPERSEDED→SUPERSEDED; E2:112 GO-12c STILL-NEEDED→STILL-NEEDED; E4:461 GO-12 STILL-NEEDED→STILL-NEEDED | in parts: STILL-NEEDED / SUPERSEDED |
| IN-09 | E2:130 IN-09 (alias -> REM-2… SUPERSEDED→SUPERSEDED; E3:344 IN-09 DONE-IN-CODE→DONE-IN-CODE | in parts: DONE-IN-CODE / SUPERSEDED |
| IN-12 | E2:96 IN-12 DONE-IN-CODE→DONE-IN-CODE; E3:345 IN-12 SUPERSEDED→DONE-IN-CODE; E4:466 IN-12 DONE-IN-CODE→DONE-IN-CODE | one: DONE-IN-CODE |
| IN-14 | E1:121 IN-14 SUPERSEDED→SUPERSEDED; E2:102 IN-14 SUPERSEDED→SUPERSEDED; E3:346 IN-14 STILL-NEEDED→SUPERSEDED; E4:467 IN-14 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| IN-18 | E1:245 IN-18 STILL-NEEDED→STILL-NEEDED; E2:92 IN-18 STILL-NEEDED→STILL-NEEDED; E3:347 IN-18 SUPERSEDED→STILL-NEEDED; E4:468 IN-18 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| IN-33 | E2:131 IN-33 (alias -> REM-2… SUPERSEDED→SUPERSEDED; E3:350 IN-33 DONE-IN-CODE→DONE-IN-CODE | in parts: DONE-IN-CODE / SUPERSEDED |
| IN-36 | E1:145 IN-36 STILL-NEEDED→STILL-NEEDED; E2:118 IN-36 STILL-NEEDED→STILL-NEEDED; E3:351 IN-36 DONE-IN-CODE→DONE-IN-CODE; E4:472 IN-36 (march cap; cas… STILL-NEEDED→STILL-NEEDED | in parts: DONE-IN-CODE / STILL-NEEDED |
| IN-44 | E1:240 IN-44 STILL-NEEDED→STILL-NEEDED; E2:93 IN-44 (row 1) DONE-IN-CODE→DONE-IN-CODE; E2:94 IN-44 (row 16) SUPERSEDED→SUPERSEDED; E2:95 IN-44 (rows 2-15 and … STILL-NEEDED→STILL-NEEDED; E3:352 IN-44 SUPERSEDED→STILL-NEEDED; E4:473 IN-44 STILL-NEEDED→STILL-NEEDED | in parts: DONE-IN-CODE / STILL-NEEDED / SUPERSEDED |
| IN-48 | E1:144 IN-48 SUPERSEDED→STILL-NEEDED; E2:119 IN-48 STILL-NEEDED→STILL-NEEDED; E3:356 IN-48 SUPERSEDED→STILL-NEEDED; E4:475 IN-48 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| IN-52 | E1:124 IN-52 STILL-NEEDED→STILL-NEEDED; E2:103 IN-52 STILL-NEEDED→STILL-NEEDED; E3:357 IN-52 SUPERSEDED→STILL-NEEDED; E4:476 IN-52 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| M31 | E3:61 M31 DONE-IN-CODE→DONE-IN-CODE; E5:117 P15 M31 STILL-NEEDED→SUPERSEDED | in parts: DONE-IN-CODE / SUPERSEDED |
| M32 | E3:62 M32 DONE-IN-CODE→DONE-IN-CODE; E5:118 P15 M32 SUPERSEDED→DONE-IN-CODE | one: DONE-IN-CODE |
| M33 | E3:63 M33 DONE-IN-CODE→DONE-IN-CODE; E5:119 P15 M33 SUPERSEDED→DONE-IN-CODE | one: DONE-IN-CODE |
| M34 | E3:64 M34 DONE-IN-CODE→STILL-NEEDED; E5:120 P15 M34 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| M36 | E3:66 M36 DONE-IN-CODE→STILL-NEEDED; E5:122 P15 M36 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| M37 | E3:67 M37 DONE-IN-CODE→DONE-IN-CODE; E5:123 P15 M37 SUPERSEDED→DONE-IN-CODE | one: DONE-IN-CODE |
| M39 | E3:69 M39 DONE-IN-CODE→STILL-NEEDED; E5:125 P15 M39 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| M40 | E3:70 M40 DONE-IN-CODE→STILL-NEEDED; E5:126 P15 M40, risk term SUPERSEDED→SUPERSEDED; E5:127 P15 M40, horizon term STILL-NEEDED→STILL-NEEDED | in parts: STILL-NEEDED / SUPERSEDED |
| MB-08 | E1:236 MB-08a SUPERSEDED→SUPERSEDED; E1:237 MB-08b STILL-NEEDED→SUPERSEDED; E2:125 MB-08 SUPERSEDED→SUPERSEDED; E3:370 MB-08 SUPERSEDED→SUPERSEDED; E4:480 MB-08 STILL-NEEDED→SUPERSEDED | one: SUPERSEDED |
| NM-W1 | E1:210 NM-W1 SUPERSEDED→SUPERSEDED; E2:48 NM-W1 STILL-NEEDED→SUPERSEDED; E4:482 NM-W1 STILL-NEEDED→SUPERSEDED | one: SUPERSEDED |
| NM-W4 | E1:211 NM-W4 SUPERSEDED→SUPERSEDED; E2:51 NM-W4 SUPERSEDED→SUPERSEDED; E4:485 NM-W4 STILL-NEEDED→SUPERSEDED | one: SUPERSEDED |
| NM-W5 | E1:212 NM-W5 SUPERSEDED→STILL-NEEDED; E2:52 NM-W5 STILL-NEEDED→STILL-NEEDED; E4:486 NM-W5 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| NM-W9 | E1:216 NM-W9a SUPERSEDED→SUPERSEDED; E1:217 NM-W9b STILL-NEEDED→STILL-NEEDED; E2:56 NM-W9 STILL-NEEDED→STILL-NEEDED; E4:490 NM-W9 STILL-NEEDED→STILL-NEEDED | in parts: STILL-NEEDED / SUPERSEDED |
| PC-06 | E1:238 PC-06 STILL-NEEDED→SUPERSEDED; E2:126 PC-06 SUPERSEDED→SUPERSEDED; E3:372 PC-06 SUPERSEDED→SUPERSEDED; E4:492 PC-06 STILL-NEEDED→SUPERSEDED | one: SUPERSEDED |
| PC-08 | E1:239 PC-08 STILL-NEEDED→STILL-NEEDED; E2:127 PC-08 STILL-NEEDED→STILL-NEEDED; E3:373 PC-08 SUPERSEDED→STILL-NEEDED; E4:493 PC-08 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| REM-26 | E4:518 REM-26 DONE-IN-CODE→DONE-IN-CODE; E5:88 P14 REM-26 (AM-A-12) STILL-NEEDED→STILL-NEEDED | in parts: DONE-IN-CODE / STILL-NEEDED |
| REM-30 | E4:522 REM-30 DONE-IN-CODE→DONE-IN-CODE; E5:93 P14 REM-30 (AM-A-18) STILL-NEEDED→STILL-NEEDED | in parts: DONE-IN-CODE / STILL-NEEDED |
| REM-40 | E4:559 §2 REM-40 WRONG→DONE-IN-CODE; E4:706 REM-40 · AM-A-02 WRONG→DONE-IN-CODE; E5:76 P14 REM-40 CUT (AM-A-… DONE-IN-CODE→DONE-IN-CODE | one: DONE-IN-CODE |
| REM-41 | E4:558 §2 REM-41 WRONG→DONE-IN-CODE; E4:707 REM-41 · AM-A-01 WRONG→DONE-IN-CODE; E5:77 P14 REM-41 CUT (AM-A-… DONE-IN-CODE→DONE-IN-CODE | one: DONE-IN-CODE |
| REM-45 | E4:527 REM-45 WRONG→WRONG; E4:550 §2 REM-45 WRONG→WRONG; E5:85 P14 REM-45 (AM-A-23) SUPERSEDED→WRONG | one: WRONG |
| REM-51 | E4:560 §2 REM-51 WRONG→WRONG; E4:708 REM-51 · AM-A-03 WRONG→WRONG; E5:78 P14 REM-51 CUT (AM-A-… SUPERSEDED→WRONG | one: WRONG |
| SC-02 | E1:250 SC-02 STILL-NEEDED→STILL-NEEDED; E2:99 SC-02 STILL-NEEDED→STILL-NEEDED; E3:360 SC-02 DONE-IN-CODE→DONE-IN-CODE; E4:532 SC-02 STILL-NEEDED→STILL-NEEDED | in parts: DONE-IN-CODE / STILL-NEEDED |
| SC-03 | E2:136 SC-03b, SC-08 (STALE) DONE-IN-CODE→DONE-IN-CODE; E3:361 SC-03b WRONG→WRONG | in parts: DONE-IN-CODE / WRONG |
| SC-04 | E3:362 SC-04 STILL-NEEDED→DONE-IN-CODE; E4:533 SC-04 DONE-IN-CODE→DONE-IN-CODE | one: DONE-IN-CODE |
| SC-07 | E1:242 SC-07 STILL-NEEDED→STILL-NEEDED; E2:129 SC-07 STILL-NEEDED→STILL-NEEDED; E3:365 SC-07 SUPERSEDED→STILL-NEEDED; E4:536 SC-07 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| SE-04 | E1:125 SE-04 SUPERSEDED→SUPERSEDED; E2:104 SE-04 (a) DONE-IN-CODE→DONE-IN-CODE; E2:105 SE-04 (b)(c) SUPERSEDED→SUPERSEDED; E3:366 SE-04 SUPERSEDED→SUPERSEDED; E4:537 SE-04 STILL-NEEDED→SUPERSEDED | in parts: DONE-IN-CODE / SUPERSEDED |
| SE-06 | E1:247 SE-06 SUPERSEDED→SUPERSEDED; E2:115 SE-06 SUPERSEDED→SUPERSEDED; E3:368 SE-06 DONE-IN-CODE→DONE-IN-CODE; E4:538 SE-06 STILL-NEEDED→SUPERSEDED | in parts: DONE-IN-CODE / SUPERSEDED |
| WR-01 | E1:112 WR-01 STILL-NEEDED→STILL-NEEDED; E2:101 WR-01 STILL-NEEDED→STILL-NEEDED; E3:376 WR-01 SUPERSEDED→STILL-NEEDED; E4:539 WR-01 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
