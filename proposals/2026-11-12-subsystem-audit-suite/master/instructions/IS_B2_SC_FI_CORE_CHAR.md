# Instruction suite, lane IS-B2 — social contest (SC), fieldwork (FI), the season core (CORE) and the character (CHAR) as standalone playable games

## Status: PROPOSED (stage 4 of `STAGES.md`, lane IS-B2 of `master/INSTRUCTION_SUITE_ORDER.md`; batch-shaped instructions for workplan v12; nothing here is applied; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Read at: `b07fc1c` (working tree of branch `ccr-62958c70-0kjhsw`, 2026-11-12). Producer: Fable, lane IS-B2. One round; no second wave. Parts: this file (§0 frame, §1 SC, §2 FI) and `IS_B2_SC_FI_CORE_CHAR_part2.md` (§3 CORE, §4 CHAR, §5 the tables v12 takes, §6 what was not checked).

## 0. What this file is, and how an item is read

**What it is.** For each of four subjects it states what has to execute for the subject to count as a
standalone playable game, in what order, through which batches of `unified/U3_DEPENDENCY_ORDER.md` (U3),
and it carries the items no proposal carries: the gaps of `unified/U4_TRACEABILITY.md` §6 that fall in
this lane (G-3, G-4, G-6, G-10, G-11, G-13), the INCOMPLETE rows of `unified/U4_DOCUMENT_STATUS.md` §3.4
for SC, FI, CORE and CHAR, and the holistic audit's findings where they bear on a scenario
(`master/HOLISTIC_AUDIT*.md` H-01, H-02, H-05; `master/CODEBASE_IMPROVEMENT_PROPOSAL*.md` CI-03, CI-06,
CI-07, CI-11). It does not restate a proposal's edits: an item that points at a proposal names the file
and adds only what is missing.

**Words.** `unified/U1_GLOSSARY.md` and ruling A-98: an *attribute* is one of the ten on the 1 to 7
scale; a *skill* is a learned rank (the tree's identifier is `capability`, kept in backticks); a person's
number in a skill is his *skill score*; the chooser's valuation of a candidate is a *choice score*;
*training* is the act of learning only. A *scenario* is a standalone playable setup of one subsystem; a
*setting* is a `Fixtures` field; a *switch* or *dial* is a setting with a control value; a *pin* is a
recorded hash a test compares; a *mover* is an edit declared to change seeded results; the *act-count
instrument* is `engine/season/harness/aperture.py`. "Check" is used in prose for a proposal's execution
artifact; the item form's field keeps the order's label GATE.

**The item form** (the order's): `Item:` handle · what it advances · INSTRUCTION (ordered edits at the
single owner) · WHERE (the edit set) · FALSIFIER and control · GATE (an execution artifact and its
expected reading; never a document) · hash movers · depends on (each marked EXISTS-IN-TREE, PROPOSED or
MISSING) · lane tag · batch it joins · cost class and model tier (CLAUDE.md §10) · what lands it. Handles
are `IS-B2-SC-nn`, `-FI-nn`, `-CORE-nn`, `-CHAR-nn`. Three kinds of item, said in each head:
**POINTER** (a proposal carries the edit; the item adds a reading, an order or a check), **NEW** (no
proposal carries it; the instruction is complete here), **BLOCKED** (the missing part is not decidable
from the repository; the blocking reason, its owner and the dormant form that lands meanwhile are
stated).

**A standalone scenario is a world, not a mode.** `proposals/11_GO_fidelity_and_campaign_modes.md:124`
(as `unified/U4_TRACEABILITY.md` §3 quotes it): *"There is no separate skirmish mode code path: a scenario
is a world."* So in every section below a scenario is four things and nothing else: (1) a **builder** (a
function returning a `World`); (2) a **verb set** handed to the chooser's composition, which is how a
neighbour is stubbed at its declared interface: `engine/season/decision/choose.py::make_chooser(fx, mint,
verbs=None, draw=None)` narrows the option set and `engine/season/harness/probes.py::chooser(w, only=None,
verbs=None)` composes it (opened at `choose.py:488`, `probes.py:278`); (3) the **seated person** (the
player, or the chooser standing in for one through
`engine/season/harness/play_surface.py::dispatching_chooser`, `:47`); (4) **end predicates** read by an
instrument over existing state and stored nowhere. A neighbour's product that the scenario needs
(an exhibit, a seat, a wound, a store) is state the builder plants through the write gate; a neighbour's
module is either left out of the verb set or reached unchanged by its composition row. No stub module is
written and no module is forked.

**What exists today, measured by this lane at `b07fc1c`, `PYTHONHASHSEED=0`** (the baseline every item's
"today" cites; each batch re-reads it on its own base, STAGES practice 1):

