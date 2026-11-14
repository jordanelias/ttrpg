"""CP-T04-07 (B10-12; AM-C-12 REPAIR): `surrender`, the holder yields a threatened place on terms. A seat granting `dispatch`
whose faction holds a settlement a `siege.pressed` named THIS SEASON gives the place to the person who pressed the siege: a
`hold` on the settlement opens to him and the yielding seat's live `hold` on it, if any, closes, in one write
(`loop/effects_information.py::_eff_surrender`, through `_take_hold`), and `place.surrendered` is emitted. The effect asks
`state/gate.py::may_cede` -- `may_warrant`'s shape -- that the exercised seat BELONGS TO `holder_faction_of(subject)`, and
declines `NO_CHANGE` as `surrender.refused` (the `_eff_arrest` precedent; no new `requires` stem). The write gate admits the
two edges under its new `cession` basis. This file is the item's own; nothing here is a shared pin.

SHIPPED WITHHELD (`Fixtures withheld_verbs`, `marshal`'s precedent): a `remit:dispatch` verb that forms for every eligible
person moves every seeded season, and the entry's Hash is EQUAL at shipped. So no Candidate forms; every `surrender` here is a
hand-built act folded through the real driver (`_fold_one`), its events appended to `w.log` as `SeasonDriver.season` does
between rounds, which is what `world_q.siege_pressed_by` reads.

THE WORLD IS HAND-BUILT, NOT NATURAL. A natural run emits no `siege.pressed` (`restore` never executes on a garrison Site,
CP-T04-06), so the threat is made here: the Crown's two marchers (`set_s_014`) press `set_s_036` (the Church's) under the
`besiege` posture, swept into the roster in a test copy as `test_cp_t04_06_besiege.py` does. The realm fixture is the one
`test_cp_t04_05_graded_walls._world` builds.

FALSIFIER (the entry's): a surrendered and a stormed town, the same pair, paired seeds (`world_seed` 0..N-1, N = `SEEDS`),
BOTH end with the hold moved to the Crown, but only the stormed one writes body and stance rows. A fold costs 0.07 to 0.3 s
(measured: a besiege 0.07, a storm plus a `seize` 0.3), so the 20-seed test (both arms) took about 12 s whole. N is 20 because the claim is not
statistical: the surrendered arm is a draw-free write, so it must hold in 20 of 20 and a single exception is the failure; the
stormed arm must write in 20 of 20 (a lost field writes the attacker's own casualties, a won one both sides').
⚠ THE STORMED ARM'S HOLD MOVE IS `seize`, NOT THE FIELD: a won field moves presence and never title (#453 R-6), and in this
fixture the Crown seat's `seize` licenses even after a LOST field because a Crown member (`p_npc_037`) already stands at the
town (`world_q.occupies`); the comparison is therefore of the two ends, not of who wins the field. Identical end states
would mean the row is redundant with `march`; the test asserts they differ in exactly that column.
PLANTED FAILURES: (a) the threat reader answers nothing, so the town is not yielded and the same predicate (`hold moved, no
blood`) is false; (b) the cession predicate answers yes to anyone, so a seat of the wrong faction is not refused at the effect
and the gate's own `cession` clause refuses the opening instead (`NotYours`). CONTROLS: a refused `surrender` moves no hold; the
shipped fixtures withhold the verb, so it forms for nobody, and flipped it forms; the unflipped realm is `build_realm(0)`'s
pre-item hash."""
from __future__ import annotations

from dataclasses import replace

import pytest

from engine.season.data import rosters
from engine.season.data.verbs import CHOICE_RANGES, VERB_TABLE
from engine.season.decision import assemble
from engine.season.decision.options import opening_set
from engine.season.harness.populated import build_realm
from engine.season.loop import effects_information as eff
from engine.season.queries import world_q
from engine.season.state import gate as G
from engine.season.state.carriers import Act, Tenure
from engine.season.tests.test_cp_t04_05_graded_walls import MARCHERS, TARGET, _world
from engine.season.tests.test_march import _fold_one

