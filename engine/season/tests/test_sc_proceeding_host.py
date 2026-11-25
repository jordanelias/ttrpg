"""B24p.13 -- the host builder and the card (V2 p2 §A, §H, §I; p1 §E): `seam/wrappers/sigma.py::proceeding_input` and `::card`.

A hand-built world (`probes.tiny_world`: realm R > duchy D > settlement S > hearth Hh, the Duke `p_high` on `off_duke`), no driver, no caller:
the builder is read on its own, and the one module call is `social_contest.proceeding` reached by its composition row, as the host reaches it.
Shared with the provider path's, the verb rows' and the written sitting's tests (B24p.14, .16, .19, .20, .22)."""
from __future__ import annotations

import copy
from dataclasses import fields, is_dataclass, replace
from types import SimpleNamespace

import pytest

from engine.dice_engine import fmath
from engine.substrate import composition

from ..data import arrangements as A
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.rosters import GROUNDS, PROCEEDING_MOVES, RUNG_KINDS
from ..harness import probes as PR
from ..gaps import Unspecified
from ..queries import person_q
from ..queries.inputs import Beat, Card, Cond, Input, Margin, Outcome, Sitting, written
from ..seam.ladder import degree_of
from ..seam.wrappers import sigma as S
from ..data.verbs import VERB_TABLE, _check_proceeds
from ..queries import world_q
from ..state.carriers import Act, Claim, Office, Person, Record, Tenure
from ..state.world import World
from .test_sc_proceeding_module import _key

CROWN, CHURCH = "Valorsmark", "Church of Solmund"
ROWS = A.ARRANGEMENTS


def PROCEED(inp, rng):
    """The entry, reached by its composition row when called: `engine/` names no module code by import (A-25), and a test file is imported by
    `test_importing_every_engine_module_pulls_in_no_subsystem`, so the row is resolved at the call and not at import."""
    return composition.require("social_contest.proceeding")(inp, rng)


def _world(**fx) -> World:
    f = DEFAULT_FIXTURES
    for name, value in fx.items():
        f = f.sweep(name, value)
    return PR.tiny_world(f)


def _seat(w, oid, who, faction=CROWN, post="Judge", rung="S", scope="D"):
    """An office at `rung` whose bench sits over `scope` (a seat with no `scope_rung` is on no bench), held by `who`."""
    off = Office(oid, post, rung, ["determine"], faction=faction)
    off.scope_rung = scope
    w.offices[oid] = off
    w.add_tenure(Tenure(f"h_{oid}", who, oid, "hold", since=0))


def _vacate(w, oid):
    for t in w.tenures:
        if t.kind == "hold" and t.object == oid:
            t.until = 0


def _build(w, claimants=("p_low",), *, row, subject="p_mid", verb="argue", topic="m1", effort=1, **kw):
    return S.proceeding_input(w, list(claimants), verb=verb, subject=subject, topic=topic, effort=effort, row=row, **kw)


def _deciders(inp):
    return tuple(p.id for p in inp.room if p.decides)


def _carriers(obj, path="input"):
    """Every carrier a record may not hold: a `Person`, a `World`, a `Tenure`, a `Record`, a `Claim`, an `Office` (a record is typed values)."""
    assert not isinstance(obj, (Person, World, Tenure, Record, Claim, Office)), f"{path} holds a {type(obj).__name__}"
    if is_dataclass(obj) and not isinstance(obj, type):
        for f in fields(obj):
            _carriers(getattr(obj, f.name), f"{path}.{f.name}")
    elif isinstance(obj, (tuple, list, set, frozenset)):
        for i, x in enumerate(obj):
            _carriers(x, f"{path}[{i}]")
    elif hasattr(obj, "items"):
        for k, v in obj.items():
            _carriers(v, f"{path}[{k!r}]")


def test_an_abridged_tell_seats_the_one_addressed_as_its_adjudicator():
    """A tell to a man is one speech nobody watches: the one addressed is seated as a hearer who decides (no side, no bench), the
    verdict is his alone, and the card names him as who decides."""
    w = _world()
    inp, card = _build(w, row=A.abridged(ROWS["conversation"]), subject="p_mid", verb="tell", effort=0)
    assert inp.rite.close == "exchange" and inp.rite.turns == 1
    addressed = next(p for p in inp.room if p.id == "p_mid")
    assert (addressed.side, addressed.decides) == (None, True)
    assert next(p for p in inp.room if p.id == "p_low").side == "for"
    assert _deciders(inp) == card.decided_by == ("p_mid",) and card.close == "exchange"
    out = PROCEED(inp, _key("host-tell"))
    assert [i for i, _ in out.verdicts] == ["p_mid"]
    assert card.odds is None                          # the verdict is the speech itself


def test_the_seat_a_self_plea_is_put_to_is_no_party_and_starts_on_his_own_ties():
    """A speech put to no man (a self-plea) is put to the presiding seat as the one addressed: he decides and is NOT the other party, so a
    party's stake floor (`bearing`'s `party=True`) is not his. His start is `start_step x mean(stake)` over his ties alone (a tie of +1 to the
    speaker starts him FOR, where the floor would have forced -0.4), and the sitting names no other party."""
    w = _world()
    w.persons["p_high"].stance = [("p_low", 5, 5)]
    inp, card = _build(w, ("p_low",), row=A.abridged(ROWS["conversation"]), subject=None, verb="speak", effort=0)
    seat = next(p for p in inp.room if p.id == "p_high")
    own = person_q.bearing(w.persons["p_high"], {}, for_party="p_low", against_party=None, edges=w.persons["p_high"].tenures, party=False)
    assert (seat.side, seat.decides) == (None, True) and card.decided_by == ("p_high",)
    assert seat.start == w.fixtures.get("start_step") * (fmath.ltr_sum(own) / person_q.BEARING_PARTS) > 0


def test_a_church_bench_seats_only_church_seats():
    """An `authority: church` row seats the church seat alone, read through the office's faction; the crown seat that would
    sit under a polity row does not; with no church seat the proceeding is refused."""
    w = _world()
    _seat(w, "off_dic", "p_other", CHURCH, post="Dicastery")
    church, polity = ROWS["inquisition_hearing"], ROWS["legal_trial"]
    assert (church["authority"], polity["authority"]) == ("church", "polity")
    inp, card = _build(w, row=church)
    assert _deciders(inp) == card.decided_by == ("p_other",)
    assert _deciders(_build(w, row=polity)[0]) == ("p_high",)
    _vacate(w, "off_dic")
    with pytest.raises(ValueError, match=r"refused\[no_seat\]"):
        _build(w, row=church)
    assert _deciders(_build(w, row=polity)[0]) == ("p_high",)      # control: the crown seat still sits under its own row


def test_a_conflicted_seat_steps_down_where_another_can_sit():
    """A seat tied to a party steps down for the next seat (`Card.recused`), kin to both parties as kin to one; where none can sit he
    sits; one with no tie presides and nobody steps down."""
    w = _world()
    _seat(w, "off_j2", "p_other")
    row = ROWS["legal_trial"]
    judge = w.persons["p_high"]
    assert _deciders(_build(w, row=row)[0]) == ("p_high",) and _build(w, row=row)[1].recused == ()
    judge.stance = [("p_low", 5, 5)]                                     # kin to one party
    inp, card = _build(w, row=row)
    assert card.recused == ("p_high",) and _deciders(inp) == ("p_other",)
    judge.stance = [("p_low", 5, 5), ("p_mid", 5, 5)]                    # kin to both: a conflict, never a cancellation
    inp, card = _build(w, row=row)
    assert card.recused == ("p_high",) and _deciders(inp) == ("p_other",)
    _vacate(w, "off_j2")                                                 # nobody else can sit: he sits, and the card shows no recusal
    inp, card = _build(w, row=row)
    assert card.recused == () and _deciders(inp) == ("p_high",)


def test_a_party_may_adjudicate():
    """An audience whose seat is the other party builds (he speaks and decides); where the presiding seat would be the sole speaker
    the next seat presides; a sitting of one character is refused."""
    w = _world()
    inp, card = _build(w, ("p_low",), row=ROWS["audience"], subject="p_high")
    seat = next(p for p in inp.room if p.id == "p_high")
    assert (seat.side, seat.decides) == ("against", True) and card.decided_by == ("p_high",)
    _seat(w, "off_j2", "p_other")
    inp, card = _build(w, ("p_high",), row=ROWS["audience"], subject=None)       # the Duke presides, and is the only speaker: the next seat
    assert card.decided_by == ("p_other",) and next(p for p in inp.room if p.id == "p_high").decides is False
    _vacate(w, "off_j2")
    with pytest.raises(ValueError, match=r"refused\[one_character\]"):
        _build(w, ("p_high",), row=ROWS["audience"], subject=None)


