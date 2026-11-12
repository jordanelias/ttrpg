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
  - The re-pin log repeats "A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM" (e.g. `:392,397,402,407`) -- confirms F-TEST section 5 that the discipline held; each entry names a control (a stub/sweep that reads the old value). Two entries are weaker: B10-13 pin commit "none isolated per item" `:541` (confirms the F-TEST-03 `133 -> 137` exception); CP-T02-05 was added then reverted `:417-418` so the pins are "the reading with the stamp reverted".
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

### engine/season/tests/test_tenure_diff_exact.py
- **What it is:** pytest file: `World._tenure_snapshot` / `_tenure_changes` (the gate's F3/F9 observation of the Tenure store around every watched write) against the per-Tenure reference loop they replaced, on 10 shapes plus a 300-step random walk.
- **Status:** no Status line. Reading: live; a strong exactness test (reference comparison, full `(tenure, was)` list compared in order).
- **Bears on:** CORE (write gate, state integrity), FA (tenures).
- **Content that matters:**
  - Clauses (a)-(j): nothing moved, field assigned, payload mutated in place, opened, removed with person, removed+opened at equal length, reordered, term+payload, opened/removed at the very end of the store; MUTATIONS (run, each alone) listed in the docstring name which clause reddens `:9-15`.
  - (k) `:201-257` random walk of 9 edit kinds, snapshot before and diff after each edit, plus edits BETWEEN writes treated as next baseline; asserts `moved >= steps // 4`, `fresh > 0`, `between > steps // 4` (asserts it moved).
  - (l) `:260-271` a field set through `__dict__` (bypassing `Tenure.__setattr__`'s version count) is invisible to the diff but `discard_caches` raises `InstrumentDefect` at the barrier -- a stated blind channel with a loud net.
  - (m) `:274-280` a clean realm passes the barrier check before and after a season; asserts `w._tshadow is not None` ("the check observed nothing" otherwise).
- **Conflicts / stale:** none. Test of a performance rewrite (fast path) against its own reference: the reference lives in the test file (a second copy of the diff rule, by design).
- **Open items:** none.

### engine/season/tests/test_tenure_gate_effect_body.py
- **What it is:** pytest file, CR-06 / H-137: the gate sees an effect body that changes a tenure by itself (`World.effect_body_observed` around `_apply_write`).
- **Status:** no Status line. Reading: live.
- **Bears on:** CORE (write gate, Layer-1 conformance), FA.
- **Content that matters:**
  - An effect that closes an unrelated live seat-hold in its own body then returns an unrelated `Change` raises `NotYours` and the seat stays live; control (same host, same actor, clean effect) succeeds with `proposition.uttered` `:51-76`.
  - An effect body that OPENS an edge eagerly is refused and the edge removed; the same edge opened inside `apply` stands `:79-97`.
  - A legitimate `Change` (closing the actor's own `tie` inside `apply`) is not refused `:100-111`.
  - Docstring boundary: "Tenures only: an eager write to an entity field is still convention-bound (`_apply_write` says so)" `:23` -- an acknowledged hole outside tenures.
- **Conflicts / stale:** uses `_plant`/`_driver` helpers from `test_g4_no_op_receipt` (a G-family strong test per F-TEST section 4).
- **Open items:** eager non-tenure entity writes in effect bodies are not observed.

### engine/season/tests/test_term_upkeep.py
- **What it is:** pytest file, plan position `17b` TERM . UPKEEP: `Tenure.term`, MATTER maturing a term, `Office.upkeep` read at one owner (`world_q.upkeep_of`), and payment by `transfer` renewing `oblige` terms (gate basis `T-n` and `renewal`).
- **Status:** no Status line. Reading: live (workplan `2026-09-28-the-plan-one-order-mc-v18-retired.md` cited as the source; that plan is named retired in its filename).
- **Bears on:** FA (offices, establishment, obligations/oaths), SE (treasury), CORE (gate bases T-n, renewal).
- **Content that matters:**
  - `_eff_oblige` opens an edge with `Term(tick + oblige_term, <the oblige act>)`; at `oblige_term` None no term; sweep (None, 1, 4) `:101-112`. An unpaid term lapses AT maturity (tick 2 for term 2) and not a season earlier; the lapse cites the oblige act and the gate admitted it as `T-n` only `:119-153`.
  - A term lapses "whoever is left to pay it": when the duke resigns, a transfer through the vacated seat renews nothing and the term matures on schedule `:156-171`.
  - Renewal: paying 1 unit (`default_upkeep` shipped 1) out of the seat's rung `D` to an obligee's home `Hh` moves the term from 2 to 4 ("on from where it stood"), re-declared by the payment, emits `transfer.made` + `term.renewed`; lapse then cites the PAYMENT act `:178-208`.
  - Narrative #3 (embezzlement made observable): two identical worlds differing only in `to` (obligee's home vs the holder's own hearth); at maturity the paid seat keeps its man, the skimmed seat loses him; "nothing in the engine names embezzlement" `:211-235`.
  - A payment covers obligees soonest-maturing first: at upkeep 1 one unit renews one of two; at declared `Office.upkeep` 3, 2 units renew nobody and 3 renew the obligee `:248-279`. Four clauses of `_renewals` each broken alone refuse; control renews `:282-308`; and 9 gate renewal refusals one clause away (shortening, no seat, stranger, ended oblige, non-oblige edge, the obligee winding his own term) `:420-455`.
  - `(Tenure, term)` is RES-only; a MATTER write of it is `Forbidden` `:489-506`.
- **Conflicts / stale:** all of this is deterministic bookkeeping: lapse at an exact tick, renewal fully determined by payment amount vs `upkeep` (no draw). Under the brief's DO-NOT-DO-DETERMINISTIC rule, the tick-clock maturing is bookkeeping (allowed); whether an unpaid establishment man LEAVES is a fixed function of state (arguably a candidate for a draw) -- flag for FA. `holonic_ARCHITECTURE.md:428` cited for "a post pays ITS establishment" `:326`.
- **Open items:** none.

### engine/season/tests/test_territorial_subsistence.py
- **What it is:** pytest file, plan position `24f` (ED-IN-0255, ruled 2026-09-18) SUBSISTENCE IS TERRITORIAL: cohorts (`weight>1` synecdoche persons from `cohorts.yaml`) eat; individuals do not; plus SE-01 `24g`/SE-06 territory temperaments, `person.demanded`/`person.individuated`, and weight/envelope write owners.
- **Status:** no Status line. Reading: live; carries the Jordan ruling verbatim: lords and guild members do not worry about subsistence, "it's a territorial issue" `:4-8`.
- **Bears on:** SE (subsistence, larders, cohorts), CHAR (cohort pursuits), WR (population as synecdoche), CORE.
- **Content that matters:**
  - Realm seats exactly the `cohorts.yaml` rows (37 per `:748`) beside an unchanged NPC cast; refuses 7 malformed row shapes (weight 1, `true`, 2.5, no weight, `npcs.yaml` fields, doubled rung, empty file) and a rung the world did not build `:110-199`. The ceiling reads `capacity` from dwelling Sites `:162-179`.
  - Falsifier on the BUILT realm: under each live `body_step` arm of register row `H-125`'s sweep (read off the register via `REG.load()`), an office-holder under a settlement in dearth keeps his body and that settlement's cohort's body falls by exactly `arm x shortfall` `:263-303`; control arm 0 moves no body and emits no `body.changed`/`person.died` `:306-323`.
  - REM-52: `body_step` ships at `10`, a live arm; seed 0: 36 of 37 cohorts at 940 = 1000 - 10 x 6 after season 0 (`:333-335`), but the shipped-arm test now needs `revert_cp_t03_08` because with CP-T03-08 `tend` live every short cohort tends itself whole in the same season (37 of 37 tended) -- the hunger a cohort suffers is erased within the season `:340-343`. So hunger is built, shipped ON and neutralised in play by a later item.
  - Drain guard: second MATTER barrier on the realm, at least one cohort draws real stock, record names no individual, matter conserved `held_after == held_before - drawn + produced` exactly (integers) `:391-451`.
  - `dispatch` to a nonexistent clerk emits `person.demanded` then next season CENSUS mints him (`person.individuated` citing the demand), weight 1, at the dispatcher's place; five control cases (site, rung, existing person, no remit, empty payload) mint nobody; a convened date id and a dead person's id are not minted `:511-592`.
  - AST sweep: no module under `engine/season` outside `loop/census.py`/`loop/matter.py`/`harness/probes.py` writes `Person.weight` or `Rung.envelope` (`scanned >= 50`; planted write must be found in two spellings) `:595-650`. A stored `Rung.population` aggregate raises `ShapeGap` `:679-689`.
  - SE-06: a cohort's pursuits are its territory's temperament via `cohorts.yaml: temperaments:` (alpha, beta over the `deontological_instrumental` axis); expected vectors recomputed in the test from `tables.pursuit_projection` at tolerance `1e-12`; T3 (0.5/0.5), T6 (0.9/0.1) and T5 (0.3/0.7) separate poles; 11 malformed temperament blocks refused; one row per territory except T15 `:699-796`. Control: removing the block reproduces the uniform realm hash `:799-813`.
- **Conflicts / stale:** `:748` pins `checked >= 37` and `T15 holds no cohort`. Docstring says the cohort-order mutation (seating cohorts before the cast's tie block) is NOT caught by any test ("said rather than implied") `:36-41`. The `body_step=10` hunger effect is overridden in play by `tend` (see above).
- **Open items:** the seating ORDER that keeps a cohort out of the tie pool is argued at the call site, not observed `:36-41`.

### engine/season/tests/test_told_by_channel.py
- **What it is:** pytest file (2,343 lines, 139 KB), plan position `15d` + the TELLING WORKPLAN (T1-T7, ED-IN-0282) + IN-18 G1/G2/G3/G6: hearsay minted from the channel, told-claim confidence and chain, hearsay weighed when read (`told_weight`, `regard_gain`, `record_gain`), a telling names its hearer, dedup by origin, a teller's record, declared intent, judged regard, stance polarity, slant, confidences.
- **Status:** no Status line. Reading: live; this is the densest epistemics test file. Its mechanism-by-mechanism "MUTATION (run ...)" paragraphs are narrative records of reverts, not executable.
- **Bears on:** FI (epistemics, hearsay), CHAR (regard, stance, pursuits), SC (what a telling carries), WR (rumour), CORE (R-07 imperfect knowledge, R-02, R-06).
- **Content that matters:**
  - Channel map: `CHANNEL_CLAIM_SOURCE` is total over `WITNESS_CHANNELS` and presence heads the precedence; one channel per person, the strongest; BOTH directions in one test (reversing the roster order credits a person in the room to `document_key` and `told_by`) `:77-130`. A document holder not in the room holds the event `told_by` while the residents hold it `firsthand` `:133-146`. A telling is hearsay for what was said and firsthand for THAT it was said; told claim carries the teller's own confidence (37, asserted != default), `chain == (teller,)`, `hops == 1`, `teller` stored `:162-213`.
  - Realm hearsay falsifier `:216-322`: `SEED = 0` re-pinned 8 times (0 -> 5 -> 4 -> 18 -> 20 -> 28 -> 0) because the realm's first season stops minting any chained told claim whenever the act mix moves; the tables record chained told counts per seed (e.g. `:298-300`: nonzero at 27 of 40 seeds at CR-17 time) and say the mechanism per seed "is NOT isolated". A pinned-seed-selection test: coverage depends on a lucky seed.
  - T1: what a telling passes on is fixed at CHOOSE via `Act.payload["said"]`, not read from the teller's live ledger at WITNESS (a newer claim cannot reach the hearer) `:325-393`. T3a/b: `told_weight` 0.5, hops via `Claim.chain`, support = noisy-OR over per-origin max: two origins at 0.5 beat one (support 0.75 vs 0.5), one origin told twice counts once (`_support == [0.5,0.5,0.5]`) `:430-470,643-682,763-794`; regard at the shipped gains: stance +/-STANCE_MAX gives weights 0.75 vs 0.25 `:797-827`; 400-trial randomised check that `weigh=None` equals the old `(when, confidence)` comparator `checked >= 1000 and ties >= 50` `:548-594`.
  - T4: `tell` carries `to`; hearer must be with the teller (`hearer`/`with` stem) else `tell.refused` BEFORE any contest, degree None; present addressee AND bystander both hear (`chain==(p_low,)`) `:837-902`; a `with` read rides the Event's `observed` but is NEVER deposited in the teller's ledger (WORLD_ONLY_STEMS) across 4 cases `:906-979`. T4b: the once-per-season filter keys `(verb, subject, counterparty)` so a second hearer is a distinct opportunity `:1083-1176`. T5: dedup by origin (one origin via two tellers deposits once; two origins deposit twice and outrank one newer single-origin claim; a firsthand or `inferred` holder is never re-told) `:1225-1315`. T6: teller record (agree/contradict pairs, `record_gain` 0.5): good 0.75, bad 0.25, mixed 0.5; control `record_gain` 0 reproduces pre-T6 weights; `seen` and event-kind pairs are not scored `:1339-1535`.
  - T7: `intent_disclosure` ships 0; at 1.0 a telling's `said` becomes the teller's chosen-not-done next act (`intent:transfer ...`), hearers hold it `told_by`, and `world_q.named` raises a `claim_landed` question about a far `x_far` who intends to fight `p_low` `:1590-1698`. Control on the realm at rate 0: shipped vs `declare_intents` excised give equal `content_hash` AND equal carried `said` (`seen["opportunities"] >= 1`) `:1733-1785`.
  - G1/G2/G3: `judged_gain`/`told_valence_gain` ship 0.5; two hearers with opposite pursuits and the same deed claim get regard of opposite sign, both 0 at control, no stance rows `:1838-1863`; `person.died` (a `PAIRED_KINDS` claim) judges nothing for its subject; a refusal kind is no deed `:1866-1939`. `stance_polarity` ships `declared`: a grudge raises `fight`/`determine`/`arrest` on its object, `legacy` ranks them the other way `:2017-2096`. `said_slant` ships `newest`; `valence` tells the older strongly valenced deed `:2113-2149`.
  - R-07 REALM READER `:1964-1987`: two-season `build_realm(0)` at the SHIPPED gains: control arm (both gains 0) shows `differ == 0`, live arm `differ >= 1` for pairs of persons holding a claim about one C whose `regard - stance_toward` differs -- an existence claim, but on the realm, shipped fixtures. This partly contradicts `F-TEST` section 3's "R-07 feeling, attitude, relationship: no test".
  - G6: `telling_privacy` ships 0; at 1.0 a private telling deposits `visibility == (teller, addressee)` for both addressee and bystander; retelling outside the circle emits `confidence.broken` (at Success, Partial and Overwhelming); inside the circle or by the confider breaks nothing `:2220-2335`. DOCUMENTED LIMIT (C1(i)): the production `said` pick (newest-first) shadows the confided copy with the hearer's own `news.told` claim, so the break path is NOT reached in shipped play; the repair "moves the shipped told channel and the hashes, and is not built here" `:2261-2284`.
- **Conflicts / stale:** (1) F-TEST row R-07 lists "Feeling, attitude, relationship: no test"; `test_r07_realm_regard_differs_between_hearers_by_claim_not_stance_alone` `:1964` and G1 tests exist (existence claim, realm, two seasons, control arm). (2) `test_t3_unplanted_members_with_opposite_loyalty_reach_different_verdicts` `:474` must sweep `loyalty_toward_creed` to False because CR-87 made build-time loyalty name the creed, so "no unplanted row toward a leader exists on the shipped build" `:503-507` (the premise is reverted in process). (3) The realm falsifier's seed pin is chosen to make it pass `:301`. (4) `intent_disclosure` 0, `telling_privacy` 0, `said_slant newest`: three telling mechanisms (intent disclosure, confidences, slant) ship OFF or neutral; tested live only on `tiny_world`.
- **Open items:** `said_of` excluding the hearer's own `news.told` claim (R8.1 `seen` precedent) so a confided copy can be broken in play, not built `:2269-2271`. Mechanism by which 13d-iii lowered chained claims "not isolated" `:249-261`.

### engine/season/tests/test_u7_own.py
- **What it is:** pytest file, plan position `14` (U7-own): the fold's counterparty clause over every counterparty row; self-loop `give`; bare-string `oblige`; the always-refused verb set not growing; `destroy_record`'s hold as an arm; `give` formable; `Candidate` has no `why`.
- **Status:** no Status line. Reading: live. Named in F-TEST as read at flagged tests (`:1-?`).
- **Bears on:** CORE (verb table, fold admission), FA (obligations), FI (records).
- **Content that matters:**
  - For EVERY `VERB_TABLE` row with a `counterparty`, an act naming the actor or nobody is refused with the row's own counterparty refusal, with eligibility and precondition stubbed open (`dataclasses.replace(row, eligibility=("own",), requires="—")`); control names another person; `checked == len(rows) >= 1`; exactly one row (`confer`) has `counterparty_may_be_self` `:77-106`.
  - A `give` to oneself opens nothing and leaves custody unchanged (control: to another moves the hold) `:122-136`. Bare-string `oblige` (`einhir_texts`) is `duty.refused` and opens no edge; a real seat (`off_dicastery`) opens one `:143-153`.
  - `DECLINED = ("tie / knot",)` is the one remaining declined row, and `resolvable_verbs()` must not contain it; untyped counterparty rows that no person can bind are exactly `["interrogate","oblige"]` `:61,160-181`. The comment history shows `repudiate`, `forge`, `carry`, `thread_read`, `exchange`, `succeed` each LEFT the declined set at named positions `:41-60`.
  - `destroy_record` is held out of formation by `Fixtures withheld_verbs` at the shipped arm (A-13, H-156): `"destroy_record" in w.fixtures.get("withheld_verbs")`; at the sink arm it forms only on the held Record `:187-205`. Control: the holder forms other verbs on the same referents.
- **Conflicts / stale:** `tie / knot` appears as a verb name with a slash (a row that is a decline placeholder). `engine/season/tests/test_in26_record_sink.py` is the named owner of the rest.
- **Open items:** none.

### engine/season/tests/test_u7_remit.py
- **What it is:** pytest file (1,244 lines), plan position `19` U7-remit plus SC-03a/SC-03b plus IN-49: the four remit verbs `requisition`, `open_case`, `determine`, `issue` through the seat (`Act.via`), the keyed `emits_on_refusal` schema, the docket, the gate's `determination`/`warrant`/`seizure` bases, `detain`/`ban` restraints, the contested `determine`.
- **Status:** no Status line. Reading: live. F-TEST read it at flagged tests; read here in full.
- **Bears on:** FA (offices, seats, remit, docket, restraint), SC (determine, arrangements, `contests: a proposition`), SE (requisition of larders), CORE (gate bases, fold, R-04).
- **Content that matters:**
  - Plan's falsifier: none of the four executes with `via=None`, run twice (eligibility refuses; and with eligibility forced open the `basis` conjunct refuses, verdict `UNKNOWN`, not False) `:175-221`. `requisition` moves matter from the rung into the seat's treasury, conserved, both rungs on the Event; two requisitions of one larder in one fold: second `requisition.refused` carrying `("stores:grain", 0)` `:228-255`; a requisition of `R` above the Duke's purview is `requisition.unauthorized` naming `purview:off_duke` `:258-266`.
  - `determine` is CONTESTED (SC-03b, `contests: "a proposition"`, provider `social_contest.roll`): a determination executes at the band the judge's roll decides. At the shipped `pool_default` 2 vs obstacle 2 "most rolls are `Failure`" so tests take a STRONG JUDGE `pool_default: 30` and assert the band (`OPENS = Overwhelming, Success`) `:58-65`. Runtime test: two judges (pool 2 and 12) x 40 act ids each; all four bands occur (`set(seen) == BANDS`, `sum(seen.values()) == 80`); Failure -> `matter.undetermined`, no edge, matter still docketed; other bands -> `matter.determined` with `edge.degree == band` `:1180-1207`; an undetermined matter can be re-heard (200 act ids) `:1210-1230`; a judge pool under one die is refused (S27.4) with no degree `:1233-1244`. Also `Failure` writes nothing, `Partial` writes the three disposal pairs, `Success/Overwhelming` add `Person.pursuits` and `pursuit.moved` `:1138-1145`.
  - Bench quorum (`bench_quorum` swept 1,2,3; `tiny_world` bench for `Hh` is ONE person) below quorum is `determine.refused` carrying `bench.size`/`quorum` reads `:354-368`. `judging_set` and `may_determine` read one bench over every person (`sits_over`) `:480-494`.
  - Gate: the `determination` basis refuses each missing clause (no seat, outside the ground, no bench grant, another seat, not seated) with the store put back `:424-447`; a determination OPENS a disposed kind and CLOSES a `detain`/`ban` and re-grades nothing; closure of a `hold` on a Record is admitted as `seizure`, not determination `:754-801`; `warrant` basis opens a `detain` only for a seat granted `dispatch` over a prisoner in purview `:820-846`; an owner cannot open or close his own restraint (T-m excludes `detain`/`ban`) `:849-875`.
  - Consequences: a `ban` blocks `oblige` (`duty.refused`) and `confer` seating; `detain` blocks `move` (`travel.blocked`) and `migrate`; a ban does not stop travel; a mustered army excludes persons in custody; the party's `release` of a `ban` is refused, of an `oblige` closes it `:700-751,878-915`.
  - IN-49: a computed `requisition` forms only on a `Rung`-classed larder inside the seat's purview with stock `larders_in_purview`; refused arms for the realm `R`, the seat's own treasury `D` and an empty larder; the requisition's kind/amount come from fixtures (`default_store_kind`, `default_transfer_amount`) not from claims about the rung, with a `transfer` control that reads the claim `:981-1109`.
  - Loader: 7 planted defects on `requisition`'s keyed `emits_on_refusal` each fail the load naming it `:564-599`.
- **Conflicts / stale:** `issue` (a writ) and `open_case` and `requisition` execute DETERMINISTICALLY once admitted (no roll): `issue` mints a `dispensation` Record, `requisition` moves exactly `default_transfer_amount`, `open_case` dockets; under the brief's DO-NOT-DO-DETERMINISTIC rule ("a decree binds") these are eligibility-gated but their consequence is a fixed function of state [UNVERIFIED whether the later compliance/obedience step draws]. `determine`, by contrast, is already a draw. Cites `21_RECONCILIATION.md:575`, `04:120`, `04:330`, `04 §B.13` (design docs; `.designs/` archive).
- **Open items:** none.

### engine/season/tests/test_u8_ambitions.py
- **What it is:** pytest file, plan position `17` (U8): `world_q.ambitions(w, p)` and `corpus_run.build_at`'s cast (the NPC corpus runner).
- **Status:** no Status line. Reading: live.
- **Bears on:** CHAR (ambitions, cast), ARCS (cast seating, `WAITS-ON-PLAYER`), CORE (corpus harness).
- **Content that matters:**
  - `ambitions` = LIVE `commit` edges to OUGHT Propositions off the person's OWN tenures; each of 4 distractors (ended, `hold` not `commit`, `commit` to HOLDS, `commit` to unknown id) tried alone returns `[]`; faction creed (OUGHT commit) IS an ambition; HOLDS only for `Guilds`, `Schoenland`, `faction x` `:61-118`.
  - `cast:` seating: `p_b`/`p_c` named from the cast; an 11-entry cast seats 11 and RUNS (`r["checks"]["R1"] is True`, `executed` non-empty, `len(actors) > 3`); a `WAITS-ON-PLAYER` entry is not seated and is reported; capability lands on its own seat only `:151-203`. Control: NPC-020 has no overlay and builds three anonymous people `p_a,p_b,p_c`; a one-entry cast changes only the name (hash differs, then tally equal after renaming) `:229-254`.
  - Q4 (`questions_for` `need` source) fires once per ambition per person: 3 propositions before, 11 after a cast of 11 `:266-290`.
- **Conflicts / stale:** the comment on `person_q` vs `world_q` placement (a deleted AX-2 guard test) `:24-28`. Knowledge -> initial Claims is REFUSED by name at load (tested in `test_u8_cast_fields.py`).
- **Open items:** none.

### engine/season/tests/test_u8_cast_fields.py
- **What it is:** pytest file, plan position `17-cast`: a `cast:` entry's `office:`, `ought:`, `capability:` and the refusal of `knows:` in `harness/corpus_run.py`, plus overlay-loading integrity (`cast_overlay`, `rescales`).
- **Status:** no Status line. Reading: live.
- **Bears on:** ARCS (the provided characters' overlays: NPC-038, NPC-088 Carin Vedel), CHAR (capability, ambitions), CORE (corpus harness).
- **Content that matters:**
  - `office:` is seated by `_seat_office` (mutation: a no-op seater makes `_held` empty) `:58-75`; a first cast entry may not carry an office beside a case-level one (`Forbidden`) `:85-102`; a titled post (Duke, etc.) must stand at the rung kind its title governs (`TITLE_DOMAINS`), refused on both caller paths, `len(wrong) >= 5` `:109-147`.
  - `ought:` replaces the rotation default (next seat) for that entry only; mutation `C._referent` pointed at the wrong seat is seen `:160-199`.
  - 21 load refusals: unknown key, `knows:`, malformed `ought`/`office`/`capability` (capability key no verb draws on, non-integer magnitude), waiting entries carrying office/ought/capability, non-list cast, missing/blank/misspelled `case:`, two files for one case, two scale files for one case; each with a positive control `:219-419`.
  - The checked-in overlays: `len(real) >= 13` cast files; NPC-088's `Carin Vedel` `capability == {"copying": 3}` `:283-285,418`; every authored `office:` is held and every authored `ought:` is a live ambition with `offices >= 1 and oughts >= 1` asserted `:426-443`.
- **Conflicts / stale:** `knows:` (initial beliefs) cannot be authored in a cast ("no builder here constructs a Claim, AX-7") -- relevant to ARCS: provided characters' starting beliefs have no authoring route in the corpus runner `:15-16`.
- **Open items:** none.

### engine/season/tests/test_works_founding.py
- **What it is:** pytest file (886 lines), plan position `24e` WORKS & FOUNDING (+ IN-45 formation, IN-28 cost): a `works` Record, `ceiling` of matured terms, `share`, `restore`/`work` through one clamped rise, `found` (new Rung under the `founding` gate basis), `build` (new Site at condition 0), cost and hold.
- **Status:** no Status line. Reading: live. F-TEST read it at flagged tests.
- **Bears on:** SE (works, settlements, founding, dwellings, capacity), FA (holdings), CORE (gate bases).
- **Content that matters:**
  - A works is a `Record` of kind `works` `{plan, at}` minted by `create_record` with its maker's `hold`; one live works per target (a second is `act.refused`, a released one frees the target) `:111-139`.
  - `ceiling = scale x matured // declared` read off `term.matured` Events: 0, 333, 666, 1000 over three barriers; the seam (no works) reads the full scale; a works whose master died bounds nothing and stops ripening `:146-195`. `share = (1, n)` persons present floored at one `:166-176`.
  - `work` advances a works (500 -> exactly 666 with 2 of 3 terms ripe, one person present) and a `text` Record is NOT advanced (`work.unavailable`) from one body, two arms `:202-222`; declared delta still wins but is bounded and never cut (`max(condition, ceiling)`) `:237-253`; `restore` raises to the ceiling then stalls (`restore.refused`, "you cannot hurry mortar") `:305-318`; two present each stage half and fold order does not matter (S27.3 sum-then-clamp-once) `:281-302`.
  - `found` mints one Rung of the plan under `at` ("census shows exactly one more rung"), admitted under the NINTH gate basis `founding`; seven refusals each make nothing; paid from the works' rung (stake moves; grain conserved two-sided) and held by the founder `:342-402,775-809`. `build` makes a Site at condition 0, once; priced via `works_cost`; unpriced plans (`body`, `settlement`) refused; the price is the only difference between executes and refuses `:434-450,839-886`. A full rung still grows: `found`/`build` never consult `capacity`/`population` (both patched to raise) and every ancestor's capacity rises by exactly one `:453-497`.
  - Lifecycle end to end: declare, ripen, `found`, `build`, move in, `restore` exactly as far as terms allow (666 then full) `:500-524`.
  - COMPUTED PLAY GAP: "what is missing in computed play is the PRODUCER, a computed `create_record` that declares one (limit 2)" `:551-554` -- no chooser forms a works; `found`/`build` form on a works the maker holds only after a hand-built `create_record`. "Where a works comes from in computed play is ED-IN-0297's open question" `:765`.
  - A founder's `hold` makes `holder_faction_of(hearth)` read `None` unless the founder is committed to the faction (pinned "as it reads", not blessed) `:812-836`.
- **Conflicts / stale:** All deterministic (no draw anywhere in works/found/build/restore; the amount raised is arithmetic); under the brief's rule these are bookkeeping and eligibility, but the outcome of whether a work "goes well" has no band. `workplans/2026-09-18-governance-settlement-behaviour-plan_part2.md` cited as the source (a retired workplan [UNVERIFIED]); r2 `proposals/2026-09-17-governance-and-holdings-r2/04_MATTER_AND_WORKS.md` cited as content owner. `:553-554` states no test asserts anything about the seed-0 realm (v9 §0.5).
- **Open items:** the producer of a works in computed play (ED-IN-0297); `raze` as the closer (H-166 design order (3), IN-12 step 11).

### engine/tests/test_band_odds.py
- **What it is:** pytest file, CP-T01-03: `sigma_leverage.band_odds`, the exact four-band odds of one d10 pool roll, enumerated over `dice_engine`'s own face table and graded by its own ladder.
- **Status:** no Status line. Reading: live; F-TEST section 4 names it among the strongest (closed form vs brute-force walk, with a count).
- **Bears on:** DICE (R-09, probabilistic chains), SC (sigma-leverage), CORE.
- **Content that matters:**
  - Worked case `band_odds(2, 2) == (0.74, 0.19, 0.07, 0.0)` asserted with `==` (exact because integer counts over `10**pool`) `:39-40` -- an exactness claim asserted exactly, not by `approx` (a model for CLAUDE.md §0.1 pt 2). Face table: -1/0/+1/+2 at 10/50/30/10 per cent (`:6-7`).
  - Sweep: 5 pools x 6 obs x 4 boosts = 120, sums to 1 within `1e-12`, `checked == 5*6*4` `:43-52`.
  - Brute-force walk of all `10**3` faces for pool 3 at three (ob, boost) cases with the fraction rule written independently; `math.isclose(..., abs_tol=1e-12)` against enumeration (a float tolerance on a derived sum, defensible) `:55-76`.
  - MUTATION in test: swap Partial/Success edges of `degree_from_net` and the tuple moves to `(0.74, 0.25, 0.01, 0.0)`, proving `band_odds` reads the owner and holds no ladder copy `:79-94`.
  - Boost is a mu-shift never an Ob change; larger boost never lowers clearing; pool is rounded and floored (`max(1, round(pool))`) as `roll_net` does `:97-119`.
- **Conflicts / stale:** the sampling arm that "agrees with the dealt distribution" was moved to `test_settle_margin.py` (single sampling arm for the whole rule) `:9-18`.
- **Open items:** none.

### engine/tests/test_contest_kernel.py
- **What it is:** pytest wrapper that runs the promoted groundup contest kernel suite `systems/social_contest/sim/contest/_kernel_tests.py` as a subprocess and asserts its `RESULT: N passed, 0 failed` line.
- **Status:** no Status line. Reading: live but a retiring subject; F-TEST section 4 and T-12 say it follows `05_SC_sc05_kernel_retirement.md` (SC-P2). The kernel suite file exists (checked).
- **Bears on:** SC (the off-loop contest kernel), DICE, PROCESS.
- **Content that matters:**
  - Asserts exit code 0, `failed == 0`, `passed >= 151` (the "behavior-preserving floor") and `passed == 389` (`_KERNEL_EXPECTED`) `:110-124` -- it pins a COUNT of an inner script's own checks, not a behaviour; any added or removed check anywhere in the kernel suite reddens it, and any bad check inside still reds it with the count unchanged.
  - Retraction in the comment: "All 151 stay green" is RETRACTED; ED-SC-0031 re-pinned four of the original 151 (the degree bands and three sigma-leverage band checks moved one step per Jordan's 2026-08-14 ladder ruling) `:83-88`.
  - The giant comment `:93-107` is a re-pin history of 389 (385 -> 389 by ED-SC-0031; breakdown of 319 through Gate B), citing `social_contest_v30`, ED-1056 (Face_max = Charisma x 3), ED-1057 (Panel aggregation weighted-by-standing), ED-1059, ED-1061, CR3 three-tracker model (Concentration, Face, Persuasion Track; Composure RETIRED), CR4/CR5 stasis x genre and self-gating.
  - Docstring at `:1-58` still says "Total 303" and "151-check"; the pinned figure is 389 -- the docstring is stale against the constant.
- **Conflicts / stale:** archived-doc references: `designs/audit/2026-06-30-contest-stage0-reconciliation`, `params/contest.md`, `RATIFIED_2026-06-01.md`, `social_contest_v30` (all dissolved/archived paths). `systems/fieldwork/sim/knots.py:85` still carries `BREAK_COMPOSURE_DAMAGE = 4` ("Both partners take 4 Composure") while this kernel retires Composure (see `test_knots_ed912.py`) -- a retired-term residue [verified by grep].
- **Open items:** retires with SC-P2.

### engine/tests/test_knots_ed912.py
- **What it is:** pytest regression for ED-912: `systems/fieldwork/sim/knots.py` runs a bidirectional -5..+5 bond-strain gauge (C-TW-12), plus a conviction-scar falsifier.
- **Status:** no Status line. Reading: live as the oracle of a RETAINED off-loop subsystem (F-TEST section 4: `knots`, `thread_mending` kept by ED-IN-0283); "knots/ is an island (no campaign callers)" `:17`.
- **Bears on:** FI (fieldwork knots), WR (threadwork), CHAR (conviction scar), CORE (off-loop).
- **Content that matters:**
  - Gauge: Distant range -2..+5 (start 0), Close -5..+5 (start -2); break/rupture at +5 for both tiers; -5 is Tempered (Close only) absorbing one rupture trigger (reset to 0) then rupturing; break/betrayal-rupture Disposition -3 (revised from -4) floor -5; a Close knot that broke from POSITIVE strain gets Conviction Scar +1 `:11-17,51-124`.
  - `test_ed912_formation_starts_at_tier_gauge_start` loops 80 seeds and asserts `formed` > 0 (asserts it asserted) `:51-63`.
  - FALSIFIER (the best part): the first scar test only asserted the consequences dict knots.py wrote for itself; the Scar never landed because knots.py passed `conviction='Loyalty'`, an unknown name that returned a magnitude-0 record. The new test reads the SCAR STORE before and after (`scar_counts.get("honour")`) and `apply_conviction_scar` raises `ValueError` on unknown or legacy names (`Reason`, `Autonomy`, `Continuity`, `Honor`) `:127-175`. Pursuit `honour` replaced `Honor` (IN-08 cells) `:145,168`.
  - `coherence_delta == -1` is tagged `[UNVERIFIED post-ED-912]` in its own test `:124`.
- **Conflicts / stale:** `BREAK_COMPOSURE_DAMAGE` residue (see test_contest_kernel entry); Disposition/Composure/Coherence vocabulary is pre-v40 sim vocabulary [UNVERIFIED current].
- **Open items:** `[UNVERIFIED post-ED-912]` coherence delta.

### engine/tests/test_settle_margin.py
- **What it is:** pytest file, CP-T01-04: `sigma_leverage.settle_margin` -- the fraction of a margin settled by the act's own uniform -- and `band_odds` enumerating that same rule.
- **Status:** no Status line. Reading: live; F-TEST: strongest tier.
- **Bears on:** DICE (R-09), SC, CORE (seam: its host twin is `test_settle_margin_seam.py`).
- **Content that matters:**
  - Rule: `m = raw_net + floor(q) + [u < frac(q)]`, `q = boost - ob`; the extra uniform is drawn ONLY when `frac(q) > 0`, so whole-Ob rolls keep their stream `:5-11`. Expected margin preserved exactly: mean settled margin `= 0.4*pool + boost - ob` to `1e-12` over pools 1-8 x 13 obs x 13 boosts `checked == 8*13*13` `:69-78` (a mean over exactly enumerated nets, so a tolerance, not an approx on an exactness claim).
  - P(Partial or better) strictly increasing in boost and strictly decreasing in Ob wherever interior, `steps > 500` asserted `:81-96`.
  - Whole margin draws nothing (a `_no_draw` that raises) `:99-106`; fractional margin draws exactly one uniform: `u=0.49 -> +1`, `u=0.50` and `0.99` -> not (strict `<`) `:108-122`.
  - `band_odds` hand-enumerated cases `(0.58, 0.255, 0.16, 0.005)` at Ob 1.5 and `(0.42, 0.32, 0.25, 0.01)` at Ob 1; brute force through `settle_margin` itself `:125-150`; six parametrized sampling arms at n = 100,000 seed `20261101` within 3 SE (`seen == 4`) `:156-173`.
  - mu-shift not Ob-change: `settle_margin(net, 0.5, 2.0, u)` equals `settle_margin(net, 0.0, 1.5, u)` `:176-180`; `record_odds`/`settle_record` are the two owners over a record's fields `:183-194`.
- **Conflicts / stale:** none; numbers like "100,000 draws resolve a band to 0.47 points" are test-design reasoning `:153-155`.
- **Open items:** none.

### engine/tests/test_sigma_leverage_parity.py
- **What it is:** pytest file, 619 lines: parity of `engine.dice_engine.sigma_leverage` against a committed golden table `engine/tests/goldens/sigma_leverage_parity.json` (1,758 rows) plus oracle-free property/identity tests.
- **Status:** no Status line. Reading: live; F-TEST-08 judged this file (58 % rows refused or contradicted) -- confirmed below.
- **Bears on:** DICE (resolution core, sigma-leverage, TN7), SC (degree extension), CORE.
- **Content that matters:**
  - TN7-ONLY PARTITION (ED-IN-0196, Jordan: "TN7 always. Never change TN anywhere ever."): 768 of 1,758 rows are TN 6/8 and are re-purposed as `KeyError` assertions (one row per TN exercised) `:62-77,195-205`; the table is NOT regenerated (`:29-30`, 'never to make a red test green'). Confirms F-TEST-08 (768 rows) `:187`.
  - PRE-RULING-LADDER PARTITION (ED-SC-0031): the 255 `degree` rows leave the parity arm; 47 moved cells, 208 kept; asserted as a SET (`by_ob == {1.0: 9, 2.0: 15, 3.0: 23}`) plus `len(moved)==47 and len(kept)==208` and that no cell bands UP `:208-252` -- so the file pins counts of a retired oracle (confirms F-TEST-08 "255 pre-ruling ladder rows checked as two counts"). `test_golden_table_is_not_vacuous` pins `by_oracle["m1"] >= 731`, `["groundup"] >= 4`, `len(_PRE_RULING_DEGREE_ROWS) == 255`, and the function set `:157-177`.
  - Parity at `TOL = 1e-9` on floats with `==` for others `:115,148-154`; 735 live rows.
  - Properties: `sigma_n = 0.8*sqrt(max(1,pool))`, `soft_cap = M_MAX*tanh(ns/M_MAX)` with spec checkpoints `(0.5,0.48),(1.0,0.87),(2.0,1.31),(3.0,1.45)` to 2 dp, `sigma_space_ob_shift == ns*sigma_n` exact, F1 uniformity (+0.7 sigma gives +25.8 pp at every pool; spread rounds to 0.0) `:259-398`.
  - `TestPoolAwareDegree`: `CD.degree` equals the owner's `degree_from_net` over a 61 x 81 grid (`checked >= 4000`), the contest extension may only demote Overwhelming to Success, and de-saturates (pool 30: owner's Overwhelming > 0.9, with extension < 0.25; crossover pools `[6, 8, 10]` for obs 1,2,3); `demoted >= 100`, `checked >= 9_000` `:453-589`. An earlier algebraic-identity assertion that "could not fail" was replaced and said so `:509-523`.
  - The `degree_extension` module under test is `systems.social_contest.sim.contest.degree_extension`, imported by no loop/module code (matches F-TEST evidence row 16).
- **Conflicts / stale:** `modifier_system_spec.md` §3.1/§2.1 cited for spec checkpoints (prose referent); the TN-6/8 and 255-degree rows are 1,023 dead golden rows (F-TEST-08 / T-11: regenerate at the generator). The header says the file used to import oracles `tests/sim/v32-combat-balance/m1_dice_sigma_core.py` and `audit/2026-06-03-contest-groundup/engine.py` (retired paths; only referenced in the generator).
- **Open items:** none.

### engine/tests/test_thread_mending_ed871.py
- **What it is:** pytest regression for ED-871: Mending (a RESTORATIVE threadwork operation) costs 0 Coherence at every degree; `systems/threadwork/sim/operations.py`.
- **Status:** no Status line. Reading: live as an off-loop oracle regression (F-TEST section 4: retained subsystem, ED-IN-0283).
- **Bears on:** WR (threadwork), PROCESS.
- **Content that matters:**
  - 300 seeds of `attempt_mending` each assert `coherence_delta == 0`; asserts Partial/Failure degrees occurred (`degrees & {"Partial","Failure"}`) so the exemption is observed `:39-49`.
  - Control: `attempt_weaving` at Relational scale costs -1 on Success/Overwhelming and -2 on Partial/Failure, guarded by `saw_penalized` `:52-70` -- the exemption is Mending-only.
  - The Leap defect C-TW-3 (same blanket penalty hits Leap against its own docstring) is "intentionally NOT fixed" (ED-WR-0005 Stratum-B tail) `:17-19`.
- **Conflicts / stale:** Coherence is the pre-v40 sim currency; "sim/thread was a total island" `:9`.
- **Open items:** C-TW-3 Leap Coherence defect.

### tests/valoria/_conservation.py
- **What it is:** helper module (not a test file): ED-MB-0045 A4/S6, the single owner of the mass-battle I1 troop-conservation check `Sum(cell_troops) == hp`.
- **Status:** no Status line. Reading: live helper for four+ MB acceptance suites.
- **Bears on:** MB (cells vs hp ledgers, conservation), PROCESS.
- **Content that matters:**
  - `assert_troop_conservation(*units, context='')` checks EVERY unit including routed/broken (the old uncounted `continue` skip was removed) and RETURNS the count so each call site can assert it checked; the docstring is candid that a call-site `checked >= 2` "cannot fail today, and that is its declared purpose" (a forward guard) `:83-90`. It first asserts `modules.mass_battle.config.PER_CELL` is on, since at PER_CELL=0 hp falls and cells never move so the invariant is false of correct behaviour `:59-62,91-94`.
  - TOLERANCE `REL_TOL = 1e-6`, `ABS_TOL = 1e-3` via `math.isclose` `:69-70,99`, justified as float slop with a measured worst case of `4.5e-13` `:47`. This is an `isclose` on a conservation (exactness) claim with an abs tolerance 9 orders above the measured slop (F-TEST flags `_conservation.py:99` `[not adjudicated: MB]`; here adjudicated: defensible as slop but loose enough to hide a sub-0.001-troop-per-exchange leak).
  - KNOWN UNTESTED DIVERGENCE (recorded, not fixed): `distribute_casualties` DISCARDS `_apply_with_spill`'s returned applied amount (`percell.py:179`) and spills only across the engaged front (`:162-172`), so `Sum(cells) > hp` whenever dmg exceeds the engaged front's live troops; no unit in 560 measured came near it because rout ends battles first `:49-57`. Sibling: `tests/valoria/test_hp_cell_ledger.py`.
  - Measured at shipped defaults 2026-07-29 (`MB_STOCHASTIC_ROUT=1`, `MB_CELL_MORALE=0`): Line-vs-Line routs 0 of 120 units in 60 seeds, pike-vs-cavalry 8 of 120 `:19-26`; flagged AGENT-MEASURED, orchestrator-unreplicated `:43-47`.
- **Conflicts / stale:** line references to `orchestration.py:1966-1967`, `:2504`, `:2566`, `:1695`, `:1968`, `percell.py:108-129` are 2026-07 line numbers [UNVERIFIED current].
- **Open items:** the engaged-front spill shortfall (`percell.py:179`) remains a real, untested divergence class.

### tests/valoria/_draw_stream.py
- **What it is:** helper module: W8d single owner of the personal-combat RNG DRAW-STREAM instrument (`static_draw_sites()`, `RecordingRandom`, `engine_draw_sites`, `underlying_random_calls`), the measuring device behind paired-seed comparisons in `combat_completion_plan_v4.md` §4.
- **Status:** no Status line. Reading: live helper for PC tests.
- **Bears on:** PC (combat RNG stream, paired-seed control), DICE.
- **Content that matters:**
  - Two measured facts it exists to keep true `:32-42`: (1) draw count is input-conditional: one seed, longsword vs arming: 57 underlying `random()` draws at `armour='none'` and 168 at `'heavy'` (2.9x), so "same seed" across armour contexts is not the same experiment; (2) `random.Random.gauss` caches the second Box-Muller variate so k calls consume `2*ceil(k/2)` underlying draws, shifting the bare-`random()` sub-stream by 0 or 2 depending on prior resolutions (`core.resolve -> sigma_leverage.roll_net_continuous -> dice_engine` calls `gauss` on the object the engine draws `random()` from).
  - `static_draw_sites()` is an AST inventory of every `rng.<method>(...)` call (`random, randrange, uniform, betavariate, gauss`) across `modules/combat`, `systems/combat/combat_engine_v1` and `engine/dice_engine/dice_engine.py`, reachability-independent so a new draw on a cold branch cannot be missed `:53-105`.
  - `RecordingRandom` subclasses `random.Random`; `trace` = engine-level (module, line, method), `underlying` = every `random()` including nested; frame offset 2 "is exact, not tuned" after an earlier off-by-one attributed 6,470 draws to one line `:148-159`.
- **Conflicts / stale:** `static_draw_sites` silently `continue`s on a missing path or `SyntaxError` `:92-97` (a dropped tree reads as fewer sites, so only a pinned shape test can see it).
- **Open items:** none.

### tests/valoria/_structure_audit.py
- **What it is:** helper module (ED-IN-0123): single owner of the loader for `skills/valoria-vector-audit/scripts/structure_audit.py` (a script, loaded by path via importlib, cached).
- **Status:** no Status line. Reading: live helper; process-only.
- **Bears on:** PROCESS.
- **Content that matters:**
  - Exists because three test files each re-implemented the loader (`test_structure_audit.py::_load`, `test_import_cycle_game_state_npe.py`, `test_oi12_orphan_census.py::_load_structure_audit`); the third's docstring falsely claimed reuse `:3-9`; the duplicated-helper ratchet in `tools/build_test_register.py` surfaced it `:10-11`.
  - `load()` caches the module in a global `_cached` `:22-33`.
- **Conflicts / stale:** subject (`valoria-vector-audit` structure audit) is a process tool with no game bearing; per CLAUDE.md §0.1 pt 5 a guard on process-only artifacts "can be wrong without cost".
- **Open items:** none.

### tests/valoria/conftest.py
- **What it is:** pytest configuration for `tests/valoria`: the KNOWN-RED register (W1, ED-MB-0061) and the session-scoped GENERATED LAYER fixture (`generated_layer`, `generated_layer_paths`).
- **Status:** no Status line. Reading: live; process-critical.
- **Bears on:** MB (known-red set), PROCESS (gate hygiene), CORE (generated artifacts).
- **Content that matters:**
  - `KNOWN_RED` holds THREE strict-xfail ids today `:34-44`: `test_conditional_orders.py::test_own_strength_fires_when_attrited` ("own_strength order never advances `_order_idx`" flags-ON residual, ED-MB-0061 Track F), `test_dg2_yield_residuals.py::test_rally_keeps_pressured_yielding_subunit` (rally clears yielding below the rally fraction, DG2 residual), `test_stochastic_rout.py::test_per_cell_break_subsumes_the_body_level_one` (per-cell and body-level break points separated again). These are applied as `xfail(strict=True)` at collection `:47-53`. F-TEST-10 mentions only the non-strict xfail in `test_mass_battle_maneuvers.py`; these three strict known-reds (all MB) are additional standing reds the addendum did not list. A fourth (`test_conditional_withdraw_fires_when_enemy_closes`) left the set at B10-12 (MB-07r) after recalibration `:35-37`.
  - The reverse guard `test_known_red_register.py` (asserting each id is collected) was DROPPED 2026-11-04 (ED-IN-0312), so a renamed or deleted test leaves a stale entry that "excuses nothing" `:22-25`.
  - Generated layer built on demand, never committed (culling wave 5, ED-IN-0194): `_GENERATED_LAYER = (build_engine_atlas.py -> engine_atlas.json/ENGINE_ATLAS.md, build_identifier_census.py -> identifier_census.json, definitions_store.py --build -> references/definitions/definitions.yaml)`; a retired builder is silently skipped (`continue`) `:101-125`. Exactly ONE xdist worker builds via an `O_CREAT|O_EXCL` lock and a `.done` marker; others block up to 900 s `:148-181` (known cost stated: a dying builder looks like a ~15-minute hang).
  - Comment history: `keys`-based builders and the execution-map cluster were retired (ED-IN-0232; `FORK:6f740d9`) `:85-100`.
- **Conflicts / stale:** the stated count ("FOUR edges/builders lost", "TWO MORE ROWS LEFT") are hand-maintained comment prose. `references/definitions/definitions.yaml` is a generated game-term store [UNVERIFIED reader].
- **Open items:** stale KNOWN_RED entries are unguarded since ED-IN-0312.

### tests/valoria/test_army_battle.py
- **What it is:** pytest file, ED-IN-0306 phase 3: an army Record fights as its order of battle (`seam/wrappers/mass_battle.py::field_input`, `mass_battle.army_order` composition row), on the realm with planted weight-12 cohorts.
- **Status:** no Status line. Reading: live (mass-battle/season seam, army chain).
- **Bears on:** MB (armies, order of battle, casualty loop), SE (cohorts as troops), FA (faction armies), CORE (seam).
- **Content that matters:**
  - A field with no army Record is the field it always was (`orders_of_battle is None`); each side with an army Record fights as that Record's OOB; the faction's `strategy`/`stance`/`fall_back_at` orders reach the battle; a cohort not mustered at the origin leaves the side `None`; troops on the field = cohort's body fraction of its assignment (120 at full, 60 at half, none at body 0) `:73-130`.
  - A headcount side meeting an OOB is scaled to `under_arms_cap(12)` (> 12) so households are not counted against troops; an empty side keeps the crash floor (>= 1) `:132-139`.
  - Provider end to end: `resolve(..., rng=Random(11))` finds both factions' armies (120/120) `:147-164`. CASUALTY LOOP: no write of the army Record, yet the loser's next army is smaller by its cohort's body fraction `abs(troops - 120*body/scale) < 1e-6`; exactly one side bleeds; bystanders mustered beside the cohorts are unhurt `:177-203`.
  - Comment: "two plain lines: a held shield wall against a balanced line can end with nobody having closed (no casualties)" `:180` -- a fixture chosen so a fight produces casualties.
- **Conflicts / stale:** `proposals/2026-10-29-army-phase5-design.md` is the design referent (see next entry). Uses `test_levy_feed.py`'s realm [UNVERIFIED].
- **Open items:** none.

### tests/valoria/test_army_menu_presets.py
- **What it is:** pytest file, ED-IN-0306 phases 5b/5c: the headless military menu (`harness/military_menu.py`) and preset orders of battle (`harness/army_presets.py`, `modules/mass_battle/troop_types/presets.py`).
- **Status:** no Status line. Reading: live.
- **Bears on:** MB (army raising, doctrine presets, advisories), GO (menu surface for a client), FA (faction without a player), CORE (play surface / R-04).
- **Content that matters:**
  - Falsifier of "the menu adds no rule": every (cohort, troop type, room) the options list is accepted by `A.apply` at `room` and refused at `room + 1`; a type with no Site (archers w/o range) is absent and refused `:62-81`; the same through the real fold: sample rows `[::9]`, `room` accepted and `room+1` `recruit.refused`, `checked >= 6` `:128-140`.
  - Menu follows the army: mint, then commands; `describe(m)`; the menu-driven chain recruit -> form -> assign -> order -> disband -> discharge is reversible ("what makes a wrong choice recoverable") `:107-118,143-168`. `callback` hands the menu to a client via `dispatching_chooser`; a return over the budget raises in DELIBERATE `:183-198`.
  - Presets: `plan` is pure and order-independent; recruit -> form -> assign; cavalry `Flanker`, levy `Reserve`; levy alone without Sites; an empty plan under 4 weights ("90 troops clear a subformation's floor but not a unit's block: it would rout at once"); a group that would rout is dropped and given to the levy; other armies' claims counted `:210-256`. `install` through the real fold yields 900 troops (`15 * under_arms_cap(2)`), deterministic, idempotent, leaves other factions alone `:265-293`.
  - NAMED LIMIT: "The shipped realm seats no barracks, range or stable, so its preset army is levy alone: 900 troops, one subformation" `:296-303`.
  - Preset army with sites beats a town's levy: `with_sites >= 5` of 8 seeds and `with_sites > levy_only` `:306-322` -- a small seeded-sample claim (8 draws, deterministic).
  - `test_the_presets_are_off_by_construction`: a source scan (`checked > 60`) that nothing under `engine/season` outside the two files imports `army_presets`/`install` (source-text regex test, with a probe line proving the pattern matches) `:325-341`.
- **Conflicts / stale:** the "off by construction" test is a source-text scan guarding an UNWIRED feature: army presets exist and no season code reaches them (no AI faction raises an army in play). Source-text test of the kind F-TEST-09 criticises, but with a population floor and a control.
- **Open items:** `proposals/2026-10-29-army-phase5-design.md` M1..M10 referenced; training Sites are planted where the shipped realm seats none.

### tests/valoria/test_army_phase5.py
- **What it is:** pytest file, ED-IN-0306 phase 5: M1..M8 missed behaviours of phases 1-4 asked of the SHIPPED realm `build_realm(0)` (the realm as fixture "on purpose").
- **Status:** no Status line. Reading: live. Header explains phases 1-4 passed on hand-planted weight-12 cohorts "the realm never ships, and that is how a chain that could not field an army went unseen" `:4-6`.
- **Bears on:** MB (armies, mustering, casualties), SE (cohorts as population), FA (Crown/Church/Hafenmark), CORE (R-04 strategic acts).
- **Content that matters:**
  - The shipped realm's facts: Crown governs 15 cohorts of weight 2 (`under_arms_cap(2) < 100`: one cohort cannot field a unit; 15 cohorts = 900), the Church's `set_s_036` is defended by six individuals, `terr_T7` is Hafenmark's and empty `:7-9,79-97`. Seeded battery: `seen = [fn(inp, Random(s)) for s in range(1,9)]` requires `attacker_wins >= 5` of 8 and `min(attacker_size_pct) > 0.5` `:95-97`.
  - An army is where its commander is (hold passes to a member away from the origin -> no OOB) `:100-110`; a faction raises only the people it governs (Crown cannot recruit a Hafenmark cohort) `:113-121`; a cohort cannot be raised to its cap into two armies `:125-141`; a `move` cannot seat a person at a territory (`travel.blocked`) but `march` parks an army there (`army.arrived`) and it can march on `:145-162`; a territory field is not a walled assault (`fort_level == 0.0` at a territory, > 0 at the settlement) `:165-170`; an army is provisioned by the cohorts it drew from (`seen[0] == sum of the cohorts' weights == 30`) with `field_provisioning` swept True `:174-186`.
  - Lost army costs the cohorts at home their bodies: only the side's cohorts bleed (`hurt == side`) `:190-220`.
- **Conflicts / stale:** `proposals/2026-10-29-army-phase5-design.md` (a proposals-tree design doc) is the source of M1..M10. `field_provisioning` is a fixture that must be swept ON (default off [UNVERIFIED]).
- **Open items:** none.

### tests/valoria/test_army_verbs.py
- **What it is:** pytest file, ED-IN-0306 phase 2: the army Record (kind `army`, minted by `create_record`) and the four verbs that change it (`recruit`, `form_unit`, `assign_troops`, `order_unit`; `loop/effects_army.py`) through the real fold and gate, with the module `modules/mass_battle/armyrecord.py` tested without a world elsewhere.
- **Status:** no Status line. Reading: live.
- **Bears on:** MB, FA (faction armies, holder = commander), SE (cohort weight), CORE (gate write `(Record, subject_matter)`).
- **Content that matters:**
  - Army minted whole, one per faction, held by its maker; a second army for a faction, an unknown faction, and a malformed record (strategy `rout`) are `act.refused` `:71-84`. Recruit up to `under_arms_cap(12)`; one over is `recruit.refused` and the record unchanged `:88-100`; archers need an `archery_range` Site, levy none `:103-113`; non-cohort (weight 1), nonexistent person, and a cohort not committed to the faction are refused `:116-124`.
  - Only the holder commands and only an army is commanded; form/assign/order conserve every trooper; 10 menu refusals each leave the record as it was; missing/mistyped payload fields are refusals not crashes (including unhashable and non-string names) `:127-178,208-229`.
  - `ARMY_VERBS` (6 verbs) are WITHHELD from formation by `Fixtures withheld_verbs`: "The command is the act's payload, which no Candidate carries: a computed act could not bind it" `:181-186`. So no NPC/AI ever forms an army verb -- armies exist only by player/menu/preset install.
  - An army minted empty so the recruiting rule cannot be skipped; non-faction Proposition has no army; a holder who is gone frees the faction's slot; only a faction member may mint or command `:190-261`.
- **Conflicts / stale:** the AI-side gap (no army verb is formable) is the inverse of the standing requirement that armies be built by the engine without a GM [CORE/MB/FA]. `ARMY_VERBS` withheld count `== 6` pinned `:185`.
- **Open items:** none.

### tests/valoria/test_axis_roster_single_owner.py
- **What it is:** pytest guard (ED-IN-0230 / ED-IN-0261): the ethical-axis set has one owner (`references/descriptor_registry.yaml: axis_roster` -> `tools/export_descriptors.py` -> `engine.substrate.descriptors.AXES`); an AST sweep fails on a second axis roster.
- **Status:** no Status line. Reading: live; one of the guards CLAUDE.md §0.1 pt 5 accepts (the artifact is game code: `engine/season/decision/choose.py` sums over it).
- **Bears on:** CHAR (pursuit axes, ethical axes), CORE (single-owner registries).
- **Content that matters:**
  - `rosters.PURSUIT_AXES` set equals `descriptors.AXES`, and `len(descriptors.AXES) == 7` (ED-IN-0261, Jordan 2026-09-20: seven bipolar axes; re-pinned 4 -> 7 at IN-08) `:65-89`.
  - The `pursuit_axes` roster row must carry `from_descriptor: axis_roster` and no `values:` list, plus `forbidden: [exposure]` (the Exposure three-senses collision) `:92-106`.
  - AST sweep over `engine/` and `ci_common.MODULE_CODE_DIRS`: any literal (tuple/list/set/dict half) holding 2+ canonical axis names is an offender; floors `len(walked) >= 100` and a named non-engine witness file `systems/characters/sim/conviction.py` must be walked `:109-150`.
- **Conflicts / stale:** the second reader `engine/substrate/keys.py::AXES` is retired with the Key substrate (ED-IN-0232), so the original two-literal drift is gone "by subtraction rather than by this guard" `:68-74`. Seven-axis count pinned with its citation.
- **Open items:** none.

### tests/valoria/test_balance_oracle_arms.py
- **What it is:** pytest file, plan position `28-i`: the season-side arms instrument `engine/season/harness/arms.py` (the n-seed two-arm comparison that replaced `tools/balance_oracle.py`) still constructs, and its live pair still differs.
- **Status:** no Status line. Reading: live for the instrument tests; contains one test of a RETIRED symbol (F-TEST-10).
- **Bears on:** CORE (instrument, §7 balance claims), MB/FA (`field_casualty_model`), PROCESS.
- **Content that matters:**
  - Live pair is `field_casualty_model`: `total` (pre-M4: "losing costs everything") vs `scaled_by_degree` (ruled default: `Person.body` scaled by the engine's survivor ratio, floored at 1); both read by one call site `loop/effects.py::_eff_march` on a LOST field `:28-31`. Exactly two arms, two distinct registered `FIELD_CASUALTY_MODELS` members `:60-69`.
  - THE FALSIFIER `:72-111`: a real `march` (p_npc_033 from `set_s_014` vs `set_s_036`, a 2-v-6 mismatch) folded through the real driver on `build_realm(0)`: under `total` every attacker's body is 0 or removed; under `scaled_by_degree` every attacker survives with body > 0; the two differ. Confirms `total` is a certain kill (the control arm) and the default is not.
  - `two_proportion_z` generalises the equal-n case (`abs(z_new - z_expected) < 1e-9`) and is degenerate-safe (zero acts return 0.0) `:114-130`. `_resolve_arm` accepts a string or `{fixtures, build}` halves, refuses unknown build kwargs/third halves, and an unregistered fixture name raises `Ungraded` instead of running a null arm `:149-191`.
  - `test_the_retired_pair_definitions_still_import` `:133-146` asserts `_ARMS_POOL` still imports and both setups run; and `not hasattr(oracle, '_ARMS_CONTEST_LADDER')`. Confirms F-TEST-10 (T-04: delete, symbol-level ledger note). The private/owner ladder pair was retired because it is not season-reachable (`seam/ladder.py::degree_of` never calls `systems.social_contest.sim.contest.resolver`) `:15-22`.
- **Conflicts / stale:** instrument is deliberately not a CI gate (a realm build is about a second, a season tens of seconds) `:5-14`; docstring says `_ARMS_FLOOR`/`_ARMS_BOUNDS` were deleted at `29b` with the faction layer.
- **Open items:** the full comparison is run by nothing automatically (`:9-11`); CLAUDE.md §7 says `arms.py` is not a campaign-level instrument.

### tests/valoria/test_band_extension_seam.py
- **What it is:** pytest guard (ED-SC-0032): the ladder's `BandExtension` seam in `engine/dice_engine/dice_engine.py` probed with deliberately hostile extensions.
- **Status:** no Status line. Reading: live; one of the guards CLAUDE.md §0.1 pt 5 admits (the ladder decides resolution in six subsystems; the seam executes a Jordan ruling).
- **Bears on:** DICE (the four-band ladder), SC (contest extension), CORE.
- **Content that matters:**
  - Four hostile/neutral extensions (always-veto, never-veto base, truthy non-bool, unstable-truthiness) over a domain of `(n/4, o/2)` for `n -12..60`, `o 0..12` (>800 cells): the ONLY band transition the seam can express is Overwhelming -> Success; `moved > 0` asserted for the two that fire `:87-103`.
  - A raising extension is never consulted below the top band (Failure/Partial/Success calls return) `:116-127`; an undeclared context key (`poool=20`) raises `TypeError` ("does not declare context key") and a declare-nothing extension accepts nothing `:130-145`; no extension means the unmodified ladder `:148-150`.
  - HONEST LIMIT: `test_the_seam_is_not_a_sandbox` `:155-183` shows a hostile extension can mutate `DE.DEGREE_ORDINAL` from inside `may_overwhelm` and the test documents that, restoring the table in `finally`. So the "structural" demote-only guarantee is true of an extension confined to its contract only.
- **Conflicts / stale:** imports `systems.social_contest.sim.contest.degree_extension.CONTEST_DEGREE_EXTENSION` (the same off-loop module F-TEST-08 notes is imported by nothing under `engine/season` or `modules/`) `:133`.
- **Open items:** none.

### tests/valoria/test_body_contact_toi.py
- **What it is:** pytest acceptance file (MB spatial-model v2 stage C, R1 probe): contact fires on the reach body; the collision step stops on the BODY circle; field vs grid path.
- **Status:** no Status line. Reading: live (MB field-movement path).
- **Bears on:** MB (cell bodies, contact, charge, cavalry).
- **Content that matters:**
  - Design stance: contact fires on reach-grown body; the collision step stops at BODY-vs-BODY touch (reach 0): "Bodies collide; weapons reach across the closing gap"; stopping on the reach surface parked cells at a boundary where the strict predicate is False -> a permanent zero-casualty standoff `:1-10`.
  - (a) head-on contact fires at `2*CELL_RADIUS + reach_for('infantry')` minus/plus 0.02 and not at +0.4 (reach-derived so it follows weapon-class reach) `:118-139`; (b)(c) head-on and cavalry-charge battles: bodies never interpenetrate after any committed tick (`_CommitProbe` wraps `separate_all_bodies`, tolerance `1e-6`), `probe.commits > 0`, and casualties exchanged (no stall) `:144-174`; (d) the FIELD_MOVEMENT=0 grid path never calls body code (primitives poisoned) `:179-198`; (e) troop conservation via `assert_troop_conservation(a, b)` with `checked >= 2` `:203-217`; same seed twice gives same outcome `:222-233`.
  - Seeds via `random.seed(...)` of the global generator; process-global movement toggles saved/restored in `finally`.
- **Conflicts / stale:** the test setup (a, b built with `build_unit('Line', 3, ...)`) runs two-unit toy battles, not the season-path MB seam. `(c)` asserts only `(a.hp < hp_a0) or (b.hp < hp_b0)` -- a weak "someone lost something" check.
- **Open items:** none.

### tests/valoria/test_body_no_interpenetration.py
- **What it is:** pytest file (Jordan, 2026-11-01: "troops have geometry. they cannot overlap."): no two bodies interpenetrate at battle scale, measured on the harness's own stress scenarios (>= 5,000 troops a side).
- **Status:** no Status line. Reading: live.
- **Bears on:** MB (geometry, stress battles).
- **Content that matters:**
  - Four scenarios x 2 seeds at `CAP = 40`: `S01_mirror_lines`, `S03_cannae_double_envelopment`, `S06_missile_against_foot`, `S07_season_path_mirror` from `systems/mass_battle/sim/stress_scenarios.json`; asserts `max(depth) <= 2 * 10**-round_digits`, contact reached, casualties taken, idle subunit ticks <= 25 % of live (freezing would also leave no overlap, ED-MB-0059), `battles == 8` and `ticks >= 4*battles` `:31-72`.
  - Mutation control: with `_separate_bodies` reduced to bare caps and the end-of-tick `separate_all_bodies` replaced by a no-op, the same instrument reads `worst > 10*tolerance` -- so the test above is not vacuous `:75-90`.
- **Conflicts / stale:** none; includes a season-path scenario (S07).
- **Open items:** none.

### tests/valoria/test_body_primitive.py
- **What it is:** pytest file for `modules/mass_battle/geometry.py`'s cell body: a circle of radius `CELL_RADIUS` (0.5), one lattice pitch across; `body_overlap`, `body_depth`, `reach_reaches`.
- **Status:** no Status line. Reading: live, pure geometry.
- **Bears on:** MB.
- **Content that matters:**
  - `CELL_RADIUS == 0.5`, `PITCH == 1.0` `:35-36`; overlap is strict and symmetric (400 random seeded pairs, `checked == 400`); tangent bodies do not overlap at ANY rotation (72 headings x 4 neighbours, `checked == 288`) -- "the property that replaced the unit square, which overlapped its own neighbour by 0.079 at 10 degrees and 0.207 at 45" `:61-74`; translation-invariant; reach is directional (front only, from the reaching body only); zero reach collapses to plain overlap; heading normalised with zero/near-zero/NaN guards defaulting to `(-1.0, 0.0)` ("up-field") `:128-141`.
  - Uses `math.isclose(..., abs_tol=1e-12)` for derived geometry (e.g. `0.25` depth) and `==` for symmetric comparisons.
- **Conflicts / stale:** none.
- **Open items:** none.

### tests/valoria/test_casualty_attribution.py
- **What it is:** pytest file, ED-MB-0052 / plan v2 §5 C1: every MB casualty is attributed to a source (`melee`, `volley`, `pursuit`, `freed_attacker`) and a tick, and the parts sum to the whole.
- **Status:** no Status line. Reading: live; a model test for exactness claims.
- **Bears on:** MB (casualty accounting, tracing), PROCESS.
- **Content that matters:**
  - THE GATE `:60-80`: over 20 seeds `attributed[side] == measured[side]` with `==` not `approx` ("`pytest.approx` on an exactness claim is not a weak test, it is an absent one (§0.1 #2)"), `checked >= 20` non-vacuity. Loss is attributed from the CLAMPED movement (`before - after`) not nominal damage (they differ on the killing blow) and melee/volley split is proportional to nominal share `:17-22`.
  - Every event carries source and tick (`t` int >= 1 for melee/volley, `delta > 0`) `:83-91`; a ranged-vs-melee matchup produces `volley` rows (12 seeds) `:94-111`; attribution is inert with tracing off (buffer from a closed `tracing()` block empty) `:114-129`.
  - MUTATION in suite: `attribute_hp_loss` silenced for `melee` and conservation then FAILS (`any(attributed != measured ...)`) `:132-154`.
  - Diagnostic motive: the engine kills the loser THEN breaks him, where history breaks him then kills him ("inverted causal shape"); 23 bespoke probes preceded this `:3-11`.
- **Conflicts / stale:** `from systems.mass_battle.sim.engine import build_unit, run_battle` -- sim oracle path, plus `modules.mass_battle.resolution.tracing`.
- **Open items:** the inverted-causal-shape question the instrument exists to answer is not asserted here.

### tests/valoria/test_cell_exclusion_no_deadlock.py
- **What it is:** pytest guard, ED-MB-0059 / 0061: the same-side cell-exclusion pass (`hierarchy/units.py::resolve_toi_and_commit`, `MB_CELL_EXCLUSION`) must never freeze a formation.
- **Status:** no Status line. Reading: live.
- **Bears on:** MB (movement, performance, golden modes).
- **Content that matters:**
  - Measured cost of the original bug: 1,213,199 extra body-box solves of which 568,785 (46.9 %) returned exactly 0.0 against 9.84 % on cross-side; halted cells fell 20,356 -> 3,300, `resolve_toi_and_commit` calls rose 1,482 -> 11,934 (8.05x tick inflation: every battle ran to the turn cap) `:13-19`.
  - Invariant: a rigid formation translating in free space is BIT-IDENTICAL with the pass on or off (`on == off` over cell positions rounded to 12 places) `:106-117`; anti-vacuity: the free formation actually moves between tick 1 and tick 6 `:119-130`; `MB_CELL_EXCLUSION` is pinned `'1'` in `tools/ci_golden_modes_check.py FIELD_PINS` `:132-143`.
  - POSITIVE guard added after a read-only critic showed the first two were one edit from vacuous: two same-side cells closing head-on are capped at body touch with the pass ON and co-located with it OFF (`off == approx(0.0, abs=1e-9)`, `on > off + 0.5`); an early-touch case (start gap 1.5, step 1.0: first touch s = 0.25) kills the `s <= 0.5` mutant (`on == approx(1.0, abs=1e-6)`) `:146-226`. Mutants are named in the comment.
- **Conflicts / stale:** `approx` with tight absolute tolerance on geometric touch values; defensible as float geometry.
- **Open items:** none.

### tests/valoria/test_charge_momentum_impulse.py
- **What it is:** pytest file, ED-MB-0041 Tier-2: a body ordered to HOLD must stop reading as a charger (`cell_last_speed` -> `_momentum_speed` feeds puncture, du Picq charge-shock, braced-wall recoil).
- **Status:** no Status line. Reading: live; F-TEST-11 / evidence row 15 read it (2 skips not taken).
- **Bears on:** MB (charge, cavalry, momentum), PC (analogue).
- **Content that matters:**
  - Control: a closing body records `_momentum_speed > 0`; hold zeroes it on the live node path and on the legacy grid path `:43-72`. Two `pytest.skip` branches: node path not active, legacy path recorded no motion `:54-55,67-68` (F-TEST: not taken today; the first is a real skip if `_node_pos` is absent).
  - Scope note (a design admission): "the wider momentum-at-halt question is deliberately NOT settled": a cell halted by contact keeps a frozen speed; recording 0 collapses the pike-vs-cavalry retention margin from > 0.02 to 0.0035; recording the current intended step sends gauge row C1 (cavalry vs steady unbraced line) from 48.3 % to 85.0 % against a 35-55 band; "the engine has no charge/recoil/re-charge cycle", recorded as a Tier-3 design call `:9-17`.
- **Conflicts / stale:** none; F-TEST's evidence row says the file ran with `test_mass_battle_maneuvers.py` (6 passed, 1 xfailed).
- **Open items:** Tier-3 design call: a charge/recoil/re-charge cycle does not exist in the MB engine (the cavalry-charge question the brief's weapon-carry/cell-based approach section touches).

### tests/valoria/test_claim_provenance_fields.py
- **What it is:** pytest guard (ED-IN-0122, ED-IN-0194) for `tools/ci_claim_provenance_check.py`: the gate must read every field a claim or its instrument can live in, and must not accept an invented path under a forked directory.
- **Status:** no Status line. Reading: live; process-only (a gate guarding a gate); CLAUDE.md §8 cites its `test_a_fabricated_path_under_a_forked_directory_still_violates` as the falsifier.
- **Bears on:** PROCESS.
- **Content that matters:**
  - Reads the gate's scanned field tuple FROM SOURCE (string slicing of `ci_claim_provenance_check.py` after `blob = `, `for k in (`) rather than re-declaring it `:43-53`; requires `description`, `provenance`, `measured_by` `:40`.
  - Two planted fixtures (claim in `measured_by` with no marker must register; instrument in `measured_by` satisfies the gate and exists on disk) `:66-89`; `cpc.check() == 0` (live ledgers pass) `:92-102`.
  - FALSIFIER for the prefix-swallow: four fabricated paths under forked directories (`tools/observability/never_existed.py` etc.) must NOT resolve through `_resolves_through_restructure_ledger`; three real retired instruments recorded by exact row must `:105-145`. The ledger carries "162 directory-prefix FORK: rows" `:111`.
- **Conflicts / stale:** `pytest.importorskip('ci_claim_provenance_check')` at import `:34` -- an absent module would skip the whole file silently (a skip hazard of the F-TEST-11 kind, for a process gate). Source-slicing of another file's text is brittle to a reformat of `for k in (`.
- **Open items:** none. Subject is process-only (CLAUDE.md §0.1 pt 5: a guard whose subject is a gate); retained by CLAUDE.md §8.

### tests/valoria/test_close_ranks.py
- **What it is:** pytest file, ED-MB-0028: `Subunit.close_ranks()` (Jordan directive 2026-07-23): as cells lose troops, unengaged troops from other cells fill them to keep engaged cells at prescribed density.
- **Status:** no Status line. Reading: live.
- **Bears on:** MB (cells, density, depth vs frontage).
- **Content that matters:**
  - `HU.MB_CLOSE_RANKS is True` by default: "Jordan ruled 2026-07-29 that every built mechanic defaults ON (ED-MB-0061)... a test asserting a flag defaults OFF protects the oracle, not the engine" `:45-49` (the function is still named `test_default_gated_off`).
  - Inert when forced off (snapshot equal); conservation `abs(before-after) < 1e-6`; front rank refilled to 100 (`pytest.approx(100.0)`) from the rear; depth spent before frontage (3 live cells front, rear thins); a 1-deep line cannot sustain (front average `approx(50.0)`); full depletion does not divide by zero `:52-119`.
- **Conflicts / stale:** `test_default_gated_off` name contradicts its assertion (stale name); `pytest.approx` here is on float troop counts where the arithmetic is a redistribution (exactness arguably expected; `abs <1e-6` on conservation).
- **Open items:** none.

### tests/valoria/test_coherence_elastic_plastic.py
- **What it is:** pytest file, position 27 (WR-SCOPE): threadwork Coherence as a distance held as two quantities, elastic then plastic (`systems/threadwork/sim/coherence.py`), plus Mending Stability scale term (ED-WR-0008) and Mending's restorative feedback (C-1, §6.8) and own-configuration Mending (WR-02).
- **Status:** no Status line. Reading: live as the oracle of an off-loop subsystem (threadwork sim is an island; F-TEST section 4).
- **Bears on:** WR (Thread Sensitivity, Coherence/drift, Mending), CHAR.
- **Content that matters:**
  - Model: elastic range `ELASTIC_RANGE` (6 per `:77`), permanent set `resting_point = stack - range`; stretch stacks across events; recovery is elastic only and never reaches the resting point; elastic range constant after set (no work hardening/brittleness, E-3); environment gates recovery; crossing past `HUMAN_BAND_LIMIT` is reported once and irreversible (`mend_resting_point` then raises "manipulation") `:55-188`. Each ruling has a test that fails under the rival reading (docstring list) `:7-14`.
  - "The magnitudes in coherence.py are invented (its own header says so); what is NOT invented is the set of orderings §7.1 fixes" `:15-17` (cites `canon/philosophy/07_drift.md` §7.1, §7.4, RULINGS.md Batch 8 E-1..E-4, Batch 9 C-1, C-2).
  - Mending: `COHERENCE_COST_BY_SCALE` keyed; Partial = the scale's cost, Failure = Partial - 1; Success/Overwhelming 0; Relational reproduces the retired -1/-2; binding ops (locking) keep flat -1 `:246-271`. Mending calls `recover()` with `mending = -COHERENCE_COST_BY_SCALE[scale]`, `seasons = 0`, term > 0 at every scale x degree except Failure (no call) `:305-324`; gated by the mender's environment (default False) `:326-339`; unpriced scale falls back to Relational for Ob and term alike `:354-358`.
  - WR-02: own-configuration Mending (`configuration_of` = `"self"` or own id) moves the RESTING POINT by `RESTING_POINT_MEND_BY_DEGREE` (Overwhelming/Success > 0; Partial/Failure 0) with no elastic term and no stress; another's aim keeps the elastic path; past the crossing it is refused with a note `"not mended ... human band"` not raised `:383-461`.
  - Rolled tests assert both branches executed (`took >= 1 and failed >= 1`; `moved >= 1 and still >= 1`) over 300 seeds `:361-380,464-477`.
- **Conflicts / stale:** `_ms_by_degree` writes to a module-level fallback store `coh.reset_all()` first `:238`. Coherence vocabulary vs v40 characters [UNVERIFIED]. Sim is off-loop (no loop caller; F-TEST evidence row 16).
- **Open items:** none.

### tests/valoria/test_combat_armour_reference.py
- **What it is:** pytest drift gate (ED-PC-0040): `tests/valoria/data/combat_armour_reference.json` records the full weapon roster across four armour tiers (deterministic seeds); the test recomputes and fails on any cell moved beyond `TOLERANCE = 0.15`.
- **Status:** no Status line. Reading: live; a golden for PC balance, marked `@pytest.mark.slow` on the drift test.
- **Bears on:** PC (armour tiers: none/light/medium/heavy; weapon roster), PROCESS.
- **Content that matters:**
  - Motivation: ED-PC-0038 aimed at plate and moved MAIL (odachi -23pp, naginata -25pp, staff -12pp); ED-PC-0039 moved odachi a further -18pp; neither caught by a test `:3-8`. The gate "is not a balance freeze"; regeneration via `python workbench/armour_participation.py --update` makes the diff the disclosure `:12-21`. Tolerance 0.15 "absorbing legitimate small shifts in the RNG trajectory from unrelated changes, not sampling noise" `:30-34`.
  - Missing reference file or a roster change without regeneration is `pytest.fail`, not skip `:46-56`; coverage test requires every `WEAPONS` key, `ref['n'] >= 40`, all four tiers `:72-89`.
- **Conflicts / stale:** a tolerance of 15 percentage points is wide; the reference is regenerated by hand (the very failure the file warns of). Workbench lives at `systems/combat/combat_engine_v1/workbench/` (path in `_instrument`).
- **Open items:** none.

### tests/valoria/test_combat_audit_pins.py
- **What it is:** pytest regression pins for defects found by the 2026-07-24 four-dimension read-only combat audit (EDs ED-PC-0034, 0035, 0036, 0037): state-carryover, a negative overcommit exposure, grab hazard sign flip, dead morphology levers, cut/thrust label vs arm paid.
- **Status:** no Status line. Reading: live; each pin names a bug that SHIPPED and was found by an auditor.
- **Bears on:** PC (personal combat engine `modules/combat`: represent gate, select_mode, coupling, morphology levers).
- **Content that matters:**
  - `represent_measure_p` must be a pure function of (weapon, opponent armour, opening gap, stats): corrupting every circumstance field the wrapper writes (`sel_head`, `grip_position`, ...) leaves it equal for 12 weapons x 2 armours; the first version used `pytest.approx(abs=1e-12)` and was tightened to `==` after byte-equal verification across 26 cells `:37-60` (a worked instance of CLAUDE.md §0.1 pt 2). Measured pre-fix path dependence: katana 0.000 -> 0.274, hook_sword 0.000 -> 0.425 `:41-45`.
  - Guisarme presents its POINT at the realistic opening room (range_utilization ~0.48) and `represent_measure_p > 0.5` `:63-79`; `overcommit_exposure >= 0.0` over 6 traditions x 5 commits x agi 2-5 x str 2/4/6 (measured -0.37 before) `:82-94`; `grab_sigma` monotone non-decreasing in skill then FLAT (`vals[5:] == [vals[4]]*3`, `==` not approx) `:97-112`.
  - Each of five morphology levers (`LEGIB_EDGELINE_K`, `BIND_SPINE_K`, `GRAB_EDGE_K`, `CHOKE_ACCURACY_K`, `FACING_REGIME_K`) is individually live at the MECHANISM level: zeroing the constant changes the quantity it feeds (`on_v != approx(off_v, abs=1e-12)`); the union metric had passed while 4 of 5 were dead (BIND_SPINE_K alone 0.5 %, CHOKE 0 %, FACING 0-0.5 %, GRAB 2-2.5 %) `:115-152`.
  - cut_thrust: label (`select_mode` damage mode) equals the arm `core.cut_thrust_arm` actually pays, parametrised over `_versatile_cells()` (cells selecting the versatile head; the old runtime `skip` removed), floor `checked >= 51` of 72 cells (re-measured after `partisan` deleted, ED-PC-0058) `:155-216`; modes across the roster are exactly `{'shear','puncture'}` and at least one weapon changes arm with armour tier (spetum, naginata, tsurugi, changdao, jian, szabla) `:219-242`; `coupling('cut_thrust', ..., eff)` respects weapon quality, each arm reads its own magnitude (keen edge != keen point) `:245-258`.
- **Conflicts / stale:** `audit/2026-07-24-combat-four-dimension-audit/` is an archived path. Floor `51` and weapon-name lists are count/name pins that move with the roster.
- **Open items:** none.

### tests/valoria/test_combat_cut_grading.py
- **What it is:** pytest file, A7a channel 1 (M6, ED-PC-0051): native edge quality (`curved_cut`, `straight_cut` heads; 16 weapons, 31 % of the roster) must be consumed by `core.coupling`.
- **Status:** no Status line. Reading: live.
- **Bears on:** PC (weapon edge quality, armour material gating, civilian-carry balance).
- **Content that matters:**
  - Defect: only the bare `'cut'` token was scaled by edge quality; native cut-eff population 0.710 (hook_sword) to 1.330 (shamshir) sits entirely above `CUT_AUTH_REF = 0.70`, so `min(1.0, eff/CUT_AUTH_REF)` is identically 1.000 -- the defect register's own proposed fix was provably a NO-OP `:1-18`.
  - Measured consequence against the civilian sidearm field ("settlement-legal 1H non-blunt roster, per Jordan's carry ruling of 2026-07-29"): shamshir 41.5 %, pulwar 35.5 % (last), sabre 38.2 %, scimitar 47.9 % against rapier 80.6 % -- the keenest edges were among the worst performers `:14-18`.
  - Jordan constraints (2026-07-29): "cutters need to be excellent in contexts where they can CUT ie unarmoured and light armour"; "the curve extends the amount of cutting edge" (already derived: `geometry.cut_factor = edge_keenness * (1 + 0.45*tanh(2*curvature))`) `:20-26`. Four guards: premise pin (`len(effs) >= 15`, `min(effs) > CUT_AUTH_REF`), native edge changes coupling, monotone across the real population (`checked >= 10`), keen-edge advantage shrinks none > light > medium > heavy with the plate bound derived from `core._shear_yield('plate')` x 1.5 slack (a first draft's invented `< 1.02` threshold was recorded as wrong), a poor edge is poor everywhere (material-ungated penalty), and the bare `cut` token untouched `:65-163`. Mutations named in the docstring.
  - Scope: channels (2) curved blade recovers faster and (3) curved thrust also cuts are specified and NOT built; `thrust_factor` for shamshir reads 0.03 "correctly collapse toward 0" `:34-40`.
- **Conflicts / stale:** the civilian-carry ruling (2026-07-29) bears on the brief's weapon-carry trade-off [MB/PC/SE]; consumed here only as the balance context.
- **Open items:** channels (2) and (3).

### tests/valoria/test_combat_duel_terms.py
- **What it is:** pytest file, PC-10a (RS-25): duel TERMS on `wrapper.fight` -- `yield`, `blood`, `death` (default) -- so "a duel need not be lethal" (Jordan, 2026-10-14).
- **Status:** no Status line. Reading: live; strong, with a kept-executable mutation control. Bears directly on F-PC-04 (lethality) as the non-lethal route.
- **Bears on:** PC (duels, surrender, lethality terms), CORE (`seam/wrappers/combat.surrender_of`; `PersonalCombatInput.terms`), SC.
- **Content that matters:**
  - Falsifiers: (1) under default `death` the fight is byte-identical to a no-`terms` call: trace, result and every engine-level draw (`RecordingRandom`) equal over 3 pairs x 40 seeds, `checked == 120` `:77-86`; (2) a seeded `blood` fight stops at the first wound with exactly one accepted `yield` by the first-wounded fighter, in that turn, with no felling, no `UPSET_FLOOR` draw after, `combat_degree` reading `'Wounded'`, `surrender_of(trace) == dict(by=..., turn=..., accepted=True)`; cases are FOUND rather than assumed (`len(cases) >= 6`), both sides yield somewhere in the sample `:99-153`; (3) `yield` stops at `YIELD_HEALTH_FRAC` of Health, `checked >= 20`; `yield` stops in a later turn than `blood` on some seed (`later >= 1`) `:198-241`; (4) `death` leaves Felled reachable (`felled >= 10` of 20 seeds, band `'Felled'`) `:246-260`.
  - (5) kept as an executable control: with `_terms_met` forced False, the same assertions raise on every case (`red == len(cases)`) `:155-165`. The module entry `modules.combat.fight.fight` reads `inp.terms` from a typed-input subclass; the field is "the season's to declare (PC-10b)" `:168-193`.
  - PC-11: both fighters cross `blood` on the same beat with equal Health left: nobody yields, fight ends UNRESOLVED (result 0, `winner=None`, one turn); unequal damage yields the worse-off one `:263-294`. Terms outside the closed set `('yield','blood','death')` raise `ValueError` by name (`'first_blood'`, `''`, `None`, `'Death'`) `:89-94`.
- **Conflicts / stale:** the default term remains `death` (lethal); F-PC-04 ("plain `fight` kills 200 of 200") is the season-loop default unless `terms` is declared; `PersonalCombatInput.terms` is not yet declared by the season in this file's reading (see PC-10b) [UNVERIFIED current].
- **Open items:** none inside the file.

### tests/valoria/test_combat_edges.py
- **What it is:** pytest file, U3 / ED-PC-0018 (+U10/ED-PC-0022, ED-PC-0023, ED-PC-0026, ED-PC-0058): the edge-count primitive `edges={sides∈{0,1,2}, false_edge_frac}` and its three readers (`edge_lines` -> legibility, `spine` -> `bind_sigma`, `grab_hazard` -> `grab_sigma`).
- **Status:** no Status line. Reading: live.
- **Bears on:** PC (blade morphology data, legibility, bind, grab).
- **Content that matters:**
  - Reader formulae (`edge_lines`: double 1.0, clipped = false frac, plain single 0, edgeless 0; `spine`: single = 1 - false; `grab_hazard`: (sides + single*false)/2 so edgeless 0, single 0.5, clipped 0.6, double 1.0); MAX over elements; `pytest.approx(0.2/0.8/0.6)` on these derived fractions `:31-55`.
  - The three constants `LEGIB_EDGELINE_K`, `BIND_SPINE_K`, `GRAB_EDGE_K` are > 0 (activated at U10); the lever is live from geometry alone (double-edged `arming` reads harder; edgeless `estoc` unaffected); shinogi amplifies a katana's spine bind `:58-95`. A known honest gap: after ED-PC-0026 re-homed the German zwerchhau ability, "no grounded edge_read amplifier" exists `:70-73`.
  - Authored-data invariants (sides==0 => keenness <= 0.1; false_edge_frac>0 => sides==1) with counted floors `checked >= 65`, `ek_fired >= 4`, `fef_fired >= 9` -- the docstring records that this loop was green on an empty roster before the floors were added (2026-07-29 vetting) `:97-138`.
  - Grounded ordering: arming/longsword edge_lines 1.0, spine 0, grab 1.0; katana/sabre/falchion spine > 0, grab in [0.5, 0.65]; estoc all zero `:141-157`.
- **Conflicts / stale:** `consolidation_v1.md` §2.1-2.3 and `edges_data_v1.md` cited (archived design docs); roster-count floors move with the weapon roster (65 after `partisan` deletion).
- **Open items:** none.

### tests/valoria/test_combat_halfsword_affordance.py
- **What it is:** pytest file, ED-PC-0014/0016: half-sword capability derived from physical facts (a `grippable` element AND `geo['halfsword']`) rather than a name whitelist; the form switch is byte-identical to the retired gate.
- **Status:** no Status line. Reading: live.
- **Bears on:** PC (weapons, half-swording against rigid armour).
- **Content that matters:**
  - The emergent affordance set is exactly `{longsword, estoc, greatsword, flamberge}` (a set pin) `:19-25`; greatsword and flamberge switch to their `*_halfsword` forms when closed against `medium`/`heavy` armour, base otherwise; every afforder has a form so the name table cannot re-acquire a gating role `:28-47`.
  - `grippable` is the gate, not geometry alone: > 5 weapons pass the geometry gate but only those with a grippable element afford it `:50-59`; `halfsword_target` equals the retired name-gated logic over every weapon x closed x 4 armours `:70-82`.
  - `test_dead_coefficient_now_consumed` `:62-67` asserts `'halfsword' in inspect.getsource(S.affords_halfsword)` and `'grippable' in src` -- a source-text-substring test (F-TEST-09 class) that can pass if the names appear anywhere in the function (incl. a comment).
- **Conflicts / stale:** the "retired gate" is reimplemented in the test as the reference (a second copy of the retired rule, by design). Source-text test with no control.
- **Open items:** none.

### tests/valoria/test_combat_heft_percussion_snapshot.py
- **What it is:** pytest golden snapshot (D12c, I8, 2026-07-03): per-weapon `core.heft_resp(grip=0)` and `weapon_physics.percussion_authority(grip=0, room=1)` against `tests/valoria/golden_heft_percussion_snapshot.json`.
- **Status:** no Status line. Reading: live; a PC golden regression (Layer-2 pin on weapon physics).
- **Bears on:** PC (weapon mass/heft/percussion model).
- **Content that matters:**
  - Fixture must cover exactly the startable weapons (`'base' not in rec`): `set(golden) == set(NAMES)` (a roster-drift guard) `:38-43`; drift at `TOL = 1e-6` abs per weapon on both quantities, reported as a `drift` dict `:46-63`.
  - Lifecycle: a deliberate re-anchor (`REC_I_REF`, `REC_S_REF`, `SWING_FLOOR`, a new mass model) is expected to move these; regenerate the fixture and record the reason; "never patch a single weapon's row to make a failure go away" `:9-14`. Cites `designs/audit/2026-07-02-scene-combat-closing-distance-redesign/plan_r1_RATIFIED.md` (dissolved path).
- **Conflicts / stale:** a hand-regenerated golden at `1e-6` over the full roster; no declared-mover discipline beyond the docstring. Tests for `heft_resp` `test_combat_heft.py`/`test_combat_capabilities.py`/`test_combat_element_parity.py` named as siblings.
- **Open items:** none.

## Cross-subsystem leads

- **R-07 knowledge/attitude coverage [CORE, FI, CHAR]:** `engine/season/tests/test_told_by_channel.py` holds an R-07 realm reader and a G1 judged-regard family (`:1964-1987`, `:1838-1939`) that `audits/01_CORE_audit_addendum_C_tests.md` §3 says does not exist ("Feeling, attitude, relationship: no test"). Several telling mechanisms ship OFF or neutral: `intent_disclosure` 0 (T7), `telling_privacy` 0 (G6), `said_slant` `newest` (G3); their live arms are tested only on `tiny_world`. A documented limit (`:2261-2284`) says the confidence-break path is not reached by the production `said` pick. FI/CHAR lanes should reconcile.
- **Armies are unreachable by AI [MB, FA, CORE]:** `test_army_verbs.py:181-186` pins that all six `ARMY_VERBS` are in `withheld_verbs`, and `test_army_menu_presets.py:325-341` pins that nothing in `engine/season` reaches `army_presets.install`. So an army exists only by player menu or preset install; the shipped realm seats no barracks/range/stable, so a preset army is levy alone (`:296-303`) and levy "never closes". MB/FA/CORE should treat armies as built-but-unplayed and the standing "no GM" requirement as open for army raising.
- **Hunger is built, shipped on, and erased in play [SE, CORE]:** `test_territorial_subsistence.py:326-343,391-451`: `body_step` ships 10 (REM-52), cohorts fall to 940 in season 0 at seed 0, but with CP-T03-08 `tend` live "37 of 37 tended, fell 0" so the fall is erased within the season; the shipped-arm test needs `revert_cp_t03_08`. SE/PC lanes: the subsistence consequence is not observable in the shipped game.
- **Strife/war readings are mostly dark on the realm [WR, FA, CORE]:** `test_strife_flows.py:817-849` asserts every person's strife flow reading is `()` after one season at seed 0; `at_war` is False "for every pair the tree can build" (`:121-123`); the `flow_stakes` stamp ships ON (CR-78) with nothing to stamp. `test_strife_instrument.py`'s link list has four UNREACHABLE links (`DA>WA, DR>IN, WN>DA, WN>FA`, `test_strife_flows.py:526-528`). `test_strife_execution.py:32-43` discloses that `victim_held` never names a victim of a real death (reads field `exists`, deaths carry `body`) so XE can never be observed on a real run.
- **Works, found, build, raze have no computed producer [SE, FA]:** `test_works_founding.py:551-554,765` says a computed `create_record` declaring a works does not exist (ED-IN-0297); `found`/`build` only form after a hand-built works. `raze` (closer) not built.
- **Two arrangements cannot dispose [SC, FA]:** `test_stress_proceedings_rehost.py:259-260`: `council_of_state` and `parliamentary_debate` dispose a `Record` and `open_case` refuses them (`case.refused`); no writer.
- **Determinism audit [PC, SC, FA, CORE]:** `test_strife_execution.py:20-21` measured a plain `fight` ran to a death at every one of 60 act ids (consistent with F-PC-04); `test_balance_oracle_arms.py:72-111` shows the `total` casualty arm is a certain kill (control arm, default is `scaled_by_degree`); `test_combat_duel_terms.py` is the non-lethal term route (`blood`, `yield`) whose `terms` field the season has yet to declare (PC-10b). In FA: `requisition`, `issue`, `open_case` execute deterministically once admitted (`test_u7_remit.py`), and `oblige` term lapse/renewal is arithmetic (`test_term_upkeep.py`). `determine` is already a draw (SC-03b).
- **Cast authoring [ARCS, CHAR]:** `test_u8_cast_fields.py` makes `knows:` (initial Claims) refused by name at load (AX-7), so provided characters' starting beliefs have no authoring route in the corpus runner; `office:`, `ought:`, `capability:` do (13+ cast overlays, NPC-088 Carin Vedel `copying: 3`).
- **MB known-reds [MB, PROCESS]:** `tests/valoria/conftest.py:34-44` holds THREE strict known-red MB tests (ED-MB-0061), more than F-TEST-10's single non-strict xfail; and the reverse guard was dropped (ED-IN-0312). `_conservation.py:49-57` records an untested real divergence class (`percell.py:179` discards the applied amount; engaged-front spill shortfall).
- **Engine/season weather ships OFF [SE, WR]:** `season_factor_draw = ()` is the shipped arm (`test_season_weather.py:736`); per-territory keying is built and tested, but no realm reading with weather on exists.
- **Off-loop oracles retained [FI, WR, SC]:** `engine/tests/test_knots_ed912.py`, `test_thread_mending_ed871.py`, `tests/valoria/test_coherence_elastic_plastic.py`, `engine/tests/test_contest_kernel.py` test code the loop never calls (F-TEST section 4, evidence row 16). The knots sim still carries `BREAK_COMPOSURE_DAMAGE = 4` ("4 Composure") though Composure is retired in the kernel (`systems/fieldwork/sim/knots.py:85`, grep-verified).

## Likely stale or superseded

- `engine/tests/test_contest_kernel.py`: docstring says "Total 303" and "151-check" against `_KERNEL_EXPECTED = 389`; the giant count-history comment `:93-107` cites dissolved paths (`designs/audit/...`, `params/contest.md`, `RATIFIED_2026-06-01.md`). Retires with SC-P2 (T-12).
- `engine/tests/test_sigma_leverage_parity.py`: 768 TN 6/8 rows and 255 pre-ruling degree rows are historical (F-TEST-08 / T-11); header cites retired oracle paths `tests/sim/v32-combat-balance/m1_dice_sigma_core.py`, `audit/2026-06-03-contest-groundup/engine.py`.
- `tests/valoria/test_balance_oracle_arms.py:133-146` `test_the_retired_pair_definitions_still_import` (F-TEST-10 / T-04); the module docstring's `tools/balance_oracle.py` references are to a retired instrument.
- `tests/valoria/test_close_ranks.py:45`: `test_default_gated_off` asserts the flag is ON (stale name).
- `engine/season/tests/test_season_weather.py` module docstring `:1-17` (says the control is the pre-change hash at build/one/two seasons; the pins have moved ~60 times and the first test runs under `revert_cr79`).
- `engine/season/tests/test_strife_credit.py:5`: "`regime_gain` is the control 0 at commit (1) and ships 0.5 at commit (2)" -- commit (2) is long landed.
- `engine/season/tests/test_term_upkeep.py:1-12`: cites `workplans/2026-09-28-the-plan-one-order-mc-v18-retired.md` (a retired plan by name); `test_works_founding.py:1-3` cites `workplans/2026-09-18-governance-settlement-behaviour-plan_part2.md` and `proposals/2026-09-17-governance-and-holdings-r2/04_MATTER_AND_WORKS.md`.
- `tests/valoria/test_combat_heft_percussion_snapshot.py`, `test_combat_audit_pins.py`, `test_combat_edges.py`: cite dissolved `designs/audit/` and `audit/2026-07-24-combat-four-dimension-audit/` paths.
- `engine/season/tests/test_stress_proceedings_rehost.py`: re-host of a `proposals/2026-09-05-proceedings-subsystem/stress/stress_proceedings.py` script; 28 of 38 cases explicitly not ported; `:94` `... or True` tautology.

## Items that could change an audit finding

- **F-TEST-02 (goldens):** `test_season_weather.py` holds the re-pin log in full (about 60 `RE-PINNED` blocks across `BASE_HASHES`, `STEP_OFF_ONE_SEASON`, `BASE_EVENTS`, `THREAD_READ_WITHHELD_EVENTS_1`), not 22; its first test and the `give`-withheld test run under `revert_cr79` (so the shipped-realm world is not read); `test_strife_flows.py:856-857` and `test_strife_credit.py` re-use the same literals (`600d8b27…`, `25660615…`); `test_strife_credit.py:41` is the one shipped-realm pin. Confirms and extends F-TEST-02 (6 files for the trajectory).
- **F-TEST-03:** `test_season_weather.py:541` records the B10-13 pin commit "none isolated per item" (confirms the `133 -> 137` exception); `test_told_by_channel.py:234-300` re-pins its SEED eight times because the realm stops minting chained told claims after any act-mix move (same trajectory fragility, separate file).
- **F-TEST-07:** `test_strife_kinds.py:126-127` is a does-not-raise test with no assertion (confirmed); no vacuous loop found in the files read here beyond `test_stress_proceedings_rehost.py:94`.
- **F-TEST-08:** `test_sigma_leverage_parity.py` confirms 768 + 255 rows, `by_ob == {1.0: 9, 2.0: 15, 3.0: 23}`, 47/208, floor `m1 >= 731`, `groundup >= 4`.
- **F-TEST-09 (source-text tests):** additional instances beyond `test_season_shape.py`: `test_combat_halfsword_affordance.py:62-67` (`inspect.getsource` substrings), `test_army_menu_presets.py:325-341` (regex scan with a probe line; has a population floor and a control), `test_claim_provenance_fields.py:43-53` (slices another file's text to read a field tuple), `test_stress_proceedings_rehost.py:94`.
- **F-TEST-10:** `test_balance_oracle_arms.py:133` confirmed. `tests/valoria/conftest.py:34-44` adds three strict KNOWN_RED MB entries that F-TEST-10 does not list (and notes `test_known_red_register.py` was dropped, ED-IN-0312).
- **F-TEST-11 / skips:** `test_charge_momentum_impulse.py:54-55,67-68` (two conditional skips); `test_claim_provenance_fields.py:34` `pytest.importorskip` of a tool; neither listed in F-TEST-11's thirteen engine-absent skips.
- **R-07 row in §3 of the addendum:** see Cross-subsystem leads (R-07 realm reader exists in `test_told_by_channel.py`).
- **R-04 (strategic and management acts) / R-05 (all verbs built out):** army verbs are withheld from the chooser (`test_army_verbs.py:181-186`); `destroy_record` is held by `withheld_verbs` (`test_u7_own.py:187-205`); `tie / knot` is a declined row (`test_u7_own.py:61`); `found`/`build`/`work` need a hand-built works (`test_works_founding.py:551-554`). These bear on the never-attempted/ refused sets.
- **R-09:** the `determine` family (`test_u7_remit.py:1180-1244`) is a model of a graded, recoverable draw (all four bands, re-hearing after Failure); `test_settle_margin*.py` and `test_band_odds.py` give the dice-level exactness; `test_total_arm_...` shows one certain-kill arm (control).
- **F-PC-04 (fight lethality):** `test_strife_execution.py:20-21` records 60/60 deaths; `test_combat_duel_terms.py` shows the `blood`/`yield` terms exist (PC-10a) but `terms` is declared by the season only via PC-10b [UNVERIFIED].
- **F-TEST-06:** `test_territorial_subsistence.py` and `test_strife_flows.py:817-849` run real-realm sweeps; nothing in the files here changes the "invariant sweep on a world with no office" finding.
