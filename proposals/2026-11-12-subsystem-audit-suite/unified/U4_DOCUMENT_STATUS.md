# U4 — document status: every file in the suite, its class, and the test 9 census

## Status: WORK LEDGER (unification lane U4c, `UNIFICATION_BRIEF.md` lane U4 and test 9; reference, resolves nothing at runtime, CLAUDE.md §0.05; the table is generated, the census is read; deleted when v12 is adopted)

Read at: branch `ccr-62958c70-0kjhsw`, working-tree HEAD `8e88508`, 2026-11-12 (the tree is dirty: this lane's edits and the sibling U4 lanes' files are uncommitted). Producer: Sonnet lane U4c. Files on disk at generation: **496** (every file under `proposals/2026-11-12-subsystem-audit-suite/`, plus the 15 `research/` files the suite added). Rows 1 to 496 below are produced by a Bash script (scratch, not committed): it lists the directories, reads each file's first `## Status:` line, counts lines that begin `Reconciled:`, `Folded:` and `Grounded:` or `Re-grounded:`, takes the size, parses the batch handle from `unified/U3_DEPENDENCY_ORDER.md` §3.1 (node table) and §2.1 (split parts), and tallies closure dispositions from `unified/U5_FINDINGS_CLOSURE_*.md`.

## 0. What the unification stage reads in full, and what at heads

