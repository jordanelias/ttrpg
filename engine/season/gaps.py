"""The gap taxonomy. Importers name this module directly (`from ..gaps import Forbidden`).

`InstrumentDefect` is deliberately NOT a subclass of `ShapeGap` -- see its own docstring.
Every `ShapeGap.__init__` writes a `TRACE.gap` row.
"""

from __future__ import annotations

import contextlib

from .trace_log import TRACE


class InstrumentDefect(Exception):
    """THE INSTRUMENT WAS CALLED WRONG. Deliberately NOT a `ShapeGap`.

    ⚠ THIS EXISTS BECAUSE `run_cases` CATCHES EVERY `ShapeGap` AND FILES IT AS A GAP. A probe
    that wrote `w.tenures += [...]` against the read-only Tenure view was refused, and a refusal
    that is a `ShapeGap` is filed as a hole in the design: A BUG IN THE PROBE, reported as a gap.

    That is the worst failure this instrument can have. Its entire output is the claim *"here is
    what #353 does not specify"*, and a call-site bug that lands in that column corrupts the
    measurement in the direction that flatters it -- more holes found. `CLAUDE.md` §0.1 point 4:
    a number without a control is not a measurement, in EITHER direction.

    So: a refusal that means *"the design forbids this"* is a `Forbidden` and is a finding. A
    refusal that means *"you called me wrong"* is this, and is an INSTRUMENT-ERROR -- a bucket
    `run_cases` already had. The separation is by CLASS, so no probe can absorb one as the other,
    and `test_w5_no_gap_is_an_instrument_defect` is the falsifier."""


class ShapeGap(Exception):
    kind = "GAP"

    def __init__(self, what: str, where: str, needs: str = "", law: str = ""):
        self.what, self.where, self.needs, self.law = what, where, needs, law
        # A refusal a probe DELIBERATELY provokes to verify it fires is not a gap in the
        # case-blocking sense. `expect_refusal()` marks the window so a passing probe does not
        # deposit a blocking gap row.
        TRACE.gap(self.kind, what, where, needs, law)
        super().__init__(f"[{self.kind}] {what}  @{where}" + (f"  needs: {needs}" if needs else ""))


class Unspecified(ShapeGap):
    """ARCHITECTURE.md NAMES this and does not specify it. Part IX S61-S62 is its own list.
    This is also the kind for EVERY unmarked cell -- matrix or Partition -- because
    S30/S30.1 are one doctrinal condition and splitting them across two counters made the kind
    histogram a measurement of the transcription rather than of the design."""
    kind = "UNSPECIFIED"


class Forbidden(ShapeGap):
    """A law forbids what the case requires."""
    kind = "FORBIDDEN"


class NoProducer(ShapeGap):
    """Something the case needs -- a state change, or an INPUT -- that no step of the loop
    produces. The question `q` is an input, not a state change."""
    kind = "NO-PRODUCER"


class Collision(ShapeGap):
    """Two in-chain documents specify incompatible things. Part IX S62 is its own list."""
    kind = "COLLISION"


class Unowned(ShapeGap):
    """A value the case must change that the ownership table (S22) assigns to nobody. S22.3
    names four itself. Distinct from UNSPECIFIED: a specified mechanism with no writer."""
    kind = "UNOWNED"


class Ungraded(ShapeGap):
    """S42.2's polarity rule: zero evidence maps to the verdict AGAINST the thing measured. A
    row with no grade FAILS the export; it does not default to `assumption`. This fires
    on an unregistered harness fixture, which is the same polarity applied to a number."""
    kind = "UNGRADED"


@contextlib.contextmanager
def expect_refusal():
    """Mark a window in which a refusal is EXPECTED -- the probe is verifying the law fires.
    Gap rows raised inside are tagged `expected` and excluded from blocking counts."""
    TRACE.expecting += 1
    try:
        yield
    finally:
        TRACE.expecting -= 1
