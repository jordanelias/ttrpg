"""PC-10a (RS-25): duel TERMS on `wrapper.fight` -- a duel need not be lethal.

Jordan, 2026-10-14: *"a duel doesn't have to be lethal"*. Under a non-lethal term the fight STOPS when a fighter's own
WoundTracker crosses it -- `blood` at the first wound, `yield` at `YIELD_HEALTH_FRAC` of Health -- and that fighter
yields, standing, through the SAME `yield` event an accepted `Yield` (PC-01, `ED-PC-0056`) emits, so the seam's
`surrender_of` lifts it unchanged and no band is added (H-98). `death`, the default, is the fight as it was.

The falsifiers are the plan position's own (v9 `_part7`, PC-10):
  (1) under the default lethal terms the fight is byte-identical: trace, result and every engine-level draw
      (`_draw_stream.RecordingRandom`) equal the no-`terms` call's;
  (2) a seeded `blood` fight stops at the first wound with `surrender` set and NO felling;
  (3) a seeded `yield` fight stops at the threshold;
  (4) under `death` terms Felled stays reachable;
  (5) the stop rule made a no-op sends (2) red -- the control is in this file
      (`test_the_blood_assertions_observe_a_missing_stop`), not left to a one-off run.
The cross-TREE half of (1) -- the lethal fight equal to the pre-PC-10a engine's -- is the existing combat suite and
the draw-stream pins, which this position does not move.
"""
import os
import random
import sys

import pytest

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_ENGINE = os.path.join(_ROOT, 'modules', 'combat')
for _p in (_ROOT, _ENGINE):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from valoria import _draw_stream as DS          # noqa: E402  the single owner of the draw instrument (CLAUDE.md §8)

import combatant as C                            # noqa: E402
import wrapper                                   # noqa: E402
from config import CFG                           # noqa: E402

_PAIRS = (('arming', 'arming'), ('spear', 'arming'), ('longsword', 'dagger'))


def _fight(seed, terms=None, pair=_PAIRS[0]):
    """One fight on `seed`. Every trace event carries `_draws` (engine-level draws so far) and `_wounds`/`_health`,
    each fighter's tracker at the moment of the event, so where the first wound landed is read off the control."""
    A, B = C.Combatant('A', weapon=pair[0]), C.Combatant('B', weapon=pair[1])
    kw = {} if terms is None else {'terms': terms}
    trace = []
    prev = wrapper._TRACE
    rng = DS.RecordingRandom(seed)
    try:
        wrapper._TRACE = lambda e: trace.append(dict(
            e, _draws=len(rng.trace),
            _wounds=(A.wt.wounds, B.wt.wounds),
            _health=(A.wt.health_remaining, B.wt.health_remaining)))
        result = wrapper.fight(A, B, CFG, rng, **kw)
    finally:
        wrapper._TRACE = prev
    return result, trace, rng, A, B


def _turn_of(trace, i):
    """The 1-based turn event `i` falls in (0 before the first `turn_start`)."""
    return sum(1 for e in trace[:i + 1] if e['kind'] == 'turn_start')


def _first(trace, pred):
    return next((i for i, e in enumerate(trace) if pred(e)), None)


def _diverge(trace):
    """Where a terms-stopped fight leaves its lethal control: the burst cut by the terms (`separation` reason `terms`),
    or, when the burst had already ended on its own that beat, the `yield` that replaces the next turn."""
    i = _first(trace, lambda e: e.get('reason') == 'terms')
    return i if i is not None else _first(trace, lambda e: e['kind'] == 'yield')


# ── (1) the lethal default is untouched ───────────────────────────────────────────────────────────────────────

def test_the_lethal_default_is_byte_identical_to_a_fight_with_no_terms():
    checked = 0
    for pair in _PAIRS:
        for seed in range(40):
            r0, t0, g0, _, _ = _fight(seed, pair=pair)
            r1, t1, g1, _, _ = _fight(seed, terms='death', pair=pair)
            assert (r1, t1, g1.trace) == (r0, t0, g0.trace), (pair, seed)
            assert not any(e['kind'] == 'yield' or e.get('reason') == 'terms' for e in t1), (pair, seed)
            checked += 1
    assert checked == 120


def test_a_term_outside_the_closed_set_is_refused_by_name():
    A, B = C.Combatant('A'), C.Combatant('B')
    for bad in ('first_blood', '', None, 'Death'):
        with pytest.raises(ValueError, match='terms'):
            wrapper.fight(A, B, CFG, random.Random(0), terms=bad)
    assert wrapper.DUEL_TERMS == ('yield', 'blood', 'death') and wrapper.LETHAL_TERMS == 'death'


