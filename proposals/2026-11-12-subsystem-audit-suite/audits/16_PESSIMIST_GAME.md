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
the one exception in nine seed-seasons is a cardinal killed in a `capture`, the same man at seeds 1 and
2, whose seat nobody then fills and whose death no other person's executed act answers. What the acting realm adds is 357
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
- **Everything that is answered is answered in writing.** The FI column holds 85%, 85% and 83% of the
  executed answers (436 of 513, 431 of 507, 453 of 545), and its largest source is not a person: `stores.changed`,
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
| 1 | he can die | of age, illness, violence, accident | of nothing, shipped: both hazard rates are 0, `fight` never forms; nine seed-seasons give two deaths, one each at seeds 1 and 2, the same cardinal in a `capture` | **INERT at FIRES** · BEHAVIOUR (the control is the shipped value) |
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
refused 81 of 102 times at seed 0 (`tell.refused`), 11 fail the roll (`news.untold`), 10 land
(`news.told`), and **no
`news.told` Event is among the causes of any other person's executed act at seeds 0 or 1** (10 and 9
emitted). A told thing is held and nothing is done with it. Opposite failure: what *is* drawn here (the
`tell` roll, three bands) has spread; what it gates has no consequence, so the spread is decoration.

**A correction this lane owes its own instrument.** The 19 descendant acts in link 6 are counted through
`causes[]`. The succession and the 43 `confer` attempts are *also* answers to the death and are not
among them: an act formed on a standing occasion (a vacancy, a writ held, a wounded person, a detainee)
is folded with no occasion id by design (`loop/resolve.py::_occasion_ids`, the Batch B-I close F1), so
the log holds no edge from the death to the claim. The reaction is therefore larger than `causes[]`
shows, and the log cannot show it: F-PES-GAME-03, proposal
`16_PESSIMIST_GAME_standing_occasions_carry_their_cause.md`. The same blindness bounds §1.2: its blank
columns are confirmed blank by the verb census (nothing executed there), not by the matrix alone.

### 2.4 "A town starves and someone is blamed" — does not hold; "starves" itself is unreachable

O (ordinary): a granary empties; the town goes hungry within the season; people sicken, leave or die at
different rates; those responsible for it (the lord, the steward) hear of it; someone petitions,
requisitions, flees, riots, or accuses; a town can die.

| # | link | C (observed) | verdict · cause |
|---|---|---|---|
| 1 | a granary can empty | no: every settlement yields about 21 times what it eats, every season, and nothing spends stores (SE audit; X1: stores equal in PLAY and NULL to within a few units) | **INERT at FIRES** |
| 2 | the town goes hungry | PROXY (stores emptied and producing Sites zeroed before each season, `x3_famine.py`). Every short cohort loses exactly 60 body a season | FOLLOWS (PROXY) · **fixed outcome** |
| 3 | at different rates | no: 37 of 37 cohorts read 940, 880, … 40 in step | **DEPARTS** · EDGE |
| 4 | a town can die | yes, in its seventeenth hungry season (four years and a quarter), and with nobody acting all 37 die in that one season | DEPARTS on pace (E6) · the standing rule |
| 5 | the hungry do something about it | in play the cohort `tend`s itself: X1, every seed: the 37 cohorts that lost 60 in season 0 are all back at 1000 by the end of that season (`body.tended` 37). `tend` restores a body whole in one act, with no roll, no food and no cost (`loop/effects_combat.py::_eff_tend`) | **INVERTED** in effect: rest cures starvation · COMPOSITION (hole row H-304; sweep D-05) |
| 6 | those above hear of it | `body.changed` is among the causes of no other person's executed act at any seed (37, 39, 41 emitted) | **INERT** |
| 7 | someone is blamed | no verb names blame; no stance row moves on a shortfall; `person_q.stability` reads 0 for every settlement (hole register, the unrest row) | **ASSERTED** — no code owns it |
| 8 | the extreme: every town dies | the 46 individuals remain, untouched, and the loop runs on: only a cohort eats (RULED, ED-IN-0255, not re-raised). A realm with no people keeps all its lords, seats and stores | EDGE — §7 item J-1 |

Play-back: *the granary was empty. The town lost a sixteenth of itself, rested, and was whole again by
autumn. This happened every season. Nobody above them heard.*

### 2.5 "A player's choice changes what happens" — holds for paper, not for the world

