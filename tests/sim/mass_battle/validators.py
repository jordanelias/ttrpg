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
  * the DECISIVE collapse of an enveloped line is build B (shock) -- IMPLEMENTED here as the
    envelopment-shock reusing _charge_shock_sigma on the fixed+flanked condition; V-SHOCK/V-BRACE;
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
_VULN_DISC = 4         # [class-B test-fixture: a typical (un-braced) line's discipline -- shattered by envelopment shock]
_DET_WIDE_COL = 42     # [class-B test-fixture: detachment deploy column, wide past the defender's flank (for the envelop maneuver)]


def _line(faction, row, advance_dir, troops, stance):
    return Subunit(shape='Line', troop_type='infantry', tier=_TIER,
                   starting_position=(row, _COL), advance_dir=advance_dir,
                   unit_type='melee', stance=stance, troops=troops, concentration=_CONC)


def _unit(name, faction, subunits, stance):
    return Unit(name=name, faction=faction, power=_PWR, command=_CMD,
                discipline=_DISC, discipline_start=_DISC, morale=_MOR, morale_start=_MOR,
                subunits=subunits, dr=_DR, stance=stance, speed='Standard')


def _defender(stance='hold', disc=_DISC):
    """The line to be fixed and enveloped. Its resilience to shock is tuned by stance/discipline:
    held + disc5 = a braced, disciplined square (resists envelopment shock -- the Waterloo square);
    balanced + disc4 = a typical line (shattered). [du Picq: order and depth absorb the moral
    impulse; a loose line does not.]"""
    su = _line('B', _DEF_ROW, _FWD, _DEF_TROOPS, stance)
    return Unit(name='D', faction='B', power=_PWR, command=_CMD, discipline=disc,
                discipline_start=disc, morale=_MOR, morale_start=_MOR, subunits=[su],
                dr=_DR, stance=stance, speed='Standard')


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


def _attacker_retained(pin, fix, shock, def_stance='hold', def_disc=_DISC,
                       seeds=_SEEDS, turns=_TURNS):
    """Per-seed attacker retained-hp fraction. BOTH mechanic flags are set explicitly (the
    engine reads them at call time), so each validator isolates exactly the mechanic it tests
    on identical geometry and seeds. Attacker hp is the apt metric: A and B both reduce the
    FIXED unit's offence, so the effect surfaces as the attacker losing less."""
    _orch.PC_FIXING_FLANK = fix
    _orch.PC_ENVELOP_SHOCK = shock
    out = []
    for s in range(seeds):
        random.seed(s)
        a = _attacker(pin)
        d = _defender(def_stance, def_disc)
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
    on = _attacker_retained(pin=True, fix=True, shock=False)
    off = _attacker_retained(pin=True, fix=False, shock=False)
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
    on_pin = _attacker_retained(pin=True, fix=True, shock=False)
    off_pin = _attacker_retained(pin=True, fix=False, shock=False)
    on_no = _attacker_retained(pin=False, fix=True, shock=False)
    off_no = _attacker_retained(pin=False, fix=False, shock=False)
    delta_pin = statistics.mean(on_pin) - statistics.mean(off_pin)
    delta_no = statistics.mean(on_no) - statistics.mean(off_no)
    no_pin_inert = all(x == y for x, y in zip(on_no, off_no))
    passed = no_pin_inert and (delta_pin > delta_no)
    return GoalResult("V-FIXING", passed, (round(delta_pin, 4), round(delta_no, 4)),
                      "delta(no-pin)==0 (provably inert) and delta(pin)>delta(no-pin)",
                      "fixing-force doctrine",
                      "without a separate front-fixer the flank term cannot fire")


def v_shock():
    """GOAL (build B): the envelopment SHOCK makes envelopment DECISIVE. A unit fixed frontally
    and struck on its flank/rear cannot face the new threat; beyond A's angle disadvantage, the
    moral shock collapses it -- the attacker retains materially more strength than under A alone.
    Measured on a balanced line (the typical enveloped unit); the shock never harms the attacker
    (per seed) and is positive in aggregate.
    [canonical: Cannae 216 BC -- the pinned legions, struck front/flank/rear, broke from the shock
    of the unfaceable attack; du Picq Battle Studies -- the moral impulse, not the physical, decides.]"""
    ab = _attacker_retained(pin=True, fix=True, shock=True, def_stance='balanced', def_disc=_VULN_DISC)
    a_only = _attacker_retained(pin=True, fix=True, shock=False, def_stance='balanced', def_disc=_VULN_DISC)
    worse = sum(1 for x, y in zip(ab, a_only) if x < y)
    delta = statistics.mean(ab) - statistics.mean(a_only)
    passed = (worse == 0) and (delta > 0)
    return GoalResult("V-SHOCK", passed, round(delta, 4),
                      "delta>0 and no seed where the shock hurt the attacker",
                      "Cannae 216 BC; du Picq",
                      "B is the decisive layer over A's modest angle disadvantage")