SEEDS = range(20)
CROWN, CHURCH = "fac_valorsmark", "fac_church_of_solmund"
RECEIVER = MARCHERS[0]                                      # p_npc_033, Crown: the man who presses the siege
CARDINAL, CARDINAL_SEAT = "p_npc_038", "off_cardinal_justice"       # Church; dispatch; purview reaches TARGET
PRUDENCE, PRUDENCE_SEAT = "p_npc_013", "off_cardinal_prudence"      # Church; dispatch; purview reaches TARGET
REP, REP_SEAT = "p_npc_034", "off_archbishops_rep"                  # Church; dispatch; purview does NOT reach TARGET
FORTITUDE, FORTITUDE_SEAT = "p_npc_040", "off_cardinal_fortitude"   # Church; NO dispatch
KING, KING_SEAT = "p_npc_020", "off_king"                           # Crown; dispatch; purview reaches TARGET
BUILD = "8480ad84c25cb665fb41dd2c57a53c15"                          # build_realm(0), unmoved by this item


@pytest.fixture
def swept(monkeypatch):
    """`march_postures` swept to `[storm, besiege]` in a test copy, at both places the roster is read."""
    monkeypatch.setattr(rosters, "MARCH_POSTURES", ("storm", "besiege"))
    monkeypatch.setitem(CHOICE_RANGES, "posture", ("storm", "besiege"))


def _fold(w, act):
    """ONE act through the real driver, its events appended to the log as the season's round does."""
    events = _fold_one(w, act)
    for e in events:
        w.log.append(e)
    return events


def _kinds(events):
    return [e.kind for e in events]


def _besiege(w, aid="b0", target=TARGET):
    return _fold(w, Act(id=aid, actor=RECEIVER, verb="march", payload={"subject": target, "posture": "besiege"},
                        via="off_spymaster"))


def _surrender(w, actor=CARDINAL, via=CARDINAL_SEAT, aid="s0", target=TARGET):
    return _fold(w, Act(id=aid, actor=actor, verb="surrender", payload={"subject": target}, via=via))


def _blood(w):
    """Every person's body and stance rows: the two columns a fought field writes and a yielded town does not."""
    return {p: (q.body, tuple(tuple(r) for r in (q.stance or []))) for p, q in w.persons.items()}


def _holds(w, rid=TARGET):
    return [t for t in w.tenures if t.kind == "hold" and t.object == rid and t.live]


def _yielded_without_blood(w, before):
    """THE FALSIFIER'S SURRENDERED-ARM PREDICATE (one function, so a planted failure is judged by the very check the real
    arm is): the hold moved to the Crown, and no person's body or stance row changed."""
    return world_q.holder_faction_of(w, TARGET) == CROWN and _blood(w) == before


# ---- THE FALSIFIER --------------------------------------------------------------------------------------------------

def test_falsifier_a_surrendered_and_a_stormed_town_both_move_the_hold_only_the_storm_writes_blood(swept):
    surrendered = stormed = 0
    for s in SEEDS:
        # the surrendered arm
        w = _world(3, 1.0)
        w.world_seed = s
        assert world_q.holder_faction_of(w, TARGET) == CHURCH
        before = _blood(w)
        _besiege(w)
        assert "place.surrendered" in _kinds(_surrender(w)), s
        assert _yielded_without_blood(w, before), s
        surrendered += 1
        end_surrender, hash_surrender = _blood(w), w.content_hash()
        # the stormed arm: the same pair, the same seed
        v = _world(3, 1.0)
        v.world_seed = s
        _fold(v, Act(id="m0", actor=RECEIVER, verb="march", payload={"subject": TARGET}, via="off_spymaster"))
        assert "rung.seized" in _kinds(_fold(v, Act(id="z0", actor=KING, verb="seize", payload={"subject": TARGET},
                                                    via=KING_SEAT))), s
        assert world_q.holder_faction_of(v, TARGET) == CROWN, s
        end_storm = _blood(v)
        written = [p for p in before if before[p] != end_storm[p]]
        assert len(written) >= 2, (s, written)                      # a lost field writes the attacker's own, a won one both
        stormed += 1
        # the two ends are not the same end
        assert end_storm != end_surrender and v.content_hash() != hash_surrender, s
    assert (surrendered, stormed) == (len(SEEDS), len(SEEDS))       # the loop asserted: n = 20, not 0


