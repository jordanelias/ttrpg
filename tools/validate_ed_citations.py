#!/usr/bin/env python3
"""
validate_ed_citations.py — citation-integrity guard for the editorial register.

WHY THIS EXISTS
---------------
The 2026-05-31 P1 resolver incident (ED-883): params/factions/stats_1_7_scale.md
asserted the Domain Action resolver "CANONICAL (ED-865/874, ratified 2026-05-29)"
and extended it (treaty positioning, unique actions, bare-stat supersession) on the
same authority — but ED-874 and ED-885 were never written to the ledger, and ED-865
was OPEN and its text *strikes* the resolver's justification rather than ratifying it.
Nothing caught this: existing hooks check ID uniqueness and JSONL validity WITHIN the
ledger, but nothing verified that ED references in canon/design docs RESOLVE to real,
non-open entries. This tool closes that gap.

WHAT IT FLAGS (both are errors; exit 1 in CI)
---------------------------------------------
  NONEXISTENT   — a cited ED-NNN is absent from the ledger universe (active + archives).
  OPEN_AS_BASIS — a cited ED-NNN is OPEN (not resolved/struck) AND the surrounding text
                  claims it as a basis: canonical / ratified / applied / extension /
                  superseded / per ED / closes / approved.

A bare reference to an open item *without* a ratification claim is allowed (you may
discuss open work) and reported only at INFO level (--info).

SCOPE (v1): ED citations only. PP/patch-register support is a follow-on (needs the
active + archived patch registers loaded the same way). See checked_prefixes.

USAGE (reads the local working tree — no PAT, no network):
    python3 tools/validate_ed_citations.py                     # full scan, exit 1 on violations
    python3 tools/validate_ed_citations.py --path PATH ...     # scan only these repo paths
    python3 tools/validate_ed_citations.py --info              # also print INFO open-refs

The pure core (audit_citations / build_status_map / _is_resolved) is import-testable
with no network — see tests/hooks/test_ed_citation_integrity.py.
"""
import os, re, sys, json, argparse

REPO = 'jordanelias/ttrpg'

CITE_RE = re.compile(r'\b(ED|PP)-(\d{1,4}(?:/\d{1,4})*)\b')   # captures compact groups: ED-865/874

# Words that turn a citation into a *claim of authority* on the citing doc.
BASIS_KEYWORDS = (
    'canonical', 'ratif', 'applied', 'apply', 'closes', 'closed by',
    'resolved by', 'approved', 'extension', 'superseded', 'per ed', 'per pp',
)
CONTEXT = 90  # chars of context captured each side of a citation

# Source-of-truth registers are never scanned as "citing docs".
REGISTER_PATHS = {'canon/editorial_ledger.jsonl', 'canon/patch_register_active.yaml'}
# Frozen history: citations there are records, not live claims.
SKIP_PREFIXES = ('archives/', 'deprecated/', 'references/atoms_pending/')
# Live docs that can make canonical claims.
SCAN_PREFIXES = ('canon/', 'designs/', 'params/', 'references/')
SCAN_SUFFIXES = ('.md', '.yaml', '.yml')

# Editorial-archive locations (the ED universe is the active JSONL + these).
ARCHIVE_GLOBS = ('archives/editorial/', 'archives/editorials/', 'deprecated/canon/')


# ── Pure core (network-free; unit-tested) ─────────────────────────────────────

def _canon_id(prefix: str, num: str) -> str:
    """Normalise ED-017 / ED-17 -> 'ED-17' so zero-padding never mismatches."""
    return f"{prefix}-{int(num)}"


def _is_resolved(status) -> bool:
    """A citation basis is satisfied only by a resolved/struck/applied/superseded entry."""
    if status is None:
        return False
    s = str(status).lower()
    return s.startswith('resolved') or s in ('struck', 'applied', 'superseded', 'closed')


def build_status_map(entries) -> dict:
    """entries: iterable of {'id','status'} dicts -> {canon_id: status}."""
    out = {}
    for e in entries:
        i = (e or {}).get('id')
        if not i:
            continue
        m = re.match(r'^(ED|PP)-(\d+)$', str(i).strip())
        if m:
            out[_canon_id(m.group(1), m.group(2))] = e.get('status')
    return out


