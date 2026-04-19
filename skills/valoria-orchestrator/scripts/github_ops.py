"""
github_ops.py — Valoria GitHub operations
Supports two repos: ttrpg (design) and valoria-game (Godot implementation).

Usage:
    import github_ops as g

    # Default: operates on ttrpg
    files = g.read_files_graphql(['session_log_current.md'])

    # Switch to valoria-game for Godot work
    g.use_repo('valoria-game')
    files = g.read_files_graphql(['autoload/Meta.gd'])
    g.use_repo('ttrpg')  # switch back

    # Or: one-shot with repo= parameter
    files = g.read_files_graphql(['autoload/Meta.gd'], repo='valoria-game')
    oid   = g.atomic_commit(additions, deletions, message, repo='valoria-game', _auth=auth)

REPO RULES:
  ttrpg        — design docs, params, registers, skills. Full hook + CI enforcement.
  valoria-game — Godot GDScript. No register health checks (different file types).
                 Commit message format still enforced. Editorial gate not enforced
                 (no worldbuilding in code). Size thresholds do not apply.
"""

import os, sys, json, base64, re, hashlib, secrets, inspect, urllib.request, urllib.error

REPO_OWNER = "jordanelias"
BRANCH     = "main"
API_BASE   = "https://api.github.com"
GRAPHQL_URL = "https://api.github.com/graphql"

# Valid repos and their characteristics
REPOS = {
    'ttrpg': {
        'name': 'ttrpg',
        'enforce_health': True,    # register size checks apply
        'enforce_editorial': True, # editorial path checks apply
        'description': 'Design repo — full enforcement',
    },
    'valoria-game': {
        'name': 'valoria-game',
        'enforce_health': False,   # no register thresholds for GDScript
        'enforce_editorial': False,# no editorial gates for code files
        'description': 'Godot implementation — commit format enforced only',
    },
}

# ── Token thresholds (ttrpg only) ─────────────────────────────────────────────
TOKEN_THRESHOLDS = {
    "session_log_current.md":                  2_000,
    "canon/editorial_ledger.yaml":             2_000,
    "canon/editorial_ledger_summary.yaml":     1_000,
    "references/file_index_summary.md":        1_000,
    "references/canonical_sources.yaml":       5_000,
    "skills/valoria-orchestrator/SKILL.md":    8_000,
    "canon/patch_register_active.yaml":       15_000,
    "tests/coverage_matrix.md":               5_000,
    "references/arc_register.md":            20_000,
    "references/propagation_map.md":         15_000,
    "references/design_registry.yaml":        8_000,
}
ARCHIVE_WARN_THRESHOLD = 100_000

# ── Session state (per-repo) ───────────────────────────────────────────────────
_active_repo:      str  = 'ttrpg'
_session_fetches:  dict = {}   # path -> content (merged across repos; use _repo_key)
_session_token:    str  = None
_health_checked:   bool = False
_commit_auth:      str  = None

# ── Disk cache (persists across bash_tool subprocesses) ──────────────────────
_CACHE_PATH = '/home/claude/.valoria_cache.json'

def _save_cache() -> None:
    """Write _session_fetches to disk. Called after reads and commits."""
    try:
        with open(_CACHE_PATH, 'w') as f:
            json.dump({
                'fetches': {k: v for k, v in _session_fetches.items() if v is not None},
                'token': _session_token,
            }, f)
    except Exception:
        pass  # non-fatal — cache is optimization, not requirement

def _load_cache() -> bool:
    """Restore _session_fetches from disk. Returns True if cache loaded."""
    global _session_fetches, _session_token, _health_checked
    try:
        with open(_CACHE_PATH) as f:
            data = json.load(f)
        _session_fetches = data.get('fetches', {})
        _session_token = data.get('token')
        _health_checked = True  # health was checked when cache was written
        return bool(_session_fetches)
    except (FileNotFoundError, json.JSONDecodeError):
        return False


def _repo_key(path: str, repo: str) -> str:
    """Namespace fetch keys by repo to avoid collisions."""
    return f"{repo}:{path}"

# ── Cache lifecycle management ────────────────────────────────────────────────

# Session-permanent keys: needed for co-file compliance, context_gate, bootstrap.
# These survive eviction calls unless explicitly targeted.
SESSION_PERMANENT_PATTERNS = (
    'session_log_current.md',
    'editorial_ledger_summary.yaml',
    'file_index_summary.md',
    'canonical_sources.yaml',
    'patch_register_active.yaml',
    'editorial_ledger.yaml',
    'propagation_map.md',
    'coverage_matrix.md',
)