Run: `x4_player.py 0 3`, the player seated as the King through `harness/play_surface.py::dispatching_chooser`
(the shipped single-player hook). Arms: AUTO (the shipped chooser decides for him; hash equals the plain
run), ABSTAIN (he does nothing for three seasons), LAST (he plays only the last scene the chooser would
have played).

| | AUTO | ABSTAIN | LAST |
|---|---|---|---|
| the King's executed acts | 24 | 0 | 11 |
| persons, seats, sites, rungs, stores | — | **same** | **same** |
| offices | 35 | 34 (`off_lord_terr_T1` never established) | 34 |
| `duty.taken` / `duty.refused` in the realm | 42 / 69 | **0 / 0** | 0 / 0 |
| stance rows that differ | — | 1 person | 1 person |
| other persons whose executed verbs differ | — | 59 of 82 | 62 of 82 |

The most powerful person in the realm ceasing to act for most of a year costs the realm one unheld
office and every sworn duty (all `oblige` traffic at seed 0 descends from him), and reshuffles what 59
other people write. Nothing else. Genre test (would a strategy player be surprised): yes — a king who
does nothing for three seasons loses nothing and nobody moves against him.

### 2.6 The premises that failed, in one list

| premise | first broken link | cause |
|---|---|---|
| an officeholder dies and the others react | "dies" is unreachable shipped; with the death planted, "the others" is 16 people and "react" is the heir alone | hazards ship at 0; news does not travel; one seat has a route |
| a decree binds | "the addressee answers" (FA) | emission-only; `comply` impossible 137 of 137 |
| a rumour spreads and someone acts on it | "spreads" (FI); "acts on it": 0 of 19 tellings answered | telling refused four in five; a told claim occasions nothing |
| a town starves and someone is blamed | "starves" is unreachable; planted, rest cures it; nobody above hears | no scarcity; `tend` free and whole; no blame verb |
| a player's choice changes what happens | "what happens" beyond paper | the skeleton does not respond to anyone |
| a war is fought and land changes hands | (MB, FA) no two factions at war; no fought field of consequence; no rung changes holder | cited: `04_MB_audit.md`, `06_FA_audit.md` |
| a trial reaches a verdict | (SC) 0 to 1 `matter.determined` per three seasons; 8 lapsed at season 5 (WR run) | cited: `05_SC_audit.md` |

## 3. Emergent-narrative audit — no player, several seeds and seasons

Sources: X1 (seeds 0, 1, 2 × 3 seasons, this lane); the WR lane's six-season runs at seeds 0, 1, 2
(`runs/WR/probe_s*_k6.txt`, cited); X2 to X6 (this lane).

### 3.1 What stories can this game produce at all (enumerated from the code that executes, not the docs)

A story needs a closing Event that changes state. The closing kinds the verb table and MATTER can emit
and that some run here or in a lane has seen executed: `person.died` (a `capture` felling; a cohort's
seventeenth hungry season; never age or illness, shipped), `succession.claimed`, `tenure.closed` (a
death; a `release`), `matter.determined` and `matter.lapsed`, `field.lost` / `field.unopposed`,
`residence.changed`, `office.established`, `record.forged`, `cover.assumed`, `commitment.made`,
`duty.taken`. No ending row of `world_q.endings_reached` has fired in any run of any lane.

### 3.2 Which it does produce, in computed play (counts: seed 0, three seasons, unless said)

| the story | beginning | escalation | reversal / cost | ending | n |
|---|---|---|---|---|---|
| **the clerk** — the granary fills and someone writes it down | a clock Event | another writes about the writing | none | none | `create_record` 350, `utter` 199; 230 answers to clock Events |
| **the petition that lapses** | `petition.filed` 28 | `docket.formed` 17, `date.fired` 12 | `speak`: 4 turned, 1 held; `speech.unheard` 23 | `matter.lapsed` (8 at season 5, WR); `matter.determined` 1 in six seasons | 28 |
| **the forger nobody catches** | `record.forged` 52 | none | none: one fixed quality, no exposure answered | none | 52 |
| **the cover** | `cover.assumed` 34 | none | none | none | 34 |
| **the march that meets nobody** | `march.declared` 29 | 25 refused; 3 `field.unopposed` | 1 `field.lost` | nothing changes hands | 29 |
| **the oath** | `commitment.made` 95; `duty.taken` 42 | none | `duty.refused` 69 | terms mature (`term.matured` 542), answered by records | 137 |
| **the arrested cardinal** (seeds 1 and 2 only) | a `capture` on the same man | wounded | felled; his seat closes | nobody fills it, nobody answers | 1 per seed |
| **the move** | `residence.changed` 16 | none | none | none | 16 |

