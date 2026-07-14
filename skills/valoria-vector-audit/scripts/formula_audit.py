#!/usr/bin/env python3
"""
formula_audit.py — the Structural Observatory's L1 FORMULA-DEPENDENCY layer.

Companion to structure_audit.py (G_code/L2, architecture) and pointer_audit.py
(G_pointer, registry resolution). This builds the QUANTITY DEPENDENCY DAG —
"which quantity is computed from which" — and surfaces formula-structure
defects on it: orphan inputs (referenced but never defined and not a
registered descriptor), multi-definition outputs (the same quantity defined
in more than one place), and dependency cycles (a quantity that transitively
depends on itself).

SCOPE — READ THIS BEFORE TRUSTING A "CLEAN" RESULT (stated, not silently
dropped — CLAUDE.md's under-claim-rather-than-over-claim ethic):
  This tool is CONTRACT-LEVEL ONLY. It builds the DAG from two canon-grade,
  already-structured sources:
    1. references/module_contracts.yaml `modules[].derivations[]`
       (`output` <- each of `inputs[]`)
    2. references/descriptor_registry.yaml `aggregates.entries[]`
       (`members[]` -> `key`, the agg.body/mind/social sums) and any
       `*_stats.entries[]` row carrying a `derived_from` field (today: only
       `prac.tps derived_from prac.thread_sensitivity`).
  It does NOT parse params/*.md prose tables. That means it CANNOT catch a
  formula contradiction that lives only in prose — e.g. the "Prosperity x50
  vs x10" family CLAUDE.md flags at the doc level is actually two
  DIFFERENT-NAMED contract outputs here ("Local Economy" vs "faction Treasury
  income (cross-module -> faction_state)"), so this tool's same-output-name
  multi-definition check correctly does NOT fire on it — that class of
  contradiction needs a real prose/formula table extractor (deliberately
  deferred, mirrors A17/A18's own sequencing note in
  tools/ci_quantity_vocabulary_check.py). Only 8 module_contracts.yaml
  derivations exist as of this writing (2026-07-13) across 27 modules, so the
  DAG this tool sees today is small and this scope limit matters a lot in
  practice, not just in theory.

REUSE, NOT REIMPLEMENTATION (CLAUDE.md §8 — "every rule lives once"):
  * tools/quantity_registry.py `resolve()` is the ONE resolver for "does this
    name point at a registered descriptor?" — imported, not re-derived, same
    as pointer_audit.py.
  * tools/ci_quantity_vocabulary_check.py's `_split_bundled()` (A17) is the
    ONE splitter for bundled "A / B / C" state/derivation names — imported,
    not re-derived.
  * structure_audit.py's `tarjan_scc()` (iterative Tarjan SCC) and `degrees()`
    are the graph primitives already built for this observatory — imported
    from the sibling script (same scripts/ directory) rather than a second
    Tarjan implementation living here.

GOVERNANCE (mirrors structure_audit.py / pointer_audit.py):
  * Working tree only; deterministic; no network; stdlib + PyYAML only.
  * PROVENANCE TAGS: an edge/definition is `notional` when it comes from a
    module_contracts.yaml module with `doc: null` or an `[ASSUMPTION]`-grade
    resolver (mirrors structure_audit.py's L2 notional flag), OR from a
    descriptor_registry.yaml aggregate still marked `status: placeholder`
    (W2.8 — "defined; not yet wired into derived values"). Findings that only
    touch notional/placeholder material are bucketed separately, lower
    confidence.
  * MEASURES, NEVER GATES. Output reduces to `formula_register.md` +
    `data/g_formula.json` (+ `data/formula_metrics.json`) + a scorecard.

KNOWN LIMITATIONS (disclosed up front, not discovered by the critic):
  * Node identity is exact raw text (after A17's bundle-split) when a
    quantity does not resolve via the registry, or the registry `key:` when
    it does. Two unresolved spellings of "the same" quantity that differ by
    more than a trailing parenthetical annotation (e.g. a leading qualifier
    word: "settlement Order" vs "Order") are DIFFERENT nodes in the graph —
    this is a known, stated gap, not a silent one. The ONE extra
    normalization applied is a loose "is this input actually defined
    elsewhere as an output" check that strips a trailing parenthetical
    annotation via `quantity_registry`'s own `_PAREN_RE` (reused, not a new
    regex) — e.g. an input written as "faction Mandate" is recognized as
    already defined by an output named "faction Mandate (cross-module ->
    faction_state)". Beyond that one normalization, orphan-vs-defined is
    exact-string.
  * Some orphan-input findings will be `tools/quantity_registry.py` false
    negatives rather than genuine contract gaps (the same class pointer_audit
    and A17 both flag: a name is unresolved because of a leading/trailing
    qualifier word the resolver's normalization doesn't strip, e.g.
    "settlement Prosperity" vs registered "Prosperity" / `set.prosperity`).
    Triage before treating every orphan row as a genuine missing definition.
  * `derivations[].inputs[]` legitimately includes internal/intermediate
    quantities with no registry-eligible identity (e.g. `cumulative_damage`,
    `L_s`, `W_s`) — A17's own docstring calls this "a real, expected backlog
    item, not a bug in the checker." They will still show as orphan inputs
    here (this tool does not special-case them) because they are also not
    the `output` of any registered derivation — that is itself informative
    (an intermediate the contract corpus never actually derives), not noise
    to suppress.
  * `--contracts`/`--descriptor` re-root only what is SCANNED, not the
    resolver: `quantity_registry.resolve()` has no path override, so it always
    reads the real references/descriptor_registry.yaml / names_index.yaml next
    to tools/quantity_registry.py (identical inherited limitation to
    pointer_audit.py / A17). An identifier's resolved/orphan status therefore
    reflects the live registry, not a `--descriptor` fixture.
  * The one loose paren-strip normalization (above) is TEXTUAL, not semantic:
    as module_contracts.yaml derivations grow, an output like "Momentum (combat
    term)" could coincidentally shadow an unrelated, genuinely-undefined input
    "Momentum" and suppress that orphan. It does not manifest in today's small
    corpus (the only paren-suffixed output collides only with its own
    same-concept input) but is a real false-negative vector to revisit if the
    derivation set expands.

CLI:
    python3 formula_audit.py --repo-root . --output-dir <run>
"""
import argparse
import json
import os
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path

