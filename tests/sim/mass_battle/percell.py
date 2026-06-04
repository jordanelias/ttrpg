"""mass_battle.percell — per-column density/depth grid, casualty distribution, fatigue,
envelopment-sigma, defender depth, stamina. Behaviour-frozen P-A extract.
Depends on config + geometry."""
import math
from mass_battle.config import *
from mass_battle.geometry import *

__all__ = ['_ColBlock', 'build_column_grid', '_engaged_cols', 'distribute_casualties', 'sync_col_grid', '_fatigue_sigma', '_envelopment_sigma', '_defender_depth', 'update_stamina']

class _ColBlock:
    """One file/column of a unit's formation: a depleting troop density + stamina + depth (rank count).
    Depth is the reserve queue (refill + fatigue rotation + flank-refusal in later increments)."""
    __slots__ = ('col', 'density', 'start_density', 'stamina', 'depth')
    def __init__(self, col, density, depth):
        self.col = col
        self.density = float(density)
        self.start_density = float(density)
        self.stamina = float(STAMINA_MAX)
        self.depth = int(depth)
    def size(self):
        return self.density / BLOCK_SIZE
    def alive(self):
        return self.density > 0.5

def build_column_grid(unit):
    """Derive a per-column block grid from the unit's CURRENT cell footprint (continuous-sigma granularity).
    frontage = distinct columns; per column: troops = (#cells in column) * troops/cell; depth = #ranks.
    Returns list[_ColBlock] ordered left->right. State only — resolution wires in at Increment 2."""
    bycol = {}
    for a in unit.subunits:
        for _pid, (r, c), troops in a.iter_cells():
            bycol.setdefault(c, []).append(troops)
    if not bycol:
        return []
    grid = []
    for c in sorted(bycol):
        col_troops = bycol[c]
        grid.append(_ColBlock(col=c, density=sum(col_troops), depth=len(col_troops)))
    return grid

def sync_col_grid(unit):
    """Cell-primary (step 1): refresh each column's density (= Sum of its cells' troops) from the
    cell state, preserving stamina/start_density. depth (structural) is left as built.
    [arch: column = emergent view, rebuilt from cells after they change.]"""
    grid = getattr(unit, 'col_grid', None)
    if not grid:
        return
    bycol = {}
    for a in unit.subunits:
        for _pid, (r, c), troops in a.iter_cells():
            bycol[c] = bycol.get(c, 0.0) + troops
    for b in grid:
        b.density = bycol.get(b.col, 0.0)

def _engaged_cols(unit, pairs):
    """Absolute columns of `unit` that are in contact this tick (from find_contacts pairs)."""
    cols = set()
    sub_ids = {id(a) for a in unit.subunits}
    for p in pairs:
        if id(p.get("atom_a")) in sub_ids:
            cols.update(c for (r, c) in p.get("a_cells", []))
        if id(p.get("atom_b")) in sub_ids:
            cols.update(c for (r, c) in p.get("b_cells", []))
    return cols

def distribute_casualties(unit, dmg, pairs):
    """Increment 2: apply `dmg` troop-casualties across the unit's ENGAGED front columns,
    proportional to each engaged column's current density. Keeps sum(col densities) == hp:
    the same total `dmg` run_battle subtracts from unit.hp is subtracted here across columns.
    Transparent substrate — does NOT feed back into resolution yet (later increments read this state)."""
    if dmg <= 0:
        return
    eng = _engaged_cols(unit, pairs)
    cells = []   # (subunit, cell_id, troops) over the ENGAGED front
    for a in unit.subunits:
        for pid, (r, c), troops in a.iter_cells():
            if troops > 0 and (not eng or c in eng):
                cells.append((a, pid, troops))
    if not cells:                                  # fallback: spread over all living cells
        for a in unit.subunits:
            for pid, (r, c), troops in a.iter_cells():
                if troops > 0:
                    cells.append((a, pid, troops))
    tot = sum(t for _a, _p, t in cells)
    if tot <= 0:
        return
    for a, pid, troops in cells:                   # proportional per cell (assoc.-equiv to the per-column spread)
        a.cell_troops[pid] = max(0.0, troops - dmg * (troops / tot))
    sync_col_grid(unit)                            # refresh emergent column densities from cells

