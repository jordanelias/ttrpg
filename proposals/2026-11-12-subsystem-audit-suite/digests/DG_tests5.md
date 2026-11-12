# Digest tests5

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane tests5: 56 test files (engine/season/tests, engine/tests, tests/valoria helpers and combat/army/body tests), read in full. Test-strength audit cited as `F-TEST-nn` = `audits/01_CORE_audit_addendum_C_tests.md`. Hash digests are quoted truncated. Every file is Layer-2 test code; none is a design document.

### engine/season/tests/test_season_weather.py
- **What it is:** pytest file for v9 IN-21 FORCE-WEATHER (keyed seasonal draw on MATTER's yield term, `H-26`), 927 lines, of which about 530 are a hash re-pin log (comments `:33-546`, `:573-662`, `:775-837`).
- **Status:** no Status line (test file). Reading: live; it is the file F-TEST-02 names as holding 22 declared-mover re-pins (it holds far more than 22 `RE-PINNED` blocks by my count, roughly 60 across the three pins).
- **Bears on:** CORE, SE (weather/yield), WR (clock), DICE (draw keying).
- **Content that matters:**
  - Pins `BASE_HASHES = {0: 600d8b27…, 1: 25660615…, 2: 27d8e869…}` (build, one season, two seasons of `build_realm(0)`), `BASE_EVENTS = {1: (13379, 0572125c…), 2: (37646, 4f192564…)}`, `STEP_OFF_ONE_SEASON` (acquaintances=False) and `THREAD_READ_WITHHELD_EVENTS_1 = (13366, b7632953…)` `:547-571,662-663,838`. These are the same `600d8b27…`/`25660615…` literals F-TEST-02 finds in six files each.
  - `test_in21_control_draw_off_and_draw_at_one_reproduce_the_base_hashes` `:725` calls `revert_cr79(monkeypatch)` (imported from `test_strife_credit`) first, so it reads a world with CR-79 reverted, not the shipped one; it asserts `season_factor_draw == ()` ("shipped default is not the control arm") and `events[1][0] >= 5000`, `events[2][0] >= 15000` as non-vacuity floors `:738`.
  - `test_the_give_withheld_arm_reproduces_the_one_season_pin` `:742` withholds `give` and requires the result to equal the pin on both `acquaintances` arms (also under `revert_cr79`); docstring records that between CR-81 and CR-82 the shipped arm DIFFERED, then CR-17 (tau 0.1 -> 0.05) made `give` stop forming in season one, so the control is now a coincidence of formation, not a design property `:750-757,769-772`.
  - Real behaviour tests on a one-town world (`_town`, `:696`): table of 1.0 reads the same hash as no table `:857`; DROUGHT table (0.5) leaves grain 20 vs 40 and emits `shortfall:grain` 10 in season 2, with `checked == 4` and control `c_short == [[],[]]` `:865-883` (a real falsifier with a control, and asserts it asserted); same seed twice one hash, draw on moves it `:886`; `season_factor_of` is keyed on seed and `tick % len(table)`, asserts FULL support `{0.5,1.0,2.0}` so a `% (n-1)` modulus would redden `:896-927`.
  - Test-fixture constants are explicitly tagged `[JUSTIFIED: a test-fixture size, not a game value]` `:690,692`; the fixture is "test data, not a claim about Valoria's economy" `:686`.
  - Re-pin log ends 94-times-style with "A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM" (e.g. `:392,397,402,407`) -- confirms F-TEST section 5 that the discipline held; each entry names a control (a stub/sweep that reads the old value). Two entries are weaker: B10-13 pin commit "none isolated per item" `:541` (confirms the F-TEST-03 `133 -> 137` exception); CP-T02-05 was added then reverted `:417-418` so the pins are "the reading with the stamp reverted".
- **Conflicts / stale:** `test_the_thread_read_withheld_arm_is_pinned_and_differs_from_the_shipped_season` `:841` asserts the arm differs from `BASE_EVENTS[1]` but its own constant's comment says the K-3-time control "can no longer be read on one tree" `:779` -- it is a change detector, not the original control. F-TEST-02 counts 22 entries for this file; the log has more (many are one-line "RE-RECORDED with BASE_HASHES" lines for `BASE_EVENTS`). The module docstring `:1-17` says the control is the pre-change hash at build/1/2 seasons; that is no longer true (the pins have moved 60+ times and the first test is under a revert).
- **Open items:** none stated. The pins fold `content_hash` so any hash-folded schema change re-pins them; there is no single-owner for the realm hash (F-TEST-02 T1).

### engine/season/tests/test_season_weather_per_territory.py
- **What it is:** pytest file, v10 CL-EVENTS (1): force-weather keyed per territory, `ProduceInput.factor` per rung (M16 (b)).
- **Status:** no Status line. Reading: live; arm `season_factor_draw = ()` remains shipped, so tests sweep a draw on their own world.
- **Bears on:** SE, WR, CORE (MATTER barrier).
- **Content that matters:**
  - KEY falsifier: 8 seeds x 8 ticks, two territories draw apart at some pairs, `0 < differing < checked`, `checked == 64` `:59-74`; docstring records a planted failure run-and-reverted (`draw_factory(...)("world","season_factor")` gives `differing == 0`) `:60-61`.
  - Territory-less key (`None`) is a third stream distinct from both territories over 24 ticks `:77-91`.
  - Interface test spies `world_q.produce_input` through the real `_matter` barrier and requires `inp.factor` covers `sorted(RUNGS)` and each rung is credited `int(v * f)` of its own territory's factor; picks a seed with non-vacuity (`seed is not None`) `:94-127`; `checked == 4`.
  - Control: with `()` every rung reads the bare constant and `draw_factory` is replaced by one that raises `:130-145`.
  - Fixture yield 40 grain / 30 salt per harbour at full condition is "test data" `:26-28`; a rung in no territory keys on `None`.
- **Conflicts / stale:** docstring says "commit (2), B10-18, is the live arm" `:5` -- the arm is still shipped `()` per `test_season_weather.py:736`, so no live-weather realm test exists (weather is off in the shipped game). `[UNVERIFIED]` whether B10-18 landed.
- **Open items:** weather is a built, keyed, tested mechanism that ships OFF; no test or realm reading of it ON.

### engine/season/tests/test_settle_margin_seam.py
- **What it is:** pytest file, CP-T01-04 at the seam: `seam/wrappers/sigma.py::resolve` settles the margin's fraction with the act's own uniform; `seam/ladder.py::degree_of` grades it.
- **Status:** no Status line. Reading: live.
- **Bears on:** DICE, CORE (seam), SC (sigma wrapper).
- **Content that matters:**
  - Whole-Ob roll draws NOTHING extra: generator state equals the module's `roll` alone for 40 seeds, `settled_margin == net - ob`, `checked == 40` `:63-74`.
  - Fractional Ob (1.5) draws exactly ONE extra uniform and `settled_margin == floor(net-ob) + (u < 0.5)`; asserts both arms observed `paid > 10 and unpaid > 10` `:76-91` (a guard against a vacuous conditional).
  - The record keeps `net`/`ob`/`pool` unchanged and adds exactly `settled_margin`: `set(out) == {status, module, resolver, pool, net, ob, leverage, settled_margin}` `:94-100`.
  - `degree_of` grades `settled_margin` against zero when present, else the pair: `pair net=3.0 ob=1.5` is Success, `settled_margin` 0 Partial, -1 Failure, 3 Overwhelming `:103-108`.
  - 20,000 real `resolve` calls graded by `degree_of` agree with `odds_of` within 3 SE (`_within_3se`, from `test_odds_of`) and Ob 1.5 odds differ from Ob 2.0 `:111-124` -- statistical, but fixed seed 11 so deterministic.
  - Hard-codes the shipped obstacle ceiling of 2 (`score/2`) in `_world` docstring `:39`.
- **Conflicts / stale:** `capability` set directly on persons with `roster-exempt` comment `:43`. None else.
- **Open items:** none.

### engine/season/tests/test_settlements_module.py
- **What it is:** pytest file, v9 IN-07: the `settlements` module imports only the record types (A-25), in a fresh interpreter.
- **Status:** no Status line. Reading: live; one of four sibling module probes (`social_contest`, `combat`, `mass_battle`, `fi03_trail`) `:6-8`.
- **Bears on:** SE, CORE (layer-1 conformance, composition).
- **Content that matters:**
  - Collects composition rows whose `target` starts `modules.settlements.`, requires `len(targets) >= 8` (population floor) `:32-34`, imports them in a fresh process and asserts the loaded repository files are only package `__init__`s, `engine/season/queries/inputs.py` and `modules/settlements/` `:36-41`.
  - Executable proof of A-25 for settlements; reads `composition.ROLES` (the runtime registry), not prose.
- **Conflicts / stale:** the allowed set is hard-coded (5 files) `:36`; the `>= 8` figure is a count pin of entry rows that would move on a legitimate new entry. Mention in docstring of `tests/valoria/test_modules_reachable_closure.py` as the sibling scan which "records a file under `engine/` as reached without walking it" `:3-6` [UNVERIFIED].
- **Open items:** none.

### engine/season/tests/test_soak_grades.py
- **What it is:** pytest file for `harness/soak.py`'s two graders (flat cost per season, act-mix convergence), plan position IN-20 STORY-SOAK. Named in F-TEST as read.
- **Status:** no Status line. Reading: live; F-TEST section 6 "kept on purpose" (grader tested on data whose answer is known).
- **Bears on:** CORE (harness/instrument), WR (soak).
- **Content that matters:**
  - Confirms F-TEST: every grader assertion pairs a PLANTED failure with a CONTROL that must pass: flat costs PASS vs 1.5^i growth FAIL `:25-32`; plateau-inside-first-half still PASS `:35-38`; one 90.0 spike is not growth (medians) `:41-43`; `[0,0,1,1]` FAIL, `[0,0,0,0]` PASS, 3 points UNGRADED `:46-50`.
  - Mix grading: steady mix PASS vs `{"tell":10}` x8 FAIL on COLLAPSE not drift (`drift == 0.0`, `top_share == 1.0`) `:53-63`; drift exact value `0.5` pinned by arithmetic (`0.5*(.5+.5)`), with a note that it would read 1.0 if the half-sum were dropped `:73-76` -- an exactness claim asserted with `==`, not approx; blocks of one season (7 seasons) are UNGRADED, 8 PASS `:91-96`.
  - Disk round-trip: `_write_world` writes `seasons.jsonl`/`acts.jsonl`, `load_series` reads them, `grade_run` names the missing `--cost-growth-ceiling` flags when a ceiling is `None` (UNGRADED) `:117-133`; planted bad world fails end to end `:136-141`.
  - Thresholds `COST_CEIL=1.5`, `DRIFT_CEIL=0.2`, `TOP_CEIL=0.8` are "the TEST's own arguments", not engine values `:6-8,17-19`.
- **Conflicts / stale:** none; the soak instrument grades but no test runs it on a played realm (F-TEST-01 gap).
- **Open items:** none.

### engine/season/tests/test_social_contest_module.py
- **What it is:** pytest file, plan position `31a` (IN-03): the `social_contest` module entry called on a hand-built `SocialContestInput`, plus S27.4 refusal at the host adapter.
- **Status:** no Status line. Reading: live (F-TEST says "social contest to `:65`" was read; this file read in full).
- **Bears on:** SC, DICE, CORE (A-25 module boundary).
- **Content that matters:**
  - Entry discovered the way the host finds it: prize rows' `module_entry:` names a composition role -> `composition.ROLES[r]["target"]`; engine never imports module code `:24-30,12-14`.
  - Subprocess probe: entry returns a `Margin` type with `ob == 2.0` and `net == roll_net(4, rng=Random(7)) + net_boost(lev, 4)` for `lev` 0.0 and 1.5; same seed gives the same result; loaded files restricted to dice_engine, `inputs.py` and the module dir `:33-83`. `checked >= 2` asserted.
  - The module's `net` is exactly `roll_net + net_boost` (ED-SC-0037): the SC resolution is dice-pool + leverage boost, no other term `:78-80`.
  - S27.4: derived obstacle EQUAL to multiple x pool (4 vs 2x2) is not refused; 4.5 is refused with exact dict `status=REFUSED, why=S27.4, module=social_contest, resolver=d10_sigma, pool=2, ob=4.5`; with ceiling 2 the same call is RESOLVED at ob 2.0 `:86-111` (a `>=` bug in the rule would redden the first assertion).
  - The second test builds `w` as a `SimpleNamespace` with `fixtures` dict and `practice_cap` 0 (the `faculty` practice addend CP-T01-02 reads that key) `:100-103`.
- **Conflicts / stale:** none found.
- **Open items:** none.

### engine/season/tests/test_storybar.py
- **What it is:** pytest file, IN-19 / REM-15 / CR-15: pins the INSTRUMENT `harness/storybar.py` (M2: the cause graph of a season, cross-person share, chain depth, draw-seed arm), "never its numbers" `:1-3`.
- **Status:** no Status line. Reading: live; same stance as `test_aperture.py`.
- **Bears on:** CORE (R-01 decisions propagate, R-02 later decisions; instrument), CHAR (chooser draw).
- **Content that matters:**
  - Falsifier on a real seeded run: plant a severed antecedent edge in a COPY of the log and the cross-person share drops; the unplanted copy must read identically (control); `checked >= 2` `:48-80`.
  - `--arms off off` is the only comparison runnable: "no forcing source is built, and an unbuilt arm is refused rather than invented" (`ValueError` for any other arm) `:83-95`. So a forcing arm for R-01/R-02 is named by the instrument and has no implementation.
  - Draw-seed arm (REM-15): same draw seed twice reads identical; across `DRAWS=(0,1,2,3)` at least one pair differs at the shipped temperature (`checked >= 6`, `differing >= 1`); at `choice_temperature=0` all four runs are identical in chains (a leak control; requires `intent_disclosure == 0.0`) `:132-170`. Cap-10 cast (`build_realm(SEED, CAP)`), not the shipped realm.
  - CR-15 "executed reading" beside the default: a refused antecedent is CUT not bridged over (a3 depth 3 default, 1 executed) `:198-238`; on a real run `refused & set(rows)` non-empty, hash unchanged, `set(ex) == set(rows) - refused` `:241-264`.
  - CLI text assertions: `--executed-only` lines `"executed seed="`, `"total:"`, and `"arms off vs off: EQUAL"` `:267-278`; a repeated `--draw-seeds 1 1` exits 2 `:281-287`.
- **Conflicts / stale:** none. This measures R-01 (cross-person edges) but only on `SEASONS=2`, `CAP=10`; F-TEST-01 gap stands.
- **Open items:** the forcing source is "not built" (`:9-10`).

### engine/season/tests/test_stress_proceedings_rehost.py
- **What it is:** pytest file, plan position `18` (PROC-A) part 5 + v9 SC-04: ten of 38 stress cases (ST-03/04/08/23/30, then ST-09/10/14/15/26) from `proposals/2026-09-05-proceedings-subsystem/stress/stress_proceedings.py` re-hosted against the real fold.
- **Status:** no Status line. Reading: live but a RE-HOST of a proposals-tree stress script; 28 of 38 cases explicitly NOT PORTED and classified (document-only, probe-model, registry-count, season-driver, not attempted) `:25-43`.
- **Bears on:** SC (proceedings, `speak`, `determine`, `release`), FA (venues/arrangements), CORE.
- **Content that matters:**
  - Corrects the old plan's counts: ST-01..ST-38 are case ids; "twenty-eight" in the old header is the FINDINGS count (F-01..F-28), not the case count `:5-11`. Old tracer `shape.py` no longer exists (absorbed into `engine/season/`; ledger `:1821-1822`).
  - ST-14 (`:223-260`): for each seeded arrangement row whose `disposes` is in `DISPOSABLE_KINDS`, open a case, determine it with a strong judge and require ONE live edge of exactly the row's kind (`oblige`/`detain`/`ban`) at a band in `OPENS`; `checked == 7`. The two `Record`-disposing rows `council_of_state` and `parliamentary_debate` have NO WRITER: `open_case` answers `case.refused`, asserted as an observed gap `:259-260`.
  - A `declared`-disposal row needs its `quorum` of the bench's live commits (CR-34); the test patches `quorum` to 1 via `monkeypatch.setitem(row,"quorum",1)` and plants an OUGHT commit by the Duke (`tiny_world` bench is the Duke alone) `:245-251`.
  - ST-15 (`:263-286`): determination is a determination only when made THROUGH the seat (`Act.via`); the same judge with `via=None` is `determine.refused`; a non-holder via the seat is refused; control (1) executes. Strong, three-arm.
  - ST-26 (`:289-312`): `release` writes `Tenure.until`; the convict can discharge the `oblige` the bench opened; the same party's `release` of a `ban` is `release.refused` ("a restraint is not the holder's to discharge").
  - ST-10 (`:198-220`): `speak` is `contests: "a matter"`; across pools (1,2,4,8) x 10 act ids, `folded == 40` and `len(seen) >= 2` bands, i.e. grading varies (not a fixed degree).
- **Conflicts / stale:** `:94` `assert not hasattr(convene, "scale") or True` is a tautology (always passes); the real assertion is the next lines on the raw YAML cell (a weak-assertion instance not in F-TEST). Counts pinned: `len(LADDER_RUNGS)==6`, `INTERPOSITION_KINDS==6`, `GENRES==3`, `PROOFS==4`, `_ARRANGEMENT_KEYS-{id} == 13`, `checked == 7` `:119,141-144,259`; several assert that named functions are STILL missing (`occasion_at`, `attendees_at`, `genre_of`) and will redden if built `:81-84` (a test that pins an absence). References `proposals/2026-09-05-proceedings-subsystem/stress/` which exists (checked) -- a proposals tree the engine does not read.
- **Open items:** `parliamentary_debate` / `council_of_state` cannot dispose (no Record writer). ST-37/38 registry checks and ST-31..36 end-to-end traces never re-hosted.

### engine/season/tests/test_strife_credit.py
- **What it is:** pytest file, v11 CR-79 commit (1)/(2): the CREDIT TERM at WITNESS (`loop/witness.py::_credit`), a told claim's confidence scaled by `1 + regime_gain * c`, `c = world_q.commensurate(hearer, teller)` in {-1,0,+1}. Also the home of `revert_cr79`.
- **Status:** no Status line. Reading: live; `regime_gain` ships `0.5` (`data/fixtures.py:1086`, verified; ED-IN-0316).
- **Bears on:** CHAR (affiliations/conviction), FI (told claims, epistemics, R-07), WR (strife), CORE.
- **Content that matters:**
  - Credit arithmetic on one telling at 37: commensurate hearer 56, incommensurate 19, unrelated 37 at 0.5; all 37 at the control; planted failures run and reverted (deleting the `if regime` branch gives 37,37,37; narrowing to `if regime and refracting` leaves 40) `:98-110,161-172`. Hearer's OWN conviction sets the sign, not his settlement's (the dissenter) `:112-122`.
  - Ceiling: `[0, max(confidence_default, uncredited value)]`: +1 leaves 100 at 100 and 120 at 120; -1 still halves `:125-137`. Range check: `regime_gain` outside [0,1] or NaN raises `ValueError` `:175-178`.
  - Control test: at `regime_gain` 0 neither `_credit` nor `commensurate` is reached (both replaced by a raise), the same raise FIRES at 0.5 (so the probe can see a call), and control equals the `_credit`-bypass arm `:181-199`.
  - `AT_THE_VALUE_GIVEN_ONE_SEASON = "5ab73af2…"` `:41` is the ONE literal that pins the shipped played realm (F-TEST-02); asserts only a count `len(calls) >= 1` for `commensurate` plus the hash, no behavioural property `:216-242`. Matches F-TEST-02/01 exactly. `5ab73af2…` also equals the realm hash probed at seed 0 in F-TEST-01 evidence row 7.
  - `revert_cr79` `:88` sets `DEFAULT_FIXTURES._v["regime_gain"] = 0.0` in process; imported by `test_season_weather.py` (two tests) and `test_strife_flows.py` -- the revert-stack mechanism in F-TEST-02 (up to seven deep).
  - `test_a_person_absent_from_the_world_reads_zero` admits it could not reproduce a told site reaching a missing teller ("MEASURED, NOT ASSUMED") `:202-213`.
- **Conflicts / stale:** the docstring says `regime_gain` is the control `0` at commit (1) and ships 0.5 at (2) `:5` -- only the latter is true now. Imports `BASE_BUILD`/`BASE_ONE_SEASON` from `test_strife_flows` and quotes them as `25660615…` -- the same literal as `test_season_weather.BASE_HASHES[1]`.
- **Open items:** none; the realm's WITNESS reaching `commensurate` is asserted only as a count of calls.

### engine/season/tests/test_strife_execution.py
- **What it is:** pytest file, CR-72 EXECUTION (XE): a MEASURE (no code changed, hash equal) of whether `fight` forms and is admitted against a HELD party (`strife-00` §9 open item (i)), on two hand-built routes (`arrest`, `capture`).
- **Status:** no Status line. Reading: live; a measure recorded as tests, with a disclosed instrument defect.
- **Bears on:** PC (fight formation/admission), FA (custody, detain), WR (strife instrument), CORE.
- **Content that matters:**
  - `fight` FORMS for a seat-holder on a held party as violence context `crime` (via the `Detainee` stamp) on both routes and the fold admits it (`fight.declared`, not `kill.refused`) `:141-150`; CONTROL: closing the `detain` withdraws the formation `:153-162`; CONTROL: the Duke at `S` while the prisoner is at `Hh` is `kill.refused` (co-location, not held state, admits) `:165-171`.
  - The restraint of the held party does NOT enter admission: nothing on `fight`'s path reads `restrained()`, so a restrained man is a legal target `:27-30` (a PC/FA finding stated in the docstring, no assertion on the absence by design).
  - DISCLOSED INSTRUMENT DEFECT: a real `person.died` carries its change on field `body`, but `victim_held` collects only field `exists`; and a dead man's `detain` is gone after `World.remove_person`. So the real instrument reads a held man's real death as KL never XE; the planted death carries an `exists` change to read the reader "AS BUILT" `:32-43`.
  - Docstring: "The encounter then ran the fight to a death at every one of 60 act ids tried, and either party was the one who died" `:20-21` -- a measured-not-asserted plain `fight` kills 60 of 60 (consistent with F-PC-04 "plain `fight` kills 200 of 200").
  - Mutation pair: planted death on a live `detain` reads `["XE"]`, closing the tenure one tick before reads `["KL"]` `:193-211`.
- **Conflicts / stale:** the measured deterministic lethality (60/60) conflicts with the brief's DO-NOT-DO-DETERMINISTIC rule (F-PC-04); the test does not assert it (by design "would be a guard on an absence" `:34`).
- **Open items:** `victim_held` never fires on a real death (`harness/strife.py` and `World.remove_person` own both; named, not fixed).

### engine/season/tests/test_strife_flows.py
- **What it is:** pytest file, CR-76/77/78 (batches B11-S3, B11-S4): the strife WORLD READING (`world_q.flows_in`, `concluded`, `within`, `presented`, `commensurate`), the PERSON READING (`flows_known`, `concluded_known`, `open_referents_known`) and the STAMP (`flow_stakes`, `Fixtures stamp_flow_stakes`).
- **Status:** no Status line. Reading: live. Docstring numbers 18 claim groups, each loop "asserts that it asserted" `:60`.
- **Bears on:** WR (strife flows/eras, narrative), FA (war/detain/docket), CHAR (conviction, affiliation), FI (what a person knows), CORE (R-07 imperfect knowledge, R-02).
- **Content that matters:**
  - World reading: two realm-wide events while an era is open read as ONE era; a terminal move at the realm rung concludes it; a strand never concludes on its own opening move; a later linked non-terminal move reopens (rule (b)); an open `detain`, docketed matter or `at_war` pair keeps an era open `:129-266`. The `at_war` arm runs on stand-ins (`_fake_war`) because "`at_war` is False for every pair the tree can build" `:121-123` (wars cannot occur in shipped data).
  - Content-opening: two petitions on one matter open a strand, on two matters none; the content-opening move is never terminal `:286-362`.
  - `commensurate` table (8 cases): `false` pair +1, shared affiliation +1, `true` pair -1 (wins over a `false`), only `null` or one holds none 0; symmetric `:365-378`. `A.INCOMPATIBILITY` values `{True,False,None}` `:381-384`.
  - Person reading (CR-77): a witness and a hearsay holder read different flows; lacking the terminal claim he reads the strand open though the world's `concluded` reads it closed; the arrest deposit names the arrester and custody edge never the prisoner; test passes `claim_subjects` through the real deposit rule `:567-660`. `test_the_person_reading_reads_no_act_store` stubs act store and log with raisers `:775-806`.
  - Control on the realm `:817-849`: after one season at seed 0 "no ledger holds an `opens` claim ... so every person reading is `()` as shipped (asserted)" -- i.e. in the shipped one-season realm EVERY person's strife flow reading is empty (`len(w.persons) > 10 and all(flows_known == ())`) `:833`; the read-twice control plants an `opens` claim. This means the stamp (CR-78, shipped ON) has no effect on the first realm season at seed 0 (consistent with the F-TEST-01 gap: play never reaches this behaviour).
  - Study-link loader: 16 links (6 robust, 10 stable), `leave_and_rejoin == 74`, `cases == 102`, refuses 8 bad documents; four links are UNREACHABLE (`DA>WA, DR>IN, WN>DA, WN>FA`) exactly the links on DR, DA, FA `:424-530`.
  - Pins `BASE_BUILD = 600d8b27…`, `BASE_ONE_SEASON = 25660615…` `:856-857` (duplicates of `test_season_weather.BASE_HASHES[0/1]`); the CR-78 control calls `revert_cr79` `:960`.
- **Conflicts / stale:** `test_the_strands_block_prints_...` pins `len(link_ln) == 16` and the exact dead-link list `:526-528`. `pytest.approx` at `:513` is on a mean of fractions (not an exactness claim). Several tests hand the code stand-ins for an arm that "no tree can build" (war), so the war arm is wiring-checked only.
- **Open items:** "named gap (1)/(2)" in the person reading (docket and war arms have no ledger source and are dropped) `:25-45`.

### engine/season/tests/test_strife_instrument.py
- **What it is:** pytest file for `harness/strife.py` (side-aware classifier of strife moves, 40 codes in `strife_moves.yaml`, static route check, grading).
- **Status:** no Status line. Reading: live; instrument-grader tests on planted data (F-TEST section 6 kept class).
- **Bears on:** WR (strife), PC (death/violence classes KL/XE/DN), FA (side_against, war), CORE (instrument).
- **Content that matters:**
  - Registry loads 40 codes and refuses 5 planted bad signatures (unknown verb/kind/code/key/attacker) `:49-67`; ends total 102 and yield 24 terminal codes; loader refuses ends totalling 103 `:133-146`.
  - Classification: `person.died` is DN with no cause, KL with `fight`/`march`/`accept`, XE for a held person killed by `fight`, `[]` for a held person felled by `accept` (a duel is not execution) `:70-77,251-259`. `field.won/lost` swap WA/WR by side; `march.declared` FR/WN/OW by side `:79-88`.
  - `side_against`: nearest governor and above are `A`; non-governor `R`; foreign factions `O` (Altonia, Schoenland by default); no governor -> `None` `:94-102,149-153`.
  - Residue check: a signature kind is matched or residue, never both: loops kind x verb x side x held and asserts `len(hits) <= 1` and exactly one tally, `checked >= ...` `:200-220`.
  - `full == ["DN"]`: DN is the one terminal code with no route "by design" (ageing is 0.0) `:248`; `OW`/`XA` are not DARK at the shipped default (`foreign` defaults True) `:164-176`.
- **Conflicts / stale:** header says the wiring from a real `World` is NOT covered here `:23-25`; `test_strife_execution.py` later found that wiring defective for deaths.
- **Open items:** "XE formation on a held party is open" comment `:109` (now answered by `test_strife_execution.py`).

### engine/season/tests/test_strife_kinds.py
- **What it is:** pytest file, CR-75: `rosters.yaml: strife_kinds` (opens, joins, never, concludes) and `foreign_factions`; import-time checks `_check_strife_kinds`, `check_strife_openers`, `check_restraint_kinds`.
- **Status:** no Status line. Reading: live; F-TEST-07 (confirmed): `:126-127` `test_the_shipped_openers_pass_their_check` is a does-not-raise test with no assert, paired with the refusal tests at `:130-163`.
- **Bears on:** WR, CORE (data registries read by code at import).
- **Content that matters:**
  - Each import-time refusal is planted on the function itself (outside `EVENT_KINDS`, in two lists, `concludes` outside opens/joins), shipped build as control `:53-65`.
  - `concludes` must EQUAL a rule derived over the registry (a kind concludes only if every code it maps to is terminal): `derive_concludes` is written in the test as a check on data no loader reads `:42-49,104-109`; mutation: `requisition.taken` in `concludes` passes the import check and fails here (VI ends no case) `:112-117`.
  - Every registry kind lies in exactly one of opens/joins/never (`len(registry) >= 40`, a population floor), falsifier strikes `tenure.opened` `:91-101`.
  - `check_restraint_kinds` refuses empty derivations and a restraint kind that is no move (`arrest.made` moved to never) `:150-163`.
  - `FOREIGN_FACTION_IDS == {faction_prop_id(f) for f in FOREIGN_FACTIONS}` `:120-121` (an identity between two owners).
- **Conflicts / stale:** the `concludes` set is both authored in `rosters.yaml` and derived in the test; a second copy of the rule that "no loader reads" `:13` (two-owners risk, though the test makes them equal).
- **Open items:** none.