def v_brace():
    """GOAL (build B guard): a BRACED, disciplined unit RESISTS envelopment shock (the square Ney
    could not break). The shock is conditional on disorder -- not a blanket flank insta-kill -- so
    B's marginal effect on a held+disciplined defender is smaller than on a balanced line.
    [canonical: Waterloo squares; PC_SHOCK_BRACE_FLOOR calibration -- order and depth absorb the
    moral impulse.]"""
    br_ab = _attacker_retained(pin=True, fix=True, shock=True, def_stance='hold', def_disc=_DISC)
    br_a = _attacker_retained(pin=True, fix=True, shock=False, def_stance='hold', def_disc=_DISC)
    ln_ab = _attacker_retained(pin=True, fix=True, shock=True, def_stance='balanced', def_disc=_VULN_DISC)
    ln_a = _attacker_retained(pin=True, fix=True, shock=False, def_stance='balanced', def_disc=_VULN_DISC)
    bm_braced = statistics.mean(br_ab) - statistics.mean(br_a)
    bm_line = statistics.mean(ln_ab) - statistics.mean(ln_a)
    passed = bm_braced < bm_line
    return GoalResult("V-BRACE", passed, (round(bm_braced, 4), round(bm_line, 4)),
                      "B-marginal(braced) < B-marginal(line): the square resists",
                      "Waterloo squares; brace-floor calibration",
                      "guards against B being a blanket flank insta-kill")


def _attacker_envelop():
    """Main body fixing the front + a detachment deployed WIDE (past the flank) carrying the
    'envelop' instruction -- the build-C maneuver routes it around to the enemy's rear."""
    main = _line('A', _MAIN_ROW, _BACK, _MAIN_TROOPS, 'balanced')
    det = _line('A', _MAIN_ROW, _BACK, _DET_TROOPS, 'balanced')
    det.starting_position = (_MAIN_ROW, _DET_WIDE_COL)
    det.instructions = ('envelop',)
    return _unit('A', 'A', [main, det], 'balanced')


def _envelop_reach(path_on, seeds=_SEEDS, turns=_TURNS):
    """Per-seed signed (detachment_row - defender_row). Negative => the detachment is BEHIND the
    defender (its rear, since the defender faces +row). PC_ENVELOP_PATH toggled in-process; the
    detachment always carries the 'envelop' instruction, so off = the maneuver disabled."""
    _orch.PC_ENVELOP_PATH = path_on
    diffs = []
    for s in range(seeds):
        random.seed(s)
        a = _attacker_envelop(); d = _defender('hold', _VULN_DISC)
        run_battle(a, d, max_turns=turns)
        det = a.subunits[1]; dfn = d.subunits[0]
        diffs.append(det.centroid()[0] - dfn.centroid()[0])
    return diffs


def v_envelop():
    """GOAL (build C): a detachment ordered to ENVELOP reaches the enemy's REAR. With the maneuver it
    paths around the flank and ends at/behind the enemy (positioned to strike the rear -- the RED shock);
    without it, the detachment advances straight and never gets behind. Capability test via the
    detachment's final position relative to the defender (public).
    [canonical: Cannae 216 BC double-envelopment; Khalid at Walaja; A.8 Envelopment -- the wrap to the rear.]"""
    on = _envelop_reach(True)
    off = _envelop_reach(False)
    on_m = statistics.mean(on); off_m = statistics.mean(off)
    on_behind = sum(1 for x in on if x < -1.0)
    off_behind = sum(1 for x in off if x < -1.0)
    passed = (on_m < off_m - 1.0) and (on_behind > off_behind) and (off_behind == 0)
    return GoalResult("V-ENVELOP", passed, (round(on_m, 2), round(off_m, 2), on_behind, off_behind),
                      "envelop pulls the detachment to the rear (much lower row-diff, some behind) vs straight (none behind)",
                      "Cannae 216 BC; Khalid at Walaja",
                      "reaching the rear enables the RED rear shock (A+B from behind)")


GOALS = [v_cannae, v_fixing, v_shock, v_brace, v_envelop]


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
