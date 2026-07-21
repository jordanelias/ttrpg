#!/usr/bin/env python3
"""
vector_audit.py — Valoria v3 Multi-Graph Triangulation Audit Pipeline

Owned by skills/valoria-vector-audit/. Do not call this directly inline; invoke
through the skill so the methodology gates are honored.

Usage:
    python3 vector_audit.py --output-dir /path/to/run --mode all
    python3 vector_audit.py --output-dir /path/to/run --mode A,B,G  (modes only)

Stages executed by --mode all:
    0. Pilot validation (8 tokens)
    1. Corpus extraction with banner classifier
    2. Token curation (seed + auto + disambiguation)
    2.5. Expanded citation graph
    3. Standard sklearn TF-IDF
    4. Metadata graphs (throughline, mu, pp)
    5. Structural property validation (P1/P2/P3)
    6. Multi-graph diagnostics (8 modes)
    7. Discourse/design overlay

PRECONDITIONS:
    - run from the repo root; the corpus is read from the working tree (the
      checkout is authoritative — no GitHub fetch, no PAT, no bootstrap).

POSTCONDITIONS:
    All intermediate JSON/NPZ files written to {output_dir}/data/
    Validation outcome in {output_dir}/data/validation.json
    Diagnostics in {output_dir}/data/multigraph_diagnostics.json

DESIGN NOTES:
    - In+out neighbor union for cite-degree, never out-only
    - Pre-committed thresholds locked; do not edit without methodology revision
    - Class taxonomy filters within-class implied-missing pairs
    - Disambiguation rules required for English-word collision tokens
    - Provisional design IS design (banner-classified into design corpus)
    - Citation graph uses ≥2 implicit mentions threshold (v3 expansion)
    - TF-IDF is supporting only; multi-graph is primary

VERSION: v3 (2026-04-29)
"""

import sys
import os
import re
import json
import argparse
import time
from collections import defaultdict, Counter
from pathlib import Path

try:
    import numpy as np  # optional; only the supporting TF-IDF graph uses it
except Exception:
    np = None
import yaml

# Reuse tools/names.py as THE reader for references/names_index.yaml (CLAUDE.md §8 — "every rule
# lives once"; names.py's own docstring declares it the single reader) instead of re-parsing that
# file locally (Fable-5 audit fix). The reader module is loaded from the REAL repo's tools/ (via
# __file__), while the DATA is read from the --repo-root-relative path, so --repo-root is honored.
_TOOLS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))), 'tools')
if _TOOLS_DIR not in sys.path:
    sys.path.insert(0, _TOOLS_DIR)
try:
    import names  # noqa: E402
except Exception:  # pragma: no cover — degrade to the local _yaml reader if unavailable
    names = None


# ──────────────────────────── CANONICAL TAXONOMY ─────────────────────────────

CLASSES = {
    'conviction': ['Faith', 'Order', 'Reason', 'Equity', 'Precedent', 'Autonomy', 'Continuity'],
    'pressure_point': ['Evidence', 'Consequence', 'Authority', 'Loyalty'],
    'faction': ['Crown', 'Church', 'Hafenmark', 'Varfell', 'Löwenritter',
                'Restoration Movement', 'Guilds'],
    'npc': ['King Almud', 'Confessor Arne', 'Inge Baralta', 'Magnus Vaynard',
            'Lisbeth Ehrenwall', 'Yrsa Vossen', 'Torben', 'Elske', 'Edeyja', 'Lenneth'],
    'clock': ['MS', 'CI', 'IP', 'PI', 'TS', 'TCV'],
}


def same_class(a, b):
    for members in CLASSES.values():
        if a in members and b in members:
            return True
    return False


# ──────────────────────────── PILOT TOKENS ───────────────────────────────────

PILOT_TOKENS = {
    'Combat':            {'patterns': [r'\bCombat\b(?!ant)']},
    'Threadwork':        {'patterns': ['Threadwork', 'Thread operation', 'Thread op']},
    'Mass Combat':       {'patterns': ['Mass Combat', 'Mass Battle', 'mass[- _]combat', 'mass[- _]battle']},
    'Faction Layer':     {'patterns': ['Faction Layer', 'faction[- _]layer']},
    'Domain Echo':       {'patterns': ['Domain Echo']},
    'Piety Track':  {'patterns': ['Piety Track', 'Conviction Wound']},
    'Scale Transitions': {'patterns': [r'\bScale Transitions?\b', r'scale[- _]transition']},
    'NPC Behavior':      {'patterns': ['NPC Behavior', 'NPC Behaviour', 'npc_behavior',
                                       'NPC Decision Procedure', 'NPC priority', 'NPC AI']},
}


# ──────────────────────────── SEED TOKENS (curated core) ─────────────────────
# This is no longer the whole token set — it is the CURATED CORE that derive_tokens()
# layers the live registries on top of (NS2: the token list is derived from
# canonical_sources.yaml + names_index.yaml + proper_noun_registry.yaml at runtime, not
# hand-maintained). The core is kept because it carries what derivation can't: the §3.5
# disambiguation `context` for English-word collision tokens (Faith/Order/Crown/Church/…),
# the foundation set, and the 7-Conviction / 4-Pressure-Point / clock members that P2
# validation and the class taxonomy depend on. The core WINS on any name collision, so
# these keep their disambiguation. To refresh tokens, update the registries — not this list.

