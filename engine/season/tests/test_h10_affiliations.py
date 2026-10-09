"""IN-08 H10 (`workplans/valoria_master_workplan_v9_part5.md`) -- the affiliation roster, the
`incompatible` half-matrix, `Person.conviction` and the derived `confliction(p)`.

THE PLAN'S FALSIFIER, *"two incompatible affiliations at full intensity load, and `confliction` is
non-zero"*, plus the refusals that make it able to fail, each an executed test:
  * a planted `incompatible` with an unrostered pair (and a self-pair, a pair keyed twice, a table
    with no `true`) -> the loader refuses;
  * two incompatible affiliations at full intensity load through the cast's authored-row path and
    `confliction != 0`; a compatible pair, the `null` pair and no affiliation are the controls at 0;
  * `(Person, conviction)` is written only where its `write_matrix.yaml` row admits it: WITNESS's
    token is refused under S9.3 and MATTER's under S3-L4, while the row's RESOLVE cell admits;
  * the world builder fills the field on every cast person, through the one validator.
"""
from __future__ import annotations

import importlib.util
import itertools
import os

import pytest

from engine.season.data import affiliations as A
from engine.season.data import cast
from engine.season.data.matrix import Step, WriteClass
from engine.season.data.rosters import AFFILIATIONS
from engine.season.gaps import Forbidden, Unspecified
from engine.season.harness import probes as P
from engine.season.loop.driver import mint_token
from engine.season.queries.person_q import confliction
from engine.season.state.carriers import Person
from engine.substrate.descriptors import AFFILIATION_CEILING, AFFILIATION_FLOOR

_FULL = AFFILIATION_CEILING


def _pairs(value):
    """Every rostered unordered pair whose shipped cell reads `value` (True, False or None)."""
    from engine.season.data.rosters import table
    cells = table("incompatible")
    return [(a, b) for a, row in cells.items() for b, v in row.items() if v is value]


def test_h10_roster_and_scale_come_from_the_single_owner():
    """The season roster is the leaf's, and full intensity is a real ceiling above the floor."""
    from engine.substrate.descriptors import AFFILIATIONS as LEAF
    assert AFFILIATIONS == frozenset(LEAF) and len(LEAF) >= 2
    assert isinstance(AFFILIATION_FLOOR, int) and isinstance(_FULL, int) and AFFILIATION_FLOOR < _FULL


def test_h10_loader_refuses_an_unrostered_pair():
    good = next(iter(sorted(AFFILIATIONS)))
    with pytest.raises(Forbidden):
        A._load_incompatible({good: {"altonian_theocracy": True}})
    with pytest.raises(Forbidden):
        A._load_incompatible({"altonian_theocracy": {good: True}})


def test_h10_loader_refuses_a_self_pair_a_double_key_and_an_inert_table():
    a, b = sorted(AFFILIATIONS)[:2]
    with pytest.raises(Forbidden):
        A._load_incompatible({a: {a: True}})
    with pytest.raises(Forbidden):
        A._load_incompatible({a: {b: True}, b: {a: True}})
    with pytest.raises(Forbidden):
        A._load_incompatible({a: {b: False}})
    with pytest.raises(Forbidden):
        A._load_incompatible({a: {b: 1}})
    assert A._load_incompatible({a: {b: True}}) == frozenset({frozenset((a, b))})


def test_h10_shipped_half_matrix_is_whole_and_loads():
    """Every unordered rostered pair is keyed once (none left unconsidered), and at least one
    strains -- so the falsifier below has a pair to plant."""
    keyed = {frozenset(p) for v in (True, False, None) for p in _pairs(v)}
    every = {frozenset(p) for p in itertools.combinations(sorted(AFFILIATIONS), 2)}
    assert keyed == every, sorted(map(sorted, every ^ keyed))
    assert A.INCOMPATIBLE == {frozenset(p) for p in _pairs(True)} and A.INCOMPATIBLE


def test_h10_two_incompatible_affiliations_at_full_intensity_load_and_conflict():
    """THE PLAN'S FALSIFIER. Each strained pair, planted at full intensity on an authored registry
    row and loaded through `cast.conviction_of` (the builder's path), gives non-zero confliction --
    the ceiling, under the `min` reading."""
    checked = 0
    for a, b in _pairs(True):
        held = cast.conviction_of({"id": "planted", "affiliations": {a: _FULL, b: _FULL}})
        p = Person("p_h10", conviction=held)
        assert confliction(p) == _FULL, (a, b, confliction(p))
        checked += 1
    assert checked >= 1


