# CORE-T1 — one owner for the realm goldens; the shipped world is what is pinned

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-13) — lands first among the hash movers, so each later mover re-records one file. E (the dice golden) is superseded in content by A-5: the golden is regenerated for the functions that remain after the whole-dice roll is deleted (`U5a_DICE_owed_edits.md` §1 row 8), not trimmed to 735 rows. D's kept pin `len(VERB_TABLE) == 67` is re-recorded by the commit that splits `tie / knot` (A-28).

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.1 row T1, §2 row literals/item D, §6 rows *749 acts*, *regime_gain control*, §7, §7b-T; `unified/U3_CONFLICT_LEDGER.md` C3-N14, C3-N27, C3-N30; `unified/U3_DEPENDENCY_ORDER.md` node B02, §6.2). Changed: item E's body is replaced by the head's sentence (A-5: regenerate the golden for the functions that remain; no "735 rows", no TN-7-only emit); the literals are named as `main`'s readings, which move at B01 (lane A's rebase) and again with A-5 (B05), A-9 (B08) and A-30 (B06) — this file lands first (B02) so each re-pin is one edit (C3-N27); item D's verb-roster pin is a reading quoted with its batch, re-read at B25 and B38 (C3-N30); "749 acts" is "749 folded acts (821 attempted)" (C3-N14); each pin's arm (control or shipped) is stated; the two scratch probes are replaced by the go07 test itself; lands-it and tier added.

**Lands in batch:** B02, first among the hash movers' prerequisites. **Depends on:** B01 (lane A rebased; its re-recorded pins are discarded and re-read on the working tree, C3-A2).

## Status: PROPOSED

Source: `audits/01_CORE_audit_addendum_C_tests.md` F-TEST-02, F-TEST-03, F-TEST-08. Read at `785bc62`.

## What it changes in `engine/season/` at runtime

Nothing. Every edit is under `engine/season/tests/`, `engine/tests/` and `tools/gen_sigma_parity_goldens.py`.
The content hash of every world is stationary.

## The problem (evidence)

1. **One trajectory, six copies.** The hash of `build_realm(0)` (`600d8b27…`) is written as a literal
   in six test files, and the hash of the realm after one season at seed 0 with `regime_gain` at 0
   (`25660615…`) in six (`test_go07_canonical_digest.py:658`, `test_cp_t02_06_continuations.py:72`,
   `test_season_weather.py:548`, `test_cp_t03_08_tend_on_the_wounded.py:50`,
   `test_rem30_character_sheet.py:71`, `test_strife_flows.py:857`). Of 51 distinct hash literals in
   `engine/season/tests`, 11 sit in more than one file. Each literal's trailing comment is its re-pin
   log: `# B10-13 batch pin commit: was d4c83c8c...; CP-T03-08: was eb2919ae...; CP-T03-07: was
   b2dde1fc...; CP-T03-04: was 20accb03...` — four re-pins in one batch, each made in every copy.
2. **Twenty of the 28 hash tests read a world nobody plays.** 28 tests in 16 files compare a
   `content_hash()` with a literal. 17 of them first call one to seven `revert_*` helpers
   (`test_cp_t03_01_cohorts_never_fight.py::test_control_the_realm_ends_at_the_base_hash_wherever_no_cohort_was_a_party`
   calls seven: `revert_cp_t03_02`, `_04`, `_07`, `_08`, `revert_cr79`, `revert_cr85`, `revert_cr87`),
   so the hash they pin is the hash of the tree as it stood several items ago, reproduced in process.
   Three more pin a withheld or switched-off arm.
3. **One literal pins the shipped played realm.** `test_strife_credit.py:41`
   (`5ab73af282d0779646c38839fbab85d8`, seed 0, one season: the **shipped** arm; the six copies of
   `25660615…` in item 1 are the **`regime_gain = 0` control** arm). Probe (`probe_realm_sweep.py`, a scratch
   script not in the repository, `PYTHONHASHSEED=0`): `build_realm(0)` + `populated.run(1, 0)` reads that
   value, 749 folded acts (821 attempted, `audits/25_GROUNDING_ENGINE.md` L-18; C3-N14), 13,379 Events, in
   7.3 s. Seeds 1 and 2 at the shipped configuration read `aa58ef0b…` and `a21ab6e1…`
   (`probe_realm_gates.py`), which are pinned only as the `regime_gain = 0` control and happen to
   equal the shipped reading there.
