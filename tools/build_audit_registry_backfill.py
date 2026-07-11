#!/usr/bin/env python3
"""
build_audit_registry_backfill.py — one-time historical backfill for
references/audit_registry.jsonl from designs/audit/.

Scans BOTH the dated subdirectories (designs/audit/YYYY-MM-DD-slug/) and the
dated flat .md files directly in designs/audit/ (designs/audit/YYYY-MM-DD-slug.md)
— roughly half of all historical entries are flat files, not folders, so a
directories-only glob silently drops them.

Deliberately conservative: only writes a record when BOTH the audit_type and the
date are unambiguous from a strong signal (a named verdict heading, a
distinctive filename pattern) and a verdict token was actually found. Everything
else is logged to stderr and skipped — a sparse, high-precision registry beats a
complete, guessed one (this corpus is already wary of leaky fabrication gates,
CLAUDE.md §7; this scanner is exactly that kind of heuristic instrument). Every
written record gets confidence: inferred, subsystem: null when no single
subsystem keyword clearly wins (dashboard/registry consumers must treat a null
subsystem as "uncategorized", not silently drop or misfile it).

Run once, by hand, review the diff, then commit references/audit_registry.jsonl.
Not part of any CI/hook — see tools/ci_audit_registry_check.py for the ongoing
(report-only) freshness gate instead.
"""
import json
import os
import re
import sys

AUDIT_DIR = os.path.join('designs', 'audit')
OUT = os.path.join('references', 'audit_registry.jsonl')

DATE_RE = re.compile(r'^(\d{4}-\d{2}-\d{2})-(.+)$')

# (regex over combined filename+content, audit_type) — first match wins, ordered
# most-specific first so e.g. "ners_verdict" doesn't get shadowed by a looser rule.
AUDIT_TYPE_SIGNALS = [
    (re.compile(r'ners_verdict|NERS Verdict|resolution.diagnostic', re.I), 'resolution_diagnostic'),
    (re.compile(r'GRAPH VERDICT|module.adjudicat', re.I), 'module_adjudicator'),
    (re.compile(r'^# Canon Guard Report|canon.guard', re.I), 'canon_guard'),
    (re.compile(r'weapon_rebalance|weapon_balance|combat.armature|balance.proposal|matchup', re.I), 'simulation_balance'),
    (re.compile(r'vector.audit|topographic.audit', re.I), 'vector_audit'),
    (re.compile(r'mechanic.audit|mechanical.audit|number.system.*audit|formula.audit', re.I), 'mechanic_audit'),
    (re.compile(r'editorial.register|editorial.ledger.audit', re.I), 'editorial_register'),
]

# (regex, subsystem) — only used when exactly one matches; ambiguous -> null.
SUBSYSTEM_SIGNALS = [
    (re.compile(r'mass.battle|provincial', re.I), 'mass_battle'),
    (re.compile(r'social.contest', re.I), 'social_contest'),
    (re.compile(r'faction|political', re.I), 'faction_political'),
    (re.compile(r'settlement|territory', re.I), 'settlement_territory'),
    (re.compile(r'threadwork|thread.op', re.I), 'threadwork'),
    (re.compile(r'fieldwork|investigation', re.I), 'fieldwork_investigation'),
    (re.compile(r'key.substrate|module.contract|architecture', re.I), 'architecture'),
    (re.compile(r'combat|weapon|armour|armor', re.I), 'personal_combat'),
]

VERDICT_LINE_RE = re.compile(
    r'(?:VERDICT|GRAPH VERDICT|Verdict)\s*:\s*\**\s*([A-Za-z_/\- ]+)', re.I)
KNOWN_VERDICTS = {'PASS', 'FAIL', 'PARTIAL', 'CONFORMANT', 'NON_CONFORMANT',
                  'NON-CONFORMANT', 'OPEN', 'MIXED', 'CLOSED'}


