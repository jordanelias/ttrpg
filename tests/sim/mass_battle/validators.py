"""Historical-goal validators for the mass_battle engine.

TOP-DOWN by construction: each validator asserts that the engine's EMERGENT outcome on a
constructed scenario matches a historical / theoretical GOAL, using only PUBLIC battle
outputs (winner, retained casualties/hp, rout). A validator never imposes a mechanic and
never orchestrates an outcome -- it builds a deployment, runs the real engine, and checks
the result against an expected band. If a validator fails, the MECHANIC is wrong, not the
validator. This is the inverse of a unit test on internals: it shapes the goal and lets
the bottom-up mechanics answer to it.

Scope -- build A (atomized fixing-force flank, subunit-scale): a subunit engaged on its
FRONT by a separate enemy body is fixed and cannot wheel as a body, so a detachment that
bears on its flank/rear lands the zone penalty and the fixed unit fights worse. A is the
ANGLE DISADVANTAGE of envelopment and is modest by design -- it reduces the fixed unit's
offence, it does not by itself shatter it. Two companions are out of A's scope and are
documented here so the bands below are read honestly:
  * the DECISIVE cohesion / morale collapse of an enveloped line is build B (shock);
  * reliable detachment rear-reach is build C -- today a detachment approaching directly
    into the rear or flank forms NO contact pair, so envelopment emerges only via the
    frontal mass spilling around a fixed defender (the scenario used below).

Run:  PER_CELL=1 PYTHONHASHSEED=0 python3 -m mass_battle.validators
"""
import statistics
import random
from collections import namedtuple

import mass_battle.orchestration as _orch
from mass_battle.engine import Subunit, Unit, run_battle

GoalResult = namedtuple("GoalResult", "name passed measured expected anchor note")

# --- scenario fixtures (validator INPUTS, not engine mechanics) ---
_DEF_TROOPS = 3000     # [class-B test-fixture: fixed defender, one mid line]
_MAIN_TROOPS = 4000    # [class-B test-fixture: pinning main body]
_DET_TROOPS = 1500     # [class-B test-fixture: enveloping detachment]
_DEF_ROW = 15          # [class-B test-fixture: defender deploy row (faction B)]
_MAIN_ROW = 20         # [class-B test-fixture: main body deploy row, in front of the defender]
_DET_ROW = 24          # [class-B test-fixture: detachment row; joins behind the main body and spills to the flank/rear]
_COL = 25              # [class-B test-fixture: field-centre column]
_CONC = 120            # [class-B test-fixture: standard line concentration]
_TIER = 4              # [class-B test-fixture: standard tier]
_PWR = 4               # [class-B test-fixture: neutral power]
_CMD = 5               # [class-B test-fixture: neutral command]
_DISC = 5              # [class-B test-fixture: neutral discipline]
_MOR = 6               # [class-B test-fixture: neutral morale]
_DR = 1                # [class-B test-fixture: neutral damage-resist]
_SEEDS = 20            # [class-B test-fixture: aggregate sample size]
_TURNS = 60            # [class-B test-fixture: run toward a decisive outcome so the angle penalty compounds]
_FWD = 1               # advance_dir for faction B (defender), toward higher rows
_BACK = -1             # advance_dir for faction A (attacker), toward lower rows


def _line(faction, row, advance_dir, troops, stance):
    return Subunit(shape='Line', troop_type='infantry', tier=_TIER,
                   starting_position=(row, _COL), advance_dir=advance_dir,
                   unit_type='melee', stance=stance, troops=troops, concentration=_CONC)


def _unit(name, faction, subunits, stance):
    return Unit(name=name, faction=faction, power=_PWR, command=_CMD,
                discipline=_DISC, discipline_start=_DISC, morale=_MOR, morale_start=_MOR,
                subunits=subunits, dr=_DR, stance=stance, speed='Standard')


def _defender():
    """A single line, held (cannot advance) -- the unit to be fixed and enveloped."""
    return _unit('D', 'B', [_line('B', _DEF_ROW, _FWD, _DEF_TROOPS, 'hold')], 'hold')


