# [canonical: tests/sim/sim_mb_06_v9_historical_spec.md §win-rate bands]
"""SIM-MB-06 v22 — Historical accuracy battery (multi-turn recalibration).

Ports v9 battery to v22 multi-turn model. Tests run_multi_turn_battle
instead of single-turn run_battle. Out-of-band results surface as OUT.
"""
import sys, random, statistics
sys.path.insert(0, '/home/claude')

# Load v22 sim into namespace
exec(open('/home/claude/sim_v22.py').read())

# [canonical: mass_battle_v30.md §deployment — anchor column per shape/tier]
# All values below: anchor columns from mass_battle_v30.md §deployment
ANCHOR_MAP = {
    ('Line', 1): 11, ('Line', 2): 10, ('Line', 3): 9,  ('Line', 4): 8,  # [canonical: mass_battle_v30.md §deployment]
    ('Arrowhead', 1): 11, ('Arrowhead', 2): 10, ('Arrowhead', 3): 8, ('Arrowhead', 4): 7,  # [canonical: mass_battle_v30.md §deployment]
    ('Horseshoe', 1): 11, ('Horseshoe', 2): 10, ('Horseshoe', 3): 8, ('Horseshoe', 4): 7,  # [canonical: mass_battle_v30.md §deployment]
    ('GappedLine', 1): 11, ('GappedLine', 2): 9,  ('GappedLine', 3): 7,  # [canonical: mass_battle_v30.md §deployment]
    ('RefusedFlank', 1): 11, ('RefusedFlank', 2): 10, ('RefusedFlank', 3): 9,  # [canonical: mass_battle_v30.md §deployment]
}

def make_unit(shape, tier, name, faction, unit_type='melee', power=4, command=4,
              discipline=5, morale=6, stance='balanced'):
    advance_dir = -1 if faction == 'A' else 1
    start_row = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    anchor_col = ANCHOR_MAP.get((shape, tier), 10)
    atom = Subunit(
        shape=shape, troop_type='infantry', tier=tier,
        starting_position=(start_row, anchor_col),
        advance_dir=advance_dir,
        unit_type=unit_type,
    )
    return Unit(
        name=name, faction=faction,
        power=power, command=command,
        discipline=discipline, discipline_start=discipline,
        morale=morale, morale_start=morale,
        subunits=[atom], dr=1,
        stance=stance,
    )

# [canonical: tests/sim/sim_mb_06_v9_battery.py — structural: n and seed_base are test parameters]
def matchup(make_a_fn, make_b_fn, shape_a, shape_b, n=80, seed_base=1000000):  # [canonical: structural — test parameters]
    a_wins = b_wins = draws = 0
    turns_list = []
    for s in range(n):
        random.seed(s + seed_base)
        ua = make_a_fn()
        ub = make_b_fn()
        r = run_multi_turn_battle(ua, ub, shape_a, shape_b, ANCHOR_MAP,
                                   max_battle_turns=20)
        if   r['winner'] == 'A': a_wins += 1
        elif r['winner'] == 'B': b_wins += 1
        else:                    draws += 1
        turns_list.append(r['battle_turns'])
    return {
        'a_pct': a_wins / n * 100,
        'b_pct': b_wins / n * 100,
        'd_pct': draws  / n * 100,
        'mean_turns': statistics.mean(turns_list),
        'n': n,
    }

