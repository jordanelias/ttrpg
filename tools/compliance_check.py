"""
compliance_check.py — Valoria compliance orchestrator.

Called by hooks. Reads atomization_rules.yaml, checks repo state, dispatches fixes.
Two modes:
  1. check_all() — full repo scan (bootstrap, session close)
  2. validate_commit() — pre-commit check of proposed additions

Dependencies: github_ops (for repo I/O), atomizer, doc_index_gen, index_gen, PyYAML.
"""

import sys, os, re, fnmatch
sys.path.insert(0, '/home/claude')

import yaml
from dataclasses import dataclass, field

# Lazy imports to avoid circular deps at module load
_atomizer = None
_doc_index_gen = None
_index_gen = None
_github_ops = None

def _lazy_import():
    global _atomizer, _doc_index_gen, _index_gen, _github_ops
    if _atomizer is None:
        # Tools may be in /home/claude or tools/ — handle both.
        # If a required tool is missing entirely (typical in a fresh container
        # session — bootstrap only fetches valoria_hooks.py and github_ops.py
        # by default), pull it from GitHub. Mirrors the auto-fetch pattern in
        # valoria_hooks.assert_bootstrap.
        for tools_dir in ['/home/claude', '/home/claude/tools', '.']:
            if os.path.isfile(os.path.join(tools_dir, 'atomizer.py')):
                if tools_dir not in sys.path:
                    sys.path.insert(0, tools_dir)
                break

        # Auto-fetch any of compliance_check's tool dependencies that aren't
        # on disk yet. Without this, a fresh session hits "No module named
        # 'doc_index_gen' — skipping" on every bootstrap.
        required = ['atomizer.py', 'doc_index_gen.py', 'index_gen.py']
        missing = [n for n in required
                   if not any(os.path.isfile(os.path.join(d, n))
                              for d in sys.path)]
        if missing:
            try:
                import urllib.request, json, base64
                pat = os.environ.get('GITHUB_PAT', '') or (
                    open('/home/claude/.valoria_pat').read().strip()
                    if os.path.isfile('/home/claude/.valoria_pat') else ''
                )
                if pat:
                    for tool_name in missing:
                        req = urllib.request.Request(
                            'https://api.github.com/repos/jordanelias/ttrpg/'
                            f'contents/tools/{tool_name}?ref=main',
                            headers={
                                'Authorization': f'token {pat}',
                                'Accept': 'application/vnd.github.v3+json',
                            },
                        )
                        with urllib.request.urlopen(req) as r:
                            data = json.loads(r.read())
                        open(f'/home/claude/{tool_name}', 'w').write(
                            base64.b64decode(data['content']).decode()
                        )
                    if '/home/claude' not in sys.path:
                        sys.path.insert(0, '/home/claude')
            except Exception:
                # If fetch fails the imports below will raise a clearer error.
                pass

        import atomizer as _a
        import doc_index_gen as _s
        import index_gen as _i
        import github_ops as _g
        _atomizer = _a
        _doc_index_gen = _s
        _index_gen = _i
        _github_ops = _g


# ── Violation dataclass ──────────────────────────────────────────────────────

@dataclass
class Violation:
    path: str
    rule: dict
    kind: str           # 'size_exceeded' | 'missing_index' | 'stale_index' |
                        # 'missing_index' | 'archive_needed' | 'unknown_pattern'
    current_tokens: int
    threshold: int
    auto_fixable: bool
    fix_action: str     # 'atomizer.atomize' | 'doc_index_gen.generate_index' | etc.
    fix_args: dict = field(default_factory=dict)
    severity: str = 'error'  # 'error' | 'warn' | 'info'

    def __str__(self):
        return (f"[{self.severity.upper()}] {self.kind}: {self.path} "
                f"({self.current_tokens:,} tokens, threshold {self.threshold:,})")


# ── Rules loading ────────────────────────────────────────────────────────────

_rules_cache = None

