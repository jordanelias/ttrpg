"""THE σ-LEVERAGE ROLL -- the `social_contest` module's entry (A-25; plan position `31a`), and since v9
SC-01 step 15 the AUTOMATED MODE of the social contest scene's contest provider.

A MODULE ENTRY: reached by the composition row whose target is `roll` below (`entry: verb_call`,
`verb: tell`), registered in `manifest.MODULE_ENTRIES` by the registrar at driver construction, and
called by the host adapter `seam/wrappers/sigma.py::resolve` -- the `@provider("contest",
"social_contest")` the prize rows `a standing`, `a proposition` and `a matter` name (ED-SC-0033 clause (2)).

It takes the host's typed input record and a seeded `rng`, and imports the dice engine and the record
types, nothing else. It never reads or writes `World`, holds no token and keeps no state between calls
(A-25). It returns a `Margin` (`queries/inputs.py`) -- a margin, never a winner; the host adapter refuses
any other return. S27.4's refusal stays with the host adapter, which applies it to the pair this entry
returns (since step 14 the obstacle is composed here, so the host has no pair until the entry has run).

SC-05 (2026-10-16, step 15): THIS ROLL IS KEPT; THE KERNEL (`systems/social_contest/sim/contest/`) IS NOT ADOPTED
(the timing of its retirement is Jordan's, `SM-15`). The kernel draws on the GLOBAL stream rather than a seeded
`rng` (`04 §C.12`'s rejection 4 and `04 PART D row 35`'s per-act generator cannot be honoured without editing it),
returns a winner (side labels, no `net`/`ob` pair to hand `degree_from_net`) where the seam wants *a MARGIN, never a
winner* (`08_SEAM.md`; a degree adapter would be the second resolver S27.2 refuses), and reads a faculty, not the
host's record. The proceedings design's nested run (`21_RECONCILIATION.md` step 15) is not this entry either.

RULED, ED-SC-0037 (Jordan, 2026-09-09): *"we have the sigma leverage d10 resolver in engine to use."*
⚠ BOTH IMPORTS, AND THE SECOND ONE IS THE POINT: `roll_net_continuous` alone is the bare pool roll, the one
sampler every provider draws from (B05.02; A-5); the σ layer is `net_boost`, the μ-shift
ED-884 / ED-934 ruled. The composition is `net = roll_net_continuous(pool) + net_boost(lev, pool)`, a REAL
margin that the ladder quantises once (`dice_engine.degree_from_net`, `MARGIN_SCALE`); nothing here draws a d10 face.

It returns a net/ob pair as a `Margin` and NEVER a band: `seam/ladder.py` grades it by calling
`degree_from_net`, the single owner.

THE OBSTACLE IS THIS MODULE'S (v9 SC-01 step 14; ED-SC-0033 clause (3), *the obstacle has a single
owner*). `obstacle` below composes it from the record's raw operands; the host input builder carries
them and composes nothing (`seam/wrappers/sigma.py`).
`modules/combat/core.py::ob_from_defender` is the precedent: the module that resolves the contest
derives what stands against it.
"""
from __future__ import annotations

import functools
import random
from typing import Optional

from engine.dice_engine.sigma_leverage import M_MAX, OB_MIN, band_odds, even_line, net_boost, opposed_ob, roll_net_continuous, saturate
from engine.season.queries.inputs import Margin, SocialContestInput


@functools.lru_cache(maxsize=None)
def _chance_floor_cap(pool: float, ceiling: float) -> Optional[float]:
    """THE `chance_floor` CAP (CP-T01-06), SOLVED ON THE CLOSED FORM OF THE ONE SAMPLER (B05.02, DOE §1 row 3): the
    highest Ob at which `pool` still keeps the chance of Partial-or-better that `ceiling` leaves a ONE-DIE roll
    -- `band_odds(1, ceiling)`'s. The floor is therefore no new number: it is the fixed ceiling's own chance, and
    the cap at one die is that ceiling itself.

    THE CAP DOES NOT DEPEND ON THE BOOST (B05 close, antagonist): `net_boost` shifts the z of a roll by the same amount at every pool, so
    equating the pool's chance to the one-die floor gives one cap at any common leverage, in closed form `0.4 N + (c - 0.4) sqrt(N)` for pool
    `N` and ceiling `c` (2.0 / 3.06 / 3.97 / 4.80 at pools 1..4 for c = 2). Both chances are read at `net_boost(-M_MAX, pool)`, which makes the
    floor the one the soft cap leaves a hostile channel (-1.142 sigma sqrt(N) on `soft_cap(-1.5)`; a stack deeper than that is past the soft cap's
    own -1.5 limit and past this floor, unreachable at the shipped sources), and which moves where `None` is returned (a ceiling at which a
    one-die roll keeps no chance at all, about 6.2 at that boost): there is nothing to hold. At a swept ceiling of 3 the derived pairs at
    pools 1 and 2 (cap 3 and 4.48) are over S27.4's `multiple x pool` where `pool_floor` is swept to 0.

    The chance falls strictly as Ob rises, so the cap is found by bisection on `band_odds` (the one closed form);
    pure; cached on its two operands."""
    def chance(ob: float) -> float:
        return 1.0 - band_odds(pool, ob, net_boost(-M_MAX, pool))[0]
    floor = 1.0 - band_odds(1, ceiling, net_boost(-M_MAX, 1))[0]
    if floor <= 0.0:
        return None
    if pool == 1:
        return float(ceiling)                                  # the floor IS this pool's chance at the ceiling; bisection lands a few ulps over it
    lo, hi = 0.0, float(ceiling) + 2.0 * pool + 10.0           # chance(lo) > floor >= chance(hi)
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if chance(mid) >= floor:
            lo = mid
        else:
            hi = mid
    return lo


