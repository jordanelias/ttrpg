"""Structural-debt scan of combat_engine_v1: ownership, hard-coding, organisation.

Counts only what it can prove from the AST. Every number printed is reproducible.

IMPORTABLE (ED-PC-0042): the analysis runs at import; only the REPORT is under __main__. Section [H]
(dead exported keys) is consumed as a CI guard by tests/valoria/test_combat_invariants.py, which imports
`dead_exported_keys()` from here rather than re-deriving it — every rule lives once (CLAUDE.md §8).
"""
import ast, os, sys, collections, json, re

# Derived from __file__, never hardcoded: this module is imported by the shipping pytest gate
# (test_no_dead_exported_engine_params), so an absolute machine path here would error on every
# other checkout — CI runs at /home/runner/work/..., the exact /home/claude-hardcode failure
# class CLAUDE.md §8 retired tools for (caught by the E0 adversarial gate, 2026-07-29).
ENG = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = [f for f in sorted(os.listdir(ENG)) if f.endswith('.py')]
WB = os.path.join(ENG, 'workbench')
WBF = [os.path.join('workbench', f) for f in sorted(os.listdir(WB)) if f.endswith('.py')]
ALL = [(f, os.path.join(ENG, f)) for f in FILES] + [(f, os.path.join(ENG, f)) for f in WBF]

trees = {}
srcs = {}
for name, path in ALL:
    src = open(path, encoding='utf-8').read()
    srcs[name] = src
    try:
        trees[name] = ast.parse(src)
    except SyntaxError as e:
        print(f"PARSE FAIL {name}: {e}")

CORE = [f for f in FILES]  # engine modules only (exclude workbench for ownership counts)

# ── A. duplicate top-level definitions across modules ────────────────────────────────
defs = collections.defaultdict(list)     # name -> [module]
consts = collections.defaultdict(list)   # NAME -> [module]
for name in CORE:
    t = trees.get(name)
    if not t:
        continue
    for node in t.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            defs[node.name].append(name)
        elif isinstance(node, ast.ClassDef):
            defs[node.name].append(name)
        elif isinstance(node, ast.Assign):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name) and tgt.id.isupper():
                    consts[tgt.id].append(name)

dup_defs = {k: v for k, v in defs.items() if len(set(v)) > 1}
dup_consts = {k: v for k, v in consts.items() if len(set(v)) > 1}

# ── B. zero-caller top-level functions (engine modules; search whole package incl. workbench)
# SCOPE FIX (adversarial review R-2, 2026-07-28): the caller sweep originally searched only the engine
# package + workbench. It therefore MISSED tests/, and shipped a FALSE "zero callers" claim for
# combat_systems.can_choke -- which is called at tests/valoria/test_combat_units_refactor.py:118 and pinned
# per-weapon in r3_identity_golden.json. That was the SECOND false positive from this scope bug (WoundTracker
# was the first, caught by hand). A caller-analysis that cannot see the test suite is not a caller analysis.
REPO = os.path.abspath(os.path.join(ENG, '..', '..', '..'))

# LAZY (ED-PC-0042): this sweep reads every .py under tests/ and runs two regexes per engine function over
# the concatenation — ~20 s. It used to run at import, which was free while this file was only ever a
# script; now that the CI dead-key guard IMPORTS the module, charging the shipping gate 20 s for a section
# it does not consume would be a real cost. Same computation, same output, paid only by report().
def zero_caller_functions():
    """Top-level engine functions with no call site in package + workbench + tests. Text-matched, so treat
    it as a CANDIDATE list: it over-reports (a name mentioned in prose as `foo(` counts as a hit) and cannot
    see dynamic dispatch. Verify each candidate by hand before deleting anything."""
    # TEST ROOTS ARE DISCOVERED, NOT HARDCODED (2026-08-03, ED-IN-0123). This walked
    # `REPO/tests` unconditionally. Two problems: it was a path-literal escape out of
    # `systems/` into a tree the fork LEAVES behind (plan of record §5), and if that tree is
    # absent `os.walk` yields nothing silently -- so every engine function would read as
    # zero-caller and the report would be confidently wrong rather than empty. Now the roots
    # that exist are used and their absence is stated by the caller-visible count below.
    test_roots = [os.path.join(REPO, 'tests'),
                  os.path.join(REPO, 'engine', 'tests')]
    test_roots = [r for r in test_roots if os.path.isdir(r)]
    testsrc = []
    for test_root in test_roots:
        for root, _dirs, files in os.walk(test_root):
            if '__pycache__' in root:
                continue
            for f in files:
                if f.endswith('.py'):
                    try:
                        testsrc.append(open(os.path.join(root, f), encoding='utf-8').read())
                    except Exception:
                        pass
    if not testsrc:
        # Loud, because the alternative is a dead-code report that lists everything.
        raise RuntimeError(
            "zero_caller_functions(): no test sources found under any of "
            f"{test_roots or '(no test root exists)'} -- every engine function would falsely "
            "read as having no caller. Point test_roots at this checkout's test tree.")
    allsrc = "\n".join(list(srcs.values()) + testsrc)
    out = []
    for fname, mods in defs.items():
        if fname.startswith('_'):
            continue
        # count usages as an attribute or bare call anywhere
        hits = len(re.findall(r'(?<![\w.])' + re.escape(fname) + r'\s*\(', allsrc))
        hits += len(re.findall(r'\.' + re.escape(fname) + r'\s*\(', allsrc))
        if hits <= len(mods):   # only the definition line(s)
            out.append((fname, mods))
    return out

