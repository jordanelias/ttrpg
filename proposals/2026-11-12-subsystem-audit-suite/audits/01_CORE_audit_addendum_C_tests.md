# CORE — addendum C: test strength

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 785bc62 (working tree)

Addendum to `01_CORE_audit.md`, whose §4 says of the tests: *"43 test files were listed for this lane;
none was opened"*. This file is that reading. Question asked of every test file or family: **what
failure can its assertions observe, and what failure could they not** (`CLAUDE.md` §0.1 pts 2–4).

## 0. Verdict

*(written first, revised as the reading proceeded; the final text is below the census)*

## 1. Method and census

Three trees were in scope: `engine/season/tests/` (162 test files, 2,180 test functions, 7,752 `assert`
statements, 71,169 lines of which 37,220 are code, 12,478 comment and 11,891 docstring),
`engine/tests/` (6 files, 66 functions, 1,301 lines) and the `tests/valoria/` files the dossiers list
(100 files scanned, 870 functions). Counts are from an AST pass
(`scratchpad/runs/CORE_C/scan_tests.py`; per-test rows in `season_tests.tsv`, `engine_tests.tsv`,
`valoria_tests.tsv`), which records for each test function: asserts, asserts under an `if`, asserts under
a non-literal loop, `pytest.raises` blocks, asserts inside same-file helpers, `approx`/`isclose`, pinned
hex or large-integer literals, source-text reads (`inspect.getsource`, `read_text`, `ast.parse`),
skips, and `monkeypatch` use. The pass classifies nothing by itself; it says where to read.

Reading was done on a comment- and docstring-stripped view with original line numbers
(`scratchpad/runs/CORE_C/strip.py`), because 60 % of `test_season_shape.py` (10,664 of 17,880 lines) is
comment or docstring and the question here is what the assertions can observe, which only the code
answers. §9 lists what was read in full, what was read at the flagged tests only, and what was not read.

## 2. `engine/season/tests/test_season_shape.py` — read in full (225 tests, 940 asserts)

The file is the season loop's original acceptance suite. Read whole on the stripped view (4,806 code
lines of 17,880). What its assertions can and cannot observe, by kind:

**Observes a behaviour, with a control in the same test (the majority, and the strong part).** The
write-gate refusals (`d1b`, `d1c`, `d3b`, `d8`, `r3_the_l4_limb`, `w2_a_planted_write`, `w3_*`,
`w4_every_matter_write`, `the_partition_seam_is_bounded_by_causation`) call `World.write` with a wrong
pair, class, driver or cause and assert the exception type and its text; the positive arm (`d3b`) asserts
the write landed and the Event is on the log. The sweep tests (`w6_h33s`, `w4_h40s`, `w9_h80s`, `w17_*`,
`wc_the_amount_sweep`, `wc_the_store_kind_sweep`, `wb_the_control_arm`, `we_a_contested_acts_consequence`)
run the loop at a zero arm, a shipped arm and a third arm and assert the arms differ in the ruled
direction: a deleted mechanism makes the arms equal and the test red. The register-rule tests
(`w0_*`, `w1_*`, `g12`, `id16`) load the committed register, assert it passes, then plant a defect in a
copy and assert the rule fires. The taint check carries nine planted routers and a lawful control
(`:7468-7513`). This is the house pattern and it is sound: 297 of the tree's 2,180 test names carry
`control`, `planted`, `mutation`, `falsifier`, `revert` or `can_fail`, across 114 of 162 files.

**Asserts only structure — a substring of source text.** Eight tests assert nothing but that a string
occurs, or does not, in `inspect.getsource(...)`:

