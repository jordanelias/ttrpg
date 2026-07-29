#!/usr/bin/env python3
"""
ci_audit_registry_check.py — report-only freshness gate for references/audit_registry.jsonl.

Warns (never blocks — audit cadence is irregular/manual, unlike code) when an
audit/ entry newer than the registry's latest known date has no corresponding
record: a skill ran an audit but the append-on-completion step (CLAUDE.md-style
skill retrofit, see the 8 SKILL.md files' "Dashboard registry logging" sections)
silently didn't happen — a script bug, an edited skill that dropped the step,
or a manual run outside the skill.

Deliberately bounded to entries newer than the registry's current max date, not
the whole audit/ history — the one-time backfill (tools/build_audit_
registry_backfill.py) already covers history at whatever precision it could;
this check is the ongoing "did anything recent slip through" signal, mirroring
workplan_status.py's staleness() discipline for the workplan board.

AUDIT_DIR points at the LIVE `audit/` corpus (moved from `designs/audit/`
2026-07-18/19, ED-IN-0071 P4/P5 continuation; repointed here 2026-07-29, OI-53a
critic addition F14 — the stale `designs/audit/` path resolved to nothing, so
this check had been silently reporting "OK" with zero files ever scanned).
"""
import json
import os
import re
import sys

AUDIT_DIR = 'audit'
REGISTRY = os.path.join('references', 'audit_registry.jsonl')
DATE_RE = re.compile(r'^(\d{4}-\d{2}-\d{2})-')


def _registry_entries():
    if not os.path.exists(REGISTRY):
        return []
    entries = []
    with open(REGISTRY, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return entries


def _audit_dir_entries():
    if not os.path.isdir(AUDIT_DIR):
        return []
    out = []
    for name in sorted(os.listdir(AUDIT_DIR)):
        m = DATE_RE.match(name)
        if not m:
            continue
        full = os.path.join(AUDIT_DIR, name).replace(os.sep, '/')
        if os.path.isdir(os.path.join(AUDIT_DIR, name)):
            full += '/'
        out.append((m.group(1), full))
    return out


def main():
    registry = _registry_entries()
    known_folders = {r.get('folder') for r in registry if r.get('folder')}
    max_registered_date = max((r.get('date', '') for r in registry), default='')

    if not max_registered_date:
        print("[AUDIT REGISTRY INFO] registry is empty or missing — run "
              "deprecated/tools/build_audit_registry_backfill.py, then this check will have "
              "a baseline. (Retired 2026-07-29, ED-IN-0097/OI-15: zero invokers. It is a "
              "one-time backfill writer, still runnable from its retired home.)")
        return 0

    unregistered = [
        (date, folder) for date, folder in _audit_dir_entries()
        if date > max_registered_date and folder not in known_folders
    ]

    if not unregistered:
        print(f"[AUDIT REGISTRY OK] no {AUDIT_DIR}/ entries newer than the registry's "
              f"latest date ({max_registered_date}) are missing a record.")
        return 0

    print(f"[AUDIT REGISTRY WARN] {len(unregistered)} {AUDIT_DIR}/ entr{'y' if len(unregistered) == 1 else 'ies'} "
          f"newer than the registry's latest date ({max_registered_date}) have no matching record "
          f"(non-blocking — verify the owning skill's registry-append step actually ran):")
    for date, folder in unregistered:
        print(f"[AUDIT REGISTRY WARN]   - {date}  {folder}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
