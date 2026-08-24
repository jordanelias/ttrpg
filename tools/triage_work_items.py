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
# ── The three-way split (Jordan, 2026-08-24: "We keep unbuilt mechanic proposal items.") ──
#
# The population is NOT doc-versus-code. It is three kinds, and conflating the middle one with the
# first is what made the first version of this classifier cull the settlement/faction design
# backlog:
#
#   DOC-DEFECT  the complaint is about a DOCUMENT — two docs disagree, a section contradicts
#               another, wording, stale duplication, an unmarked supersession. Actioning it edits
#               prose and changes no behaviour.  -> NOT A WORK ITEM
#   PROPOSAL    an unbuilt game mechanic someone authored. It concerns no code TODAY only because
#               that code does not exist yet.     -> KEPT (Jordan, explicitly)
#   CODE        a defect or gap in code that runs. -> KEPT
#
# ⚠ `§` IS NOT A DOC-DEFECT SIGNAL, and assuming it was is a recorded mis-cull. **ED-IN-0004** —
# *"Articulation §3.1 trigger ruleset omits scene.battle_concluded"* — cites a section but its
# complaint is that a RULESET omits a trigger, which is `engine/cross_scale/articulation.py`.
# The test is what the complaint is ABOUT, not what it cites. So the signature below requires a
# phrase describing a defect IN PROSE, not merely a reference to prose.
_DOCSUBJ = re.compile(
    r'one doc, two|two contradictory .{0,24}(?:coexist|within)|contradictory ways within|'
    r'\bwording\b|unmarked[- ]superseded|verbatim duplication|stale .{0,20}parallels|'
    r'zero ledger records|dangling citation|needs? naming|\bterminolog\w*\b.{0,40}\brename\b|'
    r'full rename|lore-to-\w+ mapping audit|hygiene batch \(no value drift\)|'
    r'\bunsuperseded\b|spec was silent', re.I)

# An authored proposal for a mechanic that does not exist yet. KEPT.
_PROPOSAL = re.compile(
    r'\bAUTHORED \(|\bGrounding:|\bproposed\b|\bproposal\b|\bFORK\b|needs Jordan|'
    r'design[- ]taste|new subsystem state|promote[- ]ready|\bOPT-\w+\b|\bSE-\d+\b|\bFA-\d+\b',
    re.I)

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
    or the MODULE instead. That vocabulary is derivable rather than guessable, and it is derived
    ONLY from cooked artifacts plus the directory layout: `engine/engine_params/key_types.json`
    (the 55 key type ids), `engine/engine_params/composition.json` (the composition role names) and
    the `systems/<x>/` directory names.

    ⚠ IT DELIBERATELY DOES NOT PARSE `references/module_contracts.yaml`. An earlier draft did, and
    `tests/valoria/test_engine_params_bridge.py::test_no_new_parser_of_an_authored_surface` caught
    it: that registry has ten declared parsers already and the whole point of the ratchet is that
    the eleventh goes through the exporter instead. `composition.json` IS that exporter's output,
    and the module names it does not carry are the `systems/` directory names anyway.
    """
    root = root or ROOT
    ids = set()
    for rel, pick in (
        (('engine', 'engine_params', 'key_types.json'), lambda d: (d.get('types') or {}).keys()),
        (('engine', 'engine_params', 'composition.json'), lambda d: (d.get('roles') or {}).keys()),
    ):
        path = os.path.join(root, *rel)
        if not os.path.exists(path):
            continue
        try:
            for tid in pick(json.load(open(path, encoding='utf-8'))):
                if isinstance(tid, str):
                    ids.add(tid.lower())
        except Exception:
            pass
    systems = os.path.join(root, 'systems')
    if os.path.isdir(systems):
        for name in os.listdir(systems):
            if os.path.isdir(os.path.join(systems, name)) and not name.startswith('_'):
                ids.add(name.lower())
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
    # PROPOSAL is tested BEFORE any doc test: an authored mechanic often cites the design doc it
    # would live in, and letting that path decide would cull the backlog.
    if _PROPOSAL.search(blob):
        return 'PROPOSAL'
    if _DOCSUBJ.search(blob):
        return 'DOC-DEFECT'
    if any(p.endswith('.md') for p in paths):
        return 'REFERENCE-ONLY'
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
    cull = len(buckets['DOC-DEFECT']) + len(buckets['REFERENCE-ONLY'])
    for k in ('CODE', 'PROPOSAL', 'DOC-DEFECT', 'REFERENCE-ONLY', 'UNCLASSIFIED'):
        print(f"  {k:16} {len(buckets[k])}")
    print(f"\n  NOT WORK (doc-defect + reference-only): {cull}")
    print(f"  WORK (code + proposal + unclassified)   : {total - cull}")
    if a.bucket:
        print()
        for rel, e in buckets[a.bucket.upper()]:
            print(f"  {e.get('id','?'):16} {str(e.get('title') or e.get('description',''))[:96]}")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
