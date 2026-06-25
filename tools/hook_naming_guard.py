#!/usr/bin/env python3
"""
hook_naming_guard.py — Claude Code PreToolUse(Write|Edit|MultiEdit) hook.

Edit-time, fast feedback for the one hard naming invariant: do not introduce
"Galbados" as a name (canonical is "Solmund"). It reuses the EXACT pure core of
the authoritative gate (tools/ci_naming_check.py) so there is no second copy of
the rule, and it inspects only the ADDED text of the edit, with the same path
exclusions — so it is not self-blocking on the files that legitimately use the token.

This is advisory speed; the authoritative naming gate is ci_naming_check.py in CI
and in the .githooks/pre-commit run. Reads the hook payload as JSON on stdin and
exits 2 to block the edit (surfacing stderr to Claude) when a violation is added.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_naming_check  # noqa: E402


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)  # never block on a malformed/absent payload

    ti = data.get('tool_input', {}) or {}
    path = ti.get('file_path', '') or ''

    # Collect the newly-added text across Write / Edit / MultiEdit shapes.
    added = []
    if ti.get('content'):
        added.append(ti['content'])
    if ti.get('new_string'):
        added.append(ti['new_string'])
    for e in (ti.get('edits') or []):
        if isinstance(e, dict) and e.get('new_string'):
            added.append(e['new_string'])

    hits = ci_naming_check.scan_text(path, '\n'.join(added))
    if hits:
        sys.stderr.write('NAMING: canonical name is "Solmund", never "Galbados".\n')
        for h in hits[:5]:
            sys.stderr.write(f'  + {h[:120]}\n')
        sys.stderr.write('If this is a legitimate historical/registry reference, add the '
                         'path to EXCLUDE in tools/ci_naming_check.py.\n')
        sys.exit(2)
    sys.exit(0)


if __name__ == '__main__':
    main()
