# Instruction suite, lane IS-A — the nine requirements (R-01 to R-09)

## Status: PROPOSED (stage 4 of `STAGES.md`; batch-shaped instructions for workplan v12; resolves nothing at runtime, CLAUDE.md §0.05; not canon; nothing here executes)

## Read at: branch `ccr-62958c70-0kjhsw`, HEAD `6e1ea91`, working tree of 2026-11-12 (dirty in `architecture/`, `references/id_reservations.yaml` and two ED ledgers: other lanes' work, not touched here). Producer: Fable, lane IS-A. Work order: `master/INSTRUCTION_SUITE_ORDER.md`.

**What this file is.** For each of the nine requirements of `engine/season/requirements.yaml`: the reading
today, what execution would make the row read `met` under CLAUDE.md §0.2, the sequence of batches that gets
there, and the items no existing proposal carries. Then the milestone grouping: how v12 groups the batches of
`unified/U3_DEPENDENCY_ORDER.md` into milestones by requirement. It does not restate a proposal's coding
instructions; an item that points at a proposal says so and adds only what is missing.

**Words.** `unified/U1_GLOSSARY.md`'s words are used. A *row* is one of R-01 to R-09. A *reading* is what an
instrument printed on a named tree. A *batch* is a handle `B00` to `B41` of `U3` (one close each); `IS-A-n`
is an item of this file; `BIS-n` is a batch this file creates. A *milestone* is a set of batches whose last
close moves a row (the ordinary sense: a stage reached; the tree's M1 is one such). The *act-count
instrument* is `harness/aperture.py`. `04` is `architecture/meta/04_CODE_ARCHITECTURE.md`.

**Parts.** This file: §0 the reading today, §1 what "met" has to mean, §2 to §10 one section per row.
`IS_A_NINE_part2.md`: §11 the items in full (item form), §12 the milestone grouping and the requirement map,
§13 gaps closed, §14 what was not checked.

---

## 0. The reading today (run by this lane, tree `6e1ea91`, `PYTHONHASHSEED=0`)

| command | printed | cost |
|---|---|---|
| `python -m engine.season.harness.register --requirements` | `met 3 · not_met 1 · partial 5`; R-01, R-02, R-03 `met`; R-05 `not_met`; R-04, R-06, R-07, R-08, R-09 `partial`; last line `REQUIREMENTS: every row carries a measurement or names one` | 0.7 s |
| `python tools/m1_acceptance.py --summary` | `verdict: NOT MET`, `1 row(s) failing`. Row 1 stub invocations `0 PASS` (seed 20260819, one season); row 2 same seed same hash `bbf88d55e218… PASS`; row 3 the nine `3/9 FAIL`, self-declared `DOC-DERIVED`; row 4 `0` invariant violations over 24 seeds × 4 seasons + 2 populated × 1, eight invariants, `PASS` | 21 s |

Both agree with the holistic audit's log (`master/HOLISTIC_AUDIT_part3.md` §9 rows 1 and 2, read at `4dc8a7b`):
nothing between the two trees moved either reading.

**What kind of reading each row's `status:` is.** The register checks one thing: that a row claiming `met`
carries a `measured:` line (`requirements.yaml:5-8`). It does not run a row's `measure:` command. So every
`status:` is a hand-edited string behind which a command was run once on a named tree; `m1_acceptance` row 3
counts those strings and says so. Two of the three `met` rows rest on a run nobody can repeat cheaply (R-02:
36 chunk cells, about 75 minutes, by a script under `proposals/`), and four rows share one eight-minute
command (`corpus_run`) whose printed line the row then interprets by prose. This is the first thing §1 fixes.

**This lane's own probe** (scratch, not committed; `populated.build_realm(s)` then `populated.run(1, s, w=w)`,
the shipped builder and chooser, one season):

| seed | content hash | Events | folded acts | Events with a degree | field Events | persons with `capability` / `attributes` / `pursuits` / `stance` (of 83) |
|---|---|---|---|---|---|---|
| 0 | `5ab73af282d0779646c38839fbab85d8` | 13,379 | 749 | 61 | `field.unopposed` 3 | 2 / 0 / 83 / 35 |
| 2 | `a21ab6e12e356ccc4261bec1c93ca3b4` | 11,208 | 751 | 51 | `field.lost` 1, `field.unopposed` 2 | 2 / 0 / 83 / 37 |

Control that the run happened: the seed-0 hash, Event count, act count and degree count equal the holistic
audit's (`HOLISTIC_AUDIT.md` §3; `_part3` §9 row 8), so the game is unchanged between `4dc8a7b` and `6e1ea91`.
One thing in it is new to the register: **a fought field resolves in computed play at seed 2 in the first
season** (`field.lost`, degree `Lost`, five `body` receipts on the Event; persons carrying a stance row rise
from 35 at build to 37). R-07's last recorded reading of that conjunct is `0 / 0 / 0` (`requirements.yaml`,
the REM-27 paragraph of 2026-10-30), so the row's text is stale in the favourable direction (§8). Not traced
here: whether the two new stance rows are `_eff_march`'s write.

