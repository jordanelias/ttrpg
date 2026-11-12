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
4. **Nobody carries a plan.** The driver keeps a per-person queue so that a five-scene plan is spent
   over five rounds and re-made only *"when the inputs change"* (`deliberate.py:199-263`). In three
   seasons no scene was ever released from a queue made in an earlier round: the fingerprint differed
   at every one of 1,172 calls, and 98% of the re-plans released a different scene from the one queued.
   The chooser composes up to five scenes per call and four are thrown away, five times a season. What
   the notes call triage (*"the PERSON chooses what to leave undone"*, the law text at
   `deliberate.py:237`) is in effect one greedy pick per round. See F-PES-CORE-06 and the false N-line
   in §2.
5. **The record cannot say which scene.** *"NO EVENT CARRIES A ROUND"* (`driver.py:557`); the round is
   a driver local and my figures above exist only because the probe wrapped the steps. A reader of the
   log (a chronicle, a player's "what happened this season") cannot tell a ticked season from a flat
   one, and cannot tell which acts shared a round. The notes defend this as the dead-carrier rule
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
