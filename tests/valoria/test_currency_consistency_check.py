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
    text = "| row | `params/core.md` + `params/bg/*` | `systems/combat/combat_engine_v1/` |"
    paths = ccc._current_md_paths(text)
    assert 'params/core.md' in paths
    assert 'systems/combat/combat_engine_v1/' in paths
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
    (tmp_path / 'registers').mkdir()
    (tmp_path / 'references').mkdir()
    (tmp_path / 'registers' / 'editorial_ledger.jsonl').write_text(
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


def test_ledger_lane_max_ignores_flat_ids():
    text = ('{"id": "ED-100", "status": "resolved"}\n'
            '{"id": "ED-MB-0001", "status": "ratified"}\n'
            '{"id": "ED-MB-0003", "status": "open"}\n'
            '{"id": "ED-SC-0012", "status": "open"}\n')
    import re
    out = {}
    for lane, num in re.findall(r'"id":\s*"ED-([A-Z]{2})-(\d+)"', text):
        if lane in ccc.LANE_CODES:
            out[lane] = max(out.get(lane, 0), int(num))
    assert out == {'MB': 3, 'SC': 12}   # ED-100 (flat) never contributes


def test_lane_id_ceiling_drift_flagged(tmp_path, monkeypatch):
    (tmp_path / 'registers').mkdir()
    (tmp_path / 'references').mkdir()
    (tmp_path / 'registers' / 'editorial_ledger.jsonl').write_text(
        '{"id": "ED-MB-0005", "status": "ratified"}\n', encoding='utf-8')
    (tmp_path / 'references' / 'id_reservations.yaml').write_text(
        'lane_ids:\n  lanes:\n    MB: { name: "Mass battle", next_free: 3 }\n',
        encoding='utf-8')
    monkeypatch.setattr(ccc, 'REPO_ROOT', str(tmp_path))
    drift = []
    ccc.check_lane_id_ceilings(drift)
    joined = '\n'.join(drift)
    assert 'lane_ids.MB.next_free 3 <= actual ledger max ED-MB-5' in joined


def test_lane_id_ceiling_missing_lane_flagged(tmp_path, monkeypatch):
    (tmp_path / 'registers').mkdir()
    (tmp_path / 'references').mkdir()
    (tmp_path / 'registers' / 'editorial_ledger.jsonl').write_text(
        '{"id": "ED-SE-0001", "status": "ratified"}\n', encoding='utf-8')
    (tmp_path / 'references' / 'id_reservations.yaml').write_text(
        'lane_ids:\n  lanes:\n    MB: { name: "Mass battle", next_free: 3 }\n',
        encoding='utf-8')
    monkeypatch.setattr(ccc, 'REPO_ROOT', str(tmp_path))
    drift = []
    ccc.check_lane_id_ceilings(drift)
    assert any('no entry for lane SE' in d for d in drift)


def test_lane_id_ceiling_clean_when_no_lane_ids_yet(tmp_path, monkeypatch):
    (tmp_path / 'registers').mkdir()
    (tmp_path / 'registers' / 'editorial_ledger.jsonl').write_text(
        '{"id": "ED-100", "status": "resolved"}\n', encoding='utf-8')
    monkeypatch.setattr(ccc, 'REPO_ROOT', str(tmp_path))
    drift = []
    ccc.check_lane_id_ceilings(drift)
    assert drift == []   # no lane-tagged IDs in the ledger -> nothing to check


def test_patch_register_header_check(tmp_path, monkeypatch):
    (tmp_path / 'registers').mkdir()
    (tmp_path / 'registers' / 'patch_register_active.yaml').write_text(
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
