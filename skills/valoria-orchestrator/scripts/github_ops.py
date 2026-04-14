"""
github_ops.py — Valoria GitHub operations
Single source of truth for all GitHub reads/writes.

COMMIT AUTHORIZATION:
  All commits must go through valoria_hooks.safe_commit().
  Direct atomic_commit() calls are blocked unless authorized via _authorize_next_commit().
  This prevents bypassing enforcement gates under task pressure.

REGISTER HEALTH:
  check_register_health() runs automatically on first read_files_graphql() call.
  Hard stop on any file exceeding TOKEN_THRESHOLDS. Not a warning.

SESSION TOKEN:
  read_files_graphql() generates a session token (SHA-256 of fetched content).
  assert_fetched() verifies files were fetched this session.
"""

import os, sys, json, base64, re, hashlib, secrets, urllib.request, urllib.error

REPO_OWNER  = "jordanelias"
REPO_NAME   = "ttrpg"
BRANCH      = "main"
API_BASE    = "https://api.github.com"
GRAPHQL_URL = "https://api.github.com/graphql"

# ── Register health thresholds (tokens = chars // 4) ─────────────────────────
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

ARCHIVE_WARN_THRESHOLD = 100_000  # tokens — triggers year-split warning

# ── Session state ─────────────────────────────────────────────────────────────
_session_fetches: dict = {}
_session_token:   str  = None
_health_checked:  bool = False
_commit_auth:     str  = None   # single-use token set by _authorize_next_commit()


# ── Session token ─────────────────────────────────────────────────────────────

def _refresh_token() -> str:
    global _session_token
    blob = json.dumps(
        {p: c for p, c in sorted(_session_fetches.items()) if c},
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


def assert_fetched(*paths) -> str:
    missing = [p for p in paths if p not in _session_fetches or _session_fetches[p] is None]
    if missing:
        raise RuntimeError(
            f"Required paths not fetched this session: {missing}\n"
            f"Call read_files_graphql({missing}) before proceeding."
        )
    return get_session_token()


# ── Commit authorization ──────────────────────────────────────────────────────

def _authorize_next_commit() -> str:
    """
    Generate a single-use authorization token for the next atomic_commit() call.
    Called exclusively by valoria_hooks.safe_commit() after all gates pass.
    Returns the token; caller must pass it as _auth= to atomic_commit().
    Token is reset to None immediately after use (or on any commit failure).

    For infrastructure bypasses ONLY: call this explicitly and document why.
    """
    global _commit_auth
    _commit_auth = secrets.token_hex(8)
    return _commit_auth


# ── Auth / HTTP ───────────────────────────────────────────────────────────────

def _get_pat() -> str:
    pat = os.environ.get("GITHUB_PAT", "")
    if not pat:
        raise RuntimeError("GITHUB_PAT environment variable not set")
    return pat


def _headers() -> dict:
    return {
        "Authorization": f"token {_get_pat()}",
        "Content-Type":  "application/json",
        "Accept":        "application/vnd.github.v3+json",
    }


def _get(path: str) -> dict:
    url = f"{API_BASE}/repos/{REPO_OWNER}/{REPO_NAME}/contents/{path}"
    req = urllib.request.Request(url, headers=_headers())
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())


def _graphql(query: str, variables: dict = None) -> dict:
    payload = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request(GRAPHQL_URL, data=payload, headers=_headers())
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())


# ── Register health ───────────────────────────────────────────────────────────

def check_register_health(fetched: dict) -> None:
    """
    Hard stop if any fetched file exceeds its TOKEN_THRESHOLDS limit.
    Called automatically on first read_files_graphql() of session-start files.
    Raises RuntimeError on violation — no bypass.
    """
    global _health_checked
    violations = []
    print("\n## REGISTER HEALTH CHECK")

    for path, content in fetched.items():
        if content is None:
            continue
        tokens = len(content) // 4
        threshold = TOKEN_THRESHOLDS.get(path)
        if threshold is None:
            continue
        status = "✓" if tokens <= threshold else "✗"
        print(f"  {status}  {path}: {tokens:,} / {threshold:,} tokens")
        if tokens > threshold:
            violations.append(
                f"  {path}: {tokens:,} tokens exceeds {threshold:,} limit.\n"
                f"    → Archive resolved/applied/struck content to the _archive file.\n"
                f"    → See register chunking protocol in orchestrator SKILL.md."
            )

    if violations:
        raise RuntimeError(
            "\n[HARD STOP] Register health check FAILED:\n\n"
            + "\n".join(violations)
            + "\n\nChunk registers before any other work. Session cannot proceed."
        )

    _health_checked = True
    print("  Register health: ALL PASS\n")


