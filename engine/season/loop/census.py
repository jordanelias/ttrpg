"""`loop/census.py` -- CENSUS -- shares WITNESS's join. `04 §A.2`: owns `(Person, exists)` on individuation, `weight`, `envelope`; emits `person.individuated`; token MATTER.

⚠ **THE BODY IS THE DRIVER'S OWN, BOUND BACK ONTO THE CLASS -- NOT A DELEGATING STUB.**
`loop/driver.py` ends with `SeasonDriver.census = census`, so `SeasonDriver.census` IS this
function and `inspect.getsource(SeasonDriver.census)` returns THIS SOURCE. Eight tests read a
step's body that way -- three of them `witness`'s, one of those a pure NEGATIVE assertion --
and a stub would fail two and silently vacate the third, which is why step 9 of the
decomposition (ED-IN-0203) refused to delegate. Step 5 established the technique when
`class Query` bound module functions as staticmethods.

⚠ **THE TOKEN IS STILL A `WriteClass` PARAMETER AND THAT IS G2's, NOT THIS UNIT's.** `04 §A.3`
row 3 replaces the parameter with an unforgeable token type minted only by the driver; until
that lands, this step passes `WriteClass` exactly as it did inside the class. Unit L5
delivers the MODULE boundary `04 §A.2:134` requires; the write discipline is Arc 2.
"""

from __future__ import annotations

from ..data.matrix import Step
from ..trace_log import TRACE



# -- CENSUS -- shares WITNESS's join (S29) ------------------------------
def census(self) -> None:
    w = self.w
    w.step = Step.CENSUS
    TRACE.step("CENSUS", "enter")
    TRACE.decision("individuation", "S29",
                   chose="demand-driven only; generated nobody",
                   alternatives=["a clock that generates (forbidden)",
                                 "a world-gen roster (S54 item 18 -- not a clock, not folded in)"])
    # S29: DEMAND-DRIVEN ONLY. Nothing generates without a demand and NO CLOCK GENERATES
    # ANYTHING -- so this step writes nothing here. Rev 1 called the gate with an `apply`
    # that mutated nothing, which S30.2 calls "worse than no gate"; the call is gone rather
    # than made cosmetic.
    TRACE.step("CENSUS", "leave")
