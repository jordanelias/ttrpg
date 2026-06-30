#!/usr/bin/env python3
"""
ci_sim_fabrication_check.py
Ports valoria_hooks.sim_fabrication_check into a standalone CI validator.

ERROR/blocking anti-fabrication guard. Catches uncited mechanical constants in
sim .py files — the owner's documented #1 simulation failure mode (wholly
fabricated / uncited mechanical values committed into sim code). Reads the
working tree (via ci_common) rather than an in-memory additions list, and
resolves the verification ledger REPO-RELATIVE rather than from /home/claude.

A numeric literal in a sim file must be either:
  (a) covered by a co-located (or repo-root) sim_verification_ledger.json entry, OR
  (b) annotated with a `# [canonical: path §section]` comment on the same line
      or the line immediately above.

Heuristics are preserved EXACTLY from the original:
  - exempt numbers {'0','1','2','10','100'} (structural: indices, bounds, percents);
  - numbers inside range()/len()/enumerate()/slice() idioms are skipped;
  - string literals and inline comments are stripped before scanning;
  - a constant is "cited" if the same or previous line matches `# [canonical: ...]`;
  - at most 10 items reported per file.

Original lived at valoria_hooks.sim_fabrication_check(additions); it took an
in-memory `additions` list and loaded a single ledger at
/home/claude/sim_verification_ledger.json. This version takes the changeset from
git, reads each file from the working tree, and resolves the ledger repo-relative.

No GitHub API, no PAT, no /home/claude, no network.
"""
import os
import re
import sys

try:
    import ci_common
except ImportError:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import ci_common

# ── Ported heuristics (preserved exactly from valoria_hooks) ──────────────────
_MECHANICAL_NUMERIC_PATTERN = re.compile(r'(?<![a-zA-Z_])(\d+)(?![a-zA-Z_])')
_CANONICAL_COMMENT_PATTERN = re.compile(r'#\s*\[canonical:\s*[^\]]+\]')

# Values exempt from citation requirement — these are structural, not mechanical.
_EXEMPT_NUMBERS = {'0', '1', '2', '10', '100'}  # indices, loop bounds, percentages

# Ledger filename to look for, co-located with the sim file (and at the repo root).
_LEDGER_FILENAME = 'sim_verification_ledger.json'


# ── Helpers ───────────────────────────────────────────────────────────────────
def is_sim_file(path: str) -> bool:
    """A file is a sim file if it's under tests/sim/ or its name contains 'sim'.

    Ported from valoria_hooks._is_sim_file. Must end with .py; path is checked
    with forward-slash semantics, and the basename is matched case-insensitively
    for 'sim' / 'simulation'.
    """
    if not path.endswith('.py'):
        return False
    norm = path.replace('\\', '/')
    # Archival trees are non-authoritative — never gated (cf. ci_naming_check).
    if norm.startswith('deprecated/') or norm.startswith('archives/'):
        return False
    if norm.startswith('tests/sim/'):
        return True
    basename = norm.rsplit('/', 1)[-1].lower()
    if 'sim' in basename or 'simulation' in basename:
        return True
    return False


# Build the pattern without a literal triple-quote in source, so this checker masks its OWN
# docstrings correctly (a literal """ inside a string would mis-pair the matcher on this file).
_TQ_D = '"' * 3
_TQ_S = "'" * 3
_TRIPLE_QUOTED = re.compile(r'(?s)(' + _TQ_D + '|' + _TQ_S + r')(.*?)\1')


def _mask_triple_quoted(content: str) -> str:
    """Blank the BODY of every triple-quoted string (docstrings, multi-line literals) while
    preserving line count + column structure, so reported line numbers stay accurate. Numbers in
    documentation prose ("§A.12", "ED-899", "the 1-7 scale") are never live mechanical constants;
    the original line scanner only stripped SINGLE-line string literals, so multi-line docstrings
    leaked their prose numerals as false positives — which blocked any edit to docstring-heavy sim
    files (orchestration.py alone carried dozens of such false positives at HEAD). Masking removes that
    class of false positive without weakening real detection (a numeric literal in code is untouched)."""
    def _blank(m):
        body = m.group(2)
        return m.group(1) + ''.join('\n' if c == '\n' else ' ' for c in body) + m.group(1)
    return _TRIPLE_QUOTED.sub(_blank, content)


def extract_uncited_constants(content: str):
    """
    Pure core (no I/O). Scan Python content for numeric literals on lines without
    canonical citations. Returns a list of (line_number, line_text, number) tuples
    for uncited values.

    Heuristic — skips exempt values (0, 1, 2, 10, 100), comment-only lines, and
    numbers inside range()/len()/enumerate()/slice() idioms. String literals (both
    single-line and multi-line triple-quoted docstrings) and inline comments are
    stripped before scanning. A line is "cited" if it, or the line immediately above
    it, matches `# [canonical: ...]`.

    Ported from valoria_hooks._extract_uncited_constants; extended to mask multi-line
    triple-quoted strings (the original only stripped single-line string literals).
    """
    uncited = []
    masked = _mask_triple_quoted(content).split('\n')   # docstring bodies blanked; line numbers preserved
    orig = content.split('\n')                           # report the ORIGINAL text, not the masked text
    for i, line in enumerate(masked, 1):
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        # Does this line or the line before have a canonical comment?
        prev = masked[i - 2] if i >= 2 else ''
        if _CANONICAL_COMMENT_PATTERN.search(line) or _CANONICAL_COMMENT_PATTERN.search(prev):
            continue
        # Strip string literals to avoid flagging numbers in strings.
        # Rough heuristic — doesn't handle escape sequences perfectly.
        code_only = re.sub(r"'[^']*'", "''", line)
        code_only = re.sub(r'"[^"]*"', '""', code_only)
        # Strip inline comments.
        if '#' in code_only:
            code_only = code_only.split('#', 1)[0]
        numbers = _MECHANICAL_NUMERIC_PATTERN.findall(code_only)
        for n in numbers:
            if n in _EXEMPT_NUMBERS:
                continue
            # Skip if part of a standard Python idiom (range, len, slice).
            # Heuristic: if the number is inside range(), len(), [:N], etc.,
            # it's probably structural.
            if re.search(rf'(range|len|enumerate|slice)\s*\([^)]*\b{n}\b', code_only):
                continue
            uncited.append((i, orig[i - 1].rstrip(), n))
    return uncited


