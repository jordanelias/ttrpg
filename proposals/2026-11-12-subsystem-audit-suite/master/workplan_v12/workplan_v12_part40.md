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

[POSITION TABLE: written last]

### B38.01 — one owner says which affiliations a person holds, at the control reading · `20_NARRATIVE_A` edits 1–4b, 6 (commit 1, `held_reading: any`) · BUILD · HASH EQUAL
- SOURCE: `proposals/20_NARRATIVE_A_stands_for.md` "The resolution, decided", "Exact edits, by owner" 1, 2, 3, 4, 4b, 6, "The gate" 1; its Reconciled line (C3-K2: `16_PESSIMIST_CHAR_A` lands first, B10, with the one signature; this file passes `reading`); rulings A-24, A-82, A-83, A-87, A-89; closes F-NARR-01 (with B38.03).
- ADVANCES: none of the nine; A-82, A-83 (a regime is a body of persons who stand for the same things).
- INSTRUCTION:
  1. `engine/season/queries/person_q.py`, `stands_for` (beside `conviction_stand`). B10.07 wrote it with the `"stands"` arm only (`02_CHAR_scar_is_a_wound`: "this file, landing first, writes `stands_for` with the `"stands"` arm only, and `20_NARRATIVE_A` edit 1 then adds the `any` arm, the `held_readings` roster and the fixture"). This item gives it the source's signature and docstring and adds the `any` arm:
     ```python
     def stands_for(p: Person, reading: str = "stands") -> frozenset:
         """THE AFFILIATIONS `p` HOLDS, for every yes/no question (is he commensurate with another, does
         his own set strain, can this act scar him): `stands` -- those he stands for,
         `conviction_stand(p, a) > 0` (an intensity above the scale's midpoint); `any` -- the CONTROL,
         every key stored above zero, the reading before this function. One owner; `world_q._held`,
         `confliction` and `_held(p.conviction, ...)` ask it. Person-side, no World (AX-2)."""
     ```
     "`reading` is a member of a new closed roster `held_readings: [any, stands]` (`rosters.yaml`, beside `stance_polarities`), refused if unrostered (`require_member`, the `_stance_arm` precedent)." The midpoint "is `(AFFILIATION_FLOOR + AFFILIATION_CEILING) / 2`, read from the leaf (`engine/substrate/descriptors.py`)": `conviction_stand` already reads it; no new number.
  2. `engine/season/data/fixtures.py`: "`held_reading="any"` with a NUMBER-free `[JUSTIFIED: …]` line naming a new `hole_register.yaml` row (its id from B00's block; kind `RULING`, grade `assumption`, the shape of H-275, CR-79's regime-credit row, `U3_CONFLICT_LEDGER.md` T-3): *swept `any` (control, the tree before this item) / `stands` (live)*, `[ASSUMPTION; medium; Jordan to correct; revert: set it back to `any`]`." The row is written in `engine/season/hole_register.yaml` in this commit (block slot 1).
  3. `engine/season/queries/world_q.py::_held`. Old:
     ```python
     def _held(w: World, pid: str) -> set:
         """A person's HELD affiliations: an intensity above 0."""
         return {k for k, v in (w.persons[pid].conviction or {}).items() if v > 0}
     ```
     New:
     ```python
     def _held(w: World, pid: str) -> set:
         """A person's HELD affiliations: `person_q.stands_for`, at `Fixtures held_reading`."""
         return set(stands_for(w.persons[pid], w.fixtures.get("held_reading")))
     ```
     "`commensurate`'s and `incompatible_span`'s bodies do not change. `commensurate`'s docstring line "HELD affiliations (an intensity above 0, `person_q`'s reading)" is replaced by the pointer."
  4. `person_q.confliction` "takes the reading as an argument its one caller passes (`decision/choose.py::deliberation_memo` already holds `fx`): the sum runs over the incompatible pairs both of whose members are in `stands_for(p, reading)`. At `any` it is today's sum exactly." The caller is `deliberation_memo`'s `_DAMP` line (`1.0 / (1.0 + k * confliction(p))`): it passes `fx.get("held_reading")`.
  5. (edit 4b) `person_q.conviction_after_crisis` "takes the same reading. Its one signature is `(p, among=None, band=None, shared=False, reading="any")`, written by `16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told.md` in B10 with `reading` at `"any"` (hash-equal to today's selector); this edit passes `reading="stands"` to that function and flips with `held_reading` (C3-K2). Its Failure arm's candidate set is `stands_for(p, reading)`. Its docstring records the choice this reverses: *"[ASSUMPTION: the draft's "held above threshold" is read as held at all, i.e. above 0.]"* Under `stands`, the affiliation in crisis, the heir of a FOLD and the "something else is held" test of RESTABILISE and DESTROYED each read `stands_for`; under `any` the function is today's." In this commit the call site passes `fx.get("held_reading")` (at `any`: today's); B38.03's flip makes it `stands`.
  6. Not edited (edit 5): the scar writer's affiliation arm already calls `stands_for` (B10.07); this item checks it does and writes no second threshold.
  7. `engine/season/tests/test_strife_credit.py`: "One test added, on `build_realm(0)` with no season run: at `stands`, `{commensurate(w, a, b) for every pair of convinced persons} == {-1, 0, 1}`, and at `any` the same set is asserted to be what it is today (`{-1, 1}`), so the test names the defect it excludes. `test_the_realm_reaches_commensurate…` is kept." Name: `test_commensurate_takes_three_values_only_at_stands` `[ASSUMPTION: test name; the item creates it]`; the `stands` arm is read through `Fixtures.sweep` on the built world, so the shipped value stays `any`.
- WHERE: `engine/season/queries/person_q.py` (`stands_for`, `confliction`, `conviction_after_crisis`); `engine/season/queries/world_q.py` (`_held`, `commensurate`'s docstring); `engine/season/decision/choose.py` (`deliberation_memo`, the `confliction` call); `engine/season/data/fixtures.py` (`held_reading`); `engine/season/rosters.yaml` (`held_readings`); `engine/season/hole_register.yaml` (one row, block slot 1); `engine/season/tests/test_strife_credit.py`; `unified/U1_GLOSSARY.md` (*stands for*).
- TESTS: `test_commensurate_takes_three_values_only_at_stands`, written before step 3 and read red at its `stands` assertion (`_held` reads `v > 0` whatever the fixture); green after step 3. `test_strife_credit.py`'s existing tests stay green.
- FALSIFIER and CONTROL: at `any`, any content hash moves, or `confliction` returns a sum other than today's on the built realm (the control is not today's reading). Control: `build_realm(0).content_hash()` and the one- and two-season pins at seed 0 equal B36's close (`reading @<sha>`) (`20_NARRATIVE_A` gate 1).
- GATE: `python -m pytest engine/season/tests/test_strife_credit.py engine/season/tests/test_scar_stock.py -q` → pass; `python -m engine.season.harness.register --check` → exit 0 (the new row); `python tools/ci_sim_fabrication_check.py` → exit 0 (`held_reading`'s tag); the realm hash at seed 0, one and two seasons → equal to B36's close reading.
- HASH MOVERS: none (`held_reading` ships `any`; `Fixtures` gains a key — `Fixtures` is not a carrier `World.content_hash()` encodes `[ASSUMPTION: the fixture table is outside the hashed World — basis: `20_NARRATIVE_A` gate 1 expects EQUAL with the new fixture shipped; B38.01's gate observes it]`).
- DEPENDS ON: EXISTS-IN-TREE `queries/person_q.py::conviction_stand`, `::confliction`, `queries/world_q.py::_held`, `::commensurate`, `::incompatible_span`, `decision/choose.py::deliberation_memo`, `data/rosters.py::require_member`, `rosters.yaml` `stance_polarities`; V12 B10.07 (`stands_for` with the `"stands"` arm); V12 the B10 item that lands `16_PESSIMIST_CHAR_A`'s composed `conviction_after_crisis` signature (Batch B10-character); V12 Batch B00-ids (the hole-register block).
- GLOSSARY: *stands for*: its owner column becomes a pointer to `person_q.stands_for` (with `held_readings`); the rejected-synonym column kept. "held reading": which test of a stored intensity counts as holding an affiliation, above zero or above the midpoint.
- IDS: H block slot 1.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B38's `valoria-author` producer, `isolation: worktree`; `Item: B38.01`, `[skip ci]`.

### B38.02 — the story bar's G5 class reads across a fault line · `20_NARRATIVE_F` class G5 (U3 §4.1 row 88) · BUILD · HASH EQUAL
- SOURCE: `proposals/20_NARRATIVE_F_story_inventory_and_gate.md` "Exact edits" 1 (the G5 row), 4 (`test_g5_told_claim_across_an_incompatible_pair_reads_minus_one`); its "Lands in batch" line ("its G5 clause (the `stands_for` split) lands in B38 with `20_NARRATIVE_A`"); U3 §4.1 row 88; rulings A-82.
- ADVANCES: none of the nine; the reading `20_NARRATIVE_A` gate 2 needs (it replaces the audit's `narr_probe.py` REGIME line, which is not in the repository).
- INSTRUCTION: in `engine/season/harness/storybar.py::overlaps` (written by B36 with every class; G5 printing `n/a (no reader)` until its reader lands, "detected by import of the reader's symbol, never by a zero"), the G5 row: "G5 across a fault line | an act whose occasion is a told claim, split by `commensurate(hearer, last teller)`: −1, 0, +1 | `20_NARRATIVE_A`". Its reader symbol is `person_q.stands_for` with the `held_readings` roster (B38.01): G5 now counts, per seed and pooled, executed acts (`corpus_run.attempts`) whose occasion is a told claim, keyed by the sign `world_q.commensurate(w, hearer, last_teller)` returns as the snapshot of that season stood (`snaps`, taken in `on_season`), and prints the three counts and the mean confidence of the told claims behind each sign (the audit's REGIME line: told claims held at the end, grouped by `commensurate(hearer, last teller)`, their count and mean confidence). Class G5 between two persons who both hold a conviction is printed apart (clause 1 and 2 read that subset). Once `credit_form: accord` exists (`30_WR_G`, this batch) G5 is also printed by accord band (`20_NARRATIVE_F` Folded (3)); that line is added by the `30_WR_G` item, not here.
- WHERE: `engine/season/harness/storybar.py` (`overlaps`, the G5 row); `engine/season/tests/test_storybar.py`.
- TESTS: `test_g5_told_claim_across_an_incompatible_pair_reads_minus_one` ("A planted told claim across an incompatible pair reads G5(−1) = 1"), written before the edit and read red (G5 prints `n/a` or 0 on the planted log, depending on B36's detection); green after. `test_class_with_no_reader_prints_na` and `test_overlaps_block_moves_no_hash` stay green.
- FALSIFIER and CONTROL: G5 prints `n/a (no reader)` after B38.01 has landed (the detection reads the wrong symbol), or a non-zero G5 on a log with no told claim. Control: the realm content hash at seed 0, one season, equal to B38.01's (harness only).
- GATE: `python -m pytest engine/season/tests/test_storybar.py -q` → pass; `python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 2 --overlaps --executed-only` → G5 prints three counts (any may be 0 at `any`), not `n/a`.
- HASH MOVERS: none (harness only; `20_NARRATIVE_F`: "No hash moves").
- DEPENDS ON: V12 Batch B36-wr-story-instruments (`harness/storybar.py::overlaps`, `--overlaps`, the arms, `test_storybar.py`'s other planted tests); V12 B38.01; EXISTS-IN-TREE `queries/world_q.py::commensurate`, `harness/corpus_run.py::attempts`, `harness/storybar.py::drive` (`on_season`). Serial file: `harness/storybar.py` is edited by one batch at a time (C3-K7); in B38 by this item first.
- GLOSSARY: none (*overlap* is `20_NARRATIVE_F`'s word, its row written in B36).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B38's producer; `Item: B38.02`, `[skip ci]`.

### B38.03 — a person holds what he stands for · `20_NARRATIVE_A` commit 2 (`held_reading: stands`) · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/20_NARRATIVE_A_stands_for.md` "What it changes" 1 to 5, "The gate" 2 to 5, "The falsifier"; "Lands in batch" ("Commit 2 (`stands`) a declared mover"); rulings A-82, A-87, A-89; closes F-NARR-01.
- ADVANCES: none of the nine; A-82 (the regime credit discriminates), the precondition `31_WR_A`'s values need to discriminate (its commit 2 lands after this, B38.33).
- INSTRUCTION: `engine/season/data/fixtures.py`: `held_reading="any"` → `held_reading="stands"`; its `[JUSTIFIED: …]` line and the block-slot-1 hole row read "SHIPPED `stands`; control `any`" (revert: `any`). Nothing else: `commensurate`, `incompatible_span`, `confliction` and `conviction_after_crisis` now read `stands_for(p, "stands")` through the fixture B38.01 routed them by. What then moves ("What it changes" 1–5): `commensurate` reads affiliations stood for, so its three values occur; `loop/witness.py::_credit` raises some told claims, lowers some and leaves most alone; `incompatible_span` discriminates; `confliction` counts a strained pair only where the person stands for both (damped by `confliction_weight` 0, so it moves nothing until that arm is flipped); `conviction_after_crisis` folds a broken affiliation only into an incompatible affiliation the person stands for.
- WHERE: `engine/season/data/fixtures.py` (`held_reading`); `engine/season/hole_register.yaml` (block slot 1's row: shipped value).
- TESTS: none new; `test_commensurate_takes_three_values_only_at_stands` (B38.01) now reads the shipped value.
- FALSIFIER and CONTROL: "Gate 2 with one sign only at `stands`: the realm's tellers and hearers do not cross a fault line, and the fix is in who speaks to whom (FI's `08_FI_02_rumour-that-travels.md`), not here. Gate 2 with three signs and equal means at `regime_gain 0.5`: `_credit` is not reached. Gate 4 failing: the credit term concentrates endings once it discriminates, which is L4 hardening (`strife-00` §6); then `stands` does not ship and `regime_gain` is re-swept under it." Control arm: `regime_gain 0` — "the three means are equal within rounding".
- GATE (`PYTHONHASHSEED=0`):
  1. `python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 2 --overlaps --executed-only` at the shipped fixtures → G5's told claims held at the end, grouped by `commensurate(hearer, last teller)`, "show all three signs with a non-zero count at two seeds or more, and the mean confidence orders `−1 < 0 < +1`"; the same with `regime_gain 0` (a `Fixtures.sweep` arm) → the three means equal within rounding. (Three seasons in the source; A-114. The source warns the count is at risk: "nine and five tellings between cast members in two seasons at seeds 0 and 1 (P-31-7)"; the read reports the counts, `assert checked >= 2` seeds with a told claim; a count too low to show three signs is reported as such, not as a pass, and the falsifier's first line names the owner.)
  2. `incompatible_span` over the run's strands against the same-size random-party control (`harness/strife.py --strands` prints the span column, CR-97, B11F2) → the two differ at some seed of 0 to 2, two seasons (today both read `True` / 0.95).
  3. `python -m engine.season.harness.strife 2 0 1 2 --strands` at `held_reading any` and at `stands` → "every terminal code reached at `any` is reached at `stands`, and no code's share rises by more than the `any` arm's seed spread"; BLIND (fewer than two terminal codes at `any`) is reported BLIND, and its four-season read is B99's conjunct `argv` (A-114; the source: "read it at four seasons (the plan's risk 8)").
  4. `python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 2 --arms off off --executed-only` → EQUAL (the WR story bar's control, gate 5).
  5. The realm hash at seed 0 after one season → moved (declared); `python -m pytest engine/season/tests/test_strife_credit.py -q` → pass.
- HASH MOVERS: "a declared hash mover for every world in which a told claim lands between two persons holding convictions, which is every realm season". Declared; B38's one re-pin at B38.99.
- DEPENDS ON: V12 B38.01, B38.02; V12 Batch B11F2-flow-in (CR-97's strands span column, CR-99's strife guard as a function); V12 Batch B11-fi-readers (`08_FI_02`'s told claims gate 1 counts); EXISTS-IN-TREE `loop/witness.py::_credit`, `harness/strife.py`.
- GLOSSARY: none (B38.01 wrote the row).
- COST and TIER: edit; `sonnet`, `high`; the reading of gate 3 (does the credit term concentrate endings) `opus`.
- LANDS IT: B38's producer; `Item: B38.03`, `[skip ci]`.

