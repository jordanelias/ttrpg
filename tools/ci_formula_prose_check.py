#!/usr/bin/env python3
"""
ci_formula_prose_check.py — A18: formula single-source / prose-drift detector (ED-1052 slice).

The deferred half of the quantity armature (proposed_quantity_armature_extension.md §3.2,
RATIFIED spec-only 2026-07-08 as OPT-AV-5). A17 (tools/ci_quantity_vocabulary_check.py) asks
"does every stat NAME resolve to a registry key?"; A18 asks the next question: "for every
registered quantity, does exactly ONE surface DEFINE its formula, with every other carrier
either citing that surface or textually matching it?" A non-matching restatement that carries
no supersession marker is prose drift — the C1-F5/F6 glossary rot, the C3-F1 Knot four-way, the
Mandate dual-form class.

WHY THIS TOOL EXISTS (the named gap): formula_audit.py (the observatory's L1 layer) is
CONTRACT-LEVEL only — its own docstring says it "does NOT parse params/*.md prose tables ...
that class of contradiction needs a real prose/formula table extractor (deliberately deferred)."
CLAUDE.md §5 names the same hole: "no tool parses params/*.md prose — prose formula drift has NO
automated detector." This is that detector.

WHAT IT DOES (§3.2 mechanical predicate, verbatim intent):
  1. Anchors on the 2026-07-08 census (02_census/quantity_census.yaml): each row already carries
     the ONE `defining_surface` and the formula asserted there, plus every other carrier surface.
  2. Re-scans the LIVE prose under engine/params/**/*.md for each quantity's name/aliases,
     extracting any formula RESTATEMENT (markdown table cell or inline `X = expr`). (Scope limit:
     the live scan currently walks ONLY engine/params — design-doc / systems/ / module_contracts
     carriers the census cites are covered by the deterministic census-diff core, not re-scanned.)
  3. Normalizes both strings (unicode ×/÷/−/⌊⌋, markdown emphasis, bracketed citations, min/max
     clamps) — it does NOT evaluate formulas; string-normalized inequality plus a supersession
     whitelist is the whole test (§3.2: "does not need to evaluate formulas").
  4. Emits a report-only violation for every carrier whose normalized formula ≠ the defining
     surface's AND whose line carries no supersession marker, with BOTH file:lines.

SCOPE / TRUST CAVEATS (stated, not silently dropped — the observatory's under-claim ethic):
  * MEASURES, NEVER GATES. Always exits 0. The warn→block flip is OPT-AV-6, gated on OPT-AV-1
    (the attribute roster, still OPEN) and a swept backlog — not this tool's call.
  * ATTRIBUTE-FAMILY ROWS ARE EXCLUDED from violations (roster OPEN, Jordan 2026-07-08 / this
    session): attribute_scalar/attribute_aggregate rows carry "raw attribute 1-7", not a formula,
    and A18 asserts nothing about the roster. They are counted as skipped, never flagged.
  * The live re-scan is BEST-EFFORT extraction (regex heuristics over prose). Findings are
    CANDIDATE drift to triage, not verdicts — precision is favored over recall (a missed
    restatement is a quiet false-negative; a noisy false-positive erodes trust). The census-diff
    core (intra-quantity recorded-formula divergence) is the deterministic, reliable half.
  * The census is a 2026-07-08 evidence snapshot; a cited `defining_surface` may since have MOVED
    (params/ -> engine/params/, designs/scene/combat -> systems/combat/). The report echoes the
    census's file:lines verbatim and does NOT yet verify they still resolve at HEAD — treat a
    defining-surface path as needing a repoint check before acting. (A surface-liveness check is a
    documented next step, not implemented here.)

REUSE, NOT REIMPLEMENTATION (CLAUDE.md §8 — every rule lives once):
  * tools/quantity_registry.py `resolve()` — the ONE resolver for name→registry key (imported,
    same as pointer_audit.py / formula_audit.py).
  * tools/ci_quantity_vocabulary_check.py `_split_bundled()` — the ONE splitter for bundled
    "A / B / C" names (imported when present; degrades gracefully if absent).

USAGE:
    python tools/ci_formula_prose_check.py                       # human report to stdout
    python tools/ci_formula_prose_check.py --output-dir <run>    # + formula_prose_register.md + data/
    python tools/ci_formula_prose_check.py --repo-root . --census <path>
"""
import argparse
import json
import os
import re
import sys

