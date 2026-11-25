"""CR-72 -- EXECUTION (XE): DOES `fight` FORM AGAINST A HELD PARTY? (`strife-00` §9, open item (i); a MEASURE: no code
changed, hash EQUAL.)

A hand-built world in which the holder of a custody seat and the party that seat holds are CO-LOCATED, built twice -- the
`detain` written by `arrest` (`loop/effects_information.py`, IN-12; the Duke issues a warrant, a watchman serves it, the
edge runs prisoner -> `off_duke`) and by `capture` (`loop/effects_combat.py::_eff_capture`, CP-T03-09; the edge runs
captive -> the capturer's `via` seat, `off_watch`). Per route, as built:

  (a) FORMATION. `opening_set` forms `fight` for the holder on the held man. Under CR-87 a held party is context (ii),
      CRIME: `decision/options.py::_crime_context` reads a warrant ADDRESSED to the actor naming him, or the subject
      stamped `Detainee` on the question (`world_q.detainees_held`: a live `detain` on a seat the actor holds that
      grants a `determine`). `violence_context_of` names the context that carried it: `crime` on both routes, and on
      both it is the `Detainee` stamp -- the Duke MADE his warrant, he is not its addressee, and the capturer holds none.
      CONTROL: close the `detain` (a release) and the same actor, world and question form no `fight` on him.
  (b) ADMISSION. The formed act, packed by `pack_scenes` and folded through `SeasonDriver.resolve`, is admitted:
      `fight.declared`, and not `kill.refused` (the row's one refusal kind; the access gate's `with` conjunct wants the
      attacker where his target is). CONTROL, so that the read can see a refusal at all: the arrest-route Duke stands at
      `S`, the prisoner at the hearth `Hh` inside it, and the same act from there IS `kill.refused` -- co-location is what
      the fixture arranges (`_colocate`), not something the held state supplies.
      The encounter then ran the fight to a death at every one of 60 act ids tried, and either party was the one who died.

  FORMATION ALSO WANTS KNOWLEDGE. `fight`'s referents are the persons the actor knows of; the arrest world plants the Duke's
  (`test_in12_arrest._world`) and `_capture_route` plants the capturer's the same way, because the hand-built capture scene
  leaves his ledger empty and `fight` then forms on nobody for him (MEASURED, not asserted) although `Detainee` is stamped
  and `interrogate` forms. In a realm it is WITNESS's deposit; this file does not run that pass.

  THE RESTRAINT OF THE HELD PARTY DOES NOT ENTER THE ADMISSION. Nothing in `fight`'s cells or the fold reads a `detain` on
  the subject: `world_q.restrained(...)` is read at `move` (`travel.blocked`), a march's attacking side
  (`loop/sides.py`), and the one-live-detain clauses of `arrest` and `capture`; no read sits on `fight`'s path (grep of its
  call sites, as built). So a restrained man is a legal target, and (a) answers YES on both routes.

  NOT SAID BY THIS FILE, AND MEASURED WHEN IT WAS WRITTEN (recorded, never asserted: an assertion would be a guard on an
  absence, `CLAUDE.md` §0.1 pt 5). A death the REAL fold wrote (`_run` over a `fight` by the Duke on the prisoner, 60 act
  ids) and the real `harness/strife.py::readers_for(w).victim_held` read over it:
    * the real `person.died` carries its change on field `body` (`state/gate.py::death_subjects(..., fields=("body",))`);
      `victim_held` collected only changes with field `exists` and so named NO victim of a real death, until B12a.68
      made it read `body` too (`test_a_hand_built_execution_reads_xe`);
    * a dead man's own edges are gone from `w.tenures` after `World.remove_person`, so the `detain` the reader would
      test is no longer there to be found when it is asked after the run (the way `measure` asks it).
  Either one alone reads a held man's real death as KL, never XE. The owner of both is `harness/strife.py` (the reader)
  and `World.remove_person` (the cascade); nothing here edits either.

  XE stays a named residue of the INSTRUMENT, not of formation: `fight` forms and is admitted against a held party.
"""
from __future__ import annotations

