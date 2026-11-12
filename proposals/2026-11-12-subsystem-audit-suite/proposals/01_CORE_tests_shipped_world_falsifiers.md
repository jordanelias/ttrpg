# CORE-T3 — falsifiers on the shipped realm, and the assertions that can pass on nothing

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` §4) — R-09's red-today falsifier (two persons of different capability read different odds with no monkeypatched addend) is the gate of `U5a_capability_home_and_two_inputs.md` Parts B and C.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.1 row T3 (CONFORMS), §6 row *749 acts*, §7 (COMPLETE except lands-it and tier), §7b-T; `unified/U3_CONFLICT_LEDGER.md` C3-N14, C3-N27; `unified/U3_DEPENDENCY_ORDER.md` node B02, §6.1, §6.2). Added: "749 acts" reads "749 folded acts (821 attempted)" (C3-N14); the four scratch probes the readings came from are not in the repository, and the readings are restated by the new test file itself (rows 1–2) and row 5's falsifier (U3 §6.2); `test_realm_requirements.py` is MISSING from the tree and is the batch's first commit (U3 §6.1); readings are `main`'s and move at B01 (C3-N27); lands-it and tier. No other change.

**Lands in batch:** B02 (hash EQUAL). **Depends on:** `01_CORE_requirements_reading_record.md` (B02; row 3's `reading:` field).

## Status: PROPOSED

Source: `audits/01_CORE_audit_addendum_C_tests.md` F-TEST-01, F-TEST-06, F-TEST-07, F-TEST-11,
F-TEST-12. Read at `785bc62`. Every reading below is from this audit's probes
(`scratchpad/runs/CORE_C/`, `PYTHONHASHSEED=0`); each edit re-reads its own.

## What it changes in `engine/season/` at runtime

Nothing in the loop. One harness edit (row 8: `harness/decision_spread.py` keys a self-plea apart from
an accusation), which changes an instrument's table and no world. The rest is tests.

## The problem (evidence)

1. **The suite's unit of evidence is a hand-built `Act` through `_fold` on `tiny_world`.** Of 2,180
   season tests, 316 call `_fold` / `resolve` / `encounter` directly, 192 build `P.tiny_world()`, 450 a
   file-local `_world()`. That is the right instrument for a refusal or an effect, and those tests are
   strong. It is not an observation that the property holds in computed play at the shipped
   configuration. For the rows of THE NINE, the tests that come nearest:

   | row | nearest executed falsifier | world · seeds · arm | what it leaves unobserved |
   |---|---|---|---|
   | R-01 | `test_n3_an_act_cites_what_occasioned_it…` (`r3_cases >= 16`); `_w18…` (`planted_control()` reads `False` then `True`) | corpus template worlds · seed 0 · shipped | the realm; any second seed |
   | R-02 | `test_wd_a_fork_changes_a_later_decision_at_the_shipped_default` | NPC-088 · seed 0 · `scene_budget 2 × interactions_per_scene 1` (shipped: 5 × 3) | the shipped budget, despite the name; the realm |
   | R-03 | `test_u2_*` (five tests; the plant, the late plant and the unstamped plant) | headless three-person world · seed 0 (fingerprint test: seeds 0, 1, 7, 13) | nothing material: the strongest of the nine |
   | R-04 | `test_march.py` (a real chooser reaching a field off a constructed `Question`); governance tests fold hand-built `confer` / `convene` / `dispatch` | realm build, unplayed; `tiny_world` | a seat-holder choosing a management verb in a played season; the row's `measure:` is a 25-minute instrument no test runs |
   | R-05 | the corpus set pins (`ever`, `refused_only`, the never-attempted set) | corpus · seed 0 | correct as a pin of `not_met` |
   | R-06 | `test_in62_under_the_null_every_realm_top_is_draw_or_tiebreak_and_the_shipped_reading_is_not` | realm build, tick 0 · seed 0 · with `revert_cp_t05_02` | asserts `any(…"pursuit"…)`: one decision in 498 would pass (probe: 265 pursuit, 223 draw, 10 stance); the null arm reads 10 `stance` deciders on the shipped tree, which is why the test reverts a shipped change |
   | R-07 | `test_r7_two_persons_hold_different_things_and_at_total_they_cannot`; `test_wa_a_planted_claim_removes_transfer_and_a_larger_one_leaves_it` | `tiny_world` + a planted cohort · its own seed | feeling, attitude or relationship changing a decision: no test by any name |
   | R-08 | `test_u4_the_choice_is_sampling_and_the_argmax_is_its_zero_temperature_control` | `tiny_world` · 20 draw seeds · shipped temperature and 0 | nothing material at the mechanism; share of non-top choices in play is unread |
   | R-09 | `test_we_a_contested_acts_consequence_differs_by_degree` (skips if the combat engine is absent) | `tiny_world` · 24 act ids | two persons separating by skill without a planted pool (`test_cr17…::test_two_pools…` monkeypatches `POOL_ADDENDS`) |

2. **A played realm season is cheap and nobody asserts on it.** `build_realm(0)` + one season: 7.3 s,
   749 folded acts (821 attempted; C3-N14), 13,379 Events (`probe_realm_sweep.py`; this and the probes
   below are scratch scripts not in the repository: the readings are `main`'s at the working tree, move at
   B01, and are re-read by the tests this file adds). Readings at seeds 0, 1, 2 (`probe_realm_gates.py`):
   acts whose scene was occasioned by a landed claim that walks back to **another person's act**: 134 of
   749, 141 of 731, 162 of 751. With `observation_deposit_mode` swept to `none`, the resolved sequence
   `(actor, verb, subject)` first differs at position 191, 183, 182. Control for the first
   (`probe_r01_control.py`, seed 0): with `SeasonDriver.witness` returning without depositing, the
   count is 0 of 388.
3. **The invariant sweep runs on a world with no office in it.**
   `tests/valoria/test_season_invariant_sweep.py::test_the_sweep_reports_rows_examined_not_predicates_offered`
   asserts `"offices" in r["unexercised"] and "stance_rows" in r["unexercised"]` (`:55`): on the
   headless world the sweep examines 0 offices and 0 stance rows, and the test pins that. So
   `office_singly_held` and `stance_row_shape` are checked against their planted mutation and against
   no world. Probe: over the built realm the sweep examines 34 offices, 79 stance rows, 698 tenures
   (0.7 s); over the played realm 13,379 Events and 12,351 claims as well, `unexercised == []`,
   0 violations.
4. **Three loops that assert on whatever they are handed.**
   `test_march.py::test_the_total_casualty_model_zeroes_the_losing_side` (`:348`) and
   `::test_the_none_casualty_model_writes_stance_only` (`:365`) iterate `world_q.mustered(...)` and
   assert per member. Probe (`probe_vacuity.py`): with `mustered` returning `[]` both are green.
   `tests/valoria/test_balance_oracle_arms.py::test_the_total_arm_actually_changes_the_casualty_write`
   runs the same fold and does assert `len(attackers) == 2` and `("field.lost", "Lost") in kinds`.
   `test_content_operands.py::test_no_writ_derived_operand_is_ever_a_raw_tuple` (`:278`) plays a realm
   season and asserts no candidate's `to` is a tuple, with no count; today the loop sees 245,574
   candidates, 194,714 carrying `to`.
5. **Thirteen skips on an absent combat engine.** `if C.engine() is None: pytest.skip(...)` at nine
   sites in `test_season_shape.py` (ten tests, through `_k1_combatants`), and in
   `test_combat_band_edges.py:51`, `test_cp_t03_04_arms.py:83`, `test_cr85_faculty_replaces_history.py:50`,
   `test_h206_a_death_at_matter_is_witnessed.py:162`. The whole W-E family (a contested act's
   consequence differs by degree) exits 0 if `modules/combat` fails to import. The engine loads here.
   The suite's own position is the opposite: `test_a_missing_provider_is_a_boot_failure`.
6. **Two tests kept green by reverting a shipped change.**
   `test_interactions_log.py::test_the_log_names_the_cardinals_fight_on_the_inquisitor` and
   `::test_a_planted_wrong_relation_reading_is_seen` call `revert_cr87` to reproduce a fight the shipped
   game no longer produces; `test_in62_under_the_null…` calls `revert_cp_t05_02` (item 1, R-06).
7. **An escape hatch.** `tests/valoria/test_m1_acceptance_probe.py::test_a_different_seed_can_diverge_from_the_probe_seed`
   asserts `(hash, hits) differ or fixed.events == 0` (`:112`): an empty season passes.

## The resolution (decided)

| # | edit | file (owner) |
|---|---|---|
| 1 | **R-01 on the played realm.** New test, parametrised over seeds 0, 1, 2: build the realm, play one season with `P.chooser(w, verbs=resolvable_verbs())`, count resolved acts whose scene's `occasion.source == "claim_landed"` and whose `occasioned_by(w, q)` Events have a cause that is an `Act` by a different person; assert the count is `> 0`. Control in the same test at seed 0: `monkeypatch.setattr(SeasonDriver, "witness", lambda self, token, events: 0)`, same count, assert `== 0`. | new `engine/season/tests/test_realm_requirements.py` |
| 2 | **R-02 on the played realm at the shipped budget.** Same file, seeds 0, 1, 2: play one season at `DEFAULT_FIXTURES` and one at `.sweep("observation_deposit_mode", "none")`; assert the two `(actor, verb, subject)` sequences differ and share a non-empty common prefix (the worlds start equal and part). Control: the same seed played twice at `DEFAULT_FIXTURES` gives equal sequences. | the same file |
| 3 | Rename `test_wd_a_fork_changes_a_later_decision_at_the_shipped_default` to `…_at_two_slots`; R-02's `measured:` reading names row 2 as the shipped-budget test. | `test_season_shape.py`; `engine/season/requirements.yaml` (with `01_CORE_requirements_reading_record.md`) |
| 4 | **The sweep sees a played realm.** In `test_the_engine_is_clean_under_the_sweep`, add a second sweep over `populated.build_realm(s)` played one season, seeds 0–2, asserting `not r["violations"]` and `r["unexercised"] == []`. The `:55` assertion (`"offices" in r["unexercised"]`) stays as a statement about the headless world. | `tests/valoria/test_season_invariant_sweep.py` |
| 5 | `test_march.py`: both casualty tests assert `len(attackers) == 2` and that the fold's kinds include `("field.lost", "Lost")`, the two lines the valoria sibling already has. `test_content_operands.py:278`: count candidates carrying `to` and `assert carried >= 1000` (a floor two orders below today's 194,714, the form `test_in62…` uses for `checked`). | `engine/season/tests/` |
| 6 | Every `pytest.skip(f"personal_combat engine unavailable: …")` becomes `pytest.fail(…)` (13 sites). | `engine/season/tests/` |
| 7 | `test_interactions_log.py`: the finding fixture stops naming two persons and a reverted fight. `_assert_finding` selects the first audited row of the shipped season whose candidate was chosen and whose verb declares `contests:`, and asserts the same six fields against the world (`same_faction` equals `world_q`'s reading for that pair, the question's claim id is in the actor's ledger, the candidate is the act). The planted wrong-relation test keeps its shape on that row. `revert_cr87` leaves the file. | `engine/season/tests/test_interactions_log.py` |
| 8 | `harness/decision_spread.py::read_decisions` keys a candidate on `(verb, subject, subject == actor)`, so a self-plea and an accusation are two rows; `test_in62_under_the_null…` drops `revert_cp_t05_02`, keeps `seen_null <= {"draw", "tiebreak"}`, and replaces `any("pursuit" …)` with a comparison against the null arm: the shipped reading attributes more tops to `pursuit` than the null arm does (the null's count is 0), at seeds 0, 1, 2. The test's own comment (`:264-271`) names this keying as what lifts the revert; `[UNVERIFIED: not built]` | `engine/season/harness/decision_spread.py`; `test_in62_decision_spread.py` |
| 9 | `test_a_different_seed_can_diverge…`: assert `fixed.events > 0` first, then the inequality with no `or`. | `tests/valoria/test_m1_acceptance_probe.py` |

Typed shape of the new file (rows 1 and 2), composing on existing owners only (`populated.build_realm`,
`probes.chooser`, `world_q.occasioned_by`, `SeasonDriver`):

```python
SEEDS = (0, 1, 2)

