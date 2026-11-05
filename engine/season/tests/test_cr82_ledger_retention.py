"""CR-82 (B10-09 close two, `ED-IN-0319`) -- WHAT A PERSON KNOWS OF OTHERS IS KEPT FOR YEARS, NOT SEASONS.
Jordan, 2026-11-04: "people don't stop knowing people or claims that quickly". The lever is `ledger_cap`
(`data/fixtures.py`, H-09's injected value), raised 200 -> 3200; the S20/S34 comparator
(`state/ledgers.py::eviction_key`) is unchanged.

MEASURED at four and eight seasons (`build_realm(s)`, the cap swept after build, `harness/storybar.py::drive`, PYTHONHASHSEED=0), the
236 acquaintance claims `seed_acquaintances` writes still held at season 4: seed 1, 6 at cap 200 and 208 at
3200; through eight seasons (two years at four seasons to the year, `ED-IN-0332`) 202 and 196 of 236 at 3200
on seeds 0 and 1, 0 and 0 at 200. H-09's `cite:` carries the whole sweep and the cost. ⚠ The bounds asserted
below are deliberately loose (above 200 at the shipped cap, below 170 at 200): the test is about the lever,
not a golden, and every pin that does reach the cap is re-recorded where it lives.

⚠ TWO SEASONS, NOT EIGHT OR FOUR: this directory no longer builds a four-season realm (the user's v9 section 0.5
ruling, recorded at the `season-tests` CI job's comment), and eight seasons is about six minutes on one seed. At
two seasons the cap-200 control has already lost acquaintance claims (147 of 236 held on seed 1) and the
shipped cap has lost almost none (221). The first producer's four-season form (6 against 208 at season 4) is
the measurement in H-09's `cite:`; this test observes the lever, not the horizon.
"""

from __future__ import annotations


from ..data.fixtures import DEFAULT_FIXTURES
from ..harness import storybar
from ..harness.populated import build_realm

SEED = 1
SEASONS = 2
CONTROL_CAP = 200          # the value before CR-82; the fade is read at it
HELD_FLOOR = 200           # at the shipped cap, held at season 2 (measured 221)
FADED_CEILING = 170        # at the control cap, held at season 2 (measured 147)


def _held_after(cap: int) -> tuple[int, int]:
    """Run SEASONS seasons on SEED with `ledger_cap` swept to `cap` after build; return
    (acquaintance claims written, still held)."""
    w = build_realm(SEED)
    w.fixtures = w.fixtures.sweep("ledger_cap", cap)
    assert w.fixtures.get("ledger_cap") == cap
    acq = set(w._acquaintances)
    storybar.drive(SEED, SEASONS, "off", world=w)
    assert w.tick == SEASONS, w.tick
    held = sum(1 for p in w.persons.values() for c in p.ledger if c.id in acq)
    return len(acq), held


def test_acquaintances_survive_at_the_shipped_cap_and_fade_at_200():
    """EXIT: at the shipped cap the acquaintance claims are still held at season 2. PLANTED FAILURE, in the
    same test: the cap swept back to 200 reproduces the fade (below FADED_CEILING, so below HELD_FLOOR: the
    exit's own bound would be red at the control)."""
    shipped = DEFAULT_FIXTURES.get("ledger_cap")
    assert shipped > CONTROL_CAP, shipped
    written, held = _held_after(shipped)
    assert written == 236, written
    assert held > HELD_FLOOR, (shipped, held)
    written_c, held_c = _held_after(CONTROL_CAP)
    assert written_c == 236, written_c
    assert held_c < FADED_CEILING, held_c     # below HELD_FLOOR too: the exit's assertion is red at 200
