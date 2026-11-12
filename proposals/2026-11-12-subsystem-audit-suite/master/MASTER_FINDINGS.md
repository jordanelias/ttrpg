# The master findings — every finding of the 2026-11-12 session, its evidence, its disposition, the batch that fixes it, and who lands it

## Status: REFERENCE (the master suite of `STAGES.md` stage 6, lane MF; a terminal record of findings about artifacts that already exist; it orders no work of its own — the work is workplan v12's; resolves nothing at runtime, CLAUDE.md §0.05; not canon; dies with the suite)

## Read at: branch `ccr-62958c70-0kjhsw`, HEAD `30c978f`, working tree of 2026-11-12 (dirty only in other lanes' `master/workplan_v12/` parts). Producer: Opus, lane MF of `master/workplan_v12/V12_STRUCTURE_part3.md` §9. One round.

**What this is.** Jordan (2026-11-12): *"a comprehensive master suite with findings and recommendations"*. One place where each finding of the session stands with its evidence, its disposition, the recommendation that answers it, the v12 batch that lands it and the lane that owns it. It judges; v12 schedules. It does not retype an audit: every row cites the audit section and the closure row and carries one line.

**Parts (sequential, read in order).**

| part | holds |
|---|---|
| this file | §0 how to read and the counts · §1 the verdict on the game, per requirement and per subsystem, with the execution artifacts · §2 the game as a whole (holistic findings, the game pessimist, what the grounding pass refuted) · §3 the global top 40 |
| `_part2` | §4 the recommendations: the design directions the session settled · §5 what is not established, and what each gap blocks · §6 the Layer 1 amendments applied and still owed · §7 what workplan v11 and the gap register carried and what was retired · §8 what is not resolved · §9 the reading guide |
| `_part3` to `_part6` | §10 the findings by subsystem: for each, a synthesis of at most a page, then its rows (generated from the closure tables) |

**Paths.** A path with no directory prefix is under `proposals/2026-11-12-subsystem-audit-suite/`. `U5a`..`U5d` are `unified/U5_FINDINGS_CLOSURE_U5a.md`..`_U5d.md`; `U3` is `unified/U3_DEPENDENCY_ORDER.md`; `v12` is `master/workplan_v12/` (its batch list is `V12_STRUCTURE.md` §2); `the rulings` are `unified/DECISIONS_ANSWERED.md` (A-1 to A-114, then the ladder-closed D-rows).

**Words** (`unified/U1_GLOSSARY.md`; A-98; A-99 and `unified/MB_LEXICON_part3.md`; A-101). A person has **attributes** and **skills**; his number in a skill is his **skill score**; skill at arms is **martial skill**; health, wound count and the like are **derived scores**. The tree's identifier `capability` is the old name of a skill and is written only in code font. An army is made of **units**; where its subformations stand is its **army formation**, how one unit's men stand is its **unit formation**; no size word is used. A **lap** is one pass of the season's scene budget; a **round** is one engagement of a fight. A **batch** is one v12 handle with one close.

---

## 0. How to read this file, and the counts

**What a row carries** (`V12_STRUCTURE_part3.md` §9): the finding's own id, never re-numbered · the claim in one line (the closure table's) · its **severity** · its **subsystem** · the requirement rows it bears on · its **evidence** (the closure row, which quotes the audit's run or line, and the audit line that defines the finding) · its **disposition** · the **carrier** (the proposal or plan position that holds the edit) · the **v12 batch** · the **owner lane**.

**Severity** is the audit's own grade, read off the line that defines the finding (the suite's three grades, `AUDIT_BRIEF.md`; `audits/16_PESSIMIST_GAME.md:475`): **B** blocks a requirement · **D** degrades narrative · **H** hygiene; two audits use **C** (*code matter*, `01_CORE_audit.md`) and **M** (*design matter*) and they are kept. A row whose audit gives no grade (a resolution row, a hole-register row, a verb verdict, a case row, a census row, and about 80 findings whose defining line the extract could not parse) carries **—**: ungraded is not "minor".

**Requirement**: the R-rows the audit names on the finding's defining line, or in the closure row's claim or evidence. A blank cell means the audit named none, not that none is touched; the batch's own requirement reading is in v12 (`V12_STRUCTURE.md` §2.2, column *requirement*).

**v12 batch**: the batch that lands the carrier, read from `U3` §3.1's node table (every one of the 300 proposals is a row there) under v12's changes (`V12_STRUCTURE.md` §1–§2: B12 split into B12a, B12b, B12c, written `B12a-c` where the extract cannot tell which; B03d merged into B03, D-10; the GO entries of B03 moved to B03g, D-11); a carrier that is a v11 position (CR-, CP-T, H-, IN-…) is placed through `master/eval/V12_INTAKE.md`'s heading. A row closed SUPERSEDED or STALE/FALSE-POSITIVE that names a batch names the batch of its successor or of the file that showed it stale; it is not owed a fix of its own.

**Owner**: the lane of the first v12 batch named (`V12_STRUCTURE.md` §2.1); where no batch is named, the subsystem's lane (CORE, CHAR and DICE are IN).

**Order of rows inside a subsystem** (§10): severity (B, D, C, M, H, then ungraded), then the requirement row (R-01 first, none last), then the step at which the batch opens (`V12_STRUCTURE.md` §2.3), then the closure row. This puts the task's *worst first* ahead of §9's order (requirement, batch, id), which still governs inside a grade.

