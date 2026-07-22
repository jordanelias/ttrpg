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
    # the conviction ROSTER is sourced from references/names_index.yaml conv.* entries AFTER
    # SEED_TOKENS (§8; R2/ED-IN-0082) — the hardcoded list moved into the central registry.
    'conviction': [],
    # pressure_point ROSTER sourced from names_index ppt.* below (§8; R2/ED-IN-0082)
    'pressure_point': [],
    # faction ROSTER + disambiguation sourced from names_index world.* entries tagged
    # `token_class: faction` below (§8; R2/ED-IN-0082) — patterns/context migrated verbatim; the
    # world.* proper_noun mirror is undisturbed (canonical unchanged). world.guilds added +
    # mirrored in proper_noun_registry (flagged for Jordan). Order-independent (verified).
    'faction': [],
    # npc ROSTER sourced from names_index world.* entries tagged `token_class: npc` below
    # (§8; R2 namespacing / ED-IN-0082). The former short<->formal reconciliation risk is closed:
    # the entries carry explicit first-name/title patterns (no shared `Almqvist` surname) and the
    # generic-layer token_class-skip stops the double-source that used to collapse coreference.
    'npc': [],
    'clock': ['MS', 'CI', 'IP', 'PI', 'TS', 'TCV'],
    # The performable ACTION vocabulary (verbs) is sourced from references/action_vocabulary.yaml
    # AFTER this literal (§8; R2 / ED-IN-0082) — the hand-list moved OUT of this hardcoded audit
    # into a central (provisional) register. It stays PROVISIONAL because the authoritative
    # `domain_actions` home is unbuilt (ED-FA-0002); when that lands, regenerate the register.
    'action': [],
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
    # Clocks (abbreviations): sourced from names_index clock.* (token_class: clock_track) AFTER
    # this literal (§8; R2/ED-IN-0082) — collision-safe ids for MS/CI/IP/PI/TS/TCV.
    # Convictions: sourced from references/names_index.yaml conv.* entries just AFTER this
    # literal (§8 — the §3.5 disambiguation `context` lives ONCE there; R2/ED-IN-0082).
    # Pressure Points: sourced from references/names_index.yaml ppt.* entries AFTER this literal
    # (§8; R2/ED-IN-0082) — the hardcoded roster + §3.5 context moved into the central registry.
    # NPCs: sourced from references/names_index.yaml world.* entries tagged `token_class: npc`
    # AFTER this literal (§8; R2 namespacing / ED-IN-0082) — the hardcoded roster + short match-
    # forms migrated into the central registry as FIRST-NAME/TITLE patterns (the shared `Almqvist`
    # dynasty surname is dropped, per Jordan 2026-07-22, so distinct royals never collide on it).
    # The coreference-collapse hazard the old deferral note warned about is closed by the
    # token_class-skip in derive_tokens (generic layer no longer double-sources these).
    # Factions: sourced from references/names_index.yaml world.* entries tagged
    # `token_class: faction` AFTER this literal (§8; R2/ED-IN-0082) — roster + custom patterns
    # (negative lookaheads) + §3.5 disambiguation context migrated to the central registry.
    # Cross-cutting
    'Armature System':      {'patterns': ['Armature System', 'Armature'],
                             'scale': 'crosscutting', 'status': 'provisional', 'source': 'seed'},
    'Event Impact Matrix':  {'patterns': ['Event Impact Matrix', 'EventImpact'],
                             'scale': 'crosscutting', 'status': 'provisional', 'source': 'seed'},
    # Mechanics: sourced from references/names_index.yaml mech.* (token_class: mechanic) AFTER this
    # literal (§8; R2 namespacing / ED-IN-0082) — namespaced ids make "Stability"/"Mandate" etc.
    # collision-safe from the faction stats (fac.stability …).
}

# Token classes sourced from references/names_index.yaml (§8 — the class ROSTERS and their §3.5
# disambiguation `context` live ONCE in the central registry; Reconciliation R2 / ED-IN-0082).
# For each class: CLASSES[<cls>] = the ordered display roster; each member's SEED token gets its
# match patterns (the entry's explicit `patterns` if present, else [\bcanonical\b]) + `context`.
# Built byte-identically to the former hardcoded blocks (test_vector_audit pins each). If
# names_index is unreadable (no PyYAML) these degrade to absent — the same failure mode
# derive_tokens already has, since the whole audit reads the index.
_INDEX_TOKEN_CLASSES = ('conviction', 'pressure_point', 'faction', 'mech', 'clock', 'npc')
if names is not None:
    for _cls in _INDEX_TOKEN_CLASSES:
        _members = names.by_token_class(_cls)
        # ordered display roster (index order matches the former hardcoded order, so P2's
        # per-conviction vector and the class taxonomy are unchanged)
        CLASSES[_cls] = [_e['canonical'] for _e in _members.values() if _e.get('canonical')]
        for _e in _members.values():
            _disp = _e.get('canonical')
            if not _disp:
                continue
            SEED_TOKENS[_disp] = {
                'patterns': list(_e.get('patterns') or []) or [r'\b' + _disp + r'\b'],
                'scale': _e.get('scale') or _cls, 'status': 'canonical', 'source': 'seed',
                'context': list(_e.get('context') or [])}