def _attacker(pin):
    """pin=True  -> main body (fixes the defender's front) + detachment (envelops).
    pin=False -> detachment ALONE: the defender is not fixed and is free to face it."""
    det = _line('A', _DET_ROW, _BACK, _DET_TROOPS, 'balanced')
    if pin:
        main = _line('A', _MAIN_ROW, _BACK, _MAIN_TROOPS, 'balanced')
        subs = [main, det]
    else:
        subs = [det]
    return _unit('A', 'A', subs, 'balanced')


def _attacker_retained(pin, mechanic_on, seeds=_SEEDS, turns=_TURNS):
    """Per-seed attacker retained-hp fraction. The fixing-force flank mechanic is toggled
    in-process (the engine reads the module flag at call time), so the on/off runs share
    identical geometry and seeds -- the only difference is the mechanic. Attacker hp is the
    apt metric: A reduces the FIXED unit's offence, so its effect surfaces as the attacker
    losing less, not as the defender's hp falling faster."""
    _orch.PC_FIXING_FLANK = mechanic_on
    out = []
    for s in range(seeds):
        random.seed(s)
        a = _attacker(pin)
        d = _defender()
        run_battle(a, d, max_turns=turns)
        out.append(a.hp / a.hp_max if a.hp_max else 0.0)
    return out


def v_cannae():
    """GOAL: enveloping a FIXED unit confers an advantage. The fixed-and-flanked unit fights
    worse, so the enveloping attacker retains more strength -- on every seed at least as
    much, and more in aggregate. Emergent, judged only on public hp.
    [canonical: Cannae 216 BC -- a pinned centre enveloped on both flanks and rear is
    destroyed out of proportion to the numbers; du Picq -- the telling blow is the one the
    fixed line cannot turn to meet.]"""
    on = _attacker_retained(pin=True, mechanic_on=True)
    off = _attacker_retained(pin=True, mechanic_on=False)
    worse = sum(1 for x, y in zip(on, off) if x < y)
    delta = statistics.mean(on) - statistics.mean(off)
    passed = (worse == 0) and (delta > 0)
    return GoalResult("V-CANNAE", passed, round(delta, 4),
                      "delta>0 and no seed where envelopment hurt the attacker",
                      "Cannae 216 BC; du Picq",
                      "modest by design: A is the angle disadvantage; decisive collapse is build B")


def v_fixing():
    """GOAL: the flank bonus is CONDITIONAL on the pin. A detachment on the flank/rear of a
    NON-fixed unit is refused -- the unit wheels to face it -- so the mechanic has exactly
    zero effect; only a unit fixed frontally by a separate body suffers the penalty.
    [canonical: the fixing-force doctrine -- fix, then flank; an unfixed line simply turns
    to meet the detachment, and the unseen-attack advantage never arises.]"""
    on_pin = _attacker_retained(pin=True, mechanic_on=True)
    off_pin = _attacker_retained(pin=True, mechanic_on=False)
    on_no = _attacker_retained(pin=False, mechanic_on=True)
    off_no = _attacker_retained(pin=False, mechanic_on=False)
    delta_pin = statistics.mean(on_pin) - statistics.mean(off_pin)
    delta_no = statistics.mean(on_no) - statistics.mean(off_no)
    no_pin_inert = all(x == y for x, y in zip(on_no, off_no))
    passed = no_pin_inert and (delta_pin > delta_no)
    return GoalResult("V-FIXING", passed, (round(delta_pin, 4), round(delta_no, 4)),
                      "delta(no-pin)==0 (provably inert) and delta(pin)>delta(no-pin)",
                      "fixing-force doctrine",
                      "without a separate front-fixer the flank term cannot fire")


GOALS = [v_cannae, v_fixing]


def run_all():
    results = []
    for g in GOALS:
        r = g()
        results.append(r)
        print(f"[{'PASS' if r.passed else 'FAIL'}] {r.name}: measured={r.measured} "
              f"| expected: {r.expected} | anchor: {r.anchor}")
        print(f"        note: {r.note}")
    return results


if __name__ == '__main__':
    run_all()
