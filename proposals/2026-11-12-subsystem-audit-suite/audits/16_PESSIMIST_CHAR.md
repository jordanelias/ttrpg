# CHAR — pessimist audit (NERS, premise, emergent narrative) of the character model and the decision layer

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: d161a61 (working tree)

Scope: `engine/season/decision/`, `engine/season/queries/person_q.py`, goals, convictions, scars,
attributes, the cast, the chooser; the NPC and AI-chooser intent as established in `02_CHAR_audit.md` §0A
and `02_CHAR_audit_addendum_B.md`; and the six premise sentences of a person. Prior work cited, not redone:
`02_CHAR_audit.md` (F-CHAR-01..15), `02_CHAR_audit_addendum_B.md` (F-CHAR-16..22), the `02_CHAR_*`
proposals, `18_DETERMINISM_SWEEP.md`, `16_PESSIMIST_GAME.md`. No code under `engine/`, `modules/`,
`systems/`, `references/` or `tools/` differs between the first CHAR audit's read (601e715) and this one
(`git diff --stat`: empty), and this lane's season hashes reproduce theirs (`5ab73af2`, `bacd687f` at seed 0;
`8aae8412` at seed 1, season two), so the earlier figures are cited as current.

Everything measured here is new unless a lane is named. All runs: `PYTHONHASHSEED=0`,
`harness/populated.py::build_realm`, the shipped chooser over `resolvable_verbs()`, no player, no hand-built
act unless the row says PROXY. Scripts and outputs:
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/PES_CHAR/`.

## 0. Verdict

**A person in this engine is a seat, a ledger and a coin: none of the six premise sentences of a person
holds as its words read, and the parts of the character model that carry names (the fifteen pursuits,
the creed, the scar, the scruple, the skill) are, in computed play, either free to cut, inert, or doing
something their names do not say.** Measured: a man who holds only `love` puts `forge` first in 266 of
276 situations, and so do the men of `family`, `wealth` and `reputation`; thirteen of fifteen pursuits
fail a two-line statement of what their name means; the same man asked the same question twice changes
his first choice 61% of the time, while swapping his entire religion changes it 2 to 5% of the time;
the one change that reaches a person's interior (a crisis of faith) strikes the same six persons at
both seeds, by a rule with no draw, emits no Event, and converts an orthodox man to the rival creed at
a higher intensity than he held his own (31 of 46 cast would have their strongest creed replaced by
its rival); the ruled refusal that should stop a man is off, and switched on it stops all 46 cast from
moving house, handing something over and trading; all 46 cast roll two dice at every skill there is,
and over three seasons at seed 1, 77% of everything rolled failed and nothing reached the top band; the
scar can be deleted without changing one act of 1,529 in two seasons; of 21,312
beliefs held after three seasons 312 are false and 296 of those are the grain count of a store; and
`Act.reads` is empty on every one of 4,757 resolved acts. The steelman holds where it was tried: the
layer is honest about itself (every dormant arm is declared, every assumption marked), it does not
crash at any extreme this lane fed it, the hashes replay, and pursuits do decide which verbs a person
takes (cutting them moves a person's conduct by 0.64 in total variation, against 0.01 for cutting the
believed-odds weighting; though re-rolling the dice alone moves it by 0.49). The pessimist reading is that the product of two invented tables was never
read against the names on its rows, and that every mechanism which would make a person change, refuse,
excel or be mistaken ships at its control. The single largest obstacle is therefore content with a
target, not structure: say in data what each name must mean in acts (proposal B), and let the three
interior mechanisms that exist act by a draw and leave a trace (proposals A and C).

**On the standing rule (*we do not do deterministic*).** Four fixed functions of state in scope:
the crisis of faith (*"ROLLS NOTHING"*, `person_q.py:903`; live, F-PES-CHAR-03); the choice between
acting for and against anyone a person has a stance on (the gap between the two classes is 800
temperatures, F-PES-CHAR-04); the refusal threshold (dormant, F-PES-CHAR-02); and a pool of one die at
the default obstacle (P(Success or better) exactly 0.000; a pool of zero is refused), which is the SC
and DICE lanes' and is listed for them (F-PES-CHAR-05). This lane's three proposals were checked
against the rule: A and C replace a fixed outcome with a draw (each names the ruled item it meets and
leaves that to Jordan); B decides no outcome.

## 1. Premise — the six sentences, three accounts

### 1.1 Account one: the ordinary meaning (written BEFORE reading any note or code)

This table was the first thing written to this file, before `02_CHAR_audit.md` or any code was opened
(`skills/premise-check` STEP 2). It is what a player who knows strategy and RPG games would take each
sentence to mean.

| # | premise | what each link should do, in ordinary words |
|---|---|---|
| P1 | a man pursues what he wants and is stopped by what he believes | He has a want that is his own and that he can name. Given a free hand he takes the act that advances it. There is at least one act that would advance it and that he will not take because of a belief, and a man without that belief takes it. The stop has a cost he can be seen to pay (the want goes unserved), and under enough pressure the belief may give way, which is itself an event. |
| P2 | two men with different convictions choose differently in the same situation | Hold the situation fixed (same place, same options, same knowledge, same want); change only the conviction; the choices differ often enough to be noticed, in the direction the convictions' names predict (the merciful man spares, the lawful man reports). The difference is the conviction's and not the dice's: the same man re-drawn mostly chooses as himself. |
| P3 | a man changes over time because of what he does and what is done to him | What he does (kills, betrays, keeps faith, fails) and what is done to him (wounded, robbed, pardoned, bereaved) leave marks that persist, and the marks change later choices: he chooses differently after than before, in a direction the event explains. Change is not only decay; it is specific to the event. A man to whom nothing happened is unchanged. |
| P4 | a man is wrong about the world | He holds a belief about a fact (who did it, who holds the seat, how strong the garrison is, whether he is liked) that differs from the truth; he acts on the belief and not the truth; the act goes badly or strangely because of it; he can find out, and finding out changes what he does. Ignorance (not knowing) is the weaker cousin; the sentence asks for a false belief. |
| P5 | a man's reasons are readable afterwards | After the act, a record states why this man took this act rather than the other on offer: which want, which belief, which pressure, what he knew. A narrator can read it without re-running the chooser, and two different reasons produce two different records. |
| P6 | a skilled man usually beats an unskilled one | Skill is a property of the person. In any contest where it applies, the more skilled wins more than half the time, rising with the gap, never to certainty (the standing rule: no deterministic outcome); the same holds in a choice of what to attempt (the skilled man attempts what he is good at). |

### 1.2 Account two: what the code's notes say, in aggregate

Read from the docstrings of `decision/choose.py`, `decision/options.py`, `queries/person_q.py`, the roster
notes and the first audit's §0A (cited, not redone).

- **P1.** A want is a weighted vector over fifteen pursuits projected on seven axes (I-3), plus a standing
  `commit` to an OUGHT that raises a question each season (I-4). The stop is `ED-IN-0261`'s deontological
  gate: *"it's a refusal to take certain actions"*, *"the weighting is a threshold"* (`options.py:568-608`),
  and separately clause 4, a person does not form an act whose premise he believes false. The notes say the
  gate is *"armed nowhere"* (`rosters.yaml:540`).
- **P2.** *"A choice is a ranking by values and regard, sampled"* (I-6); `Person.conviction` is religious
  affiliation as a separate intensity (ED-IN-0251) that *"strongly modulates"* the `doctrine` pursuit
  (`person_q.py:804`).
- **P3.** *"What is right is moved by argument and consequence, never by evidence"* (I-8); the scar is a
  count per element accrued by witnessing, with thresholds 1 / 2 / 3 (`person_q.py:796-801`); the crisis at
  3 *"ROLLS NOTHING"* (`person_q.py:903`); practice raises a pool (`data/fixtures.py:467-479`); a deed is
  judged *"by `p`'s OWN pursuits"* and *"a deed's claim subject is read as its doer"*
  (`person_q.py:98-129`).
- **P4.** A person decides on his own ledger and never on world truth (I-2); hearsay is graded when read
  (I-10); believed odds are his own (`sigma.py:363-365`).
- **P5.** The occasion rides the `Scene`; `Act.reads` exists as a field; `why` was cut from `Candidate`
  (first audit §0A).
- **P6.** *"Capability supplies dice and gates nothing"* (I-11); `pool_default` *"IS WHAT `capability` WOULD
  SUPPLY AND DOES NOT"* (`data/fixtures.py:434`).

The notes are candid: accounts two and three rarely disagree. Account one disagrees with both.

### 1.3 Account three: the running code (verdict by execution)

Verdicts: **HOLDS**, **NARROWED** (holds in a sense the words do not promise, or in one direction only),
**FAILS**, **UNREACHED** (no instance occurs in computed play, so the premise has nothing to be true of).

| # | premise | verdict | the cheapest observation that decided it | finding |
|---|---|---|---|---|
| P1a | a man pursues what he wants | **NARROWED** | 243 commitments are live after three seasons at seed 0 (226 at seed 1) and **0 have ever ended**; 11 of 749 resolved acts in a season answer the actor's own want (first audit). A want is a question he is asked each season; nothing counts toward it and nothing completes or abandons it | -07 |
| P1b | and is stopped by what he believes | **FAILS** as a belief about what is right; **HOLDS** as a belief about what is so | moral: shipped (`refusal_axis: None`), no candidate refused in 276 readings; armed, all 46 cast refuse `transfer`, `move`, `forge`, `reconstruct`, `exchange` in 276 of 276, so the stop is the realm's and not the man's. Factual: with clause 4 cut, refusals rise 656 to 762 in two seasons, so he does decline what he believes cannot be done | -02 |
| P2 | two men with different convictions choose differently | **NARROWED** to pursuits; **FAILS** on the field named `conviction` and on the names | swap a man's whole religious affiliation: his top act moves in 6 to 15 of 276 readings (2 to 5%); redraw the same man: it moves in 61%. A man of `love` alone tops `forge` in 266 of 276 | -01, -04 |
| P3 | a man changes because of what he does and what is done to him | **FAILS on cause, on direction and on trace** | the one change that fires (the crisis) strikes the same six persons at seeds 0 and 1, by a rule with no draw, from witnessing forgeries, emits no Event, and replaces the stronger creed with its rival. Two hostile acts naming a person resolve in two seasons; those targeted by `challenge`, `sabotage` and `lie` regard the actor more warmly afterwards | -03, -08 |
| P4 | a man is wrong about the world | **NARROWED** to stale granary counts | of 21,312 beliefs after three seasons, 1,448 are about a present fact; 312 of those are wrong, and 296 of the 312 are the count of grain or salt in a store. Believed odds equal true odds in 46 of 46 priced readings at build | -06 |
| P5 | a man's reasons are readable afterwards | **FAILS** | `Act.reads` is empty on 2,367 of 2,367 resolved acts (seed 0) and 2,390 of 2,390 (seed 1); 742 scenes carry an occasion (`claim_landed` 658, `need` 84) and nothing of the ranking | -09 |
| P6 | a skilled man usually beats an unskilled one | **UNREACHED**; **FAILS** by hand for `argue` and `tell` | all 46 cast roll a pool of 2 on all nine verbs that read a skill. PROXY: with the actor's key raised, P(Success or better) rises 0.00, 0.07, 0.17, 0.28, 0.47, 0.61, 0.80 at 1, 2, 3, 4, 6, 8, 12 dice; with the SUBJECT's key raised 0 to 8 it does not move | -05 |

The three questions of the skill, answered once for the set:

- **Genre.** A player would be surprised by every row. The sharpest: a character sheet whose largest
  entry is `love` produces a forger; a devout character converts to the enemy church after seeing
  three forged papers; nobody is good at anything.
- **Premise.** The right actor exists in each case and the effect is the wrong one, or absent.
- **Words.** `conviction` (the field) is not conviction (the premise's word): it is a religious
  intensity whose content barely enters a choice. `scar` is not a wound: it is a tally of disagreeable
  things seen, triggered for `love` by gifts. `refusal` refuses moving. `capability` supplies the same
  two dice to all. `regard` for a man rises after he sabotages you if you approve of sabotage. The
  levels and values make sense of none of these words except `honour`.

## 2. NERS — cut tests, executed

Method (`skills/ners/SKILL.md`; definitions `CLAUDE.md` §0.06): propose the cut, name what dies. A
person's parts can be cut in a running realm, so each cut was run: `d1_cuts.py`, `build_realm(0)`, two
seasons, shipped chooser, one arm per part. A choice is sampled, so any change to anything moves the
hash; the comparison is therefore against a **noise floor**, the same world under another choice-draw
seed (`drawseed`). Three distances from the shipped arm: total variation of the realm's resolved-verb
distribution; mean total variation of each person's own verb profile from his shipped self; and
identification (for each person in the shipped run, is the nearest verb profile in the arm his own;
chance is 1 in 83). A cut is **free in computed play** when all three sit at or under the floor's. The
shipped arm reproduces `5ab73af2`, `bacd687f`, so the harness is the shipped engine.

| arm (what is cut) | acts | refused | TV realm | TV person | identified | interior moved (persons of 83) | reading |
|---|---|---|---|---|---|---|---|
| shipped | 1,529 | 656 | 0 | 0 | 83/83 | pursuits 1, stance 0, conviction 0, body 0, scar 83 | the base |
| `drawseed` (**noise floor**: the same world, another choice-draw seed) | 1,572 | 614 | 0.118 | 0.488 | 13/83 | pursuits 1, stance 1, body 5, scar 83 | re-rolling the dice changes half of what each person does |
| `noscar` (the scar writer and the crisis off) | 1,529 | 656 | **0.000** | **0.000** | **83/83** | scar 0, otherwise as shipped | **free: not one act differs** |
| `noodds` (believed-odds weighting CR-17 and NPC effort CP-T01-05 off) | 1,520 | 652 | **0.008** | **0.012** | **82/83** | as shipped | **free** |
| `noconviction` (every `Person.conviction` emptied) | 1,533 | 658 | **0.022** | **0.053** | **83/83** | as shipped | **free, nearly** |
| `nostance` (the stance term zeroed) | 1,497 | 551 | 0.126 | 0.273 | 71/83 | pursuits 2, stance 6, body 12 | not free: what dies is restraint (persons harm those they were loyal to) |
| `nobelief` (clause 4, `belief_contradicts`, off) | 1,434 | 762 | 0.155 | 0.290 | 60/83 | as shipped | not free: 106 more refusals, 95 fewer acts, findings 120 to 86 |
| `tau0` (no draw in the choice) | 1,609 | 435 | 0.275 | 0.448 | 16/83 | conviction 6 (a season early) | not free: a monoculture (`create_record` 334, `utter` 206); and 221 fewer refusals |
| `nopursuit` (every person's pursuits emptied) | 1,269 | 698 | 0.365 | 0.639 | 12/83 | stance 7, conviction 1, body 13, scar 29 | not free for the realm's mix; for a person, little past the floor; **more happens to persons without wants** |
| `samemen` (the instrument's own control: realm-mean pursuits and conviction, no goals) | 1,524 | 686 | 0.342 | 0.653 | 12/83 | stance 8, body 7, **a seat changed hands**, one death | as `nopursuit`: a realm of identical men is livelier than the shipped one |

Two cautions on reading the table. The cut arms share the shipped arm's draw seed, and the choice
draw is keyed by candidate (`choose.py:462`), so an arm that barely moves the scores reproduces
nearly the same acts: the small distances (`noscar`, `noodds`, `noconviction`) are exact statements
that almost no act changed, not statements about noise. The floor uses different random numbers, so
*identified 13/83 after a re-roll* and *identified 12/83 after deleting every want* are not strictly
like for like; the like-for-like comparison (`samemen` against `samemen` re-rolled) was not run.
Single seed (0), two seasons; the crisis first fires in season three at seed 0, so `noscar` and
`noconviction` are free through two seasons and bounded after that by F-PES-CHAR-03's 2 to 5%.

### 2.1 What the cuts say

- **Three named parts of a person are free to cut in computed play**: the scar, the creed, and the
  believed-odds weighting with NPC effort. §5 lists them with the parts that are free by construction.
- **Three parts are necessary, and each for something other than what it is named for.** The stance
  term is necessary as *restraint*; clause 4 is necessary as *not attempting what he believes cannot be
  done* (the one sense in which P1's *"stopped by what he believes"* holds: it spares the realm 106
  refusals in two seasons); the draw is necessary as *variety*, and its price is 221 refusals, because
  it carries persons past their first choice into acts the fold refuses.
- **The pursuit term is necessary to the realm's mix of acts and weakly to the person.** Deleting every
  want moves a person's conduct by 0.64; re-rolling the dice moves it by 0.49; replacing every person
  with the average man moves it by 0.65. And every arm that removes a determinant of the choice
  (`nopursuit`, `samemen`, `nostance`) produces more change in persons' bodies and stances than the
  shipped arm, which produces none in two seasons. The shipped combination is the quietest realm of the
  ten (F-PES-CHAR-10).

### 2.2 The four criteria, read on the person as a whole

- **N, from six directions.** *Bottom-up* (does a part change an act): pursuits yes; conviction in 2 to
  5% of readings; scar no (its one live reader is the crisis); skill no (everyone holds the default);
  believed odds no. *Top-down* (does the realm differ for having persons with character): the realm's
  skeleton does not move at all in three seasons (`16_PESSIMIST_GAME.md` X1), so no part of a person is
  necessary to it. *Vertical* (person to seat to faction): a seat-holder's ranking is the faction's
  conduct (I-1), and 0 of 83 persons gained or lost a seat in six seed-seasons, so character never
  selects who rules. *Lateral* (person to person): 37 of 6,806 ordered person pairs hold any regard at
  build; where one exists it decides for-or-against with certainty, where none exists the pair is
  strangers. *Diagonal* (a person's interior to another scale's outcome): none found; a field, a
  settlement and a store read no pursuit. *Horizontal* (sibling mechanisms): the scar, the crisis, the
  refusal and the pursuit term all read one product of two tables, so one content defect is four.
  An N-line that holds in one direction is narrowed: the pursuit term is necessary bottom-up only.
- **R.** The half with no player: persons generate paperwork and 6 or 7 silent conversions per three
  seasons (§3). Completeness at the extremes (`x1_extremes.py`, one cast person, temperature 0): no
  crash on no pursuits, every pursuit at 100 or at −1, an empty ledger, no stance, no tenures, body 0,
  a scar of 100 on everything. But three extremes are degenerate: with no pursuits the 19 candidates
  take 2 distinct scores (the choice is the draw inside a stance class); at body 0 the ranking is
  identical to full health (first audit F-CHAR-14, addendum F-CHAR-20); and with the dormant scar shift
  armed at 0.5, a man scarred to 100 on every pursuit ranks exactly as an unscarred one, because the
  shift needs an unscarred pursuit to give weight to (`person_q.py:883`): the most wounded man in the
  realm is the least changed, and by the addendum's F-CHAR-17 everyone is that man by season three.
- **S.** *Calculations consistent in methodology*: the refusal compares a projected weight (cast range
  −0.395 to +0.306) with an alignment cell on ±1 (F-PES-CHAR-02); the score adds a pursuit term of
  about ±0.3 to a stance term of ±20 (first audit F-CHAR-08, and F-PES-CHAR-04 for what that does to the
  draw); a deed is judged by its kind against the judge's taste while a killing alone reads who it was
  done to (F-PES-CHAR-08). *Pauses correctly*: not tested here (the grid suspension is the PC lane's).
- **E, last, as a ratio.** N and R found one working discriminator (the pursuit term) and four parts
  that are free or inert in play. Against that stand fifteen names, seven axes, five creeds with an
  incompatibility relation, a three-rung scar with a crisis of three branches, a refusal with a pole
  roster, two regard gains, a heritage term, five hearsay fixtures and a practice arm. The overhead is
  large for what it presently buys, and the player cannot *"intuit complex outcomes from simple
  choices"* because the simple choice (`love: 0.9`) has an outcome nobody would guess. The repair is not
  amputation (E is not scored alone): each part is the right part; each lacks either a target or a
  switch.

### 2.3 Resolution-diagnostic evidence on the one draw this subject owns

The chooser's draw is Plackett-Luce by Gumbel at `choice_temperature` 0.05 (`choose.py:431-471`). The
first audit measured it as too loud between strangers (F-CHAR-02). Two further properties, carried in
as evidence:

- **Test-retest** (`c1_two_men.py` (b), 46 cast × 6 referents × 5 ticks' draws): the same man in the
  same situation takes a different first act in 60.7% of 2,760 redraw pairs (top-three overlap 0.46);
  two different men at one tick differ in 83.0% of 6,210 pairs (overlap 0.25). So one observed choice
  identifies its man about four times in ten.
- **A class gate with no tail** (`x1_extremes.py`): for a subject the person holds regard +10 on, the 19
  candidates split into those the row treats as for the subject (score near +20) and against (near
  −20). The gap is 40, which is 800 temperatures; a stance of 1 gives a gap of 4, 80 temperatures. The
  probability that the draw carries a man across is of order e^−80 at the smallest authored stance. The
  draw is therefore nominal exactly where a relationship exists, and total where none does.

## 3. Emergent narrative — persons, with no player

### 3.1 What stories a person can have at all (enumerated from the writers of `Person` state, not from documents)

| # | story | the writer | in computed play (seeds 0 and 1, three seasons each, 83 persons) |
|---|---|---|---|
| 1 | loses or changes his faith | `resolve._conviction_crisis` | 6 and 7 persons; the same six at both seeds, on the same vectors; no Event |
| 2 | is persuaded | `_eff_argue` → `argued_pursuits` | `argue` rolled 19 times at seed 1: 14 Failure, 5 Partial, 0 Success. Nobody was persuaded |
| 3 | is changed by his own judgement | `_eff_determine` → `consequence_pursuits` | `determine` graded once (Partial). Pursuits moved for 2 persons at seed 0 (largest single move 0.027 on a weight) and 0 at seed 1 |
| 4 | comes to like or hate someone | `regard` (computed), stance rows | computed regard for the actor moved for 289 of 612 patients (median 0.24), with a sign unrelated to the act (§4, -08). A stored stance row appeared for 1 and 2 persons, toward factions; one of them (Vidar Haldorsen, the same two rows) at both seeds |
| 5 | is wounded and recovers | `body` writers | cast: 0 at seed 0 through two seasons; the 37 cohorts go hungry once and are tended |
| 6 | dies | `_eff_kill`, hunger | 0 at seed 0; 1 at seed 1 (the cardinal `16_PESSIMIST_GAME.md` names), answered by nobody |
| 7 | gains or loses a seat | `confer`, `succeed`, `revoke` | 0 of 83 in six seed-seasons |
| 8 | learns a skill | `_eff_train`, practice | capability moved for 0; `train.refused` 119 and 116 |
| 9 | achieves or abandons an ambition | none: a `commit` has no closer in play | 0 of 243 and 0 of 226 commitments ended |
| 10 | moves house | `migrate`, `move` | 16 and 5 residences ended; the one person-story that completes, and it changes nothing later |
| 11 | is tempted and gives way | none (`refusal_axis` dormant; no trace when armed) | cannot happen |
| 12 | forms a tie (kin, oath, patron, rival) | none: `tie` and `knot` have no opener (addendum F-CHAR-18) | cannot happen |
| 13 | ages, sickens | `age_step`, `illness_rate` ship 0 (`16_PESSIMIST_GAME.md`) | cannot happen |
| 14 | is deceived and acts on it | `lie`, `forge`, the ledger | `lie` rolled 10 times at seed 1 (8 Failure, 1 Partial, 1 Success); false beliefs from a teller: 8 and 1 of 21,312 and 19,038 |

### 3.2 Beginnings, escalation, reversal, cost, ending, retelling

Read on the one story that occurs (the conversion), as the best case:

- **Beginning.** There is none a narrator could point to: the trigger is the third forgery or defiance
  witnessed (`forge` is 117 of the 129 creed-violating acts resolved at seed 1), and four of fifteen
  pursuits make `forge` their holder's first act, so the realm's apostasy is a by-product of the
  alignment table's taste for forgery.
- **Escalation.** The count rises with every witnessed act and never falls (addendum F-CHAR-17).
- **Reversal.** It is the story's only beat, and it is an inversion nobody chose (-03).
- **Cost.** None is visible: the convert's choices move in 2 to 5% of situations, his seat, ties and
  standing are untouched, and nobody else knows.
- **Ending.** After one fold the rival creed has no incompatible partner left, so the unbuilt
  RESTABILISE branch makes the person immune for good. The story ends by exhaustion.
- **Retelling.** No Event, so no claim, so no chronicle line. `conviction.moved` is declared on the row
  and emitted by nothing (0 in every arm's log).

### 3.3 The shape of the tail: are all runs the same run

- **Who changes.** The six converts are the same at both seeds. `x1_extremes.py` reads the whole
  outcome off the build with no play: of 46 cast, 31 fold to the rival of their strongest creed, 1 is
  left with nothing, 14 can never change. The end state of the realm's faith is the build's mirror
  image, and the only thing a seed decides is the season.
- **Who does what.** A cast person's three-season verb profile at seed 0 is nearest to his own at seed
  1 for 23 of 46 (chance 1 in 46; his distance to himself 0.47, to the others 0.75). So half the cast
  are recognisably themselves across seeds, which is the steelman's best number, and half are not.
  A cohort is itself for 4 of 37: populations are interchangeable. Within one run a person's first
  season identifies his third for 9 of 82.
- **What a player changes.** Not run here; `16_PESSIMIST_GAME.md` X4 is the reading.

### 3.4 Are the persons' reasons readable afterwards

No (-09). What survives a decision is the occasion. What decided it is, in 45% of readings, the draw
(first audit: 223 of 498), and in the rest a sum whose larger term is a constant per subject. A faithful
reason trail would say *"no reason"* for nearly half of what persons do; the trail proposals
(`01_CORE_reason_trail_in_the_act_store.md`, `02_CHAR_reason_trail_and_small_edits.md`) should record the
deciding term, the draw included, or they will narrate motives that were not there.

### 3.5 Extremes

The chooser survives every person-level extreme tried (§2.2 R). Two realm-level extremes were run
(`x2_alone.py`, seed 0, three seasons): **nobody acts** (0 acts, 0 scars, the cohorts' hunger and
nothing else) and **one person acts** (the King alone: 43 acts, no ending, nothing answers him because
nobody else may, and his paperwork scars all 83 persons, F-PES-CHAR-12). A lone actor's story is a list:
no beat of it depends on an earlier one. A world of literally zero or one person and a hundred
factions was **not run** (the machine was at a load average of 40 and a season cost 30 to 190
seconds): `[SKIPPED: zero-person and one-person worlds, hundred-faction worlds — cost]`.
`16_PESSIMIST_GAME.md` X5 is the reading for the realm.

## 4. Findings — ranked worst first

Severity: **B** blocks a requirement, **D** degrades narrative, **H** hygiene. Each: claim; evidence;
falsifier run and its control; requirement touched; minimal fix at the owner.

### F-PES-CHAR-01 · B · the names on a character do not predict his acts

- **Claim.** The pursuit term is the product of two invented tables that was never read against the
  fifteen names. Thirteen of fifteen names fail a two-line statement of what the name means.
- **Evidence.** `a0_words.py` (pure leans, 66 verbs), `c1_two_men.py` (c) (the live candidate set,
  46 cast × 6 referents, temperature 0, each cast person re-run holding one pursuit only): top act
  `forge` in 266 of 276 readings for `love`, `family`, `reputation` and `wealth`; `utter` 266 for
  `justice`, `virtue`, `doctrine`; `create_record` for `community`, `stability`, `stewardship`;
  `exchange` for `scholastics`; `surveil` for `liberty`; `release` for `happiness`; `survey` for
  `individuality`; `challenge` 260 for `honour`. By lean, `love` is violated by `give`, `restore`,
  `speak`; `justice` by 30 verbs including `open_case`, `petition`, `convene`; `community` and
  `stewardship` by `build`, `found`, `work`. Twenty-five of 66 resolvable verbs carry no cell on any
  axis: `forgive`, `pardon`, `tend`, `arrest`, `capture`, `raze`, `sabotage`, `conceal`, `tell`,
  `train`, `argue`, `interrogate` among them. `a2_sig.py`: against a starting signature set (two or
  three verbs a name must favour and oppose), 13 of 15 break on 35 clauses.
- **Falsifier and control.** If the names were satisfied, the single-pursuit holders would top
  different verbs, each in its name's direction. `honour` is the control that shows the reading can
  pass: it tops `fight`, `accept`, `commit`, `challenge` and opposes `evade / defy`, `lie`, `forge`.
  Scaling every verb row to unit length (`a1_norms.py`) does not repair it (`love` still tops
  `destroy_record`, `forge`), so the cause is the cells and the missing rows, not the loud rows.
- **Touches.** R-06 (robust characters), R-07 (the scar reads the same product), the capability
  authoring charge (a designer who sets `love` gets a forger).
- **Minimal fix.** `proposals/16_PESSIMIST_CHAR_B_a_pursuit_does_what_its_name_says.md`.

### F-PES-CHAR-02 · B · nothing stops a man, and the thing built to stop him stops everyone from walking

- **Claim.** P1's second half has no live mechanism; the ruled one cannot be armed as built.
- **Evidence.** `c2_stopped.py` (seed 0): shipped, 0 candidates refused in 276 readings; armed on the
  ruled axis, 46 of 46 cast refused, `transfer`, `move`, `forge`, `reconstruct`, `exchange` in 276 of
  276, `survey` 270, `lie` 37; the gate took the person's top act in 53 readings, for a median of 0.045
  of score. The other reading of *believes* (clause 4, a premise believed false) declines about 4% of
  candidates (first audit) and is necessary under the cut (§2, arm `nobelief`): that half holds.
- **Falsifier and control.** A personal stop would refuse some persons and not others (strictly between
  0 and 46). Unarmed is 0; armed is 46.
- **Touches.** R-06, R-08; H-146.
- **Minimal fix.** `proposals/16_PESSIMIST_CHAR_C_the_stop_is_the_mans.md`.

### F-PES-CHAR-03 · B · the only interior event is a fixed, inverted, silent conversion

- **Claim.** In computed play the one writer that changes who a person is fires as a function of the
  build, turns him into his opposite, and tells nobody.
- **Evidence.** `b1_season.py`: seed 0, conviction rewritten for 6 persons (all in season three); seed
  1, the same 6 in season two and a seventh in season three; each of the six ends on the same vector at
  both seeds. `x1_extremes.py`: 31 of 46 cast fold to the rival of their highest-held creed (every
  Einhir adherent at 5 becomes Solmund-orthodox at 5 and the reverse). `person_q.py:932-938` records
  why. `resolve.py:706-708`: nothing emitted; `conviction.moved` is 0 in every arm's log, the `tau0`
  arm included, where six convictions were rewritten inside the two seasons. Trigger: `forge`
  117, `evade / defy` 8, `thread_read` 4 of 2,390 resolved acts at seed 1. Effect on choice: 2 to 5%
  (`c1_two_men.py` (a)).
- **Falsifier and control.** Were it an outcome of play, the set of converts would differ between
  seeds. It does not. Control for the reading: persons who hold one creed with something compatible
  (14 cast) never change at either seed, as the code predicts.
- **Touches.** R-06, R-07, R-09 and the standing rule.
- **Minimal fix.** `proposals/16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told.md`.

### F-PES-CHAR-04 · D · between a certainty and a coin there is little room for a character

- **Claim.** Where a person holds a stance, whether he acts for or against its object is certain; where
  he holds none, the same man redrawn disagrees with himself six times in ten; and the field named
  `conviction` moves his first choice less than either.
- **Evidence.** §2.3 (test-retest 60.7% against 83.0% between men; the 800-temperature class gap);
  `c1_two_men.py` (a): replacing a person's `conviction` with nothing, with all zeros, or with any one
  creed at 5 moves at least one score in 204 to 276 of 276 readings and the top act in 6 to 15.
- **Falsifier and control.** If conviction decided, the swap would move the top more often than a
  redraw does. Redraw 61%; swap 2 to 5%.
- **Touches.** R-06, R-08; the standing rule (the class gate).
- **Minimal fix.** No new proposal. Two amendments to existing ones, decided at ladder step 5:
  (a) `02_CHAR_resolve_and_temper.md` gains the test-retest reading as its gate (a person's
  self-agreement must exceed the between-person agreement by a stated margin; today 39% against 17%);
  (b) `02_CHAR_scar_cap_and_regard_unit.md` item 3 (the clamp at `STANCE_MAX`) is necessary and not
  sufficient: `choose.stance_term` should return regard as a share of `STANCE_MAX` (on ±1, the pursuit
  term's own range) times the existing gains, behind a fixture whose control is today's value, so that a
  strong loyalty makes moving against its object rare and not impossible.

### F-PES-CHAR-05 · D · nobody is skilled, everybody fails, and an opponent's skill is not in the roll

- **Claim.** P6 has no instance in the built realm; where an instance is built by hand the opponent's
  skill is missing for the two commonest contests.
- **Evidence.** `c3_skill.py`: pool 2 for 46 of 46 cast on `tell`, `speak`, `argue`, `research`,
  `examine`, `surveil`, `fight`, `accept`, `capture`; five contested verbs (`arrest`, `interrogate`,
  `march`, `determine`, `lie`) name no capability at all. True odds at that pool: Failure 0.74, Partial
  0.19, Success 0.07, Overwhelming 0.00. In play (`b1_season.py`, seed 1, three seasons, 282 graded
  rolls on `research`, `surveil`, `tell`, `argue`, `speak`, `lie`, `determine`): Failure 216 (77%),
  Partial 50, Success 16, Overwhelming 0. `c3b_curve.py` (PROXY, hand-built acts): `argue` and `tell` do not move
  with the subject's key from 0 to 8; `speak` does. A key of 1 gives exactly 0.000; a key of 0 is
  refused.
- **Falsifier and control.** The curve responds to the actor's key (0.07 to 0.80 over 2 to 12 dice), so
  the roll can express skill; the realm holds none to express.
- **Touches.** R-06, R-09.
- **Minimal fix.** Not this lane's to add: content through `02_CHAR_capability_definitions.md` (addendum
  F-CHAR-19); the base rate through `13_SC_calibration.md`; the opposed obstacle through
  `05_SC_opposed_obstacle_parity.md` (held back, RULED) and
  `05_SC_obstacle_difficulty_and_modifiers_B.md`. Listed for the SC lane: `argue` and `tell` read no
  opposing skill today (`rosters.yaml: vocation_attribute.opposed_by` serves `speak` only, by the run).

### F-PES-CHAR-06 · D · a man is wrong about the granary and about nothing else

- **Claim.** False belief exists as staleness of one quantity. Nobody is wrong about who did a thing,
  who holds a seat or what he can do.
- **Evidence.** `b1_season.py`, at the end of three seasons, each person's belief (`LedgerReader.read`)
  on every (subject, predicate) he holds a claim on against `WorldReader.read`: seed 0, 21,312 beliefs,
  19,864 about past events (no present fact to be wrong about), 1,136 agree, 312 disagree, of which
  `stores:*` 296, `exists:*` 11, `room:*` 3; by source `inferred` 268, `firsthand` 36, `told_by` 8. Seed
  1: 19,038; 1,075 agree; 306 disagree; `stores` 294; `told_by` 1. `c3_skill.py`: believed odds equal
  true odds in 46 of 46 priced readings at build (`determine`); 151 `capture` readings have no believed
  figure at all.
- **Falsifier and control.** The reader sees disagreement where it exists (the stores), so *agree* is an
  observation. `[UNVERIFIED: whether a deed's doer is ever misattributed; `deed_doer` refuses to guess,
  so by reading it cannot be]`.
- **Touches.** R-08.
- **Minimal fix.** Owners elsewhere, cross-listed: the telling lane (first audit F-CHAR-09),
  `10_DICE_believed_odds_have_a_prior.md`, `14_VERBS_SOCIAL1_C_persuasion_and_deceit.md`. No CHAR edit.

### F-PES-CHAR-07 · D · a want never ends

- **Claim.** A commitment is made and is then held for ever; no person in six seed-seasons fulfilled,
  failed or dropped one.
- **Evidence.** `b1_season.py`: commitments 243 (seed 0) and 226 (seed 1) at the end, 0 with an `until`;
  `commitment.made` 95 and 82.
- **Falsifier and control.** Other tenure kinds do end in the same runs (`reside` 16 and 5, `hold` 3 and
  9, `contain` 42 and 46), so the reading sees an ending when one occurs.
- **Touches.** R-06 (ambitions), R-02 (consequence).
- **Minimal fix.** Decided at ladder step 5, as an amendment to `12_ARCS_arcs_as_staged_goals.md` (which
  gives a want stages and no end): the need-question for a commitment (`world_q.questions_for`, Q4) is
  not raised while the holder's OWN ledger reads the committed proposition's content as true, and the
  fold closes the tenure with a `commitment.kept` Event when his own act made it so; a want he believes
  met and that is not is then P4 at work. Abandonment is `release` on his own commitment, an ordinary
  candidate. `[UNVERIFIED: that `release` admits one's own commit today]`.

### F-PES-CHAR-08 · D · what is done to a man does not decide what he thinks of who did it

- **Claim.** A deed is judged by its kind against the judge's taste; only a killing or a wounding reads
  whom it was done to. And almost nothing hostile is done to anyone.
- **Evidence.** `person_q.py:128` (*"a deed's claim subject is read as its doer for every other kind"*);
  `_bond` applies to `PAIRED_KINDS` only. `b2_done_to_him.py` (seed 0, two seasons): 614 resolved acts
  name another person, 2 on a row that treats him as an opponent. The patient's regard for the actor
  moved in 289 of 612 (median 0.24, mean +0.15), against 16% of 6,703 control pairs (median 0.07); by
  verb, mean change in the patient's regard for the actor: `open_case` +0.54, `argue` +0.46,
  `challenge` +0.25, `lie` +0.18, `raze` +0.18, `sabotage` +0.16, `tend` +0.02, `give` −0.02. Most of
  these acts were refused, so the movement is the patient witnessing the actor's other deeds, not the
  act itself; the reading is that being targeted leaves no mark of its own. The largest move in any
  pair (12.9, above the largest authored stance of 10) is in a control pair `[cause not traced; H-339
  records unbounded stacking]`.
- **Falsifier and control.** If the patient mattered, `give` and `tend` would sit above `sabotage` and
  `lie`. They sit below.
- **Touches.** R-07.
- **Minimal fix.** Owner `person_q.deed_term`: read the patient for every deed kind whose row names a
  person subject, through the `_bond` that paired kinds already use (the judge who is the patient is
  his own full ally). An amendment to `02_CHAR_relations_have_a_ground.md`, which gives a relation its
  ground; not a new file.

### F-PES-CHAR-09 · D · no reason survives, and for half of what persons do there was none

- **Evidence.** §1.3 P5, §3.4.
- **Minimal fix.** The two reason-trail proposals stand; amendment: the stored reason names the deciding
  term as `harness/decision_spread.attribute_top` computes it (pursuit, stance or draw).

### F-PES-CHAR-10 · D · a realm of persons without wants is livelier than the shipped one

- **Evidence.** `d1_cuts.py`, arm `nopursuit`, seed 0, two seasons: stored stance moved for 7 persons
  (shipped 0), body for 13 (shipped 0), conviction for 1 (shipped 0); `march` rises from 13 acts
  (28th of the verbs) to 58 (5th); `commitment.made` falls 65 to 7 and `finding.made` 120 to 55. The
  `samemen` and `nostance` arms show the same direction (§2).
- **Reading.** The pursuit term steers persons toward records, utterances and commitments (the acts
  that always succeed) and away from the acts that touch another person's body or standing. Character,
  as tabled, is a pacifier. This is the person-level cause of `16_PESSIMIST_GAME.md`'s *correspondence
  about a world that does not move*.
- **Minimal fix.** Proposal B's signatures name `fight`, `raze`, `sabotage`, `arrest`, `capture` in what
  pursuits favour and oppose; no further edit here.

### F-PES-CHAR-11 · H · the most scarred man is the least changed

- **Evidence.** §2.2 R; `person_q.py:883` (`if not crisis or not heirs: return base`).
- **Minimal fix.** In `02_CHAR_scar_is_a_wound.md`'s scope: when every held pursuit is at the
  threshold, the shift is taken from the most-scarred toward the least-scarred, not skipped.

### F-PES-CHAR-12 · D · one man's paperwork scars the whole realm, and himself on `love` twenty times

- **Evidence.** `x2_alone.py 0 3 p_npc_020`: only the King's chooser returns acts. In three seasons he
  takes 43 acts (`create_record` 11, `research` 9, `revoke` 6 all refused, `issue` 4, `requisition`,
  `establish`, `open_case`, `convene`, `utter`, `commit`, `conceal`, one `sabotage` refused). At the
  end 83 of 83 persons carry a scar. His own counts: `liberty` 21, `love` 20, `individuality` 19,
  `justice` 19, `wealth` 15, `happiness` 14 (the actor witnesses his own act; `scar_excludes_actor`
  ships False).
- **Falsifier and control.** `x2_alone.py 0 3 nobody` (nobody acts): 0 of 83 scarred, and the same 37
  cohorts change body from hunger, so the scars are the one man's acts and nothing else.
- **Reading.** This is P3's *"because of what he does"* as built: what a man does marks him, and the
  mark for keeping records is a wound to love. It is F-PES-CHAR-01's table read through the scar.
- **Touches.** R-06, R-07.
- **Minimal fix.** Proposal B (the triggers) with `02_CHAR_scar_is_a_wound.md` (the floor and the
  outflow). No further edit.

## 5. False N-lines found

A false N-line is a part whose cut turns out free. Found, with the run that showed it:

| part | claimed necessity (the note that makes the claim) | the cut | verdict |
|---|---|---|---|
| the scar count and its crisis | how a person is changed by what he sees (`ED-IN-0261`'s scar model) | `noscar`: 0 of 1,529 acts differ in two seasons; from season three, 6 or 7 fixed conversions at 2 to 5% of choices | **free** as built |
| `Person.conviction` | *"faith as a pursuit is strongly modulated by religious conviction"* (`person_q.py:804`) | `noconviction`: a person's conduct moves 0.053; 83 of 83 still identified | **free, nearly** |
| believed-odds weighting and NPC effort | the person prices a contested act by his believed chance (CR-17) and may put effort behind it (CP-T01-05) | `noodds`: 0.012; 82 of 83 identified | **free**: almost no contested, priced candidate forms (46 `determine` and 151 unpriced `capture` readings at build) |
| the deontological refusal | *"deontology is a refusal"* (ED-IN-0261) | unarmed it executes nothing; armed it equals deleting five verb rows for everyone | **free** either way |
| capability / skill | *"capability supplies dice"* | every cast pool is the default; giving everyone the default changes nothing by construction | **free** (no holder to lose it) |
| attributes | CR-20 | ship off (first audit) | **free** |
| organization goals | orient their members' attention (I-4) | 5 of 749 resolved acts answer one (first audit); the `samemen` arm removes them with the pursuits and cannot separate the two | **nearly free** `[not separated here]` |

Mechanisms that survived only because nothing had been tried against them: the alignment table's
content against the pursuits' names (-01); the crisis's direction (-03); the refusal's scale and set
(-02); the deed judgement's blindness to the patient (-08).

N-lines that held under the cut: the pursuit term (for the realm's mix), the stance term (as
restraint), clause 4 (as foresight), the draw (as variety).

## 5A. The premises that failed, and the stories that can and cannot happen

**Premises** (§1.3): none of the six holds as worded. P1a, P2 and P4 are narrowed (a want is a
standing question; character is the pursuit vector and not the conviction; error is a stale count);
P1b fails in the moral sense and holds in the factual one; P3 and P5 fail; P6 is unreached.

**Stories a person can have in computed play today** (§3.1): a silent, pre-set conversion; a move of
house; a hungry population tended; a rare death in a capture that nobody answers; a slow drift in
regard toward whoever he has watched act. **Stories that cannot happen**: being persuaded (0 of 19
arguments succeeded); being changed by one's own judgement; learning a skill; gaining or losing a
seat; achieving or abandoning an ambition; being tempted and giving way; forming a tie; ageing;
being deceived to any effect; refusing on principle; avenging a wrong (the patient is not read).
**With this lane's three proposals and the ones they amend**: holding or losing a faith by fortune,
with witnesses; refusing what one holds wrong and being seen to pay for it; giving way; and characters
whose sheets say what they will do. The rest wait on other lanes' closers (seats, skills, ties, deceit).

## 6. Resolutions decided, and what is left for Jordan

| # | inconsistency, gap or unclear passage | resolution | ladder step | carried by |
|---|---|---|---|---|
| 1 | what a pursuit's name must mean in acts is stated nowhere code reads | signatures in `rosters.yaml`, read through `pursuit_lean`; cells repaired against them | 3 (basis ruled) then 5 | proposal B |
| 2 | 25 resolvable verbs carry no alignment cell | rows for the nine a signature names first | 5 | proposal B, step 2 |
| 3 | which creed a shared-column crisis takes (`[ASSUMPTION]` at `person_q.py:912`) | the lowest-held, not the highest | 5 | proposal A, item 1 |
| 4 | RESTABILISE is unbuilt, so 14 cast are immune | the Failure band's third arm (intensity −2) | 5 | proposal A, item 3 |
| 5 | `conviction.moved` declared, never emitted | emitted once per person in crisis | 4 (every other state write emits) | proposal A, item 4 |
| 6 | the refusal's *"certain actions"* is no set | `pursuit_axes.refusable`, a closed list | 3 (ED-IN-0261's words) | proposal C, item 1 |
| 7 | the refusal compares two scales | the axis's share of the projected vector | 5 | proposal C, item 2 |
| 8 | a refusal leaves no trace | `Scene.forgone`; `scruple.overridden` | 5 | proposal C, item 5 |
| 9 | the stance term's class gap is hundreds of temperatures | regard as a share of `STANCE_MAX` behind a fixture | 5 | amendment to `02_CHAR_scar_cap_and_regard_unit.md` |
| 10 | a commitment has no end | closed when the holder's own ledger reads it met | 5 | amendment to `12_ARCS_arcs_as_staged_goals.md` |
| 11 | a non-paired deed ignores its patient | `_bond` for every person-subject deed kind | 4 (paired kinds' precedent) | amendment to `02_CHAR_relations_have_a_ground.md` |
| 12 | a fully scarred person is unshifted | shift toward the least-scarred | 5 | amendment to `02_CHAR_scar_is_a_wound.md` |

**For Jordan (two, each a ruled item meeting the standing rule; both proposals name them):**

1. **The crisis rolls or it does not.** `ED-IN-0261`'s superseding row folds G-Q6 (*"rolls nothing"*)
   into the build. Option A keeps the rule (the realm's faith changes on a schedule fixed at world-gen);
   option B draws (it changes by fortune, and a man can hold).
2. **The scruple is a line or a tendency.** `ED-IN-0261` words it as a threshold. Option A keeps the
   threshold (knowable characters); option B draws (temptation, and giving way as an event).

## 7. Evidence log

All `PYTHONHASHSEED=0`; scripts in the scratchpad folder named in the head.

| probe | world | what it read | outcome |
|---|---|---|---|
| `a0_words.py` | none (tables only) | per pursuit: top and bottom verbs by lean, violated set; per creed: violating verbs | §4 -01; 25 of 66 verbs uncelled |
| `a1_norms.py` | none | alignment row norms; the same reading with unit rows | loudest rows top 7 of 15; unit rows do not repair |
| `a2_sig.py` | none | the proposed signatures against today's lean | 2 of 15 hold, 35 breaks |
| `c1_two_men.py 0` | `build_realm(0)`, no season | conviction swap; test-retest; single-pursuit holders | §2.3, §4 -01, -04 |
| `c2_stopped.py 0` | `build_realm(0)`, no season | the refusal gate, shipped and armed | §4 -02 |
| `c3_skill.py 0` | `build_realm(0)`, no season | pools over the cast; believed against true odds | §4 -05, -06 |
| `c3b_curve.py 0` | `build_realm(0)`, PROXY acts | P(Success or better) by actor's and subject's key | §4 -05 |
| `x1_extremes.py 0` | `build_realm(0)`, no season | the crisis branch per person from the build; the chooser at ten extremes | §2.2, §3.3, §4 -03 |
| `b1_season.py 0 3` | seed 0, three seasons | interior per season; records; commitments; belief against world | hashes `5ab73af2`, `bacd687f`, `52ff67bc`; acts 749, 780, 838 |
| `b1_season.py 1 3` | seed 1, three seasons | the same, plus degrees by verb and the crisis triggers | hashes `aa58ef0b`, `8aae8412`, `26d2091b`; acts 731, 788, 871 |
| `b2_done_to_him.py 0 2` | seed 0, two seasons | patient's regard for the actor against control pairs; scene occasions | hash `bacd687f`; §4 -08 |
| `d1_cuts.py 0 2 <arm>` | seed 0, two seasons, ten arms | §2's table | shipped arm `5ab73af2`, `bacd687f`; `drawseed` `dfc6d534`, `671cd84f`; `noscar` `b8a16d9c`, `17e98525` |
| `x2_alone.py 0 3 p_npc_020` / `nobody` | seed 0, three seasons, one chooser live / none | a lone actor; the scars one man's acts leave; the null control | §3.5, §4 -12 |
| `d1_read.py` | the arms' outputs and `b1`'s | distances, identification, cross-seed identity | §2, §3.3 |

Not run: `pytest`; any `aperture`, `strife`, `storybar` or `corpus_run` pass (other lanes ran them; cited
through their audits); realm-level extremes (§3.5). `git status --short` at the end shows this lane's four
files and nothing else of its making.
