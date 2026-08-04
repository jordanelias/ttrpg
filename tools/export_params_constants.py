#!/usr/bin/env python3
"""Dump the `engine/params/*.md` tables to YAML so the prose can leave.

WHY.

`engine/params/` is 43 markdown files of parameter tables. Jordan, 2026-08-04: *"params .md are
largely useless at this point and I want them gone. code should have superseded them all by now"*
and *"just dump the constants to a yaml"*. Under the format rule — Python for logic, JSON for data,
YAML for registries, `.md` only for canon narrative / systems reference / specs of unbuilt systems —
a parameter table is data wearing prose, and it is the last big data-in-prose surface in the tree.

WHAT THE MEASUREMENT ACTUALLY SUPPORTED, stated because it is weaker than it first looked. A census
matched ALL-CAPS identifiers in the tables against the typed layer (`sim_params.json`,
`combat_engine_v1.json`) and the Python: 295 of 378 "found". That 78% is an OPTIMISTIC UPPER BOUND
and the residue was noise — reading the 61 "orphans" showed them to be capitalised prose
(`ALIGNMENT`, `CORRECTIONS`, `DISTILLED`), HTML-comment markers (`PATCHES APPLIED`, `AUD1`), and
character names (`ALDRIC`, `MARET`). A name appearing in code also never proved its VALUE matched.
So the census could not settle whether every number is superseded, and this tool does not rely on it
having done so: it captures the tables verbatim instead of trusting that nothing is lost.

THE POINT OF THIS TOOL is therefore NOT to decide what is canonical. It is to make the prose
*deletable* by preserving, in a machine-readable form, everything the tables assert — so the `.md`
can go to the fork and any value that turns out to matter is still reachable without reading
markdown. Provenance citations that name `engine/params/...` may cite the fork (Jordan, 2026-08-04),
so they do not block the deletion either.

WHAT IT DOES NOT DO. It does not invent a schema. These tables have no consistent one — column
counts, header names and units vary per file, and several carry parenthetical caveats inside cells
("minimum 5", "×2 if braced"). Imposing a typed schema here would mean *deciding* what each row
means, which is authorship, not extraction, and would be exactly the fabrication the repo forbids.
So the dump is structural and faithful: file -> section heading -> table (header row + data rows),
cells verbatim. Anything further is a later, deliberate typing pass with its own review.

Usage:
    python3 tools/export_params_constants.py           # write engine/engine_params/params_tables.yaml
    python3 tools/export_params_constants.py --check   # re-derive and diff (exit 1 on drift)
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys

try:
    import yaml
except ImportError:
    print("[params-dump] pyyaml required", file=sys.stderr)
    raise SystemExit(2)

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_GLOB = 'engine/params/**/*.md'
OUT = os.path.join('engine', 'engine_params', 'params_tables.yaml')
SCHEMA_VERSION = 1

_HEADING = re.compile(r'^(#{1,6})\s+(.*?)\s*$')
_SEP = re.compile(r'^\s*\|[\s:|-]+\|\s*$')      # the |---|---| separator row


def _cells(line: str) -> list[str]:
    row = line.strip()
    if row.startswith('|'):
        row = row[1:]
    if row.endswith('|'):
        row = row[:-1]
    return [c.strip() for c in row.split('|')]


def parse_file(path: str) -> list[dict]:
    """Every markdown table, tagged with the heading it sits under. Cells verbatim."""
    out, heading, i = [], None, 0
    lines = open(os.path.join(REPO, path), encoding='utf-8', errors='ignore').read().splitlines()
    while i < len(lines):
        line = lines[i]
        m = _HEADING.match(line)
        if m:
            heading = m.group(2)
            i += 1
            continue
        # a table is: a pipe row, then a separator row, then pipe rows
        if line.lstrip().startswith('|') and i + 1 < len(lines) and _SEP.match(lines[i + 1]):
            header = _cells(line)
            rows, i = [], i + 2
            while i < len(lines) and lines[i].lstrip().startswith('|'):
                rows.append(_cells(lines[i]))
                i += 1
            out.append({'section': heading, 'header': header, 'rows': rows})
            continue
        i += 1
    return out


def build() -> dict:
    files = sorted(glob.glob(os.path.join(REPO, SRC_GLOB), recursive=True))
    tables, n_tables, n_rows, raw = {}, 0, 0, {}
    for full in files:
        rel = os.path.relpath(full, REPO).replace(os.sep, '/')
        # LOSSLESS BY CONSTRUCTION. The structured tables below are the useful view, but a
        # deletion must not depend on my parser being complete — and it is not: six files
        # (index stubs, history/) yield no table at all, and a cell caveat my regex mishandles
        # would vanish silently. So every file's full text is captured verbatim too. Proving a
        # parser total is harder than storing the source, and the cost here is ~580 KB.
        raw[rel] = open(full, encoding='utf-8', errors='ignore').read()
        t = parse_file(rel)
        if not t:
            continue
        tables[rel] = t
        n_tables += len(t)
        n_rows += sum(len(x['rows']) for x in t)
    if not tables:
        raise SystemExit(f"[params-dump] no tables parsed from {SRC_GLOB} — refusing to write an empty dump")
    return {
        '_generated': (
            'GENERATED by tools/export_params_constants.py from engine/params/**/*.md. '
            'NEVER hand-edit: re-run the tool. This is a FAITHFUL STRUCTURAL CAPTURE of the '
            'parameter tables (cells verbatim), not a typed schema and not a canonicity ruling — '
            'it exists so the source markdown can be evacuated without losing what it asserted. '
            'Where a value here disagrees with code, THE CODE WINS (principle 7 / ED-1050).'),
        'schema_version': SCHEMA_VERSION,
        'source_glob': SRC_GLOB,
        'file_count': len(tables),
        'table_count': n_tables,
        'row_count': n_rows,
        'raw_file_count': len(raw),
        'tables': tables,
        'raw': raw,
    }


def _serialise(doc: dict) -> str:
    return yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=1000)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args(argv)
    doc = build()
    text = _serialise(doc)
    out = os.path.join(REPO, OUT)

    if args.check:
        if not os.path.exists(out):
            print(f"[params-dump] MISSING: {OUT} — run the exporter")
            return 1
        if open(out, encoding='utf-8').read() != text:
            print(f"[params-dump] DRIFT: {OUT} does not match a fresh dump of {SRC_GLOB}")
            return 1
        print(f"[params-dump] OK — {doc['file_count']} files, {doc['table_count']} tables, "
              f"{doc['row_count']} rows")
        return 0

    with open(out, 'w', encoding='utf-8') as fh:
        fh.write(text)
    print(f"[params-dump] wrote {OUT} — {doc['file_count']} files, {doc['table_count']} tables, "
          f"{doc['row_count']} rows")
    return 0


if __name__ == '__main__':
    sys.exit(main())
