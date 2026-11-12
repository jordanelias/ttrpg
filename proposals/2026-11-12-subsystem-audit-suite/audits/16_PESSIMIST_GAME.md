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
