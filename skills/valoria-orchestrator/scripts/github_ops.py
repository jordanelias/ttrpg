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

Register health enforcement:
  check_register_health() is called automatically at bootstrap.
  Any register exceeding TOKEN_THRESHOLD raises a hard error — not a warning.
  append_to_register() enforces chunk thresholds before every write.
"""

import os, sys, json, base64, re, hashlib, urllib.request, urllib.error

REPO_OWNER  = "jordanelias"
REPO_NAME   = "ttrpg"
BRANCH      = "main"
API_BASE    = "https://api.github.com"
GRAPHQL_URL = "https://api.github.com/graphql"

# ── Register health thresholds (tokens = chars // 4) ─────────────────────────
# Any file fetched at session-start that exceeds this triggers a hard error.
SESSION_START_FILES = [
    "session_log_current.md",
    "canon/editorial_ledger.yaml",
    "canon/editorial_ledger_summary.yaml",
    "references/file_index_summary.md",
    "references/canonical_sources.yaml",
    "skills/valoria-orchestrator/SKILL.md",
]

TOKEN_THRESHOLDS = {
    # Session-start files: must stay tiny
    "session_log_current.md":              2_000,
    "canon/editorial_ledger.yaml":         2_000,   # active only — should be near-empty
    "canon/editorial_ledger_summary.yaml": 1_000,
    "references/file_index_summary.md":    1_000,
    "references/canonical_sources.yaml":   5_000,
    "skills/valoria-orchestrator/SKILL.md": 8_000,
    # Registers: chunked — active partitions only
    "canon/patch_register_active.yaml":   20_000,
    "canon/patch_register_index.md":      15_000,
    "tests/coverage_matrix.md":            5_000,
    "references/arc_register.md":         20_000,
    "references/propagation_map.md":      15_000,
    "references/design_registry.yaml":     8_000,
    # Archive files: never fetched at session start — no threshold enforced at read time
    # but append_to_register() will warn when archive exceeds ARCHIVE_WARN_THRESHOLD
}

ARCHIVE_WARN_THRESHOLD = 100_000  # tokens — archives approaching this need a year-split

# ── Session token state ───────────────────────────────────────────────────────
_session_fetches: dict = {}
_session_token:   str  = None
_health_checked:  bool = False


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


# ── Register health enforcement ───────────────────────────────────────────────

def check_register_health(fetched: dict) -> None:
    """
    Hard-stop if any fetched file exceeds its token threshold.
    Called automatically by read_files_graphql() on first session-start fetch.
    NOT a warning. Raises RuntimeError listing violations.

    Also prints a health report for every file checked.
    """
    global _health_checked
    violations = []
    report_lines = ["\n## REGISTER HEALTH CHECK"]

    for path, content in fetched.items():
        if content is None:
            continue
        tokens = len(content) // 4
        threshold = TOKEN_THRESHOLDS.get(path)
        if threshold is not None:
            status = "✓" if tokens <= threshold else "✗ VIOLATION"
            report_lines.append(
                f"  {status}  {path}: {tokens:,} tokens (limit {threshold:,})"
            )
            if tokens > threshold:
                violations.append(
                    f"  {path}: {tokens:,} tokens exceeds {threshold:,} token limit.\n"
                    f"    → This file must be chunked before this session can proceed.\n"
                    f"    → Archive resolved/old content to the corresponding _archive file.\n"
                    f"    → See register chunking protocol in orchestrator SKILL.md."
                )
        else:
            report_lines.append(f"  —  {path}: {tokens:,} tokens (no threshold set)")

    print('\n'.join(report_lines))

    if violations:
        msg = (
            "\n[HARD STOP] Register health check failed. "
            "The following files exceed their token thresholds:\n\n"
            + "\n".join(violations)
            + "\n\nDo NOT proceed with any task until these files are chunked. "
            "Chunking protocol: archive resolved/struck/applied items to the "
            "corresponding _archive.yaml or _archive.md file, update the _summary "
            "and _index files, then re-run bootstrap."
        )
        raise RuntimeError(msg)

    _health_checked = True
    print("  Register health: ALL PASS\n")


def check_append_size(path: str, current_content: str, new_content: str) -> None:
    """
    Called by append_to_register() before any write that grows a register.
    Raises if the post-append size would exceed the threshold.
    Warns (does not raise) for archive files approaching ARCHIVE_WARN_THRESHOLD.
    """
    combined = current_content + new_content
    tokens = len(combined) // 4
    threshold = TOKEN_THRESHOLDS.get(path)

    if threshold and tokens > threshold:
        raise RuntimeError(
            f"[CHUNK REQUIRED] Writing to {path} would produce {tokens:,} tokens "
            f"(limit {threshold:,}).\n"
            f"Archive resolved/applied items before appending new content.\n"
            f"Archive target: {path.replace('.yaml','_archive.yaml').replace('.md','_archive.md')}"
        )

    if tokens > ARCHIVE_WARN_THRESHOLD and '_archive' in path:
        print(
            f"[ARCHIVE SIZE WARNING] {path}: {tokens:,} tokens. "
            f"Consider year-splitting (e.g. {path.replace('_archive','_archive_2026_q1')}) "
            f"when this exceeds {ARCHIVE_WARN_THRESHOLD:,}."
        )


def append_to_register(path: str, new_entries: str, commit_message: str) -> str:
    """
    Safe append to any register file. Enforces size threshold before writing.
    Fetches current content, checks post-append size, commits atomically.

    Use this instead of building register content manually in atomic_commit().
    """
    fresh = read_files_graphql([path])
    current = fresh.get(path) or ""
    check_append_size(path, current, new_entries)
    combined = current + new_entries
    return atomic_commit(
        additions=[(path, combined)],
        deletions=[],
        message=commit_message,
    )


# ── Core read operations ──────────────────────────────────────────────────────

def read_files_graphql(paths: list, skip_health_check: bool = False) -> dict:
    """
    Batch-read multiple files in a single GraphQL request.
    On first call each session, runs check_register_health() automatically.
    Health check is skipped for subsequent calls (already checked) and for
    archive files (skip_health_check=True).

    Returns: dict {path -> content_str | None}
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

    # Run health check on first fetch of session-start files
    if not _health_checked and not skip_health_check:
        session_start_fetched = {
            p: c for p, c in output.items()
            if p in TOKEN_THRESHOLDS
        }
        if session_start_fetched:
            check_register_health(session_start_fetched)

    return output


