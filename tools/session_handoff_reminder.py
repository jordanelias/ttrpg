#!/usr/bin/env python3
"""
session_handoff_reminder.py — Claude Code Stop hook.

If the working tree is dirty when a turn ends, nudge to update HANDOFF.md. This
replaces the old context_gate()/checkpoint token-budget plumbing with zero token
math. It NEVER blocks stopping (always exits 0).
"""
import subprocess
import sys

r = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
if r.returncode == 0 and r.stdout.strip():
    print("Working tree has uncommitted changes — consider committing or updating HANDOFF.md before ending.")

# Progress-board nudge (ED-IN-0010): if the workplan progress board's as_of is behind
# HEAD, suggest a refresh (valoria-workplan-navigator Workflow C). Staleness logic lives
# once, in workplan_status.py. Advisory only; never blocks.
try:
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import workplan_status as wps
    warn = wps.staleness()
    if warn:
        print(warn + " — consider a board refresh (valoria-workplan-navigator Workflow C).")
except Exception:
    pass
sys.exit(0)
