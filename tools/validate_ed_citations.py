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

LANE-TAGGED IDS (2026-07-02, ED-IN-0001): new EDs use ED-<LANE>-NNNN (e.g. ED-MB-0001)
alongside the flat ED-NNNN format, which is FROZEN (no new allocations) but stays
permanently valid for existing citations. See references/id_reservations.yaml for the
lane roster and allocation protocol, CLAUDE.md section 3 for the format contract. Both
formats resolve through the same universe/audit path below.

USAGE (reads the local working tree — no PAT, no network):
    python3 tools/validate_ed_citations.py                     # full scan, exit 1 on violations
    python3 tools/validate_ed_citations.py --path PATH ...     # scan only these repo paths
    python3 tools/validate_ed_citations.py --info              # also print INFO open-refs

The pure core (audit_citations / build_status_map / _is_resolved) is import-testable
with no network — see tests/hooks/test_ed_citation_integrity.py.
"""
import os, re, sys, json, argparse

REPO = 'jordanelias/ttrpg'

# Lane roster for the ED-<LANE>-NNNN namespace (references/id_reservations.yaml is the
# source of truth for allocation; kept here too since the regex needs the closed set).
LANE_CODES = ('MB', 'PC', 'FI', 'SC', 'FA', 'WR', 'IN', 'GO', 'SE')
_LANE_ALT = '|'.join(LANE_CODES)

# Captures compact groups (ED-865/874) and inclusive ranges (ED-844-856 / ED-844–856),
# with an optional lane tag (ED-MB-0001) restricted to the closed LANE_CODES set so a
# stray two-uppercase-letter token elsewhere never false-positives as a lane. The
# numeric grammar (group 3) is IDENTICAL whether or not a lane tag is present, so
# _expand_nums / range handling below is untouched by the lane-tag addition.
CITE_RE = re.compile(
    rf'\b(ED|PP)-(?:({_LANE_ALT})-)?(\d{{1,4}}(?:/\d{{1,4}})*(?:[-–]\d{{1,4}})?)\b')

# Words that turn a citation into a *claim of authority* on the citing doc.
BASIS_KEYWORDS = (
    'canonical', 'ratif', 'applied', 'apply', 'closes', 'closed by',
    'resolved by', 'approved', 'extension', 'superseded', 'per ed', 'per pp',
)
# Planning / negation context: the citation is being discussed or proposed, not
# asserted as a firm canonical basis. Demotes an OPEN_AS_BASIS hit to OPEN_INFO.
NONBASIS_MARKERS = (
    'execution pending', 'pending', 'proposed', 'awaiting', 'new ed',
    'not re-filed', 'do not apply', "don't apply", 'contradiction',
    'flagged', 'flag for', 'spun out',
)
CONTEXT = 90  # chars of context captured each side of a citation

# Source-of-truth registers are never scanned as "citing docs".
REGISTER_PATHS = {'canon/editorial_ledger.jsonl', 'canon/patch_register_active.yaml'}
# Frozen history: citations there are records, not live claims.
SKIP_PREFIXES = ('archives/', 'deprecated/', 'references/atoms_pending/')
# Working documents (audits, workplans) PROPOSE and TRACK EDs — they do not
# assert canon, so they are out of the validator's mandate (which is canonical
# surfaces only). Excluded from scanning entirely. See _is_working_doc.
WORKING_PREFIXES = ('designs/audit/', 'designs/workplans/')
# Provenance registers RECORD where an ED applies; a citation there is a record,
# never a canonical-basis claim. Demoted to OPEN_INFO. See _is_provenance.
PROVENANCE_PATHS = {
    'references/roadmap_state.yaml',
    'references/synonym_registry.yaml',
    'references/mechanical_terms_index.md',
    'canon/supersession_register.yaml',
}
PROVENANCE_PREFIXES = ('references/splits/',)
# Live docs that can make canonical claims.
SCAN_PREFIXES = ('canon/', 'designs/', 'params/', 'references/')
SCAN_SUFFIXES = ('.md', '.yaml', '.yml')

# Editorial-archive locations (the ED universe is the active JSONL + these).
ARCHIVE_GLOBS = ('archives/editorial/', 'archives/editorials/', 'deprecated/canon/')

# JSONL archive siblings of the active ledger (canon/editorial_ledger.jsonl's own overflow
# chunks, per the register-size cap in tools/ci_register_size_check.py — mirrors the
# patch_register_active.yaml / patch_register_archive.yaml co-location convention, not the
# older ARCHIVE_GLOBS directories which predate the 2026-05-28 JSONL migration).
ARCHIVE_JSONL_PATHS = ('canon/editorial_ledger_archive.jsonl',)


# ── Pure core (network-free; unit-tested) ─────────────────────────────────────

def _canon_id(prefix: str, num: str, lane: str = None) -> str:
    """Normalise ED-017 / ED-17 -> 'ED-17' (flat) or ED-MB-0001 / ED-MB-1 -> 'ED-MB-1'
    (lane-tagged) so zero-padding never mismatches either format."""
    if lane:
        return f"{prefix}-{lane}-{int(num)}"
    return f"{prefix}-{int(num)}"


def _is_resolved(status) -> bool:
    """A citation basis is satisfied by any terminal/decided entry. Accepts the
    canonical statuses plus their legitimate synonyms (ratified/confirmed) and
    terminal states (deprecated) so a genuinely-decided ED is never a violation."""
    if status is None:
        return False
    s = str(status).strip().lower()
    return (s.startswith('resolved') or s.startswith('ratif')   # ratified / ratified-...
            or s in ('struck', 'applied', 'superseded', 'closed', 'confirmed', 'deprecated'))


def _is_working_doc(path: str) -> bool:
    """Audits/workplans propose & track EDs; they don't assert canon — out of mandate."""
    if any(path.startswith(p) for p in WORKING_PREFIXES):
        return True
    return 'workplan' in path.rsplit('/', 1)[-1].lower()


