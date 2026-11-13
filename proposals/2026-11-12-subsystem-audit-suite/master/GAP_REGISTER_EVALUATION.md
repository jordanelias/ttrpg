# Evaluation of the gap register: one settled disposition per row, and what v12 takes from it

## Status: EVALUATION RECORD (stage 5 of `STAGES.md`, the settle-and-merge of lanes E6 to E8; reference, resolves nothing at runtime, CLAUDE.md §0.05; not canon; deleted when workplan v12 is adopted)

## Read at: the working tree of 2026-11-12 (`engine/season/hole_register.yaml`, 352 rows; the lanes read HEAD `a248c67`, and this pass re-loaded the register with `yaml.safe_load` to re-read rows in full). Producer: the settle lane (Opus), one round, no sub-agents.

**What this is.** Every row of the gap register (`engine/season/hole_register.yaml`, read by the corpus grader, not the loop) has one recorded disposition. Three lanes filed them (`master/eval/E6.md` rows 1 to 117, `E7.md` rows 118 to 234, `E8.md` rows 235 to 352); this file settles them alongside the workplan evaluation (`V11_EVALUATION.md`, whose §4 rules apply here too). A register row is a permanent record, not a build item: DONE-IN-CODE on a register row means its subject is in the tree (a producer, or a declared and swept default), not that a magnitude is right (E6's head states this once for all three lanes).

## 0. The parts

| part | what | how made |
|---|---|---|
| this file | counts, what was settled and why, findings for stage 6 | written |
| `_part2` | the settlement ledger for E6 to E8 (keyed `E<k>:<line>`), and the one-disposition-per-id table for the register ids that lane E3 also dispositioned (v11 parts 8 and 9 list hole rows) | generated from the settle record |
| `_part3` | lane E6's table and carry-forward blocks | copied by script, byte for byte |
| `_part4` | lane E7's table and blocks | copied |
| `_part5` | lane E8's table and blocks | copied |

The copies keep each lane's own call; where `_part2` changes a row, `_part2` governs. Each copy was checked by script against its source range.

## 1. Counts

Rows are the lanes' table rows: 352 register rows, 360 table rows (E6 splits five rows, E7 one, E8 two into a superseded part and a residue).

| source | rows | DONE-IN-CODE | SUPERSEDED | WRONG | STILL-NEEDED | MISSING-DEP | RULED-CONFLICT |
|---|---|---|---|---|---|---|---|
| E6 as filed | 122 | 82 | 23 | 2 | 12 | 3 | 0 |
| E6 settled | 122 | 80 | 23 | 2 | 16 | 1 | 0 |
| E7 as filed | 118 | 59 | 37 | 4 | 15 | 3 | 0 |
| E7 settled | 118 | 56 | 38 | 2 | 20 | 2 | 0 |
| E8 as filed | 120 | 14 | 96 | 0 | 8 | 2 | 0 |
| E8 settled | 120 | 14 | 96 | 0 | 8 | 2 | 0 |
| **total as filed** | **360** | **155** | **156** | **6** | **35** | **8** | **0** |
| **total settled** | **360** | **150** | **157** | **4** | **44** | **5** | **0** |

15 rows changed and 5 were re-cited (`_part2` §1). Across both deliverables: 2,052 rows, settled DONE-IN-CODE 843, SUPERSEDED 507, WRONG 71, STILL-NEEDED 609, MISSING-DEP 22 (`V11_EVALUATION.md` §1). The carried register rows join the 273 items of `master/eval/V12_INTAKE.md`; most are one item with a v11 position (§4).

## 2. Jordan's answers applied

- **A-105 (H-132).** A reduction of a sitting holder's grant is judged as a revocation, its odds read the power relation between the two factions (A-35's resistible draw with relative power as a term). H-132 stays STILL-NEEDED, now with its rule: one clause at `state/gate.py::may_fill`, FA, the new batch B21b, a declared hash mover. E3's row for it (DONE-IN-CODE, CR-25's landing) is settled to the same.
- **A-109 (H-325, H-326 residue).** No general exploration act: that part of H-325 is SUPERSEDED (travel and inquiry cover ordinary discovery; H-327's arrival-teaches lands in B12). What stays is a way to find what is hidden (a concealment rating or a withheld claim; a drawn find under the one opposed rule where a person conceals; what finding yields; the exposure risk at depth, which gives `surveil`'s Exposure effect its carrier). Both rows stay MISSING-DEP, re-cited: the dependency is A-109's design (SE and FI lanes, a design proposal first), and no Jordan decision remains (E8's CF-E8-5 asked whether the game has an exploration act at all; A-109 answers it).
- **A-100.** `MBA_DESIGN_part3.md` §8.2: **H-361** is NARROWED (stays SUPERSEDED, re-cited: the friction re-read is on the contact draw with the multiplier at zero, `27_MB_C` 27C-3 (k); the pair-rule part of its cite is superseded by MBA-04). H-150, H-97 and H-348 stand as the lanes filed them.
- **A-101.** No register row is changed by the round spec.