def cache_evict(*paths: str, repo: str = None) -> int:
    """Remove specific paths from session cache. Returns count evicted.
    
    Use after a task completes and its fetched docs are no longer needed.
    Example: g.cache_evict('designs/scene/combat_v30.md', 'designs/threadwork/threadwork_v30.md')
    """
    repo = repo or _active_repo
    evicted = 0
    for path in paths:
        key = _repo_key(path, repo)
        if key in _session_fetches:
            del _session_fetches[key]
            evicted += 1
    if evicted:
        _save_cache()
    return evicted


def cache_evict_pattern(*prefixes: str, repo: str = None, protect_permanent: bool = True) -> int:
    """Evict all cached entries whose path starts with any given prefix.
    
    By default protects session-permanent files. Set protect_permanent=False
    to evict everything matching (use with caution).
    
    Example: g.cache_evict_pattern('designs/', 'tests/')  # evict all design/test docs
    """
    repo = repo or _active_repo
    to_evict = []
    for key in list(_session_fetches.keys()):
        # Key format: "repo:path"
        if ':' in key:
            key_repo, key_path = key.split(':', 1)
        else:
            key_path = key
            key_repo = _active_repo
        
        if repo and key_repo != repo:
            continue
        
        if any(key_path.startswith(p) for p in prefixes):
            if protect_permanent and any(perm in key_path for perm in SESSION_PERMANENT_PATTERNS):
                continue
            to_evict.append(key)
    
    for key in to_evict:
        del _session_fetches[key]
    
    if to_evict:
        _save_cache()
    return len(to_evict)


def cache_evict_committed(additions: list, deletions: list = None, repo: str = None) -> int:
    """Evict all entries that were just committed (additions + deletions).
    
    Called automatically by atomic_commit after successful commit.
    Committed content is on GitHub — no reason to keep it in session cache.
    Session-permanent files are re-fetched on next access if needed.
    """
    repo = repo or _active_repo
    evicted = 0
    for path, _ in (additions or []):
        key = _repo_key(path, repo)
        if key in _session_fetches:
            # Keep session-permanent files — they're needed for co-file checks
            if any(perm in path for perm in SESSION_PERMANENT_PATTERNS):
                # Update the cached value to the committed content instead of evicting
                _session_fetches[key] = _  # already the latest
                continue
            del _session_fetches[key]
            evicted += 1
    for path in (deletions or []):
        key = _repo_key(path, repo)
        if key in _session_fetches:
            del _session_fetches[key]
            evicted += 1
    if evicted:
        _save_cache()
    return evicted


def cache_stats() -> dict:
    """Return cache statistics for diagnostics."""
    total_chars = sum(len(v) for v in _session_fetches.values() if v)
    permanent = sum(1 for k in _session_fetches 
                    if any(p in k for p in SESSION_PERMANENT_PATTERNS))
    return {
        'entries': len(_session_fetches),
        'permanent': permanent,
        'transient': len(_session_fetches) - permanent,
        'total_chars': total_chars,
        'est_tokens': total_chars // 4,
    }


def use_repo(repo: str) -> None:
    """Switch the default active repo. Use 'ttrpg' or 'valoria-game'."""
    global _active_repo
    if repo not in REPOS:
        raise RuntimeError(
            f"Unknown repo '{repo}'. Valid: {list(REPOS.keys())}"
        )
    _active_repo = repo
    print(f"[g] Active repo: {repo} ({REPOS[repo]['description']})")


def active_repo() -> str:
    return _active_repo


# ── Session token ─────────────────────────────────────────────────────────────

def _refresh_token() -> str:
    global _session_token
    blob = json.dumps(
        {k: c for k, c in sorted(_session_fetches.items()) if c},
        sort_keys=True
    )
    _session_token = hashlib.sha256(blob.encode()).hexdigest()[:16]
    return _session_token


def get_session_token() -> str:
    if not _session_token:
        raise RuntimeError(
            "No session token — read_files_graphql() has not been called this session."
        )
    return _session_token


def assert_fetched(*paths, repo: str = None) -> str:
    repo = repo or _active_repo
    missing = [p for p in paths
               if _repo_key(p, repo) not in _session_fetches
               or _session_fetches[_repo_key(p, repo)] is None]
    if missing:
        raise RuntimeError(
            f"[{repo}] Required paths not fetched: {missing}\n"
            f"Call read_files_graphql({missing}, repo='{repo}') before proceeding."
        )
    return get_session_token()


# ── Commit authorization ──────────────────────────────────────────────────────

