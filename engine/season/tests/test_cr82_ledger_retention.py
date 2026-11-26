"""CR-82 (B10-09 close two, `ED-IN-0319`) -- WHAT A PERSON KNOWS OF OTHERS IS KEPT FOR YEARS, NOT SEASONS.
Jordan, 2026-11-04: "people don't stop knowing people or claims that quickly". The lever is `ledger_cap`
(`data/fixtures.py`, H-09's injected value), raised 200 -> 3200; the S20/S34 comparator
(`state/ledgers.py::eviction_key`) is unchanged.

MEASURED at four and eight seasons (`build_realm(s)`, the cap swept after build, `harness/storybar.py::drive`, PYTHONHASHSEED=0), the
236 acquaintance claims `seed_acquaintances` writes still held at season 4: seed 1, 6 at cap 200 and 208 at
3200; through eight seasons (two years at four seasons to the year, `ED-IN-0332`) 202 and 196 of 236 at 3200
on seeds 0 and 1, 0 and 0 at 200. H-09's `cite:` carries the whole sweep and the cost. ⚠ The bounds asserted
below are deliberately loose (above 200 at the shipped cap, below 180 at 200): the test is about the lever,
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
from ..boot.realm import build_realm

SEED = 1
SEASONS = 2
CONTROL_CAP = 200          # the value before CR-82; the fade is read at it
HELD_FLOOR = 200           # at the shipped cap, held at season 2 (measured 221; 217 with the task draw on)
FADED_CEILING = 180        # at the control cap, held at season 2 (measured 147; 172 with the task draw on, B07.99: fewer acts deposit claims, so fewer are evicted)


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


