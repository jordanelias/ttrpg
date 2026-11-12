# DICE (pessimist) — an unopposed task is opposed by the untrained score; a task nobody has ranked is plain; the task draw reports what it stopped

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-07, C-U5a-13) — its amendment to `18_DETERMINISM_task_draw_for_uncontested_verbs.md` (item 3, the gate's reading and refusal to ship) is applied in that file. Its amendments to SC's two files are U5c's. Under A-6 and A-26 the unopposed stand-in is an ordinary person's pool times `opposition_rate`; the 16.5 % and 42 % figures are the old regime's and the throughput reading is what replaces them.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-5a. Rows applied: `R5_READ.md` §2 (A-5, A-6, A-26: (a) restated as the U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "Ob" → "obstacle" in prose (glossary *obstacle*).
form; the figures of (b)-(d), "What it changes" and the gate are dropped as whole-dice history; gate 2's property kept),
§7/§7b (test file, tier); U1 D-U1-02 and architecture §4 (the opposing operand is the **trained score**, never the
pool, at `opposition_rate`; the stand-in is `opposed_ob(pool_default, opposition_rate)` with the composer's even line
`even_line(pool_add)` as its own leading term), D-U1-04 (difficulty lives on the verb row, `difficulty_levels`,
sized by `difficulty_ob`), D-U1-11j (`obstacle_default` deleted; `pool_default` is the one stand-in); U1 glossary
(*untrained score*, not "ordinary score"; *stand-in*); U3 §4.1 row 19 (the amendment to 18-A lands with 18-A in B07; the
SC-B/T13 code part in B05), C3-N26. **The decision wins over the read lane:** R5 7b wrote the stand-in as "the
ordinary person's pool times `opposition_rate`", and the U5a head line above says the same; both are superseded by
D-U1-02 (A-79: "the six base dice never part of the opposition"). Changed: title word, (a), the three ordered
amendments' wording, the gate.

## Status: PROPOSED

Lands in batch: **B05** for the SC-B composer and T13 wording (IN/DICE, SC); the 18-A amendment (edit 3) in **B07**
with 18-A (split, U3 §4.1 row 19). Depends on: `05_SC_obstacle_difficulty_and_modifiers_B.md` and
`13_SC_tuning_tables.md` (B05), `U5c_SC_one_obstacle_form.md` §4 (OBS, the composer it amends), `sigma_leverage.opposed_ob`
and `even_line` (`29_DICE_one_opposed_rule_form_and_tuning.md` item 29-1, B05).

**Whole-dice figures.** The percentages and obstacles in "What it changes", "The problem" and the gate (2.0, 1.0,
42 / 58 / 74 / 83.5 %, 74 / 19 / 7 / 0, 16.5 %) were enumerated on the whole-dice sampler and the half-score
opposition, both retired (A-5, A-26, A-79). They are kept as the finding that motivated the form; no gate reads them.

Carries findings F-PES-DICE-02 and F-PES-DICE-06 of `../audits/16_PESSIMIST_DICE.md`. It writes no new
mechanism: it amends three proposals of this suite where they meet, so that the obstacle of a task with
nobody on the other side is one rule and not three. Amended: `05_SC_obstacle_difficulty_and_modifiers_B.md`
(SC-B, the obstacle's form), `13_SC_tuning_tables.md` (T1, the level sizes),
`18_DETERMINISM_task_draw_for_uncontested_verbs.md` (18-A, the task route). Lanes that own the edited
files: SC (the composer and the level table), IN (the route and its gate). Reference only
(`CLAUDE.md` §0.05); not ratified by being written.

## What it changes in `engine/season/` at runtime

Nothing until SC-B and 18-A land; it changes what they land as.

- At SC-B's **control arm** nothing moves: every rolled act composes today's obstacle (the four rows
  with no person counterparty reach it as `routine` plus the stand-in, where SC-B reaches it as
  `demanding` plus nothing).
- At 13's **calibrated arm** a row with no person counterparty composes four distinct obstacles over the
  four difficulty levels, where 13 as written composes fewer (the floor swallows the lower levels).
- At 18-A's **shipped arm** a converted task row whose verb lane has stated no level rolls at `plain`
  plus the stand-in, never at `obstacle_default` (deleted). Its band shares are read on the A-5 sampler
  by 18-A's reading (d); the whole-dice shares this lane measured are in "The problem".

## The problem, with evidence

Exact enumeration through the owner (`band_odds`; `runs/PES_DICE/pure.txt`).

1. **18-A ships the task draw at `obstacle_default`** (*"until [the difficulty column] lands,
   `obstacle_default`"*; cost class: *"it ships at `obstacle_default` without it"*). At the shipped pool
   that is (2 dice, obstacle 2.0): `band_odds(2, 2.0) == (0.74, 0.19, 0.07, 0.0)`. Under 18-A's own
   `task_fraction` (Partial one half) a converted verb delivers 0.19 × 0.5 + 0.07 = **16.5 %** of the
   effect it delivers today. On the sweep's count of 727 consequential undrawn outcomes in five realm
   seasons, that is about 120. Plain failures write nothing. `obstacle_default` is H-127's stand-in for
   *a subject with no score to halve*; a journey, a mending or a day's work has no subject of that kind,
   and the stand-in's size (worth a score of 4) was never meant as a task's difficulty.
2. **Under 13's calibrated sizes three levels are one number for an unopposed row.** T1: `plain` 0,
   `routine` 0.5, `demanding` 1.0, `hard` 1.5, the sum *"floored at `OB_MIN` after every term"*. SC-B:
   the `opposition` term is *"absent for a non-person subject"*. So a row with no person counterparty
   composes max(1, 0), max(1, 0.5), max(1, 1.0), 1.5. T1's own separation figures
   (*"0.42 / 0.58 / 0.74 / 0.83 at pool 2"*) are for an opposed act, where the unscored counterparty adds
   1.0; its falsifier tests *"at equals"* and cannot see the unopposed rows. Those rows are `speak`,
   `research`, `examine`, `surveil` and every one of 18-A's 22 task rows.
3. **One die cannot succeed at obstacle 2.** `band_odds(1, 2.0) == (0.9, 0.1, 0.0, 0.0)`: the first point of
   a skill removes the Success band from every default task (F-PES-DICE-06).
4. **Control: the regime, not the route, is what starves the task draw.** The same fraction at other
   pairs: (2, 1.0) 0.42; (4, 1.0) 0.63; (4, 2.0) 0.40; (5, 1.0) 0.70; (5, 2.0) 0.49.

## The resolution, decided

**(a) Where nobody opposes, the untrained score does** (ladder step 1: A-26 and A-79 rule the opposing
operand, the trained score at `opposition_rate` per point, replacing the 2026-08-14 *"score/2"*; U1
D-U1-02; and `10_DICE_one_score_two_roles.md` already reads an unauthored *person* as `pool_default`).
The `opposition` term is never absent: for a person counterparty it is `opposed_ob(his trained score,
opposition_rate)`; for a row or an act with no person counterparty it is the stand-in
`opposed_ob(pool_default, opposition_rate)`, through the same one owner (`sigma_leverage.opposed_ob`). In the
social and task composer the even line `even_line(pool_add)` is its own leading term on every roll (U1
architecture §4), never part of the opposition. A self-plea keeps SC-B's rule (nobody opposes himself; the
stand-in applies). One composition for every rolled act; four levels are four numbers on every row; the
floor is met by construction on any row with no favourable term, since the even line and the stand-in are
always present.

**(b) The level of the four no-counterparty rows drops one step at the control arm**, so that today's
obstacle is reproduced: `speak`, `research`, `examine`, `surveil` → `routine` (the level plus the
stand-in reproduces today's composed obstacle at the control arm, where SC-B assigns `demanding` plus
nothing; the control-arm identity is D-U1-04's, "routine plus the stand-in = today's obstacle for an
inquiry"). At the calibrated arm the level of each row is 13's to restate on the same table; this proposal
fixes the form and assigns no calibrated level.

**(c) A task row nobody has ranked is `plain`** (ladder step 5). 18-A's item 3 reads: the obstacle is
the task's difficulty, *the row's `difficulty:` level, `plain` where the owning verb lane has stated
none*, plus the terms that exist. `plain` composes the even line plus the stand-in at both arms.
`obstacle_default` is not read by the task route at all (SC-B deletes it, D-U1-11j; this removes its last
proposed reader).

**(d) 18-A's gate gains one reading, and one refusal to ship.** The reading: for each converted verb,
the count of Events at each band per season with `task_draw_arm` on, beside the count of its success
Events with the arm off, seeds 0 to 2, two seasons, in the landing commit's body. The refusal: the arm
does not ship `on` while any converted verb with ten or more off-arm successes over those runs has
**zero** Success-or-better Events on-arm (a verb that has stopped happening; the threshold is zero, so
it is no tuned number). What the reading shows beyond that is evidence for the pool-regime question
that is already Jordan's (`../audits/10_DICE_audit_addendum_B.md` §5.6), not something to tune by
editing a level.

## The exact edits, by owner

1. **`05_SC_obstacle_difficulty_and_modifiers_B.md`**, the terms table, row `opposition`, column
   *applies to*. Old: *"an act with a person counterparty; absent for a non-person subject (a
   `DocketItem`, a Record, a site) and for a self-plea"*. New: *"every rolled act:
   `opposed_ob(the person counterparty's trained score, opposition_rate)`; where there is none (a
   `DocketItem`, a Record, a site, a task), the stand-in `opposed_ob(pool_default, opposition_rate)`; a
   self-plea likewise"*. Its edit 2, old: *"the rows with no person counterparty (`speak` …; `research`,
   `examine`, `surveil`) → `demanding` (2)"*; new: *"→ `routine` (the level plus the stand-in reproduces
   the control-arm obstacle)"*. In code, when SC-B is built: the host builder
   (`seam/wrappers/sigma.py::contest_input`) passes `opposition=None` as today, and the module's
   composer (`modules/social_contest/roll.py::obstacle`) reads `None` as
   `opposed_ob(inp.pool_default, inp.opposition_rate)`, with `SocialContestInput.pool_default` and
   `.opposition_rate` filled by `_frame` from the fixtures the pool reader already uses (U1 architecture §8
   lists both fields). The composer stays the only place the stand-in is spelt.
2. **`13_SC_tuning_tables.md`** T1. *First values* gains: *"an unopposed row composes the even line, the
   level and the stand-in; the four levels give four distinct obstacles at the calibrated arm"*.
   *Falsifier* gains: *"or two adjacent levels composing one obstacle on a row with no person
   counterparty"*. *Row values* for `research`, `examine`, `surveil`, `interrogate`: restated by that lane
   on the amended form.
3. **`18_DETERMINISM_task_draw_for_uncontested_verbs.md`** item 3, old: *"the `difficulty` column
   `13_SC_tuning_tables.md` T1 puts on the verb row; until it lands, `obstacle_default`"*; new: *"the
   row's `difficulty:` level, `plain` where the owning verb lane has stated none; the route lands with
   or after the column, never on `obstacle_default`"*. Its gate gains item 5 as (d) above. Its cost
   class line (*"it ships at `obstacle_default` without it"*) is struck.

## The gate (execution artifacts)

`runs/PES_DICE/pure.txt` was lane scratch, not in the repository. Tests in
`engine/season/tests/test_social_contest_module.py` (exists): `test_unopposed_row_term_list_has_an_opposition_entry`,
`test_four_levels_compose_four_strictly_increasing_obstacles_on_an_unopposed_row`,
`test_routine_plus_stand_in_reproduces_the_control_obstacle`. Command:
`python -m pytest engine/season/tests/test_social_contest_module.py -q`.

1. **Control.** SC-B's own: at the control arm every world hash is the base commit's. This proposal adds
   no mover there; the four re-levelled rows are the check (their term lists read the level plus the
   stand-in, composing today's obstacle).
2. **Four levels, four obstacles, on an unopposed row.** Through the composer, a `research` on a site at
   each level in turn, calibrated sizes: four strictly increasing obstacles. As 13 is written the first
   three are equal, which is the assertion that can fail. No figure is asserted.
3. **18-A's reading (d)**, in its landing commit (B07).
4. **The floor pool can Succeed on a plain task** (A-6: no pool in play is under `pool_floor`): the closed
   form's Success-or-better share at `(pool_floor, plain)` is above zero.

## The falsifier

After SC-B: a rolled act whose term list has no `opposition` entry; two difficulty levels composing one
obstacle on any row at the calibrated arm. After 18-A: a converted row whose term list shows
`obstacle_default`; an `on` arm shipped with a converted verb at zero Success-or-better.

## NERS reading (E last)

- **N.** Top-down: the standing rule's *"obstacle as the task's difficulty plus all modifiers"* needs
  the difficulty to survive the floor, and on unopposed rows it does not as written. Bottom-up: no new
  number (`pool_default`, `opposition_rate`). Laterally: an unauthored person and an unopposed task now
  resist by one rule. Cut it and what dies is the difference between a plain task and a demanding one
  wherever no person stands opposite, which is most of what a settlement, a journey and a workshop do.
- **R.** The no-player half: a realm whose routine work fails three times in four writes less story,
  not more. Completeness: Success exists at the floor pool on a plain task.
- **S.** One obstacle form for every roll; the task route and the contest route compose by one
  function; `obstacle_default`, a second stand-in beside `pool_default`, is read by nothing.
- **E.** Three sentences changed in three proposals and one line in the composer. Legibility: *every
  roll is against something, and where it is against nobody it is against an untrained score*.

## Cost class

Edit (to proposals not yet built); one field and one line in the composer when SC-B is built. Tier:
`sonnet`, effort `high`. Hash movers declared: none until SC-B and 18-A land (the control arm reproduces).
Lands it: the SC-B and T13 wording and the composer line in B05; the 18-A item 3 wording and reading (d) in
B07 with 18-A.
