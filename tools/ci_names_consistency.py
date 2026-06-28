#!/usr/bin/env python3
"""
ci_names_consistency.py — names_index.yaml is authoritative; mirrors must match it.

During the (deliberately incremental) migration, references/descriptor_registry.yaml
and references/proper_noun_registry.yaml still carry `name`/`canonical` fields. This
gate asserts those mirror fields equal the `canonical` in references/names_index.yaml,
so the index stays the single source of truth and the mirrors cannot silently drift.
(Removing the mirror fields entirely is a follow-up; until then this keeps them honest.)

Mapping (by index-key prefix):
    attr.* / agg.* / fac.* / set.*  -> descriptor_registry.yaml  (`key` -> `name`)
    proper_noun entries (e.g. world.solmund) -> proper_noun_registry.yaml (last segment -> `canonical`)

Mechanic/clock/track/substrate entries have no registry mirror (they drive the drift
lint + rename, not a mirror) and are skipped.

Whole-tree gate (no diff needed). Exit 1 on any mismatch or missing mirror.

CLI:
    python tools/ci_names_consistency.py
"""
import os
import sys

try:
    import yaml
except ImportError:
    print("ci_names_consistency: PyYAML not available; cannot validate. (install pyyaml)")
    sys.exit(1)

try:
    import names
except ImportError:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import names

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESCRIPTOR = os.path.join(_ROOT, 'references', 'descriptor_registry.yaml')
PROPER_NOUN = os.path.join(_ROOT, 'references', 'proper_noun_registry.yaml')


def _load(path):
    with open(path, encoding='utf-8') as f:
        return yaml.safe_load(f) or {}


def descriptor_names():
    """Flat {key: name} from descriptor_registry's keyed descriptor lists."""
    d = _load(DESCRIPTOR)
    out = {}
    attrs = d.get('attributes', {})
    for group in ('body', 'mind', 'social'):
        for e in (attrs.get(group) or []):
            if isinstance(e, dict) and 'key' in e:
                out[e['key']] = e.get('name')
    for section in ('aggregates', 'faction_stats', 'settlement_stats'):
        for e in ((d.get(section) or {}).get('entries') or []):
            if isinstance(e, dict) and 'key' in e:
                out[e['key']] = e.get('name')
    return out


def proper_noun_names():
    """Flat {entry_key: canonical} across every category in proper_noun_registry."""
    d = _load(PROPER_NOUN)
    out = {}
    for _category, block in d.items():
        if isinstance(block, dict):
            for k, e in block.items():
                if isinstance(e, dict) and 'canonical' in e:
                    out[k] = e.get('canonical')
    return out


def main():
    desc = descriptor_names()
    proper = proper_noun_names()
    problems = []
    checked = 0

    for key, entry in names.entries().items():
        canon = entry.get('canonical')
        category = entry.get('category', '')

        if key.split('.')[0] in ('attr', 'agg', 'fac', 'set'):
            checked += 1
            if key not in desc:
                problems.append(f"{key}: no mirror in descriptor_registry.yaml (expected name '{canon}')")
            elif desc[key] != canon:
                problems.append(f"{key}: index '{canon}' != descriptor_registry name '{desc[key]}'")
        elif category == 'proper_noun':
            checked += 1
            seg = key.split('.')[-1]
            if seg not in proper:
                problems.append(f"{key}: no mirror '{seg}' in proper_noun_registry.yaml (expected '{canon}')")
            elif proper[seg] != canon:
                problems.append(f"{key}: index '{canon}' != proper_noun_registry canonical '{proper[seg]}'")
        # else: mechanic/clock/track/substrate — no mirror, intentionally skipped.

    if problems:
        print(f"[NAMES CONSISTENCY VIOLATIONS: {len(problems)}]")
        print("  references/names_index.yaml is authoritative; update the mirror to match "
              "(or run tools/valoria_rename.py, which updates both):")
        for p in problems:
            print(f"  {p}")
        return 1
    print(f"Names consistency: {checked} mirrored name(s) agree with references/names_index.yaml.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
