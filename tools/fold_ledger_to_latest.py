#!/usr/bin/env python3
"""
fold_ledger_to_latest.py — the instrument plan position `1` (CLOSE-PASS) ships:
`workplans/2026-09-28-the-plan-one-order-mc-v18-retired.md` §3.1 item 1, carrying
`workplans/2026-09-18-governance-settlement-behaviour-plan_part2.md` §8 position 1's
original instruction ("ship the fold-to-latest script as its instrument").

Before this script, the open-queue count had four disagreeing figures (old plan §8.3):
108/158 (2026-09-11, a raw line count — double-counting any id with more than one row);
151/105 then 153/106 (`HANDOFF.md`, 2026-09-10); 41/51/77 by hand depending on the
predicate; 37 after folding append-only rows to the latest per id — computed by hand,
once, not reproducibly, against a tree this script cannot re-open, so it is not verified
to reproduce that specific number. What it is is A reproducible instrument for that KIND
of figure: read every `registers/editorial_ledger*.jsonl` file, live and archive, every
lane (`ci_common.editorial_ledger_paths()` — NOT the separate, older
`registers/archive/*.yaml` corpus, which this tool does not scan and cites by exact id
only, never by fragment), fold to the LAST row per id (the ED-IN-0149 precedent every
existing "SUPERSEDING ROW" ledger entry already cites), then count or list.

Usage:
    python tools/fold_ledger_to_latest.py --queue
        needs_jordan:true at any status, folded — HANDOFF.md's own definition of "rows
        awaiting Jordan" — plus the narrower status:open subset old plan position 1's
        OBSERVABLE text names.
    python tools/fold_ledger_to_latest.py --queue --list
        same, plus id, status, file:line and title/description head for every row counted.
    python tools/fold_ledger_to_latest.py --id ED-IN-0210
        one id's CURRENT (folded) row — how many rows it has, and the last one in full.
        Exact id only; it does not accept a fragment or a prefix.
    python tools/fold_ledger_to_latest.py --stats
        distinct ids folded, rows superseded by a later row for the same id, and a
        status histogram over the folded set.
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common


def _folded():
    rows = ci_common.read_editorial_ledger_rows()
    return rows, ci_common.fold_ledger_to_latest(rows)


def cmd_queue(args):
    """The primary count is `needs_jordan: true` at ANY status, folded to the latest row per
    id -- HANDOFF.md's own definition of "rows awaiting Jordan" (no status filter), and the
    one that matches reality: ED-IN-0210 (`status: ruled`), ED-IN-0261 (`partial`) and
    ED-IN-0247 (`resolved`) all carry `needs_jordan: true` in their current row and are all
    named as live, unresolved Jordan items elsewhere in this repo's own planning documents.

    The narrower `needs_jordan: true AND status: open` predicate is old plan position 1's own
    literal OBSERVABLE text (workplans/2026-09-18-governance-settlement-behaviour-plan_part2.md
    §8 position 1), written when "still needing Jordan" and `status: open` happened to
    coincide. They have since diverged -- a live item can carry `ruled`/`partial`/`resolved`
    while still being his to answer -- so a Terminal Phase-3 critique of this instrument's own
    first cut found that reporting ONLY the narrower predicate as "the queue" manufactures a
    fifth disagreeing figure instead of retiring the four this instrument was built to replace.
    Both counts are reported; the OBSERVABLE line is a citation of that literal text, not a
    claim that it measures the whole queue.
    """
    _rows, latest = _folded()
    needs_jordan = [
        (eid, path, line_no, entry)
        for eid, (path, line_no, entry) in latest.items()
        if entry.get('needs_jordan') is True
    ]
    needs_jordan.sort(key=lambda t: t[0])
    open_subset = [row for row in needs_jordan if row[3].get('status') == 'open']
    print(f"needs_jordan: true, folded to latest row per id, any status: {len(needs_jordan)}")
    print(f"  of which status: open (old plan position 1's literal OBSERVABLE predicate): "
          f"{len(open_subset)}")
    if args.list:
        for eid, path, line_no, entry in needs_jordan:
            title = entry.get('title') or (entry.get('description') or '')[:80]
            print(f"  {eid}  status={entry.get('status')!r}  {path}:{line_no}  {title}")
    return 0


def cmd_id(args):
    rows, latest = _folded()
    hit = latest.get(args.id)
    if hit is None:
        print(f"{args.id}: not found in any ledger", file=sys.stderr)
        return 1
    path, line_no, entry = hit
    all_rows = [r for r in rows if r[2].get('id') == args.id]
    print(f"{args.id}: {len(all_rows)} row(s); current (last) row at {path}:{line_no}")
    print(json.dumps(entry, indent=2, ensure_ascii=False))
    return 0


def cmd_stats(args):
    rows, latest = _folded()
    total_rows = len(rows)
    distinct = len(latest)
    statuses = {}
    for _eid, (_p, _l, entry) in latest.items():
        st = entry.get('status')
        statuses[st] = statuses.get(st, 0) + 1
    print(f"rows read: {total_rows}")
    print(f"distinct ids: {distinct}")
    print(f"rows superseded by a later row for the same id: {total_rows - distinct}")
    print("status histogram (folded, one row per id):")
    for st, n in sorted(statuses.items(), key=lambda kv: (-kv[1], str(kv[0]))):
        print(f"  {st!r}: {n}")
    return 0


def main():
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--queue', action='store_true',
                    help="needs_jordan:true (any status) folded, plus the status:open subset")
    p.add_argument('--list', action='store_true', help="with --queue, list each counted row")
    p.add_argument('--id', metavar='ED-ID', help="print one id's current folded row")
    p.add_argument('--stats', action='store_true', help="fold stats: distinct ids, histogram")
    args = p.parse_args()

    if args.id:
        return cmd_id(args)
    if args.stats:
        return cmd_stats(args)
    if args.queue:
        return cmd_queue(args)
    p.print_help()
    return 1


if __name__ == '__main__':
    sys.exit(main())
