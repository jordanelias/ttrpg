"""descriptor_registry.py -- loader/resolver for references/descriptor_registry.yaml (W1.13).

The bind-at-load layer: load the registry once, then resolve descriptors by key / primary name /
alias (name-indexed). Consumers reference a descriptor by its stable key while the roster churns
(rename / recategorize / extend in the YAML, never in consumer code). This is the mechanism that
makes the 'spirit move' (Spirit -> Mind/Will) cost zero formula rewrites: legacy 'Spirit'
back-resolves through the alias.
"""
import os
import yaml

_PATHS = ('references/descriptor_registry.yaml', '/home/claude/descriptor_registry.yaml')


def load(text=None):
    """Load the registry dict. Pass `text` to parse a string; else search known paths."""
    if text is None:
        for p in _PATHS:
            if os.path.exists(p):
                with open(p) as f:
                    text = f.read()
                break
        if text is None:
            raise FileNotFoundError("descriptor_registry.yaml not found in " + repr(_PATHS))
    return yaml.safe_load(text)


def all_attributes(reg):
    """Flatten the 3 categories into entries with category / domain / kind annotated."""
    out = []
    for cat in ('body', 'mind', 'social'):
        for e in reg['attributes'][cat]:
            out.append({**e, 'category': cat, 'domain': 'actor', 'kind': 'attribute_scalar'})
    return out


def resolve(reg, name_or_key):
    """Resolve a primary name, alias, or key -> attribute entry. Case-insensitive; None if absent."""
    n = str(name_or_key).strip().lower()
    for e in all_attributes(reg):
        if (e['key'].lower() == n or e['name'].lower() == n
                or any(a.lower() == n for a in e.get('aliases', []))):
            return e
    return None


def aggregate_members(reg, agg_key):
    """Member keys of a placeholder aggregate (agg.body/agg.mind/agg.social), or None."""
    for a in reg['aggregates']['entries']:
        if a['key'] == agg_key:
            return list(a['members'])
    return None


def by_domain(reg, domain):
    """Attribute keys in a domain (v1 attributes are all actor-domain)."""
    return [e['key'] for e in all_attributes(reg) if e['domain'] == domain]


def by_category(reg, category):
    """Attribute keys in a category (body/mind/social)."""
    return [e['key'] for e in all_attributes(reg) if e['category'] == category]


def is_deprecated(reg, key):
    """True if `key` is in the deprecated set (e.g. resonance_style)."""
    return any(d['key'] == key for d in reg.get('deprecated', []))