SEED_TOKENS = {
    # Foundation
    'Self-Rendering':       {'patterns': ['Self-Rendering', 'self-rendering', 'self_rendering'],
                             'scale': 'foundation', 'status': 'canonical', 'source': 'seed'},
    'Leap':                 {'patterns': [r'\bLeap\b'],
                             'scale': 'foundation', 'status': 'canonical', 'source': 'seed'},
    'Coherence':            {'patterns': [r'\bCoherence\b'],
                             'scale': 'foundation', 'status': 'canonical', 'source': 'seed'},
    'Throughlines':         {'patterns': ['Throughlines', 'throughlines_meta'],
                             'scale': 'foundation', 'status': 'canonical', 'source': 'seed'},
    # Architecture
    'Scale Transitions':    {'patterns': ['Scale Transitions', 'scale_transitions',
                                          'scale-transition', 'mode bridg'],
                             'scale': 'architecture', 'status': 'canonical', 'source': 'seed'},
    'Conflict Architecture':{'patterns': ['Conflict Architecture', 'conflict_architecture'],
                             'scale': 'architecture', 'status': 'canonical', 'source': 'seed'},
    'Campaign Architecture':{'patterns': ['Campaign Architecture', 'campaign_architecture'],
                             'scale': 'architecture', 'status': 'canonical', 'source': 'seed'},
    # Personal
    'Combat':               {'patterns': [r'\bCombat\b(?!ant)'],
                             'scale': 'personal', 'status': 'canonical', 'source': 'seed'},
    'Threadwork':           {'patterns': ['Threadwork', 'Thread operation', 'Thread op'],
                             'scale': 'personal', 'status': 'canonical', 'source': 'seed'},
    'Fieldwork':            {'patterns': ['Fieldwork'],
                             'scale': 'personal', 'status': 'canonical', 'source': 'seed'},
    'NPC Behavior':         {'patterns': ['NPC Behavior', 'NPC Behaviour', 'npc_behavior',
                                          'NPC Decision Procedure', 'NPC priority', 'NPC AI'],
                             'scale': 'personal', 'status': 'canonical', 'source': 'seed'},
    'Knot':                 {'patterns': [r'\bKnot[s]?\b'],
                             'scale': 'personal', 'status': 'canonical', 'source': 'seed'},
    'Piety Track':     {'patterns': ['Piety Track', 'Conviction Wound'],
                             'scale': 'personal', 'status': 'canonical', 'source': 'seed'},
    'Conviction':           {'patterns': [r'\bConviction\b(?! Track| Wound)'],
                             'scale': 'personal', 'status': 'canonical', 'source': 'seed'},
    # Scene
    'Social Contests':      {'patterns': ['Social Contest', 'Grand Debate'],
                             'scale': 'scene', 'status': 'canonical', 'source': 'seed'},
    'Domain Echo':          {'patterns': ['Domain Echo'],
                             'scale': 'scene', 'status': 'canonical', 'source': 'seed'},
    'Wager':                {'patterns': [r'\bWager\b'],
                             'scale': 'scene', 'status': 'canonical', 'source': 'seed'},
    # Settlement
    'Settlement Layer':     {'patterns': ['Settlement Layer', 'settlement_layer'],
                             'scale': 'settlement', 'status': 'canonical', 'source': 'seed'},
    'Settlement Adjacency': {'patterns': ['Settlement Adjacency', 'settlement_adjacency',
                                          'adjacency graph'],
                             'scale': 'settlement', 'status': 'provisional', 'source': 'seed'},
    'Fractional Province':  {'patterns': ['Fractional Province', 'fractional_province'],
                             'scale': 'settlement', 'status': 'provisional', 'source': 'seed'},
    # Province
    'Faction Layer':        {'patterns': ['Faction Layer', 'faction_layer', 'faction-layer'],
                             'scale': 'province', 'status': 'canonical', 'source': 'seed'},
    'Faction Succession':   {'patterns': ['Faction Succession', 'faction_succession',
                                          'succession contest'],
                             'scale': 'province', 'status': 'provisional', 'source': 'seed'},
    'CI Political':         {'patterns': ['CI Political', 'ci_political', 'tc_political'],
                             'scale': 'province', 'status': 'canonical', 'source': 'seed'},
    'Mass Combat':          {'patterns': ['Mass Combat', 'Mass Battle', 'mass-combat',
                                          'mass-battle', 'mass_combat', 'mass_battle'],
                             'scale': 'province', 'status': 'canonical', 'source': 'seed'},
    'Military Layer':       {'patterns': ['Military Layer', 'military_layer'],
                             'scale': 'province', 'status': 'canonical', 'source': 'seed'},
    # Peninsula
    'Victory':              {'patterns': [r'\bVictory\b', 'victory_v30', 'Sovereignty'],
                             'scale': 'peninsula', 'status': 'canonical', 'source': 'seed'},
    'Turmoil':    {'patterns': ['Turmoil', 'peninsular_strain'],
                             'scale': 'peninsula', 'status': 'canonical', 'source': 'seed'},
    'MS Trajectory':        {'patterns': ['MS Trajectory', 'ms_trajectory', 'MS trajectory'],
                             'scale': 'peninsula', 'status': 'canonical', 'source': 'seed'},
    'Thread Revelation':    {'patterns': ['Thread Revelation', 'thread revelation', 'revelation curve'],
                             'scale': 'peninsula', 'status': 'canonical', 'source': 'seed'},
    'Tensions Deck':        {'patterns': ['Tensions Deck', 'tensions_deck'],
                             'scale': 'peninsula', 'status': 'canonical', 'source': 'seed'},
    'Royal Assassination':  {'patterns': ['Royal Assassination', 'royal_assassination',
                                          'assassination fuse'],
                             'scale': 'peninsula', 'status': 'canonical', 'source': 'seed'},
    'Solmund':              {'patterns': [r'\bSolmund\b'],
                             'scale': 'peninsula', 'status': 'provisional', 'source': 'seed'},
    'Miraculous Event':     {'patterns': ['Miraculous Event', 'miraculous_event'],
                             'scale': 'peninsula', 'status': 'provisional', 'source': 'seed'},
    # Clocks
    'MS':                   {'patterns': [r'\bMS\b(?![A-Za-z])', 'Mending Stability'],
                             'scale': 'clock', 'status': 'canonical', 'source': 'seed'},
    'CI':                   {'patterns': [r'\bCI\b(?![A-Za-z])', 'Church Influence'],
                             'scale': 'clock', 'status': 'canonical', 'source': 'seed'},
    'IP':                   {'patterns': [r'\bIP\b(?![A-Za-z])', 'Invasion Pressure'],
                             'scale': 'clock', 'status': 'canonical', 'source': 'seed'},
    'PI':                   {'patterns': [r'\bPI\b(?![A-Za-z])', 'Political Instability'],
                             'scale': 'clock', 'status': 'canonical', 'source': 'seed'},
    'TS':                   {'patterns': [r'\bTS\b(?![A-Za-z])', 'Thread Sensitivity'],
                             'scale': 'clock', 'status': 'canonical', 'source': 'seed'},
    'TCV':                  {'patterns': [r'\bTCV\b'],
                             'scale': 'clock', 'status': 'canonical', 'source': 'seed'},
    # Convictions (disambiguated)
    'Faith':                {'patterns': [r'\bFaith\b'], 'scale': 'conviction',
                             'status': 'canonical', 'source': 'seed',
                             'context': [r'\bConviction\b', r'\bFramework\b', r'\bDivine\b',
                                         r'\bChurch\b', r'\bCardinal\b', r'\bdoctrine\b']},
    'Order':                {'patterns': [r'\bOrder\b'], 'scale': 'conviction',
                             'status': 'canonical', 'source': 'seed',
                             'context': [r'\bConviction\b', r'\bFaith\b', r'\bAutonomy\b',
                                         r'\bReason\b', r'\bEquity\b']},
    'Reason':               {'patterns': [r'\bReason\b'], 'scale': 'conviction',
                             'status': 'canonical', 'source': 'seed',
                             'context': [r'\bConviction\b', r'\bFaith\b', r'\bOrder\b',
                                         r'\bAutonomy\b']},
    'Equity':               {'patterns': [r'\bEquity\b'], 'scale': 'conviction',
                             'status': 'canonical', 'source': 'seed',
                             'context': [r'\bConviction\b', r'\bRestoration\b']},
    'Precedent':            {'patterns': [r'\bPrecedent\b'], 'scale': 'conviction',
                             'status': 'canonical', 'source': 'seed',
                             'context': [r'\bConviction\b', r'\bHafenmark\b', r'\blegal\b']},
    'Autonomy':             {'patterns': [r'\bAutonomy\b'], 'scale': 'conviction',
                             'status': 'canonical', 'source': 'seed',
                             'context': [r'\bConviction\b', r'\bVarfell\b', r'L[oö]wenritter']},
    'Continuity':           {'patterns': [r'\bContinuity\b'], 'scale': 'conviction',
                             'status': 'canonical', 'source': 'seed',
                             'context': [r'\bConviction\b', r'\bRestoration\b']},
    # Pressure Points (disambiguated)
    'Evidence':             {'patterns': [r'\bEvidence\b'], 'scale': 'pressure_point',
                             'status': 'canonical', 'source': 'seed',
                             'context': [r'\bPressure Point\b', r'\bInvestigation\b',
                                         r'\bEvidence Track\b']},
    'Consequence':          {'patterns': [r'\bConsequence\b'], 'scale': 'pressure_point',
                             'status': 'canonical', 'source': 'seed',
                             'context': [r'\bPressure Point\b', r'\bConsequentialist\b']},
    'Authority':            {'patterns': [r'\bAuthority\b'], 'scale': 'pressure_point',
                             'status': 'canonical', 'source': 'seed',
                             'context': [r'\bPressure Point\b', r'\bAuthority Challenge\b',
                                         r'\binstitutional\b']},
    'Loyalty':              {'patterns': [r'\bLoyalty\b'], 'scale': 'pressure_point',
                             'status': 'canonical', 'source': 'seed',
                             'context': [r'\bPressure Point\b', r'\bKnot\b',
                                         r'\brelational\b']},
    # NPCs
    'King Almud':           {'patterns': ['Almud', 'Almqvist'],
                             'scale': 'npc', 'status': 'canonical', 'source': 'seed'},
    'Confessor Arne':       {'patterns': ['Arne', 'Himlensendt', 'Confessor'],
                             'scale': 'npc', 'status': 'canonical', 'source': 'seed'},
    'Inge Baralta':         {'patterns': ['Baralta', r'\bInge\b'],
                             'scale': 'npc', 'status': 'canonical', 'source': 'seed'},
    'Magnus Vaynard':       {'patterns': ['Vaynard', r'\bMagnus\b'],
                             'scale': 'npc', 'status': 'canonical', 'source': 'seed'},
    'Lisbeth Ehrenwall':    {'patterns': ['Ehrenwall', 'Lisbeth'],
                             'scale': 'npc', 'status': 'canonical', 'source': 'seed'},
    'Yrsa Vossen':          {'patterns': [r'\bYrsa\b', 'Vossen'],
                             'scale': 'npc', 'status': 'canonical', 'source': 'seed'},
    'Torben':               {'patterns': [r'\bTorben\b'],
                             'scale': 'npc', 'status': 'canonical', 'source': 'seed'},
    'Elske':                {'patterns': [r'\bElske\b'],
                             'scale': 'npc', 'status': 'canonical', 'source': 'seed'},
    'Edeyja':               {'patterns': [r'\bEdeyja\b'],
                             'scale': 'npc', 'status': 'canonical', 'source': 'seed'},
    'Lenneth':              {'patterns': [r'\bLenneth\b'],
                             'scale': 'npc', 'status': 'canonical', 'source': 'seed'},
    # Factions (disambiguated)
    'Crown':                {'patterns': [r'\bCrown\b(?! Treaty)'], 'scale': 'faction',
                             'status': 'canonical', 'source': 'seed',
                             'context': [r'\bAlmud\b', r'\bfaction\b', r'\bMandate\b',
                                         r'\bTreaty\b', r'\bTorben\b']},
    'Church':               {'patterns': [r'\bChurch\b(?! Influence)'], 'scale': 'faction',
                             'status': 'canonical', 'source': 'seed',
                             'context': [r'\bArne\b', r'\bCardinal\b', r'\bPiety\b',
                                         r'\bHeresy\b', r'\bfaction\b', r'\bConfessor\b',
                                         r'\bdoctrine\b']},
    'Hafenmark':            {'patterns': [r'\bHafenmark\b'],
                             'scale': 'faction', 'status': 'canonical', 'source': 'seed'},
    'Varfell':              {'patterns': [r'\bVarfell\b'],
                             'scale': 'faction', 'status': 'canonical', 'source': 'seed'},
    'Löwenritter':          {'patterns': [r'L[oö]wenritter'],
                             'scale': 'faction', 'status': 'canonical', 'source': 'seed'},
    'Restoration Movement': {'patterns': ['Restoration Movement', r'\bRM\b(?![a-z])'],
                             'scale': 'faction', 'status': 'canonical', 'source': 'seed'},
    'Guilds':               {'patterns': [r'\bGuilds?\b'],
                             'scale': 'faction', 'status': 'canonical', 'source': 'seed'},
    # Cross-cutting
    'Armature System':      {'patterns': ['Armature System', 'Armature'],
                             'scale': 'crosscutting', 'status': 'provisional', 'source': 'seed'},
    'Event Impact Matrix':  {'patterns': ['Event Impact Matrix', 'EventImpact'],
                             'scale': 'crosscutting', 'status': 'provisional', 'source': 'seed'},
    # Mechanics
    'Disposition':          {'patterns': [r'\bDisposition\b'],
                             'scale': 'mechanic', 'status': 'canonical', 'source': 'seed'},
    'Standing':             {'patterns': [r'\bStanding\b'],
                             'scale': 'mechanic', 'status': 'canonical', 'source': 'seed'},
    'Stability':            {'patterns': [r'\bStability\b'],
                             'scale': 'mechanic', 'status': 'canonical', 'source': 'seed'},
    'Mandate':              {'patterns': [r'\bMandate\b'],
                             'scale': 'mechanic', 'status': 'canonical', 'source': 'seed'},
    'Tensions':             {'patterns': [r'\bTensions\b'],
                             'scale': 'mechanic', 'status': 'canonical', 'source': 'seed'},
}