def _play(seed: int, fx: Fixtures | None = None) -> tuple[World, SeasonDriver]: ...
def _occasioned_by_another(w: World, d: SeasonDriver) -> int: ...
def _sequence(d: SeasonDriver) -> list[tuple[str, str, str | None]]: ...

@pytest.mark.parametrize("seed", SEEDS)
def test_r01_an_act_is_occasioned_by_a_claim_that_walks_back_to_another_persons_act(seed): ...
def test_r01_control_with_witness_cut_no_act_is_so_occasioned(monkeypatch): ...
@pytest.mark.parametrize("seed", SEEDS)
def test_r02_withholding_what_acts_observe_changes_later_acts_at_the_shipped_budget(seed): ...
def test_r02_control_one_seed_played_twice_is_one_sequence(): ...
```

About 80 s of test time (twelve realm seasons). The file is MISSING from the tree and is written as B02's
first commit (U3 §6.1): green at the base tree where the claim is a property that holds today (rows 1–2),
and red with the cause removed (the witness-cut and same-seed controls).

**Not written here, and where it goes.** R-04, R-06's magnitude, R-07's feeling/attitude half and R-09's
separation are red at the shipped configuration by the first audit's readings (F-CORE-04: skill is
empty on the cast; R-04's block: `found` / `build` execute 0 at seeds 0 and 1). A test that is red on
`main` is the gate of the proposal that makes it green, not a test to land now. The falsifiers, stated
so the owning lanes can carry them:

- R-04: in a played realm season, at least one act with a `remit:` eligibility is formed by the
  chooser, admitted and emits its row's kind. Gate of `06_FA_remit_grant_by_row.md` /
  `06_FA_decree_binds.md`.
- R-07 (attitude): two persons identical but for one `stance` row toward a third rank a candidate about
  that third differently in a played season, and equal when the row is removed. Gate of
  `02_CHAR_choice_alignment.md`.
- R-09: two persons with different shipped `capability` read different `sigma.odds_of` for one verb in
  the realm, with no monkeypatched addend. Gate of `10_DICE_advantage_sources_for_the_arcs.md` /
  `02_CHAR_capability_uses_table.md`.

## Gate (execution artifact)

`python -m pytest engine/season/tests/test_realm_requirements.py -q` green, six parametrised cases and
two controls; `python -m pytest tests/valoria/test_season_invariant_sweep.py -q` green with
`unexercised == []` on the realm arm; `python -m pytest engine/season/tests/test_march.py -q -k
casualty` green; `grep -c "engine unavailable" engine/season/tests/*.py` shows no `pytest.skip` on
those lines.

## Falsifier

Rows 1 and 2 carry theirs in the file (the witness-cut arm must read 0; the same-seed arm must read
equal). For row 4: plant `w.offices["x"]` held twice in the played realm; the sweep must report it. For
row 5: patch `world_q.mustered` to return `[]`; both `test_march` tests must now redden where today they
are green. For row 6: make `combat.engine()` return `None` in process; the W-E tests must fail, not
skip.

## NERS reading

- **N.** Rows 1, 2 and 4 are the only assertions in the tree about a played realm at the shipped
  configuration over more than one seed; removing them returns R-01 and R-02 to single-seed template
  readings. Holds top-down (THE NINE), bottom-up (composes on four existing owners), laterally (the
  same `_play` serves both rows), across scales (the realm is the largest world the tree builds). It
  does not hold diagonally into long arcs: one season says nothing about season six (F-CORE-01 is why
  that is expensive).
- **R.** Each new assertion has a control that removes the cause, not the result. No balance claim:
  the counts are asserted `> 0` against a control of exactly 0, and the numbers above are readings, not
  thresholds.
- **S.** The realm arm of the invariant sweep uses the sweep's own function unchanged; the R-rows reuse
  the corpus's `occasioned_by` reading, so the realm and the corpus are measured one way.
- **E (last).** One file of about 90 lines, nine small edits, thirteen one-word changes.

## Cost class

Small build (rows 1, 2, 7, 8); edit (the rest).

**Lands it and tier.** The B02 batch, an IN `valoria-author` session on `sonnet` (`high`), one commit per row,
closed by B02's `methodology-close` once. **Hash movers.** None (tests and one harness table).