def _fatigue_sigma(unit, engaged_cols):
    """Increment 3: fatigue of the engaged front as a delta-sigma. 0 at full stamina, down to
    -PC_STAM_SIGMA as the fighting columns tire. Density-weighted over the engaged columns.
    [historical anchor: du Picq — a tiring front loses combat effectiveness; depth that can
     rotate fresh ranks forward sustains it, a thin line that cannot rotate wears out.]"""
    grid = getattr(unit, 'col_grid', None)
    if not grid:
        return 0.0
    blocks = [b for b in grid if b.col in engaged_cols and b.alive()]
    if not blocks:
        blocks = [b for b in grid if b.alive()]
    tot = sum(b.density for b in blocks)
    if tot <= 0:
        return 0.0
    frac = sum((b.stamina / STAMINA_MAX) * b.density for b in blocks) / tot
    return PC_STAM_SIGMA * (frac - 1.0)

def _envelopment_sigma(wide_unit, narrow_unit):
    """Increment 6: the wider formation's overhang wheels into the narrow side's flanks (a delta-sigma
    advantage to the WIDER side), but the narrow side's RESERVE DEPTH refuses it — reserve ranks beyond
    PC_FRONT_RANKS reform to meet each enveloper evenly. Returns (sigma_to_wide, sigma_to_narrow_penalty=0).
    [historical anchor: envelopment (Cannae) vs a deep formation refusing/bending its flank.]"""
    wg = getattr(wide_unit, 'col_grid', None)
    ng = getattr(narrow_unit, 'col_grid', None)
    if not wg or not ng:
        return 0.0
    w_cols = sum(1 for b in wg if b.alive())
    n_cols = sum(1 for b in ng if b.alive())
    overhang = w_cols - n_cols
    if overhang <= 0:
        return 0.0
    overhang = min(overhang, PC_FLANK_CAP)
    # narrow side's reserve depth available to reform to the flanks
    n_min_depth = min((b.depth for b in ng if b.alive()), default=1)
    reform_capacity = max(0, n_min_depth - PC_FRONT_RANKS)
    enveloping = max(0, overhang - reform_capacity)        # overhang columns NOT refused by depth
    if enveloping <= 0:
        return 0.0
    return PC_ENVELOP_SIGMA * enveloping

def _defender_depth(unit, contact_cells):
    """Increment 5: representative depth of the defender's engaged columns (charge absorption).
    Deeper columns absorb more of a charge's penetration."""
    grid = getattr(unit, 'col_grid', None)
    if not grid:
        return 0.0
    cols = set(c for r, c in contact_cells)
    blocks = [b for b in grid if b.col in cols and b.alive()]
    if not blocks:
        return 0.0
    return sum(b.depth for b in blocks) / len(blocks)

def update_stamina(unit, pairs):
    """Increment 3: drain stamina of engaged columns (damped by depth — deeper rotates fresh
    ranks forward, so it tires slower), rest non-engaged columns. Depth is the fatigue counter."""
    grid = getattr(unit, 'col_grid', None)
    if not grid:
        return
    eng = _engaged_cols(unit, pairs)
    joined = len(eng) > 0
    for b in grid:
        if not b.alive():
            continue
        if b.col in eng:
            drain = PC_STAMINA_DRAIN / (1.0 + PC_DEPTH_ROTATE * (b.depth - 1))  # deeper -> slower drain
            b.stamina = max(0.0, b.stamina - drain)
        else:
            # Only GENUINE reserves recover: a column not adjacent to any engaged column (truly behind the
            # fighting), and only while battle is joined. A front-line column momentarily out of this tick's
            # contact set is NOT a reserve and must not spuriously heal (which masked front fatigue).
            adjacent_to_front = any(abs(b.col - ec) <= 1 for ec in eng)
            if joined and not adjacent_to_front:
                b.stamina = min(float(STAMINA_MAX), b.stamina + PC_STAMINA_REST)
