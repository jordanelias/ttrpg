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

from ..data import verbs as _verbs
from ..data import affiliations as _aff
from ..data.affiliations import AFFILIATION_CEILING, conviction_map, engagement
from ..data.pursuits import to_axes
from ..data.requires import (
    KNOWN_PERSON_CLAIM, REQUIRES_OPERANDS, REQUIRES_STEMS, UNKNOWN, WORLD_ONLY_STEMS,
)
from ..data.rosters import (
    AFFILIATIONS, PURSUIT_AXES, RECORD_CONTENT, SEEN_PREDICATE, roster, roster_map,
)
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


def deeds_judged(p: Person, referent: str, scar_shift: float = 0.0) -> tuple:
    """`(judged, told)`: WHAT `p` MAKES OF THE DEEDS THEY HOLD ABOUT `referent`, by `p`'s OWN
    pursuits (v9 IN-18 `G1`, telling workplan §3's `regard` row). A deed claim is an event-kind
    claim `(referent, <kind>, True)` -- WITNESS's first deposit, or a told copy of one -- with
    `<kind>` in `data/verbs.py::EMITTED_KINDS`. Each is scored as `choose`'s score term 1 scores a
    verb, one owner per factor: `Σ_axis to_axes(crisis_weights(p, scar_shift))[axis] ·
    align_kind(kind, axis)`, so a deed that leans the way `p`'s pursuits point reads positive and
    one that leans against them negative. `judged` sums the deed claims `p` holds FIRSTHAND
    (an empty `chain`, source `firsthand`); `told` sums every other deed claim -- the told valence. Neither weighs the teller
    (§3: *"`judged` has no relation factor, so regard never calls weigh"*), so `regard` cannot
    recurse through `teller_weight`.

    ⚠ A KIND SEVERAL ROWS EMIT HAS NO `KIND_VERB` AND READS 0 (`align_kind`): `person.died`,
    `body.changed`, `contest.undecided` among them. Those are exactly the kinds whose claim subject
    may be the PATIENT (WITNESS's `both` rule deposits one claim per changed subject), so a victim
    is not judged for dying. No `deed:` cell is authored (M0b ≥ 5 % at `declared`, IN-18 §6).
    [ASSUMPTION, H-192: a deed's claim subject is read as its doer; the sum is unnormalised.]
    Person-side, no World (AX-2)."""
    axis_w = None
    judged = told = 0.0
    for c in p.ledger:
        if c.subject != referent or not is_deed(c):
            continue
        if axis_w is None:
            axis_w = to_axes(crisis_weights(p, scar_shift))
        v = deed_valence(axis_w, c)
        # FIRSTHAND only is judged (`dissents`' and `record`'s precedent, `decision/options.py`):
        # a `told_by` claim whose chain is empty is still hearsay, and lands in `told`.
        if c.firsthand:
            judged += v
        else:
            told += v
    return judged, told


def is_deed(c) -> bool:
    """A DEED CLAIM: an event-kind claim `(x, <kind>, True)`, `<kind>` in `EMITTED_KINDS` -- what
    WITNESS's first deposit writes, or a told copy of it (a `Claim` or a `Said`). A kind some row
    emits on refusal (`REFUSAL_KINDS`) is no deed: it reports an act that did not happen."""
    return c.value is True and c.predicate in _verbs.DEED_KINDS


def deed_valence(axis_w: dict, c) -> float:
    """How a holder whose projected pursuits are `axis_w` judges one deed claim `c`:
    `Σ_axis axis_w[axis] · align_kind(c.predicate, axis)`; 0 for a claim that is no deed. The one
    scoring of a deed, read by `deeds_judged` (G1) and `said_of`'s slant (G3)."""
    if not is_deed(c):
        return 0.0
    return sum(axis_w[ax] * _verbs.align_kind(c.predicate, ax) for ax in PURSUIT_AXES)