def test_the_yielded_town_is_the_receivers_and_the_territory_keeps_its_holder(swept):
    w = _world(3, 1.0)
    territory = [t.id for t in w.tenures if t.kind == "hold" and t.live and t.object in world_q.ancestry(w, TARGET)]
    assert territory and _holds(w) == []                            # a seeded town is held through its territory
    _besiege(w)
    ev = _surrender(w)
    assert _kinds(ev) == ["place.surrendered"]
    (edge,) = _holds(w)
    assert (edge.subject, edge.object, edge.since) == (RECEIVER, TARGET, w.tick)
    assert [t.id for t in w.tenures if t.id in territory and t.live] == territory       # the territory's holder keeps it
    assert world_q.holder_faction_of(w, TARGET) == CROWN
    # `sides_of` reads the holder faction of the target: a march of the Crown's now finds no opposing holder. The declared,
    # unfought `march` that would be pending is CP-T04-04's (held), so what is asserted is the reading `sides_of` makes.
    assert world_q.holder_faction_of(w, TARGET) == world_q.faction_holding(w, MARCHERS[1])


def test_a_directly_held_town_loses_the_yielders_hold_in_the_same_write(swept):
    w = _world(3, 1.0)
    old = Tenure("t_direct", PRUDENCE, TARGET, "hold", w.tick)       # another Church person holds the town itself
    w.add_tenure(old)
    assert world_q.holder_faction_of(w, TARGET) == CHURCH
    _besiege(w)
    assert _kinds(_surrender(w)) == ["place.surrendered"]
    assert old.until == w.tick and not old.live                       # his hold closed ...
    (edge,) = _holds(w)
    assert edge.subject == RECEIVER                                    # ... and exactly one stands, the receiver's
    # the yielder himself surrenders his own town: his closure is his own (T-m), the opening is the cession's or the handover's
    w = _world(3, 1.0)
    own = Tenure("t_own", PRUDENCE, TARGET, "hold", w.tick)
    w.add_tenure(own)
    _besiege(w)
    assert _kinds(_surrender(w, PRUDENCE, PRUDENCE_SEAT)) == ["place.surrendered"]
    assert not own.live and [t.subject for t in _holds(w)] == [RECEIVER]


# ---- THE REFUSALS ----------------------------------------------------------------------------------------------------

def test_a_seat_of_the_wrong_faction_is_refused_and_no_hold_moves(swept):
    w = _world(3, 1.0)
    _besiege(w)
    before = [(t.id, t.until) for t in w.tenures if t.kind == "hold"]
    ev = _surrender(w, KING, KING_SEAT)                               # the Crown's own seat yields the Church's town
    assert _kinds(ev) == ["surrender.refused"], _kinds(ev)
    assert [(t.id, t.until) for t in w.tenures if t.kind == "hold"] == before       # CONTROL: a refusal moves no hold
    assert world_q.holder_faction_of(w, TARGET) == CHURCH


def test_a_seat_without_dispatch_or_without_purview_is_unauthorized(swept):
    w = _world(3, 1.0)
    _besiege(w)
    assert not G.may_cede(w, FORTITUDE, FORTITUDE_SEAT, TARGET, to=RECEIVER)      # the fixtures are what they say
    for actor, via in ((FORTITUDE, FORTITUDE_SEAT), (REP, REP_SEAT)):
        assert _kinds(_surrender(w, actor, via, aid=f"s_{via}")) == ["surrender.unauthorized"], via
    assert world_q.holder_faction_of(w, TARGET) == CHURCH


