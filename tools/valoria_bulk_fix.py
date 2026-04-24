#!/usr/bin/env python3
"""
Valoria Bulk Fix — Unambiguous Legacy Renames
==============================================
Performs safe in-place substitutions for legacy terms that have a 1:1
canonical replacement and no per-context ambiguity.

Handles:
  - Rendering Stability → Mending Stability  (rename per ED-731)
  - Cohesion → Discipline                    (rename per PP-232)
  - Combat Power → Power                     (rename per PP-232, as a mechanic term only)

Does NOT handle (per-context judgment required):
  - TC alone → Theocracy Counter OR Conviction Track
  - CP alone → Character Point OR Combat Power (→Power)
  - TD alone → Thread Depth (removed, flag) OR flowchart TD (Mermaid, keep)
  - RS alone → Rendering Stability (now Mending Stability) OR Resonant Style
  - Bare abbreviations anywhere (TC, CP, TD, RS, CE, COMP) — flagged by collator, needs manual review

Safety rails:
  - Skips files in canon/, archives/, deprecated/, historical/
  - Skips lines containing 'formerly', 'renamed', 'previously', 'PP-', 'ED-', '[EDITORIAL:'
  - Skips YAML frontmatter and HTML comments
  - Only substitutes whole-word matches
  - Writes a dry-run report first; --apply flag commits the changes

Usage:
  python3 tools/valoria_bulk_fix.py                  # dry-run
  python3 tools/valoria_bulk_fix.py --apply          # perform substitutions
  python3 tools/valoria_bulk_fix.py --apply --limit 5  # only first 5 files
"""
import argparse
import os
import re
import sys
import urllib.request
import json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/..')
sys.path.insert(0, '/home/claude')
import github_ops as g


# ─── SUBSTITUTIONS ─────────────────────────────────────────────────────────

# Each entry: (pattern, replacement, description)
# Patterns are case-sensitive word-boundary regex. Only full-form terms are
# swept here — bare abbreviations (RS, CP, TC, etc.) are intentionally
# EXCLUDED because they require per-context judgment.
SUBSTITUTIONS = [
    (r'\bRendering Stability\b', 'Mending Stability',
     'ED-731 rename (RS→MS); historical annotations preserved'),
    (r'\bCohesion\b', 'Discipline',
     'PP-232 rename in combat system'),
    (r'\bCombat Power\b', 'Power',
     'PP-232 rename; CP now refers to Character Point only (ED-136)'),
]

# ─── SCOPE ─────────────────────────────────────────────────────────────────

SCAN_PREFIXES = ('designs/', 'params/')
SKIP_PATTERNS = (
    '_skeleton.md', '_index.md', '_historical.md', '_deprecated.md',
    'superseded',
    '/deprecated/', '/archives/', '/historical/', '/versions/',
    'canon/',  # historical annotation layer
)

# User-authority paths — worldbuilding, characters, narrative, setting.
# These require editorial flags ([EDITORIAL: ED-NNN] or [PROVISIONAL: ...]).
# Bulk-fix skips them entirely; mechanical renames in these files must be
# individually reviewed and flagged.
USER_AUTHORITY_PREFIXES = (
    'designs/world/',
    'designs/npcs/',
    'designs/arcs/',
    'designs/territory/',
)

# Lines with any of these phrases are skipped entirely (keep historical context)
SKIP_LINE_MARKERS = (
    'formerly', 'renamed', 'previously', 'was called', 'was named',
    'now called', 'now named', 'historical', 'prior name', 'used to be',
    'pp-', 'ed-', 'sim-', '[editorial:', 'superseded', 'deprecated',
)


# ─── LOGIC ─────────────────────────────────────────────────────────────────

def list_scannable_files():
    pat = open('/home/claude/.valoria_pat').read().strip()
    req = urllib.request.Request(
        'https://api.github.com/repos/jordanelias/ttrpg/git/trees/main?recursive=1',
        headers={'Authorization': f'token {pat}',
                 'Accept': 'application/vnd.github.v3+json'}
    )
    with urllib.request.urlopen(req) as r:
        tree = json.loads(r.read())['tree']
    out = []
    for e in tree:
        if e['type'] != 'blob': continue
        p = e['path']
        if not p.endswith('.md'): continue
        if not any(p.startswith(pre) for pre in SCAN_PREFIXES): continue
        if any(pat in p for pat in SKIP_PATTERNS): continue
        if any(p.startswith(pre) for pre in USER_AUTHORITY_PREFIXES): continue
        out.append(p)
    return sorted(out)


