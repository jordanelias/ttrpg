# Instruction suite — Sonnet check (stage 4 of `STAGES.md`)

## Status: REFERENCE (a record of one check of the eight instruction files; resolves nothing at runtime, CLAUDE.md §0.05; it dies with them when v12 is adopted)

Checked 2026-11-12 by the Sonnet check lane, tree `b07fc1c`-era working tree (HEAD `b06752e` at the end). One round. Read in full: `INSTRUCTION_SUITE_ORDER.md`, `IS_FOR_JORDAN.md`, all eight `IS_*` files; read in part: `unified/DECISIONS_ANSWERED.md` A-97 to A-101, `UNIFICATION_BRIEF.md` test 9, `unified/U3_DEPENDENCY_ORDER.md` §2.1 to §2.3, `unified/MB_LEXICON.md` (posts, formation), `STAGES.md`. `U1_GLOSSARY.md` was searched for the words A-98 and A-99 retire, not read whole. No pytest, no full suite. Two probes run: `len(SCALE_OF_RUNG)` (8) and `composition.json` role names. Line numbers below are as the files stood before this check's edits.

## 1. Counts

**Items audited: 75** (`Item:` headings: IS-A 13, IS-B1 11, IS-B2 29, IS-B3 22); the order's target of about 80 is met by counting 24 further pointer and blocked rows of IS-B1 (`IS-PC-P1..5`, `-B1..2`, `IS-MB-P1..7`, `-B1..4`, `IS-DICE-P1..5`, `-B1`), which carry no item form and are not tabulated. Fields: 11 per item, 825 cells (`CHAR-04` is a decision entry, 9 cells not applicable).

| reading | PRESENT | THIN | ABSENT | not applicable |
|---|---|---|---|---|
| as found | 731 | 51 | 34 | 9 |
| after this check's completions | 756 | 34 | 26 | 9 |

By field, as found → after (P / T / A): requirement or subsystem advanced 75/0/0 → same; INSTRUCTION 66/8/1; WHERE 60/7/7 → 61/7/6; FALSIFIER 65/1/8 → 67/0/7; GATE 69/5/0; hash movers 68/2/4 → 69/2/3; depends on 66/3/5 → 69/3/2; lane 74/0/0; batch 68/6/0 → 70/4/0; cost and tier 71/3/0; what lands it 49/16/9 → 65/2/7. **The one systematic gap was `what lands it`: 12 of IS-A's 13 items named no one** (completed once at the head of `IS_A_NINE_part2.md`). All 26 remaining ABSENT cells sit in seven items marked BLOCKED or POINTER-with-blocked-parts (`SC-06`, `SC-10`, `FI-02`, `FI-05`, `CORE-05`, `-06`, `-07`), each carrying a blocking reason and an owner in its own file (§4); the remaining THIN cells are `WHERE: no file` readings (`IS-PC-03`, `IS-MB-05`, `SC-09`, `FI-06`, `FA-03`), a gate whose reading is a baseline (`IS-A-07`), batch-by-milestone cells (`IS-A-08`, `-13`) and the blocked items' own.

**Tree checks.** About 125 paths and about 120 symbol, line or test-name citations were opened or grepped. Everything cited as EXISTS-IN-TREE exists at the cited line (sampled lines within 0 to 6 of the claim; `test_season_shape.py:15812` exact). Named files and symbols that do not exist were all declared new, PROPOSED or MISSING by their own item and belong to an earlier or same batch (listed per row below), **with these exceptions, defects D2, D13 and D15 in §3**: `PlayHost(deciders=…)` (used at B16, in the tree only at B34), `_mint_proposition` (described as existing). **Defects found 16, fixed 16** (§3); **left 8** (§4). **Collisions resolved 11** (§2).

## 2. Cross-lane collisions, and the decision by the five-step ladder (CLAUDE.md §0)

