"""`H-98`, plan position `8` -- THE WOUND-COUNT BAND EDGE IS DATA (`rosters.yaml: combat_band_edges`).

`seam/ladder.py::combat_degree` used to be two literals (`if st["felled"]` / `st["wounds"] > 0`).
It now walks `COMBAT_EDGES`, loaded and validated at import by `rosters.load_combat_band_edges`, over
the quantities `wound_quantities` lists -- the same list `seam/wrappers/combat.py::_state` lifts the
scene with. What each test proves, and the control that stops it passing vacuously:

  1. THE LOADER REFUSES, AT LOAD, an edge on a quantity the tracker does not return -- exercised on
     the real YAML through the documented patch point (`rosters.ROSTERS_YAML`, re-calling the
     loader), with the unmutated row as the control that the loader accepts what ships.
  2. AN UNREACHABLE EDGE (`wounds > 4`, since `wounds` never exceeds `MAXWOUNDS_CAP + 1`) GRADES EVERY
     STANDING FOUGHT SUBJECT `Untouched`, on real fights; the `max_wounds` arm moves only a subject
     BELOW the cap (a subject at the cap, `wounds = max_wounds + 1`, still reads `Wounded`). The same
     scene at the shipped edge reads `Wounded` for a subject (so the edge, not the scene, is what
     moved), and `>= 1` fought subject is asserted.
  3. THE SHIPPED EDGES REPRODUCE THE OLD LITERAL EXACTLY, over a grid of hand-built states and over
     real fights -- the old two-line function is the oracle, copied here.
  4. THE SWEPT FIXTURE REACHES THE FOLD (a driver fold at an arm writes at that arm's band), a bad
     arm refuses, and `_state` lifts exactly the roster's list.
"""

from __future__ import annotations

import copy
import functools
import itertools
from unittest import mock

import pytest

from engine.season.data import rosters
from engine.season.data.fixtures import DEFAULT_FIXTURES
from engine.season.data.matrix import Step, WriteClass
from engine.season.data.rosters import (
    COMBAT_BANDS, COMBAT_EDGES, FELLED, UNTOUCHED, WOUND_QUANTITIES, WOUNDED,
    load_combat_band_edges)
from engine.season.gaps import Forbidden, Unspecified
from engine.season.harness import probes as P
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.seam import combat_degree, contest, degree_of
from engine.season.seam.wrappers import combat as C
from engine.season.state.carriers import Act

# ⚠ A FIXTURE, NOT A MODULE-LEVEL `skipif(C.engine() is None)`. `test_importing_every_engine_module_
# pulls_in_no_subsystem` imports EVERY module under `engine/` (this one included) in a subprocess and
# fails if any subsystem file loaded; `C.engine()` at import loads the combat engine, so the skip
# test read as a leak. The engine is loaded when a test that needs it RUNS, never when this imports.
@pytest.fixture
def engine_available():
    if C.engine() is None:
        pytest.skip(f"personal_combat engine unavailable: {C.load_error()}")


needs_engine = pytest.mark.usefixtures("engine_available")


def _row() -> dict:
    return copy.deepcopy(rosters._ROSTERS["combat_band_edges"])


def _old_literal(st: dict) -> str:
    """THE ORACLE: `combat_degree`'s two literals as they stood before plan position `8`."""
    if st["felled"]:
        return FELLED
    return WOUNDED if st["wounds"] > 0 else UNTOUCHED


@functools.lru_cache(maxsize=None)
def _scene(cause: str) -> dict:
    """A fought scene, cached: the fight is deterministic and no test mutates the result (the same twelve
    scenes are graded by four tests)."""
    w = P.tiny_world()
    w.step = Step.RESOLVE
    return contest(w, "R", "the body", ["p_low", "p_mid"], 0, 2, [cause])


# --- 1. THE LOADER REFUSES AT LOAD ------------------------------------------------------------------

def test_the_shipped_edges_load_and_reproduce_the_three_bands():
    """The control for every refusal below: the unmutated row is accepted, and it is the edges the
    module bound at import. `Felled` / `Wounded` carry an edge and `Untouched` is the residual."""
    got = load_combat_band_edges(_row(), COMBAT_BANDS, WOUND_QUANTITIES)
    assert got == COMBAT_EDGES
    assert [b for b, _q, _a in got] == [FELLED, WOUNDED]
    assert COMBAT_BANDS[-1] == UNTOUCHED and UNTOUCHED not in [b for b, _q, _a in got]
    assert all(q in WOUND_QUANTITIES for _b, q, _a in got)