def check_append_size(path: str, current: str, new_content: str) -> None:
    tokens = len(current + new_content) // 4
    threshold = TOKEN_THRESHOLDS.get(path)
    if threshold and tokens > threshold:
        raise RuntimeError(
            f"[CHUNK REQUIRED] {path} would reach {tokens:,} tokens (limit {threshold:,}).\n"
            f"Archive old content first."
        )
    if tokens > ARCHIVE_WARN_THRESHOLD and '_archive' in path:
        print(
            f"[ARCHIVE WARNING] {path}: {tokens:,} tokens approaching limit. "
            f"Consider year-split."
        )


def append_to_register(path: str, new_entries: str, commit_message: str) -> str:
    """Safe register append — checks size, then commits via safe_commit path."""
    fresh = read_files_graphql([path], skip_health_check=True)
    current = fresh.get(path) or ""
    check_append_size(path, current, new_entries)
    auth = _authorize_next_commit()
    return atomic_commit(
        additions=[(path, current + new_entries)],
        deletions=[],
        message=commit_message,
        _auth=auth,
    )


# ── Core reads ────────────────────────────────────────────────────────────────

def read_files_graphql(paths: list, skip_health_check: bool = False) -> dict:
    """
    Batch-read files via GraphQL. Runs register health check on first
    call that touches threshold-governed files (unless skip_health_check=True).

    skip_health_check: use ONLY for archive reads and infrastructure bootstrap.
    """
    global _health_checked

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
    result = _graphql(query, {"owner": REPO_OWNER, "name": REPO_NAME})
    repo = result["data"]["repository"]

    output = {}
    for alias, path in aliases.items():
        content = repo[alias]["text"] if repo[alias] else None
        _session_fetches[path] = content
        output[path] = content

    _refresh_token()

    if not _health_checked and not skip_health_check:
        governed = {p: c for p, c in output.items() if p in TOKEN_THRESHOLDS and c}
        if governed:
            check_register_health(governed)

    return output


def read_file(path: str) -> str:
    d = _get(path)
    content = base64.b64decode(d["content"]).decode("utf-8")
    _session_fetches[path] = content
    _refresh_token()
    return content


def read_files(paths: list) -> dict:
    return {p: read_file(p) for p in paths}


# ── Directory helpers ─────────────────────────────────────────────────────────

def file_exists(path: str) -> bool:
    try:
        _get(path)
        return True
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return False
        raise


def file_size(path: str) -> int:
    try:
        return _get(path).get("size", 0)
    except urllib.error.HTTPError:
        return -1


def list_directory(path: str) -> list:
    items = _get(path)
    return [item["name"] for item in items if isinstance(item, dict)]


# ── Write ─────────────────────────────────────────────────────────────────────

def get_head_oid() -> str:
    q = """
    query($owner: String!, $name: String!, $branch: String!) {
      repository(owner: $owner, name: $name) {
        ref(qualifiedName: $branch) { target { oid } }
      }
    }
    """
    result = _graphql(q, {"owner": REPO_OWNER, "name": REPO_NAME, "branch": BRANCH})
    return result["data"]["repository"]["ref"]["target"]["oid"]