# ──────────────────────────── HELPERS ────────────────────────────────────────

def to_paragraphs(content):
    """Strip HTML comments + code blocks; split on blank lines; min 50 chars."""
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    content = re.sub(r'```.*?```', '\n', content, flags=re.DOTALL)
    paras = re.split(r'\n\s*\n', content)
    return [p.strip() for p in paras if len(p.strip()) > 50]


def neighbors_union(graph, t):
    """In+out neighbor union — accurate degree even for tokens without primary doc."""
    out_nbrs = set(graph.get(t, {}).keys())
    in_nbrs = set(src for src, tgts in graph.items() if t in tgts)
    return out_nbrs | in_nbrs


def to_native(o):
    """Convert numpy types for JSON serialization."""
    if isinstance(o, dict):
        return {k: to_native(v) for k, v in o.items()}
    if isinstance(o, (list, tuple, set)):
        return [to_native(x) for x in o]
    if np is not None and isinstance(o, (np.integer,)):
        return int(o)
    if np is not None and isinstance(o, (np.floating,)):
        return float(o)
    return o


def banner_classify(content, path):
    """Banner-classify a doc: design / discourse / excluded."""
    head = content[:2000]
    # STATUS-FIRST (Fable-5 audit fix): a doc that declares a recognized design/reference status is
    # DESIGN, checked BEFORE the weak AUDIT/WORKPLAN keyword heuristic below — otherwise a
    # REFERENCE/CURRENT-status head (e.g. faction_systems_overview_v30.md) is false-demoted to
    # 'discourse' merely because the word "audit" appears in its scope prose (it cites a
    # designs/audit/ doc). Mirrors gen_audit's ED-IN-0055 status-before-banner precedence;
    # single-sourced here since gen_audit reuses banner_classify. (REFERENCE/CURRENT/WORKING added.)
    if re.search(r'\bSTATUS:\s*(CANONICAL|DESIGN|REFERENCE|CURRENT|WORKING)\b', head, re.I):
        return 'design'
    # STRUCK marker is a CONTENT signal (checked in head); `deprecated/` is a PATH signal
    # (checked in path ONLY). The Fable-5 2026-07-14 audit flagged that matching `deprecated/`
    # against head+path would wrongly EXCLUDE (drop entirely) a live design doc that merely
    # CITES a deprecated/ path in its prose — the same content-substring false-classification
    # class fixed for the AUDIT keyword above. Path-anchoring closes it.
    if re.search(r'\[STRUCK\b', head, re.I) or 'deprecated/' in path.lower():
        return 'excluded'
    if 'STATUS: PROVISIONAL' in head:
        return 'design'
    if re.search(r'\b(WORKPLAN|AUDIT|SESSION CLOSE|STRESS TEST)\b', head, re.I):
        return 'discourse'
    # Audit-corpus path signal. `designs/audit/` retired 2026-07-19 (ED-IN-0071 P4/P5) →
    # the audit corpus is now the top-level `audit/` primary; the old prefix is kept for
    # historical/aliased refs (e.g. archived docs still cited as `designs/audit/…`).
    if path.startswith('audit/') or path.startswith('designs/audit/'):
        if 'development_specification' in path:
            return 'design'
        return 'discourse'
    return 'design'


# ──────────────────────────── STAGE 1 — CORPUS EXTRACTION ────────────────────
# Working-tree only (CLAUDE.md §2: the checkout is authoritative; no GitHub fetch).

_MD_PATH_RE = re.compile(r'(?:design_doc|index|infill|params|spec|related)\s*:\s*'
                         r'([A-Za-z0-9_./-]+\.md)')


def _canonical_paths(root):
    """Every design_doc/params/index/infill .md path named in canonical_sources.yaml,
    plus the foundation + throughline docs the methodology (§3.1) fixes as scope."""
    paths = set()
    cs = root / 'references' / 'canonical_sources.yaml'
    if cs.exists():
        for m in _MD_PATH_RE.finditer(cs.read_text(encoding='utf-8', errors='replace')):
            paths.add(m.group(1))
    # Foundation + framework docs (fixed scope, §3.1).
    for p in ('canon/00_philosophical_foundations.md',
              'canon/01_foundations_amendment_self_rendering.md',
              'canon/02_canon_constraints.md',
              'canon/02_foundations_amendment_leap_mechanism.md',
              'canon/03_canonical_timeline.md',
              'references/throughlines_meta.md',
              'references/throughlines_meta_infill.md',
              # `designs/` retired 2026-07-19 (ED-IN-0071 P4/P5); this reference doc
              # moved to `systems/_architecture/` — the old path was silently `missing`.
              'systems/_architecture/complete_systems_reference.md'):
        paths.add(p)
    return sorted(paths)


