"""Depth-vs-width probe: does the engine give DEPTH any reserve/staying-power value,
or is it pure-width (frontage never saturates, deep formations strictly worse)?

Controlled: equal total troops, equal per-cell density (100/cell). Only the aspect
(narrow-deep vs wide-shallow) differs. If depth = reserve, the deep column should hold
a capped frontage and NOT lose badly. If pure-width (PC_FRONTAGE_BLEND=0), the wide line
out-frontages and crushes the deep column.
"""
import sys, os, random, statistics
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mass_battle.engine import build_army, resolve_battle, SIDE_A_START_ROW, SIDE_B_START_ROW
import mass_battle.config as c


def unit(name, faction, width, depth, conc=100):
    start_row = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    troops = width * depth * conc
    spec = {'shape': 'Line', 'troop_type': 'infantry', 'unit_type': 'melee',
            'width': width, 'depth': depth, 'troops': troops,
            'starting_position': (start_row, 25)}
    return build_army([spec], name, faction), troops


def duel(wa, da, wb, db, n=20, label=''):
    aw = bw = dr = 0
    turns = []
    for s in range(n):
        random.seed(1_000_000 + s)
        ua, ta = unit('A', 'A', wa, da)
        ub, tb = unit('B', 'B', wb, db)
        r = resolve_battle(ua, ub, 'Line', 'Line', {}, kind='multi', max_battle_turns=30)
        w = r.get('winner', 'draw')
        if w == 'A': aw += 1
        elif w == 'B': bw += 1
        else: dr += 1
        turns.append(r.get('battle_turns', 30))
    print(f"  {label:40} A(w{wa}xd{da},{ta}t) vs B(w{wb}xd{db},{tb}t): A%={100*aw/n:5.1f} B%={100*bw/n:5.1f} D%={100*dr/n:5.1f} t={statistics.mean(turns):4.1f}", flush=True)


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    print(f"PC_FRONTAGE_BLEND={c.PC_FRONTAGE_BLEND} PC_FRONTAGE_REF={c.PC_FRONTAGE_REF} PC_DEPTH_ROTATE={c.PC_DEPTH_ROTATE} PC_FRONT_RANKS={c.PC_FRONT_RANKS} n={n}", flush=True)
    # equal troops (2400), equal density (100/cell), only aspect differs
    duel(24, 1, 24, 1, n=n, label='control: wide vs wide (mirror)')
    duel(6, 4, 6, 4, n=n, label='control: square vs square (mirror)')
    duel(6, 4, 24, 1, n=n, label='DEEP(6x4) vs WIDE(24x1) — same troops/density')
    duel(4, 6, 24, 1, n=n, label='DEEPER(4x6) vs WIDE(24x1)')
    duel(3, 8, 24, 1, n=n, label='DEEPEST(3x8) vs WIDE(24x1)')