def test_an_edge_on_a_quantity_the_tracker_does_not_return_refuses_at_load(tmp_path):
    """PLAN POSITION 8'S FALSIFIER (i). Written to a real YAML file and read through the loader's own
    documented patch point (`rosters.ROSTERS_YAML`, then re-call `_load_rosters`) -- not a dict the
    test built and handed straight to the checker -- so the refusal is observed on the path the
    import-time binding takes."""
    import yaml as _y
    doc = _y.safe_load(rosters.ROSTERS_YAML.read_text())
    good = doc["rosters"]["combat_band_edges"]["edges"]["Wounded"]
    assert good["quantity"] == "wounds"          # the thing the mutation changes
    refused = []
    for bad_quantity in ("hit_points", "wound_count", "Wounds"):
        doc["rosters"]["combat_band_edges"]["edges"]["Wounded"] = {
            "quantity": bad_quantity, "above": 0}
        p = tmp_path / f"rosters_{bad_quantity}.yaml"
        p.write_text(_y.safe_dump(doc))
        with mock.patch.object(rosters, "ROSTERS_YAML", p):
            loaded, _tables = rosters._load_rosters()
        with pytest.raises(Forbidden, match="does not return"):
            load_combat_band_edges(loaded["combat_band_edges"], COMBAT_BANDS, WOUND_QUANTITIES)
        refused.append(bad_quantity)
    assert refused == ["hit_points", "wound_count", "Wounds"], "a mutation loop that did not loop"


@pytest.mark.parametrize("mutate, exc, why", [
    (lambda r: r["edges"].pop("Wounded"), Unspecified, "a band with no edge"),
    (lambda r: r["edges"].pop("Felled"), Unspecified, "a band with no edge"),
    (lambda r: r["edges"].update(Untouched={"quantity": "wounds", "above": 0}), Forbidden,
     "an edge on the residual band"),
    (lambda r: r["edges"].update(Decisive={"quantity": "wounds", "above": 0}), Forbidden,
     "an edge on a band the roster does not carry (the forbidden fourth band)"),
    (lambda r: r["edges"].update(Wounded={"quantity": "wounds", "above": -1}), Unspecified,
     "a negative threshold"),
    (lambda r: r["edges"].update(Wounded={"quantity": "wounds", "above": True}), Unspecified,
     "a bool threshold (a typo for a count)"),
    (lambda r: r["edges"].update(Wounded={"quantity": "wounds", "above": "hit_points"}),
     Unspecified, "a threshold naming a quantity the tracker does not return"),
    (lambda r: r["edges"].update(Wounded={"quantity": "wounds"}), Unspecified,
     "an edge with no threshold"),
    (lambda r: r.update(keyed_on="field_degree_bands"), Forbidden,
     "keyed on a roster the bands did not come from"),
    (lambda r: r.update(edges={}), Unspecified, "an empty mapping"),
])
def test_every_malformed_edge_refuses_at_load(mutate, exc, why):
    row = _row()
    mutate(row)
    with pytest.raises(exc):
        load_combat_band_edges(row, COMBAT_BANDS, WOUND_QUANTITIES)


def test_an_absent_row_refuses_rather_than_falling_back_to_the_old_literal():
    with pytest.raises(Unspecified, match="not in rosters.yaml"):
        load_combat_band_edges(None, COMBAT_BANDS, WOUND_QUANTITIES)


# --- 3. THE SHIPPED EDGES ARE THE OLD LITERAL --------------------------------------------------------

def test_the_shipped_edges_reproduce_the_old_literal_exactly_over_a_grid():
    """FALSIFIER (iii), part 1: every combination of felled x wounds x max_wounds x health, with the
    oracle being the old two-line function. `checked` is asserted so a grid that collapsed to nothing
    cannot pass."""
    checked, seen = 0, set()
    for felled, wounds, mw, hr in itertools.product(
            (False, True), range(0, 6), range(1, 5), (0, 1, 50, 200)):
        st = dict(available=True, felled=felled, wounds=wounds, max_wounds=mw,
                  health_remaining=hr, health_full=200)
        got = combat_degree(dict(wound_state={"x": st}), "x")
        assert got == _old_literal(st), st
        seen.add(got)
        checked += 1
    assert checked == 2 * 6 * 4 * 4
    assert seen == set(COMBAT_BANDS), f"the grid did not reach every band: {seen}"


@needs_engine
def test_the_shipped_edges_reproduce_the_old_literal_on_real_fights():
    """FALSIFIER (iii), part 2: real scenes, every fought subject, both the direct and the
    fixture-carrying route. `fought` counts subjects actually graded."""
    fought, bands = 0, set()
    for n in range(12):
        raw = _scene(f"we{n}")
        for subject, st in raw["wound_state"].items():
            want = _old_literal(st)
            assert combat_degree(raw, subject) == want
            assert degree_of(raw, subject, DEFAULT_FIXTURES) == want
            assert degree_of(raw, subject, DEFAULT_FIXTURES.sweep("combat_wounded_above", 0)) == want
            fought += 1
            bands.add(want)
    assert fought == 24
    assert {FELLED, WOUNDED} <= bands, f"the real scenes never reached both fought bands: {bands}"


