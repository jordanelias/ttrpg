"""B24p.07 -- the proceeding's exchange (`modules/social_contest/proceeding.py`): the module's own behaviour, on hand-built records.

No `World`, no driver: a `Present` is built by hand, the dials are `proceeding_dials(DEFAULT_FIXTURES)` (every setting at its control) with the two
rosters the host hands in (`dials["moves"]`, `dials["reads"]`, see the module's head). The role tests of the six attributes are `test_sc_roles.py`'s.
Shared with the sitting's and the close's tests (B24p.11, .12)."""
from __future__ import annotations

import ast
import importlib
from fractions import Fraction
from itertools import product
from pathlib import Path

import pytest

from engine.dice_engine import draw
from engine.dice_engine.sigma_leverage import governing_mean, pool_of, weighted_tenth

from ..data.arrangements import GROUNDS, PROCEEDING_MOVES, RITES
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.rosters import roster
from ..queries.inputs import Choice, Cond, Input, Point, Present, Rite, SocialContestInput, Sitting
from ..seam.wrappers.sigma import proceeding_dials
from ._fresh_process import probe

FX = DEFAULT_FIXTURES


class _Lazy:
    """A module of `modules/`, loaded when a test first touches it: `engine/` names no module code by import (A-25,
    `tests/valoria/test_engine_does_not_import_systems.py` reads this directory too), and the proceeding's composition row is B24p.12's."""

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


def _p(pid, side=None, decides=False, **kw) -> Present:
    a = dict(weight=1, focus=4.0, reason=4.0, attunement=4.0, presence=4.0, grace=4.0, will=4.0, rank=0.0)
    a.update(kw)
    return Present(id=pid, side=side, decides=decides, **a)


def _rite(close="bench", turns=2, moves=None, **kw) -> Rite:
    base = dict(id="t", live="claim", bears="for", reply=(("for", "may"), ("against", "must")), silence="refusal", issues=(), weighs=(),
                concede="accepts", close=close, turns=turns, standard=4.0, reason_lean=0.0, admits=(), difficulty=0.5, gravity=0.0,
                quorum=None, unrest=0.0, moves=moves or (("for", tuple(PROCEEDING_MOVES)), ("against", tuple(PROCEEDING_MOVES))))
    base.update(kw)
    return Rite(**base)


def _inp(room, rite=None, dials=None, grounds=None) -> Input:
    grounds = grounds or tuple((g, r["reason"], 1.0) for g, r in GROUNDS.items())
    return Input(rite=rite or _rite(), matter="m", room=tuple(room), grounds=grounds, dials=dials or _dials())


def _sit(inp, **kw) -> Sitting:
    return Sitting(tracks=tuple((p.id, p.start) for p in inp.room), cond=tuple((p.id, Cond()) for p in inp.room), **kw)


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
        inp = _inp([sp, to], rite)
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
    for mid in PROCEEDING_MOVES:
        for mover in (inp.room[0], inp.room[1]):
            rng = _Counting(_key("count", checked).key)
            ground = "consequence" if PROCEEDING_MOVES[mid]["draw"] else None
            P.view(inp, _sit(inp), mover, rng)
            P.exchange(inp, _sit(inp), mover, Choice(mid, ground, None, None), rng)
            assert rng.normals == P.DRAWS_PER_EXCHANGE(G) == 35 and rng.n == 2 * 35, (mid, mover.id, rng.normals)
            checked += 1
    assert checked == 2 * len(PROCEEDING_MOVES)


def test_no_branch_names_a_move_a_rite_or_a_ground():
    """Scripting drift in game code: the module reads cells (`effect`, `draw`, `reads`, the rite's); a string equal to a move, rite or ground
    id anywhere in it is a branch on an entity. The `TERMS` keys are obstacle-roster members (`press` is one) and are exempt."""
    tree = ast.parse(Path(P.__file__).read_text())
    exempt = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and any(getattr(t, "id", None) == "TERMS" for t in node.targets):
            exempt = {id(k) for k in node.value.keys}
    ids = set(PROCEEDING_MOVES) | set(RITES) | set(GROUNDS)
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


_IMPORT = """
import sys, os
sys.path.insert(0, {root!r})
before = set(sys.modules)
import {target}
print(repr(sorted(os.path.relpath(m.__file__, {root!r}) for n, m in list(sys.modules.items())
                  if n not in before and getattr(m, "__file__", None) and os.path.abspath(m.__file__).startswith({root!r} + os.sep))))
"""


def test_the_module_imports_the_dice_engine_and_the_record_leaf_only():
    """A-25 for the proceeding: importing it, in a fresh interpreter, loads the dice engine, the record leaf and its own package and no part of
    the host (no `World`, no registry): a later import of one would hand the module the world it must not read. (`test_social_contest_module.py`
    reads this of the entries a prize row names; the proceeding's composition row is B24p.12's.)"""
    loaded = probe(_IMPORT, "modules.social_contest.proceeding", 300)
    allowed = {"engine/__init__.py", "engine/season/__init__.py", "engine/season/queries/__init__.py", "engine/season/queries/inputs.py",
               "modules/__init__.py"}
    stray = [f for f in loaded if f not in allowed and not f.startswith("engine/dice_engine/") and not f.startswith("modules/social_contest/")]
    assert not stray, stray
    assert "engine/season/queries/inputs.py" in loaded and "modules/social_contest/proceeding.py" in loaded
