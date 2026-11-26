"""B24p.07 -- the proceeding's exchange (`modules/social_contest/proceeding.py`): the module's own behaviour, on hand-built records.

No `World`, no driver: a `Present` is built by hand, the dials are `proceeding_dials(DEFAULT_FIXTURES)` (every setting at V2's shipped value since B24p.23; the control test sets its own, `CONTROL`) with the two
rosters the host hands in (`dials["moves"]`, `dials["reads"]`, see the module's head). The role tests of the six attributes are `test_sc_roles.py`'s.
Shared with the sitting's and the close's tests (B24p.11, .12)."""
from __future__ import annotations

import ast
import importlib
from dataclasses import replace
from fractions import Fraction
from itertools import product
from pathlib import Path

import pytest

from engine.dice_engine import draw
from engine.dice_engine.sigma_leverage import M_MAX, governing_mean, pool_of, weighted_tenth

from ..data.arrangements import GROUNDS, PROCEEDING_MOVES, RITES
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.rosters import PROCEEDING_FAULTS, roster
from ..queries.inputs import Choice, Cond, Input, Point, Present, Rite, SocialContestInput, Sitting
from ..seam.wrappers.sigma import proceeding_dials

FX = DEFAULT_FIXTURES


class _Lazy:
    """A module of `modules/`, loaded when a test first touches it: `engine/` names no module code by import (A-25,
    `tests/valoria/test_engine_does_not_import_systems.py` reads this directory too): the proceeding is reached by its composition row, not an import."""

    def __init__(self, name):
        self._name = name

    def __getattr__(self, attr):
        return getattr(importlib.import_module(self._name), attr)


P = _Lazy("modules.social_contest.proceeding")
ROLL = _Lazy("modules.social_contest.roll")


def _dials(fx=FX, **over) -> dict:
    d = dict(proceeding_dials(fx))
    d["moves"] = {m: (r["effect"], r["draw"]) for m, r in PROCEEDING_MOVES.items()}
    d["reads"] = {g: r["reads"] for g, r in GROUNDS.items()}
    d.update(over)
    return d


#: THE FIFTEEN SETTINGS B24p.04 SHIPPED AT THEIR CONTROL and B24p.23 flipped to V2's value (the model's `CONTROL_ZERO`): a level None, a step 0.
CONTROL = dict(fit_level=None, answer_level=None, repeat_step=0.0, esteem_step=0.0, off_step=0.0, ploy_step=0.0, grain_strain=0.0, heard_step=0.0,
               gap_step=0.0, weary_step=0.0, awe_step=0.0, room_level=0.0, heckle=0.0, crowd_lean=0.0, start_step=0.0)


def _p(pid, side=None, decides=False, **kw) -> Present:
    a = dict(weight=1, focus=4.0, reason=4.0, attunement=4.0, presence=4.0, grace=4.0, will=4.0, rank=0.0)
    a.update(kw)
    return Present(id=pid, side=side, decides=decides, **a)


def _rite(close="bench", turns=2, moves=None, **kw) -> Rite:
    base = dict(id="t", live="claim", bears="for", reply=(("for", "may"), ("against", "must")), silence="refusal", issues=(), weighs=(),
                concede="accepts", close=close, turns=turns, standard=4.0, reason_lean=0.0, admits=(), difficulty=0.5, gravity=0.0,
                quorum=None, unrest=0.0, moves=moves or (("for", tuple(PROCEEDING_MOVES)), ("against", tuple(PROCEEDING_MOVES))),
                faults=tuple(PROCEEDING_FAULTS))   # B24.32: the module records only what the rite lists, so the double lists the four (`faults=()` is the rite that lists none)
    base.update(kw)
    return Rite(**base)


def _inp(room, rite=None, dials=None, grounds=None) -> Input:
    grounds = grounds or tuple((g, r["reason"], 1.0) for g, r in GROUNDS.items())
    return Input(rite=rite or _rite(), matter="m", room=tuple(room), grounds=grounds, dials=dials or _dials())


def _sit(inp, **kw) -> Sitting:
    base = dict(tracks=tuple((p.id, p.start) for p in inp.room), cond=tuple((p.id, Cond()) for p in inp.room))
    return Sitting(**{**base, **kw})


def _key(label, n=0):
    return draw.seeded(draw.H2(label, n))


class _Counting(draw.Draw):
    """a keyed `Draw` that counts its normals (each is two uniforms, `Draw.normal`)."""

    def __init__(self, key):
        super().__init__(key)
        self.normals = 0

    def normal(self, mu, sigma):
        self.normals += 1
        return super().normal(mu, sigma)