# --- 2. THE EDGE AT `wounds > max_wounds` ------------------------------------------------------------

@needs_engine
def test_an_edge_at_max_wounds_grades_the_standing_subject_below_the_cap_untouched():
    """PLAN POSITION 8'S FALSIFIER (ii), AT THE `max_wounds` ARM. On the scene `test_we_the_band_is_read_off_the_subject_and_
    not_off_the_loser` names (`we0`: `p_low` is felled, `p_mid` stands with wounds), the shipped edge
    reads `p_mid` `Wounded`; at `wounds > max_wounds` it reads `Untouched`. The `Felled` edge is the
    engine's own verdict and is NOT swept, so `p_low` stays `Felled` -- the claim is about every
    STANDING fought subject, and `standing >= 1` is asserted.

    The precondition that makes the edge empty on this scene is asserted rather than assumed:
    `WoundTracker.wounds` is capped at `max_wounds + 1`, so `wounds > max_wounds` is NOT 'never' --
    it holds for a standing subject who reached the cap -- and `p_mid` has not. THIS TEST IS THEREFORE NOT
    THE UNIVERSAL CLAIM: the universal one (every STANDING fought subject, over the 24 real ones) is
    `test_an_unreachable_arm_grades_every_standing_fought_subject_untouched`, and the cap case is
    `test_a_standing_subject_at_the_wound_cap_still_reads_wounded_at_max_wounds`."""
    raw = _scene("we0")
    fx = DEFAULT_FIXTURES.sweep("combat_wounded_above", "max_wounds")
    standing = 0
    for subject, st in raw["wound_state"].items():
        if st["felled"]:
            assert degree_of(raw, subject, fx) == FELLED, st
            continue
        assert st["wounds"] > 0, "the control: this subject is Wounded at the shipped edge"
        assert degree_of(raw, subject, DEFAULT_FIXTURES) == WOUNDED
        assert not st["wounds"] > st["max_wounds"], "the precondition: below the cap"
        assert degree_of(raw, subject, fx) == UNTOUCHED, st
        assert combat_degree(raw, subject, "max_wounds") == UNTOUCHED
        standing += 1
    assert standing >= 1, "no standing fought subject was graded -- the assertions above were vacuous"
    assert len(raw["wound_state"]) == 2


@needs_engine
def test_a_standing_subject_at_the_wound_cap_still_reads_wounded_at_max_wounds():
    """`WoundTracker.wounds` is capped at `max_wounds + 1`, and felling needs `health_full` worth of
    damage, so a STANDING subject can hold `wounds > max_wounds`. At the `max_wounds` arm that subject
    still reads `Wounded` -- the arm is not an empty band, which is why the universal falsifier uses an
    arm above the cap. A hand-built state, so the claim does not depend on which scenes the corpus
    happens to fight."""
    for mw in (1, 2, 3):
        st = dict(available=True, felled=False, wounds=mw + 1, max_wounds=mw,
                  health_remaining=100, health_full=200)
        raw = dict(wound_state={"x": st})
        assert combat_degree(raw, "x", "max_wounds") == WOUNDED, st
        assert combat_degree(raw, "x", mw + 1) == UNTOUCHED, st
        below = dict(st, wounds=mw)
        assert combat_degree(dict(wound_state={"x": below}), "x", "max_wounds") == UNTOUCHED, below


@needs_engine
def test_an_unreachable_arm_grades_every_standing_fought_subject_untouched():
    """PLAN POSITION 8'S FALSIFIER (ii), UNIVERSAL. `wounds` never exceeds `MAXWOUNDS_CAP + 1 = 4`, so an
    edge at `wounds > 4` is unreachable: every STANDING fought subject, over all twelve real scenes (24
    subjects), grades `Untouched`; a felled subject stays `Felled` (the Felled edge is the engine's
    verdict and is not swept). `fought` and `standing` are asserted so the loop cannot pass vacuously,
    and the precondition (no subject above 4 wounds) is asserted, not assumed."""
    fx = DEFAULT_FIXTURES.sweep("combat_wounded_above", 4)
    fought = standing = felled = 0
    for n in range(12):
        raw = _scene(f"we{n}")
        for subject, st in raw["wound_state"].items():
            fought += 1
            assert st["wounds"] <= 4, f"the precondition: wounds never exceeds the cap + 1: {st}"
            if st["felled"]:
                assert degree_of(raw, subject, fx) == FELLED, st
                felled += 1
                continue
            assert degree_of(raw, subject, fx) == UNTOUCHED, st
            assert combat_degree(raw, subject, 4) == UNTOUCHED, st
            standing += 1
    assert fought == 24
    assert standing >= 1 and felled >= 1, (standing, felled)


