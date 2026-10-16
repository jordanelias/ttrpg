"""v9 SC-01 FIRED-SLOT STEP -- *an `open_case` fills a fired slot, and a judge is asked about a docketed
matter* (`workplans/valoria_master_workplan_v9_part6.md` §SC-01, the v9 STEP paragraph; #453 pass-1
step 4; H-163 limit 2). Three parts, each with its [ASSUMPTION; medium; Jordan to correct] written
where the code reads it:
  (i)   `_eff_convene` gives the Date a holder, the convener's seat (`Act.via`);
  (ii)  `_eff_open_case` fills the nearest open slot of a sitting whose venue holds the matter
        (`world_q.slot_for`), and appends the dateless item only where none is open;
  (iii) `world_q.questions_for` asks each judge on a fired sitting's bench about its docketed matters
        (`world_q.sittings_before`), citing his `date.fired` claim, so a `determine` formed from it
        walks back to the firing.

The world is `test_u7_remit.py`'s (`probes.tiny_world`, one MATTER barrier): `p_high` holds `off_duke`
(rung and scope `D`) and stands in `S`; the party `p_mid` lives in `Hh` < `S` < `D`. Sittings are
convened at `S`, where the Duke stands, so CALENDAR's `date.fired` reaches his ledger (IN-29's
co-located channel); nobody stands at `D` itself.

THE FALSIFIERS (the plan's STEP FALSIFIER and STEP EXIT), each seen red before the reader landed and
green after, 2026-10-16:
  * a date with no holder still fires and lapses (a `date.fired`, no `docket.formed`, no slot) --
    beside a convened date, which now forms one (red before: the convened date lapsed too);
  * an `open_case` with no open slot holding the matter still appends the dateless item -- beside one
    that fills the slot (red before: it appended beside the slot);
  * a bench question names exactly the docketed matters before a sitting the judge heard fire, and
    nothing once the matter leaves the docket (red before: no such question);
  * THE STEP EXIT, W26's proof (`architecture/PLAN.md` W26, intent only), in one seeded run, twice,
    with an equal `World.content_hash()`.
No test here asserts execution in the seed-0 realm (v9 §0.5's relaxed exit).
"""

from __future__ import annotations

from ..data.matrix import WriteClass
from ..decision import opening_set
from ..decision.choose import pack_scenes
from ..loop.driver import mint_token
from ..queries import world_q
from ..state.carriers import Rung, Tenure, View
from .test_u7_remit import DUKE, PARTY, SEAT, _act, _determine, _fold, _kinds, _open, _world

VENUE = "S"                     # where the Duke stands, inside his seat's scope `D`


def _convene(w, d, key="cv", venue=VENUE, via=SEAT):
    out = _fold(w, d, _act(key, "convene", via=via, subject=venue))
    assert _kinds(out) == ["date.scheduled"], _kinds(out)
    did, = [k for k, v in w.dates.items() if v.get("venue") == venue and not v.get("fired")]
    return did


def _next_season_calendar(w, d):
    """The next season's barrier 1: the tick advances and CALENDAR runs (its Events reach the log)."""
    w.tick += 1
    return d.calendar(mint_token(w, WriteClass.CALENDAR))


def _sitting(w, d):
    """A convened sitting at `VENUE` that has fired and been witnessed: `(date id, CALENDAR's Events)`."""
    did = _convene(w, d)
    cal = _next_season_calendar(w, d)
    d.witness(mint_token(w, WriteClass.INTERIOR), cal)
    return did, cal


def _walks_to(w, e, target) -> bool:
    by_id = {x.id: x for x in w.log}
    stack, seen = list(e.causes), set()
    while stack:
        c = stack.pop()
        if c == target:
            return True
        if c in seen or c not in by_id:
            continue
        seen.add(c)
        stack.extend(by_id[c].causes)
    return False


# ======================================================================================
# (i) A CONVENED DATE HAS A HOLDER; A VACANT DATE STILL FIRES AND LAPSES
# ======================================================================================

