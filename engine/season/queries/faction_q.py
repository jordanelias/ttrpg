"""`queries/faction_q.py` -- the fourth `queries/` module.

`04:132-141` names this module (`04 §A.2`); `queries/__init__.py` records why it is a module of its
own. `faction_q.resolve` is named by its OWN dotted path in §B.6.1 and §C.5.1, both ratified, which
is a different case from the one `world_q.py`'s own docstring resolved the other way (whether
`WorldReader`/a hypothetical `polity_q` deserves a fourth module); see `queries/__init__.py`.

⚠ **SCOPE (plan position `20-ii`, U9/R-04).** The governance workplan that named `faction_q`
(`ED-IN-0215`, amended `ED-IN-0253`) lists its members as *"`faction_q` as queries, never fields:
resolve, holdings, purview, superiors, subordinates, at_war."* A member with no located signature
and no consumer would be the speculative apparatus `CLAUDE.md` forbids; `resolve` has a located
ratified signature and a consumer (§C.5.1).

⚠ **`head` HAS A REAL READER, AND IT IS VACUOUS TODAY -- BOTH THINGS ARE TRUE.** §B.6.1 cites its derivation input as `F.4` -- PART F's own list of what the
spec declares insufficient: *"what `Tenure.degree` IS -- a field with a writer and no reader ... if
it is the strength of a `commit`, every faction's leadership Query has no input and every faction is
leaderless."* `04 §F.34`: *"if `Tenure.degree` gets a reader the head resolves with it."* `20-ii`'s
own instruction is *"`head` via `Tenure.degree` (F.4's first reader)"*, and `20-iv`'s row names the
SAME input as its own morale candidate. `boot/realm.py` -- the world-builder's `commit` opener --
mints every membership edge as `Tenure(id, pid, fid, "commit", 0)`, four positional args, no fifth;
`degree` is therefore the dataclass default, `None`, on every `commit` Tenure any builder in this
tree mints. `commit`'s own `verb_table.yaml` row declares `contests: ""` (empty, falsy), and
`04 PART D` row 30a types `writes` as Degree-keyed only for a verb that declares `contests:` -- so an
uncontested `commit` never reaches a fold branch that could write one, and cannot without a design
change nothing here makes. So `head` below is a genuine reader -- it
would pick up a value the instant anything ever writes a non-`None` `degree` onto a live `commit`
Tenure -- and it returns `None` for every faction in every world this tree can build today, for
the reason just given rather than by construction.

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
which `20-ii`'s own instruction still refuses (quoting `04:301`'s `NEVER:` list -- *"it never makes
a faction stat vector a field of its own"*) -- would load clean and then crash the first season in which anyone surveyed,
inside RESOLVE, as a `Forbidden` naming a Record rather than this class. `purview` below
is a FUNCTION, never a field, so it does not touch this list. This is not a sixth member of the
module's scope: it is the constructor's own output, named as a document. Nothing here reads a
Record.
"""
from __future__ import annotations

from dataclasses import dataclass, fields

from .world_q import WAR_MOOD, at_war, establishment_of, members  # noqa: F401 -- v11 CR-87: the first two MOVED to `world_q` (the war context's `enemies_heard` reads `at_war`, and this module imports `world_q`, so the reverse import would be a cycle); re-exported so every `faction_q.at_war` caller reads the one owner
from .world_q import density, footprint, provinces_of, sovereign_fraction
from ..data.rosters import FACTION_BY_PROP, HEAD_SEAT, RECORD_KIND_KEYS
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

    ⚠ `head` IS `head()` BELOW, F.4's first reader: a real read of `Tenure.degree`, so a future
    `commit` degree writer needs no second edit here. It is vacuous today, for the reason
    `head()`'s own docstring states."""
    TRACE.query("resolve", "resolver")
    mem = members(w, prop)
    inside = set(mem)
    held = [t for t in w.tenures if t.kind == "hold" and t.live and t.subject in inside]
    holdings = sorted({t.object for t in held if t.object in w.rungs})
    seats = sorted({t.object for t in held if t.object in w.offices})
    return Faction(proposition=prop, members=mem, holdings=holdings, seats=seats,
                   head=head(w, prop))


@dataclass(frozen=True)
class FactionStanding:
    """Where one faction stands across one rung, as `standing` reads it: four readings, each the
    answer of one `world_q` Query and none computed here. A Query return like `Faction`, never a
    member of `World` (`04` PART D row 47): a field set on one is dropped with the view.

    `footprint` -- the rung ids the faction reaches (`world_q.footprint`). `present`, `persons` --
    `world_q.density`'s pair at `rung_id`: the faction's members present, and the persons present.
    `sovereign_share`, `undetermined` -- `world_q.sovereign_fraction(w, rung_id)`: the share held by
    the single LARGEST holder over the rung's subtree (the rung's, so the same for every faction
    asked; it is not this faction's own share), and how many of its rungs nobody holds.
    `provinces` -- the territory ids `world_q.provinces_of` groups under this faction, `()` when it
    holds none."""
    footprint: tuple
    present: int
    persons: int
    sovereign_share: float
    undetermined: int
    provinces: tuple


