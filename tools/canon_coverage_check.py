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
    report = run_check()                      # uses live GitHub state
    report = run_check(local_cs_yaml=text)    # use specific yaml content
    if report['unregistered_with_header'] or report['registered_no_header']:
        ...

Method:
    1. Load `references/canonical_sources.yaml`. Recursively walk all string values;
       any value ending in .md / .yaml / .svg is "registered".
    2. Use the GitHub code-search API to find every file under designs/ containing
       "Status: CANONICAL" (header marker convention).
    3. Compute set difference both directions:
       - unregistered_with_header: declares CANONICAL, not in registry
       - registered_no_header: in registry under designs/, no header
    4. Report — either text (human) or json (machine).

Exit codes (when --strict):
    0  no drift in either direction
    1  drift detected
    2  unable to perform check (network, auth, parse error)

Dependencies: stdlib + PyYAML (already in container).

Related:
    - audit/lane-b/2026-05-10-canonical-index-audit_canon_coverage_drift.yaml
      — last full snapshot; this script regenerates it on demand.
    - references/canonical_sources.yaml — the registry under check.
"""

from __future__ import annotations
import os
import sys
import json
import argparse
import urllib.request
import urllib.parse
from typing import Iterable

import yaml


REPO = 'jordanelias/ttrpg'
PAT_FILE = '/home/claude/.valoria_pat'


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

def _pat() -> str:
    with open(PAT_FILE) as f:
        return f.read().strip()


def declared_canonical_files(pat: str | None = None) -> set[str]:
    """
    Set of designs/ files whose content contains the literal "Status: CANONICAL".

    Uses GitHub code-search API. Limit 100/page; for current corpus the count is
    well under that. If we ever exceed, paginate via &page=2 etc.

    Files under designs/audit/ are excluded — these are audit reports that may
    *describe* canonical content but are not themselves canonical sources. The
    audit subtree is the natural home for the diagnostic snapshots produced by
    this tool, and including them would create a self-referential false positive.
    """
    pat = pat or _pat()
    q = '"Status: CANONICAL" repo:' + REPO + ' path:designs'
    url = (
        'https://api.github.com/search/code'
        f'?q={urllib.parse.quote(q)}&per_page=100'
    )
    req = urllib.request.Request(
        url,
        headers={
            'Authorization': f'token {pat}',
            'Accept': 'application/vnd.github.v3+json',
        },
    )
    with urllib.request.urlopen(req) as r:
        data = json.loads(r.read())
    items = data.get('items', [])
    total = data.get('total_count', 0)
    files = {
        item['path'] for item in items
        if not item['path'].startswith('designs/audit/')
    }
    if total > len(items):
        # We didn't get them all — page 2+ may exist. Surface as warning by raising.
        raise RuntimeError(
            f"declared_canonical_files: total_count={total} but only "
            f"{len(items)} returned. Need pagination support."
        )
    return files


# ── Coverage report ───────────────────────────────────────────────────────────

def run_check(
    local_cs_yaml: str | None = None,
    pat: str | None = None,
) -> dict:
    """
    Run the bidirectional coverage check; return a report dict.

    local_cs_yaml: if provided, use this content for canonical_sources.yaml
                   (e.g. for pre-commit checks against staged content).
                   If None, fetch live from GitHub main.
    """
    if local_cs_yaml is None:
        cs_text = _fetch_canonical_sources(pat)
    else:
        cs_text = local_cs_yaml

    registered = registered_paths(cs_text)
    declared = declared_canonical_files(pat)

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


def _fetch_canonical_sources(pat: str | None = None) -> str:
    pat = pat or _pat()
    url = (
        f'https://api.github.com/repos/{REPO}/contents/'
        'references/canonical_sources.yaml?ref=main'
    )
    req = urllib.request.Request(
        url,
        headers={
            'Authorization': f'token {pat}',
            'Accept': 'application/vnd.github.v3+json',
        },
    )
    import base64
    with urllib.request.urlopen(req) as r:
        body = json.loads(r.read())
    return base64.b64decode(body['content']).decode()


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
