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

def _load_restructure_map():
    """Old→new path mapping from references/restructure_ledger.md — the sanctioned
    registry of repo-restructure moves. Lets live ledger entries that predate the
    restructure resolve without rewriting the append-only ledger itself."""
    content = read_file("references/restructure_ledger.md")
    mapping = {}
    if content:
        for m in re.finditer(r'^\|\s*`([^`]+)`\s*\|\s*`([^`]+)`\s*\|', content, re.M):
            mapping[m.group(1).strip()] = m.group(2).strip()
    return mapping


# Statuses whose entries are still live obligations; resolved/struck/superseded
# entries are historical record and legitimately cite paths that have since moved.
LIVE_STATUSES = ('open', 'provisional', 'applied', 'confirmed', 'deferred')

# Lane-split active ledger (2026-07-08 atomization pass): ED-<LANE>-NNNN entries live in
# their own canon/editorial_ledger_<lane>.jsonl file, mirroring handoffs/HANDOFF_<LANE>.md.
# Pre-cutover flat-ID entries stay in the main file (no retrofit). Both are "active" and
# must be checked the same way, or the lane-tagged 1/3 of live entries would silently stop
# being validated for broken paths — the exact failure class ED-1081 already fixed once.
_LANE_CODES = ('MB', 'PC', 'FI', 'SC', 'FA', 'WR', 'IN', 'GO', 'SE')
LANE_LEDGER_PATHS = tuple(f'canon/editorial_ledger_{lane.lower()}.jsonl' for lane in _LANE_CODES)


def check_editorial_ledger(all_files):
    """Check LIVE entries of canon/editorial_ledger.jsonl + its per-lane siblings for
    broken paths.

    ED-1081: this check was silently dead since inception — it read
    canon/editorial_ledger.yaml, which never existed (the ledger is JSONL), and
    the missing-file branch returned clean. It now reads the real file; validates
    only live-status entries; and resolves pre-restructure paths through
    references/restructure_ledger.md (a live ref whose mapped new home exists is
    an INFO line, not a violation — migrating the entry text is a canon edit that
    stays with Jordan)."""
    import json
    remap = _load_restructure_map()
    broken, infos = [], []
    found_any = False
    for ledger_path in ("canon/editorial_ledger.jsonl", *LANE_LEDGER_PATHS):
        content = read_file(ledger_path)
        if content is None:
            continue  # lane files are created on first allocation to that lane
        found_any = True
        for line in content.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
                status = str(entry.get('status', '')).lower()
                ed_id = entry.get('id', '?')
            except (ValueError, AttributeError):
                status, ed_id = 'open', '?'  # unparseable line: treat as live, surface its refs
            if not status.startswith(LIVE_STATUSES):
                continue
            for ref in extract_file_refs(line, ledger_path):
                if ref in all_files:
                    continue
                new_home = remap.get(ref)
                if new_home and new_home in all_files:
                    infos.append(f"{ed_id}: {ref} -> {new_home} (pre-restructure path; mapped home exists)")
                else:
                    broken.append(f"{ref} (live entry {ed_id})")
    if not found_any:
        return [], ["canon/editorial_ledger.jsonl not found"]
    for note in sorted(infos):
        print(f"  [INFO] {note}")
    return broken, []

def _find_valoria_hooks_path():
    """Locate valoria_hooks.py anywhere in the working tree. Returns None if it
    doesn't exist at all -- callers must then skip the paired_hook existence
    check rather than inventing a check against a file that isn't here."""
    for root, dirs, names in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in _IGNORE_DIRS]
        if 'valoria_hooks.py' in names:
            return os.path.join(root, 'valoria_hooks.py')
    return None


def _extract_field(block, field):
    """Pull a scalar YAML field's value out of one `- path: ...` entry block.
    Handles both `field: ""` (quoted, possibly empty) and `field: bare-value`
    (unquoted, trailing `# comment` stripped by the whitespace boundary).
    Regex-based on purpose: this checker is stdlib-only by design (no PyYAML
    install step in the `integrity` CI job) -- mirrors extract_file_refs' regex-
    over-structured-text approach used elsewhere in this same file."""
    m = re.search(rf'^\s*{field}:\s*"([^"]*)"', block, re.M)
    if m:
        return m.group(1).strip()
    m = re.search(rf'^\s*{field}:\s*(\S+)', block, re.M)
    if m:
        val = m.group(1).strip()
        return '' if val == '""' else val
    return ''


def _parse_ci_checks_entries(registry_text):
    """Extract (path, ci_job, paired_hook) for every `ci_checks:` list entry."""
    m = re.search(r'^ci_checks:\s*\n(.*?)(?=^\S|\Z)', registry_text, re.M | re.S)
    section = m.group(1) if m else ''
    entries = []
    for block in re.split(r'\n(?=\s*-\s*path:)', section):
        pm = re.search(r'-\s*path:\s*(\S+)', block)
        if not pm:
            continue
        entries.append({
            'path': pm.group(1).strip(),
            'ci_job': _extract_field(block, 'ci_job'),
            'paired_hook': _extract_field(block, 'paired_hook'),
        })
    return entries


