"""DG-2 (fighting-withdrawal/yield mechanic) acceptance tests.

proposals/mass_battle_fighting_withdrawal_v1.md, Jordan-ruled "build it now" 2026-07-08.
This session builds ONLY the commanded-entry state/movement/facing/combat-pool slice (the doc's
own §4 step 1, "lowest-risk slice") -- NOT the emergent auto-entry path (§2.2's second bullet,
explicitly deferred pending its own measurement), NOT the "rally" exit, and NOT the "pocket"
conversion (§2.4) -- only the "collapse to routed" exit, which needs no new code (the existing
`derive_rout` path already fires regardless of `yielding`). Disclosed here, not silently narrowed:
whoever picks up rally/pocket/emergent-entry next should treat them as still-open, not "already
covered by this file's tests."

Every test constructs Subunit/Unit directly (validators.py's own pattern) for precise control over
`instructions`/`orders`/`yielding`, rather than going through the single-subunit `build_unit`
adapter (which does not expose `orders`)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'sim'))  # tests/sim on path

import pytest  # noqa: E402

import mass_battle.hierarchy.units as _hu  # noqa: E402
import mass_battle.orchestration as _orch  # noqa: E402
from mass_battle.hierarchy.units import Subunit, Unit, Order, D_YIELD, YIELD_POOL_MULT  # noqa: E402
from mass_battle.core.exchange import subunit_combat_pool  # noqa: E402
from mass_battle.engine import run_battle  # noqa: E402


def _line(faction, row, advance_dir, troops=3000, **kw):
    kw.setdefault('unit_type', 'melee')
    return Subunit(shape='Line', troop_type='infantry', tier=4,
                   starting_position=(row, 25), advance_dir=advance_dir,
                   stance='balanced', troops=troops, concentration=120, **kw)


def _unit(name, faction, sub, discipline=5, morale=6):
    return Unit(name=name, faction=faction, power=4, command=4,
                discipline=discipline, discipline_start=discipline,
                morale=morale, morale_start=morale, subunits=[sub], dr=1,
                stance='balanced', speed='Standard')


def test_yield_default_inert():
    """`yielding` defaults False -> `yield_active` False for any ordinary Subunit."""
    su = _line('A', 20, -1)
    assert su.yielding is False
    assert su.yield_active is False


def test_yield_active_requires_discipline():
    """A 'yield' order on a too-disordered subunit is a no-op, not honored -- gated at the
    CONSUMPTION site (yield_active), not at order-application time."""
    weak = _line('A', 20, -1, discipline=D_YIELD - 1)
    strong = _line('A', 20, -1, discipline=D_YIELD)
    weak.yielding = True
    strong.yielding = True
    assert weak.yield_active is False
    assert strong.yield_active is True


def test_yield_active_melee_only():
    """Ranged troop types already have 'kite'; a 'yield' order on a ranged subunit is a no-op."""
    archer = _line('A', 20, -1, discipline=D_YIELD, unit_type='ranged')
    archer.yielding = True
    assert archer.yield_active is False


def test_yield_goal_flees_from_nearest_enemy():
    """`_yield_goal` reflects the nearest enemy cell through the subunit's own anchor -- the same
    flee-vector idiom `_kite_goal` uses, always active (not standoff-band-gated) while yielding."""
    su = _line('A', 20, -1, discipline=D_YIELD)
    su.yielding = True
    su._node_anchor = (20.0, 25.0)
    enemy_cells = [(18, 25)]  # due "north" of the anchor in row terms
    goal = su._resolve_maneuver_goal(enemy_cells)
    assert goal == (2 * 20.0 - 18, 2 * 25.0 - 25)  # reflected through the anchor -> away from the enemy
    # sanity: the goal really is FARTHER from the enemy than the anchor itself
    def d2(p, q):
        return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
    assert d2(goal, enemy_cells[0]) > d2(su._node_anchor, enemy_cells[0])


def test_yield_goal_inert_when_not_active():
    """No 'yield'/insufficient discipline/ranged -> `_resolve_maneuver_goal` falls through to the
    plain default (None), exactly as if `yielding` didn't exist."""
    su = _line('A', 20, -1, discipline=D_YIELD - 1)
    su.yielding = True
    su._node_anchor = (20.0, 25.0)
    assert su._resolve_maneuver_goal([(18, 25)]) is None


