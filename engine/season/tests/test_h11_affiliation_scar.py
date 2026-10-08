"""IN-08 H11 (`workplans/valoria_master_workplan_v9_part5.md`, *"H3's mechanism over the affiliation
table"*; J-5's C4, the draft's rule R-C4) -- an observer takes one `Person.scar` count per held
AFFILIATION an act he saw violates, through the same writer as H3's pursuit counts
(`loop/resolve.py::_scar_witnesses`), reading `rosters.yaml: tables.affiliation_engagement`.

THE SHIPPED REALM CANNOT SHOW IT: no cast row carries affiliation content (H10), so every shipped
`Person.conviction` is `{}`; and no verb with a negative cell lands through the fold today (the
table's own note). So the end-to-end falsifier runs on a PLANTED world -- `probes.tiny_world` with
affiliations given and the loaded table rebound so `fight` (which lands there) carries a violating
cell -- and every positive arm has a control that holds everything but the one thing it tests:
  * nobody holds an affiliation -> the same act scars nobody;
  * holdings given, the SHIPPED table (where `fight` has no cell) -> the same act scars nobody;
  * holdings given, table rebound -> every observer is scarred on exactly his violated holdings,
    the one non-observer is not, and `Person.conviction` is not written;
  * a `Failure` band of a verb rebound to violate scars nobody, while a landed act in the same
    world does;
  * a planted table with a magnitude, an overlap, a bad shared column or an unrostered column ->
    the loader refuses.
"""
from __future__ import annotations

import pytest

from engine.season.data import affiliations as A
from engine.season.data.matrix import Step, WriteClass
from engine.season.data.rosters import AFFILIATIONS, FAN_OUT_MODES, WOUNDED, table
from engine.season.data.verbs import VERB_TABLE
from engine.season.epistemic import observers_for
from engine.season.gaps import Forbidden, Unspecified
from engine.season.harness import probes as P
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.queries.person_q import said_of, violated_affiliations, violated_pursuits
from engine.season.seam import Resolution
from engine.season.state.carriers import Act, Claim, Person, Tenure
from engine.substrate.descriptors import AFFILIATION_CEILING

_ROSTER = sorted(AFFILIATIONS)
_STRAINED = sorted(_ROSTER)[:2]          # any two holdings; which two is not the point
_HOLDING = {a: AFFILIATION_CEILING for a in _STRAINED}


def _shared_negative_verbs():
    return sorted(v for v, x in A.ENGAGEMENT[A.SHARED_COLUMN].items() if x < 0)


def _world(mode="presence_only", holdings=None):
    """H3's planted world (one `knot` ties `p_low` to `p_high`, who stands away from the act), with
    NO pursuits held -- so any scar here is an affiliation's -- and `holdings` on every person."""
    w = P.tiny_world()
    for p in w.persons.values():
        p.pursuits = {}
        p.conviction = dict(holdings or {})
    w.add_tenure(Tenure("t_h11_knot", "p_low", "p_high", "knot", since=0))
    w.fixtures = w.fixtures.sweep("fan_out_mode", mode)
    w.step = Step.RESOLVE
    return w


def _fight(w, aid="h11_fight"):
    res = Resolution(WOUNDED, {"wound_state": {"p_mid": {"health_full": 10,
                                                         "health_remaining": 5}}})
    return SeasonDriver(w)._fold(w, mint_token(w, WriteClass.ACTS),
                                 Act(id=aid, actor="p_low", verb="fight",
                                     payload={"subject": "p_mid"}), res)


def _scars(w):
    return {pid: dict(p.scar) for pid, p in w.persons.items() if p.scar}


def _rebound(**cells):
    """The loaded table with `cells` laid over it: `{column: {verb: value}}`."""
    out = {col: dict(row) for col, row in A.ENGAGEMENT.items()}
    for col, row in cells.items():
        out.setdefault(col, {}).update(row)
    return out


# ---------------------------------------------------------------------------- the table, shipped

