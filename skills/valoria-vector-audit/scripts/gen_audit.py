#!/usr/bin/env python3
"""
gen_audit.py — the Structural Observatory's G_generation layer (NS4 currency).

Companion to structure_audit.py (G_code/L2), pointer_audit.py (G_pointer), and
formula_audit.py (L1). This one answers a different question from all three: not
"is the wiring/registry/formula structure sound" but **"which docs are LIVE
canonical heads vs HISTORICAL records, and do the LIVE heads point at stale
version-pointers?"**

THE CORE PARTITION (get this right — it is the whole point of the tool):
  A stale `*_vNN.md` reference inside a LIVE head is a finding — a reader trusts
  that doc as current canon, so a dead/superseded pointer misleads them (the
  `combat_v30`-partial-supersession class CLAUDE.md §1 flags by name). The
  IDENTICAL reference inside a HISTORICAL record (a ledger, an audit transcript,
  an archived proposal) is correct-as-of-when-written and must NEVER be flagged —
  historical records are allowed, expected, to cite what was true when they were
  written. This tool structurally enforces that: detection 1 (stale pointers)
  only ever runs its scan over the LIVE-classified bucket of the corpus
  partition — a HISTORICAL doc's refs are never even passed to the stale-pointer
  check, not merely filtered out after the fact.

  - **LIVE head:** a doc in `ci_generation_consistency.canonical_docs()` (declared
    authoritative in `references/canonical_sources.yaml`) whose
    `status_of()` is in the recognized current vocabulary (`RECOGNIZED`) AND is
    NOT a `superseded_ids()` entry.
  - **HISTORICAL record:** anything under `deprecated/archives/`, `deprecated/`,
    `designs/audit/`, `registers/handoffs/`, a `registers/editorial_ledger*`/`patch_register`/
    `supersession_register` path, any `superseded_ids()` entry, anything
    `vector_audit.banner_classify()` returns 'discourse'/'excluded' for *that was
    not itself registered as a live head* (the weak banner content-keyword does
    not override an authoritative registration — see the tie-break below), OR —
    the default — anything that is simply not a LIVE head by the definition above
    (registered-but-no-status, registered-but-nonstandard-status, and the vast
    majority of the corpus that was never registered as a canonical head at
    all). **When in doubt this tool classifies HISTORICAL, never LIVE** — a
    false "live" is worse here than a false "historical", because it manufactures
    a stale-pointer finding against a doc nobody claimed was current.

  **Tie-break, made explicit (not hidden):** the AUTHORITATIVE historical
  signals — a `superseded_ids()` entry, a physical archival PATH (`deprecated/archives/`,
  `deprecated/`, `designs/audit/`, `registers/handoffs/`), or a ledger/register path — are
  checked BEFORE strict-LIVE membership in `classify()`, so a doc that IS a strict
  LIVE head (registered, recognized status, not superseded) can still be demoted
  to HISTORICAL and excluded from detection 1's scan when it is physically filed as
  a record. The real, concrete instance in this corpus:
  `designs/audit/2026-05-17-v18-integration/integration_plan_v18.md` is registered
  CANONICAL for a real subsystem yet lives under `designs/audit/`, so the path rule
  demotes it (correctly — a dated plan filed in the audit tree is a record). What
  does NOT demote a live head is `banner_classify()`'s weak CONTENT-keyword
  heuristic: its `AUDIT` regex false-hits the bare word "audit" inside a live
  head's own prose (real instance:
  `designs/factions/faction_systems_overview_v30.md`, a registered REFERENCE head,
  cites a `designs/audit/...` companion doc in its Scope paragraph). Before the
  ED-IN-0055 reconciliation that false-hit demoted the doc; now `live_set`
  membership is checked before the banner heuristic, so an authoritative
  registration wins over a mere prose keyword. `run()` still computes and reports
  the (now path/superseded-only) demoted set every time
  (`live_heads_demoted_by_tiebreak` in the scorecard, its own register section) —
  a known, disclosed under-count of live-head coverage, never a silent one.

REUSE, NOT REIMPLEMENTATION (CLAUDE.md §8 — "every rule lives once"). Three
functions/constants are imported verbatim, never re-derived:
  * tools/ci_generation_consistency.py -> `canonical_docs()` (the authoritative
    live-head design-doc set), `status_of()` (a doc's `## Status:` line),
    `superseded_ids()` (supersession-register file paths), `RECOGNIZED` (the
    current-status vocabulary). This is the ONE currency-rule source.
  * tools/broken_dependency_checker.py -> `extract_file_refs()` (the ONE
    file-reference extractor — backtick/quoted paths under
    designs|compilation|references|canon|tests|skills|tools, plus a few
    `key: path` forms; see that module's docstring) and `get_all_repo_files()`
    (the ONE repo-file-existence set).
  * skills/valoria-vector-audit/scripts/vector_audit.py -> `banner_classify()`
    (the ONE design/discourse/excluded classifier).
  `build_live_heads_meta()` below COMPOSES these four imports client-side
  (`ci_generation_consistency.py`'s own `main()` inlines the identical
  docs/status/superseded loop without exposing it as a function) — no rule is
  re-derived, only recombined from the imported primitives.

DETECTIONS:
  1. **Stale version-pointer in a LIVE head** (`stale_pointers_in_live_heads`):
     for each LIVE head, `extract_file_refs()` its body; for each referenced
     target matching `*_v<digits>....md` (a `_vNN`-style version pointer), flag
     it if the target (a) does not exist on disk, or (b) is a `superseded_ids()`
     entry. This is the `combat_v30`-partial-supersession class — see e.g.
     `designs/provincial/mass_battle_integration_v30.md` citing
     `` `designs/scene/combat_v30.md` `` (a registered `superseded_id`), a real
     instance this tool catches in the live corpus as of this writing. **Triage
     before acting** (same caveat pointer_audit.py/formula_audit.py give their
     own findings): a "nonexistent" row can mean a genuine dead/renamed
     citation (confirmed real instance: `designs/world/insurgency_pipeline_v30.md`
     cites both `designs/audit/2026-05-14-balance-audit/handoff_2026-05-15_v15.md`
     (real, exists) AND `designs/audit/2026-05-15-handoff/handoff_2026-05-15_v15.md`
     (does not — a drifted second citation of the same target) elsewhere in the
     same doc), OR a still-open forward-reference to explicitly-flagged pending
     future work (e.g. `restoration_movement_v30.md "(Pass 2d pending)"` in that
     same doc) — this tool reports both alike as "nonexistent" and does not
     distinguish "broken" from "not written yet".
  2. **Unregistered canonical head** (`scan_unregistered_canonical`): a doc under
     `designs/` (excluding `designs/audit/`, which is historical by definition)
     whose `status_of()` LEADING token (before a ` — `/`(`-style annotation) is
     CANONICAL/CURRENT but which is NOT in `canonical_docs()` — the
     `conviction_track_v1.md`-class gap (PR #131 P1-B: the doc exists,
     self-declares canonical, and is simply missing from
     `canonical_sources.yaml`). Findings split into two sub-buckets (never
     silently merged): genuinely never mentioned in `canonical_sources.yaml`
     (the true P1-B class) vs. mentioned there under a key name
     `canonical_docs()`'s own `DOC_KEYS` regex does not recognize (a blind spot
     in the reused function, not a registration gap) — see
     `_mentioned_in_canonical_sources_raw()`'s docstring for four real,
     observed instances of the latter.
  3. **Currency drift** (`registered_docs & superseded_ids()`): a doc that is
     BOTH registered as a canonical head AND recorded as superseded.
     `ci_generation_consistency.py` already computes and WARNs on this
     (its own `drift` list); this reuses the same two imported sets and reports
     it as its own scorecard line — not a re-derivation, a second view.

GOVERNANCE (mirrors structure_audit.py / pointer_audit.py / formula_audit.py):
  * Working tree only; deterministic; no network; stdlib + PyYAML only (PyYAML
    is a transitive need of the imported modules, not used directly here).
  * MEASURES, NEVER GATES. `tools/ci_generation_consistency.py` is itself the
    (currently WARN-only) CI gate for the currency invariant; this script is a
    read-only observatory view that reuses its exact rule, not a second gate.

KNOWN LIMITATIONS (disclosed up front — under-claim, don't let the critic find
these first):
  * **No `references/head_pointers.yaml` exists yet** (a WS3 artifact). Without
    it, this tool can only tell that a `_vNN.md` target is *nonexistent* or
    *superseded* — it CANNOT detect a reference to a wrong-but-still-existing
    head (e.g. citing an old-but-present version when a newer current head
    exists under a different name/number, or a doc that cites its own
    superseded self correctly-but-confusingly). That whole class of "live but
    wrong" pointer is out of scope until that registry exists.
  * **`extract_file_refs()`'s own scope is inherited, not widened.** It only
    catches backtick/quoted paths (or a handful of `key: path` forms) prefixed
    by one of `designs|compilation|references|canon|tests|skills|tools`. A bare
    inline citation with no directory prefix — e.g. the real corpus's
    `"(derived_stats_v1)"` shorthand in `settlement_layer_v30.md` /
    `player_agency_v30.md` (PR #131's mass_battle G6 finding, `derived_stats_v1`
    ×5) — is textually invisible to the reused extractor and is NOT caught here.
    This is a real, material gap for the exact defect class this tool is meant
    to catch, not a hypothetical one; it inherits directly from reusing the ONE
    extractor rather than writing a second, broader one (which CLAUDE.md §8
    forbids). A future extractor upgrade (or the head_pointers.yaml registry
    above) would close it.
  * **`ci_generation_consistency`'s `canonical_docs()` / `status_of()` /
    `superseded_ids()` hardcode their OWN repo root** (computed from
    `tools/ci_generation_consistency.py`'s own `__file__`), and
    `broken_dependency_checker`'s `get_all_repo_files()` does the same. Neither
    honors a `--repo-root` override. This mirrors pointer_audit.py's identical,
    already-disclosed limitation with `quantity_registry` — `--repo-root` here
    only relocates what THIS script reads directly (the corpus-wide `.md` walk
    for the LIVE/HISTORICAL partition, and detection 2's `designs/` walk); the
    currency-rule primitives themselves always see the real checkout. In normal
    use (`--repo-root .` from the real checkout) these are the same tree, so
    this is latent, not live, in the common case — but a test fixture or a
    second worktree would see it diverge.
  * **Detection 2 inherits the same hardcoded-root limitation** for its
    `status_of()` calls specifically (each candidate path is looked up against
    the real checkout regardless of `--repo-root`); a `FileNotFoundError` there
    is swallowed (skip, not a crash) rather than invented as a finding.
  * **Version-pointer target matching is textual, not semantic**: any ref whose
    final path segment matches `_v<digits>...\.md` is treated as a version
    pointer, matching the class of filename this repo actually uses
    (`_v30.md`, `_v1.md`, `_v30_index.md`, …). A `.md` target that legitimately
    encodes a version-like number for an unrelated reason would be swept in too
    — not observed in practice, but not excluded by construction either.

CLI:
    python3 gen_audit.py --repo-root . --output-dir <run>
"""
import argparse
import json
import os
import re
import sys
from pathlib import Path