Every row but the cardinal's lacks a reversal with a cost and an ending that is not a stop. The
cardinal's is the realm's one complete story and it is the same story at both seeds that have it.

### 3.3 Dead ends (a story that begins and cannot continue), by the verb that refuses it

`challenge` 393 of 393 refused and `accept` 128 of 128 (no duel); `comply` 137 of 137 and `defy` 21 of
21 impossible (no obedience, no defiance); `covenant` 47 of 47; `exchange` 225 of 225 (no trade);
`train` 324 of 324 (no growth); `sabotage` 142 of 142, `raze` 73 of 73, `found` 25 of 25, `build` 15 of
15 (no works, no ruin); `seize` 27 of 27, `revoke` 6 of 6, `pardon` 11 of 11, `determine` 11 of 12
(no power changes hands by act). Three seeds, three seasons each. A fifth of everything attempted
(1,585 of 7,940 acts) is one of these: persons spend their scenes trying the verbs that would make a
story and being refused.

### 3.4 What a player's choice changes in them — §2.5: paper.

### 3.5 The shape of the tail — are all runs the same run

- **The built world is one world.** `build_realm(0)`, `(1)` and `(2)` are equal in every one of the 22
  projected components (persons, seats, sites, stores, stance, pursuits, convictions, tenures): the
  seed moves draws and nothing else. There is no generated realm.
- **The played skeleton is one skeleton.** After three seasons, site condition is equal at all three
  seeds (and equal to the NULL arm); seats, persons, rungs, capability, pursuits and convictions are
  **equal between seeds 1 and 2**, including the death; seed 0 differs from them by that one death.
- **The census is one census.** Attempts 2,630 / 2,646 / 2,664; not refused 53% / 57% / 57%; the same ten
  verbs certain, the same fifteen to eighteen always refused; `stores.changed` 185, `yield.taken` 111,
  `condition.worn` 966 at every seed.
- **Six seasons add nothing new** (WR runs): no ending, persons 83 throughout at seed 0, the same
  kinds, with `claim.decayed` rising to 65% of the log.

What varies by seed is which of two bands a `research` roll lands in, who writes which record, and
whether the cardinal is caught this year. The tail has no shape because there is no distribution of
outcomes to have a tail.

### 3.6 Are the persons' reasons readable afterwards

No, in three ways. (i) The closing acts carry no cause (F-PES-GAME-03). (ii) The chooser's deciding
term is returned to nobody (CORE `01_CORE_reason_trail_in_the_act_store.md`; CHAR
`02_CHAR_reason_trail_and_small_edits.md`). (iii) What the log does link is refusal-heavy: WR's deepest
"chains" read `transfer > train > dispatch > issue > tend > exchange > move > tend > train > raze`, a
sequence of unrelated refused attempts. A narrator given the seed-0 log can truthfully say who wrote
what about which granary.

### 3.7 Does the story survive the extremes

| extreme | run | what happens |
|---|---|---|
| no named person (`cap=0`) | `x5_extremes.py 0 3` | the loop runs; 37 cohorts, **no office exists** (seats are minted with the cast); 1,049 acts, 9,252 of 11,815 Events are memory; sites, stores and bodies as the full realm |
| one, two, five named persons | same | runs; 1,111 / 1,120 / 1,241 acts; the lone individual surveils and surveys |
| nobody acts | X1 NULL, SE `probe_noacts` (120 seasons) | the clocks run for ever; nothing ends |
| total famine, nobody acts | `x3_famine.py 0 0 20 nullglobal` | every cohort dies in season 17; the 46 individuals are untouched and the loop runs on |
| the King and the heir dead | `x2b_death_detail.py … p_npc_020,p_npc_031` | three seats vacant for the whole run; no ending fires; nothing else changes |
| a hundred factions | not run | no builder makes one `[SKIPPED: no generator; the realm is one authored world]` |

Completeness (R): the engine does not break at its extremes, which is to its credit, and it does not
*respond* at them either. A realm with no people, a realm with no King and a realm in which nobody acts
are each indistinguishable, in what happens next, from the shipped realm.

### 3.8 The instruments' verdicts, tested

