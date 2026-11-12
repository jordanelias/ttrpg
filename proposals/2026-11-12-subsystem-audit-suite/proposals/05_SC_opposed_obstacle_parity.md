# SC-P5 — what an equal opponent costs: the opposed obstacle against the dice's own mean

Folded: 2026-11-12, lane 29 (`audits/29_ONE_OPPOSED_RULE.md`; `proposals/29_DICE_one_opposed_rule_form_and_tuning.md`), on Jordan's A-71 — this file's edit 1 (`MU_PER_DIE × score`) is the one opposed-contest rule for the fight as well, at one fixture `opposition_rate`, through `sigma_leverage.opposed_ob(score, rate)`. Under A-6 the social composer adds the *even line* (`MU_PER_DIE × pool_add`) beside it, so equal ranks meet a plain matter exactly half the time at every rank (closed form on the bell curve: 50.0% at ranks 0, 2, 4, 7) and fail a `routine` one 56.9 to 60.1%. The tables below are whole-dice history. The falsifier's last sentence (a one-sided roll is never complementary) stands and is answered without a two-sided roll: of exchanges in which exactly one side lands, the better arguer is that side 66 / 78 / 92% at one, two and four ranks, the fight's own curve; a two-sided roll was run and loses the better side's edge (two ranks: 65.9%).

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-33) — un-held by Jordan's answer A-26 (0.4 per point: an even contest is even). The "HELD BACK" in the Status line below is superseded and this file is the carrier of the rate. Read with two things: the rate's one owner is `opposed_ob` (`U5c_SC_one_obstacle_form.md` §1), and it changes once, in that file's §4 step 5, together with A-5 (the bell curve), A-6 (score plus a base) and A-7 (two inputs), so the 0.4 is set against the re-centred sampler and not the whole-dice one this file measured.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.4 row SC-P5, §2 rows SC-P5 Status and A-80, §7, §7b-T; `unified/U1_OWNERS_AND_VOCABULARY.md` D-U1-02, D-U1-11j, ledger R-07 to R-10, R-16; `unified/U3_CONFLICT_LEDGER.md` C3-C12, `OWED_TO_UNIFICATION.md` §A row on `degree_from_net`'s docstring). Changed: the Status line is no longer HELD BACK (A-26 un-held it; A-79 makes it the one rule for fight and argument); "The two options" is replaced by the decision (option B, at `opposition_rate`); edit 1 reads the opponent's **trained score** and names the even line (D-U1-02); edit 2's "no edit" on H-127 is superseded by C-04 (`obstacle_default` deleted; the stand-in is `opposed_ob(pool_default, opposition_rate)`); the problem tables are marked whole-dice history (A-5); A-80's entrenched-world control is cited (C3-C12); the docstring that still states the 2026-08-14 form is named as owed to B05; lands-it and tier added. U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "Ob" → "obstacle" in prose (glossary *obstacle*).

**Lands in batch:** B05 (the joint calibration step, `U5c_SC_one_obstacle_form.md` §4 step 5). **Depends on:** `29_DICE_one_opposed_rule_form_and_tuning.md` item 29-1 (`opposed_ob`, B05), `U5c_SC_one_obstacle_form.md` (B05), `U5a_capability_home_and_two_inputs.md` Part B (the skill score, B05).

## Status: PROPOSED — un-held by Jordan's A-26 (2026-11-12: an equal opponent costs 0.4 per point), which overrides the 2026-08-14 half-score ruling; A-71/A-79 make it the one opposed rule for argument and fight. This file carries the rate.

Source: audit F-SC-03; hole rows H-288 (RULING), H-296, H-127 (the inversion).

## What it changes in `engine/season/` at runtime

The obstacle a PERSON opponent contributes becomes `opposition_rate × trained score` (live `MU_PER_DIE`,
0.4 per point) where it is `score / 2` today. Every contested social act against a person who holds a score moves; in the
shipped realm that is nobody (all pools and oppositions fall to the defaults; `aperture 2 0`:
*"`argue`: pools rolled [2] over 9 actors"*), so the realm hash is unchanged until attributes are
seated (`build_realm(cast_attributes=True)`). Under option A nothing changes.

## The problem (measured, exact odds; `engine.dice_engine.sigma_leverage.band_odds`, shipped arm)

A die nets `MU_PER_DIE = 0.4` on average (`engine/dice_engine/dice_engine.py`); an opponent's point
of score costs `0.5`. So an actor of score `s` against an opponent of score `s` has a mean margin of
about `−0.1·s`, and skill makes an even contest worse for the one who acts:

| s (both sides) | obstacle = s/2 | P(Failure) | P(Success or better) |
|---|---|---|---|
| 1 | 0.5 | 0.350 | 0.250 |
| 2 | 1.0 | 0.420 | 0.260 |
| 4 | 2.0 | 0.488 | 0.279 |
| 8 | 4.0 | 0.561 | 0.278 |
| 12 | 6.0 | 0.606 | 0.266 |