try:
    import yaml
except Exception:  # PyYAML absent — degrade, never crash (names.py discipline)
    yaml = None

_TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
if _TOOLS_DIR not in sys.path:
    sys.path.insert(0, _TOOLS_DIR)

try:
    import quantity_registry
except Exception:
    quantity_registry = None

try:
    from ci_quantity_vocabulary_check import _split_bundled  # A17's ONE splitter
except Exception:
    def _split_bundled(name):
        return [name]

DEFAULT_CENSUS = os.path.join(
    'designs', 'audit', '2026-07-08-attribute-value-coherence-audit',
    '02_census', 'quantity_census.yaml')

# Kinds excluded from violations while the roster (OPT-AV-1) is OPEN.
_ROSTER_GATED_KINDS = {'attribute_scalar', 'attribute_aggregate'}

# Prose surfaces the live re-scan walks (in addition to any design surface the census cites).
_PROSE_ROOTS = [os.path.join('engine', 'params')]

# Deliberately SPECIFIC: bare "was"/"old"/"corrected" over-suppressed real drift phrased
# "Mandate was round(0.5L+0.5PS)" (a genuine stale restatement) — dropped. These markers only
# fire on explicit supersession vocabulary.
_SUPERSESSION_MARKERS = re.compile(
    r'struck|supersede|deprecat|\blegacy\b|no longer|~~|retired|off-path|historical record',
    re.IGNORECASE)


# ─────────────────────────── normalization (the whole test) ───────────────────────────

_UNICODE_OPS = {
    '×': '*', '÷': '/', '−': '-',   # × ÷ −
    '≤': '<=', '≥': '>=', '⌈': 'ceil(', '⌉': ')',
    '⌊': 'floor(', '⌋': ')', '→': '->',
}
_CITATION_RE = re.compile(r'\[[^\]]*\]|\((?:per |see |ED-|PP-|§|LPS|ratif)[^)]*\)', re.IGNORECASE)
_CLAMP_RE = re.compile(r'\b(?:minimum|min)\s*[:=]?\s*(\d+)', re.IGNORECASE)
_CLAMPMAX_RE = re.compile(r'\b(?:maximum|max)\s*[:=]?\s*(\d+)', re.IGNORECASE)


def _demark(s):
    """Strip markdown emphasis and map unicode operators to ASCII, so `**28**` is not read as a
    `*` operator and `×`/`÷`/`−` compare equal to `*`/`/`/`-`."""
    s = re.sub(r'\*\*|`|~~', '', s)
    for u, a in _UNICODE_OPS.items():
        s = s.replace(u, a)
    return s


# A bare state-change delta ("MS +2", "Stability -1") — an EFFECT, not a definition.
_DELTA_RE = re.compile(r'^[A-Za-z .]{0,24}[+\-]\s*\d+\s*$')
# A bare numeric range ("5-35", "0-100") — a bound, not a formula.
_RANGE_RE = re.compile(r'^\(?\d+(?:\.\d+)?\s*[-–]\s*\d+(?:\.\d+)?\)?$')
# Trailing prose-annotation / secondary-formula clauses on a formula field
# (", range 5-47", "; recovery = (End+H)*2", ", depletes 5/exchange"). NOTE: 'threshold' is
# deliberately NOT a cut keyword — it is often the definiendum ("Threshold = Spirit*5").
_ANNOT_CLAUSE_RE = re.compile(
    r'[;,]\s*(?:range|recovery|recover|deplet|cap|starts?|per[- ]?op|per exchange|'
    r'scale|where|note|see)\b.*$', re.IGNORECASE)
# A short prose "Name = " definitional prefix ("Threshold = Spirit*5" -> "Spirit*5"); the LHS must
# be plain words, so it never eats a formula LHS like "(3*End)+...".
_DEF_PREFIX_RE = re.compile(r'^[A-Za-z][A-Za-z ]{0,30}=\s*')
# An "(Author 2026-...)" annotation parenthesis (no arithmetic meaning).
_YEAR_PAREN_RE = re.compile(r'\([^)]*\b(?:19|20)\d\d\b[^)]*\)')


