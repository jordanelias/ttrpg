# Workplan v12 — part 39: batches B36-wr-story-instruments, B31-mb-loadout-economy

## Status: PROPOSED (a body part of workplan v12, drafted under `master/workplan_v12/`; unratified input to `methodology-execute`'s 0.1 stop until Jordan adopts v12, `V12_STRUCTURE_part3.md` §8; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Written against: the working tree of branch `ccr-62958c70-0kjhsw`, read 2026-11-12; author lane A39 of `master/workplan_v12/V12_STRUCTURE_part2.md` §4.2 (sources: U3 §1 items 36 and 31; MBA-09; the intake `:211`). Every item is written against the tree as the batches before it leave it; where a symbol named here does not exist at this read, the item names the batch that makes it. Errata `V12_STRUCTURE_part4.md` (E-1 to E-15) are applied.

**What this part holds.** Two batches, in the order of this lane's row: `B36-wr-story-instruments` (WR; this file) and `B31-mb-loadout-economy` (MB; `workplan_v12_part39_cont.md`). They share no file and no gate; both open at step S19 (`V12_STRUCTURE.md` §2.3). Each is one block with one close (`V12_STRUCTURE_part2.md` §5.2, §5.3). A part cites another batch or item by handle only.

**Words.** `unified/U1_GLOSSARY.md`. A person's numbers: attribute, skill, skill score, martial skill, derived score (A-98). Armies: army, unit, army formation, unit formation; no size word (A-99, the MB lexicon). A *lap* is one pass of the season's scene budget; a *round* is one engagement of a fight (A-101); the riposte keeps its code id `finalblow_riposte`. Source text that says "round" for the season's pass is copied with a `NAMES:` line (B04's `PCR-4`). The story bar's "crossing" (a person standing on two things at once) is an **overlap** (glossary *crossing*); the story census is the **story count** (`23_STORY_D` head).

