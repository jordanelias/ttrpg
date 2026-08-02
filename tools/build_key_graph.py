#!/usr/bin/env python3
"""build_key_graph.py — merge the two authored views of the Key graph into ONE typed table.

WHY THIS EXISTS. The Key graph — which subsystem emits which key, and who consumes it — is
currently authored TWICE, independently, and the two views disagree:

  * `systems/_architecture/key_type_registry_v30.md` — 55 key types, each with a payload schema
    plus `emitting_systems` / `consuming_systems`.
  * `references/module_contracts.yaml` — 27 modules, each with `emits` / `consumes`.

MEASURED at first merge: of 47 comparable key types, **20 emitter sets disagree**, 8 declared key
types are referenced by no contract at all, 5 have no consumer in either view, and one "key name"
in the contracts is the literal string `*`. Nothing in the apparatus compared them, so the
architecture has been contradicting itself in public for months while looking finished.

The root cause is a format choice, not carelessness: the registry's `emitting_systems` is FREE
PROSE, so it contains values like `'all subscribing systems'`, `'npc_behavior / Procedure E'`,
`'articulation (low priority)'` and `'...'`. A prose field cannot be joined against a typed one,
which is why no tool ever tried.

WHAT THIS EMITS. `references/key_graph.json` — one row per key type, carrying the payload schema,
the reconciled producer/consumer sets, and, for every row, WHICH VIEW SAID WHAT and whether they
agreed. Disagreement is recorded as data (`reconciliation.status`), never silently resolved: a
merge that quietly picked a winner would manufacture exactly the false confidence this table
exists to remove.

JSON, not YAML, deliberately (Jordan's 2026-08-02 ruling + the Python-first/Godot-port plan):
Python reads it with stdlib and Godot reads it with `JSON.parse_string()` — both first-class, no
GDExtension, no build step for the engine that will consume it. JSON also has no comments, which
forces provenance into a *field* that can be validated rather than a `#` line that cannot.

SCOPE / HONESTY LIMITS, stated rather than discovered later:
  * Producers/consumers are recorded at MODULE granularity (the 27 contract modules), because that
    is the identity both views actually reference. Subsystem homes are carried as a nullable
    column — only 13 of 27 modules declare a `sim_module`, and inventing the other 14 would be
    fabricating design decisions that are open EDs (e.g. `domain_actions`, ED-FA-0002).
  * The alias map below resolves ONLY mappings defensible from evidence in the tree. Everything
    else is left unresolved and surfaces as a conflict for a human. There is no heuristic matching.
"""
from __future__ import annotations

import json
import os
import re
import sys

try:
    import yaml
except ImportError:
    print('[key-graph] pyyaml required', file=sys.stderr)
    raise SystemExit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRY = os.path.join(ROOT, 'systems', '_architecture', 'key_type_registry_v30.md')
CONTRACTS = os.path.join(ROOT, 'references', 'module_contracts.yaml')
OUT = os.path.join(ROOT, 'references', 'key_graph.json')

# Registry prose → canonical contract-module id. EVERY entry cites the evidence that justifies it;
# an alias without evidence is a guess wearing a mapping's clothes.
ALIASES = {
    # `piety_track`'s own contract row declares sim_module systems/characters/sim/conviction.py —
    # i.e. the module the registry calls `conviction_track` IS the one contracts call `piety_track`.
    'conviction_track': 'piety_track',
    # `fieldwork_knots`' contract row declares sim_module systems/fieldwork/sim/knots.py, and the
    # registry uses bare `fieldwork` for the knot-forming keys (meta.knot_formed/ruptured).
    'fieldwork': 'fieldwork_knots',
    # `articulation_layer`'s contract row declares sim_module engine/cross_scale/articulation.py.
    'articulation': 'articulation_layer',
    'articulation (low priority)': 'articulation_layer',
    # `faction_layer` -> `faction_state`, on NUMERIC evidence rather than name similarity: the
    # registry lists `faction_layer` as a consumer of exactly 25 key types, `faction_state`'s
    # contract row declares exactly 25 `consumes`, and `faction_politics` declares ZERO — while the
    # registry names `faction_politics` separately on other keys, so it plainly distinguishes the
    # two. The alternative mapping (faction_politics) would have to explain 25 consumes appearing
    # from a module that declares none.
    'faction_layer': 'faction_state',
    # The registry's name for the domain-action system; `domain_actions` is the contract module,
    # and it declares emits for the same five `da.*` keys the registry attributes to `da_framework`.
    # `da_framework` exists nowhere as a module.
    'da_framework': 'domain_actions',
    # The registry appends a procedure reference to the module name in one free-text field.
    'npc_behavior / Procedure B': 'npc_behavior',
    'npc_behavior / Procedure D': 'npc_behavior',
    'npc_behavior / Procedure E': 'npc_behavior',
}

