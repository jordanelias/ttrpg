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

_HASH_LITERAL = re.compile(r"^[0-9a-f]{32}(?:[0-9a-f]{32})?$")   # a realm content hash (32 hex) or a census digest (64 hex)
_PIN_OWNER = "engine.season.tests._realm_goldens"


_REALM_RUNNERS = frozenset({"build_realm", "run", "SeasonDriver", "build_world"})   # what builds or runs a realm


def _holds_hash(v, depth=0):
    """True for a hash literal, or a dict/tuple/list/set holding one within two levels: a module alias such as `{s: SHIPPED[(s, 1)] ...}`."""
    if isinstance(v, str):
        return bool(_HASH_LITERAL.match(v))
    if depth < 2 and isinstance(v, dict):
        return any(_holds_hash(x, depth + 1) for x in v.values())
    if depth < 2 and isinstance(v, (tuple, list, set, frozenset)):
        return any(_holds_hash(x, depth + 1) for x in v)
    return False


def _scan(fn, seen):
    """`(reads a golden, runs a realm)` for `fn` and, one level down, the same-module helpers it calls."""
    code = getattr(fn, "__code__", None)
    if code is None or code in seen:
        return False, False
    seen.add(code)
    golden = any(isinstance(c, str) and _HASH_LITERAL.match(c) for c in code.co_consts)
    runs = bool(_REALM_RUNNERS.intersection(code.co_names))
    g = getattr(fn, "__globals__", {})
    for name in code.co_names:
        v = g.get(name)
        if v is None:
            continue
        if getattr(v, "__name__", None) == _PIN_OWNER or _holds_hash(v):
            golden = True
        elif callable(v) and getattr(v, "__module__", None) == g.get("__name__"):
            a, b = _scan(v, seen)
            golden, runs = golden or a, runs or b
    return golden, runs


def _reads_pin(fn):
    """`shipped_pin` (Jordan, 2026-11-26: the shipped-output goldens are a POST-WORKPLAN gate), by IDENTITY and not by name: the test reads a
    global that IS the `_realm_goldens` module or holds a hash literal (the goldens and every alias built from them), or names an inline hash
    literal, AND builds or runs a realm (a frozen encoding vector over hand-built fixtures is a conformance check, not a pin of the shipped
    realm). A local or attribute that merely shares a golden's NAME (`Step.CENSUS`) is not a pin. Scoped to `engine/season/tests/`: a
    subsystem's own frozen digest, as `tests/valoria/test_threadwork_mending_parity.py`'s, is that subsystem's regression check and stays.
    `test_w15`, the byte-check of a derived artifact, carries the marker itself."""
    golden, runs = _scan(fn, set())
    return golden and runs

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
        r"^test_(axis_roster|balance_oracle|conviction_roster|explain$|export_season_registries|import_cycle|m1_acceptance|"
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
def _season_suites():
    """`{file stem without test_: suite}` from `references/season_test_suites.yaml`, the owner of which suite a season file belongs to."""
    import yaml
    doc = yaml.safe_load(open(os.path.join(os.path.dirname(__file__), "references", "season_test_suites.yaml")))
    return {name: f"{suite}_season" for suite, names in doc["suites"].items() for name in names}


SEASON_SUITE_OF = _season_suites()
IN_SEASON = "in_season"   # a season file the yaml does not place
SEASON_SUITES = tuple(sorted(set(SEASON_SUITE_OF.values()) | {IN_SEASON}))   # the marker names, for tools/tests_for_diff.py


def pytest_collection_modifyitems(config, items):
    for item in items:
        path = str(item.fspath).replace(os.sep, "/")
        lane = next((l for t, l in TREE_LANE.items() if t in path), None)
        if lane is None:
            base = os.path.basename(path)[:-3]
            lane = next((m for m, pat in SUBSYSTEM_FILES.items() if pat.match(base)), None)
        if lane:
            item.add_marker(getattr(pytest.mark, lane))
        if lane == "season_loop" and "engine/season/tests/" not in path:
            item.add_marker(getattr(pytest.mark, IN_SEASON))   # the registrar, the providers, the exports: cross-cutting by nature
        if "engine/season/tests/" in path:
            base = os.path.basename(path)[:-3]
            item.add_marker(getattr(pytest.mark, SEASON_SUITE_OF.get(base[len("test_"):], IN_SEASON)))
        # `shipped_pin`: the test reads a name the realm-goldens module owns (Jordan, 2026-11-26: the shipped-output pins are a
        # POST-WORKPLAN gate). Derived by what the test reads, never listed per test (`_reads_pin`).
        fn = getattr(item, "function", None)
        if fn is not None and "engine/season/tests/" in path and _reads_pin(fn):
            item.add_marker(pytest.mark.shipped_pin)


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