Also read from the tree: `len(VERB_TABLE)` is 67, 66 of them in `resolvable_verbs()` (`tie / knot` is the
one outside); eleven rows declare `contests:` (`accept`, `argue`, `arrest`, `capture`, `determine`, `fight`,
`interrogate`, `lie`, `march`, `speak`, `tell`); `engine/mc_v18.py` is absent and
`engine/season/tests/test_faction_q.py` exists.

---

## 1. What `met` has to mean, and where its text lives

**1.1 Where the text is today.** The definition of done for each row (its *`met` text*, a conjunction of
readings) is not in `requirements.yaml`. It is in `workplans/valoria_master_workplan_v11_part2.md` §2 to §10
(RATIFIED on merge, ED-1094), whose own Status line says the register *"validates for syntax only; it never
reads what a `measured:` line says"* and that the named gate is *"the batch critic's read of the line against
the printed figure"*. Adopting v12 retires v11 in the same commit (CLAUDE.md §2), and a retired plan's
content that the new plan still needs is carried forward. So the `met` texts need an owner before v12 is
adopted, and a workplan `.md` is the wrong one: the register is mechanism (`requirements.yaml:5-8`) and a
fact a program reads has its head in data (CLAUDE.md §0.05, the four clauses).

**1.2 The rule this file applies.** Three parts.

1. **A row's `met` text is a list of conjuncts in `requirements.yaml`**, each with the command that reads
   it, the line or test names expected, and the last reading (tree, seed, seasons, the printed line, the
   control, what it does not show). Item `IS-A-01` (§11). It composes on
   `proposals/01_CORE_requirements_reading_record.md` §1 (B02), which gives each row one `reading:`; seven of
   the nine `met` texts are conjunctions of two to five readings from different commands, so one reading per
   row cannot show them. The register refuses `status: met` unless every conjunct holds with a reading; it
   still executes nothing (a 25-minute instrument does not belong in a 0.7 s check).
2. **A conjunct is carried verbatim from v11 unless a ruling of this session changes it**, and each change
   below names the ruling (`unified/DECISIONS_ANSWERED.md` A-n) or the unification decision
   (`unified/U3_CONFLICT_LEDGER.md` C3-…). STAGES step 6: on a conflict, this session's content wins. Where
   v11 marked a conjunct `[ASSUMPTION; medium; Jordan to correct]` the mark is kept. No row statement is
   touched: the statements are Jordan's (ED-IN-0204).
3. **A row moves only at a re-take**: one item, the last of the batch that closes its milestone, runs every
   conjunct's command on that batch's closing tree, writes the readings, and edits `status:` only if the
   readings say so (§12, `IS-A-13`). No batch claims a row by landing (v11 part 2 §0, kept).

**1.3 Three kinds of row, and what each asks of v12.**

| kind | rows | what v12 owes it |
|---|---|---|
| **held** (reads `met` today; almost every batch moves the code under it) | R-01, R-02, R-03 | a cheap reading re-taken at each close whose diff reaches the row's code; a fall is a STOP, not a re-pin |
| **waits on a mechanism the suite already carries** | R-04, R-05, R-07, R-09 (its draw conjuncts) | the batch sequence in §5, §6, §8, §10, and the instrument lines that let a close show the conjunct (`IS-A-06`, `IS-A-07`) |
| **waits on authored values** | R-06, R-08, R-09 (its by-person conjunct) | a content batch with a handle (`BA1`, `IS-A-11`): `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` Batch U1-C has no handle in `U3` |

---

## 2. R-01 — "decisions must propagate" · register: `met`

**Reading.** Last re-take: tree `2ca90dce7`, 2026-10-30 (`requirements.yaml`, R-01's last paragraph):
`corpus_run` `check R3: 46 of 46 pass` (NPC), `97 of 97 pass` (ARC), planted control `False -> True`;
`wd_collect.py` at `2x3` 80.45 % / 64.38 % / 62.42 % against the 96 % bar. Not re-run here (eight minutes and
about 75 minutes). The holistic audit's seed-0 season shows the channel executing (ledgers 236 → 12,351
claims, 6,040 of them `told_by`; `HOLISTIC_AUDIT_part3.md` §7).

**Conjuncts.**

| id | conjunct | command and expected reading | source | holds | first read |
|---|---|---|---|---|---|
| R-01.a | the corpus cites cross-person causes | `python -m engine.season.harness.corpus_run`: `check R3: n of n pass` on both lanes, `not True: none`, control `R3 False -> True` | v11 part 2 §2, kept | yes at `2ca90dce7` | now |
| R-01.b | the played realm does too, on three seeds | `python -m pytest engine/season/tests/test_realm_requirements.py -q -k r01`: three seeds green; the witness-cut control reads 0 | `01_CORE_tests_shipped_world_falsifiers` rows 1 (B02) | unread (the file is MISSING, written in B02) | B02 |
| R-01.c | removing one person's choice changes other persons' acts | `python -m engine.season.harness.storybar --remove <person> --base-seed 0 --seasons 2`: replay line `0`; removed line above 0 | `16_PESSIMIST_CORE_the_nine_gate_and_a_knockout_reading` edits 2–3 (B02); **the expected reading is added by `IS-A-03`** (the proposal reports the line and states none) | unread | B02 |
| (retired) | reconvergence below 96 % at `2x3` | `wd_collect.py` after 36 chunk cells | v11 part 2 §2 | yes at `2ca90dce7` | — |

