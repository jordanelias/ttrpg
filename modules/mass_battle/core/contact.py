"""modules.mass_battle.core.contact — targeting + contact detection (the contact-event layer).
Stage-1 behaviour-frozen extract from orchestration.py (assign_targets, resolve_cross_side_contention,
find_contacts, count_engagements_per_atom). Depends on geometry (_oriented/octagon/facing) + config +
math + duck-typed unit/atom methods, and on hierarchy.units for its flags and body helpers, read as
attributes of the module at call time (`_u.FIELD_MOVEMENT`), not copied; units imports nothing from
here, so there is no cycle. Re-imported by orchestration via
star-import so resolve_engagements/run_battle and every caller are unchanged.
[canonical: mass_battle_v30.md §A.7 manoeuvre/contact]"""
from engine.dice_engine import fmath
import modules.mass_battle.hierarchy.units as _u
from modules.mass_battle.config import *
from modules.mass_battle.geometry import *
from types import SimpleNamespace
from engine.dice_engine import draw as _draw
from engine.dice_engine.dice_engine import Degree, degree_from_net, degree_label      # the one degree ladder (A-5)
from modules.mass_battle.resolution import trace_event   # the module's one trace call: a no-op outside a `tracing()` block
from engine.dice_engine.sigma_leverage import LEVEL_SIGMA, net_boost, pool_of, roll_net_continuous  # the one sampler, boost and pool rule (A-5, A-6)
from modules.mass_battle import rngsource

__all__ = ['check_orders', 'assign_targets', 'resolve_cross_side_contention', 'find_contacts', 'count_engagements_per_atom']


def _visible_enemy_cells(sub, enemy_cells):
    """[A2, ED-MB-0067 Part A -- squad-engagement synthesis, "Order conditions limited to what the
    unit can know"] Filter `enemy_cells` down to the ones `sub` can actually perceive: within its
    facing cone, angle-to-facing <= FOV_HALF_DEG (105 deg -- ALL of GREEN (<45) and YELLOW (45-90)
    PLUS 15 degrees of RED (90-105); NOT the GREEN+YELLOW boundary itself, which is 90 -- see
    geometry.octagon_angle's own zone cutoffs). Composed on geometry.octagon_angle
    for the angle itself (not a re-implementation of its cos/acos math). Facing falls back to
    (advance_dir, 0) when the sub-unit's node facing is unset, the same fallback find_contacts'
    head_a/head_b computation and _resolve_maneuver_goal's envelop-wheel both already use.

    The facing-cone check is conditioned on `MB_FACING_MODEL and MB_FACING_FOV_GATE` -- the SAME two flags
    orchestration.py's own FOV-blind-arc gate composes on, rather than a second, parallel, always-on perception
    check. With either flag off, every enemy cell counts as visible (MB_FACING_MODEL is the master switch for
    every facing-gated mechanic). Both default ON but MB_FACING_MODEL is pinned OFF in every golden-battery mode
    (tools/ci_golden_modes_check.py's FIELD_PINS), which is what makes this mechanism structurally inert there.

    There is no standalone sight-range distance (see config.py's note on MB_SIGHT_RANGE).

    Order conditions are the ONLY thing this filters -- assign_targets' own targeting (which enemy a
    sub-unit fights once contact is joined) is untouched; this is command/perception (what a
    standing order can react to), not combat-target selection."""
    if not enemy_cells:
        return enemy_cells
    # [movement-substrate review 06 — contact cluster precedent] Read at CALL TIME, not import-bound
    # -- same reasoning as find_contacts' own _u.FIELD_MOVEMENT reads in this file: a runtime flag
    # flip (e.g. validators.py) stays consistent.
    if not (_u.MB_FACING_MODEL and _u.MB_FACING_FOV_GATE):
        return enemy_cells
    facing = getattr(sub, '_node_facing', None) or (sub.advance_dir, 0)
    my = sub.centroid()
    out = []
    for e in enemy_cells:
        _, angle_deg = octagon_angle(e, my, facing)
        if angle_deg <= FOV_HALF_DEG:
            out.append(e)
    return out


# ─── THE OBEDIENCE DRAW (27A-4) ──────────────────────────────────────────────────────────────────────────────
# Whether a fired order takes effect: at once, late, or not at all (27_MB_A section 4). Read at call time off `ORDER_OBEY` (config's
# one dict; `arm: off` is today's certainty). Every number there is a seed; the form is what is decided.

_OBEYED, _LATE, _NOT_CARRIED_OUT = 'obeyed', 'late', 'not carried out'
#: The record a side with no commander record is rolled on: `COMMAND_DEFAULT` as the score, no dice added, no levels (27A control).
_DEFAULT_ROLLER = SimpleNamespace(person='', score=COMMAND_DEFAULT, addends=0, levels=0.0, post=None, fed_by=())
_PSEUDO_FIELDS = ('fire_signal', 'feign_retreat')    # order keys that are not a posture (see `check_orders`)


