#!/usr/bin/env python3
"""connectivity_matrix.py — throughlines across engine/ + systems/ by shared vocabulary.

WHY THIS EXISTS (Jordan, 2026-08-11): "restrict yourself to code (.py files) contained within
engine and subsystems … grep/regex/patternmatch to create document sets by term/value/name, which
you can then use to create a comprehensive throughlines/connectivity matrix."

The point is that it sees what an import graph cannot. Three prior passes in this session failed on
exactly that blind spot:

  * an AST import graph called `combat_engine_v1.wrapper` an orphan — its siblings import bare, so
    the resolver could not dot-qualify them;
  * an `import X` grep called four factions modules uncalled — `test_pipeline_reach.py` dispatches
    them by STRING module path;
  * both were blind in the SAME direction, which is why their agreement carried no information.

Shared vocabulary is a different observable. Two modules that both speak `morale_delta` are coupled
whether or not either imports the other, and a term DEFINED in two places is a competing-owner
candidate whether or not the definitions are textually similar. That is the union of the two
diseases this repo has: `tools/` duplicates text, `systems/` diverges in idiom.

WHAT IT EMITS
  1. DEFINITION COLLISIONS — one term, module-level definitions in >1 file. The consolidation
     candidates. Split by whether the values agree, because that decides whether folding them is a
     cleanup or a behaviour change.
  2. CROSS-SUBSYSTEM THROUGHLINES — a term defined in subsystem A and used in subsystem B.
  3. HIDDEN COUPLING — the subset of (2) where B has no import path to A. Vocabulary coupling no
     import expresses; invisible to every prior instrument.
  4. SUBSYSTEM x SUBSYSTEM matrix — shared-term counts.

WHAT IT DOES NOT CLAIM. Shared vocabulary is evidence of coupling, not proof of a call. A term can
collide by coincidence (`SCALE`, `MAX`), so §1 is reported with values and §3 is ranked, never
auto-actioned. It measures the declared surface of the code, not its behaviour — for behavioural
deadness the instrument is `harness.py` (00_code_leanness.md §1.11), which is strictly better and
still unrun.

Read-only. Writes nothing. Run:  python3 connectivity_matrix.py [--full]
"""
import ast
import collections
import os
import re
import subprocess
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
SELF = 'audit/2026-08-11-code-leanness/connectivity_matrix.py'

# Terms this common carry no coupling signal — they are Python or arithmetic, not domain vocabulary.
STOP = {
    'self', 'cls', 'name', 'value', 'values', 'items', 'keys', 'data', 'result', 'results',
    'total', 'count', 'index', 'key', 'type', 'kind', 'state', 'main', 'test', 'run', 'get',
    'set', 'add', 'new', 'old', 'max', 'min', 'sum', 'all', 'any', 'none', 'true', 'false',
    'args', 'kwargs', 'path', 'file', 'line', 'text', 'json', 'yaml', 'dict', 'list', 'str',
    'int', 'float', 'bool', 'seed', 'rng', 'out', 'src', 'dst', 'tmp', 'obj', 'ctx', 'cfg',
    # bare-callable builtins and stdlib verbs that are not domain vocabulary
    'append', 'clear', 'strip', 'load', 'loads', 'dump', 'dumps', 'open', 'print', 'range',
    'len', 'sorted', 'enumerate', 'zip', 'map', 'filter', 'format', 'join', 'split', 'copy',
    'deepcopy', 'round', 'abs', 'isinstance', 'getattr', 'setattr', 'hasattr', 'super',
    'lookup', 'emit', 'apply', 'check', 'probe', 'reset', 'build', 'render', 'update',
}


def git_ls(*pats):
    out = subprocess.run(['git', 'ls-files', *pats], cwd=REPO,
                         capture_output=True, text=True).stdout.split()
    return [p for p in out if p != SELF]


def subsystem_of(rel):
    """`systems/combat/sim/x.py` -> 'combat'; `engine/autoload/y.py` -> 'engine.autoload'."""
    parts = rel.split('/')
    if parts[0] == 'systems' and len(parts) > 2:
        return parts[1]
    if parts[0] == 'engine':
        return 'engine.' + parts[1] if len(parts) > 2 else 'engine'
    return parts[0]


DEF_CONST = re.compile(r'^([A-Z][A-Z0-9_]{2,})\s*(?::[^=]+)?=\s*(.+?)\s*(?:#.*)?$', re.M)
QUOTED = re.compile(r'["\']([a-z][a-z0-9_]{3,})["\']')
DOTTED = re.compile(r'["\']([a-z_]+\.[a-z_]+(?:\.[a-z_]+)?)["\']')


