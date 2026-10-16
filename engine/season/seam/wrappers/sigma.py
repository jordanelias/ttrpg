"""THE σ-LEVERAGE PROVIDER — the host adapter and the host INPUT BUILDER for the `social_contest`
module's roll (plan position `31a`, A-25).

`04_CODE_ARCHITECTURE.md` §A.2:182 types `seam/wrappers/*` as writing *"nothing, ever"*, reading
*"the projection"*, returning *"a `Margin`"*, holding token *"none"*. This module is that row. It
DECIDES NOTHING: `contest_input` (the host input builder) derives a pool and reads the obstacle's raw
operands from what the actor and the subject genuinely have and freezes them into
`queries/inputs.py::SocialContestInput`; `resolve` (the adapter) calls the module entry the prize row
names (`module_entry:`, registered in `manifest.MODULE_ENTRIES` from its composition row), keeps
S27.4's refusal on the pair it returns, and otherwise returns what it returned -- the net/ob pair as a
dict, the shape `combat_seam` already returns and `degree_of` already grades. It NEVER returns a band; `seam/ladder.py` reads one by calling `degree_from_net`,
which is the single owner. The roll itself is `modules/social_contest/roll.py`, reached by string.

⚠ THIS DOCSTRING NAMES NO BAND, ON PURPOSE AND UNDER A MEASURED CONSTRAINT.
`tests/valoria/test_degree_ladder_single_owner.py`'s `_PRODUCES_BAND` scan reads raw file TEXT
INCLUDING DOCSTRINGS and flags any file where two or more band names appear in a produce-shape. A
prose line here spelling the four bands would redden a guard this module exists to stay clear of.
Keep it band-free.

RULED, ED-SC-0037. JORDAN, 2026-09-09, VERBATIM: *"we have the sigma leverage d10 resolver in
engine to use."* A third option neither of that row's two costed.

⚠⚠ **BOTH IMPORTS, AND THE SECOND ONE IS THE POINT** -- they are the module's now
(`modules/social_contest/roll.py`), carried there with this reasoning. `roll_net` ALONE APPLIES ZERO σ-LEVERAGE:
`sigma_leverage.py::roll_net` is a back-compat shim — *"The authoritative implementation is
dice_engine.roll_pool"* — that floors the pool, delegates, and **drops `roll_pool`'s `ob`
parameter**, which `roll_pool` accepts and grades on. Importing it alone is strictly `roll_pool`
minus the obstacle: **the bare pool roll ED-SC-0037 costed, wearing the ruled module's name.**
TERM-MATCHING ON THE MODULE IS NOT THE MECHANISM. The σ layer is `net_boost` — the μ-shift ED-884 /
ED-934 ruled, *"base_ob untouched, Ob floor never breached"* — and the composition is the tree's
own, at `systems/social_contest/sim/contest/resolver.py:302`:

    net = roll_net(pool) + net_boost(lev, pool)

⚠ **THE HOST NO LONGER DERIVES AN OBSTACLE (v9 SC-01 step 14).** `sigma_leverage.eff_ob` CONSUMES
`base_ob` and is *"DISPLAY ONLY (not the resolution value)"* by its own docstring; `effective_ob` is a
pure arg-order alias of it; `sigma_space_ob_shift` takes no `base_ob` at all and returns a shift. So
the dice engine owns no obstacle, and ED-SC-0037's cost 1 — *"the interim provider derives its own
obstacle in-seam, which is an nth obstacle site"* — stood until step 14 deleted that site
(`_obstacle_of`): the obstacle is now composed by the social contest module
(`modules/social_contest/roll.py::obstacle`, ceiling included, `H-213`), ED-SC-0033 clause (3)'s
single owner. `interim: true` on the prize rows now carries clause (2) alone (the repoint, steps 13
+ 15).

⚠ **THE PLACEMENT QUESTION, ADJUDICATED AT THE SITE RATHER THAN ASSUMED.** `04 §A.2` read
*"one wrapper per **deferred subsystem**"* (that line was since amended, ED-IN-0284 and ED-IN-0285; see 04:147-151), and `sigma_leverage` is not a deferred subsystem — it is
an in-engine resolver under `engine/dice_engine/`. Two readings were available: **(i)** it is a wrapper
BY ROLE — it writes nothing, returns a margin, holds no token, which is exactly the `04:182` row, and
a module satisfying that contract IS that row whatever supplies the margin; **(ii)** §A.2's
enumeration is short by one and the finding goes on the ledger. **This unit takes (i).**
⚠ AND IT SATISFIES THREE OF THAT ROW'S FOUR COLUMNS, NOT FOUR. Column 3 is *"a `Margin`"* and this
returns a **dict**; column 2 is *"the projection"* and the signature takes `w`, a World -- the
ADAPTER's does; since `31a` the MODULE reads only the typed record `contest_input` builds.
`combat.resolve(w, …)` is the precedent for both — **and it is a precedent for the deviation, not
for conformance.** Typing `Margin` across both providers is a `seam/` item of its own; minting the
type for one provider while the other returns a dict would give the seam two return shapes, which
is worse than either.

⚠ THE PRECEDENT IS `seam/wrappers/combat.py` AND IT IS FOLLOWED, NOT REINVENTED: derive exactly what
the actor genuinely has, leave every other operand at its registered fixture, and return a typed gap
rather than fabricate a party.

⚠ THIS MODULE IMPORTS NOTHING FROM `systems/` OR `modules/` AND INSERTS NO `sys.path`. The roll is
reached by STRING: the composition row `social_contest.roll` names it, the registrar resolves it at
driver construction into `MODULE_ENTRIES`, and `resolve` below looks it up there by the role its
prize row names. NO entry is added to
`tests/valoria/test_engine_does_not_import_systems.py::PATH_SEAM_ALLOWED`. That set is shrink-only.
"""
from __future__ import annotations