# ── C. inline numeric literals inside function bodies (magic-number candidates) ──────
BENIGN = {0, 1, 2, 0.0, 1.0, 0.5, 2.0, 3, 100, -1}
magic = collections.Counter()
magic_sites = collections.defaultdict(list)
for name in CORE:
    t = trees.get(name)
    if not t:
        continue
    for fn in [n for n in ast.walk(t) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]:
        for node in ast.walk(fn):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) \
               and not isinstance(node.value, bool):
                if node.value in BENIGN:
                    continue
                magic[name] += 1
                magic_sites[name].append((fn.name, node.lineno, node.value))

# ── D. domain string literals repeated (vocabulary that should be a shared definition)
# The token list is READ FROM THE OWNER (vocabulary.GUARDED_TOKENS, ED-PC-0042) instead of being re-listed
# here, so this measurement and the CI guard that enforces it cannot drift apart. Same 18 tokens the
# pre-sweep tree measured at 279 occurrences.
sys.path.insert(0, ENG)
from vocabulary import GUARDED_TOKENS as _GUARDED
VOCAB = sorted(_GUARDED)
vocab_count = collections.Counter()
for name in CORE:
    t = trees.get(name)
    if not t:
        continue
    for node in ast.walk(t):
        if isinstance(node, ast.Constant) and isinstance(node.value, str) and node.value in VOCAB:
            vocab_count[node.value] += 1

# ── E. module size / shape ───────────────────────────────────────────────────────────
sizes = []
for name in CORE:
    t = trees.get(name)
    if not t:
        continue
    nfun = len([n for n in t.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))])
    ncls = len([n for n in t.body if isinstance(n, ast.ClassDef)])
    lines = srcs[name].count('\n') + 1
    code = len([l for l in srcs[name].splitlines()
                if l.strip() and not l.strip().startswith('#')])
    comment = len([l for l in srcs[name].splitlines() if l.strip().startswith('#')])
    sizes.append((lines, code, comment, nfun, ncls, name))
sizes.sort(reverse=True)

# ── F. classes in the engine ────────────────────────────────────────────────────────
classes = [(n, c.name, len([b for b in c.body if isinstance(b, ast.FunctionDef)]))
           for n in CORE if trees.get(n)
           for c in trees[n].body if isinstance(c, ast.ClassDef)]

# ── G. sys.path manipulation (a packaging smell) ────────────────────────────────────
syspath = [(n, srcs[n].count('sys.path.insert')) for n in CORE if 'sys.path.insert' in srcs[n]]
syspath_wb = [(n, srcs[n].count('sys.path.insert')) for n in WBF if 'sys.path.insert' in srcs[n]]

# ── H. dead EXPORTED keys — a param shipped into the typed Godot contract with NO live reader ───────
# The recurring defect this measures (ED-PC-0035 cleaned it, ED-PC-0037 cleaned it again, and the
# 2026-07-26 register found a third instance): a constant loses its last reader, the AUTO-collecting
# exporter keeps shipping it into engine/engine_params/combat_engine_v1.json, and the Godot port
# hand-transcribes a number the oracle no longer resolves on. An instrument, not a heuristic — the read
# set is AST-derived, so a name that appears only in a comment or a docstring does not count as a reader.
EXPORT_JSON = os.path.join(REPO, 'engine', 'engine_params', 'combat_engine_v1.json')