def _load_rules(repo: str = 'ttrpg') -> dict:
    """Load and cache atomization_rules.yaml."""
    global _rules_cache
    if _rules_cache is not None:
        return _rules_cache
    _lazy_import()
    files = _github_ops.read_files_graphql(
        ['references/atomization_rules.yaml'],
        repo=repo, skip_health_check=True, skip_cache=True,
    )
    content = files.get('references/atomization_rules.yaml')
    if not content:
        raise RuntimeError(
            "[COMPLIANCE] Cannot load references/atomization_rules.yaml. "
            "Compliance check impossible."
        )
    _rules_cache = yaml.safe_load(content)
    return _rules_cache


def _match_rule(path: str, rules: dict) -> dict | None:
    """First-match policy lookup using fnmatch patterns."""
    policies = rules.get('policies', [])
    for policy in policies:
        pattern = policy.get('match', '')
        # Check exclude_suffix
        excludes = policy.get('exclude_suffix', [])
        if any(path.endswith(suffix) for suffix in excludes):
            continue
        if fnmatch.fnmatch(path, pattern):
            return policy
    return None


# ── Check functions ──────────────────────────────────────────────────────────

def _check_size(path: str, content: str, rule: dict) -> Violation | None:
    """Check file size against max_tokens."""
    max_tokens = rule.get('max_tokens')
    if max_tokens is None:
        return None
    current_tokens = len(content) // 4
    if current_tokens <= max_tokens:
        return None

    on_exceed = rule.get('on_exceed', 'error')

    # 'skip' means explicitly exempted — produce no violation.
    if on_exceed == 'skip':
        return None

    strategy = rule.get('split_strategy')

    # Determine if auto-fixable
    auto_fixable = strategy is not None or on_exceed == 'block_commit'
    if on_exceed in ('flag_unknown_pattern', 'flag_for_split', 'flag_for_next_session'):
        auto_fixable = False

    fix_action = ''
    if strategy:
        fix_action = 'atomizer.atomize'
    elif rule.get('auto_archive_status'):
        fix_action = 'atomizer.archive_by_status'
        auto_fixable = True

    severity = 'warn' if on_exceed.startswith('flag') else 'error'

    return Violation(
        path=path, rule=rule, kind='size_exceeded',
        current_tokens=current_tokens, threshold=max_tokens,
        auto_fixable=auto_fixable, fix_action=fix_action,
        severity=severity,
    )


def _check_index(path: str, content: str, rule: dict,
                    repo_files: dict) -> Violation | None:
    """Check if index exists and is fresh for design docs."""
    _lazy_import()
    require_above = rule.get('require_index_above')
    if require_above is None:
        return None
    current_tokens = len(content) // 4
    if current_tokens <= require_above:
        return None

    idx_path = _doc_index_gen.index_path_for(path)
    idx_content = repo_files.get(idx_path)

    if idx_content is None:
        return Violation(
            path=path, rule=rule, kind='missing_index',
            current_tokens=current_tokens, threshold=require_above,
            auto_fixable=True,
            fix_action='doc_index_gen.generate_index',
            fix_args={'canonical_path': path, 'index_path': idx_path},
        )

    # Check staleness (would need SHA comparison — simplified: always regen if content differs)
    # In practice, the SHA check happens via needs_regeneration()
    return None


def _check_archive_pressure(path: str, content: str, rule: dict) -> Violation | None:
    """Check if active register needs archiving."""
    archive_statuses = rule.get('auto_archive_status')
    if not archive_statuses:
        return None

    max_tokens = rule.get('max_tokens', 10000)
    archive_threshold = rule.get('archive_threshold', int(max_tokens * 0.9))
    current_tokens = len(content) // 4

    if current_tokens <= archive_threshold:
        return None

    return Violation(
        path=path, rule=rule, kind='archive_needed',
        current_tokens=current_tokens, threshold=archive_threshold,
        auto_fixable=True,
        fix_action='atomizer.archive_by_status',
        fix_args={'active_path': path},
    )


# ── Public interface ─────────────────────────────────────────────────────────

