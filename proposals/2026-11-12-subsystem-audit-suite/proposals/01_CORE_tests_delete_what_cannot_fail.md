# CORE-T2 — delete the tests that cannot fail on a behaviour change

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.1 row T2 (CONFORMS), §7 (COMPLETE except lands-it and tier), §7b-T; `unified/U3_DEPENDENCY_ORDER.md` node B02, §5.1 serial edges on `requirements.yaml` and `test_season_shape.py`). Added: lands-it, tier, batch and the serial order on the two shared files; row 6 is marked for the MB lane's landing; the row-3 falsifier's `[UNVERIFIED: read, not run]` is made the batch's first step (this lane runs nothing). No other change.

**Lands in batch:** B02 (hash EQUAL). **Depends on:** nothing proposed. **Serial edges:** it edits `engine/season/requirements.yaml` and `engine/season/tests/test_season_shape.py` first in their serial orders (B02 → B03 → B09 → …; B02 → B11 → B12, U3 §5.1).

## Status: PROPOSED

Source: `audits/01_CORE_audit_addendum_C_tests.md` F-TEST-04, F-TEST-05, F-TEST-09, F-TEST-10. Read at
`785bc62`.

## What it changes in `engine/season/` at runtime

Nothing, with one exception that is a deletion of dead harness code: `_ARMS_POOL` and `_pool_arm` leave
`engine/season/harness/arms.py`, which `python -m engine.season.harness.arms` does not call (its
`main` reads `ARMS`, `arms.py:283`). One string in `engine/season/requirements.yaml` changes (R-07's
`measure:`).

## The problem (evidence)

1. **Two test files whose subject is archived prose.**
   - `tests/valoria/test_knot_pool_formula.py` (57 lines, three tests) opens three files under
     `.designs/` and asserts the text `(Spirit*2)+History(Relevant)+3` occurs in each (`:35-39`). The
     code reads `pool = spirit * 2   # CR-85 (ED-IN-0330): the history_relationships addend is DELETED`
     (`systems/fieldwork/sim/knots.py:216`). The test is green, and what it holds in place is three
     archived documents stating a formula the code stopped implementing.
   - `tests/valoria/test_flow_skeletons.py` (726 lines) checks that `` `path:line symbol` `` anchors in
     twelve `*_flow_skeleton_v1.md` files resolve against the tree. Every one of those files is under
     `.designs/` and opens *"ARCHIVED — NOT CANON … Do not edit it; do not treat it as current"*. The
     test's docstring says it *"rots on purpose: edit the traced code and the anchors drift"*; the
     documents may not be edited; so each drift is absorbed into an exemption set. There are seven
     (`RETIREMENT_SHIFTED` 13 strings, `RETIRED_SYMBOLS` 24, `RETIRED_CALL_SITES` 8, `RETIRED_GENERATED`
     6, `RETIRED_CONTRACTS` 3, `_CENSUS_SIDECARS` 6, `LINE_UNSTABLE_TARGETS` 1). Five of its tests carry
     a `pytest.skip` branch. The one consumer of the skeletons is `tools/build_engine_atlas.py`, whose
     outputs (`references/engine_atlas.json`, `ENGINE_ATLAS.md`) no file under `engine/` or `modules/`
     reads (`grep -rln engine_atlas --include=*.py`: tools, tests and one skill).
   Both are the case `CLAUDE.md` §0.1 pt 5 rules on: the guarded artifact is load-bearing on this
   repository's process only. §0.05's test — *if this were deleted, would the game behave differently?*
   — reads no for both.
