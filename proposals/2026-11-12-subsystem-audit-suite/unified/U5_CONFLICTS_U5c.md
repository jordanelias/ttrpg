# U5c — conflicts decided: SC, FI, LACUNA, and the SOCIAL1, SOCIAL2, BINDING and MATERIAL verb families

## Status: REFERENCE (a conflict ledger for the suite; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Read at: the working tree of 2026-11-12. Lane: U5c, a Fable unification-closure lane (`UNIFICATION_BRIEF.md`, "Closure rule").

Each row is one contradiction between documents of this family, or between one of them and another
family's, Layer 1, the standing rule (*we do not do deterministic*) or one of Jordan's answers in
`unified/DECISIONS_ANSWERED.md` (cited `A-nn`; its ladder table cited `D-nn`). The decision is made by
the five-step ladder (CLAUDE.md §0): 1 superseded, 2 irrelevant, 3 a design document, 4 precedent,
5 architecture. The closure table that cites these rows is `unified/U5_FINDINGS_CLOSURE_U5c.md`.

**How the losing documents were edited.** Every losing file carries a `Reconciled:` line at its head
naming the row here (45 files). Three files were also rewritten in their body, because the text
contradicted the standing rule or Jordan's answer in a way a head line would not make safe to read:
`05_SC_evidence_and_rebuttal_B.md` (entry, the evidence term, falsehood and forgery),
`05_SC_sc05_kernel_disposition_B.md` (three checks), and this lane's own four proposals. Everywhere
else the head line states the replacement reading and the body is unchanged: no finding was deleted.
Proposal paths are relative to `proposals/`. Abbreviations: **OBS** `U5c_SC_one_obstacle_form.md`;
**RES** `U5c_SC_proceedings_residue.md`; **FRES** `U5c_FI_residue.md`; **VRES**
`U5c_VERBS_residue_and_governance_owner.md`; **SC-B** `05_SC_obstacle_difficulty_and_modifiers_B.md`;
**T13** `13_SC_tuning_tables.md`; **DRAW13** `13_SC_draw_for_unrolled_contests.md`; **EVID**
`05_SC_evidence_and_rebuttal_B.md`; **ADM** `19_LACUNA_admission_rides_the_citing_draw.md`.

## 1. The five conflicts the work order named

| id | documents | the contradiction | decision | by | edit to the losing document |
|---|---|---|---|---|---|
| C-05 | `08_FI_05_evidence-interface_B.md` E-6 and E-2; EVID (the addendum's G-65); ADM | is an item entered on the file with certainty (SC) or by the citing speech's band (FI), and who decides | **Entry is a draw read off the band of the citing speech:** Failure enters nothing, Partial enters at half weight, Success enters, Overwhelming enters with the `first` mark. ADM is the owner of the question; whether an entered item stands is the answering act's draw (the sweep's D-01, already applied) | step 3 (the standing rule; ADM is the later, deciding design) | EVID rewritten (the "recorded without a roll" sentence; the **file** row); head lines on `08_FI_05_evidence-interface_B.md` and ADM |
| C-02 | SC-B; `10_DICE_one_score_two_roles.md`; `10_DICE_capability_axiom_map.md`; T13; the verb proposals | two rosters named `obstacle_terms`, a field per term, and seven private per-verb obstacle tables | **One roster** (`rosters.yaml: obstacle_terms`, 28 ordered members), **one binding table** (`sigma.py::OBSTACLE_TERMS`), **one composer** (`roll.py::obstacle`), **one record field** (`obstacle_operands`). A verb that adds a term adds a member, a host function and a fixture, never a field or a table | step 5; `ED-SC-0033` cl. 3 (the obstacle has a single owner) | OBS written; head lines on SC-B, T13, the verb files |
| C-07 | DRAW13; `05_SC_negotiation_scene.md`; `14_VERBS_SOCIAL1_B_documents_and_obedience.md` §3 | is `covenant` acceptance the offerer's contest roll or the accepter's choice | **The accepter's own sampled act** (his `commit`), with odds his pursuits set. The offerer's roll cannot open another person's edge (`04` D-10a); the drafting is drawn, the consent is the chooser's sampler, which the standing rule exempts | step 3 (Layer 1); the sweep's D-06 | DRAW13 head line (its negotiation row yields) |
| C-25 | `14_VERBS_BINDING_A` to `_E`; SC-B | four new prizes and an audience chosen per verb inside `contest_input` for the nine contested governance rows | **One prize roster, one roll, one composer.** A prize row exists per distinct pair of (who hears, when fought); the audience is the prize row's `heard_by:` cell, read by one function. Kept: `a seat`, `a holding`, `a verdict`, `a task`. Not added: `an order`, `a cover`. Rank against an act is `rank_gap`; a document's band is `force` | step 4 (the existing `heard_by: bench` cell and its loader check); step 5 | VRES §2 written; head lines on the five BINDING files |
| C-10 | `audits/16_PESSIMIST_SC.md` §5; `audits/18_DETERMINISM_SWEEP.md` | four things that did not draw | (1) What a hearer believes is a reading over drawn deposits; no draw at read. (2) A failed bench asks again at most once per sitting. (3) A lapsed or dismissed matter re-opens only on something new, then by `carry`'s draw. (4) A convict does **not** release an imposed edge (Jordan, A-37): it ends by a drawn `pardon` or its term. This lane first read (4) as a drawn release; the answer reverses that | steps 3 and 5 for (1) to (3); Jordan for (4) | RES §4, §9; VRES §4; head lines on `14_VERBS_BINDING_A`, `_B` |

