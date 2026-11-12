# Instruction suite, lane IS-B2 — part 2: the season core (CORE), the character (CHAR), the tables v12 takes

## Status: PROPOSED (part 2 of `master/instructions/IS_B2_SC_FI_CORE_CHAR.md`; nothing here is applied; resolves nothing at runtime)

Read at, words, the item form and the baseline readings are part 1's §0. Item handles continue:
`IS-B2-CORE-nn`, `IS-B2-CHAR-nn`.

---

## 3. CORE — the season core

### 3.0 The standalone-playable test for CORE

The core is the host, not a registered module, and `audits/01_CORE_audit.md` §9 records its state in one
sentence: *"'Resolves correctly' is established. 'Plays' is not: no person has been offered a choice by
this code outside a test."* Read as a game of its own, the core is **one season loop played by one seated
person in the smallest world that needs no module**: the world `engine/season/harness/headless.py::build_world`
already builds (NPC-088's season, chosen because *"she needs no sitting, no contest and no dispensation"*,
the file's own head). It is a standalone playable game when a person seated in that world is shown what
is asked of him and what he may do each round, his pick is folded by the same DELIBERATE and RESOLVE as
everyone's, a different pick makes a different world, and the run ends on an ending the loop already
computes.

| part of the test | what it is for CORE | carrier | exists today |
|---|---|---|---|
| **entry** | first, at B11: `PYTHONHASHSEED=0 python -m engine.season.harness.scenarios season --seed S --seasons K [--person P] [--play \| --script FILE]` (`IS-B2-CORE-01`, `-02`). Shared, at B34: `harness.play_surface --seed S --person P --seasons K` (the transcript replaces the printing, not the loop) | `IS-B2-CORE-01`; `11_GO_player_surface_contract_B.md` §8 | `python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0` runs automated only |
| **scenario** | `headless.build_world(seed)` (`:51`), seeds 0 to 2, two seasons; the seated person is its first person unless `--person` names another | exists | yes |
| **verb set (the stub contract)** | `resolvable_verbs()`, as `populated.run` composes the chooser (`harness/populated.py:2062`), with the shipped `withheld_verbs` setting applying as in any run. Every module is reached unchanged by its composition row; none is entered by this world's acts (the world is built to need none), which is the stub: the loop is exercised, the modules are not | §0 | yes |
| **player-facing surface** | each round: the question (and, after B34, the list of questions, A-48), the ranked candidates with their budget, the pick; after the fold: the acting person's own Events and what they caused one hop on (`audits/01_CORE_audit.md` §9, "outcome legibility") | `decision/sheet.py::DevelopmentSheet`, `development_space` (`:116`, `:135`); `11_GO_player_surface_contract_B.md` §1 to §4 at B34 | the sheet exists; nothing presents it each round |
| **stop conditions (ending kinds)** | `world_q.endings_reached(w)` non-empty (`queries/world_q.py:2619`; the loop computes it every season and nothing reads it, `loop/driver.py:549`); the seated person dead with no continuation (`harness/play_surface.py::carry_on` returns `(None, ())`); K seasons spent | `IS-B2-CORE-02` | the readers exist; no entry stops on them |
| **never a dead end, the world moves** | a refusal names its clause and is remembered (`16_PESSIMIST_CORE_a_refusal_is_remembered.md`, B09; `01_CORE_predicates_name_their_clause.md`, B09); the count of scenes with no durable write is read (`IS-B2-CORE-03`) | B09; B02 | refusals carry `observed` reads; no null-scene reading |
| **execution artifacts** | `engine/season/tests/test_scenarios_runner.py` (`IS-B2-CORE-02`'s four tests); later `tests/valoria/test_play_surface.py::test_transcript_hash_equals_plain_run` (GO-B gate 1) | B11; B34 | `test_g2_token.py`, `test_rem30_character_sheet.py` call the sheet in tests only |
| **integrated check** | it is the loop: the same seed with `take_ranked` in the seat equals the automated run's content hash (`5405522c36b0399247f83fd9f6d29494` for `--case NPC-088 --seasons 2 --seed 0` at `4dc8a7b`, `master/CODEBASE_IMPROVEMENT_PROPOSAL.md` §1; re-read after B01's re-pin) | `IS-B2-CORE-02` | the echo control is stated in `play_surface.py:29-32` and not run by an entry |

**Order of execution for CORE** (what each batch adds to "plays"):

| step | batch | what lands | reading |
|---|---|---|---|
| 1 | B02 | the requirement readings; CI-11's `ENGINES` block; `IS-B2-CORE-03` (the null-scene reading, report-only); `IS-B2-CORE-04` row 11 | every pinned hash unchanged |
| 2 | B03 | CI-06 (one owner of the chooser's composition), CI-03, CI-04, CI-05, CI-08, CI-10 | content hash equal |
| 3 | B08 | a scene runs in its own order (A-9) | `interactions_per_scene = 1` equal |
| 4 | B09 | memory: fading as a read, refusals remembered, the reason trail | each file's |
| 5 | B10 | `IS-B2-CHAR-02` (the contest decider); `IS-B2-CORE-04` row 10 | B10's |
| 6 | **B11** | `IS-B2-CORE-01`, `IS-B2-CORE-02` (the registry, the one run loop, the `season` scenario) | **the test above reads true here** |
| 7 | B28 | scene access A and B (`IS-B2-CORE-05`) | 28A's twelve rows |
| 8 | B34 | the scene contract and the transcript | GO-B gate 1 |
| 9 | B38, B39 | scene access C; `30_WR_E`'s asserted null-scene zero; `01_CORE_case_setup_and_beats.md` (cases as scenarios) | C8, C9 |

### 3.1 Items

**Item: IS-B2-CORE-01** · NEW · advances: the standing requirement for every subsystem (one name per scenario, one run loop); H-02 (the game has no entry of its own) as far as an instrument can answer it before `J-H-01` is ruled.
- What is missing. Six proposals each create their own way to enter a scenario: `headless --world hearing` (`05_SC_playable_hearing_B.md` edit 9, B24), `harness.valley` (`07_SE_valley_scenario.md`, B12), `governance_spine play SEED 8 --world realm` (`06_FA_shortest_loop_B.md`, B21), `harness/field_scene.py` (`04_MB_playable_field_scenario.md`, B20), `harness.scene <role> --fixture <name>` with its own `FIXTURES` dict (`01_CORE_one_scene_contract.md` Edit 4, B34) and `harness.play_surface --scenario NAME` (`11_GO_player_surface_contract_B.md` §8, B34). The fourth of §0's four things (builder, verb set, seat, endings) has no owner in any of them, and each would write its own season loop, as `soak`, `interactions` and `storybar` did for the chooser (`harness/probes.py:281`, the docstring CI-06 answers).
- INSTRUCTION, in order: (1) `engine/season/harness/scenarios.py` (the file `08_FI_03` §1 creates) owns one mapping `SCENARIOS: dict[str, Scenario]`, `Scenario` a frozen dataclass of `build: Callable[[int], World]`, `verbs: Optional[frozenset]` (None is `resolvable_verbs()`), `seat: Callable[[World], str]` (the default seated person), `ending: Callable[..., Optional[str]]` (a reader; returns the ending's name or None), `role: Optional[str]` (the composition role the scenario exists to enter, for the integrated check). (2) One loop, `run(name, seed, seasons, pick=None, host=None) -> dict`: builds, composes the chooser through CI-06's one owner (`harness/probes.py::chooser(w, verbs=…)`), seats `pick` through `play_surface.dispatching_chooser` (`pick=None` is `decision/sheet.py::take_ranked`, the automated run), calls `SeasonDriver.season` exactly as `populated.run` does (`:2061-2065`, including `contest_max_depth`), re-binds a dead seat through `carry_on` between seasons, stops when `ending` returns a name, and returns the ending, the tick, the content hash and CI-11's per-role entry counts. (3) `python -m engine.season.harness.scenarios <name> --seed S --seasons K [--person P] [--play | --script FILE] [--developer]` prints, per round, `DevelopmentSheet`'s candidates and the pick, and at the end one summary line. (4) Every later entry resolves names here and keeps no second mapping: `scene.py::FIXTURES` (B34) is `SCENARIOS` plus the opening act; `play_surface --scenario` and `headless --world` call `run`; `harness.valley`, `field_scene` and `governance_spine play` keep their command lines and call `run`. A lane whose batch merges before B11 registers its row in its next batch. (5) When `J-H-01` is ruled and CI-07 lands (`B03c-boot`), builders move with the realm builder; `SCENARIOS` keeps their names. Builders written after CI-07 use its one function that places a person and assign no store directly.
- WHERE: `engine/season/harness/scenarios.py` (new); `harness/headless.py` (its `main` gains `--world`, calling `run`); tests in `engine/season/tests/test_scenarios_runner.py` (new).
- FALSIFIER and control: `test_the_runner_and_populated_run_agree` (for the realm at seed 0, one season, `run` with `pick=None` returns `populated.run`'s content hash: the loop is the shipped one); `test_every_registered_scenario_builds_and_ends_or_runs_out` (each row at seed 0, `assert checked == len(SCENARIOS)`); `test_no_second_scenario_mapping_exists` is **not** written (a guard on an instrument is forbidden, CLAUDE.md §0.1 pt 5): the rule binds the lanes that register.
- GATE: `python -m engine.season.harness.scenarios season --seed 0 --seasons 2`, twice: one hash, equal to `headless --case NPC-088 --seasons 2 --seed 0`'s on the same tree.
- Hash movers: none (harness only; the automated arm is the control). Depends on: CI-06 (PROPOSED, B03); `08_FI_03` §1 (PROPOSED, B11: it creates the file, so the edit sets intersect and the items are one batch); `dispatching_chooser`, `carry_on`, `take_ranked`, `SeasonDriver.season` (EXISTS-IN-TREE); CI-11 (PROPOSED, B02); CI-07 (HELD on `J-H-01`).
- Lane: FI lands it (IN reviews the loop). Batch: B11, first item. Why not its own batch: it shares `harness/scenarios.py` with `08_FI_03` §1, and a separate IN batch would add one close to the critical path (B11 is on it). Cost: small build; `sonnet` (`high`). Lands it: B11's `valoria-author`.
- `[ASSUMPTION: at B39 a provided case is a scenario whose builder is `corpus_run.build_at(case, seed)` and whose ending is the case's terminal beat — basis: `audits/01_CORE_audit.md` §9 ("proposal 02's `setup:` is the scenario format; reuse it"); `01_CORE_case_setup_and_beats.md` was not opened by this lane.]`

**Item: IS-B2-CORE-02** · NEW · advances: CORE standalone (the season as a game); the "golden for a played season" `audits/01_CORE_audit.md` §9 names as missing.
- INSTRUCTION, in order: (1) register `season` in `SCENARIOS`: `build=headless.build_world`, `verbs=None`, `seat` its first person in id order, `ending=season_ending`. (2) `season_ending(w, pid, seasons_left) -> Optional[str]`: `realm_ended` when `world_q.endings_reached(w)` is non-empty; `line_extinct` when `carry_on` returned no person; `time` when `seasons_left` is 0; else None. (3) `--script FILE` is a list of picks by round (indices into the sheet's candidates), so a played season is reproducible; a script of `take_ranked`'s own picks is the echo.
- WHERE: `harness/scenarios.py`; `engine/season/tests/test_scenarios_runner.py`.
- FALSIFIER and control: `test_take_ranked_reproduces_the_automated_hash` (the control: seeds 0 to 2); `test_a_scripted_deviation_moves_the_hash` (one pick changed at round 1, seed 0; if the hash does not move, the pick is not load-bearing and "plays" is false); `test_the_run_stops_on_an_ending_or_a_dead_seat_with_no_continuation` (two planted worlds: a seated person who dies with no tie, and a world whose `endings_reached` is non-empty at build); `test_a_played_season_replays_from_its_script` (same script twice, one hash).
- GATE: those four tests; the summary line at seeds 0 to 2 in B11's close.
- Hash movers: none. Depends on: `IS-B2-CORE-01`. Lane: FI lands it (IN reviews). Batch: B11. Cost: edit; `sonnet`.

**Item: IS-B2-CORE-03** · NEW (the carry text is `unified/U4_TRACEABILITY.md` G-11) · advances: A-81 (no scene is still), read from B02 instead of from B38.
- INSTRUCTION, in order: (1) B02: land `null_scenes(w, n)` as `30_WR_E_cascade_chains_and_the_census.md` instruction 1 defines it (over `corpus_run.attempts(w, n)`, `harness/corpus_run.py:817`; a durable write as `30_WR_D` §3 defines it), and a report-only row 12 in `01_CORE_tests_shipped_world_falsifiers.md`'s resolution table: the count by verb and by outcome class (executed by degree, refused, unanswered) at seeds 0 to 2, printed, not asserted, with clause C9's planted-act control (a planted act that writes nothing is counted; one that writes is not). (2) B09 to B37: each batch's close quotes the count against B02's reading (`reading @<sha>`). (3) B38 keeps the `storybar --null-scenes` flag and the asserted zero, unchanged. (4) Every scenario's summary line (`IS-B2-CORE-01`) prints the same count for its run, so a standalone scene that leaves nothing is seen where it is built (`IS-B2-SC-08` is the hearing's instance).
- WHERE: `engine/season/harness/storybar.py` (the function; C3-K7 makes this file serial, and B02 is before every other batch that edits it), `engine/season/tests/test_realm_requirements.py` (the printed row).
- FALSIFIER and control: the planted-act pair above; the reading must be above 0 at B02 (at `b07fc1c` one season at seed 0 refuses 377 acts, and A-81 names refusals as the measured gap), or the counter cannot see a null scene.
- GATE: the printed row at seeds 0 to 2 in B02's close. Hash movers: none (hash EQUAL; a reader).
- Depends on: `corpus_run.attempts` (EXISTS-IN-TREE); `30_WR_D` §3's definition (PROPOSED, B38: the definition is read from that file and written once, in the function's docstring). Lane: IN. Batch: B02, after `01_CORE_tests_shipped_world_falsifiers`. Cost: edit; `sonnet`.
- Overlap: lane IS-A may carry the same row for the nine; it is one item wherever it is listed.

**Item: IS-B2-CORE-04** · NEW (the carry text is G-4) · advances: R-07 (a feeling, attitude or relationship changes a decision) and R-08 (the share of non-top choices in play), each given the test `01_CORE_tests_shipped_world_falsifiers.md:36-37` says is missing.
- INSTRUCTION, in order: (1) B02, row 11 (R-08): `engine/season/harness/decision_spread.py` prints, over seeds 0 to 2, the share of resolved acts whose chosen candidate was not rank 1; the zero-temperature arm reads 0 and the shipped arm above 0; the line is R-08's `reading.line` (`01_CORE_requirements_reading_record.md`). (2) B10, row 10 (R-07), after `02_CHAR_scar_cap_and_regard_unit.md`: in `engine/season/tests/test_realm_requirements.py`, seeds 0 to 2: build the realm, write one person's regard toward one subject through the stance row's own writer (never by assigning the field), rank his candidates before and after; the top candidate against that subject changes in at least one of three seeds; control: the same seed with no write ranks alike.
- WHERE: `harness/decision_spread.py`; `tests/test_realm_requirements.py`.
- FALSIFIER and control: row 11's zero-temperature arm; row 10's unwritten control. Row 10 failing at all three seeds means regard does not reach a decision in the shipped realm, which is R-07's finding, reported and not tuned around.
- GATE: both rows green at their batch. Hash movers: none (tests and a printed line).
- Depends on: `test_u4_…` zero-temperature control (EXISTS-IN-TREE, as G-4 cites it); the regard unit (PROPOSED, B10). Lane: IN. Batch: B02 (row 11), B10 (row 10). Cost: edit; `sonnet`. Overlap: as `IS-B2-CORE-03`.

**Item: IS-B2-CORE-05** · POINTER with two BLOCKED parts · advances: A-63, A-64 (scene access); closes the INCOMPLETE rows on `28_CORE_scene_access_A`, `_B`, `_C` as far as order closes them.
- What order now supplies (no edit needed, only the sequence): 28A commit 3's ENCOUNTER half needs `social_contest.hearing` and the attendee shape; both exist after B24 (`HearingInput.speakers` and `bench`, settled in `05_SC_playable_hearing_B.md`'s Folded line), and B28 follows B24. 28B commit 4 needs the typed `utter` of `14_VERBS_SOCIAL2_B` §1 (B25); B28 follows B25. 28C's `dues_unmet`, the held-seat reader and the one composer are `20_NARRATIVE_B` edit 1, `20_NARRATIVE_C` and `U5c_SC_one_obstacle_form.md` §3; B38 orders them first.
- BLOCKED (CONTENT): 28A commit 8's two floors (95 %, 60 %) are seeds, not targets. Owner: B28's own reading (`harness.access SEED SEASONS` at seeds 0 to 2, before and after; the throughput baseline is `audits/16_PESSIMIST_CORE.md`'s 62 of 87, to be re-read on B28's base). The floors are written into the test only after that reading, as its measured values with a stated tolerance.
- BLOCKED (DESIGN): 28B, how an ask for audience reaches the host as a `commit` referent. Owner: B28's design pass (`opus`, with `ners`). Dormant form: appointments unbuilt; the person key ships at its control (`precedence_level` `None`), which `L1-A64` (APPLIED) no longer holds back.
- INSTRUCTION: v12 writes B28's SC and CORE members in the order `14_VERBS_SOCIAL1_B` → `_D` → `_C` → `IS-B2-SC-05` → 28A → 28B, and B28's close records the two floors as readings.
- GATE: 28A's twelve named rows (U3 §6.1 lists the tests as owed; B28's first commit writes them). Hash movers: as 28A and 28B declare. Lane: SC (B28). Cost: as the files state.

**Item: IS-B2-CORE-06** · BLOCKED (DEP-v11) · advances: hygiene (the stored `scale:` column).
- Blocking reason. `U5a_CORE_owed_edits.md` E row 3 is workplan v11's CR-07, and v11 holds it: its pre-flight ran and failed on one registry-derived seat, `off_npc_084` (`rung` None), 19 of 309 attempted acts with `Act.via.scope` missing (`workplans/valoria_master_workplan_v11_part3.md:438`). Deleting the column before that seat has a rung would move those acts.
- Owner: step 5 (CR-07's disposition); the seat's rung is content (`references/npc_registry.yaml`, the guild leader's row).
- Dormant form: B03 lands `U5a_CORE_owed_edits` §A to C, E rows 1 and 2, F and I, without E row 3. GATE when released: CR-07's own (the pre-flight reads 0 missing scopes). Lane: IN. Batch: B03 (the rest); E row 3 unscheduled.

**Item: IS-B2-CORE-07** · POINTER · advances: test strength (`U5a_tests_digest_additions.md`, coded SITE).
- INSTRUCTION: the file's sites were read from the digests and not opened (`:20`, `:141`). B02's first step for this member is to open each cited site and confirm the symbol and line before the edit; a site that does not match is dropped from the member with a line in the commit body, not repaired by guess.
- GATE: B02's (every pinned hash unchanged). Lane: IN. Batch: B02. Cost: edit; `sonnet`.

---

## 4. CHAR — the character

### 4.0 The standalone-playable test for CHAR

`audits/02_CHAR_audit.md` §9: *"entry point: none that plays"*; the decision layer is not a registered
module and should not be one. The character as a game of its own is **one life**: a person picked from
the seated cast, played season by season through the same ranked candidates an NPC would rank, with his
reasons shown, until his ambition is met, his line ends, or the seasons run out. Every other subsystem
is reached unstubbed, because the character is where they meet; what is stubbed is the contests'
inner choices, which run automated for a host that plays none of them (`PlayHost.deciders` empty).

| part of the test | what it is for CHAR | carrier | exists today |
|---|---|---|---|
| **entry** | first, at B11: `python -m engine.season.harness.scenarios life --seed S --person P --seasons K [--play \| --script FILE]` (`IS-B2-CHAR-01`). Shared, at B34: `harness.play_surface --seed S --person P --seasons K` | `IS-B2-CHAR-01`; GO-B §8; `11_GO_fidelity_and_campaign_modes.md` edit 1 | no |
| **scenario** | `populated.build_realm(seed)` (83 persons at seed 0, 33 seated); the seat is a row of `decision/sheet.py::creation_sheet` (`:88`). Seeds 0 to 2 | exists | the builder and the sheet exist |
| **verb set (the stub contract)** | the shipped set. With no decider in `PlayHost.deciders`, a fight, a field and (after B24) a hearing involving the seated person resolve automated, by the person's own decider (`IS-B2-CHAR-02`) or the module's interim policy | §0; `01_CORE_one_scene_contract.md` Edit 1 | fights automate today |
| **player-facing surface** | the creation sheet (who he is: skills, attributes, pursuits, convictions, and after B34 holdings); each round the offer with its terms (`02_CHAR_voices_and_the_room.md`, `02_CHAR_reason_trail_and_small_edits.md`); the chronicle of what he holds (`sheet.chronicle`) | B09, B10, B34 | `CreationRow`, `DevelopmentSheet`, `Chronicle` exist; no terms on the options |
| **stop conditions (ending kinds)** | **fulfilled**: an ambition of his reads met (`world_q.aim_state`, `queries/world_q.py:2986`; only a rung goal can be met today, AM-B-09, and `12_ARCS_arcs_as_staged_goals.md` adds staged goals in B10); **line extinct**: dead, and `carry_on` offers nobody; **unfinished**: K seasons pass with the ambition open (a draw); **the realm ended** (`endings_reached`). Death with a living tie is a continuation the player picks, not an end | `IS-B2-CHAR-01` | the readers exist; nothing ends a run on them |
| **never a dead end, the world moves** | the options shown can be done (`02_CHAR_offer_what_can_be_done.md`, B10: today 39 to 43 % of offered options resolve as refusals, F-CHAR-05); what he does to an NPC changes what the NPC later does (regard in the stance unit, the scar cap, the goal's lean: B10) | B10 | no |
| **execution artifacts** | `test_scenarios_runner.py` (`IS-B2-CHAR-01`'s tests); `test_contest_decider.py` (`IS-B2-CHAR-02`); B10's named tests per file | B10, B11 | `test_rem30_character_sheet.py`, `test_cr20_attributes.py` |
| **integrated check** | `take_ranked` in the seat reproduces `populated.run`'s hash; `aperture 4 0` prints *"two actors at different pools: yes"* (the skill authoring surface reaches a roll; "no" on all six rolled verbs at `b07fc1c`); `decision_spread --persons` shows the cast's pools differing | `IS-B2-CHAR-06` | no |

**Order of execution for CHAR:** B04 (skills defined once, as data: `U5a_capability_home_and_two_inputs.md` Part A, `01_CORE_capability_authoring_surface.md`, `02_CHAR_capability_definitions.md`, `02_CHAR_capability_uses_table.md`; `IS-B2-CHAR-05` reads A-98 against them) → B05 (the two inputs reach the roll, Part B) → B09 (the reason trail) → B10 (the seventeen members of U3 §1 item 11, then `IS-B2-CHAR-02`) → **B11 (`IS-B2-CHAR-01`: the test reads true, thin)** → B34 (the creation sheet shows holdings; the transcript) → B38 (regimes and the pull of one's own) → B39 (a generated cast, A-44; a house continues, A-75) → the content pass (`IS-B2-CHAR-03`), which is what makes two lives differ.

### 4.1 Items

**Item: IS-B2-CHAR-01** · NEW · advances: CHAR standalone (the `PARTIAL` of `unified/U4_TRACEABILITY.md` §3: *"No CHAR proposal carries a scenario with an end condition of its own"*); R-06.
- INSTRUCTION, in order: (1) register `life` in `SCENARIOS` (`IS-B2-CORE-01`): `build=populated.build_realm`, `verbs=None`, `seat` from `--person` (required: a `CreationRow.id`; the runner prints the creation sheet and exits when it is absent), `ending=life_ending`. (2) `life_ending(w, pid, seasons_left) -> Optional[str]`, a reader over existing Queries: `fulfilled` when any Proposition in `world_q.ambitions(w, p)` reads `aim_state(w, p, prop) == "met"`; `line_extinct` when `carry_on` returned `(None, ())`; `realm_ended` when `endings_reached(w)` is non-empty; `unfinished` when `seasons_left` is 0; else None. It stores nothing and no chooser reads it. (3) Between seasons the runner calls `carry_on(w, overrides, pid, last, pick)`; on a death with a living tie the offer is printed and the pick taken from the script or stdin (an NPC seat takes the first, the precedent `carry_on`'s docstring records as its revert). (4) The summary line names the ending, the tick, the persons the seat passed through, and which ambition was met.
- WHERE: `harness/scenarios.py`; `engine/season/tests/test_scenarios_runner.py`.
- FALSIFIER and control: `test_life_with_take_ranked_reproduces_the_realm_hash` (seed 0, one season: equal to `populated.run`); `test_a_scripted_pick_moves_the_realm_hash`; `test_a_met_ambition_ends_the_life_as_fulfilled` (planted: a person holding the rung his rung goal names; control: the same person not holding it runs on); `test_a_dead_seat_is_offered_its_ties_and_an_empty_offer_ends_the_line`. Falsified as a game if, over seeds 0 to 2 and three different seats, every run ends `unfinished`: then no life in the shipped realm can be won or lost in the seasons run, and the reading is reported with the seasons count.
- GATE: the four tests; `python -m engine.season.harness.scenarios life --seed 0 --person <a seated id> --seasons 1` twice, one hash.
- Hash movers: none. Depends on: `IS-B2-CORE-01`; `ambitions`, `aim_state`, `endings_reached`, `carry_on`, `creation_sheet` (EXISTS-IN-TREE); `12_ARCS_arcs_as_staged_goals.md` (PROPOSED, B10: widens what can read `met`).
- Lane: FI lands it with the registry (IN reviews). Batch: B11. Cost: edit; `sonnet`. Note: a realm season costs about 8 s to build and run at seed 0 and grows with the log (`master/HOLISTIC_AUDIT_part2.md` §5, *over time*); the tests use one season.

**Item: IS-B2-CHAR-02** · NEW · advances: the NPC and chooser intent (one interface for a player and an NPC inside a contest); closes the DESIGN code on `27_MB_D_the_commander_as_chooser.md` 27D-4 (*"returned to CHAR"*) and the structure of `05_SC_playable_hearing_B.md` edit 8; gives `01_CORE_one_scene_contract.md` Edit 3 the builder it names and no proposal writes.
- What is missing. Three proposals say the wrapper hands a module *"the sampled decider the host builds for that person from `decision/`"*; none creates it. `02_CHAR_choice_alignment.md` (B10) supplies the judgement it needs: a value of a closed set scored by alignment cells on the seven pursuit axes, inside the chooser's own sum.
- INSTRUCTION, in order: (1) `engine/season/decision/decider.py` (new; imports what `decision/choose.py` imports, no `World`): `make_decider(p, fx, draw, *, key, odds=None, watch=None) -> Callable[[view], choice]`. `view` is any frozen dataclass with a `legal: tuple` field (HEAR_B's `HearingTurnView`; the combat module's view with `TURN_CHOICES`). (2) For each `v` in `view.legal` the choice score is the sum `02_CHAR_choice_alignment.md` adds to `score_terms` for `(key, v)`, read through `data/verbs.py::align_choice(key, v, axis)` and the person's own axis weights, multiplied by the believed chance `odds(view, v)` where the caller hands one (the module's pure estimate: `closing_odds` for a hearing, `fight_estimate` for a fight) through the same `odds_weight` rule the chooser uses; no term is added that the chooser does not have. (3) The pick is `decision/choose.py::_sample_order` over those choice scores on the keyed stream the wrapper hands (`draw_factory(seed, tick)(person, f"{role}:{scene id}:{n}")`), so it is a draw whose odds his interior sets (the determinism sweep's D-06), never the top score. (4) `watch`, when given, is called with the per-value terms, the hook `02_CHAR_reason_trail_and_small_edits.md` Part A defines, so the reason for an NPC's move is readable afterwards. (5) A setting `npc_decider_roles` in `engine/season/data/fixtures.py` (a tuple of composition roles; control and shipped value `()`): a wrapper passes this decider as `decide=` only for a role named there and a party the host does not play; for any other role the module runs its interim policy as today. (6) `seam/wrappers/_entry.py::played_by` (scene contract Edit 2) gains the fallback in that order: the host's decider, else this one if the role is listed, else None.
- WHERE: `decision/decider.py` (new), `data/fixtures.py`, `seam/wrappers/_entry.py`; `engine/season/tests/test_contest_decider.py` (new).
- FALSIFIER and control: `test_with_no_cell_and_no_odds_every_legal_choice_is_drawn` (200 keyed draws on a three-value view: each value picked at least once; a decider that always returns one value fails); `test_opposite_temperaments_pick_differently` (one cell authored on a test key; two persons with opposite weight on that axis; the two pick distributions over 200 draws differ in the cell's direction, and with the cell removed they do not); `test_the_pick_is_a_member_of_legal`; `test_empty_npc_decider_roles_is_hash_equal` (realm seeds 0 to 2, and seed 2 for a fight, since seed 0 enters no fight in three seasons, H-01); the existing path scan over `decision/` (no `World`).
- GATE: those tests green in B10; the first role is listed in the batch that makes its module accept `decide` (B16 for the duel round, B20 for the field's commander, B24 for the hearing), each a declared mover there.
- Hash movers: none at `npc_decider_roles = ()`. Depends on: `02_CHAR_choice_alignment.md` (PROPOSED, B10); `_sample_order`, `odds_weight`, `draw_factory` (EXISTS-IN-TREE; `decision/choose.py:322`, `:165`); `01_CORE_one_scene_contract.md` Edit 2 (PROPOSED, B34: if `played_by` does not exist at B10, step 6 lands with it in B34 and steps 1 to 5 land in B10).
- What stays open, with owners: the cells per key (`approach`, `retreat_at`, `hearing_move`) are content, Jordan's (`02_CHAR_choice_alignment.md:122`); a move's cost in the person's own terms inside a hearing is HEAR_B's design pass; 27D-4's `reasons` wording is the reason trail's (B09). `[ASSUMPTION: the decider is built host-side and passed as `decide=`, not a policy inside the module — basis: `01_CORE_one_scene_contract.md`'s Reconciled line (C-U5a-03), which is later than and governs the "policy inside the module" sentence of `02_CHAR_choice_alignment.md`.]`
- Lane: IN. Batch: B10, after `02_CHAR_choice_alignment`. Cost: small build; `sonnet` (`high`), reviewed with `layer-conformance` Lens B for the `decision/` island. Lands it: B10.

**Item: IS-B2-CHAR-03** · BLOCKED (CONTENT; this is G-3) · advances: R-06 (people differ in what they can do), the opposed obstacle not being one number in the shipped realm, the commander's and the advocate's manner.
- Blocking reason. The mechanisms land at their controls and the values are authored content: the cast's `stats:` and `capabilities:` rows in `references/npc_registry.yaml`; per-verb `difficulty:` beyond `routine` in `verb_table.yaml`; the alignment cells of `02_CHAR_choice_alignment.md`; the six relation rows of `02_CHAR_relations_have_a_ground.md`; `U5a_CHAR_owed_amendments.md` §7 (signature rows) and §10 (goals); `16_PESSIMIST_CHAR_B`'s cells. Each file says the values are Jordan's or the content pass's. At `b07fc1c` every rolled social and inquiry act threw pool 2 and no two actors differed (§0).
- Owner: Jordan, or a content pass he reviews (`unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` Batch U1-C).
- INSTRUCTION for v12 (the part that is decidable): one content batch, `B10c-cast-content` (IN lane; after B10; a declared mover; before B15, B19 and B24, whose calibrations read the cast). Its members are data edits only, one commit per file above, each landing behind the loader's refusal for its family. Its close reads `python -m engine.season.harness.decision_spread --persons` (the cast's pools differ) and `aperture 4 0` (*"two actors at different pools: yes"*). Until Jordan supplies or approves the values the batch is not opened and every dependent calibration says which control it ran at.
- FALSIFIER and control: authoring a `stats:` row moves no roll (U1-C's falsifier); control: the row removed, the hash returns.
- GATE: the two readings. Hash movers: every realm pin, once, at the batch's last commit. Lane: IN. Cost: content authoring, then edit-class; `sonnet` for the data edits, the values not an agent's to invent.

**Item: IS-B2-CHAR-04** · FOR JORDAN (this is G-10) · advances: the skill authoring charge (*gained, lost, trained and opposed*, `AUDIT_BRIEF.md:158-160`).
- `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §2 (`:110`) states that a skill is never lost: no loss rule exists and adding one is a new growth rule. The charge lists *lost*. The ladder does not settle it (no ruling, no precedent in the tree for a rank falling; a wound and fatigue already act as levels against a roll, A-8, which is a temporary loss of effect, not of rank). Listed in `master/instructions/IS_FOR_JORDAN.md` as `J-IS-B2-01` with two options.
- What the suite assumes meanwhile: no loss rule (the present state); B04 lands `grows_by: [train, practice, use, fixed]` with no sibling.

**Item: IS-B2-CHAR-05** · POINTER (A-98 read against B04) · advances: the skill authoring surface (one kind).
- INSTRUCTION: A-98 (2026-11-12) collapses the kinds roster to `skill`, makes `insight` a skill whose use rows give no dice, and moves the four `moved_by_*` dispositions out of the skill table to their own roster (A-98's `[ASSUMPTION]`, listed there for Jordan). The B04 members were written with three kinds; a sweep lane is rewriting them. At B04's open, read `02_CHAR_capability_definitions.md`, `U5a_capability_home_and_two_inputs.md` Part A and `10_DICE_capability_axiom_map.md` for the `kinds:` roster: if any still lists `aptitude` or `trait`, A-98 governs and the roster lands as `[skill]`. The loader's refusal for the family is the check: a definition row naming another kind is refused at import.
- WHERE: `references/descriptor_registry.yaml: capabilities` (identifier kept), its loader. Named test (added to B04's `test_u1_capability_surface.py`): `test_a_capability_row_of_a_kind_other_than_skill_is_refused` (planted).
- GATE: `tools/export_descriptors.py --check`. Hash movers: none (B04 is hash EQUAL). Lane: IN. Batch: B04. Cost: edit; `sonnet`.

**Item: IS-B2-CHAR-06** · POINTER · advances: CHAR integrated (a person's skills and attributes reach a roll and a choice in computed play).
- INSTRUCTION: three readings, quoted at the close of B05, B10 and `B10c-cast-content`, each against the one before: (1) `aperture 4 0` POOLS ROLLED, the line *"two actors at different pools"* per rolled verb (`U5a_capability_home_and_two_inputs.md` Part B gate 4); (2) `python -m engine.season.harness.decision_spread --persons` (distinct pools across the cast); (3) `IS-B2-CORE-04` row 11's share of non-top choices. Expected: (1) stays "no" in the shipped realm at B05 and B10 (the mechanism is in, the content is not) and reads "yes" at the content batch; the batch that expects otherwise says why.
- GATE: the readings. Hash movers: none. Lane: IN. Cost: a reading; `haiku` extracts.

**Decided by the ladder, not listed for Jordan** (recorded so the numbering of gaps is whole):

| gap | taken | basis |
|---|---|---|
| G-6, a player-created person | closed: creating a character is picking a seated person on the creation sheet | step 1 (a later ruling): the 2026-09-05 scales roster says *"character creation"*; IN-47 C1 (ruled, as `11_GO_fidelity_and_campaign_modes.md:110` records it) makes it a pick; the code's own names are `creation_sheet` and `CreationRow`; A-44's generated cast (B39) widens the pick. Reversible on Jordan's word |
| the negotiation's opening verb | `covenant` (`IS-B2-SC-05`) | step 4 (the row as it stands; `14_VERBS_SOCIAL1_B` §3) |
| the default rite's `bears:` | the accuser bears fact and definition, the party justification (`IS-B2-SC-03`) | step 5, marked `[ASSUMPTION]`, a data row |

---

## 5. The tables v12 takes

### 5.1 Items, by batch (29 items: SC 10, FI 6, CORE 7, CHAR 6; no new code batch, one content batch)

| batch | lane | items joining it, in order | new handle? |
|---|---|---|---|
| B02 | IN | `IS-B2-CORE-07` (first step of `U5a_tests_digest_additions`) · `IS-B2-CORE-03` · `IS-B2-CORE-04` row 11 | no |
| B03 | IN | `IS-B2-CORE-06` (E row 3 left out) | no |
| B04 | IN | `IS-B2-CHAR-05` · `IS-B2-CHAR-04`'s assumption | no |
| B05 | IN | `IS-B2-CHAR-06` reading 1 | no |
| B10 | IN | `IS-B2-CORE-04` row 10 · `IS-B2-CHAR-02` · `IS-B2-CHAR-06` readings | no |
| `B10c-cast-content` | IN | `IS-B2-CHAR-03` | **yes**: after B10; before B15, B19, B24; a declared mover; held until the values exist |
| B11 | FI | `IS-B2-CORE-01` · `IS-B2-CORE-02` · `IS-B2-CHAR-01` · `IS-B2-FI-02` (the fold) · `IS-B2-FI-03` · `IS-B2-FI-04` · `IS-B2-FI-05` (design pass) · `IS-B2-FI-06` · `IS-B2-FI-01` (close) | no |
| B24 | SC | `IS-B2-SC-02` (first) · `IS-B2-SC-03` · `IS-B2-SC-04` · `IS-B2-SC-08` · `IS-B2-SC-09` · `IS-B2-SC-01` (close) | no |
| B25 | FI | `IS-B2-SC-07` step 1 | no |
| B27 | SC | `IS-B2-SC-07` step 2 | no |
| B28 | SC | `IS-B2-SC-05` · `IS-B2-CORE-05` · `IS-B2-SC-06` when SE names the act | no |
| after B24, named by step 5 | SC | `IS-B2-SC-10` (v11's CR-58 to CR-64, SC-02) | step 5's |

**Edges added to U3's graph** (all forward): CI-06 (B03) → `IS-B2-CORE-01` (B11); CI-11 (B02) → `IS-B2-SC-09`, `IS-B2-FI-06`, `IS-B2-CORE-01`; `02_CHAR_choice_alignment` (B10) → `IS-B2-CHAR-02` (B10) → B16, B20, B24 (each lists its role); `IS-B2-CORE-01` (B11) → B12, B20, B21, B24, B34 (each registers or reads a scenario row; B21 is in the same wave as B11 and registers after B11's merge, in handle order); `IS-B2-SC-02` → the rest of B24, B25 (`14_VERBS_SOCIAL2_C` §1), B27 (`05_SC_acquittal`); `14_VERBS_SOCIAL1_B` (B28) → `IS-B2-SC-05`; B10 → `B10c-cast-content` → B15, B19, B24. No edge points back. The critical path (U3 §2.2) gains no batch from the 28 items that join existing batches. `B10c-cast-content`, when it is opened, sits between B10 and B24 in the IN lane, beside B11 (FI), so it lengthens the path only if it closes later than B11 does.

### 5.2 Declared hash movers

| item | moves seeded results? | where the re-pin is paid |
|---|---|---|
| `IS-B2-SC-02` | yes: every world in which `open_case` executes | B24's last `Item:` commit (B24 already re-pins) |
| `IS-B2-SC-03`, `-04`, `-08` | only with `sitting_exchanges` above 0 (inside HEAR_B's declared mover) | B24 |
| `IS-B2-SC-05` | yes, where a `covenant` executes with `sitting_exchanges` above 0 | B28 |
| `IS-B2-SC-07` | none until a bench convenes on a construal | B27 |
| `IS-B2-SC-09`, `IS-B2-FI-06` | none, unless `IS-B2-SC-09` step 3 is taken (declared then) | B24 |
| `IS-B2-FI-02` | as v11 declares per position; `test_fi03_trail.py` re-recorded | B11 |
| `IS-B2-CHAR-02` | none at `npc_decider_roles = ()`; each role listed is a mover | B16, B20, B24 |
| `IS-B2-CHAR-03` | yes: every realm pin, once | `B10c-cast-content` |
| every other item | none (harness, tests, readers, a registry edit) | — |

### 5.3 File census additions (file · items · batch; serial order is item order)

| file | items | batch |
|---|---|---|
| `engine/season/harness/scenarios.py` (new) | `08_FI_03` §1 → `IS-B2-CORE-01` → `IS-B2-CORE-02` → `IS-B2-CHAR-01` → `IS-B2-FI-03`; later one registry row each from B12, B20, B21, B24 | B11, then one line per batch |
| `engine/season/harness/headless.py` | `IS-B2-CORE-01` (`--world`) → HEAR_B edit 9 → `IS-B2-SC-08` | B11 → B24 |
| `engine/season/harness/governance_spine.py` | HEAR_B edit 9 (`build_hearing`) → `IS-B2-SC-08` (`hearing_ending`) | B24 (B21 edits the same file earlier: `06_FA_shortest_loop_B`) |
| `engine/season/harness/storybar.py` | `IS-B2-CORE-03` | B02 (serial file, C3-K7; first editor) |
| `engine/season/harness/decision_spread.py`, `engine/season/tests/test_realm_requirements.py` | `IS-B2-CORE-04`, `IS-B2-CORE-03` | B02, B10 |
| `engine/season/queries/world_q.py` | `IS-B2-SC-02` (`DOCKET_CASE`, `case_file_of`) | B24 (hot file: one new constant and one function, at the end of the docket block) |
| `engine/season/loop/effects_information.py` | `IS-B2-SC-02` → HEAR_B edit 7 → `IS-B2-SC-08` step 3 → negotiation edit 5; `IS-B2-SC-05`, `IS-B2-SC-07` | B24; B25, B28 |
| `engine/season/write_matrix.yaml`, `engine/season/verb_table.yaml` (`open_case`; `covenant`) | `IS-B2-SC-02`; `IS-B2-SC-05` | B24; B28 |
| `engine/season/arrangements.yaml`, `engine/season/data/arrangements.py` | `IS-B2-SC-03` | B24 |
| `engine/season/seam/wrappers/sigma.py` | CI-03 (B03) → HEAR_B edit 6 → `IS-B2-SC-03`, `-04` → `IS-B2-SC-05` | B03 → B24 → B28 |
| `engine/season/queries/person_q.py` | `IS-B2-FI-04` (`dossier`) | B11 (hot file: one function) |
| `engine/season/harness/play_surface.py` | FI_07 §3 (`board`, a print of `dossier`) → GO-B §8 | B11 → B34 |
| `engine/season/decision/decider.py` (new), `engine/season/seam/wrappers/_entry.py`, `engine/season/data/fixtures.py` (`npc_decider_roles`) | `IS-B2-CHAR-02` | B10 (`_entry.py` in B34 if `played_by` is not yet there) |
| `engine/season/requirements.yaml` (`scales:` rows 3 and 7) | `IS-B2-FI-01`, `IS-B2-SC-01` | B11 close, B24 close (permanent surface: appended once per batch) |
| `references/npc_registry.yaml`, `verb_table.yaml` (`difficulty:`), `rosters.yaml` (cells, relation rows) | `IS-B2-CHAR-03` | `B10c-cast-content` |

### 5.4 Gaps and INCOMPLETE rows, and what each becomes

| source | row | disposition here |
|---|---|---|
| U4 §6 | G-3 content | `IS-B2-CHAR-03` (BLOCKED, CONTENT; a batch named) |
| U4 §6 | G-4 R-07, R-08 tests | `IS-B2-CORE-04` |
| U4 §6 | G-6 created person | closed by the ladder (§4.1 table) |
| U4 §6 | G-10 a skill's loss | `IS-B2-CHAR-04`; `IS_FOR_JORDAN.md` `J-IS-B2-01` |
| U4 §6 | G-11 null-scene reading | `IS-B2-CORE-03` |
| U4 §6 | G-13 construal before a court | `IS-B2-SC-07` |
| U4 §6 | G-1, G-2, G-5, G-7, G-12, G-14, G-15, G-16 | not this lane's subjects (MB, the nine, SE, WR, GO, FA): lanes IS-A, IS-B1, IS-B3 |
| U4D §3.4 | `05_SC_playable_hearing_B` (DESIGN, DEP-v11) | `IS-B2-SC-02`, `-03`, `-04`; the NPC decider's cost terms stay its design pass |
| U4D §3.4 | `05_SC_negotiation_scene` (DESIGN, DEP-v11, DEP-NOCARRIER) | `IS-B2-SC-05` (decided); `IS-B2-SC-06` (BLOCKED, owner SE) |
| U4D §3.4 | `05_SC_evidence_and_rebuttal_B`, `05_SC_acquittal`, `19_LACUNA_admission…`, `14_VERBS_SOCIAL2_C` (DEP-v11, CR-61) | `IS-B2-SC-02` for the docket key; SC-02 and the rest of CR-61 in `IS-B2-SC-10` |
| U4D §3.4 | `05_SC_arrangement_rows_that_bind`, `U5c_SC_proceedings_residue` (DEP-v11; §8 part 2 no owner) | `IS-B2-SC-10` (step 5). §8 part 2 was not opened by this lane and stays unowned (§6) |
| U4D §3.4 | `29_DICE…` item 29-5, hearing half (SITE) | supplied by order: `HearingInput` and `Speaker` exist after B24; B30 lands 29-5 (U3 §1 item 30). No item |
| U4D §3.4 | `08_FI_02`, `U5c_FI_residue`, `16_PESSIMIST_FI_C`, `16_PESSIMIST_FI_D`, `19_LACUNA_questioning…` (DEP-v11) | `IS-B2-FI-02` (the fold, with dormant forms) |
| U4D §3.4 | `08_FI_03` (DESIGN) | `IS-B2-FI-05` (narrowed; BLOCKED) |
| U4D §3.4 | `28_CORE_scene_access_A`, `_B`, `_C` | `IS-B2-CORE-05` |
| U4D §3.4 | `U5a_CORE_owed_edits` (CR-07) | `IS-B2-CORE-06` |
| U4D §3.4 | `U5a_tests_digest_additions` (SITE) | `IS-B2-CORE-07` |
| U4D §3.4 | `02_CHAR_choice_alignment`, `02_CHAR_relations_have_a_ground`, `U5a_CHAR_owed_amendments`, `16_PESSIMIST_CHAR_B` (CONTENT) | `IS-B2-CHAR-03` |
| U4D §3.4 | `27_MB_D` 27D-4 (DESIGN, *returned to CHAR*) | `IS-B2-CHAR-02` (the builder; cells remain content) |
| U4D §3.4 | `12_ARCS_arcs_as_staged_goals` (CONTENT: per-case stage rows) | case authors; not an item (the mechanism lands in B10; `IS-B2-CHAR-01` reads what it makes meetable) |
| holistic | H-01 (engines reached unevenly) | `IS-B2-SC-09`, `IS-B2-FI-06` (the question asked of each role at the batch that builds it) |
| holistic | H-02 (no entry of its own) | `IS-B2-CORE-01`, `-02`; CI-06 and CI-07 as placed by the improvement proposal |
| holistic | H-05 (`sigma.py` reaches `obstacle` by reflection) | CI-03 in B03; §1.0 step 1 |

### 5.5 Requirement and scale rows these items bear on (for v12's requirement map; states are readings a batch takes, not written here)

| row | items | the reading that would move it |
|---|---|---|
| scale *social contests / debates* | `IS-B2-SC-01`, `-09` | `social_contest.hearing` entered in computed play at two of three seeds (B24) |
| scale *investigations / detective / interactive fiction* | `IS-B2-FI-01`, `-06` | found deposits above 0 at two of three seeds; every scenario run ends by a predicate (B11) |
| scale *character creation / development / chronicling* | `IS-B2-CHAR-01`, `-03` | a life ends by an ending other than `unfinished` at some seed and seat (B11, then the content batch) |
| R-06 | `IS-B2-CHAR-02`, `-03`, `-06` | two actors at different pools; opposite temperaments pick differently |
| R-07, R-08 | `IS-B2-CORE-04` | rows 10 and 11 |
| R-09, A-81 | `IS-B2-CORE-03`, `IS-B2-SC-08` | the null-scene count falling batch by batch to B38's asserted 0 |
| R-04, R-05 | `IS-B2-CORE-01` (a scenario per scale, one loop) | each scale's scenario row enters its composition role |

## 6. What this lane did not check

- **No pytest was run and no gate of any proposal was executed.** Every test named above is to be written; none exists except where the text says EXISTS-IN-TREE.
- **Runs made:** `register --requirements`; `aperture 1 0` (one season, seed 0); the `--help` of five harness entries. No two-season or three-seed run, no `corpus_run`, no `aperture 4 0`, no `m1_acceptance --summary` (lane IS-A's). Every "expected" reading above is a statement of what the batch must read, not a measurement.
- **Read in full:** the work order, `STAGES.md`, `README.md`, `AUDIT_BRIEF.md`, `unified/DECISIONS_ANSWERED.md` (A-1 to A-98), `unified/U3_DEPENDENCY_ORDER.md` §0 to §2.3, `unified/U4_TRACEABILITY.md` §0 to §4 and §6 to §8, `unified/U4_DOCUMENT_STATUS.md` §3, `master/HOLISTIC_AUDIT.md` and parts 2 and 3 (to §8), `master/CODEBASE_IMPROVEMENT_PROPOSAL.md` §0 to §3, and the proposals `05_SC_playable_hearing_B`, `05_SC_negotiation_scene`, `08_FI_03`, `08_FI_07`, `01_CORE_one_scene_contract`, `02_CHAR_choice_alignment`. **Read at heads, named sections or by search only:** `05_SC_evidence_and_rebuttal_B`, `05_SC_acquittal`, `19_LACUNA_*`, `14_VERBS_SOCIAL1_B` (§3), `14_VERBS_SOCIAL2_C`, `U5c_FI_residue` (to §2), `08_FI_02` (head and edit 1), `11_GO_player_surface_contract_B` (§5, §8 on), the audits (§8 and §9 of the four, and SC's addendum §B4), the methodology-execute skill (its BATCHES section), `engine/season/requirements.yaml` (head and `scales:`), workplan v11 at the positions cited. **Not opened:** U3 §3 to §7 (the node table, the file census, the tests owed), U4 §5, `unified/U3_LAYER1_AMENDMENTS.md` and `work/L1_APPLIED.md` beyond U3 §1.4's table (which records every `L1` node APPLIED), `unified/U1_GLOSSARY.md` beyond its term column, `unified/MB_LEXICON.md`, the dossiers and digests, `01_CORE_case_setup_and_beats`, `11_GO_fidelity_and_campaign_modes` (cited through U4), the 28_CORE files (cited through U4D §3.4), `U5c_SC_proceedings_residue` §8, `decision/options.py::operands_for`.
- **Code opened:** `loop/effects_information.py::_eff_open_case` and `_docket_item`; `queries/world_q.py` at the docket keys and by symbol search; `decision/choose.py::make_chooser` and its outline; `harness/probes.py::chooser`; `harness/play_surface.py::carry_on`; `harness/populated.py::run`; `queries/inputs.py::PlayHost`; `verb_table.yaml` rows by loader. Line numbers are of `b07fc1c` and go stale at the first batch that edits a file (and at `B03a-prose` for all of them); symbols are given beside them.
- **Two claims rest on a neighbour's text, not on this lane's reading:** that `HearingInput`'s attendee shape is settled (HEAR_B's own Folded line) and that every `L1` node is applied (U3 §1.4).
- **Sibling lanes were writing at the same time** (`IS_A_NINE.md`, `IS_B1_PC_MB_DICE.md`, `IS_B3_FA_SE_WR_GO.md` held only their heads when read). `IS-B2-CORE-01`'s registry asks one line of each of them (valley, field, governance spine, duel); `IS-B2-CORE-03` and `-04` may be carried by IS-A under another handle. Stage 6's fold reconciles the handles.
