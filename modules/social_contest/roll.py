"""THE σ-LEVERAGE ROLL -- the `social_contest` module's entry (A-25; plan position `31a`).

A MODULE ENTRY: reached by the composition row whose target is `roll` below (`entry: verb_call`,
`verb: tell`), registered in `manifest.MODULE_ENTRIES` by the registrar at driver construction, and
called by the host adapter `seam/wrappers/sigma.py::resolve` -- the `@provider("contest",
"sigma_leverage")` the prize rows `a standing` and `a proposition` name.

It takes the host's typed input record and a seeded `rng`, and imports the dice engine and the record
type, nothing else. It never reads or writes `World`, holds no token and keeps no state between calls
(A-25). S27.4's refusal stays with the host adapter, which applies it to the pair this entry returns
(since step 14 the obstacle is composed here, so the host has no pair until the entry has run).

RULED, ED-SC-0037 (Jordan, 2026-09-09): *"we have the sigma leverage d10 resolver in engine to use."*
⚠ BOTH IMPORTS, AND THE SECOND ONE IS THE POINT: `roll_net` alone is the bare pool roll (a back-compat
shim over `dice_engine.roll_pool` that drops its `ob`); the σ layer is `net_boost`, the μ-shift
ED-884 / ED-934 ruled. The composition is the tree's own
(`systems/social_contest/sim/contest/resolver.py:302`): `net = roll_net(pool) + net_boost(lev, pool)`.

It returns a net/ob pair as a dict and NEVER a band: `seam/ladder.py` grades it by calling
`degree_from_net`, the single owner.

THE OBSTACLE IS THIS MODULE'S (v9 SC-01 step 14; ED-SC-0033 clause (3), *the obstacle has a single
owner*). `obstacle` below composes it from the record's raw operands; the host input builder carries
them and composes nothing (`seam/wrappers/sigma.py`'s own obstacle site was deleted at this step).
`modules/combat/core.py::ob_from_defender` is the precedent: the module that resolves the contest
derives what stands against it.
"""
from __future__ import annotations

import random
from typing import Optional

from engine.dice_engine.sigma_leverage import OB_MIN, net_boost, roll_net
from engine.season.queries.inputs import SocialContestInput


def obstacle(inp: SocialContestInput) -> float:
    """What stands against one matter's draw: the opposition's score halved, or the `H-127` stand-in
    where there is no score, BOUNDED ABOVE by the ceiling.

    ⚠ THE RULING IS `score/2 PLUS MODIFIERS` AND IT APPLIES TO A PERSON. Jordan, 2026-08-14, carried
    live in `dice_engine.degree_from_net`'s docstring: an opposed obstacle is *"their corresponding
    score/2 plus whatever specific modifiers exist for them in that instance"*. No instance modifier
    has a producer yet, so none is added. A record, a rung or a proposition has no score and takes
    `obstacle_default`. **NO "BASE Ob BY SCALE"** (Jordan, 2026-09-05).

    ⚠ THE CEILING (`H-213`, swept; Contradiction 3 of the proceedings reconciliation, resolved): a
    ceiling caps how hard a matter can get. M-7 fails without one -- at the 1D pool floor
    `p_success` is 0.0006 at Ob 3 and effectively zero above, and buying σ-advantage cannot lift it.
    It is NOT a pool floor (that would raise everyone's competence, a statement about people), and
    it is NOT advantage: advantage stays a μ-shift on the roll (`net_boost`), and the ceiling is one
    bound inside this composition, the same for every party, never applied by a caller to `base_Ob`.
    PER MATTER (ED-SC-0038's pick): this bounds ONE record's obstacle -- one matter's draw -- and
    nothing composes obstacles across a bundle. `None` is the uncapped control arm. A ceiling below
    the Ob minimum (`OB_MIN`, PP-232) is refused rather than read: it would breach the floor."""
    ob = float(inp.opposition) / 2.0 if inp.opposition is not None else float(inp.obstacle_default)
    ceiling = inp.obstacle_ceiling
    if ceiling is None:
        return ob
    if ceiling < OB_MIN:
        raise ValueError(f"obstacle_ceiling {ceiling!r} is below the Ob minimum {OB_MIN} (PP-232); "
                         "a ceiling under the floor is a bad arm, refused rather than read (H-213)")
    return min(ob, float(ceiling))


def roll(inp: SocialContestInput, rng: Optional[random.Random] = None) -> dict:
    """Roll one contested act. RESOLVED -> dict(status, module, resolver, pool, ob, net, leverage).

    The `rng` is a parameter and is never constructed here (`04 §C.12` rejection 4): the driver
    builds it from the run seed and the seam passes it down, as it passes `World`.
    `ob` is `obstacle(inp)`, this module's, and is returned so the host can grade the margin and
    apply S27.4 on the pair (`seam/wrappers/sigma.py::resolve`)."""
    net = roll_net(inp.pool, rng=rng) + net_boost(inp.leverage, inp.pool)
    return dict(status="RESOLVED", module="sigma_leverage", resolver="d10_sigma",
                pool=inp.pool, ob=obstacle(inp), net=net, leverage=inp.leverage)
