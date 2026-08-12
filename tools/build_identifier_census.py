#!/usr/bin/env python3
"""Per-subsystem identifier census: what each design doc NAMES, and whether anything BUILT it.

WHY.

Jordan, 2026-08-04: *"for design docs with identifiers, output a file in each directory containing
the docs in question … and log all of them in yaml or json that explicitly notes what it was
supposed to be used for … so basically create a little flowchart/graph for each system for these
identifiers then compare with understanding of primitives and aliases to see if they have any merit
as being unbuilt or if they're superseded or outmoded."*

The measurement that prompted it: a census of kept `systems/` prose found ~736 identifiers the
engine has never heard of, against ~46 it has. That ratio says most kept design prose describes
things that do not exist in code — but a ratio cannot tell you WHICH of three very different things
each one is, and they have opposite dispositions:

  UNBUILT      a real mechanic, specified, never coded    -> KEEP. this is the backlog, and
                                                             CLAUDE.md §6 already warns that the
                                                             tempting "minimal" cut drops exactly this
  SUPERSEDED   the doc's own Status says something replaced it
  OUTMODED     named nowhere else — not in code, not in a register, not in another doc.
               An identifier nothing references is not a specification, it is a leftover

DELIBERATELY NOT A DELETION TOOL. It emits a per-subsystem inventory and a graph; the disposition
column is EVIDENCE, not a verdict, because the difference between "unbuilt" and "outmoded" is a
design judgement Jordan makes and a scanner cannot. Everything here is checkable: each row carries
where it was found, what referenced it, and why it landed in its bucket.

WHAT COUNTS AS "BUILT". Resolution runs through the primitives the repo actually has, in order:
  1. a Python name (module-level constant, class, function, or dict key) in engine/ or systems/
  2. a key in the typed exports (engine/engine_params/*.json) -- what Godot will read
  3. a Key TYPE in the substrate registry (systems/_architecture/key_type_registry_v30.md)
  (There is deliberately NO alias step here. An earlier version claimed one and its body was
  byte-identical to the plain lookup -- dead code advertising an enforcement that did not exist.
  It was wrong in principle too: `pathres` resolves PATHS, and no path resolution can change an
  IDENTIFIER lookup. Aliases enter this tool only where they belong, in `doc_stems()`.)

Usage:
    python3 tools/build_identifier_census.py                 # write per-subsystem + the roll-up
    python3 tools/build_identifier_census.py --check         # re-derive and diff (exit 1 on drift)
    python3 tools/build_identifier_census.py --subsystem social_contest
"""
from __future__ import annotations

import argparse
import ast
import collections
import glob
import json
import os
import re
import sys

# Primitives (repo root, lane roster, token estimate, ids, Status reader) are
# owned by tools/ci_common.py — plan G7, ED-IN-0159 §8.3. See its module docstring;
# the two lines below are the bootstrap, anchored on THIS file's directory.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402

REPO = ci_common.REPO
sys.path.insert(0, os.path.join(REPO, 'tools'))
import pathres  # noqa: E402
# TABLE PARSER, inlined 2026-08-05. It used to import export_params_constants.parse_file on the
# "one owner" principle (CLAUDE.md §8) — correct at the time, but that tool was RETIRED WITH ITS
# SOURCE when engine/params/ evacuated, so this module ImportError'd on invocation. Deferring to a
# single owner is right until the owner's subject leaves; then the dependency is the defect. ~20
# lines of markdown-table extraction, with no second consumer to drift against.
_TBL_SEP = re.compile(r'^\s*\|[\s:|-]+\|\s*$')
_TBL_HEAD = re.compile(r'^(#{1,6})\s+(.*?)\s*$')


def _cells(line):
    row = line.strip()
    if row.startswith('|'):
        row = row[1:]
    if row.endswith('|'):
        row = row[:-1]
    return [c.strip() for c in row.split('|')]


