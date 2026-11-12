# DICE — pessimist audit: NERS, premise and emergent narrative, of the resolution substrate

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 826b747 (working tree)

Scope: `engine/dice_engine/` (`dice_engine.py`, `sigma_leverage.py`), `engine/engine_params/` and its
exporters, the shared-roller question (`modules/mass_battle/resolution.py`'s own roller), the obstacle
form (task difficulty plus all modifiers), advantage as a mean shift, and five premise sentences of
chance. The first audit (`audits/10_DICE_audit.md`), its addendum (`10_DICE_audit_addendum_B.md`), the six
`10_DICE_*` proposals and the determinism sweep (`audits/18_DETERMINISM_SWEEP.md`, four `18_DETERMINISM_*`
proposals) are cited, not redone. Everything measured here is new work unless a finding id of theirs is
named.

All runs: `PYTHONHASHSEED=0`; scripts and outputs under
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/PES_DICE/`.

## 0. Verdict

**The dice are sound and they decide almost nothing: in computed play the resolution substrate is a
correct machine fed one input, whose output changes what a few people believe and, in 282 of 284 graded
rolls, no state at all.** The substrate's own claims survived attack: the odds stated are the odds dealt,
one named level buys the same at every pool on the dice actually thrown (the uniform-leverage attack
failed), the fraction of an obstacle pays its fraction, and the same seed gives the same world (this
lane's two realm hashes equal two other lanes' independent runs). What failed is everything the five
sentences of chance need around it. Nobody's dice differ, so *more dice* and *a master* have no referent
in a run. A task has no difficulty, and the one obstacle there is fails three times in four, so *hard*
names the ordinary case; under the standing rule's own remedy (every consequential verb draws) that pair
would leave the realm doing about a sixth of what it does. Past the ceiling the roll is flat in the
pool, the opposition and every hostile modifier at exactly 10 %, and every forgery in the shipped realm
stands on that ceiling. Results have two degrees that matter on six of ten verbs, the top band cannot
occur, and a failed search is forgotten by the searcher and tried again the same season. At the scale of
a field the deciding draw is not a die: a lognormal multiplier on the pool, outside the engine and its
soft cap. Two fixes are decided and written (a saturating ceiling; the unopposed task's obstacle and a
throughput reading for the task draw); one choice is Jordan's (the form of fortune in a field).

The five worst findings: F-PES-DICE-01 (the degree changes no state), -02 (at the shipped pair
"everything draws" means "little happens"), -03 (the ceiling is a wall), -04 (a field is decided outside
the dice engine), -05 (a failed search is forgotten, and remembering it would change nothing).

## 1. NERS

Method: `skills/ners/SKILL.md`; definitions `CLAUDE.md` §0.06. Instrument B
(`skills/resolution-diagnostic/SKILL.md`) was run first and its five properties are §1.1; they are
evidence, and the cut tests in §1.2 grade them. E is read last, in §1.3.

### 1.1 The five properties of the draw, as evidence

Each row is a finding with the call that reproduces it, or a named attack that failed.

| property | what was attacked | outcome | reproduces |
|---|---|---|---|
| **P-i legible odds** | can the odds, the inputs and the advantage be read from the engine's own record | **fails**: the Event keeps the band alone (H-284, known); 76 of 208 realm failures missed by one and none says so; `odds_of` mode (a) has no loop caller; the named level never leaves `fixtures.effort_level` | E-P6 |
| **P-ii uniform leverage** | does one named level buy the same on the dice actually dealt (not in the Normal closed form) at small pools | **attack failed**: at matched base chance `moderate` buys +17.5 to +19.3 points at pools 1 to 4, and +8.8 to +11.6 at each pool's own ceiling at pools 1 to 8. The Normal form misstates it at one die (it says +4.2 at pool 1 / Ob 2 where the dice give +11.6), which is F-DICE-05's subject, not a leverage defect | E-P1 B1 |
| **P-ii, second shape** | an advantage that enters outside `levels_to_net_sigma` → `net_boost` | **fails at the field**: the per-battle friction draw multiplies the pool (`core/exchange.py:147`), is not sigma-scaled and is not soft-capped; 5th to 95th percentile 0.164 to 6.107, a 37-fold spread; in a mirror field the side with the higher draw won 275 of 287 decided (PES_MB's run, cited) | E-P3 S3 |
| **P-iii bounded, monotonic** | every clamp: which terms it reaches, and what is flat past it | **fails three ways**: (a) the ceiling is a `min()`, so past it the chance is flat at exactly 10.00 % in the pool, the opposition and every hostile modifier; (b) below `OB_MIN` the sum is unfloored, and at Ob 0 a second die lowers the chance (90.0 → 89.0 %); (c) the 10 % floor is solved *"at no advantage"*, so a negative boost goes through it (pool 1 / Ob 2: 8.0 % at −0.25σ, 3.0 % at −1σ, 0.9 % at −1.5σ, 0 % from −3σ). (a) is live in the realm (7 of 284 rolls, all examinations of forged Records, all at 2.842); (b) and (c) need content that does not ship | E-P1 A1 to A3, B2, C1; E-P6 |
| **P-iv graded, recoverable** | does a band other than pass/fail change anything; is an irreversible outcome a bare binary | **fails on grading**: 6 of 10 margin verbs are declared pass/fail, Overwhelming is distinct on two verbs that write nothing, and 282 of 284 realm rolls changed no state. **Recoverable holds**, to excess (H-111, known). Mass battle's `recall_check`, `feigned_retreat_recognized`, `feigned_retreat_check` and `discipline_check_cascade` (`orchestration.py:2093-2166`) are bare `net >= Ob` binaries on the roller, with the ladder one function away | E-P5; E-P6 |
| **P-v right engine** | every draw that is not `dice_engine` + `sigma_leverage` | F-DICE-05 and -07 (cited). New: mass battle makes three kinds of draw outside any d10 (`gauss` friction, two skewed-uniform break points at `core/state.py:44` and `hierarchy/units.py:2290`), and the constants that size them (`MB_FRICTION`, `MB_FRICTION_SIGMA`, `FEIGNED_RECOGNIZE_OB`, `FEIGNED_RETREAT_OB`; `config.py:242-244`, `:328-331`) are among the environment-read flags F-MB-09 found (cited; re-confirmed here by setting three of them and importing the module) | E-P4 |

### 1.2 The cut tests

For each object: the N-line its defender would give, the cut, what died. A **false N-line** is a cut that
turned out free.

| object | N-line claimed | the cut, run | what died | reading |
|---|---|---|---|---|
| mass battle's `roll_pool` | the module must stay free of `engine.*` (its docstring) | swap in `dice_engine.roll_pool` on one stream: 20,000 seeds, pools 1 to 12, **0 nets differ**, and the stream position after the roll is identical in 2,000 of 2,000 | nothing, at whole pools | **FALSE N-LINE.** The fractional die is the only thing the copy has that the owner lacks; F-DICE-07's proposal moves it. Confirmed by execution here; the first audit measured the ladder copy, not the roller |
| the four-band ladder, top band, on the social path | *"3 or more is always overwhelming"* | count it: 0 of 284 realm rolls; impossible at the shipped pool; distinct from Success on `speak` and `interrogate`, which write nothing | nothing that ships | **FALSE N-LINE as shipped** (ruled; not proposed for removal). It becomes true only with pools of three or more **and** a row that keys a write on it |
| the Partial band, on the social path | the near miss is its own outcome | compare Partial's and Success's declared rows and realm Events | on `arrest`, `lie`, `tell` and the three inquiries, nothing; on `argue` and `determine` the pursuit move | **NARROWED** to four verbs, of which `speak` and `interrogate` differ only in an Event kind nothing consumes by name |
| S27.4 in the provider (`sigma.py:543`) | an impossible attempt is refused before dice are dealt | under the shipped ceiling it fires only for a held score of 0, and not when the subject also holds 0 | the refusal of a person holding a zero; an unauthored person (no key) rolls two dice | **NARROWED**: what it protects today is that holding 0 is worse than holding nothing |
| `BandExtension`; `p_success`, `eff_ob`, `effective_ob`, `sigma_space_ob_shift` | the seam for a subsystem's de-saturation; the closed form | F-DICE-11, F-DICE-12 (cited): no caller the loop reaches | nothing in the season | **FALSE N-LINES**, both already found |
| three of the four named levels | the player-facing ladder of advantage | the season's one source uses `moderate`; 0 of 284 rolls carried any level | nothing in computed play | **NARROWED**: N holds for the player's `effort` only, at one level |
| the per-pool ceiling (H-213) | no matter becomes impossible | the uncapped arm (E-P1 A4): REFUSED cells at one die against scores of 5 and up, and chances of 0.0 to 1.0 % | the floor on the chance | **SURVIVES**, and is the cause of P-iii (a). The cut that is free is of its *form*: a saturating bound keeps the floor and loses the flat range (proposal) |
| the fraction of a margin (`settle_margin`) | two obstacles a fraction apart differ | pool 2: Ob 2.0 / 2.5 / 3.0 read 26.0 / 16.5 / 7.0 % | the middle value, with whole dice alone | **SURVIVES** |
| `band_odds` | the odds shown are the odds dealt | first audit, steelman 1; re-read here on the 270 realm rolls thrown at the default pair: Failure 72.2 % against 74.0 exact (standard error 2.7) | — | **SURVIVES** |
| the friction multiplier | without it a large advantage in the field is certain (its config note) | PES_MB's friction-off arm (their file) | their finding, not re-run here | not graded here; §6 gives the two forms it could take |

**Mechanisms that survive because nothing was tried against them.** (i) The H-210 sweep of
`default_forgery_quality` over 0 / 1 / 3: for the shipped pool of two, 1 and 3 compose the same obstacle
(2.842), so two of the sweep's three arms are one arm and the sweep cannot return a verdict that flips
between them. (ii) The 10 % chance floor: measured *"at no advantage"* and never against a boost of the
other sign, because no source of that sign exists; `10_DICE_advantage_sources_for_the_arcs.md` would add
one. (iii) `10_DICE_one_score_two_roles.md` moves the realm's default pair from (2, 2.0) to (2, 1.0),
which takes every unscored person-opposed roll off the ceiling's reach and onto the floor's: its gate
does not include a row at Ob below 1.

### 1.3 The reading, by criterion

- **N.** From the bottom the substrate is necessary and single-owned: the face rule, the ladder, the
  boost, the settle rule and the exact odds each have one owner and each cut above that removed one of
  them lost something. From the top it is narrowed: the standing rule asks that state set the odds and
  the draw the outcome, and in computed play state sets nothing (one pool, one obstacle, no leverage on
  284 of 284), so the dice supply variance to a constant. Laterally the three scales do not share a
  meaning for one score (F-DICE-15, -17, cited; E-P3 S1 extends it to unequal pairs). Vertically the
  result does not reach state: 282 of 284 rolls. Diagonally (a roll's result read by another person at
  another scale) only belief moves. Horizontally (roll after roll for one person) there is no carry:
  no roll reads the last. N holds bottom-up and is narrowed in the other five directions.
- **R.** The strategic half fails on legibility (P-i) and on the flat ranges (a player who forges a
  better document, packs a more hostile bench or brings a better advocate against a strong opponent
  buys nothing past the ceiling). The no-player half: the dice produce events without a player and the
  events change belief and almost no state. Completeness fails at both extremes of the obstacle (P-iii)
  and at one die (no Success at the default obstacle).
- **S.** Two conventions for one operation, three times: the roll's two operands saturate differently
  (sigma by `tanh` with *"no dead-zone"*, the obstacle by `min`); a fraction of a die has three rules
  (F-DICE-08, cited); advantage enters the field by a pool multiplier and the other two scales by a mean
  shift. *Pauses correctly*: not applicable to a pure function; the season's roll holds no state between
  calls.
- **E, last, as a ratio.** What N and R found the substrate to deliver in play is one distribution
  (74 / 19 / 7 / 0). Against that the apparatus is two samplers, three rollers, four named levels, a
  soft cap, a per-pool ceiling solved by enumeration, a refusal rule and an extension seam. The ratio is
  poor today and is not a reason to cut: every part but those marked false above is what a varied input
  would need. The legibility half of E (a player intuiting outcomes from choices) is the weaker half:
  the rule a player can hold is *"two dice against two: one in four"*, and nothing he can do in the
  season as computed changes either number.

## 2. Premise audit

Method: `skills/premise-check/SKILL.md`, SLICE scope (the five sentences the work order names; boundary:
from "a person attempts a thing with a pool against an obstacle" to "the engine's record states the
result and its degree"). The ordinary account O in §2.1 was written before this lane opened any file
under `engine/dice_engine/`, `engine/engine_params/`, `modules/` or the first DICE audit. What this lane
already knew when writing O: the `resolution-diagnostic` skill's description of the stack (d10 pool,
successes against an obstacle, a four-band ladder, advantage as a shift of the roll's mean). O is written
from the words of the sentences, not from that.

### 2.1 O — what each sentence should mean (written first)

**P1 "More dice are better, but not always."**
1. Dice are the size of the pool a person brings: his skill and whatever else adds to it. 2. "Better"
means the chance of success against the same obstacle rises with every die added: monotone, no die that
lowers the chance, no plateau where a die buys nothing. 3. The gain per die is readable: a player
adding a die can say roughly what it bought. 4. "Not always" has two ordinary readings, and both should
hold: (a) a bigger pool still fails sometimes on any one roll (no pool makes an ordinary task certain);
(b) the marginal die is worth less as the pool grows (diminishing returns), and on a task far beyond or
far beneath the pool, a die changes little. 5. More dice should also be better for the DEGREE: the larger
pool lands the top band more often and the bottom band less often. 6. It holds for a fraction of a die:
half a die is better than none and worse than one. 7. Bounds: a pool of zero or less than one die is a
bad pool, not an error and not a free roll; a very large pool (20, 50) approaches but does not reach
certainty on a task that is hard for it, and does not overflow. 8. Zero: the same pool on the same seed
gives the same result. 9. [GENRE] no die is harmful: the game has no "botch" in which more dice raise the
chance of catastrophe (if it has one, the words should say so). 10. Feedback: the record of a roll says
how many dice were rolled.

**P2 "A hard task fails often and succeeds sometimes."**
1. A task has a difficulty that is a property of the task (and of what stands against it), stated as an
obstacle. 2. Hard, for a given person, means the obstacle is high against his pool. 3. "Fails often": at
a hard obstacle the ordinary competent pool fails more than half the time. 4. "Succeeds sometimes": the
chance is not zero and is large enough to be seen in play: a player who tries a hard thing ten or twenty
times sees it come off at least once (order of 5-25%), not one in ten thousand. 5. Ordered levels give
ordered results: easy > routine > hard > very hard in success chance, for every pool, with no ties
between adjacent levels and no cliff where one step of difficulty takes the chance from likely to
never. 6. The difficulty is the task's own number plus every modifier that applies (circumstance, the
opponent's quality, tools, wounds): one sum, and each modifier moves the chance in the direction its
word says. 7. The same difficulty word means the same thing at every scale of play: "hard" for a duel,
a speech and a siege give comparable odds for comparably able actors. 8. Bounds: a task cannot be made
free (an obstacle of zero or below still asks for something) or impossible by stacking modifiers,
unless the fiction says impossible. 9. A fractional difficulty is real: 1.4 is easier than 1.6.
10. Feedback: the record gives the obstacle that was rolled against, and the player can read his chance
before he commits.

**P3 "A master beats a novice more often than not."**
1. Master and novice are levels of one skill, far apart on its scale. 2. They contest: both roll, or the
novice's quality sets the master's obstacle; either way the two pools are the inputs. 3. "More often than
not": master wins well over half, and the share rises with the gap (monotone in the skill difference).
4. "Not always": the novice wins a visible share at an ordinary gap (order of 5-20%), falling toward but
not to zero at the widest gap the scale allows. 5. Mirror: equal skill gives about even; swapping seats
swaps the result. 6. The same gap means about the same thing at both ends of the scale: 2 against 4 and
6 against 8 are both "two levels better" (or differ for a reason the words give). 7. Mastery shows in the
degree as well: the master's wins are more often clean, the novice's wins more often narrow. 8. It holds
at every scale that has a contest: a duel, a debate, two captains, two factions. 9. Bounds: the lowest
skill against the highest still resolves by a draw (standing rule), and the result is not an error.
10. Feedback: the record says who won, by what margin, and with what pools.

**P4 "Advantage helps without guaranteeing."**
1. Advantage is a named circumstance in one's favour (ground, surprise, a better weapon, evidence,
standing), in ordered levels (minor < moderate < strong < major, per the diagnostic's vocabulary).
2. "Helps": with the advantage the chance of success is higher than without, on the same seed set
(counterfactual pair), for every pool and obstacle. 3. Ordered levels give ordered help; two advantages
help more than one; an advantage and an equal disadvantage cancel. 4. The help is about the same size
for a weak actor as a strong one (the same named level should not be worth triple to a small pool).
5. "Without guaranteeing": no stack of advantages takes the chance to 1; the best-placed actor still
fails a visible share on a task that was a coin toss without it. Likewise a stack of disadvantages does
not take it to 0. 6. Advantage does not change what the task is: the obstacle recorded is the same, and
the thresholds for an overwhelming result are not made cheaper by it (otherwise advantage also buys
degree for free, twice). 7. It helps the degree in the same direction (more top band, less bottom band).
8. Disadvantage is its mirror: the same size, opposite sign. 9. Feedback: the record names the advantage
and its level, not only a number. 10. Every scale that grants advantage grants it the same way (one
convention).

**P5 "A result has degrees and a failure can be recovered from."**
1. A result is one of an ordered set of degrees (more than pass/fail): a clean success, a narrow or
partial one, a failure, and something beyond at one or both ends. 2. Each degree is reachable: over
many rolls at ordinary pools every band appears, with none at zero and none swallowing the rest.
3. The degrees are ordered by the margin, and the margin is readable (how far over or under). 4. A
partial result is different in consequence from a success and from a failure: something is gained and
something withheld, and the world shows which. 5. "A failure can be recovered from": an ordinary failed
roll does not end the actor's story: he can try again (at a cost, later, or by another route), or the
failure leaves a state that a later act can repair; the failure's consequence is proportionate to the
stakes. 6. The worst band is rarer than plain failure, and only it (if anything) is irreversible. 7. The
degree drives the consequence: two results of different degree on the same act change the world
differently (a degree that nothing reads is decoration). 8. The same ladder is used everywhere a draw is
made (one ladder, not one per subsystem). 9. Bounds: at obstacle extremes (fractional, below 1, very
high) the bands still partition every outcome with no gap and no overlap. 10. Feedback: the record
carries the degree by name.

### 2.2 N — what the code's notes say, in aggregate (read after O, before the runs)

Sources: the docstrings of `dice_engine.py`, `sigma_leverage.py`, `modules/social_contest/roll.py`,
`seam/wrappers/pool.py` and `sigma.py`, `modules/combat/core.py`, `modules/mass_battle/resolution.py`;
the `*_note` and `[JUSTIFIED: …]` lines of `data/fixtures.py`; `rosters.yaml: undeposited_kinds`; hole
rows H-111, H-126, H-127, H-210, H-213, H-269, H-284.

- **Dice.** A pool is the score a person holds for the verb (the larger of his key and his attribute),
  else `pool_default` 2, plus practice; *"Rank supplies dice and gates nothing"*. A pool floors at one
  die. Whole dice are dealt (a fraction rounds); the Normal sampler takes a fraction as it is; mass battle
  deals the fraction as one more die with that probability.
- **Obstacle.** *"Their corresponding score/2 plus whatever specific modifiers exist … in that instance"*,
  and it applies to a person. A thing with no score takes the stand-in `obstacle_default` 2. **No base
  obstacle by scale** (Jordan, 2026-09-05). The room is subtracted, a forgery's quality added, and a
  ceiling bounds the sum so that *"each pool's chance at its own cap is the same 10 %"*. The notes state
  the clipping as known: *"a hostile room cannot raise a defaulted obstacle — stated, not hidden"*.
- **Advantage.** A mean shift on the roll, never an obstacle reduction; soft-capped by `tanh` with *"no
  hard ceiling and no dead-zone"*; uniform in z at every pool. One source, `effort`; 0.0 *"the honest form
  while nothing supplies it"*.
- **Degrees.** One ladder on the margin; Partial is *"the near-miss-by-nothing outcome"*; combat and the
  field read their band off their own result by ruling. A failed inquiry *"teaches its actor nothing and
  the same person re-forms it"* (the roster's own note, H-111, *Jordan to correct*).
- **Disagreement inside N.** (i) `pool.py`: *"a held 0 is still a person under one die"*; `sigma.py`:
  *"only a pool below the floor is [refused]"*. Both are true of different lines: the dice deal one die,
  and S27.4 refuses first on `ob > 2 × max(pool, 0)`. (ii) `roll.py`: the composed obstacle is not
  floored (*"score 1 gives 0.5"*), while the room's favour is floored at `OB_MIN` and `OB_MIN`'s tag is
  *PP-232, Ob minimum 1*. Neither is settled by a later ruling; SC-B's proposal floors the sum.

### 2.3 C — the runs, and the link tables

Depths: EXECUTES = the owner called directly or by exact enumeration through it (`band_odds`,
`record_odds`, `roll.obstacle` on a hand-built `SocialContestInput` with the shipped fixtures); FIRES =
`build_realm(seed)`, the shipped chooser, two seasons, seeds 0 and 1 (284 graded margin rolls). Controls
are named per row. Evidence ids are in §8.

**P1 "More dice are better, but not always"** — *holds at EXECUTES between Ob 0.5 and the ceiling; breaks
at both ends of the obstacle range; inert at FIRES (everyone rolls two dice).*

| # | link | C observed | verdict · cause | owner | evidence |
|---|---|---|---|---|---|
| 1 | dice are what the person brings | 284 of 284 realm rolls at pool 2 | FOLLOWS at EXECUTES; INERT at FIRES (F-DICE-01, cited) | `pool.py::faculty` | E-P6 |
| 2 | every die raises the chance; no plateau | monotone in P+ and S+ at Ob 0.5 to 3.5, pools 1 to 10. **At Ob 0, pool 1 → 2 lowers P+ 90.0 → 89.0 %.** **At or past the ceiling every pool reads P+ 10.00 %** (pools 1 to 12) | DEPARTS · EDGE (both ends) | `roll.py::obstacle`, `_chance_floor_cap` | E-P1 A1, A2, A3 |
| 3 | the gain per die is readable | at Ob 2: +16.0, +14.0, +11.2, +8.8, +7.0 points for dice 2 to 6 | FOLLOWS | `band_odds` | E-P1 A1 |
| 4 | still fails sometimes; returns diminish | pool 10 at Ob 2 fails 16.1 % | FOLLOWS | — | E-P1 A1 |
| 5 | more dice, better degree | Overwhelming 0 / 0 / 1.0 / 3.8 / 8.3 % at pools 1 to 5, Ob 2; **at pool 1 Success is impossible at Ob ≥ 2** (one die nets at most 2) | FOLLOWS; EDGE at one die | `degree_from_net` | E-P1 A1 |
| 6 | half a die is between none and one | pool 2.5 deals 2, 3.5 deals 4, 0.4 deals 1 on the owner; mass battle's mean net 0.161 / 1.002 / 1.410 against the owner's 0.400 / 0.800 / 1.600 | DEPARTS · BEHAVIOUR, latent in the season (F-DICE-08, cited; means are new) | `sigma_leverage._dice_dealt`; `resolution.roll_pool_fractional` | E-P3 S2 |
| 7 | zero dice is a bad pool, not an error | a held 0 is REFUSED against every subject but another held 0, where it succeeds 90 % | DEPARTS · EDGE | `sigma.py::resolve` (S27.4) | E-P1 A3 |
| 8 | same seed, same result | this lane's two realm hashes equal two other lanes' independent runs | FOLLOWS | `state/ids.py::draw_factory` (blake2b; no process hash) | E-P6 |
| 9 | [GENRE] no botch | no band below Failure exists | FOLLOWS | — | — |
| 10 | the record says how many dice | `Event` fields: `id, kind, changes, causes, emitted_at, degree, observed, ending` | DEPARTS · known limit (H-284) | `state/carriers.py::Event` | E-P6 |

**P2 "A hard task fails often and succeeds sometimes"** — *does not hold as worded: a task has no
difficulty; what holds is "every task is hard".*

| # | link | C observed | verdict · cause | owner | evidence |
|---|---|---|---|---|---|
| 1 | difficulty is the task's own | no term for it; 270 of 284 realm rolls at exactly 2.0, the stand-in for *a subject with no score* | ASSERTED (ruled out 2026-09-05; SC-B proposes it) | none | E-P6 |
| 3 | hard fails more than half | the only task there is fails 74 % | DEPARTS · WORD: the ordinary task is the hard one | `fixtures.py` `pool_default`, `obstacle_default` | E-P1 |
| 4 | succeeds sometimes, visibly | P+ 26 %, Success 7 %; at the ceiling 10 %, of which at one die none is a Success | FOLLOWS, narrowed | `_chance_floor_cap` | E-P1 A2 |
| 5 | ordered levels, ordered results; no ties; no cliff | **ties**: forgery quality 1, 2, 3, 5 all read 10.0 % for pool 2 (0.842 and up is one value); every quality 0 to 5 reads 10.0 % for pool 1; hostile reception −1, −2, −3 all 10.0 % at pool 2. No cliff (S27.4 is unreachable at pool ≥ 1) | DEPARTS · EDGE (dead ranges) | `roll.py::obstacle` (`min(ob, cap)`) | E-P1 C1 |
| 6 | one sum; each modifier in its direction | room subtracts, forgery adds, both in the right direction | FOLLOWS | `roll.py::obstacle` | E-P1 C1 |
| 7 | "hard" means the same at every scale | 4 against 4: P+ 51.2 % in a social act, 78.5 % in a combat exchange; the field has no score | DEPARTS · COMPOSITION (F-DICE-15, -17 cited; unequal pairs new) | three modules | E-P3 S1 |
| 8 | never free, never impossible | Ob 0.0 and 0.5 compose (a held 0 or 1); the room's favour floors at 1.0, so an unscored subject before the friendliest bench (Ob 1.0) is harder than a weak opponent before nobody (Ob 0.5). Never impossible: the 10 % floor holds, at no advantage only | DEPARTS · EDGE | `roll.py:141-143` | E-P1 A3, C1, B2 |
| 9 | 1.4 is easier than 1.6 | pool 2: Ob 2.5 reads 16.5 % between 26.0 and 7.0 | FOLLOWS | `settle_margin` | E-P1 A1 |
| 10 | the record gives the obstacle; the chance is readable beforehand | not on the Event; `odds_of` mode (a) has no loop caller; the chooser's *cannot say* reads as certain (F-DICE-14, cited) | DEPARTS · known limit (H-284) | — | E-P6 |

**P3 "A master beats a novice more often than not"** — *holds at EXECUTES for the social act and the
combat exchange; nothing "beats" anyone in a social act; inert at FIRES; the three scales disagree.*

| # | link | C observed | verdict · cause | owner | evidence |
|---|---|---|---|---|---|
| 2 | they contest | a social act is one party's roll against half the other's score; the other does nothing, and his own act against the first is a separate roll. Both can succeed. Only the field rolls both sides | AMBIGUOUS → WORD (`contests:`, `argument.won`) | `roll.py::roll`; `orchestration.py:1308` | — |
| 3 | more often than not, rising with the gap | 7 against 1: P+ 90.5 %, Success-or-better 79.5 %; monotone in both scores below the ceiling | FOLLOWS at EXECUTES; INERT at FIRES | `roll.py::obstacle` | E-P1 A3 |
| 4 | the novice wins a visible share | 1 against 7: 10.0 % Partial, **0.0 % Success** (shipped arm); uncapped control: REFUSED. Combat exchange, same scores: 37.0 % P+, 21.1 % Success-or-better | DEPARTS · EDGE and COMPOSITION | — | E-P1 A3, A4; E-P3 S1 |
| 5 | equals are about even | P+ 90 / 65 / 58 / 54.1 / 51.2 / 49.0 / 47.0 / 45.5 % at scores 0 to 7: two incompetents succeed against each other twice as often as two masters | FOLLOWS, narrowed (drift; F-DICE-17 cited for 2, 3, 4, 7) | `roll.py:141` (mean net 0.4 s against Ob 0.5 s) | E-P1 A3 |
| 6 | the same gap means the same at both ends | two better: 74.9 % (4 v 2), 67.0 (6 v 4), 63.7 (7 v 5); two worse: 26.0, 27.9, 28.9 | FOLLOWS, narrowed | — | E-P1 A3 |
| 8 | at every scale that has a contest | see P2 link 7; a field reads no person (F-DICE-18, cited) | DEPARTS · COMPOSITION | — | E-P3 S1 |
| 10 | the record says who won, by how much | the band; `argue` at Partial is logged `argument.won` with no change (H-269, known; 7 of 7 realm instances) | DEPARTS · known limit | `verb_table.yaml` `argue` | E-P6 |

**P4 "Advantage helps without guaranteeing"** — *holds at EXECUTES, and uniform leverage survives the
attack on dealt dice; has one source and one sign; inert at FIRES; the field's largest advantage is not
advantage as the engine defines it.*

| # | link | C observed | verdict · cause | owner | evidence |
|---|---|---|---|---|---|
| 1 | named, ordered levels | four names; the season uses one (`effort_level: moderate`) | FOLLOWS | `LEVEL_SIGMA` | — |
| 2 | with it the chance is higher | default pair, effort 0 → 3: Failure 74.0 → 56.5 → 42.4 → 32.9 % | FOLLOWS at EXECUTES; **0 of 284 realm rolls carried effort** (INERT at FIRES; F-DICE-06 cited) | `sigma.py::advantage_sigma` | E-P1 B3; E-P6 |
| 3 | ordered, stacking, cancelling | minor < moderate < major at every cell; nothing can count against (the `defender` list is never passed) | FOLLOWS; cancelling ASSERTED | `sigma.py:167` | E-P1 B1 |
| 4 | the same level is worth about the same to weak and strong | **at matched base chance**: `moderate` buys +19.3 points at pool 1 / Ob 1 and +18.8 at pool 3 / Ob 2 (base 40 % each); +17.5 at pool 2 / Ob 2 and +17.9 at pool 4 / Ob 3 (base 26 to 28 %); at each pool's own ceiling +8.8 to +11.6 (pools 1 to 8) | FOLLOWS — the attack failed | `net_boost` | E-P1 B1 |
| 5 | no stack guarantees | forty `major` levels: Failure 20.4 % at pool 2 / Ob 2, 0.2 % at pool 8 / Ob 1. The mirror: forty against takes pool 1 / Ob 2 to 100 % Failure, through the 10 % floor | FOLLOWS; EDGE on the negative side (unreachable until a source can count against) | `soft_cap`; `_chance_floor_cap` (*"at no advantage"*) | E-P1 B2 |
| 6 | the obstacle is not changed by it | `Margin.ob` is the composed obstacle with or without effort | FOLLOWS | `roll.py::roll` | E-P1 B3 |
| 9 | the record names the advantage | `leverage` is a float in the provider's dict and is dropped at the fold | DEPARTS · known limit (H-284) | — | E-P6 |
| 10 | every scale grants it one way | the field's deciding term is a per-battle lognormal multiplier on the **pool** (`core/exchange.py:147`, σ 1.1), outside `net_boost` and outside the soft cap | DEPARTS · COMPOSITION | `orchestration._draw_friction` | E-P3 S3; PES_MB's run |

**P5 "A result has degrees and a failure can be recovered from"** — *does not hold in play: results have
two degrees that matter, the degree changes no state, and failure is recovered from by forgetting it.*

| # | link | C observed | verdict · cause | owner | evidence |
|---|---|---|---|---|---|
| 2 | every degree is reachable | realm, 284 rolls: Failure 208, Partial 56, Success 20, **Overwhelming 0** (F-DICE-02, cited) | DEPARTS · EDGE | `pool_default` | E-P6 |
| 3 | the margin is readable | settled margins of the 208 failures: −1 ×76, −2 ×94, −3 ×33, −4 ×5; none is kept | DEPARTS · known limit (H-284) | `resolve.py::_contest` | E-P6 |
| 4 | Partial differs from Success and from Failure | declared rows: Partial ≡ Success on 6 of the 10 margin verbs (`arrest`, `lie`, `tell`, `examine`, `research`, `surveil`); Overwhelming ≡ Success on 8 of 10. Realm: Partial and Success emitted the same kind on `research`, `surveil` and `tell`; `argue` alone differed (Success adds `pursuit.moved`) | DEPARTS · BEHAVIOUR | `verb_table.yaml` | E-P5; E-P6 |
| 5 | a failure can be recovered from | 49 of the 151 aims (actor, verb, subject) that opened with a Failure were tried again; 50 of the 71 repeat attempts in those chains fell in the same season, each a fresh draw; a failed search deposits nothing, to the searcher included (157 of 157 `finding.none` Events have no descendant) | FOLLOWS — and over-follows (H-111, known limit; the counts are new) | `rosters.yaml: undeposited_kinds` | E-P6 |
| 7 | the degree drives the consequence | **282 of 284 graded rolls produced Events with an empty `changes`**; the two that wrote: one `argue` Success (2 changes), one `determine` Partial (1) | DEPARTS · BEHAVIOUR | `verb_table.yaml` `writes:` | E-P6 |
| 8 | one ladder everywhere | three vocabularies by ruling (margin; scene; field) and mass battle's internal copy | DELIBERATE (Jordan, 2026-09-03); the copy is F-DICE-07 | `seam/ladder.py::degree_of` | — |
| 10 | the record carries the degree | yes | FOLLOWS | `Event.degree` | E-P6 |

### 2.4 Play-back (control-P, the realm at seed 0, two seasons, told plainly)

Fifty-five of the eighty-three people in the realm tried something that could go either way; most of them
once or twice in two seasons. Whoever they were and whatever they tried, each threw two dice at the same
difficulty. Three times in four nothing came of it. When a search came up empty the searcher kept no
memory of having looked, and one time in three looked again, usually within the same season. Nobody
triumphed. Of the thirty-eight who got somewhere, one changed what another person wanted; for the rest
the stores, offices and bodies of the realm were exactly as before, and what moved was what a handful of
people believed.

Set beside the five sentences: none of the five nouns that carry them (dice, hard, master, advantage,
degrees) varied in the run.

## 3. Emergent narrative

The subject is a resolver, so the question is what the draw contributes to a story: which turns it can
produce, which it does produce with nobody playing, and what of each a narrator could read back.

### 3.1 The turns the dice can produce, enumerated from the code

From `degree_from_net`, `roll.py`, the fourteen rolled rows of `verb_table.yaml` and the two other
providers; not from any design document.

| turn | can it happen | what it needs | in two realm seasons, seeds 0 and 1 |
|---|---|---|---|
| the attempt that fails | yes | any roll | 208 |
| the near thing (Partial as its own outcome) | on `argue`, `determine`, `speak`, `interrogate` only | a row whose Partial differs from its Success | 56 Partials, 8 on rows where the band differs (7 `argue`, 1 `determine`) |
| the clean success | yes, from two dice | — | 20 |
| the triumph (Overwhelming) | on `speak` and `interrogate` only, as an Event kind | three dice at Ob 2, or two dice at Ob 1 and a pair of tens | 0 |
| the upset (the weak succeed against the strong) | to Partial only, at exactly 10 %, for anyone at the ceiling; never a Success on one die | a scored subject | 0 (nobody holds a score) |
| the strong fail | yes: 9.5 % for seven dice against a score of 1 | scores | 0 |
| pressing (odds bought with effort) | yes for a player; a person may form it (`npc_effort: on`) | a believed chance, which is `None` for every contested act but `determine` (F-DICE-14) | 0 of 284 |
| persistence (try again after failing) | yes | nothing; a failed act costs its slot | 49 of 151 failed aims, 50 of 71 repeats within the season |
| the run of luck | only for someone who rolls often | rolls | most rolls by one person: 5 and 8; longest failure run 5 and 7; best record `Partial, Partial, Failure, Partial` |
| the field turned by fortune | yes, and by fortune more than by dice: the friction draw (§1.1) | a fought field | 0 fought fields in these runs (6 `Unopposed`) |

**Turns that cannot happen at all, because no code owns them.**

- **The disaster.** No band lies below Failure, the margin is discarded, and every margin row's Failure
  writes nothing: a miss by one and a miss by four are the same Event (the 208 realm failures were 76,
  94, 33 and 5 at one to four below).
- **The success that costs.** No band and no row carries a price paid for succeeding.
- **The contest with a loser.** A social act has one roller. `argument.lost` is the arguer's own failure;
  the person argued against gains, loses and records nothing by it.
- **The comeback.** A person who fails a search holds nothing saying he searched, so his second attempt
  is not, to him, a second attempt.
- **Character shown by dice** (she is reliably good at this): impossible while the pool is a constant
  (F-DICE-01, cited). Over these runs no person's record can be told from luck: at most eight rolls each,
  one distribution for all.
- **The larger triumph.** On eight of the ten margin rows Overwhelming declares exactly what Success does.

### 3.2 What a roll leaves behind

Per graded roll, the Events that later cite its Event as a cause (E-P6):

| band | rolls | descendant Events | of which not `claim.deposited` | state changes on the roll's own Events |
|---|---|---|---|---|
| Failure, inquiries (`finding.none`) | 157 | **0** | 0 | 0 |
| Failure, other verbs | 51 | 577 | 29 | 0 |
| Partial | 56 | 639 | 25 | 1 (`determine`) |
| Success | 20 | 416 | 16 | 2 (one `argue`) |

A roll's result propagates as belief (a witness's claim that it happened) and almost never as state.
Three quarters of the realm's rolls are inquiries (`research` 166, `surveil` 45 of 284); when one fails,
nothing in the world records that it was made. So the commonest thing the dice decide is whether a
searcher comes to hold a finding, and the commonest result is an Event nobody, the searcher included,
ever reads.

### 3.3 The shape of the tail

Every run is the same run, in distribution. Seed 0 gave 80 / 27 / 11, seed 1 128 / 29 / 9; against the
pooled shares that is χ² = 3.3 on two degrees of freedom (p about 0.19): two samples of one roll. It
could not be otherwise: 270 of 284 rolls are (2 dice, Ob 2.0, no leverage), and the other fourteen moved
only by a bench or a forged Record. The same person (`p_npc_081`) is the most frequent roller in both
seeds, because who rolls is decided by the roster's standing questions, not by anything a roll did.

### 3.4 What a player's choice changes

One thing: `effort`, which takes the default roll's Failure from 74.0 to 56.5, 42.4 and 32.9 % at one to
three slots (E-P1 B3). He cannot choose an easier task (a task has no difficulty), cannot be helped (no
second person's dice enter), cannot prepare (no other advantage source), and gains nothing by choosing
whom to act against (nobody holds a score). He can try again, at the cost of the slot.

### 3.5 Are the reasons readable afterwards

No. The Event carries the band. The pool, the obstacle and its terms, the leverage and its named level,
the net and the margin exist in the provider's returned dict for the length of one function call
(`resolve.py::_contest`) and are dropped (H-284, known; SC-B's `Margin.terms` proposal is the remedy and
this lane adds one field to it, the settled margin). A narrator can write *"she failed"* and cannot write
*"she failed narrowly, against long odds, having spared no effort"*, each clause of which the engine
computed.

### 3.6 The extremes

- **No rolls.** A realm in which no standing question exists rolls nothing; the dice have no part in a
  world without inquiry or speech. Not a defect.
- **One die.** If content authors a score of 1, that person fails the default task 90 % of the time and
  cannot Succeed at it at all (E-P1 A1); the only stories he can have are failures and near things.
- **Zero.** A held 0 is refused every attempt except against another 0, which he wins nine times in
  ten.
- **Many dice.** Seven dice against an unscored subject: Failure 27.4 %, Overwhelming 20.8 %. The top
  band becomes common exactly where content is most authored, and on eight rows it means nothing more.
- **Past the ceiling.** However strong the opposition, however good the forgery, however hostile the
  bench: 10 %. The most extreme situations in the game are the ones the dice cannot tell apart.

## 4. Findings, ranked worst first

Severity vocabulary as the suite's. *Known limit confirmed* marks a finding whose mechanism a hole row
already names; what is new there is the measurement.

### F-PES-DICE-01 · blocks what R-09 is for · the degree changes no state

- **Claim.** In computed play the band a roll lands in moves a belief or nothing; it does not move the
  world.
- **Falsifier run.** Realm, seeds 0 and 1, two seasons: 284 graded margin rolls; the Events of 282
  carry an empty `changes`. **Control** (the instrument can see a change): one `argue` at Success (two
  changes, `Person.pursuits`), one `determine` at Partial (one). Declared rows (E-P5): `lie`, `tell`,
  `speak`, `interrogate` declare `writes: []` in all four bands; `examine`, `research`, `surveil` declare
  `writes: []` flat.
- **Touches.** R-01, R-02, R-09.
- **Consequence.** R-09 (chains of events are probabilistic) is met in the letter: the chain is drawn.
  What is drawn is whether a claim is deposited. A world whose dice never touch a body, an office, a
  store or a bond has chance and no stakes.
- **Minimal fix at the owner.** `engine/season/verb_table.yaml`: the seven rows above each key at least
  one write, or one deposit of differing strength, on the band. The band maps are the verb lanes'
  (`14_VERBS_SOCIAL*`, `13_SC_draw_for_unrolled_contests.md`, FI); `18_DETERMINISM_task_draw…` item 4's
  default map (Partial at half) is the shape. No edit proposed here beyond naming the seven rows.

### F-PES-DICE-02 · degrades narrative, and defeats the standing rule's own remedy · at the shipped pair "everything draws" means "little happens"

- **Claim.** `18_DETERMINISM_task_draw_for_uncontested_verbs.md` converts 22 verbs to the graded route
  and ships them at `obstacle_default` *"until [the difficulty column] lands"*. At the shipped pool that
  is Failure 74 / Partial 19 / Success 7 / Overwhelming 0. Under its own fraction table (Partial one
  half) the converted verbs deliver **16.5 %** of the effect they deliver today.
- **Falsifier run.** `band_odds(2, 2.0) == (0.74, 0.19, 0.07, 0.0)`; 0.19 × 0.5 + 0.07 = 0.165.
  **Control**: the same arithmetic at pool 2 / Ob 1.0 gives 0.42; at pool 4 / Ob 1.0, 0.63; at pool 4 /
  Ob 2.0, 0.40 (E-P1 A1). On the sweep's count of 727 consequential undrawn outcomes in five realm
  seasons, that is about 120 effect-equivalents at the shipped pair and about 305 at Ob 1.0.
- **A second defect in the same place.** Under `13_SC_tuning_tables.md` T1's calibrated sizes (`plain`
  0, `routine` 0.5, `demanding` 1.0, `hard` 1.5) with SC-B's floor at `OB_MIN`, a row with **no person
  counterparty** has no opposition term, so `plain`, `routine` and `demanding` all compose 1.0: three of
  the four difficulty levels are one number for every unopposed task (the 22 task rows, and `speak`,
  `research`, `examine`, `surveil`). T1's falsifier (*"two adjacent levels giving the same P(Failure)
  at equals"*) tests opposed pairs only and cannot see it.
- **Touches.** R-04 (strategic and management actions), R-09.
- **Consequence.** A realm in which a journey arrives one time in four and a wound mends one time in
  four is not more dramatic; it is slower, and the plain failures write nothing (F-PES-DICE-01). The
  standing rule says a good position *"still loses sometimes"*; at this pair an ordinary position loses
  usually.
- **Minimal fix.** `proposals/16_PESSIMIST_DICE_task_difficulty_and_throughput.md`: the unopposed
  stand-in, a default level of `plain` for a task row, and a throughput reading in 18-A's gate. The
  pool regime behind it is already Jordan's (addendum §5.6).

### F-PES-DICE-03 · degrades narrative · the ceiling is a wall, and the shipped forgery stands on it

- **Claim.** `min(ob, cap)` makes the obstacle flat past each pool's cap. There the chance of
  Partial-or-better is 10.00 % for every pool, every opposition and every hostile modifier.
- **Falsifier run.** E-P1 A2, A3, C1: pools 1 to 12 each read 90.0 % Failure at their cap; one die reads
  10.0 % against scores of 4, 5, 6, 7, 10, 20; two dice against 6 and up. Forgery quality 1, 2, 3 and 5
  compose 2.842 for two dice, and 0 to 5 all compose 2.000 for one die. **Control**: the uncapped arm
  (A4) separates every one of those cells (16.5 / 7.0 / 4.0 %, then REFUSED), so the flatness is the
  cap's and not the dice's. **In the realm**: 7 of 284 rolls were examinations of forged Records, all
  seven at exactly 2.842, all seven Failure.
- **What 13 already has, and what is new.** `13_SC_tuning_tables.md` problem 4 states the room's half
  (*"every favourable room composes 1.0 and every hostile one 2.842"*). New here: the plateau across
  **pools** (a die buys nothing past the cap); that `default_forgery_quality` 1 places every shipped
  forgery on the cap for the shipped pool, so H-210's sweep arms 1 and 3 are one arm; that the
  task-draw proposal's `forge_quality[band]` (a better forging roll, a better forgery) is dead above
  0.842 for a two-die examiner; and that the two operands of one roll saturate by two conventions
  (sigma by `tanh`, *"no hard ceiling and no dead-zone"*; the obstacle by `min`), an S defect.
- **Touches.** R-06, R-09; NERS-R (completeness at the extreme), NERS-S.
- **Consequence.** The mechanism is flattest where the fiction is most extreme. Past the cap, a
  master's eight dice against an impossible bench are worth what a novice's one die is (10.0 % each;
  with three slots of effort 42.4 % against 37.4 %): effort is all that counts and skill counts for
  nothing.
- **Minimal fix.** `proposals/16_PESSIMIST_DICE_soft_ceiling.md`: the excess over the fixed ceiling
  saturates toward the pool's cap as sigma saturates toward `M_MAX`. No new number.

### F-PES-DICE-04 · degrades narrative · a field is decided by a draw the dice engine never sees

- **Claim.** The largest chance term in a fought field is `exp(gauss(0, 1.1))`, drawn once per unit per
  battle and multiplied into the dice **pool** (`orchestration.py::_draw_friction`,
  `core/exchange.py:147`).
- **Falsifier run.** By construction (E-P3 S3): the multiplier's 5th and 95th percentiles are 0.164 and
  6.107; one side's draw is more than twice the other's with probability 0.656. Run by the MB pessimist
  lane and cited, not re-run (`runs/PES_MB/p1_size.txt`): 600 against 600, 300 seeds, the higher draw
  won 275 of 287 decided fields and 199 of 199 where the draws differed more than twofold; at 2 : 1 all
  85 upsets went to a smaller side with the higher draw. **Control**: their friction-off arm.
- **Bearing on this scope.** The shared-roller question (F-DICE-07 and its proposal) merges the part of
  the field's chance that does not decide it; the cut test in §1.2 shows that merge is free. The part
  that decides is not a d10, is not a mean shift, is not soft-capped (`M_MAX` bounds named advantage at
  1.5 z; doubling an eight-die pool is about 1.4 z by itself and the 95th percentile is a sixfold pool),
  is not graded, and reaches no record a player or a narrator reads.
- **Touches.** R-04, R-09; resolution-diagnostic P-ii (bypass), P-iii (unbounded), P-v.
- **Minimal fix.** Not decided here: the multiplier is a calibrated, ledgered choice (ED-MB-0016, against
  a historical win-rate curve). §6 gives the two forms.

### F-PES-DICE-05 · degrades narrative · a failed search is forgotten, retried at once, and remembering it would change nothing (known limit confirmed, with a control that narrows its remedy)

- **Claim.** `rosters.yaml: undeposited_kinds` skips `finding.none` at WITNESS for everyone, the actor
  included (H-111, *Jordan to correct*; the roster's note says the person re-forms the act). The dice
  consequence: for an inquiry the draw is a delay.
- **Falsifier run.** E-P6: 157 of 157 `finding.none` Events have no descendant. Of 151 aims that opened
  with a Failure, 49 were tried again, 17 of them reaching a result; non-failure per aim 41.2 and 29.4 %
  (seeds 0, 1) against 32.2 and 22.9 % per roll. **Control, new** (E-P7): seed 0, two seasons, the skip
  arm emptied in memory so that `finding.none` deposits as any Event does (306 descendants on 64 failed
  inquiries; content hash moves, as it must): failed inquiry aims tried again **19 of 42**, against
  **20 of 47** at the shipped arm.
- **Reading.** The roster's note offers a narrower skip (deposit to the actor) as *"the alternative
  Jordan would name"*. The control shows that depositing, to the actor or to everyone, does not reduce
  the retrying: nothing in `decision/` reads a held *"looked and found nothing"*. The missing piece is a
  reader, not a deposit.
- **Touches.** R-07 (memory), R-08 (a person who never learns from a failed attempt is not boundedly
  rational, he is amnesiac).
- **Minimal fix.** Owed to the lanes that own the chooser and the inquiry (CHAR, FI): the candidate for
  an inquiry reads the actor's own held `finding.none` on that subject (count and recency) into his
  believed chance, through the one query `believed_chance` already is. Not written as a proposal here:
  the reader is theirs, and `10_DICE_believed_odds_have_a_prior.md` is the surface it lands on.

### F-PES-DICE-06 · degrades narrative, latent · one die cannot succeed, and a zero cannot try

- **Claim.** At one die the default task's bands are 90 / 10 / 0 / 0: Success does not exist. A held 0
  is refused everything but another 0.
- **Falsifier run.** `band_odds(1, 2.0) == (0.9, 0.1, 0.0, 0.0)`; E-P1 A3 row `s=0`. **Control**: an
  unauthored person (no key) rolls two dice, 74 / 19 / 7 / 0.
- **Relation to earlier findings.** F-DICE-03 (holding a score makes a person easier to oppose) and
  addendum E-B07 (a rank of 1 would lower the pool below the default). This is the same family at the
  degree level: the first point of a skill removes the Success band.
- **Touches.** R-06.
- **Minimal fix.** None separate: it closes with `10_DICE_one_score_two_roles.md` for person-opposed
  rolls (Ob 1.0: 60 / 30 / 10 / 0) and with the unopposed stand-in of this lane's task proposal for the
  rest.

### F-PES-DICE-07 · degrades narrative · the record of a roll is its band (known limit confirmed, H-284)

- **New measurement.** The 208 realm failures missed by 1 (76), 2 (94), 3 (33) and 4 (5); the 76 successes
  cleared by 0 (56), 1 (17) and 2 (3). Every one of those numbers was computed and none is kept.
- **Minimal fix.** `05_SC_obstacle_difficulty_and_modifiers_B.md` puts the obstacle's terms on `Margin`
  and so on the Event. One field is owed to it: `settled_margin`, which the provider already returns
  (`sigma.py:555`).

### F-PES-DICE-08 · hygiene, latent · the obstacle's floor reaches one term and not the sum

- **Claim and run.** The room's favour floors at `OB_MIN`; the sum does not. A held 0 composes Ob 0.0,
  where a second die lowers the chance (90.0 → 89.0 %) and two zeros succeed against each other 90 % of
  the time; a held 1 composes 0.5, below the friendliest room's floor (E-P1 A1, A3, C1).
- **Minimal fix.** Already written: `13_SC_tuning_tables.md` T1 (*"floored at `OB_MIN` after every
  term"*). Cited; no second copy.

### F-PES-DICE-09 · hygiene · the field's four stat checks are bare binaries on the roller

- `recall_check`, `feigned_retreat_recognized`, `feigned_retreat_check`, `discipline_check_cascade`
  (`modules/mass_battle/orchestration.py:2093-2166`): `roll_pool(stat) >= Ob`, pass or fail, where the
  ladder is one call away and the outcomes (a pursuit recalled, a unit overextended, morale lost) are
  graded things. Resolution-diagnostic P-iv. Cross-listed to the MB lane; no proposal.

### F-PES-DICE-10 · hygiene · words (known limits confirmed)

- `argue` at Partial emits `argument.won` and changes nothing (H-269): 7 of 7 realm instances.
- A *contest* (`contests:`) with one roller and no loser; *won* and *lost* name the actor's own band.
  The rename belongs to `verb_table.yaml`'s owner lane and moves every hash whose log uses the kind.

## 5. Summary lists

**False N-lines found** (cuts that are free): mass battle's own `roll_pool` at whole pools (0 of 20,000
nets differ; stream position identical); the Overwhelming band on the social path as shipped; three of
the four named levels in the season; and, already found by the first audit and re-read, `BandExtension`
and the four unused functions of the advantage module. **Narrowed:** Partial as an outcome (four rows);
S27.4 in the provider (a held 0 only). **Survive:** the settle rule, `band_odds`, the ceiling's purpose
(not its form), uniform leverage on dealt dice.

**Premises that failed.** P2 as worded (a task has no difficulty; the one task there is, is hard). P5 in
play (two bands matter; the band changes no state; recovery is forgetting). **Held with breaks at the
ends:** P1 (flat past the ceiling, reversed at Ob 0), P3 (no Success for one die; no loser in a social
act; three scales, three meanings), P4 (holds, uniformly; one source, one sign, never fired; the field's
largest advantage is outside it).

**Stories the dice can tell today:** the attempt that fails; the near thing on four verbs; the clean
success; persistence. **With content:** the strong failing; the upset, to Partial; the triumph, as an
Event kind on two verbs. **Never, as coded:** the disaster; the success that costs; the contest with a
loser; the comeback remembered; character shown by a record of rolls; a triumph that does more than a
success.

## 6. For Jordan (one item survives the ladder)

**The form of fortune in a field.** Not superseded, not irrelevant; the documents point both ways
(ED-MB-0016 calibrates the multiplier; the 2026-08-15 ruling *"ONE resolver for all d10 probability"*
and the mean-shift rulings ED-884 / ED-934 describe advantage otherwise); precedent is split the same
way; the architecture favours the second and would overwrite a calibrated ledger item, so it is listed.

- **Option A — keep fortune as a pool multiplier, owned.** One lognormal per unit per battle, its sigma
  a typed fact (not an environment read), its value written on the field's result so the record says
  *fortune favoured the left*. The game this makes: a field is largely settled by one hidden draw before
  contact; upsets at 2 : 1 are common (about a quarter) and are explained by nothing a commander did.
- **Option B — fortune as named levels through the boost.** The per-battle draw selects a signed number
  of named levels for each side, summed with stance, ground and morale and soft-capped with them. The
  game this makes: fortune moves every exchange by at most 1.5 z in total with everything else, so
  composition, ground and orders decide more and luck less; the historical upset curve the multiplier
  was fitted to may not be reachable and would have to be re-measured.

Already Jordan's, with one measurement added: the pool regime of the season's roll (addendum §5.6). At
the built regime the standing rule's task draw delivers 16.5 % of today's effect at Ob 2 and 42 % at the
floor; at the designed regime's lowest pool (five dice) the same two obstacles give 49 % and 70 %
(`band_odds(5, 2.0)`, `band_odds(5, 1.0)` through the same fraction).

## 7. Proposals written, and corrections owed elsewhere

| file | carries | status |
|---|---|---|
| `proposals/16_PESSIMIST_DICE_soft_ceiling.md` | F-PES-DICE-03 | decided (ladder step 4: the engine's own precedent, `soft_cap`) |
| `proposals/16_PESSIMIST_DICE_task_difficulty_and_throughput.md` | F-PES-DICE-02, -06 | decided (ladder steps 3 and 5); amends three proposals, named there |

Owed to other lanes, one line each (nothing sent, nothing edited): **18-A** ships at `obstacle_default`
(F-PES-DICE-02); **13 / SC-B** three levels collapse on unopposed rows, and `bound()` is the hard `min`
(F-PES-DICE-02, -03); **SC-B** add `settled_margin` to what the Event keeps (F-PES-DICE-07); **the verb
lanes** seven margin rows write nothing in any band (F-PES-DICE-01); **CHAR / FI** the chooser reads no
failed search (F-PES-DICE-05); **MB** four binary checks, and the friction form (F-PES-DICE-09, -04);
**`10_DICE_advantage_sources_for_the_arcs.md`** a source that can count against goes through the 10 %
floor at one die (§1.1 P-iii (c)); **`10_DICE_one_score_two_roles.md`** its gate has no row at an
obstacle below 1.

**Standing-rule check of this lane's own text.** Neither proposal makes an outcome a function of state:
the soft ceiling changes an obstacle (odds), and the task proposal changes an obstacle and adds a
reading to a gate. No correction was needed.

## 8. Evidence log

All under `…/scratchpad/runs/PES_DICE/`, `PYTHONHASHSEED=0`. Nothing in the tree was edited but this file
and the two proposal files.

| id | what ran | seed, n | outcome |
|---|---|---|---|
| E-P1 | `probe_pure.py` → `pure.txt`: exact enumeration through `band_odds`, `record_odds` and `roll.obstacle` on hand-built `SocialContestInput` records with `DEFAULT_FIXTURES`. A1 bands by pool × raw Ob; A2 the per-pool cap; A3 actor × opposition, shipped arm; A4 the same, `obstacle_ceiling=None` (control); B1 one named level on dealt dice against the Normal form; B2 ±40σ; B3 the effort ladder; C1 forgery quality and reception | exact | as quoted in §1 and §2 |
| E-P2 | `soft.txt`: the proposed saturating bound against the hard cap, pools 1 to 8, raw Ob 2 to 10; strict decrease on a 0.005 grid, pools 2 to 12 | exact | no violation at pools 3 to 12; at pool 2 none below Ob 14.9, where `tanh` is 1.0 in a float; lowest chance 10.0000 %; largest Ob ÷ (2 × pool) is 1.0 |
| E-P3 | `probe_scales.py` → `scales.txt`: S1 one score on two scales (social enumeration; combat exchange as the Normal bands of `core.resolve` at no sigma, checked against 100,000 samples through `roll_net_continuous` + `degree_from_net`, seed 7: 62.9 / 16.0 / 17.2 / 4.0 against 63.0 / 15.9 / 17.1 / 4.0); S2 mass battle's `roll_pool` against the owner's on one stream, and the fractional means (seed 11, n 40,000); S3 the friction multiplier's percentiles | 20,000 seeds; 2,000 | 0 nets differ; 2,000 of 2,000 stream positions equal |
| E-P4 | greps and imports: every `rngsource.get().<draw>` under `modules/mass_battle/`; `orchestration.py:2060-2190` read; `modules.mass_battle.config` imported with and without `MB_FRICTION`, `MB_FRICTION_SIGMA`, `FEIGNED_RECOGNIZE_OB` set | — | five draw sites, two of them the d10; `True 1.1 2` against `False 0.5 5` |
| E-P5 | `verb_table.yaml` parsed: `writes` and `emits` per band for the fourteen rolled rows | — | as §2.3 P5 link 4 |
| E-P6 | `probe_realm.py` 0 2 and 1 2 → `realm_s0_2.json`, `realm_s1_2.json`; `analyse_realm.py`. `build_realm`, the shipped chooser over `resolvable_verbs()`, `SeasonDriver._fold` wrapped to record each graded act, its provider record, its Events and the Events citing them | seeds 0, 1; two seasons | 1,529 and 1,519 resolved acts; 118 and 166 margin rolls; **hashes `bacd687f1470883b412be9638d0b0f88` and `8aae8412c221edb44ffd45d91bae2671`, equal to the SC interrogation lane's seed-0 tap and the determinism sweep's seed-1 run** (the wrapper moved nothing) |
| E-P7 | `probe_realm_deposit.py` 0 2 → `realm_s0_2_deposit.json`: the same with `loop.witness.UNDEPOSITED_KINDS` emptied in memory | seed 0; two seasons | hash `1b61dd6127a682b09a9ee0c685340975` (moved, as declared); 120 margin rolls; failed inquiry aims tried again 19 of 42 (shipped arm 20 of 47) |
| cited | `runs/SC_INT/realm_tap_s0.json`, `_s1.json` (rolls per person re-tabulated here); `runs/PES_MB/p1_size.txt` (friction; not re-run) | — | — |

Not run: `pytest`; any `aperture` or `corpus_run`; a fought field (none occurred in E-P6; the field's
figures are the MB pessimist lane's). `[UNVERIFIED]`: that the four binary checks of F-PES-DICE-09 are
reached from the season's field (the call sites at `battle_loop.py:438` and `orchestration.py:2257`,
`:2392`, `:2430` were read, not executed).

