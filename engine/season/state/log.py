"""`season.state.log` -- THE EVENT LOG, and the three things it refuses.

`04:1024` step 3 names the log beside the gate and the act store, and the three are one unit
because the log is where the other two become checkable. A gate that mints receipts nobody
verifies is a naming convention; an act store nothing resolves against is a list.

THE THREE ASSERTIONS, all at `append`:

  1. **Every change on the Event is a receipt this gate minted.** Not "is a Receipt" -- minted,
     by identity (`Gate.issued`). This is what makes `changes[]` a record of writes rather than a
     set of claims about writes.
  2. **Every cause resolves.** `causes[] ⊆ log ids ∪ act ids ∪ {ROOT}`. #353 §19.4 calls this
     field *"the substrate of the entire emergent-narrative claim"*, and `H-80` records what the
     tree actually had: *"a log walker drops an unresolvable `[a.id]` exactly as it drops
     `[ROOT]`"*. Without the check an id naming nothing and no id at all are indistinguishable.
  3. **The kind is declared.** `04` §B.13 loader invariant 7: *"the log accepts no other kind"*. The
     roster (`data/verbs.py::EVENT_KINDS`) is HANDED IN at construction (`kinds`), never imported here:
     `state/log` reads nothing (`04` §A.2). `World` passes it, so a probe or a test that appends a kind
     no column declares declares it through `World(event_kinds=...)`; `loop/matter.py`'s direct appends
     are held to it like every other.

⚠ IT IS A LIST TO EVERY READER, AND THAT IS LOAD-BEARING. `world.py` iterates it, reverses it and
takes its length; `content_hash` folds it positionally; probes index it. Replacing the list with
an object that is merely list-LIKE would move the content hash if the fold order changed,
and would break `reversed(self.log)` in `world.py` silently -- `reversed` needs
`__reversed__` or the `__len__`+`__getitem__` pair, and a class with only `__iter__` raises. Both
are implemented for that reason, not for completeness.

⚠ AN EVENT CARRYING A BARE `StateChange` IS REFUSED (B09.09, H-145). It was admitted while
`harness/probes.py` built one outside any gate write; the probes now mint their changes through
the world's gate (`probes.py::apparatus_receipt`), so the log verifies every change and the
older class is no route round it. It is still Python: a determined author with the gate in hand
can open a window and mint. What it stops is the accident, not the adversary.
"""
from typing import Any, Callable, Iterator, Optional

from ..gaps import Forbidden
from .carriers import Event, Receipt
from .ids import ROOT