2. **Eight tests that assert a substring of source text and nothing else**
   (`engine/season/tests/test_season_shape.py`): `test_d10b_resolve_sums_then_clamps_once` (`:955`;
   the string `clamp ONCE` occurs once in `resolve`, inside a trace message, `loop/resolve.py:1197`),
   `test_choose_receives_no_world` (`:1020`), `test_d2_witness_does_not_lie_about_its_driver` (`:221`),
   `test_witness_writes_no_belief_and_no_pursuit` (`:1086`), `test_d10c_the_obstacle_refusal_gate_exists`
   (`:960`), `test_an_unfired_refusal_is_never_reported_as_a_pass` (`:1143`),
   `test_unmapped_rows_are_never_silently_passed` (`:1202`),
   `test_an_unclear_row_is_not_counted_as_an_unrouted_one` (`:1207`). Each has a behaviour test that
   observes the property it names:

   | substring test | the behaviour test that already carries it |
   |---|---|
   | `d10b` | `test_in12_step9.py::test_a_sabotage_a_restore_cancels_is_refused_after_the_fact` (a `restore` and a `sabotage` of equal size on one fabric sum to 0 and both are refused; applied per delta, each would land and emit); `test_works_founding.py:281` (two restores folded in both orders end at one condition, which same-sign deltas would do under either rule, so it is the weaker of the two) |
   | `choose_receives_no_world` | `test_a_view_raises_on_any_world_collection`; `test_decision_package_never_names_world_anywhere_under_it`; `test_w5_sense_is_still_the_only_world_taking_non_decision_function`; `test_g2_deliberate_mutates_no_store_by_any_route` |
   | `d2`, `witness_writes_no_belief…` | `test_d1c_…` (a MATTER write to `Person.pursuits` refuses); `test_r3_the_l4_limb_is_actually_exercised`; `test_w2_every_write_call_site_names_a_pair_on_the_matrix` (AST, with a plant) |
   | `d10c` | `test_w4_a_refused_attempt_names_the_attempt_not_the_campaign_seed` |
   | the three `run_probe` / `grade` word tests | `test_playable_requires_that_every_core_row_was_actually_aimed_at`; `test_a_blocker_outranks_an_unaimed_row`; `test_no_probe_currently_returns_unreachable` |

   `test_choose_receives_no_world` is the first name in R-07's `measure:`
   (`engine/season/requirements.yaml:1469`). Probe (headless world, seed 0, a spy chooser walking
   `gc.get_referents` from its four arguments): a `World` is reachable from `v` (`View > <lambda> >
   cell`, the `odds` query) and from `ask_budget` (`<lambda> > cell > SeasonDriver`); it is not
   reachable from `p` or `s`. What the engine enforces is that a `View` refuses every attribute outside
   its five slots (`carriers.py:505`) and that no module under `decision/` can name `World`; the
   substring is not that.
3. **A test that keeps a retired symbol importable.**
   `tests/valoria/test_balance_oracle_arms.py::test_the_retired_pair_definitions_still_import` (`:133`)
   asserts `_ARMS_POOL` has two entries and that each runs. `arms.py:267` calls it *"Retired comparison,
   kept because `_pool_arm` is the record of what `roll_net_continuous` did"*. `CLAUDE.md` §1:
   retiring is deleting plus a `FORK:` row; kept-on-disk is not a state. The same file's two sibling
   pairs were deleted that way at `29b` (`references/restructure_ledger.md:2728`, symbol-level).
4. **A standing non-strict `xfail`.** `tests/valoria/test_mass_battle_maneuvers.py:86`
   (`test_envelop_reaches_rear_node`, `strict=False`). Run here: `XFAIL`. Its reason text records an
   `XPASS` on 2026-07-08 *"observed on ONE run"*. Neither outcome is red.
5. **A dead helper.** `test_r3_witness_fans_to_everyone_as_specified` (`test_season_shape.py:1469-1470`)
   defines `effect` and never passes it.

## The resolution (decided)