## 2. The obstacle and the roll

| id | documents | the contradiction | decision | by | edit to the losing document |
|---|---|---|---|---|---|
| C-01 | SC-B edit 1; `16_PESSIMIST_SC_A_what_the_speaker_brings_is_leverage.md`; EVID; `19_LACUNA_questioning_has_an_approach_and_a_cost.md` | favourable modifiers subtracted from the obstacle after the ceiling, or named levels | **Levels.** What stands against the act is the obstacle; what a party brings is leverage. Nothing lowers the obstacle | step 1 (`ED-884`, `ED-934`, `ED-1037`; the `advantage_sources` roster's own law); confirmed by Jordan, A-25 | SC-B head line; EVID "The evidence term" rewritten; head line on the questioning file (C-18) |
| C-03 | SC-B; T13 T3 | the hearer's disposition read by `stance_toward` or by `person_q.regard(counterparty, actor, fx)` | **`stance_toward(counterparty, actor)`**, clamped; hostile half the `regard` term, favourable half a `favour` level. `regard(…, fx)` opens the counterparty's ledger at RESOLVE | step 3 (`04` §B.2, the F8 carve-out) | T13 head line |
| C-04 | SC-B; `10_DICE_one_score_two_roles.md`; `16_PESSIMIST_DICE_task_difficulty_and_throughput.md`; T13 | three sets of row values; an `obstacle_default`; an `opposition_fallback` fixture | **Opposition is never absent:** where nobody stands opposite, the term is `opposed_ob(pool_default)`. `obstacle_default` is deleted; `opposition_fallback` is not added; every rolled row is `routine` at the control arm; at T13 commit 2 only `interrogate` is `demanding` | step 3 (the ruled "score plus whatever specific modifiers"); step 5 | head lines on SC-B, T13, `10_DICE_one_score_two_roles.md` |
| C-06 | `05_SC_contest_record_on_event.md`; SC-B | the Event's record carries `room` | `margin_endings`: `[pool, ob, net, margin, terms, levels, leverage]` | step 5 | head line |
| C-21 | `14_VERBS_SOCIAL2_B`, `_C`, `_D`; SC-B | seven per-verb obstacle tables | folded into the one roster or the leverage channel (OBS §2, §3) | step 5 (one owner) | head lines |
| C-33 | `05_SC_opposed_obstacle_parity.md`; SC-B; T13; `13_SC_calibration.md`; `audits/13_SC_contest_interrogation.md` | the suite treated the half-score rate as ruled and held the parity proposal back | **Jordan, A-26: 0.4 per point.** The parity proposal is un-held and carries the rate; `opposed_ob` stays its one owner. With A-5 (bell curve), A-6 (score plus a base, floor five) and A-7 (two inputs) every number in T13, the calibration and OBS §4 is recomputed in **one** joint step (OBS §4 step 5). Steps before it land at the rate in force, so they stay hash-equal. This lane first read the half score as kept; the answer reverses that | Jordan | head lines on the four files; OBS conformed |
| C-35 | `14_VERBS_BINDING_C_turnover.md` (`standing`); T13 T4 (`standing_dice`); `04` §B.7 | rank in the odds, against "rank supplies dice and gates nothing" | **Jordan, A-12: a seat carries a modifier.** The half that stands against an act is the term `rank_gap`; the half that helps is declared once as the source `office`, whose first member is T13 T4's bench die. It cannot double-count with `regard`, which reads stance rows only. The Layer 1 amendment text is owed by the unification stage and is not applied by this lane | Jordan; Layer 1 is not edited to match | OBS §3; head lines on `14_VERBS_BINDING_C`, T13 |

## 3. Proceedings

| id | documents | the contradiction | decision | by | edit to the losing document |
|---|---|---|---|---|---|
| C-08 | `05_SC_acquittal.md`; `audits/05_SC_audit_addendum_B.md` G-55 and its Part 4 §3.5 | the count of failed askings that dismisses: 1 or 3, and where it lives | an arrangement-row key `ballots`, default 1; a row may author 3 | step 3 (`ED-IN-0288`'s intent) | head lines on `05_SC_acquittal.md`, `05_SC_arrangement_rows_that_bind.md` |
| C-09 | `05_SC_sc05_kernel_disposition_B.md`; the sweep's D-01, D-03 | three checks in the carry table assert a fixed outcome for mechanisms the sweep had made draws | each check asserts a share over seeds | step 1 (superseded by the sweep's own correction) | body rewritten (three table cells); head line |
| C-11 | `05_SC_playable_hearing_B.md`; DRAW13 edits 3 and 4; the host's `vote` conjunct | two owners of a bench's ballot | **The hearing's close** (`HearingOutcome.ballots`): each seat's ballot is a draw on that voter, his public commits entering as `lean` levels; the existing `veto` demotes when weighted fors fall below quorum; the `vote` conjunct is deleted | step 5; confirmed by Jordan, A-14 | RES §6; head lines on DRAW13, `05_SC_playable_hearing_B.md` |
| C-12 | `14_VERBS_SOCIAL2_C` §3; DRAW13; `19_LACUNA_questioning…`; `16_PESSIMIST_FI_D…` | three rows for `interview` | `14_VERBS_SOCIAL2_C` §3 owns the row; the LACUNA file supplies `approach`; the row stays withheld until its product lands | step 4 (the verb lane owns its row) | head lines |
| C-17 | `19_LACUNA_verdict_ladder_and_reversal.md` | a `voided` stage written on a refusal path; an appellate bench closing a lower seat's disposal | the next `convene` writes `voided`; the appellate bench writes `reversed` and the disposing seat's bench closes the edge by its own drawn `pardon`. Appeal on new grounds only (Jordan, A-39) | step 3 (`04` §C.2: no listed gate basis closes it from above); Jordan | head line |
| C-18 | `19_LACUNA_questioning…` | `press` subtracts from an obstacle | a `press_level` for the questioner and against an answering `lie` | C-01 | head line |
| C-29 | `14_VERBS_SOCIAL2_C` §2; ADM; EVID | three band maps for `speak` | ADM (entry) and EVID (answer) | step 4 | head line |
| C-36 | `16_PESSIMIST_SC_C_a_verdict_names_its_party.md`; addendum C-1; RES §8 | who a verdict serves | **Jordan, A-38: the petitioner, or a seat he names.** A seat he names is the existing `oblige` with that seat as object; a remedy to his person is a `damages` disposal kind, design-first | Jordan | RES §8 rewritten |

## 4. Fieldwork and evidence

| id | documents | the contradiction | decision | by | edit to the losing document |
|---|---|---|---|---|---|
| C-13 | T13; `audits/13_SC_contest_interrogation.md` R-11; three superseded files | citations of superseded files; R-11 ("two SC files do not exist") is false at HEAD | repointed; the three superseded files say so at their heads | step 1 | head lines on `05_SC_playable_hearing.md`, `05_SC_sc05_kernel_retirement.md`, `08_FI_05_evidence-interface.md`, T13 |
| C-14 | `08_FI_02` edits 2 to 4; `08_FI_06` §5; `16_PESSIMIST_FI_A` edit 5 | three texts for `said_slants` | `[newest, valence, unshared, unshared_first]` (FRES §6) | step 5 | FRES §6; head line on `08_FI_02` |
| C-15 | `08_FI_04` §1 and §3; `16_PESSIMIST_SC_D` edit 1; `16_PESSIMIST_SC_C` edit 1; `14_VERBS_SOCIAL1_C` | two carriers each for `argument.held` and for reading a restraint edge as two ends | carried once, by the pessimist files (the wider edits) | step 4 | head lines on `08_FI_04`, `14_VERBS_SOCIAL1_C` |
| C-16 | `08_FI_04` §6; `04` §A.2 (`loop/witness`) | a Layer 1 hunk to list the reads the code makes | fix the code, not Layer 1; no lane applies the hunk | step 3 (CLAUDE.md §0.05); decision register D-74, taken B | head line |
| C-19 | `14_VERBS_SOCIAL1_A`; `08_FI_02` edit 5; `14_VERBS_SOCIAL2_A` §4 | two readers of "who I believe is with me" | `person_q.present_persons` | step 5 | head lines |
| C-20 | `14_VERBS_SOCIAL2_B` §4; `08_FI_01` | two readers and two build steps for "who holds that seat as I know it" | `person_q.holders_named`; `seed_seat_news` | step 5 | head lines |
| C-22 | `08_FI_03` §3; `19_LACUNA_conclusion…`; `14_VERBS_MATERIAL_A` to `_E` (D-1); `18_DETERMINISM_task_draw_for_uncontested_verbs.md` | band-keyed `writes:` on a route row, which the loader refuses (`04` §B.13 invariant 12) | **Decided with U5a (its C-U5a-10):** a drawn act with nobody opposite is a route row with flat `writes:` scaled by the band, or a `contests: "a task"` row where two bands write different cells; an inquiry writes nothing and deposits to its actor. `reconstruct` is an inquiry; the committed conclusion is the maker's `utter` | step 3 (Layer 1; MECHANICAL at load) | VRES §1; FRES §7; head lines on eight files |
| C-23 | `14_VERBS_MATERIAL_A` (`effect_share`); 18-A (`task_fraction`) | two names and two value sets for one table | `task_fraction`, 1 / 1 / 0.5 / 0; the other values are a sweep arm | step 4 (the name U5a and two other proposals already cite) | head line; OBS §6 |
| C-24 | `08_FI_03` §2; `08_FI_07` §2 (b); `14_VERBS_MATERIAL_E` §2 | three rules for what a look teaches by band | `observes:` is flat; `finding_terms` owns the band; gating reads teach at every band | step 5 (one band-keyed table) | FRES §8; head lines |
| C-37 | `08_FI_01` edit 6; `audits/16_PESSIMIST_FI.md` S-PES-FI-2 | does a death travel with the seat's news | **Jordan, A-32 and A-33:** seat changes ship realm-wide with by-presence the test arm; a death travels apart, by presence, trail and telling | Jordan | FRES §2; head lines on `08_FI_01`, `08_FI_02` |

## 5. Verbs

| id | documents | the contradiction | decision | by | edit to the losing document |
|---|---|---|---|---|---|
| C-26 | `14_VERBS_SOCIAL1_C`; `05_SC_hearing_capabilities.md`; `16_PESSIMIST_SC_E` | `lie`'s skill name; a `contradiction` term and a `notoriety` term that open other people's ledgers | skill `deception`; `contradiction` dropped (done at WITNESS); `notoriety` is `watch`, read from presence | step 3 (`04` §B.2) | head line |
| C-27 | `14_VERBS_SOCIAL1_D` §3 | a MATTER write of `Person.stance` | MATTER emits `challenge.declined`; the challenger's satisfaction is his own `forgive` | step 3 (`04` §A.2, the `loop/matter` row, and AX-3: a person's stance is an ACTS row written at RESOLVE; the MATTER token does not open it) | head line |
| C-28 | `14_VERBS_SOCIAL2_A` edit 2; `audits/14_VERBS_MATERIAL.md` §17.2 | the list of bare-`Record` rows omits `research` | `_stamped` carries both pairs | step 5 | head line |
| C-30 | `14_VERBS_SOCIAL2_B` §4; the ruled `members_by_admission` | admission to a seat's service: certain, or a draw against the seat | **A draw against the seat** (decision register D-31, taken A under Jordan's A-24). This lane first disputed it; the answer reverses that | Jordan (A-24) | head line; VRES §6 |
| C-31 | `14_VERBS_BINDING_C` §3 | a Partial `succeed` that keeps the title needs an unlisted gate basis | termed seats under the existing claim basis; the title laid down | step 3 (`04` §C.2) | head line |
| C-32 | `14_VERBS_MATERIAL_A` §6; `03_PC_exits_withdrawal_recovery.md` Part C | two rows for `tend` | the MATERIAL file owns the row | step 4 | head line on the MATERIAL file; the PC file is U5b's |
| C-34 | `14_VERBS_SOCIAL1_B` §1; `06_FA_decree_binds.md`; SOCIAL1 D1 | must an answer to a decree wait on `give` | **Jordan, A-21: a decree is proclaimed.** `give` stays for a covenant and a challenge | Jordan | head line; VRES §5 |
| C-38 | `14_VERBS_BINDING_D`; `ED-IN-0256` (4) | territorial authority or command | **Jordan, A-22: command**; commit D2 ships behind its revert | Jordan | head line |

