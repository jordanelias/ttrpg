"""modules.mass_battle.core.attrition -- the frontage of a contact, in men (`engaged_files`).

The one owner of "how many of a body's men are in the front facing this contact" (MBA §1.1 `frontage`, B19.12): the contact draw
reads it as `F`, the men a contact's felling chance applies to. It re-states the retired `_lanchester_strength` (engaged columns times
body-average density over two reference constants, a pool-scale strength) as men, and adds the pair rule's edit 4: a contact cell in
`m` of this tick's pairs counts `1 / m` of its men in each (`16_PESSIMIST_MB_partition_and_the_pair_rule`). Pure: duck-typed atom
attributes and the geometry's abs-to-orig map only; no up-DAG import (no cycle)."""
from modules.mass_battle.geometry import _oriented_abs_map

__all__ = ['engaged_files']


def engaged_files(contact_cells, atom, front_width=None, shares=None):
    """The men of `atom`'s front facing this contact: the sum, over its distinct contact cells, of the men in the cell (`cell_troops`,
    read live, so a hollowed cell counts what it holds) times `1 / m`, `m` the number of this tick's pairs the cell is in (`shares`:
    `{abs cell: m}`, absent or None meaning 1). Every man of a contact cell is in its front (the tree's cell is one rank of the lattice;
    the retired owner's "all-fight" reading).

    [ED-MB-0013] `front_width`: the CONTINUOUS engaged width from the OBB front-overlap (`geometry.engaged_frontage`), recorded on the
    FIELD_MOVEMENT contact path. When given it replaces the distinct-cell count: the men are `front_width` x the mean men of a contact
    cell x the mean share of the contact cells (edit 4's continuous form). None (the grid path) counts cells. `<= 0` is no contact."""
    cells = sorted(set(contact_cells))
    if not cells or (front_width is not None and front_width <= 0.0):
        return 0.0
    shares = shares or {}
    amap = _oriented_abs_map(atom)
    troops = getattr(atom, 'cell_troops', None) or {}
    men = [max(troops.get(amap.get(c), 0.0), 0.0) for c in cells]
    weight = [1.0 / max(shares.get(c, 1), 1) for c in cells]
    if front_width is None:
        return sum(m * w for m, w in zip(men, weight))
    return front_width * (sum(men) / len(men)) * (sum(weight) / len(weight))
