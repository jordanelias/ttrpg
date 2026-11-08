"""v11 CR-55 -- *a matter lapses visibly*: a docket item held beyond `Fixtures docket_lapse` seasons is
taken off the docket by MATTER, one gate write, `matter.lapsed`, `causes` the Event that put it there;
and an overdue term stage matures once, not never and not again (`loop/matter.py`).

Three docket facts held an item for ever with no Event, each built by hand below and none run in a
seeded realm at the two-season horizon (a lapse of 4 cannot fire inside two seasons; the realm test
reads the rule at 0). An item docketed in season `t` is heard through season `t + lapse` and lapses at the
barrier opening `t + lapse + 1` (MATTER precedes DELIBERATE: `>=` took a matter from a bench in the very
season its count ran out, which `test_sc01_the_bar` saw red):
  * a DEAD PARTY -- `remove_person` closes his edges and never touches `w.docket`;
  * a VENUE WITH NO BENCH -- the sitting's slot is filled, `judging_set` is empty, nobody can determine;
  * a MATTER THAT IS NO PERSON -- `open_case` accepts any id and `determine` binds a person.
The rule asks why of none of them: it counts seasons from the item's own beginning
(`world_q.lapsing_items`), which stores nothing.

THE FALSIFIERS, each seen red with its mechanism removed (2026-11-08, the planted failure in each
docstring), then restored:
  * an item held the lapse emits `matter.lapsed` and leaves the docket; no item outlives the rule;
  * the control (`docket_lapse = None`) emits none, however many seasons pass;
  * a carried matter ages from the carry, not an older `open_case` of it (B10-13 Phase 3: the old precedence is red);
  * an undated matter the lapse is about to take is not re-slotted (the `lapsing` skip deleted is red);
  * an overdue stage matures once: `due != w.tick` never matured it; dropping the once-guard matures it
    at every barrier after.
"""

from __future__ import annotations

from ..data.matrix import Step, WriteClass
from ..harness import populated as POP
from ..loop.driver import SeasonDriver, mint_token, resolvable_verbs
from ..loop.matter import _die
from ..decision import make_chooser
from ..queries import world_q
from ..state.carriers import Act, Event, Record, Tenure
from ..state.ids import H, ROOT, draw_factory
from .test_cr56_matter_stamped import _convene_at, _next_calendar
from .test_sc01_fired_slot import VENUE, _convene, _next_season_calendar
from .test_u7_remit import DUKE, PARTY, SEAT, _fold, _kinds, _open, _world


def _season(w, d):
    """The next season's MATTER barrier alone: the tick advances, MATTER runs, its Events reach the log."""
    w.tick += 1
    return d.matter(mint_token(w, WriteClass.MATTER), [])


def _lapsed(w):
    return [e for e in w.log if e.kind == "matter.lapsed"]


def _docketing(w, kind="case.opened"):
    e, = [e for e in w.log if e.kind == kind]
    return e


def _outlives(w):
    """The docket items the rule says should be gone -- what `lapsing_items` still finds at a barrier."""
    return world_q.lapsing_items(w, w.fixtures.get("docket_lapse"))


# ======================================================================================
# THE THREE DOCKET FACTS
# ======================================================================================

def test_a_dead_partys_item_lapses_visibly_at_the_rule_and_not_before():
    """PLANTED FAILURE: the lapse loop in `matter` deleted -- the item is held for ever, red."""
    w, d = _world(docket_lapse=2)
    assert _kinds(_fold(w, d, _open("oc"))) == ["case.opened"]
    item, = w.docket
    # The party dies the way MATTER's own deaths do (`_die`, inside a gate window); his item stays.
    w.step = Step.MATTER
    _die(w, mint_token(w, WriteClass.MATTER), PARTY)
    assert PARTY not in w.persons and w.docket == [item], "the death touched the docket"
    for _ in range(3):                         # docketed at 0: heard through season 2, gone as 3 opens
        assert w.docket == [item] and not _lapsed(w), "an item lapsed inside its count"
        _season(w, d)
    ev, = _lapsed(w)
    assert w.docket == [] and ev.emitted_at == 3
    assert ev.causes == [_docketing(w).id], "the lapse does not name the Event that docketed the matter"
    assert world_q.anchor_of(w, ev) == PARTY
    assert not _outlives(w)


