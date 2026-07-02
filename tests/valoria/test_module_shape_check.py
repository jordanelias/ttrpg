"""Unit tests for tools/ci_module_shape_check.py (ED-1085) — the container/shape hygiene
guard. Synthetic-tree cases: each writes a tiny runtime layout into tmp_path and points the
checker at it, so the rules are tested independent of the live repo's state."""
import os
import sys
import textwrap

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
import ci_module_shape_check as shape  # noqa: E402


def _run_on(tmp_path, files):
    """Write {relpath: source} under tmp_path and run the checker against it."""
    for rel, src in files.items():
        p = tmp_path / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(textwrap.dedent(src), encoding='utf-8')
    old_root = shape.REPO_ROOT
    shape.REPO_ROOT = str(tmp_path)
    try:
        return shape.check(verbose=False)
    finally:
        shape.REPO_ROOT = old_root


def test_clean_runtime_passes(tmp_path):
    v = _run_on(tmp_path, {
        'sim/autoload/clean.py': """
            import math
            def f(x):
                return math.sqrt(x)
        """,
    })
    assert v == []


def test_sys_path_reach_in_flagged(tmp_path):
    v = _run_on(tmp_path, {
        'sim/personal/leaky.py': """
            import sys, os
            sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../tests/sim/v32-combat-balance'))
        """,
    })
    assert len(v) == 1 and 'reach-in' in v[0]


def test_tests_package_import_flagged(tmp_path):
    v = _run_on(tmp_path, {
        'engine/mod.py': """
            from tests.sim import thing
        """,
    })
    assert len(v) == 1 and 'import from tests/' in v[0]


def test_workbench_and_tests_excluded(tmp_path):
    v = _run_on(tmp_path, {
        'designs/scene/combat_engine_v1/workbench/harness.py': """
            import sys, os
            sys.path.insert(0, 'tests/sim/v32-combat-balance')  # measurement harness: allowed
        """,
        'sim/tests/test_x.py': """
            import sys
            sys.path.insert(0, 'tests/sim/v32-combat-balance')
        """,
    })
    assert v == []


def test_non_tests_path_insert_allowed(tmp_path):
    v = _run_on(tmp_path, {
        'designs/scene/combat_engine_v1/core_like.py': """
            import sys, os
            sys.path.insert(0, os.path.dirname(__file__))
        """,
    })
    assert v == []
