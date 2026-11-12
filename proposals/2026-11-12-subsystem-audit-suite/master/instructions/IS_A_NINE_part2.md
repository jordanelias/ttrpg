# Instruction suite, lane IS-A — part 2: the items, the milestones, the requirement map

## Status: PROPOSED (part 2 of `master/instructions/IS_A_NINE.md`; nothing here is applied; resolves nothing at runtime)

Read at `6e1ea91`. Batch handles `B00` to `B41` are `unified/U3_DEPENDENCY_ORDER.md`'s; `B03a` and `B13` are
`master/CODEBASE_IMPROVEMENT_PROPOSAL.md`'s; `BA1` is created here. `[handle provisional: v12's author
renumbers it; sibling lanes of this suite may create batches of their own.]` Dependency marks:
EXISTS (in the tree at `6e1ea91`), PROPOSED (another proposal's edit, with its batch), MISSING (no carrier).

Checked: 2026-11-12, Sonnet check (`master/instructions/IS_CHECK.md`). Decided and edited here: `IS-A-09` is a
pointer to `IS-MB-02` (one siege item); `IS-A-05` and `IS-A-07` are the owners of the R-07 and R-08 readings and
of `null_scenes` (`IS-B2-CORE-03` and `-04` point here); `BA1-cast-content` is the one cast-content batch
(`IS-B2-CHAR-03` joins it); **Lands it, for every item of this file that names no one: the batch's
`valoria-author` producer, one `Item: <handle>` commit, `[skip ci]` except the batch's last (STAGES practice 3b),
the batch close by `methodology-close`.**

## 11. The items

Thirteen items. Seven add an edit no proposal carries; six point at a proposal or a gap text and add what
it lacks. None changes what a seeded world does except `IS-A-09` (a pointer; the new posture is `IS-MB-02`'s) and
`IS-A-11` (authored values); the rest are instrument and register work, hash EQUAL.

---

**Item: IS-A-01 — the conjunct record: a row's `met` text is data the register reads**
· **Advances:** all nine (the definition of done gets an owner; no row moves).
· **INSTRUCTION** (ordered; one commit, landing *as* §1 of `proposals/01_CORE_requirements_reading_record.md`
rather than after it, so the nine rows are reshaped once):
1. `engine/season/requirements.yaml`, each of the nine rows: `measured:` leaves (the file's history is its
   git log, as that proposal decides); the row gains `conjuncts:`, a list of
   `{id, text, argv, expects, holds, reading}` where `id` is `R-0n.x`, `argv` is a list (the command, no
   shell string), `expects` is the printed line or the test names, `holds` is one of `yes | no | unread`,
   and `reading` is that proposal's record (`tree`, `date`, `seed`, `seasons`, `line`, `control`,
   `does_not_show`), required where `holds` is `yes` or `no`. A retired conjunct is deleted; the commit
   body names it. `measure:` stays one line per row for `tools/m1_acceptance.py` and the dossier script,
   and names the row's cheapest conjunct.
2. `engine/season/harness/register.py::check_requirements` (the owner of the shape; EXISTS, `:631-701`):
   refuse `status: met` unless every conjunct reads `holds: yes` with a `reading.tree`, `reading.seed` and
   `reading.line`; refuse `partial` with no conjunct at `yes`; refuse a conjunct with no `argv`; resolve
   `argv[0:3]` by the three rules of `16_PESSIMIST_CORE_the_nine_gate_and_a_knockout_reading` edit 1 (a
   module by `importlib.util.find_spec`, a path by existence, a `-k` by test name), which that proposal
   says the typed record replaces: its regexes are not written at all. Print, per row,
   `R-0n  <status>  <held> of <m> conjuncts  tree <oldest reading.tree>`.
3. `tools/m1_acceptance.py::row_nine_requirements` (EXISTS, `:293`): its detail line adds
   `conjuncts held <h> of <m>`; it stays DOC-DERIVED and says so.
· **WHERE:** the three files above; NEW `engine/season/tests/test_register_reading.py` (named by the
reading-record proposal; MISSING) and `engine/season/tests/test_check_requirements.py` (named by the
nine-gate proposal; MISSING).
· **FALSIFIER and control:** planted scratch copies through `monkeypatch.setattr(register, "REQUIREMENTS",
scratch)`: (a) a `met` row with one conjunct at `unread` exits non-zero; (b) a `met` row whose conjunct has
no `reading.line` exits non-zero; (c) `argv: ["python", "-m", "engine.season.harness.no_such_module"]` exits
non-zero; (d) control: the shipped file exits 0. Written red against today's function for (a) to (c).
· **GATE:** `python -m pytest engine/season/tests/test_register_reading.py engine/season/tests/test_check_requirements.py -q`
green; `python -m engine.season.harness.register --requirements` prints nine lines in the new form and
exits 0; `python tools/m1_acceptance.py --summary` row 3 prints the held count.
· **Hash movers:** none. · **Depends on:** `01_CORE_requirements_reading_record` §1 and
`16_PESSIMIST_CORE_the_nine_gate…` edit 1 (both PROPOSED, B02; this item is the form they land in).
· **Lane:** IN. · **Batch:** B02, in the place of `01_CORE_requirements_reading_record`. · **Cost and tier:**
edit; `sonnet`, `high`. · **Lands it:** B02's producer, one commit.
· *Why this is not a new guard* (CLAUDE.md §0.1 pt 5): the register is the existing check of a file its own
header calls mechanism, and its count reaches `m1_acceptance`, the milestone reading Jordan decides on. The
edit changes the shape that check owns; it adds no tool and no second check.

**Item: IS-A-02 — the nine's conjuncts, authored from §2 to §10**
· **Advances:** all nine. · **INSTRUCTION:** write each row's `conjuncts:` from the tables of
`IS_A_NINE.md` §2 to §10: the conjuncts carried from `workplans/valoria_master_workplan_v11_part2.md` §2 to
§10 verbatim in `text`, the changed ones with the ruling in `text` (A-9, A-24, A-30, A-35, A-81, C3-K5), each
`[ASSUMPTION]` of §2, §4 and §10 copied into its conjunct's `text` with its revert. `holds` is `yes` only
where this batch's own run of the `argv` reads it; every other conjunct is `unread` or `no` with the last
recorded reading's tree. Readings to take in B02: R-01.a (`corpus_run`), R-01.b, R-02.a, R-01.c, R-02.b
(B02 builds them), R-03.a, R-03.b, R-04.b, R-06.d, R-06.e, R-07.a, R-08.b, R-08.c, R-09.a.
· **WHERE:** `engine/season/requirements.yaml` only. · **FALSIFIER:** a conjunct marked `yes` whose
`reading.tree` is not an ancestor of the commit that wrote it (visible in one `git log -p`); control: the
register's own refusals (`IS-A-01`).
· **GATE:** `register --requirements` prints, on B02's closing tree, R-01, R-02, R-03 at `met` with every
conjunct held, and the six others at the status their held counts give. **A held row that fails to read is
a STOP reported to Jordan, not an edit of the conjunct.**
· **Hash movers:** none. · **Depends on:** `IS-A-01`, `IS-A-03`, `IS-A-05` part 1 (this file);
`01_CORE_tests_shipped_world_falsifiers` rows 1–2 (PROPOSED, B02). · **Lane:** IN. · **Batch:** B02, last
item but one. · **Cost and tier:** edit plus about fifteen minutes of instrument time (`corpus_run` is
recorded at 2.5 and at 8 minutes by two lanes; not measured here); `sonnet`, `high`.

**Item: IS-A-03 — the removal test states what it expects**
· **Advances:** R-01.c, R-02.b. · **What exists:** `16_PESSIMIST_CORE_the_nine_gate…` edits 2–3 build
`removal_arm` and `--remove` and say the removed line *"is reported"*; no expected reading is stated, and
`<most-cited person>` is not defined.
· **INSTRUCTION** (added to that proposal's edit 2): `engine/season/harness/storybar.py`: (1) `--remove` with
no name takes the person who is the actor of the most `Event.causes` antecedents of other persons' acts in
the unperturbed copy's first season (ties by person id), and prints the name; (2) the report ends with two
verdict lines: `R-01.c  others' acts differing: <n>  (replay <0>)` and `R-02.b  differing at a later
(season, round): <m>`; (3) `--base-seed` accepts several seeds and prints one pair of lines per seed.
· **WHERE:** `harness/storybar.py`; `engine/season/tests/test_storybar.py` (EXISTS): NEW
`test_removal_changes_another_persons_later_act` (seed 0, two seasons: `n >= 1` and `m >= 1`; in the same
test the replay arm reads 0 and the removed person's own acts are excluded from `n`).
· **FALSIFIER and control:** the replay arm non-zero voids every figure (the proposal's own); second control:
remove a person at a round in which the unperturbed copy shows him forming no scene: `n` must be 0.
· **GATE:** `python -m engine.season.harness.storybar --remove --base-seed 0 1 2 --seasons 2`: replay 0 at each
seed; `n >= 1` and `m >= 1` at each seed. `[ASSUMPTION: above 0 with a control of exactly 0 is the right
form — basis: it is the form `01_CORE_tests_shipped_world_falsifiers` gives rows 1 and 2; the audit's seed-0
arms read 236 to 634 against 0 on the controls, a scratch comparison (that proposal's head).]`
· **Hash movers:** none (the chooser's draw is keyed on `(world_seed, tick, person, purpose)`,
`state/ids.py::draw_factory`, so a suppressed choice shifts no other person's stream). · **Depends on:**
the nine-gate proposal's edit 2 (PROPOSED, B02). · **Lane:** IN. · **Batch:** B02. · **Cost and tier:** edit;
`sonnet`, `high`; about two minutes an arm, six arms.

**Item: IS-A-04 — each scale of play names its command; the stale line about the scale words goes**
· **Advances:** R-04.c1 to c7. · **INSTRUCTION:** `engine/season/requirements.yaml`, `scales:` block (which
`01_CORE_requirements_reading_record` leaves untouched): (1) each of the seven rows gains `conjunct: R-04.cN`
and loses nothing; its `in_loop:` stays the tree's word until the conjunct reads; (2) the header comment's
sentence *"the loop's `person`/`realm`/`settlement` vocabulary is not canon's five, and no mapping between
them exists — that gap is R-04's real content"* is replaced by a pointer: the mapping is
`rosters.yaml: scale_of_rung` (`SCALE_OF_RUNG`, `data/rosters.py`), and what is open is a game reader of it
(`hole_register.yaml` H-89); (3) the first `scales:` row's note (*"`capability` is EMPTY on 429 of the 430
persons"*) is cut to the present fact, read by command at landing.
· **WHERE:** `engine/season/requirements.yaml`; `register.py::check_requirements` reads `scales[].conjunct`
and refuses one that names no conjunct of R-04 (three lines, in `IS-A-01`'s commit).
· **FALSIFIER:** a `scales:` row naming `R-04.c9`: the register must exit non-zero.
· **GATE:** `register --requirements` exit 0; `python -c "from engine.season.data.rosters import SCALE_OF_RUNG; print(len(SCALE_OF_RUNG))"`
prints 8 (the pointer's target exists; read 2026-11-12).
· **Hash movers:** none. · **Depends on:** `IS-A-01`. · **Lane:** IN. · **Batch:** B02. · **Cost and tier:**
edit; `sonnet`, `medium`. · **Closes:** `U4_TRACEABILITY.md` G-2 as stale.

**Item: IS-A-05 — two readings the nine lack: a choice that was not the top one, and a feeling that changes a choice**
· **Advances:** R-08.c (part 1), R-07.d (part 2). · **What exists:** `U4_TRACEABILITY.md` G-4 gives both in
outline; this item fixes the sites. **This item is the one owner** (Sonnet check, 2026-11-12): lane IS-B2's
`IS-B2-CORE-04` carried the same two tests at the same files and is now a pointer here; v12 keeps this item.
· **INSTRUCTION, part 1 (B02):** in `engine/season/tests/test_realm_requirements.py` (the file
`01_CORE_tests_shipped_world_falsifiers` creates), NEW
`test_r08_some_chosen_acts_were_not_the_top_candidate_and_none_at_zero_temperature`, seeds 0–2: play one
season through `harness/decision_spread.py::play_season` (EXISTS, `:448`; the chooser is watched, never
steered) at `DEFAULT_FIXTURES` and at `.sweep("choice_temperature", 0.0)`; assert the shipped arm's count of
deliberations in which the sampler's pick was not the leading candidate is above 0 and the zero arm's is 0.
`print_season` gains one line, `not the top candidate: <k> of <deliberations with a strict top>`.
`[UNVERIFIED: that `play_season`'s split carries the outvoted count per played deliberation under one key —
basis: the module docstring says the season's draw split scores each deliberation through `attribute_top`;
the executing session opens `:448-500` first.]`
· **INSTRUCTION, part 2 (B10, after `02_CHAR_scar_cap_and_regard_unit`):** the same file, NEW
`test_r07_a_planted_regard_changes_what_a_person_ranks_first`, seeds 0–2: build the realm; pick the first
person (by id) who holds a candidate about another person; write one stance row toward that subject through
the stance-row writer the regard-unit proposal names (never a monkeypatch); rank his candidates before and
after; assert the top candidate about that subject changes in at least one seed; control: the unplanted
world ranks equal twice.
· **WHERE:** `engine/season/tests/test_realm_requirements.py`; `harness/decision_spread.py::print_season`.
· **FALSIFIER:** part 1: pin `choice_temperature` to 0 in the shipped arm: the test must fail. Part 2: plant
the row toward a subject the person holds no candidate about: the ranking must be equal.
· **GATE:** `python -m pytest engine/season/tests/test_realm_requirements.py -q -k "r08 or r07"` green at the
batch that lands each part.
· **Hash movers:** none. · **Depends on:** part 1: `01_CORE_tests_shipped_world_falsifiers` (PROPOSED, B02);
part 2: `02_CHAR_scar_cap_and_regard_unit` (PROPOSED, B10). · **Lane:** IN. · **Batches:** B02 and B10.
· **Cost and tier:** small build; `sonnet`, `high`. · **Closes:** G-4.

**Item: IS-A-06 — the act-count instrument prints which verbs are built out, and through which seat**
· **Advances:** R-05.b, R-04.a, R-07.c. · **What exists:** `harness/aperture.py` prints, per verb, formed,
offered, attempted, executed, refused, `both` and `graded`; the row's own text says *"a verb's `ex` is not a
verb built out"*, and `Act.via` is not read by the instrument (`grep -n "\.via" engine/season/harness/aperture.py`
prints nothing). `CODEBASE_IMPROVEMENT_PROPOSAL_part2.md` CI-11 adds an `ENGINES` block beside it (B02).
· **INSTRUCTION** (`engine/season/harness/aperture.py`; after CI-11 in the same batch, one edit of `report`
and `pooled_report` for both):
1. `built_out(m) -> dict`: per verb of `VERB_TABLE`, over the acts of `corpus_run.attempts(w, n)` (EXISTS,
   `:817`) that are `made` and not `refused` (a clean execution, the instrument's `ex - both`): `clean` (the
   count); `kinds` (true where the Events caused by one such act include every kind of the row's
   `emits_at(degree)` for the band it folded, `data/verbs.py:363`); `wrote` (true where the row's
   `writes_at(degree)` is empty for every band the verb can fold, or at least one such Event carries a
   `Receipt` whose `delta` is not empty: before ≠ after); `via` (the count of clean executions whose
   `Act.via` is set). A verb is **built out** when `clean >= 1`, `kinds` and `wrote`.
2. `report` gains, after the per-verb lines, `BUILT OUT` with one line per verb (zeros included, sorted) and
   the total `built out <k> of <len(VERB_TABLE)>`; then one line `FOUGHT FIELDS  won+lost <a>  unopposed <b>
   stance receipts on the losing side <c>`, `c` counted over the `Person.stance` receipts of Events caused by
   a `march` act whose field Event is `field.won` or `field.lost`.
3. `pooled_report` prints, per verb, the number of seeds in which it is built out, and the pooled total.
· **WHERE:** `harness/aperture.py`; `engine/season/tests/test_aperture.py` (EXISTS): NEW
`test_built_out_counts_a_clean_execution_with_its_kinds_and_its_receipt` (one planted act through the fold
on the file's existing world: reads 1; the same act refused reads 0; a hand-built `Act` appended to the log
without the fold reads 0, which is the "a hand-built execution never counts" clause).
· **FALSIFIER and control:** the instrument's existing `CONTROL` line (the measured arm ends in
`populated.run`'s hash) shows the block moves no world; plant: drop the `Receipt` test from `wrote` and the
new test's refused arm must still read 0 while a write-less band now reads built out (it must not).
· **GATE:** `python -m engine.season.harness.aperture 1 --seeds 0 1 2`: `CONTROL` EQUAL at each seed; the
block prints 67 lines; at `6e1ea91` the `FOUGHT FIELDS` line reads `won+lost 0` at seed 0 and `1` at seed 2
(§0's probe). The built-out total is a reading, never a threshold, until the re-take that closes R-05.
· **Hash movers:** none. · **Depends on:** CI-11 (PROPOSED, B02; shared edit of `report`). · **Lane:** IN.
· **Batch:** B02. · **Cost and tier:** small build; `sonnet`, `high`.

**Item: IS-A-07 — the count of scenes that wrote nothing is read from B02 on**
· **Advances:** R-05.c (A-81). · **What exists:** `30_WR_E_cascade_chains_and_the_census` instruction 1
defines `null_scenes(w, n)` over `corpus_run.attempts` and lands it with an asserted zero in B38;
`U4_TRACEABILITY.md` G-11 proposes moving the function and a report-only line to B02. This item adopts G-11's
text and adds the site. **This item is the one owner of `null_scenes` in B02** (Sonnet check, 2026-11-12): lane
IS-B2's `IS-B2-CORE-03` carried the same function and file and is now a pointer that adds only the per-close
quotation and the scenario summary line; `harness/storybar.py`'s B02 order stays the nine-gate proposal, `IS-A-03`,
this item (the nine-gate proposal edits that file first, C3-K7).
· **INSTRUCTION:** land `null_scenes` where `30_WR_E` puts it (`harness/storybar.py`, behind the
`--null-scenes` flag that proposal names), report-only; `harness/aperture.py::report` prints after
`BUILT OUT` one block `NULL SCENES (acts whose Events carry no durable write)` by verb and by outcome class
(made, refused, graded loss), with the total. The definition of a durable write is `30_WR_D` §3's list, read
from `write_matrix.yaml`; the budget debit does not count (A-81). The asserted zero and clause C9 stay in B38.
· **WHERE:** `harness/storybar.py`, `harness/aperture.py`; `engine/season/tests/test_storybar.py`: NEW
`test_null_scenes_sees_a_planted_act_that_writes_nothing` (clause C9's planted control, moved forward).
· **FALSIFIER:** the planted act not counted. · **GATE:** `aperture 1 0` prints the block; the count at
`6e1ea91` is unread here and is recorded at B02's close as the baseline every later close quotes.
· **Hash movers:** none. · **Depends on:** `30_WR_D` §3's definition (PROPOSED, B38: the list is copied
forward in this commit and `30_WR_D` then points at it); `IS-A-06`. · **Lane:** IN. · **Batch:** B02.
· **Cost and tier:** edit; `sonnet`, `medium`. · **Closes:** G-11.
· **Serial edge:** `harness/storybar.py` is edited by one batch at a time (C3-K7): in B02 the order is the
nine-gate proposal, `IS-A-03`, then this.

**Item: IS-A-08 — no verb row lands dark**
· **Advances:** R-05.b. · **INSTRUCTION (a rule of v12 and a gate line, no code):** every batch whose items
add, split or re-draw a row of `verb_table.yaml` carries in its gate, for each such verb, the `BUILT OUT`
line of `aperture <seasons> --seeds 0 1 2` on its closing tree, at the season count its own proposal names
(two where it names none). The batches and their verbs are the verb map of `IS_A_NINE.md` §6, plus: B07
(every converted verb, beside 18-A's throughput reading), B25 (`tie`, `knot`: the table reads 68), B38
(`riot`, if `U5d_SE_cohort_heavy_moves_and_caste` lands its row: the table reads 69), and B35 (`weave`, `lock`, `mend`, `ward`: four rows `IS-B3-WR-01` adds if `STAGES.md` step 5 carries the thread card; `n` then rises by four more, and R-05's `built out n of n` is read at B35 with the new `n`). `[Sonnet check, 2026-11-12: lane IS-B3's four thread rows were not in this item's list.]` A verb that reads not
built out at its batch's close is a failed gate of that batch: the batch does not close on a named residue.
A row whose cells are owed content (`riot`) lands in the batch that has the content, not before.
· **WHERE:** v12's batch entries (the GATE of B07, B12, B21, B22, B23, B25, B26, B28, B29, B32, B35, B38).
· **FALSIFIER:** a batch close that quotes `ex` and not the `BUILT OUT` line for a verb it added.
· **GATE:** the quoted lines in each close. · **Hash movers:** none of its own. · **Depends on:** `IS-A-06`.
· **Lane:** each batch's own. · **Cost and tier:** one background run per batch
(`aperture 4 0` is recorded at about 25 minutes in R-04's row and at 4 m 25 s in R-09's CR-18 reading; not
measured here: size it on two small runs, STAGES practice 5); no model cost.
· **Conflict recorded:** v11 part 2 §6 says *"a verb whose exit recorded 0 stays a named residue; no
position is invented to fix it"*. This suite carries an edit for every one of the 34, so the residue rule has
nothing left to cover; if a carrier fails its gate the batch stops and reports, as any failed gate does.

**Item: IS-A-09 — a siege: `march` with the posture `besiege` (POINTER to `IS-MB-02`)**
· **Advances:** R-04.c4, R-05 (the `march` row's second posture), and the standing "no dead ends" charge.
· **Decided by the Sonnet check (2026-11-12, ladder step 4: one owner, and the complete item wins).** Lane IS-B1
carries this edit in full as `IS-MB-02` (`IS_B1_PC_MB_DICE_part2.md` §P2-1.2): its roster precondition read first
(`restore` executes on a garrison Site, `rosters.yaml` `march_postures` note), the A-81 repair of a siege that wears
nothing, the wear by `_fall`'s one owner, the `field_scene` table that decides whether the mover commit is made, and
three named tests. **This item's own INSTRUCTION, WHERE, FALSIFIER and GATE are withdrawn; v12 keeps one item.**
· **What this item still adds** (the requirement side only): (1) `IS-MB-02`'s gate line `march` with posture `besiege`
formed and executed is read through `IS-A-06`'s `BUILT OUT` block at B22's close (`aperture 2 --seeds 0 1 2`), and
`field.invested` is read in `EMITTED KINDS`; (2) the `march` row's built-out reading counts a besiege that wears
nothing but leaves its claim (`IS-MB-02` step 4) as a clean execution, not a refusal.
· **Read at the tree (2026-11-12), which settles this item's former assumption:** the wear is **not** drawn today.
`loop/effects_combat.py::_siege` (`:686`) takes each garrison Site's fall from `loop/effects_economy.py::_fall`
(`:141`), `(max(0, site.condition) * num) // den`, a fixed commons fraction with no draw, and returns `NO_CHANGE`
(so `march.refused`) when no Site would fall. Converting it is therefore not this item's to do and not B22's alone:
`IS-MB-02` step 5 stops and reports to the SE lane unless B12 has made `_fall` a draw.
· **Hash movers / Depends on / Lane / Batch / Cost / Lands it:** as `IS-MB-02` (mover, one re-pin at B22's last item;
MB; B22; `sonnet`, `opus` reads the table; B22's producer). **Closes:** G-1.

**Item: IS-A-10 — R-09's first conjunct follows the task draw**
· **Advances:** R-09.a, R-09.d. · **What exists:** `18_DETERMINISM_task_draw_for_uncontested_verbs` (B07)
makes an uncontested verb graded; `test_season_shape.py::test_we_only_a_verb_that_declares_contests_can_be_graded_today`
(`:15812`) asserts that only a verb declaring `contests:` can be, and is the test R-09's `met` text names.
The proposal's gate says to run `test_season_shape.py -k graded` *"for the renamed roster's readers"* and
does not name this test.
· **INSTRUCTION** (in the commit that lands the task-draw arm): (1) rewrite that test as
`test_a_verb_is_graded_by_a_contest_or_by_its_task_draw_and_by_nothing_else` (a bookkeeping row is graded by
neither; planted: a row in no class is refused at load, which is the proposal's gate 6); (2)
`requirements.yaml` R-09.a's `argv` becomes the `test_task_draw.py` file and R-09.d's reading is taken from
`test_converted_verb_resolves_in_at_least_two_bands` (the 90 % share, seeds 0–2, two seasons).
· **WHERE:** `engine/season/tests/test_season_shape.py`, `engine/season/requirements.yaml`.
· **FALSIFIER:** with `task_draw_arm: off` the rewritten test's task-draw half must fail and its contest
half pass. · **GATE:** `python -m pytest engine/season/tests/test_task_draw.py engine/season/tests/test_season_shape.py -q -k "task_draw or graded"`
green; `register --requirements` exit 0 (R-09.a's `-k` still selects a test).
· **Hash movers:** none of its own (the arm's are B07's). · **Depends on:** `18_DETERMINISM_task_draw…`
(PROPOSED, B07); `IS-A-01`. · **Lane:** IN. · **Batch:** B07. · **Cost and tier:** edit; `sonnet`, `high`.

**Item: IS-A-11 — the cast's authored values get a batch: `BA1-cast-content`**
· **Advances:** R-06.a, R-08.a, R-09.b (three rows wait on it and on nothing else once B10 has closed).
· **What exists:** `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` Batch U1-C (*"content and the switch"*)
names the files and the check; `U3_DEPENDENCY_ORDER.md` gives U1-A and U1-B the handles B04 and B05 and
gives U1-C none. `U4_TRACEABILITY.md` G-3 lists the owed values. The tree today: 46 cast rows in
`references/npc_registry.yaml`; one has a non-empty `stats:`; none has `capabilities:` (this lane's probe);
`cast_attributes=False` ships (`harness/populated.py:1016`).
· **INSTRUCTION, in two stages.**
*Stage 1, drafting (no code; may start at wave W0 beside the IN spine):* a content lane writes one
decision-ready file under the suite's `proposals/` with five tables, each row carrying its basis from the
registry (`role`, `faction`, `resonant_style`, `convictions`, `goals`, `notes`, `source`) or marked
`[NO BASIS IN THE TREE]`: (a) per cast person, the attributes (`stats:`) and the skills with their skill
scores (`capabilities:`), keys from the definition rows B04 lands; (b) per verb, `difficulty:` where it is
not `routine` (starting with `interrogate: demanding`, U1-C item 2); (c) the alignment cells of
`02_CHAR_choice_alignment` and the pursuit-signature cells of `16_PESSIMIST_CHAR_B`; (d) the six relation
rows of `02_CHAR_relations_have_a_ground`; (e) the signature rows and goals of `U5a_CHAR_owed_amendments`
§7 and §10. Jordan corrects the tables; merging the batch ratifies them unless the PR body holds one back
(ED-1094).
*Stage 2, landing (after B10):* 1. the five tables into their owners (`references/npc_registry.yaml`;
`engine/season/verb_table.yaml`; the alignment and signature rosters B10 creates; the relation rows; the
goal rows), each through its loader, which refuses an unknown key. 2. `harness/populated.py::build_realm`'s
`cast_attributes` default flips to on, in its own commit (U1-C's "the switch"). 3. Glossary rows edited in
the same commit for any key introduced (STAGES, the glossary rule), in A-98's words.
· **WHERE:** as named; `tools/export_npc_roster.py --check` and `tools/export_descriptors.py --check` re-run.
· **FALSIFIER and control:** authoring a `stats:` row moves no roll (U1-C's own); control: with
`cast_attributes` off the pre-batch hashes reproduce at seeds 0–2.
· **GATE:** `python -m engine.season.harness.decision_spread --persons`: the cast's pools differ;
`aperture 4 0` `POOLS ROLLED`: *two actors at different pools: yes* on a non-combat verb, beside the
all-default control; `corpus_run`: no verb under `RANKING EXCLUDES`, and the tie ordering shows no tie
between candidates of zero choice score for a person holding a vector; then the re-take of R-06, R-08 and
R-09 (`IS-A-13`).
· **Hash movers:** the build hash and every season hash; one re-pin, said plainly.
· **Depends on:** B04, B05, B10 (PROPOSED). **Blocking reason for stage 2:** the values are Jordan's or the
content pass's (`02_CHAR_choice_alignment:122`, `U5a_CHAR_owed_amendments:229`); owner: Jordan, on the
stage-1 draft. Not decidable from the repository beyond what each row's basis column cites.
· **Lane:** IN. · **Batch:** NEW `BA1-cast-content` (after B00, B01, B02, B04, B05, B10; gates nothing but
the three re-takes; one close). *Why its own batch:* its edit set is content files no B10 item edits, its
mover re-pins every realm, and its close is where three rows can move; merged into B10 it would hold B10's
close on Jordan's corrections. **One batch, two items (Sonnet check, 2026-11-12):** `IS-B2-CHAR-03` (lane IS-B2's
`B10c-cast-content`) is this batch under another handle; its handle is retired and its members are stage 2's tables.
Lane IS-B2 asked that B15, B19 and B24 follow it; that edge is **soft** (a calibration that closes first names the
control arm it ran at and is re-read once at this batch's close), because a hard edge would hold three lanes on
Jordan's corrections. · **Cost and tier:** content; drafting `opus`, `high` (authorship with
competing considerations, CLAUDE.md §10); landing `sonnet`, `medium`. · **Closes:** G-3 (as far as the nine
need it; the ages of A-15 are G-12, with B37; goal rows' `axis:` with B38).

**Item: IS-A-12 — the requirement line in every batch close**
· **Advances:** all nine (`U4_TRACEABILITY.md` G-5; STAGES step 6, items 1, 3 and 4).
· **INSTRUCTION (a form of v12, no code):** each v12 batch entry carries `REQUIREMENT: <conjunct ids> →
<expected holds>` taken from §12.2 below, or `REQUIREMENT: none — <reason or ruling>` (STAGES rule 5). Each
batch close records, in its commit body and nowhere else (CLAUDE.md §1: no count in a pointer index):
`register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the named conjuncts'
readings with their tree, and for a batch under `IS-A-08` the quoted `BUILT OUT` and `ENGINES` lines before
(the previous batch's after-reading, `reading @<sha>`, not re-taken) and after. The batch's last `Item:`
commit writes the readings into the conjuncts' `reading:` records; `status:` is not edited there.
· **WHERE:** v12's batch table and each batch's GATE; `engine/season/requirements.yaml` (`reading:` records
only). · **FALSIFIER:** a close that edits `status:` outside a re-take item, or a conjunct at `yes` whose
`reading.tree` is older than the last batch that named it. · **GATE:** `register --requirements` exit 0 at
each close. · **Hash movers:** none. · **Depends on:** `IS-A-01` (the `reading:` record exists; EXISTS only after
B02) and §12.2 (this file). · **Lane:** each batch's. · **Batch:** every batch, from B02's close on. · **Cost and
tier:** none beyond the readings.

**Item: IS-A-13 — the re-take: the one item that may move a row**
· **Advances:** the row named. · **INSTRUCTION (one item per milestone of §12.1, the last item of the batch
that closes it):** on the batch's closing tree, `PYTHONHASHSEED=0`: run every conjunct `argv` of the row (the
long ones launched in the background at batch open on the base and re-run only if `git diff <base>..HEAD`
touches what they reach); write each `reading:`; set `holds`; set `status:` to `met` only where every
conjunct holds, to `partial` where some do, and leave it where none moved. State in the commit body what
the readings do not show. Where a held row (R-01, R-02, R-03) fails a conjunct: stop, report, do not edit
the conjunct and do not re-pin a golden to pass it.
· **WHERE:** `engine/season/requirements.yaml`. · **FALSIFIER:** `IS-A-01`'s refusals; the batch critic
reads each `reading.line` against the run's saved output (v11 part 2's named gate, kept).
· **GATE:** `register --requirements` prints the row at its new status with every conjunct held;
`m1_acceptance --summary` row 3 moves by one. · **Hash movers:** none. · **Depends on:** `IS-A-01`,
`IS-A-06`. · **Lane:** IN (the row file is the permanent surface; one writer per wave, in merge order).
· **Cost and tier:** edit plus instrument time; `sonnet` runs, `opus` reads the readings against the
conjunct text (the judgment node that gates a requirement, CLAUDE.md §10).

---

## 12. Milestones and the requirement map

### 12.1 The milestones (dependencies fix the sequence; the rows fix the grouping)

A milestone is the set of batches whose last close lets one or more rows be re-taken. Handles are U3's; the
schedule step is U3 §2.3's (one open batch per lane), shown where it changes.

| milestone | closes when | batches | rows re-taken at its close | expected |
|---|---|---|---|---|
| **M0 · ground** | B04 closes | B00, B01, B02 (with CI-11 and `IS-A-01` to `-07`), B03, B03a, B13, B04 | R-01, R-02 (on the new instruments), R-03 | all three stay `met`; the other six print their held counts for the first time |
| **M1 · every outcome is drawn** | B08 closes | B05, B06, B07 (with `IS-A-10`), B08 | R-03 (with R-03.c); R-09.a, .c, .d, .e read | R-03 `met`; R-09 `partial` with four of five conjuncts held |
| **M2 · persons** | BA1 closes | B09, B10 (with `IS-A-05` part 2), BA1 | R-06, R-08, R-09; R-07 if R-07.c reads with its receipt | R-06, R-08, R-09 `met`; R-07 `met` or one conjunct short |
| **M3 · every verb** | the later of B32 and B35 | B11, B12, B14, B15, B21, B22 (with `IS-A-09`), B23, B25, B26, B28, B29, B32, B35 | R-05; R-07 if still open (B19 to B22 fight fields) | R-05 `met` |
| **M4 · every scale** | B36 closes | B16, B17, B19, B20, B24, B30, B34, B36 (and M3's B12, B21, B22, B23, B25, B32) | R-04 | R-04 `met`; `m1_acceptance` row 3 reads 9 of 9 |
| **M5 · the rulings beyond the nine** | B40 closes | B18, B27, B31, B33, B37, B38, B39, B40, B41 | none moves; R-05 re-read at B38 (`riot`), R-06.e at B39 (the generated cast), all nine at B40 | all nine hold |

*Batches that serve no row, named with their reason (STAGES rule 5).* B00 (ids), B03 (deletions), B03a (reading
cost of every later batch, H-03), B13 (personal combat as a package, H-08), B41 (the port's pins; CLAUDE.md
§6). M5's batches serve rulings, each named in its proposal's head: A-80 and A-81 (B38's census clauses C8,
C9), A-82 to A-91 (B38), A-44, A-50 to A-53 (B39), A-15, A-16, A-96 (B37), A-12, A-13, A-14 (B32, B33, B40),
A-69, A-78 (B31), the standing requirement that each subsystem plays alone (B18, B27, B40; lanes IS-B1 to
IS-B3).

### 12.2 The requirement map (batch → conjuncts its close must read → expected)

Only batches that name a conjunct. "re-read" is a held conjunct the batch's diff reaches.

| batch | lane | conjuncts read at close | expected reading |
|---|---|---|---|
| B01 | IN | R-04.c5 (i) | `aperture 2 s`, s = 0–2: `challenge` executed above 0 (lane A's 26 / 19 / 24 is a comparison, not a target) |
| B02 | IN | R-01.a, .b, .c; R-02.a, .b; R-03.a, .b; R-04.b; R-06.d, .e; R-07.a; R-08.b, .c; R-09.a | all `yes`; first `BUILT OUT`, `ENGINES`, `NULL SCENES` baselines (`ENGINES`: `combat.fight` above 0 at seed 0 if B01 did what its gate says; it reads 0 at `6e1ea91`) |
| B05 | IN | R-09.c; re-read R-08.b | a non-combat verb besides `tell` at two bands whose writes differ |
| B06 | IN | R-09.e; re-read R-01.b, R-02.a, R-03.a, R-08.b | `test_draw.py` green; same seed twice, same hash |
| B07 | IN | R-09.a (re-pointed), R-09.d; `BUILT OUT` for every converted verb | the 90 % share; no converted verb at zero successes |
| B08 | IN | R-03.c; re-read R-03.a, .b, R-01.b | five scene-sequence tests green; the one-interaction control equal |
| B09 | IN | re-read R-01.b, .c; R-02.a, .b; R-07.a | unchanged |
| B10 | IN | R-07.d; re-read R-06.c, .d; R-07.b; R-08.c | a planted regard changes a top candidate |
| BA1 | IN | R-06.a; R-08.a; R-09.b; re-read R-06.d, .e | no excluded verb; no tie at zero choice score; two actors at different pools |
| B11 | FI | R-04.c7; `covenant` formed | the shortest case and the inquiry tests green |
| B12 | SE+WR | R-04.c6; `BUILT OUT`: `restore`, `work`, `sabotage`, `exchange`, `requisition`, `found`, `build` | the valley runs; each built out |
| B19, B20 | MB | R-04.c4; R-04.c5 (ii), (iii); R-07.c | `won+lost` above 0 at seeds 0–2 with the stance receipt; the commanded field equals the automatic one with no decider |
| B21 | FA | R-04.a (`establish`, `confer`, `revoke`, `dispatch`, `issue`, `requisition`); R-04.c2; `BUILT OUT`: `confer`, `revoke`, `succeed` | each `via` at least 1; the spine closes |
| B22 | MB | R-04.c1 (`train`); `BUILT OUT`: `train`, `recruit`, `discharge_troops`, `form_unit`, `assign_troops`, `disband_unit`, `order_unit`, `raze`; `besiege` (`IS-MB-02`, read through `IS-A-09`); `ENGINES`: `mass_battle.army` and `mass_battle.army_order` above 0 | each built out |
| B23 | FA | `BUILT OUT`: `marshal`, `surrender`, `seize` | each built out; the land gate's arms a–i |
| B24 | SC | R-04.c3 | the hearing's hash twice equal |
| B25 | FI | R-04.a (`open_case`); `BUILT OUT`: `construe`, `interrogate`, `tie` | the table reads 68 by command |
| B26 | FI | `BUILT OUT`: `destroy_record`, `examine`, `seize` (a Record) | each built out |
| B28 | SC | `BUILT OUT`: `comply`, `evade / defy`, `forgive`, `covenant`; re-read R-03.a | each built out |
| B29 | PC | `BUILT OUT`: `arrest`, `accept` | each built out |
| B30 | MB | R-04.c5 (the grid) | `test_squad_field.py` green |
| B32 | FA | R-04.a (`determine`, `convene`); `BUILT OUT`: `determine`, `pardon` | each `via` at least 1 |
| B34 | GO | R-04.c1 (the sheet) | the creation-sheet test green |
| B35 | WR | `BUILT OUT`: `knot`, `thread_read` (and `weave`, `lock`, `mend`, `ward` if `IS-B3-WR-01` lands them); **R-05 re-take** | `built out n of n` |
| B36 | WR | R-04.c1 (the chronicle); **R-04 re-take** | the chronicle tells; nine of nine |
| B38 | WR | re-read R-05 (`riot`); `NULL SCENES` asserted 0 (C9) | n of n at 69, if the row lands |
| B39 | WR | re-read R-06.e, R-09.b on the generated cast | every acting person vectored; pools differ |

### 12.3 Where the requirement order asks for a different schedule (ties only; no dependency is crossed)

1. **`BA1` runs at step S11, the first step after B10**, in the IN lane, which U3 §2.3 leaves empty at S11
   and S12. Three rows can then be re-taken before any subsystem batch closes. Its drafting stage starts at
   W0 because Jordan's correction is the long pole and costs no engine time (STAGES practice 4: work whose
   value depends on a later batch is held to that batch; drafting is not).
2. **In the PC lane, B29 before B18** (U3 §2.3 has B18 at S13 and B29 at S14). B29 needs B15, B16 and B21,
   all closed by S12; B18 needs B14, B16, B17. B29 completes two verbs of R-05 (`arrest`, `accept`); B18 is
   content for the standalone duel. B31 (MB, S16) needs B18 and is not delayed.
3. **Among W11's seven batches, the ones that read a conjunct go first where a lane is contended:** B20, B25
   and B34 before B27 and B37. They are in five different lanes, so U3's S13 already runs them together;
   the rule only matters if the concurrency cap is below six.
4. **No conflict found between dependency order and requirement order**: every row's last batch lies on or
   before U3's W14, and the four waves after it (B38 to B40) serve rulings. If one appears when v12's
   author checks single-proposal files, dependency order wins and the serial-edge table records it.

### 12.4 Reading cost per close (for v12's runtime column)

Measured here: `register --requirements` 0.7 s; `m1_acceptance --summary` 21 s; build plus one realm season
7.0 to 7.4 s at seeds 0 and 2. Recorded by other lanes, not re-measured: a season's cost roughly doubles
each season (`CODEBASE_IMPROVEMENT_PROPOSAL_part2.md` §5 note 4); the removal test about two minutes an arm;
`corpus_run` 2.5 or 8 minutes; `aperture 4 0` 4.5 or 25 minutes. A close that names an R-04, R-05 or R-09
conjunct launches `aperture <seasons> --seeds 0 1 2` once, in the background, at its last item
(`[estimate]`: three seeds at four seasons, 15 to 75 minutes); every other close reads the two cheap
commands and its test files inside the one suite run.

## 13. Gaps closed, carried or left

| gap (`U4_TRACEABILITY.md` §6) | disposition here |
|---|---|
| G-1 (siege) | carried: `IS-MB-02` (B22; `IS-A-09` points at it) |
| G-2 (scale vocabulary) | **closed as stale**: `rosters.yaml: scale_of_rung` is the mapping; the comment is corrected by `IS-A-04`; the open part is H-89 (a reader), stage 5's |
| G-3 (authored content) | carried as a batch: `IS-A-11` (`BA1`); the values stay Jordan's |
| G-4 (R-07 and R-08 readings) | carried: `IS-A-05` (B02, B10) |
| G-5 (requirement map) | carried: §12.2 and `IS-A-12` |
| G-11 (no-null-scene reading before B38) | carried: `IS-A-07` (B02) |
| G-6, G-7, G-10, G-12 to G-16 | not this lane's subject (CHAR creation; domain actions; a skill's loss; the ages; construal; the reveal; zero coherence; the march's occasions): left to lanes IS-B1 to IS-B3, whose subjects they are. `[UNVERIFIED: whether each sibling carries its own; their files were being written during this run.]` |

Also carried, not in U4's list: the `met` texts' owner after v11 retires (`IS-A-01`, `IS-A-02`); the removal
test's expected reading (`IS-A-03`); a built-out reading (`IS-A-06`); R-09.a's test, which B07 would
otherwise leave asserting the opposite (`IS-A-10`); U1-C's missing batch handle (`IS-A-11`).

**Holistic items.** CI-11 (`ENGINES`) is used by §12.2 as written; `IS-A-06` shares its edit of
`aperture.report`. CI-01 to CI-10 move no row and are named in M0. H-12 (R-02's instrument under
`proposals/`) ends when `IS-A-02` retires the sweep's conjunct; deleting `proposals/2026-09-04-degree-sweep/`
and `engine/reference/degree-sweep/` is not proposed here (two tests import the sweep's arms,
`HOLISTIC_AUDIT_part2.md` H-09; stage 5 evaluates the tree).

**For Jordan.** Nothing from this lane overwrites canon, a `(RULED)` item or a Layer 1 row, so
`IS_FOR_JORDAN.md` gains no entry from it. Six changes to the `met` texts are taken on rulings and stay his
to correct, each with its revert at the place it is made: the sweep's conjunct retired (§2, §3); R-03.c
(§4); `revoke` read in computed play and commander-chosen orders restored (§5); the write-less clause of
"built out" replaced on A-81 (§6); R-09.b tightened and R-09.d, .e added (§10).

## 14. What was not checked

- No `pytest`, no `corpus_run`, no `aperture`, no removal test and no `wd_collect` was run: every `holds`
  above that is not from §0's two commands and two probes is the row's own recorded reading, with its tree.
- R-07.c's stance receipt at seed 2 was not traced to `_eff_march`; seed 1 was not run.
- `IS-A-06` names `Receipt.delta` from the class docstring (`state/carriers.py:209-225`), not from a read of
  the fold; `IS-A-05` part 1 and `IS-A-09` step 3 carry their own `[UNVERIFIED]` and `[ASSUMPTION]`.
- The verb map's carriers come from a count of mentions in `proposals/14_VERBS_*`; the proposals were read
  at their titles and `Lands in batch` lines, not in full. `15_INSTITUTIONS_*`, the dossiers other than
  `00_NINE`, the digests, `U2_LAYER1_CONFORMANCE.md`, `U3` §3 to §5 and the workplan parts other than
  `v11_part2` were not read.
- Workplan v11's positions named in the rows' `blocks:` lists (IN-, CR-, CP-T-, REM- ids) are stage 5's to
  disposition; this file reads only v11 part 2's `met` texts.
- (Stale after the Sonnet check of 2026-11-12, which read the siblings: the duplicate of `IS-A-09` and the second
  cast-content handle were found and resolved at the head of this part.) The sibling instruction files were not read; a duplicate of `IS-A-09` or of a new batch handle is
  possible.
