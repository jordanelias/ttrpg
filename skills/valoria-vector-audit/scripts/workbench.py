#!/usr/bin/env python3
"""
workbench.py — the Reconciliation Workbench (R1 prototype).

Program: proposals/2026-07-21-reconciliation-program.md §2. The Workbench holds the ENGINE view
(warp — what the contracts/sim actually wire) beside the PROSE view (weft — what a design doc
articulates) and flags every DIVERGENCE between them as an iteration CARD. Engine and prose are
complementary and iterative: a card is a question a human answers by moving EITHER side; the Workbench
never auto-reconciles.

It is a COMPOSITION, not a new parser (CLAUDE.md §8): the engine side reuses
`structure_audit.build_l2` (module→module Key wiring, provenance/notional) and
`formula_audit.build_contract_edges` (derivation input→output); the prose side reads the module's
design doc from `module_contracts.yaml`'s `doc:` field, resolving a moved path through the
restructure ledger (reusing `broken_dependency_checker._resolve_remap`).

Divergence model (program §1):
  node axis  : prose | engine-live | engine-notional | unbuilt
  edge axis  : co-mentioned | mentioned | silent   (R1's HONEST heuristic for the program's ideal
               articulated/mentioned/silent — 'co-mentioned' == both endpoints co-occur within
               ~PROX chars, a lead the doc may state the link; precise articulation detection needs
               the program §3 canonical-identifier registry, which R1 does not yet have)
  card class : unspecced_wiring | notional_shadow   (this R1 covers the engine→prose direction;
               unrealized_intent — prose claim with no engine edge — is R4 once prose-claim
               extraction exists; it is scaffolded but not emitted here to avoid guessing.)

Cards carry a STABLE id (hash of class+endpoints+relationship) so `references/observatory_dispositions.yaml`
(shared with Augur) can record human answers and the Workbench surfaces only OPEN/CHANGED cards.

MEASURES, never gates. Deterministic, model-free, working-tree only. Prose matching is heuristic
co-occurrence and confidence-tagged — a lead, not a verdict. This is a prototype surface, honest
about its own fuzziness.

Usage:
    python3 workbench.py --repo-root . --module settlement_layer
    python3 workbench.py --repo-root . --module domain_actions              # one-sided / notional demo
    python3 workbench.py --repo-root . --module settlement_layer --output-dir <run>   # write view + cards
  (--entity is RESERVED for R4 per-primitive focus and is currently a no-op.)
"""
import sys
import os
import re
import json
import argparse
import hashlib
from collections import defaultdict

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPT_DIR not in sys.path:
    sys.path.insert(0, _SCRIPT_DIR)
_TOOLS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(_SCRIPT_DIR))), 'tools')
if _TOOLS_DIR not in sys.path:
    sys.path.insert(0, _TOOLS_DIR)

import yaml                               # noqa: E402
import structure_audit as sa             # noqa: E402  (the ONE L2 module-wiring builder)
import formula_audit as fa               # noqa: E402  (the ONE L1 derivation-DAG builder)
try:
    import broken_dependency_checker as bdc   # noqa: E402  (§8: reuse the longest-dir-prefix resolver)
except Exception:                              # pragma: no cover - degrade if tools/ shape changes
    bdc = None
import tag_normalizer as _tags                 # noqa: E402  (§3 keystone: the ONE tag resolver/stripper)
import names as _names                         # noqa: E402  (§8: the ONE names_index reader — registry match forms)

DISPOSITIONS = 'references/observatory_dispositions.yaml'
PROX = 240  # chars — how near two endpoints must co-occur to count as 'co-mentioned' (~1-2 sentences)
_NS = re.compile(r'^[a-z][a-z0-9]*\.')   # a lowercase schema namespace prefix (env. conv. scene. da. set. terr.)


def _restructure_remap(root):
    """Old→new path map from references/restructure_ledger.md (root-honoring). The non-trivial
    longest-dir-prefix RESOLUTION over this map is reused from broken_dependency_checker (§8)."""
    fp = os.path.join(str(root), 'references', 'restructure_ledger.md')
    if not os.path.isfile(fp):
        return {}
    with open(fp, encoding='utf-8', errors='replace') as fh:
        content = fh.read()
    return {m.group(1).strip(): m.group(2).strip()
            for m in re.finditer(r'^\|\s*`([^`]+)`\s*\|\s*`([^`]+)`\s*\|', content, re.M)}


# ──────────────────────────── ENGINE SIDE (warp) ────────────────────────────