| test (`:line`) | what is asserted | what it cannot observe |
|---|---|---|
| `test_d10b_resolve_sums_then_clamps_once` (`:955`) | `"sum(deltas)" in src and "clamp ONCE" in src` | `clamp ONCE` occurs once in `resolve`, inside a trace message (`loop/resolve.py:1197`, `chose=f"sum {deltas} = {total}, then clamp ONCE"`). Clamp per delta, keep the message: green |
| `test_choose_receives_no_world` (`:1020`) | `"choose(p, v, s, ask_budget)" in src and "choose(w" not in src`; `"sense(p, w)" in src` | a world handed in through `v`, `s`, a closure or a renamed local; **named by R-07's `measure:`** |
| `test_d2_witness_does_not_lie_about_its_driver` (`:221`) | `'driver="Event"' in src and 'driver="Act"' not in src` over a 682-line function | `driver=kind_var`; a write moved to a helper |
| `test_witness_writes_no_belief_and_no_pursuit` (`:1086`) | `'fieldname="beliefs"'`, `'fieldname="pursuits"'` absent from `witness` | the same write made from a helper `witness` calls |
| `test_d10c_the_obstacle_refusal_gate_exists` (`:960`) | the fixture name occurs in loop source and fixtures source | the gate deleted while the name is still read |
| `test_an_unfired_refusal_is_never_reported_as_a_pass` (`:1143`) | `"UNREACHABLE"` and `"NOT-REFUSED"` occur in `run_probe` | the branch that returns them |
| `test_unmapped_rows_are_never_silently_passed` (`:1202`), `test_an_unclear_row_is_not_counted_as_an_unrouted_one` (`:1207`) | a word occurs in `R.grade` | everything `grade` does |

Each has a behaviour test beside it that already observes the property (`d1c` and `w3_the_write_class_check`
for the driver; `w8_work_emits_a_success_only_when_the_site_moves` for the accumulator, though not for
order independence; `w4_a_refused_attempt` for the obstacle gate; `test_playable_requires_*` and
`test_a_blocker_outranks_*` for `grade`). The substring tests are therefore duplicates that can only
fail on a rename. Resolution: §6 row T-01.

**Source-walk tests with a vacuity guard and a planted control.** Thirty more read source through `ast`
or a tokenizer (`w2_every_write_call_site`, `jordan_no_definition_is_hardcoded`,
`decision_package_never_names_world`, `person_q_cannot_reach_the_world_side`, `w5_sense_is_still_*`,
`w10_no_verdict_turns_on_the_text_of_a_need`, `wc_no_operand_is_defaulted`, `u2_the_round_index`). These
are structure tests of a different grade: each asserts the walk saw something (`len(mods) >= 8`,
`inspected >= 5`, `resolved >= 3`, `scanned >= 5`) and most plant a violating snippet and assert it is
caught. What they observe is an import or a signature, which is the claim they make (the decision
package cannot name `World`). They stand. They are the type-level half of R-07 and they are the half
that works.

**Pins a count or a set off one seeded run.** The corpus tests carry the suite's goldens as literals in
asserts: `ever == {23 verbs}` (`:8164`), `refused_only == {13}` (`:8418`), `len(by_sig) == 136` (`:9199`),
`varying == {...}` (`:9425`), the thirty never-attempted verbs (`:9714`); `d_pub == 10` (`:4122`);
`(depths[3], depths[6]) == (16, 14)` (`:6971`); `(len(before), len(after)) == (20, 18)` (`:12366`); an
eleven-tuple list containing hashed ids (`:12713`); `len(dropped) == 18` (`:13580`); the fork counts
`(31, 3)`, `(28, 2)`, `(28, 2)` and `{none: (10, 31), actor: (6, 28), total: (6, 28)}` (`:14829-15143`);
the one-round arm's event census (`:16649`); `total == 85` `raise SystemExit` statements (`:949`);
`len(VERB_TABLE) == 67` twice (`:2310`, `:15933`); `len(gov) == 20` (`:6384`). Every one is read at
seed 0. Judgement in §5.

**Skips.** Eight tests begin `if C.engine() is None: pytest.skip(...)` (`:9752`, `:9803`, `:9834`,
`:9894`, `:9931`, `:15636`, `:15707`, `:15734`, `:16147`): the whole W-E degree family (a contested
act's consequence differs by degree) reports nothing, and exits 0, if `modules/combat` fails to load.
Probe here: the engine loads (`C.engine() is not None`, §8). `test_the_seam_calls_personal_combat`
asserts `C.load_error()` is non-empty before skipping; the others skip bare.

**A name that claims more than the test does.** `test_wd_a_fork_changes_a_later_decision_at_the_shipped_default`
(`:14260`) runs at `scene_budget 2 × interactions_per_scene 1` (`:14381`); the shipped fixtures are 5 and
3 (probe, §8). It is the suite's only executable form of R-02 and it does observe the property
(`got["total"]["diverged"] > 0`, and every arm has `genuine > 0` with `bad_windows == 0`), at one case
(NPC-088), one seed, four seasons, a non-shipped budget.

**A dead helper.** `test_r3_witness_fans_to_everyone_as_specified` (`:1458`) defines `effect(w, a)` and
never passes it; the assertion is `deposits >= len(w.persons)` on a `speak` act. Harmless.