def _restructure_remap(root):
    """Old→new path map from `references/restructure_ledger.md` (working tree, root-honoring).
    Only the root-parameterized read is local — this pipeline is `--repo-root` driven while
    broken_dependency_checker's loader is cwd-bound; the non-trivial longest-dir-prefix
    RESOLUTION is reused from bdc below (CLAUDE.md §8, never re-derive a rule)."""
    fp = root / 'references' / 'restructure_ledger.md'
    if not fp.exists():
        return {}
    mapping = {}
    for m in re.finditer(r'^\|\s*`([^`]+)`\s*\|\s*`([^`]+)`\s*\|',
                         fp.read_text(encoding='utf-8', errors='replace'), re.M):
        mapping[m.group(1).strip()] = m.group(2).strip()
    return mapping


def _resolve_live(root, rel, remap):
    """The path that actually EXISTS: literal `rel` if present, else its restructure-ledger
    successor. Self-heals a moved input on the NEXT restructure with no code edit — the class
    of bug behind this run's four hardcoded-path fixes (designs/→systems/, canon/→registers/).
    Returns None only when neither the literal nor a mapped home exists (a true `missing`)."""
    if (root / rel).exists():
        return rel
    mapped = None
    try:
        import broken_dependency_checker as _bdc  # the sanctioned old→new resolver (§8)
        mapped = _bdc._resolve_remap(rel, remap)
    except Exception:
        mapped = remap.get(rel)  # graceful fallback: exact-row only, no dir-prefix
    return mapped if (mapped and (root / mapped).exists()) else None


def extract_corpus(root):
    """Return (design, discourse, manifest): {relpath: content} maps + a manifest dict.
    Banner-classifies each doc (design / discourse / excluded)."""
    design, discourse = {}, {}
    manifest = {'design_files': [], 'discourse_files': [], 'excluded': [], 'missing': []}
    remap = _restructure_remap(root)
    for rel in _canonical_paths(root):
        live = _resolve_live(root, rel, remap)  # self-heal a moved input via the ledger
        if live is None:
            manifest['missing'].append(rel)
            continue
        fp = root / live
        try:
            content = fp.read_text(encoding='utf-8', errors='replace')
        except OSError:
            manifest['missing'].append(rel)
            continue
        cls = banner_classify(content, live)
        rec = {'path': live, 'chars': len(content)}
        if cls == 'excluded':
            manifest['excluded'].append(rel)
        elif cls == 'discourse':
            discourse[rel] = content
            manifest['discourse_files'].append(rec)
        else:
            design[rel] = content
            manifest['design_files'].append(rec)
    manifest['design_count'] = len(design)
    manifest['discourse_count'] = len(discourse)
    manifest['excluded_count'] = len(manifest['excluded'])
    manifest['missing_count'] = len(manifest['missing'])
    # capstone #6 (ED-IN-0056): the L0 corpus is a CURATED slice (`_canonical_paths`), not the
    # whole repo. Quantify what it structurally does NOT see so a green L0 result is never
    # misread as whole-repo coverage. (pathlib-only; skip VCS/cache dirs.)
    # `designs/` retired 2026-07-19 (ED-IN-0071 P4/P5) — the old `designs_total_md`
    # denominator now globs an empty tree, yielding a nonsensical "0.0% of 0" line.
    # Post-retirement the honest denominator is the whole repo; the curated slice draws
    # from `systems/`, `canon/`, `engine/params/`, `arcs/`, `references/`.
    _skip = {'.git', '.pytest_cache', '__pycache__', '.ruff_cache', '.mypy_cache'}
    all_md = [p for p in root.rglob('*.md')
              if not any(part in _skip for part in p.relative_to(root).parts)]
    total_md = len(all_md)
    manifest['coverage'] = {
        'design_files_scanned': len(design),
        'repo_total_md': total_md,
        'pct_of_repo_md': round(100 * len(design) / total_md, 1) if total_md else 0.0,
    }
    return design, discourse, manifest


# ──────────────────────────── STAGE 2 — TOKEN CURATION ───────────────────────

def _compiled(patterns):
    out = []
    for p in patterns:
        try:
            out.append(re.compile(p))
        except re.error:
            out.append(re.compile(re.escape(p)))
    return out


def _count_in(text, compiled):
    return sum(len(rx.findall(text)) for rx in compiled)


def _norm_name(s):
    return re.sub(r'[^a-z0-9]+', ' ', (s or '').lower()).strip()


def _build_coref(root):
    """Alias → canonical map from the LIVE name registries (proper_noun_registry +
    names_index `aliases:`). Authoritative coreference: e.g. both registries declare
    `Baralta` an alias of `Duchess Inge Baralta`, so every surface form of one entity
    resolves to a single canonical. Returns {normalized_surface_form: canonical_label}."""
    coref = {}

    def _ingest(canonical, aliases):
        if not canonical:
            return
        label, _ = _strip_display(canonical)
        for form in [label] + list(aliases or []):
            nf = _norm_name(form)
            if nf and len(nf) >= 3:
                coref.setdefault(nf, label)

    pn = _yaml(root, 'references/proper_noun_registry.yaml')
    for cat in ('characters', 'factions', 'subfactions', 'organizations'):
        for item in (pn.get(cat, {}) or {}).values():
            if isinstance(item, dict):
                _ingest(item.get('canonical'), item.get('aliases'))
    ni = _yaml(root, 'references/names_index.yaml')
    for e in (ni.get('entries', {}) or {}).values():
        if isinstance(e, dict) and e.get('category') in ('proper_noun', 'npc', 'faction', None):
            _ingest(e.get('canonical'), e.get('aliases'))
    return coref


# Scales whose tokens are NAMED ENTITIES — safe to coref-merge by shared proper-noun head.
# Mechanic/system scales are NOT merged ("Combat" ⊂ "Mass Combat" are different mechanics).
_NAME_SCALES = {'npc', 'faction', 'proper_noun', 'character', 'organization'}


def consolidate_tokens(token_defs, coref):
    """Unify every surface form of one named entity into a SINGLE token (user directive
    2026-07-21: "unify and simplify … for names"). Two coreference signals:
      1. registry aliases (authoritative) — forms sharing a `_build_coref` canonical merge;
      2. proper-noun substring — among NAME-scale tokens only, a name that is a contiguous
         whole-word substring of another (`Baralta` ⊂ `Inge Baralta` ⊂ `Duchess Inge Baralta`)
         is the same entity.
    Each group collapses to one token labelled by its canonical (registry canonical if any,
    else the longest/most-specific form) and matched by its HEAD — the shortest form that is a
    whole-word substring of every other form (so a single `\\bBaralta\\b` pattern catches every
    variant exactly once, no over-count). Non-name tokens pass through untouched."""
    names = list(token_defs)
    parent = {n: n for n in names}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        parent[find(a)] = find(b)

    norm = {n: _norm_name(n) for n in names}
    # signal 1: registry-alias coreference (any scale — a declared alias is authoritative)
    canon_group = {}
    for n in names:
        c = coref.get(norm[n])
        if c:
            canon_group.setdefault(_norm_name(c), []).append(n)
    for members in canon_group.values():
        for m in members[1:]:
            union(members[0], m)
    # signal 2: proper-noun substring, NAME scales only — but ONLY when the container is
    # UNIQUE. A form contained in exactly one longer name is that person with a title/surname
    # added (`Inge Baralta` ⊂ `Duchess Inge Baralta`); a form contained in MANY (`Almqvist` ⊂
    # King Almud / Prince Torben / Princess Elske …) is a shared DYNASTY name, not one person —
    # never merge distinct people through a family name.
    name_toks = [n for n in names if (token_defs[n].get('scale') in _NAME_SCALES)]
    for a in name_toks:
        if not norm[a]:
            continue
        containers = [b for b in name_toks
                      if a != b and (' ' + norm[a] + ' ') in (' ' + norm[b] + ' ')]
        if len(containers) == 1:
            union(a, containers[0])

    groups = defaultdict(list)
    for n in names:
        groups[find(n)].append(n)

    out = {}
    for members in groups.values():
        if len(members) == 1:
            out[members[0]] = token_defs[members[0]]
            continue
        # canonical label: a registry canonical among members, else the longest name
        reg_canon = next((coref[norm[m]] for m in members if norm[m] in coref), None)
        label = reg_canon or max(members, key=len)
        # HEAD = shortest member that is a whole-word substring of every other member
        head = None
        for cand in sorted(members, key=len):
            nc = norm[cand]
            if all((' ' + nc + ' ') in (' ' + norm[o] + ' ') for o in members):
                head = cand
                break
        if head:
            patterns = _pattern_for(head)
        else:  # no common head — union every form (word-boundary), deduped
            patterns = sorted({p for m in members for p in _pattern_for(m)})
        # keep the most authoritative member's scale/source/status
        best = min(members, key=lambda m: _source_rank(token_defs[m].get('source')))
        bm = token_defs[best]
        merged = dict(bm)
        merged['patterns'] = patterns
        merged['aliases_merged'] = sorted(set(members))
        out[label] = merged
    return out


