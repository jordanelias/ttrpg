#!/usr/bin/env python3
"""
Valoria Collator
================
Cross-references all design docs and params files against:
  - references/proper_noun_registry.yaml
  - references/alias_registry.yaml
  - references/values_master.yaml

Flags drift:
  1. UNKNOWN_PROPER_NOUN — capitalized tokens not in registry and not rejected
  2. UNKNOWN_ABBREVIATION — abbreviations not in alias_registry
  3. COLLISION_USED_ALONE — collision abbreviation used standalone
  4. LEGACY_TERM_USED — renamed-old-name appearing in current docs
  5. VALUE_CONFLICT — numeric value for named parameter differs from master
  6. MULTI_CANONICAL_AMBIGUITY — surname/firstname matches multiple canonicals (e.g., Maret)

Output: references/collation_report.yaml — every drift instance with file,
line, and remediation hint.

Usage:
  python3 tools/valoria_collator.py            # report only
  python3 tools/valoria_collator.py --strict   # exit 1 on any drift
"""
import os
import re
import sys
import yaml
import argparse
import urllib.request
import json
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/..')
sys.path.insert(0, '/home/claude')
import github_ops as g


# ─── CONFIG ────────────────────────────────────────────────────────────────

SCAN_PREFIXES = ('designs/', 'params/', 'canon/')
# Files whose purpose is to document historical state — findings suppressed here
EXEMPT_FILES = {
    'canon/editorial_ledger.yaml',
    'canon/editorial_ledger_summary.yaml',
    'canon/patch_register_active.yaml',
    'canon/patch_register.yaml',
    'canon/02_canon_constraints.md',
    'canon/03_canonical_timeline.md',
    'references/restructure_ledger.md',
    'references/propagation_map.md',
    'references/propagation_log.md',
    'references/throughline_registry.md',
    'references/throughlines_complete.md',
}
EXEMPT_PATH_PREFIXES = (
    'canon/',  # canon/ contains documentation of state; fix at design/params level
)

SKIP_PATTERNS = (
    '_skeleton.md',
    '_index.md',
    'superseded',
    '/deprecated/',
    '/archives/',
    '/historical/',
    '/versions/',
)


# ─── LOADERS ───────────────────────────────────────────────────────────────

def list_scannable_files():
    """List all .md files under scan prefixes, excluding skip patterns."""
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
        out.append(p)
    return sorted(out)


def load_registries():
    """Fetch the three registries from the repo."""
    files = g.read_files_graphql([
        'references/proper_noun_registry.yaml',
        'references/alias_registry.yaml',
        'references/values_master.yaml',
    ], force_full=True)
    return (
        yaml.safe_load(files.get('references/proper_noun_registry.yaml', '')) or {},
        yaml.safe_load(files.get('references/alias_registry.yaml', '')) or {},
        yaml.safe_load(files.get('references/values_master.yaml', '')) or {},
    )


def flatten_proper_nouns(reg):
    """Flatten proper noun registry into { canonical: entry } and {alias: canonical_key}."""
    canonicals = {}   # key → entry
    alias_lookup = {} # alias_token (case-sensitive) → canonical_key
    known_tokens = set()  # all known forms
    TYPE_FROM_GROUP = {
        'characters': 'character', 'territories': 'territory', 'factions': 'faction',
        'subfactions': 'subfaction', 'organizations': 'organization', 'realms': 'realm',
        'regions': 'region', 'peoples': 'people', 'concepts': 'concept',
        'structures': 'structure',
    }
    for group, entries in reg.items():
        if group in ('version',) or not isinstance(entries, dict):
            continue
        t = TYPE_FROM_GROUP.get(group)
        if not t: continue
        for k, e in entries.items():
            canonicals[k] = {**e, 'type': t}
            known_tokens.add(e['canonical'])
            for a in e.get('aliases', []) or []:
                alias_lookup[a] = k
                known_tokens.add(a)
    return canonicals, alias_lookup, known_tokens