def test_a_bench_less_venues_slot_lapses_with_its_matter():
    """The slot is filled, nobody sits (the Duke's seat is vacated), `judging_set` is empty. PLANTED
    FAILURE: `lapsing_items` returning `[]` -- the filled slot is held for ever, red."""
    w, d = _world(docket_lapse=2)
    did = _convene(w, d)
    _next_season_calendar(w, d)
    assert _kinds(_fold(w, d, _open("oc"))) == ["case.opened"]
    filled, = w.docket
    assert filled["date"] == did and filled["matter"] == PARTY
    hold, = [t for t in w.tenures if t.kind == "hold" and t.object == SEAT and t.live]
    hold.until = w.tick
    assert world_q.judging_set(w, VENUE) == [], "a bench still sits"
    opened = w.tick
    while w.tick < opened + 3:
        assert w.docket == [filled] and not _lapsed(w)
        _season(w, d)
    ev, = _lapsed(w)
    assert w.docket == [] and world_q.anchor_of(w, ev) == VENUE, "slot and matter go together, under the venue"
    assert ev.causes == [_docketing(w).id]
    assert not _outlives(w)


def test_a_matter_that_is_no_person_lapses_the_same_way():
    """`open_case` accepts any id; a rung under the venue fills no slot (`slot_for`), so the item is
    dateless, and `determine` binds a person, so nothing ever clears it."""
    w, d = _world(docket_lapse=2)
    assert _kinds(_fold(w, d, _open("oc", subject="Hh"))) == ["case.opened"]
    assert w.docket[0]["date"] is None and w.docket[0]["matter"] == "Hh"
    for _ in range(3):
        assert not _lapsed(w)
        _season(w, d)
    ev, = _lapsed(w)
    assert w.docket == [] and world_q.anchor_of(w, ev) == "Hh" and ev.causes == [_docketing(w).id]


def test_an_empty_slot_lapses_too_chained_on_the_docket_formed_that_made_it():
    """No item outlives the rule, an empty sitting's slot included: its age is its Date's `due_at`."""
    w, d = _world(docket_lapse=2)
    did = _convene(w, d)
    _next_season_calendar(w, d)
    slot, = w.docket
    assert slot == {"date": did, "matter": None}
    formed, = [e for e in w.log if e.kind == "docket.formed"]
    since = w.dates[did]["due_at"]
    while w.tick < since + 3:
        assert w.docket == [slot], "the slot lapsed early"
        _season(w, d)
    ev, = _lapsed(w)
    assert w.docket == [] and ev.causes == [formed.id] and world_q.anchor_of(w, ev) == VENUE


def test_a_slot_a_determination_emptied_lapses_on_the_event_that_formed_it_not_the_re_slot_at_its_tick():
    """Two `docket.formed` at one (venue, tick): the slot's own, and CALENDAR's re-slot of a waiting matter
    (CR-56). The re-slotted item is then emptied (a determination's effect, by hand here), and its lapse
    `causes` the slot-forming Event. PLANTED FAILURE: `formed[...] = e` -- the later Event wins, red."""
    w, d = _world(docket_lapse=2)
    assert _kinds(_fold(w, d, _open("oc"))) == ["case.opened"]       # no slot open: a waiting, dateless item
    did = _convene_at(w, d, VENUE)
    cal = _next_calendar(w, d)
    assert _kinds(cal) == ["date.fired", "docket.formed", "docket.formed"], _kinds(cal)
    _, slot_formed, reslotted = cal
    item, = w.docket
    assert item["date"] == did and item["matter"] == PARTY, "the waiting matter did not take the slot"
    item["matter"] = None                                            # the determination emptied the slot
    since = w.dates[did]["due_at"]
    while w.tick < since + 3:
        assert w.docket == [item] and not _lapsed(w)
        _season(w, d)
    ev, = _lapsed(w)
    assert w.docket == [] and ev.causes == [slot_formed.id] and ev.causes != [reslotted.id], ev.causes


def test_a_carried_matter_ages_from_the_carry_not_from_an_older_case_of_the_same_matter():
    """A matter opened at tick 0, determined and cleared, then CARRIED at tick 6: the carry's act subject is the
    PETITION, the older `open_case`'s the matter, and the item holds both. Its age is the carry's. PLANTED
    FAILURE: `by_ref.get(matter) or by_ref.get(petition)` in `lapsing_items` (the matter's older Event wins) --
    the item is returned at tick 7 as 7 seasons old, red."""
    w, d = _world(docket_lapse=4)
    assert _kinds(_fold(w, d, _open("oc"))) == ["case.opened"]
    opened = _docketing(w)
    assert opened.emitted_at == 0
    w.docket.clear()                                     # determined and cleared, by hand
    w.tick = 6
    w.acts.append(Act("act_carry", DUKE, "carry", payload={"subject": "pet_x"}))
    carried = Event("ev_carry", "petition.carried", [], ["act_carry"], 6)
    assert carried.kind in world_q.DOCKETING_KINDS, "the carry Event is not a docketing kind"
    w.log.append(carried)
    w.docket.append({"date": None, "matter": PARTY, world_q.DOCKET_ARRANGEMENT: None,
                     world_q.DOCKET_PETITION: "pet_x"})
    w.tick = 7
    assert world_q.lapsing_items(w, 4) == [], "the carried matter aged from the older open_case"
    w.tick = 11                                          # carried at 6, heard through 10, beyond 4 seasons at 11
    (item, eid), = world_q.lapsing_items(w, 4)
    assert item is w.docket[0] and eid == carried.id, "the lapse does not name the carry"


