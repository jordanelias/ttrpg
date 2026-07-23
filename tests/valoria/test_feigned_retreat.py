"""Feigned Retreat (PP-256 / mass_battle_v30.md §A.12, §B.4) — ED-MB-0022.

A unit that declares a Feigned Retreat withdraws as if routing to bait a pursuer. When a Fast victor
begins pursuing a *feigning* enemy, two rolls resolve the trap:
  1. the pursuing general rolls Command d10s vs Ob 2 to RECOGNISE the feint (success -> no effect);
  2. if deceived, the pursuer makes a Discipline check Ob 1 — failing it OVEREXTENDS the pursuer,
     cutting its next engagement pool by OVEREXTEND_PENALTY.

The whole tactic is GATED behind PC_FEIGNED_RETREAT (default OFF) so the multi-unit RNG stream is
unchanged unless explicitly enabled (the flip is needs_jordan).

Convention note (verified, not a bug): the engine's `roll_pool` is the canonical §A net-successes roll
(face 1 = -1 botch, 7-9 = +1, 10 = +2) used by EVERY other §A check (recall_check, cascade, …). Under
that shared convention the realized hold rates are Disc-1 ~40% (matches PP-256 exactly) and Disc-4
~74.5%. PP-256's "~87%" is the no-botch binomial idealization 1-0.6^4; we deliberately DO NOT introduce
a bespoke botch-free success-counter for this one check (that would be a scale-local dialect — a
CLAUDE.md §10 guardrail violation). Hold rate rising monotonically with Discipline is the invariant."""
import importlib
import os
import random
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'sim'))

import pytest  # noqa: E402


def _reload(on):
    os.environ['PC_FEIGNED_RETREAT'] = '1' if on else '0'
    import mass_battle.config as C
    importlib.reload(C)
    import mass_battle.resolution as R
    importlib.reload(R)
    import mass_battle.hierarchy.units as U
    importlib.reload(U)
    import mass_battle.orchestration as O
    importlib.reload(O)
    return C, O


class _Stub:
    """Minimal pursuer stand-in exposing the attributes the resolvers read."""
    def __init__(self, discipline=3, command=3, feigned=False):
        self.discipline = discipline
        self.command = command
        self.feigned = feigned
        self.name = 'stub'
        self.overextended = False


def test_discipline_check_rate_matches_engine_convention():
    """Hold rate is ~40% at Disc-1 (matches PP-256 exactly) and rises with Discipline under the shared
    roll_pool convention. Disc-4 realizes ~74.5% (engine net-roll), not the doc's no-botch 87%."""
    _, O = _reload(on=True)
    random.seed(20260723)
    rates = {}
    for disc in (1, 2, 4):
        holds = sum(O.feigned_retreat_check(_Stub(discipline=disc)) for _ in range(20000)) / 20000
        rates[disc] = holds
    assert 0.36 <= rates[1] <= 0.44, f"Disc-1 hold ~40% (PP-256), got {rates[1]:.3f}"
    assert 0.70 <= rates[4] <= 0.79, f"Disc-4 hold ~74.5% (engine convention), got {rates[4]:.3f}"
    assert rates[1] < rates[2] < rates[4], f"hold rate must rise with Discipline: {rates}"


def test_recognize_rate_rises_with_command():
    """The Ob-2 recognise roll: a higher-Command general recognises the feint more often."""
    _, O = _reload(on=True)
    random.seed(11)
    low = sum(O.feigned_retreat_recognized(_Stub(command=1)) for _ in range(20000)) / 20000
    high = sum(O.feigned_retreat_recognized(_Stub(command=6)) for _ in range(20000)) / 20000
    assert low < high, f"recognise rate must rise with Command: {low:.3f} vs {high:.3f}"


def test_resolve_marks_overextended_only_when_deceived_and_failing():
    """resolve_feigned_retreat: recognised -> not overextended; deceived + failed Discipline -> overextended."""
    _, O = _reload(on=True)
    # A recognised feint never overextends (high Command recognises, so overextended stays False).
    random.seed(3)
    ever_over_when_recognized = False
    for _ in range(2000):
        p = _Stub(discipline=1, command=8)
        r = O.resolve_feigned_retreat(p, _Stub(feigned=True))
        if r and r['recognized']:
            assert not p.overextended and not r['overextended']
        if p.overextended and r['recognized']:
            ever_over_when_recognized = True
    assert not ever_over_when_recognized, "a recognised feint must never overextend the pursuer"
    # Over many low-Disc low-Command pursuers, SOME overextend (deceived + failed the check).
    random.seed(4)
    n_over = sum(1 for _ in range(2000)
                 if (O.resolve_feigned_retreat(_Stub(discipline=1, command=1), _Stub(feigned=True)) or {}).get('overextended'))
    assert n_over > 0, "deceived low-discipline pursuers must sometimes overextend"


def test_non_feigning_target_returns_none():
    """Chasing a genuinely routing (non-feigned) unit is a no-op even with the toggle on."""
    _, O = _reload(on=True)
    p = _Stub(discipline=1, command=1)
    assert O.resolve_feigned_retreat(p, _Stub(feigned=False)) is None
    assert not p.overextended


def test_gate_off_is_inert():
    """OFF (default): even a declared feint is a no-op and never overextends -> byte-exact RNG stream."""
    _, O = _reload(on=False)
    p = _Stub(discipline=1, command=1)
    assert O.resolve_feigned_retreat(p, _Stub(feigned=True)) is None
    assert not p.overextended


def _build_unit(on):
    """A single-subunit Fast unit via the canonical engine.build_unit factory (the pool value itself is
    irrelevant here — only the overextended DELTA matters)."""
    C, _ = _reload(on=on)
    from mass_battle.engine import build_unit  # noqa: E402
    u = build_unit('Line', 3, 'p', 'A', 20, troop_type='cavalry',
                   power=4, command=4, discipline=5, morale=6, speed='Fast')
    return C, u


def test_overextended_pool_penalty_applies_only_when_gated_on():
    """base_combat_pool: an overextended pursuer's pool is cut by OVEREXTEND_PENALTY when the toggle is
    ON; the flag is inert when OFF (byte-exact)."""
    C, u = _build_unit(on=True)
    base = u.base_combat_pool()
    u.overextended = True
    penalized = u.base_combat_pool()
    assert penalized == max(1, base - C.OVEREXTEND_PENALTY), \
        f"ON: overextended pool must drop by {C.OVEREXTEND_PENALTY} ({base} -> {penalized})"

    # OFF: the flag is inert.
    _, u2 = _build_unit(on=False)
    off_base = u2.base_combat_pool()
    u2.overextended = True
    assert u2.base_combat_pool() == off_base, "OFF: overextended flag must be inert (byte-exact)"


def teardown_module(module):
    os.environ.pop('PC_FEIGNED_RETREAT', None)
    _reload(on=False)
