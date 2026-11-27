"""A SETTLEMENT'S WALLS -- the `settlements` module's `settlements.fortification` entry (A-25; v9 IN-07 E6).

MODULE ENTRY: reached by the composition row whose target is `fortification` below (`entry: query` -- the
projection wrapper `queries/world_q.py::fortification_of` calls it, and the field adapter
`seam/wrappers/mass_battle.py` calls that wrapper), registered in `manifest.MODULE_ENTRIES` at driver
construction and held there by `manifest/registrar.py::require_entries` against the host's declared need
(`queries/world_q.py::QUERY_ENTRIES`). The host reaches it by role string through
`engine.substrate.composition.require`, as the other settlements queries do.

It takes the host's typed input record and returns a bare `float`, imports the record type and nothing
else, never reads or writes `World`, holds no token and keeps no state.

THE RULE (`H-38`'s *"`Site.condition` is the model"* applied to defence): each garrison's shortfall is `1 - condition / scale`
(the condition clamped to `[0, scale]`); the settlement's strength is `1 - product(shortfalls)`. Several garrisons ADD in
that sense and never lower one another, and the value stays in `[0.0, 1.0]`. No garrison is `0.0`: an unfortified settlement,
not a refusal.
"""
from __future__ import annotations

from engine.season.queries.inputs import FortInput


def fortification(inp: FortInput) -> float:
    """A settlement's defensive strength, `0.0` to `1.0`: the complement of the product of each
    garrison's shortfall, so a second wall never weakens the first."""
    breach = 1.0
    for c in inp.conditions:
        breach *= 1.0 - max(0, min(c, inp.scale)) / inp.scale
    return 1.0 - breach
