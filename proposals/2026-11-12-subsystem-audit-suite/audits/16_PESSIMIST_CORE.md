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

**This file is written early and appended (the brief's instruction). Sections below the verdict are in
the order they were established; the verdict is rewritten last. A section headed `[PENDING]` was not
reached.**

## 0. Verdict

`[PENDING — rewritten after the probes; see §1–§3 for what is established so far]`

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

### 1.2 "A decision propagates and later decisions depend on it" — see §1.5 (the knockout runs)

`[appended below when the runs finish]`

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
clause 4 can never decline it, so the chooser re-forms it every round. `[the per-stem split of the 828
is appended in §1.6 when `p34.py` finishes]`

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
| that it was a state change at all | `[the minted-against-logged receipt count is appended in §1.6]` | |

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

### 1.6 The two readings §1.3 and §1.4 left open (`p34.py 0 2`; hash `bacd687f…`, the baseline's)

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
person per season each composing five scenes to release one. The kernel is legible in its rules and
carries roughly as much unexercised structure as exercised. *"Allows the player to intuit complex
outcomes from simple choices"* fails where the three surprises of §1.1 are.
