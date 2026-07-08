#!/usr/bin/env python3
"""
ci_quantity_vocabulary_check.py — A17 stat-vocabulary closure (report-only).

Implements A17 from the quantity-layer extension of the Key & Echo Armature
(designs/audit/2026-07-08-attribute-value-coherence-audit/
proposed_quantity_armature_extension.md §3.1, ED-IN-0029 — the mechanical rows
OPT-AV-4/OPT-AV-16 executed by direct Jordan instruction; the docket's
design-naming forks, e.g. OPT-AV-1/9/10/11/12/13/15/18, remain OPEN and are
NOT decided by this tool).

Mechanical predicate: every stat identifier appearing in (a)
references/module_contracts.yaml `state[].name` / `derivations[].output` /
`derivations[].inputs[]`, and (b) literal `stat_deltas={...}` /
`impact_vector={...}` dict keys in sim/*.py, resolves (directly or via a
declared alias) to a references/descriptor_registry.yaml key or a
references/names_index.yaml canonical/alias — via tools/quantity_registry.py,
the single reader for that merged vocabulary.

Report-only, same lifecycle as A1-A16 (armature §4): land report-only, burn
the backlog via a shaping wave, flip to blocking at zero backlog (armature §4
/ extension §3, OPT-AV-6). CI wires this with a STEP-level continue-on-error
(the contract_adjudicator precedent) — this script itself still exits 1 on
any unresolved identifier so a local run is informative.

Known scope limits (stated, not silently dropped — CLAUDE.md workflow ethic):
  * params/*.md prose tables are NOT scanned here. A17's own spec (extension
    §3.1) lists them as an input surface, but resolving free-form markdown
    table rows needs a real table extractor — that is A18's prose-drift
    detector (extension §3.2), sequenced AFTER this check. Scanning params/
    naively here would be noise-dominated; better to under-report than to
    ship an unreliable heuristic as the first measurement.
  * Only LITERAL string dict keys in stat_deltas={...}/impact_vector={...}
    call sites are checkable — a variable key (e.g.
    `stat_deltas={er.affected_stat: er.delta}`, the one live call site in
    sim/cross_scale/echo_transport.py today) cannot be resolved statically
    and is skipped, not flagged.
  * `derivations[].inputs[]` entries that name a computed/internal quantity
    with no registry-eligible identity (e.g. "cumulative_damage") will report
    as unresolved like everything else — that's a real, expected backlog
    item, not a bug in this checker.

CLI:
    python tools/ci_quantity_vocabulary_check.py
        [--contracts references/module_contracts.yaml] [--sim-root sim]
"""
import argparse
import os
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("ci_quantity_vocabulary_check requires PyYAML")

try:
    import quantity_registry
except ImportError:  # allow `python tools/ci_quantity_vocabulary_check.py` from repo root
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import quantity_registry

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

_STAT_DICT_RE = re.compile(r'(stat_deltas|impact_vector)\s*=\s*\{([^{}]*)\}')
_STR_KEY_RE = re.compile(r'''["']([^"']+)["']\s*:''')


def _split_bundled(name):
    """Split a bundled 'A / B / C' state/derivation name into components
    (mirrors contract_adjudicator.py's A11 handling of the same convention)."""
    return [c.strip() for c in (name or '').split('/') if c.strip()]


def scan_module_contracts(contracts):
    """Yields (surface, module, raw_name, component) for every stat identifier
    named in module_contracts.yaml state[]/derivations[]."""
    for m in contracts.get('modules', []) or []:
        name = m.get('module', '?')
        for st in m.get('state', []) or []:
            raw = st.get('name')
            for comp in _split_bundled(raw):
                yield ('state', name, raw, comp)
        for d in m.get('derivations', []) or []:
            out = d.get('output')
            for comp in _split_bundled(out):
                yield ('derivations.output', name, out, comp)
            for inp in d.get('inputs', []) or []:
                for comp in _split_bundled(inp):
                    yield ('derivations.inputs', name, inp, comp)


def scan_sim_literals(sim_root):
    """Yields (surface, file, lineno, raw_name) for every literal string key
    in a stat_deltas={...} or impact_vector={...} call-site dict."""
    for dirpath, _dirnames, filenames in os.walk(sim_root):
        if any(part in ('__pycache__', 'tests') for part in dirpath.replace(os.sep, '/').split('/')):
            continue
        for fn in filenames:
            if not fn.endswith('.py'):
                continue
            path = os.path.join(dirpath, fn)
            try:
                text = open(path, encoding='utf-8').read()
            except OSError:
                continue
            for m in _STAT_DICT_RE.finditer(text):
                surface, body = m.group(1), m.group(2)
                lineno = text.count('\n', 0, m.start()) + 1
                for km in _STR_KEY_RE.finditer(body):
                    yield (surface, os.path.relpath(path, REPO_ROOT), lineno, km.group(1))


def check(contracts, sim_root):
    """Returns (resolved_count, findings) where findings is a list of dicts."""
    findings = []
    resolved = 0

    for surface, module, raw, comp in scan_module_contracts(contracts):
        matched, key = quantity_registry.resolve(comp)
        if matched is None:
            findings.append({
                'surface': f'module_contracts.yaml:{surface}', 'module': module,
                'raw': raw, 'identifier': comp,
            })
        else:
            resolved += 1

    for surface, path, lineno, name in scan_sim_literals(sim_root):
        matched, key = quantity_registry.resolve(name)
        if matched is None:
            findings.append({
                'surface': f'sim:{surface}', 'module': f'{path}:{lineno}',
                'raw': name, 'identifier': name,
            })
        else:
            resolved += 1

    return resolved, findings


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--contracts', default=os.path.join(REPO_ROOT, 'references', 'module_contracts.yaml'))
    ap.add_argument('--sim-root', default=os.path.join(REPO_ROOT, 'sim'))
    a = ap.parse_args(argv)

    contracts = yaml.safe_load(open(a.contracts, encoding='utf-8')) or {}
    resolved, findings = check(contracts, a.sim_root)

    total = resolved + len(findings)
    print(f"== ci_quantity_vocabulary_check (A17): {len(findings)} unresolved / {total} scanned "
          f"stat identifier(s) — report-only, seed backlog re-derivation ==")
    for f in findings:
        print(f"  UNRESOLVED [{f['surface']}] {f['module']}: {f['identifier']!r} "
              f"(from {f['raw']!r})")
    if not findings:
        print("  (nothing to report — every scanned identifier resolves to the registry)")
    return 1 if findings else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