def standing(w: World, prop: str, rung_id: str) -> FactionStanding:
    """B03.65 (`U5a_CORE_owed_edits` §I): the one composed reading of where `prop` stands at
    `rung_id`, over `world_q.footprint`, `density`, `sovereign_fraction` and `provinces_of`, which
    this is the first reader of. `endings_reached` is the precedent: a strategic reading as a Query a
    host reads and nobody stores. It takes no token, stores nothing and emits nothing, and it has
    no `TRACE.query` row of its own -- a read-only step moves no committed artifact; each inner Query
    keeps its own row, reached only when a host asks, never inside `season()`.

    ⚠ RESOLVER-SIDE, AND NOT FOR `decision/`. A person's own reading of where a faction stands is a
    belief (AX-2); this record is the world's, and may not be handed to a chooser. An NPC weighs
    territory through the claims he holds.

    ⚠ `footprint` IS `world_q.footprint`'s, NOT `resolve(w, prop).holdings`: the two differ (holdings is the
    members' `hold` objects, footprint is those holds, the faction's own, and its members' presence),
    so `holdings` is a subset of `footprint` (the test asserts it) and the two are equal only for a
    faction whose members sit nowhere but in rungs they hold."""
    fp = tuple(footprint(w, prop))
    present, persons = density(w, rung_id, prop)
    share, undetermined = sovereign_fraction(w, rung_id)
    return FactionStanding(footprint=fp, present=present, persons=persons,
                           sovereign_share=share, undetermined=undetermined,
                           provinces=tuple(provinces_of(w, rung_id).get(prop, ())))


def head(w: World, prop: str) -> "str | None":
    """F.4's first reader (plan position `20-ii`): the subject of the live `commit` Tenure to
    `prop` carrying a non-`None` `Tenure.degree`; among more than one, the one `w.tenures` places
    LAST (see the no-cross-domain-ladder note below for why "last", never "highest"). Per
    `04 §F.34`'s *"if `Tenure.degree` gets a reader the head resolves with it"*.

    ⚠ `None` TODAY, FOR A NAMED REASON, NOT BY CONSTRUCTION. `commit`'s own
    `verb_table.yaml` row declares `contests: ""` (empty -- `VERB_TABLE["commit"].contests` is
    falsy), and `04 PART D` row 30a types `writes` as Degree-keyed only for a verb that declares
    `contests:`, so an uncontested `commit` never reaches a fold branch that could write one. The
    world-builder's `commit` opener (`boot/realm.py`) mints every membership edge
    with the dataclass default -- so no live `commit` Tenure this tree can build ever carries a
    non-`None` `degree`. This is a real gap for the MB lane to pick up (`Faction.head`/`resolve_field`'s
    `morale_start` candidate), not a Jordan escalation -- `commit` staying uncontested is this tree's
    own design, not an open question.

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
    # Unreachable until something writes a degree on a `commit` (see the note above).
    graded = [t for t in w.tenures
              if t.kind == "commit" and t.object == prop and t.live and t.degree is not None]
    if graded:
        return graded[-1].subject
    # CR-86 (ED-IN-0342): a faction whose `rosters.yaml: factions` row names a `head_seat` is headed by that
    # seat's live holder -- the King for Valorsmark. A graded `commit` (above) stays the more specific
    # reading and wins where one exists [CHOICE: none is built today, so the order moves nothing].
    seat = HEAD_SEAT.get(FACTION_BY_PROP.get(prop))
    if seat is None:
        return None
    held = [t.subject for t in w.tenures if t.kind == "hold" and t.live and t.object == seat]
    return held[-1] if held else None


def holdings(w: World, prop: str) -> list:
    """The standalone Query `20-ii`'s instruction names (`faction_q.{holdings, ...}`) -- §B.6.1's
    `holdings` field, over `resolve` rather than re-derived: `resolve(w, prop).holdings` IS this
    answer, and duplicating the walk here would be `CLAUDE.md` §8's second copy of one rule."""
    return resolve(w, prop).holdings


def purview(w: World, seat: str) -> list:
    """Every rung `seat`'s purview reaches: its own rung plus every descendant. The SET form of
    `state/gate.py::purview_reaches(w, off, rung) -> bool` -- `rung in purview(w, seat)` is that
    predicate (⚠ SINCE v9 IN-40 ONLY WHERE NO SEAT-HOLDER HAS SWORN AN `oblige` TO `seat`: the
    predicate's oblige clause adds the swearer's ground, and this set form does not see it), and both
    compose on the identical `containment.descendants` walk
    (`state/gate.py::purview_reaches`'s own docstring, and `world_q.own_purview`,
    which unions the same two terms for the identical reason: `descendants` EXCLUDES
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


def subordinates(w: World, seat: str) -> list:
    """Every person with a live `oblige` to `seat` -- `H-101`'s office half, `§E.1.5`: *"A body's
    subordination is exactly as strong as the people currently seated in it."* Composes on
    `world_q.establishment_of` rather than re-deriving the identical `w.tenures` walk (`CLAUDE.md`
    §8): `establishment_of(w, office_id)` IS *"the persons obliged to this seat"*, sorted here
    because that function preserves `w.tenures` order and every sibling Query in this module
    returns sorted ids."""
    TRACE.query("subordinates", "resolver")
    return sorted(establishment_of(w, seat))


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
