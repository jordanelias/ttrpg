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
design doc from `module_contracts.yaml`'s `doc:` field.

Divergence model (program §1):
  node axis  : prose | engine-live | engine-notional | unbuilt
  edge axis  : articulated | mentioned | silent   (how prose expresses each engine relationship)
  card class : unspecced_wiring | notional_shadow   (this R1 covers the engine→prose direction;
               unrealized_intent — prose claim with no engine edge — is R4 once prose-claim
               extraction exists; it is scaffolded but not emitted here to avoid guessing.)

Cards carry a STABLE id (hash of class+endpoints+relationship) so `references/observatory_dispositions.yaml`
(shared with Augur) can record human answers and the Workbench surfaces only OPEN/CHANGED cards.

MEASURES, never gates. Deterministic, model-free, working-tree only. Prose matching is heuristic
and confidence-tagged — this is a prototype surface, honest about its own fuzziness.

Usage:
    python3 workbench.py --repo-root . --module settlement_layer
    python3 workbench.py --repo-root . --module domain_actions --entity Muster   # one-sided / notional demo
    python3 workbench.py --repo-root . --module settlement_layer --output-dir <run>   # write view + cards
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

DISPOSITIONS = 'references/observatory_dispositions.yaml'


# ──────────────────────────── ENGINE SIDE (warp) ────────────────────────────

def engine_facts(root, module):
    """What the engine wires for `module`, from the contracts. Returns a dict of edges with
    provenance (live vs notional). Reuses build_l2 + build_contract_edges (§8)."""
    from pathlib import Path
    root = Path(root)
    g, meta, edges_meta, _find, _assump = sa.build_l2(root)
    with open(root / 'references' / 'module_contracts.yaml', encoding='utf-8') as fh:
        contracts = yaml.safe_load(fh) or {}
    fa_edges, _defs = fa.build_contract_edges(contracts)

    m_meta = meta.get(module, {})
    node_state = ('unbuilt' if module not in meta else
                  'engine-notional' if m_meta.get('notional') else 'engine-live')

    emits = [{'key': e['type'], 'to': e['dst']} for e in edges_meta if e.get('src') == module]
    consumes = [{'key': e['type'], 'from': e['src']} for e in edges_meta if e.get('dst') == module]
    derivations = [{'output': e['dst'], 'input': e['src'], 'notional': bool(e.get('notional'))}
                   for e in fa_edges if e.get('module') == module]
    return {'module': module, 'node_state': node_state, 'doc': m_meta.get('doc'),
            'notional': bool(m_meta.get('notional')), 'resolver': m_meta.get('resolver'),
            'emits': emits, 'consumes': consumes, 'derivations': derivations,
            'meta': meta}


# ──────────────────────────── PROSE SIDE (weft) ─────────────────────────────

def _read_doc(root, doc_rel):
    if not doc_rel:
        return None
    p = os.path.join(str(root), doc_rel)
    if not os.path.isfile(p):
        return None
    with open(p, encoding='utf-8', errors='replace') as fh:
        return fh.read()


def _mentions(text, term):
    """Word-ish boundary, case-sensitive first then humanized fallback. Prototype heuristic."""
    if not text or not term:
        return False
    if re.search(r'(?<!\w)' + re.escape(term) + r'(?!\w)', text):
        return True
    human = re.sub(r'[_.]', ' ', term)                       # scene.gossip -> "scene gossip"
    tail = human.split()[-1] if human.split() else ''
    return bool(tail and len(tail) >= 4 and re.search(r'(?<!\w)' + re.escape(tail) + r'(?!\w)', text, re.I))


def articulation(text, counterpart, relationship):
    """How prose expresses an engine relationship: articulated / mentioned / silent.
    Confidence-tagged — this is heuristic co-mention, not semantic understanding."""
    if text is None:
        return {'state': 'silent', 'confidence': 'n/a (no doc)'}
    cp = _mentions(text, counterpart)
    rel = _mentions(text, relationship)
    if cp and rel:
        return {'state': 'articulated', 'confidence': 'low (co-mention, not verified link)'}
    if cp:
        return {'state': 'mentioned', 'confidence': 'medium (endpoint present, relationship unstated)'}
    return {'state': 'silent', 'confidence': 'medium (endpoint absent from doc)'}