def engine_facts(root, module):
    """What the engine wires for `module`, from the contracts. Returns a dict of edges with
    provenance (live vs notional). Reuses build_l2 + build_contract_edges (§8).

    Emits/consumes are read from the module's OWN declared contract entry — NOT reconstructed
    from the consumer-attributed edge list (adversarial Finding 4): edges_meta only carries an
    emit once a KNOWN module consumes it, so a dangling emit — declared but unconsumed — would
    silently vanish. We read the declaration and ANNOTATE each emit with its real consumers."""
    from pathlib import Path
    root = Path(root)
    g, meta, edges_meta, _find, _assump = sa.build_l2(root)
    with open(root / 'references' / 'module_contracts.yaml', encoding='utf-8') as fh:
        contracts = yaml.safe_load(fh) or {}
    fa_edges, _defs = fa.build_contract_edges(contracts)

    m_meta = meta.get(module, {})
    node_state = ('unbuilt' if module not in meta else
                  'engine-notional' if m_meta.get('notional') else 'engine-live')

    entry = next((m for m in (contracts.get('modules') or [])
                  if isinstance(m, dict) and m.get('module') == module), {})
    consumers_of = defaultdict(list)               # (emitter, key) -> [consumer modules]
    for e in edges_meta:
        consumers_of[(e['src'], e['type'])].append(e['dst'])

    emits = []
    for e in (entry.get('emits') or []):
        if not isinstance(e, dict) or not e.get('type'):
            continue
        dsts = sorted(set(consumers_of.get((module, e['type']), [])))
        emits.append({'key': e['type'], 'to': dsts, 'terminal': bool(e.get('terminal')),
                      'wired': bool(dsts)})
    consumes = []
    for c in (entry.get('consumes') or []):
        if not isinstance(c, dict) or not c.get('type') or c.get('type') == '*':
            continue
        froms = c.get('from')
        froms = list(froms) if isinstance(froms, list) else ([froms] if froms else [])
        consumes.append({'key': c['type'], 'from': froms})

    derivations = [{'output': e['dst'], 'input': e['src'], 'notional': bool(e.get('notional'))}
                   for e in fa_edges if e.get('module') == module]
    return {'module': module, 'node_state': node_state, 'doc': m_meta.get('doc'),
            'notional': bool(m_meta.get('notional')), 'resolver': m_meta.get('resolver'),
            'emits': emits, 'consumes': consumes, 'derivations': derivations,
            'meta': meta}


# ──────────────────────────── PROSE SIDE (weft) ─────────────────────────────

def _resolve_doc(root, doc_rel):
    """Resolve a module's design doc to (text, status). Distinguishes the two states the old
    _read_doc CONFLATED (adversarial Finding 2):
      'none'     — the contract declares no doc (doc:null). Built-but-unspecced is legitimate.
      'declared' — the declared path exists and was read.
      'remapped' — the declared path moved; found at its restructure-ledger home and read.
      'missing'  — declared but not on disk even after the ledger. A BROKEN pointer — a louder,
                   different problem than 'no doc', surfaced distinctly by render().
    Reuses broken_dependency_checker._resolve_remap for the longest-dir-prefix resolution (§8)."""
    if not doc_rel:
        return None, 'none'
    p = os.path.join(str(root), doc_rel)
    if os.path.isfile(p):
        with open(p, encoding='utf-8', errors='replace') as fh:
            return _tags.strip(fh.read()), 'declared'
    if os.path.isdir(p):
        # a DIRECTORY-valued doc (e.g. personal_combat -> systems/combat/combat_engine_v1/): the
        # design lives across the dir's .md files — concatenate them so prose matching sees the
        # whole corpus, not a spurious 'missing'. (Only personal_combat uses this today.)
        mds = sorted(f for f in os.listdir(p) if f.endswith('.md'))
        if mds:
            parts = []
            for f in mds:
                with open(os.path.join(p, f), encoding='utf-8', errors='replace') as fh:
                    parts.append(fh.read())
            return _tags.strip('\n\n'.join(parts)), 'declared-dir'
    if bdc is not None:
        remapped = bdc._resolve_remap(doc_rel, _restructure_remap(root))
        if remapped:
            rp = os.path.join(str(root), remapped)
            if os.path.isfile(rp):
                with open(rp, encoding='utf-8', errors='replace') as fh:
                    return _tags.strip(fh.read()), 'remapped'
    return None, 'missing'


