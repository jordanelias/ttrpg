"""The gap taxonomy. Extracted from `shape.py` (step 1 of the shape.py decomposition,
ED-IN-0203) with no behaviour change: every symbol here is re-exported by `shape.py` so
`from ..shape import Forbidden` and `S.Unspecified` keep resolving exactly as before.

`InstrumentDefect` is deliberately NOT a subclass of `ShapeGap` -- see its own docstring.
Every `ShapeGap.__init__` writes a `TRACE.gap` row; that write is preserved verbatim below.
"""

from __future__ import annotations

import contextlib

from .trace_log import TRACE


class InstrumentDefect(Exception):
    """THE INSTRUMENT WAS CALLED WRONG. Deliberately NOT a `ShapeGap`.

    ⚠ THIS EXISTS BECAUSE THE DISTINCTION WAS LOST ONCE AND COST THREE FALSE FINDINGS. `W5` moved
    the Tenure store onto its subject; three probes still wrote `w.tenures += [...]`; the
    read-only view refused them; `run_cases` catches EVERY `ShapeGap` and files it as a GAP --
    so `F1`, `F20` and `P40` flipped PASS -> GAP and the gap count rose 73 -> 76. Every one of
    those was A BUG IN THE PROBE, reported as a hole in the design.

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
        # REV 2 fix (antagonist obs. C-5 recurrence): a refusal a probe DELIBERATELY provokes
        # to verify it fires is not a gap in the case-blocking sense. `expect_refusal()` marks
        # the window so a passing probe no longer deposits a blocking gap row.
        TRACE.gap(self.kind, what, where, needs, law)
        super().__init__(f"[{self.kind}] {what}  @{where}" + (f"  needs: {needs}" if needs else ""))


class Unspecified(ShapeGap):
    """ARCHITECTURE.md NAMES this and does not specify it. Part IX S61-S62 is its own list.
    REV 2: this is also the kind for EVERY unmarked cell -- matrix or Partition -- because
    S30/S30.1 are one doctrinal condition and splitting them across two counters made the kind
    histogram a measurement of the transcription rather than of the design."""
    kind = "UNSPECIFIED"


class Forbidden(ShapeGap):
    """A law forbids what the case requires."""
    kind = "FORBIDDEN"


class NoProducer(ShapeGap):
    """Something the case needs -- a state change, or an INPUT -- that no step of the loop
    produces. REV 2 widened the docstring: the question `q` is an input, not a state change,
    and it was the category's only member under the narrower wording."""
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
    row with no grade FAILS the export; it does not default to `assumption`. REV 2: this fires
    on an unregistered harness fixture, which is the same polarity applied to a number."""
    kind = "UNGRADED"


class Ineligible(ShapeGap):
    """The actor is not eligible for this verb. Not a gap in the design -- a fact about the actor
    -- so it EMITS rather than raising, per §E2's 'failure emits, never raises'.

    ⚠ THIS CLASS WAS SILENTLY DELETED AND IS RESTORED HERE. Step 1 of the decomposition
    (ED-IN-0203) removed it from `shape.py` and did not add it to this module, which is where the
    plan assigns it. **Nothing broke and nothing noticed, because it has no callers** — and that
    is precisely why it went unseen: a class with no users cannot fail a test when it disappears.

    Found on 2026-09-07 by a check worth keeping and running after any carve: take every
    top-level name in the PRE-carve `shape.py` and assert it still resolves as `S.<name>`. It ran
    199 names and returned four — `_HERE`, `_load_rosters` and `_load_write_matrix`, all
    deliberate (the anchor and the two loaders moved and are patched on the module that READS
    them), and this one, which was not deliberate at all.

    ⚠ AND IT HAS NO CALLERS TODAY, WHICH IS ITS OWN OPEN QUESTION AND NOT A REASON TO DROP IT.
    `E2`'s rule is that ineligibility EMITS rather than raises, so the fold's eligibility path
    correctly never constructs one; whether the taxonomy should carry a class the design forbids
    raising is a live call. Deleting it as part of a PURE MOVE was not the way to make it, and a
    move that quietly changes the taxonomy is not a pure move."""
    kind = "INELIGIBLE"


@contextlib.contextmanager
def expect_refusal():
    """Mark a window in which a refusal is EXPECTED -- the probe is verifying the law fires.
    Gap rows raised inside are tagged `expected` and excluded from blocking counts."""
    TRACE.expecting += 1
    try:
        yield
    finally:
        TRACE.expecting -= 1
