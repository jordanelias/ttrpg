"""
freshness_gate.py — Valoria canonical source freshness enforcer.

Detects drift between params files and the canonical documents they were
synced from. Uses canonical_sha__ fields in canonical_sources.yaml.

If the live HEAD SHA of a canonical doc differs from the recorded SHA,
the params file is stale and simulation/audit/patch is BLOCKED.

Usage:
    python3 tools/freshness_gate.py                      # check all systems
    python3 tools/freshness_gate.py --system combat      # check one system
    python3 tools/freshness_gate.py --update             # re-sync all SHAs after a commit

Requires: GITHUB_PAT environment variable
Exit codes:
    0 = all systems fresh
    1 = one or more stale — BLOCK simulation/audit/patch
    2 = canonical_sha fields missing — run --update first
"""

import os, sys, json, re, base64, urllib.request, argparse

REPO_OWNER = "jordanelias"
REPO_NAME  = "ttrpg"
BRANCH     = "main"
CANONICAL_SOURCES_PATH = "references/canonical_sources.yaml"

# ── GitHub helpers ─────────────────────────────────────────────────────────────

def _headers():
    pat = os.environ.get("GITHUB_PAT", "")
    if not pat:
        raise RuntimeError("GITHUB_PAT not set")
    return {"Authorization": f"token {pat}", "Accept": "application/vnd.github.v3+json"}

