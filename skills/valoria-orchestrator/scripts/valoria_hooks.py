"""
valoria_hooks.py — Hard enforcement for Valoria session protocol.

Import as `h` immediately after bootstrapping github_ops.
Every function raises RuntimeError — no warnings, no soft failures.

Usage in every bash_tool block:
    import valoria_hooks as h
    h.assert_bootstrap()
    # ... task-specific gates ...
    oid = h.safe_commit(additions, deletions, message)
"""

import os, sys, re
sys.path.insert(0, '/home/claude')
import github_ops as g

_bootstrap_confirmed = False
_task_gates_passed   = set()

EDITORIAL_PATHS = (
    'designs/npcs/',
    'designs/worldbuilding/',
    'designs/setting/',
    'gm_ref/',
    'canon/03_',
)
EDITORIAL_MARKERS = ('[EDITORIAL:', '[PROVISIONAL:', '[EDITORIAL GATE]')

VALID_SCOPES    = {'editorial','patch','simulation','compilation','infrastructure','skill','cleanup'}
COMMIT_FORMAT   = re.compile(r'^\[(editorial|patch|simulation|compilation|infrastructure|skill|cleanup)\] .{10,}')

CONTEXT_WARN    = 140_000
CONTEXT_HARD    = 180_000

TASK_REQUIRED_FILES = {
    "simulation":      ["references/canonical_sources.yaml", "canon/02_canon_constraints.md"],
    "audit":           ["references/canonical_sources.yaml", "canon/02_canon_constraints.md"],
    "canon_check":     ["canon/00_philosophical_foundations.md", "canon/02_canon_constraints.md"],
    "editorial":       ["canon/editorial_ledger.yaml"],
    "patch":           ["canon/patch_register_active.yaml"],
    "compilation":     ["references/canonical_sources.yaml", "canon/patch_register_active.yaml"],
    "propose_mechanic":["references/canonical_sources.yaml", "canon/editorial_ledger_summary.yaml"],
    "design":          ["references/canonical_sources.yaml"],
}


# ── Hook 1: Bootstrap ─────────────────────────────────────────────────────────

def assert_bootstrap() -> str:
    """Confirm github_ops fetched from GitHub this session. Raises if not."""
    global _bootstrap_confirmed
    try:
        token = g.get_session_token()
        _bootstrap_confirmed = True
        print(f"[HOOK ✓] bootstrap — token: {token}")
        return token
    except RuntimeError:
        raise RuntimeError(
            "[HOOK VIOLATION] No session token — bootstrap incomplete.\n"
            "read_files_graphql() must be called before any work begins.\n"
            "Re-run the bootstrap block."
        )


# ── Hook 2: Task gate ─────────────────────────────────────────────────────────

def task_gate(task_type: str) -> None:
    """Confirm required files fetched for this task type. Raises if missing."""
    if not _bootstrap_confirmed:
        raise RuntimeError(
            f"[HOOK VIOLATION] task_gate('{task_type}') before assert_bootstrap()."
        )
    required = TASK_REQUIRED_FILES.get(task_type)
    if required is None:
        raise RuntimeError(
            f"[HOOK VIOLATION] Unknown task type '{task_type}'.\n"
            f"Valid: {sorted(TASK_REQUIRED_FILES)}"
        )
    missing = [p for p in required
               if p not in g._session_fetches or g._session_fetches[p] is None]
    if missing:
        raise RuntimeError(
            f"[HOOK VIOLATION] Task '{task_type}' — files not fetched:\n"
            + "\n".join(f"  {p}" for p in missing)
            + "\nFetch before starting. No exceptions."
        )
    _task_gates_passed.add(task_type)
    print(f"[HOOK ✓] task_gate('{task_type}')")


