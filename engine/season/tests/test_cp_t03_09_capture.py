"""CP-T03-09 -- `capture`: TAKE A BEATEN MAN INTO A SEAT'S CUSTODY (`-08` AM-C-03; a named fold of `fight`).

`verb_table.yaml`'s `capture` row (eligibility `remit:dispatch`, `contests: "the body"`, `fight`'s typed cell) is fought
under `rosters.yaml: duel_terms` (`capture: yield`), which `seam/wrappers/combat.py::combat_input` writes into
`PersonalCombatInput.terms` (default the STRING `'death'`); `loop/effects_combat.py::_eff_capture` is `fight`'s wounds
plus ONE `detain` edge, captive -> the act's `via` seat, where the scene's `surrender` names the subject and
`may_warrant` and `_may_close_custody` both hold. The gate is unchanged.

  FALSIFIER: a seeded `capture` whose subject yields leaves him in `w.persons` with exactly one live `detain` to the
  actor's `via` seat, `person.captured` emitted, no `person.died`, and a `move` by the captive declined
  (`travel.blocked`). A `capture` by a seat granting no `dispatch`, or whose holder could not close the custody, or
  whose purview does not reach the captive, opens nothing; one across settlements is refused at the cell, before any
  fight; a scene with no yield reports `capture.refused`, not `contest.undecided`.
  MUTATION (run in `test_mutation_...`): route the yield to `remove_person` and the SAME predicate that passes on the
  shipped effect FAILS -- the captive is gone and no edge exists.
  CONTROLS: the `'death'` string default (a `None` would make `wrapper.fight` raise) and `fight`/`accept` building the
  record they always built; `_OPENERS_FROM_EFFECTS["detain"]` holds `arrest` and `capture` and NOT `fight` or `accept`;
  `duel_terms` is checked against the engine's tuple, never re-declared.
"""
from __future__ import annotations

import dataclasses
import random
from unittest import mock

import pytest

from ..data import verbs as VERBS
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import Step, WriteClass
from ..data.verbs import DUEL_TERMS_BY_VERB, KIND_VERB, VERB_TABLE, _OPENERS_FROM_EFFECTS
from ..gaps import Forbidden
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token, resolvable_verbs
from ..loop.effects_combat import _eff_kill
from ..loop.effects_shared import EFFECTS
from ..queries.inputs import PersonalCombatInput
from ..seam.contest import Resolution
from ..seam.wrappers import combat
from ..seam.wrappers._entry import entry_for
from ..state.carriers import Act, Office, Person, Rung, Tenure
from ..state.gate import Change, Subject, death_subjects
from ..loop import resolve as R

ACTOR, CAPTIVE = "p_low", "p_mid"          # tiny_world: both live at the hearth `Hh`, inside `S`, inside `D`
SEAT = "off_watch"
TRIES = 80                                 # act ids scanned for a scene the subject yields in


def _world(grants=("dispatch", "determine"), seat_rung="D", scope="D"):
    """`tiny_world` plus a seat (`off_watch`) the actor holds, granting `grants`, at `seat_rung`; the driver is built
    (the registrar fills the combat entry at construction) and one MATTER barrier run."""
    w = P.tiny_world()
    w.offices[SEAT] = Office(SEAT, "Watch", seat_rung, list(grants), scope_rung=scope, faction="Crown")
    w.add_tenure(Tenure("t_watch", ACTOR, SEAT, "hold", since=0))
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return w, d


def _run(w, d, *acts):
    """RESOLVE then ENCOUNTER (`the body` is fought at ENCOUNTER), logged as a season does."""
    depth = w.fixtures.get("contest_max_depth")
    w.step, w.frozen = Step.RESOLVE, False
    out = d.resolve(mint_token(w, WriteClass.ACTS), list(acts), depth)
    out = out + d.encounter(mint_token(w, WriteClass.ACTS), out, depth)
    w.log.extend(out)
    return out


def _fold_at(w, d, act, degree, result):
    """ONE contested act through the fold at a PINNED band and scene (`test_in12_arrest.py::_fold_at`'s shape)."""
    w.step, w.frozen = Step.RESOLVE, False
    out = R._fold(d, w, mint_token(w, WriteClass.ACTS), act, Resolution(degree, result))
    w.log.extend(out)
    return out


def _kinds(events):
    return [e.kind for e in events]


def _capture(i, subject=CAPTIVE, actor=ACTOR, via=SEAT):
    return Act(id=f"cap{i}", actor=actor, verb="capture", via=via, payload={"subject": subject})


def _detains(w, who=CAPTIVE):
    return [t for t in w.tenures if t.kind == "detain" and t.subject == who and t.live]


