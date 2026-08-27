"""The contest's declared modification of the degree ladder, injected by the wrapper (ED-SC-0032).

WHY THIS FILE EXISTS AND WHY IT IS HERE RATHER THAN IN `engine/`.
Jordan, 2026-08-15, verbatim: *"systems should not need different degree bands. it should be
consistent in application. if a system does require any modification or extension, then the
wrapper needs to inject the engine in such a manner that it can be modified cleanly."*

ED-SC-0031 did the first half — the contest's bands became `dice_engine.degree_from_net`'s. It
did NOT do the second: the pool-aware de-saturation survived as a hard-coded post-filter inside
`engine/autoload/sigma_leverage.py`, which meant (a) the ENGINE carried a rule that belongs to
one subsystem, and (b) there was no seam, so the discipline holding it to "demote only" was a
comment rather than a contract. Both halves are fixed here and in `dice_engine.BandExtension`:

  * the rule MOVED OUT of the engine into the subsystem that owns it, taking `OVERWHELM_SIGMA`
    with it — that constant is cited to the contest groundup engine and was never general;
  * the constraint became STRUCTURAL. `may_overwhelm` returns a bool consulted in exactly one
    branch of the ladder. There is no signature by which this class could promote a band, move
    the Partial window, or touch Failure.

WHAT THE RULE IS, AND WHY THE CONTEST NEEDS IT.
Overwhelming requires clearing `pool mean + 0.85 sigma` — roughly "beat your own pool's mean by
0.85 sigma" — on top of the owner's margin bar. Without it the top band SATURATES as pools grow:
under the owner's ladder alone, P(Overwhelming) at pool 30 is 0.95, and `resolver._advance` uses
the degree as a numeric MAGNITUDE, so a saturating top band collapses the whole persuasion track.
With it the rate is flat at `1 - Phi(0.85)` wherever it binds.

WHERE IT BINDS is a function of the obstacle, not a constant: the crossover is the smallest pool
whose bar exceeds `ob + 3`, which is pool 6 at ob 1.0, pool 8 at ob 2.0, pool 10 at ob 3.0.
Below that the owner's fixed margin bar is the stricter of the two and this extension is inert.

⚠ A CONSEQUENCE JORDAN RULED ON DIRECTLY (2026-08-27), so it is settled rather than open.
Under the owner's ladder a pool-2 contest can never resolve Overwhelming at all — it would need
net >= 5 from two dice, whose maximum is 4. Jordan, verbatim: *"yes accept. if you don't have
enough dice you don't have enough dice."* ACCEPTED. Do not reintroduce a small-pool carve-out.
"""
from __future__ import annotations

import math

from engine.autoload.dice_engine import BandExtension
from engine.autoload.sigma_leverage import MU_PER_DIE, SD_PER_DIE

# De-saturation bar coefficient. MOVED here from engine/autoload/sigma_leverage.py 2026-08-27
# (ED-SC-0032) — it is a contest constant and its own citation says so.
# [canonical: audit/2026-06-03-contest-groundup/engine.py §degree]
OVERWHELM_SIGMA = 0.85


def overwhelm_bar(pool: float) -> float:
    """The bar a net must clear for Overwhelming, at this pool size. ONE definition.

    `max(1, pool)` floors only the sqrt term, not the mean term. That asymmetry is carried over
    VERBATIM from the retired implementation rather than quietly tidied: it makes no difference
    for any reachable pool (the live floor is `Pool.size`, which is >= 5), and changing it would
    be a behaviour change wearing a refactor's clothes.
    """
    return MU_PER_DIE * pool + OVERWHELM_SIGMA * SD_PER_DIE * math.sqrt(max(1, pool))


class PoolDesaturation(BandExtension):
    """Overwhelming additionally requires clearing the pool-scaled bar.

    Stateless and shared: the pool arrives per call as `context`, because it is per-exchange
    state, not per-contest configuration. A per-pool instance would make the injected object
    change identity every roll, which is exactly the kind of thing that makes an injected policy
    hard to reason about in a trace.
    """

    name = "contest:pool-desaturation"

    #: The one context key this extension reads. Declared so the engine can REFUSE any other:
    #: `pool=None` means abstain, so an undeclared or misspelled key would otherwise be swallowed
    #: by `**context` and turn a Success into an Overwhelming with no error. See
    #: `BandExtension.validate_context`.
    context_keys = ("pool",)

    def may_overwhelm(self, net, ob, pool=None, **context) -> bool:
        if pool is None:
            # No pool supplied means the caller declined to give the extension the context it
            # needs. It abstains rather than guessing — the owner's ladder stands unmodified.
            return True
        return net >= overwhelm_bar(pool)


#: The instance the contest wrapper injects. One object, so `is` comparisons in tests and traces
#: are meaningful and a stray second copy is visible.
CONTEST_DEGREE_EXTENSION = PoolDesaturation()


def owner_overwhelming_margin() -> float:
    """The owner's Overwhelming margin, READ OFF the owner rather than typed as a literal.

    A test that wants "the bar the owner sets" must not spell `3` — that is a local re-decision
    of a band inside the very machinery that exists to stop local re-decisions of bands. Probing
    `degree_from_net` for the smallest quarter-step margin it bands Overwhelming means a future
    change to the ladder moves every caller with it.
    """
    from engine.autoload.dice_engine import Degree, degree_from_net

    return next(m / 4 for m in range(0, 41)
                if degree_from_net(m / 4, 0.0) is Degree.OVERWHELMING)


def crossover_pool(ob: float) -> int | None:
    """Smallest integer pool at which this extension can demote, for this `ob`. None if never.

    The search ceiling is DERIVED, not chosen: `overwhelm_bar(p) >= MU_PER_DIE * p`, so the
    crossover cannot exceed `ceil(owner_bar / MU_PER_DIE)`. An earlier version took an arbitrary
    `limit=200`, which the anti-fabrication gate correctly refused.
    """
    owner_bar = ob + owner_overwhelming_margin()
    if owner_bar < 0:
        return 1
    ceiling = math.ceil(owner_bar / MU_PER_DIE) + 1
    for pool in range(1, ceiling + 1):
        if overwhelm_bar(pool) > owner_bar:
            return pool
    return None


def degree(net: float, ob: float, pool: float | None = None) -> int:
    """The contest's ordinal degree: the OWNER's ladder with this extension injected.

    MOVED here from `engine/autoload/sigma_leverage.py` 2026-08-27 (ED-SC-0032). The function is
    unchanged in behaviour and changed in ADDRESS, which is the whole point — the engine no
    longer carries a contest-specific rule, and this one goes through the declared seam rather
    than post-filtering the engine's answer behind its back.

    The kernel needs an INT rather than a `Degree`, because `resolver._advance` uses the band as
    a numeric magnitude. That need is exactly how this surface justified keeping a private ladder
    for so long, so the encoding is read off `dice_engine.DEGREE_ORDINAL` — the owner's — and not
    re-decided here.

    `pool=None` means the extension abstains and the owner's ladder stands unmodified.
    """
    from engine.autoload.dice_engine import DEGREE_ORDINAL, degree_from_net

    return DEGREE_ORDINAL[degree_from_net(
        net, ob, extension=CONTEST_DEGREE_EXTENSION, pool=pool)]
