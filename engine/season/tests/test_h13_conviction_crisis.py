"""IN-08 `12e` H13 (`workplans/valoria_master_workplan_v9_part5.md`, *"crisis threshold 3 on G-Q6, as
the affiliation draft recommends"*) -- the crisis at scar threshold 3, the first writer of
`(Person, conviction)`.

The selector is `queries/person_q.py::conviction_after_crisis` (fold along `incompatible`; restabilise
not built; destroyed when nothing else is held) and the write is `loop/resolve.py::_conviction_crisis`,
called after the act's scar write. THE SHIPPED REALM CANNOT SHOW IT: no cast row holds an affiliation
(H10), so every `Person.conviction` is `{}` and nothing can be scarred on one. The falsifier runs on
H11's PLANTED world (`probes.tiny_world`, holdings given, the loaded engagement table rebound so
`fight` -- which lands there -- violates every holding), with the scar count planted one short of the
threshold, and every positive arm has a control:
  * planted one count lower (the act takes it to 2) -> `conviction` unwritten;
  * at the threshold on a held affiliation -> it folds into the incompatible co-holding, observers
    only; a person who did not observe the act, planted at the same count, is not touched;
  * a `Failure` band rebound to violate the holding -> no write, while a landed act in the same world
    writes;
  * WITNESS's token -> refused at the row (S9.3), through H13's own writer.
Affiliation names are derived from the loaded relation, never typed.
"""
from __future__ import annotations

import pytest

from engine.season.data import affiliations as A
from engine.season.data.matrix import Step, WriteClass, matrix_row
from engine.season.data.rosters import AFFILIATIONS, WOUNDED
from engine.season.epistemic import observers_for
from engine.season.gaps import Forbidden
from engine.season.harness import probes as P
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.loop.resolve import _conviction_crisis
from engine.season.queries.person_q import (SCAR_CRISIS_AT, conviction_after_crisis, said_of,
                                            violated_affiliations)
from engine.season.seam import Resolution
from engine.season.state.carriers import Act, Claim, Person, Tenure
from engine.substrate.descriptors import AFFILIATION_CEILING


def _pairs():
    return sorted(tuple(sorted(p)) for p in A.INCOMPATIBLE)


def _hub():
    """The affiliation in the most incompatible pairs, ties to the first by name, and its partners."""
    count = {a: sum(a in p for p in _pairs()) for a in sorted(AFFILIATIONS)}
    hub = max(sorted(count), key=lambda a: count[a])
    return hub, sorted(b for p in _pairs() if hub in p for b in p if b != hub)


def _compatible_pair():
    for a in sorted(AFFILIATIONS):
        for b in sorted(AFFILIATIONS):
            if a < b and frozenset((a, b)) not in A.INCOMPATIBLE:
                return a, b
    pytest.skip("every rostered pair is incompatible; restabilise has no case to read")


def _person(held, scar):
    return Person(id="h13", conviction=A.conviction_map(held), scar=dict(scar))


# --------------------------------------------------------------------------- the selector, person-side

def test_h13_below_the_threshold_the_vector_is_returned_untouched():
    hub, (y, *_r) = _hub()
    p = _person(dict([(hub, 3), (y, 2)]), {hub: SCAR_CRISIS_AT - 1, y: SCAR_CRISIS_AT - 1})
    assert conviction_after_crisis(p) is p.conviction


def test_h13_fold_transfers_the_intensity_to_the_incompatible_co_holding():
    hub, (y, *_r) = _hub()
    p = _person(dict([(hub, 3), (y, 1)]), {hub: SCAR_CRISIS_AT})
    assert conviction_after_crisis(p) == {y: 4}
    clamp = _person(dict([(hub, AFFILIATION_CEILING), (y, AFFILIATION_CEILING)]), {hub: 4})
    assert conviction_after_crisis(clamp) == {y: AFFILIATION_CEILING}


def test_h13_fold_target_is_the_highest_held_heir_ties_to_the_first_by_name():
    hub, heirs = _hub()
    if len(heirs) < 2:
        pytest.skip("the hub has one incompatible partner; no target choice to test")
    first, second = heirs[0], heirs[1]
    higher = _person(dict([(hub, 2), (first, 1), (second, 3)]), {hub: SCAR_CRISIS_AT})
    assert conviction_after_crisis(higher) == A.conviction_map(dict([(first, 1), (second, 5)]))
    tie = _person(dict([(hub, 2), (first, 1), (second, 1)]), {hub: SCAR_CRISIS_AT})
    assert conviction_after_crisis(tie) == A.conviction_map(dict([(first, 3), (second, 1)]))