def _yielding_scene(**world_kw):
    """`(world, driver, events)` of the first scanned `capture` whose captive yielded and was taken. Asserts that one
    exists: a scan that found none would be a falsifier observing nothing."""
    for i in range(TRIES):
        w, d = _world(**world_kw)
        out = _run(w, d, _capture(i))
        if "person.captured" in _kinds(out):
            return w, d, out
    raise AssertionError(f"no scene in {TRIES} act ids ended in the captive's yield: the falsifier observed nothing")


def _assert_held(w, out):
    """THE FALSIFIER'S PREDICATE, shared by the shipped effect and its mutant: he stands, in custody to the actor's
    seat, once, the capture reported and no death."""
    assert CAPTIVE in w.persons, "the captive left w.persons"
    held = _detains(w)
    assert len(held) == 1 and held[0].object == SEAT, [(t.id, t.object) for t in _detains(w)]
    assert "person.captured" in _kinds(out) and "person.died" not in _kinds(out), _kinds(out)


# ---------------------------------------------------------------------------------------------------------------
# 1 -- THE ROW, THE ROSTER, THE OPENER'S CREDIT, THE KIND
# ---------------------------------------------------------------------------------------------------------------

def test_the_row_is_arrests_eligibility_fights_prize_and_fights_typed_cell():
    row, fight = VERB_TABLE["capture"], VERB_TABLE["fight"]
    assert row.eligibility == ("remit:dispatch",) == VERB_TABLE["arrest"].eligibility
    assert row.contests == "the body" == fight.contests
    assert row.requires_typed == fight.requires_typed, "the typed cell is fight's: subject exists, with, individual x2"
    assert set(row.requires_typed.stems()) == {"exists", "with", "individual"}
    assert row.emits_on_refusal == ("capture.refused",)
    assert "capture" in resolvable_verbs()


def test_the_opener_is_credited_to_capture_and_not_to_the_fights_it_shares_wounds_with():
    openers = _OPENERS_FROM_EFFECTS["detain"]
    assert {"arrest", "capture"} <= set(openers), openers
    assert "fight" not in openers and "accept" not in openers, openers


def test_person_captured_has_one_emitter_and_it_is_mapped():
    assert KIND_VERB["person.captured"] == "capture"
    assert [v for v, r in VERB_TABLE.items() if "person.captured" in r.emits] == ["capture"]


def test_duel_terms_names_capture_and_accept_and_is_checked_against_the_engines_tuple_not_redeclared():
    assert DUEL_TERMS_BY_VERB == {"capture": "yield", "accept": "blood"}     # v11 CR-87 added `accept: blood`
    engine = combat.engine()
    assert engine is not None, "the combat engine did not load"
    wrapper = engine[0]
    assert all(t in wrapper.DUEL_TERMS for t in DUEL_TERMS_BY_VERB.values())
    w, _ = _world()
    with mock.patch.dict(DUEL_TERMS_BY_VERB, {"capture": "mercy"}):          # a term the engine does not name
        with pytest.raises(Forbidden) as e:
            combat.combat_input(w, [ACTOR, CAPTIVE], "capture")
    assert "duel_terms" in str(e.value) and "mercy" in str(e.value)
    # and the loader refuses a line for a verb the table lacks (the shape half, which needs no engine)
    with pytest.raises(Forbidden):
        VERBS._check_duel_terms({"no_such_verb": "yield"}, VERB_TABLE)
    with pytest.raises(Forbidden):
        VERBS._check_duel_terms({"capture": ""}, VERB_TABLE)
    assert VERBS._check_duel_terms({"capture": "yield"}, VERB_TABLE) == {"capture": "yield"}


# ---------------------------------------------------------------------------------------------------------------
# 2 -- `terms`: THE STRING DEFAULT IS THE CONTROL, AND THE ONE PATH
# ---------------------------------------------------------------------------------------------------------------

def test_the_default_terms_is_the_string_death_and_a_none_default_would_raise():
    wrapper = combat.engine()[0]
    inp = PersonalCombatInput(claimants=(ACTOR, CAPTIVE), ends=(4, 4), wound_quantities=("felled", "wounds"))
    assert inp.terms == "death" == wrapper.LETHAL_TERMS and isinstance(inp.terms, str)
    w, _ = _world()
    entry, refusal = entry_for("the body", combat.PROVIDER)
    assert entry is not None, refusal
    lethal = entry.fn(combat.combat_input(w, [ACTOR, CAPTIVE], "fight"), random.Random(5))
    assert lethal["status"] == "RESOLVED"
    with pytest.raises(ValueError):                         # CONTROL: the `None` default the string replaces
        entry.fn(dataclasses.replace(combat.combat_input(w, [ACTOR, CAPTIVE], "fight"), terms=None),
                 random.Random(5))


