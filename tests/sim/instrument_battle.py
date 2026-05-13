#!/usr/bin/env python3
# [canonical: tests/sim/ — project versioning convention: SIM-MB nn vNN]
"""Tick-by-tick instrumented battle recorder for the mass-battle simulator.

Produces a granular per-tick markdown record of an entire battle:
  - Unit state (hp, size, morale, discipline, stance, broken/routed) before and after
  - Subunit per-cell state (abs position, speed, facing vector, halted, target)
  - Volley phase (rolls, damage, targets)
  - Movement phase (which cells moved, where, raw vectors)
  - Cross-side contention firings (positions, winners, reverts)
  - Contact pairs (which cells in contact, columns)
  - Engagement pool composition (base, troops_frac, engage_frac, off_mod, angle_mod, final pool, dice, hits)
  - Phase boundary markers (every TICKS_PER_PHASE ticks)

Used for intensive audit against historical precedents — provides the data
needed to compare sim mechanics against renaissance-pre-firearms and earlier
combat at the tick level.

Output: markdown file at OUTPUT_PATH. One file per battle.
"""

import sys, random, math, os, copy, io
sys.path.insert(0, '/home/claude')
import sim_mb_06_v14 as sim


def fmt_cell(orig_r, orig_c, abs_r, abs_c, speed, facing, halted, in_pre=False):
    """Compact cell description: orig→abs, speed, facing, flags."""
    flags = []
    if halted: flags.append("HALT")
    if in_pre: flags.append("PRE")
    flag_str = f" [{','.join(flags)}]" if flags else ""
    return f"({orig_r},{orig_c})→({abs_r},{abs_c}) sp={speed} f=({facing[0]:+d},{facing[1]:+d}){flag_str}"


def cell_snapshot(atom):
    """Snapshot every cell in a subunit's current state."""
    op = sim.oriented_pattern(atom.shape, atom.tier, atom.advance_dir)
    cells = []
    for orig_r, orig_c, or_r, or_c in op:
        abs_r = (atom.starting_position[0] + or_r
                 + atom.cell_offsets.get((orig_r, orig_c), 0) * atom.advance_dir)
        abs_c = (atom.starting_position[1] + or_c
                 + atom.cell_offsets_c.get((orig_r, orig_c), 0))
        speed = sim.cell_speed(atom.shape, atom.tier, orig_r, orig_c)
        last_speed = atom.cell_last_speed.get((orig_r, orig_c), 0)
        facing = atom.cell_facing_vec.get((orig_r, orig_c), (atom.advance_dir, 0))
        halted = (orig_r, orig_c) in atom.halted_cells
        cells.append({
            'orig': (orig_r, orig_c),
            'abs': (abs_r, abs_c),
            'speed_base': speed,
            'speed_last': last_speed,
            'facing': facing,
            'halted': halted,
        })
    return cells


def unit_summary(unit, name):
    return (f"{name}: hp={unit.hp}/{unit.hp_max}, sz={unit.size}/{unit.size_max}, "
            f"morale={unit.morale}/{unit.morale_start}, disc={unit.discipline}, "
            f"cmd={unit.command}, h/sz={unit.h_per_size}, "
            f"stance={unit.stance}, broken={unit.broken}, routed={unit.routed}")


# [canonical: grid display window — covers SIDE_A_START_ROW + footprint and SIDE_B_START_ROW + footprint plus margin]
def render_grid(unit_a, unit_b, row_range=(3, 22), col_range=(5, 18)):
    """ASCII grid showing all cells. A=red letters, B=blue, overlap=#."""
    grid = {}
    for atom in unit_a.subunits:
        for c in atom.cells():
            grid[c] = grid.get(c, '.') 
            grid[c] = 'A' if grid[c] in ('.', 'A') else '#'
    for atom in unit_b.subunits:
        for c in atom.cells():
            if c in grid and grid[c] == 'A':
                grid[c] = '#'  # overlap
            else:
                grid[c] = 'B'
    lines = []
    lines.append(f"    " + " ".join(f"{c:2d}" for c in range(col_range[0], col_range[1])))
    for r in range(row_range[0], row_range[1]):
        row_str = f"r{r:2d} "
        for c in range(col_range[0], col_range[1]):
            row_str += f" {grid.get((r,c), '.')} "
        lines.append(row_str)
    return "\n".join(lines)


