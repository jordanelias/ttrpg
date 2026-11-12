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