def test_at_control_an_abridged_speech_is_the_single_roll():
    """With every setting at its control and every ground's `reason` 1.0, the abridged speech's margin IS `roll` on the record the single
    act builds -- Reason (plus rank) the dice, the addressed man's Will (plus rank) the opposition, the same keyed draw -- over 200 hand-built
    pairs. The continuity every later batch must preserve: the proceeding at control is the single roll (V2 p3 §B: 200 of 200)."""
    checked = 0
    for i in range(200):
        g = _key("pair", i)
        sp = _p("a", "for", reason=g.die(10, 70) / 10, presence=float(g.die(1, 7)), attunement=float(g.die(1, 7)),
                focus=float(g.die(1, 7)), will=float(g.die(1, 7)), rank=float(g.die(0, 3)))
        to = _p("b", decides=True, will=g.die(10, 70) / 10, rank=float(g.die(0, 3)))     # tenths: a pool rounded to a whole die reads differently
        rite = _rite(close="exchange", turns=1, moves=(("for", ("argue",)),), difficulty=(0.5, 1.0, 2.0)[i % 3], gravity=(0.0, 0.5, 1.5)[i % 3])
        inp = _inp([sp, to], rite, dials=_dials(**CONTROL), grounds=tuple((g, 1.0, 1.0) for g in GROUNDS))
        st = _sit(inp)
        ground = [x for x, r in GROUNDS.items() if r["reads"] != "item"][i % 3]
        rng = _key("speech", i)
        P.view(inp, st, sp, rng)
        _, beat = P.exchange(inp, st, sp, Choice("argue", ground, None, None), rng)
        D = inp.dials
        ref_rng = _key("speech", i)
        for _ in range(P.DRAWS_PER_EXCHANGE(len(inp.grounds)) - 1):     # the speech is the exchange's last normal
            ref_rng.normal(0.0, 1.0)
        ref = ROLL.roll(SocialContestInput(pool=pool_of(sp.reason + sp.rank, 0, D["pool_add"], D["pool_floor"]), opposition=to.will + to.rank,
                                      obstacle_ceiling=None, obstacle_refusal_multiple=float("inf"), leverage=0.0, difficulty=rite.difficulty,
                                      pool_default=D["pool_default"], pool_add=D["pool_add"], opposition_rate=D["opposition_rate"],
                                      obstacle_operands=(("gravity", rite.gravity, 1.0),)), ref_rng)
        assert beat.margin == ref.net - ref.ob, (i, beat.margin, ref.net - ref.ob)
        names = [n for n, _ in beat.terms]
        assert set(names) <= set(roster("obstacle_terms")) | {"floor", "ceiling"}, names     # a term the roster does not name never reaches `Margin.terms`
        assert {k: v for k, v in beat.terms if k in dict(ref.terms)} == dict(ref.terms) and sum(v for _, v in beat.terms) == sum(v for _, v in ref.terms)
        checked += 1
    assert checked == 200


def test_an_exchange_takes_exactly_its_draws():
    """Every exchange takes `DRAWS_PER_EXCHANGE(G)` normals whatever the move: `rest` and `concede` take as many as a speech or a press. The
    stream contract determinism rests on: a count that varied by move would move every later draw of the sitting."""
    inp = _inp([_p("a", "for"), _p("b", "against"), _p("j", decides=True)])
    G = len(inp.grounds)
    assert P.DRAWS_PER_EXCHANGE(4) == 35 and G == 4
    checked = 0
    speech = [m for m, r in PROCEEDING_MOVES.items() if r["effect"] in ("track", "strike", "yield", "none")]   # B24.03: the hearing's five are the sitting's, not this entry's
    assert len(speech) == 4
    for mid in speech:
        for mover in (inp.room[0], inp.room[1]):
            rng = _Counting(_key("count", checked).key)
            ground = "consequence" if PROCEEDING_MOVES[mid]["draw"] else None
            mark = rng.n
            P.view(inp, _sit(inp), mover, rng)
            P.exchange(inp, _sit(inp), mover, Choice(mid, ground, None, None), rng, mark=mark)
            assert rng.normals == P.DRAWS_PER_EXCHANGE(G) == 35 and rng.n == 2 * 35, (mid, mover.id, rng.normals)
            checked += 1
    assert checked == 2 * len(speech)


def test_no_branch_names_a_move_a_rite_or_a_ground():
    """Scripting drift in game code: the module reads cells (`effect`, `draw`, `reads`, the rite's); a string equal to a move, rite or ground
    id anywhere in it is a branch on an entity. The `TERMS` keys are obstacle-roster members (`press` is one) and are exempt."""
    tree = ast.parse(Path(P.__file__).read_text())
    exempt = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and any(getattr(t, "id", None) == "TERMS" for t in node.targets):
            exempt = {id(k) for k in node.value.keys}
    # B24.06: four hearing moves (`answer`, `impugn`, `rule`, `adjourn`) share their id with their EFFECT, and the module reads effects (`proceeding_effects`)
    # by name as it reads `track` and `strike`; a string that is an effect name is that read, not a branch on the move
    ids = (set(PROCEEDING_MOVES) | set(RITES) | set(GROUNDS)) - set(roster("proceeding_effects"))
    strings = [n for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, str) and id(n) not in exempt]
    assert len(ids) >= 16 and len(strings) > 100
    assert sorted(n.value for n in strings if n.value in ids) == []


def _answering():
    """a room where `against` has put a point that stands (0.3) with j1, not with j2; `for` answers it."""
    dials = _dials(FX.sweep("fit_level", "strong").sweep("answer_level", "moderate"))
    inp = _inp([_p("a", "for"), _p("b", "against"), _p("j1", decides=True), _p("j2", decides=True)], dials=dials)
    point = Point(0, "against", "m", "consequence", None, "b", (("j1", -0.3), ("j2", 0.0)))
    st = _sit(inp, points=(point,), live=(("for", None), ("against", 0)))
    return inp, st


