#!/usr/bin/env python3
"""
session_status.py — Claude Code SessionStart hook.

Plain-language status banner: the executive transparency view that replaces the
dead quick_bootstrap() STATUS BLOCK. No session token, no GitHub API, no harness —
just git + HANDOFF.md. stdout is surfaced into the session at start/resume.
"""
import os
import subprocess
import sys


def sh(args):
    r = subprocess.run(['git'] + args, capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else ''


def main():
    print("=== Valoria — session status ===")
    branch = sh(['rev-parse', '--abbrev-ref', 'HEAD'])
    if branch:
        print(f"branch:      {branch}")
    last = sh(['log', '-1', '--oneline'])
    if last:
        print(f"last commit: {last}")
    status = sh(['status', '--porcelain'])
    if status:
        print(f"working tree: {len(status.splitlines())} uncommitted change(s)")
    else:
        print("working tree: clean")

    # currency drift (ED-1087): one line from the self-updating recency gate — stamps,
    # ID ceilings, register headers, dead maintainers. Import (one rule, one home);
    # never allowed to break session start.
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import currency_consistency_check as ccc
        print(ccc.summary_line())
    except Exception:
        pass

    # workplan position (ED-IN-0010): one line from the progress board + staleness flag.
    # Renderer lives once in workplan_status.py; never allowed to break session start.
    try:
        import workplan_status as wps
        print(wps.summary_line())
        warn = wps.staleness()
        if warn:
            print(warn)
    except Exception:
        pass

    # Repository State Armature (ED-IN-0077): one-line repo-state grade from the single review
    # engine. fast=True reads the last committed review_state.json only (no subprocess, no hang);
    # silent if absent. Renderer lives once in review_core.py; never allowed to break session start.
    try:
        import review_core
        for ln in review_core.summary_lines(fast=True):
            print(ln)
    except Exception:
        pass

    # Open-work block (ED-IN-0081): the surfaces that were silently missed at start —
    # the ACTIVE LANE's HANDOFF_<LANE>.md pending items, open editorial debt (+ the
    # needs_jordan inbox), schema-in-flux flags, and ALL stale audit families (not just
    # the top-2). Composed once in session_open_work.py from the obs_core / audit_staleness
    # single-owner primitives; never allowed to break session start.
    try:
        import session_open_work as sow
        lines = sow.summary_lines()
        if lines:
            print()
            print('\n'.join(lines))
    except Exception:
        pass

    if os.path.exists('HANDOFF.md'):
        try:
            with open('HANDOFF.md', encoding='utf-8', errors='replace') as f:
                lines = f.read().splitlines()
        except OSError:
            lines = []
        out, grab = [], False
        for ln in lines:
            if ln.strip().lower().startswith('## next'):
                grab = True
                out.append(ln)
                continue
            if grab and ln.startswith('## '):
                break
            if grab:
                out.append(ln)
        if out:
            print()
            print('\n'.join(out[:12]))
    else:
        print("(no HANDOFF.md yet — create one to capture next actions)")

    sys.exit(0)


if __name__ == '__main__':
    main()
