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

Run:  PER_CELL=1 FIELD_MOVEMENT=0 PC_NODE_COHESION=0 PYTHONHASHSEED=0 python3 -m mass_battle.validators

[movement audit fix-plan step 6, ED-1096/1097] The `Run:` line above now pins FIELD_MOVEMENT/
PC_NODE_COHESION explicitly rather than leaving them at the ambient default (movement-audit
finding 1.4: since ED-1089 flipped that default to ON, a bare invocation silently measured the
DEAD node-path arm for V-ENVELOP/V-SWEEP -- the only two validators here that exercise a movement
INSTRUCTION ('envelop'/'sweep') rather than a combat mechanic. `_envelop_reach`/`_sweep_disp` below
now accept an explicit `path` ('grid'|'node') and toggle FIELD_MOVEMENT/PC_NODE_COHESION in-process
for that measurement (same "toggle in-process" idiom already used for PC_ENVELOP_PATH/PC_SWEEP);
v_envelop/v_sweep report BOTH arms, gating pass/fail on the grid arm (a real, currently-working
regression test) while the node arm is tracked separately -- see
tests/valoria/test_mass_battle_maneuvers.py, which lands the node arm as an executable, initially-
RED (xfail) CI gate: the measurement instrument fix-plan step 7 (the waypoint primitive) must turn
green, so "the maneuver works now" is never claimed again without something actually checking it.
"""
import statistics
import random
from collections import namedtuple

import mass_battle.orchestration as _orch
import mass_battle.hierarchy.units as _hu
from mass_battle.engine import Subunit, Unit, run_battle

GoalResult = namedtuple("GoalResult", "name passed measured expected anchor note")

# --- scenario fixtures (validator INPUTS, not engine mechanics) ---
_DEF_TROOPS = 3000     # [canonical: class-B test-fixture: fixed defender, one mid line]
_MAIN_TROOPS = 4000    # [canonical: class-B test-fixture: pinning main body]
_DET_TROOPS = 1500     # [canonical: class-B test-fixture: enveloping detachment]
_DEF_ROW = 15          # [canonical: class-B test-fixture: defender deploy row (faction B)]
_MAIN_ROW = 20         # [canonical: class-B test-fixture: main body deploy row, in front of the defender]
_DET_ROW = 24          # [canonical: class-B test-fixture: detachment row; joins behind the main body and spills to the flank/rear]
_COL = 25              # [canonical: class-B test-fixture: field-centre column]
_CONC = 120            # [canonical: class-B test-fixture: standard line concentration]
_TIER = 4              # [canonical: class-B test-fixture: standard tier]
_PWR = 4               # [canonical: class-B test-fixture: neutral power]
_CMD = 5               # [canonical: class-B test-fixture: neutral command]
_DISC = 5              # [canonical: class-B test-fixture: neutral discipline]
_MOR = 6               # [canonical: class-B test-fixture: neutral morale]
_DR = 1                # [canonical: class-B test-fixture: neutral damage-resist]
_SEEDS = 20            # [canonical: class-B test-fixture: aggregate sample size]
_TURNS = 60            # [canonical: class-B test-fixture: run toward a decisive outcome so the angle penalty compounds]
_FWD = 1               # advance_dir for faction B (defender), toward higher rows
_BACK = -1             # advance_dir for faction A (attacker), toward lower rows
_VULN_DISC = 4         # [canonical: class-B test-fixture: a typical (un-braced) line's discipline -- shattered by envelopment shock]
_DET_WIDE_COL = 42     # [canonical: class-B test-fixture: detachment deploy column, wide past the defender's flank (for the envelop maneuver)]


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
    return GoalResult("V-CANNAE", passed, round(delta, 4),  # [canonical: validators V-goal: round to 4 dp]
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
    return GoalResult("V-FIXING", passed, (round(delta_pin, 4), round(delta_no, 4)),  # [canonical: validators V-goal: round to 4 dp]
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
    return GoalResult("V-SHOCK", passed, round(delta, 4),  # [canonical: validators V-goal: round to 4 dp]
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
    return GoalResult("V-BRACE", passed, (round(bm_braced, 4), round(bm_line, 4)),  # [canonical: validators V-goal: round to 4 dp]
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


def _set_movement_path(path):
    """[movement audit fix-plan step 6, ED-1096/1097] Toggle which movement path new Subunits
    constructed AFTER this call will run on. 'grid' = the legacy integer path (where 'envelop'/
    'sweep' are actually implemented); 'node' = the coordinate-field path (the live default since
    ED-1089, where they are confirmed dead -- movement audit findings 1.1-1.4). Sets the module-
    level booleans on every module that star-imported its own bound copy and is read at a relevant
    call site: hierarchy.units (Subunit.__post_init__'s _init_node_state gate, advance_cells'
    early-return) and orchestration (run_battle's FIELD_MOVEMENT=>PC_NODE_COHESION assert, the
    pre-contact halt's node/legacy branch). Must be called BEFORE constructing the Subunits being
    measured -- PC_NODE_COHESION is read once at construction (__post_init__) to decide whether
    node state is initialized at all; flipping it back after construction cannot retroactively
    add node state to an atom built without it."""
    node_on = (path == 'node')
    for mod in (_hu, _orch):
        mod.FIELD_MOVEMENT = node_on
        mod.PC_NODE_COHESION = node_on


def _envelop_reach(path_on, path='grid', seeds=_SEEDS, turns=_TURNS):
    """Per-seed signed (detachment_row - defender_row). Negative => the detachment is BEHIND the
    defender (its rear, since the defender faces +row). PC_ENVELOP_PATH toggled in-process; the
    detachment always carries the 'envelop' instruction, so off = the maneuver disabled. `path`
    ('grid'|'node') selects which movement path the constructed Subunits run on -- see
    _set_movement_path."""
    _set_movement_path(path)
    _orch.PC_ENVELOP_PATH = path_on; _hu.PC_ENVELOP_PATH = path_on  # consumer (advance_cells) now lives in hierarchy.units
    diffs = []
    for s in range(seeds):
        random.seed(s)
        a = _attacker_envelop(); d = _defender('hold', _VULN_DISC)
        run_battle(a, d, max_turns=turns)
        det = a.subunits[1]; dfn = d.subunits[0]
        diffs.append(det.centroid()[0] - dfn.centroid()[0])
    return diffs


def v_envelop(path='grid', seeds=_SEEDS, turns=_TURNS):
    """GOAL (build C): a detachment ordered to ENVELOP reaches the enemy's REAR. With the maneuver it
    paths around the flank and ends at/behind the enemy (positioned to strike the rear -- the RED shock);
    without it, the detachment advances straight and never gets behind. Capability test via the
    detachment's final position relative to the defender (public).
    [canonical: Cannae 216 BC double-envelopment; Khalid at Walaja; A.8 Envelopment -- the wrap to the rear.]

    [movement audit fix-plan step 6] `path` ('grid'|'node', default 'grid') selects which movement
    path is measured -- see _set_movement_path/_envelop_reach. Default 'grid' preserves this
    validator's original, still-working regression semantics; tests/valoria/
    test_mass_battle_maneuvers.py calls this with path='node' as the live-path acceptance gate."""
    on = _envelop_reach(True, path=path, seeds=seeds, turns=turns)
    off = _envelop_reach(False, path=path, seeds=seeds, turns=turns)
    on_m = statistics.mean(on); off_m = statistics.mean(off)
    on_behind = sum(1 for x in on if x < -1.0)
    off_behind = sum(1 for x in off if x < -1.0)
    passed = (on_m < off_m - 1.0) and (on_behind > off_behind) and (off_behind == 0)
    return GoalResult("V-ENVELOP", passed, (round(on_m, 2), round(off_m, 2), on_behind, off_behind),
                      "envelop pulls the detachment to the rear (much lower row-diff, some behind) vs straight (none behind)",
                      "Cannae 216 BC; Khalid at Walaja",
                      "reaching the rear enables the RED rear shock (A+B from behind)")


def v_reform():
    """GOAL: a NON-ENGAGED unit restores +1 Discipline toward its start, gated by the
    general's Command; an engaged, routed, or Command-deficient unit does not, and with the
    flag OFF the hook is inert. Direct mechanism check on the canon Reform Phase rule.
    [canonical: mass_battle_v30.md §A.5 / Phase Reform — an unengaged unit gains +1 Discipline; the general's Command must exceed the current Discipline and be at least two (the Command-asymmetry rule); a Command of one cannot restore.]"""
    saved_flag = _orch.REFORM_CHECK_ENABLED
    saved_fc = _orch.find_contacts
    partner = _defender()  # at start (disc==start) -> never perturbed by the shared loop
    def _mk(disc, start, cmd, routed=False):
        u = _defender(disc=disc); u.discipline = disc; u.discipline_start = start
        u.command = cmd; u.routed = routed; return u
    # (label, flag_on, engaged, disc, start, cmd, routed, expected_final_disc)
    # discipline/command points are test-fixture probes of the canon gating, not engine constants.
    cases = [
        ("on_unengaged_eligible", True,  False, 3, 5, 5, False, 4),  # [canonical: validators reform test-case row] cmd5 >= 3+1 & >=2 -> +1
        ("on_cmd1_prohibited",    True,  False, 3, 5, 1, False, 3),  # Command-asymmetry: a Command of one cannot restore
        ("on_cmd_lt_disc_plus1",  True,  False, 4, 5, 4, False, 4),  # [canonical: validators reform test-case row] 4 < 4+1 -> inert
        ("on_already_at_start",   True,  False, 5, 5, 5, False, 5),  # capped at discipline_start
        ("on_engaged_blocked",    True,  True,  3, 5, 5, False, 3),  # in contact -> no reform
        ("on_routed_blocked",     True,  False, 3, 5, 5, True,  3),  # routed -> skipped
        ("off_inert",             False, False, 3, 5, 5, False, 3),  # flag OFF -> no-op
    ]
    n_ok = 0
    try:
        for label, flag_on, engaged, disc, start, cmd, routed, exp in cases:
            _orch.REFORM_CHECK_ENABLED = flag_on
            _orch.find_contacts = (lambda a, b: [object()]) if engaged else (lambda a, b: [])
            u = _mk(disc, start, cmd, routed)
            _orch.reform_check(u, partner, 1)
            n_ok += (u.discipline == exp)
    finally:
        _orch.REFORM_CHECK_ENABLED = saved_flag
        _orch.find_contacts = saved_fc
    passed = (n_ok == len(cases))
    return GoalResult("V-REFORM", passed, (n_ok, len(cases)),
                      "all gating cases correct: unengaged & Command>=Disc+1 & Command>=2 restores +1 (capped at start); engaged/routed/Command-deficient/flag-OFF inert",
                      "mass_battle_v30.md §A.5 Reform Phase; Command-asymmetry rule",
                      "default OFF preserves the calibrated baseline; opt-in for re-baseline")


_FAR_ROW = _DEF_ROW - 2   # second enemy subunit, two rows deeper than the near one, still in volley range


def _archer_pair(target_idx):
    """An archer (faction A, ranged, held) facing a two-subunit enemy -- a NEAR line and a FAR line,
    both inside volley range. target_idx=None -> no order (fires nearest); target_idx=1 -> ordered at
    the FAR subunit. Held on both sides so only the volley acts (no melee), isolating fire distribution."""
    arch = Subunit(shape='Line', troop_type='infantry', tier=_TIER,
                   starting_position=(_MAIN_ROW, _COL), advance_dir=_BACK,
                   unit_type='ranged', stance='hold', troops=_DET_TROOPS, concentration=_CONC,
                   order_target_idx=target_idx)
    A = _unit('A', 'A', [arch], 'hold')
    near = _line('B', _DEF_ROW, _FWD, _DEF_TROOPS, 'hold')
    far = Subunit(shape='Line', troop_type='infantry', tier=_TIER,
                  starting_position=(_FAR_ROW, _COL), advance_dir=_FWD,
                  unit_type='melee', stance='hold', troops=_DEF_TROOPS, concentration=_CONC)
    B = _unit('B', 'B', [near, far], 'hold')
    return A, B


def _archer_far_loss(target_idx, on, seeds=_SEEDS, turns=6):  # [canonical: validators test-fixture: short far-volley horizon]
    """Per-seed casualties inflicted on the FAR enemy subunit. PC_VOLLEY_TARGETING toggled in-process.
    Asserts the cell==hp invariant every seed -- the split (concentrate ordered / spread the rest) must
    redistribute casualties without creating or destroying any."""
    _orch.PC_VOLLEY_TARGETING = on
    losses = []
    for s in range(seeds):
        random.seed(s)
        a, b = _archer_pair(target_idx)
        far0 = sum(b.subunits[1].cell_troops.values())
        run_battle(a, b, max_turns=turns)
        far1 = sum(b.subunits[1].cell_troops.values())
        cellsum = sum(sum(su.cell_troops.values()) for su in b.subunits)
        assert abs(cellsum - b.hp) < 1, "cell==hp invariant broken under ordered volley"
        losses.append(far0 - far1)
    return losses


def v_archer():
    """GOAL (build E): archers ORDERED to a target subunit CONCENTRATE their volley casualties on it.
    Same scenario and same total fire either way -- only the FLAG differs: with PC_VOLLEY_TARGETING the
    ordered archers land their casualties on the chosen (far) subunit; without it the order is ignored and
    the fire spreads by engaged density (the prior faction-wide behaviour). Directed fire puts more on the
    target than the spread does, on every seed; the cell==hp invariant is asserted throughout, so the total
    is merely redistributed, not inflated.
    [canonical: longbow fire discipline -- Crecy/Agincourt; mass_battle §A.7 Phase 2 directed volley.]"""
    ordered = _archer_far_loss(target_idx=1, on=True)    # flag ON  -> concentrate on the far subunit
    spread = _archer_far_loss(target_idx=1, on=False)    # flag OFF -> order ignored, spreads (prior behaviour)
    worse = sum(1 for o, d in zip(ordered, spread) if o < d)
    delta = statistics.mean(ordered) - statistics.mean(spread)
    passed = (worse == 0) and (delta > 0)
    return GoalResult("V-ARCHER", passed, (round(delta, 1), worse),
                      "ordered fire concentrates MORE casualties on the target subunit than the default spread, every seed",
                      "Crecy/Agincourt longbow fire discipline; A.7 directed volley",
                      "cell==hp asserted each seed; total fire unchanged, only its distribution; flag-OFF is the byte-exact prior path")


def _attacker_sweep():
    """A single line at centre carrying the 'sweep' instruction -- the build-E lateral maneuver slides it
    to the nearer enemy flank and concentrates there (rather than holding its deployed column)."""
    su = _line('A', _MAIN_ROW, _BACK, _MAIN_TROOPS, 'balanced')
    su.instructions = ('sweep',)
    return _unit('A', 'A', [su], 'balanced')


def _sweep_disp(sweep_on, path='grid', seeds=_SEEDS, turns=_TURNS):
    """Per-seed lateral column displacement |end_col - start_col| of the sweeping unit's centroid. PC_SWEEP
    toggled in-process; the unit always carries 'sweep', so off = the maneuver disabled (straight column-local
    advance, which holds the file). `path` ('grid'|'node') selects the movement path -- see
    _set_movement_path."""
    _set_movement_path(path)
    _orch.PC_SWEEP = sweep_on; _hu.PC_SWEEP = sweep_on  # consumer (advance_cells) lives in hierarchy.units
    out = []
    for s in range(seeds):
        random.seed(s)
        a = _attacker_sweep(); d = _defender('hold', _VULN_DISC)
        c0 = a.subunits[0].centroid()[1]
        run_battle(a, d, max_turns=turns)
        c1 = a.subunits[0].centroid()[1]
        out.append(abs(c1 - c0))
    return out


def v_sweep(path='grid', seeds=_SEEDS, turns=_TURNS):
    """GOAL (build E, lateral half): a unit ordered to SWEEP marches laterally to the enemy's flank and
    concentrates there, instead of holding its deployed column. With the maneuver the body displaces sideways
    toward a flank; without it (column-local advance) it stays in its file. Capability test via the unit's
    lateral column displacement (public), on every seed.
    [canonical: oblique order / flank march -- Leuctra (Epaminondas); Leuthen 1757.]

    [movement audit fix-plan step 6] `path` ('grid'|'node', default 'grid') -- see v_envelop's
    docstring for the same convention."""
    on = _sweep_disp(True, path=path, seeds=seeds, turns=turns)
    off = _sweep_disp(False, path=path, seeds=seeds, turns=turns)
    on_m = statistics.mean(on); off_m = statistics.mean(off)
    worse = sum(1 for x, y in zip(on, off) if x < y)
    passed = (on_m > off_m + 1.0) and (worse == 0)
    return GoalResult("V-SWEEP", passed, (round(on_m, 2), round(off_m, 2)),
                      "sweep displaces the unit laterally toward a flank; straight advance holds the deployed column",
                      "oblique order / flank march -- Leuctra, Leuthen",
                      "byte-exact without the 'sweep' instruction; lateral concentration is editorial, Jordan-vetoable")


GOALS = [v_cannae, v_fixing, v_shock, v_brace, v_envelop, v_reform, v_archer, v_sweep]


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
