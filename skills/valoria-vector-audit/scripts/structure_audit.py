#!/usr/bin/env python3
"""
structure_audit.py — the Structural Observatory's ARCHITECTURE layers (WS0b core).

Companion to scripts/vector_audit.py (the L0 prose layer). This builds the code /
module / wiring layers of the observatory — deterministic, working-tree only, and
depending on nothing beyond the Python standard library + PyYAML (so it runs in CI
where only pyyaml is installed). No numpy/sklearn/networkx: the graph algorithms
(Tarjan SCC, articulation points) are implemented here.

Layers built (per the plan's WS0 layer stack):
  * G_code — AST import graph over sim/ + tools/ (real `import`/`from`, not regex).
      Finds import cycles (SCC), cut-vertices (single points of failure), orphans.
  * L2 — module/subsystem wiring graph from references/module_contracts.yaml:
      producer -> consumer edges (from `consumes[].from`), Key emit/consume CLOSURE
      checks (dangling non-terminal emits; phantom producers — a consume whose named
      source does not actually emit that Key type), scale grouping, and cross-scale
      locality (does the wiring cluster by scale, per NS3?).

GOVERNANCE (the anti-fabrication discipline at graph scale — plan §WS0):
  * Working tree only; deterministic; no network.
  * PROVENANCE TAGS: module_contracts is ~37% notional (doc:null / [ASSUMPTION]-grade
      resolvers). Every L2 module carries a `notional` flag; findings on notional
      modules are reported in a separate, lower-confidence bucket. This tool MEASURES;
      it never gates a merge (pytest + import-smoke do).
  * Output reduces to a prioritized register + a scorecard.

CLI:
    python3 structure_audit.py --repo-root . --output-dir <run>
"""
import argparse
import ast
import json
import os
import re
import sys
from collections import defaultdict, deque
from pathlib import Path

try:
    import yaml
except Exception:  # pragma: no cover
    sys.exit("structure_audit requires PyYAML")

# Single-owner __main__-guard predicate (OI-52a, ED-IN-0097, 2026-07-29-code-shape-open-items
# plan §3 Wave 4 item 2 — adopted here by the join lane per the cycle lane's coordination note).
# Was a local AST predicate duplicating tools/ci_common.py's (same both-operand-order logic,
# two independent definitions of one rule — the exact class CLAUDE.md §8 exists to prevent).
# tools/build_apparatus_registry.py already consumes the single owner; this is the second and
# last consumer. Same sys.path idiom as tests/valoria/test_retired_tree_apparatus.py.
_TOOLS_DIR = str(Path(__file__).resolve().parents[3] / 'tools')
try:
    import ci_common
except ImportError:
    if _TOOLS_DIR not in sys.path:
        sys.path.insert(0, _TOOLS_DIR)
    import ci_common


# ──────────────────────────── GRAPH ALGORITHMS (stdlib) ──────────────────────

def tarjan_scc(adj):
    """Strongly-connected components of a digraph {node: iterable(node)}.
    Iterative Tarjan (recursion-safe on large graphs). Returns list of components
    (each a list of nodes); components of size >1 (or self-loops) are cycles."""
    index = {}
    low = {}
    on_stack = {}
    stack = []
    result = []
    counter = [0]
    nodes = list(adj.keys())

    for root in nodes:
        if root in index:
            continue
        work = [(root, iter(adj.get(root, ())))]
        while work:
            node, it = work[-1]
            if node not in index:
                index[node] = low[node] = counter[0]
                counter[0] += 1
                stack.append(node)
                on_stack[node] = True
            advanced = False
            for succ in it:
                if succ not in index:
                    work.append((succ, iter(adj.get(succ, ()))))
                    advanced = True
                    break
                elif on_stack.get(succ):
                    low[node] = min(low[node], index[succ])
            if advanced:
                continue
            if low[node] == index[node]:
                comp = []
                while True:
                    w = stack.pop()
                    on_stack[w] = False
                    comp.append(w)
                    if w == node:
                        break
                result.append(comp)
            work.pop()
            if work:
                parent = work[-1][0]
                low[parent] = min(low[parent], low[node])
    return result


def articulation_points(adj):
    """Cut-vertices of the UNDIRECTED projection of {node: iterable(node)}.
    A node whose removal increases the number of connected components — a single
    point of failure in the dependency structure. Iterative DFS (Tarjan)."""
    undirected = defaultdict(set)
    for u, nbrs in adj.items():
        undirected.setdefault(u, set())
        for v in nbrs:
            if v == u:
                continue
            undirected[u].add(v)
            undirected[v].add(u)
    visited = {}
    disc = {}
    low = {}
    parent = {}
    ap = set()
    timer = [0]
    for start in list(undirected.keys()):
        if start in visited:
            continue
        root_children = 0
        stack = [(start, iter(sorted(undirected[start])))]
        visited[start] = True
        disc[start] = low[start] = timer[0]
        timer[0] += 1
        parent[start] = None
        while stack:
            node, it = stack[-1]
            advanced = False
            for nb in it:
                if nb not in visited:
                    parent[nb] = node
                    if node == start:
                        root_children += 1
                    visited[nb] = True
                    disc[nb] = low[nb] = timer[0]
                    timer[0] += 1
                    stack.append((nb, iter(sorted(undirected[nb]))))
                    advanced = True
                    break
                elif nb != parent.get(node):
                    low[node] = min(low[node], disc[nb])
            if advanced:
                continue
            stack.pop()
            if stack:
                par = stack[-1][0]
                low[par] = min(low[par], low[node])
                if parent.get(par) is not None and low[node] >= disc[par]:
                    ap.add(par)
        if root_children > 1:
            ap.add(start)
    return ap


def degrees(adj, nodes):
    out = {n: len(set(adj.get(n, ()))) for n in nodes}
    indeg = defaultdict(int)
    for u, nbrs in adj.items():
        for v in set(nbrs):
            indeg[v] += 1
    return {n: {'in': indeg.get(n, 0), 'out': out.get(n, 0)} for n in nodes}


