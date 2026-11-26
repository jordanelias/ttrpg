"""B24p.02 -- the proceeding entry's typed boundary: the room it accepts and the keyed ways it refuses one.

`queries/inputs.py::Input.__post_init__` is the one invariant every proceeding crosses (A-139 as corrected: a sitting
needs two distinct characters, a party may also decide). Hand-built records only; no `World`."""
from __future__ import annotations

from dataclasses import replace

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


def test_the_rows_carried_from_the_kernel_load_and_run_a_sitting():
    """KERN_B check 11 (RD §C.9; COL §4 item 6): the four rows of the kernel's catalogue that the hearing keeps, `rally`, `inquisition_hearing`,
    `excommunication_deliberation` and `audience`, each LOAD (an arrangement of a rite the loader holds), the host's `_rite_of` builds the rite from the row at
    `sitting_exchanges` 1, and `social_contest.proceeding` returns an `Outcome` under it: a sitting of beats, the row's own close, and one margin for each who decides.
    Hand-built room, no `World`; 20 keys a row. FALSIFIER: a row the loader drops, a rite the builder cannot read, or a sitting that returns no verdicts."""
    from engine.season.data.arrangements import ARRANGEMENTS, CONTEXT, RITES
    from engine.season.data.fixtures import DEFAULT_FIXTURES
    from engine.season.queries.inputs import Margin, Outcome
    from engine.season.seam.wrappers import sigma
    from engine.substrate import composition

    from .test_sc_proceeding_module import GROUNDS, _dials, _key
    rooms = {
        "rally": ((_p("a", "for"), _p("h1", decides=True), _p("h2", decides=True)), 2),                                       # `hearers`: each hearer's own margin
        "inquisition_hearing": ((_p("a", "for"), _p("b", "against"), _p("j0", decides=True)), 1),                            # `bench`: the presiding seat's
        "excommunication_deliberation": ((_p("a", "for"), _p("b", "against"), _p("j0", decides=True), _p("j1", decides=True), _p("j2", decides=True)), 3),   # `declared`
        "audience": ((_p("a", "for"), _p("b", "against"), _p("j0", decides=True)), 1),                                       # `bench`
    }
    fx = DEFAULT_FIXTURES.sweep("sitting_exchanges", 1)
    regime, strife = CONTEXT["regimes"][sigma.REGIME], CONTEXT["strife"][sigma.STRIFE]
    checked = 0
    for row_id, (room, deciding) in rooms.items():
        row = ARRANGEMENTS[row_id]
        assert row["rite"] in RITES and row["id"] == row_id
        rite = sigma._rite_of(fx, "determine" if row["close"] != "hearers" else "argue", row, 1, regime, strife)
        assert (rite.id, rite.close) == (row["rite"], row["close"]) and rite.turns >= 1
        inp = _inp(room, rite)
        inp = replace(inp, dials=_dials(), grounds=tuple((g, r["reason"], 1.0) for g, r in GROUNDS.items()))
        for i in range(20):
            out = composition.require("social_contest.proceeding")(inp, _key(f"row-{row_id}", i))
            assert type(out) is Outcome and out.beats and out.ended in ("yielded", "rested", "budget"), (row_id, i)
            assert len(out.verdicts) == deciding and all(type(m) is Margin for _, m in out.verdicts), (row_id, i)
            checked += 1
    assert checked == 80