**Paths.** As `V12_STRUCTURE.md` states: a bare `proposals/…` path of a numbered proposal is under `proposals/2026-11-12-subsystem-audit-suite/`; `U3` is `unified/U3_DEPENDENCY_ORDER.md`; `the intake` is `master/eval/V12_INTAKE.md`; `MBA` is `master/mb_abstraction/MBA_DESIGN_part3.md` (and `MBA_DESIGN_part2.md` for §3); `IS-A` is `master/instructions/IS_A_NINE.md` and `_part2`. A path under `engine/`, `modules/`, `tools/`, `references/`, `tests/`, `registers/`, `skills/` is the repository's, and so is `proposals/2026-10-13-narration-mechanisms.md` (NM-W5's home, outside the suite).

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
HASH READING: `PYTHONHASHSEED=0 python -c "import sys; from engine.season.boot.realm import build_realm; from engine.season.harness.populated import run; s, k = int(sys.argv[1]), int(sys.argv[2]); w = build_realm(s); run(k, s, w=w); print(w.content_hash())" <s> <k>` → the realm content hash at seed `<s>` after `<k>` seasons: `<k>` = 1, one season, unless the gate names two (never more before B99, D-17); `<k>` = 0 reads the build hash; per item `<s>` = 0 (a mover's reading, E-2), at `.99` `<s>` = 0, 1, 2; each value quoted `reading @<sha>`, the tree it was read on (`workplan_v12.md` §3.B, "the hash reading").
REQUIREMENT: R-04.c1 (the chronicle) → `python -m engine.season.harness.chronicle --seed 0 --seasons 2` tells: every line whose act has a subject names it (IS-A §2's R-04.c1, "`chronicle --seed 0` tells"); R-04.a, R-04.b, R-04.c2 to R-04.c7 re-read on this close's tree → each holds (M4 closes here, `V12_STRUCTURE.md` §3; IS-A `_part2` §12.2's B36 row "the chronicle tells; nine of nine", read as readings: no `status:` edited, A-114)
BATCH GATE (read once, on the closing tree, `PYTHONHASHSEED=0` on every seeded command; no command past two seasons, A-114):
  `python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 2 --arms off all --executed-only` → `DIFFER`, and a per-seed `person.died` count in `all` above `off`'s (three seasons in the source; A-114); `--arms off off` → `EQUAL`;
  `python -m engine.season.harness.chronicle --seed 0 --seasons 2 --chains --min-depth 2` → an edge null printed beside the chain ends; every rendered line with a subject names it (R-04.c1); `python -m engine.season.harness.strife 2 0 1 2 --strands` → a `shape:` line per seed with `closed` split `term` / `threshold`, and the `ROUTE, NEVER TAKEN` marks (three seasons in the source; A-114);
  `python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 2 --arms off --situations` → per season a `closes` line, `open=`, `motion=`, `idle=` lines; `--control flat --situations` → the flat arm's hash differs from the shipped arm's;
  `python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 2 --arms off off --stories` → `EQUAL`; the three control shapes above 0 at every seed (clause C0); every other shape 0 or `n/a` (B36.R1);
  `python -m engine.season.harness.arc --seed 0 --seasons 2` → exit 0, `no predicate (control)` 0; `python -m engine.season.harness.aperture 2 0` → a `FOREIGN` line; `python -m engine.season.harness.aperture 2 --seeds 0 1 2`'s `BUILT OUT` line for `thread_read` → built out, as at B35's close (`reading @<sha>`);
  `python -m pytest engine/season/tests/test_storybar.py engine/season/tests/test_cr69_chains.py engine/season/tests/test_in37_chronicle.py engine/season/tests/test_sc01_fired_slot.py engine/season/tests/test_in12_step9.py engine/season/tests/test_cl_thrust_b01_arc_reader.py engine/season/tests/test_aperture.py engine/season/tests/test_journal.py -q` → all pass;
  the realm content hash of `build_realm(s)` after one and two seasons, s = 0, 1, 2 → moved only by B36.10 (declared), recorded by the re-pin; every harness item reads EQUAL against the item before it;
  `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`); `--requirements` → nine lines; `python tools/m1_acceptance.py --summary` → its verdict line quoted; the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names (`verb_table.yaml` and `loop/calendar.py` are engine core: the full gates, CLAUDE.md §0.4);
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
PARALLEL: S19 with B31-mb-loadout-economy (MB) and B33-inst-economy-hands (FA). Shared file: `engine/season/verb_table.yaml` with B33 (and B31 if B31.09 adds `march`'s write): different rows, kept by hand at merge (`V12_STRUCTURE_part3.md` §7.3). All three move pins: merge order B31 → B33 → B36 (§2.1's row order, §7.4); B36 rebases on B33's merge and re-pins once.
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
- GATE: `python -m pytest engine/season/tests/test_cr69_chains.py engine/season/tests/test_storybar.py engine/season/tests/test_in37_chronicle.py -q` → pass; `python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 2 --arms off all --executed-only` → `DIFFER`, `person.died` per seed above `off`'s; `--arms off off` → `EQUAL` (three seasons in the source; A-114); `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`) (H-208's row).
- HASH MOVERS: none (harness and tests; the register row is not hashed).
- DEPENDS ON: EXISTS-IN-TREE `harness/storybar.py::ARMS`, `::drive`, `::_depths`, `harness/arms.py::_resolve_arm`, `harness/chronicle.py::consequence_chains`, `::render_chains`, `harness/arc.py::shuffled_causes`, fixtures `season_factor_draw`, `age_step`, `illness_rate`, `lattice_coupling` (`data/fixtures.py`); V12 Batch B02 (`removal_arm` in `storybar.py`, C3-K7's first edit).
- GLOSSARY: *edge null* (new row): "a control that keeps how many cross antecedents each act has and re-draws which acts they are, as a shuffled deck keeps its cards and changes their order"; *arm* unchanged (a setting of an experiment).
- COST and TIER: edit and small build; `sonnet`, `high`.
- LANDS IT: B36's `valoria-author` producer, `isolation: worktree`; `Item: B36.01`, `[skip ci]`.

### B36.02 — the strand shape line and the routes taken · `09_WR_story_instruments_that_can_fail` edits 3, 4 · BUILD · HASH EQUAL
- SOURCE: the same file, "Edit 3", "Edit 4", "The falsifier"; closes F-WR-01 (edit 4), F-WR-03 (edit 3).
- ADVANCES: none of the nine; whether the world closes what it opens is readable per seed.
- INSTRUCTION (copied):
  1. Edit 3, `engine/season/harness/strife.py::strands_block`: one line per seed, after `concluded N of M`:
     `  shape: opened O · escalated E · closed C · closed-and-stayed S (of M strands)` —
     "*opened*: the strand holds an `opens` move (always true; printed as the denominator's check); *escalated*: it holds a move by a doer other than its first doer, later in the log than its opening; *closed*: its latest move is terminal, is **not** an opening move, and `world_q.concluded` holds; *closed-and-stayed*: reported only by the two-reading form, `strands_block(w, seed, earlier=…)`, where `earlier` is the set of strand ids `concluded` at the previous season boundary: how many of those are still concluded strands now." "It reads `Flows` and `Move` fields that exist (`doer`, `opens`, `terminal`, `index`); it adds no roster."
  2. Edit 4: "`opening_routes` stays static. `strands_block` already holds the world; beside `route check: X of Y pairs have no act route` it prints, per terminal code with a static route, the executed count of that route's verbs over the run (from `corpus_run.attempts`, the one owner of made and refused), and marks a code whose every terminal verb executed 0 times `ROUTE, NEVER TAKEN`."
- WHERE: `engine/season/harness/strife.py` (`strands_block`; its `earlier=` keyword, default `None`).
- TESTS: `engine/season/tests/test_storybar.py` gains `test_a_planted_opened_escalated_closed_strand_reads_closed_one` and `test_a_planted_executed_determine_clears_route_never_taken` `[ASSUMPTION: test names and file; the source names the falsifier plants, no test; E-3]`, written before the edits and read red.
- FALSIFIER and CONTROL: "Edit 3: a plant of one opened, escalated, closed strand reading `closed 0`." "Edit 4: a planted executed `determine` leaving `ROUTE, NEVER TAKEN` on XS." Control: `build_realm(0)`'s content hash and the one- and two-season pins unchanged.
- GATE: `python -m pytest engine/season/tests/test_storybar.py -q` → pass; `python -m engine.season.harness.strife 2 0 1 2 --strands` → a `shape:` line per seed and at least one `ROUTE, NEVER TAKEN` mark (the source's E-07 reading, three seasons: every code whose route is `determine`, `covenant`, `fight`, `pardon` or `seize`; read at two, A-114, and quoted).
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `harness/strife.py::strands_block`, `::opening_routes`, `::routeless_pairs`, `queries/world_q.py::concluded`, `::flows_in`, `harness/corpus_run.py::attempts`; V12 B36.01.
- GLOSSARY: none (*strand* exists).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B36's producer; `Item: B36.02`, `[skip ci]`.

### B36.03 — the chronicle prints why an act was taken · `09_WR_story_instruments_that_can_fail` edit 5 · BUILD · HASH EQUAL
- SOURCE: the same file, "Edit 5"; audit `09_WR_audit.md` §5.5 (the reason trail).
- ADVANCES: R-04.c1 (with B36.06: a line says why).
- INSTRUCTION (copied): `engine/season/harness/chronicle.py::lines`, `render`: "`soak._occasion_row(d, act)` already returns the question an act answered (`source`, `about`, `referents`); `arc.py` reads it. The chronicle renders `answers N. <actor> <verb>` for a cross-person antecedent and nothing for an act that answered a standing ambition. Add a `why` field to each line: for a `need` question, `pursuing <Proposition id, and its predicate where the store holds one>`; for `claim_landed`, `on learning <claim predicate> about <subject name>`. It reads the driver's `Scene`, as `arc.py` does." The CORE interface the source names under this edit (the question carried in an act's first Event's `observed`) is not built here (the batch's "Not in this batch" list).
- WHERE: `engine/season/harness/chronicle.py` (`lines`, `render`).
- TESTS: `engine/season/tests/test_in37_chronicle.py` gains `test_a_line_for_a_need_act_says_what_it_pursued` `[ASSUMPTION: test name; E-3]`, written first on a planted driver whose act answered a `need` question, read red; `test_the_render_changes_nothing_in_the_world` stays green.
- FALSIFIER and CONTROL: a line for an act whose `Scene` answered a `need` question with no `why`; control: the render moves no content hash, log length or write list (the file's existing test).
- GATE: `python -m pytest engine/season/tests/test_in37_chronicle.py -q` → pass; `python -m engine.season.harness.chronicle --seed 0 --seasons 2` → lines carry `pursuing …` or `on learning …` where the driver holds the occasion.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `harness/soak.py::_occasion_row`, `harness/chronicle.py::lines`, `::render`; V12 B36.01.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B36's producer; `Item: B36.03`, `[skip ci]`.

### B36.04 — closes by act and by clock · `09_WR_B_readings_of_closure_and_tension` edit 1 · BUILD · HASH EQUAL
- SOURCE: `proposals/09_WR_B_readings_of_closure_and_tension.md` "The resolution, decided" (R-29), "Edit 1", "The gate" (1), (2), "The falsifier"; rulings A-45 (per strand), the brief's "we do not do deterministic"; C3-K7, C3-Y9; closes F-WR-13.
- ADVANCES: none of the nine by itself; the no-player half's endings become countable (clause 6 of `20_NARRATIVE_F`'s bar).
- INSTRUCTION (copied):
  1. `engine/season/harness/arc.py` gains, beside `ARC_SELF` and `ARC_WORLD`:
     ```python
     CLOSE_CELLS = frozenset({("Tenure", "until"), ("Person", "exists"), ("DocketItem", "matter"),
                              ("Rung", "exists"), ("Office", "exists")})

     def closes(log, act_of: dict, bounds: list) -> list[dict]:
         """Per season: {"by_act": Counter(kind), "by_clock": Counter(kind)} over Events whose Receipts write a
         CLOSE_CELLS cell; by act iff the Event's id is in `act_of` (the fold emitted it). Reads only."""
     ```
     "asserted at import to be a subset of their union plus `("Person", "exists")`."
  2. "The clock half is split … A close *by term* is a Tenure whose `until` was set by a declared `Term` …: bookkeeping, which the rule permits. Every other MATTER close is *by threshold* … The split is structural: a closing Event whose causes include a `Term`'s declaring act through `Tenure.term` is `term`; any other non-act close is `threshold`."
  3. `engine/season/harness/storybar.py::main` prints, under the per-season block, one line per season: `closes season=<s> by_act=<n> by_clock=<n> (term=<n> threshold=<n>) | <kind=n, …>`.
  4. "`strife.py`'s strand-shape line (the first lane's edit) splits its `closed` count into the same two, by calling `arc.closes` and not by re-deriving it." (A-45: per strand; the one-river reading kept as the control column.)
- WHERE: `engine/season/harness/arc.py` (`CLOSE_CELLS`, `closes`, the import-time assertion); `engine/season/harness/storybar.py` (`main`'s per-season block); `engine/season/harness/strife.py` (`strands_block`'s `shape:` line, B36.02).
- TESTS: `engine/season/tests/test_storybar.py` gains `test_a_planted_determine_and_a_lapse_read_by_act_one_by_clock_one` (the source's gate (2): "a planted world with one `determine` executed and one matter left to lapse reads `by_act=1 by_clock=1`") `[ASSUMPTION: test name; E-3]`, written first, read red (no `closes`).
- FALSIFIER and CONTROL: "A season with `by_act + by_clock` different from the number of Events writing a closing cell (the split lost one)". Control: `build_realm(0)` and the one- and two-season pins EQUAL with and without the line.
- GATE: `python -m pytest engine/season/tests/test_storybar.py engine/season/tests/test_cl_thrust_b01_arc_reader.py -q` → pass; `python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 2 --arms off` → a `closes` line per season. The source's gate (1) (season 5's `threshold` at least the `matter.lapsed` counts 8, 8, 7, six seasons) is past the cap and is not read here (six seasons in the source; A-114; B99's longer re-take may read it).
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `harness/arc.py::ARC_SELF`, `::ARC_WORLD`; `SeasonDriver.act_of`; V12 B36.01, B36.02.
- GLOSSARY: *close* by act / by clock (new row): "an ending made by someone's act, or one the season's clock made: a term maturing, a matter lapsing, a body falling"; *by threshold* is the clock's half that a fixed state decides.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B36's producer; `Item: B36.04`, `[skip ci]`.

### B36.05 — open situations, the wear rule, idleness, the flat control · `09_WR_B_readings_of_closure_and_tension` edits 2–4 · BUILD · HASH EQUAL
- SOURCE: the same file, "Edit 2", "Edit 3", "Edit 4", "The gate" (3)–(6), "The falsifier"; R-30; closes F-WR-15, F-WR-16, F-WR-21.
- ADVANCES: none of the nine; apparatus rows F3, F4 gain an observable.
- INSTRUCTION (one `storybar.py` commit, copied):
  1. Edit 2: `def situations(w) -> dict:` — "At a season boundary: {kind: frozenset(referent)} for the four kinds above, each a referent stamped for two or more persons by its one World-first stamper (or, for `war`, a pair `at_war` admits among persons present at one rung). Composes on `world_q`'s stampers; reads only; calls no `new_draw`." The four kinds: "`seat` (`vacancies`, and `ambitions` naming an Office), `matter` (`matters_awaiting`), `custody` (`detainees_held`), `war` (`at_war` over the faction pairs of persons present together). A kind with no stamper is not invented here." "`drive`'s existing `on_season` hook carries it: `storybar.main` gains `--situations`, which collects `situations(w)` after each season and prints per season `open=<n by kind> opened=<n> gone=<n>`, and `motion=<non-zero condition changes> crossings=<condition.band_crossed>` (R-30: a `condition.worn` Event counts only when its Receipt's before and after differ). No pass bar, no threshold."
  2. Edit 3: "The same block prints `idle=<persons with no executed act this season> of <persons>` and `idle_two=<persons idle two seasons running>`, computed from `read(...)["executed"]`'s `actor` field."
  3. Edit 4: "`storybar.main` gains `--control {none,flat}` (no default other than `none`, which is today's reading; the seed and season count stay required, `tools/ci_sim_fabrication_check.py`'s scope). `flat` builds the realm with `build_realm(seed, goals=False)`, calls `decision_spread.apply_control(w)`, and runs `drive(..., world=w)` inside `decision_spread.no_goals()`. Every reading above, `--chains` and the act mix print for both. `decision_spread` does not import `storybar`, so the edge adds no cycle."
- WHERE: `engine/season/harness/storybar.py` (`situations`, `main`'s `--situations`, `--control`).
- TESTS: `engine/season/tests/test_storybar.py` gains `test_two_persons_on_one_vacant_seat_read_open_seat_one` (gate (3): "two persons stamped on one vacant seat reads `open seat=1`, and one person alone reads 0") and `test_situations_moves_no_hash_and_no_draw_ordinal` (the falsifier) `[ASSUMPTION: test names; E-3]`, written first, read red.
- FALSIFIER and CONTROL: "a `situations` call that moves the content hash or the draw ordinal (it read the World lawlessly); a `flat` control whose hash equals the shipped arm's (the control did nothing)". Control: gate (6), "`build_realm(0)` and the one- and two-season pins are EQUAL with and without each flag".
- GATE: `python -m pytest engine/season/tests/test_storybar.py -q` → pass; `python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 2 --arms off --control flat --situations` → the flat arm's hash differs from the shipped arm's (gate (5) quotes EB-01's `1e202aff…` at seed 0 and `e48c989e…` at seed 1 on an older tree: the two hashes are recorded, not compared to those); the `motion=` and `idle=` lines printed (gate (4)'s "74 where 322" is quoted from the source's tree, read here and recorded).
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `queries/world_q.py::vacancies`, `::matters_awaiting`, `::detainees_held`, `::at_war`, `::ambitions`; `harness/decision_spread.py::apply_control`, `::no_goals`; `boot/realm.py::build_realm(goals=…)` (B03c); V12 B36.04.
- GLOSSARY: *situation* (new row): "a matter that two or more persons are caught in at once: a vacant seat, a matter awaiting judgment, a man in custody, a war"; *idle* uses the plain word.
- NAMES: `harness/populated.py::build_realm` → `boot/realm.py::build_realm` (B03c).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B36's producer; `Item: B36.05`, `[skip ci]`.

### B36.06 — the chronicle says what each act was about, starts from a close, and can be focalized · `09_WR_B_chronicle_that_tells` edits 1–4 · BUILD · HASH EQUAL
- SOURCE: `proposals/09_WR_B_chronicle_that_tells.md` "The resolution, decided" (R-28, R-32), "The edits" 1–4, "The gate", "The falsifier"; rulings A-49, A-33, A-43; C3-Y9, C3-L4; closes F-WR-14.
- ADVANCES: R-04.c1 ("`chronicle --seed 0` tells", IS-A §2).
- INSTRUCTION (copied; `engine/season/harness/chronicle.py`):
  1. "`lines()` gains an `"about"` field: `_name(persons, subject_of(act))` when the act has a subject, else `""`. `render()` prints it after the verb: `<actor> <verb> <about> | emitted …`." An act line's subject is `state/carriers.py::subject_of(act)`; an Event line's is `state/attribution.py::anchor_of(w, e)`; "nothing here may reintroduce one by reading the write call's `subject=` keyword off the log."
  2. "`deepest_chain(rows)` keeps its signature for `--pick depth`; a new `closing_chain(rows, log, act_of)` is the default pick (`--pick close`), choosing the end as above and walking back with the rarity rule. Both are pure over their arguments." The rule: "The pick's end is an act whose own Event writes a closing cell (`arc.CLOSE_CELLS`); when several do, the rarest Event kind in the seed's log wins, then the latest season, then log order. When no act closed anything, the pick falls back to today's depth rule and the header says so." "Ties walking back are broken by rarity of the antecedent's verb within the seed, then by log order … the act-id order is retired."
  3. "`--focus <pid>` (no default) restricts the rows to acts any of whose Events `pid`'s own ledger holds a claim of, read through `account` …, and tags each line `saw` / `inferred` from the row's source. The header names the focalizer: `chronicle … focus=<pid>`." `account` is called as `11_GO_player_surface_contract_B` §4 declares it, `account(w.persons[pid], since=(0, 0))` (UNDECIDED (5)); "a claim deposited by a witnessing channel is `saw`; one deposited beside a finding, FI-03's two-cause deposit, is `inferred`". `projection` / `witnessed` are not read (deleted by B03's `17_CENSUS_C1A_01` D2).
  4. "The module docstring's THE PICK paragraph is rewritten to the rule above; the `[ASSUMPTION]` tag on CR-68's selection is kept." The omniscient render is the end reveal's body (A-49): the docstring says so in one sentence. "`--seed` and `--seasons` stay required."
- WHERE: `engine/season/harness/chronicle.py` (`lines`, `render`, NEW `closing_chain`, `main`'s `--pick`, `--focus`, the docstring).
- TESTS: `engine/season/tests/test_in37_chronicle.py` gains, written first and read red: `test_every_line_with_a_subject_names_it` (gate (1)); `test_a_planted_detain_determine_fight_reads_back_from_the_death` (gate (2): "a planted `detain → determine → fight` with a death reads back from the death, three lines, three subjects"); `test_equal_depth_walk_back_takes_the_rare_verb` (gate (4): "one verb seen once and one seen fifty times, walks back through the rare one"); `test_focus_tags_saw_and_inferred` (gate (5)) `[ASSUMPTION: test names; E-3]`; gate (6) "the existing hash-and-write-list test is green unchanged".
- FALSIFIER and CONTROL: "A rendered line whose `about` names an id that is not the act's `subject` operand …; a `--pick close` render at a seed with a death that does not end on it; a `--focus` render containing an Event the focalizer holds no deposit for." Control: `test_the_render_changes_nothing_in_the_world`; `--pick depth` reproduces the pre-edit render.
- GATE: `python -m pytest engine/season/tests/test_in37_chronicle.py -q` → pass; `python -m engine.season.harness.chronicle --seed 0 --seasons 2 --chains --min-depth 2` → every line with a subject names it (R-04.c1's reading, quoted in the close); gate (3) (seed 1, six seasons, the chain ends on `person.died`, `matter.determined` or a `tenure.closed`) is read at two seasons where such an Event exists, otherwise the header's "no act closed anything" line is quoted (six seasons in the source; A-114).
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `state/carriers.py::subject_of`, `state/attribution.py::anchor_of`, `harness/chronicle.py::deepest_chain`, `::_name`; V12 B36.04 (`arc.CLOSE_CELLS`); V12 Batch B34 (`decision/sheet.py::account`, `11_GO_player_surface_contract_B` §4); V12 Batch B03 (`17_CENSUS_C1A_01` D2).
- GLOSSARY: *focalized telling* (row exists as *journal*/*telling*, A-49): its owner column points at `chronicle.py --focus` for the harness and at B36.08 for the in-play journal.
- NAMES: `account`'s `since=(tick, round)` → `(tick, lap)` (B04, `PCR-4`).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B36's producer; `Item: B36.06`, `[skip ci]`.

### B36.07 — the case thread · `19_LACUNA_verdict_ladder_and_reversal` R-19-09 · BUILD · HASH EQUAL
- SOURCE: `proposals/19_LACUNA_verdict_ladder_and_reversal.md` "R-19-09 · The case thread (harness)", "Exact edits" 6, "Gate" (last bullet), "Named tests" (B36's); C3-Y9; U3 §4.1 row 83.
- ADVANCES: none of the nine; a case can be retold (R-04.c1's chronicle, supplementary).
- INSTRUCTION (copied): "`harness/chronicle.py` gains `case_thread(w, case_file_id) -> list[line]`: from the determination (or dismissal, voiding, reversal) back through the case file's stages to the first deed claim each filed item cites, printed with `subject_of` / `anchor_of` as `09_WR_B_chronicle_that_tells` decides, and from a viewpoint where asked (`account` …; `world_q.projection` is deleted by C1A_01 D2, C3-L4). … It is how the realm 'retells' a case: who did it, who said so, on what, what the bench held, what later contradicted it. Reads only; asserts the content hash unchanged after a render, as `test_in37_chronicle.py` does." The viewpoint is B36.06's `--focus` selection, reused.
- WHERE: `engine/season/harness/chronicle.py` (NEW `case_thread`); `engine/season/tests/test_in37_chronicle.py`.
- TESTS: `engine/season/tests/test_in37_chronicle.py::test_case_thread_render_moves_no_hash` (named by the source), with a planted determined case file: "`case_thread` on the determined case prints the determination, each filed item and the deed claim it cites; the content hash is unchanged by the render". Written first, read red (no `case_thread`).
- FALSIFIER and CONTROL: a case thread that omits a filed item the case file's stages hold, or a render that moves the content hash. Control: B36.06's render of the same world, unchanged.
- GATE: `python -m pytest engine/season/tests/test_in37_chronicle.py -q` → pass.
- HASH MOVERS: none.
- DEPENDS ON: V12 B36.06; V12 Batch B27 (`19_LACUNA_verdict_ladder` R-19-07, R-19-08: the `voided` / `reversed` stages; `05_SC_acquittal`); V12 Batch B24 (`05_SC_evidence_and_rebuttal_B`'s case file).
- GLOSSARY: *case thread* (new row): "the story of one case told back from its verdict to the deeds it rests on".
- COST and TIER: edit (harness); `sonnet`, `high`.
- LANDS IT: B36's producer; `Item: B36.07`, `[skip ci]`.

### B36.08 — the focalized journal · NM-W5 · BUILD · HASH EQUAL
- SOURCE: the intake `:213` (NM-W5; `settled:` "`09_WR_B_chronicle_that_tells.md:63`: 'The journal NM-W5 owes ... is not built here'"); carry-forward `master/eval/E2.md:532` ("NM-W5, amended by the decision round") and `E4.md:3990`; home `proposals/2026-10-13-narration-mechanisms.md` §4 W5 (with the §A.2 row struck from its "Where" and "Co-edit" lines, M12 taken (a)); rulings A-49 (the focalized journal is the in-play telling), A-33, A-43; placement: after the item whose source names its id (B36.06's), because that source says the journal "composes on this" (§5.6, its own text); closes NM-W5.
- ADVANCES: none of the nine; A-49's in-play telling gets its one person-side reader.
- INSTRUCTION:
  1. Open `engine/season/decision/sheet.py::account` (B34) and `04_CODE_ARCHITECTURE.md` §A.2 and §C.11 at this tree, and record in the commit body whether the journal can be built from `account`'s rows alone. W5's statement, copied: "A `person_q` function in the §C.11 `explain` shape: no `World` parameter, no walk from `causes[]` to `Act.actor`. It selects from the focalizer's own claims and Scenes; takes text fields from each claim's `seen` struct; prints `who` and `why` per section 3.3 rule 1; tells appraisal through `deeds_judged`, labelled as the person's own". The relevance is the ledger (A-9): it takes the Questions already raised for that person "and never recompute[s] them".
  2. Build it as `journal(p, since) -> tuple[str, ...]` in `engine/season/queries/person_q.py` `[ASSUMPTION: the name and signature — basis: W5's "a `person_q` function"; `account(p, since)`'s shape, which it composes on]`, over `account(p, since)`'s rows (B34; the one person-side reading R-32 names): each line `saw` or `inferred` from the row's source as B36.06 tags it; a covered actor's act whose `seen.who` is `None` prints unattributed; a person at low legibility appears by his acts with no reason line (A-43); a death is told only to a holder who learned of it by presence, trail or telling (A-33). `skills/prose-writer/SKILL.md:158`'s "The player's vantage is genuinely omniscient" is narrowed in the same commit to the instrument chronicle (the carry-forward: "narrowed in NM-W5's commit").
  3. STOPS IF step 1 finds the journal must read Scenes and Scenes are not person-side: then "the §A.2 row is owed and lands with NM-W5 as a Layer 1 hunk" (the carry-forward, M11 answered (a), ED-IN-0300, `[ASSUMPTION; medium; Jordan to correct]`): a Layer 1 edit is Jordan's amendment, so the item is HELD (trigger: the §A.2 row amended) and leaves for the held list at the expunge; nothing else of the batch waits on it.
- WHERE: `engine/season/queries/person_q.py` (NEW `journal`); `skills/prose-writer/SKILL.md` (line 158's sentence); NEW `engine/season/tests/test_journal.py` `[ASSUMPTION: file name; E-3]`.
- TESTS: in the new file, written before step 2 and read red: `test_journal_emits_no_field_its_seen_struct_lacks` (W5 falsifier 1: "Fields the journal emits that the focalizer's `seen` struct lacks: 0"); `test_unseen_actor_prints_unattributed` (the carry-forward's planted failure: "a covered actor's act reaching the focalizer with `seen.who = None` prints unattributed (planted failure: `actor_of` passed in reddens)"); `test_two_persons_sharing_a_reach_get_different_journals` (W5 falsifier 3); `test_a_journal_call_per_person_moves_no_hash`. `[ASSUMPTION: test names; the item creates them (E-3) — basis: the names appear in no source file of the suite; K9 added this mark]`
- FALSIFIER and CONTROL: W5's three, "the control for (1) being the instrument's field count over the same focalizer (above 0) against the journal's 0". HASH control (the carry-forward's EXIT): "`content_hash()` of `build_realm(0)` over two seasons is equal with and without a journal call per person per season". W5 falsifier 2 (player coupling, a scripted callback) has no seat to run in this tree and is not read here.
- GATE: `python -m pytest engine/season/tests/test_journal.py -q` → pass; `PYTHONHASHSEED=0`, `build_realm(0)` two seasons with and without a journal call per person per season → equal content hash.
- HASH MOVERS: none ("HASH: EQUAL, asserted").
- DEPENDS ON: V12 B36.06 (`--focus`'s `saw`/`inferred` rule); V12 Batch B34 (`decision/sheet.py::account`); EXISTS-IN-TREE `queries/person_q.py::deeds_judged`; NM-W1: SUPERSEDED by `09_WR_B_chronicle_that_tells` (`master/V11_EVALUATION_part2.md:288`), met by B36.06.
- GLOSSARY: *journal* (row exists, A-49): its owner column becomes `person_q.journal`; "a person's own account of the season, told only from what he holds".
- COST and TIER: small build; `sonnet`, `high` (the carry's "second tier"); step 1's Layer 1 reading `opus`.
- LANDS IT: B36's producer; `Item: B36.08`, `[skip ci]`.

### B36.09 — CALENDAR fires what is due, not only what is due today · `16_PESSIMIST_WR_D` edit 1 · BUILD · HASH EQUAL (asserted)
- SOURCE: `proposals/16_PESSIMIST_WR_D_small_clock_repairs_and_two_readings.md` "Edit 1"; rulings A-47 (a clock's tick opens a question and decides nothing by itself); closes F-PES-WR-01.
- ADVANCES: none of the nine; S (one methodology for the three clock comparisons: CR-55's `<=`, `matter.py`'s, CALENDAR's).
- INSTRUCTION (copied): `engine/season/loop/calendar.py`, the due test. Old: `if d.get("due_at") != w.tick:` / `continue`. New:
  ```python
  due = d.get("due_at")
  if d.get("fired") or due is None or due > w.tick:
      continue
  ```
  "a Date whose `due_at` has passed unfired fires at the next CALENDAR barrier, once. No committed world holds such a Date, so every base hash is expected EQUAL (asserted, not assumed)."
- WHERE: `engine/season/loop/calendar.py` (the due test); `engine/season/tests/test_sc01_fired_slot.py`.
- TESTS: `engine/season/tests/test_sc01_fired_slot.py::test_due_date_in_the_past_fires_once` (named by the source): "P4's three planted Dates (the scratch `p4_small` plant, written in the test) all read `fired=True` after two barriers, each exactly one `date.fired`" — three Dates planted at tick 2 on a seated venue, due at ticks 1, 2 and 3. Written first, read red (the Date due at 1 never fires).
- FALSIFIER and CONTROL: "A Date fired twice, or a base hash that moves." Control: every committed golden unmoved ("`report` / `delta HEAD`, `PROBE FLIPS 0`").
- GATE: `python -m pytest engine/season/tests/test_sc01_fired_slot.py -q` → pass; the realm content hash (`HASH READING`) at seed 0, one season → equal to B36.08's reading; `python -m engine.season.harness.report && python -m engine.season.harness.delta HEAD` → `PROBE FLIPS 0` (`harness/delta.py`'s docstring: run `report` first, or the comparison is vacuous).
- HASH MOVERS: none expected (asserted); if a base hash moves, stop: the edit reached a committed world, and the item says which.
- DEPENDS ON: EXISTS-IN-TREE `loop/calendar.py` (the `due_at` test), `engine/season/tests/test_sc01_fired_slot.py`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B36's producer; `Item: B36.09`, `[skip ci]`.

### B36.10 — `thread_read` is aimed at a place · `16_PESSIMIST_WR_D` edit 2 · BUILD · HASH MOVER(behaviour)
- SOURCE: the same file, "Edit 2", "Cost class" (the declared mover); rulings A-40 (one Site per territory); closes F-PES-WR-04.
- ADVANCES: none of the nine; R-05's `thread_read` stays built out, on its premise's object.
- INSTRUCTION (copied): "The row gains `referent_class: Site`, on `restore`'s precedent (REM-22, the same file, with the same declared consequence). With `16_PESSIMIST_WR_B_the_calamity_strains_and_breaks.md` edit 4 (a crossing a person stands beside carries the Site) the verb then forms where the fabric is strained, for the four people who clear the gate. What it *finds* there is the `threadwork.read` entry of `09_WR_B_threadwork_session_and_practitioner.md` (R-21), drawn; until that lands a formed reading still finds nothing, and that is said in the row's note rather than hidden." `engine/season/verb_table.yaml`, row `thread_read`: `referent_class: Site` and a `referent_class_note:` in the form of the row's neighbours (the source, the measured before and after of this commit's gate, `REVERT: delete this column`). Both named edits have landed (B12c, B35), so the note records what it finds.
- WHERE: `engine/season/verb_table.yaml` (`thread_read`); `engine/season/tests/test_in12_step9.py`.
- TESTS: `engine/season/tests/test_in12_step9.py::test_thread_read_forms_on_a_site_and_not_on_a_record` (named by the source): "a practitioner standing at a Site named by his question forms `thread_read` on it; a question naming a Record forms none". Written first, read red.
- FALSIFIER and CONTROL: "A `thread_read` in any realm run whose subject is not a Site." Control: the other rows with a `referent_class` form as before (`test_in12_step9.py`'s existing tests green).
- GATE: `python -m pytest engine/season/tests/test_in12_step9.py -q` → pass; `python -m engine.season.harness.aperture 2 --seeds 0 1 2`'s `BUILT OUT` line for `thread_read` → still built out (B35's close, `reading @<sha>`; a drop is this item's failure, `V12_STRUCTURE.md` §3's `IS-A-08` rule, and stops the batch); the realm content hash (`HASH READING`) at seed 0, one season → moved, as declared, recorded for B36.99.
- HASH MOVERS: "edit 2 moves any world in which `thread_read` formed on a Record or a person (sideways, declared)". B36's one re-pin, in B36.99.
- DEPENDS ON: EXISTS-IN-TREE `engine/season/verb_table.yaml` row `thread_read`, `restore`'s `referent_class` (REM-22); V12 Batch B12c (`16_PESSIMIST_WR_B` edit 4: the Site referent); V12 Batch B35 (`09_WR_B_threadwork_session_and_practitioner`: `threadwork.read`).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B36's producer; `Item: B36.10`, `[skip ci]`.

### B36.11 — the turn: who closed what another opened · `16_PESSIMIST_WR_D` edit 4 · BUILD · HASH EQUAL
- SOURCE: the same file, "Edit 4"; C3-K7 (after `09_WR_B_readings`); closes F-PES-WR-05.
- ADVANCES: none of the nine; whether anything turned is readable.
- INSTRUCTION (copied): "`storybar.py` gains `turns(w, act_of) -> dict` with exactly that classification (`{"by_subject": n, "by_another": n, "by_clock": n, "deaths_by_act": n}`), printed on the per-seed line beside the executed summary. It reads the Tenure store, the log and `act_of`; it grades nothing and stores nothing, as the module's header requires. It is the third column of the `by_act` / `by_clock` split `09_WR_B_readings_of_closure_and_tension.md` edit 1 adds, and lands with it." The classification: "for every non-`contain` Tenure closed in the run, the act that opened it and the act that closed it, classed as closed by its own subject, by another person, or by a clock". `by_clock` is read through `arc.closes` (B36.04), not re-derived.
- WHERE: `engine/season/harness/storybar.py` (NEW `turns`; the per-seed line).
- TESTS: `engine/season/tests/test_storybar.py::test_turns_counts_a_revocation_by_another` (named): "a planted world in which A confers and B revokes reads `by_another == 1`; the same world with A revoking his own grant reads 0." Written first, read red.
- FALSIFIER and CONTROL: a planted revocation by another reading 0; control: the self-revocation plant reads 0 and the content hash is unmoved by the call.
- GATE: `python -m pytest engine/season/tests/test_storybar.py -q` → pass.
- HASH MOVERS: none.
- DEPENDS ON: V12 B36.04, B36.05; EXISTS-IN-TREE `w.tenures`, `SeasonDriver.act_of`.
- GLOSSARY: *turn* (new row): "an ending one person brings on what another began".
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B36's producer; `Item: B36.11`, `[skip ci]`.

### B36.12 — a cut arm and the noise floor; CALENDAR kept and marked unproven · `16_PESSIMIST_WR_D` edits 5, 3 · BUILD · HASH EQUAL
- SOURCE: the same file, "Edit 5", "Edit 3"; closes F-PES-WR-09.
- ADVANCES: none of the nine; an arm comparison can be told from noise.
- INSTRUCTION (copied): Edit 5: "(a) `ARMS` gains `no_calendar` (the driver's CALENDAR step returns `[]`), composed as the forcing arms are. (b) `compare` prints, per pair of arms, the L1 distance of the executed-verb counts and, once per seed, the same distance between two draw seeds of the first arm. A reader then sees `no_calendar 38 · noise 316` and knows what it means." `no_calendar` is a mapping entry like B36.01's; the CALENDAR suppression is applied by `drive` from the arm, not by a fixture (no fixture exists for it) `[ASSUMPTION: the mechanism — basis: the source's "the driver's CALENDAR step returns `[]`"; a driver-side flag in the harness, the loop unedited]`. Edit 3 (no code edit): the commit body records, copied, "CALENDAR stays, and is marked unproven … Decided at ladder step 5: keep the barrier; its N-line is recorded as resting on `determine` executing (SC F-SC-01), and edit 5 gives the cheap reading that says when it has become true."
- WHERE: `engine/season/harness/storybar.py` (`ARMS`, `drive`, `compare`).
- TESTS: `engine/season/tests/test_storybar.py::test_no_calendar_arm_emits_no_date_fired` and `::test_compare_prints_a_nonzero_noise_line` "on `build_realm`" (named), written first, read red.
- FALSIFIER and CONTROL: "The arm's distance exceeding the noise at two seeds once `determine` executes is the signal that edit 3's N-line has become true; that is a reading, not a blocking check." Control: `--arms off off` still EQUAL.
- GATE: `python -m pytest engine/season/tests/test_storybar.py -q` → pass; `python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 2 --arms off no_calendar` → a distance and a `noise` line printed and quoted.
- HASH MOVERS: none.
- DEPENDS ON: V12 B36.01 (`ARMS` a mapping), B36.11; EXISTS-IN-TREE `harness/storybar.py::compare`, `::draw_seed_arm`.
- GLOSSARY: *noise floor* (new row): "how far two draws of the same world lie apart, the yardstick an arm's difference is read against".
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B36's producer; `Item: B36.12`, `[skip ci]`.

### B36.13 — the overlaps block, its arms and its tests · `20_NARRATIVE_F` edits 1–4 · BUILD · HASH EQUAL
- SOURCE: `proposals/20_NARRATIVE_F_story_inventory_and_gate.md` "Exact edits" 1–4, "The gate" (the bar), "The falsifier"; rulings A-45, A-46, A-15, A-80, A-83 (the arms they add land in B38); C3-K7, C3-K2; U3 §4.1 row 88 (the G5 split lands in B38).
- ADVANCES: none of the nine; the measure the five `20_NARRATIVE` proposals of B38 gate on.
- INSTRUCTION (copied, `engine/season/harness/storybar.py`):
  1. "`overlaps(w, d, bounds, snaps) -> dict`, behind `--overlaps`. `snaps` is a per-season snapshot taken in `on_season` of the person-side readings (so a pull is read as it stood when the act was formed, never from the end state). Classes, each counted over **executed** acts (`corpus_run.attempts`, the one owner of made and refused)": G1 a due unmet, answered (reads `20_NARRATIVE_B`); G2 a stand against his own side (`20_NARRATIVE_D`); G3 a new holder meets an old oath (`20_NARRATIVE_C`); G4 an enemy with a place (`20_NARRATIVE_C`); G5 across a fault line (`20_NARRATIVE_A`); G6 a conviction broken and seen (`16_PESSIMIST_CHAR_A`'s `conviction.moved`, the one emitter); `closes` (B36.04's `arc.closes`, called). Each class's "counted when" is the source's table, copied into the function's docstring. "Until a proposal lands its class prints `n/a (no reader)`, never 0: an absent reading is not a zero" — "detected by import of the reader's symbol, never by a zero". At this batch G1 to G5 print `n/a`; G6 reads (B10 landed `16_PESSIMIST_CHAR_A`).
  2. Three lines: "*occasion of the strife verbs*: for `march`, `challenge`, `seize`, `raze`, `arrest`, `petition`, `oblige`, `release`, the five commonest `(question source, claim predicate)` of formed and of executed acts; *world Event → executed act*, by world kind and verb; *the reign*: `(year, season of year, believed holder of the realm's head seat by plurality of ledgers)` per season, for the chronicle's date line … no state is stored, and 'by plurality of ledgers' is said in the line".
  3. Arms: "`noconv` (every `Person.conviction` cleared at build: `decision_spread.apply_control`'s precedent for a build-time ablation) and `basis_off` (every fixture of `20_NARRATIVE_A` to `E` at its control)". No such fixture exists before B38, so `basis_off` ships as `{}` with the comment that B38's items add each fixture as it lands (UNDECIDED (6)); the `on` arm the source's gate names is not built here.
  4. `engine/season/tests/test_storybar.py`: "`test_g1_planted_lapsed_oath_reads_one_and_zero_without_the_belief`, `test_g5_told_claim_across_an_incompatible_pair_reads_minus_one`, `test_class_with_no_reader_prints_na`, `test_overlaps_block_moves_no_hash`". G1's and G5's tests are written now and skip with the reason "reader lands in B38 (`20_NARRATIVE_B`, `20_NARRATIVE_A`)" until then `[ASSUMPTION: skip, not delete — basis: the readers are later batches'; a skipped test is listed in the close]`.
- WHERE: `engine/season/harness/storybar.py` (NEW `overlaps`, `--overlaps`, the three lines, arms `noconv`, `basis_off`); `engine/season/tests/test_storybar.py`.
- TESTS: step 4's four; `test_class_with_no_reader_prints_na` and `test_overlaps_block_moves_no_hash` read green at this close.
- FALSIFIER and CONTROL: "Clause 2 passing under `basis_off`: the classes are too loose"; "Clause 4 failing with clause 2 passing: the overlaps are scripted by the build"; "A class above zero whose acts, read in the chronicle, do not read as that story to a person" (one rendered instance per class per seed is printed for this check). Control: `test_overlaps_block_moves_no_hash`.
- GATE: `python -m pytest engine/season/tests/test_storybar.py -q` → pass (two skips named); `python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 2 --arms off noconv --overlaps --executed-only` → G1–G5 `n/a (no reader)`, G6 a count, the three lines printed (six seasons and five seeds in the source; A-114; the bar's clauses are B36.R1).
- HASH MOVERS: none.
- DEPENDS ON: V12 B36.04 (`closes`), B36.01 (the arms mapping), B36.12; V12 Batch B10 (`16_PESSIMIST_CHAR_A`: `conviction.moved`); EXISTS-IN-TREE `harness/decision_spread.py::apply_control`, `harness/corpus_run.py::attempts`; the readers of G1–G5: V12 Batch B38 (PROPOSED).
- GLOSSARY: *overlap* (row exists: the story bar's sense of "crossing"): owner column → `storybar.overlaps`.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B36's producer; `Item: B36.13`, `[skip ci]`.

### B36.14 — the story count: shapes, the first table, the plants · `23_STORY_D` edits 1, 2, 5 · BUILD · HASH EQUAL
- SOURCE: `proposals/23_STORY_D_story_census_and_gate.md` "Exact edits" 1, 2, 5, "The gate", "The falsifier"; rulings A-9, A-15, A-19, A-23, A-35, A-38, A-46, A-51 (the U5d fold: every reading after the five-year prologue), A-59, A-77, A-80, A-81; C3-K7; ED-IN-0225 (no carrier for a story).
- ADVANCES: none of the nine; the story count every later enablement batch is read on (B38's `30_WR_E` extends it).
- INSTRUCTION (copied, `engine/season/harness/storybar.py`):
  1. Edit 1:
     ```python
     class Beat(NamedTuple):
         kinds: tuple          # Event kinds, any of
         role: str = "any"     # "any" | "other" (actor differs from the opening's) | "same" | "counterparty"
                               # (the Event's subject is the opening's actor) | "world" (no act emitted it)
         bands: tuple = ()     # degrees admitted; () is any

     class Shape(NamedTuple):
         id: str               # "S-32"
         name: str
         opening: Beat
         turn: Beat
         close: Beat
         cost: tuple           # matrix fields a party must lose on: ("Person.body", "Rung.stores", …); () = none asked
         window: int           # seasons from opening to close
         variant: str          # what the close is read by: "kind" | "band" | "kind+band" | "party"

     def stories(w, d, bounds, shapes=SHAPES, seat=None) -> dict:
         """{shape id: [Instance(season, opening, turn, close, parties, variant)]} — pure, over the log,
         `d.act_of`, the act store and the Tenures. A beat matches an Event of one of its kinds whose role
         constraint holds. Beats are LINKED: the turn has the opening among its ancestors and the close has
         the turn, through `causes[]`, an act and the Events it emitted being one node (`read`'s graph) and
         a `claim.deposited` Event a pass-through (so 'the news reached him and he acted' is a link).
         An instance is counted once, at its close. `cost` holds when a receipt with a non-None `delta` on
         one of the named fields falls on a party between opening and close."""
     ```
     "A shape any of whose kinds no verb row and no MATTER pass emits prints `n/a (no emitter)`, computed from the loaded kind table (`data/verbs.py`), never from a hand list." "`cost` prints `n/a` until `16_PESSIMIST_CORE_the_record_holds_what_changed.md` edit 1 lands …, and the instance is then counted without it and marked `(cost unread)`" (it landed in B09: `cost` is read). "`SHAPES` is data in this module, as `ARMS` is."
  2. Edit 2, `SHAPES` = the first table, copied row for row (C-a the petition that lapses; C-b the march that meets nobody; C-c a stale store corrected; S-32 a famine; S-04 a contested succession; S-02 a death reported; S-43 / S-44 a verdict, an acquittal; S-27 a duel; S-33 blame; S-68 the disaster), each row's opening, turn, close, cost and variant exactly as `23_STORY_D.md` "Exact edits" 2's table gives them. Kinds not declared at the tree (`succession.contested`, `matter.dismissed`, the challenge and acceptance kinds) make their row print `n/a (no emitter)`.
  3. Edit 5, `engine/season/tests/test_storybar.py`: "Per shape, planted logs: the full plant reads 1; each single beat removed reads 0; the plant's causes re-drawn by `edge_null` read 0; a shape with an unemitted kind reads `n/a`. One test asserts that it asserted (`assert checked >= len(SHAPES)`, §0.1 pt 2)." Tests: `test_each_shape_full_plant_reads_one`, `test_removing_any_single_beat_reads_zero`, `test_edge_null_redrawn_causes_read_zero`, `test_unemitted_kind_prints_na_no_emitter`, `test_checked_covers_every_shape`, `test_control_shapes_read_above_zero_on_the_shipped_realm`, `test_stories_block_moves_no_hash`.
- WHERE: `engine/season/harness/storybar.py` (NEW `Beat`, `Shape`, `SHAPES`, `stories`); `engine/season/tests/test_storybar.py`.
- TESTS: step 3's seven, written with step 1 and read red before it (no `stories`).
- FALSIFIER and CONTROL: "C0 failing: the story count cannot see a petition lapse"; "A shape above zero under `--null` as often as on the log: its link is coincidence"; "A shape above zero in the control arm at the on arm's rate"; "Any content hash moving: the block leaked into the loop." Control: `test_stories_block_moves_no_hash`.
- GATE: `python -m pytest engine/season/tests/test_storybar.py -q` → pass.
- HASH MOVERS: none.
- DEPENDS ON: V12 B36.01 (`edge_null`), B36.13 (the test file's overlaps block); V12 Batch B09 (`16_PESSIMIST_CORE_the_record_holds_what_changed`, `16_PESSIMIST_GAME_standing_occasions_carry_their_cause`); EXISTS-IN-TREE `engine.season.data.verbs.EVENT_KINDS`, `harness/storybar.py::read`.
- GLOSSARY: *story count* (row exists; "census" refused for it): owner column → `storybar.stories`; *shape* (new row): "the four beats and their links that make a kind of story, as a plot outline does".
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B36's producer; `Item: B36.14`, `[skip ci]`.

### B36.15 — the story count's switches and the seat reading · `23_STORY_D` edits 3, 4 · BUILD · HASH EQUAL
- SOURCE: the same file, "Exact edits" 3, 4, "The gate"; A-30 (the one `Draw` owner); `16_PESSIMIST_GO.md` §3.8 ("the story bar from a seat").
- ADVANCES: none of the nine; S-73's reading (a story a seat can follow).
- INSTRUCTION (copied): Edit 3: "`--stories` prints, per arm: per seed the count and variants of each shape; pooled, the seeds with one or more, the variant shares, and the instance rendered once per shape per seed by `chronicle.lines` (so a person can read whether it is that story …). Three switches, each composed from what exists: `--world realm|valley`: `valley` calls `harness/valley.py::build` (`07_SE_valley_scenario.md`); the default stays the realm; `--draw-seeds` (exists, REM-15) for clause C5; `--pin-rolls BAND`: a harness-only wrapper on the one `Draw` owner (`engine/dice_engine/draw.py`, B06; A-30), under which every graded draw returns `BAND`: the planted failure of clause C6. With `--null` the shapes are also counted over `edge_null(rows, seed)`." Edit 4: "`--seat PID` (the `seat` argument): the same shapes over one person's ledger: a beat counts only if that person holds a claim deposited from it."
- WHERE: `engine/season/harness/storybar.py` (`main`'s `--stories`, `--world`, `--pin-rolls`, `--null`, `--seat`).
- TESTS: `engine/season/tests/test_storybar.py::test_pin_rolls_returns_the_band_for_every_graded_draw` and `::test_seat_counts_only_beats_its_holder_holds` `[ASSUMPTION: test names; E-3]`, written first, read red.
- FALSIFIER and CONTROL: as B36.14; plus a `--pin-rolls` run whose graded draws do not all read the pinned band. Control: `--arms off off --stories` reads `EQUAL`.
- GATE: `python -m pytest engine/season/tests/test_storybar.py -q` → pass; `python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 2 --arms off off --stories` → `EQUAL`, the three control shapes above 0 at every seed (C0), every other shape 0 or `n/a`; `… --seasons 2 --stories --world valley --arms off off --base-seed 0 --n 3` → exit 0 (the source's gate runs 20 seeds at eight seasons, five at six: past the cap; A-114, read at B99's re-take).
- HASH MOVERS: none.
- DEPENDS ON: V12 B36.14; V12 Batch B12c (`harness/valley.py::build`); V12 Batch B06 (`engine/dice_engine/draw.py`, `Draw`); EXISTS-IN-TREE `harness/storybar.py::draw_seed_arm` (REM-15).
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B36's producer; `Item: B36.15`, `[skip ci]`.

### B36.16 — the arc reader gets an entry · `17_CENSUS_C1B_02` W-1 · BUILD · HASH EQUAL
- SOURCE: `proposals/17_CENSUS_C1B_02_wires.md` "W-1"; its `Reconciled:` line (W-1 after `09_WR_B_readings`, which also edits `arc.py`; `12_ARCS_case_on_the_realm`'s `match_beats` (B39) after W-1); closes census C1B §3.2's arc row.
- ADVANCES: none of the nine; a reading a session can run and quote.
- INSTRUCTION (copied): "Append to `arc.py`:"
  ```python
  def main(argv=None) -> int:
      """`python -m engine.season.harness.arc --seed S --seasons N`: persons with an arc, by four readings."""
      import argparse
      from . import storybar as SB            # lazy, as `read_arcs` already imports it: storybar builds the realm
      ap = argparse.ArgumentParser(description=main.__doc__)
      ap.add_argument("--seed", type=int, required=True)
      ap.add_argument("--seasons", type=int, required=True)
      ap.add_argument("--arm", choices=SB.ARMS, default=SB.ARMS[0])
      ap.add_argument("--cap", type=int, default=None)
      args = ap.parse_args(argv)
      w, d, _bounds = SB.drive(args.seed, args.seasons, args.arm, args.cap)
      on = ambition_thrusts(w)
      read = read_arcs(w, d, on)
      print(f"arc seed={args.seed} seasons={args.seasons} arm={args.arm} cap={args.cap}")
      print(f"  actors                       {len(read.persons)}")
      print(f"  no predicate (control)       {read_arcs(w, d).count()}")          # must be 0
      print(f"  on an ambition's thrust      {read.count()}")
      print(f"  shuffled-causes null         {read_arcs(w, d, on, log=shuffled_causes(w.log, args.seed)).count()}")
      print(f"  rosters ignored (upper bound) {read_arcs(w, d, on, unrestricted=True).count()}")
      print(f"  on-thrust acts behind a death {sum(len(v) for v in read.deaths.values())}")
      return 0


  if __name__ == "__main__":
      raise SystemExit(main())
  ```
  Correction at copy (UNDECIDED (4)): `default=SB.ARMS[0]` is written `default="off"` (B36.01 made `ARMS` a mapping). "Same argument names and the same `SB.drive` call as `harness/chronicle.py`" — the line citation is dropped (a file edited at B02).
- WHERE: `engine/season/harness/arc.py` (NEW `main`, the `__main__` guard).
- TESTS: `engine/season/tests/test_cl_thrust_b01_arc_reader.py::test_the_arc_entry_prints_a_zero_control` `[ASSUMPTION: test name; E-3]`, calling `main(["--seed", "0", "--seasons", "1"])` and asserting the control line reads 0; written first, read red (no `main`).
- FALSIFIER and CONTROL: "`read_arcs(w, d)` with no predicate must read 0 for every seed; a non-zero control means the reader counts acts that are on no thrust. And the null: if the shuffled count is not well below the real one across seeds 0 to 4, the reading is not about causes."
- GATE: `python -m engine.season.harness.arc --seed 0 --seasons 2` → exit 0, control 0 (the source measured, at its tree, actors 83, on a thrust 21, null 1, rosters ignored 53: quoted, re-read here and recorded); `python -m pytest engine/season/tests/test_cl_thrust_b01_arc_reader.py -q` → pass.
- HASH MOVERS: none ("Content hash EQUAL by construction").
- DEPENDS ON: EXISTS-IN-TREE `harness/arc.py::read_arcs`, `::ambition_thrusts`, `::shuffled_causes`; V12 B36.01, B36.04.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B36's producer; `Item: B36.16`, `[skip ci]`.

### B36.17 — `foreign_kinds` is printed where `unrowed_acts` is · `17_CENSUS_C1B_02` W-2 · BUILD · HASH EQUAL
- SOURCE: the same file, "W-2"; its `Reconciled:` line (W-2 lands in B36, against U3 §1 item 36's "not W-2": UNDECIDED (2)); U3 §5.1 `aperture.py` B36 → B37.
- ADVANCES: none of the nine; census C4's question, executed.
- INSTRUCTION (copied; the source's line numbers dropped, the symbols kept): "add `foreign_kinds` to the `from .corpus_run import …` line"; in the measured dict, beside `"unrowed"`, "`"foreign": {f"{v} -> {k}": n for (v, k), n in sorted(foreign_kinds(w).items())},`" ("string keys, because the dict is also pooled and reported"); in `report`, after the UNROWED line: "`out.append(f"  FOREIGN  Events of a kind the acting verb's row declares in neither column: {m['foreign'] or 'none'}")`"; "`pool_worlds` …: sum `foreign` across seeds as it sums `wrong_kind` (a Counter over the string keys)."
- WHERE: `engine/season/harness/aperture.py` (the `corpus_run` import, `instrumented_season`'s measured dict, `report`, `pool_worlds`).
- TESTS: `engine/season/tests/test_aperture.py::test_the_report_prints_a_foreign_line` `[ASSUMPTION: test name; E-3]`, written first, read red; `test_rem10_foreign_kinds_names_a_logged_kind_outside_both_of_the_rows_columns` stays green.
- FALSIFIER and CONTROL: "`test_aperture.py` already plants `("speak", "transfer.made")` and reads 1, so the reading can see what it excludes. If the line ever prints a pair, a verb row's `emits` is short of what the effect writes, and the correction is the row in `engine/season/verb_table.yaml`, not the reader."
- GATE: `python -m engine.season.harness.aperture 2 0` → prints the `FOREIGN` line (`none` at the source's tree, three seasons; A-114); `python -m pytest engine/season/tests/test_aperture.py -q` → pass.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `harness/corpus_run.py::foreign_kinds`, `::unrowed_acts`, `harness/aperture.py::pool_worlds`; V12 Batch B02 (`aperture.py`'s `CONTROL` line).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B36's producer; `Item: B36.17`, `[skip ci]`.

## Readings (B36)

**Reading 1 (B36.R1), the story bar at the close**, read on the closing tree after B36.17, quoted in B36.99's commit body. From `20_NARRATIVE_F` "The gate", copied: "It passes when all of these hold: 1. **A control.** Under `basis_off`, G1 to G4 and G6 read 0 at every seed … 2. **Non-degenerate.** Under `on` … 3. **Not one run.** … 4. **Not a fixed function of state.** … 5. **The modifiers are load-bearing.** Under `noconv`, G5's −1 and +1 counts and G6 fall to zero and G2 falls … 6. **Closures by persons.** Closing Events by act exceed closing Events by clock at two seeds or more … 7. **WR's bar.** `off all` prints DIFFER with more deaths in `all`; `off off` … prints EQUAL; the chain reading prints its edge null. 8. **The strife guard.** …" and "**Today** clause 1 holds and clauses 2, 5 and 6 fail … That is the bar failing on the shipped engine, which is what makes it a bar." From `23_STORY_D` "The gate": "the first prints EQUAL, the three control shapes above zero at every seed (clause C0), and every other shape 0 or `n/a` … The first run also reads C9's baseline (`null_scenes` on the shipped engine, expected above 0 there and 0 once A-81's writes land) and records it in the commit". At B36 the reading is taken at two seasons over seeds 0 to 2 (A-114): clauses 1, 6 and 7 and C0 are read and quoted; clauses 2, 3, 5 and 8 need the `on` arm (B38) and G1–G5's readers (B38) and are recorded as `n/a (no reader)`; C9's baseline is read where `--null-scenes` exists (B38's `30_WR_E`), else recorded as not yet runnable. The expected reading is the bar failing where the source says it fails; a clause that fails is a reading, not a failed gate.

### B36.99 — re-pin and close readings · E-1 · BUILD · HASH MOVER (the re-pin)
- SOURCE: `V12_STRUCTURE_part4.md` E-1, E-2; `V12_STRUCTURE_part2.md` §5.9, §5.12; `IS-A-12`.
- ADVANCES: R-04 (the readings of M4, written to `requirements.yaml`'s `reading:` records).
- INSTRUCTION: (1) re-record, once, the realm pins in `engine/season/tests/_realm_goldens.py` and every golden B36.10 moved, read against B35's close (`reading @<sha>`); the commit says "re-pin: `thread_read` forms only on a Site (B36.10); every other item of B36 is harness-only and read EQUAL". (2) Write R-04's conjuncts' `reading:` records in `engine/season/requirements.yaml` with this tree's SHA (R-04.c1: the chronicle line quoted; R-04.a, b, c2–c7: each re-read); no `status:` edited (A-114). (3) The commit body carries B36.R1's reading, the batch gate's readings, and the record of §5.12.
- WHERE: `engine/season/tests/_realm_goldens.py`; the goldens B36.10 moved; `engine/season/requirements.yaml` (`reading:` records of R-04 only).
- TESTS: none new; the covering suites `tools/tests_for_diff.py --base <batch-start-sha>` names, once.
- FALSIFIER and CONTROL: a pin that moves at seeds 0 to 2 for any reason but `thread_read`'s class (diff the executed-verb tallies against B35's close: only `thread_read`'s formations and what follows from them differ); control: every harness item's EQUAL reading.
- GATE: the BATCH GATE above, read once.
- HASH MOVERS: the re-pin itself.
- DEPENDS ON: B36.01 to B36.17, B36.R1.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`; the close's terminal critique `opus`.
- LANDS IT: B36's producer; `Item: B36.99`, the batch's last `Item:` commit, without `[skip ci]`.

| STOP. Batch B36-wr-story-instruments closes here |
