#!/usr/bin/env python3
"""
Valoria Proper Noun Extractor
==============================
Seeds references/proper_noun_registry.yaml from structured sources and
identifies candidate proper nouns across all active design files.

Structured sources (high-confidence seeds):
  - designs/world/geography_v30.md (17 territories, 6 factions)
  - designs/npcs/npc_roster_v30.md (numbered NPC headers)
  - designs/npcs/npc_character_analyses_v30.md (character sections)

Fuzzy-scan sources (flag candidates):
  - All files in STRUCTURED_SOURCES plus character_histories,
    worldbuilding, southernmost, faction params.

Output:
  - references/proper_noun_registry.yaml — confirmed entries
  - references/proper_noun_candidates.yaml — flagged candidates for review

The candidates file is a worklist. Jordan (via the collator artifact) promotes
entries to the registry, marks them as aliases of existing canonical names,
or rejects them as false positives.

Usage:
  export GITHUB_PAT=<pat>
  python3 tools/extract_proper_nouns.py          # dry-run, prints summary
  python3 tools/extract_proper_nouns.py --write  # writes YAML files
"""

import argparse
import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/..')
sys.path.insert(0, '/home/claude')
try:
    import github_ops as g
except ImportError:
    print("ERROR: github_ops.py not on path. Set PYTHONPATH or run from repo root.")
    sys.exit(1)


# ─── SOURCES ──────────────────────────────────────────────────────────────

STRUCTURED_SOURCES = [
    'designs/world/geography_v30.md',
    'designs/world/geography_v30_infill.md',
    'designs/npcs/npc_roster_v30.md',
    'designs/npcs/npc_roster_v30_infill.md',
    'designs/npcs/npc_character_analyses_v30.md',
    'designs/npcs/npc_character_analyses_v30_infill.md',
    'designs/world/character_histories_v30.md',
    'designs/world/character_histories_v30_infill.md',
    'params/factions.md',
    'designs/world/worldbuilding_v30.md',
    'designs/world/worldbuilding_v30_infill.md',
    'designs/world/southernmost_v30.md',
]


# ─── FALSE-POSITIVE FILTER ────────────────────────────────────────────────

# Pronouns + determiners
PRONOUNS = {
    'He', 'She', 'His', 'Her', 'Him', 'Hers', 'They', 'Them', 'Their',
    'Theirs', 'It', 'Its', 'You', 'Your', 'Yours', 'We', 'Us', 'Our',
    'Ours', 'I', 'Me', 'My', 'Mine',
}

# Sentence-start common capitalized words
COMMON_CAPS = {
    'The', 'This', 'That', 'These', 'Those', 'When', 'Where', 'Why',
    'How', 'What', 'Who', 'Which', 'Whose', 'A', 'An', 'If', 'But', 'And',
    'Or', 'In', 'On', 'At', 'To', 'For', 'With', 'By', 'From', 'As',
    'All', 'Any', 'Some', 'Every', 'Each', 'Both', 'Either', 'Neither',
    'First', 'Second', 'Third', 'Fourth', 'Fifth', 'Last', 'Next',
    'Yes', 'No', 'True', 'False', 'None', 'Null',
    'Can', 'Could', 'Will', 'Would', 'Should', 'May', 'Might', 'Must',
    'Do', 'Does', 'Did', 'Is', 'Are', 'Was', 'Were', 'Be', 'Been',
    'Has', 'Have', 'Had', 'Not', 'Also', 'Only', 'Even', 'Just', 'Now',
    'Then', 'There', 'Here', 'So', 'Yet', 'Still', 'Always', 'Never',
    'Often', 'Sometimes', 'Once', 'Twice', 'Again',
}