def _surface_forms(term):
    """Specific surface forms of a namespaced token, literal first. The literal token
    (`env.disaster`, `peninsular_strain`, `set.order`) always counts. A humanized form drops a
    leading schema namespace and turns _/. into spaces (`env.population_change` → 'population
    change'); it is used ONLY as a whole phrase, and a LONE humanized word must be ≥4 chars — we
    do NOT fall back to a common tail word, which is what let `env.disaster` match any 'disaster'
    in rich prose (adversarial Finding 1)."""
    forms = [(term, False)]                                   # (surface, case_insensitive)
    human = _NS.sub('', term).replace('_', ' ').replace('.', ' ').strip()
    if human and human.lower() != term.lower():
        words = human.split()
        if len(words) >= 2 or (len(words) == 1 and len(words[0]) >= 4):
            forms.append((human, True))
    # registry-backed forms (§3 canonical identifiers): if `term` is a names_index id or a known
    # display, add its canonical + aliases as PRECISE surface forms — a POINTER into the central
    # registry, not a guess. Pure gain: the registry supplies real aliases the humanizer cannot
    # infer (e.g. attr.mind.will → 'Spirit'). Unregistered engine ids (module names, Key types)
    # keep the heuristic humanize above.
    key = term if _names.canonical(term) else _names.key_for(term)
    if key and _names.canonical(key):
        for surf in [_names.canonical(key)] + list(_names.aliases(key)):
            if surf and (surf, True) not in forms and (surf, False) not in forms:
                forms.append((surf, True))
    return forms


def _positions(text, term):
    """Start offsets of every accepted surface form of `term` in `text` (word-boundary; literal
    case-sensitive, humanized case-insensitive). Positions let articulation() require PROXIMITY
    for the top state, so a lone word can never by itself manufacture a co-mention."""
    if not text or not term:
        return []
    pos = []
    for surface, ci in _surface_forms(term):
        if not surface:
            continue
        for mm in re.finditer(r'(?<!\w)' + re.escape(surface) + r'(?!\w)', text, re.I if ci else 0):
            pos.append(mm.start())
    return sorted(set(pos))


def _mentions(text, term):
    return bool(_positions(text, term))


def articulation(text, counterpart, relationship):
    """How prose expresses an engine relationship: co-mentioned / mentioned / silent.
    Heuristic co-occurrence, confidence-tagged — NOT semantic link detection:
      'co-mentioned' — counterpart AND relationship term appear within ~PROX chars (a lead the
                       doc may state the link);
      'mentioned'    — the counterpart appears, but the relationship term is absent or far;
      'silent'       — the counterpart is absent from the doc.
    Precise articulation detection needs the program §3 canonical-identifier registry — until
    then these are leads, not verdicts (see render()'s caveat)."""
    if text is None:
        return {'state': 'silent', 'confidence': 'n/a (no doc)'}
    cp = _positions(text, counterpart)
    if not cp:
        return {'state': 'silent', 'confidence': 'medium (endpoint absent from doc)'}
    # a self-relationship (dangling emit: the key IS the counterpart) has no second endpoint to
    # co-locate — presence is the most we can honestly claim.
    if not relationship or relationship == counterpart:
        return {'state': 'mentioned', 'confidence': 'medium (emitted key named in doc)'}
    rel = _positions(text, relationship)
    if rel and any(abs(c - r) <= PROX for c in cp for r in rel):
        return {'state': 'co-mentioned',
                'confidence': f'low (endpoints co-occur within ~{PROX} chars; link inferred, not verified)'}
    if rel:
        return {'state': 'mentioned', 'confidence': 'low (both present but far apart — link unstated)'}
    return {'state': 'mentioned', 'confidence': 'medium (endpoint present, relationship term absent)'}


# ──────────────────────────── DIVERGENCE CARDS ──────────────────────────────

def _card_id(cls, module, counterpart, rel):
    h = hashlib.sha1(f'{cls}|{module}|{counterpart}|{rel}'.encode()).hexdigest()[:10]
    return f'wb-{h}'


