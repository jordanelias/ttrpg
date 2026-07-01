"""
broken_dependency_checker.py — Valoria repository integrity scanner.
Scans the propagation map and canonical_sources for references to files
that do not exist in the repository.

ED-1053: ported off the GitHub API to the LOCAL WORKING TREE. It used to fetch the
recursive tree + file contents from remote `main` and required GITHUB_PAT, so it
validated remote main rather than the diff under test (and broke without a PAT). It
now reads the checkout directly — no PAT, no network — so a PR that adds or fixes a
reference is validated against its own changes. This is the working-tree integrity
model mandated by CLAUDE.md.

Usage:
    python3 tools/broken_dependency_checker.py
Output: prints broken dependencies; exits 1 if any found.
"""

import os, sys, re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

# Trees that are not part of the live corpus for ref-resolution purposes.
_IGNORE_DIRS = {'.git'}


def get_all_repo_files():
    """Return the set of all repo-relative file paths in the working tree."""
    files = set()
    for root, dirs, names in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in _IGNORE_DIRS]
        for n in names:
            rel = os.path.relpath(os.path.join(root, n), REPO_ROOT).replace(os.sep, '/')
            files.add(rel)
    return files


def read_file(path):
    """Read a file from the working tree (repo-relative path). None if missing/unreadable."""
    try:
        with open(os.path.join(REPO_ROOT, path), encoding='utf-8') as f:
            return f.read()
    except Exception:
        return None

def extract_file_refs(content, source_file=""):
    """Extract all file path references from a markdown/yaml document."""
    refs = set()
    patterns = [
        r'`((?:designs|compilation|references|canon|tests|skills|tools)/[^`\s]+\.(?:md|yaml|py|json))`',
        r'"((?:designs|compilation|references|canon|tests|skills|tools)/[^"\s]+\.(?:md|yaml|py|json))"',
        r"'((?:designs|compilation|references|canon|tests|skills|tools)/[^'\s]+\.(?:md|yaml|py|json))'",
        r'(?:canonical|source_file|path|affects):\s*((?:designs|compilation|references|canon|tests|skills|tools)/\S+\.(?:md|yaml|py|json))',
    ]
    for pat in patterns:
        for m in re.finditer(pat, content):
            path = m.group(1).strip()
            if path and not path.startswith("#"):
                refs.add(path)
    # Filter out glob patterns (*, ?) — these are not real file references
    refs = {r for r in refs if '*' not in r and '?' not in r}
    return refs

def check_propagation_map(all_files):
    """Check propagation_map.md for broken references."""
    content = read_file("references/propagation_map.md")
    if not content:
        return [], ["references/propagation_map.md not found"]
    refs = extract_file_refs(content, "propagation_map.md")
    broken = [r for r in refs if r not in all_files]
    return broken, []

def check_canonical_sources(all_files):
    """Check canonical_sources.yaml for broken references."""
    content = read_file("references/canonical_sources.yaml")
    if not content:
        return [], ["references/canonical_sources.yaml not found"]
    refs = extract_file_refs(content, "canonical_sources.yaml")
    broken = [r for r in refs if r not in all_files]
    return broken, []

# check_skill_registry retired: the orchestrator's skill_registry.md was an
# orchestrator-era coordination artifact, moved to deprecated/ when the
# orchestrator was retired (2026-06-24). Claude Code now discovers skills by
# name + description (see CLAUDE.md), so there is no live registry to validate.

def check_editorial_ledger(all_files):
    """Check editorial_ledger.yaml propagation_targets for broken paths."""
    content = read_file("canon/editorial_ledger.yaml")
    if not content:
        return [], []
    refs = extract_file_refs(content, "editorial_ledger.yaml")
    broken = [r for r in refs if r not in all_files]
    return broken, []

def main():
    print("Scanning working tree...")
    all_files = get_all_repo_files()
    print(f"Found {len(all_files)} files in working tree")

    broken = {}
    errors = []

    checks = [
        ("propagation_map.md",    check_propagation_map),
        ("canonical_sources.yaml", check_canonical_sources),
        ("editorial_ledger.yaml", check_editorial_ledger),
    ]

    for name, fn in checks:
        b, e = fn(all_files)
        if b:
            broken[name] = b
        errors.extend(e)

    if errors:
        print("\nERRORS (files not accessible):")
        for e in errors:
            print(f"  [ERROR] {e}")

    if broken:
        print("\nBROKEN DEPENDENCIES:")
        total = 0
        for source, refs in broken.items():
            print(f"\n  In {source}:")
            for r in sorted(refs):
                print(f"    [BROKEN] {r}")
                total += 1
        print(f"\nTotal broken: {total}")
        sys.exit(1)
    else:
        print("\nAll dependencies verified. No broken links found.")
        sys.exit(0)

if __name__ == "__main__":
    main()
