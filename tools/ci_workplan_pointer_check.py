#!/usr/bin/env python3
"""
ci_workplan_pointer_check.py — the workplans pointer guard (ED-IN-0103).

WHY THIS EXISTS. Jordan ruled 2026-07-29 that every plan — workplan, session plan,
implementation schedule, execution plan, remediation plan, roadmap — must either live
directly in `workplans/` or have a pointer file there. A convention with no guard is the
CLAUDE.md §0.1 point-5 anti-pattern: it propagates by imitation and rots silently. This
program exists because of exactly that failure mode at a larger scale — `references/registry/
README.md` was cited as authoritative from five places and had never existed, because nothing
checked prose path references.

So a pointer file whose `target:` does not resolve is the same defect the program was created
to hunt, sitting inside the program's own deliverable. This guard closes that.

WHAT IT CHECKS (deterministic half only — see the LIMIT below)
  1. Every `workplans/POINTER_*.md` parses and carries the five required fields.
  2. Every `target:` resolves to a real file in the working tree.
  3. No two pointers name the same target.
  4. `lane:` names a real lane code from the 9-lane roster, or is explicitly qualified.

WHAT IT DELIBERATELY DOES NOT CHECK (the LIMIT, stated plainly). It does NOT verify that
every live plan HAS a pointer. That requires a liveness oracle, and the 2026-07-29 triage
measured that liveness is not mechanically inferable: a `## Status:` heading is not a signal
in either direction (only 10 of 58 plan-shaped files carry one; 7 of those 10 are dead; 3 of
the 7 live plans carry one). Guessing would produce exactly the wrong-in-both-directions
result the convention's `liveness:` field exists to prevent. That half stays a docket
question. This tool guards the half that IS deterministic — which is the whole point of
§0.1 point 5: ship the guard you can actually write, and say which half you did not.

Report-only by default (exit 0) so it can be wired on the names-drift graduation lane;
`--strict` exits 1 on any violation.

CLI:
    python3 tools/ci_workplan_pointer_check.py [--strict]
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys

# Primitives (repo root, lane roster, token estimate, ids, Status reader) are
# owned by tools/ci_common.py — plan G7, ED-IN-0159 §8.3. See its module docstring;
# the two lines below are the bootstrap, anchored on THIS file's directory.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402

ROOT = ci_common.REPO
POINTER_GLOB = os.path.join(ROOT, "workplans", "POINTER_*.md")

# The 9-lane roster (CLAUDE.md §4). `tools/observability/obs_core.py` owns this list for the
# observability generators; it is restated here rather than imported because obs_core lives
# under tools/observability/ and importing across that boundary for one tuple would couple a
# CI gate to the observability package's import graph. If the roster ever changes, both move.
# ONE OWNER: ci_common.LANE_CODES (plan G7, ED-IN-0159 §8.3). Was a verbatim
# copy of the 9-code tuple; obs_core's header records that one such copy once
# silently omitted GO, undercounting a whole lane.
LANE_CODES = ci_common.LANE_CODES

REQUIRED_FIELDS = ("target", "lane", "liveness", "scope")

_FIELD_RE = {
    f: re.compile(r"^\*\*%s:\*\*\s*(.+)$" % f, re.M | re.I) for f in REQUIRED_FIELDS
}
# `ED:` is required but shares a line with `lane:` in the house format, so it is matched
# separately and permitted to read "none" with a justification.
_ED_RE = re.compile(r"\*\*ED:\*\*\s*(.+?)(?:\n|$)", re.I)
_TARGET_PATH_RE = re.compile(r"`([^`]+)`")


def _pointers() -> list:
    return sorted(glob.glob(POINTER_GLOB))


def check(strict: bool = False) -> int:
    pointers = _pointers()
    violations = []
    seen_targets = {}
    checked = 0

    for path in pointers:
        rel = os.path.relpath(path, ROOT)
        with open(path, encoding="utf-8") as fh:
            body = fh.read()

        # 1. required fields
        for field in REQUIRED_FIELDS:
            if not _FIELD_RE[field].search(body):
                violations.append(f"{rel}: missing required field `{field}:`")
        if not _ED_RE.search(body):
            violations.append(f"{rel}: missing required field `ED:`")

        # 2. target resolves
        m = _FIELD_RE["target"].search(body)
        if m:
            raw = m.group(1).strip()
            pm = _TARGET_PATH_RE.search(raw)
            target = pm.group(1) if pm else raw.split()[0]
            abs_target = os.path.join(ROOT, target)
            checked += 1
            if not os.path.exists(abs_target):
                violations.append(
                    f"{rel}: target does not resolve -> {target} "
                    f"(a pointer to a nonexistent plan is the defect this guard exists for)"
                )
            # 3. duplicate targets
            if target in seen_targets:
                violations.append(
                    f"{rel}: duplicate target, already claimed by {seen_targets[target]} -> {target}"
                )
            else:
                seen_targets[target] = rel

        # 4. lane resolves
        lm = _FIELD_RE["lane"].search(body)
        if lm:
            lane_text = lm.group(1)
            if not any(code in lane_text for code in LANE_CODES):
                violations.append(
                    f"{rel}: lane field names no lane from the 9-lane roster -> {lane_text[:60]}"
                )

    # A loop that asserts conditionally must assert that it asserted (CLAUDE.md §0.1 point 2).
    if pointers and checked == 0:
        violations.append(
            "found POINTER_*.md files but resolved zero targets — the field regex has drifted "
            "from the house format and this guard is scanning nothing"
        )

    print(f"[workplan-pointers] {len(pointers)} pointer file(s), {checked} target(s) resolved.")
    if violations:
        for v in violations:
            print(f"  [VIOLATION] {v}")
        print(f"\n{len(violations)} violation(s).")
        return 1 if strict else 0
    print("  All pointers well-formed and every target resolves.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 on any violation (default: report-only, exit 0)")
    args = ap.parse_args()
    return check(strict=args.strict)


if __name__ == "__main__":
    sys.exit(main())
