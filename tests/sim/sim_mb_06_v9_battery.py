# [canonical: tests/sim/sim_mb_06_v9_historical_spec.md §win-rate bands]
"""SIM-MB-06 v9 historical-accuracy battery.

Tests v9 against historically-grounded target win-rate bands. Each matchup
maps to an H# or R# entry in the historical spec. Out-of-band results
surface as ← OUT for tuning in subsequent iterations.
"""
import sys, random, statistics
sys.path.insert(0, '/home/claude')
import sim_mb_06_v9 as sim

# [canonical: mass_battle_v30.md §deployment — anchor column per shape/tier]
ANCHOR_MAP = {
    ('Line', 1): 11, ('Line', 2): 10, ('Line', 3): 9,  ('Line', 4): 8,
    ('Arrowhead', 1): 11, ('Arrowhead', 2): 10, ('Arrowhead', 3): 8, ('Arrowhead', 4): 7,
    ('Horseshoe', 1): 11, ('Horseshoe', 2): 10, ('Horseshoe', 3): 8, ('Horseshoe', 4): 7,
    ('GappedLine', 1): 11, ('GappedLine', 2): 9,  ('GappedLine', 3): 7,
    ('RefusedFlank', 1): 11, ('RefusedFlank', 2): 10, ('RefusedFlank', 3): 9,
}

def make_unit(shape, tier, name, faction, unit_type='melee', power=4, command=4,
              discipline=5, morale=6, stance='balanced'):
    """Build a unit with one atom of given shape/unit_type."""
    advance_dir = -1 if faction == 'A' else 1
    start_row   = sim.SIDE_A_START_ROW if faction == 'A' else sim.SIDE_B_START_ROW
    anchor_col  = ANCHOR_MAP.get((shape, tier), 10)
    atom = sim.Atom(
        shape=shape, troop_type='infantry', tier=tier,
        starting_position=(start_row, anchor_col),
        advance_dir=advance_dir,
        unit_type=unit_type,
        stance=stance,
    )
    return sim.Unit(
        name=name, faction=faction,
        power=power, command=command,
        discipline=discipline, discipline_start=discipline,
        morale=morale, morale_start=morale,
        atoms=[atom], dr=1,
    )

# [canonical: structural — trial counts chosen for statistical precision in spec ranges]
def matchup(make_a_fn, make_b_fn, n=100, seed_base=1000000):
    a_wins = b_wins = draws = 0
    turns_list = []
    for s in range(n):
        random.seed(s + seed_base)
        ua = make_a_fn()
        ub = make_b_fn()
        r  = sim.run_battle(ua, ub)
        if   r['winner'] == 'A': a_wins += 1
        elif r['winner'] == 'B': b_wins += 1
        else:                    draws += 1
        turns_list.append(r.get('turns', 15))
    return {
        'a_pct': a_wins / n * 100,
        'b_pct': b_wins / n * 100,
        'd_pct': draws  / n * 100,
        'mean_turns': statistics.mean(turns_list),
        'n': n,
    }

# [canonical: tests/sim/sim_mb_06_v9_historical_spec.md §target bands]
# Each entry: (test_id, label, make_a, make_b, lo, hi, notes)
TESTS = [
    # ── Equal-quality melee matchups ────────────────────────────────────────
    ('H1', 'Line vs Line (mirror)',
        lambda: make_unit('Line', 3, 'A', 'A'),
        lambda: make_unit('Line', 3, 'B', 'B'),
        45, 55),
    ('H2', 'Arrowhead (Wedge) vs Line',
        lambda: make_unit('Arrowhead', 3, 'A', 'A'),
        lambda: make_unit('Line', 3, 'B', 'B'),
        50, 65),
    ('H3', 'Horseshoe (Envelopment) vs Line  [v8 OPEN]',
        lambda: make_unit('Horseshoe', 3, 'A', 'A'),
        lambda: make_unit('Line', 3, 'B', 'B'),
        50, 65),
    ('H4', 'Horseshoe vs Arrowhead (Cannae)',
        lambda: make_unit('Horseshoe', 3, 'A', 'A'),
        lambda: make_unit('Arrowhead', 3, 'B', 'B'),
        40, 60),
    ('H5', 'RefusedFlank vs Horseshoe',
        lambda: make_unit('RefusedFlank', 3, 'A', 'A'),
        lambda: make_unit('Horseshoe', 3, 'B', 'B'),
        50, 65),
    ('H6', 'RefusedFlank vs Line',
        lambda: make_unit('RefusedFlank', 3, 'A', 'A'),
        lambda: make_unit('Line', 3, 'B', 'B'),
        45, 60),
    ('H7', 'GappedLine (Manipular) vs Line',
        lambda: make_unit('GappedLine', 3, 'A', 'A'),
        lambda: make_unit('Line', 3, 'B', 'B'),
        50, 65),
    ('H8', 'GappedLine vs Arrowhead',
        lambda: make_unit('GappedLine', 3, 'A', 'A'),
        lambda: make_unit('Arrowhead', 3, 'B', 'B'),
        45, 60),
    # ── Reversed matchups (asymmetry check) ─────────────────────────────────
    ('H9',  'Line vs Arrowhead (rev H2)',
        lambda: make_unit('Line', 3, 'A', 'A'),
        lambda: make_unit('Arrowhead', 3, 'B', 'B'),
        35, 50),
    ('H10', 'Line vs Horseshoe (rev H3)',
        lambda: make_unit('Line', 3, 'A', 'A'),
        lambda: make_unit('Horseshoe', 3, 'B', 'B'),
        35, 50),
    ('H11', 'Arrowhead vs Horseshoe (rev H4)',
        lambda: make_unit('Arrowhead', 3, 'A', 'A'),
        lambda: make_unit('Horseshoe', 3, 'B', 'B'),
        40, 60),
    # ── Ranged matchups ──────────────────────────────────────────────────────
    ('R1', 'Pure Ranged vs Pure Line (open field)',
        lambda: make_unit('Line', 3, 'A', 'A', unit_type='ranged', stance='hold'),
        lambda: make_unit('Line', 3, 'B', 'B'),
        30, 50),
    ('R3', 'Ranged vs Ranged (mirror sanity)',
        lambda: make_unit('Line', 3, 'A', 'A', unit_type='ranged', stance='hold'),
        lambda: make_unit('Line', 3, 'B', 'B', unit_type='ranged', stance='hold'),
        45, 55),
]

def row(test_id, label, r, lo, hi):
    a = r['a_pct']
    in_band = lo <= a <= hi
    flag = '  ✓' if in_band else '  ← OUT'
    return (f"  [{test_id}] {label[:42]:42s}  "
            f"A:{a:5.1f}%  B:{r['b_pct']:5.1f}%  D:{r['d_pct']:5.1f}%  "
            f"t={r['mean_turns']:4.1f}   target {lo}-{hi}%{flag}")

def main():
    sep = '=' * 88
    out = [sep, 'SIM-MB-06 v9 — Historical accuracy battery', sep]
    out.append('Target bands from tests/sim/sim_mb_06_v9_historical_spec.md\n')
    in_band = 0
    total = 0
    for test_id, label, make_a, make_b, lo, hi in TESTS:
        r = matchup(make_a, make_b, n=80)
        out.append(row(test_id, label, r, lo, hi))
        if lo <= r['a_pct'] <= hi:
            in_band += 1
        total += 1
    out.append('')
    out.append(sep)
    out.append(f'In-band: {in_band}/{total} matchups ({in_band/total*100:.0f}%)')
    out.append(sep)
    return '\n'.join(out)

if __name__ == '__main__':
    print(main())