def test_an_answer_is_bounded_both_ways_and_offered_only_to_a_standing_point():
    """An answer undoes the other side's live point and no more: with the listener it moves him by at most how far the point stands with him
    on a win and costs him at most `flop` of that on a loss; with a listener it does not stand with it moves nothing; and it is on the menu
    only while the point stands (C1, C5)."""
    inp, st = _answering()
    flop, s = inp.dials["flop"], 0.3
    ups = downs = 0
    for i in range(80):
        _, beat = P.exchange(inp, st, inp.room[0], Choice("argue", "consequence", None, "answers"), _key("answer", i))
        moved = dict(beat.moved)
        assert beat.relation == "answers"
        assert -flop * s - 1e-12 <= moved["j1"] <= s + 1e-12 and moved["j2"] == 0.0 and moved["b"] == 0.0, moved
        ups += moved["j1"] > 0
        downs += moved["j1"] < 0
    assert ups > 10 and downs > 10, (ups, downs)
    assert any(o[3] == "answers" for o in P.menu(inp, st, inp.room[0], 2)[0])
    dead = _sit(inp, points=(Point(0, "against", "m", "consequence", None, "b", (("j1", 0.3), ("j2", 0.0))),), live=(("for", None), ("against", 0)))
    assert not any(o[3] == "answers" for o in P.menu(inp, dead, inp.room[0], 2)[0])
    _, beat = P.exchange(inp, dead, inp.room[0], Choice("argue", "consequence", None, "answers"), _key("answer", 0))
    assert beat.relation == "raises"


def test_weighted_tenth_is_the_governing_rule_weighted():
    """`weighted_tenth` is `governing_mean` with the weights Reason's share of the dice gives it: exact in tenths on every integer pair and
    share, equal to it at equal weights, a value halfway between two tenths rounding up on scores that carry a tenth (a banker's rounding or
    a float mean would move the blended pool of every speech that lands on one), and it refuses what the rule refuses."""
    checked = 0
    for a, b in product(range(1, 8), repeat=2):
        for t in range(11):
            assert weighted_tenth((a, b), (t, 10 - t)) == float(Fraction(a * t + b * (10 - t), 10)), (a, b, t)
            checked += 1
        assert weighted_tenth((a, b), (5, 5)) == governing_mean((a, b))
    assert checked == 7 * 7 * 11
    halves = 0
    for a, b in product(("1.0", "2.5", "2.6", "3.3", "6.9"), repeat=2):
        for t in range(11):
            mean = (t * Fraction(a) + (10 - t) * Fraction(b)) / 10
            want = Fraction((mean * 10 + Fraction(1, 2)).__floor__(), 10)
            assert weighted_tenth((float(a), float(b)), (t, 10 - t)) == float(want), (a, b, t)
            halves += (mean * 10).denominator == 2
    assert halves > 0
    for bad in (lambda: weighted_tenth((-1, 4), (5, 5)), lambda: weighted_tenth((4, 4), (-1, 11)), lambda: weighted_tenth((4, 4), (5, 4))):
        with pytest.raises(ValueError):
            bad()


# ---------------------------------------------------------------------------------------------------------------- B24p.11: the sitting
def _pick(effect):
    """a played chooser: the first option of the given `effect` cell on his menu."""
    def decide(view, me):
        o = next((o for o in view.options if PROCEEDING_MOVES[o.move]["effect"] == effect), view.options[0])
        return Choice(o.move, o.ground, o.item, o.relation)
    return decide


def _top(view, me):
    """the view-best chooser: the top perceived option, the earlier of equals."""
    o = max(view.options, key=lambda o: o.ev)
    return Choice(o.move, o.ground, o.item, o.relation)


def _tracks_are_start_plus_moves(inp, out):
    """a track is each person's own: its start (or the resumed state's) plus the sum of the beats' moves on him, never a verdict."""
    base = dict(inp.state.tracks) if inp.state else {p.id: p.start for p in inp.room}
    T, checked = dict(out.state.tracks), 0
    for p in inp.room:
        assert abs(T[p.id] - (base[p.id] + sum(d for b in out.beats for h, d in b.moved if h == p.id))) < 1e-9, p.id    # a running sum: float noise only
        checked += 1
    assert checked == len(inp.room)


def test_one_turn_under_an_abridged_row_and_no_callback_is_asked():
    """The abridged act is one speech nobody watches: `proceed` runs it on the automatic policy and asks no callback, played or default."""
    def boom(view, me):
        raise AssertionError("a callback was asked in an abridged sitting")
    inp = _inp([_p("a", "for"), _p("b", decides=True)], _rite(close="exchange", turns=1, moves=(("for", ("argue",)),)))
    out = P.proceed(inp, _key("abridged"), decide=boom, deciders={"a": boom, "b": boom})
    assert [b.mover for b in out.beats] == ["a"] and out.ended == "budget" and out.ended_by is None and out.state.ended == "budget"


def test_the_bearer_opens_and_the_rest_follow_by_precedence():
    """The side that bears the live thing opens, its seconds by precedence, then the other side by precedence, each round, until each has
    spoken the rite's turns; and `_mover` names nobody once all have."""
    room = [_p("a", "for", precedence=1), _p("b", "for", precedence=5), _p("c", "against", precedence=9), _p("d", "against", precedence=2),
            _p("j", decides=True)]
    inp = _inp(room, _rite(turns=2))
    seen = []
    track = _pick("track")
    out = P.proceed(inp, _key("order"), decide=lambda v, me: (seen.append(me.id), track(v, me))[1])
    assert seen == ["b", "a", "c", "d"] * 2 and [b.mover for b in out.beats] == seen and out.ended == "budget"
    assert P._mover(inp, out.state) is None and P._mover(inp, _sit(inp)) == "b"