def read_file(path: str) -> str:
    d = _get(path)
    content = base64.b64decode(d["content"]).decode("utf-8")
    _session_fetches[path] = content
    _refresh_token()
    return content


def read_files(paths: list) -> dict:
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
    additions: list,
    deletions: list,
    message:   str,
    expected_oid: str = None,
) -> str:
    """
    Atomically commit additions and deletions.
    Automatically checks append size for any path in TOKEN_THRESHOLDS.
    Returns the new commit OID on success.
    """
    # Pre-commit size check for threshold-governed files
    for path, content in additions:
        tokens = len(content) // 4
        threshold = TOKEN_THRESHOLDS.get(path)
        if threshold and tokens > threshold:
            raise RuntimeError(
                f"[COMMIT BLOCKED] {path} would be {tokens:,} tokens after this commit "
                f"(limit {threshold:,}).\n"
                f"Archive old content before committing new additions."
            )

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
    Enforces session_log_current.md size threshold before writing.
    """
    # Size check on new session log
    tokens = len(new_session_log) // 4
    threshold = TOKEN_THRESHOLDS.get("session_log_current.md", 2_000)
    if tokens > threshold:
        raise RuntimeError(
            f"[COMMIT BLOCKED] session_log_current.md would be {tokens:,} tokens "
            f"(limit {threshold:,}). Trim the session log to the resumption block only."
        )

    fresh = read_files_graphql(
        ["session_log_current.md", "session_log_archive.md"],
        skip_health_check=True
    )
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
    files = read_files_graphql(["session_log_current.md", "canon/editorial_ledger_summary.yaml"])
    print("Session token:", get_session_token())
    token = assert_fetched("session_log_current.md")
    print("assert_fetched passed. Token:", token)