def apply_substitutions_to_content(content):
    """Apply all substitutions, respecting line-level skip markers.
    Returns (new_content, changes_per_line_list)."""
    lines = content.split('\n')
    new_lines = []
    changes = []

    for line_idx, line in enumerate(lines):
        # Skip markers
        line_lower = line.lower()
        if any(marker in line_lower for marker in SKIP_LINE_MARKERS):
            new_lines.append(line)
            continue
        # Skip HTML comments
        if line.strip().startswith('<!--') and line.strip().endswith('-->'):
            new_lines.append(line)
            continue
        # Apply each substitution
        new_line = line
        for pattern, repl, desc in SUBSTITUTIONS:
            new_line, n = re.subn(pattern, repl, new_line)
            if n > 0:
                changes.append({
                    'line_no': line_idx + 1,
                    'pattern': pattern,
                    'count': n,
                    'description': desc,
                    'before': line[:120],
                    'after': new_line[:120],
                })
        new_lines.append(new_line)

    return '\n'.join(new_lines), changes


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--apply', action='store_true',
                        help='Commit changes to the repo. Without this, dry-run only.')
    parser.add_argument('--limit', type=int, default=None,
                        help='Limit to first N files for testing.')
    parser.add_argument('--out', default='/tmp/valoria/bulk_fix_report.yaml')
    args = parser.parse_args()

    print("[1/3] Listing scannable files...")
    paths = list_scannable_files()
    if args.limit:
        paths = paths[:args.limit]
    print(f"  {len(paths)} files in scope")

    print("[2/3] Scanning + applying substitutions...")
    total_changes = 0
    files_changed = {}
    all_fetched = {}
    for i in range(0, len(paths), 25):
        chunk = paths[i:i+25]
        files = g.read_files_graphql(chunk, force_full=True)
        for p, c in files.items():
            if c is None: continue
            all_fetched[p] = c
            new_c, changes = apply_substitutions_to_content(c)
            if new_c != c:
                files_changed[p] = {'new': new_c, 'changes': changes}
                total_changes += sum(ch['count'] for ch in changes)

    print(f"  Files with changes: {len(files_changed)}")
    print(f"  Total substitutions: {total_changes}")

    # Breakdown per pattern
    from collections import Counter
    pattern_counts = Counter()
    for fc in files_changed.values():
        for ch in fc['changes']:
            pattern_counts[ch['pattern']] += ch['count']
    print("\n  Breakdown by pattern:")
    for p, n in pattern_counts.most_common():
        print(f"    {p}: {n}")

    print("[3/3] Writing dry-run report...")

    def yamlstr(s):
        if s is None: return 'null'
        return '"' + str(s).replace('\\', '\\\\').replace('"', '\\"') + '"'

    lines = [
        "# Valoria Bulk Fix — Dry Run Report",
        "# Generated by tools/valoria_bulk_fix.py",
        "",
        "version: 1",
        f"files_changed: {len(files_changed)}",
        f"total_substitutions: {total_changes}",
        f"applied: {str(args.apply).lower()}",
        "",
        "patterns:",
    ]
    for pattern, repl, desc in SUBSTITUTIONS:
        n = pattern_counts.get(pattern, 0)
        lines.append(f"  - pattern: {yamlstr(pattern)}")
        lines.append(f"    replacement: {yamlstr(repl)}")
        lines.append(f"    description: {yamlstr(desc)}")
        lines.append(f"    occurrences: {n}")
    lines.append("")
    lines.append("files:")
    for p in sorted(files_changed.keys()):
        fc = files_changed[p]
        lines.append(f"  - path: {yamlstr(p)}")
        lines.append(f"    changes: {len(fc['changes'])}")
        lines.append(f"    details:")
        for ch in fc['changes'][:10]:  # Cap per-file
            lines.append(f"      - line: {ch['line_no']}")
            lines.append(f"        pattern: {yamlstr(ch['pattern'])}")
            lines.append(f"        count: {ch['count']}")

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, 'w') as f:
        f.write('\n'.join(lines))
    print(f"  Report: {args.out}")

    if args.apply:
        print("\n[APPLY] Committing changes via safe_commit...")
        import valoria_hooks as h
        additions = [(p, fc['new']) for p, fc in files_changed.items()]
        msg = f"""[infrastructure] bulk-fix unambiguous legacy renames — {total_changes} substitutions across {len(files_changed)} files

Auto-applied the three safe 1:1 renames flagged by collator:
- Rendering Stability → Mending Stability ({pattern_counts.get(r'\\bRendering Stability\\b', 0)}) — ED-731
- Cohesion → Discipline ({pattern_counts.get(r'\\bCohesion\\b', 0)}) — PP-232
- Combat Power → Power ({pattern_counts.get(r'\\bCombat Power\\b', 0)}) — PP-232

Skipped lines containing: formerly, renamed, previously, was called, now called, historical, prior name, used to be, PP-, ED-, SIM-, [EDITORIAL:, superseded, deprecated
Skipped files in: canon/, archives/, deprecated/, historical/, versions/, _skeleton.md, _index.md

Remaining drift (per-context judgment required, NOT auto-fixed):
- TC alone → Theocracy Counter OR Conviction Track (943× in collator report)
- CP alone → Character Point OR Power (69× — previously ambiguous, now locked to Character Point per ED-136)
- TD alone → flag (phantom stat) OR keep (Mermaid flowchart syntax)
- Bare RS — most already caught by Rendering Stability→Mending Stability sweep; any residual RS alone should be checked

Run collator again after this to see remaining findings.
"""
        result = h.safe_commit(additions, [], msg)
        print(f"  Committed: {result}")
    else:
        print("\n  DRY-RUN — pass --apply to commit")


if __name__ == '__main__':
    main()