WR found the story bar cannot fail and its control is inverted (`09_WR_story_instruments_that_can_fail.md`);
CORE found the corpus bar NOT-COMPUTABLE for 143 of 143 cases with four checks that pass 143 of 143. Added
here: every instrument that walks `causes[]` is blind to the closing acts (F-PES-GAME-03), and none
compares against the null arm, so none can distinguish a realm that corresponds from a realm that
changes. `harness/arc.py` reads 33 "persons with an arc" at seed 0 over six seasons (WR run); the first
twelve it prints are cohorts ("the people of Kronmark: utter, commit") whose arcs are utterances.

### 3.9 The provided arcs and characters, taken together

The ARCS lane adjudicates the cases one by one (`12_ARCS_adjudication.md`); this is the reading of the
corpus as a whole against the game's two standing rules.

- **Against "no GM".** `corpus_run` (ARCS and CORE runs, cited): 16 of 143 cases name a player the engine
  does not supply; the bar reads NOT-COMPUTABLE for all 46 NPC and all 97 ARC cases (103 RUNS-UNDECLARED,
  40 SPAN-UNAUTHORED). `ENDINGS_CLASSIFIED.yaml` (an agent's blind classification of the arcs' own
  `ends_when` prose; the file calls itself the weakest evidence in its suite): of 50 arcs, 10 are
  `NEVER` (*"never, absent player action"*) and 3 `UNCLEAR`. A quarter of the provided arcs, as
  specified, do not end unless a player ends them.
