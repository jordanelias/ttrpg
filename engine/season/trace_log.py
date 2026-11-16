"""The tracing channel. Every decision made and every step performed is logged here.

This module is the TRACING AGENT'S instrument. It records, in order:
  - every STEP entered and left, with the barrier it opened or closed
  - every DECISION taken by the shape (a branch that could have gone another way)
  - every WRITE attempted, with its write class and whether the matrix admitted it
  - every ACT chosen, every EVENT emitted, every CLAIM deposited
  - every GAP raised, with the section of ARCHITECTURE.md that governs it

It stores nothing derived. It is append-only, which is the same property the design
gives its own log (ARCHITECTURE.md 19), and for the same reason: a trace that can be
rewritten cannot be evidence.

IT RECORDS ONLY WHILE AN INSTRUMENT HAS OPENED IT. `with TRACE.recording():` is the window; outside
one every row, and every gap `gap()` would have kept, is dropped at the door, so a run nobody is
reading does not build rows (one per write, event and query) for nothing. The
instruments that read the rows -- `harness/report.py`, `run_cases.py`, `soak.py` -- open it where they
read; a test that reads `TRACE.rows` opens it around the call. `case` and `expecting` are state a
reader sets, not records, and they are kept whether or not a window is open.
"""

from __future__ import annotations

import contextlib
import json
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Row:
    seq: int
    channel: str          # STEP | BARRIER | DECISION | WRITE | ACT | EVENT | CLAIM | GAP | QUERY | NOTE
    case: str
    what: str
    where: str = ""       # ARCHITECTURE.md section
    detail: dict = field(default_factory=dict)


class Trace:
    def __init__(self) -> None:
        self.rows: list[Row] = []
        self.case = "-"
        self._seq = 0
        self.expecting = 0      # >0 while a probe is deliberately provoking a refusal
        self.gaps: list[dict] = []
        self._open = 0          # windows currently open: `recording()` nests, and a count keeps it so

    @contextlib.contextmanager
    def recording(self):
        """Open the trace: rows and gaps are kept while this block runs, dropped outside one."""
        self._open += 1
        try:
            yield self
        finally:
            self._open -= 1

    def _row(self, channel: str, what: str, where: str = "", **detail: Any) -> None:
        if not self._open:
            return
        self._seq += 1
        self.rows.append(Row(self._seq, channel, self.case, what, where, detail))

    def step(self, name: str, phase: str) -> None:
        self._row("STEP", f"{phase} {name}", "S23")

    def barrier(self, n: int, name: str) -> None:
        self._row("BARRIER", f"barrier {n} - {name}", "S23")

    def decision(self, what: str, where: str, chose: str, alternatives: list[str],
                 not_implemented: list[str] | None = None) -> None:
        """A branch the shape took that could have gone another way. This is the row the
        tracing agent exists for: a decision nobody records is a decision nobody can audit."""
        self._row("DECISION", what, where, chose=chose, alternatives=alternatives,
                  not_implemented=not_implemented or [])

    def write(self, thing: str, wclass: str, step: str, admitted: bool, where: str = "S30") -> None:
        self._row("WRITE", thing, where, write_class=wclass, step=step, admitted=admitted)

    def act(self, actor: str, verb: str, budget_left: int) -> None:
        self._row("ACT", f"{actor} :: {verb}", "S26", budget_left=budget_left)

    def scene_act(self, actor: str, verb: str, scenes_left: int, n: int, of: int) -> None:
        """`W17`. ONE INTERACTION, INSIDE ONE SCENE, WITH BOTH UNITS NAMED.

        `act()` takes a single `budget_left`; a SCENE budget minus an INTERACTION index in that
        one field puts two units in it, so this records two fields."""
        self._row("ACT", f"{actor} :: {verb}", "S26",
                  scenes_left=scenes_left, interaction=f"{n}/{of}")

    def event(self, eid: str, kind: str, causes: list[str]) -> None:
        self._row("EVENT", f"{kind} [{eid}]", "S19", causes=causes)

    def claim(self, holder: str, eid: str, source: str) -> None:
        self._row("CLAIM", f"{holder} <- {eid}", "S20", source=source)

    def query(self, name: str, side: str) -> None:
        self._row("QUERY", name, "S17", side=side)

    def note(self, what: str, where: str = "") -> None:
        self._row("NOTE", what, where)

    def gap(self, kind: str, what: str, where: str, needs: str, law: str) -> None:
        """A refusal a probe DELIBERATELY provokes to verify that it fires is recorded, but
        marked `expected` -- it is evidence the law works, not evidence a case is blocked.
        Without this a PASSING probe deposits a BLOCKING gap row."""
        expected = self.expecting > 0
        self._row("GAP", f"[{kind}] {what}", where, needs=needs, law=law, expected=expected)
        if not self._open:
            return
        self.gaps.append(
            dict(kind=kind, what=what, where=where, needs=needs, law=law,
                 case=self.case, expected=expected)
        )

    def dump_text(self) -> str:
        out = []
        for r in self.rows:
            d = ""
            if r.detail:
                d = "  " + " ".join(f"{k}={json.dumps(v)}" for k, v in r.detail.items())
            out.append(f"{r.seq:>6}  {r.case:<20} {r.channel:<9} {r.what}"
                       + (f"  @{r.where}" if r.where else "") + d)
        return "\n".join(out)

    def counts(self) -> dict:
        c: dict[str, int] = {}
        for r in self.rows:
            c[r.channel] = c.get(r.channel, 0) + 1
        return c


TRACE = Trace()
