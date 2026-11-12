# Instruction suite IS-B3 — part 2: WR, GO, the tables v12 takes, what was decided, limits, evidence

## Status: PROPOSED (part 2 of `master/instructions/IS_B3_FA_SE_WR_GO.md`; nothing here is applied; resolves nothing at runtime, CLAUDE.md §0.05)

Read at `b07fc1c`. The item form, the marks and the seven-part test are part 1's §0 and §1. Item handles continue: `IS-B3-WR-nn`, `IS-B3-GO-nn`.

## 5. WR — the world

Three objects (part 1, §1). The clocks get S6 and S7 only. Threadwork and the realm get the whole test.

### 5.1 The test: threadwork (the Warden's season)

| # | today (T), with the command | as proposed (P) |
|---|---|---|
| S1 entry | **not met.** No `modules/threadwork/` (`ls modules` lists `combat`, `fieldwork`, `mass_battle`, `settlements`, `social_contest`). The oracle is `systems/threadwork/sim/` (seven files), which no realm run enters (`master/HOLISTIC_AUDIT.md` §2). One thread verb row exists, `thread_read` (`verb_table.yaml`) | **carried in part.** B03: `09_WR_threadwork_module.md` edit 3 (the operation tables as typed data). B35: `09_WR_B_threadwork_session_and_practitioner.md` edits 1 to 3 (the session on the input, three registered entries, the cost rule, the practitioner who cannot read himself). **owed:** the host that calls the entry and the verb rows that reach it are plan positions of workplan v11 with no carrier in the suite (`IS-B3-WR-01`) |
| S2 scenario | **not met.** | **carried**, B35: edit 4, a hand-built world (one settlement at distance 1 from the wound, three Sites, a practitioner, an apprentice, a steward, a hostile witness). **owed:** its builder's home and its row (`IS-B3-WR-02`) |
| S3 surface | **not met.** | **carried** for the season scale, B34, with the rule that no reading shows him his own Coherence (edit 3). **owed:** the played working is a suspended scene, and `11_GO_player_surface_contract_B.md` §6's table of which subsystem uses which kind of play has no threadwork row (`IS-B3-WR-03`) |
| S4 stub contract | not stated | **owed:** `IS-B3-WR-02` |
| S5 stop conditions | none | **carried**, B35 edit 4: four endings, "each reached by a drawn outcome, never by a number crossing". **owed:** kinds (`IS-B3-WR-02`) |
| S6 artifact | the oracle's four test files (named in the proposal's gate; not run, pytest is a close step) | **carried**, B35: those four on unchanged numbers at `prior_ops = 0, fatigue = 0`, plus the planted calls. **owed:** the host's (`IS-B3-WR-01`) and the unknowable man's (`IS-B3-WR-04`) |
| S7 integrated | `(Person, coherence)` is a write-matrix row marked `unproduced` (`write_matrix.yaml`, "only an act may write it and the verb table carries none that does"), guarded so that only a seam Event may write it (`state/world.py:1305`) | **owed:** `IS-B3-WR-01`; the reading is CI-11's `threadwork.work` count above 0 and a `coherence.changed` Event in a realm run |

### 5.2 The test: the realm as the world's own scenario

| # | today (T), with the command | as proposed (P) |
|---|---|---|
| S1 entry | **partly met.** `python -m engine.season.harness.strife 2 0 --strands` runs the realm for two seasons and prints `3 strands, 1 era(s)`, the era `OPEN` with 38 moves (26 s; P-6). Nobody is seated | **carried**, B34: `harness.play_surface --seed S --person P --seasons K` on the realm |
| S2 scenario | `populated.build_realm(seed)`, 83 persons | **carried**, B39: generated worlds (`21_PROCEDURAL_A` to `_E`); the lean year (`23_STORY_E`) as the small world in which an era ends |
| S3 surface | nothing presents a strand, an era or an ending to a person (`audits/09_WR_audit.md` §9.2) | **carried**, B38: `30_GO_F_the_plot_as_the_player_is_shown_it.md` (marker, stories, portents, recap) |
| S4 stub contract | the realm stubs nothing | n/a; the row's `unreached` set is empty, and CI-11's block says which roles a given seed in fact enters |
| S5 stop conditions | `world_q.endings_reached` returns `[]` in every run the WR audit made; the victory row is unreachable on one territory (F-WR-06) | **carried**: B12, `09_WR_world_motion.md` edit 3 (victory counts settled territories); B38, `09_WR_B_weather_with_memory_and_the_year.md` edit 4 (the `site_band` selector: the Rupture, reached by a keyed draw); the death of the line (built). An era's turn (`30_WR_A`) is a marker, not an ending. **owed:** kinds, in `IS-B3-GO-02` |
| S6 artifact | `test_in27_endings.py` (named by the proposals; not run) | **carried**: B36 and B38, the story count with its entrenched and null-scene arms |
| S7 integrated | it is the loop | — |

### 5.3 The clocks (S6, S7 only)

Carried whole by B12: `09_WR_world_motion.md` edits 1 to 3, `09_WR_B_draws_not_thresholds.md` edits 1 to 3, `16_PESSIMIST_GAME_the_world_draws.md`, `16_PESSIMIST_WR_B_the_calamity_strains_and_breaks.md`, `09_WR_B_weather_with_memory_and_the_year.md` (year and spell). Gate: controls equal, each flip its own declared mover (U3 §1 item 13); `python -m engine.season.harness.strife 3 0 1 2 --strands`. No item is added. The valley is where a clock's draw is felt by a seat (`IS-B3-SE-01`).

### 5.4 The batch sequence

B03 (`09_WR_threadwork_module` edit 3) → B05 → B09 → B11 (the scenario registry) → **B12** (the clocks; the wound) → B32 → B34 → **B35** (threadwork: `IS-B3-WR-01` to `-05`) → B36 (story instruments) → **B38** (eras, regimes, strands, momentum, the plot as shown) → B39 (generation, the lean year).

**Threadwork "plays alone" at the close of B35, and only if step 5 carries the thread card of workplan v11 into it** (`IS-B3-WR-01`). Without that card B35 lands a module nothing calls and a scenario nobody can play, as `09_WR_B_threadwork_session_and_practitioner.md` itself says ("the case cannot be played; it is written so the landing has a target").

### 5.5 Items

**Item: IS-B3-WR-01** — the one working host, and the one writer of `Person.coherence`.

