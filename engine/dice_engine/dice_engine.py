"""
engine/dice_engine/dice_engine.py — d10 dice pool, TN values, degree of success, continuous engine

Owner of the d10 face rule (`FACE_NET`), the per-die pair, the one sampler and the degree ladder (`BAND_FLOORS`,
`MARGIN_SCALE`); the values are exported to `engine/engine_params/` by `tools/export_sim_params.py`.
(`params/core.md`, which this header once named as source, is retired: the code is the source.)
Status: the ruled owner of the dice chain for every scale of the game; the code is the mechanism, this text is reference.

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
# Every subsystem's bands are this module's (ED-SC-0031); this is the hook for the second clause,
# and the point of putting it HERE rather than leaving each subsystem to police itself is that
# the constraint becomes STRUCTURAL:
#
#   * an extension's only power is to VETO the top band. `may_overwhelm`'s return is coerced with
#     `not` and consulted in exactly one branch below — the OVERWHELMING one — so the only band
#     transition an extension can express is 3 -> 2. There is no signature by which it could
#     promote a band, move the Partial window, or touch Failure.
#   * `context` is the subsystem's own state (the contest passes its pool). The engine neither
#     interprets it nor stores it. Unknown keys are REFUSED rather than swallowed (below).
#
# ⚠ THE LIMIT OF "STRUCTURAL". `may_overwhelm` is arbitrary Python and can import
# `degree_from_net` in one line: what the design prevents is RETURNING a different band, not
# re-deriving one. An extension runs in this process with access to this module's mutable state,
# and `DEGREE_ORDINAL` is a plain dict a hostile extension could mutate mid-call. The claim is
# narrower and still worth having:
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

        ⚠ `**context` accepts any keyword, and an extension that defaults its parameter (`pool=None`
        -> abstain) would turn a MISSPELLED OR RENAMED key into a band change:
        `degree_from_net(net, ob, extension=E, poool=8)` would return Overwhelming where
        `pool=8` returns Success, with no error and no warning. That is CLAUDE.md
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
    tn: int
    rolls: list[int]
    net: int
    degree: Degree | None  # None if no Ob provided
    ob: int | float | None


# Canonical die rule (params/core.md §Die Rule, PP-246):
#   1 = -1 success, 2-6 = 0, 7-9 = +1 success, 10 = +2 successes. No chain.
# The d10's faces and what each scores. THE face rule; `_die_result` reads it and nothing else spells it.
FACE_NET = {1: -1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 1, 8: 1, 9: 1, 10: 2}


def _die_result(face: int) -> int:
    return FACE_NET[face]


# Where the bands fall, as margins: Partial from 0, Success from 1, Overwhelming from 3, held in the
# ladder's integer milli-units (W3-1, C3-L1: the margin is quantised once, round(MARGIN_SCALE * margin)).
MARGIN_SCALE = 1000
BAND_FLOORS = {"partial": 0, "success": 1000, "overwhelming": 3000}


# Per-die EV at TN 7 — the only TN there is.
# [Jordan, 2026-08-25: "TN7 always. Never change TN anywhere ever." — ED-IN-0196]
#
# The ONE owner, within engine/dice_engine/, of the per-die mean and sigma. The PUBLIC names carry the
# literals (plain assignments: tools/export_sim_params.py reads only those, so the typed export keeps
# the pair) and engine/dice_engine/sigma_leverage.py aliases them rather than keeping a copy. The
# private names stay as aliases of the public ones: tests/valoria/test_tn7_always.py pins them.
# modules/mass_battle/resolution.py (`_SIG_PER_DIE`) and modules/mass_battle/config.py
# (`PER_DIE_NET_EV`) hold values of their own; REM-42 does not reach them.
MU_PER_DIE = 0.40      # [canonical: params/core.md §Expected Value, TN 7]
SIGMA_PER_DIE = 0.800  # [canonical: params/core.md §Expected Value, TN 7]
_MU_PER_DIE: float = MU_PER_DIE
_SIGMA_PER_DIE: float = SIGMA_PER_DIE
assert abs(MU_PER_DIE - sum(FACE_NET.values()) / 10) < 1e-12 and \
       abs(SIGMA_PER_DIE ** 2 - sum((v - MU_PER_DIE) ** 2 for v in FACE_NET.values()) / 10) < 1e-12, \
       "the per-die pair is the face rule's; change them together"


_TN_RULING = ('TN is 7. Always. Jordan, 2026-08-25: "TN7 always. Never change TN anywhere '
              'ever." A varying difficulty is an Ob, not a TN. (ED-IN-0196)')


def _require_tn7(tn: int) -> None:
    """The owner refuses any TN but 7.

    `tn` is kept as a parameter rather than deleted: it is carried on RollResult and call
    sites pass tn=7 explicitly. Removing it would be a wide, behaviour-free churn. Validating it
    costs nothing and turns a silently-ignored argument into a refused one — which is the entire
    point, because a silently-ignored `tn` is what let four TN-varying mechanisms sit in the tree
    looking live.
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
    return RollResult(tn=tn, rolls=rolls, net=net, degree=deg, ob=ob)