# Mechanical terms that are properly-capitalized but not proper nouns
MECHANICAL_TERMS = {
    'Thread', 'Ob', 'Full', 'Knot', 'Modifier', 'Strand',
    'Certainty', 'Depth', 'Sensitivity', 'Tension', 'Pool', 'Score',
    'Bonus', 'Penalty', 'Success', 'Failure', 'Partial', 'Overwhelming',
    'Target', 'Number', 'Die', 'Dice', 'Roll', 'Attribute', 'Skill',
    'Round', 'Turn', 'Scene', 'Session', 'Year', 'Season', 'Day',
    'Stage', 'Phase', 'Step', 'Tier', 'Level', 'Rank', 'Degree',
    'Health', 'Stamina', 'Composure', 'Focus', 'Momentum', 'Coherence',
    'Rendering', 'Stability', 'Intelligibility',
    'Mode', 'Card', 'Recall', 'Investigation', 'Debate', 'Influence',
    'Domain', 'Presence', 'Belief', 'Resolution', 'Vocation',
    'Behavioral', 'Counter', 'Event', 'Hybrid', 'Historical', 'Military',
    'Ministry', 'Mandate', 'Calamity', 'Action', 'Reaction',
    'Agility', 'Attunement', 'Cognition', 'Endurance', 'Spirit', 'Strength',
    'Rattled', 'Concession', 'Conviction', 'Composed',
    'Guilds', 'Upward', 'Inward', 'Outward', 'Downward',
    'Consul', 'Tribune',  # offices/roles not people
    'Status', 'Scope', 'Source', 'Date', 'Author', 'Version',
    'Note', 'Notes', 'Context', 'Summary', 'Overview', 'Design',
    'Principle', 'Purpose', 'Mechanic', 'Rule', 'Rules', 'Effect',
    'Result', 'Trigger', 'Condition', 'Response',
    'Section', 'Part', 'Chapter', 'Appendix', 'Example', 'Examples',
    'Canonical', 'Incorporates', 'Supersedes', 'Consolidated',
    'Compromise', 'Consequence', 'Ethics', 'Rationale',
    'Primary', 'Secondary', 'Initial', 'Default', 'Standard', 'Custom',
    'Scene Battle', 'Event Card', 'Thread Sensitivity',  # compound mechanical
}

EXCLUDE_ALL = PRONOUNS | COMMON_CAPS | MECHANICAL_TERMS


# ─── EXTRACTORS ───────────────────────────────────────────────────────────

def extract_territories(content):
    """Pull territory names from the T# table."""
    out = {}
    pattern = re.compile(
        r'^\|\s*(T\d+)\s*\|\s*([A-Z][A-Za-z]+)\s*\|',
        re.MULTILINE
    )
    for m in pattern.finditer(content):
        t_id = m.group(1)
        name = m.group(2).strip()
        out[name] = {
            'canonical': name,
            'type': 'territory',
            'territory_id': t_id,
            'aliases': [],
            'source': 'designs/world/geography_v30.md',
        }
    return out


def extract_factions_from_geography(content):
    """Pull faction names from the Starting Control Summary."""
    out = {}
    m = re.search(
        r'Starting Control Summary.*?\|.*?\|.*?\|.*?\|\n((?:\|[^\n]+\|\n)+)',
        content,
        re.DOTALL,
    )
    if not m:
        return out
    rows = m.group(1)
    for line in rows.split('\n'):
        row_match = re.match(
            r'^\|\s*\**([A-Z][A-Za-z]+)\**\s*\|',
            line.strip(),
        )
        if row_match:
            name = row_match.group(1).strip('*').strip()
            if name.lower() in ('total', 'faction'):
                continue
            out[name] = {
                'canonical': name,
                'type': 'faction',
                'aliases': [],
                'source': 'designs/world/geography_v30.md',
            }
    return out