def parse_tables(text):
    """Every markdown table, tagged with the heading it sits under. Cells verbatim."""
    out, heading, i = [], None, 0
    lines = text.splitlines()
    while i < len(lines):
        line = lines[i]
        m = _TBL_HEAD.match(line)
        if m:
            heading = m.group(2)
            i += 1
            continue
        if line.lstrip().startswith('|') and i + 1 < len(lines) and _TBL_SEP.match(lines[i + 1]):
            header = _cells(line)
            rows, i = [], i + 2
            while i < len(lines) and lines[i].lstrip().startswith('|'):
                rows.append(_cells(lines[i]))
                i += 1
            out.append({'section': heading, 'header': header, 'rows': rows})
            continue
        i += 1
    return out

try:
    import yaml
except ImportError:
    yaml = None

OUT_NAME = '_identifier_census.yaml'
ROLLUP = os.path.join('references', 'identifier_census.json')
SCHEMA_VERSION = 1

# An identifier in prose: snake_case with an underscore, or SCREAMING_CASE. A bare lowercase word
# is English; a bare capitalised word is a sentence start or a proper noun. This is the lesson from
# two failed censuses -- the first matched ALL-CAPS tokens and returned ALDRIC and DISTILLED.
IDENT = re.compile(r'\b([a-z][a-z0-9]*(?:_[a-z0-9]+)+|[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+)\b')

# Prose that is structurally a heading/field name rather than a mechanic. Cheap, and it keeps the
# noise out of the interesting buckets rather than out of the totals.
NOT_A_MECHANIC = {
    'needs_jordan', 'canonical_source', 'canonical_sources', 'restructure_ledger',
    'editorial_ledger', 'patch_register', 'id_reservations', 'module_contracts',
    'coverage_matrix', 'mechanics_index', 'session_log', 'next_free', 'as_of',
    'file_path', 'line_no', 'schema_version', 'table_of_contents',
    # HTML-comment bookkeeping the atomizer stamps into every doc. Not mechanics; they appeared in
    # EVERY subsystem's unresolved list in the first two runs, which is the signature of noise.
    'canonical_sha', 'canonical_tokens', 'canonical_source_sha', 'source_sha',
}

# A token that names a MODULE or PACKAGE the tree contains is a citation, same as a doc stem.
# `cross_scale`, `clock_registry`, `derived_stats` read as unresolved mechanics while being module
# names -- the identifier-level form of the alias defect this whole session keeps re-learning.
_MODULE_NAMES: set[str] = set()


def module_names() -> set[str]:
    global _MODULE_NAMES
    if not _MODULE_NAMES:
        import subprocess
        out = subprocess.run(['git', 'ls-files'], cwd=REPO, capture_output=True, text=True)
        for line in out.stdout.splitlines():
            for part in line.split('/'):
                stem = part.rsplit('.', 1)[0] if '.' in part else part
                if len(stem) > 4:
                    _MODULE_NAMES.add(stem.lower())
    return _MODULE_NAMES

# "supposed to be used for" -- the sentence the identifier appears in, which is the only place the
# doc says what it is FOR. Trimmed, not summarised: a summary here would be authorship.
_SENT_SPLIT = re.compile(r'(?<=[.!?])\s+')


_DOC_STEMS: set[str] = set()


def doc_stems() -> set[str]:
    """Basenames (no extension) of every tracked file — these are CITATIONS, not mechanics.

    The first run reported `derived_stats_v1`, `player_agency_v30`, `combat_design_v1` and
    `phase11_c4_v0` as unresolved mechanics. They are documents. A design doc naming another
    design doc is a cross-reference, and counting it as an unbuilt mechanic inflates the exact
    bucket that costs Jordan attention to adjudicate.
    """
    global _DOC_STEMS
    if not _DOC_STEMS:
        import subprocess
        out = subprocess.run(['git', 'ls-files'], cwd=REPO, capture_output=True, text=True)
        for line in out.stdout.splitlines():
            base = os.path.basename(line)
            stem = base.rsplit('.', 1)[0] if '.' in base else base
            if len(stem) > 4:
                _DOC_STEMS.add(stem.lower())
                # `foo_v30_index` cites `foo_v30`; strip the common doc suffixes too
                for suf in ('_index', '_infill', '_part2', '_part3'):
                    if stem.lower().endswith(suf):
                        _DOC_STEMS.add(stem.lower()[:-len(suf)])

        # RETIRED doc names are still cited -- and after the evacuation slices run, EVERY citation
        # of an evacuated doc would flip from filtered to "unbuilt mechanic" unless the retired
        # spellings are known. The alias map is exactly that list, so the census gets QUIETER as
        # the cut proceeds instead of noisier. (Reviewer's forward hazard; pathres already owns it.)
        exact, prefix = pathres.load_alias_map()
        for old in list(exact) + [o for o, _ in prefix]:
            stem = os.path.basename(old.rstrip('/'))
            stem = stem.rsplit('.', 1)[0] if '.' in stem else stem
            if len(stem) > 4:
                _DOC_STEMS.add(stem.lower())
    return _DOC_STEMS


