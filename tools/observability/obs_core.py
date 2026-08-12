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
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))       # sibling import of build_decisions
if str(HERE.parents[0]) not in sys.path:
    sys.path.insert(0, str(HERE.parents[0]))   # tools/ — for ci_common

# The dependency-free primitives (repo root, lane roster, token estimate, id
# regexes) are owned ONE LAYER DOWN, in tools/ci_common.py, and re-exported here
# (plan G7, ED-IN-0159 §8.3). The direction is forced by the dependency graph:
# this module imports build_decisions, which requires PyYAML and sweeps the
# corpus at import time, while several stdlib-only BLOCKING gates need nothing
# from here but the 9-code tuple. Owning it here would have made those gates
# depend on the observability tier to read a constant.
#
# Nothing that imports obs_core changes: every name below is still available
# under the name it always had.
import ci_common as _cc                 # noqa: E402

REPO = _cc.REPO_PATH

# --- reuse build_decisions' owned primitives (do not re-implement) -------------
import build_decisions as _bd            # noqa: E402

infer_lane = _bd.infer_lane                      # path -> ED-<LANE> (richest table)
LANE_NAMES = _bd.LANE_NAMES                       # 9-lane display names
DECISION_MARKERS = _bd.MARKERS                    # corpus-wide 13-pattern open-item set
redact_forbidden_names = _bd._redact_forbidden_names  # names_index.yaml redaction mirror

# --- lane roster (the single canonical 9-code tuple) ---------------------------
# OWNED BY ci_common (plan G7) and re-exported here. The rosters that migrated onto
# it: dashboard_data.LEDGER_LANES (which silently OMITTED 'go'),
# currency_consistency_check.LANE_CODES, validate_ed_citations.LANE_CODES,
# ci_workplan_pointer_check.LANE_CODES, broken_dependency_checker._LANE_CODES,
# handoff_atomize.LANES.
LANE_CODES: tuple[str, ...] = _cc.LANE_CODES
LEDGER_LANE_CODES: tuple[str, ...] = _cc.LEDGER_LANE_CODES  # ledger filename lanes


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
                # `date` carried since ED-IN-0114. Without it no consumer can tell a
                # freshly-filed item from one that has rotted for two months, which made
                # every open-count metric punish FILING (the cure) instead of STALENESS
                # (the disease). Normalised to the YYYY-MM-DD prefix; entries whose date
                # is absent or unparseable keep None so a consumer must decide explicitly
                # rather than silently treating unknown age as zero.
                "date": (str(e["date"])[:10] if e.get("date") else None),
                # flat pre-cutover entries predate the needs_jordan FIELD — fall back
                # to a pending-Jordan text scan so they aren't miscounted actionable.
                "needs_jordan": bool(e.get("needs_jordan")) or text_needs_jordan(desc),
                "description": str(desc).strip(),
                "source": e.get("source"),
                "file": base,
            })
    return out


def open_ledger_entries(repo: Path | None = None) -> list[dict]:
    """Live open debt — ONE ROW PER ID, resolved by its LAST row.

    THE LEDGERS ARE APPEND-ONLY, so an id's effective status is its last row. That rule is
    documented in CLAUDE.md §4, enforced for archiving by `ci_register_size_check` ("archive
    WHOLE settled ids… moving only the resolved row silently reverts it"), and implemented by
    `validate_ed_citations.build_status_map`, which is last-write-wins.

    THIS FUNCTION DID NOT IMPLEMENT IT (fixed 2026-08-12, ED-IN-0169). It filtered every row
    with `status == "open"`, so an id closed by appending a resolution row — the normal way to
    close one without rewriting history — kept appearing as open debt to every consumer of this
    owner: the decisions and incompleteness registers, the dashboard's registers card, and the
    SessionStart banner. Meanwhile `validate_ed_citations` reported it resolved. Two readers of
    one file, disagreeing, with this one declaring itself the single owner (ED-IN-0068).

    Found by an independent critic on ED-IN-0162, which this session closed by appending a
    resolution row and which consequently read as BOTH open and resolved in the same tree.
    Fixing it in the owner fixes it for every consumer at once, which is the whole point of
    having one.
    """
    latest: dict[str, dict] = {}
    for e in read_ledger_entries(repo):
        latest[e.get("id", "?")] = e          # dict preserves order; last row wins
    return [e for e in latest.values() if e.get("status") == "open"]


