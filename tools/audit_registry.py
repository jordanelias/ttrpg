#!/usr/bin/env python3
"""
audit_registry.py — the one reader/writer for references/audit_registry.jsonl.

One rule, one home (CLAUDE.md §8): every Valoria audit/simulation skill appends its
verdict here on completion (via `append`); the dashboard (tools/dashboard_data.py),
the freshness gate (tools/ci_audit_registry_check.py), and optionally the
SessionStart banner all read it back through this module (via `summary`). Never
hand-edit the JSONL directly and never re-implement this logic elsewhere.

Format: JSONL (one JSON object per line), NOT YAML — deliberately. Multiple
concurrent-session skill runs append independently; a YAML list would hit the
same merge-collision failure HANDOFF.md and editorial_ledger.yaml both hit before
their splits (CLAUDE.md §1/§3). Plain append-only is sufficient here (no lane
split needed) because audit runs are far less frequent than editorial decisions.

Modes:
  append   --audit-type ... --subsystem ... --skill ... --date YYYY-MM-DD
           --folder ... --scope "..." --verdict ... [--verdict-detail "..."]
           [--confidence measured|inferred] [--id ...]
  summary  print the latest entry per (audit_type, subsystem) pair, newest first.
           "Latest" is resolved by `date` (ties broken by file order, last-line-
           wins) — never by trusting `id` uniqueness, since two runs of the same
           audit on the same day can legitimately share an id.

Defensive by contract, mirroring workplan_status.py: summary() never raises —
a missing/unreadable registry degrades to an empty list, not a crash, since
this is read by the SessionStart-adjacent tooling chain.
"""
import argparse
import json
import os
import sys

REGISTRY = os.path.join('references', 'audit_registry.jsonl')
SCHEMA_VERSION = 1

AUDIT_TYPES = {
    'canon_guard', 'mechanic_audit', 'resolution_diagnostic', 'module_adjudicator',
    'vector_audit', 'editorial_register', 'simulation_balance',
}
# Coarse rollup matching CURRENT.md's table rows — one level up from
# references/canonical_sources.yaml's ~60 fine-grained `systems:` keys (which stays
# the finer controlled vocabulary; cite it in --scope for precision). Not a fixed
# enforced enum: CURRENT.md gaining/splitting a row is the trigger to add a value
# here, not the other way around (see tools/dashboard_data.py's freshness notes).
SUBSYSTEMS = {
    'personal_combat', 'mass_battle', 'social_contest', 'faction_political',
    'settlement_territory', 'threadwork', 'fieldwork_investigation', 'architecture',
    'cross_cutting', 'corpus_wide',
}
VERDICTS = {'PASS', 'FAIL', 'PARTIAL', 'CONFORMANT', 'NON_CONFORMANT', 'OPEN', 'MIXED', 'CLOSED'}
CONFIDENCES = {'measured', 'inferred'}

REQUIRED_FIELDS = ('audit_type', 'subsystem', 'skill', 'date', 'folder', 'scope', 'verdict')


def _warn(msg):
    print(f"WARN audit_registry: {msg}", file=sys.stderr)


def append_record(record):
    """Validate and append one record to the registry. Raises ValueError on a
    missing required field; unknown-but-present enum values only warn (the
    vocabulary is deliberately extensible, not hard-blocked — see SUBSYSTEMS note)."""
    missing = [f for f in REQUIRED_FIELDS if not record.get(f)]
    if missing:
        raise ValueError(f"missing required field(s): {', '.join(missing)}")
    if record['audit_type'] not in AUDIT_TYPES:
        _warn(f"audit_type '{record['audit_type']}' not in the known set {sorted(AUDIT_TYPES)} — appending anyway")
    if record['subsystem'] not in SUBSYSTEMS:
        _warn(f"subsystem '{record['subsystem']}' not in the known set {sorted(SUBSYSTEMS)} — appending anyway")
    if record['verdict'] not in VERDICTS:
        _warn(f"verdict '{record['verdict']}' not in the known set {sorted(VERDICTS)} — appending anyway")
    if not record.get('confidence'):
        record['confidence'] = 'measured'
    if record['confidence'] not in CONFIDENCES:
        raise ValueError(f"confidence must be one of {sorted(CONFIDENCES)}")
    record['schema_version'] = record.get('schema_version') or SCHEMA_VERSION
    if not record.get('id'):
        record['id'] = f"{record['skill']}-{record['date']}"
    record['verdict_detail'] = record.get('verdict_detail') or ''

    os.makedirs(os.path.dirname(REGISTRY), exist_ok=True)
    with open(REGISTRY, 'a', encoding='utf-8') as f:
        f.write(json.dumps(record, ensure_ascii=False) + '\n')
    return record


def _load_all():
    if not os.path.exists(REGISTRY):
        return []
    records = []
    with open(REGISTRY, encoding='utf-8') as f:
        for lineno, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as e:
                _warn(f"{REGISTRY}:{lineno} unparseable, skipping ({e})")
    return records


def summary():
    """Latest record per (audit_type, subsystem), ordered by `date` then file
    order (last line for a given date wins ties). Never raises."""
    try:
        records = _load_all()
    except Exception as e:  # never break a caller (dashboard build, SessionStart)
        _warn(f"could not read registry: {e}")
        return []
    latest = {}
    for r in records:
        key = (r.get('audit_type'), r.get('subsystem'))
        prev = latest.get(key)
        if prev is None or (r.get('date', '') >= prev.get('date', '')):
            latest[key] = r
    return sorted(latest.values(), key=lambda r: (r.get('subsystem') or '', r.get('audit_type') or ''))


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='mode')

    p_append = sub.add_parser('append', help='append one verdict record')
    p_append.add_argument('--id')
    p_append.add_argument('--audit-type', dest='audit_type', required=True)
    p_append.add_argument('--subsystem', required=True)
    p_append.add_argument('--skill', required=True)
    p_append.add_argument('--date', required=True, help='YYYY-MM-DD')
    p_append.add_argument('--folder', required=True)
    p_append.add_argument('--scope', required=True)
    p_append.add_argument('--verdict', required=True)
    p_append.add_argument('--verdict-detail', dest='verdict_detail', default='')
    p_append.add_argument('--confidence', default='measured')

    sub.add_parser('summary', help='print latest verdict per (audit_type, subsystem)')

    args = parser.parse_args()

    if args.mode == 'append':
        record = {
            'id': args.id,
            'audit_type': args.audit_type,
            'subsystem': args.subsystem,
            'skill': args.skill,
            'date': args.date,
            'folder': args.folder,
            'scope': args.scope,
            'verdict': args.verdict,
            'verdict_detail': args.verdict_detail,
            'confidence': args.confidence,
        }
        try:
            saved = append_record(record)
        except ValueError as e:
            print(f"ERROR: {e}", file=sys.stderr)
            sys.exit(1)
        print(f"appended: {saved['id']}")
    else:
        for r in summary():
            print(json.dumps(r, ensure_ascii=False))


if __name__ == '__main__':
    main()
