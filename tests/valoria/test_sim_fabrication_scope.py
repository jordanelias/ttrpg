"""The anti-fabrication gate must be able to SEE the oracle it guards (2026-08-01).

CLAUDE.md §7 leans on `tools/ci_sim_fabrication_check.py` as the guard on the 1:1 Python
reference the Godot port validates against. Measured on 2026-08-01, it matched **0 of 117** .py
files in that reference and printed `[SIM-FABRICATION OK] no changed sim .py files — nothing to
check.` over all of it.

Nothing was wrong with the code. `is_sim_file()` asked "does the BASENAME contain 'sim'", which was
a fine proxy while the oracle lived under `sim/` — every path did. `sim/` was retired 2026-07-21 and
its contents moved to `engine/` and `systems/<subsystem>/sim/`, where no basename contains "sim"
(`massbattle.py`, `mc_v18.py`, `resolver.py`). The proxy became a predicate for nothing. That is the
§0.1 point-5 signature: correct when written, broken by a move somewhere else.

Per point 5, a sweep needs a guard that fails on recurrence, and the guard is what makes grep's
blind spots tolerable. These tests are that guard. They derive the expected scope from
`ci_common.sim_reference_prefixes()` — the declared ONE OWNER — so a future subsystem added there is
covered the day it lands, with no edit here.
"""
import glob
import importlib.util
import os
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
TOOLS = os.path.join(ROOT, 'tools')
if TOOLS not in sys.path:
    sys.path.insert(0, TOOLS)


def _load():
    spec = importlib.util.spec_from_file_location(
        'ci_sim_fabrication_check', os.path.join(TOOLS, 'ci_sim_fabrication_check.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _live_oracle_files():
    """Every .py in the sim reference, per the single owner. Not a hardcoded list."""
    import ci_common
    out = []
    for prefix in ci_common.sim_reference_prefixes(ROOT):
        for p in glob.glob(os.path.join(ROOT, prefix, '**', '*.py'), recursive=True):
            rel = os.path.relpath(p, ROOT).replace(os.sep, '/')
            if rel.startswith('engine/tests/'):
                continue  # the oracle's own regression suite, excluded deliberately
            out.append(rel)
    return sorted(set(out))


# ─────────────────────────────────────────────────────────────────────── scope

def test_the_live_oracle_is_not_empty():
    """Guards the guard. Every assertion below passes vacuously over an empty file list — which
    is the same shape as the defect they exist to catch."""
    files = _live_oracle_files()
    assert len(files) > 50, f"only {len(files)} oracle files found — the derivation is broken"


def test_every_live_oracle_file_is_visible_to_the_gate():
    """THE REGRESSION. This is the assertion that was false for eleven days."""
    mod = _load()
    missed = [p for p in _live_oracle_files() if not mod.is_sim_file(p)]
    assert not missed, (
        f"{len(missed)} sim-reference file(s) invisible to the anti-fabrication gate — it would "
        f"report OK over them. First few: {missed[:5]}")


def test_a_basename_heuristic_would_still_see_none_of_it():
    """Pins WHY, not just that. If this ever fails, the oracle moved somewhere the old proxy
    happens to match again, and this file's reasoning needs re-reading rather than deleting."""
    def old_predicate(path):
        return 'sim' in path.rsplit('/', 1)[-1].lower()
    assert not [p for p in _live_oracle_files() if old_predicate(p)]


@pytest.mark.parametrize('path,expected', [
    ('systems/mass_battle/sim/massbattle.py', True),
    ('engine/mc_v18.py', True),
    ('engine/substrate/keys.py', True),
    ('tests/sim/mass_battle/bat.py', True),      # frozen, but was already in scope — not dropped
    ('engine/tests/test_pipeline_reach.py', False),  # the oracle's own tests, excluded on purpose
    ('tools/ci_sim_fabrication_check.py', False),    # validators are not reference code
    ('deprecated/tools/old_sim.py', False),          # archival, never gated
    ('systems/mass_battle/mass_battle_v30.md', False),
])
def test_predicate_boundaries(path, expected):
    assert _load().is_sim_file(path) is expected


# ────────────────────────────────────────────── added-line scoping, in both directions

def test_a_new_uncited_constant_is_caught():
    mod = _load()
    content = "SPEED = 3\nMAGIC_THRESHOLD = 3.71828\n"
    genuine = mod.genuine_violations_by_pair(content, {}, set())
    kept, _ = mod.added_only(genuine, ["MAGIC_THRESHOLD = 3.71828"])
    assert any('3.71828' in str(g[2]) or '3.71828' in g[1] for g in kept), \
        "a fabricated constant on an added line was not gated"


def test_pre_existing_debt_is_separated_rather_than_gated_or_dropped():
    """Both halves matter: untouched debt must not FAIL the build, and must not VANISH either —
    main() prints the carried count on every run precisely so it cannot go quiet."""
    mod = _load()
    content = "OLD = 987654\nNEW = 123456\n"
    genuine = mod.genuine_violations_by_pair(content, {}, set())
    assert len(genuine) >= 2, "fixture does not produce the violations this test reasons about"
    kept, carried = mod.added_only(genuine, ["NEW = 123456"])
    assert [g[1].strip() for g in kept] == ["NEW = 123456"]
    assert [g[1].strip() for g in carried] == ["OLD = 987654"]


def test_no_added_lines_means_nothing_is_gated_and_everything_is_carried():
    """The pure-rename case the gate already exempts, now expressed in the scoping primitive."""
    mod = _load()
    genuine = mod.genuine_violations_by_pair("OLD = 987654\n", {}, set())
    kept, carried = mod.added_only(genuine, [])
    assert kept == [] and len(carried) == len(genuine)


def test_full_scan_still_sees_more_than_the_gated_view():
    """`--full` must remain a real burn-down instrument, not an alias of the gated view."""
    mod = _load()
    content = "OLD = 987654\nNEW = 123456\n"
    genuine = mod.genuine_violations_by_pair(content, {}, set())
    kept, _ = mod.added_only(genuine, ["NEW = 123456"])
    assert len(genuine) > len(kept)
