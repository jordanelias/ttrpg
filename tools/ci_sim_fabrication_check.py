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
  (a) covered by a co-located (or repo-root) sim_verification_ledger.json entry —
      matched by (sim_variable, value) when the literal is assigned to a variable, OR
  (b) annotated with a `# [canonical: path §section]` comment on the same line
      or the line immediately above.

Heuristics (ported from valoria_hooks, then hardened per ED-1053 / review §4.1–4.2):
  - exempt numbers {'0','1','2','10','100'} and their '.0' floats (structural);
  - FULL numeric literals are captured, INCLUDING decimals — `1.7` is one token, not
    `1` + `7`, so a fabricated float can no longer slip through on an integer-token
    collision with the ledger (§4.2);
  - an ASSIGNED constant (`VAR = n` / `kwarg=n`) is cited only when (VAR, n) is in the
    ledger — not merely when `n` appears under any variable, so `FABRICATED = 25` no
    longer passes because some unrelated entry is also 25 (§4.1). Unassigned literals
    (expressions, list/positional args) keep the legacy loose value-match to avoid a
    false-positive blast on the large body of unbindable numbers;
  - value comparison is numeric-aware: 0.60==0.6, 25==25.0;
  - numbers inside range()/len()/enumerate()/slice() idioms are skipped;
  - string literals (incl. multi-line docstrings) and inline comments are stripped;
  - a constant is "cited" if the same or previous line matches `# [canonical: ...]`;
  - at most 10 items reported per file.

NOTE: tightening (a) surfaces pre-existing latent debt — constants that were passing by
coincidental value-collision now require a real (variable, value) ledger entry or an
inline `# [canonical: ...]`. The gate is changeset-scoped, so this only bites a sim file
the next time it is edited; the escape hatch is an inline citation or a per-file ledger.

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

# ── Ported heuristics (preserved from valoria_hooks; hardened per ED-1053) ─────
# Match a FULL numeric literal including any decimal part. The original pattern was
# `(\d+)` — digit-runs only — so `1.7` tokenized to `1` and `7`, and a fabricated
# float passed whenever one of its integer tokens collided with any ledger value
# (ED-1053 / review §4.2). Capturing `\d+(?:\.\d+)?` as one token closes that hole:
# the ledger comparison is now against the exact literal (`1.7`, `0.45`), not its
# fragments. The `(?<![\w.])`/`(?![\w.])` guards keep us off identifiers (`v18`) and
# dotted runs.
_MECHANICAL_NUMERIC_PATTERN = re.compile(r'(?<![\w.])(\d+(?:\.\d+)?)(?![\w.])')
_CANONICAL_COMMENT_PATTERN = re.compile(r'#\s*\[canonical:\s*[^\]]+\]')
# Associates a numeric literal with its assignment target / keyword-arg name, so a
# constant can be matched against the ledger by (variable, value) rather than value
# alone — `CFG = dict(adef=1.7)` associates `1.7` with `adef`.
_ASSIGN_PATTERN = re.compile(r'(\w+)\s*=\s*(\d+(?:\.\d+)?)(?![\w.])')

# Values exempt from citation requirement — these are structural, not mechanical.
# The `.0` forms are included so trivial floats (`1.0`, `2.0`) don't become false
# positives now that decimals are captured as whole tokens. `0.5` is the dominant
# structural fraction in this corpus — `** 0.5` (Euclidean distance), `* 0.5`
# (midpoint/mean/halving) — so it's exempt alongside the structural integers; a
# genuinely mechanical 0.5 threshold should carry a ledger entry or inline citation.
_EXEMPT_NUMBERS = {'0', '1', '2', '10', '100',
                   '0.0', '1.0', '2.0', '10.0', '100.0', '0.5'}  # indices, bounds, percentages, halving

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
    # tools/ are validators/generators (this checker included), not sim reference
    # code — gating them would flag a validator's own thresholds and docstring prose
    # (e.g. this file's "ED-1053" / "0.60" examples). Exclude them.
    if norm.startswith('deprecated/') or norm.startswith('deprecated/archives/') or norm.startswith('tools/'):
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


