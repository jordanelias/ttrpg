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
blind reader.
