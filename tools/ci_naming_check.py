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
define the invariant.

BOTH TIERS LIVE HERE (2026-08-23, S6/D2 — `tools/ci_names_check.py` merged in and
retired). The rule is ONE rule — "an added line must not introduce a deprecated
name" — parameterised by the index's `enforce` tier, and it was implemented twice:
same diff machinery, same path exclusions (the warn tool imported THIS file's
`is_excluded`), same scan loop, different output strings. CLAUDE.md §8's "every
rule lives once", violated by two files that differed only in a keyword argument.

    python tools/ci_naming_check.py            # block tier — BLOCKING
    python tools/ci_naming_check.py --warn     # warn tier  — report-only by CALLER policy

⚠ THE TWO TIERS DIFFER IN ONE PLACE ON PURPOSE, and it is not tidiable away: an
EMPTY block tier is a broken index and returns 1 (a gate that cannot match
anything must never report clean), while an empty warn tier is a legitimate end
state — every entry triaged and promoted to `block` — and returns 0. Same rule,
different meaning of "nothing to match".

Exit codes are truthful in both tiers (1 on findings). The report-only POLICY for
`--warn` lives in the callers, exactly as it did before the merge: CI runs it in
`validators-report` (continue-on-error), `valoria_local.py` with blocking=False.
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


def matchers_for(tier):
    """(pattern, legacy, canonical, key) for every legacy name at `tier` in names_index.yaml.

    Read fresh from the index so a name change needs no code edit. The canonical name travels
    with the pattern because the warn tier's whole output is "use this instead" — the block tier
    prints the mapping too, from the same source.
    """
    return [(re.compile(r'\b' + re.escape(legacy_name) + r'\b', re.IGNORECASE),
             legacy_name, canon, key)
            for (legacy_name, canon, key, _tier) in names.all_legacy(enforce=tier)]


def _forbidden_patterns():
    """Back-compat: the block tier's bare patterns. Derived, never a second list."""
    return [pat for (pat, _l, _c, _k) in matchers_for('block')]


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
    'dashboard/data.json',                 # generated: embeds the definitions/lexicon incl. legacy names
    # 'engine/params/bg/institutions.md' RETIRED 2026-08-12 (plan step G2,
    # ED-IN-0159 §1.6) — engine/params/ was EVACUATED 2026-08-05 (ED-IN-0145), so
    # the exclusion excluded nothing. The comment below PREDICTED this exact
    # retirement ("when engine/params/ evacuates, this entry and the one above go
    # with it") and was then not acted on for a week; that is the §1.6 pattern in
    # miniature, and it is why the recurrence guard matters more than the cut.
    #
    # GENERATED verbatim capture of the evacuated engine/params/**/*.md (ED-IN-0139).
    # It inherits whatever the sources contained, including the line excluded above.
    # NOTE the capture's exclusion CANNOT be retired with its source: the capture is
    # still in the tree, still contains the legacy token, and is now the ONLY place
    # that content exists — so it must stay excluded or the naming gate reds on a
    # byte-faithful archive nobody can edit.
    'engine/engine_params/params_tables.yaml',
    'skills/prose-writer/',
    'tests/',
    'deprecated/archives/',
    'deprecated/',
    'audit/',                     # the audit-report corpus — historical records that quote the
                                  # names they critique, plus GENERATED run data (a vector-audit
                                  # run's data/tokens.json derives its token universe from
                                  # names_index INCLUDING each entry's `legacy:` field, so it
                                  # carries deprecated names AS DATA — same rationale as the
                                  # generated bundles above). Was 'designs/audit/' until
                                  # 2026-07-26 (ED-MB-0043): designs/ was retired 2026-07-19
                                  # (ED-IN-0071 P4/P5) and the corpus moved to audit/, so that
                                  # entry had matched nothing since — the same dead-path class
                                  # this exclusion now covers.
    'registers/editorial_ledger',
    # The frozen ED archives, relocated out of `deprecated/` 2026-08-23 (S6/6b,
    # evacuation_plan's R-REL-EDUNIVERSE). FOUR of the 26 fragments quote the deprecated
    # name as historical DATA, and they were covered here only by the blanket
    # 'deprecated/' entry two lines up — so the move would have taken them out of the
    # gate's exemption and reddened it the first time anything touched one of them.
    # A rename shows no added lines while git's rename detection holds, which is exactly
    # the kind of protection that vanishes silently; this entry follows the data instead.
    'registers/archive/',
    'CLAUDE.md',                  # documents the naming rule (names the token)
    'tools/ci_naming_check.py',   # this file names the token
    'tools/hook_naming_guard.py',
)


def is_excluded(path):
    """True if `path` is a definitional/historical location exempt from the gate."""
    p = (path or '').replace('\\', '/')
    return any(x in p for x in EXCLUDE)


def _scan(path, added_text, matchers):
    """THE rule, stated once: which added lines introduce a deprecated name.

    Returns [(legacy, canonical, line), ...]. Both tiers and the edit-time hook run through
    this; the two public wrappers below differ only in which matchers they pass and what shape
    their caller already expects.
    """
    if is_excluded(path):
        return []
    hits = []
    for line in (added_text or '').splitlines():
        for pat, legacy_name, canon, _key in matchers:
            if pat.search(line):
                hits.append((legacy_name, canon, line.strip()))
    return hits


def scan_text(path, added_text):
    """BLOCK tier. Returns a list of offending line STRINGS.

    The shape is unchanged and deliberately so: `tools/hook_naming_guard.py` slices each hit as
    a string for its edit-time message. Widening this return value to satisfy the merge would
    have broken the one caller the merge is not about.
    """
    return [line for (_legacy, _canon, line) in _scan(path, added_text, matchers_for('block'))]


def scan_text_warn(path, added_text, matchers=None):
    """WARN tier. Returns [(legacy, canonical, line), ...] — the drift lint's shape, unchanged
    from `ci_names_check.scan_text`, including the injectable `matchers` its tests rely on."""
    return _scan(path, added_text, matchers_for('warn') if matchers is None else matchers)


def main(argv):
    mode = 'ci'
    if '--staged' in argv:
        mode = 'staged'
    elif '--local' in argv:
        mode = 'local'

    if '--warn' in argv:
        return _main_warn(mode)

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


def _main_warn(mode):
    """The warn-tier drift lint, merged in from tools/ci_names_check.py (S6/D2, 2026-08-23).

    An empty matcher set is CLEAN here, unlike the block tier — see the module docstring.
    """
    matchers = matchers_for('warn')
    if not matchers:
        print("Names drift lint: no warn-tier legacy names in references/names_index.yaml.")
        return 0

    added = ci_common.get_added_lines(mode)
    violations = []
    for path, lines in added.items():
        for legacy_name, canon, line in scan_text_warn(path, '\n'.join(lines), matchers):
            violations.append((path, legacy_name, canon, line))

    if violations:
        print(f"[NAMING DRIFT (report-only): {len(violations)}]")
        print("  Deprecated names found in added lines — use the canonical from "
              "references/names_index.yaml (or run tools/valoria_rename.py):")
        for path, legacy_name, canon, line in violations:
            print(f'  {path}: "{legacy_name}" -> "{canon}"  |  {line[:100]}')
        return 1
    print("Names drift lint: no new use of a deprecated name.")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
