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
from ..queries.inputs import Card, Input, Margin, Outcome, Sitting
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
    assert len(ranked) == 3 and ranked[0] > ranked[1] > ranked[2] and margin(out) == pytest.approx(ranked[1])
    bend = lambda who: replace(out, verdicts=tuple((i, _m(-100.0) if i == who else m) for i, m in out.verdicts))
    by_margin = sorted(out.verdicts, key=lambda v: v[1].net - v[1].ob)
    assert margin(bend(by_margin[0][0])) == pytest.approx(ranked[1])                            # the worst seat, bent, moves nothing
    assert margin(bend(by_margin[1][0])) == pytest.approx(ranked[2])                            # the quorum-th seat, bent, does: the control


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
FIVE = ("argue", "tell", "lie", "speak", "interrogate")


def _act(verb, **payload):
    return Act(id=f"a_{verb}", actor="p_low", verb=verb, payload=payload)


def test_five_rows_proceed_and_name_a_loadable_row():
    """Each of the five verbs carries a `proceeds` cell whose every entry names an arrangement the tree loads (or the docket's own row), a
    form, and a drawing move; no other verb is routed (`covenant`, `interview`, `determine` are their own items'). A planted cell that names a
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


def test_an_arrest_still_resolves_on_the_single_roll(monkeypatch):
    """CONTROL: `arrest` carries no `proceeds:` cell, so the same call takes today's path: the spy sees `social_contest.roll` and no sitting, and
    the result carries no proceeding. The five verbs' prize rows name the same provider, so what separates them is the row's cell alone."""
    from ..loop.driver import SeasonDriver
    w = _world()
    SeasonDriver(w)
    spy = _Spy(monkeypatch)
    out = _seamed(w, "arrest", "a standing", to="p_other")
    assert out["status"] == "RESOLVED" and len(spy.rolls) == 1 and not spy.sittings and "proceeding" not in out, out
