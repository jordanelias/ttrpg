"""A SETTLEMENT'S WALLS -- the `settlements` module's `settlements.fortification` entry (A-25; v9 IN-07 E6).

MODULE ENTRY: reached by the composition row whose target is `fortification` below (`entry: query` -- the
projection wrapper `queries/world_q.py::fortification_of` calls it, and the field adapter
`seam/wrappers/mass_battle.py` calls that wrapper), registered in `manifest.MODULE_ENTRIES` at driver
construction and held there by `manifest/registrar.py::require_entries` against the host's declared need
(`queries/world_q.py::QUERY_ENTRIES`). The host reaches it by role string through
`engine.substrate.composition.require`, as the other settlements queries do.

It takes the host's typed input record and returns a bare `float`, imports the record type and nothing
else, never reads or writes `World`, holds no token and keeps no state.

THE RULE (moved here from `world_q.fortification_of`; `H-38`'s *"`Site.condition` is the model"* applied to
defence): the MEAN garrison condition over the subtree, divided by scale -- `sum / (scale * n)`, the float
expression operand for operand. Several garrisons AVERAGE rather than sum, which keeps the value in
`[0.0, 1.0]`. No garrison is `0.0`: an unfortified settlement, not a refusal.
"""
from __future__ import annotations

from engine.season.queries.inputs import FortInput


def fortification(inp: FortInput) -> float:
    """A settlement's defensive strength, `0.0` to `1.0`."""
    if not inp.conditions:
        return 0.0
    return sum(inp.conditions) / (inp.scale * len(inp.conditions))
