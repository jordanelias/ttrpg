"""DG-2 fighting-withdrawal residuals — ED-MB-0024 (proposals/mass_battle_fighting_withdrawal_v1.md).

ED-MB-0005 shipped the yield STATE + COMMANDED entry. This covers the three explicitly-deferred residuals:
  §2.2 EMERGENT auto-entry  — a disciplined subunit under casualty pressure enters yielding on its own.
  §2.4 RALLY exit           — a yielding subunit whose morale recovered reverts at the turn-break lull.
  §2.4 POCKET exit          — a yielding subunit with nowhere to give ground holds, malus removed.

All three are GATED OFF by default (PC_YIELD_EMERGENT / PC_YIELD_RALLY / PC_YIELD_POCKET) -> inert and
byte-exact; the emergent path in particular has the largest blast radius (§4.3)."""
import importlib
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'sim'))

import pytest  # noqa: E402


def _reload(**flags):
    for k in ('PC_YIELD_EMERGENT', 'PC_YIELD_RALLY', 'PC_YIELD_POCKET'):
        os.environ[k] = '1' if flags.get(k) else '0'
    import mass_battle.config as C
    importlib.reload(C)
    import mass_battle.core.exchange as X
    importlib.reload(X)
    import mass_battle.core.state as S
    importlib.reload(S)
    import mass_battle.hierarchy.units as U
    importlib.reload(U)
    import mass_battle.engine as E
    importlib.reload(E)
    import mass_battle.orchestration as O
    importlib.reload(O)
    return C, X, S, U, E, O


# ── §2.2 EMERGENT auto-entry ────────────────────────────────────────────────────────────────────────
def _pressured_pair(E, discipline=5):
    ua = E.build_unit('Line', 3, 'A', 'A', 20, discipline=discipline)
    ub = E.build_unit('Line', 3, 'B', 'B', 20)
    ua.hp = 0.4 * ua.hp_max  # cohesion 0.4 < 0.50 -> the §A.4 casualty trigger fires
    return ua, ub


def test_emergent_entry_on_disciplined_subunit():
    """ON: a disciplined (>=D_YIELD) subunit crossing the frac<0.50 casualty trigger enters yielding."""
    _, _, S, _, E, _ = _reload(PC_YIELD_EMERGENT=True)
    ua, ub = _pressured_pair(E, discipline=5)
    assert not ua.subunits[0].yielding
    S.morale_check_phase(ua, ub, 0)
    assert ua.subunits[0].yielding is True, "disciplined pressured subunit must enter yielding"


def test_emergent_skips_low_discipline():
    """ON: a subunit below D_YIELD erodes/routs exactly as today — it does NOT enter yielding."""
    _, X, S, _, E, _ = _reload(PC_YIELD_EMERGENT=True)
    ua, ub = _pressured_pair(E, discipline=X.D_YIELD - 1)
    S.morale_check_phase(ua, ub, 0)
    assert ua.subunits[0].yielding is False, "sub-D_YIELD subunit must not auto-yield"


def test_emergent_gate_off_is_inert():
    """OFF (default): the casualty trigger never sets yielding — rout dynamics unchanged (byte-exact)."""
    _, _, S, _, E, _ = _reload(PC_YIELD_EMERGENT=False)
    ua, ub = _pressured_pair(E, discipline=5)
    S.morale_check_phase(ua, ub, 0)
    assert ua.subunits[0].yielding is False, "OFF: emergent entry must be inert"


# ── §2.4 RALLY exit ─────────────────────────────────────────────────────────────────────────────────
def test_rally_reverts_recovered_yielding_subunit():
    """ON: at the between-turn lull a yielding subunit with healthy morale reverts to normal combat."""
    C, _, _, _, E, O = _reload(PC_YIELD_RALLY=True)
    ua = E.build_unit('Line', 3, 'A', 'A', 20)  # morale 6 == start -> >= 0.75*start
    ua.subunits[0].yielding = True
    O.between_turn_recovery(ua)
    assert ua.subunits[0].yielding is False, "recovered morale must rally the subunit"