def _authorize_next_commit() -> str:
    """
    Single-use commit authorization. Called by valoria_hooks.safe_commit()
    and trusted internal callers (safe_session_close, append_to_register).

    Caller verification via inspect.stack():
    - valoria_hooks.safe_commit()
    - valoria_hooks.assert_bootstrap() (compliance auto-fix)
    - valoria_hooks.write_checkpoint() / close_checkpoint() (session checkpoints)
    - github_ops.safe_session_close()
    - github_ops.append_to_register()
    - Direct bash_tool calls (<stdin>, /tmp, <string>) for infrastructure work
    """
    frame = inspect.stack()[1]
    caller_fn, caller_file = frame.function, frame.filename
    approved = (
        (caller_fn == 'safe_commit' and 'valoria_hooks' in caller_file) or
        (caller_fn == 'assert_bootstrap' and 'valoria_hooks' in caller_file) or
        (caller_fn in ('write_checkpoint', 'close_checkpoint') and 'valoria_hooks' in caller_file) or
        (caller_fn in ('safe_session_close', 'append_to_register') and 'github_ops' in caller_file) or
        ('<stdin>' in caller_file or caller_file.startswith('/tmp') or caller_file == '<string>')
    )
    if not approved:
        raise RuntimeError(
            f"[AUTH VIOLATION] _authorize_next_commit() called from unapproved context:\n"
            f"  {caller_fn}() in {caller_file}\n"
            f"Use h.safe_commit() or call directly from a bash_tool block."
        )
    global _commit_auth
    _commit_auth = secrets.token_hex(8)
    return _commit_auth


# ── Auth / HTTP ───────────────────────────────────────────────────────────────

def _get_pat() -> str:
    pat = os.environ.get("GITHUB_PAT", "")
    if not pat:
        try:
            pat = open(os.path.expanduser('/home/claude/.valoria_pat')).read().strip()
            os.environ["GITHUB_PAT"] = pat  # cache in env for this process
        except FileNotFoundError:
            raise RuntimeError(
                "GITHUB_PAT not set and /home/claude/.valoria_pat not found.\n"
                "Re-run bootstrap to write the PAT file."
            )
    return pat


def _headers() -> dict:
    return {
        "Authorization": f"token {_get_pat()}",
        "Content-Type":  "application/json",
        "Accept":        "application/vnd.github.v3+json",
    }


def _get(path: str, repo: str) -> dict:
    url = f"{API_BASE}/repos/{REPO_OWNER}/{repo}/contents/{path}"
    req = urllib.request.Request(url, headers=_headers())
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())


def _graphql(query: str, variables: dict = None) -> dict:
    payload = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request(GRAPHQL_URL, data=payload, headers=_headers())
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())


# ── Register health (ttrpg only) ──────────────────────────────────────────────

def check_register_health(fetched_with_keys: dict) -> None:
    """
    Hard stop if any fetched ttrpg file exceeds TOKEN_THRESHOLDS.
    Skipped entirely for valoria-game files.
    """
    global _health_checked
    violations = []
    print("\n## REGISTER HEALTH CHECK")
    for key, content in fetched_with_keys.items():
        if content is None or not key.startswith('ttrpg:'):
            continue
        path = key[len('ttrpg:'):]
        threshold = TOKEN_THRESHOLDS.get(path)
        if threshold is None:
            continue
        tokens = len(content) // 4
        warn_threshold = int(threshold * 0.8)
        if tokens > threshold:
            status = "✗ OVER"
            violations.append(f"  {path}: {tokens:,} tokens exceeds {threshold:,} limit.")
        elif tokens > warn_threshold:
            status = "⚠ WARN"
        else:
            status = "✓"
        print(f"  {status}  {path}: {tokens:,} / {threshold:,} tokens")

    if violations:
        raise RuntimeError(
            "\n[HARD STOP] Register health FAILED:\n" + "\n".join(violations) +
            "\n\nArchive content before proceeding."
        )
    _health_checked = True
    print("  Register health: ALL PASS\n")


# ── Core reads ────────────────────────────────────────────────────────────────

def read_files_graphql(paths: list, repo: str = None,
                       skip_health_check: bool = False,
                       force_full: bool = False) -> dict:
    """
    Batch-read files from a repo via GraphQL.

    repo: 'ttrpg' (default) or 'valoria-game'
    Returns: dict {path -> content_str | None}
    """
    global _health_checked
    repo = repo or _active_repo
    if repo not in REPOS:
        raise RuntimeError(f"Unknown repo '{repo}'")

    if not paths:
        return {}

    # Auto-skeleton routing for design docs (unless force_full)
    if not force_full and REPOS[repo].get('enforce_health'):
        paths = _route_to_skeletons(paths, repo)

    aliases = {f"f{i}": p for i, p in enumerate(paths)}
    fields = "\n".join(
        f'  {alias}: object(expression: "main:{path}") {{ ... on Blob {{ text }} }}'
        for alias, path in aliases.items()
    )
    query = f"""
    query($owner: String!, $name: String!) {{
      repository(owner: $owner, name: $name) {{
{fields}
      }}
    }}
    """
    result = _graphql(query, {"owner": REPO_OWNER, "name": repo})
    repo_data = result["data"]["repository"]

    output = {}
    for alias, path in aliases.items():
        content = repo_data[alias]["text"] if repo_data[alias] else None
        key = _repo_key(path, repo)
        _session_fetches[key] = content
        output[path] = content

        # Record read depth. If force_full OR path is not a design doc
        # (designs/.../*.md but not _skeleton.md), it's a full read.
        # Design docs that got routed to their _skeleton.md variant are
        # tracked by read_skeleton() when that fires separately.
        if content is not None:
            is_design_doc = (
                path.startswith('designs/')
                and path.endswith('.md')
                and not path.endswith('_skeleton.md')
            )
            if force_full or not is_design_doc:
                _full_reads.add(key)

    _refresh_token()
    _save_cache()

    # Health check: only for ttrpg, only on first call with threshold-governed files
    if not _health_checked and not skip_health_check and REPOS[repo]['enforce_health']:
        governed = {_repo_key(p, repo): c
                    for p, c in output.items()
                    if p in TOKEN_THRESHOLDS and c}
        if governed:
            check_register_health(governed)

    return output