| reading | command | result |
|---|---|---|
| the nine | `python -m engine.season.harness.register --requirements` | `met 3 · not_met 1 · partial 5` (R-01 to R-03 met; R-05 not met) |
| one realm season, seed 0 | `python -m engine.season.harness.aperture 1 0` | control line `populated.run acts 749 vs measured 749; content_hash EQUAL`; TOTAL attempted 821, executed 490, refused 377 |
| SC verbs in that season (attempted / executed) | same run, PER VERB | `argue` 10 / 3; `tell` 20 / 4; `lie` 6 / 2; `speak` 8 / 1 (7 `speech.unheard`, last read `exists:DocketItem=0`); `open_case` 11 / 6; `petition` 12 / 12; `carry` 4 / 2; `determine` 1 / 0 (refused, `clause:docket`); `covenant` 3 / 0; `exchange` 15 / 0 |
| FI verbs in that season | same run | `research` 33 / 33 (24 graded losses); `surveil` 20 / 20; `reconstruct` 47 / 45; `interview` 19 / 5; `thread_read` 2 / 2; `examine` formed by 1 person, attempted 0; `forge` 31 / 16; `conceal` 11 / 11 |
| pools rolled | same run, POOLS ROLLED | `argue`, `lie`, `research`, `speak`, `surveil`, `tell`: pools `[2]`; *"two actors at different pools: no"* on all six |
| entries that exist | `python -m engine.season.harness.headless --help`; `ls engine/season/harness/` | `headless` takes `--case --seasons --seed --log` only; the harness holds no `scene.py`, `scenarios.py`, `play.py` or `valley.py`; `modules/social_contest/` holds `roll.py` only and `modules/fieldwork/` `find.py` only |

Nothing in the table is a target. It says that at this tree no person has been offered a choice inside a
hearing or an inquiry by any entry, that a bench's `determine` did not execute in the one season read,
and that every social and inquiry roll was thrown at the same pool. (`aperture 1 0` only; longer runs
were not made, §6.)

**The shared spine** (every subject below stands on it; from U3 §1 and §2.1, with the improvement
proposal's additions): B00 ids → B01 lane A → B02 tests (with CI-11's `ENGINES` reading) → B03 hygiene
(with CI-10, CI-08, CI-03, CI-04, CI-05, CI-06) → `B03a-prose` (CI-01, CI-02) → B04 the skill authoring
surface → B05 the one roll → B06 the keyed draw → B07 the task draw → B08 scene order → B09 memory → B10
character. After B10 the four subjects fan out by lane: FI (B11, B25, B26), SC (B24, B27, B28), GO for
the shared runner (B34), IN and WR for cases (B39).

