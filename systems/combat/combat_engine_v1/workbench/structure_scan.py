"""Structural-debt scan of combat_engine_v1: ownership, hard-coding, organisation.

Counts only what it can prove from the AST. Every number printed is reproducible.
"""
import ast, os, sys, collections, re

ENG = '/home/user/ttrpg/systems/combat/combat_engine_v1'
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
_TESTSRC = []
for _root, _dirs, _files in os.walk(os.path.join(REPO, 'tests')):
    if '__pycache__' in _root:
        continue
    for _f in _files:
        if _f.endswith('.py'):
            try:
                _TESTSRC.append(open(os.path.join(_root, _f), encoding='utf-8').read())
            except Exception:
                pass
allsrc = "\n".join(list(srcs.values()) + _TESTSRC)
zero_callers = []
for fname, mods in defs.items():
    if fname.startswith('_'):
        continue
    # count usages as an attribute or bare call anywhere
    hits = len(re.findall(r'(?<![\w.])' + re.escape(fname) + r'\s*\(', allsrc))
    hits += len(re.findall(r'\.' + re.escape(fname) + r'\s*\(', allsrc))
    defcount = len(mods)
    if hits <= defcount:   # only the definition line(s)
        zero_callers.append((fname, mods))

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
VOCAB = ['point', 'cut_thrust', 'straight_cut', 'curved_cut', 'blunt',
         'none', 'light', 'medium', 'heavy', 'parry', 'dodge', 'wind',
         'shear', 'puncture', 'percussion', 'cloth', 'mail', 'plate']
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

# ── report ──────────────────────────────────────────────────────────────────────────
print("=" * 78)
print(f"SCOPE: {len(CORE)} engine modules + {len(WBF)} workbench modules")
print("=" * 78)

print(f"\n[A] DUPLICATE top-level definitions across engine modules: {len(dup_defs)}")
for k, v in sorted(dup_defs.items()):
    print(f"    {k:28s} in {sorted(set(v))}")
print(f"\n[A2] CONSTANTS defined in >1 engine module: {len(dup_consts)}")
for k, v in sorted(dup_consts.items()):
    print(f"    {k:28s} in {sorted(set(v))}")

print(f"\n[B] Top-level functions with NO caller anywhere in package+workbench: {len(zero_callers)}")
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