| class | depth the unification stage gave it | basis |
|---|---|---|
| LIVE-PROPOSAL, INCOMPLETE-LIVE, SUPERSEDED (all 300 files under `proposals/`) | **read in full** | `unified/UNIFICATION_RUN.md`: five read lanes R1 to R5 each read one family in full; seven wave-3 rewrite lanes then edited their own families. These are the things v12 will build, so they are the only class with a full-reading guarantee. This lane (U4c) did not re-read them in full; see section 3.2 for exactly what it opened. |
| REFERENCE-AUDIT (`audits/`, `census/`, the closure tables and conflict ledgers `unified/U5_*`) | **heads, decision tables and the closure tables only** | their findings already have a disposition in `unified/U5_FINDINGS_CLOSURE_*.md` (`UNIFICATION_RUN.md`, "Limit, stated once"). Audits 24 to 31 have no closure table of their own (section 5). |
| DIGEST (`digests/`, `dossiers/`) | heads only | coverage extracts and script-built indexes of the tree; no finding to disposition. |
| WORK-ORDER (the eight briefs, `unified/work/`, the U3 ledgers, `OWED_TO_UNIFICATION.md`, `STAGES.md`, `UNIFICATION_RUN.md`, `WAVE3_REWRITE_ORDER.md`, this file) | read as instructions to the lane that ran them | deleted when the stage that owns them closes (each file's own Status line says which). |
| REFERENCE (rulings record, decision registers, U1 glossary / owners / capability architecture, research maps, the 15 `research/` files, `README.md`) | read as the governing record by the lanes that cite them | `unified/DECISIONS_ANSWERED.md` governs (A-1 to A-93). |

## 1. The status classes (a vocabulary, not a canon status)

- **LIVE-PROPOSAL** — a proposal a v12 batch builds (U3 gives it a batch handle) and whose test 9 reading is COMPLETE.
- **INCOMPLETE-LIVE** — a proposal a batch builds, whose test 9 reading is INCOMPLETE: something in the file itself is undecided, unwritten or content-owned (section 3.4 names it, the code and the owner).
- **SUPERSEDED** — replaced by a named successor; nothing in it lands except where the note says. Cites the successor.
- **REFERENCE-AUDIT** — an audit, a census list, a closure table or a conflict ledger whose findings are dispositioned (RESOLVED-BY, SUPERSEDED, STALE / FALSE-POSITIVE, DISPUTED, JORDAN) in `unified/U5_FINDINGS_CLOSURE_*.md`.
- **DIGEST** — a coverage extract or a script-built index; carries no finding.
- **WORK-ORDER** — a brief, run plan, ledger, work file or work list; deleted when its stage closes.
- **REFERENCE** (one class added to the six named in the work order, because 25 files are none of them) — the rulings record, decision registers, glossary and owner ledgers, research maps and the 15 research files; kept as reference.

Not a mechanism: every class here is prose about prose (CLAUDE.md §0.05). Nothing in this file is read by a program.

## 2. Counts

### 2.1 Files by directory and class

| directory | LIVE-PROPOSAL | INCOMPLETE-LIVE | SUPERSEDED | REFERENCE-AUDIT | DIGEST | WORK-ORDER | REFERENCE | total |
|---|---|---|---|---|---|---|---|---|
| suite root (briefs) | · | · | · | · | · | 8 | 1 | 9 |
| proposals/ | 246 | 47 | 7 | · | · | · | · | 300 |
| audits/ | · | · | · | 65 | · | · | · | 65 |
| census/ | · | · | · | 6 | · | · | · | 6 |
| digests/ | · | · | · | · | 51 | · | · | 51 |
| dossiers/ | · | · | · | · | 13 | · | · | 13 |
| unified/ | · | · | · | 6 | · | 8 | 10 | 24 |
| unified/work | · | · | · | · | · | 13 | · | 13 |
| research (repo `research/`) | · | · | · | · | · | · | 15 | 15 |
| **all** | **246** | **47** | **7** | **77** | **64** | **29** | **26** | **496** |

Directory `unified/work/` is counted apart from `unified/`. The two sibling-lane outputs `unified/U4_TRACEABILITY.md` and `unified/U4_FACT_CHECK.md` are counted if they existed on disk at generation and were not opened by this lane.

## 3. Test 9 census (implementation-ready, `UNIFICATION_BRIEF.md` item 9)

### 3.1 Counts first

**300 proposal files: 246 COMPLETE, 47 INCOMPLETE, 7 SUPERSEDED (no instruction to check).** Of the 246 COMPLETE, 50 carry 65 `[UNVERIFIED …]` marks that mostly state a fallback and a first step ("open the site at landing"); they are counted COMPLETE where both branches are written (this lane tested none of the 65 beyond those in section 3.3), and the number is shown per file in the table (`open checks`).

| family | COMPLETE | INCOMPLETE | SUPERSEDED | total |
|---|---|---|---|---|
| PESSIMIST | 38 | 4 | 0 | 42 |
| INSTITUTIONS | 30 | 0 | 0 | 30 |
| VERBS | 21 | 7 | 0 | 28 |
| MB | 16 | 6 | 1 | 23 |
| WR | 19 | 3 | 0 | 22 |
| SC | 13 | 3 | 3 | 19 |
| CHAR | 12 | 3 | 0 | 15 |
| CORE | 12 | 3 | 0 | 15 |
| FA | 9 | 3 | 0 | 12 |
| SE | 9 | 3 | 0 | 12 |
| PC | 7 | 3 | 1 | 11 |
| FI | 8 | 1 | 1 | 10 |
| GO | 9 | 0 | 1 | 10 |
| CENSUS | 7 | 1 | 0 | 8 |
| DICE | 7 | 1 | 0 | 8 |
| NARRATIVE | 6 | 0 | 0 | 6 |
| STORY | 5 | 1 | 0 | 6 |
| PROCEDURAL | 4 | 1 | 0 | 5 |
| ARCS | 2 | 2 | 0 | 4 |
| DETERMINISM | 4 | 0 | 0 | 4 |
| HAPPENINGS | 3 | 1 | 0 | 4 |
| LACUNA | 4 | 0 | 0 | 4 |
| CAP | 1 | 0 | 0 | 1 |
| TESTS | 0 | 1 | 0 | 1 |
| **all** | **246** | **47** | **7** | **300** |

INCOMPLETE files by code (a file may carry two): DEP 19, CONTENT 15, DESIGN 15, SITE 6. CONTENT = values that are Jordan's or a content pass's to author; DEP = blocked on a dependency that has no carrier in the suite, or on a decision another file or lane owes; DESIGN = a part the file itself leaves undecided; SITE = a symbol or site the executing session must open first.

### 3.2 Method, and what it does not show

The census is a reading of the 300 files **as they stand after waves 1 to 3**, not a copy of the read lanes' §7 verdicts (`unified/work/R1_READ.md` to `R5_READ.md`): those marked almost every proposal INCOMPLETE for want of a named test, a lands-it line and a tier, and the wave-3 rewrite lanes then added them (`unified/work/W3_*_DONE.md`), so the old verdicts are stale. This lane did four things, in this order.
1. A script scanned every proposal for the eleven parts of item 9 (files and symbols, order, rows or schema, call sites, named tests, gate, falsifier, control, hash movers, dependencies, lands-it, cost class and tier): 296 of 300 carry a `Lands in batch` line, 294 name a model tier, 289 name a `test_` function or file, 298 have a gate heading, all 300 a falsifier. It flagged 36 non-superseded files with a marker gap (before this lane's edits). **This lane opened the relevant lines** (head, cost-class and gate sections) of the files whose gap was lands-it, dependency, hash movers or tests, except that `15_INSTITUTIONS_SYNTHESIS_C_crossings.md`, `21_PROCEDURAL_B_cast_and_seats.md` and `21_PROCEDURAL_E_names_and_texts.md` were judged on their cost-class line only; for the 13 files whose gap was the word "control" it read the falsifier lines of nine (each states a failing reading; none names a separate control arm in so many words, which is the one soft point of the census) and did not read the other four. Most gaps were wording (the file declares its hash movers in its gate, or names a command gate where no test file is needed); six were real (no dependency line) and were completed (section 3.3).
2. It collected every `INCOMPLETE` token in the 300 files (71 files carry one) and opened each line: 47 are a mark that the file itself leaves something unfinished, the rest cite a read lane's old verdict that the rewrite lane closed. The 47 are the INCOMPLETE rows (section 3.4); every line number cited there is a line this lane opened.
3. It collected every body-level `[UNVERIFIED …]` mark (81 lines in 61 files, not counting marks reported settled) and tested ten of them against the tree: seven were decidable by opening or grepping and were completed in five files (section 3.3); three (the value shape of a `matter.determined` deposit, which two files mark; the doer of a `field.won` Event) were not decidable by one grep and stay conditional. The other marks are conditional instructions with the fallback written and are counted in `open checks`; this lane did not test them.
4. It drew 12 COMPLETE files at random (seed 7) and checked each of the eleven parts by line number: 11 passed; one lacked a dependency line (`08_FI_07_shortest-playable-case.md`, completed). That is a sample of 12 of 246, so the COMPLETE count carries the residual risk of a part that is present by wording but thin in substance; the sample found no such file, and it cannot rule one out.

**Not examined:** this lane did not read the 246 COMPLETE files in full and did not run any gate. A file is COMPLETE here if the parts are present and the files and symbols it names were not contradicted by what this lane opened; it is not a statement that the edits are correct (that is the v12 batch's gate, CLAUDE.md §0.2). 44 files outside the INCOMPLETE rows contain the word "design-first" (a cost-class label, or a part that sits in another lane's file); they are counted COMPLETE where the file decides the shape and names the lane, and INCOMPLETE only where the file says it leaves the part open (section 3.4). This lane read the cost-class line of about twenty of them and did not read the rest. Names of the design-first labels: `grep -l 'design-first' proposals/*.md`.

### 3.3 Completed by this lane (14 files; each gained one `Reconciled:` line, marked "unification lane U4c")

| file | part that was missing | how it was decided (opened at the tree) |
|---|---|---|
| `02_CHAR_relations_have_a_ground.md` | `S`: the `to:` id mapping function | `f"p_{_slug(cid)}"` at `engine/season/harness/populated.py:1291`, `_slug` at `:113` |
| `07_SE_capability_rate_B.md` | `S`, `R`: `about_mid`'s existence and return | not in the tree; proposed by `02_CHAR_capability_uses_table.md:82`; required exactly `1.0` at gain 0, float, with a named test |
| `15_INSTITUTIONS_BYZANTINE_E_accession_recall_and_the_crowd.md` | `S`, `C`: `may_claim` body and the ban | `state/gate.py:769-788` has three conjuncts; the ban is asked by `_req_succeed` at `loop/predicates.py:193` |
| `14_VERBS_SOCIAL1_C_persuasion_and_deceit.md` | `C`, `G`: the corpus check's definition | `harness/corpus_run.py::bands_that_differ` (`:908-916`) counts `writes_at` only; the gate takes the `emits_at` fallback (`data/verbs.py:363`) |
| `31_WR_C_what_the_stances_feed.md` | `C`: readers of a goal row's `axis:` | none carries it (`goals.yaml:33` is a comment); sole reader `data/goals.py::_axis` (`:268-280`) |
| `14_VERBS_SOCIAL2_D_tie.md` | `H`: hash movers | none at landing if `tie_gain` lands at control 0; the later flip is the mover |
| `11_GO_fidelity_and_campaign_modes.md` | `H`: hash movers | none by default (gate 1 equality); gate 3's overlay is not a pinned world |
| `U5d_WR_zero_coherence_unknowable.md` | `H`: hash movers | none while `Person.coherence` has no writer (`state/world.py:1301-1308` is the only mention) |
| `12_ARCS_arcs_as_staged_goals.md` | `D`, `S`: dependency line; AM-B-09's reach | built rung-only (`rosters.yaml:2324-2330`); `person` is a listed goal-object kind (`:2321`); the open item narrows to one grep of `data/goals.py` (the file stays INCOMPLETE) |
| `08_FI_07_shortest-playable-case.md`, `08_FI_06_testimony-names-a-hand.md`, `08_FI_04_small-edits.md`, `01_CORE_requirements_reading_record.md`, `U5a_tests_digest_additions.md` | `D`: no dependency line | from `unified/U3_DEPENDENCY_ORDER.md` §3.1 and §1 item 3, and each file's own Lands line |

### 3.4 The INCOMPLETE rows: what is missing, and who owns it

Batch handle from U3 §3.1. "Lands" is the batch that lands the file once the part is supplied; it is not blocked as a whole unless the missing part is the file's only edit.

| family | file | batch | code | missing part | owner / what supplies it |
|---|---|---|---|---|---|
| ARCS | `12_ARCS_arcs_as_staged_goals.md` | B10 | SITE, CONTENT | item 5 (`org: {person: ...}`): AM-B-09 is built rung-only (`rosters.yaml:2324-2330`, `tests/test_cp_t02_03_aim_state.py:1`; other kinds read `open`), whether the goal loader admits a `person` organization is a grep of `data/goals.py` at landing; stage rows are per-case content | landing session (grep); case authors |
| ARCS | `12_ARCS_case_on_the_realm.md` | B39 | CONTENT | per-case `prehistory` lists and `beats` are content each case lane authors (line 71) | case authors |
| CENSUS | `17_CENSUS_C1A_02_wires_and_corrections.md` | B10 | DEP | the `march`/`_siege` row has no carrier (`effects_combat.py:686`); `besiege` has none (CP-T04-06) (line 135) | v12 stage: write a carrier |
| CHAR | `02_CHAR_choice_alignment.md` | B10 | CONTENT | the alignment cells are Jordan's (file line 122) | Jordan, or the CHAR content pass |
| CHAR | `02_CHAR_relations_have_a_ground.md` | B10 | CONTENT | the six relation rows' numbers are placeholders [ASSUMPTION; low] (line 158); the `to:` id mapping was completed by U4c | Jordan |
| CHAR | `U5a_CHAR_owed_amendments.md` | B10 | CONTENT | §7 signature rows and §10 goals are Jordan's or the CHAR content pass's (line 229) | Jordan, or the CHAR content pass |
| CORE | `28_CORE_scene_access_A_occupancy_and_precedence.md` | B28 | DESIGN, CONTENT | commit 3's ENCOUNTER half needs `social_contest.hearing` and the host-side attendee shape; commit 8's floors (95%, 60%) and gate row 12 are seeds; the Layer 1 row amendment is Jordan's (line 314) | SC hearing batch; Jordan |
| CORE | `28_CORE_scene_access_B_appointments.md` | B28 | DEP, DESIGN | commit 4 needs typed `utter` (`14_VERBS_SOCIAL2_B` §1); how the ask reaches the host as a `commit` referent is undecided (line 265) | B28 order; design pass |
| CORE | `28_CORE_scene_access_C_the_petition_that_waits.md` | B38 | DEP | commit 3 needs `dues_unmet` and a held-seat reader; commit 4 needs the one composer and a declining `carry` band (line 312) | B38 order after NARR_B/C and SOCIAL1_D |
| DICE | `29_DICE_one_opposed_rule_form_and_tuning.md` | B05 | DEP | item 29-5 hearing half: `HearingInput` and `Speaker` do not exist (line 370) | HEAR_B (B24) lands the records |
| FA | `06_FA_office_capabilities.md` | B04 | DEP | the writer of a claim of another person's capability has no carrier in the suite; the term ships as `None` (line 95) | U1 capability architecture §8 / CAP lane |
| FA | `U5d_FA_land_and_seats_pass_on_a_won_march.md` | B23 | DESIGN | whether build (i) meets A-58 is U3's to re-check (line 94) | U3 re-check, then the v12 stage |
| FA | `U5d_FA_owed_edits.md` | B21 | DESIGN | §9: no admitting basis for closing the previous holder's `hold` and opening the successor's; needs Layer 1 text (line 145) | Jordan (Layer 1 text) |
| FI | `08_FI_03_playable-inquiry.md` | B11 | DESIGN | §3 acting-on and §4: which row forms a petition from a held conclusion (line 162) | SC/FI design pass |
| HAPPENINGS | `22_HAPPENINGS_A_a_death_is_rare_caused_and_drawn.md` | B37 | CONTENT | the 46 age values (line 88) | Jordan, or the prose lane (A-15) |
| MB | `26_MASS_BATTLE_rout_pursuit_and_giving_ground.md` | B19 | SITE | the season path's re-targeting site is not named; `orchestration.py:2191` is the harness loop (line 145) | landing session greps the season path |
| MB | `27_MB_A_command_and_the_obedience_draw.md` | B19 | DEP, SITE | 27A-6 cannot be coded until CAP Part B lands (no `capabilities:` block, no `pool.py::score`); four symbols unopened (lines 368-380) | CAP Part B (B05); landing session |
| MB | `27_MB_B_unit_prowess_on_the_row.md` | B31 | DESIGN, SITE | the drill step (size, cap, host-side read in `_order_of_battle`) is design only; `Unit.base_combat_pool` read by grep only (lines 185, 235) | MB lane |
| MB | `27_MB_C_dynamic_strength_and_the_residual_chance.md` | B19 | DEP | 27C-2 waits on 27A-4 to 27A-6, `26_..._rout_pursuit...` and `16_PESSIMIST_MB_rout_has_two_exits` (line 325) | MB lane, in B19 order |
| MB | `27_MB_D_the_commander_as_chooser.md` | B20 | DESIGN | 27D-4, the unplayed commander's decider, is interface only: no cells, question, weighing or `reasons` wording (line 236) | CHAR |
| MB | `27_MB_E_what_an_army_carries_back.md` | B22 | CONTENT, DEP | every share table and window (27E-3, 27E-4) has no value; the cohort-dead write is SE's (line 388) | Jordan or a source search; SE |
| PC | `03_PC_duel_round_and_approach_B.md` | B16 | DESIGN | step 3d and step 5's MB side (what a contact is, what its result does to a unit) are design-first (cost class, line 398) | PC lane step 3d; MB lane for step 5 |
| PC | `03_PC_loadout_and_carry.md` | B18 | DESIGN | items 4 and 6 are design-first in MB, carried by `04_MB_unit_loadout_and_weapon_in_hand_B.md` (cost class, line 160) | MB lane |
| PC | `U5b_PC_residue.md` | B14 | SITE | §10: the ten loops are not named; `scan_tests.py` is not in the tree (line 218) | landing session |
| PESSIMIST | `16_PESSIMIST_CHAR_B_a_pursuit_does_what_its_name_says.md` | B10 | CONTENT | the cell values are Jordan's or the CHAR pass's (line 114) | Jordan, or the CHAR content pass |
| PESSIMIST | `16_PESSIMIST_GAME_the_world_draws.md` | B12 | DESIGN | the conversion of a body (0-1000) and a shortfall into a pool and an obstacle on the A-5 sampler; set at the joint calibration as two named fixtures (line 87) | calibration batch (B12) |
| PESSIMIST | `16_PESSIMIST_GO_surface_pins.md` | B41 | CONTENT | about 150 display strings (line 101) | Jordan, or authored under his review |
| PESSIMIST | `16_PESSIMIST_PC_A_the_yield_is_a_draw.md` | B15 | CONTENT | the shipped `YIELD_OB` values: the sweep's pick (line 172) | calibration step in B15 |
| PROCEDURAL | `21_PROCEDURAL_E_names_and_texts.md` | B39 | CONTENT | the name lists (`given`, `patronymic_suffix`, `byname`, `device`) (line 90) | Jordan, or drafted for his correction |
| SC | `05_SC_negotiation_scene.md` | B24 | DESIGN | edit 6's opening verb (`treat` or `petition` to a person) and the `exchange` operands (line 138); plan position CR-63, no carrier | SC design pass; v12 stage |
| SC | `05_SC_playable_hearing_B.md` | B24 | DESIGN, DEP | edits 6 and 8: the rite's reading waits on plan positions CR-60/CR-61; the NPC decider is a design pass (line 198) | SC design pass; v12 stage (step 5 evaluation of CR-60/61) |
| SC | `U5c_SC_proceedings_residue.md` | B27 | DEP | §3 waits on CR-61's case file naming its matters; §8 part 2 has no owner (line 226) | v12 stage (CR-61 evaluation) |
| SE | `07_SE_capability_rate_B.md` | B12 | DESIGN | which verb row `labour` weights read, and the caller in `loop/` that computes them (line 113); CP-T08-01 | CP-T08-01 landing; v12 stage |
| SE | `U5d_SE_cohort_heavy_moves_and_caste.md` | B38 | CONTENT | the caste rows' cells are Jordan's (line 132) | Jordan |
| SE | `U5d_SE_owed_edits.md` | B12 | DEP | the game reader of `write_matrix.yaml:375-381` (`steps: [MAT, CEN]`) is owed (line 50) | v12 stage |
| STORY | `U5d_STORY_owed_edits.md` | B39 | DEP | §1 depends on the commit that adds `besiege` to `march_postures` (CP-T04-06); no proposal carries it (head) | v12 stage |
| TESTS | `U5a_tests_digest_additions.md` | B02 | SITE | most sites are read from the digests and not opened (lines 20, 141) | the executing session opens each site first, as the file orders |
| VERBS | `14_VERBS_BINDING_D_orders.md` | B21 | DEP | the `dispatch` effect and its destination operand (CP-T09-08) have no carrier (line 121; U3 §6.3) | v12 stage: write a carrier or retire the edit |
| VERBS | `14_VERBS_MATERIAL_A_mending.md` | B12 | DESIGN | whether an Overwhelming/Success sabotage is unseen by persons at the Site: needs a formation conjunct with no stem in the typed grammar, or a masking rule `04` §C.6 lacks (line 152) | SE and FI owners |
| VERBS | `14_VERBS_MILITARY_A_movement.md` | B22 | DEP | five modifier rows are not members of OBS §2's closed roster; U1 must name them (line 137; R4 7b.8) | U1 owners ledger |
| VERBS | `14_VERBS_MILITARY_B_train.md` | B22 | DEP | the remaining modifiers are non-members of OBS §2 (line 81) | U1 owners ledger |
| VERBS | `14_VERBS_MILITARY_C_the_muster.md` | B22 | DEP | the hostile obstacle terms are not OBS §2 members (line 166) | U1 owners ledger |
| VERBS | `14_VERBS_MILITARY_D_the_order_of_battle.md` | B22 | DEP | none of the obstacle terms is an OBS §2 member (line 174) | U1 owners ledger |
| VERBS | `14_VERBS_PHYSICAL_B_field_and_ruin.md` | B22 | DEP | the leverage source for the army's size against the town is unnamed (line 65) | U1 owners ledger |
| WR | `09_WR_B_threadwork_session_and_practitioner.md` | B35 | CONTENT, DESIGN | [ASSUMPTION] values (overweave, fatigue scale, Focus cap) await CAP and the joint calibration; edit 4 design-first on B10-15's rows (lines 253-255) | calibration batch; Thread lane |
| WR | `09_WR_world_motion.md` | B12 | CONTENT | the wound's Site kind is Jordan's content (line 165) | Jordan |
| WR | `U5d_WR_zero_coherence_unknowable.md` | B35 | DEP | `Person.coherence` has no writer and no carrier (CP-T07-02; U3 §6.3); the readers ship and read nothing | v12 stage |

### 3.5 What blocks the rest, by owner

| owner | INCOMPLETE files |
|---|---|
| the lane named in the row | 17 |
| Jordan (values or Layer 1 text) | 12 |
| v12 stage (write a carrier, retire the edit, or evaluate the v11 plan position named) | 10 |
| U1 owners ledger (name OBS members, a leverage source) | 6 |
| a content pass (CHAR, prose, case authors) | 2 |

This lane found nothing in these rows that opening or grepping the tree could settle beyond what section 3.3 did: each missing part is a value, a Layer 1 text, a name U1 has not decided, a design the file leaves open, or a thing no proposal writes. The SITE rows are by design a landing session's first grep.

## 4. Every file

Columns: `R/F/G` is the number of head lines beginning `Reconciled:` / `Folded:` / `Grounded:` (or `Re-grounded:`). `closure` is, for a proposal, the number of closure-table rows whose carrier cell names the file; for an audit, its findings' dispositions as tallied from the rows under its heading in `U5_FINDINGS_CLOSURE_*.md`. `batch` is the U3 handle; "+part" names another batch where a section of the file lands. `T9` is the test 9 reading of section 3.

| # | file | class | Status (trimmed) | R/F/G | KB | family | closure | batch | T9 | note |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `AUDIT_BRIEF.md` | WORK-ORDER | REFERENCE (a work order, not canon; resolves nothing at run… | — | 45.9 | brief | — | — | — | Status line says REFERENCE; it is the standing rule set later stages read |
| 2 | `CENSUS_BRIEF.md` | WORK-ORDER | WORK ORDER (Jordan's direction of 2026-11-12: *"Fable to id… | — | 3.5 | brief | — | — | — |  |
| 3 | `IMPLEMENTATION_BRIEF_A.md` | WORK-ORDER | WORK ORDER (Jordan's direction of 2026-11-12; not canon; re… | — | 7.3 | brief | — | — | — |  |
| 4 | `INSTITUTIONS_BRIEF.md` | WORK-ORDER | WORK ORDER (Jordan's direction of 2026-11-12; not canon; re… | — | 9.2 | brief | — | — | — |  |
| 5 | `PESSIMIST_BRIEF.md` | WORK-ORDER | WORK ORDER (Jordan's direction of 2026-11-12: *"Fable 5.2 h… | — | 5.1 | brief | — | — | — |  |
| 6 | `README.md` | REFERENCE | REFERENCE (the suite's index; resolves nothing at runtime, … | — | 12.9 | index | — | — | — | this lane |
| 7 | `STAGES.md` | WORK-ORDER | WORK ORDER (Jordan's direction of 2026-11-12; not canon) | — | 26.4 | brief | — | — | — |  |
| 8 | `UNIFICATION_BRIEF.md` | WORK-ORDER | WORK ORDER (Jordan's direction of 2026-11-12: *"ensure all … | — | 10.4 | brief | — | — | — |  |
| 9 | `VERBS_BRIEF.md` | WORK-ORDER | WORK ORDER (Jordan's direction of 2026-11-12: *"we need fab… | — | 5.6 | brief | — | — | — |  |
| 10 | `proposals/01_CORE_capability_authoring_surface.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 17.9 | CORE | 6 RESOLVED-BY · 2 SUPERSEDED | B04 (B04-capability-home) | COMPLETE |  |
| 11 | `proposals/01_CORE_case_setup_and_beats.md` | LIVE-PROPOSAL | PROPOSED | 1/0/0 | 8.1 | CORE | 6 RESOLVED-BY | B39 (B39-procgen-and-cases) | COMPLETE |  |
| 12 | `proposals/01_CORE_claim_fade_as_read.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 7.6 | CORE | 9 RESOLVED-BY | B09 (B09-memory) | COMPLETE |  |
| 13 | `proposals/01_CORE_one_scene_contract.md` | LIVE-PROPOSAL | PROPOSED | 2/1/0 | 13.3 | CORE | 6 RESOLVED-BY · 1 SUPERSEDED | B34 (B34-go-surface) | COMPLETE |  |
| 14 | `proposals/01_CORE_predicates_name_their_clause.md` | LIVE-PROPOSAL | PROPOSED | 1/0/0 | 8.4 | CORE | 2 RESOLVED-BY · 1 SUPERSEDED | B09 (B09-memory) | COMPLETE (open checks: 1) |  |
| 15 | `proposals/01_CORE_reason_trail_in_the_act_store.md` | LIVE-PROPOSAL | PROPOSED | 1/0/0 | 8.4 | CORE | 4 RESOLVED-BY | B09 (B09-memory) | COMPLETE |  |
| 16 | `proposals/01_CORE_requirements_reading_record.md` | LIVE-PROPOSAL | PROPOSED | 3/0/0 | 5.9 | CORE | 5 RESOLVED-BY | B02 (B02-tests) | COMPLETE |  |
| 17 | `proposals/01_CORE_tests_delete_what_cannot_fail.md` | LIVE-PROPOSAL | PROPOSED | 1/0/0 | 12.1 | CORE | 2 RESOLVED-BY | B02 (B02-tests) | COMPLETE (open checks: 1) |  |
| 18 | `proposals/01_CORE_tests_one_golden_owner.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 15.5 | CORE | — | B02 (B02-tests) | COMPLETE |  |
| 19 | `proposals/01_CORE_tests_shipped_world_falsifiers.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 15.6 | CORE | 1 RESOLVED-BY · 1 SUPERSEDED | B02 (B02-tests) | COMPLETE (open checks: 1) |  |
| 20 | `proposals/01_CORE_unmet_need_is_attended_first.md` | LIVE-PROPOSAL | PROPOSED | 1/0/0 | 7.9 | CORE | 2 RESOLVED-BY | B10 (B10-character) | COMPLETE |  |
| 21 | `proposals/02_CHAR_capability_definitions.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 11.7 | CHAR | 6 RESOLVED-BY | B04 (B04-capability-home) | COMPLETE |  |
| 22 | `proposals/02_CHAR_capability_uses_table.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 10.0 | CHAR | 2 RESOLVED-BY | B04 (B04-capability-home) | COMPLETE |  |
| 23 | `proposals/02_CHAR_choice_alignment.md` | INCOMPLETE-LIVE | PROPOSED | 1/0/0 | 8.5 | CHAR | 2 RESOLVED-BY · 1 SUPERSEDED · 1 STALE/FALSE-POS | B10 (B10-character) | INCOMPLETE (CONTENT) |  |
| 24 | `proposals/02_CHAR_goal_lean_on_its_own_question.md` | LIVE-PROPOSAL | PROPOSED | 1/0/0 | 8.8 | CHAR | 4 RESOLVED-BY · 1 SUPERSEDED | B10 (B10-character) | COMPLETE |  |
| 25 | `proposals/02_CHAR_offer_what_can_be_done.md` | LIVE-PROPOSAL | PROPOSED | 1/0/1 | 12.2 | CHAR | 11 RESOLVED-BY · 1 SUPERSEDED | B10 (B10-character) | COMPLETE |  |
| 26 | `proposals/02_CHAR_reason_trail_and_small_edits.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 9.9 | CHAR | 7 RESOLVED-BY | B09 (B09-memory) | COMPLETE |  |
| 27 | `proposals/02_CHAR_relations_have_a_ground.md` | INCOMPLETE-LIVE | PROPOSED | 3/0/0 | 10.8 | CHAR | 4 RESOLVED-BY · 1 SUPERSEDED | B10 (B10-character) | INCOMPLETE (CONTENT) |  |
| 28 | `proposals/02_CHAR_resolve_and_temper.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 11.6 | CHAR | 6 RESOLVED-BY | B10 (B10-character) | COMPLETE |  |
| 29 | `proposals/02_CHAR_scar_cap_and_regard_unit.md` | LIVE-PROPOSAL | PROPOSED | 3/0/0 | 16.5 | CHAR | 6 RESOLVED-BY · 1 SUPERSEDED | B10 (B10-character) | COMPLETE |  |
| 30 | `proposals/02_CHAR_scar_is_a_wound.md` | LIVE-PROPOSAL | PROPOSED | 3/0/0 | 11.4 | CHAR | 6 RESOLVED-BY · 1 SUPERSEDED | B10 (B10-character) | COMPLETE |  |
| 31 | `proposals/02_CHAR_voices_and_the_room.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 14.8 | CHAR | 1 RESOLVED-BY | B10 (B10-character) | COMPLETE |  |
| 32 | `proposals/02_CHAR_what_an_act_risks.md` | LIVE-PROPOSAL | PROPOSED | 1/0/0 | 11.3 | CHAR | 2 RESOLVED-BY | B10 (B10-character) | COMPLETE |  |
| 33 | `proposals/02_CHAR_which_ground_moves_whom.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 12.7 | CHAR | 4 RESOLVED-BY | B24 (B24-sc-hearing) | COMPLETE |  |
| 34 | `proposals/03_PC_duel_chain_reach.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 10.7 | PC | 1 RESOLVED-BY · 2 SUPERSEDED | B01 (B01-laneA) | COMPLETE |  |
| 35 | `proposals/03_PC_duel_round_and_approach.md` | SUPERSEDED | PROPOSED (superseded in part by _B; see the line above) | 2/1/1 | 25.2 | PC | — | B16 (B16-pc-round) | n/a | successor: 03_PC_duel_round_and_approach_B.md (its own Lands line: "the superseded companion of PB; no edit of its own lands") |
| 36 | `proposals/03_PC_duel_round_and_approach_B.md` | INCOMPLETE-LIVE | PROPOSED | 3/1/0 | 38.4 | PC | 1 SUPERSEDED | B16 (B16-pc-round) | INCOMPLETE (DESIGN) |  |
| 37 | `proposals/03_PC_exits_withdrawal_recovery.md` | LIVE-PROPOSAL | PROPOSED | 3/0/0 | 13.8 | PC | 3 RESOLVED-BY · 1 SUPERSEDED | B16 (B16-pc-round) | COMPLETE |  |
| 38 | `proposals/03_PC_loadout_and_carry.md` | INCOMPLETE-LIVE | PROPOSED | 2/0/0 | 13.7 | PC | — | B18 (B18-pc-content) | INCOMPLETE (DESIGN) |  |
| 39 | `proposals/03_PC_person_inputs_content.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 13.4 | PC | — | B18 (B18-pc-content) | COMPLETE |  |
| 40 | `proposals/03_PC_typed_outcome_one_door.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 15.5 | PC | 2 RESOLVED-BY | B14 (B14-pc-outcome) | COMPLETE |  |
| 41 | `proposals/03_PC_weapon_form_at_round_start.md` | LIVE-PROPOSAL | PROPOSED | 1/0/0 | 7.7 | PC | — | B14 (B14-pc-outcome) | COMPLETE |  |
| 42 | `proposals/03_PC_weapon_records_in_the_export.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 11.4 | PC | — | B14 (B14-pc-outcome) | COMPLETE |  |
| 43 | `proposals/04_MB_campaign_party_economy.md` | LIVE-PROPOSAL | PROPOSED | 2/1/0 | 15.6 | MB | 2 RESOLVED-BY | B31 (B31-mb-loadout-economy) | COMPLETE |  |
| 44 | `proposals/04_MB_cell_hierarchy_as_data.md` | LIVE-PROPOSAL | PROPOSED | 2/2/0 | 18.5 | MB | — | B19 (B19-mb-field-calibration) | COMPLETE |  |
| 45 | `proposals/04_MB_cr12_linear_law.md` | LIVE-PROPOSAL | PROPOSED | 2/2/0 | 11.0 | MB | — | B19 (B19-mb-field-calibration) | COMPLETE |  |
| 46 | `proposals/04_MB_headcount_grade_and_scale.md` | LIVE-PROPOSAL | PROPOSED | 2/1/0 | 13.5 | MB | 1 SUPERSEDED | B17 (B17-mb-scale) | COMPLETE |  |
| 47 | `proposals/04_MB_manager_battle_one_resolver.md` | LIVE-PROPOSAL | PROPOSED | 2/2/0 | 22.3 | MB | 1 RESOLVED-BY · 2 SUPERSEDED | B20 (B20-mb-orders) | COMPLETE |  |
| 48 | `proposals/04_MB_playable_field_scenario.md` | LIVE-PROPOSAL | PROPOSED | 2/2/1 | 19.4 | MB | 1 SUPERSEDED | B20 (B20-mb-orders) +part B22 | COMPLETE |  |
| 49 | `proposals/04_MB_squad_grid_of_named_characters.md` | LIVE-PROPOSAL | PROPOSED | 2/0/1 | 18.3 | MB | — | B30 (B30-mb-nested) | COMPLETE |  |
| 50 | `proposals/04_MB_typed_outcome_and_one_path.md` | LIVE-PROPOSAL | PROPOSED | 2/1/0 | 14.6 | MB | 1 RESOLVED-BY · 1 SUPERSEDED | B17 (B17-mb-scale) | COMPLETE |  |
| 51 | `proposals/04_MB_unit_loadout_and_weapon_in_hand.md` | SUPERSEDED | SUPERSEDED by 04_MB_unit_loadout_and_weapon_in_hand_B.md (i… | 2/0/0 | 6.0 | MB | 1 SUPERSEDED | B17 (B17-mb-scale) | n/a | successor: 04_MB_unit_loadout_and_weapon_in_hand_B.md |
| 52 | `proposals/04_MB_unit_loadout_and_weapon_in_hand_B.md` | LIVE-PROPOSAL | PROPOSED | 2/2/0 | 21.4 | MB | 1 RESOLVED-BY | B17 (B17-mb-scale) +part B31 | COMPLETE |  |
| 53 | `proposals/05_SC_acquittal.md` | LIVE-PROPOSAL | PROPOSED | 2/0/1 | 9.2 | SC | 12 RESOLVED-BY | B27 (B27-sc-proceedings) | COMPLETE (open checks: 1) |  |
| 54 | `proposals/05_SC_arrangement_rows_that_bind.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 8.6 | SC | 7 RESOLVED-BY · 1 SUPERSEDED | B27 (B27-sc-proceedings) | COMPLETE |  |
| 55 | `proposals/05_SC_capability_surface.md` | LIVE-PROPOSAL | PROPOSED (edit 4 only; edits 1–3 superseded by U1) | 2/0/0 | 9.3 | SC | 5 RESOLVED-BY · 1 SUPERSEDED | B04 (B04-capability-home) | COMPLETE | partly superseded (see Status) |
| 56 | `proposals/05_SC_contest_record_on_event.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 8.7 | SC | 5 RESOLVED-BY | B05 (B05-one-roll) | COMPLETE |  |
| 57 | `proposals/05_SC_evidence_and_rebuttal.md` | SUPERSEDED | SUPERSEDED by 05_SC_evidence_and_rebuttal_B.md (kept for it… | 2/0/0 | 10.1 | SC | 1 RESOLVED-BY | B24 (B24-sc-hearing) | n/a | successor: 05_SC_evidence_and_rebuttal_B.md |
| 58 | `proposals/05_SC_evidence_and_rebuttal_B.md` | LIVE-PROPOSAL | PROPOSED — supersedes 05_SC_evidence_and_rebuttal.md (SC-P8… | 3/0/0 | 21.7 | SC | 1 STALE/FALSE-POS | B24 (B24-sc-hearing) | COMPLETE |  |
| 59 | `proposals/05_SC_hearing_capabilities.md` | LIVE-PROPOSAL | PROPOSED — extends SC-P7 (05_SC_capability_surface.md; one … | 2/0/0 | 12.2 | SC | — | B04 (B04-capability-home) +part B24 | COMPLETE |  |
| 60 | `proposals/05_SC_negotiation_scene.md` | INCOMPLETE-LIVE | PROPOSED — design-first (depends on the exchange verb's ope… | 2/1/0 | 11.6 | SC | 1 RESOLVED-BY · 1 STALE/FALSE-POS | B24 (B24-sc-hearing) | INCOMPLETE (DESIGN) |  |
| 61 | `proposals/05_SC_obstacle_difficulty_and_modifiers_B.md` | LIVE-PROPOSAL | PROPOSED (two edits: the difficulty: column and Margin.term… | 2/0/0 | 11.8 | SC | — | B05 (B05-one-roll) | COMPLETE | partly superseded (see Status) |
| 62 | `proposals/05_SC_opposed_obstacle_parity.md` | LIVE-PROPOSAL | PROPOSED — un-held by Jordan's A-26 (2026-11-12: an equal o… | 2/1/0 | 9.4 | SC | 2 RESOLVED-BY · 1 SUPERSEDED | B05 (B05-one-roll) | COMPLETE |  |
| 63 | `proposals/05_SC_playable_hearing.md` | SUPERSEDED | SUPERSEDED by 05_SC_playable_hearing_B.md (kept for its evi… | 2/0/0 | 10.5 | SC | 1 RESOLVED-BY | B24 (B24-sc-hearing) | n/a | successor: 05_SC_playable_hearing_B.md |
| 64 | `proposals/05_SC_playable_hearing_B.md` | INCOMPLETE-LIVE | PROPOSED — supersedes 05_SC_playable_hearing.md (SC-P3). De… | 5/1/0 | 22.2 | SC | 4 RESOLVED-BY · 1 SUPERSEDED | B24 (B24-sc-hearing) | INCOMPLETE (DESIGN, DEP) |  |
| 65 | `proposals/05_SC_sc05_kernel_disposition_B.md` | LIVE-PROPOSAL | PROPOSED — supersedes 05_SC_sc05_kernel_retirement.md (SC-P… | 2/0/0 | 13.8 | SC | 3 SUPERSEDED | B24 (B24-sc-hearing) | COMPLETE |  |
| 66 | `proposals/05_SC_sc05_kernel_retirement.md` | SUPERSEDED | SUPERSEDED by 05_SC_sc05_kernel_disposition_B.md (kept for … | 2/0/0 | 8.9 | SC | 2 RESOLVED-BY · 1 SUPERSEDED | B24 (B24-sc-hearing) | n/a | successor: 05_SC_sc05_kernel_disposition_B.md |
| 67 | `proposals/06_FA_decree_binds.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 17.5 | FA | 2 RESOLVED-BY · 1 SUPERSEDED | B21 (B21-fa-governance) | COMPLETE |  |
| 68 | `proposals/06_FA_hygiene.md` | LIVE-PROPOSAL | PROPOSED | 1/0/0 | 7.8 | FA | 2 SUPERSEDED | B03 (B03-hygiene) | COMPLETE |  |
| 69 | `proposals/06_FA_levy_through_the_seat_B.md` | LIVE-PROPOSAL | PROPOSED | 3/0/0 | 11.8 | FA | 3 RESOLVED-BY | B21 (B21-fa-governance) | COMPLETE |  |
| 70 | `proposals/06_FA_office_capabilities.md` | INCOMPLETE-LIVE | PROPOSED | 3/0/1 | 13.0 | FA | 1 RESOLVED-BY | B04 (B04-capability-home) | INCOMPLETE (DEP) |  |
| 71 | `proposals/06_FA_playable_scenario.md` | LIVE-PROPOSAL | PROPOSED | 4/0/1 | 13.9 | FA | 1 RESOLVED-BY | B21 (B21-fa-governance) | COMPLETE |  |
| 72 | `proposals/06_FA_remit_grant_by_row.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 9.7 | FA | — | B21 (B21-fa-governance) | COMPLETE |  |
| 73 | `proposals/06_FA_seat_terms_and_turnover.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 10.6 | FA | 1 SUPERSEDED | B21 (B21-fa-governance) | COMPLETE |  |
| 74 | `proposals/06_FA_seat_terms_by_body_B.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 9.8 | FA | — | B21 (B21-fa-governance) | COMPLETE |  |
| 75 | `proposals/06_FA_shortest_loop_B.md` | LIVE-PROPOSAL | PROPOSED | 3/0/0 | 9.4 | FA | — | B21 (B21-fa-governance) | COMPLETE |  |
| 76 | `proposals/06_FA_war_lives_in_seats_B.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 12.7 | FA | 1 RESOLVED-BY | B23 (B23-land) | COMPLETE (open checks: 1) |  |
| 77 | `proposals/07_SE_arc_needs.md` | LIVE-PROPOSAL | PROPOSED | 2/0/1 | 10.3 | SE | — | B12 (B12-world-motion-and-ground) | COMPLETE (open checks: 1) |  |
| 78 | `proposals/07_SE_campaign_supply_and_muster.md` | LIVE-PROPOSAL | PROPOSED | 2/0/1 | 16.3 | SE | 1 RESOLVED-BY | B22 (B22-mb-armies) | COMPLETE (open checks: 1) |  |
| 79 | `proposals/07_SE_capability_and_chooser_surface.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 8.5 | SE | 1 SUPERSEDED | B12 (B12-world-motion-and-ground) | COMPLETE |  |
| 80 | `proposals/07_SE_capability_rate_B.md` | INCOMPLETE-LIVE | PROPOSED | 3/0/0 | 14.9 | SE | — | B12 (B12-world-motion-and-ground) | INCOMPLETE (DESIGN) |  |
| 81 | `proposals/07_SE_ground_and_granaries.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 18.4 | SE | 2 RESOLVED-BY | B12 (B12-world-motion-and-ground) | COMPLETE |  |
| 82 | `proposals/07_SE_kernel_repairs.md` | LIVE-PROPOSAL | PROPOSED | 1/0/1 | 11.7 | SE | 2 RESOLVED-BY | B12 (B12-world-motion-and-ground) | COMPLETE |  |
| 83 | `proposals/07_SE_population_census.md` | LIVE-PROPOSAL | PROPOSED | 3/0/1 | 13.1 | SE | 2 RESOLVED-BY · 2 SUPERSEDED | B12 (B12-world-motion-and-ground) | COMPLETE |  |
| 84 | `proposals/07_SE_population_regrowth_B.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 14.6 | SE | — | B12 (B12-world-motion-and-ground) | COMPLETE |  |
| 85 | `proposals/07_SE_treasury_granary_B.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 11.6 | SE | 2 RESOLVED-BY | B12 (B12-world-motion-and-ground) | COMPLETE |  |
| 86 | `proposals/07_SE_valley_scenario.md` | LIVE-PROPOSAL | PROPOSED | 3/0/0 | 11.9 | SE | — | B12 (B12-world-motion-and-ground) | COMPLETE |  |
| 87 | `proposals/08_FI_01_claim-sourced-referents.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 9.1 | FI | — | B11 (B11-fi-readers) | COMPLETE |  |
| 88 | `proposals/08_FI_02_rumour-that-travels.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 9.7 | FI | 1 RESOLVED-BY | B11 (B11-fi-readers) | COMPLETE |  |
| 89 | `proposals/08_FI_03_playable-inquiry.md` | INCOMPLETE-LIVE | PROPOSED (design-first: §3 and §4 need a design pass before… | 2/0/0 | 13.1 | FI | — | B11 (B11-fi-readers) | INCOMPLETE (DESIGN) |  |
| 90 | `proposals/08_FI_04_small-edits.md` | LIVE-PROPOSAL | PROPOSED | 4/0/0 | 11.0 | FI | 2 RESOLVED-BY · 1 SUPERSEDED | B11 (B11-fi-readers) | COMPLETE |  |
| 91 | `proposals/08_FI_05_evidence-interface.md` | SUPERSEDED | SUPERSEDED by 08_FI_05_evidence-interface_B.md (kept for it… | 2/0/0 | 8.1 | FI | — | B24 (B24-sc-hearing) | n/a | successor: 08_FI_05_evidence-interface_B.md |
| 92 | `proposals/08_FI_05_evidence-interface_B.md` | LIVE-PROPOSAL | PROPOSED (an interface statement; the consumer is SC's and … | 3/0/0 | 16.5 | FI | 3 RESOLVED-BY | B24 (B24-sc-hearing) | COMPLETE |  |
| 93 | `proposals/08_FI_06_testimony-names-a-hand.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 10.2 | FI | — | B11 (B11-fi-readers) | COMPLETE |  |
| 94 | `proposals/08_FI_07_shortest-playable-case.md` | LIVE-PROPOSAL | PROPOSED (§1, §3, §4 are harness edits; §2 is two small eng… | 3/0/0 | 11.5 | FI | — | B11 (B11-fi-readers) | COMPLETE |  |
| 95 | `proposals/08_FI_08_knots-season-form.md` | LIVE-PROPOSAL | PROPOSED (§2 is an edit; §3 is sequencing; §1 and §4 are ha… | 1/0/1 | 9.5 | FI | 1 SUPERSEDED | B25 (B25-fi-questioning) | COMPLETE |  |
| 96 | `proposals/09_WR_B_chronicle_that_tells.md` | LIVE-PROPOSAL | PROPOSED | 3/1/0 | 9.9 | WR | — | B36 (B36-wr-story-instruments) | COMPLETE |  |
| 97 | `proposals/09_WR_B_draws_not_thresholds.md` | LIVE-PROPOSAL | PROPOSED | 2/1/1 | 13.6 | WR | 3 RESOLVED-BY · 1 DISPUTED | B12 (B12-world-motion-and-ground) +part B38 | COMPLETE |  |
| 98 | `proposals/09_WR_B_pointer_text_for_the_orchestrator.md` | LIVE-PROPOSAL | PROPOSED | 1/0/0 | 7.1 | WR | 1 SUPERSEDED | B03 (B03-hygiene) | COMPLETE |  |
| 99 | `proposals/09_WR_B_readings_of_closure_and_tension.md` | LIVE-PROPOSAL | PROPOSED | 2/1/0 | 11.7 | WR | — | B36 (B36-wr-story-instruments) | COMPLETE |  |
| 100 | `proposals/09_WR_B_threadwork_session_and_practitioner.md` | INCOMPLETE-LIVE | PROPOSED | 3/0/0 | 20.4 | WR | 1 RESOLVED-BY · 1 SUPERSEDED | B35 (B35-wr-thread) | INCOMPLETE (CONTENT, DESIGN) |  |
| 101 | `proposals/09_WR_B_weather_with_memory_and_the_year.md` | LIVE-PROPOSAL | PROPOSED | 2/1/0 | 18.6 | WR | 3 RESOLVED-BY | B12 (B12-world-motion-and-ground) +part B38 | COMPLETE (open checks: 1) |  |
| 102 | `proposals/09_WR_provided_arcs.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 11.3 | WR | 1 SUPERSEDED | B12 (B12-world-motion-and-ground) | COMPLETE |  |
| 103 | `proposals/09_WR_story_instruments_that_can_fail.md` | LIVE-PROPOSAL | PROPOSED | 1/1/0 | 12.3 | WR | — | B36 (B36-wr-story-instruments) | COMPLETE |  |
| 104 | `proposals/09_WR_strand_conclusion.md` | LIVE-PROPOSAL | PROPOSED | 2/1/0 | 11.5 | WR | 1 SUPERSEDED | B12 (B12-world-motion-and-ground) | COMPLETE |  |
| 105 | `proposals/09_WR_threadwork_module.md` | LIVE-PROPOSAL | PROPOSED | 4/0/0 | 11.8 | WR | 3 SUPERSEDED | B03 (B03-hygiene) | COMPLETE |  |
| 106 | `proposals/09_WR_world_motion.md` | INCOMPLETE-LIVE | PROPOSED | 2/0/0 | 11.8 | WR | 1 RESOLVED-BY · 1 SUPERSEDED | B12 (B12-world-motion-and-ground) | INCOMPLETE (CONTENT) |  |
| 107 | `proposals/10_DICE_advantage_sources_for_the_arcs.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 11.8 | DICE | 4 RESOLVED-BY · 2 SUPERSEDED | B05 (B05-one-roll) | COMPLETE |  |
| 108 | `proposals/10_DICE_believed_odds_have_a_prior.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 9.5 | DICE | 3 RESOLVED-BY · 1 SUPERSEDED | B05 (B05-one-roll) | COMPLETE |  |
| 109 | `proposals/10_DICE_capability_axiom_map.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 33.7 | DICE | 1 SUPERSEDED | B04 (B04-capability-home) | COMPLETE |  |
| 110 | `proposals/10_DICE_exported_face_rule_and_band_edges.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 8.8 | DICE | 1 RESOLVED-BY · 1 SUPERSEDED | B05 (B05-one-roll) | COMPLETE |  |
| 111 | `proposals/10_DICE_one_roller_one_fraction_rule.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 8.7 | DICE | 2 RESOLVED-BY | B05 (B05-one-roll) | COMPLETE |  |
| 112 | `proposals/10_DICE_one_score_two_roles.md` | LIVE-PROPOSAL | PROPOSED | 3/0/0 | 11.3 | DICE | 1 RESOLVED-BY · 1 SUPERSEDED | B05 (B05-one-roll) | COMPLETE |  |
| 113 | `proposals/11_GO_design_reference_disposition.md` | LIVE-PROPOSAL | PROPOSED | 1/0/0 | 8.5 | GO | — | B03 (B03-hygiene) | COMPLETE |  |
| 114 | `proposals/11_GO_fidelity_and_campaign_modes.md` | LIVE-PROPOSAL | PROPOSED | 4/0/0 | 15.2 | GO | — | B34 (B34-go-surface) | COMPLETE |  |
| 115 | `proposals/11_GO_float_contract.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 10.0 | GO | 1 RESOLVED-BY · 1 SUPERSEDED | B06 (B06-keyed-draw) | COMPLETE |  |
| 116 | `proposals/11_GO_one_draw_owner.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 12.2 | GO | 2 RESOLVED-BY · 1 SUPERSEDED | B06 (B06-keyed-draw) | COMPLETE |  |
| 117 | `proposals/11_GO_player_surface_contract.md` | SUPERSEDED | SUPERSEDED by 11_GO_player_surface_contract_B.md, except §2… | 3/0/0 | 14.4 | GO | — | B34 (B34-go-surface) | n/a | successor: 11_GO_player_surface_contract_B.md; its §2 `explain` stays live and lands in B34 |
| 118 | `proposals/11_GO_player_surface_contract_B.md` | LIVE-PROPOSAL | PROPOSED | 2/1/0 | 25.8 | GO | 8 RESOLVED-BY · 2 SUPERSEDED | B34 (B34-go-surface) | COMPLETE |  |
| 119 | `proposals/11_GO_pointer_and_stale_text_resolutions.md` | LIVE-PROPOSAL | PROPOSED | 1/0/0 | 9.9 | GO | 1 RESOLVED-BY · 1 SUPERSEDED | B03 (B03-hygiene) +part B06 | COMPLETE |  |
| 120 | `proposals/11_GO_port_gate_order_and_coverage.md` | LIVE-PROPOSAL | PROPOSED | 3/0/0 | 18.1 | GO | — | B41 (B41-go-port-gate) | COMPLETE |  |
| 121 | `proposals/12_ARCS_arcs_as_staged_goals.md` | INCOMPLETE-LIVE | PROPOSED | 3/2/0 | 9.0 | ARCS | 1 RESOLVED-BY · 1 SUPERSEDED | B10 (B10-character) | INCOMPLETE (SITE, CONTENT) |  |
| 122 | `proposals/12_ARCS_case_on_the_realm.md` | INCOMPLETE-LIVE | PROPOSED | 2/0/0 | 8.0 | ARCS | 1 RESOLVED-BY | B39 (B39-procgen-and-cases) | INCOMPLETE (CONTENT) |  |
| 123 | `proposals/12_ARCS_cited_evidence.md` | LIVE-PROPOSAL | PROPOSED (item 4 only; items 1–3 superseded by 05_SC_eviden… | 2/0/0 | 7.9 | ARCS | — | B24 (B24-sc-hearing) | COMPLETE (open checks: 1) | partly superseded (see Status) |
| 124 | `proposals/12_ARCS_substrate_as_ground.md` | LIVE-PROPOSAL | PROPOSED (A-40 rules Option A, ground; A-43 answers S-2; A-… | 2/0/0 | 9.2 | ARCS | — | B35 (B35-wr-thread) | COMPLETE |  |
| 125 | `proposals/13_SC_calibration.md` | LIVE-PROPOSAL | PROPOSED | 2/1/0 | 12.4 | SC | — | B05 (B05-one-roll) | COMPLETE |  |
| 126 | `proposals/13_SC_draw_for_unrolled_contests.md` | LIVE-PROPOSAL | PROPOSED — a pointer file: each of its five rolls is carrie… | 2/0/0 | 10.1 | SC | — | B07 (B07-task-draw) | COMPLETE |  |
| 127 | `proposals/13_SC_tuning_tables.md` | LIVE-PROPOSAL | PROPOSED | 2/1/0 | 19.3 | SC | 1 SUPERSEDED | B05 (B05-one-roll) | COMPLETE |  |
| 128 | `proposals/14_VERBS_BINDING_A_formation.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 16.0 | VERBS | — | B21 (B21-fa-governance) | COMPLETE (open checks: 1) |  |
| 129 | `proposals/14_VERBS_BINDING_B_sittings.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 10.6 | VERBS | — | B32 (B32-inst-kit) | COMPLETE |  |
| 130 | `proposals/14_VERBS_BINDING_C_turnover.md` | LIVE-PROPOSAL | PROPOSED | 3/0/0 | 16.6 | VERBS | — | B21 (B21-fa-governance) | COMPLETE |  |
| 131 | `proposals/14_VERBS_BINDING_D_orders.md` | INCOMPLETE-LIVE | PROPOSED | 3/0/0 | 12.8 | VERBS | — | B21 (B21-fa-governance) | INCOMPLETE (DEP) |  |
| 132 | `proposals/14_VERBS_BINDING_E_war_seats.md` | LIVE-PROPOSAL | PROPOSED | 3/0/0 | 10.5 | VERBS | — | B23 (B23-land) | COMPLETE |  |
| 133 | `proposals/14_VERBS_MATERIAL_A_mending.md` | INCOMPLETE-LIVE | PROPOSED | 2/0/0 | 18.3 | VERBS | — | B12 (B12-world-motion-and-ground) | INCOMPLETE (DESIGN) |  |
| 134 | `proposals/14_VERBS_MATERIAL_B_stores.md` | LIVE-PROPOSAL | PROPOSED | 3/0/1 | 16.0 | VERBS | — | B12 (B12-world-motion-and-ground) | COMPLETE |  |
| 135 | `proposals/14_VERBS_MATERIAL_C_works.md` | LIVE-PROPOSAL | PROPOSED | 2/0/1 | 13.2 | VERBS | — | B12 (B12-world-motion-and-ground) +part B25 | COMPLETE |  |
| 136 | `proposals/14_VERBS_MATERIAL_D_paper.md` | LIVE-PROPOSAL | PROPOSED | 2/0/1 | 20.5 | VERBS | — | B26 (B26-fi-inquiry) | COMPLETE (open checks: 1) |  |
| 137 | `proposals/14_VERBS_MATERIAL_E_knowledge.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 13.0 | VERBS | — | B26 (B26-fi-inquiry) | COMPLETE (open checks: 1) |  |
| 138 | `proposals/14_VERBS_MILITARY_A_movement.md` | INCOMPLETE-LIVE | PROPOSED | 2/2/0 | 19.7 | VERBS | — | B22 (B22-mb-armies) | INCOMPLETE (DEP) |  |
| 139 | `proposals/14_VERBS_MILITARY_B_train.md` | INCOMPLETE-LIVE | PROPOSED | 2/0/0 | 13.2 | VERBS | — | B22 (B22-mb-armies) | INCOMPLETE (DEP) |  |
| 140 | `proposals/14_VERBS_MILITARY_C_the_muster.md` | INCOMPLETE-LIVE | PROPOSED | 2/1/1 | 23.7 | VERBS | — | B22 (B22-mb-armies) | INCOMPLETE (DEP) |  |
| 141 | `proposals/14_VERBS_MILITARY_D_the_order_of_battle.md` | INCOMPLETE-LIVE | PROPOSED | 2/2/1 | 21.2 | VERBS | — | B22 (B22-mb-armies) | INCOMPLETE (DEP) |  |
| 142 | `proposals/14_VERBS_PHYSICAL_A_custody_and_force.md` | LIVE-PROPOSAL | PROPOSED | 3/1/0 | 17.3 | VERBS | 1 RESOLVED-BY · 1 SUPERSEDED | B15 (B15-pc-calibration) +part B29 | COMPLETE (open checks: 1) |  |
| 143 | `proposals/14_VERBS_PHYSICAL_B_field_and_ruin.md` | INCOMPLETE-LIVE | PROPOSED | 2/1/0 | 16.8 | VERBS | — | B22 (B22-mb-armies) +part B21 | INCOMPLETE (DEP) |  |
| 144 | `proposals/14_VERBS_PHYSICAL_C_looking.md` | LIVE-PROPOSAL | PROPOSED | 2/0/1 | 9.2 | VERBS | — | B26 (B26-fi-inquiry) | COMPLETE |  |
| 145 | `proposals/14_VERBS_PHYSICAL_D_thread_read.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 8.0 | VERBS | 1 SUPERSEDED | B35 (B35-wr-thread) | COMPLETE |  |
| 146 | `proposals/14_VERBS_SOCIAL1_A_formation.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 9.3 | VERBS | 1 SUPERSEDED | B11 (B11-fi-readers) | COMPLETE |  |
| 147 | `proposals/14_VERBS_SOCIAL1_B_documents_and_obedience.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 17.4 | VERBS | 1 RESOLVED-BY | B28 (B28-social-verbs) | COMPLETE (open checks: 3) |  |
| 148 | `proposals/14_VERBS_SOCIAL1_C_persuasion_and_deceit.md` | LIVE-PROPOSAL | PROPOSED | 3/0/0 | 12.6 | VERBS | — | B28 (B28-social-verbs) | COMPLETE (open checks: 2) |  |
| 149 | `proposals/14_VERBS_SOCIAL1_D_grievance_and_settlement.md` | LIVE-PROPOSAL | PROPOSED | 2/1/0 | 18.1 | VERBS | — | B28 (B28-social-verbs) | COMPLETE (open checks: 1) |  |
| 150 | `proposals/14_VERBS_SOCIAL2_A_formation_on_what_is_known.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 9.9 | VERBS | 1 SUPERSEDED | B25 (B25-fi-questioning) | COMPLETE |  |
| 151 | `proposals/14_VERBS_SOCIAL2_B_a_word_with_content.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 16.9 | VERBS | — | B25 (B25-fi-questioning) | COMPLETE (open checks: 1) |  |
| 152 | `proposals/14_VERBS_SOCIAL2_C_case_question_confession.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 16.6 | VERBS | — | B25 (B25-fi-questioning) | COMPLETE |  |
| 153 | `proposals/14_VERBS_SOCIAL2_D_tie.md` | LIVE-PROPOSAL | PROPOSED | 3/0/0 | 9.0 | VERBS | 1 RESOLVED-BY | B25 (B25-fi-questioning) | COMPLETE |  |
| 154 | `proposals/15_INSTITUTIONS_BYZANTINE_A_dignities_and_the_roll.md` | LIVE-PROPOSAL | PROPOSED | 3/0/1 | 16.2 | INSTITUTIONS | — | B32 (B32-inst-kit) | COMPLETE |  |
| 155 | `proposals/15_INSTITUTIONS_BYZANTINE_B_the_roga_and_the_fisc.md` | LIVE-PROPOSAL | PROPOSED | 3/0/1 | 14.2 | INSTITUTIONS | — | B33 (B33-inst-economy-hands) | COMPLETE (open checks: 1) |  |
| 156 | `proposals/15_INSTITUTIONS_BYZANTINE_C_the_hands_of_the_chain.md` | LIVE-PROPOSAL | PROPOSED | 3/0/1 | 15.6 | INSTITUTIONS | — | B33 (B33-inst-economy-hands) | COMPLETE (open checks: 2) |  |
| 157 | `proposals/15_INSTITUTIONS_BYZANTINE_D_the_empire_at_a_distance.md` | LIVE-PROPOSAL | PROPOSED | 3/0/1 | 15.3 | INSTITUTIONS | 1 RESOLVED-BY | B33 (B33-inst-economy-hands) | COMPLETE (open checks: 2) |  |
| 158 | `proposals/15_INSTITUTIONS_BYZANTINE_E_accession_recall_and_the_crowd.md` | LIVE-PROPOSAL | PROPOSED | 4/0/1 | 17.9 | INSTITUTIONS | — | B32 (B32-inst-kit) | COMPLETE (open checks: 3) |  |
| 159 | `proposals/15_INSTITUTIONS_BYZANTINE_F_playable_scenarios_and_reading.md` | LIVE-PROPOSAL | PROPOSED | 2/0/1 | 12.8 | INSTITUTIONS | — | B40 (B40-inst-scenarios) | COMPLETE (open checks: 2) |  |
| 160 | `proposals/15_INSTITUTIONS_BYZANTINE_grounding_mechanisms.md` | LIVE-PROPOSAL | PROPOSED (an executable plan for a later session; ratifies … | 1/0/0 | 18.5 | INSTITUTIONS | — | B40 (B40-inst-scenarios) | COMPLETE |  |
| 161 | `proposals/15_INSTITUTIONS_COLONIAL_A_instruments.md` | LIVE-PROPOSAL | PROPOSED | 3/0/1 | 16.4 | INSTITUTIONS | — | B32 (B32-inst-kit) | COMPLETE (open checks: 2) |  |
| 162 | `proposals/15_INSTITUTIONS_COLONIAL_B_distance.md` | LIVE-PROPOSAL | PROPOSED | 3/0/1 | 19.0 | INSTITUTIONS | 1 RESOLVED-BY | B33 (B33-inst-economy-hands) | COMPLETE (open checks: 1) |  |
| 163 | `proposals/15_INSTITUTIONS_COLONIAL_C_audit_and_charter.md` | LIVE-PROPOSAL | PROPOSED | 3/0/1 | 16.3 | INSTITUTIONS | — | B33 (B33-inst-economy-hands) | COMPLETE |  |
| 164 | `proposals/15_INSTITUTIONS_COLONIAL_D_accomplishment.md` | LIVE-PROPOSAL | PROPOSED (the part once held back is released by A-17/A-18;… | 3/0/1 | 13.1 | INSTITUTIONS | — | B33 (B33-inst-economy-hands) +part B39 | COMPLETE |  |
| 165 | `proposals/15_INSTITUTIONS_COLONIAL_E_scenario.md` | LIVE-PROPOSAL | PROPOSED | 2/0/1 | 12.7 | INSTITUTIONS | — | B40 (B40-inst-scenarios) | COMPLETE |  |
| 166 | `proposals/15_INSTITUTIONS_COLONIAL_grounding_F_what_the_tree_adds.md` | LIVE-PROPOSAL | PROPOSED (an executable plan for a later session; not ratif… | 2/0/0 | 25.0 | INSTITUTIONS | — | B40 (B40-inst-scenarios) | COMPLETE (open checks: 2) |  |
| 167 | `proposals/15_INSTITUTIONS_PAPACY_A_ground.md` | LIVE-PROPOSAL | PROPOSED | 1/0/1 | 9.8 | INSTITUTIONS | — | B32 (B32-inst-kit) | COMPLETE |  |
| 168 | `proposals/15_INSTITUTIONS_PAPACY_B_patronage_election_discipline.md` | LIVE-PROPOSAL | PROPOSED | 3/0/1 | 20.0 | INSTITUTIONS | 1 RESOLVED-BY · 2 SUPERSEDED | B32 (B32-inst-kit) | COMPLETE |  |
| 169 | `proposals/15_INSTITUTIONS_PAPACY_C_consecration_and_deed_ledger.md` | LIVE-PROPOSAL | PROPOSED | 3/0/1 | 16.1 | INSTITUTIONS | — | B33 (B33-inst-economy-hands) | COMPLETE (open checks: 1) |  |
| 170 | `proposals/15_INSTITUTIONS_PAPACY_D_sanction_and_absolution.md` | LIVE-PROPOSAL | PROPOSED | 3/0/1 | 18.9 | INSTITUTIONS | 1 RESOLVED-BY | B33 (B33-inst-economy-hands) | COMPLETE (open checks: 1) |  |
| 171 | `proposals/15_INSTITUTIONS_PAPACY_E_sees_tithe_orders_legates_council.md` | LIVE-PROPOSAL | PROPOSED (items 1-4 are content and small edits; item 6 is … | 3/0/1 | 16.9 | INSTITUTIONS | — | B33 (B33-inst-economy-hands) | COMPLETE (open checks: 1) |  |
| 172 | `proposals/15_INSTITUTIONS_PAPACY_F_playable_vacant_chair.md` | LIVE-PROPOSAL | PROPOSED | 3/0/1 | 11.1 | INSTITUTIONS | — | B40 (B40-inst-scenarios) | COMPLETE (open checks: 1) |  |
| 173 | `proposals/15_INSTITUTIONS_PAPACY_grounding_mechanisms.md` | LIVE-PROPOSAL | PROPOSED (an executable plan for a later session; ratifies … | 1/0/0 | 23.6 | INSTITUTIONS | — | B40 (B40-inst-scenarios) | COMPLETE (open checks: 2) |  |
| 174 | `proposals/15_INSTITUTIONS_SYNTHESIS_A_one_kit.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 28.0 | INSTITUTIONS | — | B32 (B32-inst-kit) | COMPLETE (open checks: 1) |  |
| 175 | `proposals/15_INSTITUTIONS_SYNTHESIS_B_the_deed_ledger.md` | LIVE-PROPOSAL | PROPOSED — the canon amendment it drafts is NOT APPLIED and… | 2/0/0 | 23.1 | INSTITUTIONS | 1 RESOLVED-BY | B32 (B32-inst-kit) +part B39 | COMPLETE (open checks: 2) |  |
| 176 | `proposals/15_INSTITUTIONS_SYNTHESIS_C_crossings.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 18.4 | INSTITUTIONS | — | B33 (B33-inst-economy-hands) | COMPLETE (open checks: 1) |  |
| 177 | `proposals/15_INSTITUTIONS_SYNTHESIS_D_first_playable.md` | LIVE-PROPOSAL | PROPOSED | 3/0/0 | 18.6 | INSTITUTIONS | — | B40 (B40-inst-scenarios) | COMPLETE |  |
| 178 | `proposals/15_INSTITUTIONS_SYNTHESIS_E_implementation_plan.md` | LIVE-PROPOSAL | PROPOSED (a plan; it schedules the twenty-one family propos… | 2/0/0 | 24.3 | INSTITUTIONS | — | B40 (B40-inst-scenarios) | COMPLETE |  |
| 179 | `proposals/15_INSTITUTIONS_VENICE_A_obligation_and_the_ask.md` | LIVE-PROPOSAL | PROPOSED | 2/0/1 | 14.4 | INSTITUTIONS | — | B33 (B33-inst-economy-hands) | COMPLETE |  |
| 180 | `proposals/15_INSTITUTIONS_VENICE_B_debt_instrument.md` | LIVE-PROPOSAL | PROPOSED | 2/0/1 | 17.9 | INSTITUTIONS | 1 RESOLVED-BY | B33 (B33-inst-economy-hands) | COMPLETE |  |
| 181 | `proposals/15_INSTITUTIONS_VENICE_C_roll_lot_ballot.md` | LIVE-PROPOSAL | PROPOSED | 3/0/1 | 19.0 | INSTITUTIONS | 2 RESOLVED-BY | B32 (B32-inst-kit) | COMPLETE (open checks: 1) |  |
| 182 | `proposals/15_INSTITUTIONS_VENICE_D_houses_charters_and_content.md` | LIVE-PROPOSAL | PROPOSED | 2/0/1 | 20.9 | INSTITUTIONS | — | B33 (B33-inst-economy-hands) | COMPLETE |  |
| 183 | `proposals/15_INSTITUTIONS_VENICE_grounding_E_what_the_tree_adds.md` | LIVE-PROPOSAL | PROPOSED (an executable plan for a later session; not ratif… | 2/0/0 | 24.8 | INSTITUTIONS | — | B40 (B40-inst-scenarios) | COMPLETE (open checks: 1) |  |
| 184 | `proposals/16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told.md` | LIVE-PROPOSAL | PROPOSED | 3/0/0 | 18.4 | PESSIMIST | 3 RESOLVED-BY | B10 (B10-character) | COMPLETE |  |
| 185 | `proposals/16_PESSIMIST_CHAR_B_a_pursuit_does_what_its_name_says.md` | INCOMPLETE-LIVE | PROPOSED | 2/0/0 | 12.8 | PESSIMIST | 1 RESOLVED-BY | B10 (B10-character) | INCOMPLETE (CONTENT) |  |
| 186 | `proposals/16_PESSIMIST_CHAR_C_the_stop_is_the_mans.md` | LIVE-PROPOSAL | PROPOSED (A-24 taken: item 4, the draw, is no longer held; … | 2/0/0 | 12.6 | PESSIMIST | — | B10 (B10-character) | COMPLETE |  |
| 187 | `proposals/16_PESSIMIST_CORE_a_refusal_is_remembered.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 11.3 | PESSIMIST | 4 RESOLVED-BY · 1 SUPERSEDED | B09 (B09-memory) | COMPLETE |  |
| 188 | `proposals/16_PESSIMIST_CORE_a_scene_runs_in_its_own_order.md` | LIVE-PROPOSAL | PROPOSED (A-9 taken: Option B is the plan; edit 5 is Layer … | 3/1/0 | 14.0 | PESSIMIST | 1 RESOLVED-BY · 1 SUPERSEDED | B08 (B08-scene-order) | COMPLETE |  |
| 189 | `proposals/16_PESSIMIST_CORE_no_stored_plan.md` | LIVE-PROPOSAL | PROPOSED | 1/0/0 | 7.1 | PESSIMIST | 2 RESOLVED-BY | B03 (B03-hygiene) | COMPLETE |  |
| 190 | `proposals/16_PESSIMIST_CORE_the_nine_gate_and_a_knockout_reading.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 9.9 | PESSIMIST | 2 RESOLVED-BY | B02 (B02-tests) | COMPLETE |  |
| 191 | `proposals/16_PESSIMIST_CORE_the_record_holds_what_changed.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 10.9 | PESSIMIST | 4 RESOLVED-BY | B09 (B09-memory) | COMPLETE |  |
| 192 | `proposals/16_PESSIMIST_DICE_soft_ceiling.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 13.1 | PESSIMIST | — | B05 (B05-one-roll) | COMPLETE |  |
| 193 | `proposals/16_PESSIMIST_DICE_task_difficulty_and_throughput.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 13.6 | PESSIMIST | 1 RESOLVED-BY | B05 (B05-one-roll) +part B07 | COMPLETE |  |
| 194 | `proposals/16_PESSIMIST_FA_A_dismissal_survives_the_king.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 15.5 | PESSIMIST | 1 RESOLVED-BY | B21 (B21-fa-governance) | COMPLETE (open checks: 1) |  |
| 195 | `proposals/16_PESSIMIST_FA_B_who_may_sit_join_and_declare.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 16.0 | PESSIMIST | — | B21 (B21-fa-governance) +part B32 | COMPLETE |  |
| 196 | `proposals/16_PESSIMIST_FA_C_under_the_seat.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 11.5 | PESSIMIST | — | B21 (B21-fa-governance) | COMPLETE |  |
| 197 | `proposals/16_PESSIMIST_FI_A_what_a_rumour_can_garble.md` | LIVE-PROPOSAL | PROPOSED | 1/0/0 | 10.6 | PESSIMIST | — | B11 (B11-fi-readers) | COMPLETE |  |
| 198 | `proposals/16_PESSIMIST_FI_B_a_paper_is_about_something.md` | LIVE-PROPOSAL | PROPOSED | 1/0/0 | 8.5 | PESSIMIST | — | B26 (B26-fi-inquiry) | COMPLETE |  |
| 199 | `proposals/16_PESSIMIST_FI_C_what_a_deed_leaves_behind.md` | LIVE-PROPOSAL | PROPOSED | 3/0/0 | 11.8 | PESSIMIST | — | B11 (B11-fi-readers) | COMPLETE |  |
| 200 | `proposals/16_PESSIMIST_FI_D_withhold_what_has_no_product.md` | LIVE-PROPOSAL | PROPOSED | 1/0/0 | 8.3 | PESSIMIST | 1 RESOLVED-BY | B26 (B26-fi-inquiry) | COMPLETE (open checks: 1) |  |
| 201 | `proposals/16_PESSIMIST_GAME_consequence_reading.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 8.0 | PESSIMIST | 2 RESOLVED-BY | B02 (B02-tests) | COMPLETE |  |
| 202 | `proposals/16_PESSIMIST_GAME_standing_occasions_carry_their_cause.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 8.3 | PESSIMIST | 2 RESOLVED-BY · 1 SUPERSEDED | B09 (B09-memory) | COMPLETE |  |
| 203 | `proposals/16_PESSIMIST_GAME_the_world_draws.md` | INCOMPLETE-LIVE | PROPOSED | 2/0/0 | 9.7 | PESSIMIST | — | B12 (B12-world-motion-and-ground) | INCOMPLETE (DESIGN) |  |
| 204 | `proposals/16_PESSIMIST_GO_a_witness_may_connect_what_he_holds.md` | LIVE-PROPOSAL | PROPOSED | 1/0/0 | 9.9 | PESSIMIST | — | B09 (B09-memory) | COMPLETE |  |
| 205 | `proposals/16_PESSIMIST_GO_keyed_draw_no_recorder.md` | LIVE-PROPOSAL | PROPOSED (A-30 taken: option A; the Layer 1 RNG row text is… | 2/0/0 | 10.3 | PESSIMIST | — | B06 (B06-keyed-draw) | COMPLETE |  |
| 206 | `proposals/16_PESSIMIST_GO_surface_pins.md` | INCOMPLETE-LIVE | PROPOSED | 1/0/0 | 9.6 | PESSIMIST | — | B41 (B41-go-port-gate) | INCOMPLETE (CONTENT) |  |
| 207 | `proposals/16_PESSIMIST_GO_the_offer_names_what_is_held.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 11.3 | PESSIMIST | — | B34 (B34-go-surface) | COMPLETE |  |
| 208 | `proposals/16_PESSIMIST_MB_one_stamina_ledger.md` | LIVE-PROPOSAL | PROPOSED | 2/2/0 | 12.5 | PESSIMIST | — | B19 (B19-mb-field-calibration) +part B31 | COMPLETE |  |
| 209 | `proposals/16_PESSIMIST_MB_partition_and_the_pair_rule.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 16.6 | PESSIMIST | — | B19 (B19-mb-field-calibration) | COMPLETE |  |
| 210 | `proposals/16_PESSIMIST_MB_rout_has_two_exits.md` | LIVE-PROPOSAL | PROPOSED | 2/2/0 | 17.1 | PESSIMIST | — | B19 (B19-mb-field-calibration) | COMPLETE |  |
| 211 | `proposals/16_PESSIMIST_PC_A_the_yield_is_a_draw.md` | INCOMPLETE-LIVE | PROPOSED | 2/0/0 | 14.4 | PESSIMIST | — | B15 (B15-pc-calibration) | INCOMPLETE (CONTENT) |  |
| 212 | `proposals/16_PESSIMIST_PC_B_the_commit_window.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 10.5 | PESSIMIST | — | B15 (B15-pc-calibration) | COMPLETE |  |
| 213 | `proposals/16_PESSIMIST_PC_C_what_the_world_keeps_of_a_fight.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 9.8 | PESSIMIST | — | B14 (B14-pc-outcome) | COMPLETE |  |
| 214 | `proposals/16_PESSIMIST_PC_D_armour_turns_a_blade_by_a_draw.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 10.3 | PESSIMIST | 1 RESOLVED-BY | B15 (B15-pc-calibration) | COMPLETE |  |
| 215 | `proposals/16_PESSIMIST_SC_A_what_the_speaker_brings_is_leverage.md` | LIVE-PROPOSAL | PROPOSED (not ratified by being written; CLAUDE.md §2) | 1/0/0 | 10.8 | PESSIMIST | — | B05 (B05-one-roll) | COMPLETE |  |
| 216 | `proposals/16_PESSIMIST_SC_B_one_reader_of_a_ledger.md` | LIVE-PROPOSAL | PROPOSED (not ratified by being written; CLAUDE.md §2) | 1/0/0 | 9.3 | PESSIMIST | — | B09 (B09-memory) | COMPLETE |  |
| 217 | `proposals/16_PESSIMIST_SC_C_a_verdict_names_its_party.md` | LIVE-PROPOSAL | PROPOSED (not ratified by being written; CLAUDE.md §2) | 1/0/0 | 11.6 | PESSIMIST | — | B27 (B27-sc-proceedings) | COMPLETE |  |
| 218 | `proposals/16_PESSIMIST_SC_D_an_argument_moves_someone.md` | LIVE-PROPOSAL | PROPOSED (not ratified by being written; CLAUDE.md §2) | 1/0/0 | 10.2 | PESSIMIST | — | B27 (B27-sc-proceedings) | COMPLETE |  |
| 219 | `proposals/16_PESSIMIST_SC_E_an_honest_teller_is_not_marked.md` | LIVE-PROPOSAL | PROPOSED (not ratified by being written; CLAUDE.md §2) | 1/0/0 | 9.9 | PESSIMIST | — | B11 (B11-fi-readers) | COMPLETE |  |
| 220 | `proposals/16_PESSIMIST_SE_A_the_granary_shares_and_the_dead_are_accounted.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 16.8 | PESSIMIST | — | B12 (B12-world-motion-and-ground) | COMPLETE |  |
| 221 | `proposals/16_PESSIMIST_SE_B_harvest_walls_and_the_supply_gate.md` | LIVE-PROPOSAL | PROPOSED | 2/0/1 | 13.4 | PESSIMIST | — | B12 (B12-world-motion-and-ground) | COMPLETE |  |
| 222 | `proposals/16_PESSIMIST_WR_A_the_road_is_drawn.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 13.0 | PESSIMIST | 1 RESOLVED-BY | B12 (B12-world-motion-and-ground) | COMPLETE |  |
| 223 | `proposals/16_PESSIMIST_WR_B_the_calamity_strains_and_breaks.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 12.4 | PESSIMIST | 1 RESOLVED-BY | B12 (B12-world-motion-and-ground) | COMPLETE |  |
| 224 | `proposals/16_PESSIMIST_WR_C_illness_on_the_body_ladder.md` | LIVE-PROPOSAL | PROPOSED (reduced: carried by 22_HAPPENINGS_A edit 2, C3-K4) | 2/0/0 | 9.0 | PESSIMIST | — | B37 (B37-happenings) | COMPLETE |  |
| 225 | `proposals/16_PESSIMIST_WR_D_small_clock_repairs_and_two_readings.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 10.2 | PESSIMIST | — | B36 (B36-wr-story-instruments) | COMPLETE |  |
| 226 | `proposals/17_CENSUS_C1A_01_deletion_batches.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 10.8 | CENSUS | — | B03 (B03-hygiene) | COMPLETE |  |
| 227 | `proposals/17_CENSUS_C1A_02_wires_and_corrections.md` | INCOMPLETE-LIVE | PROPOSED | 3/0/0 | 16.2 | CENSUS | — | B10 (B10-character) +part B12,B21,B22,B24,B34 | INCOMPLETE (DEP) |  |
| 228 | `proposals/17_CENSUS_C1B_01_deletions.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 12.5 | CENSUS | — | B03 (B03-hygiene) +part B24 | COMPLETE |  |
| 229 | `proposals/17_CENSUS_C1B_02_wires.md` | LIVE-PROPOSAL | PROPOSED | 1/0/0 | 10.0 | CENSUS | — | B36 (B36-wr-story-instruments) +part B39 | COMPLETE |  |
| 230 | `proposals/17_CENSUS_C1B_03_corrections.md` | LIVE-PROPOSAL | PROPOSED | 1/0/0 | 6.8 | CENSUS | — | B03 (B03-hygiene) | COMPLETE |  |
| 231 | `proposals/17_CENSUS_REST_1_deletions.md` | LIVE-PROPOSAL | PROPOSED | 2/0/1 | 10.9 | CENSUS | — | B03 (B03-hygiene) +part B11 | COMPLETE |  |
| 232 | `proposals/17_CENSUS_REST_2_wiring.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 20.1 | CENSUS | — | B32 (B32-inst-kit) +part B35 | COMPLETE (open checks: 1) |  |
| 233 | `proposals/17_CENSUS_REST_3_corrections.md` | LIVE-PROPOSAL | PROPOSED | 1/0/0 | 14.3 | CENSUS | — | B03 (B03-hygiene) | COMPLETE (open checks: 2) |  |
| 234 | `proposals/18_DETERMINISM_no_certain_matchup.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 8.2 | DETERMINISM | — | B15 (B15-pc-calibration) | COMPLETE |  |
| 235 | `proposals/18_DETERMINISM_notice_is_a_draw.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 11.2 | DETERMINISM | 1 RESOLVED-BY | B11 (B11-fi-readers) | COMPLETE |  |
| 236 | `proposals/18_DETERMINISM_rival_acts_in_one_fold.md` | LIVE-PROPOSAL | PROPOSED | 2/1/0 | 9.0 | DETERMINISM | 1 STALE/FALSE-POS | B08 (B08-scene-order) | COMPLETE |  |
| 237 | `proposals/18_DETERMINISM_task_draw_for_uncontested_verbs.md` | LIVE-PROPOSAL | PROPOSED | 2/0/1 | 20.7 | DETERMINISM | 3 RESOLVED-BY | B07 (B07-task-draw) | COMPLETE |  |
| 238 | `proposals/19_LACUNA_admission_rides_the_citing_draw.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 11.6 | LACUNA | 1 RESOLVED-BY | B24 (B24-sc-hearing) | COMPLETE |  |
| 239 | `proposals/19_LACUNA_conclusion_is_a_committed_assertion.md` | LIVE-PROPOSAL | PROPOSED (design-first in its value-space and record halves… | 2/0/0 | 12.0 | LACUNA | — | B11 (B11-fi-readers) | COMPLETE |  |
| 240 | `proposals/19_LACUNA_questioning_has_an_approach_and_a_cost.md` | LIVE-PROPOSAL | PROPOSED (small; depends on CP-T06-05, the questioned perso… | 2/0/0 | 9.1 | LACUNA | — | B26 (B26-fi-inquiry) | COMPLETE (open checks: 1) |  |
| 241 | `proposals/19_LACUNA_verdict_ladder_and_reversal.md` | LIVE-PROPOSAL | PROPOSED (results 1-4 are edits on existing owners; reversa… | 3/0/0 | 15.1 | LACUNA | — | B27 (B27-sc-proceedings) +part B36 | COMPLETE |  |
| 242 | `proposals/20_NARRATIVE_A_stands_for.md` | LIVE-PROPOSAL | PROPOSED | 1/2/0 | 19.8 | NARRATIVE | — | B38 (B38-narrative-regimes) | COMPLETE |  |
| 243 | `proposals/20_NARRATIVE_B_what_he_was_owed.md` | LIVE-PROPOSAL | PROPOSED | 2/2/0 | 17.1 | NARRATIVE | — | B38 (B38-narrative-regimes) | COMPLETE (open checks: 1) |  |
| 244 | `proposals/20_NARRATIVE_C_who_holds_what.md` | LIVE-PROPOSAL | PROPOSED | 2/1/0 | 16.0 | NARRATIVE | — | B38 (B38-narrative-regimes) | COMPLETE |  |
| 245 | `proposals/20_NARRATIVE_D_his_own_side.md` | LIVE-PROPOSAL | PROPOSED | 2/1/0 | 13.1 | NARRATIVE | — | B38 (B38-narrative-regimes) | COMPLETE |  |
| 246 | `proposals/20_NARRATIVE_E_the_year_and_the_reason.md` | LIVE-PROPOSAL | PROPOSED | 2/1/0 | 13.8 | NARRATIVE | — | B38 (B38-narrative-regimes) | COMPLETE |  |
| 247 | `proposals/20_NARRATIVE_F_story_inventory_and_gate.md` | LIVE-PROPOSAL | PROPOSED | 2/1/0 | 14.2 | NARRATIVE | — | B36 (B36-wr-story-instruments) +part B38 | COMPLETE |  |
| 248 | `proposals/21_PROCEDURAL_A_worldgen_tables_and_ground.md` | LIVE-PROPOSAL | PROPOSED (2026-11-12; Fable design lane; ratifies nothing; … | 2/0/0 | 17.6 | PROCEDURAL | — | B39 (B39-procgen-and-cases) | COMPLETE |  |
| 249 | `proposals/21_PROCEDURAL_B_cast_and_seats.md` | LIVE-PROPOSAL | PROPOSED (2026-11-12; Fable design lane; ratifies nothing; … | 3/0/0 | 24.1 | PROCEDURAL | 3 RESOLVED-BY · 1 SUPERSEDED | B39 (B39-procgen-and-cases) | COMPLETE |  |
| 250 | `proposals/21_PROCEDURAL_C_prologue_and_case_seeds.md` | LIVE-PROPOSAL | PROPOSED (2026-11-12; Fable design lane; ratifies nothing; … | 2/0/0 | 23.8 | PROCEDURAL | — | B39 (B39-procgen-and-cases) | COMPLETE |  |
| 251 | `proposals/21_PROCEDURAL_D_world_cards_and_churn.md` | LIVE-PROPOSAL | PROPOSED (2026-11-12; Fable design lane; ratifies nothing; … | 2/0/0 | 20.2 | PROCEDURAL | 1 RESOLVED-BY · 1 SUPERSEDED | B39 (B39-procgen-and-cases) | COMPLETE |  |
| 252 | `proposals/21_PROCEDURAL_E_names_and_texts.md` | INCOMPLETE-LIVE | PROPOSED (2026-11-12; Fable design lane; ratifies nothing; … | 1/0/0 | 10.3 | PROCEDURAL | — | B39 (B39-procgen-and-cases) | INCOMPLETE (CONTENT) |  |
| 253 | `proposals/22_HAPPENINGS_A_a_death_is_rare_caused_and_drawn.md` | INCOMPLETE-LIVE | PROPOSED | 2/0/1 | 21.0 | HAPPENINGS | 1 RESOLVED-BY · 1 SUPERSEDED | B37 (B37-happenings) | INCOMPLETE (CONTENT) |  |
| 254 | `proposals/22_HAPPENINGS_B_the_throne_is_never_stranded.md` | LIVE-PROPOSAL | PROPOSED | 3/0/1 | 13.5 | HAPPENINGS | 3 RESOLVED-BY | B21 (B21-fa-governance) +part B32 | COMPLETE |  |
| 255 | `proposals/22_HAPPENINGS_C_a_killing_is_a_crime_someone_commits.md` | LIVE-PROPOSAL | PROPOSED (A-16 taken: a person may try to kill another of h… | 2/0/0 | 13.4 | HAPPENINGS | 2 RESOLVED-BY · 2 SUPERSEDED | B37 (B37-happenings) | COMPLETE (open checks: 1) |  |
| 256 | `proposals/22_HAPPENINGS_D_batches_and_added_gates.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 13.0 | HAPPENINGS | — | B37 (B37-happenings) | COMPLETE (open checks: 1) |  |
| 257 | `proposals/23_STORY_A_what_a_roll_leaves.md` | LIVE-PROPOSAL | PROPOSED | 2/1/0 | 17.4 | STORY | — | B38 (B38-narrative-regimes) | COMPLETE |  |
| 258 | `proposals/23_STORY_B_a_house_continues.md` | LIVE-PROPOSAL | PROPOSED (A-75 taken: named births on, behind birth_rate; m… | 2/1/0 | 17.3 | STORY | — | B39 (B39-procgen-and-cases) | COMPLETE |  |
| 259 | `proposals/23_STORY_C_a_founded_place_can_fail.md` | LIVE-PROPOSAL | PROPOSED (one write-matrix cell is touched; named under "Wh… | 2/0/0 | 14.6 | STORY | — | B39 (B39-procgen-and-cases) | COMPLETE |  |
| 260 | `proposals/23_STORY_D_story_census_and_gate.md` | LIVE-PROPOSAL | PROPOSED | 2/1/0 | 16.3 | STORY | 1 RESOLVED-BY | B36 (B36-wr-story-instruments) | COMPLETE |  |
| 261 | `proposals/23_STORY_E_first_playable_the_lean_year.md` | LIVE-PROPOSAL | PROPOSED | 2/1/0 | 13.7 | STORY | — | B39 (B39-procgen-and-cases) | COMPLETE |  |
| 262 | `proposals/26_MASS_BATTLE_aggression_and_land.md` | LIVE-PROPOSAL | PROPOSED | 1/0/0 | 13.8 | MB | — | B23 (B23-land) | COMPLETE |  |
| 263 | `proposals/26_MASS_BATTLE_calibration_targets.md` | LIVE-PROPOSAL | PROPOSED | 1/1/0 | 12.8 | MB | — | B19 (B19-mb-field-calibration) | COMPLETE (open checks: 1) |  |
| 264 | `proposals/26_MASS_BATTLE_cell_scale_and_time.md` | LIVE-PROPOSAL | PROPOSED | 1/0/0 | 14.0 | MB | — | B19 (B19-mb-field-calibration) | COMPLETE |  |
| 265 | `proposals/26_MASS_BATTLE_maneuver_orders.md` | LIVE-PROPOSAL | PROPOSED | 1/1/0 | 16.7 | MB | — | B20 (B20-mb-orders) | COMPLETE |  |
| 266 | `proposals/26_MASS_BATTLE_movement_and_fatigue_as_data.md` | LIVE-PROPOSAL | PROPOSED | 1/1/0 | 13.5 | MB | — | B31 (B31-mb-loadout-economy) | COMPLETE |  |
| 267 | `proposals/26_MASS_BATTLE_rout_pursuit_and_giving_ground.md` | INCOMPLETE-LIVE | PROPOSED | 1/1/0 | 17.5 | MB | — | B19 (B19-mb-field-calibration) | INCOMPLETE (SITE) |  |
| 268 | `proposals/27_MB_A_command_and_the_obedience_draw.md` | INCOMPLETE-LIVE | PROPOSED | 1/0/0 | 32.1 | MB | — | B19 (B19-mb-field-calibration) | INCOMPLETE (DEP, SITE) |  |
| 269 | `proposals/27_MB_B_unit_prowess_on_the_row.md` | INCOMPLETE-LIVE | PROPOSED | 1/0/0 | 19.7 | MB | — | B31 (B31-mb-loadout-economy) | INCOMPLETE (DESIGN, SITE) |  |
| 270 | `proposals/27_MB_C_dynamic_strength_and_the_residual_chance.md` | INCOMPLETE-LIVE | PROPOSED | 1/1/0 | 29.2 | MB | — | B19 (B19-mb-field-calibration) | INCOMPLETE (DEP) |  |
| 271 | `proposals/27_MB_D_the_commander_as_chooser.md` | INCOMPLETE-LIVE | PROPOSED | 1/0/0 | 19.8 | MB | — | B20 (B20-mb-orders) | INCOMPLETE (DESIGN) |  |
| 272 | `proposals/27_MB_E_what_an_army_carries_back.md` | INCOMPLETE-LIVE | PROPOSED | 1/1/0 | 35.2 | MB | — | B22 (B22-mb-armies) | INCOMPLETE (CONTENT, DEP) |  |
| 273 | `proposals/28_CORE_scene_access_A_occupancy_and_precedence.md` | INCOMPLETE-LIVE | PROPOSED (a plan for future execution; nothing here is exec… | 1/0/0 | 31.3 | CORE | — | B28 (B28-social-verbs) | INCOMPLETE (DESIGN, CONTENT) |  |
| 274 | `proposals/28_CORE_scene_access_B_appointments.md` | INCOMPLETE-LIVE | PROPOSED (a plan for future execution; nothing here is exec… | 1/0/0 | 22.9 | CORE | — | B28 (B28-social-verbs) | INCOMPLETE (DEP, DESIGN) |  |
| 275 | `proposals/28_CORE_scene_access_C_the_petition_that_waits.md` | INCOMPLETE-LIVE | PROPOSED (a plan for future execution; nothing here is exec… | 1/0/0 | 28.8 | CORE | — | B38 (B38-narrative-regimes) | INCOMPLETE (DEP) |  |
| 276 | `proposals/29_DICE_one_opposed_rule_form_and_tuning.md` | INCOMPLETE-LIVE | PROPOSED (a decided plan for future execution; nothing here… | 1/0/0 | 39.0 | DICE | — | B05 (B05-one-roll) +part B15,B30 | INCOMPLETE (DEP) |  |
| 277 | `proposals/30_GO_F_the_plot_as_the_player_is_shown_it.md` | LIVE-PROPOSAL | PROPOSED | 1/0/0 | 21.2 | GO | — | B38 (B38-narrative-regimes) | COMPLETE |  |
| 278 | `proposals/30_WR_A_the_era_is_a_named_period.md` | LIVE-PROPOSAL | PROPOSED (ruled A-84: the era is a named period that always… | 1/0/0 | 29.1 | WR | — | B38 (B38-narrative-regimes) +part B39 | COMPLETE |  |
| 279 | `proposals/30_WR_B_regimes_who_believes_whom.md` | LIVE-PROPOSAL | PROPOSED | 1/1/0 | 16.8 | WR | — | B38 (B38-narrative-regimes) | COMPLETE |  |
| 280 | `proposals/30_WR_C_strands_open_grow_join_conclude.md` | LIVE-PROPOSAL | PROPOSED | 1/0/0 | 16.2 | WR | — | B38 (B38-narrative-regimes) | COMPLETE |  |
| 281 | `proposals/30_WR_D_momentum_and_its_brakes.md` | LIVE-PROPOSAL | PROPOSED | 2/0/0 | 23.2 | WR | — | B38 (B38-narrative-regimes) | COMPLETE |  |
| 282 | `proposals/30_WR_E_cascade_chains_and_the_census.md` | LIVE-PROPOSAL | PROPOSED | 1/0/0 | 19.6 | WR | — | B38 (B38-narrative-regimes) | COMPLETE |  |
| 283 | `proposals/30_WR_G_regime_opinions_and_the_pull_of_ones_own.md` | LIVE-PROPOSAL | PROPOSED (the roster rows are amended and the cast's values… | 2/1/0 | 21.5 | WR | — | B38 (B38-narrative-regimes) | COMPLETE |  |
| 284 | `proposals/31_WR_A_house_cores_and_the_cast_on_the_opinion_axes.md` | LIVE-PROPOSAL | PROPOSED (Jordan's A-87 to A-91 are the cores and the four … | 2/0/0 | 39.5 | WR | — | B38 (B38-narrative-regimes) | COMPLETE (open checks: 1) |  |
| 285 | `proposals/31_WR_B_the_revival_gathers.md` | LIVE-PROPOSAL | PROPOSED (the form is decided; its four numbers are [ASSUMP… | 1/0/0 | 18.9 | WR | — | B38 (B38-narrative-regimes) | COMPLETE |  |
| 286 | `proposals/31_WR_C_what_the_stances_feed.md` | LIVE-PROPOSAL | PROPOSED (four small edits, each a request to the file that… | 2/0/0 | 15.6 | WR | — | B38 (B38-narrative-regimes) | COMPLETE (open checks: 1) |  |
| 287 | `proposals/U5a_CHAR_owed_amendments.md` | INCOMPLETE-LIVE | PROPOSED (a plan for future execution; nothing here is exec… | 1/0/0 | 16.8 | CHAR | 15 RESOLVED-BY · 1 SUPERSEDED | B10 (B10-character) | INCOMPLETE (CONTENT) |  |
| 288 | `proposals/U5a_CHAR_self_knowledge_is_a_belief.md` | LIVE-PROPOSAL | PROPOSED (a plan for future execution; nothing here is exec… | 1/0/0 | 10.1 | CHAR | 2 RESOLVED-BY | B10 (B10-character) | COMPLETE |  |
| 289 | `proposals/U5a_CORE_owed_edits.md` | LIVE-PROPOSAL | PROPOSED (a plan for future execution; nothing here is exec… | 1/0/0 | 29.2 | CORE | 33 RESOLVED-BY · 1 JORDAN | B03 (B03-hygiene) +part B34 | COMPLETE (open checks: 1) |  |
| 290 | `proposals/U5a_DICE_owed_edits.md` | LIVE-PROPOSAL | PROPOSED (a plan for future execution; nothing here is exec… | 1/0/0 | 15.2 | DICE | 1 RESOLVED-BY | B05 (B05-one-roll) +part B09 | COMPLETE |  |
| 291 | `proposals/U5a_capability_home_and_two_inputs.md` | LIVE-PROPOSAL | PROPOSED (a plan for future execution; nothing here is exec… | 1/1/0 | 17.1 | CAP | 1 RESOLVED-BY | B04 (B04-capability-home) +part B05 | COMPLETE |  |
| 292 | `proposals/U5a_tests_digest_additions.md` | INCOMPLETE-LIVE | PROPOSED (a plan for future execution; nothing here is exec… | 2/0/0 | 13.4 | TESTS | — | B02 (B02-tests) | INCOMPLETE (SITE) |  |
| 293 | `proposals/U5b_MB_residue.md` | LIVE-PROPOSAL | PROPOSED (a plan for future execution; nothing here is exec… | 1/0/0 | 15.6 | MB | — | B17 (B17-mb-scale) +part B22 | COMPLETE (open checks: 3) |  |
| 294 | `proposals/U5b_MB_rulings_in_the_field.md` | LIVE-PROPOSAL | PROPOSED (a plan for future execution; nothing here is exec… | 1/1/0 | 21.1 | MB | — | B19 (B19-mb-field-calibration) +part B23 | COMPLETE |  |
| 295 | `proposals/U5b_PC_residue.md` | INCOMPLETE-LIVE | PROPOSED (a plan for future execution; nothing here is exec… | 1/0/0 | 17.7 | PC | — | B14 (B14-pc-outcome) | INCOMPLETE (SITE) |  |
| 296 | `proposals/U5b_PC_rulings_in_the_fight.md` | LIVE-PROPOSAL | PROPOSED (a plan for future execution; nothing here is exec… | 1/1/0 | 26.5 | PC | — | B15 (B15-pc-calibration) +part B37 | COMPLETE |  |
| 297 | `proposals/U5b_VERBS_military_physical_residue.md` | LIVE-PROPOSAL | PROPOSED (a plan for future execution; nothing here is exec… | 1/0/0 | 24.5 | VERBS | — | B07 (B07-task-draw) +part B23 | COMPLETE (open checks: 1) |  |
| 298 | `proposals/U5c_FI_residue.md` | LIVE-PROPOSAL | PROPOSED (written by the U5c closure lane; a plan for a lat… | 1/0/0 | 16.4 | FI | 1 RESOLVED-BY | B11 (B11-fi-readers) | COMPLETE |  |
| 299 | `proposals/U5c_SC_one_obstacle_form.md` | LIVE-PROPOSAL | PROPOSED (a reconciliation written by the U5c closure lane;… | 2/1/0 | 31.3 | SC | 1 RESOLVED-BY · 1 SUPERSEDED | B05 (B05-one-roll) | COMPLETE |  |
| 300 | `proposals/U5c_SC_proceedings_residue.md` | INCOMPLETE-LIVE | PROPOSED (written by the U5c closure lane; a plan for a lat… | 1/0/0 | 19.9 | SC | — | B27 (B27-sc-proceedings) | INCOMPLETE (DEP) |  |
| 301 | `proposals/U5c_VERBS_residue_and_governance_owner.md` | LIVE-PROPOSAL | PROPOSED (written by the U5c closure lane; a plan for a lat… | 1/0/0 | 21.2 | VERBS | — | B07 (B07-task-draw) +part B09,B11,B24 | COMPLETE (open checks: 1) |  |
| 302 | `proposals/U5d_FA_land_and_seats_pass_on_a_won_march.md` | INCOMPLETE-LIVE | PROPOSED (a plan for a later implementation lane; nothing h… | 2/0/0 | 21.6 | FA | 3 RESOLVED-BY · 2 SUPERSEDED | B23 (B23-land) | INCOMPLETE (DESIGN) |  |
| 303 | `proposals/U5d_FA_owed_edits.md` | INCOMPLETE-LIVE | PROPOSED (a plan for a later implementation lane; nothing h… | 2/0/0 | 14.7 | FA | 1 RESOLVED-BY · 1 SUPERSEDED | B21 (B21-fa-governance) +part B32,B39 | INCOMPLETE (DESIGN) |  |
| 304 | `proposals/U5d_GO_owed_edits.md` | LIVE-PROPOSAL | PROPOSED (a plan for a later implementation lane; nothing h… | 1/0/0 | 5.1 | GO | — | B06 (B06-keyed-draw) | COMPLETE |  |
| 305 | `proposals/U5d_SE_cohort_heavy_moves_and_caste.md` | INCOMPLETE-LIVE | PROPOSED (a plan for a later implementation lane; nothing h… | 1/1/0 | 10.6 | SE | 2 RESOLVED-BY · 4 SUPERSEDED | B38 (B38-narrative-regimes) | INCOMPLETE (CONTENT) |  |
| 306 | `proposals/U5d_SE_owed_edits.md` | INCOMPLETE-LIVE | PROPOSED (a plan for a later implementation lane; nothing h… | 1/0/0 | 8.9 | SE | 1 RESOLVED-BY · 1 DISPUTED | B12 (B12-world-motion-and-ground) | INCOMPLETE (DEP) |  |
| 307 | `proposals/U5d_STORY_owed_edits.md` | INCOMPLETE-LIVE | PROPOSED (a plan for a later implementation lane; nothing h… | 1/0/0 | 7.4 | STORY | 5 RESOLVED-BY | B39 (B39-procgen-and-cases) | INCOMPLETE (DEP) |  |
| 308 | `proposals/U5d_WR_owed_edits.md` | LIVE-PROPOSAL | PROPOSED (a plan for a later implementation lane; nothing h… | 1/0/0 | 4.4 | WR | — | B12 (B12-world-motion-and-ground) +part B37 | COMPLETE |  |
| 309 | `proposals/U5d_WR_zero_coherence_unknowable.md` | INCOMPLETE-LIVE | PROPOSED, design-first (a plan for a later implementation l… | 2/0/0 | 7.7 | WR | 1 RESOLVED-BY · 1 SUPERSEDED | B35 (B35-wr-thread) | INCOMPLETE (DEP) |  |
| 310 | `audits/01_CORE_audit.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | 0/0/1 | 54.3 | CORE | 40 RESOLVED-BY · 4 SUPERSEDED · 6 STALE/FALSE-POS | — | — |  |
| 311 | `audits/01_CORE_audit_addendum_B.md` | REFERENCE-AUDIT | REFERENCE (an audit addendum; resolves nothing at runtime) | — | 78.8 | CORE | 44 RESOLVED-BY · 6 SUPERSEDED · 1 STALE/FALSE-POS · 3 JORDAN | — | — |  |
| 312 | `audits/01_CORE_audit_addendum_C_tests.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | — | 37.5 | CORE | 18 RESOLVED-BY · 2 SUPERSEDED · 1 STALE/FALSE-POS | — | — |  |
| 313 | `audits/02_CHAR_audit.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | 0/0/1 | 79.3 | CHAR | 30 RESOLVED-BY · 2 SUPERSEDED | — | — |  |
| 314 | `audits/02_CHAR_audit_addendum_B.md` | REFERENCE-AUDIT | REFERENCE (an audit addendum; resolves nothing at runtime) | — | 78.8 | CHAR | 12 RESOLVED-BY | — | — |  |
| 315 | `audits/03_PC_audit.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | — | 80.7 | PC | 60 RESOLVED-BY · 29 SUPERSEDED · 4 STALE/FALSE-POS | — | — |  |
| 316 | `audits/03_PC_audit_addendum_B.md` | REFERENCE-AUDIT | REFERENCE (an audit addendum; resolves nothing at runtime) | — | 46.3 | PC | 24 RESOLVED-BY · 12 SUPERSEDED | — | — |  |
| 317 | `audits/04_MB_audit.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | 0/2/2 | 141.6 | MB | 46 RESOLVED-BY · 18 SUPERSEDED · 2 STALE/FALSE-POS | — | — |  |
| 318 | `audits/04_MB_audit_addendum_B.md` | REFERENCE-AUDIT | REFERENCE (an audit addendum; resolves nothing at runtime) | 0/0/1 | 94.2 | MB | 30 RESOLVED-BY · 11 SUPERSEDED · 1 STALE/FALSE-POS | — | — |  |
| 319 | `audits/05_SC_audit.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | 0/0/1 | 86.9 | SC | 45 RESOLVED-BY · 9 SUPERSEDED · 1 STALE/FALSE-POS | — | — |  |
| 320 | `audits/05_SC_audit_addendum_B.md` | REFERENCE-AUDIT | REFERENCE (an audit addendum; resolves nothing at runtime) | 1/0/1 | 57.8 | SC | 45 RESOLVED-BY · 4 SUPERSEDED | — | — |  |
| 321 | `audits/06_FA_audit.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | 0/0/1 | 90.8 | FA | 58 RESOLVED-BY · 11 SUPERSEDED · 4 STALE/FALSE-POS | — | — |  |
| 322 | `audits/06_FA_audit_addendum_B.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | 1/0/0 | 65.3 | FA | 24 RESOLVED-BY · 2 SUPERSEDED | — | — |  |
| 323 | `audits/07_SE_audit.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | 0/0/1 | 73.1 | SE | 37 RESOLVED-BY · 7 SUPERSEDED · 1 STALE/FALSE-POS · 1 DISPUTED | — | — |  |
| 324 | `audits/07_SE_audit_addendum_B.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | 1/0/1 | 63.2 | SE | 17 RESOLVED-BY · 1 SUPERSEDED | — | — |  |
| 325 | `audits/08_FI_audit.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | 0/0/2 | 99.5 | FI | 44 RESOLVED-BY · 3 SUPERSEDED · 1 STALE/FALSE-POS · 2 DISPUTED | — | — |  |
| 326 | `audits/08_FI_audit_addendum_B.md` | REFERENCE-AUDIT | REFERENCE (an audit addendum; resolves nothing at runtime) | 0/0/1 | 53.4 | FI | 35 RESOLVED-BY · 1 SUPERSEDED · 2 STALE/FALSE-POS | — | — |  |
| 327 | `audits/09_WR_audit.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | — | 85.4 | WR | 35 RESOLVED-BY · 7 SUPERSEDED · 2 STALE/FALSE-POS | — | — |  |
| 328 | `audits/09_WR_audit_addendum_B.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | — | 102.3 | WR | 23 RESOLVED-BY · 1 SUPERSEDED · 1 STALE/FALSE-POS | — | — |  |
| 329 | `audits/10_DICE_audit.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | 0/0/1 | 82.6 | DICE | 11 RESOLVED-BY · 3 SUPERSEDED | — | — |  |
| 330 | `audits/10_DICE_audit_addendum_B.md` | REFERENCE-AUDIT | REFERENCE (an audit addendum; resolves nothing at runtime) | — | 53.7 | DICE | 11 RESOLVED-BY · 7 SUPERSEDED | — | — |  |
| 331 | `audits/11_GO_audit.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | — | 79.4 | GO | 27 RESOLVED-BY · 6 SUPERSEDED · 2 STALE/FALSE-POS | — | — |  |
| 332 | `audits/11_GO_audit_addendum_B.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | 0/0/1 | 57.4 | GO | 10 RESOLVED-BY · 2 SUPERSEDED | — | — |  |
| 333 | `audits/12_ARCS_adjudication.md` | REFERENCE-AUDIT | REFERENCE (an adjudication; resolves nothing at runtime) | — | 94.0 | ARCS | 20 RESOLVED-BY · 9 SUPERSEDED | — | — |  |
| 334 | `audits/13_SC_contest_interrogation.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | 0/0/1 | 38.1 | SC | 19 RESOLVED-BY · 1 SUPERSEDED · 1 STALE/FALSE-POS · 2 DISPUTED | — | — |  |
| 335 | `audits/14_VERBS_BINDING.md` | REFERENCE-AUDIT | REFERENCE (a verb build-out audit under VERBS_BRIEF.md; res… | — | 58.0 | VERBS | 14 RESOLVED-BY · 1 SUPERSEDED | — | — |  |
| 336 | `audits/14_VERBS_MATERIAL.md` | REFERENCE-AUDIT | REFERENCE (a verb build-out audit under VERBS_BRIEF.md; res… | — | 69.6 | VERBS | 18 RESOLVED-BY · 2 SUPERSEDED · 1 DISPUTED | — | — |  |
| 337 | `audits/14_VERBS_MILITARY.md` | REFERENCE-AUDIT | REFERENCE (a verb build-out audit; resolves nothing at runt… | 0/0/1 | 47.1 | VERBS | 23 RESOLVED-BY · 9 SUPERSEDED · 1 DISPUTED | — | — |  |
| 338 | `audits/14_VERBS_PHYSICAL.md` | REFERENCE-AUDIT | REFERENCE (a verb build-out audit; resolves nothing at runt… | 0/0/1 | 86.7 | VERBS | 25 RESOLVED-BY · 4 SUPERSEDED | — | — |  |
| 339 | `audits/14_VERBS_SOCIAL1.md` | REFERENCE-AUDIT | REFERENCE (a verb build-out audit under VERBS_BRIEF.md; res… | — | 72.2 | VERBS | 16 RESOLVED-BY · 1 SUPERSEDED | — | — |  |
| 340 | `audits/14_VERBS_SOCIAL2.md` | REFERENCE-AUDIT | REFERENCE (a verb build-out audit; resolves nothing at runt… | — | 55.3 | VERBS | 13 RESOLVED-BY | — | — |  |
| 341 | `audits/15_INSTITUTIONS_BYZANTINE.md` | REFERENCE-AUDIT | REFERENCE (a design and plan in proposal form under INSTITU… | 1/0/1 | 112.2 | INSTITUTIONS | 14 RESOLVED-BY · 6 SUPERSEDED | — | — |  |
| 342 | `audits/15_INSTITUTIONS_COLONIAL.md` | REFERENCE-AUDIT | REFERENCE (a design and plan in proposal form; resolves not… | 1/0/1 | 120.9 | INSTITUTIONS | 14 RESOLVED-BY · 6 SUPERSEDED | — | — |  |
| 343 | `audits/15_INSTITUTIONS_PAPACY.md` | REFERENCE-AUDIT | REFERENCE (a design and plan in proposal form; resolves not… | 1/0/1 | 123.9 | INSTITUTIONS | 14 RESOLVED-BY · 6 SUPERSEDED | — | — |  |
| 344 | `audits/15_INSTITUTIONS_SYNTHESIS.md` | REFERENCE-AUDIT | REFERENCE (a design and plan in proposal form under INSTITU… | — | 144.2 | INSTITUTIONS | 9 RESOLVED-BY · 11 SUPERSEDED · 1 DISPUTED | — | — |  |
| 345 | `audits/15_INSTITUTIONS_VENICE.md` | REFERENCE-AUDIT | REFERENCE (a design and plan in proposal form; resolves not… | 1/0/1 | 131.9 | INSTITUTIONS | 14 RESOLVED-BY · 6 SUPERSEDED | — | — |  |
| 346 | `audits/16_PESSIMIST_CHAR.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | 0/0/1 | 50.9 | PESSIMIST | 17 RESOLVED-BY · 3 SUPERSEDED | — | — |  |
| 347 | `audits/16_PESSIMIST_CORE.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | — | 48.2 | PESSIMIST | 19 RESOLVED-BY · 3 SUPERSEDED · 2 STALE/FALSE-POS | — | — |  |
| 348 | `audits/16_PESSIMIST_DICE.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | — | 59.8 | PESSIMIST | 7 RESOLVED-BY · 5 SUPERSEDED · 2 JORDAN | — | — |  |
| 349 | `audits/16_PESSIMIST_FA.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | — | 65.1 | PESSIMIST | 13 RESOLVED-BY · 1 SUPERSEDED | — | — |  |
| 350 | `audits/16_PESSIMIST_FI.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | — | 79.7 | PESSIMIST | 16 RESOLVED-BY · 1 SUPERSEDED | — | — |  |
| 351 | `audits/16_PESSIMIST_GAME.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | — | 56.7 | PESSIMIST | 15 RESOLVED-BY · 11 SUPERSEDED | — | — |  |
| 352 | `audits/16_PESSIMIST_GO.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | — | 53.0 | PESSIMIST | 14 RESOLVED-BY · 1 SUPERSEDED | — | — |  |
| 353 | `audits/16_PESSIMIST_MB.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | — | 70.2 | PESSIMIST | 18 RESOLVED-BY · 5 SUPERSEDED | — | — |  |
| 354 | `audits/16_PESSIMIST_PC.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | 0/0/1 | 67.3 | PESSIMIST | 24 RESOLVED-BY · 7 SUPERSEDED | — | — |  |
| 355 | `audits/16_PESSIMIST_SC.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | — | 65.3 | PESSIMIST | 26 RESOLVED-BY · 1 STALE/FALSE-POS | — | — |  |
| 356 | `audits/16_PESSIMIST_SE.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | 0/0/1 | 67.2 | PESSIMIST | 18 RESOLVED-BY · 3 SUPERSEDED | — | — |  |
| 357 | `audits/16_PESSIMIST_WR.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | — | 49.1 | PESSIMIST | 13 RESOLVED-BY · 1 SUPERSEDED | — | — |  |
| 358 | `audits/17_CENSUS_C1A.md` | REFERENCE-AUDIT | REFERENCE (a census verdict; resolves nothing at runtime) | — | 54.1 | CENSUS | 8 RESOLVED-BY · 4 SUPERSEDED · 2 STALE/FALSE-POS | — | — |  |
| 359 | `audits/17_CENSUS_C1B.md` | REFERENCE-AUDIT | REFERENCE (a census lane's audit; resolves nothing at runti… | — | 124.9 | CENSUS | 14 RESOLVED-BY · 4 SUPERSEDED · 2 STALE/FALSE-POS | — | — |  |
| 360 | `audits/17_CENSUS_REST.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | — | 52.9 | CENSUS | 34 RESOLVED-BY · 24 SUPERSEDED · 16 STALE/FALSE-POS · 1 JORDAN | — | — |  |
| 361 | `audits/18_DETERMINISM_SWEEP.md` | REFERENCE-AUDIT | REFERENCE — a terminal sweep (CLAUDE.md §0, the RULED excep… | — | 19.1 | DETERMINISM | 22 RESOLVED-BY · 7 SUPERSEDED · 1 DISPUTED · 1 JORDAN | — | — |  |
| 362 | `audits/19_LACUNA_investigation_to_proceedings.md` | REFERENCE-AUDIT | REFERENCE (a precedent-and-design lane; resolves nothing at… | 0/0/2 | 41.9 | LACUNA | 18 RESOLVED-BY | — | — |  |
| 363 | `audits/20_NARRATIVE_CHURN.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime) | — | 72.8 | NARRATIVE | 20 RESOLVED-BY · 3 SUPERSEDED | — | — |  |
| 364 | `audits/21_PROCEDURAL_GENERATION.md` | REFERENCE-AUDIT | REFERENCE (a design audit and plan; resolves nothing at run… | 0/0/2 | 81.1 | PROCEDURAL | 11 RESOLVED-BY · 7 SUPERSEDED | — | — |  |
| 365 | `audits/22_HAPPENINGS.md` | REFERENCE-AUDIT | REFERENCE (an audit; resolves nothing at runtime; proposals… | 0/0/1 | 36.7 | HAPPENINGS | 15 RESOLVED-BY · 9 SUPERSEDED | — | — |  |
| 366 | `audits/23_STORY_ENABLEMENT.md` | REFERENCE-AUDIT | REFERENCE (a planning lane; resolves nothing at runtime, CL… | — | 116.2 | STORY | 23 RESOLVED-BY · 8 SUPERSEDED · 1 JORDAN | — | — |  |
| 367 | `audits/24_GROUNDING_GAMES.md` | REFERENCE-AUDIT | REFERENCE (a grounding pass over documents that already exi… | — | 36.4 | GROUNDING | no closure table | — | — |  |
| 368 | `audits/25_GROUNDING_ENGINE.md` | REFERENCE-AUDIT | REFERENCE (a grounding pass over documents that already exi… | — | 48.2 | GROUNDING | no closure table | — | — |  |
| 369 | `audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md` | REFERENCE-AUDIT | REFERENCE (an adjudication; resolves nothing at runtime, CL… | 0/1/0 | 37.4 | MASS | no closure table | — | — |  |
| 370 | `audits/27_MB_COMMAND_AND_DYNAMIC_STRENGTH.md` | REFERENCE-AUDIT | REFERENCE (a design adjudication serving rulings A-59 and A… | 0/1/0 | 34.2 | MB | no closure table | — | — |  |
| 371 | `audits/28_SCENE_ACCESS.md` | REFERENCE-AUDIT | REFERENCE (an audit and a plan for future execution; resolv… | — | 38.7 | SCENE | no closure table | — | — |  |
| 372 | `audits/29_ONE_OPPOSED_RULE.md` | REFERENCE-AUDIT | REFERENCE (a design audit with measurements; resolves nothi… | — | 36.5 | ONE | no closure table | — | — |  |
| 373 | `audits/30_ERAS_REGIMES_STRIFE_AND_MOMENTUM.md` | REFERENCE-AUDIT | REFERENCE (an audit and a plan; resolves nothing at runtime… | — | 41.6 | ERAS | no closure table | — | — |  |
| 374 | `audits/31_HOUSE_STANCES_AND_CAST_VALUES.md` | REFERENCE-AUDIT | REFERENCE (an audit and a plan; resolves nothing at runtime… | — | 19.9 | HOUSE | no closure table | — | — |  |
| 375 | `census/C1_unreferenced_symbols.md` | REFERENCE-AUDIT | (no Status line; leads list) | — | 82.5 | census | closure: U5a 4.1-4.2 | — | — |  |
| 376 | `census/C2_record_fields.md` | REFERENCE-AUDIT | (no Status line; leads list) | — | 9.8 | census | closure: U5_FINDINGS_CLOSURE_U5a Part 4.3 (C2-C6); C1 in 4.1-4.2 | — | — |  |
| 377 | `census/C3_registry_keys_no_code_names.md` | REFERENCE-AUDIT | (no Status line; leads list) | — | 1.1 | census | closure: U5_FINDINGS_CLOSURE_U5a Part 4.3 (C2-C6); C1 in 4.1-4.2 | — | — |  |
| 378 | `census/C4_event_kinds_emitted_without_consumer.md` | REFERENCE-AUDIT | (no Status line; leads list) | — | 0.3 | census | closure: U5_FINDINGS_CLOSURE_U5a Part 4.3 (C2-C6); C1 in 4.1-4.2 | — | — |  |
| 379 | `census/C5_hole_register_stale_pointers.md` | REFERENCE-AUDIT | (no Status line; leads list) | — | 2.1 | census | closure: U5_FINDINGS_CLOSURE_U5a Part 4.3 (C2-C6); C1 in 4.1-4.2 | — | — |  |
| 380 | `census/C6_composition_targets_that_do_not_resolve.md` | REFERENCE-AUDIT | (no Status line; leads list) | — | 0.1 | census | closure: U5_FINDINGS_CLOSURE_U5a Part 4.3 (C2-C6); C1 in 4.1-4.2 | — | — |  |
| 381 | `digests/DG_audit1.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 122.7 | digest | — | — | — |  |
| 382 | `digests/DG_audit2.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 105.4 | digest | — | — | — |  |
| 383 | `digests/DG_auditB1.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 65.1 | digest | — | — | — |  |
| 384 | `digests/DG_auditB2.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 89.9 | digest | — | — | — |  |
| 385 | `digests/DG_auditB3.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 32.1 | digest | — | — | — |  |
| 386 | `digests/DG_auditB4.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 140.3 | digest | — | — | — |  |
| 387 | `digests/DG_auditB5.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 97.3 | digest | — | — | — |  |
| 388 | `digests/DG_canon_arch1.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 126.0 | digest | — | — | — |  |
| 389 | `digests/DG_designs1.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 177.7 | digest | — | — | — |  |
| 390 | `digests/DG_designs2.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 140.5 | digest | — | — | — |  |
| 391 | `digests/DG_designs_rest.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 52.8 | digest | — | — | — |  |
| 392 | `digests/DG_engine1.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 71.9 | digest | — | — | — |  |
| 393 | `digests/DG_engine2.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 49.3 | digest | — | — | — |  |
| 394 | `digests/DG_modsys1.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 64.2 | digest | — | — | — |  |
| 395 | `digests/DG_modsys2.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 94.3 | digest | — | — | — |  |
| 396 | `digests/DG_modsys3.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 27.6 | digest | — | — | — |  |
| 397 | `digests/DG_proposalsB1.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 70.5 | digest | — | — | — |  |
| 398 | `digests/DG_proposalsB10.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 35.9 | digest | — | — | — |  |
| 399 | `digests/DG_proposalsB2.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 80.9 | digest | — | — | — |  |
| 400 | `digests/DG_proposalsB4.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 73.9 | digest | — | — | — |  |
| 401 | `digests/DG_proposalsB5.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 93.2 | digest | — | — | — |  |
| 402 | `digests/DG_proposalsB6.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 169.8 | digest | — | — | — |  |
| 403 | `digests/DG_proposalsB7.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 100.6 | digest | — | — | — |  |
| 404 | `digests/DG_proposalsB8.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 74.5 | digest | — | — | — |  |
| 405 | `digests/DG_proposalsB9.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 72.4 | digest | — | — | — |  |
| 406 | `digests/DG_proposals_old_heads.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 137.0 | digest | — | — | — |  |
| 407 | `digests/DG_proposals_recent1.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 117.3 | digest | — | — | — |  |
| 408 | `digests/DG_proposals_recent2.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 132.9 | digest | — | — | — |  |
| 409 | `digests/DG_proposals_recent3.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 119.4 | digest | — | — | — |  |
| 410 | `digests/DG_proposals_recent4.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 141.6 | digest | — | — | — |  |
| 411 | `digests/DG_refs1.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 96.9 | digest | — | — | — |  |
| 412 | `digests/DG_refs2.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 39.9 | digest | — | — | — |  |
| 413 | `digests/DG_register.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 122.7 | digest | — | — | — |  |
| 414 | `digests/DG_registers_refs2.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 120.6 | digest | — | — | — |  |
| 415 | `digests/DG_research1.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 142.2 | digest | — | — | — |  |
| 416 | `digests/DG_research2.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 79.3 | digest | — | — | — |  |
| 417 | `digests/DG_research3.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 80.2 | digest | — | — | — |  |
| 418 | `digests/DG_research4.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 34.0 | digest | — | — | — |  |
| 419 | `digests/DG_researchB1.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 65.6 | digest | — | — | — |  |
| 420 | `digests/DG_researchB2.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 79.0 | digest | — | — | — |  |
| 421 | `digests/DG_researchB3.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 45.2 | digest | — | — | — |  |
| 422 | `digests/DG_research_rest1.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 86.1 | digest | — | — | — |  |
| 423 | `digests/DG_tests1.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 161.5 | digest | — | — | — |  |
| 424 | `digests/DG_tests2.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 102.4 | digest | — | — | — |  |
| 425 | `digests/DG_tests3.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 47.2 | digest | — | — | — |  |
| 426 | `digests/DG_tests4.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 95.1 | digest | — | — | — |  |
| 427 | `digests/DG_tests5.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 124.6 | digest | — | — | — |  |
| 428 | `digests/DG_tests6.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 159.6 | digest | — | — | — |  |
| 429 | `digests/DG_tools.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 101.0 | digest | — | — | — |  |
| 430 | `digests/DG_workplan1.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 61.0 | digest | — | — | — |  |
| 431 | `digests/DG_workplan2.md` | DIGEST | REFERENCE (a coverage digest; resolves nothing at runtime) | — | 88.6 | digest | — | — | — |  |
| 432 | `dossiers/00_NINE.md` | DIGEST | (no Status line; built by script from the tree) | — | 13.3 | dossier | — | — | — |  |
| 433 | `dossiers/01_CORE.md` | DIGEST | (no Status line; built by script from the tree) | — | 68.2 | dossier | — | — | — |  |
| 434 | `dossiers/02_CHAR.md` | DIGEST | (no Status line; built by script from the tree) | — | 94.5 | dossier | — | — | — |  |
| 435 | `dossiers/03_PC.md` | DIGEST | (no Status line; built by script from the tree) | — | 37.6 | dossier | — | — | — |  |
| 436 | `dossiers/04_MB.md` | DIGEST | (no Status line; built by script from the tree) | — | 30.4 | dossier | — | — | — |  |
| 437 | `dossiers/05_SC.md` | DIGEST | (no Status line; built by script from the tree) | — | 42.3 | dossier | — | — | — |  |
| 438 | `dossiers/06_FA.md` | DIGEST | (no Status line; built by script from the tree) | — | 41.7 | dossier | — | — | — |  |
| 439 | `dossiers/07_SE.md` | DIGEST | (no Status line; built by script from the tree) | — | 35.0 | dossier | — | — | — |  |
| 440 | `dossiers/08_FI.md` | DIGEST | (no Status line; built by script from the tree) | — | 60.8 | dossier | — | — | — |  |
| 441 | `dossiers/09_WR.md` | DIGEST | (no Status line; built by script from the tree) | — | 77.6 | dossier | — | — | — |  |
| 442 | `dossiers/10_DICE.md` | DIGEST | (no Status line; built by script from the tree) | — | 15.2 | dossier | — | — | — |  |
| 443 | `dossiers/11_GO.md` | DIGEST | (no Status line; built by script from the tree) | — | 9.4 | dossier | — | — | — |  |
| 444 | `dossiers/99_cross_cutting.md` | DIGEST | (no Status line; built by script from the tree) | — | 28.7 | dossier | — | — | — |  |
| 445 | `unified/DECISIONS_ANSWERED.md` | REFERENCE | RECORD (Jordan's answers, 2026-11-12; reference, resolves n… | — | 50.2 | unified | — | — | — |  |
| 446 | `unified/DECISIONS_FOR_JORDAN.md` | REFERENCE | REFERENCE (a decision register for the suite; resolves noth… | — | 109.6 | unified | — | — | — |  |
| 447 | `unified/DECISIONS_QUICKSHEET.md` | REFERENCE | REFERENCE (companion to DECISIONS_FOR_JORDAN.md; resolves n… | — | 7.9 | unified | — | — | — |  |
| 448 | `unified/OWED_TO_UNIFICATION.md` | WORK-ORDER | WORK LIST (a register of items other lanes reported as owed… | — | 11.5 | unified | — | — | — |  |
| 449 | `unified/RESEARCH_MAP_INSTITUTIONS_A.md` | REFERENCE | REFERENCE (a map of what the tree's own research holds; res… | — | 31.4 | unified | — | — | — |  |
| 450 | `unified/RESEARCH_MAP_INSTITUTIONS_B.md` | REFERENCE | REFERENCE (a map of what the tree's own research holds; res… | — | 50.4 | unified | — | — | — |  |
| 451 | `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` | REFERENCE | REFERENCE (the suite's one decision on how a capability is … | 1/0/0 | 47.4 | unified | — | — | — |  |
| 452 | `unified/U1_GLOSSARY.md` | REFERENCE | REFERENCE (vocabulary for the suite's documents and the cod… | — | 31.2 | unified | — | — | — |  |
| 453 | `unified/U1_JORDAN_CALLS.md` | REFERENCE | REFERENCE (a list for Jordan; resolves nothing at runtime, … | — | 3.2 | unified | — | — | — |  |
| 454 | `unified/U1_OWNERS_AND_VOCABULARY.md` | REFERENCE | REFERENCE (a unification-lane ledger; a plan of ordered edi… | — | 72.1 | unified | — | — | — |  |
| 455 | `unified/U3_CONFLICT_LEDGER.md` | WORK-ORDER | WORK LEDGER (unification wave 2, lane U3; reference, resolv… | — | 80.9 | unified | — | — | — |  |
| 456 | `unified/U3_DEPENDENCY_ORDER.md` | WORK-ORDER | WORK LEDGER (unification wave 2, lane U3; the input to work… | — | 173.8 | unified | — | — | — |  |
| 457 | `unified/U3_JORDAN_CALLS.md` | REFERENCE | REFERENCE (a decision register for the suite, in the form o… | — | 9.4 | unified | — | — | — |  |
| 458 | `unified/U4_DOCUMENT_STATUS.md` | WORK-ORDER | WORK LEDGER (unification lane U4c, UNIFICATION_BRIEF.md lan… | — | 112.2 | unified | — | — | — | this file; size is as of the generating run |
| 459 | `unified/U4_FACT_CHECK.md` | WORK-ORDER | (not opened by this lane; written by a sibling U4 lane) | — | 40.9 | unified | — | — | — | output named by UNIFICATION_BRIEF.md lane U4 |
| 460 | `unified/U4_TRACEABILITY.md` | WORK-ORDER | (not opened by this lane; written by a sibling U4 lane) | — | 48.3 | unified | — | — | — | output named by UNIFICATION_BRIEF.md lane U4 |
| 461 | `unified/U5_CONFLICTS_U5a.md` | REFERENCE-AUDIT | REFERENCE (a closure record for the suite; resolves nothing… | — | 22.9 | unified | — | — | — |  |
| 462 | `unified/U5_CONFLICTS_U5c.md` | REFERENCE-AUDIT | REFERENCE (a conflict ledger for the suite; resolves nothin… | — | 18.4 | unified | — | — | — |  |
| 463 | `unified/U5_FINDINGS_CLOSURE_U5a.md` | REFERENCE-AUDIT | REFERENCE (a closure ledger for the suite; resolves nothing… | — | 118.0 | unified | — | — | — |  |
| 464 | `unified/U5_FINDINGS_CLOSURE_U5b.md` | REFERENCE-AUDIT | REFERENCE (a closure table for the suite; resolves nothing … | 1/0/0 | 80.8 | unified | — | — | — |  |
| 465 | `unified/U5_FINDINGS_CLOSURE_U5c.md` | REFERENCE-AUDIT | REFERENCE (a closure table for the suite; resolves nothing … | — | 74.2 | unified | — | — | — |  |
| 466 | `unified/U5_FINDINGS_CLOSURE_U5d.md` | REFERENCE-AUDIT | REFERENCE (a closure table for the suite; resolves nothing … | — | 118.8 | unified | — | — | — |  |
| 467 | `unified/UNIFICATION_RUN.md` | WORK-ORDER | WORK ORDER (the run plan for UNIFICATION_BRIEF.md; resolves… | — | 6.4 | unified | — | — | — |  |
| 468 | `unified/WAVE3_REWRITE_ORDER.md` | WORK-ORDER | WORK ORDER (applies UNIFICATION_BRIEF.md after waves 1 and … | — | 5.0 | unified | — | — | — |  |
| 469 | `unified/work/R1_READ.md` | WORK-ORDER | WORK FILE (R1 read lane output for unified/UNIFICATION_RUN.… | — | 178.8 | unified/work | — | — | — |  |
| 470 | `unified/work/R2_READ.md` | WORK-ORDER | WORK FILE (a read lane's extract for the unification stage;… | — | 156.5 | unified/work | — | — | — |  |
| 471 | `unified/work/R3_READ.md` | WORK-ORDER | WORK FILE (input to the Wave 2 and Wave 3 lanes of unified/… | — | 120.5 | unified/work | — | — | — |  |
| 472 | `unified/work/R4_READ.md` | WORK-ORDER | WORK (a read lane's extract for the unification stage; reso… | — | 162.8 | unified/work | — | — | — |  |
| 473 | `unified/work/R5_READ.md` | WORK-ORDER | WORK FILE (read lane R5 of unified/UNIFICATION_RUN.md; refe… | — | 311.7 | unified/work | — | — | — |  |
| 474 | `unified/work/W3_1_DONE.md` | WORK-ORDER | WORK FILE (progress record for unified/WAVE3_REWRITE_ORDER.… | — | 13.2 | unified/work | — | — | — |  |
| 475 | `unified/work/W3_2_DONE.md` | WORK-ORDER | WORK FILE (progress of wave-3 rewrite lane W3-2; resolves n… | — | 19.2 | unified/work | — | — | — |  |
| 476 | `unified/work/W3_3_DONE.md` | WORK-ORDER | WORK FILE (progress log of wave-3 lane W3-3; deleted when t… | — | 11.3 | unified/work | — | — | — |  |
| 477 | `unified/work/W3_4a_DONE.md` | WORK-ORDER | WORK (progress record of a wave-3 rewrite lane; resolves no… | — | 18.1 | unified/work | — | — | — |  |
| 478 | `unified/work/W3_4b_DONE.md` | WORK-ORDER | WORK (progress record of a wave-3 rewrite lane; resolves no… | — | 15.3 | unified/work | — | — | — |  |
| 479 | `unified/work/W3_5a_DONE.md` | WORK-ORDER | WORK FILE (wave-3 rewrite lane W3-5a; deleted when the stag… | — | 13.0 | unified/work | — | — | — |  |
| 480 | `unified/work/W3_5b_DONE.md` | WORK-ORDER | WORK FILE (progress record for unified/WAVE3_REWRITE_ORDER.… | — | 14.0 | unified/work | — | — | — |  |
| 481 | `unified/work/W3_MOPUP_DONE.md` | WORK-ORDER | WORK FILE (progress record of the wave-3 cross-lane mop-up;… | — | 10.4 | unified/work | — | — | — |  |
| 482 | `../../research/game_precedent_suite/grounding/bannerlord_encounter_menu.md` | REFERENCE | FILED — reference, not canon (CLAUDE.md §0.05) · tier 3 (re… | — | 3.9 | research | — | — | — |  |
| 483 | `../../research/game_precedent_suite/grounding/burning_wheel_and_griftlands.md` | REFERENCE | FILED — reference, not canon (CLAUDE.md §0.05) · tier 3 (re… | — | 5.8 | research | — | — | — |  |
| 484 | `../../research/game_precedent_suite/grounding/detective_set.md` | REFERENCE | FILED — reference, not canon (CLAUDE.md §0.05) · tier 3 (re… | — | 7.8 | research | — | — | — |  |
| 485 | `../../research/game_precedent_suite/grounding/football_manager_instant_result.md` | REFERENCE | FILED — reference, not canon (CLAUDE.md §0.05) · tier 3 (re… | — | 4.2 | research | — | — | — |  |
| 486 | `../../research/game_precedent_suite/grounding/hades_spelunky.md` | REFERENCE | FILED — reference, not canon (CLAUDE.md §0.05) · tier 3 (re… | — | 5.0 | research | — | — | — |  |
| 487 | `../../research/game_precedent_suite/grounding/lacuna.md` | REFERENCE | FILED — reference, not canon (CLAUDE.md §0.05) · tier 3 (re… | — | 7.2 | research | — | — | — |  |
| 488 | `../../research/game_precedent_suite/grounding/ogre_battle.md` | REFERENCE | FILED — reference, not canon (CLAUDE.md §0.05) · tier 3 (re… | — | 6.5 | research | — | — | — |  |
| 489 | `../../research/game_precedent_suite/grounding/paradise_killer.md` | REFERENCE | FILED — reference, not canon (CLAUDE.md §0.05) · tier 3 (re… | — | 4.4 | research | — | — | — |  |
| 490 | `../../research/game_precedent_suite/grounding/shadows_of_doubt_generation.md` | REFERENCE | FILED — reference, not canon (CLAUDE.md §0.05) · tier 3 (re… | — | 6.5 | research | — | — | — |  |
| 491 | `../../research/game_precedent_suite/grounding/sherlock_holmes_crimes_and_punishments.md` | REFERENCE | FILED — reference, not canon (CLAUDE.md §0.05) · tier 3 (re… | — | 4.4 | research | — | — | — |  |
| 492 | `../../research/game_precedent_suite/grounding/unicorn_overlord.md` | REFERENCE | FILED — reference, not canon (CLAUDE.md §0.05) · tier 3 (re… | — | 3.5 | research | — | — | — |  |
| 493 | `../../research/historical/mass_battle_casualties_and_results_grounding.md` | REFERENCE | FILED — reference, tier 3 (research/00_INDEX.md §1) · not c… | — | 19.8 | research | — | — | — |  |
| 494 | `../../research/historical/mass_battle_maneuver_sequences_grounding.md` | REFERENCE | FILED — reference, tier 3 (research/00_INDEX.md §1) · not c… | — | 21.5 | research | — | — | — |  |
| 495 | `../../research/historical/mass_battle_movement_and_behaviour_grounding.md` | REFERENCE | FILED — reference, tier 3 (research/00_INDEX.md §1) · not c… | — | 20.8 | research | — | — | — |  |
| 496 | `../../research/historical/mass_battle_wargame_models_grounding.md` | REFERENCE | FILED — reference, tier 3 (research/00_INDEX.md §1) · not c… | — | 13.3 | research | — | — | — |  |

## 5. Limits, stated once

- **Audits are read at heads and closure tables, not in full** (section 0). The audit tallies in section 4 count table rows under the audit's heading in the four closure files by script; a row that closes several ids counts once, and a row under a heading shared by several audits (the four institutions family audits, Part 7.2 of U5d) counts against each.
- **Audits 24 to 31 have no closure table** (`24_GROUNDING_GAMES`, `25_GROUNDING_ENGINE`, `26_MASS_BATTLE_HISTORICAL_ADJUDICATION`, `27_MB_COMMAND_AND_DYNAMIC_STRENGTH`, `28_SCENE_ACCESS`, `29_ONE_OPPOSED_RULE`, `30_ERAS_REGIMES_STRIFE_AND_MOMENTUM`, `31_HOUSE_STANCES_AND_CAST_VALUES`). U5b cites 24 to 27 by row only; 28 to 31 are not named in any `U5_*` file. Their resolutions live in their own proposals (`28_CORE_*`, `29_DICE_*`, `30_WR_*`, `30_GO_F`, `31_WR_*`) and in A-63 to A-93. Whether each of their findings has exactly one disposition (the closure rule) was not checked here.
- **The `closure` column for a proposal undercounts** where a closure row names its carrier by an abbreviation (OBS, CAP, PB, UPR, UMR, RES-V, FA-P1 and the like) and not by file name; 165 of 300 proposals show no row for that reason or because they carry no finding.
- **The census is a reading, not an execution** (CLAUDE.md §0.2). A COMPLETE proposal is one a batch can start from; whether its gate passes is the batch's. The sample in 3.2 is 12 of 246.
- **Two outputs of sibling lanes** (`unified/U4_TRACEABILITY.md`, `unified/U4_FACT_CHECK.md`) are listed by name and size and were not opened.
- **Research files**: only the 15 that the suite added under `research/` (found by `git log d015c93^..HEAD --diff-filter=A -- research`) are rows; the pre-existing research tree is not part of the suite.
- **The class REFERENCE is an addition** to the six classes the work order named; if the v12 stage wants six, fold REFERENCE into REFERENCE-AUDIT or DIGEST by file.