# The performable-action verb roster is sourced from references/action_vocabulary.yaml (§8; the
# provisional central home — see that file's PROVISIONAL banner + ED-FA-0002). It is NOT in
# names_index, so it does NOT go through _INDEX_TOKEN_CLASSES / SEED_TOKENS: the derive_tokens
# ACTIONS loop reads CLASSES['action'] and applies _pattern_for, exactly as before — only the
# roster's HOME moved out of this file. Loaded from the real repo (via __file__) at import.
_ACTION_VOCAB = os.path.join(
    os.path.dirname(_TOOLS_DIR), 'references', 'action_vocabulary.yaml')
try:
    with open(_ACTION_VOCAB, encoding='utf-8') as _af:
        _av = yaml.safe_load(_af) or {}
    CLASSES['action'] = [v for v in (_av.get('verbs') or []) if isinstance(v, str) and v.strip()]
except Exception:  # pragma: no cover — degrade to empty (same failure mode as a missing register)
    CLASSES['action'] = []


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


# Design-content trees the EXTENDED layer (L1) traces — the whole authored DESIGN corpus, not just
# the canonical_sources slice. IMPORTANT SCOPE HONESTY (adversarial-pass H1/H2, 2026-07-22): L1
# extends ONLY the corpus-breadth direction, and within the 4-graph triangulation ONLY the CITE
# graph consumes the doc corpus. The throughline and mu graphs derive from throughlines_meta (a
# registry), and the token universe derives from names_index/proper_noun/module_contracts — NONE of
# those grow with L1. So L1 = more DOCS, same TOKENS, cite-graph only. Narrative (arcs/) and planning
# (workplans/) trees are EXCLUDED: they are not design mechanics, and letting a token's primary_doc
# migrate to a narrative doc would pollute cite with story co-mention (H2). The design corpus is
# systems/engine/canon/godot/proposals.
_L1_TREES = ('systems', 'engine', 'canon', 'godot', 'proposals')
_L1_SKIP_DIRS = {'.git', '.pytest_cache', '__pycache__', '.ruff_cache', '.mypy_cache',
                 'deprecated', 'sim', 'node_modules'}


def _design_tree_paths(root):
    """Every .md under the design-content trees (_L1_TREES) — the L1 extended-corpus scope.
    Co-file _index/_infill halves are INCLUDED (they are authored content). Skips history/tooling."""
    paths = set()
    for tree in _L1_TREES:
        base = root / tree
        if not base.exists():
            continue
        for p in base.rglob('*.md'):
            rel = p.relative_to(root)
            if any(part in _L1_SKIP_DIRS for part in rel.parts):
                continue
            paths.add(str(rel))
    return paths


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


def extract_corpus(root, layer='L0'):
    """Return (design, discourse, manifest): {relpath: content} maps + a manifest dict.
    Banner-classifies each doc (design / discourse / excluded).

    `layer`: 'L0' (default) = the curated canonical_sources slice (~6% of the repo; the validated
    methodology scope). 'L1' = extend the trace to the WHOLE design tree (_design_tree_paths) so
    the graphs trace connections across every authored doc — "extend audit performance in the
    corpus-breadth direction". L0 stays default so P1/P2/P3 calibration + tests are unchanged."""
    design, discourse = {}, {}
    manifest = {'design_files': [], 'discourse_files': [], 'excluded': [], 'missing': [],
                'layer': layer}
    remap = _restructure_remap(root)
    scope = set(_canonical_paths(root))
    if layer == 'L1':
        scope |= _design_tree_paths(root)
    seen_live = set()  # dedup by LIVE path, not scope key (guards the L1 alias↔glob double-count)
    for rel in sorted(scope):
        live = _resolve_live(root, rel, remap)  # self-heal a moved input via the ledger
        if live is None:
            manifest['missing'].append(rel)
            continue
        if live in seen_live:
            continue  # same physical file reached by two scope keys (alias + glob) — read once
        seen_live.add(live)
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


# Canonical-source `systems:` keys NOT tokenized — each paired with WHY (never a silent drop;
# a core purpose of this tool is to SURFACE what is excluded, not hide it — see audit_exclusions()
# and the Incompleteness Ledger). An exclusion is a claim you can audit and challenge, not noise.
SKIP_SYSTEMS_REASONS = {
    'module_contracts': 'index/spine doc, not a mechanic surface (the contracts themselves)',
    'ui_ux': 'presentation-layer spec, not a mechanic',
    'videogame_mode_spec': 'platform/mode spec, not a mechanic',
    'core_engine': 'substrate/kernel doc, not a domain mechanic',
    'narrative_voice_canon': 'voice/style canon, not a mechanic',
    'solmund_voice': 'voice/style canon, not a mechanic',
    'solmund_philosophy': 'philosophy canon, not a mechanic',
    'solmund_artifacts': 'lore artifacts, not a mechanic',
    'character_generation_questionnaire': 'authoring aid, not a mechanic',
    'character_histories': 'lore/backstory, not a mechanic',
    'character_canon_consolidation': 'consolidation/migration doc, not a mechanic',
    'faction_canon_consolidation': 'consolidation/migration doc, not a mechanic',
    'political_dynamics_keys_migration': 'migration doc, not a mechanic',
    'conviction_migration_roster': 'migration roster, not a mechanic',
    'throughlines_framework': 'meta-framework doc, not a mechanic',
    'tc_political': 'DEPRECATED pre-CI naming variant; superseded by the CI Political token',
}
SKIP_SYSTEMS = set(SKIP_SYSTEMS_REASONS)  # keys only, for the fast membership test in derive_tokens

