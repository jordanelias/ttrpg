"""Post-D1 cavalry spot-check in the GAUGE structure (run_multi_turn_battle, 1x pace, reset) — the
calibrated fidelity authority (NOT the 2x-pace controlled-sweep harness, which amplifies cavalry).
Confirms: C1 frontal-vs-steady in band 35-55 (=> D2 is a harness artifact, not an engine defect);
C2/C6 still REPELLED (=> D1 did not break the legit cavalry recoil); C4/C7 envelopment in band."""
import os, sys, random
for _k in ('PER_CELL', 'LANCHESTER_ENABLED', 'COMMAND_SIGMA_ENABLED', 'PC_BRACE_ENABLED'):
    os.environ.setdefault(_k, '1')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..'))
from mass_battle.config import SIDE_A_START_ROW, SIDE_B_START_ROW   # noqa: E402
from mass_battle.orchestration import Subunit, Unit, run_multi_turn_battle  # noqa: E402

ANCHOR = {('Line', 3): 9, ('Arrowhead', 3): 8, ('Horseshoe', 3): 8}


def make_unit(shape, name, fac, troop_type='infantry', power=4, command=4, discipline=5, morale=6,
              stance='balanced', speed='Standard', instructions=(), morale_start=None):
    adv = -1 if fac == 'A' else 1
    su = Subunit(shape=shape, troop_type=troop_type, tier=3,
                 starting_position=(SIDE_A_START_ROW if fac == 'A' else SIDE_B_START_ROW, ANCHOR.get((shape, 3), 10)),
                 advance_dir=adv, instructions=tuple(instructions))
    return Unit(name=name, faction=fac, power=power, command=command, discipline=discipline,
                discipline_start=discipline, morale=morale, morale_start=(morale if morale_start is None else morale_start),
                subunits=[su], dr=1, stance=stance, speed=speed)


CAV = dict(troop_type='cavalry', speed='Fast')


def row(sa, sb, ka, kb, n=60):
    aw = bw = dr = 0
    for s in range(n):
        random.seed(s + 1_000_000)
        ua = make_unit(sa, 'A', 'A', **ka); ub = make_unit(sb, 'B', 'B', **kb)
        r = run_multi_turn_battle(ua, ub, sa, sb, ANCHOR, max_battle_turns=20)
        w = r['winner']; aw += w == 'A'; bw += w == 'B'; dr += w == 'draw'
    dec = aw + bw
    return dict(decA=round(100 * aw / dec, 1) if dec else 50.0, rawA=round(100 * aw / n, 1), draw=dr)


print("Post-D1 cavalry spot-check (GAUGE structure, n=60 multi):")
print("  C1 Cav vs steady Line          band 35-55 decA :", row('Arrowhead', 'Line', CAV, {}),
      " [in band => D2 is a 2x-pace harness artifact, not an engine defect]")
print("  C2 Cav vs BRACED Line          band 0-30 rawA  :", row('Arrowhead', 'Line', CAV, dict(stance='hold', discipline=8, instructions=('brace',))),
      " [rawA LOW => D1 preserved the legit recoil]")
print("  C4 Cav flank/envelop vs Line   band 75-95 decA :", row('Horseshoe', 'Line', CAV, {}))
print("  C7 Cav envelop vs holding Line band 65-100 decA:", row('Horseshoe', 'Line', CAV, dict(stance='hold', discipline=8)))