def test_a_convened_date_is_held_by_the_conveners_seat_and_forms_a_slot_where_a_vacant_one_lapses():
    w, d = _world()
    did = _convene(w, d)
    assert w.dates[did]["holder"] == SEAT, w.dates[did]
    # CONTROL, the plan's first falsifier clause: a date nobody holds, due the same season.
    w.dates["d_vacant"] = dict(id="d_vacant", venue="D", due_at=w.tick + 1, holder=None, fired=False)
    cal = _next_season_calendar(w, d)
    assert w.dates[did]["fired"] and w.dates["d_vacant"]["fired"]
    assert len([e for e in cal if e.kind == "date.fired"]) == 2, _kinds(cal)
    formed = [e for e in cal if e.kind == "docket.formed"]
    assert len(formed) == 1 and world_q.anchor_of(w, formed[0]) == VENUE, (
        f"one slot for the held date and none for the vacant one: {_kinds(cal)}")
    assert w.docket == [{"date": did, "matter": None}], w.docket
    # The vacant date decided nothing: no slot names it, no bench is asked about it.
    assert world_q.open_slots(w, "D") == [] and world_q.sittings_before(w, w.persons[DUKE]) == []


# ======================================================================================
# (ii) OPEN_CASE FILLS THE SLOT, AND APPENDS ONLY WHERE NONE HOLDS THE MATTER
# ======================================================================================

def test_open_case_with_no_open_slot_holding_the_matter_still_appends_the_dateless_item():
    """The plan's second falsifier clause: today's shape where no sitting holds the matter -- in a world
    with no slot, and in one whose only open slot sits at a sibling settlement `S2` (`D` > `S2`), which
    does not hold `Hh`: the venue is the match key."""
    w, d = _world()
    assert _kinds(_fold(w, d, _open("oc"))) == ["case.opened"]
    assert w.docket == [{"date": None, "matter": PARTY, world_q.DOCKET_ARRANGEMENT: None,
                         world_q.DOCKET_PETITION: None}], w.docket
    w, d = _world()
    w.rungs["S2"] = Rung("S2", "settlement")
    w.add_tenure(Tenure("t_s2", "S2", "D", "contain", since=0))
    did = _convene(w, d, venue="S2")
    _next_season_calendar(w, d)
    assert world_q.open_slots(w, "S2") == [{"date": did, "matter": None}]
    assert world_q.slot_for(w, PARTY) is None
    assert _kinds(_fold(w, d, _open("oc"))) == ["case.opened"]
    assert w.docket == [{"date": did, "matter": None},
                        {"date": None, "matter": PARTY, world_q.DOCKET_ARRANGEMENT: None,
                         world_q.DOCKET_PETITION: None}], w.docket


def test_open_case_fills_the_nearest_fired_slot_holding_the_matter_and_appends_nothing():
    w, d = _world()
    far = _convene(w, d, key="cv_far", venue="D")
    near = _convene(w, d, key="cv_near", venue=VENUE)
    _next_season_calendar(w, d)
    assert len(w.docket) == 2 and all(i["matter"] is None for i in w.docket), w.docket
    assert _kinds(_fold(w, d, _open("oc"))) == ["case.opened"]
    assert len(w.docket) == 2, f"a dateless item was appended beside the slots: {w.docket}"
    filled, = world_q.docketed(w, PARTY)
    assert filled == {"date": near, "matter": PARTY, world_q.DOCKET_ARRANGEMENT: None,
                      world_q.DOCKET_PETITION: None}, filled
    assert world_q.open_slots(w, "D") == [{"date": far, "matter": None}]
    # A second matter in the same duchy fills the far sitting's slot (`S`'s is taken).
    assert _kinds(_fold(w, d, _open("oc2", subject="p_low"))) == ["case.opened"]
    assert world_q.docketed(w, "p_low")[0]["date"] == far and len(w.docket) == 2, w.docket


# ======================================================================================
# (iii) THE BENCH IS ASKED ABOUT WHAT IS ON THE DOCKET, AND ABOUT NOTHING ELSE
# ======================================================================================

