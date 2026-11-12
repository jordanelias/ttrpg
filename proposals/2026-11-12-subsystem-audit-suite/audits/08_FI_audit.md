# FI — adversarial steelman audit

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 601e715 (working tree)

Subsystem: fieldwork, investigation, epistemics, information, witness. Lane tag `FI` (with the `IN`
epistemic work the dossier files here). Written head-first (brief, "write early"); later sections were
appended as the reading and the probes completed. Every execution reading below carries its seed and season
count; `PYTHONHASHSEED=0` throughout. Scratch output: the session scratchpad, `runs/FI/`.

## 0. Verdict

**The information model is a sound basis for an emergent-narrative game and the fieldwork game on top of it
is not yet a game; the single largest obstacle is that almost nothing a person knows reaches another person
by a person's act.** The witness barrier, the per-holder ledger, provenance chains, refraction, the
teller's record and clause 4 are real, executed, single-owned and unusually principled: two people in one
realm hold different facts, and a decision can only be declined on what its maker holds. But in computed
play the machine idles. Over three seeds and one season each, between 0 and 7 of the 10,000 to 12,000 claims
people hold arrived by someone telling them; about a third to a half arrived as speakerless hearsay, chiefly
by `chronicle`, a realm-wide broadcast that reads no person; no claim was retold; no trail was found; and of 461, 445 and 485 candidates
a belief declined, the world disagreed with the belief once, twice and once. False beliefs form (a liar's
cell lie, a `Partial` telling's drift, a stale reading), in single digits per season; they do not spread,
they are exposed only to a hearer who already knew better, and they change close to nothing anyone does.
Separately, **decisions are not non-omniscient as `requirements.yaml` R-07/R-08 state**: the question
projection hands a person referents read from world truth he was never told (F-FI-01, shown by a probe
with a control), against a decision the ledger already records as taken (ED-IN-0292, last row). As a
standalone game, investigation has no scenario, no stake, no conclusion and no end: its registered module
is a band-to-terms lookup over a trail that the seeded realm never reaches.

## 1. What it is, as coded

**Three layers, one of which is the game's whole information model.**

1. **The witness barrier** — `engine/season/loop/witness.py::witness` (bound onto `SeasonDriver`, barrier 4).
   Input: the round's `Event[]`. For each Event it asks `epistemic.observers_for` who is admitted and by
   which channel, then deposits, into each admitted person's OWN `Person.ledger` through the write gate
   (`w.write("claim_ledger", token, …, emits="claim.deposited")`), up to six kinds of `Claim`:
   (1) an event-kind claim per subject `claim_subjects` names (`predicate = e.kind, value = True`);
   (2) one claim per `Observation` the fold made, in the `requires` vocabulary (`stores:<kind>`,
   `condition`, …), to the actor alone at the shipped `observation_deposit_mode`;
   (3) one `seen` claim whose value is `epistemic.Seen(stratum, marks, who, why)`, terms masked per channel;
   (4) a `content:<kind>` claim to whoever came to hold a Record this tick;
   (5) for `news.told`, the told claim — the `Said` the teller fixed at CHOOSE, lossy at `Partial`
   (`_told_value`), source `told_by`, `chain = teller's chain + (teller,)`, confidence refracted
   (`_refract`) and credited by shared regime (`_credit`);
   (6) the found deposit (`_found_claims`) for a graded inquiry that uncovered a covert deed's trail.
   It then evicts over `ledger_cap` through the gate. It owns no state but the ledger writes.
2. **The channel and knowability rules** — `engine/season/epistemic.py`: the five `_ch_*` predicates
   (`co_located`, `witness_key`, `document_key`, `chronicle`, `post_remit`), built into `CHANNEL_PREDICATES`
   from `rosters.yaml: witness_channels`; `observers_for` (one strongest channel per person);
   `claim_subjects` (what a deposit is about); `Seen` and its term readers; `trail_of` / `holds_trail`
   (what an inquiry can still uncover); and `belief_contradicts` — the single place a person's own ledger
   can refuse a candidate (§F1 clause 4), called by bare name from `decision/options.py::opening_set`.
3. **The information verbs** — `engine/season/loop/effects_information.py` (records, propositions,
   matters: `create_record`, `issue`, `give`, `forge`, `survey`, `conceal`, `seize`, `petition`, `carry`,
   `open_case`, `determine`, `convene`, `argue`, `utter`, …) and the six investigation acts as
   `verb_table.yaml` rows (`examine`, `interview`, `research`, `surveil`, `thread_read`, `reconstruct`),
   whose graded band reaches the registered module `modules/fieldwork/find.py` through the `inquiry`
   composition role (`seam/wrappers/fieldwork.py`).

Beside these: `queries/person_q.py` (the ledger readers — `LedgerReader`, `said_of`, `regard`,
`ledger_names`, `drifted`, `deeds_judged`), `queries/inputs.py` (the typed input records a host builds for a
module entry), and `systems/fieldwork/sim/knots.py` (a Knot lifecycle oracle the season loop does not call).

**How a decision reads it.** `loop/driver.py::_questions_at_barrier` calls
`queries/world_q.py::questions_for(w, p, since)` for every person at barrier 2 — a RESOLVER-SIDE function that
takes the `World` — and hands the `Question[]` to `loop/deliberate.py`, which builds a `View`
(ids + questions + one `odds` callable) and calls `choose(p, v, s, ask_budget)`. `decision/` names no `World`
(the `View.__getattr__` raises `Forbidden`). So what a person may act on is: his own `Person` (ledger,
`tenures`, body, pursuits), the `Question[]` the projection built for him, and `Fixtures`.

### 1a. Execution evidence (what ran and what it showed)

All on `harness/populated.py::build_realm(seed)` (83 persons, 34 offices), the shipped fixtures and the
shipped chooser (`probes.chooser(w, verbs=resolvable_verbs())`), `PYTHONHASHSEED=0`. Probe scripts and raw
output: scratchpad `runs/FI/` (`r08_probe.py`, `dynamics.py`, `*.out`). §12 lists every run.

**One season, seed 0** (`dynamics.py 0 1`; 13,379 Events, 749 folded acts; the instrumented run's content
hash is compared with an un-instrumented `populated.run` in §12):

| reading | value |
|---|---|
| claims held, by source | `firsthand` 6,014 · `told_by` 6,040 · `inferred` 297 (12,351; largest ledger 271 against a cap of 3,200) |
| of the 6,040 `told_by`, claims that carry a teller (`Claim.chain` non-empty) | **7** — the other 6,033 came by a channel with no speaker (`chronicle`'s realm-wide broadcast, and `document_key`), not by anything a person said |
| tellings | `news.told` 2 (both `Partial`), `news.untold` 4, `tell.refused` 20; `lie` folded 2, `tell` folded 4 |
| told chain lengths | `{1: 7}` — no claim was retold (hearsay of hearsay: 0) |
| cell claims (a `stores:`/`condition`-class value) against the world at the end of the run | firsthand 701 true / 5 false · inferred 256 true / 14 false · **told 0 true / 7 false** |
| clause 4 (`belief_contradicts` from `opening_set`) | 20,080 calls, 461 declines; the world agreed (`requires` false) in **460 of 461** |
| a teller's record with a hearer (`decision/options.py::record`) | 7 (hearer, teller) pairs: 4 below 1.0, 3 never checked |
| covert deeds and inquiries | `record.forged` 16 (`forge.refused` 15), `cover.assumed` 11, `finding.made` 62, `finding.none` 59; found deposits: 0 trail uncovered (the driver's `findings` store empty at the end; the tree's own test pins the seed-0 realm at "reaches no find") |
| acts by what occasioned their scene | `need` 121 · a firsthand claim landing 654 · a `told_by` claim landing 31 · an `inferred` claim 15 |
| chosen acts whose SUBJECT the actor held no claim about, was not, and did not hold an edge on | **81 of 1,977 chosen (30 of 749 folded)** |

Seeds 1 and 2 (one season) and seed 0 at two seasons are in §12.

**The unwitnessed-fact probe** (`r08_probe.py`, tick 0, before any season) is F-FI-01's falsifier; its
result is stated there.

## 2. Steelman

Ranked by the weight each bears. Each was attacked; what survived is stated.

1. **Knowledge is a per-holder ledger written at one barrier, and nothing else is knowledge.** Every deposit
   ends in one gated write (`loop/witness.py::_deposit`), into the holder's own `Person.ledger`, caused by the
   witnessed Event (`causes=[e.id]`), so a belief has an antecedent and a provenance and no second store of
   "what is known" exists. *Attack:* count a claim held by someone the channels did not admit. *Outcome:*
   none found; the controlled arm is the tree's own (`total` against `all_five`,
   `test_r7_two_persons_hold_different_things_and_at_total_they_cannot`). **Holds** for claims. It does not
   cover referents (F-FI-01), which are not claims.
2. **The decision side is typed away from the world.** `decision/` takes `Person`, `View`, `Question`,
   `Fixtures`; `View.__getattr__` raises on any world reach (`state/carriers.py:504-509`); clause 4 reads
   the person's ledger with UNKNOWN ≠ False (`epistemic.py:131-134`), so a person with no belief still tries,
   and the fold refuses him. *Attack:* the unwitnessed-fact probe. *Outcome:* the type holds and the
   information leaks around it, through `questions_for`, which is built with the World and handed in
   (F-FI-01). **Holds as a structure; fails as the claim R-07/R-08 make of it.**
3. **Hearsay is graded at read, by who told you, how many hops, and whether he has been right**
   (`decision/options.py::teller_weight`, `record`; `queries/person_q.py::LedgerReader._support`, a noisy-OR
   over distinct origins). This is the right model for rumour: one origin heard twice is one witness, two
   origins corroborate, a contradicted teller is credited less on the next cell, and nothing is frozen at
   deposit but the channel and the prior (`refracted_confidence`). *Attack:* is any of it exercised?
   *Outcome:* `record` returned a value other than 1.0 for 4 of 7 pairs at seed 0 and for no pair at seeds 1
   and 2 (no told claim exists there); no two-hop chain exists in any run. **Holds as mechanism, dormant as
   behaviour** (F-FI-02).
4. **A document is a belief with no attribution, so a forgery is playable** (`loop/witness.py`, the fourth
   deposit; `_eff_forge`; `Record.forgery_quality` read by the examination's obstacle). A holder cannot tell
   a forged sheet from a true one by construction, and what the forgery falsifies is exactly the key a
   reader acts on (`_FORGED_SHEET_KEY`, read off the roster). *Attack:* does a forged sheet reach a second
   holder, and is one found? *Outcome:* `record.forged` 16 / 19 / 17 a season, `record.given` 0 / 1 / 0,
   found deposits 0 / 0 / 0. **Holds as a design object; the loop it belongs to does not close** (F-FI-03).
5. **Investigation was not forced into the contest seam** (Jordan, SM-3: *"investigation is not a contest
   seam. it is its own thing"*; `rosters.yaml`'s `inquiry_modules`; `graded_inquiries` rolls through the one
   roll owner with no prize). One roll owner, one ladder, a second role with its own typed records
   (`queries/inputs.py::FieldworkInput`, `Findings`), reached by composition row. *Attack:* is the module a
   resolver or a lookup? *Outcome:* a lookup (`modules/fieldwork/find.py:28-34`), and it says so. **Holds as
   architecture; it is a seam with nothing behind it.**
6. **Every assumption is a named, swept fixture with its control arm** (`fan_out_mode`,
   `observation_deposit_mode`, `refraction_gain`, `regime_gain`, `telling_privacy`, `told_drift_band`,
   `lie_offered`, `said_slant`, `default_forgery_quality`). *Attack:* is a shipped arm a fake control?
   *Outcome:* `telling_privacy` 0, `said_slant: newest` and `competence_gain` 0 ship at the control, so
   confidences, slant and competence are built and off; the told-claim population is too small for any told
   arm to separate (the knowledge-model plan measured the same and said so). **Holds**, with the caveat that
   a sweep over an empty population measures nothing.

## 3. Adversarial findings

### F-FI-01 · blocks a requirement (R-07, R-08) · A person's candidates move on a fact he has not witnessed or been told

**Claim.** `requirements.yaml` R-08 opens *"NON-OMNISCIENCE HOLDS, structurally (see R-07)"* and R-07 opens
*"IMPERFECT KNOWLEDGE IS STRUCTURAL AND HOLDS"*. Both are true of the access path and false of the content:
`queries/world_q.py::questions_for` reads world truth with no claim behind it and hands the result to the
chooser as referents.

**The reads (opened at the line).** In `engine/season/queries/world_q.py`:
`goal_referents` `:2836` — a `seat_holders` goal's referents are *"the persons now holding any listed seat (a
live `hold`, `w.tenures` order)"*, and its own docstring says *"`seat_holders` IS A WORLD READ WITH NO CLAIM
BEHIND IT ... it hands `p` the identity of whoever sits on a throne he may never have been told of"*;
`vacancies` `:3121` — every Office with no live `hold` that a conferrer's seat may fill;
`aim_state` `:2986` — *"the shipped rule reads the world alone"*;
`matters_awaiting` `:3633` and `holdings_to_found` `:3524` — *"world-read ... NOT gated on his ledger"*;
`questions_for` clause 2 `:4135` — `place_of(w, c.subject)`, where the subject of a held claim is NOW;
`attention_key` `:3857` orders the questions with the World. The tree names the class itself (*"the tree's
own `in tension with AX-7` shape"*, `world_q.py:3610`).

**Falsifier run** (`r08_probe.py`; `build_realm(s)`, s = 0, 1, 2, tick 0; the three builds are identical for
these facts, so this is one world read three times, not three samples). A tenure is edited directly on the
World: no Event, no WITNESS; the subject's ledger and own tenures are compared before and after.

| arm | questions moved | candidates moved | subject's ledger / tenures |
|---|---|---|---|
| control: no edit | no | no | identical |
| control: an unrelated seat (`off_archbishops_rep`) changes hands far from the subject | no | no | identical |
| **P1** `p_npc_088` (goal `goal_restoration_evade_capture`, about the holders of `off_cardinal_justice`); the seat passes from `p_npc_038` to `cohort_set_s_001`; subject at `b_s_026_workshop`, both holders elsewhere; his ledger (3 claims) names neither | **yes** | **yes**: 44 → 43 candidates; the eight lost that the probe prints all name `p_npc_038`, the eight gained all name `cohort_set_s_001` (`challenge`, `interview`, `petition`, `forge`, `move`, …) | identical |
| **P2** `p_npc_020` (King; `confer` through `off_king`); `off_archbishops_rep` silently vacated at `b_s_036_cathedral`, subject at `b_s_002_cottage` | **yes** | **yes**: 152 → 180 candidates, none lost; the eight gained that the probe prints are all `confer` on the vacated seat | identical |

**In computed play** (`dynamics.py`, the chooser wrapped; a subject is "unsourced" when the actor is not it,
holds no live edge on it, his ledger names it by neither `ledger_names` nor `known_persons`, and it is not on
his own home ladder): 81 / 82 / 84 chosen acts at seeds 0 / 1 / 2 in season 1 (of 1,977 / 2,034 / 1,960), of
which 30 / 32 / 29 folded; verbs at seed 0: `petition` 8, `reconstruct` 7, `create_record` 6, `transfer` 6,
`exchange` 5, `interview` 5, `surveil` 5, `forge` 4, `move` 4, `survey` 4, `tend` 4, `utter` 4, others ≤ 3.
At seed 0 the two-season total is still 81: season 2 added none. So the footprint in the realm is about 4%
of season-1 choices and falls to nothing once the broadcast channel has named everyone; the mechanism is
unconditional (the probe).

**What the tree already decided.** `registers/editorial_ledger_in.jsonl`, ED-IN-0292, last row (2026-10-26,
`status: closed`): item (2) *"TAKEN at ladder step 5 (A1-02, TAKEN-ARCH): a vacancy reaches a person as a
claim deposited through the channels, not as a world stamp; AX-7 ... prohibits the engine's resolution being
handed into belief unmediated, which the stamp (`world_q.vacancies`) is."* The code at HEAD still stamps
(P2), and `goal_referents`' docstring reads that closing row backwards (*"THAT PRECEDENT WAS TAKEN ... and
this read follows that answer"*). `workplans/valoria_master_workplan_v11_part11.md:39` (G-18) grades the
state correctly: the claim route ABSENT-RUN, the world read PRESENT-USED. Since the decision, three more
stampers were added on `vacancies`' precedent (`matters_awaiting`, `holdings_to_found`, `aim_state`).

**Test strength.** R-07's `measure:` is `-k 'choose_receives_no_world or a_view or r7_two_persons'`: the
first two assert a type, the third compares deposited claims. None can observe a referent that entered with
no claim (§0.1 pt 2). The row's status rests on an instrument that cannot see this failure.

**Requirements touched.** R-07 (imperfect knowledge), R-08 (non-omniscient decisions).
**Narrative consequence.** A conspirator's quarry is re-targeted the instant a seat changes hands in another
duchy; a King fills a vacancy nobody has reported to him. The succession, the usurpation heard late, the
order sent to a dead man: the stories that need news to travel cannot occur where the engine supplies the
news for free. It also hides F-FI-02: because referents arrive without telling, nothing in the realm needs
`tell` in order to act.
**Minimal fix at the owner.** `proposals/08_FI_01_claim-sourced-referents.md`: `goal_referents`' own stated
revert (holders the person's ledger names), `vacancies` filtered by `ledger_names`, a world-gen deposit so
the realm does not start blind, and the R-07/R-08 text corrected. It is the decision already taken, built.

### F-FI-02 · degrades narrative (R-01, R-07) · Nothing a person knows reaches another person by a person's act; `told_by` is a broadcast

**Claim.** Rumour, the carrier the whole epistemic design exists for, does not run in computed play.
**Evidence** (`dynamics.py`, one season, seeds 0 / 1 / 2): `tell` folded 4 / 10 / 2 and `lie` 2 / 3 / 0;
`tell.refused` 20 / 43 / 4; `news.untold` 4 / 12 / 2; `news.told` 2 / 1 / 0, every one `Partial`. Claims held
with a teller on them (`Claim.chain` non-empty): **7 / 0 / 0**, of 6,040 / 4,049 / 3,746 `told_by` claims; the
rest are `chronicle` deposits (`epistemic.py::_ch_chronicle` `:649`, which *"DOES NOT READ `pid`"*). Chain
lengths `{1: 7}`: no retelling. At seed 0, two seasons: 12 chained claims, all one hop. The tree's own
readings agree (`hole_register.yaml` H-272: 114 one-hop and 0 two-hop over 800 `tell` acts in 13 worlds;
`research/game_precedent_suite/dispositions/D_T06.md` probe: chained claims alive 0 / 0 / 1).
**Why, by reading the call sites.** (i) `tell` forms for every person the teller knows of
(`known_persons`) and is refused when the hearer is elsewhere, because where another person is, is the
world's to answer (`data/requires.py: WORLD_ONLY_STEMS`); the teller cannot decline it and pays the scene.
(ii) `tell` is contested (`a standing`) at the default pool, and most admitted tellings are `news.untold`.
(iii) `queries/person_q.py::said_of` `:1165` passes on the teller's newest non-`seen` claim about the
subject, which a co-located hearer usually already holds, so the exact-triple guard
(`loop/witness.py:958-960`) drops the deposit: at seed 1 one `news.told` produced no told claim. (iv) After a
telling, the hearer's newest claim about the topic is his own event-kind claim `(topic, news.told, True)`, so
that is what he would retell (H-272, H-204).
**Falsifier.** A run in which chained claims with two or more hops exist at the shipped fixtures; none in
seeds 0–2, nor in the two other readings cited.
**Requirements.** R-01 (propagation: it is met by the broadcast and by presence, not by speech), R-07.
**Narrative consequence.** No whisper network, no garbled report arriving at third hand, no informant whose
value is what he alone heard. The provenance chain, hop discount, noisy-OR and teller's record have no input.
**Minimal fix.** `proposals/08_FI_02_rumour-that-travels.md`: a third `said_slants` arm, at the one owner
(`said_of`), that never passes on the transport's own event kinds and prefers what the room did not see; and
the paired deletion of `chronicle` that B10-14's CR-29 already schedules, taken first rather than third.

### F-FI-03 · blocks standalone play; degrades narrative (R-05) · Investigation resolves and does not play

**Claim.** There is no investigation game: no case, no conclusion, no stake, no end, and the one findable
trail is unreachable in the seeded realm.
**Evidence.** `modules/fieldwork/find.py:28-34` is the whole module: `inp.terms[inp.band]` applied to
`inp.items`. `rosters.yaml: covert_kinds` has one member, `record.forged`; `epistemic.py::trail_of` `:368`
says of itself *"REACHABLE ONLY THROUGH A PLANT"*. Runs: found deposits 0 at seeds 0 / 1 / 2 while
`record.forged` is 16 / 19 / 17 and `finding.made` 62 / 58 / 62 (the tree pins the same:
`test_fi03_trail.py::test_the_realm_seed_twice_in_one_process_gives_one_hash_and_reaches_no_find`; H-316).
`interview`, `reconstruct` and `thread_read` carry no bands and no `writes:` (`verb_table.yaml`), so a
`finding.made` from them deposits the event-kind claim and nothing else: 19 / 8 / 19, 47 / 45 / 54 and
2 / 1 / 0 folded acts a season that teach nobody anything (H-218, H-315, H-331; H-320: each repeat mints the
same claim again). `examine` folded 0 times at seeds 0 and 1. A `Partial` find closes the trail to a later,
better one (`holds_trail` `:336`; H-314, pinned by a test), and a claim at confidence 0 still closes it
(H-341). There is no act that states a conclusion (`reconstruct` writes nothing), none that tests a told
claim (H-271), no accusation whose correctness anything later reads (D_T06 rows 16, 23, 37, 38).
**Falsifier.** A seeded run with a found deposit; a verb row whose band writes a conclusion. Neither exists.
**Requirements.** R-05 (three of six inquiry rows are "built out on execution" with nothing to execute),
R-09 (three inquiries are graded; three are not).
**Narrative consequence.** The Bellarmine case the corpus asks for (NPC-004: a confident wrong conclusion
acted on as true) cannot occur: there is no conclusion to be wrong.
**Minimal fix.** `proposals/08_FI_03_playable-inquiry.md` (a scenario fixture, a conclusion that is a
Proposition the investigator utters, an accusation by the existing `petition` → `carry` → `determine`
route, and the world answering by consequence), on top of B10-14 as written.

### F-FI-04 · degrades narrative (R-07, R-08) · A lie deceives only those it changes nothing for, and is caught only by those it cannot deceive

**Claim.** The false-belief loop has formation and a private exposure reader, and no spread, no public
exposure and no behavioural stake.
**Evidence.** Formation: `lie` folded 2 / 3 / 0; all 7 told cell claims at seed 0 are false against the
world at the end of the season (10 of 11 at two seasons), from the cell lie (`lie_said_of`) and the `Partial`
drift (`_told_value`). Exposure: `decision/options.py::record` `:1727` pairs a told cell against the hearer's
own firsthand claim on the same cell; it read below 1.0 for 4 of 7 pairs at seed 0 (5 of 12 at two seasons).
That pairing exists only where the hearer already holds the cell firsthand, and there `LedgerReader` ranks his
own claim (weight 1.0) above the told one (`told_weight ** hops`), so the lie does not move him. Where he
holds nothing, the lie lands, and nothing can check it (H-271). Being caught writes nothing: no Event, no
stance, no claim about the liar; the liar never learns it and no third party can (`record` is computed at
read, per hearer). Behaviour: clause 4 declined 461 / 445 / 485 candidates and the world disagreed with the
belief in 1 / 2 / 1 (7 of 1,903 at two seasons, when stale readings accumulate: firsthand cells false 73 of
1,208, `inferred` 270 of 270).
**Falsifier.** An act formed or declined on a told-false cell, with the liar's standing moved by it. One
decline in 461 is the closest reading; no liar is affected.
**Requirements.** R-07, R-08 (a character acting wrongly on what he was told is the row's own subject).
**Narrative consequence.** Deception is a private arithmetic adjustment. Nobody is disgraced, no one is
misled into a march, and the hearer who was fooled is, by construction, the one who cannot find out.
**Minimal fix.** Two edits carried by `proposals/08_FI_03`: an inquiry's graded success deposits the cells
of what it examined firsthand (the W-B observation deposit that already exists, so `record` gains its pair
after the fact: checking is investigating), and a `record` falling below 1.0 for the first time is a
landed claim about the teller (`deed:lie` on `person_predicates`' side), which Q2 already turns into a
question. Design-first where it prices the liar (CR-83 is the plan's home for it).

### F-FI-05 · degrades narrative (R-07) · The largest single source of what people hold is a channel that reads no person

**Claim.** `told_by` claims with no teller are 49% / 39% / 37% of all claims held after one season (6,033 of
12,351; 4,049 of 10,395; 3,746 of 10,203). Two channels mint them, `chronicle` and `document_key`; this
audit did not split them [UNVERIFIED split], and the tree's own arm found `chronicle` the only one minting
`told_by` in the realm at `29af7354`. `chronicle` deposits every Event of a kind a `binding_decision` row
emits into every living person, across every border (at confidence 67 by the refraction arithmetic, the
figure H-333 also records).
**Evidence.** `epistemic.py:685-686`; the docstring's own arm (`told_by` 879 → 0 with the predicate forced
`False`); H-214 (deletion held for want of the replacement); H-333 (an `argue`'s `pursuit.moved` reaches
people who were not there, because the kind is shared with `determine`); H-351 (no channel reads faction).
**Status.** Known and scheduled: B10-14's CR-29 (the event-kind reach channel, then `chronicle`'s paired
deletion). Not re-raised. What this audit adds is the share, and the ordering consequence: while a
broadcast names everyone to everyone, F-FI-01's leak is invisible after season 1 and F-FI-02's silence
costs nothing, so CR-29 is the precondition for measuring either fix.
**Minimal fix.** Take CR-29 first in B10-14's order (it is third).

### F-FI-06 · degrades narrative (R-07) · Nothing said can be private, and nothing hidden can be found

**Claim.** Concealment, the third leg of the charge, has two halves and neither closes.
**Evidence.** Speech: a telling deposits its content into everyone co-located, not the addressee (H-323:
bystander told 18 of 18); the confidence circle exists (`_circle_of`) and ships off (`telling_privacy` 0), and
its break path is unreachable at the shipped slant (H-204), so `confidence.broken` is 0 in every run here.
Deeds: `conceal` folded 11 / 22 / 8 a season, minting a `cover` Record that re-anchors the actor's later acts
for the far channels only; those present still read `seen.who` (H-324); no inquiry can uncover a cover
(`covert_kinds` holds `record.forged` alone).
**Status.** The deed half is scheduled (B10-14: CP-T06-09, -01, -02, -07). The speech half is not: a private
telling was ruled out of scope once (*"private whispers are not built"*, `_circle_of`'s docstring, §10
decision 1) and stands; accepted as binding.
**Minimal fix.** None beyond B10-14 for deeds. For speech, the shipped arm of `telling_privacy` is a design
value with a control; flipping it is pointless until F-FI-02 gives a confided claim a route to be retold.

### F-FI-07 · hygiene, with a determinism edge · `systems/fieldwork/sim/knots.py` holds state, draws unseeded, and cites a path that does not exist

**Evidence.** Module-level registry `_knots` and counter (`knots.py:156-157`); `rng = random.Random()` when
none is passed (`:219-221`), an unseeded draw; *"Canon source: systems/fieldwork/reference/knots_v30.md"*
(`:4`) names a file that is now under `.designs/` and is not canon; a self-knot forms (H-332); its only
callers are `engine/tests/test_knots_ed912.py` and two tools. The season's `knot` is a Tenure kind read by
`_ch_witness_key`; `tie / knot` has no effect (H-182: formed for 83 persons, executed 0), and
`thread_read` reads no bond (H-331).
**Requirements.** None directly; R-06/R-07's "relationships" has no producer here.
**Minimal fix.** Three text edits and one refusal, in `proposals/08_FI_04_small-edits.md`; the knot's
season form waits on `_eff_tie` (plan position `14`), which is CHAR's.

### F-FI-08 · hygiene · Event kinds and register rows that say something other than what happened

`finding.none` covers a refusal, an impossible task and a rolled failure; `finding.made` from an ungraded
row means "the act was admitted" (H-318). `argument.won` at `Partial` changes nothing (H-269). Register rows
H-42, H-43, H-45, H-84 are closed in code and carry open-looking heads; H-116's head still describes the
severed feedback edge that W-A/W-B closed (clause 4 fired 461 times in one season here). `HANDOFF_FI.md`
points ED-FI-0002 at the live ledger; the research file (`research/by_lane/FI_fieldwork_investigation.md`
§0 item 11) records that it lives in the archive ledger [UNVERIFIED by this audit]. Resolutions in §6.

## 4. Code matters

**Ownership and duplication.** Single owners hold where it matters: one gated deposit (`_deposit`), one cap
body (`_cap`), one comparator (`LedgerReader._best`), one pairing step (`options._pair`), one drift rule
(`person_q.drifted`, shared by the liar and the lossy copy), one "what is this deposit about"
(`claim_subjects`, with `_hold_tenure_ends` shared by three readers), one mint (`_mint_document`). Two
second owners remain. (a) *What a person may be asked about* has a ledger-sourced family (`seats_named`,
`places_named`, `propositions_heard`, `larders_in_purview`' named half) and a world-sourced family
(`vacancies`, `seat_holders`, `aim_state`, `matters_awaiting`, `holdings_to_found`) inside one function,
with no field on `Question` that says which a referent is (F-FI-01). (b) `said_of` and `LedgerReader` both
answer "what does this person hold about X", unweighed in one and weighed in the other; the knowledge-model
plan already sends `said_of`'s weighing to CR-83.

**Dead or unreached code** (each by a run, §12): the found deposit (`_found_claims`) executes 0 times in the
seeded realm at seeds 0–2; the confidence circle (`_circle_of`) takes no draw at the shipped 0;
`competence` returns 1.0 for every person (no authored Attunement, gain 0); `rank` returns 0 by its own
`ABSENT` marker; `_term_why` returns `None` always; the `post_remit` predicate credits few (`inferred` 297 /
297 / 324 claims come from the IN-22 purview limb and the found slot's borrowed source, not from an obligee
at his post [UNVERIFIED split]); `systems/fieldwork/sim/knots.py` has no production caller. None of these is
a deletion candidate except by the plan positions that own them; they are listed because a reader of the
file would take them for running behaviour.

**Contract and seam fidelity.** `references/module_contracts.yaml:120-123` registers `fieldwork.find`
(`modules.fieldwork.find:find`, `step_call`); the module imports only the record types, takes no World and
no RNG, holds no state, and its adapter refuses any return that is not `Findings`
(`seam/wrappers/fieldwork.py`). It conforms to `holonic_ARCHITECTURE.md` §45 as far as a 7-line entry can.
The same contracts file still describes the module by `knots_v30.md` state (`Evidence Track`,
`Disposition Track`, `resolver: dice_pool`; `:329-362`), which is the unplugged oracle's, not `find`'s: the
contract row and the registered entry describe two different things. Against
`04_CODE_ARCHITECTURE.md` §A.2: `epistemic.py` is not one of the nine modules (its own docstring says so);
`loop/witness`'s may-read cell (`04:178`: *"this tick's log, presence cache, channel predicates, the act
store"*) is exceeded five times, each declared at the top of `witness.py` as CONVENTION: it imports
`decision/` (refraction), reads every ledger's id set, a driver-held `findings` store, older ticks' Events,
and two persons' convictions. A row exceeded five times by declared convention has stopped binding
(§11, item 1).

**Determinism.** The lossy copy and the liar spend no draw (the selection reuses the claim id's hash);
`_circle_of` keys its one draw on the telling's id; the instrumented and plain runs here hash identically
(`5ab73af2…`, seed 0, one season), so a read-only wrap of `belief_contradicts` and the chooser perturbs
nothing. The one unseeded draw in scope is `knots.py:219-221` (F-FI-07), outside the season loop.

**Test strength.** `test_told_by_channel.py` (2,343 lines) and `test_fi03_trail.py` (868) are built with
controls and mutation arms, and several pin a limit rather than a behaviour (`..._reaches_no_find`,
`test_a_partial_find_closes_the_same_trail_to_a_later_better_one`, `test_g6_limit_...`): honest, and it means
the suite is green over a mechanism that does not occur. R-07's `measure:` cannot observe F-FI-01 (stated
there). No test asserts that a told claim with two hops exists in a seeded run, so H-272's state is unpinned
in either direction.

**Performance.** One realm season took 40–46 s of CPU here; WITNESS's fan is persons × Events with five
predicates each, and `establishment_of` rescans `w.tenures` per call by ruling. At 13,379 Events a season
the cost is the broadcast: speakerless `told_by` claims are a third to a half of everything held, each a
gated write with its own `claim.deposited` Event. CR-29 is also the performance fix.

## 5. Design matters

**Agree (intent, ruling and code).** Claims live in the holder's ledger and nobody else reads them;
investigation is its own role, not a contest (SM-3); no verifier and no truth oracle for a conclusion
(the world answers by consequence, Q5 of the 2026-08-18 rulings); a document carries no attribution;
hearsay is graded at read (CAT-3) with distinct origins corroborating and one origin counted once
(ED-IN-0320 to 0323, built); knowledge is kept for years (ED-IN-0319; `ledger_cap` 3,200). These are
accepted as binding and none is re-raised.

**Disagree, and the game follows the code.**
- *A vacancy reaches a person as a claim* (ED-IN-0292 last row, TAKEN-ARCH) against `vacancies` and four
  siblings reading the world. Cost: F-FI-01. The code is the defect; the decision stands.
- *"Rumours with provenance"* as the realm's information economy (the 2026-08-18 epistemic proposal's
  premise, and r2 `02` §A.10's lossy copy) against 0–7 told claims a season. The design assumes a volume
  the chooser does not produce. Cost: every told-side fixture is a sweep over an empty set.
- *Six investigation acts* against three that roll and three that write and deposit nothing. The game
  follows the code: `interview`, `reconstruct`, `thread_read` are scene sinks.
- *A telling is addressed* (`to`) against a deposit into the room (H-323). Deliberate (hearing by
  presence); the cost is that secrecy has no carrier, and it is accepted with the ruling that private
  whispers are not built.

**NERS readings of the design objects** (definitions `CLAUDE.md` §0.06; E last, as a ratio).
- *The witness channels + per-holder ledger.* N: removing it removes every asymmetry of knowledge; holds
  top-down (R-07), bottom-up (every deposit one write), lateral (CHAR's regard, SC's reception and proofs
  read it), vertical (a seat's purview limb). R: the no-player half is where it is thin (F-FI-02): the world
  does not gossip. S: one deposit rule, one comparator; *pauses correctly* is untested for a played scene.
  E against that: high: one barrier, six deposit shapes, all the same carrier. **Survives.** A cut would
  lose the only place imperfect knowledge is real.
- *`chronicle`.* N fails from four of six directions: it is defined by a verb stratum, not by anything
  about the witness (bottom-up), it makes distance and borders irrelevant (lateral, diagonal), and it masks
  two defects (top-down). What dies with it is the realm hearing of a death or a seat changing hands, which
  CR-29 keeps by kind. **Fails; the cut is scheduled.**
- *World-stamped referents (`vacancies` and siblings).* N as a mechanism: a conferrer must learn of a
  vacancy somehow, and world-gen ledgers are nearly empty. But it is defined against R-07/R-08's own
  statement and holds only bottom-up (it makes `confer` form). **Fails as built; survives as a claim.**
- *`reconstruct`, `interview`, `thread_read` as written.* R fails on completeness (*"fully formed,
  error-free, and complete opportunities"*): 47–54 `reconstruct` acts a season produce nothing. E as a
  ratio is zero: overhead with no outcome to intuit. **Fail; each needs a product or to leave formation.**
- *The cell lie (`lie`, `lie_said_of`, `record`).* S is good (one drift rule, one pairing step, no draw).
  R fails on both halves: no stake for a player's lie, no drama without one (F-FI-04). **Survives a cut
  only with its consequence built**; alone it is arithmetic.
- *The knot (`witness_key`, `tie / knot`, `knots.py`).* Two ladders for one quantity (the oracle's strain
  gauge and the season's undegreed Tenure): an S defect by definition, and the season's half has no
  producer. **Not yet a design object in the game.**

**Prose only, therefore not game.** The Evidence Track, Depth axis, Desperate Trail, Dialogue Lattice,
Response Matrix, Case Board, Cover/Exposure, points of interest and discovery (`fieldwork_v30.md`,
`investigation_systems_v30.md`; archived, not canon). The research lane file records the archived corpus
as GM-dependent in four places and internally contradictory in seventeen; nothing here should be built
from it without a new design. 59 of the 143 corpus cases name one of these terms in a need (§13).

## 6. Hole-register and workplan disposition, and resolutions

### 6a. Hole-register rows (primary to this dossier)

Read at the register line through a compact dump (each row's `hole`, `default`, `unblocks` and the head of
`cite`; the long `cite` tails of H-33, H-55, H-122, H-169, H-182, H-197 and H-222 were read in part:
`[PARTIAL READ]`). "Verified" is against code or a run in §12, not against the row's own text.

| id | listed | verified | evidence | action |
|---|---|---|---|---|
| H-22 | ruled, open? | closed but for `ttl` | `Record.ttl` has no reader (`_eff_destroy_record` docstring; H-259) | R-24 |
| H-33 | assumption | open as an assumption; `all_five` is the ruled default | `fan_out_mode="all_five"`, `fixtures.py:421` | none; CR-29 changes the fifth channel |
| H-42 | closed? | closed | `_eff_utter`; `utter` folded 73 / 69 / 68 | none |
| H-43 | closed? | closed | `_mint_document` is the one mint | none |
| H-45 | closed? | closed as rows; three rows have no product | `verb_table.yaml` rows; F-FI-03 | R-07, R-08 |
| H-55 | closed? | closed (measured) | `observers_for` read at every WITNESS | none |
| H-62 | absent | open; wrongly filed (CHAR: interior writes) | — | CHAR lane |
| H-72 | closed? | closed | clause 4 declined 461 / 445 / 485 | none |
| H-79 | assumption | open as an assumption (`both` ships) | `claim_subjects` | none |
| H-84 | closed? | closed; `give` rare in play | `record.given` 0 / 1 / 0 | see H-316 |
| H-92 | absent | open; wrongly filed (CHAR: `decision/budget.py`) | a held Record or Proposition is a `hold`; `budget` counts every live `hold` | R-22 |
| H-104 | measured | closed as a bound; not exercised at the shipped cap in two seasons | largest ledger 271 (535 at two seasons) against 3,200 | none |
| H-106 | absent | open; wrongly filed (IN: loop enumeration) | — | IN lane |
| H-111 | assumption | open; answered by the plan | B10-14 CP-T06-04 | R-09 |
| H-112 | measured | closed as a bound | `World.write` MATTER-only buffer [not re-run] | none |
| H-138 | measured | open, latent; wrongly filed (economy) and its cite names a moved function | `_eff_transfer` is not in `effects_information.py` | WR/SE lane; fix the cite |
| H-116 | measured, open? | closed; the head describes the tree before W-A/W-B | clause 4 fires (above) | R-16 |
| H-122 | assumption | open as an assumption (`actor` ships) | `fixtures.py:584` | none |
| H-155 | assumption | open; unsweepable at this volume | `news.told` 2 / 1 / 0 a season | after R-05 |
| H-157 | measured | closed | `teller_weight` reads `Claim.chain` | none |
| H-162 | measured | SC's; writer built, no reader | — | SC lane |
| H-169 | measured | partly closed (`forge`, `destroy_record` built since); open: a sheet's content is unbounded | `_eff_forge`; `_eff_survey` docstring | design-first, unchanged |
| H-173 | assumption | closed by delegated ruling (no distinct reading) | row's own `default:` | none |
| H-182 | absent | open; CHAR's (`_eff_tie`, position `14`) | `tie / knot` has no effect | CHAR lane |
| H-197 | closed? | open as an assumption; ships at the control | `telling_privacy=0.0` | after R-05 |
| H-210 | closed? | open as an assumption; CR-94 scheduled | B10-14 | none |
| H-214 | measured | superseded by the plan | B10-14 CR-29 | R-06 |
| H-217 | measured | open; wrongly filed (SC/FA: succession) | — | SC lane |
| H-218 | closed? | superseded in both halves (its own cite); residue open | K-36, K-37; CP-T06-05 | R-07, R-08 |
| H-219 | absent | SC's; stopped | — | SC lane |
| H-222 | closed? | built, never fires; irrelevant until a `person_predicates` producer exists | `standing_of` returns the maximum for everyone | none (R-21) |
| H-231 | measured | open | `event_place` None for a razing; `_hold_tenure_ends` expands `hold` only | R-23 |
| H-234 | measured, ruling | answered by the plan's reach channel | CR-29's roster row keyed on event kind | R-18 |
| H-259 | measured | open | `issue` mints with no end | R-24 |
| H-267 | measured, ruling | SC's; answered by precedent (`speak`'s `reception`) | `SocialContestInput.reception` | SC lane, R-25 |
| H-269 | measured | open (name) | `argue` `Partial` emits `argument.won` | R-11 |
| H-275 | assumption | open as an assumption; unsweepable at this volume | 7 / 0 / 0 told claims | after R-05 |
| H-279, H-285, H-295, H-299, H-301, H-302 | measured | SC/FA's; filed here by path (`effects_information.py`) | — | SC, FA lanes |
| H-314 | measured, ruling | superseded by the plan | B10-14 CP-T06-03 | R-09 |
| H-315 | measured | open | one covert kind; three ungraded inquiries | R-07 |
| H-318 | measured | open (name) | `finding.none` for three causes | R-10 |
| H-319 | measured | open | `research`'s cell has no place conjunct | R-12 |
| H-320 | measured | open | repeats mint the same event-kind claim | R-13 |
| H-323 | measured, ruling | closed by ruling (hearing by presence; whispers not built) | `_circle_of` docstring | none |
| H-324 | measured | superseded by the plan | B10-14 CP-T06-09, -07 | none |
| H-325 | measured | open; SE/WR's (exploration) | — | SE lane |
| H-331 | measured | open; T07's | `thread_read` has no bands | B10-15 |
| H-332 | measured | open | F-FI-07 | R-14 |
| H-333 | measured | superseded by the plan | CR-29 deletes the channel that leaks it | R-06 |
| H-335, H-336 | measured | SC's (conversation state); design-only | — | SC lane |
| H-341 | measured | half defect, half ruled | `holds_trail` ignores confidence (defect); `deeds_judged` ignoring it is ED-IN-0320 | R-15 |
| H-345 | measured | closed by ruling (r2 `02` §A.10's lossy copy) | all `news.told` here are `Partial` | none |
| H-351 | measured | closed by precedent: no faction channel | r2's retirement of the place-blind broadcast; `post_remit` is place-bound | R-19 |

Secondary rows that bear on a finding: H-204 and H-272 (R-05), H-271 (R-08), H-316 (R-07), H-230 and H-207
(R-01, R-02), H-198 (the deed lie: stays absent, no deposit can hold a deed false), H-327 (SE's).

### 6b. Workplan positions (B10-14, `workplans/valoria_master_workplan_v11_part3.md:104-125`)

| item | listed | verified | action |
|---|---|---|---|
| CR-94 forgery quality reads Coordination | BUILD | unbuilt (`default_forgery_quality` is a fixture) | keep |
| CP-T06-09 room files a covered deed under the hand | EDIT | unbuilt | keep |
| CR-29 reach channel, then `chronicle`'s deletion | BUILD | unbuilt; `_ch_chronicle` live | **move first** (R-06) |
| CP-T06-01 a deed that writes a place or alias leaves a trail | BUILD | unbuilt; `covert_kinds` has one member | keep |
| CP-T06-03 a `Partial` closes the deed, not the hand | BUILD | unbuilt; the test pins the old behaviour | keep (closes H-314) |
| CP-T06-04 a refused or failed inquiry teaches its actor his reads | EDIT | unbuilt | keep; widen by R-08 |
| CP-T06-02 `surveil` finds covert deeds at the place watched | BUILD | unbuilt | keep |
| CP-T06-07 a cover can borrow another's name | BUILD | unbuilt | keep |
| CP-T06-05 the person questioned answers by his own act | EDIT | unbuilt | keep; R-05 is its precondition (an answer is a telling) |
| CP-T06-08 paper can be burned | HELD on JA-1 | `destroy_record` has its effect; formation withheld | unchanged |
| CR-83 (B10-13 tail; familiarity sets inference) | DESIGN-FIRST | no design file found by this audit [UNVERIFIED] | owns F-FI-04's price |

### 6c. Resolutions (every inconsistency, gap and unclear passage found; decided)

Ladder step: 1 superseded · 2 irrelevant · 3 a design document or plan answers · 4 precedent · 5 what the
architecture needs. Proposal files are under `proposals/2026-11-12-subsystem-audit-suite/proposals/`.

| # | what | kind | resolution (decided) | step | carried by |
|---|---|---|---|---|---|
| R-01 | R-07/R-08 say non-omniscience holds; `questions_for` hands world-read referents | doc against code | the code is the defect; referents about OTHERS' state come from the person's ledger; R-07/R-08 `measured:` text corrected to "holds for claims, not for referents" until built | 1 (ED-IN-0292 last row) | `08_FI_01` |
| R-02 | `goal_referents`' docstring reads ED-IN-0292's closing row as licensing the world read | unclear passage | rewrite to the row's actual answer; take the docstring's own stated revert | 1 | `08_FI_01` |
| R-03 | which stampers may stay world-read | gap (no rule) | a stamp over the person's OWN live edges stays (`writs_held`, `records_held_for_holding_rows`, `works_sites`, `detainees_held`, `holdings_to_found`: "a man knows his own lands"); a stamp over anyone else's state is ledger-gated (`vacancies`, `seat_holders`, `aim_state`, `matters_awaiting`) | 4 (`docket_question` and `sittings_before` already require a held claim) | `08_FI_01` |
| R-04 | Q2 clause 2 reads where a claim's subject is now | unclear | stays: it filters the person's own landed claims and adds no referent (r2 `01` §A.4.4) | 3 | none |
| R-05 | a telling passes on what the room already holds; a retelling passes on "a telling happened" | gap | a third `said_slants` arm, `unshared`, at `said_of` | 5 | `08_FI_02` |
| R-06 | CR-29 is third in B10-14; two defects cannot be measured while `chronicle` broadcasts | sequencing | CR-29 first | 5 | `08_FI_02` |
| R-07 | investigation has no scenario, conclusion, stake or end | gap | a standalone fixture and a conclusion carried by existing verbs | 5 | `08_FI_03` |
| R-08 | nothing checks a told claim (H-271); a lie has no consequence | gap | a graded inquiry's success deposits what it examined firsthand; a teller's record first falling below neutral lands as a claim | 5, then 3 (CR-83 prices it) | `08_FI_03` |
| R-09 | H-111 (does a refusal propagate) and H-314 (a `Partial` closes the trail) flagged as rulings | flagged for Jordan | both answered by B10-14 as written (CP-T06-04, CP-T06-03); not escalated | 3 | none |
| R-10 | `finding.none` names three outcomes | name | a refused inquiry emits `<verb>.refused`'s shape, `inquiry.refused`; a rolled Failure keeps `finding.none` | 4 (CP-T05-03 split `tell.refused` from `news.untold`) | `08_FI_04` |
| R-11 | `argument.won` at `Partial` | name | `Partial` emits `argument.held` | 4 (`speak`'s `matter.held`) | `08_FI_04` |
| R-12 | `research` needs no presence | wiring | add the `present_at` conjunct on the Record's place | 4 (`examine`, `surveil`) | `08_FI_04` |
| R-13 | a repeated ungraded finding mints the same claim again | wiring | the told channel's exact-triple guard applied to an event-kind claim the holder already holds firsthand at the same tick-or-later subject | 4 | `08_FI_04` |
| R-14 | `knots.py`: global registry, unseeded draw, dead "Canon source" path, self-knot | hygiene | refuse a missing `rng`; refuse `actor_a == actor_b`; correct the path line; registry stays (an oracle, unplugged) | 5 | `08_FI_04` |
| R-15 | a claim at confidence 0 still closes a trail | wiring | `holds_trail` requires `confidence > 0`; `deeds_judged` unchanged (ED-IN-0320: the opinion stays) | 5, 1 | `08_FI_04` |
| R-16 | H-116's head states a severed edge that is closed | stale row | head rewritten to "closed by W-A/W-B", with this audit's count | 1 | `08_FI_04` |
| R-17 | `module_contracts.yaml`'s `fieldwork` module row describes the knots oracle; `HANDOFF_FI.md` names two ledger rows as unwritten | pointer | split the contract row's description (entry `find`; oracle `knots.py` unplugged); write the two ED-FI rows | 5 | `08_FI_04` |
| R-18 | H-234: how news of unrest travels (needs_jordan on ED-IN-0298 [last row UNVERIFIED]) | flagged for Jordan | a row in CR-29's `reach` roster for the unrest kinds, by rung kind; not a sixth channel | 3 | `08_FI_02` |
| R-19 | H-351: should a faction's members learn of its acts at a distance | unclear | no: every channel is place-bound or edge-bound by precedent; members learn by being told (R-05) | 4 | none |
| R-20 | H-323 / H-345: bystanders hear; a garbled copy carries no flag | flagged as rulings | both ruled already; closed | 1 | none |
| R-21 | H-222: `standing` is the same constant for everyone | gap | irrelevant while no deposit mints a `person_predicates` claim and no chooser term reads `standing` (REM-44) | 2 | none |
| R-22 | H-92: a held document buys a scene | wiring | `budget` counts live `hold`s whose object is an Office | 5 (S26.3: the budget varies *by office*) | `08_FI_04` (CHAR's owner) |
| R-23 | H-231: a razing is witnessed by the razer alone; custody receipts name nobody | wiring | `event_place` falls back to the place the actor departed in the same write (H-206's limb); `_hold_tenure_ends` also expands `detain` and `ban` to (prisoner, seat) | 4 (H-206, H-71) | `08_FI_04` |
| R-24 | `Record.ttl` has no reader; a decree never lapses (H-259) | dead carrier | a writ lapses when its last declared stage matures (`stages`/`matured` already run at MATTER); `ttl` leaves the matrix | 5 (ID-13) | `08_FI_04` |
| R-25 | H-267: a hearer's regard never enters `argue` | unclear | the hearer's `regard` for the arguer rides the existing `reception` operand | 4 | SC lane (named, not authored here) |
| R-26 | `loop/witness` exceeds `04:178` five times by declared convention | spec against code | amend the row's may-read cell (listed in §11: it overwrites ratified Layer 1) | 5 | `08_FI_04` §6, and §11 |
| R-27 | `reconstruct` has no product (K-37: "no value space") | gap | its value space is the persons the actor's own ledger names as doers; its product is an uttered HOLDS Proposition | 5 | `08_FI_03` |
| R-28 | H-204: the confidence break path is unreachable | wiring | closed by R-05's arm (a confided copy outranks the hearer's own "a telling happened" claim) | 5 | `08_FI_02` |

**28 resolutions decided.** Two are also listed in §11 (R-01's scope for common knowledge; R-26).

## 7. Research transfer

Read: `research/00_INDEX.md` (§1 rules), `research/by_lane/FI_fieldwork_investigation.md` (§0–§2 in full,
§3–§11 by heading), `research/game_precedent_suite/dispositions/D_T06.md` (rows 1–51), the README and the
sifting/simulation file of `research/emergent_narrative_literature/`. Not read: the companion parts 2–8,
`research/historical/`, `research/provenance/`, `tables/R5`, `tutorials/T06` (§12 lists them as skipped).
Research is tier 3; nothing below settles a design.

**Precedents that change what to build.**

| precedent | finding | what it changes here |
|---|---|---|
| Dwarf Fortress rumours; *Talk of the Town* (via the lane file's N-9 row and S05) | claims with provenance that characters act on, including false ones, is a shipped shape | confirms the carrier (`Claim.chain`, `teller`); the gap is volume (F-FI-02), not model. Valoria has the shape and not the traffic |
| Lacuna; Pentiment (D_T06 rows 21, 37–39) | a conclusion is submitted whether or not it is right, and the world answers later; Pentiment works *only when the accusation lands a consequence* | the shape of `08_FI_03`: a conclusion as an uttered Proposition, an accusation by `petition` → `determine`, no verifier. D_T06 row 38 found that nothing downstream reads whether the judgment was right: that is the missing half |
| Return of the Obra Dinn (rows 3–5) | every inference stays revisable; the confirm-in-threes lock leaks the answer | supports no verifier (already ruled) and argues against the terminal `Partial` (H-314): CP-T06-03 is the right edit |
| L.A. Noire (rows 30–31) | missing evidence removes the option; a wrong answer loses the information | Valoria has the first by construction (`own_ledger` cells); it has the second only by accident (the trail lockout) |
| Shadows of Doubt (rows 8–9, 15) | each kind of deed leaves a signature pattern; leads chain; inquiring is itself witnessed | one covert kind gives no material to recognise (CP-T06-01 widens it); lead-following exists as Q2; "inquiring is witnessed" already runs (`finding.made` is seen by the room) and is the natural counter-play |
| GUMSHOE's access/quality split (lane file §2.2, marked *misapplied* there) | the core clue is never behind a roll; the roll buys quality | `finding_terms` is exactly a quality table, but access is behind the roll (a Failure deposits nothing). R-08's edit (a failed or refused inquiry still teaches its reads, CP-T06-04) moves toward the split without adopting it |
| Felt / Winnow / Select the Unexpected (literature file `04`) | a simulation needs a sifter to surface storyful sequences; coupling sifting to the simulation is where the leverage is; unexpectedness as rarity is a usable ranking | bears on legibility (§9): the causal log (`causes[]`, `claim.deposited` chained to the witnessed act) is a sifting substrate nobody queries. Not an FI build; named for the holistic stage |
| Historical: pre-modern inquiry was testimonial and procedural (lane file §1.3: oath, denunciation, inquest jury), and the Foscarini affair (wrongful execution on fabricated informer testimony) | four of the six acts are physical or archival, an anachronism; the richest historical material maps to proceedings | `interview` answered by the questioned person's own `tell` or `lie` (CP-T06-05) is the testimonial act; with R-05 and R-08 it produces the Foscarini shape (false testimony, a ruling on it, exposure later) from parts that exist |

**Tried and did not transfer.**
- *Heaven's Vault* (confidence as the number of independent support chains): already built as the noisy-OR
  over distinct origins; it cannot be evaluated while chained claims number 0–7.
- *CK3 secrets* (ownable, leakable, with a cost on exposure): no carrier for exposure exists and
  `rosters.yaml` forbids a bare `exposure` name; D_T06 row 44 marks the claimed equivalence stale. A design
  problem, not a transfer.
- *Disco Elysium* passive checks and the Dialogue Lattice: design-only; K-36 makes `interview` a prompt.
- *Brindlewood Bay* (player-authored truth): rejected by the lane file for the right reason: a strategic
  layer needs a fact to propagate.
- *Obra Dinn's and L.A. Noire's case objects, ratings and endings*: there is no case object by design (no
  GM), so every score-over-a-closed-puzzle row is discarded.

**Nulls.**
- **No historical research was ever run for FI** (lane file §1.3). Act-level grounding is three single
  rows, one `[UNVERIFIED]`. Any number or threshold drawn from "history" for the inquiry acts would be false
  comfort.
- **The game survey behind the 2026-08-18 fieldwork architecture is unattributed and self-graded**, and
  most of its borrowings landed on the retired Key substrate. What survives are three disciplines (access
  never behind a roll; deduction by consequence; the record as a derived view), none of which the code
  honours yet.
- **No shipped game was found that makes NPC-to-NPC rumour the main carrier of a strategic layer and
  shows it readable to a player.** Shadows of Doubt spreads by newspaper, Pentiment by scripted lines, KCD2
  by a scalar per place (D_T06 rows 17, 24, 47). Valoria is alone here, so its own measurement is the only
  evidence, and it reads near zero.
- **The emergent-narrative literature passes no verdict on a design** and none of its `rater`, `player` or
  `ablation` rows can be applied without a played build.

## 8. Best path forward

Ordered. "Alone" = needed for the subsystem to run well by itself; "compose" = needed for it to feed the
others. Each gate is an execution artifact (§0.2).

| # | change | file / owner | gate (what shows it worked) | unblocks | class | for |
|---|---|---|---|---|---|---|
| 1 | CR-29 first in B10-14: the `reach` roster and predicate, then `_ch_chronicle` deleted | `epistemic.py`, `rosters.yaml`, B10-14's order | `dynamics.py`-style reading: speakerless `told_by` falls from 3,700–6,000 a season to the kinds the roster carries; `tenure.closed` and `person.died` still reach the realm | R-07; makes steps 2–3 measurable | small build (scheduled) | compose |
| 2 | Claim-sourced referents (`08_FI_01`) | `queries/world_q.py` (`goal_referents`, `vacancies`, `aim_state`, `matters_awaiting`), `harness/populated.py::seed_acquaintances`' sibling, `requirements.yaml` R-07/R-08 text | `r08_probe.py` re-run: P1 and P2 read "candidates moved: no" with both controls unchanged; then the same seat change made by a real act the subject witnesses reads "yes" | R-07, R-08 | small build | alone |
| 3 | The `unshared` slant (`08_FI_02`) | `queries/person_q.py::said_of`, `rosters.yaml: said_slants`, `Fixtures.said_slant` | chained claims with ≥ 2 hops > 0 at seeds 0–2 over two seasons, against the `newest` arm reading 0; told claims per `news.told` ≥ 1 | R-01, R-07; H-204, H-272 | edit | compose |
| 4 | B10-14 as written (CR-94, CP-T06-09, -01, -03, -04, -02, -07, -05) | per card | per card; found deposits > 0 in a seeded realm (today 0 / 0 / 0) | R-05, R-09 | builds (scheduled) | alone |
| 5 | Inquiry products and the standalone scenario (`08_FI_03`) | `verb_table.yaml` (`reconstruct`, `interview`, `examine`, `surveil` rows), `loop/witness.py` (observation deposit for a graded inquiry), `harness/` fixture | the scenario's four endings each reached at some seed in a 20-seed sweep; a hearer's `record` of a liar moves after an inquiry, not before | R-05, R-08 | design-first, then build | alone |
| 6 | Small edits (`08_FI_04`): names, `research` presence, the confidence-0 trail, the repeat guard, `knots.py`, pointers, `budget`, razing, `ttl` | per row | each row names its test | hygiene; R-05 honesty | edit | both |
| 7 | CR-83's design (familiarity sets inference; what a caught lie costs) | `proposals/` (design-first, B10-13 tail) | its own falsifier | R-06, R-08 | design-first | compose |

Deletions recommended: `Record.ttl` (R-24); `_ch_chronicle` (with CR-29). Nothing else. No guard is
proposed anywhere in this audit.

## 9. Playable standalone and integrated

**What exists today.**
- *Entry point:* none for fieldwork. `harness/play_surface.py` (`dispatching_chooser`, `carry_on`) can seat a
  player-proxy on any person in any world, and `decision/sheet.py::development_space` returns his ranked
  candidates; nothing builds an investigation scenario for it.
- *Fixture:* `engine/season/tests/test_fi03_trail.py` builds a hand-made `trail_world` (a forger, a forged
  Record handed on, an investigator) inside the test file; it is not importable as a scenario.
- *Choice surface:* the six inquiry rows plus `tell`, `lie`, `forge`, `conceal`, `survey`, `give`,
  `create_record`, `petition`, `carry`. In the realm an inquirer's candidates are formed on whatever his
  question's referent is; `examine` never folds (its `site` operand is rarely a Site).
- *Outcome legibility:* a finding is three or four claims in a ledger (`record.forged`, a masked `seen`).
  Nothing renders a ledger to anyone (`sheet.chronicle` returns a person's claims as a record; no
  instrument prints "what you learned and from whom"). A refusal, an impossible task and a failure are one
  kind (`finding.none`), deposited to nobody.
- *Stakes:* none. Inquiring costs a scene. A wrong conclusion cannot be stated; a right one changes nothing.
- *End condition:* none. There is no case; the trail closes when held.
- *Instrument:* `harness/aperture.py` per-verb lines; no fieldwork instrument. This audit's
  `dynamics.py` is a session script.

**Point by point against the standing requirement.**

| requirement | state | gap |
|---|---|---|
| Playable alone: scenario seed | absent | a builder (`trail_world` promoted to `harness/`), with a deed done, a paper handed on, three people who know parts |
| choice surface | present, thin | three inquiries with no product; no act that states a conclusion; no act that checks a telling |
| consequences | absent | nothing reads whether a conclusion was right; a caught liar loses nothing visible |
| legibility | absent | no ledger view; `finding.none` conflates three outcomes |
| ending or stable continuation | absent | the accusation determined, the forger fled, the trail cold, the investigator discredited: none representable |
| One code path | **holds** | the season reaches `modules/fieldwork/find.py` by composition row (`fieldwork.find`, `step_call`) and there is no standalone fork. The risk is the opposite: a playable mode will need more than `find` returns, and must extend the same entry (its docstring reserves this: *"a playable mode that draws takes its generator as a parameter"*) |
| Layer 1 conformance | module: conforms (typed in, typed out, no World, no state). Host: `loop/witness` exceeds its may-read cell five times; `epistemic.py` is unlisted in §A.2; `seam/wrappers/fieldwork.py` is a non-contest wrapper under a contest-typed row (three amendments it names itself) | §11 item 1 |
| Integrates | executed: RESOLVE → `find_trail` → `self.findings` → WITNESS found deposit → Q2 → a response act (`test_a_found_trail_forms_a_response_on_the_forger...`). Not executed in a seeded realm (0 finds) | reachability (steps 4–5) |
| Pauses the other scales | untested: a fieldwork scene is one act in a round; there is no multi-step scene to enter and leave | arises only with a played mode |
| No GM | holds for what exists. The archived design needs one in four places (hidden thresholds, Sincerity, escalation, the false lead) and none of those is built | do not build from the archive |

**Ordered work to close.** (1) Promote the trail fixture to a harness scenario and add a ledger rendering to
the play surface (edit; no engine change). (2) B10-14. (3) `08_FI_03`: products for the three empty inquiries,
the conclusion, the check. (4) An end condition read by an instrument, not stored: the scenario ends when the
accused is determined, has left reach, or the investigator's remaining budget is spent with the trail held
by nobody (three predicates over existing state). (5) A fieldwork line in `aperture` (found / formed /
refused per inquiry, per seed).

## 10. Interfaces

| edge | direction | carrier | executed? |
|---|---|---|---|
| every subsystem → FI | in | the round's `Event[]` (changes, observed, causes) at WITNESS | yes: 11,000–13,000 Events a season |
| FI → CHAR (decision) | out | `Person.ledger` → Q2 questions, clause 4, `said_of`, `known_persons`, `regard`'s judged and told halves, `opinion` | yes: 654 / 641 / 618 acts a season occasioned by a firsthand claim landing; clause 4 461 / 445 / 485 |
| FI → CHAR (decision), unmediated | out | `questions_for`'s world-read stamps | yes, and it should not be (F-FI-01) |
| FI → SC (contests) | out | `world_q.reception`, `proofs` read ledgers of the bench; `SocialContestInput.forgery_quality` | reception and proofs: built, read 0.00 in the measured cases (H-335); forgery quality: executed only where a forged Record is researched by another (0 in realm) |
| SC → FI | in | the one roll (`social_contest.roll`) grades `research`, `examine`, `surveil`, `tell`, `lie` | yes |
| FI → FA/WR (governance) | out | `tenure.closed`, `order.given`, `date.fired` claims; writs' `content:` claims; `seats_named`, `places_named` | yes by broadcast and by held document; a writ reaches its addressee only by a separate `give` (H-203) |
| WR (MATTER) → FI | in | decay (`claim.decayed`), shortfall observations to seat-holders (the IN-22 limb), death | yes: `inferred` 297 / 297 / 324 |
| FI → MB/PC | out | `enemies_heard` (a war he knows of), `wounded_with` (those he believes hurt), `attackers_of` | built; not measured here |
| PC/MB → FI | in | `person.died`, `fight`/`march` Events witnessed by presence | yes (H-206's departed limb) |
| FI → SE | out | `places_named`, `larders_in_purview` (named half) | yes for the named half; arrival teaches nothing (H-327) |
| T07 threadwork → FI | in | `Person.thread_sensitivity` gates `thread_read`; a `knot` admits a witness by key | gate: yes; knot: only where a builder plants one (no producer) |
| FI → GO (port) | out | the ledger is state in `content_hash`; `Seen`, `Said`, `Claim` are carriers the port must mirror | designed (`04` §C.12); not ported |

## 11. Survivors for Jordan

Two items survive the five-step ladder. Everything else in §6 is decided.

**1. Is who holds a public seat common knowledge?** (R-01's one open parameter.) The ledger already took
"a vacancy reaches a person as a claim through the channels" (ED-IN-0292 last row) and recorded that *"the
Jordan-deferred question of offices as common knowledge stays open as a channel's reach"*. `08_FI_01` builds
the claim route either way; this decides one roster row (CR-29's `reach` map for `tenure.opened` /
`tenure.closed` on an Office).
- *Option A: realm-wide.* Every person in a realm holds a `told_by` claim of each seat change in it.
  Politics is legible and fast: a conspiracy re-targets within the season, a vacancy is filled at once, and
  only what crosses a border is late. Close to today's behaviour, now mediated and carrying a confidence.
- *Option B: by presence, purview and telling only.* A seat change is known where it happened, to those
  whose seats contain it, and to whoever is told. A plot can run against a dead man for seasons; a king
  can be the last to learn; a messenger matters. Slower, error-prone politics in which F-FI-02's fix is
  load-bearing.
These are different games. This audit builds for A as the shipped row and B as the swept control (A is what
the realm does today and B cannot be judged until tellings travel), marked `[ASSUMPTION; medium; Jordan to
correct]`.

**2. `04_CODE_ARCHITECTURE.md` §A.2, the `loop/witness` row's may-read cell** (R-26; ratified Layer 1).
The row lists four reads; the body makes nine, five declared as CONVENTION at the top of `witness.py`.
- *Option A: amend the row* to name the refraction reads (`decision/options`' `refracted_confidence`,
  `ledger_weigh`), the ledger id set, the driver's `findings` store, older Events by id, and two persons'
  held affiliations.
- *Option B: restore the row* by moving the refraction and credit arithmetic behind a per-holder projection
  built at the barrier by a `queries/` function, so `witness.py` imports no `decision/` and reads only
  declared inputs; amend only for the `findings` store and older Events, which no refactor removes.
The game is identical either way; what differs is whether Layer 1 follows five accumulated exceptions or
the code is brought back to it. `CLAUDE.md` §0.05 (*"a spec edited to match its implementation checks
nothing"*) points to B for the two `decision/` imports; the row is ratified, so the choice is Jordan's.
Carried in `08_FI_04` §6.

## 12. Evidence log

All `PYTHONHASHSEED=0`. Outputs under the session scratchpad, `runs/FI/`.

| # | command or probe | seed · seasons | outcome |
|---|---|---|---|
| 1 | `python -m engine.season.harness.register --requirements` | — | exit 0; R-07 `partial`, R-08 `partial`; *"every row carries a measurement or names one"* |
| 2 | `explore.py` (`build_realm(0)`) | 0 · 0 | 83 persons, 34 offices, 698 tenures; 6 conferrers; 0 vacant offices; goal ambitions by object kind: `seat_holders` 34, `rung` 14, `deed_doers` 11 |
| 3 | `r08_probe.py` | 0, 1, 2 · 0 | F-FI-01's table; identical at the three seeds (the build does not vary these facts) |
| 4 | `dynamics.py 0 1` | 0 · 1 | hash `5ab73af282d0779646c38839fbab85d8`; §1a |
| 5 | `dynamics.py 0 1 --plain` (control: un-instrumented `populated.run`) | 0 · 1 | hash `5ab73af282d0779646c38839fbab85d8`, 13,379 Events, 749 acts: identical to #4, so the wrappers perturb nothing |
| 6 | `dynamics.py 1 1` | 1 · 1 | hash `aa58ef0b…`; 11,409 Events, 731 acts; `told_by` 4,049, chained 0; `news.told` 1 (`Partial`), `news.untold` 12, `tell.refused` 43; `tell` 10, `lie` 3; clause 4: 20,345 calls, 445 declines, world disagreed 2; unsourced chosen 82 (folded 32); `record.forged` 19, `record.given` 1 |
| 7 | `dynamics.py 2 1` | 2 · 1 | hash `a21ab6e1…`; 11,208 Events, 751 acts; `told_by` 3,746, chained 0; `news.told` 0, `news.untold` 2, `tell.refused` 4; `tell` 2, `lie` 0; clause 4: 19,629 / 485 / 1; unsourced chosen 84 (folded 29); cells: firsthand 734 true / 10 false, inferred 238 / 32 |
| 8 | `dynamics.py 0 2` | 0 · 2 | hash `bacd687f…`; 37,646 Events, 1,529 acts; claims 22,958 (`firsthand` 12,929, `told_by` 9,708, `inferred` 321), largest ledger 535; chained 12, all one hop; `news.told` 7 (`Partial` 5, `Success` 2); cells: firsthand 1,135 / 73, inferred 0 / 270, told 1 / 10; clause 4: 49,271 / 1,903 / 7; `record` pairs 12: below 1.0 five, above one, unchecked six; unsourced chosen still 81 |
| 9 | three-season runs at seeds 0–2 | — | **not completed**: stopped under machine load (other lanes' runs; load average ~30). No three-season reading is claimed anywhere in this file |
| 10 | `python -m engine.season.harness.corpus_run` (from the scratchpad directory) | 0 | [see the note below this table] |
| 11 | `run_cases.load_cases("NPC")`, `("ARC")` + a keyword classifier | — | 143 cases; §13's class counts (regex readings, not a classification by hand) |

Not run: `pytest` (by instruction); `aperture`, `strife`, `m1_acceptance` (not needed for a claim made here).
Everything quoted from a hole-register `cite:` as "the tree's own reading" was read, not re-run.