# ── (2) `blood` stops at the first wound ──────────────────────────────────────────────────────────────────────

def _blood_cases():
    """Seeds whose LETHAL control runs at least one more turn after its first wound, found rather than assumed --
    so a fight that ignored the term would be observably longer."""
    out = []
    for pair in _PAIRS:
        for seed in range(60):
            _, ctrl, _, _, _ = _fight(seed, pair=pair)
            k = _first(ctrl, lambda e: max(e['_wounds']) >= 1)
            # ONE fighter wounded at the first wounded event: when both cross in one beat the yielder is the
            # one with less Health left (`wrapper._terms_yielder`), which `first_wounded` below does not predict.
            if (k is not None and _turn_of(ctrl, len(ctrl) - 1) > _turn_of(ctrl, k)
                    and (ctrl[k]['_wounds'][0] >= 1) != (ctrl[k]['_wounds'][1] >= 1)):
                out.append((pair, seed))
            if sum(1 for p, _ in out if p == pair) == 4:
                break
    return out


def _assert_blood_stop(pair, seed):
    """The assertions (2) rests on, shared with the mutation control below."""
    from engine.season.seam.wrappers.combat import surrender_of
    _, ctrl, ctrl_rng, _, _ = _fight(seed, pair=pair)
    result, trace, rng, A, B = _fight(seed, terms='blood', pair=pair)
    k = _first(ctrl, lambda e: max(e['_wounds']) >= 1)
    first_wounded = 'A' if ctrl[k]['_wounds'][0] >= 1 else 'B'
    # The stop: exactly one `yield`, unrefused, by the fighter the first wound fell on, in the turn it fell in.
    ylds = [e for e in trace if e['kind'] == 'yield']
    assert len(ylds) == 1, [e['kind'] for e in trace[-6:]]
    ev = ylds[0]
    assert ev['by'] == first_wounded and ev['accepted'] is True and ev['refused'] is None and ev['terms'] == 'blood'
    assert ev['turn'] == _turn_of(ctrl, k), (ev['turn'], _turn_of(ctrl, k))
    # Up to the stop, the fight IS the control, draw for draw; the control then ran on and drew more.
    assert trace[:_diverge(trace)] == ctrl[:_diverge(trace)]
    assert len(rng.trace) == ev['_draws'] and len(rng.trace) < len(ctrl_rng.trace)
    # Nothing follows the yield but the result: no UPSET_FLOOR draw.
    assert [e['kind'] for e in trace[trace.index(ev) + 1:]] == ['fight_result']
    # NO DEATH: nobody felled, the yielder read by the existing bands (never Felled), the opponent's result.
    from engine.season.data.rosters import COMBAT_BANDS, WOUND_QUANTITIES
    from engine.season.seam.ladder import combat_degree
    yielder = A if first_wounded == 'A' else B
    assert not A.felled and not B.felled
    st = dict(available=True, **{q: getattr(yielder.wt, q) for q in WOUND_QUANTITIES})
    assert combat_degree(dict(wound_state={first_wounded: st}), first_wounded) == COMBAT_BANDS[1]   # 'Wounded'
    assert result == (-1 if first_wounded == 'A' else 1)
    assert surrender_of(trace) == dict(by=first_wounded, turn=ev['turn'], accepted=True)


def test_a_blood_duel_stops_at_the_first_wound_with_surrender_set_and_no_death():
    cases = _blood_cases()
    assert len(cases) >= 6, cases
    for pair, seed in cases:
        _assert_blood_stop(pair, seed)
    assert {('A' if _fight(s, 'blood', pair=p)[0] == -1 else 'B') for p, s in cases} == {'A', 'B'}, \
        'both sides yield somewhere in the sample, so the yielder is not hard-wired to one label'


def test_the_blood_assertions_observe_a_missing_stop(monkeypatch):
    """(5) THE MUTATION, kept executable: with the stop rule a no-op, the same assertions go red on every case."""
    cases = _blood_cases()
    assert cases
    monkeypatch.setattr(wrapper, '_terms_met', lambda A, B, terms, cfg: False)
    red = 0
    for pair, seed in cases:
        with pytest.raises(AssertionError):
            _assert_blood_stop(pair, seed)
        red += 1
    assert red == len(cases)