import random
from typing import Any, Optional

from ...data.rosters import VERB_CAPABILITY
# ⚠ THE LEAF, NOT THE PACKAGE'S RE-EXPORT. `manifest/providers.py` imports nothing, so no import
# here closes a loop back into this package (`_entry.py` says the same of the entry lookup).
from ...manifest.providers import provider
from ...queries.inputs import SocialContestInput
from ._entry import entry_for

_PROVIDER = "sigma_leverage"


def _capability(entity: Any, verb: str):
    """What `entity` brings to `verb`'s capability key, or `None` if it brings nothing.

    ⚠ ONE READ, TWO CALLERS, AND THEY HAD IT TWICE. `_pool_of` and the opposition read (then
    `_obstacle_of`, deleted at v9 SC-01 step 14) each mapped the verb through `VERB_CAPABILITY`,
    guarded a missing key, and guarded a missing entry — the same three steps, differing only in
    WHOSE dict they read and what default they fall to. Those differences are the callers'; the read
    is not. Returning `None` rather than a default is what keeps it that way: the pool falls to
    `pool_default`, and the opposition's `None` reaches the module, which falls to
    `obstacle_default`; neither is this function's to know."""
    key = VERB_CAPABILITY.get(verb)
    if not key:
        return None
    return (getattr(entity, "capability", None) or {}).get(key)


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
    have = _capability(person, verb)
    return int(have if have is not None else fx.get("pool_default"))


def _opposition_of(w: Any, subject: Optional[str], verb: str) -> Optional[float]:
    """The subject's score on the verb's capability key, or `None` -- a READ, not an obstacle.

    ⚠ v9 SC-01 step 14 DELETED THIS MODULE'S OBSTACLE SITE (`_obstacle_of`; ED-SC-0033 clause (3),
    *the obstacle has a single owner*). What it composed -- `score/2`, the `obstacle_default`
    stand-in, and now the ceiling -- is `modules/social_contest/roll.py::obstacle`'s. What stays
    here is the half only the host can do: reading `World` for the score a PERSON subject brings
    (`None` for a record, a rung or a proposition, or a person with no entry)."""
    if subject and subject in w.persons:
        have = _capability(w.persons[subject], verb)
        if have is not None:
            return float(have)
    return None