# --- D. status-line parsing --------------------------------------------------
# OWNED BY ci_common (plan G8, ED-IN-0159 §1.3a) and re-exported here, same as the
# lane roster: the regex has no dependencies, and stdlib-only gates
# (ci_generation_consistency) read it. Every consumer of obs_core.STATUS_RE /
# obs_core.first_status is unaffected — they are the same objects.
#
# The prior comment here recorded a reconciliation of two regexes. The measurement
# behind G8 found a third fact worth carrying forward: the divergence that
# actually changed results was never the regex, it was the WINDOW each caller
# scanned. ci_common owns both, and STATUS_HEAD_LINES is the named default.
STATUS_RE = _cc.STATUS_RE
first_status = _cc.first_status
doc_status = _cc.doc_status
STATUS_HEAD_LINES = _cc.STATUS_HEAD_LINES


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

# --- pending-Jordan free-text detection (single owner) --------------------------
# Rescues two STRUCTURAL undercounts in build_proposals' needs-your-decision split:
#   (A) proposal_doc / provisional_status_doc kinds never carried a needs_jordan
#       flag at all, so a design doc whose Status reads "HELD FOR JORDAN" showed as
#       plain actionable — structurally unflaggable.
#   (B) pre-cutover flat ledger entries (registers/editorial_ledger.jsonl) predate the
#       needs_jordan FIELD, so an entry whose own text says "PENDING Jordan" /
#       "Jordan to confirm" / "DECISION (Jordan)" defaulted to actionable.
# The vocabulary deliberately matches FUTURE / PENDING Jordan action ONLY, never a
# citation of a PAST ruling — so "evidence-decided, not a Jordan choice" (ED-913) and
# "per Jordan's prior ruling" (ED-930) correctly STAY actionable. Verified empirically
# against the live ledger + proposals/ when this landed (see
# tests/valoria/test_observability_core.py::test_text_needs_jordan_*).
NEEDS_JORDAN_TEXT = re.compile(
    r"""
      HELD \s+ FOR \s+ JORDAN
    | JORDAN \s+ RULING \s+ NEEDED
    | needs_jordan \s* [:=] \s* true
    | PENDING \s* :? \s* JORDAN
    | AWAITING \s+ (?:A \s+)? JORDAN
    | JORDAN [-\s] VETO(?:ABLE)?
    | \b for \s+ Jordan \s+ veto \b
    | DECISION \s* \( \s* JORDAN \s* \)
    | \[ \s* (?:GATE [^\]]* [-–] \s*)? JORDAN \s+ DECISION [^\]]* \]
    | \b JORDAN \s+ (?: TO \s+ (?:CONFIRM|NAME|RULE|DECIDE|ADJUDICATE|CHOOSE|RESOLVE|VET)
                     | NAMING \s+ RULING
                     | DECISION \s+ NEEDED )
    | \[ \s* JORDAN \s+ TO \s+ \w+ [^\]]* \]
    | UNDETERMINED [:,]? \s+ JORDAN
    """,
    re.I | re.X,
)


def text_needs_jordan(text: str | None) -> bool:
    """True when free text signals a *pending* Jordan decision (see NEEDS_JORDAN_TEXT).
    Matches future/pending phrasings only — never a past ruling's citation."""
    return bool(text) and bool(NEEDS_JORDAN_TEXT.search(text))


# --- 3-artifact JS-bundle writer (single owner) --------------------------------
def write_js_bundle(path: Path, var: str, obj) -> None:
    """Emit `window.<var> = <json>;` — the committed dashboard bundle idiom that
    build_decisions / build_graph / build_lexicon each hand-rolled independently."""
    path.write_text(f"window.{var} = " + json.dumps(obj, ensure_ascii=False) + ";\n",
                    encoding="utf-8")
