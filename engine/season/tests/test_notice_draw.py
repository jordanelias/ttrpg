"""B11.65 -- THE `public:` COLUMN ON EVERY VERB ROW (`18_DETERMINISM_notice_is_a_draw`, Exact edits 1).

A deed is public only when its verb row says so, and the column is required: a row without it, or with a value that is not a
boolean, never loads. Each test plants the defect in a copy of `verb_table.yaml` and observes `_load_verb_table` refuse it; the
unplanted copy is the control. The notice draw's later items (B11.66 on) extend this file.
"""
from __future__ import annotations

from engine.season.tests.test_u1_capability_surface import _planted_verb_load, _row


def test_public_column_absent_is_refused_at_load():
    """A planted row without `public:` is refused, naming the row; the same copy unplanted loads (the control)."""
    assert _planted_verb_load(lambda doc: None) is None
    msg = _planted_verb_load(lambda doc: _row(doc, "argue").pop("public", None))
    assert msg is not None and "argue" in msg and "public" in msg, msg


def test_public_column_not_a_boolean_is_refused_at_load():
    """`public: "yes"` (and an integer, which `bool` would also admit) is refused, naming the row."""
    for bad in ("yes", 1, None):
        msg = _planted_verb_load(lambda doc, bad=bad: _row(doc, "speak").update(public=bad))
        assert msg is not None and "speak" in msg and "public" in msg and "boolean" in msg, (bad, msg)