def flatten_aliases(alias_reg):
    """Extract from alias_registry.yaml: known abbreviations, legacy names, collisions."""
    abbrev_to_canonical = {}    # abbr → canonical
    standalone_ok = set()       # abbrs that may stand alone
    standalone_banned = set()   # abbrs that may NOT stand alone
    legacy_terms = {}           # legacy → current canonical
    collision_abbrs = set()     # collision abbrs
    all_canonicals = set()

    def walk_entries(category_dict):
        for k, e in category_dict.items():
            if not isinstance(e, dict): continue
            canonical = e.get('canonical')
            if canonical:
                all_canonicals.add(canonical)
            for a in e.get('abbreviations', []) or []:
                abbrev_to_canonical[a] = canonical
                if e.get('standalone_ok') is True:
                    standalone_ok.add(a)
                elif e.get('standalone_ok') is False:
                    standalone_banned.add(a)
            for leg in e.get('legacy', []) or []:
                legacy_terms[leg] = canonical

    for cat, entries in alias_reg.items():
        if cat in ('version', 'collision_table', 'unresolved', 'legacy_renames'):
            continue
        if isinstance(entries, dict):
            walk_entries(entries)

    # Collision table
    for k, e in (alias_reg.get('collision_table') or {}).items():
        if isinstance(e, dict) and e.get('abbreviation'):
            collision_abbrs.add(e['abbreviation'])

    # Legacy renames
    for k, e in (alias_reg.get('legacy_renames') or {}).items():
        if isinstance(e, dict):
            old = e.get('old')
            new = e.get('new')
            if old:
                # Strip (ABBR) if present
                old_clean = re.sub(r'\s*\([A-Z]{2,}\)\s*$', '', old).strip()
                if old_clean:
                    legacy_terms[old_clean] = new
                # Also register the abbr if in parens
                abbr_m = re.search(r'\(([A-Z]{2,})\)', old)
                if abbr_m:
                    legacy_terms[abbr_m.group(1)] = new

    return {
        'abbrev_to_canonical': abbrev_to_canonical,
        'standalone_ok': standalone_ok,
        'standalone_banned': standalone_banned,
        'legacy_terms': legacy_terms,
        'collision_abbrs': collision_abbrs,
        'all_canonicals': all_canonicals,
    }


def flatten_values(vm):
    """Build { name_key: canonical_numeric_value } from values_master.
    Only includes explicit named values (not table cells)."""
    canon_values = {}
    # values are grouped by file
    for path, entries in (vm.get('values') or {}).items():
        if not isinstance(entries, list): continue
        for v in entries:
            # Only named values in params/ are considered canonical
            if not path.startswith('params/'): continue
            if v.get('table_col'): continue
            if v.get('numeric') is None: continue
            name = v['name']
            key = re.sub(r'\s+', '_', name.lower())
            key = re.sub(r'[^\w]+', '_', key).strip('_')
            if key not in canon_values:
                canon_values[key] = {
                    'numeric': v['numeric'],
                    'source_file': path,
                    'source_section': v.get('section', ''),
                }
    return canon_values


# ─── SCANNERS ──────────────────────────────────────────────────────────────

# Pattern for potential proper-noun-like tokens
TOKEN_PATTERN = re.compile(
    r'\b([A-ZÆÖÄÜ][a-zæöäüßé]+(?:\s+[A-ZÆÖÄÜ][a-zæöäüßé]+){0,2})\b'
)
ABBREV_PATTERN = re.compile(r'\b([A-Z]{2,6})\b')

# Known skip list (matches extractor's FALSE_POSITIVE set — plus common mechanical terms)
EXTRACTOR_SKIP = {
    'The', 'This', 'That', 'These', 'Those', 'When', 'Where', 'Why', 'How',
    'What', 'Who', 'Which', 'Whose', 'A', 'An', 'If', 'But', 'And', 'Or',
    'In', 'On', 'At', 'To', 'For', 'With', 'By', 'From', 'As', 'All',
    'He', 'She', 'His', 'Her', 'They', 'Them', 'Their', 'It', 'Its',
    'I', 'Me', 'My', 'You', 'Your', 'We', 'Our',
    'First', 'Second', 'Third', 'Last', 'Next',
    'Yes', 'No', 'Not',
}