def _core_expr(s):
    """Reduce a prose-wrapped formula field to its arithmetic expression. Correctness invariants
    (each a fixed bug): (1) NEVER truncate at the 2nd operator — the whole expression is kept, so
    `(3*End)+(2*Spirit)` != `(3*End)+(2*Focus)`; (2) a leading `LABEL:` and a short `Name =` prefix
    are stripped; (3) trailing ", range .../; recovery ..." annotation clauses are cut; (4) a bare
    numeric range is NOT a formula. The primary formula leads the field, so cut tail-first."""
    if not s:
        return ''
    s = _demark(s)
    s = re.sub(r'^[^:]{0,22}:\s*', '', s.strip())   # drop a leading "CURRENT:" / "LINEAR:" label
    s = _ANNOT_CLAUSE_RE.sub('', s)                  # cut trailing ", range .../; recovery ..." tails
    s = _DEF_PREFIX_RE.sub('', s)                    # "Threshold = " -> "" (keep the RHS definition)
    s = re.sub(r'^\s*[a-z]+(?: [a-z]+)* +(?=[(\d])', '', s.strip())  # strip a lowercase prose lead-in
    return s.strip()


def _norm(expr):
    """Canonical comparable string for a formula's arithmetic core. NOT an evaluation — just enough
    normalization that two textually-equivalent formulas compare equal and two genuinely-different
    ones do not. Conservative: when in doubt it preserves distinctions (favoring precision)."""
    if not expr:
        return ''
    s = _core_expr(expr)
    s = _YEAR_PAREN_RE.sub('', s)                   # drop "(Author 2026-..)" annotations
    s = _CITATION_RE.sub('', s)                     # drop [..]/(per..)/(ED-..) citations
    s = _CLAMP_RE.sub(r'min:\1', s)                 # "minimum 5" -> min:5
    s = _CLAMPMAX_RE.sub(r'max:\1', s)
    s = s.lower()
    s = re.sub(r'\b(?:relevant\s+)?history(?:\s+points)?\b', 'history', s)
    s = re.sub(r'[\s,]+', '', s)                    # drop whitespace + separators
    s = s.strip('.')
    return '' if _RANGE_RE.match(s) else s


def _looks_like_formula(cell):
    """Cell/RHS is a real formula worth comparing: has a binary/function operator AND is neither a
    bare state-change delta ("MS +2") nor a bare numeric range ("5-35"). A definition combines
    operands; an effect just nudges a track; a range is a bound."""
    if not cell or len(cell) > 200:
        return False
    c = _demark(cell).strip()
    if _DELTA_RE.match(c) or _RANGE_RE.match(c):
        return False
    return bool(re.search(r'[*/]|[0-9)] *[+\-] *[0-9(]|\b(?:floor|ceil|round|min|max)\s*\(', c))


# ─────────────────────────── census loading ───────────────────────────

def load_census(path):
    if yaml is None or not os.path.exists(path):
        return []
    try:
        with open(path, encoding='utf-8') as f:
            data = yaml.safe_load(f) or {}
    except Exception:
        return []
    return data.get('rows', []) or []


def _defining_formula(row):
    """The formula asserted at the row's defining_surface (else the first recorded formula)."""
    ds = (row.get('defining_surface') or '').strip()
    forms = row.get('formulas') or []
    for f in forms:
        if isinstance(f, dict) and (f.get('surface') or '').strip() == ds:
            return f.get('formula', ''), ds
    if forms and isinstance(forms[0], dict):
        return forms[0].get('formula', ''), (forms[0].get('surface') or ds)
    return '', ds


# ─────────────────────────── live prose re-scan ───────────────────────────

def _iter_prose_files(root):
    """Walk the prose roots, EXCLUDING params/history/** (changelog, CLAUDE.md §3) and
    *_superseded.md (explicitly retired) — both carry old formulas by design; scanning them
    manufactures false drift."""
    for base in _PROSE_ROOTS:
        d = os.path.join(root, base)
        for dirpath, dirs, files in os.walk(d):
            if os.path.basename(dirpath) == 'history':
                dirs[:] = []
                continue
            for fn in files:
                if fn.endswith('.md') and not fn.endswith('_superseded.md'):
                    yield os.path.join(dirpath, fn)