def read_file(path: str, repo: str = None) -> str:
    repo = repo or _active_repo
    d = _get(path, repo)
    content = base64.b64decode(d["content"]).decode("utf-8")
    _session_fetches[_repo_key(path, repo)] = content
    _refresh_token()
    return content


# ── Directory helpers ─────────────────────────────────────────────────────────

def file_exists(path: str, repo: str = None) -> bool:
    repo = repo or _active_repo
    try:
        _get(path, repo)
        return True
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return False
        raise


def file_size(path: str, repo: str = None) -> int:
    repo = repo or _active_repo
    try:
        return _get(path, repo).get("size", 0)
    except urllib.error.HTTPError:
        return -1


def list_directory(path: str, repo: str = None) -> list:
    repo = repo or _active_repo
    items = _get(path, repo)
    return [item["name"] for item in items if isinstance(item, dict)]


# ── Write ─────────────────────────────────────────────────────────────────────

def get_head_oid(repo: str = None) -> str:
    repo = repo or _active_repo
    q = """
    query($owner: String!, $name: String!, $branch: String!) {
      repository(owner: $owner, name: $name) {
        ref(qualifiedName: $branch) { target { oid } }
      }
    }
    """
    result = _graphql(q, {"owner": REPO_OWNER, "name": repo, "branch": BRANCH})
    return result["data"]["repository"]["ref"]["target"]["oid"]


def atomic_commit(
    additions: list,
    deletions: list,
    message:   str,
    repo:      str  = None,
    expected_oid: str = None,
    _auth:     str  = None,
) -> str:
    """
    Atomic commit to ttrpg or valoria-game.

    REQUIRES authorization token from _authorize_next_commit().
    Use h.safe_commit(additions, deletions, message, repo='valoria-game') instead.
    """
    global _commit_auth, _session_token
    repo = repo or _active_repo

    if _auth != _commit_auth or _commit_auth is None:
        raise RuntimeError(
            f"[COMMIT BLOCKED] atomic_commit() to '{repo}' called without authorization.\n"
            f"Use h.safe_commit(additions, deletions, message, repo='{repo}')."
        )
    _commit_auth = None

    # Size check (ttrpg only)
    if REPOS[repo]['enforce_health']:
        for path, content in additions:
            tokens = len(content) // 4
            threshold = TOKEN_THRESHOLDS.get(path)
            if threshold and tokens > threshold:
                raise RuntimeError(
                    f"[COMMIT BLOCKED] {path}: {tokens:,} tokens exceeds {threshold:,} limit."
                )

    if expected_oid is None:
        expected_oid = get_head_oid(repo)

    file_additions = [
        {"path": p, "contents": base64.b64encode(c.encode("utf-8")).decode("ascii")}
        for p, c in additions
    ]
    file_deletions = [{"path": p} for p in (deletions or [])]

    mutation = """
    mutation($input: CreateCommitOnBranchInput!) {
      createCommitOnBranch(input: $input) {
        commit { oid url }
      }
    }
    """
    variables = {
        "input": {
            "branch": {
                "repositoryNameWithOwner": f"{REPO_OWNER}/{repo}",
                "branchName": BRANCH,
            },
            "message": {"headline": message},
            "fileChanges": {
                "additions": file_additions,
                "deletions": file_deletions,
            },
            "expectedHeadOid": expected_oid,
        }
    }

    try:
        result = _graphql(mutation, variables)
        if "errors" in result:
            errs = result["errors"]
            if any("expectedHeadOid" in str(e) for e in errs):
                variables["input"]["expectedHeadOid"] = get_head_oid(repo)
                result = _graphql(mutation, variables)
                if "errors" in result:
                    raise RuntimeError(f"Commit failed after OID retry: {result['errors']}")
            else:
                raise RuntimeError(f"Commit failed: {errs}")

        oid = result["data"]["createCommitOnBranch"]["commit"]["oid"]

        # Evict committed content — it's on GitHub now.
        # Session-permanent files get their cached value updated instead of evicted.
        for path, content in additions:
            key = _repo_key(path, repo)
            if any(perm in path for perm in SESSION_PERMANENT_PATTERNS):
                _session_fetches[key] = content  # update to committed version
            else:
                _session_fetches.pop(key, None)
        for path in (deletions or []):
            _session_fetches.pop(_repo_key(path, repo), None)
        if _session_fetches:
            _refresh_token()
        else:
            _session_token = None
        _save_cache()

        return oid

    except Exception as e:
        raise RuntimeError(f"Commit error [{repo}]: {e}")


