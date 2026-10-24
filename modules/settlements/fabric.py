"""A FABRIC'S BOUND AND SHARE -- the `settlements` module's `settlements.fabric` entry (A-25; v9 IN-07 E5).

MODULE ENTRY: reached by the composition row whose target is `fabric` below (`entry: query` -- the
projection wrappers `queries/world_q.py::ceiling` and `share` call it), registered in
`manifest.MODULE_ENTRIES` at driver construction and held there by `manifest/registrar.py::require_entries`
against the host's declared need (`queries/world_q.py::QUERY_ENTRIES`). The host reaches it by role string
through `engine.substrate.composition.require`, as the other settlements queries do.

It takes the host's typed input record and returns a typed output record, imports the record types and
nothing else, never reads or writes `World`, holds no token and keeps no state. `works_for` and
`matured_terms` (a Record/hold scan and a log scan), the two-live-works `Forbidden` (a store-integrity
backstop against hand-built worlds, design A6), `loop/resolve.py`'s clamp and `_rise`'s headroom
arithmetic (fold and effect bodies) stay host.

THE RULE (moved here from `world_q.ceiling` and `world_q.share`; unchanged clause for clause):
  * CEILING (r2 `04` §A.6.3): the full `scale` when no live works names the site or it declares no
    terms; otherwise `scale * min(matured, declared) // declared` -- MULTIPLY FIRST, DIVIDE LAST, so a
    2-of-3 works reads 666 and not 0; `min` keeps the ratio total if the declared list shrank below what
    the log saw ripen. A bound on the rise, never a cut (the fold's clamp says so).
  * SHARE (r2 `04` §A.6.4, RULED): `(1, max(1, present))` -- one over the persons at the rung, floored at
    one so a fabric nobody stands at is not divided by zero.
  * A half whose inputs are `None` was not projected and is answered `None`.
"""
from __future__ import annotations

from engine.season.queries.inputs import Fabric, FabricInput


def fabric(inp: FabricInput) -> Fabric:
    """The fabric's ceiling and the commons' share, each from its own half of the record."""
    ceiling = None
    if inp.live_works is not None:
        if not inp.live_works or inp.declared == 0:
            ceiling = inp.scale
        else:
            ceiling = inp.scale * min(inp.matured, inp.declared) // inp.declared
    share = None if inp.present is None else (1, max(1, inp.present))
    return Fabric(ceiling, share)
