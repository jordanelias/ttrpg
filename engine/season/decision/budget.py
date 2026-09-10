"""`decision/` -- the `budget` member of `04_CODE_ARCHITECTURE.md` §A.2:133.

`budget`, and the body-band penalty it applies. §A.2's table lists `budget` in `decision/`'s
members row (`04:133`) AND in its "may read" column, an ambiguity `04` carries and this unit does
not resolve; L3 records it rather than picking silently.

AX-2 binds every file under `decision/`: no `World`, as an import, a name, an attribute or a
string. Enforced BY PATH over this directory (`04:1046`).
"""

from __future__ import annotations

from ..state.carriers import Person, View
from ..trace_log import TRACE


def budget(p: Person, v: View, k: int, fx: "Fixtures") -> int:
    """S26 / `H-28`: `budget : (Person, View) -> int`, PERSON-SIDE, NO WORLD. Returns SCENE
    ACTIONS, per Jordan's 2026-09-02 ruling.

    ⚠ REV 4 IS THE FIRST VERSION THAT READS ITS OWN ARGUMENTS. Rev 3's docstring disclosed,
    honestly, that it "RETURNS THE INJECTED FIXTURE AND IGNORES `p` AND `v`" -- functionally
    the FIELD S26.3 forbids. The reason it gave was a collision it called unresolved: S26
    types it with no `World`, S26.3 says it varies by office, condition and distance, and all
    three looked resolver-side.

    **They were never resolver-side; the STORE was in the wrong place.** #353 `:730` gives
    Person "every Tenure whose subject they are", so office-holding is the person's own state;
    `(Person, body)` and `(Person, travel_leg)` are Part D rows on Person. W5 moved the tenure
    store onto its subject (see `_TenureView`) and added the two fields, and the collision
    dissolved with no signature change. That is PLAN §3.3's SMALLER AMENDMENT, and taking it
    is what lets `:634`'s "the ONE non-decision function permitted a `World`" stay true --
    V2 §F3 took the larger one and made `budget` a second such function.

        budget = base + office_bonus x (own live `hold` Tenures)
                      - condition_penalty(own body band)
                      - distance_penalty(own travel legs)

    `condition_penalty` COUNTS BANDS on the `band_floors["body"]` table the site gate already
    uses -- `H-38` closed with "`Site.condition` is the model", so this spends that closure
    rather than inventing a second band scheme. Floor of 1: a wounded duke gets fewer scenes,
    and a dying one still gets one, because a budget of 0 would delete the person from the
    season silently rather than narrowing them (S26.3's triage is the point).

    `k` remains the injected base so the sweep site is unchanged. The two modifier magnitudes
    are fixtures (`H-70`); the DIRECTIONS are #353 `:912-913` and are not open.

    ⚠ `fx` IS NOT A WORLD, and the distinction is the one L2 actually draws. A `World` is other
    people's state -- persons, rungs, sites, the tenure store -- and reading it person-side is
    what L2 forbids. `Fixtures` is the PARAMS REGISTRY: flat numbers, no entity, identical for
    every person in the season, and #353 §22 assigns them to `params` precisely so they are
    not world state. `k` was already one of them, handed in by the driver; `fx` generalises
    that rather than widening it. The AST proof below tests for a `World` ANNOTATION, so it
    would catch a real regression here and correctly passes this."""
    TRACE.query("budget", "person")
    offices = sum(1 for t in p.tenures if t.kind == "hold" and t.live)
    b = k + offices * fx.get("budget_office_bonus")
    b -= body_band_penalty(p, fx)
    b -= len(p.travel_leg) * fx.get("budget_leg_penalty")
    return max(1, b)


def body_band_penalty(p: Person, fx: "Fixtures") -> int:
    """How many bands `p`'s body has fallen below the top, on `band_floors["body"]`.

    PERSON-SIDE: it reads `p.body` and a params table, never a World. `H-38` closed with *"the
    answer is YES -- `Site.condition` is the model"*, and this is that closure SPENT: the same
    floors table, the same "a band is a floor you are at or above" reading, one kind lower. A
    second band scheme would have been the invention `H-38` was closed to avoid.

    Returns 0 at full operations and rises by one per band crossed, so the order is FIXED and
    the narrowing is monotone -- which is the property `P32` names."""
    floors = fx.get("band_floors")["body"]
    # Descending, so "the top band" is unambiguous and the count is the number of floors passed.
    return sum(1 for f in sorted(floors.values(), reverse=True) if p.body < f)
