# DICE (pessimist) — an unopposed task is opposed by the ordinary score; a task nobody has ranked is plain; the task draw reports what it stopped

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-07, C-U5a-13) — its amendment to `18_DETERMINISM_task_draw_for_uncontested_verbs.md` (item 3, the gate's reading and refusal to ship) is applied in that file. Its amendments to SC's two files are U5c's. Under A-6 and A-26 the unopposed stand-in is an ordinary person's pool times `opposition_rate`; the 16.5 % and 42 % figures are the old regime's and the throughput reading is what replaces them.

## Status: PROPOSED

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
  with no person counterparty reach 2.0 as `routine` 1 plus a stand-in of 1.0, where SC-B reaches it as
  `demanding` 2 plus nothing).
- At 13's **calibrated arm** a row with no person counterparty composes four distinct obstacles over the
  four difficulty levels (1.0 / 1.5 / 2.0 / 2.5), where 13 as written composes two (1.0 / 1.0 / 1.0 /
  1.5).
- At 18-A's **shipped arm** a converted task row whose verb lane has stated no level rolls at Ob 1.0
  instead of 2.0. At the shipped pool of two that is Failure 42 / Partial 32 / Success 25 /
  Overwhelming 1 instead of 74 / 19 / 7 / 0.

## The problem, with evidence

Exact enumeration through the owner (`band_odds`; `runs/PES_DICE/pure.txt`).

1. **18-A ships the task draw at `obstacle_default`** (*"until [the difficulty column] lands,
   `obstacle_default`"*; cost class: *"it ships at `obstacle_default` without it"*). At the shipped pool
   that is (2 dice, Ob 2.0): `band_odds(2, 2.0) == (0.74, 0.19, 0.07, 0.0)`. Under 18-A's own
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
3. **One die cannot succeed at Ob 2.** `band_odds(1, 2.0) == (0.9, 0.1, 0.0, 0.0)`: the first point of
   a skill removes the Success band from every default task (F-PES-DICE-06).
4. **Control: the regime, not the route, is what starves the task draw.** The same fraction at other
   pairs: (2, 1.0) 0.42; (4, 1.0) 0.63; (4, 2.0) 0.40; (5, 1.0) 0.70; (5, 2.0) 0.49.

## The resolution, decided

**(a) Where nobody opposes, the ordinary score does** (ladder step 3: the ruled form is *"score/2 plus
whatever specific modifiers exist"*, and `10_DICE_one_score_two_roles.md` already reads an unauthored
*person* as `pool_default`). SC-B's `opposition` term is never absent: for a person counterparty it is
his score halved, as SC-B has it; for a row or an act with no person counterparty it is
`opposed_ob(pool_default)`, 1.0 at the shipped fixture, through the same one owner of the divisor. A
self-plea keeps SC-B's rule (nobody opposes himself; the stand-in applies). One composition for every
rolled act; four levels are four numbers on every row; `OB_MIN` is met by construction on any row with
no favourable term, since the stand-in is itself 1.0.

**(b) The level of the four no-counterparty rows drops one step at the control arm**, so that today's
obstacle is reproduced: `speak`, `research`, `examine`, `surveil` → `routine` (1 + 1.0 = 2.0), where
SC-B assigns `demanding` (2 + nothing). At the calibrated arm the level of each row is 13's to restate
on the same table; this proposal fixes the form and assigns no calibrated level.

**(c) A task row nobody has ranked is `plain`** (ladder step 5). 18-A's item 3 reads: the obstacle is
the task's difficulty, *the row's `difficulty:` level, `plain` where the owning verb lane has stated
none*, plus the terms that exist. `plain` composes 0 + 1.0 = 1.0 at both arms. `obstacle_default` is not
read by the task route at all (SC-B deletes it; this removes its last proposed reader).

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
   `DocketItem`, a Record, a site) and for a self-plea"*. New: *"every rolled act: the person
   counterparty's score halved; where there is none (a `DocketItem`, a Record, a site, a task),
   `opposed_ob(pool_default)`; a self-plea likewise"*. Its edit 2, old: *"the rows with no person
   counterparty (`speak` …; `research`, `examine`, `surveil`) → `demanding` (2)"*; new: *"→ `routine`
   (1, plus `opposed_ob(pool_default)` 1 = 2)"*. In code, when SC-B is built: the host builder
   (`seam/wrappers/sigma.py::contest_input`) passes `opposition=None` as today, and the module's
   composer (`modules/social_contest/roll.py::obstacle`) reads `None` as
   `opposed_ob(inp.pool_default)`, one new field on `SocialContestInput` filled by `_frame` from the
   fixture the pool reader already uses. The composer stays the only place the stand-in is spelt.
