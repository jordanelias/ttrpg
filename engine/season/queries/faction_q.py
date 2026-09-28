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
"""
from __future__ import annotations

from dataclasses import dataclass

from .world_q import members
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