def weave(root, module):
    """Cross the two sides → the two-sided rows + divergence cards for `module`.
    Returns (eng, has_doc, cards, rows); eng carries eng['doc_status'] (none/declared/remapped/
    missing) so render() can surface a BROKEN doc pointer loudly, distinct from 'no doc'."""
    eng = engine_facts(root, module)
    text, doc_status = _resolve_doc(root, eng['doc'])
    eng['doc_status'] = doc_status
    has_doc = doc_status in ('declared', 'remapped', 'declared-dir')
    notional_node = eng['notional'] or eng['node_state'] != 'engine-live'
    cards = []
    rows = []
    seen_rows, seen_cards = set(), set()

    def add(cls, counterpart, rel, art, edge_notional=False):
        # notional endpoints/edges down-rank to notional_shadow (guard fabricated contract rows).
        # An edge's OWN notional flag matters even when the counterpart is a scalar, not a module,
        # so meta.get(counterpart) misses (adversarial Finding 3).
        cp_notional = eng['meta'].get(counterpart, {}).get('notional', False)
        shadow = notional_node or cp_notional or edge_notional
        klass = 'notional_shadow' if shadow else cls
        cid = _card_id(klass, module, counterpart, rel)
        if cid in seen_cards:                                 # dedup identical edges (Finding 6)
            return
        seen_cards.add(cid)
        q = (f"Engine wires {module} {rel} {counterpart}; prose is '{art['state']}'. "
             + ("This contract row is itself notional/[ASSUMPTION] — CONFIRM it's real before "
                "reconciling to it." if shadow else
                "Articulate it in the design — or should the engine not do this?"))
        cards.append({'id': cid, 'class': klass, 'module': module, 'counterpart': counterpart,
                      'relationship': rel, 'prose': art, 'shadow': shadow, 'question': q})

    def edge(engine_str, counterpart, rel_label, rel_term, kind, edge_notional=False):
        art = articulation(text, counterpart, rel_term)
        if engine_str not in seen_rows:                       # dedup identical rows (Finding 6)
            seen_rows.add(engine_str)
            rows.append({'engine': engine_str, 'state': art['state']})
        if art['state'] != 'co-mentioned':
            add(kind, counterpart, rel_label, art, edge_notional=edge_notional)

    for e in eng['emits']:
        if e['to']:
            for dst in e['to']:
                edge(f"emits `{e['key']}` → {dst}", dst, f"emits [{e['key']}] to", e['key'],
                     'unspecced_wiring')
        else:
            # dangling emit: declared but no known module consumes it (engine finding). No target
            # module — articulation reduces to 'is this emitted key named in the doc'.
            tag = ' (terminal)' if e['terminal'] else ' (dangling — unconsumed)'
            edge(f"emits `{e['key']}`{tag}", e['key'], f"emits [{e['key']}]", None,
                 'unspecced_wiring')
    for c in eng['consumes']:
        for src in (c['from'] or [None]):
            cp = src if src else c['key']
            estr = (f"consumes `{c['key']}` ← {src}" if src
                    else f"consumes `{c['key']}` (source unspecified)")
            edge(estr, cp, f"consumes [{c['key']}] from", (c['key'] if src else None),
                 'unspecced_wiring')
    for d in eng['derivations']:
        edge(f"`{d['output']}` ← `{d['input']}`", d['input'], f"derives [{d['output']}] from",
             d['output'], 'unspecced_wiring', edge_notional=d['notional'])

    return eng, has_doc, cards, rows


# ──────────────────────────── DISPOSITIONS (memory) ─────────────────────────

def load_dispositions(root):
    p = os.path.join(str(root), DISPOSITIONS)
    if not os.path.isfile(p):
        return {}
    with open(p, encoding='utf-8', errors='replace') as fh:
        d = yaml.safe_load(fh) or {}
    return d.get('cards', {}) if isinstance(d, dict) else {}


def partition(cards, dispositions):
    """Open (new/unanswered) vs resolved (human-answered in the dispositions file)."""
    open_, resolved = [], []
    for c in cards:
        ans = dispositions.get(c['id'])
        (resolved if ans else open_).append({**c, 'disposition': ans})
    return open_, resolved


# ──────────────────────────── RENDER ────────────────────────────────────────

_STATE_MARK = {'co-mentioned': '~ co-mentioned (endpoints near; link inferred)',
               'mentioned': '~ mentioned (endpoint only)', 'silent': '✗ silent'}