- **Against "we do not do deterministic".** The same file: 8 arcs close on a `THRESHOLD` (*"a counter,
  clock or tracked resource fires, nobody named as choosing"*) and 19 are `forced_by_threshold`; 9 close
  on a `ROLL`. So as written, 8 to 19 of 50 arcs end by the mechanism the standing rule forbids (a
  crossing that produces an outcome), and the engine's own law agrees with the rule against them
  (`loop/matter.py`: *"L5: a crossing MAY NEVER PRODUCE AN OUTCOME"*). The cases are the specification
  of what must be simulated (`AUDIT_BRIEF.md`), so this is a conflict between two things Jordan has
  stated; it is listed for the ARCS lane and §7 J-3, and not resolved here.
- **Against the running game.** Every arc that turns on a death, a succession, a verdict, a famine, a
  war or a betrayal with consequence (the ARCS lane's `core` needs) meets §3.3: the closing verb is
  refused or unformed in computed play. The corpus is one template world run 143 times (F-CORE-02); the
  realm, where the arcs' characters all live at once, produces none of their endings in any run.

## 4. Findings, worst first

Severity: **B** blocks a requirement · **D** degrades narrative · **H** hygiene. Each: claim · falsifier
run and its control · requirement · minimal fix at the owner.

**F-PES-GAME-01 · B · the world's skeleton does not respond to its people.** Persons, seats, site
conditions, rungs and stores after three played seasons equal the same world with nobody acting, at
seeds 0, 1, 2 (one `capture` death excepted). *Falsifier:* `x1_world.py`; a difference in any skeleton
component without a planted hazard. *Control:* the NULL arm's own wear, yield and hunger are seen; the
planted death (X2) and the established office are seen. *Touches* R-01, R-02, R-04, R-05. *Fix:* no
single owner; the ring in §7, read by `16_PESSIMIST_GAME_consequence_reading.md`.

**F-PES-GAME-02 · B · no consequence crosses a seam.** Executed answers to another's Event land in the
information verbs 83 to 85% of the time and in personal combat, mass battle, the settlement verbs and
training never; `person.died`, `field.lost`, `news.told`, `body.changed` are answered by nobody.
*Falsifier:* §1.2's matrix; any executed answer in the PC, MB, SE or CHAR column. *Control:* the verb
census (nothing executed in those columns) agrees; the matrix does see the FA, SC and FI cells. *Touches*
R-01, R-04. *Fix:* the occasions each lane names (`03_PC_duel_chain_reach.md`,
`04_MB_headcount_grade_and_scale.md`, `07_SE_ground_and_granaries.md`, `06_FA_decree_binds.md`), in the
order of §7.

**F-PES-GAME-03 · D · the acts that close a story carry no cause.** An act on a standing occasion
(a vacancy, a writ, a wounded person, a detainee; fifteen sources in `world_q.questions_for`) is folded
with `causes == [the act]`. The Prince's succession does not cite the King's death. *Falsifier:*
`x2b_death_detail.py 0 1 4 p_npc_020`, the `succession.claimed` line (`causes=['ACT']`). *Control:* a
`create_record` answering the same death does cite it (the 19 descendants). *Touches* R-01, R-02; every
reader of `causes[]`. *Fix:* `16_PESSIMIST_GAME_standing_occasions_carry_their_cause.md`.

**F-PES-GAME-04 · D · in computed play the game is a fixed function of state** (standing rule; R-09).
7.8%, 10.8% and 8.4% of attempted acts are drawn; four of the engine's seven draw sites ship off; the
built world is identical at every seed and the played skeleton is identical at two seeds of three.
*Falsifier:* §1.3's census; the BUILD and PLAY projection lines of `x1_s*_k3.txt`. *Control:* the drawn
verbs do show spread (`research` three bands; `tell` three). *Fix:* the act side is
`18_DETERMINISM_task_draw_for_uncontested_verbs.md` and its siblings; the clock side is
`16_PESSIMIST_GAME_the_world_draws.md`, `09_WR_world_motion.md` edit 4 and B10-18's weather draw.

**F-PES-GAME-05 · D · the world's own motion is fixed and synchronized.** A planted total famine kills
all 37 cohorts in the same season, the seventeenth; every Site of a kind wears by one step; yield is
one figure. *Falsifier:* `x3_famine.py 0 0 20 nullglobal` (trajectory 940 … 40, then 37 deaths).
*Control:* the unstarved arm holds 940 for twenty seasons. *Touches* R-09. *Fix:*
`16_PESSIMIST_GAME_the_world_draws.md`.

**F-PES-GAME-06 · D · rest cures starvation.** `tend` restores a body whole, with no roll, no food and
no cost; every cohort that hungers in season 0 is whole by its end, at every seed. A wound is the same.
*Falsifier:* X1 PLAY vs NULL `body` row (PLAY 1000, NULL 940, all 37). *Control:* the NULL arm, where
nobody tends, keeps the loss. *Touches* R-01 (consequence), R-09. *Fix (owned elsewhere, cross-listed):*
`loop/effects_combat.py::_eff_tend` as a graded draw restoring part of the headroom (sweep D-05,
`03_PC_exits_withdrawal_recovery.md` Part C, hole row H-304); **and one clause no lane has written:**
`tend` restores nothing to a body whose last fall was hunger while its home's larder is still short
(the predicate is `world_q.hunger`'s band for the subject's home; an eligibility conjunct on the `tend`
row, so a refusal, not a second rule).

**F-PES-GAME-07 · D · the largest news in the realm does not travel.** The King's death is held by 16
of 82 the season it happens and 17 three seasons later; in the season after the heir has taken the
throne a confessor is still trying to confer it (24 attempts). *Falsifier:* `x2b` know-of-a-death line
per season. *Control:* the 16 who were present do hold it. *Touches* R-07 (imperfect knowledge is met;
*spreading* knowledge is not). *Fix:* FI's `08_FI_02_rumour-that-travels.md`; add to its gate that a
`person.died` of a seat-holder is held by more than those present within two seasons.

**F-PES-GAME-08 · D · a vacant seat has one route, and it is the heir's.** The throne passes by one
uncontested, undrawn claim; the dead King's duchy and the heir's old seat stay empty; with the heir
dead too the throne stays empty and nothing else changes; 43 `confer` attempts in three seasons are
refused, one of them a duke conferring the crown on a settlement's cohort. *Falsifier:* `x2_death.py`,
`x2b` both arms. *Touches* R-04, R-09. *Fix (FA and sweep, cross-listed):* `06_FA_seat_terms_and_turnover.md`,
`14_VERBS_BINDING_C_turnover.md`, `09_WR_world_motion.md` edit 2, sweep C-07 and C-11 (the claim is a
draw; rival claims are opposed). **Owed to CHAR/FA:** `confer`'s `to` operand is formed over every
person the conferrer knows, cohorts included; it should be formed over persons the seat's `binds`
admits.

**F-PES-GAME-09 · D · most persons are downstream of nobody and upstream of nobody.** Reach (executed
acts by others descending from a person's acts), seed 0, three seasons: 48 of 83 at zero; median 0;
cohorts' mean 0.6, seat-holders' 18.2. The 37 cohorts are 45% of the actors and make 43% of the acts
(1,143 attempted of 2,630; 596 executed of 1,394: `x6_cohort_cut.py 0 3`, the shipped arm), and what
"the people of" a settlement execute is `create_record` 174, `utter` 107, `reconstruct` 51, `research`
49, `forge` **34** (the 46 individuals forge 18), `surveil` 28, `conceal` **18** covers. A town's
population forges documents and assumes cover identities, and cannot `migrate` (refused every time).
*Falsifier:* `x4_player.py 0 3` REACH lines; `x5`; `x6`. *Touches* R-06; the genre test fails (a
strategy player does not expect a village to be a spy). *Fix:* none proposed here; §7 J-2.

**F-PES-GAME-10 · D · a player-king who does nothing loses nothing.** §2.5. *Touches* R-02 as meant.
*Fix:* the ring; nothing specific to the play surface.

**F-PES-GAME-11 · D · the provided arcs conflict with two standing rules as specified.** §3.9. *Fix:*
ARCS lane; §7 J-3.

**F-PES-GAME-12 · H · three `met` requirements are met on a channel that carries paper.** R-01, R-02
and R-03 are true as worded and unshown as meant. *Fix:* `16_PESSIMIST_GAME_consequence_reading.md`.

**F-PES-GAME-13 · H · offices exist only where the cast seats them.** `build_realm(0, cap=0)` has no
office; a seat is minted with its first holder. A realm whose seats die out has no seats to fill.
*Falsifier:* `x5_extremes.py 0 3`, the `offices=0` line. *Fix:* FA lane (seats from `offices.yaml`
independent of the cast cap); cross-listed, no proposal here.

## 5. Determinism register (the standing rule), ranked

The act side is `audits/18_DETERMINISM_SWEEP.md` C-01 to C-15 and is not restated. What that sweep does
not cover, ranked by what it decides:

| id | where | what is fixed | measured | owner of the fix |
|---|---|---|---|---|
| W-1 | `queries/world_q.py::body_hazard`; `illness_rate`, `age_step` ship 0 | nobody can die of age or illness: a certain *non*-event | 0 natural deaths in every run of every lane | `09_WR_world_motion.md` edit 4 (Jordan's) |
| W-2 | `world_q.season_factor`; `season_factor_draw` ships `()` | every harvest the same | `yield.taken` 111 and `stores.changed` 185 at every seed | B10-18 CL-EVENTS (2) |
| W-3 | `modules/settlements/subsist.py` (`lost = body_step × units short`) | who suffers in a famine and how much | 37 of 37 cohorts in step; all die in season 17 | `16_PESSIMIST_GAME_the_world_draws.md` |
| W-4 | `loop/matter.py`, the wear loop | every Site of a kind decays alike | site condition equal at seeds 0, 1, 2 | same proposal |
| W-5 | `decision/choose.py::declare_intents`, `intent_disclosure` 0.0; `loop/witness.py`, `telling_privacy` 0.0 | nobody ever lets an intent slip; nothing is ever confided | both draws never taken | FI / CHAR `[UNVERIFIED: whether either lane's proposals turn them on]` |
| G-1 | `harness/populated.py::build_realm` | the realm itself: persons, seats, stances, convictions identical at every seed | 22 of 22 projected components equal at seeds 0, 1, 2 | `21_PROCEDURAL_GENERATION.md`'s subject `[not opened]`; a Jordan call if it is not covered there |
| G-2 | the realm's violence | one authored situation yields the one death, the same man, at two seeds | `p_npc_013` at seeds 1 and 2 | PC occasions (`03_PC_duel_chain_reach.md`) |
| G-3 | `_eff_succeed`, the roster `successions` | the heir, always, at once, unopposed; with no heir, vacancy, always | X2, both arms | sweep C-07, C-11 |
| G-4 | eighteen verbs refused at every attempt | a *certain no* is as fixed as a certain yes: 1,585 of 7,940 acts | §3.3 | each lane's formation proposals (`14_VERBS_*_A_formation.md`) |

**The opposite failure (should vary, does not), tested per premise:** the succession (no spread); the
famine's toll (no spread); the death's reach (16 then 17: no spread over time); the played skeleton
across seeds (none). **Should not vary and does:** nothing found; seeded replay held wherever it was
compared (the control arm of X2 reproduces the shipped four-season hash).

**This lane's own text, checked against the rule.** "A decree binds" (given to this lane as a premise
sentence) is restated in §2.2 as a drawn answer. No proposal of this lane makes an outcome a fixed
function of state: the world-draws proposal adds draws; the standing-occasion proposal changes
`causes[]` only; the consequence reading is an instrument.

## 6. The stories that cannot happen, and the ones that can

**Cannot, today, in the shipped realm (each with the run that shows it):** a duel (`challenge` 0 of
393); a killing outside one arrest (`fight` unformed); a death in bed (hazards 0); a contested
inheritance (one claimant; first claim wins); a regency or an interregnum with a cost (X2b: nothing
changes); a usurpation (`seize` 0 of 27, `revoke` 0 of 6); a war, a conquest, a siege that ends
(MB, FA); a famine (stores 21 times need; rest cures hunger); a founding, a great work, a ruin
(`found`, `build`, `raze` 0 of 113); a trade (`exchange` 0 of 225); an apprenticeship (`train` 0 of
324); obedience or defiance (`comply` 0 of 137); a rumour that moves someone (0 of 19 tellings
answered); revenge (a death answered by nobody); a friendship or a feud forming (stance moved for 1 to
7 of 83 persons); a birth, a marriage, a coming of age (no verb, no clock: persons never increase); a
trial with a verdict that changes a life (`determine` 1 of 12); an ending.

**Can, and do:** a record of what the granary held; a petition that lapses; a forgery nobody examines;
a cover nobody penetrates; an oath that matures; a march that finds an empty field; a move to another
town; the arrest of one cardinal.

**Can, with the proxy planted, and then stop:** a King's death (the heir succeeds; nothing follows); a
famine (the town rests and recovers).

## 7. Proposals, the order of the ring, and what is Jordan's

### 7.1 Proposals written by this lane

| file | carries | cost |
|---|---|---|
| `proposals/16_PESSIMIST_GAME_standing_occasions_carry_their_cause.md` | F-03 | edit |
| `proposals/16_PESSIMIST_GAME_the_world_draws.md` | F-05, W-3, W-4 | edit |
| `proposals/16_PESSIMIST_GAME_consequence_reading.md` | F-01, F-02, F-12 (amends CORE 03 §2) | edit |

### 7.2 The first ring — the shortest order in which one consequence crosses one seam

Every step is another lane's proposal except where marked; this is the dependency order the game-level
runs imply, for the holistic stage. A step is done when its own gate passes; the ring is done when the
game gate below passes.

1. **The world produces occasions.** Scarcity and difference (`07_SE_ground_and_granaries.md`); the
   weather draw (B10-18); hunger and wear drawn (*this lane*); natural death on (`09_WR_world_motion.md`
   edit 4, Jordan's).
2. **Consequences stick.** `tend` graded and partial, and refused on a hungry body with a short larder
   (sweep D-05; the clause in F-06).
3. **Consequences are readable.** Standing occasions carry their cause (*this lane*).
4. **Others learn.** `08_FI_02_rumour-that-travels.md`.
5. **Seats change hands, by a draw.** `06_FA_seat_terms_and_turnover.md`, `14_VERBS_BINDING_C_turnover.md`,
   sweep C-07 and C-11.
6. **Orders are answered, by a draw.** `06_FA_decree_binds.md` as reconciled by the sweep.
7. **Violence has occasions and more than one outcome.** `03_PC_duel_chain_reach.md`,
   `14_VERBS_PHYSICAL_A_custody_and_force.md` A3, `04_MB_headcount_grade_and_scale.md`.
8. **The reading.** `16_PESSIMIST_GAME_consequence_reading.md` (*this lane*).

**The game gate** (one command, three seeds, three seasons, no planted state): the played arm differs
from the null arm in persons and in seat holders at each seed; at least one executed answer stands in
each of the PC, SE and non-emission FA columns; `person.died` and `tenure.closed`, where emitted, are
each among the causes of another person's executed act; the played skeleton differs between at least
two of the three seeds. Today every clause fails.

### 7.3 Survivors for Jordan (each survives the five-step ladder; two options, two games)

- **J-1 · a land with no people.** With every cohort of a settlement (or the realm) dead, the
  individuals seated over it are untouched (only a cohort eats: RULED, ED-IN-0255, not re-raised).
  (a) Leave it: depopulation is felt only through yield, levy and stability once those bind; a lord of
  an empty land is a legitimate state. (b) A seat whose rung has no living cohort beneath it loses its
  remit until one returns. Under (a) famine is an economic story; under (b) it is a political one, and
  a blight can unseat a duke.
- **J-2 · cohorts as full actors.** The 37 cohorts are persons (S9.1) and are offered the whole verb
  table: they write records, utter propositions, commit, research, forge (34 forgeries to the
  individuals' 18) and assume covers (18), make 43% of all acts, and are answered by almost nobody
  (reach 0.6). (a) Keep: the people are a chorus of individuals writ
  large. (b) Give a cohort a collective aperture by a roster column (petition, migrate, work, tend,
  comply or refuse, riot) so that what a population does is what a population can do. Under (a) the
  realm's log is mostly the populace's paperwork; under (b) it is the named persons' acts against a
  populace that moves in a few heavy ways. `[X6, the cut run that would price (b), had not finished
  when this was written: §8.]`
- **J-3 · arcs that end on a threshold.** Eight of fifty provided arcs close when a counter fires and
  nineteen are forced by one (`ENDINGS_CLASSIFIED.yaml`); the standing rule and the engine's L5 both
  forbid a crossing that produces an outcome. (a) The arcs are restated so each threshold raises a
  *question* a person answers by a drawn act (the engine's present law). (b) The rule admits clocks
  that force a moment (a crossing may open a mandatory scene, never decide it). They differ in whether
  the world can corner a character.
- **J-4 · the realm is one realm.** `build_realm` gives the same persons, seats and stances at every
  seed (G-1). (a) Intended: Valoria is authored, and the seed moves only chance. (b) The seed also
  draws some of the starting state (who holds a grudge, which granary is low, who is ill). Under (a)
  replay variety must come entirely from play; today it does not come.

## 8. Evidence log

All at `4995824`, `PYTHONHASHSEED=0`, outputs under `runs/PES_GAME/` in the scratchpad.

| run | command | seed · seasons | outcome |
|---|---|---|---|
| X1 | `x1_world.py S 3` → `x1_s{0,1,2}_k3.txt` | 0, 1, 2 · 3 | §1.1 to §1.3, §3.5; shipped hashes `52ff67bc…`, `26d2091b…`, `b9555289…` (seed 0's equals WR's season-2 hash) |
| X2 | `x2_death.py 0 1 3` → `x2_death_s0.txt` | 0 · 1 + 3 | §2.1; control hash `abbde715aa0e` equals the shipped four-season realm |
| X2b | `x2b_death_detail.py 0 1 4 p_npc_020` and `… p_npc_020,p_npc_031` | 0 · 1 + 4 | §2.1 links 3 to 8; both finished. King only: 16 hold an `exists` claim of his death in every one of the four seasons (17 by `x2_death.py`'s wider predicate match), `off_duke_valorsmark` and `off_heir` vacant at the end. King and heir: 15 know; `off_king`, `off_duke_valorsmark`, `off_heir` vacant in all four seasons |
| X3 | `x3_famine.py 0 0 20 nullglobal` → `x3_nullglobal_s0.txt` | 0 · 20 | §2.4 links 2 to 4, 8 |
| X3 local | `x3_famine.py 0 1 5 local` | 0 · 1 + 5 | `[not finished under load; §2.4 link 5 rests on X1, not on it]` |
| X4 | `x4_player.py 0 3` → `x4_s0.txt` | 0 · 3 | §2.5; reach |
| X5 | `x5_extremes.py 0 3` → `x5_s0.txt` | 0 · 3 | §3.7 |
| X6 | `x6_cohort_cut.py 0 3` → `x6_s0.txt` | 0 · 3 | the shipped arm finished (F-09's cohort figures; 513 executed answers, equal to X1's matrix total, the instrument's own agreement); the CUT arm (cohorts do not deliberate) `[not finished under load: J-2 is unpriced]` |
| census parse | `parse_census.py x1_s*_k3.txt` | — | §1.3 table; the dead-end sum 1,585 of 7,940 |
| fixtures | `build_realm(0).fixtures.get(...)` | 0 | the four draw sites shipped off |
| cited, not rerun | `runs/WR/probe_s{0,1,2}_k6.txt`, `runs/WR/storybar_drawseeds_s0_k2.txt`, `runs/SE/probe_noacts_s0_120.txt`, `runs/SE/probe_play_s0_4.txt`, `runs/CORE/register_requirements.txt`, `runs/CORE/m1_summary.txt`, `runs/ARCS/corpus_run.txt` | | as the lanes report |

Not read: the subsystem dossiers and `.designs/` sets (the subsystem lanes' reading is relied on);
`audits/20_NARRATIVE_CHURN.md` and `21_PROCEDURAL_GENERATION.md` beyond their heads; the `16_PESSIMIST_*`
siblings. No `pytest`, no `aperture`, no tracked file written; machine load passed 40 during the last
third of the runs.
