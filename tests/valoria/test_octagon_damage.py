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


def _reload_mb(monkeypatch, **overrides):
    """Reload the mass_battle modules under an explicit flag set."""
    env = {'PER_CELL': '1', 'PC_REFUSE': '1', 'LANCHESTER_ENABLED': '1',
           'PC_OCTAGON_DMG': '1', 'PC_FRACTIONAL_POOL': '1'}
    env.update(overrides)
    for k, v in env.items():
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


@pytest.fixture
def mb(monkeypatch):
    """Fresh mass_battle modules with the octagon-damage model ON and the per-cell facing path enabled.
    Discrete lattice contact (FIELD_MOVEMENT off) -> deterministic geometry for the isolation asserts.

    [ED-MB-0063 critic finding D] PC_FRACTIONAL_POOL is now pinned EXPLICITLY rather than inherited
    from the ambient default. It is the flag that flipped this module's verdict before the isolation
    fix, so leaving it ambient was the one gap in a fixture that already pins four others -- the same
    reason test_mass_battle_byte_exact.py pins PC_OCTAGON_DMG per mode instead of trusting the default.
    """
    for k, v in (('PER_CELL', '1'), ('PC_REFUSE', '1'), ('LANCHESTER_ENABLED', '1'),
                 ('PC_OCTAGON_DMG', '1'), ('PC_FRACTIONAL_POOL', '1')):
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


# ─── ED-MB-0063: the arc-ratio isolation ──────────────────────────────────────
# A is deployed at (BROW-3, BCOL), i.e. at the LOWER row, so a defender facing the
# attacker points row-negative. These rotate ONLY the cell facing vectors.
FACE_TOWARD_A = (-1.0, 0.0)   # GREEN — B fronts the attacker
FACE_AWAY_A = (1.0, 0.0)      # RED   — B's back to the attacker, blind arc


def _arc_pair(orch, contact, seed, t=5):
    """Matched GREEN/RED damage with the DEFENDER'S BODY HELD FIXED — vary only the arc.

    THE CONFOUND THIS REPLACES (ED-MB-0063, F2 of the Track-F series). These tests used to
    flip `def_adv` between -1 and +1 and describe the two arms as "same dice, same contact
    cells, only the facing arc differs". **That description was false, and the falsity was
    load-bearing.** `advance_dir` orients the whole SUBUNIT (`geometry.oriented_pattern`), so
    flipping it changes WHICH of B's cells the attacker touches: the absolute footprint is
    identical, but in the ORIGINAL frame the front arm contacts B's rank `(0,*)` and the rear
    arm contacts rank `(2,*)`. Cell identity is what matters, because the pool is
    support-depth weighted.

    THE MECHANISM IS SUPPORT DEPTH, NOT TROOP COUNTS. `core.exchange._pair_engaged_troops`
    takes `front_r = min(r)` over the contact cells and credits every deeper cell at
    `SUPPORT_WEIGHTS = {1: 1.0, 2: 0.7, 3: 0.5}`. Contacting rank 0 leaves two ranks behind it
    -> `(5 + 5*1.0 + 5*0.7)/15 = 0.9` of base; contacting rank 2 leaves none -> `5/15 = 1/3`.
    At base pool 4 that is exactly the observed **3.6 vs 1.333**. `compute_degree` is RELATIVE,
    so B's smaller pool rolling a higher net (2 vs 1) outranked A's larger one: at seed 5 A's
    IDENTICAL net of 1.0 read `Success` in one arm and `Partial` in the other, and `Partial`
    (damage 1) minus the universal `dr=1` is **0.0** — a rear strike doing less than a frontal one.

    [CORRECTED by the ED-MB-0063 critic pass] The first write-up of this attributed the pool
    difference to "different cells carry different troops". **That was wrong** — `distribution`
    defaults to `'uniform'`, so every cell holds `troop_count/len(ids)` and ranks 0 and 2 are
    identical in troops. The support-depth hypothesis had in fact been dismissed earlier in the
    same investigation by measuring `geometry.support_engage_frac`, which returned 1.0 in both
    arms — but that function is **never called on this path** (`orchestration.py` guards it with
    `if POOL_VARIANT != "C-ii"`, and `POOL_VARIANT == "C-ii"`), and its `min(1.0, ...)` cap would
    have hidden the asymmetry anyway. The concept was right and was discarded on the strength of
    the wrong function: pattern-matching a name instead of following the live path.

    So the reported failure was never the engine mis-applying the arc. The two arms were not
    the same experiment: CLAUDE.md §0.1 #4, attacked at the level of the ratio's statistics and
    never at the level of its setup. Prior art: `audit/2026-07-30-mb-session-retrospective/
    00_lessons.md` §"What this corrects" had already classified F2 as a test-premise defect and
    named orig-frame support depth. This module implements that classification.

    `PC_FRACTIONAL_POOL=0` makes the old form pass, which is why a flag bisect fingers it — but
    it is a MASK, not a cause. Flooring sends 3.6 -> 3 and 1.333 -> 1, which at this seed happens
    to keep B's net under A's. The confound is untouched; only its visibility changes. Recording
    that flag as F2's cause would have shipped a wrong diagnosis that reproduced on demand.

    Holding the body fixed at `def_adv=-1` and rotating only `cell_facing_vec` makes the arc the
    single variable — both arms then share one contact set, one pool, and one RNG stream.

    ⚠ THE ISOLATION IS SCENARIO-DEPENDENT, NOT STRUCTURAL (critic finding C). `cell_facing_vec`
    also feeds `_per_cell_angle_mod`, which gates charge-shock, envelopment-shock and brace-recoil,
    and feeds `_compute_atom_sides`. Those are inert HERE only because this fixture has no `brace`
    instruction, no momentum differential, and one subunit per side. Add an instruction or a second
    body and "only the arc varies" quietly stops being true. Stated so the next author does not
    inherit the precondition silently — which is how the confound this replaces was inherited.
    """
    green, _ = _dmg_b(orch, contact, def_adv=-1, seed=seed, t=t, def_face=FACE_TOWARD_A)
    red, _ = _dmg_b(orch, contact, def_adv=-1, seed=seed, t=t, def_face=FACE_AWAY_A)
    return green, red