def atomic_commit(
    additions: list,
    deletions: list,
    message:   str,
    expected_oid: str = None,
    _auth: str = None,
) -> str:
    """
    Atomic commit via GraphQL.

    REQUIRES authorization: must pass _auth=g._authorize_next_commit().
    valoria_hooks.safe_commit() does this automatically after all gates pass.
    Direct calls without authorization raise RuntimeError.

    Exception: safe_session_close() is a trusted internal caller and passes
    its own authorization token.
    """
    global _commit_auth, _session_token

    # Authorization check
    if _auth != _commit_auth or _commit_auth is None:
        raise RuntimeError(
            "[COMMIT BLOCKED] atomic_commit() called without authorization.\n"
            "Use h.safe_commit(additions, deletions, message) — it runs all\n"
            "enforcement gates and authorizes the commit automatically.\n\n"
            "For infrastructure-only bypasses:\n"
            "  auth = g._authorize_next_commit()\n"
            "  g.atomic_commit(..., _auth=auth)\n"
            "This bypass is visible in code and auditable."
        )
    _commit_auth = None  # single-use — reset immediately

    # Size check (redundant with pre_commit_gate but defense-in-depth)
    for path, content in additions:
        tokens = len(content) // 4
        threshold = TOKEN_THRESHOLDS.get(path)
        if threshold and tokens > threshold:
            raise RuntimeError(
                f"[COMMIT BLOCKED] {path}: {tokens:,} tokens exceeds {threshold:,} limit."
            )

    if expected_oid is None:
        expected_oid = get_head_oid()

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
                "repositoryNameWithOwner": f"{REPO_OWNER}/{REPO_NAME}",
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
                variables["input"]["expectedHeadOid"] = get_head_oid()
                result = _graphql(mutation, variables)
                if "errors" in result:
                    raise RuntimeError(f"Atomic commit failed after OID retry: {result['errors']}")
            else:
                raise RuntimeError(f"Atomic commit failed: {errs}")

        oid = result["data"]["createCommitOnBranch"]["commit"]["oid"]

        for path, _ in additions:
            _session_fetches.pop(path, None)
        for path in (deletions or []):
            _session_fetches.pop(path, None)
        if _session_fetches:
            _refresh_token()
        else:
            _session_token = None

        return oid

    except Exception as e:
        raise RuntimeError(f"Atomic commit error: {e}")


# ── Session close ─────────────────────────────────────────────────────────────

def _extract_session_id(content: str) -> str:
    m = re.search(r'session_id:\s*(.+)', content)
    return m.group(1).strip() if m else ""


def safe_session_close(
    new_session_log: str,
    bootstrap_session_log: str,
    extra_additions: list = None,
    message: str = "[infrastructure] Session close",
) -> str:
    """
    Safely close a session. Enforces session_log size limit.
    Trusted internal caller — authorizes its own commit.
    """
    tokens = len(new_session_log) // 4
    limit  = TOKEN_THRESHOLDS.get("session_log_current.md", 2_000)
    if tokens > limit:
        raise RuntimeError(
            f"[COMMIT BLOCKED] session_log_current.md would be {tokens:,} tokens "
            f"(limit {limit:,}). Trim to resumption block only."
        )

    fresh = read_files_graphql(
        ["session_log_current.md", "session_log_archive.md"],
        skip_health_check=True
    )
    live_current = fresh.get("session_log_current.md", "") or ""
    live_archive  = fresh.get("session_log_archive.md",  "") or ""

    # Archive size warning
    archive_tokens = len(live_archive) // 4
    if archive_tokens > ARCHIVE_WARN_THRESHOLD:
        print(
            f"[ARCHIVE WARNING] session_log_archive.md: {archive_tokens:,} tokens. "
            f"Consider year-split: session_log_archive_2026_q1.md"
        )

    live_id      = _extract_session_id(live_current)
    new_id       = _extract_session_id(new_session_log)
    bootstrap_id = _extract_session_id(bootstrap_session_log)

    if live_id and new_id and live_id == new_id:
        raise RuntimeError(
            f"DUPLICATE CLOSE BLOCKED: session_id '{live_id}' already closed."
        )

    if live_current.strip() != bootstrap_session_log.strip():
        print(
            f"[safe_session_close] Intervening session: "
            f"bootstrap='{bootstrap_id}', live='{live_id}'. Archiving live first."
        )

    updated_archive = live_archive + "\n---\n\n" + live_current
    additions = [
        ("session_log_current.md", new_session_log),
        ("session_log_archive.md", updated_archive),
    ]
    if extra_additions:
        additions.extend(extra_additions)

    # Trusted internal caller — self-authorize
    auth = _authorize_next_commit()
    return atomic_commit(additions=additions, deletions=[], message=message, _auth=auth)


# ── CLI smoke test ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Head OID:", get_head_oid())
    files = read_files_graphql(["session_log_current.md", "canon/editorial_ledger_summary.yaml"])
    print("Session token:", get_session_token())
    assert_fetched("session_log_current.md")
    print("Smoke test passed.")
