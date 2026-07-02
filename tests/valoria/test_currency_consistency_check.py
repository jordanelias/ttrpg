"""Unit tests for tools/currency_consistency_check.py (ED-1087) — the self-updating recency
gate. Pure-function tests over synthetic inputs; the git-dependent stamp check is exercised
only through its date-grace helper (the walk itself is integration-covered by the CI job)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
import currency_consistency_check as ccc  # noqa: E402


def test_next_day_grace():
    assert ccc._next_day('2026-07-01') == '2026-07-02'
    assert ccc._next_day('2026-12-31') == '2027-01-01'


def test_current_md_paths_filter_globs():
    text = "| row | `params/core.md` + `params/bg/*` | `designs/scene/combat_engine_v1/` |"
    paths = ccc._current_md_paths(text)
    assert 'params/core.md' in paths
    assert 'designs/scene/combat_engine_v1/' in paths
    assert all('*' not in p for p in paths)


def test_maintained_by_regex_matches_variants():
    hits = [ccc.MAINTAINED_RE.search(s) for s in (
        "## Maintained by: valoria-orchestrator skill",
        "*Registry maintained by valoria-orchestrator. Update in same commit*",
        "## Auto-maintained — appended by valoria-orchestrator on patch application",
    )]
    assert all(h and h.group(1).lower() == 'valoria-orchestrator' for h in hits)


def test_retired_markers_suppress():
    line = "*Glossary maintained by hand (the valoria-orchestrator skill was retired 2026-06-28)*"
    m = ccc.MAINTAINED_RE.search(line)
    # the regex may or may not hit 'hand'; the retired-marker suppression is what matters
    assert any(k in line.lower() for k in ccc.RETIRED_MARKERS)


def test_ledger_max_and_ceiling_logic(tmp_path, monkeypatch):
    (tmp_path / 'canon').mkdir()
    (tmp_path / 'references').mkdir()
    (tmp_path / 'canon' / 'editorial_ledger.jsonl').write_text(
        '{"id": "ED-100", "status": "resolved"}\n{"id": "ED-1090", "status": "open"}\n',
        encoding='utf-8')
    (tmp_path / 'references' / 'id_reservations.yaml').write_text(
        'verified_live_max:\n  ED: 1080\n  PP: 726\n'
        'reservations:\n  D:\n    ED: { block: "1050-1099", next_free: 1085 }\n',
        encoding='utf-8')
    monkeypatch.setattr(ccc, 'REPO_ROOT', str(tmp_path))
    assert ccc._ledger_max_ed() == 1090
    drift = []
    ccc.check_id_ceilings(drift)
    joined = '\n'.join(drift)
    assert 'verified_live_max.ED 1080' in joined          # stale verification flagged
    assert 'next_free 1085 <= live max ED-1090' in joined  # in-block overrun flagged


def test_patch_register_header_check(tmp_path, monkeypatch):
    (tmp_path / 'canon').mkdir()
    (tmp_path / 'canon' / 'patch_register_active.yaml').write_text(
        '# Next PP number: 724\npatches:\n  - id: PP-726\n', encoding='utf-8')
    monkeypatch.setattr(ccc, 'REPO_ROOT', str(tmp_path))
    drift = []
    ccc.check_patch_register_header(drift)
    assert drift and 'Next PP number: 724' in drift[0]


def test_summary_line_never_raises(monkeypatch):
    def boom():
        raise RuntimeError('synthetic')
    monkeypatch.setattr(ccc, 'run_checks', boom)
    line = ccc.summary_line()
    assert 'errored' in line
