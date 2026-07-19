"""depth.py — event significance tiers (1 minor / 2 medium / 3 major) and the
per-tier exploration policy.

Tier is a property of the EVENT (a resolver call site). What this module actually
enforces, mechanically, at DecisionPoint construction (both ValueError, not
deferred to a runtime check that could be skipped): (1) default_tier must be a
real Tier member, not any int/other value that happens to look plausible — found
by adversarial review, an earlier cut let default_tier=99 sail through and only
failed later, deep inside Harness.run(), with a bare KeyError; (2) every
DecisionPoint MUST declare a non-empty justification for its tier — an adapter
can never leave a tiering choice unexplained, and the justification is carried
into the trace record so it's auditable after the fact.

What this module does NOT (and, without a fuller rubric-classifier, cannot)
mechanically enforce: that the declared tier is actually the CORRECT one for the
event's real-world consequence. "An adapter may raise its own tier, never lower it"
is a review-time discipline for whoever authors or audits an adapter, not a runtime
guarantee the code checks — nothing here re-derives the "right" tier independently
to compare against. Silently claiming otherwise would be exactly the kind of
overclaim this project's own anti-fabrication discipline exists to catch, so this
docstring says the limitation plainly instead: catching a self-serving tier
downgrade is presently a code-review responsibility (e.g. the module-adjudicator or
canon-guard skills), not something Harness.run() can detect. See design doc section
5 for the tier rubric and worked examples of what qualifies as minor/medium/major.
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
    sampled Outcome into one of these via Outcome.detail["branch"].

    justification is mandatory (see __post_init__) and is carried into the trace
    record — a tiering choice always leaves an auditable reason, even though (per
    this module's docstring) nothing here verifies the reason is a GOOD one."""
    name: str
    default_tier: Tier
    branches: list[str] = field(default_factory=list)
    justification: str = ""

    def __post_init__(self):
        # default_tier isn't runtime-checked by the `Tier` type hint — an adapter
        # passing a raw int/other value (e.g. default_tier=99) would otherwise sail
        # through construction and only fail deep inside Harness.run() with a bare
        # KeyError from DEPTH_TIERS[tier], after contract-binding and canon
        # resolution already ran, with no trace or registry record produced. Found
        # by deliberately stress-testing an adapter with an out-of-range tier value.
        if not isinstance(self.default_tier, Tier):
            raise ValueError(
                f"DecisionPoint {self.name!r} declares default_tier="
                f"{self.default_tier!r}, not a real Tier member ({list(Tier)}) — "
                f"caught at construction time so this fails loudly for the adapter "
                f"author instead of crashing mid-run with an opaque KeyError"
            )
        # (self.justification or "") tolerates a caller passing justification=None
        # (violates the str type hint, but nothing stops an adapter author doing it
        # e.g. via a dict.get() default) — without this, .strip() on None raises an
        # opaque AttributeError instead of the intended, informative ValueError this
        # method exists to guarantee. Found by adversarial review: the first cut of
        # this check crashed exactly this way.
        if not (self.justification or "").strip():
            raise ValueError(
                f"DecisionPoint {self.name!r} declares tier {self.default_tier!r} "
                f"with no justification — every tiering choice must state why, so "
                f"it can be reviewed (this is enforced at construction time, not "
                f"deferred to a runtime check that could be skipped)"
            )

    def tier(self) -> Tier:
        return self.default_tier