# ──────────────────────────── G_CODE — AST IMPORT GRAPH ──────────────────────

# Live Python homes. `sim/` was RETIRED 2026-07-21 (ED-IN-0071 P4 continuation, sim/ hollow-out):
# the engine core moved to `engine/` and every per-subsystem sim to `systems/<sub>/sim/`. This tuple
# still read ('sim', 'tools') until 2026-07-26, so G_code silently covered 88 `tools/` modules and
# ZERO simulation code — the code-architecture layer was blind to the entire engine for five days
# and nothing failed. See EXTRA_CODE_ROOTS for the live-engine-under-tests/ exception, and
# tests/valoria/test_structure_audit.py::test_code_roots_all_exist for the guard that makes this
# class of silent-blindness fail loudly on recurrence.
CODE_ROOTS = ('engine', 'systems', 'tools')

# Live engine code that sits UNDER a SKIP_DIR_PARTS directory and would otherwise be invisible.
# `tests/sim/mass_battle/` is the actively-developed multi-unit battle engine (~10.5k LOC, last
# advanced 2026-07-25) despite `tests/sim/README.md` declaring that tree a frozen run-output
# archive — see engine/sim_reference_README.md's ED-IN-0074 D5 note. Allowlisted EXPLICITLY rather
# than by dropping 'tests' from SKIP_DIR_PARTS, which would drag in the whole tests/ corpus.
EXTRA_CODE_ROOTS = ('tests/sim/mass_battle',)

SKIP_DIR_PARTS = {'__pycache__', 'tests', 'test', 'deprecated', 'archives'}

# The single owner of "explicitly-flagged not-built" (P1 primitive, ED-IN-0091 plan §2.1):
# engine/substrate/stubwire.py. A module is `stub_wired` iff it imports this — one dotted name,
# checked below.
STUBWIRE_MODULE = 'engine.substrate.stubwire'


def _module_name(rel_path):
    """systems/factions/sim/faction_action.py -> systems.factions.sim.faction_action;
    .../__init__.py -> the package name."""
    p = rel_path[:-3] if rel_path.endswith('.py') else rel_path
    parts = p.split('/')
    if parts and parts[-1] == '__init__':
        parts = parts[:-1]
    return '.'.join(parts)


def collect_py_modules(root):
    """{dotted_module: relpath} for every internal .py under the code roots
    (skipping caches/tests/deprecated/archives)."""
    mods = {}
    for base in CODE_ROOTS + EXTRA_CODE_ROOTS:
        allow = base in EXTRA_CODE_ROOTS      # allowlisted root: don't re-skip its own path parts
        base_parts = base.split('/')
        for dirpath, dirnames, filenames in os.walk(root / base):
            rel_dir = os.path.relpath(dirpath, root).replace(os.sep, '/')
            tail = rel_dir.split('/')[len(base_parts):] if allow else rel_dir.split('/')
            if any(part in SKIP_DIR_PARTS for part in tail):
                continue
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIR_PARTS]
            for fn in filenames:
                if fn.endswith('.py'):
                    rel = os.path.relpath(os.path.join(dirpath, fn), root).replace(os.sep, '/')
                    mods[_module_name(rel)] = rel
    return mods


def missing_code_roots(root):
    """Configured code roots that do not exist on disk. A non-empty result means G_code is
    silently under-scanning — the 2026-07-26 `sim/` blindness class. Surfaced in the register
    and asserted by tests/valoria/test_structure_audit.py."""
    return [b for b in CODE_ROOTS + EXTRA_CODE_ROOTS if not (Path(root) / b).is_dir()]


def sys_path_aliases(modules):
    """{imported_name: collected_name} for roots that are put on `sys.path` at runtime and are
    therefore imported under a SHORTER dotted name than their repo path implies.

    `tests/sim/mass_battle/` inserts `tests/sim` on `sys.path` and imports itself as top-level
    `mass_battle.*`. Without this map its 28 modules collect as `tests.sim.mass_battle.*`, NO
    internal edge resolves, and the whole package lands in the orphan list as 28 false positives
    — visible but edgeless is WORSE than unscanned, because it reads as a measured emptiness."""
    aliases = {}
    for base in EXTRA_CODE_ROOTS:
        prefix = base.replace('/', '.')
        parent = prefix.rsplit('.', 1)[0] if '.' in prefix else ''
        if not parent:
            continue
        for mod in modules:
            if mod == prefix or mod.startswith(prefix + '.'):
                aliases[mod[len(parent) + 1:]] = mod
    return aliases


def _resolve_internal(target, known, aliases=None):
    """Map an imported dotted name to the known internal module it (or its nearest
    package prefix) denotes, else None."""
    if target in known:
        return target
    if aliases and target in aliases:
        return aliases[target]
    parts = target.split('.')
    while parts:
        cand = '.'.join(parts)
        if cand in known:
            return cand
        if aliases and cand in aliases:
            return aliases[cand]
        parts = parts[:-1]
    return None


