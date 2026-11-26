"""B24.03 -- the hearing's rosters and the `a verdict` prize row (HEAR_B edit 1; U5c_VERBS_residue §2).

What the loader reads, as rows: the five moves the hearing adds beside `argue`, `press`, `concede` and `rest`, the faults a sitting
records, the issue ladder's `procedure` head, and the prize `a verdict` with its bench. Later items of Batch B24-sc-hearing add
their named tests to this file.
"""
from __future__ import annotations

import pytest

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
    nothing disclosed; B24.32 gave it the four faults), so the reading is the row's and not a constant. And the switch: at `sitting_exchanges` 0 (the control, set here: shipped is 1, B24.37) a bench's sitting
    has no turns, at 1 it has the row's own."""
    from ..data.arrangements import RITES
    from ..data.rosters import PROCEEDING_FAULTS
    from ..queries import world_q
    from .test_u7_remit import DUKE, PARTY, _determine, _fold, _kinds, _open, _petition, _world

    w, d = _world(sitting_exchanges=0)
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
    assert (other.id, other.faults, other.disclosed) == ("inquisition", tuple(PROCEEDING_FAULTS), False) and other.id != rite.id


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

    w, d = _world(sitting_exchanges=0)
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


# ---- B24.15: the hearing scenario, `build_hearing` and `headless --world hearing` --------------------------------------------------------

def _sit(seed, hand=(3, 3), decide=None):
    """ONE SITTING OF `build_hearing(seed, hand)`: the accuser's `determine` of the accused, folded and then fought at ENCOUNTER, the accuser decided by `decide` (a
    `View -> Choice`, or a ready `PlayHost`) or, with none, by the NPC decider as every other attendee is. Returns `(Event kind, degree, Outcome, closing obstacle,
    closing net, Event)`."""
    from ..data.matrix import WriteClass
    from ..harness import governance_spine as G
    from ..loop.driver import SeasonDriver, mint_token
    from ..queries.inputs import PlayHost
    from ..seam.wrappers import sigma
    from ..state.carriers import Act

    w = G.build_hearing(seed, hand)
    d, got, real = SeasonDriver(w), {}, sigma._resolve_proceeding
    act = Act(id="t:det", actor=G.ACCUSER, verb="determine", via=G.ACCUSER_SEAT, payload={"subject": G.ACCUSED, "to": G.ACCUSED})
    depth = w.fixtures.get("contest_max_depth")
    out = d.resolve(mint_token(w, WriteClass.ACTS), [act], contest_max_depth=depth)
    host = decide if isinstance(decide, PlayHost) else None if decide is None else PlayHost(frozenset({G.ACCUSER}), None,
                                                                                         deciders={sigma.PROCEEDING_ROLE: decide})
    sigma._resolve_proceeding = lambda *a, **k: got.setdefault("r", real(*a, **k))
    try:
        fought = d.encounter(mint_token(w, WriteClass.ACTS), out, depth, host)
    finally:
        sigma._resolve_proceeding = real
    (event,) = [e for e in fought if e.kind.startswith("matter.")]
    return event.kind, event.degree, got["r"]["proceeding"], got["r"]["ob"], got["r"]["net"], event


def test_headless_hearing_auto_twice_same_hash():
    """GATE 2 (R-04.c3): `headless --world hearing --seed 0 --auto`, run twice under `PYTHONHASHSEED=0` in two processes (a set-order dependence a same-process comparison
    cannot see), prints one content hash; and the world the command plays holds a `matter.determined` whose `ending` lists an exchange at some seed of the first six (the season's
    own draw decides the band and the entries: seed 0's sitting is a Failure that enters none). FALSIFIER: two hashes, or no such Event in six seasons of the world."""
    import os
    import subprocess
    import sys

    from ..harness import scenarios as S
    from ..queries import world_q

    cmd = [sys.executable, "-m", "engine.season.harness.headless", "--world", "hearing", "--seed", "0", "--auto"]
    ran = [subprocess.run(cmd, capture_output=True, text=True, env={**os.environ, "PYTHONHASHSEED": "0"}, check=True).stdout.splitlines()[-1] for _ in range(2)]
    assert ran[0] == ran[1] and ran[0].startswith("CONTENT HASH: ") and len(ran[0].split()[-1]) == 32, ran
    found = False
    for seed in range(6):
        found = any(e.kind == "matter.determined" and world_q.ending_exchanges(e) for e in S.run("hearing", seed, 1)["world"].log)
        if found:
            break
    assert found


