"""`loop/calendar.py` -- CALENDAR -- barrier 1. `04 §A.2`: owns `Date.fired`, `DocketItem`, `ConveningCondition`; emits `date.fired` / `docket.formed`; token CALENDAR.

⚠ **THE BODY IS THE DRIVER'S OWN, BOUND BACK ONTO THE CLASS -- NOT A DELEGATING STUB.**
`loop/driver.py` ends with `SeasonDriver.calendar = calendar`, so `SeasonDriver.calendar` IS this
function and `inspect.getsource(SeasonDriver.calendar)` returns THIS SOURCE. Eight tests read a
step's body that way -- three of them `witness`'s, one of those a pure NEGATIVE assertion --
and a stub would fail two and silently vacate the third, which is why step 9 of the
decomposition (ED-IN-0203) refused to delegate. Step 5 established the technique when
`class Query` bound module functions as staticmethods.

⚠ **THE TOKEN IS HANDED IN BY THE DRIVER (G2).** `SeasonDriver.season` mints a CALENDAR `Token`
through `loop/driver.py::mint_token` and passes it as `token`; every gate write below presents
it. This module constructs none and calls no minter -- `tests/test_g2_token.py` fails if it does.
"""

from __future__ import annotations

from ..data.matrix import Step
from ..state.carriers import Event
from ..state.gate import Token
from ..state.ids import ROOT
from ..trace_log import TRACE



# -- CALENDAR -- barrier 1 -- DECIDES NOTHING (S24) ----------------------
def calendar(self, token: Token) -> list[Event]:
    w = self.w
    w.step = Step.CALENDAR
    TRACE.step("CALENDAR", "enter"); TRACE.barrier(1, "CALENDAR")
    w.discard_caches()
    # ⚠ RETURNS ITS OWN EMISSIONS, SO `season()` CAN HAND THEM TO WITNESS BESIDE MATTER'S (IN-29).
    # `World.write` buffers an emission for fan-out ONLY at `Step.MATTER` (`state/world.py`, the
    # `_emitted_by_write` guard, which exists to keep WITNESS's own `claim.deposited` from looping),
    # so CALENDAR's `date.fired` reached `w.log` and nothing else. The log tail since this mark is
    # exactly what this barrier's writes emitted -- nothing else writes between here and the return.
    _mark = len(w.log)
    for did, d in list(w.dates.items()):
        if d.get("due_at") != w.tick:
            continue
        vacant = not d.get("holder")
        TRACE.decision(f"date {did} came due", "S24",
                       chose="fire-and-lapse" if vacant else "fire-as-sitting",
                       alternatives=["block until a holder exists", "defer to next season"])
        # ⚠ CHAINED ON THE VENUE, NOT `did` -- `last_emission_of`'s second argument must equal
        # the write's own `subject=`, because it matches `anchor_of(...) == subject` and
        # `anchor_of`'s tier 2 reads back exactly the `subject=` a write passed (`W4`,
        # `state/world.py:1042-1046`). Every MATTER clock this mirrors (`body.changed`/`pid`,
        # `stores.changed`/`yield.taken`/`rid` in `loop/matter.py`) uses the SAME value in both
        # places; chaining on `did` here would look for a prior Event whose subject is `did`,
        # which no `date.fired` Event ever carries (its subject is always the venue) -- so the
        # chain would silently never leave `[ROOT]`, on every date, forever.
        prior = w.last_emission_of("date.fired", d.get("venue"))
        w.write("Date", token, lambda d=d: d.__setitem__("fired", True),
                record_kind="Date", fieldname="fired", driver="Event",
                emits="date.fired", subject=d.get("venue"),
                causes=[prior] if prior else [ROOT])
        if not vacant:
            w.write("DocketItem", token,
                    lambda did=did: w.docket.append({"date": did, "matter": None}),
                    record_kind="DocketItem", fieldname="matter", driver="Event")
    TRACE.step("CALENDAR", "leave")
    return list(w.log[_mark:])
