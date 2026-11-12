# Workplan v12 — part 39: batches B36-wr-story-instruments, B31-mb-loadout-economy

## Status: PROPOSED (a body part of workplan v12, drafted under `master/workplan_v12/`; unratified input to `methodology-execute`'s 0.1 stop until Jordan adopts v12, `V12_STRUCTURE_part3.md` §8; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Written against: the working tree of branch `ccr-62958c70-0kjhsw`, read 2026-11-12; author lane A39 of `master/workplan_v12/V12_STRUCTURE_part2.md` §4.2 (sources: U3 §1 items 36 and 31; MBA-09; the intake `:211`). Every item is written against the tree as the batches before it leave it; where a symbol named here does not exist at this read, the item names the batch that makes it. Errata `V12_STRUCTURE_part4.md` (E-1 to E-15) are applied.

**What this part holds.** Two batches, in the order of this lane's row: `B36-wr-story-instruments` (WR; this file) and `B31-mb-loadout-economy` (MB; `workplan_v12_part39_cont.md`). They share no file and no gate; both open at step S19 (`V12_STRUCTURE.md` §2.3). Each is one block with one close (`V12_STRUCTURE_part2.md` §5.2, §5.3). A part cites another batch or item by handle only.

**Words.** `unified/U1_GLOSSARY.md`. A person's numbers: attribute, skill, skill score, martial skill, derived score (A-98). Armies: army, unit, army formation, unit formation; no size word (A-99, the MB lexicon). A *lap* is one pass of the season's scene budget; a *round* is one engagement of a fight (A-101); the riposte keeps its code id `finalblow_riposte`. Source text that says "round" for the season's pass is copied with a `NAMES:` line (B04's `PCR-4`). The story bar's "crossing" (a person standing on two things at once) is an **overlap** (glossary *crossing*); the story census is the **story count** (`23_STORY_D` head).

**Paths.** As `V12_STRUCTURE.md` states: a bare `proposals/…` path of a numbered proposal is under `proposals/2026-11-12-subsystem-audit-suite/`; `U3` is `unified/U3_DEPENDENCY_ORDER.md`; `the intake` is `master/eval/V12_INTAKE.md`; `MBA` is `master/mb_abstraction/MBA_DESIGN_part3.md` (and `MBA_DESIGN_part2.md` for §3); `IS-A` is `master/instructions/IS_A_NINE.md` and `_part2`. A path under `engine/`, `modules/`, `tools/`, `references/`, `tests/`, `registers/` is the repository's.

---

