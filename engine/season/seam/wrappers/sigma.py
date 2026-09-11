"""THE σ-LEVERAGE PROVIDER — the seam's wrapper around the resolver Jordan named.

`04_CODE_ARCHITECTURE.md` §A.2:164 types `seam/wrappers/*` as writing *"nothing, ever"*, reading
*"the projection"*, returning *"a `Margin`"*, holding token *"none"*. This module is that row. It
DECIDES NOTHING: it derives a pool and an obstacle from what the actor and the subject genuinely
have, calls the σ layer, and returns the net/ob pair as a dict — the shape `combat_seam` already
returns and `degree_of` already grades. It NEVER returns a band; `seam/ladder.py` reads one by
calling `degree_from_net`, which is the single owner.

⚠ THIS DOCSTRING NAMES NO BAND, ON PURPOSE AND UNDER A MEASURED CONSTRAINT.
`tests/valoria/test_degree_ladder_single_owner.py`'s `_PRODUCES_BAND` scan reads raw file TEXT
INCLUDING DOCSTRINGS and flags any file where two or more band names appear in a produce-shape. A
prose line here spelling the four bands would redden a guard this module exists to stay clear of.
Keep it band-free.

RULED, ED-SC-0037. JORDAN, 2026-09-09, VERBATIM: *"we have the sigma leverage d10 resolver in
engine to use."* A third option neither of that row's two costed.

⚠⚠ **BOTH IMPORTS, AND THE SECOND ONE IS THE POINT.** `roll_net` ALONE APPLIES ZERO σ-LEVERAGE:
`sigma_leverage.py::roll_net` is a back-compat shim — *"The authoritative implementation is
dice_engine.roll_pool"* — that floors the pool, delegates, and **drops `roll_pool`'s `ob`
parameter**, which `roll_pool` accepts and grades on. Importing it alone is strictly `roll_pool`
minus the obstacle: **the bare pool roll ED-SC-0037 costed, wearing the ruled module's name.**
TERM-MATCHING ON THE MODULE IS NOT THE MECHANISM. The σ layer is `net_boost` — the μ-shift ED-884 /
ED-934 ruled, *"base_ob untouched, Ob floor never breached"* — and the composition is the tree's
own, at `systems/social_contest/sim/contest/resolver.py:302`:

    net = roll_net(pool) + net_boost(lev, pool)

⚠ **THE SEAM STILL DERIVES AN OBSTACLE, AND AN EARLIER READING OF ED-SC-0037 CLAIMED IT DID NOT.**
`sigma_leverage.eff_ob` CONSUMES `base_ob` and is *"DISPLAY ONLY (not the resolution value)"* by its
own docstring; `effective_ob` is a pure arg-order alias of it; `sigma_space_ob_shift` takes no
`base_ob` at all and returns a shift. The live composition has the CALLER supply `base_ob`. So
ED-SC-0037's cost 1 — *"the interim provider derives its own obstacle in-seam, which is an nth
obstacle site"* — is UNCHANGED, not answered, and `interim: true` on the prize row is what carries
it. ED-SC-0033 clause (3)'s single owner is the PROCEEDINGS SUBSYSTEM, not this module.

⚠ **THE PLACEMENT QUESTION, ADJUDICATED AT THE SITE RATHER THAN ASSUMED.** `04 §A.2:135` reads
*"one wrapper per **deferred subsystem**"*, and `sigma_leverage` is not a deferred subsystem — it is
an in-engine resolver under `engine/autoload/`. Two readings were available: **(i)** it is a wrapper
BY ROLE — it writes nothing, returns a margin, holds no token, which is exactly the `04:164` row, and
a module satisfying that contract IS that row whatever supplies the margin; **(ii)** §A.2's
enumeration is short by one and the finding goes on the ledger. **This unit takes (i).**
⚠ AND IT SATISFIES THREE OF THAT ROW'S FOUR COLUMNS, NOT FOUR. Column 3 is *"a `Margin`"* and this
returns a **dict**; column 2 is *"the projection"* and the signature takes `w`, a World.
`combat.resolve(w, …)` is the precedent for both — **and it is a precedent for the deviation, not
for conformance.** Typing `Margin` across both providers is a `seam/` item of its own; minting the
type for one provider while the other returns a dict would give the seam two return shapes, which
is worse than either.

⚠ THE PRECEDENT IS `seam/wrappers/combat.py` AND IT IS FOLLOWED, NOT REINVENTED: derive exactly what
the actor genuinely has, leave every other operand at its registered fixture, and return a typed gap
rather than fabricate a party.

⚠ THIS MODULE IMPORTS NOTHING FROM `systems/` AND INSERTS NO `sys.path`. It reaches
`engine.autoload.sigma_leverage` by dotted path, which the package already does for
`engine.autoload.dice_engine`, so NO entry is added to
`tests/valoria/test_engine_does_not_import_systems.py::PATH_SEAM_ALLOWED`. That set is shrink-only.
"""
from __future__ import annotations

import random
from typing import Any, Optional

from ...data.rosters import VERB_CAPABILITY
# ⚠ THE LEAF, NOT THE PACKAGE. `...manifest` re-exports from `registry.py`, which imports
# THIS module to register it — importing the package here closes that loop and the cycle
# guard counts it. `manifest/providers.py` imports nothing and is safe to reach from here.
from ...manifest.providers import provider

# RULED, ED-SC-0037. Both names; see the docstring for why `roll_net` alone is the bare pool roll.
from engine.autoload.sigma_leverage import net_boost, roll_net