4. **The count pins are a second, coarser tripwire over the same runs.**
   `test_season_shape.py::test_the_corpus_runs_and_the_ranking_cannot_discriminate` asserts
   `len(by_sig) == 136` (`:9199`) under a comment log of every re-record. The log's own entries describe
   trajectory re-rolls: *"134 -> 133 … `arms` in the vocation range gives every `train` formation one
   more Candidate (nobody holds the key, so none lands …); the draws walk another trajectory"*. Four
   entries say the new figure was read off the failing assertion; one says *"The batch's items were not
   isolated one by one [ASSUMPTION; low …]"* (`:9184-9188`). Beside each count stands an assertion of
   the property the count is a proxy for (`universal == set()`, `ever == {…}`, `refused_only == {…}`).
5. **The dice golden is 58 % rows the engine refuses or contradicts.**
   `engine/tests/goldens/sigma_leverage_parity.json` holds 1,758 rows
   (`tools/gen_sigma_parity_goldens.py --check`: `current (1758 rows)`). 768 are target-number 6 and 8
   rows the engine raises `KeyError` on by ruling; 255 are `groundup/degree` rows on the pre-ruling
   ladder, checked only as `len(moved) == 47 and len(kept) == 208` against
   `systems/social_contest/sim/contest/degree_extension.py`, which the season loop does not import and
   which `05_SC_sc05_kernel_retirement.md` deletes. 735 rows are live parity.

## The resolution (decided)

**A. One owner.** New file `engine/season/tests/_realm_goldens.py` (a test-support module beside
`_scar_helpers.py`, not a registry: nothing but tests reads it):

```python
"""The realm goldens: one literal per (seed, seasons, arm). Every hash test imports from here.
A re-record is one edit to this file, in the commit that moves the world, with the mover named in
that commit's message (CLAUDE.md §7)."""
BUILD = {0: "600d8b27147478e158553552cc1409a5"}                      # build_realm(seed), unplayed
SHIPPED = {(0, 1): "5ab73af282d0779646c38839fbab85d8",                # (seed, seasons) at DEFAULT_FIXTURES
           (1, 1): "aa58ef0b71c947ce5ff9f0a75ffd8ca6",
           (2, 1): "a21ab6e12e356ccc4261bec1c93ca3b4"}
CENSUS = {(0, 1): dict(acts=749, log=13379), ...}                      # read with populated.run
```