**The counts.** Printed by a scratch extract (not committed: lane MF edits only these files) that reads every row of every table in `U5a`..`U5d` whose header has a `disposition` column and whose cell holds one of the five codes; the four Jordan-answer and conflict tables, which have no such column, are not rows. **Control:** the extract's U5b counts equal U5b's own tally (`U5b` §5.4: PC 117 / 48 / 4, MB 104 / 39 / 3, MILITARY 23 / 9 / 0 / 1, PHYSICAL 32 / 8) row for row.

| scope | rows | RESOLVED-BY | SUPERSEDED | STALE/FP | DISPUTED | JORDAN | graded B / D / H+C+M | rows naming a v12 batch |
|---|---|---|---|---|---|---|---|---|
| CORE (with the test digests) | 238 | 169 | 39 | 26 | 0 | 4 | 9 / 9 / 15 | 158 |
| CHAR | 125 | 104 | 15 | 6 | 0 | 0 | 7 / 18 / 9 | 96 |
| PC | 169 | 117 | 48 | 4 | 0 | 0 | 4 / 8 / 11 | 146 |
| MB | 146 | 104 | 39 | 3 | 0 | 0 | 19 / 15 / 9 | 125 |
| SC | 154 | 135 | 14 | 3 | 2 | 0 | 6 / 19 / 7 | 151 |
| FI | 105 | 95 | 5 | 3 | 2 | 0 | 3 / 7 / 3 | 97 |
| FA | 118 | 97 | 16 | 4 | 0 | 1 | 6 / 15 / 6 | 99 |
| SE | 85 | 72 | 11 | 1 | 1 | 0 | 5 / 23 / 9 | 77 |
| WR | 83 | 71 | 9 | 3 | 0 | 0 | 3 / 22 / 10 | 68 |
| DICE | 77 | 49 | 24 | 3 | 0 | 1 | 4 / 15 / 13 | 50 |
| GO | 62 | 51 | 9 | 2 | 0 | 0 | 8 / 16 / 7 | 53 |
| the game (`16_PESSIMIST_GAME`) | 26 | 15 | 11 | 0 | 0 | 0 | 2 / 9 / 2 | 16 |
| verbs (the six families) | 139 | 116 | 21 | 0 | 2 | 0 | — | 122 |
| institutions | 41 | 23 | 17 | 0 | 1 | 0 | 1 / 0 / 0 | 20 |
| arcs | 29 | 20 | 9 | 0 | 0 | 0 | — | 20 |
| determinism | 34 | 21 | 11 | 1 | 1 | 0 | — | 13 |
| lacuna | 18 | 18 | 0 | 0 | 0 | 0 | — | 16 |
| narrative churn | 23 | 20 | 3 | 0 | 0 | 0 | 1 / 7 / 0 | 20 |
| procedural generation | 18 | 11 | 7 | 0 | 0 | 0 | — | 15 |
| happenings | 24 | 15 | 9 | 0 | 0 | 0 | — | 18 |
| story enablement | 32 | 23 | 8 | 0 | 0 | 1 | — | 24 |
| census | 80 | 41 | 26 | 13 | 0 | 0 | — | 56 |
| **all** | **1,826** | **1,387** | **351** | **72** | **9** | **7** | **78 / 183 / 101** | **1,460** |

Of the 1,387 RESOLVED-BY rows, 1,255 name a v12 batch; the other 132 name a carrier the extract could not place (a section of the closure table itself, a plan position the intake retired, "no edit owed", or an abbreviation the extract does not resolve) and are printed with **—** in the batch cell; their carrier cell says what they name. Every one of the 7 JORDAN rows has since been answered by a ruling (§8). Rows per closure file: U5a 545, U5b 388, U5c 343, U5d 550.

**Not in the closure tables, and carried here by hand:** the holistic audit's H-01 to H-13 (`master/HOLISTIC_AUDIT_part2.md` §4; their carriers are CI-01 to CI-11, §2.1 below); audits 24 to 31 (games grounding, engine grounding, mass-battle history, command, scene access, the one opposed rule, eras and regimes, house stances), which have no closure rows (`unified/U6_VERDICT_AND_REPAIRS.md`, "Not checked by the verdict"); their findings are carried by the proposals `26_*` to `31_*` and by rulings A-59 to A-114, and §10 gives each a synthesis with pointers instead of rows.

**Verification of the extract (one round).** Thirty rows were drawn at random (seed 20261112): 22 with a defining audit line, 8 without. For each, the audit line the extract named was opened and its claim compared with the closure row's, and the carrier proposal's `Lands in batch:` head line was compared with the batch the extract printed. All 22 claims match their audit lines and their grades; all 30 batches agree with the proposals' own head lines, with two kinds of imprecision the table keeps and states: a proposal that lands in two batches (`06_FA_war_lives_in_seats_B`: edits 1–3 in B21, the rest later) is printed at U3's node batch; a superseded proposal (`05_SC_evidence_and_rebuttal`: "Lands in batch: none (node B24 kept for the order)") still prints its node batch. Three sub-rows (`F-PC-08 (a)` to `(c)`) take the grade of their parent finding, as the audit writes them. **The sample found one extract defect, fixed before the tables were written:** a closure table defines short carrier names per section (U5a §2.8: `A`, `B`, `C` for the three CHAR pessimist proposals), and the first extract applied them file-wide, so `F-PES-CHAR-02` printed B07, B08, B15 for `16_PESSIMIST_CHAR_C_the_stop_is_the_mans` (B10). Single-letter names now apply only inside their own section and never in "Part B" or "A–D"; the eight rows of the sample without an audit line were re-drawn and re-read after the fix, and agree.

---

## 1. The verdict on the game as it stands