def _is_provenance(path: str) -> bool:
    """Provenance registers record where an ED applies — never a basis claim."""
    return path in PROVENANCE_PATHS or any(path.startswith(p) for p in PROVENANCE_PREFIXES)


def _expand_nums(group: str) -> list:
    """Expand a citation's numeric group into individual ED numbers.

    Handles slash groups (865/874 -> [865, 874]) and inclusive ranges
    (844-856 / 844–856 -> [844..856]). Ranges wider than 200 are not expanded
    (only the low bound is checked) to guard against pathological spans.
    """
    nums = []
    for token in group.split('/'):
        rng = re.match(r'^(\d{1,4})[-–](\d{1,4})$', token)
        if rng:
            lo, hi = int(rng.group(1)), int(rng.group(2))
            if lo <= hi <= lo + 200:
                nums.extend(str(n) for n in range(lo, hi + 1))
            else:
                nums.append(rng.group(1))
        else:
            nums.append(token)
    return nums


def build_status_map(entries) -> dict:
    """entries: iterable of {'id','status'} dicts -> {canon_id: status}."""
    out = {}
    for e in entries:
        i = (e or {}).get('id')
        if not i:
            continue
        m = re.match(rf'^(ED|PP)-(?:({_LANE_ALT})-)?(\d+)$', str(i).strip())
        if m:
            out[_canon_id(m.group(1), m.group(3), m.group(2))] = e.get('status')
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
        prov = _is_provenance(path)
        for m in CITE_RE.finditer(text):
            prefix = m.group(1)
            if prefix not in checked:
                continue
            lane = m.group(2)
            line = text.count('\n', 0, m.start()) + 1
            ctx = text[max(0, m.start() - CONTEXT): m.end() + CONTEXT].replace('\n', ' ').strip()
            # Basis detection uses the citation's OWN line only — a 90-char window
            # bleeds across table-row / list-item boundaries and counts a neighbour
            # row's "RESOLVED"/"canonical" as if it qualified this citation (false
            # OPEN_AS_BASIS). The display ctx above stays wide for human context.
            ls = text.rfind('\n', 0, m.start()) + 1
            le = text.find('\n', m.end())
            ctx_l = text[ls:(le if le != -1 else len(text))].lower()
            for num in _expand_nums(m.group(3)):
                raw = f"{prefix}-{lane}-{num}" if lane else f"{prefix}-{num}"
                key = _canon_id(prefix, num, lane)
                if key not in status_map:
                    out.append({'path': path, 'line': line, 'id': raw, 'kind': 'NONEXISTENT', 'ctx': ctx})
                elif not _is_resolved(status_map[key]):
                    # A basis claim requires a basis keyword AND a non-provenance file
                    # AND no planning/negation marker that recasts it as discussion.
                    is_basis = (not prov
                                and any(k in ctx_l for k in BASIS_KEYWORDS)
                                and not any(n in ctx_l for n in NONBASIS_MARKERS))
                    kind = 'OPEN_AS_BASIS' if is_basis else 'OPEN_INFO'
                    out.append({'path': path, 'line': line, 'id': raw, 'kind': kind, 'status': status_map[key], 'ctx': ctx})
    return out


# ── Local working-tree layer (default; no network, no PAT) ───────────────────

def _walk_entries(obj):
    """Yield dicts that look like ledger entries ({'id': 'ED-..'} or {'id': 'ED-MB-..'})
    anywhere in a YAML structure."""
    if isinstance(obj, dict):
        if 'id' in obj and re.match(rf'^(ED|PP)-(?:(?:{_LANE_ALT})-)?\d+$', str(obj.get('id')).strip()):
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