def audit_citations(docs: dict, status_map: dict, checked_prefixes=('ED',)) -> list:
    """
    docs:        {path: text}
    status_map:  {canon_id: status}  (canon_id missing => nonexistent)
    Returns list of violation dicts: {path,line,id,kind[,status],ctx}.
    """
    out = []
    checked = set(checked_prefixes)
    for path, text in docs.items():
        for m in CITE_RE.finditer(text):
            prefix = m.group(1)
            if prefix not in checked:
                continue
            line = text.count('\n', 0, m.start()) + 1
            ctx = text[max(0, m.start() - CONTEXT): m.end() + CONTEXT].replace('\n', ' ').strip()
            ctx_l = ctx.lower()
            for num in m.group(2).split('/'):        # expand compact "ED-865/874" -> 865, 874
                raw = f"{prefix}-{num}"
                key = _canon_id(prefix, num)
                if key not in status_map:
                    out.append({'path': path, 'line': line, 'id': raw, 'kind': 'NONEXISTENT', 'ctx': ctx})
                elif not _is_resolved(status_map[key]):
                    kind = 'OPEN_AS_BASIS' if any(k in ctx_l for k in BASIS_KEYWORDS) else 'OPEN_INFO'
                    out.append({'path': path, 'line': line, 'id': raw, 'kind': kind, 'status': status_map[key], 'ctx': ctx})
    return out


# ── Local working-tree layer (default; no network, no PAT) ───────────────────

def _walk_entries(obj):
    """Yield dicts that look like ledger entries ({'id': 'ED-..'}) anywhere in a YAML structure."""
    if isinstance(obj, dict):
        if 'id' in obj and re.match(r'^(ED|PP)-\d+$', str(obj.get('id')).strip()):
            yield obj
        for v in obj.values():
            yield from _walk_entries(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _walk_entries(v)


def _read(path):
    try:
        with open(path, encoding='utf-8', errors='replace') as f:
            return f.read()
    except (FileNotFoundError, IsADirectoryError):
        return None


def _walk_repo_files():
    out = []
    for base in ('canon', 'designs', 'params', 'references', 'archives', 'deprecated'):
        if not os.path.isdir(base):
            continue
        for root, _dirs, files in os.walk(base):
            for fn in files:
                out.append(os.path.join(root, fn).replace('\\', '/'))
    return out


def load_ed_universe() -> dict:
    """Active JSONL ledger + editorial archive YAMLs on disk -> {canon_id: status}."""
    import yaml
    entries = []
    led = _read('canon/editorial_ledger.jsonl') or ''
    for ln in led.splitlines():
        ln = ln.strip()
        if ln:
            try:
                entries.append(json.loads(ln))
            except Exception:
                pass
    for ap in _walk_repo_files():
        if (any(ap.startswith(g) for g in ARCHIVE_GLOBS)
                and 'editorial_ledger' in ap and ap.endswith(('.yaml', '.yml'))):
            raw = _read(ap)
            if not raw:
                continue
            try:
                data = yaml.safe_load(raw)
            except Exception:
                continue
            for d in _walk_entries(data):
                entries.append(d)
    return build_status_map(entries)


def select_docs(only_paths=None):
    if only_paths:
        return list(only_paths)
    return [p for p in _walk_repo_files()
            if p not in REGISTER_PATHS
            and any(p.startswith(s) for s in SCAN_PREFIXES)
            and not any(p.startswith(s) for s in SKIP_PREFIXES)
            and p.endswith(SCAN_SUFFIXES)]


def main():
    ap = argparse.ArgumentParser(description='Validate ED citations against the editorial ledger universe (reads the working tree).')
    ap.add_argument('--path', nargs='*', default=None, help='Scan only these repo paths.')
    ap.add_argument('--info', action='store_true', help='Also print INFO-level open references.')
    args = ap.parse_args()

    status_map = load_ed_universe()
    print(f'ED universe: {len(status_map)} ids loaded (active + archives)')

    paths = select_docs(args.path)
    docs = {}
    for p in paths:
        c = _read(p)
        if c is not None:
            docs[p] = c
    print(f'Scanning {len(docs)} doc(s) for ED citations...\n')

    viols = audit_citations(docs, status_map, checked_prefixes=('ED',))
    errors = [v for v in viols if v['kind'] in ('NONEXISTENT', 'OPEN_AS_BASIS')]
    infos = [v for v in viols if v['kind'] == 'OPEN_INFO']

    for v in sorted(errors, key=lambda x: (x['kind'], x['path'], x['line'])):
        extra = f" (status={v.get('status')})" if 'status' in v else ''
        print(f"[{v['kind']}] {v['path']}:{v['line']} cites {v['id']}{extra}")
        print(f"    …{v['ctx']}…")
    if args.info:
        for v in infos:
            print(f"[OPEN_INFO] {v['path']}:{v['line']} references {v['id']} (status={v.get('status')})")

    print(f"\n{len(errors)} citation-integrity violation(s); {len(infos)} open-reference info.")
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
