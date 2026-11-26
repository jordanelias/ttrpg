"""PC-10a (RS-25): duel TERMS on `wrapper.fight` -- a duel need not be lethal.

Jordan, 2026-10-14: *"a duel doesn't have to be lethal"*. Under a non-lethal term the fight STOPS when a fighter's own
WoundTracker crosses it -- `blood` at the first wound, `yield` at `YIELD_HEALTH_FRAC` of Health -- and that fighter
yields, standing, through the SAME `yield` event an accepted `Yield` (PC-01, `ED-PC-0056`) emits, so the seam's
`modules/combat/fight.py::_surrender` lifts it unchanged and no band is added (H-98). `death`, the default, is the fight as it was.

The falsifiers are the plan position's own (v9 `_part7`, PC-10):
  (1) under the default lethal terms the fight is byte-identical: trace, result and every engine-level draw
      (`_draw_stream.RecordingRandom`) equal the no-`terms` call's;
  (2) a seeded `blood` fight stops at the first wound with `surrender` set and NO felling;
  (3) a seeded `yield` fight stops at the threshold;
  (4) under `death` terms Felled stays reachable;
  (5) the stop rule made a no-op sends (2) red -- run once at the build; its control
      (`test_the_blood_assertions_observe_a_missing_stop`) is retired.
The cross-TREE half of (1) -- the lethal fight equal to the pre-PC-10a engine's -- is the existing combat suite and
the draw-stream pins, which this position does not move.

B15.10 (A-24): whether a fighter who crosses the terms yields is a ROLL (`wrapper._yield_roll`, `CFG['YIELD_OB']`), under every term, `death`
included. These tests pin the TERMS (where a round is cut, the one `yield` event, no riposte after it, the tie rule) at the roll's two
extremes -- `_ALWAYS`: no pool beats an obstacle of +99 (he yields at his first roll) and none fails one of -99 (`death` never yields, the
lethal fight as it was) -- and the roll's own shares are read in `test_combat_yield_draw.py` and in `test_yield_and_blood_are_different_stops`.
"""
from engine.dice_engine import draw

import pytest


from valoria import _draw_stream as DS          # noqa: E402  the single owner of the draw instrument (CLAUDE.md §8)

from modules.combat import combatant as C                            # noqa: E402
from modules.combat import wrapper                                   # noqa: E402
from modules.combat.config import CFG                           # noqa: E402

_PAIRS = (('arming', 'arming'), ('spear', 'arming'), ('longsword', 'dagger'))
_ALWAYS = dict(CFG, YIELD_OB={'blood': 99, 'yield': 99, 'death': -99})   # the roll at its extremes: yield at the first roll under `blood` and `yield`, never under `death`


def _fight(seed, terms=None, pair=_PAIRS[0], cfg=_ALWAYS):
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
        result = wrapper.fight(A, B, cfg, rng, **kw)
    finally:
        wrapper._TRACE = prev
    return result, trace, rng, A, B


def _turn_of(trace, i):
    """The 1-based round event `i` falls in (0 before the first `round_start`)."""
    return sum(1 for e in trace[:i + 1] if e['kind'] == 'round_start')


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
            for cfg in (_ALWAYS, CFG):    # at the shipped roll `death` yields sometimes, but a fight with no terms is the `death` fight all the same
                r0, t0, g0, _, _ = _fight(seed, pair=pair, cfg=cfg)
                r1, t1, g1, _, _ = _fight(seed, terms='death', pair=pair, cfg=cfg)
                assert (r1, t1, g1.trace) == (r0, t0, g0.trace), (pair, seed)
                assert not any(e.get('reason') == 'terms' for e in t1), (pair, seed)   # `death` never cuts a round
                if cfg is _ALWAYS:
                    assert not any(e['kind'] == 'yield' for e in t1), (pair, seed)
                checked += 1
    assert checked == 240


