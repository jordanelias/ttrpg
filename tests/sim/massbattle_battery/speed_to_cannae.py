"""Make a Cannae fit inside ONE engagement (12 simultaneous rounds = 72 ticks; 6 alternating = 36t),
by experimenting with unit SPEED. Multi-body envelopment is required (a lone shape can't); the
question is how fast units must move for the wrap+rout to complete in <=12 rounds, reasonably.

Levers:
  (1) cavalry-speed WINGS (historical Cannae: the envelopment was cavalry-driven). troop_type='cavalry'
      gets PC_CAVALRY_SPEED_MULT automatically.
  (2) a global movement-speed multiplier F applied to ALL infantry (patch cell_speed), to find the
      "tactical pace" at which infantry alone could do it.

Measure: routs of the enemy wedge within 6 and 12 rounds (continuous engagement), + casualty margin.
Sanity: a Line-vs-Line mirror must NOT become an instant blowout at the chosen pace.

Run:
  PER_CELL=1 LANCHESTER_ENABLED=1 COMMAND_SIGMA_ENABLED=1 PC_BRACE_ENABLED=1 \
    python -u tests/sim/massbattle_battery/speed_to_cannae.py
"""
import os, sys, random, json
for _k in ('PER_CELL', 'LANCHESTER_ENABLED', 'COMMAND_SIGMA_ENABLED', 'PC_BRACE_ENABLED'):
    os.environ.setdefault(_k, '1')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..'))
from mass_battle.config import SIDE_A_START_ROW, SIDE_B_START_ROW   # noqa: E402
import mass_battle.orchestration as O                               # noqa: E402
from mass_battle.orchestration import Subunit, Unit, run_battle      # noqa: E402

_ORIG_CELL_SPEED = O.cell_speed


def set_speed(F):
    if F == 1.0:
        O.cell_speed = _ORIG_CELL_SPEED
    else:
        O.cell_speed = lambda shape, tier, r, c, _f=F: _ORIG_CELL_SPEED(shape, tier, r, c) * _f


def sub(col, fac, tt='heavy_infantry', shape='Line', stance='balanced', instr=()):
    adv = -1 if fac == 'A' else 1; row = SIDE_A_START_ROW if fac == 'A' else SIDE_B_START_ROW
    return Subunit.of_type(tt, shape, 3, (row, col), advance_dir=adv, stance=stance, instructions=tuple(instr))


def unit(subs, name, fac, speed='Standard'):
    return Unit(name=name, faction=fac, power=4, command=5, discipline=5, discipline_start=5,
                morale=6, morale_start=6, subunits=subs, dr=1, speed=speed)


def conv_inf():   # 3 converging heavy-infantry subunits
    return unit([sub(10, 'A'), sub(6, 'A', stance='aggressive'), sub(14, 'A', stance='aggressive')], 'inf3', 'A')


def conv_cavwings():  # heavy-infantry center + two CAVALRY wings (combined arms, Cannae-shaped)
    return unit([sub(10, 'A', 'heavy_infantry'),
                 sub(6, 'A', 'cavalry', 'Arrowhead', stance='aggressive', instr=('charge',)),
                 sub(14, 'A', 'cavalry', 'Arrowhead', stance='aggressive', instr=('charge',))], 'cavwings', 'A', speed='Fast')


def wedge():  return unit([sub(8, 'B', 'heavy_infantry', 'Arrowhead')], 'wedge', 'B')
def line(fac): return unit([sub(9 if fac == 'A' else 9, fac, 'heavy_infantry', 'Line')], 'line', fac)


def routs(make_a, make_b, K, n=20):
    rb = 0; margin = []
    for s in range(n):
        random.seed(s + 1_000_000); ua = make_a(); ub = make_b(); b0 = ub.hp_max
        run_battle(ua, ub, max_turns=K)
        rb += (ub.routed and not ua.routed); margin.append(100 * (b0 - ub.hp) / b0)
    return dict(routs=rb, n=n, B_cas=round(sum(margin) / n, 1))


R6, R12, R24 = 36, 72, 144   # ticks for 6 / 12 / 24 rounds
if __name__ == '__main__':
    out = {}

    print("=== (1) cavalry-speed WINGS (natural 2x; historical Cannae) vs infantry-only, F=1 ===")
    for name, mk in (('infantry converging-3', conv_inf), ('cavalry-winged combined arms', conv_cavwings)):
        r6, r12, r24 = routs(mk, wedge, R6), routs(mk, wedge, R12), routs(mk, wedge, R24)
        out[name] = dict(r6=r6, r12=r12, r24=r24)
        print(f"  {name:30}  6r: routs {r6['routs']:>2}/20 (B_cas {r6['B_cas']:4.1f})   12r: routs {r12['routs']:>2}/20 (B_cas {r12['B_cas']:4.1f})   24r: routs {r24['routs']:>2}/20")

    print("\n=== (2) global infantry SPEED multiplier F (converging-3 infantry) ===")
    out['speed_sweep'] = {}
    for F in (1.0, 1.5, 2.0, 3.0, 4.0):
        set_speed(F)
        r6, r12 = routs(conv_inf, wedge, R6), routs(conv_inf, wedge, R12)
        out['speed_sweep'][F] = dict(r6=r6, r12=r12)
        print(f"  F={F:>3}x :  6r routs {r6['routs']:>2}/20 (B_cas {r6['B_cas']:4.1f})   12r routs {r12['routs']:>2}/20 (B_cas {r12['B_cas']:4.1f})")
    set_speed(1.0)

    print("\n=== (3) SANITY at F=2 and F=3: Line-vs-Line mirror must NOT become an instant blowout (12r) ===")
    out['mirror'] = {}
    for F in (1.0, 2.0, 3.0):
        set_speed(F)
        m = routs(lambda: line('A'), lambda: line('B'), R12)
        out['mirror'][F] = m
        print(f"  F={F:>3}x mirror Line vs Line, 12r:  A routs B {m['routs']:>2}/20  (B_cas {m['B_cas']:4.1f})  -> want ~balanced/modest, not 20/20")
    set_speed(1.0)

    json.dump({k: (v if not isinstance(v, dict) else v) for k, v in out.items()},
              open(os.path.join(HERE, 'speed_to_cannae_results.json'), 'w'), indent=1, default=str)
    print("\nwrote speed_to_cannae_results.json")
