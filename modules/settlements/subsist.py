"""ONE SEASON'S SUBSISTENCE -- the `settlements` module's `step_call` entry (A-25; v9 IN-07 E2).

MODULE ENTRY: reached by the composition row whose target is `subsist` below (`entry: step_call` -- a
loop step calls it: MATTER, `loop/matter.py`, once a season).
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

THE RULE (items 3a/3b and plan position `19d`):
  * THE DRAW is `larder_draw`'s (`larder.py`) -- the same function, so the draw MATTER writes from and the
    one `demanded`/`delivered` sum cannot disagree: one module computes both (`ED-IN-0246` item 3a).
  * THE DEBIT: per rung drawn from, each cell's `parts` summed per kind (under `larder_walk` `first` a
    cell's one part is `(source, take)`; under `through` a draw splits across rungs and each loses what it
    gave), kinds in the order the draw first debited them.
    `larder_after` is the source's stores less that debit, kept only where a unit moved. The draw capped
    every take at what was held, so nothing goes below zero and no `max(0, ...)` hides an error.
  * SHORT: an eater is short a kind by `want - take` where `take < want`. A source that gave out with a
    mouth still unfed is DRAINED for that kind (`source None` drains nothing HERE: a ladder with no unit of the kind is reported at its crossing, below).
  * A FIRST DEARTH IS REPORTED ONCE (B12b.40, D-69): a short cell with no source (`src None`) is a crossing if the eater was not short of that kind in
    the last barrier (`SubsistInput.short_before`); its rung is the first of its ladder that ever carried a key for the kind (`once_held`), else the
    ladder's first rung, and it joins the drained set below. A person short of the kind again next season is no crossing: silent while the dearth lasts.
  * WHERE EACH SHORT EATER WAS SHORT (B12b.41, `SubsistOutcome.short_at`): the rung that gave out for its first short kind, else R2's rung above. The host reads
    it to cite the store on the fall; unlike the report it is not once-only, so a chronic dearth has a rung here and reports none.
  * THE DRAINED RUNG'S GAP: per drained kind, `demanded - delivered` over the rung's subtree -- the
    eaters whose home's chain passes through it, summed by `drawn_under` -- kept only where positive.
    It NESTS (a hearth and its settlement can both report one hungry household): the Query's meaning.
  * THE BODY: `lost = body_step x (units short, summed in kind order) x the eater's severity multiplier
    (1 when none is given)`, truncated to an int; under `per_head` (fixture `hunger_loss`, B12b.35) the
    `body_step x units` magnitude is first divided by the eater's `Person.weight` (floor division: one
    ladder for the body, per head), so a weight-20 cohort short the same per head loses what a weight-2 one does; the multiplier is the host's draw (`SubsistInput.severity`),
    this module draws nothing. Nothing falls at `lost <= 0` (the `body_step = 0` control arm, or a severity
    of 0); the body falls to `max(0, body - lost)`, and dies at `<= 0`.
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
        for kind, want, take, src, parts in row.cells:
            for rung, units in parts:
                given = debit.setdefault(rung, {})
                given[kind] = given.get(kind, 0) + units
            if take < want:
                short.setdefault(row.pid, {})[kind] = want - take
                # a short cell gave out EVERY rung it drew from (under `through` a draw splits across rungs: each emptied)
                for rung in (r for r, _ in parts) if parts else ((src,) if src is not None else ()):
                    drained.setdefault(rung, set()).add(kind)

    # B12b.40 (D-69): A FIRST DEARTH IS REPORTED ONCE, AT THE CROSSING. A short cell no source gave out for (`src None`: its ladder holds nothing of the kind)
    # drained no rung above, so nothing would carry it. It is a crossing if the person was not short of that kind last barrier (`short_before`), and is
    # reported at the first ladder rung that ever carried a key for the kind (`once_held`: the granary an exact multiple emptied), else, a never-stocked
    # ladder, at its first rung. `kind in short_before` makes either arm fire once per dearth, never per season.
    before = {pid: frozenset(kinds) for pid, kinds in inp.short_before}
    held_once = {rung: frozenset(kinds) for rung, kinds in inp.once_held}
    ladders = dict(inp.larder.ladders)

    def dearth_rung(home, kind):
        """R2's rung for a short `kind` no source gave out for: the first ladder rung that ever carried a key for it, else (D-69) the ladder's first."""
        ladder = ladders.get(home, ())
        at = next((r for r in ladder if kind in held_once.get(r, ())), None)
        return ladder[0] if at is None and ladder else at

    short_at: dict = {}       # pid -> the rung its first short kind was short at (B12b.41: where the fall's cause is read; a chronic dearth has one, reports none)
    for row in draw.rows:
        for kind, want, take, src, _parts in row.cells:
            if take >= want:
                continue
            at = src if src is not None else dearth_rung(row.home, kind)
            if at is not None:
                short_at.setdefault(row.pid, at)
            if src is not None or kind in before.get(row.pid, ()):
                continue                      # already counted as drained; or not a crossing
            if at is not None:
                drained.setdefault(at, set()).add(kind)

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
    sev = dict(inp.severity)
    weight_of = {e.pid: e.weight for e in inp.larder.eaters}
    falls = []
    for pid in sorted(short):
        units = sum(short[pid].values())
        step = inp.body_step * units // weight_of[pid] if inp.per_head else inp.body_step * units   # B12b.35: the Partial band's magnitude, per head under `per_head`
        lost = int(step * sev.get(pid, 1))
        if lost <= 0:
            continue
        after = max(0, bodies[pid] - lost)
        falls.append(BodyFall(pid, after))

    held = dict(inp.larder.stores)
    larder_after = []
    for src in sorted(debit):
        have = dict(held.get(src, ()))
        left = tuple((kind, have.get(kind, 0) - units) for kind, units in debit[src].items())
        if any(units != have.get(kind, 0) for kind, units in left):
            larder_after.append((src, left))

    return SubsistOutcome(draw, tuple((pid, tuple(kinds.items())) for pid, kinds in short.items()),
                          tuple(shortfalls), tuple(falls), tuple(larder_after), tuple(sorted(short_at.items())))
