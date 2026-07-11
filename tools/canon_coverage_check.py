#!/usr/bin/env python3
"""
canon_coverage_check.py — bidirectional canonical-index coverage verification.

Checks that every file declaring `Status: CANONICAL` in its header is registered
in `references/canonical_sources.yaml` (and vice-versa, allowing _index/_infill
companions to inherit registration from their parent).

Surfaces drift between the file-level claim ("this file is canonical") and the
registry ("here are the canonical files"). Either direction breaking is a
consistency defect.

Usage (CLI):
    python3 tools/canon_coverage_check.py [--strict] [--json]

    --strict   exit 1 if any drift detected (for CI integration)
    --json     emit machine-readable report instead of text

Usage (in-session, hook-friendly):
    from tools.canon_coverage_check import run_check
    report = run_check()                      # reads references/canonical_sources.yaml
                                                # and walks designs/ from the working tree
    report = run_check(local_cs_yaml=text)    # use specific yaml content instead
    if report['unregistered_with_header'] or report['registered_no_header']:
        ...

Method (working-tree only — no network, per CLAUDE.md's working-tree-is-truth doctrine;
this previously used the GitHub code-search API, a direct violation of that doctrine,
ported out 2026-07-11, ED-IN-0031):
    1. Load `references/canonical_sources.yaml`. Recursively walk all string values;
       any value ending in .md / .yaml / .svg is "registered".
    2. Walk the working tree under `designs/` (os.walk) and read every `.md` file,
       checking its content for the literal header marker "Status: CANONICAL" — the
       same literal-string convention the prior GitHub-search query used
       (`"Status: CANONICAL" repo:... path:designs`), so the matched set is unchanged
       by the port. Files under `designs/audit/` are still excluded (audit reports
       that *describe* canonical content are not themselves canonical sources).
    3. Compute set difference both directions:
       - unregistered_with_header: declares CANONICAL, not in registry
       - registered_no_header: in registry under designs/, no header
    4. Report — either text (human) or json (machine).

Exit codes (when --strict):
    0  no drift in either direction
    1  drift detected
    2  unable to perform check (parse error, missing file)

Dependencies: stdlib + PyYAML (already in container). No network calls.

Related:
    - designs/audit/2026-05-10-canonical-index-audit/canon_coverage_drift.yaml
      — last full snapshot; this script regenerates it on demand.
    - references/canonical_sources.yaml — the registry under check.
"""

from __future__ import annotations
import os
import sys
import json
import argparse
from typing import Iterable

import yaml


_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESIGNS_DIR = os.path.join(_REPO_ROOT, 'designs')
CANONICAL_SOURCES_PATH = os.path.join(_REPO_ROOT, 'references', 'canonical_sources.yaml')
STATUS_MARKER = 'Status: CANONICAL'


# ── Walking the registry ─────────────────────────────────────────────────────

def _walk_paths(obj) -> Iterable[str]:
    """Yield every string value reachable in obj that looks like a repo path."""
    if isinstance(obj, dict):
        for v in obj.values():
            yield from _walk_paths(v)
    elif isinstance(obj, list):
        for x in obj:
            yield from _walk_paths(x)
    elif isinstance(obj, str):
        if obj.endswith('.md') or obj.endswith('.yaml') or obj.endswith('.svg'):
            yield obj


def registered_paths(canonical_sources_yaml_text: str) -> set[str]:
    """Set of all repo paths reachable as string values in canonical_sources.yaml."""
    data = yaml.safe_load(canonical_sources_yaml_text) or {}
    return set(_walk_paths(data))


# ── Walking declared-canonical headers ───────────────────────────────────────

