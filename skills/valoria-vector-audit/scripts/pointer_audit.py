#!/usr/bin/env python3
"""
pointer_audit.py — the Structural Observatory's G_pointer layer (WS1 progress meter).

Companion to structure_audit.py (G_code/L2, the architecture layers). This builds the
REGISTRY-RESOLUTION graph + progress meter over the same identifier surfaces A17
(tools/ci_quantity_vocabulary_check.py) already scans: for every stat/quantity
identifier used in the corpus, does it resolve to a references/descriptor_registry.yaml
/ references/names_index.yaml key, or is it hardcoded pointer-debt?

THIS TOOL REUSES A17's RULE — IT DOES NOT REIMPLEMENT IT (CLAUDE.md §8: "every rule
lives once"). Both the identifier scanners and the resolution predicate are imported
from tools/, not re-derived here:
  * tools/quantity_registry.py       -> resolve(name), all_known()   (the resolver)
  * tools/ci_quantity_vocabulary_check.py -> scan_module_contracts(contracts),
                                              scan_sim_literals(sim_root)  (the scanners)
A17 itself decides "resolved vs unresolved" via `quantity_registry.resolve(x)[0] is not
None`; this tool applies that exact same predicate to the exact same scanner output —
it only adds the graph/bucket/scorecard VIEW A17 does not build (A17 is a flat CI
report; this is a graph + a progress meter over the same facts).

Scanned surfaces (identical to A17 — see that module's docstring for the full
rationale, in particular why params/*.md prose tables are NOT scanned here):
  * references/module_contracts.yaml `state[].name`
  * references/module_contracts.yaml `derivations[].output`
  * references/module_contracts.yaml `derivations[].inputs[]`
  * literal `stat_deltas={...}` / `impact_vector={...}` dict keys in sim/*.py

GOVERNANCE (mirrors structure_audit.py):
  * Working tree only; deterministic; no network; stdlib + PyYAML only.
  * MEASURES, NEVER GATES. A17 (`tools/ci_quantity_vocabulary_check.py`) is the CI
    gate (report-only today, per its own docstring's lifecycle note); this script is
    a read-only observatory view over the same facts and asserts nothing about CI.
  * quantity_registry.resolve() is name-based / best-effort against the vocabulary
    files it reads (see that module's docstring); this tool inherits its accuracy and
    its known blind spots (e.g. a variable stat_deltas key, e.g.
    `stat_deltas={er.affected_stat: er.delta}` in
    sim/cross_scale/echo_transport.py, is unresolvable statically and is skipped by
    the scanner it reuses, not flagged — see A17's docstring).
  * Known limitation (stated, not silently dropped): quantity_registry.resolve() has
    no --repo-root override — it always reads the real
    references/descriptor_registry.yaml / references/names_index.yaml next to
    tools/quantity_registry.py, regardless of this script's --repo-root flag (A17 has
    the identical limitation for the same reason: neither module threads a root
    override through the resolver). --repo-root here only relocates which
    module_contracts.yaml / sim/ tree gets *scanned*.

CLI:
    python3 pointer_audit.py --repo-root . --output-dir <run>
"""
import argparse
import json
import os
import sys
from collections import Counter, OrderedDict, defaultdict
from pathlib import Path

try:
    import yaml
except Exception:  # pragma: no cover
    sys.exit("pointer_audit requires PyYAML")

# Import the ONE resolver + the ONE pair of scanners from tools/ — never re-parse
# module_contracts.yaml/sim/*.py or re-derive resolution logic here (CLAUDE.md §8).
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_STATIC_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_SCRIPT_DIR)))
_TOOLS_DIR = os.path.join(_STATIC_REPO_ROOT, 'tools')
if _TOOLS_DIR not in sys.path:
    sys.path.insert(0, _TOOLS_DIR)

import quantity_registry                          # noqa: E402  (the resolver, tools/quantity_registry.py)
import ci_quantity_vocabulary_check as a17         # noqa: E402  (the scanners, A17)


# ──────────────────────────── SURFACE BUCKETS ────────────────────────────────

# The four surfaces named in the WS1 spec, in report order. Any scan surface not
# exactly one of the module_contracts three collapses into 'sim_literals' (today
# that's 'stat_deltas' / 'impact_vector', A17's two literal-dict surfaces).
SURFACE_BUCKETS = (
    'module_contracts.state',
    'module_contracts.derivations.output',
    'module_contracts.derivations.inputs',
    'sim_literals',
)


def _bucket_for(surface):
    return surface if surface in SURFACE_BUCKETS else 'sim_literals'


# ──────────────────────────── COLLECTION (reuse A17's scanners) ─────────────