# id + (optionally) nearby status, tolerant of malformed/garbled YAML indentation.
# Flat ED-\d+ only, by design: archives under ARCHIVE_GLOBS predate the lane-tagged
# namespace (2026-07-02) and can never contain an ED-<LANE>-NNNN id.
_SALVAGE_ID = re.compile(r'(?:^|[\s"\'-])id["\']?\s*:\s*["\']?(ED-\d+)', re.M)
_SALVAGE_STATUS = re.compile(r'status["\']?\s*:\s*["\']?([A-Za-z][\w-]*)')


def _salvage_entries(raw: str) -> list:
    """Recover {'id','status'} entries from an archive whose YAML won't parse.

    Frozen archive fragments carry orphaned/mixed-indent lines that defeat
    yaml.safe_load. Rather than silently lose every ID in the file (or hand-edit
    frozen history), pull each `id: ED-NNN` and the `status:` in its block so the
    universe still includes archived IDs. Status is read from the window up to the
    next `id:` (its own block); absent => None (still registers ID existence)."""
    out = []
    hits = list(_SALVAGE_ID.finditer(raw))
    for i, m in enumerate(hits):
        end = hits[i + 1].start() if i + 1 < len(hits) else len(raw)
        block = raw[m.end():end]
        sm = _SALVAGE_STATUS.search(block)
        out.append({'id': m.group(1), 'status': sm.group(1) if sm else None})
    return out


def _walk_repo_files():
    out = []
    for base in ('canon', 'designs', 'params', 'references', 'archives', 'deprecated'):
        if not os.path.isdir(base):
            continue
        for root, _dirs, files in os.walk(base):
            for fn in files:
                out.append(os.path.join(root, fn).replace('\\', '/'))
    return out


def load_ed_universe(warn=True) -> dict:
    """Active JSONL ledger + editorial archive YAMLs/JSONLs on disk -> {canon_id: status}.

    The active ledger is AUTHORITATIVE. Archive entries are loaded FIRST and the
    active JSONL LAST, so that build_status_map's last-write-wins ordering lets a
    current active-ledger status override any stale archived copy of the same ID
    (e.g. an archived 'ED-864: open' must not shadow the active 'ED-864: struck').

    Archive YAML parse failures are SURFACED (stderr) and counted, never silently
    swallowed — otherwise the 'active + archives' universe would quietly shrink to
    active-only and start emitting false NONEXISTENTs for archive-only IDs.
    """
    import yaml
    archive_entries = []
    dropped = []
    for ap in _walk_repo_files():
        if (any(ap.startswith(g) for g in ARCHIVE_GLOBS)
                and 'editorial_ledger' in ap and ap.endswith(('.yaml', '.yml'))):
            raw = _read(ap)
            if not raw:
                continue
            try:
                data = yaml.safe_load(raw)
                parsed = list(_walk_entries(data))
            except Exception as e:
                # Don't lose the file: salvage its IDs via regex, but record that
                # it is malformed so the breakage stays visible.
                salvaged = _salvage_entries(raw)
                dropped.append((ap, (str(e).splitlines()[0] if str(e) else type(e).__name__), len(salvaged)))
                archive_entries.extend(salvaged)
                continue
            archive_entries.extend(parsed)
    for ap in ARCHIVE_JSONL_PATHS:
        raw = _read(ap)
        if not raw:
            continue
        bad_lines = 0
        for ln in raw.splitlines():
            ln = ln.strip()
            if not ln:
                continue
            try:
                archive_entries.append(json.loads(ln))
            except Exception:
                bad_lines += 1
        if warn and bad_lines:
            dropped.append((ap, f"{bad_lines} malformed JSONL line(s)", 0))
    active_entries = []
    led = _read('canon/editorial_ledger.jsonl') or ''
    for ln in led.splitlines():
        ln = ln.strip()
        if ln:
            try:
                active_entries.append(json.loads(ln))
            except Exception:
                pass
    if warn and dropped:
        sys.stderr.write(
            f"WARNING: {len(dropped)} editorial-archive file(s) failed YAML parse; "
            f"IDs salvaged via regex fallback (fix the source YAML to silence this):\n")
        for ap, msg, n in dropped:
            sys.stderr.write(f"  - {ap}: {msg} (salvaged {n} id(s))\n")
    # archives first, active last → active status is authoritative on conflict.
    return build_status_map(archive_entries + active_entries)


def select_docs(only_paths=None):
    if only_paths:
        return list(only_paths)
    return [p for p in _walk_repo_files()
            if p not in REGISTER_PATHS
            and any(p.startswith(s) for s in SCAN_PREFIXES)
            and not any(p.startswith(s) for s in SKIP_PREFIXES)
            and not _is_working_doc(p)
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
    print('Mandate: canonical surfaces only — audits/workplans excluded '
          '(designs/audit/, designs/workplans/, *workplan*); provenance registers '
          'reported as INFO, not basis.')
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