# Prose that names no module at all. Recorded as an explicit unresolved marker rather than dropped,
# so the count of unresolved references is visible instead of silently shrinking the graph.
NON_REFERENTS = {'...', 'all', 'all subscribing systems', 'legacy-aware consumers only',
                 'substrate (auto)'}

KEY_RE = re.compile(r'^([a-z_]+)\.([a-z_]+)$')


def _canon(name: str):
    """(canonical_id, kind) where kind ∈ resolved | unresolved | non_referent."""
    n = str(name).strip()
    if n in NON_REFERENTS:
        return n, 'non_referent'
    if n in ALIASES:
        return ALIASES[n], 'resolved'
    return n, 'resolved'


def load_registry():
    """{key_type: {...}} from the markdown registry's fenced yaml blocks."""
    txt = open(REGISTRY, encoding='utf-8').read()
    out = {}
    for m in re.finditer(r'^### ([a-z_]+\.[a-z_]+)\s*\n+```yaml\n(.*?)```', txt, re.S | re.M):
        kt, body = m.group(1), m.group(2)
        try:
            y = yaml.safe_load(body) or {}
        except yaml.YAMLError:
            continue
        out[kt] = {
            'description': y.get('description'),
            'required': list(y.get('required_payload_fields') or []),
            'optional': list(y.get('optional_payload_fields') or []),
            'scale': y.get('default_scale_signature'),
            'permanence': y.get('default_permanence'),
            'time_horizon': y.get('default_time_horizon'),
            'emitters': [str(x) for x in (y.get('emitting_systems') or [])],
            'consumers': [str(x) for x in (y.get('consuming_systems') or [])],
        }
    return out


def load_contracts():
    """(modules, emitters, consumers) keyed by module id / key type."""
    d = yaml.safe_load(open(CONTRACTS, encoding='utf-8'))
    rows = d['modules']
    rows = rows if isinstance(rows, list) else list(rows.values())
    modules, em, co = {}, {}, {}
    for r in rows:
        name = r.get('module')
        if not name:
            continue
        sm = str(r.get('sim_module') or '')
        m = re.match(r'systems[/.]([a-z_]+)', sm)
        modules[name] = {
            'sim_module': sm or None,
            # nullable ON PURPOSE — 14 of 27 have no home, and several are open design decisions.
            'subsystem': m.group(1) if m else ('engine' if sm.startswith('engine') else None),
            'doc': r.get('doc'),
            'status': r.get('status'),
        }
        for field, sink in (('emits', em), ('consumes', co)):
            for x in (r.get(field) or []):
                t = x.get('type') if isinstance(x, dict) else x
                if t:
                    sink.setdefault(str(t), set()).add(name)
    return modules, em, co


