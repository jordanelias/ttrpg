#!/usr/bin/env python3
"""
triage_work_items.py — classify editorial-ledger work items by whether they concern CODE.

WHY THIS EXISTS (Jordan, 2026-08-24)
------------------------------------
    "Our first work is to triage all work items that specifically concern reference-only
     design documents then cull those items. If the work item doesn't concern code, then
     it isn't a work item."

That follows from CLAUDE.md §0.05: code is the mechanism, `.md` design documents are
reference. A ledger row whose entire subject is a document's text — two docs disagreeing,
a §-section contradicting another, a wording fix, an unmarked supersession — describes a
defect in REFERENCE. It cannot change how the game resolves, so it is not work.

THE CLASSIFIER IS CODE, NOT A JUDGEMENT CALL, so the cull is reproducible and challengeable.
Three buckets:

  CODE            the row names a `.py`/`.gd` file, OR a data file that code actually reads,
                  OR an `.md` that code actually reads (those are inputs, not reference), OR
                  it carries code-shaped signals (`engine/`, `systems/<sub>/sim`, a resolver,
                  a golden, a CI job, an exporter).
  REFERENCE-ONLY  the row names `.md` paths and nothing else.
  DOC-SUBJECT     the row names no path, and its complaint is about a document's text,
                  sections or internal consistency.

Anything left is UNCLASSIFIED and is KEPT — the default is to keep, because mis-culling a
behavioural question is worse than carrying a dead row.

⚠ THE MACHINE-READ SET IS DERIVED FROM CODE, NEVER HARDCODED. `machine_read_inputs()` scans
`tools/`, `engine/`, `systems/`, `skills/` for filenames used in a read context. That matters:
`systems/_architecture/key_type_registry_v30.md` IS an input (the Key-type schema is authored
in markdown), so rows about it are CODE, not reference — a hardcoded "all .md are reference"
rule would have culled the schema of the Key bus.

USAGE
    python3 tools/triage_work_items.py                 # report the split
    python3 tools/triage_work_items.py --list CODE     # list one bucket
    python3 tools/triage_work_items.py --json          # machine-readable
"""
import argparse
import collections
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402
import validate_ed_citations as V  # noqa: E402

ROOT = ci_common.REPO if hasattr(ci_common, 'REPO') else os.getcwd()

_PATH = re.compile(r'[A-Za-z0-9_./-]+\.(?:py|gd|ya?ml|jsonl?|md)')
_READ_CTX = re.compile(r'open\(|read_text|_read\(|safe_load|json\.load|finditer|findall|Path\(|glob')
_CODEISH = re.compile(
    r'\bengine/|\bsystems/\w+/sim\b|\bresolver\b|\bgolden\b|\btest_\w+|\bCI job\b|\bexporter\b|'
    r'\bdef \w+|\bclass \w+|\.py\b|\bimport \b')
# The complaint is about a document's TEXT rather than a behaviour.
_DOCSUBJ = re.compile(
    r'§|\bwording\b|\bdocs?\b|document|\bmaster\b|spec was silent|unsuperseded|\bunmarked\b|'
    r'duplication|\bprose\b|needs? naming|terminolog|\brename\b|canonical doc|one doc, two|'
    r'zero ledger records|stale .*parallels|\bdangling\b', re.I)

_TEXT_FIELDS = ('title', 'description', 'system', 'source', 'falsifier',
                'provenance', 'measured_by', 'files_to_recheck')


def code_identifiers(root=None):
    """Key-type ids and registered module names — CODE IDENTIFIERS, not prose.

    ⚠ ADDED AFTER A MIS-CULL, and the miss is the reason this function exists rather than a wider
    regex. The first classifier struck **ED-IN-0014** — *"Key the silent emitters: settlement_layer
    + ci_political + victory era/occupation transitions"* — and **ED-IN-0004**, about the
    articulation trigger ruleset omitting `scene.battle_concluded`. Both are squarely about code:
    the first IS the hub-and-bus gap (subsystems that emit no Keys), the second is
    `engine/cross_scale/articulation.py`'s trigger set. They were culled because they name `.md`
    paths and none of `_CODEISH`'s file-shaped patterns.

    A work item can be entirely about code while naming no filename at all — it names the KEY TYPE
    or the MODULE instead. Those live in `key_types.json` and `module_contracts.yaml`, both
    machine-read, so the vocabulary is derivable rather than guessable.
    """
    root = root or ROOT
    ids = set()
    kt = os.path.join(root, 'engine', 'engine_params', 'key_types.json')
    if os.path.exists(kt):
        try:
            data = json.load(open(kt, encoding='utf-8'))
            for t in (data.get('types') or data.get('key_types') or data):
                tid = t.get('id') if isinstance(t, dict) else t
                if isinstance(tid, str) and '.' in tid:
                    ids.add(tid.lower())
        except Exception:
            pass
    mc = os.path.join(root, 'references', 'module_contracts.yaml')
    if os.path.exists(mc):
        try:
            import yaml
            for m in (yaml.safe_load(open(mc, encoding='utf-8')) or {}).get('modules', []):
                if m.get('module'):
                    ids.add(str(m['module']).lower())
                for side in ('emits', 'consumes'):
                    for x in (m.get(side) or []):
                        t = x.get('type') if isinstance(x, dict) else x
                        if isinstance(t, str) and '.' in t:
                            ids.add(t.lower())
        except Exception:
            pass
    return {i for i in ids if len(i) > 4}