def test_every_end_is_reachable_and_is_never_a_verdict():
    """`budget` (the turns are spent), `rested` (a whole round with nothing to say), `yielded` (the matter given up) each end a sitting from a
    planted room; none fixes a band or a side: each leaves the tracks as start plus what was said, and a final concession puts the room as
    far against its maker as the close can carry it and names who yielded."""
    room = [_p("a", "for", start=0.4), _p("b", "against", start=-0.2), _p("j", decides=True, start=0.1)]
    inp = _inp(room, _rite(turns=2))
    ends = {}
    for name, decide in (("budget", _pick("track")), ("rested", _pick("none")), ("yielded", _pick("yield"))):
        out = P.proceed(inp, _key("end"), decide=decide)
        assert out.ended == out.state.ended == name, (name, out.ended)
        _tracks_are_start_plus_moves(inp, out)
        ends[name] = out
    assert len(ends["budget"].beats) == 4 and ends["budget"].ended_by is None
    assert [b.move for b in ends["rested"].beats] == ["rest", "rest"] and ends["rested"].ended_by is None     # one whole round, then it stops
    assert len(ends["yielded"].beats) == 1 and ends["yielded"].ended_by == "a"
    floor, T = -M_MAX / inp.dials["track_step"], dict(ends["yielded"].state.tracks)
    assert T["j"] == pytest.approx(floor) and T["b"] == pytest.approx(floor)


def test_a_broken_temper_cannot_rest():
    """A-146: at or past `temper_break` the moves that do nothing leave his menu, for a player, the policy, and a party who decides alike;
    composed, he may rest; with his turns spent, only rest is left."""
    for decides in (False, True):
        a = _p("a", "for", decides=decides)
        inp = _inp([a, _p("b", "against"), _p("j", decides=True)])
        hot = _sit(inp, cond=tuple((p.id, Cond(heat=2.0 if p.id == "a" else 0.0)) for p in inp.room))
        assert P._broken(inp, a, dict(hot.cond)["a"]) and not P._broken(inp, a, Cond())
        assert "rest" not in P._legal(inp, hot, a) and "rest" in P._legal(inp, _sit(inp), a)
        v = P.view(inp, hot, a, _key("hot", decides))
        assert v.broke and not any(o.move == "rest" for o in v.options)
        with pytest.raises(ValueError, match=r"refused\[choice\]: a "):
            P.proceed(replace(inp, state=hot), _key("hot"), decide=lambda view, me: Choice("rest"))
        assert P.policy(inp, v, a).move != "rest"
        spent = _sit(inp, cond=tuple((p.id, Cond(heat=2.0, spoken=inp.rite.turns)) for p in inp.room))
        assert P._legal(inp, spent, a) == ("rest",)


def test_nobody_breaks_unprovoked_and_a_rattle_provokes_and_cools():
    """C4: with no rattle the temper is 0 at every Will and Grace of 1 to 7; a rattle that lands puts heat 1 on the man pressed, who is then
    past what a low Will and Grace carry, and each beat he makes cools it by `temper_cool`."""
    inp = _inp([_p("a", "for"), _p("b", "against"), _p("j", decides=True)])
    checked = 0
    for will, grace in product(range(1, 8), repeat=2):
        p = _p("x", "for", will=float(will), grace=float(grace))
        assert P.temper_of(inp, p, Cond()) == 0.0 and not P._broken(inp, p, Cond())
        checked += 1
    assert checked == 49
    low, presser = _p("b", "against", will=1.0, grace=1.0), _p("a", "for", reason=7.0, rank=3.0)
    inp = _inp([presser, low, _p("j", decides=True)])
    for i in range(60):
        new, beat = P.exchange(inp, _sit(inp), presser, Choice("press", "consequence", None, "presses"), _key("provoke", i))
        if beat.rattled:
            break
    else:
        raise AssertionError("no press landed in 60 keys")
    c = dict(new.cond)["b"]
    assert beat.rattled == "b" and c.rattles == 1 and c.heat == 1.0 and P._broken(inp, low, c)
    after, _ = P.exchange(inp, new, low, Choice("argue", "consequence", None, "raises"), _key("cool"))
    assert dict(after.cond)["b"].heat == pytest.approx(1.0 * (1.0 - inp.dials["temper_cool"]))


def test_a_composed_npc_is_the_view_best_chooser():
    """Below the break the automatic policy takes the top perceived option of the same view a player is shown, no other information: the
    sitting it plays equals the one a view-best callback plays, key for key (and none of these beats was a broken man's)."""
    room = [_p("a", "for", will=7.0, grace=7.0), _p("b", "against", will=7.0, grace=7.0), _p("j", decides=True)]
    inp = _inp(room, _rite(turns=2))
    checked = 0
    for i in range(5):
        auto, played = P.proceed(inp, _key("view-best", i)), P.proceed(inp, _key("view-best", i), decide=_top)
        assert not any(b.broke for b in auto.beats) and auto == played, i
        checked += len(auto.beats)
    assert checked == 5 * 4
    heated = _sit(inp, cond=tuple((p.id, Cond(heat=1.0)) for p in inp.room))     # provoked, not broken: the temper terms are still not his
    seen = 0
    for i in range(12):
        for who in room[:2]:
            assert 0.0 < P.temper_of(inp, who, Cond(heat=1.0)) < inp.dials["temper_break"]
            v = P.view(inp, heated, who, _key("heated", i))
            assert not v.broke and P.policy(inp, v, who) == _top(v, who), (i, who.id)
            seen += 1
    assert seen == 24
    from engine.season.queries.inputs import Option     # a proud man's temperament pulls toward a press only once the temper breaks
    v = replace(P.view(inp, heated, room[0], _key("heated")), options=(Option("press", "consequence", None, "presses", 0.0, 0.5, None),
                                                                       Option("concede", None, None, "concedes", 0.3, None, None)))
    assert P.policy(inp, v, room[0]).move == "concede"


