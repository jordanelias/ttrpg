#!/usr/bin/env python3
"""
tools/observability/obs_core.py — shared observability primitives (single owner).

The observability tier had the same rules re-implemented in ≥4 places (editorial
ledger parsed 4 ways; status-line regex 3 ways; lane rosters 3 ways; the
`window.VALORIA_X = …` JS bundle hand-rolled 3 times). This module is the ONE
home for those primitives (CLAUDE.md §8 "every rule lives once"), so
build_proposals.py, dashboard_data.py and future consumers share them instead of
diverging (the GO-lane undercount, the disagreeing Status regexes, etc.).

Design:
  • REUSE, don't duplicate, the richest existing implementations — build_decisions.py
    already owns the best lane table (infer_lane / LANE_PATH_PREFIXES), the corpus
    marker set (MARKERS) and the name-redaction mirror. core imports them; it never
    re-derives them, and build_decisions NEVER imports core (no cycle — guarded by
    tests/valoria/test_observability_core.py).
  • OWN the genuinely-new shared primitives below (ledger reader, status parser,
    JS-bundle writer, the narrow needs-Jordan marker vocab).

Import-only module (no __main__): consumers `import core`.
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))       # sibling import of build_decisions

# --- reuse build_decisions' owned primitives (do not re-implement) -------------
import build_decisions as _bd            # noqa: E402

infer_lane = _bd.infer_lane                      # path -> ED-<LANE> (richest table)
LANE_NAMES = _bd.LANE_NAMES                       # 9-lane display names
DECISION_MARKERS = _bd.MARKERS                    # corpus-wide 13-pattern open-item set
redact_forbidden_names = _bd._redact_forbidden_names  # names_index.yaml redaction mirror

# --- lane roster (the single canonical 9-code tuple) ---------------------------
# The prior rosters that must migrate to this: dashboard_data.LEDGER_LANES (which
# silently OMITTED 'go'), currency_consistency_check.LANE_CODES, validate_ed_citations.LANE_CODES.
LANE_CODES: tuple[str, ...] = ("MB", "PC", "FI", "SC", "FA", "WR", "IN", "GO", "SE")
LEDGER_LANE_CODES: tuple[str, ...] = tuple(c.lower() for c in LANE_CODES)  # ledger filename lanes


# --- A. editorial-ledger reader (single owner) ---------------------------------
def read_ledger_entries(repo: Path | None = None) -> list[dict]:
    """Every entry across registers/editorial_ledger*.jsonl (flat + per-lane), normalized.
    Lane comes free from the filename (`editorial_ledger_<xx>.jsonl`) — the 2-letter
    match captures GO, which dashboard_data.LEDGER_LANES did not. Archive file skipped
    (settled history, not live debt)."""
    repo = repo or REPO
    out: list[dict] = []
    for path in sorted((repo / "registers").glob("editorial_ledger*.jsonl")):
        base = path.name
        if "archive" in base:
            continue
        m = re.match(r"editorial_ledger_([a-z]{2})\.jsonl$", base)
        lane = m.group(1).upper() if m else None
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                e = json.loads(line)
            except json.JSONDecodeError:
                continue
            desc = e.get("description") or ""
            if isinstance(desc, list):            # schema drift: some entries use a list
                desc = " ".join(str(x) for x in desc)
            out.append({
                "id": e.get("id", "?"),
                "lane": lane,
                "status": e.get("status"),
                "needs_jordan": bool(e.get("needs_jordan")),
                "description": str(desc).strip(),
                "source": e.get("source"),
                "file": base,
            })
    return out


def open_ledger_entries(repo: Path | None = None) -> list[dict]:
    return [e for e in read_ledger_entries(repo) if e.get("status") == "open"]


# --- D. status-line parsing (single owner) -------------------------------------
# One tolerance policy, a superset of the two prior regexes it replaces:
#   dashboard_data._STATUS_RE        = ^#{1,3}\s*Status:        (needs a hash, no space)
#   ci_generation_consistency.status_of = #{0,3}\s*Status\s*:   (0-3 hashes, tolerates 'Status :')
# Using the tolerant superset is a deliberate RECONCILIATION (may match a few more
# docs); the expected delta is asserted in the core test, not hidden under a
# "byte-identical" claim.
STATUS_RE = re.compile(r'^#{0,3}\s*Status\s*:\s*(.+)$', re.I)


def first_status(head_text: str) -> str | None:
    """The first `## Status:` value in a doc head, or None."""
    for line in head_text.splitlines():
        m = STATUS_RE.match(line.strip())
        if m:
            return m.group(1).strip()
    return None


def is_unratified_status(status: str | None) -> bool:
    """True for PROPOSED / PROVISIONAL / DRAFT statuses that are not CANONICAL."""
    up = (status or "").upper()
    prefix = up.split("(")[0]  # "CANONICAL (with provisional elements)" stays canonical
    return (("PROPOSED" in up or "PROVISIONAL" in up or "DRAFT" in up)
            and "CANONICAL" not in prefix)


# --- narrow needs-Jordan marker vocab (distinct from DECISION_MARKERS) ----------
# Scanned ONLY over handoff files for the high-signal "needs YOUR decision" inbox.
# Kept SEPARATE from DECISION_MARKERS (the corpus-wide TODO/GAP/STUB sweep) on
# purpose — merging them would flood the inbox with hygiene items (finding B3).
NEEDS_JORDAN_MARKERS = re.compile(r'JORDAN RULING NEEDED|needs_jordan\s*[:=]\s*true', re.I)


# --- 3-artifact JS-bundle writer (single owner) --------------------------------
def write_js_bundle(path: Path, var: str, obj) -> None:
    """Emit `window.<var> = <json>;` — the committed dashboard bundle idiom that
    build_decisions / build_graph / build_lexicon each hand-rolled independently."""
    path.write_text(f"window.{var} = " + json.dumps(obj, ensure_ascii=False) + ";\n",
                    encoding="utf-8")