def regard(p: Person, referent: str, fx=None) -> float:
    """HOW `p` REGARDS `referent`, computed when read and never written (telling workplan §1's
    spine):

        regard = stance_toward(p, x) + judged_gain · judged + told_valence_gain · told

    the stored half (`stance_toward`, the person's own stance rows) plus `deeds_judged`'s two
    halves (v9 IN-18 `G1`). With no `fx`, or with both gains 0 -- the CONTROL (both ship live at 0.5,
    `H-192`/`H-193`) -- it is the stored half exactly and reads no ledger. ⚠ `judged_gain` IS NOT
    `regard_gain`: the shape row spells `regard_gain · judged`, but `regard_gain` is `teller_weight`'s
    relation gain (`H-179`, shipped 0.5), and zeroing it for G1's control would move every told
    claim's weight -- two decisions on one fixture, `H-121`'s defect. A second name for one sum is
    deliberate: `decision/options.py::teller_weight` asks for REGARD, so when the gains move, the
    reader does not."""
    stored = stance_toward(p, referent)
    if fx is None:
        return stored
    jg = float(fx.get("judged_gain"))
    tg = float(fx.get("told_valence_gain"))
    if not (jg >= 0 and tg >= 0):
        raise ValueError(f"judged_gain {jg} / told_valence_gain {tg} must be >= 0 (H-192/H-193)")
    if not jg and not tg:
        return stored
    judged, told = deeds_judged(p, referent, fx.get("scar_weight_shift"))
    return stored + jg * judged + tg * told


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
    (AX-2). Sorted, so a caller writing counts in this order writes a canonical dict.

    NO PRODUCTION CALLER: `loop/resolve.py::_scar_witnesses` asks `elements_violated_by` once per act
    and `broken_by` per person, which compose the same `_pursuits_violated_by` below. This wrapper
    is the per-person reading kept for tests (`test_h11_affiliation_scar.py` asserts it equals
    the production scar; `test_h3_scar_by_observation.py` computes its own), so a change to the sign test is made in `_pursuits_violated_by`."""
    return _held(p.pursuits, _pursuits_violated_by(verb))


def violated_affiliations(p: Person, verb: str) -> tuple:
    """WHICH OF `p`'s OWN RELIGIOUS AFFILIATIONS AN ACT OF `verb` VIOLATES -- IN-08 H11, H3's
    mechanism over the affiliation table (J-5's C4).

    An affiliation `a` that `p` holds (intensity > 0) is violated when `data/affiliations.py::
    engagement(verb, a) < 0`: the verb's cell for that affiliation, which is the shared column's
    cell when the affiliation has none of its own (R-C4.1: the vow-shaped verbs engage every creed
    alike). A sign test, as `violated_pursuits` is; the intensity does not enter it, because the
    scar is a COUNT per element and an act is witnessed or not. It is `violated_pursuits`'
    sibling and not a second scar path: `loop/resolve.py::_scar_witnesses` asks for both through
    `elements_violated_by` + `broken_by` and writes once, so this wrapper has no production caller
    (it is a test oracle, as `violated_pursuits` is). Person-side, no World (AX-2). Sorted, as
    `violated_pursuits` is."""
    return _held(p.conviction, _affiliations_violated_by(verb))


def _pursuits_violated_by(verb: str) -> frozenset:
    """The pursuits an act of `verb` violates, whoever holds them: `violated_pursuits`' sign test,
    which reads only `(verb, element)`. The candidates are `data/verbs.py::PURSUIT_PROJECTION`'s
    keys, read through the module at call time so a rebound projection is what is asked; a pursuit
    the projection does not list projects to the zero vector and violates nothing."""
    lean = {ax: _verbs.align(verb, ax) for ax in PURSUIT_AXES}
    if not any(lean.values()):
        return frozenset()
    out = set()
    for e in _verbs.PURSUIT_PROJECTION:
        proj = to_axes({e: 1.0})
        if sum(proj[ax] * lean[ax] for ax in PURSUIT_AXES) < 0:
            out.add(e)
    return frozenset(out)


def _affiliations_violated_by(verb: str) -> frozenset:
    """The rostered affiliations an act of `verb` violates, whoever holds them:
    `violated_affiliations`' sign test, `engagement(verb, a) < 0`. The candidates are
    `rosters.AFFILIATIONS`, the roster `data/affiliations.py::conviction_map` holds every
    `Person.conviction` key to."""
    return frozenset(a for a in AFFILIATIONS if engagement(verb, a) < 0)


def elements_violated_by(verb: str) -> tuple:
    """`(pursuits, affiliations)` an act of `verb` violates, as two frozensets -- the person-free
    half of `violated_pursuits` and `violated_affiliations`. Whether an element is violated is a
    property of `(verb, element)` alone, so `loop/resolve.py::_scar_witnesses` asks this once per
    act and intersects each person's holdings with it (`broken_by`) instead of re-deriving the sign
    test per person. Reads `ALIGNMENT` and `PURSUIT_PROJECTION` at call time: never cache it
    across a sweep's rebind."""
    return _pursuits_violated_by(verb), _affiliations_violated_by(verb)


def _held(weights, violated: frozenset) -> tuple:
    """The elements of `weights` held above zero and in `violated`, sorted by name."""
    weights = weights or {}
    return tuple(e for e in sorted(weights) if float(weights[e]) > 0 and e in violated)


def broken_by(p: Person, violated: tuple) -> tuple:
    """The elements `p` holds that `violated` (an `elements_violated_by` answer) names: the held
    pursuits, then the held affiliations, each sorted -- `violated_pursuits(p, verb) +
    violated_affiliations(p, verb)` without re-asking the sign test."""
    pursuits, affiliations = violated
    return _held(p.pursuits, pursuits) + _held(p.conviction, affiliations)


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
    held = p.conviction or {}
    return sum(min(held.get(a, 0), held.get(b, 0)) for a, b in _aff.INCOMPATIBLE)


# `ED-IN-0261`'s scar thresholds are 1 (destabilise), 2 (weight shifts, the others gain
# proportionally) and 3+ (crisis, terminal). IN-08 H9 reads THRESHOLD 2 ONLY: threshold 1 has no
# mechanism anywhere, and 3 is H13's (G-Q6, `conviction_after_crisis` below). Each count is the
# ruled threshold, not a swept value.
SCAR_WEIGHT_SHIFT_AT = 2  # [JUSTIFIED: the ruled threshold, not a swept value -- `ED-IN-0261` rules 2 as the weight shift; the fraction shifted is the swept `scar_weight_shift`]
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
    # `shift` is a FRACTION of a weight: past 1 a crisis pursuit's weight goes negative and the
    # heirs gain more than was given up. `not 0 <= shift <= 1` also refuses a NaN (cf. the
    # `confliction_weight` check in `decision/choose.py::make_chooser`).
    if not 0 <= shift <= 1:
        raise ValueError(f"scar_weight_shift {shift} is not in [0, 1]: it is the fraction of a "
                         f"weight given up, and outside that range a weight goes negative (H-187)")
    base = p.pursuits or {}
    if not shift or not p.scar:
        return base
    held = {e: float(w) for e, w in base.items() if float(w) > 0}
    # A LIST IN `held`'s ORDER, not a set: `given` sums over it, and a set's order is
    # PYTHONHASHSEED's, so the float sum would not be reproducible across processes.
    crisis = [e for e in held if p.scar.get(e, 0) >= SCAR_WEIGHT_SHIFT_AT]
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


def conviction_after_crisis(p: Person, among: frozenset | None = None) -> dict:
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
    threshold, so the heir's next scar ON THAT AFFILIATION breaks it.

    `among` is the set of elements the calling act has just scarred `p` on: only an affiliation in
    it can be in crisis, because a crisis follows THAT affiliation's count moving -- a person held
    at the threshold on one creed and scarred on a pursuit alone is not in crisis.
    `loop/resolve.py::_conviction_crisis` passes it; `None` (a direct caller) considers every held
    affiliation at the threshold.

    Re-evaluated at every count at or over the threshold, not only the one that reaches it: a
    folded or destroyed affiliation is no longer held, so it is never violated (hence never
    counted) again, and a restabilised one is left unwritten. CONVICTION TRACK ONLY: the pursuit
    track has no `incompatible` relation to fold along and `Person.pursuits` has no writer (H-62;
    its first is SC-02 `22b`). Person-side, no World (AX-2). With no held affiliation in crisis it
    returns `p.conviction` unchanged."""
    if not p.conviction:
        return p.conviction
    held = dict(p.conviction)
    scar = p.scar or {}
    crisis = [x for x in sorted(held) if scar.get(x, 0) >= SCAR_CRISIS_AT
              and (among is None or x in among)]
    if not crisis:
        return p.conviction
    # `crisis` and `heirs` are in name order and `max` keeps the FIRST of equal keys, so a tie on
    # intensity goes to the lowest name.
    x = max(crisis, key=held.__getitem__)
    heirs = [y for y in sorted(held) if y != x and frozenset((x, y)) in _aff.INCOMPATIBLE]
    if heirs:
        y = max(heirs, key=held.__getitem__)
        held[y] = min(AFFILIATION_CEILING, held[y] + held[x])
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


SAID_SLANTS = roster("said_slants")


def _slant(fx) -> str:
    """`Fixtures.said_slant`, held to `rosters.yaml: said_slants` (`H-196`): an unknown arm raises
    rather than silently reading the control. `ValueError` for this module's reason
    (`_check_intent_claim`'s: the AX-2 allow-list)."""
    arm = fx.get("said_slant")
    if arm not in SAID_SLANTS:
        raise ValueError(f"said_slant {arm!r} is not in rosters.yaml: said_slants "
                         f"{sorted(SAID_SLANTS)} (H-196)")
    return arm


def said_of(claims, subject, fx, teller: "Person | None" = None) -> "Said | None":
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
    (`_best`); only the pool differs.

    ⚠ SLANT (v9 IN-18 `G3`, `H-196`): at `Fixtures.said_slant == "valence"`, with the `teller`
    given, the pool is first narrowed to the claims the teller judges MOST STRONGLY -- the largest
    `|deed_valence|` by the teller's own projected pursuits -- and the comparator picks among those;
    where no claim carries valence (every one 0) the pick is the unslanted one exactly. A teller
    passes on the deed that matters most to THEM, not the newest thing they hold. At `newest` (the
    CONTROL, shipped), with no `teller`, or with no `fx`, it is the pre-G3 pick and reads no
    pursuits."""
    pool = [c for c in claims if c.subject == subject] if claims else []
    if teller is not None and fx is not None and pool and _slant(fx) == "valence":
        axis_w = to_axes(crisis_weights(teller, fx.get("scar_weight_shift")))
        strength = {id(c): abs(deed_valence(axis_w, c)) for c in pool}
        top = max(strength.values())
        if top > 0:
            pool = [c for c in pool if strength[id(c)] == top]
    reader = LedgerReader(pool)
    # ABSENT: H-198 deception  (an `absent` hole row, read by harness/register.py; nothing reads this marker)
    c = (reader._best(lambda c: c.subject == subject and c.predicate != SEEN_PREDICATE)
         or reader.latest_about(subject))
    if c is None:
        return None
    return Said(c.subject, c.predicate, c.value, c.confidence, c.chain)


def confided_outside(claims, said: "Said", hearer: str) -> bool:
    """v9 IN-18 `G6`: DOES A COPY OF `said` IN `claims` HOLD A CONFIDENCE CIRCLE `hearer` IS OUTSIDE?
    The copy is the claim with the said `(subject, predicate, value, chain)` -- the four fields
    `said_of` copies out of it above, so the match lives beside the copy it inverts. A circle is a
    tuple `Claim.visibility` (a confided telling's deposit, `loop/witness.py::_circle_of`); `"own"`
    is none. `claims` is the TELLER'S OWN ledger, passed by the fold (`loop/resolve.py::
    _confidence_broken`); this reads nothing else."""
    key = (said.subject, said.predicate, said.value, tuple(said.chain))
    return any(isinstance(c.visibility, tuple) and hearer not in c.visibility
               and (c.subject, c.predicate, c.value, c.chain) == key
               for c in claims)


# ---------------------------------------------------------------------------
# A DECLARED INTENT -- telling `T7` (G9; v9 IN-16, `ED-IN-0282`). The claim kind
# `rosters.yaml: intent_claim` declares: `(actor, <stem>:<verb>, ((name, id), ...))`, an act the actor
# has CHOSEN and not yet done. Minted at CHOOSE by `decision/choose.py::declare_intents` onto a
# telling's `said`, so the told deposit (`loop/witness.py`) lands it in each hearer's ledger with the
# teller as the chain; read back by `queries/world_q.py::named` (`intent_named`). Both halves of the
# value's shape live here, once.
# ---------------------------------------------------------------------------
INTENT_STEM = roster_map("intent_claim", "claim").get("predicate")
INTENT_NAMES = roster("intent_claim", ordered=True)


def _check_intent_claim(stem, names, requires_stems, requires_operands, taken) -> None:
    """Refuse, at import, an intent stem that another reader already answers, and a carried name
    that is no operand. A `requires` grammar stem would read the intent as a WORLD FACT
    (`WorldReader.read`) and make it a cell `record` pairs; the `seen` or `content:` predicate, or an
    emitted event kind, would give one predicate two meanings. `ValueError`, not `gaps.Unspecified`:
    this module may reach `data/`, the carriers and the trace sink only (the AX-2 allow-list)."""
    if not stem or ":" in str(stem):
        raise ValueError(f"rosters.yaml: intent_claim.claim.predicate is {stem!r}; it is a bare stem "
                         f"and the intended verb is its argument")
    if stem in requires_stems or stem in taken:
        raise ValueError(f"rosters.yaml: intent_claim.claim.predicate {stem!r} is already a "
                         f"predicate another reader answers; an intent is not a world fact or an event")
    bad = [n for n in names if n not in requires_operands]
    if bad:
        raise ValueError(f"rosters.yaml: intent_claim names {bad}, which are not `requires_operands` "
                         f"members; an intent carries the ids its act's operands bind")


_check_intent_claim(INTENT_STEM, INTENT_NAMES, REQUIRES_STEMS, REQUIRES_OPERANDS,
                    {SEEN_PREDICATE, RECORD_CONTENT.get("predicate")} | set(_verbs.EMITTED_KINDS))


def intent_said(actor: str, verb: str, operands, confidence: int) -> Said:
    """WHAT A TELLER SAYS WHEN THEY DECLARE AN INTENT: `actor` will do `verb`, on the ids `operands`
    binds under `INTENT_NAMES` (a non-string operand -- a list of addressees -- is not carried). A
    `Said` with an empty chain: the actor's own intent is no hearsay. Person-side; reads no ledger."""
    ops = operands if isinstance(operands, dict) else {}
    value = tuple((n, ops[n]) for n in INTENT_NAMES if isinstance(ops.get(n), str))
    return Said(actor, f"{INTENT_STEM}:{verb}", value, confidence, ())


def intent_named(c) -> tuple:
    """The ids a declared-intent claim (or `Said`) names -- `intent_said`'s value read back; `()` for
    any other predicate. `queries/world_q.py::named`'s intent branch."""
    stem, sep, _ = str(c.predicate).partition(":")
    if not sep or stem != INTENT_STEM or not isinstance(c.value, tuple):
        return ()
    return tuple(v for _n, v in c.value)


def known_persons(claims, actor) -> tuple:
    """THE PERSONS THIS HOLDER KNOWS OF, from their OWN claims only -- sorted ids, never `actor`
    (telling workplan `T4`, `ED-IN-0282`). Three sources, and no other:

      * a truthy existence reading of a person -- `rosters.yaml: known_person_operands.claim.
        predicate`, deposited where a fold asked whether somebody exists;
      * who was SEEN doing something -- the `seen` claim's `seen_term` (`Seen.who`);
      * who TOLD them something -- a told claim's last teller, `chain[-1]`.

    A person is never known from the world: no presence read, no roster of acquaintances (`AX-2`).
    WHETHER the person is present to hear is the fold's question (`tell`'s `hearer` conjunct, the
    `with` stem), so a known person who has walked away is still named and the telling is refused
    -- and the person does NOT learn it from the refusal (`news.untold` is one kind for both
    conjuncts and the `with` read is never deposited, `witness.py`). The actor is excluded because a
    person does not tell themselves (`opening_set`'s counterparty rule declines it too).
    ⚠ THE TOPIC IS NOT EXCLUDED (v9 IN-18 step 2a, #453): a telling names its topic on `subject`
    and its hearer on `to`, and they MAY be one person -- B, knowing C and holding `(C, x)`, may tell
    C what B holds about C. Until step 2a the topic was discarded here, so that telling never formed.

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
    out.discard(None)
    return tuple(sorted(out))
