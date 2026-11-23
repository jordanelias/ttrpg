"""B24p.13 -- the host builder and the card (V2 p2 §A, §H, §I; p1 §E): `seam/wrappers/sigma.py::proceeding_input` and `::card`.

A hand-built world (`probes.tiny_world`: realm R > duchy D > settlement S > hearth Hh, the Duke `p_high` on `off_duke`), no driver, no caller:
the builder is read on its own, and the one module call is `social_contest.proceeding` reached by its composition row, as the host reaches it.
Shared with the provider path's, the verb rows' and the written sitting's tests (B24p.14, .16, .19, .20, .22)."""
from __future__ import annotations

import copy
from dataclasses import fields, is_dataclass, replace

import pytest

from engine.dice_engine import fmath
from engine.substrate import composition

from ..data import arrangements as A
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.rosters import GROUNDS, PROCEEDING_MOVES, RUNG_KINDS
from ..harness import probes as PR
from ..queries.inputs import Card, Input
from ..seam.wrappers import sigma as S
from ..state.carriers import Claim, Office, Person, Record, Tenure
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
    kind it does not admit, speaks more turns than it gives, and the verdicts are its adjudicators' and no others."""
    w = _world()
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