def check_ci_registry_coverage(all_files):
    """Cross-check references/ci_checks_registry.yaml against the working tree and
    .github/workflows/valoria-ci.yml (ED-IN-0033, Phase 2 item 11 -- the registry's
    own header has demanded a self-check since 2026-05-10: "this registry must
    update in the same commit" plus a proposed-but-never-built check that every
    listed paired_hook actually exists).

    Four checks:
      (a) every registry `path:` exists on disk;
      (b) every non-empty `ci_job:` names a real job id in valoria-ci.yml;
      (c) every `python[3] tools/X.py` invocation anywhere in valoria-ci.yml has a
          corresponding `path: tools/X.py` entry somewhere in the registry;
      (d) every non-empty `paired_hook:` exists as a `def <name>(` in
          valoria_hooks.py -- skipped (INFO note, not a violation) if that file
          doesn't exist anywhere in the repo (it currently lives only under
          deprecated/skills/valoria-orchestrator/scripts/, so the check DOES run
          against that path when present).
    """
    violations = []
    errors = []

    registry_text = read_file('references/ci_checks_registry.yaml')
    if registry_text is None:
        return [], ["references/ci_checks_registry.yaml not found"]

    workflow_text = read_file('.github/workflows/valoria-ci.yml')
    if workflow_text is None:
        return [], [".github/workflows/valoria-ci.yml not found"]

    jm = re.search(r'^jobs:\s*\n(.*)\Z', workflow_text, re.M | re.S)
    jobs_section = jm.group(1) if jm else workflow_text
    job_ids = set(re.findall(r'^  ([a-zA-Z][\w-]*):\s*$', jobs_section, re.M))

    entries = _parse_ci_checks_entries(registry_text)
    registry_paths = {e['path'] for e in entries if e['path']}

    # (a) + (b)
    for e in entries:
        path = e['path']
        if path and path not in all_files:
            violations.append(f"ci_checks_registry.yaml: path does not exist on disk: {path}")
        ci_job = e['ci_job']
        if ci_job and ci_job not in job_ids:
            violations.append(
                f"ci_checks_registry.yaml: ci_job {ci_job!r} (path={path}) is not a job id "
                f"in .github/workflows/valoria-ci.yml"
            )

    # (c) Only real invocations count -- strip comment-only lines first, so a
    # `#` line documenting or mentioning a tool path (e.g. a `--update` usage
    # note, or prose in an added-job comment block) can never trip this BLOCKING
    # check. A trailing `# ...` on a genuine `run:` line is untouched -- only
    # lines whose FIRST non-whitespace character is `#` are dropped. Caught by
    # adversarial review of ED-IN-0033: the pre-fix regex matched
    # `# python3 tools/freshness_gate.py --update` (a usage-note comment) and
    # would have false-positived on any future commented-out example invoking
    # an unregistered tool.
    non_comment_text = '\n'.join(
        line for line in workflow_text.splitlines()
        if not line.lstrip().startswith('#')
    )
    invoked = set(re.findall(r'python3?\s+(tools/[\w./-]+\.py)', non_comment_text))
    for inv in sorted(invoked):
        if inv not in registry_paths:
            violations.append(
                f"valoria-ci.yml invokes {inv} but no matching `path: {inv}` entry exists "
                f"in references/ci_checks_registry.yaml"
            )

    # (d)
    hooks_path = _find_valoria_hooks_path()
    if hooks_path is None:
        errors.append(
            "valoria_hooks.py not found anywhere in the repo -- paired_hook existence "
            "check (d) skipped, not invented against a nonexistent file"
        )
    else:
        try:
            with open(hooks_path, encoding='utf-8') as f:
                hooks_content = f.read()
        except OSError:
            hooks_content = ''
        defined_hooks = set(re.findall(r'^def (\w+)\(', hooks_content, re.M))
        hooks_rel = os.path.relpath(hooks_path, REPO_ROOT).replace(os.sep, '/')
        for e in entries:
            hook = e['paired_hook']
            if hook and hook not in defined_hooks:
                violations.append(
                    f"ci_checks_registry.yaml: paired_hook {hook!r} (path={e['path']}) not "
                    f"found as a function in {hooks_rel}"
                )

    return violations, errors


def main():
    print("Scanning working tree...")
    all_files = get_all_repo_files()
    print(f"Found {len(all_files)} files in working tree")

    broken = {}
    errors = []

    checks = [
        ("propagation_map.md",    check_propagation_map),
        ("canonical_sources.yaml", check_canonical_sources),
        ("editorial_ledger.jsonl", check_editorial_ledger),
        ("ci_checks_registry.yaml", check_ci_registry_coverage),
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