def render(eng, has_doc, rows, open_cards, resolved_cards):
    L = []
    L.append(f"# Workbench — {eng['module']}")
    L.append('')
    doc_status = eng.get('doc_status', 'none')
    if doc_status == 'missing':
        doc_bit = f" · **doc: BROKEN pointer `{eng['doc']}` (declared, not on disk)**"
    elif doc_status == 'remapped':
        doc_bit = f" · doc `{eng['doc']}` (moved; read via restructure ledger)"
    elif doc_status == 'declared-dir':
        doc_bit = f" · doc `{eng['doc']}` (directory — all .md files concatenated)"
    elif eng['doc']:
        doc_bit = f" · doc `{eng['doc']}`"
    else:
        doc_bit = ' · **doc: none declared**'
    L.append(f"**node:** {eng['node_state']}"
             + (f" · resolver `{eng['resolver']}`" if eng['resolver'] else '') + doc_bit)
    co = sum(1 for r in rows if r['state'] == 'co-mentioned')
    L.append('')
    if doc_status == 'missing':
        note = " — _declared design doc is MISSING (broken pointer); every edge reads silent_"
    elif not has_doc:
        note = " — _no design doc declared; every edge is silent (built-but-unspecced)_"
    else:
        note = ""
    L.append(f"**responsiveness:** {co}/{len(rows)} engine edges co-mentioned in prose (heuristic)"
             + note)
    L.append('')
    L.append('| ENGINE (warp — what the contracts wire) | PROSE (weft) |')
    L.append('|---|---|')
    for r in rows:
        mark = 'no doc' if not has_doc else _STATE_MARK.get(r['state'], r['state'])
        L.append(f"| {r['engine']} | _{mark}_ |")
    if not rows:
        L.append("| _(engine wires nothing for this module)_ | — |")
    L.append('')
    L.append(f"## Divergence cards — {len(open_cards)} open · {len(resolved_cards)} resolved")
    L.append("_Each card is an iteration point. Resolve by moving EITHER side (articulate the prose, "
             "or change the engine); record the answer in `references/observatory_dispositions.yaml`._")
    L.append('')
    for c in open_cards:
        tag = ' ⚠shadow' if c['shadow'] else ''
        L.append(f"- **[{c['class']}]{tag}** `{c['id']}` — {c['question']}")
        L.append(f"  - prose: _{c['prose']['state']}_ ({c['prose']['confidence']})")
    if not open_cards:
        L.append("- _(no open divergences — engine and prose agree, or all cards dispositioned)_")
    if resolved_cards:
        L.append('')
        L.append(f"### Resolved ({len(resolved_cards)}) — carried for provenance")
        for c in resolved_cards:
            L.append(f"- `{c['id']}` — {c['disposition']}")
    L.append('')
    L.append("_Prototype (R1). Prose matching is heuristic co-occurrence (word-boundary literal + "
             "namespace-stripped phrase, proximity-gated), confidence-tagged — a LEAD, not a verdict. "
             "Precise articulation detection needs the program §3 canonical-identifier registry. "
             "MEASURES, never gates._")
    return '\n'.join(L)


# ──────────────────────────── CLI ───────────────────────────────────────────

def run(root, module):
    eng, has_doc, cards, rows = weave(root, module)
    disp = load_dispositions(root)
    open_, resolved = partition(cards, disp)
    return eng, has_doc, rows, open_, resolved


def main():
    ap = argparse.ArgumentParser(description='The Workbench — engine↔prose reconciliation workbench (R1).')
    ap.add_argument('--repo-root', default='.')
    ap.add_argument('--module', required=True, help='the module/subsystem to weave')
    ap.add_argument('--entity', default=None, help='(reserved for R4 per-primitive focus; no-op)')
    ap.add_argument('--output-dir', default=None, help='write workbench_<module>.md + cards json here')
    args = ap.parse_args()

    contracts = os.path.join(args.repo_root, 'references', 'module_contracts.yaml')
    if not os.path.isfile(contracts):
        ap.error(f'not a repo root (missing {contracts})')

    eng, has_doc, rows, open_, resolved = run(args.repo_root, args.module)
    view = render(eng, has_doc, rows, open_, resolved)

    if args.output_dir:
        from pathlib import Path
        out = Path(args.output_dir)
        (out / 'data').mkdir(parents=True, exist_ok=True)
        (out / f'workbench_{args.module}.md').write_text(view, encoding='utf-8')
        (out / 'data' / f'workbench_{args.module}_cards.json').write_text(
            json.dumps({'module': args.module, 'node_state': eng['node_state'],
                        'doc_status': eng.get('doc_status'),
                        'open': open_, 'resolved': resolved}, indent=1, sort_keys=True),
            encoding='utf-8')
        print(f"[workbench] {args.module}: {len(open_)} open cards, {len(resolved)} resolved -> {out}")
    else:
        print(view)
    return 0


if __name__ == '__main__':
    sys.exit(main())
