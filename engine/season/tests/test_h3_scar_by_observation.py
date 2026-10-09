"""IN-08 H3 (`workplans/valoria_master_workplan_v9_part5.md`, `= 12`'s scar rebuild) -- `Person.scar`
as `{pursuit: count}`, ONE COUNT PER OBSERVER PER VIOLATED PURSUIT, written at RESOLVE by the act
(`loop/resolve.py::_scar_witnesses`) on whoever `epistemic.observers_for` says saw it.

THE PLAN'S FALSIFIER, EACH CLAUSE AN EXECUTED TEST THAT CAN FAIL:
  * counts differ between `fan_out_mode` `presence_only` and `all_five`;
  * a scar on a person who did not observe the act -> fail;
  * a scar write reachable from a `Failure` band or from WITNESS's token -> fail.

The world is `probes.tiny_world`, whose persons hold no pursuits -- so every one is given all fifteen
(otherwise nobody can be scarred and every negative assertion here would pass vacuously), and one
`knot` ties the actor to `p_high`, who stands at `S`, away from the `Hh` where the act happens: the
witness-key channel admits him under `all_five` and nothing admits him under `presence_only`. That
knot is the whole of the planted difference between the two arms.
"""
from __future__ import annotations

import inspect

import pytest

from engine.season.data import verbs as _verbs
from engine.season.data.matrix import Step, WriteClass
from engine.season.data.rosters import FAN_OUT_MODES, PURSUITS
from engine.season.epistemic import observers_for
from engine.season.gaps import Forbidden
from engine.season.harness import probes as P
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.queries.person_q import said_of, violated_pursuits
from engine.season.seam import Resolution
from engine.season.state.carriers import Act, Claim, Tenure

from ._scar_helpers import fight
from ._scar_helpers import scars as _scars


def _world(mode: str = "all_five", exclude_actor: bool = False):
    w = P.tiny_world()
    for p in w.persons.values():
        p.pursuits = {e: 0.5 for e in PURSUITS}
    w.add_tenure(Tenure("t_h3_knot", "p_low", "p_high", "knot", since=0))
    w.fixtures = (w.fixtures.sweep("fan_out_mode", mode)
                  .sweep("scar_excludes_actor", exclude_actor))
    w.step = Step.RESOLVE
    return w


def test_h3_scar_counts_differ_between_presence_only_and_all_five():
    """FALSIFIER 1. The same act, the same world, the two fan-out arms: the counts differ, and the
    difference is exactly the person only the wider arm admits."""
    totals, scarred = {}, {}
    for mode in ("presence_only", "all_five"):
        w = _world(mode)
        kinds = [e.kind for e in fight(w, "h3_fight")]
        assert kinds == ["body.changed"], f"{mode}: the fight did not land ({kinds})"
        scarred[mode] = _scars(w)
        totals[mode] = sum(sum(s.values()) for s in scarred[mode].values())
    assert totals["presence_only"] > 0, "nobody was scarred under `presence_only`; nothing compared"
    assert totals["presence_only"] != totals["all_five"], (
        f"scar counts are identical across the fan-out arms ({totals}): the scar is not reading "
        "`observers_for`")
    assert set(scarred["all_five"]) - set(scarred["presence_only"]) == {"p_high"}, scarred


@pytest.mark.parametrize("mode", sorted(FAN_OUT_MODES))
def test_h3_no_scar_on_a_person_who_did_not_observe_the_act(mode):
    """FALSIFIER 2, on every declared fan-out arm. Every scarred person is one `observers_for`
    admits for the act's own Events, and every observer holding a pursuit the verb violates is
    scarred on exactly those pursuits, once. Under the two narrow arms at least one person with
    violable pursuits did NOT observe, and is asserted unscarred -- so the subset claim is not
    satisfied by a world in which everyone saw everything."""
    w = _world(mode)
    events = fight(w, "h3_fight")
    w.discard_caches()
    seen = {pid for e in events for pid, _ch in observers_for(w, e, mode, list(w.persons))}
    scars = _scars(w)
    assert scars, f"{mode}: nobody was scarred, so the subset assertion is vacuous"
    stray = set(scars) - seen
    assert not stray, f"{mode}: scarred {sorted(stray)}, who did not observe the act"
    for pid in seen:
        want = violated_pursuits(w.persons[pid], "fight")
        assert scars.get(pid, {}) == {e: 1 for e in want}, (pid, scars.get(pid), want)
    unseen = [pid for pid in w.persons if pid not in seen
              and violated_pursuits(w.persons[pid], "fight")]
    if mode != "total":
        assert unseen, f"{mode}: everyone observed, so nobody here tests the non-observer"
    assert not any(pid in scars for pid in unseen), (unseen, scars)


def test_h3_one_count_per_act_and_the_actor_arm():
    """A second identical act adds ONE to each count (the unit is a count, `ED-IN-0261`), and the
    `scar_excludes_actor` arm removes the actor and nobody else."""
    w = _world()
    fight(w, "h3_f1")
    once = _scars(w)
    fight(w, "h3_f2")
    twice = _scars(w)
    assert twice == {pid: {e: 2 * n for e, n in s.items()} for pid, s in once.items()}, twice
    assert all(isinstance(n, int) for s in twice.values() for n in s.values()), twice
    assert all(list(s) == sorted(s) for s in twice.values()), "a scar dict is not key-sorted"

    w_in, w_out = _world(exclude_actor=False), _world(exclude_actor=True)
    fight(w_in, "h3_fight")
    fight(w_out, "h3_fight")
    with_actor, without = _scars(w_in), _scars(w_out)
    assert "p_low" in with_actor, "under `False` the actor observed his own act and was not scarred"
    assert "p_low" not in without, without
    assert {k: v for k, v in with_actor.items() if k != "p_low"} == without


