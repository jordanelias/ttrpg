#!/usr/bin/env python3
"""Verify every location claimed by the divergence audit actually resolves.

This is the falsifier artifact for `01_locations.tsv` (CLAUDE.md §0.1 point 3): a location
log is only worth something if every row is mechanically checkable. Run it and the claim
"these 400 sites exist and say what the audit says they say" becomes falsifiable rather
than asserted.

    python audit/2026-08-11-divergence-audit/verify_locations.py

Input format — `01_locations.tsv`, tab-separated, `#` comments and blank lines ignored:

    group   path   line   expect   note

`expect` is a substring that must appear on `path:line`. Use `--fuzz N` to accept a match
within +/- N lines (reports the drift so a stale line number is visible rather than silently
tolerated). An empty `expect` checks only that the line exists.

Exit status is 1 if any row fails, so this is usable as a gate.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DEFAULT_TSV = Path(__file__).resolve().parent / "01_locations.tsv"

OK = "OK"
DRIFT = "DRIFT"
MISMATCH = "MISMATCH"
OUT_OF_RANGE = "OUT_OF_RANGE"
NO_FILE = "NO_FILE"
BAD_ROW = "BAD_ROW"


def _load(tsv: Path) -> list[dict]:
    rows = []
    for n, raw in enumerate(tsv.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.rstrip("\n")
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 3:
            rows.append({"row": n, "status": BAD_ROW, "raw": line})
            continue
        group, path, lineno = parts[0], parts[1], parts[2]
        expect = parts[3] if len(parts) > 3 else ""
        note = parts[4] if len(parts) > 4 else ""
        rows.append(
            {
                "row": n,
                "group": group.strip(),
                "path": path.strip(),
                "line": lineno.strip(),
                "expect": expect,
                "note": note,
                "status": None,
            }
        )
    return rows


def _read_lines(path: Path, cache: dict[Path, list[str] | None]) -> list[str] | None:
    if path not in cache:
        try:
            cache[path] = path.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            cache[path] = None
    return cache[path]


def verify(rows: list[dict], fuzz: int) -> list[dict]:
    cache: dict[Path, list[str] | None] = {}
    for r in rows:
        if r["status"] == BAD_ROW:
            continue
        target = REPO / r["path"]
        lines = _read_lines(target, cache)
        if lines is None:
            r["status"] = NO_FILE
            continue
        try:
            want = int(r["line"])
        except ValueError:
            r["status"] = BAD_ROW
            r["detail"] = f"non-integer line {r['line']!r}"
            continue
        if not (1 <= want <= len(lines)):
            r["status"] = OUT_OF_RANGE
            r["detail"] = f"file has {len(lines)} lines"
            continue

        actual = lines[want - 1]
        r["actual"] = actual.strip()
        expect = r["expect"].strip()
        if not expect:
            r["status"] = OK
            continue
        if expect in actual:
            r["status"] = OK
            continue

        # Report drift rather than tolerate it silently: find the nearest line that matches.
        found = None
        for delta in range(1, fuzz + 1):
            for cand in (want - delta, want + delta):
                if 1 <= cand <= len(lines) and expect in lines[cand - 1]:
                    found = cand
                    break
            if found:
                break
        if found:
            r["status"] = DRIFT
            r["detail"] = f"found at line {found} ({found - want:+d})"
        else:
            r["status"] = MISMATCH
            r["detail"] = f"expected {expect!r}"
    return rows


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("tsv", nargs="?", default=str(DEFAULT_TSV))
    ap.add_argument(
        "--fuzz",
        type=int,
        default=0,
        help="accept a match within +/- N lines, reporting the drift (default 0 = strict)",
    )
    ap.add_argument("--quiet", action="store_true", help="summary only")
    args = ap.parse_args()

    tsv = Path(args.tsv)
    if not tsv.exists():
        print(f"no such file: {tsv}", file=sys.stderr)
        return 2

    rows = verify(_load(tsv), args.fuzz)
    counts = Counter(r["status"] for r in rows)

    bad = [r for r in rows if r["status"] not in (OK,)]
    if bad and not args.quiet:
        for r in bad:
            if r["status"] == BAD_ROW and "raw" in r:
                print(f"{BAD_ROW:13} line {r['row']}: {r['raw'][:100]}")
                continue
            loc = f"{r.get('path')}:{r.get('line')}"
            detail = r.get("detail", "")
            print(f"{r['status']:13} [{r.get('group','')}] {loc}  {detail}")
            if r.get("actual") is not None:
                print(f"{'':13}   actual: {r['actual'][:110]}")

    total = len(rows)
    print()
    print(f"rows: {total}")
    for status in (OK, DRIFT, MISMATCH, OUT_OF_RANGE, NO_FILE, BAD_ROW):
        if counts.get(status):
            print(f"  {status:13} {counts[status]}")

    groups = Counter(r.get("group", "") for r in rows if r["status"] != BAD_ROW)
    print(f"groups: {len(groups)}")

    # DRIFT is a failure too: a location log whose line numbers have moved is exactly the
    # thing this file exists to catch, and tolerating it would make the log rot silently.
    return 1 if (total - counts.get(OK, 0)) else 0


if __name__ == "__main__":
    raise SystemExit(main())
