"""`queries/faction_q.py` -- the fourth `queries/` module.

⚠ **HISTORY, RETRACTED IN PLACE RATHER THAN DELETED.** From 2026-09-03 to plan position `20-ii`
this docstring said `04 §A.2:132` was STALE and NOT edited to add a fourth `queries/` member,
citing `layer-conformance` B4's third disposition (an internal ambiguity between `04`'s own
clauses -- §A.2:132 naming three modules while §B.6.1/§B.10-12/§C.5.1, all also ratified, already
named `faction_q` by its own dotted path) and CLAUDE.md §0.05's *"a spec edited to match its
implementation checks nothing"* as the reason NOT to fix it there. **THAT REASONING NO LONGER
APPLIES: `20-ii` is the module going from partial to complete, which the contradiction's own
resolution names as exactly the moment to edit §A.2:132 -- not the code catching up to a stale
spec, but the spec's own deferred edit landing on schedule.** `04:132-141` now names this module;
`queries/__init__.py` records the same history at more length. Nor is the repair to fold this
function into `world_q.py`: `world_q.py`'s own docstring already resolved a materially different
version of this question (whether `WorldReader`/a hypothetical `polity_q` deserves a fourth module)
the OTHER way, and that precedent is followed where it actually applies -- see `queries/__init__.py`
for why `faction_q` is distinguished from it rather than silently overriding it.

⚠ **SCOPE, WIDENED AT PLAN POSITION `20-ii` (U9/R-04).** The governance workplan that named
`faction_q` (`ED-IN-0215`, amended `ED-IN-0253`) lists six eventual members -- `resolve, holdings,
purview, superiors, subordinates, at_war` -- and until this position only `resolve` had a located
ratified signature and a consumer (§C.5.1). `20-ii`'s own instruction
(`workplans/2026-09-18-governance-settlement-behaviour-plan_part2.md:1459-1474`) is what supplies
the other five: *"`faction_q` as queries, never fields: resolve, holdings, purview, superiors,
subordinates, at_war."* Building them earlier, with no located signature and no consumer, would
have been the speculative apparatus `CLAUDE.md` forbids -- that is why the note above this one
stood for as long as it did, and it is retracted here rather than deleted, so the next session sees
that the deferral was deliberate and not an oversight.

⚠ **`head` HAS A REAL READER NOW, AND IT IS STILL VACUOUS TODAY -- BOTH THINGS ARE TRUE AND NEITHER
CONTRADICTS THE OTHER.** §B.6.1 cites its derivation input as `F.4` -- PART F's own list of what the
spec declares insufficient: *"what `Tenure.degree` IS -- a field with a writer and no reader ... if
it is the strength of a `commit`, every faction's leadership Query has no input and every faction is
leaderless."* `04 §F.34`: *"if `Tenure.degree` gets a reader the head resolves with it."* `20-ii`'s
own instruction is *"`head` via `Tenure.degree` (F.4's first reader)"*, and `20-iv`'s row names the
SAME input as its own morale candidate, attacked at that build. **The attack landed here, and is
recorded rather than routed around:** `harness/populated.py:692` -- the world-builder's ONE `commit`
opener -- mints every membership edge as `Tenure(id, pid, fid, "commit", 0)`, four positional args,
no fifth; `degree` is therefore the dataclass default, `None`, on every `commit` Tenure any builder
in this tree mints. `commit`'s own `verb_table.yaml` row declares `contests: ""` (empty, falsy), and
`04 PART D` row 30a types `writes` as Degree-keyed only for a verb that declares `contests:` -- so an
uncontested `commit` never reaches a fold branch that could write one, and cannot without a design
change nothing here makes. So `head` below is a genuine reader -- it
would pick up a value the instant anything ever writes a non-`None` `degree` onto a live `commit`
Tenure -- and it MEASURABLY returns `None` for every faction in every world this tree can build
today, for the reason just given rather than by construction. That is the honest state of F.4's
first reader, not a second stub wearing the first one's clothes.

⚠ **`holdings` AND `seats` ARE THE SAME SHAPE, READ TWICE.** §B.6.1: `holdings` is "the union of
MEMBERS' hold objects"; `seats` is "the seats members hold". Both are the identical query -- every
live `hold` Tenure whose SUBJECT is a member of this faction -- split only by which store the
`object` resolves in (`w.rungs` vs `w.offices`). This is narrower than `world_q.footprint()`, which
also unions in members' `contain` presence and the faction-Proposition's OWN direct `hold` edges;
§B.6.1 asks a different, more literal question than `footprint` does, so this does not reuse it.

⚠ **THE VIEW HAS A DOCUMENT FORM, AND ITS SHAPE IS OWNED HERE (plan position `20-iii`, THE
INFORMATION CLUSTER).** `survey` (`loop/effects.py::_eff_survey`) resolves a `Faction` at the moment
of writing and freezes it into a `Record` of kind `SHEET_KIND` -- proposal 14's *"a faction sheet is
those Queries, resolved at the moment of writing and frozen into a `Record`"*
(`proposals/2026-09-12-emergent-narrative-primitives-v2/01_THE_TEN.md`). That kind's key list lives in
`rosters.yaml: record_kinds`, because `Record.__post_init__` refuses any content whose keys are not
its kind's (⊕L35) and that roster is the one place it reads. So one key list has two owners -- this
dataclass's fields and that roster row -- and `_check_sheet_keys` below REFUSES AT IMPORT if they
differ, in either direction or in order. Without it a field added to `Faction` -- a stat vector, say,
which `20-ii`'s own instruction still refuses (`workplans/2026-09-28-the-plan-one-order-mc-v18-
retired.md:747`, quoting `04:301`'s `NEVER:` list -- *"it never makes a faction stat vector a
field of its own"*) -- would load clean and then crash the first season in which anyone surveyed,
inside RESOLVE, as a `Forbidden` naming a Record rather than this class. `purview`/`superiors` below
are FUNCTIONS, never fields, so neither touches this list. This is not a sixth member of the
module's scope: it is the constructor's own output, named as a document. Nothing here reads a
Record.
"""
from __future__ import annotations

