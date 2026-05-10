#!/usr/bin/env python3
"""
Valoria Values Extractor
=========================
Scans `params/` (recursively) and `designs/` (recursively, excluding
designs/audit/) for .md files and extracts named mechanical values.

Files matching `*_superseded.md` or `*_deprecated.md` are excluded — they hold
historical content and produce noisy conflicts against current canon.

Extracted patterns:
  1. Formula assignments: "X = Y" or "X: Y" where Y is numeric/formulaic
  2. Labeled table values: rows in tables with a "Value" / "Range" / "TN" / "Ob" / "Formula" column
  3. Constants in prose: "The Ob cap is 20", "RS ceiling: 100", etc.

Output: references/values_master.yaml
  - Grouped by source file
  - Each value has a stable key, raw text, extracted numeric (if any),
    formula (if applicable), and surrounding section context.
  - Conflicts between files for the same-named value are surfaced.

Scope expansion 2026-05-10: previously params/ only at the top level. Designs
now hold mechanical values too; a same-name value disagreeing between
params/combat.md and designs/scene/combat_v30.md is exactly the drift this
tool exists to catch.
"""
import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/..')
sys.path.insert(0, '/home/claude')
try:
    import github_ops as g
except ImportError:
    print("ERROR: github_ops.py not on path.")
    sys.exit(1)

import urllib.request
import json


def _list_md_recursive(repo_path: str, pat: str) -> list[str]:
    """List .md files under repo_path recursively (using GitHub Trees API)."""
    out = []
    req = urllib.request.Request(
        f'https://api.github.com/repos/jordanelias/ttrpg/git/trees/main?recursive=1',
        headers={'Authorization': f'token {pat}',
                 'Accept': 'application/vnd.github.v3+json'}
    )
    with urllib.request.urlopen(req) as r:
        data = json.loads(r.read())
    for entry in data.get('tree', []):
        if entry.get('type') != 'blob':
            continue
        p = entry.get('path', '')
        if not p.startswith(repo_path):
            continue
        if not p.endswith('.md'):
            continue
        out.append(p)
    return out


def list_source_files():
    """
    List all .md files that hold mechanical content:
      - params/  (all subdirs, recursive)
      - designs/ (all subdirs, recursive, EXCEPT designs/audit/)

    Excludes:
      - *_superseded.md  (historical; produces noisy conflicts vs canon)
      - *_deprecated.md  (same)
      - designs/audit/   (audit reports about canon, not canon itself)
    """
    pat = open('/home/claude/.valoria_pat').read().strip()
    candidates = _list_md_recursive('params/', pat) + _list_md_recursive('designs/', pat)

    out = []
    for p in candidates:
        if p.startswith('designs/audit/'):
            continue
        base = p.rsplit('/', 1)[-1]
        if base.endswith('_superseded.md') or base.endswith('_deprecated.md'):
            continue
        out.append(p)
    return sorted(out)


# Backwards-compatible alias — any tool that imported list_params_files()
# continues to work, but now sees the expanded scope.
def list_params_files():
    """DEPRECATED: use list_source_files(). Retained for backward compat."""
    return list_source_files()


# ─── EXTRACTION PATTERNS ──────────────────────────────────────────────────

# Matches named value on its own line/after bullet:
# "X: <number or range>"       (e.g., "RS ceiling: 100", "TN: 7")
# "X = <expression>"           (e.g., "Stamina = Endurance × 5")
# "**X:** <number>"            (bolded key)
NAMED_VALUE_RE = re.compile(
    r'^[-\s*]*(\*\*)?([A-Z][A-Za-z][\w\s\-\(\)/]{2,40}?)(\*\*)?\s*'
    r'[:=]\s*'
    r'([^<.\n]{1,200}?)'
    r'(?:\s*\([A-Z]{2}-\d+|$|\.|<!--)',
    re.MULTILINE
)

# Matches table rows with recognized numeric columns.
# Tables in markdown: | col1 | col2 | ...
TABLE_ROW_RE = re.compile(r'^\|[^\n]+\|$', re.MULTILINE)