def test_two_scripts_differing_in_the_first_move_differ_in_standing_and_closing_margin():
    """GATE 3 (the entry names the closing OBSTACLE; A-25 keeps it the empty board's, so what a move moves is the board and the net the close is drawn on): the played accuser
    reads his menu (`scenarios.played_host`, the `--play` host) and two scripts differ only in the first line, `present` an exhibit or `rest`, every later line `rest`. Over 20
    seeds the standing set differs and the closing net differs in every one, the closing obstacle in none (the control: the obstacle is the form's, not the board's).
    FALSIFIER: a seed at which the two leave one standing set or one net, the moves not being load-bearing."""
    from ..harness import scenarios as S

    lines: list = []
    _sit(0, decide=S.played_host("lp_accuser", read=lambda prompt: "", out=lines.append))
    first = lines[1:next(i for i, t in enumerate(lines) if i and t.startswith("-- exchange"))]
    menu = {t.split("]")[0].strip()[1:]: t.split("]")[1].split()[0] for t in first if t.lstrip().startswith("[")}
    present, rest = (next(i for i, m in menu.items() if m == name) for name in ("present", "rest"))

    def script(first_line):
        said = iter([first_line])
        return lambda prompt: next(said, rest)
    checked = same_ob = 0
    for seed in range(20):
        a, b = (_sit(seed, decide=S.played_host("lp_accuser", read=script(line), out=lambda t: None)) for line in (present, rest))
        assert tuple(i.id for i in a[2].standing) != tuple(i.id for i in b[2].standing), seed
        assert a[4] != b[4], seed
        same_ob += a[3] == b[3]
        checked += 1
    assert checked == 20 and same_ob == checked


def test_scripted_player_echoing_the_npc_reproduces_the_auto_hash(monkeypatch):
    """GATE 4 (REM-31's shape: the mode is recorded nowhere): a host that plays the accuser and returns the NPC decider's own pick each turn (`sigma._npc_decider`, built for the
    room, asked for him) leaves the world the content hash the automated run leaves, over a season at two seeds. FALSIFIER: two hashes, there being two code paths. CONTROL: a host
    that plays him and always rests leaves another hash (the played route is the one the decider is read through)."""
    from types import SimpleNamespace

    from ..harness import scenarios as S
    from ..harness.governance_spine import ACCUSER
    from ..queries.inputs import Choice, PlayHost
    from ..seam.wrappers import sigma

    built, real = {}, sigma._npc_decider
    monkeypatch.setattr(sigma, "_npc_decider", lambda w, inp: built.__setitem__("npc", real(w, inp)) or built["npc"])   # the room's own, rebuilt for each sitting
    host = lambda f: PlayHost(frozenset({ACCUSER}), None, deciders={sigma.PROCEEDING_ROLE: f})
    checked = 0
    for seed in (1, 4):
        auto = S.run("hearing", seed, 1)["hash"]
        built.clear()
        assert S.run("hearing", seed, 1, host=host(lambda view: built["npc"](view, SimpleNamespace(id=view.mover))), person=ACCUSER)["hash"] == auto, seed
        built.clear()
        assert S.run("hearing", seed, 1, host=host(lambda view: Choice("rest")), person=ACCUSER)["hash"] != auto, seed
        checked += 1
    assert checked == 2


# ---- B24.32: the kernel's `ProofBar` is carried ---------------------------------------------------------------------------------------