def append_to_register(path: str, new_entries: str,
                       commit_message: str, repo: str = None) -> str:
    """Safe register append with size check. ttrpg only."""
    repo = repo or 'ttrpg'
    fresh = read_files_graphql([path], repo=repo, skip_health_check=True)
    current = fresh.get(path) or ""
    combined = current + new_entries
    tokens = len(combined) // 4
    threshold = TOKEN_THRESHOLDS.get(path)
    if threshold and tokens > threshold:
        raise RuntimeError(
            f"[CHUNK REQUIRED] {path} would reach {tokens:,} tokens (limit {threshold:,})."
        )
    auth = _authorize_next_commit()
    return atomic_commit(
        additions=[(path, combined)], deletions=[],
        message=commit_message, repo=repo, _auth=auth,
    )


# ── Session close (ttrpg only) ────────────────────────────────────────────────

def _extract_session_id(content: str) -> str:
    m = re.search(r'session_id:\s*(.+)', content)
    return m.group(1).strip() if m else ""


def safe_session_close(
    new_session_log: str,
    bootstrap_session_log: str,
    extra_additions: list = None,
    message: str = "[infrastructure] Session close",
) -> str:
    tokens = len(new_session_log) // 4
    limit  = TOKEN_THRESHOLDS.get("session_log_current.md", 2_000)
    if tokens > limit:
        raise RuntimeError(
            f"[COMMIT BLOCKED] session_log_current.md: {tokens:,} tokens (limit {limit:,}).\n"
            f"Trim to resumption block only."
        )

    # Validate required YAML fields are present
    REQUIRED_LOG_FIELDS = ['session_id', 'session_close', 'phase', 'status',
                           'last_stage', 'next_action', 'blockers']
    missing = [fld for fld in REQUIRED_LOG_FIELDS if fld not in new_session_log]
    if missing:
        raise RuntimeError(
            f"[COMMIT BLOCKED] session_log_current.md missing required fields: {missing}\n"
            f"Required: {REQUIRED_LOG_FIELDS}\n"
            f"Session log must be resumption-block YAML only — no prose, no task summaries."
        )

    # Reject narrative content (## headers = prose summary, not resumption block)
    import re as _re
    if _re.search(r'^## ', new_session_log, _re.MULTILINE):
        raise RuntimeError(
            "[COMMIT BLOCKED] session_log_current.md contains prose headers (## ...).\n"
            "Protocol: resumption block only — pure YAML, no summaries, no task lists.\n"
            "Move narrative content to the archives/session/session_log_archive_part_7.md entry instead."
        )

    fresh = read_files_graphql(
        ["session_log_current.md", "archives/session/session_log_archive_part_7.md"],
        repo='ttrpg', skip_health_check=True
    )
    live_current = fresh.get("session_log_current.md", "") or ""
    live_archive  = fresh.get("archives/session/session_log_archive_part_7.md",  "") or ""

    archive_tokens = len(live_archive) // 4
    if archive_tokens > ARCHIVE_WARN_THRESHOLD:
        print(f"[ARCHIVE WARNING] archives/session/session_log_archive_part_7.md: {archive_tokens:,} tokens. Year-split soon.")

    live_id      = _extract_session_id(live_current)
    new_id       = _extract_session_id(new_session_log)
    bootstrap_id = _extract_session_id(bootstrap_session_log)

    if live_id and new_id and live_id == new_id:
        raise RuntimeError(f"DUPLICATE CLOSE BLOCKED: '{live_id}' already closed.")

    if live_current.strip() != bootstrap_session_log.strip():
        print(f"[safe_session_close] Intervening session: '{bootstrap_id}'→'{live_id}'. Archiving.")

    additions = [
        ("session_log_current.md", new_session_log),
        ("archives/session/session_log_archive_part_7.md", live_archive + "\n---\n\n" + live_current),
    ]
    if extra_additions:
        additions.extend(extra_additions)

    auth = _authorize_next_commit()
    return atomic_commit(additions=additions, deletions=[], message=message,
                         repo='ttrpg', _auth=auth)