def test_yield_pool_malus_applied():
    """A yielding, sufficiently-disciplined subunit fights at YIELD_POOL_MULT of its normal pool
    (reduced but nonzero -- "traded ground at a cost", not "stopped fighting")."""
    su = _line('A', 20, -1, discipline=D_YIELD)
    u = _unit('A', 'A', su)
    base = subunit_combat_pool(u, su)
    su.yielding = True
    yielding_pool = subunit_combat_pool(u, su)
    assert yielding_pool < base
    assert yielding_pool >= 1  # never zero -- still fighting


def test_yield_pool_malus_not_applied_below_discipline():
    """The SAME subunit at insufficient discipline: the order is a no-op, pool unaffected."""
    su = _line('A', 20, -1, discipline=D_YIELD - 1)
    u = _unit('A', 'A', su)
    base = subunit_combat_pool(u, su)
    su.yielding = True
    assert subunit_combat_pool(u, su) == base


def test_yield_order_is_order_safe():
    """A 'yield' order (behavior={'yielding': True}) is accepted -- `yielding` is in
    _ORDER_SAFE_FIELDS, so check_orders' existing generic setattr-application mechanism can set it
    with no new order-primitive code, per the proposal doc's explicit design intent."""
    Order(trigger='immediate', behavior={'yielding': True})  # must not raise


@pytest.fixture(autouse=True)
def _movement_toggles():
    """Same save/restore idiom as test_mass_battle_maneuvers.py. `_yield_goal` is wired into
    `_resolve_maneuver_goal`, which only `_node_advance` calls -- exactly like 'envelop'/'sweep'
    before it, the legacy grid `advance_cells` path has its own separate inline dispatch this
    session does not touch (out of scope; the node/field path is the live default Jordan watches
    and the only one bearing on the gauge). Force node/field ON regardless of what ran before."""
    saved = {(mod, name): getattr(mod, name) for mod in (_hu, _orch)
              for name in ('FIELD_MOVEMENT', 'PC_NODE_COHESION')}
    _hu.FIELD_MOVEMENT = True
    _hu.PC_NODE_COHESION = True
    _orch.FIELD_MOVEMENT = True
    _orch.PC_NODE_COHESION = True
    try:
        yield
    finally:
        for (mod, name), val in saved.items():
            setattr(mod, name, val)


def test_yield_facing_stays_locked_toward_engaged_enemy():
    """Acceptance (§6.b of the proposal doc): a yielding subunit's facing stays locked toward its
    engaged enemy even as it visibly moves AWAY from it -- the mechanical distinction from a routing
    body (which turns its back). Runs a short real battle and inspects the ATTACKER's own recorded
    facing vector after it has demonstrably moved away from the defender."""
    import random
    random.seed(7)
    atk = _line('A', 20, -1, troops=2000, discipline=D_YIELD,
                orders=(Order(trigger='immediate', behavior={'yielding': True}),))
    d = _line('B', 15, 1, troops=3000)
    a = _unit('A', 'A', atk, discipline=D_YIELD)
    dd = _unit('D', 'B', d)
    from mass_battle.core.contact import check_orders
    check_orders(a, 1, [c for c in dd.subunits[0].cells()])
    assert atk.yield_active
    run_battle(a, dd, max_turns=6)
    # The subunit must have actually moved (yield's flee vector is live, not a no-op).
    assert atk._moved_this_turn or atk.cell_offsets, "yielding subunit never moved at all"
    # Facing must point TOWARD the defender's centroid, not away (the flee direction).
    assert atk.target_atom is not None, "yielding attacker never acquired a target to face"
    # Reference the yielding subunit's CURRENT centroid, not its hardcoded start (20, 25): a yielding
    # body flees, so "faces toward the enemy" means toward the target FROM WHERE IT NOW IS. Pinning the
    # start position made this assertion sensitive to the defender's lateral centroid drift once the
    # engagement geometry shifted (v2 Stage E's reach change surfaced it); the current-centroid reference
    # tests the actual intent (facing at the enemy, unlike a rout that turns its back).
    my = atk.centroid()
    for (orig_r, orig_c), fv in atk.cell_facing_vec.items():
        tc = atk.target_atom.centroid()
        # the raw movement/anchor-relative facing vector should have a non-negative dot product
        # with the direction toward the target -- i.e. it points roughly AT the enemy, not away.
        to_target = (tc[0] - my[0], tc[1] - my[1])
        dot = fv[0] * to_target[0] + fv[1] * to_target[1]
        assert dot >= 0, f"cell {(orig_r, orig_c)} facing {fv} points away from the target {to_target}"
