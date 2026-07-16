"""Unit + integration tests for the Structural Observatory's G_generation layer
(skills/valoria-vector-audit/scripts/gen_audit.py).

Per the observatory governance (see test_structure_audit.py's docstring): the
LIVE/HISTORICAL partition logic is unit-tested on synthetic fixtures with known
answers — in particular the core discriminator (an identical stale reference,
scanned only when it lives inside a LIVE head) — and at least one assertion is
pinned against the REAL corpus so the tool is proven to reuse the real
tools/ci_generation_consistency.py currency rule,
tools/broken_dependency_checker.py extractor, and
skills/valoria-vector-audit/scripts/vector_audit.py banner classifier rather
than a private reimplementation.
"""
import importlib.util
import os
import sys

import pytest

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_SCRIPT = os.path.join(_ROOT, 'skills', 'valoria-vector-audit', 'scripts', 'gen_audit.py')

# Make tools/ importable EXPLICITLY (mirrors test_pointer_audit.py / test_formula_audit.py)
# rather than relying on gen_audit.py's own sys.path side effect at load time — the
# reuse-by-identity tests below import ci_generation_consistency / broken_dependency_checker
# directly and must not depend on import order.
_TOOLS = os.path.join(_ROOT, 'tools')
if _TOOLS not in sys.path:
    sys.path.insert(0, _TOOLS)


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


ga = _load(_SCRIPT, 'gen_audit')
# gen_audit.py's own module-level `sys.path.insert(0, _SCRIPT_DIR)` (run above, as part of
# loading it) already put scripts/ on sys.path and cached 'vector_audit' in sys.modules via
# its `import vector_audit as va` — a plain `import vector_audit` here (NOT a second
# importlib.util load) hits that same cache entry, mirroring test_formula_audit.py's
# identical structure_audit cross-check.
import vector_audit as va  # noqa: E402


# ── proves real reuse (CLAUDE.md §8: "every rule lives once") ───────────────

def test_module_imports_the_real_ci_generation_consistency():
    import ci_generation_consistency as real_gc
    assert ga.gc is real_gc
    assert ga.gc.canonical_docs is real_gc.canonical_docs
    assert ga.gc.status_of is real_gc.status_of
    assert ga.gc.superseded_ids is real_gc.superseded_ids
    assert ga.gc.RECOGNIZED is real_gc.RECOGNIZED


def test_module_imports_the_real_broken_dependency_checker():
    import broken_dependency_checker as real_bdc
    assert ga.bdc is real_bdc
    assert ga.bdc.extract_file_refs is real_bdc.extract_file_refs
    assert ga.bdc.get_all_repo_files is real_bdc.get_all_repo_files
    # ED-IN-0055: detection 1's severity triage reuses the SAME restructure-ledger
    # map bdc.check_editorial_ledger() uses — proven by identity, not reimplemented.
    assert ga.bdc._load_restructure_map is real_bdc._load_restructure_map


def test_module_imports_the_real_vector_audit_banner_classify():
    assert ga.va is va
    assert ga.va.banner_classify is va.banner_classify


# ── classify() unit tests: the tie-break priority, on tiny known fixtures ───

def test_classify_live_head_when_in_live_set():
    assert ga.classify('designs/foo_v30.md', '## Status: CANONICAL\n\nBody.',
                       {'designs/foo_v30.md'}, set()) == ('live', 'canonical_head')


def test_classify_defaults_to_historical_when_not_in_live_set():
    # "when in doubt, HISTORICAL" — a doc simply absent from the live set,
    # even with content that looks like ordinary design prose, is historical.
    assert ga.classify('designs/foo_v30.md', '## Status: CANONICAL\n\nBody.',
                       set(), set()) == ('historical', 'not_a_live_head')


def test_classify_superseded_wins_even_if_in_live_set():
    assert ga.classify('designs/foo_v30.md', 'text',
                       {'designs/foo_v30.md'}, {'designs/foo_v30.md'}) == ('historical', 'superseded_id')


def test_classify_archival_path_wins_even_if_in_live_set():
    # Regression pin for the real observed tie-break (module docstring):
    # designs/audit/2026-05-17-v18-integration/integration_plan_v18.md is a
    # genuine strict-LIVE head (registered CANONICAL) yet still classifies
    # historical because it lives under designs/audit/.
    bucket, reason = ga.classify('designs/audit/x/y.md', '## Status: CANONICAL',
                                 {'designs/audit/x/y.md'}, set())
    assert bucket == 'historical'
    assert reason == 'archival_path'