## Batch B36-wr-story-instruments · lane WR · wave W19 · step S19 · HASH MOVER, one re-pin
INVOCATION: /methodology-execute Batch B36-wr-story-instruments
IN-FLIGHT ROW: registers/handoffs/HANDOFF_WR.md, Open table
GATE: Batch B00-ids
GATE: Batch B01-laneA
GATE: Batch B02-tests
GATE: Batch B03-hygiene
GATE: Batch B09-memory
GATE: Batch B12c-material-verbs-and-valley
GATE: Batch B27-sc-proceedings
GATE: Batch B34-go-surface
GATE: Batch B35-wr-thread
REQUIREMENT: R-04.c1 (the chronicle) → `python -m engine.season.harness.chronicle --seed 0 --seasons 2` tells: every line whose act has a subject names it (IS-A §2's R-04.c1, "`chronicle --seed 0` tells"); R-04.a, R-04.b, R-04.c2 to R-04.c7 re-read on this close's tree → each holds (M4 closes here, `V12_STRUCTURE.md` §3; IS-A `_part2` §12.2's B36 row "the chronicle tells; nine of nine", read as readings: no `status:` edited, A-114)
BATCH GATE (read once, on the closing tree, `PYTHONHASHSEED=0` on every seeded command; no command past two seasons, A-114):
  `python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 2 --arms off all --executed-only` → `DIFFER`, and a per-seed `person.died` count in `all` above `off`'s (three seasons in the source; A-114); `--arms off off` → `EQUAL`;
  `python -m engine.season.harness.chronicle --seed 0 --seasons 2 --chains --min-depth 2` → an edge null printed beside the chain ends; every rendered line with a subject names it (R-04.c1); `python -m engine.season.harness.strife 2 0 1 2 --strands` → a `shape:` line per seed with `closed` split `term` / `threshold`, and the `ROUTE, NEVER TAKEN` marks (three seasons in the source; A-114);
  `python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 2 --arms off --situations` → per season a `closes` line, `open=`, `motion=`, `idle=` lines; `--control flat --situations` → the flat arm's hash differs from the shipped arm's;
  `python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 2 --arms off off --stories` → `EQUAL`; the three control shapes above 0 at every seed (clause C0); every other shape 0 or `n/a` (B36.R1);
  `python -m engine.season.harness.arc --seed 0 --seasons 2` → exit 0, `no predicate (control)` 0; `python -m engine.season.harness.aperture 2 0` → a `FOREIGN` line; `python -m engine.season.harness.aperture 2 --seeds 0 1 2`'s `BUILT OUT` line for `thread_read` → built out, as at B35's close (`reading @<sha>`);
  `python -m pytest engine/season/tests/test_storybar.py engine/season/tests/test_cr69_chains.py engine/season/tests/test_in37_chronicle.py engine/season/tests/test_sc01_fired_slot.py engine/season/tests/test_in12_step9.py engine/season/tests/test_cl_thrust_b01_arc_reader.py engine/season/tests/test_aperture.py engine/season/tests/test_journal.py -q` → all pass;
  the realm content hash of `build_realm(s)` after one and two seasons, s = 0, 1, 2 → moved only by B36.10 (declared), recorded by the re-pin; every harness item reads EQUAL against the item before it;
  `python -m engine.season.harness.register --check` → exit 0; `--requirements` → nine lines; `python tools/m1_acceptance.py --summary` → its verdict line quoted; the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names (`verb_table.yaml` and `loop/calendar.py` are engine core: the full gates, CLAUDE.md §0.4);
  the glossary rows each item names, read against the code it landed (a mismatch fails the close);
  the close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, R-04's conjuncts' readings with their tree, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<sha>`, B35's close) and after, and the batch's measured wall time; B36.99 writes R-04's conjuncts' `reading:` records; `status:` is not edited (`IS-A-12`).
RE-PIN: once, in B36.99: the realm pins in `engine/season/tests/_realm_goldens.py` (B02's one pin file) and every golden `thread_read`'s new class moves, read against B35's close (`reading @<sha>`); the commit says "re-pin: `thread_read` forms only on a Site (B36.10); every other item harness-only".
IDS: ED-WR 0; H 0
DIALS AT CONTROL: none (the story bar's arms are an instrument's settings, not the game's; `basis_off` ships as the empty mapping until B38's `20_NARRATIVE_A` to `E` add their fixtures, B36.13)
C(B36-wr-story-instruments): this batch's entries; the plan's head parts; `engine/season/harness/storybar.py`, `chronicle.py`, `strife.py`, `arc.py`, `aperture.py`, `arms.py` (`_resolve_arm`, read), `decision_spread.py` (`apply_control`, `no_goals`, read), `corpus_run.py` (`attempts`, `foreign_kinds`, read), `valley.py` (B12c, read), `soak.py` (`_occasion_row`, read); `engine/season/boot/realm.py` (B03c; `build_realm`); `engine/season/loop/calendar.py`; `engine/season/verb_table.yaml` (`thread_read`, `restore`); `engine/season/decision/sheet.py` (`account`, B34); `engine/season/queries/person_q.py`; `engine/season/queries/world_q.py` (the stampers `vacancies`, `matters_awaiting`, `detainees_held`, `at_war`, `ambitions`; `concluded`); `engine/season/state/carriers.py` (`subject_of`), `state/attribution.py` (`anchor_of`); `engine/season/data/verbs.py` (`EVENT_KINDS`); `engine/dice_engine/draw.py` (B06); `engine/season/hole_register.yaml` (H-26, H-208, H-235);
  the tests named in the items; instruments: `storybar`, `chronicle`, `strife`, `arc`, `aperture`, `register`, `tools/m1_acceptance.py`, `tools/tests_for_diff.py`, `tools/ci_sim_fabrication_check.py`; `engine/season/tests/_realm_goldens.py` (B02);
  read whole by B36.08 only: `proposals/2026-10-13-narration-mechanisms.md` §3.3 (the journal's epistemic rules) and §4 W5; `master/eval/E2.md:530-532` (NM-W5's carry-forward block);
  the closing SHAs of B00, B01, B02, B03, B09, B12c, B27, B34, B35; the permanent surface (CLAUDE.md, `CURRENT.md`, `HANDOFF.md`, `registers/handoffs/HANDOFF_WR.md`, the skill and `methodology-close`).
UNDECIDED:
  (1) HASH: `V12_STRUCTURE.md` §2.2 calls B36 EQUAL (0 of 7); `16_PESSIMIST_WR_D` edit 2 declares itself a mover ("moves any world in which `thread_read` formed on a Record or a person"). Taken as written by the source: B36 is a MOVER, one re-pin at B36.99; H2's hash table changes.
  (2) `17_CENSUS_C1B_02` W-2: U3 §1 item 36 says "not W-2" and U4 lists "+part B39"; the file's own later `Reconciled:` line (checked at the tree) says W-1 and W-2 both land in B36 and B39 carries only `12_ARCS_case_on_the_realm`'s `match_beats` after W-1. The file is followed (B36.17); A42 must not carry W-2.
  (3) Grouping (E-13): `09_WR_story_instruments` edits 1–2 are one item (one `storybar.py` commit, C3-K7), 3–4 one (`strife.py`), 5 one; `09_WR_B_readings` edit 1 alone (it writes `arc.py`, which `09_WR_B_chronicle` and W-1 read), edits 2–4 one; `16_PESSIMIST_WR_D` one item per edit as its "Lands it" says, edit 3 (no code) recorded in edit 5's commit; `23_STORY_D` edits 1, 2, 5 one item and 3, 4 one.
  (4) `storybar.ARMS` becomes a mapping (B36.01): `chronicle.py`'s `--arm` default `SB.ARMS[0]` and W-1's copied `default=SB.ARMS[0]` would raise `KeyError`; both are written `default="off"` (one token; the reading that changes less). Not in any source.
  (5) `09_WR_B_chronicle` calls `account(w, pid)`; `11_GO_player_surface_contract_B` §4 declares `account(p, since)` with `since = (tick, lap)` after B04. The declared signature is followed (B36.06, B36.07, B36.08).
  (6) `20_NARRATIVE_F`'s gate names an `on` arm ("every `20_NARRATIVE` fixture at its proposed live value") that no edit builds and whose fixtures land in B38; B36.13 builds `noconv` and `basis_off` (empty), and the bar's `on`-arm clauses are read at B38 (B36.R1).
  (7) NM-W5 (the intake `:213`): E1 reads it SUPERSEDED, E4 "design-first, held", E2 STILL-NEEDED in B36; the intake's `settled:` governs (D-14): an item, B36.08, after the chronicle it composes on; its NEEDS NM-W1 is met (NM-W1 is SUPERSEDED by `09_WR_B_chronicle_that_tells`, `master/V11_EVALUATION_part2.md:288`).
SERIAL EDGES: within the batch: `harness/storybar.py` (C3-K7, one proposal at a time, in this order): B36.01 → B36.04 → B36.05 → B36.11 → B36.12 → B36.13 → B36.14 → B36.15; `harness/chronicle.py`: B36.01 (the null) → B36.03 (`why`) → B36.06 (`about`, the pick, `--focus`) → B36.07 (`case_thread`); `harness/strife.py`: B36.02 → B36.04 (the `closed` split calls `arc.closes`); `harness/arc.py`: B36.04 (`CLOSE_CELLS`, `closes`) → B36.06 (the pick reads `CLOSE_CELLS`) → B36.16 (W-1's entry; `12_ARCS_case_on_the_realm`'s `match_beats` follows in B39); B36.04 → B36.11 (`turns` is the third column of the split); B36.06 → B36.08 (the journal composes on `--focus`); B36.13 → B36.14 (the story count's tests live in the file the overlaps block opens); B36.10 → B36.12 (the `no_calendar` arm is compared against the moved realm).
  With other batches, by file (U3 §5.1, `→` is landing order): `harness/storybar.py`, `engine/season/tests/test_storybar.py` B02 → B36 → B38; `harness/chronicle.py` B02 → B36 → B38 (`30_GO_F` adds `era`, `story`, `left`); `harness/strife.py` B12 → B32 → B36 → B38; `harness/arc.py` B36 → B39; `harness/aperture.py` B02 → B36 → B37; `engine/season/verb_table.yaml` (hot) B35 → B36 → B38, one row (`thread_read`); `engine/season/hole_register.yaml` (permanent surface) one row (H-208's `sweep:`).
PARALLEL: S19 with B31-mb-loadout-economy (MB) and B33-inst-economy-hands (FA). Shared file: `engine/season/verb_table.yaml` with B33 (and B31 if B31.12 adds `march`'s write): different rows, kept by hand at merge (`V12_STRUCTURE_part3.md` §7.3). All three move pins: merge order B31 → B33 → B36 (§2.1's row order, §7.4); B36 rebases on B33's merge and re-pins once.
COST: small builds in harness readers, two edits at a clock and a verb row; producer `valoria-author` on `sonnet`, `high` (each source's tier); B36.08's Layer 1 question read by `opus`; the close's terminal critique `opus`.
EST: 10 h [estimate: `V12_STRUCTURE.md` §2.4's formula over 19 positions, 0.4 h × 19 + 2.5 h (E-15); no calibration and no instrument past two seasons]

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B36.01 | the story bar's forcing arms and the edge null | `09_WR_story_instruments_that_can_fail` edits 1, 2 | BUILD | EQUAL | Batch B02, Batch B12c |
| B36.02 | the strand shape line and the routes taken | `09_WR_story_instruments_that_can_fail` edits 3, 4 | BUILD | EQUAL | B36.01 |
| B36.03 | the chronicle prints why an act was taken | `09_WR_story_instruments_that_can_fail` edit 5 | BUILD | EQUAL | B36.01 |
| B36.04 | closes by act and by clock | `09_WR_B_readings_of_closure_and_tension` edit 1 | BUILD | EQUAL | B36.01, B36.02 |
| B36.05 | open situations, the wear rule, idleness, the flat control | `09_WR_B_readings_of_closure_and_tension` edits 2–4 | BUILD | EQUAL | B36.04 |
| B36.06 | the chronicle says what each act was about, starts from a close, and can be focalized | `09_WR_B_chronicle_that_tells` edits 1–4 | BUILD | EQUAL | B36.04, B36.03; Batch B34, Batch B03 |
| B36.07 | the case thread | `19_LACUNA_verdict_ladder_and_reversal` R-19-09 | BUILD | EQUAL | B36.06; Batch B27 |
| B36.08 | the focalized journal | NM-W5 (the intake `:213`) | BUILD | EQUAL | B36.06; Batch B34 |
| B36.09 | CALENDAR fires what is due, not only what is due today | `16_PESSIMIST_WR_D` edit 1 | BUILD | EQUAL (asserted) | Batch B02 |
| B36.10 | `thread_read` is aimed at a place | `16_PESSIMIST_WR_D` edit 2 | BUILD | MOVER(behaviour) | Batch B12c, Batch B35 |
| B36.11 | the turn: who closed what another opened | `16_PESSIMIST_WR_D` edit 4 | BUILD | EQUAL | B36.04, B36.05 |
| B36.12 | a cut arm and the noise floor; CALENDAR kept and marked unproven | `16_PESSIMIST_WR_D` edits 5, 3 | BUILD | EQUAL | B36.11, B36.10 |
| B36.13 | the overlaps block, its arms and its tests | `20_NARRATIVE_F` edits 1–4 (not the G5 split) | BUILD | EQUAL | B36.12 |
| B36.14 | the story count: shapes, the first table, the plants | `23_STORY_D` edits 1, 2, 5 | BUILD | EQUAL | B36.13; Batch B09 |
| B36.15 | the story count's switches and the seat reading | `23_STORY_D` edits 3, 4 | BUILD | EQUAL | B36.14; Batch B12c |
| B36.16 | the arc reader gets an entry | `17_CENSUS_C1B_02` W-1 | BUILD | EQUAL | B36.04, B36.01 |
| B36.17 | `foreign_kinds` is printed where `unrowed_acts` is | `17_CENSUS_C1B_02` W-2 | BUILD | EQUAL | Batch B02 |
| B36.R1 | the story bar's readings at the close | `20_NARRATIVE_F` "The gate"; `23_STORY_D` "The gate" (C0, C9's baseline) | READING | — | B36.15 |
| B36.99 | re-pin and close readings | E-1 | BUILD | MOVER (the re-pin) | B36.01 to B36.R1 |

Not in this batch, and where each is: `30_WR_E`'s fork lift, the `entrenched`, `custom_off`, `custom_on` arms and `--null-scenes` (B38); `09_WR_story_instruments` edit 3's per-strand state and subject once `30_WR_C` commit 2 lands, and edit 5's `era`, `story`, `left` (`30_GO_F`, B38); `20_NARRATIVE_F`'s G5 split by `stands_for` (B38, with `20_NARRATIVE_A`; U3 §4.1 row 88); `09_WR_story_instruments`' "Interface this lane needs from CORE" (an act's first Event carrying the question in `Event.observed`: a hash mover of `loop/resolve.py::_act_events`, named as CORE's and not an edit of this file; no item carries it); `17_CENSUS_C1B_02` W-3 (decided in `09_WR_threadwork_module.md`, nothing built); `19_LACUNA_verdict_ladder` R-19-07, R-19-08 (B27).

### B36.01 — the story bar's forcing arms and the edge null · `09_WR_story_instruments_that_can_fail` edits 1, 2 · BUILD · HASH EQUAL
- SOURCE: `proposals/09_WR_story_instruments_that_can_fail.md` "Edit 1", "Edit 2", "The gate", "The falsifier"; rulings A-15 (the `bodies` arm stands); C3-K7; closes F-WR-03 (edits 1–2).
- ADVANCES: none of the nine by itself; the M2 instrument can report a failure (R-04.c1's chronicle is read through B36.03 and B36.06).
- INSTRUCTION (one commit: the source's storybar edits, C3-K7):
  1. `engine/season/harness/storybar.py`, the `ARMS` tuple (today `ARMS = ("off",)` with its two comment lines) becomes, copied:
     ```python
     #: arm name -> {fixture name: value}; each value is a member of that fixture's own declared `sweep:`
     #: (hole_register H-26, H-208, H-235), never a number invented here. `off` is the shipped loop.
     ARMS = {
         "off":      {},
         "weather":  {"season_factor_draw": ((0.5, 1.0, 2.0),) * 4},      # H-26's swept arm
         "bodies":   {"age_step": 0.01},                                   # H-208's own test arm (its `sweep:`)
         "lattice":  {"lattice_coupling": 250},                            # H-235's swept arm
         "all":      {**weather, **bodies, **lattice},                     # the union of the three
     }
     ```
     The `all` row is written out as the union of the three mappings above (the source's `**weather` names no variable). `drive()` applies the arm "with `w.fixtures.get(name)` then `w.fixtures.sweep(name, value)` on the freshly built world before the chooser is made (the two lines `harness/arms.py:205-207` already uses)". The module docstring's FORCING ARMS sentence "No forcing source is built yet … so there is no `on` arm" is deleted. "`--arms off off` stays the control and must still read EQUAL." `drive(seed, seasons, arm, cap=None, …) -> (world, driver, bounds)` is unchanged; `if arm not in ARMS` keeps refusing an unbuilt arm. Whatever B02 added (`removal_arm`, `--remove`) is kept.
  2. `engine/season/hole_register.yaml` H-208 `sweep:` gains `"illness_rate 0.05 (a test arm; the value `09_WR_world_motion.md` edit 4 and the WR addendum read)"` in this commit.
  3. `engine/season/harness/chronicle.py::main`: `--arm`'s `default=SB.ARMS[0]` → `default="off"` (UNDECIDED (4): a mapping has no index 0).
  4. `storybar.py`, beside `_depths`, copied: `def edge_null(rows: dict, seed: int) -> dict:` with the docstring "`rows` (as `read` returns them) with each act's cross antecedents RE-DRAWN: the same number, chosen uniformly among earlier-logged acts by another actor (`random.Random(seed)`). Depth is recomputed by `_depths`. A reading that does not exceed this is what any log with that many cross edges would show." Defined for an empty log and for a log with no cross edge (it returns the rows).
  5. "`chronicle.consequence_chains` gains `null_seeds: tuple = ()` and, when given, returns `"null_chain_ends": [..]` beside `"chain_ends"`; `render_chains` prints `chain_ends=N (edge null: mean M, range a..b)`. `arc.shuffled_causes` is kept for `read_arcs` … it is removed as the control of the chain reading."
  6. `engine/season/tests/test_cr69_chains.py`: "`test_the_shuffled_causes_null_reads_below_the_linked_log` is replaced by a test over `edge_null` on the same plant (four depth-3 chains: the edge null reads below 4 at every seed), and `test_the_reader_on_a_real_seed…`'s `null != real` becomes: `edge_null` over the real rows preserves the number of cross edges exactly and changes at least one antecedent."
- WHERE: `engine/season/harness/storybar.py` (`ARMS`, `drive`, `edge_null`, the docstring); `engine/season/harness/chronicle.py` (`consequence_chains`, `render_chains`, `main`'s `--arm`); `engine/season/tests/test_cr69_chains.py`; `engine/season/hole_register.yaml` (H-208 `sweep:`).
- TESTS: the two replaced tests in `test_cr69_chains.py`, written before step 4 and read red (no `edge_null`); `test_storybar.py::test_forcing_off_the_two_arms_read_equal` and `::test_an_unbuilt_forcing_arm_is_refused_not_invented` stay green unedited.
- FALSIFIER and CONTROL: "an arm that reads EQUAL to `off` on every pooled season reading. That is a fixture the loop does not read, and is a finding about the fixture"; "`edge_null` over the planted world reading at or above the plant's four chains". Control: `--arms off off` EQUAL; `build_realm(0)`'s content hash and the one- and two-season pins unchanged.
- GATE: `python -m pytest engine/season/tests/test_cr69_chains.py engine/season/tests/test_storybar.py engine/season/tests/test_in37_chronicle.py -q` → pass; `python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 2 --arms off all --executed-only` → `DIFFER`, `person.died` per seed above `off`'s; `--arms off off` → `EQUAL` (three seasons in the source; A-114); `python -m engine.season.harness.register --check` → exit 0 (H-208's row).
- HASH MOVERS: none (harness and tests; the register row is not hashed).
- DEPENDS ON: EXISTS-IN-TREE `harness/storybar.py::ARMS`, `::drive`, `::_depths`, `harness/arms.py::_resolve_arm`, `harness/chronicle.py::consequence_chains`, `::render_chains`, `harness/arc.py::shuffled_causes`, fixtures `season_factor_draw`, `age_step`, `illness_rate`, `lattice_coupling` (`data/fixtures.py`); V12 Batch B02 (`removal_arm` in `storybar.py`, C3-K7's first edit).
- GLOSSARY: *edge null* (new row): "a control that keeps how many cross antecedents each act has and re-draws which acts they are, as a shuffled deck keeps its cards and changes their order"; *arm* unchanged (a setting of an experiment).
- COST and TIER: edit and small build; `sonnet`, `high`.
- LANDS IT: B36's `valoria-author` producer, `isolation: worktree`; `Item: B36.01`, `[skip ci]`.

<!-- A39 append point -->
