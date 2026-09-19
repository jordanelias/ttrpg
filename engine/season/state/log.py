"""`season.state.log` -- THE EVENT LOG, and the two things it refuses.

`04:1024` step 3 names the log beside the gate and the act store, and the three are one unit
because the log is where the other two become checkable. A gate that mints receipts nobody
verifies is a naming convention; an act store nothing resolves against is a list.

THE TWO ASSERTIONS, both at `append`:

  1. **Every change on the Event is a receipt this gate minted.** Not "is a Receipt" -- minted,
     by identity (`Gate.issued`). This is what makes `changes[]` a record of writes rather than a
     set of claims about writes.
  2. **Every cause resolves.** `causes[] ⊆ log ids ∪ act ids ∪ {ROOT}`. #353 §19.4 calls this
     field *"the substrate of the entire emergent-narrative claim"*, and `H-80` records what the
     tree actually had: *"a log walker drops an unresolvable `[a.id]` exactly as it drops
     `[ROOT]`"*. An id naming nothing and no id at all were indistinguishable. They are not now.

⚠ IT IS A LIST TO EVERY READER, AND THAT IS LOAD-BEARING. `world.py` iterates it, reverses it and
takes its length; `content_hash` folds it positionally; probes index it. Replacing the list with
an object that is merely list-LIKE would have moved the content hash if the fold order changed,
and would have broken `reversed(self.log)` at `world.py:625` silently -- `reversed` needs
`__reversed__` or the `__len__`+`__getitem__` pair, and a class with only `__iter__` raises. Both
are implemented for that reason, not for completeness.

⚠ WHAT IS DELIBERATELY NOT REFUSED: an Event carrying a bare `StateChange`. Refusing it outright
is the correct end state and it is not reachable in this unit -- `harness/probes.py:1797` builds
one outside any gate write, and rewriting the probe corpus is its own change. So a bare
`StateChange` is admitted and a `Receipt` is verified: the type you reach for when you mean "the
gate wrote this" is checked, and the one that predates the distinction is not. **This is a
transitional asymmetry and it is the file's weakest seam** -- anyone wanting to forge provenance
today simply uses the older class. What it stops is the accident, not the adversary. `G4`
finalises the effect contract and is where the bare class should stop being admitted.
"""
from typing import Any, Callable, Iterator, Optional

from ..gaps import Forbidden
from .carriers import Event, Receipt
from .ids import ROOT


class EventLog:
    """Append-only event log with provenance checks. Indexable, iterable, reversible."""

    # roster-exempt: MECHANISM -- the log's own private attributes, as on `state/gate.py`.
    __slots__ = ("_events", "_ids", "_gate", "_act_ids")

    def __init__(self, gate: Any = None,
                 act_ids: Optional[Callable[[], frozenset]] = None) -> None:
        self._events: list[Event] = []
        self._ids: set[str] = set()
        self._gate = gate
        # A CALLABLE, not the store. The log must not import the act store (the package layering
        # in `state/__init__.py` is one-way and this would not break it, but a log that holds a
        # store can walk it), and the act ids change as RESOLVE folds. A thunk reads them at
        # append time without the log knowing what produced them.
        self._act_ids = act_ids or (lambda: frozenset())

    def append(self, ev: Event) -> None:
        if not isinstance(ev, Event):
            raise Forbidden(
                f"the log holds Event, not {type(ev).__name__}", "S19",
                needs="an Event",
                law="acts go in the act store; the log holds what occurred")

        if self._gate is not None:
            for c in ev.changes:
                if isinstance(c, Receipt) and not self._gate.issued(c):
                    raise Forbidden(
                        f"Event {ev.id!r} ({ev.kind}) carries a receipt this gate did not mint "
                        f"(serial {c.serial}, subject {c.subject!r}, field {c.field!r})", "S16",
                        needs="a receipt from `Gate.mint`, obtained during a real gate write",
                        law="a Receipt asserts THE GATE WROTE THIS; one the gate never issued "
                            "is an Event reporting a state change that did not happen, which "
                            "is ID-9's own worked example")

        known = self._ids | self._act_ids() | {ROOT}
        unresolvable = [c for c in ev.causes if c not in known]
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

    def extend(self, events) -> None:
        """⚠ ROUTES THROUGH `append`, ONE AT A TIME, AND THAT IS THE WHOLE REASON IT EXISTS.
        `harness/corpus_run.py:565` does `w.log.extend([e1, e2])` where `e2` names `e1` as its
        cause, so the two must be checked IN ORDER -- a bulk insert that validated against the
        pre-extend id set would reject a legitimate chain built in one call. Implementing it as
        a loop rather than letting `AttributeError` stand also keeps the refusals on the path:
        the alternative fix was to rewrite the caller, which would have quietly moved one more
        log write outside the checks."""
        for e in events:
            self.append(e)

    def __repr__(self) -> str:
        return f"EventLog({len(self._events)} events)"
