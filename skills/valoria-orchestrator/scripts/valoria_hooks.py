"""
valoria_hooks.py — Hard enforcement hooks for Valoria session protocol.

Import this at the TOP of every bash_tool execution block, immediately after
importing github_ops. It wraps github_ops functions with enforcement that
cannot be bypassed by task pressure.

Usage (in every bash_tool block):
    import valoria_hooks as h
    h.assert_bootstrap()          # confirms github_ops loaded from repo this session
    h.task_gate("simulation")     # confirms required files fetched for task type
    h.editorial_gate("content")   # hard stops on editorial content without flag
    h.pre_commit_gate(additions)  # runs all pre-commit checks, raises on failure
    h.propose_mechanic_gate()     # confirms canonical sources fetched before any proposal

Every function raises RuntimeError with a clear message. No warnings. No suggestions.
"""

import os, sys, re, subprocess
sys.path.insert(0, '/home/claude')
import github_ops as g

# ── State tracking ────────────────────────────────────────────────────────────

_bootstrap_confirmed = False
_task_gates_passed   = set()   # which task types have been cleared
_editorial_gate_open = False   # True only when user has explicitly approved editorial work


# ════════════════════════════════════════════════════════════════════════════════
# HOOK 1 — Bootstrap confirmation
# Prevents any work starting if github_ops was not freshly loaded from repo.
# ════════════════════════════════════════════════════════════════════════════════

def assert_bootstrap():
    """
    Confirm github_ops.py was loaded from GitHub this session (not a stale local copy).
    Call immediately after bootstrapping. Raises if token absent (= no fetch occurred).
    """
    global _bootstrap_confirmed
    try:
        token = g.get_session_token()
        _bootstrap_confirmed = True
        print(f"[HOOK] Bootstrap confirmed. Session token: {token}")
        return token
    except RuntimeError:
        raise RuntimeError(
            "[HOOK VIOLATION] Bootstrap not confirmed — no session token exists.\n"
            "github_ops.py must be fetched from GitHub and at least one "
            "read_files_graphql() call must complete before any work begins.\n"
            "Do not proceed. Re-run the bootstrap block."
        )


# ════════════════════════════════════════════════════════════════════════════════
# HOOK 2 — Task gate
# Enforces the GitHub Read Protocol: specific files must be fetched before
# specific task types. Raises if required files not in session fetch registry.
# ════════════════════════════════════════════════════════════════════════════════

# Maps task type → required files that MUST be fetched before starting
TASK_REQUIRED_FILES = {
    "simulation": [
        "references/canonical_sources.yaml",
        "canon/02_canon_constraints.md",
    ],
    "audit": [
        "references/canonical_sources.yaml",
        "canon/02_canon_constraints.md",
    ],
    "canon_check": [
        "canon/00_philosophical_foundations.md",
        "canon/02_canon_constraints.md",
    ],
    "editorial": [
        "canon/editorial_ledger.yaml",
    ],
    "patch": [
        "canon/patch_register_active.yaml",
    ],
    "compilation": [
        "references/canonical_sources.yaml",
        "canon/patch_register_active.yaml",
    ],
    "propose_mechanic": [
        "references/canonical_sources.yaml",
        "canon/editorial_ledger_summary.yaml",
    ],
    "design": [
        "references/canonical_sources.yaml",
    ],
}

# For simulation/audit: the canonical design doc for the target system
# must ALSO be fetched. This is checked by task_gate_with_system().

def task_gate(task_type: str):
    """
    Confirm all required files for this task type have been fetched.
    Raises with explicit list of missing files if not.

    task_type: one of simulation | audit | canon_check | editorial |
               patch | compilation | propose_mechanic | design
    """
    if not _bootstrap_confirmed:
        raise RuntimeError(
            f"[HOOK VIOLATION] task_gate('{task_type}') called before assert_bootstrap().\n"
            "Run assert_bootstrap() first."
        )

    required = TASK_REQUIRED_FILES.get(task_type)
    if required is None:
        raise RuntimeError(
            f"[HOOK VIOLATION] Unknown task type '{task_type}'.\n"
            f"Valid types: {list(TASK_REQUIRED_FILES.keys())}"
        )

    missing = [p for p in required if p not in g._session_fetches or g._session_fetches[p] is None]
    if missing:
        raise RuntimeError(
            f"[HOOK VIOLATION] Task '{task_type}' requires files not yet fetched:\n"
            + "\n".join(f"  - {p}" for p in missing)
            + "\n\nFetch these via read_files_graphql() before starting this task.\n"
            "This is not optional. Proceeding without canonical sources produces invalid output."
        )

    _task_gates_passed.add(task_type)
    print(f"[HOOK] Task gate '{task_type}': PASS")