def test_no_siege_this_season_is_a_refusal_a_stale_or_other_siege_included(swept):
    w = _world(3, 1.0)
    assert _kinds(_surrender(w)) == ["surrender.refused"]              # no threat at all
    w = _world(3, 1.0)
    _besiege(w)
    w.tick += 1                                                         # the siege was pressed LAST season
    assert world_q.siege_pressed_by(w, TARGET) is None
    assert _kinds(_surrender(w)) == ["surrender.refused"]
    w = _world(3, 1.0)
    _besiege(w)
    assert world_q.siege_pressed_by(w, "set_s_037") is None             # a siege on this town is no threat to another
    assert _kinds(_surrender(w, target="set_s_037")) in (["surrender.refused"], ["surrender.unauthorized"])
    assert world_q.holder_faction_of(w, TARGET) == CHURCH


def test_a_place_cannot_be_yielded_to_ones_own_side(swept):
    w = _world(3, 1.0)
    _besiege(w)
    for t in w.tenures:                                                 # the besieger now sits in the Church
        if t.subject == RECEIVER and t.kind == "commit" and t.live:
            t.until = w.tick
    w.add_tenure(Tenure("t_conv", RECEIVER, CHURCH, "commit", w.tick))
    assert _kinds(_surrender(w)) == ["surrender.refused"]


# ---- THE GATE'S BASIS -----------------------------------------------------------------------------------------------

def test_the_cession_basis_admits_the_opening_and_the_closure_and_nothing_wider():
    w = build_realm(0)
    opening = Tenure("t_c1", RECEIVER, TARGET, "hold", w.tick)
    basis = lambda t, was, actor, via: G.tenure_write_basis(w, t, was, actor, via, frozenset())
    assert basis(opening, None, CARDINAL, CARDINAL_SEAT) == G.CESSION
    assert basis(opening, None, CARDINAL, None) is None                 # no seat exercised
    assert basis(opening, None, FORTITUDE, FORTITUDE_SEAT) is None     # a seat with no `dispatch` grant
    assert basis(opening, None, REP, REP_SEAT) is None                  # a seat whose purview does not reach the town
    assert basis(Tenure("t_c2", PRUDENCE, TARGET, "hold", w.tick), None, CARDINAL, CARDINAL_SEAT) is None   # to its own side
    assert basis(Tenure("t_c3", RECEIVER, CARDINAL_SEAT, "hold", w.tick), None, CARDINAL, CARDINAL_SEAT) != G.CESSION   # a seat is never ceded
    assert basis(Tenure("t_c4", RECEIVER, TARGET, "tie", w.tick), None, CARDINAL, CARDINAL_SEAT) is None               # a hold only
    held = Tenure("t_c5", PRUDENCE, TARGET, "hold", w.tick)
    w.add_tenure(held)
    was, closed = replace(held), replace(held, until=w.tick)
    assert basis(closed, was, CARDINAL, CARDINAL_SEAT) == G.SEIZURE     # a seat that may also seize closes it under the older basis
    seat = G.seat_hold(w, CARDINAL, CARDINAL_SEAT)
    seat.payload = {**seat.payload, "remit_acts": tuple(a for a in seat.payload["remit_acts"] if a != G.SEIZURE_ACT)}
    assert G.SEIZURE_ACT not in seat.granted_acts                        # a dispatch seat with no `issue`: only `cession` is left
    assert basis(closed, was, CARDINAL, CARDINAL_SEAT) == G.CESSION     # the yielding side's own hold may be closed
    other = replace(closed, subject=RECEIVER)
    assert basis(other, replace(was, subject=RECEIVER), CARDINAL, CARDINAL_SEAT) is None    # an enemy's may not


