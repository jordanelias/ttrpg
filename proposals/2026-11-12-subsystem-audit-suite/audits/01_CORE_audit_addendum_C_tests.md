# CORE — addendum C: test strength

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 785bc62 (working tree; `engine/`, `tests/`, `modules/`, `tools/`, `systems/`, `references/` unmoved at 46500d4)

Addendum to `01_CORE_audit.md`, whose §4 says of the tests: *"43 test files were listed for this lane;
none was opened"*. This file is that reading. The question asked of every test file or family: **what
failure can its assertions observe, and what failure could they not** (`CLAUDE.md` §0.1 pts 2–4).

## 0. Verdict

**The tests are strong where they test a rule and weak where they are cited as evidence for the game:
the gate, the fold, the refusals and the dice are each pinned by behaviour tests that carry their own
planted control, and almost nothing asserts on a played world at the shipped configuration.** The
house pattern (run the mechanism, then remove its cause in process and show the assertion redden) is
real and widespread: 297 of 2,180 season test names carry `control`, `planted`, `mutation`, `falsifier`,
`revert` or `can_fail`, across 114 of 162 files, and every one of those I opened does what its name
says. The largest weakness is on the other side. The suite's unit of evidence is a hand-built `Act`
through `_fold` on a three-to-six-person fixture; the nine requirements are claims about computed play;
and between the two there is one hash literal for a played realm at the shipped configuration, at one
seed, and no behavioural assertion on it at all. A realm season costs 7.3 s and reads cleanly against
both R-01 and R-02 with a zero control (§3), so the gap is cheap to close. The second weakness is the
goldens: one trajectory is pinned in six files, 20 of the 28 hash tests read a world that is not the
shipped one (earlier items' changes reverted in process, up to seven deep), and the corpus count pins
re-roll by one to four on unrelated changes, by their own re-pin log. The third is a small set of
tests that cannot fail on a behaviour change: two files whose subject is archived prose (one holds
three archived documents to a formula the code deleted), eight that assert a substring of source text
(one of them the first test named by R-07's `measure:`), one standing non-strict `xfail`, and three
loops that pass when handed nothing. Twenty-two resolutions are decided in §6 and carried by three
proposals.

## 1. Method, census, and what was actually read

Three trees were in scope: `engine/season/tests/` (162 test files, 2,180 test functions, 7,752 `assert`
statements; 71,169 lines, of which 37,220 are code, 12,478 comment and 11,891 docstring),
`engine/tests/` (6 files, 66 functions, 1,301 lines) and the `tests/valoria/` files the dossiers list
(100 files, 870 functions). Every dossier-listed test file exists on disk.

**Instrument.** An AST pass over all 268 files (`scratchpad/runs/CORE_C/scan_tests.py`; per-test rows in
`season_tests.tsv`, `engine_tests.tsv`, `valoria_tests.tsv`; per-family counts in `family_table.txt`)
records for each test function: asserts; asserts under an `if`; asserts under a non-literal loop;
`pytest.raises` blocks; asserts inside same-file helpers; `approx` / `isclose`; source-text reads
(`inspect.getsource`, `read_text`, `ast.parse`); skips; `monkeypatch`. It classifies nothing by itself;
it says where to read.

**Reading.** Done on a comment- and docstring-stripped view with original line numbers
(`strip.py`), because 60 % of `test_season_shape.py` (10,664 of 17,880 lines) is comment or docstring
and the question is what the assertions observe, which only the code answers.

⚠ **The charge was "read in full". That was not met, and the family table marks which rows rest on the
scan alone.**

- **Read in full (code):** `test_season_shape.py` (225 tests, 4,806 code lines); `test_g1a_*`,
  `test_g1b_*`, `test_g2_token.py`, `test_g4_no_op_receipt.py`; `test_go07_canonical_digest.py`;
  `test_interactions_log.py`, `test_soak_grades.py`, `test_loops_instrument.py`; of the four
  `*_module.py` seam tests, settlements and combat (social contest to `:65`; mass battle not reached);
  `test_in62_decision_spread.py`; `test_cr17_odds_weighting.py` (to `:248`); all six files of
  `engine/tests/`; from `tests/valoria/`: `test_m1_acceptance_probe.py`,
  `test_season_invariant_sweep.py`, `test_balance_oracle_arms.py`, `test_definitions_store.py`,
  `test_link_values_pointers.py`, `test_vocab_store.py`, `test_knot_pool_formula.py`,
  `test_export_game_constants_ambiguity.py`, `test_references_yaml_parse.py`.
- **Read at the tests the scan flagged** (zero-assert, all-conditional, skip, hash pin, `approx`):
  `test_content_operands.py`, `test_in22_shortfall_reach.py`, `test_march.py`,
  `test_sc01_obstacle_ceiling.py`, `test_u7_own.py`, `test_u7_remit.py`, `test_scale_of_rung.py`,
  `test_strife_kinds.py`, `test_cp_t03_07_body_ceiling.py`, `test_in12_step9.py`,
  `test_works_founding.py`, `test_fi03_trail.py`, `test_aperture.py` (names and callees),
  `tests/valoria/test_flow_skeletons.py` (head, constants, names), `test_mass_battle_maneuvers.py`,
  `test_charge_momentum_impulse.py`, and every hash literal and `revert_*` call in the tree.
- **`[SKIPPED: about 120 season files and about 85 valoria files — scanned by the instrument, not read;
  the reading budget went to the file that is a quarter of the tree and to the R-row tests]`.** The
  per-lane combat, mass-battle, governance, settlement, fieldwork and world families are therefore
  classified from counts, and their rows in §4 say so. Their lanes' own audits are the place a reading
  of them belongs.

## 2. Findings (worst first)

### F-TEST-01 · blocks an honest reading of THE NINE · no test asserts a requirement on a played world at the shipped configuration

- **Claim.** For each of R-01..R-09 the nearest executed falsifier runs on a fixture or template world,
  at one seed, and in two cases at a non-shipped arm (table in §3). 316 of 2,180 season tests call
  `_fold` / `resolve` / `encounter` with a hand-built `Act`; 192 build `P.tiny_world()`; 450 a file-local
  `_world()`; 215 call `build_realm`.
- **Evidence / falsifier run.** The falsifier of this claim is a test that plays the realm at
  `DEFAULT_FIXTURES` and asserts a property of the game in what happened. Tests that play the shipped
  realm exist: `test_strife_credit.py::test_the_realm_reaches_commensurate_at_the_value_given_and_never_at_the_control`
  (a hash at seed 0), `test_interactions_log.py`'s observer-effect arm, `test_in62…`'s `season_pairs`
  fixture, `test_content_operands.py:278`. Each of those opened asserts a hash, an instrument's
  property or an operand's type; none asserts propagation, a changed later decision or a
  seat-holder's act. `[the unread families may hold one; the scan cannot tell]`
- **What the realm reads when asked** (`probe_realm_gates.py`, `probe_r01_control.py`, §8): seeds 0, 1,
  2, one season: 134 of 749, 141 of 731, 162 of 751 resolved acts were occasioned by a landed claim
  that walks back to another person's act; with WITNESS cut the count is 0 of 388. With
  `observation_deposit_mode` at `none` the resolved sequence first differs at position 191, 183, 182.
  So R-01 and R-02 hold on the shipped realm at three seeds with a zero control; the tests do not say so.
- **Touches.** R-01, R-02 directly; R-04, R-06, R-07, R-09 by the same shape (planted inputs).
- **Fix.** `01_CORE_tests_shipped_world_falsifiers.md` rows 1–3, 8; the red-today falsifiers are named
  there as the gates of the lanes that own them.

### F-TEST-02 · goldens · one trajectory in six files, and 20 of 28 hash tests read a world nobody plays

- **Claim / evidence** (`probe_hash_pins.py`). 28 tests in 16 files compare `content_hash()` with a
  literal; 51 distinct literals, 11 in more than one file; `600d8b27…` (`build_realm(0)`) and `25660615…`
  (one season, seed 0, `regime_gain` 0) in six files each. 17 of the 28 call `revert_*` helpers first,
  up to seven (`test_cp_t03_01_cohorts_never_fight.py`), so they pin the tree as it stood several items
  ago; three more pin a withheld or switched-off arm. Each literal's trailing comment is a re-pin log
  with four entries from the last two batches. One literal pins the shipped played realm
  (`test_strife_credit.py:41`); probe: the realm reads it (§8).
- **Steelman.** Each revert-stacked control was the proof, at landing, that its item moved the world
  and nothing else did: with the item reverted the previous pin reads exactly. That is the declared-mover
  discipline §7 asks for, and it was followed: the logs name a control for every re-record
  (`test_go07_canonical_digest.py:320-656` has 25, `test_season_shape.py` 23, `test_season_weather.py` 22).
- **Attack.** The proof is about a commit; the test outlives it and must be kept true by every later
  item, which either re-pins it or adds a revert. The cost is quadratic in items and the world it
  observes is not the game. The steelman survives as a rule for the commit, not as a standing test.
- **Fix.** `01_CORE_tests_one_golden_owner.md` A–C.

### F-TEST-03 · goldens · the corpus count pins cannot separate a trajectory re-roll from a regression

- **Claim.** `test_the_corpus_runs_and_the_ranking_cannot_discriminate` asserts `len(by_sig) == 136`
  (`:9199`) and its siblings pin fork counts, chain depths and candidate counts (§7). All are read at
  seed 0. The run is deterministic, so a move is never sampling noise; it is also never informative on
  its own, because any change that alters one draw alters the trajectory.
- **Evidence.** The re-pin log above `:9199`: `136 -> 140`, `140 -> 134`, `134 -> 133` (*"the draws
  walk another trajectory"*), `133 -> 137`, `137 -> 136`. Four entries in the file read the new figure
  off *"the failing assertion's printed figure"*; one says *"The batch's items were not isolated one by
  one [ASSUMPTION; low …]"* (`:9184-9188`). The first audit (F-CORE-02) already judged the quantity:
  *"`DISTINCT EXECUTED SETS 136` measures variety between seeds of a template"*.
- **What survives.** The set identities beside the counts (`ever`, `refused_only`, the never-attempted
  set, `universal == set()`) state R-05's condition exactly and move only when a verb crosses a line.
- **Fix.** `01_CORE_tests_one_golden_owner.md` D: the counts go, the properties stay, and the shipped
  realm hash is the single tripwire.

### F-TEST-04 · tests of archived prose · two files, one of which holds stale text in place

- `tests/valoria/test_knot_pool_formula.py` asserts three `.designs/` documents contain
  `(Spirit*2)+History(Relevant)+3`; the code is `pool = spirit * 2` with the history addend deleted
  (`systems/fieldwork/sim/knots.py:216`, CR-85). Green.
- `tests/valoria/test_flow_skeletons.py` (726 lines) checks line anchors in twelve ARCHIVED-NOT-CANON
  documents that may not be edited, and carries 61 exemption strings in seven sets for the drift.
  `modules/mass_battle/terrain.py:269-270` keeps a constant below a lookup *"so the lookup's line stays
  where the mass-battle flow skeleton's line anchor cites it"*: the test has decided where code sits.
- **Falsifier.** §0.05's question, applied: delete either file and no game behaviour, exported
  parameter or Jordan decision changes. Neither artifact is read by `engine/` or `modules/`.
- **Fix.** `01_CORE_tests_delete_what_cannot_fail.md` rows 1–2.

### F-TEST-05 · R-07's named measure begins with a substring test, and the property it names is not the one enforced

- **Claim.** `test_choose_receives_no_world` asserts `"choose(p, v, s, ask_budget)" in src and
  "choose(w" not in src`. R-07's `measure:` (`requirements.yaml:1469`) selects it, two type-refusal tests
  on a hand-built `View`, one behaviour test with a control, and by accident
  `test_a_view_with_no_query_forms_no_effort`.
- **Probe** (headless world, seed 0, a spy chooser walking `gc.get_referents` from its arguments): a
  `World` is reachable from `v` (`View > <lambda> > cell`, the `odds` query) and from `ask_budget`
  (`<lambda> > cell > SeasonDriver`); not from `p` or `s`. `vars(v)` raises `Forbidden`. What is
  enforced, and tested well, is that a `View` refuses every attribute outside five slots and that no
  module under `decision/` can name `World` (AST walk with a population floor). "Receives no world" as
  a reference-level statement is false by design; as an access-level statement it is true and the
  substring is not what shows it.
- **Fix.** `01_CORE_tests_delete_what_cannot_fail.md` rows 3–4: delete the substring test; R-07's
  `measure:` names the tests that observe the property, including the one in which a false belief
  changes a decision.

### F-TEST-06 · the invariant sweep runs on a world with no office, and a test pins that

- `tests/valoria/test_season_invariant_sweep.py:55` asserts `"offices" in r["unexercised"] and
  "stance_rows" in r["unexercised"]`. Probe: headless world, 0 offices and 0 stance rows examined; built
  realm, 34 and 79 (0.7 s); played realm, every carrier examined, `unexercised == []`, 0 violations.
  The mutation half of the file is the best-built in the tree (every invariant has a planted defect and
  `test_every_invariant_has_a_mutation` asserts the mapping is total); its world is the weak part.
- **Fix.** `01_CORE_tests_shipped_world_falsifiers.md` row 4.

### F-TEST-07 · three loops that assert on whatever they are handed

- `test_march.py:348`, `:365`: `for pid in attackers: assert …` over `world_q.mustered(...)`. Mutation
  run (`probe_vacuity.py`): `mustered -> []`, both green. With the fold removed both redden, so they do
  observe the casualty model; they do not observe that anyone was mustered.
- `test_content_operands.py:278`: no count. Today 245,574 candidates, 194,714 carrying `to`; not
  vacuous now, unguarded against becoming so.
- Checked and sound: the other four all-conditional season tests iterate module constants;
  `test_scale_of_rung.py:55` and `test_strife_kinds.py:126` are does-not-raise tests paired with
  refusal tests.
- **Fix.** `01_CORE_tests_shipped_world_falsifiers.md` row 5.

### F-TEST-08 · the dice golden is 58 % rows the engine refuses or contradicts

- `engine/tests/goldens/sigma_leverage_parity.json`: 1,758 rows, current against its generator
  (`tools/gen_sigma_parity_goldens.py --check`, run). 768 are target-number 6 / 8 rows (one of each is
  exercised, as a `KeyError`); 255 are pre-ruling ladder rows checked as two counts (47 moved, 208
  kept) against `systems/social_contest/sim/contest/degree_extension.py`. 735 are live parity, at
  `1e-9` on transcendental functions and `==` on the rest, with no sampling in them: this golden can
  separate a regression from noise, because there is no noise.
- **Fix.** `01_CORE_tests_one_golden_owner.md` E.

### F-TEST-09 · eight tests assert a substring of source text and nothing else

Listed in §7 with what each cannot see. The clearest: `test_d10b_resolve_sums_then_clamps_once`
asserts the text `clamp ONCE`, which occurs once in `resolve`, in a trace message
(`loop/resolve.py:1197`). Each has a behaviour test beside it. **Fix.**
`01_CORE_tests_delete_what_cannot_fail.md` row 3.

### F-TEST-10 · a test that keeps a retired symbol importable; a standing non-strict `xfail`

- `tests/valoria/test_balance_oracle_arms.py:133` asserts `_ARMS_POOL` still imports and runs;
  `arms.py:267` calls it a retired comparison kept as a record.
- `tests/valoria/test_mass_battle_maneuvers.py:86`, `strict=False`. Run here: `XFAIL`; its reason
  records an `XPASS` in July. Neither is red.
- **Fix.** `01_CORE_tests_delete_what_cannot_fail.md` rows 5–6.

### F-TEST-11 · thirteen skips on an absent combat engine

Nine sites in `test_season_shape.py` (ten tests) and four other files. The W-E degree family exits 0
if `modules/combat` fails to import. The engine loads here. **Fix.**
`01_CORE_tests_shipped_world_falsifiers.md` row 6.

### F-TEST-12 · hygiene · tests kept green by reverting a shipped change; one escape hatch

`test_interactions_log.py` (two tests, `revert_cr87`: the fixture is a fight the shipped game no longer
produces); `test_in62_under_the_null…` (`revert_cp_t05_02`: on the shipped tree the null arm reads 10
`stance` deciders, so the titled claim is false without the revert, and the test's comment says so);
`test_m1_acceptance_probe.py:112` (`… or fixed.events == 0`). **Fix.**
`01_CORE_tests_shipped_world_falsifiers.md` rows 7–9.

## 3. R-01..R-09: the falsifier, and whether a test is it

| row | the falsifier (what would show the claimed behaviour wrong) | is a test that falsifier? | world · seeds · arm |
|---|---|---|---|
| R-01 decisions propagate | in computed play, no act is occasioned by a claim that walks back to another person's act; equivalently the count equals the count with WITNESS cut | **yes on the corpus, no on the realm.** `test_n3_…` (`r3_cases >= 16`, with an unrun world reading `False`) and `_w18_…` (`planted_control()` `False` → `True`) | corpus template · seed 0 · shipped. Realm probe: 134 / 141 / 162 against 0 |
| R-02 decisions affect later decisions | with what acts observe withheld, the later act sequence is unchanged | **yes, narrowly.** `test_wd_a_fork_…` (every arm `genuine > 0`, `total` arm `diverged > 0`, `bad_windows == 0`); `test_wb_a_refusals_reads_land_as_a_claim_…` (one person, hand-driven) | NPC-088 · seed 0 · budget 2 × 1, not the shipped 5 × 3. Realm probe: sequences part at 191 / 183 / 182 |
| R-03 seasons tick scene by scene | a deposit in round *n* leaves round *n+1*'s candidate set unchanged | **yes.** `test_u2_a_deposit_in_one_round_…` with a late plant and an unstamped plant as controls; `test_u2_the_inputs_fingerprint_is_complete_…` drops a fingerprint field and requires a violation | headless · seed 0 (fingerprint: 0, 1, 7, 13) · shipped |
| R-04 strategic and management acts | in a played season no seat-gated verb is chosen, admitted and executed | **no.** Governance tests fold hand-built acts; `test_march.py` reaches a field from a constructed `Question`; the `measure:` is a 25-minute instrument no test runs | `tiny_world`; realm build |
| R-05 all verbs built out | a verb in the never-attempted set executes, or an executed one stops | **yes, as a pin of `not_met`.** `ever`, `refused_only`, the never-attempted set, asserted as exact sets | corpus · seed 0 |
| R-06 robust characters | two persons differing only in pursuits choose alike | **at the mechanism, yes** (`test_in62_two_persons_one_question_…`, `test_t2_one_rebind_moves_score_and_gate`, both on synthetic persons or a planted projection). **In the realm, an existence claim:** `any("pursuit" in k …)` | realm build at tick 0 · seed 0 · one shipped change reverted. Probe: 265 pursuit, 223 draw, 10 stance of 498 |
| R-07 memory, feeling, attitude; imperfect knowledge | two persons hold the same things; or a false belief leaves a decision unchanged; or a changed attitude leaves it unchanged | **knowledge: yes** (`test_r7_two_persons_…` with the `total` arm as control; `test_wa_a_planted_claim_…`). **Feeling, attitude, relationship: no test.** The `measure:` leads with a substring (F-TEST-05) | `tiny_world` + planted cohort |
| R-08 not omniscient, not perfectly rational | at the shipped temperature every seed picks the top-scored candidate | **yes.** `test_u4_…` (20 draw seeds: at least two distinct tops at the shipped temperature, exactly one at 0); `test_the_planted_factor_of_one_reddens_the_difference` for believed odds | `tiny_world` · 20 seeds |
| R-09 probabilistic chains within a scene | one contested act yields one band whatever the draw; or two persons of different capability read the same odds | **first half yes** (`test_we_a_contested_acts_consequence_differs_by_degree`: all three bands over 24 act ids, with `total` and `none` harm arms; skips if the engine is absent). **Second half only with a planted pool** (`test_two_pools_give_two_believed_chances_…` monkeypatches `POOL_ADDENDS`) | `tiny_world` |

## 4. Family table

Counts from `family_table.txt`. `marked` = test names carrying `control`, `planted`, `mutation`,
`falsifier`, `revert`, `can_fail`. `src` = tests reading source or file text. Classification is the
dominant kind; **(scan)** marks a row classified from the instrument without reading the files.

| tree · family | files | tests | asserts | `raises` | marked | src | approx | skip | all-cond. | classification | weakest point |
|---|---|---|---|---|---|---|---|---|---|---|---|
| season · CORE | 27 | 514 | 1,919 | 93 | 59 | 40 | 1 | 8 | 1 | observes a behaviour, with controls; a tail of source-text and count pins | the corpus count pins; eight substring tests; skips |
| season · CHAR | 23 | 231 | 674 | 56 | 30 | 13 | 3 | 0 | 0 | observes a behaviour on synthetic persons and planted tables (read: two files; rest scan) | inputs are planted; realm claim is `any(…)` |
| season · PC | 15 | 176 | 490 | 18 | 42 | 3 | 2 | 0 | 0 | behaviour + mutation pairs; **the pre/post hash chain lives here** (scan + hash read) | revert stacks up to seven deep |
| season · MB | 10 | 113 | 407 | 17 | 38 | 1 | 2 | 0 | 0 | behaviour + control (scan) | — |
| season · SC | 15 | 140 | 506 | 25 | 14 | 7 | 2 | 0 | 1 | behaviour (scan; one flagged test read, sound) | — |
| season · FA | 22 | 335 | 1,188 | 71 | 27 | 6 | 0 | 0 | 2 | behaviour through hand-built acts (scan; two flagged tests read, sound) | R-04: nothing chosen in play |
| season · SE | 14 | 161 | 715 | 15 | 24 | 4 | 0 | 0 | 1 | behaviour + sweeps (scan; hash pins read) | hash pins in `test_season_weather.py` |
| season · FI | 11 | 153 | 632 | 13 | 24 | 3 | 0 | 2 | 0 | behaviour (scan; the two skips read: not taken today) | — |
| season · WR | 22 | 308 | 1,064 | 38 | 33 | 19 | 1 | 0 | 2 | behaviour + schema structure (scan; `test_march.py` flagged tests read) | F-TEST-07 |
| season · DICE, GO, CROSS | 3 | 49 | 157 | 3 | 6 | 0 | 1 | 0 | 0 | `test_go07…`: the encoding pinned to byte vectors (read) | its played-realm control is the reverted world |
| engine · dice (`band_odds`, `settle_margin`, `sigma_leverage_parity`) | 3 | 54 | 101 | 3 | 0 | 0 | 4 | 0 | 4 | exactness by enumeration against the closed form; a pure-function golden (read) | 1,023 dead golden rows |
| engine · `contest_kernel` | 1 | 1 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | pins a count (`passed == 389`) of an off-loop kernel's own checks (read) | subject retires with `05_SC_sc05_kernel_retirement.md` |
| engine · `knots`, `thread_mending` | 2 | 11 | 24 | 2 | 0 | 0 | 0 | 0 | 0 | behaviour of `systems/*/sim` oracles the loop does not call (read); each loop asserts it asserted | off-loop, by ED-IN-0283 retention; kept |
| valoria · CORE | 16 | 128 | 266 | 5 | 4 | 3 | 0 | 0 | 7 | asserts structure of registries and generated views (three read; rest scan) | loops over registry rows with no count |
| valoria · CROSS | 19 | 144 | 334 | 8 | 3 | 6 | 0 | 5 | 10 | mixed: the invariant sweep (strong), the m1 probe, **`test_flow_skeletons.py`** | F-TEST-04, F-TEST-06 |
| valoria · DICE | 8 | 42 | 98 | 3 | 1 | 1 | 3 | 0 | 6 | properties over sweeps (scan); `test_knot_pool_formula.py` read | F-TEST-04; `test_fractional_pool.py:39` a sampled mean at `abs=0.05` on a 0.2 quantity `[not adjudicated: DICE]` |
| valoria · MB | 33 | 351 | 820 | 25 | 4 | 2 | 35 | 3 | 7 | behaviour of `modules/mass_battle` (scan) | 35 tests use `approx`, some on conservation claims (`_conservation.py:99`) `[not adjudicated: MB]`; the standing `xfail` |
| valoria · PC | 17 | 164 | 465 | 5 | 2 | 4 | 14 | 0 | 10 | behaviour and byte-identity of `modules/combat` (scan) | ten all-conditional loops over weapon rosters `[not adjudicated: PC]` |
| valoria · CHAR, SE, WR | 7 | 41 | 98 | 4 | 3 | 2 | 4 | 0 | 0 | (scan) | — |

**Strongest.** (1) The gate family, `test_g1a` – `test_g4`: every refusal is run, every positive arm is
run beside it, the token scan plants four constructions and requires each to be caught, and
`test_g2_deliberate_mutates_no_store_by_any_route` digests the whole world before and after every
DELIBERATE across two worlds, then plants a mutation through a seated player and requires its own
assertion to fire. (2) `engine/tests/test_settle_margin.py` and `test_band_odds.py`: the closed form
is compared with a brute-force walk of the face table, cell by cell, with a count of cells.
(3) The mutation half of `tests/valoria/test_season_invariant_sweep.py`.

**Weakest.** `tests/valoria/test_knot_pool_formula.py`; `tests/valoria/test_flow_skeletons.py`; the
eight substring tests; the seven-deep revert stack.

**Approx on an exactness claim.** In the season tree, none that matters: twelve uses, nine of them
`sum == 1.0` at `1e-12` over float sums and three derived-expression equalities.
`test_cr21_cells.py:70-71` pins a measured `effective_axes` at `abs=0.01`, which is a tolerance on a
two-decimal reading and says so. The valoria MB and PC uses were not adjudicated.

**Tests of a retired thing.** `test_the_retired_pair_definitions_still_import` (F-TEST-10);
`test_flow_skeletons.py` and `test_knot_pool_formula.py` (archived documents); `test_contest_kernel.py`
and `TestPoolAwareDegree` (the kernel SC-P2 retires); the 1,023 superseded golden rows; the two
`test_interactions_log.py` tests whose fixture is a reverted fight.

## 5. The goldens, judged against `CLAUDE.md` §7

- **§7's sentence about `engine/tests/` is stale.** It says the seeded goldens there *"observe any
  output-moving change to campaign-reachable code"*. `engine/tests/goldens/` holds one file, a
  pure-function dice table; the campaign driver it once sat beside is deleted. The goldens that observe
  an output-moving change to the season loop are the hash literals under `engine/season/tests/`.
  Resolution T-22: the sentence is corrected to point there (an edit to `CLAUDE.md` is the
  orchestrator's; recorded here, carried by no proposal).
- **Which re-pins were declared movers.** Of the logs read, nearly all. Each re-record in
  `test_go07…` (25 entries, read by their `CONTROL` lines) and in the `by_sig` log of
  `test_season_shape.py` names the unit, the direction and a control whose revert reads the old value.
  The other six files' logs (`test_season_weather.py` 22 entries, five smaller) were counted, not read.
  Exceptions found: four re-records read off the failing assertion's printed figure, of which one
  (`133 -> 137`, the B10-13 batch pin) says its items were not isolated.
- **Which pins cannot separate noise from regression.** The corpus counts (F-TEST-03): a trajectory
  re-roll and a collapse of variety trip the same assertion, and the re-pin procedure is the same for
  both. The fork counts and chain depths, for the same reason. The hash pins cannot either, and do not
  claim to: they are tripwires, and the one that pins the shipped realm is the only one whose trip
  means the game moved.
- **Which can.** The dice golden's 735 live rows; the canonical-encoding vectors in `test_go07…`
  (`TENURE_VECTOR`, `WORLD_FRAMES`, the float bit patterns, the cross-`PYTHONHASHSEED` set order).
- **No golden supports a balance claim, and none is used as one.** The logs say *"A GOLDEN RE-RECORDED,
  NOT A BALANCE CLAIM"* 94 times across eight files. That discipline held.

## 6. Resolutions decided (22)

Ladder step: 1 superseded · 2 irrelevant · 3 design document · 4 precedent · 5 architecture.
Proposals (all under `../proposals/`): **T1** `01_CORE_tests_one_golden_owner.md` · **T2**
`01_CORE_tests_delete_what_cannot_fail.md` · **T3** `01_CORE_tests_shipped_world_falsifiers.md`.

| # | item | decided | step | carried by |
|---|---|---|---|---|
| T-01 | eight substring tests in `test_season_shape.py` | **delete**; a behaviour test already observes each | 5 | T2 row 3 |
| T-02 | `tests/valoria/test_flow_skeletons.py` | **delete**; subject is archived prose (§0.1 pt 5) | 2 | T2 row 2 |
| T-03 | `tests/valoria/test_knot_pool_formula.py` | **delete**; pins prose the code superseded (CR-85) | 1 | T2 row 1 |
| T-04 | `test_the_retired_pair_definitions_still_import`, `_ARMS_POOL`, `_pool_arm` | **delete**, symbol-level ledger note | 4 (`29b`, ledger `:2728`) | T2 row 5 |
| T-05 | R-07's `measure:` | **replace** the `-k` expression with six named tests | 5 | T2 row 4 |
| T-06 | `test_envelop_reaches_rear_node` (`xfail`, non-strict) | **replace** with a two-arm count over the same seeds | 5 | T2 row 6 (MB's file) |
| T-07 | dead `effect` helper | **delete** | 5 | T2 row 7 |
| T-08 | realm hash literals in 16 files | **replace** with one owner module; three shipped seeds | 4 (§0.05 cl. 3) | T1 A–B |
| T-09 | 17 revert-stacked hash controls | **delete** 15, cut the hash arm from 2; the proof lives in the commit | 3 (§0.1 pt 3, §2) | T1 C |
| T-10 | corpus and fork count pins; `total == 85`; duplicate `== 67` | **delete**; keep the property beside each | 5 | T1 D |
| T-11 | 1,023 superseded golden rows | **delete** at the generator; regenerate | 1 | T1 E |
| T-12 | kernel tests in `engine/tests` | **follow** `05_SC_sc05_kernel_retirement.md`; nothing separate | 1 | SC-P2 |
| T-13 | R-01 on the played realm | **strengthen**: new test, seeds 0–2, WITNESS-cut control | 5 | T3 row 1 |
| T-14 | R-02 at the shipped budget | **strengthen**: new test, seeds 0–2, same-seed control | 5 | T3 row 2 |
| T-15 | `test_wd_…_at_the_shipped_default` | **rename** `…_at_two_slots` | 5 | T3 row 3 |
| T-16 | invariant sweep's world | **strengthen**: add the played realm, `unexercised == []` | 5 | T3 row 4 |
| T-17 | three unguarded loops | **strengthen**: assert the population and the precondition | 4 (the valoria sibling) | T3 row 5 |
| T-18 | thirteen engine-absent skips | **replace** `skip` with `fail` | 4 (`test_a_missing_provider_is_a_boot_failure`) | T3 row 6 |
| T-19 | `test_interactions_log.py` reverted fixture | **replace** with a row of the shipped season | 5 | T3 row 7 |
| T-20 | `test_in62_under_the_null…` revert and `any(…)` | **strengthen**: key the self-plea apart; compare with the null | 3 (the test's own comment) | T3 row 8 |
| T-21 | `… or fixed.events == 0` | **strengthen**: assert events first | 5 | T3 row 9 |
| T-22 | `CLAUDE.md` §7's sentence on `engine/tests/` goldens | **correct** to name the season hash pins | 3 | orchestrator (Layer 0 edit) |

Kept on purpose, with the reason: the source-walk tests with a population floor and a plant (they
observe what they claim); the instrument-grader tests on planted series (`test_soak_grades.py`,
`test_loops_instrument.py`, `test_aperture.py`: a grader is tested on data whose answer is known);
the off-loop sim tests for knots and thread mending (retained subsystems' oracles); the set-identity
pins of R-05.

Nothing here survives to §11 of the parent audit. T-22 edits Layer 0 and is the orchestrator's to
make; it overwrites no ruling.

## 7. `engine/season/tests/test_season_shape.py` — the detail

**Observes a behaviour, with a control in the same test (the majority).** The write-gate refusals
(`d1b`, `d1c`, `d3b`, `d8`, `r3_the_l4_limb`, `w2_a_planted_write`, `w3_*`, `w4_every_matter_write`,
`the_partition_seam_is_bounded_by_causation`) call `World.write` with a wrong pair, class, driver or
cause and assert the exception type and text; the positive arm (`d3b`) asserts the write landed and
the Event is on the log. The sweep tests (`w6_h33s`, `w4_h40s`, `w9_h80s`, `w17_*`,
`wc_the_amount_sweep`, `wc_the_store_kind_sweep`, `wb_the_control_arm`, `we_a_contested_acts_consequence`)
run the loop at a zero arm, the shipped arm and a third and assert the arms differ in the ruled
direction: a deleted mechanism makes the arms equal. The register-rule tests (`w0_*`, `w1_*`, `g12`,
`id16`) load the committed register, assert it passes, plant a defect in a copy and assert the rule
fires. The taint check carries nine planted routers and a lawful control (`:7468-7513`).

**Asserts only structure — a substring of source text (eight).**

| test (`:line`) | asserted | cannot observe |
|---|---|---|
| `test_d10b_resolve_sums_then_clamps_once` (`:955`) | `"sum(deltas)" in src and "clamp ONCE" in src` | per-delta application with the trace message kept |
| `test_choose_receives_no_world` (`:1020`) | two substrings of `deliberate` | F-TEST-05 |
| `test_d2_witness_does_not_lie_about_its_driver` (`:221`) | `'driver="Event"'` present, `'driver="Act"'` absent, in a 682-line function | `driver=<variable>`; a write moved to a helper |
| `test_witness_writes_no_belief_and_no_pursuit` (`:1086`) | two `fieldname=` strings absent from `witness` | the same write from a helper |
| `test_d10c_the_obstacle_refusal_gate_exists` (`:960`) | a fixture name occurs in two sources | the gate removed, the name still read |
| `test_an_unfired_refusal_is_never_reported_as_a_pass` (`:1143`) | two words occur in `run_probe` | the branch that returns them |
| `test_unmapped_rows_are_never_silently_passed` (`:1202`), `test_an_unclear_row_is_not_counted_as_an_unrouted_one` (`:1207`) | a word occurs in `grade` | everything `grade` does |

**Source walks with a population floor and a plant (about thirty).** `w2_every_write_call_site`,
`jordan_no_definition_is_hardcoded`, `decision_package_never_names_world`,
`person_q_cannot_reach_the_world_side`, `w5_sense_is_still_*`, `w10_no_verdict_turns_on_the_text_of_a_need`,
`wc_no_operand_is_defaulted`, `u2_the_round_index`. Each asserts the walk saw something
(`len(mods) >= 8`, `inspected >= 5`, `resolved >= 3`, `scanned >= 5`). They observe imports and
signatures, which is their claim. They stand.

**Pins a count or a set off one seeded run.** `ever == {23 verbs}` (`:8164`), `refused_only == {13}`
(`:8418`), `len(by_sig) == 136` (`:9199`), `varying == {…}` (`:9425`), the never-attempted set
(`:9714`); `d_pub == 10` (`:4122`); `(depths[3], depths[6]) == (16, 14)` (`:6971`);
`(len(before), len(after)) == (20, 18)` (`:12366`); an eleven-tuple list containing hashed ids
(`:12713`); `len(dropped) == 18` (`:13580`); the fork counts (`:14829-15143`); the one-round arm's
event census (`:16649`); `total == 85` `raise SystemExit` statements (`:949`); `len(VERB_TABLE) == 67`
twice (`:2310`, `:15933`); `len(gov) == 20` (`:6384`). Between consecutive asserts of the corpus test
sit 400 to 700 lines of comment (`:7764` → `:8164`, `:8482` → `:9199`), which is the re-pin log.

**Skips.** Nine `if C.engine() is None: pytest.skip(...)` sites (`:9754`, `:9804`, `:9835`, `:9895`,
`:9932`, `:15637`, `:15708`, `:15735`, `:16148`), ten tests. `test_the_seam_calls_personal_combat…`
asserts `C.load_error()` is non-empty before skipping; the rest skip bare.

**A name that claims more than the test does.** `test_wd_a_fork_changes_a_later_decision_at_the_shipped_default`
(`:14260`) runs at `scene_budget 2 × interactions_per_scene 1` (`:14381`); shipped is 5 and 3.

## 8. Evidence log

All probes `PYTHONHASHSEED=0`, read-only, outputs under
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/CORE_C/`.
`git status --short` after the last probe: no path outside this suite's directory is modified.

| # | command or probe | outcome |
|---|---|---|
| 1 | `scan_tests.py` over the three trees | season 162 files / 2,180 tests / 7,752 asserts; engine 6 / 66; valoria 100 / 870. Season: 2 zero-assert, 7 all-conditional, 79 with an assert under `if`, 96 reading source text, 349 with `pytest.raises`, 374 with `monkeypatch` |
| 2 | line census (tokenizer + AST) | `test_season_shape.py`: 17,880 lines = 5,951 code, 7,818 comment, 2,846 docstring, 1,265 blank |
| 3 | `inspect.getsource` needles on `SeasonDriver.resolve`, `.deliberate`, `.witness` | `clamp ONCE` occurs once, in `chose=f"sum {deltas} = {total}, then clamp ONCE"`; `witness` is 682 lines |
| 4 | `DEFAULT_FIXTURES.get(...)` | `scene_budget` 5, `interactions_per_scene` 3, `fan_out_mode` `all_five`, `observation_deposit_mode` `actor`, `choice_temperature` 0.05; `combat.engine()` loads |
| 5 | `probe_hash_pins.py` | 28 tests in 16 files; 17 with a revert, at most 7; 51 literals, 11 in more than one file |
| 6 | `grep -c 'GOLDEN RE-RECORDED'` | 94 across eight files; `failing assertion's printed figure` 4, `not isolated one by one` 1, in `test_season_shape.py` |
| 7 | `probe_realm_sweep.py` (realm, seed 0, one season) | 7.3 s; 749 acts; 13,379 Events; hash `5ab73af282d0779646c38839fbab85d8`; sweep examines every carrier, 0 violations |
| 8 | `invariants.sweep` on `build_realm(0)` unplayed, and on the headless world | realm: 34 offices, 79 stance rows, 698 tenures, 0.7 s, clean; headless: 0 offices, 0 stance rows |
| 9 | `probe_vacuity.py` | `test_march` casualty tests: control green; `mustered -> []` both **green**; fold removed both red. `test_content_operands` loop: 245,574 candidates, 194,714 with `to`, 0 tuples |
| 10 | `decision_spread.read_decisions(build_realm(0))`, shipped and under `null_alignment()` | shipped `{pursuit: 265, draw: 223, stance: 10}`; null `{draw: 488, stance: 10}` |
| 11 | reachability probe (spy chooser, `gc.get_referents`) | `World` reachable from `v` and `ask_budget`, not from `p` or `s`; `vars(v)` raises `Forbidden` |
| 12 | `probe_realm_gates.py` (seeds 0, 1, 2) | occasioned by another's act: 134 / 749, 141 / 731, 162 / 751; `none` arm sequences part at 191, 183, 182; shipped hashes `5ab73af2…`, `aa58ef0b…`, `a21ab6e1…` |
| 13 | `probe_r01_control.py` (seed 0, WITNESS cut) | 0 of 388 |
| 14 | `python tools/gen_sigma_parity_goldens.py --check` | `current (1758 rows)`, exit 0; no file written |
| 15 | `python -m pytest tests/valoria/test_mass_battle_maneuvers.py tests/valoria/test_charge_momentum_impulse.py -q -p no:cacheprovider -rsxX` (the one pytest run) | 6 passed, 1 xfailed (`test_envelop_reaches_rear_node`); neither conditional skip taken |
| 16 | `grep` for importers of `degree_extension`, `sim.contest`, `sim.knots`, `threadwork.sim`, `engine_atlas` outside tests | no import under `engine/season/` or `modules/` for any; `arms.py`, `sigma_leverage.py`, `seam/wrappers/sigma.py` and `modules/social_contest/roll.py` name the kernel in docstrings and comments only |
| 17 | `test_fi03_trail.BLIND_BANDS` | `frozenset({'Partial'})`: its two skips are not taken |

Not run: the suite; any 4-season realm; the aperture instrument; the mutation in T2's falsifier for
`d10b` (marked `[UNVERIFIED]` there).