def test_combat_input_fills_terms_from_the_roster_by_verb_and_nothing_else_does():
    w, _ = _world()
    got = {v: combat.combat_input(w, [ACTOR, CAPTIVE], v).terms for v in ("fight", "accept", "capture")}
    assert got == {"fight": "death", "accept": "blood", "capture": "yield"}, got    # `accept`: v11 CR-87
    assert combat.duel_terms_of("fight") is None and combat.duel_terms_of("capture") == "yield"


def test_the_sampler_is_called_with_the_same_terms():
    """`fight_estimate` for `capture` samples under `yield` -- a yield exists in its shares -- and for `fight` under
    `death`, where no yield can occur; both on the one `combat_input`, so there is no second `terms` path."""
    w, _ = _world()
    cap = combat.fight_estimate(w, ACTOR, SEAT, CAPTIVE, "capture")
    fgt = combat.fight_estimate(w, ACTOR, SEAT, CAPTIVE, "fight")
    assert cap["status"] == fgt["status"] == "ESTIMATED"
    assert cap["yielded"] > 0.0, cap
    assert fgt["yielded"] == 0.0, fgt
    h = w.content_hash()
    combat.fight_estimate(w, ACTOR, SEAT, CAPTIVE, "capture")
    assert w.content_hash() == h, "the sampler consumed a draw"


# ---------------------------------------------------------------------------------------------------------------
# 3 -- THE FALSIFIER
# ---------------------------------------------------------------------------------------------------------------

def test_a_capture_whose_subject_yields_holds_him_in_the_actors_seat_and_a_move_is_declined():
    w, d, out = _yielding_scene()
    _assert_held(w, out)
    edge = _detains(w)[0]
    assert edge.subject == CAPTIVE and edge.object == SEAT and edge.since == w.tick
    assert w.persons[ACTOR].body > 0 and ACTOR in w.persons
    move = Act(id="mv", actor=CAPTIVE, verb="move", payload={"to": "S"})
    assert _kinds(_run(w, d, move)) == ["travel.blocked"], "the captive was free to travel"
    assert len(_detains(w)) == 1


def test_mutation_routing_the_yield_to_remove_person_fails_the_same_predicate():
    """The mutant is `_eff_capture` with the yield sent to the grave. The control (the shipped effect) passes
    `_assert_held` above; the mutant must FAIL it, or the predicate observes nothing."""
    def mutant(w, a, res=None):
        base = _eff_kill(w, a, res)
        who = a.payload["subject"]
        yielded = res.result.get("surrender")
        if yielded is None or yielded.get("by") != who or who not in w.persons:
            return base

        def perform():
            base.apply()
            w.persons[who].body = 0
            w.remove_person(who)
        return Change(base.subjects + death_subjects(w, who, (), fields=("body",)), perform)

    with mock.patch.dict(EFFECTS, {"capture": mutant}):
        w, d, out = None, None, None
        for i in range(TRIES):
            w, d = _world()
            out = _run(w, d, _capture(i))
            if CAPTIVE not in w.persons and ACTOR in w.persons:
                break
        else:
            raise AssertionError("the mutant never removed a yielder: it observed nothing")
        with pytest.raises(AssertionError):
            _assert_held(w, out)


def test_a_seat_that_could_not_close_the_custody_opens_nothing():
    """`dispatch` without `determine`: the act is admitted (the eligibility reads `dispatch`) and the captive is
    fought and wounded as in `fight`, but no custody nothing could release is opened."""
    fought = 0
    for i in range(TRIES):
        w, d = _world(grants=("dispatch",))
        out = _run(w, d, _capture(i))
        assert "capture.declared" in _kinds(out) and not _detains(w), (i, _kinds(out))
        assert "person.captured" not in _kinds(out), _kinds(out)
        fought += "body.changed" in _kinds(out)
    assert fought >= 1, "no scene wounded anybody: the control observed nothing"


def test_a_seat_granting_no_dispatch_is_refused_before_any_fight():
    w, d = _world(grants=("determine",))
    out = _run(w, d, _capture(0))
    assert _kinds(out) == ["capture.refused"] and not _detains(w), _kinds(out)
    assert w.persons[CAPTIVE].body == P.tiny_world().persons[CAPTIVE].body


def test_a_seat_whose_purview_does_not_reach_the_captive_opens_nothing():
    """The second settlement's seat: it grants both acts, but its ground is `S2`, not the hearth the captive stands in."""
    opened = 0
    for i in range(TRIES):
        w = P.tiny_world()
        w.rungs["S2"] = Rung("S2", "settlement", stores={"grain": 40})
        w.add_tenure(Tenure("t_s2", "S2", "D", "contain", since=0))
        w.offices[SEAT] = Office(SEAT, "Watch", "S2", ["dispatch", "determine"], scope_rung="S2", faction="Crown")
        w.add_tenure(Tenure("t_watch", ACTOR, SEAT, "hold", since=0))
        d = SeasonDriver(w)
        d.matter(mint_token(w, WriteClass.MATTER), [])
        out = _run(w, d, _capture(i))
        opened += bool(_detains(w))
        assert "person.captured" not in _kinds(out), _kinds(out)
    assert opened == 0