# Known numeric column headers to extract values from
NUMERIC_COLUMN_HEADERS = {
    'tn', 'ob', 'range', 'formula', 'value', 'cost', 'min', 'max',
    'minimum', 'maximum', 'floor', 'ceiling', 'cap', 'default',
    'start', 'starting', 'base', 'modifier', 'bonus', 'penalty',
    'damage', 'wounds', 'hp', 'mp', 'duration', 'frequency',
    'threshold', 'gain', 'loss',
}

# Heuristic for numeric-like values
NUMERIC_VALUE_RE = re.compile(
    r'^-?\d+(?:[\.\-–~]\d+)?(?:\s*(?:to|–|-|~)\s*-?\d+)?$'
)


def extract_section_path(content, position):
    """Determine the section heading stack at a given position."""
    # Find all headers before this position
    before = content[:position]
    headers = []
    for line in before.split('\n'):
        m = re.match(r'^(#{1,6})\s+(.+?)$', line)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            # Pop any same-or-deeper level headers
            while headers and headers[-1][0] >= level:
                headers.pop()
            headers.append((level, title))
    return ' > '.join(h[1] for h in headers)


def extract_named_values(content, path):
    """Extract 'X: value' and 'X = value' patterns as named values."""
    out = []
    seen_positions = set()
    for m in NAMED_VALUE_RE.finditer(content):
        pos = m.start()
        if pos in seen_positions:
            continue
        seen_positions.add(pos)
        name = m.group(2).strip()
        raw_value = m.group(4).strip()

        # Skip obvious false positives
        if not name or len(name) < 3:
            continue
        # Skip if name starts with lowercase word — likely sentence continuation
        if name[0].islower():
            continue
        # Skip obvious english phrases that aren't values
        skip_tokens = {'Formation', 'See', 'Required', 'Cross-reference', 'Lock_chronic_drift', 'Cover', 'Replaced', 'Example', 'Supersedes', 'History_bonus', 'Note', 'Success', 'Effect', 'Mending_success', 'Incorporates', 'Last-updated', 'Rupture', 'Standard_loser', 'Source', 'Instances', 'Partial', 'Covers', 'Overwhelming', 'Authority', 'Date', 'Scope', 'Instance', 'Godot', 'Loss', 'Examples', 'Coherence', 'Effects', 'Dissolution', 'Requirements', 'Status', 'Author', 'Pool', 'Rationale', 'Version', 'Notes', 'Commit', 'Damage_success', 'Recovery', 'Requires', 'Failure', 'Cross-references'}
        if name in skip_tokens:
            continue
        if name.startswith('Example') or name.startswith('PP-'):
            continue

        # Classify the value
        value_numeric = None
        value_formula = None
        value_kind = 'text'

        # Pure number or range
        if NUMERIC_VALUE_RE.match(raw_value):
            value_kind = 'numeric'
            # Try to parse leading number
            n = re.match(r'-?\d+', raw_value)
            if n:
                value_numeric = int(n.group())

        # Formula (contains + - × / × or attribute names)
        elif re.search(r'[+\-×÷*/=]|\b(?:Endurance|Agility|Strength|Cognition|'
                       r'Presence|Attunement|Spirit|History|TN|Ob|TS|TPS|'
                       r'RS|TT|CI|HP|MP)\b', raw_value, re.IGNORECASE):
            value_kind = 'formula'
            value_formula = raw_value

        # Skip entries that are pure prose (no number, no formula)
        if value_kind == 'text':
            continue

        section = extract_section_path(content, pos)
        out.append({
            'name': name,
            'value_raw': raw_value,
            'value_kind': value_kind,
            'value_numeric': value_numeric,
            'value_formula': value_formula,
            'source_file': path,
            'source_section': section,
            'line_hint': content[:pos].count('\n') + 1,
        })
    return out


