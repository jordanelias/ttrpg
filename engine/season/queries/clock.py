"""`season.queries.clock` -- THE ONE FOLD OF A CLOCK (v12 B21d.02, CR-89 commit (1); ED-IN-0343, ED-IN-0345).

A **clock** is a running total folded from the log's Events of named kinds, read when asked and never stored, as a doomsday
clock is a count that advances as things happen. Its row is `rosters.yaml: tables.clocks` (`data/rosters.py::clocks`, a
`ClockRow`); its store is `w.log`. This module owns the arithmetic and nothing else: it takes Events ALREADY ATTRIBUTED
(`ClockEvent`) and a row, and reads no world, so the world-side reading (`queries/world_q.py::clock`, every act-caused Event in
the log) and the person-side reading (`queries/person_q.py::believed_clock`, the Events a person holds a claim of) are the same
fold over two sets of Events. Attribution -- who acted and on whom -- is `world_q.clock_events`', its one owner.

THE FOLD: from `row.start`, season by season in order of `ClockEvent.tick`, add `sign * weight` for every feeder each Event
matches (its `kind`; its `actor_faction` unless the feeder's is `None`, "any"; a faction in its `against` unless the feeder's is
`None`), cap that season's sum at `row.season_cap` either way (`None`: uncapped), then clamp the running total to
`[row.lo, row.hi]`. An Event counts once per feeder it matches; the caller passes each Event once.

v12 B21d.03 (CR-89 commit (2); ED-IN-0341): THE BREAKING POINT'S COUNT lives beside the fold for the same reason -- both sides read it
(`world_q.sittings_failed` over the log, `person_q.believed_sittings_failed` over what a person holds), and `person_q` may not import `world_q`.
`sittings_failed_of` takes sittings' Events ALREADY READ (`SittingEvent`, `world_q.sitting_events` their one reader) and counts; it reads no world.
"""
from __future__ import annotations

from typing import Iterable, NamedTuple, Optional


class ClockEvent(NamedTuple):
    """ONE EVENT AS A CLOCK READS IT: `event`, its id (the person-side fold counts one Event once by it); `tick`, its
    `emitted_at` (its season); `kind`; `actor_faction`, the faction of its causing act's actor at that tick, or `None`;
    `against`, the factions it acted on (`world_q.clock_events` says how they are read)."""
    event: str
    tick: int
    kind: str
    actor_faction: Optional[str]
    against: frozenset


def _matches(f, e: ClockEvent) -> bool:
    return (f.kind == e.kind
            and (f.actor_faction is None or f.actor_faction == e.actor_faction)
            and (f.against is None or f.against in e.against))


def clock_fold(events: Iterable[ClockEvent], row) -> float:
    """THE CLOCK'S VALUE over `events` (each a `ClockEvent`, each Event once) by `row` (a `data/rosters.py::ClockRow`). Pure: no
    world, no store, no draw; the same Events and row give the same number. With no Event it is `row.start`."""
    by_tick: dict = {}
    for e in events:
        delta = sum(f.sign * f.weight for f in row.feeders if _matches(f, e))
        if delta:
            by_tick[e.tick] = by_tick.get(e.tick, 0) + delta
    value = row.start
    for t in sorted(by_tick):
        step = by_tick[t]
        if row.season_cap is not None:
            step = max(-row.season_cap, min(row.season_cap, step))
        value = max(row.lo, min(row.hi, value + step))
    return value


class SittingEvent(NamedTuple):
    """ONE EVENT OF A SITTING AS THE BREAKING POINT READS IT: `event`, its id; `sitting`, the act whose proceeding it was written by (`Event.causes[0]`:
    a sitting is one act, and every Event the act emits carries it); `tick`, its `emitted_at`; `kind`; `arrangement`, the row the sitting was held under
    (the head of `Event.ending`); `determined`, whether this Event is the determination (`data/verbs.py::DISPOSAL_EVENTS["determine"]`)."""
    event: str
    sitting: str
    tick: int
    kind: str
    arrangement: str
    determined: bool


def sittings_failed_of(events: Iterable[SittingEvent], arrangement: str, window: int) -> int:
    """OF THE LAST `window` SITTINGS OF `arrangement` AMONG `events`, HOW MANY DISPOSED OF NOTHING -- a sitting disposes of nothing when none of its
    Events (here) is the determination. Sittings are ordered by their first Event's tick, then by the order `events` gives them (the log's). Pure: no
    world, no store; `window` 0 reads 0."""
    first: dict = {}
    disposed: dict = {}
    for n, e in enumerate(events):
        if e.arrangement != arrangement:
            continue
        first.setdefault(e.sitting, (e.tick, n))
        disposed[e.sitting] = disposed.get(e.sitting, False) or e.determined
    last = sorted(first, key=first.get)[-window:] if window > 0 else []
    return sum(1 for s in last if not disposed[s])