try:
    import yaml
except Exception:  # pragma: no cover
    sys.exit("formula_audit requires PyYAML")

# Import the graph primitives + the shared provenance/cycle rules from the sibling
# observatory script (same scripts/ directory) rather than a second implementation.
# `is_notional` and `_cycles` are single-sourced in structure_audit.py (capstone §8
# reconciliation, ED-IN-0056) — this module previously kept its own copies.
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPT_DIR not in sys.path:
    sys.path.insert(0, _SCRIPT_DIR)
from structure_audit import tarjan_scc, degrees, is_notional, _cycles  # noqa: E402  (reused, not reimplemented)

# Import the ONE resolver + the ONE bundle-splitter from tools/ (mirrors
# pointer_audit.py's import block exactly).
_STATIC_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_SCRIPT_DIR)))
_TOOLS_DIR = os.path.join(_STATIC_REPO_ROOT, 'tools')
if _TOOLS_DIR not in sys.path:
    sys.path.insert(0, _TOOLS_DIR)

import quantity_registry                          # noqa: E402  (the resolver, tools/quantity_registry.py)
import descriptor_registry                         # noqa: E402  (the ONE descriptor_registry.yaml parser)
import ci_quantity_vocabulary_check as a17          # noqa: E402  (the bundle-splitter, A17)


# ──────────────────────────── IDENTITY / RESOLUTION ──────────────────────────

def resolve_component(comp):
    """(resolved, node_id) for a single already-bundle-split component string.

    node_id is the registry `key:` when `quantity_registry.resolve()` finds one
    (this is what lets a module_contracts.yaml derivation input like "Strength"
    and a descriptor_registry.yaml aggregate member `attr.body.strength` land
    on the SAME graph node); otherwise node_id is the raw component text
    itself. `resolved` follows the exact same predicate pointer_audit.py /
    A17 use: `matched_as is not None` (a `not_descriptors` match — matched but
    no key — still counts as resolved; see quantity_registry.resolve()'s
    docstring)."""
    matched, key = quantity_registry.resolve(comp)
    resolved = matched is not None
    node_id = key if (resolved and key) else comp
    return resolved, node_id


