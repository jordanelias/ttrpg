"""B09.01 -- FADING IS COMPUTED WHERE A CLAIM IS READ, NOT WRITTEN BY A CLOCK.

A claim stored `confidence` is the value it was deposited at. What a person holds it at, at a tick, is
`state/ledgers.py::present_confidence(confidence, when, tick, decay)`: the deposit, less `decay` per season
elapsed. MATTER no longer walks ledgers, so nothing writes `Claim.confidence` and no `claim.decayed` Event
stands in the log (`write_matrix.yaml` row `(Claim, confidence)` names no step and no kind).

What each test proves, and the control that stops it passing vacuously:

  1. `present_confidence` reproduces the schedule of the write it replaces, tick by tick, against that
     write restated here as the oracle (a `max(0, c - decay)` per season after the deposit's own).
  2. A reader reads the present value: two claims whose stored values differ but which have both faded
     to zero tie, and the reader answers the first found, as the written zero did. Control: at
     `decay = 0` the stored values order them.
  3. A telling carries the present value (`said_of` -> `Said.confidence`), so a fade the writer no longer
     makes still lowers what a hearer is told.
  4. No `claim.decayed` Event in a two-season log, seeds 0, 1, 2. Control: the matrix row's old form
     would have one (the test reads the row and the roster, so the absence is not a missing instrument).
  5. Season one's log holds no fade Event, and its length is the before-reading's less that reading's
     `claim.decayed` count (both 0 at the before-reading: a claim has its first fade one season after its
     deposit). Two runs at one seed give one hash.
"""
from __future__ import annotations

from collections import Counter
from functools import lru_cache

import pytest

from engine.season.boot.realm import build_realm
from engine.season.data.fixtures import DEFAULT_FIXTURES
from engine.season.harness import probes as P
from engine.season.loop.driver import SeasonDriver, resolvable_verbs
from engine.season.queries.person_q import LedgerReader, said_of
from engine.season.state import ledgers
from engine.season.state.carriers import Claim

# THE BEFORE-READING, `reading @c765c86bbeda17da2c17744696732c843345c98e` (the tree this item was written
# on, unedited), seed 0, season 1, `PYTHONHASHSEED=0`: the realm builds with an empty log, one season adds
# 11936 Events, and none is a `claim.decayed` (a deposited claim's first fade came one season after its
# deposit, at the next MATTER).
BEFORE_SEASON_ONE_ENTRIES = 11936
BEFORE_SEASON_ONE_DECAYED = 0


def _old_write(confidence: int, when: int, tick: int, decay: int) -> int:
    """THE RETIRED MATTER WALK, restated as the oracle: a claim deposited at `when` was written
    `max(0, c - decay)` at each MATTER from `when + 1` to `tick` (the barrier runs at the season's own tick,
    before DELIBERATE and WITNESS), and a claim at 0 was skipped."""
    for _ in range(when + 1, tick + 1):
        if confidence <= 0:
            break
        confidence = max(0, confidence - decay)
    return confidence


@pytest.mark.parametrize("decay", [0, 5, 20, 33])
@pytest.mark.parametrize("deposited,when", [(100, 0), (63, 0), (25, 3), (100, 5)])
def test_present_confidence_matches_the_schedule_of_the_old_write(deposited, when, decay):
    checked = 0
    for tick in range(0, 8):
        if tick < when:
            continue                    # a claim is not read before it is deposited
        assert ledgers.present_confidence(deposited, when, tick, decay) == _old_write(deposited, when, tick, decay), (
            deposited, when, tick, decay)
        checked += 1
    assert checked >= 3
    # the control: the fade is observable here, so an identity function would fail this file
    assert ledgers.present_confidence(100, 0, 4, 20) == 20
    assert ledgers.present_confidence(100, 0, 9, 20) == 0                # clamped, never negative
    assert ledgers.present_confidence(100, 4, 2, 20) == 100              # a tick before the deposit elapses nothing


def _claim(cid, when, confidence, value=1):
    return Claim(cid, "p_a", "r_x", "stores.level", value, when, "firsthand", confidence, "own")


