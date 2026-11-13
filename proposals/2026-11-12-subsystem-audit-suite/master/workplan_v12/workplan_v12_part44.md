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
REQUIREMENT: none — the settings batch (`V12_STRUCTURE.md` §2.2: "none of its own: the mechanisms shipped dormant begin to run", CLAUDE.md §0.2). No conjunct's `reading:` record is written here and no `status:` is edited: B99 re-takes all nine on this batch's closing tree (D-22: "a reading and a mover in one close would make the re-take's tree the one being re-pinned"). The close quotes `register --requirements` and the `m1_acceptance` verdict line in its commit body only.
BATCH GATE (read once, on the closing tree; `PYTHONHASHSEED=0` on every seeded command; nothing past two seasons, D-17):
  `python -m engine.season.harness.register --check` → exit 0; `python -m engine.season.harness.register --requirements` → nine lines, quoted (no `status:` changed by this batch);
  `python tools/m1_acceptance.py --summary` → its verdict line, quoted;
  `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 2 s` for s = 0, 1, 2 → the `BUILT OUT`, `ENGINES`, `NULL SCENES` and `FOUGHT FIELDS` lines before (`reading @<B40 closing sha>`) and after; **every verb built out at B40's close is still built out** (a flip that leaves a verb not built out is reverted, P8; `IS-A-08`'s rule applied to settings);
  every flip item's own GATE reading, quoted from its commit body (`## Readings` R1 lists them); every BLOCKED position's control value read on the closing tree (R2);
  the realm content hash at seeds 0, 1, 2, one season → the values B98.99 re-pins;
  `python tools/export_sim_params.py --check` → exit 0; `python tools/export_engine_params.py --check` → exit 0; `python tools/ci_golden_modes_check.py` → every digest equal to B40's close unless a flip names the fight's curve (rows 32, 47, 61: each declares it); `python tools/ci_sim_fabrication_check.py` → exit 0;
  the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names (the batch edits `engine/season/data/fixtures.py` and registries: the full gates, CLAUDE.md §0.4);
  "the close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the named conjuncts' readings with their tree, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<sha>`) and after, and the batch's measured wall time; the last `Item:` commit writes the conjuncts' `reading:` records; `status:` is not edited" (`IS-A-12`), read here as: this batch names no conjunct, so it writes no `reading:` record.
RE-PIN: once, in B98.99's commit: `engine/season/tests/_realm_goldens.py` (B02's one pin file): `SHIPPED` and `CENSUS` at seeds 0 to 2, and `BUILD[0]` if a flip moved the build (row 95, `cohort_convictions`, declares it); the NPC-088 headless hash; the corpus pins and the combat goldens only where a flip moved them; each old → new in the body, read against B40's close (`reading @<sha>`); the commit says "re-pin: B98, behaviour movers B98.<n>, … (the settings flipped); the BLOCKED positions moved nothing".
IDS: ED-IN 0; H 0 (no position writes a ledger or hole-register row: every setting's NUMBER row was written by the batch that shipped it, and a flip edits that row's text in its own commit; a BLOCKED position records its reason in B98.99's commit body and the PR body, D-19). The held blocks stay unused and are named in the expunge: `ED-IN-0399..0400`, `H-846..H-850` (part 2 §9, which supersedes the head's §12 figures `ED-IN-0398..0399`, `H-845..H-849`; UNDECIDED U8). B99's blocks `ED-IN-0401..0402`, `H-851..H-855` are not touched.
DIALS AT CONTROL: none set by a later batch (this batch is the setter). The settings it leaves at control are its BLOCKED positions; each is quoted by B99 on the tree as left (R2).