from types import SimpleNamespace

import pytest

from ..data.rosters import DETAIN_KIND
from ..harness.strife import Readers, classify, readers_for
from ..state.carriers import Event, StateChange, Tenure
from ..data.verbs import VIOLENCE_CONTEXTS
from ..decision import options as O
from ..decision.options import opening_set, violence_context_of
from ..loop.driver import mint_token
from ..queries import world_q
from ..state.carriers import Claim, Question
from ..data.matrix import Step, WriteClass
from .test_cp_t03_09_capture import ACTOR as CAPTOR, CAPTIVE, _world as _capture_world, _yielding_scene
from .test_in10_record_operands import _acts, _formed
from .test_in12_arrest import DUKE, PRISONER, WATCH, WATCHMAN, _act, _fold_at, _warrant_to_watchman
from .test_in12_arrest import _world as _arrest_world
from ._seat_at_success import writ_at_success  # noqa: F401  (the fixture; its reason is in its module)

pytestmark = pytest.mark.usefixtures("writ_at_success")   # B21.56: the arrest world's warrant is issued at Success; this file's question is `fight` on a held party, not `issue`'s draw

HEARTH = "Hh"          # `tiny_world`: where the prisoner / captive lives, inside the settlement `S` where the Duke stands


def _colocate(w, who, place=HEARTH):
    """Stand `who` where the held man stands: re-point his `contain` and `reside` edges at `place`."""
    moved = 0
    for t in w.tenures:
        if t.subject == who and t.kind in ("contain", "reside") and t.live:
            t.object, moved = place, moved + 1
    assert moved == 2, moved


def _arrest_route(colocated=True):
    """`(w, d, holder, victim)`: the Duke's warrant served by the watchman at a pinned winning band -> `detain`
    prisoner -> `off_duke`; the Duke (holder of that seat) standing at the prisoner's hearth when `colocated`."""
    w, d = _arrest_world()
    _warrant_to_watchman(w, d)
    out = _fold_at(w, d, "Success", _act("a1", "arrest", WATCHMAN, WATCH, subject=PRISONER))
    assert [e.kind for e in out] == ["arrest.made"], [e.kind for e in out]
    if colocated:
        _colocate(w, DUKE)
    return w, d, DUKE, PRISONER


def _capture_route():
    """`(w, d, holder, victim)`: the first scanned `capture` whose captive yielded -> `detain` captive -> `off_watch`;
    the capturer holds that seat and both live at the hearth."""
    w, d, out = _yielding_scene()
    assert "person.captured" in [e.kind for e in out]
    # KNOWLEDGE, PLANTED AS `test_in12_arrest._world` PLANTS THE DUKE'S: `fight`'s referents are the persons he knows of
    # (`exists:Person` in his ledger), and the capture scene deposits none in a hand-built world (the capturer's ledger
    # is empty after it; a realm's WITNESS pass deposits the sighting). Without it `fight` forms on NOBODY for him, the
    # `Detainee` stamp notwithstanding -- the stamp narrows a formation, it does not supply the knowledge.
    w.persons[CAPTOR].ledger.append(Claim("c_knows_captive", CAPTOR, CAPTIVE, "exists:Person", 1, 0,
                                          "firsthand", 100, "own"))
    return w, d, CAPTOR, CAPTIVE


ROUTES = {"arrest": _arrest_route, "capture": _capture_route}


def _custody(w, victim):
    return [t for t in w.tenures if t.kind == "detain" and t.subject == victim and t.live]


def _question(w, holder) -> Question:
    qs = world_q.questions_for(w, w.persons[holder])
    assert qs, "the holder answers no question: formation would read nothing"
    return qs[0]


def _fights(w, holder, victim) -> list:
    return [c for c in _formed(w, holder, _question(w, holder)) if c.verb == "fight" and c.subject == victim]


def _context(w, holder, victim):
    p = w.persons[holder]
    return violence_context_of(p, _question(w, holder), victim, VIOLENCE_CONTEXTS["fight"], O.held_record_claims(p))