def _docstring_nodes(tree):
    doc = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            body = getattr(node, 'body', [])
            if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) \
               and isinstance(body[0].value.value, str):
                doc.add(id(body[0].value))
    return doc

def _read_sites(tree):
    """Every identifier a module READS: a Load-context bare name, an attribute name, or a string literal
    (the `cfg['KEY']` form). DEFINITIONS are excluded by construction — a Store-context target and a
    `dict(KEY=...)` keyword are neither Load-Names nor Constants — so `X = 1` alone never makes X live."""
    doc = _docstring_nodes(tree)
    out = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str) and id(node) not in doc:
            out.add(node.value)
        elif isinstance(node, ast.Attribute):
            out.add(node.attr)
        elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
            out.add(node.id)
    return out

_ENGINE_READS = set()
for _name in CORE:
    if trees.get(_name):
        _ENGINE_READS |= _read_sites(trees[_name])

def exported_keys(sections=('cfg', 'core')):
    """The keys of the typed Godot-facing export, per section. Read from the artifact (never re-derived),
    so this measures what actually SHIPS. Note the nesting: json['sections']['cfg'|'core']."""
    with open(EXPORT_JSON, encoding='utf-8') as fh:
        payload = json.load(fh)
    return {s: sorted(payload['sections'][s]) for s in sections}

def dead_exported_keys(sections=('cfg', 'core')):
    """Exported params with zero live read-sites in the ENGINE package (workbench excluded on purpose: a
    tooling-only reader does not make a key live in the thing that ships). Sorted; [] is the healthy state."""
    keys = exported_keys(sections)
    return sorted(k for s in sections for k in keys[s] if k not in _ENGINE_READS)


# ── report ──────────────────────────────────────────────────────────────────────────
def report():
    print("=" * 78)
    print(f"SCOPE: {len(CORE)} engine modules + {len(WBF)} workbench modules")
    print("=" * 78)

    print(f"\n[A] DUPLICATE top-level definitions across engine modules: {len(dup_defs)}")
    for k, v in sorted(dup_defs.items()):
        print(f"    {k:28s} in {sorted(set(v))}")
    print(f"\n[A2] CONSTANTS defined in >1 engine module: {len(dup_consts)}")
    for k, v in sorted(dup_consts.items()):
        print(f"    {k:28s} in {sorted(set(v))}")

    zero_callers = zero_caller_functions()
    print(f"\n[B] Top-level functions with NO caller anywhere in package+workbench+tests: {len(zero_callers)}")
    for k, v in sorted(zero_callers):
        print(f"    {k:34s} defined in {v}")

    print(f"\n[C] Inline numeric literals inside function bodies (magic-number candidates)")
    print(f"    TOTAL across engine modules: {sum(magic.values())}")
    for name, c in magic.most_common():
        print(f"    {name:24s} {c}")

    print(f"\n[D] Domain vocabulary strings hard-coded as literals (should be shared defs)")
    print(f"    TOTAL occurrences: {sum(vocab_count.values())}  across {len(vocab_count)} tokens")
    for k, c in vocab_count.most_common(12):
        print(f"    '{k}'{'':<{max(0,16-len(k))}} {c}")

    print(f"\n[E] Module shape (lines / code / comment / funcs / classes)")
    for lines, code, comment, nfun, ncls, name in sizes:
        pct = round(100 * comment / max(1, code + comment))
        print(f"    {name:22s} {lines:5d} {code:5d} {comment:5d} ({pct:3d}% cmt) {nfun:3d} fn {ncls} cls")

    print(f"\n[F] Classes in the entire engine: {len(classes)}")
    for mod, cname, nmeth in classes:
        print(f"    {mod:22s} {cname:20s} {nmeth} methods")

    print(f"\n[G] sys.path.insert occurrences (packaging smell)")
    print(f"    engine modules: {sum(c for _, c in syspath)} across {len(syspath)} files")
    print(f"    workbench:      {sum(c for _, c in syspath_wb)} across {len(syspath_wb)} files")

    dead = dead_exported_keys()
    counts = {s: len(v) for s, v in exported_keys().items()}
    print(f"\n[H] DEAD EXPORTED PARAMS (in the typed Godot contract, zero live engine reader)")
    print(f"    scope: {counts['cfg']} cfg + {counts['core']} core = {sum(counts.values())} exported params")
    print(f"    dead:  {dead}")


if __name__ == '__main__':
    report()
