"""Smoke test: validate the modular mass-battle engine end-to-end (direct package import,
all components wired) before running the full battery. Runs the H4 'Cannae' formation
matchup (Horseshoe envelops Arrowhead) for a small sample and prints the win split.

Run (from repo root):
  PER_CELL=1 LANCHESTER_ENABLED=1 COMMAND_SIGMA_ENABLED=1 PC_BRACE_ENABLED=1 \
    python tests/sim/massbattle_battery/smoke.py
"""
import os, sys, random

for _k in ('PER_CELL', 'LANCHESTER_ENABLED', 'COMMAND_SIGMA_ENABLED', 'PC_BRACE_ENABLED'):
    os.environ.setdefault(_k, '1')

# tests/sim on path so `mass_battle` package imports
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from mass_battle.config import SIDE_A_START_ROW, SIDE_B_START_ROW          # noqa: E402
from mass_battle.orchestration import (                                     # noqa: E402
    Subunit, Unit, run_battle, run_multi_turn_battle)

# Canonical anchor columns (subset, T3) — from gauge_mb.ANCHOR_MAP
ANCHOR_MAP = {
    ('Line', 3): 9, ('Arrowhead', 3): 8, ('Horseshoe', 3): 8,
    ('GappedLine', 3): 7, ('RefusedFlank', 3): 9,
}


def make_unit(shape, tier, name, fac, troop_type='infantry', unit_type='melee',
              power=4, command=4, discipline=5, morale=6, stance='balanced',
              speed='Standard', morale_start=None, instructions=()):
    advance_dir = -1 if fac == 'A' else 1
    start_row = SIDE_A_START_ROW if fac == 'A' else SIDE_B_START_ROW
    anchor_col = ANCHOR_MAP.get((shape, tier), 10)
    su = Subunit(shape=shape, troop_type=troop_type, tier=tier,
                 starting_position=(start_row, anchor_col), advance_dir=advance_dir,
                 unit_type=unit_type, instructions=tuple(instructions))
    return Unit(name=name, faction=fac, power=power, command=command,
                discipline=discipline, discipline_start=discipline,
                morale=morale, morale_start=(morale if morale_start is None else morale_start),
                subunits=[su], dr=1, stance=stance, speed=speed)


def run_split(sa, sb, n=24, mode='multi'):
    aw = bw = dr = 0
    for s in range(n):
        random.seed(s + 1_000_000)
        ua = make_unit(sa, 3, 'A', 'A')
        ub = make_unit(sb, 3, 'B', 'B')
        if mode == 'single':
            r = run_battle(ua, ub, max_turns=18)
        else:
            r = run_multi_turn_battle(ua, ub, sa, sb, ANCHOR_MAP, max_battle_turns=20)
        w = r.get('winner', 'draw')
        aw += (w == 'A'); bw += (w == 'B'); dr += (w == 'draw')
    return aw, bw, dr


if __name__ == '__main__':
    print("ENV:", {k: os.environ.get(k) for k in ('PER_CELL', 'LANCHESTER_ENABLED', 'COMMAND_SIGMA_ENABLED', 'PC_BRACE_ENABLED')})
    aw, bw, dr = run_split('Horseshoe', 'Arrowhead', n=24, mode='multi')
    n = aw + bw + dr
    decA = (100 * aw / (aw + bw)) if (aw + bw) else 50.0
    print(f"H4 Cannae  Horseshoe(A) envelops Arrowhead(B)  n={n} multi:  A={aw} B={bw} draw={dr}  decA={decA:.0f}%  (history band 45-62 decisive-split, draws high)")
    print("SMOKE OK" if n == 24 else "SMOKE INCOMPLETE")
