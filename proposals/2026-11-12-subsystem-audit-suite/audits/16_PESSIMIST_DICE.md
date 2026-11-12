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

(Sections below are appended as the work proceeds; §0 is written last and placed first.)

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
are named per row. Evidence ids are in §9.

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

