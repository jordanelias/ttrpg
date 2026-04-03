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
    """Return the current HEAD blob OID for a repo file. None if missing."""
    q = """query($owner:String!,$name:String!,$expr:String!){
      repository(owner:$owner,name:$name){
        object(expression:$expr){...on Blob{oid}}
      }
    }"""
    result = _graphql(q, {"owner": REPO_OWNER, "name": REPO_NAME, "expr": f"HEAD:{path}"})
    obj = result.get("data", {}).get("repository", {}).get("object")
    return obj.get("oid") if obj else None

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

# Matches canonical path lines:  canonical_*: some/path/file.md
_CANON_PATH_RE = re.compile(
    r'^(\s+)(canonical[^:\s]*?):\s+((?:designs|compilation|canon|references|skills|tests)/[^\s#"\']+)'
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
        next_sys_idx = content.find("\n  ", sys_idx + len(system_filter) + 3)
        block = content[sys_idx: next_sys_idx if next_sys_idx > 0 else len(content)]
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