def test_the_module_entry_reads_the_terms_off_the_typed_input():
    """`fight.py` passes `inp.terms` when the record carries it, the lethal default when it does not. The field is
    the season's to declare (PC-10b); a subclass stands in for it here."""
    import importlib
    from dataclasses import dataclass
    from engine.season.queries.inputs import PersonalCombatInput
    from engine.season.seam.wrappers.combat import surrender_of
    entry = importlib.import_module('modules.combat.fight')   # the composition row's `target:` module

    @dataclass(frozen=True)
    class _Termed(PersonalCombatInput):
        terms: str = 'death'

    qs = ('felled', 'wounds', 'health_remaining', 'health_full')
    seen = 0
    for seed in range(10):
        bare = entry.fight(PersonalCombatInput(('p_a', 'p_b'), (4, 4), qs), random.Random(seed))
        death = entry.fight(_Termed(('p_a', 'p_b'), (4, 4), qs, 'death'), random.Random(seed))
        blood = entry.fight(_Termed(('p_a', 'p_b'), (4, 4), qs, 'blood'), random.Random(seed))
        assert (death['result'], death['trace']) == (bare['result'], bare['trace'])
        assert surrender_of(bare['trace']) is None
        s = surrender_of(blood['trace'])
        assert s is not None and blood['result'] == (-1 if s['by'] == 'p_a' else 1)
        assert not any(w['felled'] for w in blood['wound_state'].values())
        seen += 1
    assert seen == 10


# ── (3) `yield` stops at the threshold ────────────────────────────────────────────────────────────────────────

def test_a_yield_duel_stops_at_the_health_threshold():
    from engine.season.seam.wrappers.combat import surrender_of
    frac = CFG['YIELD_HEALTH_FRAC']
    checked = 0
    for pair in _PAIRS:
        for seed in range(30):
            A0, B0 = C.Combatant('A', weapon=pair[0]), C.Combatant('B', weapon=pair[1])
            full = (A0.wt.health_full, B0.wt.health_full)
            _, ctrl, ctrl_rng, _, _ = _fight(seed, pair=pair)
            # the first event at which the control has a fighter at or below the threshold, still standing
            k = _first(ctrl, lambda e: any(0 < h <= frac * f for h, f in zip(e['_health'], full)))
            if k is None:
                continue
            result, trace, rng, A, B = _fight(seed, terms='yield', pair=pair)
            if A.felled or B.felled:
                continue     # the declared residue: a beat that crosses the threshold AND fells is a felling
            ylds = [e for e in trace if e['kind'] == 'yield']
            assert len(ylds) == 1, (pair, seed)
            ev = ylds[0]
            by = 0 if ev['by'] == 'A' else 1
            yielder = (A, B)[by]
            # the yielder is at or below the threshold; it was strictly above it at the scene's start
            assert yielder.wt.health_remaining <= frac * yielder.wt.health_full < yielder.wt.health_full
            # it is the turn the control first crossed it, and the fight is the control's up to the stop
            assert ev['turn'] == _turn_of(ctrl, k), (pair, seed, ev['turn'], _turn_of(ctrl, k))
            assert trace[:_diverge(trace)] == ctrl[:_diverge(trace)]
            assert len(rng.trace) == ev['_draws'] < len(ctrl_rng.trace)
            assert result == (-1 if by == 0 else 1) and ev['terms'] == 'yield'
            assert surrender_of(trace) == dict(by=ev['by'], turn=ev['turn'], accepted=True)
            checked += 1
    assert checked >= 20, checked


def test_yield_and_blood_are_different_stops():
    """The two terms read different quantities: on some seed the `yield` stop comes in a LATER turn than `blood`'s."""
    later = 0
    for pair in _PAIRS:
        for seed in range(30):
            tb = [e for e in _fight(seed, 'blood', pair=pair)[1] if e['kind'] == 'yield']
            ty = [e for e in _fight(seed, 'yield', pair=pair)[1] if e['kind'] == 'yield']
            if tb and ty:
                assert ty[0]['turn'] >= tb[0]['turn'], (pair, seed)
                later += ty[0]['turn'] > tb[0]['turn']
    assert later >= 1


# ── (4) `death` leaves Felled reachable ───────────────────────────────────────────────────────────────────────

def test_death_terms_leave_felled_reachable():
    from engine.season.data.rosters import COMBAT_BANDS, WOUND_QUANTITIES
    from engine.season.seam.ladder import combat_degree
    felled = 0
    for seed in range(20):
        result, trace, _, A, B = _fight(seed, terms='death')
        ends = [e for e in trace if e['kind'] == 'engagement_end' and e['felled'] is not None]
        if not ends:
            continue
        loser = A if ends[0]['felled'] == 'A' else B
        assert loser.felled and not any(e['kind'] == 'yield' for e in trace)
        st = dict(available=True, **{q: getattr(loser.wt, q) for q in WOUND_QUANTITIES})
        assert combat_degree(dict(wound_state={loser.label: st}), loser.label) == COMBAT_BANDS[0]   # 'Felled'
        felled += 1
    assert felled >= 10, felled