## 6. Layer 1 (Lens B of `skills/layer-conformance`): what was rewritten, what is a conflict with intent

Rewritten to conform (each by a row above): C-03 and C-26 (a ledger other than the actor's opened at
RESOLVE, `04` §B.2; STRUCTURAL in the spec, CONVENTION in enforcement until a test plants the read);
C-22 (invariant 12; MECHANICAL at load); C-27 (an ACTS row written under the MATTER token; MECHANICAL at the gate); C-17
and C-31 (a write under no listed gate basis, `04` §C.2; MECHANICAL at the gate); C-07 (a non-owner
write of another's edge, D-10a); C-16 (a spec edited to match its code).

Conflicts between Jordan's stated intent and a ratified Layer 1 row. Each is now answered, so neither is
listed with two options; each owes an amendment text that no lane here applies:

| row | Layer 1 says | Jordan's answer | owed |
|---|---|---|---|
| `04` §B.7 | rank supplies dice and gates nothing | A-12: a seat carries a modifier | amendment text (unification stage); `rank_gap` and `office` are written under the answer and say so (VRES "Layer 1 reading") |
| `ED-IN-0256` (4), as `04` cites it | a seat orders whoever stands in its land | A-22: command | amendment text; behind a revert until then |

## 7. Owed to other families (named, not edited by this lane)

- **U5a (DICE).** `10_DICE_capability_axiom_map.md` §G edit 7's "favourable sum clipped" clause: under
  A-25 a favourable `circumstance` is an `edge` row on the leverage channel; `circumstance` gains are
  non-negative. `16_PESSIMIST_DICE_task_difficulty_and_throughput.md`'s self-plea text reads with C-04.
- **U5a and U5d (18-A).** Item 2 of `18_DETERMINISM_task_draw_for_uncontested_verbs.md` still says a
  routed row's `writes:` is "degree-keyed, never flat", against its own reconciled item 4. Item 4 is the
  decision (C-22).
- **U5b (PC).** `03_PC_exits_withdrawal_recovery.md` Part C defers its `tend` text to
  `14_VERBS_MATERIAL_A_mending.md` §6 (C-32).
- **U5d (institutions).** The obstacle members `obligation` and `remove` are that family's to place;
  `remove` reads as the same quantity as `distance` and should be one member (OBS §2).
- **The calibration step.** A-5, A-6, A-7 and A-26 together move every social number. One step re-solves
  them (OBS §4 step 5); no file in this family holds a number that survives it.

## 8. For Jordan

Nothing. Every item this family would have carried is answered in `unified/DECISIONS_ANSWERED.md`; the
closure table lists them. Three answers reversed this lane's first reading (C-10 row 4, C-30, C-33) and
the rows above say so.
