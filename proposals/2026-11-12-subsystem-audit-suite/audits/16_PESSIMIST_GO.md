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

**IN PROGRESS: this head was written before the reading finished; sections are appended in the order they
are established and the verdict is rewritten last. If this line is still present, the lane was
interrupted and what follows is partial.**

## 0. Verdict

`[PENDING — rewritten after the probes]`

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
