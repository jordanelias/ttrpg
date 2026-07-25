"""mass_battle.percell — per-column density/depth grid, casualty distribution, fatigue,
envelopment-sigma, defender depth, stamina. Behaviour-frozen P-A extract.
Depends on config + geometry."""
import math
from mass_battle.config import *
from mass_battle.geometry import *

__all__ = ['_erode_cell_morale_from_damage', '_apply_with_spill', '_ColBlock', 'build_column_grid', '_engaged_cols', 'distribute_casualties', 'distribute_casualties_cellwise', 'sync_col_grid', '_fatigue_sigma', '_defender_depth', 'update_stamina', 'apply_to_subunit']

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
    """Cell-primary: rebuild the column view from the LIVE cell state — membership, density AND depth
    — carrying each surviving column's fatigue forward.
    [arch: column = emergent view, rebuilt from cells after they change.]

    [ED-MB-0041 Tier-2] Previously this refreshed only `density`, for the columns the grid happened to
    be BUILT with — and `col_grid` is built exactly once, in `Unit.__post_init__`, from the spawn
    footprint. So the column *structure* was frozen at spawn. Any body that wheeled or drifted
    laterally ended up occupying columns absent from its own grid, and then:
      • every live column read density 0 -> `alive()` False -> `_fatigue_sigma` found no blocks at all
        and returned 0.0 (no fatigue, ever, for a manoeuvring body), and
      • `_defender_depth` found no matching columns and returned 0.0 (no depth-based charge absorption).
    Two mechanics that silently switched themselves off for precisely the units doing the interesting
    manoeuvres. Rebuilding membership fixes both.

    `depth` now tracks live ranks too: a column ground down from 5 ranks to 1 no longer claims the
    rotation/absorption of a deep file it no longer has. Stamina and start_density are carried over for
    columns that persist (fatigue is a property of the men in that file, not of the grid object); a
    newly-occupied column starts fresh at full stamina with its current density as its reference."""
    grid = getattr(unit, 'col_grid', None)
    if grid is None:
        return
    bycol = {}
    for a in unit.subunits:
        for _pid, (r, c), troops in a.iter_cells():
            if troops <= 0:
                continue   # an emptied cell is not a live rank: it must not pad the column's depth
            bycol.setdefault(c, []).append(troops)
    prior = {b.col: b for b in grid}
    rebuilt = []
    for c in sorted(bycol):
        col_troops = bycol[c]
        b = prior.get(c)
        if b is None:
            b = _ColBlock(col=c, density=sum(col_troops), depth=len(col_troops))
        else:
            b.density = sum(col_troops)
            b.depth = len(col_troops)
        rebuilt.append(b)
    unit.col_grid = rebuilt

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


def _apply_with_spill(targets, dmg):
    """[ED-MB-0041] SINGLE OWNER of proportional casualty application with overflow spill.

    `targets` is a list of (atom, orig_cell, weight). `dmg` is split across them in proportion to
    `weight`, but a cell that cannot absorb its full share (fewer troops than the share) spills the
    remainder onto the still-living cells instead of silently vanishing.

    Why this exists: the three distributors each open-coded `max(0.0, troops - dmg*(troops/tot))`, which
    DISCARDS any damage beyond what the engaged cells hold. Measured: 5000 damage against a 600-troop
    front had cells absorb 600 and **4400 silently discarded**, while `unit.hp` took the full 5000 — so
    the two ledgers diverge exactly in the annihilation cases (encirclement) that matter most. Only
    `distribute_casualties_cellwise` had the spill loop; `distribute_casualties` and `apply_to_subunit`
    did not. One rule, one implementation.

    Returns the amount actually applied (<= dmg; the shortfall is real — every target was emptied)."""
    remaining = float(dmg)
    for _ in range(8):                      # [canonical: epsilon: bounded spill passes; residual guard 1e-9]
        live = [(a, o, w) for (a, o, w) in targets if a.cell_troops.get(o, 0.0) > 0 and w > 0]
        wtot = sum(w for _a, _o, w in live)
        if remaining <= 1e-9 or not live or wtot <= 0:   # [canonical: epsilon: float residual guard]
            break
        applied = 0.0
        for atom, orig, w in live:
            cur = atom.cell_troops.get(orig, 0.0)
            take = min(cur, remaining * (w / wtot))
            atom.cell_troops[orig] = cur - take
            applied += take
            # [ED-MB-0041 phase 1] Local morale erosion rides on the SINGLE owner of casualty
            # application, so every path that kills men (melee, volley, pursuit, freed-attacker,
            # cellwise facing-weighted) shakes the cells it killed them in -- without any caller
            # having to remember to. Inert when cell morale is unseeded.
            _erode_cell_morale_from_damage(atom, orig, take, cur)
        remaining -= applied
        if applied <= 1e-9:                 # [canonical: epsilon: float residual guard]
            break
    return float(dmg) - remaining


