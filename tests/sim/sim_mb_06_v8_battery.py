# [canonical: tests/sim/sim_mb_06_v8_manifest.md §battery — targets from Jordan handoff + v7 baselines]
"""SIM-MB-06 v8 tension-F battery.
Tests T1 Arrowhead/Line (key), T2 mirror sanity, T3 Cannae, T4 reversed,
T5 tier sweep, T6 Horseshoe/Line, T7 lethality.
Targets and baselines: see tests/sim/sim_mb_06_v8_manifest.md.
"""
import sys, random, statistics
sys.path.insert(0, '/home/claude')
import sim_mb_06_v8 as sim

# [canonical: mass_battle_v30.md §deployment — anchor column per shape/tier in 25-col battlefield]
ANCHOR_MAP = {
    ('Line', 1): 11, ('Line', 2): 10, ('Line', 3): 9,  ('Line', 4): 8,
    ('Arrowhead', 1): 11, ('Arrowhead', 2): 10, ('Arrowhead', 3): 8, ('Arrowhead', 4): 7,
    ('Horseshoe', 1): 11, ('Horseshoe', 2): 10, ('Horseshoe', 3): 8, ('Horseshoe', 4): 7,
}

def make_unit(shape, tier, name, faction):
    advance_dir = -1 if faction == 'A' else 1
    start_row   = sim.SIDE_A_START_ROW if faction == 'A' else sim.SIDE_B_START_ROW
    anchor_col  = ANCHOR_MAP.get((shape, tier), 10)
    atom = sim.Atom(
        shape=shape, troop_type='infantry', tier=tier,
        starting_position=(start_row, anchor_col),
        advance_dir=advance_dir,
    )
    return sim.Unit(
        name=name, faction=faction,
        power=4, command=4,
        discipline=5, discipline_start=5,
        morale=6, morale_start=6,
        atoms=[atom], dr=1,
    )

# [canonical: structural — trial counts n=80/100/120 and seed bases chosen for reproducibility]
def matchup(shape_a, tier_a, shape_b, tier_b, n=100, seed_base=800000):
    a_wins = b_wins = draws = 0
    turns_list = []
    for s in range(n):
        random.seed(s + seed_base)
        ua = make_unit(shape_a, tier_a, 'A', 'A')
        ub = make_unit(shape_b, tier_b, 'B', 'B')
        r  = sim.run_battle(ua, ub)
        if   r['winner'] == 'A': a_wins += 1
        elif r['winner'] == 'B': b_wins += 1
        else:                    draws   += 1
        turns_list.append(r.get('turns', sim.MAX_TURNS if hasattr(sim, 'MAX_TURNS') else 15))
    return {
        'a_pct':      a_wins / n * 100,
        'b_pct':      b_wins / n * 100,
        'draw_pct':   draws  / n * 100,
        'mean_turns': statistics.mean(turns_list),
        'n': n,
    }

# Target ranges from Jordan handoff: see sim_mb_06_v8_manifest.md
# [canonical: tests/sim/sim_mb_06_v8_manifest.md §targets]
A_LO, A_HI   = 40, 60   # standard winrate target band
CANNAE_HI     = 65       # Cannae upper bound (asymmetric shape advantage)
REV_LO        = 35       # reversed Cannae lower bound
BIAS_THRESHOLD = 8       # mirror match max acceptable side bias (pp)
TURN_LO, TURN_HI = 3, 6 # lethality target

def row(label, r, lo=A_LO, hi=A_HI):
    ok   = lo <= r['a_pct'] <= hi
    flag = '' if ok else ' <- OUT'
    return (f"  {label:45s}  A:{r['a_pct']:5.1f}%  B:{r['b_pct']:5.1f}%  "
            f"D:{r['draw_pct']:5.1f}%  t={r['mean_turns']:.1f}{flag}")

def main():
    sep = '=' * 78
    out = [sep, 'SIM-MB-06 v8 — tension F battery', sep]

    out.append('\n[T1] Arrowhead vs Line T3  (KEY: was 0%, target ' + str(A_LO) + '-' + str(A_HI) + '%)')
    r = matchup('Arrowhead', 3, 'Line', 3, n=120)
    out.append(row('Arrowhead-A vs Line-B  T3', r))

    out.append('\n[T2] Line vs Line T3 mirror  (sanity ~50/50)')
    r = matchup('Line', 3, 'Line', 3, n=100)
    bias_ok = abs(r['a_pct'] - 50) <= BIAS_THRESHOLD
    flag = '' if bias_ok else ' <- BIAS'
    out.append(f"  {'Line-A vs Line-B  T3':45s}  A:{r['a_pct']:5.1f}%  B:{r['b_pct']:5.1f}%  t={r['mean_turns']:.1f}{flag}")

    out.append('\n[T3] Horseshoe vs Arrowhead T3  (Cannae; target ' + str(A_LO) + '-' + str(CANNAE_HI) + '%)')
    r = matchup('Horseshoe', 3, 'Arrowhead', 3, n=100)
    out.append(row('Horseshoe-A vs Arrowhead-B  T3', r, lo=A_LO, hi=CANNAE_HI))

    out.append('\n[T4] Arrowhead vs Horseshoe T3  (reversed; target ' + str(REV_LO) + '-' + str(CANNAE_HI) + '%)')
    r = matchup('Arrowhead', 3, 'Horseshoe', 3, n=100)
    out.append(row('Arrowhead-A vs Horseshoe-B  T3', r, lo=REV_LO, hi=CANNAE_HI))

    out.append('\n[T5] Tier sweep — Arrowhead vs Line  (target ' + str(A_LO) + '-' + str(A_HI) + '%)')
    for tier in [2, 3, 4]:
        r = matchup('Arrowhead', tier, 'Line', tier, n=80)
        out.append(row(f'Arrowhead-A vs Line-B  T{tier}', r))

    out.append('\n[T6] Horseshoe vs Line T3  (was 0%; target ' + str(A_LO) + '-' + str(A_HI) + '%)')
    r = matchup('Horseshoe', 3, 'Line', 3, n=120)
    out.append(row('Horseshoe-A vs Line-B  T3', r))

    out.append('\n[T7] Lethality — Line mirror mean turns  (was 9.7; target ' + str(TURN_LO) + '-' + str(TURN_HI) + ')')
    r = matchup('Line', 3, 'Line', 3, n=100, seed_base=900000)
    ok = TURN_LO <= r['mean_turns'] <= TURN_HI
    flag = '' if ok else ' <- OUT'
    out.append(f"  {'Line-A vs Line-B  T3 (lethality)':45s}  t={r['mean_turns']:.1f}  "
               f"A:{r['a_pct']:5.1f}%  B:{r['b_pct']:5.1f}%{flag}")

    out.append('\n' + sep)
    out.append(f'TARGETS: T1={A_LO}-{A_HI}%  T2=±{BIAS_THRESHOLD}pp  T3={A_LO}-{CANNAE_HI}%  '
               f'T6={A_LO}-{A_HI}%  T7={TURN_LO}-{TURN_HI}t')
    out.append(sep)

    return '\n'.join(out)

if __name__ == '__main__':
    print(main())
