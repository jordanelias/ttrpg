"""`loop/census.py` -- CENSUS -- shares WITNESS's join. `04 §A.2`: owns `(Person, exists)` on individuation, `weight`, `envelope`; emits `person.individuated`; token MATTER.

⚠ **THE BODY IS THE DRIVER'S OWN, BOUND BACK ONTO THE CLASS -- NOT A DELEGATING STUB.**
`loop/driver.py` ends with `SeasonDriver.census = census`, so `SeasonDriver.census` IS this
function and `inspect.getsource(SeasonDriver.census)` returns THIS SOURCE. Eight tests read a
step's body that way -- three of them `witness`'s, one of those a pure NEGATIVE assertion --
and a stub would fail two and silently vacate the third, which is why step 9 of the
decomposition (ED-IN-0203) refused to delegate. Step 5 established the technique when
`class Query` bound module functions as staticmethods.

⚠ **THE TOKEN IS HANDED IN BY THE DRIVER (G2), AND THIS BODY DOES NOT YET SPEND IT.** `04 §C.1`
gives CENSUS a MATTER token -- `mat2 = Token(MATTER,t); census(w,mat2); drop` -- and the write
matrix licenses writes at CENSUS, so `SeasonDriver.season` mints one and passes it. The body below
writes nothing (S29: demand-driven, and no demand is wired), so the parameter is held for the
licensed rows rather than read. Kept rather than dropped because `04 §C.1` is Layer 1 and names it,
and because the first individuation write then needs no signature change; if it is dropped instead,
a write added here without one is refused at the gate as `NoToken`, loudly.
"""

from __future__ import annotations

from ..data.matrix import Step
from ..state.gate import Token
from ..trace_log import TRACE



# -- CENSUS -- shares WITNESS's join (S29) ------------------------------
def census(self, token: Token) -> None:
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