def test_the_rig_tilts_the_room_and_never_the_turns():
    """A rig between unequal powers moves the seat's start by `presume_step x tilt` toward the arranger and nothing else in the room or
    the rite; equals, a rite with nothing to tilt and a third party tied to neither side tilt nothing and name no arranger."""
    w = _world(start_step=2.0)
    _seat(w, "off_chancellor", "p_king", post="Chancellor", rung="R", scope=None)       # the arranger's power: a realm seat, on no bench
    w.persons["p_king"].stance = [("p_low", 5, 5)]                                       # he favours the bearer
    row, fx = ROWS["legal_trial"], w.fixtures
    built = {rig: _build(w, row=row, arranger="p_king", rig=rig) for rig in (0.0, 0.5, 1.0)}
    base, base_card = built[0.0]
    assert (base_card.tilt, base_card.arranged_by, base_card.tilted_against) == (0.0, None, None)
    power = RUNG_KINDS.index("realm") + A.CONTEXT["regimes"]["crown"]["power"]["polity"]      # his seat's rung and the regime's weight; the weak party holds none
    for rig in (0.5, 1.0):
        inp, card = built[rig]
        tilt = rig * fmath.tanh(power / fx.get("power_scale"))
        assert inp.rite == base.rite and inp.rite.turns == base.rite.turns         # turns are never cut
        assert (card.arranged_by, card.tilted_against) == ("p_king", "against") and card.tilt == round(tilt, 2) > 0
        moved = [p for p, p0 in zip(inp.room, base.room) if p != p0]
        assert [p.id for p in moved] == ["p_high"] and moved[0].decides and moved[0].side is None
        assert moved[0].start == pytest.approx(next(p0 for p0 in base.room if p0.id == "p_high").start + fx.get("presume_step") * tilt, abs=1e-12)
    crowd = {**ROWS["conversation"], "floor": "open"}                                   # the man addressed is a party who decides, and so does the floor
    flat, tilted = (_build(w, row=crowd, arranger="p_king", rig=r)[0] for r in (0.0, 1.0))
    assert [p.id for p, p0 in zip(tilted.room, flat.room) if p != p0] == ["p_other"]       # a party who decides is not presumed toward the arranger
    assert next(p for p in tilted.room if p.id == "p_mid").decides
    # controls: nothing to tilt
    def tilts(arranger, rite_row):
        card = _build(w, row=rite_row, arranger=arranger, rig=1.0)[1]
        return card.tilt, card.arranged_by, card.tilted_against
    assert tilts("p_low", row) == (0.0, None, None)                                    # equals: a party of no more power than the other
    assert tilts("p_king", ROWS["conversation"]) == (0.0, None, None)                  # only a party decides: nobody to tilt
    w.persons["p_king"].stance = []
    assert tilts("p_king", row) == (0.0, None, None)                                   # a third party tied to neither side


class _Own(list):
    """A ledger that raises when read by anyone but its owner (`gate["reader"]`: whose `Present` the builder is building)."""

    def __init__(self, owner, claims, gate):
        super().__init__(claims)
        self.owner, self.gate = owner, gate

    def _read(self):
        self.gate["reads"] += 1
        if self.gate["reader"] != self.owner:
            raise AssertionError(f"{self.owner}'s ledger was read while building {self.gate['reader']!r}")

    def __iter__(self):
        self._read()
        return super().__iter__()

    def __len__(self):
        self._read()
        return super().__len__()

    def __getitem__(self, i):
        self._read()
        return super().__getitem__(i)

    def __contains__(self, x):
        self._read()
        return super().__contains__(x)


def test_the_builder_reads_no_ledger_but_each_persons_own(monkeypatch):
    """Every ledger raises when read for anyone but its owner: the builder returns, each person's `believes` and items are his own
    claim's, and the record it returns holds no carrier (F8; a record is typed values)."""
    w = _world()
    gate = {"reader": None, "reads": 0}
    held = {"p_low": True, "p_mid": False, "p_high": True, "p_other": False}
    for pid, value in held.items():
        w.persons[pid].ledger = _Own(pid, [Claim(f"c_{pid}", pid, "m1", "held_by:q", value, 0, "firsthand", 80 + len(pid), "own")], gate)
    real = S._present

    def building(w_, p, *a, **k):
        prev, gate["reader"] = gate["reader"], p.id
        try:
            return real(w_, p, *a, **k)
        finally:
            gate["reader"] = prev
    monkeypatch.setattr(S, "_present", building)
    inp, card = _build(w, row=ROWS["legal_trial"])
    assert {p.id for p in inp.room} == set(held) and gate["reads"] >= len(held)
    for p in inp.room:
        assert (p.believes > 0) == held[p.id]                                          # his own claim's side
        assert {it.id for it in p.items if it.kind != "title"} <= {f"c_{p.id}", f"word:{p.id}:m1"}
    _carriers(inp)
    _carriers(card)
    # the control: a builder that reads a neighbour's ledger for a person's value is caught by the same ledgers
    def peeking(w_, p, *a, **k):
        other = next(q for q in held if q != p.id)
        gate["reader"] = p.id
        list(w_.persons[other].ledger)
        return real(w_, p, *a, **k)
    monkeypatch.setattr(S, "_present", peeking)
    with pytest.raises(AssertionError, match="ledger was read while building"):
        _build(w, row=ROWS["legal_trial"])


def test_the_builder_reads_a_claim_at_the_worlds_tick_and_only_a_truth_valued_one():
    """A claim of full sureness deposited at tick 0 is read at the world's tick: the man's `believes` and the weight of the false word he may offer
    fall as the seasons pass (the stored `Person` has no tick of his own). A witnessed sitting about the matter's person (a `sitting:*` claim, a
    number, the newest he holds) does not blank what he believes. CONTROL: the same claim read at tick 0 is at its deposited sureness."""
    from ..data.rosters import SITTING_SOURCE
    w = _world()
    full = w.fixtures.get("confidence_default")
    w.persons["p_low"].ledger = [Claim("c_low", "p_low", "m1", "held_by:q", False, 0, "firsthand", full, "own")]
    row = {p.id: p for p in _build(w, row=ROWS["legal_trial"])[0].room}["p_low"]
    word = {it.id: it.weight for it in row.items}["word:p_low:m1"]
    assert row.believes == -1.0 and word == 1.0
    w.tick = 3
    later = {p.id: p for p in _build(w, row=ROWS["legal_trial"])[0].room}["p_low"]
    assert -1.0 < later.believes < 0.0 and {it.id: it.weight for it in later.items}["word:p_low:m1"] < word
    w.persons["p_low"].ledger.append(Claim("c_sit", "p_low", "m1", "sitting:rattled", 400, 3, SITTING_SOURCE, full, "own"))
    assert {p.id: p for p in _build(w, row=ROWS["legal_trial"])[0].room}["p_low"].believes == later.believes
    w.persons["p_low"].ledger.append(Claim("c_bond", "p_low", "m1", person_q.BOND_STEM + "rivalry", True, 3, "firsthand", full, "own"))   # a relationship, newest and bool
    assert {p.id: p for p in _build(w, row=ROWS["legal_trial"])[0].room}["p_low"].believes == later.believes


def test_a_passing_word_nobody_watches_runs_abridged():
    """`form="auto"`: a word of effort 0 that nobody watches (a closed floor, or no one present) is the one-speech form; effort, or a
    floor that watches, makes it the full rite; an explicit form is kept."""
    w = _world()
    row = ROWS["conversation"]
    assert row["floor"] == "closed"
    quiet = _build(w, row=row, effort=0)[0]
    assert quiet.rite.close == "exchange" and quiet.rite.turns == 1 and dict(quiet.rite.moves)["against"] == ()
    assert _build(w, row=A.abridged(row), effort=0)[0].rite.close == "exchange"
    full = _build(w, row=row, effort=1)[0]
    assert full.rite.close == "hearers" and full.rite.turns == 2 and next(p for p in full.room if p.id == "p_mid").side == "against"
    watched = _build(w, row={**row, "floor": "open"}, effort=0)[0]               # p_other is at the hearth
    assert watched.rite.close == "hearers" and "p_other" in _deciders(watched)
    assert _build(w, row=row, effort=0, form="full")[0].rite.close == "hearers"
    assert _build(w, row=row, effort=3, form="abridged")[0].rite.close == "exchange"


def test_the_card_promises_what_the_sitting_does():
    """Over 200 keyed sittings of a church inquisition with items held, nobody makes a move the card bars, shows an item of a
    kind it does not admit, speaks more turns than it gives, and the verdicts are its adjudicators' and no others. B24.10: at the control
    (`sitting_exchanges` 0, shipped) a bench's sitting has no turns and nobody speaks, so the sitting that speaks is the one at `sitting_exchanges` 1."""
    w = _world(sitting_exchanges=1)
    _seat(w, "off_dic", "p_other", CHURCH, post="Dicastery")
    w.records["rec_writ"] = Record("rec_writ", "Hh", "text")
    w.add_tenure(Tenure("h_rec", "p_low", "rec_writ", "hold", since=0))
    w.add_tenure(Tenure("h_title", "p_low", "off_duke", "hold", since=0))      # a `title`: held, and not a kind this rite admits
    w.persons["p_mid"].ledger = [Claim("c_mid", "p_mid", "m1", "held_by:q", False, 0, "firsthand", 90, "own")]
    inp, card = _build(w, row=ROWS["inquisition_hearing"], effort=0, form="full")
    assert card.barred and ("for", "concede") in card.barred and ("against", "press") in card.barred
    assert "title" not in card.admits and not any(it.kind == "title" for p in inp.room for it in p.items)     # held, never offered here
    kind = {it.id: it.kind for p in inp.room for it in p.items}
    shown = beats = 0
    for n in range(200):
        out = PROCEED(inp, _key("host-card", n))
        spoken = {}
        for b in out.beats:
            beats += 1
            assert (b.side, b.move) not in card.barred
            if b.item is not None:
                shown += 1
                assert kind[b.item] in card.admits
            spoken[b.mover] = spoken.get(b.mover, 0) + 1
        assert all(c <= card.turns for c in spoken.values())
        assert {i for i, _ in out.verdicts} <= set(card.decided_by) == {"p_other"} and out.verdicts
    assert shown >= 1 and beats >= 200