Seeds 1 and 2 are re-read at the edit (the values above are this audit's probe, readings of `main` at the
working tree; the edit records its own on its base). Every literal here is `main`'s reading and moves at
B01 (lane A's rebase re-records the pins, C3-A2, C3-N27), then once each with A-5 (the one sampler, B05),
A-30 (the keyed draw, B06) and A-9 (the scene order, B08); because this file lands first, each of those
re-pins is one edit to `_realm_goldens.py`. The scratch probes `probe_realm_sweep.py` and
`probe_realm_gates.py` are not needed: the go07 test (B) runs `build_realm(s)` + `populated.run(1, s)` and is
the instrument (U3 §6.2).

**B. One test owns the shipped pin.** `test_go07_canonical_digest.py::test_go07_control_the_world_did_not_move_only_its_digest`
drops `revert_cr79(monkeypatch)` and its `BASE` block and asserts `SHIPPED` and `CENSUS` at the three
seeds. `test_go07_control_the_build_world_old_digest_is_unmoved` keeps one assertion,
`build_realm(0).content_hash() == BUILD[0]`. The `_old_content_hash` half of both (the pre-GO-07
`repr` digest) and the `foreign=False` / `acquaintances=False` build variants are deleted: GO-07 landed,
and a digest format nobody computes is not a control for anything that can still move. The four
encoding-vector tests in that file (`TENURE_VECTOR`, `WORLD_FRAMES`, float bit patterns, set order
across `PYTHONHASHSEED`) stay untouched; they pin the canonical encoding, not a trajectory, and are the
strongest hash tests in the tree.

**C. The revert-stacked controls are deleted** (15 tests deleted, the hash arm cut from 2 more; the
item's own behaviour and mutation tests in the same files stay):

| file | test deleted | literals deleted |
|---|---|---|
| `test_cp_t02_06_continuations.py` | `test_no_death_means_no_behaviour_change_and_the_realm_hash_is_the_pre_build_hash` | `PRE_BUILD` |
| `test_cp_t03_01_cohorts_never_fight.py` | `test_control_the_realm_ends_at_the_base_hash_wherever_no_cohort_was_a_party`, `test_where_a_cohort_was_a_party_the_realm_moves_and_the_refusals_are_the_conjuncts` (hash arm only; the refusal-conjunct asserts stay) | `BASE` |
| `test_cp_t03_02_band_ending_and_body.py` | `test_control_the_item_at_its_revert_reproduces_the_pre_item_one_season_hash` | `PRE_ITEM` |
| `test_cp_t03_04_arms.py` | `test_control_formation_moves_every_hash_and_the_item_off_reproduces_the_pre_item_hash` | `PRE_ITEM`, `POST_ITEM` |
| `test_cp_t03_07_body_ceiling.py` | `test_hash_post_item_control_and_revert`, `test_build_hash_is_a_schema_mover_and_the_revert_reads_the_old_one` | `PRE_ITEM`, `POST_ITEM`, `CONTROL`, `BUILD_PRE`, `BUILD_POST` |
| `test_cp_t03_08_tend_on_the_wounded.py` | `test_hash_post_item_and_revert`, `test_build_hash_is_unmoved` | `POST_ITEM`, `BUILD` |
| `test_cr33_lifepaths.py` | `test_control_the_expansion_skipped_reproduces_the_pre_commit_hash` | the three-seed block |
| `test_cr85_faculty_replaces_history.py` | `test_control_faculty_3_for_every_party_reproduces_the_pre_item_hash`; the hash arm of `test_falsifier_every_season_roll_reads_pool_8_against_ob_1` | `PRE_ITEM`, `POST_ITEM` |
| `test_cr87_violence_contexts.py` | `test_control_the_block_empty_and_every_value_at_its_revert_reproduce_the_pre_item_hash` | `BASE_BUILD`, `BASE_SEASON` |
| `test_rem30_character_sheet.py` | `test_rem30_creation_arm_off_reproduces_the_pre_build_hash` | the three-seed block |
| `test_season_weather.py` | `test_in21_control_draw_off_and_draw_at_one_reproduce_the_base_hashes`, `test_the_give_withheld_arm_reproduces_the_one_season_pin` | `BASE_HASHES`, `STEP_OFF_ONE_SEASON`, `BASE_EVENTS` |
| `test_strife_flows.py` | `test_cr78_control_the_switch_off_reproduces_the_base_hash` | `BASE_BUILD`, `BASE_ONE_SEASON` |
| `test_cp_t04_07_surrender.py`, `test_cr81_realm_acquaintances.py`, `test_strife_credit.py` | none deleted; each imports `BUILD` / `SHIPPED` from the owner in place of its literal | their copies |

A `revert_*` helper with no remaining caller is deleted with its last caller; one still used by a
behaviour test (`revert_cr87` in `test_interactions_log.py`, until CORE-T3 row 7 lands) stays.

**The rule this leaves** (a sentence in `_realm_goldens.py`'s docstring, binding a reader, not a
program): *an item that moves the realm proves in its own commit that its revert reads the previous
pin, and records that in the commit message; the proof is not kept as a test.* That is §0.1 pt 3 as
written (the falsifier and its outcome in the same commit) and §2 (*"the commit is their record"*).

**D. The corpus counts go; the properties beside them stay.** In `test_season_shape.py` delete the
exact pins and the comment logs that exist only to narrate them, keeping the assertion named in the
right-hand column, which is already there:

| deleted | kept beside it |
|---|---|
| `len(by_sig) == 136` (`:9199`) | `universal == set()`; `ever == {…}`; `refused_only == {…}`; the never-attempted set (R-05's state, exactly) |
| `d_pub == 10` (`:4122`) | `d >= 4`; `redeposits == 1`; no late `ROOT`; the chain's origin is hers |
| `(depths[3], depths[6]) == (16, 14)` (`:6971`); the `== 10` in `max(depth5…) == 10 < depths[3]` (`:7040`) | `matured[0] == 0`; `matured[3] < matured[6]`; `depths[3] > depths[0]`; `max(depth5…) < depths[3]` |
| `(len(before), len(after)) == (20, 18)` (`:12366`) | `dropped == ["exchange", "transfer"]`; `len(after) == len(before) - 2` |
| the eleven-tuple `actor_end` list (`:12713`); `len(dropped) == 18` (`:13580`) | `none_arm == []`; `actor_arm` non-empty; `len(total_arm) >= len(actor_arm)`; `bit == {…}` |
| the fork tuples `(31, 3)`, `(28, 2)`, `(28, 2)`, `_TRAIN_KIND_GAP`, the `{none: (10, 31), …}` dict (`:14829-15143`, `:15507-15555`) | `windows >= 90`; `bad_windows == 0`; every arm `genuine > 0`; `got["total"]["diverged"] > 0`; `5 * acts_differ > genuine` |
| the one-round arm's event census (`:16649`) | `d.resolved` non-empty; the planted-round tests |
| `total == 85` `raise SystemExit` statements (`:949`, with the 260-line narrative above it) | `test_h115_the_degree_branches_raise_unspecified_not_systemexit` |
| `len(VERB_TABLE) == 67` at `:2310` | the same assertion at `:15933` (R-05's denominator, once). It is a reading of `main` (67 rows, U3 T-7), re-read and re-recorded at B25 (A-28's `tie`/`knot` split, 68) and B38 (`riot`, if it lands, 69) and quoted with its batch, never typed into prose (C3-N30) |

The single tripwire for "something moved" is the shipped realm hash in B, which is strictly more
sensitive than any count: it covers every Event, receipt and observation.

**E. The dice golden carries live rows only (superseded in content by A-5).** The golden is regenerated
with `tools/gen_sigma_parity_goldens.py` for the functions that remain after the whole-dice roll is deleted
(`U5a_DICE_owed_edits.md` §1 row 8), in that batch (B05), never trimmed by hand; the row count is whatever the
tool writes and is quoted in the commit. In `engine/tests/test_sigma_leverage_parity.py` the superseded-row
helpers and their tests go with the functions they covered (`_SUPERSEDED_TN_ROWS`, `_PRE_RULING_DEGREE_ROWS`,
`TestPoolAwareDegree` with the kernel, per `05_SC_sc05_kernel_disposition_B.md`); `test_golden_table_is_not_vacuous`
keeps a floor read off the regenerated table at that commit.

## Gate (execution artifact)

`python -m pytest engine/season/tests/test_go07_canonical_digest.py -q` green with the three shipped
pins; `git grep -cE '"[0-9a-f]{32}"' -- engine/season/tests` reads one file for every trajectory
literal (`_realm_goldens.py`) plus the encoding vectors in `test_go07_canonical_digest.py`;
`python tools/gen_sigma_parity_goldens.py --check` prints `current` (at B05, with the regenerated count);
`python -m pytest engine/tests/test_sigma_leverage_parity.py -q` green.

## Falsifier

Sweep any shipped fixture in process (`DEFAULT_FIXTURES._v["regime_gain"] = 0.0`) and run the go07
file: the seed-0 pin must redden (it reads `25660615…`, the control arm). If it stays green the owner is not
what the test reads. For E: hand-edit one row of the regenerated JSON; `--check` must print `stale`.

## NERS reading

- **N.** Removing the six copies loses nothing a reader or the game uses; the shipped pin is the one
  the realm's players would meet. Holds bottom-up (one literal per fact, §0.05 cl. 3), top-down (R-rows
  are read at the shipped configuration), laterally (each lane's item tests keep their behaviour
  falsifiers), and across time (a re-record is one line). The direction it does not hold in: an item's
  author loses a standing proof that their item alone moved the world; that proof moves to the commit.
- **R.** Completeness: three seeds where there was one at the shipped configuration. No balance claim
  is made from them (§7); they are a tripwire.
- **S.** One method for every hash pin (import the owner), where sixteen files each had their own
  constant names, revert stacks and comment logs.
- **E (last, against N and R).** Fifteen tests, some 40 literals, 1,023 golden rows and several thousand
  comment lines leave; one small module arrives. Nothing that observes game behaviour is removed.

## Cost class

Edit. Mechanical in fourteen files; the judgement is only in D (confirm each kept assertion still
stands alone), which the table settles.

**Lands it and tier.** The B02 batch (hash EQUAL), first commit: an IN `valoria-author` session on `sonnet`
(`high`), closed by B02's `methodology-close` once. Item E lands in B05 with the sampler. **Hash movers.**
None (tests only); the control is the base tree's go07 run.
