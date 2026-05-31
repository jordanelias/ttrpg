"""
Per-cell mass-combat resolver (PROTOTYPE — validate standalone, then wire into sim_mb_sigma).

Design (Jordan 2026-05-31, bottom-up + du Picq / depth scholarship):
  - Cells are STATEFUL: each carries a troop density and a stamina. Unit troops = sum of cells.
    Same troops -> few dense cells (packed) OR many sparse cells (spread): the tactical lever.
  - Combat is PER CELL: each contacted front-cell-pair resolves on its own pool
    (min(cell_size, command) + command), roll -> degree -> casualties to that cell.
    Total damage = sum over contacted columns. Frontage scales how many men fight.
  - DEPTH does three jobs via the rear stack (this is what makes depth trade off vs frontage):
      (1) casualty replacement  — rear rank steps forward to refill a thinned front cell;
      (2) fatigue rotation      — a rested rear cell rotates in for a fatigued front cell;
      (3) charge absorption     — each rear rank blunts a charge's penetration; a thin line is punched through.
  - So: wide+shallow = more frontage now, but thins fast, fatigues fast (no rotation),
    and is vulnerable to charges. Narrow+deep = fewer cells fighting, but sustained.

This module owns ONLY the per-cell mechanics. Dice primitives (roll_pool, compute_degree,
DAMAGE_BY_DEGREE) are passed in so we stay faithful to the engine's resolution.
"""
import math
from dataclasses import dataclass, field

BLOCK_SIZE = 100          # troops per size-unit (matches engine)
STAMINA_MAX = 100
# [class-B tunables — validate, then tune]
STAMINA_DRAIN_PER_CLASH = 12     # front cell stamina lost per clash it fights
STAMINA_REST_PER_TICK   = 5     # a rear cell (not fighting) recovers this per tick
ROTATE_STAMINA_FLOOR    = 50    # front cell rotates out below this if a fresher rear cell exists
REFILL_FLOOR_FRAC       = 0.60  # front cell pulls reinforcement below this fraction of its start density


@dataclass
class Cell:
    density: float                 # troops currently in this cell
    start_density: float           # troops at full strength (for refill threshold)
    stamina: float = STAMINA_MAX
    rank: int = 0                  # 0 = front, increasing toward rear

    def size(self):                # troops in size-units
        return self.density / BLOCK_SIZE

    def alive(self):
        return self.density > 0.5


def build_column_stack(frontage, depth, rank_density=100):
    """frontage = front-rank cells (width); depth = ranks deep; rank_density = men per cell.
    Front-rank density is CONSTANT regardless of depth: men stand shoulder-to-shoulder in
    front, and EXTRA men form ranks BEHIND (reserves). So depth does NOT thin the front —
    it adds a reserve queue. Total troops = frontage * depth * rank_density.
    Density (men per front cell) is a separate tactical lever from depth."""
    cols = []
    for _c in range(frontage):
        stack = [Cell(density=rank_density, start_density=rank_density, rank=r) for r in range(depth)]
        cols.append(stack)
    return cols


def _stam_pen(stamina):
    return 0  # fatigue now enters as a delta-sigma (stamina_sigma), uniform impact


def cell_pool(cell, command):
    """Per-cell pool — the engine's formula applied to ONE cell:
       min(cell_size, command) + command, with a small stamina penalty."""
    raw = min(cell.size(), command) + command + _stam_pen(cell.stamina)
    return max(1, math.floor(raw))


def front_clash(front_a, front_b, cmd_a, cmd_b, pow_a, pow_b, dr_a, dr_b,
                ns_a, ns_b, dice):
    """Resolve ONE contacted front-cell pair. dice = (roll_pool, compute_degree,
    DAMAGE_BY_DEGREE, sigma_net_boost). ns_a/ns_b = delta-sigma for this pair
    (facing/charge/morale). Returns (dmg_to_a, dmg_to_b) as troop casualties.
    Mutates nothing — caller applies casualties + stamina."""
    roll_pool, compute_degree, DAMAGE_BY_DEGREE, sigma_net_boost = dice
    pa = cell_pool(front_a, cmd_a)
    pb = cell_pool(front_b, cmd_b)
    a_net = roll_pool(pa) + sigma_net_boost(ns_a, pa)
    b_net = roll_pool(pb) + sigma_net_boost(ns_b, pb)
    a_deg = compute_degree(a_net, max(1, b_net))
    b_deg = compute_degree(b_net, max(1, a_net))
    dmg_to_a = max(0.0, DAMAGE_BY_DEGREE[b_deg](pow_b) - dr_a)
    dmg_to_b = max(0.0, DAMAGE_BY_DEGREE[a_deg](pow_a) - dr_b)
    return dmg_to_a, dmg_to_b


