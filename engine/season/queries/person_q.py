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
does: `choose` and `options` read `stance_toward` and `said_of` from here. The AX-2 by-path scan
(`test_decision_package_never_names_world_anywhere_under_it`) is an allow-list: it forbids
`queries` from `decision/` and admits `queries.person_q` only; this module's own scan
(`test_person_q_cannot_reach_the_world_side`) still forbids `decision`, so the edge runs one way.
"""

from __future__ import annotations

from ..data.requires import KNOWN_PERSON_CLAIM, UNKNOWN, WORLD_ONLY_STEMS
from ..data.rosters import SEEN_PREDICATE
from ..state.carriers import Person, Said
from ..trace_log import TRACE


def entrenchment(p: Person, seasons_held: int, scale: int, span: int) -> int:
    TRACE.query("entrenchment", "person")
    return min(scale, (seasons_held * scale) // span)


def ambitions(p: Person, propositions) -> list:
    """WHAT THIS PERSON IS COMMITTED TO AS AN OUGHT: the Proposition ids on `p`'s own LIVE `commit`
    edges whose Proposition is mood OUGHT, in the order the edges were opened, each once. Plan
    position `17`; `R-06`'s *"a READ over it (no `ambitions(p)` query anywhere in the package)"*.
    A belief is a `commit` to an OUGHT, not a field (`04` PART D row 44), so this READS the edge
    and keeps nothing: it is computed when asked and never stored.

    ⚠ IT TAKES THE PERSON'S OWN TENURES AND A `propositions` MAPPING, NEVER A `World` -- the AX-2
    test (`test_w5_sense_is_still_the_only_world_taking_non_decision_function`) refuses any
    function whose first parameter is a `Person` and another is a `World`. THE MAPPING IS NOT A
    SECOND WAY IN: a `commit` edge's object is only an id, and the same edge kind also binds a
    person to a faction, a treaty and a WAR, so the edge cannot say whether it is an ambition;
    the Proposition's MOOD can, and a Proposition is an identity-bearing, immutable UTTERANCE
    (S14), not hidden world truth. This reads only the keys `p`'s own edges name and never
    enumerates the mapping, so a caller hands in `w.propositions` and the function sees one
    utterance per edge the person already holds. Two sentences of this, said plainly: nothing
    here names a `World`, a store handle or another person, which is what AX-2's guard checks;
    and the plan's one-parameter spelling `ambitions(p)` is NOT met, because the mood has to come
    from somewhere and a `Person` does not carry it. Whether `04`'s *"`PersonInterior` snapshot
    only"* is read strictly enough to forbid a second, read-only argument is not settled here.
    (`propositions` is the LIVE store, `w.propositions`, handed in whole: `04` §A.2's `person_q`
    row, `:164`, reads *a `PersonInterior` snapshot only*, and `:241` says that snapshot carries
    *no store handle* -- a Layer-1 observation for `layer-conformance`, not decided here.)

    ⚠ FACTION MEMBERSHIP IS NOT A HOLDS THAT THE MOOD FILTERS OUT, FOR SIX OF THE NINE FACTIONS.
    `populated.build_realm` mints each creed as an OUGHT Proposition (Jordan, 2026-09-13, *"Faction
    creed as an ought: sure"*, subject the faction's authored leader) and membership is a `commit`
    to it, so `ambitions` DOES return a member's `fac_*` creed (MEASURED, `build_realm(0)`, Batch C
    close: 35 of 83 persons' `ambitions` include one). Only the three factions with no leader or
    template in canon (`Guilds`, `Schoenland`, `faction x`) keep HOLDS and are filtered by mood.

    ⚠ ONE OWNER OF *"a live `commit` to an OUGHT"*. `world_q.questions_for`'s Q4 source reads
    this rather than restating it, so the ambition mechanism `R-06` names exists once. A
    proposition id that is not in `propositions` is NOT an ambition (absent is the refusal, not a
    default); an ended edge (`until` set) is not one either; two live edges to one Proposition
    are one ambition. No TRACE row is written: `TRACE.query` rows are folded into the committed
    `runs/TRACE.txt` per call, and Q4 calls this once per person per deliberation."""
    out: list = []
    for t in p.tenures:
        if t.kind != "commit" or not t.live or t.object in out:
            continue
        prop = propositions.get(t.object)
        if prop is not None and str(prop.mood).upper() == "OUGHT":
            out.append(t.object)
    return out


def stance_toward(p: Person, referent: str) -> float:
    """§F2's second term, from `p`'s OWN stance rows. #353 `:333`: `(referent, valence -5..+5,
    weight 0..5)`. Valence times weight, summed over the rows naming this referent -- weight is
    what `:333` supplies it for, and dropping it would make a 5-weight conviction and a 0-weight
    one count alike."""
    total = 0.0
    for row in p.stance:
        if len(row) >= 3 and row[0] == referent:
            total += float(row[1]) * float(row[2])
    return total


def regard(p: Person, referent: str) -> float:
    """HOW `p` REGARDS `referent`, computed when read and never written (telling workplan §1's
    spine). Today it is the STORED HALF ONLY -- `stance_toward`, the person's own stance rows.
    The judged-deeds and told-valence halves are the gated position `G1`, not built; nothing here
    stands in for them. A second name for one sum is deliberate: `decision/options.py::
    teller_weight` asks for REGARD, and when `G1` widens what regard is, the reader does not move."""
    return stance_toward(p, referent)


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
    asymmetry is that absence of a belief is not a belief in the negative.

    ⚠ `weigh` (telling workplan `T3a`, `ED-IN-0282`, `H-157`): HEARSAY IS GRADED WHEN READ, NEVER
    AT DEPOSIT. `weigh(c) -> [0, 1]` is how far this holder credits one claim; the caller builds it
    (`decision/options.py::teller_weight`) because this module may not import `decision/`. With
    a `weigh`, the comparator ranks a claim by `(support, when, confidence)`, where `support` is
    the noisy-OR over the DISTINCT ORIGINS asserting the same value (below). `None` is today's
    comparator, unchanged, and every caller but `epistemic.belief_contradicts` passes `None`.
    `confidence` is read RAW either way: weighing never rewrites a claim."""

    def __init__(self, claims, weigh=None):
        self._claims = list(claims or [])
        self._weigh = weigh

    def _support(self, matches) -> list:
        """`support(v) = 1 - PROD over distinct origins (1 - weigh(c))`, one entry per match, in
        match order. Grouped by `(predicate, value)` -- `read`'s matches share one predicate, so
        for `read` that is grouping by value. Under a `weigh`, `latest_about` therefore ranks
        ACROSS predicates by support, so a firsthand claim on any predicate outranks hearsay on
        another; no caller weighs `latest_about` today, and the position that weighs `said_of`
        (G3) decides it. An origin is `c.chain[0]` for a told claim and the holder for
        anything else; one origin counts once per value, at its highest
        weight, so a teller repeating himself adds nothing. Grouped by `==`, not by hash: a
        claim's `value` need not be hashable.

        ⚠ AT `weigh == 1` FOR EVERY CLAIM, EVERY GROUP'S SUPPORT IS EXACTLY `1.0` (`1 - 0.0`), so
        the key collapses to `(when, confidence)` -- today's order, by arithmetic rather than by a
        branch. `test_t3_weigh_none_and_weigh_one_order_a_ledger_as_today` checks it over
        randomised ledgers."""
        groups: list = []       # [key, {origin: weight}]
        idx: list = []
        for c in matches:
            key = (c.predicate, c.value)
            for i, g in enumerate(groups):
                if g[0] == key:
                    break
            else:
                groups.append([key, {}])
                i = len(groups) - 1
            origin = c.chain[0] if c.chain else c.holder
            wt = self._weigh(c)
            g = groups[i][1]
            g[origin] = max(g.get(origin, 0.0), wt)
            idx.append(i)
        support = []
        for _key, origins in groups:
            miss = 1.0
            for wt in origins.values():
                miss *= 1.0 - wt
            support.append(1.0 - miss)
        return [support[i] for i in idx]

    def _best(self, match):
        """THE COMPARATOR, ONCE. *Most recent, then most confident*, over whatever `match` admits
        -- and, under a `weigh`, *best supported* first (`_support`). Strict `>`, so the first
        found wins a tie, in both forms.

        ⚠ IT EXISTS BECAUSE THE DOCSTRING BELOW CLAIMED IT ALREADY DID. `latest_about` was added
        asserting it *"reuses `read`'s comparator rather than restating it"* while carrying its own
        copy of the identical loop -- a single-owner claim made in the act of breaking it, which is
        the anti-pattern `ci_common.load_yaml`'s own docstring records against itself
        (*"a single-owner comment asserting a property the tree lacks is worse than no comment"*).
        Extracting it makes the sentence true."""
        if self._weigh is None:
            best = None
            for c in self._claims:
                if match(c) and (best is None
                                 or (c.when, c.confidence) > (best.when, best.confidence)):
                    best = c
            return best
        matches = [c for c in self._claims if match(c)]
        best, best_key = None, None
        for c, s in zip(matches, self._support(matches)):
            key = (s, c.when, c.confidence)
            if best is None or key > best_key:
                best, best_key = c, key
        return best

    def read(self, subject, predicate: str):
        # `T4`: where another person is NOW is the world's to answer, never a ledger's
        # (`data/requires.py: WORLD_ONLY_STEMS`) -- UNKNOWN, so clause 4 never declines on it.
        if str(predicate).partition(":")[0] in WORLD_ONLY_STEMS:
            return UNKNOWN
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

    def belief_among(self):
        """THE ONE CLAIM THIS READER WOULD ANSWER FROM, over every claim it holds -- `_best`'s
        comparator with no subject or predicate filter. For a caller that has already narrowed the
        ledger to one cell (`decision/options._pair`) and wants `read`'s ordering without reaching
        into a private name."""
        return self._best(lambda _c: True)


def said_of(claims, subject, fx) -> "Said | None":
    """WHAT THIS PERSON WOULD SAY ABOUT `subject`, as the `Said` a telling carries -- or `None` for
    nothing to say. Asked of the TELLER'S OWN claims at CHOOSE (`decision/options.py::opening_set`),
    never at WITNESS: what a telling passes on is decided when it is chosen, and rides the Act.

    ⚠ A `seen` CLAIM IS PASSED ON ONLY WHEN IT IS ALL THE TELLER HOLDS ABOUT THE SUBJECT (`R8.1`,
    moved here from `loop/witness.py::_told_content` unchanged). The `seen` deposit lands in every
    co-located witness -- the teller included -- with an identical value, so without this the
    teller's NEWEST claim about a rung was almost always a `seen` the hearer already held, the
    exact-triple guard at the told deposit suppressed it, and the told channel carried nothing:
    MEASURED at the `R8.1` commit, `build_world(0)`, four seasons, 0 `told_by` claims. A rumour of
    a sighting still travels when a sighting is all the teller has.

    ⚠ THE COMPARATOR IS `LedgerReader`'s, BOTH TIMES. *Most recent, then most confident* lives once
    (`_best`); only the pool differs. `fx` is unread; the workplan's §3 shape names it and G3 (slant)
    is its first reader (`workplans/2026-10-01-telling-workplan.md`), and a signature that changes
    under every caller is the churn this avoids."""
    reader = LedgerReader(claims)
    c = (reader._best(lambda c: c.subject == subject and c.predicate != SEEN_PREDICATE)
         or reader.latest_about(subject))
    if c is None:
        return None
    return Said(c.subject, c.predicate, c.value, c.confidence, c.chain)


def known_persons(claims, actor, topic) -> tuple:
    """THE PERSONS THIS HOLDER KNOWS OF, from their OWN claims only -- sorted ids, never `actor`
    and never `topic` (telling workplan `T4`, `ED-IN-0282`). Three sources, and no other:

      * a truthy existence reading of a person -- `rosters.yaml: known_person_operands.claim.
        predicate`, deposited where a fold asked whether somebody exists;
      * who was SEEN doing something -- the `seen` claim's `seen_term` (`Seen.who`);
      * who TOLD them something -- a told claim's last teller, `chain[-1]`.

    A person is never known from the world: no presence read, no roster of acquaintances (`AX-2`).
    WHETHER the person is present to hear is the fold's question (`tell`'s `hearer` conjunct, the
    `with` stem), so a known person who has walked away is still named and the telling is refused
    -- and the person does NOT learn it from the refusal (`news.untold` is one kind for both
    conjuncts and the `with` read is never deposited, `witness.py`). `topic` is excluded because a telling
    names its topic on `subject` and its hearer on `to`, and the two are different people by
    construction; the actor because a person does not tell themselves (`opening_set`'s
    counterparty rule declines it too).

    ⚠ `exists:Person` DEPOSITS ARE RARE AND `Seen.who` CARRIES THE LOAD: measured at T0 (scratch
    `t0/m0_summary.md`, M0d), every realm hit came from `seen`. The told source is empty until a
    told claim lands, which T4 itself is what makes possible."""
    predicate = KNOWN_PERSON_CLAIM.get("predicate")
    term = KNOWN_PERSON_CLAIM.get("seen_term")
    out = set()
    for c in claims or ():
        if c.predicate == predicate and c.value:
            out.add(c.subject)
        elif c.predicate == SEEN_PREDICATE:
            who = getattr(c.value, term, None)
            if who:
                out.add(who)
        if c.chain:
            out.add(c.chain[-1])
    out.discard(actor)
    out.discard(topic)
    out.discard(None)
    return tuple(sorted(out))