def collect_occurrences(contracts, sim_root):
    """Every scanned identifier occurrence, resolved via quantity_registry.resolve()
    (A17's exact predicate: `matched_as is not None` => resolved). One record per
    occurrence (NOT deduped) — raw occurrence counts are what make the meter honest.

    Returns a list of dicts: surface, location, raw, identifier, matched_as, key, resolved.
    """
    occurrences = []

    for surface, module, raw, comp in a17.scan_module_contracts(contracts):
        matched, key = quantity_registry.resolve(comp)
        occurrences.append({
            'surface': f'module_contracts.{surface}',
            'location': module,
            'raw': raw,
            'identifier': comp,
            'matched_as': matched,
            'key': key,
            'resolved': matched is not None,
        })

    for surface, path, lineno, name in a17.scan_sim_literals(sim_root):
        matched, key = quantity_registry.resolve(name)
        occurrences.append({
            'surface': f'sim.{surface}',
            'location': f'{path}:{lineno}',
            'raw': name,
            'identifier': name,
            'matched_as': matched,
            'key': key,
            'resolved': matched is not None,
        })

    return occurrences


# ──────────────────────────── G_POINTER GRAPH ────────────────────────────────

def build_g_pointer(occurrences):
    """{identifier: registry_key_or_null} over UNIQUE identifiers (first occurrence
    wins; resolve() is a pure function of the identifier string so this is safe —
    the same raw identifier always resolves the same way).

    NOTE (stated, not silently dropped): `null` here covers TWO different things —
    (1) genuinely unresolved (pointer-debt) and (2) resolved to a `not_descriptors`
    entry, which legitimately has no registry key (a computed/bounded value that is
    deliberately NOT registry-keyed, e.g. a track/clock/pool — see
    quantity_registry.load()'s docstring). This flat map cannot distinguish the two;
    the `resolved` boolean on each occurrence (and the unresolved list / scorecard
    below, which key off that boolean, not off key-nullness) is the authoritative
    signal for the progress meter.
    """
    g = {}
    for o in occurrences:
        ident = o['identifier']
        if ident not in g:
            g[ident] = o['key']
    return g


def resolved_key_buckets(occurrences):
    """Registry keys ranked by occurrence count referencing them — the load-bearing
    pointers. Only counts occurrences that resolved to an ACTUAL key (excludes
    not_descriptors matches, which resolve but carry key=None — those aren't
    pointers into the registry, so they can't be "most-referenced registry keys")."""
    occ_counts = Counter()
    ident_sets = defaultdict(set)
    for o in occurrences:
        if o['resolved'] and o['key']:
            occ_counts[o['key']] += 1
            ident_sets[o['key']].add(o['identifier'])
    buckets = [
        {'key': k, 'occurrences': occ_counts[k], 'unique_identifiers': sorted(ident_sets[k])}
        for k in occ_counts
    ]
    buckets.sort(key=lambda b: (-b['occurrences'], b['key']))
    return buckets


# ──────────────────────────── SCORECARD (the WS1 progress meter) ────────────

def build_scorecard(occurrences):
    """Occurrence-level AND unique-identifier-level resolved/unresolved counts,
    overall and broken down by surface bucket. Both levels are reported side by
    side on purpose: a single hot identifier repeated across many state entries
    would otherwise inflate (or, if unresolved, deflate) an occurrence-only meter."""
    by_surface = OrderedDict((b, {'total': 0, 'resolved': 0, 'unresolved': 0}) for b in SURFACE_BUCKETS)
    for o in occurrences:
        b = by_surface[_bucket_for(o['surface'])]
        b['total'] += 1
        b['resolved' if o['resolved'] else 'unresolved'] += 1
    for b in by_surface.values():
        b['percent_resolved'] = round(100.0 * b['resolved'] / b['total'], 1) if b['total'] else None

    total = sum(b['total'] for b in by_surface.values())
    resolved = sum(b['resolved'] for b in by_surface.values())
    unresolved = total - resolved

    ident_resolved = set()
    ident_unresolved = set()
    for o in occurrences:
        (ident_resolved if o['resolved'] else ident_unresolved).add(o['identifier'])
    # resolve() is deterministic per string, so these two sets are disjoint by construction;
    # assert it rather than silently trusting it (a fabrication-adjacent invariant worth checking).
    overlap = ident_resolved & ident_unresolved
    assert not overlap, f"identifier resolved AND unresolved across occurrences: {overlap}"
    unique_total = len(ident_resolved) + len(ident_unresolved)

    overall = {
        'occurrences_total': total,
        'occurrences_resolved': resolved,
        'occurrences_unresolved': unresolved,
        'percent_resolved_occurrences': round(100.0 * resolved / total, 1) if total else None,
        'unique_identifiers_total': unique_total,
        'unique_identifiers_resolved': len(ident_resolved),
        'unique_identifiers_unresolved': len(ident_unresolved),
        'percent_resolved_unique_identifiers': round(100.0 * len(ident_resolved) / unique_total, 1)
                                                if unique_total else None,
    }
    return {'overall': overall, 'by_surface': by_surface}