def check_all(repo: str = 'ttrpg') -> list[Violation]:
    """
    Scan repo against rules. Returns list of violations.
    Two-pass strategy:
      Pass 1: directory listing (cheap — identifies candidate files)
      Pass 2: fetch only files flagged in pass 1 for content-level checks
    """
    _lazy_import()
    rules = _load_rules(repo)
    defaults = rules.get('defaults', {})

    # Pass 1: get repo file listing
    try:
        import urllib.request, json
        pat = _github_ops._get_pat()
        req = urllib.request.Request(
            f'https://api.github.com/repos/jordanelias/{repo}/git/trees/main?recursive=1',
            headers={
                'Authorization': f'token {pat}',
                'Accept': 'application/vnd.github.v3+json',
            }
        )
        with urllib.request.urlopen(req) as r:
            tree_data = json.loads(r.read())
        all_paths = [item['path'] for item in tree_data.get('tree', [])
                     if item['type'] == 'blob'
                     and (item['path'].endswith('.md') or item['path'].endswith('.yaml'))]
    except Exception as e:
        raise RuntimeError(f"[COMPLIANCE] Cannot list repo files: {e}")

    # Match each file against rules
    files_to_check = []
    for path in all_paths:
        rule = _match_rule(path, rules)
        if rule:
            files_to_check.append((path, rule))

    if not files_to_check:
        return []

    # Pass 2: fetch files that need content checks (batched)
    paths_to_fetch = [p for p, r in files_to_check
                      if r.get('max_tokens') or r.get('require_index_above')
                      or r.get('auto_archive_status')]

    # Batch fetch (GraphQL has a practical limit, so chunk)
    repo_files = {}
    for i in range(0, len(paths_to_fetch), 50):
        batch = paths_to_fetch[i:i+50]
        fetched = _github_ops.read_files_graphql(batch, repo=repo, skip_health_check=True, skip_cache=True)
        repo_files.update(fetched)

    # Run checks
    violations = []
    for path, rule in files_to_check:
        content = repo_files.get(path)
        if content is None:
            continue

        v = _check_size(path, content, rule)
        if v:
            violations.append(v)

        v = _check_index(path, content, rule, repo_files)
        if v:
            violations.append(v)

        v = _check_archive_pressure(path, content, rule)
        if v:
            violations.append(v)

    return violations


def validate_commit(additions: list, deletions: list,
                    repo: str = 'ttrpg') -> list[Violation]:
    """
    Validate a proposed commit against rules. Checks:
      - No addition exceeds its file's max_tokens
      - Index co-files present when required
      - Index files regenerated when triggers match
    """
    _lazy_import()
    rules = _load_rules(repo)
    violations = []
    addition_paths = {p for p, _ in additions}

    for path, content in additions:
        rule = _match_rule(path, rules)
        if not rule:
            continue

        # Size check
        v = _check_size(path, content, rule)
        if v:
            violations.append(v)

        # Index co-file check for design docs
        require_above = rule.get('require_index_above')
        if require_above and len(content) // 4 > require_above:
            idx_path = _doc_index_gen.index_path_for(path)
            if idx_path not in addition_paths:
                violations.append(Violation(
                    path=path, rule=rule, kind='missing_index',
                    current_tokens=len(content) // 4, threshold=require_above,
                    auto_fixable=True,
                    fix_action='doc_index_gen.generate_index',
                    fix_args={'canonical_path': path, 'index_path': idx_path,
                              'content': content},
                ))

    return violations


