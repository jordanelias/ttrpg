"""
engine/autoload/dice_engine.py — d10 dice pool, TN values, degree of success, continuous engine
(The header read `sim/autoload/...` until 2026-08-27; that tree was retired 2026-07-21. Its twin
in sigma_leverage.py was fixed the same day and this one was missed — §0.1 pt 5's sweep-the-pattern.)

Canon source: params/core.md (Die Rule, TN Values, Degrees of Success, Continuous Engine Decision E)
Params source: params/core.md
Status: [CANONICAL — Phase 1 implementation 2026-05-17]

Dependencies:
  - none — root primitive

Entry points:
  - roll_pool(pool_size: int, tn: int, rng=None) -> RollResult
  - continuous_engine_sample(pool: float, tn: int, rng=None) -> float
  - degree_from_net(net, ob, extension: BandExtension | None = None, **context) -> Degree
  - BandExtension — the ED-SC-0032 injection seam a subsystem's wrapper passes as `extension`
"""
from __future__ import annotations

import math
import random
from dataclasses import dataclass
from enum import Enum


class Degree(Enum):
    OVERWHELMING = "overwhelming"
    SUCCESS = "success"
    PARTIAL = "partial"
    FAILURE = "failure"


# Several subsystems carry the four bands as Title-Case strings rather than the enum. ONE map, so a
# string-speaking module still resolves its bands through the owner instead of re-deciding them.
DEGREE_LABEL: dict["Degree", str] = {
    Degree.OVERWHELMING: "Overwhelming",
    Degree.SUCCESS: "Success",
    Degree.PARTIAL: "Partial",
    Degree.FAILURE: "Failure",
}

# The same four bands as an ORDINAL. The social-contest kernel uses the degree as a numeric
# magnitude (`contest/_advance` multiplies by it), so it needs 0-3 rather than an enum — and
# before ED-SC-0031 it got there by keeping a private ladder that returned ints directly, which
# is how the ninth ladder survived a census. Owning the encoding here means a caller that needs
# a number still resolves its BANDS through `degree_from_net`; only the spelling is local.
DEGREE_ORDINAL: dict["Degree", int] = {
    Degree.FAILURE: 0,
    Degree.PARTIAL: 1,
    Degree.SUCCESS: 2,
    Degree.OVERWHELMING: 3,
}


# ══════════════════════════════════════════════════════════════════════════════════════
# THE EXTENSION SEAM (ED-SC-0032). Jordan, 2026-08-15, verbatim:
#
#   "systems should not need different degree bands. it should be consistent in application.
#    if a system does require any modification or extension, then the wrapper needs to inject
#    the engine in such a manner that it can be modified cleanly."
#
# ED-SC-0031 satisfied the first clause — every subsystem's bands became this module's — and
# NOT the second: the social contest's pool-aware de-saturation survived as a hard-coded
# post-filter inside `sigma_leverage`, with no hook here and nothing stopping the next
# subsystem bolting on a differently-shaped one. This is the hook, and the point of putting it
# HERE rather than leaving each subsystem to police itself is that the constraint becomes
# STRUCTURAL:
#
#   * an extension's only power is to VETO the top band. `may_overwhelm`'s return is coerced with
#     `not` and consulted in exactly one branch below — the OVERWHELMING one — so the only band
#     transition an extension can express is 3 -> 2. There is no signature by which it could
#     promote a band, move the Partial window, or touch Failure.
#   * `context` is the subsystem's own state (the contest passes its pool). The engine neither
#     interprets it nor stores it. Unknown keys are REFUSED rather than swallowed (below).
#
# ⚠ THE LIMIT OF "STRUCTURAL", stated because an adversarial pass broke the stronger claim this
# comment first made. Two sentences are retracted. (1) "the ladder itself is never passed to the
# extension, so an extension cannot re-derive it" — FALSE: `may_overwhelm` is arbitrary Python and
# can import `degree_from_net` in one line. What the design prevents is RETURNING a different
# band, not re-deriving one. (2) "whatever its author intends" — OVERSTATED: an extension runs in
# this process with access to this module's mutable state, and `DEGREE_ORDINAL` is a plain dict a
# hostile extension could mutate mid-call. The honest claim is narrower and still worth having:
# an extension that confines itself to its own contract CANNOT express any band change but 3 -> 2,
# and any attempt to do more has to reach outside the seam, where it is visible in a diff. That is
# an auditable convention with a structurally-bounded return channel — not a sandbox, and this
# module should not be read as promising one.
#
# WHY VETO-THE-TOP-BAND IS THE RIGHT AND ONLY POWER, rather than a general hook: it is the one
# shape the two real cases need. The contest's bar de-saturates Overwhelming as pools grow (a
# large pool clears a fixed margin nearly every roll, so without it the band stops
# discriminating). Nothing in the tree has ever needed to make a band EASIER, and a hook that
# allowed it would re-admit the private ladders this seam exists to end. Widening this contract
# is a design decision with a ledger entry, not a convenience.
class BandExtension:
    """What a subsystem may inject into the ladder. Subclass and override `may_overwhelm`.

    Deliberately a class rather than a bare callable: an extension is a NAMED, declared policy
    that a wrapper injects, and a name is what makes it auditable in a stack trace, in a repr,
    and in the registry. `tests/valoria/test_degree_ladder_single_owner.py` enrols them.
    """

    #: Short human name, used in reprs and in the ladder registry's roster.
    name = "band-extension"

    #: Context keys this extension reads. The engine REFUSES any other key (see below).
    context_keys: tuple = ()

    def may_overwhelm(self, net, ob, **context) -> bool:
        """Return False to demote an Overwhelming to Success. Default: never vetoes."""
        return True

    def validate_context(self, context) -> None:
        """Refuse a context key this extension does not declare. Called by the ladder.

        ⚠ THIS EXISTS BECAUSE THE SEAM SHIPPED WITH A SILENT-NO-OP HOLE, found by an adversarial
        pass on the commit that built it. `**context` accepts any keyword, and an extension that
        defaults its parameter (`pool=None` -> abstain) turns a MISSPELLED OR RENAMED key into a
        band change: `degree_from_net(net, ob, extension=E, poool=8)` returned Overwhelming where
        `pool=8` would have returned Success, with no error and no warning. That is CLAUDE.md
        §0.1 point 1's read/write asymmetry exactly — the write silently misses the read — and it
        is the failure mode a seam must not have, because the whole point of a declared extension
        is that its inputs are declared.

        An extension declaring no `context_keys` accepts none, so the default is strict rather
        than permissive: a new extension that forgets to declare fails loudly on its first call
        instead of quietly abstaining forever.
        """
        unknown = set(context) - set(self.context_keys)
        if unknown:
            raise TypeError(
                f"{type(self).__name__} does not declare context key(s) {sorted(unknown)}; "
                f"it reads {sorted(self.context_keys)}. An undeclared key would be swallowed by "
                "**context and silently change the band — declare it or fix the caller."
            )

    def __repr__(self) -> str:      # pragma: no cover - diagnostics only
        return f"<{type(self).__name__} {self.name!r}>"