def _graphql(query, variables=None):
    payload = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=payload,
        headers={**_headers(), "Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

def get_blob_sha(path):
    """Return the current HEAD blob OID for a repo file. None if missing.

    Distinguishes API errors (rate limit, auth failure, network) from genuine
    file-not-found. API errors raise RuntimeError; only a successful query
    where the repo returns `object: null` yields None ("file truly absent").

    Background: prior implementation silently mapped any response without a
    populated `data.repository.object` field to None, which conflated
    rate-limit-induced empty responses with real 404s. That bug surfaced as
    spurious [MISSING] entries during freshness_gate scans run after heavy
    GraphQL usage. Fix: inspect response shape before defaulting to None.
    """
    q = """query($owner:String!,$name:String!,$expr:String!){
      repository(owner:$owner,name:$name){
        object(expression:$expr){...on Blob{oid}}
      }
    }"""
    result = _graphql(q, {"owner": REPO_OWNER, "name": REPO_NAME, "expr": f"HEAD:{path}"})

    # Detect API-level errors before interpreting empty data as "file missing"
    if "errors" in result:
        err_types = [e.get("type", "") for e in result["errors"]]
        err_msgs  = [e.get("message", "") for e in result["errors"]]
        if "RATE_LIMITED" in err_types or "RATE_LIMIT" in err_types or \
           any("rate limit" in m.lower() for m in err_msgs):
            raise RuntimeError(
                f"GitHub GraphQL rate limit hit while resolving HEAD:{path}. "
                f"Re-run after reset; do NOT trust missing-file reports from this scan."
            )
        raise RuntimeError(f"GraphQL error resolving HEAD:{path}: {result['errors']}")

    if "data" not in result:
        # No errors key but also no data — unexpected. Raise rather than
        # silently report missing.
        raise RuntimeError(
            f"GraphQL response missing 'data' for HEAD:{path}: {result}"
        )

    repo_obj = result["data"].get("repository")
    if repo_obj is None:
        # Repo itself unresolvable (auth issue, repo renamed, etc.) — not
        # a per-file missing condition.
        raise RuntimeError(
            f"GraphQL returned null repository for HEAD:{path}: {result}"
        )

    obj = repo_obj.get("object")
    # Only here does None genuinely mean "file does not exist at HEAD"
    return obj["oid"] if obj else None



# Public alias used by valoria_hooks.assert_bootstrap freshness check.
# Kept as a thin alias of get_blob_sha for API stability — callers use
# whichever name is more readable in context. Do not remove without
# updating callers (current caller: skills/valoria-orchestrator/scripts/valoria_hooks.py).
get_live_sha = get_blob_sha


def get_blob_shas_batch(paths):
    """Return {path: live_sha | None} for many paths via a single GraphQL call.

    Uses GraphQL aliases to batch N path queries into one request. Reduces
    bootstrap freshness-check cost from N GraphQL calls to 1.

    For N up to ~200 (typical canonical_sources.yaml size: ~110 pairs) this
    fits comfortably in a single GraphQL request and a single rate-limit
    point. For larger N, split into batches of 200; GraphQL rate-limit
    cost is per request, not per alias.

    Distinguishes API errors (rate limit, auth failure, network) from genuine
    file-not-found, matching the error-distinction pattern in get_blob_sha.
    API errors raise RuntimeError; only a successful query where the alias's
    `object` field is null yields None for that path ("file truly absent").

    Returns dict mapping every input path to its current HEAD blob OID
    (or None if the path doesn't exist on HEAD).
    """
    if not paths:
        return {}

    BATCH_SIZE = 200
    out = {}
    for batch_start in range(0, len(paths), BATCH_SIZE):
        batch = paths[batch_start:batch_start + BATCH_SIZE]
        aliases = {f"p{i}": p for i, p in enumerate(batch)}
        fields = "\n".join(
            f'  {alias}: object(expression: "HEAD:{p}") {{ ... on Blob {{ oid }} }}'
            for alias, p in aliases.items()
        )
        q = f"""query($owner:String!,$name:String!){{
          repository(owner:$owner,name:$name){{
        {fields}
          }}
        }}"""
        result = _graphql(q, {"owner": REPO_OWNER, "name": REPO_NAME})

        # Detect API-level errors before interpreting empty data as "files missing"
        if "errors" in result:
            err_types = [e.get("type", "") for e in result["errors"]]
            err_msgs  = [e.get("message", "") for e in result["errors"]]
            if "RATE_LIMITED" in err_types or "RATE_LIMIT" in err_types or \
               any("rate limit" in m.lower() for m in err_msgs):
                raise RuntimeError(
                    f"GitHub GraphQL rate limit hit during freshness batch "
                    f"({len(batch)} paths). Re-run after reset; do NOT trust "
                    f"missing-file reports from this scan."
                )
            raise RuntimeError(f"freshness batch GraphQL failed: {result['errors']}")

        if "data" not in result:
            raise RuntimeError(
                f"GraphQL response missing 'data' for freshness batch: {result}"
            )

        repo_obj = result["data"].get("repository")
        if repo_obj is None:
            raise RuntimeError(
                f"GraphQL returned null repository for freshness batch: {result}"
            )

        for alias, path in aliases.items():
            obj = repo_obj.get(alias)
            # Only here does None genuinely mean "file does not exist at HEAD"
            out[path] = obj["oid"] if obj else None
    return out


def get_file(path):
    """Return (content_str, rest_blob_sha) for a repo file."""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{path}?ref={BRANCH}"
    req = urllib.request.Request(url, headers=_headers())
    with urllib.request.urlopen(req) as r:
        data = json.loads(r.read())
    return base64.b64decode(data["content"]).decode("utf-8"), data["sha"]

def put_file(path, content, message, sha):
    """Commit a single file update. sha = REST blob SHA of current file."""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{path}"
    body = {
        "message": message,
        "content": base64.b64encode(content.encode("utf-8")).decode("ascii"),
        "branch": BRANCH,
        "sha": sha,
    }
    payload = json.dumps(body).encode()
    req = urllib.request.Request(url, data=payload,
                                  headers={**_headers(), "Content-Type": "application/json"})
    req.get_method = lambda: "PUT"
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

# ── Parsing helpers ────────────────────────────────────────────────────────────

# Matches any indented key-value where value is a repo path
_CANON_PATH_RE = re.compile(
    r'^(\s+)([a-z_]+):\s+((?:designs|params|compilation|canon|references|skills|tests)/[^\s#"\']+)'
)
# Matches sha lines:  canonical_sha__...: "40hexchars"
_SHA_LINE_RE = re.compile(
    r'^\s+(canonical_sha__[^:]+):\s+"([a-f0-9]{40})"'
)

def sha_key(path):
    return "canonical_sha__" + path.replace("/", "__").replace(".", "_")

def parse_canonical_pairs(content):
    """
    Return list of (path, recorded_sha_or_None) for every canonical path in the file.
    recorded_sha is None if the sha line is missing immediately after the path line.
    """
    lines = content.split("\n")
    pairs = []
    for i, line in enumerate(lines):
        m = _CANON_PATH_RE.match(line)
        if not m:
            continue
        path = m.group(3).strip()
        recorded_sha = None
        if i + 1 < len(lines):
            sha_m = _SHA_LINE_RE.match(lines[i + 1])
            if sha_m:
                recorded_sha = sha_m.group(2)
        pairs.append((path, recorded_sha))
    return pairs

def inject_shas(content, path_to_sha):
    """
    Insert/update canonical_sha__ lines after every canonical path line.
    Returns updated content string.
    """
    lines = content.split("\n")
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        new_lines.append(line)
        m = _CANON_PATH_RE.match(line)
        if m:
            indent = m.group(1)
            path = m.group(3).strip()
            if path in path_to_sha and path_to_sha[path]:
                key = sha_key(path)
                sha_line = f'{indent}{key}: "{path_to_sha[path]}"'
                next_line = lines[i + 1] if i + 1 < len(lines) else ""
                if key in next_line:
                    # Replace existing sha line
                    new_lines.append(sha_line)
                    i += 1  # consume old sha line
                else:
                    new_lines.append(sha_line)
        i += 1
    return "\n".join(new_lines)

# ── Check mode ─────────────────────────────────────────────────────────────────

def run_check(system_filter=None):
    print("Loading canonical_sources.yaml...")
    content, _ = get_file(CANONICAL_SOURCES_PATH)

    if system_filter:
        sys_idx = content.find(f"  {system_filter}:")
        if sys_idx < 0:
            print(f"[ERROR] System '{system_filter}' not found in canonical_sources.yaml")
            sys.exit(1)
        # Find where the next top-level system key begins (two-space indent + word + colon)
        remaining = content[sys_idx + len(system_filter) + 3:]
        next_sys = re.search(r'\n  \w[^:\n]+:', remaining)
        end_idx = sys_idx + len(system_filter) + 3 + next_sys.start() if next_sys else len(content)
        block = content[sys_idx:end_idx]
        pairs = parse_canonical_pairs(block)
    else:
        pairs = parse_canonical_pairs(content)

    if not pairs:
        print("[ERROR] No canonical paths found. File may be malformed.")
        sys.exit(1)

    print(f"\n=== FRESHNESS GATE {'(' + system_filter + ')' if system_filter else '(all systems)'} ===\n")

    fresh, stale, no_sha = [], [], []

    for path, recorded_sha in pairs:
        live_sha = get_blob_sha(path)

        if live_sha is None:
            print(f"  [MISSING] {path} — not found on GitHub")
            stale.append(path)
        elif recorded_sha is None:
            print(f"  [NO-SHA]  {path} — canonical_sha field missing")
            no_sha.append(path)
        elif live_sha != recorded_sha:
            print(f"  [STALE]   {path}")
            print(f"            recorded: {recorded_sha[:16]}")
            print(f"            live:     {live_sha[:16]}  ← canonical doc has changed")
            stale.append(path)
        else:
            print(f"  [FRESH]   {path} @ {live_sha[:16]}")
            fresh.append(path)

    print(f"\n{'='*60}")
    print(f"  FRESH:  {len(fresh)}")
    print(f"  STALE:  {len(stale)}")
    print(f"  NO-SHA: {len(no_sha)}")

    if stale:
        print("\n[GATE FAILED] Stale canonical docs detected.")
        print("Simulation, audit, and patch on affected systems are BLOCKED.")
        print("Resolution:")
        print("  1. Read the updated canonical doc before proceeding.")
        print("  2. Re-sync params file if values have changed.")
        print("  3. Run: python3 tools/freshness_gate.py --update")
        print("  4. Re-run gate to confirm clean.")
        sys.exit(1)

    if no_sha:
        print("\n[GATE INCOMPLETE] SHA fields missing.")
        print("Run: python3 tools/freshness_gate.py --update")
        sys.exit(2)

    print("\n[GATE PASSED] All canonical sources are current.")
    sys.exit(0)

# ── Update mode ────────────────────────────────────────────────────────────────

def run_update():
    print("=== SHA UPDATE MODE ===")
    print("Fetching canonical_sources.yaml...")
    content, rest_sha = get_file(CANONICAL_SOURCES_PATH)

    pairs = parse_canonical_pairs(content)
    unique_paths = list(set(p for p, _ in pairs))
    print(f"Canonical paths found: {len(unique_paths)}\n")

    path_to_sha = {}
    for path in unique_paths:
        sha = get_blob_sha(path)
        path_to_sha[path] = sha
        print(f"  {path}: {sha[:16] if sha else 'NOT FOUND'}")

    missing = [p for p, s in path_to_sha.items() if not s]
    if missing:
        print(f"\n[WARN] {len(missing)} paths not found on GitHub:")
        for p in missing:
            print(f"  {p}")

    print("\nInjecting SHA fields...")
    updated = inject_shas(content, path_to_sha)
    sha_count = updated.count("canonical_sha__")
    print(f"canonical_sha__ fields in updated file: {sha_count}")

    print("Committing to GitHub...")
    # Prefer atomic_commit (hook-compatible) when github_ops is available
    try:
        sys.path.insert(0, "/home/claude")
        import github_ops as g
        g._load_cache()
        g.atomic_commit(
            additions=[(CANONICAL_SOURCES_PATH, updated)],
            deletions=[],
            message="[infrastructure] freshness_gate --update: sync canonical_sha fields",
        )
    except Exception:
        # Fallback: direct REST commit (CI environment, no github_ops)
        put_file(
            CANONICAL_SOURCES_PATH,
            updated,
            "[infrastructure] freshness_gate --update: sync canonical_sha fields",
            sha=rest_sha
        )
    print("\n[DONE] canonical_sources.yaml updated with current SHAs.")
    print("Run 'python3 tools/freshness_gate.py' to verify.")
    sys.exit(0)

# ── Entry point ────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Valoria canonical source freshness gate")
    parser.add_argument("--system", help="Check a single named system only")
    parser.add_argument("--update", action="store_true",
                        help="Re-sync all canonical_sha fields from live GitHub SHAs")
    args = parser.parse_args()

    if args.update:
        run_update()
    else:
        run_check(system_filter=args.system)

if __name__ == "__main__":
    main()