def machine_read_inputs(root=None):
    """{basename} of every non-.py file that code opens/parses. Derived, never listed."""
    root = root or ROOT
    found = set()
    for sub in ('tools', 'engine', 'systems', 'skills'):
        base = os.path.join(root, sub)
        for dirpath, _dirs, files in os.walk(base):
            if '__pycache__' in dirpath:
                continue
            for fn in files:
                if not fn.endswith('.py'):
                    continue
                try:
                    txt = open(os.path.join(dirpath, fn), encoding='utf-8', errors='replace').read()
                except OSError:
                    continue
                for m in re.finditer(r'["\']([A-Za-z0-9_./-]+\.(?:ya?ml|json|jsonl|md))["\']', txt):
                    if _READ_CTX.search(txt[max(0, m.start() - 200):m.start() + 120]):
                        found.add(os.path.basename(m.group(1)))
    return found


def work_items(root=None):
    """(file, entry) for every ledger id whose EFFECTIVE (last) row is unresolved or needs_jordan."""
    root = root or ROOT
    last = {}
    for f in sorted(glob.glob(os.path.join(root, 'registers', 'editorial_ledger*.jsonl'))):
        rel = os.path.relpath(f, root).replace(os.sep, '/')
        for line in open(f, encoding='utf-8'):
            line = line.strip()
            if not line:
                continue
            try:
                e = json.loads(line)
            except ValueError:
                continue
            if e.get('id'):
                last[e['id']] = (rel, e)
    return [(rel, e) for rel, e in last.values()
            if not V._is_resolved(e.get('status', '')) or e.get('needs_jordan')]


def _live(path, root=None):
    """Does this path point at anything — on disk, or through the restructure ledger?

    A path under an evacuated tree (`designs/audit/...`) is DEAD and is evidence of nothing.
    Counting it as evidence was a real defect in the first version of this classifier: five rows
    whose complaint was explicitly about a document's §-sections were held out of DOC-SUBJECT
    because they happened to name a dead `.jsonl` alongside, and a `not paths` guard then blocked
    the text test. A dead pointer must not be able to rescue a row from classification.
    """
    root = root or ROOT
    if os.path.exists(os.path.join(root, path)):
        return True
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import pathres
        return pathres.resolve(path).status != 'DEAD'
    except Exception:
        return False


def classify(entry, machine_read, code_ids=None):
    blob = ' '.join(str(entry.get(k, '')) for k in _TEXT_FIELDS)
    paths = {p for p in _PATH.findall(blob) if _live(p)}
    if any(p.endswith(('.py', '.gd')) for p in paths):
        return 'CODE'
    if any(os.path.basename(p) in machine_read for p in paths):
        return 'CODE'
    if _CODEISH.search(blob):
        return 'CODE'
    low = blob.lower()
    if any(cid in low for cid in (code_ids if code_ids is not None else code_identifiers())):
        return 'CODE'
    if any(p.endswith('.md') for p in paths):
        return 'REFERENCE-ONLY'
    # NOT gated on `paths` being empty: a row may name a dead or non-code path and still be, in
    # substance, a complaint about a document's text.
    if _DOCSUBJ.search(blob):
        return 'DOC-SUBJECT'
    return 'UNCLASSIFIED'


def triage(root=None):
    mr = machine_read_inputs(root)
    cids = code_identifiers(root)
    out = collections.defaultdict(list)
    for rel, e in work_items(root):
        out[classify(e, mr, cids)].append((rel, e))
    return out, mr


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[1])
    ap.add_argument('--list', dest='bucket')
    ap.add_argument('--json', action='store_true')
    a = ap.parse_args(argv)
    buckets, mr = triage()
    if a.json:
        print(json.dumps({k: [[r, e] for r, e in v] for k, v in buckets.items()}, indent=1))
        return 0
    total = sum(len(v) for v in buckets.values())
    print(f"work items (effective status unresolved or needs_jordan): {total}")
    print(f"machine-read non-.py inputs discovered from code: {len(mr)}")
    cull = len(buckets['REFERENCE-ONLY']) + len(buckets['DOC-SUBJECT'])
    for k in ('CODE', 'REFERENCE-ONLY', 'DOC-SUBJECT', 'UNCLASSIFIED'):
        print(f"  {k:16} {len(buckets[k])}")
    print(f"\n  NOT WORK (reference-only + doc-subject): {cull}")
    print(f"  WORK (code + unclassified, kept)       : {total - cull}")
    if a.bucket:
        print()
        for rel, e in buckets[a.bucket.upper()]:
            print(f"  {e.get('id','?'):16} {str(e.get('title') or e.get('description',''))[:96]}")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
