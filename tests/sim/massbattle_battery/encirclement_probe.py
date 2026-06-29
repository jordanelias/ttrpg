"""Is infantry envelopment a MULTI-BODY (encirclement) phenomenon, not a single-shape one?

The engagement-length sweep showed a lone Horseshoe LOSES to a wedge no matter how long it runs
(concentration out-attrites frontage). Reason hypothesis: the engine's encirclement penalty
(ns -= ENCIRCLEMENT_PENALTY*SIGMA_PER_D) fires only when an atom is engaged by >=2 enemy atoms
(orchestration ~L1927). In a 1-subunit-vs-1-subunit match it can NEVER fire -> frontage has no
"being-surrounded" channel, so the wedge's density wins. So a real Cannae should need MULTIPLE
converging subunits (the unit/strategy level), exactly per the unit>subunit>cell hierarchy.

Test: A = THREE heavy-infantry subunits converging (cols 7/10/13, all advancing) vs B = one wedge.
Compare to the lone Horseshoe baseline, over a 12-round continuous engagement, at ENCIRCLEMENT_PENALTY
= 1 (baseline) and 3 (boosted). Win = rout; also report casualty margin (enemy% - own%).

Run:
  PER_CELL=1 LANCHESTER_ENABLED=1 COMMAND_SIGMA_ENABLED=1 PC_BRACE_ENABLED=1 \
    python -u tests/sim/massbattle_battery/encirclement_probe.py
"""
import os, sys, random, json

for _k in ('PER_CELL', 'LANCHESTER_ENABLED', 'COMMAND_SIGMA_ENABLED', 'PC_BRACE_ENABLED'):
    os.environ.setdefault(_k, '1')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))

from mass_battle.config import SIDE_A_START_ROW, SIDE_B_START_ROW   # noqa: E402
import mass_battle.orchestration as O                               # noqa: E402
from mass_battle.orchestration import Subunit, Unit, run_battle      # noqa: E402

ROW_A, ROW_B = SIDE_A_START_ROW, SIDE_B_START_ROW


def _hi(col, fac, shape='Line', instr=(), stance='balanced'):
    adv = -1 if fac == 'A' else 1
    row = ROW_A if fac == 'A' else ROW_B
    return Subunit.of_type('heavy_infantry', shape, 3, (row, col), advance_dir=adv,
                           instructions=tuple(instr), stance=stance)


def unit(subs, name, fac, command=5):
    return Unit(name=name, faction=fac, power=4, command=command, discipline=5, discipline_start=5,
                morale=6, morale_start=6, subunits=subs, dr=1)


def lone_horseshoe():   # H4 baseline enveloper
    return unit([_hi(8, 'A', 'Horseshoe')], 'lone-HS', 'A')


def converging_three():  # multi-subunit envelopment: center + two flanking bodies, all engaging
    return unit([_hi(10, 'A'), _hi(6, 'A', stance='aggressive'), _hi(14, 'A', stance='aggressive')],
                'converging-3', 'A')


def wedge_B():
    return unit([_hi(8, 'B', 'Arrowhead')], 'wedge', 'B')


def run(make_a, K=72, n=20):
    aw = bw = dr = 0; margin = []
    for s in range(n):
        random.seed(s + 1_000_000)
        ua = make_a(); ub = wedge_B()
        a0, b0 = ua.hp_max, ub.hp_max
        run_battle(ua, ub, max_turns=K)
        w = ('A' if (ub.routed and not ua.routed) else 'B' if (ua.routed and not ub.routed) else 'draw')
        aw += (w == 'A'); bw += (w == 'B'); dr += (w == 'draw')
        margin.append((100 * (b0 - ub.hp) / b0) - (100 * (a0 - ua.hp) / a0))
    dec = aw + bw
    return dict(decA=round(100 * aw / dec, 1) if dec else 50.0, draw_pct=round(100 * dr / n, 1),
                cas_margin=round(sum(margin) / n, 1), A=aw, B=bw, routsB=aw)


if __name__ == '__main__':
    print("12-round (72t) continuous engagement vs a single WEDGE; band-relevant signal = enveloper wins / positive margin\n")
    out = {}
    for pen in (1, 3):
        O.ENCIRCLEMENT_PENALTY = pen
        print(f"  -- ENCIRCLEMENT_PENALTY = {pen} --")
        lo = run(lone_horseshoe); cv = run(converging_three)
        out[pen] = dict(lone_horseshoe=lo, converging_three=cv)
        print(f"     lone Horseshoe (1 subunit) : decA={lo['decA']:5.1f}  draws={lo['draw_pct']:5.1f}%  cas-margin={lo['cas_margin']:+5.1f}  routs-wedge={lo['routsB']}/20")
        print(f"     converging 3 subunits      : decA={cv['decA']:5.1f}  draws={cv['draw_pct']:5.1f}%  cas-margin={cv['cas_margin']:+5.1f}  routs-wedge={cv['routsB']}/20")
    O.ENCIRCLEMENT_PENALTY = 1
    with open(os.path.join(HERE, 'encirclement_results.json'), 'w') as fh:
        json.dump(out, fh, indent=1)
    print("\nwrote encirclement_results.json")