def test_classify_live_head_survives_banner_discourse_false_hit():
    # ED-IN-0055 reconciliation (agonist + antagonist both flagged this): the weak
    # banner_classify CONTENT-keyword must NOT override an authoritative live-head
    # registration. Real instance: designs/factions/faction_systems_overview_v30.md
    # (a registered REFERENCE head) was demoted because "audit" appears in its Scope
    # prose. A registered head now stays LIVE even when banner_classify -> 'discourse'.
    content = 'This document is a STRESS TEST log.\n'
    relpath = 'designs/foo_v30.md'
    assert va.banner_classify(content, relpath) == 'discourse'  # sanity-check the fixture itself
    bucket, reason = ga.classify(relpath, content, {relpath}, set())
    assert bucket == 'live'
    assert reason == 'canonical_head'


def test_classify_banner_discourse_still_demotes_a_NON_registered_doc():
    # The banner heuristic is NOT removed — it still tiebreaks docs that were never
    # registered as canonical heads (its legitimate job), just no longer overrides
    # an authoritative registration.
    content = 'This document is a STRESS TEST log.\n'
    relpath = 'designs/foo_v30.md'
    assert va.banner_classify(content, relpath) == 'discourse'
    bucket, reason = ga.classify(relpath, content, set(), set())   # NOT in live_set
    assert bucket == 'historical'
    assert reason == 'banner_discourse'


def test_classify_ledger_path_is_historical():
    bucket, reason = ga.classify('registers/editorial_ledger_pc.jsonl', 'text', set(), set())
    assert bucket == 'historical'
    assert reason == 'ledger_or_register'


# ── _is_version_pointer / _leading_status_token: small pure-function pins ───

@pytest.mark.parametrize('ref,expected', [
    ('designs/scene/combat_v30.md', True),                              # plain _vNN.md
    ('designs/scene/derived_stats_v1.md', True),                        # single-digit version
    ('designs/architecture/campaign_architecture_v30_index.md', True),  # _v30_index.md
    ('designs/scene/social_contest_v30_infill.md', True),               # _v30_infill.md
    ('designs/scene/fieldwork.md', False),                              # no version suffix at all
    ('designs/scene/combat_v30.py', False),                             # not .md
    ('tools/quantity_registry.py', False),                              # not .md, no version suffix
])
def test_is_version_pointer(ref, expected):
    assert ga._is_version_pointer(ref) == expected


def test_leading_status_token_strips_trailing_annotation():
    # regression pin for the real false-positive this fixed: a status string can
    # legitimately contain the word "canonical" WITHOUT declaring itself canonical.
    assert ga._leading_status_token(
        'SUPERSEDED — canonical doc is designs/systems/npc_behavior_v30.md') == 'SUPERSEDED'
    assert ga._leading_status_token('CANONICAL') == 'CANONICAL'
    assert ga._leading_status_token('CANONICAL — approved 2026-04-17 (editorial batch).') == 'CANONICAL'
    assert ga._leading_status_token(
        'D1–D6 RATIFIED (D1-D5: ...; D6: ... is canonical, on condition ...)') == 'D1–D6 RATIFIED'


# ── the core discriminator: identical ref, LIVE flagged / HISTORICAL never ──

def test_core_discriminator_live_head_flagged_historical_never(tmp_path):
    """The whole point of the tool. Two docs carry the IDENTICAL stale
    `_v1.md` reference; only the one classified LIVE is even offered to the
    stale-pointer scan. This exercises the real pipeline shape
    (partition_corpus -> stale_pointers_in_live_heads), not a shortcut."""
    ref_line = 'See `designs/fake_target_v1.md` for details.\n'

    designs_dir = tmp_path / 'designs'
    designs_dir.mkdir()
    (designs_dir / 'fake_live_v30.md').write_text(
        '## Status: CANONICAL\n\nThis is a fake live head. ' + ref_line, encoding='utf-8')

    archives_dir = tmp_path / 'deprecated' / 'archives'
    archives_dir.mkdir(parents=True)
    (archives_dir / 'fake_historical_v30.md').write_text(
        '## Status: CANONICAL\n\nThis is a fake historical record. ' + ref_line, encoding='utf-8')

    live_set = {'designs/fake_live_v30.md'}
    partition, reason_counts, per_file_reason, live_contents = ga.partition_corpus(
        tmp_path, live_set, set())

    assert partition['live'] == ['designs/fake_live_v30.md']
    assert 'deprecated/archives/fake_historical_v30.md' in partition['historical']
    # the historical doc's content is structurally never even collected for scanning —
    # not filtered out later, never gathered in the first place.
    assert set(live_contents) == {'designs/fake_live_v30.md'}

    # the target genuinely does not exist anywhere in this fixture -> nonexistent
    all_files = {'designs/fake_live_v30.md', 'deprecated/archives/fake_historical_v30.md'}
    stale = ga.stale_pointers_in_live_heads(live_contents, all_files, set())

    assert stale == [{'live_head': 'designs/fake_live_v30.md',
                      'ref': 'designs/fake_target_v1.md', 'reason': 'nonexistent'}]
    assert not any(s['live_head'] == 'deprecated/archives/fake_historical_v30.md' for s in stale)


