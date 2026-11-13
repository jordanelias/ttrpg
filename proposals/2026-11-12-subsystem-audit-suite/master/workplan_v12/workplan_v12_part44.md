# Workplan v12 — part 44: batches B98-dials and B99-nine-retake

## Status: PROPOSED (the last body part of workplan v12, drafted under `master/workplan_v12/`; unratified input to `methodology-execute`'s 0.1 stop until Jordan adopts v12, `V12_STRUCTURE_part3.md` §8; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Written against: the working tree at `f4eb906` (branch `ccr-62958c70-0kjhsw`, read 2026-11-13, a shallow clone); author lane A44 of `master/workplan_v12/V12_STRUCTURE_part2.md` §4.2 (second pass), one round. Input: `workplan_v12_part2.md` §4, "The settings at control" (105 rows), each row's `DIALS AT CONTROL` line and the item that ships the setting, opened in its part, and the source the item cites. Every item is written against the tree as B00 to B41 will leave it; a symbol that does not exist at `f4eb906` names the batch and item that make it.

**What this part holds.** Two batches of the IN lane, the plan's last two. **`B98-dials`** (W23, S23): one position per setting that an earlier batch shipped at its control value and did not set itself (D-22; `workplan_v12.md` §6), in the order of part 2 §4's table (the order the mechanisms landed), with the few moves the dependencies force (UNDECIDED U2). A TARGETED row is a flip item: the owner's file and symbol, the control value and the new value, the source's reading rule (a sweep run as a probe where the source gives one), the control arm, the revert and a gate read on a command. A BLOCKED row is a short item that flips nothing and records why, who must supply the target and what B99 quotes. An IN-BATCH row is a flip item that runs only if its owner batch's close did not set it. Then `## Readings`, `B98.99` (the one re-pin) and the boundary row. **`B99-nine-retake`** (W24, S24): `IS-A-13`, the one longer re-take of all nine on B98's closing tree, the only item of the plan that may edit a row's `status:`; `B99.99` (an EQUAL close) and the boundary row. Files: this file (the head of B98, its position table, `B98.01` to `B98.22`) → `workplan_v12_part44_cont.md` (`B98.23` to `B98.60`) → `workplan_v12_part44_cont2.md` (`B98.61` to `B98.86`, `## Readings`, `B98.99`, the boundary row, SERIAL EDGES and FILE CENSUS) → `workplan_v12_part44_cont3.md` (B99).

**Paths.** As `V12_STRUCTURE.md` states: a bare path is under `proposals/2026-11-12-subsystem-audit-suite/`; `proposals/<file>` is under that directory's `proposals/`; `IS-A` is `master/instructions/IS_A_NINE.md` and `_part2`; `part 2` is `master/workplan_v12/workplan_v12_part2.md`; `the table` is part 2 §4; "row n" is that table's row n. A path under `engine/`, `modules/`, `tools/`, `references/`, `registers/`, `tests/` is the repository's. An item handle `Bnn.mm` names the item in its own part (the head's §14 maps a handle to its file).

**Words.** `unified/U1_GLOSSARY.md`. A person's numbers are an attribute, a skill and its skill score, a derived score (A-98). Armies: unit, army formation, unit formation, no size word (the MB lexicon). A *lap* is one pass of the season's scene budget; a *round* is one engagement of a fight (A-101). A *setting at control* is a switch, gain or roster shipped at the value that reproduces the previous behaviour (`workplan_v12.md` §13); to *flip* it is to change its shipped value in its owner's file in one commit; a *sweep* is a run of the same reading at each value of a stated set. No word is coined here.

---

## Batch B98-dials · lane IN · wave W23 · step S23 · HASH MOVER, one re-pin
INVOCATION: /methodology-execute Batch B98-dials
IN-FLIGHT ROW: registers/handoffs/HANDOFF_IN.md, Open table
GATE: Batch B00-ids
GATE: Batch B01-laneA
GATE: Batch B02-tests
GATE: Batch B03-hygiene
GATE: Batch B03g-go-early-landings
GATE: Batch B03c-boot
GATE: Batch B16L-mb-words
GATE: Batch B03a-prose
GATE: Batch B13-pc-package
GATE: Batch B16M-mb-engine-words
GATE: Batch B04-capability-home
GATE: Batch B05-one-roll
GATE: Batch B06-keyed-draw
GATE: Batch B07-task-draw
GATE: Batch B08-scene-order
GATE: Batch B09-memory
GATE: Batch B10-character
GATE: Batch BA1-cast-content
GATE: Batch B11-fi-readers
GATE: Batch B11F1-flow-se
GATE: Batch B11F2-flow-in
GATE: Batch B12a-world-motion-and-ground
GATE: Batch B12b-weather-arcs-population
GATE: Batch B12c-material-verbs-and-valley
GATE: Batch B14-pc-outcome
GATE: Batch B15-pc-calibration
GATE: Batch B16-pc-round
GATE: Batch B17-mb-scale
GATE: Batch B18-pc-content
GATE: Batch B19a-mb-contact-instrument
GATE: Batch B19-mb-field-calibration
GATE: Batch B20-mb-orders
GATE: Batch B21-fa-governance
GATE: Batch B21b-fa-war
GATE: Batch B21c-fa-seats
GATE: Batch B21d-fa-arc
GATE: Batch B21s-strife-supply
GATE: Batch B22-mb-armies
GATE: Batch B23-land
GATE: Batch B24-sc-hearing
GATE: Batch B24a-sc-outside-the-room
GATE: Batch B25-fi-questioning
GATE: Batch B26-fi-inquiry
GATE: Batch B27-sc-proceedings
GATE: Batch B28-social-verbs
GATE: Batch B29-pc-custody
GATE: Batch B30-mb-nested
GATE: Batch B31-mb-loadout-economy
GATE: Batch B32-inst-kit
GATE: Batch B33-inst-economy-hands
GATE: Batch B34-go-surface
GATE: Batch B35-wr-thread
GATE: Batch B36-wr-story-instruments
GATE: Batch B37-happenings
GATE: Batch B37p-wr-kin-and-life
GATE: Batch B38-narrative-regimes
GATE: Batch B39-procgen-and-cases
GATE: Batch B40-inst-scenarios
GATE: Batch B41-go-port-gate
HASH READING: `PYTHONHASHSEED=0 python -c "import sys; from engine.season.boot.realm import build_realm; from engine.season.harness.populated import run; s, k = int(sys.argv[1]), int(sys.argv[2]); w = build_realm(s); run(k, s, w=w); print(w.content_hash())" <s> <k>` → the realm content hash at seed `<s>` after `<k>` seasons: `<k>` = 1, one season, unless the gate names two (never more before B99, D-17); `<k>` = 0 reads the build hash; per item `<s>` = 0 (a mover's reading, E-2), at `.99` `<s>` = 0, 1, 2; each value quoted `reading @<sha>`, the tree it was read on (`workplan_v12.md` §3.B, "the hash reading").
REQUIREMENT: none — the settings batch (`V12_STRUCTURE.md` §2.2: "none of its own: the mechanisms shipped dormant begin to run", CLAUDE.md §0.2). No conjunct's `reading:` record is written here and no `status:` is edited: B99 re-takes all nine on this batch's closing tree (D-22: "a reading and a mover in one close would make the re-take's tree the one being re-pinned"). The close quotes `register --requirements` and the `m1_acceptance` verdict line in its commit body only.
BATCH GATE (read once, on the closing tree; `PYTHONHASHSEED=0` on every seeded command; nothing past two seasons, D-17):
  `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`); `python -m engine.season.harness.register --requirements` → nine lines, quoted (no `status:` changed by this batch);
  `python tools/m1_acceptance.py --summary` → its verdict line, quoted;
  `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 2 s` for s = 0, 1, 2 → the `BUILT OUT`, `ENGINES`, `NULL SCENES` and `FOUGHT FIELDS` lines before (`reading @<B40 closing sha>`) and after; **every verb built out at B40's close is still built out** (a flip that leaves a verb not built out is reverted, P8; `IS-A-08`'s rule applied to settings);
  every flip item's own GATE reading, quoted from its commit body (`## Readings` R1 lists them); every BLOCKED position's control value read on the closing tree (R2);
  the realm content hash at seeds 0, 1, 2, one season → the values B98.99 re-pins;
  `python tools/export_sim_params.py --check` → exit 0; `python tools/export_engine_params.py --check` → exit 0; `python tools/ci_golden_modes_check.py` → every digest equal to B40's close unless a flip declares the fight's or the field's goldens moved (B98.39, B98.51, B98.54); `python tools/ci_sim_fabrication_check.py` → exit 0;
  the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names (the batch edits `engine/season/data/fixtures.py` and registries: the full gates, CLAUDE.md §0.4);
  "the close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the named conjuncts' readings with their tree, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<sha>`) and after, and the batch's measured wall time; the last `Item:` commit writes the conjuncts' `reading:` records; `status:` is not edited" (`IS-A-12`), read here as: this batch names no conjunct, so it writes no `reading:` record.
RE-PIN: once, in B98.99's commit: `engine/season/tests/_realm_goldens.py` (B02's one pin file): `SHIPPED` and `CENSUS` at seeds 0 to 2, and `BUILD[0]` if a flip moved the build (row 95, `cohort_convictions`, declares it); the NPC-088 headless hash; the corpus pins and the combat goldens only where a flip moved them; each old → new in the body, read against B40's close (`reading @<sha>`); the commit says "re-pin: B98, behaviour movers B98.<n>, … (the settings flipped); the BLOCKED positions moved nothing".
IDS: ED-IN 0; H 0 (no position writes a ledger or hole-register row: every setting's NUMBER row was written by the batch that shipped it, and a flip edits that row's text in its own commit; a BLOCKED position records its reason in B98.99's commit body and the PR body, D-19). The held blocks stay unused and are named in the expunge: `ED-IN-0399..0400`, `H-846..H-850` (part 2 §9, which supersedes the head's §12 figures `ED-IN-0398..0399`, `H-845..H-849`; UNDECIDED U3). B99's blocks `ED-IN-0401..0402`, `H-851..H-855` are not touched.
DIALS AT CONTROL: none set by a later batch (this batch is the setter). The settings it leaves at control are its BLOCKED positions; each is quoted by B99 on the tree as left (R2).