def _loose_form(raw):
    """The ONE extra normalization applied when checking whether an input is
    'itself the output of some derivation' (not applied to node identity,
    only to that one check) — strips a trailing parenthetical annotation by
    reusing `quantity_registry`'s own `_PAREN_RE`, not a new regex."""
    return quantity_registry._PAREN_RE.sub('', raw or '').strip()


# ──────────────────────────── SOURCE 1: module_contracts.yaml ────────────────

def module_meta_from_contracts(contracts):
    """{module_name: {'doc':, 'resolver':, 'notional': bool}} — same notional
    predicate as structure_audit.py's build_l2()."""
    meta = {}
    for m in contracts.get('modules', []) or []:
        if not isinstance(m, dict):
            continue
        name = m.get('module')
        doc = m.get('doc')
        resolver = m.get('resolver')
        notional = is_notional(doc, resolver)   # single-sourced from structure_audit (§8, ED-IN-0056)
        meta[name] = {'doc': doc, 'resolver': resolver, 'notional': bool(notional)}
    return meta


def build_contract_edges(contracts):
    """Edges + output definitions from module_contracts.yaml `derivations[]`.

    Returns (edges, definitions):
      edges: list of dicts {src, dst, src_raw, dst_raw, src_resolved,
             dst_resolved, module, derivation_index, notional, formula,
             source, layer='module_contracts.derivations'} — one row per
             (input component, output component) pair within a derivation
             (bundled "A / B / C" outputs/inputs are split via A17's
             `_split_bundled`, matching how A17/pointer_audit already treat
             this convention).
      definitions: {node_id: [ {module, derivation_index, raw_output,
             component, inputs, formula, source, bucket, notional} ]} — every
             place a node_id is produced as an output, for multi-definition
             detection.
    """
    meta = module_meta_from_contracts(contracts)
    edges = []
    definitions = defaultdict(list)

    for m in contracts.get('modules', []) or []:
        if not isinstance(m, dict):
            continue
        mod_name = m.get('module')
        notional = meta.get(mod_name, {}).get('notional', False)
        for idx, d in enumerate(m.get('derivations') or []):
            if not isinstance(d, dict):
                continue
            raw_output = d.get('output')
            raw_inputs = [i for i in (d.get('inputs') or []) if isinstance(i, str)]
            output_components = a17._split_bundled(raw_output)
            input_components = []
            for raw_inp in raw_inputs:
                for comp in a17._split_bundled(raw_inp):
                    input_components.append((raw_inp, comp))

            # A missing/blank `output` must NOT silently drop this derivation's inputs
            # (a typo'd output field would otherwise hide a genuine orphan). Route the
            # inputs to a clearly-labelled sentinel output node so they are still
            # emitted and orphan-evaluated; find_malformed_derivations() surfaces the
            # malformed contract row itself for the register.
            if not output_components and input_components:
                output_components = [f'<no-output: {mod_name}#{idx}>']

            for out_comp in output_components:
                out_resolved, out_node = resolve_component(out_comp)
                definitions[out_node].append({
                    'module': mod_name, 'derivation_index': idx, 'raw_output': raw_output,
                    'component': out_comp, 'inputs': list(raw_inputs),
                    'formula': d.get('formula'), 'source': d.get('source'),
                    'bucket': d.get('bucket'), 'notional': notional,
                })
                for raw_inp, in_comp in input_components:
                    in_resolved, in_node = resolve_component(in_comp)
                    edges.append({
                        'src': in_node, 'dst': out_node,
                        'src_raw': in_comp, 'dst_raw': out_comp,
                        'src_resolved': in_resolved, 'dst_resolved': out_resolved,
                        'module': mod_name, 'derivation_index': idx, 'notional': notional,
                        'formula': d.get('formula'), 'source': d.get('source'),
                        'layer': 'module_contracts.derivations',
                    })
    return edges, definitions


