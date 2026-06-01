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
# TOKEN_THRESHOLDS — token caps per file (raised 2026-05-02 per ED-786; 2026-05-30 per Jordan)
# Rationale: The 2026-05-02 register-collision incidents (ED-782, ED-783) traced to chronic
# cap pressure on editorial_ledger and canonical_sources during heavy editorial sessions.
# Caps below were raised to give realistic headroom for routine work (2-3 commits per session).
# Combined with the chunking discipline documented in workplan §6.x, registers should now
# stay under 80% of cap during normal operations.
# 2026-05-30 (Jordan directive): hand-edited register/accumulator class -> uniform 20_000
# (design_registry, patch_register_active, propagation_map, coverage_matrix; arc_register already
# 20_000). On-demand fetches, NOT in the bootstrap session set -- headroom here is rate-budget-free.
# NOT raised: bootstrap-loaded summaries (@ 2_000) + SKILL.md (@ 8_000) load every subprocess / stay lean.
# editorial_ledger.jsonl already @ 200_000. canonical_sources.yaml: interim 9_000->12_000 to clear an
# imminent commit-blocking OVER; NOT the fix -- bloat is 115 freshness canonical_sha fields. Root-cause
# fix queued (own infra task): split SHA store -> references/canonical_freshness.yaml (writer
# tools/freshness_gate.py) so canonical_sources reverts to ~5k declarations on the hot bootstrap path.
# Deferred -- freshness-subsystem refactor; subsystem undocumented (roadmap 2.4).
TOKEN_THRESHOLDS = {
    "session_log_current.md":                  2_000,   # bootstrap-loaded; rotates each session
    "session_logs/index.md":                   2_000,   # bootstrap-loaded; tiny index
    "canon/editorial_ledger.jsonl":            200_000, # JSONL single-source (2026-05-28): never loaded whole at bootstrap; append-by-line
    "references/file_index_summary.md":        2_000,   # bootstrap-loaded; grows with project
    "references/canonical_sources.yaml":      12_000,   # bootstrap-loaded; 5_000->8_000->9_000; 2026-05-30 INTERIM 9_000->12_000 (was 8_955/9_000); SHA-split queued
    "skills/valoria-orchestrator/SKILL.md":    8_000,   # skill doc -- kept lean on purpose (composability)
    "canon/patch_register_active.yaml":       20_000,   # register; 2026-05-30 18_000->20_000 (uniform register class)
    "tests/coverage_matrix.md":               20_000,   # accumulator (grows per sim/test); 2026-05-30 8_000->20_000
    "references/arc_register.md":             20_000,   # register (already 20_000 -- class anchor)
    "references/propagation_map.md":          20_000,   # co-file map; 2026-05-30 15_000->20_000 (uniform register class)
    "references/design_registry.yaml":        20_000,   # register; 2026-05-30 8_000->20_000 (uniform register class)
}
ARCHIVE_WARN_THRESHOLD = 100_000

# ── Session state (per-repo) ───────────────────────────────────────────────────
_active_repo:      str  = 'ttrpg'
_session_fetches:  dict = {}   # path -> content (merged across repos; use _repo_key)
_session_token:    str  = None
_health_checked:   bool = False
_commit_auth:      str  = None

# Optimistic concurrency state
_fetch_head:       dict = {}   # repo_key -> HEAD OID at fetch time


class CollisionError(RuntimeError):
    """
    Raised when a commit is blocked because a file was modified by another
    session since this session's fetch. The caller must re-fetch the affected
    paths, reconcile, and retry.
    """
    def __init__(self, colliding_paths, fetch_head, current_head, message=None):
        self.colliding_paths = colliding_paths
        self.fetch_head = fetch_head
        self.current_head = current_head
        default_msg = (
            f"[COLLISION] Commit blocked — repository HEAD moved since session fetch.\n"
            f"  Paths in commit: {colliding_paths}\n"
            f"  Your fetch HEAD: {fetch_head[:12] if fetch_head else 'unknown'}\n"
            f"  Current HEAD:    {current_head[:12] if current_head else 'unknown'}\n\n"
            f"  Another session committed between your fetch and this commit.\n"
            f"  To resolve:\n"
            f"    1. Re-fetch affected paths with read_files_graphql(<paths>).\n"
            f"    2. Examine the fresh content — has your target file been modified?\n"
            f"    3. If yes, reconcile your changes against the fresh content.\n"
            f"    4. Retry the commit.\n\n"
            f"  For session-coordinating files (session_log_current.md, registers)\n"
            f"  where the other session's changes are orthogonal to yours,\n"
            f"  merge rather than overwrite."
        )
        super().__init__(message or default_msg)


def get_fetch_head(path: str, repo: str = None) -> str:
    """
    Return the HEAD OID recorded at fetch time for path, or None if not fetched.
    Used by tooling to check collision state without touching _fetch_head directly.
    """
    repo = repo or _active_repo
    return _fetch_head.get(_repo_key(path, repo))

# ── Disk cache (persists across bash_tool subprocesses) ──────────────────────
_CACHE_PATH = '/home/claude/.valoria_cache.json'

def _save_cache() -> None:
    """Write _session_fetches + _fetch_head to disk. Called after reads and commits."""
    try:
        with open(_CACHE_PATH, 'w') as f:
            json.dump({
                'fetches': {k: v for k, v in _session_fetches.items() if v is not None},
                'token': _session_token,
                'fetch_head': _fetch_head,
            }, f)
    except Exception:
        pass  # non-fatal — cache is optimization, not requirement

