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
draws nothing, so it takes no rng (the remainder's permutation, `LarderInput.order`, arrives on its typed input). The projection (`world_q.larder_input`, `world_q.under_input`), the
public names (`subsistence_draw`, `demanded`, `delivered`) with their `TRACE.query` lines, and every
write MATTER makes from the record stay host.

THE RULE (`ED-IN-0246` item 3a, `ED-IN-0255`):
  * ONLY A COHORT EATS. An eater whose `is_cohort` is false is not in the record: he wants nothing,
    draws nothing and is never short (`ED-IN-0255`, Jordan 2026-09-18, *"it's a territorial issue"*).
  * No weights registered gives an empty record (`H-11`: the loop is over the weights, so a kind with
    no weight is not drawn at all, never read as a weight of zero).
  * Per weighted kind in kind order, a cohort's `want = weight x Person.weight`, skipped when `<= 0`.
  * THE WALK, IN PASSES (B12b.39): the eater's ladder is read home first, then up, and a rung counts only if it holds `> 0` of the kind at the
    START of the pass and the eater has not yet pointed at it this draw. A short rung is SHARED in proportion to want (see `larder_draw`),
    never given to whoever came first, so two cohorts on one thin rung both go short by their share. `LarderInput.walk` says how many passes
    (`Fixtures.larder_walk`, `H-528`):
      - `"first"` (the control; `through` ships since B12a.62's close): one pass, so the remainder is NOT walked further up.
      - `"through"`: passes repeat until no eater has a rung left to point at, so a town with a few units at home reaches the
        treasury above. The ladder is the eater's own ancestry and nothing else (no rung beside it is
        reached, `ED-SE-0053`).
    A cell is `(kind, want, take, source, parts)`: `source` the FIRST rung drawn from (the first rung pointed at when the share gave it
    nothing; `None` when no rung on the ladder holds any of that kind: a shortfall, never an error), `take` the sum, and `parts` every
    rung drawn from with its units, in walk order, `()` where nothing was drawn.
    The debit (`subsist.py`) is per part, so a draw split across rungs takes from each exactly what it gave.
    A `walk` outside the two raises, never read as the control.
  * `drawn_under` sums one column (`want` or `take`) over the rows whose home lies in the subtree,
    returned sorted by kind.
"""
from __future__ import annotations

from engine.season.queries.inputs import DrawRecord, DrawRow, LarderInput, Under


def larder_draw(inp: LarderInput) -> DrawRecord:
    """What every housed cohort asks of the larder ladder this season, what it is given, and from where.

    PER KIND, IN PASSES (B12b.39; "pass" is one sweep of the walk over the eaters, neither a fight's round nor the season's lap): every
    cohort with want left points at the first rung on its ladder that holds any of the kind at the START of the pass and that it has not yet
    pointed at this draw. Per rung, claims that fit are each taken whole; claims that do not fit each take `held * claim // total` and the
    units left over go one each, in the order of `LarderInput.order`, to claimants still short (an eater `order` does not name sorts after
    those it does, in host order, so `()` is host order throughout). Under `first` there is one pass; under `through` passes repeat until
    none has a rung left to point at. Nothing is drawn here: the permutation arrives on the input."""
    if inp.walk not in ("first", "through"):
        raise ValueError(f"larder_draw walk {inp.walk!r} is neither 'first' nor 'through'")
    if not inp.weights:
        return DrawRecord(())
    ladders = dict(inp.ladders)
    stock = {(rung, kind): units for rung, kinds in inp.stores for kind, units in kinds}
    eaters = [e for e in inp.eaters if e.is_cohort]
    rank = {pid: i for i, pid in enumerate(inp.order)}
    claim_order = {e.pid: (rank.get(e.pid, len(rank)), i) for i, e in enumerate(eaters)}      # the remainder's order: the draw's, then host order
    cells = {e.pid: [] for e in eaters}
    for kind, wt in inp.weights:
        want = {e.pid: wt * e.weight for e in eaters if wt * e.weight > 0}
        taken = {pid: 0 for pid in want}
        parts = {pid: [] for pid in want}         # ((rung, units), ...) in walk order: what each rung gave
        pointed = {pid: [] for pid in want}       # every rung this eater has pointed at, in order (a rung is pointed at once per draw)
        held = {}                                 # rung -> units still unspent this draw
        while True:
            claims: dict = {}                     # rung -> [pid, ...] in host order, as the pass opened
            for e in eaters:
                if e.pid not in want or want[e.pid] <= taken[e.pid]:
                    continue
                for rung in ladders.get(e.home, ()):
                    if rung not in pointed[e.pid] and held.setdefault(rung, stock.get((rung, kind), 0)) > 0:
                        pointed[e.pid].append(rung)
                        claims.setdefault(rung, []).append(e.pid)
                        break
            if not claims:
                break
            for rung, pids in claims.items():
                claim = {pid: want[pid] - taken[pid] for pid in pids}
                total = sum(claim.values())
                if total <= held[rung]:
                    give = claim
                else:
                    give = {pid: held[rung] * claim[pid] // total for pid in pids}
                    left = held[rung] - sum(give.values())
                    for pid in sorted(pids, key=claim_order.__getitem__):
                        if left <= 0:
                            break
                        if give[pid] < claim[pid]:
                            give[pid] += 1
                            left -= 1
                held[rung] -= sum(give.values())
                for pid in pids:
                    if give[pid] > 0:
                        taken[pid] += give[pid]
                        parts[pid].append((rung, give[pid]))
            if inp.walk == "first":
                break
        for e in eaters:
            if e.pid in want:
                src = parts[e.pid][0][0] if parts[e.pid] else (pointed[e.pid][0] if pointed[e.pid] else None)
                cells[e.pid].append((kind, want[e.pid], taken[e.pid], src, tuple(parts[e.pid])))
    return DrawRecord(tuple(DrawRow(e.pid, e.home, tuple(cells[e.pid])) for e in eaters))


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