def build():
    reg = load_registry()
    modules, c_em, c_co = load_contracts()

    keys, unresolved_refs = {}, set()

    def resolve(names):
        out, bad = [], []
        for n in names:
            cid, kind = _canon(n)
            if kind == 'non_referent':
                bad.append(cid)
                unresolved_refs.add(cid)
            else:
                out.append(cid)
                if cid not in modules:
                    unresolved_refs.add(cid)
        return sorted(set(out)), sorted(set(bad))

    for kt in sorted(set(reg) | set(c_em) | set(c_co)):
        r = reg.get(kt, {})
        r_em, r_em_bad = resolve(r.get('emitters') or [])
        r_co, r_co_bad = resolve(r.get('consumers') or [])
        c_e = sorted(c_em.get(kt, set()))
        c_c = sorted(c_co.get(kt, set()))

        def status(a, b):
            """Distinguish DISAGREEMENT from INCOMPLETENESS — they need different human responses.

            A strict subset means one view simply never authored the rows the other has: nobody
            asserted anything contradictory, so it is a filing task, not a decision. A true
            `conflict` is when each side claims something the other denies — only those need
            adjudication. Collapsing both into "conflict" is what made this graph look like 42
            open decisions when it is 2 authoring gaps; the whole point of the distinction is to
            stop a tractable backlog reading as an intractable one.
            """
            sa, sb = set(a), set(b)
            if not sa and not sb:
                return 'absent_both'
            if not sa:
                return 'contracts_only'
            if not sb:
                return 'registry_only'
            if sa == sb:
                return 'agreed'
            if sa < sb:
                return 'contracts_superset'   # registry under-declares
            if sb < sa:
                return 'registry_superset'    # contracts under-declares
            return 'conflict'                 # each asserts what the other omits — a real decision

        keys[kt] = {
            'well_formed': bool(KEY_RE.match(kt)),
            'description': r.get('description'),
            'payload': {'required': r.get('required') or [], 'optional': r.get('optional') or []},
            'scale': r.get('scale'),
            'permanence': r.get('permanence'),
            'time_horizon': r.get('time_horizon'),
            # UNION, not a pick. A merge that chose a winner would fabricate a decision nobody made;
            # the union is the honest superset and `reconciliation` records who claimed what.
            'producers': sorted(set(r_em) | set(c_e)),
            'consumers': sorted(set(r_co) | set(c_c)),
            'reconciliation': {
                'producer_status': status(r_em, c_e),
                'consumer_status': status(r_co, c_c),
                'registry_producers': r_em, 'contract_producers': c_e,
                'registry_consumers': r_co, 'contract_consumers': c_c,
                'non_referent_prose': sorted(set(r_em_bad) | set(r_co_bad)),
            },
        }

    return {
        '_generated': ('GENERATED by tools/build_key_graph.py from '
                       'systems/_architecture/key_type_registry_v30.md + '
                       'references/module_contracts.yaml. NEVER hand-edit: regenerate. '
                       'Conflicts are RECORDED, not resolved — see reconciliation.*_status.'),
        'schema_version': 1,
        'modules': dict(sorted(modules.items())),
        'keys': keys,
        'unresolved_references': sorted(unresolved_refs),
    }


def summarize(g):
    ks = g['keys']
    c = {'total': len(ks)}
    for f in ('producer_status', 'consumer_status'):
        for k, v in ks.items():
            s = v['reconciliation'][f]
            c[f'{f}:{s}'] = c.get(f'{f}:{s}', 0) + 1
    c['no_producer'] = sum(1 for v in ks.values() if not v['producers'])
    c['no_consumer'] = sum(1 for v in ks.values() if not v['consumers'])
    c['malformed'] = sum(1 for v in ks.values() if not v['well_formed'])
    c['modules_without_home'] = sum(1 for m in g['modules'].values() if not m['subsystem'])
    return c


def main():
    g = build()
    write = '--check' not in sys.argv
    if write:
        with open(OUT, 'w', encoding='utf-8') as f:
            json.dump(g, f, indent=1, sort_keys=True)
            f.write('\n')
    s = summarize(g)
    print(f"[key-graph] {s['total']} key types · {len(g['modules'])} modules "
          f"({s['modules_without_home']} without a subsystem home)")
    for k in sorted(s):
        if k.startswith(('producer_status', 'consumer_status')):
            print(f"   {k}: {s[k]}")
    print(f"   keys with NO producer: {s['no_producer']} · NO consumer: {s['no_consumer']} "
          f"· malformed name: {s['malformed']}")
    if g['unresolved_references']:
        print(f"   unresolved references ({len(g['unresolved_references'])}): "
              f"{', '.join(g['unresolved_references'])}")
    if write:
        print(f"   -> {os.path.relpath(OUT, ROOT)}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