def task_gate_with_system(task_type: str, system: str, canonical_sources: dict):
    """
    Extended task gate: also confirms the canonical design doc for `system`
    has been fetched, as resolved from canonical_sources.yaml content.

    canonical_sources: parsed dict from canonical_sources.yaml
    """
    task_gate(task_type)

    # Resolve canonical doc path for system
    system_entry = canonical_sources.get("systems", {}).get(system, {})
    canonical_path = system_entry.get("canonical") or system_entry.get("design_doc")

    if not canonical_path:
        raise RuntimeError(
            f"[HOOK VIOLATION] System '{system}' not found in canonical_sources.yaml\n"
            f"or has no canonical/design_doc entry.\n"
            f"Fetch and check canonical_sources.yaml before proceeding."
        )

    if canonical_path not in g._session_fetches or g._session_fetches[canonical_path] is None:
        raise RuntimeError(
            f"[HOOK VIOLATION] Canonical design doc for '{system}' not fetched:\n"
            f"  Required: {canonical_path}\n"
            f"Fetch via read_files_graphql(['{canonical_path}']) before starting."
        )

    print(f"[HOOK] System gate '{system}' ({canonical_path}): PASS")


# ════════════════════════════════════════════════════════════════════════════════
# HOOK 3 — Editorial gate
# The user retains exclusive authority over setting, worldbuilding, characters,
# narrative, faction behaviour, ambiguous design intent.
# This hook enforces that: any output containing editorial content must be
# flagged [EDITORIAL: ED-NNN] and NOT committed without user approval.
# ════════════════════════════════════════════════════════════════════════════════

EDITORIAL_CONTENT_PATTERNS = [
    r'\[EDITORIAL:',           # explicit flag — allowed, means flagged correctly
    r'\bcharacter\s+name\b',
    r'\bfaction\s+identity\b',
    r'\bworldbuilding\b',
    r'\bnarrative\s+decision\b',
    r'\bsetting\s+decision\b',
]

# Paths that require [EDITORIAL] or [PROVISIONAL] flags if they contain
# narrative/worldbuilding prose (not just mechanical tables/formulas)
EDITORIAL_PATH_PREFIXES = (
    'designs/npcs/',
    'designs/worldbuilding/',
    'designs/setting/',
    'gm_ref/',
    'canon/03_',   # timeline = worldbuilding
)

# If content in an editorial path lacks these markers, flag for review
EDITORIAL_MARKERS = ('[EDITORIAL:', '[PROVISIONAL:', '[EDITORIAL GATE]')

def editorial_gate(path: str, content: str):
    """
    Hard gate for commits to editorial-governed paths.
    Raises if:
      - Path is under an editorial-governed prefix AND
      - Content contains no [EDITORIAL] or [PROVISIONAL] markers AND
      - Content is longer than 200 chars (i.e. substantive, not a stub)

    Use: call for every addition in pre_commit_gate automatically.
    Does NOT block mechanical content (tables, formulas, params files).
    """
    is_editorial_path = any(path.startswith(p) for p in EDITORIAL_PATH_PREFIXES)
    if not is_editorial_path:
        return  # not an editorial-governed file

    has_marker = any(m in content for m in EDITORIAL_MARKERS)
    is_substantive = len(content) > 200

    if is_substantive and not has_marker:
        raise RuntimeError(
            f"[HOOK VIOLATION] Committing to editorial path without flag:\n"
            f"  Path: {path}\n"
            f"  This path requires [EDITORIAL: ED-NNN] or [PROVISIONAL: ...] markers\n"
            f"  for any substantive content changes.\n\n"
            f"User retains exclusive authority over: setting, worldbuilding, characters,\n"
            f"narrative, faction behaviour, ambiguous design intent.\n"
            f"Add [EDITORIAL: ED-NNN — description] flags before committing."
        )
    print(f"[HOOK] Editorial gate '{path}': PASS")


# ════════════════════════════════════════════════════════════════════════════════
# HOOK 4 — Pre-commit gate
# Runs ALL required pre-commit checks. Raises on any failure.
# This replaces the prose instruction "run these three tools before committing."
# ════════════════════════════════════════════════════════════════════════════════