def test_swapping_bears_moves_p_carried_over_200_seeds():
    """KERN_B check 6 (who bears the question): the rite's `bears` is who opens and who carries the burden of putting the matter. On one hand-built bench (one judge, two
    turns, the other side owing an answer) where both sides rest, the bearer's rest is a charge not pressed, so the room moves against whoever bears: the same 200 keys
    carry the matter at a lower share when `for` bears than when `against` does, and the closed-form `card_odds` moves the same way. NO SINGLE RESULT IS FIXED by the
    swap (each arm carries at some keys and fails at others). CONTROL: with `silence: free` no charge is levied and the swap moves nothing (the burden is the whole of what
    `bears` reaches here). FALSIFIER: a swap that leaves the share, or the card's odds, where it was."""
    from .test_sc_proceeding_module import P, _bench, _carried, _key, _silent

    shares, odds, free, checked = {}, {}, {}, 0
    for bears, other in (("for", "against"), ("against", "for")):
        reply = ((bears, "may"), (other, "must"))
        inp = _bench("bench", 1, turns=2, bears=bears, reply=reply, silence="refusal")
        shares[bears] = [_carried(inp, _silent(inp, _key("bears", i))) for i in range(200)]
        odds[bears] = P.card_odds(inp)
        loose = _bench("bench", 1, turns=2, bears=bears, reply=reply, silence="free")
        free[bears] = [_carried(loose, _silent(loose, _key("bears", i))) for i in range(200)]
        checked += len(shares[bears]) + len(free[bears])
    assert checked >= 200 and checked == 800
    assert all(0 < sum(s) < 200 for s in shares.values()), {b: sum(s) for b, s in shares.items()}      # no single result is fixed
    assert sum(shares["for"]) < sum(shares["against"]) and odds["for"] < odds["against"], (sum(shares["for"]), sum(shares["against"]), odds)
    assert free["for"] == free["against"]


def test_silence_adds_levels_only_where_the_row_lists_it():
    """KERN_B check 5 (silence is a fault where the row lists it): one sitting, the other side (`against`) presenting its item, the bearer (`for`) holding one in the
    room and resting both rounds, so the bearer rests twice with nothing of his standing on the rung. The rite's `faults` is the row's list (`sigma._rite_of` stores
    it) and the module records only what it lists: with `faults=()` nothing is recorded and no level is owed; with `("silence",)` the bearer's side owes two levels
    for each silence; with all four the sitting is the same as with silence alone (no other fault's condition holds here). At the shipped dials `fault_step` is nil
    and a level costs nothing on the draw, so the closing draw is read with `fault_step` set: the net falls under silence by the levels owed and not at all under
    `faults=()`, on the same key. FALSIFIER: a module that records a fault its rite does not list gives `faults=()` the silence levels. CONTROL: the arms differ in
    one cell, the rite's list; the room, the decider, the keys and the dials are the same."""
    from dataclasses import replace

    from ..data.rosters import PROCEEDING_FAULTS
    from ..queries.inputs import Choice, Item
    from .test_sc_proceeding_module import P, _bench, _dials, _key, _pick

    rest = _pick("none")

    def decide(view, me):                                               # `against` presents; everyone else rests
        o = next((o for o in view.options if o.move == "present"), None)
        return Choice(o.move, o.ground, o.item, o.relation) if me.side == "against" and o else rest(view, me)

    arms = {"none": (), "silence": ("silence",), "all": tuple(PROCEEDING_FAULTS)}
    ran = {}
    for name, listed in arms.items():
        inp = _bench("bench", 1, turns=2, faults=listed, admits=("record",))
        room = tuple(replace(p, items=(Item(f"i_{p.id}", "record", 1.0),)) if p.side else p for p in inp.room)
        assert inp.rite.bears == "for" and inp.rite.faults == listed and inp.dials["fault_step"] is None
        priced = replace(inp, room=room, dials=_dials(fault_step="minor"))
        ran[name] = [(P.proceed(replace(inp, room=room), _key("silence", i), decide=decide), P.proceed(priced, _key("silence", i), decide=decide)) for i in range(20)]
    checked = 0
    for (n0, p0), (n1, p1), (n4, p4) in zip(ran["none"], ran["silence"], ran["all"]):
        assert (n0.faults, n0.state.levels) == ((), ()) == (p0.faults, p0.state.levels)
        assert (n1.faults, n1.state.levels) == (("silence",) * 2, (("for", 2),) * 2) == (n4.faults, n4.state.levels)
        (_, m0), (_, m1), (_, m4) = p0.verdicts[0], p1.verdicts[0], p4.verdicts[0]
        assert m0.ob == m1.ob == m4.ob and m1.net < m0.net and m1.net == m4.net, (m0, m1, m4)      # levels owed are leverage taken from `for`, never an obstacle term
        assert n0.verdicts[0][1] == n1.verdicts[0][1]                       # the control: at the shipped nil `fault_step` the levels owed cost the draw nothing
        checked += 1
    assert checked >= 20