| # | edit | owner |
|---|---|---|
| 1 | delete `tests/valoria/test_knot_pool_formula.py` | `tests/valoria/` |
| 2 | delete `tests/valoria/test_flow_skeletons.py`; in `modules/mass_battle/terrain.py:269-270` delete the comment sentence that says `WALLS_DEFENDER_DR` is kept below the lookup so a skeleton's line anchor stays put (a constant's position in a module should not be decided by an archived document's line number). `tools/build_engine_atlas.py` is left as it is: its output is reference, and an unguarded reference that can be wrong without cost is the accepted state (§0.1 pt 5) | `tests/valoria/`, `modules/mass_battle/terrain.py` |
| 3 | delete the eight substring tests named above from `test_season_shape.py` | `engine/season/tests/` |
| 4 | R-07's `measure:` becomes `python -m pytest engine/season/tests -k 'a_view_raises or a_view_is_capped or r7_two_persons or wa_a_planted_claim or decision_package_never_names_world or another_modules_prize_and_a_foreign_actor'` (the last two are the type half and the query half; `wa_a_planted_claim` is the test in which a person holding a false belief about a granary declines `transfer` while the world holds the grain). The current `-k a_view` also selects `test_a_view_with_no_query_forms_no_effort` (`test_cp_t01_05_npc_effort.py`), which is about effort; the tightened expression does not | `engine/season/requirements.yaml` |
| 5 | delete `test_the_retired_pair_definitions_still_import`; delete `_ARMS_POOL`, `_pool_arm` and the `# noqa: F401 (kept for _pool_arm)` import note in `engine/season/harness/arms.py`; add a symbol-level sentence to the existing `engine/season/harness/arms.py` row in `references/restructure_ledger.md` (the `29b` precedent, same row) | `tests/valoria/`, `engine/season/harness/arms.py`, the ledger |
| 6 | `test_envelop_reaches_rear_node`: remove the `xfail` and replace the single-fixture pass/fail with a two-arm count over the same twenty seeds its reason text already cites: the detachment ordered to envelop reaches behind the defender in strictly more seeds than the same detachment ordered to hold, and the hold arm reaches it in none. A direction with a control, no threshold invented. If the envelop arm does not beat the hold arm, the test is red and the mechanism is the finding | `tests/valoria/test_mass_battle_maneuvers.py` (MB lane's file; the edit is theirs to land) |
| 7 | delete the unused `effect` in `test_r3_witness_fans_to_everyone_as_specified` | `engine/season/tests/` |

Not deleted, and why: the thirty-odd source-walk tests that go through `ast` or a tokenizer
(`test_w2_every_write_call_site…`, `test_jordan_no_definition_is_hardcoded_in_a_body`,
`test_decision_package_never_names_world…`, `test_person_q_cannot_reach_the_world_side`,
`test_w10_no_verdict_turns_on_the_text_of_a_need`, `test_g2_token_is_constructed_in_loop_driver_only`).
Each asserts its walk saw a minimum population and most plant a violating snippet and assert it is
caught. What they claim is a fact about imports and signatures, and that is what they observe.

## Gate (execution artifact)

`python -m engine.season.harness.register --requirements` exits 0 (it checks that every name in a
`measure:` resolves); `python -m pytest engine/season/tests -k '<the new R-07 expression>' -q` collects
six tests and passes; `python -m pytest engine/season/tests/test_season_shape.py -q` green;
`python -m engine.season.harness.arms --n 1 --seasons 1` runs; `git ls-files tests/valoria | grep -c
'flow_skeletons\|knot_pool_formula'` reads 0.

## Falsifier

For row 3, the mutation each substring test could not see must be seen by its named successor: in
process, apply each staged delta as its own clamped write in `loop/resolve.py` and keep the trace
string; `test_a_sabotage_a_restore_cancels_is_refused_after_the_fact` must redden (it would read
`site.restored` and `site.damaged`). `[UNVERIFIED: read, not run]` — the batch's first step runs this
mutation and records the outcome in the commit body before row 3 deletes anything. If it does not, `d10b`'s deletion is
wrong and that test gains a mixed-sign case at the ceiling (a `restore` of more than the headroom and a
`sabotage`, folded in both orders, one end condition). For row 4: delete `View.__getattr__`'s refusal
in process; `a_view_raises` must redden.

## NERS reading

- **N.** Each deleted test fails the removal question from every direction tried: bottom-up (no code
  path depends on it), top-down (no R-row is read through it once R-07 is re-pointed), laterally (a
  sibling test observes the property), across time (two of them now hold stale prose in place).
- **R.** Completeness improves at one point: R-07's measure gains the one test in which imperfect
  knowledge changes a decision. It does not gain a test of feeling, attitude or relationship changing
  one; none exists under that name, and that gap is CHAR's (`audits/02_CHAR_audit.md`), recorded in
  the addendum's R-row table, not papered over here.
- **S.** One way to state "the chooser cannot read the world" (the type and the import walk) where
  there were two.
- **E (last).** About 800 test lines, seven exemption sets and one retired harness pair leave; nothing
  arrives except one edited string.

## Cost class

Edit.

**Lands it and tier.** The B02 batch, an IN `valoria-author` session on `sonnet` (`high`), one commit per row
of the table, closed by B02's `methodology-close` once. Row 6 is the MB lane's file
(`tests/valoria/test_mass_battle_maneuvers.py`): it lands in B02 only with that lane's agreement, else in the
MB lane's first batch (B17). **Hash movers.** None.