def _holds(sub, key, value):
    """True when `sub` is already in the posture `key: value` an order would set."""
    return (sub.eff_stance if key == 'stance' else getattr(sub, key, None)) == value


def _order_kind(order, sub):
    """The kind of an order, the key of `ORDER_OBEY['step']` (26_MASS_BATTLE_maneuver_orders section 1): `keep` (the posture it sets is the
    one the unit holds: nothing is asked), `restrain` (a signalled halt: `stance: hold` on a signal), `signal` (any other change
    on a signal) or `change`. The triggers `enemy_broken` and `in_lull`, and a `recall` order, do not exist here (B20), so
    `restrain` is reached by a signalled halt only."""
    posture = {k: v for k, v in order.behavior.items() if k not in _PSEUDO_FIELDS}
    if all(_holds(sub, k, v) for k, v in posture.items()):
        return 'keep'
    if order.trigger.startswith('signal:'):
        return 'restrain' if posture.get('stance') == 'hold' else 'signal'
    return 'change'


def _slot(army, sub):
    return next(i for i, u in enumerate(army.units) if u is sub)


def _post_cell(army, name):
    """Where the commander is: the centroid of the unit named `name`, or, with none, the army's rear centre (the rearmost unit's
    row, the mean column of the units)."""
    if name is not None:
        for u in army.units:
            if u.name == name:
                return u.centroid()
        raise ValueError(f"commander_post {name!r} names no unit of the army {army.name!r}")
    cells = [u.centroid() for u in army.units]
    adv = army.units[0].advance_dir
    return (min((r for r, _c in cells), key=lambda r: r * adv), sum(c for _r, c in cells) / len(cells))


def _distance_steps(roller, sub, army):
    """A distance step: the whole number of `obey.reach` cells between the roller's post and the unit's centroid, beyond the
    first. An officer is with his unit: none."""
    if roller is sub.officer_record and roller is not None:
        return 0
    post = _post_cell(army, roller.post if roller.post is not None else army.commander_post)
    here = sub.centroid()
    return max(0, int(fmath.hypot(here[0] - post[0], here[1] - post[1]) / ORDER_OBEY['reach']) - 1)


def _in_contact(sub, enemy_cells):
    """True when one of the unit's cells has an enemy cell on it or beside it."""
    enemy = set(enemy_cells)
    return any((r + dr, c + dc) in enemy for r, c in sub.cells() for dr in (-1, 0, 1) for dc in (-1, 0, 1))


def _obey_terms(order, roller, sub, army, enemy_cells):
    """`(pool, levels, obstacle)` of the draw (27_MB_A section 4), or None when the order's kind asks nothing (`step: none`)."""
    spec = ORDER_OBEY
    step = spec['step'][_order_kind(order, sub)]
    if step == 'none':
        return None
    signalled = order.trigger.startswith('signal:')
    waiting = sum(1 for u in army.units if any(o.trigger == order.trigger for o in u.orders[u._order_idx:])) if signalled else 0
    obstacle = (army.obey_task + step
                + (spec['distance'] * _distance_steps(roller, sub, army) if spec['distance'] else 0)
                + spec['across'] * max(0, waiting - 3)
                + (spec['unsteady'] if sub.eff_discipline <= 1 else 0)
                + (spec['in_contact'] if spec['in_contact'] and _in_contact(sub, enemy_cells) else 0))
    # A-25 [ASSUMPTION as the source marks it]: a body with Discipline 4 or more raises its roller by a `minor` level.
    levels = roller.levels + (LEVEL_SIGMA['minor'] if sub.eff_discipline >= 4 else 0.0)
    return pool_of(roller.score, roller.addends, army.obey_pool_add, army.obey_pool_floor), levels, obstacle


def _roller_for(army, sub, source):
    """The persons who give `sub` an order, one draw each (27_MB_A section 3: an order is drawn once for each person who has to
    pass it on to the unit). A `standing` order or a `signal`: the unit's officer, else the commander. An `improvised` one: the
    commander, then, for an officered unit, the officer once more. A side with no commander record rolls `_DEFAULT_ROLLER`."""
    if source not in ('standing', 'signal', 'improvised'):
        raise ValueError(f"_roller_for: source {source!r} is not standing, signal or improvised")
    commander = army.commander if army.commander is not None else _DEFAULT_ROLLER
    officer = sub.officer_record
    if officer is None:
        return (commander,)
    return (commander, officer) if source == 'improvised' else (officer,)