def _source_rank(src):
    order = {'derived:proper_noun': 0, 'seed': 1, 'derived:names_index': 2,
             'derived:canonical_sources': 3}
    return order.get(src, 4)


def _passes_context(para, ctx_compiled):
    """Disambiguation (§3.5): a collision token counts in a paragraph only if a
    context pattern is also present."""
    if not ctx_compiled:
        return True
    return any(rx.search(para) for rx in ctx_compiled)


def _yaml(root, rel):
    fp = root / rel
    if not fp.exists():
        return {}
    try:
        return yaml.safe_load(fp.read_text(encoding='utf-8', errors='replace')) or {}
    except Exception:
        return {}


def _strip_display(s):
    """Registry display string -> (bare label, abbreviation|None). Strips markdown
    bold and a trailing '(ABBR)' parenthetical, returning the abbreviation separately
    so it becomes its own match pattern."""
    s = (s or '').replace('*', '').strip()
    m = re.search(r'\(([A-Z][A-Za-z0-9]{1,6})\)\s*$', s)
    abbr = m.group(1) if m else None
    s = re.sub(r'\s*\([^)]*\)\s*$', '', s).strip()
    return s, abbr


def _pattern_for(label, abbr=None):
    """Match patterns for a token label: word-boundary-anchored for short single
    words (avoids substring noise), plain phrase otherwise; abbreviation added
    word-boundary-anchored if present."""
    if not label:
        return []
    esc = re.escape(label)
    pats = [r'\b' + esc + r'\b'] if (' ' not in label and len(label) <= 6) else [esc]
    if abbr:
        pats.append(r'\b' + re.escape(abbr) + r'\b')
    return pats


# Canonical-source `systems:` keys that are lore/meta/migration docs, not mechanics —
# excluded from derivation to keep the token set signal-heavy.
SKIP_SYSTEMS = {
    'module_contracts', 'ui_ux', 'videogame_mode_spec', 'core_engine',
    'narrative_voice_canon', 'solmund_voice', 'solmund_philosophy', 'solmund_artifacts',
    'character_generation_questionnaire', 'character_histories', 'character_canon_consolidation',
    'faction_canon_consolidation', 'political_dynamics_keys_migration',
    'conviction_migration_roster', 'throughlines_framework',
    'tc_political',  # deprecated pre-CI naming variant; the 'CI Political' seed token is canonical
}

_ACRONYMS = {'Npc': 'NPC', 'Ci': 'CI', 'Ms': 'MS', 'Ip': 'IP', 'Ui': 'UI',
             'Ux': 'UX', 'Ap': 'AP', 'Pi': 'PI', 'Ts': 'TS', 'Rm': 'RM'}


def _humanize_system(key):
    """Turn a canonical_sources system key into a display label: drop a trailing
    '_npc' tag, title-case, then restore known acronyms (NPC/CI/MS/…)."""
    key = re.sub(r'_npc$', '', key)
    label = key.replace('_', ' ').title()
    return ' '.join(_ACRONYMS.get(w, w) for w in label.split())


def derive_tokens(root):
    """Build the token table from the LIVE central registries (NS2: derived, not a
    hardcoded frozen list), layered on the curated SEED_TOKENS core. The curated core
    carries the validated §3.5 disambiguation context plus the foundation / 7-Conviction
    / 4-Pressure-Point / clock sets that P2 validation and the class taxonomy depend on,
    and it WINS on any name collision — so the English-word collision tokens
    (Faith/Order/Crown/Church/Evidence/…) keep their disambiguation rather than being
    re-derived context-free. Additive sources: canonical_sources.yaml `systems:`,
    names_index.yaml `entries:` (minus bare attributes, which are grep-noisy),
    proper_noun_registry.yaml characters/factions/subfactions/organizations (minus
    rarely-mentioned entities)."""
    tokens = {name: dict(meta) for name, meta in SEED_TOKENS.items()}
    for m in tokens.values():
        m.setdefault('source', 'seed')
    norm = lambda s: re.sub(r'[^a-z0-9]+', ' ', (s or '').lower()).strip()
    seen = {norm(n) for n in tokens}

    def add(name, patterns, scale, source):
        n = norm(name)
        if not name or not patterns or not n or n in seen or len(name) < 3:
            return
        seen.add(n)
        tokens[name] = {'patterns': patterns, 'scale': scale, 'status': 'canonical',
                        'source': source, 'context': []}

    cs = _yaml(root, 'references/canonical_sources.yaml')
    for key in sorted((cs.get('systems', {}) or {})):
        if key in SKIP_SYSTEMS:
            continue
        label = _humanize_system(key)
        add(label, _pattern_for(label) + [re.escape(key)], 'system', 'derived:canonical_sources')

    _ni_entries = (names.entries(path=str(root / 'references' / 'names_index.yaml')) if names
                   else (_yaml(root, 'references/names_index.yaml').get('entries', {}) or {}))
    for e in _ni_entries.values():
        if not isinstance(e, dict) or e.get('category') == 'attribute':
            continue
        label, abbr = _strip_display(e.get('canonical'))
        pats = _pattern_for(label, abbr) + [re.escape(a) for a in (e.get('aliases') or []) if len(a) >= 4]
        add(label, pats, e.get('category') or 'mechanic', 'derived:names_index')

    pn = _yaml(root, 'references/proper_noun_registry.yaml')
    for cat, scale in (('characters', 'npc'), ('factions', 'faction'),
                       ('subfactions', 'faction'), ('organizations', 'faction')):
        grp = pn.get(cat, {}) or {}
        if not isinstance(grp, dict):
            continue
        for item in grp.values():
            if not isinstance(item, dict):
                continue
            occ = item.get('occurrences_count')
            if isinstance(occ, int) and occ < 5:  # drop barely-present entities (noise)
                continue
            label, _ = _strip_display(item.get('canonical'))
            pats = _pattern_for(label) + [re.escape(a) for a in (item.get('aliases') or []) if len(a) >= 4]
            add(label, pats, scale, 'derived:proper_noun')

    # Coreference consolidation: unify every surface form of one named entity into a
    # single token (registry aliases + proper-noun substring). "Just search Baralta."
    return consolidate_tokens(tokens, _build_coref(root))


def curate_tokens(design, token_defs):
    """Compute per-token paragraph_count and primary_doc against the design corpus
    for the derived token table (see derive_tokens)."""
    paras_by_doc = {d: to_paragraphs(c) for d, c in design.items()}
    tokens = {}
    for name, meta in token_defs.items():
        comp = _compiled(meta['patterns'])
        ctx = _compiled(meta.get('context', []))
        para_count, per_doc = 0, {}
        for doc, paras in paras_by_doc.items():
            doc_hits = 0
            for para in paras:
                if _passes_context(para, ctx) and any(rx.search(para) for rx in comp):
                    para_count += 1
                    doc_hits += 1
            if doc_hits:
                per_doc[doc] = doc_hits
        primary = max(per_doc, key=per_doc.get) if per_doc else None
        tokens[name] = {
            'patterns': meta['patterns'],
            'scale': meta.get('scale'), 'status': meta.get('status'),
            'source': meta.get('source', 'seed'),
            'context': meta.get('context', []),
            'paragraph_count': para_count, 'primary_doc': primary,
            '_compiled': comp, '_ctx': ctx,
        }
    return tokens, paras_by_doc


# ──────────────────────────── STAGE 2.5 — CITATION GRAPH ─────────────────────

