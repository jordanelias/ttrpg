"""CR-24 (`H-360`, M4 Ask B (b)): the winners of a fought field take their own engine casualties, on `body` only.

`field_winner_casualties: engine` is SHIPPED; `off` is the field as ED-IN-0279 left it (the winner is not written).

THE FIELD IS A REAL FOLD OF A HAND-BUILT SITUATION. One season of the shipped realm fights almost no field (seed 0:
`field.unopposed` 3, `march.declared` 6), so the falsifier folds ONE `march` through the real driver (RESOLVE then
ENCOUNTER, `test_march._fold_one`) -- the engine fights it; no `Resolution` is hand-built -- with the Crown's two
marchers made cohorts (`Person.weight` 10) on `set_s_036`, the weight -> troops scale at 10 (REM-32's
`field_troops_per_weight`, a value of THIS TEST) and `field_subunits: person` (CP-T04-01). Realm seed 0: the attacker
WINS (`field.won`), one marcher's subunit is cut (survivor ratio 0.982) and the other's is not. The preconditions are
asserted, so a moved fixture reads as a precondition, not a pass.

Why `person`: under `side` a winning headcount side's ratio reads 1.0 or above (`effective_size / size_max` floors
`size_max`, `_grade`'s own note), and a winner is never raised, so the `side` arm writes a winner nothing in these folds.
The per-person ratio is the one that is below 1 for a winner.

The cases: the falsifier (each attacking claimant's `body` falls by HIS OWN ratio; the defenders still take theirs; no
stance row on any winner), its planted failure (winners written at the loser's ratio reddens it), the control (`off`
writes no winner and reproduces the pre-item world; `engine` differs from it in the winner's body and nothing else),
the one-Subject rule for a winner who marches, and the arm's refusal of a stranger."""
from __future__ import annotations

import importlib

import pytest

from engine.season.harness.populated import build_realm
from engine.season.state.world import World
from engine.season.tests.test_march import _fold_one, _march_act

SEED, WEIGHT, SCALE = 0, 10, 10
MARCHERS = ("p_npc_033", "p_npc_035")


def _mb():
    """`engine/` names no `modules/` import at module level; the module is loaded on first use."""
    return importlib.import_module("modules.mass_battle.massbattle")


def _fold(arm="engine", *, model=None, subunits="person", spy=None):
    """Fold the one march. Returns `(world, events, bodies before, stance before, the module's per-person record)`.
    The record is read off `_person_report`'s return (`spy`, when given, is applied to it first)."""
    mb = _mb()
    real = mb._person_report
    seen = {}

    def tap(units, members, logs):
        rep = real(units, members, logs)
        if spy is not None:
            rep = spy(units, rep)
        seen.update(rep["subunits"])
        return rep

    mb._person_report = tap
    try:
        w = build_realm(SEED)
        for pid in MARCHERS:
            w.persons[pid].weight = WEIGHT
        w.fixtures = (w.fixtures.sweep("field_troops_per_weight", SCALE).sweep("field_subunits", subunits)
                      .sweep("field_winner_casualties", arm))
        if model is not None:
            w.fixtures = w.fixtures.sweep("field_casualty_model", model)
        before = {pid: w.persons[pid].body for pid in w.persons}
        stance = {pid: list(w.persons[pid].stance or []) for pid in w.persons}
        events = _fold_one(w, _march_act(MARCHERS[0], "set_s_036", "off_spymaster"), contest_max_depth=2)
    finally:
        mb._person_report = real
    return w, events, before, stance, seen


def _check_winners_by_own_ratio(w, before, record):
    """The falsifier's assertions: each attacking claimant's body is `max(1, int(body * his ratio))`, strictly below the
    start for the one whose subunit was cut, so a write at any other ratio fails here."""
    for pid in MARCHERS:
        want = max(1, int(before[pid] * min(1.0, record[pid][0])))
        assert w.persons[pid].body == want, f"{pid}: body {w.persons[pid].body}, his own ratio gives {want}"
    cut = [pid for pid in MARCHERS if record[pid][0] < 1.0]
    assert cut, "precondition: a winner with a survivor ratio below 1"
    assert all(w.persons[pid].body < before[pid] for pid in cut)


def test_shipped_arm_is_engine():
    assert build_realm(0).fixtures.get("field_winner_casualties") == "engine"


def test_falsifier_each_winning_claimant_falls_by_his_own_ratio_and_earns_no_stance_row():
    """The entry's falsifier, on a real fold: the attacker wins with a survivor ratio below 1, and under `engine` each
    attacking claimant's `body` falls by his own ratio -- one marcher is cut, the other (ratio 1.0) is not -- with no
    grudge or morale row on any winner, and the losers still take theirs."""
    w, events, before, stance, record = _fold("engine")
    kinds = [e.kind for e in events]
    assert "field.won" in kinds and "field.lost" not in kinds, f"precondition: the attacker wins ({kinds})"
    assert record[MARCHERS[0]][0] == 1.0 and 0.0 < record[MARCHERS[1]][0] < 1.0, f"precondition: ratios {record}"
    _check_winners_by_own_ratio(w, before, record)
    assert w.persons[MARCHERS[0]].body == before[MARCHERS[0]] != w.persons[MARCHERS[1]].body

    # No winner earns a row: the stance of both marchers is what the build left it.
    for pid in MARCHERS:
        assert list(w.persons[pid].stance or []) == stance[pid], f"{pid}: a stance row was written on a winner"
    # The losers are written as they were: each defender's stance gained its rows, scaled by his own ratio.
    defenders = [pid for pid in record if pid not in MARCHERS]
    assert defenders and all(list(w.persons[pid].stance or []) != stance[pid] for pid in defenders), (
        "control: the losing side's stance rows are still written")