def _extract_uncited_with_vars(content: str):
    """
    Pure core (no I/O). Like extract_uncited_constants but also returns the variable
    each numeric literal is associated with (the assignment target / keyword-arg name
    on the same line, or None when the literal isn't in an `ident = value` form).
    Returns a list of (line_number, line_text, number, variable_or_None) tuples.

    Used by genuine_violations_by_pair to match constants against the ledger by
    (variable, value) — closing the global value-collision hole (ED-1053 / review §4.1)
    where a fabricated constant passed merely because its value appeared somewhere in
    the ledger under an unrelated variable.
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
        # Map each assigned numeric literal to its target/kwarg identifier.
        assign_vars = {}
        for m in _ASSIGN_PATTERN.finditer(code_only):
            assign_vars.setdefault(m.group(2), m.group(1))
        numbers = _MECHANICAL_NUMERIC_PATTERN.findall(code_only)
        for n in numbers:
            if n in _EXEMPT_NUMBERS:
                continue
            # Skip if part of a standard Python idiom (range, len, slice).
            # Heuristic: if the number is inside range(), len(), [:N], etc.,
            # it's probably structural.
            if re.search(rf'(range|len|enumerate|slice)\s*\([^)]*\b{re.escape(n)}\b', code_only):
                continue
            uncited.append((i, orig[i - 1].rstrip(), n, assign_vars.get(n)))
    return uncited


def extract_uncited_constants(content: str):
    """
    Pure core (no I/O). Scan Python content for numeric literals on lines without
    canonical citations. Returns a list of (line_number, line_text, number) tuples
    for uncited values.

    Heuristic — skips exempt values (0, 1, 2, 10, 100, and their `.0` floats),
    comment-only lines, and numbers inside range()/len()/enumerate()/slice() idioms.
    String literals (both single-line and multi-line triple-quoted docstrings) and
    inline comments are stripped before scanning. A line is "cited" if it, or the line
    immediately above it, matches `# [canonical: ...]`.

    Thin wrapper over _extract_uncited_with_vars (drops the variable) — preserved as the
    value-only core that the loose genuine_violations() and the unit tests rely on.
    """
    return [(ln, txt, n) for ln, txt, n, _var in _extract_uncited_with_vars(content)]


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


def _num_match(token: str, candidates: set) -> bool:
    """True if `token` equals any value in `candidates` — by exact string OR by numeric
    value (so `0.60`==`0.6` and `25`==`25.0`). Robust to the int/float/trailing-zero
    representation drift between the code literal and the ledger's JSON value."""
    if token in candidates:
        return True
    try:
        t = float(token)
    except (TypeError, ValueError):
        return False
    for c in candidates:
        try:
            if float(c) == t:
                return True
        except (TypeError, ValueError):
            continue
    return False


def genuine_violations_by_pair(content: str, ledger_pairs, ledger_values=None):
    """
    Pure core (no I/O). Production matcher used by main(). HYBRID of strict (variable,
    value) matching and the legacy loose value-match, tuned to close the value-collision
    hole (ED-1053 / review §4.1) WITHOUT the false-positive blast of strict-everywhere:

      - A constant with an assignment target (`VAR = n` / `kwarg=n`) is cited ONLY when
        (VAR, n) is registered in the ledger. So `FABRICATED_CRIT = 25` no longer passes
        merely because some unrelated `BATTLEFIELD_SIZE` is also 25.
      - A constant with NO assignment target (appears in an expression, list, or
        positional call — there is no variable to bind it to) keeps the legacy loose
        behaviour: cited if its value appears anywhere in the ledger. This preserves the
        prior pass-rate for the large body of unbindable literals instead of flagging
        them all at once.

    Either form is also cited by an inline `# [canonical: ...]` (honoured in extraction)
    or by being an exempt structural value. `ledger_pairs` maps variable -> set of
    stringified values; `ledger_values` is the flat value set for the no-variable case.
    Value comparison is numeric-aware (see _num_match): 0.60==0.6, 25==25.0.
    """
    ledger_pairs = ledger_pairs or {}
    ledger_values = ledger_values or set()
    out = []
    for ln, txt, n, var in _extract_uncited_with_vars(content):
        if var is not None:
            if _num_match(n, ledger_pairs.get(var, set())):
                continue
        else:
            if _num_match(n, ledger_values):
                continue
        out.append((ln, txt, n))
    return out


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


def load_ledger_pairs(sim_path: str) -> dict:
    """
    Repo-relative ledger resolution returning a {variable: set(stringified values)} map
    (the strict counterpart to load_ledger_values). Same candidate search — co-located
    ledger first, repo-root fallback — but keyed by the entry's `sim_variable` so the
    checker can match constants by (variable, value). Entries lacking `sim_variable`
    contribute nothing to the strict map (they can only be honoured by inline citation).
    """
    import json
    from collections import defaultdict

    norm = sim_path.replace('\\', '/')
    candidates = []
    co_dir = norm.rsplit('/', 1)[0] if '/' in norm else ''
    co_located = os.path.join(co_dir, _LEDGER_FILENAME) if co_dir else _LEDGER_FILENAME
    candidates.append(co_located)
    if _LEDGER_FILENAME not in candidates:
        candidates.append(_LEDGER_FILENAME)

    pairs = defaultdict(set)
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
            var = e.get('sim_variable')
            v = e.get('value')
            if var is not None and v is not None:
                pairs[str(var)].add(str(v))
    return dict(pairs)


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
        ledger_pairs = load_ledger_pairs(path)
        ledger_values = load_ledger_values(path)
        genuine = genuine_violations_by_pair(content, ledger_pairs, ledger_values)
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