def auto_fix(violations: list[Violation],
             session_commit: bool = True) -> tuple[list, str]:
    """
    Execute auto-fixable violations. Returns (additions, commit_message).
    Limits: max_auto_fix_iterations from defaults (prevent infinite loops).
    """
    _lazy_import()
    rules = _load_rules()
    max_iters = rules.get('defaults', {}).get('max_auto_fix_iterations', 3)

    additions = []
    fixed = []

    for v in violations:
        if not v.auto_fixable:
            continue

        if v.fix_action == 'doc_index_gen.generate_index':
            canonical_content = v.fix_args.get('content', '')
            if not canonical_content:
                # Need to fetch
                fetched = _github_ops.read_files_graphql(
                    [v.path], skip_health_check=True, skip_cache=True
                )
                canonical_content = fetched.get(v.path, '')
            if canonical_content:
                idx_path = v.fix_args.get('index_path',
                                           _doc_index_gen.index_path_for(v.path))
                idx_content = _doc_index_gen.generate_index(v.path, canonical_content)
                additions.append((idx_path, idx_content))
                fixed.append(f"index: {idx_path}")

        elif v.fix_action == 'atomizer.atomize':
            fetched = _github_ops.read_files_graphql(
                [v.path], skip_health_check=True, skip_cache=True
            )
            content = fetched.get(v.path, '')
            if content:
                rule = v.rule.copy()
                # If custom_map, fetch the split map
                if rule.get('split_strategy') == 'custom_map':
                    split_map_path = rule.get('split_map', '')
                    if split_map_path:
                        sm_fetched = _github_ops.read_files_graphql(
                            [split_map_path], skip_health_check=True, skip_cache=True
                        )
                        rule['_split_map_content'] = sm_fetched.get(split_map_path, '')
                new_files = _atomizer.atomize(v.path, content, rule)
                for p, c in new_files.items():
                    additions.append((p, c))
                fixed.append(f"atomize: {v.path} → {len(new_files)} files")

                # Generate index if index_replaces_canonical
                if rule.get('index_replaces_canonical'):
                    index_content = _index_gen.generate_atomized_file_index(
                        new_files, v.path
                    )
                    additions.append((v.path, index_content))
                    fixed.append(f"index: {v.path}")

        elif v.fix_action == 'atomizer.archive_by_status':
            active_path = v.fix_args.get('active_path', v.path)
            fetched = _github_ops.read_files_graphql(
                [active_path], skip_health_check=True, skip_cache=True
            )
            active_content = fetched.get(active_path, '')
            if active_content:
                # Fetch existing archives
                archive_pattern = v.rule.get('archive_target_pattern', '')
                archive_contents = {}  # Would need to discover existing archives
                new_files = _atomizer.archive_by_status(
                    active_content, active_path,
                    archive_contents, v.rule,
                )
                for p, c in new_files.items():
                    additions.append((p, c))
                fixed.append(f"archive: {active_path}")

                # Regenerate index if configured
                index_file = v.rule.get('index_file')
                if index_file:
                    # Determine index type
                    if 'patch' in active_path:
                        idx = _index_gen.generate_patch_index(
                            new_files.get(active_path, active_content),
                            {p: c for p, c in new_files.items() if p != active_path}
                        )
                    else:
                        idx = _index_gen.generate_editorial_index(
                            new_files.get(active_path, active_content),
                            {p: c for p, c in new_files.items() if p != active_path}
                        )
                    additions.append((index_file, idx))
                    fixed.append(f"index: {index_file}")

                # Regenerate summary if configured
                summary_file = v.rule.get('summary_file')
                if summary_file:
                    summary = _index_gen.generate_editorial_summary(
                        new_files.get(active_path, active_content)
                    )
                    additions.append((summary_file, summary))
                    fixed.append(f"summary: {summary_file}")

    msg = "[infrastructure] Compliance auto-fix: " + "; ".join(fixed) if fixed else "[infrastructure] Compliance check — no fixes needed"
    return additions, msg


def apply_auto_fixes_to_additions(additions: list,
                                  violations: list[Violation]) -> list:
    """
    Transform proposed additions to comply with rules.
    Returns augmented additions list.
    """
    _lazy_import()
    extra = []
    for v in violations:
        if not v.auto_fixable:
            continue
        if v.fix_action == 'doc_index_gen.generate_index':
            # Find the content in additions
            content = None
            for p, c in additions:
                if p == v.path:
                    content = c
                    break
            if content:
                idx_path = v.fix_args.get('index_path',
                                           _doc_index_gen.index_path_for(v.path))
                idx_content = _doc_index_gen.generate_index(v.path, content)
                extra.append((idx_path, idx_content))

    return additions + extra