# [canonical: tests/sim/sim_mb_06_v9_historical_spec.md §target bands — all band values below]
# (test_id, label, make_a, make_b, shape_a, shape_b, lo, hi)
TESTS = [
    ('H1', 'Line vs Line (mirror)',
        lambda: make_unit('Line', 3, 'A', 'A'),  # [canonical: mass_battle_v30.md §deployment]
        lambda: make_unit('Line', 3, 'B', 'B'),  # [canonical: mass_battle_v30.md §deployment]
        'Line', 'Line', 45, 55),  # [canonical: sim_mb_06_v9_historical_spec.md §target bands]
    ('H2', 'Arrowhead vs Line',
        lambda: make_unit('Arrowhead', 3, 'A', 'A'),  # [canonical: mass_battle_v30.md §deployment]
        lambda: make_unit('Line', 3, 'B', 'B'),  # [canonical: mass_battle_v30.md §deployment]
        'Arrowhead', 'Line', 50, 65),  # [canonical: sim_mb_06_v9_historical_spec.md §target bands]
    ('H3', 'Horseshoe vs Line',
        lambda: make_unit('Horseshoe', 3, 'A', 'A'),  # [canonical: mass_battle_v30.md §deployment]
        lambda: make_unit('Line', 3, 'B', 'B'),  # [canonical: mass_battle_v30.md §deployment]
        'Horseshoe', 'Line', 50, 65),  # [canonical: sim_mb_06_v9_historical_spec.md §target bands]
    ('H4', 'Horseshoe vs Arrowhead',
        lambda: make_unit('Horseshoe', 3, 'A', 'A'),  # [canonical: mass_battle_v30.md §deployment]
        lambda: make_unit('Arrowhead', 3, 'B', 'B'),  # [canonical: mass_battle_v30.md §deployment]
        'Horseshoe', 'Arrowhead', 40, 60),  # [canonical: sim_mb_06_v9_historical_spec.md §target bands]
    ('H5', 'RefusedFlank vs Horseshoe',
        lambda: make_unit('RefusedFlank', 3, 'A', 'A'),  # [canonical: mass_battle_v30.md §deployment]
        lambda: make_unit('Horseshoe', 3, 'B', 'B'),  # [canonical: mass_battle_v30.md §deployment]
        'RefusedFlank', 'Horseshoe', 50, 65),  # [canonical: sim_mb_06_v9_historical_spec.md §target bands]
    ('H6', 'RefusedFlank vs Line',
        lambda: make_unit('RefusedFlank', 3, 'A', 'A'),  # [canonical: mass_battle_v30.md §deployment]
        lambda: make_unit('Line', 3, 'B', 'B'),  # [canonical: mass_battle_v30.md §deployment]
        'RefusedFlank', 'Line', 45, 60),  # [canonical: sim_mb_06_v9_historical_spec.md §target bands]
    ('H7', 'GappedLine vs Line',
        lambda: make_unit('GappedLine', 3, 'A', 'A'),  # [canonical: mass_battle_v30.md §deployment]
        lambda: make_unit('Line', 3, 'B', 'B'),  # [canonical: mass_battle_v30.md §deployment]
        'GappedLine', 'Line', 50, 65),  # [canonical: sim_mb_06_v9_historical_spec.md §target bands]
    ('H8', 'GappedLine vs Arrowhead',
        lambda: make_unit('GappedLine', 3, 'A', 'A'),  # [canonical: mass_battle_v30.md §deployment]
        lambda: make_unit('Arrowhead', 3, 'B', 'B'),  # [canonical: mass_battle_v30.md §deployment]
        'GappedLine', 'Arrowhead', 45, 60),  # [canonical: sim_mb_06_v9_historical_spec.md §target bands]
    ('H9', 'Line vs Arrowhead (rev H2)',
        lambda: make_unit('Line', 3, 'A', 'A'),  # [canonical: mass_battle_v30.md §deployment]
        lambda: make_unit('Arrowhead', 3, 'B', 'B'),  # [canonical: mass_battle_v30.md §deployment]
        'Line', 'Arrowhead', 35, 50),  # [canonical: sim_mb_06_v9_historical_spec.md §target bands]
    ('H10', 'Line vs Horseshoe (rev H3)',
        lambda: make_unit('Line', 3, 'A', 'A'),  # [canonical: mass_battle_v30.md §deployment]
        lambda: make_unit('Horseshoe', 3, 'B', 'B'),  # [canonical: mass_battle_v30.md §deployment]
        'Line', 'Horseshoe', 35, 50),  # [canonical: sim_mb_06_v9_historical_spec.md §target bands]
    ('H11', 'Arrowhead vs Horseshoe (rev H4)',
        lambda: make_unit('Arrowhead', 3, 'A', 'A'),  # [canonical: mass_battle_v30.md §deployment]
        lambda: make_unit('Horseshoe', 3, 'B', 'B'),  # [canonical: mass_battle_v30.md §deployment]
        'Arrowhead', 'Horseshoe', 40, 60),  # [canonical: sim_mb_06_v9_historical_spec.md §target bands]
    ('R1', 'Ranged vs Line (open field)',
        lambda: make_unit('Line', 3, 'A', 'A', unit_type='ranged', stance='hold'),  # [canonical: mass_battle_v30.md §deployment]
        lambda: make_unit('Line', 3, 'B', 'B'),  # [canonical: mass_battle_v30.md §deployment]
        'Line', 'Line', 30, 50),  # [canonical: sim_mb_06_v9_historical_spec.md §target bands]
    ('R3', 'Ranged vs Ranged (mirror)',
        lambda: make_unit('Line', 3, 'A', 'A', unit_type='ranged', stance='hold'),  # [canonical: mass_battle_v30.md §deployment]
        lambda: make_unit('Line', 3, 'B', 'B', unit_type='ranged', stance='hold'),  # [canonical: mass_battle_v30.md §deployment]
        'Line', 'Line', 45, 55),  # [canonical: sim_mb_06_v9_historical_spec.md §target bands]
]

def row(test_id, label, r, lo, hi):
    a = r['a_pct']
    in_band = lo <= a <= hi
    flag = '  OK' if in_band else '  <- OUT'
    return (f"  [{test_id}] {label[:42]:42s}  "
            f"A:{a:5.1f}%  B:{r['b_pct']:5.1f}%  D:{r['d_pct']:5.1f}%  "
            f"t={r['mean_turns']:4.1f}   target {lo}-{hi}%{flag}")

if __name__ == '__main__':
    sep = '=' * 92  # [canonical: structural — formatting width]
    print(sep)
    print('SIM-MB-06 v22 — Historical accuracy battery (multi-turn)')
    print(sep)
    in_band = 0
    for test_id, label, make_a, make_b, sa, sb, lo, hi in TESTS:
        # [canonical: structural — sample size for battery run]
        r = matchup(make_a, make_b, sa, sb, n=40)
        line = row(test_id, label, r, lo, hi)
        print(line)
        if lo <= r['a_pct'] <= hi:
            in_band += 1
    print()
    print(sep)
    print(f'In-band: {in_band}/{len(TESTS)} ({in_band/len(TESTS)*100:.0f}%)')
    print(sep)