def _pool_of(person: Any, verb: str, fx: Any) -> int:
    """Dice, from what the actor genuinely has. `03 §A.2` — *"Rank supplies dice and gates nothing"*.

    `VERB_CAPABILITY` maps a verb to the capability key it draws on; `Person.capability` is the
    person's own dict. ⚠ IT IS EMPTY ON EVERY CORPUS PERSON TODAY — one writer, and it zeroes it —
    so in practice this returns `pool_default` for everybody, which is why R-09 reads `partial`
    after this unit and not `met`: the roll varies by SEED and by FIXTURE, not by PERSON. It varies
    by person the day capability is written, and that is character development, out of this arc.
    ⚠ `08 §3` GIVES THE POLARITY: an `assumption` grade means *inject the default, declare the site,
    sweep three points* — never refuse the whole corpus for a missing key. `absent` is the grade
    that refuses, and this is not one."""
    key = VERB_CAPABILITY.get(verb)
    have = (getattr(person, "capability", None) or {}).get(key) if key else None
    return int(have if have is not None else fx.get("pool_default"))


def _obstacle_of(w: Any, subject: Optional[str], verb: str, fx: Any) -> float:
    """What stands against it.

    ⚠ THE RULING IS `score/2 PLUS MODIFIERS` AND IT APPLIES TO A PERSON, which is the only subject
    this can read a score off. Jordan, 2026-08-14, carried live in `dice_engine.py`: an opposed
    obstacle is *"their corresponding score/2 plus whatever specific modifiers exist for them in
    that instance"*. So when the subject IS a person, the obstacle is half the capability they bring
    to the same key; when it is a record, a rung or a proposition, no score exists and the registered
    fixture stands in.
    ⚠ **NO "BASE Ob BY SCALE"** (Jordan, 2026-09-05). The scale of the thing is not the obstacle.
    ⚠ AND THIS IS REGISTERED AS AN nth SITE IN A FAMILY THE TREE RECORDS AS DISAGREEING, not as a
    single owner arriving: `H-127` carries that, and ED-SC-0033 clause (3) names the proceedings
    subsystem as the owner this defers to."""
    if subject and subject in getattr(w, "persons", {}):
        key = VERB_CAPABILITY.get(verb)
        have = (w.persons[subject].capability or {}).get(key) if key else None
        if have is not None:
            return float(have) / 2.0
    return float(fx.get("obstacle_default"))


@provider("contest", "sigma_leverage")
def resolve(w: Any, claimants: list, causes: list, prize: Any, *,
            verb: str = "", subject: Optional[str] = None,
            rng: Optional[random.Random] = None) -> dict:
    """Roll for one contested act. Returns a net/ob pair, NEVER a band.

    RESOLVED -> dict(status, module, resolver, pool, ob, net, leverage)
    REFUSED  -> dict(status, why, pool, ob)   # S27.4: ob > obstacle_refusal_multiple x pool

    ⚠ THE RNG IS A PARAMETER AND IS NOT CONSTRUCTED HERE, WHICH IS `04 §C.12`'s REJECTION 4 BECOMING
    LOAD-BEARING FOR THE FIRST TIME: *"When R-09's producer is built … its generator must be
    constructed by the driver from the run seed and passed down exactly as `World` is. This is the
    one rejection that is not yet load-bearing, because no roll exists yet."* It exists now.
    ⚠ *"Threaded like `World`"* MEANS PASSED BY PARAMETER RATHER THAN REACHABLE BY A GLOBAL NAME —
    not one continuous stream. `04 PART D row 35` settles it: `H(seed, tick, subject, purpose)`, no
    counter, no service. A single stream threaded through a season would make every roll depend on
    the count of prior draws, so adding one contested verb would move every other verb's outcome.

    ⚠ S27.4 IS EVALUATED HERE, ON THE DERIVED PAIR, AND THE DRIVER'S OWN BRANCH KEEPS ITS JOB. The
    fold already refuses an act whose HAND-DECLARED `obstacle` exceeds the multiple; this refuses on
    the pair the provider derived. One rule, two inputs, and neither site re-evaluates the other's —
    which is §8's *the rule lives once* stated for a rule with two legitimate operands."""
    if not claimants:
        return dict(status="PARTY-GAP", why="a contest needs at least one claimant",
                    module="sigma_leverage")
    actor = w.persons.get(claimants[0]) if hasattr(w, "persons") else None
    if actor is None:
        return dict(status="PARTY-GAP", why=f"claimant is not a person: {claimants[0]!r}",
                    module="sigma_leverage")
    fx = w.fixtures
    pool = _pool_of(actor, verb, fx)
    ob = _obstacle_of(w, subject, verb, fx)
    mult = fx.get("obstacle_refusal_multiple")
    if ob > mult * max(pool, 0):
        return dict(status="REFUSED", why="S27.4", module="sigma_leverage",
                    resolver="d10_sigma", pool=pool, ob=ob)
    # THE COMPOSITION IS THE TREE'S OWN. `roll_net` is the discrete d10 engine; `net_boost` is the
    # μ-shift that makes this σ-leverage rather than a pool roll. `lev` is zero until something
    # supplies leverage — an `assumption` reading with no producer, and stating it as zero is the
    # honest form: a fabricated leverage would be a number nobody chose.
    lev = 0.0
    net = roll_net(pool, rng=rng) + net_boost(lev, pool)
    return dict(status="RESOLVED", module="sigma_leverage", resolver="d10_sigma",
                pool=pool, ob=ob, net=net, leverage=lev)