# Import the ONE currency-rule source + the ONE ref-extractor/file-set + the ONE
# banner classifier — never re-derive any of the three (CLAUDE.md §8).
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPT_DIR not in sys.path:
    sys.path.insert(0, _SCRIPT_DIR)
_STATIC_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_SCRIPT_DIR)))
_TOOLS_DIR = os.path.join(_STATIC_REPO_ROOT, 'tools')
if _TOOLS_DIR not in sys.path:
    sys.path.insert(0, _TOOLS_DIR)

import ci_generation_consistency as gc        # noqa: E402  (the ONE currency-rule source)
import broken_dependency_checker as bdc       # noqa: E402  (the ONE ref-extractor / file-set)
import vector_audit as va                     # noqa: E402  (the ONE banner classifier, same scripts/ dir)


# ──────────────────────────── PARTITION (LIVE vs HISTORICAL) ─────────────────

_HISTORICAL_PATH_PREFIXES = ('deprecated/archives/', 'deprecated/', 'designs/audit/', 'registers/handoffs/')
# Ephemeral / gitignored build+cache dirs: they are not part of the design corpus
# and their presence varies by environment (a fresh CI clone has no `.pytest_cache`),
# so walking them would make the HISTORICAL count non-deterministic across machines
# (agonist-antagonist reconciliation 2026-07-13, ED-IN-0055 — antagonist found
# `.pytest_cache/README.md` polluting the partition on a local tree).
_SKIP_WALK_DIRS = {'.git', '.pytest_cache', '__pycache__', '.ruff_cache',
                   '.mypy_cache', '.hypothesis', 'node_modules'}