def pre_commit_gate(additions: list, deletions: list = None, run_tools: bool = True):
    """
    Hard gate before any atomic_commit() call. Raises on ANY violation.

    Checks:
    1. Register size thresholds (via github_ops TOKEN_THRESHOLDS)
    2. Commit message format (caller must pass message separately — checked in commit_gate)
    3. Required co-files (params + canonical_sources + propagation_map rules)
    4. Tool runner: freshness_gate, broken_dependency_checker, patch_propagation_checker

    additions: list of (path, content) tuples — same as atomic_commit() additions arg
    run_tools: set False only in infrastructure commits (tools themselves being updated)
    """
    if deletions is None:
        deletions = []

    errors = []

    # ── Editorial gate per path ──────────────────────────────────────────────
    for path, content in additions:
        editorial_gate(path, content)

    # ── Size check ────────────────────────────────────────────────────────────
    for path, content in additions:
        tokens = len(content) // 4
        threshold = g.TOKEN_THRESHOLDS.get(path)
        if threshold and tokens > threshold:
            errors.append(
                f"SIZE VIOLATION: {path} would be {tokens:,} tokens (limit {threshold:,}).\n"
                f"  Archive old content before committing."
            )

    # ── Required co-files check ───────────────────────────────────────────────
    paths_in_commit = {p for p, _ in additions} | set(deletions)

    # If any design doc changes → canonical_sources.yaml must be in commit
    design_changed = any('designs/' in p for p in paths_in_commit)
    if design_changed and 'references/canonical_sources.yaml' not in paths_in_commit:
        errors.append(
            "MISSING CO-FILE: design doc modified but references/canonical_sources.yaml "
            "not included.\nAdd canonical_sources.yaml to commit if source authority changed."
        )

    # If mechanical values changed → corresponding params file must be in commit
    # (heuristic: if a design doc is included, its params file should be too)
    for path, content in additions:
        if 'designs/' in path and '_v30.md' in path:
            system = path.split('/')[-1].replace('_v30.md', '').replace('_', '')
            params_candidates = [
                f'references/params_{system}.md',
                f'references/params_{path.split("/")[1]}.md',
            ]
            params_present = any(p in paths_in_commit for p in params_candidates)
            if not params_present and 'infill' not in path:
                errors.append(
                    f"MISSING CO-FILE: {path} modified but no params file found in commit.\n"
                    f"  Expected one of: {params_candidates}\n"
                    f"  Include params file if mechanical values changed."
                )

    # If patches applied → patch_register_active must be in commit
    patch_keywords = ['patch', 'PP-', '[patch]']
    has_patch = any(
        any(kw in content for kw in patch_keywords)
        for _, content in additions
    )
    if has_patch and 'canon/patch_register_active.yaml' not in paths_in_commit:
        errors.append(
            "MISSING CO-FILE: patch content detected but canon/patch_register_active.yaml "
            "not in commit.\nInclude patch register in any commit that applies patches."
        )

    # ── Tool runner ───────────────────────────────────────────────────────────
    if run_tools:
        for tool in [
            'tools/freshness_gate.py --update',
            'tools/broken_dependency_checker.py',
            'tools/patch_propagation_checker.py',
        ]:
            try:
                result = subprocess.run(
                    ['python3'] + tool.split(),
                    capture_output=True, text=True, cwd='/home/claude'
                )
                if result.returncode != 0:
                    errors.append(
                        f"TOOL FAILURE: python3 {tool} exited {result.returncode}\n"
                        f"  stdout: {result.stdout[-500:]}\n"
                        f"  stderr: {result.stderr[-500:]}"
                    )
                else:
                    print(f"[HOOK] Tool {tool.split()[0]}: PASS")
            except FileNotFoundError:
                # Tool not available in container — skip with warning (not error)
                print(f"[HOOK] Tool {tool.split()[0]}: SKIPPED (not found in container)")

    # ── Raise if any errors ───────────────────────────────────────────────────
    if errors:
        raise RuntimeError(
            "[HOOK VIOLATION] Pre-commit gate failed:\n\n"
            + "\n\n".join(f"  [{i+1}] {e}" for i, e in enumerate(errors))
            + "\n\nFix all violations before calling atomic_commit()."
        )

    print(f"[HOOK] Pre-commit gate: PASS ({len(additions)} additions, {len(deletions)} deletions)")


# ════════════════════════════════════════════════════════════════════════════════
# HOOK 5 — Commit message gate
# Enforces commit message format. Raises on non-conforming messages.
# ════════════════════════════════════════════════════════════════════════════════

VALID_SCOPES = {'editorial', 'patch', 'simulation', 'compilation', 'infrastructure', 'skill', 'cleanup'}
COMMIT_FORMAT = re.compile(r'^\[(editorial|patch|simulation|compilation|infrastructure|skill|cleanup)\] .{10,}')

def commit_message_gate(message: str):
    """Raises if commit message does not match [scope] description format."""
    if not COMMIT_FORMAT.match(message):
        raise RuntimeError(
            f"[HOOK VIOLATION] Invalid commit message format: '{message}'\n"
            f"Required: '[scope] description — PP-NNN / ED-NNN if applicable'\n"
            f"Valid scopes: {sorted(VALID_SCOPES)}"
        )
    print(f"[HOOK] Commit message: PASS")