def test_an_undated_matter_the_lapse_is_about_to_take_is_not_re_slotted_into_a_fresh_slot():
    """A person-matter docketed at tick 0 and still dateless at tick 5 (`docket_lapse` 2) is beyond the rule when a
    sitting fires. CALENDAR's re-slot would move it into the fresh slot only for MATTER, next, to take it off with
    the item; it stays dateless, the slot stays empty, and MATTER lapses it. PLANTED FAILURE: the `lapsing` skip in
    `loop/calendar.py` deleted -- the matter takes the slot, red."""
    w, d = _world(docket_lapse=2)
    assert _kinds(_fold(w, d, _open("oc"))) == ["case.opened"]
    w.tick = 4
    did = _convene_at(w, d, VENUE)
    cal = _next_calendar(w, d)                           # tick 5: the sitting fires
    assert _kinds(cal) == ["date.fired", "docket.formed"], _kinds(cal)
    assert world_q.lapsing_items(w, 2) and w.tick - _docketing(w).emitted_at > 2, "the item is not past the rule"
    assert world_q.open_slots(w, VENUE) == [{"date": did, "matter": None}], "the lapsing matter took the slot"
    item, = world_q.undated_matters(w)
    assert item["date"] is None and item["matter"] == PARTY
    _season(w, d)                                        # MATTER lapses it
    ev, = _lapsed(w)
    assert world_q.anchor_of(w, ev) == PARTY and world_q.undated_matters(w) == []
    assert w.docket == [{"date": did, "matter": None}], w.docket


def test_the_lapse_leaves_the_neighbouring_item_alone():
    """Two matters docketed in different seasons: the first lapses at its own count, the second at its
    own, not at the first's."""
    w, d = _world(docket_lapse=2)
    assert _kinds(_fold(w, d, _open("oc1", subject="Hh"))) == ["case.opened"]
    _season(w, d)
    assert _kinds(_fold(w, d, _open("oc2", subject="S"))) == ["case.opened"]
    _season(w, d)                              # tick 2
    assert len(w.docket) == 2 and not _lapsed(w)
    _season(w, d)                              # tick 3: the first is beyond two seasons, the second not
    assert [i["matter"] for i in w.docket] == ["S"] and len(_lapsed(w)) == 1
    _season(w, d)                              # tick 4
    assert w.docket == [] and len(_lapsed(w)) == 2


# ======================================================================================
# THE CONTROL
# ======================================================================================

def test_the_rule_at_never_lapses_nothing_however_long_the_item_is_held():
    w, d = _world(docket_lapse=None)
    assert _kinds(_fold(w, d, _open("oc", subject="Hh"))) == ["case.opened"]
    for _ in range(12):
        _season(w, d)
    assert len(w.docket) == 1 and not _lapsed(w)
    assert world_q.lapsing_items(w, None) == []


def test_an_item_with_no_beginning_does_not_lapse():
    """A hand-planted dateless item with no docketing Event: its age is unknown, and unknown is not old."""
    w, d = _world(docket_lapse=1)
    w.docket.append({"date": None, "matter": "Hh", world_q.DOCKET_ARRANGEMENT: None,
                     world_q.DOCKET_PETITION: None})
    for _ in range(3):
        _season(w, d)
    assert len(w.docket) == 1 and not _lapsed(w)


# ======================================================================================
# AN OVERDUE STAGE MATURES ONCE
# ======================================================================================

def _staged(w, d, stages, key="rec_cr55"):
    """A Record held by the Duke with the given `(due, label, winder)` stages, minted without a fold."""
    w.records[key] = Record(key, VENUE, "text", stages=list(stages))
    w.add_tenure(Tenure(f"t_{key}", DUKE, key, "hold", since=w.tick))
    return key


def _matured(w, key):
    return [e for e in w.log if e.kind == "term.matured" and any(c.subject == key for c in e.changes)]