*The retired conjunct.* C3-K5 and C-U5a-01 decide one instrument per property and re-point `measure:` to the
removal test; the sweep sits under `proposals/` (`HOLISTIC_AUDIT_part2.md` H-12), costs 75 minutes, and its
own caveat stands on every reading (*"detected OVER THE BASELINE on ALL 4 plants: False"*). It leaves the
`met` text at B02 with its last reading kept in the file's history. `[ASSUMPTION: retiring the conjunct, not
only the `measure:` string, is what C3-K5 means — basis: a conjunct no session re-takes is not a reading.
Revert: keep it as R-01.d and R-02.c, re-taken once at milestone M2's close.]`

**Batch sequence.** B02 (the three instruments). Then held: B06 (the draw's key), B08 (scene order), B09
(a refusal remembered, claims fading as read), B10 (attention and choice) and B11 (rumour) each edit
`loop/witness.py`, `decision/` or `epistemic.py`; each such batch's close re-reads R-01.b (it is in the
suite run) and R-01.c (two minutes an arm).

**What holds it.** Nothing. **Risk:** R-01.c on a seed where the most-cited person's removed scene was a
refusal reads 0 for a reason that is not the row's; `IS-A-03` names the person by a stated rule and two
further seeds.

## 3. R-02 — "decisions affect subsequent decisions" · register: `met`

**Reading.** The same run as R-01's (`2ca90dce7`). Its `measure:` is the script under `proposals/`.

| id | conjunct | command and expected reading | source | holds | first read |
|---|---|---|---|---|---|
| R-02.a | withholding what acts observe changes later acts at the shipped budget | `pytest engine/season/tests/test_realm_requirements.py -q -k r02`: seeds 0–2 differ after a common prefix; the same seed twice is one sequence | `01_CORE_tests_shipped_world_falsifiers` row 2 (B02) | unread | B02 |
| R-02.b | a removed choice changes acts in a *later* round or season | the R-01.c command: at least one differing act at a `(season, round)` after the removed one | `IS-A-03` | unread | B02 |
| (retired) | reconvergence below 96 % | as R-01 | v11 part 2 §3 | yes at `2ca90dce7` | — |

**Batch sequence and risk.** As R-01. `test_wd_a_fork_changes_a_later_decision_at_the_shipped_default` is
renamed `…_at_two_slots` by the same B02 proposal (its row 3); the conjunct list does not name it.

## 4. R-03 — "seasons must tick scene-by-scene, so what occurs after one scene can impact the next scene" · register: `met`

**Reading.** `headless --case NPC-088 --seasons 2 --seed 0` runs five rounds a season (holistic probe 5, hash
`5405522c36b0399247f83fd9f6d29494`); `-k test_u2_` was not run here (no pytest).

| id | conjunct | command and expected reading | source | holds | first read |
|---|---|---|---|---|---|
| R-03.a | a deposit in one round changes a later round's candidates | `python -m pytest engine/season/tests -q -k test_u2_`: all pass, the one-round control among them | v11 part 2 §4, kept | yes (last read `444a00e1`) | now |
| R-03.b | a real case runs its rounds | `python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0`: exits 0, prints `rounds=` per season | v11 part 2 §4, kept | yes | now |
| R-03.c | inside one scene, a step can hang on the band of the step before | `python -m pytest engine/season/tests/test_scene_sequence.py -q` (five tests); control `interactions_per_scene = 1` reproduces the pre-edit hash | A-9; `16_PESSIMIST_CORE_a_scene_runs_in_its_own_order` edits 1–4 (B08) | unread (the file is written in B08) | B08 |

