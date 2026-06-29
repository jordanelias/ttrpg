"""Re-run the controlled one-variable sweeps under the PROPOSED/FIXED structure to test whether the
hierarchy comes alive: continuous engagement (positions persist, no per-turn reset) + ~2x base closing
pace + a 24-round budget. Same control opponent, same single-variable design. If strategy (formation),
tactic (instruction), and infantry troop-quality now DIFFERENTIATE outcomes, the structure fix is what
makes the hierarchy load-bearing.
"""
import os, sys, random, json
for _k in ('PER_CELL', 'LANCHESTER_ENABLED', 'COMMAND_SIGMA_ENABLED', 'PC_BRACE_ENABLED'):
    os.environ.setdefault(_k, '1')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..'))
from mass_battle.config import SIDE_A_START_ROW, SIDE_B_START_ROW   # noqa: E402
import mass_battle.orchestration as O                               # noqa: E402
from mass_battle.orchestration import Subunit, Unit, run_battle      # noqa: E402

ANCHOR = {('Line', 3): 9, ('Arrowhead', 3): 8, ('Horseshoe', 3): 8, ('GappedLine', 3): 7,
          ('RefusedFlank', 3): 9, ('Column', 3): 10}
N = int(os.environ.get('SWEEP_N', '30'))
PACE = float(os.environ.get('PACE', '2.0'))
K = int(os.environ.get('TICKS', '144'))   # 24 rounds

_ORIG = O.cell_speed
O.cell_speed = lambda shape, tier, r, c, _f=PACE: _ORIG(shape, tier, r, c) * _f


def mk(shape, fac, troop='heavy_infantry', unit_type='melee', stance='balanced', instr=()):
    adv = -1 if fac == 'A' else 1; row = SIDE_A_START_ROW if fac == 'A' else SIDE_B_START_ROW
    su = Subunit.of_type(troop, shape, 3, (row, ANCHOR.get((shape, 3), 10)), advance_dir=adv,
                         unit_type=unit_type, stance=stance, instructions=tuple(instr))
    return Unit(name=fac, faction=fac, power=4, command=5, discipline=5, discipline_start=5,
                morale=6, morale_start=6, subunits=[su], dr=1, stance=stance,
                speed='Fast' if troop == 'cavalry' else 'Standard')


def control_B(): return mk('Line', 'B')


def battle(make_a, n=N):
    aw = bw = dr = 0; margin = []
    for s in range(n):
        random.seed(s + 1_000_000)
        ua = make_a(); ub = control_B(); a0, b0 = ua.hp_max, ub.hp_max
        run_battle(ua, ub, max_turns=K)
        w = ('A' if (ub.routed and not ua.routed) else 'B' if (ua.routed and not ub.routed) else 'draw')
        aw += (w == 'A'); bw += (w == 'B'); dr += (w == 'draw')
        margin.append((100 * (b0 - ub.hp) / b0) - (100 * (a0 - ua.hp) / a0))
    dec = aw + bw
    return dict(decA=round(100 * aw / dec, 1) if dec else 50.0, draw_pct=round(100 * dr / n, 1),
                cas_margin=round(sum(margin) / n, 1))


def show(title, rows):
    print(f"\n=== {title} (FIXED structure: continuous, {PACE}x pace, {K//6} rounds; vs heavy-inf Line control) ===")
    print(f"  {'variable value':34} {'decA':>6} {'draw%':>6} {'cas-marg':>9}")
    out = {}
    for label, mka in rows.items():
        r = battle(mka); out[label] = r
        print(f"  {label:34} {r['decA']:6.1f} {r['draw_pct']:6.1f} {r['cas_margin']:+9.1f}")
    return out


if __name__ == '__main__':
    print(f"N={N}, pace={PACE}x, {K} ticks ({K//6} rounds), control = heavy-inf Line/balanced")
    res = {}
    res['A_strategy'] = show("SWEEP A — STRATEGY (formation/stance)", {
        'Line / balanced (control mirror)': lambda: mk('Line', 'A'),
        'Horseshoe (envelop)':              lambda: mk('Horseshoe', 'A'),
        'Arrowhead (wedge)':                lambda: mk('Arrowhead', 'A'),
        'RefusedFlank (oblique)':           lambda: mk('RefusedFlank', 'A'),
        'GappedLine (manipular)':           lambda: mk('GappedLine', 'A'),
        'Line / aggressive':                lambda: mk('Line', 'A', stance='aggressive'),
        'Line / hold':                      lambda: mk('Line', 'A', stance='hold'),
    })
    res['B_tactic'] = show("SWEEP B — TACTIC (instruction)", {
        'plain (control)':           lambda: mk('Line', 'A'),
        'brace':                     lambda: mk('Line', 'A', instr=('brace',)),
        'brace+hold (shieldwall)':   lambda: mk('Line', 'A', stance='hold', instr=('brace', 'hold')),
        'charge':                    lambda: mk('Line', 'A', stance='aggressive', instr=('charge',)),
        'advance/push':              lambda: mk('Line', 'A', stance='aggressive', instr=('advance',)),
        'envelop':                   lambda: mk('Line', 'A', instr=('envelop',)),
        'loose/harass (skirmish)':   lambda: mk('Line', 'A', instr=('loose', 'harass')),
    })
    res['C_troop_type'] = show("SWEEP C — TROOP TYPE", {
        'levy':                     lambda: mk('Line', 'A', troop='levy'),
        'light_infantry':           lambda: mk('Line', 'A', troop='light_infantry'),
        'heavy_infantry (control)': lambda: mk('Line', 'A', troop='heavy_infantry'),
        'cavalry':                  lambda: mk('Line', 'A', troop='cavalry'),
        'archers (melee)':          lambda: mk('Line', 'A', troop='archers'),
        'archers (ranged)':         lambda: mk('Line', 'A', troop='archers', unit_type='ranged', stance='hold'),
        'knights_templar':          lambda: mk('Line', 'A', troop='knights_templar'),
    })
    json.dump(res, open(os.path.join(HERE, 'controlled_sweeps_fixed_results.json'), 'w'), indent=1)
    print("\nwrote controlled_sweeps_fixed_results.json")