def test_a_stage_that_missed_its_due_tick_matures_once_and_not_again():
    """The world skips the due tick (a hand-driven fold, a builder that starts mid-campaign): `due != w.tick`
    never matured it. PLANTED FAILURES: the old `!=` -- zero maturations, red; the once-guard deleted --
    a maturation at every barrier after, red."""
    w, d = _world()
    key = _staged(w, d, [(1, "stage1", ROOT)])
    w.tick = 3                                   # ticks 1 and 2 were never run
    d.matter(mint_token(w, WriteClass.MATTER), [])
    assert len(_matured(w, key)) == 1, "an overdue stage did not mature"
    for _ in range(3):
        _season(w, d)
    assert len(_matured(w, key)) == 1, "an overdue stage matured again"


def test_each_stage_matures_once_at_its_own_tick_and_a_later_stage_is_not_taken_for_the_earlier():
    w, d = _world()
    key = _staged(w, d, [(2, "stage1", ROOT), (5, "stage2", ROOT)])
    seen = []
    for _ in range(7):
        _season(w, d)
        seen.append((w.tick, len(_matured(w, key))))
    assert seen == [(1, 0), (2, 1), (3, 1), (4, 1), (5, 2), (6, 2), (7, 2)], seen


def test_two_overdue_stages_both_mature_at_the_first_barrier_that_finds_them():
    """The once-guard reads the last maturation BEFORE the pass emits: the first stage's maturation does
    not hide the second, due by the same tick."""
    w, d = _world()
    key = _staged(w, d, [(1, "stage1", ROOT), (2, "stage2", ROOT)])
    w.tick = 4
    d.matter(mint_token(w, WriteClass.MATTER), [])
    assert len(_matured(w, key)) == 2
    _season(w, d)
    assert len(_matured(w, key)) == 2


def test_a_stage_whose_winder_was_gone_at_its_tick_matures_once_when_he_is_back():
    w, d = _world()
    key = _staged(w, d, [(1, "stage1", ROOT)])
    hold, = [t for t in w.tenures if t.object == key and t.kind == "hold"]
    hold.until = 0                               # nobody winds it at tick 1
    _season(w, d)
    assert not _matured(w, key)
    hold.until = None                            # he holds it again
    _season(w, d)
    assert len(_matured(w, key)) == 1
    _season(w, d)
    assert len(_matured(w, key)) == 1


def test_a_stage_wound_by_an_act_matures_once_though_no_logged_event_touches_the_record():
    """The winder is an ACT id, and no logged Event names the Record: `term.matured` then `causes` the act, so
    `anchor_of` answers the MAKER and not the Record (`matured_terms`' docstring, H-129's shape). The once-guard
    must read the Event that WROTE the Record (`last_emission_of(..., written=True)`). PLANTED FAILURE: the
    unkeyed `last_emission_of("term.matured", rid)` -- it finds no maturation, and the stage matures at every
    barrier, red."""
    w, d = _world()
    w.acts.append(Act("act_wind", DUKE, "create_record"))
    key = _staged(w, d, [(1, "stage1", "act_wind")])
    assert not [e for e in w.log if any(c.subject == key for c in e.changes)], "an Event already names the Record"
    _season(w, d)
    ev, = _matured(w, key)
    assert ev.causes == ["act_wind"] and world_q.anchor_of(w, ev) == DUKE, "the act is not the cause"
    for _ in range(3):
        _season(w, d)
    assert len(_matured(w, key)) == 1, "a stage wound by an act matured again at a later barrier"


# ======================================================================================
# THE REALM, TWO SEASONS, SEED 0
# ======================================================================================

def _realm(lapse):
    w = POP.build_realm(0)
    w.fixtures = w.fixtures.sweep("docket_lapse", lapse)
    d = SeasonDriver(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(), draw=draw_factory(w.world_seed, lambda: w.tick))
    for _ in range(2):
        d.season(ch, question=None, contest_max_depth=w.fixtures.get("contest_max_depth"))
    return w


def test_in_the_realm_a_lapse_of_zero_emits_visibly_and_the_control_emits_nothing():
    """The shipped rule (4) cannot fire inside two seasons, so the instrument reads it at 0: every item the
    first season docketed is beyond a count of zero at the second season's MATTER. Each lapse names a docketing
    Event in the log, a claim of it reaches a ledger (it is witnessed like any other), and the control run
    (`None`) is the same world with none. PLANTED FAILURE: the `emits=` kind changed -- the gate refuses."""
    on, off = _realm(0), _realm(None)
    lapsed = _lapsed(on)
    assert len(lapsed) >= 1 and not _lapsed(off)
    ids = {e.id for e in on.log}
    for e in lapsed:
        assert e.causes and all(c in ids for c in e.causes), e
        assert {x.kind for x in on.log if x.id in e.causes} <= {"case.opened", "petition.carried", "docket.formed"}
    assert len(on.docket) < len(off.docket)
    assert any(c.predicate == "matter.lapsed" for p in on.persons.values() for c in p.ledger)
    assert on.content_hash() != off.content_hash()