def distribute_casualties(unit, dmg, pairs):
    """Increment 2: apply `dmg` troop-casualties across the unit's ENGAGED front columns,
    proportional to each engaged column's current density. Keeps sum(col densities) == hp:
    the same total `dmg` run_battle subtracts from unit.hp is subtracted here across columns.
    Transparent substrate — does NOT feed back into resolution yet (later increments read this state).

    [D4 fix, 2026-07-05, mass-battle Cannae gauge follow-up audit] The engaged-column filter is now
    computed PER SUBUNIT, not unioned across the whole Unit. The prior whole-unit union let one
    subunit's engaged column leak onto an UNRELATED, unengaged subunit's cells that merely happen to
    share the same absolute column value -- confirmed by direct trace: a wide-placed wheeling wing
    20+ rows from any enemy absorbed a share of the CENTER subunit's casualties purely because its
    column briefly overlapped the center's engaged range. A subunit's own cells now only count as
    engaged against THAT subunit's own contact columns."""
    if dmg <= 0:
        return
    eng_by_sub = {}
    sub_ids = {id(a) for a in unit.subunits}
    for p in pairs:
        aid = id(p.get("atom_a"))
        if aid in sub_ids:
            eng_by_sub.setdefault(aid, set()).update(c for (_r, c) in p.get("a_cells", []))
        bid = id(p.get("atom_b"))
        if bid in sub_ids:
            eng_by_sub.setdefault(bid, set()).update(c for (_r, c) in p.get("b_cells", []))
    # `any_engaged` preserves the original degenerate-fallback semantics: if NOTHING in the whole
    # Unit is in contact this tick (no pairs reference any of its subunits at all), spread dmg over
    # every living cell exactly as before. Once ANYTHING is engaged, a subunit only contributes cells
    # if IT SPECIFICALLY has contact this tick -- an uninvolved subunit contributes nothing, closing
    # the cross-subunit column-leak this fix targets.
    any_engaged = bool(eng_by_sub)
    cells = []   # (subunit, cell_id, troops) over the ENGAGED front
    for a in unit.subunits:
        eng = eng_by_sub.get(id(a))
        for pid, (r, c), troops in a.iter_cells():
            if troops > 0 and (not any_engaged or (eng and c in eng)):
                cells.append((a, pid, troops))
    if not cells:                                  # fallback: spread over all living cells
        for a in unit.subunits:
            for pid, (r, c), troops in a.iter_cells():
                if troops > 0:
                    cells.append((a, pid, troops))
    tot = sum(t for _a, _p, t in cells)
    if tot <= 0:
        return
    # [ED-MB-0041] Route through the shared spill primitive. Was
    # `a.cell_troops[pid] = max(0.0, troops - dmg*(troops/tot))`, which silently discarded any damage
    # exceeding the engaged front's troops while unit.hp took it in full (measured: 4400 of 5000 lost).
    _apply_with_spill([(a, pid, troops) for a, pid, troops in cells], dmg)
    sync_col_grid(unit)                            # refresh emergent column densities from cells

