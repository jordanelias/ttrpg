"""B24.03 -- the hearing's rosters and the `a verdict` prize row (HEAR_B edit 1; U5c_VERBS_residue §2).

What the loader reads, as rows: the five moves the hearing adds beside `argue`, `press`, `concede` and `rest`, the faults a sitting
records, the issue ladder's `procedure` head, and the prize `a verdict` with its bench. Later items of Batch B24-sc-hearing add
their named tests to this file.
"""
from __future__ import annotations

from ..data import rosters as R
from ..data.rosters import PROCEEDING_FAULTS, PROCEEDING_MOVES, ISSUE_RUNGS, roster_map
from ..manifest import registry

HEARING_MOVES = ("present", "answer", "impugn", "rule", "adjourn")


def test_the_hearing_rosters_load_with_the_rows_named():
    assert tuple(PROCEEDING_MOVES)[:4] == ("argue", "press", "concede", "rest")    # the speech's four keep their place and their cells
    assert tuple(PROCEEDING_MOVES)[4:] == HEARING_MOVES
    effects = R.roster("proceeding_effects", ordered=True)
    assert {PROCEEDING_MOVES[m]["effect"] for m in HEARING_MOVES} == {"exhibit", "answer", "impugn", "rule", "adjourn"} <= set(effects)
    assert [m for m, r in PROCEEDING_MOVES.items() if r["draw"]] == ["argue", "press", "answer", "impugn"]
    assert PROCEEDING_MOVES["impugn"]["capability"] == "argue" and set(PROCEEDING_MOVES["answer"]["capability"]) == set(ISSUE_RUNGS)   # B24.04: answer's is by rung
    assert {m for m, r in PROCEEDING_MOVES.items() if r.get("descends")} == {"concede"}
    # no effect, and so no move, names a winner or a side (V2 p2 §D: the close is each adjudicator's own draw)
    assert not [e for e in effects if any(w in e for w in ("win", "lose", "side", "verdict"))]
    assert PROCEEDING_FAULTS == ("self_contradiction", "silence", "forgery_found", "irrelevance")
    assert tuple(ISSUE_RUNGS) == ("procedure", "fact", "definition", "justification")
    assert ISSUE_RUNGS["procedure"]["weighs"] == {}                                  # every ground alike
    assert all(ISSUE_RUNGS[r]["weighs"] for r in ("fact", "definition", "justification"))


def test_the_verdict_prize_is_heard_by_the_bench_and_sat_at_encounter():
    row = roster_map("contest_subsystems", "prizes")["a verdict"]
    assert (row["heard_by"], row["step"], row["declares"]) == ("bench", "ENCOUNTER", "Declared")
    assert (row["module"], row["provider"]) == (roster_map("contest_subsystems", "prizes")["a matter"]["module"],
                                                  roster_map("contest_subsystems", "prizes")["a matter"]["provider"])
    assert (("contest", "a verdict") in registry.check_rows())                         # `_check_heard_by` and the step pair read the row at boot


# ---- B24.05: the hearing's records, and the host's role-keyed deciders ---------------------------------------------------------------

def test_the_hearing_records_are_frozen_and_world_free():
    """A record a later batch makes mutable (or hands a carrier) breaks `04` §A.2's module contract: it would be state the module keeps."""
    import dataclasses

    import pytest

    from ..queries.inputs import Beat, Item, Outcome, PlayHost, Sitting, View

    item = Item("i", "record", 1.0)
    assert (item.side, item.rung, item.cell, item.origin, item.forged_found) == (None, None, (), None, False)    # the added cells default: B24p's callers are unchanged
    out = Outcome((), Sitting(), "budget", None, ())
    assert (out.standing, out.faults) == ((), ())
    assert {"board", "hand"} <= {f.name for f in dataclasses.fields(View)}
    for rec, cell in ((item, "weight"), (out, "standing"), (Sitting(), "n")):
        with pytest.raises(dataclasses.FrozenInstanceError):
            setattr(rec, cell, 0)
    for cls in (Item, Beat, View, Outcome):
        for f in dataclasses.fields(cls):
            assert "World" not in str(f.type), (cls.__name__, f.name)         # no field is typed as a carrier (the instance walk is `test_sc_proceeding_host._carriers`)

    host = PlayHost(frozenset({"a"}), lambda v: "x")                           # built as today: no deciders, and `decide` still the combat fight's
    assert host.deciders == {} and host.decide(None) == "x"
    mine = {"social_contest.proceeding": lambda v: None}
    assert PlayHost(frozenset(), None, deciders=mine).deciders is mine
    assert PlayHost(frozenset(), None).deciders is not PlayHost(frozenset(), None).deciders   # a default mapping is not shared between hosts