def build_live_heads_meta(registered_docs, superseded_set):
    """{relpath: status} for docs that qualify as LIVE heads (recognized status,
    not superseded), plus {relpath: reason} for registered docs that do NOT
    qualify (superseded / no status / nonstandard status) — this second map is
    reported as a lower-confidence bucket, not silently dropped.

    Composes `gc.canonical_docs()` / `gc.status_of()` / `gc.superseded_ids()` /
    `gc.RECOGNIZED` exactly as `ci_generation_consistency.main()` does inline —
    that module does not expose its own loop as a function, so this recombines
    the imported primitives rather than reimplementing the rule they encode.
    """
    live, non_live = {}, {}
    for d in sorted(registered_docs):
        if d in superseded_set:
            non_live[d] = 'superseded'
            continue
        s = gc.status_of(d)
        if s is None:
            non_live[d] = 'no_status'
        elif any(k in s.upper() for k in gc.RECOGNIZED):
            live[d] = s
        else:
            non_live[d] = 'nonstandard_status:' + s
    return live, non_live


def classify(relpath, content, live_set, superseded_set):
    """(bucket, reason) for one doc — 'live' or 'historical'. Pure function of
    its arguments (no disk access, no hidden global state) so it is directly
    unit-testable against synthetic fixtures. `live_set` is the precomputed
    LIVE-head path set (see build_live_heads_meta); everything not in it is
    HISTORICAL by default, per the "when in doubt, HISTORICAL" rule.

    Signal precedence (agonist-antagonist reconciliation 2026-07-13, ED-IN-0055).
    The AUTHORITATIVE historical signals win even over strict-LIVE membership: a
    `superseded_ids()` entry, a physical archival PATH (`deprecated/archives/`, `deprecated/`,
    `designs/audit/`, `registers/handoffs/`), or a ledger/register path — a doc physically
    filed under `designs/audit/` is a historical record whatever its `## Status:`
    line claims (real instance: `integration_plan_v18.md`, registered CANONICAL yet
    filed under `designs/audit/`). But `banner_classify()`'s CONTENT-keyword
    heuristic is weak and substring-based — its `AUDIT` regex false-hits the bare
    word "audit" inside a live head's own prose (real instance:
    `designs/factions/faction_systems_overview_v30.md`, a registered REFERENCE head,
    cites a `designs/audit/...` companion doc in its Scope paragraph). A weak
    content keyword must NOT override an authoritative live-head registration, so
    `live_set` membership is checked BEFORE the banner heuristic — which then only
    tiebreaks docs that were never registered as canonical heads at all."""
    if relpath in superseded_set:
        return 'historical', 'superseded_id'
    if relpath.startswith(_HISTORICAL_PATH_PREFIXES):
        return 'historical', 'archival_path'
    if (relpath.startswith('registers/') or relpath.startswith('canon/')) and any(
            s in relpath for s in ('editorial_ledger', 'patch_register', 'supersession_register')):
        return 'historical', 'ledger_or_register'
    if relpath in live_set:
        return 'live', 'canonical_head'
    bc = va.banner_classify(content, relpath)
    if bc in ('discourse', 'excluded'):
        return 'historical', 'banner_' + bc
    return 'historical', 'not_a_live_head'


