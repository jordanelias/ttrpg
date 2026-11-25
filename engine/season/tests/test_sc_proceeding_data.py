"""B24p.02 -- the proceeding entry's typed boundary: the room it accepts and the keyed ways it refuses one.

`queries/inputs.py::Input.__post_init__` is the one invariant every proceeding crosses (A-139 as corrected: a sitting
needs two distinct characters, a party may also decide). Hand-built records only; no `World`."""
from __future__ import annotations

import pytest

from engine.season.queries.inputs import Cond, Input, Present, Rite, Sitting


def _p(pid, side=None, decides=False, weight=1):
    return Present(id=pid, weight=weight, side=side, decides=decides, focus=4.0, reason=4.0, attunement=4.0,
                   presence=4.0, grace=4.0, will=4.0, rank=0.0)


def _rite(close="bench", turns=2, moves=(("for", ("argue", "rest")), ("against", ("argue", "rest")))):
    return Rite(id="t", live="claim", bears="for", reply=(("for", "may"), ("against", "must")), silence="refusal",
                issues=(), weighs=(), concede="accepts", moves=moves, close=close, turns=turns, standard=4.0,
                reason_lean=0.0, admits=(), difficulty=0.5, gravity=0.0, quorum=None, unrest=0.0)


def _inp(room, rite=None, state=None):
    return Input(rite=rite or _rite(), matter="m", room=tuple(room), grounds=(("evidence", 1.0, 1.0),), dials={},
                 state=state)


def _sitting(ended=None, ids=("a", "b"), spoken=0):
    return Sitting(tracks=tuple((i, 0.0) for i in ids), cond=tuple((i, Cond(spoken=spoken)) for i in ids), ended=ended)


def _trial():
    return [_p("a", "for"), _p("b", "against"), _p("j", decides=True)]


def test_each_refusal_is_keyed():
    def key(inp_fn):
        with pytest.raises(ValueError) as e:
            inp_fn()
        msg = str(e.value)
        assert msg.startswith("refused["), msg
        return msg[len("refused["):msg.index("]")]

    refused = {
        "one_character": lambda: _inp([_p("a", "for", True), _p("a", "against")]),
        "abridged_self": lambda: _inp([_p("a", "for"), _p("b")], _rite(close="exchange", turns=1,
                                                                     moves=(("for", ("argue",)),))),
        "no_weight": lambda: _inp([_p("a", "for"), _p("b", "against", weight=0), _p("j", decides=True)]),
        "no_adjudicator": lambda: _inp([_p("a", "for"), _p("b", "against")]),
        "nobody_speaks": lambda: _inp([_p("a"), _p("j", decides=True)]),
        "resume_yielded": lambda: _inp(_trial(), state=_sitting("yielded", ids=("a", "b", "j"))),
        "abridged_resume": lambda: _inp([_p("a", "for"), _p("j", decides=True)],
                                        _rite(close="exchange", turns=1, moves=(("for", ("argue",)),)),
                                        state=_sitting(ids=("a", "j"))),
        "room_changed": lambda: _inp(_trial(), state=_sitting(ids=("a", "b"))),
        "spent": lambda: _inp(_trial(), state=_sitting(ids=("a", "b", "j"), spoken=2)),
        "closed": lambda: _inp(_trial(), state=_sitting("rested", ids=("a", "b", "j"))),
    }
    checked = 0
    for want, build in refused.items():
        assert key(build) == want
        checked += 1
    # A-139 as corrected: two persons, one a side who also decides, is a proceeding; a lawful resume is too
    assert _inp([_p("a", "for", decides=True), _p("b", "against")]).room[0].decides
    checked += 1
    assert _inp(_trial(), state=_sitting("budget", ids=("a", "b", "j"), spoken=1)).state.ended == "budget"
    checked += 1
    assert checked == 12