def test_stale_pointers_flags_superseded_target_too():
    live_contents = {'designs/live_v30.md': 'Cross-ref: `designs/old_v1.md` for background.'}
    all_files = {'designs/live_v30.md', 'designs/old_v1.md'}   # target EXISTS but is superseded
    superseded_set = {'designs/old_v1.md'}
    stale = ga.stale_pointers_in_live_heads(live_contents, all_files, superseded_set)
    assert stale == [{'live_head': 'designs/live_v30.md', 'ref': 'designs/old_v1.md', 'reason': 'superseded'}]


def test_stale_pointers_does_not_flag_a_healthy_reference():
    live_contents = {'designs/live_v30.md': 'Cross-ref: `designs/other_v30.md` for background.'}
    all_files = {'designs/live_v30.md', 'designs/other_v30.md'}
    stale = ga.stale_pointers_in_live_heads(live_contents, all_files, set())
    assert stale == []


def test_stale_pointers_moved_target_is_not_mislabeled_nonexistent():
    # ED-IN-0055 [HIGH] antagonist finding: a missing target whose restructure-ledger
    # successor EXISTS on disk is 'moved' (a trivial one-line repoint to a KNOWN
    # target), NOT 'nonexistent' (dead). In the real corpus >half of detection 1's
    # findings are this class; mislabeling them all 'dead' would waste a cleanup pass.
    live_contents = {'designs/live_v30.md': 'See `designs/old_place/thing_v30.md`.'}
    all_files = {'designs/live_v30.md', 'designs/new_place/thing_v30.md'}  # old gone, new exists
    remap = {'designs/old_place/thing_v30.md': 'designs/new_place/thing_v30.md'}
    stale = ga.stale_pointers_in_live_heads(live_contents, all_files, set(), remap)
    assert stale == [{'live_head': 'designs/live_v30.md',
                      'ref': 'designs/old_place/thing_v30.md', 'reason': 'moved',
                      'new_home': 'designs/new_place/thing_v30.md'}]


def test_stale_pointers_moved_only_when_the_successor_actually_exists():
    # A restructure-map entry whose NEW path is ALSO absent stays 'nonexistent' —
    # don't promise a trivial repoint to a target that isn't there either.
    live_contents = {'designs/live_v30.md': 'See `designs/old_place/thing_v30.md`.'}
    all_files = {'designs/live_v30.md'}   # neither old nor mapped-new exists
    remap = {'designs/old_place/thing_v30.md': 'designs/new_place/thing_v30.md'}
    stale = ga.stale_pointers_in_live_heads(live_contents, all_files, set(), remap)
    assert stale == [{'live_head': 'designs/live_v30.md',
                      'ref': 'designs/old_place/thing_v30.md', 'reason': 'nonexistent'}]


# ── unregistered-canonical detection on a synthetic fixture ─────────────────

def test_scan_unregistered_canonical_synthetic_fixture(tmp_path, monkeypatch):
    """gc.status_of() hardcodes its own repo root (gc.ROOT, computed from
    tools/ci_generation_consistency.py's __file__ at import time — see module
    docstring's disclosed limitation). Monkeypatching that one global is the
    minimal way to sandbox the REAL, unmodified status_of() against a
    synthetic fixture tree instead of the real repo — reuse-by-identity is
    preserved; only where it looks is redirected."""
    monkeypatch.setattr(ga.gc, 'ROOT', str(tmp_path))

    designs_dir = tmp_path / 'designs'
    designs_dir.mkdir()
    (designs_dir / 'true_gap_v1.md').write_text(
        '## Status: CANONICAL\n\nA real canonical doc nobody registered.\n', encoding='utf-8')
    (designs_dir / 'false_positive_v1.md').write_text(
        '## Status: SUPERSEDED — canonical doc is designs/true_gap_v1.md\n\nBody.\n', encoding='utf-8')
    (designs_dir / 'already_registered_v1.md').write_text(
        '## Status: CANONICAL\n\nBody.\n', encoding='utf-8')
    audit_dir = designs_dir / 'audit'
    audit_dir.mkdir()
    (audit_dir / 'sneaky_v1.md').write_text('## Status: CANONICAL\n\nBody.\n', encoding='utf-8')

    registered_docs = {'designs/already_registered_v1.md'}
    findings = ga.scan_unregistered_canonical(tmp_path, registered_docs)
    found_paths = {f['path'] for f in findings}

    assert 'designs/true_gap_v1.md' in found_paths
    # regression pin: "canonical" appearing inside a SUPERSEDED doc's descriptive
    # text must not trip this detection (the real npc_behavior_system_v1.md class)
    assert 'designs/false_positive_v1.md' not in found_paths
    assert 'designs/already_registered_v1.md' not in found_paths   # registered -> excluded
    assert 'designs/audit/sneaky_v1.md' not in found_paths         # designs/audit/ -> excluded

    # the genuinely-unmentioned fixture doc must land in the "never mentioned" bucket
    # (no references/canonical_sources.yaml exists under tmp_path at all)
    true_gap = next(f for f in findings if f['path'] == 'designs/true_gap_v1.md')
    assert true_gap['mentioned_in_canonical_sources_under_unrecognized_key'] is False