**In one sentence:** the season loop is a sound, seeded, replayable kernel whose three ruled requirements about propagation and ticking read `met`, but as computed play it is a world of paper — persons read clocks and each other's records and answer with more records, while the verbs that move the world's skeleton (kill, seat, unseat, build, raze, found, trade, starve, win a field) are refused or never formed, almost every outcome is a fixed function of state, and every person is the same fighter, arguer and worker; v12's 61 batches carry a recorded fix for 1,255 of the 1,387 findings closed RESOLVED-BY, and none of it has executed.

### 1.1 The execution artifacts that exist

Run by this lane at `30c978f`, `PYTHONHASHSEED=0` (two short runs; nothing else was run):

| command | printed | time |
|---|---|---|
| `python -m engine.season.harness.register --requirements` | `met 3 · not_met 1 · partial 5`: R-01, R-02, R-03 `met`; R-04, R-06, R-07, R-08, R-09 `partial`; R-05 `not_met`; `REQUIREMENTS: every row carries a measurement or names one` | 0.6 s |
| `python tools/m1_acceptance.py --summary` | `verdict: NOT MET`, `1 row(s) failing`: row 1 stub invocations `0 PASS` (seed 20260819, one season); row 2 same seed, same hash `bbf88d55e218… PASS`; row 3 the nine `3/9 FAIL`, `DOC-DERIVED`; row 4 `0` invariant violations over 24 seeds × 4 seasons + 2 populated × 1, `PASS` | 20 s |

These equal the readings of `master/instructions/IS_A_NINE.md` §0 (tree `6e1ea91`) and `master/HOLISTIC_AUDIT_part3.md` §9 rows 1–2 (tree `4dc8a7b`): the game did not move during the session (`audits/25_GROUNDING_ENGINE.md` §0: every suite commit touches the suite directory only). **Row 3 counts hand-edited `status:` strings and says so;** a `met` is a string behind which a command was run once (`IS_A_NINE.md` §0, "What kind of reading each row's `status:` is").

Execution artifacts other lanes made and recorded (scratch outputs, not committed; cited by the document that holds the reading): the holistic lane's reach probes (`HOLISTIC_AUDIT_part3.md` §9 rows 3–8: seed 0, one season, hash `5ab73af2…`, 13,379 Events, 749 resolved acts, 61 Events with a degree; seed 2, four seasons, hash `b4bae063…`, equal to `audits/25` L-18); IS-A's one-season probes at seeds 0 and 2 (`IS_A_NINE.md` §0: 83 persons, 2 with a skill, 0 with attributes; at seed 2 a fought field resolves in the first season); the game pessimist's acting-against-idle control at seeds 0–2 over three seasons (`audits/16_PESSIMIST_GAME.md` §0); implementation lane A's two unmerged commits measured at `aperture 2 s`, seeds 0–2 (`unified/OWED_TO_UNIFICATION.md` §E: `challenge` executed 0/0/0 → 26/19/24; obstacle still 2.0 in 998 of 1,106 rolls).

### 1.2 Per requirement

"Register" is the tree's `status:` today; "what a run shows" is the reading of a seeded run, with its source; "carried by" names the v12 batches whose close reads the row's conjuncts (`V12_STRUCTURE.md` §2.2 and §3) and the milestone at which every conjunct has a reading.