2. **`13_SC_tuning_tables.md`** T1. *First values* gains: *"an unopposed row composes the level plus the
   stand-in: 1.0 / 1.5 / 2.0 / 2.5 at the calibrated arm"*. *Falsifier* gains: *"or two adjacent levels
   composing one obstacle on a row with no person counterparty"*. *Row values* for `research`,
   `examine`, `surveil`, `interrogate`: restated by that lane on the amended form (as written,
   `demanding` would now compose 2.0 on the three unopposed rows, which is today's obstacle).
3. **`18_DETERMINISM_task_draw_for_uncontested_verbs.md`** item 3, old: *"the `difficulty` column
   `13_SC_tuning_tables.md` T1 puts on the verb row; until it lands, `obstacle_default`"*; new: *"the
   row's `difficulty:` level, `plain` where the owning verb lane has stated none; the route lands with
   or after the column, never on `obstacle_default`"*. Its gate gains item 5 as (d) above. Its cost
   class line (*"it ships at `obstacle_default` without it"*) is struck.

## The gate (execution artifacts)

1. **Control.** SC-B's own: at the control arm every world hash is the base commit's. This proposal adds
   no mover there; the four re-levelled rows are the check (their term lists read
   `difficulty 1 + opposition 1.0`, summing to 2.0).
2. **Four levels, four obstacles, on an unopposed row.** Through the composer, a `research` on a site
   at each level in turn, calibrated sizes, pool 2: obstacles 1.0, 1.5, 2.0, 2.5 and Failure 42.0, 58.0,
   74.0, 83.5 %. As 13 is written the first three are equal, which is the assertion that can fail.
3. **18-A's reading (d)**, in its landing commit.
4. **One die.** `band_odds(1, 1.0) == (0.6, 0.3, 0.1, 0.0)`: a plain task done with one die can Succeed.

## The falsifier

After SC-B: a rolled act whose term list has no `opposition` entry; two difficulty levels composing one
obstacle on any row at the calibrated arm. After 18-A: a converted row whose term list shows
`obstacle_default`; an `on` arm shipped with a converted verb at zero Success-or-better.

## NERS reading (E last)

- **N.** Top-down: the standing rule's *"obstacle as the task's difficulty plus all modifiers"* needs
  the difficulty to survive the floor, and on unopposed rows it does not as written. Bottom-up: no new
  number (`pool_default`, the ruled divisor). Laterally: an unauthored person and an unopposed task now
  resist by one rule. Cut it and what dies is the difference between a plain task and a demanding one
  wherever no person stands opposite, which is most of what a settlement, a journey and a workshop do.
- **R.** The no-player half: a realm whose routine work fails three times in four writes less story,
  not more. Completeness: Success exists at one die on a plain task.
- **S.** One obstacle form for every roll; the task route and the contest route compose by one
  function; `obstacle_default`, a second stand-in beside `pool_default`, is read by nothing.
- **E.** Three sentences changed in three proposals and one line in the composer. Legibility: *every
  roll is against something, and where it is against nobody it is against an ordinary score*.

## Cost class

Edit (to proposals not yet built); one field and one line in the composer when SC-B is built.
