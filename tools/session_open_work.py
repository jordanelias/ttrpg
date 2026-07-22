#!/usr/bin/env python3
"""
session_open_work.py — the "open work" face of the SessionStart banner (ED-IN-0081).

Closes a standing gap: session_status.py greeted every session with git + workplan +
top-2 audit-staleness + the ROOT HANDOFF.md "Next actions" only — so the surfaces where
live work actually accrues were silently missed at start (the recurring "things keep
getting missed" complaint):

  • the ACTIVE LANE's registers/handoffs/HANDOFF_<LANE>.md "## Pending" block — where
    per-lane continuity lives; CLAUDE.md §1 says "check your lane's file too", but the
    banner never read it. Root HANDOFF.md carries only cross-cutting items.
  • open EDITORIAL debt — open ledger entries + the needs_jordan subset (your decision
    inbox), computed already by obs_core but only ever published to the dashboard.
  • SCHEMA-in-flux flags — the descriptor roster "IN FLUX" + values_master quarantine —
    real traps for anyone binding numbers (CLAUDE.md §5), surfaced nowhere at start.

Design (mirrors audit_staleness.py, ED-IN-0032's proven pattern):
  • REUSE the single-owner primitives — obs_core (editorial ledger, lane inference,
    status parsing) and audit_staleness (family report). No rule is re-implemented here
    (CLAUDE.md §8 "every rule lives once"); this module only COMPOSES them into banner lines.
  • Git facts only for lane detection; no network, no new hand-maintained registry.
  • Defensive by contract: every public function catches broadly and degrades to "no
    data" (returns []) rather than raising — this is imported by the SessionStart hook
    and MUST NEVER break session start.

Import-only for the hook (`import session_open_work`); `python tools/session_open_work.py`
prints the full block for a manual look.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
_OBS = HERE / "observability"
for p in (str(HERE), str(_OBS)):
    if p not in sys.path:
        sys.path.insert(0, p)

HANDOFF_DIR = REPO / "registers" / "handoffs"


def _sh(args):
    try:
        r = subprocess.run(["git"] + args, capture_output=True, text=True, timeout=20)
    except Exception:
        return ""
    return r.stdout if r.returncode == 0 else ""


# --- active-lane detection (git facts only) -----------------------------------
def _changed_paths(commits: int = 12) -> list[str]:
    """Corpus-relative paths touched in the working tree + the last `commits` commits.
    The working tree is weighted first (what THIS session is doing); recent history
    disambiguates a clean tree just resumed on a lane."""
    paths: list[str] = []
    porcelain = _sh(["status", "--porcelain"])
    for ln in porcelain.splitlines():
        ln = ln.rstrip()
        if len(ln) > 3:
            paths.append(ln[3:].split(" -> ")[-1])  # handle rename "old -> new"
    hist = _sh(["log", f"-{commits}", "--name-only", "--pretty=format:"])
    paths += [ln.strip() for ln in hist.splitlines() if ln.strip()]
    return paths


def active_lane() -> str | None:
    """The lane this session is most plausibly working in, or None.

    Inferred from changed-file paths via obs_core.infer_lane (the single-owner lane
    table). Working-tree changes count double so an in-progress edit outweighs stale
    history. Returns None honestly when nothing classifies — no force-pick."""
    try:
        import obs_core
        tally: dict[str, int] = {}
        wt = set()
        for ln in _sh(["status", "--porcelain"]).splitlines():
            if len(ln) > 3:
                wt.add(ln[3:].split(" -> ")[-1])
        for path in _changed_paths():
            lane = obs_core.infer_lane(path)
            if lane:
                tally[lane] = tally.get(lane, 0) + (2 if path in wt else 1)
        if not tally:
            return None
        return max(tally, key=lambda k: tally[k])
    except Exception:
        return None


# --- lane HANDOFF "## Pending" reader ------------------------------------------
def _pending_items(lane: str) -> list[str]:
    """Top-level '- ' bullets under the '## Pending' heading of HANDOFF_<LANE>.md.
    Only top-level bullets (no leading indent) are counted as items; nested sub-bullets
    belong to the item above them."""
    fp = HANDOFF_DIR / f"HANDOFF_{lane}.md"
    if not fp.exists():
        return []
    try:
        lines = fp.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return []
    # Reuse build_decisions.RESOLVED_SKIP (single owner) so a "✅ … DONE" / "RESOLVED"
    # bullet left in the Pending section isn't miscounted as live work.
    try:
        import build_decisions
        settled = build_decisions.RESOLVED_SKIP
    except Exception:
        settled = None
    items, grab = [], False
    for ln in lines:
        if ln.strip().lower().startswith("## pending"):
            grab = True
            continue
        if grab and ln.startswith("## "):
            break
        if grab and ln.startswith("- "):
            body = ln[2:].strip()
            if body.startswith("✅") or body.startswith("~~"):
                continue
            if settled is not None and settled.search(body):
                continue
            items.append(body)
    return items


def _first_sentence(text: str, width: int = 96) -> str:
    """A compact one-line teaser: strip markdown emphasis, collapse to `width` chars."""
    t = text.replace("**", "").replace("`", "").strip()
    t = " ".join(t.split())
    return t if len(t) <= width else t[: width - 1].rstrip() + "…"


# --- the composed banner block -------------------------------------------------
def _lane_lines() -> list[str]:
    lane = active_lane()
    try:
        import obs_core
        lane_name = obs_core.LANE_NAMES.get(lane, lane) if lane else None
    except Exception:
        lane_name = lane
    out: list[str] = []
    if lane:
        items = _pending_items(lane)
        if items:
            out.append(f"lane {lane} ({lane_name}): {len(items)} pending — check "
                       f"registers/handoffs/HANDOFF_{lane}.md")
            out.append(f"  → {_first_sentence(items[0])}")
        else:
            out.append(f"lane {lane} ({lane_name}): no pending items tracked")
    else:
        # No active lane inferred — show which lanes carry pending work, as an index.
        # Roster comes from obs_core.LANE_CODES (single owner) — never a local literal,
        # so a future lane can't be silently omitted (the dashboard GO-omission class).
        try:
            import obs_core
            counts = []
            for code in obs_core.LANE_CODES:
                n = len(_pending_items(code))
                if n:
                    counts.append(f"{code}({n})")
            if counts:
                out.append("lanes with pending work: " + " ".join(counts)
                           + " — see registers/handoffs/HANDOFF_<LANE>.md")
        except Exception:
            pass
    return out


def _editorial_line() -> list[str]:
    try:
        import obs_core
        openes = obs_core.open_ledger_entries()
        if not openes:
            return []
        nj = sum(1 for e in openes if e.get("needs_jordan"))
        tail = f" ({nj} need Jordan)" if nj else ""
        return [f"editorial: {len(openes)} open ED item(s){tail} — "
                "registers/editorial_ledger*.jsonl"]
    except Exception:
        return []


def _schema_line() -> list[str]:
    """One flag line if the derived-stat schema or values_master are known-unstable
    (CLAUDE.md §5 traps). Cheap substring checks against the two registries."""
    flags = []
    try:
        dr = (REPO / "references" / "descriptor_registry.yaml")
        if dr.exists() and "IN FLUX" in dr.read_text(encoding="utf-8", errors="replace"):
            flags.append("descriptor roster IN FLUX")
    except Exception:
        pass
    try:
        vm = (REPO / "references" / "values_master.yaml")
        if vm.exists():
            head = "".join(vm.read_text(encoding="utf-8", errors="replace").splitlines(True)[:12])
            if "QUARANTINED" in head.upper():
                flags.append("values_master quarantined-stale")
    except Exception:
        pass
    if flags:
        return ["schema: " + " · ".join(flags) + " — do not bind Godot fields yet (CLAUDE.md §5)"]
    return []


def _audit_lines() -> list[str]:
    """ALL stale audit families (not just the top-2), delegated to audit_staleness."""
    try:
        import audit_staleness
        # n = the family count (self-adjusting) so "all stale families" never silently
        # caps if a family is added — not a magic literal.
        return audit_staleness.top_stale(n=len(audit_staleness.FAMILIES))
    except Exception:
        return []


def summary_lines() -> list[str]:
    """The 'open work' banner block, best-effort. Returns [] if nothing to show or on
    any failure — never raises (imported by the SessionStart hook)."""
    try:
        body = _lane_lines() + _editorial_line() + _schema_line() + _audit_lines()
        if not body:
            return []
        return ["── open work ──"] + body
    except Exception:
        return []


def main():
    lines = summary_lines()
    if lines:
        print("\n".join(lines))
    else:
        print("open-work: (nothing to surface, or status unavailable)")
    sys.exit(0)


if __name__ == "__main__":
    main()
