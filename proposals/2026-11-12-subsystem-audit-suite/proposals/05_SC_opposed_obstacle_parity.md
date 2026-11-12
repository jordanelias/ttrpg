# SC-P5 — what an equal opponent costs: the opposed obstacle against the dice's own mean

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-33) — un-held by Jordan's answer A-26 (0.4 per point: an even contest is even). The "HELD BACK" in the Status line below is superseded and this file is the carrier of the rate. Read with two things: the rate's one owner is `opposed_ob` (`U5c_SC_one_obstacle_form.md` §1), and it changes once, in that file's §4 step 5, together with A-5 (the bell curve), A-6 (score plus a base) and A-7 (two inputs), so the 0.4 is set against the re-centred sampler and not the whole-dice one this file measured.

## Status: PROPOSED — HELD BACK. It would overwrite a RULED item (Jordan, 2026-08-14: an opposed
obstacle is *"their corresponding score/2 plus whatever specific modifiers exist for them in that
instance"*). Listed in `audits/05_SC_audit.md` §11 with both options. Nothing here ratifies on merge.

Source: audit F-SC-03; hole rows H-288 (RULING), H-296, H-127 (the inversion).

## What it changes in `engine/season/` at runtime

Under option B, the obstacle a PERSON opponent contributes becomes `MU_PER_DIE × score` where it is
`score / 2` today. Every contested social act against a person who holds a score moves; in the
shipped realm that is nobody (all pools and oppositions fall to the defaults; `aperture 2 0`:
*"`argue`: pools rolled [2] over 9 actors"*), so the realm hash is unchanged until attributes are
seated (`build_realm(cast_attributes=True)`). Under option A nothing changes.

## The problem (measured, exact odds; `engine.dice_engine.sigma_leverage.band_odds`, shipped arm)

A die nets `MU_PER_DIE = 0.4` on average (`engine/dice_engine/dice_engine.py`); an opponent's point
of score costs `0.5`. So an actor of score `s` against an opponent of score `s` has a mean margin of
about `−0.1·s`, and skill makes an even contest worse for the one who acts:

| s (both sides) | Ob = s/2 | P(Failure) | P(Success or better) |
|---|---|---|---|
| 1 | 0.5 | 0.350 | 0.250 |
| 2 | 1.0 | 0.420 | 0.260 |
| 4 | 2.0 | 0.488 | 0.279 |
| 8 | 4.0 | 0.561 | 0.278 |
| 12 | 6.0 | 0.606 | 0.266 |

Swapping sides does not swap the result: 6 against 3 succeeds 0.570 of the time, 3 against 6 succeeds
0.052 (H-288's figures, reproduced). And the stand-in is worth a score of 4: an opponent holding a
score of 2 composes Ob 1.0, one holding none composes `obstacle_default` 2 (H-127's inversion,
reproduced: P(Failure) 0.42 against 0.74 at pool 2).

Control (the same pairs at `Ob = MU_PER_DIE × s`): P(Failure) 0.358 / 0.393 / 0.410 / 0.421 / 0.436
and P(Success or better) 0.324 / 0.372 / 0.394 / 0.407 / 0.423 at s = 2 / 4 / 6 / 8 / 12 — flat, and
near the Partial boundary, as an even contest reads on a four-band ladder.

## The two options

- **A — keep `score / 2` (the ruling as it stands).** A contested social act is an attempt against a
  defence, and the defence is deliberately worth more than the attack: the status quo holds, the
  person acted upon has the advantage, and the more skilled the pair the more it holds. Cost: no
  contest is "between equals"; an arrest, an argument and a hearing all favour whoever is acted on,
  by an amount that grows with skill (H-296's 20 % and 29 %).
- **B — `MU_PER_DIE × score` (this proposal).** The opponent's score is priced at what a die of it
  would net, so equal parties are even and the acting side wins by being better, by the room
  (`reception`, `proofs`) or by effort. Cost: it replaces a ruled constant with a derived one, and
  every authored expectation built on `score/2` (H-213's per-pool caps, `chance_floor`) is re-read.

They are different games: A is a world where moving anyone is uphill; B is one where contests are
symmetric and institutions (the room's terms) supply the asymmetry.

## Exact edits (option B only)

1. `modules/social_contest/roll.py::obstacle` — `ob = float(inp.opposition) * inp.opposition_rate`
   where `opposition_rate` is a new field of `queries/inputs.py::SocialContestInput`, filled by
   `seam/wrappers/sigma.py::_frame` from a fixture `opposition_rate` whose shipped value is `0.5`
   (option A, the control) and whose swept arm is `dice_engine.MU_PER_DIE` (read from the owner, not
   typed). A NUMBER row in `hole_register.yaml` carries the sweep.
2. H-127's inversion, independent of A/B and not ruled: in `seam/wrappers/sigma.py::_opposition_of`,
   a held score below `obstacle_default / opposition_rate` is not floored (the row's own stated
   revert is the floor). DECIDED: no floor — a person with a low score SHOULD be easier to move than
   an unknown; the defect is the stand-in's size, which is H-127's own swept value. No edit.

## Gate

`engine/season/tests/test_sc01_obstacle_ceiling.py`: at the swept arm, exact `band_odds` for equal
pairs s ∈ {2, 4, 8, 12} have P(Failure) within 0.10 of each other; at the control arm they reproduce
the table above. `build_realm(0)` hashes equal on both arms (nobody holds a score).

## Falsifier

For equal pairs, P(Failure) rises 0.186 from s = 2 to s = 12 today (0.420 → 0.606) and 0.078 at the
swept arm (0.358 → 0.436). If a re-run at the swept arm shows a rise above 0.10, the rate is not the
cause and this proposal is wrong. What the rate does NOT fix, stated: a one-sided roll is never
complementary under a four-band ladder (6 against 3 succeeds 0.630 and 3 against 6 succeeds 0.124 at
the swept arm; the rest is Partial and Failure mass), so "swapping sides flips the result" needs a
two-sided roll, which is a different mechanism and is not proposed.

## NERS reading

- **N**: holds lateral (combat and mass battle are two-sided) and bottom-up (the dice's mean is the
  owner's); top-down it is a design choice, which is why it is held back.
- **R**: B lets a player intuit "equal means even"; A is a defensible world-statement.
- **S**: *calculations consistent in methodology* — the one flag against A: the obstacle is priced in
  a unit (half-points) the pool is not (0.4 per die).
- **E**: one field and one fixture.

## Cost class

Edit, after a ruling.