def subsystems() -> list[str]:
    out = []
    for name in sorted(os.listdir(os.path.join(REPO, 'systems'))):
        d = os.path.join(REPO, 'systems', name)
        if os.path.isdir(d) and glob.glob(os.path.join(d, '*.md')):
            out.append(name)
    return out


# ---------------------------------------------------------------------------------------------
# What the engine actually defines -- the primitives side
# ---------------------------------------------------------------------------------------------
def built_names() -> dict[str, list[str]]:
    """{lowercased identifier: [where it is defined]} across code, typed exports, Key registry."""
    built: dict[str, list[str]] = collections.defaultdict(list)
    # tools/ COUNTS. The reviewer's find: `all_legacy` read UNRESOLVED in _architecture while
    # being defined at tools/names.py:91 -- process/armature docs legitimately name tooling, and
    # excluding tools/ made every such name look like an unbuilt mechanic.
    for root in ('engine', 'systems', 'tools'):
        for path in glob.glob(os.path.join(REPO, root, '**', '*.py'), recursive=True):
            rel = os.path.relpath(path, REPO).replace(os.sep, '/')
            try:
                tree = ast.parse(open(path, encoding='utf-8', errors='ignore').read())
            except (SyntaxError, OSError, UnicodeDecodeError):
                continue
            is_tool = rel.startswith('tools/')
            # module-level bindings only; a nested `x = ...` is a local, not a definition
            toplevel = set()
            for stmt in ast.walk(tree):
                if isinstance(stmt, ast.Module):
                    toplevel.update(id(n) for n in stmt.body)
                elif isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                    toplevel.update(id(n) for n in stmt.body)
            for node in ast.walk(tree):
                names = []
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                    names = [node.name]
                    # PARAMETERS COUNT. `max_bouts` read as UNRESOLVED in the first run while
                    # being a live function parameter -- module-level-only harvesting understates
                    # "built" and inflates the bucket Jordan has to adjudicate.
                    a = getattr(node, 'args', None)
                    if a is not None and not is_tool:   # tool params collide with game vocabulary
                        names += [x.arg for x in
                                  list(a.args) + list(a.posonlyargs) + list(a.kwonlyargs)
                                  + ([a.vararg] if a.vararg else [])
                                  + ([a.kwarg] if a.kwarg else [])]
                elif isinstance(node, ast.Assign):
                    if id(node) not in toplevel:
                        continue                        # a LOCAL binding is not a definition
                    names = [getattr(t, 'id', None) or getattr(t, 'attr', None)
                             for t in node.targets]
                elif isinstance(node, ast.AnnAssign):
                    if id(node) not in toplevel:
                        continue
                    names = [getattr(node.target, 'id', None)]
                elif isinstance(node, ast.Dict):
                    names = [k.value for k in node.keys
                             if isinstance(k, ast.Constant) and isinstance(k.value, str)]
                for n in names:
                    if n and len(n) > 3:
                        built[n.lower()].append(f'py:{rel}')
    for jf in glob.glob(os.path.join(REPO, 'engine', 'engine_params', '*.json')):
        rel = os.path.relpath(jf, REPO).replace(os.sep, '/')
        try:
            doc = json.load(open(jf, encoding='utf-8'))
        except (OSError, ValueError):
            continue

        def walk(o):
            if isinstance(o, dict):
                for k, v in o.items():
                    if isinstance(k, str) and len(k) > 3:
                        built[k.lower()].append(f'typed:{rel}')
                    walk(v)
            elif isinstance(o, list):
                for v in o:
                    walk(v)
        walk(doc)
    # the Key substrate: a type id like `combat.strike` is the primitive an identifier may name
    reg = os.path.join(REPO, 'systems', '_architecture', 'key_type_registry_v30.md')
    if os.path.exists(reg):
        for m in re.finditer(r'^###\s+`?([a-z_]+\.[a-z_]+)`?', open(reg, encoding='utf-8').read(),
                             re.M):
            for part in m.group(1).split('.'):
                built[part.lower()].append('key:key_type_registry_v30.md')
            built[m.group(1).lower()].append('key:key_type_registry_v30.md')
    return {k: sorted(set(v)) for k, v in built.items()}


