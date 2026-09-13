"""`queries/person_q.py` -- the ASKER-FIRST Query family, `04_CODE_ARCHITECTURE.md` §A.1's AX-2
row and §A.2's table.

> `queries/`  ownerless functions: world_q (World first) · **person_q (asker first)** · cache
>
> `queries/person_q` | owns **nothing** | may read **a `PersonInterior` snapshot only** | -- | --

⚠ **ONE MEMBER, AND THE SMALLNESS IS A MEASUREMENT RATHER THAN A STUB.** Unit L3 adjudicated every
candidate against `04` per symbol instead of executing `ED-IN-0206` item (2) literally, which would
have been wrong. That row reads *"§A.1's AX-2 row assigns the person-side family to
`queries/person_q`; step 7 put budget/opening_set/assemble/entrenchment in `decision.py` instead."*
Measured:

- **`budget` and `opening_set` are named BY `04:133` as `decision/`'s OWN members** -- *"`decision/`
  AX-2's island: questions · opening_set · choose · budget"*. Moving them here would BREAK
  conformance, not restore it. ED-IN-0206 item (2) is wrong about them and says so now.
- **`assemble` is the `questions` member**, same line.
- **`entrenchment` is the only one of the four `04` does not name**, and it is person-first in
  signature and self-declares as a person Query at its own first statement --
  `TRACE.query("entrenchment", "person")`. It reads a `Person` and three ints and touches nothing
  else, which is exactly the *"`PersonInterior` snapshot only"* the table allows. So it is here.
- **Every function in `world_q.py` takes `w: World` first** -- all thirteen, checked by `ast`. There
  is no misfiled person-first Query hiding in the world-side module.

⚠ **§A.3 ROW 2's PROPERTY IS THE POINT, NOT THE FILE COUNT.** *"one `Query` class holding both
families"* becomes *"two modules; the second cannot import the first"*, forced by T-f: *"in one
class, a person-side function calls a resolver-side one with no import to scan."* Splitting by
module makes that checkable, and **nothing checked it until this unit** --
`test_person_q_cannot_reach_the_world_side` is the scan.

`decision/` MAY import this module (`04 §C.3`: *"`decision/` imports `person_q` and `data/`"*), and
today does not: `entrenchment` had no caller inside `decision/`. The AX-2 by-path scan therefore
still forbids `queries` wholesale from `decision/`, which is narrower than §C.3 allows and is left
that way deliberately -- a guard is widened when a unit needs it, not in advance.
"""

from __future__ import annotations

from ..data.requires import UNKNOWN
from ..state.carriers import Person
from ..trace_log import TRACE


def entrenchment(p: Person, seasons_held: int, scale: int, span: int) -> int:
    TRACE.query("entrenchment", "person")
    return min(scale, (seasons_held * scale) // span)


# ---------------------------------------------------------------------------
# `LedgerReader` -- MOVED HERE FROM `queries/readers.py` AT UNIT L3 (ED-IN-0206). It asks ONE
# PERSON'S OWN CLAIMS and nothing else: it takes neither a `World` nor even a `Person`, only the
# claims themselves, which is the asker-first family exactly and the `§A.2` table's *"may read a
# `PersonInterior` snapshot only"* row it now sits under.
#
# ⚠ THE TWO READERS ARE STILL THE SAME QUESTION ASKED OF TWO SOURCES, and splitting them by source
# is what makes that symmetry checkable instead of merely stated -- `test_person_q_cannot_reach_the
# _world_side` can now assert that this side cannot reach the other. The pointer note that stood
# between them in `readers.py` travels here because it is about what BOTH `.read` methods dispatch
# on, and this is the module a reader of the person-side half meets first:
# `REQUIRES_STEMS` and `LEDGER_DERIVED_STEMS` -- the stems `WorldReader.read`/`LedgerReader.read`
# dispatch on, above and below -- now live in `season.data.requires` (step 3), imported back at
# the top of this file. See that module for the two roster-exempt notes that used to stand here.
# ---------------------------------------------------------------------------


class LedgerReader:
    """THE SAME QUESTIONS ASKED OF ONE PERSON'S OWN CLAIMS, AND OF NOTHING ELSE.

    ⚠ IT TAKES CLAIMS, NOT A WORLD, AND NOT A PERSON. `#353 :634` permits `sense()` exactly one
    World among the non-decision functions, and §F1 clause 4 runs person-side; handing this a
    World would make `belief_contradicts` read the world, which is the filter §F1 spends two
    paragraphs forbidding (*"a filter on world truth would be `choose` reading the world"*).

    THE MOST RECENT, THEN THE MOST CONFIDENT. A ledger may hold two claims about one
    `(subject, predicate)` -- that is what a ledger IS -- and answering with the first found would
    make the verdict depend on append order. No matching claim is UNKNOWN, never False: §F1's
    asymmetry is that absence of a belief is not a belief in the negative."""

    def __init__(self, claims):
        self._claims = list(claims or [])

    def _best(self, match):
        """THE COMPARATOR, ONCE. *Most recent, then most confident*, over whatever `match` admits.

        ⚠ IT EXISTS BECAUSE THE DOCSTRING BELOW CLAIMED IT ALREADY DID. `latest_about` was added
        asserting it *"reuses `read`'s comparator rather than restating it"* while carrying its own
        copy of the identical loop -- a single-owner claim made in the act of breaking it, which is
        the anti-pattern `ci_common.load_yaml`'s own docstring records against itself
        (*"a single-owner comment asserting a property the tree lacks is worse than no comment"*).
        Extracting it makes the sentence true."""
        best = None
        for c in self._claims:
            if match(c) and (best is None
                             or (c.when, c.confidence) > (best.when, best.confidence)):
                best = c
        return best

    def read(self, subject, predicate: str):
        best = self._best(lambda c: c.subject == subject and c.predicate == predicate)
        return UNKNOWN if best is None else best.value

    def latest_about(self, subject):
        """THE ONE CLAIM THIS PERSON WOULD OFFER ABOUT `subject`, or `None` for no claim.

        ⚠ IT RETURNS THE CLAIM, NOT THE VALUE, AND THAT IS THE ONLY DIFFERENCE FROM `read`.
        A teller transmits a `(subject, predicate, value)` triple; `read` answers a value for a
        predicate the caller already knows, and a telling does not know one -- `tell`'s `requires`
        cell is *the teller holds a claim on the subject*, with no predicate in it.

        ⚠ AND IT REUSES `read`'s COMPARATOR RATHER THAN RESTATING IT -- through `_best`, which
        both methods now call. `CLAUDE.md` §8: the rule lives once. MOST RECENT, THEN MOST
        CONFIDENT is this class's answer to *a ledger may hold two claims about one thing*, and a
        second copy of that key anywhere would be a second owner of which belief a person holds --
        free to drift, and drifting silently, because both orderings agree until the day two
        claims tie on `when`."""
        return self._best(lambda c: c.subject == subject)
