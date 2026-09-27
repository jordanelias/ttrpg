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
from ..state.gate import Token
from ..trace_log import TRACE



# -- CALENDAR -- barrier 1 -- DECIDES NOTHING (S24) ----------------------
def calendar(self, token: Token) -> None:
    w = self.w
    w.step = Step.CALENDAR
    TRACE.step("CALENDAR", "enter"); TRACE.barrier(1, "CALENDAR")
    w.discard_caches()
    for did, d in list(w.dates.items()):
        if d.get("due_at") != w.tick:
            continue
        vacant = not d.get("holder")
        TRACE.decision(f"date {did} came due", "S24",
                       chose="fire-and-lapse" if vacant else "fire-as-sitting",
                       alternatives=["block until a holder exists", "defer to next season"])
        w.write("Date", token, lambda d=d: d.__setitem__("fired", True),
                record_kind="Date", fieldname="fired", driver="Event")
        if not vacant:
            w.write("DocketItem", token,
                    lambda did=did: w.docket.append({"date": did, "matter": None}),
                    record_kind="DocketItem", fieldname="matter", driver="Event")
    TRACE.step("CALENDAR", "leave")