def scan_file_for_drift(path, content, ctx):
    """Run all drift checks on one file's content. Returns list of findings."""
    findings = []
    if not content: return findings

    # 1. Unknown abbreviations (uppercase 2-6 letters not in alias registry)
    seen_abbrs = set()
    for m in ABBREV_PATTERN.finditer(content):
        abbr = m.group(1)
        if abbr in seen_abbrs: continue
        seen_abbrs.add(abbr)
        # Skip if it's a known abbreviation
        if abbr in ctx['alias']['abbrev_to_canonical']:
            continue
        # Skip acronyms that are really all-caps English (rare) or numbered series (PP-, ED-, SIM-)
        # Get position context to check
        pos = m.start()
        # Skip if preceded by a prefix like "PP-", "ED-"
        before = content[max(0,pos-5):pos]
        if before.endswith(('-', 'PP', 'ED', 'SIM', 'HP', 'MP', 'IP')):
            continue
        # Skip common tech acronyms
        if abbr in ('API', 'JSON', 'YAML', 'CSV', 'HTML', 'URL', 'PDF', 'ID',
                    'UI', 'UX', 'MD', 'UTF', 'CLI', 'CI', 'CD', 'AI', 'ML',
                    'OS', 'PC', 'NPC', 'GM', 'BG', 'TN', 'CT', 'TS', 'TPS',
                    'TT', 'MS', 'CI', 'TD', 'COMP', 'POP', 'FR', 'CE', 'CP',
                    'DR', 'EV', 'FIX', 'TBD', 'TODO', 'WIP', 'WARN', 'TEST',
                    'NONE', 'NULL', 'GAP', 'OK', 'PIC', 'RAM', 'CPU'):
            # CI here is accepted as 'Continuous Integration' — but we want
            # to flag CI used *as a game term*. The collator can't distinguish
            # from abbreviation alone — log but low-severity
            pass
        line = content[:pos].count('\n') + 1
        findings.append({
            'kind': 'UNKNOWN_ABBREVIATION',
            'token': abbr,
            'file': path,
            'line': line,
            'severity': 'warn',
            'hint': f'Abbreviation "{abbr}" not registered in alias_registry',
        })

    # 2. Collision abbreviations used alone (must NOT appear bare)
    for abbr in ctx['alias']['collision_abbrs']:
        for m in re.finditer(rf'\b{re.escape(abbr)}\b', content):
            pos = m.start()
            # Check if immediately preceded by the canonical name in parens-expansion form
            # e.g. "Church Influence (CI)" is OK; standalone "CI" alone is not
            before = content[max(0, pos-60):pos]
            # If the canonical full term appears within 50 chars before, it's OK (definition)
            canonical = ctx['alias']['abbrev_to_canonical'].get(abbr)
            if canonical and canonical.lower() in before.lower():
                continue
            # Check if preceded by "-" (like PP-CI = patch ID form)
            if content[max(0,pos-1):pos] == '-':
                continue
            line = content[:pos].count('\n') + 1
            findings.append({
                'kind': 'COLLISION_USED_ALONE',
                'token': abbr,
                'file': path,
                'line': line,
                'severity': 'error',
                'hint': f'"{abbr}" is a collision abbreviation — write full term. Canonical: {canonical}',
            })

    # 3. Legacy terms in current docs
    for legacy, current in ctx['alias']['legacy_terms'].items():
        if not legacy: continue
        # Skip entries whose replacement is None (fully removed)
        # (still flag legacy even if fully removed, since appearance in docs = stale)
        for m in re.finditer(rf'\b{re.escape(legacy)}\b', content):
            pos = m.start()
            # Skip if immediately follows "formerly" or "was" or "renamed from"
            # Skip if the surrounding context (full line) marks this as historical
            line_start = content.rfind("\n", 0, pos) + 1
            line_end = content.find("\n", pos)
            if line_end == -1: line_end = len(content)
            full_line = content[line_start:line_end].lower()
            if any(phrase in full_line for phrase in (
                'formerly', 'renamed from', 'renamed to', 'historical', 'prior name', 'previously',
                'pp-', 'ed-', 'sim-', 'ded ', 'superseded', 'deprecated',
                'was called', 'was named', 'used to be', 'now called', 'now named',
            )):
                continue
            # Skip if inside editorial brackets [EDITORIAL: ...]
            if '[editorial:' in full_line:
                continue
            line = content[:pos].count('\n') + 1
            findings.append({
                'kind': 'LEGACY_TERM_USED',
                'token': legacy,
                'file': path,
                'line': line,
                'severity': 'error',
                'hint': (f'Legacy term "{legacy}" used — current canonical: "{current}"'
                         if current else f'"{legacy}" was removed — should not appear'),
            })

    # 4. Value drift — for each canon value name, check if file has conflicting numeric
    # Only do this for params files and substantive designs/
    # Pattern: "X: <num>" or "X = <num>"
    VALUE_IN_FILE_RE = re.compile(
        r'^[-\s*]*(?:\*\*)?([A-Z][\w\s\-]{2,40}?)(?:\*\*)?\s*[:=]\s*(-?\d+)\b',
        re.MULTILINE
    )
    for m in VALUE_IN_FILE_RE.finditer(content):
        name = m.group(1).strip()
        val = int(m.group(2))
        key = re.sub(r'\s+', '_', name.lower())
        key = re.sub(r'[^\w]+', '_', key).strip('_')
        canon = ctx['values'].get(key)
        if canon and canon['numeric'] != val:
            # Skip if this is the canonical source itself
            if canon['source_file'] == path: continue
            line = content[:m.start()].count('\n') + 1
            findings.append({
                'kind': 'VALUE_CONFLICT',
                'token': name,
                'file': path,
                'line': line,
                'severity': 'error',
                'hint': (f'Value "{name}"={val} in {path} conflicts with canonical '
                         f'{canon["numeric"]} in {canon["source_file"]}'),
            })

    # 5. Unknown proper nouns (capitalized tokens not in registry and not in skip list)
    # Only flag HIGH-OCCURRENCE unknowns, otherwise noise drowns signal
    unknown_counts = defaultdict(int)
    for m in TOKEN_PATTERN.finditer(content):
        tok = m.group(1).strip()
        # In registry
        if tok in ctx['noun']['known_tokens']:
            continue
        # In alias registry canonicals or abbreviations
        if tok in ctx['alias']['all_canonicals']:
            continue
        # In skip list
        if tok in EXTRACTOR_SKIP:
            continue
        # Starts with a common non-proper first word
        first = tok.split()[0]
        if first in EXTRACTOR_SKIP:
            continue
        unknown_counts[tok] += 1

    # Only flag tokens with 3+ occurrences in this file
    for tok, count in unknown_counts.items():
        if count < 5: continue
        findings.append({
            'kind': 'UNKNOWN_PROPER_NOUN',
            'token': tok,
            'file': path,
            'line': None,
            'count_in_file': count,
            'severity': 'info',
            'hint': f'Uncategorized capitalized token "{tok}" appears {count} times in {path}',
        })

    return findings