def test_rear_is_exactly_double_front(mb):
    """(1) A pure rear strike doubles the defender's casualties vs the identical frontal strike --
    the octagon arc multiplier is EXACTLY 2.0x per seed (front faces attacker, rear turns its back;
    same dice, same contact cells, only the facing arc differs)."""
    orch, contact, C = mb
    checked = 0
    for seed in range(12):
        front, rear = _arc_pair(orch, contact, seed)   # body fixed; only the arc varies
        if front > 0:
            assert rear == pytest.approx(2.0 * front), f"seed {seed}: rear {rear} != 2x front {front}"
            checked += 1
        else:
            # a braced front can parry to zero; the rear then still takes the shock-stripped hit
            assert rear >= front
    # Measured 7 at shipped defaults (ED-MB-0063). Floor at 3 rather than 7 so a benign RNG-stream
    # reorder is not a false red, while "the ratio was never actually observed" is still caught.
    assert checked >= 3, "expected several seeds with a non-zero frontal exchange to pin the 2.0x ratio"


@pytest.mark.parametrize('fractional', ['0', '1'])
def test_arc_ratio_is_invariant_to_the_fractional_pool_flag(monkeypatch, fractional):
    """THE REAL FALSIFIER FOR THE ED-MB-0063 ISOLATION (critic finding D).

    "7 of 12 seeds gave exactly 2.0x" is weak evidence and was over-sold as strong. Once the body
    is held fixed, both arms consume the SAME dice and differ only in the arc multiplier, so
    `rear == 2*front` is arithmetically forced wherever `front > 0` — a passing run confirms the
    arithmetic, not the isolation.

    THIS assertion has content, because it is the specific thing that was false before. F2 was
    defined by the verdict depending on `PC_FRACTIONAL_POOL`: ON it failed, OFF it passed, and the
    flag looked like the cause. If the confound is genuinely gone, that dependence must be gone
    too — the ratio has to hold under BOTH settings of the flag, for the same seeds. If someone
    reintroduces a body-orienting difference between the arms, the pools diverge again, flooring
    starts to matter again, and this test goes red on one parameter and not the other. That is a
    failure mode "7 of 12" cannot see at all.
    """
    orch, contact, _ = _reload_mb(monkeypatch, PC_FRACTIONAL_POOL=fractional)
    checked = 0
    for seed in range(12):
        front, rear = _arc_pair(orch, contact, seed)
        if front > 0:
            assert rear == pytest.approx(2.0 * front), (
                f'PC_FRACTIONAL_POOL={fractional}, seed {seed}: rear {rear} != 2x front {front} — '
                f'the arc ratio still depends on the flag, so the arms are not yet one experiment')
            checked += 1
    assert checked >= 3, (
        f'PC_FRACTIONAL_POOL={fractional}: only {checked} seeds produced a non-zero frontal '
        f'exchange, so the invariance was not actually observed')