def test_a_capture_across_settlements_is_refused_at_the_cell():
    w, d = _world()
    w.rungs["S2"] = Rung("S2", "settlement", stores={"grain": 40})
    w.add_tenure(Tenure("t_s2", "S2", "D", "contain", since=0))
    w.persons["p_far"] = Person("p_far", "a stranger from afar")
    w.rungs["p_far"] = Rung("p_far", "person")
    w.add_tenure(Tenure("t_far", "p_far", "S2", "contain", since=0))
    out = _run(w, d, _capture(0, subject="p_far"))
    assert _kinds(out) == ["capture.refused"] and not _detains(w, "p_far"), _kinds(out)
    assert "p_far" in w.persons


def test_a_cohort_is_never_captured():
    w, d = _world()
    P.plant_cohort(w, "c_crowd", "Hh", weight=3)
    out = _run(w, d, _capture(0, subject="c_crowd"))
    assert _kinds(out) == ["capture.refused"] and not _detains(w, "c_crowd")


# ---------------------------------------------------------------------------------------------------------------
# 4 -- THE EFFECT'S OWN CLAUSES, ON PINNED SCENES (no dice)
# ---------------------------------------------------------------------------------------------------------------

def _state(wounds, health, full=10, felled=False):
    return dict(available=True, felled=felled, wounds=wounds, max_wounds=4, health_remaining=health, health_full=full)


def _scene(actor=None, captive=None, surrender=None):
    return dict(status="RESOLVED", wound_state={ACTOR: actor or _state(0, 10), CAPTIVE: captive or _state(0, 10)},
                surrender=surrender)


def test_a_scene_with_no_yield_and_no_wound_is_capture_refused_not_contest_undecided():
    w, d = _world()
    out = _fold_at(w, d, _capture(0), "Untouched", _scene())
    assert _kinds(out) == ["capture.refused"] and not _detains(w), _kinds(out)
    assert "contest.undecided" not in _kinds(out)


def test_a_wounded_scene_with_no_yield_wounds_and_reports_no_capture():
    w, d = _world()
    out = _fold_at(w, d, _capture(0), "Wounded", _scene(captive=_state(1, 6)))
    assert _kinds(out) == ["body.changed"] and not _detains(w), _kinds(out)


def test_a_yield_by_the_captive_opens_one_detain_and_earns_person_captured_alone_on_the_edge():
    w, d = _world()
    surrender = dict(by=CAPTIVE, turn=3, accepted=True)
    out = _fold_at(w, d, _capture(0), "Wounded", _scene(captive=_state(1, 3), surrender=surrender))
    assert sorted(_kinds(out)) == ["body.changed", "person.captured"], _kinds(out)
    _assert_held(w, out)
    # the body event does not carry the edge, nor the capture event the wound: each kind its own earners' changes
    by_kind = {e.kind: e for e in out}
    assert len(by_kind["person.captured"].changes) >= 1 and len(by_kind["body.changed"].changes) >= 1
    # a second capture of a man already in custody opens no second edge (one live detain per prisoner)
    out2 = _fold_at(w, d, _capture(1), "Untouched", _scene(surrender=surrender))
    assert len(_detains(w)) == 1 and "person.captured" not in _kinds(out2), _kinds(out2)


def test_a_clean_yield_runs_the_effect_because_untouched_declares_tenure_since():
    w, d = _world()
    out = _fold_at(w, d, _capture(0), "Untouched", _scene(surrender=dict(by=CAPTIVE, turn=1, accepted=True)))
    assert _kinds(out) == ["person.captured"], _kinds(out)
    _assert_held(w, out)


def test_a_yield_by_the_actor_opens_nothing():
    w, d = _world()
    out = _fold_at(w, d, _capture(0), "Untouched", _scene(surrender=dict(by=ACTOR, turn=1, accepted=True)))
    assert _kinds(out) == ["capture.refused"] and not _detains(w) and not _detains(w, ACTOR), _kinds(out)


def test_a_scene_in_which_a_party_was_felled_opens_nothing():
    w, d = _world()
    surrender = dict(by=CAPTIVE, turn=2, accepted=True)
    out = _fold_at(w, d, _capture(0), "Felled", _scene(actor=_state(4, 0, felled=True), surrender=surrender))
    assert not _detains(w) and "person.captured" not in _kinds(out), _kinds(out)