def build_g_code(root, modules):
    """Directed import graph over internal modules. Edge A -> B iff A imports B."""
    known = set(modules)
    aliases = sys_path_aliases(modules)
    g = defaultdict(set)
    parse_errors = []
    for mod, rel in modules.items():
        g.setdefault(mod, set())
        try:
            tree = ast.parse((root / rel).read_text(encoding='utf-8', errors='replace'), filename=rel)
        except SyntaxError as e:
            parse_errors.append(f'{rel}: {e}')
            continue
        # The package this file lives in: for a package __init__.py the module NAME already IS
        # the package (so its own `from . import x` must resolve against itself); for a regular
        # module a.b.c it is a.b. (Fable-5 audit fix: the old `mod.rsplit('.',1)[0]` dropped the
        # last segment unconditionally, so every relative import inside a package __init__ resolved
        # one package too high — e.g. `from . import ip_track` in sim/peninsular/__init__.py landed
        # on the nonexistent sim.ip_track instead of sim.peninsular.ip_track — producing false
        # import-orphans and a dropped relative-import cycle. It also ignored multi-dot node.level.)
        is_pkg = rel.endswith('__init__.py')
        cur_pkg = mod if is_pkg else (mod.rsplit('.', 1)[0] if '.' in mod else '')
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    tgt = _resolve_internal(alias.name, known, aliases)
                    if tgt and tgt != mod:
                        g[mod].add(tgt)
            elif isinstance(node, ast.ImportFrom):
                base = node.module or ''
                if node.level:  # relative import — resolve against this file's package, walking
                    #             up (level-1) packages for each leading dot beyond the first
                    parts = cur_pkg.split('.') if cur_pkg else []
                    up = node.level - 1
                    base_pkg = '.'.join(parts[:len(parts) - up]) if up <= len(parts) else ''
                    base = (base_pkg + ('.' + base if base else '')) if base_pkg else base
                # try the module, then module.name for `from pkg import submod`
                cands = [base] + [f'{base}.{a.name}' for a in node.names if base]
                for c in cands:
                    tgt = _resolve_internal(c, known, aliases)
                    if tgt and tgt != mod:
                        g[mod].add(tgt)
    return g, parse_errors


# ──────────────────────────── CLI ENTRY-POINT DETECTION ──────────────────────
#
# OI-55 open half (ED-IN-0092): code_orphans (below) previously excluded only
# `.__main__` suffixes and leading-`_` private names, so a genuine CLI tool with
# zero internal importers — every `tools/ci_*.py` invoked only from a workflow
# YAML or a git hook, never from another Python module — read as dead code. A
# `python foo.py` entry point is a real, intentional zero-importer by design; it
# is a different thing from an accidentally-orphaned module, and conflating them
# makes the orphan list too noisy to trust (exactly the "visible but wrong bucket"
# failure mode CLAUDE.md §0.1 warns against). Detection lives ONCE here — a single
# AST predicate plus a single split function — and both the CLI list and the
# (now narrower) orphan list are surfaced in the same report/JSON, never silently.

def collect_cli_entry_modules(root, modules):
    """{module_name, ...} — every module whose AST contains a `__main__` guard, per
    `ci_common.has_main_guard()` — the single owner (OI-52a/OI-54, ED-IN-0097). Parses each module
    independently of `build_g_code`'s import-focused AST pass (a second, cheap parse over the same
    files) so this detection stays self-contained and never touches the already-verified
    relative-import resolution fix in `build_g_code`."""
    entries = set()
    for mod, rel in modules.items():
        try:
            tree = ast.parse((root / rel).read_text(encoding='utf-8', errors='replace'), filename=rel)
        except SyntaxError:
            continue
        if ci_common.has_main_guard(tree):
            entries.add(mod)
    return entries


def split_orphans_and_cli_entries(code_nodes, code_deg, main_guard_modules):
    """The single owner of the orphan/CLI-entry split, so `run()`'s JSON + register
    output and any test exercise identical logic. A node is an orphan CANDIDATE iff
    it has zero internal importers and isn't a `.__main__` shim or a private
    (`_`-prefixed) name — unchanged from the pre-existing rule. Among candidates:
    a `__main__`-guarded module is a `cli_entries` member (a real, intentional
    entry point), never a `code_orphans` member. A guarded module that DOES have
    importers is neither — it was never an orphan candidate to begin with."""
    candidates = [n for n in code_nodes
                  if code_deg[n]['in'] == 0
                  and not n.endswith('.__main__')
                  and not n.split('.')[-1].startswith('_')]
    cli_entries = sorted(n for n in candidates if n in main_guard_modules)
    code_orphans = sorted(n for n in candidates if n not in main_guard_modules)
    return code_orphans, cli_entries


def stub_wired_modules(g_code):
    """`stub_wired` node attribute (P1 primitive §2.1, ED-IN-0091): every module that imports
    `engine.substrate.stubwire`, per the SAME AST import pass `build_g_code` already ran — no
    second parser (CLAUDE.md §0 "compose on top of it", §8 "every rule lives once"). `g_code` is
    the resolved internal import graph {module: {imported internal modules}}; a module is
    stub-wired iff STUBWIRE_MODULE is one of its resolved edges. Self-import is impossible here
    (build_g_code already excludes `tgt == mod`), so stubwire.py itself never lists itself."""
    return sorted(m for m, targets in g_code.items() if STUBWIRE_MODULE in targets)


# ──────────────────────────── L2 — MODULE WIRING GRAPH ───────────────────────

def _as_list(v):
    """module_contracts `from:` is sometimes a bare string, sometimes a list — a
    real data hazard (iterating the string yields characters). Normalize."""
    if v is None:
        return []
    if isinstance(v, str):
        return [v]
    if isinstance(v, list):
        return [x for x in v if isinstance(x, str)]
    return []


def is_notional(doc, resolver):
    """The ONE provenance predicate (capstone §8 reconciliation, ED-IN-0056): a
    module_contracts entry is `notional` — lower-confidence, doc:null /
    [ASSUMPTION]-grade — when it has no home design doc OR no real resolver.
    Single-sourced HERE and imported by formula_audit.py (which previously
    copy-pasted the identical `(not doc) or (resolver in (None,'None'))` rule),
    so the governance predicate the observatory's contract says every layer
    honors uniformly genuinely lives once."""
    return (not doc) or (resolver in (None, 'None'))


