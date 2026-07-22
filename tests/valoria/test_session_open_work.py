"""
Unit tests for tools/session_open_work.py — the SessionStart "open work" face (ED-IN-0081).

The binding contract is DEFENSIVE: this module is imported by the SessionStart hook
(tools/session_status.py), so every public entry point must degrade to "no data" rather
than raise, no matter the tree state. These tests pin that contract plus the two pieces
of real logic worth locking (settled-bullet filtering, block shape).
"""
import os
import sys

HERE = os.path.dirname(__file__)
TOOLS = os.path.join(HERE, '..', '..', 'tools')
sys.path.insert(0, TOOLS)
import session_open_work as sow  # noqa: E402


def test_summary_lines_never_raises_and_returns_list():
    out = sow.summary_lines()
    assert isinstance(out, list)
    assert all(isinstance(x, str) for x in out)


def test_block_header_present_only_when_body_present():
    out = sow.summary_lines()
    # Either empty, or a header followed by at least one body line — never a lone header.
    assert out == [] or (out[0] == "── open work ──" and len(out) > 1)


def test_active_lane_returns_code_or_none():
    # Roster derived from the single owner (obs_core.LANE_CODES), not a local literal —
    # a future lane addition must not falsely fail this.
    sys.path.insert(0, os.path.join(TOOLS, 'observability'))
    import obs_core
    lane = sow.active_lane()
    assert lane is None or lane in obs_core.LANE_CODES


def test_pending_items_filters_settled_bullets(tmp_path, monkeypatch):
    # A Pending section with a live item, a ✅-DONE item, a ~~struck~~ item, and a
    # "RESOLVED" item — only the live one survives.
    hd = tmp_path / "handoffs"
    hd.mkdir()
    (hd / "HANDOFF_XX.md").write_text(
        "# H\n\n## Pending\n"
        "- live work item that is genuinely open\n"
        "- ✅ finished thing DONE\n"
        "- ~~struck item~~\n"
        "- earlier item, RESOLVED 2026-07-01\n"
        "\n## History\n- not pending\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(sow, "HANDOFF_DIR", hd)
    items = sow._pending_items("XX")
    assert items == ["live work item that is genuinely open"]


def test_pending_items_missing_file_is_empty(tmp_path, monkeypatch):
    monkeypatch.setattr(sow, "HANDOFF_DIR", tmp_path)
    assert sow._pending_items("ZZ") == []


def test_first_sentence_truncates_and_strips_markdown():
    assert sow._first_sentence("**bold** `code` text") == "bold code text"
    long = "x " * 100
    assert len(sow._first_sentence(long)) <= 96