def _subject_matches(subject, names, key):
    """True if `subject` (a line's LHS/first-cell) denotes the SAME quantity as this census row —
    by normalized-name equality, or (when the row resolves to a registry key) same key. Stronger
    than substring so 'Thread Tension' does not match a row for 'Thread Pool'."""
    subj = subject.strip().lower()
    for n in names:
        if subj == n.lower():
            return True
    if key and quantity_registry is not None:
        try:
            _m, k = quantity_registry.resolve(subject)
            if k and k == key:
                return True
        except Exception:
            pass
    return False


def _extract_line_formula(line, names, key):
    """If `line` DEFINES a formula for this quantity, return (subject, rhs_text). Two shapes: a
    markdown table row `| Name | formula | ... |`, or an inline `Name = expr`. Requires the subject
    to match the quantity (not just appear in the line) so effect-lines and homonyms are rejected."""
    low = line.lower()
    if not any(n.lower() in low for n in names):
        return None
    if line.count('|') >= 2:
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if cells and _subject_matches(cells[0], names, key):
            for cell in cells[1:]:
                if _looks_like_formula(cell):
                    return cells[0], cell
    m = re.search(r'([A-Z][A-Za-z /]+?)\s*=\s*([^|]+)', line)
    if m and _subject_matches(m.group(1), names, key) and _looks_like_formula(m.group(2)):
        return m.group(1).strip(), m.group(2).strip()
    return None


def scan(root, census, live_scan=False):
    """Return (findings, stats). Two finding types: CENSUS_DRIFT (deterministic — recorded carriers
    disagree) and, when live_scan=True, LIVE_DRIFT (best-effort — current prose restatement differs).
    """
    findings = []
    stats = {'rows': 0, 'formula_rows': 0, 'roster_skipped': 0, 'live_drift': 0,
             'census_drift': 0}

    prose = {}
    if live_scan:
        for fp in _iter_prose_files(root):
            try:
                with open(fp, encoding='utf-8') as f:
                    prose[os.path.relpath(fp, root).replace('\\', '/')] = f.read().splitlines()
            except Exception:
                continue

    for row in census:
        stats['rows'] += 1
        kind = (row.get('kind') or '').strip()
        name = (row.get('canonical_name') or '').strip()
        if not name:
            continue
        def_formula, def_surface = _defining_formula(row)
        if not _looks_like_formula(def_formula):
            continue  # not a formula-bearing quantity (raw attributes, tracks w/o formula, etc.)
        stats['formula_rows'] += 1
        if kind in _ROSTER_GATED_KINDS:
            stats['roster_skipped'] += 1
            continue

        names = [name] + [a for a in (row.get('aliases') or []) if a]
        def_norm = _norm(def_formula)
        key = _resolve_key(name)

        # (a) census-diff core (deterministic): recorded carriers that disagree, no supersession note
        row_status = (row.get('status') or '').strip()
        row_divergences = ' '.join(row.get('divergences') or [])
        for f in (row.get('formulas') or []):
            if not isinstance(f, dict):
                continue
            surf = (f.get('surface') or '').strip()
            if surf == def_surface:
                continue
            other = f.get('formula', '')
            if not _looks_like_formula(other):
                continue
            if _norm(other) != def_norm and not _SUPERSESSION_MARKERS.search(other + ' ' + row_divergences):
                findings.append({
                    'quantity': name, 'kind': kind, 'type': 'CENSUS_DRIFT',
                    'defining_surface': def_surface, 'defining_formula': def_formula.strip(),
                    'drift_surface': surf, 'drift_formula': other.strip(),
                    'census_status': row_status})
                stats['census_drift'] += 1

        # (b) live re-scan (best-effort, opt-in): current prose restatements that differ
        for relpath, lines in prose.items():
            for i, line in enumerate(lines, 1):
                got = _extract_line_formula(line, names, key)
                if not got:
                    continue
                _matched, rhs = got
                if _norm(rhs) == def_norm:
                    continue
                if _SUPERSESSION_MARKERS.search(line):
                    continue
                findings.append({
                    'quantity': name, 'kind': kind, 'type': 'LIVE_DRIFT',
                    'defining_surface': def_surface, 'defining_formula': def_formula.strip(),
                    'drift_surface': f'{relpath}:{i}', 'drift_formula': rhs.strip(),
                    'census_status': row_status})
                stats['live_drift'] += 1

    return findings, stats


