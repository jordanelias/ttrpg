"""Guard the retired-tree pointer scanner in tools/observability/build_incompleteness.py.

ED-IN-0086 (finding: ED-IN-0085). Two things needed pinning, and neither was observable before:

1. **Coverage that cannot fire.** `RETIRED_TREES` was `("designs/",)` and the scan regex ended in
   a literal `\\.md`. Adding `sim/` to the tuple without widening the extension set would have
   produced an entry that could never match anything — the retired `designs/` tree was design DOCS,
   but the retired `sim/` tree was PYTHON. That reads as coverage while catching nothing, which is
   exactly what CLAUDE.md §0.1 point 2 forbids: "an assertion must be able to observe the failure
   it excludes." So the positive cases below are load-bearing, not decorative.

2. **Three live look-alike trees.** `tests/sim/`, `tests/sim_framework/`, and
   `systems/<subsystem>/sim/` are all live and all unrelated to the retired top-level `sim/`
   (CLAUDE.md §3 warns about this confusion by name). A bare `sim/` alternation would report every
   one of them as a stale pointer, burying the real findings under false positives. The negative
   cases pin the lookbehind that prevents it.

If a future retirement adds a tree to `RETIRED_TREES`, add a positive case here for a file
extension that tree actually contains — otherwise the entry is decorative.
"""
import importlib.util
import os
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
TARGET = os.path.join(ROOT, 'tools', 'observability', 'build_incompleteness.py')


def _module():
    """Import the generator without running it (it writes artifacts at import-time on some paths)."""
    spec = importlib.util.spec_from_file_location('_bi_under_test', TARGET)
    mod = importlib.util.module_from_spec(spec)
    sys.modules['_bi_under_test'] = mod
    try:
        spec.loader.exec_module(mod)
    except SystemExit:
        pass
    return mod


MUST_MATCH = [
    ('designs/scene/combat_v30.md', 'retired designs/ tree, markdown'),
    ('designs/audit/some_report.yaml', 'retired designs/ tree, yaml'),
    ('sim/personal/contest.py', 'retired sim/ tree, python'),
    ('sim/provincial/faction_action.py', 'retired sim/ tree, python'),
    ('sim/substrate/keys.py', 'retired sim/ tree, python'),
]

MUST_NOT_MATCH = [
    ('tests/sim/v32-combat-balance/m1_dice_sigma_core.py', 'tests/sim/ is LIVE and unrelated'),
    ('tests/sim_framework/runner.py', 'tests/sim_framework/ is LIVE and unrelated'),
    ('systems/combat/sim/core.py', 'systems/<sub>/sim/ is the LIVE per-subsystem sim home'),
    ('engine/substrate/keys.py', 'engine/ is where the retired sim core moved TO'),
    ('systems/threadwork/sim/thread.py', 'another LIVE per-subsystem sim'),
]


@pytest.mark.parametrize('path,why', MUST_MATCH)
def test_retired_paths_are_detected(path, why):
    assert _module()._RETIRED_RE.search(path), (
        f"{path} should be flagged as a retired-tree pointer ({why}). A RETIRED_TREES entry whose "
        f"extension set cannot match that tree's real files is coverage that never fires.")


@pytest.mark.parametrize('path,why', MUST_NOT_MATCH)
def test_live_lookalike_trees_are_not_flagged(path, why):
    assert not _module()._RETIRED_RE.search(path), (
        f"{path} must NOT be flagged ({why}). CLAUDE.md §3 warns these are different things from "
        f"the retired top-level sim/; matching them buries real findings in false positives.")


def test_every_retired_tree_has_a_matching_positive_case():
    """A tree in RETIRED_TREES with no positive case above is untested coverage."""
    trees = _module().RETIRED_TREES
    covered = {t for t in trees if any(p.startswith(t) for p, _ in MUST_MATCH)}
    missing = sorted(set(trees) - covered)
    assert not missing, (
        f"RETIRED_TREES entries with no positive test case: {missing}. Add one using a file "
        f"extension that tree actually contained, or the entry cannot be shown to work.")
