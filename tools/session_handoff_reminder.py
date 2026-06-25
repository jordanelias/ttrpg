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
sys.exit(0)