def obey(order, roller, sub, army, t, link=0, enemy_cells=()):
    """Whether `roller`, passing `order` to `sub`, gets it carried out: 'obeyed', 'late' or 'not carried out' (27_MB_A section 4).
    At `arm: off`, and for an order that asks nothing (`keep`), 'obeyed' with NO draw consumed. Otherwise one draw on the one sampler and
    the one ladder, keyed on (the field's key, tick, army, unit, order, link) and purpose `obey` (A-30), so the draws do not depend
    on who issued the order or on any other draw the field makes."""
    if ORDER_OBEY['arm'] != 'on':
        return _OBEYED
    terms = _obey_terms(order, roller, sub, army, enemy_cells)
    if terms is None:
        return _OBEYED
    pool, levels, obstacle = terms
    key = _draw.H2(rngsource.get().key, f"obey|{t}|{army.faction}|{army.name}|{_slot(army, sub)}|{sub._order_idx}|{link}")
    net = roll_net_continuous(pool, rng=_draw.seeded(key)) + net_boost(levels, pool)
    band = degree_from_net(net, obstacle)
    trace_event('draw', tick=t, side=army.faction, unit=getattr(sub, 'name', '?'), kind='obey', band=degree_label(net, obstacle))
    if band in (Degree.OVERWHELMING, Degree.SUCCESS):
        return _OBEYED
    return _LATE if band is Degree.PARTIAL else _NOT_CARRIED_OUT


def _verdict(order, sub, army, t, enemy_cells):
    """`obey` over every link of the order; the first that does not obey stops it. `(verdict, that link's roller)`."""
    source = 'signal' if order.trigger.startswith('signal:') else 'standing'
    for link, roller in enumerate(_roller_for(army, sub, source)):
        verdict = obey(order, roller, sub, army, t, link, enemy_cells)
        if verdict != _OBEYED:
            return verdict, roller
    return _OBEYED, None


def _obey_blocked(sub, t):
    """True while an order the draw left not carried out is in the phase it was left in: it is drawn again at most once a phase."""
    return bool(sub._obey_block) and t >= sub._obey_block and (t - 1) // TICKS_PER_PHASE == (sub._obey_block - 1) // TICKS_PER_PHASE


def _misread(sub, order):
    """The one case the data can express: `order` came by signal and the unit holds another pending order on a DIFFERENT signal. That
    order is taken off the queue and returned, to be answered now; `order` stays pending. None when there is none."""
    if not order.trigger.startswith('signal:'):
        return None
    for j in range(sub._order_idx + 1, len(sub.orders)):
        other = sub.orders[j]
        if other.trigger.startswith('signal:') and other.trigger != order.trigger:
            sub.orders = sub.orders[:j] + sub.orders[j + 1:]
            return other
    return None