Line numbers: file and line as read before the edits. Edited files carry `Checked: 2026-11-12, Sonnet check` at their head (the four part 1 files, `IS_A_NINE_part2.md`, `IS_B2_SC_FI_CORE_CHAR_part2.md`, `IS_B1_PC_MB_DICE_part2.md`; the B3 part 2 file is covered by part 1's line).

| # | collision | where | decision (step) | edit |
|---|---|---|---|---|
| C1 | **Siege, twice.** `IS-A-09` and `IS-MB-02` both add `besiege` to `march_postures` at B22, both with a re-pin at B22's last item. `IS-A-09` assumed the wear is a draw and tested `…can_fail_to_wear_in_a_season`; the tree says it is not (`_siege` → `_fall`, a fixed fraction, `effects_economy.py:141`). | `IS_A_NINE_part2.md:215-245`; `IS_B1_PC_MB_DICE_part2.md:71-86` | Keep `IS-MB-02` (step 5: it is the complete item: roster precondition, A-81 repair, one formula owner, decision table). `IS-A-09` was itself marked `[If lane IS-B1 also carries the siege, v12 keeps one item]`. | `IS-A-09` rewritten as a POINTER with the tree reading; `IS-MB-02` step 5 records the tree reading (it stops unless B12 makes `_fall` a draw); `IS_A_NINE.md:224`, the G-1 row and the B22 map row repointed |
| C2 | **Cast content, two batches.** `IS-A-11` creates `BA1-cast-content` (gates nothing); `IS-B2-CHAR-03` creates `B10c-cast-content` (before B15, B19, B24). Same files, same mover, two handles, opposite edges. | `IS_A_NINE_part2.md:265-305`; `IS_B2_SC_FI_CORE_CHAR_part2.md:145-151, 186, 194, 207, 228` | Keep `BA1` (step 5: the fuller item, with the drafting stage and tables). The edge to B15, B19, B24 is **soft**: a hard edge puts three lanes on Jordan's corrections (the long pole), and the B2 item itself says dependent calibrations then name the control they ran at. | `B10c-cast-content` renamed everywhere in B2 part 2; `IS-A-11` states the merge and the soft edge; §5.1 table and edges reworded |
| C3 | **`null_scenes`, twice.** `IS-A-07` and `IS-B2-CORE-03` both land the function in `harness/storybar.py` at B02; CORE-03 also claimed to be the file's *first editor*, against the nine-gate proposal (C3-K7) and `IS-A-07`'s own order. | `IS_A_NINE_part2.md:176-194`; `IS_B2_SC_FI_CORE_CHAR_part2.md:68-74, 211` | `IS-A-07` owns it (step 4: the requirement lane; it is G-11's carry text). | `IS-B2-CORE-03` is a POINTER keeping only the per-close quotation and the scenario summary line; census row corrected |
| C4 | **R-07 and R-08 readings, twice.** `IS-A-05` and `IS-B2-CORE-04` write the same two tests in `test_realm_requirements.py` and the same printed line. | `IS_A_NINE_part2.md:116-142`; `IS_B2_SC_FI_CORE_CHAR_part2.md:76-81` | `IS-A-05` owns them (step 4). | `IS-B2-CORE-04` is a POINTER; §5.1 and §5.3 rows corrected |
| C5 | **Scenario registry bypassed.** `IS-B2-CORE-01` makes `scenarios.run` the one season loop (`IS_B2_…_part2.md:53`, rule (4)); `IS-B3-FA-01`, `-SE-01`, `-WR-02` register rows. `IS-PC-01` step 3 ran `SeasonDriver.season` itself; `IS-MB-01` and `IS-MB-04` (via the scenario proposal's `play`) built their own runners. | `IS_B1_PC_MB_DICE.md:96`; `IS_B1_PC_MB_DICE_part2.md:59-63, 104-111` | Register rows and call `run` (step 4: precedent, three sibling items already do). | `IS-PC-01`, `IS-MB-01`, `IS-MB-04` register `duel`, `field`, `squad`; WHERE and Depends lines and the B1 census gain the `scenarios.py` row |
| C6 | **Ending words: a dialect.** B1 returns `win | lose | draw | none`; `IS-B3-GO-01` closes `ENDING_KINDS = won | lost | drawn` and refuses a row without `kinds`. Four B2 rows (`season`, `life`, `inquiry`, `hearing`) stated none. | `IS_B1_PC_MB_DICE.md:97, 102`; `IS_B1_PC_MB_DICE_part2.md:61`; `IS_B2_…_part2.md` (CORE-02, CHAR-01); `IS_B2_….md` (FI-03, SC-08) | One closed set (shape divergence is forbidden, §10); GO-01 owns it (step 4). | B1 functions return the closed kinds; `kinds` stated for the four B2 rows (hearing carries an `[ASSUMPTION]` on the seat); `IS-B2-CORE-01` records GO-01's two fields |
| C7 | **Two deciders for one design.** `IS-MB-03` writes `choose.py::general_action_of` (choice score by `align_choice`, `_sample_order`); `IS-B2-CHAR-02` writes `decision/decider.py::make_decider` doing the same sum and pick, and both say they close `27_MB_D` 27D-4. A third, `approach_of` (PB step 4), is the same shape. | `IS_B1_PC_MB_DICE_part2.md:88-102`; `IS_B2_…_part2.md:135-143` | `make_decider` is the one owner (step 5: single-owner primitive, B10 lands before B20). | `IS-MB-03` calls it; `bias` added to its signature with a single-value test; `choose.py` dropped from MB-03's WHERE and the census; `approach_of` named a thin caller |
| C8 | **The realm scenario has two names.** `IS-B3-FA-01` registers `realm.governs`; `IS-B3-WR-02` (3a) registers `realm` (same builder, same world). | `IS_B3_FA_SE_WR_GO.md:94`; `IS_B3_…_part2.md:66` | One row, `realm`, registered once by the first batch that needs it (B21) (step 5). | FA-01 renamed and given `season_ending`; WR-02 (3a) reads it |
| C9 | **`test_play_surface.py` in two trees** (`tests/valoria/` per GO-B build order 1; `engine/season/tests/` per the fidelity proposal gate 3; B3 left it as 'merged or renamed at B34'). B2 cited the first. | `IS_B3_…_part2.md:133, 137, 270`; `IS_B2_…_part2.md:32` | `engine/season/tests/` (step 4: `test_aperture.py`, `test_storybar.py`, `test_rem30_*`, `test_rem31_*` all sit there; the module under test is `harness/play_surface.py`). | §6.1 decided in B3; S6 row and B2 CORE row repointed; `test_play_surface_own_outcome.py` beside it |
| C10 | **Verb-table denominator.** `IS-A-08` and R-05 list the rows that raise `n` (68 at B25, 69 at B38) and omit `weave`, `lock`, `mend`, `ward`, four rows `IS-B3-WR-01` adds at B35. | `IS_A_NINE_part2.md` IS-A-08 and §12.2 B35; `IS_B3_…_part2.md:56` | B35 joins the list (step 3: `IS-A-08`'s own rule, a row landed dark raises n). | IS-A-08 and the B35 map row |
| C11 | **Words.** The lexicon (A-95, A-99) renames the post `front` to `centre` and refuses bare 'formation'; `IS-MB-03` step 3 said `front` and 'the formation's post names'; `IS-MB-06` said 'broken-formation sentinel'. A-98 words (aptitude, talent, prowess of a person, bare 'score', 'capability' outside backticks): none found; 'company, battalion, regiment, banner, host (size word)': none. | `IS_B1_PC_MB_DICE_part2.md:94, 125` | Lexicon governs (step 1: a later ruling). | `centre` and 'army formation'; 'broken-unit-formation sentinel (the tree's comment says broken-formation)' |

**Checked and found consistent (no edit):** handle citations (all 75 defined; no item cited and undefined; every `Bnn-name` equals `U3` §2.1's; `B03a`, `B03c`, `B13` are the improvement proposal's and marked new there; `B10c` was the only unknown handle); batch order against `U3` §2.1 for the items' dependencies (B20 after B16, B30 after B24, B22 after B12, B34 after B24 hold); shared files: `harness/scenarios.py` (B11 → B21 → B12 → B16 → B20 → B34 → B35), `storybar.py` (nine-gate, `IS-A-03`, `IS-A-07`), `governance_spine.py` (B21 → B24 → B34), `requirements.yaml` `scales:` rows (B02 → B11 → B24); hash movers (one re-pin each at B11 notice flip, B21, B22, B24, B35, BA1; no two items re-pin one world twice in a batch); `IS-A-06` and `IS-B3-SE-03` both edit `aperture.report` in different batches (B02, B12), in order.

## 3. Defects, worst first (all fixed)

- **D1. A refuted assumption under a duplicated item (siege).** `IS-A-09` step 3 assumed the siege's wear is a draw and gated on a test (`…can_fail_to_wear_in_a_season`) that cannot pass at the tree: `_siege` reads `_fall`, a fixed fraction. Fixed by C1; the tree reading is now in `IS-MB-02` step 5 and `IS-A-09`.
- **D2. A symbol used before it exists, and a second loop.** `IS-PC-01` step 3 (B16) passed `PlayHost(persons=…, deciders={…})`; `PlayHost` has two fields, `persons` and `decide` (`queries/inputs.py:178`), and `deciders` is B34's change. Fixed: it uses `decide=`; the loop is `scenarios.run` (C5).
- **D3. Two batches for one content with opposite edges.** C2.
- **D4. A false order claim on a serial file.** `IS-B2-CORE-03` 'first editor' of `storybar.py` against the nine-gate proposal (`16_PESSIMIST_CORE_the_nine_gate…:16`, edits it first). C3.
- **D5. Duplicated tests at one file.** C4.
- **D6. A second season loop and a registry bypass in three B1 items.** C5.
- **D7. A dialect of ending words, and registry rows that `IS-B3-GO-01` would refuse.** C6.
- **D8. Two sampled deciders for one design.** C7.
- **D9. One scenario, two names.** C8.
- **D10. A test file in two trees.** C9.
- **D11. The wrong instrument in two gates.** `IS-B2-SC-01` and `IS-B2-FI-01` gate an edit of `requirements.yaml` on `register --check`, which reads the hole register only (`register.py:706-736`); the instrument is `register --requirements` (what the same items' controls already use). Fixed in both.
- **D12. A requirement denominator that omits four rows.** C10.
- **D13. Words against the lexicon.** C11 (`front`/`centre`; bare 'formation' twice).
- **D14. A proposed symbol described as existing.** `IS-B2-SC-07` named `_mint_proposition` as the minting site; it is `14_VERBS_SOCIAL2_B` §1's (PROPOSED, B25; not in `effects_information.py`). Labelled.
- **D15. Missing fields.** `what lands it` absent or implied in 12 IS-A items (one line at the head of `IS_A_NINE_part2.md`); `IS-A-12` had no hash-mover and no depends line (added); `IS-B2-CHAR-05` and `-06` lacked falsifier, depends and lands (added from B04/B05/B10/BA1 and CI-11, which the items already name).
- **D16. A stale statement of absence.** `IS_A_NINE_part2.md` §14 says the sibling files were not read and a duplicate is possible; marked stale where it stands.

## 4. Left, with the reason and who decides

- **A-100 and A-101 are not applied.** Both rulings (mass battle as an abstraction of personal combat, a fight as a sequence of rounds) post-date the instruction files. They touch `IS-MB-01`'s P-3 baseline, `IS-MB-06` (unit prowess arithmetic), `IS-MB-02`'s decision table and the round wording of `IS-PC-01` and `IS-PC-02`. DECISIONS_ANSWERED says `master/mb_abstraction/` and `master/pc_round/` list and apply the supersessions 'in a later pass'. Owner: those lanes; nothing here pre-empts them.
- **`IS-A-05` and R-08.c count different things.** R-08.c's text is the share of resolved acts whose chosen candidate was not rank 1; `IS-A-05` part 1 counts deliberations whose pick was not the leading candidate. They agree only when one deliberation yields one act. Owner: `IS-A-05`'s landing session, which opens `decision_spread.py:448-500` first (the item says so).
- **BLOCKED or FOR JORDAN items, each with its own reason and owner (not decidable from the repository):** `IS-B2-SC-06` (SE names the act), `-SC-10` and `-FI-02` (workplan v11 positions, `STAGES.md` step 5), `-FI-05` (design pass), `-CORE-05` two parts, `-CORE-06` (CR-07), `-CORE-07` (sites unopened), `-CHAR-03` (content, Jordan), `-CHAR-04` (`J-IS-B2-01`, Jordan); B1's blocked rows `IS-PC-B1/B2`, `IS-MB-B1..B4`, `IS-DICE-B1`.
- **v11 positions the items depend on** (`CP-T07-02`, `CP-T08-01`, `CP-T09-07/08`, `CR-61`, the B10-15 card): dispositioned by step 5, not here.
- **Line numbers drift.** Citations are of `b07fc1c` or `6e1ea91`; the code tree was unchanged between them (`git diff --name-only` of the engine trees was empty in two lanes' own checks, not re-run here). They go stale at the first batch that edits a file and at `B03a-prose` for all.
- **Tests named but not run.** No named test was run (none exists yet except those marked EXISTS). The expected readings are predictions; a gate whose expected reading is a baseline (`IS-A-07`) says so.
- **Not read.** `U1_GLOSSARY.md` beyond word searches; `U2`, `U4` beyond the cited gaps; the proposals the items point at, except lines opened for a named test (test names were grepped in the proposals: all found where an item says a proposal creates them); the glossary row-by-row against each coined word of the eight files.
- **Possible further collision not resolved.** Several items edit `engine/season/seam/wrappers/sigma.py` (CI-03 at B03, HEAR_B edit 6, `IS-B2-SC-03/-04`, `-05`); the census in IS-B2 §5.3 gives the order and B1's `IS-DICE-01` does not edit it; no conflict seen.

## 5. The table (as found; completions are marked)

Codes: P present, T thin (implied, partial or a reading without its object), A absent, N not applicable. Columns: ADV · INS · WHE · FAL · GAT · MOV · DEP · LAN · BAT · COS · LND = requirement/subsystem advanced · INSTRUCTION · WHERE · FALSIFIER · GATE · hash movers · depends on (EXISTS/PROPOSED/MISSING) · lane · batch · cost and tier · what lands it. The 'after' code is shown only where this check completed a field.

| item | as found | after | tree check (opened at this read) |
|---|---|---|---|
| `IS-A-01` | `PPPPPPPPPPP` | — | register.py check_requirements :631 ok; m1_acceptance row_nine_requirements :293 ok; two new test files absent, declared MISSING |
| `IS-A-02` | `PPPPPPPPPPT` | `PPPPPPPPPPP` | requirements.yaml ok; readings named are runs, not names |
| `IS-A-03` | `PPPPPPPPPPT` | `PPPPPPPPPPP` | storybar.py, test_storybar.py ok; state/ids.py draw_factory :49 ok; `--base-seed` is one int today (the item changes it) |
| `IS-A-04` | `PPPPPPPPPPT` | `PPPPPPPPPPP` | rosters.yaml scale_of_rung :292 ok; data/rosters.py SCALE_OF_RUNG :776 ok, `len` run: 8 (gate reading true); test_scale_of_rung.py ok |
| `IS-A-05` | `PPPPPPPPPPT` | `PPPPPPPPPPP` | decision_spread.py play_season :448, print_season :551 ok; Fixtures.sweep data/fixtures.py:89 ok; DEFAULT_FIXTURES is in fixtures.py:213 not decision_spread; owner of R-07/R-08 tests |
| `IS-A-06` | `PPPPPPPPPPT` | `PPPPPPPPPPP` | aperture `.via` absent (as claimed); corpus_run.attempts :817, data/verbs emits_at :363 / writes_at :401, carriers Receipt :209 ok; `--seeds` flag ok |
| `IS-A-07` | `PPPPTPPPPPT` | `PPPPTPPPPPP` | storybar ok; gate reading is a baseline, not a number (stated) |
| `IS-A-08` | `PPPPPPPPTPT` | `PPPPPPPPTPP` | rule; B35 thread rows added to the batch list |
| `IS-A-09` | `PPPPPPPPPPT` | `PPPPPPPPPPP` | now POINTER; rosters march_postures ok; _siege :686 ok; _fall :141 is a fixed fraction (assumption refuted) |
| `IS-A-10` | `PPPPPPPPPPT` | `PPPPPPPPPPP` | test_season_shape.py def at :15812 ok exactly; test_task_draw.py created by 18_DETERMINISM (proposal names it) |
| `IS-A-11` | `PPPPPPPPPPT` | `PPPPPPPPPPP` | populated.py cast_attributes :1016 ok; exporters ok; absorbs IS-B2-CHAR-03 |
| `IS-A-12` | `PPPPPAAPTPT` | `PPPPPPPPPPP` | no symbols |
| `IS-A-13` | `PPPPPPPPTPT` | `PPPPPPPPTPP` | no symbols; batch is per milestone (12.1) |
| `IS-PC-01` | `PPPPPPPPPPP` | — | populated.py:513-518 four writes ok; attributes.SPEC ok; world_q.kit_of :3484 ok; fight_endings :986 = felled/yielded/undecided ok; fight.py:55 ok; PlayHost has `persons`,`decide` only (inputs.py:178): `deciders` absent (FIXED); duel_scene.py absent (new) |
| `IS-PC-02` | `PPPPPPPPPPP` | — | test_squad_field.py absent, created by squad proposal; fight.round PROPOSED |
| `IS-PC-03` | `PPTPPPPPPPP` | — | aperture ENGINES block is CI-11 (PROPOSED) |
| `IS-PC-04` | `PPPPPPPPPPP` | — | four functions exist: duel_terms :231, invariants :1150 and :1295, strength_jobs :216 (loop :222) ok |
| `IS-MB-01` | `PPPPPPPPPPP` | — | field_scene.py absent (new); military_menu.menu :87, field_estimate :463, army_presets.install :66 ok; fixtures field_troops_per_weight :789 ok |
| `IS-MB-02` | `PPPPPPPPPPP` | — | rosters march_postures + restore precondition note ok; _siege :686, _fall :141 read (fixed fraction); verb_table siege.pressed not re-opened |
| `IS-MB-03` | `PPPPPPPPPPP` | — | choose.py _sample_order :322 ok; CHOICE_RANGES :1698 ok; combat.py:394-395 party test ok; seam/wrappers/mass_battle.py resolve :355 ok; window_responses absent (new) |
| `IS-MB-04` | `PPPPPPPPPPP` | — | test_squad_field.py absent (created by squad proposal) |
| `IS-MB-05` | `PPTPPPPPPPP` | — | role names mass_battle.resolve_field / .army / .army_order in composition.json ok |
| `IS-MB-06` | `PPPPPPPPPPP` | — | units.py base_combat_pool :2998, POOL_QUALITY_MODEL arm and formula ok; exchange.py subunit_combat_pool :77 ok; tools/ci_golden_modes_check.py ok |
| `IS-DICE-01` | `PPPPPPPPPPP` | — | roll.py:157, sigma_leverage band_odds :345 / record_odds :378, sigma.py odds_of :350 ok; scene.py absent (B34) |
| `IS-B2-SC-01` | `PPPPPPPPPPP` | — | GATE named `register --check`, which never reads requirements.yaml (register.py:706-736): FIXED |
| `IS-B2-SC-02` | `PPPPPPPPPPP` | — | effects_information _eff_open_case :367, _docket_item :196, _mint_document :205 ok; world_q DOCKET_* :218-238 ok; write_matrix DocketItem rows ok |
| `IS-B2-SC-03` | `PPPPPPPPPPP` | — | arrangements.yaml and data/arrangements.py exist; `rites:` and sigma.hearing_input absent (new) |
| `IS-B2-SC-04` | `PPPPPPPPPPP` | — | sigma.py hearing_input absent (PROPOSED) |
| `IS-B2-SC-05` | `PPPPPPPPPPP` | — | verb_table covenant row :300 ok |
| `IS-B2-SC-06` | `PTAAPPTPTPA` | — | BLOCKED (SE names the act); exchange row exists |
| `IS-B2-SC-07` | `PPPPPPPPPPP` | — | _mint_proposition absent in tree (PROPOSED by SOCIAL2_B): label FIXED; test_vm_s2_b_word.py created by SOCIAL2_B |
| `IS-B2-SC-08` | `PPPPPPPPPPP` | — | governance_spine.build :93 ok; hearing_ending / kinds added |
| `IS-B2-SC-09` | `PPTPPPPPPPP` | — | aperture ok; ENGINES PROPOSED |
| `IS-B2-SC-10` | `PAAATAPPTTA` | — | BLOCKED (DEP-v11, step 5) |
| `IS-B2-FI-01` | `PPPPPPPPPPP` | — | GATE named `register --check`: FIXED |
| `IS-B2-FI-02` | `PTTAPPPPPPA` | — | BLOCKED on step 5; v11 positions |
| `IS-B2-FI-03` | `PPPPPPPPPPP` | — | scenarios.py absent (new); sheet.chronicle :196, world_q.reach :1045 ok |
| `IS-B2-FI-04` | `PPPPPPPPPPP` | — | person_q.deed_doers :302 ok (module is person_q, not world_q); options.py `contradicts` absent, only private `_pair` :1491 (EVID_B proposes it, item says so) |
| `IS-B2-FI-05` | `PTAAPAAPPPA` | — | BLOCKED (design); operands_for :1259, held_record_claims :979, terms_sourced :2508 ok |
| `IS-B2-FI-06` | `PPTPPPPPPPT` | — | aperture ok |
| `IS-B2-CORE-01` | `PPPPPPPPPPP` | — | choose.make_chooser :488, probes.chooser :278, play_surface.dispatching_chooser :47, carry_on :61, populated.run :2048 (loop :2058-2066), sheet.take_ranked :166 ok |
| `IS-B2-CORE-02` | `PPPPPPPPPPP` | — | headless.build_world :51, world_q.endings_reached :2619 ok |
| `IS-B2-CORE-03` | `PPPPPPPPPPT` | `PPPPPPPPPPP` | now POINTER to IS-A-07; false storybar `first editor` claim removed |
| `IS-B2-CORE-04` | `PPPPPPPPPPT` | `PPPPPPPPPPP` | now POINTER to IS-A-05 |
| `IS-B2-CORE-05` | `PTAATTTPPTA` | — | BLOCKED parts; harness/access.py absent, created by 28A (proposal row 7) |
| `IS-B2-CORE-06` | `PTAATTPPPTA` | — | BLOCKED on CR-07 |
| `IS-B2-CORE-07` | `PTAATAAPPPA` | — | sites unopened by its own statement |
| `IS-B2-CHAR-01` | `PPPPPPPPPPP` | — | ambitions :2797, aim_state :2986, creation_sheet :88 ok; kinds added |
| `IS-B2-CHAR-02` | `PPPPPPPPPPP` | — | decider.py absent (new); _sample_order :322, odds_weight (choose.py), draw_factory :49 ok; npc_decider_roles absent (new); `bias` added |
| `IS-B2-CHAR-03` | `PTTPPPTPPPT` | — | BLOCKED (content, Jordan); now joins BA1 |
| `IS-B2-CHAR-04` | `PTNNNNNNNNN` | — | decision entry, J-IS-B2-01; no build |
| `IS-B2-CHAR-05` | `PPPTPPAPPPA` | `PPPPPPPPPPP` | descriptor_registry.yaml and export_descriptors.py exist |
| `IS-B2-CHAR-06` | `PPAAPPAPTPA` | `PPPPPPPPPPP` | readings only |
| `IS-B3-FA-01` | `PPPPPPPPPPP` | — | governance_spine.py: census :181, build :93 ok; play/offered/situation absent (PROPOSED, B21); `realm.governs` renamed `realm` |
| `IS-B3-FA-02` | `PPPPPPPPPPP` | — | `offered` absent in tree today (PROPOSED, B21) |
| `IS-B3-FA-03` | `PPTPPPPPPPP` | — | storybar flags --world / --null-scenes absent (PROPOSED) |
| `IS-B3-FA-04` | `PPPPPPPPPPP` | — | world_q.fields_in_reach absent (PROPOSED); state/gate.py CLAIM ok; march_occasions absent (new) |
| `IS-B3-FA-05` | `PPPPPPPPPPP` | — | verb_table dispatch :424 ok; _eff_dispatch absent (grep, as claimed); predicates dispatch ok; effects_migration._relocate :98 ok |
| `IS-B3-FA-06` | `PPPPPPPPPPP` | — | world_q writs_held :3234, vacancies :3121, questions_for :4031 ok; test_in61_succession.py ok |
| `IS-B3-SE-01` | `PPPPPPPPPPP` | — | valley.py absent (new); scarce.py exists |
| `IS-B3-SE-02` | `PPPPPPPPPPP` | — | reading |
| `IS-B3-SE-03` | `PPPPPPPPPPP` | — | populated.census :1996, hunger_by_settlement :2045 ok; composition.json has settlements.drawn_under and .fabric ok |
| `IS-B3-SE-04` | `PPPPPPPPPPP` | — | module_contracts.yaml domain_actions :522, DA_proposal :532/:980, accounting_phase :142 ok; 13 tools read module_contracts ok; ED-FA-0002 in the archive (6 hits) ok; requirements.yaml :171 note ok |
| `IS-B3-SE-05` | `PPPPPPPPPPP` | — | notice composer PROPOSED (B11); witness.py exists |
| `IS-B3-WR-01` | `PPPPPPPPPPP` | — | state/world.py :1301-1308 coherence guard ok; threadwork wrapper / modules/threadwork absent (as claimed); weave/lock/mend/ward rows absent (new) |
| `IS-B3-WR-02` | `PPPPPPPPPPP` | — | exercises.py holds readers only (need_sha :62, load :108) ok; `realm` row now FA-01's |
| `IS-B3-WR-03` | `PPPPPPPPPPP` | — | modules/threadwork absent (new) |
| `IS-B3-WR-04` | `PPPPPPPPPPP` | — | test_unknowable.py absent (new) |
| `IS-B3-WR-05` | `PPPPPPPPPPP` | — | data/files.py GEOGRAPHY_YAML :147 ok; geography yaml ok; test_in35_lattice_coupling.py ok |
| `IS-B3-GO-01` | `PPPPPPPPPPP` | — | composition ROLES; scenarios.py absent (B11) |
| `IS-B3-GO-02` | `PPPPPPPPPPP` | — | play_surface.py holds dispatching_chooser and carry_on only (as claimed) |
| `IS-B3-GO-03` | `PPPPPPPPPPP` | — | state/world.py ok; test_go07_canonical_digest.py ok |
| `IS-B3-GO-04` | `PPPPPPPPPPP` | — | reveal absent (PROPOSED, 30_GO_F); test_in27_endings.py ok |
| `IS-B3-GO-05` | `PPPPPPPPPPP` | — | tools/export_oracle_pins.py absent (new, B41) |
| `IS-B3-GO-06` | `PPPPPPPPPPP` | — | text item |

The check completed fields by Edit only where the tree or an existing proposal decides them (§2, §3 D15); the rest are marked in the items with a blocking reason and an owner.