def extract_characters_from_roster(content):
    """Pull NPC names from '## N. Name — Role (Location)' headers."""
    out = {}
    pattern = re.compile(
        r'^##\s+\d+\.\s+([^—\n]+?)\s*—\s*([^\n(]+?)(?:\s*\(([^)]+)\))?$',
        re.MULTILINE,
    )
    for m in pattern.finditer(content):
        name = m.group(1).strip()
        role = m.group(2).strip()
        location = (m.group(3) or '').strip()
        if not name:
            continue
        out[name] = {
            'canonical': name,
            'type': 'character',
            'role': role,
            'location': location if location else None,
            'aliases': [],
            'source': 'designs/npcs/npc_roster_v30.md',
        }
    return out


def extract_characters_from_analyses(content):
    """Pull NPC names from analysis-doc headers."""
    out = {}
    pattern = re.compile(
        r'^##\s+(?:\d+\.\s+)?([A-ZÆÖÄÜ][A-Za-zæöäüßé]+'
        r'(?:\s+[A-ZÆÖÄÜ][A-Za-zæöäüßé]+)*)\s*—',
        re.MULTILINE,
    )
    for m in pattern.finditer(content):
        name = m.group(1).strip()
        if name in EXCLUDE_ALL:
            continue
        out[name] = {
            'canonical': name,
            'type': 'character',
            'aliases': [],
            'source': 'designs/npcs/npc_character_analyses_v30.md',
        }
    return out


def merge_noun_dicts(*dicts):
    """
    Merge dicts. If a name appears in multiple extractors with different
    types, record all types (e.g., Schoenland is both a territory and a
    faction).
    """
    merged = {}
    for d in dicts:
        for name, entry in d.items():
            if name not in merged:
                merged[name] = dict(entry)
                merged[name].setdefault('additional_sources', [])
                # Normalize type to a list internally
                if 'type' in merged[name]:
                    merged[name]['types'] = [merged[name]['type']]
            else:
                # Add type if not already present
                new_type = entry.get('type')
                if new_type and new_type not in merged[name].get('types', []):
                    merged[name].setdefault('types', []).append(new_type)
                src = entry.get('source')
                if src and src not in merged[name].get('additional_sources', []):
                    merged[name].setdefault('additional_sources', []).append(src)
                # Preserve territory_id and role if new entry has them
                for k in ('territory_id', 'role', 'location'):
                    if k in entry and k not in merged[name]:
                        merged[name][k] = entry[k]
    # Collapse types list: if single type, keep scalar for backwards-compat
    for name, entry in merged.items():
        types = entry.get('types', [])
        if len(types) == 1:
            entry['type'] = types[0]
            del entry['types']
        elif len(types) > 1:
            # Primary type for grouping = first one found
            entry['type'] = types[0]
            entry['also_types'] = types[1:]
            del entry['types']
    return merged


# ─── FUZZY SCAN ───────────────────────────────────────────────────────────

CAND_PATTERN = re.compile(
    r'\b([A-ZÆÖÄÜ][a-zæöäüßé]+(?:\s+[A-ZÆÖÄÜ][a-zæöäüßé]+){0,2})\b'
)


def fuzzy_scan_validation(registry, files):
    """
    Count occurrences of known names + flag unknown capitalized tokens.

    Returns:
      occurrences: {canonical: {path: count}}
      candidates:  {token: {path: count}} for tokens not in registry
    """
    occurrences = defaultdict(lambda: defaultdict(int))

    # Count known names
    for name in registry:
        pattern = re.compile(r'\b' + re.escape(name) + r'\b')
        for path, content in files.items():
            if content is None:
                continue
            count = len(pattern.findall(content))
            if count > 0:
                occurrences[name][path] = count

    # Candidate scan
    candidate_counts = defaultdict(lambda: defaultdict(int))
    known = set(registry.keys())

    for path, content in files.items():
        if content is None:
            continue
        for m in CAND_PATTERN.finditer(content):
            tok = m.group(1).strip()
            # Filter
            if tok in known:
                continue
            if tok in EXCLUDE_ALL:
                continue
            # Skip if first word alone is a common cap
            first = tok.split()[0]
            if first in PRONOUNS or first in COMMON_CAPS:
                # Multi-word may still be valid (e.g., "The Forgetting")
                # but skip if it's the full token
                if tok == first:
                    continue
            candidate_counts[tok][path] += 1

    # Threshold: appear in ≥2 files OR ≥3 occurrences total
    candidates = {}
    for tok, file_counts in candidate_counts.items():
        total = sum(file_counts.values())
        if len(file_counts) >= 2 or total >= 3:
            candidates[tok] = dict(file_counts)

    return dict(occurrences), candidates


