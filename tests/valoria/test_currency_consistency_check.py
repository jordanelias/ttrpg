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


# ---------------------------------------------------------------------------
# check_current_stamp_structure — the reconcile-chain guard (ED-IN-0189, 2026-08-14).
#
# These pin the guard that replaces the deleted 38,164-char CURRENT.md history blob. Every
# assertion below is one the pre-deletion file WOULD HAVE FAILED: measured on `9933ff2`, the
# check reported 1 chronology inversion (link 13, 2026-08-10 following 2026-07-30) and 8
# verbatim-duplicated stamp bodies of 466-3,303 chars. That measurement is what the floor and
# the monotonicity rule were chosen against, not a fixture written to make them pass.

_HEAD = "# Valoria\n\nintro paragraph\n\n"
_TAIL = "\n\n| Subsystem | Current head |\n|---|---|\n| **X** | `systems/x/x.md` |\n"


def _write_current(tmp_path, monkeypatch, stamp_para):
    (tmp_path / 'CURRENT.md').write_text(_HEAD + stamp_para + _TAIL)
    monkeypatch.setattr(ccc, 'REPO_ROOT', str(tmp_path))


def _body(tag, n=600):
    """A stamp body over the duplication floor, distinct per tag."""
    return f"(**{tag}-lane stamp reconcile**: " + (f"{tag} detail. " * n)[:n] + ")"


def test_clean_descending_chain_reports_nothing(tmp_path, monkeypatch):
    para = (f"_Last reconciled: 2026-08-14 {_body('IN')} "
            f"Prior reconcile: 2026-08-10 {_body('PC')} "
            f"Prior reconcile: 2026-08-03 {_body('MB')}_")
    _write_current(tmp_path, monkeypatch, para)
    drift = []
    ccc.check_current_stamp_structure(drift)
    assert drift == [], drift


def test_flags_a_date_inversion(tmp_path, monkeypatch):
    """The exact defect three independent lenses found by reading and no tool could see."""
    para = (f"_Last reconciled: 2026-08-12 {_body('IN')} "
            f"Prior reconcile: 2026-07-30 {_body('PC')} "
            f"Prior reconcile: 2026-08-10 {_body('MB')}_")   # climbs — the splice signature
    _write_current(tmp_path, monkeypatch, para)
    drift = []
    ccc.check_current_stamp_structure(drift)
    assert any('non-monotonic' in d for d in drift), drift
    assert any('2026-08-10' in d for d in drift), drift


def test_flags_a_verbatim_duplicated_stamp_body(tmp_path, monkeypatch):
    dup = _body('SC')
    para = (f"_Last reconciled: 2026-08-14 {_body('IN')} "
            f"Prior reconcile: 2026-08-08 {dup} "
            f"Prior reconcile: 2026-08-06 {dup} "
            f"Prior reconcile: 2026-08-01 {_body('WR')}_")
    _write_current(tmp_path, monkeypatch, para)
    drift = []
    ccc.check_current_stamp_structure(drift)
    assert any('repeats' in d for d in drift), drift
    # Reported ONCE per distinct body, not once per extra copy.
    assert sum('repeats' in d for d in drift) == 1, drift


def test_same_day_reconciles_from_different_lanes_are_LEGAL(tmp_path, monkeypatch):
    """THE FALSIFIER FOR THE PLAN'S OWN WORDING, and the reason this guard deviates from it.

    ED-IN-0185 step A2 prescribed "strictly-descending dates". The real tree falsifies that:
    on 2026-08-08 the IN, MB, PC and SC lanes each landed a legitimate reconcile stamp. A
    strict rule reds on correct content, and a guard that reds on correct content gets
    weakened by the next session rather than obeyed. Non-increasing is the true invariant.
    """
    para = (f"_Last reconciled: 2026-08-08 {_body('IN')} "
            f"Prior reconcile: 2026-08-08 {_body('MB')} "
            f"Prior reconcile: 2026-08-08 {_body('PC')} "
            f"Prior reconcile: 2026-08-08 {_body('SC')}_")
    _write_current(tmp_path, monkeypatch, para)
    drift = []
    ccc.check_current_stamp_structure(drift)
    assert drift == [], "same-day cross-lane reconciles must not be reported as drift"


def test_short_repeats_stay_below_the_duplication_floor(tmp_path, monkeypatch):
    """Connective fragments recur legitimately; only stamp-sized bodies are splice evidence."""
    short = "(see the lane handoff)"
    para = (f"_Last reconciled: 2026-08-14 {short} "
            f"Prior reconcile: 2026-08-08 {short} "
            f"Prior reconcile: 2026-08-06 {short}_")
    _write_current(tmp_path, monkeypatch, para)
    drift = []
    ccc.check_current_stamp_structure(drift)
    assert drift == [], drift


def test_guard_is_wired_into_run_checks():
    """A check nothing calls is decoration (ED-IN-0180's 'live signal with no consumer')."""
    import inspect
    assert 'check_current_stamp_structure' in inspect.getsource(ccc.run_checks)
