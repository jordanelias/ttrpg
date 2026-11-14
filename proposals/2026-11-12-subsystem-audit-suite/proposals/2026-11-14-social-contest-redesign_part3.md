# SC · DICE — the social contest redesigned, part 3: the build items (the batch block; B24p.01 to B24p.12)

## Status: PROPOSED (the third part of `2026-11-14-social-contest-redesign.md`; read that file's head first: its markers, short names and status sentence apply here; reference under CLAUDE.md §0.05, nothing reads it at runtime)

---

## E. The build, in the plan's item form

Written in workplan v12's forms (`### B05.09`, wp `part8.md:252-286`; `### B28.35`, wp `part35_cont.md:329-348`), against
the tree as B00 to B07 leave it. Where a symbol is named that does not exist at `1257a4a`, the item says which batch makes
it. A path under `engine/`, `modules/`, `tools/`, `references/`, `registers/`, `tests/` is the repository's;
`engine/season/` is dropped where the context is plain. §A to §D of this proposal are cited as RD §A to RD §D. Every
INSTRUCTION is complete in itself for the code it names; the formulas it cites are RD §B's, copied where they are short.

### E.0 The batch block

## Batch B24p-sc-proceeding · lane SC · wave W12 · step S12 · HASH MOVER, one re-pin
INVOCATION: /methodology-execute Batch B24p-sc-proceeding
IN-FLIGHT ROW: registers/handoffs/HANDOFF_SC.md, Open table
GATE: Batch B00-ids @c3418a6a160fc6a17e5a8bf45112a0e55699a695
GATE: Batch B01-laneA @cfd9aefb049c2fe49b55c7ada1b0b624919af23d
GATE: Batch B01a-attributes-generated (the drawn attributes, `attr.spirit.will` (B01a.06, landed `1257a4a`) and `harness/pairs.py`; every reading this batch takes on a contest between persons is a curve over generated pairs, never one even-matchup number)
GATE: Batch B02-tests
GATE: Batch B03-hygiene
GATE: Batch B04-capability-home
GATE: Batch B05-one-roll
GATE: Batch B06-keyed-draw
GATE: Batch B07-task-draw
HASH READING: `PYTHONHASHSEED=0 python -c "import sys; from engine.season.boot.realm import build_realm; from engine.season.harness.populated import run; s, k = int(sys.argv[1]), int(sys.argv[2]); w = build_realm(s); run(k, s, w=w); print(w.content_hash())" <s> <k>` → the realm content hash at seed `<s>` after `<k>` seasons: `<k>` = 1 unless the gate names two (never more before B99, D-17); per item `<s>` = 0, at `.99` `<s>` = 0, 1, 2; each value quoted `reading @<sha>`.
REQUIREMENT: none of its own. Re-read R-09.c → `python -m engine.season.harness.corpus_run --seasons 2`'s `DEGREES RESOLVED BY VERB` block and R-08.b → `python -m pytest engine/season/tests -q -k test_u4_the_choice_is_sampling`, each unchanged in verdict from B07's close; it supplies the entry R-04.c3's hearing runs on (B24). No `status:` is edited (A-114).
BATCH GATE (read once, on the closing tree, B24p.99's commit; `PYTHONHASHSEED=0` on every seeded command; no command past two seasons):
  `python -m pytest engine/season/tests/test_sc_proceeding_data.py engine/season/tests/test_sc_proceeding_module.py engine/season/tests/test_sc_roles.py engine/season/tests/test_sc_proceeding_host.py engine/season/tests/test_pairs.py engine/season/tests/test_social_contest_module.py engine/season/tests/test_sc01_provider.py engine/season/tests/test_arrangements.py engine/season/tests/test_verb_governing_attributes.py -q` → all pass;
  the six roles: `python -m engine.season.harness.pairs proceeding --type conversation --form abridged --diff all --seed 0 1 2` and the same for `--form full`, `--type rally`, `--type legal_trial`, `--type questioning` at the instrument's default `--n` → per type, one SLOPE line per attribute key and side, the curve's SPREAD, MONOTONE and DOMINANT, quoted before (the control arm, B24p.21's reading) and after (B24p.23); expected `[ASSUMPTION; Jordan to correct]`: on the speaker's side every one of the six social keys reads a SLOPE whose interval (two standard errors) excludes 0 in at least one of the five readings, the four body and perception keys read within ±0.002 in all five, and no bin's DOMINANT share exceeds 0.90;
  the variance rule: every reading above is a curve by difference bin; no single even-matchup number is quoted as a calibration (B01a.05);
  `python -m engine.season.harness.aperture 2 s`, s = 0, 1, 2, with the `ENGINES` block → `social_contest.proceeding` entered at least once at every seed, and the per-verb `DEGREES RESOLVED` lines for `tell`, `lie`, `speak`, `argue` quoted before and after;
  `python tools/export_composition.py --check`, `python tools/export_sim_params.py --check`, `python tools/ci_sim_fabrication_check.py`, `python tools/validate_ed_citations.py`, `python tools/freshness_gate.py` → exit 0 each;
  `python -m pytest tests/valoria/test_engine_does_not_import_systems.py -q` → pass (the module imports the dice engine and the record leaf only);
  `python -m engine.season.harness.register --check` → each check's violation count does not rise from the reading at the batch's opening (both quoted, `reading @<sha>`); `--requirements` → nine lines; `python tools/m1_acceptance.py --summary` → its verdict line, quoted;
  the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names, run once (CLAUDE.md §0.4);
  the glossary rows each item names, read against the code it landed; the close's commit body records the readings above with their trees and the batch's measured wall time.
RE-PIN: once, at B24p.99: the realm pins in `engine/season/tests/_realm_goldens.py` at seeds 0 to 2 and every seeded golden a moved `tell`, `lie`, `speak`, `argue`, `interrogate` or `open_case` reaches, against the base this batch rebased on in S12; the commit names each mover (B24p.15, .19, .20, .23) old → new and says "re-pin: the proceeding entry (R3, R6), the row a computed case names (R4), the six roles on (R1, R2)".
EXPECTED RED UNTIL B24p.99 (under `[skip ci]`): the realm and corpus pins from B24p.15 on; `engine/season/tests/test_go07_canonical_digest.py`; `engine/season/tests/test_season_weather.py`; every test that pins a pool or a band for `tell`, `lie`, `speak`, `argue` or `interrogate` (`git grep -ln "contest_input(" engine/season/tests` at B24p.19's open, each named in its commit).
IDS: ED-SC 1 (B24p.16's ledger row); H 49 (NUMBER rows: B24p.04's 48 settings and tables, B24p.15's `case_rows` note row).
DIALS AT CONTROL: every setting of B24p.04, from B24p.04 to B24p.22; set by B24p.23 to RD §B's shipped values, each `[ASSUMPTION; Jordan to correct]`; target: the BATCH GATE's role readings. Left at control past this batch, for B98: `reading_kept` (the deposit of a reading; target: B24p.22's falsifier), `presumption_level`, `strike_level` (targets: none stated → B98 writes each `BLOCKED (design: no target reading)` unless Jordan gives one).
UNDECIDED: (1) the batch sits at S12 and not S10 or S11, where its gates would let it: B09 runs alone at S10 (wp `part11_cont.md:43`) and B10 gates on B09 `[ASSUMPTION: B10 is not parallel-safe with an SC mover — basis: its edit set was not read]`; the other reading runs it beside B10 at S11 and saves no critical-path time (B24 waits on B10 and B11 anyway). (2) In S12 it merges before BA1 (BA1.13 writes verb cells B24p.16 replaces) and before B11, B15 and B21; the coordinator's order line gains it first. (3) B24p.14's believed odds return `None` where the believer holds no claim on the hearer's skill score, as today (INT E-13): pricing an unknown hearer is B10's or B28's, not this batch's. (4) `proceeding_moves` is created here and B24.03 adds to it; the other reading leaves B24.03 its own `hearing_moves` roster and makes two rosters of moves (refused: one roster, CLAUDE.md §8).
C(B24p-sc-proceeding): this proposal (five parts); the rulings file; `unified/U1_GLOSSARY.md` rows *proceeding*, *sitting*, *exchange*, *move*, *ground*, *decider*, *audience*, *rite*, *strain*, *mark*, *resolve*, *track*, *standard*;
  `modules/social_contest/roll.py`, NEW `modules/social_contest/proceeding.py`; `engine/dice_engine/sigma_leverage.py`, `draw.py` (B06), `fmath.py` (B06);
  `engine/season/queries/inputs.py`; `engine/season/queries/person_q.py`; `engine/season/queries/world_q.py` (`judging_set`, `reception`, `proofs`, `docketed`, `presence`, `place_of`); `engine/season/seam/wrappers/sigma.py`, `pool.py`, `_entry.py`; `engine/season/seam/contest.py`; `engine/season/loop/resolve.py` (`_contest`, `_fold`), `loop/sides.py`, `loop/effects_information.py` (`_eff_open_case`, `_eff_carry`, `_eff_argue`, `_docket_item`); `engine/season/state/carriers.py` (`Event.ending`); `engine/season/data/arrangements.py`, `rosters.py`, `verbs.py`, `fixtures.py`;
  `engine/season/arrangements.yaml`, `rosters.yaml`, `verb_table.yaml`, `hole_register.yaml`; `references/module_contracts.yaml`; `references/id_reservations.yaml`; `registers/editorial_ledger_sc.jsonl`; `registers/handoffs/HANDOFF_SC.md`;
  `engine/season/harness/pairs.py`, `aperture.py`, `probes.py`; the tests the items name; instruments: `pairs`, `aperture`, `register`, `tools/m1_acceptance.py`, `tools/tests_for_diff.py`, `tools/export_composition.py`, `tools/export_sim_params.py`, `tools/ci_sim_fabrication_check.py`;
  the closing SHAs of B04, B05, B06, B07; the permanent surface (CLAUDE.md, `CURRENT.md`, `HANDOFF.md`, `registers/handoffs/HANDOFF_SC.md`, the skill and `methodology-close`).
SERIAL EDGES: within the batch: .01 → .02 → .03 → .04 → .05 → .06 → .07 → .08 → .09 → .10 → .11 → .12 (the module, bottom up) → .13 → .14 → .15 → .16 → .17 → .18 → .21 (the control reading) → .19 → .20 → .22 → .23 → .99. With other batches, by file: `roll.py` B05 → B24p → B33; `sigma.py` B07 → B24p → B24; `queries/inputs.py` B05 → B24p → B24; `arrangements.yaml`, `data/arrangements.py` B05 → B24p → B24 → B24a → B27; `rosters.yaml`, `fixtures.py`, `verb_table.yaml` B07 → B24p → BA1 → B24; `harness/pairs.py` B01a → B24p; `references/module_contracts.yaml` B05 → B24p → B24. B24, B24a, B27, B28 and BA1.13 gate on this batch.
PARALLEL: S12 with B21-fa-governance (FA), B11-fi-readers (FI), B15-pc-calibration (PC), BA1-cast-content (IN). Hot files: `rosters.yaml`, `fixtures.py`, `verb_table.yaml`, `world_q.py` with B21 and B11 (different keys and functions); `verb_table.yaml` with BA1.13 (the same rows: serialised, B24p first). Every batch of S12 is a mover; B24p merges first and each later one rebases and re-pins once.
COST: small builds; producer `valoria-author` on `sonnet`, `high`, one per item; judgment nodes on `opus`: B24p.07's control equality, the role readings of B24p.21 and B24p.23, the re-pin's tallies; the close's terminal critique `opus`.
EST: 14 h [estimate: 0.4 h × 24 positions + 2.5 h for the close + 2 h for the `pairs` readings]

| pos | item | state | hash | gates on |
|---|---|---|---|---|
| B24p.01 | the rosters: grounds, moves, ends, authorities | BUILD | EQUAL | Batch B07 |
| B24p.02 | the proceeding's records | BUILD | EQUAL | B24p.01 |
| B24p.03 | the type rows: five keys, two disposals, rites, audience kinds, four rows | BUILD | EQUAL | B24p.01; Batch B05 |
| B24p.04 | the settings, at their controls | BUILD | EQUAL | B24p.03; Batch B00 |
| B24p.05 | the leverage sources and obstacle terms of the roles | BUILD | EQUAL | B24p.04; Batch B05 |
| B24p.06 | what moves a person, and the strain he carries, derived | BUILD | EQUAL | B24p.01 |
| B24p.07 | the speech draw: Reason, Presence, Grace and Will on one roll | BUILD | EQUAL | B24p.02, .04, .05; Batch B05, B06 |
| B24p.08 | the reading: Attunement | BUILD | EQUAL | B24p.07 |
| B24p.09 | the hold: Focus | BUILD | EQUAL | B24p.07 |
| B24p.10 | the moves' effects and the steadiness draw | BUILD | EQUAL | B24p.08, .09 |
| B24p.11 | the sitting: order, legal moves, the automatic policy, resolve, ends | BUILD | EQUAL | B24p.10 |
| B24p.12 | the close, the odds, and the composition row | BUILD | EQUAL | B24p.11; Batch B03 |
| B24p.13 | the host builder | BUILD | EQUAL | B24p.06, .12; Batch B07 |
| B24p.14 | the provider path and the believed odds | BUILD | EQUAL | B24p.13 |
| B24p.15 | every computed case names its row | BUILD | MOVER(behaviour) | B24p.03 |
| B24p.16 | the verb rows say how they proceed | BUILD | EQUAL | B24p.14; Batch B05 (B05.25) |
| B24p.17 | `pairs proceeding` | BUILD | EQUAL | B24p.13 |
| B24p.18 | each role moves only its own operand; the two profiles | BUILD | EQUAL | B24p.12 |
| B24p.21 | the curves at control | READING | — | B24p.17 |
| B24p.19 | the influence verbs call the proceeding | BUILD | MOVER(behaviour) | B24p.16, .21 |
| B24p.20 | the sitting is written; each hearer is moved for himself; the topic reaches the effect | BUILD | MOVER(behaviour) | B24p.19 |
| B24p.22 | a reading is kept by the one who read | BUILD | EQUAL | B24p.20 |
| B24p.23 | the six roles on | BUILD | MOVER(behaviour) | B24p.18, .22 |
| B24p.99 | re-pin and close readings | BUILD | MOVER (the re-pin) | every position above |

---

### B24p.01 — the rosters: grounds, moves, ends, authorities · RD §A.1, §C.4, §C.1 · BUILD · HASH EQUAL
- SOURCE: RD §A.1 (the words), §A.5 (ends), §B.3 (the grounds and their `read:` cells), §C.4 (the moves), §C.1 (`authority`); B24.03 (which planned `hearing_moves`; C(B24p) UNDECIDED (4)); B24a.04 (`authority.by_faction`); B04.07 (the four `moved_by_*` traits); rulings R1, R4.
- ADVANCES: none of the nine; the closed sets every later item reads.
- INSTRUCTION:
  1. `engine/season/rosters.yaml`, four rosters, each with `source:`, `cite:` and a note in the file's form:
     `grounds` (ordered): `evidence {read: {attribute: attr.mind.acuity}, trait: moved_by_evidence}`, `consequence {read: {pursuit: strongest}, trait: moved_by_consequence}`, `authority {read: {conviction: strongest}, trait: moved_by_authority}`, `solidarity {read: {attribute: attr.social.attunement}, trait: moved_by_solidarity}`;
     `proceeding_moves` (ordered), one row each with `draw`, `capability`, `resisted_by`, `ground` as RD §C.4's table gives them and three more cells the module branches on, so that no move id is ever compared in code: `fit` (does the ground's fit count: true on `argue`, `deceive`), `holds` (does the move carry its own pull: true on `deceive`), `effect` (`track` on `argue` and `deceive`, `strike` on `press`, `pull` on `divert`, `yield` on `concede`, `none` on `rest`): `argue`, `press`, `divert`, `deceive`, `concede`, `rest`;
     `proceeding_ends`: `budget`, `rested`, `yielded`, `broken`, `struck`, `adjourned`;
     `authorities`: `parties`, `polity`, `church`, `guild`, `none`, with a mapping `by_faction` from each faction the realm seats (`role_templates.by_faction`'s keys) to one member `[ASSUMPTION; Jordan to correct: Crown, Parliament, the duchies → polity; Church → church; Guild → guild; any other → polity — basis: `venues.yaml:64-109`'s `serves:` tags]`.
  2. `engine/season/data/rosters.py`: `GROUNDS`, `PROCEEDING_MOVES`, `PROCEEDING_ENDS`, `AUTHORITIES`, `AUTHORITY_BY_FACTION` beside `LADDER_RUNGS`, each refusing a duplicate id; `GROUNDS` refuses a `read:` whose key is not one of `attribute`, `pursuit`, `conviction`, an attribute outside `descriptors.ATTRIBUTES`, and a `trait:` that is not a seated disposition (B04.07's roster); `PROCEEDING_MOVES` refuses a `capability:` outside `descriptors.CAPABILITIES`, a skill on a move with `draw: false`, a `resisted_by` outside `will`, `attunement`, and an `effect` outside the five.
- WHERE: `engine/season/rosters.yaml`; `engine/season/data/rosters.py`; NEW `engine/season/tests/test_sc_proceeding_data.py`.
- TESTS: in the new file, written first and read red: `test_the_proceeding_rosters_load_with_the_rows_named` (ids and order equal RD's lists); `test_a_ground_reading_an_unknown_attribute_is_refused`; `test_a_drawless_move_with_a_skill_is_refused`.
- FALSIFIER and CONTROL: a move row whose effect names a winner; a ground with no `read:`. Control: the seed-0 one-season hash equals B07's close (no reader yet).
- GATE: `python -m pytest engine/season/tests/test_sc_proceeding_data.py -q` → three pass; `python -c "import engine.season.data.rosters"` → exit 0; `python -m engine.season.harness.register --check` → counts not risen; the seed-0 hash (`HASH READING`) → equal.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `data/rosters.py::LADDER_RUNGS`, `rosters.yaml: role_templates.by_faction`, `descriptors.ATTRIBUTES`; V12 Batch B04-capability-home (B04.07's traits, `descriptors.CAPABILITIES`, the `deception` row B04.18).
- GLOSSARY: rows *move* (owner `rosters.yaml: proceeding_moves`), *ground* ("what an argument appeals to: evidence, consequence, authority or solidarity"), *proceeding* ("a run of exchanges between sides, before those who decide and those who watch, on one topic, under a type").
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B24p's `valoria-author` producer, `isolation: worktree`; `Item: B24p.01`, `[skip ci]`.

### B24p.02 — the proceeding's records · RD §A.3 · BUILD · HASH EQUAL
- SOURCE: RD §A.3 (the records, copied there in full); B24.05 (HEAR_B's seven records, which these generalise); `04` §A.2 (a module's typed input and outcome); `queries/inputs.py:12-15` (the leaf rule).
- ADVANCES: none; the typed boundary of the entry.
- INSTRUCTION: `engine/season/queries/inputs.py`, after `Margin`: the frozen dataclasses `Speaker`, `Decider`, `Room`, `Move`, `ProceedingType`, `ProceedingInput`, `SideState`, `ProceedingState`, `ExchangeView`, `Exchange`, `ProceedingOutcome` and the `NamedTuple` `Choice`, with the fields and field comments of RD §A.3, each comment kept as the docstring's field list (the file's form). Stdlib only: `dataclass`, `NamedTuple`, `Mapping`, `Optional`. No field holds a `World`, a token, a `Person` or a callable. `ProceedingOutcome.verdicts` is a tuple of `(id, Margin)`; the class docstring says: *"margins, never a band, a side or a winner: the host grades each on the one ladder (`seam/ladder.py::degree_of`)"*.
- WHERE: `engine/season/queries/inputs.py`; `engine/season/tests/test_sc_proceeding_data.py`.
- TESTS: written first and read red: `test_the_proceeding_records_are_frozen_and_world_free` (constructs each; assigning a field raises `FrozenInstanceError`; an `ast` scan of the file finds no import outside the standard library); `engine/season/tests/test_social_contest_module.py` stays green (a module importing a record pulls in nothing else of the host).
- FALSIFIER and CONTROL: a record with a mutable default or a host import. Control: hash equal (records are not `World` state).
- GATE: `python -m pytest engine/season/tests/test_sc_proceeding_data.py engine/season/tests/test_social_contest_module.py -q` → pass.
- HASH MOVERS: none.
- DEPENDS ON: V12 B24p.01; EXISTS-IN-TREE `queries/inputs.py::Margin`, `::SocialContestInput`.
- GLOSSARY: rows *exchange* ("one speech by one side in a proceeding"), *decider* ("a person the close of a proceeding ballots"), owner `queries/inputs.py`.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B24p's producer; `Item: B24p.02`, `[skip ci]`.

### B24p.03 — the type rows: five keys, two disposals, rites, audience kinds, four rows · RD §C.1 to §C.5 · BUILD · HASH EQUAL
- SOURCE: RD §C.1 (keys), §C.2 (the loader's checks 1 to 6), §C.3 (the thirteen rows), §C.4 (`rites:`), §C.5 (`audience_kinds:`), §C.6 item 4 (`abridged`); `data/arrangements.py:60-77`; B05.21 (`standard:`); B24.09 (which planned `rites:` and `rite:`); ruling R4.
- ADVANCES: none of the nine; R4's parameters are loaded and checked.
- INSTRUCTION:
  1. `engine/season/data/arrangements.py`: `_ARRANGEMENT_KEYS` gains `rite`, `exchanges`, `authority`, `presumes`, `strikes`; `_DISPOSAL_VALUES` gains `hearers`, `exchange`; NEW `_RITE_KEYS = frozenset({"id", "moves", "faults"})`, `_AUDIENCE_KEYS = frozenset({"id", "attention", "distraction", "proof_weight"})`, `_AUDIENCE_IDS = ("none", "bench", "gallery", "crowd")`; `_load` reads `rites:` then `audience_kinds:` then `arrangements:`; `_load_arrangement` applies RD §C.2's checks 2 and 3, each a `SystemExit` naming the row and the key; exposed: `RITES`, `AUDIENCE_KINDS` beside `ARRANGEMENTS`.
  2. NEW `abridged(row: dict, move: str = "argue") -> dict` (pure; RD §C.6 item 4): a copy with `order: "free"`, `exchanges: (1, 1)`, `disposal: "exchange"`, `strikes: 0`, `presumes: "none"`, and `moves` `{"for": (move,), "against": (), "bench": ()}`; it refuses a `move` that is not a `PROCEEDING_MOVES` member with `draw: true`.
  3. `engine/season/arrangements.yaml`: the `rites:` block (four rows, RD §C.4) and the `audience_kinds:` block (four rows, every `attention` 0, `distraction` 0, `proof_weight` 0.5: the control) before `arrangements:`; on each of the nine rows the five cells of RD §C.3's table; the four new rows `conversation`, `questioning`, `rally`, `audience` with every key (the existing thirteen as RD §C.3 and these: `bench_basis: none` on the three `hearers` rows and `determine` on `audience`; `records_dissent: false`; `term_required: false`; `appeal_basis: none`; `interposed: []`; `proofs` as RD §C.3's notes; `disposal_reach: room`; `standard: plain`). Each new cell carries `# [ASSUMPTION; Jordan to correct]` and the file header's count sentence is corrected.
- WHERE: `engine/season/data/arrangements.py`; `engine/season/arrangements.yaml`; `engine/season/tests/test_sc_proceeding_data.py`; `engine/season/tests/test_arrangements.py`.
- TESTS: written first and read red: `test_thirteen_rows_load_and_each_names_a_rite`; `test_a_row_whose_rite_names_an_unrostered_move_is_refused` (planted); `test_a_seeded_row_may_not_be_disposal_exchange` (planted); `test_abridged_keeps_the_venue_and_takes_one_exchange` (for every row, `abridged(row)` equals the row on `standard`, `floor`, `authority`, `venue_min_rank`, `proofs` and reads `exchanges == (1, 1)`; `assert checked == 13`); `test_audience_kinds_are_exactly_four`. `test_arrangements.py`'s count assertion is re-pointed from nine to thirteen and named in the commit.
- FALSIFIER and CONTROL: a row loads with `disposal: hearers` and a bench; a fourteenth key loads unread. Control: `_eff_determine` reads the same `disposes` for the nine rows before and after (their existing cells are byte-equal: `git diff` shows only added lines on them); the seed-0 hash equal.
- GATE: `python -m pytest engine/season/tests/test_sc_proceeding_data.py engine/season/tests/test_arrangements.py -q` → pass; `python -c "import engine.season.data.arrangements as a; print(len(a.ARRANGEMENTS), sorted(a.RITES), sorted(a.AUDIENCE_KINDS))"` → `13` and the eight ids; the seed-0 hash → equal.
- HASH MOVERS: none (no computed case names a row until B24p.15).
- DEPENDS ON: V12 B24p.01 (`PROCEEDING_MOVES`, `AUTHORITIES`); V12 Batch B05-one-roll (B05.21: `standard` in `_ARRANGEMENT_KEYS`); EXISTS-IN-TREE `_load_arrangement`, `_refuse_unknown`, `_refuse_not_in`, `_ORDER_VALUES` (`free`, `written_only` already members).
- GLOSSARY: rows *rite* ("the moves each side may make and the faults a proceeding counts", owner `arrangements.yaml: rites`), *audience* ("those present who are not speakers; its kind is computed from who is there"), *proceeding type* (owner `arrangements.yaml: arrangements`).
- COST and TIER: small build; `sonnet`, `high`; SC review of the new cells.
- LANDS IT: B24p's producer; `Item: B24p.03`, `[skip ci]`.

### B24p.04 — the settings, at their controls · RD §B (every table) · BUILD · HASH EQUAL
- SOURCE: RD §B.1 to §B.6 (each role's settings table: name, control, shipped), §A.5 (`track_step`, `track_clip`, `yield_level`, `break_level`), §C.1 (`presumption_level`), §C.4 (`deceive_pull`, `concede_step`), §C.5 (`crowd_at`); `data/fixtures.py`'s tag form (`reception_gain`'s line); B24.07 (the precedent).
- ADVANCES: none; each number the roles read has one home and a register row.
- INSTRUCTION:
  1. `engine/season/data/fixtures.py`: one line per setting, at its CONTROL value, each with a `[JUSTIFIED: engine/season/hole_register.yaml H-<slot> -- site: Fixtures <name>, graded assumption …]` tag. Forty-eight in all: Focus `off_topic_step` 0, `divert_pull` 0, `divert_gain` 0, `rattle_pull` 0, `strike_level` None; Reason `proofs_per_reason` None, `account_step` 0, `account_max` 0.9; Attunement `fit_level` None, `misfit_level` None, `read_ob` 1.4, `read_scale` 1.0, `read_blur` 1.0, `guard_step` 0, `reading_kept` False; Presence `delivery_step` 0, `heard_step` 0, `heard_floor` 1.0; Grace `standard_step` 0, `standard_demand` (a table over `difficulty_levels`, every level 0), `respect_step` 0, `mark_level` None, `cover_step` 0, `cover_max` 0.9, `mark_shame` 0; Will `press_base` 1.0, `blow_gain` 0, `sore_gain` 0, `strain_carry` 0, `mark_resolve` 0, `resolve_base` None (read as the type's maximum), `resolve_per_will` 0, `shield_step` 0, `shield_max` 0.6, `resist_step` 0, `press_rebound` 0, `press_at` 1.0, `strain_rest` 1, `yield_level` None, `break_level` None, `break_at` None (never); the close `track_step` 0, `track_clip` 3.0, `presumption_level` None, `concede_step` 0, `deceive_pull` 0, `crowd_at` 12; and `audience_room` (a pointer row: the three columns of `arrangements.yaml: audience_kinds` are tuned as one table).
  2. `engine/season/hole_register.yaml`: one NUMBER row per line, `site: Fixtures <name>`, graded `assumption`, naming its control, RD §B's shipped value and a three-point sweep (the control, the shipped value, one point between; where the control is `None`, the two `LEVEL_SIGMA` names beside the shipped one). Ids: B24p's H block slots 1 to 48.
  3. NEW `engine/season/seam/wrappers/sigma.py::proceeding_dials(fx) -> Mapping`: the forty-eight values plus `pool_add`, `pool_floor`, `pool_default`, `opposition_rate`, `obstacle_ceiling`, `ceiling_per_pool`, `obstacle_refusal_multiple`, `attribute_mid`, `attribute_floor`, `attribute_ceiling` (the last three from `engine/substrate/descriptors.py`), as a `types.MappingProxyType`: the one place the proceeding's settings are named for the record.
- WHERE: `engine/season/data/fixtures.py`; `engine/season/hole_register.yaml`; `engine/season/seam/wrappers/sigma.py` (`proceeding_dials`); `engine/season/tests/test_sc_proceeding_data.py`.
- TESTS: written first and read red: `test_every_proceeding_setting_has_a_register_row_and_a_control` (each name in `proceeding_dials` is a `Fixtures` field with a tag; `assert checked >= 48`).
- FALSIFIER and CONTROL: a setting with no register row (`tools/ci_sim_fabrication_check.py` refuses). Control: nothing reads them: the seed-0 hash equals B24p.03's.
- GATE: `python tools/ci_sim_fabrication_check.py` → exit 0; `python tools/export_sim_params.py --check` → exit 0 (after `--build` if the exporter reads `Fixtures`); `python -m engine.season.harness.register --check` → counts not risen; the seed-0 hash → equal.
- HASH MOVERS: none.
- DEPENDS ON: V12 Batch B00-ids (B24p's H block, allocated at the fold: §F); V12 Batch B05-one-roll (B05.08's `pool_add`, `pool_floor`, `opposition_rate`); EXISTS-IN-TREE `data/fixtures.py`, `LEVEL_SIGMA`, `descriptors.ATTRIBUTE_FLOOR`, `::ATTRIBUTE_CEILING`.
- GLOSSARY: none.
- IDS: H block slots 1–48.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B24p's producer; `Item: B24p.04`, `[skip ci]`.

### B24p.05 — the leverage sources and obstacle terms of the roles · RD §B.7, §B.2 c, §B.6 c · BUILD · HASH EQUAL
- SOURCE: RD §B.7 (the sources and terms, the two bindings), §B.2 (c) and §B.6 (c) (`eased_by`); B05.10 (the signed channel), B05.14 (`obstacle_terms`, `OBSTACLE_TERMS`), B05.17, B05.21 (`standard`, `regard`); `sigma.py:160-170` (the roster/binding check); CP-T01-05.
- ADVANCES: none; the roster stays the only door into the sigma term and the obstacle.
- INSTRUCTION:
  1. `engine/season/rosters.yaml: advantage_sources`: five members appended in order, each with `bound: module`: `delivery`, `fit`, `respect`, `marks`, `resist`; every existing member gains `bound: host`. `obstacle_terms`: a member `off_topic` appended, `bound: module`; `standard` gains `bound: module` (its operand is the speaker's shortfall, RD §B.5 a); a column `eased_by:` on every member, one of `reason`, `will`, `none`: `reason` on `rank_gap` and `commitment`, `will` on `reception` and `regard`, `none` elsewhere (a member absent at this item's open takes its cell when its own item lands it; the loader refuses a member with no cell).
  2. `engine/season/data/rosters.py`: read `bound` and `eased_by`; refuse another value.
  3. `engine/season/seam/wrappers/sigma.py`: the import-time check becomes: the `bound: host` members of each roster equal the keys of `ADVANTAGE_SOURCES` and `OBSTACLE_TERMS`, and the `bound: module` members equal the names the module declares (`composition.require("social_contest.proceeding")`'s module attributes `LEVERAGE` and `TERMS`, read at the first call, B24p.12); until B24p.12 lands the second half is skipped with the entry absent and asserted by B24p.12's test. `obstacle_operands(w, act, row)` returns four-tuples `(name, raw, step, eased_by)` for the proceeding's builder (the three-tuple stays `roll.py`'s input: the fourth member is dropped where `SocialContestInput.obstacle_operands` is filled).
- WHERE: `engine/season/rosters.yaml`; `engine/season/data/rosters.py`; `engine/season/seam/wrappers/sigma.py`; `engine/season/tests/test_sc_proceeding_data.py`; `engine/season/tests/test_obstacle_form.py` (B05.14's, read).
- TESTS: written first and read red: `test_every_source_and_term_is_bound_exactly_once` (no member is in both tables or in neither; `assert checked == len(roster)` for each roster); `test_an_obstacle_term_with_no_eased_by_is_refused` (planted).
- FALSIFIER and CONTROL: a module source that is not a roster member reaches a speech (B24p.07's test re-reads it). Control: `test_obstacle_form.py::test_every_roster_member_has_a_host_function` re-pointed to the `bound: host` members and green; the seed-0 hash equal.
- GATE: `python -m pytest engine/season/tests/test_sc_proceeding_data.py engine/season/tests/test_obstacle_form.py -q` → pass; `python -c "from engine.season.seam.wrappers import sigma"` → imports.
- HASH MOVERS: none.
- DEPENDS ON: V12 Batch B05-one-roll (B05.10, B05.14, B05.17, B05.21); V12 B24p.04; EXISTS-IN-TREE `sigma.py::ADVANTAGE_SOURCES`, `roster("advantage_sources")`.
- GLOSSARY: none (the five sources are named in *leverage*'s row as its members).
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B24p's producer; `Item: B24p.05`, `[skip ci]`.

### B24p.06 — what moves a person, and the strain he carries, derived · RD §B.3, §A.2 · BUILD · HASH EQUAL
- SOURCE: RD §B.3 (the dispositions and their `read:` cells), §A.2 (the last row of the state table), §B.6 (`strain_rest`); `Person.pursuits`, `.conviction`, `.attributes` (`state/carriers.py:782-855`); `affiliation_roster.scale`; the practice addend's read of a person's own acts (`sigma.py:306-307`); AX-2.
- ADVANCES: none; R1's *"audience adjudicator opponent"* each have something to read.
- INSTRUCTION: `engine/season/queries/person_q.py` (person-side, no `World`):
  1. `moved_by(p: Person) -> tuple`: for each row of `GROUNDS` in roster order, `(ground id, weight)` with weight in `[0, 1]`: `attribute` → `(p.attributes.get(key, mid) - FLOOR) / (CEILING - FLOOR)`; `pursuit: strongest` → `max(p.pursuits.values(), default=0.0)` clamped to `[0, 1]`; `conviction: strongest` → `max(p.conviction.values(), default=0) / scale_max` (the roster's own scale ceiling, read, never typed); and `1.0` where `p` holds the row's `trait` (B04.07's `Person.traits`). An unheld attribute reads the mid-point (B05.16's rule).
  2. `strain_carried(marks: int, scenes_since: int, fx) -> float`: `max(0, marks - fx.get("strain_rest") * scenes_since) * fx.get("press_base")`: the marks he has not yet rested off, each worth one base blow of strain, in the units `SideState.strain` uses; `0.0` when `blow_gain` is 0 (the control: no press does anything). The host (B24p.13) passes `marks`, the count of marks he took in the `ending` records of this season's Events (B24p.20 writes them), and `scenes_since`, the scenes he has spent since the last of them.
- WHERE: `engine/season/queries/person_q.py` (`moved_by`, `strain_carried`); NEW `engine/season/tests/test_sc_roles.py`.
- TESTS: in the new file, written first and read red: `test_moved_by_reads_four_grounds_from_what_he_holds` (a hand-built person: Reason 7 → `evidence` 1.0; no conviction → `authority` 0.0; a seated trait → 1.0); `test_every_generated_person_has_a_ground_that_moves_him_most` (over `generated_attributes` for 2,000 keys with drawn pursuits absent: the four weights are not all equal for at least 80 % of them; `assert checked == 2000`); `test_strain_carried_clears_with_scenes`.
- FALSIFIER and CONTROL: `moved_by` reading another person or the `World`; a flat vector for most of a generated population (then Attunement has nothing to read, RD §B.3's control). Control: no caller yet: hash equal.
- GATE: `python -m pytest engine/season/tests/test_sc_roles.py -q -k "moved_by or strain_carried"` → pass; the share of non-flat vectors quoted in the commit body.
- HASH MOVERS: none.
- DEPENDS ON: V12 B24p.01 (`GROUNDS`); V12 Batch B04-capability-home (B04.07 `Person.traits`); EXISTS-IN-TREE `Person.pursuits`, `.conviction`, `.attributes`, `data/affiliations.py` (the scale).
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B24p's producer; `Item: B24p.06`, `[skip ci]`.

### B24p.07 — the speech draw: Reason, Presence, Grace and Will on one roll · RD §B.2, §B.4, §B.5, §B.6 c–d, §B.7 · BUILD · HASH EQUAL
- SOURCE: RD §B.7 (the composition, copied), §B.2, §B.4, §B.5 (a), (b) start and (c), §B.6 (c), (d); `modules/social_contest/roll.py::roll`, `::obstacle` (B05.02, B05.14); `04` §A.2; R1, R2, R8.
- ADVANCES: none at control; four of the six roles have their operand.
- INSTRUCTION: NEW `modules/social_contest/proceeding.py`. Imports: `engine.dice_engine.sigma_leverage` (`pool_of`, `level`, `net_boost`, `band_odds`), `engine.dice_engine.fmath` (B06), `engine.season.queries.inputs` (the records), `.roll` (`roll`, `obstacle`). Nothing else; no `World`; no module-level state but the two binding tables.
  1. `LEVERAGE: dict` — name → `fn(S, s, target, room, type, move, ground, dials) -> (sigma_for, sigma_against)` for `delivery`, `respect`, `marks`, `resist` (and `fit`, a stub returning `(0.0, 0.0)` until B24p.08), each the formula of RD §B.4, §B.5 (b), §B.5 (c), §B.6 (d); `resist` reads the target's `will`, or his `attunement` where the move's `resisted_by` says so (a `Move` record of `ProceedingType.moves`, handed in; no move id is compared in code). `TERMS: dict` — name → `fn(...) -> (raw, step)` for `standard` (RD §B.5 a) and `off_topic` (a stub returning `(0.0, 0.0)` until B24p.09).
  2. `_heard(S, room, type, dials) -> float` (RD §B.4); `_shield(S, dials)`, `_account(S, dials)`, `_cover(S, dials)` (RD §B.6 c, §B.2 c, §B.5 c).
  3. `_speech_input(inp, S, s, target, move, ground, on_topic) -> SocialContestInput`: `pool = pool_of(S.reason + rank(S, move.capability), S.addends, pool_add, pool_floor) * _heard(...)`; operands = `S.operands` with each step multiplied by `(1 - _account)` where `eased_by == "reason"` and the name is in `S.accounts`, by `(1 - _shield)` where `eased_by == "will"`, plus the `TERMS` in roster order; sources = `S.levels` plus the `LEVERAGE` in roster order, the `proofs` source being `(level(proof_level) * min(S.proofs, cap) * 2 * room.proof_weight, 0.0)` with `cap = proofs_per_reason * S.reason` or no cap when the setting is `None`; `leverage = sum(for) - sum(against) * (1 - _shield)`; `opposition = target.score`; the bounds from `dials`.
  4. `_speech(inp, S, s, target, move, ground, on_topic, rng) -> tuple[Margin, tuple, SocialContestInput]`: `roll(_speech_input(...), rng)` and the per-source pairs for `Exchange.levels`.
  5. `exchange_odds(inp, state, mover_id, choice) -> tuple` (pure): `band_odds(x.pool, obstacle(x)[0], net_boost(x.leverage, x.pool))` for `x = _speech_input(...)` with `on_topic=True`.
- WHERE: NEW `modules/social_contest/proceeding.py`; NEW `engine/season/tests/test_sc_proceeding_module.py`; `engine/season/tests/test_sc_roles.py`.
- TESTS: written first and read red (no module): in `test_sc_proceeding_module.py`, `test_at_control_a_speech_is_the_single_roll` (for 200 hand-built speakers at every setting's control, `exchange_odds` `==` `band_odds` on the record `SocialContestInput(pool=pool_of(reason + rank, addends, …), opposition=target.score, …)`, and `_speech` with a seeded `Draw` returns exactly `roll(that record, the same Draw)`; `assert checked == 200`); `test_the_module_imports_the_dice_engine_and_the_record_leaf_only` (a fresh-process import, `test_social_contest_module.py`'s form). In `test_sc_roles.py`: `test_reason_is_the_dice_the_usable_proofs_and_the_account`, `test_presence_is_the_share_heard_and_the_delivery`, and parts (i), (ii) of `test_grace_meets_the_standard_keeps_esteem_and_covers_a_mark` and (iii), (iv) of `test_will_resists_the_rattle_outlasts_and_discounts_what_is_against_him` (RD §B.2, §B.4, §B.5, §B.6, with the shipped values set in the test's own fixtures).
- FALSIFIER and CONTROL: a source or term the roster does not name reaches `Exchange.levels` or `Margin.terms`; a pool rounded to a whole die (`Speaker.reason` 2.5 must reach `roll` as 2.5 plus the base). Control: the `==` of `test_at_control_a_speech_is_the_single_roll`.
- GATE: `python -m pytest engine/season/tests/test_sc_proceeding_module.py engine/season/tests/test_sc_roles.py -q` → pass; `grep -n "import" modules/social_contest/proceeding.py` → the four imports named; the seed-0 hash → equal (no caller).
- HASH MOVERS: none.
- DEPENDS ON: V12 B24p.02, .04, .05; V12 Batch B05-one-roll (B05.02 the continuous `roll`, the closed-form `band_odds`; B05.14 `obstacle`, `Margin.terms`, `SocialContestInput.obstacle_operands`); V12 Batch B04 (B04.24 `pool_of`); V12 Batch B06 (`fmath`).
- GLOSSARY: row *leverage*: its members gain the five module-bound sources.
- COST and TIER: small build (about 150 lines); `sonnet`, `high`; `opus` reads the control equality.
- LANDS IT: B24p's producer; `Item: B24p.07`, `[skip ci]`.

### B24p.08 — the reading: Attunement · RD §B.3 · BUILD · HASH EQUAL
- SOURCE: RD §B.3 (the formulas, copied); ED-IN-0350; v30 `:154-188`; N12.
- ADVANCES: none at control; Attunement's operand.
- INSTRUCTION: `modules/social_contest/proceeding.py`:
  1. `_fit(v: tuple, g: str) -> float` and `_fit_body(targets: tuple, g: str) -> float` (RD §B.3; a flat vector returns 0.0; the body's weights are `Decider.weight`).
  2. `_read(inp, S, s, T_side, targets, rng) -> tuple`: draws `1 + len(inp.grounds) + 1` normals in that order (`rng.normal(0.0, 1.0)` for the `xi`; the first through `roll_net_continuous` on the reading pool `pool_of(S.attunement + rank(S, "insight"), 0, pool_add, pool_floor)`); `read = net + net_boost(-guard_step * (guard - mid), pool) - (even_line(pool_add) + read_ob)` with `guard` the other speaker's `grace`, or the weight-mean `grace` of the deciders for a one-speaker type; `acc = (1 + fmath.tanh(read / read_scale)) / 2`; `blur = read_blur * (1 - acc)`; returns `(("acc", acc), ("target:<ground>", believed), …, ("other:<ground>", believed), …, ("strain", believed strain))`, where the `target:` entries blur the weight-mean vector of the persons an argument addresses and the `other:` entries the other speaker's own vector (empty for a one-speaker type); both use the same `xi` per ground.
  3. `LEVERAGE["fit"]` becomes RD §B.3's `fit source` on the TRUE vectors for a move with `fit: true`, and `(0.0, 0.0)` otherwise (a `strike` move's ground is an aim, B24p.10).
- WHERE: `modules/social_contest/proceeding.py` (`_fit`, `_fit_body`, `_read`, `LEVERAGE["fit"]`); `engine/season/tests/test_sc_roles.py`.
- TESTS: written first and read red: `test_attunement_sharpens_the_reading_and_moves_only_the_choice` parts (i) to (iii) and its control (RD §B.3); `test_a_reading_always_takes_the_same_number_of_draws` (a counting `Draw`: `len(grounds) + 2` normals whatever the target; `assert` on the count).
- FALSIFIER and CONTROL: Attunement moving a speech whose ground was forced; a reading that shows `true`. Control: a flat target vector; both fit levels `None`.
- GATE: `python -m pytest engine/season/tests/test_sc_roles.py -q -k "attunement or reading"` → pass; hash equal.
- HASH MOVERS: none.
- DEPENDS ON: V12 B24p.07; V12 Batch B06 (`Draw.normal`, `fmath.tanh`).
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B24p's producer; `Item: B24p.08`, `[skip ci]`.

### B24p.09 — the hold: Focus · RD §B.1 · BUILD · HASH EQUAL
- SOURCE: RD §B.1 (the formulas, copied); HEAR_B `irrelevance`; AR-23.
- ADVANCES: none at control; Focus's operand.
- INSTRUCTION: `modules/social_contest/proceeding.py`: `_hold(inp, S, s, move, rng) -> bool`: one normal, always taken: `pull = s.pull + inp.room.distraction + (deceive_pull if move.holds else 0)`; `on_topic = pull <= 0 or roll_net_continuous(pool_of(S.focus, 0, pool_add, pool_floor), rng) - (even_line(pool_add) + pull) >= 0`. `TERMS["off_topic"]` returns `(0.0 if on_topic else 1.0, off_topic_step)`. The caller clears `s.pull` and adds a strike when off the topic (B24p.10 owns the state write).
- WHERE: `modules/social_contest/proceeding.py` (`_hold`, `TERMS["off_topic"]`); `engine/season/tests/test_sc_roles.py`.
- TESTS: written first and read red: `test_focus_holds_the_topic_and_moves_nothing_else` and its two controls (RD §B.1); `test_a_deceiver_always_has_something_to_hold` (with `deceive_pull` above 0 and an empty room, a `deceive` draws a hold that can fail and an `argue` cannot).
- FALSIFIER and CONTROL: an off-topic speech with no `off_topic` entry in `Margin.terms`; Focus changing a speech when nothing pulls. Control: pull 0.
- GATE: `python -m pytest engine/season/tests/test_sc_roles.py -q -k "focus or deceiver"` → pass; hash equal.
- HASH MOVERS: none.
- DEPENDS ON: V12 B24p.07.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B24p's producer; `Item: B24p.09`, `[skip ci]`.

### B24p.10 — the moves' effects and the steadiness draw · RD §A.4 steps 5–7, §B.5 b–c, §B.6 a–b · BUILD · HASH EQUAL
- SOURCE: RD §A.4 (the step table), §B.6 (a), (b) (the formulas, copied), §B.5 (the esteem changes), §B.1 (`divert`), §C.4 (`concede`); v30 `:197-270`; N5, N8.
- ADVANCES: none at control; Will's draw and Grace's esteem act between exchanges.
- INSTRUCTION: `modules/social_contest/proceeding.py`: `_exchange(inp, state, i, choice, rng) -> tuple[ProceedingState, Exchange]`, pure but for `rng`, building new `SideState` values with `dataclasses.replace` (never a field assignment). In order: `_read` (B24p.08; the caller passed its result to the decider before `choice` was made, so `_exchange` receives the reading and does not redraw), `_hold`, `_speech`, then one normal for the steadiness draw, always taken; then by the move's `effect`:
  `track` (`argue`, `deceive`) → `track += sign * clamp(margin, -track_clip, track_clip)` (`sign` +1 for `for`);
  `strike` (`press`) → as RD §B.6 (a): on `margin >= 0`, `aim`, `blow`, and `steady = that normal's roll on pool_of(T.will, 0, pool_add, pool_floor) - (even + t.strain + blow)`; a mark or carried strain as written there, with `t.esteem` reduced by `mark_shame * (1 - _cover(T))`; on `margin < 0`, `s.esteem -= press_rebound`;
  `pull` (`divert`) → on `margin >= 0`, `t.pull += divert_pull + divert_gain * margin`;
  `yield` (`concede`) → `track -= sign * concede_step`, `s.resolve += 1`; `none` (`rest`) → nothing.
  Then `s.resolve -= 1` for a move with `draw: true`, `s.pull = 0.0`, `s.strikes += 1` when off the topic, `state.n += 1`, and the `Exchange` record (its `strain` the blow dealt, `marked` whether a mark was taken). Which branch runs is read from `Move.effect`, never from the move's id.
- WHERE: `modules/social_contest/proceeding.py` (`_exchange`); `engine/season/tests/test_sc_roles.py`, `test_sc_proceeding_module.py`.
- TESTS: written first and read red: parts (i), (ii) of `test_will_resists_the_rattle_outlasts_and_discounts_what_is_against_him` and part (iii) of `test_grace_meets_the_standard_keeps_esteem_and_covers_a_mark` (RD §B.6, §B.5); `test_an_exchange_takes_a_fixed_number_of_draws` (a counting `Draw`: `len(grounds) + 5` normals for every move, `rest` and `concede` included); `test_no_effect_branch_names_a_move` (an `ast` scan of `proceeding.py` finds no string equal to a `PROCEEDING_MOVES` id).
- FALSIFIER and CONTROL: a mark with no steadiness draw; a press whose blow is the same on every ground. Control: `blow_gain` 0: no press changes any `SideState`.
- GATE: `python -m pytest engine/season/tests/test_sc_roles.py engine/season/tests/test_sc_proceeding_module.py -q` → pass; hash equal.
- HASH MOVERS: none.
- DEPENDS ON: V12 B24p.08, .09.
- GLOSSARY: rows *strain* ("the pressure a side has taken in a sitting"), *mark* ("a rattle: a blow he did not stand"), *resolve* ("how many more exchanges a side can speak"), owner `queries/inputs.py::SideState`.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B24p's producer; `Item: B24p.10`, `[skip ci]`.

### B24p.11 — the sitting: order, legal moves, the automatic policy, resolve, ends · RD §A.5, §A.6, §B.6 b · BUILD · HASH EQUAL
- SOURCE: RD §A.5 (order, ends), §A.6 (the automatic policy), §B.6 (b) (resolve); B24.06's "How a sitting runs" (HEAR_B `:139-149`), which this is with the six roles in it; the fight's decider precedent (`queries/inputs.py:165-196`).
- ADVANCES: none at control; R6's *"a run of exchanges"* exists as code.
- INSTRUCTION: `modules/social_contest/proceeding.py`:
  1. `_start(inp) -> ProceedingState`: `inp.state` if given; else per speaker a `SideState` with `strain = S.strain`, `marks = 0`, `resolve = resolve_base + resolve_per_will * S.will` (or the type's maximum when `resolve_base` is `None`), `pull = 0`, `strikes = 0`, `esteem = respect_step * (S.grace - mid)`, `read = ()`; `track = 0.0`; `issue = inp.issue`.
  2. `_mover(inp, state) -> Optional[int]` by `type.order` (RD §A.5): `free`, `written_only` → the speaker with the most `effort - spoken` left, ties to `for`; `alternating`, `scripted` → the sides in turn, `for` first; `rank` → by `precedence` descending, ties by id, cycling; a speaker with no legal move but `rest` is passed over; `None` when nobody can move.
  3. `_legal(inp, state, i) -> tuple`: the rite's moves for his side, less every `draw: true` move when `s.resolve <= 0` or his effort is spent.
  4. `_auto(inp, state, i, reading) -> Choice` (RD §A.6): his first legal move of effect `track`, on the argmax of the reading's `target:` entries, unless the track stands against him, he has a legal move of effect `strike`, and `1 - steady_odds >= press_at`, where `steady_odds` is the closed form of B.6 (a)'s draw on the believed strain, the blow `blow_gain * (press_base + 1) * (1 + sore_gain * believed_other[g])` and a Will read at `mid` (he does not know it): then that `strike` move, on the argmax of the `other:` entries. With no legal `track` move he takes his first legal move. The policy reads effects, never ids.
  5. `proceed(inp, rng, decide=None) -> ProceedingOutcome`: `state = _start(inp)`; loop while `state.n < type.exchanges[1]`: `i = _mover(...)` (stop `rested` when `None`); the reading; `choice = decide(ExchangeView(...)) if decide else _auto(...)`, refused with a `ValueError` naming the mover if not in `_legal`; `_exchange`; then the ends in this order: `broken` (a side at `break_at` marks), `struck` (strikes over the row's allowance, where the rite lists `irrelevance` as ending), `yielded` (a side with `resolve <= 0` whose opposite still has resolve and effort; or a `concede` on the last issue), `budget`. A sitting shorter than `type.exchanges[0]` continues past `rested` only if a side can still move. Then `_close` (B24p.12).
- WHERE: `modules/social_contest/proceeding.py` (`_start`, `_mover`, `_legal`, `_auto`, `proceed`); `engine/season/tests/test_sc_proceeding_module.py`.
- TESTS: written first and read red: `test_one_exchange_under_an_abridged_row_and_no_decider_is_asked` (`decide` is a function that raises: `proceed` under `abridged(conversation)` returns one `Exchange` and never calls it); `test_order_follows_the_row` (hand-built `rank`, `alternating`, `scripted`, `free` types: the movers' ids equal the expected lists); `test_a_scripted_respondent_cannot_press` (a decider returning `press` for `against` under `questioned` raises); `test_every_end_is_reachable_and_is_never_a_verdict` (planted states reach each of `budget`, `rested`, `yielded`, `broken`, `struck`; in each the outcome's `verdicts` are margins); `test_the_same_key_gives_the_same_sitting` (two runs on `draw.seeded(k)`: the outcomes are `==`).
- FALSIFIER and CONTROL: an end that fixes a band (HEAR_B's falsifier: a planted yielded sitting whose closing margin cannot land in two bands over 200 keys); a decider consulted in an automatic sitting. Control: with one speaker, one exchange and `decide=None`, the outcome's one margin equals `_speech`'s for the same key.
- GATE: `python -m pytest engine/season/tests/test_sc_proceeding_module.py -q` → pass; hash equal.
- HASH MOVERS: none.
- DEPENDS ON: V12 B24p.10.
- GLOSSARY: row *sitting* ("one meeting of a proceeding: one run of its exchanges and its close").
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B24p's producer; `Item: B24p.11`, `[skip ci]`.

### B24p.12 — the close, the odds, and the composition row · RD §A.5, §B.6 d · BUILD · HASH EQUAL
- SOURCE: RD §A.5 (the close by `disposal`, the ballot's formula, copied); A-14; B24.06 step 4 and B24.11 (the ballot's reading stays the host's); `references/module_contracts.yaml:48-56` (the composition row's form), `:464-480` (the stale contract row, INT E-17).
- ADVANCES: none at control; every verdict system of RD §C.3 has its draw.
- INSTRUCTION:
  1. `modules/social_contest/proceeding.py`: `_ballot_input(inp, state, d, ended) -> SocialContestInput`: `pool = d.pool`; `opposition = d.score`; `difficulty = type.difficulty`; operands `(("stakes", type.stakes, 1.0),)`; `leverage = track_step * state.track + d.lean + level(d.modifier) + presumption - ends - resist`, where `presumption` is `±level(presumption_level)` by `type.presumes`, `ends` sums `level(yield_level)`, `level(break_level)` and `level(strike_level)` per strike over the allowance against the side concerned (signed toward `for`), and `resist = resist_step * (d.will - mid)`; a level whose setting is `None` is 0. `_close(inp, state, ended, rng) -> tuple`: `exchange` → `((target id, the last drawn Exchange's Margin),)`; `none`, `mutual` → `()` (consent under `mutual` is a move, RD §A.5); every other value → one `roll(_ballot_input(...), rng)` per `inp.deciders` member in id order, one normal each; `adjourned` → `()`.
  2. `closing_odds(inp, state) -> tuple` (pure): per decider `(id, band_odds(pool, ob, boost))` on `_ballot_input` with `ended="budget"`.
  3. `references/module_contracts.yaml`: under `composition_roles`, `social_contest.proceeding: {target: "modules.social_contest.proceeding:proceed", entry: verb_call, verb: argue, needed_by: "engine/season/seam/wrappers/sigma.py — the provider path for a verb row carrying `proceeds:` (B24p.14)"}`; in the contract row `module: social_contest`, delete the `persuasion_track` state row (the module keeps no state) and set `resolver: d_sigma` (B05.04's name) `[ASSUMPTION: the rest of that row is B24.33's to repoint]`. Re-derive the composition artifact with `python tools/export_composition.py` (never by hand), then `--check`.
  4. The module-side binding check of B24p.05: `LEVERAGE` and `TERMS` keys equal the `bound: module` roster members.
- WHERE: `modules/social_contest/proceeding.py` (`_ballot_input`, `_close`, `closing_odds`); `references/module_contracts.yaml`; the exporter's artifact, re-derived; `engine/season/tests/test_sc_proceeding_module.py`, `test_sc_proceeding_data.py`.
- TESTS: written first and read red: `test_a_ballot_is_a_draw_on_the_voter` (a decider's margin moves with his own `pool`, `lean`, `will` and the track, and with no speaker attribute once the track is fixed); `test_exchange_disposal_ballots_nobody` (the verdict is the exchange's own margin, `is` the same `Margin`); `test_hearers_are_each_balloted_once_in_id_order` (twelve hearers: twelve verdicts, ids sorted; `assert checked == 12`); `test_closing_odds_match_the_ballots_drawn` (20,000 keyed ballots on one board sit within three standard errors of `closing_odds` per band: an approximation claim, so a tolerance is honest); `test_the_module_tables_equal_the_roster` (B24p.05's second half).
- FALSIFIER and CONTROL: a close that returns a band or a side; a `yielded` sitting whose ballot is certain. Control: with `track_step` 0 and every end level `None`, a ballot equals `roll` on the decider's own record.
- GATE: `python -m pytest engine/season/tests/test_sc_proceeding_module.py engine/season/tests/test_sc_proceeding_data.py -q` → pass; `python tools/export_composition.py --check` → exit 0; `python -m pytest tests/valoria/test_engine_does_not_import_systems.py -q` → pass; hash equal.
- HASH MOVERS: none (the role is registered and no prize row names it until B24p.19).
- DEPENDS ON: V12 B24p.11; V12 Batch B03-hygiene (`tools/export_composition.py`); V12 Batch B05 (B05.04 `d_sigma`; B05.21 `stakes`); EXISTS-IN-TREE `references/module_contracts.yaml: composition_roles`.
- GLOSSARY: row *track* ("the running position of the proposition before those who decide; it enters each ballot as leverage").
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B24p's producer; `Item: B24p.12`, `[skip ci]`.