def contest_input(w: Any, claimants: list, *, verb: str = "",
                  subject: Optional[str] = None) -> SocialContestInput:
    """THE HOST INPUT BUILDER (plan position `31a`, A-25): `World` -> the frozen record the roll reads.

    Reads `w.persons` (the actor, `claimants[0]`, and a person subject) and `w.fixtures`, and nothing
    else; the module that consumes the record never sees `World`. Its precondition is the adapter's
    PARTY-GAP checks (`resolve`, below): at least one claimant, and the first a person.
    `leverage` is zero until something supplies leverage -- an `assumption` reading with no
    producer, and stating it as zero is the honest form: a fabricated leverage would be a number
    nobody chose. The obstacle's operands are carried RAW (`opposition`, `obstacle_default`,
    `obstacle_ceiling`); the module composes them (step 14)."""
    fx = w.fixtures
    return SocialContestInput(
        pool=_pool_of(w.persons[claimants[0]], verb, fx),
        opposition=_opposition_of(w, subject, verb),
        obstacle_default=fx.get("obstacle_default"),
        obstacle_ceiling=fx.get("obstacle_ceiling"),
        obstacle_refusal_multiple=fx.get("obstacle_refusal_multiple"),
        leverage=0.0)


@provider("contest", _PROVIDER)
def resolve(w: Any, claimants: list, causes: list, prize: Any, *,
            verb: str = "", subject: Optional[str] = None,
            rng: Optional[random.Random] = None, rung: str = "") -> dict:
    """Roll for one contested act: build the record, refuse S27.4, call the module entry. Returns a
    net/ob pair, NEVER a band.

    RESOLVED -> dict(status, module, resolver, pool, ob, net, leverage)   # the entry's own return
    REFUSED  -> dict(status, why, pool, ob)   # S27.4: ob > obstacle_refusal_multiple x pool

    ⚠ THE ENTRY IS LOOKED UP BY THE ROLE THE PRIZE ROW NAMES (`module_entry:`), IN `MODULE_ENTRIES`.
    The registrar fills that table at driver construction from the composition row, and
    `manifest.check_contest_prizes` refuses construction when the two rows disagree; a call reaching
    here with the role unregistered (no driver constructed in the process) is `ENGINE-UNAVAILABLE`,
    `combat.py`'s typed refusal, never a direct import of the module.

    ⚠ `rung` IS ACCEPTED AND NOT USED HERE, THE SAME DELIBERATE NON-CHANGE AS IN `combat.py`
    (M4, `ED-IN-0279` clause (a)). A leverage roll derives its obstacle from the parties
    themselves, not from presence at a place.

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
    which is §8's *the rule lives once* stated for a rule with two legitimate operands.
    ⚠ SINCE v9 SC-01 STEP 14 IT IS EVALUATED AFTER THE ENTRY, on the pair the entry RETURNS: the
    obstacle is the module's (`roll.py::obstacle`, ED-SC-0033 clause (3)), so the host has no pair
    until the entry has run. A refused act's roll is discarded; its generator is the act's own
    (`H(seed, tick, subject, purpose)` above), so no other act's draw moves. Under the shipped
    ceiling (`H-213`, 2 = the multiple x the 1D floor) a derived pair with a pool of 1 or more is
    never refused here; only a pool below the floor is."""
    if not claimants:
        return dict(status="PARTY-GAP", why="a contest needs at least one claimant",
                    module=_PROVIDER)
    if w.persons.get(claimants[0]) is None:
        return dict(status="PARTY-GAP", why=f"claimant is not a person: {claimants[0]!r}",
                    module=_PROVIDER)
    inp = contest_input(w, claimants, verb=verb, subject=subject)
    entry, refusal = entry_for(prize, _PROVIDER)
    if entry is None:
        return refusal
    out = entry.fn(inp, rng)
    if out.get("status") == "RESOLVED" and out["ob"] > inp.obstacle_refusal_multiple * max(out["pool"], 0):
        return dict(status="REFUSED", why="S27.4", module=_PROVIDER,
                    resolver="d10_sigma", pool=out["pool"], ob=out["ob"])
    return out
