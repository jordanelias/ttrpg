"""Two questions:
 A) Is cavalry better modeled at 3x closing speed than 2x? Sweep PC_CAVALRY_SPEED_MULT over the
    envelopment + control scenarios and watch for overshoot (mirror must stay even; a braced wall
    must still repel; envelopment must not saturate past its band).
 B) Does INFANTRY envelop through STRUCTURE + DURATION (not speed)? Compare a lone Horseshoe vs a
    combined-arms infantry unit (held/braced center that FIXES + two 'envelop' wing subunits) over a
    PROLONGED single engagement. Hypothesis (Jordan): infantry envelops only in prolonged affairs /
    ambush, so duration + a fixing center — not speed — should let the wings bite.

Run:
  PER_CELL=1 LANCHESTER_ENABLED=1 COMMAND_SIGMA_ENABLED=1 PC_BRACE_ENABLED=1 \
    python -u tests/sim/massbattle_battery/speed_infantry_probe.py
"""
import os, sys, random, json

for _k in ('PER_CELL', 'LANCHESTER_ENABLED', 'COMMAND_SIGMA_ENABLED', 'PC_BRACE_ENABLED'):
    os.environ.setdefault(_k, '1')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))

from mass_battle.config import SIDE_A_START_ROW, SIDE_B_START_ROW   # noqa: E402
import mass_battle.orchestration as O                               # noqa: E402
from mass_battle.orchestration import Subunit, Unit, run_battle, run_multi_turn_battle  # noqa: E402

ANCHOR = {('Line', 3): 9, ('Arrowhead', 3): 8, ('Horseshoe', 3): 8}


def make_unit(shape, name, fac, troop_type='infantry', unit_type='melee', power=4, command=4,
              discipline=5, morale=6, stance='balanced', speed='Standard', instructions=()):
    adv = -1 if fac == 'A' else 1
    row = SIDE_A_START_ROW if fac == 'A' else SIDE_B_START_ROW
    su = Subunit(shape=shape, troop_type=troop_type, tier=3, starting_position=(row, ANCHOR.get((shape, 3), 10)),
                 advance_dir=adv, unit_type=unit_type, instructions=tuple(instructions))
    return Unit(name=name, faction=fac, power=power, command=command, discipline=discipline,
                discipline_start=discipline, morale=morale, morale_start=morale, subunits=[su],
                dr=1, stance=stance, speed=speed)


def decA(make_a, make_b, n=24):
    aw = bw = dr = 0
    for s in range(n):
        random.seed(s + 1_000_000)
        ua, sa = make_a(); ub, sb = make_b()
        r = run_multi_turn_battle(ua, ub, sa, sb, ANCHOR, max_battle_turns=20)
        w = r['winner']; aw += (w == 'A'); bw += (w == 'B'); dr += (w == 'draw')
    dec = aw + bw
    return dict(A=aw, B=bw, draw=dr, decA=round(100 * aw / dec, 1) if dec else 50.0,
                rawA=round(100 * aw / n, 1), draw_pct=round(100 * dr / n, 1))


# ── Part A: cavalry speed sweep ──
CAV = dict(troop_type='cavalry', speed='Fast')
SCEN = {
    'cav-envelop  (Horseshoe cav vs Line inf)  band 75-95': (
        lambda: (make_unit('Horseshoe', 'A', 'A', **CAV), 'Horseshoe'), lambda: (make_unit('Line', 'B', 'B'), 'Line')),
    'cav-mirror   (Arrowhead cav vs same)      ~even ctrl': (
        lambda: (make_unit('Arrowhead', 'A', 'A', **CAV), 'Arrowhead'), lambda: (make_unit('Arrowhead', 'B', 'B', **CAV), 'Arrowhead')),
    'cav-vs-braced(Arrowhead cav vs brace wall) rawA LOW': (
        lambda: (make_unit('Arrowhead', 'A', 'A', **CAV), 'Arrowhead'),
        lambda: (make_unit('Line', 'B', 'B', stance='hold', discipline=8, instructions=('brace',)), 'Line')),
    'h4-cav       (Horseshoe cav vs Arrowhead cav) band 45-62': (
        lambda: (make_unit('Horseshoe', 'A', 'A', **CAV), 'Horseshoe'), lambda: (make_unit('Arrowhead', 'B', 'B', **CAV), 'Arrowhead')),
}


