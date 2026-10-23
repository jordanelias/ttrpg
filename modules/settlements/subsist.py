"""ONE SEASON'S SUBSISTENCE -- the `settlements` module's `step_call` entry (A-25; v9 IN-07 E2).

MODULE ENTRY: reached by the composition row whose target is `subsist` below (`entry: step_call` -- a
loop step calls it: MATTER, `loop/matter.py`, once a season, where it called `world_q.subsistence_draw`).
Registered in `manifest.MODULE_ENTRIES` by the registrar at driver construction and held there by
`manifest/registrar.py::require_entries` against the host's declared need (`loop/matter.py::STEP_CALLS`),
so a deleted, stripped or re-kinded row refuses at construction. MATTER looks it up in `MODULE_ENTRIES`,
as the other `step_call` host (`seam/wrappers/fieldwork.py`, `fieldwork.find`) does.

It takes the host's typed input record and returns a typed outcome, and imports the record types and
its own module's larder rule, nothing else. It never reads or writes `World`, holds no token, keeps no
state between calls and draws nothing. EVERY WRITE STAYS HOST, in MATTER: the body writes, the
`_crossings` emissions, the deaths, the debit writes with `observed=`, the `Observation` construction
(the `shortfall:` predicate is host vocabulary, `data/requires.py`), `World._subsistence_shortfall`
and the `TRACE.note` sample.

THE RULE (moved here from MATTER's larder pass, items 3a/3b and plan position `19d`; unchanged clause for
clause):
  * THE DRAW is `larder_draw`'s (`larder.py`) -- the same function, so the draw MATTER writes from and the
    one `demanded`/`delivered` sum cannot disagree: one module computes both (`ED-IN-0246` item 3a).
  * THE DEBIT: per source rung, `take` summed per kind, kinds in the order the draw first debited them.
    `larder_after` is the source's stores less that debit, kept only where a unit moved. The draw capped
    every take at what was held, so nothing goes below zero and no `max(0, ...)` hides an error.
  * SHORT: an eater is short a kind by `want - take` where `take < want`. A source that gave out with a
    mouth still unfed is DRAINED for that kind (`source None` drains nothing: a ladder never stocked).
  * THE DRAINED RUNG'S GAP: per drained kind, `demanded - delivered` over the rung's subtree -- the
    eaters whose home's chain passes through it, summed by `drawn_under` -- kept only where positive.
    It NESTS (a hearth and its settlement can both report one hungry household): the Query's meaning.
  * THE BODY: `lost = body_step x (units short, summed in kind order)`; nothing falls at `lost <= 0`
    (the `body_step = 0` control arm); the body falls to `max(0, body - lost)`, and dies at `<= 0`.
  The ORDER RULE (#353 §25: draw before produce) is the host's: MATTER calls this before the yield.
"""
from __future__ import annotations

from engine.season.queries.inputs import BodyFall, SubsistInput, SubsistOutcome, Under

from .larder import drawn_under, larder_draw


def subsist(inp: SubsistInput) -> SubsistOutcome:
    """Who ate what from where, who went short, whose body falls and to what, and each drawn larder after."""
    draw = larder_draw(inp.larder)
    debit: dict = {}          # source rung -> {kind: units given up}, first-debit order
    short: dict = {}          # pid -> {kind: units short}, record order
    drained: dict = {}        # source rung -> {kinds it ran out of with a mouth unfed}
    for row in draw.rows:
        for kind, want, take, src in row.cells:
            if src is not None:
                given = debit.setdefault(src, {})
                given[kind] = given.get(kind, 0) + take
            if take < want:
                short.setdefault(row.pid, {})[kind] = want - take
                if src is not None:
                    drained.setdefault(src, set()).add(kind)

    shortfalls = []
    for src in sorted(drained):
        under = frozenset(home for home, chain in inp.chains if src in chain)
        need = dict(drawn_under(Under(draw, under, "want")))
        got = dict(drawn_under(Under(draw, under, "take")))
        gaps = []
        for kind in sorted(drained[src]):
            gap = need.get(kind, 0) - got.get(kind, 0)
            if gap > 0:
                gaps.append((kind, gap))
        if gaps:
            shortfalls.append((src, tuple(gaps)))

    bodies = dict(inp.bodies)
    falls = []
    for pid in sorted(short):
        lost = inp.body_step * sum(short[pid].values())
        if lost <= 0:
            continue
        after = max(0, bodies[pid] - lost)
        falls.append(BodyFall(pid, after, after <= 0))

    held = {rung: dict(kinds) for rung, kinds in inp.larder.stores}
    larder_after = []
    for src in sorted(debit):
        have = held.get(src, {})
        left = tuple((kind, have.get(kind, 0) - units) for kind, units in debit[src].items())
        if any(units != have.get(kind, 0) for kind, units in left):
            larder_after.append((src, left))

    return SubsistOutcome(draw, tuple((pid, tuple(kinds.items())) for pid, kinds in short.items()),
                          tuple(shortfalls), tuple(falls), tuple(larder_after))
