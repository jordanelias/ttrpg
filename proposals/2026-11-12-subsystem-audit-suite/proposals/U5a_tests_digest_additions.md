# U5a · TESTS — what the six test digests add to the three test proposals

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.3 row tests (CONFORMS), §7 (INCOMPLETE: sites unopened), §7b-T; `unified/U3_CONFLICT_LEDGER.md` C3-N30; `unified/U3_DEPENDENCY_ORDER.md` nodes B02, B08). Changed: §E's verb-roster rule is aligned with T1 D and C3-N30 (the one pin T1 keeps at `test_season_shape.py:15933` is a reading re-recorded at B25 and B38, not deleted); §G is placed in B08 with the scene order; lands-it and tier added. Left INCOMPLETE, with the reason: most sites are read from the digests and not opened (this lane runs and edits no test); the executing session's first step per row is to open the site, as the file already orders.

Reconciled: 2026-11-12, unification lane U4c (test 9; from `unified/U3_DEPENDENCY_ORDER.md` §1 item 3 and §3.1, node B02) — dependency line added, which the file lacked: **Depends on:** `01_CORE_tests_one_golden_owner.md` and `01_CORE_tests_delete_what_cannot_fail.md` (B02, both before this file in U3's order); it adds to those two and to `01_CORE_tests_shipped_world_falsifiers.md`, which follows it.

**Lands in batch:** B02 (§A–§C, §E, §F with T1–T3); §D2 after T1 in B02; §D3 with the `tend` draw (`14_VERBS_MATERIAL_A` §6, B12); §G in B08 with `16_PESSIMIST_CORE_a_scene_runs_in_its_own_order.md`.

## Status: PROPOSED (a plan for future execution; nothing here is executed by the closing lane)

Authored by the U5a unification-closure lane, 2026-11-12. `audits/01_CORE_audit_addendum_C_tests.md`
declared that about 205 test files were scanned, not read. `digests/DG_tests1.md` … `DG_tests6.md` are the
second reading. Their closing sections (*Items that could change an audit finding*) confirm F-TEST-01 to
F-TEST-12 and add instances the three carrying proposals do not name. This file carries those instances
and nothing else. It adds no new rule: each row applies a rule already decided in

- **T1** = `01_CORE_tests_one_golden_owner.md`,
- **T2** = `01_CORE_tests_delete_what_cannot_fail.md`,
- **T3** = `01_CORE_tests_shipped_world_falsifiers.md`.

Every site below is cited from a digest. Sites this lane opened itself are marked **opened**; the rest are
`[UNVERIFIED: read from the digest, site not opened]`, and the executing session opens each before it
edits (CLAUDE.md §0.1 pt 3).

## What it changes in `engine/season/` at runtime

Nothing. Test files, one register row's wording, and one `measure:` expression. No hash moves.

## A. Assertions that cannot fail (T2's rule: delete, or give the loop a floor; T3 row 5's form)

| # | site | defect | exact edit |
|---|---|---|---|
| A1 | `engine/season/tests/test_information_cluster.py:659-683` (`test_20iii_every_sheet_the_populated_realm_makes_says_what_its_holder_holds`) | asserts per sheet inside the loop and `checked + skipped == len(sheets)`; with no sheets both pass | add `assert checked >= 1` after the loop (T3 row 5's form; no count pin) |
| A2 | `engine/season/tests/test_in61_succession.py:180-212` | the execution half is asserted only `if claimed:` | assert `claimed` before the block. If the fixture cannot make a claim, delete the execution half and keep the formation half; the commit says which |
| A3 | `engine/season/tests/test_stress_proceedings_rehost.py:94` (**opened**) | `assert not hasattr(convene, "scale") or True` | delete the line; the raw-cell assertion below it is the test |
| A4 | `engine/season/tests/test_season_shape.py:2598` | `len(missing) == len(prose) - len(evaluable)`, a tautology | delete the assertion |
| A5 | `engine/season/tests/test_season_shape.py:3490` | `checked >= 1` after unconditional increments | replace with a floor on the population the loop walks (`assert len(<the iterable>) >= 1` before the loop) |
| A6 | `tests/valoria/test_degree_ladder_single_owner.py::test_the_held_site_still_diverges` | loops over an empty dict | delete the test. After `U5a_DICE_owed_edits.md` §1 row 4 no held site exists at all |
| A7 | `tests/valoria/test_descriptor_registry_category_b.py:81-82`; `tests/valoria/test_descriptors_runtime.py:102-114` | assertions on constants | delete those assertions |

**Not edited, with the reason.**
`engine/season/tests/test_strife_kinds.py:126-127` (**opened**): the does-not-raise call is the control of
the planted-refusal tests directly below it. Sound.
`test_season_shape.py:1148-1199`, `:1332`, `:7664` (harness probe loops with no floor): they guard
`engine/season/harness/` and its case files, which the loop does not read. Accepted, nothing written
(CLAUDE.md §0.1 pt 5).
`tests/valoria/test_frontage_conservation.py:180-182`, `test_mass_battle_yield.py:156`,
`test_combat_reversed_grip.py`, `test_octagon_damage.py`, `test_combat_units_refactor.py:28`,
`test_combat_invariants.py:784-785, 869`, `test_stochastic_rout.py`, the module-reload order dependence:
mass battle's and combat's files, handed to their closure (U5b), listed in `unified/U5_CONFLICTS_U5a.md` §3.

## B. Source-text assertions beyond T2 row 3's eight

Sites: `test_season_shape.py:258`, `:311`, `:369`, `:409-410`, `:426`, `:580`, `:1551`, `:3609-3615`,
`:4159`, `:4176`, `:5613`, `:7574-7578`; `test_sc02_typed_ids_and_loader.py:63`, `:322`;
`test_governance_build.py:776-783`; `test_cp_t03_04_arms.py:93-94`;
`tests/valoria/test_combat_halfsword_affordance.py:62-67` (combat's; U5b lands it by the same rule).

**Rule (T2's falsifier, applied per line).** In process, make the change the substring guards against.
If a behaviour test in the same file goes red, delete the substring assertion: its fact is observed.
If none does, keep the line and name it in the commit body; it is then the only observer and a behaviour
test is owed by whoever next edits that code. No line is deleted on the digest's word alone.

Kept as they are (a walk with a population floor and a planted control): `test_army_menu_presets.py:325-341`,
the `ast` walks in `test_in23`, `test_k3`, `test_migrate_capacity`, `test_governance_build.py:1559-1604`.
`tests/valoria/test_claim_provenance_fields.py:43-53` reads a tool's text: process, accepted.

## C. Skips on an absent combat engine beyond T3 row 6's thirteen

T3 row 6's rule (a skip becomes `pytest.fail`) covers every skip conditioned on the combat engine's load,
including the fixture forms it did not list: `test_combat_band_edges.py` (`engine_available`),
`test_cp_t03_04_arms.py` (`_engine`), `test_cr85_faculty_replaces_history.py` (the autouse fixture),
`test_h206_a_death_at_matter_is_witnessed.py:161-162`. Of the nine sites in `test_season_shape.py`, eight
do not assert `load_error()` first; after the edit none needs to.
`tests/valoria/test_charge_momentum_impulse.py:54-55, 67-68` is mass battle's (U5b).

## D. Fixtures that revert shipped changes beyond T3 rows 7–8

| # | site | exact edit |
|---|---|---|
| D1 | `engine/season/tests/test_rem31_grid_suspension.py` (an autouse fixture reverting CR-87, CR-85 and CP-T03-04, because no fight reaches ENCOUNTER in one shipped season) | drop the three reverts; build the fight as a hand-built `fight` act folded on the shipped `build_realm(0)`, the form `test_combat_module.py` uses. The suspension is then observed at the shipped configuration. If a hand-built fight cannot reach ENCOUNTER on the shipped tree, that is a finding for `11_GO_player_surface_contract_B.md` §8's host, and the file keeps one revert, named in the commit |
| D2 | hash literals asserted under a revert stack in `test_cp_t03_01` (7 reverts), `test_cr17` (8), `test_cr87` (7), `test_cr85` (4), `test_cp_t03_04` (3), `test_in27_endings.py:357-385`, `test_season_weather.py` (first test; the `give`-withheld test) | they fall to T1 C by its rule (a hash pin read under `revert_*` is deleted; the one owner holds the shipped trajectory). The behaviour assertions in those files stay |
| D3 | `test_territorial_subsistence.py` (needs `revert_cp_t03_08`: 37 of 37 hungry cohorts are tended whole inside the season) | no test edit. The cause is the certain, whole `tend`, closed by `18_DETERMINISM_SWEEP.md` D-05 / C-04. The revert goes in the commit that lands that draw |

## E. Count pins and re-pin logs beyond T1 D's list

`test_season_shape.py:2407`, `:4122`, `:4873`, `:6384`, `:6971`, `:7040`, `:7746`, `:10083`, `:12366`,
`:12713`, `:13580`, `:13723`, `:13771`, `:14829`, `:14889`, `:14933`, `:15143`, `:16649`, `:17845`, `:17878`;
the `ever` literal at `:8164`, `:9425`, `:11122`; `test_governance_build.py:913`, `:1975-1991`, `:2421`,
`:2957`; `test_in53_vacancy_need.py:246`, `:298`; `test_in36_foreign.py:99`, `:273-286`;
`test_told_by_channel.py:234-300` (a seed re-picked eight times).

**Rule (T1 D's, applied per pin).** A pin whose comment states the property it stands for is replaced by
that property (a floor, a set inclusion, an equality between two readings of the same run). A pin that
states none, and whose re-pin log shows it moved with unrelated commits, is deleted with its log. A pin
on a closed roster's size that a loader already refuses (`len(REFERENT_CLASSES) == 8`, `len(VERB_TABLE)`)
is deleted: the loader is the owner. The one exception is the pin T1 D keeps at `test_season_shape.py:15933`
(R-05's denominator): it is a reading of `main` (67), re-read and re-recorded at B25 (A-28's `tie`/`knot`
split, 68) and B38 (`riot`, 69, if it lands), quoted with its batch (C3-N30); every other copy of
`len(VERB_TABLE) == 67` is deleted.

## F. Two statements of addendum C the digests correct

| # | statement | correction | edit |
|---|---|---|---|
| F1 | §3, R-07: *"Feeling, attitude, relationship: no test"* | too strong. Tests exist at the mechanism: `test_told_by_channel.py::test_r07_realm_regard_differs_between_hearers_by_claim_not_stance_alone` (**opened**; a two-season realm reader), `test_sc02_reception.py`, `test_in12_forgive.py`, `test_in70_opinion_at_read.py`, `test_march.py:1013-1035`. What is absent is a test that a changed attitude changes a played decision at the shipped configuration | T2 row 4's `-k` expression for R-07's `measure:` gains `or r07_realm_regard_differs`. The absent half stays the gate of `02_CHAR_choice_alignment.md` (T3's "Not written here") |
| F2 | §3, R-02: *"yes, narrowly"*, resting on the fork-and-follow record | at that slice the no-deposit arm diverges as often as the shipped arm (10 of 33 against 10 of 36), and at cell 2 × 3 the shipped arm diverges 0 of 733. The fork test shows a fork changes a later decision; it does not attribute the change to deposits | no test edit: T3 row 2 is the test that varies deposits alone and row 3 already renames the fork test. `01_CORE_requirements_reading_record.md` §1's R-02 reading says both things in one sentence: *the played sequence parts when observation deposits are cut (T3 row 2); the fork-and-follow test shows divergence in both arms and attributes nothing to the deposit channel* |

Also corrected, no edit: F-TEST-02's *"one literal pins the shipped played realm"*. Two more literals in
`test_rem30_character_sheet.py` (`PRE_BUILD` seeds 1 and 2) equal the shipped hashes
`[UNVERIFIED by run: read from the addendum's table]`. T1 A–C is unchanged by it: one owner, three seeds.

## G. H-172: the round stamp has no test that tells it apart

`engine/season/hole_register.yaml` H-172 (**opened**): `Claim.round`'s two arms (stamped with its round,
stamped round 0) read the same in `test_u2_a_deposit_in_one_round_…`. R-03's general claim holds in that
test for both arms. The stamp itself is not in question: it has readers in game code (**opened**:
`queries/person_q.py` pairs a deed with its doer on `(when, round)`; `loop/matter.py:242` reads it as a
floor; `seam/wrappers/sigma.py:290` orders held claims by it). What has no value is the test's arm pair.
Decided (ladder step 5): the pair earns its place or goes, in the commit that makes order inside a
season matter.

1. In the landing of `16_PESSIMIST_CORE_a_scene_runs_in_its_own_order.md` (Jordan's answer A-9), add one
   arm to that test on a fixture where the claim lands at a later position than the read it would
   change: stamped with its round, the earlier read does not see it; stamped 0, it does.
2. If no such fixture can be built on the shipped predicates after that landing, delete the
   `late` / `unstamped` pair from the test (T2's rule: an arm that cannot differ asserts nothing) and
   close H-172 as irrelevant, citing the commit. No game code changes in either case.

**Falsifier.** After step 1, stamp every claim round 0 in process: the new arm must go red. If it stays
green, step 2 applies.

## Gate (execution artifacts)

`python -m pytest <each edited file> -q` green, one file at a time (CLAUDE.md §0.4);
`python -m engine.season.harness.register --requirements` exits 0 with R-07's new expression collecting
seven tests; for section B the commit body lists, per line, the mutation made and the test that went red.

## Order, dependencies, who lands it

An IN-lane session, in the same batch as T2 and T3 (the same files): B02. D2 after T1 (B02). D3 with the
`tend` draw (B12). G with the scene-order proposal (B08). Sections A–C and F have no dependency.
**Tier.** `valoria-author` on `sonnet` (`high`); closed by each batch's `methodology-close`. **INCOMPLETE,
blocking reason:** the `[UNVERIFIED]` sites must be opened by the executing session before each edit (this
lane runs and edits no test); no row is decidable further from the repository without opening them.

## NERS reading

Not a design object. The test that applies (CLAUDE.md §0): each row edits a test that exists and
explains one judgment about it; none opens a queue.

## Cost class

Edit.
