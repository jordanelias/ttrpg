#!/usr/bin/env python3
"""
quantity_registry.py — the single reader for the quantity/attribute vocabulary.

references/descriptor_registry.yaml is the canonical pointer registry for
attributes/aggregates/faction-stats/settlement-stats/practitioner-stats/
territory-stats (systems bind descriptors BY KEY so a name can churn without
rewriting consumers — see that file's header). references/names_index.yaml
separately carries canonical display
names for some quantities (clocks, mass-combat stats, mechanics) under its own
`entries:` map. Both are "known-vocabulary" sources for the same question a
consumer asks: "is this stat name a pointer into a registry, or did I just
hardcode it?"

ONE SOURCE, MANY READERS (mirrors tools/names.py): descriptor_registry.yaml is
parsed in exactly one place, tools/descriptor_registry.py's load() — this
module imports and calls that loader rather than re-parsing the YAML itself,
then merges its output with names_index.yaml (parsed here, since no other
module owns that file) into one resolvable vocabulary.
tools/ci_quantity_vocabulary_check.py (A17) is the primary caller; any future
runtime caller (e.g. a KeyLog stat_vocabulary hook) should use this instead of
re-parsing either YAML.

Loading is fault-tolerant BY DESIGN (same discipline as names.py): a missing
file or absent PyYAML degrades to an empty vocabulary rather than raising, so
nothing importing this module can be crashed by a corpus edit.

Resolution is name-based and best-effort: registry entries are prose-adjacent
display strings (parenthetical annotations, "Track"/"Clock"/"Pool" suffixes,
bundled "A / B / C" forms), not a single normalized identifier space. See
`resolve()` for the exact normalization steps tried, in order.
"""
import os
import re
import sys

try:
    import yaml
except Exception:  # PyYAML absent — degrade, never crash
    yaml = None

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
if _TOOLS_DIR not in sys.path:
    sys.path.insert(0, _TOOLS_DIR)

try:
    import descriptor_registry as _descriptor_registry
except Exception:  # PyYAML absent, or the module can't import — degrade, never crash
    _descriptor_registry = None

DESCRIPTOR_PATH = os.path.join(_REPO_ROOT, 'references', 'descriptor_registry.yaml')
NAMES_INDEX_PATH = os.path.join(_REPO_ROOT, 'references', 'names_index.yaml')

_cache = None


def _load_yaml(path):
    """Generic YAML-to-dict loader for files descriptor_registry.py does not own
    (currently only names_index.yaml). Not used for descriptor_registry.yaml — see
    _load_descriptor(), which delegates that file's parsing to descriptor_registry.load()."""
    if yaml is None:
        return {}
    try:
        with open(path, encoding='utf-8') as f:
            data = yaml.safe_load(f) or {}
    except Exception:
        return {}
    return data if isinstance(data, dict) else {}


def _load_descriptor(path):
    """Load descriptor_registry.yaml's dict via tools/descriptor_registry.py's load() —
    the one parser for that file — instead of re-parsing it independently. Reads `path`
    as text and hands it to that loader's `text=` parameter, so an explicit path override
    (e.g. a test fixture) is honored the same way the rest of this module honors overrides.
    Fault-tolerant: missing file, absent PyYAML, or a parse error all degrade to {} — same
    discipline as the rest of this module.
    """
    if _descriptor_registry is None:
        return {}
    try:
        with open(path, encoding='utf-8') as f:
            text = f.read()
    except Exception:
        return {}
    try:
        data = _descriptor_registry.load(text=text)
    except Exception:
        return {}
    return data if isinstance(data, dict) else {}