def iter_markdown_files(root):
    """Every `.md` file under `root` (repo-relative, `/`-separated), skipping VCS
    and ephemeral cache dirs (`_SKIP_WALK_DIRS` — `.git`, `.pytest_cache`,
    `__pycache__`, …) that are gitignored build noise rather than corpus. This is
    THIS script's own corpus enumeration (not one of the three reused primitives)
    — it honors `--repo-root` even though the currency-rule functions it feeds into
    do not (see module docstring)."""
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in _SKIP_WALK_DIRS]
        for fn in filenames:
            if fn.endswith('.md'):
                yield os.path.relpath(os.path.join(dirpath, fn), root).replace(os.sep, '/')


def _read(root, relpath):
    try:
        return (root / relpath).read_text(encoding='utf-8', errors='replace')
    except OSError:
        return None


def partition_corpus(root, live_set, superseded_set):
    """Classify every `.md` file in the working tree into live/historical.
    Returns (partition: {'live': [...], 'historical': [...]}, reason_counts:
    {reason: count}, per_file_reason: {relpath: reason}, live_contents:
    {relpath: content} for the live bucket only — the exact set detection 1 is
    allowed to see).

    NOTE — a `live_set` member can still land in the 'historical' bucket, but ONLY via an
    AUTHORITATIVE signal: `classify()` checks superseded_id / archival-path-prefix / ledger
    BEFORE `live_set` membership, and checks `live_set` membership BEFORE the weak
    `banner_classify` content heuristic (the ED-IN-0055 fix — an authoritative registration
    must not be demoted by a mere prose keyword like a stray "audit" in the doc's scope
    text). So a registered live head is demoted only by a genuine path/superseded/ledger
    signal, never by banner_classify alone. `run()` below computes exactly which `live_set`
    members are demoted and reports them explicitly (never silently dropped) — see the
    'live heads demoted by a historical-path signal' section of the register."""
    partition = {'live': [], 'historical': []}
    reason_counts = {}
    per_file_reason = {}
    live_contents = {}
    for relpath in sorted(iter_markdown_files(root)):
        content = _read(root, relpath)
        if content is None:
            continue
        bucket, reason = classify(relpath, content, live_set, superseded_set)
        partition[bucket].append(relpath)
        reason_counts[reason] = reason_counts.get(reason, 0) + 1
        per_file_reason[relpath] = reason
        if bucket == 'live':
            live_contents[relpath] = content
    return partition, reason_counts, per_file_reason, live_contents


# ──────────────────────────── DETECTION 1 — STALE VERSION-POINTERS ───────────

_VERSION_TARGET_RE = re.compile(r'_v\d+[A-Za-z0-9_]*\.md$')


def _is_version_pointer(ref):
    """A `*_vNN.md`-style target: some `_v<digits>` marker immediately before a
    trailing `.md` (matches this repo's real convention — `_v30.md`, `_v1.md`,
    `_v30_index.md`, `_v30_infill.md`, …).

    KNOWN UNDER-MATCH (ED-IN-0055 disclosure, deliberately NOT broadened): only the
    underscore-suffix convention is recognized. Two other version-in-filename shapes
    exist in this repo — PREFIX-style (`v40_generation_plan.md`, `v32_bout_…md`) and
    HYPHEN-style (`…-v3_1.md`) — and are invisible here. Left as-is on purpose: those
    are plan/audit artifacts, not subsystem heads, and every current citation of them
    lands in `designs/audit/` (a HISTORICAL doc detection 1 never scans), so nothing
    is silently dropped today. Broadening to a bare `vNN` anywhere would false-match
    unrelated filenames — over-match is the worse failure for a currency signal — so
    this stays a disclosed gap, re-checked if such a file ever becomes a live head."""
    return bool(_VERSION_TARGET_RE.search(ref))