def extract_table_values(content, path):
    """Extract numeric values from tables where the column header suggests
    they're canonical values (Ob, TN, Range, Formula, etc.)."""
    out = []
    lines = content.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # Detect start of table: header row + separator
        if line.startswith('|') and i + 1 < len(lines):
            next_line = lines[i+1].strip()
            if next_line.startswith('|') and re.match(r'\|[\s\-:|]+\|', next_line):
                # This is a table. Parse header.
                headers = [h.strip().lower() for h in
                           re.split(r'\s*\|\s*', line.strip('|'))]
                # Identify columns that carry canonical values
                value_cols = {}
                for idx, h in enumerate(headers):
                    # Normalize (strip bold, etc.)
                    h_clean = re.sub(r'\*+', '', h).strip().lower()
                    if h_clean in NUMERIC_COLUMN_HEADERS:
                        value_cols[idx] = h_clean
                if not value_cols:
                    i += 1
                    continue
                # Parse rows
                row_idx = i + 2
                while row_idx < len(lines):
                    rl = lines[row_idx].strip()
                    if not rl.startswith('|'):
                        break
                    cells = [c.strip() for c in
                             re.split(r'\s*\|\s*', rl.strip('|'))]
                    if len(cells) < 2:
                        row_idx += 1
                        continue
                    # First cell = row label (the "name" of this value)
                    row_label = re.sub(r'\*+', '', cells[0]).strip()
                    if not row_label or len(row_label) < 2:
                        row_idx += 1
                        continue
                    for col_idx, col_name in value_cols.items():
                        if col_idx >= len(cells):
                            continue
                        cell_val = cells[col_idx]
                        if not cell_val:
                            continue
                        # Classify
                        value_numeric = None
                        if NUMERIC_VALUE_RE.match(cell_val):
                            n = re.match(r'-?\d+', cell_val)
                            if n:
                                value_numeric = int(n.group())
                        section = extract_section_path(
                            content,
                            sum(len(l)+1 for l in lines[:row_idx])
                        )
                        out.append({
                            'name': f'{row_label} ({col_name})',
                            'value_raw': cell_val,
                            'value_kind': 'numeric' if value_numeric is not None else 'formula',
                            'value_numeric': value_numeric,
                            'value_formula': cell_val if value_numeric is None else None,
                            'source_file': path,
                            'source_section': section,
                            'source_table_column': col_name,
                            'line_hint': row_idx + 1,
                        })
                    row_idx += 1
                i = row_idx
                continue
        i += 1
    return out


def extract_all_values(contents):
    """Run all extractors on all files."""
    all_values = []
    per_file_counts = {}
    for path, content in contents.items():
        if not content:
            continue
        named = extract_named_values(content, path)
        table = extract_table_values(content, path)
        all_values.extend(named)
        all_values.extend(table)
        per_file_counts[path] = {
            'named': len(named),
            'table': len(table),
            'total': len(named) + len(table),
        }
    return all_values, per_file_counts


def detect_conflicts(values):
    """Group by normalized name, flag entries where multiple files disagree.
    Only considers named values (not table rows) to avoid false positives
    where the same column header appears in multiple unrelated tables."""
    by_name = defaultdict(list)
    for v in values:
        # Skip table-cell values — they're per-context and don't conflict
        if v.get('source_table_column'):
            continue
        k = re.sub(r'\s+', '_', v['name'].lower())
        k = re.sub(r'[^\w]+', '_', k).strip('_')
        by_name[k].append(v)
    conflicts = []
    for name_key, vs in by_name.items():
        if len(vs) < 2:
            continue
        # Require different FILES (or different sections in same file)
        unique_contexts = set((v['source_file'], v['source_section']) for v in vs)
        if len(unique_contexts) < 2:
            continue
        nums = set()
        formulas = set()
        for v in vs:
            if v['value_numeric'] is not None:
                nums.add(v['value_numeric'])
            if v['value_formula']:
                f = re.sub(r'\s+', ' ', v['value_formula']).strip()
                formulas.add(f)
        if len(nums) > 1 or len(formulas) > 1:
            conflicts.append({
                'name_key': name_key,
                'instances': vs,
                'distinct_numeric': sorted(nums) if nums else None,
                'distinct_formulas': sorted(formulas) if formulas else None,
            })
    return conflicts


def yamlstr(s):
    if s is None:
        return 'null'
    s = str(s)
    # Use block scalar if contains newline
    if '\n' in s:
        return '|-\n        ' + s.replace('\n', '\n        ')
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'