def doc_status(text: str) -> str | None:
    """ONE OWNER: ci_common.doc_status (plan G8, ED-IN-0159 §1.3a).

    Was `^##\\s*Status:` — EXACTLY two hashes, over the WHOLE document. That is
    both halves of the §1.3a divergence in one line, and the measured delta of
    replacing it is +3 / -1, with ZERO change to any doc's SUPERSEDED
    classification (which is what this function actually gates, at :348):

      GAINED  engine/sim_reference_CONVENTIONS.md      (bare `Status:`)
      GAINED  references/restructure_ledger.md         (`# Status:`, one hash)
      GAINED  systems/combat/combat_engine_v1/README.md (bare `Status:`)
      LOST    godot/godot_architecture_specification.md

    The loss is a FIX, not a regression: that file's `## Status:` line reads
    "NOT STARTED / IN PROGRESS / COMPLETE" — a legend, past the head window, not
    a status. Scanning the whole document is what made it visible.

    The window matters more than the regex here and was chosen by measurement,
    not inheritance. At the whole document this function newly reads
    `  status : IN_FORCE | VETOED | SUPERSEDED` — a schema TEMPLATE inside an
    audit doc — and would flip a live document to SUPERSEDED. At a 12-line
    window, two genuinely-superseded docs stop being recognised. 40 and 80 give
    the same answer; ci_common.STATUS_HEAD_LINES is 80.
    """
    return ci_common.doc_status(text)


def table_purposes(text: str) -> dict[str, str]:
    """{identifier: the WHOLE TABLE ROW it appears in}, with its section and column headers.

    SCAN ROWS, NOT SENTENCES (Jordan, 2026-08-04: "we need to be thorough in scanning rows etc").
    Design docs put mechanics in tables, and a table row IS the statement of what an identifier is
    for -- name, value, unit, caveat, all in one row. A sentence-based scan sees `| kite_penalty |
    -2 | per zone | if unbraced |` as a line of pipes and reports the first fragment containing
    the token, throwing away the columns that carry the meaning. Row + headers + section is the
    doc's own answer to "what was this supposed to be used for", quoted rather than summarised.
    """
    out: dict[str, str] = {}
    for tbl in parse_tables(text):
        hdr = ' | '.join(c for c in tbl['header'] if c)
        for row in tbl['rows']:
            joined = ' | '.join(row)
            for cell in row:
                for m in IDENT.finditer(cell):
                    key = m.group(1).lower()
                    if key not in out:
                        ctx = f"[{tbl['section']}] {hdr} :: {joined}" if tbl['section'] else \
                              f"{hdr} :: {joined}"
                        out[key] = ' '.join(ctx.split())[:400]
    return out