def genuine_violations(content: str, ledger_values: set):
    """
    Pure core (no I/O). Run extract_uncited_constants over `content`, then drop any
    constant whose number string is present in `ledger_values` (those count as
    cited). Returns the surviving (line_number, line_text, number) tuples.

    This is loose by design — a matching number with a different meaning would
    pass — but the primary failure mode is wholly fabricated values, which this
    catches. Mirrors the original filter in sim_fabrication_check.
    """
    ledger_values = ledger_values or set()
    uncited = extract_uncited_constants(content)
    return [(ln, txt, n) for ln, txt, n in uncited if n not in ledger_values]


def load_ledger_values(sim_path: str) -> set:
    """
    Repo-relative ledger resolution. For a sim file at <dir>/<file>.py, look for a
    co-located ledger at <dir>/sim_verification_ledger.json, and ALSO check the
    repo-root sim_verification_ledger.json as a fallback. Collect the set of ledger
    'value' fields (stringified) from any ledger found. If none is found, return an
    empty set (only inline `# [canonical: ...]` citations will count).

    Ledger schema (preserved from the original): a JSON object with an 'entries'
    list, each entry an object with an optional 'value' field.
    """
    import json

    norm = sim_path.replace('\\', '/')
    candidates = []
    # Co-located ledger.
    co_dir = norm.rsplit('/', 1)[0] if '/' in norm else ''
    co_located = os.path.join(co_dir, _LEDGER_FILENAME) if co_dir else _LEDGER_FILENAME
    candidates.append(co_located)
    # Repo-root fallback.
    if _LEDGER_FILENAME not in candidates:
        candidates.append(_LEDGER_FILENAME)

    values = set()
    seen = set()
    for cand in candidates:
        cand_norm = cand.replace('\\', '/')
        if cand_norm in seen:
            continue
        seen.add(cand_norm)
        raw = ci_common.read_text(cand)
        if raw is None:
            continue
        try:
            ledger = json.loads(raw)
        except Exception:
            continue
        if not isinstance(ledger, dict):
            continue
        for e in ledger.get('entries', []) or []:
            if not isinstance(e, dict):
                continue
            v = e.get('value')
            if v is not None:
                values.add(str(v))
    return values


def main(argv) -> int:
    """
    Compute the changeset via ci_common, filter to sim .py files present on disk,
    load each file's repo-relative ledger values, compute genuine_violations, and
    print a per-file report. Exit 1 if any uncited constants are found (ERROR /
    blocking, matching the original), else print OK and exit 0.
    """
    mode = 'ci'
    if '--staged' in argv:
        mode = 'staged'
    elif '--local' in argv:
        mode = 'local'

    changed = ci_common.get_changed_files(mode)
    sim_paths = sorted(p for p in changed if is_sim_file(p))
    if not sim_paths:
        print("[SIM-FABRICATION OK] no changed sim .py files — nothing to check.")
        return 0

    problems = []          # list of (path, genuine_violations)
    scanned = 0
    for path in sim_paths:
        content = ci_common.read_text(path)
        if content is None:
            # Deleted or unreadable in the working tree — skip (nothing to scan).
            continue
        scanned += 1
        ledger_values = load_ledger_values(path)
        genuine = genuine_violations(content, ledger_values)
        if genuine:
            problems.append((path, genuine))

    if not problems:
        print(f"[SIM-FABRICATION OK] {scanned} sim file(s) scanned, all constants cited.")
        return 0

    print("[SIM-FABRICATION] uncited mechanical constants found:")
    for path, items in problems:
        print(f"[SIM-FABRICATION]   {path}:")
        for ln, txt, n in items[:10]:  # cap at 10 per file to avoid spam
            print(f"[SIM-FABRICATION]     line {ln}: value {n} — {txt[:80]}")
        if len(items) > 10:
            print(f"[SIM-FABRICATION]     ... and {len(items) - 10} more")
    print("[SIM-FABRICATION] Every mechanical constant requires either:")
    print(f"[SIM-FABRICATION]   (a) an entry in a {_LEDGER_FILENAME} "
          "(co-located with the sim file or at the repo root), OR")
    print("[SIM-FABRICATION]   (b) a `# [canonical: path §section]` comment on the "
          "same or prior line.")
    print("[SIM-FABRICATION] Fabricated constants are the primary simulation "
          "failure mode; this gate is intentionally noisy.")
    return 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
