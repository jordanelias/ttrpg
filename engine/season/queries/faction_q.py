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
INFORMATION CLUSTER).** `survey` (`loop/effects_information.py::_eff_survey`) resolves a `Faction` at the moment
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
from .world_q import density, enclosing_territory, footprint, provinces_of, residence_of, sovereign_fraction
from .world_q import head  # noqa: F401 -- B21.65: MOVED to `world_q` (`opinion_of` regards the present head and this module imports `world_q`, so a definition here is a cycle); re-exported, the `at_war` precedent above, so `faction_q.head` is the one owner's function object
from ..data.rosters import RECORD_KIND_KEYS, territory_id_of, territory_weight_of
from ..gaps import Unspecified
from ..state.containment import descendants
# B21b.13 (CR-91 (4)): `civil_war` reads the sovereign's seats (the realm's rung kind) and the vassal oaths sworn to them.
from .world_q import REALM_KIND
from ..state.gate import is_sworn_to, seat_faction
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

    ⚠ `head` IS `world_q.head` (re-exported above), F.4's first reader: a real read of `Tenure.degree`, so a future
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


def holdings(w: World, prop: str) -> list:
    """The standalone Query `20-ii`'s instruction names (`faction_q.{holdings, ...}`) -- §B.6.1's
    `holdings` field, over `resolve` rather than re-derived: `resolve(w, prop).holdings` IS this
    answer, and duplicating the walk here would be `CLAUDE.md` §8's second copy of one rule."""
    return resolve(w, prop).holdings


def purview(w: World, seat: str) -> list:
    """Every rung `seat`'s purview reaches: its own rung plus every descendant. The SET form of
    `state/gate.py::purview_reaches(w, off, rung) -> bool` -- `rung in purview(w, seat)` is that
    predicate (⚠ SINCE v9 IN-40 ONLY WHERE NO SEAT-HOLDER HAS SWORN AN `oblige` TO `seat`: the
    predicate's oblige clause adds the swearer's ground, and this set form does not see it; the set
    form that does is `state/gate.py::purview_of`, B21b.21, which `world_q.own_purview` reads -- this
    one has no game caller and is left, the plan's call), and both
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


def civil_war(w: World, a: str, b: str) -> bool:
    """IS THE WAR BETWEEN `a` AND `b` A CIVIL WAR? (B21b.13, CR-91 (4); [ASSUMPTION; medium; Jordan to correct; revert: delete this function, nothing reads it
    before B21d].) `world_q.at_war(w, a, b)`, AND both factions' heads (`head`) hold a live, sworn `oblige` (`gate.is_sworn_to`: an imposed one is no oath) to a seat
    of the SOVEREIGN'S faction -- the faction (`gate.seat_faction`) of a seat sitting at the realm's rung (`world_q.REALM_KIND`) -- one sovereign for both (CR-86's
    vassal edges: the Duchess of Hafenmark and the Duke of Varfell are sworn to `off_king`). A war between two parties of one realm, read and never stored. A war
    the sovereign's own faction wages against a vassal is no civil war by this reading (the sovereign's head is sworn to no seat of his own): the source's sentence
    is 'both heads under the sovereign's purview'. `False` for a faction with no head, and for `a == b`. Its consumer, the breakdown clause, is CR-89 commit (3) (B21d)."""
    TRACE.query("civil_war", "resolver")
    if a == b or not at_war(w, a, b):
        return False
    heads = (head(w, a), head(w, b))
    if None in heads:
        return False
    realm = {r for r, g in w.rungs.items() if g.kind == REALM_KIND}
    sovereigns = {seat_faction(w, o.id) for o in w.offices.values() if o.rung in realm} - {None}
    return any(all(any(is_sworn_to(w, h, o.id) for o in w.offices.values() if seat_faction(w, o.id) == s) for h in heads)
               for s in sorted(sovereigns))


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


def weight(w: World, prop: str) -> float:
    """B21.68 (`U5d_FA_owed_edits` §4, A-41, A-42): HOW MUCH A FACTION'S MEMBERS COUNT -- the summed `Person.weight` of its members, each
    multiplied by the political weight of the territory he LIVES in (`rosters.yaml: tables.territory_weight`, read through
    `rosters.territory_weight_of`; an absent key, or a member with no residence or none inside a territory, reads 1.0). THE ONE OWNER of a
    faction's weight: it is a Query, computed on demand and stored nowhere (no `Rung` field, `04` §B.3's *"NEVER: any social aggregate"*), so a
    reader that wants a faction's power asks here and keeps no second copy. Residence, not presence: `world_q.residence_of` (where a person
    LIVES, which only `migrate` changes), not `home_of` (where he is). With every territory at 1.0 -- the table ships empty -- this is the
    unweighted sum of the members' `Person.weight`. It takes no token and emits nothing, and has no `TRACE.query` row of its own, `standing`'s
    precedent (a read-only step moves no committed artifact; the inner Queries keep theirs). First readers: instruments, then the councils and
    elections whose weight sets a voter's draw (A-14), never a count."""
    lives = residence_of(w)
    return float(sum(w.persons[m].weight * territory_weight_of(territory_id_of(enclosing_territory(w, lives.get(m))))
                     for m in members(w, prop)))
