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


# ---- B24.09: one default rite, as data -----------------------------------------------------------------------------------------------

def test_a_rite_naming_an_unrostered_move_is_refused():
    """The loader's refusal is the standing contract on what a rite may name: a move or bench move outside `proceeding_moves`, a fault outside
    `proceeding_faults`, a `bears:` key outside `issue_rungs` or a side outside the two, each stops the load naming the cell. The unplanted
    `default` row loads (the control: each refusal is the planted cell's, not the row's)."""
    import copy

    import pytest

    from ..data import arrangements as A
    from ..data.rosters import load_yaml

    row = next(r for r in load_yaml(A.ARRANGEMENTS_YAML.read_text(encoding="utf-8"))["rites"] if r["id"] == "default")
    rite = A._load_rite(copy.deepcopy(row))
    assert rite["bench"] == ("rule", "adjourn") and rite["faults"] == tuple(A.PROCEEDING_FAULTS) and rite["disclosed"] is True
    assert dict(rite["bears_by_rung"]) == {"procedure": "for", "fact": "for", "definition": "for", "justification": "against"}
    assert A.RITES["default"] == rite
    planted = [
        (lambda r: r["moves"]["for"].append("filibuster"), r"names move\(s\) of the `for` side \['filibuster'\] outside .*proceeding_moves"),
        (lambda r: r["moves"]["bench"].append("filibuster"), r"names move\(s\) of the `bench` side \['filibuster'\] outside .*proceeding_moves"),
        (lambda r: r["faults"].append("sulking"), r"names fault\(s\) \['sulking'\] outside .*proceeding_faults"),
        (lambda r: r["bears"].update(motive="for"), r"`bears: 'motive'`.*issue_rungs"),
        (lambda r: r["bears"].update(fact="bench"), r"`bears\.fact: 'bench'`"),
    ]
    refused = 0
    for plant, why in planted:
        bad = copy.deepcopy(row)
        plant(bad)
        with pytest.raises(SystemExit, match=why):
            A._load_rite(bad)
        refused += 1
    assert refused == len(planted)


# ---- B24.10: the host builder's reading of the rite, and the sitting of no exchanges through the host -----------------------------------

def _heard(w, act, claimants, **kw):
    """`(row, form, Input)` the host builds for `act` (a `determine`) on the docket as the seam would hand it (`world_q.proceeding_row`)."""
    from ..queries import world_q
    from ..seam.wrappers import sigma
    row, form, _move, _item = world_q.proceeding_row(w, act)
    inp, _card = sigma.proceeding_input(w, claimants, verb=act.verb, subject=act.payload["subject"], topic=act.payload["subject"], effort=0, row=row, form=form, **kw)
    return row, form, inp


def test_a_computed_case_is_heard_under_the_default_rite():
    """`IS-B2-SC-03` step 3 (falsifier): `proceeding_input` reads the rite of the docket item's arrangement row, and `default` where the item names none (every
    computed `open_case`, `world_q.proceeding_row`'s second entry for a `determine`): the built `Rite` carries the default's own cells (the bench's moves beside
    the sides', the faults, `disclosed`, who bears each rung). CONTROL, one change: a case filed under `examination` is heard under ITS rite (`inquisition`:
    no faults, nothing disclosed), so the reading is the row's and not a constant. And the switch: at `sitting_exchanges` 0 (shipped) a bench's sitting
    has no turns, at 1 it has the row's own."""
    from ..data.arrangements import RITES
    from ..data.rosters import PROCEEDING_FAULTS
    from ..queries import world_q
    from .test_u7_remit import DUKE, PARTY, _determine, _fold, _kinds, _open, _petition, _world

    w, d = _world()
    assert _kinds(_fold(w, d, _open("oc"))) == ["case.opened"]
    assert world_q.docketed(w, PARTY)[0][world_q.DOCKET_ARRANGEMENT] is None            # a computed case: the item names no row
    row, form, inp = _heard(w, _determine("dt"), [DUKE, PARTY])
    cells, rite = RITES["default"], inp.rite
    assert (form, row["rite"], rite.id) == ("full", "default", "default")
    assert dict(rite.moves)["bench"] == ("rule", "adjourn") == cells["bench"] and dict(rite.moves)["for"] == cells["moves"]["for"]
    assert rite.faults == tuple(PROCEEDING_FAULTS) and rite.disclosed is True
    assert dict(rite.bears_by_rung) == dict(cells["bears_by_rung"]) and rite.bears == cells["bears"] == "for"
    assert rite.turns == 0 and row["turns"][0] > 0                                       # the control: the row's own turns are not nil
    w1, _d1 = _world(sitting_exchanges=1)
    _fold(w1, _d1, _open("oc"))
    assert _heard(w1, _determine("dt"), [DUKE, PARTY])[2].rite.turns == row["turns"][0]  # at 1 the row's own, which `effort` 0 and `peace` give the floor of
    named, nd = _world()
    assert _kinds(_fold(named, nd, _open("oc", arrangement="examination", petition=_petition(named)))) == ["case.opened"]
    other = _heard(named, _determine("dt"), [DUKE, PARTY])[2].rite
    assert (other.id, other.faults, other.disclosed) == ("inquisition", (), False) and other.id != rite.id