def _load_cache() -> bool:
    """Restore _session_fetches + _fetch_head from disk. Returns True if cache loaded."""
    global _session_fetches, _session_token, _health_checked, _fetch_head
    try:
        with open(_CACHE_PATH) as f:
            data = json.load(f)
        _session_fetches = data.get('fetches', {})
        _session_token = data.get('token')
        _fetch_head = data.get('fetch_head', {})
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
    'session_logs/index.md',
    'file_index_summary.md',
    'canonical_sources.yaml',
    'patch_register_active.yaml',
    'editorial_ledger.jsonl',          # canonical editorial store (post-2026-05-28 JSONL migration)
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
    and trusted internal callers.

    Caller verification via inspect.stack():
    - valoria_hooks.safe_commit()
    - valoria_hooks.assert_bootstrap() (compliance auto-fix)
    - valoria_hooks.write_checkpoint() / close_checkpoint() (session checkpoints)
    - github_ops.safe_session_close()
    - github_ops.append_to_register()
    - github_ops.start_session_log() / close_session_log() / update_session_log() (session lifecycle)
    - github_ops.write_handoff() / archive_handoff() (handoff lifecycle)
    - Direct bash_tool calls (<stdin>, /tmp, <string>) for infrastructure work
    """
    frame = inspect.stack()[1]
    caller_fn, caller_file = frame.function, frame.filename
    approved = (
        (caller_fn == 'safe_commit' and 'valoria_hooks' in caller_file) or
        (caller_fn == 'assert_bootstrap' and 'valoria_hooks' in caller_file) or
        (caller_fn in ('write_checkpoint', 'close_checkpoint') and 'valoria_hooks' in caller_file) or
        (caller_fn in ('safe_session_close', 'append_to_register',
                       'start_session_log', 'close_session_log', 'update_session_log',
                       'write_handoff', 'archive_handoff')
         and 'github_ops' in caller_file) or
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
                       force_full: bool = False,
                       skip_cache: bool = False) -> dict:
    """
    Batch-read files from a repo via GraphQL.

    repo: 'ttrpg' (default) or 'valoria-game'
    skip_cache: when True, do NOT write fetched content into _session_fetches.
        Use this for tool-internal scans (compliance, freshness, indexers) whose
        content never enters Claude's conversation context. Writing those fetches
        into _session_fetches poisons context_gate's accounting — the gate
        treats _session_fetches as a Claude-side context proxy, but tool-side
        bulk fetches don't actually consume the chat window.
    Returns: dict {path -> content_str | None}
    """
    global _health_checked
    repo = repo or _active_repo
    if repo not in REPOS:
        raise RuntimeError(f"Unknown repo '{repo}'")

    if not paths:
        return {}

    # Auto-index routing for design docs (unless force_full)
    if not force_full and REPOS[repo].get('enforce_health'):
        paths = _route_to_indexes(paths, repo)

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
        if not skip_cache:
            _session_fetches[key] = content
        output[path] = content

        # Record read depth. If force_full OR path is not a design doc
        # (designs/.../*.md but not _index.md), it's a full read.
        # Design docs that got routed to their _index.md variant are
        # tracked by read_index() when that fires separately.
        # Skip read-depth tracking on skip_cache fetches — they don't enter
        # the conversation and shouldn't be credited as reads.
        if content is not None and not skip_cache:
            is_design_doc = (
                path.startswith('designs/')
                and path.endswith('.md')
                and not path.endswith('_index.md')
            )
            if force_full or not is_design_doc:
                _full_reads.add(key)

    # Record HEAD OID at fetch time for optimistic concurrency protection.
    # One HEAD fetch per batch. All files in the batch share this fetch_head.
    # Skip on skip_cache — these fetches aren't followed by writes.
    if not skip_cache:
        try:
            current_head = get_head_oid(repo)
            for path in paths:
                key = _repo_key(path, repo)
                if output.get(path) is not None:
                    _fetch_head[key] = current_head
        except Exception:
            pass  # non-fatal — if we can't get HEAD, skip collision tracking

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


def _is_branch_protection_error(errs) -> bool:
    """True if a createCommitOnBranch failure is branch protection (B6),
    not a concurrency/other error."""
    s = str(errs).lower()
    return any(k in s for k in (
        'status check', 'required status', 'protected branch',
        'branch protection', 'not authorized to push', 'protected_branch',
    ))


def _commit_via_pr(additions, deletions, message, repo, base_oid=None) -> str:
    """B6 resolution (path 3): when createCommitOnBranch is rejected by main
    branch protection, commit the SAME changes via temp-branch + PR + squash-merge.
    Returns the merged HEAD oid on main. Reuses _headers() auth.

    Bounded risk: only invoked from atomic_commit's error path, i.e. when the
    direct mutation has ALREADY failed with a protection error — it cannot
    regress a working commit. If the PR merge is itself blocked, raises and
    leaves the temp branch for manual merge.
    """
    import time as _time
    api = f"https://api.github.com/repos/{REPO_OWNER}/{repo}"

    def _rest(method, url, body=None):
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(url, data=data, headers=_headers(), method=method)
        try:
            with urllib.request.urlopen(req) as r:
                return r.status, json.loads(r.read() or '{}')
        except urllib.error.HTTPError as e:
            return e.code, json.loads(e.read() or '{}')

    if not base_oid:
        base_oid = get_head_oid(repo)
    s, commit = _rest('GET', f'{api}/git/commits/{base_oid}')
    if s != 200:
        raise RuntimeError(f"[B6 fallback] cannot read base commit {base_oid}: {s} {commit}")
    base_tree = commit['tree']['sha']

    tree = []
    for path, content in additions:
        s, blob = _rest('POST', f'{api}/git/blobs',
                        {'content': base64.b64encode(content.encode('utf-8')).decode('ascii'),
                         'encoding': 'base64'})
        if s != 201:
            raise RuntimeError(f"[B6 fallback] blob create failed for {path}: {s} {blob}")
        tree.append({'path': path, 'mode': '100644', 'type': 'blob', 'sha': blob['sha']})
    for path in (deletions or []):
        tree.append({'path': path, 'mode': '100644', 'type': 'blob', 'sha': None})  # delete

    s, newtree = _rest('POST', f'{api}/git/trees', {'base_tree': base_tree, 'tree': tree})
    if s != 201:
        raise RuntimeError(f"[B6 fallback] tree create failed: {s} {newtree}")
    s, nc = _rest('POST', f'{api}/git/commits',
                  {'message': message, 'tree': newtree['sha'], 'parents': [base_oid]})
    if s != 201:
        raise RuntimeError(f"[B6 fallback] commit create failed: {s} {nc}")
    new_commit = nc['sha']

    br = f"auto/commit-{int(_time.time())}-{secrets.token_hex(3)}"
    s, r = _rest('POST', f'{api}/git/refs', {'ref': f'refs/heads/{br}', 'sha': new_commit})
    if s != 201:
        raise RuntimeError(f"[B6 fallback] temp branch create failed: {s} {r}")

    title = message.splitlines()[0]
    s, pr = _rest('POST', f'{api}/pulls',
                  {'title': title, 'head': br, 'base': BRANCH,
                   'body': '[automated B6-fallback commit — direct createCommitOnBranch was '
                           'rejected by branch protection]\n\n' + message})
    if s != 201:
        raise RuntimeError(f"[B6 fallback] PR open failed: {s} {pr}")
    prnum = pr['number']

    s, m = _rest('PUT', f'{api}/pulls/{prnum}/merge',
                 {'merge_method': 'squash', 'commit_title': title})
    if s != 200:
        raise RuntimeError(
            f"[B6 fallback] PR #{prnum} could not be merged ({s}: {m.get('message','')}). "
            f"Branch '{br}' left in place for manual merge.")
    _rest('DELETE', f'{api}/git/refs/heads/{br}')  # cleanup (best-effort)
    return get_head_oid(repo)


def atomic_commit(
    additions: list,
    deletions: list,
    message:   str,
    repo:      str  = None,
    expected_oid: str = None,
    _auth:     str  = None,
    collision_check: bool = True,
) -> str:
    """
    Atomic commit to ttrpg or valoria-game.

    REQUIRES authorization token from _authorize_next_commit().
    Use h.safe_commit(additions, deletions, message, repo='valoria-game') instead.

    Optimistic concurrency (collision_check=True, default):
      If expected_oid is not explicitly passed, this function uses the HEAD OID
      recorded at fetch time (from _fetch_head). If the repo HEAD has moved
      since any fetched file in this commit was read, raises CollisionError
      WITHOUT retrying. Caller must re-fetch, reconcile, retry.

    Escape hatch (collision_check=False):
      Use current HEAD, never fail on concurrency. Only safe for genuinely
      append-only patterns where the fresh fetch occurred immediately before
      this call (e.g. append_to_register's internal use).
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

    # Determine expected_oid for optimistic concurrency.
    committed_paths = [p for p, _ in additions] + list(deletions or [])
    committed_keys = [_repo_key(p, repo) for p in committed_paths]

    if expected_oid is not None:
        # Caller explicitly set it — honor their choice, no lookup needed.
        pass
    elif not collision_check:
        # Legacy/escape-hatch: use current HEAD, never fail on concurrency.
        expected_oid = get_head_oid(repo)
    else:
        # Optimistic concurrency: use the fetch-time HEAD of the paths being
        # committed. If none of the paths were fetched this session, we have
        # no anchor — fall back to current HEAD (effectively no protection,
        # but nothing to protect against). If paths have differing fetch
        # HEADs, require the most recent one (most restrictive).
        session_heads = set()
        for key in committed_keys:
            h = _fetch_head.get(key)
            if h:
                session_heads.add(h)
        if not session_heads:
            # No fetch heads recorded — this is a first-touch commit. Use
            # current HEAD; GitHub will still reject if someone else is also
            # first-touching, but this is the honest fallback.
            expected_oid = get_head_oid(repo)
        elif len(session_heads) == 1:
            expected_oid = session_heads.pop()
        else:
            # Multiple fetch heads among committed files — use the one that
            # is still current if any, else take any (will likely collision).
            current = get_head_oid(repo)
            expected_oid = current if current in session_heads else next(iter(session_heads))

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

    result = _graphql(mutation, variables)
    oid = None
    if "errors" in result:
        errs = result["errors"]
        # If the failure was expectedHeadOid mismatch, raise CollisionError.
        if any("expectedHeadOid" in str(e) or "stale" in str(e).lower() for e in errs):
            if collision_check:
                current_head = get_head_oid(repo)
                raise CollisionError(
                    colliding_paths=committed_paths,
                    fetch_head=expected_oid,
                    current_head=current_head,
                )
            else:
                # collision_check disabled — retry with fresh HEAD (legacy)
                variables["input"]["expectedHeadOid"] = get_head_oid(repo)
                result = _graphql(mutation, variables)
                if "errors" in result:
                    if _is_branch_protection_error(result["errors"]):
                        oid = _commit_via_pr(additions, deletions, message, repo, get_head_oid(repo))
                    else:
                        raise RuntimeError(f"Commit failed after HEAD refresh: {result['errors']}")
        elif _is_branch_protection_error(errs):
            # B6: branch protection rejects direct createCommitOnBranch (required
            # status checks). Transparently fall back to temp-branch + PR + merge.
            oid = _commit_via_pr(additions, deletions, message, repo, expected_oid)
        else:
            raise RuntimeError(f"Commit failed: {errs}")

    if oid is None:
        oid = result["data"]["createCommitOnBranch"]["commit"]["oid"]

    # Evict committed content — it's on GitHub now.
    # Session-permanent files get their cached value updated instead of evicted.
    for path, content in additions:
        key = _repo_key(path, repo)
        if any(perm in path for perm in SESSION_PERMANENT_PATTERNS):
            _session_fetches[key] = content  # update to committed version
            # Record the new HEAD as this file's fetch_head — it's authoritative now
            _fetch_head[key] = oid
        else:
            _session_fetches.pop(key, None)
            _fetch_head.pop(key, None)
    for path in (deletions or []):
        _session_fetches.pop(_repo_key(path, repo), None)
        _fetch_head.pop(_repo_key(path, repo), None)
    if _session_fetches:
        _refresh_token()
    else:
        _session_token = None
    _save_cache()

    return oid


def append_to_register(path: str, new_entries: str,
                       commit_message: str, repo: str = None) -> str:
    """Safe register append with size check. ttrpg only.

    Uses optimistic concurrency via atomic_commit's default behavior — the fresh
    fetch at the top of this function establishes a new fetch_head, and if
    anything else commits between our fetch and our commit, we get CollisionError.
    Caller should catch CollisionError and retry (re-fetch, re-append, re-commit).
    """
    repo = repo or 'ttrpg'
    fresh = read_files_graphql([path], repo=repo, skip_health_check=True)
    current = fresh.get(path) or ""
    if path.endswith('.jsonl'):
        # JSONL: ensure newline separation; new_entries is one or more JSON lines.
        if current and not current.endswith("\n"):
            current += "\n"
        combined = current + (new_entries if new_entries.endswith("\n") else new_entries + "\n")
    else:
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


# ── Per-session session logs ─────────────────────────────────────────────────

# Valid scope tags for session logs
SESSION_SCOPES = {
    'infrastructure', 'godot', 'editorial', 'design',
    'simulation', 'audit', 'general',
}

_active_session_scope: str = None
_active_session_log_path: str = None


def start_session_log(scope: str, token: str) -> str:
    """
    Create a per-session log file and update the session index.

    Creates: session_logs/<scope>_<token>.md
    Updates: session_logs/index.md (auto-generated active session list)
    Updates: session_log_current.md (auto-generated pointer to active sessions)

    Returns the path of the created session log file.
    """
    global _active_session_scope, _active_session_log_path

    if scope not in SESSION_SCOPES:
        raise RuntimeError(
            f"[SESSION] Unknown scope '{scope}'.\n"
            f"Valid: {sorted(SESSION_SCOPES)}"
        )

    from datetime import datetime, timezone
    now = datetime.now(timezone.utc).isoformat()

    log_path = f"session_logs/{scope}_{token}.md"
    log_content = (
        f"session_id: {scope}_{token}\n"
        f"scope: {scope}\n"
        f"token: {token}\n"
        f"started_at: {now}\n"
        f"status: ACTIVE\n"
    )

    # Read current index (may not exist yet)
    try:
        idx_files = read_files_graphql(
            ['session_logs/index.md'], repo='ttrpg', skip_health_check=True
        )
        index_content = idx_files.get('session_logs/index.md') or ''
    except Exception:
        index_content = ''

    # Append this session to index
    new_entry = f"- scope: {scope} | token: {token} | started: {now} | log: {log_path}\n"
    if not index_content.strip():
        index_content = "# Active Sessions\n\n" + new_entry
    else:
        index_content = index_content.rstrip() + "\n" + new_entry

    # Generate session_log_current.md as auto-pointer
    pointer_content = _generate_pointer(index_content)

    additions = [
        (log_path, log_content),
        ('session_logs/index.md', index_content),
        ('session_log_current.md', pointer_content),
    ]

    auth = _authorize_next_commit()
    oid = atomic_commit(
        additions=additions, deletions=[],
        message=f'[infrastructure] Session start — scope: {scope}, token: {token}',
        repo='ttrpg', _auth=auth,
    )

    _active_session_scope = scope
    _active_session_log_path = log_path
    print(f"[SESSION ✓] Started: {log_path} → {oid}")
    return log_path


def close_session_log(
    scope: str,
    token: str,
    final_log_content: str,
    handoff_id: str = None,
    extra_additions: list = None,
) -> str:
    """
    Archive a per-session log and remove it from the active index.

    Archives to: archives/session/session_log_<scope>_<date>_<token>.md
    Removes from: session_logs/index.md
    Updates: session_log_current.md (pointer)
    Deletes: session_logs/<scope>_<token>.md

    handoff_id: if provided, must reference an existing valid handoff file
    at handoffs/<handoff_id>.yaml. The handoff is the authoritative
    resumption document for the next session on this workstream.
    The archived session log will cite the handoff path.

    Returns commit OID.
    """
    global _active_session_scope, _active_session_log_path

    from datetime import datetime, timezone
    date_str = datetime.now(timezone.utc).strftime('%Y-%m-%d')

    log_path = f"session_logs/{scope}_{token}.md"
    archive_path = f"archives/session/session_log_{scope}_{date_str}_{token}.md"

    # Validate final log content
    REQUIRED_FIELDS = ['session_id', 'session_close', 'status', 'last_stage', 'next_action', 'blockers']
    missing = [f for f in REQUIRED_FIELDS if f not in final_log_content]
    if missing:
        raise RuntimeError(
            f"[SESSION] Close log missing fields: {missing}\n"
            f"Required: {REQUIRED_FIELDS}"
        )

    # Validate handoff reference if provided
    if handoff_id is not None:
        import yaml as _yaml
        handoff_path = f"{HANDOFF_DIR}/{handoff_id}.yaml"
        try:
            hf = read_files_graphql([handoff_path], repo='ttrpg', skip_health_check=True)
        except Exception as e:
            raise RuntimeError(
                f"[SESSION CLOSE BLOCKED] Cannot read handoff '{handoff_path}': {e}\n"
                f"Write the handoff with g.write_handoff() before closing the session."
            )
        hcontent = hf.get(handoff_path)
        if hcontent is None:
            raise RuntimeError(
                f"[SESSION CLOSE BLOCKED] Handoff '{handoff_path}' does not exist.\n"
                f"Write the handoff with g.write_handoff() before closing the session."
            )
        try:
            hparsed = _yaml.safe_load(hcontent)
        except Exception as e:
            raise RuntimeError(f"[SESSION CLOSE BLOCKED] Handoff '{handoff_path}' is not valid YAML: {e}")
        herrors = _validate_handoff_schema(hparsed)
        if herrors:
            raise RuntimeError(
                f"[SESSION CLOSE BLOCKED] Handoff '{handoff_path}' failed schema validation:\n"
                + "\n".join(f"  - {e}" for e in herrors)
            )
        # Hook-level checks (mirrors h.validate_handoff for consistent enforcement)
        for cf in hparsed.get('context_files', []):
            p = cf.get('path', '')
            if p.startswith('/') or '..' in p:
                raise RuntimeError(
                    f"[SESSION CLOSE BLOCKED] context_files path must be relative repo path, got: '{p}'"
                )
        for pattern in hparsed.get('owns', []):
            if not isinstance(pattern, str) or not pattern.strip():
                raise RuntimeError(
                    f"[SESSION CLOSE BLOCKED] 'owns' entries must be non-empty strings, got: {pattern!r}"
                )
        print(f"[SESSION] Handoff validated: {handoff_path}")

    # Read current index
    fresh = read_files_graphql(
        ['session_logs/index.md'], repo='ttrpg', skip_health_check=True
    )
    index_content = fresh.get('session_logs/index.md') or ''

    # Remove this session's entry from index
    lines = index_content.split('\n')
    new_lines = [l for l in lines if token not in l]
    new_index = '\n'.join(new_lines)

    # Generate updated pointer
    pointer_content = _generate_pointer(new_index)

    additions = [
        (archive_path, final_log_content),
        ('session_logs/index.md', new_index),
        ('session_log_current.md', pointer_content),
    ]
    if extra_additions:
        additions.extend(extra_additions)

    deletions = [log_path]

    auth = _authorize_next_commit()
    oid = atomic_commit(
        additions=additions, deletions=deletions,
        message=f'[infrastructure] Session close — scope: {scope}, token: {token}',
        repo='ttrpg', _auth=auth,
    )

    _active_session_scope = None
    _active_session_log_path = None
    print(f"[SESSION ✓] Closed: {log_path} → archived {archive_path} → {oid}")
    return oid


def read_active_sessions() -> list:
    """
    Parse session_logs/index.md and return list of active session dicts.
    Each dict: {scope, token, started, log}.
    """
    try:
        files = read_files_graphql(
            ['session_logs/index.md'], repo='ttrpg', skip_health_check=True
        )
        content = files.get('session_logs/index.md') or ''
    except Exception:
        return []

    sessions = []
    for line in content.split('\n'):
        if not line.startswith('- scope:'):
            continue
        parts = {}
        for segment in line[2:].split(' | '):
            segment = segment.strip()
            if ':' in segment:
                k, v = segment.split(':', 1)
                parts[k.strip()] = v.strip()
        if parts.get('scope') and parts.get('token'):
            sessions.append(parts)
    return sessions


def update_session_log(scope: str, token: str, content: str) -> str:
    """
    Write updated content to the active per-session log.
    Only the owning session should call this.
    """
    log_path = f"session_logs/{scope}_{token}.md"
    tokens = len(content) // 4
    if tokens > 2000:
        raise RuntimeError(
            f"[SESSION] Per-session log too large: {tokens:,} tokens (limit 2,000).\n"
            f"Trim to resumption block only."
        )
    auth = _authorize_next_commit()
    oid = atomic_commit(
        additions=[(log_path, content)], deletions=[],
        message=f'[infrastructure] Session log update — {scope}_{token}',
        repo='ttrpg', _auth=auth,
    )
    print(f"[SESSION ✓] Updated: {log_path} → {oid}")
    return oid


def _generate_pointer(index_content: str) -> str:
    """
    Generate session_log_current.md as an auto-generated pointer
    to the active sessions index.
    """
    from datetime import datetime, timezone
    now = datetime.now(timezone.utc).isoformat()

    # Count active sessions from index
    session_count = sum(1 for l in index_content.split('\n') if l.startswith('- scope:'))

    return (
        f"# Session Status (auto-generated)\n"
        f"# DO NOT EDIT — this file is managed by start_session_log / close_session_log\n"
        f"#\n"
        f"# Active sessions: {session_count}\n"
        f"# Last updated: {now}\n"
        f"# See: session_logs/index.md for details\n"
        f"#\n"
        f"session_id: pointer\n"
        f"status: {'ACTIVE' if session_count > 0 else 'IDLE'}\n"
        f"active_sessions: {session_count}\n"
        f"last_stage: auto-generated\n"
        f"next_action:\n"
        f"  skill: see session_logs/index.md\n"
        f"blockers: []\n"
    )

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
        'session_logs/index.md',
        # canon/editorial_ledger_summary.yaml retired in the 2026-05-28 JSONL cutover
        # (deprecated to deprecated/canon/). The canonical canon/editorial_ledger.jsonl
        # is fetched on demand by editorial tasks (task_gate editorial / propose_mechanic /
        # design_proposal), not at every bootstrap — it is a consolidated store, not a
        # kept-small register.
        'references/file_index_summary.md',
        'references/canonical_sources.yaml',
        'references/roadmap_state.yaml',
        'references/lane_assignments.yaml',
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

    # Read and report active handoffs
    try:
        _g_mod._active_handoffs = read_all_handoffs()
        report_handoffs(_g_mod._active_handoffs)
    except Exception as e:
        _g_mod._active_handoffs = []
        print(f"[HANDOFF WARN] Could not read handoffs: {e}")

    # Report roadmap position (non-blocking; absent file degrades gracefully)
    try:
        report_roadmap(files.get('references/roadmap_state.yaml'))
    except Exception as e:
        print(f"[ROADMAP WARN] Could not read roadmap state: {e}")

    # Report current lane (3-session mode; non-blocking; silent if no lane declared)
    try:
        report_lane(files.get('references/lane_assignments.yaml'))
    except Exception as e:
        print(f"[LANE WARN] Could not read lane assignment: {e}")

    return _g_mod, _h_mod, files, token



# ── Smart fetch (index-first) ────────────────────────────────────────────

def fetch_system(system: str, canonical_sources_content: str,
                 depth: str = 'index', repo: str = None) -> dict:
    """
    Fetch system files using depth-aware routing.

    depth:
      'index'    — canonical doc only (default, sufficient for most work)
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
    status = (entry.get('status') or 'active').lower()
    if status == 'deprecated':
        print(f"[SKIP] System '{system}' is deprecated — no fetch needed.")
        return {}
    if status == 'provisional':
        print(f"[WARN] System '{system}' is PROVISIONAL — design not finalized; "
              f"treat as a stub pending editorial review.")
    elif status == 'design_debt':
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
    if depth in ('index', 'full', 'all'):
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


# ── Index routing ─────────────────────────────────────────────────────────

_index_route_cache: dict = {}  # path -> index_path or None

def _route_to_indexes(paths: list, repo: str) -> list:
    """
    For any design doc path that has a committed _index.md,
    substitute the index path unless force_full=True.
    Caches mapping in session state.
    """
    routed = []
    for p in paths:
        if not p.startswith('designs/') or p.endswith('_index.md') or p.endswith('_infill.md'):
            routed.append(p)
            continue
        cache_key = _repo_key(p, repo)
        if cache_key in _index_route_cache:
            skel = _index_route_cache[cache_key]
            routed.append(skel if skel else p)
        else:
            # Check if index exists (one API call — cached after first check)
            idx_path = p[:-3] + '_index.md' if p.endswith('.md') else p + '_index.md'
            if file_exists(idx_path, repo):
                _index_route_cache[cache_key] = idx_path
                routed.append(idx_path)
                # Record that the ORIGINAL design doc path was index-routed.
                # This lets read_depth(original_path) return 'index' even
                # though the fetch cache holds content under the index path.
                _index_reads[cache_key] = True
                print(f"[INDEX ROUTE] {p} → {idx_path}")
            else:
                _index_route_cache[cache_key] = None
                routed.append(p)
    return routed


# ── fetch_for_task: single-call task setup ───────────────────────────────────

def fetch_for_task(task_type: str, system: str = None) -> dict:
    """
    Single call to load everything a task needs, routed optimally.
    - Loads task-required files from TASK_REQUIRED_FILES
    - If system provided, loads index + params (via fetch_system)
    - Uses index routing by default
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
        system_files = fetch_system(system, cs, depth='index')
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


# ── Heading-gated reads (index-first audit pattern) ─────────────────────

import re as _re_mod

def read_index(path: str, repo: str = None) -> list:
    """
    Fetch a file and return its heading structure without body content.
    
    Returns list of dicts:
      [{'line': int, 'level': int, 'text': str, 'idx': int}, ...]
    
    Also caches the full content internally (avoids double-fetch on infill).
    Prints index to stdout for Claude's context.
    """
    repo = repo or _active_repo
    key = _repo_key(path, repo)
    
    # Use cached content if available. If the path was index-routed on a
    # prior fetch, the content lives under the routed _index.md key — not
    # under the original path's key.
    content = _session_fetches.get(key)
    if content is None:
        # Check if this path has been index-routed this session
        routed_cached = _index_route_cache.get(key)
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
                raise RuntimeError(f"[INDEX] File not found: {path} in {repo}")
    
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
    
    # Track that this path has been indexed
    _index_reads[_repo_key(path, repo)] = True
    
    # Print compact index
    total_lines = len(lines)
    total_tokens = total_lines * 10 // 4  # rough estimate
    print(f"\n[INDEX] {path} — {total_lines} lines, ~{len(content)//4} tokens, {len(headings)} headings")
    for h in headings:
        indent = "  " * (h['level'] - 1)
        print(f"  {h['idx']:>3}  L{h['line']:<5} {indent}{h['text']}")
    
    return headings


def read_sections(path: str, heading_indices: list, repo: str = None) -> str:
    """
    Return content under specified headings only.
    
    heading_indices: list of idx values from read_index() output.
    Returns concatenated section content (heading + body until next same-or-higher heading).
    """
    repo = repo or _active_repo
    key = _repo_key(path, repo)
    
    content = _session_fetches.get(key)
    if content is None:
        # Check index-route cache — content may live under routed path
        routed = _index_route_cache.get(key)
        if routed:
            content = _session_fetches.get(_repo_key(routed, repo))
            if content is not None:
                # Update key so section tracking below records against original path
                # (intentional: sim_gate uses the original path for depth lookups)
                pass
    if content is None:
        raise RuntimeError(f"[SECTIONS] File not fetched: {path}. Call read_index() first.")
    
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

# Index tracking state
_index_reads: dict = {}

# Read-depth tracking state
_section_reads: dict = {}  # repo_key -> set of heading indices read via read_sections()
_full_reads: set = set()   # repo_keys that have been fully read

def was_indexed(path: str, repo: str = None) -> bool:
    """Check if a path went through read_index() this session."""
    repo = repo or _active_repo
    return _index_reads.get(_repo_key(path, repo), False)


def read_depth(path: str, repo: str = None) -> str:
    """
    Return read depth for a path this session:
      'full'     — full content fetched (non-design doc or force_full=True or all sections read)
      'sections' — partial read via read_sections() (subset of headings)
      'index' — only the index was fetched (design doc auto-route)
      'none'     — not fetched this session
    """
    repo = repo or _active_repo
    key = _repo_key(path, repo)

    if key in _full_reads:
        return 'full'
    if key in _section_reads and _section_reads[key]:
        return 'sections'
    if key in _index_reads and _index_reads[key]:
        return 'index'
    if key in _session_fetches and _session_fetches[key] is not None:
        # Content present, no tracking — assume full for non-design docs.
        # Design docs always route through index or sections tracking.
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
      'any'      — any depth including index counts

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


# ── Handoffs ─────────────────────────────────────────────────────────────────
#
# Per-workstream handoff files live at handoffs/<id>.yaml.
# Each handoff is a structured context-loading recipe: what to resume,
# which files to fetch, what state to carry forward.
#
# Multiple handoffs can be active concurrently (parallel workstreams).
# Conflict detection uses the `owns` field — glob patterns of files
# each workstream is actively modifying.

HANDOFF_DIR = 'handoffs'
HANDOFF_ARCHIVE_DIR = 'archives/handoffs'

HANDOFF_REQUIRED_FIELDS = {
    'id', 'task', 'context_files', 'working_state', 'last_commit', 'owns',
}
HANDOFF_TASK_REQUIRED = {'skill', 'description'}
HANDOFF_CTX_FILE_REQUIRED = {'path', 'depth', 'reason'}
HANDOFF_VALID_DEPTHS = {'full', 'skeleton'}


def _validate_handoff_schema(handoff: dict) -> list:
    """
    Validate a handoff dict against the schema.
    Returns list of error strings. Empty = valid.
    """
    errors = []

    missing_top = HANDOFF_REQUIRED_FIELDS - set(handoff.keys())
    if missing_top:
        errors.append(f"Missing top-level fields: {sorted(missing_top)}")

    task = handoff.get('task', {})
    if isinstance(task, dict):
        missing_task = HANDOFF_TASK_REQUIRED - set(task.keys())
        if missing_task:
            errors.append(f"task missing fields: {sorted(missing_task)}")
    else:
        errors.append("'task' must be a dict with 'skill' and 'description'")

    ctx = handoff.get('context_files', [])
    if not isinstance(ctx, list):
        errors.append("'context_files' must be a list")
    elif len(ctx) == 0:
        errors.append("'context_files' must not be empty — a resuming session needs at least one file")
    else:
        for i, entry in enumerate(ctx):
            if not isinstance(entry, dict):
                errors.append(f"context_files[{i}]: must be a dict")
                continue
            missing_cf = HANDOFF_CTX_FILE_REQUIRED - set(entry.keys())
            if missing_cf:
                errors.append(f"context_files[{i}] missing: {sorted(missing_cf)}")
            depth = entry.get('depth')
            if depth and depth not in HANDOFF_VALID_DEPTHS:
                errors.append(f"context_files[{i}] depth '{depth}' not in {HANDOFF_VALID_DEPTHS}")

    ws = handoff.get('working_state', {})
    if isinstance(ws, dict):
        if 'next' not in ws:
            errors.append("working_state must include 'next' (what the resuming session should do)")
        elif not ws['next']:
            errors.append("working_state.next must not be empty — resuming session needs at least one item")
    else:
        errors.append("'working_state' must be a dict")

    owns = handoff.get('owns', None)
    if owns is not None:
        if not isinstance(owns, list) or len(owns) == 0:
            errors.append("'owns' must be a non-empty list of file paths/globs — required for conflict detection")

    return errors


def write_handoff(handoff: dict, extra_additions: list = None) -> str:
    """
    Write or update a handoff file at handoffs/<id>.yaml.

    Validates schema, adds timestamps, commits to GitHub.
    Returns commit OID.

    The handoff dict must contain at minimum:
      id, task, context_files, working_state, last_commit

    Optional fields:
      owns (list of glob patterns), key_values (list), blockers (list),
      session_token, scope
    """
    import yaml
    from datetime import datetime, timezone

    errors = _validate_handoff_schema(handoff)
    if errors:
        raise RuntimeError(
            f"[HANDOFF BLOCKED] Schema validation failed:\n"
            + "\n".join(f"  - {e}" for e in errors)
        )

    hid = handoff['id']
    if '/' in hid or '\\' in hid or ' ' in hid:
        raise RuntimeError(f"[HANDOFF BLOCKED] id must be a simple slug, got: '{hid}'")

    now = datetime.now(timezone.utc).isoformat()
    handoff.setdefault('created', now)
    handoff['updated'] = now
    handoff.setdefault('status', 'active')
    handoff.setdefault('key_values', [])
    handoff.setdefault('blockers', [])

    path = f"{HANDOFF_DIR}/{hid}.yaml"
    content = yaml.safe_dump(handoff, default_flow_style=False,
                             sort_keys=False, allow_unicode=True)

    additions = [(path, content)]
    if extra_additions:
        additions.extend(extra_additions)

    auth = _authorize_next_commit()
    oid = atomic_commit(
        additions=additions, deletions=[],
        message=f"[infrastructure] handoff write — {hid}",
        repo='ttrpg', _auth=auth,
    )
    print(f"[HANDOFF ✓] Written: {path} → {oid}")
    print_resumption_block(hid)
    return oid


def print_resumption_block(handoff_id: str) -> None:
    """
    Print a self-contained copy-paste block for resuming a handoff in a new session.

    Called automatically by write_handoff(). Also callable standalone when you
    need to regenerate the block for an existing handoff.

    The printed block:
      - bootstraps github_ops + valoria_hooks from repo
      - calls g.load_handoff_context(handoff_id) to fetch all context_files
      - prints a status summary (task, completed, next, key_values, blockers)
      - does NOT start a new session log (that is the operator's decision)
    """
    block = f'''
# ─────────────────────────────────────────────────────────
# VALORIA HANDOFF RESUME — {handoff_id}
# Paste this entire block as your first message in a new chat.
# ─────────────────────────────────────────────────────────
bootstrap {handoff_id}

```python
python3 - <<\'RESUME\'
import os, sys, time, urllib.request, json, base64

PAT = open(\'/mnt/project/VALORIA_PAT\').read().strip()
os.environ[\'GITHUB_PAT\'] = PAT
open(\'/home/claude/.valoria_pat\', \'w\').write(PAT)
REPO = \'jordanelias/ttrpg\'
HANDOFF_ID = \'{handoff_id}\'

SCRIPTS = [
    (\'skills/valoria-orchestrator/scripts/github_ops.py\',  \'/home/claude/github_ops.py\'),
    (\'skills/valoria-orchestrator/scripts/valoria_hooks.py\', \'/home/claude/valoria_hooks.py\'),
]
for src, dst in SCRIPTS:
    if os.path.exists(dst) and (time.time() - os.path.getmtime(dst)) < 3600:
        continue
    req = urllib.request.Request(
        f\'https://api.github.com/repos/{{REPO}}/contents/{{src}}?ref=main\',
        headers={{\'Authorization\': f\'token {{PAT}}\', \'Accept\': \'application/vnd.github.v3+json\'}}
    )
    with urllib.request.urlopen(req) as r:
        open(dst, \'w\').write(base64.b64decode(json.loads(r.read())[\'content\']).decode())

sys.path.insert(0, \'/home/claude\')
import github_ops as g, valoria_hooks as h

g.read_files_graphql([\'session_log_current.md\'], skip_health_check=True)
token = h.assert_bootstrap()

result = g.load_handoff_context(HANDOFF_ID)
handoff = result[\'handoff\']
files   = result[\'files\']

print()
print(\'=\' * 55)
print(f\'RESUMING: {{HANDOFF_ID}}\')
print(\'=\' * 55)
print(f\'Task:     {{handoff["task"]["description"]}}\')
print(f\'Skill:    {{handoff["task"]["skill"]}}\')
ws = handoff.get(\'working_state\', {{}})
completed  = ws.get(\'completed\',  [])
in_progress = ws.get(\'in_progress\', [])
next_items = ws.get(\'next\',       [])
if completed:
    print(\'\\nCompleted:\')
    for item in completed:
        print(f\'  ✓ {{item}}\')
if in_progress:
    print(\'\\nIn progress:\')
    for item in in_progress:
        print(f\'  ► {{item}}\')
print(\'\\nNext:\')
for i, item in enumerate(next_items, 1):
    print(f\'  {{i}}. {{item}}\')
kv = handoff.get(\'key_values\', [])
if kv:
    print(\'\\nKey values:\')
    for item in kv:
        print(f\'  — {{item}}\')
blockers = handoff.get(\'blockers\', [])
if blockers:
    print(\'\\nBlockers:\')
    for b in blockers:
        print(f\'  ⚠  {{b}}\')
last = handoff.get(\'last_commit\')
if last:
    print(f\'\\nLast commit: {{last}}\')
print(f\'\\nContext loaded: {{len(files)}} file(s)\')
missing = [cf[\'path\'] for cf in handoff.get(\'context_files\', [])
           if cf[\'path\'] not in files]
if missing:
    print(f\'Missing files: {{missing}}\')
print(\'=\' * 55)
print(f\'Session token: {{token}}\')
print(\'\\nContext files now in memory. Confirm task or send new instructions.\')
print(\'=\' * 55)
RESUME
```'''

    print(block)


def read_all_handoffs() -> list:
    """
    Read all active handoff files from handoffs/ directory.
    Returns list of (id, parsed_dict) tuples, sorted by updated desc.
    """
    import yaml

    try:
        names = list_directory(HANDOFF_DIR, repo='ttrpg')
    except Exception:
        return []

    yaml_names = [n for n in names if n.endswith('.yaml')]
    if not yaml_names:
        return []

    paths = [f"{HANDOFF_DIR}/{n}" for n in yaml_names]
    files = read_files_graphql(paths, repo='ttrpg', skip_health_check=True)

    handoffs = []
    for path, content in files.items():
        if content is None:
            continue
        try:
            parsed = yaml.safe_load(content)
            if isinstance(parsed, dict) and parsed.get('status') == 'active':
                handoffs.append((parsed.get('id', path), parsed))
        except Exception:
            print(f"[HANDOFF WARN] Could not parse {path}")

    handoffs.sort(key=lambda x: x[1].get('updated', ''), reverse=True)
    return handoffs


def archive_handoff(handoff_id: str, extra_additions: list = None) -> str:
    """
    Archive a handoff: move from handoffs/<id>.yaml to archives/handoffs/<id>_<date>.yaml.
    Sets status to 'closed'. Returns commit OID.
    """
    import yaml
    from datetime import datetime, timezone

    path = f"{HANDOFF_DIR}/{handoff_id}.yaml"

    try:
        files = read_files_graphql([path], repo='ttrpg', skip_health_check=True)
    except Exception:
        raise RuntimeError(f"[HANDOFF BLOCKED] Cannot read {path}")

    content = files.get(path)
    if content is None:
        raise RuntimeError(f"[HANDOFF BLOCKED] {path} does not exist — cannot archive")

    try:
        parsed = yaml.safe_load(content)
    except Exception as e:
        raise RuntimeError(f"[HANDOFF BLOCKED] Cannot parse {path}: {e}")

    parsed['status'] = 'closed'
    parsed['closed_at'] = datetime.now(timezone.utc).isoformat()
    date_str = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    archive_path = f"{HANDOFF_ARCHIVE_DIR}/{handoff_id}_{date_str}.yaml"

    closed_content = yaml.safe_dump(parsed, default_flow_style=False,
                                    sort_keys=False, allow_unicode=True)

    additions = [(archive_path, closed_content)]
    if extra_additions:
        additions.extend(extra_additions)

    auth = _authorize_next_commit()
    oid = atomic_commit(
        additions=additions, deletions=[path],
        message=f"[infrastructure] handoff close — {handoff_id}",
        repo='ttrpg', _auth=auth,
    )
    print(f"[HANDOFF ✓] Archived: {path} → {archive_path} → {oid}")
    return oid


def check_handoff_conflicts(proposed_paths: list) -> list:
    """
    Check if proposed file paths conflict with active handoffs' owns fields.
    Uses fnmatch glob matching.

    Returns list of (path, conflicting_handoff_id) tuples.
    Empty = no conflicts.
    """
    from fnmatch import fnmatch

    handoffs = read_all_handoffs()
    if not handoffs:
        return []

    conflicts = []
    for proposed in proposed_paths:
        for hid, hdata in handoffs:
            for pattern in hdata.get('owns', []):
                if fnmatch(proposed, pattern):
                    conflicts.append((proposed, hid))
                    break

    return conflicts


def report_lane(lane_assignments_content: str = None) -> None:
    """Print the current session's lane line in the bootstrap Status Block (3-session mode).

    Lane is declared via env VALORIA_LANE=<A|B|C> or the marker file /home/claude/.valoria_lane.
    Degrades silently when no lane is declared (single-session mode) and gracefully when the
    spec is absent/unparseable — mirrors report_roadmap. Reads references/lane_assignments.yaml.
    """
    import os
    lane = os.environ.get('VALORIA_LANE')
    if not lane:
        try:
            with open('/home/claude/.valoria_lane') as _f:
                lane = _f.read().strip()
        except Exception:
            lane = None
    if not lane:
        return  # no lane declared — single-session mode, print nothing
    lane = lane.strip().upper()
    if not lane_assignments_content:
        print(f"\n[LANE {lane}] declared, but references/lane_assignments.yaml not found — run lane-spec setup (workplan 5.11).")
        return
    try:
        import yaml
        spec = yaml.safe_load(lane_assignments_content) or {}
    except Exception as e:
        print(f"\n[LANE {lane}] lane spec unparseable: {e}")
        return
    lanes = spec.get('lanes', {}) or {}
    info = lanes.get(lane) or lanes.get(lane.lower())
    if not info:
        print(f"\n[LANE {lane}] not defined in lane_assignments.yaml (defined: {sorted(lanes)}).")
        return
    owns = info.get('owns', []) or []
    items = info.get('entry_items', []) or []
    print(f"\nLANE {lane} — {info.get('name','')}")
    print(f"  owns ({len(owns)}): " + ", ".join(owns[:6]) + (" …" if len(owns) > 6 else ""))
    print(f"  reserved: ED {info.get('reserved_ed','?')} · PP {info.get('reserved_pp','?')}")
    print(f"  entry items: " + ", ".join(str(i) for i in items[:10]) + (" …" if len(items) > 10 else ""))
    if info.get('launch_ready') is False:
        print(f"  ⚠ launch_ready: FALSE — {info.get('launch_blocker','(see lane_assignments.yaml)')}")
    print(f"  boundary: write only inside owns; allocate IDs only from your reserved block; CollisionError -> re-fetch + retry.")


def report_roadmap(content: str = None) -> None:
    """
    Print the project's roadmap position in the bootstrap Status Block.

    Reads references/roadmap_state.yaml (passed in from the bootstrap fetch
    cache). Degrades gracefully if the file is absent or malformed — roadmap
    surfacing is informational, never blocking.
    """
    import yaml

    print()
    if not content:
        print("ROADMAP POSITION: not tracked (references/roadmap_state.yaml absent)")
        return
    try:
        rm = yaml.safe_load(content)
    except Exception as e:
        print(f"ROADMAP POSITION: unreadable (references/roadmap_state.yaml — {e})")
        return

    updated = rm.get('updated', '?')
    cur_id = rm.get('current_phase')
    phases = rm.get('phases', [])
    by_id = {p.get('id'): p for p in phases}

    print(f"ROADMAP POSITION (references/roadmap_state.yaml · updated {updated}):")

    cur = by_id.get(cur_id)
    if cur:
        done = cur.get('items_done', 0)
        total = cur.get('items_total', '?')
        print(f"  \u25b8 CURRENT: Phase {cur_id} \u2014 {cur.get('name','?')} ({done}/{total} items done)")
        for na in (cur.get('next_actions') or [])[:5]:
            print(f"      next: {na}")
        extra = len(cur.get('next_actions') or []) - 5
        if extra > 0:
            print(f"      next: (+{extra} more)")

    done_phases = [p for p in phases if p.get('status') == 'complete']
    if done_phases:
        labels = [f"Phase {p['id']} ({p.get('items_done','?')}/{p.get('items_total','?')})" for p in done_phases]
        print(f"  \u2713 done: {', '.join(labels)}")

    todo = [p for p in phases if p.get('status') == 'not_started']
    if todo:
        labels = [f"P{p['id']} {p.get('name','?')}" for p in todo]
        print(f"  \u25e6 ahead: {'; '.join(labels)}")

    pend = rm.get('pending_decisions', [])
    if pend:
        ids = []
        for d in pend:
            ids.append(str(d).split(' \u2014 ')[0].split(' -')[0].strip())
        print(f"  \u2691 pending decisions: {', '.join(ids)}")
    print()


def report_handoffs(handoffs: list = None) -> None:
    """
    Print a status report of all active handoffs.
    Called during bootstrap to show what workstreams exist.
    """
    if handoffs is None:
        handoffs = read_all_handoffs()

    print()
    if not handoffs:
        print("ACTIVE HANDOFFS: none")
        return

    print(f"ACTIVE HANDOFFS ({len(handoffs)}):")
    for i, (hid, hdata) in enumerate(handoffs, 1):
        task = hdata.get('task', {})
        skill = task.get('skill', '?')
        desc = task.get('description', '?')
        owns = hdata.get('owns', [])
        blockers = hdata.get('blockers', [])
        ctx_count = len(hdata.get('context_files', []))
        updated = hdata.get('updated', '?')

        print(f"  {i}. {hid}")
        print(f"     skill: {skill} | context_files: {ctx_count}")
        print(f"     {desc}")
        if owns:
            print(f"     owns: {', '.join(owns[:5])}")
        if blockers:
            print(f"     blockers: {', '.join(str(b) for b in blockers[:3])}")
        print(f"     updated: {updated}")
    print()


def load_handoff_context(handoff_id: str) -> dict:
    """
    Read a specific handoff and fetch all its context_files.
    Returns dict with 'handoff' (parsed) and 'files' (path→content).

    This is what a resuming session calls after selecting a handoff.
    """
    import yaml

    path = f"{HANDOFF_DIR}/{handoff_id}.yaml"
    files = read_files_graphql([path], repo='ttrpg', skip_health_check=True)
    content = files.get(path)
    if content is None:
        raise RuntimeError(f"[HANDOFF] {path} not found — cannot load context")

    parsed = yaml.safe_load(content)
    ctx_files = parsed.get('context_files', [])

    if not ctx_files:
        return {'handoff': parsed, 'files': {}}

    # Group paths by repo (context_files may span ttrpg and valoria-game)
    by_repo: dict = {}
    for cf in ctx_files:
        repo = cf.get('repo', 'ttrpg')
        by_repo.setdefault(repo, []).append(cf['path'])

    fetched: dict = {}
    for repo, paths in by_repo.items():
        result = read_files_graphql(paths, repo=repo, skip_health_check=True)
        fetched.update(result)

    # Report what was loaded
    print(f"\n[HANDOFF] Loaded context for '{handoff_id}':")
    for cf in ctx_files:
        p = cf['path']
        depth = cf.get('depth', 'full')
        reason = cf.get('reason', '')
        repo = cf.get('repo', 'ttrpg')
        found = fetched.get(p) is not None
        status = '✓' if found else '✗ NOT FOUND'
        repo_tag = f' [{repo}]' if repo != 'ttrpg' else ''
        print(f"  {status}  {p} ({depth}){repo_tag} — {reason}")

    return {'handoff': parsed, 'files': fetched}