def test_h11_shipped_table_loads_and_its_sign_test_reads_both_clauses():
    """R-C4.1 (shared column: every holding alike) and R-C4.2 (a per-affiliation cell) on the
    shipped table, with the zero-vector control: a person holding nothing is violated by no verb."""
    neg = _shared_negative_verbs()
    assert neg, "the shared column has no negative cell; the scar can read nothing from it"
    everyone = Person(id="h11_all", conviction={a: 1 for a in _ROSTER})
    for verb in neg:
        assert violated_affiliations(everyone, verb) == tuple(_ROSTER), verb
    exceptions = {(col, v): x for col, row in A.ENGAGEMENT.items() if col != A.SHARED_COLUMN
                  for v, x in row.items()}
    assert exceptions, "no per-affiliation cell loaded; R-C4.2 is not in the table"
    for (col, verb), x in exceptions.items():
        assert (col in violated_affiliations(everyone, verb)) is (x < 0), (col, verb, x)
    nobody = Person(id="h11_none", conviction={})
    assert not any(violated_affiliations(nobody, v) for v in VERB_TABLE)
    positive = [v for v, x in A.ENGAGEMENT[A.SHARED_COLUMN].items() if x > 0]
    assert positive and not any(violated_affiliations(everyone, v) for v in positive)


# ------------------------------------------------------------------------- the falsifier, planted

@pytest.mark.parametrize("mode", sorted(FAN_OUT_MODES))
def test_h11_an_observed_violation_scars_each_observer_on_his_violated_holdings(monkeypatch, mode):
    """Control 1 (no holdings) and control 2 (shipped table) leave everyone unscarred; the rebound
    table scars exactly the observers, on exactly the holdings the table says `fight` violates,
    once each, and writes no `conviction`."""
    w0 = _world(mode)
    _fight(w0)
    assert not _scars(w0), f"{mode}: an unaffiliated, pursuit-less world was scarred {_scars(w0)}"

    w1 = _world(mode, _HOLDING)
    _fight(w1)
    assert not _scars(w1), f"{mode}: the shipped table gives `fight` no cell, yet {_scars(w1)}"

    monkeypatch.setattr(A, "ENGAGEMENT", _rebound(**{A.SHARED_COLUMN: {"fight": -0.3}}))
    w = _world(mode, _HOLDING)
    events = _fight(w)
    assert [e.kind for e in events] == ["body.changed"], [e.kind for e in events]
    w.discard_caches()
    seen = {pid for e in events for pid, _ch in observers_for(w, e, mode, list(w.persons))}
    scars = _scars(w)
    assert scars, f"{mode}: nobody was scarred, so the assertions below are vacuous"
    assert set(scars) <= seen, f"{mode}: scarred {sorted(set(scars) - seen)}, who did not observe"
    for pid in seen:
        want = violated_affiliations(w.persons[pid], "fight")
        assert want == tuple(_STRAINED)
        assert not violated_pursuits(w.persons[pid], "fight")
        assert scars.get(pid) == {a: 1 for a in want}, (pid, scars.get(pid))
    if mode != "total":
        unseen = set(w.persons) - seen
        assert unseen, f"{mode}: everyone observed, so nobody tests the non-observer"
        assert not unseen & set(scars), (unseen, scars)
    assert all(p.conviction == _HOLDING for p in w.persons.values()), "H11 wrote `conviction`"


def test_h11_a_per_affiliation_cell_scars_only_that_holding(monkeypatch):
    """R-C4.2 end to end: a cell under ONE affiliation scars an observer on that one and not on
    another he holds -- the per-affiliation column is read per affiliation, not as the shared one."""
    target, other = _STRAINED
    monkeypatch.setattr(A, "ENGAGEMENT", _rebound(**{target: {"fight": -1.0}}))
    w = _world("all_five", _HOLDING)
    _fight(w)
    scars = _scars(w)
    assert scars and all(s == {target: 1} for s in scars.values()), scars
    assert not any(other in s for s in scars.values())


