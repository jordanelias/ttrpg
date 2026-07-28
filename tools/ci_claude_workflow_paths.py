#!/usr/bin/env python3
"""Resolve every repo-relative path referenced by the Claude Code apparatus in `.claude/`.

WHY THIS EXISTS (ED-IN-0085). The `designs/` (2026-07-19, ED-IN-0071 P4/P5) and `sim/`
(2026-07-21) retirements silently broke every `.claude/wf_*.js` Workflow script and
`.claude/launch.json`. Nothing caught it: `build_apparatus_registry._workflows()` resolves to
`.github/workflows` only (CI workflows — the word is overloaded), and the incumbent owner of the
retired-tree-pointer rule, `tools/observability/build_incompleteness.scan_retired_tree_pointers`,
declares this exact blind spot in its own COVERAGE_GAPS: "pointers in docs/comments and
non-`designs/` dead paths are not yet validated."

This is the INSTRUMENT for that claim, not a second owner of the rule. It exists so the number in
ED-IN-0085 is re-runnable rather than hand-counted (CLAUDE.md §0.1 point 3, and the same discipline
`tools/ci_claim_provenance_check.py` enforces on ledger entries). The intended end state is to fold
this resolver into `scan_retired_tree_pointers` and widen its `RETIRED_TREES` — see ED-IN-0085 P1.

Three outcomes per referenced path:
  LIVE    — exists in the working tree.
  ALIASED — does not exist, but `references/restructure_ledger.md` maps it to something that does.
            Not a hard break: a capable agent *might* find it. But the script never mentions the
            ledger, so the indirection is undeclared — degraded, not dead.
  DEAD    — unresolvable by any sanctioned route. This is what fails the gate.

Usage:
    python3 tools/ci_claude_workflow_paths.py            # report + exit 1 if any DEAD
    python3 tools/ci_claude_workflow_paths.py --json     # machine-readable
"""
from __future__ import annotations

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LEDGER = os.path.join(ROOT, "references", "restructure_ledger.md")
SCAN_DIR = os.path.join(ROOT, ".claude")

# Top-level trees a repo-relative path can start with. `designs/` and `sim/` are retired and are
# included deliberately — a reference to them is the failure this tool looks for.
TREES = (
    "designs", "sim", "systems", "engine", "references", "params", "tests",
    "registers", "canon", "audit", "arcs", "godot", "tools", "skills", "proposals",
    "workplans", "deprecated",
)
PATH_RE = re.compile(r"\b(?:%s)/[A-Za-z0-9_./-]+" % "|".join(TREES))

# A prompt is prose as well as code, so two classes of match are NOT dependencies:
#
# 1. Prose fragments that merely look path-shaped — "an engine/Godot consumer", "params prose
#    tables, sim/engine constants". A real reference is quoted, carries a file extension, or ends
#    in a slash; a bare two-segment noun phrase is none of those.
# 2. Paths the script DELIBERATELY names as nonexistent, because their absence IS the audit
#    finding — e.g. wf_attribute_coherence.js:50 "(filed under NONEXISTENT params/combat.md)".
#    Counting those as rot inverts the script's meaning and inflates the defect count.
KNOWN_EXT = (".md", ".py", ".yaml", ".yml", ".json", ".jsonl", ".js", ".gd", ".txt", ".html")
ABSENCE_MARKER = re.compile(
    r"NONEXISTENT|nonexistent|\bis dead\b|do(?:es)? not exist|no longer exists?|\bdead\b",
    re.I,
)


def is_dependency(ref: str, line: str) -> bool:
    """True when `ref` is a real dependency rather than prose or a declared-absent finding."""
    if ABSENCE_MARKER.search(line):
        return False
    if ref.endswith(KNOWN_EXT) or ref.endswith("/"):
        return True
    # Quoted anywhere on the line → a code string (e.g. `const ENG = 'C:/…/combat_engine_v1'`).
    return bool(re.search(r"['\"`][^'\"`]*%s" % re.escape(ref), line))
# `references/restructure_ledger.md` MOVES table: | `old` | `new` | STATUS |
ROW_RE = re.compile(r"^\|\s*`([^`]+)`\s*\|\s*`([^`]+)`\s*\|", re.M)

_MAX_ALIAS_HOPS = 6


