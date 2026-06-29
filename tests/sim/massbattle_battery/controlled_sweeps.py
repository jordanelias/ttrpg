"""Controlled bottom-up stress test — ONE variable per sweep, everything else fixed at a control,
mapped onto the hierarchy: STRATEGY (unit formation/stance), TACTIC (subunit instruction), TROOP
TYPE (subunit). Every test unit fights the SAME fixed control opponent so the only thing that moves
is the one variable. Uses the engine's canonical resolving driver (run_multi_turn_battle), PER_CELL=1.

Output: controlled_sweeps_results.json + console tables. Each row: decA (A_wins/(A+B)), draw%,
casualty margin (enemy% - own%, +ve = test unit winning the attrition), avg battle-turns.
"""
import os, sys, random, json
for _k in ('PER_CELL', 'LANCHESTER_ENABLED', 'COMMAND_SIGMA_ENABLED', 'PC_BRACE_ENABLED'):
    os.environ.setdefault(_k, '1')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..'))
from mass_battle.config import SIDE_A_START_ROW, SIDE_B_START_ROW   # noqa: E402
from mass_battle.orchestration import Subunit, Unit, run_multi_turn_battle  # noqa: E402

ANCHOR = {('Line', 3): 9, ('Arrowhead', 3): 8, ('Horseshoe', 3): 8, ('GappedLine', 3): 7,
          ('RefusedFlank', 3): 9, ('Column', 3): 10}
N = int(os.environ.get('SWEEP_N', '30'))


def mk(shape, fac, troop='heavy_infantry', unit_type='melee', stance='balanced', instr=()):
    adv = -1 if fac == 'A' else 1; row = SIDE_A_START_ROW if fac == 'A' else SIDE_B_START_ROW
    su = Subunit.of_type(troop, shape, 3, (row, ANCHOR.get((shape, 3), 10)), advance_dir=adv,
                         unit_type=unit_type, stance=stance, instructions=tuple(instr))
    return Unit(name=f'{fac}', faction=fac, power=4, command=5, discipline=5, discipline_start=5,
                morale=6, morale_start=6, subunits=[su], dr=1, stance=stance,
                speed='Fast' if troop == 'cavalry' else 'Standard')


# Fixed control opponent for EVERY test: a standard heavy-infantry Line, balanced.
def control_B():
    return mk('Line', 'B')


def battle(make_a, shape_a, n=N):
    aw = bw = dr = 0; margin = []; turns = []
    for s in range(n):
        random.seed(s + 1_000_000)
        ua = make_a(); ub = control_B()
        a0, b0 = ua.hp_max, ub.hp_max
        r = run_multi_turn_battle(ua, ub, shape_a, 'Line', ANCHOR, max_battle_turns=20)
        w = r['winner']; aw += (w == 'A'); bw += (w == 'B'); dr += (w == 'draw')
        turns.append(r['battle_turns'])
        margin.append((100 * (b0 - ub.hp) / b0) - (100 * (a0 - ua.hp) / a0))
    dec = aw + bw
    return dict(decA=round(100 * aw / dec, 1) if dec else 50.0, A=aw, B=bw, draw=dr,
                draw_pct=round(100 * dr / n, 1), cas_margin=round(sum(margin) / n, 1),
                avg_turns=round(sum(turns) / n, 1))


def show(title, rows):
    print(f"\n=== {title} (vs fixed control: heavy-infantry Line/balanced; decA = test-unit decisive split) ===")
    print(f"  {'variable value':34} {'decA':>6} {'draw%':>6} {'cas-marg':>9} {'turns':>6}")
    out = {}
    for label, (mka, shape) in rows.items():
        r = battle(mka, shape)
        out[label] = r
        print(f"  {label:34} {r['decA']:6.1f} {r['draw_pct']:6.1f} {r['cas_margin']:+9.1f} {r['avg_turns']:6.1f}")
    return out


if __name__ == '__main__':
    print(f"N={N} per cell; control opponent = heavy-infantry Line/balanced")
    results = {}

    # SWEEP A — STRATEGY (unit overall): formation + stance.  Fixed: troop=heavy_infantry, tactic=plain.
    A = {
        'Line / balanced  (control mirror)': (lambda: mk('Line', 'A'), 'Line'),
        'Horseshoe / balanced (envelop)':    (lambda: mk('Horseshoe', 'A'), 'Horseshoe'),
        'Arrowhead / balanced (wedge)':      (lambda: mk('Arrowhead', 'A'), 'Arrowhead'),
        'RefusedFlank / balanced (oblique)': (lambda: mk('RefusedFlank', 'A'), 'RefusedFlank'),
        'GappedLine / balanced (manipular)': (lambda: mk('GappedLine', 'A'), 'GappedLine'),
        'Line / aggressive':                 (lambda: mk('Line', 'A', stance='aggressive'), 'Line'),
        'Line / hold (defensive)':           (lambda: mk('Line', 'A', stance='hold'), 'Line'),
    }
    results['A_strategy'] = show("SWEEP A — STRATEGY (unit formation/stance)", A)

    # SWEEP B — TACTIC (subunit instruction).  Fixed: troop=heavy_infantry, strategy=Line/balanced.
    B = {
        'plain  (control)':         (lambda: mk('Line', 'A'), 'Line'),
        'brace':                    (lambda: mk('Line', 'A', instr=('brace',)), 'Line'),
        'brace + hold (shieldwall)':(lambda: mk('Line', 'A', stance='hold', instr=('brace', 'hold')), 'Line'),
        'charge':                   (lambda: mk('Line', 'A', stance='aggressive', instr=('charge',)), 'Line'),
        'advance / push':           (lambda: mk('Line', 'A', stance='aggressive', instr=('advance',)), 'Line'),
        'envelop':                  (lambda: mk('Line', 'A', instr=('envelop',)), 'Line'),
        'loose / harass (skirmish)':(lambda: mk('Line', 'A', instr=('loose', 'harass')), 'Line'),
    }
    results['B_tactic'] = show("SWEEP B — TACTIC (subunit instruction)", B)

    # SWEEP C — TROOP TYPE (subunit).  Fixed: strategy=Line/balanced, tactic=plain melee.
    C = {
        'levy':            (lambda: mk('Line', 'A', troop='levy'), 'Line'),
        'light_infantry':  (lambda: mk('Line', 'A', troop='light_infantry'), 'Line'),
        'heavy_infantry (control)': (lambda: mk('Line', 'A', troop='heavy_infantry'), 'Line'),
        'cavalry':         (lambda: mk('Line', 'A', troop='cavalry'), 'Line'),
        'archers (melee)': (lambda: mk('Line', 'A', troop='archers'), 'Line'),
        'archers (ranged)':(lambda: mk('Line', 'A', troop='archers', unit_type='ranged', stance='hold'), 'Line'),
        'crossbow (ranged)':(lambda: mk('Line', 'A', troop='crossbow', unit_type='ranged', stance='hold'), 'Line'),
        'knights_templar': (lambda: mk('Line', 'A', troop='knights_templar'), 'Line'),
    }
    results['C_troop_type'] = show("SWEEP C — TROOP TYPE (subunit)", C)

    json.dump(results, open(os.path.join(HERE, 'controlled_sweeps_results.json'), 'w'), indent=1)
    print("\nwrote controlled_sweeps_results.json")
