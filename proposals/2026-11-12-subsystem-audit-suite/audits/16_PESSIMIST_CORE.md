# CORE — pessimist audit: NERS, premise and emergent narrative, of the season-loop core

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: d161a61 (working tree)

Scope: the season-loop core (`engine/season/loop/driver.py` and the steps it binds, `state/`, the gate,
`seam/`, `manifest/`, `verb_table.yaml`, `write_matrix.yaml`, the fold, `queries/`, the `harness/`
instruments and `register --requirements`), the nine requirements as that instrument decides them, and
the four premise sentences of the loop: *a season ticks scene by scene*; *a decision propagates and later
decisions depend on it*; *an act that cannot happen is refused and the refusal teaches*; *what happened is
recorded and retellable*. The CORE audit and its addenda B and C (`01_CORE_audit*.md`), the determinism
sweep (`18_DETERMINISM_SWEEP.md`) and the GAME pessimist (`16_PESSIMIST_GAME.md`) are cited, not redone.
Everything measured here is new work unless a lane is named. All runs: `PYTHONHASHSEED=0`; scripts and
outputs in `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/PES_CORE/`.

## 0. Verdict

**The kernel does what two of its four premise sentences say and half of each of the other two: a
season does tick, and a decision does propagate (shown here by a counterfactual with a clean null,
which is better evidence than the requirement rows cite); but a refusal does not teach, and what
happened is recorded only as the fact that something of a named kind touched a named cell.** In three
seasons of the shipped realm at seed 0, 56% of what individuals attempt is refused; a refused
opportunity is twice as likely to be tried again as one that worked, and the retry fails 24 times in 25,
because the commonest reason an act cannot happen (the other person is not here) is the one read the
engine rules a person may never learn, although the person already holds an unread claim that he was
refused. Every one of 36,586 receipts in the log carries no value; 69% of the state changes that are not
ledger bookkeeping (every scar, and the only writer of a conviction crisis) are in no Event; 94% of the
log is claim bookkeeping. The "scene" the season ticks by is a budget unit: its steps fold in hash
order, not the order chosen (23%, which is chance), and the person spoken to is busy with a scene of his
own 71% of the time. The gate over the nine requirements returns success on a file that claims all nine `met` on a
module that does not exist. **The single largest obstacle in the core is F-PES-CORE-01**: more than half
of every person's season is spent being refused the same things, so whatever the other lanes build to
make acts land, the chooser spends its budget relearning nothing.

**Steelman, and what survived.** The causal edge, the gate, seeded replay and the same-season answer
channel all held: a replay differs in 0 acts; removing a scene that touches nobody changes 0 of other
people's acts; removing one individual's scene changes 236 to 634, ordered by how often it was cited.
The teaching channel is real where it is wired (8% retry against 57% where it is not). Three cuts came
back free (the stored plan tail, the five strata, the retry licence at 99 parts in 100) and one came back
*not* free and is reported as such (the budget the chooser is shown).

**On the standing rule (*we do not do deterministic*).** Nothing proposed here makes an outcome a fixed
function of state: the refusal fix is a weight on a drawn choice, and the alternative that would be a
ban is named and rejected. Fold order, which the determinism sweep (C-11) flagged as an undrawn decider
between rival acts, was measured: it decides about one act in 175.

## 1. Premise audit — the four sentences of the loop, by execution

Method (`skills/premise-check/SKILL.md`): the ordinary meaning first, then the notes' account, then the
running code, on the shipped realm (`harness/populated.py::build_realm(0)`, 83 persons: 46 individuals, 37
cohorts), the shipped chooser, no player. Baseline run: `run_dump.py 0 3` (three seasons; content hash
`52ff67bc…`, equal to the GAME lane's seed-0 hash, so the recording wrappers moved nothing: that equality
is the control for every figure below). 2,630 acts; 74,510 Events.

### 1.1 "A season ticks scene by scene" — **holds as a tick; fails as a scene**

*Ordinary meaning.* A scene has a place, people in it, a beginning and an end; what happens in it happens
in order; the next scene starts from where the last one left things; someone who is in a scene is not
somewhere else at the same time.

*The notes' account* (`loop/driver.py:392-443`, `state/carriers.py:602-632`): a season is R rounds
(`scene_budget`, 5); each round every person deliberates, at most `scenes_per_round` (1) of his scenes is
released, all released acts are folded together, and WITNESS deposits before the next round, *"so what
occurs after one scene can impact the next scene"*. A `Scene` is `(id, actor, acts, occasion)`: one
person, one to three interactions, the question it is about. `place` is *"deliberately not added"*.

*The running code.*

| reading (seed 0, 3 seasons unless said) | value |
|---|---|
| individuals' acts in rounds 1–4 | 1,073 |
| of those, citing an Event of **another person's act in an earlier round of the same season** | 420 (39%) |
| of those, executed (not refused) | 154 (14% of rounds 1–4) |
| individuals' acts in round 0 answering the same season | 0 of 414 (the control: nothing precedes round 0) |
| multi-interaction scenes folded (2 seasons) | 525 |
| of those, folded **in the scene's own order** | 120 (23%; chance is 17% for three, 50% for two) |
| (round, person) pairs where the person is the named counterparty of another's **executed** act (2 seasons) | 87 |
| of those, the person also executes a scene of his own in that round | 62 (71%) |
| scenes released from a plan queued in an earlier round | **0 of 1,137** |
| `choose()` calls that found a queued plan and released something else (2 seasons) | 516 of 527 |

1. **The tick is real.** Two fifths of what individuals attempt after round 0 cites something another
   person did earlier in the same season; none could under one pass. R-03's `met` survives this attack,
   and by a stronger reading than the one the row cites (the `scene_budget = 1` arm changes the act
   count from 16 to 1, which shows fewer acts, not interleaving; F-CORE addendum did not separate the
   two). The pessimist qualification is what the 154 executed answers are: the GAME lane's seam matrix
   shows them to be records and utterances about clock Events.
