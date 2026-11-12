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