def build_l2(root):
    """L2 module graph + closure findings from references/module_contracts.yaml.
    Returns (graph, modules_meta, findings)."""
    path = root / 'references' / 'module_contracts.yaml'
    raw = path.read_text(encoding='utf-8', errors='replace')
    data = yaml.safe_load(raw) or {}
    mods = data.get('modules', []) or []
    names = {m.get('module') for m in mods if isinstance(m, dict)}

    meta = {}
    emit_index = defaultdict(set)   # key_type -> {modules that emit it}
    emit_terminal = {}              # (module, type) -> terminal?
    for m in mods:
        if not isinstance(m, dict):
            continue
        name = m.get('module')
        doc = m.get('doc')
        resolver = m.get('resolver')
        notional = is_notional(doc, resolver)
        meta[name] = {
            'scales': m.get('scales') or [], 'resolver': resolver,
            'doc': doc, 'status': m.get('status'),
            'notional': bool(notional),
            # optional prose display-names for this module (how OTHER docs refer to it) — lets the
            # Workbench match a module counterpart precisely instead of only humanizing its id.
            'aliases': [a for a in (m.get('aliases') or []) if isinstance(a, str)],
            # OI-54 (ED-IN-0097): the module's own declared code home — a repo-relative file/dir
            # path, the literal string 'none' (with a reason comment in the YAML), or absent
            # (None) if the contract predates this field. Raw value only; l2_contract_code_join()
            # does the resolution against G_code.
            'sim_module': m.get('sim_module'),
        }
        for e in (m.get('emits') or []):
            if isinstance(e, dict) and e.get('type'):
                emit_index[e['type']].add(name)
                emit_terminal[(name, e['type'])] = bool(e.get('terminal'))

    g = defaultdict(set)
    for n in names:
        g.setdefault(n, set())
    consume_index = defaultdict(set)  # key_type -> {consumers}
    edges_meta = []
    findings = {'phantom_producer': [], 'dangling_emit': [], 'doc_null': [],
                'unconsumed_terminal_ok': 0}

    for m in mods:
        if not isinstance(m, dict):
            continue
        dst = m.get('module')
        for c in (m.get('consumes') or []):
            if not isinstance(c, dict):
                continue
            ktype = c.get('type')
            if not ktype or ktype == '*':      # wildcard consume — skip closure logic
                continue
            for src in _as_list(c.get('from')):
                if src in names:
                    g[src].add(dst)
                    edges_meta.append({'src': src, 'dst': dst, 'type': ktype})
                consume_index[ktype].add(dst)
                # phantom producer: src named as a source but does not emit ktype
                if src in names and src not in emit_index.get(ktype, set()):
                    findings['phantom_producer'].append(
                        {'consumer': dst, 'named_source': src, 'type': ktype,
                         'src_notional': meta.get(src, {}).get('notional', False)})

    # dangling emit: a non-terminal emit that nobody consumes
    for (mod, ktype), terminal in emit_terminal.items():
        if ktype not in consume_index:
            if terminal:
                findings['unconsumed_terminal_ok'] += 1
            else:
                findings['dangling_emit'].append(
                    {'emitter': mod, 'type': ktype,
                     'notional': meta.get(mod, {}).get('notional', False)})

    for name, mm in meta.items():
        if not mm['doc']:
            findings['doc_null'].append(name)

    assumption_count = raw.count('[ASSUMPTION]')
    return g, meta, edges_meta, findings, assumption_count


def cross_scale_locality(g, meta):
    """Per NS3: what fraction of L2 edges stay within a scale vs cross scales.
    High cross-scale fraction = the wiring does not cluster by scale."""
    intra = cross = 0
    per_module = {}
    for src, dsts in g.items():
        s_scales = set(meta.get(src, {}).get('scales', []))
        sm_intra = sm_cross = 0
        for dst in dsts:
            d_scales = set(meta.get(dst, {}).get('scales', []))
            if s_scales & d_scales:
                intra += 1; sm_intra += 1
            else:
                cross += 1; sm_cross += 1
        if sm_intra + sm_cross:
            per_module[src] = {'intra': sm_intra, 'cross': sm_cross}
    total = intra + cross
    return {'intra': intra, 'cross': cross,
            'cross_fraction': round(cross / total, 3) if total else 0.0,
            'per_module': per_module}


def l2_contract_without_code(l2_nodes, code_nodes):
    """Evidence for the contract↔code correspondence DISCLOSURE (capstone #7,
    ED-IN-0056). Nothing in the observatory joins L2's `module_contracts.yaml`
    modules to G_code's real code modules, so a fictional / unimplemented contract
    would surface as canon-grade wiring unchallenged. This computes the plain-name
    match rate purely to SHOW that a name heuristic cannot close that gap: a contract
    'has code' only if its name is a dotted segment of some G_code module path (e.g.
    `mass_battle` <- `sim.provincial.mass_battle`). It returns the unmatched list, but
    that list is NOT presented as findings — the real convention diverges (`massbattle`,
    `faction_action.py`, ...) so most misses are false positives. `run()` uses only the
    COUNT, to disclose (not measure) the gap; closing it needs a mechanics_index
    `sim_module:` join, a deferred task."""
    code_segments = set()
    for m in code_nodes:
        for seg in m.split('.'):
            code_segments.add(seg)
    return sorted(m for m in l2_nodes if m and m not in code_segments)