from dataclasses import dataclass, fields

from .world_q import establishment_of, members
from ..data.rosters import RECORD_KIND_KEYS
from ..gaps import Unspecified
from ..state.containment import descendants
from ..state.world import World
from ..trace_log import TRACE


@dataclass(frozen=True)
class Faction:
    """§B.6.1's five-field VIEW. Built at a barrier, handed on, dropped at the next (G.2.8) --
    NEVER a member of `World`, a field of its own, `Act.actor`, a `contest` claimant, or a `hold`
    subject. `holdings`/`seats` hold bare ids (`RungId`/`SeatId` are this tree's naming for them,
    not dataclasses of their own -- no `Seat` class exists in `state/carriers.py`; an Office id
    held via a `hold` Tenure is what the spec calls a seat)."""
    proposition: str
    members: list
    holdings: list
    seats: list
    head: "str | None"


def resolve(w: World, prop: str) -> Faction:
    """§B.6.1's one constructor. `sides = (faction_q.resolve(proj, A), faction_q.resolve(proj, B))`
    -- §C.5.1, called ONCE per side before a provider runs; never re-derived inside one.

    ⚠ `head=None` WAS HARDCODED HERE UNTIL PLAN POSITION `20-ii`; IT NOW CALLS `head()` BELOW, F.4's
    first reader. The visible behaviour does not move today (`head()`'s own docstring: MEASURED
    vacuous, for a stated reason) -- what moves is that this is a real read of `Tenure.degree`
    rather than a literal, so a future `commit` degree writer needs no second edit here."""
    TRACE.query("resolve", "resolver")
    mem = members(w, prop)
    inside = set(mem)
    held = [t for t in w.tenures if t.kind == "hold" and t.live and t.subject in inside]
    holdings = sorted({t.object for t in held if t.object in w.rungs})
    seats = sorted({t.object for t in held if t.object in w.offices})
    return Faction(proposition=prop, members=mem, holdings=holdings, seats=seats,
                   head=head(w, prop))


