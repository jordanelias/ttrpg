"""THE σ-LEVERAGE ROLL -- the `social_contest` module's entry (A-25; plan position `31a`).

A MODULE ENTRY: reached by the composition row whose target is `roll` below (`entry: verb_call`,
`verb: tell`), registered in `manifest.MODULE_ENTRIES` by the registrar at driver construction, and
called by the host adapter `seam/wrappers/sigma.py::resolve` -- the `@provider("contest",
"sigma_leverage")` the prize rows `a standing` and `a proposition` name.

It takes the host's typed input record and a seeded `rng`, and imports the dice engine and the record
type, nothing else. It never reads or writes `World`, holds no token and keeps no state between calls
(A-25). S27.4's refusal stays with the host adapter, so a refused pair never reaches it.

RULED, ED-SC-0037 (Jordan, 2026-09-09): *"we have the sigma leverage d10 resolver in engine to use."*
⚠ BOTH IMPORTS, AND THE SECOND ONE IS THE POINT: `roll_net` alone is the bare pool roll (a back-compat
shim over `dice_engine.roll_pool` that drops its `ob`); the σ layer is `net_boost`, the μ-shift
ED-884 / ED-934 ruled. The composition is the tree's own
(`systems/social_contest/sim/contest/resolver.py:302`): `net = roll_net(pool) + net_boost(lev, pool)`.

It returns a net/ob pair as a dict and NEVER a band: `seam/ladder.py` grades it by calling
`degree_from_net`, the single owner.
"""
from __future__ import annotations

import random
from typing import Optional

from engine.dice_engine.sigma_leverage import net_boost, roll_net
from engine.season.queries.inputs import SocialContestInput


def roll(inp: SocialContestInput, rng: Optional[random.Random] = None) -> dict:
    """Roll one contested act. RESOLVED -> dict(status, module, resolver, pool, ob, net, leverage).

    The `rng` is a parameter and is never constructed here (`04 §C.12` rejection 4): the driver
    builds it from the run seed and the seam passes it down, as it passes `World`."""
    net = roll_net(inp.pool, rng=rng) + net_boost(inp.leverage, inp.pool)
    return dict(status="RESOLVED", module="sigma_leverage", resolver="d10_sigma",
                pool=inp.pool, ob=inp.ob, net=net, leverage=inp.leverage)