**Two reads every flip item uses** (defined once here; an item names them):
- **`HASH(s, n; key = v)`**, the realm content hash at seed `s` after `n` seasons with one setting overridden: `PYTHONHASHSEED=0 python -c "from engine.season.boot.realm import build_realm; from engine.season.harness.populated import run; w = build_realm(s); w.fixtures = w.fixtures.sweep('<key>', <v>); run(n, s, w=w); print(w.content_hash())"`. Without `key = v` it is the shipped arm. `[ASSUMPTION: `run` stays at `harness/populated.py::run` after B03c moves `build_realm` to `boot/realm.py` — basis: `V12_STRUCTURE_part2.md` §5.10 moves `build_realm` and `chooser` only; `Fixtures.sweep` (`engine/season/data/fixtures.py`, read at `f4eb906`) returns a swept copy; `run(seasons, seed, cap, w)` takes a built world (read at `f4eb906`); B05's second half reads its control arm the same way, part 9's head]`. A setting that is not a `Fixtures` key (a roster row, a module constant, a column of `references/troops.yaml`, a `build_realm` parameter) or that is read at build (`cohort_convictions`) names its own override in its item (a scoped edit restored in `try/finally`, B21.72's `SUCCESSIONS` precedent).
- **The control arm.** After the flip, `HASH(0, 2; <key> = <control value>)` equals the previous position's recorded after-reading `HASH(0, 2)` (`reading @<sha>`, in that position's commit body; for B98.02, the batch's base reading). A control that moves falsifies the item (P8: revert). "The previous position's after-reading" is the last flip actually committed: a BLOCKED position, a stopped one and a probe that ships nothing record no new reading, and the next flip's control arm reads against the one before them. The base reading is taken once at the batch's open on B40's closing tree, `HASH(0, 1)` and `HASH(0, 2)`; `HASH(0, 1)` must equal B40.99's re-pinned `SHIPPED[(0, 1)]` (the control that the run happened, CLAUDE.md §0.1 pt 3).
- **`FIX(<key>)`**, a setting's shipped value: `python -c "from engine.season.data.fixtures import DEFAULT_FIXTURES as F; print(repr(F.get('<key>')))"`. Every BLOCKED position's GATE is this read (or its named equivalent for a roster row, a column or a constant) on the closing tree, expecting the control value. A BLOCKED position has no commit of its own: B98.99's commit body records each one (the reason, the owner who must supply the target, what B99 quotes), and the PR body lists the content rows for Jordan (D-19).

**Every flip is a behaviour mover; one re-pin only, at B98.99.** Each flip item's `EXPECTED RED UNTIL B98.99` names the tests that read `_realm_goldens.py`'s `SHIPPED` or `CENSUS` (`git grep -ln '_realm_goldens' engine/season/tests` at the item's open; at B02's text: `test_go07_canonical_digest.py::test_go07_control_the_world_did_not_move_only_its_digest`, and the readers in `test_cp_t04_07_surrender.py`, `test_cr81_realm_acquaintances.py`, `test_strife_credit.py`) wherever its flip moves the one-season pin, and the NPC-088 headless pin where it moves; each stays under `[skip ci]`. A flip whose effect cannot show in one season leaves the pins green and says so.

UNDECIDED (each reading taken is the one that changes less, `V12_STRUCTURE_part2.md` §5.1; for the receipt and the 0.1 stop):
  (U1) **Grouping (E-13).** A TARGETED row stays one item (one flip, one commit, one control arm). BLOCKED rows of one owner batch that sit next to each other in the table, ship at control in the same owner file and read the same way are one position, each row still its own numbered record inside it: rows 8 and 9 (B98.08), 17 and 18 (B98.16), 21 and 22 (B98.19), 23 to 26 (B98.20), 37 to 39 (B98.31), 41 and 42 (B98.33), 51 and 52 (B98.42), 68 and 69 (B98.58), 74 to 76 (B98.63), 78 and 79 (B98.65), 81 to 83 (B98.67), 84 to 87 (B98.68). The reason is the handle form: 105 rows and `.99` do not fit two-digit positions (`V12_STRUCTURE_part2.md` §5.3). The other reading (one position per row) needs a three-digit handle the skill's `Bnn.mm` form does not use; it changes more.
  (U2) **Order.** The table's order, except where a target reads another setting: row 95 (`cohort_convictions`) lands before row 94 (`sway_gain`), whose gate reads "with `cohort_convictions` on" (B98.76 lands before B98.75; the handles keep the table's order and the position table lists landing order); row 61 follows row 60 (the table's own note); row 71 (`presumption_gain`, "after B39's prehistory") keeps its place: the prehistory is B39.32's three founders, landed in B39, not row 100's prologue (B98.60). Row 21 (`notice_ob`) stays BLOCKED (its target is "may read row 20's gate 1": a may, not a stated reading).
  (U3) **The ids.** The prompt for this lane names `ED-IN-0398..0399`, `H-845..H-849`; part 2 §9 shifts every IN range by +1 and every H block from B12c on by +1 and says it supersedes the head's §12. Taken: part 2 §9's. This batch writes none either way.
  (U4) **A sweep's chosen point.** Where a source gives a sweep and a reading rule, the item runs the sweep as a probe (seeds named, two seasons at most) and ships the smallest value whose reading satisfies the rule; where several satisfy it and the source names a first value, that value. Where none satisfies it, the item ships nothing, keeps the setting at control and records the reading (the row becomes a READING for B99), never a value outside the swept set.
  (U5) **IN-BATCH rows** (20, 24, 48, 70, 73, 80, 104). Each item opens its owner batch's `.99` commit body (or the owner item's commit) on `main` and runs only if the setting is still at control there; if the owner set it, the item records `set by <handle> @<sha>` and is a POINTER at close (no commit). Part 2 marks row 24's first half set by B21.73; its item is the BLOCKED re-centring only.
  (U6) **Two-season reads of longer sources.** A source reading at three, four, six, eight, fourteen or twenty seasons is read at two with the source's horizon noted (D-17, `workplan_v12.md` P10); where two seasons cannot show the target, the flip is not made and the row's reading is B99's (`workplan_v12.md` §6). Rows so treated: 8, 9, 51, 52 (A-114 in part 2) and 100 (decided here: A-51's prologue is twenty seasons, B98.81), all BLOCKED; and the longer arms of rows 27, 45, 90, 94, quoted at B99 (B99.01 step 6).
  (U7) **Content at its seed.** A flip whose new value is the source's `[ASSUMPTION; Jordan to correct]` (row 6's chance, row 35's spell terms, row 103's rate, row 105's pool, obstacle and patience) ships it marked so and lists it in the PR body for Jordan's correction (D-19); it is not a value chosen here.
  (U8) **One `opus` read per flip** (CLAUDE.md §10): the reading against the source's target is the judgment node; `sonnet` runs the sweep and the commands. A reading the `opus` reader judges not to meet the target reverts the flip (P8), and the row is recorded in R1 as "not flipped: <reading>".
  (U9) **A target with no value.** Part 2 marks a row TARGETED when its source states a reading. Where the source also states no value and no sweep for a numeric setting (rows 29 and 30: the `[CALIBRATE]` pool and obstacle rows "set by the one joint calibration … not here", with no figure; row 32: "a ruling on its coefficient", PB §11, no candidate; row 47: `CARRY_CLOSE_K`, "0 as the control", no candidate; row 66: `leaderless_dispersal`, "swept" with "no figure"; row 102: `covert_kinds.fade`, no `per_season` or `cap`), a flip would need a value this plan would invent: the position is written `BLOCKED (design: no value stated)` with the target recorded for whoever supplies the value, and listed as a correction to part 2. Where the setting's domain is closed and small (a switch, a roster member, a whole number of seasons under the two-season cap, the values a stance read takes in the realm), the item probes every member of it under the source's rule (rows 33, 45, 60, 64, 72). Where a sibling member of the same owner was swept by a stated set, that set is taken (ladder step 4, precedent): the obstacle-term steps of row 56 take `13_SC_calibration` §3 step 3's sweep for `regard_step`, the sibling member of the one obstacle composer (OBS). Where the source's gate reads the target but the setting's value is content (which doctrine's commander rides forward, row 55), the position is `BLOCKED (content)` with the gate read and quoted.
C(B98-dials): this batch's entries; the plan's head parts (`workplan_v12.md` §6; part 2 §4, the table); `engine/season/data/fixtures.py` (`DEFAULT_FIXTURES`, `Fixtures.sweep`); `engine/season/hole_register.yaml` (each flipped setting's NUMBER row, edited in the flip's commit); `engine/season/rosters.yaml`, `references/troops.yaml` and the module constants the items name (`modules/combat/` for rows 32, 47, 61; `modules/mass_battle/` for rows 48, 55, 66); `engine/season/tests/_realm_goldens.py` and its readers; each owner item named in a DEPENDS ON line (read its GATE and its commit body's recorded readings, never re-derived); the closing SHAs of every batch B00 to B41 (the `reading @<sha>` of each owner's last reading); instruments `register`, `aperture`, `decision_spread`, `conviction_spread`, `chronicle`, `storybar`, `corpus_run`, `headless`, `tools/m1_acceptance.py`, `tools/tests_for_diff.py`, `tools/export_sim_params.py`, `tools/export_engine_params.py`, `tools/ci_golden_modes_check.py`, `tools/ci_sim_fabrication_check.py`, `systems/combat/combat_engine_v1/workbench/balance.py`; the permanent surface (CLAUDE.md, `CURRENT.md`, `HANDOFF.md`, `registers/handoffs/HANDOFF_IN.md`, the skill and `methodology-close`). A source proposal is read whole only where an item says so.
PARALLEL: S23, alone in the plan (`V12_STRUCTURE.md` §2.3). No sibling; no merge position.
BACKGROUND RUN: each probe over many fights or seeds (rows 4, 32, 47, 55, 61: 200 to 6,000 fights; rows 30, 96: 200 planted seeds or eight draw seeds) is sized on two small runs at the batch's open, launched in the background (`exec python -u … > log 2>&1`, the skill's "Running a slow instrument"), and read at its item's gate; each item's commit body records the wall time and worker count. No run passes two seasons.
COST: calibration (one value per commit, read against its target); producer `valoria-author` on `sonnet`, `high`; `opus` reads each flip's reading against its source's target before the commit (U8); BLOCKED positions are reading on `sonnet`, `low`.
EST: 39 h [estimate: `workplan_v12.md` §5's formula over 87 positions: 0.4 h × 87 + 2.5 h for the close + 2 h for the probes; the structure's 8 h predates the member list]