def l2_contract_code_join(meta, modules):
    """JOIN-VERIFIED contract↔code correspondence (OI-54, ED-IN-0097, 2026-07-29-code-shape-open-
    items plan §3 Wave 4 item 4). Supersedes `l2_contract_without_code()`'s plain-name heuristic as
    `run()`'s primary correspondence signal — that function's disclosure text (kept, unmodified, for
    its own pinned test) already explains WHY a name match cannot do this job; this is the real join
    it named as the closing move: read each contract's own declared `sim_module:` field
    (`references/module_contracts.yaml`) and resolve it against the SAME file set
    `collect_py_modules()` already parsed for G_code — no second file-existence scan, no second
    owner of "does this path exist" (§8).

    `meta`    — {module_name: {..., 'sim_module': <str | 'none' | None>}} from `build_l2()`.
    `modules` — {dotted_module: relpath} from `collect_py_modules()`; `relpath` is what a
                `sim_module:` file path is checked against, and a `sim_module:` DIRECTORY path
                (combat_engine_v1/, contest/, ...) is checked as a prefix of at least one relpath —
                the same convention `combat`/`social_contest` already use in
                `registers/mechanics_index.yaml`.

    Four buckets, every L2 module in exactly one:
      - 'joined'        the declared path resolves to a real file or a real directory (>=1 scanned
                         code file under it) — genuine G_code correspondence.
      - 'none'           the contract explicitly declares no code exists (`sim_module: none`) — a
                         disclosed absence, not a gap in this join.
      - 'unresolvable'  the declared path matches NEITHER a file nor a directory prefix in the
                         scanned set — the FICTIONAL-CONTRACT case this whole join exists to catch
                         (a contract could otherwise claim wiring to code that was never verified to
                         exist). This is the one bucket that should always be empty in a clean tree.
      - 'undeclared'    the contract carries no `sim_module:` key at all — reported separately so a
                         future contract that forgets the field is visible, never silently folded
                         into 'unresolvable' (which would conflate "never declared" with "declared
                         and wrong")."""
    relpaths = set(modules.values())

    def _resolves(path):
        if path in relpaths:
            return True
        d = path if path.endswith('/') else path + '/'
        return any(rp.startswith(d) for rp in relpaths)

    joined, none, unresolvable, undeclared = [], [], [], []
    for name in sorted(meta):
        sm = meta[name].get('sim_module')
        if sm is None:
            undeclared.append(name)
        elif sm == 'none':
            none.append(name)
        elif isinstance(sm, str) and _resolves(sm):
            joined.append(name)
        else:
            unresolvable.append(name)
    return {'joined': joined, 'none': none, 'unresolvable': unresolvable, 'undeclared': undeclared}


# ──────────────────────────── OUTPUT ─────────────────────────────────────────

def _cycles(scc, adj):
    """Cycles = SCCs of size >1, PLUS single-node self-loops. `tarjan_scc` groups a
    self-loop into a size-1 component, so a self-loop must be checked against the
    adjacency explicitly — exactly what this module's own `tarjan_scc` docstring
    promises ("components of size >1 (or self-loops) are cycles"). Extracting only
    `len(c) > 1` silently DROPPED self-loops (capstone reconciliation #1/#2,
    ED-IN-0056): a module that imports itself, or an L2 module that emits a Key it
    also consumes, is a real 1-node cycle the scorecard must not undercount. Shared
    with formula_audit.py, which imports this rather than keeping its own copy (§8)."""
    out = []
    for c in scc:
        if len(c) > 1:
            out.append(sorted(c))
        elif len(c) == 1 and c[0] in adj.get(c[0], ()):
            out.append(list(c))
    return out