# ─────────────────────────── reporting ───────────────────────────

def _resolve_key(name):
    if quantity_registry is None:
        return None
    try:
        _matched, key = quantity_registry.resolve(name)
        return key
    except Exception:
        return None


def build_report(findings, stats):
    L = ['# A18 — Formula Prose-Drift Report (report-only)', '']
    L.append(f"- census rows scanned: **{stats['rows']}**  ·  formula-bearing: **{stats['formula_rows']}**  "
             f"·  roster-gated skipped (attributes, OPT-AV-1 OPEN): **{stats['roster_skipped']}**")
    L.append(f"- CENSUS_DRIFT (recorded carriers disagree): **{stats['census_drift']}**  ·  "
             f"LIVE_DRIFT (current prose restatement differs): **{stats['live_drift']}**")
    L.append('')
    L.append('> MEASURES, NEVER GATES (exit 0). Findings are CANDIDATE drift to triage — attribute-family '
             'rows excluded while the roster is open. See tool docstring for trust caveats.')
    L.append('')
    if not findings:
        L.append('_No formula prose-drift found in scope._')
        return '\n'.join(L) + '\n'
    by_q = {}
    for f in findings:
        by_q.setdefault(f['quantity'], []).append(f)
    for q in sorted(by_q):
        key = _resolve_key(q)
        L.append(f"## {q}" + (f"  -> `{key}`" if key else "  -> _(unresolved key)_"))
        fs = by_q[q]
        def0 = fs[0]
        L.append(f"- **defining surface** `{def0['defining_surface']}` : `{def0['defining_formula']}`")
        if def0.get('census_status'):
            L.append(f"- census status: {def0['census_status']}")
        for f in fs:
            L.append(f"  - [{f['type']}] `{f['drift_surface']}` : `{f['drift_formula']}`")
        L.append('')
    return '\n'.join(L) + '\n'


def run(root, output_dir=None, census_path=None, live_scan=False):
    census = load_census(census_path or os.path.join(root, DEFAULT_CENSUS))
    findings, stats = scan(root, census, live_scan=live_scan)
    report = build_report(findings, stats)
    if output_dir:
        out = os.path.join(output_dir)
        os.makedirs(os.path.join(out, 'data'), exist_ok=True)
        with open(os.path.join(out, 'formula_prose_register.md'), 'w', encoding='utf-8') as f:
            f.write(report)
        with open(os.path.join(out, 'data', 'formula_prose.json'), 'w', encoding='utf-8') as f:
            json.dump({'findings': findings, 'stats': stats}, f, indent=1, sort_keys=True)
        print(f'[done] {out}/formula_prose_register.md')
    else:
        print(report)
    print(f"[A18] {stats['census_drift']} census-drift + {stats['live_drift']} live-drift findings "
          f"across {stats['formula_rows']} formula-bearing quantities "
          f"({stats['roster_skipped']} attribute rows skipped; roster OPEN). Report-only.")
    return findings, stats


def main():
    # Report text echoes census formulas that contain ×/÷/− etc.; a cp1252 console would otherwise
    # crash (or mojibake) on them. Force UTF-8 with lossy fallback for the CLI entry point only
    # (never in run(), so pytest's capture is untouched).
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument('--repo-root', default='.', help='repo root (working tree)')
    ap.add_argument('--output-dir', default=None, help='write register.md + data/ here (else stdout)')
    ap.add_argument('--census', default=None, help='override census path')
    ap.add_argument('--live-scan', action='store_true',
                    help='additionally re-scan live prose for restatements (best-effort, '
                         'precision-limited — see docstring; default off)')
    a = ap.parse_args()
    run(os.path.abspath(a.repo_root), a.output_dir, census_path=a.census, live_scan=a.live_scan)
    return 0  # report-only: never non-zero (flip is OPT-AV-6, roster-gated)


if __name__ == '__main__':
    sys.exit(main())