def test_mentioned_in_canonical_sources_raw_honors_root(tmp_path):
    refs_dir = tmp_path / 'references'
    refs_dir.mkdir()
    (refs_dir / 'canonical_sources.yaml').write_text(
        'systems:\n  foo:\n    adjacency: designs/territory/foo_v30.md\n', encoding='utf-8')
    text = ga._mentioned_in_canonical_sources_raw(tmp_path)
    assert 'designs/territory/foo_v30.md' in text


def test_mentioned_in_canonical_sources_raw_missing_file_returns_empty(tmp_path):
    assert ga._mentioned_in_canonical_sources_raw(tmp_path) == ''


# ── real-corpus smoke: end-to-end, partition sums, deterministic ───────────

@pytest.fixture(scope='module')
def real_run(tmp_path_factory):
    from pathlib import Path
    out = tmp_path_factory.mktemp('gen_audit_real_run')
    return ga.run(Path(_ROOT), out)


def test_real_corpus_smoke_runs_end_to_end(real_run):
    sc = real_run['scorecard']
    assert sc['md_files_classified'] > 1000          # sanity: real corpus, not an empty scan
    assert sc['live_head_count'] > 0
    assert sc['historical_count'] > 0


def test_real_corpus_partition_sums_to_classified_total(real_run):
    partition = real_run['partition']
    sc = real_run['scorecard']
    assert len(partition['live']) + len(partition['historical']) == sc['md_files_classified']
    assert len(partition['live']) == sc['live_head_count']
    # no file double-counted across the two buckets
    assert set(partition['live']).isdisjoint(set(partition['historical']))


def test_real_corpus_finds_the_known_combat_v30_currency_drift(real_run):
    # designs/scene/combat_v30.md is registered canonical (via some key) AND
    # recorded as a supersession_register.yaml superseded_id — a live, standing
    # instance of currency drift in this corpus as of this writing.
    assert 'designs/scene/combat_v30.md' in real_run['drift']


def test_real_corpus_finds_the_known_mass_battle_stale_pointer(real_run):
    # designs/provincial/mass_battle_integration_v30.md (a real LIVE head) cites
    # `designs/scene/combat_v30.md` (a superseded_ids() entry) — a live, standing
    # stale version-pointer in this corpus as of this writing (see module docstring).
    hits = [s for s in real_run['stale']
            if s['live_head'] == 'designs/provincial/mass_battle_integration_v30.md'
            and s['ref'] == 'designs/scene/combat_v30.md']
    assert hits and hits[0]['reason'] == 'superseded'


def test_real_corpus_stale_severity_split_sums_and_moved_targets_exist(real_run):
    # ED-IN-0055 [HIGH]: the flat 'nonexistent' bucket is split by severity. The
    # three sub-counts must sum to the total, and every 'moved' finding's new_home
    # must actually exist on disk — that existence is exactly what makes it a trivial
    # repoint rather than a hunt. (In this corpus 'moved' is the majority class.)
    sc = real_run['scorecard']
    assert (sc['stale_pointers_superseded'] + sc['stale_pointers_moved_successor_exists']
            + sc['stale_pointers_nonexistent']) == sc['stale_pointers_in_live_heads']
    import broken_dependency_checker as real_bdc
    all_files = real_bdc.get_all_repo_files()
    moved = [s for s in real_run['stale'] if s['reason'] == 'moved']
    assert moved, "expected at least one restructure-ledger 'moved' finding in the real corpus"
    for s in moved:
        assert s.get('new_home') and s['new_home'] in all_files


def test_real_corpus_never_flags_a_historical_doc_as_a_stale_pointer_source(real_run):
    # Structural guarantee, cross-checked against the real run: no finding's
    # live_head is ever a path under deprecated/archives/ or deprecated/ or designs/audit/.
    for s in real_run['stale']:
        assert not s['live_head'].startswith(('deprecated/archives/', 'deprecated/', 'designs/audit/'))


def test_real_corpus_deterministic_across_two_runs(real_run, tmp_path_factory):
    from pathlib import Path
    out2 = tmp_path_factory.mktemp('gen_audit_real_run_2')
    r2 = ga.run(Path(_ROOT), out2)
    assert real_run['scorecard'] == r2['scorecard']
    assert real_run['stale'] == r2['stale']
    assert real_run['drift'] == r2['drift']
    assert real_run['partition'] == r2['partition']