def stale_pointers_in_live_heads(live_contents, all_files, superseded_set, restructure_map=None):
    """The core detection. `live_contents` MUST already be filtered to the LIVE
    bucket only (see partition_corpus) — this function does not itself
    re-check liveness, so a HISTORICAL doc's refs are structurally never
    passed in, not merely filtered out afterward. Deterministic order.

    Severity triage (agonist-antagonist reconciliation 2026-07-13, ED-IN-0055).
    A cited `*_vNN.md` target that is not on disk is NOT automatically a dead
    reference: `references/restructure_ledger.md` maps sanctioned repo-restructure
    moves OLD->NEW, and the majority of "missing" live-head citations are simply a
    live head still naming a doc's PRE-restructure path whose successor exists right
    now. This reuses `broken_dependency_checker._load_restructure_map()` — the SAME
    map `bdc.check_editorial_ledger()` consults for exactly this disambiguation
    (§8 "every rule lives once"; not a second parser) — to split the old flat
    'nonexistent' bucket into three honestly-different severities:
      * 'superseded'  — target exists on disk but is a supersession-register entry;
      * 'moved'       — target missing, but the restructure ledger maps it to a NEW
                        path that exists on disk: a trivial mechanical repoint to a
                        KNOWN target (`new_home`), low-effort cleanup, not a hunt;
      * 'nonexistent' — target missing AND no restructure-ledger successor exists
                        (genuinely dead / never-written / typo — needs human triage).
    All three are still stale pointers a live head should not carry, but the split
    tells a cleanup pass which are one-line repoints and which need investigation —
    without it, >half of this corpus's findings mislabel a known rename as 'dead'.
    `restructure_map` defaults to {} so unit fixtures stay hermetic; `run()` passes
    the real `bdc._load_restructure_map()`."""
    remap = restructure_map or {}
    findings = []
    for relpath in sorted(live_contents):
        content = live_contents[relpath]
        for ref in sorted(bdc.extract_file_refs(content, relpath)):
            if not _is_version_pointer(ref):
                continue
            if ref in all_files:
                if ref in superseded_set:
                    findings.append({'live_head': relpath, 'ref': ref, 'reason': 'superseded'})
                continue
            new_home = remap.get(ref)
            if new_home and new_home in all_files:
                findings.append({'live_head': relpath, 'ref': ref, 'reason': 'moved',
                                 'new_home': new_home})
            else:
                findings.append({'live_head': relpath, 'ref': ref, 'reason': 'nonexistent'})
    return findings


# ──────────────────────────── DETECTION 2 — UNREGISTERED CANONICAL HEAD ──────

_STATUS_LEAD_SPLIT_RE = re.compile(r'\s+—\s+|\s+--\s+|\s+-\s+|\(')


def _leading_status_token(s):
    """The primary status word/phrase before a ' — '/'--'/'('-style annotation
    — e.g. `status_of()` returning 'SUPERSEDED — canonical doc is X' must NOT
    be read as this doc declaring itself canonical; its leading token is
    'SUPERSEDED'. A naive substring search for "CANONICAL"/"CURRENT" over the
    FULL status string false-positives on exactly this shape (observed for
    real in this corpus — `designs/npcs/npc_behavior_system_v1.md`'s
    `SUPERSEDED — canonical doc is designs/systems/npc_behavior_v30.md ...`,
    and `designs/architecture/governance_consolidation_v1.md`'s
    `D1–D6 RATIFIED (... is canonical, on the explicit condition ...)`) — this
    split is the fix, applied only to THIS detection's own bespoke
    CANONICAL/CURRENT check, not to `gc.RECOGNIZED` membership (untouched,
    still the imported rule)."""
    return _STATUS_LEAD_SPLIT_RE.split(s.strip(), maxsplit=1)[0].strip().upper()


def _mentioned_in_canonical_sources_raw(root):
    """Raw text of `<root>/references/canonical_sources.yaml`. Unlike
    `gc.canonical_docs()`/`gc.status_of()`/`gc.superseded_ids()` (which always
    read `gc.CANON_SOURCES`/`gc.ROOT`, hardcoded from
    tools/ci_generation_consistency.py's own `__file__`), this is a plain file
    read with no reuse obligation forcing it through that hardcoded constant —
    so it genuinely honors `--repo-root`/`root`, unlike those three. Used only
    to tell apart, among detection-2 findings, 'genuinely never mentioned'
    (the true `conviction_track_v1.md` class) from 'mentioned in
    canonical_sources.yaml, but under a key name `canonical_docs()`'s
    `DOC_KEYS` regex does not match' (e.g. `adjacency:`, `fractional:`,
    `social_contest_design:` — none contain the substrings
    design_doc/index/infill/integration_plan_doc/spec/related that regex
    requires). Real, observed against the actual repo root: `settlement_adjacency_v30.md`,
    `fractional_province_ownership_v30.md`, `march_layer_v30.md`, and
    `social_contest_v30.md` — a CURRENT.md-listed head — are ALL mentioned in
    canonical_sources.yaml yet invisible to `canonical_docs()` for this exact
    reason. This is informational context only; it does not change whether a
    doc is reported as a finding (the detection's contract is membership in
    `canonical_docs()`, not in the raw file), and it is NOT a fix to
    `canonical_docs()`'s regex (that rule lives once, in
    tools/ci_generation_consistency.py — CLAUDE.md §8) — only a disclosure
    that the regex has a real, material blind spot."""
    try:
        return (Path(root) / 'references' / 'canonical_sources.yaml').read_text(
            encoding='utf-8', errors='replace')
    except OSError:
        return ''