def head(w: World, prop: str) -> "str | None":
    """F.4's first reader (plan position `20-ii`): the subject of the live `commit` Tenure to
    `prop` carrying a non-`None` `Tenure.degree`; among more than one, the one `w.tenures` places
    LAST (see the no-cross-domain-ladder note below for why "last", never "highest"). Per
    `04 §F.34`'s *"if `Tenure.degree` gets a reader the head resolves with it"*.

    ⚠ MEASURABLY `None` TODAY, FOR A NAMED REASON, NOT BY CONSTRUCTION. `commit`'s own
    `verb_table.yaml` row declares `contests: ""` (empty -- `VERB_TABLE["commit"].contests` is
    falsy), and `04 PART D` row 30a types `writes` as Degree-keyed only for a verb that declares
    `contests:`, so an uncontested `commit` never reaches a fold branch that could write one. The
    world-builder's one `commit` opener (`harness/populated.py:692`) mints every membership edge
    with the dataclass default -- so no live `commit` Tenure this tree can build ever carries a
    non-`None` `degree`. This is the `20-iv`/MB-lane attack `workplans/2026-09-28-the-plan-one-
    order-mc-v18-retired.md:808-811` asks `20-ii` to run at the build; it landed here and is a
    real gap for the MB lane to pick up (`Faction.head`/`resolve_field`'s `morale_start`
    candidate), not a Jordan escalation from this position -- `commit` staying uncontested is
    this tree's own design, not an open question.

    ⚠ NO CROSS-DOMAIN DEGREE RANK IS INVENTED HERE. `Tenure.degree` carries whichever band the verb
    that graded it uses (`FELLED/WOUNDED/UNTOUCHED` for combat, `DECLARED/WON/LOST/UNOPPOSED` for a
    field contest, ...) and no ratified ladder orders those bands against each other (`seam/ladder`
    owns ONE ladder, `D-30`, and it is the dice-engine `Degree` enum -- `OVERWHELMING/SUCCESS/
    PARTIAL/FAILURE` -- a different vocabulary again). Building a "which degree wins" comparator
    across families would be the speculative, scale-local dialect `CLAUDE.md` §10 forbids. So on
    the day more than one live `commit` carries a degree, this picks the one `w.tenures` places
    LAST -- `state/containment.py::home_of`'s own precedent for the identical ambiguity (more than
    one live edge where the model expects one): *"LAST WRITE WINS ... the incumbent behaviour of
    every site this replaces, preserved deliberately rather than quietly tightened here."*"""
    TRACE.query("head", "resolver")
    graded = [t for t in w.tenures
              if t.kind == "commit" and t.object == prop and t.live and t.degree is not None]
    return graded[-1].subject if graded else None


def holdings(w: World, prop: str) -> list:
    """The standalone Query `20-ii`'s instruction names (`faction_q.{holdings, ...}`) -- §B.6.1's
    `holdings` field, over `resolve` rather than re-derived: `resolve(w, prop).holdings` IS this
    answer, and duplicating the walk here would be `CLAUDE.md` §8's second copy of one rule."""
    return resolve(w, prop).holdings