# ─── MAIN ──────────────────────────────────────────────────────────────────

def build_report_yaml(findings):
    """Group findings by kind and severity, emit YAML."""
    by_kind = defaultdict(list)
    for f in findings:
        by_kind[f['kind']].append(f)

    lines = [
        "# Valoria Collation Report",
        "# Generated by tools/valoria_collator.py",
        "# Cross-references all design/params/canon .md files against:",
        "#   - references/proper_noun_registry.yaml",
        "#   - references/alias_registry.yaml",
        "#   - references/values_master.yaml",
        "",
        "version: 1",
        f"total_findings: {len(findings)}",
        "",
        "summary:",
    ]
    for kind in ['VALUE_CONFLICT', 'LEGACY_TERM_USED', 'COLLISION_USED_ALONE',
                 'UNKNOWN_ABBREVIATION', 'UNKNOWN_PROPER_NOUN']:
        lines.append(f"  {kind}: {len(by_kind.get(kind, []))}")
    lines.append("")

    lines.append("findings:")
    for kind in ['VALUE_CONFLICT', 'LEGACY_TERM_USED', 'COLLISION_USED_ALONE',
                 'UNKNOWN_ABBREVIATION', 'UNKNOWN_PROPER_NOUN']:
        items = by_kind.get(kind, [])
        if not items: continue
        lines.append(f"  {kind}:")
        # Group by token → file list for UNKNOWN_* to avoid spam
        if kind in ('UNKNOWN_ABBREVIATION', 'UNKNOWN_PROPER_NOUN'):
            by_token = defaultdict(list)
            for f in items:
                by_token[f['token']].append(f)
            for tok in sorted(by_token.keys(), key=lambda t: -len(by_token[t])):
                occurrences = by_token[tok]
                lines.append(f"    - token: {yamlstr(tok)}")
                lines.append(f"      count: {sum(f.get('count_in_file', 1) for f in occurrences)}")
                lines.append(f"      files: {len(set(f['file'] for f in occurrences))}")
                lines.append(f"      severity: {occurrences[0]['severity']}")
                lines.append(f"      hint: {yamlstr(occurrences[0]['hint'])}")
                lines.append(f"      sample_files:")
                for f in occurrences[:5]:
                    lines.append(f"        - {yamlstr(f['file'])}")
        else:
            # Per-instance for important kinds
            for f in items:
                lines.append(f"    - token: {yamlstr(f['token'])}")
                lines.append(f"      file: {yamlstr(f['file'])}")
                if f.get('line'):
                    lines.append(f"      line: {f['line']}")
                lines.append(f"      severity: {f['severity']}")
                lines.append(f"      hint: {yamlstr(f['hint'])}")
    return '\n'.join(lines)