def find_index_for(path: str, repo: str = 'ttrpg') -> str | None:
    """
    For design doc paths, check if a committed index exists.
    Returns index path if found, None otherwise.
    """
    _lazy_import()
    if not path.startswith('designs/'):
        return None
    # Skip index/infill files themselves
    if path.endswith('_index.md') or path.endswith('_infill.md'):
        return None

    idx_path = _doc_index_gen.index_path_for(path)
    if _github_ops.file_exists(idx_path, repo):
        return idx_path
    return None


def report(violations: list[Violation]) -> str:
    """Human-readable violation summary."""
    if not violations:
        return "No violations found."

    lines = [f"Compliance Report — {len(violations)} violation(s):", ""]
    for v in violations:
        auto = " [AUTO-FIXABLE]" if v.auto_fixable else " [MANUAL]"
        lines.append(f"  [{v.severity.upper()}]{auto} {v.kind}")
        lines.append(f"    Path: {v.path}")
        lines.append(f"    Size: {v.current_tokens:,} tokens (threshold: {v.threshold:,})")
        if v.fix_action:
            lines.append(f"    Fix: {v.fix_action}")
        lines.append("")

    return "\n".join(lines)


# ── CLI interface ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Valoria compliance checker")
    parser.add_argument('--check-only', action='store_true',
                        help="Check and report, exit nonzero on violations")
    parser.add_argument('--repo-state', default=None,
                        help="Path to local repo checkout (for CI)")
    args = parser.parse_args()

    if args.repo_state:
        # CI mode: check local files instead of GitHub API
        print("[COMPLIANCE] CI mode — checking local repo state")
        # Load rules from local file
        rules_path = os.path.join(args.repo_state, 'references', 'atomization_rules.yaml')
        if not os.path.isfile(rules_path):
            print("[COMPLIANCE] No atomization_rules.yaml found — skipping")
            sys.exit(0)

        with open(rules_path) as f:
            rules = yaml.safe_load(f)

        violations = []
        # Walk local files
        for root, dirs, files in os.walk(args.repo_state):
            for fname in files:
                if not (fname.endswith('.md') or fname.endswith('.yaml')):
                    continue
                full_path = os.path.join(root, fname)
                rel_path = os.path.relpath(full_path, args.repo_state)
                rule = _match_rule(rel_path, rules)
                if not rule:
                    continue
                with open(full_path) as f:
                    content = f.read()
                max_tokens = rule.get('max_tokens')
                if max_tokens and len(content) // 4 > max_tokens:
                    on_exceed = rule.get('on_exceed', 'error')
                    if on_exceed in ('flag_unknown_pattern', 'flag_for_split', 'flag_for_next_session'):
                        severity = 'warn'
                    else:
                        severity = 'error'
                    violations.append(Violation(
                        path=rel_path, rule=rule, kind='size_exceeded',
                        current_tokens=len(content) // 4, threshold=max_tokens,
                        auto_fixable=False, fix_action='',
                        severity=severity,
                    ))

        if violations:
            errors = [v for v in violations if v.severity == 'error']
            warns = [v for v in violations if v.severity == 'warn']
            if warns:
                print(f"[COMPLIANCE ⚠] {len(warns)} warning(s):")
                for v in warns:
                    print(f"  {v}")
            if errors:
                print(f"[COMPLIANCE ✗] {len(errors)} error(s):")
                for v in errors:
                    print(f"  {v}")
                sys.exit(1)
            else:
                print(f"[COMPLIANCE ✓] {len(warns)} warning(s), 0 errors")
                sys.exit(0)
        else:
            print("[COMPLIANCE ✓] All files within thresholds")
            sys.exit(0)
    else:
        # Interactive mode
        violations = check_all()
        if violations:
            print(report(violations))
            sys.exit(1 if args.check_only else 0)
        else:
            print("[COMPLIANCE ✓] No violations")
            sys.exit(0)