# ---- B24.06: the board's effects and faults, on the proceeding's exchange and ballot -------------------------------------------------

def test_a_sitting_of_no_exchanges_is_todays_roll():
    """GATE 1 (unit): a sitting where no turn is spoken (`sitting_exchanges` 0: the rite's turns are nil) closes by `roll` on the one record `determine` throws,
    at the shipped settings and whatever each seat's start, and writes nothing on the board. A board that reached the close of an empty sitting would be
    a second roll."""
    from dataclasses import replace

    from engine.dice_engine.sigma_leverage import pool_of

    from ..queries.inputs import SocialContestInput
    from .test_sc_proceeding_module import P, ROLL, _bench, _key

    inp, checked = _bench("bench", 1, turns=0, difficulty=1.0), 0
    D = inp.dials
    assert D["proof_level"] is not None and D["track_step"] > 0                      # shipped: the board's levels would act if one stood
    for i in range(30):
        start = (i - 15) / 10.0
        room = tuple(replace(p, start=start) if p.decides else p for p in inp.room)
        out = P.proceed(replace(inp, room=room), _key("today", i))
        ref = ROLL.roll(SocialContestInput(pool=pool_of(D["attribute_mid"], 0, D["pool_add"], D["pool_floor"]), opposition=D["attribute_mid"],
                                           obstacle_ceiling=None, obstacle_refusal_multiple=float("inf"), leverage=D["track_step"] * start, difficulty=1.0,
                                           pool_default=D["pool_default"], pool_add=D["pool_add"], opposition_rate=D["opposition_rate"],
                                           obstacle_operands=(("gravity", inp.rite.gravity, 1.0),)), _key("today", i))
        assert out.beats == () and out.verdicts == (("j0", ref),) and (out.standing, out.faults) == ((), ()), (i, out.verdicts, ref)
        checked += 1
    assert checked == 30


def test_a_favourable_exhibit_never_lowers_the_obstacle():
    """A-25: an item that stands for the party reaches the closing draw as leverage (the net rises) and never as a subtraction from the obstacle (`ob` and
    its `terms` are the empty board's); one that stands against him lowers the net and leaves the obstacle alone. The item enters by the exchange's own `present`."""
    from ..queries.inputs import Choice, Item
    from .test_sc_proceeding_module import P, _inp, _key, _p, _rite, _sit

    a, b = _p("a", "for", items=(Item("i1", "record", 2.0),)), _p("b", "against", items=(Item("i2", "record", 1.0),))
    inp = _inp([a, b, _p("j0", decides=True, precedence=1)], _rite(close="bench", admits=("record",)))
    empty = _sit(inp)
    sat_for, _beat = P.exchange(inp, empty, a, Choice("present", None, "i1"), _key("board", 0))
    sat_against, _beat = P.exchange(inp, empty, b, Choice("present", None, "i2"), _key("board", 1))
    assert [(it.id, it.side, it.weight, s) for it, s in sat_for.board] == [("i1", "for", 2.0, "stands")] and sat_against.board[0][0].side == "against"
    checked = 0
    for i in range(40):
        none, plus, minus = (P._close(inp, st, _key("close", i))[0][0][1] for st in (empty, sat_for, sat_against))
        assert plus.ob == none.ob == minus.ob and plus.terms == none.terms == minus.terms      # the obstacle is the empty board's, to the term
        assert plus.net > none.net > minus.net, (i, plus.net, none.net, minus.net)             # the board is leverage: one level `proof_level` per whole unit of weight
        checked += 1
    assert checked == 40