@needs_engine
def test_the_swept_arms_move_the_band_and_the_default_arm_is_the_roster():
    """The three arms `H-98` declares, on one scene: `None` and `0` are the shipped edge (identical),
    `1` and `max_wounds` are not the same arm -- so the sweep can differ, which is what makes it a
    sweep. Found on whichever of the first scenes has a standing subject with exactly one wound; the
    count of such subjects is asserted, not hoped for."""
    one_wound = 0
    for n in range(24):
        raw = _scene(f"we{n}")
        for subject, st in raw["wound_state"].items():
            if st["felled"]:
                continue
            base = degree_of(raw, subject, DEFAULT_FIXTURES)
            assert degree_of(raw, subject, DEFAULT_FIXTURES.sweep("combat_wounded_above", 0)) == base
            if st["wounds"] == 1:
                one_wound += 1
                assert base == WOUNDED
                assert combat_degree(raw, subject, 1) == UNTOUCHED     # one wound is not enough
                assert combat_degree(raw, subject, 0) == WOUNDED
    assert one_wound >= 1, "no scene gave a standing subject exactly one wound; the arm is unobserved"


def test_a_bad_arm_refuses_instead_of_reading_a_quantity_nobody_returned():
    raw = dict(wound_state={"x": dict(available=True, felled=False, wounds=1, max_wounds=2,
                                      health_remaining=5, health_full=9)})
    refused = 0
    for bad in ("hit_points", -1, True, 1.5):
        with pytest.raises(Unspecified, match="above"):
            combat_degree(raw, "x", bad)
        refused += 1
    assert refused == 4
    # the control: the same state at a good arm answers
    assert combat_degree(raw, "x", "max_wounds") == UNTOUCHED
    assert combat_degree(raw, "x") == WOUNDED


def test_a_scene_that_does_not_lift_a_quantity_an_edge_reads_refuses():
    st = dict(available=True, felled=False, wounds=1)          # no `max_wounds`
    raw = dict(wound_state={"x": st})
    assert combat_degree(raw, "x") == WOUNDED                   # the shipped edges read only `wounds`
    with pytest.raises(Unspecified, match="max_wounds"):
        combat_degree(raw, "x", "max_wounds")


# --- 4. THE FIXTURE REACHES THE FOLD, AND `_state` LIFTS THE ROSTER'S LIST -----------------------------

@needs_engine
def test_the_swept_fixture_reaches_the_fold():
    """The same act folded at two arms writes at two bands: through the driver, so the fixture is read
    where `loop/resolve.py` hands it to `degree_of`, not only where a test hands it directly."""
    degrees = {}
    for arm in (None, "max_wounds"):
        w = P.tiny_world()
        w.step = Step.RESOLVE
        w.fixtures = DEFAULT_FIXTURES.sweep("combat_wounded_above", arm)
        d = SeasonDriver(w)
        evs = d.resolve(mint_token(d.w, WriteClass.ACTS),
                        [Act(id="we0", actor="p_low", verb="fight", payload={"subject": "p_mid"})], 2)
        degrees[arm] = [e.degree for e in evs]
        assert w.fixtures.reads.get("combat_wounded_above", 0) >= 1, "the fixture was never read"
    assert degrees[None] == [WOUNDED], degrees
    assert degrees["max_wounds"] != degrees[None], degrees


@needs_engine
def test_state_lifts_exactly_the_rosters_quantities_in_order():
    raw = _scene("we0")
    for subject, st in raw["wound_state"].items():
        assert list(st) == ["available", *WOUND_QUANTITIES], (subject, list(st))
        assert type(st["felled"]) is bool
        assert all(type(st[q]) is int for q in WOUND_QUANTITIES if q != "felled")
    assert len(raw["wound_state"]) == 2


@needs_engine
def test_a_roster_quantity_the_tracker_does_not_carry_refuses_by_name_at_the_scene():
    with mock.patch.object(C, "WOUND_QUANTITIES", (*WOUND_QUANTITIES, "hit_points")):
        w = P.tiny_world()
        w.step = Step.RESOLVE
        with pytest.raises(Unspecified, match="hit_points"):
            contest(w, "R", "the body", ["p_low", "p_mid"], 0, 2, ["we0"])
