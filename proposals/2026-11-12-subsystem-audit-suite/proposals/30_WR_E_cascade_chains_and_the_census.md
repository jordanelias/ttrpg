# WR-30-E — cascade chains and the census: the chains written link by link, an instrument that tells compounding from correspondence, and the gates for eras, regimes, strife, endings and cascades

Reconciled: 2026-11-12, wave 3 (W3-3) — R3 §1 found it CONFORMS (harness only) and R3 §2 found no ruling it contradicts; added: the serial order on `harness/storybar.py` (C3-K7), the batch (U3 B38), and the glossary's reading of "regime" in E-07 and C13 (they read `30_WR_B`'s creed bodies and, after `31_WR_A`, `core_standing`'s cores; "regime" in A-82's sense is the latter). Tier already named. U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "province" → "territory" (glossary *territory*).

## Status: PROPOSED

Lands in batch: B38 (narrative and regimes), after `30_WR_D` and before `30_GO_F` (U3 §1 item 38). Edits `harness/storybar.py` after `30_WR_C`, before `31_WR_B` commit 3 (C3-K7: one commit per proposal, never concurrently).
Depends on: see "Dependencies" below (`23_STORY_D` and `20_NARRATIVE_F` land in B36).

Source: `audits/30_ERAS_REGIMES_STRIFE_AND_MOMENTUM.md` §4, §7, F-30-09, F-30-10. Jordan, 2026-11-12: *"cascade effects and compounding are real"*; A-80; A-81. Reference only (`CLAUDE.md` §0.05). Lane WR; owner file IN's (`engine/season/harness/storybar.py`).

Extends `23_STORY_D_story_census_and_gate.md` (the `--stories` block, `Shape`, clauses C0 to C6) with shapes and clauses; it adds no second bar. Composes on `09_WR_story_instruments_that_can_fail.md` (arms, `edge_null`), `20_NARRATIVE_F` (crossings), `09_WR_B_readings_of_closure_and_tension.md` (`closes`, `situations`), `16_PESSIMIST_GAME_consequence_reading.md`, CR-97, CR-99, and `30_WR_A` to `D`, `30_WR_G`.

## What it changes in `engine/season/` at runtime

**Nothing.** Every edit is under `engine/season/harness/` or `engine/season/tests/`. No hash moves. It mints no carrier, field, Event kind or register row for an arc, story, era or cascade (`ED-IN-0225`).

## 1. The cascade chains