def test_h13_restabilise_is_not_built_and_destroyed_leaves_the_zero_vector():
    a, b = _compatible_pair()
    both = _person(dict([(a, 3), (b, 2)]), {a: SCAR_CRISIS_AT})
    assert conviction_after_crisis(both) == both.conviction, "restabilise wrote; it is not built"
    alone = _person({a: 3}, {a: SCAR_CRISIS_AT})
    assert conviction_after_crisis(alone) == {}


def test_h13_one_crisis_at_a_time_the_highest_held_folds_into_the_lower():
    """Two incompatible holdings at the threshold together (what the shared column produces): ONE
    crisis is taken, the higher-held's, so the direction follows intensity both ways; the heir,
    still at the threshold and now held alone, breaks at its own next crisis."""
    hub, (y, *_r) = _hub()
    both = {hub: SCAR_CRISIS_AT, y: SCAR_CRISIS_AT}
    assert conviction_after_crisis(_person(dict([(hub, 3), (y, 1)]), both)) == {y: 4}
    assert conviction_after_crisis(_person(dict([(hub, 1), (y, 3)]), both)) == {hub: 4}
    tie = conviction_after_crisis(_person(dict([(hub, 2), (y, 2)]), both))
    first, second = sorted((hub, y))
    assert tie == {second: 4}, f"a tie is taken by name: {first} folds, got {tie}"
    assert conviction_after_crisis(_person({y: 4}, both)) == {}


# ---------------------------------------------------------------------------- the falsifier, planted

def _rebound(**cells):
    out = {col: dict(row) for col, row in A.ENGAGEMENT.items()}
    for col, row in cells.items():
        out.setdefault(col, {}).update(row)
    return out


def _world(holdings, count, mode="presence_only"):
    """H11's planted world: one `knot` ties `p_low` to `p_high`, who stands away from the act; no
    pursuits held; `holdings` on every person, each holding planted at scar `count`."""
    w = P.tiny_world()
    for p in w.persons.values():
        p.pursuits = {}
        p.conviction = A.conviction_map(holdings)
        p.scar = {a: count for a in sorted(p.conviction)}
    w.add_tenure(Tenure("t_h13_knot", "p_low", "p_high", "knot", since=0))
    w.fixtures = w.fixtures.sweep("fan_out_mode", mode)
    w.step = Step.RESOLVE
    return w


def _fight(w, aid="h13_fight"):
    res = Resolution(WOUNDED, {"wound_state": {"p_mid": {"health_full": 10,
                                                         "health_remaining": 5}}})
    return SeasonDriver(w)._fold(w, mint_token(w, WriteClass.ACTS),
                                 Act(id=aid, actor="p_low", verb="fight",
                                     payload={"subject": "p_mid"}), res)


def test_h13_an_observed_violation_at_the_threshold_folds_each_observer_only(monkeypatch):
    hub, (y, *_r) = _hub()
    holdings = dict([(hub, 3), (y, 1)])
    monkeypatch.setattr(A, "ENGAGEMENT", _rebound(**{A.SHARED_COLUMN: {"fight": -0.3}}))

    control = _world(holdings, SCAR_CRISIS_AT - 2)
    _fight(control)
    assert any(p.scar.get(hub) == SCAR_CRISIS_AT - 1 for p in control.persons.values()), \
        "the control's act scarred nobody, so its unwritten conviction proves nothing"
    assert all(p.conviction == holdings for p in control.persons.values()), "written below 3"

    w = _world(holdings, SCAR_CRISIS_AT - 1)
    events = _fight(w)
    w.discard_caches()
    seen = {pid for e in events for pid, _ch in observers_for(w, e, "presence_only",
                                                              list(w.persons))}
    unseen = set(w.persons) - seen
    assert seen and unseen, (seen, unseen)
    for pid in seen:
        p = w.persons[pid]
        assert violated_affiliations(Person(id="x", conviction=holdings), "fight")
        assert p.scar.get(hub) == SCAR_CRISIS_AT, (pid, p.scar)
        assert p.conviction == {y: 4}, (pid, p.conviction)
    for pid in unseen:
        assert w.persons[pid].conviction == holdings, (pid, w.persons[pid].conviction)