**Two reads every flip item uses** (defined once here; an item names them):
- **`HASH(s, n; key = v)`**, the realm content hash at seed `s` after `n` seasons with one setting overridden: `PYTHONHASHSEED=0 python -c "from engine.season.boot.realm import build_realm; from engine.season.harness.populated import run; w = build_realm(s); w.fixtures = w.fixtures.sweep('<key>', <v>); run(n, s, w=w); print(w.content_hash())"`. Without `key = v` it is the shipped arm. `[ASSUMPTION: `run` stays at `harness/populated.py::run` after B03c moves `build_realm` to `boot/realm.py` — basis: `V12_STRUCTURE_part2.md` §5.10 moves `build_realm` and `chooser` only; `Fixtures.sweep` (`engine/season/data/fixtures.py`, read at `f4eb906`) returns a swept copy; `run(seasons, seed, cap, w)` takes a built world (read at `f4eb906`); B05's second half reads its control arm the same way, part 9's head]`. A setting that is not a `Fixtures` key (a roster row, a module constant, a column of `references/troops.yaml`) names its own override in its item (a scoped edit restored in `try/finally`, B21.72's `SUCCESSIONS` precedent).
- **The control arm.** After the flip, `HASH(0, 2; <key> = <control value>)` equals the previous position's recorded after-reading `HASH(0, 2)` (`reading @<sha>`, in that position's commit body; for B98.02, the batch's base reading). A control that moves falsifies the item (P8: revert). The base reading is taken once at the batch's open on B40's closing tree, `HASH(0, 1)` and `HASH(0, 2)`; `HASH(0, 1)` must equal B40.99's re-pinned `SHIPPED[(0, 1)]` (the control that the run happened, CLAUDE.md §0.1 pt 3).

**Every flip is a behaviour mover; one re-pin only, at B98.99.** Each flip item's `EXPECTED RED UNTIL B98.99` names the tests that read `_realm_goldens.py`'s `SHIPPED` or `CENSUS` (`git grep -ln '_realm_goldens' engine/season/tests` at the item's open; at B02's text: `test_go07_canonical_digest.py::test_go07_control_the_world_did_not_move_only_its_digest`, and the readers in `test_cp_t04_07_surrender.py`, `test_cr81_realm_acquaintances.py`, `test_strife_credit.py`) wherever its flip moves the one-season pin, and the NPC-088 headless pin where it moves; each stays under `[skip ci]`. A flip whose effect cannot show in one season leaves the pins green and says so.

UNDECIDED (each reading taken is the one that changes less, `V12_STRUCTURE_part2.md` §5.1; for the receipt and the 0.1 stop):
  (U1) **Grouping (E-13).** A TARGETED row stays one item (one flip, one commit, one control arm). BLOCKED rows of one owner batch that sit next to each other in the table, ship at control in the same owner file and read the same way are one position, each row still its own numbered record inside it: rows 8 and 9 (B98.08), 17 and 18 (B98.16), 21 and 22 (B98.19), 23 to 26 (B98.20), 37 to 39 (B98.31), 41 and 42 (B98.33), 51 and 52 (B98.42), 68 and 69 (B98.58), 74 to 76 (B98.63), 78 and 79 (B98.65), 81 to 83 (B98.67), 84 to 87 (B98.68). The reason is the handle form: 105 rows and `.99` do not fit two-digit positions (`V12_STRUCTURE_part2.md` §5.3). The other reading (one position per row) needs a three-digit handle the skill's `Bnn.mm` form does not use; it changes more.
  (U2) **Order.** The table's order, except where a target reads another setting: row 95 (`cohort_convictions`) lands before row 94 (`sway_gain`), whose gate reads "with `cohort_convictions` on" (B98.76 lands before B98.75; the handles keep the table's order and the position table lists landing order); row 61 follows row 60 (the table's own note); row 71 (`presumption_gain`, "after B39's prehistory") lands after row 100 (`prologue_seasons`) only if its item's STOPS IF reads that the prehistory is the prologue (B98.60 says which). Row 21 (`notice_ob`) stays BLOCKED (its target is "may read row 20's gate 1": a may, not a stated reading).
  (U3) **The ids.** The prompt for this lane names `ED-IN-0398..0399`, `H-845..H-849`; part 2 §9 shifts every IN range by +1 and every H block from B12c on by +1 and says it supersedes the head's §12. Taken: part 2 §9's. This batch writes none either way.
  (U4) **A sweep's chosen point.** Where a source gives a sweep and a reading rule, the item runs the sweep as a probe (seeds named, two seasons at most) and ships the smallest value whose reading satisfies the rule; where several satisfy it and the source names a first value, that value. Where none satisfies it, the item ships nothing, keeps the setting at control and records the reading (the row becomes a READING for B99), never a value outside the swept set.
  (U5) **IN-BATCH rows** (20, 24, 48, 70, 73, 80, 104). Each item opens its owner batch's `.99` commit body (or the owner item's commit) on `main` and runs only if the setting is still at control there; if the owner set it, the item records `set by <handle> @<sha>` and is a POINTER at close (no commit). Part 2 marks row 24's first half set by B21.73; its item is the BLOCKED re-centring only.
  (U6) **Two-season reads of longer sources.** A source reading at three, four, six, eight, fourteen or twenty seasons is read at two with the source's horizon noted (D-17, `workplan_v12.md` P10); where two seasons cannot show the target, the flip is not made and the row's reading is B99's (`workplan_v12.md` §6). Rows so treated: 8, 9, 51, 52 (A-114, BLOCKED) and the longer arms of 27, 90, 100, quoted at B99.
  (U7) **Content at its seed.** A flip whose new value is the source's `[ASSUMPTION; Jordan to correct]` (rows 6, 103, 105's pools and obstacles) ships it marked so and lists it in the PR body for Jordan's correction (D-19); it is not a value chosen here.
  (U8) **One `opus` read per flip** (CLAUDE.md §10): the reading against the source's target is the judgment node; `sonnet` runs the sweep and the commands. A reading the `opus` reader judges not to meet the target reverts the flip (P8), and the row is recorded in R1 as "not flipped: <reading>".