def _erode_cell_morale_from_damage(atom, cid, killed, before):
    """[ED-MB-0041 phase 1] A cell that is being cut down loses heart LOCALLY.

    Scaled by the fraction of THAT CELL destroyed, not by the absolute count: losing 20 of 100 men beside
    you is the same shock whether the body is large or small, and an absolute scale would make dense
    cells look braver purely for being dense. Bounded by the same per-phase cap the aggregate erosion
    uses, so one savage tick cannot instantly zero a cell that the cohesion pull would otherwise recover.
    """
    # getattr, not attribute access: this helper hangs off `_apply_with_spill`, the SINGLE owner of
    # casualty application, which is deliberately duck-typed — callers pass anything with cell_troops
    # (including test doubles). Requiring `cell_morale` on every such object would make a morale feature
    # impose a structural requirement on the damage substrate, which is backwards. CI caught this via
    # test_hp_cell_ledger's _FakeAtom; the lesson is about the coupling, not the double.
    if not getattr(atom, 'cell_morale', None) or killed <= 0 or before <= 0:
        return
    frac = min(1.0, killed / before)
    atom.erode_cell_morale(cid, MORALE_PHASE_CAP * frac)


def distribute_casualties_cellwise(unit, dmg, cell_dmg):
    """[ED-MB-0040, Jordan directive: "the cell is the primitive ... damage is supposed to be done to
    cells ... flank/rear damage is supposed to be cellular"] Apply `dmg` to the unit's CONTACT CELLS using
    the per-cell facing-weighted shares the resolver accumulated (`cell_dmg`: {id(atom): (atom, {abs_cell:
    share})}), instead of `distribute_casualties`' uniform density-proportional spread over every engaged
    cell. The shares are used as RELATIVE WEIGHTS and renormalised to the caller's `dmg`, so the total is
    exactly the resolver's (post-scaled) figure and the cells==hp invariant holds regardless of any
    post-scaling upstream. Effect: a flanked/rear cell loses ~2x what a front-facing sibling in the SAME
    subunit loses, so an enveloped body is stripped shell-inward rather than thinning uniformly.
    Falls back to the aggregate spread when no cellular shares exist (e.g. contact with no live cells)."""
    if dmg <= 0:
        return
    tot = 0.0
    for _k, (_atom, cells) in cell_dmg.items():
        tot += sum(cells.values())
    if tot <= 0:
        return
    # Resolve to (atom, orig_cell, weight) once, then fill in passes so a cell that cannot absorb its
    # full share (it has fewer troops than the share) spills the remainder onto the still-living cells
    # instead of silently vanishing — without this the cells==hp invariant drifts exactly in the
    # annihilation cases (encirclement) this mechanic exists to model.
    targets = []
    for _k, (atom, cells) in cell_dmg.items():
        amap = _oriented_abs_map(atom)
        for abs_cell, share in cells.items():
            orig = amap.get(abs_cell)
            if orig is None or share <= 0:
                continue
            if atom.cell_troops.get(orig, 0.0) > 0:
                targets.append((atom, orig, share))
    _apply_with_spill(targets, dmg)   # [ED-MB-0041] shared primitive — was an inline copy of this loop
    sync_col_grid(unit)


def apply_to_subunit(unit, subunit, dmg):
    """Apply `dmg` troop-casualties to a SINGLE subunit's living cells, proportional to density,
    then refresh the unit's column grid. Used by ORDERED volley fire (build E) to CONCENTRATE
    casualties on a chosen target subunit instead of spreading them across the whole unit. The same
    `dmg` the caller removes from unit.hp for this portion is removed here from the target's cells,
    preserving the cell == hp invariant.
    [canonical: directed/aimed fire concentration -- longbow fire discipline, Crecy/Agincourt;
    mass_battle §A.7 volley targeting.]"""
    if dmg <= 0:
        return
    cells = [(pid, t) for pid, (_r, _c), t in subunit.iter_cells() if t > 0]
    tot = sum(t for _p, t in cells)
    if tot <= 0:
        return
    # [ED-MB-0041] same shared spill primitive — see distribute_casualties.
    _apply_with_spill([(subunit, pid, t) for pid, t in cells], dmg)
    sync_col_grid(unit)


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

# [ED-MB-0036 sweep, 2026-07-24] _envelopment_sigma (Increment 6) REMOVED — it was dormant at
# PC_ENVELOP_SIGMA=0.0 and its unit-level col-grid "wider side" overhang test mis-targeted a split envelop
# army. Superseded by the octagon flank multiplier + multi-side shock (B6) + perimeter/orbital-wheel
# envelopment (ED-MB-0035). Removing the always-zero term is byte-exact (see orchestration.py Increment-6 note).

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