def test_h3_a_failure_band_and_a_refusal_scar_nobody(monkeypatch):
    """FALSIFIER 3a. `tell` is the one verb with a `Failure` band, and it is `uncelled:` -- so on
    the shipped table it could never scar and this would pass vacuously. The alignment binding is
    REBOUND (the one `data.verbs.align` reads) to cell `tell` exactly as `fight` is celled. Then:
    a `tell` folded at `Failure` scars nobody; and in the SAME rebound world a `fight` that lands
    does scar, so the empty arm can fail. A refused act (an ineligible `tell`) scars nobody too."""
    from engine.dice_engine.dice_engine import DEGREE_LABEL, Degree
    failure = DEGREE_LABEL[Degree.FAILURE]
    rebound = {ax: {**row, "tell": _verbs.align("fight", ax)}
               for ax, row in _verbs.ALIGNMENT.items()}
    monkeypatch.setattr(_verbs, "ALIGNMENT", rebound)
    w = _world()
    assert violated_pursuits(w.persons["p_mid"], "tell"), "the rebind did not cell `tell`"

    w.persons["p_low"].ledger.append(
        Claim("c_h3", "p_low", "Hh", "stores:grain", 8, 0, "firsthand", 37, "own"))
    tell = Act(id="h3_tell", actor="p_low", verb="tell",
               payload={"subject": "Hh", "to": "p_mid",
                        "said": said_of(w.persons["p_low"].ledger, "Hh", w.fixtures)})
    evs = SeasonDriver(w)._fold(w, mint_token(w, WriteClass.ACTS), tell, Resolution(failure, {}))
    assert [e.degree for e in evs] == [failure], [(e.kind, e.degree) for e in evs]
    assert not _scars(w), f"a `{failure}` band scarred {_scars(w)}"
    # The same act at a passing band emits the SUCCESS kind, so the act above was ADMITTED and
    # reached its `Failure` band -- not refused, which would emit the same `news.untold`.
    twin = Act(id="h3_tell_ok", actor="p_low", verb="tell", payload=dict(tell.payload))
    ok = SeasonDriver(w)._fold(w, mint_token(w, WriteClass.ACTS), twin,
                               Resolution(DEGREE_LABEL[Degree.SUCCESS], {}))
    assert [e.kind for e in ok] == ["news.told"], [e.kind for e in ok]

    refused = Act(id="h3_tell_x", actor="p_low", verb="tell",
                  payload={"subject": "nowhere", "to": "p_mid", "said": None})
    kinds = [e.kind for e in SeasonDriver(w)._fold(w, mint_token(w, WriteClass.ACTS), refused,
                                                     Resolution(failure, {}))]
    assert not _scars(w), f"a refusal ({kinds}) scarred {_scars(w)}"

    fight(w, "h3_fight")
    assert _scars(w), "a landed fight scarred nobody in this world, so the arms above prove nothing"


def test_h3_no_failure_band_declares_a_write():
    """FALSIFIER 3a's DATA HALF. The fold scars only on an outcome whose writes MOVED state, so a
    `Failure` band is unable to scar exactly while it declares no write. A verb row that gives its
    `Failure` band a write would make a failed act scar its witnesses: this fails first."""
    from engine.dice_engine.dice_engine import DEGREE_LABEL, Degree
    failure = DEGREE_LABEL[Degree.FAILURE]
    keyed = [(v, row) for v, row in _verbs.VERB_TABLE.items()
             if row.writes_by_degree and failure in row.writes_by_degree]
    assert keyed, f"no verb row has a `{failure}` band; this test checks nothing"
    bad = {v: row.writes_at(failure) for v, row in keyed if row.writes_at(failure)}
    assert not bad, f"a `{failure}` band declares writes, so a failed act would scar: {bad}"


def test_h3_a_fold_at_encounter_scars_its_observers():
    """The `(Person, scar)` row declares RESOLVE and ENCOUNTER (where a deferred contest such as
    `march` folds). The same act folded at ENCOUNTER scars the same observers by the same counts as
    at RESOLVE, and only persons `observers_for` admits."""
    from engine.season.data.matrix import matrix_row
    assert Step.ENCOUNTER in matrix_row("Person", "scar").steps
    at = {}
    for step in (Step.RESOLVE, Step.ENCOUNTER):
        w = _world("presence_only")
        w.step = step
        events = fight(w, "h3_fight")
        assert [e.kind for e in events] == ["body.changed"], (step, [e.kind for e in events])
        at[step] = _scars(w)
        w.discard_caches()
        seen = {pid for e in events
                for pid, _ch in observers_for(w, e, "presence_only", list(w.persons))}
        assert at[step] and set(at[step]) <= seen, (step, at[step], seen)
    assert at[Step.ENCOUNTER] == at[Step.RESOLVE], at


def test_h3_witness_cannot_write_a_scar():
    """FALSIFIER 3b. WITNESS's token cannot reach `(Person, scar)`: the gate refuses the row at
    WITNESS under S9.3 (WITNESS NEVER TOUCHES A BELIEF), and WITNESS's own body names neither the
    field nor the scar writer."""
    w = P.tiny_world()
    w.step = Step.WITNESS
    with pytest.raises(Forbidden) as exc:
        w.write("scar", mint_token(w, WriteClass.INTERIOR), lambda: None,
                record_kind="Person", fieldname="scar", driver="Act")
    assert exc.value.where == "S9.3", exc.value.where
    src = inspect.getsource(SeasonDriver.witness)
    assert 'fieldname="scar"' not in src and "_scar_witnesses" not in src