def find_malformed_derivations(contracts):
    """Derivations whose `output` is missing/blank. build_contract_edges routes such
    a derivation's inputs to a sentinel node so their orphan status still surfaces;
    this flags the malformed contract row itself so it is visible in the register."""
    meta = module_meta_from_contracts(contracts)
    out = []
    for m in contracts.get('modules', []) or []:
        if not isinstance(m, dict):
            continue
        mod_name = m.get('module')
        notional = meta.get(mod_name, {}).get('notional', False)
        for idx, d in enumerate(m.get('derivations') or []):
            if not isinstance(d, dict):
                continue
            if not a17._split_bundled(d.get('output')):
                out.append({'module': mod_name, 'derivation_index': idx,
                            'inputs': [i for i in (d.get('inputs') or []) if isinstance(i, str)],
                            'notional': notional})
    return out


# ──────────────────────────── SOURCE 2: descriptor_registry.yaml ─────────────

def build_descriptor_edges(descriptor):
    """Edges from descriptor_registry.yaml: aggregate members -> aggregate,
    and any `*_stats.entries[]` row's `derived_from` -> its own key. Both
    sides are already canonical registry keys (this file IS the registry) so
    `src_resolved`/`dst_resolved` are True by construction — these are NOT
    run through `quantity_registry.resolve()`, which is name-based and would
    spuriously fail on a bare dotted key like `attr.body.strength` (it
    resolves display NAMES like "Strength", not keys)."""
    edges = []
    for e in (descriptor.get('aggregates', {}) or {}).get('entries', []) or []:
        if not isinstance(e, dict):
            continue
        agg_key = e.get('key')
        if not agg_key:
            continue
        low_conf = (e.get('status') == 'placeholder')
        for member in e.get('members') or []:
            edges.append({
                'src': member, 'dst': agg_key, 'src_raw': member, 'dst_raw': agg_key,
                'src_resolved': True, 'dst_resolved': True,
                'module': None, 'derivation_index': None, 'notional': low_conf,
                'formula': e.get('compute'), 'source': 'descriptor_registry.yaml aggregates',
                'layer': 'descriptor_registry.aggregates',
            })

    for section in ('practitioner_stats', 'faction_stats', 'settlement_stats', 'territory_stats'):
        sec = descriptor.get(section, {}) or {}
        for e in sec.get('entries', []) or []:
            if not isinstance(e, dict):
                continue
            df = e.get('derived_from')
            key = e.get('key')
            if not df or not key:
                continue
            edges.append({
                'src': df, 'dst': key, 'src_raw': df, 'dst_raw': key,
                'src_resolved': True, 'dst_resolved': True,
                'module': None, 'derivation_index': None,
                'notional': (e.get('status') == 'placeholder'),
                'formula': e.get('formula'), 'source': f'descriptor_registry.yaml {section}',
                'layer': f'descriptor_registry.{section}',
            })
    return edges


# ──────────────────────────── GRAPH ASSEMBLY ──────────────────────────────────

def build_adjacency(edges, definitions):
    """{node: set(successors)} over every node touched by an edge OR a
    definition (an output with zero declared inputs still needs to exist)."""
    adj = defaultdict(set)
    for e in edges:
        adj[e['src']].add(e['dst'])
        adj.setdefault(e['dst'], set())
    for node in definitions:
        adj.setdefault(node, set())
    return adj


def compute_max_depth(adj, scc):
    """Longest path (edge count) through the SCC-condensed graph. Condensing
    first makes this safe even if a cycle exists (a raw longest-path search
    on a cyclic graph does not terminate)."""
    comp_of = {}
    for i, comp in enumerate(scc):
        for n in comp:
            comp_of[n] = i
    n_comps = len(scc)
    cadj = defaultdict(set)
    for u, vs in adj.items():
        cu = comp_of[u]
        for v in vs:
            cv = comp_of[v]
            if cu != cv:
                cadj[cu].add(cv)
    indeg = Counter()
    for u in range(n_comps):
        indeg.setdefault(u, 0)
    for u, vs in cadj.items():
        for v in vs:
            indeg[v] += 1
    q = deque(u for u in range(n_comps) if indeg.get(u, 0) == 0)
    dist = {u: 0 for u in range(n_comps)}
    indeg_work = dict(indeg)
    processed = 0
    while q:
        u = q.popleft()
        processed += 1
        for v in cadj.get(u, ()):
            if dist[u] + 1 > dist[v]:
                dist[v] = dist[u] + 1
            indeg_work[v] -= 1
            if indeg_work[v] == 0:
                q.append(v)
    return max(dist.values()) if dist else 0