def test_an_attendees_turns_grow_with_effort_within_the_rows_bounds():
    """KERN_B check 9, in the form the tree has. The entry's 'an attendee at effort zero makes no move' is NOT the carried form: effort is no per-attendee budget here,
    it is one term of the rite's turns (`sigma._rite_of`: `max(lo, min(hi, effort + 1 + strife))`) and every shipped bench row has a floor `lo` of at least 1, so an
    attendee at effort 0 speaks exactly the row's floor. Through `sigma.resolve` on the `arbitration` row at `sitting_exchanges` 1: at effort 0 each speaker speaks
    the floor and no more, no effort ever gives a speaker more than the ceiling, and a speaker's beats are non-decreasing in effort over 0..5 and do grow somewhere
    (so effort is read). THE SWITCH: at the control `sitting_exchanges` 0 nobody speaks at any effort. FALSIFIER (run once, not kept): turns taken as the floor whatever the
    effort leaves every speaker's beats flat and reddens the growth arm."""
    from collections import Counter

    from ..data.arrangements import ARRANGEMENTS
    from ..seam.wrappers import sigma
    from .test_sc_proceeding_module import _key
    from .test_u7_remit import DUKE, PARTY, _fold, _open, _world

    row, (lo, hi) = ARRANGEMENTS["arbitration"], ARRANGEMENTS["arbitration"]["turns"]
    assert row["close"] == "bench" and 1 <= lo < hi

    def spoken(sx, effort):
        w, d = _world(sitting_exchanges=sx)
        _fold(w, d, _open("oc", arrangement="arbitration"))
        out = sigma.resolve(w, [DUKE, PARTY], ["dt"], "a verdict", verb="determine", subject=PARTY, rng=_key("turns", 0),
                            proceeds=(row, "full", None, None), topic=PARTY, effort=effort)
        assert out["status"] == "RESOLVED"
        return Counter(b.mover for b in out["proceeding"].beats)

    efforts, checked = range(6), 0
    ran = {e: spoken(1, e) for e in (*efforts, 9)}
    assert len(ran[0]) >= 2 and set(ran[0].values()) == {lo}                    # effort 0: each speaker the floor, exactly
    for e, got in ran.items():
        assert set(got) == set(ran[0]) and max(got.values()) <= hi, (e, got)    # no effort gives a speaker more than the ceiling
        checked += 1
    per = [max(ran[e].values()) for e in efforts]
    assert per == sorted(per) and per[-1] > per[0] and ran[9] == ran[5] == Counter({s: hi for s in ran[0]}), per    # non-decreasing, growing, and capped at the ceiling
    assert all(not spoken(0, e) for e in efforts)                               # the switch: the control, nobody speaks at any effort
    assert checked == 7


