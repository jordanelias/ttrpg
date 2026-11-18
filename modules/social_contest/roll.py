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

from engine.dice_engine.sigma_leverage import M_MAX, OB_MIN, band_odds, even_line, net_boost, opposed_ob, roll_net_continuous
from engine.season.queries.inputs import Margin, SocialContestInput


@functools.lru_cache(maxsize=None)
def _chance_floor_cap(pool: float, ceiling: float) -> Optional[float]:
    """THE `chance_floor` CAP (CP-T01-06), SOLVED ON THE CLOSED FORM OF THE ONE SAMPLER (B05.02, DOE §1 row 3): the
    highest Ob at which `pool` still keeps the chance of Partial-or-better that `ceiling` leaves a ONE-DIE roll
    -- `band_odds(1, ceiling)`'s. The floor is therefore no new number: it is the fixed ceiling's own chance, and
    the cap at one die is that ceiling itself.

    SOLVED AT THE LARGEST LAWFUL DISADVANTAGE, NOT "AT NO ADVANTAGE" (closes the pessimist's P-iii (c)): both the
    one-die floor and the pool's chance are read with the roll's boost at `net_boost(-M_MAX, pool)`, the soft
    cap's own floor on a hostile channel, so a signed leverage channel can never carry a roll through the floor:
    under the cap, no pool's chance of Partial-or-better at `-M_MAX` falls below the one-die chance at the
    ceiling at `-M_MAX`. Returns `None` where the floor is 0 (a ceiling at which a one-die roll keeps no chance
    at all): there is nothing to hold.

    The chance falls strictly as Ob rises, so the cap is found by bisection on `band_odds` (the one closed form);
    pure; cached on its two operands."""
    def chance(ob: float) -> float:
        return 1.0 - band_odds(pool, ob, net_boost(-M_MAX, pool))[0]
    floor = 1.0 - band_odds(1, ceiling, net_boost(-M_MAX, 1))[0]
    if floor <= 0.0:
        return None
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
        ob    = max(OB_MIN, min(hard, cap(pool)))          # the ceiling (H-213), then the floor
        terms = ((name, value), ...) in `rosters.yaml: obstacle_terms` order, + ("ceiling", -clip) and ("floor", +lift) where a bound acted

    `even` is `sigma_leverage.even_line(pool_add)`, the pool's expected net (an obstacle at it is an even contest); `difficulty` is the
    act's own (the size of its verb row's level); `opposition` is the one acted against: a PERSON opposite opposes with what he brings
    (his opposing attribute plus his skill score, A-79, A-137 -- the host reads it, `sigma.py::OBSTACLE_TERMS`), read at
    `sigma_leverage.opposed_ob` and `opposition_rate`, and where NO person stands opposite (a docket item, a Record, a site, a self-plea:
    nobody opposes himself) it is `opposed_ob(pool_default)` -- NEVER ABSENT, so no act's obstacle is zero for want of a counterparty
    and no verb is named here. `obstacle_operands` carries the members that are a raw operand times a step (none ship at step 1a).
    Every member is non-negative; a negative one raises `ValueError` (nothing lowers the obstacle). The values in `terms` sum to `ob`.

    ⚠ LANE A'S TWO STEPS STAY WHERE THEY WERE, OUTSIDE THE ROSTER (U-6), SO THE CONTROL IS EXACT: after the members, `room` (minus the
    bench's reception and the speaker's proofs, never taking the obstacle below `OB_MIN` or below a base already under it -- a bench
    disposed toward the speaker, and proofs his opponent cannot mirror, make the matter easier; one against him makes it harder, v9 SC-02
    `22a`) and `forgery` (an examined document's quality, ADDED: a better forgery is harder to find, `22b` step 25). `room` is the one
    entry that may be negative; OBS §4 step 1b moves its favourable half to leverage.

    ⚠ THE CEILING (`H-213`): a ceiling caps how hard a matter can get. M-7 fails without one -- at the 1D pool floor `p_success` is
    0.0006 at Ob 3 and effectively zero above, and buying σ-advantage cannot lift it. It is NOT a pool floor (that would raise
    everyone's competence, a statement about people), and it is NOT advantage: advantage stays a μ-shift on the roll (`net_boost`), and the
    ceiling is one bound inside this composition, the same for every party. PER MATTER (ED-SC-0038's pick): this bounds ONE record's
    obstacle and nothing composes obstacles across a bundle. `None` is the uncapped control arm. THE SHIPPED ARM IS SOLVED PER POOL
    (CP-T01-06, `chance_floor`; `ceiling_per_pool`): from one die the cap is the highest Ob at which that pool keeps the chance of
    Partial-or-better the fixed ceiling leaves a one-die roll (`_chance_floor_cap`, solved on the closed form of the one sampler at the
    largest lawful disadvantage, `-M_MAX`; 2.0 at pool 1, 3.06 at pool 2, rising with the pool), so a larger pool is never worse for the
    cap, and at the shipped ceiling (2) S27.4's `ob > multiple x pool` never holds on a derived pair. Below one die the fixed ceiling
    applies. A ceiling below the Ob minimum (`OB_MIN`, PP-232) is refused rather than read: it would breach the floor. THE FLOOR comes
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
    room = float(inp.reception_gain) * float(inp.reception) + float(inp.proof_step) * float(inp.proofs)
    if room:
        before = ob
        ob = max(ob - room, min(ob, float(OB_MIN))) if room > 0 else ob - room
        terms.append(("room", ob - before))
    if inp.forgery_quality:
        terms.append(("forgery", float(inp.forgery_quality)))
    ob += float(inp.forgery_quality)
    ceiling = inp.obstacle_ceiling
    if ceiling is not None:
        if ceiling < OB_MIN:
            raise ValueError(f"obstacle_ceiling {ceiling!r} is below the Ob minimum {OB_MIN} (PP-232); "
                             "a ceiling under the floor is a bad arm, refused rather than read (H-213)")
        cap = float(ceiling)
        if inp.ceiling_per_pool and inp.pool >= 1:
            cap = _chance_floor_cap(inp.pool, cap) or cap
        if ob > cap:
            terms.append(("ceiling", cap - ob))
            ob = cap
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