def test_a_term_outside_the_closed_set_is_refused_by_name():
    A, B = C.Combatant('A'), C.Combatant('B')
    for bad in ('first_blood', '', None, 'Death'):
        with pytest.raises(ValueError, match='terms'):
            wrapper.fight(A, B, CFG, draw.seeded(draw.H2("test_combat_duel_terms", 0)), terms=bad)
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
    from engine.season.queries.inputs import Surrender
    from modules.combat.fight import _surrender as surrender_of    # the module's one lift of the yield event (B14.01)
    _, ctrl, ctrl_rng, _, _ = _fight(seed, pair=pair)
    result, trace, rng, A, B = _fight(seed, terms='blood', pair=pair)
    k = _first(ctrl, lambda e: max(e['_wounds']) >= 1)
    first_wounded = 'A' if ctrl[k]['_wounds'][0] >= 1 else 'B'
    # The stop: exactly one `yield`, unrefused, by the fighter the first wound fell on, in the turn it fell in.
    ylds = [e for e in trace if e['kind'] == 'yield']
    assert len(ylds) == 1, [e['kind'] for e in trace[-6:]]
    ev = ylds[0]
    assert ev['by'] == first_wounded and ev['accepted'] is True and ev['refused'] is None and ev['terms'] == 'blood'
    assert ev['round'] == _turn_of(ctrl, k), (ev['round'], _turn_of(ctrl, k))
    # Up to the stop, the fight IS the control, draw for draw; the control then ran on and drew more.
    assert trace[:_diverge(trace)] == ctrl[:_diverge(trace)]
    assert len(rng.trace) == ev['_draws'] and len(rng.trace) < len(ctrl_rng.trace)
    # Nothing follows the yield but the result: no riposte draw.
    assert [e['kind'] for e in trace[trace.index(ev) + 1:]] == ['fight_result']
    # NO DEATH: nobody felled, the yielder read by the existing bands (never Felled), the opponent's result.
    from engine.season.data.rosters import COMBAT_BANDS, WOUND_QUANTITIES
    from engine.season.seam.ladder import combat_degree
    yielder = A if first_wounded == 'A' else B
    assert not A.felled and not B.felled
    st = dict(available=True, **{q: getattr(yielder.wt, q) for q in WOUND_QUANTITIES})
    assert combat_degree(dict(wound_state={first_wounded: st}), first_wounded) == COMBAT_BANDS[1]   # 'Wounded'
    assert result == (-1 if first_wounded == 'A' else 1)
    assert surrender_of(trace) == Surrender(by=first_wounded, round=ev['round'], accepted=True)


def test_a_blood_duel_stops_at_the_first_wound_with_surrender_set_and_no_death():
    cases = _blood_cases()
    assert len(cases) >= 6, cases
    for pair, seed in cases:
        _assert_blood_stop(pair, seed)
    assert {('A' if _fight(s, 'blood', pair=p)[0] == -1 else 'B') for p, s in cases} == {'A', 'B'}, \
        'both sides yield somewhere in the sample, so the yielder is not hard-wired to one label'


def test_the_module_entry_reads_the_terms_off_the_typed_input():
    """`fight.py` passes `inp.terms` when the record carries it, the lethal default when it does not. The field is
    the season's to declare (PC-10b); a subclass stands in for it here."""
    from dataclasses import dataclass
    from engine.season.queries.inputs import PersonalCombatInput
    from modules.combat import fight as entry   # the composition row's `target:` module

    @dataclass(frozen=True)
    class _Termed(PersonalCombatInput):
        terms: str = 'death'

    qs = ('felled', 'wounds', 'health_remaining', 'health_full')
    seen = 0
    for seed in range(10):
        bare = entry.fight(PersonalCombatInput(('p_a', 'p_b'), (4, 4), qs), draw.seeded(draw.H2("test_combat_duel_terms", seed)), cfg=_ALWAYS)
        death = entry.fight(_Termed(('p_a', 'p_b'), (4, 4), qs, 'death'), draw.seeded(draw.H2("test_combat_duel_terms", seed)), cfg=_ALWAYS)
        blood = entry.fight(_Termed(('p_a', 'p_b'), (4, 4), qs, 'blood'), draw.seeded(draw.H2("test_combat_duel_terms", seed)), cfg=_ALWAYS)
        assert death == bare                              # the record: wounds, yield, beat, rounds and trace
        assert bare.surrender is None
        s = blood.surrender
        # the integer `wrapper.fight` returns is not in the record; the engine's own `fight_result` event names it
        won = next(e['result'] for e in blood.trace if e['kind'] == 'fight_result')
        assert s is not None and won == (-1 if s.by == 'p_a' else 1)
        assert not any(w.felled for w in blood.wounds.values())
        seen += 1
    assert seen == 10



# ── (3) `yield` cuts a round at the threshold ─────────────────────────────────────────────────────────────────

_NEVER = dict(CFG, YIELD_OB={'blood': -99, 'yield': -99, 'death': -99})   # no pool fails these: the fighter always fights on, so the burst-breaker's cut is read alone


def _crossings(ctrl, full, frac):
    """The control's events at which a standing fighter is at or below the threshold having taken a wound gate in the round he is in (the burst-breaker's
    crossing, `wrapper._terms_crossed`); `_wounds` at each `round_start` is the round's opening count."""
    w0 = [0, 0]
    out = []
    for i, e in enumerate(ctrl):
        if e['kind'] == 'round_start':
            w0[:] = e['_wounds']
        if any(0 < h <= frac * f and w > o for h, f, w, o in zip(e['_health'], full, e['_wounds'], w0)):
            out.append(i)
    return out