- **Advances.** WR standalone (S1, S7); R-05 (the thread verbs execute), R-09 (a working is drawn).
- **INSTRUCTION.** Four suite files wait on a writer of `Person.coherence` with "no carrier in the suite" (`14_VERBS_PHYSICAL_D_thread_read` stage 2, `U5d_WR_zero_coherence_unknowable`, `12_ARCS_substrate_as_ground` item 3, `09_WR_B_threadwork_session_and_practitioner` edit 4). The carrier is designed at its plan home: `proposals/2026-10-23-subsystem-completion/2026-10-23-subsystem-completion-07-threadwork.md`, CP-T07-02 (`engine/season/seam/wrappers/threadwork.py`, the one host every thread row dispatches through; one seam Event `coherence.changed`; one prize row in `rosters.yaml: contest_subsystems.prizes`), within the card B10-15 of `workplans/valoria_master_workplan_v11_part3.md` (order: CR-13, then CP-T07-02, -03, -05, -09, -04, -06, -07, -10, -08, -11, IN-32). **B35 takes that card's positions as its build items, at their home's text and in the card's order, after `09_WR_B_threadwork_session_and_practitioner.md` edits 1 and 2, with these changes, each ordered by a ruling or by a suite decision:**
  1. *The host builds the suite's input.* It calls `threadwork.work` with `WorkingInput` as edit 1 has it: `prior_ops`, `fatigue`, and `draws`, a tuple the host pre-draws through the one draw owner under keys that include `prior_ops` (A-30). The module holds no draw handle and no store (edit 2's move deletes the oracle's module stores).
  2. *One sampler.* The Leap and the operation are drawn on the one sampler (A-5), their pools by the one pool rule from the `thread` use site of `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §3 (a skill score plus the base, attributes as levels; A-6, A-7). CP-T07-01's "`spirit` is the oracle default 4 for everyone" is replaced by that site's rows.
  3. *The crossing is a draw* (CP-T07-08): as `09_WR_B_threadwork_session_and_practitioner.md` edit 2's last paragraph states it, with the odds from how far past the band the displacement stands.
  4. *One writer.* `12_ARCS_substrate_as_ground.md` item 3 gives its operation row's lower bands a write of `(Person, coherence)` from a task row. `state/world.py:1305` refuses that write from any driver but `Seam`, and CP-T07-02's own falsifier greps for a second assignment. **Decided:** the operation on the Thread ground is one more thread row dispatched through the host; its cost to the operator is the host's `coherence.changed`, and ARCS-03 item 3 adds no write of its own.
  5. *The control arm* stays CP-T07's: `ts_seed: none`, under which no thread candidate forms and the hash equals the base.
- **WHERE.** `engine/season/seam/wrappers/threadwork.py` (new), `engine/season/rosters.yaml` (`contest_subsystems.prizes`, `thread_scales`, `tenure_kinds`), `engine/season/verb_table.yaml` (`weave`, `lock`, `mend`, `ward`; `thread_read`), `references/module_contracts.yaml` (edit 2's rows), `loop/driver.py` (`require_entries` gains the wrapper's `STEP_CALLS`), `engine/season/tests/test_threadwork_loop.py` (new; the card's test home).
- **FALSIFIER and control.** CP-T07-02's own: a planted practitioner's `weave` at a seed writes exactly one `coherence.changed` whose deltas equal the module's `WorkingOutcome.coherence_delta` plus the Leap's for the same draws; a Leap Failure writes the Leap's charge and no target change; mutation: skip the Leap, and the Leap-Failure test reds. Added: over `engine/season/loop`, `engine/season/seam` and `modules/threadwork`, one site writes `(Person, coherence)`, the host's (the card's test greps for a second). Control: `ts_seed: none` gives the base hash.
- **GATE.** `python -m pytest engine/season/tests/test_threadwork_loop.py -q`; `python -m engine.season.harness.aperture 1 0`: a thread row offered and executed, and CI-11's block reads `threadwork.work` above 0. The plan home reads four of the 46 cast rows at or above the Thread Sensitivity gate (CP-T07-01; not re-counted here), so the count is expected to be small and is reported, not asserted.
- **Hash movers.** Every executed thread row, by outcome; one re-pin at B35's last item.
- **Depends on.** `09_WR_threadwork_module.md` edit 3 (PROPOSED, B03); `09_WR_B_threadwork_session_and_practitioner.md` edits 1 and 2 (PROPOSED, B35); B05, B06 (the sampler, the keyed draw); the positions of card B10-15 (plan positions: `STAGES.md` step 5 gives each its disposition. This lane's reading is that CP-T07-02, -03, -04, -06, -08, -10 and -11 are needed for the test and CP-T07-05, -07, -09 for it to be legible; CR-13, IN-32 and JQ-2's question about a stored attribute were not opened).
- **Lane · batch · cost · tier · lands it.** WR · B35, first build item · small build per position, design-first for -03 and -08 as their home says · `sonnet` producer, `opus` critic on -03 and -08 · the B35 session.

**Item: IS-B3-WR-02** — the Warden's season and the realm are rows of the scenario registry.

- **Advances.** WR standalone (S2, S4, S5).
- **INSTRUCTION.** `09_WR_B_threadwork_session_and_practitioner.md` edit 4 places the case as "one overlay case" in `harness/exercises.py`. At this SHA that file holds overlay readers over the corpus cases (`need_sha`, `load`, `unbound`, `coverage`, `resolve`) and no world builder. (1) The world's builder is `scenarios.warden_world(seed)` in `engine/season/harness/scenarios.py`, built from the same constructors `scarce.governed` uses, with the wound from `09_WR_world_motion.md` edit 1's switch. The exercises overlay names the scenario; it builds nothing. (2) Register `warden` (`IS-B2-CORE-01`): `build = scenarios.warden_world`, `verbs = None`, `seat` the practitioner, `role = "threadwork.work"`, `ending = scenarios.warden_ending`, which returns the four names of edit 4's table, each read as a Query over the log and Tenures, with their `kinds` (`IS-B3-GO-01`): `restored` (the Site restored and holding two seasons), `won`; `breached` (the breach Event), `lost`; `closed` (the Site's last use closed), `lost`; `detained` (a live `detain` on him), `lost`; `time` (twelve seasons with none), `drawn`. (3) `unreached`, declared from the per-role entry counts `run` returns at seeds 0, 1, 2 over eight seasons, as in `IS-B3-FA-01`; expected: the `mass_battle.*` roles. (3a) Register `realm`, the world's own scenario (§5.2): `build = populated.build_realm`, `verbs = None`, `seat` the caller's `--person`, `ending` the reader `IS-B2-CORE-02` writes for the season (`realm_ended`, `line_extinct`, `time`), with the kinds `IS-B3-GO-02` gives it, and an empty `unreached`. (4) The A-80 reading, on a practitioner who rests every season (the held position is a ward or a lock that stands): `storybar --world warden --arms off entrenched --null-scenes`. The world's own wear is not a `contests:` row and is not pinned by the arm, so the Site keeps moving; expected, C8's measure.
- **WHERE.** `engine/season/harness/scenarios.py`, `engine/season/tests/test_scenarios.py`.
- **FALSIFIER and control.** An ending reached with every draw pinned to Success (`--pin-rolls Success`, `23_STORY_D`) at every seed is an ending the build decides, not the draws. Control: the unwatched run twice at one seed, one hash.
- **GATE.** `python -m engine.season.harness.play_surface --scenario warden --seed 0 --seasons 8` prints at least one occasioned thread row in the first season and an `ENDING` line or the season count; `test_each_warden_ending_kind_is_reached_by_a_planted_run`.
- **Hash movers.** None.
- **Depends on.** `IS-B3-WR-01`; `IS-B2-CORE-01`, `IS-B2-CORE-02` and `IS-B3-GO-01` (B11); `IS-B3-GO-02` (B34); `09_WR_world_motion.md` edit 1 (B12).
- **Lane · batch · cost · tier · lands it.** WR · B35, after `IS-B3-WR-01` · small build · `sonnet` · the B35 session.

**Item: IS-B3-WR-03** — a played working is a suspended scene with one choice: go on, or stop.

- **Advances.** WR standalone (S3); the one scene contract.
- **INSTRUCTION.** Edit 4 gives the practitioner a choice inside a working ("continue … or stop") and its NERS line says it pauses "where a played fight does". `01_CORE_one_scene_contract.md` edit 3 states what a playable module entry owes, and `11_GO_player_surface_contract_B.md` §6 rules 1 to 5 govern it. (1) `modules/threadwork/working.py` exports `WORKING_CHOICES = ("continue", "stop")` and a frozen `WorkingTurnView(operation, prior_ops, ops_left, last_degree, last_wrote, contact_lost)`. It carries no Coherence, resting point or displacement (edit 3: he cannot read himself). `[ASSUMPTION: `fatigue` is not on the view either — basis: edit 4 lists his headroom as "never shown to him" and names what he learns as each working's degree and what it wrote; the Thread lane may add it as his own state.]` (2) The wrapper, not the module, resolves the decider (`played_by(host, "threadwork.work", parties)`, `01_CORE_one_scene_contract.md` edit 2) and folds the entry again with `prior_ops + 1` and the returned `fatigue` while the decider answers `continue`, the outcome is not `contact_lost`, and the entry does not refuse with `window_closed`. (3) With no decider the session has length one, which is the season's fold as edit 1 defines it, so an automated working is today's arithmetic and the echo control is exact. (4) The outcome's `trace` is one step per operation (operation, degree, what it wrote, whether contact held). (5) `tools/export_engine_params.py` writes `WORKING_CHOICES` with a `name` and a line of `text` each (`11_GO_fidelity_and_campaign_modes.md` edit 3). (6) GO's §6 table gains the row: threadwork · both · season: `Offer`; inside a working: `WorkingTurnView` + `WORKING_CHOICES` · the working's `trace`; `account` after.
- **WHERE.** `modules/threadwork/working.py`, `engine/season/seam/wrappers/threadwork.py`, `tools/export_engine_params.py`, `engine/season/tests/test_scene_contract.py`.
- **FALSIFIER and control.** `test_scene_contract.py::test_a_deviating_decider_moves_a_played_module` gains its threadwork case (a decider answering `continue` once changes the outcome); `test_echo_decider_equals_no_decider` gains it (a decider answering `stop` at once equals no decider). `test_the_working_view_carries_no_coherence` (a field-name scan of the dataclass).
- **GATE.** `python -m engine.season.harness.scene threadwork.work --fixture warden --seed 0`, with and without a decider.
- **Hash movers.** None with no host.
- **Depends on.** `IS-B3-WR-01`; `01_CORE_one_scene_contract.md` (PROPOSED, B34: B35 is after B34 in U3 §2.1).
- **Lane · batch · cost · tier · lands it.** WR (GO review) · B35 · small build · `sonnet` · the B35 session.

**Item: IS-B3-WR-04** — the gate for a person who cannot be understood (A-43; U4 G-15).

- **Advances.** WR integrated; R-07, R-08.
- **INSTRUCTION.** `U5d_WR_zero_coherence_unknowable.md` names no execution artifact. U4 G-15 drafted one and left "the tolerance and n" as calibration. **No tolerance is needed:** reader 2 multiplies the weight on what the believer holds by legibility, so at legibility 0 the believed odds are the prior exactly. New file `engine/season/tests/test_unknowable.py`, on a hand-built world with one person's Coherence written to 0 through the host (`IS-B3-WR-01`) and a witness who holds a claim of it: `test_at_zero_the_witness_s_believed_odds_equal_the_prior` (exact equality, over every candidate of the unknowable man's next deliberation, `assert checked >= 1`); `test_between_zero_and_full_the_estimate_lies_between` (one planted legibility strictly inside the interval); `test_his_seats_offices_and_goals_are_unchanged`; `test_the_witness_s_account_row_of_his_act_carries_no_reason`; `test_his_tell_deposits_nothing_a_hearer_can_use`; `test_a_second_witness_with_no_claim_of_his_coherence_reads_him_as_before` (the file's own falsifier: it comes through what the witness believes). Control: the same world with Coherence at its ceiling reproduces the base readings.
- **WHERE.** `engine/season/tests/test_unknowable.py`; the proposal gains its Gate section.
- **FALSIFIER and control.** As named. A hash control: with `legibility_curve` at `()` every world's hash is equal.
- **GATE.** `python -m pytest engine/season/tests/test_unknowable.py -q`.
- **Hash movers.** Any world with a person below full Coherence once the curve leaves control; none while the curve is `()`.
- **Depends on.** `IS-B3-WR-01`; `10_DICE_believed_odds_have_a_prior.md` (B05); `01_CORE_reason_trail_in_the_act_store.md` (B09); `11_GO_player_surface_contract_B.md` (B34). `[BLOCKED: the curve's values — Jordan (the proposal's own mark); the tests above do not need them.]`
- **Lane · batch · cost · tier · lands it.** WR · B35, with `U5d_WR_zero_coherence_unknowable` · edit · `sonnet` · the B35 session.

**Item: IS-B3-WR-05** — the wound at Askeheim is that territory's Thread ground.

- **Advances.** WR clocks; closes the content mark on `09_WR_world_motion.md` as far as the rulings reach.
- **INSTRUCTION.** `09_WR_world_motion.md` edit 1 adds `wound: {kind: <a site_kinds member that has band_floors>, condition: 0}` to T15's row and leaves the kind as Jordan's content. A-40 then ruled the wearing-down a real condition of places, "one site per territory; no new entity kind", and `12_ARCS_substrate_as_ground.md` (B35) adds that Site kind (`thread_ground`, its id marked as an assumption there). B12 lands the wound with a kind the roster already holds (the proposal's own fallback). When B35 adds the kind: one row edit, `wound.kind` becomes the Thread ground's id, and T15's ground Site is the wound (not a second Site on the territory). `[ASSUMPTION: the wound is T15's own Thread ground at condition 0 — basis: A-40's one site per territory; both are the substrate's condition at a place. The kind's name stays Jordan's.]`
- **WHERE.** The geography registry row (`systems/settlements/valoria_geography_v30.yaml`, the file `data/files.py:147` names), `harness/populated.py::build_realm`.
- **FALSIFIER and control.** `build_realm(0)` holds exactly one Site of the Thread-ground kind on `terr_T15`. Control: `wound=False` builds the realm without it.
- **GATE.** Band crossings ordered by distance from T15 (the reading `audits/09_WR_audit.md` §8 step 5 names for the wound; `engine/season/tests/test_in35_lattice_coupling.py` is its covering file), re-read after the re-point.
- **Hash movers.** The realm at build with the wound on; declared inside B35's one re-pin.
- **Depends on.** `09_WR_world_motion.md` edit 1 (B12); `12_ARCS_substrate_as_ground.md` (B35).
- **Lane · batch · cost · tier · lands it.** WR · B35 · edit · `sonnet` · the B35 session.

### 5.6 The INCOMPLETE WR proposals, each with its disposition

| file (batch) | missing part | disposition | needed for the test |
|---|---|---|---|
| `09_WR_B_threadwork_session_and_practitioner` (B35) | the host and the thread rows; three values (overweave step, fatigue scale, the cap on operations in a contact) | host and rows: **`IS-B3-WR-01`**. Values: `[BLOCKED: CONTENT — the joint calibration; they ship as data at the design set's figures, marked]` | yes (the host) |
| `14_VERBS_PHYSICAL_D_thread_read` (B35) | stage 2 waits on a writer of `Person.coherence` | **`IS-B3-WR-01`** | no |
| `U5d_WR_zero_coherence_unknowable` (B35) | the writer; a gate artifact | **`IS-B3-WR-01`**, **`IS-B3-WR-04`** | no |
| `12_ARCS_substrate_as_ground` (B35) | the operation row's band amounts and difficulty | the write is settled (`IS-B3-WR-01`, change 4). `[BLOCKED: DESIGN — the WR lane's design read on `opus` with `ners`, as the file orders]` | no |
| `09_WR_world_motion` (B12) | the wound's Site kind | **`IS-B3-WR-05`** | no |
| `09_WR_B_weather_with_memory_and_the_year` (B12) | edit 3 waits on CP-T10-01 (`route`, `route_pricing`); neither name is in `engine/season` at this SHA (grep) | `[BLOCKED: step 5's disposition of CP-T10-01]`; edits 1, 2 and 4 do not wait | no |
| `30_WR_D_momentum_and_its_brakes` (B38) | commit 2 lands after CR-98's rows | `[BLOCKED: step 5's disposition of CR-98]`; commit 1 does not wait | no |
| `31_WR_C_what_the_stances_feed` (B38) | no goal row carries `axis:` | `[BLOCKED: CONTENT — the goal rows' content pass]`; ships at its control | no |

---

## 6. GO — the player surface and the port

### 6.1 The test

| # | today (T), with the command | as proposed (P) |
|---|---|---|
| S1 entry | **not met for a seat.** `python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0` runs two seasons unseated (`rounds=5 acts=16`, then `rounds=5 acts=17`, hash `5405522c36b0399247f83fd9f6d29494`, 1.1 s; P-5). `python -m engine.season.harness.play_surface` prints nothing | **carried**, B34: `python -m engine.season.harness.play_surface --seed S --person P --seasons K [--scenario NAME]` (`11_GO_player_surface_contract_B.md` §8); a module's scene alone, `python -m engine.season.harness.scene <role> --fixture <name> --seed S` (`01_CORE_one_scene_contract.md` edit 4) |
| S2 scenario | `build_realm`; the corpus cases; `creation_sheet` lists the seated persons | every lane's scenario, by name, through the registry of `IS-B2-CORE-01` (B11). **owed:** the two row fields this lane's test needs (`IS-B3-GO-01`) |
| S3 surface | `DevelopmentSheet`, `chronicle(p)` (`decision/sheet.py`) | **carried**, B34: four readings and the scene pair; `explain` (the superseded file's §2, kept live); B38: the plot |
| S4 stub contract | `PlayHost` is typed for combat alone | **carried**, B34: `PlayHost.deciders`, a role with no decider is automated; "no decider means the person's own policy" (`11_GO_fidelity_and_campaign_modes.md` §2) |
| S5 stop conditions | death, then `carry_on`; "no end state reaches a client" (`audits/11_GO_audit.md` §9) | **carried in words** (`11_GO_fidelity…` §4: the line is extinct, or the player concludes). **owed:** a reading (`IS-B3-GO-02`); the reveal's gate (`IS-B3-GO-04`) |
| S6 artifact | `test_rem30_character_sheet.py`, `test_rem31_grid_suspension.py` (named by `play_surface.py`; not run) | **carried**, B34: `tests/valoria/test_play_surface.py` (four named), `test_play_surface_own_outcome.py`, `engine/season/tests/test_scene_contract.py`; B41: `test_surface_trace.py` |
| save and resume | none | **carried**, B06: `U5d_GO_owed_edits.md` §1 (a snapshot; `decode`). **owed:** a snapshot that names its scenario (`IS-B3-GO-03`) |
| S7 integrated | the port's contract is `World.content_hash()` over two season-shaped slices | **carried**, B41: `tools/export_oracle_pins.py --check` with `module_scenes`, `surface`, `halts`. **owed:** the scenario worlds as pins (`IS-B3-GO-05`); the gate's plan text (`IS-B3-GO-06`) |

**One naming collision, for v12's file census.** Two proposals name a new test file `test_play_surface.py` in two trees: `tests/valoria/test_play_surface.py` (`11_GO_player_surface_contract_B.md`, build order 1) and `engine/season/tests/test_play_surface.py` (`11_GO_fidelity_and_campaign_modes.md`, gate 3, its own `[ASSUMPTION: the file name]`). This lane's tests go in the second, the tree where the harness's other tests are. The two files are either merged at B34 or the second is renamed there; it is one edit and it is stated so that two sessions do not each create one.

### 6.2 The batch sequence

B00 → B01 → B02 → **B03** (`11_GO_pointer_and_stale_text_resolutions`, `11_GO_design_reference_disposition`; `IS-B3-GO-06`'s early landings) → B05 → **B06** (the keyed draw, the float contract, the snapshot) → B10 → **B11** (the scenario registry, lane IS-B2's; `IS-B3-GO-01`) → B24 → **B34** (the surface; `IS-B3-GO-02`, `IS-B3-GO-03`; `IS-B3-FA-02`) → **B38** (the plot; `IS-B3-GO-04`) and, beside it from W12, **B41** (the port gate; `IS-B3-GO-05`).

**A seat can play a season and read it at the close of B34.** Every scenario row that has landed by then (the inquiry at B11, the spine at B21, the valley at B12, the duel at B16, the hearing at B24) is playable through the one runner from that point; the field's row lands at B20, in B34's own wave, and the rows that land later (the Warden at B35, the lean year at B39, the institutions at B40) join it as they land.

### 6.3 Items

**Item: IS-B3-GO-01** — two fields on the scenario registry's row: what kind each ending is, and which roles the world cannot reach.

- **Advances.** S4 and S5 of every loop-played scenario; H-01's reading at the scale of a scenario.
- **INSTRUCTION.** The registry, its row and its loop are `IS-B2-CORE-01` (lane IS-B2; `engine/season/harness/scenarios.py`; B11, first item). This item is an amendment to that one, built in the same commit, and creates nothing of its own. (1) `Scenario` gains `kinds: Mapping[str, str]`, from each name its `ending` reader can return to a member of the closed tuple `ENDING_KINDS = ("won", "lost", "drawn")`. The dataclass refuses, at construction, a value outside the tuple. `run`'s returned dict gains `kind` beside the ending's name (`None` while the run goes on). (2) `Scenario` gains `unreached: frozenset[str]`, composition roles (members of `engine.substrate.composition.ROLES`, refused otherwise) whose per-role entry count must read 0 on this world. `run` already returns CI-11's per-role counts; no reader is added. (3) The registry's rule that every later entry resolves its names there (`IS-B2-CORE-01` (4) names `scene.py::FIXTURES`, `play_surface --scenario`, `headless --world`, `harness.valley`, `field_scene`, `governance_spine play`) is extended to two flags that item does not list: `storybar --world` (`23_STORY_D`, B36) and the `scenario:` names of the port gate's `module_scenes` block (`IS-B3-GO-05`, B41). Neither holds a list of its own. (4) A scenario whose opening situation is made by acts (FA's four) folds them inside its `build` (`IS-B3-FA-01`); the row needs no field for them.
- **WHERE.** `engine/season/harness/scenarios.py`; `engine/season/tests/test_scenarios_runner.py` (the file `IS-B2-CORE-01` creates).
- **FALSIFIER and control.** `test_every_ending_name_a_reader_can_return_has_a_kind` (for each registered row, the names its reader returned over seeds 0 to 2 are keys of `kinds`; `assert checked == len(SCENARIOS)`); `test_a_role_declared_unreached_reads_zero` (each row, seeds 0 to 2); and its control, a planted row that declares `unreached` a role its world enters, which must fail. A row with no `kinds` for a name is refused when the name is returned, not silently labelled.
- **GATE.** `python -m pytest engine/season/tests/test_scenarios_runner.py -q`; `python -m engine.season.harness.scenarios <name> --seed 0 --seasons K`'s summary line prints the ending's name and kind.
- **Hash movers.** None.
- **Depends on.** `IS-B2-CORE-01` (PROPOSED by lane IS-B2, B11); CI-11 (PROPOSED, B02).
- **Lane · batch · cost · tier · lands it.** GO states the fields; FI lands them with the registry (IN reviews the loop) · B11, with `IS-B2-CORE-01` · edit · `sonnet` · B11's session.
- **Overlap, stated so it is folded once.** This lane first drafted the registry itself and withdrew the draft on finding `IS-B2-CORE-01`. If v12's author prefers the registry earlier than B11 (it reads only CI-06's composition and three builders that exist today, so it could join B03 hash EQUAL and be on every lane's base from wave W3), that is a move of `IS-B2-CORE-01`, with this item, and it removes the ordering point of part 1, §3.2. It is not a second item.

**Item: IS-B3-GO-02** — a run's ending reaches the surface.

- **Advances.** GO standalone (S5), and S5 of every scenario; R-04.
- **INSTRUCTION.** The problem is part 1, §2, gap 2. (1) `harness/play_surface.py`'s transcript runner (`11_GO_player_surface_contract_B.md` §8) runs through `scenarios.run` (`IS-B2-CORE-01` (4)), and when the run returns an ending prints one line, `ENDING <name> <kind>`, after the seated person's last `account`, then stops. (2) The season's reader, which `IS-B2-CORE-02` writes (`season_ending`: `realm_ended` when `world_q.endings_reached(w)` is non-empty, `line_extinct` when `carry_on` returned no person, `time` at the count), gains the seat's side so that each name has one kind: `realm_ended` splits into `realm_held`, when one of the seated person's own live `commit`s is to the faction the reached row's holders cohere under (his own Tenures, read as `Situation.holdings` reads them), and `realm_fallen` otherwise; with nobody seated it stays `realm_ended`. Kinds: `realm_held` `won`; `realm_fallen` and `line_extinct` `lost`; `realm_ended` and `time` `drawn`. `time` is the headless stand-in for "the player concludes" (`11_GO_fidelity…` §4: a conclusion writes nothing). `[ASSUMPTION: a seat of the faction that holds the peninsula has won — basis: GD-1 as `rosters.yaml: endings` quotes it names the one victory, and the roster row's `under: one_faction` names the winner as a faction. The split is an amendment to `IS-B2-CORE-02`'s reader, made in this item's batch.]` (3) What the client is shown at an ending: the name and kind, `chronicle(p)` and the whole `account` (§4 of the fidelity proposal), and nothing of the world's truth. The antecedents `endings_reached` computes stay host-side and reach the client only through `reveal` (`IS-B3-GO-04`). (4) An ending is read at a season boundary only (the barrier at which a save is allowed), never inside a suspended scene.
- **WHERE.** `engine/season/harness/play_surface.py`, `engine/season/harness/scenarios.py` (`season_ending` and the `kinds` of the rows that use it), `engine/season/tests/test_play_surface.py`.
- **FALSIFIER and control.** `test_the_transcript_stops_on_an_ending_and_prints_its_kind` (a planted reader); `test_a_realm_ending_is_held_for_a_seat_of_the_holding_faction_and_fallen_for_another` (on the hand-built world `test_in27_endings.py` uses); `test_line_extinct_is_lost_and_a_living_continuation_is_not_an_ending`. Control: a reader that never returns a name leaves the transcript's hash equal to the plain run's (gate 1 of the surface contract).
- **GATE.** `python -m engine.season.harness.play_surface --scenario valley --seed 0 --seasons 12` ends with an `ENDING` line; the three tests.
- **Hash movers.** None.
- **Depends on.** `IS-B2-CORE-01`, `IS-B2-CORE-02`, `IS-B3-GO-01` (B11); `11_GO_player_surface_contract_B.md` §8 and `11_GO_fidelity_and_campaign_modes.md` (PROPOSED, B34).
- **Lane · batch · cost · tier · lands it.** GO · B34, after `11_GO_fidelity_and_campaign_modes` · edit · `sonnet` · the B34 session.

**Item: IS-B3-GO-03** — a snapshot names its scenario, so a client holding no engine state can resume.

- **Advances.** GO standalone (save and resume).
- **INSTRUCTION.** `U5d_GO_owed_edits.md` §1's snapshot is the GO-07 encoding of the hashed frames plus four named extras (`world_seed`, `tick`, the act store, the settings digest). A resumed run also needs to know which `ending` reader applies, which is not world state. (1) A fifth extra, `scenario`: a key of `SCENARIOS`, or `None` for a world no scenario built. (2) `decode` returns the name with the world and does not look it up (`state/` may not import the instrument package); `scenarios.resume` refuses an unknown name by value. (3) `scenarios.resume(snapshot, seasons, pick=None, host=None) -> dict`: decodes, looks the row up, and continues `run`'s loop from the decoded world without `build`. The seat is not saved: who is played is the client's own choice and changes at `carry_on`.
- **WHERE.** `engine/season/state/world.py` (beside the encoder, as §1 places `decode`), `engine/season/harness/scenarios.py`, `engine/season/tests/test_go07_canonical_digest.py`.
- **FALSIFIER and control.** `test_a_snapshot_names_its_scenario_and_resume_refuses_an_unknown_one`; `test_a_resumed_run_reaches_the_ending_the_unbroken_run_reaches` (for one registered row: `run(name, 0, 6)` against `run(name, 0, 3)` then `resume(..., 3)`: one hash, one ending). Control: §1's own round trip, unchanged, with `scenario` `None`.
- **GATE.** `python -m pytest engine/season/tests/test_go07_canonical_digest.py engine/season/tests/test_scenarios_runner.py -q`.
- **Hash movers.** None (no game path reads a snapshot).
- **Depends on.** `U5d_GO_owed_edits.md` §1 (PROPOSED, B06); `IS-B2-CORE-01` (B11).
- **Lane · batch · cost · tier · lands it.** GO, IN · B34 (the registry lands at B11, after B06, so the key cannot land with §1) · edit · `sonnet` · the B34 session.

**Item: IS-B3-GO-04** — the end reveal has a gate, in the batch that builds it (A-49; U4 G-14).

- **Advances.** GO standalone (S5).
- **INSTRUCTION.** U4 G-14 found A-49's reveal without a gate, placed two tests in `11_GO_fidelity_and_campaign_modes.md` gate 4 (B34) and marked the reading's name as an assumption. The reading has a name and a builder: `harness/play_surface.py::reveal(w, line) -> Reveal`, instruction 6 of `30_GO_F_the_plot_as_the_player_is_shown_it.md` (B38). The fidelity proposal's "one host-side reading" (§4) is that function; B34 builds none. (1) The tests land in B38 with the function: `engine/season/tests/test_play_surface.py::test_reveal_is_refused_while_a_person_of_the_line_lives`, `::test_reveal_is_refused_when_a_continuation_is_taken`, `::test_reveal_returns_what_the_line_believed_beside_what_was_so` (a planted lie believed by the seated person appears in `held_against_true` with the world's answer). (2) Its refusal reads the run's ending, not the realm alone: instruction 6 refuses "unless `world_q.endings_reached(w)` is non-empty or no person of `line` is alive"; for a scenario world the first clause becomes "the ending `scenarios.run` returned is not `None`", so a valley or a spine run can be revealed when it ends. Signature: `reveal(w, line, ending, continuation=False)`.
- **WHERE.** `engine/season/harness/play_surface.py`, `engine/season/tests/test_play_surface.py`.
- **FALSIFIER and control.** The three tests; `reveal` callable in play is `30_GO_F`'s own falsifier. Control: calling `reveal` leaves `content_hash()` equal (it writes nothing).
- **GATE.** `python -m pytest engine/season/tests/test_play_surface.py -q`.
- **Hash movers.** None.
- **Depends on.** `30_GO_F` (PROPOSED, B38); `IS-B3-GO-02` (B34).
- **Lane · batch · cost · tier · lands it.** GO · B38, with `30_GO_F` · edit · `sonnet` · the B38 session.

**Item: IS-B3-GO-05** — the scenario worlds are pinned, so the port plays them without porting a builder.

- **Advances.** GO integrated (S7); the standing requirement on the port's side; H-02.
- **INSTRUCTION.** The port re-implements no instrument (`master/HOLISTIC_AUDIT_part3.md` §8), and every scenario builder is in the instrument package. `11_GO_port_gate_order_and_coverage.md` §3's `module_scenes` block pins one module entry per scene from "a fixture world … built by the harness builders"; nothing pins a scenario a seat plays through a season. (1) `tools/export_oracle_pins.py` gains a `scenarios` block: for each `SCENARIOS` row and seeds 0 to 2, `initial` (the snapshot of the world `build` returns, in `U5d_GO_owed_edits.md` §1's format with `IS-B3-GO-03`'s key), `seasons` (a count declared on the block, the smallest at which the unwatched run reaches an ending, or 8), `content_hash` of the unwatched run, and `ending` (its name and kind). (2) The twelve `module_scenes` scenario names of §3 (`duel_even` … `finding_full`) are keys of `SCENARIOS`, so the fixture worlds have one owner. (3) `--check` rebuilds the block. A batch that lands or changes a row re-runs `--build` in its own commit and says so (the proposal's rule for behaviour pins; no ledger row). `[ASSUMPTION: GO-08's artifact can hold a world in the GO-07 encoding — basis: §1 of the port-gate proposal lists "initial worlds" among the behaviour pins; the GO-08 plan entry itself was not opened.]`
- **WHERE.** `tools/export_oracle_pins.py` (built in B41 by `16_PESSIMIST_GO_surface_pins.md`), `engine/engine_params/oracle_pins.json`, `tests/valoria/test_oracle_pins.py`.
- **FALSIFIER and control.** `test_each_scenario_pin_decodes_to_its_initial_hash_and_replays_to_its_ending` (red before the block exists). Editing one row's builder without a re-export reds `--check`. Control: slices 1 and 2 stay green under that edit, which is the case the season-shaped slices cannot see.
- **GATE.** `python tools/export_oracle_pins.py --check` OK with a `scenarios` block of every row landed by B41.
- **Hash movers.** None.
- **Depends on.** `16_PESSIMIST_GO_surface_pins.md`, `11_GO_port_gate_order_and_coverage.md` (PROPOSED, B41); `IS-B2-CORE-01`, `IS-B3-GO-01` (B11); `IS-B3-GO-03` (B34; B41 is after B34 in U3 §2.1).
- **Lane · batch · cost · tier · lands it.** GO · B41, after the `module_scenes` block · small build · `sonnet` · the B41 session.