def check_orders(unit, t, enemy_cells):
    """[Stage C] Fire each subunit's pending orders (Unit.orders, a Tuple[Order,...]) whose trigger
    condition is met this tick. Called once per tick per side, BEFORE assign_targets (an order's
    behavior dict may itself set target_condition/target_delay_ticks/etc., so orders must land first).
    Orders fire in sequence -- a later order cannot fire before an earlier one's trigger is satisfied.
    Reuses the exact 'kind:value' trigger-parsing idiom already in production for target_condition's
    'in_range:N' (see assign_targets, immediately below) -- no new parsing pattern.

    Triggers: 'immediate' | 'tick:N' (t >= N) | 'enemy_range:D' (within D of the nearest OBSERVED
    enemy cell -- filtered per-sub-unit through _visible_enemy_cells, see A2) | 'ally_at:D' (within D
    of order.waypoint_ref's centroid -- the allied Unit to watch) | 'own_strength:FRAC' (this
    subunit's own casualty fraction) | 'signal:NAME' (A4 -- NAME is in `unit.fired_signals`).
    behavior may also set 'fire_signal': NAME (A4) -- a pseudo-field, not a real Unit attribute:
    once THIS order's own trigger condition fires, NAME is added to the issuing Army's
    fired_signals, the one real order-writable path to release a 'signal:NAME' trigger from inside
    a battle. behavior may also set 'feign_retreat': bool (C4, ED-MB-0067 Part C / ED-MB-0071) --
    another pseudo-field: sets the issuing Army's `.feigned` (PP-256), pre-declaring a Feigned
    Retreat before the unit's normal rout check runs -- the order-writable path that mechanic (fully
    built in orchestration.py) was missing.

    [27A-4, B19.05] An order whose trigger holds is then DRAWN (`obey`) when `ORDER_OBEY['arm']` is 'on': obeyed -> applied now; late
    -> held `1 +` distance steps ticks (`Unit._order_due`), or, for an order on a signal while the unit holds another pending order on a
    different signal, MISREAD (the other is answered now, `_misread`); not carried out -> stays pending, not drawn again in the same
    phase (`Unit._obey_block`). Each link that has to pass the order on draws once (`_roller_for`). At 'off' nothing is drawn.

    Byte-exact: Unit.orders defaults to () -- the while loop body never executes for any existing
    Unit, the identical safe-default pattern as the already-shipped target_delay_ticks: int = 0; and `arm: off` applies every fired
    order as before."""
    for sub in unit.units:
        while sub._order_idx < len(sub.orders):
            order = sub.orders[sub._order_idx]
            fired = False
            carried = bool(sub._order_due) and t >= sub._order_due      # [27A-4] a late order, now due: applied without a new draw
            if sub._order_due and not carried:
                break                                                    # a late order is still on its way
            if carried:
                sub._order_due = 0
                fired = True
            elif order.trigger == 'immediate':
                fired = True
            elif order.trigger.startswith('tick:'):
                fired = t >= int(order.trigger.split(':', 1)[1])
            elif order.trigger.startswith('enemy_range:'):
                D = float(order.trigger.split(':', 1)[1])
                # [A2, ED-MB-0067 Part A] Perception-limited: an enemy cell only counts toward this
                # trigger if `sub` can actually see it (facing cone, when the facing model is on --
                # see _visible_enemy_cells) -- was every enemy cell unconditionally, omniscient
                # regardless of facing, in every configuration including the facing model's own OFF.
                visible = _visible_enemy_cells(sub, enemy_cells)
                if visible:
                    my = sub.centroid()
                    fired = min(fmath.hypot(my[0] - er, my[1] - ec) for (er, ec) in visible) <= D
            elif order.trigger.startswith('ally_at:'):
                D = float(order.trigger.split(':', 1)[1])
                if order.waypoint_ref is not None:
                    my = sub.centroid(); wp = order.waypoint_ref.centroid()
                    fired = fmath.hypot(my[0] - wp[0], my[1] - wp[1]) <= D
            elif order.trigger.startswith('own_strength:'):
                # [ED-MB-0030] fire once THIS subunit is attrited to <= FRAC of its spawn count — a unit
                # reacting to its OWN losses (withdraw a spent body / commit a weakened one / brace when
                # thinned). Uses the same _start_troops spawn denominator the §A.4 casualty triggers +
                # per-subunit survival fraction already use; no new state. A subunit that never thins that far keeps
                # the order pending forever (by design, same as an unmet enemy_range).
                frac = float(order.trigger.split(':', 1)[1])
                start = getattr(sub, '_start_troops', 0) or 0
                fired = start > 0 and (sub.troop_total() / start) <= frac
            elif order.trigger.startswith('signal:'):
                # [A4, ED-MB-0067 Part A] Go-code: fires once NAME has been added to the issuing
                # Army's `fired_signals` set (see Army.fired_signals and Order's own docstring). A
                # signal never fired keeps the order pending forever, the same "correctly never
                # met" semantics every other trigger already has (an unmet enemy_range, an
                # unreached own_strength threshold).
                name = order.trigger.split(':', 1)[1]
                fired = name in unit.fired_signals
            if not fired:
                break
            if not carried and ORDER_OBEY['arm'] == 'on':
                if _obey_blocked(sub, t):
                    break
                verdict, roller = _verdict(order, sub, unit, t, enemy_cells)
                if verdict == _NOT_CARRIED_OUT:
                    sub._obey_block = t
                    break
                if verdict == _LATE:
                    answered = _misread(sub, order)
                    if answered is None:
                        sub._order_due = t + 1 + (_distance_steps(roller, sub, unit) if ORDER_OBEY['distance'] else 0)
                    else:
                        _apply_order(unit, sub, answered, t)
                    break
            _apply_order(unit, sub, order, t)
            sub._order_idx += 1


