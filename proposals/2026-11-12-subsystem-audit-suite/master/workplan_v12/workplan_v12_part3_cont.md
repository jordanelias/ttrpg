# Workplan v12 — part 3, continued: batch B02-tests from item B02.23

## Status: PROPOSED (the continuation of a body part of workplan v12, split at an item boundary at the part cap; unratified input to `methodology-execute`'s 0.1 stop until Jordan adopts v12; resolves nothing at runtime, CLAUDE.md §0.05)

Batch B02-tests's block head (INVOCATION, GATE, REQUIREMENT, BATCH GATE, C(k), SERIAL EDGES, the position table) and items B02.01 to B02.22 are in the file before this one; the head's index maps each handle to its file. Words and paths as that file states.

### B02.23 — the fork test is named for the budget it runs · 01_CORE_tests_shipped_world_falsifiers row 3 · BUILD · HASH EQUAL
- SOURCE: `proposals/01_CORE_tests_shipped_world_falsifiers.md` row 3; closes F-TEST-06.
- ADVANCES: R-02 (its reading names the shipped-budget test, B02.22, in B02.38).
- INSTRUCTION: "Rename `test_wd_a_fork_changes_a_later_decision_at_the_shipped_default` to `…_at_two_slots`" (it runs `scene_budget 2 × interactions_per_scene 1`; the shipped budget is 5 × 3): the new name is `test_wd_a_fork_changes_a_later_decision_at_two_slots`. The row's second half ("R-02's `measured:` reading names row 2 as the shipped-budget test") lands in B02.38 as R-02.a's conjunct: `measured:` left the file in B02.13.
- WHERE: `engine/season/tests/test_season_shape.py` (the one test's name).
- TESTS: the renamed test, unchanged in body.
- FALSIFIER and CONTROL: a reference to the old name survives (`git grep -n "at_the_shipped_default"` → nothing). Control: the test passes before and after.
- GATE: `python -m pytest engine/season/tests/test_season_shape.py -q -k at_two_slots` → one test passes; `git grep -n "fork_changes_a_later_decision_at_the_shipped_default" -- engine tools tests` → nothing.
- HASH MOVERS: none.
- DEPENDS ON: V12 B02.12 (`test_season_shape.py`, serial).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, medium.
- LANDS IT: B02's producer; `Item: B02.23`, `[skip ci]`.

### B02.24 — the invariant sweep sees a played realm · 01_CORE_tests_shipped_world_falsifiers row 4 · BUILD · HASH EQUAL
- SOURCE: the same file, row 4 and "Falsifier" (row 4); closes F-TEST-07.
- ADVANCES: none of the nine as a conjunct; the eight invariants checked against a world with offices in it (`m1_acceptance` row 4's family).
- INSTRUCTION: "In `test_the_engine_is_clean_under_the_sweep`, add a second sweep over `populated.build_realm(s)` played one season, seeds 0–2, asserting `not r["violations"]` and `r["unexercised"] == []`. The `:55` assertion (`"offices" in r["unexercised"]`) stays as a statement about the headless world."
- WHERE: `tests/valoria/test_season_invariant_sweep.py` (`test_the_engine_is_clean_under_the_sweep`).
- TESTS: the added arm (readings at `main`, a comparison: 34 offices, 79 stance rows, 698 tenures built; 13,379 Events and 12,351 claims played; `unexercised == []`, 0 violations).
- FALSIFIER and CONTROL: "plant `w.offices["x"]` held twice in the played realm; the sweep must report it." Control: the headless arm's `unexercised` still names `offices`.
- GATE: `python -m pytest tests/valoria/test_season_invariant_sweep.py -q` → green with `unexercised == []` on the realm arm.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `tests/valoria/test_season_invariant_sweep.py::test_the_engine_is_clean_under_the_sweep`, `harness/populated.py::build_realm`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, high.
- LANDS IT: B02's producer; `Item: B02.24`, `[skip ci]`.

### B02.25 — three loops assert that they saw something · 01_CORE_tests_shipped_world_falsifiers row 5 · BUILD · HASH EQUAL
- SOURCE: the same file, row 5 and "Falsifier" (row 5); closes F-TEST-11.
- ADVANCES: none: test strength (§0.1 pt 2).
- INSTRUCTION: "`test_march.py`: both casualty tests assert `len(attackers) == 2` and that the fold's kinds include `("field.lost", "Lost")`, the two lines the valoria sibling already has. `test_content_operands.py`: count candidates carrying `to` and `assert carried >= 1000` (a floor two orders below today's 194,714, the form `test_in62…` uses for `checked`)."
- WHERE: `engine/season/tests/test_march.py` (`test_the_total_casualty_model_zeroes_the_losing_side`, `test_the_none_casualty_model_writes_stance_only`); `engine/season/tests/test_content_operands.py` (`test_no_writ_derived_operand_is_ever_a_raw_tuple`).
- TESTS: the three edited tests.
- FALSIFIER and CONTROL: "patch `world_q.mustered` to return `[]`; both `test_march` tests must now redden where today they are green." Control: both pass unpatched.
- GATE: `python -m pytest engine/season/tests/test_march.py -q -k casualty` → green; `python -m pytest engine/season/tests/test_content_operands.py -q` → green.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE the three tests named.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, high.
- LANDS IT: B02's producer; `Item: B02.25`, `[skip ci]`.

### B02.26 — a skip on an absent combat engine becomes a failure · 01_CORE_tests_shipped_world_falsifiers row 6, with U5a_tests_digest_additions §C · BUILD · HASH EQUAL
- SOURCE: the same file, row 6 and "Falsifier" (row 6); `proposals/U5a_tests_digest_additions.md` §C (code SITE; `IS-B2-CORE-07`); closes F-TEST-12.
- ADVANCES: none of the nine as a conjunct; the W-E family (a contested act's consequence differs by degree) cannot pass by skipping.
- INSTRUCTION:
  1. SITE (`IS-B2-CORE-07`): open each site and record what is found in the commit body.
  2. Row 6: "Every `pytest.skip(f"personal_combat engine unavailable: …")` becomes `pytest.fail(…)` (13 sites)": nine sites in `test_season_shape.py` (ten tests, through `_k1_combatants`), and in `test_combat_band_edges.py`, `test_cp_t03_04_arms.py`, `test_cr85_faculty_replaces_history.py`, `test_h206_a_death_at_matter_is_witnessed.py`.
  3. §C, copied: "T3 row 6's rule (a skip becomes `pytest.fail`) covers every skip conditioned on the combat engine's load, including the fixture forms it did not list: `test_combat_band_edges.py` (`engine_available`), `test_cp_t03_04_arms.py` (`_engine`), `test_cr85_faculty_replaces_history.py` (the autouse fixture), `test_h206_a_death_at_matter_is_witnessed.py:161-162`. Of the nine sites in `test_season_shape.py`, eight do not assert `load_error()` first; after the edit none needs to." (`tests/valoria/test_charge_momentum_impulse.py` is mass battle's: not edited here.)
- WHERE: `engine/season/tests/test_season_shape.py`, `test_combat_band_edges.py`, `test_cp_t03_04_arms.py`, `test_cr85_faculty_replaces_history.py`, `test_h206_a_death_at_matter_is_witnessed.py`.
- TESTS: the edited tests (no new names).
- FALSIFIER and CONTROL: "make `combat.engine()` return `None` in process; the W-E tests must fail, not skip." Control: with the engine loading they pass.
- GATE: `grep -n "engine unavailable" engine/season/tests/*.py` → no `pytest.skip` on those lines; `python -m pytest <each edited file> -q` → green, one file at a time.
- HASH MOVERS: none.
- DEPENDS ON: V12 B02.23 (`test_season_shape.py`, serial).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, high.
- LANDS IT: B02's producer; `Item: B02.26`, `[skip ci]`.

### B02.27 — the interactions-log finding is read off the shipped season · 01_CORE_tests_shipped_world_falsifiers row 7 · BUILD · HASH EQUAL
- SOURCE: the same file, row 7; closes F-TEST-07 (the revert half).
- ADVANCES: none: test strength.
- INSTRUCTION: "`test_interactions_log.py`: the finding fixture stops naming two persons and a reverted fight. `_assert_finding` selects the first audited row of the shipped season whose candidate was chosen and whose verb declares `contests:`, and asserts the same six fields against the world (`same_faction` equals `world_q`'s reading for that pair, the question's claim id is in the actor's ledger, the candidate is the act). The planted wrong-relation test keeps its shape on that row. `revert_cr87` leaves the file." (B02.01 kept `revert_cr87` for this file only; it is deleted here with its last caller.)
- WHERE: `engine/season/tests/test_interactions_log.py` (`_assert_finding`, `test_the_log_names_the_cardinals_fight_on_the_inquisitor`, `test_a_planted_wrong_relation_reading_is_seen`); the `revert_cr87` helper wherever it is defined, if this was its last caller.
- TESTS: the two edited tests; `assert checked >= 1` over the audited rows.
- FALSIFIER and CONTROL: the planted wrong-relation reading is not seen on the selected row. Control: the shipped row's six fields read equal to the world's.
- GATE: `python -m pytest engine/season/tests/test_interactions_log.py -q` → green; `git grep -n "revert_cr87" -- engine/season/tests` → no caller in this file.
- HASH MOVERS: none.
- DEPENDS ON: V12 B02.01 (left `revert_cr87` for this file).
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: B02's producer; `Item: B02.27`, `[skip ci]`.

### B02.28 — a self-plea and an accusation are two rows; R-06's test drops its revert · 01_CORE_tests_shipped_world_falsifiers row 8 · BUILD · HASH EQUAL
- SOURCE: the same file, row 8 ("`[UNVERIFIED: not built]`" in the source; the test's own comment names this keying as what lifts the revert); closes F-TEST-07 (R-06's revert).
- ADVANCES: R-06.d's instrument (`decision_spread`; the reading is B02.38's).
- INSTRUCTION: "`harness/decision_spread.py::read_decisions` keys a candidate on `(verb, subject, subject == actor)`, so a self-plea and an accusation are two rows; `test_in62_under_the_null…` drops `revert_cp_t05_02`, keeps `seen_null <= {"draw", "tiebreak"}`, and replaces `any("pursuit" …)` with a comparison against the null arm: the shipped reading attributes more tops to `pursuit` than the null arm does (the null's count is 0), at seeds 0, 1, 2."
- WHERE: `engine/season/harness/decision_spread.py` (`read_decisions`); `engine/season/tests/test_in62_decision_spread.py` (`test_in62_under_the_null_every_realm_top_is_draw_or_tiebreak_and_the_shipped_reading_is_not`).
- TESTS: the edited test; red before the keying edit if the revert is dropped first (the source's "not built": the producer drops the revert, reads the test, then keys, and records both readings).
- FALSIFIER and CONTROL: with the keying reverted the test without `revert_cp_t05_02` fails. Control: the null arm's `pursuit` count is 0 at each seed.
- GATE: `python -m pytest engine/season/tests/test_in62_decision_spread.py -q` → green at seeds 0, 1, 2; `PYTHONHASHSEED=0 python -m engine.season.harness.decision_spread --decisions` → prints, with self-pleas and accusations on separate rows (an instrument table; no world moves).
- HASH MOVERS: none (an instrument's table).
- DEPENDS ON: V12 B02.26 (placed after it; no data edge); EXISTS-IN-TREE `harness/decision_spread.py::read_decisions`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: B02's producer; `Item: B02.28`, `[skip ci]`.

### B02.29 — the different-seed test cannot pass on an empty season · 01_CORE_tests_shipped_world_falsifiers row 9 · BUILD · HASH EQUAL
- SOURCE: the same file, row 9; closes F-TEST-12 (the escape hatch).
- ADVANCES: none: test strength.
- INSTRUCTION: "`test_a_different_seed_can_diverge…`: assert `fixed.events > 0` first, then the inequality with no `or`."
- WHERE: `tests/valoria/test_m1_acceptance_probe.py` (`test_a_different_seed_can_diverge_from_the_probe_seed`).
- TESTS: the edited test.
- FALSIFIER and CONTROL: a season with no Events passes the test (it must fail). Control: the test passes on the shipped probe.
- GATE: `python -m pytest tests/valoria/test_m1_acceptance_probe.py -q` → green.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE the test.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, medium.
- LANDS IT: B02's producer; `Item: B02.29`, `[skip ci]`.

### B02.30 — a fixture that reverted three shipped changes plays the shipped tree · U5a_tests_digest_additions §D1 · BUILD · HASH EQUAL
- SOURCE: `proposals/U5a_tests_digest_additions.md` §D row D1 (code SITE; `IS-B2-CORE-07`). The source's "Lands in batch" line names §A–§C, §E, §F, §D2 for B02 and is silent on D1; placed here, with the row-7 and row-8 edits it extends ("Fixtures that revert shipped changes beyond T3 rows 7–8"), `UNDECIDED` in this part's receipt.
- ADVANCES: none of the nine as a conjunct; the grid suspension observed at the shipped configuration.
- INSTRUCTION:
  1. SITE: open `engine/season/tests/test_rem31_grid_suspension.py` and record its autouse fixture in the commit body.
  2. Copied: "drop the three reverts; build the fight as a hand-built `fight` act folded on the shipped `build_realm(0)`, the form `test_combat_module.py` uses. The suspension is then observed at the shipped configuration. If a hand-built fight cannot reach ENCOUNTER on the shipped tree, that is a finding for `11_GO_player_surface_contract_B.md` §8's host, and the file keeps one revert, named in the commit."
- WHERE: `engine/season/tests/test_rem31_grid_suspension.py` (the autouse fixture reverting CR-87, CR-85 and CP-T03-04).
- TESTS: the file's tests on the new fixture.
- FALSIFIER and CONTROL: the hand-built fight does not reach ENCOUNTER (then the second branch applies). Control: the suspension tests pass with the reverts before the edit.
- GATE: `python -m pytest engine/season/tests/test_rem31_grid_suspension.py -q` → green; `grep -n "revert_" engine/season/tests/test_rem31_grid_suspension.py` → nothing, or one revert named in the commit body (the second branch).
- HASH MOVERS: none.
- DEPENDS ON: V12 B02.27 (placed after it); EXISTS-IN-TREE `engine/season/tests/test_combat_module.py` (the hand-built fight's form).
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: B02's producer; `Item: B02.30`, `[skip ci]`.

### B02.31 — each scale of play names its conjunct; the stale line about the scale words goes · IS-A-04 · BUILD · HASH EQUAL
- SOURCE: `master/instructions/IS_A_NINE_part2.md` `IS-A-04`; `IS_A_NINE.md` §5 ("Not a conjunct, and why"); closes `U4_TRACEABILITY.md` G-2 as stale.
- ADVANCES: R-04.c1 to c7.
- INSTRUCTION (copied): "`engine/season/requirements.yaml`, `scales:` block (which `01_CORE_requirements_reading_record` leaves untouched): (1) each of the seven rows gains `conjunct: R-04.cN` and loses nothing; its `in_loop:` stays the tree's word until the conjunct reads; (2) the header comment's sentence *'the loop's `person`/`realm`/`settlement` vocabulary is not canon's five, and no mapping between them exists — that gap is R-04's real content'* is replaced by a pointer: the mapping is `rosters.yaml: scale_of_rung` (`SCALE_OF_RUNG`, `data/rosters.py`), and what is open is a game reader of it (`hole_register.yaml` H-89); (3) the first `scales:` row's note (*'`capability` is EMPTY on 429 of the 430 persons'*) is cut to the present fact, read by command at landing." The register's three lines that read `scales[].conjunct` landed in B02.13.
- WHERE: `engine/season/requirements.yaml` (`scales:` block and its header comment).
- TESTS: `test_check_requirements.py::test_a_scales_row_naming_no_r04_conjunct_is_refused` (B02.13) stays green.
- FALSIFIER and CONTROL: "a `scales:` row naming `R-04.c9`: the register must exit non-zero" (the B02.13 test). Control: the seven `in_loop:` values unchanged (`git diff`).
- GATE: `python -c "from engine.season.data.rosters import SCALE_OF_RUNG; print(len(SCALE_OF_RUNG))"` → 8 (the pointer's target exists; read 2026-11-12); the `register --requirements` exit-0 arm reads R-04's conjuncts, which B02.38 writes: moved there (§5.8). Step (3)'s present fact: `python -c` over `build_realm(0)` counting persons with a non-empty `capability` (after B01 every person holds `unauthored_attributes`; the note states what the command prints, with its tree).
- HASH MOVERS: none.
- DEPENDS ON: V12 B02.13 (the register reads `scales[].conjunct`); EXISTS-IN-TREE `engine/season/data/rosters.py::SCALE_OF_RUNG`, `engine/season/tests/test_scale_of_rung.py`.
- GLOSSARY: none (`capability` stays the tree's identifier in backticks, A-98).
- COST and TIER: edit; `sonnet`, medium.
- LANDS IT: B02's producer; `Item: B02.31`, `[skip ci]`.

### B02.32 — R-08.c's test: some chosen acts were not the top candidate, and none at zero temperature · IS-A-05 part 1 · BUILD · HASH EQUAL
- SOURCE: `master/instructions/IS_A_NINE_part2.md` `IS-A-05` part 1 (the one owner: `IS-B2-CORE-04` is a pointer to it); `U4_TRACEABILITY.md` G-4 row 11. Part 2 (R-07.d) lands in B10 after `02_CHAR_scar_cap_and_regard_unit`.
- ADVANCES: R-08.c.
- INSTRUCTION (copied): "in `engine/season/tests/test_realm_requirements.py`, NEW `test_r08_some_chosen_acts_were_not_the_top_candidate_and_none_at_zero_temperature`, seeds 0–2: play one season through `harness/decision_spread.py::play_season` (the chooser is watched, never steered) at `DEFAULT_FIXTURES` and at `.sweep("choice_temperature", 0.0)`; assert the shipped arm's count of deliberations in which the sampler's pick was not the leading candidate is above 0 and the zero arm's is 0. `print_season` gains one line, `not the top candidate: <k> of <deliberations with a strict top>`." `[UNVERIFIED: that play_season's split carries the outvoted count per played deliberation under one key — basis: the module docstring; the executing session opens play_season first]`: step 0 of this item is to open `play_season` and record in the commit body where the outvoted count is read.
- WHERE: `engine/season/tests/test_realm_requirements.py` (NEW test); `engine/season/harness/decision_spread.py` (`print_season`).
- TESTS: the new test, written red before `print_season`'s line where the count needs a new key, else read green at once with its falsifier run.
- FALSIFIER and CONTROL: "pin `choice_temperature` to 0 in the shipped arm: the test must fail." Control: the zero arm reads 0.
- GATE: `python -m pytest engine/season/tests/test_realm_requirements.py -q -k r08` → green; `PYTHONHASHSEED=0 python -m engine.season.harness.decision_spread --season --seed 0` → prints the `not the top candidate` line.
- HASH MOVERS: none.
- DEPENDS ON: V12 B02.22 (the file); V12 B02.28 (`decision_spread.py`, serial); EXISTS-IN-TREE `harness/decision_spread.py::play_season`, `::print_season`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: B02's producer; `Item: B02.32`, `[skip ci]`.

### B02.33 — the sites of the digest additions are opened before each edit · IS-B2-CORE-07 · POINTER
- SOURCE: `master/instructions/IS_B2_SC_FI_CORE_CHAR_part2.md` `IS-B2-CORE-07` (POINTER: "B02's first step for this member is to open each cited site and confirm the symbol and line before the edit; a site that does not match is dropped from the member with a line in the commit body, not repaired by guess").
- No work of its own: closed by the first INSTRUCTION step of B02.09, B02.10, B02.11, B02.12, B02.26 and B02.30, which copy it. No commit.
- What the pointed section does: before any digest-addition edit, each cited `file:line` is opened on the batch's tree and its symbol confirmed; a site that does not match is dropped with a line in the commit body.
- Targets: the files in the WHERE lines of those six items (`engine/season/tests/test_season_shape.py`, `test_sc02_typed_ids_and_loader.py`, `test_governance_build.py`, `test_cp_t03_04_arms.py`, `test_in53_vacancy_need.py`, `test_in36_foreign.py`, `test_told_by_channel.py` and the others those items name); B02.10 step 1 gives the locating command (`git show 785bc62:<file> | sed -n '<L>p'`, then `grep -nF`).
- Gate: `git log --grep "Item: B02.09\|Item: B02.10\|Item: B02.11\|Item: B02.12\|Item: B02.26\|Item: B02.30" --format=%B` → each body carries one line per cited site, "found" or "absent at base" (repair lane R2a, K1 F7: E-5's body).

### B02.34 — R-05's `measure:` carries a command, no figure · the intake V9-27 · BUILD · HASH EQUAL
- SOURCE: the intake `:108` (V9-27, carry-forward E3 Block 8 (i): "`requirements.yaml:997` (R-05's `measure:` comment) says the verb table has 44 rows; it has 56 | EDIT | CR-02 (h), at the next batch that touches R-05"); placed by `V12_STRUCTURE.md` §2.2's order (the entry's own text, "with `01_CORE_requirements_reading_record`", is met: that proposal's §1 landed as B02.13); closes V9-27.
- ADVANCES: R-05 (its `measure:` line).
- INSTRUCTION: the entry's gate, "no figure in the comment, a command instead": R-05's `measure:` (`engine/season/requirements.yaml`, row R-05) keeps one command and no count of rows. On this tree the comment carries the history "It was '38' as of ED-IN-0261, '32' until ED-FI-0009 made the count honest and '37' until `release` landed" and the definition of "built out" (read 2026-11-12; the "44 rows" text has moved, E3's `[UNVERIFIED]`): the figures are deleted (the file's git log keeps them); the definition is carried by R-05.b's conjunct `text` in B02.38, and the `measure:` becomes `python -m engine.season.harness.corpus_run --seasons 2  # the 'WHERE THE <n> GO' line; n is len(VERB_TABLE) at measurement time` [v12: two seasons a case, D-17; the case's own span, to `MAX_SEASONS`, is B99's], naming the row's cheapest conjunct (B02.13's rule).
- WHERE: `engine/season/requirements.yaml` (R-05, `measure:`).
- TESTS: none new.
- FALSIFIER and CONTROL: `grep -n "measure:" engine/season/requirements.yaml` on R-05's line shows a digit that is a row count. Control: R-05's `status:` unchanged.
- GATE: `python -c "import yaml; r=[x for x in yaml.safe_load(open('engine/season/requirements.yaml'))['rows'] if x['id']=='R-05'][0]; import re; print(re.findall(r'\b\d+\b', r['measure']))"` → `[]` (no figure; the key path `rows` is checked against the file at the item's open).
- HASH MOVERS: none.
- DEPENDS ON: V12 B02.13 (the row shape; `measure:` names the cheapest conjunct).
- GLOSSARY: none.
- COST and TIER: edit; `haiku` (the entry's tier) or the batch's `sonnet` producer in the same window.
- LANDS IT: B02's producer; `Item: B02.34`, `[skip ci]`.

### B02.35 — R-01's and R-02's narrative leaves `requirements.yaml` · the intake DEF-8 · POINTER
- SOURCE: the intake `:109` (DEF-8, "IN · U3 B02 (decide there)"; carry-forward E4 `:4360`: "NERS X2 (move R-01/R-02 narrative out of `requirements.yaml`) … deferred until after RB-2's R-01/R-02 re-take"; E4 `:593`: "session `01_CORE_requirements_reading_record.md` (U3 B02) and `16_PESSIMIST_CORE_the_nine_gate…` rewrite requirements.yaml `measure:` strings; may satisfy [UNVERIFIED]").
- Decided here, ladder step 1 (superseded): B02.13 deletes every row's `measured:` ("the file's history is its git log"), which is the narrative DEF-8 would move; B02.15 re-points the two `measure:` strings. No work of its own; DEF-8 is closed by B02.13, cited in B02.13's commit body. No commit.
- What the pointed section does: B02.13 step 1 removes the `measured:` key from all nine rows of `engine/season/requirements.yaml` (the narrative R-01's and R-02's DEF-8 would have moved), and B02.15 re-points the two `measure:` strings.
- Targets: `engine/season/requirements.yaml` (`rows[*].measured`, read at the tree of 2026-11-13 on all nine rows).
- Gate: `python -c "import yaml; r=yaml.safe_load(open('engine/season/requirements.yaml'))['rows']; print(sum('measured' in x for x in r))"` → `0` after B02.13 (control: `9` on the base, read by repair lane R2a, K1 F7).

### B02.36 — R-03's stale opening text and the header's "one tick granularity" · the intake H-2 · BUILD · HASH EQUAL
- SOURCE: the intake `:110` (H-2, carry-forward E5 Block D9, copying v11 part 15 §5 H-2: "Stale: the opening of `measured:` (… 'What is missing is a scene-granular TICK … flattened into one `acts` list'), which describes the pre-U2 loop, and the file header (… 'The loop implements one tick granularity and no zoom'). … checked by `python -m engine.season.harness.register --requirements`"); placed by §2.2's order; closes H-2.
- ADVANCES: R-03 (its text).
- INSTRUCTION: (1) R-03's stale `measured:` opening left the file with `measured:` in B02.13: checked, not edited (`git grep -n "scene-granular TICK" -- engine/season/requirements.yaml` → nothing). (2) The header comment's sentence "The loop implements one tick granularity and no zoom, so R-03's scene tick is the Hybrid mode's precondition, not a local nicety." is replaced by a sentence that states what runs: the loop ticks scene by scene (R-03's `met` rests on R-03.a and R-03.b, the conjuncts B02.38 writes), and the zoom between the modes is not built; no figure.
- WHERE: `engine/season/requirements.yaml` (the header comment of `§1 THREE MODES`).
- TESTS: none new.
- FALSIFIER and CONTROL: the header still says "one tick granularity" (`grep -n "one tick granularity" engine/season/requirements.yaml` → nothing). Control: no row's `status:` changes.
- GATE: the grep above → nothing; the `register --requirements` exit-0 arm at B02.38 (moved, §5.8).
- HASH MOVERS: none.
- DEPENDS ON: V12 B02.13.
- GLOSSARY: none (the season's pass is still `round` in the tree until B04; the sentence says "scene by scene").
- COST and TIER: edit; `sonnet`, medium.
- LANDS IT: B02's producer; `Item: B02.36`, `[skip ci]`.

B02.37 (READING): its text is Reading 1 of `## Readings (B02)`, before B02.99 (E-10; moved there by repair lane R2a, K1 F11).

### B02.39 — the corpus run takes a seasons cap, so a gate reads it at two seasons · v12 repair R1 (D-17) · BUILD · HASH EQUAL
- SOURCE: none in the suite; the plan's own repair (`checks/R1_APPLIED.md`, repair 2): K1 F3 and K3 F2 found that `engine/season/harness/corpus_run.py` plays each case for its own `temporal.span_seasons` clamped at `MAX_SEASONS = 6` (`seasons_for`), with no way to ask for fewer, so every gate that runs it (B02.38's conjuncts, B03, B04, B05, B10, B21 and later) breaks D-17 (no gate past two seasons before B99). Ladder step 5 (what the architecture needs): one optional cap, the shipped clamp unchanged when it is absent. Lands after B02.13 (the item that first writes the corpus command into a conjunct's `measure:`) and before B02.38 (the first item that runs it). `[ASSUMPTION: "after the item that first runs the corpus" read as after B02.13 and before B02.38 — basis: a cap that lands after the first run cannot bound that run]`
- ADVANCES: none of the nine by itself; every later corpus reading is taken at two seasons a case (D-17), and B99's re-take runs it without the cap.
- INSTRUCTION (the exact edit, `engine/season/harness/corpus_run.py`):
  1. `seasons_for` takes an optional cap; with none, it returns what it returns today:
  ```python
  def seasons_for(case: dict, cap: int | None = None) -> int:
      """The case's own `temporal.span_seasons` where it is an integer, clamped to `MAX_SEASONS`; with
      `cap`, clamped to `cap` too (a gate's two-season horizon, D-17). With no cap, the shipped clamp."""
      t = case.get("temporal")
      n = t.get("span_seasons") if isinstance(t, dict) else None
      n = min(int(n), MAX_SEASONS) if isinstance(n, int) and n > 0 else DEFAULT_SEASONS
      return n if cap is None else min(n, cap)
  ```
  2. `run_case(case: dict, seed: int = 0, lane: str = "NPC", seasons_cap: int | None = None)`; its `n = seasons_for(case)` becomes `n = seasons_for(case, seasons_cap)`.
  3. `main(seed: int = 0, seasons_cap: int | None = None)`; its call becomes `run_case(c, seed, lane, seasons_cap)`; its header line reads `f"CORPUS RUN — {len(rows)} cases, seed {seed}, seasons from `temporal.span_seasons`" + (f", capped at {seasons_cap}" if seasons_cap is not None else "")`, so a reading quotes the cap it ran under.
  4. The command line: a pure parser beside `main`, and the `__main__` block calls it (the positional seed stays as it is):
  ```python
  def parse_argv(argv: list[str]) -> tuple[list[int], int | None]:
      """`[seed] [--seasons N]`: the positional seed as before; `--seasons N` caps every case at N seasons."""
      argv, cap = list(argv), None
      if "--seasons" in argv:
          i = argv.index("--seasons"); cap = int(argv[i + 1]); del argv[i:i + 2]
      return [int(a) for a in argv], cap


  if __name__ == "__main__":
      args, cap = parse_argv(sys.argv[1:])
      raise SystemExit(main(*args, seasons_cap=cap))
  ```
  5. `_span_status` is not edited: it reports the corpus's own span against `MAX_SEASONS` (`CLAMPED`), a fact about the case, not about the run.
- WHERE: `engine/season/harness/corpus_run.py` (`seasons_for`, `run_case`, `main`, `parse_argv` NEW, the `__main__` block); NEW `engine/season/tests/test_corpus_run_seasons_cap.py`.
- TESTS: NEW `engine/season/tests/test_corpus_run_seasons_cap.py` `[ASSUMPTION: test names; the item creates them (E-3)]`: `test_with_no_cap_every_case_runs_the_shipped_clamp` (for every case of `run_cases.load_cases("NPC")` and `("ARC")`, `seasons_for(c)` equals `min(span, MAX_SEASONS)` for an integer span and `DEFAULT_SEASONS` otherwise, computed in the test from the case's own `temporal`; `assert checked >= 100`); `test_a_cap_of_two_bounds_every_case` (`seasons_for(c, 2) <= 2` for every case, and `== min(seasons_for(c), 2)`; a case with `span_seasons: 1` reads 1); `test_the_command_line_reads_the_cap` (`parse_argv(["0", "--seasons", "2"]) == ([0], 2)`, `parse_argv(["--seasons", "2", "1"]) == ([1], 2)`, `parse_argv(["0"]) == ([0], None)`, `parse_argv([]) == ([], None)`).
- FALSIFIER and CONTROL: a cap that does not bound (a case at three seasons under `--seasons 2`), or a default that moved (any case whose uncapped count differs from the shipped clamp): either reds a test above. Control: the uncapped run is the shipped run (test 1 over the whole corpus); `seasons_for`'s callers that pass no cap (`test_season_shape.py`, `test_in50_refusals_carry_the_occasion.py`, `test_u8_ambitions.py`) are unchanged.
- GATE: `python -m pytest engine/season/tests/test_corpus_run_seasons_cap.py engine/season/tests/test_u8_ambitions.py engine/season/tests/test_in50_refusals_carry_the_occasion.py -q` → pass; `PYTHONHASHSEED=0 python -m engine.season.harness.corpus_run 0 --seasons 2` → exit 0, its header line ends `capped at 2` (sized first, run in the background, read at B02.38, whose step 6 runs it anyway).
- HASH MOVERS: none (an instrument; `World.content_hash()` does not reach `harness/`).
- DEPENDS ON: EXISTS-IN-TREE `engine/season/harness/corpus_run.py::seasons_for`, `::run_case`, `::main`, `MAX_SEASONS`, `DEFAULT_SEASONS`; `engine/season/harness/run_cases.py::load_cases`; V12 B02.13.
- GLOSSARY: none (no game term; "cap" is the ordinary word, said in the docstring and `--help`-less usage line of `parse_argv`).
- COST and TIER: small build; `sonnet`, medium.
- LANDS IT: B02's producer; `Item: B02.39`, `[skip ci]`.

### B02.38 — the nine's conjuncts, authored, and the readings this batch takes · IS-A-02 · BUILD · HASH EQUAL
- SOURCE: `master/instructions/IS_A_NINE_part2.md` `IS-A-02`; `master/instructions/IS_A_NINE.md` §1.2, §2 to §10 (the conjunct tables, copied below whole); rulings A-9, A-24, A-30, A-35, A-81, C3-K5; `proposals/U5a_tests_digest_additions.md` §F2 (R-02's reading text); `proposals/01_CORE_tests_shipped_world_falsifiers.md` row 3 (R-02's reading names the shipped-budget test); the batch's last item (`V12_STRUCTURE.md` §2.2: "`IS-A-02` last").
- ADVANCES: all nine; R-01.a, .b, .c; R-02.a, .b; R-03.a, .b; R-04.b; R-06.d, .e; R-07.a; R-08.b, .c; R-09.a read.
- INSTRUCTION:
  1. (`IS-A-02`, copied) "write each row's `conjuncts:` from the tables of `IS_A_NINE.md` §2 to §10: the conjuncts carried from `workplans/valoria_master_workplan_v11_part2.md` §2 to §10 verbatim in `text`, the changed ones with the ruling in `text` (A-9, A-24, A-30, A-35, A-81, C3-K5), each `[ASSUMPTION]` of §2, §4 and §10 copied into its conjunct's `text` with its revert. `holds` is `yes` only where this batch's own run of the `argv` reads it; every other conjunct is `unread` or `no` with the last recorded reading's tree. Readings to take in B02: R-01.a (`corpus_run --seasons 2` [v12: two seasons a case, D-17; the case's own span, to `MAX_SEASONS`, is B99's]), R-01.b, R-02.a, R-01.c, R-02.b (B02 builds them), R-03.a, R-03.b, R-04.b, R-06.d, R-06.e, R-07.a, R-08.b, R-08.c, R-09.a."
  2. The `argv` of each conjunct is the command of the table's "command and expected reading" column as a list (no shell string); `expects` is the expected reading; `text` is the conjunct column with its marks. Two corrections the earlier items of this batch force, each said in the commit body: (a) R-07.a's `argv` is B02.05's `-k` expression, because B02.04 deleted `test_choose_receives_no_world`, the first name of the table's expression, and B02.13's register refuses a `-k` name that is no test's; (b) R-02.a's `reading.does_not_show` carries §F2's sentence: "the played sequence parts when observation deposits are cut (T3 row 2); the fork-and-follow test shows divergence in both arms and attributes nothing to the deposit channel".
  3. The two retired conjuncts (R-01's and R-02's reconvergence below 96 % at `2x3`) are not written; the commit body names them and keeps their last reading's tree (`2ca90dce7`), with the table's assumption and revert.
  4. `status:` is NOT edited (A-114; `V12_STRUCTURE.md` V4: only B99 may edit a row's `status:`; repair by lane H3 after K11): each conjunct's `holds:` and `reading:` are written from the readings, and the row keeps the `status:` it has. The held count (conjuncts holding with a reading of this batch) is what `--requirements` prints. A held row (R-01, R-02, R-03) that fails to read is a STOP reported to Jordan, not an edit of the conjunct, and no golden is re-pinned to pass it.
  5. The conjunct tables, copied whole from `IS_A_NINE.md` (columns as there; "holds" is the reading at `6e1ea91` or the row's last recorded tree, re-read here where step 1 names the conjunct):

  **R-01 — "decisions must propagate"**

  | id | conjunct | command and expected reading | source | holds | first read |
  |---|---|---|---|---|---|
  | R-01.a | the corpus cites cross-person causes | `python -m engine.season.harness.corpus_run --seasons 2` [v12: two seasons a case, D-17; the case's own span, to `MAX_SEASONS`, is B99's]: `check R3: n of n pass` on both lanes, `not True: none`, control `R3 False -> True` | v11 part 2 §2, kept | yes at `2ca90dce7` | now |
  | R-01.b | the played realm does too, on three seeds | `python -m pytest engine/season/tests/test_realm_requirements.py -q -k r01`: three seeds green; the witness-cut control reads 0 | `01_CORE_tests_shipped_world_falsifiers` rows 1 (B02) | unread (the file is MISSING, written in B02) | B02 |
  | R-01.c | removing one person's choice changes other persons' acts | `python -m engine.season.harness.storybar --remove <person> --base-seed 0 --seasons 2`: replay line `0`; removed line above 0 | `16_PESSIMIST_CORE_the_nine_gate_and_a_knockout_reading` edits 2–3 (B02); **the expected reading is added by `IS-A-03`** (the proposal reports the line and states none) | unread | B02 |
  | (retired) | reconvergence below 96 % at `2x3` | `wd_collect.py` after 36 chunk cells | v11 part 2 §2 | yes at `2ca90dce7` | — |

  *The retired conjunct* (copied): "C3-K5 and C-U5a-01 decide one instrument per property and re-point `measure:` to the removal test; the sweep sits under `proposals/`, costs 75 minutes, and its own caveat stands on every reading (*'detected OVER THE BASELINE on ALL 4 plants: False'*). It leaves the `met` text at B02 with its last reading kept in the file's history. `[ASSUMPTION: retiring the conjunct, not only the measure: string, is what C3-K5 means — basis: a conjunct no session re-takes is not a reading. Revert: keep it as R-01.d and R-02.c, re-taken once at milestone M2's close.]`" (A-114: no re-take runs at M2; the revert, if taken, re-takes them in B99.)

  **R-02 — "decisions affect subsequent decisions"**

  | id | conjunct | command and expected reading | source | holds | first read |
  |---|---|---|---|---|---|
  | R-02.a | withholding what acts observe changes later acts at the shipped budget | `pytest engine/season/tests/test_realm_requirements.py -q -k r02`: seeds 0–2 differ after a common prefix; the same seed twice is one sequence | `01_CORE_tests_shipped_world_falsifiers` row 2 (B02) | unread | B02 |
  | R-02.b | a removed choice changes acts in a *later* lap or season | the R-01.c command: at least one differing act at a `(season, round)` after the removed one | `IS-A-03` | unread | B02 |
  | (retired) | reconvergence below 96 % | as R-01 | v11 part 2 §3 | yes at `2ca90dce7` | — |

  **R-03 — "seasons must tick scene-by-scene, so what occurs after one scene can impact the next scene"**

  | id | conjunct | command and expected reading | source | holds | first read |
  |---|---|---|---|---|---|
  | R-03.a | a deposit in one lap changes a later lap's candidates | `python -m pytest engine/season/tests -q -k test_u2_`: all pass, the one-lap control among them | v11 part 2 §4, kept | yes (last read `444a00e1`) | now |
  | R-03.b | a real case runs its laps | `python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0`: exits 0, prints `rounds=` per season | v11 part 2 §4, kept | yes | now |

  [v12, repair lane R2a (K1 F6): in the `text` of R-02.b, R-03.a, R-03.b and the copied assumption below, the season's pass is "lap" (A-101; precedent B03.51, B03.56: the drift corrected and said); the identifiers `(season, round)` and the printed `rounds=` key are the tree's and are kept until B04 renames them. The commit body names this as the one departure from `IS-A-02`'s "verbatim in `text`".]
  **R-03.c is not written by this item** (repair lane V1, `V12_VERDICT.md` defect 1). R-03 is `met` at the tree (`engine/season/requirements.yaml`, row R-03), and B02.13's step 2 refuses `status: met` unless every conjunct of the row reads `holds: yes`; R-03.c's file (`test_scene_sequence.py`) is written in B08, so in B02 it could only be `unread`, the row would be refused, and this item's GATE could not read exit 0. B08.99 adds R-03.c to R-03's `conjuncts:` with its `holds: yes` and its reading (its row, the assumption and the revert are copied there whole). The rule for every other conjunct whose instrument a later batch builds is unchanged: it is written here with `holds: unread` and its `argv`, and B02.13's step 2 resolves the `argv` of a conjunct at `yes` or `no` only (R-04.c1 to c7's tests and harnesses, R-06.c, R-07.d, R-09.a's `test_task_draw.py`, R-09.d, R-09.e); none of them is on a `met` row.

  **R-04 — "strategic and management actions must be possible, ie decisions at differing scales"** (v11 part 2 §5; three, the third one per `scales:` row)

  | id | conjunct | command and expected reading | holds | carried by (batch) |
  |---|---|---|---|---|
  | R-04.a | every seat-gated remit verb executes at least once with `Act.via` set: `requisition`, `issue`, `open_case`, `determine`, `convene`, `dispatch`, `confer`, `establish`, `revoke` | `python -m engine.season.harness.aperture 2 0` [v12: two seasons, D-17; the table's four seasons are B99's `argv`]: for each, the `BUILT OUT` block's `via` column at least 1 (`IS-A-06`; today the instrument prints attempted and executed and does not read `Act.via`) | no: `confer`, `determine`, `requisition` and `revoke` are among the 34 verbs that execute in neither instrument at `4995824` (`audits/17_CENSUS_REST.md` §6); `via` is unread for all nine | `establish`: `14_VERBS_BINDING_A` (B21) · `confer`, `revoke`: `14_VERBS_BINDING_C` (B21) · `dispatch`: `14_VERBS_BINDING_D` (B21; D4 waits, below) · `requisition`: `14_VERBS_MATERIAL_B` (B12), `06_FA_levy_through_the_seat_B` (B21) · `issue`: `06_FA_decree_binds` (B21) · `open_case`: `14_VERBS_SOCIAL2_C` (B25) · `determine`, `convene`: `14_VERBS_BINDING_B` (B32) |
  | R-04.b | no second driver; the faction view is tested | `engine/mc_v18.py` absent; `pytest engine/season/tests/test_faction_q.py -q` green | file state yes; test not run here | — |
  | R-04.c1 | character creation, development, chronicling is in the loop | a seated person is picked and his sheet shown (`11_GO_fidelity_and_campaign_modes` edit 1, `test_creation_sheet_shows_holdings_for_a_seat_holder`); `train` built out (`BUILT OUT` block); `python -m engine.season.harness.chronicle --seed 0` tells (`09_WR_B_chronicle_that_tells`, `test_in37_chronicle.py`) | no (`in_loop: false`) | B34 · B22 · B36 |
  | R-04.c2 | grand strategy politics | `governance_spine play 0 8 --world realm`: exit `closed True` at seeds 0–2 (`06_FA_shortest_loop_B`) | no | B21; land on a won march B23 |
  | R-04.c3 | social contests and debates | `python -m engine.season.harness.headless --world hearing`: the same content hash twice (`05_SC_playable_hearing_B`) | no ("seam unbuilt") | B24 |
  | R-04.c4 | mass battles and strategy warfare | `field.won + field.lost` above 0 in computed play at `aperture 1 s`, s = 0–2, printed beside `field.unopposed`; `test_field_scene.py` (`04_MB_playable_field_scenario`) | partly: `field.lost` 1 at seed 2, 0 at seed 0 (§0 probe) | B19, B20, B22 |
  | R-04.c5 | personal combat and grid combat with units | (i) a duel resolves in computed play at seeds 0–2 (`aperture 2 s`: `challenge` executed above 0, `03_PC_duel_chain_reach`); (ii) a fought field resolves on the cell battlefield (c4); (iii) commander-chosen orders (`27_MB_D`, `test_none_decider_equals_no_decider`); the grid of named persons (`04_MB_squad_grid_of_named_characters`, `test_squad_field.py`) | (i) in the realm at seed 2 only: no function of `modules/combat` is entered at seed 0 in three seasons (`HOLISTIC_AUDIT.md` §3; §0 probe: `challenge.refused` 48); (ii) seed 2 only; (iii) and the grid: no | B01 · B20 · B30 |
  | R-04.c6 | settlement management, city building | `python -m engine.season.harness.valley` (`07_SE_valley_scenario`, `test_valley.py`); `found`, `build`, `work` built out at `aperture 2 0` [v12: two seasons, D-17; four are B99's] | no | B12 |
  | R-04.c7 | investigations | `test_shortest_case.py` and `test_playable_inquiry.py` (`08_FI_07`, `08_FI_03`) | no | B11; the hearing piece B24 |

  *Changes against v11, each by a ruling* (copied into the conjuncts' `text`): "(1) **`revoke` reads in computed play.** … A-35 rules a head strips an officer by a resistible draw and `14_VERBS_BINDING_C_turnover` carries the `revoke` draw (B21): the revert's condition is met, so the hand-built reading ends. (2) **Commander-chosen orders join c5.** … A-1 makes the commanded and the automatic battle one resolver. Its own revert (*'commander-chosen orders restored as a third gate'*) is taken. (3) **Each `scales:` row gains a `command:` and a `reading:`** in the file (`IS-A-04`)." Every R-04 gate over two seasons is written at two (`aperture 4 0` → `aperture 2 0`, "(four seasons in the source; A-114)"); `governance_spine play 0 8` is kept as written and `unread`: the tree's `harness/governance_spine.py` has no `play` command (its `__main__` prints `census(build(0))`, read 2026-11-12); `06_FA_shortest_loop_B` (B21) builds it, and B21's author reads whether 8 is a season count (if it is, two, with the A-114 note).

  **R-05 — "all verbs must be built out, and doing so requires planning out all the different scales of play required in a season"**

  | id | conjunct | command and expected reading | source |
  |---|---|---|---|
  | R-05.a | no verb row is without a predicate and effect, never attempted, or only refused | `python -m engine.season.harness.corpus_run --seasons 2` [v12: two seasons a case, D-17; the case's own span, to `MAX_SEASONS`, is B99's]: `WHERE THE <n> GO: 0 have no predicate/effect · 0 foldable but never even attempted · 0 attempted and always refused`; **or** R-05.b for every verb in the last two classes | v11 part 2 §6, kept |
  | R-05.b | every verb is built out in the realm | `python -m engine.season.harness.aperture 2 --seeds 0 1 2` [v12: two seasons, D-17; the table's four seasons are B99's `argv`]: the `BUILT OUT` block reads `built out <n> of <n>`, n = `len(VERB_TABLE)` at measurement time (`IS-A-06`) | v11 part 2 §6 and REM-02's definition; the block is new |
  | R-05.c | no built-out verb has a band that writes nothing | the same run: `NULL SCENES` reads 0 for every verb (`IS-A-07`) | **A-81** |

  R-05.b's `text` carries the definition (copied): "*'Built out'*, as v11 defines it `[ASSUMPTION; medium; Jordan to correct]`, kept: at least one act formed by the chooser in a seeded run of a shipped builder is admitted, folds its band and emits the row's declared kinds; where the band declares writes, a minted receipt has before ≠ after; a hand-built execution never counts; the denominator is `len(VERB_TABLE)` and a row leaves the table only by a ruling. **One clause of it is superseded:** *'a verb whose bands write nothing (`speak`, `interrogate`) is built out on execution'*. A-81 rules that every scene writes a durable change whatever its outcome, so no verb's band may write nothing; R-05.c replaces the clause." R-05.b's and R-05.c's `argv` run at two seasons: `aperture 2 --seeds 0 1 2` "(four seasons in the source; A-114)".

  **R-06 — "characters must be robustly built with goals, ambitions, convictions, moral values, etc"**

  | id | conjunct | command and expected reading | holds | what moves it |
  |---|---|---|---|---|
  | R-06.a | every candidate offered carries a nonzero conviction term (no tie broken by the draw where a person has a reason) | `corpus_run --seasons 2` [v12: two seasons a case, D-17; the case's own span, to `MAX_SEASONS`, is B99's]: the `RANKING DISCRIMINATION` line, with no verb under `RANKING EXCLUDES` | no (eight verbs excluded at the last reading; the alignment table is sparse) | the cells of `02_CHAR_choice_alignment` and `16_PESSIMIST_CHAR_B` (B10 the mechanism; **BA1 the values**) |
  | R-06.b | the cast tests pass | `pytest engine/season/tests -q -k 'ambitions or cast'` | recorded, and by v11's own note blind (it saturated at 5 of 5 seeds in all 46 cases): it does not count | — |
  | R-06.c | convictions spread decisions | `python -m engine.season.harness.conviction_spread` passes | not run for the last paragraphs | `16_PESSIMIST_CHAR_B` adds `harness.conviction_spread` readings (B10) |
  | R-06.d | pursuit decides more than the draw | `decision_spread --decisions`, seeds 0–2: the strict-top share above one half at the shipped τ, beside the control τ `[ASSUMPTION: one half, H-96]` | yes at the CR-17 reading | re-read at B10 (`02_CHAR_resolve_and_temper` changes what the departure from the top is) |
  | R-06.e | every acting person carries a pursuit vector | `decision_spread --persons`: n of n at the built realm | yes, 83 of 83 | re-read at B39, where A-44's generated cast (about 94 persons and kin) arrives |

  R-06.b is written with its note ("it does not count") and `holds: unread`, so it neither holds nor blocks `met` `[ASSUMPTION: the table keeps the row as a recorded, non-counting conjunct — basis: IS_A_NINE.md §7 "it does not count"; UNDECIDED in this part's receipt: drop it as retired, or keep it so]`. R-06.c's `argv` names `harness.conviction_spread`, which B10 adds: `unread` until then (R-06 is not a `met` row, so the register does not refuse it).

  **R-07 — "characters must have memories and feelings and attitudes and relationships, and they must only have imperfect knowledge"**

  | id | conjunct | command and expected reading | holds | what moves it |
  |---|---|---|---|---|
  | R-07.a | the chooser is handed no world; two persons hold different things | `python -m pytest engine/season/tests -k 'choose_receives_no_world or a_view or r7_two_persons'` (written with B02.05's expression in its place: step 2 (a)) | yes by the row; not run here | held: B09, B10, B11 |
  | R-07.b | two hearers with different claims about one subject read different regard after two realm seasons | v11 names no committed command (met at B-E on a test) `[UNVERIFIED: the test's name was not opened]` | yes by the row | `02_CHAR_scar_cap_and_regard_unit` (B10) changes the unit: re-read there |
  | R-07.c | a fought field writes the losers' stance | `aperture 1 s`, s = 0–2: `field.won + field.lost` above 0, quoted with `_eff_march`'s `Person.stance` receipt on the losing side, `field.unopposed` printed beside `[ASSUMPTION; medium; Jordan to correct]` | count: 0 / not read / 1 at seeds 0 / 1 / 2 (before B01); receipt unread | B01 (re-pins every realm), then B19, B20, B22; the read is `IS-A-06`'s block |
  | R-07.d | a feeling, attitude or relationship changes a decision | `pytest engine/season/tests/test_realm_requirements.py -q -k r07`: a planted regard changes the top candidate at least once in seeds 0–2; the unplanted seed is equal | unread: *"no test by any name"* (`01_CORE_tests_shipped_world_falsifiers:36`) | **`IS-A-05`** (`U4` G-4 row 10), in B10 |

  R-07.b's `argv`: `engine/season/tests/test_told_by_channel.py::test_r07_realm_regard_differs_between_hearers_by_claim_not_stance_alone` (opened by `U5a_tests_digest_additions` §F1, "a two-season realm reader"), which settles the table's `[UNVERIFIED]`; the commit body says so.

  **R-08 — "decisions must not be omniscient and perfectly rational"**

  | id | conjunct | command and expected reading | holds | what moves it |
  |---|---|---|---|---|
  | R-08.a | every tie among offered candidates is between candidates of equal, nonzero choice score | `corpus_run --seasons 2` [v12: two seasons a case, D-17; the case's own span, to `MAX_SEASONS`, is B99's] (`RANKING DISCRIMINATION` and the tie ordering) and `decision_spread --decisions` | no (the same sparse table as R-06.a) | **BA1** (the cells) |
  | R-08.b | the choice is sampling, and the argmax is its zero-temperature control | `pytest engine/season/tests -q -k test_u4_the_choice_is_sampling` | yes by the row | held: B06 (the draw's owner), B10 |
  | R-08.c | in play, some chosen acts were not the top-ranked candidate | `python -m engine.season.harness.decision_spread --season --seed s`, s = 0–2: the share of resolved acts whose chosen candidate was not rank 1 is above 0 at the shipped setting and 0 at temperature 0 | unread: *"share of non-top choices in play is unread"* (`01_CORE_tests_shipped_world_falsifiers:37`) | **`IS-A-05`** (`U4` G-4 row 11), in B02 |

  R-08.c's `argv` is the test B02.32 writes (`pytest engine/season/tests/test_realm_requirements.py -q -k r08`), the committed form of the table's command `[ASSUMPTION: the test is the conjunct's command and decision_spread --season its printed line — basis: IS-A-05 part 1 builds the test and the line for this conjunct]`.

  **R-09 — "chains of events within a scene are probabilistic, not deterministic"**

  | id | conjunct | command and expected reading | holds | what moves it |
  |---|---|---|---|---|
  | R-09.a | a verb that draws is graded | today `pytest -k test_we_only_a_verb_that_declares_contests_can_be_graded_today`; **from B07** `pytest engine/season/tests/test_task_draw.py -q` (six tests; `checked >= 10` verbs) | yes today | B07 retires the premise of the present test (an uncontested verb is graded by the task draw): `IS-A-10` re-points the conjunct in that batch |
  | R-09.b | two persons resolve the same verb at different pools because they differ | `python -m engine.season.harness.aperture 2 0` [v12: two seasons, D-17; the table's four seasons are B99's `argv`]: `POOLS ROLLED` prints *two actors at different pools: yes* on a non-combat verb, beside the control in which every person holds the default | no | B04 (the home), B05 (`U5a_capability_home_and_two_inputs` Part B: the roll with two inputs, A-6, A-7), **BA1** (the cast's attributes and skill scores; U1-C's check) |
  | R-09.c | a non-combat verb besides `tell` resolves at two bands whose writes differ | `corpus_run --seasons 2` [v12: two seasons a case, D-17; the case's own span, to `MAX_SEASONS`, is B99's]: `DEGREES RESOLVED BY VERB` | no at the last reading | B05, B07 (`13_SC_draw_for_unrolled_contests`, the task draw) |
  | R-09.d | outcomes that could go either way are drawn | `test_task_draw.py::test_converted_verb_resolves_in_at_least_two_bands` (seeds 0–2, two seasons): for every converted verb with ten or more resolved acts at least two bands occur and none is 100 % one band; success Events carrying a degree at least 90 % of non-bookkeeping success Events | no (61 of 13,379 Events carry a degree, §0) | **A-24** and the standing rule; `18_DETERMINISM_task_draw_for_uncontested_verbs` gate 1 (B07) |
  | R-09.e | the draw is one owner's, keyed | `pytest engine/tests/test_draw.py -q`; same seed twice, same hash | no (14 `random.Random(` constructions in 7 files, `HOLISTIC_AUDIT_part2.md` H-10) | A-30; `11_GO_one_draw_owner` (B06) |

  R-09's assumption, copied into R-09.d's and R-09.e's `text`: "`[ASSUMPTION: R-09.d and .e are conjuncts of the row and not only gates of B06 and B07 — basis: the standing rule names R-09; v11's text would read met on one verb at two bands while nine in ten successes stay a fixed function of state. Revert: drop them; the row can then read met at B07 plus BA1.]`" R-09.a's `argv` today is `python -m pytest engine/season/tests/test_season_shape.py -q -k test_we_only_a_verb_that_declares_contests_can_be_graded_today`. R-09.b's `argv` at two seasons: `aperture 2 0` "(four seasons in the source; A-114)".

  6. The readings of step 1 are taken on the tree after B02.39 (the corpus cap; repair lane R1: B02.36 before it), `PYTHONHASHSEED=0`; the long ones (`corpus_run --seasons 2` [v12: two seasons a case, D-17; the case's own span, to `MAX_SEASONS`, is B99's]; the removal test at seeds 0–2; `aperture 1` and `2` at seeds 0–2) launched in the background at this item's open, each sized first on one seed, and read here (`STAGES.md` practice 5). Each `reading:` record carries `tree`, `date`, `seed`, `seasons`, `line` (the printed line), `control`, `does_not_show`.
- WHERE: `engine/season/requirements.yaml` only (every row's `conjuncts:` records, never a row's `status:` (step 4), `measure:` of any row B02.13 left naming a deleted command).
- TESTS: `test_check_requirements.py::test_shipped_file_exits_zero` (B02.13) turns green.
- FALSIFIER and CONTROL: "a conjunct marked `yes` whose `reading.tree` is not an ancestor of the commit that wrote it (visible in one `git log -p`); control: the register's own refusals (`IS-A-01`)."
- GATE: `python -m pytest engine/season/tests/test_register_reading.py engine/season/tests/test_check_requirements.py -q` → green (every test); `python -m engine.season.harness.register --requirements` → exit 0 (B02.13's refusal rule read on the shipped file: R-01, R-02 and R-03 stay `met`, so every conjunct this item writes on them is at `holds: yes` with a `reading.tree`, `.seed` and `.line`: R-01.a to .c, R-02.a and .b, R-03.a and .b; R-03.c is not written here, B08.99 adds it; no `met` row carries an `unread` or `no` conjunct), "prints, on B02's closing tree, R-01, R-02, R-03 with every conjunct held, and the six others with the held count their readings give, each row's `status:` as it stood at B02's opening (B99 alone edits it)" in the form `R-0n  <status>  <held> of <m> conjuncts  tree <oldest reading.tree>` (B02.13's moved arm); **the execution arm** (repair lane R2a, K1 F5: `--requirements` reads the `holds` and `status:` strings this item writes, so it cannot observe a wrong one): step 6's runs each `tee` their output to `B02.38_<conjunct id>.log` in the producer's scratchpad, and for every conjunct of R-01, R-02, R-03 at `holds: yes`, `grep -cF "<its reading.line>" B02.38_<id>.log` → at least 1 (a `reading.line` no run printed is a fabricated reading: STOP); `python tools/m1_acceptance.py --summary` → row 3 prints the held count, quoted as a record line, not a gate arm (the row is DOC-DERIVED by its own declaration, CLAUDE.md §0.2). "A held row that fails to read is a STOP reported to Jordan, not an edit of the conjunct."
- HASH MOVERS: none.
- DEPENDS ON: V12 B02.39 (`corpus_run --seasons 2`, the two-season cap its corpus conjuncts run under); V12 B02.13 (`IS-A-01`), B02.19 (`IS-A-03`), B02.32 (`IS-A-05` part 1), B02.21 and B02.22 (rows 1–2), B02.18 (`BUILT OUT`), B02.20 (`NULL SCENES`), B02.05 (R-07's expression); EXISTS-IN-TREE `engine/season/tests/test_faction_q.py`, `harness/headless.py`, `harness/corpus_run.py`, `harness/decision_spread.py`; `engine/mc_v18.py` absent.
- GLOSSARY: none beyond B02.13's rows.
- COST and TIER: edit plus instrument time (`corpus_run` recorded at 2.5 and at 8 minutes by two lanes; not measured here); `sonnet`, high; `opus` reads each reading against its conjunct's text before `holds` is written (no `status:` is written, step 4) (the judgment node that gates a requirement, CLAUDE.md §10).
- LANDS IT: B02's producer; `Item: B02.38`, `[skip ci]` (the batch's last `Item:` push is B02.99; repair lane R1, E-1); it writes the conjuncts' `reading:` records (`IS-A-12`).

## Readings (B02)

**Reading 1** (B02.37, `IS-A-12`, `master/instructions/IS_A_NINE_part2.md` "Item: IS-A-12"; the paragraph as the part's author wrote it, moved here unchanged by repair lane R2a, K1 F11, E-10):
B02.37 (`IS-A-12`, READING: no code, no commit) is the close line of this batch's BATCH GATE, which every later batch's BATCH GATE repeats: "each batch close records, in its commit body and nowhere else (CLAUDE.md §1: no count in a pointer index): `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the named conjuncts' readings with their tree, and for a batch under `IS-A-08` the quoted `BUILT OUT` and `ENGINES` lines before (the previous batch's after-reading, `reading @<sha>`, not re-taken) and after. The batch's last `Item:` commit writes the readings into the conjuncts' `reading:` records; `status:` is not edited there." Its falsifier ("a close that edits `status:` outside a re-take item, or a conjunct at `yes` whose `reading.tree` is older than the last batch that named it") is read by each batch's critic. In B02, B02.38 writes each conjunct's `holds` from its own readings and leaves every row's `status:` as it stands (its step 4; A-114 and V4: only B99 edits `status:`, which supersedes `IS-A-02`'s order to write it; the conjuncts are new; no row is claimed by landing). (Repair lane V1, `V12_VERDICT.md` defect 1: the sentence that had B02.38 write `status:` is replaced.)

### B02.99 — re-pin and close readings (EQUAL: the record) · `V12_STRUCTURE_part4.md` E-1 · BUILD · HASH EQUAL (records)
- SOURCE: `V12_STRUCTURE_part4.md` E-1, E-2; `V12_STRUCTURE_part2.md` §5.12; B02's BATCH GATE and RE-PIN lines; part 2 §11 C-01 (written by repair lane R1).
- ADVANCES: the close of the readings B02.38 takes and records (R-01 to R-03 `met`; the first `BUILT OUT`, `ENGINES` and `NULL SCENES` baselines); nothing beyond them.
- INSTRUCTION: (1) Re-pin nothing (RE-PIN: none; every item is EQUAL; the BATCH GATE's first line reads every pinned hash against B01's close, `reading @<B01 closing sha>`). (2) Read once on the closing tree and quote in this commit's body every BATCH GATE line, the `HASH READING` at `<s>` = 0, 1, 2 (`<k>` = 1) equal to B01's close, and the batch's measured wall time (build and close apart). The conjuncts' `reading:` records are B02.38's (written on B02.39's tree), not rewritten here. The commit carries no file unless the record needs one (`git commit --allow-empty`).
- WHERE: none but the commit body.
- TESTS: none new.
- FALSIFIER and CONTROL: a pinned hash that differs from B01's close (then an item here was not EQUAL: `STOPPED`). Control: B01's close readings (`reading @<B01 closing sha>`).
- GATE: the BATCH GATE above, every line, read once on this commit's tree.
- HASH MOVERS: none.
- DEPENDS ON: V12 B02.01 to B02.38, B02.39.
- GLOSSARY: none.
- COST and TIER: reading; `sonnet`, medium; the readings against each conjunct's text read by `opus` (B02's COST line).
- LANDS IT: B02's producer; `Item: B02.99`, the batch's last `Item:` push (no `[skip ci]`).

| STOP. Batch B02-tests closes here |
