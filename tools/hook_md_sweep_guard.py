#!/usr/bin/env python3
"""
hook_md_sweep_guard.py — a PreToolUse hook that stops `.md` design documents being SWEPT.

WHY (Jordan, 2026-08-24)
------------------------
    "unless I specifically mention prose or documents, I do not want any .md documents
     scanned as they are all going to drift or be stale or inconsistent with most current
     codebase"

and, one instruction earlier:

    "whatever mechanisms we have that rely on prose are worthless."

Which is exactly why this is a HOOK and not a paragraph in CLAUDE.md. A rule telling the agent
not to sweep `.md` is itself prose, and prose is what the ruling just demoted. The harness runs
this file; that makes it a mechanism.

WHAT IT BLOCKS — only the SWEEP, never a deliberate read
--------------------------------------------------------
It intercepts `Grep` and `Glob` and blocks a call ONLY when the call would rake in markdown
indiscriminately:

  * `Glob` whose pattern targets markdown broadly (`**/*.md`, `systems/**/*.md`, `*.md`)
  * `Grep` restricted to markdown via `glob`/`type` (e.g. `--include=*.md`)
  * `Grep` with NO path and NO glob — an unscoped repo-wide sweep, which rakes in every `.md`
    in the tree as a side effect

It does NOT block, because none of these is a sweep:

  * `Read` — always allowed. Naming a file IS the explicit reference.
  * `Grep`/`Glob` scoped to a non-markdown tree (`engine/`, `systems/**/*.py`, `tools/`)
  * any call naming a specific `.md` path — that is an explicit reference
  * any call whose pattern or path mentions a MACHINE-READ markdown input (see below)

⚠ SOME `.md` FILES ARE CODE INPUTS AND MUST STAY SEARCHABLE. `systems/_architecture/
key_type_registry_v30.md` is the authored schema of the Key bus; `references/
restructure_ledger.md` is the path-resolution table; `CURRENT.md` and `HANDOFF.md` are read by
`currency_consistency_check`. Those are not reference documents, they are inputs, and a guard
that blocked them would break real work. The allowlist is DERIVED from code by
`triage_work_items.machine_read_inputs()`, not hardcoded here — so a markdown file becomes
searchable the moment code starts reading it, and stops when code stops.

ESCAPE HATCH, deliberate and explicit: set `VALORIA_ALLOW_MD_SWEEP=1` for a session that is
genuinely doing prose work — which is the case the ruling carves out ("unless I specifically
mention prose or documents").

Exit codes follow the Claude Code hook contract: 0 allow, 2 block with the message on stderr.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

_MD_BROAD = re.compile(r'\*\*?/?\*?\.md$|\*\.md$|\.md["\']?$')


def _machine_read_md():
    """Markdown filenames that CODE reads. Derived, never listed — see the module docstring."""
    try:
        import triage_work_items as T
        return {n for n in T.machine_read_inputs() if n.endswith('.md')}
    except Exception:
        # Fail OPEN, never closed: a guard that blocks everything when its helper breaks is worse
        # than the drift it prevents. The naming guard makes the same choice.
        return None


def verdict(tool: str, ti: dict):
    """(blocked: bool, message: str). Pure — unit-testable without the harness."""
    if os.environ.get('VALORIA_ALLOW_MD_SWEEP') == '1':
        return False, ''
    if tool not in ('Grep', 'Glob'):
        return False, ''

    pattern = str(ti.get('pattern') or '')
    path = str(ti.get('path') or '')
    g = str(ti.get('glob') or '')
    typ = str(ti.get('type') or '')
    blob = f'{pattern} {path} {g} {typ}'

    allow = _machine_read_md()
    if allow is None:
        return False, ''
    if any(name in blob for name in allow):
        return False, ''                      # names a markdown file code reads → an input

    # A specific .md path is an explicit reference, not a sweep.
    named = re.findall(r'[A-Za-z0-9_./-]+\.md\b', blob)
    if named and not any(_MD_BROAD.search(n) or '*' in n for n in named):
        return False, ''

    if tool == 'Glob' and _MD_BROAD.search(pattern.strip()):
        return True, f'Glob pattern {pattern!r} rakes in markdown across the tree.'
    if tool == 'Grep':
        if _MD_BROAD.search(g.strip()) or typ.strip() in ('md', 'markdown'):
            return True, f'Grep is restricted to markdown ({g or typ}).'
        if not path and not g and not typ:
            return True, ('Grep has no `path`, `glob` or `type`, so it sweeps the whole tree '
                          'including every design document.')
    return False, ''


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    tool = payload.get('tool_name') or payload.get('tool') or ''
    ti = payload.get('tool_input') or payload.get('input') or {}
    blocked, why = verdict(tool, ti)
    if not blocked:
        return 0
    sys.stderr.write(
        f'MD SWEEP BLOCKED: {why}\n'
        '  `.md` design documents are REFERENCE ONLY (CLAUDE.md §0.05) and drift against the code, '
        'so sweeping them yields stale answers.\n'
        '  Do one of these instead:\n'
        '    - scope the search to code:   path="engine/" or glob="**/*.py"\n'
        '    - name the document you mean: Read("systems/combat/combat_v30.md")\n'
        '    - if you are genuinely doing PROSE work, run with VALORIA_ALLOW_MD_SWEEP=1\n'
        '  Markdown that CODE reads (the Key-type registry, the restructure ledger, CURRENT.md, '
        'HANDOFF.md) is NOT blocked — those are inputs, not reference.\n')
    return 2


if __name__ == '__main__':
    sys.exit(main())