def test_a_sitting_opens_each_man_at_his_start_carrying_his_strain():
    """What a man carries in from earlier rattles and where his track starts are the sitting's opening values; nothing else is."""
    inp = _inp([_p("a", "for", start=0.4, strain=1.5), _p("b", "against", start=-0.2), _p("j", decides=True, start=0.1)])
    st = P.start(inp)
    assert dict(st.tracks) == {"a": 0.4, "b": -0.2, "j": 0.1} and dict(st.cond)["a"] == Cond(strain=1.5) and dict(st.cond)["b"] == Cond()
    assert (st.n, st.issue, st.points, st.ended) == (0, 0, (), None)


def test_a_broken_man_shows_by_temperament():
    """Past the break the proud press and will not give way, the timid give way (A-136): the same two options, nearly level, the same temper."""
    from engine.season.queries.inputs import Option
    for will, want in ((7.0, "press"), (1.0, "concede")):
        a = _p("a", "for", will=will, grace=1.0)
        inp = _inp([a, _p("b", "against"), _p("j", decides=True)])
        hot = _sit(inp, cond=tuple((p.id, Cond(heat=3.0 if p.id == "a" else 0.0)) for p in inp.room))
        v = replace(P.view(inp, hot, a, _key("shows")), options=(Option("press", "consequence", None, "presses", 0.0, 0.5, None),
                                                                   Option("concede", None, None, "concedes", 0.05, None, None)))
        assert v.broke and P.policy(inp, v, a).move == want, (will, want)


def test_a_concession_never_improves_the_conceder():
    """C5: conceding an issue moves each listener `-side x concede_step x (1 + max|stake|)` from WHERE HE STANDS (never back to his start),
    keeps the issue conceded and opens the next rung; the last rung ends the sitting `yielded` and names the conceder."""
    checked = 0
    for side, other in (("for", "against"), ("against", "for")):
        sg = 1.0 if side == "for" else -1.0
        for x in (-3.0, -0.5, 0.0, 0.5, 3.0):
            a, b = _p("a", side, stake=(0.3, 0.0, 0.0)), _p("b", other)
            inp = _inp([a, b, _p("j", decides=True, start=0.2)], _rite(turns=1, concede="descends", issues=("r1", "r2", "r3"), bears=side,
                       reply=((side, "may"), (other, "must")), moves=((side, ("argue", "concede")), (other, ("rest",)))))
            cost = inp.dials["concede_step"] * (1.0 + 0.3)
            stands = (("a", x), ("b", x), ("j", x))
            out = P.proceed(replace(inp, state=_sit(inp, tracks=stands)), _key("concede", checked), decide=_pick("yield"))
            T = dict(out.state.tracks)
            assert [x.closed for x in out.beats if x.closed] == ["r1"] and out.state.issue == 1 and out.ended == "budget" and out.ended_by is None
            for who in ("b", "j"):
                assert (T[who] - x) * sg == pytest.approx(-cost), (side, x, who)      # against the conceder's side, from where it stood
            last = P.proceed(replace(inp, state=_sit(inp, issue=2, tracks=stands)), _key("last", checked), decide=_pick("yield"))
            assert last.ended == "yielded" and last.ended_by == "a" and last.state.issue == 2
            checked += 1
    assert checked == 10


def test_a_resumed_sitting_keeps_its_count_and_issue():
    """A two-turn sitting resumed under four turns runs each speaker's two further turns: the beats go on from the count, the issue reached
    stands, nobody is given a turn he has had."""
    inp = _inp([_p("a", "for"), _p("b", "against"), _p("j", decides=True)], _rite(turns=2, concede="descends", issues=("r1", "r2", "r3")))
    first = P.proceed(inp, _key("resume"), decide=lambda v, me: _pick("yield" if (me.id == "a" and v.turns_left == 2) else "track")(v, me))
    assert first.state.n == 4 and first.state.issue == 1 and first.ended == "budget"
    again = replace(inp, rite=replace(inp.rite, turns=4), state=first.state)
    second = P.proceed(again, _key("resume", 1), decide=_pick("track"))
    assert [b.n for b in second.beats] == [5, 6, 7, 8] and {b.issue for b in second.beats} == {"r2"} and second.state.issue == 1
    assert {i: c.spoken for i, c in second.state.cond if i != "j"} == {"a": 4, "b": 4}
    _tracks_are_start_plus_moves(again, second)


def test_the_same_key_gives_the_same_sitting():
    """Determinism: the sitting is a function of the input and the key, so a replay on the same key is the same outcome, and another key is not."""
    room = [_p("a", "for", will=6.0, grace=2.0), _p("b", "against", will=2.0, grace=2.0), _p("c", "against"), _p("j", decides=True)]
    inp = _inp(room, _rite(turns=2))
    one, two, other = P.proceed(inp, _key("replay")), P.proceed(inp, _key("replay")), P.proceed(inp, _key("replay", 1))
    assert one == two and one != other and len(one.beats) >= 4


def test_the_sitting_asserts_every_exchange_takes_its_whole_draw_count():
    """The stream contract is held per exchange by the sitting: a view that takes a draw too many fails it, so no later draw of the sitting
    can move silently (`proceed` passes `mark`, `rng.n` before the view)."""
    inp = _inp([_p("a", "for"), _p("b", "against"), _p("j", decides=True)], _rite(turns=1))
    mod = importlib.import_module("modules.social_contest.proceeding")
    real = mod.view

    def greedy(inp_, st, mover, rng):
        out = real(inp_, st, mover, rng)
        rng.normal(0.0, 1.0)
        return out
    mod.view = greedy
    try:
        with pytest.raises(AssertionError):
            P.proceed(inp, _key("greedy"))
    finally:
        mod.view = real
    assert len(P.proceed(inp, _key("greedy")).beats) == 2


