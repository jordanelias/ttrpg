"""canon_resolver.py — resolves a subsystem's live canonical head from CURRENT.md,
and can verify a specific cited constant is still literally present in the target
prose doc before a caller trusts it.

Never fabricates: raises CanonGapError when no matching row exists, or when a
caller-asserted citation can't be found verbatim, rather than guessing a path or
falling back to a filename convention. CLAUDE.md section 4 is explicit that a
filename or in-file version string cannot tell you what is current — only
CURRENT.md and a head's "## Status:" line can — so this resolver reads CURRENT.md
and nothing else for the "is this canonical" question; verify_citation() is the
one place it looks past CURRENT.md into the cited prose doc itself, and only to
confirm one specific asserted string is still there (not to extract/parse values —
that is the larger, deliberately out-of-scope "typed engine-params pipeline" gap
named in CLAUDE.md section 5 and design doc section 3).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CURRENT_MD = REPO_ROOT / "CURRENT.md"

_TOOLS_DIR = REPO_ROOT / "tools"
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))
from currency_consistency_check import _current_md_paths  # noqa: E402
# ^ the repo's existing CURRENT.md path-citation parser (tools/currency_consistency_check.py) —
# reused rather than re-implemented so this module stays in sync with the one other
# place that already knows how to extract citable paths from CURRENT.md (backticked,
# keeps trailing-slash package dirs, so a directory-only canonical head like
# designs/scene/combat_engine_v1/ is captured, not just *.md files).

_ROW_RE = re.compile(r"^\|\s*\*\*(.+?)\*\*\s*\|(.*)\|\s*$")


class CanonGapError(RuntimeError):
    """A subsystem has no resolvable canonical citation, or an asserted citation
    could not be verified verbatim in its target doc. Callers must surface this as
    a CANON_GAP triage flag — never catch it to substitute a fabricated default."""


class CanonResolver:
    def __init__(self, current_md_path: Path = CURRENT_MD):
        self._path = current_md_path
        self._rows: dict[str, str] | None = None

    def _load_rows(self) -> dict[str, str]:
        if self._rows is not None:
            return self._rows
        # Every other failure path in this module raises CanonGapError so
        # Harness.run()'s `except CanonGapError` can convert it to a graceful
        # triage flag instead of crashing the run. A bare read_text() call here
        # would let a missing/unreadable CURRENT.md raise an uncaught OSError
        # straight through that same except clause — found by deliberately
        # pointing a CanonResolver at a nonexistent path.
        try:
            text = self._path.read_text(encoding="utf-8")
        except OSError as exc:
            raise CanonGapError(f"cannot read {self._path}: {exc}") from exc
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
        multiple matches (ambiguity is a gap too, not a coin flip).

        doc_paths is every citable path mentioned in the row's text, in the order
        they appear — it is NOT a ranked list and doc_paths[0] is not guaranteed to
        be "the" canonical head. A CURRENT.md row commonly cites several docs (an
        audit trail, a handoff pointer, the live head itself); a caller that needs
        one specific document should use verify_citation() to confirm that exact
        path is present, rather than indexing into doc_paths and assuming primacy.
        """
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
            "doc_paths": _current_md_paths(body),
        }

    def verify_citation(self, row_label_substring: str, doc_relpath: str,
                         expected_substring: str) -> str:
        """Confirm doc_relpath is cited in the resolved row AND that
        expected_substring appears verbatim in doc_relpath's current text. This is
        the mechanism an adapter uses to trust one specific canon-derived constant
        (e.g. a table row in params/core.md) instead of hardcoding it: if the doc
        moves, the citation is dropped from CURRENT.md, or the cited text changes,
        this raises CanonGapError rather than silently returning a stale value.

        This is deliberately narrow — a substring presence check, not extraction or
        parsing. Turning prose tables into typed, extractable values is the larger
        gap CLAUDE.md section 5 names as not yet built; this method only prevents
        USING a value the corpus no longer actually says, it does not derive new
        values from prose on its own.

        Known limitation, inherited from the reused _current_md_paths() parser
        (found verifying this fix, not introduced by it): some CURRENT.md rows cite
        a doc list as `` `full/path/first.md` + `bare_filename.md` + ... `` — only
        the first citation carries its directory prefix, the rest rely on prose-
        level "+" continuation for a human reader. _current_md_paths() requires a
        path to start with a known top-level directory, so a bare continuation
        filename like `` `faction_layer_v30.md` `` is silently dropped from
        doc_paths — meaning verify_citation() would wrongly raise CanonGapError for
        a legitimately-cited doc formatted that way (confirmed against CURRENT.md's
        Faction/political row). Not fixed here: the parser is shared with the
        already-CI-wired tools/currency_consistency_check.py, and this method
        deliberately reuses it rather than adding a second, drifting one (see
        module docstring) — broadening the shared regex is a change to a live CI
        check's behavior and belongs in its own reviewed change, not folded
        silently into this harness fix. An adapter targeting a row that uses this
        citation shorthand should verify against the row's FIRST (full-path)
        citation, or file the parser gap separately before relying on the rest.
        """
        resolved = self.resolve(row_label_substring)
        if doc_relpath not in resolved["doc_paths"]:
            raise CanonGapError(
                f"{doc_relpath!r} is not cited in the {resolved['row_label']!r} "
                f"CURRENT.md row (cited docs: {resolved['doc_paths']}) — refusing "
                f"to trust a value from an uncited doc"
            )
        doc_path = REPO_ROOT / doc_relpath
        try:
            text = doc_path.read_text(encoding="utf-8")
        except OSError as exc:
            raise CanonGapError(f"cannot read cited doc {doc_relpath!r}: {exc}") from exc
        if expected_substring not in text:
            raise CanonGapError(
                f"{expected_substring!r} not found verbatim in {doc_relpath!r} — "
                f"the cited value may have changed; re-derive it, do not keep the "
                f"old hardcoded number"
            )
        return expected_substring
