"""The ED-citation gate must scan the corpus it claims to, WITHOUT starving its own ledger universe.

Two defects, one of them mine, and the second is the reason this file exists at all.

DEFECT 1 (pre-existing). `_walk_repo_files()` walked a hardcoded
`('canon','designs','params','references','archives','deprecated')`. Three of those six were gone:
`designs/` retired 2026-07-19, `params/` moved to `engine/params/` 2026-07-16, `archives/` merged
into `deprecated/archives/` 2026-07-16. `systems/` and `engine/params/` HAD been added to
SCAN_PREFIXES — but SCAN_PREFIXES only filters what the walker yields, so 205 subsystem docs were
never produced. Measured 2026-08-01: a BLOCKING gate scanned 45 files believing it covered 293.

DEFECT 2 (introduced by fixing defect 1, caught by measuring against a pre-change control). The
same walker also fed `load_ed_universe()`. Deriving it from SCAN_PREFIXES dropped
`deprecated/archives/editorials/` from the walk, the universe fell 1167 -> 1107, and 110 perfectly
valid citations became NONEXISTENT — a gate that would have failed the build loudly and wrongly.
One function was answering two unrelated questions and only worked because the stale list happened
to be a superset of both.

So the tests below pin BOTH directions at once: scope must not shrink, and the universe must not
shrink either. Either alone would have passed while the other was broken.
"""
import importlib.util
import os
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
TOOLS = os.path.join(ROOT, 'tools')


@pytest.fixture(scope='module')
def ved():
    cwd = os.getcwd()
    os.chdir(ROOT)               # the tool resolves paths relative to the repo root
    if TOOLS not in sys.path:
        sys.path.insert(0, TOOLS)
    spec = importlib.util.spec_from_file_location(
        'validate_ed_citations', os.path.join(TOOLS, 'validate_ed_citations.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    yield mod
    os.chdir(cwd)


# ─────────────────────────────────────────────────────────────────── defect 1: the audit scope

def test_the_subsystem_corpus_is_actually_scanned(ved):
    """THE REGRESSION. `systems/` was in SCAN_PREFIXES and yielded nothing for ~13 days."""
    docs = ved.select_docs()
    n_systems = sum(1 for p in docs if p.startswith('systems/'))
    assert n_systems > 150, (
        f"only {n_systems} systems/ doc(s) scanned — the walker is not producing the subsystem "
        f"corpus, so the gate is passing over it")


def test_engine_params_is_scanned(ved):
    docs = ved.select_docs()
    assert any(p.startswith('engine/params/') for p in docs), \
        "engine/params/ is declared in SCAN_PREFIXES but produces nothing"


def test_scope_is_derived_from_the_declared_prefixes_not_a_second_list(ved):
    """Every scanned doc must sit under a declared prefix. A path outside them means a second,
    undeclared source list has grown back."""
    stray = [p for p in ved.select_docs() if not p.startswith(ved.SCAN_PREFIXES)]
    assert not stray, f"scanned paths outside SCAN_PREFIXES: {stray[:5]}"


def test_a_retired_prefix_is_tolerated_rather_than_fatal(ved):
    """`designs/` is still listed and no longer exists; that must yield nothing, not crash."""
    assert not os.path.isdir(os.path.join(ROOT, 'designs'))
    assert not [p for p in ved.select_docs() if p.startswith('designs/')]


# ──────────────────────────────────────────── defect 2: the universe must not starve

def test_the_ed_universe_still_contains_archived_ids(ved):
    """THE BUG THE SCOPE FIX INTRODUCED. Archived EDs are legitimately citable (ED-IN-0075), so
    losing the archives turns valid citations into NONEXISTENT and fails the build wrongly."""
    u = ved.load_ed_universe(warn=False)
    assert len(u) > 1150, f"ED universe collapsed to {len(u)} — archive loading is starved"
    # ED-391 lives ONLY in deprecated/archives/editorials/, i.e. outside SCAN_PREFIXES entirely
    assert u.get('ED-391') == 'resolved', "archive-only ids are missing from the universe"


def test_the_two_walks_are_independent(ved):
    """The archive walk must not be reachable from the audit scope, or the coupling returns."""
    archive = ved._walk_archive_files()
    assert archive, "archive walk yields nothing"
    assert all(p.startswith(ved.ARCHIVE_GLOBS) for p in archive)
    # and the audit scope must contain none of it (deprecated/ is skipped there)
    assert not (set(archive) & set(ved.select_docs()))


def test_the_live_tree_has_no_nonexistent_citations(ved):
    """A NONEXISTENT anywhere in the corpus is a broken reference, never deferred. This is the
    assertion that would have caught defect 2 on its own."""
    status = ved.load_ed_universe(warn=False)
    docs = {p: ved._read(p) for p in ved.select_docs()}
    docs = {p: c for p, c in docs.items() if c is not None}
    viols = ved.audit_citations(docs, status, checked_prefixes=('ED',))
    dead = [v for v in viols if v['kind'] == 'NONEXISTENT']
    assert not dead, f"{len(dead)} citation(s) resolve to no ledger entry: {dead[:3]}"


# ──────────────────────────────────────────────────────────── the burn-down tier is a ratchet

def test_the_burn_down_ceiling_matches_reality(ved):
    """Forces the ceiling DOWN as debt is paid. Without this the pin drifts above the real count
    and silently re-opens room for new debt — a ratchet that only ever ratchets is not one."""
    status = ved.load_ed_universe(warn=False)
    docs = {p: ved._read(p) for p in ved.select_docs()}
    docs = {p: c for p, c in docs.items() if c is not None}
    viols = ved.audit_citations(docs, status, checked_prefixes=('ED',))
    burn = [v for v in viols
            if v['kind'] == 'OPEN_AS_BASIS' and v['path'].startswith(ved.BURN_DOWN_PREFIXES)]
    assert len(burn) == ved.BURN_DOWN_MAX, (
        f"BURN_DOWN_MAX is {ved.BURN_DOWN_MAX} but {len(burn)} finding(s) exist. If you PAID debt, "
        f"lower the pin in tools/validate_ed_citations.py. If you ADDED debt, don't.")


def test_deferral_covers_open_as_basis_only_and_never_a_broken_reference(ved):
    """A NONEXISTENT id inside a burn-down tree must still fail: it is broken, not undecided.

    Calls ved.is_deferred directly. An earlier version of this test re-implemented the predicate
    inline and therefore passed while the real one was mutated to defer NONEXISTENT as well —
    mutation-checked, which is the only reason that was noticed.
    """
    assert ved.BURN_DOWN_PREFIXES, "the deferral set is empty; this test would be vacuous"
    inside = ved.BURN_DOWN_PREFIXES[0] + 'x.md'
    assert ved.is_deferred({'kind': 'OPEN_AS_BASIS', 'path': inside}) is True
    assert ved.is_deferred({'kind': 'NONEXISTENT', 'path': inside}) is False
    assert ved.is_deferred({'kind': 'OPEN_AS_BASIS', 'path': 'canon/x.md'}) is False