def load_alias_map() -> tuple[dict[str, str], list[tuple[str, str]]]:
    """Return (exact rows, dir-prefix rows sorted longest-first).

    Longest-prefix-first mirrors `broken_dependency_checker`'s resolution order, so a single
    `designs/X/ -> systems/.../` pointer row resolves every file moved under it.
    """
    if not os.path.exists(LEDGER):
        return {}, []
    with open(LEDGER, encoding="utf-8") as fh:
        rows = ROW_RE.findall(fh.read())
    exact = {old: new for old, new in rows if not old.endswith("/")}
    prefix = sorted(
        ((old, new) for old, new in rows if old.endswith("/")),
        key=lambda pair: -len(pair[0]),
    )
    return exact, prefix


def resolve(path: str, exact: dict[str, str], prefix: list[tuple[str, str]]) -> str | None:
    """Follow the alias map (chained moves allowed) to a path that exists. None if unresolvable."""
    seen: set[str] = set()
    current = path
    for _ in range(_MAX_ALIAS_HOPS):
        if current in seen:
            return None  # cycle in the ledger
        seen.add(current)
        nxt = None
        if current in exact:
            nxt = exact[current]
        else:
            for old, new in prefix:
                if current.startswith(old):
                    nxt = new + current[len(old):]
                    break
        if nxt is None:
            return None
        if os.path.exists(os.path.join(ROOT, nxt)):
            return nxt
        current = nxt
    return None


def scan() -> dict:
    exact, prefix = load_alias_map()
    results: dict[str, dict[str, list]] = {}

    if not os.path.isdir(SCAN_DIR):
        return {"files": {}, "totals": {"live": 0, "aliased": 0, "dead": 0}}

    for name in sorted(os.listdir(SCAN_DIR)):
        # settings.json holds tool-permission names, not paths — skip to avoid false positives.
        if name == "settings.json" or not name.endswith((".js", ".json", ".mjs")):
            continue
        full = os.path.join(SCAN_DIR, name)
        if not os.path.isfile(full):
            continue
        with open(full, encoding="utf-8", errors="replace") as fh:
            text = fh.read()

        # Keep each match's line so prose and declared-absent findings can be filtered out.
        candidates: dict[str, str] = {}
        for line in text.split("\n"):
            for raw in PATH_RE.findall(line):
                candidates.setdefault(raw.rstrip(".,;:)"), line)

        live, aliased, dead = [], [], []
        for ref, line in sorted(candidates.items()):
            if not is_dependency(ref, line):
                continue
            if os.path.exists(os.path.join(ROOT, ref)):
                live.append(ref)
                continue
            target = resolve(ref, exact, prefix)
            (aliased.append({"ref": ref, "resolves_to": target}) if target else dead.append(ref))
        results[os.path.join(".claude", name)] = {
            "live": live, "aliased": aliased, "dead": dead,
        }

    totals = {
        "live": sum(len(v["live"]) for v in results.values()),
        "aliased": sum(len(v["aliased"]) for v in results.values()),
        "dead": sum(len(v["dead"]) for v in results.values()),
    }
    return {"files": results, "totals": totals}


def main(argv: list[str]) -> int:
    report = scan()
    if "--json" in argv:
        print(json.dumps(report, indent=2, sort_keys=True))
        return 1 if report["totals"]["dead"] else 0

    print("Claude Code apparatus — path resolution (.claude/)")
    print("=" * 68)
    for path, res in report["files"].items():
        n = len(res["live"]) + len(res["aliased"]) + len(res["dead"])
        if not n:
            continue
        print(f"\n{path}: {n} referenced | "
              f"{len(res['live'])} live | {len(res['aliased'])} aliased | {len(res['dead'])} DEAD")
        for item in res["aliased"]:
            print(f"    ALIASED  {item['ref']}\n             -> {item['resolves_to']}")
        for ref in res["dead"]:
            print(f"    DEAD     {ref}")

    t = report["totals"]
    total = t["live"] + t["aliased"] + t["dead"]
    print("\n" + "=" * 68)
    print(f"TOTAL {total} referenced | {t['live']} live | "
          f"{t['aliased']} aliased (undeclared indirection) | {t['dead']} DEAD")
    if t["dead"]:
        print(f"\n[GATE FAILED] {t['dead']} path(s) unresolvable by any sanctioned route.")
        return 1
    print("\n[GATE PASSED] every referenced path resolves.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