def purview(w: World, seat: str) -> list:
    """Every rung `seat`'s purview reaches: its own rung plus every descendant. The SET form of
    `state/gate.py::purview_reaches(w, off, rung) -> bool` -- `rung in purview(w, seat)` is that
    predicate, and both compose on the identical `containment.descendants` walk
    (`state/gate.py::purview_reaches`'s own docstring, and `world_q.reach`'s inline purview limb,
    `:445-450`, which unions the same two terms for the identical reason: `descendants` EXCLUDES
    its own rung, so the seat's rung must be unioned in explicitly or a Duke seated at his own
    duchy would never be reached by a claim about the duchy itself).

    ⚠ A RUNGLESS SEAT (a cluster, S6.2) REACHES NOTHING -- `[]`, matching `purview_reaches`'s own
    `seat.rung is None -> False`; a CONTENT fact about such a seat, not a refusal. An unknown seat
    id answers the same way rather than raising, so a caller need not guard `seat in w.offices`
    first -- `04 §B.7`: a seat "adds no verb and no modifier", so this asks the seat's declared
    `rung` and nothing else, never a field."""
    TRACE.query("purview", "resolver")
    off = w.offices.get(seat)
    if off is None or off.rung is None:
        return []
    return sorted({off.rung} | set(descendants(w, off.rung)))


def superiors(w: World, person: str) -> list:
    """Every live `oblige` edge's OBJECT, for `person` as SUBJECT -- `H-101`'s own candidate
    (`01_AXIOMS.md` §E.1.1): *"the candidates are `tenure_kinds` members already rostered (`oblige`,
    `tie`)"*, and `oblige`'s domain is `Person -> Person | Office` (`loop/predicates.py::
    _req_oblige`'s own comment), so the return type is `(SeatId | PersonId)[]`, not resolved to
    either -- returning the raw object is the whole of the answer, because `oblige`'s edge IS the
    superior relation (`§E.1.5`: *"subordination is sworn by a person, at both scales ... there is
    one relation, and it was never institutional"*), never a field walk over `contain`.

    ⚠ EVERY LIVE `oblige` OBJECT IN THIS TREE IS A SEAT TODAY, MEASURED, NOT ASSUMED --
    `loop/predicates.py::_req_oblige` clause 1 refuses any subject that is not `w.offices`
    (*"A person, a rung, a Record or a bare string refuses"*), so the `Person -> Person` half of
    `oblige`'s own ratified domain is unbuilt. This does not filter for it: a future build of that
    half needs no second edit here, exactly `head`'s reasoning above for `Tenure.degree`."""
    TRACE.query("superiors", "resolver")
    return sorted(t.object for t in w.tenures
                  if t.kind == "oblige" and t.subject == person and t.live)


def subordinates(w: World, seat: str) -> list:
    """Every person with a live `oblige` to `seat` -- `H-101`'s office half, `§E.1.5`: *"A body's
    subordination is exactly as strong as the people currently seated in it."* Composes on
    `world_q.establishment_of` rather than re-deriving the identical `w.tenures` walk (`CLAUDE.md`
    §8): `establishment_of(w, office_id)` IS *"the persons obliged to this seat"*, sorted here
    because that function preserves `w.tenures` order and every sibling Query in this module
    returns sorted ids."""
    TRACE.query("subordinates", "resolver")
    return sorted(establishment_of(w, seat))


# `20-ii`'s instruction names `at_war` last; the `mood` a war Proposition carries. `Proposition.mood`
# is a plain string with no roster of allowed values (`OUGHT`/`HOLDS` are the two the tree already
# mints, `harness/populated.py:658,661`); `WAR` is a third, idiomatic value of the SAME field, never
# a new one -- `_eff_utter` already writes whatever `payload["mood"]` names, so this needs no new
# verb and no matrix row. Declared once, beside the one function that reads it, the way `SHEET_KIND`
# is declared beside `resolve`.
WAR_MOOD = "WAR"