## 3. The weakest calls, re-checked

**WRONG calls (6 as filed): 4 confirmed, 2 reversed.** Confirmed: **H-52** (`verb_table.yaml`'s `open_case` carries its three-arm sweep only as `eligibility_sweep_note`, a note no code runs: re-read with `yaml.safe_load`); **H-87** (the depth sweep gives one hash at depths 1, 2, 3 and 7 because nothing recurses, `U5a_CORE_owed_edits.md` §A row 1); **H-168** (`migrate` executes in computed play, 16 of 116 at seed 0 over three seasons, `09_WR_B_pointer_text_for_the_orchestrator.md:99`, opened); **H-237** (12 chained claims of 22,958 at seed 0, `02_CHAR_reason_trail_and_small_edits.md:91`, opened). Reversed: **H-209** and **H-225**, WRONG to SUPERSEDED: their measurements cannot be reproduced at their seed, but the mechanism claim is unfalsified, and `09_WR_B_pointer_text_for_the_orchestrator.md:101-102` (opened) carries the re-measure at seed 2 or under the illness arm, after the duel path executes; WRONG ('do not carry') would have dropped a possibly real gap.

**E7's extract rows (rows 143 to 234, which E7 read as head fields and closure sentences).** This pass re-read the whole `cite:` of 37 of them (34 to the end; H-166, H-170 and H-222 to their first 2,600 characters), favouring STILL-NEEDED, MISSING-DEP, WRONG and SUPERSEDED-on-closure-only calls: H-153, H-154, H-164, H-166, H-168, H-169, H-170, H-171, H-172, H-173, H-176, H-180, H-181, H-185, H-191, H-192, H-193, H-195, H-198, H-199, H-204, H-208, H-209, H-211, H-214, H-219, H-220, H-222, H-224, H-225, H-226, H-227, H-229, H-232, H-236, H-237, H-241. Changed on the full text:

- **H-185** STILL-NEEDED to DONE-IN-CODE: the full cite records ladder step 4's precedent (`harness/corpus_run.py::build_at`, 2026-09-13: `Proposition.predicate` kept as a declared non-causal label) and IN-43's hold ('nothing planned needs it'); the extract had only the hole text.
- **H-199** DONE-IN-CODE to STILL-NEEDED: the full cite records two spacings of one ordinal (`world_q.remove_weight` and `refracted_confidence`), two ladders for one quantity, which is an S defect (CLAUDE.md §0.06) the ladder's step 5 settles by picking one.
- **H-181** MISSING-DEP to STILL-NEEDED: its producer is v11 CR-32 (E3 Block 18), carried in B21c.
- **H-173, H-222, H-224** DONE-IN-CODE (record rows) to STILL-NEEDED: v11's 'what closes it' (measure the four consequences; a writer of person-predicate claims; the window measurement at CR-29's exit) is owed and nothing supersedes it (E3 Blocks 9, 11, 12). E7's own cell for H-222 names the missing producer.
- **H-217** SUPERSEDED to STILL-NEEDED: its closure row says 'RESOLVED-BY plan CR-35', a v11 position, not a session item (this one rests on E7's evidence text, not the re-read cite).
- **H-171** re-cited: limit (2) is superseded by C3-C4 with `07_SE_population_regrowth_B.md` (:124-133, opened); limit (1) stays carried.

The other rows re-read held as filed.

**Rows E6 marked UNVERIFIED for an unopened carrier.** **H-63**: `05_SC_evidence_and_rebuttal.md:67` (`Record.stages`, the speech's write) opened, SUPERSEDED holds. **H-65**: `engine.season.loop.predicates` imported; all five prose-`requires` verbs (`confer`, `convene`, `dispatch`, `establish`, `revoke`) have registered predicates, so DONE-IN-CODE holds and the UNVERIFIED is lifted. **H-105**: `14_VERBS_MATERIAL_A_mending.md` §4 `work` (raises `site.worked`) opened, SUPERSEDED holds. **H-136**: `02_CHAR_offer_what_can_be_done.md`'s rule ('`opening_set` stops forming a candidate whose refusal the actor can read off his own state', :15-18) opened; a transfer to one's own hearth is such a refusal, so SUPERSEDED holds `[ASSUMPTION: the own-hearth case falls under the general rule; the proposal does not name it]`.

**SUPERSEDED calls resting on a closure row only.** This pass opened the cited proposal line behind 27 register rows (with 3 v11 rows, 30 in all): H-63, H-105, H-136 (the paragraph above), H-164 (`07_SE_capability_rate_B.md:43,104`), H-171 (above), H-203, H-260 (`06_FA_decree_binds.md:15,48,117`), H-232 (`14_VERBS_SOCIAL2_A_formation_on_what_is_known.md:40`), H-250 (`04_MB_headcount_grade_and_scale.md:85`), H-252 (`06_FA_hygiene.md:35-41`), H-254 (`15_INSTITUTIONS_COLONIAL_C_audit_and_charter.md:17`), H-257 (`U5d_WR_owed_edits.md` §1), H-258 and H-264 (`U5b_PC_residue.md:197,200`), H-259 (`08_FI_04_small-edits.md:78-82`), H-262 and H-298 (`06_FA_hygiene.md` item 4), H-263 (`03_PC_exits_withdrawal_recovery.md:90`), H-266 (`05_SC_contest_record_on_event.md:32`), H-267 (`05_SC_obstacle_difficulty_and_modifiers_B.md:47`), H-268 (`02_CHAR_which_ground_moves_whom.md:31`), H-269 (`16_PESSIMIST_SC_D_an_argument_moves_someone.md:28`), H-271 (`08_FI_03_playable-inquiry.md:29`), H-272 (`08_FI_02_rumour-that-travels.md:33`), H-338 (`16_PESSIMIST_CHAR_B_a_pursuit_does_what_its_name_says.md:66`, `02_CHAR_relations_have_a_ground.md:117`), H-209 and H-225 (above). Each line names the row's defect as the proposal's subject or carries its edit; none was reversed. (A grep of eight more cited proposals for the row's id found no mention; those rows keep the lanes' `[UNVERIFIED]` marks: H-265, H-273, H-307, H-317, H-334, H-350, H-170, H-215.)

## 4. One disposition per id, and the merged items

**84 register ids** were dispositioned differently by lane E3 (which tables the hole rows v11 parts 8 and 9 list) and a register lane. E3's convention 6 defers the register row to E6 to E8, so their call governs (`_part2` §2), with the exceptions of `V11_EVALUATION.md` §4 rule 5: a register lane's 'record' row whose v11 closure still owes work no session item supersedes is carried (H-11, H-125 with CR-22; H-173; H-199; H-222; H-224 with CR-29; H-217 with CR-35), and a 'missing dependency' that is in fact a v11 position is carried with it (H-47 and H-62 with CP-T07-02, the one carrier of a `Person.coherence` writer U3 §6.3 names; H-90 with CR-35 to CR-38 and IN-48; H-181 with CR-32). H-89 goes the other way: one item with CR-07, MISSING-DEP, because the instruction suite (IS-B2-CORE-06) records CR-07's pre-flight BLOCKED on content the plan may not author.

**Merged with v11 positions (one v12 item each).** H-145 with NM-W9 (b) (IN, B09); H-101 with CR-09 (FA, B21b); H-214 with CR-29, with H-224's measurement and H-234 (SUPERSEDED by FI-02 edit 1, a row on CR-29's reach roster) (FI/IN, B11 first); H-25 and H-106 with CR-98 (IN, B11F2: E6's `B10b-loops` folds into it); H-108 (b) with IN-48 (FA, B21b); H-47 and H-62 with CP-T07-02 (WR, B35); H-181 with CR-32 and H-217 with CR-35 and H-90 with CR-38 (FA, B21c); H-11 and H-125 with CR-22 (SE, B12); H-222 with A1-87 (SC, B27); H-314 with CP-T06-03/-04 (FI, B11); H-198 with M9 (held, MISSING-DEP); H-325 with H-326 (r) (A-109's design). The full list is `master/eval/V12_INTAKE.md` §1.

## 5. Errors the lanes found, settled here

- **H-262 and H-298: the closure row against the proposal.** `unified/U5_FINDINGS_CLOSURE_U5d.md:66` says 'HYG item 4 (R-11, R-12); declared hash mover'; `proposals/06_FA_hygiene.md:3,18-19` (opened) reads item 4 **WITHDRAWN** (D-U1-11h: the roster key stays `dispensation`, prose says *writ*, and *decree* for one proclaimed; no rename, no hash moves). The proposal is the later text (wave-3 reconciliation) and governs: both rows stay SUPERSEDED, closed by the glossary's words (*writ*, *sworn*); the closure row's text is stale and is for stage 6 to correct at its owner. The tree key `obligees` reads backwards; the glossary records its rename as a candidate (17 files, no hash), which is a v12 candidate item under `STAGES.md`'s tree-name rule.
- **H-245, H-246, H-247 cite a forked test.** `engine/season/tests/test_practice.py` is gone (`references/restructure_ledger.md:3166`, ED-IN-0314); the behaviour is covered elsewhere; E8's CF-E8-1 carries the text correction.
- **Stale counts in register heads** (E6): H-02 (56 verb rows; the tree has 67), H-01 (40 matrix rows; 42), H-61 (no module carries `entry:`; 16 of 16 do), H-65 (three verbs without a typed cell; none now). Text edits for B03's hygiene items.
- **A stale premise in a proposal** (E6): `proposals/12_ARCS_cited_evidence.md:31` says `destroy_record` cannot fire (H-75); the tree's row has `eligibility: [own, hold:<record>, presence]`, so it can.
- **E8's H-311 finding stands:** the session's proof-kind table (`08_FI_05_evidence-interface_B.md:54`) would still spend `confession.withheld` (emitted at `Failure`) as proof against the prisoner; carried STILL-NEEDED (CF-E8-4).

## 6. What this pass could not check

- Rows of E6 and E8 (read in full by their lanes) were not re-read here except where a rule, an answer or a conflict touched them; of E7's 92 extract rows, 37 were re-read, 55 keep E7's extract-based call.
- No run: no `aperture`, no seeded probe, no pytest. Every measured figure in a row is the row's own or a session proposal's; none was reproduced.
- The carry-forward blocks were copied, not re-read.
