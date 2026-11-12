# Workplan v12 — part 40: Batch B38-narrative-regimes, first half (the batch block's head; U3 §1 item 38 from `20_NARRATIVE_A` through `31_WR_A`)

## Status: PROPOSED (a body part of workplan v12, drafted under `master/workplan_v12/`; unratified input to `methodology-execute`'s 0.1 stop until Jordan adopts v12, `V12_STRUCTURE_part3.md` §8; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Written against: the working tree of branch `ccr-62958c70-0kjhsw`, read 2026-11-12; author lane A40 of `master/workplan_v12/V12_STRUCTURE_part2.md` §4.2. Every item is written against the tree as B00 to B36 will leave it; where a symbol named here does not exist in today's tree, the item says which batch makes it (DEPENDS ON).

**What this part holds.** The head of the one batch `B38-narrative-regimes` (lane WR) and its items from U3 §1 item 38's first member through `31_WR_A_house_cores_and_the_cast_on_the_opinion_axes`, in U3 §1 item 38's landing order as §1.2 and each member's own `Reconciled:` line correct it: `20_NARRATIVE_A` (with `20_NARRATIVE_F`'s G5 clause, U3 §4.1 row 88) → `20_NARRATIVE_C` → `20_NARRATIVE_B` (carrying `30_WR_D` commit 1) → `28_CORE_scene_access_C` → `20_NARRATIVE_D` commit 1 → `20_NARRATIVE_E` (not edit 1) → `30_WR_B` → `30_WR_G` → `31_WR_A`. The second half of the batch (handles from `B38.51`: `20_NARRATIVE_D`'s later commits, `31_WR_B`, `30_WR_A` with A-103's correction, `30_WR_C`, `23_STORY_A`, `30_WR_D` commit 2, `30_WR_E`, `30_GO_F` with `IS-B3-GO-04`, `IS-B3-FA-03`, `31_WR_C`, `U5d_SE_cohort_heavy_moves_and_caste` with `IS-B3-SE-02`, the `## Readings` block, `B38.99` and the boundary row) is another lane's part; this part cites it by handle only. One batch, one close (RULED 2026-11-06): nothing in this part closes.

**Words.** `unified/U1_GLOSSARY.md`. A person's numbers: attribute, skill, skill score, martial skill, derived score (A-98). Armies: army, unit, army formation, unit formation, no size words (A-99, the MB lexicon). A *lap* is one pass of the season's scene budget; a *round* is one engagement of a fight (A-101): every source here was written before PCR-4 (B04) and says `round` for the season's pass, so the copied text keeps it and each item says `NAMES:`. An *affiliation* is a thing a person may stand for; a *creed* is a faction's declared affiliations (glossary "creed"). A *regime* is a body of persons who stand for the same affiliations (glossary "regime"); `commensurate` names the credit term.

**Paths.** As `V12_STRUCTURE.md` states: a bare path is under `proposals/2026-11-12-subsystem-audit-suite/`; `U3` is `unified/U3_DEPENDENCY_ORDER.md`; `the intake` is `master/eval/V12_INTAKE.md`. A path under `engine/`, `tools/`, `references/`, `registers/`, `tests/` is the repository's. The builder is `engine/season/boot/realm.py::build_realm` after B03c (`CI-07`); sources say `harness/populated.py::build_realm`.

---