def purpose_for(ident: str, text: str) -> str | None:
    """The sentence the identifier first appears in — the doc's own statement of what it is FOR.

    Quoted verbatim and trimmed. Summarising would be authorship, which is the fabrication this
    repo forbids; a reviewer needs the doc's words, not mine. Table rows take precedence (see
    `table_purposes`); this is the fallback for identifiers that live in prose.
    """
    for line in text.splitlines():
        if ident in line:
            stripped = line.strip().lstrip('|#*->_ ').strip()
            if not stripped:
                continue
            for sent in _SENT_SPLIT.split(stripped):
                if ident in sent:
                    s = ' '.join(sent.split())
                    return s[:300] + ('…' if len(s) > 300 else '')
    return None


def census_for(sub: str, built: dict) -> dict:
    docs = sorted(glob.glob(os.path.join(REPO, 'systems', sub, '*.md')))
    rows: dict[str, dict] = {}
    dropped: dict[str, str] = {}
    for path in docs:
        rel = os.path.relpath(path, REPO).replace(os.sep, '/')
        text = open(path, encoding='utf-8', errors='ignore').read()
        rowctx = table_purposes(text)          # rows first — they carry the meaning
        # A TOKEN THE DOC ITSELF SPELLS WITH `.md` IS A CITATION, whatever the filesystem says.
        # The reviewer's named falsifiers (threadwork <=3, victory <=2) still failed after the
        # alias-map pass, and reading the 12 survivors showed why: every one cites a doc that no
        # longer exists AND is not in the alias map (batch_d_designs.md, mass_battle_v3.md,
        # opus_design_proposal). A filesystem lookup cannot see those. The text can -- and being a
        # CONTENT signal rather than a lookup, it keeps working after the evacuation slices run,
        # which is when the lookup-based filters get weakest.
        cited_docs = {m.group(1).lower()
                      for m in re.finditer(r'([A-Za-z0-9_.-]+)\.md\b', text)}
        status = doc_status(text)
        superseded = bool(status and 'SUPERSEDED' in status.upper()
                          and 'PART' not in status.upper())
        for m in IDENT.finditer(text):
            ident = m.group(1)
            key = ident.lower()
            if key in NOT_A_MECHANIC or len(key) < 5:
                dropped.setdefault(key, 'boilerplate-or-too-short')
                continue
            if key in cited_docs:                            # the doc spells it with .md
                dropped.setdefault(key, 'the doc spells it as <name>.md — a citation')
                continue
            if key in doc_stems():
                dropped.setdefault(key, 'matches a tracked/aliased document stem')
                continue
            if key in module_names():
                dropped.setdefault(key, 'matches a module or path component')
                continue
            row = rows.setdefault(key, {
                'identifier': ident, 'docs': [], 'purpose': None,
                'built_in': [], 'disposition': None, 'doc_status': None, 'in_table': False,
            })
            if rel not in row['docs']:
                row['docs'].append(rel)
            if row['purpose'] is None:
                row['purpose'] = rowctx.get(key) or purpose_for(ident, text)
            if key in rowctx and not row.get('in_table'):
                row['in_table'] = True
            if superseded and row['doc_status'] is None:
                row['doc_status'] = status[:120]
    for key, row in rows.items():
        where = built.get(key, [])
        row['built_in'] = where
        if where:
            row['disposition'] = 'BUILT'
        elif row['doc_status']:
            row['disposition'] = 'SUPERSEDED-DOC'
        else:
            row['disposition'] = 'UNRESOLVED'   # unbuilt-or-outmoded: JORDAN'S CALL, not mine
    return {
        '_generated': (
            'GENERATED by tools/build_identifier_census.py. NEVER hand-edit: re-run the tool. '
            'Every identifier named in this subsystem\'s design docs, with the sentence the doc '
            'uses it in and whether anything in engine/ or systems/ defines it. '
            'KNOWN LIMITS, so this file is not read as more than it is. (1) BUILT is a NAME '
            'match, not a wiring proof: it means something in engine/systems/tools defines that '
            'name, which for a common word can be a collision -- read `built_in` before trusting '
            'a BUILT row. (2) Identifiers shorter than 5 chars, and any not written in snake_case '
            'or SCREAMING_CASE, are INVISIBLE here -- victory_v30 s WC/WR/MS tracks do not appear '
            'at all, so an empty census is NOT evidence a subsystem has nothing unbuilt. '
            '(3) Parameters of one mechanic are separate rows, so the count overstates DISTINCT '
            'design decisions by roughly 2-3x. (4) `dropped_as_not_a_mechanic` lists every token '
            'filtered out and why -- read it before concluding something is missing. '
            'DISPOSITION IS EVIDENCE, NOT A VERDICT: UNRESOLVED means "no definition found", '
            'which is UNBUILT (keep — this is the backlog, CLAUDE.md §6) or OUTMODED (cut) '
            'depending on design intent a scanner cannot read.'),
        'schema_version': SCHEMA_VERSION,
        'subsystem': sub,
        'docs': [os.path.relpath(d, REPO).replace(os.sep, '/') for d in docs],
        'counts': collections.Counter(r['disposition'] for r in rows.values()),
        'identifiers': {k: rows[k] for k in sorted(rows)},
        # AUDIT TRAIL. Silent filtering is how a subsystem's whole mechanic set disappeared
        # without leaving a row anyone could disagree with. Every drop, with its reason.
        'dropped_as_not_a_mechanic': {k: dropped[k] for k in sorted(dropped)},
    }