*Why R-03.c is added.* A-9 makes a turn a short sequence and re-keys the fold order to an order over scenes
(`04:662`, amended under A-97), so the thing the row statement calls a scene changes; the holistic audit
says the row's meaning moves (`_part3` §7). `[ASSUMPTION: the row needs the new conjunct to stay `met` after
B08 — basis: R-03.a and .b read rounds, not the scene A-9 defines. Revert: drop R-03.c; the row is then
unmoved by B08.]`

**Batch sequence.** B08. Held by every batch that edits `loop/driver.py` or `loop/deliberate.py` (v11's
constraint, kept): B06, B08, B09, B10, B28 (`28_CORE_scene_access_A`, an occupied counterparty, A-63) keep
`-k test_u2_` green in their covering run.

## 5. R-04 — "strategic and management actions must be possible, ie decisions at differing scales" · register: `partial`

**Reading.** Last readings in the row: `aperture 4 s` at trees `90d93384c` / `6831bea98` (2026-10-30):
`requisition` executes at every seed; `found` and `build` execute 0 at seeds 0 and 1; no `work` executes.
The holistic audit, two seeds: the army record's four composition rows and `loop/effects_army.py` are entered
by no run; `effects_founding.py` 1 of 9 functions (`HOLISTIC_AUDIT.md` §3). `aperture 4 0` was not run here
(about 25 minutes).

**Conjuncts** (v11 part 2 §5; three, the third one per `scales:` row).

| id | conjunct | command and expected reading | holds | carried by (batch) |
|---|---|---|---|---|
| R-04.a | every seat-gated remit verb executes at least once with `Act.via` set: `requisition`, `issue`, `open_case`, `determine`, `convene`, `dispatch`, `confer`, `establish`, `revoke` | `python -m engine.season.harness.aperture 4 0`: for each, the `BUILT OUT` block's `via` column at least 1 (`IS-A-06`; today the instrument prints attempted and executed and does not read `Act.via`) | no: `confer`, `determine`, `requisition` and `revoke` are among the 34 verbs that execute in neither instrument at `4995824` (`audits/17_CENSUS_REST.md` §6); `via` is unread for all nine | `establish`: `14_VERBS_BINDING_A` (B21) · `confer`, `revoke`: `14_VERBS_BINDING_C` (B21) · `dispatch`: `14_VERBS_BINDING_D` (B21; D4 waits, below) · `requisition`: `14_VERBS_MATERIAL_B` (B12), `06_FA_levy_through_the_seat_B` (B21) · `issue`: `06_FA_decree_binds` (B21) · `open_case`: `14_VERBS_SOCIAL2_C` (B25) · `determine`, `convene`: `14_VERBS_BINDING_B` (B32) |
| R-04.b | no second driver; the faction view is tested | `engine/mc_v18.py` absent; `pytest engine/season/tests/test_faction_q.py -q` green | file state yes; test not run here | — |
| R-04.c1 | character creation, development, chronicling is in the loop | a seated person is picked and his sheet shown (`11_GO_fidelity_and_campaign_modes` edit 1, `test_creation_sheet_shows_holdings_for_a_seat_holder`); `train` built out (`BUILT OUT` block); `python -m engine.season.harness.chronicle --seed 0` tells (`09_WR_B_chronicle_that_tells`, `test_in37_chronicle.py`) | no (`in_loop: false`) | B34 · B22 · B36 |
| R-04.c2 | grand strategy politics | `governance_spine play 0 8 --world realm`: exit `closed True` at seeds 0–2 (`06_FA_shortest_loop_B`) | no | B21; land on a won march B23 |
| R-04.c3 | social contests and debates | `python -m engine.season.harness.headless --world hearing`: the same content hash twice (`05_SC_playable_hearing_B`) | no ("seam unbuilt") | B24 |
| R-04.c4 | mass battles and strategy warfare | `field.won + field.lost` above 0 in computed play at `aperture 1 s`, s = 0–2, printed beside `field.unopposed`; `test_field_scene.py` (`04_MB_playable_field_scenario`) | partly: `field.lost` 1 at seed 2, 0 at seed 0 (§0 probe) | B19, B20, B22 |
| R-04.c5 | personal combat and grid combat with units | (i) a duel resolves in computed play at seeds 0–2 (`aperture 2 s`: `challenge` executed above 0, `03_PC_duel_chain_reach`); (ii) a fought field resolves on the cell battlefield (c4); (iii) commander-chosen orders (`27_MB_D`, `test_none_decider_equals_no_decider`); the grid of named persons (`04_MB_squad_grid_of_named_characters`, `test_squad_field.py`) | (i) in the realm at seed 2 only: no function of `modules/combat` is entered at seed 0 in three seasons (`HOLISTIC_AUDIT.md` §3; §0 probe: `challenge.refused` 48); (ii) seed 2 only; (iii) and the grid: no | B01 · B20 · B30 |
| R-04.c6 | settlement management, city building | `python -m engine.season.harness.valley` (`07_SE_valley_scenario`, `test_valley.py`); `found`, `build`, `work` built out at `aperture 4 0` | no | B12 |
| R-04.c7 | investigations | `test_shortest_case.py` and `test_playable_inquiry.py` (`08_FI_07`, `08_FI_03`) | no | B11; the hearing piece B24 |

*Changes against v11, each by a ruling.* (1) **`revoke` reads in computed play.** v11 read it on a hand-built
act by H-207 (A), with the revert *"a vacancy motive for a superior's `revoke` is designed"*. A-35 rules a
head strips an officer by a resistible draw and `14_VERBS_BINDING_C_turnover` carries the `revoke` draw
(B21): the revert's condition is met, so the hand-built reading ends. (2) **Commander-chosen orders join
c5.** v11 held them out as a named residue whose trigger was *"a position that designs a typed `Orders`
record shared by the PLAYABLE scene and the AUTOMATED planner"*; `04_MB_manager_battle_one_resolver`,
`26_MASS_BATTLE_maneuver_orders` and `27_MB_D` (B20) are that position, and A-1 makes the commanded and the
automatic battle one resolver. Its own revert (*"commander-chosen orders restored as a third gate"*) is
taken. (3) **Each `scales:` row gains a `command:` and a `reading:`** in the file (`IS-A-04`): v11's
conjunct (3) already asks that each row *"names a command that the batch ran"*, and the rows carry none.

*Not a conjunct, and why.* The `scales:` header says the loop's scale words have *"no mapping"* to canon's
five and calls that *"R-04's real content"*; `U4_TRACEABILITY.md` G-2 carries it as a gap that cannot be
written from the repository. **That is stale: the mapping is in the tree.** `engine/season/rosters.yaml:
scale_of_rung` (closed, `open: false`) maps the eight `rung_kinds` onto canon's five scales, `Object`
reached by nothing by design; `data/rosters.py:775-794` checks it total over `rung_kinds` at load;
`engine/season/tests/test_scale_of_rung.py` exists. What is true is narrower: no game reader consumes the
map or the verb table's `scale:` column (`hole_register.yaml` H-89, grade `absent`). G-2 is closed as stale
for the mapping; the header comment is corrected in `IS-A-04`; H-89 stays where it is (stage 5's row).

**Batch sequence.** B01 → B12 → B19 → B20 → B21 → B22 → B23 → B24 → B25 → B30 → B32 → B34 → B36.
**Earliest `met`: B36's close** (the chronicle is the last reading of c1), with B30 and B32 closed.

**What holds it.** (1) `dispatch` D4, the order that sends a person, has no carrier (`_eff_dispatch`, `U3`
§6.3); R-04.a does not need it (`dispatch` executes today, 86 attempted and 16 executed at `23bea9da`), so
it holds nothing here. (2) `06_FA_war_lives_in_seats_B` waits on v11's CP-T09-02 (stage 5). (3) The hearing's
rite and its unplayed decider are design-first (`05_SC_playable_hearing_B` edits 6 and 8). (4) Domain
actions: `U4` G-7 reads the contract row `domain_actions` as superseded by A-10; that is lane IS-B3's (SE).
(5) A siege (`march` with posture `besiege`) has no carrier: `IS-A-09`.

## 6. R-05 — "all verbs must be built out, and doing so requires planning out all the different scales of play required in a season" · register: `not_met`

**Reading.** `audits/17_CENSUS_REST.md` §6 (tree `4995824`): corpus 23 of 67 executed; realm, three seasons,
30; **33 of 67 execute in at least one, 34 in neither.** `audits/25_GROUNDING_ENGINE.md` L-14 as the holistic
audit quotes it: one season at seed 0, 42 attempted, 26 execute, 16 only refused. The row's own last
paragraph says 20 of 56 (2026-10-30) and is two table sizes behind. `corpus_run` was not re-run here.

**Conjuncts.**

| id | conjunct | command and expected reading | source |
|---|---|---|---|
| R-05.a | no verb row is without a predicate and effect, never attempted, or only refused | `python -m engine.season.harness.corpus_run`: `WHERE THE <n> GO: 0 have no predicate/effect · 0 foldable but never even attempted · 0 attempted and always refused`; **or** R-05.b for every verb in the last two classes | v11 part 2 §6, kept |
| R-05.b | every verb is built out in the realm | `python -m engine.season.harness.aperture 4 --seeds 0 1 2`: the `BUILT OUT` block reads `built out <n> of <n>`, n = `len(VERB_TABLE)` at measurement time (`IS-A-06`) | v11 part 2 §6 and REM-02's definition; the block is new |
| R-05.c | no built-out verb has a band that writes nothing | the same run: `NULL SCENES` reads 0 for every verb (`IS-A-07`) | **A-81** |

*"Built out"*, as v11 defines it `[ASSUMPTION; medium; Jordan to correct]`, kept: at least one act formed by
the chooser in a seeded run of a shipped builder is admitted, folds its band and emits the row's declared
kinds; where the band declares writes, a minted receipt has before ≠ after; a hand-built execution never
counts; the denominator is `len(VERB_TABLE)` and a row leaves the table only by a ruling. **One clause of it
is superseded:** *"a verb whose bands write nothing (`speak`, `interrogate`) is built out on execution"*.
A-81 rules that every scene writes a durable change whatever its outcome, so no verb's band may write
nothing; R-05.c replaces the clause. The denominator moves by ruling: 67 → 68 at B25 (A-28, `tie` and `knot`
split), and to 69 at B38 if `riot` lands (`U5d_SE_cohort_heavy_moves_and_caste`; its cells are Jordan's).

**The verb map** (the 34 that execute in neither instrument, by the batch whose close must show each built
out; carrier files found by this lane's count of backticked mentions over `proposals/14_VERBS_*`, each
proposal's own verb list is the authority).

| batch | verbs of the 34 it must show built out | carrier |
|---|---|---|
| B12 | `restore`, `work`, `sabotage` · `exchange`, `requisition` · `found`, `build` | `14_VERBS_MATERIAL_A` · `_B` · `_C` |
| B21 | `confer`, `revoke`, `succeed` | `14_VERBS_BINDING_C` (with `06_FA_seat_terms_and_turnover`, `22_HAPPENINGS_B`) |
| B22 | `train` · `recruit`, `discharge_troops` · `form_unit`, `assign_troops`, `disband_unit`, `order_unit` · `raze` | `14_VERBS_MILITARY_B` · `_C` · `_D` · `14_VERBS_PHYSICAL_B` |
| B23 | `marshal`, `surrender` · `seize` (a place) | `14_VERBS_BINDING_E` · `14_VERBS_MATERIAL_D` §6 |
| B25 | `construe`, `interrogate` · `tie` | `14_VERBS_SOCIAL2_B`, `_C` · `_D` |
| B26 | `destroy_record`, `seize` (a Record) · `examine` | `14_VERBS_MATERIAL_D` · `14_VERBS_PHYSICAL_C` |
| B28 | `comply`, `evade / defy` · `forgive` · `covenant` (formed in B11 by `14_VERBS_SOCIAL1_A`, obeyed here) | `14_VERBS_SOCIAL1_B` · `_D` |
| B29 | `arrest` · `accept` (with its challenge, B14's A4 and B28's "challenge spent") | `14_VERBS_PHYSICAL_A` A1–A2 |
| B32 | `determine`, `pardon` | `14_VERBS_BINDING_B` |
| B35 | `knot` (after the split) | `08_FI_08_knots-season-form` §1, §4 |

The 33 that execute today are not safe by that fact: B05, B06 and B07 re-draw every one of them, and the
task draw's throughput gate (`18_DETERMINISM_task_draw_for_uncontested_verbs` gate 5) is what stops a
converted verb from falling to zero successes. The `BUILT OUT` block is read at each of those closes too.

**Batch sequence.** B07 (every uncontested verb draws) → B10 (`02_CHAR_offer_what_can_be_done`: an act is
formed only where it can be done) → B11 → B12 → B14, B15 → B21 → B22 → B23 → B25 → B26 → B28 → B29 → B32 →
B35. **Earliest `met`: the later of B32's and B35's close**, re-read at B38 if `riot` joins the table.

**What holds it.** (1) The four army-order verbs and the muster: `14_VERBS_MILITARY_A` to `_D` are
INCOMPLETE (DESIGN): their obstacle terms are not members of the one obstacle roster and the membership is
U1's, not taken (`U4_DOCUMENT_STATUS.md` §3.4). (2) `interrogate` and `open_case` wait on v11's CR-61 through
`14_VERBS_SOCIAL2_C` (stage 5). (3) `knot` waits on the Thread lane's rows (B10-15 in v11; stage 5).
(4) v11's standing rule for a verb whose exit read 0 was *"a named residue; no position is invented"*; under
this suite every one of the 34 has a carrier, so a residue at a batch close is a failed gate of that batch,
not a carried name. (5) **A row landed dark raises n** (v11, kept): `IS-A-08` makes that a rule of every
batch that adds a verb row.

**The second clause** (*"planning out all the different scales of play"*) is the `scales:` roster, read
under R-04.c1 to c7.

## 7. R-06 — "characters must be robustly built with goals, ambitions, convictions, moral values, etc" · register: `partial`

**Reading.** The row's last paragraph (CR-17, 2026-11-05): `decision_spread --decisions`, seeds 0 / 1 / 2,
the strict top decides 54.4 / 59.6 / 54.8 % at τ = 0.05, every person carrying a pursuit vector. This lane's
probe (§0): 83 of 83 persons carry `pursuits`, 35 a stance row, 2 a `capability` entry, 0 `attributes`
(`cast_attributes=False` ships, `audits/25_GROUNDING_ENGINE.md` L-06, L-08). The holistic verdict: people
differ in what they pursue and hold, not in what they can do.

| id | conjunct | command and expected reading | holds | what moves it |
|---|---|---|---|---|
| R-06.a | every candidate offered carries a nonzero conviction term (no tie broken by the draw where a person has a reason) | `corpus_run`: the `RANKING DISCRIMINATION` line, with no verb under `RANKING EXCLUDES` | no (eight verbs excluded at the last reading; the alignment table is sparse) | the cells of `02_CHAR_choice_alignment` and `16_PESSIMIST_CHAR_B` (B10 the mechanism; **BA1 the values**) |
| R-06.b | the cast tests pass | `pytest engine/season/tests -q -k 'ambitions or cast'` | recorded, and by v11's own note blind (it saturated at 5 of 5 seeds in all 46 cases): it does not count | — |
| R-06.c | convictions spread decisions | `python -m engine.season.harness.conviction_spread` passes | not run for the last paragraphs | `16_PESSIMIST_CHAR_B` adds `harness.conviction_spread` readings (B10) |
| R-06.d | pursuit decides more than the draw | `decision_spread --decisions`, seeds 0–2: the strict-top share above one half at the shipped τ, beside the control τ `[ASSUMPTION: one half, H-96]` | yes at the CR-17 reading | re-read at B10 (`02_CHAR_resolve_and_temper` changes what the departure from the top is) |
| R-06.e | every acting person carries a pursuit vector | `decision_spread --persons`: n of n at the built realm | yes, 83 of 83 | re-read at B39, where A-44's generated cast (about 94 persons and kin) arrives |

*Changes against v11.* None in the text. Three rulings add characters' content without adding a conjunct:
A-34 (self-knowledge, a belief; `U5a_CHAR_self_knowledge_is_a_belief`, B10), A-82 to A-91 (the opinion axes
and the houses' cores; `31_WR_A`, B38) and A-7 (an attribute and a skill, two numbers), which is read under
R-09.b.

**Batch sequence.** B04 → B05 → B10 → **BA1** → (re-read) B38, B39. **Earliest `met`: BA1's close.**

**What holds it.** Authored values, not code: the alignment cells (`02_CHAR_choice_alignment:122`, *"the
cells are Jordan's"*), the pursuit-signature cells (`16_PESSIMIST_CHAR_B:114`), the six relation rows
(`02_CHAR_relations_have_a_ground:158`), the signature rows and goals of `U5a_CHAR_owed_amendments` §7 and
§10. `U4` G-3. `IS-A-11` gives them a batch and a way to be drafted for correction.

## 8. R-07 — "characters must have memories and feelings and attitudes and relationships, and they must only have imperfect knowledge" · register: `partial`

**Reading.** The row (v11 part 2 §8): conjunct 1 passes; conjunct 2 (two hearers, different regard) was met
at B-E; conjunct 3 (a fought field reaches `_eff_march`'s stance write) read `0 / 0 / 0` at REM-27. **This
lane's probe (§0) reads `field.lost` 1 at seed 2, one season**, so conjunct 3's count is no longer zero at
that seed; the stance receipt beside it was not traced. The holistic audit: the chooser's package imports no
`World` (five import edges into `state/`, all to `carriers.py`).

| id | conjunct | command and expected reading | holds | what moves it |
|---|---|---|---|---|
| R-07.a | the chooser is handed no world; two persons hold different things | `python -m pytest engine/season/tests -k 'choose_receives_no_world or a_view or r7_two_persons'` | yes by the row; not run here | held: B09, B10, B11 |
| R-07.b | two hearers with different claims about one subject read different regard after two realm seasons | v11 names no committed command (met at B-E on a test) `[UNVERIFIED: the test's name was not opened]` | yes by the row | `02_CHAR_scar_cap_and_regard_unit` (B10) changes the unit: re-read there |
| R-07.c | a fought field writes the losers' stance | `aperture 1 s`, s = 0–2: `field.won + field.lost` above 0, quoted with `_eff_march`'s `Person.stance` receipt on the losing side, `field.unopposed` printed beside `[ASSUMPTION; medium; Jordan to correct]` | count: 0 / not read / 1 at seeds 0 / 1 / 2; receipt unread | B01 (re-pins every realm), then B19, B20, B22; the read is `IS-A-06`'s block |
| R-07.d | a feeling, attitude or relationship changes a decision | `pytest engine/season/tests/test_realm_requirements.py -q -k r07`: a planted regard changes the top candidate at least once in seeds 0–2; the unplanted seed is equal | unread: *"no test by any name"* (`01_CORE_tests_shipped_world_falsifiers:36`) | **`IS-A-05`** (`U4` G-4 row 10), in B10 |

*Changes against v11.* R-07.d is added: the row statement names feelings, attitudes and relationships, and
no conjunct of v11 reads one of them changing anything (`U4_TRACEABILITY.md` §2, R-07, and G-4). Memory gains
two mechanisms without a new conjunct: forgetting computed when read (D-48; `01_CORE_claim_fade_as_read`,
B09) and a remembered refusal (A-81; `16_PESSIMIST_CORE_a_refusal_is_remembered`, B09).

**Batch sequence.** B09 → B10 (with `IS-A-05`) → B11 → the first of B19, B20, B22 whose close reads R-07.c
with its receipt. **Earliest `met`: B10's close**, if R-07.c reads with its receipt on that tree (it may
already; §0); otherwise B19's.