2. **A scene is not a sequence.** `resolve._canonical_order` sorts every act of the round by
   `(stratum, H(seed, tick, actor, "order:verb:act id"))` (`loop/resolve.py:51-58`); the scene's own
   order is not a key. 77% of multi-interaction scenes fold out of the order their chooser composed
   them in, which is chance. All of a scene's interactions are chosen before any of them resolves, so
   the second cannot depend on how the first came out. **R-09 asks that "chains of events within a
   scene" be probabilistic; there is no chain within a scene to be probabilistic about.** The most
   common three-interaction scene at seed 0 is `train, train, train` (13 scenes, every act refused).
3. **A scene has one person in it.** The person told, argued with, petitioned or interviewed spends
   nothing and is not held: in 62 of 87 cases he executes a scene of his own in the same round, with
   somebody else or nobody (`p_npc_013` is told a thing while he `reconstruct`s). Nothing bounds how
   many persons' scenes one person is the other half of. This is the S test *pauses correctly* failing
   at the smallest scale: the loop has no notion of two people being occupied with each other.
4. **Nobody carries a plan from one round to the next.** The driver keeps a per-person queue so that a
   five-scene plan is spent over five rounds and re-made only *"when the inputs change"*
   (`deliberate.py:199-263`). In three seasons no scene was ever released from a queue made in an
   earlier round: the fingerprint differed at every one of 1,172 calls, and 98% of the re-plans
   released a different scene from the one queued. The chooser composes a plan per call and all but
   its head is thrown away, five times a season. **The control cuts the other way and is reported:**
   telling the chooser it can afford one scene only (`qcut.py 0 2`) moves the run (812 and 799 acts
   against 821 and 882; different hashes), so the *budget shown* shapes the scene chosen and only the
   *stored tail* is dead. What the notes call triage (*"the PERSON chooses what to leave undone"*,
   `deliberate.py:237`) is one pick per round made with the whole budget in view. F-PES-CORE-07.
5. **The record does not say which scene.** *"NO EVENT CARRIES A ROUND"* (`driver.py:557`); the round
   is a driver local, `Claim.round` is its one carrier, and `Scene` objects live in a driver dict
   (`d.scenes`), not in the World. The figures above exist because the probe wrapped the steps. A
   reader of the log can group acts into scenes by `Act.scene` and can infer round boundaries only
   from where the blocks of `claim.deposited` fall. The notes defend this as the dead-carrier rule
   (nothing reads it); the premise sentence is the reader.

**Verdict on the sentence.** Would a player who knows strategy and RPG games be surprised? Yes, on three
counts: the order he composes a scene in is not the order it happens in; the person he speaks to is
simultaneously elsewhere; and the season's log does not show scenes. Does the behaviour correspond to
the premise? As a *tick*, yes. As a *scene*, the word names a budget unit, not a scene.

### 1.2 "A decision propagates and later decisions depend on it" — **holds, by a controlled counterfactual; the dependence is mostly not in the record, and it saturates**

*Ordinary meaning.* Had that person not done that thing, other people would later have done otherwise,
and one could say which and why.

*The notes' account.* A scene cites the question that occasioned it (`Scene.occasion`), the question
walks to a landed claim, the claim to an Event, the Event to another person's act: `causes[]` *"is the
substrate of the entire emergent-narrative claim"* (`state/world.py:1496-1499`). R-01 and R-02 read `met`
on that edge (corpus `R3`) and on a degree sweep whose plants are not detected (F-CORE-03).

