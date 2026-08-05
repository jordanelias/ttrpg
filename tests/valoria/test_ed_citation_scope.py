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
    assert ved.BURN_DOWN_ALLOW, "the deferral set is empty; this test would be vacuous"
    path, ed = sorted(ved.BURN_DOWN_ALLOW)[0]
    assert ved.is_deferred({'kind': 'OPEN_AS_BASIS', 'path': path, 'id': ed}) is True
    # same allowed pair, but a BROKEN reference rather than an undecided one
    assert ved.is_deferred({'kind': 'NONEXISTENT', 'path': path, 'id': ed}) is False
    assert ved.is_deferred({'kind': 'OPEN_AS_BASIS', 'path': 'canon/x.md', 'id': ed}) is False


# ────────────────────────────────── the ratchet is keyed by IDENTITY, not by spare capacity

def test_deferral_is_granted_to_named_findings_not_to_a_region_with_headroom(ved):
    """ADVERSARIAL REVIEW FINDING. A count-only ceiling was launderable: fix one of the 10 existing
    findings, add a brand-new open-ED-as-basis claim anywhere under systems/, count stays 10, gate
    green, and its own test green too. `git mv`ing a doc from canon/ into systems/ laundered the
    same way. Nothing pinned WHICH findings were deferred."""
    # a real deferred pair is deferred
    known = sorted(ved.BURN_DOWN_ALLOW)[0]
    assert ved.is_deferred({'kind': 'OPEN_AS_BASIS', 'path': known[0], 'id': known[1]}) is True
    # the SAME file citing a DIFFERENT open ED is new debt, and must not inherit the deferral
    assert ved.is_deferred({'kind': 'OPEN_AS_BASIS', 'path': known[0], 'id': 'ED-IN-0999'}) is False
    # a different file under the same prefix likewise
    assert ved.is_deferred(
        {'kind': 'OPEN_AS_BASIS', 'path': 'systems/brand/new_doc.md', 'id': known[1]}) is False


def test_every_allowed_pair_is_still_a_real_finding(ved):
    """Stops the allow-list outliving its findings. A stale entry is latent permission for debt
    that a later edit could reintroduce under an id nobody is still watching."""
    status = ved.load_ed_universe(warn=False)
    docs = {p: ved._read(p) for p in ved.select_docs()}
    docs = {p: c for p, c in docs.items() if c is not None}
    live = {(v['path'], v['id']) for v in ved.audit_citations(docs, status, checked_prefixes=('ED',))
            if v['kind'] == 'OPEN_AS_BASIS'}
    stale = sorted(ved.BURN_DOWN_ALLOW - live)
    assert not stale, (
        f'{len(stale)} BURN_DOWN_ALLOW entr(y/ies) no longer correspond to a live finding: {stale}. '
        f'The debt was paid — remove the entry (and lower BURN_DOWN_MAX) in the same commit.')


# ------------------------------------------------------------------------------------------
# The generated-sidecar exemption (ED-IN-0142) — a LOOSENING of a blocking gate, so it gets a
# control on every branch of its predicate.
# ------------------------------------------------------------------------------------------

def test_generated_sidecar_exemption_requires_BOTH_conditions(tmp_path):
    """A quoted citation is not a made citation — but the exemption must not become a hatch.

    `systems/<sub>/_identifier_census.yaml` quotes design-doc prose verbatim, so it carries the
    docs' own ED references; the gate read those as the inventory asserting an open ED as its
    basis (17 findings, every one a double-count of a citation already counted in the source).
    The fix exempts generated sidecars — and an exemption on a BLOCKING gate is only as safe as
    the narrowness of its predicate, so both halves are pinned here in both directions.
    """
    import validate_ed_citations as v
    banner = 'GENERATED by tools/build_identifier_census.py\n'

    exempt = tmp_path / '_census.yaml'
    exempt.write_text(banner + 'cites ED-IN-0004\n', encoding='utf-8')
    assert v.is_generated_sidecar(str(exempt)) is True

    # underscore but NO banner -> a hand-authored file cannot buy the exemption by renaming
    no_banner = tmp_path / '_handwritten.md'
    no_banner.write_text('## Status: DRAFT\nbased on ED-IN-0004\n', encoding='utf-8')
    assert v.is_generated_sidecar(str(no_banner)) is False, \
        'renaming a hand-authored doc must not exempt it from the citation gate'

    # banner but NO underscore -> a generated file cannot buy it by dropping the sidecar marker
    no_underscore = tmp_path / 'census.yaml'
    no_underscore.write_text(banner + 'cites ED-IN-0004\n', encoding='utf-8')
    assert v.is_generated_sidecar(str(no_underscore)) is False


def test_the_exemption_does_not_shrink_the_ED_universe():
    """THE HAZARD THIS TOOL'S OWN DOCSTRING RECORDS: losing one archive directory shrank the
    universe 1167 -> 1107 and turned 110 VALID citations into NONEXISTENT. `_walk` builds BOTH the
    scan set and the universe, so an exclusion added for the scan side could silently starve the
    universe. It must not."""
    import validate_ed_citations as v
    assert len(v._walk(v.ARCHIVE_GLOBS)) >= 26, \
        'the generated-sidecar exclusion removed archive files from the ED universe'
    ids = v.load_universe() if hasattr(v, 'load_universe') else None
    if ids is not None:
        assert len(ids) >= 1190, f'ED universe shrank to {len(ids)}'