def build_g_cite(tokens, design, thresh=2):
    """Directed weighted citation graph. G_cite[A][B] = mentions of token B inside
    token A's primary doc, kept when >= thresh (§3.7). Tokens without a primary doc
    cannot be citation *sources* (§4) but are reached as targets."""
    g = {}
    for a, ma in tokens.items():
        doc = ma['primary_doc']
        if not doc or doc not in design:
            continue
        text = design[doc]
        edges = {}
        for b, mb in tokens.items():
            if b == a:
                continue
            # honor B's disambiguation context at doc granularity
            if mb['_ctx'] and not any(rx.search(text) for rx in mb['_ctx']):
                continue
            c = _count_in(text, mb['_compiled'])
            if c >= thresh:
                edges[b] = c
        if edges:
            g[a] = edges
    return g


# ──────────────────────────── STAGE 4 — METADATA GRAPHS ──────────────────────

_TL_ROW_RE = re.compile(r'^\|\s*(T-\d+)\s*\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|')


def _slug_lookup(tokens):
    """Map a load-bearing-system slug (e.g. 'self_rendering') to a token name."""
    lut = {}
    def norm(s):
        return re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip()
    for name in tokens:
        lut[norm(name)] = name
        for pat in tokens[name]['patterns']:
            bare = re.sub(r'\\b|\(|\)|\[[^\]]*\]|\?|\+|\*|\.', '', pat)
            lut.setdefault(norm(bare), name)
    return lut, norm


def _add_edge(g, a, b):
    if a == b:
        return
    g.setdefault(a, {}).setdefault(b, 0)
    g[a][b] += 1
    g.setdefault(b, {}).setdefault(a, 0)
    g[b][a] += 1


def parse_throughlines(root):
    """Yield (T-id, primary_mu, secondary_mu, [system_slugs]) from the infill table."""
    fp = root / 'references' / 'throughlines_meta_infill.md'
    if not fp.exists():
        return []
    rows = []
    for line in fp.read_text(encoding='utf-8', errors='replace').splitlines():
        m = _TL_ROW_RE.match(line)
        if not m:
            continue
        tid = m.group(1).strip()
        pmu = m.group(3).strip()
        smu = m.group(4).strip()
        systems = [s.strip() for s in re.split(r'[;,]', m.group(6)) if s.strip()]
        rows.append((tid, pmu, smu, systems))
    return rows


def build_g_throughline(rows, tokens):
    lut, norm = _slug_lookup(tokens)
    g = {}
    for _tid, _p, _s, systems in rows:
        members = [lut[norm(s)] for s in systems if norm(s) in lut]
        for i in range(len(members)):
            for j in range(i + 1, len(members)):
                _add_edge(g, members[i], members[j])
    return g


def build_g_mu(rows, tokens):
    """Tokens sharing an Μ mode: collect each Μ field's member-systems across all
    throughlines, connect within the Μ collection."""
    lut, norm = _slug_lookup(tokens)
    by_mu = defaultdict(set)
    for _tid, pmu, smu, systems in rows:
        members = {lut[norm(s)] for s in systems if norm(s) in lut}
        for mu in (pmu, smu):
            mu = mu.strip()
            if mu and mu not in ('—', '-', ''):
                by_mu[mu] |= members
    g = {}
    for members in by_mu.values():
        members = sorted(members)
        for i in range(len(members)):
            for j in range(i + 1, len(members)):
                _add_edge(g, members[i], members[j])
    return g


def build_g_pp(root, tokens):
    """Tokens whose primary docs co-appear in a patch's affects: list (§1 G_pp)."""
    # Moved out of `canon/` to `registers/` (ED-IN-0071 P0, 2026-07-16). The old
    # `canon/` path silently didn't exist → G_pp loaded EMPTY (every `pp` degree a
    # false 0), which corrupted the Mode A/B metadata-graph agreement counts.
    fp = root / 'registers' / 'patch_register_active.yaml'
    doc_to_tokens = defaultdict(list)
    for name, m in tokens.items():
        if m['primary_doc']:
            doc_to_tokens[m['primary_doc']].append(name)
    g = {}
    if not fp.exists():
        return g
    try:
        data = yaml.safe_load(fp.read_text(encoding='utf-8', errors='replace')) or []
    except Exception:
        return g
    entries = data if isinstance(data, list) else data.get('patches', []) or []
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        affects = entry.get('affects', []) or []
        paths = []
        for a in affects:
            if isinstance(a, str):
                paths.append(a)
            elif isinstance(a, dict):
                paths.append(a.get('path') or a.get('file') or '')
        hit = []
        for p in paths:
            for doc, toks in doc_to_tokens.items():
                if p and (p in doc or doc in p):
                    hit.extend(toks)
        hit = sorted(set(hit))
        for i in range(len(hit)):
            for j in range(i + 1, len(hit)):
                _add_edge(g, hit[i], hit[j])
    return g


# ──────────────────────────── STAGE 3 — TF-IDF (supporting, optional) ────────

def build_g_tfidf(tokens, paras_by_doc):
    """Cosine-similarity matrix over per-token TF-IDF vectors. Supporting only
    (§3.6). Degrades to {} if numpy/sklearn are absent — the multi-graph core does
    not depend on it."""
    try:
        import numpy as np
        from sklearn.feature_extraction.text import TfidfVectorizer
    except Exception:
        return {}, False
    all_paras, para_owner = [], []
    for doc, paras in paras_by_doc.items():
        for para in paras:
            all_paras.append(para)
            para_owner.append(doc)
    if len(all_paras) < 3:
        return {}, False
    vec = TfidfVectorizer(lowercase=False, token_pattern=r'(?u)\b\w[\w\-]+\b',
                          min_df=2, max_df=0.5, sublinear_tf=True, norm='l2')
    try:
        X = vec.fit_transform(all_paras)
    except ValueError:
        return {}, False
    names = list(tokens)
    rows = []
    for name in names:
        comp = tokens[name]['_compiled']
        acc = np.zeros(X.shape[1])
        for i, para in enumerate(all_paras):
            w = _count_in(para, comp)
            if w:
                acc += w * X[i].toarray()[0]
        n = np.linalg.norm(acc)
        rows.append(acc / n if n else acc)
    M = np.vstack(rows)
    sim = M @ M.T
    g = {}
    for i, a in enumerate(names):
        for j, b in enumerate(names):
            if i < j and sim[i, j] >= 0.15:
                _add_edge(g, a, b)
    return g, True


# ──────────────────────────── STAGE 5 — VALIDATION ───────────────────────────

FOUNDATION = ['Self-Rendering', 'Leap', 'Coherence', 'Throughlines', 'Ein Sof']


def _median(xs):
    xs = sorted(xs)
    n = len(xs)
    if not n:
        return 0.0
    return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2.0


def validate(tokens, deg_cite, deg_tl, g_cite):
    names = list(tokens)
    found = [t for t in FOUNDATION if t in names]
    f_cite = [deg_cite.get(t, 0) for t in found]
    f_tl = [deg_tl.get(t, 0) for t in found]
    cite_med = _median([deg_cite.get(t, 0) for t in names])
    tl_med = _median([deg_tl.get(t, 0) for t in names])
    f_cite_mean = sum(f_cite) / len(f_cite) if f_cite else 0.0
    f_tl_mean = sum(f_tl) / len(f_tl) if f_tl else 0.0
    p1 = bool(f_cite_mean > cite_med and f_tl_mean > tl_med)

    convs = CLASSES['conviction']
    cd = [deg_tl.get(c, 0) for c in convs]
    mean = sum(cd) / len(cd) if cd else 0.0
    if mean > 0:
        var = sum((x - mean) ** 2 for x in cd) / len(cd)
        cv = (var ** 0.5) / mean
    else:
        cv = 999.0
    p2 = bool(mean > 0 and cv <= 0.5)

    n_edges = sum(len(v) for v in g_cite.values())
    p3 = bool(n_edges >= 100)

    passed = sum([p1, p2, p3])
    return {
        'p1': {'pass': p1, 'foundation_cite_mean': round(f_cite_mean, 3),
               'overall_cite_median': cite_med, 'foundation_tl_mean': round(f_tl_mean, 3),
               'overall_tl_median': tl_med},
        'p2': {'pass': p2, 'conviction_degrees': cd, 'mean': round(mean, 3),
               'cv': round(cv, 3)},
        'p3': {'pass': p3, 'n_cite_edges': n_edges},
        'passed': passed, 'verdict': 'VALIDATED' if passed >= 2 else 'FAILED',
    }


