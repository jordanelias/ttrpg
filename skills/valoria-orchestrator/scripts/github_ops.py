"""
github_ops.py — Valoria GitHub operations
Single source of truth for all GitHub reads/writes.
Uses GraphQL createCommitOnBranch for atomic multi-file commits.

PAT must be set as environment variable: GITHUB_PAT

Session token system:
  read_files_graphql() records every fetched path and generates a session
  token (SHA-256 of all fetched content). Use assert_fetched(paths) to
  verify specific files were fetched before proceeding. Include the token
  in every fetch log.
"""

import os, sys, json, base64, re, hashlib, urllib.request, urllib.error

REPO_OWNER = "jordanelias"
REPO_NAME  = "ttrpg"
BRANCH     = "main"
API_BASE   = "https://api.github.com"
GRAPHQL_URL = "https://api.github.com/graphql"

# ── Session token state ───────────────────────────────────────────────────────
_session_fetches: dict = {}   # path -> content (str)
_session_token:   str  = None


def _refresh_token() -> str:
    global _session_token
    blob = json.dumps(
        {p: c for p, c in sorted(_session_fetches.items()) if c},
        sort_keys=True
    )
    _session_token = hashlib.sha256(blob.encode()).hexdigest()[:16]
    return _session_token


def get_session_token() -> str:
    """Return current session token; raises if no fetches have occurred."""
    if not _session_token:
        raise RuntimeError(
            "No session token — read_files_graphql() has not been called this session. "
            "Fetch required files before proceeding."
        )
    return _session_token


def assert_fetched(*paths) -> str:
    """
    Assert that every path in `paths` was fetched via read_files_graphql()
    this session. Returns the current session token on success.

    Raises RuntimeError listing any paths not fetched.

    Usage (in skill Input Validation):
        token = g.assert_fetched(
            'references/canonical_sources.yaml',
            'references/params_combat.md',
        )
        # Include token in fetch log before proceeding.
    """
    missing = [p for p in paths if p not in _session_fetches]
    if missing:
        raise RuntimeError(
            f"Required paths not fetched this session: {missing}\n"
            f"Call read_files_graphql({missing}) before proceeding."
        )
    return get_session_token()


# ── Auth / HTTP helpers ───────────────────────────────────────────────────────

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


# ── Core read operations ──────────────────────────────────────────────────────

def read_files_graphql(paths: list) -> dict:
    """
    Batch-read multiple files in a single GraphQL request.
    Records every fetched path in the session fetch registry and
    refreshes the session token.

    Returns: dict {path -> content_str | None}
    None means the file does not exist on GitHub.
    """
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
        _session_fetches[path] = content   # record regardless of None
        output[path] = content

    _refresh_token()
    return output


def read_file(path: str) -> str:
    """Single-file read via REST. Prefer read_files_graphql() for batches."""
    d = _get(path)
    content = base64.b64decode(d["content"]).decode("utf-8")
    _session_fetches[path] = content
    _refresh_token()
    return content


def read_files(paths: list) -> dict:
    """Sequential REST reads. Use read_files_graphql() instead."""
    return {p: read_file(p) for p in paths}


# ── Directory / existence helpers ─────────────────────────────────────────────

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


# ── Write operations ──────────────────────────────────────────────────────────

def get_head_oid() -> str:
    q = """
    query($owner: String!, $name: String!, $branch: String!) {
      repository(owner: $owner, name: $name) {
        ref(qualifiedName: $branch) {
          target { oid }
        }
      }
    }
    """
    result = _graphql(q, {"owner": REPO_OWNER, "name": REPO_NAME, "branch": BRANCH})
    return result["data"]["repository"]["ref"]["target"]["oid"]


def atomic_commit(
    additions: list,   # list of (path, content_str)
    deletions: list,   # list of path strings
    message:   str,
    expected_oid: str = None,
) -> str:
    """
    Atomically commit additions and deletions.
    Returns the new commit OID on success.
    Raises RuntimeError on failure.

    After calling this, re-fetch any modified files before referencing
    them again (call read_files_graphql on modified paths).
    """
    if expected_oid is None:
        expected_oid = get_head_oid()

    file_additions = [
        {
            "path": path,
            "contents": base64.b64encode(content.encode("utf-8")).decode("ascii"),
        }
        for path, content in additions
    ]
    file_deletions = [{"path": p} for p in deletions]

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

        # Invalidate fetched cache for committed paths so re-fetch is forced
        for path, _ in additions:
            _session_fetches.pop(path, None)
        for path in deletions:
            _session_fetches.pop(path, None)
        if _session_fetches:
            _refresh_token()
        else:
            global _session_token
            _session_token = None

        return oid

    except Exception as e:
        raise RuntimeError(f"Atomic commit error: {e}")


# ── Session close helper ───────────────────────────────────────────────────────

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
    Close a session safely, preventing overwrite of concurrent session closes.
    See docstring in original github_ops.py for full protocol.
    """
    fresh = read_files_graphql(["session_log_current.md", "session_log_archive.md"])
    live_current = fresh.get("session_log_current.md", "") or ""
    live_archive  = fresh.get("session_log_archive.md",  "") or ""

    live_id      = _extract_session_id(live_current)
    new_id       = _extract_session_id(new_session_log)
    bootstrap_id = _extract_session_id(bootstrap_session_log)

    if live_id and new_id and live_id == new_id:
        raise RuntimeError(
            f"DUPLICATE CLOSE BLOCKED: session_log_current.md already contains "
            f"session_id '{live_id}'. This session has already been closed."
        )

    if live_current.strip() != bootstrap_session_log.strip():
        print(
            f"[safe_session_close] Intervening session detected: "
            f"bootstrap='{bootstrap_id}', live='{live_id}'. "
            f"Archiving live session before writing ours."
        )

    updated_archive = live_archive + "\n---\n\n" + live_current
    additions = [
        ("session_log_current.md", new_session_log),
        ("session_log_archive.md", updated_archive),
    ]
    if extra_additions:
        additions.extend(extra_additions)

    return atomic_commit(additions=additions, deletions=[], message=message)


# ── CLI smoke test ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Head OID:", get_head_oid())
    print("session_log_current.md size:", file_size("session_log_current.md"))
    print("tools/ contents:", list_directory("tools"))
    files = read_files_graphql(["session_log_current.md"])
    print("Session token:", get_session_token())
    token = assert_fetched("session_log_current.md")
    print("assert_fetched passed. Token:", token)