*The running code* (`knock.py 0 2`, `knock2.py`: one built realm, forked; in each arm exactly one
`choose()` call is made to return nothing, everything else replays; ids and draws are
`H(seed, tick, subject, purpose)`, so removing an act shifts no other draw; the figure is the *other*
persons' acts that differ from the unperturbed run, by `(actor, season, round, verb, opportunity,
outcome)`, counted both ways, of about 1,690):

| arm | other persons' acts differing | persons affected (individuals of 45) | first round that differs |
|---|---|---|---|
| **control: replay, nothing removed** | **0** (hash `bacd687f…` reproduced) | 0 | — |
| **control: a cohort's round-0 scene removed** (it tends itself) | **0** | 0 | — |
| a round-0 scene of an individual **no other act ever cites** (`p_npc_001`) | 236 | 21 (12) | season 1, round 1 |
| a round-0 scene of a median-cited individual (`p_npc_005`, cited 4 times) | 309 | 33 (15) | season 0, round 1 |
| a round-0 scene of the most-cited individual (`p_npc_035`, cited 12 times) | 634 | 63 (30) | season 0, round 1 |
| **that individual's whole season 0 removed** (five scenes) | 625 | 64 (31) | season 0, round 1 |
| ceiling: the chooser's draw re-seeded for everybody (`storybar`'s existing arm) | 2,760 | 83 (46 of 46) | season 0, round 0 |

1. **It propagates, and the controls say so.** Zero for a replay, zero for a scene that touches nobody,
   then 236, 309, 634 as the removed scene is cited by 0, 4 and 12 other acts. This is the reading R-01
   and R-02 lacked: an effect with a null, a dose-ordering and a ceiling. On this evidence the two rows'
   `met` is better supported than their own `measured:` blocks support it. The steelman holds.
2. **It saturates.** Removing five scenes of the same person moves 625 acts; removing one moves 634.
   Past the first perturbation the realm does not respond in proportion: about 130 acts a round differ
   in season 1 whatever was removed. What a decision buys is *a different season*, not *a consequence of
   its own size*. A player who withholds one act and one who withholds a season's work change the world
   by the same amount.
3. **Most of the dependence is not on the edge the record keeps.** The scene nobody cites still changes
   236 acts by 21 people, none in its own season, all from round 1 of the next. `causes[]` carries the
   *occasion* of a scene; it does not carry what else was in the person's View when he scored his
   options (`view_k = 12` claims of a ledger of several hundred), and that is how an uncited act reaches
   21 people `[the path is inferred from the code, not traced: UNVERIFIED]`. So an instrument that walks
   `causes[]` (corpus `R3`, `storybar`, `chronicle`) under-counts dependence, and a narrator who asks
   *why did these 21 act differently* finds no edge to follow. F-CORE-12 (the reason for an act is not in
   the world) is the same defect seen from the act; this is it seen from the cause.
4. **What depends is paper.** The executed acts that differ are `create_record`, `utter`,
   `reconstruct`, `oblige`, `commit`; the end states differ in records held, propositions, the docket
   and its dates, and scar. In the largest arm one office that had been established is not, one person
   lives elsewhere, and three or four of 39 stores differ by a few units. No person, no seat, no site.
   The GAME lane's null-arm reading (§1.1 there) is the same fact from the other side.

**Verdict on the sentence.** Genre: no surprise; a player's act changes what others do. Intent: yes.
Words: *propagates* is earned; *depend on it* is true and not retellable. Fix: none at the mechanism;
the reading goes to the requirements (F-PES-CORE-05), and the unrecorded influence is F-CORE-12's
proposal (`01_CORE_reason_trail_in_the_act_store.md`), which this evidence makes more urgent.

### 1.3 "An act that cannot happen is refused and the refusal teaches" — **refused: yes; teaches: no**

*Ordinary meaning.* When I try a thing and am told I cannot, I learn why, and I stop trying that thing
until what stopped me changes.

*The notes' account.* A refusal is an Event (*failure emits, never raises*); the fold's own reads ride
it as `Event.observed`; WITNESS deposits those reads into the actor's ledger (`loop/witness.py:740-800`,
`W-B`); the next `opening_set` declines a Candidate whose precondition is KNOWN-FALSE from the person's
own claims (`decision/options.py:76-107`, §F1 clause 4). So a man refused at an empty granary knows the
granary is empty and does not ask again.

*The running code* (seed 0, 3 seasons, individuals only; `an1.py`, `an2.py`):

| reading | value |
|---|---|
| individuals' acts | 1,487 |
| refused | 828 (56%); by season 226/479, 299/487, 303/521 (47% → 61% → 58%: not falling) |
| refused acts whose **same (actor, verb, opportunity)** is attempted again | 342 (41%), 303 within the same season |
| the next attempt: refused again / executed | **328 / 14** (96% / 4%) |
| control: executed acts whose same opportunity is attempted again | 137 of 659 (21%) |
| `(actor, verb)` pairs attempted three or more times and refused every time | 69 pairs, 378 acts |
| worst single cases | one man's `march` 15 of 15, one man's `train` 15 of 15, `challenge` 12 of 12, `tell` 12 of 12 |
| per individual, share of all acts refused | median 0.56; 30 of 46 persons above one half |
| refusals carrying an observation | 801 of 828 |

A refused act is **twice as likely** to be tried again as one that worked, and the retry fails 24 times
in 25. More than half of what the median person does in three seasons is refused. The teaching channel
exists and is exercised (801 of 828 refusals carry what the fold read), and behaviour does not change.

*Why, located.* The verbs that fill the refusal column require `relation: with` (the other person is
where I am: `train`, `tell`, `argue`, `challenge`, `give`, `interview`, `capture`) or `relation:
audience` (`move`). `loop/witness.py:780-790` names those two stems `WORLD_ONLY_STEMS`: *"observed, never
deposited"*; and `queries/person_q.py:1415-1418` says it in terms: *"a known person who has walked away
is still named and the telling is refused — and the person does NOT learn it from the refusal"*. The
reason given is sound (a stale `with:` claim would feed tellings); the consequence is that **the most
common reason an act cannot happen is the one reason the engine has ruled a person can never learn**, so
clause 4 can never decline it, so the chooser re-forms it every round. The split by failing read is
§1.5. Research's `finding.none` (a search that found nothing, carried on the row's `emits_on_refusal`)
is counted as a refusal above because the driver counts it so; without `research` the figures are 773
refused of 1,408, 309 retried, **305 refused again and 4 executed**.

The driver adds a second cause on purpose: `_drop_what_was_already_done` filters only what was
*realised*, so that *"an act attempted and REFUSED in round 0 must be retryable in round 3, because a
later round's world may have made its precondition true"* (`driver.py:508-518`). Measured: the retry
succeeds 14 times in 342.

**Verdict on the sentence.** Genre: a player watching an NPC try to train an absent man fifteen times
in three seasons reads it as a broken AI. Intent: half the sentence holds. Words: `refused` is honest;
nothing in the engine could be named "learned". Fix: F-PES-CORE-01 and its proposal.

### 1.4 "What happened is recorded and retellable" — **that something happened is recorded; what happened is not**

*Ordinary meaning.* After the fact one can say who did what to whom, where, when, why, and what it
changed — and by how much.

*The notes' account.* One append-only log; every Event carries `causes[]` and `changes[]`; a change is a
`Receipt` the gate minted (*"what changed AND THAT THE GATE IS THE ONE THAT CHANGED IT"*,
`state/carriers.py:209-220`); `harness/chronicle.py` renders a chain.

*The running code* (seed 0, 2 seasons, `knock.py` baseline arm, hash `bacd687f…`):

| question a retelling asks | where the answer is | reading |
|---|---|---|
| who | `causes[]` → the act store (`state/attribution.py`) | present for act-caused Events |
| did what, to whom | the Act's verb and payload | present |
| **what it changed, and by how much** | `Receipt.delta` | **`None` on 36,586 of 36,586 receipts**; no call site passes one (`state/world.py:1442`, `:1494` are the only two `gate.mint` calls) |
| **where** | `world_q.event_place(w, e)`: the actor's *live* `contain` edge | of 831 act-caused Events of season 0, 39 answer a different place one season later (a refusal at the cathedral is later "at" the settlement its actor moved to) |
| **when, within the season** | nothing (`driver.py:557`) | the round is not on the Event |
| **why** | F-CORE-12 (the reason for an act is not in the world) | cited, not redone |
| that it was a state change at all | a receipt on some Event | 3,914 of 40,494 minted receipts are on no Event (§1.5) |

The gate already holds the answer to the third row. For a `Change` it reads `was = state_of(s)` for every
subject before applying and compares after (`world.py:1396-1399`, and that comparison is how a no-op is
refused); it then mints the receipt without either value. `Receipt.delta`, `Receipt.spec` and
`Receipt.mode` (always `"set"`) are three declared fields with one writer of a constant and, for `delta`,
one fold in `content_hash` of that constant (`world.py:1716`). The tree's own rule for this is `ID-13`:
*a declared field must reach a reader*.

So the log can say `stores.changed` at a granary and cannot say whether it rose or fell; `body.changed`
and not whether the cohort starved or recovered; `pursuit.moved` and not toward what. A narrator reading
the log knows the *kind* of every occurrence and the cell it touched. Every quantity must be re-read from
the present world, which is the state *now*, not then. The log is not a record from which the world could
be rebuilt, or an earlier world recovered.

*And most of the record is not about what happened.* 69,952 of the 74,510 Events (94%) are
`claim.deposited` and `claim.decayed`; act-caused Events that are not claim bookkeeping number 2,664
(3.6%). F-CORE-01 measured the fade half on a three-person world; on the realm the deposit half is as
large (35,115 against 34,837).

**Verdict on the sentence.** Genre: a chronicle that reads *"season 1 | Aldric create_record | emitted
record.created | answers 3. Berta utter"* is an index entry, not a retelling. Intent: partly; integrity
(the `causes[]` edge) is real and held against attack in the CORE audit. Words: `Receipt` promises more
than an acknowledgement that a write occurred. Fix: F-PES-CORE-02.

### 1.5 The readings §1.3 and §1.4 rest on (`p34.py 0 2`; hash `bacd687f…`, the baseline's)

**Refusals, split by what the refusal's own observation could teach** (525 refused individual acts in two
seasons; `Event.observed` read off each refusal; the stem lists are `loop/witness.py`'s own
`WORLD_ONLY_STEMS` and `LEDGER_DERIVED_STEMS`):

| the read that failed | refusals | same opportunity attempted again | again refused |
|---|---|---|---|
| a stem WITNESS deposits (`exists`, `stores`, `room`, `present_at`, `purview`, `contain.path`) | 189 | **15 (8%)** | 15 |
| a world-only stem, never deposited (`with` 174, `dispute`, `individual`, `audience`) | 181 | **100 (55%)** | 100 |
| every observation true (the refusal's cause is not among the fold's reads: eligibility, the write clause, a null search) | 139 | **81 (58%)** | 74 |
| no observation | 9 | 6 | 5 |
| `claim.held` false, never deposited | 7 | 2 | 1 |

This is the control the sentence needed, and it cuts both ways. **Where the failing read reaches the
ledger, the refusal teaches: 8% retry, against 20% for acts that succeeded.** Where it does not (327 of
525, 62%), 57% are tried again and 96% of those fail. The mechanism is sound and is wired to two fifths
of its cases. The largest unwired case is one stem, `with`.

**Gate writes the log does not hold.** The gate minted 40,494 receipts; 36,580 ride an Event; **3,914 are
in no Event, and every one is a `Person.scar` write** (3,906 at RESOLVE, 8 at ENCOUNTER), on all 83
persons: 47 per person in two seasons. Non-claim receipts in the log number 1,749, so **of the 5,663
state changes that are not ledger bookkeeping, 69% are absent from the record**. This is deliberate and
documented (`loop/resolve.py:637-640`: *"Nothing is emitted: `scar.taken` is declared on the row and no
reader consumes it, and putting the receipts on the act's Event would deposit claims about every scarred
observer at WITNESS"*; `_conviction_crisis` follows *"the scar's precedent"*, `:706-708`), and
`write_matrix.yaml` still declares `emits: scar.taken` and `emits: conviction.moved` on the two rows. The
rate itself (a scar on 38% of acts, a dozen observers each) is the CHAR lane's finding; the core's is that
the one kind of change that reaches every person in the realm, and the only writer of a conviction
crisis (*"fold, restabilise or destroyed"*), leaves nothing a retelling can find. F-PES-CORE-03.

**The retelling the instrument makes** (`harness/chronicle.py`, same world):

- over consequence acts (446 of 1,703): the deepest chain is **4 acts**: `conceal` (cover.assumed), then
  three `create_record`s by three people. With the log's `causes[]` shuffled (`arc.shuffled_causes`, the
  instrument's own control) the deepest chain is **5**. The pick cannot be told from a shuffle; the WR
  lane found the same of chain ends (its E-05) and that proposal is cited, not redone.
- over all acts: 10 acts, of which **8 are refusals** (*transfer.refused → train.refused → order.given →
  dispensation.issued → tend.refused → exchange.refused → travel.blocked → tend.refused → train.refused →
  travel.blocked*). The longest thing that happened in two seasons is people failing after watching
  other people fail.

## 2. NERS — cut tests on the core's own structures, executed

Method (`skills/ners/SKILL.md`; definitions `CLAUDE.md` §0.06): propose the cut, run it or read it off a
run, name what dies. Graded on false N-lines. `ordp.py 0 1` (one season, seed 0; the replay arm
reproduces hash `5ab73af2…` and differs in nothing, which is the control); the queue and receipt rows
are read off the three-season dump.

| structure | the cut | what died | verdict |
|---|---|---|---|
| **the stored tail of a plan** (`_queued`, `_inputs`, `_inputs_fingerprint`, the reuse branch; `deliberate.py:199-308`) | re-plan every round, keep nothing | nothing: **0 of 1,137** released scenes came from a queue an earlier round made (read off the run; reuse never fired, so the cut is the run) | **FALSE N-LINE.** The N-line is *"re-made only when the inputs change"*; the inputs always change |
| the plan itself (the budget the chooser is shown) | show the chooser one scene's budget (`qcut.py`) | **not free**: 812/799 acts against 821/882, hashes differ | N holds. Reported because the row above would otherwise be read as wider than it is |
| **the five strata** (`resolve._canonical_order`, `rosters.yaml: strata`) | hash order only (`stratum_of → 0`) | of 821 acts: **0** executed/refused flips, 0 differences in emitted kinds or degree in round 0; 820 of 821 act ids in common over the season; two persons' scar counts; one log entry | **FALSE N-LINE in computed play.** What the strata would decide (movement before a social act that needs presence) needs two acts in one round that touch one thing; see the next row for how often that is |
| **fold order at all** | reverse the hash order inside each stratum | round 0: **1 of 175** acts flips (`speak`, executed → refused); season: 6 status flips among 774 common acts | **nearly free.** S27.1's *"each act sees the world its predecessors left"* decides under 1% of acts. This is the frequency `18_DETERMINISM_rival_acts_in_one_fold.md` left unmeasured: its draw would touch about one act in 175 |
| **the retry licence** (`driver.py:508-518`: a refused act stays retryable *"because a later round's world may have made its precondition true"*) | filter refused opportunities for the season as realised ones are | 4 of 309 retries succeed (research excluded); 305 scenes are spent on a second refusal | **FALSE N-LINE, 99 parts in 100.** The possibility it protects is real and is 1.3% of its uses. Not the fix (a ban is a fixed outcome); see F-PES-CORE-01 |
| `Receipt.delta`, `.spec`, `.mode` | delete the three fields | nothing: one constant written, one constant folded into the hash | free as built; the better cut is to fill `delta` (F-PES-CORE-02) |
| the contest depth cap | F-CORE-07 | nothing | cited |
| CENSUS (the sixth step) | drop the step | nothing at seed 0 in three seasons: `person.demanded` is never emitted | **unexercised, not shown false.** Individuation on demand is the only way a person enters after the build; that nobody is ever demanded is the finding |
| the `obstacle > 2 × pool` gate (`resolve.py:1046`) and the fold kinds `act.ineligible`, `act.refused`, `attempt.refused` | — | none of the three kinds is emitted in three seasons | unexercised |
| the write matrix as a runtime refusal | let any step write any cell | of 65 `(kind, field, step)` cells, 26 are written in a season; **no write was refused by the matrix** (the 59 writes that raised are all `NoOpReceipt`) | N holds from one direction only (authoring: a new effect that writes the wrong cell is stopped at its first run). Narrowed, not passing as a play-time rule. No finding: that is what a type check is |
| the `Scene` level (one to three interactions) | one act per scene | 1,995 of 2,630 acts ride three-interaction scenes: the level triples what a budget buys | N holds **for quantity**; as sequence it is empty (§1.1 pt 2) |
| WITNESS per round | once per season | the 420 same-season answers of §1.1 | N holds |
| ENCOUNTER | fold fights where declared | `[not cut]` 29 `march.declared`, 5 `field.unopposed` at seed 0 pass through it | exercised; not attacked |

**R, the half with no player.** The kernel makes occasions without a player (every one of 1,487
individual acts has an occasion; 1,408 of them `claim_landed`, 79 `need`: the roster has those two sources
and no other, `rosters.yaml: question_sources`). It does not make *completion*: 100 of the 178 declared
Event kinds were never emitted in three seasons, and the list is the list of things that finish something
(`person.died`, `matter.determined`, `tenure.opened`, `exchange.made`, `site.built`, `rung.founded`,
`capability.raised`, `confession.made`, `succession.claimed`, `record.destroyed`, `field.won`); 19 of 67
verbs were never attempted. **R at the extremes** (`extremes.py`): an empty World runs five rounds of
nothing without error; at `scene_budget = 0` MATTER's Events are logged and witnessed by nobody (WITNESS
is called only inside the round loop: ledgers stay at 0); at 40 rounds two persons of a three-person world
emit `travel.blocked` 108 times in two seasons.

**S.** *Pauses correctly*: fails at the scene (§1.1 pt 3). *Calculations consistent with siblings*: the
believed-odds factor weights a contested Candidate by the chance of its bands (`choose.py::odds_weight`),
and nothing weights any Candidate by the chance it is admitted at all, though admission decides 13 verbs
outright (GAME §1.3) and the person holds the evidence. One ladder for "will the roll go my way" and
none for "can I even try" is the sibling inconsistency F-PES-CORE-01's fix removes.

**E, last, as a ratio.** What N and R found the core to deliver in computed play: a clock, a gate, a
causal edge, a same-season answer channel, and a teaching channel that works where it is wired. Against
that: a plan queue that is never used, an order rule that decides nothing, a retry rule that pays once in
a hundred, three receipt fields holding a constant, a log 94% bookkeeping, and five `choose()` calls per
person per season each composing a plan to release its head. The kernel is legible in its rules and
carries roughly as much unexercised structure as exercised. *"Allows the player to intuit complex
outcomes from simple choices"* fails where the three surprises of §1.1 are.

## 3. The nine requirements, and how `register --requirements` decides them

**How it decides** (`harness/register.py:631-701`, read in full): a status word from a roster of three;
a non-empty `measure:`; for `met`/`partial` a non-empty `measured:`; a non-empty `statement:`. Two
further checks on the measure: a `python <path>.py` must name an existing file with a `__main__`; a
`-k` expression must "select a test". It executes nothing. `tools/m1_acceptance.py::row_nine_requirements`
counts the same strings; CI runs the same command.

**Can it fail on a false `met`? No** (`req_forge.py`; scratch copies, tracked file untouched):

| scratch copy | exit | prints |
|---|---|---|
| the shipped file (control) | 0 | `met 3 · not_met 1 · partial 5` |
| A: every row `met`, `measured: x` | **0** | `met 9` |
| B: A, and every `measure:` is `python -m engine.season.harness.no_such_module` | **0** | `met 9` |
| C: A, and every `measure:` is a pytest line with `-k 'zz_no_such_test or import'` | **0** | `met 9` |
| D: A, and every `measure:` is `true` | **0** | `met 9` |
| positive controls: status off the roster; missing `.py`; `-k` matching nothing | 1, 1, 1 | the violation |

A is the known limit (F-CORE-03: statuses are strings). B, C and D are new and are defects in the check
the docstring claims: the existence test's pattern does not match `python -m <module>`, which is the
form of **six of the nine shipped measures**, so those six are unchecked; and the `-k` test passes when
any one word of the expression occurs anywhere in any test file. F-PES-CORE-04; proposal
`16_PESSIMIST_CORE_the_nine_gate_and_a_knockout_reading.md`.

**What this lane's runs say of each row** (the status is the file's; the reading is new evidence, seed 0;
a row not attacked says so):

| row | status | this lane's reading |
|---|---|---|
| R-01 propagation | met | **supported, with a control it did not have**: removing one scene changes 236 to 634 other persons' acts; replay and a cohort's scene change 0 (§1.2). Qualified: saturates; the dependence is mostly off the `causes[]` edge the row's instrument walks |
| R-02 consequence shapes later decisions | met | the same runs. Qualified: what differs is paper (§1.2 pt 4) |
| R-03 scene by scene | met | **supported as a tick**: 39% of acts after round 0 cite another person's earlier-round act of the same season, 14% executed; round 0: 0. The row's own control (`scene_budget = 1`) changes the act count and so does not isolate interleaving. Not supported as a scene (§1.1) |
| R-04 strategic and management actions | partial | not attacked. In one season no person's act wrote `Site.condition`, `Site.exists`, `Rung.exists`, `Office.exists` or `Person.capability` (§2, the matrix row) |
| R-05 all verbs built out | not_met | 48 of 67 attempted, 30 executed at seed 0 (30 to 32 over seeds 0–2, 28 common to all three); 100 of 178 declared Event kinds never emitted |
| R-06 robust characters | partial | the median individual has 56% of his acts refused; 69 `(actor, verb)` pairs are refused at every one of three or more attempts |
| R-07 memory, feeling, attitude | partial | the memory of a refusal is held (184 of 226) and read by nothing; 47 scar writes a person in two seasons leave no Event |
| R-08 non-omniscient, not perfectly rational | partial | non-omniscient: yes, to the point that absence cannot be learned. *Not perfectly rational* is being met by *does not update*, which is a different thing |
| R-09 probabilistic chains within a scene | partial | **the subject is missing**: a scene has no internal order (23% fold in order) and no step can depend on another (§1.1 pt 2). Fold order decides about 1 act in 175 |

## 4. Emergent narrative — what the kernel can and cannot tell

Scope: the kernel's own story-making (occasion, answer, refusal, deferral, clock, record) and the
instruments that read it. The WR lane's chain statistics and the GAME lane's null arm are cited.

**4.1 What the loop can produce at all (enumerated from the code).** A beginning is an *occasion*:
`rosters.yaml: question_sources` has two (`claim_landed`, `need`). An escalation is an answer in a later
round, so two people can exchange at most five times a season. A reversal needs a write that undoes one
(a `Tenure.until`, a store falling). A cost is a spent scene. An ending is `world_q.endings_reached`: two
roster rows (`peninsular_sovereignty`, `theocracy`), *"a read … the run does not halt on it"*
(`driver.py:546-549`). A retelling is `chronicle.render` of one chain.

**4.2 What it produces in computed play (seed 0; three seasons unless said).**

| story element | reading |
|---|---|
| beginnings | 1,487 individual acts, every one with an occasion: 1,408 `claim_landed`, 79 `need`. Nobody begins anything unprompted |
| escalation | deepest cross-person chain of consequence acts: 4 (`conceal`, then three `create_record`s); over all acts 10, eight of them refusals (§1.5) |
| reversal | none observed: no `tenure.opened`, `stance.moved`, `conviction.moved`, `commitment.ended`, `record.destroyed` in three seasons |
| cost | 828 refused scenes; the price leaves no receipt (F-CORE-17, cited) |
| ending | `endings: []` at every season of every arm run here (11 two- or three-season runs); the WR lane reports none in six seasons |
| retelling | one chain, as `season | actor verb | kinds | answers n`; no value, no place at the time, no reason (§1.4) |

**4.3 Dead ends.** Every Event kind that finishes something is among the 100 never emitted (§2, R).
Nineteen verbs are never attempted: `arrest`, `assign_troops`, `confer`, `destroy_record`,
`disband_unit`, `discharge_troops`, `examine`, `fight`, `forgive`, `form_unit`, `interrogate`, `marshal`,
`order_unit`, `recruit`, `restore`, `succeed`, `surrender`, `tie / knot`, `work`.

**4.4 What a choice changes.** §1.2: one scene withheld changes a seventh to two fifths of everyone
else's next season, in records, promises and dockets; a whole season withheld changes the same amount.

**4.5 The shape of the tail: are all runs the same run?** In distribution, yes. Over seeds 0, 1, 2
(the GAME lane's three-season outputs, re-read): the cosine between seeds of executed-act counts by verb
is 0.993 to 0.995; the eight most executed verbs are the same eight in nearly the same order
(`create_record`, `utter`, `research`, `reconstruct`, `commit`, `surveil`, `forge`, then `oblige` or
`tend`); 28 of the 33 verbs ever executed are executed at all three seeds. In particulars, no: re-seeding
the chooser's draw alone changes 81% of acts from the first round (§1.2, the ceiling arm). The realm is
one story-shape with different names in it.

**4.6 Are the persons' reasons readable afterwards?** For 95% of acts the recorded occasion is "a claim
landed". The View the person scored against is not kept (F-CORE-12), and §1.2 pt 3 shows it matters: a
scene can redirect 21 people through no recorded edge.

**4.7 Extremes** (`extremes.py`; the GAME lane ran the cast cap). No person, no rung: five rounds of
nothing, no error. `scene_budget = 0`: the season's wear is logged and reaches no ledger. Forty rounds on
three persons: 87 acts a season, 108 `travel.blocked` in two seasons, which is §1.3 again at small scale.

**4.8 The instruments, as claims.** `chronicle`'s pick is not distinguishable from its own shuffled
control on this log (4 against 5). `storybar`'s `--draw-seeds` arm is a real second arm and gave this
lane its ceiling. `register --requirements` cannot fail (§3). The invariant sweep and the loop check are
the CORE addenda's (F-TEST-06, F-CORE-21) and were not re-run.

## 5. Findings, ranked worst first

**F-PES-CORE-01 · degrades narrative; touches R-06, R-07, R-08 · a refusal does not teach.**
Falsifier run: `run_dump.py 0 3` + `an1.py`/`an2.py`: 41% of refused opportunities retried, 96% of
retries refused; control: executed opportunities retried 21%. Second run and its control, `p34.py 0 2`:
8% retry where the failing read is deposited, 57% where it is not (62% of refusals). `refclaim.py`: the
actor already holds the refusal claim for 184 of 226. Minimal fix at the owner:
`decision/choose.py::score_terms` gains an admission weight read by a new `person_q.refused_before`;
proposal `16_PESSIMIST_CORE_a_refusal_is_remembered.md`.

**F-PES-CORE-02 · degrades narrative (retelling); touches R-01, R-02 as legibility · no receipt carries
a value.** Falsifier: any receipt with a non-`None` `delta` in two seasons; found 0 of 36,586, and no
call site passes one. Control: the gate's own `was`/after comparison exists at `world.py:1399,1427`.
Fix: `World.write` mints with what it read; proposal `16_PESSIMIST_CORE_the_record_holds_what_changed.md`
(edit 1).

**F-PES-CORE-03 · degrades narrative; touches R-07 · the interior is not in the log.** Falsifier:
receipts minted against receipts logged; 3,914 of 40,494 are on no Event, all `Person.scar`; the
conviction crisis is built the same way. Control: every other field's receipts are all logged (0
orphans). Fix: emit the kinds the matrix rows already declare, through the gate, outside the fan-out;
same proposal (edit 2).

**F-PES-CORE-04 · blocks an honest reading of THE NINE · the gate accepts `met 9` on a module that does
not exist.** §3. Fix: three predicates in `check_requirements`; proposal
`16_PESSIMIST_CORE_the_nine_gate_and_a_knockout_reading.md`.

**F-PES-CORE-05 · touches R-01, R-02 · propagation is real, saturates, and mostly leaves no edge.**
§1.2. Falsifier: the replay and cohort arms (0 and 0); dose arms 236/309/634; five scenes 625. This is a
positive finding with two qualifications, not a defect in the loop. Fix: the reading goes into the
requirement rows (same proposal as F-04); the unrecorded influence is F-CORE-12's proposal.

**F-PES-CORE-06 · touches R-03, R-09 · a scene has no order and one occupant.** §1.1 pts 2, 3.
Falsifier: 120 of 525 in order (chance); 62 of 87 counterparties busy. Held back for Jordan (§6);
proposal `16_PESSIMIST_CORE_a_scene_runs_in_its_own_order.md`.

**F-PES-CORE-07 · code matter · the stored plan tail is never used.** §2 row 1. Falsifier: any release
from a stored queue; 0 of 1,137 (realm), 0 of 38 (headless), and the branch cut outright reproduces four
season hashes. Control that bounds it: `qcut.py` (the shown budget is not free). Fix: delete the branch;
proposal `16_PESSIMIST_CORE_no_stored_plan.md`.

**F-PES-CORE-08 · hygiene · an old Event's place is wherever its actor is now.** `world_q.event_place`
reads the live `contain` edge; 39 of 831 season-0 act Events answer a different place a season later.
Correct for WITNESS (its only caller in the loop, at the Event's own tick); wrong for any retelling.
Resolution in §6.

**F-PES-CORE-09 · hygiene · the five strata and fold order decide almost nothing in computed play.**
0 of 821 outcomes change with the strata cut; 1 of 175 with the hash reversed. No fix: the strata are
ruled and cost one sort key. The figure is handed to `18_DETERMINISM_rival_acts_in_one_fold.md`, which
asked for it.

**F-PES-CORE-10 · hygiene · at `scene_budget = 0` MATTER's Events are witnessed by nobody.** WITNESS
is called only inside the round loop (`driver.py:486-541`). Resolution in §6.

## 6. Lists the brief asks for

**False N-lines found** (cuts that came back free): the stored tail of a plan (executed, two worlds);
the five strata (executed, one season); fold order (1 in 175); the retry licence (pays 4 times in 309);
`Receipt.delta`/`.spec`/`.mode` (a constant). **A cut that came back not free and is reported:** the
budget the chooser is shown. **Unexercised, not shown false:** CENSUS; the obstacle gate; three fold
kinds; 39 of 65 write-matrix cells in one season.

**Premises that failed.** *The refusal teaches* (fails for 62% of refusals). *What happened is recorded*
(the value, the place at the time, the round and the interior are not). *A season ticks scene by scene*
holds as a tick and fails as a scene (no order, one occupant). **Premise that held under attack:** *a
decision propagates and later decisions depend on it*.

**Stories the kernel can tell today** (observed): a correspondence chain (news, then a record, then
records about the record); a five-round exchange inside a season; a march declared, deferred and
resolved; a docket formed and dated; a refusal cascade; a season re-rolled by one withheld scene.
**Stories it cannot tell, by construction:** a scene whose second step hangs on its first; an errand (he
is not here, so I go and find him); anything with a retold magnitude; an inner change the record holds;
two people occupied with each other; a person entering the world; a story that ends. **Stories the code
admits and three seasons do not produce:** a death, a succession, a founding, a building, an exchange, a
training, a confession, a determination, either roster ending.

**Resolutions decided (8)**, by the five-step ladder:

| item | resolution | ladder step | carried by |
|---|---|---|---|
| a refusal's memory is held and unread | weigh it in the score; no deposit of `with` | 4 (precedent: `odds_weight`) | `…_a_refusal_is_remembered.md` |
| receipts carry no value | fill `delta` from what the gate read | 3 (`04 §C.2`'s recipe) | `…_the_record_holds_what_changed.md` |
| scar and crisis writes reach no Event | emit the row's declared kind through the gate, outside the fan-out | 4 (precedent: `claim.deposited`) | same |
| the nine's gate has two holes | tighten three predicates | 5 | `…_the_nine_gate_and_a_knockout_reading.md` |
| R-01/R-02 lack a controlled reading | `storybar.knockout_arm` beside `draw_seed_arm`; statuses untouched | 4 (precedent: `draw_seed_arm`) | same |
| the stored plan tail | delete | 5 | `…_no_stored_plan.md` |
| an old Event's place | a retelling reads the actor's `contain` edge live at `e.emitted_at` (`move` writes `Tenure.until` and `Tenure.since`, so the closed edge is kept); `event_place` stays as WITNESS's read; no proposal file: one function beside it when a retelling is built | 5 | this row |
| `scene_budget = 0` | `Fixtures` refuses `scene_budget < 1` at load, as it refuses other unusable values: a season with no round is not a season | 4 (precedent: the loader's refusals) | this row |

**Survivor for Jordan (1).** *Is a scene a budget unit or a short sequence?* Option A: keep the global
fold order; define *scene* as a budget unit; re-point R-09 at chains across rounds. Option B: fold a
scene's steps in the chooser's order and let a step hang on the band of the one before; R-09 gains a
subject; the #353 §27 order becomes an order over scenes. They are different games (a turn of
simultaneous picks, or a turn of short conditional sequences). It survives the ladder because B edits
what Layer 1 ratifies and A leaves a ruled requirement without a subject. This lane recommends B and
does not decide it.

## 7. Evidence log

All `PYTHONHASHSEED=0`, `build_realm` unless said; scripts and outputs under
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/PES_CORE/`.
The machine was heavily loaded (load average 25 to 42); wall times are not measurements.