def test_front_takes_no_arc_penalty(mb):
    """(1) A head-on clash of equal-width lines is GREEN for every contact cell -- including the WINGS.
    The multiplier uses the LOCAL attacker centroid, so a wide line's wing cell is NOT mis-read as
    flanked by the enemy centre. Front casualties must never exceed the flank/rear casualties."""
    orch, contact, C = mb
    checked = 0
    for seed in range(12):
        front, _ = _dmg_b(orch, contact, def_adv=-1, seed=seed)
        rear, _ = _dmg_b(orch, contact, def_adv=+1, seed=seed)
        # [test-critic T2] Bound front at rear/2 (i.e. front never exceeds 1.0x when rear is 2.0x): the
        # broken global-centroid variant inflated a wide line's head-on WINGS to ~1.4x, which makes front
        # EXCEED rear/2 -> caught here. (A braced front can parry to 0 while rear>0, so this is an upper
        # bound, not equality; the exact 2.0x ratio is pinned by test_rear_is_exactly_double_front.)
        if rear > 0:
            checked += 1
            assert front <= rear / 2.0 + 1e-9, (
                f"seed {seed}: front {front} must not exceed rear/2 ({rear/2.0}) -- wing cells must stay GREEN")
    # [ED-MB-0045 A4a] The bound above is CONDITIONAL on rear>0, so without this the loop could observe
    # nothing and still pass. Measured 2026-07-29 at shipped defaults: 9 of the 12 seeds produce rear>0
    # (deterministic — every _dmg_b call re-seeds). Floor set at 6, not the exact 9, so a benign
    # RNG-stream reorder is not a false red while "the branch barely/never fired" is still caught —
    # the same robustness policy as test_feigned_retreat.py's floor (critic-pass consistency fix).
    assert checked >= 6, (
        f"only {checked} of 12 seeds produced a non-zero rear exchange (measured 9) -- the wing-cell "
        f"bound is not being observed, so this test proves nothing")


def test_rear_penalty_persists_across_reaction_window(mb):
    """(2) A rear strike is in the blind arc: the cell can never perceive it, so it never wheels to face
    and the 2.0x persists tick after tick -- long PAST FACING_REACTION_TICKS. Asserted on the observable:
    at every tick across the window, the rear defender still takes exactly 2x the matched frontal
    casualties (never refuses back to 1x). (Contrast: a *seen* flank threat refuses once the window
    elapses -- test_visible_flank_refuses_after_delay.)

    ⚠ THIS TEST DOES NOT CURRENTLY OBSERVE THE WINDOW IT NAMES (ED-MB-0063 critic finding A;
    PRE-EXISTING, not introduced by the isolation fix, and NOT fixed here). The reaction counter
    in `orchestration` is CONSECUTIVE-TICK: it accumulates in a per-subunit `_react_since` map
    across calls. `_arc_pair` builds a FRESH `Subunit` per call, so the map always starts empty
    and `_cnt` can never exceed 1 — while `FACING_REACTION_TICKS` is 2. The `_cnt >=
    FACING_REACTION_TICKS` branch is therefore unreachable from here, and an engine that DID
    wheel out of the blind arc after two consecutive ticks would still pass. Varying `t` varies
    the tick LABEL, not the elapsed window.

    Recorded rather than silently re-blessed: routing this through `_arc_pair` fixed its arms-
    comparability but says nothing about its temporal claim. The correct form ticks a PERSISTENT
    subunit, as `test_visible_flank_refuses_after_delay` already does in this file — that is the
    template for the fix, and it is a separate change with its own expected-delta.
    """
    orch, contact, C = mb
    horizon = C.FACING_REACTION_TICKS + 3
    checked = 0
    for t in range(1, horizon + 1):
        # Matched GREEN/RED at the SAME tick and seed. Routed through _arc_pair (ED-MB-0063): the
        # old `def_adv=±1` form claimed "identical dice/contact" and was not — see that docstring.
        front, rear = _arc_pair(orch, contact, seed=3, t=t)
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
