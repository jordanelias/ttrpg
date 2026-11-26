"""THE LARDER LADDER -- the `settlements` module's two `query` entries (A-25; v9 IN-07 E1).

MODULE ENTRIES: reached by the composition rows whose targets are `larder_draw` and `drawn_under` below
(`entry: query` -- a projection consumer calls each, not a verb's adapter and not a loop step),
registered in `manifest.MODULE_ENTRIES` by the registrar at driver construction, and held there by
`manifest/registrar.py::require_entries` against the host's declared needs
(`queries/world_q.py::QUERY_ENTRIES`), so a deleted or stripped row refuses at construction. The host
reaches them by role string through `engine.substrate.composition.require`, because some callers run
with no driver (the tests that read `demanded`/`delivered` on a bare world; `harness/scarce.py` builds its
driver before it calls them).

It takes the host's typed input record and returns a typed output record, and imports the record types,
nothing else. It never reads or writes `World`, holds no token and keeps no state between calls; it
draws nothing, so it takes no rng. The projection (`world_q.larder_input`, `world_q.under_input`), the
public names (`subsistence_draw`, `demanded`, `delivered`) with their `TRACE.query` lines, and every
write MATTER makes from the record stay host.

THE RULE (`ED-IN-0246` item 3a, `ED-IN-0255`):
  * ONLY A COHORT EATS. An eater whose `is_cohort` is false is not in the record: he wants nothing,
    draws nothing and is never short (`ED-IN-0255`, Jordan 2026-09-18, *"it's a territorial issue"*).
  * No weights registered gives an empty record (`H-11`: the loop is over the weights, so a kind with
    no weight is not drawn at all, never read as a weight of zero).
  * Per eater in the host's pid order, per weighted kind in kind order: `want = weight x Person.weight`,
    skipped when `<= 0`.
  * THE WALK: the eater's ladder is read home first, then up, and a rung counts only if it holds `> 0`
    of the kind in the RUNNING view -- what this draw has left, else the rung's own stores. The running
    view is why two eaters cannot spend the same unit, and how scarcity binds. `LarderInput.walk` says
    how far it goes (`Fixtures.larder_walk`, `H-528`):
      - `"first"` (the control; `through` ships since B12a.62's close): the first such rung gives `min(want, held)` and the remainder is NOT walked
        further up.
      - `"through"`: each such rung gives `min(want - taken so far, held)` and the walk goes on up the
        ladder until `want` is met or the ladder ends, so a town with a few units at home reaches the
        treasury above. The ladder is the eater's own ancestry and nothing else (no rung beside it is
        reached, `ED-SE-0053`).
    A cell is `(kind, want, take, source, parts)`: `source` the FIRST rung drawn from (`None` when no rung
    on the ladder holds any of that kind: a shortfall, never an error), `take` the sum, and `parts` every
    rung drawn from with its units, `((source, take),)` under `"first"` and `()` where `source` is `None`.
    The debit (`subsist.py`) is per part, so a draw split across rungs takes from each exactly what it gave.
    A `walk` outside the two raises, never read as the control.
  * `drawn_under` sums one column (`want` or `take`) over the rows whose home lies in the subtree,
    returned sorted by kind.
"""
from __future__ import annotations

from engine.season.queries.inputs import DrawRecord, DrawRow, LarderInput, Under


def larder_draw(inp: LarderInput) -> DrawRecord:
    """What every housed cohort asks of the larder ladder this season, what it is given, and from where."""
    if inp.walk not in ("first", "through"):
        raise ValueError(f"larder_draw walk {inp.walk!r} is neither 'first' nor 'through'")
    if not inp.weights:
        return DrawRecord(())
    ladders = dict(inp.ladders)
    stock = {(rung, kind): units for rung, kinds in inp.stores for kind, units in kinds}
    left: dict = {}           # (rung, kind) -> units still unspent this draw
    rows = []
    for e in inp.eaters:
        if not e.is_cohort:
            continue
        cells = []
        for kind, wt in inp.weights:
            want = wt * e.weight
            if want <= 0:
                continue
            parts = []        # ((rung, units), ...) in walk order: what each rung gave
            for rung in ladders.get(e.home, ()):
                held = left.get((rung, kind))
                if held is None:
                    held = stock.get((rung, kind), 0)
                if held <= 0:
                    continue
                part = min(want - sum(u for _, u in parts), held)
                left[(rung, kind)] = held - part
                parts.append((rung, part))
                if inp.walk == "first" or sum(u for _, u in parts) == want:
                    break
            cells.append((kind, want, sum(u for _, u in parts), parts[0][0] if parts else None, tuple(parts)))
        rows.append(DrawRow(e.pid, e.home, tuple(cells)))
    return DrawRecord(tuple(rows))


def drawn_under(inp: Under) -> tuple:
    """`((kind, units), ...)`, sorted: one column of the draw summed over the eaters homed in the subtree."""
    if inp.column not in ("want", "take"):
        raise ValueError(f"drawn_under column {inp.column!r} is neither 'want' nor 'take'")
    out: dict = {}
    for row in inp.record.rows:
        if row.home not in inp.subtree:
            continue
        for kind, want, take, _src, _parts in row.cells:
            out[kind] = out.get(kind, 0) + (want if inp.column == "want" else take)
    return tuple(sorted(out.items()))
