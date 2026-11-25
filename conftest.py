"""Lane markers (`pytest -m <lane>`, the table below); and the `flat_fold` mark's fixture (`_flat_fold_arm`, below).

WHY. A change to mass battle does not need the personal-combat tests and the reverse, and most test files say
what they test in their name. This file assigns the marker from the file name, in one place, to every test
collected under the repo root (tests/valoria, engine/season/tests, engine/tests). It selects tests, nothing more: the
inner loop's (`tools/tests_for_diff.py`) and a batch close's (v12 P18):

  * `python -m pytest -m mass_battle -q -n auto` runs the mass-battle files across all three trees.
  * CI runs no `-m` filter, and `pytest.ini` says why it must not (a filter at the gate is a coverage cut).
  * It is NOT a statement of what a change can break. The season suite builds a whole realm, so its tests
    execute the combat, mass-battle and contest modules too (measured: a `modules/combat/` edit is reached by
    tests costing about three quarters of the whole suite). If a module edit could change a realm, run
    `-m season_loop` too (`tools/tests_for_diff.py`'s docstring).

MEMBERSHIP IS BY NAME, and was checked against what each file executes (coverage by test, 2026-11-04): every
`combat` file under tests/valoria executes `modules/combat` or `engine/dice_engine` and nothing in
`engine/season`; every `mass_battle` file executes `modules/mass_battle`. A file whose name does not say
which lane it tests would carry no marker, and every test has one lane: add its prefix to the table below.
"""
import os
import re

import pytest

# marker -> a pattern over the test file's base name (without `.py`). One owner of the table.
#
# EVERY TEST BELONGS TO ONE LANE (Jordan, 2026-11-22: "each lane/subsystem is to have its own test suite ... no test
# suite that doesn't concern a specific subsystem or the season loop or engine"): the SEASON LOOP (`engine/season/tests/`
# whole, plus the `tests/valoria` files below), the ENGINE (`engine/tests/` whole, plus the dice engine, substrate and
# exporters), or one subsystem. The tree decides first; in `tests/valoria` the first matching pattern decides. `process`
# marks the files that concern none of them (tool and ledger checks): it exists so they are findable, not as a suite.
SUBSYSTEM_FILES = {
    "combat": re.compile(
        r"^test_(combat_|band_extension_seam|coherence_elastic_plastic|dice_engine_properties|tn7_)"),
    "mass_battle": re.compile(
        r"^test_(mass_battle_|army_|body_|cell_|charge_|charger_|close_ranks|col_grid|conditional_orders|"
        r"deployment_|dg2_|face_aggressors|feigned_|frontage_|friction|front_fixer|hp_cell|"
        r"intent_resolution|morale_write_sweep|octagon|partition_invariance|perimeter_|reach_weapon|"
        r"rekey_cells|reserve_commit|rout_contagion|stochastic_rout|subphase_|troop_density|volley_|"
        r"casualty_attribution|march|territory_march|sides$|levy_feed)"),
    "social_contest": re.compile(
        r"^test_(sc0\d_|social_contest|stress_proceedings|settle_margin|contest_kernel)"),
    "threadwork": re.compile(r"^test_threadwork_"),
    "season_loop": re.compile(
        r"^test_(axis_roster|balance_oracle|conviction_roster|export_season_registries|import_cycle|m1_acceptance|"
        r"module_registrar|modules_reachable|season_)"),
    "engine": re.compile(
        r"^test_(degree_|descriptor|engine_does_not_import|engine_params|export_(game_constants|sim_params|troops)|"
        r"field_golden|fmath_|names_chain|per_die|wiring)"),
    "process": re.compile(
        r"^test_(claim_provenance|design_prose|module_shape|references_yaml|names$|no_polling|pathres|stubwire)"),
}
TREE_LANE = {"engine/season/tests/": "season_loop", "engine/tests/": "engine"}
# SUITES (Jordan, 2026-11-23: "specific lane based test suites"): a SECOND marker, beside the lane and never a lane. The subsystems'
# tests that live in `engine/season/tests/` are `season_loop` by tree, so `-m social_contest` selects none of them; each file below also
# carries its subsystem's `<lane>_season` marker, and `-m "<lane> or <lane>_season"` is that subsystem's whole suite across the three
# trees (`tools/tests_for_diff.py --suite`). Not counted by `references/test_lane_caps.yaml`: a test keeps exactly one lane.
SEASON_SUITES = {
    "sc_season": re.compile(r"^test_(sc\d|sc_|social_contest|stress_proceedings|settle_margin|contest_kernel)"),
    "mb_season": re.compile(r"^test_(march|mass_battle_|levy_feed)"),
    "pc_season": re.compile(r"^test_(combat_|cp_t\d|cl_thrust_|b11a_)"),
}


def pytest_collection_modifyitems(config, items):
    for item in items:
        path = str(item.fspath).replace(os.sep, "/")
        lane = next((l for t, l in TREE_LANE.items() if t in path), None)
        if lane is None:
            base = os.path.basename(path)[:-3]
            lane = next((m for m, pat in SUBSYSTEM_FILES.items() if pat.match(base)), None)
        if lane:
            item.add_marker(getattr(pytest.mark, lane))
        if "engine/season/tests/" in path:
            base = os.path.basename(path)[:-3]
            for suite, pat in SEASON_SUITES.items():
                if pat.match(base):
                    item.add_marker(getattr(pytest.mark, suite))


@pytest.fixture(autouse=True)
def _flat_fold_arm(request):
    """`@pytest.mark.flat_fold` (file or test): the task draw is off for the test, so a world built from the default fixtures folds flat.
    `DEFAULT_FIXTURES` is one shared object whose `sweep` copies its values at call time, so setting the one value covers every world
    the test builds, `build_realm`'s and `tiny_world`'s alike; `monkeypatch` undoes it. A MODULE- or SESSION-scoped fixture is set up
    before this one: it builds its own world through `engine/season/harness/flat_fold.py::flat_fold`. A test with no mark is untouched."""
    if request.node.get_closest_marker("flat_fold") is not None:
        from engine.season.data.fixtures import DEFAULT_FIXTURES
        from engine.season.harness.flat_fold import ARM
        DEFAULT_FIXTURES.get(ARM)      # a renamed arm raises `Ungraded` here instead of setting a dead key and leaving the draw on
        request.getfixturevalue("monkeypatch").setitem(DEFAULT_FIXTURES._v, ARM, "off")
