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
    "canon/patch_register_active.yaml":       20_000,
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

def _repo_key(path: str, repo: str) -> str:
    """Namespace fetch keys by repo to avoid collisions."""
    return f"{repo}:{path}"


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
    - github_ops.safe_session_close()
    - github_ops.append_to_register()
    - Direct bash_tool calls (<stdin>, /tmp, <string>) for infrastructure work
    """
    frame = inspect.stack()[1]
    caller_fn, caller_file = frame.function, frame.filename
    approved = (
        (caller_fn == 'safe_commit' and 'valoria_hooks' in caller_file) or
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
        raise RuntimeError("GITHUB_PAT not set")
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
                       skip_health_check: bool = False) -> dict:
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

    _refresh_token()

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

        for path, _ in additions:
            _session_fetches.pop(_repo_key(path, repo), None)
        for path in (deletions or []):
            _session_fetches.pop(_repo_key(path, repo), None)
        if _session_fetches:
            _refresh_token()
        else:
            _session_token = None

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

    fresh = read_files_graphql(
        ["session_log_current.md", "session_log_archive.md"],
        repo='ttrpg', skip_health_check=True
    )
    live_current = fresh.get("session_log_current.md", "") or ""
    live_archive  = fresh.get("session_log_archive.md",  "") or ""

    archive_tokens = len(live_archive) // 4
    if archive_tokens > ARCHIVE_WARN_THRESHOLD:
        print(f"[ARCHIVE WARNING] session_log_archive.md: {archive_tokens:,} tokens. Year-split soon.")

    live_id      = _extract_session_id(live_current)
    new_id       = _extract_session_id(new_session_log)
    bootstrap_id = _extract_session_id(bootstrap_session_log)

    if live_id and new_id and live_id == new_id:
        raise RuntimeError(f"DUPLICATE CLOSE BLOCKED: '{live_id}' already closed.")

    if live_current.strip() != bootstrap_session_log.strip():
        print(f"[safe_session_close] Intervening session: '{bootstrap_id}'→'{live_id}'. Archiving.")

    additions = [
        ("session_log_current.md", new_session_log),
        ("session_log_archive.md", live_archive + "\n---\n\n" + live_current),
    ]
    if extra_additions:
        additions.extend(extra_additions)

    auth = _authorize_next_commit()
    return atomic_commit(additions=additions, deletions=[], message=message,
                         repo='ttrpg', _auth=auth)


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