# ════════════════════════════════════════════════════════════════════════════════
# HOOK 6 — Propose mechanic gate
# Enforces: never propose rules from memory. canonical_sources + canonical
# design doc + params + editorial ledger must be fetched first.
# ════════════════════════════════════════════════════════════════════════════════

def propose_mechanic_gate(system: str):
    """
    Call before proposing any mechanic or rule for system.
    Confirms canonical_sources fetched. Raises if not.
    Then returns the canonical doc path so caller can fetch it.
    """
    if 'references/canonical_sources.yaml' not in g._session_fetches:
        raise RuntimeError(
            f"[HOOK VIOLATION] propose_mechanic_gate('{system}') called but "
            f"canonical_sources.yaml not fetched.\n"
            f"Fetch canonical_sources.yaml first — you cannot propose mechanics "
            f"without knowing which document is canonical for '{system}'."
        )
    print(f"[HOOK] Propose mechanic gate '{system}': canonical_sources present")
    # Caller is responsible for then fetching the canonical doc + params


# ════════════════════════════════════════════════════════════════════════════════
# HOOK 7 — Context limit gate
# Raises a warning (not error) when context is approaching limits.
# Enforces session-close before degradation.
# Cannot actually measure context, but can count tokens fetched this session.
# ════════════════════════════════════════════════════════════════════════════════

CONTEXT_WARN_TOKENS  = 140_000   # warn at 70% of 200k
CONTEXT_HARD_TOKENS  = 180_000   # hard stop at 90%

def context_gate():
    """
    Estimate tokens consumed this session from fetch registry.
    Raises hard stop at 90% threshold. Warns at 70%.
    Call periodically during long sessions.
    """
    total_chars = sum(
        len(c) for c in g._session_fetches.values() if c
    )
    estimated_tokens = total_chars // 4

    if estimated_tokens >= CONTEXT_HARD_TOKENS:
        raise RuntimeError(
            f"[HOOK VIOLATION] Context limit approaching hard stop.\n"
            f"Estimated tokens from fetches alone: {estimated_tokens:,} of 200,000.\n"
            f"HALT all tasks. Run Session Close Protocol immediately.\n"
            f"Commit all in-progress state. Start a new chat."
        )
    elif estimated_tokens >= CONTEXT_WARN_TOKENS:
        print(
            f"[HOOK WARNING] Context at ~{estimated_tokens:,} tokens from fetches "
            f"(70% threshold). Complete current stage then close session."
        )
    else:
        print(f"[HOOK] Context gate: {estimated_tokens:,} estimated fetch tokens — OK")


# ════════════════════════════════════════════════════════════════════════════════
# HOOK 8 — Memory contamination guard
# Prevents using _session_fetches values that were never actually fetched
# (i.e. injected via memory or project files).
# ════════════════════════════════════════════════════════════════════════════════

def memory_contamination_guard(path: str, content: str):
    """
    Verify that content for path actually came from GitHub this session,
    not from memory or a local file. Raises if content doesn't match session fetch.
    """
    fetched = g._session_fetches.get(path)
    if fetched is None:
        raise RuntimeError(
            f"[HOOK VIOLATION] memory_contamination_guard: '{path}' was not fetched "
            f"from GitHub this session.\n"
            f"Do not use content from memory, project files, or local copies.\n"
            f"Fetch from GitHub via read_files_graphql(['{path}'])."
        )
    if fetched != content:
        raise RuntimeError(
            f"[HOOK VIOLATION] memory_contamination_guard: content for '{path}' "
            f"does not match what was fetched from GitHub.\n"
            f"Content has been modified locally without a re-fetch after commit.\n"
            f"Re-fetch the file before using it."
        )
    print(f"[HOOK] Memory contamination guard '{path}': PASS")


# ════════════════════════════════════════════════════════════════════════════════
# CONVENIENCE: atomic_commit with all gates built in
# Use this instead of g.atomic_commit() directly.
# ════════════════════════════════════════════════════════════════════════════════

def safe_commit(additions: list, deletions: list, message: str, run_tools: bool = True) -> str:
    """
    Drop-in replacement for g.atomic_commit() with all hooks enforced:
    1. commit_message_gate
    2. editorial_gate (per path)
    3. pre_commit_gate (size, co-files, tools)
    3. g.atomic_commit()

    Returns commit OID on success.
    """
    commit_message_gate(message)
    pre_commit_gate(additions, deletions, run_tools=run_tools)
    oid = g.atomic_commit(additions=additions, deletions=deletions, message=message)
    print(f"[HOOK] safe_commit: SUCCESS — {oid}")
    return oid