# ── quick_bootstrap: one-call preamble for all subsequent bash blocks ─────────

def quick_bootstrap(extra_paths: list = None) -> tuple:
    """
    Standard preamble for every bash_tool block after the initial bootstrap.

    Uses disk cache to avoid re-fetching files already read this session.
    Only fetches from GitHub when: (a) cache miss, or (b) extra_paths not cached.
    atomic_commit() invalidates cache for committed paths, ensuring freshness.

    Returns: (g, h, files, token) — ready to use immediately.

    Usage in any bash_tool block:
        import sys; sys.path.insert(0, '/home/claude')
        from github_ops import quick_bootstrap
        g, h, files, token = quick_bootstrap(['canon/patch_register_active.yaml'])
        h.task_gate('patch')
        # ... do work ...
    """
    import importlib, valoria_hooks as _h_mod
    importlib.reload(_h_mod)  # reset process-scoped state (bootstrap_confirmed etc.)

    # Restore session state from disk cache (written by previous bash_tool blocks)
    cache_hit = _load_cache()

    session_paths = [
        'session_log_current.md',
        'canon/editorial_ledger_summary.yaml',
        'references/file_index_summary.md',
        'references/canonical_sources.yaml',
    ]
    all_needed = session_paths + [p for p in (extra_paths or []) if p not in session_paths]

    # Only fetch paths not already in cache
    to_fetch = [p for p in all_needed
                if _repo_key(p, 'ttrpg') not in _session_fetches
                or _session_fetches[_repo_key(p, 'ttrpg')] is None]

    if to_fetch:
        read_files_graphql(to_fetch)  # populates _session_fetches + saves cache

    # Build return dict from cache
    files = {}
    for p in all_needed:
        key = _repo_key(p, 'ttrpg')
        files[p] = _session_fetches.get(key)

    import github_ops as _g_mod
    token = _h_mod.assert_bootstrap()
    _h_mod.context_gate()
    return _g_mod, _h_mod, files, token



# ── Smart fetch (skeleton-first) ────────────────────────────────────────────

def fetch_system(system: str, canonical_sources_content: str,
                 depth: str = 'skeleton', repo: str = None) -> dict:
    """
    Fetch system files using depth-aware routing.

    depth:
      'skeleton'    — canonical doc only (default, sufficient for most work)
      'full'        — canonical doc + infill (for deep editorial or prose review)
      'params_only' — params file only (for simulation, value checks)
      'all'         — canonical + infill + params

    Returns dict of {path: content} for fetched files.
    """
    import yaml
    repo = repo or _active_repo

    try:
        sources = yaml.safe_load(canonical_sources_content)
    except Exception as e:
        raise RuntimeError(f"Cannot parse canonical_sources: {e}")

    systems = sources.get('systems', {})
    entry = systems.get(system, {})
    status = entry.get('status', 'active')
    if status == 'deprecated':
        print(f"[SKIP] System '{system}' is deprecated — no fetch needed.")
        return {}
    if status == 'design_debt':
        print(f"[WARN] System '{system}' has no proper design doc (canonical points to compilation).")

    if not entry:
        raise RuntimeError(
            f"System '{system}' not in canonical_sources. "
            f"Available: {sorted(systems.keys())}"
        )

    canonical = (entry.get('canonical') or entry.get('canonical_bg') or
                 entry.get('design_doc') or entry.get('canonical_ttrpg'))
    params = entry.get('params')

    paths = []
    if depth in ('skeleton', 'full', 'all'):
        if canonical:
            paths.append(canonical)
    if depth in ('full', 'all'):
        infill = canonical.replace('_v30.md', '_v30_infill.md') if canonical else None
        if infill and infill != canonical:
            paths.append(infill)
    if depth in ('params_only', 'all'):
        if params:
            paths.append(params)

    if not paths:
        raise RuntimeError(f"No fetchable paths for '{system}' at depth '{depth}'")

    return read_files_graphql(paths, repo=repo, skip_health_check=True)


# ── Skeleton routing ─────────────────────────────────────────────────────────

_skeleton_route_cache: dict = {}  # path -> skeleton_path or None