@pytest.mark.slow
def test_no_constant_decider_wins_on_all_three_hands():
    """GATE 5 (HEAR_B run 5): three constant deciders for the accuser -- always the heaviest `present`, always `argue`, always `rest` -- against the decider the NPC takes (the
    chooser's), over 200 seeded sittings on each of three hands (the accuser holds 3, 2, 1 exhibits against the accused's 1, 2, 3), the same 200 seeds for every decider. A
    decider's share is the sittings whose determination OPENS the disposal (`Overwhelming` or `Success`). FALSIFIER: one constant decider has the best share on all three
    hands, the menu being stationary. CONTROL: the shares are not all alike (a hand and a decider move what is got)."""
    from collections import Counter

    from ..queries.inputs import Choice

    def heaviest_present(view):
        weight = {i.id: i.weight for i in view.hand}
        present = [o for o in view.options if o.move == "present"]
        o = max(present, key=lambda o: weight.get(o.item, 0.0)) if present else None
        return Choice(o.move, o.ground, o.item, o.relation) if o else Choice("rest")

    def always_argue(view):
        o = next((o for o in view.options if o.move == "argue"), None)
        return Choice(o.move, o.ground, o.item, o.relation) if o else Choice("rest")
    arms = {"chooser": None, "present": heaviest_present, "argue": always_argue, "rest": lambda view: Choice("rest")}
    hands, seeds, share, checked = {"strong": (3, 1), "even": (2, 2), "weak": (1, 3)}, 200, {}, 0
    for hand, held in hands.items():
        for name, decide in arms.items():
            opened = Counter(_sit(s, held, decide)[1] for s in range(seeds))
            share[hand, name] = (opened["Overwhelming"] + opened["Success"]) / seeds
            checked += seeds
    assert checked >= 600 and checked == len(hands) * len(arms) * seeds
    best = {h: max(arms, key=lambda n: (share[h, n], n)) for h in hands}
    assert not (len(set(best.values())) == 1 and "chooser" not in best.values()), (best, share)
    assert len(set(share.values())) > 3, share


# ---- B24.38: every ending of a sitting writes (IS-B2-SC-08) --------------------------------------------------------------------------

def test_every_ending_of_a_sitting_leaves_a_durable_write():
    """`headless --world hearing --auto` at seeds 0 to 19 (the same `scenarios.run` call, two seasons): each run ends by one of the seven kinds, the row's reading is the exchange count and the
    write count of the SITTING'S OWN Events (`sitting_events`: the disposal Events of a `determine`; case-file stages, Tenures opened or closed, claims deposited to attendees), and the write count
    is above 0 in every run whose ending is a sitting held. `lapsed` IS THE ONE KIND THAT READS 0, BY DEFINITION: it is "no sitting held" (`hearing_ending`), so no Event of a sitting exists to
    write, and the test asserts the 0 there rather than skip it. FALSIFIER: a held sitting that ends with nothing written, a `lapsed` run that reads a write, an ending outside the seven, or
    twenty runs of one kind (the loop cannot pass by one kind)."""
    from collections import Counter

    from ..harness import governance_spine as G
    from ..harness import scenarios as S

    kinds, checked, held = Counter(), 0, 0
    for seed in range(20):
        r = S.run("hearing", seed, 2)
        w, tally = r["world"], G.sitting_writes(r["world"], G.ACCUSED)
        assert r["ending"] in G.HEARING_ENDINGS and r["kind"] in S.ENDING_KINDS, (seed, r["ending"])
        if r["ending"] == "lapsed":
            assert sum(tally.values()) == 0 and not G.sitting_events(w, G.ACCUSED), (seed, tally)
        else:
            assert sum(tally.values()) > 0, (seed, r["ending"], tally)
            held += 1
        assert S.SCENARIOS["hearing"].reading(w, r["seat"]).endswith(f"writes {sum(tally.values())}"), seed
        kinds[r["ending"]] += 1
        checked += 1
    assert checked == 20 and held >= 10 and len(kinds) >= 3, kinds


