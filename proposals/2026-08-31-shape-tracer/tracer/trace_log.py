"""The tracer's log: the sequence of the idealized code, and the gap register.

Two outputs, and they are different kinds of thing:

  * THE TRACE — the ordered sequence of steps, signature calls, writes (with class and driver)
    and events. This is what "run accompanying tracers that log the sequence of the idealized
    code" asks for. It is evidence that a case ran, and in what order.

  * THE GAP REGISTER — every place the shape could not carry a case. This is the finding.
    A gap is recorded with its kind, what failed, where, and what it needs.
"""

from __future__ import annotations

import json
from collections import Counter
from dataclasses import dataclass, field, asdict
from typing import Any, Optional


@dataclass
class Gap:
    kind: str
    what: str
    where: str
    needs: str
    case: str
    season: int
    step: Optional[str]


class TraceLog:
    def __init__(self):
        self.lines: list[str] = []
        self.gaps: list[Gap] = []
        self.case: str = "-"
        self.cur_season: int = 0
        self.cur_step: Optional[str] = None
        self._seen: set[tuple] = set()
        self.acts = 0
        self.events = 0
        self.writes = 0

    # -- context ------------------------------------------------------------
    def start_case(self, name: str):
        self.case = name
        self.cur_season = 0
        self.cur_step = None
        self.lines.append(f"\n=== CASE {name} ===")

    # -- sequence -----------------------------------------------------------
    def season(self, n: int):
        self.cur_season = n
        self.lines.append(f"-- SEASON {n} --")

    def step(self, s):
        self.cur_step = getattr(s, "value", str(s))
        self.lines.append(f"  [{self.cur_step}]")

    def call(self, fn: str, subject: str, omitted: str = ""):
        tail = f"   (omits {omitted})" if omitted else ""
        self.lines.append(f"    call {fn}({subject}){tail}")

    def act(self, a):
        self.acts += 1
        self.lines.append(f"    ACT  {a.actor} :: {a.verb} -> {a.target}")

    def event(self, ev):
        self.events += 1
        self.lines.append(f"    EVT  {ev.id} {ev.family} @{ev.subject} causes={ev.causes}")

    def write(self, step, wclass, kind, fieldname, subject, driver, value):
        self.writes += 1
        self.lines.append(
            f"    W    {kind}.{fieldname}[{subject}] <- {value!r}  "
            f"class={getattr(wclass,'value',wclass)} driver={driver}")

    def note(self, what: str, where: str = ""):
        self.lines.append(f"    ..   {what} {where}")

    # -- findings -----------------------------------------------------------
    def gap(self, kind: str, what: str, where: str, needs: str):
        key = (kind, what, where, self.case)
        self.lines.append(f"    !!   {kind}: {what} @{where}")
        if key in self._seen:
            return
        self._seen.add(key)
        self.gaps.append(Gap(kind=kind, what=what, where=where, needs=needs,
                             case=self.case, season=self.cur_season, step=self.cur_step))

    # -- output -------------------------------------------------------------
    def text(self) -> str:
        return "\n".join(self.lines)

    def gap_rows(self) -> list[dict]:
        return [asdict(g) for g in self.gaps]

    def summary(self) -> dict:
        return {
            "acts": self.acts, "events": self.events, "writes": self.writes,
            "gaps_total": len(self.gaps),
            "gaps_by_kind": dict(Counter(g.kind for g in self.gaps)),
            "gaps_by_case": dict(Counter(g.case for g in self.gaps)),
        }

    def dump(self, trace_path: str, gaps_path: str):
        with open(trace_path, "w") as f:
            f.write(self.text() + "\n")
        with open(gaps_path, "w") as f:
            json.dump({"summary": self.summary(), "gaps": self.gap_rows()}, f, indent=1)


TRACE = TraceLog()