def test_h13_a_failure_band_reaches_no_crisis(monkeypatch):
    from engine.dice_engine.dice_engine import DEGREE_LABEL, Degree
    failure = DEGREE_LABEL[Degree.FAILURE]
    hub, (y, *_r) = _hub()
    holdings = dict([(hub, 3), (y, 1)])
    monkeypatch.setattr(A, "ENGAGEMENT",
                        _rebound(**{A.SHARED_COLUMN: {"tell": -0.3, "fight": -0.3}}))
    w = _world(holdings, SCAR_CRISIS_AT - 1, mode="all_five")
    w.persons["p_low"].ledger.append(
        Claim("c_h13", "p_low", "Hh", "stores:grain", 8, 0, "firsthand", 37, "own"))
    tell = Act(id="h13_tell", actor="p_low", verb="tell",
               payload={"subject": "Hh", "to": "p_mid",
                        "said": said_of(w.persons["p_low"].ledger, "Hh", w.fixtures)})
    evs = SeasonDriver(w)._fold(w, mint_token(w, WriteClass.ACTS), tell, Resolution(failure, {}))
    assert [e.degree for e in evs] == [failure], [(e.kind, e.degree) for e in evs]
    assert all(p.conviction == holdings for p in w.persons.values()), "a Failure band wrote"
    _fight(w)
    assert any(p.conviction != holdings for p in w.persons.values()), \
        "a landed fight in the same world reached no crisis, so the arm above proves nothing"


def test_h13_a_pursuit_only_scar_reaches_no_crisis(monkeypatch):
    """A crisis follows an AFFILIATION's count moving. A person already at the threshold on a held
    affiliation who is scarred on a PURSUIT alone (the shipped engagement table leaves `fight`
    uncelled, so no holding is violated) keeps the vector; the control is the same world with
    `fight` rebound to violate the holding, which folds as before."""
    from engine.season.data.rosters import PURSUITS
    hub, (y, *_r) = _hub()
    holdings = dict([(hub, 3), (y, 1)])

    def world():
        w = _world(holdings, SCAR_CRISIS_AT)
        for p in w.persons.values():
            p.pursuits = {e: 0.5 for e in PURSUITS}
        return w

    w = world()
    assert not violated_affiliations(w.persons["p_mid"], "fight"), \
        "the shipped table violates the holding, so this arm is not pursuit-only"
    before = {pid: dict(p.scar) for pid, p in w.persons.items()}
    _fight(w)
    pursuit_scarred = [pid for pid, p in w.persons.items()
                       if p.scar != before[pid] and p.scar.get(hub) == SCAR_CRISIS_AT]
    assert pursuit_scarred, "the act scarred nobody on a pursuit, so the unmoved vector proves nothing"
    for pid in pursuit_scarred:
        assert w.persons[pid].conviction == holdings, (pid, w.persons[pid].conviction)

    monkeypatch.setattr(A, "ENGAGEMENT", _rebound(**{A.SHARED_COLUMN: {"fight": -0.3}}))
    control = world()
    _fight(control)
    assert any(control.persons[pid].conviction == {y: 4} for pid in pursuit_scarred), \
        "the affiliation-scarred control did not fold, so the arm above proves nothing"


def test_h13_witness_token_is_refused_and_encounter_is_admitted():
    hub, (y, *_r) = _hub()
    w = _world(dict([(hub, 3), (y, 1)]), SCAR_CRISIS_AT)
    act = Act(id="h13_direct", actor="p_low", verb="fight", payload={})
    w.step = Step.WITNESS
    with pytest.raises(Forbidden) as exc:
        _conviction_crisis(w, mint_token(w, WriteClass.INTERIOR), act, ["p_mid"])
    assert exc.value.where == "S9.3", exc.value.where
    assert w.persons["p_mid"].conviction == dict([(hub, 3), (y, 1)])
    assert Step.ENCOUNTER in matrix_row("Person", "conviction").steps
    w.step = Step.ENCOUNTER
    _conviction_crisis(w, mint_token(w, WriteClass.ACTS), act, ["p_mid"])
    assert w.persons["p_mid"].conviction == {y: 4}