def test_a_yield_duel_cuts_the_round_at_the_health_threshold():
    """The `yield` term's line is the burst-breaker's: with the roll passed every time (`_NEVER`) the round is cut at the beat head after the
    first crossing of the line, in the turn the control (the same fight with no terms) first crossed it, and the fight is the control's up to it."""
    frac = CFG['YIELD_HEALTH_FRAC']
    checked = 0
    for pair in _PAIRS:
        for seed in range(30):
            A0, B0 = C.Combatant('A', weapon=pair[0]), C.Combatant('B', weapon=pair[1])
            full = (A0.wt.health_full, B0.wt.health_full)
            _, ctrl, ctrl_rng, _, _ = _fight(seed, pair=pair, cfg=_NEVER)
            cross = _crossings(ctrl, full, frac)
            if not cross:
                continue
            result, trace, rng, A, B = _fight(seed, terms='yield', pair=pair, cfg=_NEVER)
            assert not any(e['kind'] == 'yield' for e in trace), (pair, seed)
            i = _first(trace, lambda e: e.get('reason') == 'terms')
            # a cut follows a crossing in its own round (a crossing in a round's last beat ends the round on its own, with no beat head after it)
            assert i is not None and any(c < i and _turn_of(ctrl, c) == _turn_of(trace, i) for c in cross), (pair, seed)
            assert trace[:i] == ctrl[:i]
            checked += 1
    assert checked >= 20, checked


def test_a_yield_duel_stops_at_the_first_failed_roll():
    """With the roll failed every time (`_ALWAYS`) the scene ends at the end of the first round in which a fighter took a wound gate: the one
    `yield` event, `degree` `fail`, the opponent's result, no riposte draw, and the fight is the control's up to the round's end."""
    from engine.season.queries.inputs import Surrender
    from modules.combat.fight import _surrender as surrender_of    # the module's one lift of the yield event (B14.01)
    checked = 0
    for pair in _PAIRS:
        for seed in range(30):
            _, ctrl, ctrl_rng, _, _ = _fight(seed, pair=pair)
            result, trace, rng, A, B = _fight(seed, terms='yield', pair=pair)
            if A.felled or B.felled:
                continue     # the declared residue: a beat that crosses the threshold AND fells is a felling
            ylds = [e for e in trace if e['kind'] == 'yield']
            if not ylds:
                continue     # a tie (both failed at the same Health) ends undecided with no yield: the tie test reads it
            assert len(ylds) == 1, (pair, seed)
            ev = ylds[0]
            by = 0 if ev['by'] == 'A' else 1
            assert (A, B)[by].wt.wounds >= 1 and ev['terms'] == 'yield' and ev['degree'] == 'fail' and ev['accepted'] is True
            first_gate = _first(ctrl, lambda e: max(e['_wounds']) >= 1)
            assert ev['round'] == _turn_of(ctrl, first_gate), (pair, seed, ev['round'], _turn_of(ctrl, first_gate))
            assert len(rng.trace) == ev['_draws'] < len(ctrl_rng.trace)   # the roll takes no position of the stream
            assert result == (-1 if by == 0 else 1)
            assert surrender_of(trace) == Surrender(by=ev['by'], round=ev['round'], accepted=True)
            checked += 1
    assert checked >= 20, checked


def test_yield_and_blood_are_different_stops():
    """The two terms read different quantities: with the roll passed every time (`_NEVER`) the `yield` term's first cut comes in a LATER turn than
    `blood`'s on some seed."""
    later = 0
    checked = {pair: 0 for pair in _PAIRS}
    for pair in _PAIRS:
        for seed in range(30):
            tb, ty = (_fight(seed, terms, pair=pair, cfg=_NEVER)[1] for terms in ('blood', 'yield'))
            ib, iy = (_first(t, lambda e: e.get('reason') == 'terms') for t in (tb, ty))
            if ib is not None and iy is not None:
                assert _turn_of(ty, iy) >= _turn_of(tb, ib), (pair, seed)
                later += _turn_of(ty, iy) > _turn_of(tb, ib)
                checked[pair] += 1
    # the comparison is conditional on both terms cutting a round: it must have run at least once per pair
    assert all(n >= 1 for n in checked.values()), checked
    assert later >= 1
    # THE ROLL'S SHARES (B15.10): at the shipped `YIELD_OB` a fighter across the `yield` line fights on to a felling more often than one across
    # the `blood` line (the `yield` obstacle is lower), and under neither is the stop certain nor the felling
    felled = {}
    for terms in ('blood', 'yield'):
        n = 150
        felled[terms] = sum(1 for seed in range(n) for _, _, _, A, B in [_fight(seed, terms, cfg=CFG)] if A.felled or B.felled) / n
    assert 0 < felled['blood'] < felled['yield'] < 1, felled


# ── (4) `death` leaves Felled reachable ───────────────────────────────────────────────────────────────────────