def _apply_order(unit, sub, order, t):
    """Apply one fired order's behaviour to `sub` (the one site an order takes effect; `check_orders` calls it once the order is
    due, obeyed, late or misread). Its body is the loop that was inline in `check_orders`, unmoved but for its indent."""
    for k, v in order.behavior.items():
        if k == 'fire_signal':
            # [A4, ED-MB-0067 Part A] Not a real Unit attribute -- a PSEUDO-field consumed here directly, adding
            # the name to the ISSUING Army's fired_signals set (per-Army, see Army.fired_signals' own note) instead of
            # being setattr-ed onto the subunit. This is the one real, order-writable path to fire a 'signal:'
            # trigger from inside a battle: once THIS order's own trigger condition is met (any kind), it releases
            # every other pending order (on any subunit of this same Army) watching for the same name -- WITHIN THIS
            # SAME tick's check_orders call if that other subunit's own turn through the `for sub in unit.units`
            # loop below has not yet been taken, otherwise on the next call. Unit ITERATION ORDER decides which of
            # the two happens, and no messenger latency is modelled (out of scope for A4) -- so "at most one tick's
            # delay, never more" is the honest guarantee, not "always next call".
            unit.fired_signals.add(v)
            continue
        if k == 'feign_retreat':
            # [C4, ED-MB-0067 Part C / ED-MB-0071] Same shape as fire_signal immediately above: not a real Unit
            # attribute, so it is set on the ISSUING ARMY instead -- PP-256's Feigned Retreat is an Army-wide tactic
            # (Army.feigned), not a per-subunit one. This is the trigger for PP-256's resolution machinery
            # (feigned_retreat_recognized / feigned_retreat_check / resolve_feigned_retreat, all in orchestration.py).
            unit.feigned = bool(v)
            continue
        if k == 'stance':
            sub._stance_explicit = True   # [MB-04] an Order's stance (even 'balanced') beats a role keyword
        setattr(sub, k, v)
    # [A1, ED-MB-0067 Part A] Clamp a freshly-assigned route to Jordan's ruled path-length
    # budget (0.5*speed*max-ticks) THE MOMENT it is assigned, using the sub-unit's position
    # at THIS tick as the route's start point -- see Unit._clamp_route_to_budget. Applying
    # this here (not inside _resolve_route_goal, which reads the route fresh every tick
    # without re-deriving it) means the budget is a fixed planning bound set at order-issue
    # time, not one that silently grows if the sub-unit is later shoved backward by combat
    # contention. Inert whenever 'route' is not one of the fields this order sets.
    #
    # The resume index is resolved ONCE here (`order.behavior.get('_route_idx', 0)`, not read back off
    # `sub._route_idx` after setattr already applied it) and threaded explicitly into BOTH the clamp call
    # (`start_idx=`, so a resume-partway order's already-passed legs are never measured against the budget)
    # and the cursor assignment immediately after, so the two can never disagree about which index this
    # order resumes at.
    if 'route' in order.behavior:
        _resume_idx = order.behavior.get('_route_idx', 0)
        sub.route = sub._clamp_route_to_budget(sub.route, start_idx=_resume_idx)
        sub._route_idx = _resume_idx
        # [F2] A fresh/re-issued route must not inherit a stalled-waypoint tick count left over from whatever
        # the sub-unit was previously chasing (see _resolve_route_goal's stall-breaker): an index COLLISION (old
        # and new route resuming at the same idx) would otherwise carry the old count onto an unrelated
        # waypoint.
        sub._route_wait_ticks = 0
        sub._route_wait_idx = _resume_idx
    # [ED-1095] Track when 'brace' most recently BECAME present via an order (vs. having been
    # present since construction, stamped 0 in __post_init__) -- resolution._subunit_braced
    # requires a full tick since this stamp before treating the subunit as braced. Reset to -1
    # on removal so a later re-brace gets its own fresh delay rather than reusing a stale stamp.
    if 'brace' in sub.instructions:
        if sub._brace_since_tick < 0:
            sub._brace_since_tick = t
    else:
        sub._brace_since_tick = -1




def assign_targets(unit_a, unit_b):
    """Assign target_atom per subunit every tick.
    Priority: delay countdown > order_target_idx (direct by index) > target_condition.
    Conditions: 'nearest'(default) | 'weakest'(fewest remaining troops) | 'in_range:N'(hold until within N).
    Delay: target_delay_ticks=N holds the subunit N ticks before first activation (one-shot countdown)."""
    def _pick(atom, enemies):
        if not enemies: return None
        if atom.target_delay_ticks > 0:
            atom.target_delay_ticks -= 1
            return None                                          # subunit holds this tick
        if atom.order_target_idx is not None and atom.order_target_idx < len(enemies):
            return enemies[atom.order_target_idx]               # direct: fixed index
        cond = atom.target_condition or 'nearest'
        if cond == 'nearest':
            my = atom.centroid()
            return min(enemies, key=lambda e: fmath.hypot(my[0]-e.centroid()[0], my[1]-e.centroid()[1]))
        elif cond == 'weakest':
            return min(enemies, key=lambda e: sum(e.cell_troops.values()) if e.cell_troops else 0)
        elif cond.startswith('in_range:'):
            R = float(cond.split(':', 1)[1])
            my = atom.centroid()
            nearest = min(enemies, key=lambda e: fmath.hypot(my[0]-e.centroid()[0], my[1]-e.centroid()[1]))
            d = fmath.hypot(my[0]-nearest.centroid()[0], my[1]-nearest.centroid()[1])
            return nearest if d <= R else None                   # hold until in range
        else:
            my = atom.centroid()
            return min(enemies, key=lambda e: fmath.hypot(my[0]-e.centroid()[0], my[1]-e.centroid()[1]))
    for atom in unit_a.units: atom.target_atom = _pick(atom, unit_b.units)
    for atom in unit_b.units: atom.target_atom = _pick(atom, unit_a.units)

# ─── CONTACTS ────────────────────────────────────────────────────────────────