@dataclass
class RollResult:
    pool_size: int
    tn: int
    rolls: list[int]
    net: int
    degree: Degree | None  # None if no Ob provided
    ob: int | float | None


# Canonical die rule (params/core.md §Die Rule, PP-246):
#   1 = -1 success, 2-6 = 0, 7-9 = +1 success, 10 = +2 successes. No chain.
def _die_result(face: int) -> int:
    if face == 1:
        return -1
    elif face <= 6:
        return 0
    elif face <= 9:
        return 1
    else:  # 10
        return 2


# Per-die EV at TN 7 — the only TN there is.
# [Jordan, 2026-08-25: "TN7 always. Never change TN anywhere ever." — ED-IN-0196]
# The table used to carry TN 6 (μ=0.50, σ=0.806) and TN 8 (μ=0.30, σ=0.781). Those rows are
# dead under the ruling and are deleted rather than left as reachable-looking configuration.
# The historical table survives, reference-only and NOT a mechanism (§0.05), in
# engine/engine_params/params_tables.yaml.
#
# Note the TN 6 row was always in tension with `_die_result` below, which has never read `tn`:
# μ=0.50 is only reachable if faces 6-9 score, and no face rule here has ever done that. The
# ruling resolves that tension in favour of the die rule.
_MU_PER_DIE: float = 0.40      # [canonical: params/core.md §Expected Value, TN 7]
_SIGMA_PER_DIE: float = 0.800  # [canonical: params/core.md §Expected Value, TN 7]


_TN_RULING = ('TN is 7. Always. Jordan, 2026-08-25: "TN7 always. Never change TN anywhere '
              'ever." A varying difficulty is an Ob, not a TN. (ED-IN-0196)')


def _require_tn7(tn: int) -> None:
    """The owner refuses any TN but 7.

    `tn` is kept as a parameter rather than deleted: it is carried on RollResult, ~30 call
    sites pass tn=7 explicitly, and WEAPON_TN_BASE crosses to the Godot bridge. Removing it
    would be a wide, behaviour-free churn. Validating it costs nothing and turns a silently
    -ignored argument into a refused one — which is the entire point, because a silently
    -ignored `tn` is what let four TN-varying mechanisms sit in the tree looking live.
    """
    # [canonical: Jordan ruling 2026-08-25 "TN7 always. Never change TN anywhere ever." — ED-IN-0196]
    if tn != 7:
        raise ValueError(f"{_TN_RULING} Got tn={tn!r}.")


def roll_pool(pool_size: int, tn: int = 7, ob: int | float | None = None,
              rng: random.Random | None = None) -> RollResult:
    """Roll pool_size d10s under the canonical face rule at TN 7. Pool minimum 1D."""
    _require_tn7(tn)
    if rng is None:
        rng = random.Random()
    effective_pool = max(1, pool_size)  # params/core.md §Pool Minimum
    rolls = [rng.randint(1, 10) for _ in range(effective_pool)]
    net = sum(_die_result(face) for face in rolls)
    deg = degree_from_net(net, ob) if ob is not None else None
    return RollResult(pool_size=effective_pool, tn=tn, rolls=rolls, net=net, degree=deg, ob=ob)