## Batch B38-narrative-regimes · lane WR · wave W20 · step S20 · HASH MOVER, one re-pin
INVOCATION: /methodology-execute Batch B38-narrative-regimes
IN-FLIGHT ROW: registers/handoffs/HANDOFF_WR.md, Open table
GATE: Batch B00-ids
GATE: Batch B01-laneA
GATE: Batch B02-tests
GATE: Batch B05-one-roll
GATE: Batch B07-task-draw
GATE: Batch B09-memory
GATE: Batch B10-character
GATE: Batch B11-fi-readers
GATE: Batch B11F1-flow-se
GATE: Batch B11F2-flow-in
GATE: Batch B12c-material-verbs-and-valley
GATE: Batch B21-fa-governance
GATE: Batch B22-mb-armies
GATE: Batch B23-land
GATE: Batch B27-sc-proceedings
GATE: Batch B28-social-verbs
GATE: Batch B32-inst-kit
GATE: Batch B34-go-surface
GATE: Batch B36-wr-story-instruments
REQUIREMENT: re-read R-05 (`riot`, if `U5d_SE_cohort_heavy_moves_and_caste`'s row lands in this batch's second half) → `built out n of n` at 69 (`IS_A_NINE_part2.md` §12.2 row B38); `NULL SCENES` asserted 0 (clause C9, `30_WR_E`; `IS-A-07`'s line); no `status:` edited (A-114). Otherwise none of the nine: the batch serves A-80 to A-91 (eras, regimes, momentum, the pull of one's own, the house cores and the cast on the opinion axes; `IS_A_NINE_part2.md` §12, M5)
BATCH GATE (read once, on the closing tree, `PYTHONHASHSEED=0` on every seeded command, two seasons at most (D-17)):
  `python -m engine.season.harness.register --check` → exit 0 (G13 on the LOOP rows `30_WR_D` commit 2 writes; every hole row this batch adds has a site);
  `python -m engine.season.harness.register --requirements` → nine lines; R-05 re-read; `python tools/m1_acceptance.py --summary` → its verdict line, quoted;
  `python -m pytest engine/season/tests/test_held_by.py engine/season/tests/test_narrative_dues.py engine/season/tests/test_scene_access_waiting.py engine/season/tests/test_custom.py engine/season/tests/test_strife_credit.py engine/season/tests/test_storybar.py engine/season/tests/test_told_by_channel.py -q` → pass (`test_held_by.py`, `test_narrative_dues.py`, `test_scene_access_waiting.py`, `test_custom.py` are this half's new files; U3 §1.3 row B38, §6.1); the second half's new files (`test_sway.py` and those its items name) → pass;
  `python -m engine.season.harness.storybar --base-seed 0 --n 5 --seasons 2 --arms basis_off on --overlaps --executed-only` → G1 to G6 read (no class prints `n/a (no reader)` once this half's readers have landed: G1 at B38.10, G2 at B38.24, G3 and G4 at B38.06, G5 at B38.02), clause 1 (the control) holds under `basis_off` (`20_NARRATIVE_F` gate, six seasons in the source; A-114);
  `python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 2 --arms off off --executed-only` → EQUAL (the WR bar's control, `20_NARRATIVE_A` gate 5);
  `python -m engine.season.harness.strife 2 0 1 2 --strands` → every terminal code reached at the control arms is reached at the batch's live arms (`20_NARRATIVE_A` gate 4; four seasons in the source; A-114); BLIND is reported as BLIND;
  `python -m engine.season.harness.regimes`-reading of `30_WR_B` (`storybar --regimes`, B38.29) → the regime table at seeds 0 to 2, quoted;
  the second half's items' gates, each read at its item and quoted again here once (C9's asserted zero, the census clauses C7 to C13, the `riot` row's `BUILT OUT` line);
  the realm content hash at seeds 0 to 2 after one and two seasons → moved, each value recorded by the re-pin; the control arms (every fixture this batch adds at its control value) reproduce B36's close readings (`reading @<sha>`), read once per arm family at seed 0;
  the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names (engine core, a registry and `rosters.yaml` are touched: the full gates, CLAUDE.md §0.4);
  the glossary rows each item names, read against the code it landed (`STAGES.md`, "The glossary always matches", rule 2): a mismatch fails the close;
  the close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the named conjuncts' readings with their tree, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<sha>`) and after, and the batch's measured wall time; the last `Item:` commit writes the conjuncts' `reading:` records; `status:` is not edited (`IS-A-12`).
RE-PIN: once, at `B38.99` (written by the second half's lane; `V12_STRUCTURE_part4.md` E-1): the realm pins in `engine/season/tests/_realm_goldens.py` (B02's one pin file) and every seeded result this batch's movers move, read against B36's close (`reading @<sha>`). This half's movers: B38.03 (`held_reading` → `stands`), B38.04 (the build seeds `held_by`), B38.05 (`deposit_holder` → `on`), B38.13 (the waiting deposit, if its switch ships `on`: it does not, see the item), B38.22 (`stamp_own_side` stays at control here; no move), B38.24, B38.27, B38.30, B38.33, B38.35 (each said at its item). Encoding movers in this half: none (no item adds, removes or renames a field of a hashed carrier; B38.27 adds roster rows and fixture keys only — `Fixtures` is checked under "HASH MOVERS" at each item).
IDS: ED-WR 0; H 12 (this half's hole-register rows, block slots 1–12, listed at each item's IDS line; the second half adds its own, among them `30_WR_D` commit 2's nine LOOP rows)
DIALS AT CONTROL (this half; the second half adds `sway_gain` and its own):
  `held_reading` = `any`; set by B38.03 (this batch); target: `20_NARRATIVE_A` gate 2.
  `seed_holders` = on (a builder switch, shipped on in B38.04; off is the control): none to set.
  `deposit_holder` = `off`; set `on` by B38.05 (this batch).
  `holder_gain` = 0; set by B98; target: `20_NARRATIVE_C` gate 3 and gate 4 (march regard differs between arms by more than the control's seed spread for at least one verb, two seasons; swept 0 / 0.5 / 1).
  `dues_valence` = 0.0; set by B98; target: `20_NARRATIVE_B` gates 2 to 4 on the planted world (i) at 2 (swept 0 / 2 / 4); world (ii)'s six-season reading is B99's conjunct `argv` (A-114).
  the dials of `28_CORE_scene_access_C` (`waiting_valence` = 0; `petition_intensify` = `off`; `petition_reaches` and `petition_refusal_deposit` as B38.12 to B38.17 state); set by B98; targets: that file's census readings (each item's GATE names it).
  `stamp_own_side` = `False`; set by the second half's `20_NARRATIVE_D` later commits (this batch) (`20_NARRATIVE_D` commit 3).
  `own_side_weight` = 0; set by B98; target: `20_NARRATIVE_D` gate 3.
  `year_reason` = off and the `chronicle_year` reading (B38.25, B38.26): harness only, no setting.
  `custom_pull` = 0 (`30_WR_G` commit 5): set by B98; target: `30_WR_G` gate (the pull felt and resisted, clause C11 of `30_WR_E`); `credit_form` = `commensurate` (the `accord` arm offered, not shipped): set by B98; target: `30_WR_G`'s accord gate.
  (The exact values and owners are copied at each item; H2 collects this list, `V12_STRUCTURE_part3.md` §7.8.)
C(B38-narrative-regimes): [written last, E-11]
SERIAL EDGES: [written last, E-11]
PARALLEL: S20, alone in the whole plan (`V12_STRUCTURE.md` §2.3: B38 is the only batch open at S20).
COST: edits and small builds on person-side readers, the builder, `witness`, `choose.py::_stance_arm`, rosters and fixtures; producer `valoria-author` on `sonnet`, `high`; the judgment nodes are named at their items (`opus` for `30_WR_G` commits 4 and 5, `31_WR_A`'s authored values and `31_WR_B` commit 1; `opus` with a `ners` critic on any `DESIGN-FIRST` item); the close's terminal critique `opus`.
EST: [written last, from the position count, E-15]
UNDECIDED: [written last]