# [canonical: Jordan design — speed-priority cell contention; historical: Crécy/Agincourt timing, Leuctra oblique order, hoplite equal-speed combat resolution]
def resolve_cross_side_contention(unit_a, unit_b):
    """Cross-side cell contention — strict speed-differential resolution.

    Rule (Jordan design): "if they were to occupy the same cell, then the troop with higher speed gets
    priority for taking up that adjacent cell while the other remains in place."

    Implementation, for each contested abs position (cells from BOTH sides):
      - Skip if both sides have only static cells (stale contention)
      - If a_speed > b_speed: A wins, B loser-cells that moved this turn revert to their pre-move snapshot
        (didn't advance into A's space)
      - If b_speed > a_speed: symmetric
      - Tied speed: NO MOVEMENT-BASED RESOLUTION. Cells stay at the contested position; combat resolves
        via find_contacts + engagement damage (equal-speed meetings, e.g. phalanx against phalanx, are
        decided by the push, not by movement priority).

    Size and random tiebreakers from Jordan's spec are NOT applied: random tiebreakers per contested
    position per turn add noise that does not model anything historical. Charge-through (cavalry past
    static infantry) and end-of-phase displacement are not implemented.

    Citation: see preceding canonical comment.
    """
    if _u.FIELD_MOVEMENT:
        # ⚠ [ED-MB-0061] Co-location on the field path is NOT guaranteed impossible: 875 DEEP cross-side body
        # interpenetrations (obb_overlap with penetration depth >= 0.1) were measured over 140 historical-scale
        # snapshots, and tests/valoria/test_obb_contact_toi.py fails under MB_FACING_MODEL=1 ("opposing cell
        # BODIES interpenetrated after a commit"), because the TOI certificate is issued for a heading that
        # _commit_cell_position then REWRITES (see hierarchy/units.py's resolve_toi_and_commit and the ED-MB-0061
        # fix plan R2). This function is a no-op on the field path (cross-side resolution belongs to the TOI
        # solve), so nothing here may be relied on as a guarantee that co-location cannot occur. The OFF/grid
        # path below does the full speed-priority resolution.
        return 0

    def collect(unit):
        """abs_pos -> [(subunit, orig_coord, contention_speed)]"""
        result = {}
        for su in unit.units:
            op = _oriented(su)
            for orig_r, orig_c, or_r, or_c in op:
                ar = (su.starting_position[0] + or_r
                      + su.cell_offsets.get((orig_r, orig_c), 0) * su.advance_dir)
                ac = (su.starting_position[1] + or_c
                      + su.cell_offsets_c.get((orig_r, orig_c), 0))
                if MB_NODE_COHESION and hasattr(su, '_node_pos'):
                    _pr, _pc = su._node_pos.get((orig_r, orig_c), (0.0, 0.0))
                    # [migration H] file-bin the column on ON so the contested-set intersection tests
                    # co-location on the SAME file-cell grid as cells()/find_contacts (the ratified
                    # 'contested grid cell = unit of contested ground' model), not raw-float equality
                    # (which almost never coincides). OFF = verbatim int(round). Toggles at call time.
                    ar, ac = (int(round(_pr)), int(round(_pc / _u.COL_WIDTH))) if _u.FIELD_MOVEMENT else (int(round(_pr)), int(round(_pc)))
                # Contention speed: only counts if cell moved this turn
                speed = (su.cell_last_speed.get((orig_r, orig_c), 0)
                         if (orig_r, orig_c) in su._moved_this_turn
                         else 0)
                result.setdefault((ar, ac), []).append((su, (orig_r, orig_c), speed))
        return result

    a_pos = collect(unit_a)
    b_pos = collect(unit_b)
    contested = set(a_pos.keys()) & set(b_pos.keys())
    n_resolved = 0
    for pos in contested:
        a_cells = a_pos[pos]
        b_cells = b_pos[pos]
        # Each side's representative speed is its highest at this position
        a_speed = max(sp for _, _, sp in a_cells)
        b_speed = max(sp for _, _, sp in b_cells)
        # Skip stale contention — neither moved into this position this turn
        if a_speed == 0 and b_speed == 0:
            continue
        # Strict speed differential only. Equal-speed meetings stay co-located
        # (combat resolves via engagement, not movement priority).
        if a_speed > b_speed:
            winner = 'A'
        elif b_speed > a_speed:
            winner = 'B'
        else:
            continue  # tied speed → combat resolves, no movement adjustment
        losers = b_cells if winner == 'A' else a_cells
        for su, oc, _ in losers:
            if oc in su._moved_this_turn:
                # Loser moved this turn → revert to pre-move snapshot.
                # Historical: "the other remains in place" — slower cell
                # didn't actually advance to the contested cell; it stays at
                # the position it held at the start of the turn.
                su.cell_offsets[oc] = su._prev_offsets.get(oc, 0)
                su.cell_offsets_c[oc] = su._prev_offsets_c.get(oc, 0)
                su.cell_facing_vec[oc] = su._prev_facings.get(oc, (su.advance_dir, 0))
                if MB_NODE_COHESION and hasattr(su, '_node_pos'):
                    su._node_pos[oc] = su._node_prev_pos.get(oc, su._node_pos.get(oc, (0.0, 0.0)))
                n_resolved += 1
            # Loser that didn't move: nothing to revert. The mover (winner) is
            # already at this position; both cells now occupy it. This is the
            # cavalry-charge-through case (handled separately when implemented).
    return n_resolved