def _dump(doc: dict) -> str:
    d = dict(doc)
    d['counts'] = dict(d['counts'])
    if yaml is None:
        return json.dumps(d, indent=1, sort_keys=False) + '\n'
    return yaml.safe_dump(d, sort_keys=False, allow_unicode=True, width=1000)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--subsystem')
    args = ap.parse_args(argv)

    built = built_names()
    subs = [args.subsystem] if args.subsystem else subsystems()
    rollup, drift = {}, []
    for sub in subs:
        doc = census_for(sub, built)
        text = _dump(doc)
        out = os.path.join(REPO, 'systems', sub, OUT_NAME)
        if args.check:
            if not os.path.exists(out) or open(out, encoding='utf-8').read() != text:
                drift.append(f'systems/{sub}/{OUT_NAME}')
        else:
            with open(out, 'w', encoding='utf-8') as fh:
                fh.write(text)
        rollup[sub] = dict(doc['counts'])
        rollup[sub]['docs'] = len(doc['docs'])
        rollup[sub]['identifiers'] = len(doc['identifiers'])

    if args.check:
        if drift:
            print(f'[identifier-census] DRIFT in {len(drift)} file(s): {drift[:5]}')
            return 1
        print(f'[identifier-census] OK — {len(subs)} subsystem(s) current')
        return 0

    with open(os.path.join(REPO, ROLLUP), 'w', encoding='utf-8') as fh:
        fh.write(json.dumps({'_generated': 'GENERATED by tools/build_identifier_census.py',
                             'schema_version': SCHEMA_VERSION,
                             'engine_names': len(built),
                             'by_subsystem': rollup}, indent=1, sort_keys=True) + '\n')
    tot = collections.Counter()
    for sub, c in rollup.items():
        for k in ('BUILT', 'SUPERSEDED-DOC', 'UNRESOLVED'):
            tot[k] += c.get(k, 0)
    print(f'[identifier-census] {len(subs)} subsystem(s), {len(built)} engine-defined names')
    print(f'    BUILT           {tot["BUILT"]:5d}   named in prose AND defined in code/typed/Keys')
    print(f'    SUPERSEDED-DOC  {tot["SUPERSEDED-DOC"]:5d}   only in a doc whose own Status says superseded')
    print(f'    UNRESOLVED      {tot["UNRESOLVED"]:5d}   no definition found — UNBUILT or OUTMODED (Jordan\'s call)')
    print(f'    -> systems/<sub>/{OUT_NAME} + {ROLLUP}')
    for sub in sorted(rollup, key=lambda s: -rollup[s].get('UNRESOLVED', 0))[:12]:
        c = rollup[sub]
        print(f'      {c.get("UNRESOLVED",0):5d} unresolved / {c["identifiers"]:5d} total   '
              f'{sub}  ({c["docs"]} doc(s))')
    return 0


if __name__ == '__main__':
    sys.exit(main())