Each chain is a sequence of links; every link is a draw (a person's sampled choice and his act's roll, or the world's keyed draw). "Likelier because" names the reading of `30_WR_D` §1 that the earlier link moves. "May stop at" is where the chain ends short, which it must be able to do (C2). Story ids are `audits/23_STORY_ENABLEMENT.md` §2's; the carrier of each link is that file's §5, not restated.

| chain | links (story ids) | likelier because | may stop at | what it does to era, strand and regime |
|---|---|---|---|---|
| **K-1 the crown** | a death (S-01, S-09) → the news of it, apart from the seat's (S-02, A-33) → a vacancy that costs (S-05) → a claim, then a rival's (S-04, A-19) → sworn men meet a new holder (S-16) → a march on the claim (S-20, A-74) → a field (S-21) → a peace (S-18) | the vacancy is on the table of all who may claim (mandatory, A-47); each estimator's `legitimacy` differs by what he holds of the deeds; a standing rival claim is a ground | one claim, acclaimed; a regency accepted; a rival who yields | RULE turns twice; `contested`, then `civil_war`; one strand whose subject is the seat; regimes hold two accounts of who is king |
| **K-2 the lean year** | a harvest remembered (S-35) → a famine (S-32) → blame (S-33) → a petition for relief (S-49) → the petitioner kept waiting (A-64) → refugees or a riot (S-34, A-56) → a decree defied (S-15) → a steward stripped (S-10, S-11) | the spell is shared for the year; a due unmet lowers regard; the waiting intensifies the matter | relief sent; a good second year; the bench grants | `dearth`; strands at the settlement, zooming to the duchy; the era is troubled only if a realm-rung strand opens by force |
| **K-3 the unpaid lord** | an oath that lapses unpaid (S-62) → blame (S-33) → the same man refused at the door (S-49 denied) → he swears elsewhere or withholds (S-16, S-15) → others who hold the same grievance follow (E-08) → a rival holds the seat (S-14) | `dues_unmet`; `refused_before` turns him to another means; the side thins | paid late (Partial: a new term); one man leaves and no one follows | a strand inside one regime (a quarrel over what the tie requires); a faction split without a change of creed |
| **K-4 the killing** | a killing as a crime (S-09, A-16) → found out (S-55) → the wrong man accused (S-51) → a verdict (S-43) or an acquittal (S-44) → an appeal on new grounds (S-45, A-39) → revenge (S-08) | grievance and hatred gate the attempt; a trail is evidence someone holds; a verdict names the party it serves (A-38) | caught in the act; never found (the strand goes dormant, and may be revived: `30_WR_C`) | a strand at the hearth that zooms when the dead man held a seat; if he was the head, K-1 |
| **K-5 the split** | a crisis of faith drawn and seen (S-64, A-24) → a man talked round (S-59) → a member asked what he thinks of his own side (S-16) → he leaves the creed (A-46) → a second leaves → an excommunication (S-17) or a rival head | accord and credit along the fault line; the creed on his table; `opinion_of` after the first leaver | reconciled; stripped first (A-35); leaves alone | a regime splits; `schism` when a realm-reach seat leaves; the strand is between regimes |
| **K-6 the conquest** | a war for a cause (S-20) → a field won (S-21) → the victor's choice to seize, occupy or go home (A-66) → an army eats the territory (S-26) → refugees (S-34) → the holder's kin and sworn men (S-08, S-16) → a counter-march or a treaty | victory raises standing and committers; losses and fatigue carried lower the next muster | a drawn field (both home at once); a withdrawal; a siege that fails | `foreign_war` or `civil_war`, then `occupation`; seats pass with the land (A-58) |
| **K-7 the word** | a rumour past one mouth (S-52) → believed in one camp, denied in the other (G5) → a man deceived and acting on it (S-56) → a false accuser pays, or a liar is caught (S-47, S-54) | credit by accord; each hop refracts | disbelieved; forgotten | two accounts of one deed; a strand between regimes |
| **K-8 the breaking place** | the wearing ground (A-40) strains → a site breaks by a draw (`16_PESSIMIST_WR_B`) → a witness asks what can be done (S-42) → a mending that costs and can fail → the neighbours strain or hold | a broken site pulls its neighbours; a band crossing seen is a question | mended; holds by the draw | a strand opened by natural shock (CR-73); an ending row if the Rupture is reached |
| **K-9 the King, as he dies today** | an order names him → a `capture` is fought → he is felled (`audits/22_HAPPENINGS.md` §1.3) → nothing: both seats close and stay empty | nothing (the verb was ungated) | n/a | today: a `vacant` era that never turns. Repaired, it is K-1 with a killer to find (K-4) |

## 2. Telling compounding from correspondence

A chain in the log shows that b followed a. It does not show that a made b likelier: both may follow from the build. Three controls, in rising strength, all on the one instrument:

1. **Order against mix** (exists): `harness/strife.py::link_profile` (`:294`), a pair's count against the same strands in shuffled order.
2. **Links against the edge null** (WR's `edge_null`): a shape counted on the log against the same log with each act's antecedents re-dealt, edge counts kept.
3. **The fork lift** (new). The engine's draws are keyed and seeded, so the counterfactual can be run. Build one world; run it to the season before a could occur; fork it (`storybar.fork`, `:394`) under N draw seeds (`draw_seed_arm`, `:406`). The history up to the fork is identical in every fork. In some forks a occurs and in some it does not, because a is a draw. Then

   `lift(a → b) = P(b within W seasons | a occurred) / P(b within W seasons | a did not)`.

   Anything the build wrote into both a and b is in both groups and cancels. A lift above 1 by more than the spread across fork groups is compounding; a lift of 1 with a high co-occurrence is correspondence. A lift that cannot be computed because a occurs in every fork or in none is reported as such (a is then a schedule, or impossible: C2's own failure).

## 3. Shapes added to the census (`SHAPES`, in `23_STORY_D`'s format)

A shape any of whose kinds has no emitter prints `n/a (no emitter)`, as that proposal rules.

| id | name | opening | turn | close | variant |
|---|---|---|---|---|---|
| E-01 | a reign ends | `person.died` of the head seat's holder, or `tenure.closed` on the head seat by an act | — | `tenure.opened` on the head seat (other) | the turn's code: DN, KL, XE, abdicated, deposed |
| E-02 | a vacancy that is fought over | `tenure.closed` on the head seat | a second `succession.claimed` on it (other) | `tenure.opened` on it | which title won (party) |
| E-03 | a war inside the realm, with an end | a `commitment.made` to a WAR Proposition by a mustering seat, both parties holding under the realm | `field.won`, `field.lost` or `rung.seized` | the last such commit's `commitment.ended`, or a `covenant` between the parties | kind and band |
| E-04 | a conquest | `march.declared` by side R or O | `field.won` by the marcher | `rung.seized`, an occupation, or the army home | seize, occupy, withdraw |
| E-05 | a schism | a `commitment.ended` or `tenure.closed` on a creed or head seat by a realm-reach holder | a second such by another on the same creed | a rival `office.established`, a `commitment.made` back, or a strip | rival, reconciled, stripped |
| E-06 | a famine's end | S-32's opening | S-32's turn | the era condition `dearth` closing (`30_WR_A`) | by relief, by the year |
| E-07 | a regime moves | counted from `--regimes`' derived lines (`30_WR_B` commit 2), not from `causes[]`: `formed`, `split`, `unseated`, `ended`, each with the Event that moved the person | | | the word |
| E-08 | the side thins | a `commitment.ended` on a creed by A | a `claim.deposited` of it in B, a member | a `commitment.ended` on the same creed by B | B left, argued, stayed (the last counted from `argue`) |
| E-09 | a strand revived | counted from `30_WR_C` commit 2's `revived` | | | the opening kind |
| E-10 | the man who would not do as his house does | an executed act by A whose verb's alignment with A's believed custom is below 0 (`30_WR_G`), with a `claim.deposited` of it in a member of his circle | — | an executed `argue`, `revoke`, `release` or `challenge` by that member whose subject is A | the answering verb |
| E-11 | an era turns | counted from `world_q.era_turns` (`30_WR_A`): one per turn, with `opened_by`'s code and the facts before and after | | | the fact that changed |
| E-12 | a cascade | a consequence chain (`chronicle.consequence_chains`, `:177`) of depth 4 or more whose acts' Receipts write three or more different cells of `arc.ARC_WORLD` | | | the cells, in order |
| E-13 | another means | a contested act by A whose Event is its Failure band, subject X | — | within two seasons an executed act by A with a **different verb** whose subject is X or X's believed holder | forum (`petition`, `carry`), force (`march`, `challenge`, `capture`), paper (`forge`, `cite`), flight (`migrate`, `release`), ally (`covenant`, `commit`, `oblige`), claim (`succeed`, `establish`) |

Each shape lands with its plants in `engine/season/tests/test_storybar.py`, as STORY-D edit 5 rules: the full plant reads 1, each beat removed reads 0, the plant under `edge_null` reads 0, and the test asserts it asserted.

## 4. Clauses added to the gate (beside C0 to C6)

| clause | reads | fails when | control |
|---|---|---|---|
| **C7 it compounds** | the fork lift of §2 for each loop row of `30_WR_D` §2 (a = the loop's first event, b = its next), eight draw seeds, window two seasons | the lift is within the spread across fork groups (the path is declared and does nothing), or a occurs in all forks or none | the loop's switch at control: the lift there is the base rate |
| **C8 a held world still moves** (A-80) | the **entrenched arm**: every draw on a row that declares `contests:` returns the challenger's Failure (the holder always holds). Reads E-13's six variants, S-33, S-34, E-08 and the petition's intensified stage | fewer than three of those ten at two seeds or more of five; or executed acts per person-season below half the free arm's `[ASSUMPTION; Jordan to correct: three of ten; a half]` | the free arm at the same seeds; and, as the control of the control, S-43 and E-02 must read 0 in the entrenched arm (the pin is real) |
| **C9 no scene is still** (A-81) | `null_scenes`: acts with no durable write, by verb and outcome class (the definition is `30_WR_D` §3) | any count above 0 once that section's carriers have landed | a planted act whose Events write nothing reads 1 (the reading can see a null); today's baseline, by this lane's looser probe: 59 of 821 acts at seed 0, one season (P-2) |
| **C10 the pull is felt and resisted** (A-83) | arms `custom_off` and `custom_on`: the aligned share of executed acts; E-10 | the aligned share is equal within the off arm's spread; or E-10 reads 0 at every seed of the on arm (nobody ever resists) | `custom_off` |
| **C11 an era can end, and not on a timer** | E-01, E-11 over five seeds, eight seasons, bodies arm on | no RULE turn at any seed; or a turn at every seed in the same season (a schedule) | bodies arm off: no natural turn |
| **C12 strands stay several and conclude** | `strife --strands`: strands per rung kind; largest share; `closes` by act against by term and threshold | one rung kind only; the largest strand above the `all` arm's share; no strand concluded by act at any seed | `strand_links: all` |
| **C13 regimes are more than one, and move** | `--regimes`: bodies, core and fringe, `moved` | one body holds more than 60% of the convinced; or `moved` equal at every seed | `held_reading: any`; `regime_gain 0` |

## Instructions to code

Tier: second (sonnet); a third-tier critic on the fork lift's grouping. All under `engine/season/harness/storybar.py` unless said; hash EQUAL throughout. Land after STORY-D (it owns `Shape`, `SHAPES`, `stories`, `--stories`, `--pin-rolls`).

1. **`null_scenes(w, n) -> dict`**: `{"total": int, "null": Counter((verb, cls))}` over `corpus_run.attempts(w, n)` (the one owner of made and refused, `harness/corpus_run.py:817`), `cls` in `made`, `graded_loss`, `refused`. An act is null when no Receipt on any Event naming it in `causes[]` writes a `write_matrix.yaml` cell with a `RES` or `WIT` step, counting a `claim.deposited` only where the claim's holder is the actor or the act's counterparty (`state/carriers.py::subject_of(act)` when it is a person, or a seat's live holder). A-62: the budget is a Query and writes no cell, so nothing is excluded for it; if a later build makes the debit a write, that cell is excluded by name here. CLI `--null-scenes`, printed per season and pooled: `null_scenes total=<n> null=<n> | <verb/cls=n, …>`.
2. **The entrenched arm**: `ARMS` (`:87`) gains `entrenched`, applied as a harness-only `draw_factory` wrapper (the mechanism of STORY-D's `--pin-rolls`), under which a draw whose act's row declares `contests:` returns the band the row maps to the challenger's Failure, and every other draw is untouched. `--arms off entrenched` prints both.
3. **`fork_lift(base, seasons_before, window, draw_seeds, a, b) -> dict`**: `a` and `b` are predicates over `(log slice, act_of)` (a `Beat` of STORY-D, reused). Runs `base` for `seasons_before`, forks per draw seed, runs each `window` seasons, groups forks by whether `a` matched in the first season after the fork, returns `{"with_a": n, "b_given_a": n, "without_a": n, "b_given_not_a": n, "lift": float or None, "note": str}`. CLI `--cascade <loop id>`, with the `(a, b)` pair per loop held in one table `CASCADES` in this module (an instrument's table, as `SHAPES` is), keyed by the LOOP row ids of `30_WR_D`. No default for the seeds or the window (`tools/ci_sim_fabrication_check.py`'s scope).
4. **`SHAPES`** gains E-01 to E-06, E-08, E-10, E-12, E-13; E-07, E-09 and E-11 are printed by their owning blocks and listed in the `--stories` summary by reference, not recomputed.
5. **Arms** `custom_off`, `custom_on` (`30_WR_G`), composed from fixtures as `20_NARRATIVE_F` edit 3 composes `basis_off`.
6. **Tests**, `engine/season/tests/test_storybar.py`: `test_null_scenes_sees_a_planted_null_and_not_a_planted_write`; `test_a_bystander_s_sighting_alone_is_not_a_durable_write`; `test_the_entrenched_arm_pins_contested_draws_and_no_others`; `test_fork_lift_is_one_on_a_planted_coincidence` (a and b both caused by the build: lift within tolerance of 1); `test_fork_lift_is_above_one_on_a_planted_cause` (b admitted only where a's write exists); `test_fork_lift_reports_a_schedule` (a in every fork: `lift None`, note says so); one plant set per new shape; `assert checked >= …` in each.

## The gate for this proposal (execution artifacts)

```sh
PYTHONHASHSEED=0 python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 2 --arms off off --null-scenes --stories
PYTHONHASHSEED=0 python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 3 --arms off entrenched --stories --null-scenes
PYTHONHASHSEED=0 python -m engine.season.harness.storybar --base-seed 0 --seasons 3 --draw-seeds 0 1 2 3 4 5 6 7 --cascade L15
python -m pytest engine/season/tests/test_storybar.py -q
```

Expected **on the shipped engine**, which is the bar failing where it should: the first prints `null=` above 0 with the four inquiry verbs leading (P-2), EQUAL arms, the control shapes of STORY-D above 0 and E-01 to E-13 at 0 or `n/a`; the second prints S-43 and E-02 at 0 in the entrenched arm and fails C8; the third prints the retry loop's lift, the first reading that can say whether PES-CORE's 41% against 21% (a refused act is repeated more than an executed one) is cause or coincidence; above 1 is expected and is recorded either way, since it is the one compounding the shipped engine may have, and the one to be removed. After the carriers land, each clause is read by the session closing that batch.

## The falsifier

- `null_scenes` reading 0 on the shipped engine: the definition counts bystanders' sightings (it cannot see P-2's 59).
- A fork lift above 1 on the planted coincidence: the groups are not built from one history.
- The entrenched arm changing an uncontested draw (compare the uncontested Events of the two arms up to the first contested one: equal).
- A shape E-xx above 0 under `edge_null` at the log's rate.
- Any content hash moving.

## Dependencies

After STORY-D, `09_WR_story_instruments_that_can_fail.md`, `20_NARRATIVE_F`. Each clause needs its subject: C7 `30_WR_D`; C8 and C9 `16_PESSIMIST_CORE_a_refusal_is_remembered.md`, `23_STORY_A`, `U5a_DICE_owed_edits.md` §4, `28_CORE_scene_access_C`; C10 `30_WR_G`; C11 `30_WR_A`, `22_HAPPENINGS_A`; C12 `30_WR_C`, `09_WR_strand_conclusion.md`; C13 `30_WR_B`, `20_NARRATIVE_A`.

## Layer 1

`ED-IN-0225` (no arc carrier): kept, **STRUCTURAL**; the census is a reading. `04` §A.2: the harness reads, writes nothing. The entrenched arm and the fork wrapper live in the harness and never in `loop/` or `seam/`: **MECHANICAL** (the existing test that a render moves no hash covers the pattern; each new flag gets the same assertion). `CLAUDE.md` §0.1 pt 5: no guard is added; the clauses are read by a closing session, as STORY-D's are.

## NERS reading

- **N.** Without the fork lift "compounding is real" is asserted from chains, which correspondence also produces. Without C8 and C9 two standing requirements have no observable. Holds from the instrument's side in every direction the census does.
- **R.** It measures the half with no player in it, and at the extremes: a world where nothing can be won, a world with the pull off.
- **S.** One instrument, STORY-D's `Beat` reused for every predicate, WR's null, the one made-and-refused rule.
- **E, last.** Three functions and thirteen table rows against the only readings that say whether a small thing grew. High.

## Cost class

Small build, one session, after STORY-D; then one row and one plant per shape in each batch's commit.