def test_a_bench_question_names_exactly_the_docketed_matters_of_a_sitting_its_judge_heard_fire():
    """The plan's third falsifier clause. Controls: an empty slot names nothing; a dateless docket item
    is no sitting; a person off the bench, or a judge who never heard the date fire, is not asked; and
    once the determination takes the matter off the docket the question is gone."""
    w, d = _world()
    duke = w.persons[DUKE]
    did, cal = _sitting(w, d)
    heard, = [c for c in duke.ledger if c.predicate == "date.fired" and c.subject == VENUE]
    assert world_q.sittings_before(w, duke) == [], "an empty slot named a matter"
    # A dateless item for another matter: docketed, but before no sitting.
    w.docket.append({"date": None, "matter": "p_low", world_q.DOCKET_ARRANGEMENT: None,
                     world_q.DOCKET_PETITION: None})
    assert world_q.sittings_before(w, duke) == []
    assert _kinds(_fold(w, d, _open("oc"))) == ["case.opened"]
    got = world_q.sittings_before(w, duke)
    assert [(g[0], g[1].id, g[2]) for g in got] == [(did, heard.id, (PARTY,))], got
    q, = [q for q in world_q.questions_for(w, duke) if q.id == f"q:sitting:{did}"]
    assert (q.source, q.referents, q.about) == ("claim_landed", (PARTY,), heard.id), q
    assert set(q.referents) <= {i["matter"] for i in w.docket if i["date"] is not None}
    # Off the bench: the King stands outside the duchy and holds no judging seat.
    assert world_q.sittings_before(w, w.persons["p_king"]) == []
    # A judge who never heard the sitting fire is not asked.
    kept = list(duke.ledger)
    duke.ledger[:] = [c for c in kept if c.predicate != "date.fired"]
    assert world_q.sittings_before(w, duke) == []
    duke.ledger[:] = kept
    # Determined: off the docket, and the question with it.
    assert _kinds(_fold(w, d, _determine("dt"))) == ["matter.determined"]
    assert world_q.sittings_before(w, duke) == []
    assert not [q for q in world_q.questions_for(w, duke) if q.id.startswith("q:sitting:")]


# ======================================================================================
# THE STEP EXIT -- W26's proof, one seeded run
# ======================================================================================

def _w26_run():
    w, d = _world()
    duke = w.persons[DUKE]
    did = _convene(w, d)                                           # a convene by a seated holder
    cal = _next_season_calendar(w, d)                              # next season: it fires
    fired, = [e for e in cal if e.kind == "date.fired"]
    assert [e.kind for e in cal] == ["date.fired", "docket.formed"], _kinds(cal)
    assert w.docket == [{"date": did, "matter": None}], "the firing formed no docket slot"
    assert d.witness(mint_token(w, WriteClass.INTERIOR), cal) > 0
    assert any(c.predicate == "date.fired" for c in duke.ledger), "no date.fired claim reached a ledger"
    assert _kinds(_fold(w, d, _open("oc"))) == ["case.opened"]   # fills the slot
    assert w.docket == [{"date": did, "matter": PARTY, world_q.DOCKET_ARRANGEMENT: None,
                         world_q.DOCKET_PETITION: None}], "no `{'date': None}` item may be appended"
    # The bench member's COMPUTED question names the docketed party ...
    q, = [q for q in world_q.questions_for(w, duke) if PARTY in q.referents and q.id.startswith("q:sitting:")]
    # ... the person-side opening set forms the determination on it ...
    det, = [c for c in opening_set(duke, View(duke.id, [], w.fixtures.get("view_k"), q), q, w.fixtures)
            if c.verb == "determine"]
    assert det.subject == PARTY, det
    # ... released as DELIBERATE releases a scene (`loop/deliberate.py`: registered, act stamped) ...
    acts = []
    for sc in pack_scenes(duke, [det], 5, w.fixtures, lambda pid, verb, s: f"w26:{verb}:{s}", occasion=q):
        d.scenes[sc.id] = sc
        for a in sc.acts:
            a.scene = sc.id
            acts.append(a)
    out = _fold(w, d, *acts)
    done, = [e for e in out if e.kind == "matter.determined"]
    # ... and the determination's `causes[]` walk back to the date that raised it.
    assert _walks_to(w, done, fired.id), (done.causes, fired.id)
    assert world_q.docketed(w, PARTY) == []
    return w.content_hash()


def test_w26_a_convened_sitting_fires_takes_a_case_and_its_bench_determines_it():
    first = _w26_run()
    assert _w26_run() == first, "the same seeded run hashed differently"
