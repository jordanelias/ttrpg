"""Cannae probe — WHY does infantry formation-geometry envelopment underdeliver vs history
(H4 Horseshoe-vs-Arrowhead: engine 41% vs band 45-62) while cavalry envelopment (C4/C7) passes?

Isolates the candidate levers by re-running H4 under controlled changes:
  C0 baseline   — Horseshoe(inf)  vs Arrowhead(inf), no instruction      (reproduce ~41%)
  C1 +envelop   — Horseshoe(inf) carries the 'envelop' instruction        (WIRING: rear-wrap path)
  C2 cav-speed  — Horseshoe(cav) vs Arrowhead(cav) (symmetric stats)       (SPEED: 2x close = reach rear)
  C3 sigma=0.6  — Horseshoe(inf), re-enable the dormant _envelopment_sigma (TUNING: width bonus)

If C1 or C3 lifts decA into 45-62 -> the lever is identified (wiring vs tuning). If only C2 -> the
rear-wrap is reachable only at cavalry speed and infantry shapes cannot envelop as built.

Run (from repo root):
  PER_CELL=1 LANCHESTER_ENABLED=1 COMMAND_SIGMA_ENABLED=1 PC_BRACE_ENABLED=1 \
    python tests/sim/massbattle_battery/cannae_probe.py
"""
import os, sys, random, json

for _k in ('PER_CELL', 'LANCHESTER_ENABLED', 'COMMAND_SIGMA_ENABLED', 'PC_BRACE_ENABLED'):
    os.environ.setdefault(_k, '1')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))

from mass_battle.config import SIDE_A_START_ROW, SIDE_B_START_ROW   # noqa: E402
import mass_battle.orchestration as O                               # noqa: E402
import mass_battle.percell as PC                                    # noqa: E402
from mass_battle.orchestration import Subunit, Unit, run_multi_turn_battle  # noqa: E402

ANCHOR_MAP = {
    ('Line', 3): 9, ('Arrowhead', 3): 8, ('Horseshoe', 3): 8,
    ('GappedLine', 3): 7, ('RefusedFlank', 3): 9,
}
BAND = (45, 62)  # H4 history band (decisive split)


def make_unit(shape, tier, name, fac, troop_type='infantry', unit_type='melee', power=4,
              command=4, discipline=5, morale=6, stance='balanced', speed='Standard', instructions=()):
    adv = -1 if fac == 'A' else 1
    row = SIDE_A_START_ROW if fac == 'A' else SIDE_B_START_ROW
    col = ANCHOR_MAP.get((shape, tier), 10)
    su = Subunit(shape=shape, troop_type=troop_type, tier=tier, starting_position=(row, col),
                 advance_dir=adv, unit_type=unit_type, instructions=tuple(instructions))
    return Unit(name=name, faction=fac, power=power, command=command,
                discipline=discipline, discipline_start=discipline,
                morale=morale, morale_start=morale, subunits=[su], dr=1, stance=stance, speed=speed)


def decA(sa, sb, ka, kb, n=50):
    aw = bw = dr = 0
    for s in range(n):
        random.seed(s + 1_000_000)
        ua = make_unit(sa, 3, 'A', 'A', **ka)
        ub = make_unit(sb, 3, 'B', 'B', **kb)
        r = run_multi_turn_battle(ua, ub, sa, sb, ANCHOR_MAP, max_battle_turns=20)
        w = r['winner']; aw += (w == 'A'); bw += (w == 'B'); dr += (w == 'draw')
    dec = aw + bw
    return dict(A=aw, B=bw, draw=dr, decA=round(100 * aw / dec, 1) if dec else 50.0,
                draw_pct=round(100 * dr / n, 1))


def verdict(d):
    lo, hi = BAND
    return 'IN BAND' if (d['A'] + d['B'] > 0 and lo <= d['decA'] <= hi) else ('below' if d['decA'] < lo else 'above')


if __name__ == '__main__':
    N = int(os.environ.get('PROBE_N', '50'))
    print("flags:", dict(PER_CELL=os.environ.get('PER_CELL'), PC_REFUSE=O.PC_REFUSE, PC_WHEEL=O.PC_WHEEL,
                         PC_ENVELOP_PATH=O.PC_ENVELOP_PATH, PC_ENVELOP_SIGMA=PC.PC_ENVELOP_SIGMA,
                         PC_ENVELOP_MOD=O.PC_ENVELOP_MOD))
    print(f"H4 Cannae band = {BAND} decisive-split; N={N}\n")
    res = {}

    res['C0_baseline'] = decA('Horseshoe', 'Arrowhead', {}, {}, N)
    print(f"  C0 baseline   inf Horseshoe vs inf Arrowhead     decA={res['C0_baseline']['decA']:5.1f}  draws={res['C0_baseline']['draw_pct']:4.1f}%  [{verdict(res['C0_baseline'])}]")

    res['C1_envelop'] = decA('Horseshoe', 'Arrowhead', {'instructions': ('envelop',)}, {}, N)
    print(f"  C1 +envelop   inf Horseshoe(envelop) vs Arrowhd  decA={res['C1_envelop']['decA']:5.1f}  draws={res['C1_envelop']['draw_pct']:4.1f}%  [{verdict(res['C1_envelop'])}]  <- WIRING (rear-wrap path)")

    res['C2_cav_speed'] = decA('Horseshoe', 'Arrowhead', {'troop_type': 'cavalry', 'speed': 'Fast'},
                               {'troop_type': 'cavalry', 'speed': 'Fast'}, N)
    print(f"  C2 cav-speed  cav Horseshoe vs cav Arrowhead     decA={res['C2_cav_speed']['decA']:5.1f}  draws={res['C2_cav_speed']['draw_pct']:4.1f}%  [{verdict(res['C2_cav_speed'])}]  <- SPEED (2x close)")

    PC.PC_ENVELOP_SIGMA = 0.6
    res['C3_sigma'] = decA('Horseshoe', 'Arrowhead', {}, {}, N)
    PC.PC_ENVELOP_SIGMA = 0.0
    print(f"  C3 sigma=0.6  inf Horseshoe (width-sigma on)     decA={res['C3_sigma']['decA']:5.1f}  draws={res['C3_sigma']['draw_pct']:4.1f}%  [{verdict(res['C3_sigma'])}]  <- TUNING (dormant width bonus)")

    with open(os.path.join(HERE, 'cannae_probe_results.json'), 'w') as fh:
        json.dump(res, fh, indent=1)
    print("\nwrote cannae_probe_results.json")