def declared_canonical_files(designs_dir: str | None = None) -> set[str]:
    """
    Set of designs/ files (repo-relative paths, forward-slash) whose content
    contains the literal "Status: CANONICAL".

    Pure working-tree walk (os.walk under designs/) — no network. Matches the
    same literal-string convention the prior GitHub code-search query used
    ("Status: CANONICAL" as a phrase, anywhere in the file). Extension set
    (.md/.yaml/.svg) matches registered_paths' — a couple of real canonical
    sources are .yaml/.svg, not .md.

    Files under designs/audit/ are excluded — these are audit reports that may
    *describe* canonical content but are not themselves canonical sources. The
    audit subtree is the natural home for the diagnostic snapshots produced by
    this tool, and including them would create a self-referential false positive.
    """
    root = designs_dir or DESIGNS_DIR
    files: set[str] = set()
    for dirpath, dirnames, filenames in os.walk(root):
        relroot = os.path.relpath(dirpath, _REPO_ROOT).replace(os.sep, '/')
        if relroot == 'designs/audit' or relroot.startswith('designs/audit/'):
            dirnames[:] = []  # don't descend into designs/audit/
            continue
        for fn in filenames:
            # Match registered_paths' extension set (line 83) exactly — the registry
            # can name .md/.yaml/.svg files, and a couple of real canonical sources
            # (e.g. designs/territory/valoria_geography_v30.yaml,
            # valoria_map_v30.svg) carry the "Status: CANONICAL" marker in a
            # header comment despite not being Markdown. Restricting this walk to
            # .md only (as an earlier version of this fix did) silently drops
            # those from the declared set and produces false-positive
            # registered_no_header drift — caught in adversarial review of
            # ED-IN-0031.
            if not (fn.endswith('.md') or fn.endswith('.yaml') or fn.endswith('.svg')):
                continue
            fpath = os.path.join(dirpath, fn)
            relpath = os.path.relpath(fpath, _REPO_ROOT).replace(os.sep, '/')
            try:
                with open(fpath, encoding='utf-8', errors='strict') as f:
                    content = f.read()
            except (OSError, UnicodeDecodeError):
                continue
            if STATUS_MARKER in content:
                files.add(relpath)
    return files


# ── Coverage report ───────────────────────────────────────────────────────────

def run_check(
    local_cs_yaml: str | None = None,
) -> dict:
    """
    Run the bidirectional coverage check; return a report dict.

    local_cs_yaml: if provided, use this content for canonical_sources.yaml
                   (e.g. for pre-commit checks against staged content).
                   If None, read references/canonical_sources.yaml from the
                   working tree.
    """
    if local_cs_yaml is None:
        cs_text = _read_canonical_sources()
    else:
        cs_text = local_cs_yaml

    registered = registered_paths(cs_text)
    declared = declared_canonical_files()

    unregistered_with_header = sorted(declared - registered)
    registered_no_header = sorted(
        p for p in (registered - declared) if p.startswith('designs/')
    )

    return {
        'totals': {
            'declared_canonical': len(declared),
            'registered_paths_total': len(registered),
            'registered_paths_designs_only': len(
                [p for p in registered if p.startswith('designs/')]
            ),
            'unregistered_with_header': len(unregistered_with_header),
            'registered_no_header': len(registered_no_header),
        },
        'unregistered_with_header': unregistered_with_header,
        'registered_no_header': registered_no_header,
    }


def _read_canonical_sources() -> str:
    """Read references/canonical_sources.yaml from the working tree (no network)."""
    with open(CANONICAL_SOURCES_PATH, encoding='utf-8') as f:
        return f.read()


# ── CLI ───────────────────────────────────────────────────────────────────────

def _format_text(report: dict) -> str:
    t = report['totals']
    lines = [
        '== Canonical-index coverage check ==',
        f"  Files declaring Status: CANONICAL (designs/): {t['declared_canonical']}",
        f"  Paths registered in canonical_sources.yaml:  {t['registered_paths_total']} "
        f"(designs/-only: {t['registered_paths_designs_only']})",
        '',
        f"  Unregistered with header: {t['unregistered_with_header']}",
        f"  Registered without header (designs/): {t['registered_no_header']}",
    ]
    if report['unregistered_with_header']:
        lines.append('')
        lines.append('  Files declaring CANONICAL but not in registry:')
        for p in report['unregistered_with_header']:
            lines.append(f'    - {p}')
    if report['registered_no_header']:
        lines.append('')
        lines.append('  Files in registry but not declaring CANONICAL header:')
        for p in report['registered_no_header']:
            lines.append(f'    - {p}')
    if not (report['unregistered_with_header'] or report['registered_no_header']):
        lines.append('')
        lines.append('  CLEAN — no drift detected.')
    return '\n'.join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split('\n')[1])
    parser.add_argument(
        '--strict', action='store_true',
        help='Exit 1 if any drift detected (for CI).',
    )
    parser.add_argument(
        '--json', action='store_true',
        help='Emit machine-readable report instead of text.',
    )
    args = parser.parse_args()

    try:
        report = run_check()
    except Exception as e:
        print(f'ERROR: {e}', file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(_format_text(report))

    if args.strict and (
        report['unregistered_with_header'] or report['registered_no_header']
    ):
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