_ACRONYMS = {'Npc': 'NPC', 'Ci': 'CI', 'Ms': 'MS', 'Ip': 'IP', 'Ui': 'UI',
             'Ux': 'UX', 'Ap': 'AP', 'Pi': 'PI', 'Ts': 'TS', 'Rm': 'RM'}


def _humanize_system(key):
    """Turn a canonical_sources system key into a display label: drop a trailing
    '_npc' tag, title-case, then restore known acronyms (NPC/CI/MS/…)."""
    key = re.sub(r'_npc$', '', key)
    label = key.replace('_', ' ').title()
    return ' '.join(_ACRONYMS.get(w, w) for w in label.split())


def derive_tokens(root, record_drops=None):
    """Build the token table from the LIVE central registries (NS2: derived, not a
    hardcoded frozen list), layered on the curated SEED_TOKENS core.

    `record_drops`: optional list; when provided, every candidate the cull rules reject is
    appended (with a reason) so nothing is dropped silently. The returned token table is
    IDENTICAL whether or not recording is on — recording is pure observation (audit_exclusions
    uses it to surface the culls into the Incompleteness Ledger). The curated core
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
        # SURFACE, never silently cull (the tool's purpose is to expose what's missing).
        # When a drop recorder is attached, every rejected candidate is recorded with a reason
        # so audit_exclusions()/the Incompleteness Ledger can list it. The token OUTPUT is
        # unchanged whether or not recording is on — recording is pure observation.
        n = norm(name)
        if not name or not n:
            if record_drops is not None and name:
                record_drops.append({'candidate': str(name), 'scale': scale, 'source': source,
                                     'reason': 'empty_after_normalization'})
            return
        if len(name) < 3:
            if record_drops is not None:
                record_drops.append({'candidate': name, 'scale': scale, 'source': source,
                                     'reason': 'name_shorter_than_3_chars'})
            return
        if not patterns:
            if record_drops is not None:
                record_drops.append({'candidate': name, 'scale': scale, 'source': source,
                                     'reason': 'no_match_patterns'})
            return
        if n in seen:
            return  # dedup of an already-present entity, not a cull of a missing thing
        seen.add(n)
        tokens[name] = {'patterns': patterns, 'scale': scale, 'status': 'canonical',
                        'source': source, 'context': []}

    def alias_pats(aliases, owner):
        """Keep aliases >=4 chars as escaped patterns; RECORD the shorter ones dropped by the
        alias_min_chars floor (F4 — the floor's culling effect is now surfaced, not silent)."""
        kept = []
        for a in (aliases or []):
            if len(a) >= 4:
                kept.append(re.escape(a))
            elif record_drops is not None and len(a) > 0:
                record_drops.append({'candidate': a, 'scale': 'alias', 'source': owner,
                                     'reason': 'alias_shorter_than_4_chars'})
        return kept

    cs = _yaml(root, 'references/canonical_sources.yaml')
    for key in sorted((cs.get('systems', {}) or {})):
        if key in SKIP_SYSTEMS:
            if record_drops is not None:
                record_drops.append({'candidate': _humanize_system(key), 'scale': 'system',
                                     'source': 'canonical_sources:' + key, 'reason': 'skip_systems_denylist',
                                     'detail': SKIP_SYSTEMS_REASONS.get(key, '')})
            continue
        label = _humanize_system(key)
        add(label, _pattern_for(label) + [re.escape(key)], 'system', 'derived:canonical_sources')

    _ni_entries = (names.entries(path=str(root / 'references' / 'names_index.yaml')) if names
                   else (_yaml(root, 'references/names_index.yaml').get('entries', {}) or {}))
    # Expansive token universe (Jordan 2026-07-21): include the PRIMITIVE / stat / definition
    # categories too (attribute, aggregate, faction_stat, settlement_stat, mass_combat_stat,
    # clock, substrate), not just proper_noun — every named definition is a token.
    _PRIMITIVE_CATS = {'attribute', 'aggregate', 'faction_stat', 'settlement_stat',
                       'mass_combat_stat', 'clock', 'substrate'}
    for e in _ni_entries.values():
        if not isinstance(e, dict):
            continue
        if (e.get('token_class') or e.get('category')) in _INDEX_TOKEN_CLASSES:
            # already SEED-sourced with explicit patterns via the _INDEX_TOKEN_CLASSES loop
            # (conviction/faction/mech/clock/…) — don't ALSO derive a context-free token here,
            # which would collide + let coreference pick the wrong surface form (R2 namespacing).
            # Non-sourced token_class values (e.g. clock_full) are NOT skipped — they stay tokens.
            continue
        cat = e.get('category')
        label, abbr = _strip_display(e.get('canonical'))
        pats = _pattern_for(label, abbr) + alias_pats(e.get('aliases'), 'names_index:'+str(label))
        scale = 'primitive' if cat in _PRIMITIVE_CATS else (cat or 'mechanic')
        add(label, pats, scale, 'derived:names_index')

    pn = _yaml(root, 'references/proper_noun_registry.yaml')
    for cat, scale in (('characters', 'npc'), ('factions', 'faction'),
                       ('subfactions', 'faction'), ('organizations', 'faction'),
                       # place names, peoples, concepts, historical figures — the full ontology
                       ('territories', 'place'), ('realms', 'place'), ('regions', 'place'),
                       ('peoples', 'people'), ('concepts', 'concept')):
        grp = pn.get(cat, {}) or {}
        if not isinstance(grp, dict):
            continue
        for item in grp.values():
            if not isinstance(item, dict):
                continue
            # No occurrence floor (Jordan 2026-07-21: "ensure ALL NPCs and movements and
            # concepts and canon stuff"). Every registered named entity is a token, however
            # rarely mentioned — a rarely-cited canon entity is a finding, not noise to drop.
            label, _ = _strip_display(item.get('canonical'))
            pats = _pattern_for(label) + alias_pats(item.get('aliases'), 'proper_noun:'+str(label))
            add(label, pats, scale, 'derived:proper_noun')

    # ── PRIMITIVES / values from descriptor_registry.yaml (attributes + stat rosters) ──
    dr = _yaml(root, 'references/descriptor_registry.yaml')
    prim_rows = []
    attrs = dr.get('attributes', {})
    if isinstance(attrs, dict):
        for grp in ('body', 'mind', 'social'):
            g = attrs.get(grp, {})
            if isinstance(g, dict) and isinstance(g.get('entries'), list):
                prim_rows += g['entries']
    for sect in ('aggregates', 'practitioner_stats', 'territory_stats',
                 'faction_stats', 'settlement_stats'):
        v = dr.get(sect, {})
        e = v.get('entries') if isinstance(v, dict) else None
        if isinstance(e, list):
            prim_rows += e
    for row in prim_rows:
        if not isinstance(row, dict) or not row.get('name'):
            continue
        key = row.get('key')
        pats = _pattern_for(row['name']) + ([re.escape(key)] if key else []) \
            + alias_pats(row.get('aliases'), 'descriptor:'+str(row.get('name')))
        add(row['name'], pats, 'primitive', 'derived:descriptor_registry')

    # ── MECHANICS (modules), KEYS (schema names), VALUES (derivations) from module_contracts ──
    mc = _yaml(root, 'references/module_contracts.yaml')
    keys_seen = set()
    for m in (mc.get('modules', []) or []):
        if not isinstance(m, dict):
            continue
        mod = m.get('module')
        if mod:
            add(_humanize_system(mod), _pattern_for(_humanize_system(mod)) + [re.escape(mod)],
                'mechanic', 'derived:module_contracts')
        for e in (m.get('emits') or []) + (m.get('consumes') or []):
            if isinstance(e, dict) and e.get('type') and e['type'] != '*':
                keys_seen.add(e['type'])
        for d in (m.get('derivations') or []):
            if isinstance(d, dict) and d.get('output'):
                for out in (s.strip() for s in re.split(r'\s*/\s*', d['output'])):
                    if out:
                        add(out, _pattern_for(out), 'value', 'derived:module_contracts')
    for ktype in sorted(keys_seen):
        # a Key like `scene.gossip` — match the identifier and its humanized tail ("gossip")
        tail = _humanize_system(ktype.split('.')[-1])
        add(f'Key: {ktype}', [re.escape(ktype)] + _pattern_for(tail), 'key', 'derived:module_contracts')

    # ── ACTIONS (performable verbs) — "anything that can be performed in a system is a token" ──
    for act in CLASSES['action']:
        add(act, _pattern_for(act), 'action', 'seed:action')

    # Coreference consolidation: unify every surface form of one named entity into a
    # single token (registry aliases + proper-noun substring). "Just search Baralta."
    return consolidate_tokens(tokens, _build_coref(root))


# Methodology floors (documented, not hidden). `enumerated` marks whether audit_exclusions records
# EACH culled item (via record_drops) or only documents the threshold. name<3 + alias<4 are
# enumerated per-item; the two corpus-runtime floors (paragraph<50 in to_paragraphs, citation<2 in
# build_g_cite) are thresholds whose per-item effect is NOT enumerated — honestly noted, not implied
# away (see build_incompleteness COVERAGE_GAPS).
AUDIT_FLOORS = {
    'paragraph_min_chars': {'value': 50, 'enumerated': False},   # to_paragraphs drops shorter blocks
    'citation_min_mentions': {'value': 2, 'enumerated': False},  # build_g_cite drops edges below this
    'alias_min_chars': {'value': 4, 'enumerated': True},         # short registry aliases, recorded
    'name_min_chars': {'value': 3, 'enumerated': True},          # short token names, recorded
}


def audit_exclusions(root):
    """SURFACE everything the token pipeline culls — the whole point of the tool is to expose
    what is missing/excluded, never to hide it. Returns a structured manifest of:
      - skip_systems: the hand-maintained denylist, each with its reason + would-be label
      - dropped_candidates: every registry-derived candidate the cull rules rejected, with reason
      - floors: the corpus-level methodology parameters and their culling effect
    Consumed by the Incompleteness Ledger (build_incompleteness.py) so the culls appear there."""
    from pathlib import Path as _P
    root = _P(root) if not hasattr(root, 'joinpath') else root
    drops = []
    derive_tokens(root, record_drops=drops)  # token output ignored; we want the drop record
    cs = _yaml(root, 'references/canonical_sources.yaml')
    present = set((cs.get('systems', {}) or {}))
    skip = [{'system': k, 'would_be_label': _humanize_system(k),
             'reason': SKIP_SYSTEMS_REASONS.get(k, ''), 'present_in_canonical_sources': k in present}
            for k in sorted(SKIP_SYSTEMS_REASONS)]
    from collections import Counter as _C
    by_reason = _C(d['reason'] for d in drops)
    return {
        'skip_systems': skip,
        'dropped_candidates': drops,
        'dropped_by_reason': dict(by_reason),
        'floors': AUDIT_FLOORS,
        'totals': {'skip_systems': len(skip), 'dropped_candidates': len(drops)},
    }


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

    # P2 v4 (RULED option A, Jordan 2026-07-21 — ED-IN-0080; program doc §5): measure
    # conviction symmetry on CONTEXT-GATED PROSE PRESENCE (paragraph_count, which
    # curate_tokens computes under the §3.5 disambiguation gate), NOT throughline-degree.
    # The v3 throughline formulation was unsatisfiable by construction: the throughline
    # table routes all 7 convictions through the aggregate `conviction_track` slug, so
    # their individual degrees were permanently [0,…,0]. The 0.5 bar is UNCHANGED.
    # Sentinel fix (same ruling): an all-zero vector is NOT MEASURABLE, never
    # "maximally asymmetric" — the cv=999.0 sentinel is retired.
    convs = CLASSES['conviction']
    cd = [(tokens.get(c) or {}).get('paragraph_count', 0) for c in convs]
    mean = sum(cd) / len(cd) if cd else 0.0
    measurable = mean > 0
    if measurable:
        var = sum((x - mean) ** 2 for x in cd) / len(cd)
        cv = (var ** 0.5) / mean
    else:
        cv = None
    p2 = bool(measurable and cv <= 0.5)

    n_edges = sum(len(v) for v in g_cite.values())
    p3 = bool(n_edges >= 100)

    passed = sum([p1, p2, p3])
    return {
        'p1': {'pass': p1, 'foundation_cite_mean': round(f_cite_mean, 3),
               'overall_cite_median': cite_med, 'foundation_tl_mean': round(f_tl_mean, 3),
               'overall_tl_median': tl_med},
        'p2': {'pass': p2, 'measure': 'context_gated_paragraphs', 'measurable': measurable,
               'conviction_presence': cd, 'mean': round(mean, 3),
               'cv': round(cv, 3) if cv is not None else None},
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
    _trunc = [0]  # M2: count reaches() calls that hit the traversal cap — a capped 'False' may be a
                  # FALSE 'does-not-return' (=> false cascade-sink). SURFACE it, never hide it.
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
        if steps >= 5000 or len(seen2) >= 200:
            _trunc[0] += 1   # cap tripped: this False is unreliable
        return False
    for a in names:
        for b in adj.get(a, ()):
            for c in adj.get(b, ()):
                if c != a and not reaches(c, a):
                    sinks[c] += 1
    sinks_ranked = sinks.most_common()
    out['D_cascade_sinks'] = [{'terminal': t, 'chains': n} for t, n in sinks_ranked[:15]]
    out['D_cascade_sinks_total'] = len(sinks_ranked)   # true total (side channel; not just the shown 15)
    out['D_cascade_truncated_calls'] = _trunc[0]       # >0 => some sinks may be cap-artifacts (denser corpora)

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


# ── Token-universe extension: DISCOVER authored terms the registries don't know ──
# The token universe is registry-derived, so a design term never registered is invisible to the
# WHOLE audit (every graph, every layer). This finds candidate terms in the corpus that NO token
# pattern matches — i.e. MISSING REGISTRATIONS — so the audit surfaces what it cannot yet see and
# the terms can be registered (then everything downstream can trace them). Leads, not verdicts.
_CANDIDATE_STOPWORDS = {
    'Status', 'Version', 'Scope', 'Section', 'Overview', 'Design', 'Note', 'Notes', 'Example',
    'Examples', 'Table', 'Figure', 'Appendix', 'Summary', 'Rationale', 'Purpose', 'Goal', 'Goals',
    'Context', 'Background', 'Detail', 'Details', 'Definition', 'Definitions', 'Mechanic',
    'Mechanics', 'System', 'Systems', 'Phase', 'Stage', 'Step', 'Steps', 'Rule', 'Rules', 'Case',
    'Cases', 'Type', 'Types', 'Value', 'Values', 'State', 'States', 'Event', 'Events', 'Action',
    'Actions', 'Result', 'Results', 'Output', 'Input', 'Change', 'Model', 'Layer', 'Track', 'Clock',
    'Key', 'Keys', 'Token', 'Tokens', 'Player', 'Game', 'Turn', 'Round', 'Score', 'Pool', 'Check',
    'Roll', 'Test', 'Tests', 'Tier', 'Level', 'Point', 'Points', 'Count', 'Total', 'Draft', 'Final',
    'Current', 'Canonical', 'Reference', 'Proposed', 'Provisional', 'Open', 'Closed', 'Yes', 'No',
    'The', 'This', 'That', 'When', 'What', 'Where', 'How', 'Why', 'For', 'And', 'But', 'Not',
    # doc-structure / formatting noise (not design concepts) — adversarial-pass (c) expansion
    'Board Game', 'Heading Index', 'Section Sizes', 'Table Of', 'Open Items', 'Year-End',
    'Design Doc', 'Index File', 'Infill File', 'Co-File', 'Design Principle', 'Design Principles',
    'Philosophical Foundations', 'Starting Values', 'Personal Phase', 'Strategic Phase',
    'Cascade Phase', 'Design Note', 'Design Notes', 'Design Goal', 'Design Intent', 'Worked Example',
    'Section Size', 'Line Count', 'Word Count', 'Key Insight', 'Core Loop', 'Core Idea',
    # repudiated / external / generic-TTRPG (NOT candidate registrations)
    'Game Master', 'Player Character', 'Player Characters', 'Non-Player Character',
    'Non-Player Characters', 'Crusader Kings', 'Koei', 'Paradox', 'Total War', 'Martial Law',
    'Royal Decree', 'Real World', 'Real Time', 'Disco Elysium', 'Derived Value', 'Derived Values',
    'Primary Attribute', 'Primary Attributes', 'Worked Examples', 'Hybrid Mode',
}
_CAND_BOLD = re.compile(r'\*\*([A-Z][A-Za-z][A-Za-z0-9 /-]{2,38}[A-Za-z0-9])\*\*')
_CAND_HEAD = re.compile(r'^#{2,5}\s+([A-Z][A-Za-z][A-Za-z0-9 /-]{2,38}[A-Za-z0-9])\s*$', re.M)
_CAND_TITLE = re.compile(r'\b([A-Z][a-z]{2,}(?:[ -][A-Z][a-z]{2,}){1,3})\b')
# a leading article/honorific stripped so "The Church"==Church, "Magnus Vaynard"==Duke … Vaynard
_LEAD_RE = re.compile(r'^(the|a|an|king|queen|prince|princess|duke|duchess|cardinal|confessor'
                      r'|grandmaster|consul|senator|tribune|warden|guildmaster|doux|lord|lady|sir)\s+',
                      re.I)


def _known_ontology(root, token_defs):
    """Every concept the central ontology ALREADY knows: token names+aliases, module ids (raw +
    humanized) + their aliases, descriptor attribute/stat names, and graph node ids/names. A
    candidate matching any of these (name-level, with plural folding) is NOT an unregistered term.
    Fixes the substring predicate (adversarial-pass a): it neither drops a multi-word extension of
    a registered head-word (false-neg) nor re-surfaces a concept another scanner already carries
    (redundancy f)."""
    def norm(s):
        return re.sub(r'[^a-z0-9]+', '', (s or '').lower())
    def fold(s):  # plural-fold each word so "Domain Action" == module "domain_actions"
        return ''.join(re.sub(r's$', '', w) for w in re.sub(r'[^a-z0-9]+', ' ', (s or '').lower()).split())
    known = set()
    def add(s):
        if s:
            known.add(norm(s)); known.add(fold(s))
    # a leading article/honorific-title variant is also "known" (so "The Church" == Church,
    # "Magnus Vaynard" == Duke Magnus Vaynard) — the residual surface-form false-positives.
    def add2(s):
        add(s)
        if s:
            add(_LEAD_RE.sub('', s))
    for name, meta in token_defs.items():
        add2(name)
        for a in (meta.get('aliases_merged') or []):
            add2(a)
    mc = _yaml(root, 'references/module_contracts.yaml') or {}
    for m in (mc.get('modules') or []):
        if isinstance(m, dict) and m.get('module'):
            add(m['module']); add2(_humanize_system(m['module']))
            for a in (m.get('aliases') or []):
                add2(a)
    pn = _yaml(root, 'references/proper_noun_registry.yaml') or {}
    for grp in pn.values():
        if isinstance(grp, dict):
            for item in grp.values():
                if isinstance(item, dict):
                    add2(item.get('canonical'))
                    for a in (item.get('aliases') or []):
                        add2(a)
    dr = _yaml(root, 'references/descriptor_registry.yaml') or {}
    def walk(node):
        if isinstance(node, dict):
            for k, v in node.items():
                if k in ('name', 'key', 'canonical') and isinstance(v, str):
                    add(v)
                walk(v)
        elif isinstance(node, list):
            for it in node:
                walk(it)
    walk(dr)
    g = _load_json_local(root, 'tools/observability/graph.json')
    for grp in ('systems', 'keys', 'scalars'):
        for n in (g.get(grp, []) if g else []):
            add(n.get('id')); add(n.get('name'))
    return known, norm, fold


def _load_json_local(root, rel):
    fp = root / rel
    if not fp.exists():
        return None
    try:
        return json.loads(fp.read_text(encoding='utf-8'))
    except Exception:
        return None


def discover_unregistered_candidates(root, design=None, token_defs=None, min_docs=8):
    """Corpus terms the central ontology does NOT know — candidate MISSING registrations. Uses a
    NAME-LEVEL (not substring) known-set over tokens+modules+descriptors+graph nodes, so it neither
    drops multi-word extensions of a registered head-word nor re-reports concepts other scanners
    already carry. No hard top-N cap (churn-proof: the `min_docs` floor is the only cutoff — a
    boundary tie can't reshuffle a committed slice). Each finding back-links to its top docs.
    (root, or a prebuilt design/token_defs to reuse an in-flight run — the reuse hook is now live.)"""
    from pathlib import Path as _P
    root = _P(root) if not hasattr(root, 'joinpath') else root
    if design is None:
        design, _, _ = extract_corpus(root, layer='L1')
    if token_defs is None:
        token_defs = derive_tokens(root)
    known, norm, fold = _known_ontology(root, token_defs)
    def is_known(term):
        t2 = _LEAD_RE.sub('', term)   # "The Church" -> "Church"; "Magnus Vaynard" stays
        return any(norm(x) in known or fold(x) in known for x in (term, t2))
    doc_count, total, doc_hits = Counter(), Counter(), defaultdict(Counter)
    for doc, content in design.items():
        seen_here = set()
        for rx in (_CAND_BOLD, _CAND_HEAD, _CAND_TITLE):
            for m in rx.finditer(content):
                term = m.group(1).strip().rstrip(' -/')
                if len(term) < 4 or term in _CANDIDATE_STOPWORDS:
                    continue
                if all(w in _CANDIDATE_STOPWORDS for w in term.split()):
                    continue
                total[term] += 1
                doc_hits[term][doc] += 1
                seen_here.add(term)
        for term in seen_here:
            doc_count[term] += 1
    out = []
    for term, dc in doc_count.items():
        if dc < min_docs or is_known(term):
            continue
        top_docs = [d for d, _ in doc_hits[term].most_common(3)]
        out.append({'term': term, 'docs': dc, 'total': total[term], 'top_docs': top_docs})
    out.sort(key=lambda r: (-r['docs'], -r['total'], r['term']))
    return out


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
          f"- **P2 conviction-symmetry (v4, context-gated presence):** "
          + ("NOT MEASURABLE — zero gated presence across all 7 convictions"
             if not validation['p2']['measurable'] else
             f"{'PASS' if validation['p2']['pass'] else 'FAIL'} — "
             f"context-gated paragraph CV {validation['p2']['cv']} (≤0.5 to pass), presence "
             f"{validation['p2']['conviction_presence']}"),
          f"- **P3 citation-density:** {'PASS' if validation['p3']['pass'] else 'FAIL'} — "
          f"{validation['p3']['n_cite_edges']} cite token-edges (≥100 to pass)", '',
          f"TF-IDF supporting graph: {'built' if tfidf_on else 'skipped (numpy/sklearn absent)'}."]
    (out / '03_validation_report.md').write_text('\n'.join(vr), encoding='utf-8')

    # 02_weakness_register.md — primary deliverable
    conf = "leads, not verdicts" if validation['verdict'] == 'FAILED' else "structural findings"
    _cov = manifest.get('coverage', {})
    _layer = manifest.get('layer', 'L0')
    _scope_note = ("the curated `canonical_sources.yaml` slice — most of `systems/`, all of "
                   "`engine/`/`sim/`/`tests/`/`canon/` prose not named there is invisible"
                   if _layer == 'L0' else
                   "the whole DESIGN tree (systems/engine/canon/godot/proposals); still excludes "
                   "arcs/ narrative, workplans/, tests/, deprecated/, audit prose, and non-.md")
    # H1/M1 honesty: name the directions L1 does NOT extend + that validation is L0-calibrated.
    _extend_note = ("L1 extends the corpus-breadth direction and the CITE graph ONLY. NOT extended: "
                    "the throughline & mu graphs (registry-derived from throughlines_meta), the token "
                    "universe (registry-derived; a token absent from names_index/proper_noun/"
                    "module_contracts is invisible at EVERY layer), non-.md content (sim .py, "
                    "engine/params values, the Key propagation graph), and the P1/P2/P3 thresholds "
                    "(calibrated on L0 — the verdict below is NOT re-validated for the L1 corpus)."
                    if _layer == 'L1' else
                    "Directions this tool does not trace at any layer: non-.md content (sim .py, "
                    "typed engine/params, the Key propagation graph) and registry-absent tokens.")
    _run_hint = ("" if _layer == 'L1' else
                 " Run `--layer L1` to extend the CITE trace across the whole design tree "
                 "(L0 stays the validated default; L1 does NOT re-validate).")
    wr = [f'# Weakness register — vector audit v3 ({conf})', '',
          f"Corpus: {manifest['design_count']} design docs, "
          f"{len(tokens)} tokens. Validation: **{validation['verdict']}** "
          f"({validation['passed']}/3){' — L0-calibrated thresholds, NOT re-validated for L1' if _layer=='L1' else ''}. "
          f"Confidence inherits from validation (methodology §3.8).",
          '',
          f"**Coverage disclosure (capstone #6):** layer **{_layer}** traces "
          f"{_cov.get('design_files_scanned', manifest['design_count'])} design docs = "
          f"{_cov.get('pct_of_repo_md', '?')}% of the repo's "
          f"{_cov.get('repo_total_md', '?')} `.md` files — {_scope_note}. A green result at this "
          f"layer is NOT whole-repo coverage.{_run_hint}",
          '',
          f"**Direction disclosure:** {_extend_note}",
          f"Scorecard: cite-edges={validation['p3']['n_cite_edges']}, "
          f"hubs={len(diag['A_multigraph_hubs'])}, implied-missing={len(diag['B_implied_missing'])}, "
          f"notional={diag.get('C_notional_total', len(diag['C_notional']))}, "
          f"cascade-sinks={diag.get('D_cascade_sinks_total', len(diag['D_cascade_sinks']))}, "
          f"sparse={len(diag['E_sparse_context'])}, "
          f"isolates={len(diag['H_isolates'])}, vocab-debt-terms={len(vocab)}.",
          (f"⚠ Mode D reachability hit its traversal cap on {diag['D_cascade_truncated_calls']} "
           f"call(s) — some cascade-sinks may be cap artifacts, not true sinks (denser corpus / L1). "
           f"Treat cascade-sinks as leads here." if diag.get('D_cascade_truncated_calls') else ''),
          '']
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

def run(root, out, layer='L0'):
    root, out = Path(root), Path(out)
    (out / 'data').mkdir(parents=True, exist_ok=True)

    print(f'[stage 1] extracting corpus (working tree, layer {layer})...')
    design, discourse, manifest = extract_corpus(root, layer=layer)
    cov = manifest.get('coverage', {})
    print(f'          {manifest["design_count"]} design / {manifest["discourse_count"]} discourse '
          f'/ {manifest["missing_count"]} missing  ({cov.get("pct_of_repo_md", "?")}% of '
          f'{cov.get("repo_total_md", "?")} repo .md)')

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


def emit_structural_findings(root, out_path, layer='L0'):
    """Write a COMPACT, deterministic feed of the audit's UNIQUE structural findings — Mode B
    (implied-but-missing: two design concepts linked in >=2 metadata graphs but never cited
    together) + Mode H (multi-graph isolates: structurally disconnected tokens). This is how the
    vector-audit TALKS to the Incompleteness Ledger / dashboard: its cross-graph findings, which
    no other tool computes, become surfaced findings. No timestamps (churn-proof). Skips tf-idf
    (supporting-only) for speed."""
    root, out_path = Path(root), Path(out_path)
    design, _, manifest = extract_corpus(root, layer=layer)
    token_defs = derive_tokens(root)
    tokens, _ = curate_tokens(design, token_defs)
    g_cite = build_g_cite(tokens, design)
    rows = parse_throughlines(root)
    graphs = {'cite': g_cite, 'throughline': build_g_throughline(rows, tokens),
              'mu': build_g_mu(rows, tokens), 'pp': build_g_pp(root, tokens)}
    names = list(tokens)
    degs = {k: _degrees(graphs[k], names) for k in ('cite', 'throughline', 'mu', 'pp')}
    diag = diagnostics(tokens, graphs, degs)
    payload = {
        'schema_version': 1,
        'generator': 'skills/valoria-vector-audit/scripts/vector_audit.py --emit-findings',
        'note': 'GENERATED — the vector-audit\'s unique cross-graph structural findings (Mode B '
                'implied-missing + Mode H isolates), for the Incompleteness Ledger to surface. '
                'Layer ' + layer + ' (curated slice — not whole-repo).',
        'layer': layer,
        'design_docs': manifest.get('design_count'),
        'implied_missing': [{'a': r['a'], 'b': r['b'], 'meta_links': r.get('meta_links')}
                            for r in diag.get('B_implied_missing', [])],
        'isolates': [{'token': r['token'], 'status': r.get('status')}
                     for r in diag.get('H_isolates', [])],
    }
    out_path.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
    print(f'[emit] {len(payload["implied_missing"])} implied-missing + {len(payload["isolates"])} '
          f'isolates -> {out_path}')
    return payload


def main():
    ap = argparse.ArgumentParser(description='Valoria v3 multi-graph vector audit (working-tree).')
    ap.add_argument('--output-dir', help='audit output folder (full run)')
    ap.add_argument('--mode', default='all', help='(reserved) stage selector')
    ap.add_argument('--repo-root', default='.', help='repo root (working tree)')
    ap.add_argument('--layer', default='L0', choices=['L0', 'L1'],
                    help="corpus breadth: L0 = curated canonical_sources slice (~6%%, validated "
                         "scope); L1 = extend the trace to the whole design tree (all directions)")
    ap.add_argument('--emit-findings', metavar='PATH',
                    help="write ONLY the compact structural-findings feed (Mode B implied-missing "
                         "+ Mode H isolates) to PATH — for the Incompleteness Ledger to surface")
    args = ap.parse_args()

    root = Path(args.repo_root)
    if not (root / 'references' / 'canonical_sources.yaml').exists():
        sys.exit(f"not a Valoria repo root (no references/canonical_sources.yaml): {root}")
    print(f"[vector_audit v3] corpus root (working tree): {root.resolve()}")
    if args.emit_findings:
        emit_structural_findings(root, args.emit_findings, layer=args.layer)
        return
    if not args.output_dir:
        sys.exit("either --output-dir (full run) or --emit-findings PATH is required")
    run(root, args.output_dir, layer=args.layer)


if __name__ == '__main__':
    main()
