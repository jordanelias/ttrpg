"""D1 verification — zone+actor-gated charge-recoil.
Expect: shieldwall(brace+hold) vs Line drops from +38.5/decA96 to ~even (HOLD, not annihilate);
cavalry vs BRACED wall still REPELLED (recoil still fires for a cavalry charger); mirror unchanged."""
import os, sys, random
for _k in ('PER_CELL', 'LANCHESTER_ENABLED', 'COMMAND_SIGMA_ENABLED', 'PC_BRACE_ENABLED'):
    os.environ.setdefault(_k, '1')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..'))
from mass_battle.config import SIDE_A_START_ROW, SIDE_B_START_ROW   # noqa: E402
import mass_battle.orchestration as O                               # noqa: E402
from mass_battle.orchestration import Subunit, Unit, run_battle      # noqa: E402

PACE, K = 2.0, 144
_ORIG = O.cell_speed
O.cell_speed = lambda s, t, r, c, _f=PACE: _ORIG(s, t, r, c) * _f
ANCHOR = {('Line', 3): 9, ('Arrowhead', 3): 8}


def mk(shape, fac, troop='heavy_infantry', unit_type='melee', stance='balanced', instr=(), disc=5):
    adv = -1 if fac == 'A' else 1; row = SIDE_A_START_ROW if fac == 'A' else SIDE_B_START_ROW
    su = Subunit.of_type(troop, shape, 3, (row, ANCHOR.get((shape, 3), 10)), advance_dir=adv,
                         unit_type=unit_type, stance=stance, instructions=tuple(instr))
    return Unit(name=fac, faction=fac, power=4, command=5, discipline=disc, discipline_start=disc,
                morale=6, morale_start=6, subunits=[su], dr=1, stance=stance,
                speed='Fast' if troop == 'cavalry' else 'Standard')


def run(make_a, make_b, n=24):
    aw = bw = dr = 0; margin = []
    for s in range(n):
        random.seed(s + 1_000_000); ua = make_a(); ub = make_b(); a0, b0 = ua.hp_max, ub.hp_max
        run_battle(ua, ub, max_turns=K)
        w = 'A' if (ub.routed and not ua.routed) else 'B' if (ua.routed and not ub.routed) else 'draw'
        aw += w == 'A'; bw += w == 'B'; dr += w == 'draw'
        margin.append((100 * (b0 - ub.hp) / b0) - (100 * (a0 - ua.hp) / a0))
    dec = aw + bw
    return dict(decA=round(100 * aw / dec, 1) if dec else 50.0, rawA=round(100 * aw / n, 1),
                draw=dr, cas=round(sum(margin) / n, 1))


ctrl = lambda: mk('Line', 'B')
print("D1 verification (fixed structure, n=24):")
print("  shieldwall(brace+hold) vs Line  :", run(lambda: mk('Line', 'A', stance='hold', instr=('brace', 'hold')), ctrl),
      " [was +38.5/decA96 -> expect ~even]")
print("  cavalry(Arrowhead) vs BRACED wall:", run(lambda: mk('Arrowhead', 'A', troop='cavalry', stance='aggressive'),
                                                  lambda: mk('Line', 'B', stance='hold', disc=8, instr=('brace',))),
      " [C2 repel -> expect cav rawA LOW]")
print("  mirror Line vs Line             :", run(lambda: mk('Line', 'A'), ctrl), " [expect ~+3.6, unchanged]")
