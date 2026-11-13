# GO — pessimist audit: NERS, premise and emergent narrative, of the port, the port gate and the player-facing layer

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 826b747 (working tree)

Scope: `godot/`, the port-gate positions GO-07..GO-16, the typed exports (`engine/engine_params/` and
their exporters), the oracle recorder, the player-surface contract, the auto/manual doctrine, cognitive
load; and the five premise sentences of presentation: *a player sees what their character could see*;
*a player can read why a thing happened*; *a player can choose a lever and see its effect*; *a duel and a
battle can be watched, steered or skipped*; *the story the world tells is legible as a story*. The
emergent-narrative method is applied here to **legibility**: what a player could be shown today, from the
data the oracle exports, of the stories the engine produces. Prior work cited, not redone:
`11_GO_audit.md`, `11_GO_audit_addendum_B.md`, the `11_GO_*` proposals, `16_PESSIMIST_GAME.md`,
`18_DETERMINISM_SWEEP.md`, `20_NARRATIVE_CHURN.md`. Everything measured here is new work unless a lane is
named. All runs: `PYTHONHASHSEED=0`; scripts and outputs in
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/PES_GO/`.

Layout: §0 verdict; §1 NERS; §2 premise; §3 emergent narrative as legibility; §4 findings
`F-PES-GO-nn`; §5 resolutions; §6 stories; §7 survivors for Jordan; §8 evidence log.

## 0. Verdict

**The port gate, as planned, would certify a game no player can read, and it cannot tell.** Three
things are sound and were re-shown at full width: the played and automated seasons are one code path
(all 83 persons seated on the player's sheet at once, two seasons, seeds 0–2, hash equal to the
automated run); a View leaks nothing by type; and the short chains the world produces do reach
witnesses (three in four are held whole, as claims, by someone who took no part). Everything a
player would call presentation fails by execution. **Seeing:** 160 to 194 times in a two-season run
the offer names a person the seat holds no claim about, has no tie to and does not live beside,
because the Question is stamped from world truth and "follows a succession"; in the other direction three record kinds
reach 82 of 82 persons in the tick they occur, while person-to-person telling carried 5 to 12
claims of 22,000. **Reasons:** `why` is `None` on 24,822 of 24,822 witness claims, by construction.
**Levers:** 42% of acts are refused, fifteen offered verbs were refused every time (1,085 acts),
believed odds answer on 0.8% of the candidates they apply to, and one swapped pick changes 82 of 82
ledgers with nothing saying it was his. **Scenes:** six fights in six realm-seasons, all one man's
`capture`; the one steering choice is a certain, costless escape that deleted a death; a watcher
learns that a body changed. **Story:** 79 of 84 chains are two links of paperwork, and no exported
file holds a word for any Event kind or verb. **The single largest obstacle** is that the parity
contract is blind to all of it: keeping only the rows a budget can pack (dropping 78.3% of 18,689
offered rows) leaves the hash equal, so a port could show the player anything and pass. The second
is a false N-line inside the gate: 99.73% of the oracle's generators yield one uniform from a key
the port can already compute, so the draw recorder, its export and the replay (GO-16) are not
needed, and removing them makes parity checkable at any seed. Four proposals carry the repairs;
eleven resolutions are decided; one question (the draw, against a ratified Layer 1 row) returns to
Jordan; two findings of the prior GO lane are corrected (F-GO-16's measure; addendum B's "absent,
not greyed … built, by type").

## 1. NERS — cut tests on the port gate and the player surface, executed

The objects: the draw recorder (GO-16), the believed-odds query on the surface, the one suspension
(`PlayHost`), the offer's tail, the creation sheet. Each cut was run or measured; E is scored last.
Instrument for all of §1–§3: `probe.py` in the scratchpad directory above (modes `plain`, `census`,
`base`, `trunc`, `lever`, `host`, `verbs`); it writes nothing to the tree. Controls are named with
each reading; the standing control is that the instrumented run's `content_hash` equals the plain
run's (seed 0: `5ab73af282d0779646c38839fbab85d8` after one season, `bacd687f1470883b412be9638d0b0f88`
after two, in `plain`, `census` and `base` alike).

### 1.1 Cut GO-16 (the draw recorder, `oracle_draws.json`, replay): free, and worth more than it costs

**The N-line as the plan states it** (`workplans/…v11_part3.md:360`): the port will not implement
CPython's Mersenne Twister, so the oracle must record every draw of the pinned runs and the port must
replay them.

**The cut.** Make a draw a function of its key. `draw_factory` (`state/ids.py:87-90`) already computes
a 64-bit key `H(seed, tick, subject, purpose)` for every draw and then spends it seeding a
`random.Random` that is asked one question and thrown away.

**Measured** (`probe.py census 0 1`: counting shims on `random.Random` and `hashlib.blake2b`, no
generator method overridden, the build excluded; control: hash `5ab73af2…`, equal to plain). One
computed season of the realm at seed 0:

| | count |
|---|---|
| generators built | 18,702 |
| … that drew exactly once (`.random()`) | **18,651 (99.73%)** |
| … that drew six or more (a d10 pool: `randint` → `randrange` → `getrandbits`; 96 / 96 / 159 calls) | 48 |
| … that drew nothing | 3 |
| `blake2b` calls in the same season (ids, the mint, the digest) | 50,975 |

So the generator is being used as a hash-to-float function, 18,651 times a season, and the port
already has to own `blake2b` at two and a half times that rate for ids alone. If `u = (key >> 11) /
2**53` for the first draw of a key and `H(key | n)` for the n-th, then: nothing is recorded, nothing
is replayed, `oracle_draws.json` and its digest in GO-08 are not built, the port's own samplers run
inside the parity test, and parity is checkable at **any** seed and season count the port can run
rather than on the pinned slices at seeds 0–2. That last property dissolves the prior lane's F-GO-01
(the slices barely enter the two largest modules) and F-GO-03 (replay never exercises the port's
samplers) instead of patching around them.

**What dies with the cut.** (i) One declared re-pin of every seeded golden; the prior lane's
`11_GO_one_draw_owner.md` already declares one for the nine non-uniform sites, and the two fold into
one. (ii) The Mersenne Twister, which no requirement names. (iii) A sentence of ratified Layer 1
(`04` §C.12, the RNG row, "a seeded `RandomNumberGenerator` threaded like `World`", and rejection 4,
which still says "no roll exists yet"); the invariant behind it (never global, derived from the run
seed) is kept. Because (iii) touches ratified text it is returned to Jordan in §7 with the two
options; the proposal is `16_PESSIMIST_GO_keyed_draw_no_recorder.md`.

**Verdict: a false N-line.** GO-16 is necessary only if the oracle keeps a generator it does not
need. *Steelman tried:* the cut costs a `blake2b` per draw in GDScript where Godot's native generator
is free. It does not hold: under the present plan the shipped port's draws come from a generator the
parity test never ran, which is the defect; and seeding a Mersenne Twister per key (a 624-word
initialisation) is what the oracle pays today for each of those 18,651 single draws.

### 1.2 Cut the believed-odds column from the surface: free today, because the query answers nothing

**The N-line** (SURF-B `OfferRow.odds`; P3(b)): the player is shown what his person believes the
chance is.

**Measured** (`base`, seeds 0–2, two seasons; every person seated on `development_space`; the probe
asks `sheet.view.odds` exactly as `choose.odds_weight` does, for every seventh priceable candidate,
600 per seed; control: hash equal to plain at both seasons, so asking moved nothing).

| | seed 0 | seed 1 | seed 2 |
|---|---|---|---|
| candidate rows shown | 45,520 | 45,581 | 45,355 |
| … priceable (the verb contests something and writes in a band) | 10,024 | 11,144 | 9,997 |
| sampled | 600 | 600 | 600 |
| … whose prize is a fight's or a field's (`_estimated`) | 306 | 309 | 285 |
| … … believed odds answered | **0** | **0** | **0** |
| … whose prize is the social roll's | 294 | 291 | 315 |
| … … believed odds answered | **3** | **4** | **8** |
| … … believed `None` while the true odds exist | 291 | 287 | 307 |
| answered, and equal to the true odds to four places | 3 of 3 | 4 of 4 | 8 of 8 |

Fifteen answers in 1,800 (0.8%), all on `determine` and `arrest`, the two verbs with nothing unknown
in the roll. The three reasons are in `seam/wrappers/sigma.py`: mode (b) "IS NOT BUILT for a fight"
(`:376-378`) or a field; a person subject needs a capability claim the believer holds (`:288-294`),
and none is held; a heard contest needs `believed_room`, which `believed_chance` never passes
(`:428`, `:411`), so every contest before a bench answers `None` by construction.

**Verdict: an unexamined survivor, two ways.** For the player, P3(b) is unbuilt in effect: the column
would be blank on 99% of the rows it applies to. For the chooser, `odds_weighting: believed` is the
SHIPPED arm (`data/fixtures.py:971`) and multiplies a priceable candidate's pursuit term by 1.0 on
those same rows: the shipped arm and the `none` control differ on under 1% of priceable candidates,
which `fixtures.py:314` half-says ("moves these shares by nothing at any grid value"). Cross-listed to
CHAR and DICE. **S defect in the same function:** `odds_of` returns an untyped tuple that is the four
bands for a social roll, `(actor felled, subject felled, yielded, undecided)` for a fight and
`(Won, Lost, Unopposed)` for a field, "and the caller knows which it asked by the act's prize"
(`:372-374`): three ladders for "how will this go", one of which has a believed form.

### 1.3 Cut the one suspension (`PlayHost`): what dies is one lever for one person's victims

**Measured** (`base`, seeds 0–2 × two seasons, 83 persons; `host`, seed 2).

- Personal fights in six realm-seasons: **6**. Every one is the verb `capture`, and every one is
  initiated by the same person, `p_npc_013` (seed 0: none; seed 1: two; seed 2: four, in the last of
  which he is `felled` and dies). `fight` was attempted 0 times in 5,116 acts. `challenge` was
  attempted 295 times and refused 295 times (§2.3).
- `probe.py host 2 2 engage` (every person hosted, the decider always returning `engage`): season-0
  hash `a21ab6e12e356ccc4261bec1c93ca3b4`, equal to the automated run; 4 decider calls for two fights.
  `… withdraw`: hash `14b47698…`, 2 calls. So `engage` on every turn *is* the automated fight (the
  control holds, as `modules/combat/wrapper.py:545` says), and the whole of "steered" is one
  binary, of which one value is the default.

**Verdict: narrowed, not passing.** N holds bottom-up (the module can be suspended and resumed with
no hash cost) and fails top-down (the season brings a seat to a fight only if that seat is
`p_npc_013` or one of the four people he tries to seize), laterally (no other module has a decider:
prior lane, F-GO-08 and F-GO-18) and diagonally (a bystander's deposit is `body.changed`, with no
kind that says a fight occurred: §2.4). The cut would lose a `withdraw` for about five seats in 83.
This is not a recommendation to cut; Jordan's stated intent is the opposite. It is the measure of
how far "PLAYABLE and AUTOMATED are one code path" is from "a duel can be played".

### 1.4 Cut the offer's tail: free for the port gate, which is the finding

`probe.py trunc 0` (§2.0a, and F-PES-GO-01): keeping only the rows a budget can pack leaves the hash
equal. For an NPC the tail is inert by construction. For a player it is the aperture, and the gate
pins none of it. The tail is also where the size is (`base`, two seasons, per seed):

| | seed 0 | seed 1 | seed 2 |
|---|---|---|---|
| deliberations | 774 | 783 | 771 |
| candidate rows per deliberation: mean / median / **max** | 58.8 / 32 / **543** | 58.2 / 29 / **531** | 58.8 / 31 / **544** |
| distinct verbs per deliberation, mean | 21.8 | 21.6 | 21.7 |
| separate questions on the view: mean / max | 24.4 / 260 | 24.4 / 252 | 24.7 / 245 |
| scene budget, mean | 5.49 | 5.51 | 5.51 |

The prior lane measured one seat (22 to 38 rows, F-GO-19). Realm-wide the median agrees and the tail
does not: one deliberation in each seed shows more than 530 rows against a budget of about five
scenes, and a view carries up to 260 questions against a cap of 12 claim ids. The design set's
legibility figure is 5 to 8 options.

### 1.5 The creation sheet: survives the cut test only because nothing else shows a seat

`creation_sheet` at seed 0 (probe in §8, E9): 83 rows, of which **37 are cohorts** ("the people of
Valorsplatz"), offered as seats with nothing on the row that says so. `capability` is non-empty on 2
rows, `attributes` on 0, `conviction` on 46, `pursuits` on 83; 51 distinct `(capability, pursuits)`
pairs among 83 rows. The Senior Inquisitor (`p_npc_004`) and the fugitive whose standing goal is to
evade him (`p_npc_088`) show the same `capability` (`{'inquiry': 2}`) and differ by pursuit weights
and four conviction counts. Office, place, faction, goal and kin (the live Tenures that decide what
the seat's game is) are not on the row. Cut it and a player cannot choose a person at all, so it is
N; what it shows does not let a player choose *between* persons, so R fails on "customization" and
P1(e) fails at the first screen. SURF-B's `Situation.holdings` is the right reading and is not wired
to creation; the edit is one field (§5, resolution 6).

### 1.6 E, last, as a ratio

What N and R found the player surface must carry: a situation, an offer he can tell apart, a result
for each act, a reason, a way to steer a scene. What exists per unit of mechanism: the offer is one
ranked list with a median of 30 rows and no grouping; the odds column answers 0.8% of the time; the
reason field is `None` by construction; the one scene decider is a binary whose default value is the
automated run. Against that, the gate's apparatus for the same layer is ten positions, an exporter
per registry, a recorder and a replay. **The overhead sits on the side that is not shown to anyone;
the side that is shown has almost none, and what it has is not legible.** E is poor in both senses of
its definition: unnecessary overhead (GO-16) and no way to "intuit complex outcomes from simple
choices" (the offer).

### 1.7 False N-lines and unexamined survivors

| object | N-line claimed | finding |
|---|---|---|
| GO-16 recorder, `oracle_draws.json`, replay | the port cannot reproduce the oracle's draws | **false**: 99.73% of generators yield one uniform from a key the port can already compute (§1.1) |
| GO-08's "draw log digest" and "no Mersenne Twister vectors" clauses | follow from GO-16 | fall with it |
| "the pinned slices pin the game the port must run" | hash parity is the contract | **false for the player surface**: 78.3% of offered rows and every reading are outside the hash (§1.4, F-PES-GO-01) |
| `odds_weighting: believed` as the shipped arm | a believed chance weighs a contested choice | **unexamined survivor**: answers on 0.8% of priceable candidates; the arm is the control on the rest (§1.2) |
| `View.odds` on the player's sheet | the player sees believed odds | **unexamined survivor**: nothing calls it from the sheet (prior lane) and it would answer `None` (§1.2) |
| `PlayHost` | a fight can be played | **narrowed**: reachable for one initiator's `capture`; `engage` is the automated run (§1.3) |
| `Seen.why` | a witness may hold a motive | **dead carrier**: `_term_why` returns `None`; 0 of 24,822 `seen` claims in three seeds carry one (§2.2) |
| `Event.ending` | the fight's outcome per party | **no reader**, as the field's own comment says; the only thing that would tell a bystander who won (§2.4) |

## 2. Premise audit — the five sentences of presentation

### 2.0 The first account: what each sentence means in ordinary words (written before the probes ran)

Written from the words alone, as a player of strategy and role-playing games would take them, and
committed to this file before any measurement below existed. Each link is a thing the game must do
for the sentence to be true.

**P1. "A player sees what their character could see."**
(a) The character has a place, senses, company and holdings. (b) The player is shown what lies within
them: where he stands, who is with him, what he holds, what he has been told and by whom. (c) The
player is not shown what lies outside them: a death in another town is unknown until word arrives.
(d) What is shown may be wrong, because a rumour is shown as a rumour. (e) The converse holds too:
nothing the character could plainly see (his purse, his wound, the people in the room) is hidden from
the player. *Genre:* a Crusader Kings player expects an omniscient ledger and would be surprised by
darkness; a Disco Elysium or Pentiment player expects exactly this sentence. Both would be surprised
if the menu of actions named a thing the character has never heard of.

**P2. "A player can read why a thing happened."**
(a) A thing happened that the player knows of. (b) It had causes: a person's act and that person's
reason, or a process of the world. (c) The game shows the cause as far as the character could know
it: who did it, in answer to what. (d) Where a roll decided it and the roll was his own, he is shown
what went into it and how it fell. (e) Where he cannot know, the game says "unknown", not nothing.

**P3. "A player can choose a lever and see its effect."**
(a) Several choices are offered that a player can tell apart. (b) Before choosing he can anticipate
what each would do: the chance, the cost. (c) Choosing one rather than another changes what happens.
(d) The change is shown to him and is traceable to the choice, at once (the result of the act) and
later (what others did about it).

**P4. "A duel and a battle can be watched, steered or skipped."**
(a) A duel or battle occurs with the player's person in it or near it. (b) *Watched:* an account of
its course, blow by blow or phase by phase, is presented with no input. (c) *Steered:* at decision
points his input changes the course. (d) *Skipped:* the outcome is produced at once, by the same
resolver, at the same odds. (e) The three are one fight, not three.

**P5. "The story the world tells is legible as a story."**
(a) The world produces sequences of events that answer one another. (b) A record of them exists.
(c) The record can be read in order with who, what and in answer to what. (d) Someone inside the
world, and so the player, can follow at least one thread from its opening to its end. (e) The things
in it have names a person would say aloud.

### 2.0a Established early (kept here in case the lane is interrupted; restated in the findings)

- **The parity contract cannot see the player's offer.** `probe.py trunc 0`: every one of the 83
  persons seated on `development_space`, the pick keeping only the head of the offer a budget can pack
  (`budget × interactions_per_scene`, 3). One season, seed 0: 383 deliberations showed **18,689**
  candidate rows; the pick kept **4,063**; `content_hash` = `5ab73af282d0779646c38839fbab85d8`, equal to
  the plain run (control, same session: `probe.py plain 0 2`, season 0). So 78.3% of every row a player
  is offered is outside anything the port gate pins, and so is every reading the `11_GO` proposals add
  (none is hashed; a `Question` "is never hashed", `state/carriers.py:538`).
- **"Why" is `None` by construction.** The one field named `why` on the one witness value
  (`epistemic.py::Seen.why`) is filled by `_term_why`, whose body is `return None` (`epistemic.py:939-950`);
  `Candidate.why` was deleted (`state/carriers.py:591-595`); a `Claim` has no cause field.

### 2.0b The second account: what the code's own notes say, in aggregate

Read after §2.0 was written. The notes describe a surface that is sound by type and thin by content,
and they say so more candidly than the design documents do.

- *Seeing.* "A View holds IDS, NEVER REFERENCES … any attempt to reach a world collection through a
  View raises" (`state/carriers.py:457-458`); the sheet "holds copies" and "ranks and selects; it
  never forms" (`decision/sheet.py:21-26, 36-41`). But `goal_referents`' `seat_holders` "IS A WORLD
  READ WITH NO CLAIM BEHIND IT … it hands `p` the identity of whoever sits on a throne he may never
  have been told of" and "the referent FOLLOWS A SUCCESSION" (`queries/world_q.py:2847-2859`). The
  note says it follows the precedent of ED-IN-0292 (2). **It reads that precedent backwards.** The
  row that closed item (2) (`registers/editorial_ledger_in.jsonl:74`, 2026-10-26, opened) says the
  answer TAKEN is "a vacancy reaches a person as a claim deposited through the channels, not as a
  world stamp; AX-7 … prohibits the engine's resolution being handed into belief unmediated, which
  the stamp … is", with offices-as-common-knowledge left open "as a channel's reach". So the world
  read is against the taken answer, not under it.
- *Reasons.* "NO CHANNEL SUPPLIES `why`, AND THAT IS `R8.4`'s DEFECT … Case 4 (*no discernible
  reason*) is therefore every deposit today" (`rosters.yaml:1303-1306`). `chronicle()` "shows no scar
  or crisis as an event" (`sheet.py:29-34`). `harness/chronicle.py` is "read OUTSIDE the simulation"
  and "says 'answers' and means 'had among its causes'" (`:1`, `:44-48`).
- *Levers.* The odds are "what he BELIEVES", `None` "where a factor is unknown to him … never a
  figure"; mode (b) "IS NOT BUILT for a fight" (`seam/wrappers/sigma.py:260-278, 376-378`).
- *Scenes.* `engage` "is exactly [the automated fight] every turn"; `withdraw` is "the loop's
  existing UNRESOLVED exit, taken early … no UPSET_FLOOR draw"; the set is an `[ASSUMPTION]`
  (`modules/combat/wrapper.py:545-550`). "Nothing records the mode" (`queries/inputs.py:191`).
  `Event.ending`: "NO PRODUCTION READER EXISTS AT THIS COMMIT" (`state/carriers.py:303`).
- *Story.* An Event has "no actor … no target … no stat_deltas", by decision (`carriers.py:248-250`);
  who did it is "a per-witness Claim".

So the notes' account is: the player sees only claims (true by type, with one admitted world read);
reasons are not carried (admitted); odds are believed and often unknown (stated as a virtue, not
measured); a fight has one binary; the story is the log, read from outside. The third account is
what ran.

### 2.1 P1 "A player sees what their character could see" — holds for the View, fails through the Question, fails the other way by broadcast, and fails its converse by omission

| link | ordinary meaning | the notes | what ran |
|---|---|---|---|
| (b) shown what is within reach | place, company, holdings, what was told and by whom | the sheet copies his own fields; the View is ≤ 12 claim ids | the sheet carries no place, company or holding (prior lane, B3.2). Of the claims held at the end of two seasons, `told_by` is 9,708 of 22,958 (seed 0), 8,102 of 21,469, 8,214 of 21,558; a claim with a speaking teller (`chain` non-empty) is **12, 5 and 5**. "By whom" is blank on 99.9% of what he was told |
| (c) not shown what is outside | a death elsewhere is unknown until word comes | reaching past the View raises | **the offer names what he does not hold.** 479 / 468 / 414 candidate rows (1.05%, 1.03%, 0.91%), in 105 of 774, 90 of 783 and 76 of 771 deliberations (13.6%, 11.5%, 9.9%), name an entity the person holds no claim about, has no live Tenure with and shares no container with |
| (c′) and the reverse | news travels | channels admit by presence, knot, document, remit, record | **some kinds reach everyone at once.** Seed 2: `p_npc_013` dies; `person.died` reaches 7 persons, the `tenure.closed` that follows reaches **82 of 82** in the same tick. In the lever runs a `dispensation.issued` and an `order.given` each reach 82 of 82 |
| (d) a rumour is shown as a rumour | source and confidence | `Claim.source`, `confidence`, `chain` | built; exercised only in its anonymous form |
| (e) nothing plainly visible is hidden | purse, wound, the room | `Situation.holdings` is proposed (SURF-B) | absent at play; absent at creation (§1.5) |

**The worked case for (c), identical in seeds 0, 1 and 2.** Carin Vedel (`p_npc_088`), of the
restoration movement, lives in a workshop in settlement 026 and holds three claims, each that an
acquaintance exists (`p_npc_003`, `_041`, `_087`). Her first question is
`q:need:goal_restoration_evade_capture`, whose referents are `p_npc_004` and `p_npc_038`: the Senior
Inquisitor and the Cardinal Justice, resident in the cathedral of settlement 036, read off their live
`hold` Tenures by `goal_referents`. Her offer then carries `train`, `tend`, `forgive`, `challenge`,
`sabotage`, `surveil`, `interview`, `forge`, `release` … each on one of the two (40 of the first 40
recorded rows). The occurrences by route: a classed referent naming a person 160 / 191 / 194; a
classed referent naming a rung 273 / 237 / 185; a rung as an operand 43 / 37 / 32; a site 3 / 3 / 3.
**Only the person route is established** (traced to `seat_holders`). The rung routes were not traced
to a stamp and may be larders in a seat's purview, which a seat-holder may fairly know; they are not
counted in F-PES-GO-03.

*Steelman.* A fugitive knows who hunts her, and great offices are common knowledge. In the fiction,
yes. In the engine her knowledge is her ledger, and the ledger and the offer disagree; the player is
shown both. And because the referent "follows a succession", the offer names a new office-holder
the moment he is seated: **the menu is a faster news channel than any the world has.** A Pentiment
player would not be surprised that she knows the Inquisitor's name. He would be surprised to be
offered `tend` on a man in another town whom her own journal has never mentioned, and to learn of
his replacement from a button.

**Verdict.** Genre: surprised, at (c) and (c′). Intent: the View corresponds; the Question does not.
Names: `told_by` does not mean told by someone (it is the record's channel); `seen` claims are the
only ones with a `who`.

### 2.2 P2 "A player can read why a thing happened" — fails at "in answer to what", though the material is in the ledgers

| link | what ran (seeds 0 / 1 / 2, two seasons) |
|---|---|
| (c) who did it | of the `seen` claims held at the end, `who` is filled on 4,045 of 8,694 (46.5%), 4,079 of 8,072 (50.5%), 4,093 of 8,056 (50.8%) |
| (c) in answer to what | `why` is filled on **0 of 24,822**. A `Claim` has no cause field; the Event's `causes[]` is dropped at the deposit (`loop/witness.py:601-608` cites the Event as the cause of the *deposit*, and the claim carries none of it) |
| (d) his own roll | a degree rides 433 of 5,116 acts (8.5%); 39 of the 48 verbs used never carry one; the margin stops at the seam (prior lane) |
| (e) "unknown" rather than nothing | the actor receives a deposit from an Event of his own act in 1,593 of 1,703 acts (93.5%), 1,566 of 1,706 (91.8%), 1,587 of 1,707 (93.0%). The whole gap is three inquiry verbs: `research` 20 of 71, 19 of 95, 19 of 67; `surveil` 6 of 44, 9 of 58, 5 of 55; `interview` 9 of 28, 4 of 17, 9 of 25. Every other verb is at 96% or above |

**The control that cuts the other way.** Are the links of a story held by anyone? `storybar.read`
over consequence acts, chain ends at cross-person depth ≥ 2, each walked back (`chronicle`'s own
walk); a link is "held" by a person who did the act or holds a deposit from one of its Events
(exact, by recording `TRACE.claim`).

| | seed 0 | seed 1 | seed 2 |
|---|---|---|---|
| chains (ends at depth ≥ 2) | 29 | 27 | 28 |
| depth 2 / 3 / 4 | 28 / 0 / 1 | 27 / 0 / 0 | 24 / 4 / 0 |
| every link held by one person | 29 | 27 | 28 |
| every link held by one **bystander** (acted in none of it) | 23 (79%) | 20 (74%) | 22 (79%) |
| no bystander holds any link | 2 | 2 | 2 |

So three chains in four are held whole by someone who took no part. The world's short stories do
reach witnesses; what does not reach them is that the links are links. This corrects the pessimistic
reading in both directions: the surface is not starved of material (a "does not work" I expected and
did not find), and the prior lane's F-GO-16 ("a person cannot read what his own act came to", 7 of 15
by a kind-and-subject matcher) overstates the own-act gap, which is 6 to 8% and confined to inquiry.

**Verdict.** Genre: surprised (every strategy game answers "why did he do that" at least with a
tooltip). Intent: does not correspond; the admitted defect `R8.4`. Names: `why` names a motive the
engine does not keep; what it *could* lawfully hold is the antecedent the witness himself holds
(proposal `16_PESSIMIST_GO_a_witness_may_connect_what_he_holds.md`).

### 2.3 P3 "A player can choose a lever and see its effect" — the lever moves the world; the offer is half inert; the effect is unattributed

**(a) and (b), the offer.** Per verb, three seeds, two seasons, automated (`probe.py verbs`; control:
the three hashes equal the `base` runs' second-season hashes). 5,116 acts by 48 of the 66 resolvable
verbs.

| | acts | share |
|---|---|---|
| refused (every Event of the act is a refusal kind; nothing written) | 2,151 | 42.0% |
| by verbs refused **every time**: `challenge` 295, `train` 221, `exchange` 137, `sabotage` 107, `comply` 87, `accept` 82, `raze` 49, `covenant` 31, `construe` 24, `seize` 15, `evade / defy` 12, `found` 11, `build` 9, `confer` 3, `pardon` 2 | 1,085 | 21.2% |
| carrying a degree (a graded draw): `research`, `surveil`, `tell`, `speak`, `lie`, `argue`, `capture`, `march`, `determine` | 433 | 8.5% |
| writing anything but a claim ledger | 2,011 | 39.3% |

Eighteen resolvable verbs were never attempted in any seed (`arrest`, `examine`, `fight`,
`interrogate`, `succeed`, `surrender`, `work`, the six army verbs and others). So of 66 verbs, 33 have
never been seen to do anything in six realm-seasons, and nine resolve by a graded draw. The GAME and
CORE pessimists and the VERBS lanes found the refusals from the engine's side
(`16_PESSIMIST_GAME.md` §1.2, `16_PESSIMIST_CORE.md`, `14_VERBS_*`); this is an independent probe that
agrees. What is added here is what it does to the surface: **the offer is not "what he may attempt"**.
The prior lane's intent 1 ("a control he cannot use is absent, not greyed … built, by type",
addendum B, B3.1) is false as measured. The ranked head of the Senior Inquisitor's first
deliberation is `open_case`, then `train` four times on the Cardinal Justice; a player who takes the
engine's own ranking is refused on most of his season. Believed odds: 0.8% (§1.2).

**(c) the choice changes what happens: holds, strongly.** `probe.py lever 0 <seat> <mode>`, one
season; baseline `ranked` (hash `5ab73af2…`, equal to plain: the control).

| seat, and the one change at his first deliberation | hash | other persons whose ledger differs | claims differing in others' ledgers | claims differing in **his own** ledger |
|---|---|---|---|---|
| `p_npc_004`, takes only the last-ranked row (`forge`) | `c093236b…` | **82 of 82** | 1,022 | 97 (45 lost, 52 gained) |
| `p_npc_004`, does nothing | `ab3a9d01…` | 9 of 82 | 35 | 4 |
| `p_npc_006`, takes only the last-ranked row (`speak`) | `aa014148…` | 3 of 82 | 16 | 7 |
| `p_npc_089`, takes only the last-ranked row (`survey`) | `1064b434…` | **82 of 82** | 799 | 51 |

**(d) the effect is shown and attributable: fails.** His ledger does change (4 to 97 claims), so the
effect reaches him. Nothing in a claim says it follows from his choice: no cause field, no `why`. And
the reach is bimodal for a reason unrelated to the weight of the choice: where the changed season
includes a record-channel kind (`dispensation.issued`, `order.given`), all 82 other ledgers move;
where it does not, three or nine do. Doing nothing moved less of the world than swapping one act.

**Verdict.** Genre: surprised, twice: by a menu half of which cannot be done, and by a world that
answers one swapped act with a different realm and says nothing of why. Intent: (c) corresponds;
(a), (b), (d) do not. Names: "candidate" is honest; "ranked" promises advice the fold then refuses.

### 2.4 P4 "A duel and a battle can be watched, steered or skipped" — skipped holds; steered is one binary whose other value is a certain escape; watched has no account; and almost no seat meets either

- **(a) It occurs.** Six personal fights in six realm-seasons, all `capture`, all begun by
  `p_npc_013` (§1.3). `march`: 25 acts, 14 refused, 10 unopposed, **one fought field** (`field.lost`,
  seed 2, held by 3 persons). A seat chosen at random from the 46 named persons meets a fight if it
  is `p_npc_013` or one of his four targets.
- **(d) Skipped: holds.** With no host the provider decides; with a host that always engages the
  hash is the automated run's (`a21ab6e1…` and `89109213…` at both seasons). One resolver.
- **(c) Steered.** `probe.py host 2 2 withdraw`: five fights attempted, five decider calls (each at
  turn 1), and **no fight Event of any kind in the log**: no `body.changed`, no `person.died`. In the
  automated run the same captor wounds or is yielded to three times and is felled the fourth. So a
  hosted party ends any fight, with certainty, unhurt, by one return value; and the decider is asked
  once per fight, not per party, with a view (`turn`, `claimants`, `wound_state`) that does not say
  whose side it decides. The PC lane found the free exit in the module (`03_PC_audit.md` F-PC-05,
  F-PC-14, 300 seeds; `03_PC_exits_withdrawal_recovery.md`); this is the same defect confirmed
  through the season, where it deletes a death. It is a deterministic outcome of a thing that could
  go either way (R-09) and it breaks the ruled doctrine's one constraint (`E[auto] ≈ E[played]`,
  ED-SC-0013 §6): mode-shopping with a certain payoff.
- **(b) Watched.** A fight's Events are `capture.declared`, `body.changed` (degree `Wounded`) or
  `person.died`; eight persons hold a deposit, six of them bystanders. The deposit is
  `(subject, "body.changed", True)` and a `seen` with a `who`. No kind says a fight took place; the
  band is on the Event, not on the claim; `Event.ending` (who yielded, who was felled) has no reader;
  the module's `trace` returns to the wrapper (`seam/wrappers/combat.py:398-422`) and reaches no
  Event. A watcher learns that a body changed.
- **(e) One fight, not three.** Holds for skipped and steered. "Watched" is not a third fidelity; it
  is the absence of the other two.

**Verdict.** Genre: surprised at (c) (no tactics game lets the defender cancel an attack) and at (b).
Intent: the suspension corresponds to its own note and to nothing a player would call steering.

### 2.5 P5 "The story the world tells is legible as a story" — a record exists and is read from outside; inside, it is two-link paperwork, without connectives or words

- **(a), (b) Sequences and a record: hold.** 440 to 496 consequence acts per seed; 27 to 29 chains.
- **(c) Readable in order with who and in answer to what: only from outside.**
  `harness/chronicle.py` (seed 0, two seasons) prints depth 4: `conceal` → `create_record` →
  `create_record` → `create_record`. It holds `w` and `SeasonDriver.act_of`; no person-side reading
  can do the same, because the actor of an Event is in the act store and "in answer to" is in
  `causes[]`, and neither crosses into a ledger.
- **(d) A thread followed from inside.** 74 to 79% of chains are held whole by a bystander (§2.2).
  What the chains are, by their verbs: seed 0, `issue → create_record` ×6, `create_record →
  create_record` ×3, `commit → petition` ×3; seed 1, `create_record → create_record` ×5, `issue →
  create_record` ×5; seed 2, `commit → create_record` ×3, `issue → create_record` ×3, and the one
  chain in three seeds with a body in it, `commit → capture → issue` ×2. 79 of 84 chains are two
  links long.
- **(e) Names.** Persons, settlements and offices have names. Of the 72 / 75 / 80 Event kinds and
  46 / 46 / 48 verbs that occurred, **0** have an entry in `engine/engine_params/names.json` (122
  names in five classes: clock, clock_full, faction, mech, npc), the only exported vocabulary. No
  export carries a word for `record.created`, `cover.assumed` or `evade / defy`.

**Verdict.** Genre: a Dwarf Fortress or Crusader Kings player expects to be able to read back what
happened; here he can, as a developer. Intent: the record corresponds; legibility from a seat does
not. The churn finding (`20_NARRATIVE_CHURN.md`) and the GAME pessimist's "chains are plentiful and
are about paper" are confirmed from the seat's side.

## 3. Emergent narrative, read for legibility

The method's questions, asked of what a seat can be shown. "Exported" is taken at its two senses:
what the oracle exports as files today, and what it would hand a client as typed readings.

**3.1 What can be shown at all (enumerated from code).** As files: eight JSON artifacts under
`engine/engine_params/`, all parameters and rosters; none holds a run, an Event, a claim or a word
for one. The planned pins (GO-08) add hashes, an initial world and act traces for seeds 0–2. So no
story is exported as data; the port regenerates the world and must read it through a seat. As
readings, a seat's lawful material is its ledger, and a claim is one of six shapes
(`loop/witness.py`): *a thing of kind K happened concerning S* (value `True`: no band, no actor, no
cause); *S's P is V* (an observation the fold read); *I saw someone (who, or not) do something of a
stratum at S* (`seen`); *this record says …* (content); the same, told (with a chain if a person
told it); *I found …*. The atoms a story needs and no shape carries: in answer to what; with what
result band; how a fight went; who told me.

**3.2 What is produced in computed play.** Audience of every consequence act (persons other than the
actor holding a deposit from it), two seasons:

| audience | seed 0 (446 acts) | seed 1 (440) | seed 2 (496) |
|---|---|---|---|
| nobody | 253 (56.7%) | 252 (57.3%) | 307 (61.9%) |
| one person | 59 | 55 | 33 |
| 2 to 5 | 46 | 38 | 57 |
| 6 to 20 | 67 | 77 | 78 |
| more than 20 | 21 | 18 | 21 |
| deposits by source: firsthand / record or remit (`told_by`) / inferred | 676 / 1,626 / 9 | 722 / 1,422 / 13 | 767 / 1,622 / 15 |

Control for "the world reaches nobody": of Events that are not ledger bookkeeping (`claim.deposited`,
`claim.decayed`), 2,321 of 2,809 at seed 0 deposit a claim with someone (83%), so the log is not
dark; it is the *acts that change something* that are mostly unwitnessed, and those that are
witnessed widely are witnessed by everyone at once through the record. Person-to-person telling
carried 12, 5 and 5 claims.

**3.3 Dead ends.** A failed search leaves its searcher nothing (§2.2). A challenge never leads to a
duel (295 of 295 refused). A fight leaves no account (§2.4). A motive is never held (§2.2).

**3.4 What a player's choice changes.** Everything or almost nothing, by whether a record kind is in
the changed season; never attributably (§2.3).

**3.5 The shape of the tail: are all runs the same run?** Across seeds 0, 1, 2 at two seasons: acts
1,703 / 1,706 / 1,707; deliberations 774 / 783 / 771; rows offered 45,520 / 45,581 / 45,355; the
largest offer 543 / 531 / 544; consequence chains 29 / 27 / 28; the same first forty leak rows; the
same captor; the same three marchers (`p_npc_007`, `_074`, `_052`). The seed moves which capture
ends in a wound and whether the captor dies. At this horizon the realm is one authored opening with
seeded margins, and a second playthrough from another seat would meet the same events in the same
places. Longer horizons were not run (the machine was loaded; `20_NARRATIVE_CHURN.md` and the GAME
pessimist own them).

**3.6 Are the persons' reasons readable afterwards?** No: `why` 0 of 24,822; `who` on half.

**3.7 The extremes.** `build_realm(0, cap)` at cap 0, 1 and 2 (37 cohorts and 0, 1, 2 named
persons), one season, every seat on the sheet: no raise; 158 / 161 / 166 deliberations, 319 / 326 /
338 acts, 37 one-row offers per run. The surface is complete at the small end in the narrow sense
that it does not break. At the large end one sheet holds 544 rows and a view 260 questions, with no
grouping (§1.4). A hundred factions was not run.

**3.8 The story bar from a seat.** `storybar` and `chronicle` have one arm and read the whole log
with the act store; a seat has neither. The legibility reading above (links held, audience, sources)
is the seat-side counterpart and could be one more column on `chronicle --chains`; it is not
proposed as an instrument of its own (§0.1 pt 5).

## 4. Findings, ranked worst first

Severity uses the suite's three grades. "Requirement" names R-01..R-09 where one is touched; several
of these block port validity or the standing requirement instead.

**F-PES-GO-01 · blocks port validity · the parity contract cannot see the player's surface.**
*Claim:* a port that mis-forms, drops or reorders every offered row a budget does not pack matches
every pin. *Falsifier run:* `probe.py trunc 0`; *outcome:* 18,689 rows shown, 4,063 kept, hash equal
to plain. *Control:* the same run with `take_ranked` (`base`) is also equal, and a one-row change by
one seat moves the hash (`lever`), so the instrument can see a difference when there is one.
*Touches:* R-04, R-05 as a player meets them. *Consequence:* the freeze certifies the NPCs' game and
nothing of the player's. *Fix:* a `surface` block in the pins (proposal
`16_PESSIMIST_GO_surface_pins.md`).

**F-PES-GO-02 · degrades the port · GO-16 is a false N-line, and its cost is the gate's validity.**
§1.1. *Falsifier:* a season in which a material share of generators draw more than once; *outcome:*
48 of 18,702. *Control:* hash equal under the counting shim. *Touches:* none of the nine; removes
F-GO-01 and F-GO-03. *Fix:* `16_PESSIMIST_GO_keyed_draw_no_recorder.md`; one question to Jordan (§7).

**F-PES-GO-03 · degrades narrative · the offer names persons the seat does not know, and follows a
succession.** §2.1. *Falsifier:* zero rows naming an unheld person under a generous closure (own
claims, own Tenures, everyone sharing a container); *outcome:* 160 / 191 / 194 occurrences through
classed referents. *Control:* the same closure passes 99% of rows, so it is not vacuous. *Touches:*
R-08 (non-omniscient). *Fix:* `16_PESSIMIST_GO_the_offer_names_what_is_held.md`.

**F-PES-GO-04 · degrades narrative · "why" is `None` by construction while three chains in four are
held whole by a bystander.** §2.2. *Falsifier:* one `seen` claim with a `why`; *outcome:* 0 of
24,822. *Control:* `who` is filled on half, so the term machinery works. *Touches:* R-07, R-01 as
legibility. *Fix:* `16_PESSIMIST_GO_a_witness_may_connect_what_he_holds.md`.

**F-PES-GO-05 · degrades narrative · believed odds answer on 0.8% of the candidates they apply to,
and the shipped odds arm is the control on the rest.** §1.2. *Touches:* R-08, R-09 as shown.
*Fix:* not GO's; three edits at `seam/wrappers/sigma.py`, listed in §5 (resolution 4) and cross-listed
to CHAR and DICE. Until then SURF-B's `OfferRow.odds` should ship typed and be expected blank.

**F-PES-GO-06 · degrades narrative · what a person learns of others' acts is nothing (57 to 62% of
consequence acts) or everything at once (4 to 5%), and almost never told by someone.** §3.2, §2.1
(c′). The certain, simultaneous reach of record kinds is a deterministic outcome (R-09) owned by WR
and CORE; listed for them. *Falsifier:* a record kind whose deposit count varies across persons at
the tick; *outcome:* 82 of 82, three kinds observed.

**F-PES-GO-07 · degrades narrative · the offer is half inert: 21% of all acts are spent on fifteen
verbs that are refused every time, and the surface presents them as available.** §2.3. Confirms the
GAME, CORE and VERBS lanes; the addition is that addendum B's intent 1 "built, by type" is false.
*Fix:* theirs (`16_PESSIMIST_CORE_a_refusal_is_remembered.md`, `16_PESSIMIST_FI_D_withhold_what_has_no_product.md`
and the VERBS proposals); GO's part is resolution 5.

**F-PES-GO-08 · blocks the standing requirement · PLAYABLE's reach is one person's one verb, its
only choice is a certain escape, and a watched fight has no account.** §1.3, §2.4. Confirms F-PC-05
and F-PC-14 through the season; adds the reach (6 fights, one initiator, `fight` 0, `challenge`
0 of 295) and the missing account. *Fix:* PC's proposals; GO's part is resolution 7.

**F-PES-GO-09 · degrades narrative · the offer's size has a tail the prior measure missed: up to 544
rows and 260 questions at one deliberation.** §1.4. Extends F-GO-19. *Fix:* SURF-B `OfferRow.occasion`
as proposed; the surface pin (F-PES-GO-01) makes the grouping checkable.

**F-PES-GO-10 · degrades narrative · the creation sheet cannot tell seats apart and offers 37 cohorts
as persons.** §1.5. *Fix:* resolution 6.

**F-PES-GO-11 · CORRECTS F-GO-16 · the own-act gap is 6 to 8% and confined to three inquiry verbs.**
§2.2. `receipt` (SURF-B §3) is still the right reading; its justification is the band and the
fold's reads, not that the actor is told nothing.

**F-PES-GO-12 · hygiene · no exported word for any Event kind or verb.** §2.5. *Fix:* in
`16_PESSIMIST_GO_surface_pins.md` §3 (a vocabulary block behind the names exporter).

**F-PES-GO-13 · hygiene · the gate's exit line 4 lists a check that reports drift and passes.**
`python tools/export_npc_roster.py --check` prints "9 row(s) differ from the derivation — REPORTED,
NOT FAILED" and exits 0 (`tools/export_npc_roster.py:196-199`). The other seven `--check`s ran
current at this commit (§8, E8). The roster is hand-correctable by design, so the behaviour is
intended; the defect is the card calling it a round-trip. *Fix:* resolution 8.

## 5. Resolutions decided

Ladder steps as `CLAUDE.md` §0. "P-" names the proposal file under
`proposals/16_PESSIMIST_GO_*.md`.

| # | inconsistency, gap or unclear passage | resolution | step | carried by |
|---|---|---|---|---|
| 1 | hash parity is called the port's contract; it sees none of the player's offer | the pins gain a `surface` block: per pinned seed, for a declared set of seats, a digest per deliberation of the ranked candidate rows, the question ids and the budget, in GO-07's encoding | 5 | P- `surface_pins` |
| 2 | GO-16 records draws the port could compute | the draw is a function of its key; GO-16 is not built; GO-08 loses the draw-log digest and gains draw vectors | 5, and Jordan for the Layer 1 row (§7) | P- `keyed_draw_no_recorder` |
| 3 | the Question carries world reads into the offer (`seat_holders`), against the View's own rule | `seat_holders` reads the holders the person's own ledger names; the world builder deposits the holders of public seats as record-channel claims at build, by a draw | 1 (ED-IN-0292 (2)'s closing row, `editorial_ledger_in.jsonl:74`: a claim through the channels, not a stamp; the docstring's own named revert) | P- `the_offer_names_what_is_held` |
| 4 | believed odds answer `None` almost everywhere | three edits at the owner, in order: `believed_chance` passes the believer's own `believed_room` (his claims of `reception` and `proofs` where he holds them); a believed form for a module estimate, fed from the capability and body claims he holds about the other party; `odds_of` returns a typed record naming its ladder | 5 | listed for CHAR and DICE; no GO proposal |
| 5 | a verb refused every time is offered as a row | SURF-B's `Offer.withheld` stays own-state only; the world-side case is the CORE proposal (a person discounts what he has been refused). GO adds nothing: a surface-side filter would be a second owner of admission | 4 | — |
| 6 | the creation row hides what decides the seat's game | `CreationRow` gains `holdings` (the live Tenure pairs SURF-B's `Situation.holdings` already defines) and `cohort: bool`; `creation_sheet` takes the same reader | 4 (SURF-B) | P- `the_offer_names_what_is_held` §4 |
| 7 | a watched fight has no account | SURF-B rule 4 (the outcome carries a typed `trace`) stands; add: WITNESS deposits the band Event's `ending` to a co-located witness as one observation claim on the fight's subject (who yielded, who was felled), the "body Observation" home `state/carriers.py:303-305` already names for it; no new field on `Seen` | 5 | listed for PC (`03_PC_typed_outcome_one_door.md`) |
| 8 | exit line 4 counts `export_npc_roster --check` among round-trips | the card's line 4 names it apart: "reports hand-corrected rows; fails only on a row naming no case, place or seated person" | 3 (the tool's own text) | — (a card edit at B10-20's open) |
| 9 | `Seen.why` is declared and never filled | `why` is the id of the claim the witness himself holds about an antecedent of the Event, supplied by a draw | 5 | P- `a_witness_may_connect_what_he_holds` |
| 10 | F-GO-16's measure | corrected (F-PES-GO-11) | — | this file |
| 11 | "one code path" was shown for one seat | shown for all 83 seats at once, two seasons, seeds 0–2 (hash equal to the automated run) | — | this file, §8 E2 |

## 6. Stories a seat can and cannot be shown

**Can, today (each seen in a run):** a proclamation reaching the whole realm (a dispensation, an
order, a tenure closing); the kinds of his own acts' results (93%); that someone, named half the
time, did something social, physical or of movement at a place he is at; what a record he holds
says; a two-link paper chain (`issue → create_record`) of which he holds both ends.

**Cannot:** a rumour with its speaker (5 to 12 claims in 22,000); a motive, or even "in answer to
what" (0); the course of a fight, or who won it, as a bystander; a battle (one fought field in six
realm-seasons, held by three persons); a duel that follows a challenge (0 of 295); a search that
found nothing; a succession learned as news rather than read off the menu; his own odds (0.8%); the
effect of his choice as *his*.

## 7. Survivors for Jordan

One, and it is the prior lane's question sharpened, not a new one.

**The draw.** `04` §C.12 (ratified) names "a seeded `RandomNumberGenerator` threaded like `World`";
the plan resolves parity by recorded-draw replay (GO-16); the oracle as built does neither (a keyed
generator per draw). Two defensible options:

- **A — the draw is a function of its key** (`16_PESSIMIST_GO_keyed_draw_no_recorder.md`). No
  recorder, no replay; parity at any seed; the shipped game draws exactly as the tested one did. One
  re-pin of every seeded golden and a rewritten Layer 1 row. The port owns `blake2b`, which it must
  for ids in any case.
- **B — the plan as written.** The oracle keeps `random.Random`; the port uses its own generator and
  replays a recorded log in tests. No re-pin now. Parity exists only on the recorded slices, the
  port's samplers are untested, and two saves of one seed on the oracle and on the port diverge at
  the first draw.

They differ as games in one way that a player can meet: under B a seed is not a world (a shared seed
does not reproduce across builds or platforms unless the port's generator happens to be bit-stable);
under A it is.

Everything else found here is answered by the ladder (§5).

## 8. Evidence log

All `PYTHONHASHSEED=0`, HEAD `826b747`, realm `build_realm(seed, None)` unless said; outputs in the
scratchpad directory named at the head. The machine's load average was 25 to 44 throughout; no
`aperture`, no pytest.

| id | command | reading |
|---|---|---|
| E1 | `python -m engine.season.harness.chronicle --seed 0 --seasons 2 --chains --min-depth 2` | 1,703 acts, 446 consequence acts, depth 4 (`conceal → create_record ×3`), 29 chain ends (`chron_s0_k2.txt`) |
| E2 | `probe.py plain 0 2` | `5ab73af282d0779646c38839fbab85d8`, `bacd687f1470883b412be9638d0b0f88`; the first equals the prior lane's pin |
| E3 | `probe.py base {0,1,2} 2` | every seat on `development_space(take_ranked)`; hashes seed 0 equal E2; seed 1 `aa58ef0b…`, `8aae8412…`; seed 2 `a21ab6e1…`, `89109213…`; JSON `base_s{0,1,2}_k2.json` (sheets, leak, odds, audience, chains, receipts, fights, ledgers) |
| E4 | `probe.py census 0 1` | hash equal E2; 18,702 generators, 18,651 single-draw, 48 six-plus, 3 none; `random` 18,652, `randint` 96, `randrange` 96, `getrandbits` 159; 50,975 `blake2b` calls |
| E5 | `probe.py trunc 0` | hash equal E2; 18,689 shown, 4,063 kept, 383 deliberations, `interactions_per_scene` 3 |
| E6 | `probe.py lever 0 p_npc_004 {ranked,last,idle}`, `… p_npc_006 last`, `… p_npc_089 last` | `5ab73af2…` (control), `c093236b…`, `ab3a9d01…`, `aa014148…`, `1064b434…`; diffs in §2.3 |
| E7 | `probe.py host 2 2 {engage,withdraw}` | engage `a21ab6e1…`, `89109213…` (equal E3, 6 calls); withdraw `14b47698…`, `20ea27f2…` (5 calls, no fight Event) |
| E8 | the eight `tools/export_*.py --check` | all exit 0; `export_npc_roster` reports 9 differing rows and passes (`checks.txt`) |
| E9 | inline probe: `creation_sheet` at seed 0; `build_realm(0, cap)` for cap 0, 1, 2, one season | §1.5, §3.7 |
| E10 | `probe.py verbs {0,1,2} 2` | hashes equal E3's second-season hashes; per-verb table in §2.3 (`verbs_s*_k2.json`) |
| E11 | inline probe: `questions_for(w, p_npc_088)` and the Tenures of `p_npc_004`, `_038`, `_088` at build, seed 0 | §2.1's worked case |

**Not done, and why.** Seeds beyond 2 and horizons beyond two seasons (load). The rung routes of the
leak were not traced to a stamp. The odds sample covers the first 4,200 priceable candidates of each
run (every seventh, 600), which is the first season and part of the second. `valoria-game` is not
attached and nothing here asserts a fact about it. The UI design set and `.audit/` were not re-read;
the prior lane's reading of them is cited.