**The two shared carriers of "playable", both in B34** (owned by IS-B3's GO section; cited here, not
restated): `proposals/01_CORE_one_scene_contract.md` Edit 4, `python -m engine.season.harness.scene <role>
--fixture <name> --seed S` (one module's scene instance, alone, through `seam.contest`), and
`proposals/11_GO_player_surface_contract_B.md` §8, `python -m engine.season.harness.play_surface --seed S
--person P --seasons K [--scenario NAME]` (the transcript: what is asked, what is offered, the pick, the
account). B34 is wave W11; B11 and B24 land before it. Each subsystem section therefore names a **first
entry** that exists at its own batch and the **shared entry** it is re-read through at B34
(`IS-B2-CORE-01` makes the two resolve one scenario name).

---

## 1. SC — social contest

### 1.0 The standalone-playable test for SC

A hearing is a standalone playable game when a person seated at it (a party, an advocate or a bench
member) can enter a sitting, choose what to present, answer, argue, impugn, concede or rest, see the
board change by his choices, and reach a verdict that the world then carries; and the same
`social_contest.hearing` entry is what the season calls at ENCOUNTER when a bench's `determine` comes up
in computed play. A negotiation is the same entry under a `disposal: mutual` row.

| part of the test | what it is for SC | carrier | exists today |
|---|---|---|---|
| **entry** | first: `PYTHONHASHSEED=0 python -m engine.season.harness.headless --world hearing --seed S [--auto \| --play <person id>]` (`05_SC_playable_hearing_B.md` edit 9, B24). Shared, at B34: `harness.scene social_contest.hearing --fixture hearing` and `harness.play_surface --scenario hearing` | HEAR_B edit 9; `01_CORE_one_scene_contract.md` Edit 4; `11_GO_player_surface_contract_B.md` §8 | no (`headless` has no `--world`) |
| **scenario** | `engine/season/harness/governance_spine.py::build_hearing(seed)`: a fired sitting, a named arrangement row, a bench, two parties each with three filed exhibits. Seeds 0 to 2 for hashes; 200 seeded sittings on each of three hands for the stationary-menu run | HEAR_B edit 9, gates 2 and 5 | `governance_spine.build(seed)` and `census(w)` exist (`:93`, `:181`); `build_hearing` does not |
| **verb set (the stub contract)** | `speak`, `determine`, `argue`, `tell`, `lie`, `petition`, `carry`, `open_case`, `commit`, `utter`, `give`; nothing else is offered. FI is stubbed by planted state: each party's exhibits are Records and claims the builder writes (no inquiry verb runs). FA is stubbed by the bench's seats, built with `remit: determine`. PC and MB are not in the set, so `seam.contest` is entered at depth 0 only. WR and SE run as MATTER runs them. CHAR supplies each NPC's decider (`IS-B2-CHAR-02`) or the module's named interim policy. DICE is not stubbed: the one roll | §0; HEAR_B "Who decides" | the verb narrowing exists (`probes.chooser(verbs=)`) |
| **player-facing surface** | on entry: the arrangement, the rung tried and who bears it, the disposal each degree opens, his filed exhibits, the bench's public commits; each turn: the board, his hand, his effort, the legal moves, his believed chance (HEAR_B "What a player sees"); as records: `HearingTurnView` and the scene pair of `11_GO_player_surface_contract_B.md` §6 | HEAR_B; GO-B §6, §8 | no |
| **stop conditions (ending kinds)** | **carried**: `determine` at Overwhelming or Success, the disposal opens at full degree (the petitioner's win, A-38); **carried in part**: Partial, the disposal at its lower degree and a subsidiary matter named; **dismissed**: Failure, the case file gains a `failed` stage and the accused is acquitted for the present (`05_SC_acquittal.md`, B27; the petitioner's loss); **adjourned**: the bench holds the stage to the next sitting, and `matter.lapsed` closes a matter held past `docket_lapse` seasons (a draw). Negotiation: **agreed** (each party's own `oblige`) or **parted** (all rest; the exchanges are on the case file) | HEAR_B; `05_SC_acquittal.md`; `05_SC_negotiation_scene.md` | `matter.determined` and `matter.lapsed` exist; acquittal does not |
| **never a dead end, the world moves** (A-80, A-81) | every ending writes: the exchange list on the case file (HEAR_B edit 7), the disposal Tenure or the `failed` stage, and what each attendee witnessed. A held position is not stillness: a dismissed accuser keeps his claims and may appeal on new grounds (A-39, `19_LACUNA_verdict_ladder_and_reversal.md`) | `IS-B2-SC-08` adds the reading | no reading exists |
| **execution artifacts** | `engine/season/tests/test_sc_hearing_sitting.py` (seven named tests, HEAR_B "Named tests"); `test_sc_hearing_evidence.py`, `test_sc_hearing_admission.py`, `test_sc_hearing_negotiation.py`, `test_fi_evidence_interface.py`, `test_verdict_ladder.py`, `test_arrangements.py` (their proposals) | B24, B27 | none of these files |
| **integrated check** | in `build_realm(s)`, s = 0, 1, 2, two seasons: `determine` executes through `social_contest.hearing` at least once with at least one exhibit on file, and the role appears in CI-11's `ENGINES` block | `IS-B2-SC-09` | today `determine` 1 attempted, 0 executed at seed 0, one season |

**One code path.** Holds by construction if HEAR_B gate 1 and gate 4 read as written: with no exhibits and
effort 0 the sitting is today's `roll`, and a scripted player echoing the NPC decider reproduces the
`--auto` hash. If gate 4's hashes differ there are two paths and B24 does not close.

**Order of execution for SC** (U3 handles; what each contributes to the test):

| step | batch | what lands for SC | SC reading recorded at its close |
|---|---|---|---|
| 1 | B03 | CI-03: `social_contest.obstacle` becomes a composition row (the host stops reaching the module by reflection, H-05) | `tools/export_composition.py --check`; roles 16 → 17 |
| 2 | B04 | `05_SC_capability_surface.md`, `05_SC_hearing_capabilities.md` (definition rows) | `tools/export_descriptors.py --check` |
| 3 | B05 | the one obstacle form and its calibration: `U5c_SC_one_obstacle_form.md`, `05_SC_obstacle_difficulty_and_modifiers_B.md`, `16_PESSIMIST_SC_A`, `05_SC_contest_record_on_event.md`, `13_SC_tuning_tables.md`, `13_SC_calibration.md`, `05_SC_opposed_obstacle_parity.md` | `aperture 4 0`: *"two actors at different pools"* (expected to stay "no" in the shipped realm until content lands, `IS-B2-CHAR-03`); `13_SC_calibration` C1 to C8 |
| 4 | B07 | `13_SC_draw_for_unrolled_contests.md` (surviving rows) | its own gate |
| 5 | B09, B10 | `16_PESSIMIST_SC_B_one_reader_of_a_ledger.md`; the chooser's sampler and `IS-B2-CHAR-02` (the contest decider) | B10's readings |
| 6 | B11 | `16_PESSIMIST_SC_E`; the FI readers the exhibits are made of | B11's readings |
| 7 | **B24** | `IS-B2-SC-02` → `IS-B2-SC-03` → HEAR_B → `19_LACUNA_admission_rides_the_citing_draw.md` → `05_SC_evidence_and_rebuttal_B.md` → `08_FI_05_evidence-interface_B.md` → `hearing_moves` → `05_SC_negotiation_scene.md` edits 1 to 5 → kernel disposition → `12_ARCS_cited_evidence.md` → `02_CHAR_which_ground_moves_whom.md` → `IS-B2-SC-08` → `IS-B2-SC-09` | HEAR_B gates 1 to 5; **the standalone test above reads true here for the hearing** |
| 8 | B27 | `05_SC_acquittal.md`, `05_SC_arrangement_rows_that_bind.md`, `16_PESSIMIST_SC_C`, `_D`, the residue, `19_LACUNA_verdict_ladder_and_reversal.md`; `IS-B2-SC-07` (its B27 row) | the dismissed ending exists; A-80's control in `test_arrangements.py` |
| 9 | B28 | `14_VERBS_SOCIAL1_B` (the `covenant` reader), `_D`, `_C`; scene access A and B; `IS-B2-SC-05` (the negotiation's opening) | the negotiation is reachable by a computed act |
| 10 | B34 | the shared runner and transcript | `harness.scene social_contest.hearing --fixture hearing` equals step 7's `--auto` hash |

### 1.1 Items

**Item: IS-B2-SC-01** · POINTER · advances: the scale *social contests / debates* (`engine/season/requirements.yaml` `scales:`, `in_loop: "seam unbuilt"`), R-04, R-09.
- INSTRUCTION: (1) v12 schedules the ten steps of §1.0 in that order and writes, in each batch's close, the SC reading the table names (a reading with its command, seed and tree, never a count in a pointer index). (2) At B24's close, and only if `IS-B2-SC-09`'s reading is above zero, edit the `scales:` row `social contests / debates` in `engine/season/requirements.yaml`: `in_loop:` becomes the measured sentence (the command, the seeds, the count of `determine` acts resolved through `social_contest.hearing`); its `note:` loses the sentences about the kernel, which `05_SC_sc05_kernel_disposition_B.md` retires in the same batch. (3) Nothing else moves a status by writing (`01_CORE_requirements_reading_record.md` head).
- WHERE: v12's requirement map; `engine/season/requirements.yaml` (`scales:` row 3), once, in B24's last `Item:` commit.
- FALSIFIER and control: the row is edited while `IS-B2-SC-09` reads 0 at all three seeds (a status moved by writing). Control: `python -m engine.season.harness.register --requirements` prints the same nine statuses before and after (the `scales:` block carries no status the count reads).
- GATE: `register --check` green; the row's sentence reproduces by its own command.
- Hash movers: none. Depends on: B24 (PROPOSED). Lane: SC. Batch: B24 (close). Cost: edit; `sonnet`. Lands it: B24's close.

**Item: IS-B2-SC-02** · NEW · advances: SC and FI standalone (the case file as the board); narrows four INCOMPLETE rows coded DEP-v11 on CR-61 (`19_LACUNA_admission_rides_the_citing_draw.md`, `05_SC_evidence_and_rebuttal_B.md`, `05_SC_acquittal.md`, `14_VERBS_SOCIAL2_C_case_question_confession.md` §1).
- What is missing, and why it is decidable now. Those files wait on workplan v11's CR-61 (`workplans/valoria_master_workplan_v11_part4.md:556`), a position with five parts and a chain of predecessors (CR-60, CR-57, CR-48). Opened at the lines that name it, what these four read of it is one fact: **the docket item names its case file** (`05_SC_acquittal.md:71-74`; `14_VERBS_SOCIAL2_C…:65`; EVID_B `:184`; `19_LACUNA_admission…:7`). `[ASSUMPTION: no other part of CR-61 is read by these four — basis: a search of each file for CR-61 and "case file", not a full read of EVID_B's 262 lines; the landing session confirms at EVID_B edit 4.]` Two neighbours need more and are not claimed: `U5c_SC_proceedings_residue.md` §3 needs the case file to name its matters, and EVID_B also waits on v11's SC-02 (the re-source of `reception` and `proofs`, HELD); both are in `IS-B2-SC-10`. In the tree `_eff_open_case` mints the case file and writes the docket item in one `apply` (`engine/season/loop/effects_information.py:367-442`), the minted id is known there (`_mint_document`: `rid = d.get("record") or f"rec:{a.id}"`), and the item's shape has one owner (`_docket_item`, `:196-202`) with two keys already added by this route (`world_q.DOCKET_ARRANGEMENT`, `DOCKET_PETITION`, `engine/season/queries/world_q.py:236-237`). The rest of CR-61 (the `case` Record kind, the fifth `determine` conjunct, `forge` on `case`, the citation writ) stays CR-61's and is dispositioned by `STAGES.md` step 5.
- INSTRUCTION, in order: (1) `engine/season/queries/world_q.py`: `DOCKET_CASE = "case"` beside `DOCKET_PETITION`; a reader `case_file_of(w, item) -> Optional[str]` returning `item.get(DOCKET_CASE) or item.get(DOCKET_PETITION)` (a carried petition is its own file, `05_SC_acquittal.md:71`). (2) `engine/season/loop/effects_information.py::_docket_item(matter, arrangement, petition, date=None, case=None)` writes the key; `_eff_open_case` passes the minted record's id; `_eff_carry` passes `None`. (3) `engine/season/write_matrix.yaml`: one `DocketItem` row for `case` beside the `arrangement` and `petition` rows (`:133-145`), writer `open_case`. (4) `engine/season/verb_table.yaml`: `open_case` `writes:` gains `DocketItem.case`. (5) Every site the six proposals name as "the docket item's case file" calls `case_file_of`; none reads the key directly.
- WHERE: `queries/world_q.py`, `loop/effects_information.py`, `write_matrix.yaml`, `verb_table.yaml`; new tests in `engine/season/tests/test_docket_names_its_case_file.py`.
- FALSIFIER and control: `test_an_opened_case_names_a_record_that_exists` (for every docket item after `open_case` at seeds 0 to 2, `case_file_of` is a key of `w.records`, with `assert checked >= 1` per seed); `test_a_carried_petition_is_its_own_case_file`; control `test_a_slot_calendar_formed_names_no_case` (an unfilled slot reads `None`). Fails if two docket items name one case file, or an item names a Record that is not on anyone's `hold`.
- GATE: the three tests green; `python -m engine.season.harness.aperture 1 0` prints `open_case` executed at its opening count (6 at `b07fc1c`), unchanged.
- Hash movers: **declared mover** on every world in which `open_case` executes (the item gains a key; the precedent is SC-03a's, recorded in `_eff_open_case`'s docstring, `:413-414`). Re-pinned once, in B24's last `Item:` commit.
- Depends on: `_docket_item`, `_mint_document`, the two `DOCKET_*` keys (EXISTS-IN-TREE); CR-61 whole (MISSING: a v11 position; if step 5 carries it ahead of B24, this item is its first commit and is not landed twice).
- Lane: SC. Batch: B24, first item. Cost: edit; `sonnet` (`high`). Lands it: B24's `valoria-author`.

**Item: IS-B2-SC-03** · NEW · advances: SC standalone (HEAR_B edits 3 and 6, the row's reading, stop waiting on CR-60).
- What is missing. HEAR_B edit 3 says *"Until CR-60, one default rite carries them"* and leaves the default unwritten; edit 6's reading of the rite is marked not decidable for want of CR-60 and CR-61. The second wait is closed by `IS-B2-SC-02`. The first is closed by writing the default as data now; CR-60's two-valued block (`accusatorial`, `inquisitorial`, v11 part 4 `:543`) later replaces the one row without touching the reader.
- INSTRUCTION, in order: (1) `engine/season/arrangements.yaml`: a top-level block `rites:` with one row, `default`, keys `bears:` (`{procedure: against, fact: against, definition: against, justification: for}`, sides as HEAR_B's `Exhibit.side`), `moves:` (the six `hearing_moves` plus the bench's `rule` and `adjourn`), `faults:` (the four `hearing_faults`), `disclosed: true`, `order: alternating`. `[ASSUMPTION: the accuser bears fact and definition and the party bears justification — basis: the issue ladder HEAR_B carries from the kernel (`audits/05_SC_audit_addendum_B.md:242`, `:246`: "who bears the question … carry as the row's `bears:` map"); the tree holds no ruled assignment; reversible by editing the row.]` (2) `engine/season/data/arrangements.py`: the loader reads `rites:`, refuses a move or fault that is not a roster member and a `bears:` key that is not an `issue_rungs` member; an arrangement row may name `rite:`, default `default`. (3) `seam/wrappers/sigma.py::hearing_input` (HEAR_B edit 6) reads the rite of the docket item's arrangement row, and `default` where the item's arrangement is `None` (every computed case today: `_eff_open_case`'s docstring, `:413`). (4) A mutual row (`negotiation`) keeps `bench_basis: none`; its rite adds `offer` and `accept` (`05_SC_negotiation_scene.md` edit 1).
- WHERE: `arrangements.yaml`, `data/arrangements.py`, `seam/wrappers/sigma.py::hearing_input`; tests in `engine/season/tests/test_sc_hearing_sitting.py`.
- FALSIFIER and control: `test_a_computed_case_is_heard_under_the_default_rite`; `test_a_rite_naming_an_unrostered_move_is_refused` (planted); control: with `sitting_exchanges` 0 the rite is read by nothing and `build_realm` hashes at seeds 0 to 2 are EQUAL (HEAR_B gate 1).
- GATE: HEAR_B gate 2 (`headless --world hearing --seed 0 --auto`, twice, one hash) runs on the default rite.
- Hash movers: none at `sitting_exchanges` 0. Depends on: HEAR_B edits 1, 4, 5 (PROPOSED, B24); `issue_rungs`, `hearing_moves`, `hearing_faults` (PROPOSED, HEAR_B edit 1); CR-60 (MISSING: v11; replaces the row later).
- Lane: SC. Batch: B24, after HEAR_B edit 1, before edit 6. Cost: small build; `sonnet` (`high`); the `bears:` row is read once by the batch's `opus` design pass with `ners`. Lands it: B24.

**Item: IS-B2-SC-04** · POINTER · advances: SC standalone (HEAR_B edit 8, the NPC's decider; `05_SC_negotiation_scene.md` "How each side chooses").
- INSTRUCTION: the decider is built by `IS-B2-CHAR-02` (one builder in `engine/season/decision/`, B10). B24 adds the hearing's two inputs to it and nothing else: (1) `key="hearing_move"`, a `choice_sourced`-shaped key whose values are the `hearing_moves` roster (so `02_CHAR_choice_alignment.md`'s `choices:` block may carry a cell per move); (2) `odds=` the module's pure `closing_odds(inp, standing)` evaluated on the board each legal move would leave, weighed by what each degree's disposal means to the person (HEAR_B "Who decides"). The wrapper (`sigma.py`), not the module, resolves the decider (`01_CORE_one_scene_contract.md` Edit 3). The move's cost terms HEAR_B lists (an item exposed, an enemy made, a concession witnessed) stay that file's design pass.
- WHERE: `seam/wrappers/sigma.py` (the `@provider` path of HEAR_B edit 6).
- FALSIFIER and control: HEAR_B gate 5 (no constant decider best on all three hands) and gate 4 (the echo). Control: with no cell authored and `closing_odds` flat, the decider's pick is the sampler's draw over equal choice scores.
- GATE: `test_sc_hearing_sitting.py::test_no_constant_decider_wins_on_all_three_hands`.
- Hash movers: with `sitting_exchanges` above 0 only (HEAR_B's declared mover). Depends on: `IS-B2-CHAR-02` (NEW, B10); HEAR_B (PROPOSED). Lane: SC. Batch: B24. Cost: small build; `sonnet`, the cost terms `opus` with `ners`. Lands it: B24.

**Item: IS-B2-SC-05** · NEW (decided by the ladder, reversible) · advances: SC standalone (the negotiation is reachable by a computed act); closes the DESIGN half of `05_SC_negotiation_scene.md` edit 6.
- What is missing. Edit 6 leaves the opening verb undecided between a new row `treat` and `petition` to a person, and hands it to v11's CR-63. Neither was checked against the row the tree already has for offering terms in person: `covenant` (`engine/season/verb_table.yaml`: `counterparty: to`, `requires` a Person and *"the terms are an uttered Proposition"*, `emits: covenant.offered`), whose in-force reader and breach `14_VERBS_SOCIAL1_B_documents_and_obedience.md` §3 builds in B28.
- Decision (ladder step 4, precedent; step 2 for the alternative): **the negotiation is opened by `covenant`.** A-21 keeps covenants in person, which a sitting is; the row already names the two parties and the terms; the verb roster was just fixed at 68 by A-28 and CLAUDE.md §4 forbids coining where a word exists, so `treat` is not added; `petition` addresses a person from a place and writes a petition Record, which is an ask, not an offer of terms. `[ASSUMPTION: `covenant` is the opening act — basis: the row as it stands and SOCIAL1_B §3; revert: a row `treat`, which moves the verb roster and needs an operand vocabulary entry (H-94 closes it).]`
- INSTRUCTION, in order (B28, after SOCIAL1_B §3): (1) `engine/season/rosters.yaml`: the prize a `covenant` contests under a `disposal: mutual` arrangement row carries `module_entry: social_contest.hearing`, `step: "ENCOUNTER"` (the pair HEAR_B edit 1 gives `a verdict`). (2) `verb_table.yaml: covenant`: the drafting draw SOCIAL1_B §3 defines stays the row's draw; at Success or better the offered Record's `terms` become the opener's standing `offer` on the board of a sitting with the counterparty (`HearingInput.closing = None`, no bench). (3) `seam/wrappers/sigma.py::hearing_input`: for a mutual row the speakers are the maker and the `to` of the covenant Record. (4) The end stays as `05_SC_negotiation_scene.md` writes it (each party's own act), and the agreement's in-force reading is SOCIAL1_B's `covenant_in_force`; where the two files differ on the binding Tenure (`oblige` in the negotiation file, a `commit` on the terms in SOCIAL1_B), **SOCIAL1_B's `commit` governs** for a covenant and the arrangement row's `disposes: oblige` stays for a bench-less row that names it: the negotiation file's edit 5 writes the kind its row's `disposes:` names, never a fixed kind. (5) Scene access: the counterparty is engaged for the round (`28_CORE_scene_access_A` §2).
- WHERE: `rosters.yaml` (prize row), `verb_table.yaml: covenant`, `seam/wrappers/sigma.py`, `loop/effects_information.py` (the negotiation file's edit 5); `engine/season/tests/test_sc_hearing_negotiation.py`.
- FALSIFIER and control: a new test `test_a_computed_covenant_opens_a_negotiation` (a planted seat-holder with an uttered Proposition and a counterparty present forms `covenant`; the sitting runs; either `covenant_in_force` reads above 0 or the case file holds the parted exchanges). Control: `sitting_exchanges` 0 leaves `covenant` the single draw SOCIAL1_B defines. Falsified if the opener's draw, not the counterparty's own act, makes the agreement.
- GATE: that test; `aperture 2 0` shows `covenant` executed above its opening reading (0 of 3 attempted at `b07fc1c`, one season).
- Hash movers: declared, wherever a `covenant` executes with `sitting_exchanges` above 0. Depends on: `14_VERBS_SOCIAL1_B` §3 (PROPOSED, B28); `05_SC_negotiation_scene.md` edits 1 to 5 (PROPOSED, B24); CR-63 (MISSING, v11; no longer needed for this edit).
- Not settled here: `covenant` is seat-gated (`eligibility: remit:issue`), so two unseated persons cannot open one; whether that is wanted is SOCIAL1_B's row to say.
- Lane: SC. Batch: B28, after `14_VERBS_SOCIAL1_B`. Cost: small build; `sonnet`, with the batch's `opus` read of step (4). Lands it: B28.

**Item: IS-B2-SC-06** · BLOCKED · advances: SC standalone (a negotiated exchange of stores).
- Blocking reason. `05_SC_negotiation_scene.md` marks `exchange`'s operands *"no carrier in the suite"*. Opened: the `exchange` row needs six operands (`from`, `to`, `kind`, `amount`, `return_kind`, `return_amount`) and writes `Rung.stores` twice, so its two sides are **rungs' stores**, not two persons'; in one realm season it was attempted 15 times and executed 0 (last reads `stores:grain=0`, `stores:salt`). Which person's act may move a rung's stores toward another rung under an agreed term is the stores lane's (`14_VERBS_MATERIAL_B_stores.md`, B12) and not decidable from the SC side.
- Owner: SE (MATERIAL_B) names the act and its operand source; SC then adds `Offer.stores`.
- Dormant form that lands: `Offer.stores` is `None`; an offer carries an obligation term only (`05_SC_negotiation_scene.md` edit 2 with `stores` absent). Named test already in that file: `test_each_oblige_is_opened_by_its_own_partys_act`.
- GATE when unblocked: an accepted offer with a stores term is followed, in the same round's MATTER, by one `exchange.made` whose actor is the giving party, or by `exchange.refused` and a broken agreement. Hash movers: declared then. Lane: SC (edit), SE (owner). Batch: none until SE names it; then B28. Cost: design-first; `opus` with `ners`.

**Item: IS-B2-SC-07** · NEW (the carry text is `unified/U4_TRACEABILITY.md` G-13) · advances: A-27 (a construal is testable by a court against the terms); FI and SC integrated.
- INSTRUCTION, in order: (1) B25: an edit 5 to `14_VERBS_SOCIAL2_B_a_word_with_content.md` §2: a construal's Proposition (`prop:{act id}`, minted by `_mint_proposition`) is citable at a sitting as an exhibit beside the writ's `terms` Proposition. (2) B27: one gate row in `05_SC_arrangement_rows_that_bind.md`: the sitting's one comparator (`LedgerReader`) grades the two, and a construal that contradicts the terms is answered by the rules of `05_SC_evidence_and_rebuttal_B.md` (excluded by the answering draw's degree, never struck with certainty).
- WHERE: `engine/season/loop/effects_information.py` (the citing `speak`'s admitted kinds), `engine/season/rosters.yaml: proofs`; test `engine/season/tests/test_vm_s2_b_word.py::test_a_construal_contradicting_the_terms_loses_at_the_bench`.
- FALSIFIER and control: the construal that contradicts the terms carries at the bench as often as one that agrees (200 seeded sittings; the two shares must differ). Control: a construal equal to the terms forms no act (S2-B `:204`).
- GATE: the named test. Hash movers: none until a bench convenes on a construal.
- Depends on: `14_VERBS_SOCIAL2_B` §2 (PROPOSED, B25); EVID_B (PROPOSED, B24). Lane: FI (step 1), SC (step 2). Batch: B25 and B27. Cost: small build; `sonnet`, the contested degree `opus`. Lands it: B25, then B27.

**Item: IS-B2-SC-08** · NEW · advances: A-81 (no scene is still) and A-80 (a held position moves the world), read for the hearing at the batch that builds it rather than at B38.
- What is missing. HEAR_B's gates show the sitting runs and that choices matter; none reads that **every ending writes**. `adjourn` (the bench holds the stage) and a Failure before B27's acquittal are the two endings whose write is not stated in a gate.
- INSTRUCTION, in order: (1) `engine/season/harness/governance_spine.py`: `hearing_ending(w, matter) -> str`, a reader over the log and the case file returning one of `carried`, `carried_in_part`, `dismissed`, `adjourned`, `lapsed`, `agreed`, `parted`; computed, stored nowhere. (2) `headless --world hearing` prints one summary line per run: the ending, the tick, the count of exchanges, and the count of durable writes the sitting's Events made (case-file stages, Tenures opened or closed, claims deposited to attendees; the budget debit excluded, A-81). (3) `adjourn` writes one `adjourned` stage to the case file under the bench member's own act (HEAR_B edit 7's carrier), so the next sitting reads it. (4) The entrenched arm: the same fixture with every party's `argue` and `answer` returning Failure (a planted generator); the reading is that the run still ends by one of the seven kinds and writes.
- WHERE: `harness/governance_spine.py`, `harness/headless.py`, `loop/effects_information.py::_eff_determine`; `test_sc_hearing_sitting.py`.
- FALSIFIER and control: `test_every_ending_of_a_sitting_leaves_a_durable_write` (seeds 0 to 19, `--auto`; for each run the write count is above 0, and `assert` that at least three ending kinds occurred across the twenty, so the loop cannot pass by one kind); `test_an_adjourned_stage_is_read_by_the_next_sitting`; control `test_a_sitting_with_its_case_file_writes_suppressed_counts_zero` (the counter can read zero).
- GATE: those tests; the summary line at seeds 0 to 2 recorded in B24's close, and again at B27's close with `dismissed` now reachable.
- Hash movers: step (3) only, where a bench adjourns with `sitting_exchanges` above 0 (inside HEAR_B's declared mover).
- Depends on: HEAR_B edits 7 and 9 (PROPOSED). Lane: SC. Batch: B24, after HEAR_B edit 9. Cost: small build; `sonnet`. Lands it: B24. Later: `30_WR_E`'s `null_scenes` (B38, and `IS-B2-CORE-03`) reads the same writes realm-wide.

**Item: IS-B2-SC-09** · NEW · advances: SC integrated (the hearing is reached by computed play; H-01's question asked of the role before the batch closes).
- What is missing. HEAR_B's gates run a fixture. In the realm a bench's `determine` did not execute in the season this lane read (1 attempted, refused at `clause:docket`; `speak` 1 of 8, seven `speech.unheard`). A hearing no computed act reaches is the holistic audit's H-01 for one more role.
- INSTRUCTION, in order: (1) at B24's open, record `python -m engine.season.harness.aperture 2 s` for s = 0, 1, 2: `open_case`, `speak`, `determine` attempted, executed and the deciding read per refusal. (2) After HEAR_B edit 6: the same three runs, with CI-11's `ENGINES` block. Expected: `social_contest.hearing` entered at least once in at least two of the three seeds, and at least one `matter.determined` whose `ending` lists an exchange. (3) If the role is entered in none, the batch does not close on the fixture alone: the refusing clause is read from the run (`clause:docket` asks for *a fired Date with a DocketItem*, `verb_table.yaml: determine`), and the repair is made at that clause's owner (`world_q.slot_for`, `_eff_convene`'s Date, or the chooser's formation of `determine`), as its own `Item:` commit with its own test. No verb is special-cased and no docket is planted in the realm builder.
- WHERE: no file in steps (1) and (2); step (3) at the owner the reading names.
- FALSIFIER and control: the fixture's `--auto` run enters the role (the instrument can see an entry); the realm reads 0 at all three seeds after the edit.
- GATE: the `ENGINES` reading above, recorded in B24's close.
- Hash movers: step (3) if taken (declared then). Depends on: CI-11 (PROPOSED, B02); HEAR_B (PROPOSED). Lane: SC. Batch: B24. Cost: a reading; `haiku` for the three runs' extraction, `opus` if step (3) is taken. Lands it: B24. `[UNVERIFIED: this lane read one season at one seed; two seasons at three seeds is the item's first step.]`

**Item: IS-B2-SC-10** · BLOCKED (DEP-v11) · advances: SC standalone at full depth (the choices outside the room).
- Blocking reason. Five robust decisions outside the room (which proofs to offer, self or advocate, naming enemies, the warrant duty, appear or evade or defy) are v11's CR-63; the plea is CR-62; the rite's two values and church scope are CR-60; the `case` Record kind and the citation writ are CR-61; consent and appeal are CR-58, CR-59 (`workplans/valoria_master_workplan_v11_part4.md:517-596`, all STATE BUILD, none in the tree); the re-source of `reception` and `proofs` is SC-02 (v11 part 4 `:698`, HELD on its design's approval), which `05_SC_evidence_and_rebuttal_B.md` names; `U5c_SC_proceedings_residue.md` §3 (several matters on one case file) waits on CR-61's content keys. No suite proposal carries them and `05_SC_arrangement_rows_that_bind.md` edit 5 gates on that batch's close.
- Owner: `STAGES.md` step 5 (one disposition each). This lane's reading, for that evaluation: nothing in this session supersedes CR-58 to CR-64 except where `IS-B2-SC-02` (one key of CR-61), `IS-B2-SC-03` (CR-60's rite default), HEAR_B (the room; CR-62's plea becomes a rung conceded by the `concede` move) and `IS-B2-SC-05` (CR-63's opening verb for a negotiation) take a part; A-39 (appeal on new grounds only) narrows CR-59.
- Dormant form: the hearing plays on the default rite, a `text`-kind case file and the present `evade / defy` row; the scenario's verb set (§1.0) is what a party may do outside the room.
- GATE when carried: CR-63's own exit (each of the five taken above 0 at seeds 0 to 2). Lane: SC. Batch: a v12 batch after B24, named by step 5. Cost: as v11 states (third tier).