def run(root, out):
    root, out = Path(root), Path(out)
    (out / 'data').mkdir(parents=True, exist_ok=True)

    print('[G_code] parsing sim/ + tools/ imports (AST)...')
    modules = collect_py_modules(root)
    g_code, parse_errors = build_g_code(root, modules)
    code_nodes = list(modules)
    code_scc = tarjan_scc(g_code)
    code_cycles = sorted(_cycles(code_scc, g_code))   # sort the cycle LIST (each cycle is already
    #                                                   internally sorted) so the dumped order is
    #                                                   deterministic — tarjan visits SCCs in the
    #                                                   set-derived node order, hash-seed dependent
    #                                                   (Fable-5 audit finding; mirrors the capstone
    #                                                   cut-vertex/hub tiebreak, now applied to cycles)
    code_cuts = articulation_points(g_code)
    code_deg = degrees(g_code, code_nodes)
    main_guard_modules = collect_cli_entry_modules(root, modules)
    code_orphans, cli_entries = split_orphans_and_cli_entries(code_nodes, code_deg, main_guard_modules)
    stub_wired = stub_wired_modules(g_code)
    print(f'         {len(code_nodes)} modules, '
          f'{sum(len(v) for v in g_code.values())} import edges, '
          f'{len(code_cycles)} cycle(s), {len(code_cuts)} cut-vertex(es), '
          f'{len(cli_entries)} cli-entry(ies), {len(stub_wired)} stub-wired')

    print('[L2] building module_contracts wiring graph...')
    g_l2, meta, edges_meta, findings, assumption_count = build_l2(root)
    l2_nodes = list(meta)
    l2_scc = tarjan_scc(g_l2)
    l2_cycles = sorted(_cycles(l2_scc, g_l2))  # sorted for determinism; cross-check vs contracts' `loops`
    l2_deg = degrees(g_l2, l2_nodes)
    l2_cuts = articulation_points(g_l2)
    locality = cross_scale_locality(g_l2, meta)
    l2_without_code = l2_contract_without_code(l2_nodes, code_nodes)
    l2_join = l2_contract_code_join(meta, modules)   # OI-54: the real join (l2_without_code kept
    #        above only for its own pinned test + disclosure text; run() no longer keys off it)
    assert (len(l2_join['joined']) + len(l2_join['none']) + len(l2_join['unresolvable'])
            + len(l2_join['undeclared'])) == len(l2_nodes), \
        'OI-54 join must account for every L2 module exactly once (§0.1 #2: assert it asserted)'
    # capstone #4 (ED-IN-0056): `edges_meta` is the RAW emit->consume edge list (parallel
    # edges kept); the cycle/cut-vertex/locality metrics all run on `g_l2`, the DEDUPLICATED
    # simple graph. Report BOTH so the scorecard never juxtaposes a raw multi-edge count with
    # simple-graph stats as if they were the same graph.
    l2_simple_edges = sum(len(v) for v in g_l2.values())
    print(f'     {len(l2_nodes)} modules, {len(edges_meta)} wiring edges, '
          f'{len(findings["phantom_producer"])} phantom-producer, '
          f'{len(findings["dangling_emit"])} dangling-emit, '
          f'{len(findings["doc_null"])} doc:null')

    # ---- JSON ----
    def dump(name, obj):
        (out / 'data' / name).write_text(json.dumps(obj, indent=1, sort_keys=True), encoding='utf-8')
    dump('g_code.json', {k: sorted(v) for k, v in g_code.items()})
    dump('g_l2.json', {k: sorted(v) for k, v in g_l2.items()})
    dump('structure_metrics.json', {
        'code': {'nodes': len(code_nodes), 'edges': sum(len(v) for v in g_code.values()),
                 'cycles': code_cycles, 'cut_vertices': sorted(code_cuts),
                 'orphans': code_orphans, 'cli_entries': cli_entries,
                 'stub_wired': stub_wired, 'parse_errors': parse_errors},
        'l2': {'nodes': len(l2_nodes),
               'edges_raw': len(edges_meta),        # raw emit->consume edges (parallels kept)
               'edges_simple': l2_simple_edges,     # deduplicated graph the metrics below run on
               'cycles': l2_cycles,
               'cut_vertices': sorted(l2_cuts), 'locality': locality,
               # OI-54 (ED-IN-0097): JOIN-VERIFIED against sim_module:, superseding the old
               # capstone #7 "no reliable name join" disclosure. True now that every contract
               # carries a sim_module: field resolved against G_code — see l2_join below.
               'contract_code_correspondence_verified': True,
               'contract_code_join': l2_join,   # {'joined', 'none', 'unresolvable', 'undeclared'}
               'contract_code_name_unmatched': l2_without_code,   # kept: the retired heuristic's
               #        own output, informational only (its function's docstring explains why a
               #        plain-name match cannot do this job — now demonstrated, not just asserted)
               'assumption_markers': assumption_count},
        'findings': findings,
    })

    # ---- register (primary deliverable) ----
    top_code_hubs = sorted(code_nodes, key=lambda n: (-(code_deg[n]['in'] + code_deg[n]['out']), n))[:12]
    top_l2_hubs = sorted(l2_nodes, key=lambda n: (-(l2_deg[n]['in'] + l2_deg[n]['out']), n))[:12]
    real_phantoms = [p for p in findings['phantom_producer'] if not p['src_notional']]
    notional_phantoms = [p for p in findings['phantom_producer'] if p['src_notional']]
    real_dangling = [d for d in findings['dangling_emit'] if not d['notional']]

    L = []
    L.append('# Structure register — architecture layers (G_code + L2)')
    L.append('')
    L.append('Deterministic, working-tree only. **Measures; does not gate** (pytest + import-smoke gate). '
             'Provenance: L2 is built on `module_contracts.yaml`, which carries '
             f'{assumption_count} `[ASSUMPTION]` markers and {len(findings["doc_null"])} `doc:null` modules — '
             'findings on those are bucketed as lower-confidence.')
    L.append('')
    _missing = missing_code_roots(root)
    L.append(f'**Code roots scanned:** {", ".join(CODE_ROOTS + EXTRA_CODE_ROOTS)}.')
    if _missing:
        L.append(f'> ⚠️ **CONFIGURED CODE ROOT MISSING — G_code IS UNDER-SCANNING:** {", ".join(_missing)}. '
                 'Every finding below is scoped to the roots that DO exist; absence of a finding in a '
                 'missing root is not evidence of health.')
    L.append('')
    L.append(f'**Scorecard:** code-modules={len(code_nodes)}, import-edges={sum(len(v) for v in g_code.values())}, '
             f'import-cycles={len(code_cycles)}, code-cut-vertices={len(code_cuts)}, code-orphans={len(code_orphans)}, '
             f'cli-entries={len(cli_entries)}, stub-wired={len(stub_wired)}; '
             f'l2-modules={len(l2_nodes)}, wiring-edges={len(edges_meta)} raw ({l2_simple_edges} simple/deduped — '
             f'the cycle/cut-vertex/locality metrics run on the simple graph), l2-cycles={len(l2_cycles)}, '
             f'l2-contract↔code-correspondence=JOINED({len(l2_join["joined"])} joined, '
             f'{len(l2_join["none"])} none, {len(l2_join["unresolvable"])} unresolvable, '
             f'{len(l2_join["undeclared"])} undeclared / {len(l2_nodes)}), '
             f'phantom-producers={len(real_phantoms)}(+{len(notional_phantoms)} notional), '
             f'dangling-emits={len(real_dangling)}, cross-scale-fraction={locality["cross_fraction"]}.')
    L.append('')

    def section(title, rows, fmt, empty='(none)'):
        # Disclose truncation with a "… N more" line, matching formula_audit.py /
        # gen_audit.py's helpers. The Fable-5 2026-07-14 audit caught this helper silently
        # dropping rows (87 import-orphans, only 20 shown) with no in-section signal —
        # the observatory's own "never a silent cap" rule, violated in the observatory.
        L.append(f'## {title}')
        L.append(empty if not rows else '')
        for r in rows[:20]:
            L.append('- ' + fmt(r))
        if len(rows) > 20:
            L.append(f'- … {len(rows) - 20} more (see `data/structure_metrics.json`)')
        L.append('')

    L.append('## L2 Key-closure — relationship to the module-adjudicator (§8 disclosure)')
    L.append('')
    L.append('The two closure findings below (phantom-producer, dangling-emit) overlap '
             '`valoria-module-adjudicator`’s **A3 consume-closure** and **A4 orphan emission** — and '
             'the honest §8 accounting (corrected after the Fable-5 2026-07-14 audit called out an '
             'earlier over-claim) is: this is **NOT the same rule, and the two are NOT equivalent.** '
             '`contract_adjudicator.adjudicate()` already runs A1–A12 **corpus-wide** in one call '
             '(it is not per-module — the earlier version of this note wrongly implied it was), '
             'against the Key registry, and — critically — it does **family-wildcard inhabitance** '
             'checking for wildcard consumes like `scene.*` (`_wild_registered`/`_pat_overlap`). This '
             'layer’s `build_l2()` deliberately does **less**: it `continue`s past every wildcard '
             'consume (`ktype == "*"` or a family pattern) rather than resolving it, so it detects '
             'only the exact-type phantom/dangling cases. It is therefore a **strict-subset, '
             'registry-unaware, corpus-wide MEASURE**, not a re-implementation of A3/A4 and not a '
             'second gate. The adjudicator is the authoritative registry-aware gate; where the two '
             'disagree the adjudicator wins, and this layer will MISS any closure defect that only a '
             'wildcard-family resolution would surface. A row here is a pointer to inspect, not a '
             'ruling. (True single-sourcing — importing `adjudicate()` here — is the right end-state; '
             'it is tracked, not yet done, because that function returns prose verdicts rather than '
             'the structured edge list this graph layer needs.)')
    L.append('')
    section('L2 phantom producers — a consume names a source that does NOT emit that Key '
            '(canon-grade; the mass_battle `scene_outcome.battle_concluded` class)',
            real_phantoms,
            lambda p: f"`{p['consumer']}` consumes `{p['type']}` from `{p['named_source']}`, "
                      f"which emits no such Key")
    section('L2 dangling emits — a non-terminal Key emitted but consumed nowhere (canon-grade)',
            real_dangling, lambda d: f"`{d['emitter']}` emits `{d['type']}` — no consumer")
    section('Import cycles (SCC > 1) in sim/ + tools/', code_cycles,
            lambda c: ' ↔ '.join(c[:6]) + (' …' if len(c) > 6 else ''))
    # capstone #3 (ED-IN-0056): articulation_points() returns a set; sorting only by
    # -degree left equal-degree ties resolving in set-iteration (hash-seed) order —
    # nondeterministic across runs. The `n` tiebreaker makes the register order a total,
    # reproducible order (the JSON already sorts alphabetically; now the register agrees).
    section('Code cut-vertices — single points of failure (removal disconnects the import graph)',
            sorted(code_cuts, key=lambda n: (-(code_deg[n]['in'] + code_deg[n]['out']), n)),
            lambda n: f"`{n}` (in {code_deg[n]['in']}, out {code_deg[n]['out']})")
    section('L2 module cut-vertices — wiring fragility points',
            sorted(l2_cuts, key=lambda n: (-(l2_deg[n]['in'] + l2_deg[n]['out']), n)),
            lambda n: f"`{n}` (in {l2_deg[n]['in']}, out {l2_deg[n]['out']}, "
                      f"{'notional' if meta[n]['notional'] else 'canon'})")
    section('doc:null modules — registered contract, no home design doc (unimplementable spec)',
            sorted(findings['doc_null']), lambda n: f"`{n}`")
    L.append('## Contract↔code correspondence — JOIN-VERIFIED (OI-54, ED-IN-0097, was capstone #7\'s '
             'DISCLOSED BLACK-HOLE, ED-IN-0056)')
    L.append('')
    L.append(f'Every one of L2\'s {len(l2_nodes)} `module_contracts.yaml` modules now carries an explicit '
             f'`sim_module:` field, resolved here against G_code\'s {len(code_nodes)} real code modules — '
             f'a file path checked for an exact relpath match, a directory path checked as a prefix of '
             f'>=1 scanned file (the `combat`/`social_contest` convention `mechanics_index.yaml` already '
             f'used), and the literal `none` accepted as a disclosed absence. A plain NAME match — kept '
             f'below as `l2_contract_without_code()`, unmodified, for its own pinned test — still finds '
             f'only {len(l2_nodes) - len(l2_without_code)}/{len(l2_nodes)} (the code uses `massbattle` for '
             f'the `mass_battle` contract, folds `faction_state`\'s state into `game_state.py`, etc.); the '
             f'join below is what actually closes the gap that heuristic could only disclose. Result: '
             f'**{len(l2_join["joined"])} joined, {len(l2_join["none"])} explicitly none, '
             f'{len(l2_join["unresolvable"])} unresolvable, {len(l2_join["undeclared"])} undeclared** — '
             f'`unresolvable` is the fictional-contract case this join exists to catch and should read 0 '
             f'on a clean tree; `undeclared` should always read 0 now that all 27 modules carry the field '
             f'(a nonzero value here is itself a regression, not a pre-existing gap).')
    L.append('')
    section('L2 contract↔code UNRESOLVABLE — sim_module: names neither a real file nor a real '
            'directory prefix in G_code (canon-grade: a fictional or stale code-home claim)',
            l2_join['unresolvable'], lambda n: f"`{n}` -> `{meta[n].get('sim_module')}`")
    section('L2 contract↔code UNDECLARED — no sim_module: field at all (regression watch: should '
            'be empty now that all 27 module_contracts.yaml entries carry the field)',
            l2_join['undeclared'], lambda n: f"`{n}`")
    section('Import orphans — internal module nothing imports (dead-ish; verify before removal)',
            code_orphans, lambda n: f"`{n}`")
    section('CLI entry points — modules with an `if __name__ == \'__main__\':` guard and zero '
            'importers: runnable as scripts, NOT verified as invoked (a module whose only '
            '`__main__` is a self-test still lands here) — excluded from Import orphans above '
            '(OI-55/ED-IN-0092); cross-check `references/apparatus_registry.md`\'s Invoked-by '
            'column before trusting any row',
            cli_entries, lambda n: f"`{n}`")
    section(f'Stub-wired — modules that import `{STUBWIRE_MODULE}` (P1 primitive §2.1, '
            'ED-IN-0091: an explicitly-flagged not-built call site, never a silent raise or a '
            'fabricated value)',
            stub_wired, lambda n: f"`{n}`")
    section('Code import hubs (highest total degree — change-impact)', top_code_hubs,
            lambda n: f"`{n}` (in {code_deg[n]['in']}, out {code_deg[n]['out']})")
    section('L2 wiring hubs (highest total degree)', top_l2_hubs,
            lambda n: f"`{n}` (in {l2_deg[n]['in']}, out {l2_deg[n]['out']})")
    L.append('## Cross-scale locality (NS3 — does the wiring cluster by scale?)')
    L.append(f"{locality['intra']} intra-scale vs {locality['cross']} cross-scale edges "
             f"({locality['cross_fraction']:.0%} cross). Lower is better-clustered.")
    L.append('')
    L.append('> **EXPLORATORY, not authoritative (capstone #8, ED-IN-0056):** this metric keys on each '
             'module\'s `scales:` field, whose vocabulary is NOT yet reconciled (that is WS2 — the four '
             'divergent scale vocabularies are an open workstream), so the intra/cross split can shift '
             'when the vocabulary lands. Unlike the phantom-producer / dangling-emit findings above, this '
             'one does NOT split notional (`doc:null`/`[ASSUMPTION]`) modules into a lower-confidence '
             'bucket — a notional module\'s declared `scales:` is weighted the same as a canon module\'s. '
             'Read it as a directional signal, not a gate.')
    L.append('')
    if notional_phantoms:
        L.append('## Lower-confidence (findings on notional/[ASSUMPTION] modules)')
        for p in notional_phantoms[:15]:
            L.append(f"- `{p['consumer']}` ← `{p['named_source']}` `{p['type']}` (source notional)")
        L.append('')

    (out / 'structure_register.md').write_text('\n'.join(L), encoding='utf-8')
    print(f'[done] {out}/structure_register.md')
    return findings


