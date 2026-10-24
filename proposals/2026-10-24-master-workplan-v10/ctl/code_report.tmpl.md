# Code report — what the engine, the season loop and the subsystems do at HEAD, measured by running them (T00 · lane IN)
## Status: PROPOSED. Reference, not canon (`CLAUDE.md` §0.05). Merging this file ratifies nothing and moves no row of THE NINE: a row moves only on its own `measured:` block.
## Lane: IN (cross-cutting). Evidence for the v10 plan proposal that sits beside it (`2026-10-24-v10-00-head.md`). The figures in §4 to §11 are produced by scripts in `ctl/` and can be re-run from the tree; the line counts and the settlement count in §2 and the non-pytest gate rows in §3 were read off the console and are not saved there `[UNVERIFIED: not re-derivable from ctl/]`.
## Grade under `CLAUDE.md` §0.2: `paper` as a plan input; the figures themselves are `measured` at HEAD `b7a1e1b`, shallow clone, one container (see §12).
## Placement, and a conflict named. `CLAUDE.md` §0 bars audit documents that create work for a future session, with one exception: a terminal pass whose verdict is the thing asked for may sit beside its subject. Jordan asked for this report and for the plan it feeds (2026-10-24), so it records verdicts about artifacts that already exist and proposes no work itself; the work is the plan's. If the plan is not adopted, this file is reference and may stay or go on its own.

## 0. Verdict

**The engine is a deterministic, well-tested simulator of a lawful society, and it is not yet a game.** It runs: three pytest suites pass except three tests, the milestone's four-row gate passes three of four rows, and a season is byte-reproducible. What it does when it runs is mostly refuse. Over three seeds of four seasons, 67% of resolved acts end in a refusal event and no success (73.6% of all attempts once the refusals the instruments do not count, §5, are added), 16 of the 48 verbs that were attempted never once executed (a 17th, `march`, was declared 59 times and every declared march was then also refused: `march.declared` and `march.refused` both appear), and at seed 0 half of the people can neither tell nor argue because they know no one. The causal chains that make the engine look emergent (over the four storybar seeds, depth up to 15 and 30% of acts answering another person's act) are not mostly refusals, since half of the cross-person edges at seed 0 start from a success, but the deepest chain at seed 0 runs through nine refusals and three successes. There is no text layer; the only rendering is one line per act.

Ranked, worst first:

1. **Formation outruns feasibility.** The chooser forms acts the world cannot satisfy. {{T:wrong_referent_total}} of {{T:refusal_events_n}} refusal events ({{T:wrong_referent_pct}}) end on a read that finds no referent of the kind the verb needs: {{T:exists_zero_total}} are `exists:<Kind> = 0` ({{T:docket_empty}} of them `DocketItem`, an empty docket rather than a wrong kind) and {{T:condition_nonsite}} are `work` acts whose subject is not a Site. The count takes the 60 most frequent reads per seed, so it is a lower bound. A further {{T:wrote_nothing_total}} admitted acts changed nothing when their effect ran ({{T:capacity_total}} of them are migrations into a rung at capacity). (§6, §8)
2. **The instruments undercount.** {{T:invisible_n}} of {{T:admission_refusals_n}} admission refusals ({{T:invisible_pct}}) belong to contested acts that never enter `driver.resolved`, so `aperture` and `corpus_run.attribute` do not see them; they read "never attempted" for verbs that were attempted and refused hundreds of times. (§5, §6)
3. **Information does not circulate, and memory is a fixed window.** At build every person knows no one and holds no claim; after four seasons at seed 0 {{T:know_nobody_end}} of {{T:acq_persons_end}} still know no one, a person's own telling is rare (at most {{T:told_claims_max}} claims anywhere carry a `Claim.chain`, which only a spoken `tell` builds), and the ledgers fill to the 200-claim cap (all of them at seeds 0 and 2; at seed 1 the smallest holds 176). Of 236 `tell` attempts over three seeds, 54 won, 113 lost the contest and 69 were refused. (§10)
4. **Eight carrier fields end every run empty, and 62 of 146 declared Event kinds are never emitted.** Each empty field already has a reason on the record (four `Rung` containers that ratified Layer 1 declares and nothing maintains; `Record.ttl` with no reader or writer; `Person.capability` waiting on J-13's remainder; `Office.upkeep` read but declared by no office; `Claim.chain` empty at the end because only a spoken `tell` builds it and `tell` rarely wins), so none is a new defect; the never-emitted kinds are the larger signal. (§9)
5. **Stability, endings and the strategic scale do not reach play.** `stability` reads 0 at every office rung in every reading; no ending is reachable in computed play; the realm fights no field. These are already registered holes (H-224, H-176, H-175); this report only confirms them at the current HEAD. (§11)
6. **Three tests fail in this container.** Two are the known shallow-clone failures; one is a 1-unit-in-the-last-place drift in a combat pin that CI does not show. (§3)

## 1. Method, instruments and controls

All runs: `engine.season.harness.storybar.drive(seed, seasons, "off")`, which builds the full realm (`build_realm(seed)`, cast cap `None`) and drives the unmodified `SeasonDriver` with the shipped chooser. Seeds 0, 1 and 2, four seasons each. `PYTHONHASHSEED` was not set (the runs do not depend on it; the control below shows why that is a claim and not an assumption).

- **`ctl/failure_census.py`** wraps `SeasonDriver._admits` and `SeasonDriver._eligible` to record every admission decision (fold branch and contest branch of `resolve`), once per act: an admitted contested act is checked a second time inside `_fold`, and that repeat (529 over the three runs, `admission_rechecks` in the JSON) is counted apart, tallies the TRACE channel per season (WRITE refused, GAP, NOTE, DECISION, QUERY), attributes execution per act with `corpus_run.attribute`, and walks every carrier in the World for `None` and empty fields.
- **`ctl/static_inventory.py`** reads the tree without running a season: hole-register rows, last editorial-ledger rows, the v9 state index, verb-table properties against `EFFECTS` and `REQUIRES_PREDICATES`, null values in the YAML registries, and `skip`/`xfail` markers.
- **`ctl/acquaintance_probe.py`** and **`ctl/chain_outcomes_probe.py`** measure acquaintance and ledger fill by season and the outcome class on each end of every cross-person causal edge.
- **`ctl/build_report_tables.py`** renders the tables below from the JSON the scripts wrote; no number in a table was typed.

**Controls, each of which can fail.**

- *The instrument does not move the game.* {{T:control}}. A second control: the one-season seed-0 run under the same hooks has `World.content_hash()` {{T:control1}}.
- *Determinism.* The seed-0 event count (68,348) is identical in three independent runs made with three different scripts (`kinds_probe`, `failure_census` with hooks, and without); the resolved-act counts of the census (2,628, 2,620, 2,633 at seeds 0 to 2) equal the story-bar's `resolved=` counts for the same seeds; and two full story-bar runs (about twelve minutes each) print identical arm-1 pooled lines.
- *The eligibility hook fires.* In a one-season seed-0 probe `_eligible` was called 730 times and returned True 730 times (`ctl/elig_check.py`). No act failing `_eligible` at admission is therefore a measurement, not a dead hook: the person-side gate removes ineligible acts before they are formed. The 14 `act.ineligible` Events (4, 4 and 6 at seeds 0 to 2) come from the earlier `_survives` check (an actor removed by a predecessor act in the same fold, S27.1), which runs before `_admits` and so never reaches the hook (`loop/resolve.py:61-91`).
- *Each other claim in this report has the command that reproduces it in §13.*

{{T:seeds}}

## 2. What exists

| tree | lines of Python |
|---|---|
| `engine/season/` excluding tests | 44,589 (loop 8,525 · state 4,962 · queries 5,432 · decision 2,564 · harness 12,012) |
| `engine/season/tests/` | 55,030 |
| `engine/substrate/`, `engine/dice_engine/` | 504 and 673 |
| `modules/` (combat, mass battle, settlements, …) | 16,413 |
| `systems/` (oracle simulators) | 15,376 |
| `tests/valoria/` | 35,008 |
| Godot (`godot/skeleton/*.gd`) | 539, a skeleton that does not compile and extends a spine defined nowhere (`CLAUDE.md` §6) |

The verb table has 56 rows; 51 are in `resolvable_verbs()`; the five that are not are `construe`, `evade / defy`, `exchange`, `succeed`, `tie / knot`. The realm is 83 persons at build (31 seated; 52 unseated; 32 offices), 37 settlements, and, after one season at seed 0, 411 rungs, 322 sites, 87 propositions and 88 records. There is no player-facing client in this repository; `valoria-game` was not examined.

{{T:verb_static}}

## 3. Gates

| instrument | result |
|---|---|
| `pytest engine/tests -n auto` | 913 passed, 16 s |
| `pytest engine/season/tests -n auto` | 1,786 passed, 590 s |
| `pytest tests/valoria -n auto` | 1,960 passed, **3 failed**, 23 skipped, 15 xfailed, 291 s |
| `tools/freshness_gate.py` | 7 fresh, 0 stale |
| `tools/currency_consistency_check.py` | 8 heads newer than `CURRENT.md`'s stamp (2026-10-01); report-only |
| `tools/m1_acceptance.py --summary` | verdict NOT MET: stub invocations 0 PASS · same seed same hash PASS · nine requirements 3/9 FAIL (doc-derived) · 24 seeds × 4 seasons plus 2 populated × 1, 8 invariants, 0 violations PASS |
| `register --requirements` | met 3 (R-01 R-02 R-03) · partial 5 (R-04 R-06 R-07 R-08 R-09) · not_met 1 (R-05) |

The three failures. (a, b) `tests/valoria/test_forked_status.py::test_the_fork_rows_name_a_real_ref` and `::test_the_evacuated_content_is_actually_at_the_ref` fail because `.git/shallow` exists; `CLAUDE.md` §0.4 names them. (c) `tests/valoria/test_combat_lever_sign_safety.py::test_default_builds_are_byte_identical_at_both_lever_sites` fails on `bear_spear`: `bind_sigma(...).hex()` is `0x1.c57592d86e352p-1` against the pin `0x1.c57592d86e353p-1`, one unit in the last place. It reproduced when the file was re-run alone. CI's `Validator Unit Tests` job ran `pytest tests/valoria -q -n auto` green on `e605082` (run 40040180865), which is the commit before the last one (`b7a1e1b`, #503) and after #502, so the likely cause is a floating-point difference in this container (Python 3.13.17, glibc 2.39) and not a regression; the operation was not isolated. `[CONFIDENCE: medium]` `[UNVERIFIED: CI at b7a1e1b]`

Static `skip` and `xfail` marker lines, not runtime outcomes (the runs above had 23 skipped and 15 xfailed in `tests/valoria` and none skipped in `engine/season/tests`): {{T:markers}}. The reasons were not audited here.

## 4. The act funnel

An *act* is a person's chosen verb at a subject, resolved by the fold. *Executed* is read from the Event log through the verb row's own `emits:` kinds (`corpus_run.attribute`), *refused* through `emits_on_refusal:`; a graded `tell` loss and a `march` that declares and is refused at ENCOUNTER match both columns.

{{T:funnel_total}}. Over the three runs 48 of the 56 verbs were attempted and 32 executed at least once. Never attempted in 12 seed-seasons: `arrest`, `comply`, `construe`, `destroy_record`, `evade / defy`, `exchange`, `succeed`, `tie / knot`. (`march` is counted as executed in this paragraph because it declares; each of the 59 declared marches was then also refused, and `army.arrived` is never emitted.) Attempted and never executed: `argue`, `build`, `covenant`, `establish`, `examine`, `found`, `pardon`, `raze`, `requisition`, `restore`, `revoke`, `sabotage`, `seize`, `tend`, `train`, `work`.

{{T:funnel}}

The one-season, seed-0 aperture (`ctl/aperture_1_0_seed0.txt`) reads 539 acts attempted, 24 of 56 verbs executed once or more and 17 never attempted. The two readings differ for two reasons that matter: the horizon (a verb that needs a season of ledger first, such as `oblige` or `give`, is "never attempted" in one season and attempted in four), and the undercount of §6.

## 5. The instruments undercount contested refusals

A contested act (one whose row declares `contests:` or routes through a graded inquiry) is admitted or refused in the contest branch of `resolve`, which `continue`s before `_fold` runs. `_fold`'s first statement is the only place an act is appended to `driver.resolved`, and `driver.resolved` is what `aperture` and `corpus_run.attribute` iterate. A contested act refused at admission is therefore logged as an Event and absent from the funnel.

{{T:invisible}}

This is the defect REM-10 and REM-11 of the v9 remediation proposal describe (their scan found 984 refusal events in the realm against 761 counted by the aperture). It is reproduced here at the current HEAD, independently, with a different instrument. Per seed, refusal Events outnumber the funnel's refused acts by about a third (2,520 against 1,892 at seed 0).

## 6. Refusals

A refusal passes through up to four gates, in this order, and each leaves a different trace.

1. **Formation (person-side).** The act is never formed. Traces: NOTE rows. {{T:note_remit_total}} rows say a seat-gated verb "declines" because the person holds no seat granting it; that is the design. {{T:note_presence}} rows say `requisition` "declines rather than admitting" because its `presence:` eligibility cannot be evaluated person-side; it still formed 42 times over the three runs and was refused at admission every time. The largest block that is not design is {{T:note_nobody_total}} rows of "needs a `to` from a person they know, and they know nobody; NO Candidate is formed" (§10).
2. **Admission (the fold's `_admits`, §E2).** Eligibility, then `requires`, then the counterparty. Over the three runs:

{{T:admission}}

   There was no INELIGIBLE outcome at admission: the person-side gate removes every act the fold would find ineligible (the 14 `act.ineligible` Events come from `_survives`, §1). The two UNKNOWN classes are refusals by the fold's own polarity rule ("zero evidence goes to the verdict against the thing measured"): an operand the act does not carry, or a question the world cannot answer. The 523 UNKNOWN verdicts with no recorded read are `release` (228), `oblige` (158), `confer` (55), `dispatch` (25), `convene` (24), `revoke` (19) and `establish` (14), none of which can say why it refused.

{{T:admission_by_verb}}

3. **Effect.** The act was admitted, the effect ran, and it changed nothing: the gate raises `NoOpReceipt` and the fold emits the refusal. {{T:wrote_nothing_total}} such decisions:

{{T:wrote_nothing}}

   Of the {{T:wrote_nothing_total}}, `migrate` accounts for 1,242 and {{T:capacity_total}} of those are explicit "migration into a rung at capacity" decisions; `migrate` executed 8 times in 1,284 attempts (0.6%).
4. **Seam.** Contested acts that reach the seam can end `contest.undecided` (4 at seed 0) or in a graded loss; these are not refusals and are counted as outcomes.

**What the deciding read says.** The refusal Event carries the verdict's reads in `Event.observed`. The refusal-event total counts every kind a verb row lists under `emits_on_refusal`, which includes graded losses ({{T:graded_loss_n}}: the `both` class of `tell`, `research` and `surveil`), although item 4 above does not call those refusals. The last read recorded, pooled:

{{T:last_read}}

{{T:refusal_events}} `exists:<Kind> = 0` — the act was formed on a referent of the wrong kind, or on none — accounts for {{T:exists_zero_total}} refusal Events: {{T:exists_zero}} (a lower bound, since only the 60 most frequent reads per seed are kept; `DocketItem` counts dockets naming the subject, so 0 there means nothing is docketed). `condition = UNKNOWN` ({{T:condition_nonsite}}, all `work`) belongs to the same class. These are the failure classes REM-21 to REM-28 name; they are all still present at HEAD. None of the remediation's formation or instrument items has been built: REM-21's stamper registry (`STAMPERS`), REM-10's `attempts(w, n)` and REM-40's removal of the fold's `act.ineligible`/`act.refused`/`attempt.refused` literals are all absent from `engine/season/` (grep, this session); v9's B-Q to B-Y and B-T landed instead.

## 7. Read failures

- **UNKNOWN verdicts**: 1,089 of 9,780 admission decisions (11.1%), listed above. Of the 566 with a recorded read, `work` accounts for 483 (a `condition` read whose subject is not a Site: `WorldReader.read` returns UNKNOWN for `condition` only then, `queries/world_q.py:3129-3131`, and a Site's condition is a fixed-point integer, so these belong to the wrong-referent class of §0), `move` 68 (`contain.path`), `tell` 15 (`with`).
- **Unevaluable person-side**: `presence:` (3,322 rows; `requisition`). The *presence index* has no person-side reader by design (AX-2), so a verb whose eligibility needs presence declines at formation for the persons it cannot be checked for.
- **No candidate for want of a counterparty**: 5,276 rows (§10).
- **Unread causes**: the story-bar's `unread` counter, which counts Event causes that resolve to neither an Event nor `ROOT`, read 0 in every run.
- **Reads over three seeds × four seasons**: the TRACE channel logged {{T:q_home}} `home_of` and {{T:q_presence}} `presence` reads over the three runs, against {{T:q_questions}} `questions_for`. This is cost, not failure, and is recorded because the soak grades only per-season wall clock.

## 8. Write failures

The gate admits or refuses each write; TRACE records both. Of {{T:write_rows_seed0}} WRITE rows at seed 0, {{T:write_refused_seed0}} were refused (all of write class ACTS); pooled over the three runs:

{{T:write_refused}}

{{T:gap}}

Every refused write is a no-op or a write that "named no subject": the effect computed a delta over nothing. The totals reconcile with the DECISION channel's "wrote nothing" rows in §6, which is a cross-check between two separate TRACE channels: `(Person, travel_leg)` 1,384 = `migrate` 1,242 + `move` 142; `(Rung, stores)` 207 = `transfer` 207; `(Rung, exists)` 98 = `raze` 98; `(Person, capability)` 64 = `train` 64; `(Person, body)` 42 = `tend` 42; `(Tenure, until)` 14 = `open_case` 14; `(Record, exists)` 281 against `forge` 142 + `survey` 124 = 266 (the other 15 were not attributed). REM-28 and REM-2A name the same classes.

{{T:write_classes}}

## 9. NULL content

*Never populated.* The following fields are `None` or empty on every instance at the end of the seed-0 run (the footnote under the table says how many were so in all three seeds):

{{T:never_populated}}

Each was checked against the code for a writer and a reader before being called anything (grep over `engine/season/` excluding tests):

- `Rung.sites`, `.records`, `.dates`, `.envelope`: declared by ratified `04 §B.3` and kept on purpose although nothing maintains them (`state/carriers.py:1066-1083`; `loop/matter.py` calls `sites` "a back-reference nothing maintains"). A documented ID-13 exception, not a defect found here.
- `Record.ttl`: no reader and no writer (`loop/effects_information.py:1054`); this is H-169's "`Record.ttl` has no reader in `loop/`".
- `Office.upkeep`: has a reader (`queries/world_q.py:2120-2140`), and no office in `offices.yaml` declares one; CP-T08-08 of the #501 proposals is about this.
- `Person.capability`: has writers (`_eff_train`, cast overlays) and a reader (`seam/wrappers/sigma.py::_pool_of`); it is empty on all realm persons because no cast row authors one: J-13's remainder. `train` cannot execute while it is empty: `_eff_train` mints no key and returns `NO_CHANGE` unless the subject already holds the vocation (`loop/effects_combat.py`), which is the 64 refused `(Person, capability)` writes of §8.
- `Claim.chain`: written only where a person's `tell` builds a told claim from a held one (`loop/witness.py:963-966`); 0, 0, 4, 0 at the four season ends (§10).

The finding is therefore not that fields are dead: three of the eight (`Office.upkeep`, `Person.capability`, `Claim.chain`) stay empty for lack of *content*, which a plan can supply; `Record.ttl` lacks a *mechanism* (no reader, no writer); and the four Rung containers stay empty by ruling.

*Mostly empty.*

{{T:high_null}}

{{T:event_fields}} `Event.degree` is set only on graded contests, which is by design; `Event.observed` is empty on 96% of Events because only refusals and graded acts carry reads.

*Declared and never emitted.* {{T:never_emitted}}. {{T:undeclared}}.

*Registries.* The YAML registries contain these null or empty values (most are intentional absences; the cast gaps are known):

{{T:yaml_nulls}}

`references/npc_registry.yaml` carries `age: null` on 29 characters, `coherence: null` on 28 and `stats: null` on 28; the engine's build-time age default (`age_at_build`) and `pool_default` stand in for them. `engine/season/hole_register.yaml` rows have an empty `site:` on 93 of 231 rows.

## 10. Memory, acquaintance and the flow of information

{{T:acq}}

- At build the realm has **no ledger content and no acquaintances**: all 83 persons know no one. At seed 0, after one season 46 of 82 still do not; after four, 40 of 80 (the probe ran at seed 0 only; the NOTE rows below are the three-seed evidence).
- A person knows another only through a `seen` claim, a truthy existence reading, or a told claim (`person_q.known_persons`). `tell`, `argue`, `give`, `covenant` and `issue` need a `to` the actor knows, so for the half of the population that knows no one they never form: {{T:note_nobody_total}} declines.
- **Ledgers are a 200-claim window.** `ledger_cap = 200` (`data/fixtures.py`, H-09). From empty at build, at seed 0 one ledger is at the cap after season 1, 17 after season 2, 46 after season 3, 80 of 80 after season 4 (at seed 1 the smallest ledger ends at 176; at seed 2 all are at the cap). Eviction at the cap emits no Event (`loop/witness.py`, `queries/world_q.py:3004`), so it was not counted; pooled `claim.deposited` ({{T:claim_dep}}) and `claim.decayed` ({{T:claim_dec}}, MATTER's per-season confidence decay, `loop/matter.py`) are not an eviction count.
- **A person's own telling is rare; hearsay is not.** After one season at seed 0, 1,565 of the 5,865 held claims (27%) are `told_by` (`ctl/aperture_1_0_seed0.txt`, `claim_sources`); they arrive by the chronicle channel, which `epistemic.py` records as the realm's only minter of `told_by` when it was last measured (a binding decision heard by persons nowhere near it), and they carry no `Claim.chain`. Claims with a chain, which only a spoken `tell` builds, numbered 0, 0, 4, 0 at the four season ends. `tell` was attempted 236 times over three seeds: 54 won (23%), 113 lost the contest and 69 were refused.

What this means for the game: the engine's non-omniscience (R-07, structurally sound) has a fixed-size memory and a social graph that does not form by itself. People who know no one cannot gossip, petition-by-name, or be told anything; what they know is what they saw in the room.

## 11. Emergent narrative

*Cross-person causation exists.* `storybar` over seeds 0 to 3, four seasons (`ctl/storybar_4seeds_4seasons.txt`; run twice: the arm-1 pooled lines of the two runs are identical): 12,899 acts; 30.4% have another person's act among their antecedents; the cross-person chain reaches depth 15; the two `off`/`off` arms read equal on every pooled reading (the control). The deepest chain at seed 0 has 14 steps (`ctl/chronicle_seed0_4seasons.txt`).

*Through refusals and successes alike.* `ctl/chain_outcomes_seed0_4seasons.txt` classifies both ends of every cross-person edge by whether the act succeeded or was refused: {{T:chain_outcomes}}

*The events that change the world are few.* Of 68,348 events at seed 0, 91.9% are `claim.deposited`/`claim.decayed` (belief bookkeeping) and 2,516 more are refusal-type events. About 3,000 are anything else, in 38 kinds, of which `condition.worn` (1,288) and `term.matured` (531) are bookkeeping; the events a reader would call a happening number a few dozen: 3 deaths, 13 tenures closed, 1 opened, 21 marches declared, 6 challenges issued, 5 `matter.turned`, 18 dispensations.

*Stability, endings, fields.* `stability` is constant (one distinct value, mean 0) across all 16 seed-season storybar readings (the two arms are both `off`, so they read identically by construction); the legitimacy estimate varies (160 to 350 distinct values per reading). `endings` is `[]` (H-176, a structural zero). The realm fights no field (H-175, H-149). Mortality is live: 83 persons at build, 80 after four seasons at seed 0, with 3 `person.died`.

*No text.* The only rendering is `harness/chronicle.py`: "<n>. season <s> | <actor> <verb> | emitted <kinds> | answers <m>". There is no function that turns a chain into prose. The narration proposal (`proposals/2026-10-13-narration-mechanisms.md`) landed only IN-50 and a narrower IN-37.

*What cannot be said from these instruments.* Whether a reader would find a chain compelling is not measured by anything in the tree. `corpus_run`'s ARC ENDS prints NOT-COMPUTABLE.

## 12. Limits of this report

- One container, shallow clone, Python 3.13.17; one platform (see the combat pin in §3).
- Three seeds, four seasons. Anything that needs a longer horizon (ledger saturation, long-run decay, endings) is not measured; the soak harness grades cost and act mix only.
- The census hooks observe `_admits` and `_eligible`; an act that is formed and then lost between the chooser and the fold is not seen. The `acts in act_of` count (3,256 at seed 0, four seasons) exceeds the fold's `resolved` count (2,628) by 628 acts that the chain-outcome probe could not classify: 624 are the contested admission refusals of §5 and 4 are `act.ineligible` acts (§1).
- `storybar`'s season-0 count at seed 0 (695) exceeds the aperture's (539, one season of a different instrument) by 156: 153 contested admission refusals (§5) and 3 `act.ineligible` acts.
- The 62 never-emitted kinds are never emitted in 12 seed-seasons, not in all play.
- Counts of refusals by verb are counts of decisions, not of persons.
- Figures about the proposals (item counts, collisions) are in the v10 head and were taken from extraction lanes that read the documents; they were spot-checked, not re-derived.

## 13. Reproduction

```
python tools/session_provision.py
export PYTHONPATH=$PWD
python proposals/2026-10-24-master-workplan-v10/ctl/failure_census.py SEED 4 OUT.json        # SEED = 0, 1, 2; add --no-hooks for the control
python proposals/2026-10-24-master-workplan-v10/ctl/static_inventory.py OUT.json
python proposals/2026-10-24-master-workplan-v10/ctl/acquaintance_probe.py 0 4 OUT.json
python proposals/2026-10-24-master-workplan-v10/ctl/chain_outcomes_probe.py 0 4 > OUT.txt
python proposals/2026-10-24-master-workplan-v10/ctl/build_report_tables.py DIR OUT.json       # DIR holds the JSON above
python -m engine.season.harness.storybar --base-seed 0 --n 4 --seasons 4 --arms off off
python -m engine.season.harness.aperture 1 0
```

The JSON the report was built from is in `ctl/`. Each run of the census takes about 90 seconds on four cores.