def test_a_sitting_of_no_exchanges_is_todays_roll_through_the_host():
    """GATE 1 (unit, through the host): a `determine` heard at `sitting_exchanges` 0 is the record the one `roll` takes -- the bench's draw -- and nothing else: the
    provider's `net` and `ob` are `roll`'s own on the record the sitting's seat closes by, the generator the same, no beat spoken and nothing on the board.
    FALSIFIER: an exchange the host let run (a beat), a board effect on the close, or a second draw (the margin would differ from `roll`'s at the same key).
    CONTROL: the shipped sitting has a seat that decides, so the reference record is the one he closes on."""
    from engine.dice_engine.sigma_leverage import pool_of

    from ..queries import world_q
    from ..queries.inputs import SocialContestInput
    from ..seam.wrappers import sigma
    from .test_sc_proceeding_module import ROLL, _key
    from .test_u7_remit import DUKE, PARTY, _determine, _fold, _kinds, _open, _world

    w, d = _world()
    assert _kinds(_fold(w, d, _open("oc"))) == ["case.opened"]
    row, form, inp = _heard(w, _determine("dt"), [DUKE, PARTY])
    seat, = [p for p in inp.room if p.decides]
    D, checked, bands = inp.dials, 0, set()
    assert D["proof_level"] is not None and D["track_step"] > 0 and inp.rite.turns == 0
    for i in range(30):
        out = sigma.resolve(w, [DUKE, PARTY], ["dt"], "a verdict", verb="determine", subject=PARTY, rng=_key("host", i), proceeds=(row, form, None, None), topic=PARTY)
        ref = ROLL.roll(SocialContestInput(pool=pool_of(D["attribute_mid"], 0, D["pool_add"], D["pool_floor"]), opposition=D["attribute_mid"],
                                           obstacle_ceiling=None, obstacle_refusal_multiple=float("inf"), leverage=D["track_step"] * seat.start,
                                           difficulty=inp.rite.difficulty, pool_default=D["pool_default"], pool_add=D["pool_add"],
                                           opposition_rate=D["opposition_rate"], obstacle_operands=(("gravity", inp.rite.gravity, 1.0),)), _key("host", i))
        assert out["status"] == "RESOLVED" and (out["net"], out["ob"]) == (ref.net, ref.ob), (i, out, ref)
        assert out["proceeding"].beats == () and out["proceeding"].standing == () and out["proceeding"].faults == (), i
        bands.add(round(out["settled_margin"], 1) > 0)
        checked += 1
    assert checked == 30 and bands == {True, False}                                        # the draw is live: the margin falls on both sides of nothing


# ---- B24.13: the hearing's NPC decider ---------------------------------------------------------------------------------------------