def part_a():
    print("=== Part A: cavalry speed sweep (PC_CAVALRY_SPEED_MULT) ===")
    out = {}
    for mult in (2.0, 3.0):
        O.PC_CAVALRY_SPEED_MULT = mult
        print(f"\n  -- mult = {mult}x --")
        out[mult] = {}
        for label, (ma, mb) in SCEN.items():
            r = decA(ma, mb, n=24)
            metric = f"rawA={r['rawA']:5.1f}" if 'braced' in label else f"decA={r['decA']:5.1f}"
            print(f"     {label:52} {metric}  draws={r['draw_pct']:4.1f}%")
            out[mult][label] = r
    O.PC_CAVALRY_SPEED_MULT = 2.0
    return out


# ── Part B: infantry envelopment via structure + duration ──
def lone_horseshoe(fac='A'):
    return make_unit('Horseshoe', 'lone-HS', fac, command=5)


def combined_arms_inf(fac='A'):
    """A held/braced CENTER that fixes + two 'envelop' wing subunits (the parallel hierarchy:
    unit=strategy 'envelop', subunit=tactic {Anvil, Envelop, Envelop}, cell=behaviour {brace, advance})."""
    adv = -1 if fac == 'A' else 1
    row = SIDE_A_START_ROW if fac == 'A' else SIDE_B_START_ROW
    center = Subunit.of_type('heavy_infantry', 'Line', 3, (row, 10), advance_dir=adv,
                             instructions=('brace', 'hold'), stance='hold')
    lwing = Subunit.of_type('heavy_infantry', 'Line', 3, (row, 5), advance_dir=adv,
                            instructions=('envelop',), stance='aggressive')
    rwing = Subunit.of_type('heavy_infantry', 'Line', 3, (row, 15), advance_dir=adv,
                            instructions=('envelop',), stance='aggressive')
    return Unit(name='combined-arms', faction=fac, power=4, command=5, discipline=5,
                discipline_start=5, morale=6, morale_start=6, subunits=[center, lwing, rwing], dr=1)


def enemy_line(fac='B'):
    adv = -1 if fac == 'A' else 1
    row = SIDE_A_START_ROW if fac == 'A' else SIDE_B_START_ROW
    su = Subunit.of_type('heavy_infantry', 'Line', 3, (row, 10), advance_dir=adv)
    return Unit(name='enemy', faction=fac, power=4, command=4, discipline=5, discipline_start=5,
                morale=6, morale_start=6, subunits=[su], dr=1)


def measure_engagement(make_a, durations=(18, 50, 100), n=12):
    res = {}
    for K in durations:
        bcas = []; brouts = 0; arouts = 0
        for s in range(n):
            random.seed(s + 1_000_000)
            ua = make_a(); ub = enemy_line('B')
            b0 = ub.hp_max
            run_battle(ua, ub, max_turns=K)        # ONE prolonged engagement (positions persist)
            bcas.append(100 * (b0 - ub.hp) / b0 if b0 else 0)
            brouts += ub.routed; arouts += ua.routed
        res[K] = dict(B_cas_pct=round(sum(bcas) / len(bcas), 1), B_routs=brouts, A_routs=arouts, n=n)
    return res


def part_b():
    print("\n=== Part B: infantry envelopment via STRUCTURE + DURATION (no speed boost) ===")
    print("  enemy = heavy-infantry Line; measure B casualty% and routs over a prolonged single engagement")
    lone = measure_engagement(lone_horseshoe)
    comb = measure_engagement(combined_arms_inf)
    for K in (18, 50, 100):
        print(f"  ticks={K:>3}: lone-Horseshoe  B_cas={lone[K]['B_cas_pct']:5.1f}%  B_routs={lone[K]['B_routs']}/{lone[K]['n']}"
              f"   |  combined-arms  B_cas={comb[K]['B_cas_pct']:5.1f}%  B_routs={comb[K]['B_routs']}/{comb[K]['n']}")
    return dict(lone_horseshoe=lone, combined_arms=comb)


if __name__ == '__main__':
    a = part_a()
    b = part_b()
    with open(os.path.join(HERE, 'speed_infantry_results.json'), 'w') as fh:
        json.dump({'part_a_cav_speed': {str(k): v for k, v in a.items()}, 'part_b_infantry': b}, fh, indent=1)
    print("\nwrote speed_infantry_results.json")
