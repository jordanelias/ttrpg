# GAME — pessimist audit: NERS, premise and emergent narrative, of the game as a whole

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 4995824 (working tree)

Scope: the whole game as a suite of engines, the season loop and every seam, the nine requirements, the
provided arcs and characters taken together, and the premise that this is a dynamic emergent-narrative
game with no GM. Subsystem audits (`01`–`12`, `14`, `15`) are cited, not redone. Everything measured here
is new work unless a lane is named. All runs: `PYTHONHASHSEED=0`, `harness/populated.py::build_realm`,
the shipped chooser, no player, no hand-built act unless the row says PROXY. Scripts and outputs:
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/PES_GAME/`.

## 0. Verdict

**The game, run as a whole with no player, is one working engine and six attachments: persons read the
world's clocks and each other's paper and answer with more paper, and nothing they do changes who lives,
who rules, what stands or what is in the granary.** Three seasons of the shipped realm at seeds 0, 1 and
2 against a control in which nobody acts at all (X1): the acting realm ends with the same persons, the
same holder in every one of the 34 seats, the same condition on every one of the 322 sites, the same
rungs and (to within a few units of grain) the same stores as the realm in which no person did anything;
the one exception in nine seed-seasons is a cardinal killed in a `capture` at seed 1, whose seat nobody
then fills and whose death no other person's executed act answers. What the acting realm adds is 357
records, 199 propositions, 95 commitments, 42 duties, a docket of 18 and a ledger for everyone. Every
executed act that answers another person's act lands in the information verbs (`create_record`, `utter`,
`reconstruct`, `research`, `surveil`), the docket verbs (`petition`, `convene`) or the emission-only
governance verbs (`issue`, `dispatch`, `commit`); the columns for personal combat, mass battle,
settlement and character development are empty (§1.2). The single largest obstacle is therefore not in
any one subsystem and no subsystem lane can see it from inside: **the verbs that move the world's
skeleton (kill, seat, unseat, build, raze, found, trade, starve, win a field) are refused or unformed in
computed play, so every seam that would carry a consequence from one engine into another carries
nothing, and the "emergent narrative" the instruments count is a correspondence about a world that does
not move.**

**On the standing rule (*we do not do deterministic*):** in computed play the game is overwhelmingly a
fixed function of state. Of 2,630 acts attempted in three seasons at seed 0, 206 (7.8%) were resolved by
a draw; at seed 1, 286 of 2,646 (10.8%). Ten verbs succeed every time they are admitted with no roll
(894 acts at seed 0: `create_record`, `utter`, `reconstruct`, `commit`, `interview`, `conceal`,
`petition`, `convene`, `dispatch`, `thread_read`); eighteen are refused every time (569 acts); thirteen
are decided by admission alone (732 acts). The world's own motion ships with its draws off: every site
wears by the same step, every settlement yields the same quantities, every cohort starves by the same 60
in season 0 and never again, and nobody can die of age or illness (`age_step` and `illness_rate` ship at
0). §5 ranks the fixed outcomes.

The steelman is owed and holds where it was tried: the kernel is honest (one clock, one gate, causes on
every Event, seeded replay), every refusal is visible and keyed, nothing is scripted, and the lanes'
proposals between them name most of the missing closing verbs. The pessimist reading is about the sum:
the lanes each report "my engine idles because another lane's occasions are missing", and the sum of
those sentences is a ring with no entry.

## 1. NERS — cut tests on the engines and on the seams, executed

Method (`skills/ners/SKILL.md`; definitions `CLAUDE.md` §0.06): propose the cut, name what dies. At game
scale the cut is executable two ways, and both were run: **(a) the null arm** — cut every person's
agency (a chooser that returns no act; MATTER and CALENDAR run) and diff the world's state, component by
component, against the shipped arm on the same built world; **(b) the ancestry reading** — in the
shipped arm's own log, for every act-caused Event, which other person's Event stands in its `causes[]`,
and which engine emitted each end. A cut is free when nothing that is not the cut thing's own bookkeeping
differs or descends.

### 1.1 X1 — who moves the world (the game-level cut of all agency)

`x1_world.py SEED 3`, seeds 0, 1, 2. Components of state compared: persons; body; scar; stance;
pursuits; conviction; capability; attributes; ledger sizes; live `hold` edges on offices; `hold` edges
on other things (records, propositions); persons' and rungs' `contain` edges; live tenure kinds; site
conditions; stores; rungs; offices; record kinds; proposition, docket and date counts.

| component | NULL (nobody acts) vs BUILD | PLAY vs NULL, seed 0 | PLAY vs NULL, seed 1 |
|---|---|---|---|
| persons | same | **same** | 1 fewer (a cardinal, killed in a `capture`) |
| seats (`hold` on an office) | same | **same, 34 of 34** | the dead man's seat is empty; 33 others same |
| site condition (322) | 74 worn | **same** | **same** |
| rungs (414) | same | **same** | the dead man's person rung |
| stores | filled by yield | 2 settlements differ by 1 grain | 3 differ by a few units |
| body | 37 cohorts 1000 → 940 | the 37 cohorts tended back to 1000 | same shape |
| stance | same | 1 person of 83 | 3 of 83 |
| pursuits | same | 2 of 83 | 1 of 83 |
| conviction | same | 6 of 83 | 8 of 83 |
| scar | same | 83 of 83 (CHAR: the counter runs past its ladder) | 83 of 83 |
| residence | same | 7 persons moved | 8 |
| offices | same | +1 (`off_lord_terr_T1` established, unheld) | same |
| records | same | +357 text, 69 faction sheets, 34 covers, 29 dispensations, 28 petitions | same shape |
| commitments / duties | same | `commit` 148 → 243, `oblige` 4 → 46 | same shape |
| propositions, docket, dates | same | 70 → 269; 0 → 18; 0 → 17 | 70 → 280; 0 → 21; 0 → 15 |

Reading. The realm's material and political skeleton at the end of three played seasons is the build
plus the clocks. What persons add is paper, promises, a docket and memory; what they change in each
other is close to nothing (stance 1 to 3 persons of 83; CHAR measured 0 of 83 over two seasons). The SE
lane's `probe_noacts` and `probe_play` runs show the same for stores over four seasons and are cited for
that; the seat, site and rung rows are new here.

Control for the instrument: the projection does see change when change happens (the NULL arm's wear,
yield and hunger rows; the seed-1 death; the established office), so "same" is an observation and not a
blind reader. Seed 2 reads as seed 1, and with the same death: at both seeds the one person who dies is
the same cardinal (`p_npc_013`, `off_cardinal_prudence`), felled in a `capture`.

### 1.2 The seam matrix — which engine's Events does another engine's act answer

Read off the shipped arm's log (`pes.py::seam_edges`): one edge per (answering act, antecedent Event)
where the antecedent Event sits in the `causes[]` of an Event the act caused and was caused by ANOTHER
person's act (row `WORLD`: by no act, a clock). Rows: the engine of the antecedent act; columns: the
engine of the answering act. The verb → engine map is this lane's reading `[ASSUMPTION]` (no typed
column owns it; it is in `pes.py`). Cells: answering acts that were NOT refused, three seasons.

| antecedent ↓ / answer → | PC | MB | SC | FA | SE | FI | CHAR |
|---|---|---|---|---|---|---|---|
| WORLD (clocks), seed 0 / 1 / 2 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/1 | 9/9/7 | **221/226/236** | 0/0/0 |
| PC | 0/0/0 | 0/0/0 | 0/1/0 | 0/1/2 | 0/1/0 | 2/19/5 | 0/0/0 |
| MB | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/1/4 | 0/0/0 |
| SC | 0/1/1 | 0/0/0 | 5/5/12 | 5/2/0 | 0/1/1 | 37/27/46 | 0/0/0 |
| FA | 0/1/2 | 0/0/0 | 15/16/10 | 11/11/22 | 0/0/1 | 67/54/76 | 0/0/0 |
| SE | 0/0/0 | 0/0/0 | 2/3/4 | 5/0/4 | 0/2/2 | 26/19/32 | 0/0/0 |
| FI | 0/1/0 | 0/0/0 | 5/10/6 | 9/6/11 | 2/4/2 | 69/67/49 | 0/0/0 |
| CHAR | 0/0/1 | 0/0/0 | 1/1/1 | 7/0/2 | 1/0/0 | 14/18/5 | 0/0/0 |

Reading, by column (what an engine is ever moved to do by someone else):

- **MB is answered by nothing and answers nothing.** No executed march in nine seed-seasons has another
  person's Event among its causes; a `field.lost`, `field.unopposed` or `army.arrived` Event is among the
  causes of no other person's executed act at seeds 0 and 1 and of four information acts at seed 2.
- **PC answers nothing.** The handful of PC-column edges are `capture` scenes at seeds 1 and 2; `fight`
  never forms, `challenge` is refused 393 of 393 and `accept` 128 of 128 over the three runs.
- **CHAR answers nothing.** `train` is refused 324 of 324; `tend` executes only as a cohort mending itself.
- **SE answers almost nothing** (a `move` after a store report); `exchange` 0 of 225, `build`/`found`/
  `raze`/`sabotage` 0 of every attempt.
- **Everything that is answered is answered in writing.** The FI column holds 80% of executed
  cross-person answers at every seed, and its largest source is not a person: `stores.changed`,
  `yield.taken` and `term.matured` (clock Events) answered by `create_record` and `utter`. The top
  executed pairs at seed 0: `stores.changed → create_record` 29, `yield.taken → create_record` 25,
  `yield.taken → utter` 21, `term.matured → research` 21, `term.matured → create_record` 20.

So the cross-person chains the story bar counts (WR: cross share 25%, depth to 21) are, by content,
persons recording that the granary filled and that a term matured. The WR lane found the deepest
consequence chain to be one concealment answered by three records; this is why.

**Event kinds emitted and never among the causes of another person's executed act** (seed 0 / 1 / 2,
emitted counts): `person.died` (– / 1 / 1), `field.lost` (1 / 1 / 3), `field.unopposed` (3 / 5 / 6),
`army.arrived`, `march.declared` (29 at seed 0), `news.told` (10 / 9 / –), `body.changed` (37 / 39 / 41),
`residence.changed`, `travel.moved`, `record.given`, `petition.carried`, `faction.surveyed`,
`office.established`, `finding.none`, `condition.worn` (966). A death, a lost battle, a told rumour and a
hungry town are each a terminal: they are logged, witnessed, remembered, and answered by nobody.

### 1.3 The determinism census — how much of the game is a draw

Jordan's standing rule (`AUDIT_BRIEF.md`, "WE DO NOT DO DETERMINISTIC"): a thing that could go either
way for the people in the fiction goes by a draw. Read two ways.

**By running** (`pes.py::outcome_census` over the X1 shipped arms; an act's outcome signature is the set
of non-claim Event kinds it caused plus its degree; "by a draw" = the signature carries a degree other
than a bare `Declared`):

| | seed 0 | seed 1 | seed 2 |
|---|---|---|---|
| acts attempted, 3 seasons | 2,630 | 2,646 | 2,664 |
| not refused | 1,394 (53%) | 1,498 (57%) | 1,525 (57%) |
| **resolved by a draw** | **206 (7.8%)** | **286 (10.8%)** | **225 (8.4%)** |
| verbs that ever drew | 7 | 9 | 8 |
| verbs that succeeded every time, no draw | 10 (894 acts) | 10 (967) | 9 (990) |
| verbs refused every time | 18 (569 acts) | 15 (549) | 17 (528) |
| verbs split by admission alone, no draw | 13 (732 acts) | 13 (612) | 14 (704) |

The draws that do occur are `research` (always drawn), `surveil` (drawn in under half its acts), `tell`,
`lie`, `argue`, `speak`, `capture`, `determine` and a fought `march`. Of the ~15% of executed acts that
draw, about 60% are `research`, a solitary act whose finding nobody but the researcher reads (FI audit).
**Excluding `research`, a draw decides 3% of what is attempted** (78 of 2,630 at seed 0).

**By reading** (`engine/season/data/verbs.py::VerbRow.contests`; `VERB_TABLE`): 11 of 67 rows declare
`contests:` (`accept`, `argue`, `arrest`, `capture`, `determine`, `fight`, `interrogate`, `lie`, `march`,
`speak`, `tell`); the six fieldwork verbs draw through the `inquiry` role; the other 50 rows, once
admitted, write their effect with certainty. Among those 50 are acts that in the fiction could plainly go
either way: `forge` (a forgery is made, always, at the forger's fixed quality), `conceal`, `sabotage`,
`seize`, `raze`, `requisition`, `migrate`, `exchange`, `recruit`, `found`, `build`, `restore`, `train`,
`tend`, `oblige`, `covenant`, `comply`/`defy`, `succeed`, `confer`, `revoke`, `pardon`, `release`,
`convene`, `issue`, `dispatch`. §5 ranks them with the world-clock cases.

**The engine's own draw sites, all of them** (grep over `engine/season/` outside `tests/` and `harness/`
for `.random()`, `.choice(`, `draw_factory(`, `roll_`): the chooser's sampled order
(`decision/choose.py::_sample_order`, `choice_temperature` 0.05); intent disclosure
(`choose.py::declare_intents`, `intent_disclosure` **0.0**); the bodies hazard (`loop/matter.py`,
`illness_rate` **0.0**, `age_step` **0.0**); the two rolls of the fold (`loop/resolve.py`, the contest and
the graded act, at `pool_default` 2 against `obstacle_default` 2 for everyone: DICE audit); confiding
(`loop/witness.py`, `telling_privacy` **0.0**); the season factor (`queries/world_q.py`,
`season_factor_draw` **()**, the control); the believed-odds estimate (`seam/wrappers/_estimate.py`).
Seven sites; four ship switched off. Shipped, the season engine's chance is one shuffle of what a
person tries and one two-dice roll on a tenth of what they try. (Read with `build_realm(0).fixtures.get`.)

### 1.4 False N-lines and unexamined survivors, at game scale

A false N-line is a claim that a thing is necessary which a cut shows to be free. Graded on what X1 and
§1.2 observed, not on design text.

| claimed necessary | the cut | what died (computed play, 3 seeds × 3 seasons) | verdict |
|---|---|---|---|
| the personal-combat seam in the season (`fight`, `accept`, `challenge`) | remove the three rows | nothing: 0 executed of 521 attempts; no Event of theirs is anyone's cause | **false N-line today**; true on paper (PC audit: "a module with almost no customers") |
| the mass-battle seam (`march` → field) | remove `march` | 1, 1 and 3 `field.lost`, 14 `field.unopposed`, no territory changed hands, no Event answered | **false N-line today** |
| `train` (character development) | remove the row | nothing: 324 refusals | false N-line today |
| the settlement verbs (`build`, `found`, `raze`, `sabotage`, `exchange`, `work`, `restore`) | remove them | nothing but refusals; site condition and stores identical with and without persons | false N-line today |
| compliance (`comply`, `evade / defy`) | remove both | nothing: `compliance.impossible` 137 of 137 + 21 of 21 | false N-line today (FA audit: decrees are emission-only) |
| the named individuals (46 cast persons) | `build_realm(0, cap=0)`: 37 cohorts, no individual, no office (X5) | the loop runs; 1,049 acts in three seasons against 2,630 with the cast; sites, stores and bodies end the same | the cast is necessary to the *paper*, not to the *world* |
| persons at all | the NULL arm | paper, promises, the docket, memory; no seat, site, rung or (bar one) life | the world does not need its people |
| memory decay as logged Events | drop `claim.decayed` from the log | nothing reads it as a cause in any seam cell above; it is 65% of the log at six seasons (WR run, seed 0: 179,056 of 273,067) | false N-line as an *Event*; the fade itself is needed (CORE F-CORE-01, WR F-WR-09 own the fix) |

**Survivors nobody attacked.** Mechanisms that stand because nothing has been tried against them, with
the attack run here:

- *"Seasons tick scene by scene so one scene can change the next"* (R-03, `met`). Holds for paper; the
  attack "does a mid-season death, verdict or battle change a later scene the same season" cannot be run:
  the antecedents do not occur. R-03 is met on a channel through which nothing consequential flows.
- *"Decisions propagate"* (R-01, `met`). The player-king abstaining for three seasons (X4) changes the
  executed verbs of 59 of 82 other persons and the state of none: one unheld office is not established,
  42 duties are not taken, one person's stance row is not written. Propagation is real and is confined to
  paper. R-01 as worded is met; R-01 as meant (consequence) is not shown.
- *"Characters matter"*: reach (X4, seed 0, three seasons): of 83 persons, **48 have no executed act by
  anyone else anywhere downstream of anything they did**; median reach 0; the 37 cohorts' mean reach 0.6;
  seat-holders' 18.2; the maximum 80.

### 1.5 E and S at game scale

- **E, scored last, as a ratio.** What N and R found is one working loop (information → paper → docket)
  and an honest kernel. Against it: 67 verb rows of which 23 to 30 ever execute in the realm; six
  registered engines of which one is reached by other persons' acts; a combat module (~6,000 lines, PC
  audit), a mass-battle module and a second social-contest kernel (~6,700 lines, SC audit) that computed
  play does not enter or enters a handful of times. The overhead is not in the kernel (CORE: ~14,000
  executable lines); it is that the player cannot *intuit complex outcomes from simple choices* because
  nine in ten choices have a fixed outcome and half are refused. E fails on legibility, not on tidiness.
- **S, the two tests the shorthand drops.** *Pauses correctly*: untestable at game scale in computed play
  (no duel, no fought field of consequence, no hearing that ends: SC audit). *Calculations consistent in
  methodology*: three rollers for one quantity (DICE audit); body on a person, a cohort and a unit by
  three rules (MB audit: `hp / 100` handed to the season as a survivor ratio); and, new here, **two
  rules for whether an outcome is a draw at all**: 11 verbs contest, 6 grade, 50 are certain, and which
  is which follows the history of the build and no stated principle (`forge` certain, `lie` drawn;
  `seize` certain, `capture` drawn; `succeed` certain, `argue` drawn).

## 2. Premise audit — the game's own sentences

Method (`skills/premise-check/SKILL.md`): the ordinary account (O) written first; the notes' account (N)
taken from the lanes' audits and the rows they cite; the code's account (C) by a run with a control.
Depths: EXECUTES (a hand-built act), FORMS (the chooser offers it), FIRES (it appears in a seeded season
with no hand in it). Each premise below is run at FIRES in the shipped realm, with the missing antecedent
planted as a labelled PROXY where the realm never produces it.

### 2.1 "An officeholder dies and the others react" — holds to the death, then breaks at "the others"

Run: `x2_death.py 0 1 3`, `x2b_death_detail.py 0 1 4 p_npc_020` and `… p_npc_020,p_npc_031`. One played
season, then the King (Almud Almqvist, `off_king` and `off_duke_valorsmark`) dies at the next MATTER
through the engine's own writer (`loop/matter.py::_die`). PROXY: his `born` is set so the bodies hazard
is 1; `age_step` 1e-9 in both arms. CONTROL: same sweep, nobody dies; its hash equals the shipped
four-season realm's (`abbde715aa0e`), so the sweep itself moved nothing.

| # | link | O (ordinary) | C (observed) | verdict · cause |
|---|---|---|---|---|
| 1 | he can die | of age, illness, violence, accident | of nothing, shipped: both hazard rates are 0, `fight` never forms; nine seed-seasons give one death, the same cardinal at seeds 1 and 2 | **INERT at FIRES** · BEHAVIOUR (the control is the shipped value) |
| 2 | the death is an event with a trace | one Event, his seats close | `person.died` (causes `[ROOT]`), `tenure.closed` naming both seats | FOLLOWS (PROXY) |
| 3 | "the others": who learns | the court at once, the realm within a season | 16 of 82 the season he dies; **17 of 82 three seasons later** | **DEPARTS** · BEHAVIOUR: news does not travel (FI audit: almost nothing is told) |
| 4 | the seat is filled | an heir claims; rivals may contest; an interregnum has a cost | the Prince's `succeed`, once, the season after: no rival, no roll, no refusal possible once admitted. `succession.claimed`'s `causes[]` is his own act alone: the log does not say he claimed *because* the King died | FOLLOWS for the throne · **fixed outcome** (standing rule) · E10 DEPARTS (reason unreadable) |
| 5 | his other seats | pass by the same or another rule | `off_duke_valorsmark` vacant to the end of the run; the heir's own seat (`off_heir`) vacant to the end; 43 `confer` attempts refused in three seasons (the Confessor conferring the duchy and then the crown on cardinals; a duke conferring the crown on a settlement's cohort) | **DEPARTS** · BEHAVIOUR: no seat but the throne has a route to a new holder |
| 6 | the others react | grief, opportunism, realignment, a challenge, a petition | 19 acts by 8 persons descend from the death by `causes[]` in three seasons; 8 executed: four records, a dispatch, a forgery, a transfer, a research. No stance row moved because of it; no faction changed head but the Crown | **DEPARTS** · COMPOSITION |
| 7 | the world shows it | fewer decrees, a new King's acts | untraced aggregate: `dispensation.issued` 25 → 6, `duty.taken` 46 → 105, `march.declared` 34 → 58. Not traceable through `causes[]` to the death, so reported as difference, not effect | AMBIGUOUS |
| 8 | no heir (King and Prince both die) | a succession crisis: claimants, a regency, a war | the throne, the duchy and the heir's seat stay vacant for all four seasons; 7, 5, 24 … `confer` attempts refused; nobody seizes, nobody is elected, the Queen's seat ("Widow Regent if Almud eliminated", by its post string) does nothing; the realm's other counts are unremarkable | **INERT** · the realm does not notice it has no King |

Play-back, as a player would tell it: *the King died in his bed. A dozen people in the room knew. The
Prince took the crown the next season without anyone saying a word; the duchy the King also held was
left empty and a confessor spent a year trying to hand it to a cardinal. Three seasons on, four in five
of his subjects had not heard.* Set beside the premise: the death is real, "the others" are sixteen
people, and "react" is four records.

Opposite-failure test (an outcome that should vary and does not): the succession. One claimant, one
attempt, certain success, at every run in which the heir lives; with the heir dead, certain vacancy.
Neither arm has a spread.

### 2.2 "A decree binds" — does not hold (FA audit, cited; one game-level addition)

FA measured it: 91 decrees issued over nine seed-seasons, none held, obeyed or defied by an addressee
(`06_FA_audit.md` §0; proposal `06_FA_decree_binds.md`). X1 adds the game-level reading: `comply` and
`evade / defy` are formed 137 and 21 times over three seeds and end in `compliance.impossible` every
time; `dispensation.issued` is answered by 24 executed acts at seed 0, every one of them a record, an
utterance or a reconstruction *about* the decree. A decree is a topic.

⚠ **Standing rule, applied to this lane's own sentence and to the FA proposal's title:** "a decree
binds" must not be repaired into a fixed effect. The repaired premise is "a decree is *answered*:
each addressee's compliance is a draw whose odds the issuer's standing, the addressee's stance and the
cost of obeying set; defiance is visible to the issuer". Listed for the FA lane in §7.

### 2.3 "A rumour spreads and someone acts on it" — does not hold

FI measured the first half: between 0 and 7 of 10,000 to 12,000 held claims arrived by a person telling
another; no claim was retold (`08_FI_audit.md` §0). X1 adds the second half: `tell` and `lie` are
refused 81 of 102 times at seed 0 (`tell.refused`), 12 tellings land (`news.told` 10), and **no
`news.told` Event is among the causes of any other person's executed act at seeds 0 or 1** (10 and 9
emitted). A told thing is held and nothing is done with it. Opposite failure: what *is* drawn here (the
`tell` roll, three bands) has spread; what it gates has no consequence, so the spread is decoration.

### 2.4 "A town starves and someone is blamed"