def obstacle(inp: SocialContestInput) -> tuple:
    """`(ob, terms)`: WHAT STANDS AGAINST ONE MATTER'S DRAW, AND EVERY TERM THAT MADE IT (B05.14; OBS §2; ED-SC-0033 clause (3), *the
    obstacle has a single owner*; Jordan, 2026-11-12, relayed: *"social contest obstacle is defined by the difficulty of the task and all
    associated modifiers"*). THE ONE FORM, at every site and every arm:

        hard  = even + difficulty + opposed_ob(opposition if a person opposes else pool_default, opposition_rate) + sum(raw_i x step_i)
        ob    = max(OB_MIN, bound(hard))                   # the ceiling (H-213, `ceiling_form`), then the floor
        terms = ((name, value), ...) in `rosters.yaml: obstacle_terms` order, + ("ceiling", -clip) and ("floor", +lift) where a bound acted

    `even` is `sigma_leverage.even_line(pool_add)`, the pool's expected net (an obstacle at it is an even contest); `difficulty` is the
    act's own (the size of its verb row's level); `opposition` is the one acted against: a PERSON opposite opposes with what he brings
    (his opposing attribute plus his skill score, A-79, A-137 -- the host reads it, `sigma.py::OBSTACLE_TERMS`), read at
    `sigma_leverage.opposed_ob` and `opposition_rate`, and where NO person stands opposite (a docket item, a Record, a site, a self-plea:
    nobody opposes himself) it is `opposed_ob(pool_default)` -- NEVER ABSENT, so no act's obstacle is zero for want of a counterparty
    and no verb is named here. `obstacle_operands` carries the members that are a raw operand times a step (the room's hostile `reception` and the `capability` circumstances).
    Every member is non-negative; a negative one raises `ValueError` (nothing lowers the obstacle). The values in `terms` sum to `ob`.

    ⚠ WHAT STANDS AGAINST THE ACT RAISES THE OBSTACLE AND NOTHING LOWERS IT; WHAT THE ACTOR BRINGS IS LEVERAGE (B05.17, PES-A; `ED-884`):
    a hostile bench is the roster's `reception` member, and a held proof or a friendly bench reaches the roll as named levels on the
    host's `leverage` (`rosters.yaml: advantage_sources`), so this function reads no room. Lane A's one step stays outside the roster
    (U-6): `forgery` (an examined document's quality, ADDED: a better forgery is harder to find, `22b` step 25).

    ⚠ THE CEILING (`H-213`): a ceiling caps how hard a matter can get. M-7 fails without one -- at the 1D pool floor `p_success` is
    0.0006 at Ob 3 and effectively zero above, and buying σ-advantage cannot lift it. It is NOT a pool floor (that would raise
    everyone's competence, a statement about people), and it is NOT advantage: advantage stays a μ-shift on the roll (`net_boost`), and the
    ceiling is one bound inside this composition, the same for every party. PER MATTER (ED-SC-0038's pick): this bounds ONE record's
    obstacle and nothing composes obstacles across a bundle. `None` is the uncapped control arm. THE SHIPPED ARM IS SOLVED PER POOL
    (CP-T01-06, `chance_floor`; `ceiling_per_pool`): from one die the cap is the highest Ob at which that pool keeps the chance of
    Partial-or-better the fixed ceiling leaves a one-die roll (`_chance_floor_cap`, solved on the closed form of the one sampler at the
    the closed form above; 2.0 at pool 1, 3.06 at pool 2, rising with the pool), so a larger pool is never worse for the
    cap, and at the shipped ceiling (2) S27.4's `ob > multiple x pool` never holds on a derived pair. Below one die the fixed ceiling
    applies. THE CEILING'S FORM (`ceiling_form`, B05.54; `16_PESSIMIST_DICE_soft_ceiling`): `hard` is the flat bound above (`min(ob, cap)`:
    a hostile room, a forgery or any other term cannot raise the obstacle past the cap, and past it they are all one value); `soft`
    bends the excess instead: `bound(ob) = ob` up to the knee (the fixed ceiling), `knee + saturate(ob - knee, cap - knee)` past it, so
    the obstacle stays strictly under the cap and a hostile term past the knee still changes the odds. At one die, or with no per-pool
    cap, `cap == knee` and both forms are `min`; the "cannot raise" sentences hold of the `hard` arm and of one die only. The bent bound
    is recorded as the `ceiling` term the fold adds and `ob` is that fold's last step, so the terms sum to `ob` exactly on this branch (on the hard branch the clip is `bounded - ob`, which sums back to `bounded` to within an ulp outside the Sterbenz range). A ceiling below the Ob minimum (`OB_MIN`, PP-232) is refused rather than read: it would breach the floor. THE FLOOR comes
    last: a composed obstacle under `OB_MIN` (a `plain` act against a person scoring 0) is lifted to it and the lift is the `floor` term.
    **NO "BASE Ob BY SCALE"** (Jordan, 2026-09-05)."""
    terms = [("even", even_line(inp.pool_add)),
             ("difficulty", float(inp.difficulty)),
             ("opposition", opposed_ob(inp.pool_default if inp.opposition is None else inp.opposition, inp.opposition_rate))]
    terms += [(name, float(raw) * float(step)) for name, raw, step in inp.obstacle_operands]
    negative = [(name, value) for name, value in terms if value < 0]
    if negative:
        raise ValueError(f"the obstacle's terms are never negative (nothing lowers it); got {negative}")
    ob = 0.0
    for _, value in terms:
        ob += value
    if inp.forgery_quality < 0:
        raise ValueError(f"the obstacle's terms are never negative (nothing lowers it); got forgery {inp.forgery_quality!r}")
    if inp.forgery_quality:
        terms.append(("forgery", float(inp.forgery_quality)))
    ob += float(inp.forgery_quality)
    ceiling = inp.obstacle_ceiling
    if ceiling is not None:
        if ceiling < OB_MIN:
            raise ValueError(f"obstacle_ceiling {ceiling!r} is below the Ob minimum {OB_MIN} (PP-232); "
                             "a ceiling under the floor is a bad arm, refused rather than read (H-213)")
        knee = float(ceiling)
        cap = knee
        if inp.ceiling_per_pool and inp.pool >= 1:
            cap = _chance_floor_cap(inp.pool, knee) or knee
        if inp.ceiling_form not in ("hard", "soft"):
            raise ValueError(f"ceiling_form {inp.ceiling_form!r} is not an arm the module reads ('hard', 'soft'); `soft_late` is named, not built (H-213)")
        if inp.ceiling_form == "hard" or cap <= knee or ob <= knee:
            bounded = min(ob, cap)
            clip = bounded - ob                  # flat: the bound itself is the new `ob`, as it was before the form existed
            new_ob = bounded
        else:
            bounded = knee + saturate(ob - knee, cap - knee)
            clip = bounded - ob
            new_ob = ob + clip                   # bent: the fold's own last step, so the terms sum to `ob` exactly (`bounded` is not dyadic)
        if bounded < ob:
            terms.append(("ceiling", clip))
            ob = new_ob
    if ob < OB_MIN:
        terms.append(("floor", OB_MIN - ob))
        ob = float(OB_MIN)
    return ob, tuple(terms)


def roll(inp: SocialContestInput, rng: Optional[random.Random] = None) -> Margin:
    """Roll one contested act -> `Margin(net, ob, terms)`.

    The `rng` is a parameter and is never constructed here (`04 §C.12` rejection 4): the driver
    builds it from the run seed and the seam passes it down, as it passes `World`.
    `ob` and `terms` are `obstacle(inp)`, this module's, and are returned so the host can grade the margin, apply S27.4 on the pair
    (`seam/wrappers/sigma.py::resolve`) and record why that obstacle was thrown at. The pool and leverage are the
    record's own, which the host already holds, so the margin does not carry them back."""
    ob, terms = obstacle(inp)
    return Margin(net=roll_net_continuous(inp.pool, rng=rng) + net_boost(inp.leverage, inp.pool), ob=ob, terms=terms)