def _route_to_skeletons(paths: list, repo: str) -> list:
    """
    For any design doc path that has a committed _skeleton.md,
    substitute the skeleton path unless force_full=True.
    Caches mapping in session state.
    """
    routed = []
    for p in paths:
        if not p.startswith('designs/') or p.endswith('_skeleton.md') or p.endswith('_infill.md'):
            routed.append(p)
            continue
        cache_key = _repo_key(p, repo)
        if cache_key in _skeleton_route_cache:
            skel = _skeleton_route_cache[cache_key]
            routed.append(skel if skel else p)
        else:
            # Check if skeleton exists (one API call — cached after first check)
            skel_path = p[:-3] + '_skeleton.md' if p.endswith('.md') else p + '_skeleton.md'
            if file_exists(skel_path, repo):
                _skeleton_route_cache[cache_key] = skel_path
                routed.append(skel_path)
                # Record that the ORIGINAL design doc path was skeleton-routed.
                # This lets read_depth(original_path) return 'skeleton' even
                # though the fetch cache holds content under the skeleton path.
                _skeleton_reads[cache_key] = True
                print(f"[SKELETON ROUTE] {p} → {skel_path}")
            else:
                _skeleton_route_cache[cache_key] = None
                routed.append(p)
    return routed


# ── fetch_for_task: single-call task setup ───────────────────────────────────

def fetch_for_task(task_type: str, system: str = None) -> dict:
    """
    Single call to load everything a task needs, routed optimally.
    - Loads task-required files from TASK_REQUIRED_FILES
    - If system provided, loads skeleton + params (via fetch_system)
    - Uses skeleton routing by default
    - Returns {path: content} ready for work
    """
    import valoria_hooks as h
    h.task_gate(task_type)

    paths = h.TASK_REQUIRED_FILES.get(task_type, []).copy()
    files = read_files_graphql(paths, skip_health_check=True)

    if system:
        cs = files.get('references/canonical_sources.yaml', '')
        if not cs:
            cs_fetch = read_files_graphql(
                ['references/canonical_sources.yaml'], skip_health_check=True
            )
            cs = cs_fetch.get('references/canonical_sources.yaml', '')
            files.update(cs_fetch)
        system_files = fetch_system(system, cs, depth='skeleton')
        files.update(system_files)

    return files


# ── CLI smoke test ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("ttrpg HEAD:", get_head_oid('ttrpg'))
    print("valoria-game HEAD:", get_head_oid('valoria-game'))
    files = read_files_graphql(["session_log_current.md"], repo='ttrpg')
    print("ttrpg session token:", get_session_token())
    files2 = read_files_graphql(["README.md"], repo='valoria-game',
                                 skip_health_check=True)
    print("valoria-game README:", len((files2.get('README.md') or '').splitlines()), "lines")
    print("Smoke test passed.")


# ── Heading-gated reads (skeleton-first audit pattern) ─────────────────────

import re as _re_mod

def read_skeleton(path: str, repo: str = None) -> list:
    """
    Fetch a file and return its heading structure without body content.
    
    Returns list of dicts:
      [{'line': int, 'level': int, 'text': str, 'idx': int}, ...]
    
    Also caches the full content internally (avoids double-fetch on infill).
    Prints skeleton to stdout for Claude's context.
    """
    repo = repo or _active_repo
    key = _repo_key(path, repo)
    
    # Use cached content if available. If the path was skeleton-routed on a
    # prior fetch, the content lives under the routed _skeleton.md key — not
    # under the original path's key.
    content = _session_fetches.get(key)
    if content is None:
        # Check if this path has been skeleton-routed this session
        routed_cached = _skeleton_route_cache.get(key)
        if routed_cached:
            content = _session_fetches.get(_repo_key(routed_cached, repo))
        if content is None:
            fetched = read_files_graphql([path], repo=repo, skip_health_check=True)
            # Fetched output may be under routed path; check both
            content = fetched.get(path)
            if content is None:
                # Try routed path
                for k, v in fetched.items():
                    if v is not None:
                        content = v
                        break
            if content is None:
                raise RuntimeError(f"[SKELETON] File not found: {path} in {repo}")
    
    lines = content.splitlines()
    headings = []
    for i, line in enumerate(lines):
        m = _re_mod.match(r'^(#{1,6})\s+(.+)', line)
        if m:
            headings.append({
                'line': i + 1,
                'level': len(m.group(1)),
                'text': m.group(2).strip(),
                'idx': len(headings),
            })
    
    # Track that this path has been skeletonized
    _skeleton_reads[_repo_key(path, repo)] = True
    
    # Print compact skeleton
    total_lines = len(lines)
    total_tokens = total_lines * 10 // 4  # rough estimate
    print(f"\n[SKELETON] {path} — {total_lines} lines, ~{len(content)//4} tokens, {len(headings)} headings")
    for h in headings:
        indent = "  " * (h['level'] - 1)
        print(f"  {h['idx']:>3}  L{h['line']:<5} {indent}{h['text']}")
    
    return headings