def build_registry_yaml(values, conflicts):
    """Emit values grouped by source file."""
    lines = [
        "# Valoria Values Master Registry",
        "# Auto-extracted by tools/extract_values.py from params/ + designs/ (recursive).",
        "# Files excluded: *_superseded.md, *_deprecated.md, designs/audit/.",
        "# Each entry records a named mechanical value with its source location.",
        "# Conflicts (same name, different values across files) surfaced below.",
        "",
        "version: 2",
        f"total_values: {len(values)}",
        f"total_conflicts: {len(conflicts)}",
        "",
    ]
    # Conflicts first (most important)
    if conflicts:
        lines.append("# ═══ CONFLICTS (same-named values disagree across files) ═══")
        lines.append("conflicts:")
        for c in conflicts:
            lines.append(f"  {c['name_key']}:")
            if c['distinct_numeric']:
                lines.append(f"    distinct_numeric: {c['distinct_numeric']}")
            if c['distinct_formulas']:
                lines.append(f"    distinct_formulas:")
                for f in c['distinct_formulas']:
                    lines.append(f"      - {yamlstr(f)}")
            lines.append(f"    instances:")
            for inst in c['instances']:
                lines.append(f"      - file: {yamlstr(inst['source_file'])}")
                lines.append(f"        section: {yamlstr(inst['source_section'])}")
                lines.append(f"        line: {inst['line_hint']}")
                lines.append(f"        raw_value: {yamlstr(inst['value_raw'])}")
        lines.append("")

    # Full values list by file
    lines.append("# ═══ FULL VALUES INDEX (by source file) ═══")
    lines.append("values:")
    by_file = defaultdict(list)
    for v in values:
        by_file[v['source_file']].append(v)
    for path in sorted(by_file.keys()):
        lines.append(f"  {yamlstr(path)}:")
        for v in by_file[path]:
            lines.append(f"    - name: {yamlstr(v['name'])}")
            lines.append(f"      value_raw: {yamlstr(v['value_raw'])}")
            lines.append(f"      kind: {v['value_kind']}")
            if v['value_numeric'] is not None:
                lines.append(f"      numeric: {v['value_numeric']}")
            if v['value_formula']:
                lines.append(f"      formula: {yamlstr(v['value_formula'])}")
            lines.append(f"      section: {yamlstr(v['source_section'])}")
            if v.get('source_table_column'):
                lines.append(f"      table_col: {v['source_table_column']}")
            lines.append(f"      line: {v['line_hint']}")
    return '\n'.join(lines)


def main():
    paths = list_source_files()
    print(f"[1/3] Fetching {len(paths)} source files (params/ + designs/)...")
    contents = g.read_files_graphql(paths, force_full=True)
    loaded = sum(1 for v in contents.values() if v)
    print(f"  Loaded: {loaded}")

    print("[2/3] Extracting values...")
    values, per_file = extract_all_values(contents)
    print(f"  Total values extracted: {len(values)}")
    print(f"  Per-file breakdown:")
    for path, counts in sorted(per_file.items()):
        print(f"    {path}: {counts['total']} (named: {counts['named']}, table: {counts['table']})")

    print("[3/3] Detecting conflicts...")
    conflicts = detect_conflicts(values)
    print(f"  Conflicts detected: {len(conflicts)}")
    if conflicts:
        print(f"\n  Sample conflicts:")
        for c in conflicts[:5]:
            print(f"    {c['name_key']}: numeric={c['distinct_numeric']}, formulas={len(c['distinct_formulas'] or [])}")
            for inst in c['instances']:
                print(f"      - {inst['source_file']} (§{inst['source_section'][:50]}): {inst['value_raw']}")

    # Write YAML
    yaml_out = build_registry_yaml(values, conflicts)
    os.makedirs('/tmp/valoria', exist_ok=True)
    out_path = '/tmp/valoria/values_master.yaml'
    with open(out_path, 'w') as f:
        f.write(yaml_out)
    print(f"\nWrote: {out_path} ({os.path.getsize(out_path)} bytes)")

    # Validate
    try:
        import yaml as _y
        _y.safe_load(yaml_out)
        print("YAML valid")
    except Exception as e:
        print(f"YAML INVALID: {e}")


if __name__ == '__main__':
    main()