def test_the_hearing_decider_picks_a_legal_move_by_a_draw(monkeypatch):
    """`IS-B2-SC-04` (HEAR_B edit 8), through the live path (`sigma._played_by`, as `_resolve_proceeding` hands it to the entry): 200 keyed draws on a hand-built `View`
    each return a `Choice` that is an option of the view, and with no cell authored on `hearing_move` and a flat menu every legal move and every ground of `argue` is
    picked at least once -- the pick is the sampler's draw over equal scores, never a fixed function of the board. Then one change: a cell on `hearing_move=argue` (and
    his one weighted axis) moves the draw toward `argue` for the person who weighs it, and `p_carried` is asked of the move (the believed chance): a draw whose odds his
    interior sets."""
    from ..data import verbs as V
    from ..decision import choose as CH
    from ..queries.inputs import Cond, Option, PlayHost, View
    from ..seam.wrappers import sigma
    from .test_u7_remit import DUKE, PARTY, _determine, _fold, _kinds, _open, _world

    w, d = _world(sitting_exchanges=1)
    assert _kinds(_fold(w, d, _open("oc"))) == ["case.opened"]
    _row, _form, inp = _heard(w, _determine("dt"), [DUKE, PARTY])
    me = next(p for p in inp.room if p.side == "for")
    assert sigma._played_by(w, None, inp) == {}                                                # CONTROL, shipped: no role listed, the sitting is automatic
    w, _d = _world(sitting_exchanges=1, npc_decider_roles=("social_contest.proceeding",))
    assert set(sigma._played_by(w, None, inp)["deciders"]) == {p.id for p in inp.room if p.side}
    assert sigma._played_by(w, PlayHost(frozenset({me.id}), None), inp)["deciders"].keys() == {p.id for p in inp.room if p.side} - {me.id}   # a person the host plays is not the NPC's
    moves, grounds = dict(inp.rite.moves)["for"], [g for g, _, _ in inp.grounds]
    assert len(moves) > 2 and len(grounds) > 1
    options = tuple(Option(m, g, None, "raises", 0.0, 0.5) for m in moves for g in (grounds if m in ("argue", "press") else (None,)))
    menu = [(o.move, o.ground, o.item, o.relation) for o in options]
    decide = sigma._played_by(w, None, inp)["deciders"][me.id]

    def picks(count):
        return [decide(View(n, me.id, "for", "procedure", 2, None, None, options, Cond(), 0.0, 0.0, 0.0, False, (), 0.0, 0.5, 0.0, 1.0), me)
                for n in range(count)]

    bare = picks(200)
    assert len(bare) == 200 and all(c in menu for c in bare)
    assert {c.move for c in bare} == set(moves), {c.move for c in bare}                      # a constant decider fails here
    assert {c.ground for c in bare if c.move == "argue"} == set(grounds)
    assert picks(200) == bare                                                                  # keyed: the same stream gives the same picks

    axis = "grandiose_humble"
    monkeypatch.setattr(CH, "project", lambda person, shift=0.0, **read: {a: (1.0 if a == axis else 0.0) for a in V.ALIGNMENT})
    asked, module = [], sigma._proceeding_module()
    real = module.p_carried
    monkeypatch.setattr(module, "p_carried", lambda i, track, board=0.0: asked.append(track) or real(i, track, board))
    monkeypatch.setattr(V, "ALIGNMENT", {**V.ALIGNMENT, axis: {**V.ALIGNMENT.get(axis, {}), "choice:hearing_move=argue": 0.3}})
    celled = picks(200)
    assert asked and all(c in menu for c in celled)
    assert [c.move for c in celled].count("argue") > [c.move for c in bare].count("argue")
    # the believed chance is signed by side: a better perceived worth raises the mover's own chance, whichever side he is on (unsigned, `against` would fall)
    for side in ("for", "against"):
        v = View(0, me.id, side, "procedure", 2, None, None, (), Cond(), 0.0, 0.0, 0.0, False, (), 0.2, 0.5, 0.0, 1.0)
        low, high = (sigma._believed_chance(inp, sigma._Pick((), v), Option("argue", None, None, "raises", ev, None)) for ev in (-2.0, 2.0))
        assert 0.0 <= low < high <= 1.0, (side, low, high)


# ---- B24.14: the sitting is written on the case file and on the Event ---------------------------------------------------------------

def test_a_sitting_appends_its_exchanges_to_the_case_file():
    """A determination whose sitting entered an item and then struck it leaves two stages on the file `open_case` minted, `(kind, item)` in the beats'
    order, and an `ending` listing the same two; a determination whose sitting entered nothing leaves the file's stages and the ending as they were.
    FALSIFIER: the Event and the file are one list (`inputs.exchanges`), so an exchange on one and not the other fails the equality; a determination of an
    item that names no case file writes the Event alone."""
    from dataclasses import replace as _replace

    from ..data.matrix import WriteClass
    from ..loop.driver import mint_token
    from ..queries import world_q
    from ..seam import Resolution
    from .test_sc_proceeding_host import _beat, _planted
    from .test_u7_remit import DUKE, JUDGE, PARTY, _act, _determine, _fold, _open, _world

    def determined(beats, case=True):
        w, d = _world(**JUDGE)
        _fold(w, d, _open("oc"))
        if not case:
            for item in w.docket:
                item[world_q.DOCKET_CASE] = None
        file = w.records["rec:oc"]
        before = list(file.stages)
        act = _determine("dt")
        events = d._fold(w, mint_token(w, WriteClass.ACTS), act, Resolution("Success", _planted(beats)))
        return file, before, [e for e in events if e.kind == "matter.determined"]

    first = _replace(_beat(1, "p_low", "for", 0.1), entered=("i1",))
    second = _replace(_beat(2, "p_mid", "against", -0.1), struck=("i1",))
    file, before, events = determined([first, second])
    assert events and before and all(len(s) == 3 for s in before)                                  # the file was opened with its clock stages
    assert file.stages == before + [("entered", "i1"), ("struck", "i1")]
    ended = {e.ending for e in events}
    assert len(ended) == 1 and world_q.ending_exchanges(events[0]) == (("entered", "i1"), ("struck", "i1")) == tuple(file.stages[len(before):])
    # the control: a sitting that entered and struck nothing writes neither
    file, before, events = determined([_beat(1, "p_low", "for", 0.1), _beat(2, "p_mid", "against", -0.1)])
    assert events and file.stages == before and world_q.ending_exchanges(events[0]) == () and all(t[0] != "exchange" for t in events[0].ending)
    # the falsifier's other arm: an item with no case file lists its exchanges on the Event alone
    file, before, events = determined([first, second], case=False)
    assert events and file.stages == before and world_q.ending_exchanges(events[0]) == (("entered", "i1"), ("struck", "i1"))
