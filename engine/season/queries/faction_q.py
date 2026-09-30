"""`queries/faction_q.py` -- a fourth `queries/` module, named as an ambiguity rather than fixed at
the source.

⚠ **§A.2:132 IS STALE ON THIS ONE POINT, AND `04` IS NOT EDITED TO SAY SO.** Its line reads
*"queries/ ownerless functions: world_q (World first) · person_q (asker first) · cache
(barrier-built)"* -- three members, no stated extension mechanism. But three OTHER clauses in the
SAME document, added by the identical 2026-09-03 amendment that never touched §A.2:132, name
`faction_q` as its own real module:

  - **§B.6.1** types `Faction` as a five-field VIEW and gives it exactly one constructor:
    `faction_q.resolve(w, prop) -> Faction`, "built at a barrier, handed on, dropped at the next".
  - **§B.10-12** (governance carriers) cross-reference it by that name.
  - **§C.5.1**, the mass-battle ROSTER CONTRACT: `sides = (faction_q.resolve(proj, A),
    faction_q.resolve(proj, B))` -- ONCE, before the provider runs.

This is `layer-conformance` B4's third disposition: the spec is internally ambiguous between its
own clauses, not between spec and code. §A.2:132's list is the unmaintained one -- the 2026-09-03
amendment's own diff lists the sections it touched, and §A.2 is not among them, while §B.6.1/§C.5.1
demonstrably are. **B4 is explicit that the repair is NOT to edit `04` to match the code -- "it is
ratified, and a spec edited to match its implementation checks nothing" -- so §A.2 stays exactly as
written, stale on this point, and this paragraph is the naming B4's third disposition actually
asks for.** Nor is the repair to fold this function into `world_q.py`: `world_q.py`'s own docstring
already resolved a materially different version of this question (whether `WorldReader`/a
hypothetical `polity_q` deserves a fourth module) the OTHER way, and that precedent is followed
where it actually applies -- see `queries/__init__.py` for why `faction_q` is distinguished from
it rather than silently overriding it.

⚠ **SCOPE: `resolve` ONLY.** The governance workplan that named `faction_q` (`ED-IN-0215`, amended
`ED-IN-0253`) lists six eventual members -- `resolve, holdings, purview, superiors, subordinates,
at_war`. A workplan is reference (`CLAUDE.md` §0.05); it is not this module's contract. The one
function §C.5.1 actually cites as a consumer -- the only ratified, load-bearing call site that
exists today -- is `resolve`. Building the other five now, with no located ratified signature for
`purview`/`superiors`/`subordinates` and no consumer for any of them, would be exactly the
speculative apparatus `CLAUDE.md` forbids. They are added when something reads them, not before.

⚠ **`head` IS ALWAYS `None`, AND THAT IS NOT A STUB.** §B.6.1 cites its derivation input as `F.4` --
PART F's own list of what the spec declares insufficient: *"what `Tenure.degree` IS -- a field with
a writer and no reader | carried unread ... if it is the strength of a `commit`, every faction's
leadership Query has no input and every faction is leaderless."* `Tenure.degree` IS a real field
(`state/carriers.py:59`, default `None`) -- checked, not assumed -- but MEASURED to have no
game-logic reader anywhere in the tree (`harness/populated.py:551-556`, grep, 2026-09-14); the only
touches are the gate's generic before/after diff and `World`'s hash/snapshot machinery, which treat
it exactly as every other field and read no game meaning from it. So F.4's gap is not that the field
is absent, but that it is carried unread -- ID-13's sense, not a literal one. An empirical pattern
in the corpus data (`Proposition.subject` naming a person under one `mood`) is DATA convention, not
the ratified mechanism F.4 names as unbuilt; using it would invent a mechanism the spec's own gap
list says is still open. `None`, citing `F.4`, is the honest reading -- the same "generate none
automatically rather than fabricate" precedent `world.npcs` already sets.

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
differ, in either direction or in order. Without it a field added to `Faction` (the `purview` or
`superiors` the scope note above defers, say) would load clean and then crash the first season in
which anyone surveyed, inside RESOLVE, as a `Forbidden` naming a Record rather than this class. This
is not a sixth member of the module's scope: it is the constructor's own output, named as a
document. Nothing here reads a Record.
"""
from __future__ import annotations

from dataclasses import dataclass, fields

from .world_q import members
from ..data.rosters import RECORD_KIND_KEYS
from ..gaps import Unspecified
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
    -- §C.5.1, called ONCE per side before a provider runs; never re-derived inside one."""
    TRACE.query("resolve", "resolver")
    mem = members(w, prop)
    inside = set(mem)
    held = [t for t in w.tenures if t.kind == "hold" and t.live and t.subject in inside]
    holdings = sorted({t.object for t in held if t.object in w.rungs})
    seats = sorted({t.object for t in held if t.object in w.offices})
    return Faction(proposition=prop, members=mem, holdings=holdings, seats=seats, head=None)


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