def scan_unregistered_canonical(root, registered_docs):
    """A doc under designs/ (excluding designs/audit/, historical by
    definition) whose Status line's LEADING token is CANONICAL/CURRENT but the
    doc is absent from canonical_docs(). `gc.status_of()` reads the real repo
    root regardless of `root` (see module docstring); a path that does not
    resolve there is skipped, not fabricated as a finding.

    DISCLOSED, NOT REPRODUCED: the motivating PR #131 P1-B example itself,
    `designs/personal/conviction_track_v1.md`, states its status as
    `<!-- STATUS: CANONICAL — ... -->` (an HTML-comment convention) rather
    than a `## Status:` markdown line. `gc.status_of()`'s regex anchors at the
    start of the line and requires (whitespace/`#`)* then literal "Status" —
    the HTML comment prefix `<!--` breaks that match, so `status_of()` returns
    None for this file and detection 2 CANNOT flag it. This is a real,
    material gap inherited from reusing `status_of()` verbatim rather than
    writing a second, laxer status-line parser (which CLAUDE.md §8 forbids) —
    disclosed here rather than left for the critic to discover."""
    findings = []
    designs_root = root / 'designs'
    if not designs_root.exists():
        return findings
    cs_raw = _mentioned_in_canonical_sources_raw(root)
    for dirpath, dirnames, filenames in os.walk(designs_root):
        rel_dir = os.path.relpath(dirpath, root).replace(os.sep, '/')
        if rel_dir == 'designs':
            dirnames[:] = [d for d in dirnames if d != 'audit']
        for fn in sorted(filenames):
            if not fn.endswith('.md'):
                continue
            relpath = os.path.relpath(os.path.join(dirpath, fn), root).replace(os.sep, '/')
            if relpath.startswith('designs/audit/') or relpath in registered_docs:
                continue
            try:
                s = gc.status_of(relpath)
            except OSError:
                continue
            if not s:
                continue
            if _leading_status_token(s) in ('CANONICAL', 'CURRENT'):
                findings.append({
                    'path': relpath, 'status': s,
                    'mentioned_in_canonical_sources_under_unrecognized_key': relpath in cs_raw,
                })
    return sorted(findings, key=lambda f: f['path'])


# ──────────────────────────── OUTPUT ─────────────────────────────────────────