def test_death_terms_leave_felled_reachable():
    from engine.season.data.rosters import COMBAT_BANDS, WOUND_QUANTITIES
    from engine.season.seam.ladder import combat_degree
    felled = 0
    for seed in range(20):
        result, trace, _, A, B = _fight(seed, terms='death')
        ends = [e for e in trace if e['kind'] == 'round_end' and e['felled'] is not None]
        if not ends:
            continue
        loser = A if ends[0]['felled'] == 'A' else B
        assert loser.felled and not any(e['kind'] == 'yield' for e in trace)
        st = dict(available=True, **{q: getattr(loser.wt, q) for q in WOUND_QUANTITIES})
        assert combat_degree(dict(wound_state={loser.label: st}), loser.label) == COMBAT_BANDS[0]   # 'Felled'
        felled += 1
    assert felled >= 10, felled


# ── the exact-tie ending (PC-11) ──────────────────────────────────────────────────────────────────────────────────

def _fight_with_stub_engagement(monkeypatch, damage_A, damage_B, terms):
    """One `fight` whose first engagement is a stub that wounds both fighters at once and ends without a felling, so
    BOTH cross the terms on the same beat and both fail their yield roll (`_ALWAYS`): the one situation `_terms_yielder`'s tie branch exists for."""
    A, B = C.Combatant('A', weapon='arming'), C.Combatant('B', weapon='arming')

    def _both_cross(A_, B_, first, cfg, rng, prev_closed=False, terms=None, turn=1, scene=0):
        A_.apply_wound(damage_A); B_.apply_wound(damage_B)
        return None, False, 'terms'
    monkeypatch.setattr(wrapper, 'engagement', _both_cross)
    trace = []
    monkeypatch.setattr(wrapper, '_TRACE', trace.append)
    return wrapper.fight(A, B, _ALWAYS, draw.seeded(draw.H2("test_combat_duel_terms", 0)), terms=terms), trace, A, B


def test_an_exact_tie_through_the_host_entry_ends_the_fight_with_nobody_yielded(monkeypatch):
    """The same tie through the HOST's loop (`modules.combat.fight.fight`, B16.01), not the workbench's: the stub engagement wounds both parties to the same
    Health on the first beat, both fail their yield roll (`_ALWAYS`), and the round's trace carries the engine's `fight_result` (result 0, no winner) that
    `fight` reads to stop. FALSIFIER: a host loop that ignores the marker runs on to the next round (`rounds` above 1) or names a yielder."""
    from engine.season.queries.inputs import PersonalCombatInput
    from modules.combat import fight as host

    def _both_cross(A_, B_, first, cfg, rng, prev_closed=False, terms=None, turn=1, scene=0, **kw):
        A_.apply_wound(A_.wt.wi); B_.apply_wound(B_.wt.wi)
        return None, False, 'terms'
    monkeypatch.setattr(wrapper, 'engagement', _both_cross)
    inp = PersonalCombatInput(claimants=("p_a", "p_b"), ends=(4, 4), terms="blood", wound_quantities=("felled", "wounds"))
    out = host.fight(inp, draw.seeded(draw.H2("test_combat_duel_terms", 1)), cfg=_ALWAYS)
    assert out.surrender is None and out.rounds == 1, (out.surrender, out.rounds)
    assert [e for e in out.trace if e['kind'] == 'fight_result'] == [dict(kind='fight_result', result=0, winner=None)]
    assert not any(e['kind'] == 'yield' for e in out.trace)


def test_an_exact_tie_on_the_terms_ends_unresolved_with_no_yield(monkeypatch):
    """Both fighters cross `blood` on the same beat with the same Health left: nobody yields, the fight ends
    UNRESOLVED (result 0, no winner) on the first beat. The control (the same stub, unequal
    damage) yields the one who is worse off, so the assertion can observe the tie branch being absent."""
    wi = C.Combatant('A', weapon='arming').wt.wi
    result, trace, A, B = _fight_with_stub_engagement(monkeypatch, wi, wi, 'blood')
    assert A.wt.wounds >= 1 and B.wt.wounds >= 1 and not (A.felled or B.felled)
    assert result == 0
    assert [e for e in trace if e['kind'] == 'fight_result'] == [dict(kind='fight_result', result=0, winner=None)]
    assert not any(e['kind'] == 'yield' for e in trace)
    assert sum(e['kind'] == 'round_start' for e in trace) == 1      # a tie ends the fight; it does not fight on
    assert wrapper._terms_yielder(A, B, [A, B]) is None

    # control: unequal damage, same stub -> the fighter with the smaller fraction of Health left yields
    result, trace, A, B = _fight_with_stub_engagement(monkeypatch, 2 * wi, wi, 'blood')
    assert result == -1 and [e['by'] for e in trace if e['kind'] == 'yield'] == ['A']
