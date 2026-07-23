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
        # [test-critic T2] Bound front at rear/2 (i.e. front never exceeds 1.0x when rear is 2.0x): the
        # broken global-centroid variant inflated a wide line's head-on WINGS to ~1.4x, which makes front
        # EXCEED rear/2 -> caught here. (A braced front can parry to 0 while rear>0, so this is an upper
        # bound, not equality; the exact 2.0x ratio is pinned by test_rear_is_exactly_double_front.)
        if rear > 0:
            assert front <= rear / 2.0 + 1e-9, (
                f"seed {seed}: front {front} must not exceed rear/2 ({rear/2.0}) -- wing cells must stay GREEN")


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
    """(2) A seen flank threat (in FOV, not pinned) is refused once the cell has had FACING_REACTION_TICKS
    to wheel. [test-critic T4] The old test only asserted the clock got STAMPED -- it passed even if the
    penalty were permanent. This asserts the per-cell reaction COUNTER actually reaches the wheel
    threshold (the exact condition, `_cnt >= FACING_REACTION_TICKS`, under which the source drops the
    penalty to m=0), by ticking a PERSISTENT subunit across the window."""
    orch, contact, C = mb
    ub, subB = _mk(orch, (BROW, BCOL), -1, 'B')
    for cid in list(subB.cell_troops):
        subB.cell_facing_vec[cid] = (0, 1)   # face east; attacker due north = seen left flank (<=105deg FOV)
    ua, _ = _mk(orch, (BROW - 3, BCOL), +1, 'A')
    for t in range(1, C.FACING_REACTION_TICKS + 3):
        random.seed(900 + t)
        orch.resolve_engagements(ua, ub, contact.find_contacts(ua, ub), t=t)
    rs = getattr(subB, '_react_since', {})
    # the clock stores (last_tick, consecutive_count); after > FACING_REACTION_TICKS consecutive ticks the
    # count must have reached the threshold -> the cell has wheeled -> the source zeroes the arc penalty.
    counts = [v[1] for v in rs.values()]
    assert counts, "a seen flank threat must stamp the reaction clock"
    assert max(counts) >= C.FACING_REACTION_TICKS, (
        f"seen-flank reaction counter must reach the wheel threshold {C.FACING_REACTION_TICKS}, got {max(counts)}")


def _pincer_dmgb(orch, contact, attackers, seed=13, t=5):
    """Defender B (faces north) struck by a list of attacker bodies at (row_offset, advance_dir)."""
    random.seed(2000 + seed)
    ub, subB = _mk(orch, (BROW, BCOL), -1, 'B')
    subs = [orch.Subunit(shape='Line', troop_type='infantry', tier=2,
                         starting_position=(BROW + dr, BCOL), advance_dir=adv) for dr, adv in attackers]
    ua = orch.Unit(name='A', faction='A', power=4, command=4, discipline=5, discipline_start=5,
                   morale=6, morale_start=6, subunits=subs, dr=1)
    for su in subs:
        su._unit = ua
    return orch.resolve_engagements(ua, ub, contact.find_contacts(ua, ub), t=t)['dmg_b']


def test_multi_side_shock_is_face_based_not_pair_count(mb):
    """(3) + balance-critic A1/A1-gap + arch-critic #1: the shock triggers on the number of DISTINCT FACES
    struck (front/rear/left/right, nearest-perimeter-face of each enemy body), NOT the arc-blind pair count
    `eng_counts` used before. [test-critic T5] The old test never called the engine (only checked the
    INPUTS existed), so deleting the whole mechanic passed it. Here the shock CONSTANT is toggled on
    IDENTICAL geometry+dice, cleanly isolating (a) that a genuine front+rear pincer IS shocked, and (b)
    the A1 fix: two co-FRONT bodies are ONE face, so the shock must NOT apply to them."""
    orch, contact, C = mb

    def with_shock(shock, attackers):
        old = orch.MULTI_SIDE_SHOCK
        orch.MULTI_SIDE_SHOCK = shock
        try:
            return _pincer_dmgb(orch, contact, attackers, seed=13)
        finally:
            orch.MULTI_SIDE_SHOCK = old

    PINCER = [(-3, +1), (+3, -1)]          # front pinner + rear body -> faces {F, B} -> 2 sides -> SHOCK
    TWO_FRONT = [(-3, +1), (-4, +1)]       # two bodies BOTH to the front -> face {F} -> 1 side -> NO shock
    # (a) the effect is real and points the right way: turning the shock ON strictly raises the enveloped
    # defender's casualties (same dice, only the shock constant differs).
    assert with_shock(0.5, PINCER) > with_shock(0.0, PINCER), (
        "a front+rear pincer (2 faces) must take MORE damage with the multi-side shock on")
    # (b) A1 FIX: two co-front bodies are the SAME face -> the shock must be inert for them (identical
    # damage shock-on vs shock-off). The old eng_counts>=2 trigger WOULD have shocked this (2 pairs).
    assert with_shock(0.5, TWO_FRONT) == pytest.approx(with_shock(0.0, TWO_FRONT)), (
        "two co-front bodies are one face -> the multi-side shock must NOT fire (balance-critic A1 fix)")


def test_reaction_clock_resets_between_battles(mb):
    """reaction-critic R1: the per-cell reaction clock is per-engagement transient state on a persistent
    Subunit -- it MUST be cleared at the battle boundary, or a stamp from battle 1 mis-scores battle 2's
    opening ticks. Asserts reset_morale_between_battles clears it."""
    orch, contact, C = mb
    ub, subB = _mk(orch, (BROW, BCOL), -1, 'B')
    for cid in list(subB.cell_troops):
        subB.cell_facing_vec[cid] = (0, 1)   # face east -> a seen flank stamps the clock
    ua, _ = _mk(orch, (BROW - 3, BCOL), +1, 'A')
    random.seed(5)
    orch.resolve_engagements(ua, ub, contact.find_contacts(ua, ub), t=3)
    assert getattr(subB, '_react_since', {}), "a seen-flank engagement should stamp the reaction clock"
    orch.reset_morale_between_battles(ub)
    assert not subB._react_since, "reset_morale_between_battles must CLEAR the reaction clock (R1 leak fix)"