@pytest.mark.parametrize("value", [False, None])
def test_h10_control_a_pair_that_does_not_strain_reads_zero(value):
    """CONTROL: the same full-intensity load over a `false` or a `null` pair reads 0, as does one
    affiliation alone and none at all -- so the non-zero above is the relation's, not the load's."""
    pairs = _pairs(value)
    assert pairs, f"no shipped pair reads {value!r}; this control checks nothing"
    for a, b in pairs:
        p = Person("p_h10", conviction=cast.conviction_of({"affiliations": {a: _FULL, b: _FULL}}))
        assert confliction(p) == 0, (a, b)
    for a in sorted(AFFILIATIONS):
        assert confliction(Person("p_one", conviction={a: _FULL})) == 0
    assert confliction(Person("p_none")) == 0


def test_h10_intensity_and_name_are_refused_off_the_roster_and_scale():
    a = sorted(AFFILIATIONS)[0]
    for bad in (_FULL + 1, AFFILIATION_FLOOR - 1, 2.5, True, "5"):
        with pytest.raises(Unspecified):
            cast.conviction_of({"affiliations": {a: bad}})
    with pytest.raises(Unspecified):
        cast.conviction_of({"affiliations": {"threadwork": 3}})
    assert cast.conviction_of({"affiliations": {a: 0}}) == {}
    assert cast.conviction_of({}) == {}


def test_h10_witness_and_matter_cannot_write_conviction_and_resolve_can():
    """`(Person, conviction)` is reachable only through its row's RESOLVE cell. WITNESS's token is
    refused under S9.3 (WITNESS NEVER TOUCHES A BELIEF) and MATTER's under S3-L4 -- each by its own
    law, not the generic unmarked-cell fallback -- and the row admits an ACTS write at RESOLVE."""
    w = P.tiny_world()
    pid = next(iter(w.persons))
    for step, cls, law in ((Step.WITNESS, WriteClass.INTERIOR, "S9.3"),
                           (Step.MATTER, WriteClass.MATTER, "S3-L4")):
        w.step = step
        with pytest.raises(Forbidden) as exc:
            w.write("conviction", mint_token(w, cls), lambda: None,
                    record_kind="Person", fieldname="conviction", driver="Act")
        assert exc.value.where == law, (step, exc.value.where)
    w.step = Step.RESOLVE
    a = sorted(AFFILIATIONS)[0]
    w.write("conviction", mint_token(w, WriteClass.ACTS),
            lambda: w.persons[pid].conviction.update({a: 1}),
            record_kind="Person", fieldname="conviction", driver="Act")
    assert w.persons[pid].conviction == {a: 1}


def test_h10_world_builder_fills_conviction_from_the_authored_row(monkeypatch):
    """The field is FILLED, not merely declared. No registry row carries `affiliations:` today, so
    the shipped fill is `{}` everywhere -- indistinguishable from a builder that never filled it. So
    the row source is planted: every cast row gains one strained pair at full intensity, and every
    person the builder seeded from a row must carry exactly that vector (and conflict)."""
    from engine.season.harness import populated
    a, b = _pairs(True)[0]
    planted = {a: _FULL, b: _FULL}
    real_row = cast.row

    def _row(cid):
        r = real_row(cid)
        return None if r is None else {**r, "affiliations": dict(planted)}

    monkeypatch.setattr(cast, "row", _row)
    w = populated.build_realm(0)
    filled = [pid for pid, p in w.persons.items() if p.conviction]
    assert filled, "the builder filled no person's conviction from the planted rows"
    for pid in filled:
        assert w.persons[pid].conviction == planted, pid
        assert confliction(w.persons[pid]) == _FULL, pid


def test_h10_exporter_refuses_an_unbounded_or_open_scale():
    path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "tools", "export_descriptors.py")
    spec = importlib.util.spec_from_file_location("_export_descriptors_h10", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    names = ["a", "b"]
    assert mod._affiliation_roster({"affiliation_roster": {"names": names, "scale": "0-5"}})[
        "scale"] == {"floor": 0, "ceiling": 5}
    for scale in (None, "0-5+", "5-0", "0-1.5"):
        with pytest.raises(SystemExit):
            mod._affiliation_roster({"affiliation_roster": {"names": names, "scale": scale}})
    with pytest.raises(SystemExit):
        mod._affiliation_roster({"affiliation_roster": {"names": names, "count": 3, "scale": "0-5"}})