def test_an_adjourned_stage_is_read_by_the_next_sitting():
    """A bench that adjourns (the sitting ends `budget` on the bench member's own `adjourn`) leaves ONE `adjourned` stage on the case file, under the act of the member who adjourned, and
    the Event reads `adjourned`; the next sitting of the matter on the same file finds it (`world_q.adjournments` reads 1 before it sits, and the stage stays one after it), and its own
    ending reads by its band. CONTROL: the same sitting with its last move `rule` writes no `adjourned` stage; a sitting whose item names no case file writes none either."""
    from dataclasses import replace as _replace

    from ..data.matrix import WriteClass
    from ..harness import governance_spine as G
    from ..loop.driver import mint_token
    from ..queries import world_q
    from ..seam import Resolution
    from .test_sc_proceeding_host import _beat, _planted
    from .test_u7_remit import JUDGE, PARTY, _determine, _fold, _open, _world

    def sit(w, d, act_id, last, degree="Success", ended="budget"):
        beats = [_beat(1, "p_low", "for", 0.1), _replace(_beat(2, "p_mid", "against", -0.1), move=last)]
        act = _determine(act_id)
        w.acts.append(act)                                           # the act store holds it, as RESOLVE leaves it: the log's reader asks which act caused an Event
        return d._fold(w, mint_token(w, WriteClass.ACTS), act, Resolution(degree, _planted(beats, ended=ended)))

    w, d = _world(**JUDGE)
    _fold(w, d, _open("oc"))
    file = w.records["rec:oc"]
    before = list(file.stages)
    w.tick = G.HEARING_OPENS
    first = [e for e in sit(w, d, "dt1", "adjourn") if e.kind == "matter.determined"]
    w.log.extend(first)
    assert first and file.stages == before + [("adjourned", "p_mid")] and world_q.adjournments(w, "rec:oc") == 1
    assert G.hearing_ending(w, PARTY) == "adjourned"
    for item in w.docket:                                           # the matter is back before the room (the disposal took it off), the file the same, the first edge spent
        item["matter"] = PARTY
    for t in w.tenures:
        if t.kind == "oblige" and t.subject == PARTY:
            t.until = w.tick
    assert world_q.adjournments(w, "rec:oc") == 1                   # what the next sitting reads, before it sits
    w.tick += 1
    second = [e for e in sit(w, d, "dt2", "rule") if e.kind == "matter.determined"]
    w.log.extend(second)
    assert second and world_q.adjournments(w, "rec:oc") == 1 and G.hearing_ending(w, PARTY) == "carried"
    # the control: a closing `rule` writes no adjourned stage
    w2, d2 = _world(**JUDGE)
    _fold(w2, d2, _open("oc"))
    w2.tick = G.HEARING_OPENS
    assert [e for e in sit(w2, d2, "dt1", "rule") if e.kind == "matter.determined"] and world_q.adjournments(w2, "rec:oc") == 0


def test_a_sitting_with_its_case_file_writes_suppressed_counts_zero():
    """THE COUNTER CAN READ ZERO. `sitting_writes` counts what the matter's Events wrote SINCE THE OPENING: on the world `build_hearing` hands over, whose opening acts (`open_case`'s case file and
    clock stages, the Tenures and the claims they made) were folded before it, every cell reads 0, with the case file full of its clock's stages; after one season of the same world the cells that
    a sitting moves read above 0. FALSIFIER: a counter that reads the premise's own writes (a case file's clock stages, an opened Tenure) as the sitting's, so that no ending could fail to write."""
    from ..harness import governance_spine as G
    from ..harness import scenarios as S

    w = G.build_hearing(1)
    assert any(rec.stages for rec in w.records.values()) and w.tenures                  # the premise did write: a file with its stages, and Tenures
    assert dict(G.sitting_writes(w, G.ACCUSED)) == {"stages": 0, "tenures": 0, "claims": 0} and G.hearing_ending(w, G.ACCUSED) == "lapsed"
    ran = G.sitting_writes(S.run("hearing", 1, 1)["world"], G.ACCUSED)
    assert ran["claims"] > 0 and ran["stages"] > 0, ran
