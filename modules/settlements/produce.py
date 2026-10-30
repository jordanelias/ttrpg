"""ONE SEASON'S YIELD AND CREDIT -- the `settlements` module's second `step_call` entry (A-25; v9 IN-07 E3).

MODULE ENTRY: reached by the composition row whose target is `produce` below (`entry: step_call` -- a
loop step calls it: MATTER, `loop/matter.py`, once a season, after `settlements.subsist`). Registered in
`manifest.MODULE_ENTRIES` by the registrar at driver construction and held there by
`manifest/registrar.py::require_entries` against the host's declared need (`loop/matter.py::STEP_CALLS`),
so a deleted, stripped or re-kinded row refuses at construction.

It takes the host's typed input record and returns a typed outcome, and imports the record types,
nothing else. It never reads or writes `World`, holds no token, keeps no state between calls and draws
nothing (the season's factor is drawn by the host, `world_q.season_factor_of`, once per territory, and
handed in per rung: `ProduceInput.factor`, v10 CL-EVENTS (1)). EVERY
WRITE STAYS HOST, in MATTER: the `yield` write, the `stores` credit write and their `last_emission_of`
causes. Site WEAR stays host too (design A10).

THE RULE (moved here from MATTER's per-rung loop; unchanged clause for clause):
  * THE YIELD: per rung in id order, per Site in id order whose own `rung` is that rung (the maintained
    side, never a back-reference), per `(kind, base)` in the Site kind's table order, add
    `int(base * (max(0, condition) / scale) * factor)` -- the float expression operand for operand, since
    a reordering can move a truncation. A kind the table does not list yields nothing.
  * Zero entries are dropped; a rung whose yield is empty has no row (MATTER writes nothing there).
  * THE CREDIT: `held + produced` per produced kind, where `held` is the rung's stores AFTER the same
    season's debit (`larder_after` overlaid on `stores`), because MATTER writes a rung's debit, then its
    yield, then its credit, in sequence. A kind the rung does not hold counts from `0`.
  The ORDER RULE (#353 §25: draw before produce) is the host's: MATTER calls `settlements.subsist` first.
"""
from __future__ import annotations

from engine.season.queries.inputs import ProduceInput, ProduceOutcome, ProduceRow


def produce(inp: ProduceInput) -> ProduceOutcome:
    """What each rung's fabric yields this season, and the stores each producing rung is credited to."""
    table = dict(inp.table)
    after = dict(inp.larder_after)
    factor = dict(inp.factor)     # `((rung, factor), ...)`: the rung's territory's draw (CL-EVENTS (1)); the same rungs as `stores`
    by_rung: dict = {}        # one pass over the Sites, not one per rung; each rung's list keeps id order
    for _sid, site_kind, site_rung, condition in inp.sites:
        by_rung.setdefault(site_rung, []).append((site_kind, condition))
    rows = []
    for rung, kinds in inp.stores:
        produced: dict = {}
        for site_kind, condition in by_rung.get(rung, ()):
            for k, base in table.get(site_kind) or ():
                produced[k] = produced.get(k, 0) + int(
                    base * (max(0, condition) / inp.scale) * factor[rung])
        produced = {k: v for k, v in produced.items() if v}
        if not produced:
            continue
        held = dict(kinds)
        held.update(after.get(rung, ()))
        credited = tuple((k, held.get(k, 0) + v) for k, v in produced.items())
        rows.append(ProduceRow(rung, tuple(produced.items()), credited))
    return ProduceOutcome(tuple(rows))