def test_the_speech_lands_on_the_frame_the_chooser_was_shown():
    """The frame is picked from the ground by what the speaker believes of those who decide, shown on the option, and is the one the speech
    is made on: a beat's `frame` is the frame of the option the chooser took."""
    holds = (("want", "t1", 0.8, 1.0), ("want", "t2", 0.2, 1.0))
    inp = replace(_inp([_p("a", "for"), _p("b", "against"), _p("j", decides=True, holds=holds)],
                       _rite(turns=1, moves=(("for", ("argue",)), ("against", ("rest",))))), frames=(("want", "t1"), ("want", "t2")))
    taken, rest = [], _pick("none")

    def decide(view, me):
        if me.id != "a":
            return rest(view, me)
        o = next(o for o in view.options if o.ground == "consequence")
        taken.append(o.frame)
        return Choice(o.move, o.ground, o.item, o.relation)
    out = P.proceed(inp, _key("frame"), decide=decide)
    assert taken[0] in ("t1", "t2") and out.beats[0].frame == taken[0]


# ---------------------------------------------------------------------------------------------------------------- B24p.12: the close, the odds
_NO_SPEECH = (("for", ("argue", "rest")), ("against", ("argue", "rest")))


def _bench(close="bench", n=1, quorum=None, weights=None, starts=None, **rite):
    """a sitting room: `for` and `against` speakers and `n` adjudicators j0.. (precedence falling, so j0 presides), at `starts`."""
    starts, weights = starts or [0.0] * n, weights or [1] * n
    ds = [_p(f"j{i}", decides=True, start=starts[i], precedence=n - i, weight=weights[i]) for i in range(n)]
    return _inp([_p("a", "for"), _p("b", "against")] + ds, _rite(close=close, quorum=quorum, **rite))


def _silent(inp, key, **kw):
    """the sitting where every side rests: nobody speaks, the close is the whole result."""
    return P.proceed(inp, key, decide=_pick("none"), **kw)


def _carried(inp, out) -> bool:
    """the host's reading of the verdicts (B24p.13 builds it; here it is the plain statement of it): the presiding seat's margin, the
    quorum-th best seat's, or the weight-mean, graded on the one ladder; carried is Success or better."""
    from engine.dice_engine.dice_engine import Degree, degree_from_net
    ms = {i: m.net - m.ob for i, m in out.verdicts}
    if inp.rite.close == "bench":
        m = ms[out.verdicts[0][0]]
    elif inp.rite.close == "declared":
        m = sorted(ms.values(), reverse=True)[inp.rite.quorum - 1]
    else:
        w = {p.id: p.weight for p in inp.room}
        m = sum(w[i] * x for i, x in ms.items()) / sum(w[i] for i in ms)
    return degree_from_net(m, 0.0) in (Degree.SUCCESS, Degree.OVERWHELMING)


def test_a_drawn_close_takes_one_normal_per_adjudicator():
    """A drawn close (`bench`, `declared`, `hearers`) takes one normal per adjudicator, after the sitting's own draws, and returns the presiding
    seat's alone (`bench`) or every seat's; under `consent` nothing is drawn and nothing returned, and under `exchange` the verdict is the
    speech itself and no normal is drawn."""
    checked = 0
    for close, n in (("bench", 1), ("bench", 3), ("declared", 3), ("hearers", 2), ("hearers", 4)):
        inp = _bench(close, n, quorum=2)
        rng = _Counting(_key("count", checked).key)
        out = _silent(inp, rng)
        assert rng.normals == P.DRAWS_PER_EXCHANGE(len(inp.grounds)) * len(out.beats) + n, (close, n, rng.normals)
        assert [i for i, _ in out.verdicts] == (["j0"] if close == "bench" else [f"j{i}" for i in range(n)]), (close, n)
        checked += 1
    inp = _bench("consent", 0, moves=_NO_SPEECH)
    rng = _Counting(_key("consent").key)
    out = _silent(inp, rng)
    assert out.verdicts == () and out.ruled == () and rng.normals == P.DRAWS_PER_EXCHANGE(len(inp.grounds)) * len(out.beats) > 0
    rng = _Counting(_key("exchange").key)
    out = P.proceed(_inp([_p("a", "for"), _p("j", decides=True)], _rite(close="exchange", turns=1, moves=(("for", ("argue",)),))), rng)
    assert len(out.verdicts) == 1 and rng.normals == P.DRAWS_PER_EXCHANGE(4)     # the one speech's, none for the close
    assert checked == 5


