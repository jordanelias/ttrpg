"""`loop/census.py` -- CENSUS -- shares WITNESS's join. `04 §A.2`: owns `(Person, exists)` on individuation, `weight`, `envelope`; emits `person.individuated`; token MATTER.

⚠ **THE BODY IS THE DRIVER'S OWN, BOUND BACK ONTO THE CLASS -- NOT A DELEGATING STUB.**
`loop/driver.py` ends with `SeasonDriver.census = census`, so `SeasonDriver.census` IS this
function and `inspect.getsource(SeasonDriver.census)` returns THIS SOURCE. Eight tests read a
step's body that way -- three of them `witness`'s, one of those a pure NEGATIVE assertion --
and a stub would fail two and silently vacate the third, which is why step 9 of the
decomposition (ED-IN-0203) refused to delegate. Step 5 established the technique when
`class Query` bound module functions as staticmethods.

⚠ **THE TOKEN IS HANDED IN BY THE DRIVER (G2), AND SINCE v9 SE-01 THIS BODY SPENDS IT.** `04 §C.1`
gives CENSUS a MATTER token -- `mat2 = Token(MATTER,t); census(w,mat2); drop` -- and the write
matrix licenses `(Person, exists)` at CENSUS. Until SE-01 (`24g`) the body wrote nothing (S29:
demand-driven, and no demand was wired). `H-51` -- *what DEMANDS an individuation* -- is answered
here as P3 (`proposals/2026-09-10-settlements-factions-populations/02_PROPOSALS_SUBSTRATE.md`, *"P3 ·
INDIVIDUATION IS A REFUSAL"*): a `dispatch` naming an id the world does not hold refuses with
`person.demanded` (`loop/resolve.py::_demand_earned`), and this step individuates that id.
"""

from __future__ import annotations

from ..data.matrix import Step
from ..queries import world_q
from ..state.attribution import anchor_of, causing_act
from ..state.carriers import Person, Rung, Tenure
from ..state.gate import Token
from ..trace_log import TRACE
# The refusal kind a demand rides on: declared on `dispatch`'s row (`verb_table.yaml`), earned at
# the fold, and spelled once there.
from .resolve import PERSON_DEMANDED


# -- CENSUS -- shares WITNESS's join (S29) ------------------------------
def census(self, token: Token) -> None:
    w = self.w
    w.step = Step.CENSUS
    TRACE.step("CENSUS", "enter")
    # S29: DEMAND-DRIVEN ONLY. Nothing generates without a demand and NO CLOCK GENERATES
    # ANYTHING. Rev 1 called the gate with an `apply` that mutated nothing, which S30.2 calls
    # "worse than no gate"; every write below individuates a person a demand named, or is not made.
    #
    # ⚠ THIS SEASON'S DEMANDS ONLY (`emitted_at == w.tick`), READ ONCE, IN LOG ORDER. A demand
    # already answered is not re-read next season, and a second demand for the same id in one
    # season finds it held (`demanded_person` returns `None`) and individuates nobody twice.
    demands = [e for e in w.log if e.kind == PERSON_DEMANDED and e.emitted_at == w.tick]
    # ⚠ A SEASON WITH NO DEMAND TRACES EXACTLY WHAT IT TRACED BEFORE SE-01, AND THE LINE IS STILL
    # TRUE OF IT. The committed run artifacts (`runs/DECISIONS.md`, `runs/TRACE.txt`, reproduced
    # byte for byte by `test_w15_report_py_...`) carry this decision every season, and no run they
    # record demands anyone; a season that does says so instead.
    TRACE.decision("individuation", "S29",
                   chose=("demand-driven only; generated nobody" if not demands else
                          f"demand-driven only; {len(demands)} `person.demanded` Event(s) this "
                          "season, each individuating the id it names if the world still lacks it"),
                   alternatives=["a clock that generates (forbidden)",
                                 "a world-gen roster (S54 item 18 -- not a clock, not folded in)"])
    for e in demands:
        a = causing_act(w, e)
        pid = world_q.demanded_person(w, a) if a is not None else None
        if pid is None:
            continue
        # WHERE THE DEMAND WAS MADE -- `place_of(w, anchor_of(w, e))`, the one expression the tree
        # uses for *where an Event happened* (`epistemic._ch_co_located`). A refusal's anchor is
        # its actor, so the person is individuated where the order was given.
        at = world_q.place_of(w, anchor_of(w, e))
        if at is None:
            TRACE.note(f"{e.id} demanded {pid!r} at no place; individuated nobody "
                       "(F.30: a Person with no `contain` edge is nowhere)")
            continue
        # F.30: *"an individuated Person needs a new person-rung and `contain` edge in the same
        # CENSUS write, or the new Person is nowhere"* -- what every builder mints for a person
        # (`harness/populated.py::seat_cohorts`), at weight 1, and nothing else. The `contain` edge
        # is admitted by the gate's `founding` basis (its subject is born in this same write).
        # ⚠ NO ENVELOPE IS DRAWN: P3 mints *out of the envelope*, and P2's grown band is not built,
        # so this individuates from no residual (`H-51`'s row says so).
        w.write("exists", token,
                lambda pid=pid, at=at: _individuate(w, pid, at),
                record_kind="Person", fieldname="exists", driver="Event",
                emits="person.individuated", subject=pid, causes=[e.id])
    TRACE.step("CENSUS", "leave")


def _individuate(w, pid: str, at: str) -> None:
    w.persons[pid] = Person(pid, pid)
    w.rungs[pid] = Rung(pid, "person")
    w.add_tenure(Tenure(f"t_{pid}_in", pid, at, "contain", w.tick))
