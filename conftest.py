"""Subsystem markers: `pytest -m combat`, `-m mass_battle`, `-m social_contest`; and the `flat_fold` mark's fixture (`_flat_fold_arm`, below).

WHY. A change to mass battle does not need the personal-combat tests and the reverse, and most test files say
what they test in their name. This file assigns the marker from the file name, in one place, to every test
collected under the repo root (tests/valoria, engine/season/tests, engine/tests). It is an inner-loop
accelerator, nothing more:

  * `python -m pytest -m mass_battle -q -n auto` runs the mass-battle files across all three trees.
  * CI runs no `-m` filter, and `pytest.ini` says why it must not (a filter at the gate is a coverage cut).
  * It is NOT a statement of what a change can break. The season suite builds a whole realm, so its tests
    execute the combat, mass-battle and contest modules too (measured: a `modules/combat/` edit is reached by
    tests costing about three quarters of the whole suite). After a module edit run `-m <subsystem>` for the
    quick answer, then the full season suite once at the close (`CLAUDE.md` section 0.4).

MEMBERSHIP IS BY NAME, and was checked against what each file executes (coverage by test, 2026-11-04): every
`combat` file under tests/valoria executes `modules/combat` or `engine/dice_engine` and nothing in
`engine/season`; every `mass_battle` file executes `modules/mass_battle`. A file whose name does not say
which subsystem it tests carries no marker; add its prefix to the table below rather than guessing.
"""
import os
import re

import pytest

# marker -> a pattern over the test file's base name (without `.py`). One owner of the table.
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
}


def pytest_collection_modifyitems(config, items):
    for item in items:
        base = os.path.basename(str(item.fspath))[:-3]
        for marker, pat in SUBSYSTEM_FILES.items():
            if pat.match(base):
                item.add_marker(getattr(pytest.mark, marker))


@pytest.fixture(autouse=True)
def _flat_fold_arm(request):
    """`@pytest.mark.flat_fold` (file or test): the task draw is off for the test, so a world built from the default fixtures folds flat.
    `DEFAULT_FIXTURES` is one shared object whose `sweep` copies its values at call time, so setting the one value covers every world
    the test builds, `build_realm`'s and `tiny_world`'s alike; `monkeypatch` undoes it. A MODULE- or SESSION-scoped fixture is set up
    before this one: it builds its own world through `engine/season/tests/_flat_fold.py::flat_fold`. A test with no mark is untouched."""
    if request.node.get_closest_marker("flat_fold") is not None:
        from engine.season.data.fixtures import DEFAULT_FIXTURES
        from engine.season.tests._flat_fold import ARM
        DEFAULT_FIXTURES.get(ARM)      # a renamed arm raises `Ungraded` here instead of setting a dead key and leaving the draw on
        request.getfixturevalue("monkeypatch").setitem(DEFAULT_FIXTURES._v, ARM, "off")
