# Workplan v12 — part 44, continued (3): batch B99-nine-retake

## Status: PROPOSED (the third continuation of part 44: the plan's last batch; drafted under `master/workplan_v12/`; unratified until Jordan adopts v12; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

Paths and words as stated in `workplan_v12_part44.md`. `IS-A-13`, the item this batch carries, is `master/instructions/IS_A_NINE_part2.md` §11; the nine rows' conjuncts are `IS_A_NINE.md` §2 to §10, as `IS-A-02` (B02.38) wrote them into `engine/season/requirements.yaml` and later batches re-pointed them (`IS-A-10` in B07; `IS-A-04`'s `scales:` rows). The file is the owner of every conjunct's `argv`, `expects`, `holds` and `reading` (CLAUDE.md §0.05: a fact a program reads lives where code reads it); the tables below are reference for the reader and are not run from.

---

## Batch B99-nine-retake · lane IN · wave W24 · step S24 · HASH EQUAL
INVOCATION: /methodology-execute Batch B99-nine-retake
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
GATE: Batch B98-dials
HASH READING: `PYTHONHASHSEED=0 python -c "import sys; from engine.season.boot.realm import build_realm; from engine.season.harness.populated import run; s, k = int(sys.argv[1]), int(sys.argv[2]); w = build_realm(s); run(k, s, w=w); print(w.content_hash())" <s> <k>` → the realm content hash at seed `<s>` after `<k>` seasons: `<k>` = 1, one season, unless the gate names two (never more before B99, D-17); `<k>` = 0 reads the build hash; per item `<s>` = 0 (a mover's reading, E-2), at `.99` `<s>` = 0, 1, 2; each value quoted `reading @<sha>`, the tree it was read on (`workplan_v12.md` §3.B, "the hash reading").
REQUIREMENT: R-01 to R-09, every conjunct, re-taken once on B98's closing tree (A-114; `V12_STRUCTURE.md` §3, row "the settings, then the re-take": "all nine, on B98's closing tree (the settings as set)" → "`m1_acceptance --summary` row 3 reads what the readings say"). Expected, as `IS_A_NINE_part2.md` §12.1 states it for the last milestone before this one (M5: "all nine hold") and for each row's own milestone: R-01, R-02, R-03 hold (M0); R-03 with R-03.c, and R-09.a, .c, .d, .e (M1); R-06, R-08, R-09 `met`, R-07 `met` or one conjunct short (M2); R-05 `met`, `built out n of n` (M3); R-04 `met`, "`m1_acceptance` row 3 reads 9 of 9" (M4). These are expectations to be read, not results: a row moves only on its readings.
BATCH GATE (read once, on the closing tree; `PYTHONHASHSEED=0` on every seeded command):
  `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`); `python -m engine.season.harness.register --requirements` → nine lines in `IS-A-01`'s form (`R-0n  <status>  <held> of <m> conjuncts  tree <oldest reading.tree>`), every row at the status B99.01 wrote, every `reading.tree` equal to B98's closing SHA, exit 0 (`IS-A-01`'s refusals: no `met` with a conjunct `unread` or without `reading.line`);
  `python tools/m1_acceptance.py --summary` → row 3 reads the count of rows at `met` that B99.01 wrote, still self-declared DOC-DERIVED; the verdict line quoted;
  the realm content hash at seeds 0, 1, 2, one season → equal to B98.99's re-pinned `SHIPPED` (nothing in this batch moves a world: the EQUAL reading);
  the test files that read `engine/season/requirements.yaml` (`grep -rl requirements.yaml engine/season/tests tests/valoria`; at the plan's text `test_register_reading.py`, `test_check_requirements.py`) and the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names (CLAUDE.md §0.4 cl. 1: a data-only diff runs the files that read the data, not the whole suite);
  "the close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the named conjuncts' readings with their tree … and the batch's measured wall time" (`IS-A-12`); here the last `Item:` commit before `.99` (B99.01) writes the `reading:` records and the `status:` lines.
RE-PIN: none (hash EQUAL; `IS-A-13`: "Hash movers: none"; a held row that fails is never answered by a re-pin).
IDS: ED-IN 0; H 0 (block held: `ED-IN-0401..0402`, `H-851..H-855`, part 2 §9). A failing conjunct is listed in the PR body for Jordan; one `ED-IN` row from the block is written only for a failing held row (R-01, R-02, R-03) that survives the five-step ladder as a decision of his (CLAUDE.md §0, `needs_jordan` is not a parking space). Unused ids are named at the expunge.
DIALS AT CONTROL: none (a reading batch; every setting is as B98 left it, R2 of part 44's `## Readings`).
UNDECIDED:
  (U1) **A row that would move down.** `IS-A-13` sets `status:` "to `met` only where every conjunct holds, to `partial` where some do, and leave it where none moved"; its held-row clause: "Where a held row (R-01, R-02, R-03) fails a conjunct: stop, report, do not edit the conjunct and do not re-pin a golden to pass it". The lane's prompt: "a row that does not hold keeps its status and the failing conjunct is quoted with its tree and listed for Jordan". Taken (the reading that changes less): a row moves up by `IS-A-13`'s rule; a row whose readings would move it down (a `met` row with a conjunct now `no`) keeps its `status:`, its conjunct's `holds:` and `reading:` record the failing reading with its tree, and the row is listed for Jordan; for R-01, R-02 and R-03 the run stops there (`IS-A-13`), the remaining rows are read, and the close is `STOPPED`.
  (U2) **The horizon.** `IS-A-13`'s gate states no season count; it runs "every conjunct `argv` of the row". Taken: each conjunct's `argv` exactly as `requirements.yaml` holds it on B98's closing tree, at the season count written in it (D-17: "the longer form is left to B99's conjunct `argv`"; where a source's four-season form was written there, four). The readings past two seasons that are not conjuncts (step 6) are quoted at their sources' horizons and move no row.
  (U3) **What the `holds` of a reported-not-asserted conjunct is.** A conjunct whose `expects` is a printed figure with no bar (R-01's retired sweep is deleted; `aperture`'s built-out total "is a reading, never a threshold, until the re-take that closes R-05", `IS-A-06`) is read against the bar its row's conjunct text gives at this re-take (`built out <n> of <n>`); none other is invented.
C(B99-nine-retake): this batch's entry; the plan's head parts; `engine/season/requirements.yaml` (every row's `conjuncts:`, `scales:`, `measure:`); `engine/season/harness/register.py` (`check_requirements`); `tools/m1_acceptance.py` (`row_nine_requirements`); every instrument a conjunct's `argv` names (at the plan's text: `harness/corpus_run.py`, `harness/storybar.py`, `harness/headless.py`, `harness/aperture.py`, `harness/governance_spine.py`, `harness/decision_spread.py`, `harness/conviction_spread.py`, `harness/chronicle.py`, `harness/valley.py`, the pytest files named in §2 to §10 of `IS_A_NINE.md`); for step 6, `harness/worldgen.py`, `harness/institution.py`, `harness/strife.py`, `tests/valoria/test_scar_stock.py`'s home, part 44's R2 and its BLOCKED positions B98.08, .42, .71, .81 and the upkeep and sway lines of R1; B98's closing SHA; the skill's "Running a slow instrument"; the permanent surface (CLAUDE.md, `CURRENT.md`, `HANDOFF.md`, `registers/handoffs/HANDOFF_IN.md`, the skill and `methodology-close`).
PARALLEL: S24, alone in the plan. No sibling; no merge position.
BACKGROUND RUN: every conjunct `argv` that runs a season loop, and step 6's runs, are sized on two small runs (one and two seasons) at the batch's open (the skill: "Time two sizes on the axis that will scale … fit the growth, extrapolate with a margin"; "a season's cost roughly doubling with each season played" is a recorded estimate, not a reading), launched in the background on B98's closing tree before B99.01's reading step, at most `max(1, nproc − round(load average))` at once, and read at B99.01. A run past three times its estimate is examined, not assumed dead; a limit that kills a run is a measurement failure, reported as one, never read as a result.
COST: instrument time; `sonnet` runs; `opus` reads each conjunct's printed line against its conjunct text before any `holds` or `status:` is written (the judgment node that gates a requirement, CLAUDE.md §10; `IS-A-13`).
EST: 5 h [estimate: the structure's figure; the instrument time is not known before the sizing runs, and the twenty-season and eight-season readings of step 6 dominate it]

THE NINE, AS `IS_A_NINE.md` §2 TO §10 STATE THEIR CONJUNCTS (reference for B99.01's reader: the `argv` run is the one `requirements.yaml` holds; a conjunct the file no longer holds is not run, and one it holds that this table lacks is run):

| row | conjuncts and the reading each expects |
|---|---|
| R-01 | .a `corpus_run`: `check R3: n of n pass` on both lanes, `not True: none`, control `R3 False -> True`; .b `pytest engine/season/tests/test_realm_requirements.py -q -k r01`: three seeds green, the witness-cut control 0; .c `storybar --remove --base-seed 0 1 2 --seasons 2` (`IS-A-03`'s form): replay `0` at each seed, `n >= 1` |
| R-02 | .a `-k r02`: seeds 0–2 differ after a common prefix, the same seed twice one sequence; .b the R-01.c run: `m >= 1`, a differing act at a later (season, lap) |
| R-03 | .a `pytest engine/season/tests -q -k test_u2_`: all pass, the one-round control among them; .b `headless --case NPC-088 --seasons 2 --seed 0`: exits 0, prints `rounds=` per season (the harness key keeps its string, D-05: the season's laps); .c `test_scene_sequence.py`: five tests; control `interactions_per_scene = 1` reproduces the pre-edit hash |
| R-04 | .a `aperture 4 0`: each of `requisition`, `issue`, `open_case`, `determine`, `convene`, `dispatch`, `confer`, `establish`, `revoke` with the `BUILT OUT` block's `via` at least 1; .b `engine/mc_v18.py` absent, `test_faction_q.py` green; .c1 to .c7 per `scales:` row: the creation sheet test, `train` built out, `chronicle --seed 0` tells; `governance_spine play 0 8 --world realm` exit `closed True` at seeds 0–2; `headless --world hearing` the same hash twice; `field.won + field.lost` above 0 at `aperture 1 s`, s = 0–2, beside `field.unopposed`, and `test_field_scene.py`; a duel at `aperture 2 s`, the cell field, `test_none_decider_equals_no_decider`, `test_squad_field.py`; `harness.valley`, `test_valley.py`, `found`, `build`, `work` built out at `aperture 4 0`; `test_shortest_case.py`, `test_playable_inquiry.py` |
| R-05 | .a `corpus_run`: `WHERE THE <n> GO: 0 … · 0 … · 0 …`, or .b for every verb in the last two classes; .b `aperture 4 --seeds 0 1 2`: `built out <n> of <n>`, n = `len(VERB_TABLE)` at measurement time; .c the same run: `NULL SCENES` 0 for every verb (A-81) |
| R-06 | .a `corpus_run`: the `RANKING DISCRIMINATION` line, no verb under `RANKING EXCLUDES`; .b recorded, "blind: it does not count"; .c `conviction_spread` passes; .d `decision_spread --decisions`, seeds 0–2: strict-top share above one half beside the control τ `[ASSUMPTION: one half, H-96]`; .e `decision_spread --persons`: n of n (the generated cast if B98.80 flipped `variable`) |
| R-07 | .a `pytest engine/season/tests -k 'choose_receives_no_world or a_view or r7_two_persons'`; .b two hearers, different regard after two realm seasons (`[UNVERIFIED]` test name in the source: the `argv` the file holds is run); .c `aperture 1 s`, s = 0–2: `field.won + field.lost` above 0 with the losing side's `Person.stance` receipt (the `FOUGHT FIELDS` line); .d `-k r07`: a planted regard changes the top candidate at least once in seeds 0–2, the unplanted seed equal |
| R-08 | .a `corpus_run` and `decision_spread --decisions`: every tie between candidates of equal, nonzero choice score; .b `-k test_u4_the_choice_is_sampling`; .c `decision_spread --season --seed s`, s = 0–2: the non-top share above 0 at the shipped setting and 0 at temperature 0 |
| R-09 | .a `pytest engine/season/tests/test_task_draw.py -q` (re-pointed by `IS-A-10`); .b `aperture 4 0`: `POOLS ROLLED` *two actors at different pools: yes* on a non-combat verb, beside the all-default control; .c `corpus_run`: `DEGREES RESOLVED BY VERB`, a non-combat verb besides `tell` at two bands whose writes differ; .d `test_converted_verb_resolves_in_at_least_two_bands` (the 90 % share, seeds 0–2); .e `pytest engine/tests/test_draw.py -q`; same seed twice, same hash |

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B99.01 | the re-take: every conjunct of the nine read once, longer, on B98's closing tree; the only item that may edit a row's `status:` | `IS-A-13` | BUILD | EQUAL | Batch B98 |
| B99.99 | close readings: the EQUAL reading recorded, nothing re-pinned | `V12_STRUCTURE_part4.md` E-1 | BUILD | EQUAL | B99.01 |

### B99.01 — the re-take: every conjunct of the nine read once, longer, on B98's closing tree · `IS-A-13` · BUILD · HASH EQUAL
- SOURCE: `master/instructions/IS_A_NINE_part2.md` §11, "Item: IS-A-13 — the re-take: the one item that may move a row" (PLACEMENT, INSTRUCTION, WHERE, FALSIFIER, GATE, Hash movers, Depends on, Lane, Cost and tier); §12.1; `IS_A_NINE.md` §1.2 item 3 ("A row moves only at a re-take"), §2 to §10 (the conjuncts); rulings A-114 ("the longer re-take of the nine runs once, as the plan's very last item, not at each milestone"); D-17; `workplan_v12.md` §6; H2's HD-26.
- ADVANCES: R-01 to R-09 (the row each reading names).
- INSTRUCTION (`IS-A-13`, copied: "on the batch's closing tree, `PYTHONHASHSEED=0`: run every conjunct `argv` of the row (the long ones launched in the background at batch open on the base and re-run only if `git diff <base>..HEAD` touches what they reach); write each `reading:`; set `holds`; set `status:` to `met` only where every conjunct holds, to `partial` where some do, and leave it where none moved. State in the commit body what the readings do not show. Where a held row (R-01, R-02, R-03) fails a conjunct: stop, report, do not edit the conjunct and do not re-pin a golden to pass it."), in steps:
  1. **The base.** B98's closing SHA, `git rev-parse HEAD`, recorded. The before-readings: `register --requirements` and `m1_acceptance --summary` as B98.99's body quotes them (`reading @<B98 sha>`), not re-taken.
  2. **The list.** A scratch reader (not committed) prints, from `engine/season/requirements.yaml`, every row's conjuncts as `id  argv  expects`; `scales:` rows print with their `conjunct:` (`IS-A-04`). Its count is asserted against the file (`assert listed == sum(len(r["conjuncts"]) for r in rows)`, CLAUDE.md §0.1 pt 2). No `argv` is edited: a conjunct whose `argv` fails to resolve is read `no` with the error as its line (the register already refuses an unresolvable `argv`, `IS-A-01` (c)).
  3. **Size, then launch** (the head's BACKGROUND RUN): each season-running `argv` timed at one and two seasons, its full time extrapolated, then launched once: `PYTHONHASHSEED=0 exec python -u <argv…> > "$SCRATCH/b99/<conjunct id>.log" 2>&1`, its `$!` and `ps -o lstart= -p $!` written to `<conjunct id>.pid` in the same call, a wrapper appending `EXIT <code>` (a reading counts only with `EXIT 0`, or a pytest `argv`'s expected code); watched by CPU time (`ps -o cputime`; CLAUDE.md §11). The pytest `argv`s run in the foreground.
  4. **Read.** For each conjunct: its log's printed line against its `expects`; the control the conjunct names (the replay line `0` of R-01.c, the witness-cut control of R-01.b, the one-interaction control of R-03.c, the all-default control of R-09.b, temperature 0 of R-08.c, the same seed twice of R-09.e); `holds: yes` only on the printed line and its control both; `no` otherwise; the `opus` reader reads each line against its conjunct text before anything is written.
  5. **Write** `engine/season/requirements.yaml`, the one file, the only fields: per conjunct `holds:` and `reading:` with `tree` (B98's closing SHA), `date`, `seed`, `seasons`, `line` (the printed line, verbatim), `control`, `does_not_show` (`IS-A-01`'s record); per row `status:` by `IS-A-13`'s rule with UNDECIDED U1 (`met` only where every conjunct reads `yes`; `partial` where some do; unchanged where none moved; never down); `measure:` untouched. A held row (R-01, R-02, R-03) with a conjunct `no`: its conjunct is not edited, the run stops after the other rows are read, and B99 closes `STOPPED` with the reading quoted for Jordan.
  6. **The readings past two seasons that are not conjuncts:** `## Readings` R1 below, launched with step 3, quoted in the commit body with their tree; they move no row and ship nothing.
  7. **After.** `python -m engine.season.harness.register --requirements` and `python tools/m1_acceptance.py --summary` on the edited tree, quoted; the commit body states, row by row, what the readings do not show (`IS-A-13`), and lists every conjunct read `no` with its tree for Jordan.
- WHERE: `engine/season/requirements.yaml` (per conjunct `holds:` and `reading:`; per row `status:`; nothing else). No code, no test, no pin.
- TESTS: none new.
- FALSIFIER and CONTROL: `IS-A-01`'s refusals ("a `met` row with one conjunct at `unread` exits non-zero; a `met` row whose conjunct has no `reading.line` exits non-zero"); the batch critic reads each `reading.line` against the run's saved log (`IS-A-13`, "v11 part 2's named gate, kept"); `IS-A-12`'s: "a conjunct at `yes` whose `reading.tree` is older than the last batch that named it". Control: the realm content hash at seeds 0 to 2, one season, equal to B98.99's re-pinned values (nothing here moves a world).
- GATE (`IS-A-13`, copied): "`register --requirements` prints the row at its new status with every conjunct held; `m1_acceptance --summary` row 3 moves by one" for each row moved; read here as: every row whose `status:` changed prints it with its held count, and row 3 moves by the number of rows newly `met`; exit 0. Expected (§12.1, M5 and the milestone rows): all nine `met`, row 3 nine of nine. A reading short of it is recorded as read, never rounded up.
- HASH MOVERS: none.
- DEPENDS ON: V12 Batch B98-dials (its closing tree); `IS-A-01`, `IS-A-02` (B02: the conjunct record and the register's refusals), `IS-A-06` (B02: the `BUILT OUT` block), `IS-A-07` (`NULL SCENES`), `IS-A-10` (B07), `IS-A-11` (BA1); every batch whose `REQUIREMENT:` line wrote a conjunct's `reading:` (part 2 §10's map).
- GLOSSARY: none.
- COST and TIER: edit plus instrument time; `sonnet` runs; `opus` reads the readings against the conjunct text (`IS-A-13`: "the judgment node that gates a requirement").
- LANDS IT: B99's producer; `Item: B99.01`, `[skip ci]`. The permanent-surface rule (`V12_STRUCTURE_part3.md` §7.6): `requirements.yaml` takes `reading:` records from every batch's last `Item:` commit and `status:` from this item alone; it is edited once here, in one commit, with no other batch open (S24).

## Readings

**R1 — B99.01 step 6: the readings past two seasons that are not conjuncts** (A-114; part 44's R2 rows marked `A-114`, the longer arms its positions left, and H2's HD-26). Each moves no row and ships nothing (B99 is hash-EQUAL); each is a quotation for Jordan, and whether any setting flips on it is his (P10, "unless Jordan calls for it"):
- (a) `02_CHAR_scar_is_a_wound` gates (b) and (c) at eight seasons, seeds 0 to 2, at the four live arms together, read in-process (B98.08); and `U5a_CHAR_owed_amendments` §8 item 1 at `scar_weight_shift` 1 only if (b) reads a share strictly between 0 and 1.
- (b) CR-90's arm for the Church Influence band triggers and the untested Turmoil and goal-row triggers (B98.42), at four seasons `[ASSUMPTION: four — basis: CI starts at 28 and moves at most ±5 a season, so the first band, 40, is reachable from season 3; the plan's other longer reads are four-season `argv`s; Jordan may call a longer one]`, each band's crossing per seed.
- (c) `20_NARRATIVE_B` world (ii), `build_realm`, seeds 0 to 2, six seasons, at the shipped `dues_valence` (B98.71).
- (d) CP-T08-08's "seed 1, six seasons, `term.renewed` > 0" at the shipped `upkeep_lead` (B98.36).
- (e) PG-4's story inventory at A-51's prologue of five years (`5 × len(SEASONS_OF_YEAR)`), seeds 0 to 19, through `python -m engine.season.harness.worldgen --range 20 --prologue <that>` and its cache (B98.81).
- (f) `31_WR_B`'s readings 2 to 6 at six seasons and its core-motion target at four, at the shipped `sway_gain` (B98.75).
- (g) `16_PESSIMIST_WR_B`'s fourteen-season front (the yield at season 13 above 719 and differing between seeds 0 and 1; a `site.ruptured` whose season differs), at the shipped `lattice_coupling` (B98.21).
- (h) the readings HD-26 names: `claim_fade` edit 5's `MAX_SEASONS` reading; B39.18's docket past season 8; `HAP_D` G-1(ii).
- (i) B40's endings two seasons could not reach (part 43's U13: `roga`'s sworn terms at season 4, the long vacancy, SYN-E's "the same ending at every seed" arm).

### B99.99 — close readings: the EQUAL reading recorded, nothing re-pinned · `V12_STRUCTURE_part4.md` E-1 · BUILD · HASH EQUAL
- SOURCE: E-1 ("for a hash-EQUAL batch it records the EQUAL reading and re-pins nothing"), E-2; `V12_STRUCTURE_part2.md` §5.12; B21s.99's form.
- INSTRUCTION: read the BATCH GATE once on this tree; record in the commit body the realm content hash at seeds 0, 1, 2 after one season, equal to B98.99's re-pinned `SHIPPED` (`reading @<B98 sha>`); `register --requirements` (nine lines) and `m1_acceptance --summary`'s verdict line; the background runs' wall times and worker counts; the batch's measured wall time; the list for Jordan (every conjunct read `no`, with its tree; step 6's quotations). Re-pin nothing.
- WHERE: none but the commit body (the batch's last `Item:` commit carries the readings).
- TESTS: none new.
- FALSIFIER and CONTROL: any realm hash moved; any file other than `requirements.yaml` in the batch's diff.
- GATE: the BATCH GATE.
- HASH MOVERS: none.
- DEPENDS ON: V12 B99.01.
- GLOSSARY: none.
- COST and TIER: reading; `sonnet`, high.
- LANDS IT: B99's producer; `Item: B99.99`, no `[skip ci]` (the batch's last `Item:` push, which opens BATCH-CLOSE; as the last batch of the plan it is also the run's `/close`, the skill's "The last batch is also the run's `/close`").

| STOP. Batch B99-nine-retake closes here |

SERIAL EDGES (written last, E-11): within the batch: B99.01 → B99.99. With other batches, by file: `engine/season/requirements.yaml` B02 → (every batch's last `Item:` commit, `reading:` only) → B40 → B99 (`status:` here alone); no other file.

FILE CENSUS (this batch's edits, for H2): `engine/season/requirements.yaml` (B99.01: `holds:`, `reading:`, `status:`). Read only: every instrument and test file a conjunct's `argv` names; `engine/season/tests/_realm_goldens.py` (the EQUAL reading).