# ─── INCREMENT 2: column tick (depth = refill + rotation + rest) ──────────────
@dataclass
class Combatant:
    cols: list            # list[column]; column = list[Cell] front->rear
    command: int
    power: int
    dr: int
    name: str = ""
    charge_pen: int = 0   # >0 = charging this turn with this penetration depth (cavalry/wedge shock)

def _front_idx(col):
    for i, c in enumerate(col):
        if c.alive():
            return i
    return None

def _rest_rear(col, front_i):
    for i, c in enumerate(col):
        if i != front_i and c.alive():
            c.stamina = min(STAMINA_MAX, c.stamina + STAMINA_REST_PER_TICK)

def _refill(col, front_i):
    """Rear rank steps forward: if the front cell is below REFILL_FLOOR_FRAC of its
    start density, pull troops forward from the next alive rear cell."""
    f = col[front_i]
    if f.density >= REFILL_FLOOR_FRAC * f.start_density:
        return
    need = f.start_density - f.density
    for j in range(front_i + 1, len(col)):
        r = col[j]
        if not r.alive():
            continue
        take = min(need, r.density)
        f.density += take
        r.density -= take
        need -= take
        if need <= 0.5:
            break

def _rotate(col, front_i):
    """Fatigue rotation: if the front cell is winded and a fresher rear cell exists,
    swap them (fresh men step to the front). Shallow columns have no one to rotate."""
    f = col[front_i]
    if f.stamina >= ROTATE_STAMINA_FLOOR:
        return
    best_j, best_stam = None, f.stamina + 15  # require meaningfully fresher
    for j in range(front_i + 1, len(col)):
        r = col[j]
        if r.alive() and r.stamina > best_stam:
            best_j, best_stam = j, r.stamina
    if best_j is not None:
        col[front_i], col[best_j] = col[best_j], col[front_i]

def tick_column(col_a, col_b, A, B, ns_a, ns_b, dice, cscale):
    """One tick on a single contested column pair. Mutates the columns.
    Returns (troop_casualties_to_A, troop_casualties_to_B) on this column."""
    ia, ib = _front_idx(col_a), _front_idx(col_b)
    if ia is None or ib is None:
        return 0.0, 0.0
    fa, fb = col_a[ia], col_b[ib]
    ns_a = ns_a + stamina_sigma(fa.stamina)   # tired front fights worse
    ns_b = ns_b + stamina_sigma(fb.stamina)
    dmg_a, dmg_b = front_clash(fa, fb, A.command, B.command, A.power, B.power,
                               A.dr, B.dr, ns_a, ns_b, dice)
    cas_a = cscale * dmg_a
    cas_b = cscale * dmg_b
    fa.density = max(0.0, fa.density - cas_a)
    fb.density = max(0.0, fb.density - cas_b)
    fa.stamina = max(0.0, fa.stamina - STAMINA_DRAIN_PER_CLASH)
    fb.stamina = max(0.0, fb.stamina - STAMINA_DRAIN_PER_CLASH)
    _rest_rear(col_a, ia); _rest_rear(col_b, ib)
    _refill(col_a, ia);    _refill(col_b, ib)
    _rotate(col_a, ia);    _rotate(col_b, ib)
    return cas_a, cas_b

def col_troops(col):
    return sum(c.density for c in col if c.alive())

def _living_depth(col):
    return sum(1 for c in col if c.alive())


# ─── INCREMENT 3: multi-column battle (frontage overhang -> flank; depth counters) ──
SIGMA_PER_D = 0.2                 # delta-sigma per die-equivalent (matches engine)
FLANK_CAP   = 3                   # max overhang columns that count toward flanking
ROUT_TROOP_FRAC = 0.45            # prototype rout: side breaks below this fraction of start troops
STAM_SIGMA_SCALE  = 1.5           # fatigue -> delta-sigma: a winded front fights worse (shallow can't rotate fresh men in)
FLANK_DEPTH_RESIST = 0.6          # depth refuses flanks: each rank of the flanked side blunts the overhang flank penalty
CHARGE_SIGMA = 0.55              # per-rank-of-unabsorbed-penetration delta-sigma the charger gets on impact
CHARGE_IMPACT_TICKS = 3          # a charge is a brief shock: bonus only for the first few ticks of contact
ENVELOP_SIGMA = 0.5              # delta-sigma an overhang column gets attacking an enemy flank (blunted by that flank column depth)
FRONT_RANKS_NEEDED = 2           # ranks a column must keep on its front; deeper ranks are free to reform to a flank