def test_may_cede_asks_the_belonging_when_a_caller_can_read_the_query():
    w = build_realm(0)
    assert G.may_cede(w, CARDINAL, CARDINAL_SEAT, TARGET, to=RECEIVER)
    assert G.may_cede(w, CARDINAL, CARDINAL_SEAT, TARGET, to=RECEIVER, holder_faction=CHURCH)
    assert not G.may_cede(w, CARDINAL, CARDINAL_SEAT, TARGET, to=RECEIVER, holder_faction=CROWN)
    assert not G.may_cede(w, CARDINAL, CARDINAL_SEAT, TARGET)                               # neither person named
    assert not G.may_cede(w, CARDINAL, CARDINAL_SEAT, TARGET, to=RECEIVER, yielder=PRUDENCE)  # both named


# ---- MUTATIONS ------------------------------------------------------------------------------------------------------

def test_planted_failure_a_threat_reader_that_answers_nothing_yields_no_town(swept, monkeypatch):
    monkeypatch.setattr(eff, "siege_pressed_by", lambda w, place: None)
    w = _world(3, 1.0)
    before = _blood(w)
    _besiege(w)
    assert _kinds(_surrender(w)) == ["surrender.refused"]
    assert not _yielded_without_blood(w, before)                        # the falsifier's predicate is false


def test_planted_failure_a_predicate_that_answers_yes_leaves_the_refusal_to_the_gate(swept, monkeypatch):
    """The effect's belonging test gone, the Crown's seat yields the Church's town to a Crown man: the write is not refused as
    `surrender.refused` but killed at the gate, because the `cession` clause refuses an opening for the seat's own side."""
    monkeypatch.setattr(eff, "may_cede", lambda *a, **k: True)
    w = _world(3, 1.0)
    _besiege(w)
    with pytest.raises(G.NotYours):
        _surrender(w, KING, KING_SEAT)
    assert world_q.holder_faction_of(w, TARGET) == CHURCH


def test_planted_failure_without_the_cession_clause_the_gate_refuses_the_effects_own_write(swept, monkeypatch):
    """The write gate's predicate answering no (the effect's binding, a different name, is untouched): the surrender the
    effect admitted is `NotYours` at the gate and the town stays the Church's. The clause is load-bearing, not decorative."""
    monkeypatch.setattr(G, "may_cede", lambda *a, **k: False)
    w = _world(3, 1.0)
    _besiege(w)
    with pytest.raises(G.NotYours):
        _surrender(w)
    assert world_q.holder_faction_of(w, TARGET) == CHURCH


# ---- THE CONTROL: SHIPPED WITHHELD ----------------------------------------------------------------------------------

def test_control_surrender_ships_withheld_so_no_candidate_forms_and_the_realm_is_the_pre_item_one():
    w = build_realm(0)
    assert w.content_hash() == BUILD
    assert "surrender" in w.fixtures.get("withheld_verbs")
    p = w.persons[KING]
    flipped = w.fixtures.sweep("withheld_verbs", tuple(v for v in w.fixtures.get("withheld_verbs") if v != "surrender"))

    def formed(fx):
        return [c for q in world_q.questions_for(w, p) for c in opening_set(p, assemble(p, q, 12), q, fx)]
    shipped = formed(w.fixtures)
    assert "march" in {c.verb for c in shipped}                        # a dispatch seat forms Rung-classed verbs: the absence is an observation
    assert "surrender" not in {c.verb for c in shipped}
    assert any(c.verb == "surrender" for c in formed(flipped))          # the flip would form it (on every Rung the seat is offered)


def test_the_row_is_remit_dispatch_and_adds_no_requires_stem():
    row = VERB_TABLE["surrender"]
    assert row.eligibility == ("remit:dispatch",) or list(row.eligibility) == ["remit:dispatch"]
    assert row.emits == ("place.surrendered",) or list(row.emits) == ["place.surrendered"]
    assert row.requires_typed is not None