| row | register | what a run shows (source) | verdict of this file | carried by (v12) · milestone |
|---|---|---|---|---|
| **R-01** decisions propagate | met | seed 0, one season: 749 acts leave 13,379 Events, 12,115 of them `claim.deposited`; ledgers grow 236 → 12,351 claims (`HOLISTIC_AUDIT_part3.md` §7). Against an idle control, the acting realm ends with the same holders in all 34 seats and the same condition on all 322 sites (`16_PESSIMIST_GAME.md` §0) | **met on a channel that carries paper** (F-PES-GAME-12): propagation is real and almost all of it is records about records; the row's own measure is a committed log, not a re-runnable command (F-CORE-03) | B02 (the reading record, the knockout arm), re-read at B09, B10 · M0 |
| **R-02** decisions affect later decisions | met | not reproducible cheaply: the measure is a 36-cell sweep of about 75 minutes under `proposals/2026-09-04-degree-sweep/` (H-12); identical persons disagree in 70–74 % of readings (F-CHAR-02) | **inconclusive as measured**; the instrument lives in the unratified tree | B02, B10 · M0 |
| **R-03** seasons tick scene by scene | met | `headless --case NPC-088 --seasons 2 --seed 0`: five laps a season, hash `5405522c…` (`HOLISTIC_AUDIT_part3.md` §7) | **executes**; A-9 (a scene is a short sequence) changes what the row means | B02, B08 (A-9's scene order) · M1 |
| **R-04** decisions at differing scales | partial | the field resolver is entered at seed 0 only in the third season and at seed 2 in the first; the army record and `effects_army.py` are entered by no run (`HOLISTIC_AUDIT_part3.md` §7, H-01); 91 decrees in three seasons, none answered (F-FA-01) | **partial, narrower than the register's sentence** | B12a-c, B19, B20, B21, B22, B24, B30, B34, B36 · M4 |
| **R-05** all verbs built out | not met | one season at seed 0: 42 verbs attempted, 26 execute, 16 only refused (`audits/25` L-14); 34 of 67 execute in neither the corpus nor three seasons (`audits/17_CENSUS_REST.md` §0) | **not met; the largest obstacle** (H-01 is this row seen from the engines) | B07 (the task draw), then every verb family's batch · M3, re-read B38 |
| **R-06** characters robustly built | partial | at `build_realm(0)`: 83 persons, all with pursuits, 35 with a stance, 2 with a skill, 0 with attributes (`IS_A_NINE.md` §0; `audits/25` L-06, L-08) | **partial: people differ in what they pursue, not in what they can do** | B04, B10, BA1 (the cast's values) · M2 |
| **R-07** memory, feeling, relationship, imperfect knowledge | partial | the knowledge half executes and is separated by module path (`HOLISTIC_AUDIT_part3.md` §7); stance moved for 0 of 83 at two seeds (F-CHAR-03); a fought field at seed 2 adds two stance rows (`IS_A_NINE.md` §0) | **partial**: knowledge yes, feeling and relationship not observed to change a decision | B09, B10, B19–B20 · M2 |
| **R-08** not omniscient, not perfectly rational | partial | the chooser draws at `choice_temperature 0.05`; the departure from the optimum is one realm-wide draw, not the person's (F-CHAR-02) | **partial: the mechanism is present, its effect is not the person's** | B10 · M2 |
| **R-09** probabilistic chains | partial | 61 of 13,379 Events carry a degree (`HOLISTIC_AUDIT_part3.md` §7); 206 of 2,630 attempted acts (7.8 %) resolved by a draw at seed 0 over three seasons (`16_PESSIMIST_GAME.md` §0); 282 of 284 graded rolls change no state (F-PES-DICE-01) | **partial, and by execution near not met**: against the standing rule (A-24) | B05, B06, B07, B08; BA1 for R-09.b · M1, M2 |

**Across the nine.** The three rows read `met` are the three the season core, the chooser and the readers serve; the six that are not are served by the resolver engines and the cast's data, which is where every B-grade finding below sits. No row's `status:` moves before B99, the one re-take of the nine at the end of v12 (A-114; `V12_STRUCTURE.md` §3).

### 1.3 Per subsystem

Each line: the subsystem audit's verdict and the pessimist's (each `§0`), the strongest execution reading, and where v12 builds it. "Playable" is `unified/U4_TRACEABILITY.md` §3's mark (CARRIED: a proposal carries a scenario, one code path and the integration; PARTIAL: something is design-first or content).

| subsystem | the audits' verdict (one line each) | strongest reading | playable (U4 §3) | batches |
|---|---|---|---|---|
| **CORE** | a sound kernel (one clock, one write gate, one fold, one causal log, seeded and replayable) and not yet a basis for *judging* the game: the 143-case corpus runs one template (`01_CORE_audit.md` §0); a season ticks and a decision propagates, but a refusal does not teach (`16_PESSIMIST_CORE.md` §0) | `corpus_run` seed 0: `RUNS-UNDECLARED 103 · SPAN-UNAUTHORED 40`; 56 % of attempts refused, a refused act retried and failing 24 times in 25 | CARRIED as substrate | B02, B03, B08, B09, B34, B39 |
| **CHAR** | structurally sound, not behavioural: a person's ranking reads the verb and nothing about what the act would do (`02_CHAR_audit.md` §0); "a person is a seat, a ledger and a coin" (`16_PESSIMIST_CHAR.md` §0) | a man of `love` alone ranks `forge` first in 266 of 276 situations; identical persons disagree 70–74 % | PARTIAL (no CHAR scenario of its own; the cast's values are content) | B04, B09, B10, BA1, B39 |
| **PC** | a sound resolver and a clean module that computed play almost never reaches, and then every fighter is the same (`03_PC_audit.md` §0); a two-blow lottery between identical men (`16_PESSIMIST_PC.md` §0) | seed 0, two seasons: `challenge` 84 of 84 refused, `fight` formed 0; in 5,000 fights 70.0 % of deaths take exactly two blows | CARRIED | B01, B13, B14, B15, B16, B18, B29 |
| **MB** | a real, deterministic, well-instrumented simulator that never runs in natural play and at the shipped scale does not resolve a battle (`04_MB_audit.md` §0); an army divided into units loses to the same men in one block (`16_PESSIMIST_MB.md` §0); the history agrees with the skeleton and not the results (`26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md` §0) | the attacker loses 60 of 60 below a block; three units win 0 of 60 where one block wins 36; the side-wide multiplier decides 275 of 287 fields (`27_MB_COMMAND_AND_DYNAMIC_STRENGTH.md` §0) | CARRIED | B16L, B16M, B17, B19a, B19, B20, B22, B23, B30, B31 |
| **SC** | a sound resolution primitive and not a game: a hearing almost never ends, cannot be lost by the bench, is not moved by what is said (`05_SC_audit.md` §0); none of the five premise sentences holds (`16_PESSIMIST_SC.md` §0); no tuning dimension reaches the roll but two (`13_SC_contest_interrogation.md` §0) | 3 of 27 proceedings determined (seeds 0–1); the verdict deals 105 / 33 / 12 over 150 acts in all six cells of bench × case | PARTIAL (the hearing's moves design-first) | B05, B24, B24a, B27, B28 |
| **FI** | a sound information model and not yet a game: almost nothing a person knows reaches another by a person's act (`08_FI_audit.md` §0); the busiest engine informs nobody (`16_PESSIMIST_FI.md` §0); the detective game lacks a committed conclusion (`19_LACUNA_investigation_to_proceedings.md` §0) | 73.7 % of executed acts are information verbs; 93.9 % of 74,510 Events are ledger bookkeeping; 0–7 of 10,000–12,000 held claims arrived by telling | PARTIAL (which row forms a petition from a held conclusion) | B11, B25, B26 |
| **FA** | a sound skeleton without force or turnover (`06_FA_audit.md` §0); the realm runs the same with every office empty (`16_PESSIMIST_FA.md` §0) | 91 decrees, none held, obeyed or defied; cutting all 34 seat-holds moves the executed-verb vector by 263 where the dice alone move it by 240 | CARRIED | B21, B21b, B21c, B21d, B23, B32, B33, B40 |
| **SE** | a correct accounting kernel under a world that gives it nothing to account for (`07_SE_audit.md` §0); starving a third of the realm changes nothing anyone does (`16_PESSIMIST_SE.md` §0) | eleven of 37 towns starved by hand: no grain moved, no one left, no one learned of it | CARRIED | B11F1, B12a, B12b, B12c, B33, B38, B39 |
| **WR** | a sound causal substrate and not a source of narrative (`09_WR_audit.md` §0); clocks that keep time for nobody, with no turn (`16_PESSIMIST_WR.md` §0); no era, no regime beyond a credit factor (`30_ERAS_REGIMES_STRIFE_AND_MOMENTUM.md` §0); the stances land as data today (`31_HOUSE_STANCES_AND_CAST_VALUES.md` §0) | six seasons, seeds 0 and 1: no ending, one death; idle for 41 seasons the realm is one ramp in 37 identical places | PARTIAL | B12a-c, B35, B36, B37p, B38, B39 |
| **DICE** | the best-owned code in the tree, fed a constant: chance without character (`10_DICE_audit.md` §0); the dice decide almost nothing (`16_PESSIMIST_DICE.md` §0); one opposed rule serves fight and argument (`29_ONE_OPPOSED_RULE.md` §0) | 568 graded rolls, 564 at pool 2, leverage 0.0; 282 of 284 change no state | PARTIAL by nature (a substrate holds no scenario) | B04, B05, B06, B07 |
| **GO** | the oracle half of a port contract, one position in ten built, and that one holds (`11_GO_audit.md` §0); the port gate as planned would certify a game no player can read (`16_PESSIMIST_GO.md` §0) | the realm's hash identical under three `PYTHONHASHSEED` values and three CPython minors; the pinned slices enter combat 0/2/4 times | CARRIED for the oracle surface | B03g, B06, B34, B41 |

---

## 2. The game as a whole

### 2.1 The holistic findings (`master/HOLISTIC_AUDIT_part2.md` §4, worst first)

The holistic audit has no closure table; its carriers are CI-01 to CI-11 of `master/CODEBASE_IMPROVEMENT_PROPOSAL.md` (placed at its `:70-78`), every one hash-EQUAL. What holds (`HOLISTIC_AUDIT.md` §0): one write gate, one fold, one loader; 0 import edges from `engine/season` to `modules/`; every registered module reached by a composition row; same seed, same hash.

| id | claim (one line) | grade | evidence | carrier | v12 batch | owner |
|---|---|---|---|---|---|---|
| H-01 | the engines are reached unevenly and by seed: at seed 0 `modules/combat` (195 functions) is entered by no function in three seasons; six of sixteen composition rows entered in no run | B (R-05, R-04) | `HOLISTIC_AUDIT_part3.md` §9 rows 3–7 (`reach_mon.py 0 3`: combat 0, 0, 0) | CI-11 (an `ENGINES` reading on the act-count instrument); the fix itself is every verb batch | B02 (reading) | IN |
| H-02 | the game has no entry point of its own: the realm builder (982 lines) and the run loop live in `harness/` | D (R-04, R-05 delivery; the port) | `HOLISTIC_AUDIT_part2.md:39` | CI-06, CI-07 (A-102, the tenth module `engine/season/boot/`) | B03, B03c | IN |
| H-03 | more than half the source is prose; the two largest registries are about 70 % annotation | D (cost of every later batch) | 39,502 code lines of 81,908; `rosters.yaml` and `verb_table.yaml` 713 KB, about 500 KB notes | CI-01, CI-02 | B03a | IN |
| H-04 | the season's 101 tuning values have no typed export | D (CLAUDE.md §5; the port) | the parity file maps five constants | CI-04, CI-05 | B03 | IN |
| H-05 | one host site reaches a module attribute no composition row names | D (modularity) | `seam/wrappers/sigma.py:246`, 102 calls a season | CI-03 | B03 | IN |
| H-06 | the contest seam returns an untyped mapping for two engines | D (carried) | `queries/inputs.py:17-24`; `audits/25` V-01, V-02 | `03_PC_typed_outcome_one_door`, `04_MB_typed_outcome_and_one_path` | B14, B17 | PC, MB |
| H-07 | sixteen files carry the plan; the two most edited are the two largest registries | D (delivery) | `rosters.yaml` edited by 130 proposals | CI-01, CI-02 | B03a | IN |
| H-08 | personal combat is a flat set of top-level modules behind a path insert | H | `engine/substrate/pc_engine.py` seam | CI-09 | B13 | PC |
| H-09 | the driver's import list is defended by a frozen instrument that does not need it | H | 79 never-referenced imports of `loop/driver.py` | CI-08 | B03 | IN |
| H-10 | duplicated facts and dead code: mostly already carried | H | the census lanes (`audits/17_CENSUS_REST.md` §0) | CI-10 | B03 | IN |
| H-11 | the authored data has three roots | H | `data/files.py:98-130`, `:147`, `:158` | none (a placement note; `U1_OWNERS_AND_VOCABULARY.md` §4.6 decides a move) | — | IN |
| H-12 | a ruled requirement's instrument lives in the unratified-proposal tree | H | R-02's `measure:` under `proposals/2026-09-04-degree-sweep/` | `16_PESSIMIST_CORE_the_nine_gate_and_a_knockout_reading`; CI-08 | B02, B03 | IN |
| H-13 | `tools/` is half apparatus about the repository | H | 8 of 54 tools write an artifact the engine or the port opens | CI-10 only (CLAUDE.md §0.1 pt 5: nothing more earned) | B03 | IN |

### 2.2 The game pessimist (`audits/16_PESSIMIST_GAME.md` §0, findings at `:478-561`)

**The game, run with no player, is one working engine and six attachments; nothing persons do changes who lives, who rules, what stands or what is in the granary.** The single largest obstacle is outside every subsystem: the verbs that move the world's skeleton are refused or unformed, so every seam that would carry a consequence carries nothing. Its thirteen findings are rows of §10's "the game" block (U5d Part 6): two B (F-PES-GAME-01, -02), nine D (among them -04, the game is a fixed function of state; -07, the King's death does not travel; -10, a player-king who does nothing loses nothing), two H (-12, the three `met` rows are met on paper; -13, offices exist only where the cast seats them). The carrier of -01 and -02 is a reading (`16_PESSIMIST_GAME_consequence_reading`, B02), and the fix is the order of the carriers its "first ring" names — every verb batch from B07 on.

### 2.3 What the grounding passes settled

`audits/25_GROUNDING_ENGINE.md` (§6): **92 claims checked, 70 verified, 11 verified with a correction, 11 refuted**; 225 `[UNVERIFIED]` lines remain outside the institutions family, in nine groups (§5, U-01 to U-09). The refutations that change a proposal (§3):

- **G-01** — a graded-route verb row cannot carry degree-keyed writes: the loader refuses both forms (`engine/season/data/verbs.py:848-851`, `:872-876`), though the fold is ready (`loop/resolve.py:897`). Every verb band map in the suite rests on this; `18_DETERMINISM_task_draw_for_uncontested_verbs` now carries the loader edit (B07). It is also the substance of the two DISPUTED verb rows (§8).
- **G-08** — `mortal_terms` has no legal home in either place a proposal named (`queries/world_q.py:16-17`; `decision/budget.py:71`).
- **G-32** — `world_q.mustered` does not read `restrained` today (`queries/world_q.py:2132-2149`).
- **L-19** — "the King dies at tick 0 in every seed" is refuted at HEAD (`audits/22_HAPPENINGS.md` §0: alive after season 0 at seeds 0–2; he still dies by the one verb the repair missed).
- G-02 to G-06 and G-13: a proposal's hoped-for shape is absent and its stated fallback applies.

`audits/24_GROUNDING_GAMES.md` §0: 63 claim groups about other games; 33 already grounded by the suite's own citations, 6 grounded from the repository, 11 newly sourced and filed, 7 partly sourced, the rest to be marked.

`unified/U6_VERDICT_AND_REPAIRS.md` (the unification verdict): **yes, with listed repairs**; about 70 tree citations opened, all correct but those listed; no symbol fabricated; the batch graph has no cycle. Two summary claims were not bankable and were repaired: "246 COMPLETE" (re-run: 211 COMPLETE, 82 INCOMPLETE, 7 SUPERSEDED; 211 an upper bound) and "acyclic and every dependency exists" (re-checked inside each batch: 87 edges pointed forward and were moved or dispositioned).

---

## 3. The global top 40 (worst first)

Chosen by this lane, a judgment and marked as one: every B-grade finding that blocks one of the nine or the whole game is a candidate, ranked by (1) whether no subsystem can see it from inside (the game-level ones first), (2) how many of the nine it bears on, (3) whether a later fix stands on it (the earliest batch first). Two holistic findings (H-01, H-02) enter by hand. Rows that repeat one cause in two audits are kept as two rows, each with its own evidence, and marked "with" the other.

| # | id | claim | grade · R | evidence | disposition · carrier | v12 batch | owner |
|---|---|---|---|---|---|---|---|
| 1 | F-PES-GAME-01 | the world's skeleton does not respond to its people | B | `16_PESSIMIST_GAME.md:478`; X1 (acting against idle, seeds 0–2, three seasons) · `U5d:565` | RESOLVED-BY `16_PESSIMIST_GAME_consequence_reading` (the reading); the first ring of carriers | B02, then B07 on | IN |
| 2 | F-PES-GAME-02 | no consequence crosses a seam | B | `16_PESSIMIST_GAME.md:485`; §1.2 seam matrix · `U5d:566` | RESOLVED-BY the same | B02, then B07 on | IN |
| 3 | H-01 | the engines are reached unevenly and by seed | B · R-05, R-04 | `HOLISTIC_AUDIT_part2.md:10`; reach probes §9 rows 3–7 | CI-11 (the reading) | B02 | IN |
| 4 | F-PES-GAME-04 | in computed play the game is a fixed function of state | D · R-09 | `16_PESSIMIST_GAME.md:501`; 7.8 % of attempts drawn at seed 0 · `U5d:568` | RESOLVED-BY `18_DETERMINISM_*` and each verb lane's band rows | B05, B06, B07 | IN |
| 5 | F-DICE-01 | the dice engine is fed a constant: every social roll two dice, no leverage | B | `10_DICE_audit.md:139`; 568 graded rolls, 564 at pool 2 · `U5a:549` | RESOLVED-BY U1 §4–§6; `U5a_capability_home_and_two_inputs` Parts B, C | B04, B05 | IN |
| 6 | F-PES-DICE-01 | the degree changes no state in 282 of 284 graded rolls | B · R-09 | `16_PESSIMIST_DICE.md:423` · `U5a:633` | SUPERSEDED by the verb lanes' closures (the writes per band) | B07 on | IN |
| 7 | F-CORE-03 | the nine's statuses are strings; R-01 and R-02 `met` lack a control | B · R-01, R-02 | `01_CORE_audit.md:167`; `register.py:631-701` executes nothing · `U5a:64` | RESOLVED-BY `01_CORE_requirements_reading_record` §1 (as `IS-A-01`); `16_PESSIMIST_CORE_the_nine_gate_and_a_knockout_reading` | B02 | IN |
| 8 | F-PES-CORE-04 | the nine's gate accepts `met 9` on a module that does not exist | B | `16_PESSIMIST_CORE.md:475`; `req_forge.py` arms B–D exit 0 · `U5a:302` | RESOLVED-BY the knockout-reading proposal, edit 1 | B02 | IN |
| 9 | F-TEST-01 | no test asserts a requirement on a played world at the shipped configuration | B | `01_CORE_audit_addendum_C_tests.md:78`; WITNESS-cut probe 134 / 141 / 162 against 0 · `U5a:266` | RESOLVED-BY `01_CORE_tests_shipped_world_falsifiers` (T3 rows 1–3, 8) | B02, B10 | IN |
| 10 | F-PC-01 | computed play almost never reaches personal combat, and never by a duel | B · R-05, R-09 | `03_PC_audit.md:124`; `aperture 2 0`: `challenge` 84 of 84 refused · `U5b:67` | RESOLVED-BY `03_PC_duel_chain_reach` (lane A); `22_HAPPENINGS_C` (A-16); CR-91 (the war context) | B01, B07, B21b, B37 | PC |
| 11 | F-PC-02 | every person is the same fighter | B · R-06, R-09 | `03_PC_audit.md:150`; 83 of 83 default · `U5b:68` | RESOLVED-BY the skill home (U1 §1–§3; two inputs, A-7); `U5b_PC_rulings_in_the_fight` §2 | B04, B15, B18 | PC |
| 12 | F-PES-PC-01 | a fight is two blows | B · R-04, R-09 | `16_PESSIMIST_PC.md:650`; 70.0 % of 5,000 deaths in two blows · `U5b:216` | RESOLVED-BY `U5b_PC_rulings_in_the_fight` §4 (A-31's damage scale) and `29_DICE_one_opposed_rule_form_and_tuning` (A-79) | B05, B15 | PC |
| 13 | F-CHAR-01 | a person's ranking reads the verb and nothing about what the act would do | B · R-01 | `02_CHAR_audit.md:220`; 36 of 46 cast hold one top verb across six referents · `U5a:366` | RESOLVED-BY `02_CHAR_goal_lean_on_its_own_question` | B10 | IN |
| 14 | F-PES-CHAR-01 | the names on a character do not predict his acts (with F-CHAR-01) | B · R-01 | `16_PESSIMIST_CHAR.md:309`; `love` alone tops `forge` in 266 of 276 · `U5a:513` | RESOLVED-BY `16_PESSIMIST_CHAR_B` (signatures, cells, the loader's refusal) | B10, B11 | IN |
| 15 | F-CHAR-02 | the departure from the optimum is the realm's, not the person's | B · R-02, R-08 | `02_CHAR_audit.md:243`; identical persons disagree 70–74 % · `U5a:367` | RESOLVED-BY `02_CHAR_resolve_and_temper` with the test-retest gate | B10 | IN |
| 16 | F-CHAR-03 | the interior does not move | B · R-03, R-07 | `02_CHAR_audit.md:261`; stance moved for 0 of 83 at two seeds · `U5a:368` | RESOLVED-BY `02_CHAR_scar_cap_and_regard_unit`; `02_CHAR_relations_have_a_ground` | B10 | IN |
| 17 | F-PES-CHAR-03 | the only interior event is a fixed, inverted, silent conversion (with F-CHAR-03) | B · R-03 | `16_PESSIMIST_CHAR.md:346`; the same six convert at both seeds · `U5a:515` | RESOLVED-BY `16_PESSIMIST_CHAR_A` (the crisis of faith drawn, A-24) | B07, B10 | IN |
| 18 | F-PES-CHAR-02 | nothing stops a man; armed, the gate stops everyone | B · R-02 | `16_PESSIMIST_CHAR.md:333`; unarmed 0 of 46, armed 46 of 46 · `U5a:514` | RESOLVED-BY `16_PESSIMIST_CHAR_C` (the scruple a drawn tendency, A-24) | B07, B10 | IN |
| 19 | F-FA-01 | a decree binds nobody and reaches nobody as a writ | B · R-02, R-04 | `06_FA_audit.md:132`; 29 / 21 / 41 writs, 0 answered · `U5d:56` | RESOLVED-BY `06_FA_decree_binds` (A-21 proclaimed; A-22 command) | B21 | FA |
| 20 | F-FA-02 | power does not change hands in computed play | B · R-04 | `06_FA_audit.md:161`; `confer` attempted 0 · `U5d:57` | RESOLVED-BY `06_FA_seat_terms_and_turnover`, `14_VERBS_BINDING_C`; natural death (A-15) | B21, B37 | FA |
| 21 | F-PES-FA-01 | a vacant seat is filled by the Crown or by nobody | B · R-04, R-09 | `16_PESSIMIST_FA.md:492` · `U5d:180` | RESOLVED-BY `16_PESSIMIST_FA_B`; the deed race (A-19) | B21 | FA |
| 22 | F-SC-01 | a proceeding rarely closes; nothing said in it decides it | B · R-04, R-05 | `05_SC_audit.md:153`; 3 determined of 27 · `U5c:51` | RESOLVED-BY `05_SC_acquittal`, `05_SC_playable_hearing_B`, the evidence proposal, `U5c_SC_one_obstacle_form`; CR-57…CR-64 | B05, B24, B24a, B27 | SC |
| 23 | F-PES-SC-05 | the verdict reads nothing of the hearing (with F-SC-01) | B · R-02, R-05, R-09 | `16_PESSIMIST_SC.md:653`; one distribution in six cells · `U5c:203` | RESOLVED-BY the one obstacle form; evidence with admission; the acquittal; the hearing | B05, B24, B27 | SC |
| 24 | F-SC-07 | no decision inside a social contest | B | `05_SC_audit.md:235`; `sigma.py:459-460` · `U5c:57` | RESOLVED-BY `05_SC_playable_hearing_B` (six moves, one decider) | B24 | SC |
| 25 | F-FI-01 | a person's candidates move on a fact he has not witnessed or been told | B · R-07, R-08 | `08_FI_audit.md:151`; `r08_probe.py` with two controls · `U5c:240` | RESOLVED-BY `08_FI_01_claim-sourced-referents`; `16_PESSIMIST_FI_C` edit 4 | B11 | FI |
| 26 | F-FI-11 | the hand that did a killing cannot be passed on | B · R-01, R-05, R-07 | `08_FI_audit_addendum_B.md:110` · `U5c:310` | RESOLVED-BY `08_FI_06_testimony-names-a-hand` | B11 | FI |
| 27 | F-FI-03 | investigation resolves and does not play | B · R-05 | `08_FI_audit.md:240`; found deposits 0 / 0 / 0 · `U5c:242` | RESOLVED-BY `08_FI_07_shortest-playable-case`, `08_FI_03_playable-inquiry` | B11, B26 | FI |
| 28 | F-MB-01 | the shipped scale does not resolve a battle | B | `04_MB_audit.md:182`; the attacker loses 60 of 60 below a block · `U5b:285` | RESOLVED-BY `04_MB_headcount_grade_and_scale` (one scale owner) | B17, B19 | MB |
| 29 | F-PES-MB-01 | an army divided into units loses to the same men in one block | B | `16_PESSIMIST_MB.md:605`; 0 of 60 against 36 · `U5b:408` | RESOLVED-BY `16_PESSIMIST_MB_partition_and_the_pair_rule` (edit 4 by MBA-04; edits 1–3 SUPERSEDED by A-100) | B19 | MB |
| 30 | F-MB-03 | nothing in natural play reaches the battle engine; no choice surface is on | B | `04_MB_audit.md:229`; `field.won`, `field.lost` never emitted at `aperture 2 0` · `U5b:287` | RESOLVED-BY `04_MB_playable_field_scenario` §E; `14_VERBS_MILITARY_C`, `_D` | B07, B20, B22 | MB |
| 31 | F-SE-01 | every settlement is the same economic object | B | `07_SE_audit.md:245`; 8 of 37 settlements in no polygon · `U5d:212` | RESOLVED-BY `07_SE_ground_and_granaries` (endowment by territory) | B12a-c | SE |
| 32 | F-PES-SE-01 | a failing place changes nothing any person does | B | `16_PESSIMIST_SE.md:549`; eleven towns starve unseen · `U5d:291` | RESOLVED-BY `16_PESSIMIST_SE_A`; `U5d_SE_cohort_heavy_moves_and_caste` (A-56) | B12a-c, B38 | SE |
| 33 | F-SE-02 | population is a constant that can only fall, falls whole, and its loss is invisible | B | `07_SE_audit.md:261` · `U5d:213` | RESOLVED-BY `07_SE_population_census` §4 and its rising arm | B12a-c | SE |
| 34 | F-WR-01 | no story in the shipped realm escalates or ends | B · R-01 | `09_WR_audit.md:130`; six seasons, one strand of 234 moves · `U5d:330` | RESOLVED-BY `09_WR_story_instruments_that_can_fail` edit 4 (the reading); the closing acts are PC's, SC's, FA's | B36 | WR |
| 35 | F-PES-WR-01 | no story in computed play has a turn (with F-WR-01) | B · R-01 | `16_PESSIMIST_WR.md:445` · `U5d:409` | RESOLVED-BY `16_PESSIMIST_WR_D` edit 4 | B36 | WR |
| 36 | F-WR-05 | threadwork is not in the game and is not a module | B · R-05 | `09_WR_audit.md:276`; `(Person, coherence)` unproduced · `U5d:334` | RESOLVED-BY `09_WR_threadwork_module` edit 3; `09_WR_B_threadwork_session_and_practitioner` | B03, B35 | WR |
| 37 | F-CORE-05 | the play surface is a seam with no client | B | `01_CORE_audit.md:206`; no `input(` under `engine/season` · `U5a:66` | RESOLVED-BY `11_GO_player_surface_contract_B` §8 | B34 | GO |
| 38 | H-02 | the game has no entry point of its own | D | `HOLISTIC_AUDIT_part2.md:39` | CI-06, CI-07 (A-102) | B03, B03c | IN |
| 39 | F-GO-01 | the port's pinned slices barely enter the two largest modules | B (port validity) | `11_GO_audit.md:115`; combat entered 0 / 2 / 4 times · `U5d:441` | RESOLVED-BY `11_GO_port_gate_order_and_coverage` §3; `16_PESSIMIST_GO_surface_pins` | B41 | GO |
| 40 | F-PES-GO-01 | the parity contract cannot see the player's surface | B | `16_PESSIMIST_GO.md:542` · `U5d:498` | RESOLVED-BY `16_PESSIMIST_GO_surface_pins` | B41 | GO |

**Every one of the forty is a plan, not an edit**: the closure lanes resolved nothing against code (`U5a` head, "Resolve is a plan, not an edit"), and the first execution of any of them is the batch named.