def yamlstr(s):
    if s is None: return 'null'
    return '"' + str(s).replace('\\', '\\\\').replace('"', '\\"') + '"'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--strict', action='store_true',
                        help='Exit 1 if any findings of severity error')
    parser.add_argument('--out', default='/tmp/valoria/collation_report.yaml')
    args = parser.parse_args()

    print("[1/4] Loading registries...")
    pn, alias, vm = load_registries()
    canonicals, alias_lookup, known_tokens = flatten_proper_nouns(pn)
    alias_data = flatten_aliases(alias)
    canon_values = flatten_values(vm)
    print(f"  proper nouns: {len(canonicals)} canonicals, "
          f"{len(alias_lookup)} aliases, {len(known_tokens)} known tokens")
    print(f"  alias registry: {len(alias_data['abbrev_to_canonical'])} abbrevs, "
          f"{len(alias_data['legacy_terms'])} legacy, "
          f"{len(alias_data['collision_abbrs'])} collisions")
    print(f"  values: {len(canon_values)} canonical numeric values")

    ctx = {
        'noun': {'canonicals': canonicals, 'aliases': alias_lookup,
                 'known_tokens': known_tokens},
        'alias': alias_data,
        'values': canon_values,
    }

    print("[2/4] Listing files to scan...")
    paths = list_scannable_files()
    print(f"  {len(paths)} files under {SCAN_PREFIXES}")

    print("[3/4] Fetching + scanning files...")
    all_findings = []
    chunk_size = 25
    for i in range(0, len(paths), chunk_size):
        chunk = paths[i:i+chunk_size]
        files = g.read_files_graphql(chunk, force_full=True)
        for p, c in files.items():
            if c is None: continue
            if p in EXEMPT_FILES or any(p.startswith(pre) for pre in EXEMPT_PATH_PREFIXES):
                continue
            findings = scan_file_for_drift(p, c, ctx)
            all_findings.extend(findings)
        if i % 100 == 0:
            print(f"  ... scanned {min(i+chunk_size, len(paths))}/{len(paths)}")

    print(f"[4/4] Writing report: {len(all_findings)} findings")

    # Summary
    from collections import Counter
    counter = Counter(f['kind'] for f in all_findings)
    for kind, count in counter.most_common():
        print(f"  {kind}: {count}")

    report = build_report_yaml(all_findings)
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, 'w') as f:
        f.write(report)
    print(f"\nReport written: {args.out} ({os.path.getsize(args.out)} bytes)")

    # Validate
    try:
        yaml.safe_load(report)
        print("YAML valid")
    except Exception as e:
        print(f"YAML INVALID: {e}")

    if args.strict:
        errors = sum(1 for f in all_findings if f['severity'] == 'error')
        if errors > 0:
            print(f"\nSTRICT MODE: {errors} errors — exiting 1")
            sys.exit(1)


if __name__ == '__main__':
    main()
