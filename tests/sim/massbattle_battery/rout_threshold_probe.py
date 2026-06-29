"""Decisive separation: does a MULTI-BODY envelopment (3 converging subunits) that already out-attrites
a wedge by +17..+25 pts EVER convert that into a ROUT given more rounds? If yes -> the fix is purely
round-budget (with multi-body structure). If it never routs despite a huge casualty margin -> the
morale/rout model cannot convert envelopment pressure and must be wired (the deepest bottleneck).
"""
import os, sys, random, json
for _k in ('PER_CELL', 'LANCHESTER_ENABLED', 'COMMAND_SIGMA_ENABLED', 'PC_BRACE_ENABLED'):
    os.environ.setdefault(_k, '1')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..'))
from mass_battle.config import SIDE_A_START_ROW, SIDE_B_START_ROW   # noqa: E402
from mass_battle.orchestration import Subunit, Unit, run_battle      # noqa: E402


def hi(col, fac, shape='Line', stance='balanced'):
    adv = -1 if fac == 'A' else 1; row = SIDE_A_START_ROW if fac == 'A' else SIDE_B_START_ROW
    return Subunit.of_type('heavy_infantry', shape, 3, (row, col), advance_dir=adv, stance=stance)


def converging(): return Unit(name='c3', faction='A', power=4, command=5, discipline=5, discipline_start=5,
                              morale=6, morale_start=6, dr=1,
                              subunits=[hi(10, 'A'), hi(6, 'A', stance='aggressive'), hi(14, 'A', stance='aggressive')])
def wedge(): return Unit(name='w', faction='B', power=4, command=4, discipline=5, discipline_start=5,
                         morale=6, morale_start=6, dr=1, subunits=[hi(8, 'B', 'Arrowhead')])


out = {}
for rounds in (12, 18, 24, 36, 48):
    K = rounds * 6; routsB = 0; margin = []
    for s in range(20):
        random.seed(s + 1_000_000); ua = converging(); ub = wedge(); b0 = ub.hp_max
        run_battle(ua, ub, max_turns=K)
        routsB += (ub.routed and not ua.routed); margin.append(100 * (b0 - ub.hp) / b0)
    out[rounds] = dict(routs_wedge=routsB, B_cas_pct=round(sum(margin) / len(margin), 1))
    print(f"  {rounds:>2} rounds ({K:>3}t): converging-3 routs wedge {routsB:>2}/20   B_casualties={out[rounds]['B_cas_pct']:5.1f}%")
json.dump(out, open(os.path.join(HERE, 'rout_threshold_results.json'), 'w'), indent=1)
print("wrote rout_threshold_results.json")