# ──────────────────────────── STAGE 6 — DIAGNOSTICS (A–H) ────────────────────

def _degrees(g, names):
    return {t: len(neighbors_union(g, t)) for t in names}


def _top_quintile(deg):
    vals = sorted(deg.values(), reverse=True)
    if not vals:
        return set()
    k = max(1, len(vals) // 5)
    cut = vals[k - 1]
    return {t for t, d in deg.items() if d >= cut and d > 0}


def _percentile_10_cut(values):
    xs = sorted(values)
    if not xs:
        return 0
    return xs[max(0, int(0.10 * len(xs)) - 1)]


def diagnostics(tokens, graphs, degs):
    names = list(tokens)
    g_cite = graphs['cite']
    dg = {k: degs[k] for k in ('cite', 'throughline', 'mu', 'pp')}
    out = {}

    # A — multi-graph hubs (top quintile in >=3 of 4)
    tq = {k: _top_quintile(dg[k]) for k in dg}
    hubs = []
    for t in names:
        c = sum(1 for k in dg if t in tq[k])
        if c >= 3:
            hubs.append({'token': t, 'in_graphs': c,
                         **{k: dg[k].get(t, 0) for k in dg}})
    out['A_multigraph_hubs'] = sorted(hubs, key=lambda r: (-r['in_graphs'], r['token']))

    # B — implied-but-missing (>=2 metadata graphs link, no cite edge, cross-class)
    def cite_linked(a, b):
        return b in g_cite.get(a, {}) or a in g_cite.get(b, {})
    meta = ('throughline', 'mu', 'pp')
    implied = []
    for a in names:
        for b in names:
            if a >= b or same_class(a, b):
                continue
            links = sum(1 for k in meta if b in graphs[k].get(a, {}))
            if links >= 2 and not cite_linked(a, b):
                implied.append({'a': a, 'b': b, 'meta_links': links})
    out['B_implied_missing'] = sorted(implied, key=lambda r: (-r['meta_links'], r['a'], r['b']))

    # C — notional (cite edge, no metadata support). The itemized list is capped for
    # readability, but the TRUE total is recorded separately so nothing is silently
    # dropped (governance: "never a silent cap — every exclusion logged"). The Fable-5
    # 2026-07-14 audit caught the old `[:25]` destroying the true count (~9k) with no
    # side channel — the scorecard read "25" as if complete.
    notional = []
    for a, edges in g_cite.items():
        for b, w in edges.items():
            if not any(b in graphs[k].get(a, {}) or a in graphs[k].get(b, {}) for k in meta):
                notional.append({'source': a, 'target': b, 'cite_weight': w})
    notional_sorted = sorted(notional, key=lambda r: -r['cite_weight'])
    out['C_notional'] = notional_sorted[:50]
    out['C_notional_total'] = len(notional_sorted)

    # D — cascade-without-return (chains len>=3, no return path)
    sinks = Counter()
    adj = {a: set(g_cite.get(a, {})) for a in names}
    def reaches(start, target):
        stack, seen2 = [start], {start}
        steps = 0
        while stack and steps < 5000:
            steps += 1
            cur = stack.pop()
            for nx in adj.get(cur, ()):
                if nx == target:
                    return True
                if nx not in seen2 and len(seen2) < 200:
                    seen2.add(nx); stack.append(nx)
        return False
    for a in names:
        for b in adj.get(a, ()):
            for c in adj.get(b, ()):
                if c != a and not reaches(c, a):
                    sinks[c] += 1
    sinks_ranked = sinks.most_common()
    out['D_cascade_sinks'] = [{'terminal': t, 'chains': n} for t, n in sinks_ranked[:15]]
    out['D_cascade_sinks_total'] = len(sinks_ranked)   # true total (side channel; not just the shown 15)

    # E — sparse-context (paragraph AND cite-degree in bottom 10th pct)
    pcut = _percentile_10_cut([tokens[t]['paragraph_count'] for t in names])
    dcut = _percentile_10_cut([degs['cite'].get(t, 0) for t in names])
    sparse = [{'token': t, 'paragraphs': tokens[t]['paragraph_count'],
               'cite_deg': degs['cite'].get(t, 0), 'status': tokens[t]['status']}
              for t in names
              if tokens[t]['paragraph_count'] <= pcut and degs['cite'].get(t, 0) <= dcut]
    out['E_sparse_context'] = sorted(sparse, key=lambda r: (r['paragraphs'], r['token']))

    # F, G filled by caller (need corpus / throughline rows)

    # H — multi-graph isolates (max degree <=1 across cite/tl/mu/pp)
    isolates = [{'token': t, **{k: dg[k].get(t, 0) for k in dg}, 'status': tokens[t]['status']}
                for t in names if max(dg[k].get(t, 0) for k in dg) <= 1]
    out['H_isolates'] = sorted(isolates, key=lambda r: r['token'])
    return out


def load_struck_terms(root):
    """Mode G legacy/struck vocabulary. Curated, NOT loaded wholesale from
    references/deprecated_terms_registry.yaml — that register's struck *labels*
    collide with still-canonical words (it lists "Faith"/"Equity"/"Strength" as
    retired Ethical-Framework/attribute labels, but those are live Conviction and
    attribute names), so a bare grep over the full register is noise-dominated.
    These three are the genuinely-struck terms that are NOT names_index `legacy`
    entries — the names_index-tracked deprecations (e.g. the Theocracy→Church
    rename, the deprecated proper noun) are already enforced corpus-wide by the
    hard naming gate (tools/ci_naming_check.py), so Mode G need not (and, to stay
    lint-clean, must not) restate them here. `root` is accepted for signature
    stability / future register-driven curation."""
    return ['Game Master', 'Cultural Reformation', 'Coup Counter']


def vocabulary_debt(design, struck_terms):
    rows = []
    for term in struck_terms:
        rx = re.compile(re.escape(term))
        docs = {}
        for doc, content in design.items():
            n = len(rx.findall(content))
            if n:
                docs[doc] = n
        if docs:
            rows.append({'term': term, 'total': sum(docs.values()),
                         'docs': len(docs),
                         'concentration': sorted(docs.items(), key=lambda kv: -kv[1])[:3]})
    return sorted(rows, key=lambda r: -r['total'])


def throughline_orphans(rows, design):
    """Mode F: throughlines with <=2 substantiating paragraphs (>=2 load-bearing
    systems mentioned in the paragraph)."""
    all_paras = [p for c in design.values() for p in to_paragraphs(c)]
    out = []
    for tid, _p, _s, systems in rows:
        slugs = [re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip() for s in systems]
        subst = 0
        for para in all_paras:
            low = re.sub(r'[^a-z0-9]+', ' ', para.lower())
            if sum(1 for s in slugs if s and s in low) >= 2:
                subst += 1
        if subst <= 2:
            out.append({'throughline': tid, 'systems': systems, 'substantiating': subst})
    return out


# ──────────────────────────── OUTPUT ─────────────────────────────────────────

def _clean_tokens(tokens):
    return {k: {kk: vv for kk, vv in v.items() if not kk.startswith('_')}
            for k, v in tokens.items()}


def write_outputs(out, tokens, manifest, graphs, degs, validation, diag,
                  vocab, orphans, tfidf_on):
    data = out / 'data'
    def dump(name, obj):
        (data / name).write_text(json.dumps(to_native(obj), indent=1), encoding='utf-8')
    dump('corpus_manifest.json', manifest)
    dump('tokens.json', {'tokens': _clean_tokens(tokens)})
    dump('g_cite.json', graphs['cite'])
    dump('g_metadata.json', {'throughline': graphs['throughline'],
                             'mu': graphs['mu'], 'pp': graphs['pp']})
    dump('degrees.json', degs)
    dump('validation.json', validation)
    diag = dict(diag)
    diag['F_throughline_orphans'] = orphans
    diag['G_vocabulary_debt'] = vocab
    dump('multigraph_diagnostics.json', diag)

    # 03_validation_report.md
    vr = ['# Validation report — P1/P2/P3', '',
          f"**Verdict: {validation['verdict']}** ({validation['passed']}/3 passed)",
          "(2/3 required to publish as authoritative; a FAIL is itself a finding — methodology §3.8)", '',
          f"- **P1 foundation-periphery:** {'PASS' if validation['p1']['pass'] else 'FAIL'} — "
          f"foundation cite-mean {validation['p1']['foundation_cite_mean']} vs median "
          f"{validation['p1']['overall_cite_median']}; tl-mean {validation['p1']['foundation_tl_mean']} "
          f"vs median {validation['p1']['overall_tl_median']}",
          f"- **P2 conviction-symmetry:** {'PASS' if validation['p2']['pass'] else 'FAIL'} — "
          f"throughline-degree CV {validation['p2']['cv']} (≤0.5 to pass), degrees "
          f"{validation['p2']['conviction_degrees']}",
          f"- **P3 citation-density:** {'PASS' if validation['p3']['pass'] else 'FAIL'} — "
          f"{validation['p3']['n_cite_edges']} cite token-edges (≥100 to pass)", '',
          f"TF-IDF supporting graph: {'built' if tfidf_on else 'skipped (numpy/sklearn absent)'}."]
    (out / '03_validation_report.md').write_text('\n'.join(vr), encoding='utf-8')

    # 02_weakness_register.md — primary deliverable
    conf = "leads, not verdicts" if validation['verdict'] == 'FAILED' else "structural findings"
    _cov = manifest.get('coverage', {})
    wr = [f'# Weakness register — vector audit v3 ({conf})', '',
          f"Corpus: {manifest['design_count']} design docs, "
          f"{len(tokens)} tokens. Validation: **{validation['verdict']}** "
          f"({validation['passed']}/3). Confidence inherits from validation (methodology §3.8).",
          '',
          f"**Coverage disclosure (capstone #6):** this L0 layer is a CURATED slice — "
          f"{_cov.get('design_files_scanned', manifest['design_count'])} design docs = "
          f"only {_cov.get('pct_of_repo_md', '?')}% of the repo's "
          f"{_cov.get('repo_total_md', '?')} `.md` files. Everything outside `_canonical_paths()` "
          f"(most of `systems/`, all of `engine/params/`/`sim/`/`tests/`/`canon/` prose not named in "
          f"`canonical_sources.yaml`) is structurally invisible to L0 — a green result here is NOT "
          f"whole-repo coverage.",
          f"Scorecard: cite-edges={validation['p3']['n_cite_edges']}, "
          f"hubs={len(diag['A_multigraph_hubs'])}, implied-missing={len(diag['B_implied_missing'])}, "
          f"notional={diag.get('C_notional_total', len(diag['C_notional']))}, "
          f"cascade-sinks={diag.get('D_cascade_sinks_total', len(diag['D_cascade_sinks']))}, "
          f"sparse={len(diag['E_sparse_context'])}, "
          f"isolates={len(diag['H_isolates'])}, vocab-debt-terms={len(vocab)}.", '']
    def section(title, rows, fmt, empty='(none)', total=None):
        # total overrides len(rows) when the caller already capped `rows` upstream (Modes
        # C/D), so the disclosed "… N more" reflects the TRUE count, not the shown slice.
        wr.append(f'## {title}')
        if not rows:
            wr.append(empty)
        else:
            for r in rows[:20]:
                wr.append('- ' + fmt(r))
            shown = min(len(rows), 20)
            true_total = len(rows) if total is None else total
            if true_total > shown:
                wr.append(f'- … {true_total - shown} more (see `data/multigraph_diagnostics.json`)')
        wr.append('')
    section('Mode A — multi-graph hubs (highest change-impact)',
            diag['A_multigraph_hubs'],
            lambda r: f"**{r['token']}** — top-quintile in {r['in_graphs']}/4 "
                      f"(cite {r['cite']}, tl {r['throughline']}, mu {r['mu']}, pp {r['pp']})")
    section('Mode B — implied-but-missing (metadata links, no citation)',
            diag['B_implied_missing'],
            lambda r: f"{r['a']} ↔ {r['b']} ({r['meta_links']} metadata graphs, 0 cite)")
    section('Mode C — notional edges (cited, no metadata support)',
            diag['C_notional'],
            lambda r: f"{r['source']} → {r['target']} (cite weight {r['cite_weight']})",
            total=diag.get('C_notional_total'))
    section('Mode D — cascade sinks (one-way "black holes")',
            diag['D_cascade_sinks'],
            lambda r: f"**{r['terminal']}** — {r['chains']} chains terminate here",
            total=diag.get('D_cascade_sinks_total'))
    section('Mode E — sparse-context tokens (gapped regions)',
            diag['E_sparse_context'],
            lambda r: f"{r['token']} ({r['paragraphs']} paras, cite-deg {r['cite_deg']}, {r['status']})")
    section('Mode F — throughline orphans (≤2 substantiating paragraphs)',
            orphans, lambda r: f"{r['throughline']} — {r['substantiating']} subst. ({', '.join(r['systems'][:4])})")
    section('Mode G — vocabulary debt (struck terms still present)',
            vocab, lambda r: f"**{r['term']}** — {r['total']} in {r['docs']} docs "
                             f"(top: {r['concentration'][0][0]})")
    section('Mode H — multi-graph isolates (structurally disconnected)',
            diag['H_isolates'],
            lambda r: f"{r['token']} (cite {r['cite']}, tl {r['throughline']}, "
                      f"mu {r['mu']}, pp {r['pp']}, {r['status']})")
    (out / '02_weakness_register.md').write_text('\n'.join(wr), encoding='utf-8')


# ──────────────────────────── DRIVER ─────────────────────────────────────────

def run(root, out):
    root, out = Path(root), Path(out)
    (out / 'data').mkdir(parents=True, exist_ok=True)

    print('[stage 1] extracting corpus (working tree)...')
    design, discourse, manifest = extract_corpus(root)
    print(f'          {manifest["design_count"]} design / {manifest["discourse_count"]} discourse '
          f'/ {manifest["missing_count"]} missing')

    print('[stage 2] deriving + curating tokens (registries + seed core)...')
    token_defs = derive_tokens(root)
    tokens, paras_by_doc = curate_tokens(design, token_defs)
    _srcs = Counter(m.get('source', 'seed').split(':')[0] for m in token_defs.values())
    print(f'          {len(tokens)} tokens ({dict(_srcs)})')

    print('[stage 2.5] citation graph...')
    g_cite = build_g_cite(tokens, design)

    print('[stage 4] metadata graphs (throughline / mu / pp)...')
    rows = parse_throughlines(root)
    g_tl = build_g_throughline(rows, tokens)
    g_mu = build_g_mu(rows, tokens)
    g_pp = build_g_pp(root, tokens)

    print('[stage 3] tf-idf (supporting)...')
    g_tfidf, tfidf_on = build_g_tfidf(tokens, paras_by_doc)

    graphs = {'cite': g_cite, 'throughline': g_tl, 'mu': g_mu, 'pp': g_pp, 'tfidf': g_tfidf}
    names = list(tokens)
    degs = {k: _degrees(graphs[k], names) for k in ('cite', 'throughline', 'mu', 'pp', 'tfidf')}

    print('[stage 5] validation...')
    validation = validate(tokens, degs['cite'], degs['throughline'], g_cite)
    print(f'          {validation["verdict"]} ({validation["passed"]}/3)')

    print('[stage 6] diagnostics (8 modes)...')
    diag = diagnostics(tokens, graphs, degs)
    vocab = vocabulary_debt(design, load_struck_terms(root))
    orphans = throughline_orphans(rows, design)

    print('[write] outputs...')
    write_outputs(out, tokens, manifest, graphs, degs, validation, diag,
                  vocab, orphans, tfidf_on)
    print(f'[done] {out}/02_weakness_register.md')
    return validation


def main():
    ap = argparse.ArgumentParser(description='Valoria v3 multi-graph vector audit (working-tree).')
    ap.add_argument('--output-dir', required=True, help='audit output folder')
    ap.add_argument('--mode', default='all', help='(reserved) stage selector')
    ap.add_argument('--repo-root', default='.', help='repo root (working tree)')
    args = ap.parse_args()

    root = Path(args.repo_root)
    if not (root / 'references' / 'canonical_sources.yaml').exists():
        sys.exit(f"not a Valoria repo root (no references/canonical_sources.yaml): {root}")
    print(f"[vector_audit v3] corpus root (working tree): {root.resolve()}")
    run(root, args.output_dir)


if __name__ == '__main__':
    main()