def _fold_fight(w, d, holder, victim):
    """The formed `fight`, packed as a season packs it, RESOLVE then ENCOUNTER (`test_cp_t03_09_capture._run`'s order)."""
    (act,) = [a for a in _acts(w, holder, _fights(w, holder, victim)) if a.verb == "fight"]
    depth = w.fixtures.get("contest_max_depth")
    w.step, w.frozen = Step.RESOLVE, False
    out = d.resolve(mint_token(w, WriteClass.ACTS), [act], depth)
    out = out + d.encounter(mint_token(w, WriteClass.ACTS), out, depth)
    w.log.extend(out)
    return act, [e.kind for e in out]


# ---------------------------------------------------------------------------------------------------------------
# (a) -- FORMATION AND ADMISSION, BOTH ROUTES
# ---------------------------------------------------------------------------------------------------------------

@pytest.mark.parametrize("route", sorted(ROUTES))
def test_fight_forms_for_the_holder_on_a_held_party_as_crime_and_the_fold_admits_it(route):
    w, d, holder, victim = ROUTES[route]()
    assert len(_custody(w, victim)) == 1, "the route left no live detain: the measure would read a free man"
    cands = _fights(w, holder, victim)
    assert cands, f"{route}: `fight` did not form for {holder} on the held {victim}"
    assert _context(w, holder, victim) == "crime"
    assert (victim, "Detainee") in _question(w, holder).classes
    act, kinds = _fold_fight(w, d, holder, victim)
    assert "fight.declared" in kinds and "kill.refused" not in kinds, (route, kinds)


@pytest.mark.parametrize("route", sorted(ROUTES))
def test_control_the_release_of_the_detain_withdraws_the_formation(route):
    """The same actor, world and question with the `detain` closed: the held state is what carried the formation."""
    w, d, holder, victim = ROUTES[route]()
    assert _fights(w, holder, victim), "CONTROL: formed while held"
    for t in _custody(w, victim):
        t.until = w.tick
    assert not _custody(w, victim)
    assert _context(w, holder, victim) is None
    assert not _fights(w, holder, victim)


def test_control_the_admission_read_sees_a_refusal_when_the_holder_stands_elsewhere():
    """The Duke at `S`, the prisoner at the hearth inside it: the formation (a) is unchanged (a person-side read that
    never sees a location, `with` being WORLD-ONLY) and the fold refuses with the row's one kind."""
    w, d, holder, victim = _arrest_route(colocated=False)
    assert _fights(w, holder, victim)
    act, kinds = _fold_fight(w, d, holder, victim)
    assert "kill.refused" in kinds and "fight.declared" not in kinds, kinds


# ---------------------------------------------------------------------------------------------------------------
# (c) -- THE READER: a hand-built execution reads XE (B12a.68, H-257)
# ---------------------------------------------------------------------------------------------------------------

def _death(changed_field):
    """A `person.died` Event at tick 9 whose one change, on `changed_field`, names `PRISONER`."""
    return Event("e_death", "person.died", [StateChange(PRISONER, "set", "Act", changed_field)], ["a_fight"], 9)


def _held_world(since=3, until=None, subject=PRISONER):
    return SimpleNamespace(tenures=[Tenure("t_detain", subject, DUKE, DETAIN_KIND, since, until)])


@pytest.mark.parametrize("changed_field", ["body", "exists"])
def test_a_hand_built_execution_reads_xe(changed_field):
    """The real death's change is on `body`; the held man's `detain` is live at the tick. The read names him a victim
    and `classify` reads the fight-caused death as XE, not KL. CONTROLS: the `detain` closed a tick before the death,
    and a `detain` on another man, both read KL, so the read can see a refusal."""
    e = _death(changed_field)
    fight = lambda w: Readers(lambda _: "fight", lambda _: None, readers_for(w).victim_held)
    w = _held_world()
    assert readers_for(w).victim_held(e) is True
    assert [c for c, _ in classify(e, fight(w))] == ["XE"]
    for free in (_held_world(until=8), _held_world(subject="someone_else")):
        assert readers_for(free).victim_held(e) is False
        assert [c for c, _ in classify(e, fight(free))] == ["KL"]