class EventLog:
    """Append-only event log with provenance checks. Indexable, iterable, reversible."""

    # roster-exempt: MECHANISM -- the log's own private attributes, as on `state/gate.py`.
    __slots__ = ("_events", "_ids", "_gate", "_act_ids", "_on_append", "_kinds")

    def __init__(self, gate: Any = None, kinds: frozenset = frozenset(),
                 act_ids: Optional[Callable[[], frozenset]] = None,
                 on_append: Optional[Callable[[Event], None]] = None) -> None:
        self._events: list[Event] = []
        self._ids: set[str] = set()
        self._gate = gate
        # REQUIRED IN SUBSTANCE: the default is the EMPTY roster, which refuses every kind, so a log built
        # without one cannot quietly accept anything. A VALUE handed in, not an import (see the head).
        self._kinds = frozenset(kinds)
        # A CALLABLE, not the store. The log must not import the act store (the package layering
        # in `state/__init__.py` is one-way and this would not break it, but a log that holds a
        # store can walk it), and the act ids change as RESOLVE folds. A thunk reads them at
        # append time without the log knowing what produced them.
        self._act_ids = act_ids or (lambda: frozenset())
        # IN-56. A CALLABLE, FOR THE SAME REASON AS `act_ids`: the owner of a LOG INDEX (`World`'s
        # last-emission maps) needs the act store to key an Event by what it is about
        # (`anchor_of`), and this module may read nothing (`04` §A.2). The log tells its owner an
        # Event was appended and reads nothing to do it. Every append -- `append`, `extend`, a
        # probe's direct `w.log.append` -- passes the one line below, so no site can bypass it.
        self._on_append = on_append

    def append(self, ev: Event) -> None:
        if not isinstance(ev, Event):
            raise Forbidden(
                f"the log holds Event, not {type(ev).__name__}", "S19",
                needs="an Event",
                law="acts go in the act store; the log holds what occurred")

        if ev.kind not in self._kinds:
            raise Forbidden(
                f"Event {ev.id!r} has kind {ev.kind!r}, which no emission column declares", "S19",
                needs="a kind in the derived roster (`data/verbs.py::EVENT_KINDS`): declare it in the "
                      "column that emits it, or hand a test kind in through `World(event_kinds=...)`",
                law="04 §B.13 loader invariant 7 -- the Event-kind roster is derived from every emission "
                    "column, and the log accepts no other kind")

        if self._gate is not None:
            for c in ev.changes:
                if not isinstance(c, Receipt):
                    # H-145 / B09.09: a bare `StateChange` is no receipt, so no gate vouches for it.
                    raise Forbidden(
                        f"Event {ev.id!r} ({ev.kind}) carries a bare {type(c).__name__} "
                        f"(subject {c.subject!r}, field {c.field!r}), not a receipt", "S16",
                        needs="a receipt from `Gate.mint`, obtained during a real gate write "
                              "(an apparatus builds one with `harness/probes.py::apparatus_receipt`)",
                        law="a change on an Event is one the gate wrote; a bare StateChange is an "
                            "assertion with no provenance, ID-9's own worked example")
                if not self._gate.issued(c):
                    raise Forbidden(
                        f"Event {ev.id!r} ({ev.kind}) carries a receipt this gate did not mint "
                        f"(serial {c.serial}, subject {c.subject!r}, field {c.field!r})", "S16",
                        needs="a receipt from `Gate.mint`, obtained during a real gate write",
                        law="a Receipt asserts THE GATE WROTE THIS; one the gate never issued "
                            "is an Event reporting a state change that did not happen, which "
                            "is ID-9's own worked example")

        # IN-56. MEMBERSHIP, NOT A UNION: a cause is resolved if it is ROOT, a prior Event id or an
        # act id; `self._act_ids()` is evaluated once, and only when some cause is neither.
        unresolvable = [c for c in ev.causes if c != ROOT and c not in self._ids]
        if unresolvable:
            act_ids_now = self._act_ids()
            unresolvable = [c for c in unresolvable if c not in act_ids_now]
        if unresolvable:
            raise Forbidden(
                f"Event {ev.id!r} ({ev.kind}) names cause(s) that resolve to nothing: "
                f"{unresolvable!r}", "S19.4",
                needs="each cause to be a prior Event id, an act id in the act store, or ROOT",
                law="#353 §19.4 makes `causes[]` the substrate of the emergent-narrative claim, "
                    "and H-80 measured what an unresolvable id is worth: a log walker drops it "
                    "exactly as it drops ROOT, so an id naming nothing and no id at all are the "
                    "same object to every reader")

        self._events.append(ev)
        self._ids.add(ev.id)
        if self._on_append is not None:
            self._on_append(ev)

    # -- the list surface every existing reader already uses -------------------------------
    def __iter__(self) -> Iterator[Event]:
        return iter(self._events)

    def __reversed__(self) -> Iterator[Event]:
        return reversed(self._events)

    def __len__(self) -> int:
        return len(self._events)

    def __getitem__(self, i):
        return self._events[i]

    def __bool__(self) -> bool:
        return bool(self._events)

    def __contains__(self, item: object) -> bool:
        return item in self._events

    def has_id(self, eid: str) -> bool:
        """Whether an Event with this id is logged: the id set `append` already keeps to resolve
        causes, read once more. v9 SC-02 `22b` step 23 -- `world_q.standing_crossed` asks it per
        person per lap, where `in` (a scan of Events) would cost the whole log each time."""
        return eid in self._ids

    def extend(self, events) -> None:
        """⚠ ROUTES THROUGH `append`, ONE AT A TIME, AND THAT IS THE WHOLE REASON IT EXISTS.
        `harness/corpus_run.py` does `w.log.extend([e1, e2])` where `e2` names `e1` as its
        cause, so the two must be checked IN ORDER -- a bulk insert that validated against the
        pre-extend id set would reject a legitimate chain built in one call. Implementing it as
        a loop also keeps the refusals on the path."""
        for e in events:
            self.append(e)

    def __repr__(self) -> str:
        return f"EventLog({len(self._events)} events)"
