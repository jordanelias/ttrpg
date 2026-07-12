"""triage.py — the mandatory triage-flag taxonomy.

A run's verdict is never PASS while an unresolved flag exists (design doc section 5).
Categories are deliberately small and closed-set in Gate-0; UNCLASSIFIED exists so a
future adapter never has to force-fit a real finding into the wrong bucket while a
new category is proposed and added here (single home, per CLAUDE.md section 8's
"every rule lives once").
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class TriageCategory(str, Enum):
    #: a value or doc reference the harness needed did not resolve via CanonResolver
    CANON_GAP = "CANON_GAP"
    #: a references/module_contracts.yaml A1-A12-style closure check failed
    CONTRACT_VIOLATION = "CONTRACT_VIOLATION"
    #: a sampled outcome fell outside a declared clamp/bound
    OUT_OF_RANGE = "OUT_OF_RANGE"
    #: the adapter's resolver hit a NotImplementedError / [PROVISIONAL] branch
    STUB_HIT = "STUB_HIT"
    #: a distribution collapsed to (near-)one outcome at a tier that requires spread
    DEGENERATE_DISTRIBUTION = "DEGENERATE_DISTRIBUTION"
    #: a numeric literal reached the resolver without a citation CanonResolver could verify
    FABRICATION_RISK = "FABRICATION_RISK"
    UNCLASSIFIED = "UNCLASSIFIED"


@dataclass
class TriageFlag:
    event_id: str
    tier: int
    category: TriageCategory
    detail: str
    source_citation: str | None = None

    def to_obj(self) -> dict:
        return {
            "event_id": self.event_id,
            "tier": self.tier,
            "category": self.category.value,
            "detail": self.detail,
            "source_citation": self.source_citation,
        }


class TriageLog:
    """Collects flags for one harness run. Gate-0 has no resolution workflow yet —
    every flag a run produces is open by construction; a future wave should let a
    flag resolve to a filed ED-<LANE>-NNNN id (the same forward-only-disposition
    discipline ED-IN-0036 already added to valoria-vector-audit/valoria-simulator)."""

    def __init__(self):
        self.flags: list[TriageFlag] = []

    def flag(self, event_id: str, tier: int, category: TriageCategory, detail: str,
              source_citation: str | None = None) -> TriageFlag:
        f = TriageFlag(event_id, int(tier), category, detail, source_citation)
        self.flags.append(f)
        return f

    def verdict(self) -> str:
        """PASS only when zero flags exist. CONTRACT_VIOLATION/CANON_GAP always force
        FAIL (a broken architectural guarantee or a fabrication risk is never merely
        partial); anything else open forces PARTIAL — never silently PASS."""
        if not self.flags:
            return "PASS"
        hard_fail = {TriageCategory.CONTRACT_VIOLATION, TriageCategory.CANON_GAP,
                     TriageCategory.FABRICATION_RISK}
        if any(f.category in hard_fail for f in self.flags):
            return "FAIL"
        return "PARTIAL"
