"""HOW A TRAVELLER ARRIVES -- the `settlements` module's road entry (A-25; v12 B12b.08, `16_PESSIMIST_WR_A_the_road_is_drawn` edit 3).

MODULE ENTRY: reached by the composition row whose target is `exposure` below (`entry: step_call` -- a loop step calls it: MATTER,
`loop/matter.py`, once a season, from B12b.11). Registered in `manifest.MODULE_ENTRIES` by the registrar at driver construction and held there by
`manifest/registrar.py::require_entries` against the host's declared need (`loop/matter.py::STEP_CALLS`), so a deleted, stripped or re-kinded
row refuses at construction.

It takes the host's typed input record and returns a typed outcome, and imports the record types and the one roller, nothing else. It never reads or
writes `World`, holds no token and keeps no state between calls. IT DRAWS, and the generator is a parameter in the only form a value record can carry
one (A-30: a draw is a function of its key): each traveller's `draw_key` is the host's keyed draw `(world_seed, tick, pid, "road:<leg index>")`, seeded
through the one constructor (`engine.dice_engine.draw.seeded`), as `modules/combat/fight.py::_mortal_draw` seeds the mortal roll. Nothing of the
scene's stream, nothing between calls.

THE RULE: one roll per traveller, `roll_net_continuous(pool, rng=seeded(draw_key))` against the traveller's declared obstacle, banded by
`degree_from_net` (the one ladder, `seam/ladder.py::degree_of`'s). WHAT A DEGREE COSTS (a body step, a spent traveller, a delay) is the host's:
the module returns the degree and nothing else. A traveller with no row in the input draws nothing: the host puts a journey of no border in none.
"""
from __future__ import annotations

from engine.dice_engine.dice_engine import degree_from_net
from engine.dice_engine.draw import seeded
from engine.dice_engine.sigma_leverage import roll_net_continuous
from engine.season.queries.inputs import RoadInput, RoadOutcome


def exposure(inp: RoadInput) -> RoadOutcome:
    """Each traveller of `inp` takes one keyed draw on the road; `RoadOutcome.rows` is `(pid, degree)` in the input's order."""
    return RoadOutcome(tuple((pid, degree_from_net(roll_net_continuous(pool, rng=seeded(key)), obstacle))
                             for pid, pool, obstacle, key in inp.travellers))