| # | command | seed × seasons | outcome |
|---|---|---|---|
| E-01 | `run_dump.py 0 3 s0_k3.json` | 0 × 3 | 2,630 acts, 74,510 Events, hashes `5ab73af2…`, `bacd687f…`, `52ff67bc…` (equal to the GAME lane's: the wrappers are inert); `endings []` each season |
| E-02 | `an1.py s0_k3.json` | — | scene, round, refusal and log readings of §1.1, §1.3, §1.4 |
| E-03 | `an2.py s0_k3.json` | — | retry by verb and by observation; refusal share per person |
| E-04 | `knock.py 0 2` | 0 × 2, five arms | baseline `bacd687f…`; receipts 36,586 all `delta=None`; place drift 39 of 831; scene order 120 of 525; plan change 516 of 527; knockouts 634 / 309 / 236 / 625. **OOM-killed** in its sixth arm (the process-global `TRACE.rows` grows without bound across arms) |
| E-05 | `knock2.py replay`, `cohort`, `noise` | 0 × 2, one arm a process | 0 (hash `bacd687f…`); 0; 2,760 |
| E-06 | `p34.py 0 2` | 0 × 2 | refusals by failing stem; 3,914 orphan receipts, all `scar`; chronicle 4 acts against a shuffled 5 |
| E-07 | `ordp.py 0 1` | 0 × 1, four arms | strata cut 0 flips; reversed 1 of 175; replay identical; write-matrix cells 26 of 65 written |
| E-08 | `refclaim.py` | 0 × 1 | 184 of 226 refused actors hold the refusal claim, `doer` himself |
| E-09 | `qcut.py 0 2` | 0 × 2 | one-scene budget: 812/799 acts, hashes differ (the cut is not free) |
| E-10 | `qreuse_small.py` | headless 0 × 4 | 0 reuse; branch cut: hashes identical |
| E-11 | `extremes.py` | empty World; headless at budgets 0, 1, 5, 40 | all run; budget 0 deposits 0; budget 40 emits `travel.blocked` 108 times |
| E-12 | `req_forge.py` | — | forged copies A–D exit 0; three positive controls exit 1 |
| E-13 | read of `PES_GAME/x1_s{0,1,2}_k3.txt` | 0, 1, 2 × 3 | verb-count cosine 0.993 to 0.995 |

**Read in full:** `loop/driver.py:380-570`, the comment-stripped `loop/{deliberate,resolve,encounter,
census,calendar}.py`, `state/{acts,log}.py`, `harness/chronicle.py`, `harness/register.py:600-763`,
`AUDIT_BRIEF.md`, `PESSIMIST_BRIEF.md`, `16_PESSIMIST_GAME.md` §0–§1.3, `01_CORE_audit.md` §0–§3.
**Read in part:** `state/world.py` (the write path, `state_of`), `state/carriers.py` (Act, Scene, Event,
Receipt, Claim), `loop/witness.py:655-800`, `decision/choose.py:150-300`, `decision/options.py:76-110`,
`queries/person_q.py:1385-1442`, `epistemic.py:137-220`, the heads of addenda B and C and of
`18_DETERMINISM_SWEEP.md`. **Not read** `[SKIPPED]`: `seam/`, `manifest/`, `queries/world_q.py` beyond
two functions, `data/`, the other harness instruments, the hole register, the `.designs/` and `.audit/`
sets, the dossier (the CORE audit and addenda were taken as its digest). Seam and manifest claims in
this file are therefore the CORE audit's, not this lane's. One seed (0) carries every new figure except
E-13; a figure here is a reading at that seed, not a rate.

**Not done, by the brief's limits:** no `pytest`; no `aperture`; no tracked file edited; no commit.
The brief's §13 (arcs) and §14 (capability surface) tables are the CORE audit's and its addendum B's and
are not repeated: this lane's scope adds one edge to §13, which is that every arc whose needs include
an errand, a conditional scene or an ending meets a construction limit of §6 before it meets a missing
verb.