def _entry_paths():
    """Yield (name, [content-bearing file paths]) for every dated entry —
    both directories and flat .md files — directly under designs/audit/."""
    for name in sorted(os.listdir(AUDIT_DIR)):
        full = os.path.join(AUDIT_DIR, name)
        if os.path.isdir(full):
            files = []
            for root, dirs, fnames in os.walk(full):
                dirs.sort()
                for fn in sorted(fnames):
                    if fn.endswith(('.md', '.json')):
                        files.append(os.path.join(root, fn))
            yield name, full, files
        elif name.endswith('.md'):
            yield name, full, [full]


def _classify_audit_type(name, texts):
    # Name first — the strongest, least-noisy signal (a whole folder's concatenated
    # content pulls in incidental cross-references to unrelated systems). Only fall
    # back to scanning individual files, one at a time, if the name alone is silent —
    # and even then, the FIRST file to give a hit wins rather than a merged blob, so
    # one tangential mention deep in an unrelated file can't hijack classification.
    for pattern, audit_type in AUDIT_TYPE_SIGNALS:
        if pattern.search(name):
            return audit_type
    for text in texts:
        for pattern, audit_type in AUDIT_TYPE_SIGNALS:
            if pattern.search(text):
                return audit_type
    return None


def _classify_subsystem(name, texts):
    # Name-only, deliberately — folder content frequently cross-references other
    # subsystems in passing, which made content-based matching produce false
    # ambiguity (2+ keyword hits) on almost every entry during testing. A name that
    # doesn't disclose its subsystem falls back to cross_cutting in the caller
    # (an honest "spans or unclear", not a guess), rather than mining prose for it.
    hits = {subsystem for pattern, subsystem in SUBSYSTEM_SIGNALS if pattern.search(name)}
    if len(hits) == 1:
        return next(iter(hits))
    return None


def _find_verdict(texts):
    for text in texts:
        for m in VERDICT_LINE_RE.finditer(text):
            parts = m.group(1).strip().split()
            if not parts:
                continue
            token = parts[0].upper().replace('-', '_')
            if token in KNOWN_VERDICTS:
                return token
    return None


def main():
    if not os.path.isdir(AUDIT_DIR):
        print(f"ERROR: {AUDIT_DIR} not found", file=sys.stderr)
        sys.exit(1)

    written, skipped = 0, 0
    out_lines = []

    for name, full_path, files in _entry_paths():
        date_match = DATE_RE.match(name)
        if not date_match:
            print(f"SKIP (no leading date): {name}", file=sys.stderr)
            skipped += 1
            continue
        date, slug = date_match.groups()
        slug = slug[:-3] if slug.endswith('.md') else slug

        texts = []
        for fp in files:
            try:
                with open(fp, encoding='utf-8', errors='replace') as f:
                    texts.append(f.read())
            except OSError:
                continue

        audit_type = _classify_audit_type(name, texts)
        if not audit_type:
            print(f"SKIP (no audit_type signal): {name}", file=sys.stderr)
            skipped += 1
            continue

        verdict = _find_verdict(texts)
        if not verdict:
            print(f"SKIP (no verdict token found): {name}", file=sys.stderr)
            skipped += 1
            continue

        subsystem = _classify_subsystem(name, texts) or 'cross_cutting'
        rel_folder = full_path.replace(os.sep, '/')
        if os.path.isdir(full_path):
            rel_folder += '/'

        record = {
            'id': f"{slug}-{date}",
            'schema_version': 1,
            'audit_type': audit_type,
            'subsystem': subsystem,
            'skill': 'backfill',
            'date': date,
            'folder': rel_folder,
            'scope': slug.replace('-', ' '),
            'verdict': verdict,
            'verdict_detail': '',
            'confidence': 'inferred',
        }
        out_lines.append(json.dumps(record, ensure_ascii=False))
        written += 1

    if out_lines:
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        with open(OUT, 'a', encoding='utf-8') as f:
            for line in out_lines:
                f.write(line + '\n')

    print(f"\nBackfill complete: {written} written, {skipped} skipped (ambiguous/no signal).", file=sys.stderr)
    print(f"Review {OUT} by hand before committing.", file=sys.stderr)


if __name__ == '__main__':
    main()