def run(root, out):
    root, out = Path(root), Path(out)
    (out / 'data').mkdir(parents=True, exist_ok=True)

    print('[G_generation] resolving the LIVE-head set (tools/ci_generation_consistency.py)...')
    registered_docs = set(gc.canonical_docs())
    superseded_set = set(gc.superseded_ids())
    live_heads_meta, non_live_canonical = build_live_heads_meta(registered_docs, superseded_set)
    print(f'               {len(registered_docs)} registered canonical docs; '
          f'{len(live_heads_meta)} qualify as LIVE heads; '
          f'{len(non_live_canonical)} registered-but-not-live (no-status / nonstandard / superseded)')

    print('[G_generation] partitioning the working tree (.md corpus) into LIVE / HISTORICAL...')
    partition, reason_counts, per_file_reason, live_contents = partition_corpus(
        root, set(live_heads_meta), superseded_set)
    print(f'               {len(partition["live"])} live / {len(partition["historical"])} historical '
          f'({len(partition["live"]) + len(partition["historical"])} .md files classified)')

    # live_heads_meta is the STRICT currency-rule set (registered + recognized status +
    # not superseded); partition['live'] additionally applies the path/banner tie-break
    # (see classify()'s docstring), so a strict-live doc CAN be demoted to historical.
    # Surfaced explicitly, never silently dropped.
    demoted_live_heads = [{'path': d, 'reason': per_file_reason.get(d, 'unknown')}
                          for d in sorted(set(live_heads_meta) - set(partition['live']))]
    if demoted_live_heads:
        print(f'               NOTE: {len(demoted_live_heads)} strict-LIVE doc(s) demoted to HISTORICAL '
              f'by a path/banner tie-break signal (not scanned for stale pointers) — see register')

    print('[G_generation] detection 1: stale version-pointers inside LIVE heads...')
    all_files = bdc.get_all_repo_files()
    restructure_map = bdc._load_restructure_map()   # reuse the sanctioned OLD->NEW move map (§8)
    stale = stale_pointers_in_live_heads(live_contents, all_files, superseded_set, restructure_map)
    stale_heads = sorted({s['live_head'] for s in stale})
    stale_by_reason = {}
    for s in stale:
        stale_by_reason[s['reason']] = stale_by_reason.get(s['reason'], 0) + 1
    print(f'               {len(stale)} stale pointer(s) across {len(stale_heads)} live head(s) — '
          f'{stale_by_reason.get("superseded", 0)} superseded, '
          f'{stale_by_reason.get("moved", 0)} moved (successor exists, trivial repoint), '
          f'{stale_by_reason.get("nonexistent", 0)} genuinely nonexistent')

    print('[G_generation] detection 2: unregistered canonical heads (designs/, excluding designs/audit/)...')
    unregistered = scan_unregistered_canonical(root, registered_docs)
    print(f'               {len(unregistered)} unregistered-canonical doc(s)')

    print('[G_generation] detection 3: currency drift (registered AND superseded)...')
    drift = sorted(registered_docs & superseded_set)
    print(f'               {len(drift)} currency-drift doc(s)')

    scorecard = {
        'live_head_count': len(partition['live']),
        'historical_count': len(partition['historical']),
        'md_files_classified': len(partition['live']) + len(partition['historical']),
        'live_heads_strict_count': len(live_heads_meta),
        'live_heads_demoted_by_tiebreak': len(demoted_live_heads),
        'registered_canonical_docs': len(registered_docs),
        'registered_but_not_live': len(non_live_canonical),
        'stale_pointers_in_live_heads': len(stale),
        'stale_pointers_superseded': stale_by_reason.get('superseded', 0),
        'stale_pointers_moved_successor_exists': stale_by_reason.get('moved', 0),
        'stale_pointers_nonexistent': stale_by_reason.get('nonexistent', 0),
        'live_heads_with_a_stale_pointer': len(stale_heads),
        'unregistered_canonical_heads': len(unregistered),
        'currency_drift_docs': len(drift),
    }

    # ---- JSON (single artifact, per spec) ----
    (out / 'data' / 'g_generation.json').write_text(json.dumps({
        'scorecard': scorecard,
        'partition_reason_counts': reason_counts,
        'live_heads_strict': live_heads_meta,
        'live_heads_demoted_by_tiebreak': demoted_live_heads,
        'registered_but_not_live': non_live_canonical,
        'partition': partition,
        'stale_pointers': stale,
        'unregistered_canonical': unregistered,
        'currency_drift': drift,
    }, indent=1, sort_keys=True), encoding='utf-8')

    # ---- register (primary deliverable) ----
    L = []
    L.append('# Generation register — G_generation currency layer (NS4)')
    L.append('')
    L.append('Deterministic, working-tree only. **Measures; does not gate** — '
             '`tools/ci_generation_consistency.py` is the (WARN-only) gate for the currency '
             'invariant this reuses. LIVE head = registered in `references/canonical_sources.yaml` '
             '(`canonical_docs()`), recognized `## Status:` (`status_of()`/`RECOGNIZED`), and NOT a '
             '`superseded_ids()` entry — everything else, including registered-but-unrecognized-status '
             'docs, is HISTORICAL by default (never flagged for a stale pointer). See the script '
             'docstring for the disclosed scope limits (no `head_pointers.yaml` yet; '
             '`extract_file_refs()` only catches directory-prefixed, quoted/backtick paths — a bare '
             'shorthand citation like `derived_stats_v1` with no path is invisible to it).')
    L.append('')
    L.append(f'**Scorecard:** live-heads={scorecard["live_head_count"]} '
             f'(strict currency-rule count {scorecard["live_heads_strict_count"]}, '
             f'{scorecard["live_heads_demoted_by_tiebreak"]} demoted by the path/banner tie-break — '
             f'see below), historical={scorecard["historical_count"]} '
             f'(of {scorecard["md_files_classified"]} `.md` files classified); '
             f'registered-canonical-docs={scorecard["registered_canonical_docs"]} '
             f'({scorecard["registered_but_not_live"]} registered-but-not-live); '
             f'stale-pointers-in-live-heads={scorecard["stale_pointers_in_live_heads"]} '
             f'(across {scorecard["live_heads_with_a_stale_pointer"]} head(s)); '
             f'unregistered-canonical={scorecard["unregistered_canonical_heads"]}; '
             f'currency-drift={scorecard["currency_drift_docs"]}.')
    L.append('')
    L.append('> **Scope disclosures (capstone reconciliation, ED-IN-0056):**')
    L.append('> - **#9 — this measures currency-partition HEALTH, not v40 ADOPTION.** All three '
             'detections (stale pointers, unregistered heads, drift) can read zero while ZERO live '
             'heads carry a legible `v40` marker — a green scorecard here is compatible with no v40 '
             'transition at all. Measuring v40-marker adoption needs the WS3 `head_pointers.yaml` + a '
             '`Generation: v40` stamp, which do not exist yet; until they do, "NS4 meter" means "the '
             'live/historical partition is clean," NOT "v40 is adopted."')
    L.append('> - **#11 — `canon/`, `registers/`, `references/`, and `params/` paths can NEVER be LIVE heads here.** '
             'The reused `ci_generation_consistency.DOC_KEYS` extraction hard-anchors captured paths to '
             'a literal `designs/` prefix, so a current head such as `params/core.md` (named live in '
             '`CURRENT.md`) is unconditionally HISTORICAL to this layer — a structural, corpus-wide '
             'blind spot beyond the four detection-2 DOC_KEYS examples already disclosed. Widening it '
             'is a `ci_generation_consistency.py` change (that rule lives once, §8), not a gen_audit '
             'patch.')
    L.append('')

    def section(title, rows, fmt, empty='(none)'):
        L.append(f'## {title}')
        L.append(empty if not rows else '')
        for r in rows[:30]:
            L.append('- ' + fmt(r))
        if len(rows) > 30:
            L.append(f'- … {len(rows) - 30} more (see `data/g_generation.json`)')
        L.append('')

    section('Currency drift — registered as a canonical head AND recorded as superseded '
             '(reuses `ci_generation_consistency.py`\'s own drift check)',
             drift, lambda d: f'`{d}`')
    L.append('## Stale version-pointers in LIVE heads — a `_vNN.md` reference that is superseded, '
             'moved (successor exists), or genuinely nonexistent (the `combat_v30`-partial-supersession class)')
    L.append('')
    L.append(f'**Severity triage** — a missing target is NOT automatically dead. Split by reason: '
             f'**{stale_by_reason.get("superseded", 0)} superseded** (target exists but is a '
             f'supersession-register entry — repoint at the successor head); '
             f'**{stale_by_reason.get("moved", 0)} moved** (target missing, but the restructure ledger '
             f'`references/restructure_ledger.md` maps it to a NEW path that exists on disk — a trivial '
             f'one-line repoint to the shown `new_home`, NOT an investigation; reused from '
             f'`broken_dependency_checker._load_restructure_map()`); '
             f'**{stale_by_reason.get("nonexistent", 0)} genuinely nonexistent** (no restructure-ledger '
             f'successor — a real dead/drifted citation, a typo, OR a still-open forward-reference to '
             f'explicitly-flagged pending future work; this tool does not distinguish those last three). '
             f'Only the nonexistent bucket needs a human; superseded/moved are mechanical repoints.')
    L.append('' if stale else '(none)')
    for s in stale[:30]:
        tail = f" — now at `{s['new_home']}`" if s.get('new_home') else ''
        L.append(f"- `{s['live_head']}` -> `{s['ref']}` ({s['reason']}){tail}")
    if len(stale) > 30:
        L.append(f'- … {len(stale) - 30} more (see `data/g_generation.json`)')
    L.append('')
    L.append('## Unregistered canonical heads — confidence caveat before acting')
    L.append('')
    L.append('These are flagged because their `## Status:` HEADING leads with CANONICAL/CURRENT, and '
             '`status_of()` (the reused, first-match-wins parser) reads only that heading line. '
             'Several docs in this corpus carry a CANONICAL/CURRENT heading immediately contradicted '
             'by a later bolded `**Status:** PROVISIONAL …` line the parser never sees (real, swept '
             '2026-07-13: ≥11 docs, incl. `designs/territory/march_layer_v30.md`, '
             '`designs/territory/settlement_adjacency_v30.md`, '
             '`designs/provincial/fractional_province_ownership_v30.md`). "Declares a canonical-family '
             'heading" therefore ≠ "is settled CANONICAL" — verify the body\'s `**Status:**` line '
             'before registering any of these. Not fixed in-tool: writing a second, laxer status-line '
             'parser is exactly what §8 (every rule lives once) forbids — the one parser is '
             '`ci_generation_consistency.status_of()`.')
    L.append('')
    unreg_never_mentioned = [u for u in unregistered
                             if not u['mentioned_in_canonical_sources_under_unrecognized_key']]
    unreg_under_bad_key = [u for u in unregistered
                           if u['mentioned_in_canonical_sources_under_unrecognized_key']]
    section('Unregistered canonical heads — genuinely never mentioned in `canonical_sources.yaml` '
             '(the true `conviction_track_v1.md` class, PR #131 P1-B; NOTE: that exact example is '
             'not reproduced here — its Status line is an HTML comment `status_of()` cannot parse, '
             'see the script docstring)',
             unreg_never_mentioned,
             lambda u: f"`{u['path']}` — {u['status'][:70]}")
    section('Unregistered canonical heads — mentioned in `canonical_sources.yaml`, but under a key '
             'name `canonical_docs()`\'s `DOC_KEYS` regex does not match (e.g. `adjacency:`, '
             '`social_contest_design:` — a regex blind spot in the reused function itself, not a '
             'true missing-registration; disclosed separately, not silently merged into the class above)',
             unreg_under_bad_key,
             lambda u: f"`{u['path']}` — {u['status'][:70]}")

    if demoted_live_heads:
        L.append('## Live heads demoted by an authoritative-path tie-break (NOT scanned for stale pointers)')
        L.append('')
        L.append('These pass the strict currency rule (registered, recognized `## Status:`, not '
                 'superseded) but are demoted to HISTORICAL by an AUTHORITATIVE override — a physical '
                 'archival path (`deprecated/archives/`/`deprecated/`/`designs/audit/`/`registers/handoffs/`) or a '
                 'ledger/register path — because a doc filed as a record is a record whatever its '
                 '`## Status:` line says (e.g. a registered-CANONICAL plan under `designs/audit/`). '
                 'Since the ED-IN-0055 reconciliation, `vector_audit.banner_classify()`\'s weak '
                 'CONTENT-keyword no longer demotes a registered head (it was false-hitting the word '
                 '"audit" in live-head prose), so this list is now path/superseded-only. Disclosed, '
                 'not silently dropped: a demotion here can still mask a real stale pointer in that doc.')
        L.append('')
        for d in demoted_live_heads:
            L.append(f"- `{d['path']}` ({d['reason']})")
        L.append('')

    if non_live_canonical:
        L.append('## Lower-confidence — registered canonical docs that do not qualify as LIVE '
                  '(no `## Status:` line, or a non-standard one; not itself a finding, context only)')
        L.append('')
        for d in sorted(non_live_canonical)[:20]:
            L.append(f"- `{d}` ({non_live_canonical[d]})")
        if len(non_live_canonical) > 20:
            L.append(f'- … {len(non_live_canonical) - 20} more (see `data/g_generation.json`)')
        L.append('')

    (out / 'generation_register.md').write_text('\n'.join(L), encoding='utf-8')
    print(f'[done] {out}/generation_register.md')
    return {'scorecard': scorecard, 'partition': partition, 'stale': stale,
            'unregistered': unregistered, 'drift': drift,
            'demoted_live_heads': demoted_live_heads}


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument('--repo-root', default='.', help='repo root (working tree)')
    ap.add_argument('--output-dir', required=True, help='audit output folder')
    a = ap.parse_args()
    root = Path(a.repo_root)
    if not (root / 'references' / 'canonical_sources.yaml').exists():
        sys.exit(f"not a Valoria repo root (no references/canonical_sources.yaml): {root}")
    print(f'[gen_audit] repo root (working tree): {root.resolve()}')
    run(root, a.output_dir)


if __name__ == '__main__':
    main()
