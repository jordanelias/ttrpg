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


def violated_pursuits(p: Person, verb: str) -> tuple:
    """WHICH OF `p`'s OWN PURSUITS AN ACT OF `verb` VIOLATES -- the per-element half of the scar
    (IN-08 H3, `ED-IN-0261`'s scar model: a COUNT per element, accrued by WITNESSING).

    A pursuit `e` that `p` holds (weight > 0) is violated when `Σ_axis projection[e][axis] ·
    alignment(verb, axis) < 0` -- the verb leans against where the pursuit points. ⚠ THAT SIGN TEST
    IS A CANDIDATE READING RECORDED FOR REVIEW, NOT A RULING (`workplans/valoria_master_workplan_v9_part5.md`,
    IN-08 H3): no source states the violation predicate; this is the plainest one the two owned
    tables admit. It composes on the two owners and copies neither: `data/pursuits.py::to_axes`
    (pursuit -> axes, one owner) and `data/verbs.py::align` (the one binding the alignment sweep
    rebinds). A verb with no celled axis violates nothing, by construction. Person-side, no World
    (AX-2). Sorted, so a caller writing counts in this order writes a canonical dict."""
    from ..data.pursuits import to_axes
    from ..data.rosters import PURSUIT_AXES
    from ..data.verbs import align
    lean = {ax: align(verb, ax) for ax in PURSUIT_AXES}
    if not any(lean.values()):
        return ()
    out = []
    for e in sorted(p.pursuits or {}):
        if not float(p.pursuits[e]) > 0:
            continue
        proj = to_axes({e: 1.0})
        if sum(proj[ax] * lean[ax] for ax in PURSUIT_AXES) < 0:
            out.append(e)
    return tuple(out)


def violated_affiliations(p: Person, verb: str) -> tuple:
    """WHICH OF `p`'s OWN RELIGIOUS AFFILIATIONS AN ACT OF `verb` VIOLATES -- IN-08 H11, H3's
    mechanism over the affiliation table (J-5's C4).

    An affiliation `a` that `p` holds (intensity > 0) is violated when `data/affiliations.py::
    engagement(verb, a) < 0`: the verb's cell for that affiliation, which is the shared column's
    cell when the affiliation has none of its own (R-C4.1: the vow-shaped verbs engage every creed
    alike). A sign test, as `violated_pursuits` is; the intensity does not enter it, because the
    scar is a COUNT per element and an act is witnessed or not. It is `violated_pursuits`'
    sibling and not a second scar path: `loop/resolve.py::_scar_witnesses` asks both and writes
    once. Person-side, no World (AX-2). Sorted, as `violated_pursuits` is."""
    from ..data.affiliations import engagement
    held = p.conviction or {}
    return tuple(a for a in sorted(held) if int(held[a]) > 0 and engagement(verb, a) < 0)


def confliction(p: Person) -> int:
    """HOW FAR `p`'s RELIGIOUS AFFILIATIONS STRAIN AGAINST EACH OTHER -- IN-08 H10, `12b`'s derived
    Query (ED-IN-0251 R1: *confliction is DERIVED from an `incompatible` relation and never stored*).

    `Σ over the incompatible pairs {a, b} of min(conviction[a], conviction[b])`: a pair strains as
    far as the WEAKER of its two holdings, so it is 0 unless both are held, and a person holding
    both at full intensity is in confliction at the ceiling. [ASSUMPTION; Jordan to correct] No source
    states the magnitude -- the draft gives only *"holding BOTH at high intensity"*; `min` is chosen
    because it stays an int on the intensity's own 0-5 spine (the alternative the draft names, a
    product of the two, leaves the scale). Composes on `data/affiliations.py::INCOMPATIBLE`, the one
    loaded relation. Person-side, no World (AX-2).

    Its caller is IN-08 6f: `decision/choose.py`'s `make_chooser` damps the pursuit dot by it, at
    the swept `confliction_weight` arm (H-188; control 0, shipped)."""
    from ..data.affiliations import INCOMPATIBLE
    held = p.conviction or {}
    return sum(min(int(held.get(a, 0)), int(held.get(b, 0)))
               for a, b in (tuple(pair) for pair in INCOMPATIBLE))


# `ED-IN-0261`'s scar thresholds are 1 (destabilise), 2 (weight shifts, the others gain
# proportionally) and 3+ (crisis, terminal). IN-08 H9 reads THRESHOLD 2 ONLY: threshold 1 has no
# mechanism anywhere, and 3 is H13's (G-Q6, `conviction_after_crisis` below). Each count is the
# ruled threshold, not a swept value.
SCAR_WEIGHT_SHIFT_AT = 2
SCAR_CRISIS_AT = 3  # [JUSTIFIED: the ruled threshold, not a swept value -- `ED-IN-0261` rules 3+ as the terminal crisis; the draft's G-Q6 gives the mechanism]