def test_the_dice_weights_come_from_the_rows(monkeypatch):
    """The built `grounds`' `reason` is the roster's, `rite.reason_lean` the row's plus the regime's, an era's weight is the context
    table's, and the card shows Reason's share of the dice from them; an edit planted in a copy of each moves the built value."""
    w = _world()
    row = ROWS["legal_trial"]
    inp, card = _build(w, row=row)
    assert [(g, r) for g, r, _ in inp.grounds] == [(g, GROUNDS[g]["reason"]) for g in GROUNDS]
    crown = A.CONTEXT["regimes"]["crown"]
    assert inp.rite.reason_lean == row["reason_lean"] + crown["reason_lean"]
    assert dict(inp.dials["moves"]) == {m: (r["effect"], r["draw"]) for m, r in PROCEEDING_MOVES.items()}
    assert dict(inp.dials["reads"]) == {g: r["reads"] for g, r in GROUNDS.items()}
    grounds, ctx = copy.deepcopy(GROUNDS), copy.deepcopy(A.CONTEXT)
    grounds["evidence"]["reason"] = 0.3
    ctx["regimes"]["crown"]["reason_lean"] = 0.1
    ctx["eras"]["plain"]["evidence"] = 1.4
    monkeypatch.setattr(S, "GROUNDS", grounds)
    monkeypatch.setattr(S, "CONTEXT", ctx)
    moved, moved_card = _build(w, row=row)
    assert moved.grounds[0] == ("evidence", 0.3, 1.4) and moved.grounds[1:] == inp.grounds[1:]
    assert moved.rite.reason_lean == row["reason_lean"] + 0.1
    assert dict(moved_card.reason_weight)["evidence"] == round(10 * (0.3 + moved.rite.reason_lean)) / 10 != dict(card.reason_weight)["evidence"]


# ---------------------------------------------------------------------------------------------------------------------------------
# B24p.14 -- the provider path and the believed odds: `sigma.resolve(proceeds=...)`, `act_band`, `believed_proceeding_odds`.
# ---------------------------------------------------------------------------------------------------------------------------------
def _m(margin, ob=1.0):
    return Margin(net=ob + margin, ob=ob, terms=(("difficulty", ob),))


def _outcome(verdicts, ended="budget", by=None, beats=()):
    return Outcome(tuple(beats), Sitting(), ended, by, tuple(verdicts))


def _rite(close, quorum=None):
    return SimpleNamespace(close=close, quorum=quorum, bears="for")


def _said(mover, side):
    return SimpleNamespace(mover=mover, side=side)


def _band(out, rite, weights=None):
    return degree_of(S.act_band(out, rite, weights))


def _resolve(w, row, *, verb="tell", subject="p_mid", form="auto", effort=0):
    return S.resolve(w, ["p_low"], [], None, rng=_key("b14-resolve"), verb=verb, subject=subject, effort=effort,
                     proceeds=(row, form, "argue", None))


def _plant_entry(monkeypatch, entry):
    real = composition.require
    entry.__module__ = real(S.PROCEEDING_ROLE).__module__             # the host reads the module's closed forms (the card) through the same row
    monkeypatch.setattr(composition, "require", lambda role: entry if role == S.PROCEEDING_ROLE else real(role))


def test_a_proceeding_return_that_is_not_an_outcome_raises(monkeypatch):
    """A winner string where an `Outcome` belongs, and an `Outcome` whose verdict is a band or a number and not a `Margin`, are each refused
    naming the entry; the real entry's return is accepted (the control: the same call)."""
    w, row = _world(), A.abridged(ROWS["conversation"])
    assert _resolve(w, row)["status"] == "RESOLVED"
    for ret in ("for", _outcome([("p_mid", "Success")]), _outcome([("p_mid", 2.0)])):
        _plant_entry(monkeypatch, lambda inp, rng, ret=ret: ret)
        with pytest.raises(Unspecified, match="social_contest.proceeding"):
            _resolve(w, row)


def test_the_acts_band_by_close():
    """The act's record by the close (V2 p2 §D) and by who yields (§C.5), each graded on the one ladder: `exchange` and `bench` the one
    verdict; `hearers` the weight-mean (a head each would read otherwise); `declared` the quorum-th best; a yield decides the band
    whatever the draw would have carried (the control: the same verdicts, nobody yielding); under `consent`, an accept, a withdrawal, neither."""
    assert _band(_outcome([("p_mid", _m(3.2))]), _rite("exchange")) == "Overwhelming"
    assert _band(_outcome([("p_high", _m(1.4))]), _rite("bench")) == "Success"
    hearers = _outcome([("p_a", _m(2.0)), ("p_b", _m(-1.0))])
    assert _band(hearers, _rite("hearers"), {"p_a": 3, "p_b": 1}) == "Success"                   # (3 x 2.0 - 1.0) / 4 = 1.25
    assert _band(hearers, _rite("hearers"), {"p_a": 1, "p_b": 1}) == "Partial"                   # control: a head each is 0.5
    declared = _outcome([("p_a", _m(3.5)), ("p_b", _m(1.2)), ("p_c", _m(-2.0))])
    assert [_band(declared, _rite("declared", q)) for q in (1, 2, 3)] == ["Overwhelming", "Success", "Failure"]
    # a yield: the bearer drops the matter, though the close would have carried it
    verdict = [("p_mid", _m(2.0))]
    dropped = _outcome(verdict, "yielded", "p_low", [_said("p_low", "for")])
    assert _band(_outcome(verdict), _rite("hearers"), {"p_mid": 1}) == "Success"
    assert _band(dropped, _rite("hearers"), {"p_mid": 1}) == "Failure"
    # a party whose verdict alone is the close gives way: Success for the bearer, though his own draw ran against him
    against = [("p_mid", _m(-2.0))]
    gave = _outcome(against, "yielded", "p_mid", [_said("p_mid", "against")])
    assert _band(gave, _rite("hearers"), {"p_mid": 1}) == "Success"
    assert _band(_outcome(against), _rite("hearers"), {"p_mid": 1}) == "Failure"
    shared = _outcome([*against, ("p_z", _m(-2.0))], "yielded", "p_mid", [_said("p_mid", "against")])
    assert _band(shared, _rite("hearers"), {"p_mid": 1, "p_z": 1}) == "Failure"                  # one seat, one vote: his yield decides nothing
    # consent: an accept, a withdrawal, neither
    consent = _rite("consent")
    assert _band(_outcome([], "yielded", "p_mid", [_said("p_mid", "against")]), consent) == "Success"
    assert _band(_outcome([], "yielded", "p_low", [_said("p_low", "for")]), consent) == "Failure"
    impasse = S.act_band(_outcome([], "rested"), consent)
    assert impasse["status"] == "IMPASSE" and "net" not in impasse
    with pytest.raises(Unspecified):
        degree_of(impasse)                                                                       # no band: refused loudly, never guessed


def test_declared_reads_the_quorum_th_best_seat_and_sets_no_veto():
    """Three church seats drawn for real: the act's margin is the second best of the seats' own (a majority carries); the presiding seat's
    margin or the worst seat's, made as bad as it can be, moves nothing (nobody holds a veto); the second best seat's moves it (control)."""
    w = _world()
    for oid, who in (("off_c1", "p_other"), ("off_c2", "p_mid"), ("off_c3", "p_king")):
        _seat(w, oid, who, CHURCH, post="Dicastery")
    row = ROWS["excommunication_deliberation"]
    assert (row["close"], row["quorum"]) == ("declared", 2)
    inp, card = _build(w, ("p_low",), row=row, subject="p_high", effort=1)
    assert len(card.decided_by) == 3
    out = PROCEED(inp, _key("b14-declared"))
    margin = lambda o: S.act_band(o, inp.rite)["settled_margin"]
    ranked = sorted((m.net - m.ob for _, m in out.verdicts), reverse=True)
    assert len(ranked) == 3 and ranked[0] > ranked[1] > ranked[2] and margin(out) == ranked[1]
    bend = lambda who: replace(out, verdicts=tuple((i, _m(-100.0) if i == who else m) for i, m in out.verdicts))
    by_margin = sorted(out.verdicts, key=lambda v: v[1].net - v[1].ob)
    assert margin(bend(by_margin[0][0])) == ranked[1]                            # the worst seat, bent, moves nothing
    assert margin(bend(by_margin[1][0])) == ranked[2]                            # the quorum-th seat, bent, does: the control


def test_a_decided_band_is_graded_on_its_settled_margin(monkeypatch):
    """A yield's band rides as `settled_margin` at its edge and `degree_of` grades it first: a result whose `net`/`ob` pair would read the
    other way reads the band, and without the key the same pair reads its own (the control). Through `resolve`, the bearer's yield returns
    the band with the proceeding and the card."""
    assert degree_of(dict(net=5.0, ob=1.0, settled_margin=-0.001)) == "Failure" and degree_of(dict(net=5.0, ob=1.0)) == "Overwhelming"
    dropped = _outcome([("p_mid", _m(2.0))], "yielded", "p_low", [_said("p_low", "for")])
    got = S.act_band(dropped, _rite("hearers"), {"p_mid": 1})
    assert got["settled_margin"] == -0.001 and degree_of(got) == "Failure"
    _plant_entry(monkeypatch, lambda inp, rng: dropped)
    res = _resolve(_world(), A.abridged(ROWS["conversation"]))
    assert res["status"] == "RESOLVED" and degree_of(res) == "Failure" and isinstance(res["card"], Card) and res["proceeding"] is dropped