def continuous_engine_sample(pool: float, tn: int = 7,
                             rng: random.Random | None = None) -> float:
    """Sample net successes from Normal(μ·N, σ·√N) per Decision E continuous engine.

    Canon: params/core.md §Continuous Engine — statistically equivalent to discrete.
    Pool may be fractional (enables a fractional Ob).
    """
    _require_tn7(tn)
    if rng is None:
        rng = random.Random()
    if pool <= 0:
        return 0.0
    mu, sigma = _MU_PER_DIE, _SIGMA_PER_DIE
    mean = mu * pool
    std = sigma * math.sqrt(pool)
    return rng.gauss(mean, std)


def degree_from_net(net: int | float, ob: int | float,
                    extension: "BandExtension | None" = None, **context) -> Degree:
    """THE degree ladder. Single owner for every scale of the game (Jordan ruling, 2026-08-14).

    The ladder reads the MARGIN — how far the dice cleared the obstacle — never the obstacle's
    own size:

        margin = net - ob

        margin >= 3        Overwhelming   "3 or more is always overwhelming"
        margin >= 1        Success        cleared it by at least one whole success
        0 <= margin < 1    Partial        the obstacle is MET but not EXCEEDED
        margin <  0        Failure        fell short

    Both operands may be fractional. `net` already is — the continuous engine returns fractional
    nets. `ob` is RULED to become fractional (Jordan, 2026-08-14: an obstacle rolled against a
    character or faction is "their corresponding score/2 plus whatever specific modifiers exist for
    them in that instance") but ⚠ THAT DERIVATION IS IMPLEMENTED NOWHERE — every call site in the
    tree still passes a hand-set Ob. An earlier draft of this paragraph stated it as an accomplished
    fact; it is a ruling awaiting execution, and the distinction matters here more than anywhere
    else, because this is the function a reader consults to learn what an obstacle IS.
    The Partial band is a whole-success-wide window rather
    than the single point `margin == 0`, which is what the same rule reduces to on integers
    (`floor(margin) == 0`) — the two readings agree everywhere the game rolls whole dice, and
    only the windowed one survives contact with fractional obstacles, where exact equality
    essentially never occurs and Partial would otherwise vanish.

    ⚠ THE CAPTURED PARAMS TABLE STILL SHOWS THE OLD LADDER, and it is not a competing source.
    `engine/engine_params/params_tables.yaml` §"Degrees of Success" holds the PRE-RULING bands
    (Overwhelming at Net >= 2*Ob, Failure at Net <= 0) because it is a byte-faithful capture of the
    evacuated `params/core.md` and its own header says NEVER hand-edit. It is history, not canon:
    where it disagrees with code, the code wins (principle 7 / ED-1050). Do not restore bands from
    it. The note lives here, at the owner a reader consults, rather than in the capture — annotating
    the capture would have broken the one property it exists to have, and its generator was retired
    with its source, so the edit could not have been regenerated away.

    RULED OUT, explicitly, by the same ruling (all three were live here until 2026-08-14):
      * Ob-scaled Overwhelming (`net >= 2*Ob`) — Overwhelming no longer depends on difficulty.
      * The separate PP-232 `net >= 3` floor — subsumed; the margin bar IS 3.
      * The Ob-20 exception (Overwhelming unavailable, Partial needing net >= 10) — "always"
        admits no ceiling case.

    `extension` is the ED-SC-0032 injection seam: a subsystem's declared `BandExtension`, which
    may VETO an Overwhelming and can do nothing else. It is passed BY THE SUBSYSTEM'S WRAPPER,
    never resolved here — the engine does not know which subsystems exist, and a default of None
    means the unmodified ladder. `**context` is forwarded to the extension untouched.

    Behaviour change, stated rather than buried (CLAUDE.md 0.1 point 4): the Partial band was
    `0 < net < Ob`, so a roll that cleared zero but fell far short of a hard obstacle read as a
    Partial. It now reads as a Failure. Partial is the near-miss-by-nothing outcome, not the
    tried-and-failed one. Measured deltas are in the ED-IN-0187 ledger entry.
    """
    margin = net - ob
    if margin < 0:
        return Degree.FAILURE
    if margin < 1:
        return Degree.PARTIAL
    if margin >= 3:
        # THE ONE BRANCH AN EXTENSION CAN REACH (ED-SC-0032). See `BandExtension` above for why
        # this is the only one, and why the constraint is structural rather than a convention a
        # subsystem is asked to respect. Note the ladder result is NOT passed to the extension:
        # it is asked whether an Overwhelming is permissible, never what the band should be.
        if extension is not None:
            extension.validate_context(context)
            if not extension.may_overwhelm(net, ob, **context):
                return Degree.SUCCESS
        return Degree.OVERWHELMING
    return Degree.SUCCESS


def degree_label(net: int | float, ob: int | float) -> str:
    """`degree_from_net` in the Title-Case string vocabulary. Convenience, not a second ladder."""
    return DEGREE_LABEL[degree_from_net(net, ob)]