def test_a_close_is_a_draw_on_the_adjudicators_track():
    """A-14: each adjudicator's verdict is one draw on his OWN track: with the key fixed it moves with his track by exactly the leverage
    `net_boost(track_step x track)` and by nothing else, and not with any speaker's attribute; it is a `Margin` (never a band or a side) whose
    terms are the one obstacle's with `gravity` named. A yielded sitting, the room at the floor the close can carry it to, still draws: over
    200 keys it lands in more than one band (a close that fixed the band is the falsifier)."""
    from engine.dice_engine.dice_engine import degree_from_net
    from engine.dice_engine.sigma_leverage import net_boost
    from ..queries.inputs import Margin
    inp = _bench("bench", 1, gravity=0.7)
    D = inp.dials
    pool = pool_of(D["attribute_mid"], 0, D["pool_add"], D["pool_floor"])
    got = {}
    for track in (-3.0, 0.0, 3.0):
        verdicts, ruled = P._close(inp, _sit(inp, tracks=(("a", 0.0), ("b", 0.0), ("j0", track))), _key("track"))
        (who, v), = verdicts
        assert who == "j0" and type(v) is Margin and ruled == ()
        assert v.terms[-1] == ("gravity", 0.7) and dict(v.terms)["difficulty"] == inp.rite.difficulty and sum(x for _, x in v.terms) == pytest.approx(v.ob)
        got[track] = v
    assert got[0.0].ob == got[3.0].ob == got[-3.0].ob
    for track in (-3.0, 3.0):
        assert got[track].net - got[0.0].net == pytest.approx(net_boost(D["track_step"] * track, pool) - net_boost(0.0, pool))
    assert got[3.0].net > got[0.0].net > got[-3.0].net
    other = _inp([_p("a", "for", reason=7.0, presence=7.0, will=7.0, rank=3.0), _p("b", "against", will=1.0), inp.room[2]], inp.rite)
    assert P._close(other, _sit(other, tracks=(("a", 5.0), ("b", -5.0), ("j0", 3.0))), _key("track"))[0] == (("j0", got[3.0]),)
    yielded = _bench("bench", 1)
    bands, checked = set(), 0
    for i in range(200):
        rng = _Counting(_key("yielded", i).key)
        out = P.proceed(yielded, rng, decide=_pick("yield"))
        (_, v), = out.verdicts
        assert out.ended == "yielded" and dict(out.state.tracks)["j0"] == pytest.approx(-M_MAX / D["track_step"])
        assert rng.normals == P.DRAWS_PER_EXCHANGE(len(yielded.grounds)) + 1
        bands.add(degree_from_net(v.net, v.ob))
        checked += 1
    assert checked == 200 and len(bands) >= 2, bands


def test_a_close_at_control_is_the_single_roll_on_the_ordinary_bench():
    """Control: with `track_step` at 0 and `gravity` 0 a drawn close IS `roll` on the ordinary bench's record (the middle of the scale for pool
    and opposition, the rite's difficulty) at the same key, whatever the track: the close composes on the one roll and adds nothing."""
    inp = replace(_bench("bench", 1, difficulty=1.0), dials=_dials(track_step=0.0))
    D, checked = inp.dials, 0
    for i in range(50):
        got = P._close(inp, _sit(inp, tracks=(("a", 0.0), ("b", 0.0), ("j0", float(i - 25)))), _key("control", i))[0][0][1]
        ref = ROLL.roll(SocialContestInput(pool=pool_of(D["attribute_mid"], 0, D["pool_add"], D["pool_floor"]), opposition=D["attribute_mid"],
                                           obstacle_ceiling=None, obstacle_refusal_multiple=float("inf"), leverage=0.0, difficulty=1.0,
                                           pool_default=D["pool_default"], pool_add=D["pool_add"], opposition_rate=D["opposition_rate"],
                                           obstacle_operands=(("gravity", 0.0, 1.0),)), _key("control", i))
        assert got == ref, (i, got, ref)
        checked += 1
    assert checked == 50


def test_declared_carries_by_the_quorum_th_best_seat():
    """C5: a `declared` close carries when at least `quorum` seats' own draws carry, the presiding seat one vote with no veto: a presiding seat
    far for against two far against does not carry at quorum 2 (it does at quorum 1), two far for against a presiding seat far against do;
    and the card's odds are, seat by seat, the sum over every subset of seats of its probability."""
    far = 30.0     # past the leverage cap: a seat there is as for (or as against) as the close can make it
    odds = lambda q, ts: P.card_odds(_bench("declared", 3, quorum=q, starts=ts))
    up, down = P.p_carried(_bench(), far), P.p_carried(_bench(), -far)
    assert 0.5 < up < 1.0 and 0.0 < down < 0.5
    assert odds(2, [far, -far, -far]) < up and odds(2, [-far, far, far]) > down      # the presiding seat is one vote: not a veto, not a casting voice
    assert odds(2, [far, -far, -far]) < odds(2, [-far, far, far]) and odds(1, [far, -far, -far]) > odds(2, [far, -far, -far]) > odds(3, [far, -far, -far])
    ts, q, total = [4.0, -1.0, 0.5], 2, 0.0
    inp = _bench("declared", 3, quorum=q, starts=ts, silence="free")     # free: no burden charge on the bearer, each seat at his own start
    ps =[P.p_carried(inp, t) for t in ts]
    for mask in range(8):
        pr = 1.0
        for i, p in enumerate(ps):
            pr *= p if mask >> i & 1 else 1 - p
        total += pr if bin(mask).count("1") >= q else 0.0
    assert P.card_odds(inp) == pytest.approx(total, abs=1e-12)


def test_the_card_odds_are_what_a_silent_sitting_delivers():
    """A-133, p1 §E: the card's odds are P(carried) of the close itself where nobody speaks: each who decides at his own start (the rig's
    presumption among them) less what the burden charges the bearer, then the presiding seat's (`bench`), at least the quorum of the seats'
    own draws (`declared`) or the weight-mean margin (`hearers`). An approximation claim, so a tolerance is honest: 600 keyed sittings in
    which every side rests sit within three standard errors of it, at rig 0 and rig 1; `consent` and `exchange` have none."""
    seen = []
    for close, n, kw in (("bench", 1, {}), ("declared", 3, dict(quorum=2)), ("hearers", 3, dict(weights=[1, 2, 1]))):
        for rig in (0.0, 1.0):
            inp = _bench(close, n, starts=[rig * _dials()["presume_step"] + s for s in (0.0, 0.5, -0.5)[:n]], **kw)
            want = P.card_odds(inp)
            hits = sum(_carried(inp, _silent(inp, _key(f"silent-{close}-{rig}", i))) for i in range(600))
            se = (want * (1.0 - want) / 600) ** 0.5
            assert 0.05 < want < 0.95 and abs(hits / 600 - want) <= 3 * se, (close, rig, want, hits / 600, se)
            seen.append(want)
    assert len(set(seen)) == 6 and seen[1] > seen[0]
    assert P.card_odds(_bench("consent", 0, moves=_NO_SPEECH)) is None
    assert P.card_odds(_inp([_p("a", "for"), _p("j", decides=True)], _rite(close="exchange", turns=1, moves=(("for", ("argue",)),)))) is None


