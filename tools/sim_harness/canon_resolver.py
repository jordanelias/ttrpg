"""canon_resolver.py — resolves a subsystem's live canonical head from CURRENT.md.

Never fabricates: raises CanonGapError when no matching row exists, rather than
guessing a path or falling back to a filename convention. CLAUDE.md section 4 is
explicit that a filename or in-file version string cannot tell you what is current —
only CURRENT.md and a head's "## Status:" line can — so this resolver reads
CURRENT.md and nothing else for the "is this canonical" question.
"""
from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CURRENT_MD = REPO_ROOT / "CURRENT.md"

_ROW_RE = re.compile(r"^\|\s*\*\*(.+?)\*\*\s*\|(.*)\|\s*$")
_DOC_RE = re.compile(r"`([^`]+\.md)`")


class CanonGapError(RuntimeError):
    """A subsystem has no resolvable canonical citation. Callers must surface this
    as a CANON_GAP triage flag — never catch it to substitute a fabricated default."""


class CanonResolver:
    def __init__(self, current_md_path: Path = CURRENT_MD):
        self._path = current_md_path
        self._rows: dict[str, str] | None = None

    def _load_rows(self) -> dict[str, str]:
        if self._rows is not None:
            return self._rows
        text = self._path.read_text(encoding="utf-8")
        rows: dict[str, str] = {}
        for line in text.splitlines():
            m = _ROW_RE.match(line)
            if m:
                label, body = m.group(1).strip(), m.group(2).strip()
                rows[label] = body
        self._rows = rows
        return rows

    def resolve(self, row_label_substring: str) -> dict:
        """Return {"row_label", "raw", "doc_paths"} for the one CURRENT.md row whose
        bold label contains row_label_substring. Raises CanonGapError on zero or
        multiple matches (ambiguity is a gap too, not a coin flip)."""
        rows = self._load_rows()
        matches = {
            label: body for label, body in rows.items()
            if row_label_substring.lower() in label.lower()
        }
        if not matches:
            raise CanonGapError(
                f"no CURRENT.md row matches {row_label_substring!r} — refusing to "
                f"fabricate a canonical source; file the gap, do not guess"
            )
        if len(matches) > 1:
            raise CanonGapError(
                f"{row_label_substring!r} matches multiple CURRENT.md rows "
                f"{list(matches)} — ambiguous, narrow the adapter's canon_row"
            )
        (label, body), = matches.items()
        return {
            "row_label": label,
            "raw": body,
            "doc_paths": _DOC_RE.findall(body),
        }
