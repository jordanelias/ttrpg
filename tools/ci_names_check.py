#!/usr/bin/env python3
"""
ci_names_check.py — report-only naming-drift lint over the WHOLE names index.

Where ci_naming_check.py is the hard gate for `enforce: block` entries (the
proper-noun invariant), THIS lint covers every `enforce: warn` entry in
references/names_index.yaml: it flags any newly-added use of a `legacy` term and
names the `canonical` replacement to use instead.

It is REPORT-ONLY for now — callers run it non-blocking (CI: continue-on-error;
local: blocking=False in valoria_local.py) while the existing tree is triaged.
Flip an entry from `warn` to `block` in the index (which moves it under
ci_naming_check) once its corpus residuals are cleared. The tool itself returns
a truthful exit code (1 on findings); the report-only policy lives in the caller.

ONE SOURCE, MANY READERS: legacy->canonical pairs come from tools/names.py; the
diff machinery and path exclusions are reused from ci_common / ci_naming_check —
nothing is re-implemented here.

CLI (same modes as the other gates):
    python tools/ci_names_check.py            # CI mode
    python tools/ci_names_check.py --staged   # the git index (pre-commit)
    python tools/ci_names_check.py --local    # HEAD~1..HEAD
"""
import re
import sys

try:
    import ci_common
    import names
    import ci_naming_check
except ImportError:  # allow running from repo root
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import ci_common
    import names
    import ci_naming_check


def _warn_matchers():
    """List of (compiled_pattern, legacy_name, canonical, key) for `warn`-tier legacy names."""
    out = []
    for legacy_name, canon, key, _tier in names.all_legacy(enforce='warn'):
        pat = re.compile(r'\b' + re.escape(legacy_name) + r'\b', re.IGNORECASE)
        out.append((pat, legacy_name, canon, key))
    return out


def scan_text(path, added_text, matchers=None):
    """
    Return [(legacy, canonical, line), ...] for `warn`-tier legacy names found in
    `added_text`. Honors the same path exclusions as the hard gate. Pure: callers
    pass only newly-added content.
    """
    if ci_naming_check.is_excluded(path):
        return []
    matchers = _warn_matchers() if matchers is None else matchers
    hits = []
    for line in (added_text or '').splitlines():
        for pat, legacy_name, canon, _key in matchers:
            if pat.search(line):
                hits.append((legacy_name, canon, line.strip()))
    return hits


def main(argv):
    mode = 'ci'
    if '--staged' in argv:
        mode = 'staged'
    elif '--local' in argv:
        mode = 'local'

    matchers = _warn_matchers()
    if not matchers:
        print("Names drift lint: no warn-tier legacy names in references/names_index.yaml.")
        return 0

    added = ci_common.get_added_lines(mode)
    violations = []
    for path, lines in added.items():
        for legacy_name, canon, line in scan_text(path, '\n'.join(lines), matchers):
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