def task_gate_with_system(task_type: str, system: str, canonical_sources_content: str) -> None:
    """Extended task gate: also confirms canonical design doc fetched for system."""
    task_gate(task_type)
    import re as _re
    # Find canonical path for system in the YAML content
    pattern = _re.compile(
        rf'(?:^|\n)\s*{_re.escape(system)}:.*?\n(?:(?!\n\w)[\s\S])*?canonical:\s*([^\n]+)',
        _re.MULTILINE
    )
    m = pattern.search(canonical_sources_content)
    if not m:
        raise RuntimeError(
            f"[HOOK VIOLATION] System '{system}' not found in canonical_sources.yaml.\n"
            f"Cannot proceed — canonical doc path unknown."
        )
    canonical_path = m.group(1).strip()
    if canonical_path not in g._session_fetches or g._session_fetches[canonical_path] is None:
        raise RuntimeError(
            f"[HOOK VIOLATION] Canonical doc for '{system}' not fetched:\n"
            f"  Required: {canonical_path}\n"
            f"Fetch before starting."
        )
    print(f"[HOOK ✓] system gate '{system}' — {canonical_path}")


# ── Hook 3: Editorial gate ────────────────────────────────────────────────────

def editorial_gate(path: str, content: str) -> None:
    """
    Blocks commits to editorial paths without [EDITORIAL] or [PROVISIONAL] markers.
    Called automatically for every addition in pre_commit_gate.
    """
    if not any(path.startswith(p) for p in EDITORIAL_PATHS):
        return
    if len(content) < 200:
        return  # stub — exempt
    if not any(m in content for m in EDITORIAL_MARKERS):
        raise RuntimeError(
            f"[HOOK VIOLATION] Editorial path without flag:\n"
            f"  {path}\n"
            f"Add [EDITORIAL: ED-NNN — description] or [PROVISIONAL: ...] before committing.\n"
            f"User retains exclusive authority over: setting, worldbuilding, characters,\n"
            f"narrative, faction behaviour, ambiguous design intent."
        )
    print(f"[HOOK ✓] editorial_gate — {path}")


# ── Hook 4: Commit message ────────────────────────────────────────────────────

def commit_message_gate(message: str) -> None:
    """Raises if message doesn't match [scope] description format."""
    if not COMMIT_FORMAT.match(message):
        raise RuntimeError(
            f"[HOOK VIOLATION] Bad commit message: '{message}'\n"
            f"Required: '[scope] description — PP-NNN / ED-NNN if applicable'\n"
            f"Valid scopes: {sorted(VALID_SCOPES)}"
        )
    print(f"[HOOK ✓] commit_message_gate")


# ── Hook 5: Pre-commit gate ───────────────────────────────────────────────────

def pre_commit_gate(additions: list, deletions: list = None) -> None:
    """
    Hard gate before every commit. Checks:
    1. Editorial gate per path
    2. Size thresholds (via github_ops — defense in depth)
    3. Required co-files (design doc → canonical_sources, patch → register, sim → matrix)

    Tool runner (freshness_gate, broken_dependency_checker, patch_propagation_checker)
    is NOT run here — those tools run in CI against the full repo after push.
    Running them client-side from a container without the full repo is unreliable.
    CI is the authoritative gate for those checks.
    """
    if deletions is None:
        deletions = []

    errors = []
    paths_in_commit = {p for p, _ in additions} | set(deletions)

    # Editorial check per path
    for path, content in additions:
        try:
            editorial_gate(path, content)
        except RuntimeError as e:
            errors.append(str(e))

    # Size check
    for path, content in additions:
        tokens = len(content) // 4
        threshold = g.TOKEN_THRESHOLDS.get(path)
        if threshold and tokens > threshold:
            errors.append(
                f"SIZE: {path}: {tokens:,} tokens exceeds {threshold:,} limit.\n"
                f"  Archive old content before committing."
            )

    # Co-file: design doc → canonical_sources.yaml
    design_docs = [p for p, _ in additions
                   if re.match(r'designs/.+_v30\.md$', p) and 'infill' not in p]
    if design_docs and 'references/canonical_sources.yaml' not in paths_in_commit:
        errors.append(
            f"CO-FILE: design docs changed {design_docs} but\n"
            f"  references/canonical_sources.yaml not in commit.\n"
            f"  Include if source authority changed."
        )

    # Co-file: patch register write → propagation_map
    patch_writes = [p for p in paths_in_commit if 'patch_register' in p]
    if patch_writes and 'references/propagation_map.md' not in paths_in_commit:
        errors.append(
            f"CO-FILE: patch_register changed but propagation_map.md not included."
        )

    # Co-file: sim output → coverage_matrix
    sim_writes = [p for p in paths_in_commit
                  if p.startswith('tests/sim_') or p.startswith('tests/aud_')]
    if sim_writes and 'tests/coverage_matrix.md' not in paths_in_commit:
        errors.append(
            f"CO-FILE: simulation output added but tests/coverage_matrix.md not updated.\n"
            f"  Sim outputs: {sim_writes}"
        )

    if errors:
        raise RuntimeError(
            "[HOOK VIOLATION] pre_commit_gate FAILED:\n\n"
            + "\n\n".join(f"  [{i+1}] {e}" for i, e in enumerate(errors))
            + "\n\nFix before committing. CI will also check after push."
        )

    print(f"[HOOK ✓] pre_commit_gate ({len(additions)} additions, {len(deletions)} deletions)")