def at_war(w: World, a: str, b: str) -> bool:
    """`04:451`, verbatim signature and docstring: *"over live `commit`s to a WAR Proposition.
    NEVER a stored flag."* `D-48`: *"war is a `WAR` Proposition with an `utterer` (AX-6) plus
    `commit` edges owned by their subjects; `at_war` is a Query over the live ones ... There is no
    boolean between two factions to set, because there is no faction record to hold one."*

    A `WAR_MOOD` Proposition names its two parties directly, the same shape a creed's `OUGHT`
    Proposition names its leader (`subject`) and faction (`value`, `harness/populated.py:661`):
    `subject` and `value` are the two factions, UNORDERED (a war has no "first" side), so this
    compares `{p.subject, p.value}` as a set against `{a, b}` rather than picking a slot for
    either. `at_war` asks whether that Proposition still has ANY live `commit` -- `F.32`: *"a
    `commit` whose subject is the declaring person, so `T-m` gives peace to the declarer"* (peace
    = writing `until` on that edge, the owner's own discretion, exactly as a faction's own
    membership commits close).

    ⚠ MEASURABLY `False` FOR EVERY PAIR IN EVERY WORLD THIS TREE'S WORLD-GEN CAN BUILD TODAY --
    BUT NOT FOR WANT OF A PRODUCER. `_eff_utter` (generic over `mood`) and `_eff_commit` are both
    shipped, uncontested, `own`-eligible verbs, so a hand-built `Act(verb="utter", payload=
    {"mood": WAR_MOOD, "subject": a, "value": b})` followed by a `commit` to the Proposition it
    mints is a REAL fold today, not a hypothetical one -- `10_FACTIONS_AND_DEPLOYMENT.md` §4.1's
    gap list (`F.33`) is about whether `at_war` may gate a verb's `requires`, which is a narrower,
    still-open question than whether the Proposition can exist. No world-generation code (`cast`,
    `build_realm`, the corpus overlays) currently AUTHORS such an act, which is why every corpus
    and populated-realm world reads `False` for every pair -- a fact about what nothing yet
    chooses to utter, not about this Query. The falsifier this module's test file carries drives
    the real fold rather than planting a Tenure by hand, to prove that."""
    TRACE.query("at_war", "resolver")
    pair = {a, b}
    for p in w.propositions.values():
        if p.mood != WAR_MOOD or {p.subject, p.value} != pair:
            continue
        if any(t.kind == "commit" and t.object == p.id and t.live for t in w.tenures):
            return True
    return False


# THE `record_kinds` MEMBER A SURVEY MINTS -- `world_q.WORKS_KIND`'s shape: named once, beside the
# owner of what it carries, and refused at import below if the roster stops carrying it as this
# dataclass's fields.
SHEET_KIND = "faction_sheet"


def _check_sheet_keys(keys) -> None:
    """THE SHEET KIND'S KEYS ARE `Faction`'s FIELDS, EXACTLY AND IN ORDER -- or `Unspecified`.

    A function and not an inline `if`, so the test can plant a drifted roster and watch it refuse
    (`CLAUDE.md` §0.1 pt 3: a load check with no falsifier cannot be told from one that never
    runs). ORDER is checked as well as membership because `loop/witness.py::content_value` freezes a
    document's content as `(key, value)` pairs in the order the mapping carries, and the mint builds
    the mapping from this dataclass -- a roster listing the same five keys in another order would
    describe a document nobody writes."""
    want = tuple(f.name for f in fields(Faction))
    if keys is None or tuple(keys) != want:
        raise Unspecified(
            f"`rosters.yaml: record_kinds.{SHEET_KIND}` is {keys!r}, and `Faction`'s fields are "
            f"{list(want)}", "rosters.yaml -- record_kinds",
            needs=f"a `{SHEET_KIND}: {list(want)}` row -- or `Faction` and the row changed together",
            law="plan position `20-iii` -- a faction sheet IS the resolved view frozen into a "
                "Record, so its keys are the view's fields; a second key list that may drift is a "
                "document the survey cannot mint (⊕L35 refuses it at construction, mid-season)")


_check_sheet_keys(RECORD_KIND_KEYS.get(SHEET_KIND))
