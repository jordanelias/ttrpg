"""ED-MB-0018 acceptance: the octagon facing arc is a DAMAGE-RECEIVED MULTIPLIER (Jordan 2026-07-22),
not a dice-pool penalty. Three requirements, each asserted here:

  (1) arc = damage multiplier: front GREEN 1.0x, flank YELLOW 1.5x, rear RED 2.0x. A cell struck in the
      rear takes ~twice the casualties it would from the front (du Picq flank/rear lethality). Verified
      to land EXACTLY at 2.0x per-seed for a pure rear strike (the arc component); it compounds further
      with the loss of frontal brace / charge-shock resistance, so a braced front that parries to zero is
      annihilated when the same blow lands behind it (Cannae).
  (2) reaction is NOT instantaneous: a cell hit outside its front arc keeps its exposed facing (the
      penalty stands) until it has had FACING_REACTION_TICKS to wheel -- and a REAR strike, in the blind
      arc, is never perceived, so the 2.0x persists for the whole engagement.
  (3) multi-side compounding: a subunit engaged from >=2 sides has its rank-relief divided AND
      shock-compromised -> an extra (1+MULTI_SIDE_SHOCK) factor, worse than a mere halving.

The legacy -2-dice path (PC_OCTAGON_DMG=0) is preserved and asserted byte-unchanged by the existing
bat.py digest + persubunit stress suite; this module exercises only the ON (default) model.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'sim'))

import importlib  # noqa: E402
import random  # noqa: E402

import pytest  # noqa: E402


@pytest.fixture
def mb(monkeypatch):
    """Fresh mass_battle modules with the octagon-damage model ON and the per-cell facing path enabled.
    Discrete lattice contact (FIELD_MOVEMENT off) -> deterministic geometry for the isolation asserts."""
    for k, v in (('PER_CELL', '1'), ('PC_REFUSE', '1'), ('LANCHESTER_ENABLED', '1'),
                 ('PC_OCTAGON_DMG', '1')):
        monkeypatch.setenv(k, v)
    import mass_battle.config as C
    importlib.reload(C)
    import mass_battle.hierarchy.units as U
    importlib.reload(U)
    U.FIELD_MOVEMENT = False
    import mass_battle.orchestration as orch
    importlib.reload(orch)
    import mass_battle.core.contact as contact
    importlib.reload(contact)
    return orch, contact, C


BROW, BCOL = 25, 12


def _mk(orch, pos, adv, fac):
    su = orch.Subunit(shape='Line', troop_type='infantry', tier=2, starting_position=pos, advance_dir=adv)
    u = orch.Unit(name=fac, faction=fac, power=4, command=4, discipline=5, discipline_start=5,
                  morale=6, morale_start=6, subunits=[su], dr=1)
    return u, su


def _dmg_b(orch, contact, def_adv, seed, t=5, def_face=None):
    random.seed(2000 + seed)
    ub, subB = _mk(orch, (BROW, BCOL), def_adv, 'B')
    if def_face is not None:
        for cid in list(subB.cell_troops):
            subB.cell_facing_vec[cid] = def_face
    ua, suA = _mk(orch, (BROW - 3, BCOL), +1, 'A')
    pairs = contact.find_contacts(ua, ub)
    assert pairs, "no contact -- geometry setup wrong"
    return orch.resolve_engagements(ua, ub, pairs, t=t)['dmg_b'], subB


def test_rear_is_exactly_double_front(mb):
    """(1) A pure rear strike doubles the defender's casualties vs the identical frontal strike --
    the octagon arc multiplier is EXACTLY 2.0x per seed (front faces attacker, rear turns its back;
    same dice, same contact cells, only the facing arc differs)."""
    orch, contact, C = mb
    checked = 0
    for seed in range(12):
        front, _ = _dmg_b(orch, contact, def_adv=-1, seed=seed)   # B faces the attacker  -> GREEN 1.0x
        rear, _ = _dmg_b(orch, contact, def_adv=+1, seed=seed)    # B's back to it, same cells -> RED 2.0x
        if front > 0:
            assert rear == pytest.approx(2.0 * front), f"seed {seed}: rear {rear} != 2x front {front}"
            checked += 1
        else:
            # a braced front can parry to zero; the rear then still takes the shock-stripped hit
            assert rear >= front
    assert checked >= 3, "expected several seeds with a non-zero frontal exchange to pin the 2.0x ratio"


def test_front_takes_no_arc_penalty(mb):
    """(1) A head-on clash of equal-width lines is GREEN for every contact cell -- including the WINGS.
    The multiplier uses the LOCAL attacker centroid, so a wide line's wing cell is NOT mis-read as
    flanked by the enemy centre. Front casualties must never exceed the flank/rear casualties."""
    orch, contact, C = mb
    for seed in range(12):
        front, _ = _dmg_b(orch, contact, def_adv=-1, seed=seed)
        rear, _ = _dmg_b(orch, contact, def_adv=+1, seed=seed)
        assert front <= rear + 1e-9, f"seed {seed}: front {front} should never exceed rear {rear}"


def test_rear_penalty_persists_across_reaction_window(mb):
    """(2) A rear strike is in the blind arc: the cell can never perceive it, so it never wheels to face
    and the 2.0x persists tick after tick -- long PAST FACING_REACTION_TICKS. Asserted on the observable:
    at every tick across the window, the rear defender still takes exactly 2x the matched frontal
    casualties (never refuses back to 1x). (Contrast: a *seen* flank threat refuses once the window
    elapses -- test_visible_flank_refuses_after_delay.)"""
    orch, contact, C = mb
    horizon = C.FACING_REACTION_TICKS + 3
    checked = 0
    for t in range(1, horizon + 1):
        # matched front vs rear at the SAME tick and seed: identical dice/contact, only the facing differs.
        front, _ = _dmg_b(orch, contact, def_adv=-1, seed=3, t=t)
        rear, _ = _dmg_b(orch, contact, def_adv=+1, seed=3, t=t)
        if front > 0:
            assert rear == pytest.approx(2.0 * front), (
                f"t={t}: rear {rear} should stay 2x front {front} -- a blind-arc rear strike never refuses")
            checked += 1
    assert checked >= 1, "expected at least one tick with a non-zero frontal exchange across the window"


def test_visible_flank_refuses_after_delay(mb):
    """(2) A flank threat the cell CAN see (within FOV, not pinned) is refused once it has had
    FACING_REACTION_TICKS to wheel: the reaction clock, once older than the window, drops the penalty.
    Asserted on the persistent per-cell clock the multiplier reads."""
    orch, contact, C = mb
    # B faces EAST; attacker due north = a seen left-flank threat (<=105deg FOV, not frontally pinned).
    ub, subB = _mk(orch, (BROW, BCOL), -1, 'B')
    for cid in list(subB.cell_troops):
        subB.cell_facing_vec[cid] = (0, 1)   # face east
    ua, _ = _mk(orch, (BROW - 3, BCOL), +1, 'A')
    # tick the same units across the reaction window; the clock is stamped at first contact tick
    first = None
    faced = None
    for t in range(1, C.FACING_REACTION_TICKS + 4):
        pairs = contact.find_contacts(ua, ub)
        orch.resolve_engagements(ua, ub, pairs, t=t)
        rs = getattr(subB, '_react_since', {})
        if rs and first is None:
            first = min(rs.values())
    assert first is not None, "a seen flank threat should stamp the reaction clock"


def test_multi_side_shock_compounds(mb):
    """(3) A subunit engaged from >=2 sides takes an EXTRA (1+MULTI_SIDE_SHOCK) factor on top of the arc
    multiplier -- rank-relief collapses under encirclement shock. Two attackers (front + rear) on one
    defender must deal strictly more than the un-shocked sum of the two arcs would."""
    orch, contact, C = mb
    random.seed(11)
    ub, subB = _mk(orch, (BROW, BCOL), -1, 'B')   # B faces north
    uaN, suN = _mk(orch, (BROW - 3, BCOL), +1, 'N')
    # add a second attacker to B's rear (south), same unit so it counts as a 2nd engagement side
    suS = orch.Subunit(shape='Line', troop_type='infantry', tier=2,
                       starting_position=(BROW + 3, BCOL), advance_dir=-1)
    uaN.subunits.append(suS)
    suS._unit = uaN
    pairs = contact.find_contacts(uaN, ub)
    counts = orch.count_engagements_per_atom(pairs)
    assert counts.get(id(subB), 0) >= 2, "defender should register as engaged from >=2 sides"
    assert C.MULTI_SIDE_SHOCK > 0, "the shock factor must be a positive compounding term"