def stamina_sigma(stamina):
    frac = max(0.0, min(1.0, stamina / STAMINA_MAX))
    return STAM_SIGMA_SCALE * (frac - 1.0)

def _center_slice(cols, k):
    """Return indices of the centered k columns of `cols`."""
    n = len(cols)
    start = (n - k) // 2
    return list(range(start, start + k))

def battle(A, B, dice, cscale, max_ticks=300, verbose=False):
    """Equal-or-unequal frontage battle. Contested columns pair head-to-head, centered.
    The wider side's overhang flanks the narrower side's OUTER contested columns
    (a defensive delta-sigma penalty there). Depth (refill/rotation) is the counter.
    Returns dict(winner, ticks, a_frac, b_frac)."""
    fa, fb = len(A.cols), len(B.cols)
    contested = min(fa, fb)
    ia = _center_slice(A.cols, contested)
    ib = _center_slice(B.cols, contested)
    overhang = abs(fa - fb)
    flanked_side = 'B' if fa > fb else ('A' if fb > fa else None)
    flank_sig = -min(FLANK_CAP, overhang) * SIGMA_PER_D
    n_flank_cols = min(contested, max(1, min(FLANK_CAP, overhang)))  # outer cols that get flanked

    start_a = sum(col_troops(c) for c in A.cols)
    start_b = sum(col_troops(c) for c in B.cols)

    def flank_ns(side, pos):
        if flanked_side != side:
            return 0.0
        from_end = min(pos, contested - 1 - pos)
        if from_end >= n_flank_cols:
            return 0.0
        col = A.cols[ia[pos]] if side == "A" else B.cols[ib[pos]]
        depth = len(col)
        return flank_sig / (1.0 + FLANK_DEPTH_RESIST * (depth - 1))

    wide = A if len(A.cols) > len(B.cols) else (B if len(B.cols) > len(A.cols) else None)
    if wide is not None:
        narrow = B if wide is A else A
        w_contested = ia if wide is A else ib
        w_overhang = [i for i in range(len(wide.cols)) if i not in w_contested]
        n_contested = ib if narrow is B else ia
    for t in range(1, max_ticks + 1):
        charging = t <= CHARGE_IMPACT_TICKS
        for pos in range(contested):
            ca, cb = A.cols[ia[pos]], B.cols[ib[pos]]
            ns_a = ns_b = 0.0
            if charging and A.charge_pen > 0:
                ns_a += CHARGE_SIGMA * max(0, A.charge_pen - _living_depth(cb))   # B's depth absorbs the charge
            if charging and B.charge_pen > 0:
                ns_b += CHARGE_SIGMA * max(0, B.charge_pen - _living_depth(ca))
            tick_column(ca, cb, A, B, ns_a, ns_b, dice, cscale)
        # ENVELOPMENT: overhang columns wheel into the narrow side's flanks (real clashes,
        # exposed troops, flank bonus blunted by the flanked column's depth)
        if wide is not None and w_overhang and n_contested:
            narrow_min_depth = min(_living_depth(narrow.cols[i]) for i in n_contested)
            reform_capacity = max(0, narrow_min_depth - FRONT_RANKS_NEEDED)  # reserve ranks free to reform to the flank
            for k, oc in enumerate(w_overhang):
                fpos = n_contested[0] if k % 2 == 0 else n_contested[-1]
                ocol = wide.cols[oc]; fcol = narrow.cols[fpos]
                if _front_idx(ocol) is None or _front_idx(fcol) is None:
                    continue
                if k < reform_capacity:
                    env = 0.0   # refused: deep side reformed reserves to meet this enveloper evenly
                else:
                    env = ENVELOP_SIGMA / (1.0 + FLANK_DEPTH_RESIST * (_living_depth(fcol) - 1))
                if wide is A:
                    tick_column(ocol, fcol, A, B, env, 0.0, dice, cscale)
                else:
                    tick_column(fcol, ocol, A, B, 0.0, env, dice, cscale)
        ta = sum(col_troops(c) for c in A.cols)
        tb = sum(col_troops(c) for c in B.cols)
        a_break = ta < ROUT_TROOP_FRAC * start_a
        b_break = tb < ROUT_TROOP_FRAC * start_b
        if a_break or b_break:
            winner = 'B' if a_break and not b_break else ('A' if b_break and not a_break else 'draw')
            return dict(winner=winner, ticks=t, a_frac=ta/start_a, b_frac=tb/start_b)
    ta = sum(col_troops(c) for c in A.cols); tb = sum(col_troops(c) for c in B.cols)
    return dict(winner='draw', ticks=max_ticks, a_frac=ta/start_a, b_frac=tb/start_b)