def crisis_weights(p: Person, shift: float = 0.0) -> dict:
    """`p`'s pursuit weights as the chooser should read them once scars have reached threshold 2
    (IN-08 H9, `ED-IN-0261`: *"WEIGHT SHIFTS, others gain proportionally"*) -- A READER, it writes
    nothing and `Person.pursuits` is untouched.

    A held pursuit `e` with `p.scar[e] >= SCAR_WEIGHT_SHIFT_AT` gives up the fraction `shift` of
    its weight (downward: `conviction_track_v1.md` §2, reference for intent), and the mass given up
    is shared among the held pursuits that have NOT reached the threshold in proportion to their
    own weights, so a person's total weight is conserved. Where every held pursuit is at the
    threshold there is nobody to gain and the weights are returned unshifted rather than lose mass.
    `shift` is `Fixtures.scar_weight_shift`; `0` -- the shipped control -- returns `p.pursuits`
    itself, so the arm at its control is the unmodified read by construction.

    Person-side, no World (AX-2). Keys keep `p.pursuits`' own order, which `to_axes` sums in."""
    base = p.pursuits or {}
    if not shift or not p.scar:
        return base
    held = {e: float(w) for e, w in base.items() if float(w) > 0}
    crisis = {e for e in held if int(p.scar.get(e, 0)) >= SCAR_WEIGHT_SHIFT_AT}
    heirs = {e: w for e, w in held.items() if e not in crisis}
    if not crisis or not heirs:
        return base
    given = sum(held[e] * shift for e in crisis)
    pool = sum(heirs.values())
    out = dict(base)
    for e in crisis:
        out[e] = held[e] * (1.0 - shift)
    for e, w in heirs.items():
        out[e] = w + given * w / pool
    return out


def conviction_after_crisis(p: Person) -> dict:
    """`p.conviction` as the crisis at scar threshold 3 leaves it -- IN-08 `12e` H13, G-Q6 as the
    affiliation draft recommends (folded into the build by Jordan's 2026-10-06 ruling, `ED-IN-0261`'s
    superseding row): THE ENGINE CHOOSES PER CASE, BY A RULE OVER STATE THE CRISIS ALREADY READS, AND
    ROLLS NOTHING (the crisis rewrites the vector, never an outcome). A READER: it returns a new
    vector and writes nothing; the write is `loop/resolve.py::_conviction_crisis`'s, by an act.

    A held affiliation is IN CRISIS when `p.scar` for it is `>= SCAR_CRISIS_AT`. ONE CRISIS AT A
    TIME: where several are, the one taken is the highest-held, ties to the first by name -- the
    design's own multi-crisis rule (`conviction_track_v1.md` §2 `:62`, quarantined, reference for
    intent: *"the most recent Scar event ... ties resolve to highest-weighted primary"*) with its
    first key dropped, because a count carries no time and one act scars every holding it violates
    at once [ASSUMPTION; Jordan to correct]. For that one, `x`, the first branch that applies:
      * FOLD -- `x` is co-held with an affiliation `y` it is `incompatible` with
        (`data/affiliations.py::INCOMPATIBLE`, the one loaded relation): `x`'s intensity transfers
        to `y` and `x` drops. With several such `y`, the highest-held takes it, ties to the first
        by name (the draft's *"highest-weighted other element"*; the name order is only the tie
        rule). The sum is clamped to the intensity's ceiling [ASSUMPTION: the spine is closed,
        `conviction_map` refuses past it].
      * RESTABILISE -- `x` is co-held with nothing it is incompatible with, and something else is
        held: the draft's branch is "the threshold-2 mechanism continuing". NOT BUILT -- the vector
        is left as it is. The threshold-2 mechanism is a reader over PURSUIT weights (H9's
        `crisis_weights`, a float fraction); `conviction` is an int on the 0-5 spine, so moving it
        by that fraction needs a rounding rule nobody has chosen.
      * DESTROYED -- nothing else is held: `x` drops, leaving the zero vector (no affiliation
        held, a real state).
    "Held" is a present key: `conviction_map` drops a zero, so every key is held at 1 or more
    [ASSUMPTION: the draft's "held above threshold" is read as held at all].

    ⚠ UNDER THE SHARED COLUMN THE FOLD'S DIRECTION IS INTENSITY'S, NOT CONTENT'S. The draft gives
    the direction as *"which affiliation was scarred"*, but `affiliation_engagement`'s shared column
    (R-C4.1) violates every held creed alike, so co-held creeds accrue equal counts and reach the
    threshold in the same act; the selector above then folds the HIGHER-held creed into the lower.
    Only a per-affiliation cell (R-C4.2) scars one creed alone, and of those only `thread_read`'s
    exists, which writes nothing at RESOLVE. The heir keeps its own count, already at the
    threshold, so its next violation breaks it.

    Re-evaluated at every count at or over the threshold, not only the one that reaches it: a
    folded or destroyed affiliation is no longer held, so it is never violated (hence never
    counted) again, and a restabilised one is left unwritten. CONVICTION TRACK ONLY: the pursuit
    track has no `incompatible` relation to fold along and `Person.pursuits` has no writer (H-62;
    its first is SC-02 `22b`). Person-side, no World (AX-2). With no held affiliation in crisis it
    returns `p.conviction` unchanged."""
    from ..data.affiliations import AFFILIATION_CEILING, INCOMPATIBLE, conviction_map
    held = dict(p.conviction or {})
    scar = p.scar or {}
    crisis = [x for x in sorted(held) if int(scar.get(x, 0)) >= SCAR_CRISIS_AT]
    if not crisis:
        return p.conviction

    def first_highest(names: list) -> str:
        return max(names, key=lambda k: (int(held[k]), -names.index(k)))

    x = first_highest(crisis)
    heirs = [y for y in sorted(held) if y != x and frozenset((x, y)) in INCOMPATIBLE]
    if heirs:
        y = first_highest(heirs)
        held[y] = min(AFFILIATION_CEILING, int(held[y]) + int(held[x]))
        del held[x]
    elif len(held) == 1:
        del held[x]
    else:                            # RESTABILISE -- not built (above)
        return p.conviction
    return conviction_map(held, where=f"{p.id}: conviction after crisis")


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