def test_a_played_adjudicator_rules_at_the_close_only():
    """D7: a played adjudicator is called once, at the close, with his own track, his odds and the points as they stood; he may rule for,
    against or leave it to his draw (taken whatever he rules, so the stream is the same); how far a ruling departs from his own track is
    returned; he is never consulted during the sitting."""
    inp = _bench("declared", 2, quorum=1, starts=[-1.5, 2.0])
    base = P.proceed(inp, _key("rule"), decide=_pick("track"))
    assert base.state.points and base.ruled == ()
    departed = {}
    for how, want_net in (("for", 2.0), ("against", -2.0), (None, None)):
        calls = []

        def rule(jv):
            calls.append(jv)
            return how
        rng = _Counting(_key("rule").key)
        out = P.proceed(inp, rng, decide=_pick("track"), rulings={"j0": rule})
        assert out.beats == base.beats and rng.normals == len(out.beats) * 35 + 2        # his draw is taken whatever he rules
        (jv,) = calls
        assert jv.id == "j0" and jv.points == out.state.points and jv.track == dict(out.state.tracks)["j0"]
        assert jv.odds == pytest.approx(P.p_carried(inp, jv.track))
        v = dict(out.verdicts)["j0"]
        assert out.verdicts[1] == base.verdicts[1]                           # nobody else is touched
        if how is None:
            assert out.verdicts == base.verdicts and out.ruled == ()
        else:
            assert v.net - v.ob == pytest.approx(want_net) and v.ob == dict(base.verdicts)["j0"].ob
            assert out.ruled == (("j0", round(max(0.0, -jv.track) if how == "for" else max(0.0, jv.track), 2)),)
            departed[how] = out.ruled[0][1]
    assert max(departed.values()) > 0 == min(departed.values())     # he leans one way: ruling the other way departs from his mind, ruling his own way does not


def test_one_speaker_one_turn_no_callback_is_the_speech_plus_the_addressed_mans_start():
    """Control: with one speaker, one turn and no callback, the outcome's one verdict is that speech's margin plus the addressed man's start,
    its obstacle and terms the speech's, and nothing is drawn for the close."""
    checked = 0
    for start in (-0.8, 0.0, 0.4):
        inp = _inp([_p("a", "for", reason=6.0), _p("b", decides=True, start=start)], _rite(close="exchange", turns=1, moves=(("for", ("argue",)),)))
        for i in range(10):
            rng = _Counting(_key("one", i).key)
            out = P.proceed(inp, rng)
            (who, v), = out.verdicts
            assert who == "b" and rng.normals == 35 and len(out.beats) == 1
            assert v.net - v.ob == pytest.approx(out.beats[0].margin + start) and v.terms == out.beats[0].terms    # not `==`: (net + start) - ob and (net - ob) + start differ in the last bit
            assert v.ob == pytest.approx(sum(x for _, x in v.terms))
            checked += 1
    assert checked == 30


def test_an_abridged_close_is_the_addressed_mans_own_margin_not_a_watchers():
    """The one verdict of an abridged act carries the OBSTACLE AND TERMS of the man addressed, however many hear it after him: a watcher (a
    hearer who does not decide, seated after the addressee, of another Will) is not the man the close reads. Net less obstacle is the speech's
    margin with him plus his start."""
    checked = 0
    for start in (-0.8, 0.4):
        inp = _inp([_p("a", "for", reason=6.0), _p("b", decides=True, start=start, will=3.0, rank=1.0), _p("w", will=7.0, rank=2.0)],
                   _rite(close="exchange", turns=1, moves=(("for", ("argue",)),)))
        for i in range(10):
            out = P.proceed(inp, _key("watched", i))
            (who, v), = out.verdicts
            (beat,) = out.beats
            a, to, watcher = inp.room
            own = ROLL.obstacle(P.speech(inp, _sit(inp), a, a, to, beat.ground, None, beat.relation, abridged=True)[2])
            his = ROLL.obstacle(P.speech(inp, _sit(inp), a, a, watcher, beat.ground, None, beat.relation, abridged=True)[2])
            assert own != his and (v.ob, v.terms) == own and who == "b"
            assert v.net - v.ob == pytest.approx(beat.margin + start)     # (net + start) - ob and (net - ob) + start differ in the last bit: not `==`
            checked += 1
    assert checked == 20


def test_the_view_shows_the_chooser_the_odds_of_an_ordinary_bench_on_his_reading():
    """`View.odds` is P(carried) before an ordinary bench at the track his believed mood implies (B05.62), and none under `consent`."""
    inp = _bench("bench", 1)
    v = P.view(inp, _sit(inp), inp.room[0], _key("odds"))
    assert v.odds == P.p_carried(inp, v.mood * inp.dials["mood_scale"]) and 0.0 < v.odds < 1.0
    assert P.view_odds(inp, replace(v, mood=0.9)) > P.view_odds(inp, replace(v, mood=-0.9))
    assert P.view_odds(inp, replace(v, side="against", mood=0.9)) < P.view_odds(inp, replace(v, side="for", mood=0.9))    # a room that leans HIS way is his loss on `against`
    assert P.view_odds(replace(inp, rite=replace(inp.rite, close="consent")), v) == 0.0