The position table, in landing order (the handles follow part 2 §4's rows, UNDECIDED U1; landing order is the table's except B98.76 before B98.75, U2). Every flip also gates on the last committed flip before it (the control arm's chain); that edge is not repeated per row. The SERIAL EDGES and FILE CENSUS lines are at the batch's end, in `workplan_v12_part44_cont2.md` (E-11).

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B98.01 | `confer_fit_weight` stays at 0 | row 1; B04.22; `06_FA_office_capabilities` edit 4 | BLOCKED (design: no target reading) | EQUAL | Batch B04 |
| B98.02 | `stakes_ob` takes its first values, by the source's sweep | row 2; B05.21; `13_SC_tuning_tables` T4; `13_SC_calibration` §3 step 2 | BUILD (flip) | MOVER(behaviour) | Batch B05 |
| B98.03 | `wound_step` stays at its assumed third | row 3; B05.60; ADV Edit D | BLOCKED (design: no target reading) | EQUAL | Batch B05 |
| B98.04 | `body_mark_model` becomes `drawn` | row 4; B14.23; `U5b_PC_residue` §7 | BUILD (flip) | MOVER(behaviour) | Batch B14 |
| B98.05 | a failed search is remembered by the one who searched | row 5; B09.04; `U5a_DICE_owed_edits` §4 | BUILD (flip) | MOVER(behaviour) | Batch B09 |
| B98.06 | a witness may connect what he holds, on the proposed chance | row 6; B09.17; `16_PESSIMIST_GO_a_witness_may_connect_what_he_holds` | BUILD (flip) | MOVER(behaviour) | Batch B09 |
| B98.07 | `stance_scale` stays at the stance bound | row 7; B10.04; `U5a_CHAR_owed_amendments` §2 | BLOCKED (design: no target reading) | EQUAL | Batch B10 |
| B98.08 | the scar's live arms and `scar_weight_shift` stay at control: their target is eight seasons out | rows 8, 9; B10.06, B10.07, B10.08, B10.33; `02_CHAR_scar_is_a_wound` gates (b), (c); `U5a_CHAR_owed_amendments` §8 item 1 | BLOCKED (A-114: target past two seasons) | EQUAL | Batch B10 |
| B98.09 | regard is counted in stance steps | row 10; B10.09; `02_CHAR_scar_cap_and_regard_unit` "Gate" (regard) | BUILD (flip) | MOVER(behaviour) | Batch B10 |
| B98.10 | what is done to a man orders his regard for the doer | row 11; B10.20; `U5a_CHAR_owed_amendments` §4 | BUILD (flip) | MOVER(behaviour) | Batch B10 |
| B98.11 | the stance term is clamped to the stance bound | row 12; B10.10; `02_CHAR_scar_cap_and_regard_unit` "Gate" (clamp) | BUILD (flip) | EQUAL expected | B98.09; Batch B10 |
| B98.12 | the crisis of faith is drawn, at a calibrated obstacle | row 13; B10.13, B10.15, B10.16 (POINTER here); `16_PESSIMIST_CHAR_A` | BUILD (flip) | MOVER(behaviour) | Batch B10 |
| B98.13 | `temper_gain` stays at 0 | row 14; B10.28; `02_CHAR_resolve_and_temper`; `U5a_CHAR_owed_amendments` §1 | BLOCKED (design: no target reading) | EQUAL | Batch B10 |
| B98.14 | the goal leans on its own question | row 15; B10.30; `02_CHAR_goal_lean_on_its_own_question` | BUILD (flip) | MOVER(behaviour) | Batch B10 |
| B98.15 | what an act risks enters the choice | row 16; B10.31; `02_CHAR_what_an_act_risks` gate (d) | BUILD (flip) | MOVER(behaviour) | Batch B10 |
| B98.16 | `rival_gain` stays at 0 and `stance_polarity` stays `declared` | rows 17, 18; B10.63, B10.69; H-180; `17_CENSUS_C1A_02` W4 | BLOCKED (design: no target reading) | EQUAL | Batch B10 |
| B98.17 | `said_choices` stays at 1 | row 19; B11.10; `08_FI_02` edit 7 | BLOCKED (design: no target reading) | EQUAL | Batch B11 |
| B98.18 | `notice_arm` on, if B11 did not turn it on | row 20; B11.66, B11.67; `18_DETERMINISM_notice_is_a_draw` | BUILD (flip, conditional) | MOVER(behaviour) | Batch B11 |
| B98.19 | `notice_ob` stays `routine` and `record_concluders` stays 0 | rows 21, 22; B11.66, B11.75 | BLOCKED (design: no target reading) | EQUAL | Batch B11 |
| B98.20 | four governance steps stay at control | rows 23 to 26; B21.09, B21.12, B21.73, B21.61, B21.69 | BLOCKED (design: no target reading) | EQUAL | Batch B21 |
| B98.21 | the Calamity's weight leaves 0, with the wound planted | row 27; B12a.07, B12a.63 to .65, B12a.71 (HELD there); `09_WR_world_motion` edit 1; `16_PESSIMIST_WR_B` | BUILD (flip) | MOVER(behaviour), and the build hash | Batch B35; Batch B12a |
| B98.22 | `site_yield.harbour.grain` under `ground` stays 40 | row 28; B12a.51 | BLOCKED (design: no target reading) | EQUAL | Batch B12a |
| B98.23 | wear stays a rate: the draw has no pool or obstacle values | row 29; B12a.10; `09_WR_B_draws_not_thresholds` edit 1, gate (2) | BLOCKED (design: no value stated) | EQUAL | Batch B12a |
| B98.24 | endings stay reached by crossing: the draw has no pool or obstacle values | row 30; B12a.12; `09_WR_B_draws_not_thresholds` edit 3, gate (3) | BLOCKED (design: no value stated) | EQUAL | Batch B12a |
| B98.25 | `arrival_report` stays off | row 31; B12a.16; `07_SE_kernel_repairs` D | BLOCKED (design: no target reading) | EQUAL | Batch B12a |
| B98.26 | `APPROACH_SIGMA_K` stays 0: a ruling on the coefficient is owed | row 32; B16.08; PB §7 step 3c, §11 | BLOCKED (design: no value stated) | EQUAL | Batch B16 |
| B98.27 | a journey is priced by its route | row 33; B12b.02, B12b.04; CP-T10-01 | BUILD (flip) | MOVER(behaviour) | Batch B12b |
| B98.28 | the territory yield scale stays empty and the tensions stay unbuilt | row 34; B12b.45, B12b.46; CL-EVENTS (4) | BLOCKED (design: no target reading) | EQUAL | Batch B12b |
| B98.29 | the year's spell is drawn | row 35; B12b.03; `09_WR_B_weather_with_memory_and_the_year` edit 1, gate (4), edit 2 | BUILD (flip) | MOVER(behaviour) | Batch B12b |
| B98.30 | the season's terms stay at 1.0 | row 36; B12b.01; CP-T10-03 | BLOCKED (content: the winter values are Jordan's) | EQUAL | Batch B12b |
| B98.31 | shares, hunger loss and regrowth stay at control | rows 37 to 39; B12b.19, B12b.35, B12b.36, B12b.38 | BLOCKED (design: no target reading) | EQUAL | Batch B12b |
| B98.32 | `management_orders` stays empty | row 40; B34.10; `IS-B3-GO-07` | BLOCKED (content: CL-MGMT's list, held) | EQUAL | Batch B34 |
| B98.33 | hands and spoilage stay at control | rows 41, 42; B12c.02, B12c.03; CP-T08-01, CP-T08-03 | BLOCKED (design: no target reading) | EQUAL | Batch B12c |
| B98.34 | prices stay at par: no computed `offer` | row 43; B12c.16, B12c.17 (HELD); CP-T08-05 | BLOCKED (carrier: no computed producer of `offer`) | EQUAL | Batch B12c |
| B98.35 | `craft` stays withheld | row 44; B12c.25; CP-T08-04 | BLOCKED (design: no target reading) | EQUAL | Batch B12c |
| B98.36 | the upkeep payment gets its question | row 45; B12c.18; CP-T08-08 | BUILD (flip) | MOVER(behaviour) | Batch B12c |
| B98.37 | `effect_rate_gain` stays at 0 | row 46; B12c.26; `07_SE_capability_rate_B` §4 | BLOCKED (design: no target reading) | EQUAL | Batch B12c |
| B98.38 | `CARRY_CLOSE_K` stays 0: no value is stated | row 47; B18.07; `03_PC_loadout_and_carry` Gate 2 | BLOCKED (design: no value stated) | EQUAL | Batch B18 |
| B98.39 | an order is obeyed by a draw, if B19 did not ship it | row 48; B19.68; `27_MB_C` §4; MNV gate 1 | BUILD (flip, conditional) | MOVER(behaviour) | Batch B19 |
| B98.40 | `orders.obey.in_contact` stays 0 | row 49; B19 (27A-2); `27_MB_A` §4 | BLOCKED (design: no target reading) | EQUAL | Batch B19 |
| B98.41 | an elected seat keeps its conferral fallback | row 50; B21c.03; CR-35 (8); H-80 | BLOCKED (design: no computed route; H-80) | EQUAL | Batch B21c |
| B98.42 | the Church Influence bands and the untested triggers stay off: their reading is past two seasons | rows 51, 52; B21d.06 to B21d.09; CR-89, CR-90 | BLOCKED (A-114: target past two seasons) | EQUAL | Batch B21d |
| B98.43 | three kinds of building stay unworn | row 53; B11F1; CR-106 | BLOCKED (design: no target reading) | EQUAL | Batch B11F1 |
| B98.44 | `window_responses` stays empty | row 54; B20 (`IS-MB-03` step 5) | BLOCKED (content: no authored row) | EQUAL | Batch B20 |
| B98.45 | every doctrine's commander stays in reserve; the forward post is read, not shipped | row 55; B20.17; CHO gate 3 | BLOCKED (content: which doctrine rides forward) | EQUAL | Batch B20 |
| B98.46 | four obstacle steps of the word verbs leave 0 | row 56; B25.04, B25.06, B25.13, B25.16; S2B §1, §2, §4; S2C §4; OBS §4 step 6+ | BUILD (flip) | MOVER(behaviour) | Batch B25 |
| B98.47 | a tie weighs the teller, at IN-32's value | row 57; B25.20; S2D edit 4; FI08 §3 | BUILD (flip) | MOVER(behaviour) | Batch B25 |
| B98.48 | a sentence moves the hearers' regard | row 58; B27.04; SC_C "Gate" | BUILD (flip) | MOVER(behaviour) | Batch B27 |
| B98.49 | `docket_crossing_floors` stays empty | row 59; B27; TL §8 row B4.1 | BLOCKED (content: TL B6.n, held) | EQUAL | Batch B27 |
| B98.50 | enmity can move a man to kill: the floor is set inside the realm's band | row 60; B37.13; `22_HAPPENINGS_C` | BUILD (flip) | MOVER(behaviour) | Batch B37 |
| B98.51 | the opener of an unexpected attack has an edge | row 61; B37.15; UPR §6 | BUILD (flip) | MOVER(behaviour) | B98.50; Batch B37 |
| B98.52 | the flow of news within a side stays off: CR-103 is held | row 62; B11F2.09, B11F2.10 (HELD); CR-103 | BLOCKED (CR-103's trigger: Batch B21s-strife-supply and Batch B21b-fa-war closed) | EQUAL | Batch B11F2 |
| B98.53 | an army's recovery after a field stays off | row 63; B22; `IS-MB-B3`; `27_MB_E` §5 | BLOCKED (content: values not established) | EQUAL | Batch B22 |
| B98.54 | a side carries its fatigue into a second field in the same season | row 64; B22; `27_MB_E` §5 row T-17 | BUILD (flip) | MOVER(behaviour) | Batch B22; Batch B31 |
| B98.55 | `standing_ration` stays off | row 65; B22 | BLOCKED (design: no target reading) | EQUAL | Batch B22 |
| B98.56 | a leaderless army does not thin: no rate is stated | row 66; B22.22; `14_VERBS_MILITARY_C` edit 6 | BLOCKED (design: no value stated) | EQUAL | Batch B22 |
| B98.57 | the military verbs' obstacle terms stay absent | row 67; B22.01; `14_VERBS_MILITARY_A`–`_D`, `14_VERBS_PHYSICAL_B` | BLOCKED (design: until B22.01's design names each) | EQUAL | Batch B22 |
| B98.58 | six social obstacle steps stay at 0 | rows 68, 69; B28; S1-B, S1-D | BLOCKED (design: no target reading) | EQUAL | Batch B28 |
| B98.59 | the host's engagement and the precedence draw, if B28 did not switch them on | row 70; B28.29; 28A commit 8 | BUILD (flip, conditional) | MOVER(behaviour) | Batch B28 |
| B98.60 | standing passes down the seat, at a discount | row 71; B32.07; SYN_B gate 2; B39.32 | BUILD (flip) | MOVER(behaviour) | Batch B32, Batch B39 |
| B98.61 | a grievance can occasion a march | row 72; B23.12; `IS-B3-FA-04` | BUILD (flip) | MOVER(behaviour) | B98.09; Batch B23 |
| B98.62 | an unopposed entry onto held land is drawn, if B23 did not switch it on | row 73; B23.05, B23.07; U5d-LAND | BUILD (flip, conditional) | MOVER(behaviour) | Batch B23 |
| B98.63 | three Thread settings stay at control | rows 74 to 76; B35; CP-T07-04, AM-E-07, WR-01 | BLOCKED (design: no target reading) | EQUAL | Batch B35 |
| B98.64 | `legibility_curve` stays empty | row 77; B35; `IS-B3-WR-04` | BLOCKED (content: Jordan's curve) | EQUAL | Batch B35 |
| B98.65 | the thread's seed values and `crossing_step` stay as seeded | rows 78, 79; B35, B35.18; `09_WR_B…` | BLOCKED (design: no target reading) | EQUAL | Batch B35 |
| B98.66 | the Thread ground's amounts and the knot strain: set in B35 or left | row 80; B35.01, B35.02, B35.24, B35.26 | BLOCKED (design: no target reading), unless B35 set them | EQUAL | Batch B35 |
| B98.67 | veterancy, troop upkeep and the drill step stay at control | rows 81 to 83; B31; `04_MB_campaign_party_economy`; `IS-MB-B2` | BLOCKED (design: no target reading; carrier for 82) | EQUAL | Batch B31 |
| B98.68 | four of the money institutions' settings stay at control | rows 84 to 87; B33; VEN_A, VEN_B, PAP | BLOCKED (design: no target reading) | EQUAL | Batch B33 |
| B98.69 | the Church's goal of its liberties stays off | row 88; B33.24; PAP_C | BLOCKED (carrier: a place filter on `deed_doers`) | EQUAL | Batch B33 |
| B98.70 | a seat's believed holder enters the stance term | row 89; B38.06; `20_NARRATIVE_C` gates 3, 4 | BUILD (flip) | MOVER(behaviour) | Batch B38 |
| B98.71 | an unmet due lowers regard for its holder | row 90; B38.07; `20_NARRATIVE_B` gates 2 to 4 | BUILD (flip) | MOVER(behaviour) | Batch B38 |
| B98.72 | a teller's credit reads graded accord | row 91; B38.22; `30_WR_G` commit 4 | BUILD (flip) | MOVER(behaviour) | Batch B38 |
| B98.73 | the pull of one's own custom | row 92; B38.23; `30_WR_G` commit 5 | BUILD (flip) | MOVER(behaviour) | Batch B38 |
| B98.74 | a member who thinks ill of his own side argues its creed | row 93; B38.53; `20_NARRATIVE_D` gate 3 | BUILD (flip) | MOVER(behaviour) | Batch B38 |
| B98.76 | the populace starts at its house's core (lands before B98.75) | row 95; B38.56; `31_WR_B` commit 2; A-91 (3) | BUILD (flip) | MOVER(behaviour), and the build hash | Batch B38 |
| B98.75 | the Revival gathers: the sway draw's dial leaves 0 (lands after B98.76) | row 94; B38.55; `31_WR_B`; A-92 | BUILD (flip) | MOVER(behaviour) | B98.76; Batch B38 |
| B98.77 | a vacant head seat is a mandatory question | row 96; B38.61; `30_WR_A` commit 3; `30_WR_E` C7 | BUILD (flip) | MOVER(behaviour) | Batch B38 |
| B98.78 | the stake sizes stay off: no row is staked | row 97; B38.66; `23_STORY_A` | BLOCKED (carrier: no item declares stake cells on any verb row) | EQUAL | Batch B38 |
| B98.79 | the caste practice factors stay at 1.0 | row 98; B38.85 | BLOCKED (content: Jordan's) | EQUAL | Batch B38 |
| B98.80 | the world is generated from its tables | row 99; B39.01 to B39.03; `PROC_A` PG-1, `PROC_B` PG-2; A-50 | BUILD (flip) | MOVER(behaviour), and the build hash | Batch B39 |
| B98.81 | the prologue stays off: its target is twenty seasons | row 100; B39.10; `PROC_C` PG-4; A-51 | BLOCKED (A-114: target past two seasons) | EQUAL | Batch B39 |
| B98.82 | world cards are drawn, if their pools hold rows | row 101; B39.15; `PROC_D` PG-6 | BUILD (flip, conditional) | MOVER(behaviour) | Batch B39 |
| B98.83 | the trail of a covert deed does not fade: no rate is stated | row 102; B39.17; `PROC_C` PG-5 (d) | BLOCKED (design: no value stated) | EQUAL | Batch B39 |
| B98.84 | a marriage may bear a child | row 103; B39.24, B39.26; `STORY_B` gate 2 | BUILD (flip) | MOVER(behaviour) | Batch B39; Batch B37 |
| B98.85 | the age of majority, if B39 did not set it | row 104; B39.27, B39.28; `STORY_B` gate 4; A-15 | BUILD (flip, conditional) | MOVER(behaviour) | Batch B39 |
| B98.86 | an empty founded place may be abandoned | row 105; B39.30; `STORY_C` gates 2, 3; A-55 | BUILD (flip) | MOVER(behaviour) | Batch B39 |
| B98.99 | re-pin and close readings | `V12_STRUCTURE_part4.md` E-1 | BUILD | MOVER (the re-pin) | B98.01 to B98.86 |

---

### B98.01 — `confer_fit_weight` stays at 0 · row 1; B04.22; `06_FA_office_capabilities` edit 4 · BLOCKED (design: no target reading) · HASH EQUAL
- SOURCE: part 2 §4 row 1; `workplan_v12_part7.md` B04's `DIALS AT CONTROL` line; `proposals/06_FA_office_capabilities.md` edit 4: "the flip to a non-zero value is its own declared mover, made on a reading"; no reading is named.
- SETTING: `engine/season/data/fixtures.py` (`confer_fit_weight`) = `0.0`, shipped by B04.22; read by `decision/choose.py::score_terms` (the `confer` candidate's term).
- INSTRUCTION: none; flip nothing.
- OWNER OF THE TARGET: a design item of the FA lane stating the reading the flip is made on (D-18); until it exists the weight ships at 0 (D-22).
- GATE: `FIX(confer_fit_weight)` → `0.0` on the closing tree (R2).
- B99 QUOTES: the value as left; a conferrer weighs no candidate's believed skill. No conjunct reads it.
- DEPENDS ON: V12 Batch B04, B04.22 (PROPOSED).
- COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.02 — `stakes_ob` takes its first values, by the source's sweep · row 2; B05.21; `13_SC_tuning_tables` T4; `13_SC_calibration` §3 step 2 · BUILD (flip) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 2; `proposals/13_SC_tuning_tables.md` T4 ("first values: `oblige` 0, `detain` 0.5, `ban` 1.0 (obstacle). Read for `determine` (the docketed row's `disposes:`) and `arrest` (`detain`). Sweep 0 / 0.5× / 1× / 2×"); `proposals/13_SC_calibration.md` §3 step 2 ("`stakes_ob` at 0 / 0.5× / 1× / 2×, in a planted hearing per row (a docketed `speak` and its `determine`)") and §4's T4 falsifier ("a `determine` disposing `ban` with the same obstacle as one disposing `oblige`").
- SETTING: `engine/season/data/fixtures.py` (`stakes_ob`, the Tenure-kind entries) = `0` for every kind (B05.21; B05.23 left it, "no edit of T13 ships its first values"). New value: the first values × the multiplier the probe chooses. The `requisition: 0.5` entry (B12c.13) and the `debt` reading (row 87) are not touched.
- INSTRUCTION:
  1. Probe (no commit): in `engine/season/tests/test_sc_tuning_tables.py` (B05.23's file), NEW `test_stakes_sweep_in_a_planted_hearing` `[ASSUMPTION: test name; the item creates it, E-3]`: for each docketed arrangement row, a planted hearing (a docketed `speak` and its `determine`), at multipliers {0, 0.5, 1, 2} on (`oblige` 0, `detain` 0.5, `ban` 1.0), pools 2 to 4; print per cell the composed obstacle and the band shares.
  2. Rule (U4): ship the smallest multiplier at which (a) a `determine` disposing `ban` composes a larger obstacle than one disposing `oblige`, with `detain` between (the T4 falsifier reads false); (b) the step from 0 changes a band at pools 2 to 4 in at least one row (CAL §3's test for a value that is not decoration); (c) `test_sc_calibration_targets.py` stays green on C1 to C8. If 1× and a smaller value both pass, 1× (the source's first values). If none passes, ship nothing (U4).
  3. Edit `stakes_ob`'s Tenure-kind entries to the chosen values; its NUMBER row's text records the value and "T4 falsifier; C2–C4" (CAL edit 2).
- FALSIFIER and CONTROL: T4's falsifier at the chosen arm. Control arm: `HASH(0, 2; stakes_ob = the control table)` equals the batch's base reading.
- GATE: `python -m pytest engine/season/tests/test_sc_tuning_tables.py engine/season/tests/test_sc_calibration_targets.py engine/season/tests/test_obstacle_form.py -q` → pass; the probe's table quoted; `HASH(0, 2)` → moved, recorded.
- HASH MOVERS: every world with a docketed `determine` or an `arrest`. EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers if `HASH(0, 1)` moved.
- REVERT: `stakes_ob`'s Tenure-kind entries back to 0 (one edit).
- DEPENDS ON: V12 Batch B05, B05.21, B05.22, B05.23 (PROPOSED); B12c.13 (`requisition` entry).
- STOPS IF: `stakes_ob` is not a table keyed by Tenure kind on the base (`FIX(stakes_ob)` prints otherwise): stop and report.
- COST and TIER: calibration; `sonnet`, high; `opus` reads the probe table against T4 and C1–C8.
- LANDS IT: B98's producer; `Item: B98.02`, `[skip ci]`.

### B98.03 — `wound_step` stays at its assumed third · row 3; B05.60; ADV Edit D · BLOCKED (design: no target reading) · HASH EQUAL
- SOURCE: part 2 §4 row 3 (decided there, C-06); `workplan_v12_part9.md` B05's second-half `DIALS AT CONTROL` line ("set by B15 … target: B15's calibration of the in-fight wound σ"); no B15 item sets it, and "a calibration of the in-fight wound σ" names no reading.
- SETTING: `engine/season/data/fixtures.py` (`wound_step`) = a third of `condition_scale` `[ASSUMPTION, ADV Edit D]`, shipped by B05.60; read by `seam/wrappers/sigma.py::_wound_levels`.
- INSTRUCTION: none; flip nothing.
- OWNER OF THE TARGET: the PC lane (U1 §4 R-27: the in-fight σ and `wound_step` "sized in PC's one calibration batch"): a reading for the season-scale wound level, which B15 did not state.
- GATE: `FIX(wound_step)` → the B05.60 value on the closing tree (R2).
- B99 QUOTES: the value as left, with its `[ASSUMPTION]` tag. No conjunct reads it alone; R-09.c's degrees include wounded rolls.
- DEPENDS ON: V12 Batch B05, B05.60; Batch B15 (PROPOSED).
- COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.04 — `body_mark_model` becomes `drawn` · row 4; B14.23; `U5b_PC_residue` §7 · BUILD (flip) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 4 (C-06: B14 named B15, no B15 item flips it); `proposals/U5b_PC_residue.md` §7, "Gate": "200 seeded fights that leave a survivor at his limit: the three outcomes each occur; control (`deepest_gate`) reproduces the pre-change hash"; "Falsifier. Under `drawn`, a mark on every such survivor"; "the flip is read with the calibration batch, after A3 (B15)".
- SETTING: `engine/season/data/fixtures.py` (`body_mark_model`) = `deepest_gate` (shipped; the swept set `none` / `deepest_gate` / `drawn`, B14.23). New value: `drawn`. `mark_ob` keeps its `[ASSUMPTION]` seed (B14.23), read only under `drawn`; the PR body lists it for Jordan (D-19).
- INSTRUCTION: `body_mark_model` `deepest_gate` → `drawn`, one line; its NUMBER row's text names the shipped value and the gate.
- TESTS: `engine/season/tests/test_combat_module.py::test_drawn_marks_yield_all_three_outcomes_over_200_seeds` (`assert checked >= 200`) and `::test_deepest_gate_reproduces_the_pre_change_hash` (B14.23's), read green before the edit at `drawn` passed explicitly.
- FALSIFIER and CONTROL: under `drawn`, a mark on every such survivor (one outcome in 200). Control arm: `HASH(0, 2; body_mark_model = deepest_gate)` equals B98.03's after-reading (B98.02's, B98.03 moved nothing).
- GATE: the two tests → pass; the 200-fight reading quoted (Failure, Partial, Success-or-better shares, each above 0); `HASH(0, 2)` → recorded (moved only if a survivor at his limit occurs in two seasons at seed 0; said either way).
- HASH MOVERS: "At the flip: every fight with a survivor at his limit" (the source). EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers and the combat goldens only if moved.
- REVERT: `body_mark_model` → `deepest_gate`.
- DEPENDS ON: V12 Batch B14, B14.23; Batch B15 (A3, the mortal-wound draw, "after A3"); Batch B06 (`draw_factory`).
- STOPS IF: `_marks` has no `drawn` branch on the base (B14.23 not landed as written).
- COST and TIER: calibration; `sonnet`, high; `opus` reads the three shares.
- LANDS IT: B98's producer; `Item: B98.04`, `[skip ci]`.

### B98.05 — a failed search is remembered by the one who searched · row 5; B09.04; `U5a_DICE_owed_edits` §4 · BUILD (flip) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 5; `proposals/U5a_DICE_owed_edits.md` §4, "Gate": "Seeds 0–2, two seasons, both arms: failed inquiry aims tried again fall at the `actor` arm with `refusal_memory` above 0, and do not fall at `refusal_memory` 0 (the pessimist's control, reproduced); deposits to non-actors equal across arms." "Falsifier. The retry share is unchanged with both edits in." "Hash movers. The `actor` arm."
- SETTING: `engine/season/data/fixtures.py` (`finding_none_deposit`) = `none` (B09.04). New value: `actor`.
- INSTRUCTION: read the gate's three arms (`none`, `actor` at the shipped `refusal_memory` 0.5 from B09.05, `actor` at `refusal_memory` 0), seeds 0 to 2, two seasons, with the instrument and override B09.05's commit body names for this arm reading (`reading @<B09 close sha>` is the `none` arm's before-reading); if the reading holds, `finding_none_deposit` `none` → `actor`, one line, and its `[JUSTIFIED: …]` line names H-111.
- FALSIFIER and CONTROL: the retry share unchanged between the arms. Control arm: `HASH(0, 2; finding_none_deposit = none)` equals B98.04's after-reading.
- GATE: `python -m pytest engine/season/tests/test_refusal_memory.py -q` → pass; the three arms' readings quoted per seed (failed inquiry aims tried again; deposits from `finding.none` Events into ledgers other than the doer's, equal across `none` and `actor`); `HASH(0, 2)` recorded.
- HASH MOVERS: "the `actor` arm" (the source). EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers if moved at one season.
- REVERT: `finding_none_deposit` → `none`.
- DEPENDS ON: V12 Batch B09, B09.04, B09.05 (`refusal_memory` 0.5), B09.03 (`admission_weight`).
- STOPS IF: `refusal_memory` is not above 0 on the base (B09.05 reverted): the arm cannot read, stop.
- COST and TIER: calibration; `sonnet`, high; `opus` reads the arms.
- LANDS IT: B98's producer; `Item: B98.05`, `[skip ci]`.

### B98.06 — a witness may connect what he holds, on the proposed chance · row 6; B09.17; `16_PESSIMIST_GO_a_witness_may_connect_what_he_holds` · BUILD (flip) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 6; `proposals/16_PESSIMIST_GO_a_witness_may_connect_what_he_holds.md` §2 (`connection_chance = 0.0  # CONTROL … proposed on-value 0.6, + 0.2 where his claim on the antecedent carries a who`), "The gate" 2 to 5, "The falsifier".
- SETTING: `engine/season/data/fixtures.py` (`connection_chance`) = `0.0` (B09.17). New value: `0.6` `[ASSUMPTION; medium; Jordan to correct; revert: 0.0]` (the source's own mark, kept; UNDECIDED U7). The "+ 0.2 where his claim … carries a `who`" has no carrier in B09.17's edit (one chance, one draw) and is not built here: listed for Jordan.
- INSTRUCTION: `connection_chance` `0.0` → `0.6`, one line; the NUMBER row's text names the value and the gates read.
- FALSIFIER and CONTROL: the source's: "A `why` naming a claim the holder does not hold. A `why` on a document-channel deposit. An on-arm run in which every eligible witness connects (the draw is decoration) or none does." Control arm: `HASH(0, 2; connection_chance = 0.0)` equals B98.05's after-reading (gate 1).
- GATE: `python -m pytest engine/season/tests/test_seen_why.py -q` → pass (gate 2, `checked >= 100`; gate 3, the binomial 99 % band; gate 5); gate 4: `PYTHONHASHSEED=0 python -m engine.season.harness.chronicle --seed s --seasons 2 --chains --min-depth 2`, s = 0 to 2 → the count of chains whose later link is held by a bystander with a `why` naming his claim on the earlier link: above 0 and below the "held whole by a bystander" count, per seed, quoted.
- HASH MOVERS: "a declared mover when the chance is raised" (B09.17). EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers if moved.
- REVERT: `connection_chance` → `0.0`.
- DEPENDS ON: V12 Batch B09, B09.17, B09.16 (`scene_of`).
- STOPS IF: `test_seen_why.py`'s on-arm tests take the chance from a constant, not the fixture (they could not see the flip).
- COST and TIER: calibration; `sonnet`, high; `opus` reads gates 3 and 4.
- LANDS IT: B98's producer; `Item: B98.06`, `[skip ci]`.

### B98.07 — `stance_scale` stays at the stance bound · row 7; B10.04; `U5a_CHAR_owed_amendments` §2 · BLOCKED (design: no target reading) · HASH EQUAL
- SOURCE: part 2 §4 row 7; `workplan_v12_part12.md` B10's `DIALS AT CONTROL` line; `proposals/U5a_CHAR_owed_amendments.md` §2: "The live value is flipped only after a reading; none is proposed here."
- SETTING: `engine/season/data/fixtures.py` (`stance_scale`) = `STANCE_MAX` (25), shipped by B10.04; read by `decision/choose.py::stance_term`.
- INSTRUCTION: none; flip nothing. OWNER OF THE TARGET: the CHAR design (IN lane): a reading for the scale of the stance term against the pursuit term.
- GATE: `FIX(stance_scale)` → 25 (R2). B99 QUOTES: the value as left; R-07.b and R-07.d read regard at this scale.
- DEPENDS ON: V12 Batch B10, B10.04. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.08 — the scar's live arms and `scar_weight_shift` stay at control: their target is eight seasons out · rows 8, 9; B10.06, B10.07, B10.08, B10.33; `02_CHAR_scar_is_a_wound` gates (b), (c); `U5a_CHAR_owed_amendments` §8 item 1 · BLOCKED (A-114: target past two seasons) · HASH EQUAL
- SOURCE: part 2 §4 rows 8, 9 (HD-26); `workplan_v12_part12.md` B10's `DIALS AT CONTROL` lines and UNDECIDED 2; `workplan_v12.md` §6 ("written in B98 as `BLOCKED (target reading beyond two seasons; A-114)`, and B99 quotes its reading on the tree as left").
- SETTINGS: (row 8) `engine/season/data/fixtures.py` (`scar_season_cap` = `None`, `scar_hold` = `any`, `scar_lean_floor` = `0.0`, `scar_vindication` = `off`; `scar_primary_mass` 0.6), shipped by B10.06, B10.07; (row 9) `scar_weight_shift` = 0, shipped by B10.08, armed by no item (B10.33 is a POINTER here).
- TARGETS, copied: row 8, `02_CHAR_scar_is_a_wound` gate (b), "at the four live arms together, the share of cast persons with some element at 3 or more after eight seasons lies strictly between 0 and 1 at every seed", and (c) "at least one count falls by vindication"; 0 by construction at two seasons (HD-26). Row 9, §8 item 1, "the realm's per-person conduct … moves for persons at threshold 2 and not for persons below it, seeds 0–2", licensed only "after `02_CHAR_scar_is_a_wound.md`'s gate (b) reads a share strictly between 0 and 1".
- INSTRUCTION: none; flip nothing (B98 is capped at two seasons, B99 is hash-EQUAL; `workplan_v12.md` §6).
- GATE: `FIX(<key>)` for each of the five keys → the control values above (R2).
- B99 QUOTES: gate (b) and (c) at eight seasons, seeds 0 to 2, read in-process at the four live arms together (a sweep on B98's closing tree, nothing shipped; `test_scar_stock.py::test_at_the_live_arms_the_share_at_three_lies_strictly_between_0_and_1` is the source's named test), and, only if (b) holds, §8 item 1's reading at `scar_weight_shift` 1 (B99.01 step 6). Whether to flip on that reading is Jordan's (P10: "unless Jordan calls for it").
- DEPENDS ON: V12 Batch B10, B10.06, B10.07, B10.08. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.09 — regard is counted in stance steps · row 10; B10.09; `02_CHAR_scar_cap_and_regard_unit` "Gate" (regard) · BUILD (flip) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 10; `proposals/02_CHAR_scar_cap_and_regard_unit.md` "Gate", Regard: "Reading rule, stated before the run: at arm `stance`, after two seasons, the median computed half among pairs that hold one is at least 0.5 (half a valence step) and no pair's exceeds `STANCE_MAX`"; B10.09's HASH MOVERS ("its live flip is a declared mover read against the control at seeds 0–2").
- SETTING: `engine/season/data/fixtures.py` (`regard_unit`) = `raw` (B10.09; roster `rosters.yaml: regard_units: [raw, stance]`). New value: `stance`.
- INSTRUCTION: read the rule in-process at `regard_unit = stance`, seeds 0 to 2, two seasons (`w = build_realm(s)`, sweep, `run(2, s, w=w)`; over every ordered pair holding a judged or told half, `person_q.regard`'s computed half, its median and its maximum, printed per seed); if it holds at every seed, `regard_unit` `raw` → `stance`, one line, its NUMBER row's text naming the reading.
- FALSIFIER and CONTROL: the source's: "Two holders with opposite pursuits who each saw one deed hold regards of opposite sign, of size at most `judged_gain` … at arm `stance` and of the raw size at `raw`" (`test_regard_unit.py`). Control arm: `HASH(0, 2; regard_unit = raw)` equals B98.06's after-reading.
- GATE: `python -m pytest engine/season/tests/test_regard_unit.py engine/season/tests/test_told_by_channel.py -q` → pass (`test_r07_realm_regard_differs_between_hearers_by_claim_not_stance_alone` green: R-07.b's test); the median and maximum per seed quoted (median ≥ 0.5; maximum ≤ `STANCE_MAX`); `HASH(0, 2)` recorded.
- HASH MOVERS: every world in which a judged or told deed enters regard. EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers.
- REVERT: `regard_unit` → `raw`.
- DEPENDS ON: V12 Batch B10, B10.09, B10.10 (the clamp the rule's bound reads), B10.04.
- STOPS IF: `person_q.regard` exposes no computed half to read per pair at the base: the producer records how the half is read before the run.
- COST and TIER: calibration; `sonnet`, high; `opus` reads the median per seed.
- LANDS IT: B98's producer; `Item: B98.09`, `[skip ci]`.

### B98.10 — what is done to a man orders his regard for the doer · row 11; B10.20; `U5a_CHAR_owed_amendments` §4 · BUILD (flip) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 11; `proposals/U5a_CHAR_owed_amendments.md` §4, "Gate": "Control: hash EQUAL. Live, seed 0, two seasons (… restated as `engine/season/tests/test_relations.py::test_what_is_done_to_a_man_orders_his_regard`): the mean change in a counterparty's regard for the actor is higher for `give` and `tend` than for `sabotage` and `lie`." "Falsifier. The order is unchanged at the live arm." "Hash movers. The flip."
- SETTING: `engine/season/data/fixtures.py` (`deed_counterparty`) = `paired_only` (B10.20; roster `deed_counterparties`). New value: `person_subject`.
- INSTRUCTION: run `test_relations.py::test_what_is_done_to_a_man_orders_his_regard` at `person_subject` (seed 0, two seasons); if the order holds, `deed_counterparty` → `person_subject`, one line.
- FALSIFIER and CONTROL: the order unchanged at the live arm. Control arm: `HASH(0, 2; deed_counterparty = paired_only)` equals B98.09's after-reading.
- GATE: `python -m pytest engine/season/tests/test_relations.py -q` → pass; the four kinds' mean regard changes at seed 0 quoted; `HASH(0, 2)` recorded.
- HASH MOVERS: "The flip" (every deed of a kind whose row names a person subject). EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers.
- REVERT: `deed_counterparty` → `paired_only`.
- DEPENDS ON: V12 Batch B10, B10.20, B10.62.
- STOPS IF: B10.20 landed the fixture at control only (its STOPS IF found no field naming an unpaired deed's counterparty, and the live half is `BLOCKED (v12: a carrier is owed)`): this position is then BLOCKED (carrier) and flips nothing.
- COST and TIER: calibration; `sonnet`, high; `opus` reads the order.
- LANDS IT: B98's producer; `Item: B98.10`, `[skip ci]`.

### B98.11 — the stance term is clamped to the stance bound · row 12; B10.10; `02_CHAR_scar_cap_and_regard_unit` "Gate" (clamp) · BUILD (flip) · HASH EQUAL expected
- SOURCE: part 2 §4 row 12; `proposals/02_CHAR_scar_cap_and_regard_unit.md` "Gate", Clamp: "`build_realm(0)`'s one-season hash is EQUAL with the clamp on, because no shipped row stacks past 25 (if it moves, a shipped row stacks, and that is a finding)"; B10.10's GATE read both arms at B10's close.
- SETTING: `engine/season/data/fixtures.py` (`stance_clamp`) = `False` (B10.10). New value: `True`.
- INSTRUCTION: `stance_clamp` `False` → `True`, one line. Read `HASH(0, 1)` and `HASH(0, 2)` before and after.
- FALSIFIER and CONTROL: `test_regard_unit.py::test_stance_term_is_clamped` (H-339's twenty grudges read no lower than −50). Control arm: `HASH(0, 2; stance_clamp = False)` equals B98.10's after-reading.
- GATE: `python -m pytest engine/season/tests/test_regard_unit.py -q` → pass; `HASH(0, 1)` and `HASH(0, 2)` → equal to the control arm's (the target). A moved hash is the finding the source names: it is quoted with the person and row that stacks past 25, the flip stays (the clamp is the type's bound, "a type error, not a tuning"), and the item is re-tagged MOVER(behaviour) in its commit.
- HASH MOVERS: none expected. EXPECTED RED UNTIL B98.99: none unless the finding above.
- REVERT: `stance_clamp` → `False`.
- DEPENDS ON: V12 Batch B10, B10.10; B98.09 (the regard unit the clamp bounds).
- COST and TIER: edit; `sonnet`, high.
- LANDS IT: B98's producer; `Item: B98.11`, `[skip ci]`.

### B98.12 — the crisis of faith is drawn, at a calibrated obstacle · row 13; B10.13, B10.15, B10.16 (POINTER here); `16_PESSIMIST_CHAR_A` · BUILD (flip) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 13; `proposals/16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told.md` "Gate" 2 ("`on`: the set of persons whose conviction moved differs between at least two seeds, and at least one person in crisis at some seed holds (band Success or better)") and 3 ("Of the persons whose highest-intensity creed changes, the count whose new top creed is one they held at less than half their old top's intensity is 0 without a Failure band on the roll"), its order of edits ("`crisis_arm: drawn` in its own commit"); A-24 (the shipped arm is `drawn`); B10's UNDECIDED 3 (the obstacle set here, the arm flipped with it, one commit); the source's horizon is three seasons, read at two (A-114).
- SETTINGS: `engine/season/data/fixtures.py` (`crisis_arm` = `rule`; `crisis_obstacle` = `None`), B10.13. New values: `crisis_arm` = `drawn`; `crisis_obstacle` = the level the probe chooses from the swept set B10.13's hole row names ("the difficulty levels of B05's obstacle ladder").
- INSTRUCTION:
  1. Probe (no commit): at `crisis_arm = drawn` and each level of the ladder (`plain`, `routine`, `demanding`, `hard`), seeds 0 to 3, two seasons, in-process: the persons with a `conviction.moved` Event per seed, the band of each crisis roll, and gate 3's count; print a table per level.
  2. Rule (U4): ship the lowest level at which gate 2 and gate 3 both hold `[ASSUMPTION: "lowest" — basis: the source states no level and no preference; the lowest passing level changes least from the rule arm's certainty of breaking]`. None passing: ship nothing (U4); the row becomes a READING for B99.
  3. One commit: `crisis_obstacle` → the level, `crisis_arm` → `drawn`; both hole rows' texts name the reading.
- FALSIFIER and CONTROL: gate 3 above; `test_crisis_draw.py::test_off_reproduces_conviction_after_crisis` (gate 1). Control arm: `HASH(0, 2; crisis_arm = rule)` equals B98.11's after-reading.
- GATE: `python -m pytest engine/season/tests/test_crisis_draw.py -q` → six pass (`test_two_seeds_move_different_persons`, gate 2; `test_lowest_intensity_creed_is_the_one_in_crisis_for_shared_column`, gate 3; gate 4's receipt test); the probe table and the chosen level quoted; `HASH(0, 2)` recorded.
- HASH MOVERS: "every run in which a crisis fires re-records" (the source). EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers and the NPC-088 headless pin if a crisis fires in its run.
- REVERT: `crisis_arm` → `rule`, `crisis_obstacle` → `None` (one commit).
- DEPENDS ON: V12 Batch B10, B10.13, B10.14, B10.15; Batch B05 (the obstacle ladder).
- STOPS IF: the emitter at `drawn` raises with `crisis_obstacle` set (B10.15's guard not keyed on `None`).
- COST and TIER: calibration; `sonnet`, high; `opus` reads gate 2 and 3 per level.
- LANDS IT: B98's producer; `Item: B98.12`, `[skip ci]`.

### B98.13 — `temper_gain` stays at 0 · row 14; B10.28; `02_CHAR_resolve_and_temper`; `U5a_CHAR_owed_amendments` §1 · BLOCKED (design: no target reading) · HASH EQUAL
- SOURCE: part 2 §4 row 14; B10's `DIALS AT CONTROL` line: "none stated beyond the direction readings … (`U5a_CHAR_owed_amendments` §1: 'No threshold is invented: each line is a direction against a control') … unless CR-93's design (B10.51) states one".
- SETTING: `engine/season/data/fixtures.py` (`temper_gain`) = 0 (B10.28); read by `decision/choose.py::temper`.
- INSTRUCTION: open B10.51's merged design file; record whether it states a target reading for `temper_gain`. Flip nothing.
- OWNER OF THE TARGET: CR-93's design (B10.51; IN lane).
- STOPS IF: the design states a target reading: the position stops and is reported at the batch's 0.1 stop (the flip is then written from that text, which this plan did not copy).
- GATE: `FIX(temper_gain)` → 0 (R2). B99 QUOTES: the value as left; R-08.c's magnitude is read at it.
- DEPENDS ON: V12 Batch B10, B10.28, B10.51. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.14 — the goal leans on its own question · row 15; B10.30; `02_CHAR_goal_lean_on_its_own_question` · BUILD (flip) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 15; `proposals/02_CHAR_goal_lean_on_its_own_question.md` "Gate": "`aim_gain` 1, `decision_spread --season`, seeds 0–2: … Reading rule, stated before the run: the share of persons with one score-top verb across a `need` question and a `claim_landed` question on the same referent falls below the 36-of-46 read above"; "`aperture 2 0`: no verb's `executed` count falls to 0 that was above 0 at the control". Sweep (B10.30's hole row): `[0, 0.5, 1, 2]`.
- SETTING: `engine/season/data/fixtures.py` (`aim_gain`) = 0 (B10.30). New value: the probe's choice from `{0.5, 1, 2}`.
- INSTRUCTION:
  1. Probe: at each gain, seeds 0 to 2, `harness/decision_spread.py::play_season(w, 1)` on `build_realm(s)` with the gain swept in-process (the source's "`decision_spread --season`", one season); the share of persons with one score-top verb across the two questions, printed with the gain-0 control's share on the same base (the source's 36 of 46 was read on an older tree and is quoted beside it, not used as the bar) `[ASSUMPTION: the share is read from `play_season`'s result; the producer names the key in the commit body]`.
  2. Rule (U4): the source reads its target at 1: ship 1 if the share falls below the control's at every seed and the `aperture` arm holds; else the smallest of 0.5, 2 that passes; none: ship nothing.
  3. `aim_gain` → the value; its hole row's text names the reading.
- FALSIFIER and CONTROL: `test_goal_lean.py`'s hand-built pair (the source's falsifier). Control arm: `HASH(0, 2; aim_gain = 0)` equals B98.12's after-reading.
- GATE: `python -m pytest engine/season/tests/test_goal_lean.py engine/season/tests/test_in62_decision_spread.py -q` → pass; the probe's shares quoted; `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 2 0` on the item's base and after the edit → no verb whose `executed` was above 0 reads 0; `HASH(0, 2)` recorded.
- HASH MOVERS: "declared when the gain flips" (B10.30). EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers.
- REVERT: `aim_gain` → 0.
- DEPENDS ON: V12 Batch B10, B10.30. COST and TIER: calibration; `sonnet`, high; `opus` reads the shares. LANDS IT: B98's producer; `Item: B98.14`, `[skip ci]`.

### B98.15 — what an act risks enters the choice · row 16; B10.31; `02_CHAR_what_an_act_risks` gate (d) · BUILD (flip) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 16; `proposals/02_CHAR_what_an_act_risks.md` "The gate" (d): "Seeds 0 to 2, after the offer proposal lands: attempts at exposed acts by persons below the top body band fall against the gain-0 control"; "(d) is a realm reading (`decision_spread`), quoted in the flip's commit"; the falsifier ("At a non-zero gain the rank of any candidate whose row contests no bodily prize changes … or, in (d), wounded persons attempt exposed acts as often as before at three seeds"). Sweep (B10.31): `risk_gain` 0, 0.5, 1.0.
- SETTINGS: `engine/season/data/fixtures.py` (`risk_gain` = 0.0; `nerve_gain` = 0.0; `risk_unknown_chance` 0.5), B10.31. New value: `risk_gain` from `{0.5, 1.0}`. `nerve_gain` stays 0.0: it reads only through a `choice_exposure` uses row and "no row ships" (B10.31 step 5), so a flip would move nothing; it is recorded in R2 as left at control for want of the row (content: the uses row, BA1's or Jordan's).
- INSTRUCTION: probe at each `risk_gain`, seeds 0 to 2, two seasons, in-process (`play_season(w, 2)`): attempts at exposed acts (rows contesting a prize in `rosters.yaml: bodily_prizes`) by persons below the top body band, against gain 0. Rule (U4): the smallest gain at which the count falls at every seed and `test_an_uncontested_candidate_is_unchanged_at_any_gain` holds; none: ship nothing. `risk_gain` → the value.
- FALSIFIER and CONTROL: the source's falsifier above. Control arm: `HASH(0, 2; risk_gain = 0.0)` equals B98.14's after-reading.
- GATE: `python -m pytest engine/season/tests/test_risk_term.py engine/season/tests/test_goal_lean.py -q` → pass; the counts per seed and gain quoted; `HASH(0, 2)` recorded.
- HASH MOVERS: "declared when the gain flips" (B10.31): every deliberation offering an exposed act. EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers.
- REVERT: `risk_gain` → 0.0.
- DEPENDS ON: V12 Batch B10, B10.31; "after the offer proposal lands": `02_CHAR_offer_what_can_be_done` (B10, PROPOSED).
- COST and TIER: calibration; `sonnet`, high; `opus` reads (d). LANDS IT: B98's producer; `Item: B98.15`, `[skip ci]`.

### B98.16 — `rival_gain` stays at 0 and `stance_polarity` stays `declared` · rows 17, 18; B10.63, B10.69; H-180; `17_CENSUS_C1A_02` W4 · BLOCKED (design: no target reading) · HASH EQUAL
- SOURCE: part 2 §4 rows 17, 18; `workplan_v12_part13.md` B10's second-half `DIALS AT CONTROL` lines: `rival_gain` "set by B98; target: none stated"; `stance_polarity` "set by: no batch (`17_CENSUS_C1A_02` W4: 'the flip is design-first' …); target: none stated".
- SETTINGS: (row 17) `engine/season/data/fixtures.py` (`rival_gain`) = 0.0, shipped by B10.63 (read by `decision/options.py::teller_weight`); (row 18) `stance_polarity` = `"declared"` (the `beneficiary` arm ships unswitched; B10.69 reads it).
- INSTRUCTION: none; flip nothing.
- OWNER OF THE TARGET: row 17, H-180's design (no design document gives the factor's shape, B10.63); row 18, a design item no batch carries (`17_CENSUS_C1A_02` W4).
- GATE: `FIX(rival_gain)` → 0.0; `FIX(stance_polarity)` → `'declared'` (R2). B99 QUOTES: both as left.
- DEPENDS ON: V12 Batch B10, B10.63, B10.69. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.17 — `said_choices` stays at 1 · row 19; B11.10; `08_FI_02` edit 7 · BLOCKED (design: no target reading) · HASH EQUAL
- SOURCE: part 2 §4 row 19: "`08_FI_02` edit 7 names 1 as the control only".
- SETTING: `engine/season/data/fixtures.py` (`said_choices`) = 1, shipped by B11.10 (the operand range of `tell`, `lie` read through `operand_bags`).
- INSTRUCTION: none; flip nothing. OWNER OF THE TARGET: the FI lane's design of how many sayings a teller weighs.
- GATE: `FIX(said_choices)` → 1 (R2). B99 QUOTES: the value as left.
- DEPENDS ON: V12 Batch B11, B11.10. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.18 — `notice_arm` on, if B11 did not turn it on · row 20; B11.66, B11.67; `18_DETERMINISM_notice_is_a_draw` · BUILD (flip, conditional) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 20 ("IN-BATCH (B11.67 if B11.66's gate reads), else TARGETED"); B11.67: "If any arm fails, do not flip: the commit records the readings, `notice_arm` stays `off`, and the DIALS AT CONTROL line names B98 with this gate as its target"; `proposals/18_DETERMINISM_notice_is_a_draw.md` "Gate" 1, 2, 4 (copied in B11.67).
- CONDITION (U5): open B11.67's commit on `main` (`git log --grep='Item: B11.67'`) and `FIX(notice_arm)`. If it reads `on`, this position records "set by B11.67 @<sha>" and closes as a POINTER (no commit). If `off`, it runs.
- SETTING: `engine/season/data/fixtures.py` (`notice_arm`) = `off` (B11.66). New value: `on`. `notice_ob` stays `routine` (row 21).
- INSTRUCTION: read B11.67's gate at `notice_arm = on` on this base (`PYTHONHASHSEED=0`): "1. Realm seeds 0, 1, 2, one season, `notice_arm: on`: all four bands occur among notice draws; deed claims deposited to non-parties fall strictly below the `off` arm and stay above 0; deposits to doers and subjects are equal across arms (counted per arm). 2. … in a planted world, a witness holding `inquiry` 3 notices a `forge` more often over 200 seeds than one at `pool_default`, and a forger holding a Success cover is noticed less often than one with none; no share is 0 or 1 (`assert checked >= 200`). 4. 04 PART D 41a's permutation test passes at `on`". If every arm reads, `notice_arm` → `on`.
- FALSIFIER and CONTROL: B11.66's ("A non-party witness whose deposit is identical in both arms at every seed …; a Partial deposit that names the hand; a doer who does not know his own act"). Control arm: `HASH(0, 2; notice_arm = off)` equals B98.16's after-reading.
- GATE: `python -m pytest engine/season/tests/test_notice_draw.py -q` → pass; arms 1, 2, 4 quoted; R-07's `told_by` shares from `register --requirements` quoted before and after, not gated (the source); `HASH(0, 2)` recorded.
- HASH MOVERS: "every world with a deed and a non-party witness at `on`" (all of them). EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers, the NPC-088 headless pin, `test_fi03_trail.py`'s realm hash.
- REVERT: `notice_arm` → `off`.
- DEPENDS ON: V12 Batch B11, B11.66, B11.67; Batch B12c, B12c.09 (sabotage reads the notice draw).
- COST and TIER: calibration; `sonnet`, high; `opus` reads arms 1 and 2. LANDS IT: B98's producer; `Item: B98.18`, `[skip ci]` (if it runs).

### B98.19 — `notice_ob` stays `routine` and `record_concluders` stays 0 · rows 21, 22; B11.66, B11.75 · BLOCKED (design: no target reading) · HASH EQUAL
- SOURCE: part 2 §4 rows 21 ("its member is set at calibration"; "B98 may read row 20's gate 1 as its target": a may, not a stated reading, U2) and 22 ("until CR-83's design (B11, `IS-B2-FI-05`) names a sweep and a target").
- SETTINGS: (21) `engine/season/data/fixtures.py` (`notice_ob`) = `routine` `[ASSUMPTION: OBS's control arm]`, B11.66; (22) `record_concluders` = 0, B11.75 (`decision/options.py`, `record`'s pairing).
- INSTRUCTION: none; flip nothing. OWNER OF THE TARGET: (21) the FI lane, a reading for the notice obstacle; (22) CR-83's design (`IS-B2-FI-05`).
- GATE: `FIX(notice_ob)` → `'routine'`; `FIX(record_concluders)` → 0 (R2). B99 QUOTES: both as left.
- DEPENDS ON: V12 Batch B11, B11.66, B11.75. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.20 — four governance steps stay at control · rows 23 to 26; B21.09, B21.12, B21.73, B21.61, B21.69 · BLOCKED (design: no target reading) · HASH EQUAL
- SOURCE: part 2 §4 rows 23 to 26; `workplan_v12_part14.md` and `_part15.md` B21's `DIALS AT CONTROL` lines.
- SETTINGS, each in `engine/season/data/fixtures.py`, each with its reason:
  (23) `rank_step` = 0 (B21.09; obstacle member `rank_gap`): "a proposed 0.25, swept {0, 0.25, 0.5}, `unified/work/R4_READ.md:315`; no reading named".
  (24) `provisional_term`: its first half is set in its own batch (B21.73 sets 2; IN-BATCH, not a member); the later re-centring is "the joint re-centring (OBS §4 step 5) or the story census sets it" (`14_VERBS_BINDING_C_turnover.md` edit 1), no owner after B21.
  (25) `cross_chain_step` = 0 (B21.61): `16_PESSIMIST_FA_B` edit 2, "control 0, proposed 2", no reading.
  (26) `faction_power_step` = 0 (B21.69): `IS-B3-FA-07`, "set by Jordan or the B21 calibration"; B21 runs none.
- INSTRUCTION: open B21.73's commit and record `provisional_term`'s value (expected 2); flip nothing.
- OWNER OF THE TARGET: (23), (25) the FA lane's design of a reading; (24) the joint re-centring or the story census (no batch); (26) Jordan, or a calibration item the FA lane writes.
- GATE: `FIX(rank_step)` → 0; `FIX(provisional_term)` → B21.73's value; `FIX(cross_chain_step)` → 0; `FIX(faction_power_step)` → 0 (R2). B99 QUOTES: all four as left.
- DEPENDS ON: V12 Batch B21, B21.09, B21.12, B21.61, B21.69, B21.73. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.21 — the Calamity's weight leaves 0, with the wound planted · row 27; B12a.07, B12a.63 to .65, B12a.71 (HELD there); `09_WR_world_motion` edit 1; `16_PESSIMIST_WR_B` · BUILD (flip) · HASH MOVER(behaviour), and the build hash
- SOURCE: part 2 §4 row 27 (C-05: part 20 governs); `workplan_v12_part20.md` B12a's `DIALS AT CONTROL` lines and B12a.71; `proposals/09_WR_world_motion.md` edit 1 ("as its own commit and its own mover: `lattice_coupling` 0 → 250 (H-235's swept arm) with `wound=True` the default"); `proposals/16_PESSIMIST_WR_B_the_calamity_strains_and_breaks.md` "The gate that shows it worked" ("On `build_realm` with the wound planted and the weight at 250, nobody acting, fourteen seasons, seeds 0 and 1": the yield "differs between the two seeds"; "at least one `site.ruptured` is emitted in at least one seed, and its season differs between seeds"; "the front stops where it is mended"; "at weight 0 the season is the base hash"); read at two seasons (fourteen in the source; A-114).
- SETTINGS: `engine/season/data/fixtures.py` (`lattice_coupling`) = 0; `engine/season/boot/realm.py::build_realm` (`wound=False` default); `rupture_band` 100, `rupture_base` 2, `rupture_pool_cap` 6 (B12a.64, inert at weight 0). New: `lattice_coupling` 250, `wound=True`; the three rupture values stay as shipped unless the gate fails on them ("re-read at the joint calibration … before the weight leaves 0": read here, not changed). The wound's Site kind is Jordan's content, set by B12a.07 (listed in the PR body, D-19).
- INSTRUCTION: one commit: `lattice_coupling` 0 → 250 and `build_realm`'s `wound` default `False` → `True`; H-235's row text names the reading.
- TESTS: `engine/season/tests/test_in35_lattice_coupling.py` (B12a's four, `test_weight_zero_is_the_base_hash` among them), run at the new defaults.
- FALSIFIER and CONTROL: the source's falsifier; `test_weight_zero_is_the_base_hash`. Control arm: `HASH(0, 2; lattice_coupling = 0)` with `build_realm(0, wound=False)` equals B98.20's after-reading.
- GATE: the test file → pass; seeds 0 and 1, two seasons, nobody acting (the test file's fold): the realm yield at the last season, per seed, quoted and differing; `site.ruptured` count and season per seed quoted (the source's season 13 and 719 are fourteen-season figures, quoted beside, not asserted, U6); the mended-front arm read on the test's planted source; `HASH(0, 2)` and `build_realm(0).content_hash()` recorded.
- HASH MOVERS: every seeded world (the wound strains its neighbours' wear) and the build hash (`wound=True`). EXPECTED RED UNTIL B98.99: `test_go07_canonical_digest.py` (`BUILD[0]` and `SHIPPED`), the `_realm_goldens` readers, the NPC-088 headless pin.
- REVERT: `lattice_coupling` → 0, `wound` default → `False` (one commit).
- DEPENDS ON: V12 Batch B12a, B12a.07, B12a.63, B12a.64, B12a.65; Batch B35 (the Mend, `09_WR_B_threadwork_session_and_practitioner`; B35.27, the wound as Thread ground).
- STOPS IF: H-165 / H-07's wear-0 kinds are not decided on the base (`engine/season/hole_register.yaml` rows H-165 and H-07 still open; `09_WR_world_motion` edit 1: "the flip waits on it"); or the Mend is not callable at the base. Either: stop, report, flip nothing; B99 quotes the weight-0 reading.
- COST and TIER: calibration; `sonnet`, high; `opus` reads the yields and ruptures.
- LANDS IT: B98's producer; `Item: B98.21`, `[skip ci]`.

### B98.22 — `site_yield.harbour.grain` under `ground` stays 40 · row 28; B12a.51 · BLOCKED (design: no target reading) · HASH EQUAL
- SOURCE: part 2 §4 row 28; part 20's `DIALS AT CONTROL` line: "the source's 'a reduced `grain` (fish) of 10' under `ground` is not built here (`B12a.51`, UNDECIDED 3); … target: none stated ('joins JQ-6's sweep')".
- SETTING: `engine/season/rosters.yaml` (`site_yield.harbour.grain` under `ground`) = 40 (today's, both arms).
- INSTRUCTION: none; flip nothing. OWNER OF THE TARGET: JQ-6's sweep (SE lane; no batch carries it).
- GATE: the row `site_yield.harbour.grain` under `ground` in `engine/season/rosters.yaml`, read on the closing tree → 40 (R2). B99 QUOTES: the value as left.
- DEPENDS ON: V12 Batch B12a, B12a.51. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.
