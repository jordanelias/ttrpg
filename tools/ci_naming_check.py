#!/usr/bin/env python3
"""
ci_naming_check.py — authoritative naming-invariant gate.

Rule (from CLAUDE.md): the canonical name is "Solmund"; "Galbados" is the
deprecated name and must never be introduced as a name.

This was previously enforced NOWHERE in CI (the only matcher,
skills/prose-writer/scripts/consistency_check.py, scans 4 prose files over the
GitHub API). This module makes the invariant real, and is deliberately built to
be SAFE rather than self-blocking:

  * DIFF-AWARE — inspects only ADDED lines, so the ~28 files that legitimately
    contain the token today (the registry that defines it, the migration note,
    tests, archives, the matcher itself) are never re-flagged for old content.
  * PATH-SCOPED — those definitional/historical paths are excluded outright.
  * WORD-BOUNDARY — matches the token as a name, not as a substring.

One validator, many callers: the pure core (scan_text / is_excluded) is imported
by tools/hook_naming_guard.py for edit-time feedback; the CLI runs in CI and in
the local pre-commit hook over the changeset.

CLI:
    python tools/ci_naming_check.py            # CI mode (GitHub event context)
    python tools/ci_naming_check.py --staged   # the git index (pre-commit)
    python tools/ci_naming_check.py --local     # HEAD~1..HEAD

SOURCE OF TRUTH: the deprecated name(s) are no longer hardcoded here — they are
read from references/names_index.yaml (via tools/names.py): every entry whose
`enforce` tier is `block` contributes its `legacy` names. That is the single
place a name is changed. This file therefore enforces the index; it does not
define the invariant. (The broader, report-only drift lint over `warn`-tier
entries lives in tools/ci_names_check.py.)
"""
import re
import sys

try:
    import ci_common
    import names
except ImportError:  # allow `python tools/ci_naming_check.py` from repo root
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import ci_common
    import names


def _forbidden_patterns():
    """Word-boundary, case-insensitive matchers for every `block`-tier legacy name
    in names_index.yaml. Read fresh so a change to the index needs no code edit."""
    return [re.compile(r'\b' + re.escape(legacy_name) + r'\b', re.IGNORECASE)
            for (legacy_name, _canon, _key, _tier) in names.all_legacy(enforce='block')]


# Built once at import; the index is the authoritative source (see module docstring).
FORBIDDEN = tuple(_forbidden_patterns())

# Paths that legitimately contain a forbidden token (definition, history, tests,
# the matcher). Matched as substrings against the forward-slashed path.
EXCLUDE = (
    'references/names_index.yaml',          # the source of truth — names the token by design
    'references/alias_registry.yaml',       # deprecated->canonical alias source (names tokens by design)
    'references/name_collision_database.yaml',
    'references/ci_checks_registry.yaml',
    'references/deprecated_terms_registry.yaml',
    'references/proper_noun_registry.yaml',
    # generated glossary bundles carry the deprecated aliases AS DATA (the "from"
    # side of each mapping, generated from alias_registry/names_index) — same
    # rationale as the source registries above; a regen must not trip the gate.
    'tools/observability/lexicon',          # lexicon.json, lexicon_data.js
    'tools/observability/console.html',     # embeds window.VALORIA_LEXICON
    'references/definitions/',              # generated unified definitions store + vocab_source (ED-IN-0078)
                                            # — carry `legacy`/deprecated names AS DATA, same as above
    'references/censured_vocabulary.yaml',  # GENERATED view (ED-IN-0078 fold) — lists censured terms by design
    'references/synonym_registry.yaml',     # GENERATED view (ED-IN-0078 fold) — lists legacy synonyms by design
    'references/name_collision_database.yaml',  # GENERATED view (ED-IN-0078 slice 3) — deprecated terms (incl. Galbados) as data
    'dashboard/data.json',                 # generated: embeds the definitions/lexicon incl. legacy names
    'engine/params/bg/institutions.md',
    'skills/prose-writer/',
    'tests/',
    'deprecated/archives/',
    'deprecated/',
    'designs/audit/',
    'registers/editorial_ledger',
    'CLAUDE.md',                  # documents the naming rule (names the token)
    'tools/ci_naming_check.py',   # this file names the token
    'tools/hook_naming_guard.py',
)


def is_excluded(path):
    """True if `path` is a definitional/historical location exempt from the gate."""
    p = (path or '').replace('\\', '/')
    return any(x in p for x in EXCLUDE)


def scan_text(path, added_text):
    """
    Pure core used by both the CLI and the edit-time hook.

    Returns a list of offending line strings drawn from `added_text`. Returns []
    if the path is excluded or nothing matches. `added_text` should be only the
    newly-added content (a diff's + lines, or an edit's new_string).
    """
    if is_excluded(path):
        return []
    hits = []
    for line in (added_text or '').splitlines():
        if any(pat.search(line) for pat in FORBIDDEN):
            hits.append(line.strip())
    return hits


def main(argv):
    mode = 'ci'
    if '--staged' in argv:
        mode = 'staged'
    elif '--local' in argv:
        mode = 'local'

    if not FORBIDDEN:
        # Fail-safe: an empty matcher means the index could not be read (missing
        # file / no PyYAML / no block-tier entries). Never silently disable the gate.
        print("[NAMING CHECK ERROR] no block-tier names loaded from "
              "references/names_index.yaml — cannot enforce the naming invariant.")
        return 1

    added = ci_common.get_added_lines(mode)
    violations = []
    for path, lines in added.items():
        hits = scan_text(path, '\n'.join(lines))
        for h in hits:
            violations.append((path, h))

    if violations:
        mapping = '; '.join(f'"{canon}" (never "{leg}")'
                            for (leg, canon, _k, _t) in names.all_legacy(enforce='block'))
        print(f"[NAMING VIOLATIONS: {len(violations)}]")
        print(f"  Canonical names enforced from references/names_index.yaml: {mapping}")
        for path, line in violations:
            print(f"  {path}: {line[:120]}")
        print("  If this is a legitimate historical/registry reference, add the path to "
              "EXCLUDE in tools/ci_naming_check.py.")
        return 1
    print("Naming check: no new use of a deprecated name.")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