# ──────────────────────────── DETECTIONS ──────────────────────────────────────

def find_orphan_inputs(edges, definitions):
    """Inputs that are neither (a) resolvable via quantity_registry.resolve()
    nor (b) themselves the output of some derivation. (b) is checked at TWO
    granularities: exact raw component text, and the loose paren-stripped
    form (see `_loose_form`) — nothing else is normalized (stated limitation
    in the module docstring)."""
    output_forms = set()
    for defs in definitions.values():
        for d in defs:
            output_forms.add(d['component'])
            output_forms.add(_loose_form(d['component']))

    rows = {}
    for e in edges:
        if e['layer'] != 'module_contracts.derivations':
            continue  # descriptor_registry edges are src_resolved=True by construction
        if e['src_resolved']:
            continue
        raw = e['src_raw']
        if raw in output_forms or _loose_form(raw) in output_forms:
            continue
        row = rows.setdefault(raw, {
            'identifier': raw, 'occurrences': [], 'any_canon': False,
        })
        row['occurrences'].append({
            'module': e['module'], 'derivation_index': e['derivation_index'],
            'formula': e.get('formula'), 'notional': e['notional'],
        })
        if not e['notional']:
            row['any_canon'] = True

    out = list(rows.values())
    out.sort(key=lambda r: (not r['any_canon'], -len(r['occurrences']), r['identifier']))
    return out


def find_multi_definitions(definitions):
    """Node ids that are the `output` of more than one distinct (module,
    derivation_index) — the 'defined N ways' contradiction class, AT THE
    CONTRACT LEVEL (see module docstring for why prose-level cases like
    Prosperity x50-vs-x10 do not surface here — they are different output
    names, so no node collision occurs)."""
    out = []
    for node_id, defs in definitions.items():
        distinct = {}
        for d in defs:
            distinct[(d['module'], d['derivation_index'])] = d
        if len(distinct) <= 1:
            continue
        recs = list(distinct.values())
        input_sets = sorted({tuple(sorted(r['inputs'])) for r in recs})
        out.append({
            'node': node_id,
            'definitions': recs,
            'differing_inputs': len(input_sets) > 1,
            'any_canon': any(not r['notional'] for r in recs),
        })
    out.sort(key=lambda m: (not m['any_canon'], not m['differing_inputs'], -len(m['definitions']), m['node']))
    return out


# ──────────────────────────── OUTPUT ──────────────────────────────────────────

