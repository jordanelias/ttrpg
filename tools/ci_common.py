#!/usr/bin/env python3
"""
ci_common.py — shared helpers for the Valoria validators.

Single source of truth for "what changed" so every caller (GitHub Actions CI,
the local .githooks/pre-commit hook, the Claude Code PreToolUse runner, and the
unit tests) computes the changeset the same way. Previously get_changed_files()
was copy-pasted byte-for-byte into ci_co_file_checker.py and ci_editorial_checker.py;
this module collapses that duplication.

Modes:
  'ci'      — use GitHub Actions event context (push / pull_request); the
              authoritative path. Falls back to HEAD~1 then the empty tree.
  'staged'  — the index (git diff --cached): what a `git commit` is about to record.
              Used by the local pre-commit hook and the PreToolUse runner.
  'local'   — HEAD~1..HEAD (or empty tree for the first commit): ad-hoc local runs.

All functions are pure wrappers over `git`; no network, no PAT, no cache.
"""
import os
import subprocess

# git's well-known empty-tree object — diff against this == "everything is new".
EMPTY_TREE = '4b825dc642cb6eb9a060e54bf8d69288fbee4904'


def _git(args):
    """Run a git command, returning stdout on success and '' on failure.

    Decodes as UTF-8 explicitly (errors='replace'). This is REQUIRED on Windows:
    text=True would decode with the cp1252 locale, which fails on the UTF-8 bytes
    in the design corpus (em-dashes, minus signs) and silently yields stdout=None.
    The repo is UTF-8; CI (Linux) is UTF-8 too, so this is consistent everywhere.
    """
    r = subprocess.run(['git'] + args, capture_output=True,
                       encoding='utf-8', errors='replace')
    return (r.stdout or '') if r.returncode == 0 else ''


def _has_parent():
    return bool(_git(['rev-parse', '--verify', '-q', 'HEAD~1']).strip())


def _diff_args(mode):
    """Return the git-diff revision args for `mode` (excluding 'diff' itself)."""
    if mode == 'staged':
        return ['--cached']
    if mode == 'local':
        return ['HEAD~1', 'HEAD'] if _has_parent() else [EMPTY_TREE, 'HEAD']

    # mode == 'ci'
    event = os.environ.get('GITHUB_EVENT_NAME', '')
    before = os.environ.get('GITHUB_EVENT_BEFORE', '')
    sha = os.environ.get('GITHUB_SHA', '')
    base = os.environ.get('GITHUB_BASE_REF', '')
    if event == 'push' and before and sha and before != '0' * 40:
        return [before, sha]
    if event == 'pull_request' and base:
        return [f'origin/{base}...HEAD']
    return ['HEAD~1', 'HEAD'] if _has_parent() else [EMPTY_TREE, 'HEAD']


def get_changed_files(mode='ci'):
    """Set of repo-relative paths changed in the given mode (added/modified/deleted)."""
    out = _git(['diff', '--name-only'] + _diff_args(mode))
    return {line for line in out.splitlines() if line.strip()}


def get_changed_files_filtered(mode='ci', diff_filter=None):
    """Like get_changed_files but with a git --diff-filter (e.g. 'd' to drop deletions)."""
    args = ['diff', '--name-only']
    if diff_filter:
        args.append(f'--diff-filter={diff_filter}')
    out = _git(args + _diff_args(mode))
    return {line for line in out.splitlines() if line.strip()}


def get_added_lines(mode='ci'):
    """
    Map {path: [added_line, ...]} containing only the ADDED ('+') lines of the diff.

    This is what makes the naming guard diff-aware: it inspects only newly-introduced
    text, so the ~28 files that legitimately contain the forbidden token (registries,
    tests, archives, the matcher itself) are never re-flagged for content they already had.
    """
    out = _git(['diff', '--unified=0', '--no-color'] + _diff_args(mode))
    result = {}
    current = None
    for line in out.splitlines():
        if line.startswith('+++ '):
            target = line[4:].strip()
            if target == '/dev/null':
                current = None
            else:
                current = target[2:] if target.startswith('b/') else target
                result.setdefault(current, [])
        elif line.startswith('+') and not line.startswith('+++') and current is not None:
            result[current].append(line[1:])
    return result


def read_text(path):
    """Read a working-tree file as UTF-8; return None if missing or undecodable."""
    try:
        with open(path, encoding='utf-8', errors='strict') as f:
            return f.read()
    except (FileNotFoundError, IsADirectoryError, UnicodeDecodeError):
        return None
