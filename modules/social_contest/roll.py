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
⚠ BOTH IMPORTS, AND THE SECOND ONE IS THE POINT: `roll_net` alone is the bare pool roll (a back-compat
shim over `dice_engine.roll_pool` that drops its `ob`); the σ layer is `net_boost`, the μ-shift
ED-884 / ED-934 ruled. The composition is the tree's own
(`systems/social_contest/sim/contest/resolver.py:302`): `net = roll_net(pool) + net_boost(lev, pool)`.

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

from engine.dice_engine.sigma_leverage import OB_MIN, band_odds, net_boost, roll_net
from engine.season.queries.inputs import Margin, SocialContestInput


@functools.lru_cache(maxsize=None)
def _chance_floor_cap(pool: float, ceiling: float) -> Optional[float]:
    """THE `chance_floor` CAP (CP-T01-06): the highest Ob at which `pool` still keeps the chance of
    Partial-or-better that `ceiling` leaves a ONE-DIE roll -- `band_odds(1, ceiling)`'s, 10 % at the
    shipped 2. The floor is therefore no new number: it is the fixed ceiling's own chance, and the cap
    at one die is that ceiling itself.

    Exact, not a whole step: with no boost the odds at an Ob between two whole Obs are the straight
    line between the two whole-Ob odds (the fraction rule, `settle_margin`), so the cap is read off the
    segment where the chance crosses the floor. The chance only falls as Ob rises and the floor is
    above zero, so the walk from `OB_MIN` stops. Returns `None` where the floor is 0 (a ceiling at
    which a one-die roll keeps no chance, 3 and over): there is nothing to hold. Pure; cached on its
    two operands."""
    def chance(ob: float) -> float:
        return 1.0 - band_odds(pool, ob)[0]
    floor = 1.0 - band_odds(1, ceiling)[0]
    if floor <= 0.0:
        return None
    k = float(OB_MIN)
    while chance(k + 1) >= floor:
        k += 1
    above, below = chance(k), chance(k + 1)
    return k + (above - floor) / (above - below)


def obstacle(inp: SocialContestInput) -> float:
    """What stands against one matter's draw, BOUNDED ABOVE by the ceiling: `obstacle_terms`'s first member. On the
    shipped task arm (`inp.difficulty` set, B11 lane A) the task's difficulty plus the opposing person's score halved
    where a person opposes, and the difficulty alone where none does; on the control arm (`difficulty` `None`) the
    opposition's score halved, or the `H-127` stand-in where there is no score.

    ⚠ THE RULING IS `score/2 PLUS MODIFIERS` AND IT APPLIES TO A PERSON. Jordan, 2026-08-14, carried
    live in `dice_engine.degree_from_net`'s docstring: an opposed obstacle is *"their corresponding
    score/2 plus whatever specific modifiers exist for them in that instance"*. The instance
    modifiers are the room's terms and an examined document's forgery quality, below (and, on the task arm, the task's
    difficulty). A record, a rung or a proposition has no score: on the task arm it takes the difficulty alone, on the
    control arm `obstacle_default`. **NO "BASE Ob BY SCALE"** (Jordan, 2026-09-05).

    ⚠ THE CEILING (`H-213`): a
    ceiling caps how hard a matter can get. M-7 fails without one -- at the 1D pool floor
    `p_success` is 0.0006 at Ob 3 and effectively zero above, and buying σ-advantage cannot lift it.
    It is NOT a pool floor (that would raise everyone's competence, a statement about people), and
    it is NOT advantage: advantage stays a μ-shift on the roll (`net_boost`), and the ceiling is one
    bound inside this composition, the same for every party, never applied by a caller to `base_Ob`.
    PER MATTER (ED-SC-0038's pick): this bounds ONE record's obstacle -- one matter's draw -- and
    nothing composes obstacles across a bundle. `None` is the uncapped control arm. THE SHIPPED ARM IS
    SOLVED PER POOL (CP-T01-06, `chance_floor`; `ceiling_per_pool`): from one die the cap is the highest
    Ob at which that pool keeps the chance of Partial-or-better the fixed ceiling leaves a one-die roll
    (`_chance_floor_cap`; 2.0 at pool 1, 2.842 at pool 2, rising with the pool), so, AT NO ADVANTAGE, a
    larger pool is never worse for the cap (it is an equality: each pool's chance at its own cap is the
    same 10 %), and at the shipped ceiling (2) S27.4's `ob > multiple x pool` never holds on a derived
    pair. With an `effort` boost the chance at each pool's own cap is NOT monotone in the pool (the
    boost grows with the root of the pool while the cap sits where the unboosted chance is 10 %);
    and a ceiling of 3 or more has floor 0 and falls back to the fixed ceiling, which is tighter than the
    solved cap at ceiling 2 for pools of 3 and up (H-213). Below one
    die the fixed ceiling applies. `ceiling_per_pool` off is the
    fixed arm, which the sentences below describe at ceiling 2. A ceiling below
    the Ob minimum (`OB_MIN`, PP-232) is refused rather than read: it would breach the floor. Nothing floors the composed obstacle itself: a score under 2 composes
    below `OB_MIN` (score 1 gives 0.5).

    ⚠ THE ROOM'S TERMS ARE THE INSTANCE MODIFIERS THE RULING NAMES (v9 SC-02 `22a`; proceedings
    `19_PLAN.md` steps 17, 18, 20): `room = reception_gain · reception + proof_step · proofs`, both read
    raw off the record, is SUBTRACTED -- a bench disposed toward the speaker, and proofs his opponent
    cannot mirror, make the matter easier; a bench against him makes it harder. A room's favour never
    takes the obstacle below `OB_MIN` (or below a base already under it): it moves the obstacle, it
    does not abolish it. The ceiling still bounds the result, so under the fixed `H-213` ceiling (2,
    the same as `obstacle_default`) a hostile room cannot raise a defaulted obstacle -- stated, not
    hidden; under the per-pool arm it can, up to that pool's cap (a pool of 2 reaches 2.842). THE FAVOURABLE HALF IS CLIPPED THE SAME WAY: the ceiling is applied after the room, so
    against a strong opposition (base above the ceiling) a favourable room bites only where it takes
    the obstacle below the ceiling (`room > base - ceiling`); a room of +1.5 against a base of 4 under
    a ceiling of 2 changes nothing.

    ⚠ AND AN EXAMINED DOCUMENT'S FORGERY QUALITY IS ONE MORE (v9 SC-02 `22b` step 25; `19_PLAN.md` step
    25, *"examination contests the record's forgery quality"*): `forgery_quality`, read raw off the
    Record an inquiry examines, is ADDED -- a better forgery is harder to find -- before the ceiling,
    which bounds it as it bounds a hostile room. `0` (a genuine document, or the `H-210` control arm)
    adds nothing. Under the fixed `H-213` ceiling (2 = `obstacle_default`) a forgery cannot raise a
    defaulted inquiry's obstacle: the quality reaches the roll only where the ceiling sits above the
    default (the uncapped `None` arm, `3`, or a pool whose solved cap is above 2) -- stated, not hidden."""
    return obstacle_terms(inp)[0]


