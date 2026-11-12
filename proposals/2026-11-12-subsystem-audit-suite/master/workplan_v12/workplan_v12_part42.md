# Workplan v12 — part 42: Batch B39-procgen-and-cases

## Status: PROPOSED (a body part of workplan v12, drafted under `master/workplan_v12/`; unratified input to `methodology-execute`'s 0.1 stop until Jordan adopts v12, `V12_STRUCTURE_part3.md` §8; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Written against: the working tree at `59ddec1` (branch `ccr-62958c70-0kjhsw`), read 2026-11-12; author lane A42 of `master/workplan_v12/V12_STRUCTURE_part2.md` §4.2. Every item is written against the tree as B00 to B38 will leave it; where a symbol does not exist at `59ddec1`, the item says which batch makes it. Continued in `workplan_v12_part42_cont.md` (the items after `B39.17`, the readings, `B39.99` and the boundary row).

**What this part holds.** One WR batch, `B39-procgen-and-cases`: the world-generation switch and its tables (`21_PROCEDURAL_A` to `_E`), cases built on the realm with beats and controls (`01_CORE_case_setup_and_beats`, `12_ARCS_case_on_the_realm`), five owed story edits (`U5d_STORY_owed_edits`), a house that continues, a founded place that can fail and the lean year (`23_STORY_B`, `_C`, `_E`), the split parts other batches left here (`15_INSTITUTIONS_SYNTHESIS_B` §2, `15_INSTITUTIONS_COLONIAL_D`'s realm reading, `U5d_FA_owed_edits` §10, `30_WR_A`'s `minority` row, `17_CENSUS_C1B_02` W-2 as a named non-carry), and the intake's one entry (CR-85's hooks half, intake `:504` under the heading at `:502`).

**Words.** `unified/U1_GLOSSARY.md`. A person's numbers are an attribute, a skill and its skill score, a derived score (A-98); where copied source text says "skill ids" for the keys of a lifepath's `adds:` map, those keys are attributes, and the correction is said at the item. A *lap* is one pass of the season's scene budget; a *round* is one engagement of a fight (A-101); this batch's fight edit (`U5d_STORY_owed_edits` §5) speaks of an exchange inside a round. The tree identifier `capability` (and clause names built on it, `doer_capability_at_least`) is kept in backticks; prose says skill. "Bout" for an illness is "spell of illness" (glossary). Armies: unit, army formation, unit formation (A-99, the lexicon); a besieged place is under an `Invested` field.

**Paths.** As `V12_STRUCTURE.md` states: a bare path is under `proposals/2026-11-12-subsystem-audit-suite/`; `U3` is `unified/U3_DEPENDENCY_ORDER.md`; `the intake` is `master/eval/V12_INTAKE.md`. A path under `engine/`, `modules/`, `tools/`, `references/`, `tests/` is the repository's. `PROC_A` to `PROC_E` are `proposals/21_PROCEDURAL_A_worldgen_tables_and_ground.md` to `21_PROCEDURAL_E_names_and_texts.md`; `CORE_case` is `proposals/01_CORE_case_setup_and_beats.md`; `ARCS_case` is `proposals/12_ARCS_case_on_the_realm.md`; `STORY_B`, `_C`, `_E` are `proposals/23_STORY_B_a_house_continues.md`, `23_STORY_C_a_founded_place_can_fail.md`, `23_STORY_E_first_playable_the_lean_year.md`; `U5d_STORY` is `proposals/U5d_STORY_owed_edits.md`; `SYN_B` is `proposals/15_INSTITUTIONS_SYNTHESIS_B_the_deed_ledger.md`; `COL_D` is `proposals/15_INSTITUTIONS_COLONIAL_D_accomplishment.md`.

**How this part was assembled.** U3 §1 item 39 and §1.2's B39 row give the order: `PROC_A` → `_B` → `_E` → `PROC_C` → `CORE_case` → `ARCS_case` → `PROC_D` → `U5d_STORY` → `STORY_B` → `STORY_C` → `STORY_E` → the split parts. Each source's own commits are items (`V12_STRUCTURE_part2.md` §5.5). Four places differ from U3's order, each for a reason a source states, and each is in the block's `UNDECIDED` line: `PROC_C` is two items, its prologue (PG-4) in U3's place and its case seeds (PG-5) after `PROC_D`'s card receiver, because PG-5 adds rows to the file PG-6 creates and uses the clause roster PG-6 owns (`PROC_C` "Depends on": "`21_PROCEDURAL_D` … the card loader"); `U5d_FA_owed_edits` §10 is placed beside `PROC_B`'s seats, as its own head says ("§10 in B39 (with `21_PROCEDURAL_B_cast_and_seats.md`)"); `30_WR_A`'s `minority` row lands in `STORY_B` edit 4's commit (`30_WR_A` "Commit 4 … one row per landing proposal, in that proposal's commit"); `PROC_D`'s PG-7 (g) is the same edit as `PROC_B` (d) and is a POINTER to it (`PROC_D` (g): "proposal B (d), as reconciled. That is the whole of PG-7's unheld part").

---