def test_h11_a_failure_band_scars_nobody_on_an_affiliation(monkeypatch):
    """`tell` is the one verb with a `Failure` band. Rebound to violate a holding, a `tell` folded at
    `Failure` scars nobody; a landed `fight` rebound the same way in the same world does, so the
    empty arm can fail."""
    from engine.dice_engine.dice_engine import DEGREE_LABEL, Degree
    failure = DEGREE_LABEL[Degree.FAILURE]
    monkeypatch.setattr(A, "ENGAGEMENT",
                        _rebound(**{A.SHARED_COLUMN: {"tell": -0.3, "fight": -0.3}}))
    w = _world("all_five", _HOLDING)
    assert violated_affiliations(w.persons["p_mid"], "tell"), "the rebind did not cell `tell`"
    w.persons["p_low"].ledger.append(
        Claim("c_h11", "p_low", "Hh", "stores:grain", 8, 0, "firsthand", 37, "own"))
    tell = Act(id="h11_tell", actor="p_low", verb="tell",
               payload={"subject": "Hh", "to": "p_mid",
                        "said": said_of(w.persons["p_low"].ledger, "Hh", w.fixtures)})
    evs = SeasonDriver(w)._fold(w, mint_token(w, WriteClass.ACTS), tell, Resolution(failure, {}))
    assert [e.degree for e in evs] == [failure], [(e.kind, e.degree) for e in evs]
    assert not _scars(w), f"a `{failure}` band scarred {_scars(w)}"
    _fight(w)
    assert _scars(w), "a landed rebound fight scarred nobody, so the arm above proves nothing"


# ------------------------------------------------------------------------------- the refusals

def _shipped():
    return table("affiliation_engagement")


def test_h11_loader_accepts_the_shipped_table_and_refuses_each_planted_defect():
    shared, cells = A._load_engagement(_shipped(), A.SHARED_COLUMN)
    assert shared == A.SHARED_COLUMN and cells == A.ENGAGEMENT
    some_aff = _ROSTER[0]
    verb = _shared_negative_verbs()[0]
    other_verb = next(v for v in sorted(VERB_TABLE) if v not in _shipped()[A.SHARED_COLUMN])

    magnitude = {**_shipped(), some_aff: {other_verb: -0.5}}
    with pytest.raises(Forbidden, match="not a sign"):
        A._load_engagement(magnitude, A.SHARED_COLUMN)
    overlap = {**_shipped(), some_aff: {verb: -1}}
    with pytest.raises(Forbidden, match="shared cell and a cell"):
        A._load_engagement(overlap, A.SHARED_COLUMN)
    with pytest.raises(Unspecified):
        A._load_engagement(_shipped(), some_aff)
    with pytest.raises(Unspecified):
        A._load_engagement(_shipped(), "")
    with pytest.raises(Forbidden):
        A._load_engagement({**_shipped(), "h11_no_such_creed": {other_verb: -1}}, A.SHARED_COLUMN)
    with pytest.raises(Forbidden):
        A._load_engagement({A.SHARED_COLUMN: {"h11_no_such_verb": -0.3}}, A.SHARED_COLUMN)
    with pytest.raises(Forbidden):
        A._load_engagement({A.SHARED_COLUMN: {verb: None}}, A.SHARED_COLUMN)


def test_h11_loader_refuses_a_name_on_both_the_affiliation_and_pursuit_rosters(monkeypatch):
    """`Person.scar` keys both rosters at once, so one name on both would merge two counts. The
    loader imports `rosters.PURSUITS` at call time, so rebinding it here is what the check reads;
    the control is the same call on the shipped rosters, which loads."""
    from engine.season.data import rosters as R
    A._load_engagement(_shipped(), A.SHARED_COLUMN)
    monkeypatch.setattr(R, "PURSUITS", tuple(R.PURSUITS) + (_ROSTER[0],))
    with pytest.raises(Forbidden, match="name both an affiliation and a pursuit"):
        A._load_engagement(_shipped(), A.SHARED_COLUMN)


def test_h11_witness_cannot_reach_the_scar_row():
    """The row H11 writes through is H3's `(Person, scar)`; WITNESS's token is refused there (S9.3),
    and H11 adds no second row and no `conviction` write (its `unproduced:` stands)."""
    w = P.tiny_world()
    w.step = Step.WITNESS
    with pytest.raises(Forbidden) as exc:
        w.write("scar", mint_token(w, WriteClass.INTERIOR), lambda: None,
                record_kind="Person", fieldname="scar", driver="Act")
    assert exc.value.where == "S9.3", exc.value.where