Swapping sides does not swap the result: 6 against 3 succeeds 0.570 of the time, 3 against 6 succeeds
0.052 (H-288's figures, reproduced). And the stand-in is worth a score of 4: an opponent holding a
score of 2 composes obstacle 1.0, one holding none composes `obstacle_default` 2 (H-127's inversion,
reproduced: P(Failure) 0.42 against 0.74 at pool 2).

*(The tables of this section are whole-dice history: they were measured on the whole-dice social roll
that A-5 retires. The live arm's closed forms are lane 29's, quoted in the Folded line above.)*

Control (the same pairs at `Ob = MU_PER_DIE × s`): P(Failure) 0.358 / 0.393 / 0.410 / 0.421 / 0.436
and P(Success or better) 0.324 / 0.372 / 0.394 / 0.407 / 0.423 at s = 2 / 4 / 6 / 8 / 12 — flat, and
near the Partial boundary, as an even contest reads on a four-band ladder.

## Decided

Option B (A-26, 2026-11-12: *0.4 per point; an even contest is even*), made the one opposed rule for the fight
and the argument by A-71 and A-79. The 2026-08-14 half-score form (option A) is the control arm only
(`opposition_rate` 0.5). A-79's own reading keeps a position hard to move (an even argument on a routine
matter fails 59%), and A-80 requires that entrenchment still moves the world: the control that shows it is the
entrenched-world arm carried by `28_CORE_scene_access_A_occupancy_and_precedence.md` gate row 12,
`28_CORE_scene_access_C_the_petition_that_waits.md` gate row 7 and `23_STORY_D_story_census_and_gate.md` (C3-C12).

## Exact edits

1. `modules/social_contest/roll.py::obstacle` — the opposition term is
   `sigma_leverage.opposed_ob(inp.opposition, inp.opposition_rate)`, where `inp.opposition` is the
   opponent's **skill score** (`pool.py::score`; no base dice, no practice addend, no seat; A-79,
   D-U1-02) and `opposition_rate` is a field of `queries/inputs.py::SocialContestInput`, filled by
   `seam/wrappers/sigma.py::_frame` from the fixture `opposition_rate` (control `0.5`, the 2026-08-14 form;
   live arm `dice_engine.MU_PER_DIE`, read from the owner, not typed). A NUMBER row in `hole_register.yaml`
   carries the sweep. The social composer leads with the even line `even_line(pool_add)` (OBS §2); the
   fight reads the same `opposed_ob` and has no even line. `engine/dice_engine/dice_engine.py::degree_from_net`'s
   docstring, which still records the 2026-08-14 opposed form, is rewritten in the same batch (B05;
   `OWED_TO_UNIFICATION.md` §A).
2. H-127's inversion: superseded by C-04. `obstacle_default` and its fixture are deleted (OBS §2,
   §4 step 1a); a person without a held score opposes with the untrained score `pool_default`, and where
   nobody stands opposite the stand-in is `opposed_ob(pool_default, opposition_rate)`. A person with a low
   held score is never easier to move than an unknown: a first rank is never below the untrained score
   (`max(untrained score, rank)`, U1 §4). No floor edit.

## Gate

`engine/season/tests/test_sc01_obstacle_ceiling.py` (exists): at the control arm the whole-dice table above
is no longer reproducible after A-5 lands (the sampler changes); the test's control reads the base tree's
closed form. At the live arm, on the re-centred sampler (A-5, A-6), equal skill scores 0, 2, 4, 7 meet a
`plain` row with P(margin ≥ 0) within 0.005 of 0.5 (lane 29's closed form: 50.0%), named
`engine/season/tests/test_sc_calibration_targets.py::test_equal_ranks_at_plain_are_even` (the file is
MISSING from the tree and is written as B05's first commit, U3 §6.1). `build_realm(0)` hashes equal on both
arms until a cast row holds a score.

## Falsifier

For equal pairs, P(Failure) rises 0.186 from s = 2 to s = 12 on the whole-dice roll (0.420 → 0.606) and
0.078 at the swept arm (0.358 → 0.436), both history. On the live arm: if equal skill scores at `plain`
read outside 0.5 ± 0.005 at any rank, or an opposition value moves with a practice addend, a seat or an
attribute, the rule is not what A-79 rules and this edit is wrong. What the rate does NOT fix, stated: a one-sided roll is never
complementary under a four-band ladder (6 against 3 succeeds 0.630 and 3 against 6 succeeds 0.124 at
the swept arm; the rest is Partial and Failure mass), so "swapping sides flips the result" needs a
two-sided roll, which is a different mechanism and is not proposed.

## NERS reading

- **N**: holds lateral (combat and mass battle are two-sided) and bottom-up (the dice's mean is the
  owner's); top-down it was a design choice, which Jordan made (A-26, A-79).
- **R**: B lets a player intuit "equal means even"; A is a defensible world-statement.
- **S**: *calculations consistent in methodology* — the one flag against A: the obstacle is priced in
  a unit (half-points) the pool is not (0.4 per die).
- **E**: one field and one fixture.

## Cost class

Edit (the ruling is given: A-26, A-79).

**Lands it and tier.** The B05 batch, at OBS §4 step 5 (the joint calibration with A-5, A-6, A-7):
`valoria-author` on `sonnet` (`high`) for the edit; the calibration read on `opus`; one `methodology-close`
for the batch. **Hash movers.** Every social roll against a person who holds a score, and the stand-in's
size at the live arm; re-pinned once with B05, said plainly.
