"""
sim/personal/tribunal.py — Asymmetric proceedings + Excommunication Tribunal

Canon source: designs/scene/social_contest_v30.md §7 + §7.1 (ED-625, approved 2026-04-17)
Game Design constraints applicable: GD-3 (status-flag enforcement at boundary)
Status: [PROVISIONAL — Phase 5/9 integration 2026-05-17. Single-roll procedural
         abstraction of the §7.1 procedure. Full multi-Exchange Contest engine
         (Persuasion Track tick-by-tick, Resistance per Exchange, Inquisitor-set
         exchange count) is canonical Phase 5 (personal-scale) work, deferred.
         The current implementation captures the §7.1 modifications as roll-shape
         adjustments and is sufficient for strategic-scale faction-action use.]

Dependencies:
  - sim/autoload/dice_engine — d10 pool, TN 7, degree resolution

Entry points:
  - run_excommunication_tribunal(accused, church, world, rng, formal_grounds) -> TribunalResult
  - run_tribunal(accused, accusers, proceeding_type, world, rng) -> TribunalResult
        [NotImplementedError — generic §7 Asymmetric Proceeding; canonical Phase 5]
"""
from __future__ import annotations

from dataclasses import dataclass

from sim.autoload import dice_engine
from sim.autoload.dice_engine import Degree


# ── Ledger-cited constants (every value here has a sim_verification_ledger.json entry) ──

# Canon: designs/scene/social_contest_v30.md §7.1 — Persuasion Track starts at 7
# (institutional fait accompli). In the multi-Exchange procedure this means the
# track is near-decisive before Exchange 1. In our single-roll abstraction it
# translates to +1D pool bonus for the Church side when formal grounds apply.
TRIBUNAL_PERSUASION_TRACK_START = 7  # [canonical: social_contest_v30.md §7.1]
TRIBUNAL_FORMAL_GROUNDS_POOL_BONUS = 1  # derived: +1D abstraction of Persuasion start 7

# Canon: §7.1 — Resistance for accused: halved (same as standard)
# Applied to Ob (target's resistance metric at strategic scale).
TRIBUNAL_RESISTANCE_HALVED_FACTOR = 0.5  # [canonical: social_contest_v30.md §7.1]

# Canon: §7.1 Prerequisites — CI >= 40, Church Mandate >= 4
TRIBUNAL_PREREQ_CI_FORMAL = 40  # [canonical: social_contest_v30.md §7.1]
TRIBUNAL_PREREQ_L_FORMAL = 4  # [canonical: social_contest_v30.md §7.1]

# Canon: §7.1 Exchange count: 1-3 (set by Inquisitor). Stored for future
# multi-Exchange Contest engine; not used in current single-roll form.
TRIBUNAL_EXCHANGE_COUNT_MIN = 1  # [canonical: social_contest_v30.md §7.1]
TRIBUNAL_EXCHANGE_COUNT_MAX = 3  # [canonical: social_contest_v30.md §7.1]

# Canon: params/core.md — TN 7 is the canonical default for social contests
TRIBUNAL_TN = 7  # [canonical: params/core.md §TN Values]


# ── Result type ───────────────────────────────────────────────────────────────

@dataclass
class TribunalResult:
    """Outcome of one Excommunication Tribunal resolution."""
    degree: Degree
    pool_size: int
    ob: float
    net: int
    formal_grounds: bool
    rolls: list[int]
    notes: list[str]


# ── §7.1 procedure ────────────────────────────────────────────────────────────

def formal_grounds_check(church, world) -> bool:
    """Returns True iff §7.1 stricter prerequisites are met.

    Per §7.1: CI >= 40 AND Church Mandate (=L) >= 4.
    (The Evidence Track / Obligation / 2-prior-conviction clause is one of three
    alternative gates; in v18 strategic-scale we treat the L+CI gate as
    sufficient for formal tribunal procedure since Evidence Track is a
    personal-scale concept not yet ported.)
    """
    # Canon: social_contest_v30.md §7.1 Prerequisites
    ci = world.clocks.get('CI', 0.0)
    return ci >= TRIBUNAL_PREREQ_CI_FORMAL and church.L >= TRIBUNAL_PREREQ_L_FORMAL


def run_excommunication_tribunal(accused, church, world, rng,
                                  formal_grounds: bool | None = None) -> TribunalResult:
    """Resolve one Excommunication Tribunal against `accused` faction.

    Per social_contest_v30.md §7.1 — single-roll procedural abstraction of the
    multi-Exchange procedure. Modifications applied:
      - Pool: Church.L (Mandate); +1D when formal grounds (Persuasion Track 7 abstraction)
      - Ob: target.L (resistance) — halved when formal grounds (Resistance halved)
      - TN 7 (params/core.md social-contest default)

    `formal_grounds=None` -> auto-detect via formal_grounds_check.

    Returns TribunalResult; consequences applied by the caller (excommunication.py).
    """
    if formal_grounds is None:
        formal_grounds = formal_grounds_check(church, world)

    # Pool: Church Mandate
    # Canon: faction_canon §9 "Roll: L vs target L". L is the institutional weight.
    pool = int(church.L)
    notes: list[str] = []

    if formal_grounds:
        # +1D bonus abstraction of Persuasion Track 7 start
        pool += TRIBUNAL_FORMAL_GROUNDS_POOL_BONUS
        notes.append("formal_grounds: +1D (Persuasion Track 7 abstraction)")

    # Ob: target's L (their institutional weight resists)
    # Canon: §9 "L vs target L (leader)". For faction-action use, target IS the leader's faction.
    base_ob = float(accused.L)
    if formal_grounds:
        # Resistance halved per §7.1; floor at 1 (Pool Minimum analog)
        effective_ob = max(1.0, round(base_ob * TRIBUNAL_RESISTANCE_HALVED_FACTOR))
        notes.append(f"formal_grounds: Ob {base_ob:.1f} -> {effective_ob:.1f} (Resistance halved)")
    else:
        effective_ob = max(1.0, round(base_ob))

    # Roll
    result = dice_engine.roll_pool(
        pool_size=pool,
        tn=TRIBUNAL_TN,
        ob=effective_ob,
        rng=rng,
    )

    return TribunalResult(
        degree=result.degree,
        pool_size=result.pool_size,
        ob=effective_ob,
        net=result.net,
        formal_grounds=formal_grounds,
        rolls=result.rolls,
        notes=notes,
    )


def run_tribunal(accused, accusers, proceeding_type: str, world=None, rng=None):
    """Generic §7 Asymmetric Proceeding handler.

    Not implemented in v18 — covers §7.2 Succession Contest and §7.3 Heresy
    Investigation Lifecycle. These are canonical Phase 5 personal-scale work.
    """
    # GD-3: status-flag enforcement at boundary lives at parliamentary_vote.py;
    # this generic path is not yet wired.
    raise NotImplementedError(
        "sim/personal/tribunal.py — run_tribunal generic §7 dispatch not implemented; "
        "use run_excommunication_tribunal for §7.1 specifically. "
        "Canonical Phase 5 personal-scale Contest engine pending."
    )