def harvest(rel):
    """Return (defs, uses, imports) for one module.

    defs  : {term -> literal-ish value string} for module-level CONSTANTS, def/class names
    uses  : set of every domain-ish token appearing anywhere
    """
    text = open(os.path.join(REPO, rel), encoding='utf-8', errors='ignore').read()
    defs, uses = {}, set()

    for m in DEF_CONST.finditer(text):
        term, val = m.group(1), m.group(2).strip()
        if term.lower() not in STOP:
            defs[term] = val[:60]

    try:
        tree = ast.parse(text)
    except SyntaxError:
        tree = None
    if tree is not None:
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                if not node.name.startswith('_') and node.name.lower() not in STOP:
                    defs.setdefault(node.name, '<callable>')

    for rx in (QUOTED, DOTTED):
        for tok in rx.findall(text):
            if tok.lower() not in STOP:
                uses.add(tok)
    for tok in re.findall(r'\b([A-Z][A-Z0-9_]{3,})\b', text):
        if tok.lower() not in STOP:
            uses.add(tok)
    # BARE calls only. `(?<![.\w])` rejects `x.append(` / `obj.strip(` — without it the matrix
    # reported `append` as vocabulary shared by 12 subsystems, which is `list.append`, not coupling.
    # This was the instrument's own false-positive class, caught on its first run.
    for tok in re.findall(r'(?<![.\w])([a-z_]{4,})\s*\(', text):
        if tok.lower() not in STOP:
            uses.add(tok)

    imports = set(re.findall(r'(?:^|\n)\s*(?:from|import)\s+([\w.]+)', text))
    return defs, uses, imports


def main(full=False):
    files = [f for f in git_ls('engine/*.py', 'engine/**/*.py', 'systems/**/*.py')
             if not f.endswith('__init__.py')]
    D, U, I = {}, {}, {}
    for f in files:
        D[f], U[f], I[f] = harvest(f)

    subs = {f: subsystem_of(f) for f in files}
    print(f"corpus: {len(files)} modules across {len(set(subs.values()))} subsystems")

    # ── 1. definition collisions ────────────────────────────────────────────
    where = collections.defaultdict(dict)
    for f, d in D.items():
        for term, val in d.items():
            where[term][f] = val
    collisions = {t: w for t, w in where.items() if len(w) > 1}
    callable_only = {t: w for t, w in collisions.items()
                     if all(v == '<callable>' for v in w.values())}
    valued = {t: w for t, w in collisions.items() if t not in callable_only}
    disagree = {t: w for t, w in valued.items() if len(set(w.values())) > 1}

    print(f"\n{'='*78}\n1. DEFINITION COLLISIONS — one term, defined in more than one module\n{'='*78}")
    print(f"  {len(collisions)} term(s) defined in >1 module")
    print(f"    of which constants/values : {len(valued)}   (VALUES DISAGREE: {len(disagree)})")
    print(f"    of which callables only   : {len(callable_only)}")
    print(f"\n  -- constants whose VALUES DISAGREE (folding these is a BEHAVIOUR CHANGE) --")
    for t, w in sorted(disagree.items(), key=lambda x: -len(x[1]))[:25]:
        print(f"    {t}  ({len(w)} definitions)")
        for f, v in sorted(w.items()):
            print(f"        {v:<42s} {f}")
    if not disagree:
        print("    (none)")

    print(f"\n  -- callables defined in >1 module (competing owners) --")
    for t, w in sorted(callable_only.items(), key=lambda x: -len(x[1]))[:20]:
        print(f"    {t:<34s} {len(w):2d}x  {', '.join(sorted(subs[f] for f in w))}")

    # ── 2/3. cross-subsystem throughlines + hidden coupling ────────────────
    def has_import_path(consumer, producer):
        """Does `consumer` name `producer`'s module (or its package) in an import?"""
        mod = producer[:-3].replace('/', '.')
        pkg = '.'.join(mod.split('.')[:-1])
        return any(i == mod or i.startswith(mod + '.') or i == pkg or i.startswith(pkg + '.')
                   for i in I[consumer])

    throughlines, hidden = [], []
    for term, w in where.items():
        producers = list(w)
        psubs = {subs[p] for p in producers}
        for f in files:
            if f in w or term not in U[f]:
                continue
            if subs[f] in psubs:
                continue
            linked = any(has_import_path(f, p) for p in producers)
            rec = (term, sorted(psubs), subs[f], f, producers[0])
            throughlines.append(rec)
            if not linked:
                hidden.append(rec)

    print(f"\n{'='*78}\n2. CROSS-SUBSYSTEM THROUGHLINES — term defined in A, used in B\n{'='*78}")
    print(f"  {len(throughlines)} (term, consumer) edge(s) crossing a subsystem boundary")
    print(f"  {len(hidden)} of them have NO import path from consumer to producer  <-- section 3")

    by_term = collections.Counter(r[0] for r in hidden)
    print(f"\n{'='*78}\n3. HIDDEN COUPLING — shared vocabulary no import expresses\n{'='*78}")
    print("  Ranked by how many foreign subsystems use a term they never import.\n")
    shown = by_term.most_common(None if full else 30)
    for term, n in shown:
        recs = [r for r in hidden if r[0] == term]
        prod = '+'.join(recs[0][1])
        cons = sorted({r[2] for r in recs})
        print(f"    {term:<32s} defined in {prod:<22s} used by {len(cons)} foreign subsystem(s): "
              f"{', '.join(cons)}")
    if not full and len(by_term) > 30:
        print(f"    … +{len(by_term)-30} more (run with --full)")

    # ── 4. subsystem x subsystem ───────────────────────────────────────────
    pair = collections.Counter()
    for term, psubs, csub, _f, _p in throughlines:
        for ps in psubs:
            if ps != csub:
                pair[tuple(sorted((ps, csub)))] += 1
    print(f"\n{'='*78}\n4. SUBSYSTEM x SUBSYSTEM — shared-vocabulary edge counts (top 25)\n{'='*78}")
    for (a, b), n in pair.most_common(25):
        print(f"    {n:5d}  {a}  <->  {b}")
    return 0


if __name__ == '__main__':
    sys.exit(main(full='--full' in sys.argv))