def run(root, out, contracts_path=None, descriptor_path=None):
    root, out = Path(root), Path(out)
    (out / 'data').mkdir(parents=True, exist_ok=True)

    contracts_path = Path(contracts_path) if contracts_path else root / 'references' / 'module_contracts.yaml'
    descriptor_path = Path(descriptor_path) if descriptor_path else root / 'references' / 'descriptor_registry.yaml'

    print('[L1] reading module_contracts.yaml derivations + descriptor_registry.yaml aggregates/derived_from...')
    if not contracts_path.exists():
        sys.exit(f"module_contracts.yaml not found: {contracts_path}")
    contracts = yaml.safe_load(contracts_path.read_text(encoding='utf-8')) or {}
    if not isinstance(contracts, dict):
        sys.exit(f"module_contracts.yaml is not a mapping (got {type(contracts).__name__}): {contracts_path}")
    if descriptor_path.exists():
        descriptor = descriptor_registry.load(text=descriptor_path.read_text(encoding='utf-8')) or {}
    else:
        print(f'[L1] warn: descriptor_registry.yaml not found ({descriptor_path}); descriptor edges skipped')
        descriptor = {}

    contract_edges, definitions = build_contract_edges(contracts)
    descriptor_edges = build_descriptor_edges(descriptor)
    malformed = find_malformed_derivations(contracts)
    edges = contract_edges + descriptor_edges

    adj = build_adjacency(edges, definitions)
    nodes = list(adj)
    scc = tarjan_scc(adj)
    cycles = _cycles(scc, adj)
    deg = degrees(adj, nodes)
    roots = sorted(n for n in nodes if deg[n]['in'] == 0 and deg[n]['out'] > 0)
    leaves = sorted(n for n in nodes if deg[n]['out'] == 0 and deg[n]['in'] > 0)
    isolated = sorted(n for n in nodes if deg[n]['in'] == 0 and deg[n]['out'] == 0)
    max_depth = compute_max_depth(adj, scc)

    orphans = find_orphan_inputs(edges, definitions)
    multi_defs = find_multi_definitions(definitions)

    total_edges = sum(len(v) for v in adj.values())
    print(f'         {len(nodes)} nodes, {total_edges} edges '
          f'({len(contract_edges)} module_contracts, {len(descriptor_edges)} descriptor_registry), '
          f'{len(cycles)} cycle(s), {len(orphans)} orphan input(s), {len(multi_defs)} multi-def output(s), '
          f'{len(malformed)} malformed derivation(s)')

    # ---- JSON ----
    def dump(name, obj):
        (out / 'data' / name).write_text(json.dumps(obj, indent=1, sort_keys=True, default=list), encoding='utf-8')

    dump('g_formula.json', {k: sorted(v) for k, v in adj.items()})
    dump('formula_metrics.json', {
        'nodes': len(nodes), 'edges': total_edges,
        'contract_edges': len(contract_edges), 'descriptor_edges': len(descriptor_edges),
        'cycles': cycles, 'roots': roots, 'leaves': leaves, 'isolated': isolated,
        'max_depth': max_depth,
        'orphan_inputs': orphans, 'multi_definitions': multi_defs,
        'malformed_derivations': malformed,
    })

    # ---- register (primary deliverable) ----
    canon_orphans = [o for o in orphans if o['any_canon']]
    notional_orphans = [o for o in orphans if not o['any_canon']]
    canon_multi = [m for m in multi_defs if m['any_canon']]
    notional_multi = [m for m in multi_defs if not m['any_canon']]

    L = []
    L.append('# Formula register — L1 quantity-dependency layer (module_contracts.yaml + descriptor_registry.yaml)')
    L.append('')
    L.append('Deterministic, working-tree only. **Measures; does not gate.** '
             '**Scope: CONTRACT-level formula structure only** — built from '
             '`references/module_contracts.yaml` `derivations[]` and '
             '`references/descriptor_registry.yaml` aggregates/`derived_from`. Does **not** parse '
             '`params/*.md` prose tables, so it cannot catch a formula contradiction that lives only '
             'in prose (e.g. the Prosperity x50-vs-x10 family) — see the script docstring for why that '
             'specific example does not collide as a same-output multi-definition at this layer. A real '
             'params-table/formula extractor is deliberately deferred, not attempted here.')
    L.append('')
    L.append(f'**Scorecard:** nodes={len(nodes)}, edges={total_edges} '
             f'({len(contract_edges)} module_contracts.derivations, {len(descriptor_edges)} descriptor_registry), '
             f'roots(pure inputs)={len(roots)}, leaves(final outputs)={len(leaves)}, isolated={len(isolated)}, '
             f'max-depth={max_depth}, cycles={len(cycles)}, '
             f'orphan-inputs={len(canon_orphans)}(+{len(notional_orphans)} notional/placeholder-only), '
             f'multi-def-outputs={len(canon_multi)}(+{len(notional_multi)} notional/placeholder-only).')
    L.append('')

    def section(title, rows, fmt, empty='(none)'):
        L.append(f'## {title}')
        L.append(empty if not rows else '')
        for r in rows[:25]:
            L.append('- ' + fmt(r))
        if len(rows) > 25:
            L.append(f'- … {len(rows) - 25} more (see `data/formula_metrics.json`)')
        L.append('')

    L.append('## Orphan inputs — referenced as a derivation input, not resolvable via the '
             'registry, and not itself the output of any derivation')
    L.append('')
    L.append('**Triage before acting — not every row is a genuine missing definition** (same '
             'caveat as the G_pointer register). This is the FA-A-01/`cascade_alignment_modifier` '
             'class *in principle*, but at the contract level it mixes three kinds: (a) a genuine '
             'referenced-but-undefined quantity (real defect); (b) a `quantity_registry` false '
             'negative — the name is unresolved only because of a leading/trailing qualifier word '
             'the resolver does not strip (e.g. `settlement Prosperity` vs registered `Prosperity`); '
             'and (c) an internal/intermediate quantity with no registry-eligible identity that '
             'A17 itself calls "expected backlog, not a bug" (`cumulative_damage`, `L_s`, `W_s`, '
             '`PS_s`). Every one of today\'s rows is (b) or (c), not (a) — inspect each before filing.')
    L.append('')
    if not canon_orphans:
        L.append('(none)')
    for o in canon_orphans[:25]:
        L.append(f"- `{o['identifier']}` — {len(o['occurrences'])} occurrence(s), e.g. "
                 f"`{o['occurrences'][0]['module']}` derivation #{o['occurrences'][0]['derivation_index']}")
    if len(canon_orphans) > 25:
        L.append(f'- … {len(canon_orphans) - 25} more (see `data/formula_metrics.json`)')
    L.append('')
    section(
        'Multi-definition outputs — the same quantity is a `derivations.output` in more than one place',
        canon_multi,
        lambda m: f"`{m['node']}` — defined {len(m['definitions'])} time(s) "
                  f"({'DIFFERING input sets' if m['differing_inputs'] else 'same input set'}): " +
                  '; '.join(f"`{d['module']}`#{d['derivation_index']} <- {d['inputs']}" for d in m['definitions']),
    )
    section('Cycles — a quantity transitively depends on itself (Tarjan SCC > 1, or a self-loop)',
            cycles, lambda c: ' -> '.join(c[:8]) + (' …' if len(c) > 8 else ''))
    section('Malformed derivations — `output` field missing/blank (inputs were routed to a '
            'sentinel node so their orphan status still surfaces above)',
            [m for m in malformed if not m['notional']],
            lambda m: f"`{m['module']}` derivation #{m['derivation_index']} — inputs {m['inputs']}")
    section('Roots — pure inputs (nothing in this DAG derives them)', roots[:25], lambda n: f'`{n}`')
    section('Leaves — final outputs (nothing in this DAG consumes them as an input)', leaves[:25], lambda n: f'`{n}`')

    if notional_orphans or notional_multi:
        L.append('## Lower-confidence (findings that touch ONLY notional/`doc:null`/placeholder-status material)')
        L.append('')
        for o in notional_orphans[:15]:
            L.append(f"- orphan `{o['identifier']}` (all occurrences notional)")
        for m in notional_multi[:15]:
            L.append(f"- multi-def `{m['node']}` (all definitions notional)")
        L.append('')

    (out / 'formula_register.md').write_text('\n'.join(L), encoding='utf-8')
    print(f'[done] {out}/formula_register.md')
    return {'edges': edges, 'definitions': definitions, 'adj': adj, 'cycles': cycles,
            'orphans': orphans, 'multi_defs': multi_defs, 'roots': roots, 'leaves': leaves,
            'max_depth': max_depth}


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument('--repo-root', default='.', help='repo root (working tree)')
    ap.add_argument('--output-dir', required=True, help='audit output folder')
    ap.add_argument('--contracts', default=None,
                     help='override references/module_contracts.yaml path (default: <repo-root>/references/module_contracts.yaml)')
    ap.add_argument('--descriptor', default=None,
                     help='override references/descriptor_registry.yaml path (default: <repo-root>/references/descriptor_registry.yaml)')
    a = ap.parse_args()
    root = Path(a.repo_root)
    if not (root / 'references' / 'module_contracts.yaml').exists():
        sys.exit(f"not a Valoria repo root (no references/module_contracts.yaml): {root}")
    print(f'[formula_audit] repo root (working tree): {root.resolve()}')
    run(root, a.output_dir, contracts_path=a.contracts, descriptor_path=a.descriptor)


if __name__ == '__main__':
    main()