def run_stub_count(root):
    """Lightweight `--stub-count` mode (tools/review_core.py's `stubs.count` signal, ED-IN-0091
    plan §2.1): runs only the G_code import pass + `stub_wired_modules` — no L2 build, no
    `--output-dir`, no files written — and prints a count `review_core`'s `count_re` can parse.
    Same single-owner rule as the full `run()`: no second AST pass, no second registry. Exit code
    follows the existing report-only convention (`ci_quantity_vocabulary_check.py` et al.): 0 when
    the count is 0, 1 otherwise, so review_core's ratchet reads a fresh count only on 'fail'."""
    modules = collect_py_modules(root)
    g_code, _parse_errors = build_g_code(root, modules)
    stub_wired = stub_wired_modules(g_code)
    print(f'== structure_audit --stub-count: {len(stub_wired)} stub-wired module(s) '
          f'(engine.substrate.stubwire, ED-IN-0091 plan §2.1) — report-only ==')
    for m in stub_wired:
        print(f'  STUB-WIRED {m}')
    if not stub_wired:
        print('  (nothing to report — zero modules import engine.substrate.stubwire yet)')
    return 1 if stub_wired else 0


def run_contracts_join(root):
    """Lightweight `--contracts-join` mode (tools/review_core.py's `contracts.join` signal,
    OI-54, ED-IN-0097, 2026-07-29-code-shape-open-items plan §3 Wave 4 item 4): runs only the
    G_code pass + `build_l2()` + `l2_contract_code_join()` — no `--output-dir`, no files written
    — and prints a count `review_core`'s `count_re` can parse. Same single-owner rule as the full
    `run()`: no second AST pass, no second contract parse. Mirrors `run_stub_count()`'s exit-code
    convention: 0 when unresolvable count is 0, 1 otherwise, so review_core's ratchet reads a
    fresh count only on 'fail'. Deliberately keys ONLY on `unresolvable` (a fictional/stale
    sim_module: claim) — `undeclared` (a contract that has not yet added the field, e.g. the
    MB-owned mass_battle row) is a disclosed, tracked state, not itself a regression signal."""
    modules = collect_py_modules(root)
    _g_code, _parse_errors = build_g_code(root, modules)
    _g_l2, meta, _edges_meta, _findings, _assumption_count = build_l2(root)
    join = l2_contract_code_join(meta, modules)
    unresolvable = join['unresolvable']
    print(f'== structure_audit --contracts-join: {len(join["joined"])} joined, {len(join["none"])} none, '
          f'{len(unresolvable)} unresolvable, {len(join["undeclared"])} undeclared '
          f'(of {len(meta)} module_contracts.yaml modules) — report-only ==')
    for m in unresolvable:
        print(f'  UNRESOLVABLE {m} -> {meta[m].get("sim_module")!r}')
    if join['undeclared']:
        print(f'  (undeclared, not counted as regression: {", ".join(join["undeclared"])})')
    if not unresolvable:
        print('  (nothing to report — every declared sim_module: resolves to a real G_code node)')
    return 1 if unresolvable else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument('--repo-root', default='.', help='repo root (working tree)')
    ap.add_argument('--output-dir', help='audit output folder (required unless --stub-count / '
                                          '--contracts-join)')
    ap.add_argument('--stub-count', action='store_true',
                    help='print the stub_wired module count only (tools/review_core.py '
                         "'stubs.count' signal) and exit — skips the full run() output")
    ap.add_argument('--contracts-join', action='store_true',
                    help='print the contract<->code join unresolvable count only '
                         "(tools/review_core.py 'contracts.join' signal, OI-54) and exit — "
                         'skips the full run() output')
    a = ap.parse_args()
    root = Path(a.repo_root)
    if not (root / 'references' / 'module_contracts.yaml').exists():
        sys.exit(f"not a Valoria repo root (no references/module_contracts.yaml): {root}")
    if a.stub_count:
        sys.exit(run_stub_count(root))
    if a.contracts_join:
        sys.exit(run_contracts_join(root))
    print(f'[structure_audit] repo root (working tree): {root.resolve()}')
    if not a.output_dir:
        sys.exit('--output-dir is required unless --stub-count or --contracts-join is passed')
    run(root, a.output_dir)


if __name__ == '__main__':
    main()