def obstacle_terms(inp: SocialContestInput) -> tuple:
    """`(ob, terms)`: THE OBSTACLE AND EVERY TERM THAT MADE IT, NAMED (B11 lane A; Jordan, 2026-11-12, relayed: *"social
    contest obstacle is defined by the difficulty of the task and all associated modifiers"*). `obstacle` returns the
    first; the host writes the second on the roll's record (`seam/wrappers/sigma.py::resolve`, `ob_terms`), so why a
    given Ob was thrown at can be read after the draw. `ob` is composed in sequence, never as `sum(terms)`.

    THE TASK ARM (`inp.difficulty` set, shipped): `difficulty` (the task's own, `rosters.yaml: task_difficulty`) PLUS
    `opposition` -- the opposing person's score halved, the RULED term (2026-08-14), kept as one modifier and unchanged
    -- where a person opposes; a task no person opposes (an inquiry, a contest against a Record) has no such term and
    no stand-in. THE CONTROL ARM (`inp.difficulty is None`): `opposition`, or `stand_in` (`obstacle_default`) where
    there is no score. THEN, on both: `room` (minus the bench's reception and the speaker's
    proofs, floored), `forgery` (an examined document's quality) and `ceiling` (the H-213 cap's cut, zero or
    negative). A term that does not apply is absent from the record."""
    terms: dict = {}
    if inp.difficulty is not None:
        ob = float(inp.difficulty)
        terms["difficulty"] = ob
        if inp.opposition is not None:
            half = float(inp.opposition) / 2.0
            terms["opposition"] = half
            ob = ob + half
    elif inp.opposition is not None:
        ob = float(inp.opposition) / 2.0
        terms["opposition"] = ob
    else:
        ob = float(inp.obstacle_default)
        terms["stand_in"] = ob
    room = float(inp.reception_gain) * float(inp.reception) + float(inp.proof_step) * float(inp.proofs)
    if room:
        before = ob
        ob = max(ob - room, min(ob, float(OB_MIN))) if room > 0 else ob - room
        terms["room"] = ob - before
    if inp.forgery_quality:
        terms["forgery"] = float(inp.forgery_quality)
    ob += float(inp.forgery_quality)
    ceiling = inp.obstacle_ceiling
    if ceiling is None:
        return ob, terms
    if ceiling < OB_MIN:
        raise ValueError(f"obstacle_ceiling {ceiling!r} is below the Ob minimum {OB_MIN} (PP-232); "
                         "a ceiling under the floor is a bad arm, refused rather than read (H-213)")
    cap = float(ceiling)
    if inp.ceiling_per_pool and inp.pool >= 1:
        cap = _chance_floor_cap(inp.pool, cap) or cap
    if ob > cap:
        terms["ceiling"] = cap - ob
    return min(ob, cap), terms


def roll(inp: SocialContestInput, rng: Optional[random.Random] = None) -> Margin:
    """Roll one contested act -> `Margin(net, ob)`.

    The `rng` is a parameter and is never constructed here (`04 §C.12` rejection 4): the driver
    builds it from the run seed and the seam passes it down, as it passes `World`.
    `ob` is `obstacle(inp)`, this module's, and is returned so the host can grade the margin and
    apply S27.4 on the pair (`seam/wrappers/sigma.py::resolve`). The pool and leverage are the
    record's own, which the host already holds, so the margin does not carry them back."""
    return Margin(net=roll_net(inp.pool, rng=rng) + net_boost(inp.leverage, inp.pool),
                  ob=obstacle(inp))