# ─── YAML OUTPUT ──────────────────────────────────────────────────────────

def registry_to_yaml(registry, occurrences):
    """Emit registry as YAML grouped by type."""
    lines = [
        "# Valoria Proper Noun Registry",
        "# Auto-seeded by tools/extract_proper_nouns.py",
        "# Canonical source of truth for character, territory, faction,",
        "# settlement, and landmark names.",
        "#",
        "# Schema per entry:",
        "#   canonical: <canonical spelling>",
        "#   type: character|territory|faction|settlement|landmark|people",
        "#   aliases: [list of known alternative spellings/references]",
        "#   source: <primary source file>",
        "#   occurrences: <count of files this name appears in>",
        "",
        f"version: 1",
        "",
    ]
    by_type = defaultdict(list)
    for name, entry in registry.items():
        by_type[entry.get('type', 'unknown')].append((name, entry))
    PLURAL = {
        'character': 'characters',
        'territory': 'territories',
        'faction': 'factions',
        'settlement': 'settlements',
        'landmark': 'landmarks',
        'people': 'peoples',
        'unknown': 'unknown',
    }
    for type_name in ['character', 'territory', 'faction', 'settlement',
                      'landmark', 'people', 'unknown']:
        entries = sorted(by_type.get(type_name, []))
        if not entries:
            continue
        lines.append(f"{PLURAL[type_name]}:")
        for name, entry in entries:
            occ = occurrences.get(name, {})
            total_files = len(occ)
            total_occ = sum(occ.values())
            lines.append(f"  {_yaml_key(name)}:")
            lines.append(f"    canonical: \"{entry['canonical']}\"")
            if entry.get('also_types'):
                lines.append(f"    also_types: {entry['also_types']}")
            if entry.get('territory_id'):
                lines.append(f"    territory_id: {entry['territory_id']}")
            if entry.get('role'):
                lines.append(f"    role: \"{entry['role']}\"")
            if entry.get('location'):
                lines.append(f"    location: \"{entry['location']}\"")
            aliases = entry.get('aliases', [])
            if aliases:
                lines.append(f"    aliases: {aliases}")
            else:
                lines.append(f"    aliases: []")
            lines.append(f"    source: \"{entry['source']}\"")
            addl = entry.get('additional_sources', [])
            if addl:
                lines.append(f"    additional_sources:")
                for s in addl:
                    lines.append(f"      - \"{s}\"")
            lines.append(f"    occurrences_count: {total_occ}")
            lines.append(f"    files_count: {total_files}")
        lines.append("")
    return '\n'.join(lines)


def candidates_to_yaml(candidates):
    """Emit candidates worklist as YAML."""
    lines = [
        "# Valoria Proper Noun Candidates (worklist)",
        "# Auto-generated by tools/extract_proper_nouns.py",
        "# Tokens found in design files that look like proper nouns but",
        "# are not yet in the registry. Each entry needs triage:",
        "#   - Promote to registry (confirm as canonical)",
        "#   - Mark as alias of an existing canonical entry",
        "#   - Reject as false positive (add to EXCLUDE list in extractor)",
        "#",
        "# Sort: descending by total occurrences.",
        "",
        f"version: 1",
        "candidates:",
    ]
    sorted_c = sorted(
        candidates.items(),
        key=lambda kv: (-sum(kv[1].values()), kv[0])
    )
    for tok, file_counts in sorted_c:
        total = sum(file_counts.values())
        lines.append(f"  {_yaml_key(tok)}:")
        lines.append(f"    token: \"{tok}\"")
        lines.append(f"    total_occurrences: {total}")
        lines.append(f"    files_count: {len(file_counts)}")
        lines.append(f"    appears_in:")
        for path, count in sorted(file_counts.items(),
                                  key=lambda kv: -kv[1]):
            lines.append(f"      \"{path}\": {count}")
    return '\n'.join(lines)