**Item: IS-B3-GO-06** — the port gate's plan text is v12's own, and its early landings have a batch.

- **Advances.** GO integrated (S7); the fold of stage 6.
- **INSTRUCTION.** `11_GO_port_gate_order_and_coverage.md` §1, §2 and §5 are edits to `workplans/valoria_master_workplan_v11_part3.md` (the B10-20 card), `_part5.md` (the GO-12 and GO-15 entries) and `proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-B10-20.md`; its build order's step (1) lands them in B41. Adopting v12 deletes v11 in the same commit (`STAGES.md` step 6; CLAUDE.md §2), so at B41 those files do not exist. `16_PESSIMIST_GO_surface_pins.md` already re-points its one plan row to "the v12 card for GO-08". **For v12's author:** (1) B41's content-owner entry carries as its own text what §1, §2 and §5 decide: the contract and behaviour split (a contract change writes an `ED-GO-` row; a behaviour mover re-runs `--build` in its own commit and says so); GO-15 as two acts; GO-16 not built (A-30); GO-12's scope as every `os.environ` read under `modules/`, built in B17 and checked in B41; the order draw owner → float contract → GO-12 → GO-10 → module-scene pins → GO-08 → GO-15a → GO-15b. Step (1) of the proposal's build order is dropped from B41's items. (2) The four early landings §2 names (GO-01, GO-11, GO-05, GO-09: each hash EQUAL, each with a `--check`) are plan positions of v11 with no batch in U3. They join B03 as its last items, after the registry edits of that batch, so that GO-09's check is live through every later batch that edits a registry, which is the reason the proposal gives for landing it early. `[ASSUMPTION: each of the four is hash EQUAL and needs nothing after B03 — basis: the proposal's §2 table; the four plan entries were not opened, and step 5 gives each its disposition. One that is not hash EQUAL does not join B03.]`
- **WHERE.** v12's B41 and B03 entries; the files of GO-01, GO-11, GO-05, GO-09 as their plan entries name them (`references/engine_series.yaml`, `references/module_contracts.yaml`, the manifest, `tools/export_season_registries.py`, per `audits/11_GO_audit.md` §8 step 1).
- **FALSIFIER and control.** A registry row edited after B03 without a re-export reds GO-09's `--check`; the same edit before GO-09 lands reds nothing.
- **GATE.** Each early landing's `--check` prints OK at B03's close (the proposal's gate 4, with "before B10-18b merges" read as "at B03").
- **Hash movers.** None.
- **Depends on.** The four plan positions (step 5); `11_GO_port_gate_order_and_coverage.md` (B41).
- **Lane · batch · cost · tier · lands it.** GO · B03 (the landings) and v12's text for B41 · edit · `sonnet` · the B03 session; v12's author.

### 6.4 The INCOMPLETE GO proposal

| file (batch) | missing part | disposition | needed for the test |
|---|---|---|---|
| `16_PESSIMIST_GO_surface_pins` (B41) | about 150 display strings for verbs and Event kinds | `[BLOCKED: CONTENT — Jordan, or authored under his review (the file's own mark)]`. The key sets are derivable now by the two commands the file gives; `tools/export_names.py --check`'s completeness rule lands with the strings or reds | no for the Python runner (it prints keys); yes for a port that shows words |

---

## 7. The tables v12 takes

### 7.1 Items by batch (22 items; every one joins an existing U3 handle; no new batch)

| batch (lane, wave) | items, in landing order within the batch | position in the batch |
|---|---|---|
| B03-hygiene (IN, W3) | `IS-B3-SE-04`; `IS-B3-GO-06` (the four early landings) | SE-04 after CI-03; the landings last |
| B11-fi-readers (FI, W9) | `IS-B3-GO-01` | with lane IS-B2's `IS-B2-CORE-01`, the batch's first item |
| B12-world-motion-and-ground (SE+WR, W10) | `IS-B3-SE-03`; `IS-B3-SE-05`; `IS-B3-SE-01` | SE-03 first commit; SE-05 with `14_VERBS_MATERIAL_A`; SE-01 last |
| B21-fa-governance (FA, W9) | `IS-B3-FA-05`; `IS-B3-FA-06`; `IS-B3-FA-01` | FA-05 after `14_VERBS_BINDING_D`; FA-06 with the rest of `U5d_FA_owed_edits`; FA-01 after `06_FA_shortest_loop_B` |
| B23-land (FA, W13) | `IS-B3-FA-04`; the added gate arm of part 1, §3.4 row 3 | after `U5d_FA_land_and_seats_pass_on_a_won_march` |
| B34-go-surface (GO, W11) | `IS-B3-GO-02`; `IS-B3-GO-03`; `IS-B3-FA-02` | after `11_GO_fidelity_and_campaign_modes` |
| B35-wr-thread (WR, W13) | `IS-B3-WR-01`; `IS-B3-WR-03`; `IS-B3-WR-02`; `IS-B3-WR-04`; `IS-B3-WR-05` | WR-01 after `09_WR_B_threadwork…` edits 1 and 2; the rest in this order |
| B38-narrative-regimes (WR, W15) | `IS-B3-GO-04`; `IS-B3-FA-03`; `IS-B3-SE-02` | GO-04 with `30_GO_F`; the two readings after `30_WR_E` and `U5d_SE_cohort_heavy_moves_and_caste` |
| B41-go-port-gate (GO, W12) | `IS-B3-GO-05`; v12's text per `IS-B3-GO-06` | after the `module_scenes` block |

Count: FA 6, SE 5, WR 5, GO 6.

### 7.2 Declared hash movers

| item | moves a world's content hash | re-pin |
|---|---|---|
| `IS-B3-FA-04` | only when `march_grievance_regard` leaves `None` | co-pinned at B23's last item |
| `IS-B3-FA-05` | every world in which a `dispatch` is complied with | B21's one re-pin |
| `IS-B3-FA-06` | every world with a succession after an `issue` | B21's one re-pin |
| `IS-B3-SE-05` | worlds with a non-public deed and a co-located bystander, once `notice_arm` is on | with B11's flip of `notice_arm`; no second re-pin |
| `IS-B3-WR-01` | every executed thread row | B35's one re-pin |
| `IS-B3-WR-04` | none while `legibility_curve` is `()` | — |
| `IS-B3-WR-05` | the realm at build with the wound on | inside B35's re-pin |
| the other fifteen | none (harness, instruments, exporters, tests, text) | — |

### 7.3 File census additions (serial order is the batch order)

| file | items | batches |
|---|---|---|
| `engine/season/harness/scenarios.py` (new at B11, by `IS-B2-CORE-01` and `08_FI_03`) | GO-01; FA-01; SE-01; GO-02; GO-03; WR-02; each later lane's row | B11 → B21 → B12 → B34 → B35 → … (a row is appended at the end of the mapping; B11 and B21 are open together and merge in handle order) |
| `engine/season/harness/play_surface.py` | GO-02; GO-04 | B34 → B38 (already serial in U3 §5.1) |
| `engine/season/harness/governance_spine.py` | FA-01; FA-02 | B21 → B34 (U3 has B21 → B24 → B40; B34 is added between B24 and B40) |
| `engine/season/harness/valley.py` | SE-01 | B12 |
| `engine/season/harness/storybar.py` | FA-03 | B38 (serial instrument file, C3-K7) |
| `engine/season/harness/populated.py`, `aperture.py` | SE-03 | B12 |
| `engine/season/queries/world_q.py` | FA-04; FA-06 | B23; B21 |
| `engine/season/verb_table.yaml`, `rosters.yaml` | FA-04, FA-05, SE-05, WR-01 | B21, B23, B12, B35 |
| `references/module_contracts.yaml` | SE-04; WR-01 | B03 → B35 |
| `engine/season/seam/wrappers/threadwork.py`, `modules/threadwork/working.py` | WR-01; WR-03 | B35 |
| `engine/season/state/world.py` | GO-03 (one extra on the snapshot `U5d_GO_owed_edits` §1 built in B06) | B06 → B34 |
| `engine/season/tests/test_scenarios_runner.py` (new at B11, `IS-B2-CORE-01`'s) | GO-01; GO-03; WR-02 | B11 → B34 → B35 |
| `tools/export_oracle_pins.py` | GO-05 | B41 |
| `engine/season/tests/test_play_surface.py` | GO-02; GO-04; the fidelity proposal's gate 3 | B34 → B38 (see the naming collision, §6.1) |

**Edges added to U3's graph** (all forward): B11 → B21 for the registry file, which is a merge order inside wave W9 and not a wait (part 1, §3.2); B11 → B12, B34, B35, B41 (each already after B11); B21 → B34 for `governance_spine.py`; B06 → B34 for the snapshot (already implied: B34 is after B24, B24 after B07, B07 after B06). No batch gains a dependency on a later one.

### 7.4 The requirement map this lane contributes (STAGES step 6, rule 1)

Readings, not decisions: the row's state is what `register --requirements` prints at the batch's close. Today: `met 3 · not_met 1 · partial 5` (P-1).

| batch | requirement rows its close can advance | by which execution artifact |
|---|---|---|
| B12 | R-04 (the settlement scale), R-05 (`found`, `build`, `work`, `tend`, `restore`, `transfer`, `requisition` execute) | `valley` policies end differently (SE-01's gate); the `settlement_motion` block (SE-03); CI-11 rows `settlements.drawn_under`, `.fabric` |
| B21 | R-04 (grand strategy politics), R-05 (`comply`, `evade / defy`, `construe`, `revoke`, `confer`, `succeed`, `dispatch`) | `governance_spine play SEED 8 --world realm` reads `closed True`, `persons ≥ 3`, seeds 0 to 2 |
| B23 | R-04, R-05 (`march` on an occasion, `seize`) | `aperture 2 0` and `2 2`; CI-11 row `mass_battle.resolve_field` |
| B34 | no row by itself; it is what makes R-04's "decisions at differing scales" playable by a seat | the transcript's hash equals the plain run's; an occasioned row in the first deliberation of each scenario |
| B35 | R-05 (the thread verbs), R-09 (a working is drawn) | `aperture 1 0`; CI-11 row `threadwork.work`; `test_threadwork_loop.py` |
| B38 | R-01, R-04 under A-80 and A-81 | the entrenched and null-scene arms on `realm`, `valley`, `spine.recall`, `warden` |
| B41 | none (the port's ground) | `export_oracle_pins.py --check` |

### 7.5 Gaps and findings this lane closes, and those it passes on

| source | id | disposition here |
|---|---|---|
| `U4_TRACEABILITY.md` §6 | G-7 (domain actions) | `IS-B3-SE-04` |
| | G-14 (the reveal's gate) | `IS-B3-GO-04` (placed in B38, where the function is built) |
| | G-15 (zero coherence's gate) | `IS-B3-WR-04` (exact arm; no tolerance) |
| | G-16 (a march's occasions) | `IS-B3-FA-04` (the `claim` basis is not widened) |
| | G-1 (`_siege`, `besiege`) | not this lane's: MB (lane IS-B1). Cross-listed: `U5d_STORY_owed_edits` §1 and `04_MB_playable_field_scenario` wait on it; FA's standalone test does not |
| | G-2 (the scale vocabulary), G-5 (the requirement map) | lane IS-A |
| | G-6 (a player-created person) | not raised: IN-47 C1 is the ruled shape (`11_GO_fidelity…` §4: the player picks a seated person) |
| | G-11 (the null-scene reading from B02) | lanes IS-A and IS-B2; `IS-B3-FA-03` and `IS-B3-SE-02` quote it |
| | G-10 (a skill's loss), G-13 (a construal tested at a bench) | not this lane's subjects: the skill surface and SC (lane IS-B2) |
| | G-12 (the 46 ages) | content; B37 |
| `U4_DOCUMENT_STATUS.md` §3.4 | `14_VERBS_BINDING_D` (and through it `BYZANTINE_D`, `COLONIAL_grounding_F`, `SYNTHESIS_E`) | `IS-B3-FA-05` |
| | `U5d_FA_owed_edits` §9 | `IS-B3-FA-06` |
| | `U5d_FA_land_and_seats_pass_on_a_won_march` | decided (§8 row 3); one gate arm |
| | `14_VERBS_MATERIAL_A_mending` | `IS-B3-SE-05` |
| | `14_VERBS_PHYSICAL_D`, `U5d_WR_zero_coherence_unknowable`, `09_WR_B_threadwork…` (the host) | `IS-B3-WR-01`, `IS-B3-WR-04` |
| | `09_WR_world_motion` | `IS-B3-WR-05` |
| | the other FA, SE, WR, GO rows | blocked, each with its reason and owner (part 1 §3.4, §4.4; §5.6, §6.4) |
| `master/HOLISTIC_AUDIT_part2.md` | H-01 (engines reached unevenly) | each S7 above quotes CI-11's block; `IS-B3-SE-03` adds the settlement block |
| | H-02 (no entry point; six builders; hand-composed run loops) | lane IS-B2's `IS-B2-CORE-01` (one loop for scenarios), which this lane's rows use; `IS-B3-GO-05` (scenario worlds as pins, so the port ports no builder). `J-H-01` and CI-07 are untouched |
| `master/CODEBASE_IMPROVEMENT_PROPOSAL*.md` | CI-06, CI-11 | depended on (B03, B02); CI-01 to CI-05, CI-07 to CI-10 are not this lane's subjects |

## 8. Decided by the ladder, and reversible on a word

Nothing in this file overwrites ratified canon, a `(RULED)` item or a ratified Layer 1 row, so nothing is added to `master/instructions/IS_FOR_JORDAN.md` by this lane. These are the places where a careful reader could have gone the other way.

| # | what was decided | the other way | step that decided it | to reverse |
|---|---|---|---|---|
| 1 | **A scenario's ending carries a kind (won, lost, drawn) as a label in the harness registry** (`IS-B3-GO-01`), never as a row of `rosters.yaml: endings` | no kinds: a run just ends, and the client reads what it likes | 3 and 5: the work order asks for the kinds; GD-1's one victory row is untouched because the loop never reads a kind | delete the `kinds` field; the readers still stop the run |
| 2 | **A writ does not pass to a successor; he is asked about it and may issue it again** (`IS-B3-FA-06`) | a new write basis, "a Record's hold follows the seat that issued it" | 3: `04` §C.2's enumeration is complete as ratified; the other way is Jordan's amendment | amend §C.2 and restore `U5d_FA_owed_edits.md` §9 reading (ii) |
| 3 | **Seats pass with the land as the right to fill them**: a `seize` vacates the anchored seats and the seizer is offered them (`U5d_FA_land…` reading (i)) | the seizer holds them at once, by a new basis | 3, and U3's C3-L7 (already shown to Jordan in `unified/U3_JORDAN_CALLS.md`, "Not yours"); this lane only corrects C3-L7's last clause, which the tree refutes | amend §C.2 and build reading (ii) |
| 4 | **A man sent by `dispatch` goes by his own answer** (`IS-B3-FA-05`, change (b)) | the sender's act moves him (CP-T09-08 as written at its home) | 1 and 3: A-24, and the row's own ruled note ("their own choose decides") | restore CP-T09-08's effect; the row's ruled note is then touched and must be listed |
| 5 | **A march's occasion is read from the person's side; the `claim` gate basis is not widened** (`IS-B3-FA-04`) | widen the basis so a non-heir may hold a claim Tenure | 5: the basis admits `succeed`; widening it changes who may take a seat | add the basis arm |
| 6 | **The `domain_actions` contract row is retired and ED-FA-0002 superseded** (`IS-B3-SE-04`) | author the home document that row asked for | 1 and 2: A-10; the Key substrate is retired | drop the item; the row stays with `doc: null` |
| 7 | **Whether a sabotage is seen is the notice draw's** (`IS-B3-SE-05`) | a masking rule or a new formation stem | 4: B11's notice draw; C3-C14's "perception is a drawn deposit, not a gate" | — |
| 8 | **One writer of `Person.coherence`: the host** (`IS-B3-WR-01`, change 4) | a task row's bands write it too (ARCS-03 item 3) | 5: the write gate refuses any driver but the seam | — |
| 9 | **The wound is T15's own Thread ground** (`IS-B3-WR-05`) | a Site of another kind beside the ground | 1: A-40, one site per territory | keep the B12 kind |
| 10 | **The port plays a scenario from a pinned world, not from a ported builder** (`IS-B3-GO-05`) | port each scenario's builder | 4 and 5: the port re-implements no instrument, and the builders are instruments until `J-H-01` is answered | build the pins anyway; port a builder when CI-07 has moved it into game code |

## 9. Limits, stated once

- **Read in full:** the work order; `STAGES.md`; `README.md`; `AUDIT_BRIEF.md`; `unified/DECISIONS_ANSWERED.md` (A-1 to A-98); `master/HOLISTIC_AUDIT.md` and parts 2 and 3; `master/HOLISTIC_FOR_JORDAN.md`; the proposals `06_FA_playable_scenario`, `06_FA_shortest_loop_B`, `06_FA_war_lives_in_seats_B`, `U5d_FA_owed_edits`, `07_SE_valley_scenario`, `23_STORY_E`, `09_WR_B_threadwork_session_and_practitioner`, `U5d_WR_zero_coherence_unknowable`, `12_ARCS_substrate_as_ground`, `11_GO_player_surface_contract_B`, `11_GO_fidelity_and_campaign_modes`, `11_GO_port_gate_order_and_coverage`, `16_PESSIMIST_GO_surface_pins`, `U5d_GO_owed_edits`, `01_CORE_one_scene_contract`.
- **Read in part:** `unified/U3_DEPENDENCY_ORDER.md` (§0 to §2 in full; §5.1 and §6.3 by search); `unified/U4_TRACEABILITY.md` (§0 to §4, §6, §7); `unified/U4_DOCUMENT_STATUS.md` (§3); `unified/U3_LAYER1_AMENDMENTS.md` and `unified/work/L1_APPLIED.md` (the node tables); `master/CODEBASE_IMPROVEMENT_PROPOSAL*.md` (§0 to §3, CI-07, CI-11, §4 to §6); the four audits at §8 to §10; `.claude/skills/methodology-execute/SKILL.md` (0.2 to 0.5 and BATCHES); the glossary by row search; the other FA, SE, WR, GO proposals at head, gate and the lines cited. **Not read:** the dossiers and digests of the four subjects (the audits' §9 and the proposals were used in their place), `engine/season/requirements.yaml` beyond the lines cited and its printed register, the audit addenda and pessimist audits, `U1_OWNERS_AND_VOCABULARY.md`, `U2_LAYER1_CONFORMANCE.md`, the closure tables.
- **Sibling lanes' files were read by search, not in full.** `master/instructions/IS_B2_SC_FI_CORE_CHAR_part2.md` §3.1 (`IS-B2-CORE-01` to `-03`) was opened because it owns the scenario registry this lane's rows use; the field names used here (`build`, `verbs`, `seat`, `ending`, `role`, `run(name, seed, seasons, pick, host)`) are that item's as read at this SHA, and if lane IS-B2 changes them the rows here follow it. `IS_A_NINE*.md` and `IS_B1*.md` were searched for overlap only.
- **Plan positions of workplan v11 are cited at their home text only where an item carries them** (CP-T07-01, -02; CP-T08-01; CP-T09-08; the B10-15 card's order line). Their dispositions are step 5's. An item that says a position "is still needed" states this lane's reading and its reason, not a disposition.
- **No pytest was run** and no proposal's gate was run: none of the proposed commands exists yet. Every test named in an item is a name for a later batch to write; every expected reading is a prediction to be read at that batch's close.
- **The stub declarations are instructions to measure, not measurements**, except the spine's (P-3). The expected `unreached` roles are stated by construction and must be confirmed by CI-11's reading at landing.
- **Thresholds marked `[ASSUMPTION]`** ("two of five", "two of three") follow the suite's own C8 form, which is itself marked for Jordan to correct.
- Other lanes were editing proposals in the working tree while this was written (`git status --short` lists `06_FA_hygiene.md`, `06_FA_war_lives_in_seats_B.md`, `16_PESSIMIST_FA_B…` among others, for the A-98 word sweep). Citations to those files are by section and symbol.

## 10. Evidence log

All from the repository root, `PYTHONHASHSEED=0`, at `b07fc1c`. Nothing was written outside `master/instructions/`.

| # | command or probe | seed, seasons | outcome |
|---|---|---|---|
| P-1 | `python -m engine.season.harness.register --requirements`; `python tools/m1_acceptance.py --summary` | —; 20260819 ×1, 24 seeds ×4 | `met 3 · not_met 1 · partial 5`; `verdict: NOT MET`, one row failing (the nine, 3/9, DOC-DERIVED); rows 1, 2, 4 PASS, hash `bbf88d55e218…` twice |
| P-2 | `python -m engine.season.harness.governance_spine`; `python -m engine.season.harness.play_surface` | — | a census (`offices 13, persons 13, rungs 26, seated 13`), no season, 0.7 s; the second prints nothing and exits 0 |
| P-3 | scratch probe: `governance_spine.build(0)`, `SeasonDriver`, `probes.chooser(w, verbs=resolvable_verbs())`, three seasons with `populated.run`'s arguments | 0, 3 | 1.1 s; 4,593 Events; 311 resolved acts; hash `8d76d7e7e4230ffa3933f56cb2eafee0`; `order.given` 4, `compliance.impossible` 3, `march.declared` 25, `march.refused` 25, `tenure.closed` 3, `term.matured` 33, `finding.made` 16, `finding.none` 16, `matter.undetermined` 1, `requisition.unauthorized` 6; no `field.*`, `fight.*`, `tenure.opened` or `compliance.given` kind; 34 Events carry a degree |
| P-4 | `python -m engine.season.harness.scarce` | 0, 4 ticks, two arms | 1.2 s; hashes `d2730068e19527208b8b32b06bb36ba3` (question named) and `631b80ad65728c9787d41e85f8037392` (not named); one `transfer.made` (8 salt), the other transfers granary-to-granary and refused; grain delivered 0 at ticks 1 to 3 |
| P-5 | `python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0` | 0, 2 | 1.1 s; `rounds=5 acts=16 events=17`, `rounds=5 acts=17 events=92`; 66 of 67 verbs foldable; hash `5405522c36b0399247f83fd9f6d29494` (equal to the holistic audit's reading) |
| P-6 | `python -m engine.season.harness.strife 2 0 --strands` | 0, 2 | 26 s; `3 strands, 1 era(s)`; the era `OPEN`, 38 moves, opening kinds `march.declared, petition.filed`; open referents `detain 0, ban 0, at_war 0, docketed 3` (equal to `30_WR_A`'s cited reading) |
| P-7 | `git diff --name-only 4dc8a7b b07fc1c -- engine modules tools references` | — | `references/id_reservations.yaml` only: the code tree is unchanged since the holistic audit's readings |
| P-8 | greps, each as quoted at its item: `_eff_dispatch`; `coherence` under `engine/season` (non-test); `labour_mode`, `route_pricing`; `besiege` in `rosters.yaml`; `domain_actions` and `DA_proposal` outside `proposals/`; `module_contracts` in `tools/*.py`; `def ` in `harness/exercises.py`, `harness/play_surface.py`, `decision/sheet.py` | — | no `_eff_dispatch`; `coherence` only at `state/world.py:1301-1308`; neither `labour_mode` nor `route_pricing`; `besiege` in notes only (`march_postures` holds `storm`); the contract row, the vocabulary banner, two skill scripts, the requirements note, one archive; thirteen tools; `exercises.py` holds no world builder; `play_surface.py` holds `dispatching_chooser` and `carry_on` only |

**Controls and their limits.** P-3 is one seed and three seasons of one small world: it shows that the spine holds no situation and that a march on it is refused, and it is not a rate. P-5 and P-6 reproduce other lanes' readings at this SHA, which with P-7 is the control that the tree those lanes read is the tree this lane read. No number here is a balance claim.