def record_battle(unit_a, unit_b, seed, max_turns=15, output_path=None):
    """Run a battle with full instrumentation. Returns markdown string and result dict."""
    random.seed(seed)
    
    out = io.StringIO()
    p = lambda *args: print(*args, file=out)
    
    p(f"# SIM-MB-06 Tick-by-Tick Record")
    p(f"")
    p(f"**Seed:** {seed}  **Max turns:** {max_turns}  **TICKS_PER_PHASE:** {sim.TICKS_PER_PHASE}")
    p(f"")
    p(f"## Initial state")
    p(f"")
    p(f"- {unit_summary(unit_a, 'A')}")
    p(f"  - subunit: shape={unit_a.subunits[0].shape}, tier={unit_a.subunits[0].tier}, "
      f"start={unit_a.subunits[0].starting_position}, advance_dir={unit_a.subunits[0].advance_dir}, "
      f"unit_type={unit_a.subunits[0].unit_type}")
    p(f"- {unit_summary(unit_b, 'B')}")
    p(f"  - subunit: shape={unit_b.subunits[0].shape}, tier={unit_b.subunits[0].tier}, "
      f"start={unit_b.subunits[0].starting_position}, advance_dir={unit_b.subunits[0].advance_dir}, "
      f"unit_type={unit_b.subunits[0].unit_type}")
    p(f"")
    p(f"### Initial grid")
    p(f"```")
    p(render_grid(unit_a, unit_b))
    p(f"```")
    p(f"")
    
    turns = 0
    current_phase = 0
    
    for t in range(1, max_turns + 1):
        turns = t
        tick_in_phase = ((t - 1) % sim.TICKS_PER_PHASE) + 1
        
        p(f"---")
        p(f"")
        p(f"## Tick {t} — Phase {current_phase + 1}, Tick-in-phase {tick_in_phase}")
        p(f"")
        
        if unit_a.routed or unit_b.routed:
            p(f"**Battle ended:** A.routed={unit_a.routed}, B.routed={unit_b.routed}")
            break
        
        # ── PRE-TICK STATE ────────────────────────────────────────────────
        hp_a_pre, sz_a_pre, mor_a_pre = unit_a.hp, unit_a.size, unit_a.morale
        hp_b_pre, sz_b_pre, mor_b_pre = unit_b.hp, unit_b.size, unit_b.morale
        p(f"### State at tick start")
        p(f"- {unit_summary(unit_a, 'A')}")
        p(f"- {unit_summary(unit_b, 'B')}")
        p(f"")
        
        # ── A cells ─────────────────────────────────────────────────────
        p(f"### A cells (pre-movement)")
        p(f"```")
        for c in cell_snapshot(unit_a.subunits[0]):
            p(f"  {fmt_cell(c['orig'][0], c['orig'][1], c['abs'][0], c['abs'][1], c['speed_last'], c['facing'], c['halted'])}")
        p(f"```")
        p(f"")
        p(f"### B cells (pre-movement)")
        p(f"```")
        for c in cell_snapshot(unit_b.subunits[0]):
            p(f"  {fmt_cell(c['orig'][0], c['orig'][1], c['abs'][0], c['abs'][1], c['speed_last'], c['facing'], c['halted'])}")
        p(f"```")
        p(f"")
        
        # ── VOLLEY PHASE ─────────────────────────────────────────────────
        vol = sim.volley_phase(unit_a, unit_b)
        volley_dmg_a = vol["loss_a"]
        volley_dmg_b = vol["loss_b"]
        if volley_dmg_a or volley_dmg_b:
            p(f"### Volley phase")
            p(f"- A volley damage pending: {volley_dmg_a}")
            p(f"- B volley damage pending: {volley_dmg_b}")
            p(f"")
        
        # ── PRE-MOVEMENT CONTACTS / HALT ────────────────────────────────
        pre_pairs = sim.find_contacts(unit_a, unit_b)
        for atom in unit_a.subunits + unit_b.subunits:
            atom.halted_cells = set()
        for pair in pre_pairs:
            op_a = sim.oriented_pattern(pair["atom_a"].shape, pair["atom_a"].tier, pair["atom_a"].advance_dir)
            for cell in pair["a_cells"]:
                for orig_r, orig_c, or_r, or_c in op_a:
                    abs_r = (pair["atom_a"].starting_position[0] + or_r
                             + pair["atom_a"].cell_offsets.get((orig_r, orig_c), 0) * pair["atom_a"].advance_dir)
                    abs_c = (pair["atom_a"].starting_position[1] + or_c
                             + pair["atom_a"].cell_offsets_c.get((orig_r, orig_c), 0))
                    if (abs_r, abs_c) == cell:
                        pair["atom_a"].halted_cells.add((orig_r, orig_c)); break
            op_b = sim.oriented_pattern(pair["atom_b"].shape, pair["atom_b"].tier, pair["atom_b"].advance_dir)
            for cell in pair["b_cells"]:
                for orig_r, orig_c, or_r, or_c in op_b:
                    abs_r = (pair["atom_b"].starting_position[0] + or_r
                             + pair["atom_b"].cell_offsets.get((orig_r, orig_c), 0) * pair["atom_b"].advance_dir)
                    abs_c = (pair["atom_b"].starting_position[1] + or_c
                             + pair["atom_b"].cell_offsets_c.get((orig_r, orig_c), 0))
                    if (abs_r, abs_c) == cell:
                        pair["atom_b"].halted_cells.add((orig_r, orig_c)); break
        
        p(f"### Pre-movement contacts (halt source)")
        p(f"- {len(pre_pairs)} contact pair(s)")
        for i, pair in enumerate(pre_pairs):
            p(f"  - pair {i}: A halted cells={sorted(pair['atom_a'].halted_cells)}, "
              f"B halted cells={sorted(pair['atom_b'].halted_cells)}, cols={sorted(pair['cols'])}")
        p(f"")
        
        # ── TARGET ASSIGNMENT ────────────────────────────────────────────
        sim.assign_targets(unit_a, unit_b)
        a_target = unit_a.subunits[0].target_atom
        b_target = unit_b.subunits[0].target_atom
        p(f"### Target assignment")
        p(f"- A targets: {b_target.shape if a_target else None}, centroid={a_target.centroid() if a_target else None}")
        p(f"- B targets: {a_target.shape if b_target else None}, centroid={b_target.centroid() if b_target else None}")
        p(f"")
        
        # ── ADVANCE ─────────────────────────────────────────────────────
        b_cells_set = set(c for sub in unit_b.subunits for c in sub.cells())
        a_cells_set = set(c for sub in unit_a.subunits for c in sub.cells())
        # Snapshot positions BEFORE advance
        a_before = {c['orig']: c['abs'] for c in cell_snapshot(unit_a.subunits[0])}
        b_before = {c['orig']: c['abs'] for c in cell_snapshot(unit_b.subunits[0])}
        for atom in unit_a.subunits:
            if atom.target_atom:
                atom.advance_cells(unit_a.discipline, atom.target_atom.centroid(), enemy_cells=b_cells_set)
        for atom in unit_b.subunits:
            if atom.target_atom:
                atom.advance_cells(unit_b.discipline, atom.target_atom.centroid(), enemy_cells=a_cells_set)
        for atom in unit_a.subunits: atom.halt_before_enemy(unit_b)
        for atom in unit_b.subunits: atom.halt_before_enemy(unit_a)
        
        a_after = {c['orig']: c['abs'] for c in cell_snapshot(unit_a.subunits[0])}
        b_after = {c['orig']: c['abs'] for c in cell_snapshot(unit_b.subunits[0])}
        a_moved = [(o, a_before[o], a_after[o]) for o in a_before if a_before[o] != a_after[o]]
        b_moved = [(o, b_before[o], b_after[o]) for o in b_before if b_before[o] != b_after[o]]
        
        p(f"### Advance phase")
        p(f"- A cells moved: {len(a_moved)}")
        for o, b4, af in a_moved[:8]:
            p(f"  - orig {o}: {b4} → {af}")
        if len(a_moved) > 8: p(f"  ... +{len(a_moved)-8} more")
        p(f"- B cells moved: {len(b_moved)}")
        for o, b4, af in b_moved[:8]:
            p(f"  - orig {o}: {b4} → {af}")
        if len(b_moved) > 8: p(f"  ... +{len(b_moved)-8} more")
        p(f"")
        
        # ── CROSS-SIDE CONTENTION ────────────────────────────────────────
        # Wrap to capture firings
        a_after_again = {c['orig']: c['abs'] for c in cell_snapshot(unit_a.subunits[0])}
        b_after_again = {c['orig']: c['abs'] for c in cell_snapshot(unit_b.subunits[0])}
        n_resolved = sim.resolve_cross_side_contention(unit_a, unit_b)
        a_after_xsc = {c['orig']: c['abs'] for c in cell_snapshot(unit_a.subunits[0])}
        b_after_xsc = {c['orig']: c['abs'] for c in cell_snapshot(unit_b.subunits[0])}
        a_reverted = [(o, a_after_again[o], a_after_xsc[o]) for o in a_after_again if a_after_again[o] != a_after_xsc[o]]
        b_reverted = [(o, b_after_again[o], b_after_xsc[o]) for o in b_after_again if b_after_again[o] != b_after_xsc[o]]
        
        p(f"### Cross-side contention")
        p(f"- {n_resolved} cells resolved")
        if a_reverted:
            p(f"- A cells reverted:")
            for o, b4, af in a_reverted: p(f"  - orig {o}: {b4} → {af}")
        if b_reverted:
            p(f"- B cells reverted:")
            for o, b4, af in b_reverted: p(f"  - orig {o}: {b4} → {af}")
        p(f"")
        
        # ── POST-MOVEMENT CONTACTS ────────────────────────────────────────
        pairs = sim.find_contacts(unit_a, unit_b)
        p(f"### Post-movement contact pairs")
        p(f"- {len(pairs)} contact pair(s)")
        for i, pair in enumerate(pairs):
            a_unique = sorted(set(pair['a_cells']))
            b_unique = sorted(set(pair['b_cells']))
            p(f"  - pair {i}: cols={sorted(pair['cols'])}")
            p(f"    A contact cells ({len(a_unique)}): {a_unique[:10]}{'...' if len(a_unique)>10 else ''}")
            p(f"    B contact cells ({len(b_unique)}): {b_unique[:10]}{'...' if len(b_unique)>10 else ''}")
        p(f"")
        
        # ── ENGAGEMENT (instrumented) ────────────────────────────────────
        # We run resolve_engagements_cascading but also reconstruct pool components
        # for the audit trail.
        p(f"### Engagement pool components")
        for i, pair in enumerate(pairs):
            atom_a_ = pair["atom_a"]
            atom_b_ = pair["atom_b"]
            cols = pair["cols"]
            primary_col = sorted(cols)[len(cols)//2]
            role_a = atom_a_.role_at_contact(primary_col)
            role_b = atom_b_.role_at_contact(primary_col)
            off_a = sim.SHAPE_OFF_MOD[atom_a_.shape](role_a)
            off_b = sim.SHAPE_OFF_MOD[atom_b_.shape](role_b)
            tf_a = atom_a_.troop_count / unit_a.total_troops()
            tf_b = atom_b_.troop_count / unit_b.total_troops()
            base_a = unit_a.base_combat_pool()
            base_b = unit_b.base_combat_pool()
            ef_a = sim.support_engage_frac(atom_a_, pair["a_cells"])
            ef_b = sim.support_engage_frac(atom_b_, pair["b_cells"])
            mom_a = sim._momentum_speed(atom_a_, pair["a_cells"]) if sim.PUNCTURE_ENABLED else 0
            mom_b = sim._momentum_speed(atom_b_, pair["b_cells"]) if sim.PUNCTURE_ENABLED else 0
            p(f"  - pair {i}: primary_col={primary_col}")
            p(f"    A: role={role_a} off={off_a} base_pool={base_a} troops_frac={tf_a:.2f} engage_frac={ef_a:.2f} momentum_speed={mom_a:.2f}")
            p(f"    B: role={role_b} off={off_b} base_pool={base_b} troops_frac={tf_b:.2f} engage_frac={ef_b:.2f} momentum_speed={mom_b:.2f}")
        p(f"")
        
        # Now actually resolve
        result = (sim.resolve_engagements_cascading(unit_a, unit_b, pairs)
                  if sim.CASCADING_ENABLED
                  else sim.resolve_engagements(unit_a, unit_b, pairs))
        p(f"### Engagement result")
        p(f"- A dmg taken: {result['dmg_a']}")
        p(f"- B dmg taken: {result['dmg_b']}")
        p(f"- engagements: {result.get('engagements', '?')}")
        p(f"")
        
        # ── APPLY DAMAGE ─────────────────────────────────────────────────
        sz_a_mid, sz_b_mid = unit_a.size, unit_b.size
        volley_hp_scale = lambda u: max(1, (u.h_per_size + 1) // 2)
        unit_a.hp = max(0, unit_a.hp - result["dmg_a"] - volley_dmg_a * volley_hp_scale(unit_a))
        unit_a.recalc_size()
        unit_b.hp = max(0, unit_b.hp - result["dmg_b"] - volley_dmg_b * volley_hp_scale(unit_b))
        unit_b.recalc_size()
        
        # Discipline / morale checks (same as run_battle)
        for u, sls, slo in [(unit_a, sz_a_mid - unit_a.size, sz_b_mid - unit_b.size),
                            (unit_b, sz_b_mid - unit_b.size, sz_a_mid - unit_a.size)]:
            if u.routed or u.broken: continue
            if sls > u.discipline and sls > slo:
                u.discipline = max(0, u.discipline - 1)
            u.check_drift()
        for u in [unit_a, unit_b]:
            if u.routed: continue
            cap = 3; adj = 0
            if u.size < u.size_max // 4 and u.size > 0: adj += -min(2, cap); cap -= 2
            elif u.size < u.size_max // 2: adj += -min(1, cap); cap -= 1
            u.morale = max(1, u.morale + adj)
            if u.morale <= 0: u.routed = True
        
        # ── END-OF-TICK SUMMARY ──────────────────────────────────────────
        p(f"### End-of-tick deltas")
        p(f"- A: hp {hp_a_pre}→{unit_a.hp} (Δ{unit_a.hp - hp_a_pre}), sz {sz_a_pre}→{unit_a.size} (Δ{unit_a.size - sz_a_pre}), morale {mor_a_pre}→{unit_a.morale} (Δ{unit_a.morale - mor_a_pre})")
        p(f"- B: hp {hp_b_pre}→{unit_b.hp} (Δ{unit_b.hp - hp_b_pre}), sz {sz_b_pre}→{unit_b.size} (Δ{unit_b.size - sz_b_pre}), morale {mor_b_pre}→{unit_b.morale} (Δ{unit_b.morale - mor_b_pre})")
        p(f"")
        
        # ── GRID ─────────────────────────────────────────────────────────
        p(f"### Grid at end of tick")
        p(f"```")
        p(render_grid(unit_a, unit_b))
        p(f"```")
        p(f"")
        
        # ── PHASE BOUNDARY ───────────────────────────────────────────────
        if t % sim.TICKS_PER_PHASE == 0:
            current_phase += 1
            sim.phase_boundary(unit_a, unit_b, current_phase)
            p(f"### ═══════ PHASE {current_phase} BOUNDARY ═══════")
            p(f"- stamina_check fired (no-op in v14)")
            p(f"- morale_check_phase fired (no-op in v14)")
            p(f"- rout_resolution fired (no-op in v14)")
            p(f"- rally_check fired (no-op in v14)")
            p(f"- reform_check fired (no-op in v14)")
            p(f"- threadwork_check fired (no-op in v14)")
            p(f"")
    
    # ── BATTLE RESULT ────────────────────────────────────────────────────
    winner = ("A" if not unit_a.routed and unit_b.routed else
              "B" if not unit_b.routed and unit_a.routed else "draw")
    p(f"---")
    p(f"")
    p(f"## Battle result")
    p(f"")
    p(f"- Winner: **{winner}**")
    p(f"- Turns: {turns}")
    p(f"- Phases completed: {current_phase}")
    p(f"- Final A: hp={unit_a.hp}/{unit_a.hp_max}, sz={unit_a.size}/{unit_a.size_max}, routed={unit_a.routed}")
    p(f"- Final B: hp={unit_b.hp}/{unit_b.hp_max}, sz={unit_b.size}/{unit_b.size_max}, routed={unit_b.routed}")
    
    output = out.getvalue()
    if output_path:
        with open(output_path, 'w') as f:
            f.write(output)
    return output, {"winner": winner, "turns": turns, "phases": current_phase}


if __name__ == '__main__':
    ANCHOR = {'Line':9,'Arrowhead':8,'Horseshoe':8,'GappedLine':7,'RefusedFlank':9}
    def mk(shape, faction, unit_type='melee', stance='balanced'):
        ad = -1 if faction == 'A' else 1
        sr = sim.SIDE_A_START_ROW if faction == 'A' else sim.SIDE_B_START_ROW
        return sim.Unit(faction, faction, 4, 4, 5, 5, 6, 6, subunits=[
            sim.Subunit(shape, 'infantry', 3, (sr, ANCHOR[shape]), ad, stance, unit_type)], dr=1)
    
    # H5 — outstanding tension
    ua = mk('RefusedFlank', 'A')
    ub = mk('Horseshoe', 'B')
    # [canonical: tests/sim/sim_mb_06_v13.py — battery seed offset 1_000_000 for reproducibility]
    text, result = record_battle(ua, ub, seed=1_000_000, output_path='/home/claude/h5_tick_record.md')
    print(f"H5 (RF vs HS, seed 1000000): {result}")
    print(f"  → /home/claude/h5_tick_record.md ({len(text)} chars)")
    
    # H1 — control (Line vs Line)
    ua = mk('Line', 'A')
    ub = mk('Line', 'B')
    # [canonical: tests/sim/sim_mb_06_v13.py — battery seed offset 1_000_000 for reproducibility]
    text, result = record_battle(ua, ub, seed=1_000_000, output_path='/home/claude/h1_tick_record.md')
    print(f"H1 (Line vs Line, seed 1000000): {result}")
    print(f"  → /home/claude/h1_tick_record.md ({len(text)} chars)")
