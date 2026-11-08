"""v11 CR-56 -- THE MATTER IS STAMPED WHERE IT WAITS (`workplans/valoria_master_workplan_v11_part4.md` CR-56;
reasons-to-convene RL1 and its re-slot step). Two mechanisms, each with its [ASSUMPTION; medium; Jordan to
correct] written where the code reads it:
  (i)  `world_q.matters_awaiting(w, p)` stamps, as `Rung` beside `places_named`, for each undated person-matter on
       the docket (`world_q.undated_matters`), the lowest rung among `p`'s own convening seats that contains the
       matter's place, so `convene` forms on the tier that can hear it;
  (ii) CALENDAR's re-slot step (`loop/calendar.py`) moves each undated person-matter into the open slot
       `world_q.slot_for` finds for it, since no act back-fills a matter already waiting.

The world is `test_u7_remit.py`'s (`probes.tiny_world`): `p_high` holds `off_duke` (rung `D`, granting `convene`)
and lives in `S` < `D`; the party `p_mid` lives in `Hh` < `S`; `p_king` lives in `R`, outside `D`. `places_named`
never offers the Duke `D` (he lives under it), so a `D` stamp is this item's.

FALSIFIERS (each seen red with its mechanism removed, then green): the waiting matter's tier is stamped and
`convene` forms on it; of two convening seats the lower is stamped; a waiting matter fills a later slot.
CONTROLS: a world with no docketed person-matter stamps nothing and forms no such Candidate; a matter outside
every convener's seat stays unstamped and undated; a non-person matter is never re-slotted; the stamp leaves
the question order untouched (the stop condition: it displaces no question `attention_key` ranks first).
The seeded reading (two seasons at seed 0, one at seeds 1 and 2) is in the item's receipt, not pinned here.
"""

from __future__ import annotations

from ..data.matrix import WriteClass
from ..data.verbs import CONVENING_REMIT_ACTS
from ..decision import opening_set
from ..loop.driver import mint_token
from ..queries import world_q
from ..state.carriers import Office, Tenure, View
from .test_u7_remit import DUKE, OUTSIDER, PARTY, SEAT, _act, _fold, _kinds, _open, _world


def _convene_at(w, d, venue, key="cv"):
    out = _fold(w, d, _act(key, "convene", via=SEAT, subject=venue))
    assert _kinds(out) == ["date.scheduled"], _kinds(out)
    did, = [k for k, v in w.dates.items() if v.get("venue") == venue and not v.get("fired")]
    return did


def _next_calendar(w, d):
    w.tick += 1
    return d.calendar(mint_token(w, WriteClass.CALENDAR))


def _convene_subjects(w, pid):
    p = w.persons[pid]
    q = world_q.questions_for(w, p)[0]
    view = View(p.id, [], w.fixtures.get("view_k"), q)
    return q, {c.subject for c in opening_set(p, view, q, w.fixtures) if c.verb == "convene"}


def _plant(w, matter):
    w.docket.append({"date": None, "matter": matter, world_q.DOCKET_ARRANGEMENT: None,
                     world_q.DOCKET_PETITION: None})


# ======================================================================================
# (i) THE STAMP
# ======================================================================================

def test_the_convening_acts_are_read_off_the_rows():
    assert CONVENING_REMIT_ACTS == {"convene"}, CONVENING_REMIT_ACTS


def test_a_waiting_matter_stamps_its_tier_and_convene_forms_there_and_not_before():
    w, d = _world()
    # CONTROL: no docketed person-matter -- nothing stamped, no Candidate on the tier.
    assert world_q.matters_awaiting(w, w.persons[DUKE]) == ()
    q, subjects = _convene_subjects(w, DUKE)
    assert ("D", "Rung") not in q.classes and "D" not in subjects, (q.classes, subjects)
    assert _kinds(_fold(w, d, _open("oc"))) == ["case.opened"]          # no slot open: a dateless item
    assert world_q.undated_matters(w) == [w.docket[0]] and w.docket[0]["matter"] == PARTY
    assert world_q.matters_awaiting(w, w.persons[DUKE]) == ("D",)
    q, subjects = _convene_subjects(w, DUKE)
    assert ("D", "Rung") in q.classes and "D" in subjects, (q.classes, subjects)
    # A person with no convening seat is offered nothing.
    assert world_q.matters_awaiting(w, w.persons[PARTY]) == ()


def test_of_two_convening_seats_the_lowest_that_contains_the_matter_is_stamped():
    w, d = _world()
    w.offices["off_crown"] = Office("off_crown", "Crown", "R", ["convene"], faction="Valorsmark")
    w.add_tenure(Tenure("t_crown", DUKE, "off_crown", "hold", since=0))
    _plant(w, PARTY)                          # in Hh < S < D < R: both seats contain it, D is lower
    assert world_q.matters_awaiting(w, w.persons[DUKE]) == ("D",)
    _plant(w, OUTSIDER)                       # in R alone: only the Crown's seat contains it
    assert world_q.matters_awaiting(w, w.persons[DUKE]) == ("D", "R")


def test_a_matter_outside_every_conveners_seat_is_not_stamped_and_stays_undated():
    w, d = _world()
    _plant(w, OUTSIDER)                       # lives in R; the Duke's one seat is D
    assert world_q.matters_awaiting(w, w.persons[DUKE]) == ()
    did = _convene_at(w, d, "D")
    _next_calendar(w, d)
    assert world_q.open_slots(w, "D") == [{"date": did, "matter": None}]
    assert world_q.undated_matters(w)[0]["matter"] == OUTSIDER, w.docket


def test_the_stamp_displaces_no_question(monkeypatch):
    """The entry's stop condition: the stamp rides the question he answers and reorders nothing."""
    w, d = _world()
    _plant(w, PARTY)
    duke = w.persons[DUKE]
    with_stamp = world_q.questions_for(w, duke)
    monkeypatch.setattr(world_q, "matters_awaiting", lambda w_, p_: ())
    without = world_q.questions_for(w, duke)
    assert len(without) >= 2, "one question cannot be displaced: the order is unobserved"
    assert [q.id for q in with_stamp] == [q.id for q in without]
    assert set(with_stamp[0].classes) - set(without[0].classes) == {("D", "Rung")}


# ======================================================================================
# (ii) THE RE-SLOT
# ======================================================================================

def test_a_waiting_matter_fills_a_later_slot_that_reaches_it():
    w, d = _world()
    assert _kinds(_fold(w, d, _open("oc"))) == ["case.opened"]
    waiting = dict(w.docket[0])
    did = _convene_at(w, d, "D")
    cal = _next_calendar(w, d)
    assert _kinds(cal) == ["date.fired", "docket.formed", "docket.formed"], _kinds(cal)
    assert w.docket == [{**waiting, "date": did}], w.docket
    assert world_q.undated_matters(w) == [] and world_q.slot_for(w, PARTY) is None
    fired, _, slotted = cal
    assert world_q.anchor_of(w, slotted) == "D" and slotted.causes == [fired.id], slotted.causes


def test_a_matter_that_is_no_person_is_not_re_slotted():
    w, d = _world()
    _plant(w, "Hh")
    did = _convene_at(w, d, "D")
    cal = _next_calendar(w, d)
    assert _kinds(cal) == ["date.fired", "docket.formed"], _kinds(cal)
    assert world_q.open_slots(w, "D") == [{"date": did, "matter": None}]
    assert {"date": None, "matter": "Hh", world_q.DOCKET_ARRANGEMENT: None,
            world_q.DOCKET_PETITION: None} in w.docket