# ──────────────────────────── DIVERGENCE CARDS ──────────────────────────────

def _card_id(cls, module, counterpart, rel):
    h = hashlib.sha1(f'{cls}|{module}|{counterpart}|{rel}'.encode()).hexdigest()[:10]
    return f'wb-{h}'


def weave(root, module):
    """Cross the two sides → the two-sided rows + divergence cards for `module`."""
    eng = engine_facts(root, module)
    text = _read_doc(root, eng['doc'])
    notional_node = eng['notional'] or eng['node_state'] != 'engine-live'
    cards = []
    rows = []  # every engine edge with its prose-articulation state (the two-sided table)

    def add(cls, counterpart, rel, art, extra=''):
        # notional endpoints down-rank to notional_shadow (guard the ED-MB-0010 fabricated class)
        cp_notional = eng['meta'].get(counterpart, {}).get('notional', False)
        shadow = notional_node or cp_notional
        klass = 'notional_shadow' if shadow else cls
        q = (f"Engine wires {module} {rel} {counterpart}; prose is '{art['state']}'. "
             + ("This contract row is itself notional/[ASSUMPTION] — CONFIRM it's real before "
                "reconciling to it." if shadow else
                "Articulate it in the design — or should the engine not do this?"))
        cards.append({'id': _card_id(klass, module, counterpart, rel), 'class': klass,
                      'module': module, 'counterpart': counterpart, 'relationship': rel,
                      'prose': art, 'shadow': shadow, 'question': q, 'note': extra})

    def edge(engine_str, counterpart, rel_label, rel_term, kind):
        art = articulation(text, counterpart, rel_term)
        rows.append({'engine': engine_str, 'state': art['state']})
        if art['state'] != 'articulated':
            add(kind, counterpart, rel_label, art)

    for e in eng['emits']:
        edge(f"emits `{e['key']}` → {e['to']}", e['to'], f"emits [{e['key']}] to", e['key'], 'unspecced_wiring')
    for c in eng['consumes']:
        edge(f"consumes `{c['key']}` ← {c['from']}", c['from'], f"consumes [{c['key']}] from", c['key'], 'unspecced_wiring')
    for d in eng['derivations']:
        edge(f"`{d['output']}` ← `{d['input']}`", d['input'], f"derives [{d['output']}] from", d['output'], 'unspecced_wiring')

    return eng, text is not None, cards, rows


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

_STATE_MARK = {'articulated': '✓ articulated', 'mentioned': '~ mentioned (link unstated)',
               'silent': '✗ silent'}


def render(eng, has_doc, rows, open_cards, resolved_cards):
    L = []
    L.append(f"# Workbench — {eng['module']}")
    L.append('')
    L.append(f"**node:** {eng['node_state']}"
             + (f" · resolver `{eng['resolver']}`" if eng['resolver'] else '')
             + (f" · doc `{eng['doc']}`" if eng['doc'] else ' · **doc: none**'))
    art = sum(1 for r in rows if r['state'] == 'articulated')
    L.append('')
    L.append(f"**responsiveness:** {art}/{len(rows)} engine edges articulated in prose"
             + ("" if has_doc else " — _no design doc; every edge is silent (built-but-unspecced)_"))
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
    L.append("_Prototype (R1). Prose matching is heuristic co-mention, confidence-tagged — a lead, "
             "not a verdict. MEASURES, never gates._")
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
    ap.add_argument('--entity', default=None, help='(reserved) focus one primitive/action/effect')
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
                        'open': open_, 'resolved': resolved}, indent=1, sort_keys=True),
            encoding='utf-8')
        print(f"[workbench] {args.module}: {len(open_)} open cards, {len(resolved)} resolved -> {out}")
    else:
        print(view)
    return 0


if __name__ == '__main__':
    sys.exit(main())