def continuous_engine_sample(pool: float, tn: int = 7,
                             rng: random.Random | None = None) -> float:
    """The sampler every provider draws from (ED-833; Jordan, 2026-11-12). Same mean and variance as the d10
    face rule it is derived from.

    Normal(μ·N, σ·√N) per Decision E continuous engine; the pool is taken as it is for `pool > 0` (it may be
    fractional, which enables a fractional Ob), and a pool of nothing rolls nothing.
    Canon: params/core.md §Continuous Engine — statistically equivalent to discrete.
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
    nets. `ob` is RULED to become fractional (Jordan, 2026-08-14). An obstacle a person opposes
    with is `sigma_leverage.opposed_ob(his skill score, opposition_rate)`, `MU_PER_DIE` (0.4) a
    point (A-26, A-71, A-79), composed by the module owners `modules/social_contest/roll.py::obstacle`
    and `modules/combat/core.py::ob_from_defender` (the latter reads `faculty / 2.0` until B05.58
    moves it onto `opposed_ob`); hostile terms add, nothing lowers it.
    ⚠ (ED-IN-0202) The derivation is implemented at some sites:
    `systems/factions/sim/crown_initiative.py::coronation_renewal_ob` implements
    `floor(Church.L / 2) + 1` exactly, Royal Progress derives its Ob from the standing
    gap, and the tribunal derives under formal grounds. But there is NO
    SINGLE-OWNER derivation — most sites still hand-set (Muster 1, Govern 2, the
    threadwork table; combat's fixed Ob 3 is deleted, PC-03), the three opposed sites disagree
    (the person-opposed term has one owner since B05: `opposed_ob`; the faction and threadwork sites
    named here are untouched), and `parliamentary_transfer`'s `L+2`
    contradicts the ruling while being stated as canon in `parliamentary_transfer_v30.md`.
    Reconciling them is a systems ruling, not an edit, and is SUSPENDED by Jordan (2026-08-21).
    The distinction matters here more than anywhere else, because this is the function a reader
    consults to learn what an obstacle IS.
    The Partial band is a whole-success-wide window rather
    than the single point `margin == 0`, which is what the same rule reduces to on integers
    (`floor(margin) == 0`) — the two readings agree everywhere the game rolls whole dice, and
    only the windowed one survives contact with fractional obstacles, where exact equality
    essentially never occurs and Partial would otherwise vanish.

    ⚠ THE PRE-RULING BANDS (Overwhelming at Net >= 2*Ob, Failure at Net <= 0) ARE NOT CANON: where
    any capture of them disagrees with code, the code wins (principle 7 / ED-1050). Do not restore
    bands from one.

    RULED OUT, explicitly, by the same ruling:
      * Ob-scaled Overwhelming (`net >= 2*Ob`) — Overwhelming no longer depends on difficulty.
      * The separate PP-232 `net >= 3` floor — subsumed; the margin bar IS 3.
      * The Ob-20 exception (Overwhelming unavailable, Partial needing net >= 10) — "always"
        admits no ceiling case.

    `extension` is the ED-SC-0032 injection seam: a subsystem's declared `BandExtension`, which
    may VETO an Overwhelming and can do nothing else. It is passed BY THE SUBSYSTEM'S WRAPPER,
    never resolved here — the engine does not know which subsystems exist, and a default of None
    means the unmodified ladder. `**context` is forwarded to the extension untouched, and is validated
    against the extension's declared keys on entry, in every band; a context with `extension=None` raises
    `TypeError`.

    Behaviour change, stated rather than buried (CLAUDE.md 0.1 point 4): the Partial band was
    `0 < net < Ob`, so a roll that cleared zero but fell far short of a hard obstacle read as a
    Partial. It now reads as a Failure. Partial is the near-miss-by-nothing outcome, not the
    tried-and-failed one. Measured deltas are in the ED-IN-0187 ledger entry.
    """
    # THE CONTEXT IS CHECKED ON ENTRY, BEFORE THE BAND IS DECIDED (DOE §3 row 2; F-DICE-11): a misspelled key
    # reached the extension's check only on the Overwhelming branch, so below it the key was swallowed and the
    # call returned a band with no error. A context with no extension has no reader, and is refused alike.
    if extension is not None:
        extension.validate_context(context)
    elif context:
        raise TypeError(f"degree_from_net got context {sorted(context)} and no extension to read it; "
                        "an undeclared key would be swallowed by **context -- pass the extension or drop the key.")
    # The real margin is converted ONCE, here, to integer milli-units and compared against the integer
    # BAND_FLOORS (C3-L1): a margin that is a float sum a rounding error under an edge reads as on it.
    m = round(MARGIN_SCALE * (net - ob))
    if m < BAND_FLOORS["partial"]:
        return Degree.FAILURE
    if m < BAND_FLOORS["success"]:
        return Degree.PARTIAL
    if m >= BAND_FLOORS["overwhelming"]:
        # THE ONE BRANCH AN EXTENSION CAN REACH (ED-SC-0032). See `BandExtension` above for why
        # this is the only one, and why the constraint is structural rather than a convention a
        # subsystem is asked to respect. Note the ladder result is NOT passed to the extension:
        # it is asked whether an Overwhelming is permissible, never what the band should be.
        if extension is not None and not extension.may_overwhelm(net, ob, **context):
            return Degree.SUCCESS
        return Degree.OVERWHELMING
    return Degree.SUCCESS


def degree_label(net: int | float, ob: int | float) -> str:
    """`degree_from_net` in the Title-Case string vocabulary. Convenience, not a second ladder."""
    return DEGREE_LABEL[degree_from_net(net, ob)]
