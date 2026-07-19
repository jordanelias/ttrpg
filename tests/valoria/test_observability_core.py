"""
Unit tests for tools/observability/core.py — the shared observability primitives.

Pins the contracts that the dedup depends on: the 9-code lane roster INCLUDES GO
(the bug dashboard_data.LEDGER_LANES had), the ledger reader normalizes entries and
tolerates list-valued descriptions, the reconciled Status regex matches the tolerant
superset, and — critically — core does NOT create an import cycle (build_decisions
must never import core).
"""
import os
import sys

HERE = os.path.dirname(__file__)
OBS = os.path.join(HERE, '..', '..', 'tools', 'observability')
sys.path.insert(0, OBS)
import obs_core as core  # noqa: E402  (distinct name — no collision with combat's core.py)


def test_lane_codes_includes_go():
    # the GO-omission time-bomb: LANE_CODES must carry all 9, including GO
    assert core.LANE_CODES == ("MB", "PC", "FI", "SC", "FA", "WR", "IN", "GO", "SE")
    assert "go" in core.LEDGER_LANE_CODES


def test_status_regex_tolerant_superset():
    # reconciled tolerance: 0-3 hashes AND optional space before the colon
    assert core.first_status("## Status: PROPOSED") == "PROPOSED"
    assert core.first_status("Status : DRAFT") == "DRAFT"          # no hash, space before colon
    assert core.first_status("### Status:CANONICAL") == "CANONICAL"
    assert core.first_status("# heading\nno status here") is None


def test_is_unratified_status():
    assert core.is_unratified_status("PROPOSED")
    assert core.is_unratified_status("PROVISIONAL — pending")
    assert core.is_unratified_status("DRAFT")
    # a canonical doc that merely mentions provisional elements stays canonical
    assert not core.is_unratified_status("CANONICAL (with provisional elements)")
    assert not core.is_unratified_status(None)


def test_ledger_reader_normalizes_and_tolerates_list_desc(tmp_path):
    d = tmp_path / "registers"
    d.mkdir()
    (d / "editorial_ledger_go.jsonl").write_text(
        '{"id":"ED-GO-0001","status":"open","needs_jordan":true,"description":["a","b"]}\n'
        '{"id":"ED-GO-0002","status":"resolved","description":"done"}\n',
        encoding="utf-8")
    (d / "editorial_ledger_archive.jsonl").write_text(
        '{"id":"ED-OLD","status":"open"}\n', encoding="utf-8")  # archive must be skipped
    entries = core.read_ledger_entries(tmp_path)
    ids = {e["id"] for e in entries}
    assert ids == {"ED-GO-0001", "ED-GO-0002"}         # archive skipped
    go1 = next(e for e in entries if e["id"] == "ED-GO-0001")
    assert go1["lane"] == "GO"                          # GO captured from filename
    assert go1["description"] == "a b"                  # list description coerced
    assert core.open_ledger_entries(tmp_path) == [e for e in entries if e["status"] == "open"]


def test_text_needs_jordan_positive():
    # the pending-Jordan phrasings that build_proposals' design-doc + flat-ledger
    # rescue depends on (the structural undercount fix)
    assert core.text_needs_jordan("Status: PROPOSAL — pending Jordan sign-off")
    assert core.text_needs_jordan("HELD FOR JORDAN.")
    assert core.text_needs_jordan("DRAFT — awaiting Jordan review")
    assert core.text_needs_jordan("[GATE G8 - Jordan decision] out-of-bounds …")
    assert core.text_needs_jordan("Two mechanical-tier decisions for Jordan veto: (1) …")
    assert core.text_needs_jordan("INTENT UNDETERMINED: Jordan to confirm the surfaces")
    assert core.text_needs_jordan("DECISION (Jordan): (a) declare RETAINED …")
    assert core.text_needs_jordan("this doc is Jordan-vetoable throughout")


def test_text_needs_jordan_negative():
    # must match FUTURE/PENDING action only — a PAST ruling's citation stays actionable
    assert not core.text_needs_jordan("evidence-decided, not a Jordan choice")
    assert not core.text_needs_jordan("Decided canon per Jordan's prior ruling")
    assert not core.text_needs_jordan("routine cleanup, no ruling needed")
    assert not core.text_needs_jordan(None)
    assert not core.text_needs_jordan("")


def test_ledger_reader_rescues_fieldless_pending_jordan(tmp_path):
    # a pre-cutover flat entry with NO needs_jordan field but pending-Jordan text
    # must read as needs_jordan (the field-absent undercount)
    d = tmp_path / "registers"
    d.mkdir()
    (d / "editorial_ledger.jsonl").write_text(
        '{"id":"ED-9001","status":"open","description":"[GATE - Jordan decision] pending Jordan."}\n'
        '{"id":"ED-9002","status":"open","description":"evidence-decided, not a Jordan choice"}\n',
        encoding="utf-8")
    entries = {e["id"]: e for e in core.read_ledger_entries(tmp_path)}
    assert entries["ED-9001"]["needs_jordan"] is True    # rescued by text scan
    assert entries["ED-9002"]["needs_jordan"] is False   # past/negated — stays actionable


def test_no_import_cycle():
    # core imports build_decisions; build_decisions must NOT import core (would cycle)
    import build_decisions  # noqa: F401
    bd_src = open(os.path.join(OBS, "build_decisions.py"), encoding="utf-8").read()
    assert "import core" not in bd_src, "build_decisions must not import core (cycle)"


def test_redaction_reachable_from_new_home():
    # _redact_forbidden_names uses parents[2] repo-root resolution; it must still work
    # when reached via core (same depth). Load-bearing for keeping ci_naming_check green.
    out = core.redact_forbidden_names("plain text with no legacy name")
    assert isinstance(out, str) and "plain text" in out


def test_write_js_bundle(tmp_path):
    p = tmp_path / "x_data.js"
    core.write_js_bundle(p, "VALORIA_X", {"a": 1})
    txt = p.read_text(encoding="utf-8")
    assert txt.startswith("window.VALORIA_X = ")
    assert txt.rstrip().endswith(";")
