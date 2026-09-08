"""`season.queries.readers` — the two readers the `requires` grammar asks its questions THROUGH.

EXTRACTED, step 5 of the decomposition (a PURE MOVE but for two call sites, named below). Step 3
moved the grammar to `season.data.requires` and left these two here deliberately, recording the
reason at the site: *"They are READERS, `queries/` territory at a later step, and the grammar they
serve asks only `reader.read(subject, predicate)`; moving a reader into the grammar module would
give the grammar an opinion about where its answers come from."* This is that later step.

THE TWO READERS ARE THE SAME QUESTION ASKED OF TWO SOURCES, and that symmetry is the design:
`WorldReader` asks the world (and the ACTOR'S OWN ledger, by construction — see its docstring),
`LedgerReader` asks one person's claims and nothing else. Both answer `UNKNOWN` to a question they
cannot resolve, which is the grammar's third truth value and not a failure.

⚠ TWO LINES ARE NOT A BYTE-IDENTICAL MOVE, and they are declared rather than buried:
`Query.parent_of` and `Query.presence` are now `world_q.parent_of`/`world_q.presence`. Same
functions, same objects — `shape.Query` binds them — but a reader may not reach a world query
through a class that also holds the person-side family.
"""

from __future__ import annotations

from ..data.requires import UNKNOWN
from ..data.rosters import TENURE_KINDS
from ..gaps import Unspecified
from ..state.world import World
from . import world_q