**What holds it.** `08_FI_02_rumour-that-travels` and `U5c_FI_residue` wait on v11's CR-29 (the reach map;
stage 5): they strengthen imperfect knowledge and hold no conjunct.

## 9. R-08 — "decisions must not be omniscient and perfectly rational — characters may not make the optimal decision based upon their epistemic knowledge and personal inclinations" · register: `partial`

**Reading.** The row (CR-17, 2026-11-05): at τ = 0.05 the sampler overrules the leading candidate in 223 /
196 / 220 of 498 readings; ties 4 / 5 / 5; *"no tie is broken by inclination, the table being sparse"*. The
holistic probe reads `choice_temperature = 0.05`.

| id | conjunct | command and expected reading | holds | what moves it |
|---|---|---|---|---|
| R-08.a | every tie among offered candidates is between candidates of equal, nonzero choice score | `corpus_run` (`RANKING DISCRIMINATION` and the tie ordering) and `decision_spread --decisions` | no (the same sparse table as R-06.a) | **BA1** (the cells) |
| R-08.b | the choice is sampling, and the argmax is its zero-temperature control | `pytest engine/season/tests -q -k test_u4_the_choice_is_sampling` | yes by the row | held: B06 (the draw's owner), B10 |
| R-08.c | in play, some chosen acts were not the top-ranked candidate | `python -m engine.season.harness.decision_spread --season --seed s`, s = 0–2: the share of resolved acts whose chosen candidate was not rank 1 is above 0 at the shipped setting and 0 at temperature 0 | unread: *"share of non-top choices in play is unread"* (`01_CORE_tests_shipped_world_falsifiers:37`) | **`IS-A-05`** (`U4` G-4 row 11), in B02 |

*Changes against v11.* R-08.c is added (G-4). `02_CHAR_resolve_and_temper` (B10) makes the departure from
the top the person's own (his temper) and `02_CHAR_what_an_act_risks` adds a risk term; both change R-08.c's
magnitude, so it is re-read at B10. A-43 (a person at zero coherence is unknowable to others) is carried by
`U5d_WR_zero_coherence_unknowable` (B35) and adds no conjunct: it concerns what others can predict of him.

**Batch sequence.** B02 (`IS-A-05`) → B06 → B10 → **BA1**. **Earliest `met`: BA1's close.**

## 10. R-09 — "chains of events within a scene are probabilistic, not deterministic" · register: `partial`

**Reading.** This lane's probe (§0): 61 of 13,379 Events carry a degree at seed 0, 51 of 11,208 at seed 2.
`audits/25_GROUNDING_ENGINE.md` L-15: 92.7 % of success Events at seed 0 carry none. The row (CR-18,
`8bdfb72ce`): *"NO TWO PERSONS SEPARATE, in the live arm or the control"*. The holistic verdict: by
execution closer to not met in the shipped realm.

| id | conjunct | command and expected reading | holds | what moves it |
|---|---|---|---|---|
| R-09.a | a verb that draws is graded | today `pytest -k test_we_only_a_verb_that_declares_contests_can_be_graded_today`; **from B07** `pytest engine/season/tests/test_task_draw.py -q` (six tests; `checked >= 10` verbs) | yes today | B07 retires the premise of the present test (an uncontested verb is graded by the task draw): `IS-A-10` re-points the conjunct in that batch |
| R-09.b | two persons resolve the same verb at different pools because they differ | `python -m engine.season.harness.aperture 4 0`: `POOLS ROLLED` prints *two actors at different pools: yes* on a non-combat verb, beside the control in which every person holds the default | no | B04 (the home), B05 (`U5a_capability_home_and_two_inputs` Part B: the roll with two inputs, A-6, A-7), **BA1** (the cast's attributes and skill scores; U1-C's check) |
| R-09.c | a non-combat verb besides `tell` resolves at two bands whose writes differ | `corpus_run`: `DEGREES RESOLVED BY VERB` | no at the last reading | B05, B07 (`13_SC_draw_for_unrolled_contests`, the task draw) |
| R-09.d | outcomes that could go either way are drawn | `test_task_draw.py::test_converted_verb_resolves_in_at_least_two_bands` (seeds 0–2, two seasons): for every converted verb with ten or more resolved acts at least two bands occur and none is 100 % one band; success Events carrying a degree at least 90 % of non-bookkeeping success Events | no (61 of 13,379 Events carry a degree, §0) | **A-24** and the standing rule; `18_DETERMINISM_task_draw_for_uncontested_verbs` gate 1 (B07) |
| R-09.e | the draw is one owner's, keyed | `pytest engine/tests/test_draw.py -q`; same seed twice, same hash | no (14 `random.Random(` constructions in 7 files, `HOLISTIC_AUDIT_part2.md` H-10) | A-30; `11_GO_one_draw_owner` (B06) |

*Changes against v11.* R-09.a is re-pointed (the test it names asserts the opposite of what B07 builds).
R-09.b returns from v11's looser reading (*"pools may differ by seeded history, not capability"*, marked
`[ASSUMPTION]`) to the `met` text's own (*"two persons with different `capability`"*): A-7 makes the roll
take an attribute and a skill score, so persons separate by what they are, and U1-C's check is that reading.
R-09.d and R-09.e are added on A-24 and A-30. `[ASSUMPTION: R-09.d and .e are conjuncts of the row and not
only gates of B06 and B07 — basis: the standing rule names R-09 (`AUDIT_BRIEF.md`, "touches R-09"); v11's
text would read `met` on one verb at two bands while nine in ten successes stay a fixed function of state.
Revert: drop them; the row can then read `met` at B07 plus BA1.]`

**Batch sequence.** B04 → B05 → B06 → B07 → B08 (a scene's second step hangs on the first's band: the chain
in the row's own words) → **BA1**. **Earliest `met`: BA1's close** (R-09.a, .c, .d, .e can read at B07's).

**What holds it.** The by-person conjunct is content (R-06's batch). The fight's and the field's calibrations
(B15, B19) and the hearing's (B24) re-draw their contests later; each re-reads R-09.c and .d for its verbs.

---

*Continued in `IS_A_NINE_part2.md`: §11 the items, §12 milestones and the requirement map, §13 gaps closed,
§14 what was not checked.*
