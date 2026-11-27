"""B12b.23 -- a second wall adds (`16_PESSIMIST_SE_B` edit 3).

`settlements.fortification` is the complement of the product of each garrison's shortfall, so a settlement's second
garrison never lowers what the first gave it. Read through the composition row the host reaches it by, on the
`FortInput` the projection builds (`queries/world_q.py::fort_input`), at the shipped `condition_scale` of 1000.
"""
from engine.season.queries.inputs import FortInput
from engine.substrate import composition

SCALE = 1000


def _wall(*conditions):
    return composition.require("settlements.fortification")(FortInput(tuple(conditions), SCALE if conditions else None))


def test_second_wall_never_lowers_the_first():
    one, ruined_pair, full_pair = _wall(1000), _wall(1000, 0), _wall(1000, 1000)
    assert (one, ruined_pair, full_pair) == (1.0, 1.0, 1.0)
    assert _wall(400, 0) == _wall(400) == 0.4        # a ruined second garrison leaves the first as it was
    assert _wall(400, 300) > _wall(400)               # a standing second one adds


def test_half_strength_pair_reads_075():
    assert _wall(500, 500) == 0.75


def test_no_garrison_reads_zero():
    assert _wall() == 0.0
