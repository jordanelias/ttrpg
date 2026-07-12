"""depth.py — event significance tiers (1 minor / 2 medium / 3 major) and the
per-tier exploration policy.

Tier is a property of the EVENT (a resolver call site), classified by the harness's
own rubric by default. An adapter's DecisionPoint may raise its own tier above the
rubric default with a one-line justification — it may never lower it. Letting an
adapter quietly downgrade its own scrutiny would be exactly the "scripting drift"
failure mode the Holonic Container Doctrine names (an adapter should never special-
case its own outcome). See the design doc section 5 for the full rubric and the
worked examples of what qualifies as minor/medium/major.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import IntEnum


class Tier(IntEnum):
    MINOR = 1
    MEDIUM = 2
    MAJOR = 3


@dataclass(frozen=True)
class TierPolicy:
    label: str
    #: minimum trial count required to trust a distribution at this tier; below this,
    #: the harness flags DEGENERATE_DISTRIBUTION rather than silently trusting a small N
    #: (the generalized form of the sim/tests/test_f7_smoke_oracle.py lesson: "no
    #: balance claim without an oracle + n >= 100").
    min_n: int
    #: if more than one branch is declared and one branch's empirical share meets or
    #: exceeds this threshold, flag DEGENERATE_DISTRIBUTION. None disables the check
    #: (appropriate for tier 1, where a skewed single-check distribution is expected
    #: and not itself informative).
    degenerate_threshold: float | None


DEPTH_TIERS: dict[Tier, TierPolicy] = {
    Tier.MINOR: TierPolicy("minor", min_n=20, degenerate_threshold=None),
    Tier.MEDIUM: TierPolicy("medium", min_n=100, degenerate_threshold=0.97),
    Tier.MAJOR: TierPolicy("major", min_n=100, degenerate_threshold=0.90),
}


@dataclass
class DecisionPoint:
    """One event an adapter's resolver can be driven through. `branches` names the
    outcome buckets the harness will tally trials into — the adapter classifies each
    sampled Outcome into one of these via Outcome.detail["branch"]."""
    name: str
    default_tier: Tier
    branches: list[str] = field(default_factory=list)
    justification: str = ""

    def tier(self) -> Tier:
        return self.default_tier