def find_contacts(unit_a, unit_b):
    # Toggles read at CALL TIME (not import-bound) so a runtime flag flip stays consistent across modules.
    # [movement-substrate review 06 — contact cluster]
    if _u.FIELD_MOVEMENT:
        # [Stage A] The continuous-field halt (_node_advance) now stops cells at standoff() -- not at
        # Chebyshev<=1 -- so contact must fire at the SAME radius, or cells halt at 2-3 lattice units
        # while contact still only fires at <=1 (out of sync). Takes priority over FIELD_CONTACT (a
        # narrower, separate int-round-snap refinement that predates this fix and is untouched here).
        return _find_contacts_standoff(unit_a, unit_b)
    if not _u.FIELD_CONTACT:
        pairs = []
        a_cells = {id(a): set(a.cells()) for a in unit_a.units}
        b_cells = {id(b): set(b.cells()) for b in unit_b.units}
        for atom_a in unit_a.units:
            for atom_b in unit_b.units:
                ca = a_cells[id(atom_a)]
                cb = b_cells[id(atom_b)]
                contact_cells_a, contact_cells_b, contact_cols = [], [], set()
                for (ra, c) in ca:
                    for (rb, cb_) in cb:
                        if abs(ra-rb) <= 1 and abs(c-cb_) <= 1:
                            contact_cells_a.append((ra, c))
                            contact_cells_b.append((rb, cb_))
                            contact_cols.add((c + cb_) // 2)
                if contact_cols:
                    pairs.append({"atom_a": atom_a, "atom_b": atom_b,
                                   "a_cells": contact_cells_a, "b_cells": contact_cells_b,
                                   "cols": list(contact_cols)})
        return pairs
    return _find_contacts_field(unit_a, unit_b)


def _cell_radius(atom):
    """Half the max lattice extent of an atom's footprint (min 0.5) — a per-atom contact radius for the
    FIELD_CONTACT centroid bound. [movement-substrate review 06 — contact cluster]"""
    op = _oriented(atom)
    rows = [r for r, c, _o, _p in op]
    cols = [c for r, c, _o, _p in op]
    if not rows:
        return 0.5
    ext = max(max(rows) - min(rows), max(cols) - min(cols)) + 1
    return max(0.5, ext / 2.0)


def _find_contacts_standoff(unit_a, unit_b):
    """[Stage A] FIELD_MOVEMENT ON: contact fires at the same standoff() radius the halt uses, on true
    floats (cells_float(), no snapping) -- so contact and halt never drift out of sync. Returned
    a_cells/b_cells are snapped to the same (rank, file) convention _node_advance/orchestration.py
    already use for halted_cells matching (int(round(r)), int(round(c/COL_WIDTH))) -- only the contact
    PREDICATE is continuous; the reported cell identities stay on the existing snap convention."""
    pairs = []
    # Each cell is a circular body (CellBody) whose weapon reach extends its FRONT along its own heading; contact
    # fires on reach_reaches (a's reach body meets b's body, or b's meets a's). The bodies are built by
    # _u.cell_bodies_for, index-aligned with cells_float() and heading/reach-identical to the bodies
    # resolve_toi_and_commit stops on, so contact and the collision stop share one touch surface exactly.
    af = {id(a): (a.cells_float(), _u.cell_bodies_for(a, _u.reach_for(a.troop_type))) for a in unit_a.units}
    bf = {id(b): (b.cells_float(), _u.cell_bodies_for(b, _u.reach_for(b.troop_type))) for b in unit_b.units}
    for atom_a in unit_a.units:
        fa, bodies_a = af[id(atom_a)]
        for atom_b in unit_b.units:
            fb, bodies_b = bf[id(atom_b)]
            # Sets, not lists: the engagement envelope is wide enough that one cell can meet several enemy cells at
            # once, which would otherwise append the SAME snapped identity multiple times and over-count stamina drain
            # downstream (orchestration.py sums len(a_cells) directly). Converted to sorted lists at the end for
            # deterministic output.
            contact_cells_a, contact_cells_b, contact_cols = set(), set(), set()
            # [v2 Stage D, ED-MB-0013] Collect the ENGAGED cell boxes (index-deduped) alongside the
            # snapped cell identities. The snapped (rank, file) identities stay -- they key the
            # formation-lattice casualty/density/stamina substrate (distribute_casualties, col_grid,
            # _defender_depth), a discrete troop-block identity, NOT a live-position integer (I3's
            # defensible-quantization carve-out). What Stage D removes is the integer FRONTAGE MAGNITUDE:
            # the engaged boxes below feed engaged_frontage() -> a CONTINUOUS front-overlap width that
            # replaces len(set(int_col)) in the Lanchester term (the last integer on the live contact
            # path, per backwards_analysis.md).
            eng_bodies_a, eng_bodies_b = [], []
            seen_a, seen_b = set(), set()
            for ia, ((ar, ac), body_a) in enumerate(zip(fa, bodies_a)):
                for ib, ((br, bc), body_b) in enumerate(zip(fb, bodies_b)):
                    # Cheap reject: a's reach body reaches b's body only if their centres are within the two radii plus
                    # the longer reach (exact bound, never skips a pair that engages). Far pairs skip the test in O(1).
                    _lim = 2.0 * _u.CELL_RADIUS + max(body_a.reach_front, body_b.reach_front)
                    if (ar - br) * (ar - br) + (ac - bc) * (ac - bc) >= _lim * _lim:
                        continue
                    if reach_reaches(body_a, body_b):
                        contact_cells_a.add((int(round(ar)), int(round(ac / _u.COL_WIDTH))))
                        contact_cells_b.add((int(round(br)), int(round(bc / _u.COL_WIDTH))))
                        contact_cols.add(round(((ac + bc) / 2.0) / _u.COL_WIDTH))
                        if ia not in seen_a:
                            seen_a.add(ia); eng_bodies_a.append(body_a)
                        if ib not in seen_b:
                            seen_b.add(ib); eng_bodies_b.append(body_b)
            if contact_cols:
                # Representative frontage axis per side = perpendicular to the atom's live facing
                # (matches _cell_heading's fallback chain: node facing, else advance_dir).
                head_a = getattr(atom_a, '_node_facing', None) or (atom_a.advance_dir, 0)
                head_b = getattr(atom_b, '_node_facing', None) or (atom_b.advance_dir, 0)
                a_front = engaged_frontage(eng_bodies_a, eng_bodies_b, head_a)
                b_front = engaged_frontage(eng_bodies_b, eng_bodies_a, head_b)
                pairs.append({"atom_a": atom_a, "atom_b": atom_b,
                               "a_cells": sorted(contact_cells_a), "b_cells": sorted(contact_cells_b),
                               "cols": sorted(contact_cols),
                               "a_front": a_front, "b_front": b_front})
    return pairs


def _find_contacts_field(unit_a, unit_b):
    """FIELD_CONTACT ON: contact on the promoted floats. Each atom's cells_float() is snapped to int(round())
    here (NOT pre-snapped at cells()), then the SAME append-per-adjacent-pair Chebyshev<=1 loop runs on the
    snapped cells — so the contacting SET reconstruction is identical IN KIND to the OFF path. ca_snap/cb_snap
    are SETS (matching OFF's set(a.cells()) dedup) so round-colliding float cells do not multiply-count.
    At CONTACT_REACH=0.0 this reduces exactly to OFF adjacency. [movement-substrate review 06 — contact cluster]
    NOTE: reach>0 widening of the SET predicate is UNSPECIFIED and pending Jordan; ships reach=0.0 only."""
    _reach = _u.CONTACT_REACH  # exercised only when a ratified non-zero reach lands; 0.0 => OFF adjacency
    pairs = []
    af = {id(a): a.cells_float() for a in unit_a.units}
    bf = {id(b): b.cells_float() for b in unit_b.units}
    for atom_a in unit_a.units:
        fa = af[id(atom_a)]
        ca_snap = set((int(round(r)), int(round(c))) for (r, c) in fa)
        for atom_b in unit_b.units:
            fb = bf[id(atom_b)]
            cb_snap = set((int(round(r)), int(round(c))) for (r, c) in fb)
            contact_cells_a, contact_cells_b, contact_cols = [], [], set()
            for (ra, c) in ca_snap:
                for (rb, cb_) in cb_snap:
                    if abs(ra-rb) <= 1 and abs(c-cb_) <= 1:
                        contact_cells_a.append((ra, c))
                        contact_cells_b.append((rb, cb_))
                        if _u.FIELD_MOVEMENT:
                            contact_cols.add(round(((c + cb_) / 2.0) / _u.COL_WIDTH))  # file index of the meeting column
                        else:
                            contact_cols.add((c + cb_) // 2)
            if contact_cols:
                pairs.append({"atom_a": atom_a, "atom_b": atom_b,
                               "a_cells": contact_cells_a, "b_cells": contact_cells_b,
                               "cols": list(contact_cols)})
    return pairs

def count_engagements_per_atom(pairs):
    counts = {}
    for p in pairs:
        counts[id(p["atom_a"])] = counts.get(id(p["atom_a"]), 0) + 1
        counts[id(p["atom_b"])] = counts.get(id(p["atom_b"]), 0) + 1
    return counts
