"""
freshness_gate.py — Valoria canonical source freshness enforcer.

Detects drift between params files and the canonical documents they were
synced from. Uses canonical_sha__ fields in canonical_sources.yaml.

If the working-tree git blob SHA of a canonical doc differs from the recorded
SHA, the params file is stale and simulation/audit/patch is BLOCKED.

ED-1053: ported off the GitHub API to the LOCAL WORKING TREE. It used to resolve
each canonical doc's blob OID from remote `main` via GraphQL (and re-sync pins FROM
GitHub on --update), requiring GITHUB_PAT — so it validated remote main, not the
checkout, directly contradicting CLAUDE.md's working-tree rule, and its --update path
was dead (hardcoded /home/claude github_ops). It now computes the git blob OID of the
local file and --update rewrites the pins from local SHAs in place (no commit; the
caller commits).

EOL normalization (2026-07-01): the blob OID is computed over LF-normalized bytes
(CRLF→LF, honoring core.autocrlf) so it equals the OID git actually commits and stores,
regardless of whether the working-tree checkout has CRLF line endings (Windows) or LF
(Linux/CI). Earlier this hashed the raw on-disk bytes, so a CRLF checkout produced a
CRLF-byte SHA that only matched a pin generated on that same CRLF checkout — and read
STALE on any LF/CI checkout. Pins must be git-hash-object OIDs; do not hash raw CRLF.

Usage:
    python3 tools/freshness_gate.py                      # check all systems
    python3 tools/freshness_gate.py --system combat      # check one system
    python3 tools/freshness_gate.py --update             # re-sync all SHAs from the working tree

Exit codes:
    0 = all systems fresh
    1 = one or more stale — BLOCK simulation/audit/patch
    2 = canonical_sha fields missing — run --update first
"""

import os, sys, re, hashlib, argparse

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
CANONICAL_SOURCES_PATH = "references/canonical_sources.yaml"

# ── Working-tree blob SHA (git hash-object equivalent) ──────────────────────────

def _looks_binary(data: bytes) -> bool:
    """git treats a blob with a NUL byte as binary and does NOT EOL-normalize it."""
    return b"\0" in data


def _normalize_eol(data: bytes) -> bytes:
    """CRLF→LF normalization matching git's autocrlf-on-commit behavior for text blobs.
    Binary blobs (containing NUL) are left byte-exact, as git does."""
    if _looks_binary(data):
        return data
    return data.replace(b"\r\n", b"\n")


def _blob_sha_bytes(data: bytes) -> str:
    """git blob OID of the given bytes: sha1(b'blob <len>\\0' + LF-normalized data).

    LF-normalizes first (CRLF→LF for text) so the result equals the blob OID git
    actually commits and `git hash-object` reports — on both CRLF (Windows) and LF
    (Linux/CI) checkouts. It is therefore directly comparable to the canonical_sha__
    pins, which are git-hash-object OIDs. Do NOT feed raw CRLF disk bytes to git's
    blob-header formula; that yields a checkout-specific SHA that reads STALE on CI."""
    norm = _normalize_eol(data)
    h = hashlib.sha1()
    h.update(b"blob " + str(len(norm)).encode() + b"\0" + norm)
    return h.hexdigest()


def get_blob_sha(path):
    """Return the working-tree git blob OID for a repo-relative file. None if missing."""
    try:
        with open(os.path.join(REPO_ROOT, path), "rb") as f:
            return _blob_sha_bytes(f.read())
    except (FileNotFoundError, IsADirectoryError, OSError):
        return None


# Public alias kept for API stability (thin alias of get_blob_sha).
get_live_sha = get_blob_sha


def get_blob_shas_batch(paths):
    """Return {path: blob_sha | None} for many paths (local — no batching needed)."""
    return {p: get_blob_sha(p) for p in (paths or [])}


def get_file(path):
    """Return (content_str, blob_sha) for a repo file read from the working tree."""
    with open(os.path.join(REPO_ROOT, path), "rb") as f:
        raw = f.read()
    return raw.decode("utf-8"), _blob_sha_bytes(raw)

# ── Parsing helpers ────────────────────────────────────────────────────────────

# Matches any indented key-value where value is a repo path
# Prefix allow-list MUST track the live repo map — the ED-IN-0071 restructure (2026-07-16..19)
# moved canonical content into systems/ engine/ registers/ arcs/, and the pre-restructure regex
# (designs|params|compilation|canon|references|skills|tests only) silently matched just ~4% of the
# 133 pins, passing the BLOCKING gate green while blind to the rest (ED-IN-0077 freshness review).
_CANON_PATH_RE = re.compile(
    r'^(\s+)([a-z_]+):\s+((?:designs|params|compilation|canon|references|skills|tests'
    r'|systems|engine|registers|arcs)/[^\s#"\']+)'
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
            print(f"  [MISSING] {path} — not found in working tree")
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
        print(f"\n[WARN] {len(missing)} paths not found in working tree:")
        for p in missing:
            print(f"  {p}")

    print("\nInjecting SHA fields...")
    updated = inject_shas(content, path_to_sha)
    sha_count = updated.count("canonical_sha__")
    print(f"canonical_sha__ fields in updated file: {sha_count}")

    print("Writing canonical_sources.yaml in the working tree...")
    with open(os.path.join(REPO_ROOT, CANONICAL_SOURCES_PATH), "w", encoding="utf-8") as f:
        f.write(updated)
    print("\n[DONE] canonical_sources.yaml updated with current working-tree SHAs.")
    print("Review and commit it yourself; then run 'python3 tools/freshness_gate.py' to verify.")
    sys.exit(0)

# ── Entry point ────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Valoria canonical source freshness gate")
    parser.add_argument("--system", help="Check a single named system only")
    parser.add_argument("--update", action="store_true",
                        help="Re-sync all canonical_sha fields from the working tree")
    args = parser.parse_args()

    if args.update:
        run_update()
    else:
        run_check(system_filter=args.system)

if __name__ == "__main__":
    main()
