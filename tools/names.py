#!/usr/bin/env python3
"""
names.py — the single reader for references/names_index.yaml.

names_index.yaml is the ONE place a definition's display name lives: change a
`canonical` there (or run tools/valoria_rename.py) and that single edit
propagates everywhere, while the naming gates (ci_naming_check.py,
ci_names_check.py) read the deprecated->canonical mapping FROM here instead of
hardcoding it.

ONE SOURCE, MANY READERS: ci_naming_check, ci_names_check, valoria_rename and
ci_names_consistency all import this module; none re-parse the index themselves.

Loading is fault-tolerant BY DESIGN. This module is imported transitively by the
Claude Code edit-time hook (hook_naming_guard -> ci_naming_check -> names), which
must never crash on a missing/malformed index or an absent PyYAML. On any load
failure the readers return empty results; CI installs PyYAML so the gates there
see the real data.

Schema (references/names_index.yaml):
    version: 1
    entries:
      <dotted.key>:
        canonical: <the one display string>
        aliases:   [<allowed equivalent phrasings>]
        legacy:    [<deprecated names that must not appear>]
        category:  <attribute|faction_stat|...|proper_noun>
        enforce:   block | warn      # block = hard gate, warn = report-only lint
"""
import os

try:
    import yaml
except Exception:  # PyYAML absent (e.g. edit-time hook env) — degrade, never crash
    yaml = None

# references/names_index.yaml, resolved relative to this file (tools/).
_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(_REPO_ROOT, 'references', 'names_index.yaml')

_cache = None


def load(path=None):
    """Parsed index as a dict, or {} if it cannot be read/parsed. Never raises."""
    global _cache
    if path is None and _cache is not None:
        return _cache
    if yaml is None:
        return {}
    try:
        with open(path or INDEX_PATH, encoding='utf-8') as f:
            data = yaml.safe_load(f) or {}
    except Exception:
        return {}
    if not isinstance(data, dict):
        data = {}
    if path is None:
        _cache = data
    return data


def entries(path=None):
    """The `entries` mapping {key: {canonical, aliases, legacy, category, enforce}}."""
    e = load(path).get('entries', {})
    return e if isinstance(e, dict) else {}


def _entry(key, path=None):
    e = entries(path).get(key)
    return e if isinstance(e, dict) else {}


def canonical(key, path=None):
    """The canonical display name for `key`, or None if unknown."""
    return _entry(key, path).get('canonical')


def aliases(key, path=None):
    """Allowed equivalent phrasings for `key` (never errors)."""
    v = _entry(key, path).get('aliases') or []
    return list(v) if isinstance(v, list) else []


def legacy(key, path=None):
    """Deprecated names for `key` that must not appear in active docs."""
    v = _entry(key, path).get('legacy') or []
    return list(v) if isinstance(v, list) else []


def all_legacy(path=None, enforce=None):
    """
    Flat list of (legacy_name, canonical, key, enforce) over every entry.

    `enforce`, if given, filters to that tier ('block' = hard gate,
    'warn' = report-only drift lint).
    """
    out = []
    for key, e in entries(path).items():
        if not isinstance(e, dict):
            continue
        tier = e.get('enforce', 'warn')
        if enforce is not None and tier != enforce:
            continue
        canon = e.get('canonical')
        for name in (e.get('legacy') or []):
            if name:
                out.append((name, canon, key, tier))
    return out


def key_for(name, path=None):
    """Reverse lookup: the key whose canonical (or alias) equals `name`, else None."""
    if not name:
        return None
    target = name.strip()
    for key, e in entries(path).items():
        if not isinstance(e, dict):
            continue
        if (e.get('canonical') or '').strip() == target:
            return key
        if target in [a.strip() for a in (e.get('aliases') or []) if isinstance(a, str)]:
            return key
    return None