def read_sections(path: str, heading_indices: list, repo: str = None) -> str:
    """
    Return content under specified headings only.
    
    heading_indices: list of idx values from read_skeleton() output.
    Returns concatenated section content (heading + body until next same-or-higher heading).
    """
    repo = repo or _active_repo
    key = _repo_key(path, repo)
    
    content = _session_fetches.get(key)
    if content is None:
        # Check skeleton-route cache — content may live under routed path
        routed = _skeleton_route_cache.get(key)
        if routed:
            content = _session_fetches.get(_repo_key(routed, repo))
            if content is not None:
                # Update key so section tracking below records against original path
                # (intentional: sim_gate uses the original path for depth lookups)
                pass
    if content is None:
        raise RuntimeError(f"[SECTIONS] File not fetched: {path}. Call read_skeleton() first.")
    
    lines = content.splitlines()
    
    # Rebuild heading map
    headings = []
    for i, line in enumerate(lines):
        m = _re_mod.match(r'^(#{1,6})\s+(.+)', line)
        if m:
            headings.append({'line': i + 1, 'level': len(m.group(1)), 'idx': len(headings)})
    
    if not headings:
        return content  # no headings = return all
    
    # Build heading index → (start_line, end_line) map
    sections = {}
    for i, h in enumerate(headings):
        start = h['line'] - 1  # 0-indexed
        # End at next heading of same or higher level, or EOF
        end = len(lines)
        for j in range(i + 1, len(headings)):
            if headings[j]['level'] <= h['level']:
                end = headings[j]['line'] - 1
                break
        sections[h['idx']] = (start, end)
    
    # Extract requested sections
    result_parts = []
    for idx in sorted(heading_indices):
        if idx not in sections:
            print(f"[SECTIONS] Warning: heading index {idx} not found in {path}")
            continue
        start, end = sections[idx]
        result_parts.append("\n".join(lines[start:end]))
    
    extracted = "\n\n".join(result_parts)
    print(f"[SECTIONS] {path}: extracted {len(heading_indices)} sections, ~{len(extracted)//4} tokens (full file: ~{len(content)//4} tokens)")

    # Track section reads. If all headings have been read via sections,
    # promote to full read.
    if key not in _section_reads:
        _section_reads[key] = set()
    # Only count indices that actually existed in the file
    valid_indices = {idx for idx in heading_indices if idx in sections}
    _section_reads[key].update(valid_indices)
    if len(_section_reads[key]) >= len(headings):
        _full_reads.add(key)

    return extracted

# Skeleton tracking state
_skeleton_reads: dict = {}

# Read-depth tracking state
_section_reads: dict = {}  # repo_key -> set of heading indices read via read_sections()
_full_reads: set = set()   # repo_keys that have been fully read

def was_skeletonized(path: str, repo: str = None) -> bool:
    """Check if a path went through read_skeleton() this session."""
    repo = repo or _active_repo
    return _skeleton_reads.get(_repo_key(path, repo), False)


def read_depth(path: str, repo: str = None) -> str:
    """
    Return read depth for a path this session:
      'full'     — full content fetched (non-design doc or force_full=True or all sections read)
      'sections' — partial read via read_sections() (subset of headings)
      'skeleton' — only the skeleton was fetched (design doc auto-route)
      'none'     — not fetched this session
    """
    repo = repo or _active_repo
    key = _repo_key(path, repo)

    if key in _full_reads:
        return 'full'
    if key in _section_reads and _section_reads[key]:
        return 'sections'
    if key in _skeleton_reads and _skeleton_reads[key]:
        return 'skeleton'
    if key in _session_fetches and _session_fetches[key] is not None:
        # Content present, no tracking — assume full for non-design docs.
        # Design docs always route through skeleton or sections tracking.
        _full_reads.add(key)
        return 'full'
    return 'none'


def read_depth_report(paths: list, repo: str = None) -> dict:
    """Return {path: depth} for a list of paths. Uses read_depth()."""
    repo = repo or _active_repo
    return {p: read_depth(p, repo) for p in paths}


def sections_read(path: str, repo: str = None) -> set:
    """Return set of heading indices read via read_sections() for path."""
    repo = repo or _active_repo
    key = _repo_key(path, repo)
    return set(_section_reads.get(key, set()))


def verify_reads_for_task(required_paths: list, repo: str = None,
                          require_depth: str = 'full') -> list:
    """
    Cross-reference required_paths against what was read this session.

    require_depth:
      'full'     — require full read (default for sim)
      'sections' — sections or full count
      'any'      — any depth including skeleton counts

    Returns list of (path, depth) for paths that fail the requirement.
    Empty list = all requirements met.
    """
    if require_depth not in ('full', 'sections', 'any'):
        raise ValueError(f"require_depth must be 'full', 'sections', or 'any'; got '{require_depth}'")
    failures = []
    for path in required_paths:
        depth = read_depth(path, repo)
        if require_depth == 'full':
            if depth != 'full':
                failures.append((path, depth))
        elif require_depth == 'sections':
            if depth not in ('full', 'sections'):
                failures.append((path, depth))
        else:  # 'any'
            if depth == 'none':
                failures.append((path, depth))
    return failures