# ── Hook 6: Propose mechanic ──────────────────────────────────────────────────

def propose_mechanic_gate(system: str) -> None:
    """Call before any mechanic proposal. Raises if canonical_sources not fetched."""
    if 'references/canonical_sources.yaml' not in g._session_fetches:
        raise RuntimeError(
            f"[HOOK VIOLATION] propose_mechanic_gate('{system}'):\n"
            f"  canonical_sources.yaml not fetched.\n"
            f"  Cannot propose mechanics without knowing which doc is canonical."
        )
    print(f"[HOOK ✓] propose_mechanic_gate('{system}')")


# ── Hook 7: Context gate ──────────────────────────────────────────────────────

def context_gate() -> None:
    """Estimate session token usage. Hard stop at 90%, warn at 70%."""
    total = sum(len(c) for c in g._session_fetches.values() if c) // 4
    if total >= CONTEXT_HARD:
        raise RuntimeError(
            f"[HOOK VIOLATION] Context hard stop: ~{total:,} fetch tokens.\n"
            f"Run Session Close Protocol immediately. Do not start new work."
        )
    elif total >= CONTEXT_WARN:
        print(f"[HOOK ⚠] Context at ~{total:,} tokens (70% threshold). Close soon.")
    else:
        print(f"[HOOK ✓] context_gate: ~{total:,} fetch tokens")


# ── Hook 8: Memory contamination guard ───────────────────────────────────────

def memory_contamination_guard(path: str, content: str) -> None:
    """Verify content for path came from GitHub this session, not memory."""
    fetched = g._session_fetches.get(path)
    if fetched is None:
        raise RuntimeError(
            f"[HOOK VIOLATION] '{path}' not fetched this session.\n"
            f"Do not use content from memory or local copies."
        )
    if fetched != content:
        raise RuntimeError(
            f"[HOOK VIOLATION] '{path}' content differs from GitHub fetch.\n"
            f"Re-fetch after any commit that modifies this file."
        )
    print(f"[HOOK ✓] memory_contamination_guard — {path}")


# ── safe_commit: the only valid way to commit ─────────────────────────────────

def safe_commit(additions: list, deletions: list, message: str) -> str:
    """
    The ONLY valid path to atomic_commit(). Runs all gates in sequence.
    Replaces direct g.atomic_commit() calls everywhere except infrastructure.

    Sequence:
      1. commit_message_gate    — format check
      2. editorial_gate         — per-path (via pre_commit_gate)
      3. pre_commit_gate        — size + co-files
      4. _authorize_next_commit — single-use token
      5. g.atomic_commit        — actual commit
    """
    commit_message_gate(message)
    pre_commit_gate(additions, deletions or [])
    auth = g._authorize_next_commit()
    oid = g.atomic_commit(
        additions=additions,
        deletions=deletions or [],
        message=message,
        _auth=auth,
    )
    print(f"[HOOK ✓] safe_commit — {oid}")
    return oid