def test_s274_refuses_an_exchange_pair_and_never_a_close():
    """A speech whose obstacle is past `obstacle_refusal_multiple` times its pool is refused S27.4; a close is an adjudicator's draw and is
    never refused, at the same setting."""
    w = _world(obstacle_refusal_multiple=0.0)
    refused = _resolve(w, A.abridged(ROWS["conversation"]))
    assert (refused["status"], refused["why"]) == ("REFUSED", "S27.4") and refused["ob"] > 0 and "settled_margin" not in refused
    assert _resolve(w, ROWS["legal_trial"], form="full", verb="argue", effort=1)["status"] == "RESOLVED"
    assert _resolve(_world(), A.abridged(ROWS["conversation"]))["status"] == "RESOLVED"          # control: the shipped multiple


def test_believed_odds_use_his_own_values_and_an_ordinary_man_for_the_rest(monkeypatch):
    """The chooser's odds at a rally are read on a room where he is himself and every other person is an ordinary man (what he holds a claim
    on drawn toward the middle by what his accuracy does not reach, nothing of another's interior): a listener's true interior moves the
    true odds and the believed ones not at all."""
    w, row = _world(start_step=2.0), ROWS["rally"]
    believe = lambda: S.believed_proceeding_odds(w, w.persons["p_low"], ["p_low"], verb="argue", subject=None, effort=1,
                                                 proceeds=(row, "full", "argue", None))
    true_odds = lambda: S._proceeding_module().card_odds(_build(w, ("p_low",), row=row, subject=None, topic=None, form="full")[0])
    base, before = believe(), true_odds()
    assert 0.0 < base < 1.0
    acuity = "attr.mind.acuity"
    w.persons["p_low"].ledger = [Claim("c_said", "p_low", "p_mid", person_q.CAPABILITY_CLAIM + acuity, 9.0, 0, "told", 90, "own")]
    seen, real = [], S.proceeding_input
    monkeypatch.setattr(S, "proceeding_input", lambda w_, claimants, **kw: (seen.append(kw["seen"]) if "seen" in kw else None, real(w_, claimants, **kw))[1])
    believed = believe()
    mid, who = S.attribute_midpoint(), seen[-1].get
    assert who("p_low") is w.persons["p_low"]                                                    # himself, true
    assert who("p_other").attributes == {} and who("p_other").stance == [] and who("p_other").ledger == []   # an ordinary man for the rest
    assert mid < who("p_mid").attributes[acuity] < 9.0                                            # a claim, drawn toward the middle
    w.persons["p_mid"].stance, w.persons["p_mid"].pursuits = [("p_low", 9, 9)], {"grain": 0.9}  # a listener's true interior moves ...
    w.persons["p_mid"].attributes = {acuity: 9.0}
    assert true_odds() != before and believe() == believed                                       # ... the true odds and not the believed


# B24p.16 -- THE VERB ROWS SAY HOW THEY PROCEED (RD §D.1 to §D.4; V2 p2 §M): `VerbRow.proceeds`, `data/verbs.py::_check_proceeds`,
# `world_q.proceeding_row`. Nothing dispatches on the cell until B24p.19; the routing is what these read.
FIVE = ("argue", "tell", "lie", "speak", "interrogate", "determine")      # B24.08 added `determine`: the six


def _act(verb, **payload):
    return Act(id=f"a_{verb}", actor="p_low", verb=verb, payload=payload)


def test_five_rows_proceed_and_name_a_loadable_row():
    """Each of the five verbs carries a `proceeds` cell whose every entry names an arrangement the tree loads (or the docket's own row), a
    form, and a drawing move; no other verb is routed (`covenant`, `interview` are their own items'). A planted cell that names a
    row nothing loads is refused naming the verb: the check observes the failure it excludes."""
    routed = {v: r for v, r in VERB_TABLE.items() if r.proceeds}
    assert set(routed) == set(FIVE), sorted(routed)
    checked = 0
    for verb, row in routed.items():
        for when, rid, form, move, item in row.proceeds:
            assert rid in ROWS or rid == "docket", (verb, rid)
            assert form in ("full", "abridged", "auto") and PROCEEDING_MOVES[move]["draw"] and item in ("any", "false"), (verb, form, move, item)
            checked += 1
        assert row.proceeds[-1][0] == (), verb                                           # a fallback closes every list
    assert checked >= len(FIVE), checked
    _check_proceeds(VERB_TABLE)                                                           # control: the shipped table passes
    entry = (("hearer", "cohort"),), "no_such_row", "full", "argue", "any"
    with pytest.raises(Unspecified, match="argue"):
        _check_proceeds({**VERB_TABLE, "argue": replace(VERB_TABLE["argue"], proceeds=(entry, *VERB_TABLE["argue"].proceeds))})


def test_argue_to_a_cohort_proceeds_as_a_rally():
    """An `argue` addressed to a cohort is a rally, in the full form; to one man it is a conversation, in the full form."""
    w = _world()
    assert world_q.proceeding_row(w, _act("argue", to="p_mid", subject="p_mid")) == (ROWS["conversation"], "full", "argue", "any")
    w.persons["p_mid"].weight = 30
    assert w.persons["p_mid"].is_cohort
    assert world_q.proceeding_row(w, _act("argue", to="p_mid", subject="p_mid")) == (ROWS["rally"], "full", "argue", "any")
    assert world_q.proceeding_row(w, _act("interrogate", to="p_mid", subject="p_mid"))[:2] == (ROWS["interrogation"], "full")   # no cohort clause


def test_speak_proceeds_abridged_under_the_dockets_row():
    """A `speak` on a docketed matter proceeds abridged, under the row the docket hears the matter under (`abridged` of it); two matters on
    two rows read two rows; a matter on no docket has no row to proceed under and is refused naming the verb; a docketed matter whose item names no arrangement (a computed case) is heard by the seat, the `audience` row."""
    w = _world()
    w.docket.append({"date": None, "matter": "p_mid", "arrangement": "audience", "petition": None})
    w.docket.append({"date": None, "matter": "p_other", "arrangement": "arbitration", "petition": None})
    read = lambda who: world_q.proceeding_row(w, _act("speak", subject=who))
    assert read("p_mid") == (A.abridged(ROWS["audience"]), "abridged", "argue", "any")
    assert read("p_other") == (A.abridged(ROWS["arbitration"]), "abridged", "argue", "any")
    assert read("p_mid")[0]["close"] == "exchange" and ROWS["audience"]["close"] == "bench"      # the row's venue kept, its close the speech's
    with pytest.raises(Unspecified, match="speak"):
        world_q.proceeding_row(w, _act("speak", subject="p_high"))                      # on no docket: refused naming the verb
    w.docket.append({"date": None, "matter": "p_high", "arrangement": None, "petition": None})
    assert read("p_high") == (A.abridged(ROWS["audience"]), "abridged", "argue", "any")   # a computed case names no row: the seat hears it


def test_a_lie_is_an_argue_on_his_own_false_word():
    """`lie` proceeds as `tell` does (a conversation, abridged) with the move `argue` and the item `false`, so the speaker is offered his own
    false items only; `tell` and `argue` offer any."""
    w = _world()
    lie, tell = (world_q.proceeding_row(w, _act(v, to="p_mid", subject="p_mid")) for v in ("lie", "tell"))
    assert lie == (A.abridged(ROWS["conversation"]), "abridged", "argue", "false")
    assert tell == (A.abridged(ROWS["conversation"]), "abridged", "argue", "any")


# B24p.19 -- THE INFLUENCE VERBS CALL THE PROCEEDING (RD §D.1; V2 p2 §M): `seam/contest.py::contest` resolves `proceeding_row` for a verb row that
# carries `proceeds:` and the provider takes `social_contest.proceeding`; every other act keeps `social_contest.roll`. A spy stands on each entry.
class _Spy:
    """Records each call of the two entries the social provider can reach: the proceeding (through its composition row) and the single roll."""

    def __init__(self, monkeypatch):
        from ..manifest import MODULE_ENTRIES
        self.sittings, self.rolls = [], []
        real, roll = composition.require, MODULE_ENTRIES["social_contest.roll"]
        proceed = real(S.PROCEEDING_ROLE)

        def entry(inp, rng):
            out = proceed(inp, rng)
            self.sittings.append((inp, out))
            return out
        entry.__module__ = proceed.__module__
        monkeypatch.setattr(composition, "require", lambda role: entry if role == S.PROCEEDING_ROLE else real(role))

        def rolled(inp, rng):
            self.rolls.append(inp)
            return roll.fn(inp, rng)
        monkeypatch.setitem(MODULE_ENTRIES, "social_contest.roll", replace(roll, fn=rolled))


def _seamed(w, verb, prize, *, to="p_mid", topic=None, effort=0, **payload):
    """`seam/contest.py::contest` as `loop/resolve.py::_contest` calls it for the act."""
    from ..seam import contest
    act = Act(id=f"a19_{verb}", actor="p_low", verb=verb, payload={"to": to, "subject": topic or to, **payload})
    return contest(w, "Hh", prize, ["p_low", to], 0, 2, [act.id], verb=verb, subject=to, topic=topic, rng=_key(f"b19-{verb}"), effort=effort, act=act)


