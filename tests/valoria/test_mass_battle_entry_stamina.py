"""One stamina ledger (`16_PESSIMIST_MB_one_stamina_ledger` step 1): the column ledger
(`percell._ColBlock.stamina`) is the only store, so a per-unit `stamina` / `stamina_max` key on a
`build_army` spec is refused with a message naming `entry_stamina`, not forwarded to a field that is gone."""
import pytest

from modules.mass_battle.armies import build_army
from modules.mass_battle.config import STAMINA_MAX


def _spec(**extra):
    return {'shape': 'Line', 'troop_type': 'infantry', 'unit_type': 'melee', 'width': 3, 'depth': 5, 'troops': 1500.0, **extra}


@pytest.mark.parametrize('key', ['stamina', 'stamina_max'])
def test_a_unit_stamina_spec_key_is_refused(key):
    with pytest.raises(ValueError, match='entry_stamina'):
        build_army([_spec(**{key: 50})], 'A', 'A')
    # control: the same spec without the key builds, and its column ledger starts at the ceiling
    army = build_army([_spec()], 'A', 'A')
    assert army.col_grid and all(b.stamina == STAMINA_MAX for b in army.col_grid)
    assert army.agg_stamina() == STAMINA_MAX


def test_a_spent_column_costs_the_units_standing_in_it_one_die():
    """The exhausted -1 die reads the column ledger (`percell.column_exhausted`): a unit loses one die when the
    lowest live column block it stands in is at 0, and a unit standing in other columns does not."""
    from modules.mass_battle.config import SIDE_A_START_ROW, STAMINA_EXHAUSTED_POOL_PENALTY
    from modules.mass_battle.core.exchange import subunit_combat_pool
    army = build_army([_spec(starting_position=(SIDE_A_START_ROW, 10)),
                       _spec(starting_position=(SIDE_A_START_ROW, 30))], 'A', 'A')
    left, right = army.units
    cols_l, cols_r = ({c for _p, (_r, c), t in u.iter_cells() if t > 0} for u in (left, right))
    assert cols_l and cols_r and not (cols_l & cols_r)
    fresh = (subunit_combat_pool(army, left), subunit_combat_pool(army, right))
    assert fresh[0] > 1 and fresh[1] > 1               # above the floor, so a lost die is visible
    one = min(cols_l)
    for b in army.col_grid:
        if b.col == one:
            b.stamina = 0.0                            # one file of the left unit is spent
    assert subunit_combat_pool(army, left) == fresh[0] + STAMINA_EXHAUSTED_POOL_PENALTY
    assert subunit_combat_pool(army, right) == fresh[1]   # control: the right unit's files are fresh