def test_rally_keeps_pressured_yielding_subunit():
    """ON: a yielding subunit still below the rally morale fraction stays yielding (no premature reform)."""
    C, _, _, _, E, O = _reload(PC_YIELD_RALLY=True)
    ua = E.build_unit('Line', 3, 'A', 'A', 20)
    ua.subunits[0].yielding = True
    ua.morale = 3  # eff_morale 3 < 0.75*6 = 4.5
    O.between_turn_recovery(ua)
    assert ua.subunits[0].yielding is True, "morale below rally fraction must stay yielding"


def test_rally_gate_off_is_inert():
    """OFF (default): a yielding subunit is never auto-reverted at the turn boundary."""
    C, _, _, _, E, O = _reload(PC_YIELD_RALLY=False)
    ua = E.build_unit('Line', 3, 'A', 'A', 20)
    ua.subunits[0].yielding = True
    O.between_turn_recovery(ua)
    assert ua.subunits[0].yielding is True, "OFF: rally must be inert"


# ── §2.4 POCKET exit ────────────────────────────────────────────────────────────────────────────────
def _atom_at(U, anchor):
    su = U.Subunit(shape='Line', troop_type='infantry', tier=3, starting_position=(0, 0))
    su._node_anchor = anchor
    return su


def test_pocket_map_edge():
    """A yielding body backed against the map edge (flee vector points off-field) is pocketed."""
    C, _, _, U, _, _ = _reload(PC_YIELD_POCKET=True)
    su = _atom_at(U, (0.0, 20.0))               # at the top edge
    # nearest enemy BELOW -> flee vector points UP, off the field (row < 0)
    assert su._yield_pocketed((-5.0, 20.0), [(5.0, 20.0)]) is True


def test_pocket_enemy_behind():
    """A yielding body with an enemy in its retreat direction (gotten behind) is pocketed."""
    C, _, _, U, _, _ = _reload(PC_YIELD_POCKET=True)
    su = _atom_at(U, (20.0, 20.0))
    # nearest enemy below (front); a second enemy ABOVE, within reach, sits in the flee path
    flee = (2 * 20.0 - 25.0, 2 * 20.0 - 20.0)   # reflect (25,20) through (20,20) -> (15,20), dir = up
    assert su._yield_pocketed(flee, [(25.0, 20.0), (18.0, 20.0)]) is True


def test_pocket_open_retreat_not_pocketed():
    """A yielding body with clear ground behind it (in-field, no enemy in the retreat path) is NOT pocketed."""
    C, _, _, U, _, _ = _reload(PC_YIELD_POCKET=True)
    su = _atom_at(U, (20.0, 20.0))
    flee = (2 * 20.0 - 25.0, 2 * 20.0 - 20.0)   # dir = up, one cell (19,20) in-field, no enemy behind
    assert su._yield_pocketed(flee, [(25.0, 20.0)]) is False


def test_pocket_removes_pool_malus():
    """subunit_combat_pool: a POCKETED yielding subunit fights at FULL pool (malus removed); a non-pocketed
    yielding subunit keeps the YIELD_POOL_MULT malus."""
    C, X, _, U, E, _ = _reload(PC_YIELD_POCKET=True)
    u = E.build_unit('Line', 3, 'A', 'A', 20, discipline=5)  # eff_discipline 5 >= D_YIELD -> yield_active
    atom = u.subunits[0]
    atom.yielding = True
    yielding_pool = X.subunit_combat_pool(u, atom)   # malus applied
    atom.pocketed = True
    pocketed_pool = X.subunit_combat_pool(u, atom)   # malus removed
    assert pocketed_pool > yielding_pool, f"pocketed pool ({pocketed_pool}) must exceed malused ({yielding_pool})"


def teardown_module(module):
    for k in ('PC_YIELD_EMERGENT', 'PC_YIELD_RALLY', 'PC_YIELD_POCKET'):
        os.environ.pop(k, None)
    _reload()