class WorldReader:
    """§F.24a's questions asked OF THE WORLD, with every read recorded as an `Observation`.

    ⚠ THE ACTOR'S OWN LEDGER AND NO OTHER, STRUCTURALLY. `04_CODE_ARCHITECTURE.md` §B.2's
    corrected row (`F8`): *"the carve-out is exact and it is not a widening: the fold may ask the
    ACTOR'S OWN ledger ... and no other. A Query taking a ledger and an asker who is not its
    holder still does not exist."* This reader is constructed with ONE actor id, so there is no
    argument by which a caller could name somebody else's claims -- the same move the
    `valoria-critic` agent definition makes against a read-only promise written in a prompt.

    ⚠ THE `if stem ==` CHAIN IS NOT THE ROUTER `G2` FORBIDS. It enumerates the GRAMMAR'S OWN
    predicates -- the strings `Observation` derives from the seven forms -- not verbs, entities or
    outcomes. A predicate it does not know is UNKNOWN, so an unanswerable question refuses."""

    def __init__(self, w, actor: str):
        self._w, self._actor = w, actor

    def _ancestry(self, start: str) -> list:
        seen, cur = [], start
        while cur is not None and cur not in seen:
            seen.append(cur)
            cur = world_q.parent_of(self._w, cur)
        return seen

    def read(self, subject, predicate: str):
        w = self._w
        stem, _, arg = str(predicate).partition(":")
        if stem == "exists":
            # An EDGE kind is a `tenure_kinds` member and an OBJECT class is one of `World`'s own
            # collections. Both are DATA -- neither is a list written here.
            if arg in TENURE_KINDS:
                return sum(1 for t in w.tenures
                           if t.kind == arg and t.object == subject and t.live)
            attr = arg.lower() + "s"
            if attr in World._STATE_COLLECTIONS:
                return 1 if subject in getattr(w, attr) else 0
            return UNKNOWN
        if stem == "stores":
            r = w.rungs.get(subject)
            return UNKNOWN if r is None else (r.stores or {}).get(arg, 0)
        if stem == "condition":
            s = w.sites.get(subject)
            return UNKNOWN if s is None else s.condition
        if stem == "floor":
            s = w.sites.get(subject)
            if s is None:
                return UNKNOWN
            floors = w.fixtures.get("band_floors").get(s.kind)
            if floors is None:
                # `_req_work`'s refusal, carried unchanged: `H-08` owns the per-kind floors and
                # §42.2.1 forbids picking a plausible number for a kind nobody registered.
                raise Unspecified(
                    f"no band floors for site kind {s.kind!r}", "S12.1",
                    needs="a per-kind floor table -- register row H-08",
                    law="§12.1 gates verbs on `condition` against per-kind FLOORS, and §42.2.1 "
                        "forbids picking a plausible number for a kind nobody registered")
            # ⚠ THE LOOSEST FLOOR, AND AN ADVERSARIAL PASS CALLED THIS AN UNDER-REFUSAL.
            # The objection was exact and is answered rather than dismissed. It said: the prose is
            # `condition >= floor(verb)`, `band_floors`' inner keys are SITE-USE verbs
            # (bulk_shipping, fishing, deep_mining …) which its roster note says are "NOT
            # verb-table rows", so `work` is not among them and `min` silently substitutes the
            # loosest floor for the one the prose names — admitting, on a harbour, every condition
            # in 100..800 where `floor(bulk_shipping)` is 800.
            #
            # WHAT THE OBJECTION GETS RIGHT: this is not `floor(verb)`, and the site-USE is an
            # operand neither the act nor `requires_operands` carries (`H-94`).
            # WHAT IT GETS WRONG, AND WHY `min` STAYS: `work` is the GENERIC labour verb, so the
            # question its precondition asks is *can this site be worked at all* — and a site is
            # workable if it clears the floor of its LEAST demanding use. A seam at condition 100
            # cannot be deep-mined and CAN be surface-gleaned (`surface_gleaning: 50`); a harbour
            # at 150 cannot take bulk shipping and can be fished. So `min` is the READING of
            # `floor(verb)` for a verb that names no use, not a substitute for it.
            #
            # BOTH ALTERNATIVES WERE BUILT AND MEASURED BEFORE SETTLING HERE, which is why this
            # comment is long: `max` refuses a seam at 100 that surface-gleaning supports, and
            # turned `test_w8_...` red for exactly that site; `UNKNOWN` destroys the gate outright
            # — `work`'s precondition could then never return False, so §12.1's condition gate
            # could not observe the failure it exists to exclude (§0.1 point 2), and it turned
            # `test_w3_...` red. `min` is the only one of the three that both refuses an unworkable
            # site and admits a workable one.
            #
            # WHAT REMAINS OPEN AND IS NOT PAPERED OVER: a `work` that MEANS deep-mining is
            # admitted on a seam only surface-gleaning could support, because nothing on the act
            # says which use is intended. That is `H-94`'s operand, and when it exists this line
            # reads `floors[use]` and the reading collapses to the prose.
            return min(floors.values())
        if stem == "contain.path":
            if subject not in w.rungs or arg not in w.rungs:
                return UNKNOWN
            if subject == arg:
                return False           # a node is not a path to itself
            return bool(set(self._ancestry(subject)) & set(self._ancestry(arg)))
        if stem == "held_by":
            return any(t.kind == "hold" and t.subject == arg and t.object == subject and t.live
                       for t in w.tenures)
        if stem == "present_at":
            s = w.sites.get(subject)
            place = s.rung if s is not None else (subject if subject in w.rungs else None)
            return UNKNOWN if place is None else (arg in world_q.presence(w, place))
        if stem == "claim.held":
            p = w.persons.get(self._actor)
            return UNKNOWN if p is None else any(c.subject == subject for c in p.ledger)
        return UNKNOWN
# `REQUIRES_STEMS` and `LEDGER_DERIVED_STEMS` -- the stems `WorldReader.read`/`LedgerReader.read`
# dispatch on, above and below -- now live in `season.data.requires` (step 3), imported back at
# the top of this file. See that module for the two roster-exempt notes that used to stand here.

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

    def read(self, subject, predicate: str):
        best = None
        for c in self._claims:
            if c.subject == subject and c.predicate == predicate:
                if best is None or (c.when, c.confidence) > (best.when, best.confidence):
                    best = c
        return UNKNOWN if best is None else best.value