def unresolved_pointer_debt(occurrences):
    """(surface, location, identifier) pointer-debt rows, deduped, each carrying its
    raw occurrence count (so dedup for readability never hides the honest count)."""
    counts = Counter((o['surface'], o['location'], o['identifier']) for o in occurrences if not o['resolved'])
    rows = [{'surface': s, 'location': loc, 'identifier': ident, 'occurrences': n}
            for (s, loc, ident), n in counts.items()]
    rows.sort(key=lambda r: (-r['occurrences'], r['surface'], r['location'], r['identifier']))
    return rows


# ──────────────────────────── OUTPUT ─────────────────────────────────────────

def _pct(v):
    """Render a percent that may be None (empty bucket / empty corpus) as an em-dash
    rather than the literal string 'None%'."""
    return f'{v}%' if v is not None else '—'


def run(root, out, contracts_path=None, sim_root=None):
    root, out = Path(root), Path(out)
    (out / 'data').mkdir(parents=True, exist_ok=True)

    contracts_path = Path(contracts_path) if contracts_path else root / 'references' / 'module_contracts.yaml'
    sim_root = Path(sim_root) if sim_root else root / 'sim'

    print('[G_pointer] scanning module_contracts.yaml state/derivations + sim/*.py literals...')
    contracts = yaml.safe_load(contracts_path.read_text(encoding='utf-8')) or {}
    occurrences = collect_occurrences(contracts, str(sim_root))
    print(f'            {len(occurrences)} identifier occurrence(s) scanned '
          f'(reusing tools/ci_quantity_vocabulary_check.py\'s A17 scanners)')

    print('[G_pointer] resolving each identifier via tools/quantity_registry.py...')
    g_pointer = build_g_pointer(occurrences)
    scorecard = build_scorecard(occurrences)
    resolved_buckets = resolved_key_buckets(occurrences)
    debt = unresolved_pointer_debt(occurrences)
    ov = scorecard['overall']
    print(f'            {ov["unique_identifiers_resolved"]}/{ov["unique_identifiers_total"]} unique identifiers '
          f'resolve ({_pct(ov["percent_resolved_unique_identifiers"])}); '
          f'{ov["occurrences_resolved"]}/{ov["occurrences_total"]} occurrences resolve '
          f'({_pct(ov["percent_resolved_occurrences"])})')

    # capstone #5 (ED-IN-0056): `all_known()` returns every RESOLVABLE NAME STRING —
    # aliases included (e.g. "Dexterity", "Agility", "attr.body.agility" all resolve to
    # ONE key). Reporting its length as "known registry vocabulary = N names" reads as
    # "N distinct registered quantities" when the real count of distinct keyed quantities
    # is roughly half. Compute BOTH and label each honestly.
    _name_strings = quantity_registry.all_known()
    _distinct_keys = {quantity_registry.resolve(n)[1] for n in _name_strings}
    _distinct_keys.discard(None)
    n_name_strings = len(_name_strings)
    n_distinct_keys = len(_distinct_keys)

    # ---- JSON ----
    def dump(name, obj):
        (out / 'data' / name).write_text(json.dumps(obj, indent=1, sort_keys=True), encoding='utf-8')

    dump('g_pointer.json', g_pointer)
    dump('pointer_scorecard.json', {
        'overall': scorecard['overall'],
        'by_surface': scorecard['by_surface'],
        'top_resolved_registry_keys': resolved_buckets[:25],
        'unresolved_pointer_debt': debt,
        'known_registry_name_strings': n_name_strings,   # resolvable names incl. aliases
        'distinct_registry_keys': n_distinct_keys,        # distinct keyed quantities (~half)
    })

    # ---- register (primary deliverable) ----
    L = []
    L.append('# Pointer register — G_pointer registry-resolution layer (WS1 progress meter)')
    L.append('')
    L.append('Deterministic, working-tree only. **Measures; does not gate** — the gate is '
             '`tools/ci_quantity_vocabulary_check.py` (A17), report-only today per its own '
             'docstring; this is the graph/meter VIEW over that same check\'s facts, reusing '
             'its scanners (`scan_module_contracts`, `scan_sim_literals`) and '
             '`tools/quantity_registry.py`\'s `resolve()` verbatim — no resolution logic is '
             'reimplemented here.')
    L.append('')
    L.append(f'**Scorecard (progress meter):** '
             f'{ov["unique_identifiers_resolved"]}/{ov["unique_identifiers_total"]} unique identifiers resolved '
             f'({_pct(ov["percent_resolved_unique_identifiers"])}) · '
             f'{ov["occurrences_resolved"]}/{ov["occurrences_total"]} raw occurrences resolved '
             f'({_pct(ov["percent_resolved_occurrences"])}) · '
             f'known registry vocabulary = {n_name_strings} resolvable name strings '
             f'(aliases included) → {n_distinct_keys} distinct registry keys.')
    L.append('')

    L.append('## By surface')
    L.append('')
    L.append('| surface | total | resolved | unresolved | % resolved |')
    L.append('|---|---:|---:|---:|---:|')
    for b, d in scorecard['by_surface'].items():
        pct = f"{d['percent_resolved']}%" if d['percent_resolved'] is not None else '—'
        L.append(f"| `{b}` | {d['total']} | {d['resolved']} | {d['unresolved']} | {pct} |")
    L.append('')

    L.append('## Resolved buckets — load-bearing registry keys (most-referenced pointers)')
    L.append('')
    if not resolved_buckets:
        L.append('(none)')
    for b in resolved_buckets[:20]:
        idents = ', '.join(f'`{i}`' for i in b['unique_identifiers'][:6])
        more = '' if len(b['unique_identifiers']) <= 6 else f" (+{len(b['unique_identifiers']) - 6} more)"
        L.append(f"- `{b['key']}` — {b['occurrences']} occurrence(s), "
                 f"{len(b['unique_identifiers'])} unique identifier(s): {idents}{more}")
    L.append('')

    L.append('## Unresolved identifiers — candidate pointer-debt (surface / location / identifier)')
    L.append('')
    L.append('**Triage before acting — not every row is fixable debt.** This list mixes two kinds '
             '(the resolver cannot tell them apart): (a) genuinely-missing registrations — a stat '
             'name that *should* resolve but is hardcoded (real pointer-debt: register it or rename '
             'it to canonical); and (b) computed/internal quantities with no registry-eligible '
             'identity, which A17\'s own docstring calls out as "a real, expected backlog item, not '
             'a bug" (e.g. `cumulative_damage`, and the `_s`-suffixed intermediates like `L_s`/'
             '`W_s`/`PS_s`). Case (b) is not something to "fix" by registration. `derivations.inputs` '
             'rows skew toward (b); `state`/`derivations.output` rows skew toward (a).')
    L.append('')
    L.append(f'{len(debt)} unique unresolved (surface, location, identifier) row(s), '
             f'{ov["occurrences_unresolved"]} raw occurrence(s), '
             f'{ov["unique_identifiers_unresolved"]} unique identifier(s).')
    L.append('')
    if not debt:
        L.append('(nothing to report — every scanned identifier resolves to the registry)')
    for row in debt[:60]:
        occ_note = '' if row['occurrences'] == 1 else f" (×{row['occurrences']})"
        L.append(f"- [`{row['surface']}`] `{row['location']}`: `{row['identifier']}`{occ_note}")
    if len(debt) > 60:
        L.append(f'- … {len(debt) - 60} more (see `data/pointer_scorecard.json` -> `unresolved_pointer_debt`)')
    L.append('')

    (out / 'pointer_register.md').write_text('\n'.join(L), encoding='utf-8')
    print(f'[done] {out}/pointer_register.md')
    return {'occurrences': occurrences, 'g_pointer': g_pointer, 'scorecard': scorecard,
            'resolved_buckets': resolved_buckets, 'debt': debt}


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument('--repo-root', default='.', help='repo root (working tree)')
    ap.add_argument('--output-dir', required=True, help='audit output folder')
    ap.add_argument('--contracts', default=None,
                     help='override references/module_contracts.yaml path (default: <repo-root>/references/module_contracts.yaml)')
    ap.add_argument('--sim-root', default=None,
                     help='override sim/ root to scan (default: <repo-root>/sim)')
    a = ap.parse_args()
    root = Path(a.repo_root)
    if not (root / 'references' / 'module_contracts.yaml').exists():
        sys.exit(f"not a Valoria repo root (no references/module_contracts.yaml): {root}")
    print(f'[pointer_audit] repo root (working tree): {root.resolve()}')
    run(root, a.output_dir, contracts_path=a.contracts, sim_root=a.sim_root)


if __name__ == '__main__':
    main()