def load(descriptor_path=None, names_index_path=None):
    """Merged vocabulary: {'known': {display_name: key_or_None}, 'not_descriptors': set}.

    `known` maps every registered display name/alias to its registry `key:`
    (attr.body.strength, fac.influence, ...), or to None when the name comes
    from `not_descriptors` (a legitimate computed/bounded container name that
    is deliberately NOT registry-keyed — see descriptor_registry.yaml's own
    not_descriptors section) or from names_index.yaml (which keys by a
    dotted id but is not itself the descriptor registry).

    Cached on the no-args call (the common case); pass explicit paths to
    bypass the cache (used by tests).
    """
    global _cache
    use_cache = descriptor_path is None and names_index_path is None
    if use_cache and _cache is not None:
        return _cache

    known = {}

    def _add(name, key=None):
        name = (name or '').strip()
        if name and name not in known:
            known[name] = key

    descriptor = _load_descriptor(descriptor_path or DESCRIPTOR_PATH)

    attrs = descriptor.get('attributes', {}) or {}
    for group in ('body', 'mind', 'social'):
        for e in attrs.get(group, []) or []:
            if not isinstance(e, dict):
                continue
            _add(e.get('name'), e.get('key'))
            for a in e.get('aliases') or []:
                _add(a, e.get('key'))

    for e in (descriptor.get('aggregates', {}) or {}).get('entries', []) or []:
        if isinstance(e, dict):
            _add(e.get('name'), e.get('key'))

    for section in ('faction_stats', 'practitioner_stats', 'territory_stats', 'settlement_stats'):
        for e in (descriptor.get(section, {}) or {}).get('entries', []) or []:
            if not isinstance(e, dict):
                continue
            _add(e.get('name'), e.get('key'))
            for a in e.get('aliases') or []:
                _add(a, e.get('key'))

    for e in descriptor.get('by_reference', []) or []:
        if isinstance(e, dict):
            _add(e.get('name'), e.get('key'))

    not_descriptors = set()
    nd = descriptor.get('not_descriptors', {}) or {}
    for bucket in ('derived_values', 'tracks', 'clocks', 'pools'):
        for name in nd.get(bucket, []) or []:
            name = (name or '').strip()
            if name:
                not_descriptors.add(name)
                _add(name, None)

    names_idx = _load_yaml(names_index_path or NAMES_INDEX_PATH)
    for key, e in (names_idx.get('entries') or {}).items():
        if not isinstance(e, dict):
            continue
        _add(e.get('canonical'), key)
        for a in e.get('aliases') or []:
            _add(a, key)

    result = {'known': known, 'not_descriptors': not_descriptors}
    if use_cache:
        _cache = result
    return result


_SUFFIX_RE = re.compile(r'\s+(Track|Clock|Pool|Field)$', re.IGNORECASE)
_PAREN_RE = re.compile(r'\s*\([^)]*\)')
_PAREN_CONTENT_RE = re.compile(r'\(([^)]*)\)')


def _candidates(raw):
    """Yield normalized candidate forms of a raw identifier, most-specific first.

    Handles the concrete drift patterns seen in module_contracts.yaml `state[].name`
    strings: parenthetical annotations ("CV (per-territory Piety)"), and
    track/clock/pool suffixes ("Evidence Track", "persuasion_track").
    """
    raw = (raw or '').strip()
    if not raw:
        return
    seen = set()

    def emit(cand):
        cand = (cand or '').strip()
        if cand and cand not in seen:
            seen.add(cand)
            return cand
        return None

    c = emit(raw)
    if c:
        yield c

    underscored = raw.replace('_', ' ')
    c = emit(underscored)
    if c:
        yield c

    no_paren = _PAREN_RE.sub('', underscored).strip()
    c = emit(no_paren)
    if c:
        yield c

    m = _PAREN_CONTENT_RE.search(raw)
    if m:
        c = emit(m.group(1))
        if c:
            yield c

    no_suffix = _SUFFIX_RE.sub('', no_paren).strip()
    c = emit(no_suffix)
    if c:
        yield c


def resolve(raw_name, descriptor_path=None, names_index_path=None):
    """Best-effort resolution of a raw identifier to (matched_as, key).

    `matched_as` is the exact known display name that matched (for reporting);
    `key` is its registry key, or None if it matched a not_descriptors /
    names_index-only entry with no descriptor key. Returns (None, None) if
    nothing resolves under any tried normalization.
    """
    data = load(descriptor_path, names_index_path)
    known = data['known']
    lowered = {name.lower(): (name, key) for name, key in known.items()}
    for cand in _candidates(raw_name):
        if cand in known:
            return cand, known[cand]
        hit = lowered.get(cand.lower())
        if hit:
            return hit
    return None, None


def resolves(raw_name, descriptor_path=None, names_index_path=None):
    matched, _ = resolve(raw_name, descriptor_path, names_index_path)
    return matched is not None


def all_known(descriptor_path=None, names_index_path=None):
    return set(load(descriptor_path, names_index_path)['known'].keys())
