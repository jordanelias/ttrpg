"""THE σ-LEVERAGE ROLL -- the `social_contest` module's entry (A-25; plan position `31a`), and since v9
SC-01 step 15 the AUTOMATED MODE of the social contest scene's contest provider.

A MODULE ENTRY: reached by the composition row whose target is `roll` below (`entry: verb_call`,
`verb: tell`), registered in `manifest.MODULE_ENTRIES` by the registrar at driver construction, and
called by the host adapter `seam/wrappers/sigma.py::resolve` -- the `@provider("contest",
"social_contest")` the prize rows `a standing`, `a proposition` and `a matter` name (repointed from the
interim `sigma_leverage` at steps 13 + 15, ED-SC-0033 clause (2)).

It takes the host's typed input record and a seeded `rng`, and imports the dice engine and the record
types, nothing else. It never reads or writes `World`, holds no token and keeps no state between calls
(A-25). It returns a `Margin` (`queries/inputs.py`) -- a margin, never a winner; the host adapter refuses
any other return. S27.4's refusal stays with the host adapter, which applies it to the pair this entry
returns (since step 14 the obstacle is composed here, so the host has no pair until the entry has run).

SC-05, MEASURED AT STEP 15 (2026-10-16, base `29af7354`): KEEP THIS ROLL, DO NOT ADOPT THE KERNEL
(`systems/social_contest/sim/contest/`, evaluated, not deleted; the timing of its retirement is Jordan's,
`SM-15`). Read by importing `wrapper.build_contest` / `resolve_contest` and calling them, 200 seeds per
proceeding:
  * NO RNG PARAMETER. `resolve_contest`'s parameters are `contest, game, policy_a, policy_b, record`;
    the draws are `random.gauss` / `random.uniform` and `sigma_leverage.roll_net(rng=random)` on the
    GLOBAL stream (`resolver.py:32, :139, :144, :334`), and one call moves the next unrelated
    `random.random()` -- `04 §C.12`'s rejection 4 and `04 PART D row 35`'s per-act `H(seed, tick,
    subject, purpose)` generator cannot be honoured without editing the kernel.
  * IT RETURNS A WINNER, NOT A MARGIN: `((band, reason), bout)`, and over the eight proceedings the band
    vocabulary is side labels -- `a`/`b`/`draw`, `A_decisive`/`B_decisive`/`A_total`/`B_total`, and
    `committee` (199 of 200 at `formal_contest` and `grand_contest`). No `net`/`ob` pair exists to hand
    `degree_from_net`, so a "degree adapter" would map winners to bands: the second resolver S27.2
    refuses, and `08_SEAM.md`'s *a MARGIN, never a winner*.
  * IT READS A FACULTY, NOT THE HOST'S RECORD: sides are `Contestant | int | dict` (faculty, standing,
    dossier) inside a named proceeding (faculty 1 vs 4 at `casual_dispute`: `b` 145 / `a` 48 / `draw`
    7); `SocialContestInput` carries a pool and obstacle operands, so adoption needs a new record.
  * COST: 0.08-0.47 ms per call against this entry's 0.002 ms; importing it loads 23 repository files
    (9 outside the kernel: `engine/substrate/stubwire.py`, `systems/__init__.py`, the dice engine).
So the three things the plan names as adoption's price -- a typed input record, a seeded rng, a degree
adapter -- are each a rewrite of the kernel's entry, and the third is refused by rule. The proceedings
design's nested run (`21_RECONCILIATION.md` step 15) is not this entry either; it is unbuilt.

RULED, ED-SC-0037 (Jordan, 2026-09-09): *"we have the sigma leverage d10 resolver in engine to use."*
⚠ BOTH IMPORTS, AND THE SECOND ONE IS THE POINT: `roll_net` alone is the bare pool roll (a back-compat
shim over `dice_engine.roll_pool` that drops its `ob`); the σ layer is `net_boost`, the μ-shift
ED-884 / ED-934 ruled. The composition is the tree's own
(`systems/social_contest/sim/contest/resolver.py:302`): `net = roll_net(pool) + net_boost(lev, pool)`.

It returns a net/ob pair as a `Margin` and NEVER a band: `seam/ladder.py` grades it by calling
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
from engine.season.queries.inputs import Margin, SocialContestInput


def obstacle(inp: SocialContestInput) -> float:
    """What stands against one matter's draw: the opposition's score halved, or the `H-127` stand-in
    where there is no score, BOUNDED ABOVE by the ceiling.

    ⚠ THE RULING IS `score/2 PLUS MODIFIERS` AND IT APPLIES TO A PERSON. Jordan, 2026-08-14, carried
    live in `dice_engine.degree_from_net`'s docstring: an opposed obstacle is *"their corresponding
    score/2 plus whatever specific modifiers exist for them in that instance"*. The instance
    modifiers are the room's terms and an examined document's forgery quality, below. A record, a rung or a proposition has no score and takes
    `obstacle_default`. **NO "BASE Ob BY SCALE"** (Jordan, 2026-09-05).

    ⚠ THE CEILING (`H-213`, swept; Contradiction 3 of the proceedings reconciliation, resolved): a
    ceiling caps how hard a matter can get. M-7 fails without one -- at the 1D pool floor
    `p_success` is 0.0006 at Ob 3 and effectively zero above, and buying σ-advantage cannot lift it.
    It is NOT a pool floor (that would raise everyone's competence, a statement about people), and
    it is NOT advantage: advantage stays a μ-shift on the roll (`net_boost`), and the ceiling is one
    bound inside this composition, the same for every party, never applied by a caller to `base_Ob`.
    PER MATTER (ED-SC-0038's pick): this bounds ONE record's obstacle -- one matter's draw -- and
    nothing composes obstacles across a bundle. `None` is the uncapped control arm. A ceiling below
    the Ob minimum (`OB_MIN`, PP-232) is refused rather than read: it would breach the floor. Nothing floors the composed obstacle itself: a score under 2 composes
    below `OB_MIN` (score 1 gives 0.5), as the deleted `_obstacle_of` did.

    ⚠ THE ROOM'S TERMS ARE THE INSTANCE MODIFIERS THE RULING NAMES (v9 SC-02 `22a`; proceedings
    `19_PLAN.md` steps 17, 18, 20): `room = reception_gain · reception + proof_step · proofs`, both read
    raw off the record, is SUBTRACTED -- a bench disposed toward the speaker, and proofs his opponent
    cannot mirror, make the matter easier; a bench against him makes it harder. A room's favour never
    takes the obstacle below `OB_MIN` (or below a base already under it): it moves the obstacle, it
    does not abolish it. The ceiling still bounds the result, so under the shipped `H-213` ceiling (2,
    the same as `obstacle_default`) a hostile room cannot raise a defaulted obstacle -- stated, not
    hidden. THE FAVOURABLE HALF IS CLIPPED THE SAME WAY: the ceiling is applied after the room, so
    against a strong opposition (base above the ceiling) a favourable room bites only where it takes
    the obstacle below the ceiling (`room > base - ceiling`); a room of +1.5 against a base of 4 under
    a ceiling of 2 changes nothing. With no room (both terms 0) this is the obstacle as it was.

    ⚠ AND AN EXAMINED DOCUMENT'S FORGERY QUALITY IS ONE MORE (v9 SC-02 `22b` step 25; `19_PLAN.md` step
    25, *"examination contests the record's forgery quality"*): `forgery_quality`, read raw off the
    Record an inquiry examines, is ADDED -- a better forgery is harder to find -- before the ceiling,
    which bounds it as it bounds a hostile room. `0` (a genuine document, or the `H-210` control arm)
    adds nothing. Under the shipped `H-213` ceiling (2 = `obstacle_default`) a forgery cannot raise a
    defaulted inquiry's obstacle: the quality reaches the roll only where the ceiling sits above the
    default (the uncapped `None` arm, or `3`) -- stated, not hidden."""
    ob = float(inp.opposition) / 2.0 if inp.opposition is not None else float(inp.obstacle_default)
    room = float(inp.reception_gain) * float(inp.reception) + float(inp.proof_step) * float(inp.proofs)
    ob = max(ob - room, min(ob, float(OB_MIN))) if room > 0 else ob - room
    ob += float(inp.forgery_quality)
    ceiling = inp.obstacle_ceiling
    if ceiling is None:
        return ob
    if ceiling < OB_MIN:
        raise ValueError(f"obstacle_ceiling {ceiling!r} is below the Ob minimum {OB_MIN} (PP-232); "
                         "a ceiling under the floor is a bad arm, refused rather than read (H-213)")
    return min(ob, float(ceiling))


def roll(inp: SocialContestInput, rng: Optional[random.Random] = None) -> Margin:
    """Roll one contested act -> `Margin(net, ob)`.

    The `rng` is a parameter and is never constructed here (`04 §C.12` rejection 4): the driver
    builds it from the run seed and the seam passes it down, as it passes `World`.
    `ob` is `obstacle(inp)`, this module's, and is returned so the host can grade the margin and
    apply S27.4 on the pair (`seam/wrappers/sigma.py::resolve`). The pool and leverage are the
    record's own, which the host already holds, so the margin does not carry them back."""
    return Margin(net=roll_net(inp.pool, rng=rng) + net_boost(inp.leverage, inp.pool),
                  ob=obstacle(inp))