## Batch B39-procgen-and-cases · lane WR · wave W21 · step S21 · HASH MOVER, one re-pin
INVOCATION: /methodology-execute Batch B39-procgen-and-cases
IN-FLIGHT ROW: registers/handoffs/HANDOFF_WR.md, Open table
GATE: Batch B00-ids
GATE: Batch B01-laneA
GATE: Batch B02-tests
GATE: Batch B04-capability-home
GATE: Batch B06-keyed-draw
GATE: Batch B07-task-draw
GATE: Batch B10-character
GATE: Batch B11-fi-readers
GATE: Batch B11F1-flow-se
GATE: Batch B12c-material-verbs-and-valley
GATE: Batch B15-pc-calibration
GATE: Batch B21-fa-governance
GATE: Batch B22-mb-armies
GATE: Batch B24-sc-hearing
GATE: Batch B25-fi-questioning
GATE: Batch B26-fi-inquiry
GATE: Batch B27-sc-proceedings
GATE: Batch B32-inst-kit
GATE: Batch B33-inst-economy-hands
GATE: Batch B36-wr-story-instruments
GATE: Batch B37-happenings
GATE: Batch B37p-wr-kin-and-life
GATE: Batch B38-narrative-regimes
REQUIREMENT: re-read R-06.e and R-09.b on the generated cast (IS-A §12.2's B39 row) → every acting person vectored; pools differ; no `status:` edited (A-114). The batch otherwise serves rulings, not a row: A-15, A-16, A-19, A-33, A-40, A-44, A-47, A-50 to A-55, A-75 (`IS_A_NINE_part2.md` §12, M5 row: "A-44, A-50 to A-53 (B39)").
BATCH GATE (read once, on the closing tree, `PYTHONHASHSEED=0` on every seeded command; no command past two seasons, D-17):
  `python -m pytest engine/season/tests/test_worldgen_switch.py engine/season/tests/test_census_generated_arrival.py engine/season/tests/test_worldgen_names.py engine/season/tests/test_prologue.py engine/season/tests/test_case_setup_and_beats.py engine/season/tests/test_case_on_the_realm.py engine/season/tests/test_world_cards.py engine/season/tests/test_births.py engine/season/tests/test_abandonment.py engine/season/tests/test_lean_year.py engine/season/tests/test_inst_syn_b_deed_ledger.py engine/season/tests/test_endowment.py engine/season/tests/test_narrative_dues.py engine/season/tests/test_strife_flows.py engine/season/tests/test_storybar.py engine/season/tests/test_scenarios_runner.py -q` → all pass;
  `python -m engine.season.harness.worldgen --seed 0 --sheet` → the shipped realm with every drawn column empty; `--range 20` → 20 of 20 seeds pass V1, the rejection rate printed and under one in five, at least 10 distinct settlement signatures per world (`PROC_A` §5 PG-1);
  `python -m engine.season.harness.decision_spread --persons` → n of n at the built realm (R-06.e, shipped arm); `python -m engine.season.harness.aperture 2 0` → its `POOLS ROLLED` block prints two actors at different pools on a non-combat verb (R-09.b, shipped arm); the generated arm of both is B39.34 (`test_every_generated_person_carries_a_pursuit_vector`, `test_two_generated_persons_roll_one_verb_at_different_pools`);
  the realm content hash of `build_realm(s)` after one season at s = 0, 1, 2 → moved by the declared movers only, each value recorded by the re-pin; at `variable=False`, `prologue=0`, `cards=False`, `birth_rate` 0.0, `abandonment_draw` `off` every generation and story arm is at control (the movers are B39.04, B39.19 to B39.23, B39.25, B39.28 and B39.32);
  `python -m engine.season.harness.register --check` → exit 0; `python -m engine.season.harness.register --requirements` → nine lines; `python tools/m1_acceptance.py --summary` → its verdict line quoted;
  `python tools/ci_naming_check.py` → exit 0 (B39.09's name lists); `python tools/export_sim_params.py --check` → exit 0 and `python tools/ci_sim_fabrication_check.py` → exit 0 (every new fixture carries its tag);
  the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names (the batch touches engine core, `modules/combat/` and registries: the full gates, CLAUDE.md §0.4);
  the glossary rows each item names, read against the code it landed (STAGES "The glossary always matches" rule 2): a mismatch fails the close;
  the close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the named conjuncts' readings with their tree, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<sha>` of B38's close) and after, and the batch's measured wall time; the last `Item:` commit writes the conjuncts' `reading:` records; `status:` is not edited (`IS-A-12`).
EXPECTED RED UNTIL B39.99: none named by a source; an item's own `EXPECTED RED UNTIL` line says so where it has one.
RE-PIN: once, in B39.99: the realm pins in `engine/season/tests/_realm_goldens.py` (B02's one pin file), the combat goldens and golden modes `U5d_STORY` §5 moves (`modules/combat/` exchange resolution: `python tools/ci_golden_modes_check.py` and the combat suite's pins re-recorded, `tools/export_engine_params.py --check` re-read), read against B38's close (`reading @<sha>`); the commit says "re-pin" and lists the movers by handle.
IDS: ED-WR 0; H 3 (B39.30: `abandonment_pool`, `abandonment_ob`, `abandonment_patience`, each a hole-register row graded `assumption`, `STORY_C` edit 4); and 3 registry case ids in `references/npc_registry.yaml` for the three founders (B39.32, `SYN_B` §2: "ids from `references/id_reservations.yaml` at landing") `[ASSUMPTION: `id_reservations.yaml` holds no NPC block at `59ddec1` (its `lane_ids` are ED lanes); B00 reserves the three case ids in its table or the item takes the registry's next free case id on `main` — basis: the file opened at `:1-90`]`
DIALS AT CONTROL:
  `variable` = False (`build_realm`'s switch); set by: no batch names a flip (`PROC_A` §3 item 1: "each later batch that flips a default is its own declared mover"; A-50 licenses the flip, "each table a declared mover at its flip"); target: `PROC_A` §5 PG-1's `--range 20` reading and PG-2's play reading at two seasons → B98 candidate, `UNDECIDED` below;
  `prologue_seasons` (the shipped build's `prologue`) = 0; `worldgen.yaml` carries `prologue_years: 5` (A-51) and the build passes it only "once the default flips" (`PROC_C` (a)); target: PG-4's story-inventory reading; its source reads it at twenty seasons, over the cap before B99 (A-114) → B98, target as stated at two seasons, the twenty-season form left to B99's argv;
  `cards` = False (`build_realm`); set by: none named; target: PG-6's variety reading (`PROC_D` §6) → B98 candidate, with `variable`;
  `covert_kinds.fade.per_season` = 0 for every member; set by B98; target: `PROC_C` PG-5 (d) ("the right rate falls as the proxy is seated later; with `fade` at 0 it does not"), read at seasons 0, 1, 2 (4, 8, 12 in the source; A-114);
  `birth_rate` = 0.0, with `birth_pool`, `birth_ob`, `birth_level`, `birth_step`, `fertile_ages`, `fertile_peak` at their starting points; set by B98 ("set at the calibration with the A-5 sampler", `STORY_B` edit 2); target: `STORY_B` gate 2 ("a birth at some seeds and none at others; at least three of the four bands' outcomes across seeds");
  `majority_age` = 0; set in this batch by B39.28 if the cast's ages are authored at the batch's open (`STORY_B` head: "ships on with the ages"), otherwise by B98; target: `16 × len(SEASONS_OF_YEAR)` and `STORY_B` gate 4;
  `abandonment_draw` = "off", with `abandonment_pool`, `abandonment_ob`, `abandonment_patience`; set by B98 (A-55: "licenses turning it on as a declared mover after its reading"); target: `STORY_C` gate 2 and 3 ("the rung stands at the end at some and is abandoned at others"; "the season of abandonment differs between seeds").
C(B39-procgen-and-cases): this batch's entries; the plan's head parts; `unified/U1_GLOSSARY.md` rows *lifepath*, *heritage*, *prologue*, *prehistory*, *case*, *beat*, *card*, *trail*, *fade*, *lapse*, *abandonment*, *marriage*, *majority*, *regency*, *spell of illness*, *census*, *attribute*, *skill*;
  `engine/season/boot/realm.py` (`build_realm`, B03c), `engine/season/boot/chooser.py` (B03c), `engine/season/harness/populated.py` (`run`), `engine/season/state/ids.py` (`H`), `engine/season/data/cast.py`, `engine/season/data/fixtures.py`, `engine/season/data/rosters.py`, `engine/season/data/goals.py`, `engine/season/data/pursuits.py`, `engine/season/data/verbs.py`, `engine/season/loop/census.py`, `engine/season/loop/matter.py`, `engine/season/loop/effects_founding.py`, `engine/season/loop/effects_governance.py`, `engine/season/loop/effects_economy.py`, `engine/season/epistemic.py` (`trail_of`), `engine/season/seam/wrappers/fieldwork.py` (`fieldwork_input`), `engine/season/queries/world_q.py`, `engine/season/queries/person_q.py`, `engine/season/decision/options.py`, `modules/settlements/subsist.py`, `modules/combat/wrapper.py`;
  `engine/season/harness/corpus_run.py`, `arc.py`, `play_surface.py`, `storybar.py`, `chronicle.py`, `aperture.py`, `decision_spread.py`, `valley.py` (B12c), `scenarios.py` (B11), `strife.py`;
  `engine/season/rosters.yaml`, `engine/season/verb_table.yaml`, `engine/season/write_matrix.yaml`, `engine/season/offices.yaml`, `engine/season/instruments.yaml` (B32), `engine/season/valley.yaml` (B12c), `engine/season/cohorts.yaml`, `engine/season/cases/exercises/NPC-088.yaml`, `engine/season/hole_register.yaml`, `references/npc_registry.yaml`, `references/names_index.yaml`, `references/proper_noun_registry.yaml`, `systems/settlements/valoria_geography_v30.yaml`, `engine/substrate/descriptors.py` (`HERITAGES`, `CAPABILITIES`);
  NEW in this batch: `engine/season/worldgen.yaml`, `engine/season/data/worldgen.py`, `engine/season/harness/worldgen.py`, `engine/season/worldgen_names.yaml`, `engine/season/world_cards.yaml`, `engine/season/data/world_cards.py`, `engine/season/harness/variety.py`, the test files of the BATCH GATE;
  read whole by B39.07 only: `proposals/2026-11-05-cr85-histories-hooks-and-combat-input.md` §2; instruments: `register`, `tools/m1_acceptance.py`, `tools/tests_for_diff.py`, `tools/ci_naming_check.py`, `tools/ci_golden_modes_check.py`, `tools/export_sim_params.py`, `tools/export_engine_params.py`; `engine/season/tests/_realm_goldens.py`;
  the closing SHAs of every batch in the GATE lines; the permanent surface.
SERIAL EDGES: (written last; below the position table)
PARALLEL: S21, alone (`V12_STRUCTURE.md` §2.3: B39 is the only open batch at S21). No file is shared with an open batch.
COST: small builds in the harness and the build, edits to rosters and fixtures, three content drafts (B39.09, B39.13 and B39.14, B39.25); producer `valoria-author` on `sonnet`, `high`; the CENSUS reading (B39.04), the faction-kind roster (B39.03), the PG-5 proxy design (B39.17), the CR-85 design (B39.07), the matrix-row reading (B39.30) and the content drafts on `opus`; the close's terminal critique `opus`.
EST: 19 h [estimate: `V12_STRUCTURE.md` §2.4's formula over this block's 37 positions (0.4 h × 37 + 2.5 h) plus 2 h for the generated-world instrument runs (`--range 20` and the two-season prologue arm over 20 seeds, cached by `(seed, table hash, prologue)` under the scratch directory, `PROC_C` (b)); §2.2's 7 h counted the eleven members]
UNDECIDED:
  (1) `PROC_C` split in two items (PG-4 at U3's place; PG-5 after PG-6) — readings: one item at U3's place (PG-5 would then write rows into a file and a roster that do not exist yet) or two; taken: two, the source's own dependency line.
  (2) `U5d_FA_owed_edits` §10 beside `PROC_B`'s seats (B39.06), not at U3 §1.2's position 15 — both readings land in this batch; taken: beside, the source's own "with" and the shared `build_realm` Office minting.
  (3) whether B98 flips `variable` and `cards` (no source names their flip as a calibration, D-22) — taken: listed under DIALS with their sources' target readings; H2 and A44 decide membership.
  (4) `U5d_STORY` §5 says it "lands with A-31's recalibration" (the PC calibration, B15); U3 places the whole file in B39 — taken: B39 (U3's batch; §2.2 governs the order of batches, E-8), the combat goldens re-recorded at B39.99, and B15's calibration readings re-read at the close (`reading @<sha>` of B15) with any move reported.
  (5) `STORY_B`'s `majority_age`: "edit 4 one commit (hash-equal at `majority_age` 0)" and "ships on with the authored ages" — taken: edit 4 at 0 (B39.27), the flip its own item (B39.28) behind a `STOPS IF` on the ages.
  (6) the lean year as a row of `harness/scenarios.py::SCENARIOS` with `kinds` (`IS-B2-CORE-01` (4) binds "every later entry"; `IS-B3-GO-01` refuses a name with no kind); no source states the lean year's kinds — taken: registered, the kinds `[ASSUMPTION]` from the steward's seat and listed for Jordan in the PR body.
  (7) `17_CENSUS_C1B_02` W-2: U3 §4.1 row 87 sends it here; the file's own `Reconciled:` line moves both W-1 and W-2 to B36 — taken: a named non-carry (B39.33); if B36's part did not carry W-2, H2 adds it there.
  (8) `CORE_case` edit 5's seven further cases and the integer spans of the 86 prose rows: content "other lanes author" — taken: one CONTENT drafting item (B39.14) under D-19, values `status: seed`.

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B39.01 | the world-generation switch, its tables file, the pure planner, the sheet, and the redraw rule | `PROC_A` PG-0 (a)–(e) | BUILD | EQUAL | Batch B12c, Batch B38 |
| B39.02 | ground, endowment `drawn`, climate and points of interest from tables | `PROC_A` PG-1 (f)–(j) | BUILD | EQUAL | B39.01 |
| B39.03 | the person generator, its tables and the institution-kind roster | `PROC_B` PG-2 (a)–(c), (e) | BUILD | EQUAL | B39.02; Batch B37, Batch B33 |
| B39.04 | an arrival at CENSUS takes only his name and birth from the generator | `PROC_B` (d) with `PROC_D` PG-7 (g) | BUILD | MOVER(behaviour) | B39.03 |
| B39.05 | local seats and pedigree Records | `PROC_B` PG-3 (f)–(h) | BUILD | EQUAL | B39.03; Batch B21, Batch B32 |
| B39.06 | a seat exists whether or not it is filled | `U5d_FA_owed_edits` §10 | BUILD | EQUAL | B39.05 |
| B39.07 | what a lifepath's hook is and where it is written: the design | CR-85 (hooks half, ED-IN-0331; intake `:504`) | DESIGN-FIRST | EQUAL | B39.03 |
| B39.08 | names by grammar: the names file, the loader, its checks, the `--names` flag | `PROC_E` (a)–(d) | BUILD | EQUAL | B39.03 |
| B39.09 | the name lists and the house devices, drafted | `PROC_E` (a) INCOMPLETE (CONTENT) | CONTENT | EQUAL | B39.08 |
| B39.10 | a past by simulation: the prologue, its cache and the history page | `PROC_C` PG-4 (a)–(d) | BUILD | EQUAL | B39.05 |
| B39.11 | a case builds its own world and states its beats | `CORE_case` edits 1–4 | BUILD | EQUAL | B39.10; Batch B36 |
| B39.12 | a case is a delta on the realm, with prehistory and three controls | `ARCS_case` "Edits, by owner" | BUILD | EQUAL | B39.11 |
| B39.13 | NPC-088's setup and beats on the realm | `CORE_case` edit 5 (first case); `ARCS_case` (NPC-088 first) | CONTENT | EQUAL | B39.12 |
| B39.14 | the seven further cases' setups and beats, and integer spans | `CORE_case` edit 5 (the rest) | CONTENT | EQUAL | B39.13 |
| B39.15 | one card schema, one loader, one draw; the variety instrument | `PROC_D` PG-6 (a)–(f) | BUILD | EQUAL | B39.12, B39.05 |
| B39.16 | arrivals take name and birth from the generator | `PROC_D` PG-7 (g) | POINTER | — | B39.04 |
| B39.17 | case seeds, leaving patterns, fade, solvability, the inquiry scenario | `PROC_C` PG-5 (e)–(h) | BUILD | EQUAL | B39.15, B39.10 |
| B39.18 | the docket, and an arrival binding a card | `PROC_D` §5, (g′) (A-52) | HELD (PG-6's openings-per-season reading past season 8 shows cards run dry; over the two-season cap before B99) | — | B39.15 |
| B39.19 | a besieged town's larder | `U5d_STORY` §1 | BUILD | MOVER(behaviour) | Batch B22 (B22.12) |
| B39.20 | a burned granary: `sabotage` of a store | `U5d_STORY` §2 | BUILD | MOVER(behaviour) | Batch B12c |
| B39.21 | a lapse under an empty seat is laid on the believed filler | `U5d_STORY` §3 | BUILD | MOVER(behaviour) | Batch B38 (B38.07) |
| B39.22 | the opener's edge on an unready victim | `U5d_STORY` §4 | BUILD | MOVER(behaviour) | Batch B11 (B11.66), Batch B37 |
| B39.23 | both blows of one exchange land before the felling check | `U5d_STORY` §5 | BUILD | MOVER(behaviour) | Batch B15 |
| B39.24 | a marriage is a form of instrument | `STORY_B` edit 1 | BUILD | EQUAL | Batch B32 |
| B39.25 | the cast's marriages, drafted | `STORY_B` edit 1 (`spouse:` content) | CONTENT | MOVER(behaviour) | B39.24 |
| B39.26 | a birth is drawn on the bodies clock; CENSUS individuates the child | `STORY_B` edits 2–3 | BUILD | EQUAL | B39.24, B39.04 |
| B39.27 | a majority, the regency it makes, and the era's `minority` standing | `STORY_B` edit 4 with `30_WR_A` commit 4's `minority` row | BUILD | EQUAL | B39.26; Batch B21, Batch B38 |
| B39.28 | `majority_age` on with the authored ages | `STORY_B` head (A-15) | BUILD | MOVER(behaviour) | B39.27; Batch B37 |
| B39.29 | one owner for a rung ending | `STORY_C` edit 2 | BUILD | EQUAL | Batch B22 |
| B39.30 | an empty founded place is put to a draw each season | `STORY_C` edits 1, 3, 3b, 4 | BUILD | EQUAL | B39.29; Batch B38 |
| B39.31 | the lean year: rows, preset, endings, and its scenario row | `STORY_E` edits 1–3 | BUILD | EQUAL | B39.12, B39.27, B39.30 |
| B39.32 | three founders and their deeds, before tick 0 | `SYN_B` §2 | BUILD | MOVER(behaviour) | B39.12; Batch B32 |
| B39.33 | `foreign_kinds` beside `unrowed_acts` | `17_CENSUS_C1B_02` W-2 | POINTER (non-carry: lands in B36) | — | — |
| B39.34 | R-06.e, R-09.b and `COL_D`'s orderings read on this tree | IS-A §12.2 B39 row; `COL_D` gate (B39 part) | READING | — | B39.03, B39.32 |
| B39.35 | CR-85's hooks: the build | CR-85 (ED-IN-0331) | HELD (B39.07's design merged and naming a build) | — | B39.07 |
| B39.36 | the lean year's cuts read | `STORY_E` edit 3 | READING | — | B39.31 |
| B39.99 | re-pin and close readings | E-1 | BUILD | MOVER (the re-pin) | B39.01 to B39.36 |

Not in this batch, and where each is: `SYN_B` edits 1, 3, 4 (B32); `COL_D` edit 4 and its ledger test (B33); `U5d_FA_owed_edits` §1, §2, §4–§9 (B21) and §3 (B32); `30_WR_A` commits 1–3 and its other commit-4 rows (B38); `17_CENSUS_C1B_02` W-1 and W-2 (B36); `PROC_D` §5's docket and (g′) (held, B39.18); CR-85 (a), combat's input (DONE-IN-CODE, `modules/combat/core.py::resolution_pool`; replaced by A-112's skill scores in the PC batches).

### B39.01 — the world-generation switch, its tables file, the pure planner, the sheet, and the redraw rule · `PROC_A` PG-0 · BUILD · HASH EQUAL
- SOURCE: `PROC_A` §3 items 1–6, §4 "PG-0" (a)–(e), §5 PG-0, §6; U3 §6.1 row `test_worldgen_switch.py` ("write it as the batch's first commit"); rulings A-50, A-53, A-55; closes R-21-02, R-21-13 (`audits/21_PROCEDURAL_GENERATION.md`).
- ADVANCES: none of the nine by itself; the ground every later item of the batch draws on (A-50: some starting state is drawn, small and bounded).
- INSTRUCTION (the source's edits, in order; the test file first):
  1. NEW `engine/season/tests/test_worldgen_switch.py`, written before step 2, each test executing the build: `test_variable_false_reproduces_the_pinned_hash` (`variable=False` reproduces the pinned realm hash at seeds 0, 1, 2); `test_two_seeds_differ_in_at_least_n_settlements` ("with one filled table, `build_realm(0, variable=True)` and `build_realm(1, variable=True)` differ in at least one site or store (the assertion that asserts it asserted: it counts the differing settlements and requires at least `N`)"); `test_table_edit_on_one_territory_moves_no_other_draw` ("plant a table with one extra optional kind on one territory; every settlement outside that territory draws exactly what it drew before"); `test_same_seed_twice_equal_plan_and_hash`; `test_failed_world_takes_the_next_seed_unless_play_failed_world`.
  2. NEW `engine/season/worldgen.yaml` ("typed; the authoring surface; every value `[ASSUMPTION; medium; Jordan to correct; revert: delete the row]`. Empty tables ship; the file's presence changes nothing while `variable` is off"):
     ```yaml
     meta:
       authority: "AUTHORED FOR PLAY. Not canon. Read by engine/season/data/worldgen.py and nothing else."
       schema: 1
     max_attempts: 8            # redraws within the seed on a V1 or V2 failure before the next seed is taken (A-53)
     play_failed_world: false   # A-53's setting: true accepts the last attempt instead of moving to the next seed
     scenario:                  # THE ONLY BLOCK IN WHICH A ROW MAY NAME A FACTION, HOUSE OR PERSON (04 PART D row 27a)
       pinned_persons: []       # case ids that generation may not move, re-home or re-seat
     ground: {}                 # PG-1
     climate: {}                # PG-1
     bars: {}                   # PG-1 onward
     cast_quota: {}             # PG-2 (proposal B)
     lifepaths: {}              # PG-2
     relations: {}              # PG-2
     local_seats: {}            # PG-3
     prologue_seasons: 0        # PG-4 (proposal C): 0 is the off arm; A-51's five years are 5 × len(SEASONS_OF_YEAR), derived there, never typed here
     ```
  3. NEW `engine/season/data/worldgen.py` ("beside `data/cast.py`; one read per process, that module's idiom; `load_yaml`'s duplicate-key refusal"), the typed interface copied whole: frozen dataclasses `SitePlan(settlement: str, kind: str, condition: int)`, `StorePlan(settlement: str, kind: str, amount: int)`, `CohortPlan(settlement: str, weight: int, stance_seed: int)`, `ClimatePlan(territory: str, endurance: int, hardship: int)` ("A-54: the place's pool ground and the season's obstacle ground"), `RealmPlan(seed: int, attempt: int, sites: tuple[SitePlan, ...], stores: tuple[StorePlan, ...], cohorts: tuple[CohortPlan, ...], climate: tuple[ClimatePlan, ...], poi: Mapping[str, tuple[str, ...]], persons: tuple = (), seats: tuple = (), cards: tuple = ())`; functions `load(text: str | None = None) -> dict` ("schema-checked tables; each refusal names the row"), `pick(seed: int, key: str, purpose: str, weights: Mapping[str, int], attempt: int = 0) -> str`, `spread(seed: int, key: str, purpose: str, lo: int, hi: int, attempt: int = 0) -> int`, `draw(seed: int, tables: dict, canon: dict, fixtures, attempt: int = 0) -> RealmPlan` ("pure; no World"), `invariants(plan: RealmPlan, canon: dict) -> list[str]` ("V1: empty list or the defects, each naming a row"), `possibility(w) -> dict[str, int]` ("V2: counts of armed situations in a BUILT world"). "`pick` and `spread` are the only two draw forms. Both reduce the hex digest of `H(seed, 0, key, f"worldgen:{purpose}:{attempt}")` to an integer; `pick` walks cumulative integer weights in sorted-key order (so file order is not an input), `spread` returns an integer in `[lo, hi]`. Neither ever returns 'the largest weight'." `H` is `state/ids.py::H`; "No new RNG, no sequential stream."
  4. `build_realm` "gains `variable: bool = False` and, when true, calls `worldgen.draw` once before the site loop and mints from `plan.sites`, `plan.stores`, `plan.cohorts` instead of the uniform loops" (the producing-site loop, the garrison-condition loop and `seat_cohorts`'s rows; cite by symbol, the source's line numbers predate B03c). "On a V1 defect, or (if `bars` is non-empty) a V2 miss read by `possibility(w)` after the build: rebuild with `attempt + 1` (same seed: the table-edit stability property holds); after `max_attempts`, by default take `seed + 1` and start again at attempt 0, logging the seed's defects and the bars missed with their counts (A-53); with `play_failed_world: true`, accept the last attempt and print its defects instead." "A table that fails at every seed of a `--range` run is reported by the instrument, not looped on forever: the build raises after `max_attempts` seeds in a row, naming the table." `[ASSUMPTION: attempts first, then the next seed — basis: A-53 names the next seed as the replacement; the attempt counter is this file's stability device]` (the source's).
  5. NEW `engine/season/harness/worldgen.py` ("an instrument; no loop step imports it"): "`--seed N --sheet` prints, per territory and settlement, the canon band, the drawn value and the live query beside each other (sites, conditions, stores, cohort weight, expected yield against expected draw), then the V2 counts; `--range N` builds seeds `0..N-1` (build only) and prints, per metric, min, quartiles and max, and the rejection rate."
  6. Glossary: no new term (`variable` is a parameter name; "world seed" has its row); none edited.
- WHERE: NEW `engine/season/worldgen.yaml`; NEW `engine/season/data/worldgen.py`; `engine/season/boot/realm.py` (`build_realm`: the `variable` parameter, the plan branch before the site loop, the redraw loop); NEW `engine/season/harness/worldgen.py`; NEW `engine/season/tests/test_worldgen_switch.py`.
- TESTS: the five of step 1, written first; read before the edit: red (no `variable` parameter, no module); after: green.
- FALSIFIER and CONTROL: "If two `variable=True` seeds build equal sites and stores, the planner is not reading the seed. If a table edit on one territory moves a draw in another, the draws are not keyed." Control: `variable=False` reproduces the pinned realm hash at seeds 0, 1, 2 (B38's close, `reading @<sha>`).
- GATE: `python -m pytest engine/season/tests/test_worldgen_switch.py -q` → five pass; `python -m engine.season.harness.worldgen --seed 0 --sheet` → "the shipped realm with every drawn column empty (the off arm is legible)"; the realm hash at seed 0, one season → equal to B38's close.
- HASH MOVERS: none (`variable=False` ships).
- DEPENDS ON: EXISTS-IN-TREE `engine/season/state/ids.py::H`, `harness/populated.py::seat_cohorts` (moved by B03c), `data/cast.py`; V12 Batch B03c-boot (`build_realm` in `boot/realm.py`, B03c.01); V12 Batch B12a (`site_endowment`, `endowment_for`, B12a.51).
- GLOSSARY: none.
- NAMES: `harness/populated.py::build_realm` → `boot/realm.py::build_realm` (B03c, §5.10).
- COST and TIER: small build; `sonnet`, `high` (`PROC_A` "Tier").
- LANDS IT: B39's `valoria-author` producer, `isolation: worktree`; `Item: B39.01`, `[skip ci]`; the batch's first commit (U3 §6.1).

### B39.02 — ground, endowment `drawn`, climate and points of interest from tables · `PROC_A` PG-1 · BUILD · HASH EQUAL
- SOURCE: `PROC_A` §4 "PG-1" (f)–(j), §5 PG-1, §6; rulings A-50, A-54, A-55 ("the ground PG-1 draws is on the fixed map: no settlement node is added or removed"); closes R-21-03.
- ADVANCES: none of the nine; scarcity that can differ by world (`audits/07_SE_audit.md` §0: no scarcity, so no exchange, requisition, hunger band crossing or migration in computed play).
- INSTRUCTION:
  1. `engine/season/rosters.yaml: site_endowment` ("the SE lane's table; this edit extends each ground row, it does not add a table"): each `ground` row gains two optional keys, `optional:` ("NEW: at most one more kind, by keyed draw over integer weights", e.g. `{seam: 1, orchard: 2, none: 3}`) and `spread:` ("NEW: half-width, on condition_scale, of the starting-condition draw"). "A kind named in `optional:` must be a `SITE_YIELD` kind or `none`; refused at import otherwise, naming the row." The kind names in the source's sketch are illustrative; the rows written use the kinds `site_endowment` names at the batch's open (B12a.51).
  2. `engine/season/data/fixtures.py`: "`endowment_mode` gains the value `drawn` (swept `uniform / ground / drawn`). `endowment_for` is unchanged; `worldgen.draw` calls it for the fixed kinds and adds the `optional:` draw (`pick(seed, settlement_code, "endowment:optional")`)." The shipped value of `endowment_mode` is not changed.
  3. `engine/season/worldgen.yaml`: `ground`, `climate`, `bars`, copied:
     ```yaml
     ground:
       stores_seasons_by_P: {1: [0, 1], 2: [1, 2], 3: [1, 3], 4: [2, 4]}   # canon stats[0] -> seasons of own yield in store, [lo, hi]
       garrison_by_D:       {0: [200, 500], 1: [400, 700], 2: [600, 900], 3: [800, 1000], 4: [900, 1000]}   # canon stats[1] -> condition band
       cohort_weight_by_type: {Village: [1, 2], Town: [2, 4], Fortress: [1, 2], City: [4, 6], Seat: [4, 6], Fortress-City: [3, 5], Cathedral-City: [3, 5]}
       cohort_stance_by_O:  {0: [-2, 0], 1: [-1, 0], 2: [-1, 1], 3: [0, 1], 4: [0, 2]}   # canon stats[2] -> stance seed toward the holder
       poi: by_draw          # each territory's poi_catalog counts are placed on its settlements by keyed draw; `none` leaves them unplaced
     climate:
       by_terrain:           # A-54: per territory, the ground of the season's four-band draw (pool against obstacle), [lo, hi]
         lowland:  {endurance: [3, 5], hardship: [1, 2]}
         upland:   {endurance: [2, 4], hardship: [2, 3]}
         coastal:  {endurance: [3, 5], hardship: [1, 3]}
       # a steward's skill enters that draw as named levels for the place (an `edge` row at site `settlement_effect`, D-U1-09), never here
     bars:
       deficit_settlements: 3   # settlements whose expected yield is under their cohort's draw AND that border a surplus settlement
       aggrieved_cohorts: 3     # cohorts with a negative stance toward a holder who can be petitioned
     ```
     "Every key in `*_by_P`, `*_by_D`, `*_by_O` must cover every value canon's `stats` uses; refused otherwise. The terrain keys must be the terrain classes the geography file declares (the loader reads the file's own set; the three above are placeholders to be replaced by that set at build of the batch)." The geography file is `systems/settlements/valoria_geography_v30.yaml` (read as data by the loader; not a `.md`).
  4. `build_realm`: "under `variable=True` and `endowment_mode == "drawn"`, stores are set to `spread(…)` seasons of the settlement's drawn Sites' base yield (the SE lane sets exactly one season under `ground`); garrison and site conditions from the bands; cohort rows from `plan.cohorts` (the authored `cohorts.yaml` rows remain the off arm); `plan.climate` is written where the WR lane's four-band season draw reads the place's endurance and the season's hardship (`09_WR_B_draws_not_thresholds.md` names the owner; if it has not landed, `climate` is drawn, shown on the sheet and read by nothing, and the sheet says so)." At the item's open, grep for that reader (B12a.10, B12b.03) and record in the commit body which branch was taken.
  5. `possibility(w)` "computes `deficit_settlements` from `world_q.subsistence_draw` and `SITE_YIELD` (existing readers), `aggrieved_cohorts` from cohort stance rows and `world_q` seat scope."
- WHERE: `engine/season/rosters.yaml` (`site_endowment` ground rows); `engine/season/data/fixtures.py` (`endowment_mode`'s values); `engine/season/worldgen.yaml` (`ground`, `climate`, `bars`); `engine/season/data/worldgen.py` (`draw`, `possibility`, the loader's coverage checks); `engine/season/boot/realm.py` (`build_realm`'s `drawn` branch); `engine/season/tests/test_worldgen_switch.py`.
- TESTS: in `test_worldgen_switch.py`, written before step 1: `test_optional_kind_outside_site_yield_is_refused_naming_the_row` and `test_stats_key_uncovered_is_refused` `[ASSUMPTION: test names; the item creates them]` (red before: no loader check); `test_two_seeds_differ_in_at_least_n_settlements` now runs on the filled tables.
- FALSIFIER and CONTROL: "If under `drawn` no world shows want in three seasons while `ground` does, the spread is washing out the SE lane's differentiation and the bands are wrong" (read at two seasons; A-114). "If the rejection rate is high, the bars are doing the generator's work; edit the tables." Control: "`optional` absent and `spread: 0` gives the SE lane's `ground` hash exactly."
- GATE: `python -m engine.season.harness.worldgen --range 20` → "20 of 20 seeds pass V1; rejection rate printed and under one in five; distinct settlement signatures per world at least 10 (today 1); scarcity index (deficit settlements) has a non-zero range across seeds"; play, 3 seeds × 2 seasons (3 in the source; A-114): at least one of `exchange.made`, `requisition.taken`, a hunger band crossing or an executed cohort `migrate` per world, against the `uniform` arm run the same way, both printed; `python -m pytest engine/season/tests/test_worldgen_switch.py -q` → pass; the realm hash at seed 0, one season, at shipped settings → equal to B39.01's.
- HASH MOVERS: none at shipped settings (`variable=False`; `endowment_mode` unchanged).
- DEPENDS ON: V12 B39.01; V12 Batch B12a (B12a.51 `site_endowment`, `endowment_for`; B12a.10 the wear draw); V12 Batch B12b (B12b.03, the season's harvest draw, the reader of `climate`); EXISTS-IN-TREE `queries/world_q.py::subsistence_draw`, `data/fixtures.py::SITE_YIELD`.
- GLOSSARY: none (*endowment*, *climate* rows carry these senses; `drawn` is a value of an existing setting).
- NAMES: as B39.01.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B39's producer; `Item: B39.02`, `[skip ci]`.