def test_planted_failure_winners_written_at_the_losers_ratio_reddens_the_falsifier():
    """MUTATION: every attacking claimant's ratio is the LOSING side's (the defenders' survivor share). The falsifier's
    check, against the unmutated record, must then fail -- were it to pass, the test could not observe the failure."""
    _w0, _e0, before0, _s0, record0 = _fold("engine")

    def loser_ratio(units, rep):
        loser = units[1].effective_size / max(1, units[1].size_max)
        for pid in MARCHERS:
            rep["subunits"][pid] = (loser, rep["subunits"][pid][1])
        return rep

    w, _events, _before, _stance, _rec = _fold("engine", spy=loser_ratio)
    assert w.persons[MARCHERS[0]].body < before0[MARCHERS[0]], "the mutant wrote nobody (the loser's ratio is below 1)"
    with pytest.raises(AssertionError):
        _check_winners_by_own_ratio(w, before0, record0)


def test_control_off_writes_no_winner_and_engine_differs_from_it_in_the_winners_body_alone():
    """`off` is the field as it was: both marchers keep their bodies. `engine` differs from `off` in the one marcher's
    body and in nothing else -- restore it and the two worlds hash equal -- so a winner earns no stance row, no mover
    write, and the defenders' casualties are the same."""
    w_off, ev_off, before, _stance, _ = _fold("off")
    w_on, ev_on, _b, _s, record = _fold("engine")
    assert [e.kind for e in ev_off] == [e.kind for e in ev_on]
    assert [w_off.persons[pid].body for pid in MARCHERS] == [before[pid] for pid in MARCHERS]
    assert w_off.content_hash() != w_on.content_hash()
    cut = [pid for pid in MARCHERS if record[pid][0] < 1.0]
    assert cut == [MARCHERS[1]]
    for pid in cut:
        w_on.persons[pid].body = before[pid]
    assert w_off.content_hash() == w_on.content_hash()


def test_a_winner_who_also_marches_is_one_subject_and_a_winner_is_never_a_stance_subject(monkeypatch):
    """`Won` moves the claimants (`_relocate`), so the marchers are both winners and movers: each is named ONCE, by the
    mover's whole-entity Subject, and no Subject names a winner's `stance`."""
    captured = []
    real = World.effect_body_observed

    def tap(self, build, *a, **k):
        out = real(self, build, *a, **k)
        if hasattr(out, "subjects"):
            captured.append(out)
        return out

    monkeypatch.setattr(World, "effect_body_observed", tap)
    _fold("engine")
    march = [c for c in captured if any(s.id in MARCHERS for s in c.subjects)]
    assert len(march) == 1, "the march effect ran once"
    named = [s.id for s in march[0].subjects]
    for pid in MARCHERS:
        assert named.count(pid) == 1, f"{pid} is named {named.count(pid)} times"
    assert all(s.ref[3] is None for s in march[0].subjects if s.id in MARCHERS), (
        "a winner who marches is named whole (the mover's Subject), not by a field")


def test_total_casualty_arm_kills_a_winner_who_took_a_casualty_by_the_same_death_rule():
    """`field_casualty_model: total` ("any wound is lethal"): a winner whose ratio is below 1 takes the loser's body-to-0
    and the same death write -- removed as a dead loser is (`remove_person`), publishes `person.died`, and does not
    arrive; a winner at ratio 1 took no casualty and is untouched, so he still arrives."""
    w, events, before, _stance, _ = _fold("engine", model="total")
    kinds = [e.kind for e in events]
    # the fold's two marchers carry ratios 1.0 and 0.982 (see the falsifier)
    assert "p_npc_033" in w.persons and w.persons["p_npc_033"].body == before["p_npc_033"]
    assert "p_npc_035" not in w.persons, "the winner who took a casualty should have died by the loser's rule"
    assert "field.won" in kinds and "person.died" in kinds and "army.arrived" in kinds

    w_off, ev_off, _b, _s, _r = _fold("off", model="total")
    assert all(pid in w_off.persons for pid in MARCHERS) and "army.arrived" in [e.kind for e in ev_off]


def test_model_none_writes_no_winner():
    w, _events, before, _stance, _ = _fold("engine", model="none")
    assert [w.persons[pid].body for pid in MARCHERS] == [before[pid] for pid in MARCHERS]


def test_an_unknown_arm_is_refused():
    from engine.season.gaps import Unspecified
    with pytest.raises(Exception) as err:
        _fold("sometimes")
    assert "sometimes" in str(err.value) or isinstance(err.value, Unspecified)