def test_a_reader_reads_the_present_value_not_the_stored_one():
    a, b = _claim("c_a", 0, 10), _claim("c_b", 0, 20)
    # raw: `b` is the more confident of the two, and wins
    assert LedgerReader([a, b]).belief_among() is b
    # at tick 4, decay 5 both have faded to 0 (`10 - 20`, `20 - 20`): a tie, and the first found wins
    assert LedgerReader([a, b], tick=4, decay=5).belief_among() is a
    # the control: at decay 0 nothing fades and the stored values order them as before
    assert LedgerReader([a, b], tick=4, decay=0).belief_among() is b
    # nothing was written: the stored value is the deposited one
    assert (a.confidence, b.confidence) == (10, 20)


def test_a_telling_carries_the_present_value():
    c = _claim("c_a", 1, 80)
    said = said_of([c], "r_x", DEFAULT_FIXTURES, tick=4)
    assert said.confidence == ledgers.present_confidence(80, 1, 4, DEFAULT_FIXTURES.claim_decay())
    assert said.confidence < 80                                       # the fade is real at the shipped rate
    assert said_of([c], "r_x", DEFAULT_FIXTURES, tick=1).confidence == 80     # the deposit's own tick elapses none


def test_eviction_ranks_on_the_present_value():
    # `eviction_key` is `confidence x (when + 1)`. Stored: `old` 50 x 1 = 50 against `new` 30 x 2 = 60, so
    # `old` leaves first. At tick 4, decay 10 (each `max(0, c - 10 x (4 - when))`): `old` 10 x 1 = 10, `new` 0 x 2 = 0,
    # so `new` leaves first. The fade, not the stored value, is what a ledger over its cap forgets by.
    old, new = _claim("c_old", 0, 50), _claim("c_new", 1, 30)
    assert [c.id for c in ledgers.evict_over_cap([old, new], 1)] == ["c_old"]
    assert [c.id for c in ledgers.evict_over_cap([old, new], 1, tick=4, decay=10)] == ["c_new"]
    # the control: at decay 0 the present value is the stored one
    assert [c.id for c in ledgers.evict_over_cap([old, new], 1, tick=4, decay=0)] == ["c_old"]


@lru_cache(maxsize=None)
def _run(seed: int, seasons: int):
    w = build_realm(seed)
    d = SeasonDriver(w)
    ch = P.chooser(w, verbs=resolvable_verbs())
    lens = []
    for _ in range(seasons):
        d.season(ch, question=None, contest_max_depth=w.fixtures.get("contest_max_depth"))
        lens.append(len(w.log))
    return w, tuple(lens)


def test_the_matrix_row_names_no_clock_and_no_kind():
    from engine.season.data.matrix import MATRIX
    row = MATRIX[("Claim", "confidence")]      # the row stays: the field is still a field
    assert not row.steps, "a step still writes Claim.confidence"
    assert not row.emits, "the row still names a kind"


@pytest.mark.parametrize("seed", [0, 1, 2])
def test_no_claim_decayed_in_a_two_season_log(seed):
    w, lens = _run(seed, 2)
    kinds = Counter(e.kind for e in w.log)
    assert len(lens) == 2 and lens[1] > lens[0] > 0
    assert kinds["claim.deposited"] > 0, "no deposit in the log: the absence below observes nothing"
    assert kinds["claim.decayed"] == 0


def test_season_one_log_holds_no_fade_events():
    w, lens = _run(0, 1)
    kinds = Counter(e.kind for e in w.log)
    assert kinds["claim.decayed"] == 0
    # the build leaves an empty log, so season one's new entries are the whole log (the before-reading's
    # count less its `claim.decayed` count, `BEFORE_SEASON_ONE_DECAYED`)
    assert lens[0] == BEFORE_SEASON_ONE_ENTRIES - BEFORE_SEASON_ONE_DECAYED


def test_two_runs_at_one_seed_give_one_hash():
    w1, _ = _run(0, 1)
    w2 = build_realm(0)
    d = SeasonDriver(w2)
    d.season(P.chooser(w2, verbs=resolvable_verbs()), question=None,
             contest_max_depth=w2.fixtures.get("contest_max_depth"))
    assert w1.content_hash() == w2.content_hash()
