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

import glob
import json
import os
import re
import sys

# ONE OWNER for the repo root, the 9-lane roster, token estimation and the id
# regexes: tools/ci_common.py (plan G7, ED-IN-0159 §8.3). The two lines below are
# the irreducible bootstrap — a module cannot import its owner without first
# knowing where the owner is — and they anchor on THIS FILE's directory, never on
# the repo root, so they are not the duplication they replace.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = ci_common.REPO   # ONE OWNER (plan G7, ED-IN-0159 §8.3)
LEDGER = os.path.join(ROOT, "references", "restructure_ledger.md")
SCAN_DIR = os.path.join(ROOT, ".claude")

# WIDENED (2026-07-29). The `.claude/` scan above exists because the `designs/`/`sim/` retirements
# silently broke path references. The IDENTICAL hazard in `.github/workflows/*.yml` was unguarded,
# and it bit: `contract-conformance` passed `--registry designs/architecture/key_type_registry_v30.md`
# from the 2026-07-19 `designs/` retirement until 2026-07-29 — ~10 days of `FileNotFoundError`,
# masked by the step's `continue-on-error: true`, reporting green while scanning nothing.
#
# ALIAS POLICY — the load-bearing difference, and the reason a naive widening would have been
# DECORATION. A `.claude/` prompt is read by an AGENT, which can consult
# `references/restructure_ledger.md` and find the moved file: ALIASED is degraded, not dead. A
# workflow `run:` line is executed by a SHELL, and `open()` does not consult the ledger: for an
# executed command ALIASED is FATAL. Verified — the alias map DOES resolve the dead path above to
# `systems/_architecture/key_type_registry_v30.md`, so classifying it ALIASED would have passed the
# gate on the exact defect it was written to catch.
#
# Comments inside a workflow are prose, not commands, so they keep the agent-readable alias policy
# (a citation to a retired path is legitimate — CLAUDE.md §3's alias map is the sanctioned route).
SCAN_TARGETS = (
    # (dir relative to ROOT, file extensions, alias_is_fatal_for_executed_lines)
    (".claude", (".js", ".json", ".mjs"), False),
    (os.path.join(".github", "workflows"), (".yml", ".yaml"), True),
)

# Top-level trees a repo-relative path can start with. `designs/` and `sim/` are retired and are
# included deliberately — a reference to them is the failure this tool looks for.
TREES = (
    "designs", "sim", "systems", "engine", "references", "params", "tests",
    "registers", "canon", "audit", "arcs", "godot", "tools", "skills", "proposals",
    "workplans", "deprecated",
)
# `*` is inside the class so a GLOB is captured whole. Workflow `paths:` trigger filters are
# legitimately globs (`registers/editorial_ledger*.jsonl`); truncating at the `*` yields a
# path that never exists and reports a false DEAD. Globs resolve via glob.glob, not os.path.exists.
PATH_RE = re.compile(r"\b(?:%s)/[A-Za-z0-9_.*/-]+" % "|".join(TREES))

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


def resolve_glob(pattern: str, prefix: list[tuple[str, str]]) -> str | None:
    """Alias-resolve a GLOB pattern. `resolve()` cannot be reused: it tests os.path.exists, which is
    always False for a pattern. Rewrite through the dir-prefix rows and re-glob instead."""
    for old, new in prefix:  # already sorted longest-first
        if pattern.startswith(old):
            candidate = new + pattern[len(old):]
            if glob.glob(os.path.join(ROOT, candidate)):
                return candidate
    return None


def scan() -> dict:
    exact, prefix = load_alias_map()
    results: dict[str, dict[str, list]] = {}

    for scan_rel, exts, alias_fatal in SCAN_TARGETS:
        scan_dir = os.path.join(ROOT, scan_rel)
        if not os.path.isdir(scan_dir):
            continue

        for name in sorted(os.listdir(scan_dir)):
            # settings.json holds tool-permission names, not paths — skip to avoid false positives.
            if name == "settings.json" or not name.endswith(exts):
                continue
            full = os.path.join(scan_dir, name)
            if not os.path.isfile(full):
                continue
            with open(full, encoding="utf-8", errors="replace") as fh:
                text = fh.read()

            # Keep each match's line so prose and declared-absent findings can be filtered out.
            # `executed` distinguishes a shell command from a comment: only the former is bound by
            # the fatal-alias policy, because only the former is run by a shell that cannot follow
            # the restructure ledger.
            candidates: dict[str, tuple[str, bool]] = {}
            for line in text.split("\n"):
                executed = not line.lstrip().startswith("#")
                for raw in PATH_RE.findall(line):
                    candidates.setdefault(raw.rstrip(".,;:)"), (line, executed))

            live, aliased, dead = [], [], []
            for ref, (line, executed) in sorted(candidates.items()):
                if not is_dependency(ref, line):
                    continue
                if "*" in ref:
                    # A glob is live when it matches at least one file on disk. It gets the same
                    # alias treatment as a plain path — `params/*.md` must resolve through the
                    # `params/ -> engine/params/` row (ED-IN-0071 P3) rather than read as dead.
                    if glob.glob(os.path.join(ROOT, ref)):
                        live.append(ref)
                        continue
                    target = resolve_glob(ref, prefix)
                    if not target:
                        dead.append(f"{ref} (glob matches nothing)")
                    elif alias_fatal and executed:
                        dead.append(
                            f"{ref} (alias-only -> {target}; a shell cannot follow the ledger)")
                    else:
                        aliased.append({"ref": ref, "resolves_to": target})
                    continue
                if os.path.exists(os.path.join(ROOT, ref)):
                    live.append(ref)
                    continue
                target = resolve(ref, exact, prefix)
                if not target:
                    dead.append(ref)
                elif alias_fatal and executed:
                    # An alias a shell cannot follow is a break, not an indirection.
                    dead.append(f"{ref} (alias-only -> {target}; a shell cannot follow the ledger)")
                else:
                    aliased.append({"ref": ref, "resolves_to": target})
            results[os.path.join(scan_rel, name)] = {
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

    print("Apparatus path resolution (.claude/ + .github/workflows/)")
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