def test_a_tell_resolves_through_the_proceeding_entry_as_one_exchange(monkeypatch):
    """A `tell` folded by the driver reaches `social_contest.proceeding` and never `social_contest.roll`: one sitting, one beat, the man addressed
    its only adjudicator, the matter the act's subject; the Event's band is the one ladder's reading of the sitting's own margin. CONTROL: the
    spy sees a roll for an act on the single roll (`test_an_arrest_still_resolves_on_the_single_roll`). The pool reader refuses the verb."""
    from ..data.matrix import WriteClass
    from ..gaps import Forbidden
    from ..loop.driver import SeasonDriver, mint_token
    from ..seam.wrappers import pool
    w = _world()
    d = SeasonDriver(w)
    w.persons["p_low"].ledger.append(Claim("c_held", "p_low", "Hh", "stores:grain", 8, 0, "firsthand", 80, "own"))
    spy = _Spy(monkeypatch)
    said = person_q.said_of(w.persons["p_low"].ledger, "Hh", w.fixtures)
    act = Act(id="a_tell19", actor="p_low", verb="tell", payload={"subject": "Hh", "to": "p_mid", "said": said})
    events = d.resolve(mint_token(w, WriteClass.ACTS), [act], contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert len(spy.sittings) == 1 and not spy.rolls, (len(spy.sittings), len(spy.rolls))
    inp, out = spy.sittings[0]
    assert len(out.beats) == 1 and [v[0] for v in out.verdicts] == ["p_mid"] and inp.matter == "Hh", (len(out.beats), out.verdicts, inp.matter)
    assert inp.rite.close == "exchange" and _deciders(inp) == ("p_mid",)
    assert events and {e.degree for e in events} == {degree_of(S.act_band(out, inp.rite))}, [(e.kind, e.degree) for e in events]
    with pytest.raises(Forbidden, match="tell"):
        pool.faculty(w, w.persons["p_low"], "tell")


def test_an_argue_resolves_as_exchanges_and_the_hearers_draw():
    """An `argue` to one man runs the full conversation (more than one exchange, the one addressed drawing the close); to a cohort it is a rally
    in which the hearers each draw their own verdict, so the act's band is read off the weight-mean of those who hear (`close: hearers`)."""
    from ..loop.driver import SeasonDriver
    w = _world()
    SeasonDriver(w)                                                  # constructed first: the registrar fills the provider and entry tables
    one = _seamed(w, "argue", "a proposition", topic="m1", effort=2)
    assert one["status"] == "RESOLVED" and one["proceeding"] is not None and len(one["proceeding"].beats) > 1, one.get("status")
    assert [v[0] for v in one["proceeding"].verdicts] == ["p_mid"]
    w = _world()
    SeasonDriver(w)
    w.persons["p_mid"].weight = 30
    w.persons["p_other"].weight = 3
    many = _seamed(w, "argue", "a proposition", topic="m1", effort=2)
    heard = [v[0] for v in many["proceeding"].verdicts]
    assert many["status"] == "RESOLVED" and "p_mid" in heard and len(heard) > 1, heard


def test_odds_of_has_no_social_roll_figure_for_a_verb_that_proceeds():
    """`odds_of` shows the social roll's odds; a verb that proceeds is dealt by the sitting, so there are none, shown or believed, where
    the single roll would have raised on a skill no such verb names. CONTROL: `arrest` still reads."""
    w = _world()
    argue = Act(id="a_argue", actor="p_low", verb="argue", payload={"to": "p_mid", "subject": "m1"})
    assert S.odds_of(w, argue) is None and S.odds_of(w, argue, believer=w.persons["p_low"]) is None
    assert S.odds_of(w, Act(id="a_arrest", actor="p_low", verb="arrest", payload={"to": "p_other"})) is not None


def test_an_arrest_still_resolves_on_the_single_roll(monkeypatch):
    """CONTROL: `arrest` carries no `proceeds:` cell, so the same call takes today's path: the spy sees `social_contest.roll` and no sitting, and
    the result carries no proceeding. The five verbs' prize rows name the same provider, so what separates them is the row's cell alone."""
    from ..loop.driver import SeasonDriver
    w = _world()
    SeasonDriver(w)
    spy = _Spy(monkeypatch)
    out = _seamed(w, "arrest", "a standing", to="p_other")
    assert out["status"] == "RESOLVED" and len(spy.rolls) == 1 and not spy.sittings and "proceeding" not in out, out



# B24p.24 -- THE ARRANGER AND HIS RIG REACH THE BUILDER (V2 p2 §E, §H; p4 §F 19, §K C3): `_docket_item`'s two keys, `_eff_open_case`, `_eff_convene`,
# `decision/options.py::rig_offer`, `seam/wrappers/sigma.py::arranged_by`.
def _opened(w, d, key="oc", **payload):
    """`open_case` on the party by the Duke, folded: `(its Event kinds, the matter's docket items)`."""
    from .test_u7_remit import _fold, _kinds, _open
    out = _fold(w, d, _open(key, **payload))
    return _kinds(out), world_q.docketed(w, "p_mid")


def test_an_opened_case_carries_its_arranger_and_rig():
    """The docket item says who arranged the sitting and how hard: the opener, at the rig his act carried (none where it carried none); a level
    outside `rig_levels` is declined and nothing is docketed; and a convening's rig stands for the sitting where the opener rigged none, the
    opener's own where he did (V2 p2 §H, the convening seat). A convening that rigs nothing writes neither key on its Date."""
    from .test_u7_remit import SEAT, _act, _fold, _kinds, _world as case_world
    from ..data.matrix import WriteClass
    from ..loop.driver import mint_token
    for rig, want in ((0.5, 0.5), (1, 1.0), (None, 0.0)):
        w, d = case_world()
        kinds, (item,) = _opened(w, d, **({} if rig is None else {"rig": rig}))
        assert kinds == ["case.opened"] and (item[world_q.DOCKET_ARRANGER], item[world_q.DOCKET_RIG]) == ("p_high", want), item
    w, d = case_world()
    kinds, items = _opened(w, d, rig=0.3)
    assert kinds == ["case.refused"] and items == [], (kinds, items)                      # a level outside the roster is no rig

    def sitting(w, d, **rig):
        out = _fold(w, d, _act("cv", "convene", subject="S", **rig))
        assert _kinds(out) == ["date.scheduled"], _kinds(out)
        did, = [k for k, v in w.dates.items() if v.get("venue") == "S"]
        w.tick += 1
        d.calendar(mint_token(w, WriteClass.CALENDAR))                                       # the sitting fires and forms its empty slot
        assert [x for x in w.docket if x.get("date") == did and x.get("matter") is None], w.docket
        return did
    w, d = case_world()
    did = sitting(w, d)
    assert "rig" not in w.dates[did] and "arranger" not in w.dates[did]                    # nothing rigged: the Date is what it was
    w, d = case_world()
    did = sitting(w, d, rig=1)
    assert (w.dates[did]["arranger"], w.dates[did]["rig"]) == ("p_high", 1.0)
    item, = _opened(w, d)[1]
    assert (item["date"], item[world_q.DOCKET_ARRANGER], item[world_q.DOCKET_RIG]) == (did, "p_high", 1.0)          # the convener's rig stands
    w, d = case_world()
    sitting(w, d, rig=1)
    item, = _opened(w, d, rig=0.5)[1]
    assert item[world_q.DOCKET_RIG] == 0.5                                                  # the opener's own, where he rigged


_SHIPPED_HEARING = S._hearing


def _gap_world(weak=None, *, hearing=True, monkeypatch=None):
    """The King (a realm seat on no bench) may open a case on `p_mid`, heard by the Duke's bench in the full legal trial; `weak` gives `p_mid` a seat of
    that rung, so his power is the gap's other end. `hearing` plants the full row for the case's hearing: the shipped one is abridged and has nobody
    but a party to decide, so there is nothing to tilt (V2 p4 §L 10)."""
    from ..loop.driver import SeasonDriver
    w = _world()
    SeasonDriver(w)
    _seat(w, "off_chancellor", "p_king", post="Chancellor", rung="R", scope=None)
    if weak:
        _seat(w, "off_weak", "p_mid", post="Clerk", rung=weak, scope=None)
    w.persons["p_king"].ledger.append(Claim("c_knows", "p_king", "p_mid", "exists:Person", 1, 0, "firsthand", 100, "own"))
    monkeypatch.setattr(S, "_hearing", (lambda w_: ("speak", (ROWS["legal_trial"], "full", None, None))) if hearing else _SHIPPED_HEARING)
    return w


def _rigs(w, **fx):
    """The `rig` each `open_case` candidate the King forms on `p_mid` carries (`None` for one that carries none), through `opening_set`."""
    from ..decision import opening_set
    from ..state.carriers import Question, View
    fixtures = w.fixtures
    for name, value in fx.items():
        fixtures = fixtures.sweep(name, value)
    q = Question("q_rig", "need", ("p_mid",), "p_mid", classes=(("p_mid", "Person"),))
    king = w.persons["p_king"]
    v = View(king.id, [], fixtures.get("view_k"), q, odds=S.believed_odds_query(w, king))
    return [c.operands.get("rig") for c in opening_set(king, v, q, fixtures) if c.verb == "open_case"]


def test_rig_is_offered_only_over_a_power_gap(monkeypatch):
    """A man of more power than the other party, before a bench that someone else sits, is offered a rig by the reckoning (the half, at the shipped
    price); between equals, and where only a party decides, none; and a View that cannot ask offers none. CONTROL: the same King offers a rig at the
    gap and not at the equal's seat, so what withholds it is the gap and not the verb."""
    w = _gap_world(monkeypatch=monkeypatch)
    assert _rigs(w) == [0.5]                                         # a gap of the realm's seat over nobody: the reckoning's half
    equal = _gap_world("R", monkeypatch=monkeypatch)                  # the other party sits as high: no tilt, no price, no rig
    assert _rigs(equal) == [None]
    only_a_party = _gap_world(hearing=False, monkeypatch=monkeypatch)   # the shipped hearing: abridged, nobody but a party decides
    assert _rigs(only_a_party) == [None]
    from ..decision import opening_set
    from ..state.carriers import Question, View
    q = Question("q_rig", "need", ("p_mid",), "p_mid", classes=(("p_mid", "Person"),))
    blind = View("p_king", [], w.fixtures.get("view_k"), q, odds=lambda act, bands: None)        # a query that answers odds and not arrangements
    assert [c.operands.get("rig") for c in opening_set(w.persons["p_king"], blind, q, w.fixtures) if c.verb == "open_case"] == [None]


def test_each_rig_level_is_best_somewhere(monkeypatch):
    """V2 p4 §K C3, on the host's own readings: over the stakes a man may have in a matter and the power gaps he may hold over the other party, the
    reckoning's best level is none somewhere, the half somewhere and the whole somewhere; the price is `rig_price x tilt^2` and it rises with the rig,
    so no level is the best for being dearer. FALSIFIER: a price that fell as the rig rose would make the whole rig dominate wherever the half did."""
    from ..decision import options as O
    act = Act("x", "p_king", "open_case", payload={"subject": "p_mid"})
    best, rising = set(), 0
    for weak in (None, "S", "D"):
        w = _gap_world(weak, monkeypatch=monkeypatch)
        ask = S.believed_odds_query(w, w.persons["p_king"]).arranged
        readings = {r: ask(act, r) for r in (0, 0.5, 1)}
        price = w.fixtures.get("fold_rig_price")
        costs = [-O.rig_worth(0.0, 0.0, readings[r][1], price) for r in (0, 0.5, 1)]          # what the reckoning charges, the stake and odds nothing
        assert costs[0] == 0.0 < costs[1] < costs[2], costs                                  # monotone in the rig
        rising += 1
        best |= {O.best_rig(stake, readings, price) for stake in (0.25, 0.5, 1, 2, 4)}
    assert rising == 3 and best == {0, 0.5, 1}, best


def test_a_docketed_rig_reaches_the_card(monkeypatch):
    """A docketed item's arranger and rig are what the act that hears it hands the builder (`arranged_by`, through `_contest` and `contest()`), and the
    card the builder then derives from them names the tilt and the side it works against; an item with no rig names no arranger to the builder."""
    from ..data.matrix import WriteClass
    from ..loop.driver import SeasonDriver, mint_token
    seen, real = [], S.proceeding_input
    monkeypatch.setattr(S, "proceeding_input", lambda w_, claimants, **kw: (seen.append((kw.get("arranger"), kw.get("rig"))), real(w_, claimants, **kw))[1])
    for rig, want in ((1.0, ("p_king", 1.0)), (0.0, (None, 0.0))):
        w = _world()
        d = SeasonDriver(w)
        w.docket.append({"date": None, "matter": "p_mid", "arrangement": None, "petition": None, "arranger": "p_king", "rig": rig})
        del seen[:]
        d.resolve(mint_token(w, WriteClass.ACTS), [Act(id="a_speak24", actor="p_low", verb="speak", payload={"subject": "p_mid"})],
                  contest_max_depth=w.fixtures.get("contest_max_depth"))
        assert seen and set(seen) == {want}, (rig, seen)                                     # the pair the item holds, and nothing where it holds no rig
    w = _world()
    _seat(w, "off_chancellor", "p_king", post="Chancellor", rung="R", scope=None)
    w.persons["p_king"].stance = [("p_low", 5, 5)]                                           # he favours the bearer: the side his tie takes
    w.docket.append({"date": None, "matter": "p_mid", "arrangement": "legal_trial", "petition": None, "arranger": "p_king", "rig": 1.0})
    arranger, rig = S.arranged_by(w, _act("speak", subject="p_mid"), "p_mid")
    card = _build(w, row=ROWS["legal_trial"], arranger=arranger, rig=rig)[1]
    assert (card.arranged_by, card.tilted_against) == ("p_king", "against") and card.tilt > 0, card


# B24p.20 -- THE SITTING IS WRITTEN (V2 p2 §C.1, §J; p4 §L 20): `loop/resolve.py::_proceeding_ending` writes the Event's `ending`, `world_q.ending_*`
# read it back, `_eff_argue` moves each hearer of a rally for himself. A sitting is run by the entry and folded through the driver's own `_fold`.
def _beat(n, mover, side, mood, *, rattled=None, moved=(), move="argue", relation="raises", issue="m1", item=None, evaded=False, caught=(), broke=False):
    return Beat(n, mover, mover, side, move, relation, issue, "consequence", item, None, None, 0.5, 0.0, evaded, None, 0.0, tuple(caught), rattled, None, 1.0, 1.0,
                0.0, broke, tuple(moved), None, mood, (("difficulty", 1.0),))


def _card(**kw):
    """The cells of a card a sitting writes (`_proceeding_ending`): `close`, who decided, who tilted the forum, how far and against which side."""
    return SimpleNamespace(**{**dict(close="bench", decided_by=("p_mid",), arranged_by=None, tilt=0.0, tilted_against=None), **kw})


def _planted(beats, ended="budget", by=None, read=("p_mid",), tracks=None, who=("p_low", "p_mid"), verdicts=(("p_mid", 3.0),), card=None, ruled=(),
             arrangement="conversation"):
    """A hand-built sitting of `beats` over `who` (every start 0): the outcome, and the result `_resolve_proceeding` would hold it in."""
    run = {p: 0.0 for p in who}
    for b in beats:
        for p, d in b.moved:
            run[p] += d
    state = Sitting(n=len(beats), tracks=tuple((tracks or run).items()), cond=tuple((p, Cond(rattles=sum(b.rattled == p for b in beats))) for p in who), ended=ended)
    out = Outcome(tuple(beats), state, ended, by, tuple((p, _m(m)) for p, m in verdicts), tuple(ruled))
    return dict(status="RESOLVED", proceeding=out, card=card or _card(), arrangement=arrangement, form="full", topic="m1",
                read=read, starts=tuple((p, 0.0) for p in who), net=5.0, ob=1.0, settled_margin=4.0, terms=())


def _folded(w, result, *, verb="argue", to="p_mid", degree="Success", act_id="a20", witness=False):
    """`result` folded as the driver folds an act of `verb` (`_fold`, with the act's own resolution): the Events the act emitted; `witness` runs the
    driver's WITNESS barrier over them, as the loop does (B24p.22)."""
    from ..data.matrix import WriteClass
    from ..loop.driver import SeasonDriver, mint_token
    from ..seam import Resolution
    act = Act(id=act_id, actor="p_low", verb=verb, payload={"to": to, "subject": "m1"})
    d = SeasonDriver(w)
    events = d._fold(w, mint_token(w, WriteClass.ACTS), act, Resolution(degree, result))
    if witness:
        w.log.extend(events)
        for e in events:
            d.act_of[e.id] = act
        d.witness(mint_token(w, WriteClass.INTERIOR), events)
    return events


def _sat(w, row="conversation", form="full", effort=2):
    """One real sitting on the entry, as the provider path runs it: `(input, card, outcome, the result `_resolve_proceeding` would return)`."""
    inp, card = _build(w, row=ROWS[row], effort=effort)
    out = PROCEED(inp, _key("b20-sat"))
    return inp, card, out, dict(status="RESOLVED", proceeding=out, card=card, arrangement=row, form=form, topic=inp.matter, read=(out.verdicts[0][0],),
                                starts=tuple((p.id, p.start) for p in inp.room), net=5.0, ob=1.0, settled_margin=4.0, terms=())


def test_a_proceedings_event_carries_its_beats_sitting_and_verdicts():
    """A full sitting folded as an act leaves, on every Event the act emitted, its head, one tuple per beat (a `Beat`'s fields in order, never `terms`),
    the whole `Sitting` and each verdict's band on the one ladder, in milli-units; `ending_beats`, `ending_sitting` and `ending_verdicts` read back what
    the outcome held and no more. CONTROL: one abridged speech writes the head, one beat and its one verdict. FALSIFIER: a sitting whose tracks are not
    the starts plus the beats' moves is refused at the write, so a stored aggregate cannot drift from the beats."""
    from ..gaps import InstrumentDefect
    w = _world()
    inp, card, out, result = _sat(w)
    events = _folded(w, result)
    assert events and len({e.ending for e in events}) == 1 and events[0].ending, [e.kind for e in events]
    e = events[0]
    assert e.ending[0] == ("proceeding", "conversation", "full", out.ended, out.ended_by)
    beats = world_q.ending_beats(e)
    assert len(out.beats) > 1 and [(b.n, b.mover, b.move, b.margin) for b in beats] == [(b.n, b.mover, b.move, round(b.margin * 1000)) for b in out.beats]
    assert all(len(t) == len(written(Beat)) + 1 for t in e.ending if t[0] == "beat")               # the beat's written cells (`queries/inputs.py::UNWRITTEN`), one tag more
    assert out.beats[0].terms and all(out.beats[0].terms not in t for t in e.ending)
    state = world_q.ending_sitting(e)
    assert (state.n, state.issue, state.ended) == (out.state.n, out.state.issue, out.state.ended)
    assert len(state.tracks) == len(out.state.tracks) and all(abs(a - b) <= 0.001 for (_, a), (_, b) in zip(state.tracks, out.state.tracks))
    assert world_q.ending_verdicts(e) == tuple((who, degree_of(dict(net=m.net, ob=m.ob, settled_margin=m.net - m.ob))) for who, m in out.verdicts)
    # the control: the one-speech form
    w = _world()
    abridged_inp, _ = _build(w, row=A.abridged(ROWS["conversation"]), effort=0)
    one = PROCEED(abridged_inp, _key("b20-one"))
    result = dict(result, proceeding=one, form="abridged", starts=tuple((p.id, p.start) for p in abridged_inp.room), read=(one.verdicts[0][0],))
    ended = _folded(w, result)[0].ending
    assert [t[0] for t in ended] == ["proceeding", "beat", "sitting", "verdict", "card"] and ended[0][2] == "abridged", [t[0] for t in ended]
    # the falsifier
    bad = dict(result, starts=tuple((p, s + 1.0) for p, s in result["starts"]))
    with pytest.raises(InstrumentDefect, match="04 G.1.5"):
        _folded(_world(), bad)


def test_the_record_names_the_rooms_stance_where_it_turns():
    """The record names the room in five bands of the beat's mood, at the beat that turns it (the first, and each whose band differs from the one before)
    and nowhere else; the clamped number is never in it; a yield that decided is said to have decided, and one the close then drew on is not. FALSIFIER: a
    writer that named every beat, or kept the number, or called a drawn close's yield `decided`, fails one of the three reads below."""
    from ..data.rosters import STANCE_BANDS, STANCE_DECIDED
    moods = [0.0, 0.1, 0.5, 0.7, 0.3, -0.9, -0.5, -0.1]
    edges = (-0.6, -0.2, 0.2, 0.6)
    band = lambda m: STANCE_BANDS[sum(m >= e for e in edges)]
    beats = [_beat(i + 1, "p_low", "for", m) for i, m in enumerate(moods)]
    e = _folded(_world(), _planted(beats))[0]
    stances = [b.stance for b in world_q.ending_beats(e)]
    want = [band(m) if i == 0 or band(m) != band(moods[i - 1]) else None for i, m in enumerate(moods)]
    assert stances == want and None in stances and len({s for s in stances if s}) >= 4, stances      # the bands are the five fifths of -1..1
    assert not any(isinstance(v, float) for t in e.ending for v in t), "a real is written in whole milli-units only"
    two = [_beat(1, "p_low", "for", 0.1), _beat(2, "p_low", "for", 0.1)]
    settled = world_q.ending_beats(_folded(_world(), _planted(two, "yielded", "p_low", read=()))[0])
    assert [b.stance for b in settled] == ["hanging", STANCE_DECIDED]                                 # the yield that decided names itself, though the band held
    drawn = world_q.ending_beats(_folded(_world(), _planted(two, "yielded", "p_low", read=("p_mid",)))[0])
    assert [b.stance for b in drawn] == ["hanging", None]                                              # a yield the close was then drawn on is a beat like another


def test_a_written_sitting_resumes_without_replay():
    """`ending_sitting` handed back as `Input.state` continues the sitting: the count of beats, the issue reached and each man's turns are the written
    ones, and the new beats begin after them with no beat replayed. A sitting that `yielded` is refused, as the entry refuses one."""
    w = _world()
    inp, card = _build(w, row=ROWS["conversation"], effort=2)
    first = PROCEED(replace(inp, rite=replace(inp.rite, turns=2)), _key("b20-resume"))
    assert first.ended == "budget" and first.state.n >= 2, first.ended
    result = dict(_planted(first.beats, "budget", read=("p_mid",), tracks=dict(first.state.tracks), who=tuple(p.id for p in inp.room)), proceeding=first,
                  starts=tuple((p.id, p.start) for p in inp.room))
    state = world_q.ending_sitting(_folded(w, result)[0])
    assert (state.n, state.issue) == (first.state.n, first.state.issue)
    assert {i: c.spoken for i, c in state.cond} == {i: c.spoken for i, c in first.state.cond}
    more = PROCEED(replace(inp, rite=replace(inp.rite, turns=4), state=state), _key("b20-resume-2"))
    assert more.beats and more.beats[0].n == state.n + 1 and more.state.n == state.n + len(more.beats), (state.n, [b.n for b in more.beats])
    assert more.state.issue >= state.issue
    with pytest.raises(ValueError, match=r"refused\[resume_yielded\]"):
        replace(inp, state=replace(state, ended="yielded"))


def test_a_rally_moves_each_carried_hearer_and_no_other():
    """An `argue` to a crowd under a `hearers` close moves, for each verdict, THAT hearer's pursuits at his own band: the two carried hearers move
    (the man the act names, `to`, is one the sitting did not carry and does not move); the two not carried do not. CONTROL: the same band under any
    other close moves the one named, at the act's band. FALSIFIER: an effect that moved the named man at the act's band moves p_mid and not p_other."""
    from ..data.rosters import PURSUITS
    from ..loop.effects import EFFECTS
    a, b = sorted(PURSUITS)[:2]
    heard = ("p_mid", "p_other", "p_high", "p_king")

    def stage(close):
        w = _world()
        for who in heard:
            w.persons[who].pursuits = {a: 0.2, b: 0.4}
        w.persons["p_low"].pursuits = {a: 1.0, b: 0.0}
        result = _planted([], read=heard, who=("p_low",) + heard, verdicts=(("p_mid", -1.0), ("p_other", 3.5), ("p_high", 0.4), ("p_king", 1.5)))
        result["card"] = _card(close=close)
        return w, Act(id="a20r", actor="p_low", verb="argue", payload={"to": "p_mid", "subject": "m1"}), result
    w, act, result = stage("hearers")
    change = EFFECTS["argue"](w, act, SimpleNamespace(degree="Success", result=result))
    change.apply()
    moved = {who for who in heard if w.persons[who].pursuits != {a: 0.2, b: 0.4}}
    assert moved == {"p_other", "p_king"} and {s.id for s in change.subjects} == moved, moved                        # Overwhelming and Success carried; Partial and Failure did not
    over, success = (w.persons[who].pursuits for who in ("p_other", "p_king"))
    assert over[a] - 0.2 > 1.5 * (success[a] - 0.2) > 0, (over, success)                                                # each at his own band: the one ladder's steps
    for close, read in (("bench", heard), ("hearers", ())):                  # another close, and a yield that decided the band (no verdict did)
        w, act, result = stage(close)
        EFFECTS["argue"](w, act, SimpleNamespace(degree="Success", result=dict(result, read=read))).apply()
        assert {who for who in heard if w.persons[who].pursuits != {a: 0.2, b: 0.4}} == {"p_mid"}, close


def test_a_rattle_is_counted_into_the_strain_he_carries_next():
    """A press that landed on a man is in his sitting's ending (`ending_rattles`) and the next proceeding builds him carrying it (`rattled_since`, through
    `strain_carried`): less the more scenes since, none for a man it did not land on, none for a chooser's picture of him, and none once the season
    closes. FALSIFIER: the old caller, handing `strain_carried` nothing, builds every man at zero."""
    w = _world()
    beats = [_beat(1, "p_low", "for", 0.0), _beat(2, "p_low", "for", 0.0, rattled="p_mid")]
    events = _folded(w, _planted(beats, who=("p_low", "p_mid", "p_other")), act_id="a20-first")
    w.log.extend(events)
    assert [world_q.ending_rattles(events[0], who) for who in ("p_mid", "p_low", "p_other")] == [1, 0, 0]
    strain = lambda who, **kw: {p.id: p.strain for p in _build(w, row=ROWS["conversation"], **kw)[0].room}[who]
    fresh = strain("p_mid")
    assert fresh == person_q.strain_carried((0,), w.fixtures) > 0 and strain("p_low") == 0.0
    w.log.extend(_folded(w, _planted([_beat(1, "p_low", "for", 0.0)], who=("p_low", "p_mid")), act_id="a20-second"))       # a later scene he sat in
    assert world_q.rattled_since(w, "p_mid") == (1,) and 0.0 < strain("p_mid") < fresh
    assert strain("p_mid", seen=S._Believed(w, w.persons["p_low"], 0.5)) == 0.0                                          # a picture of him carries none
    w.tick += 1
    assert strain("p_mid") == 0.0


def test_every_end_of_a_proceeding_writes_an_ending():
    """A-81: a sitting that ended on its budget, a whole round at rest or a yield leaves a non-empty ending on every Event the act emitted, a refusal after
    the sitting's included (an `argue` at Success that moved nobody is refused, and the sitting is still on the stage)."""
    checked = 0
    for ended, by, read in (("budget", None, ("p_mid",)), ("rested", None, ("p_mid",)), ("yielded", "p_low", ())):
        events = _folded(_world(), _planted([_beat(1, "p_low", "for", 0.2), _beat(2, "p_mid", "against", 0.0)], ended, by, read=read))
        assert events and all(e.ending and e.ending[0][3] == ended for e in events), (ended, [(e.kind, e.ending[:1]) for e in events])
        checked += len(events)
        assert {e.kind for e in events} == {"argument.refused"}
    assert checked >= 3


# B24p.22 -- WHAT THE BEATS SHOW IS DEPOSITED WITH THOSE WHO SAW IT (V2 p2 §J; p4 §K B2, B4, B21, C1, C4): `loop/witness.py::_sitting_claims` reads a sitting's
# `Event.ending` alone and each person in its room holds the claims in his OWN ledger (`rosters.yaml: sitting_claims`). A sitting is hand-built here
# (`_planted`) and folded and witnessed as the loop does it (`_folded(witness=True)`).
def _held(w, who, *kinds):
    """The sitting's claims `who` holds, `(kind, subject, value, confidence)` each, in his ledger's order; `kinds` narrows them."""
    from ..data.rosters import SITTING_PREDICATES
    named = {v: k for k, v in SITTING_PREDICATES.items()}
    return [(named[c.predicate], c.subject, c.value, c.confidence) for c in w.persons[who].ledger if c.predicate in named and (not kinds or named[c.predicate] in kinds)]


def _room(*, decided=("p_mid",), **kw):
    return dict(who=("p_low", "p_mid", "p_other"), card=_card(decided_by=decided), verdicts=tuple((d, 3.0) for d in decided), **{"read": decided, **kw})


def test_a_sitting_deposits_only_in_the_ledgers_of_those_present():
    """A sitting that rattled a man, showed an item and ended in a concession leaves each claim in the own ledger of each person in its room, about
    the speaker and never about the holder himself, and in no ledger of anyone who was not in the room. FALSIFIER: a deposit in `p_high`'s or `p_king`'s
    ledger (the world holds both, in the realm and not in the room), or a man holding a claim of himself. CONTROL: a sitting with no rattle, no item, no
    concession and no rest under a standing point deposits only the bystander's `heard` claim."""
    w = _world()
    beats = [_beat(1, "p_low", "for", 0.0, item="i1"), _beat(2, "p_mid", "against", 0.0, rattled="p_low", move="press", relation="presses"),
             _beat(3, "p_mid", "against", 0.0, move="concede", relation="concedes")]
    _folded(w, _planted(beats, **_room()), witness=True)
    got = {who: {(k, s) for k, s, _, _ in _held(w, who)} for who in w.persons}
    assert got["p_high"] == got["p_king"] == set(), got
    assert got["p_low"] == {("rattled", "p_mid"), ("conceded", "p_mid")}, got["p_low"]
    assert got["p_mid"] == {("shown", "p_low")}, got["p_mid"]
    assert got["p_other"] == {("shown", "p_low"), ("rattled", "p_mid"), ("conceded", "p_mid"), ("heard", "p_low")}, got["p_other"]
    assert [v for k, s, v, _ in _held(w, "p_other", "rattled")] == ["p_low"] and [v for k, s, v, _ in _held(w, "p_low", "rattled")] == ["p_low"]
    control = _world()
    _folded(control, _planted([_beat(1, "p_low", "for", 0.0), _beat(2, "p_mid", "against", 0.0)], **_room()), witness=True)
    assert [(who, [k for k, *_ in _held(control, who)]) for who in control.persons] == [(who, ["heard"] if who == "p_other" else []) for who in control.persons]


def test_hypocrite_only_where_the_reading_turned_the_lie():
    """A speech some hearer's own reading turned (`caught`) leaves a `hypocrite` claim of the speaker with those hearers alone; the same speech where
    nobody's reading turned it leaves none, with the room or the man caught. FALSIFIER: a claim held by `p_other`, who was in the room and read him as
    he spoke; or one in the world where the lie carried."""
    w = _world()
    beats = [_beat(1, "p_low", "for", 0.0, issue="fact", caught=("p_mid",)), _beat(2, "p_low", "for", 0.0, issue="definition")]
    _folded(w, _planted(beats, **_room()), witness=True)
    assert _held(w, "p_mid", "hypocrite") == [("hypocrite", "p_low", "fact", w.fixtures.get("confidence_default"))]
    assert _held(w, "p_other", "hypocrite") == _held(w, "p_low", "hypocrite") == []
    carried = _world()
    _folded(carried, _planted([_beat(1, "p_low", "for", 0.0, issue="fact")], **_room()), witness=True)
    assert [c for who in carried.persons for c in _held(carried, who, "hypocrite")] == []


def test_one_temper_claim_per_man_per_sitting():
    """A man whose temper breaks on three beats of one sitting is one claim with each witness, at the first of them; a second sitting in which he breaks
    again is a second. FALSIFIER: three claims with each witness (one a beat); the broken man holding a claim of himself."""
    w = _world()
    beats = [_beat(1, "p_low", "for", 0.0)] + [_beat(n, "p_mid", "against", 0.0, issue=i, broke=True) for n, i in ((2, "fact"), (3, "definition"), (4, "justification"))]
    _folded(w, _planted(beats, **_room(decided=("p_other",))), witness=True)
    assert [_held(w, who, "temper") for who in ("p_low", "p_other", "p_mid")] == [[("temper", "p_mid", "fact", 100)], [("temper", "p_mid", "fact", 100)], []]
    _folded(w, _planted(beats, **_room(decided=("p_other",))), act_id="a22-second", witness=True)
    assert len(_held(w, "p_low", "temper")) == 2


def test_a_bystander_holds_heard_and_no_ruling():
    """A person in the room who neither speaks nor decides holds one `heard` claim, of the man who bore the matter, and nothing of what was decided: no
    verdict is his, and the one who decides holds no `heard`. FALSIFIER: a `heard` claim in a decider's or a speaker's ledger, or a verdict naming him."""
    w = _world()
    events = _folded(w, _planted([_beat(1, "p_low", "for", 0.0), _beat(2, "p_mid", "against", 0.0)], **_room()), witness=True)
    assert _held(w, "p_other") == [("heard", "p_low", "m1", 100)]
    assert [_held(w, who, "heard") for who in ("p_low", "p_mid")] == [[], []]
    assert [who for who, _ in world_q.ending_verdicts(events[0])] == ["p_mid"]


def test_a_silent_accused_leaves_contumacy_claims():
    """An accused who rests, or presses, in place of an answer a standing point is owed (`evaded`) leaves a `contumacy` claim of him with the judge and the
    accuser, one for each issue; a speech that raises in place of an answer, and a rest where nothing stood, leave none. FALSIFIER: a claim from the `argue`
    on the third issue or the unowed rest on the fourth."""
    w = _world()
    beats = [_beat(1, "p_low", "for", 0.0, issue="fact"),
             _beat(2, "p_mid", "against", 0.0, issue="fact", move="rest", relation="rests", evaded=True),
             _beat(3, "p_mid", "against", 0.0, issue="definition", move="press", relation="presses", evaded=True),
             _beat(4, "p_mid", "against", 0.0, issue="justification", evaded=True),
             _beat(5, "p_mid", "against", 0.0, issue="procedure", move="rest", relation="rests")]
    _folded(w, _planted(beats, **_room(decided=("p_other",))), witness=True)
    want = [("contumacy", "p_mid", "fact", 100), ("contumacy", "p_mid", "definition", 100)]
    assert [_held(w, who, "contumacy") for who in ("p_other", "p_low", "p_mid")] == [want, want, []]


def test_a_yield_leaves_the_questioner_what_the_band_names():
    """Under the `yield` disposal the questioner holds a `yielded` claim of the questioned man at the claim's full weight at Success, a `hinted` one at
    its weight (0.4) at Partial and neither at Failure; a sitting whose row disposes nothing leaves neither at any band. FALSIFIER: a claim in the
    questioned man's ledger, or a `yielded` claim at Partial."""
    full = _world().fixtures.get("confidence_default")
    beats = [_beat(1, "p_low", "for", 0.0), _beat(2, "p_mid", "against", 0.0, move="concede", relation="concedes")]
    held = {}
    for arrangement, degree in (("interrogation", "Success"), ("interrogation", "Partial"), ("interrogation", "Failure"), ("conversation", "Success")):
        w = _world()
        _folded(w, _planted(beats, "yielded", "p_mid", arrangement=arrangement, **_room(read=())), degree=degree, witness=True)
        assert _held(w, "p_mid", "yielded", "hinted") == []
        held[arrangement, degree] = _held(w, "p_low", "yielded", "hinted")
    assert held == {("interrogation", "Success"): [("yielded", "p_mid", "m1", full)], ("interrogation", "Partial"): [("hinted", "p_mid", "m1", round(0.4 * full))],
                    ("interrogation", "Failure"): [], ("conversation", "Success"): []}, held


def test_the_cards_cells_a_rigged_forum_and_a_conflicted_seat_are_deposited():
    """A forum the card shows tilted leaves a `rigged` claim of the arranger with each person in the room, a played adjudicator whose ruling departed
    from his own track an `overruled` one, and a decider whose conflict reaches `recuse_at` a `partial` one with everyone but himself; a decider with no
    ties holds none. FALSIFIER: a `partial` claim of the unconflicted `p_high`, or one in `p_king`'s ledger (not in the room)."""
    w = _world()
    w.persons["p_other"].stance = [("p_low", 5, 5)]                                              # the seat favours the bearer: a conflict
    who = ("p_low", "p_mid", "p_other", "p_high")
    card = _card(decided_by=("p_other", "p_high"), arranged_by="p_king", tilt=0.5, tilted_against="against")
    _folded(w, _planted([_beat(1, "p_low", "for", 0.0), _beat(2, "p_mid", "against", 0.0)], who=who, card=card, ruled=(("p_high", 0.4),),
                        verdicts=(("p_other", 3.0),), read=("p_other",)), witness=True)
    assert all(_held(w, x, "rigged") == [("rigged", "p_king", ("against", 500), 100)] for x in who) and _held(w, "p_king") == []
    assert [_held(w, x, "overruled") for x in ("p_low", "p_other", "p_high")] == [[("overruled", "p_high", 400, 100)], [("overruled", "p_high", 400, 100)], []]
    partial = {x: [(s, v) for k, s, v, _ in _held(w, x, "partial")] for x in who}
    assert partial["p_other"] == [] and partial["p_high"] != [] and {s for s, _ in partial["p_high"]} == {"p_other"}, partial
    assert all(partial[x] == partial["p_high"] for x in ("p_low", "p_mid")) and partial["p_high"][0][1][0] >= round(1000 * w.fixtures.get("recuse_at")), partial