def _yaml_key(name):
    """Convert a name to a safe YAML key (lowercase, underscore, ascii)."""
    import unicodedata
    s = unicodedata.normalize('NFKD', name)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r'[^\w]+', '_', s.lower())
    s = s.strip('_')
    return s or 'unnamed'


# ─── MAIN ─────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true',
                        help='Write YAML output to /tmp/ (not committed)')
    parser.add_argument('--out-dir', default='/tmp',
                        help='Output directory for YAML files')
    args = parser.parse_args()

    print("[1/4] Fetching sources...")
    files = g.read_files_graphql(STRUCTURED_SOURCES, force_full=True)
    loaded = sum(1 for v in files.values() if v)
    print(f"  {loaded}/{len(STRUCTURED_SOURCES)} sources loaded")

    print("[2/4] Extracting from structured tables/headers...")
    geography = files.get('designs/world/geography_v30.md', '') or ''
    roster = files.get('designs/npcs/npc_roster_v30.md', '') or ''
    analyses = files.get('designs/npcs/npc_character_analyses_v30.md', '') or ''

    territories = extract_territories(geography)
    factions = extract_factions_from_geography(geography)
    roster_chars = extract_characters_from_roster(roster)
    analyses_chars = extract_characters_from_analyses(analyses)

    print(f"  territories={len(territories)} factions={len(factions)} "
          f"characters(roster)={len(roster_chars)} "
          f"characters(analyses)={len(analyses_chars)}")

    registry = merge_noun_dicts(territories, factions,
                                roster_chars, analyses_chars)
    print(f"  merged: {len(registry)} confirmed entries")

    print("[3/4] Fuzzy-scanning for occurrences + unknown candidates...")
    occurrences, candidates = fuzzy_scan_validation(registry, files)
    print(f"  occurrence records: {len(occurrences)}")
    print(f"  candidates flagged: {len(candidates)}")

    print("[4/4] Rendering YAML...")
    registry_yaml = registry_to_yaml(registry, occurrences)
    candidates_yaml = candidates_to_yaml(candidates)

    if args.write:
        os.makedirs(args.out_dir, exist_ok=True)
        reg_path = os.path.join(args.out_dir, 'proper_noun_registry.yaml')
        cand_path = os.path.join(args.out_dir, 'proper_noun_candidates.yaml')
        with open(reg_path, 'w') as f:
            f.write(registry_yaml)
        with open(cand_path, 'w') as f:
            f.write(candidates_yaml)
        print(f"  wrote {reg_path}")
        print(f"  wrote {cand_path}")
    else:
        print("  (dry-run — pass --write to emit files)")

    # Summary
    print("\n=== REGISTRY SUMMARY ===")
    by_type = defaultdict(int)
    for entry in registry.values():
        by_type[entry.get('type', 'unknown')] += 1
    for t, n in sorted(by_type.items()):
        print(f"  {t}: {n}")

    # Top unknown candidates
    print("\n=== TOP 20 CANDIDATES FOR TRIAGE ===")
    sorted_c = sorted(
        candidates.items(),
        key=lambda kv: (-sum(kv[1].values()), kv[0])
    )[:20]
    for tok, fc in sorted_c:
        total = sum(fc.values())
        print(f"  {tok}: {total} occ / {len(fc)} files")


if __name__ == '__main__':
    main()
