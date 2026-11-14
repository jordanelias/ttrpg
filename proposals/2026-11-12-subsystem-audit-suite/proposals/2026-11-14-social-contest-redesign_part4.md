# SC · DICE — the social contest redesigned, part 4: the build items (B24p.13 to B24p.99)

## Status: PROPOSED (the fourth part of `2026-11-14-social-contest-redesign.md`; read that file's head first, and part 3's E.0 for the batch block these items belong to; reference under CLAUDE.md §0.05, nothing reads it at runtime)

⚠ R11 (2026-11-14) is folded into the plan's copy of these items only (`master/workplan_v12/workplan_v12_part22_b24p_cont.md`); where they differ, that copy governs (part 3, §E's note).

---

### B24p.13 — the host builder · RD §C.5, §C.7, §A.3 · BUILD · HASH EQUAL
- SOURCE: RD §C.7 (each binding and the carrier it reads), §C.5 (the room), §A.3 (the records it fills); `sigma.py::contest_input` (`:183-226`, the precedent and its F8 note); B24.10 (HEAR_B edit 6, which planned `hearing_input`: this is that builder, generalised); `04` §A.2 (the adapter builds a typed input from a projection).
- ADVANCES: none (no caller until B24p.19); the one place `World` is read for a proceeding.
- INSTRUCTION: `engine/season/seam/wrappers/sigma.py`:
  1. `proceeding_input(w, claimants, *, verb, subject, topic, rung, effort, row, state=None) -> ProceedingInput`, where `row` is an arrangement row dict (a seeded one, or `abridged(row, move)`'s). It fills:
     `type` — `ProceedingType` from the row: `moves` from the row's own `moves` if present (the abridged form) else `RITES[row["rite"]]["moves"]`, each id replaced by its `Move` record from `PROCEEDING_MOVES`; `standard = fx.get("standard_demand")[row["standard"]]`; `difficulty` the verb row's level sized by `difficulty_ob` (B05.14); `stakes` the `stakes_ob` of `row["disposes"]` (B05.21), 0 for `none` or `Record`; `break_at`, `strikes`, `exchanges`, `order`, `disposal`, `presumes`, `quorum` as the row and the fixture give them;
     `speakers` — `_speaker(w, pid, side, …)` for `claimants[0]` as `for`, and for the opponent as `against` where the rite gives `against` a move: the six attributes from `Person.attributes` (an unheld key reads the mid-point); `ranks` from `pool._capability` for every skill the rite's moves name and `insight`; `addends` the `POOL_ADDENDS` sum; `score = pool.score(w, p, verb)`; `proofs = world_q.proofs(w, pid, other, rung)`; `operands = obstacle_operands(w, act, row)` as four-tuples (B24p.05), less the `bound: module` members; `accounts` = the names of the `eased_by: reason` operands when `person_q.attributed_deeds(p.ledger, other)` is non-empty `[ASSUMPTION: holding any deed claim about the other counts as knowing his circumstances — basis: B28.34 names `attributed_deeds` for "knowledge of the other person"; B28.35 may narrow it per term]`; `levels` from the `bound: host` advantage sources other than `proofs`, each pair of level lists summed to sigma through `levels_to_net_sigma`; `precedence` the rung ordinal of his highest seat; `effort = effort + 1` for the actor and `type.exchanges[1]` for the one addressed `[ASSUMPTION: a person answers for as long as he is spoken to and his resolve lasts — basis: he formed no act of his own]`; `moved_by = person_q.moved_by(p)`; `strain = person_q.strain_carried(...)`;
     `deciders` — by `row["disposal"]`: `bench`, `declared` → `judging_set(w, rung, topic)` in id order, each `_decider(...)` with `pool = faculty(w, seat holder, verb)`, his seat's `modifier`, `lean` 0.0 here (B24.02's commit term and B24.11's per-member count fill it); `hearers` → the one addressed (the opponent, as a `Decider` with the base pool and his own `score`) followed by the hearers; `mutual`, `exchange`, `none` → `()`;
     `hearers` — RD §C.5: `audience_of` (B07.04) less the speakers and the bench, filtered by the row's `floor`; each `_decider` with `pool = pool_of(untrained(fx), 0, pool_add, pool_floor)`, `lean` from `person_q.stance_toward(hearer, speaker)` clamped at `STANCE_MAX` times `regard_step`;
     `room` — `Room(audience_kind(...), **AUDIENCE_KINDS[kind], reception=((speaker id, world_q.reception(w, speaker id, rung)), …))`;
     `grounds = GROUNDS` ids; `dials = proceeding_dials(fx)`; `issue = None`; `state` as passed.
  2. `audience_kind(bench: int, hearer_weight: int, crowd_at: int) -> str` (pure; RD §C.5).
  It reads `w.persons`, `w.fixtures`, seats and each person's own interior; of ledgers, only a speaker's own (`accounts`, `proofs`, as `contest_input` does). No write, no token.
- WHERE: `engine/season/seam/wrappers/sigma.py` (`proceeding_input`, `_speaker`, `_decider`, `audience_kind`); NEW `engine/season/tests/test_sc_proceeding_host.py`.
- TESTS: in the new file, written first and read red: `test_an_abridged_tell_has_one_speaker_and_no_decider`; `test_a_bench_row_seats_the_judging_set_as_deciders`; `test_the_room_is_computed_from_who_is_present` (the same row at an empty hearth, with two onlookers, with a cohort of weight 30: `none`, `gallery`, `crowd`); `test_a_closed_floor_admits_no_hearer`; `test_the_builder_reads_no_ledger_but_a_speakers_own` (every other person's `ledger` replaced by an object that raises on access: the builder returns).
- FALSIFIER and CONTROL: a field read from another person's ledger (F8); a record holding a `Person`. Control: no caller: the seed-0 hash equal.
- GATE: `python -m pytest engine/season/tests/test_sc_proceeding_host.py -q` → five pass; hash equal.
- HASH MOVERS: none.
- DEPENDS ON: V12 B24p.03 (`RITES`, `AUDIENCE_KINDS`, `abridged`), .04 (`proceeding_dials`), .05, .06, .12; V12 Batch B07-task-draw (`audience_of`); V12 Batch B05 (`obstacle_operands`, `difficulty_ob`, `stakes_ob`, `regard_step`); EXISTS-IN-TREE `world_q.judging_set`, `::reception`, `::proofs`, `::presence`, `pool.faculty`, `::score`, `::untrained`, `person_q.stance_toward`, `::attributed_deeds`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B24p's producer; `Item: B24p.13`, `[skip ci]`.

### B24p.14 — the provider path and the believed odds · RD §A.5, §A.2; `04` §C.5 · BUILD · HASH EQUAL
- SOURCE: RD §A.5 (how the host reads each disposal), §A.2 (the decider argument); `sigma.py::resolve` (`:495-601`: the `Margin` hold, S27.4), `::believed_input` (`:296-344`), `::believed_chance`; `04` §C.5 (the seam grades one margin; a veto can only demote); B24.11 (the declared reading); INT E-13.
- ADVANCES: none (not yet dispatched to); the adapter half of the entry.
- INSTRUCTION: `engine/season/seam/wrappers/sigma.py`:
  1. `resolve(...)` gains a keyword `proceeds: Optional[tuple] = None` (`(row dict, form, move)`, resolved by the seam at B24p.19). When it is `None` the body is today's, byte for byte. When given: build `proceeding_input`; look the entry up with `entry_for(prize, _PROVIDER, "social_contest.proceeding")`; call `entry.fn(inp, rng, decide=None)` (every sitting of this batch is automatic: B24.05 and B24.13 hand a decider in); raise `Unspecified` naming the entry if the return is not a `ProceedingOutcome` or any verdict is not a `Margin` (the message `resolve` uses for a non-`Margin` today); then `act_margin`.
  2. `act_margin(outcome, type) -> tuple[Optional[Margin], bool]`: the act's one margin and a veto, by `type.disposal`: `exchange`, `bench` → the first verdict, no veto; `declared` → the first verdict (the presiding seat's), with `veto = True` when fewer than `type.quorum` verdicts grade Success or better through `ladder.degree_of` (B24.11's rule: a veto only demotes); `hearers` → `Margin(net = weight-mean of the verdicts' nets, ob = weight-mean of their obs)`, a real pair saying how the address went with the room as a whole; `none`, `mutual` → the last drawn exchange's margin (how the last speech went; under `mutual` the agreement itself is B24.30's `accept`); an `adjourned` sitting → `(None, False)` and the adapter returns `status="ADJOURNED"` (no band; B24's `adjourn` owns its fold).
  3. S27.4 is applied to an `exchange` disposal's pair only, as today (`ob > obstacle_refusal_multiple x pool`, on the speech's own record); a ballot is the decider's draw and is never refused.
  4. RESOLVED → `dict(status, module, resolver, pool, net, ob, leverage, terms, levels, veto, proceeding=outcome)`: `pool`, `leverage`, `terms`, `levels` those of the draw the act's margin came from (the exchange, or the first ballot).
  5. `believed_chance(w, holder, act, bands)`: for an act whose verb row carries `proceeds:`, the chance is `exchange_odds` (B24p.07) summed over `bands`, on a `ProceedingInput` built from what the holder holds: himself as the speaker at his own true values; the one addressed with `score` from the holder's `capability:` claim (none held → `None`, as today), every other attribute at the mid-point and `moved_by` flat unless he holds `moved_by` claims on him (B24p.22); the room his own believed one, or `none`. For a full form it is the first exchange's odds `[ASSUMPTION: the chooser prices a full proceeding by its opening speech — basis: the smallest honest figure; pricing the whole run is B24.13's `closing_odds` decider]`.
- WHERE: `engine/season/seam/wrappers/sigma.py` (`resolve`, NEW `act_margin`, `believed_chance`); `engine/season/tests/test_sc_proceeding_host.py`; `engine/season/tests/test_sc01_provider.py` (read; green).
- TESTS: written first and read red: `test_a_proceeding_return_that_is_not_an_outcome_raises` (a planted entry returning a winner string); `test_the_acts_margin_by_disposal` (hand-built outcomes for the six disposals); `test_a_declared_close_under_quorum_sets_the_veto`; `test_believed_odds_use_his_own_values_and_the_midpoint_for_the_other`; `test_believed_odds_are_none_without_a_claim_on_the_hearers_score` (today's rule, kept).
- FALSIFIER and CONTROL: a path on which a band or a side crosses the module boundary; `resolve` with `proceeds=None` differing from before (the control: `test_sc01_provider.py` green and the seed-0 hash equal).
- GATE: `python -m pytest engine/season/tests/test_sc_proceeding_host.py engine/season/tests/test_sc01_provider.py engine/season/tests/test_odds_of.py -q` → pass; hash equal.
- HASH MOVERS: none.
- DEPENDS ON: V12 B24p.13; EXISTS-IN-TREE `sigma.py::resolve`, `::believed_chance`, `seam/ladder.py::degree_of`, `seam/wrappers/_entry.py::entry_for`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B24p's producer; `Item: B24p.14`, `[skip ci]`.

### B24p.15 — every computed case names its row · RD §C.6 item 3 · BUILD · HASH MOVER(behaviour)
- SOURCE: RD §C.6 item 3 (the table and the function, copied); `loop/effects_information.py::_eff_open_case` (`:417-431`: *"WHICH arrangement a computed case is heard under is NOT DERIVED here"*), `::_eff_carry`; `state/gate.py:272-275` (`UNDECLARED_DISPOSAL = "oblige"`, `DISPOSABLE_KINDS`), `:378` (`seat_faction`); `world_q.judging_set`'s recorded gap (`:675-677`); INT §G.4 missing link (1); R4.
- ADVANCES: R-04 (contributor): a case is heard under a type.
- INSTRUCTION:
  1. `engine/season/rosters.yaml: case_rows` (ordered; the six rows of RD §C.6, each `# [ASSUMPTION; Jordan to correct]`) with a closed `when` roster `case_when` (`authority`, `matter`, `bench`, `seat_at_least`); `engine/season/data/rosters.py::CASE_ROWS`, refusing an unknown `when` key, a `row` that is not an arrangement id, an `authority` outside `AUTHORITIES`, a `seat_at_least` outside `RUNG_KINDS`, and a table whose last row has a non-empty `when` (there must be a row for every case).
  2. `engine/season/queries/world_q.py::row_for_case(w, seat: str, matter: Optional[str]) -> str`: the first `CASE_ROWS` row whose `when` holds and whose arrangement row has `disposes` in `DISPOSABLE_KINDS` and `venue_min_rank` at or below the kind of the seat's rung: `authority` = `AUTHORITY_BY_FACTION.get(seat_faction(w, seat), "polity")`; `matter` = `person` for an id in `w.persons`, `proposition` for one in `w.propositions`, `record` for one in `w.records`; `bench` = `one` or `several` by `len(judging_set(w, <the seat's rung>, matter))`; `seat_at_least` by `RUNG_KINDS.index`.
  3. `_eff_open_case`: where the act declares no arrangement, `arrangement = row_for_case(w, a.via, matter)`; `_eff_carry`: the same with the room's seat (`_seat_rung`'s owner). A declared arrangement is kept as declared. The two docstring paragraphs that record the gap say it is closed here.
  4. `hole_register.yaml`: one row for `case_rows` (graded `assumption`: which case goes where is content); H-80's and `judging_set`'s notes re-pointed.
- WHERE: `engine/season/rosters.yaml` (`case_rows`, `case_when`); `engine/season/data/rosters.py`; `engine/season/queries/world_q.py` (`row_for_case`); `engine/season/loop/effects_information.py` (`_eff_open_case`, `_eff_carry`); `engine/season/hole_register.yaml`; `engine/season/tests/test_sc_proceeding_host.py`.
- TESTS: written first and read red: `test_every_computed_case_names_a_row` (seeds 0 to 2, one season: every docket item `open_case` or `carry` wrote has an `arrangement` in `ARRANGEMENTS`; `assert checked >= 1` per seed); `test_a_church_seat_opening_on_a_person_names_the_inquisition_hearing` (hand-built); `test_no_row_is_named_that_determine_would_decline` (for every seat and matter class of a built realm the named row's `disposes` is disposable); `test_a_declared_arrangement_is_kept`.
- FALSIFIER and CONTROL: a computed docket item with `arrangement: None`; a named row whose `disposes` `_eff_determine` declines (a wedge). Control: with `case_rows` cut to its last row, every determination disposes what it disposed before (`oblige`, the same edge id: `_disposal`'s `UNDECLARED_DISPOSAL` branch is the `oblige` branch), read as the seed-0 Tenure list equal to B24p.14's; `aperture 1 0`'s `open_case` executed count unchanged.
- GATE: `python -m pytest engine/season/tests/test_sc_proceeding_host.py engine/season/tests/test_arrangements.py -q` → pass; `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 1 0` → `open_case` executed equal to the before-reading; the count of docket items by row at seeds 0, 1, 2, quoted in the commit body; the seed-0 hash → moved (declared).
- HASH MOVERS: every world in which `open_case` or `carry` executes (the item's `arrangement` gains a value; where the row is not `arbitration`, what `determine` disposes changes). Declared; B24p.99.
- EXPECTED RED UNTIL: B24p.99 (the realm pins).
- DEPENDS ON: V12 B24p.01 (`AUTHORITY_BY_FACTION`), .03 (the rows); EXISTS-IN-TREE `state/gate.py::seat_faction`, `::DISPOSABLE_KINDS`, `world_q.judging_set`, `_eff_open_case`, `_eff_carry`.
- GLOSSARY: row *proceeding type*: "a computed case names its row by `rosters.yaml: case_rows`".
- IDS: H block slot 49.
- COST and TIER: small build; `sonnet`, `high`; `opus` reads the by-row counts.
- LANDS IT: B24p's producer; `Item: B24p.15`, `[skip ci]`.

### B24p.16 — the verb rows say how they proceed · RD §C.6 items 1–2, §D.1, §D.3, §D.4 · BUILD · HASH EQUAL
- SOURCE: RD §D.1 (the routing), §D.3 (the cells), §D.4 (what of B05.24 and B05.25 stays), §C.6 items 1 and 2; B05.25 (`_check_governing_attributes`, the three kinds); rulings R3, R6, R7.
- ADVANCES: none at this commit (the cell is read at B24p.19); R3's routing is data.
- INSTRUCTION:
  1. `engine/season/data/verbs.py`: `_VERB_ROW_KEYS` gains `proceeds`; `VerbRow` gains `proceeds: tuple = ()` (a tuple of `(when, row, form, move)` entries; a single mapping in the file is read as one entry with an empty `when`); NEW `_check_proceeds(rows, prizes)`, called from `_load_verb_table` after `_check_governing_attributes`, raising `Unspecified` and naming every row that: carries `proceeds` together with `brute`; names a `row` that is neither an arrangement id nor `docket`; names a `form` outside `full`, `abridged`; names a `move` that is not a `PROCEEDING_MOVES` member with `draw: true`; uses a `when` key outside `hearer`, `docketed`; has a list whose last entry's `when` is not empty; or carries `proceeds` on a row whose prize row names `social_contest.proceeding` in neither `proceeding_entry` nor `module_entry`. `_check_governing_attributes`'s kind rule reads: a row is `brute`, or names `governing`, or names `proceeds`, or has a prize of `person_inputs: own`; a row naming both `governing` and `proceeds` is admitted here and refused from B24p.19, which deletes the six rows' `governing` cells in the commit that stops reading them (so the single roll has its pool at every commit before the flip).
  2. `engine/season/rosters.yaml: contest_subsystems.prizes`: `a standing`, `a proposition`, `a matter` gain `proceeding_entry: "social_contest.proceeding"` (RD §D.3); `engine/season/manifest/registry.py::check_contest_prizes` refuses a `proceeding_entry` no composition row declares, as it refuses `module_entry`.
  3. `engine/season/verb_table.yaml`: on `argue`, `tell`, `lie`, `speak`, `interrogate`: write `proceeds:` as RD §D.1 gives it (`determine`'s cell is B24.08's, with its prize), beside B05.25's interim `governing:` and `opposed_attribute:` cells, which stay until B24p.19. `capability:` and `difficulty:` stay.
  4. `engine/season/queries/world_q.py::proceeding_row(w, act) -> tuple`: the first entry of the verb row's `proceeds` whose `when` holds (`hearer`: the addressed person's `is_cohort`; `docketed`: `bool(docketed(w, subject))`); `row: docket` → `ARRANGEMENTS[item["arrangement"]]` of the docketed matter's item; `form: abridged` → `abridged(row, move)`; returns `(row dict, form, move)`.
  5. `registers/editorial_ledger_sc.jsonl`: one `ED-SC` row from `references/id_reservations.yaml` `next_free` (allocate, bump, co-commit) recording R1 to R6 as the rulings this batch builds and the one sentence of RD §D.4 that amends B05.24's rule.
- WHERE: `engine/season/data/verbs.py`; `engine/season/rosters.yaml`; `engine/season/manifest/registry.py`; `engine/season/verb_table.yaml`; `engine/season/queries/world_q.py` (`proceeding_row`); `registers/editorial_ledger_sc.jsonl`; `references/id_reservations.yaml`; `engine/season/tests/test_sc_proceeding_host.py`; `engine/season/tests/test_verb_governing_attributes.py`.
- TESTS: written first and read red: `test_a_brute_row_with_proceeds_is_refused` (planted); `test_five_rows_proceed_and_name_a_loadable_row`; `test_argue_to_a_cohort_proceeds_as_a_rally`; `test_speak_proceeds_abridged_under_the_dockets_row`. `test_verb_governing_attributes.py::test_every_verb_row_names_its_attributes_or_its_authority_or_its_subsystem` is re-pointed to four kinds and stays at `checked == len(VERB_TABLE)`.
- FALSIFIER and CONTROL: a `proceeds:` cell naming a row that does not load; a brute row given one. Control: nothing dispatches on `proceeds` yet and `governing` still pools the six rows: the seed-0 hash equals B24p.15's.
- GATE: `python -m pytest engine/season/tests/test_sc_proceeding_host.py engine/season/tests/test_verb_governing_attributes.py -q` → pass; `python -c "import engine.season.data.verbs"` → exit 0; `python tools/validate_ed_citations.py` → exit 0.
- HASH MOVERS: none.
- DEPENDS ON: V12 B24p.14; V12 Batch B05-one-roll (B05.25's loader and cells); EXISTS-IN-TREE `data/verbs.py::_load_verb_table`, `manifest/registry.py::check_contest_prizes`, `world_q.docketed`.
- GLOSSARY: *governing attribute*'s row gains: "a verb that opens a proceeding names none"; new row *abridged proceeding* ("one speech weighed by the room it is made in, with no ballot: a telling, a lie, a speech at a sitting").
- IDS: ED-SC 1.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B24p's producer; `Item: B24p.16`, `[skip ci]`.

### B24p.17 — `pairs proceeding` · RD §B (the readings), INT E-18 · BUILD · HASH EQUAL
- SOURCE: `engine/season/harness/pairs.py` (B01a.04: `social_pairs` `:147-164`, `_read`, `curve`); INT E-18 (*"a redesign with exchanges needs `social_pairs` to call the module's new entry rather than `roll`"*); R8 (curves over generated populations, very high iterations); B01a.05.
- ADVANCES: none; the instrument every role reading of this batch and of B98 uses.
- INSTRUCTION: `engine/season/harness/pairs.py`:
  1. The `contest` argument gains `proceeding`, with `--type <arrangement id>` (default `conversation`), `--form full|abridged` (default `abridged`), `--move <move id>` (default `argue`), `--side for|against|decider` (whose sheet the difference is taken on; default `for`), `--room none|gallery|crowd` (how many onlookers the instrument seats: 0, 2, a cohort of weight 30).
  2. `proceeding_pairs(seed, n, type_id, form, move, room, plant=None)`: the world and sheets as `social_pairs` (`_world`, `_sheets`, `_seat`); a third person `p_high` drawn the same way is the decider for a row that has one; `sigma.proceeding_input(...)` with the row (or `abridged(row, move)`); the entry found by its composition row (`composition.ROLES["social_contest.proceeding"]["target"]`); `rng = draw(f"pair{i}", f"pairs:proceeding:{type_id}:{form}")`; `margin, veto = sigma.act_margin(outcome, inp.type)`; the band by `degree_of` (a veto demotes, as the fold does). Yields `ProceedingPair(i, a, b, c, read, band, outcome)` where `read` is the speech pool less the opposition, as `social_pairs`'s.
  3. `proceeding_report`: `y` the share of carried bands; with `--diff all` one SLOPE line per key, for the side `--side` names (`a[k] - b[k]` for `for` and `against`; `c[k]` for `decider`); and three further lines read off the outcomes: `EXCHANGES` (the mean count), `ENDS` (the share of each `proceeding_ends` member), `MARKS` (marks per sitting).
  4. `DEFAULT_N["proceeding"] = 200000` for the abridged form and `40000` for the full form `[ASSUMPTION: under the two minutes a contest the instrument allows — basis: `social`'s 0.25 s per 1,000 pairs and nine normals an exchange; re-measured and written in the docstring]`.
- WHERE: `engine/season/harness/pairs.py`; `engine/season/tests/test_pairs.py`.
- TESTS: in `test_pairs.py`, written first and read red: `test_proceeding_pairs_are_reproducible` (two runs, the same lists); `test_a_planted_speaker_of_higher_reason_carries_more_often` (the `plant` hook: `a` at Reason 6, `b`'s copy at Reason 2, else equal, 20,000 pairs, at the shipped settings in the test's own fixtures); `test_the_instrument_reads_an_end_and_an_exchange_count`.
- FALSIFIER and CONTROL: the instrument calling `roll` instead of the entry (`ENDS` would be empty); a curve that is one point. Control: `pairs social --verb examine` prints what it printed at B24p.16's tree (the single roll's instrument is untouched).
- GATE: `python -m pytest engine/season/tests/test_pairs.py -q` → pass; `PYTHONHASHSEED=0 python -m engine.season.harness.pairs proceeding --type conversation --form abridged --n 20000 --seed 0 --diff all` → ten SLOPE lines; its wall time quoted.
- HASH MOVERS: none (an instrument).
- DEPENDS ON: V12 B24p.13, .14; EXISTS-IN-TREE `harness/pairs.py`, `probes.tiny_world` (`p_low`, `p_mid`, `p_high`).
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B24p's producer; `Item: B24p.17`, `[skip ci]`.

### B24p.18 — each role moves only its own operand; the two profiles · RD §B.8, §B.5 · BUILD · HASH EQUAL
- SOURCE: RD §B.8 (the table: no two roles share an operand), §B.5's `test_the_two_profiles`; R2 (*"in the manner that I specified"*); AR-49, AR-50; B24.41 item (6).
- ADVANCES: none; R2's falsifier.
- INSTRUCTION: `engine/season/tests/test_sc_roles.py`, two tests on the module with hand-built inputs and the shipped settings in the tests' own fixtures (no code edit):
  1. `test_each_role_moves_only_its_own_operand`: for each of the six attributes, two speakers equal but for that attribute (2 and 6) run one scripted exchange of `argue` on a fixed ground, under a `routine` standard with a gallery, a standing pull of 1.0, two proofs held, a known `rank_gap` of 2.0 and one mark planted, over 2,000 keys. The operands are named: pool before `heard`; `heard`; each entry of `Exchange.levels`; each entry of `Exchange.terms`; `on_topic`. Asserted with `==` on the per-key lists: Focus changes `on_topic` and `terms["off_topic"]` and nothing else; Reason changes the pool, `levels["proofs"]` and `terms["rank_gap"]`; Attunement changes nothing (the choice is scripted); Presence changes `heard` and `levels["delivery"]`; Grace changes `terms["standard"]`, `levels["respect"]` and `levels["marks"]`; Will changes the net sigma through the shield, `terms["reception"]` where the room is hostile, and nothing else on his own speech. A second pass with the choice free shows Attunement changing the chosen ground's distribution alone. `assert checked == 6 * 2000`.
  2. `test_the_two_profiles` (RD §B.5): 20,000 keyed two-sided sittings; the Presence 6, Grace 2 speaker is carried more often AND ends with the lower `esteem` than the Presence 2, Grace 6 speaker, each difference over four standard errors.
- WHERE: `engine/season/tests/test_sc_roles.py`.
- TESTS: the two above, written before any setting leaves control and read green on the module as B24p.12 left it (they set their own fixtures); read red once, by a planted fault (Presence added to the pool), reverted.
- FALSIFIER and CONTROL: one attribute's change moving another role's operand; the planted fault not reddening the test. Control: every setting at control: the six pairs of speakers give identical exchanges but for the pool under Reason.
- GATE: `python -m pytest engine/season/tests/test_sc_roles.py -q` → every role test passes, `checked` counts asserted; the planted fault's red reading named in the commit body.
- HASH MOVERS: none.
- DEPENDS ON: V12 B24p.12.
- GLOSSARY: none.
- COST and TIER: small build (tests); `sonnet`, `high`.
- LANDS IT: B24p's producer; `Item: B24p.18`, `[skip ci]`.

*(B24p.21 is a READING position, taken between B24p.18 and B24p.19: no item body; its text is reading R1 in the Readings block below.)*

### B24p.19 — the influence verbs call the proceeding · RD §D.1, §A.6 · BUILD · HASH MOVER(behaviour)
- SOURCE: RD §D.1, §D.2, §D.3 (the second entry on the prize row), §A.6 (the abridged form is the same entry); `seam/contest.py::contest` (`:182`), `loop/resolve.py::_contest` (`:766-874`); rulings R3, R6.
- ADVANCES: R-09.c (re-read); R3 and R6 execute.
- INSTRUCTION:
  1. `engine/season/seam/contest.py::contest`: where the act's verb row carries `proceeds` and the prize row a `proceeding_entry`, resolve `world_q.proceeding_row(w, act)` and pass it to the provider as `proceeds=`; the provider is unchanged (`@provider("contest", "social_contest")`), the entry is the prize row's `proceeding_entry`, else its `module_entry`. Every other act takes today's path. No verb is named: the branch is the row's cell.
  2. `engine/season/loop/resolve.py::_contest`: pass the act's `subject` operand as `topic` where the row's opponent operand is not `subject`, and the docket matter where it is (INT C.1); the act's generator is unchanged (`"roll:<prize>:<act id>"`).
  3. `engine/season/verb_table.yaml`: on the five rows of B24p.16, delete `governing:` and `opposed_attribute:` (RD §D.3); `data/verbs.py::_check_proceeds` now refuses a row carrying `proceeds` with either. `engine/season/seam/wrappers/pool.py::faculty`: a row with `proceeds` is no longer pooled here (the builder reads the person); `faculty` raises `Forbidden` naming the verb if one reaches it, as it does for a `brute` row (B05.25).
  4. The fold reads `settled`'s place: `ladder.degree_of` on the adapter's `net`, `ob` and `veto` (the ladder takes the minimum on a veto, `04` §C.5).
- WHERE: `engine/season/seam/contest.py`; `engine/season/loop/resolve.py` (`_contest`); `engine/season/verb_table.yaml` (six rows); `engine/season/data/verbs.py` (`_check_proceeds`); `engine/season/seam/wrappers/pool.py` (`faculty`); `engine/season/tests/test_sc_proceeding_host.py`; `engine/season/tests/test_verb_governing_attributes.py`; the pool-pinning tests the commit names.
- TESTS: written first and read red: `test_a_row_with_proceeds_and_governing_is_refused` (planted); `test_a_tell_resolves_through_the_proceeding_entry_as_one_exchange` (a hand-built act: the Event's record names `social_contest.proceeding`, one exchange, no ballot); `test_an_argue_resolves_as_exchanges_and_the_hearers_ballot`; `test_an_arrest_still_resolves_on_the_single_roll` (control: `social_contest.roll`); `test_the_same_seed_twice_gives_the_same_season` (seed 0, one season, twice: equal hashes).
- FALSIFIER and CONTROL: an influence verb still on `social_contest.roll`; a non-influence verb (`arrest`, `examine`, `research`, `surveil`) moved. Control: every setting at control, so what moves is named and nothing else: the pool's attribute (Reason plus rank where B05.25 read a mean), the stream (the exchange's fixed draws where one normal was taken), and `argue`'s second draw (the hearer's ballot); `pairs social --verb examine` equal to B24p.17's reading.
- GATE: `python -m pytest engine/season/tests/test_sc_proceeding_host.py engine/season/tests/test_sc01_provider.py -q` → pass; `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 2 0` with the `ENGINES` block → `social_contest.proceeding` entered, count quoted; the per-verb `DEGREES RESOLVED` lines for `tell`, `lie`, `speak`, `argue`, `interrogate` before (`reading @<B24p.18 sha>`) and after; the seed-0 hash → moved, run twice equal.
- HASH MOVERS: every world in which one of the five verbs resolves. Declared; B24p.99.
- EXPECTED RED UNTIL: B24p.99 (the realm pins; each pool-pinning test named in the commit).
- DEPENDS ON: V12 B24p.16, reading R1 (B24p.21: the before-curves must be on file first); EXISTS-IN-TREE `seam/contest.py::contest`, `loop/resolve.py::_contest`, `loop/sides.py::sides_of`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`; `opus` reads the before and after `DEGREES RESOLVED`.
- LANDS IT: B24p's producer; `Item: B24p.19`, `[skip ci]`.

### B24p.20 — the sitting is written; each hearer is moved for himself; the topic reaches the effect · RD §A.2, §A.7 · BUILD · HASH MOVER(behaviour)
- SOURCE: RD §A.2 (the state table: the Event's `ending`), §A.7; `state/carriers.py:296-313` (`Event.ending`); B05.18 (SC-P1: the social roll's record on its Event); B24.14 (the case-file copy, B24's); `loop/effects_information.py::_eff_argue` (`:648-675`), `person_q.argued_pursuits` (`:723`); A-81; INT E-10, E-11.
- ADVANCES: R-04 (contributor): a proceeding leaves a record; a crowd is moved hearer by hearer.
- INSTRUCTION:
  1. `engine/season/loop/resolve.py::_fold`: for an act resolved through the proceeding, the Event's `ending` is a tuple of plain values built from the outcome: `("proceeding", row id, form, ended, round(track, 3))`, then per side `(speaker id, marks, strikes, round(esteem, 3))`, then per exchange `(n, mover, move, ground, on_topic, round(margin, 3), marked)`, then per verdict `(id, band)` graded by `ladder.degree_of`. Milli-rounded reals, B05.01's unit, so the encoding is stable. SC-P1's fields for a single roll are unchanged.
  2. `engine/season/queries/world_q.py`: readers over that tuple, the one owner of its shape: `ending_exchanges(event)`, `ending_marks(event, person)`, `ending_verdicts(event)`. `person_q.strain_carried`'s host caller (B24p.13) counts marks through `ending_marks`.
  3. `loop/effects_information.py::_eff_argue`: under a `hearers` disposal the effect runs once per verdict, on that hearer, at that hearer's own band (today it runs once, on `to`, at the act's band): `argued_pursuits(hearer, arguer, degree, gain)` unchanged. The act's own band (B24p.14's weight-mean margin) chooses the row's `emits`. `_eff_argue` receives `topic` on the resolution and passes it on unused `[ASSUMPTION: which pursuits a topic bears on is B27.05's edit (`argued_pursuits` takes a number of steps and `_eff_argue` chooses who moves); this item delivers the operand it needs]`.
  4. `write_matrix.yaml`: no new row (`ending` is an Event field; `(Person, pursuits)` is `argue`'s existing write, now possibly on several hearers: the row's `by:` already admits the act).
- WHERE: `engine/season/loop/resolve.py` (`_fold`); `engine/season/queries/world_q.py` (three readers); `engine/season/loop/effects_information.py` (`_eff_argue`); `engine/season/tests/test_sc_proceeding_host.py`.
- TESTS: written first and read red: `test_a_proceedings_event_carries_its_exchanges_and_verdicts`; `test_a_rally_moves_each_carried_hearer_and_no_other` (a hand-built address to four hearers with planted ballots: the carried two have moved pursuits, the other two have not); `test_a_mark_is_counted_into_the_strain_he_carries_next` (a marked speaker's next `Speaker.strain` is above 0 at the shipped `blow_gain` and 0 at control); `test_every_end_of_a_proceeding_writes_an_ending` (A-81: each of the six ends leaves a non-empty `ending`).
- FALSIFIER and CONTROL: an exchange on the Event that the outcome did not hold, or the reverse; a hearer moved who was not carried. Control: a proceeding of one exchange under `disposal: exchange` writes what SC-P1 wrote plus the `("proceeding", …)` head.
- GATE: `python -m pytest engine/season/tests/test_sc_proceeding_host.py -q` → pass; `python -m engine.season.harness.register --check` → counts not risen; the seed-0 hash → moved (declared; `ending` folds into `World.content_hash` where non-empty).
- HASH MOVERS: every world in which a proceeding resolves (encoding: the `ending`); behaviour where an `argue` addresses a cohort. Declared; B24p.99.
- EXPECTED RED UNTIL: B24p.99.
- DEPENDS ON: V12 B24p.19; V12 Batch B05 (B05.18: SC-P1's carrier); EXISTS-IN-TREE `Event.ending`, `_eff_argue`, `person_q.argued_pursuits`.
- GLOSSARY: row *ending (of a proceeding)*: owner `world_q.ending_exchanges` and its two siblings.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B24p's producer; `Item: B24p.20`, `[skip ci]`.

### B24p.22 — a reading is kept by the one who read · RD §B.3 ("The reading is kept") · BUILD · HASH EQUAL
- SOURCE: RD §B.3; ED-IN-0350 (a choice-side input); B24.29 (the precedent: a drawn reading deposited in the viewer's own ledger, sometimes wrong, never revealed); `loop/witness.py`; AX-2; N12.
- ADVANCES: none at control; Attunement's choice-side half has a carrier.
- INSTRUCTION:
  1. `ProceedingOutcome` gains nothing: each speaker's last reading is already `state.sides[i].read`.
  2. `engine/season/loop/witness.py`: for an Event whose `ending` is a proceeding's and with `reading_kept` on, each speaker receives, in his OWN ledger, one claim per ground about the other speaker (or, in a one-speaker type, none): `Claim(subject=<other>, predicate="moved_by:" + ground, value=round(believed, 1), confidence=acc, source=<the act>)` through the ordinary deposit path (the eviction comparator applies). The values are the believed ones the module returned; the witness step reads no true disposition.
  3. `engine/season/seam/wrappers/sigma.py::believed_chance` (B24p.14 step 5) reads those claims for the addressed person's `moved_by` (the latest, then the most confident), so a person who has read someone prices arguing with him on what he read.
  4. `data/fixtures.py`: `reading_kept` stays `False` (B24p.04); the item builds the path behind it.
- WHERE: `engine/season/loop/witness.py`; `engine/season/seam/wrappers/sigma.py` (`believed_chance`); `engine/season/tests/test_sc_proceeding_host.py`.
- TESTS: written first and read red, with `reading_kept` on in the test's fixtures: `test_a_reading_is_deposited_in_the_readers_own_ledger_only`; `test_a_kept_reading_can_be_wrong_at_every_attunement` (400 keys at Attunement 2 and 6: the share of deposits naming the other's true best ground is strictly between 0.25 and 1 at both, and higher at 6; `assert checked >= 400`); `test_a_kept_reading_changes_the_believed_odds_of_arguing_with_him`.
- FALSIFIER and CONTROL: a deposit that shows the true vector with certainty, or lands in anyone else's ledger. Control: `reading_kept` off: no claim is deposited and the seed-0 hash equals B24p.20's.
- GATE: `python -m pytest engine/season/tests/test_sc_proceeding_host.py -q` → pass; the seed-0 hash → equal to B24p.20's.
- HASH MOVERS: none at control; declared (ledger growth) when B98 turns it on.
- DEPENDS ON: V12 B24p.20; EXISTS-IN-TREE `loop/witness.py` (the deposit path), `state/carriers.py::Claim`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B24p's producer; `Item: B24p.22`, `[skip ci]`.

### B24p.23 — the six roles on · RD §B (the shipped columns), §C.3, §C.5 · BUILD · HASH MOVER(behaviour)
- SOURCE: RD §B.1 to §B.6 (each table's shipped column), §C.3 (`standard` per row), §C.5 (the audience table); R1, R2, R8; A-79 (an even argument on a routine matter carries about one time in four); `proposals/13_SC_calibration.md` C1 to C8 (B05.22's test); B01a.05.
- ADVANCES: R-09.b (the obstacle and the pool differ person to person); R1 and R2 execute in the realm.
- INSTRUCTION, one commit:
  1. `engine/season/data/fixtures.py`: every setting of B24p.04 to RD §B's shipped value, except `reading_kept`, `presumption_level` and `strike_level` (left for B98); each line's `SHIPPED` comment moved.
  2. `engine/season/arrangements.yaml`: the `audience_kinds` rows to RD §C.5's table; `standard:` on the thirteen rows to RD §C.3's column.
  3. The centre, read and restored. Take `pairs proceeding --type conversation --form abridged --diff read --seed 0 1 2` at its default `--n` and read the middle bin (`read` = 0): A-79's 25 % carried is its target, within the bin's two standard errors. The roles are zero-centred on the attribute mid-point by construction (delivery, respect, resist) or one-sided by design (the standard, the off-topic term, the shield, a best ground found more often than a worst): the one-sided ones move the centre. It is brought back by ONE cell, `conversation`'s verb rows' `difficulty:` level through `difficulty_ob` (B05.14's table), never by a role's own setting `[ASSUMPTION: the centre is held by the difficulty table — basis: B05.23 sets A-79's centre there; a role's setting is sized by its own reading]`. If no level of the table lands the bin, the item STOPS and reports the reading (the table is B05's, and B98's to re-sweep).
  4. B05.22's `test_sc_calibration_targets.py`: each C-row that reads a social roll between persons is re-pointed to the abridged proceeding under `conversation` and read as the curve's middle bin; the rows and their re-read values are listed in the commit body. A row that no longer has a subject (it tested the averaged pool) is deleted with its subject and named.
- WHERE: `engine/season/data/fixtures.py`; `engine/season/arrangements.yaml`; `engine/season/verb_table.yaml` (a `difficulty:` cell, if step 3 moves one); `engine/season/tests/test_sc_calibration_targets.py`.
- TESTS: none new; `test_sc_roles.py` green on the shipped fixtures (its tests set the same values); `test_sc_calibration_targets.py` green as re-pointed.
- FALSIFIER and CONTROL: a role whose SLOPE reads within two standard errors of 0 in all five type readings of the BATCH GATE (then its mechanism is inert at the shipped values: STOP, the setting is re-sized and the reading re-taken once); a body or perception key reading outside ±0.002; a bin whose DOMINANT share exceeds 0.90. Control: every setting restored to control in a scratch run reproduces B24p.22's seed-0 hash.
- GATE: the five `pairs proceeding` readings of the BATCH GATE, each quoted beside reading R1 (the control arm): per key the SLOPE with its standard error, the SPREAD, MONOTONE, DOMINANT, `EXCHANGES`, `ENDS`, `MARKS`; expected `[ASSUMPTION; Jordan to correct]`, from the scratch probe of RD §B: in the abridged conversation, Reason and Presence each between 0.04 and 0.09 per point, Grace between 0.01 and 0.04, Focus, Attunement and Will each above 0.003, the hearer's Will between −0.06 and −0.02; before a crowd Presence above Reason; before a bench with proofs Reason above Presence; in the full conversation between 5 % and 30 % of sittings end `yielded` or `broken`. A reading outside a bound is reported, not tuned to (D-18: what the ladder cannot settle goes to Jordan). `python -m pytest engine/season/tests/test_sc_roles.py engine/season/tests/test_sc_calibration_targets.py -q` → pass; the seed-0 hash → moved.
- HASH MOVERS: every world in which a proceeding resolves. Declared; B24p.99.
- EXPECTED RED UNTIL: B24p.99.
- DEPENDS ON: V12 B24p.18, .22; reading R1; V12 Batch B05 (B05.22, B05.23: the calibration test and the difficulty table).
- GLOSSARY: none.
- COST and TIER: calibration; `sonnet`, `high` runs the readings; `opus` reads each role's curve against its bound and decides a STOP.
- LANDS IT: B24p's producer; `Item: B24p.23`, `[skip ci]`.

## Readings (B24p)

Reading R1 (B24p.21): on B24p.18's tree, every setting at control, `PYTHONHASHSEED=0 python -m engine.season.harness.pairs proceeding --diff all --seed 0 1 2` for `--type conversation --form abridged`, `--type conversation --form full`, `--type rally --room crowd`, `--type legal_trial`, `--type questioning`, at the instrument's defaults: per reading the ten SLOPE lines for `--side for`, the two for `--side against` on Will and Grace, SPREAD, MONOTONE, DOMINANT, `EXCHANGES`, `ENDS`, `MARKS`, with the tree's SHA. Expected at control: Reason alone reads a slope (the pool); the other nine keys within ±0.002. Written here by the producer, copied into B24p.23's and B24p.99's commit bodies, and deleted with the block at the expunge.

### B24p.99 — re-pin and close readings · the batch's one re-pin (E-1) · BUILD · HASH MOVER (the re-pin)
- SOURCE: `V12_STRUCTURE_part4.md` E-1, E-2; Jordan, R10: *"we can re-pin after it's been built"*.
- ADVANCES: the batch's readings on file.
- INSTRUCTION: (1) re-record, once, the realm pins in `engine/season/tests/_realm_goldens.py` at seeds 0 to 2 and every seeded golden the movers reached, against the base this batch rebased on in S12 (`reading @<sha>`); the commit says "re-pin: behaviour (B24p.15 the row a computed case names; B24p.19 the proceeding entry; B24p.20 the ending and the hearers; B24p.23 the six roles on)" and names each pin old → new. (2) Write the BATCH GATE's readings into the commit body: the five `pairs proceeding` readings before (R1) and after, `aperture 2 s` for s = 0, 1, 2, the `DEGREES RESOLVED` lines, `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the batch's wall time. (3) Append the batch's 49 register rows from its H block once, in merge order, if the items did not each write their own. (4) `registers/handoffs/HANDOFF_SC.md`: the Open row closed, with a pointer to B24's block.
- WHERE: `engine/season/tests/_realm_goldens.py`; the pinned digests the items name; `engine/season/hole_register.yaml` (if step 3 applies); `registers/handoffs/HANDOFF_SC.md`.
- TESTS: the full gates the BATCH GATE names, once (CLAUDE.md §0.4).
- FALSIFIER and CONTROL: a pin moved that no item declared; a behaviour tally moved where every item said EQUAL (B24p.01 to .14, .16 to .18, .22). Control: B24p.14's seed-0 hash equal to B24p.01's (the EQUAL items moved nothing).
- GATE: the BATCH GATE, read once on this commit's tree.
- HASH MOVERS: the re-pin itself.
- DEPENDS ON: B24p.01 to B24p.23.
- GLOSSARY: the close reads every glossary row the items named against the code.
- COST and TIER: reading; `sonnet`, `high` runs; the close's terminal critique `opus`.
- LANDS IT: B24p's producer; `Item: B24p.99`, the batch's last `Item:` commit, without `[skip ci]`.

| STOP. Batch B24p-sc-proceeding closes here |
