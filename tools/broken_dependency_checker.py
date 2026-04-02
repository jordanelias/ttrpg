"""
broken_dependency_checker.py — Valoria repository integrity scanner.
Scans the propagation map and canonical_sources for references to files
that do not exist in the repository. Runs against live GitHub tree.

Usage:
    python3 broken_dependency_checker.py

Requires: GITHUB_PAT environment variable
Output: prints broken dependencies; exits 1 if any found.
"""

import os, sys, json, re, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../')

REPO_OWNER = "jordanelias"
REPO_NAME  = "ttrpg"
BRANCH     = "main"

def get_headers():
    pat = os.environ.get("GITHUB_PAT", "")
    if not pat:
        raise RuntimeError("GITHUB_PAT not set")
    return {"Authorization": f"token {pat}", "Accept": "application/vnd.github.v3+json"}

def graphql(query, variables=None):
    payload = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=payload,
        headers={**get_headers(), "Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

def get_all_repo_files():
    """Return set of all file paths in the repo via GraphQL tree."""
    q = """
    query($owner: String!, $name: String!) {
      repository(owner: $owner, name: $name) {
        object(expression: "HEAD:") {
          ... on Tree {
            entries { name type object { ... on Tree { entries { name type } } } }
          }
        }
      }
    }
    """
    # Use REST for recursive tree — simpler
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/git/trees/{BRANCH}?recursive=1"
    req = urllib.request.Request(url, headers=get_headers())
    with urllib.request.urlopen(req) as r:
        data = json.loads(r.read())
    return {item["path"] for item in data.get("tree", []) if item["type"] == "blob"}

def read_file(path):
    """Read a file from GitHub."""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{path}?ref={BRANCH}"
    req = urllib.request.Request(url, headers=get_headers())
    try:
        with urllib.request.urlopen(req) as r:
            import base64
            data = json.loads(r.read())
            return base64.b64decode(data["content"]).decode()
    except Exception:
        return None

def extract_file_refs(content, source_file=""):
    """Extract all file path references from a markdown/yaml document."""
    refs = set()
    patterns = [
        r'`((?:designs|compilation|references|canon|tests|skills|tools)/[^`\s]+\.(?:md|yaml|py|json))`',
        r'"((?:designs|compilation|references|canon|tests|skills|tools)/[^"\s]+\.(?:md|yaml|py|json))"',
        r"'((?:designs|compilation|references|canon|tests|skills|tools)/[^'\s]+\.(?:md|yaml|py|json))'",
        r'(?:canonical|source_file|path|affects):\s*((?:designs|compilation|references|canon|tests|skills|tools)/\S+\.(?:md|yaml|py|json))',
    ]
    for pat in patterns:
        for m in re.finditer(pat, content):
            path = m.group(1).strip()
            if path and not path.startswith("#"):
                refs.add(path)
    return refs

def check_propagation_map(all_files):
    """Check propagation_map.md for broken references."""
    content = read_file("references/propagation_map.md")
    if not content:
        return [], ["references/propagation_map.md not found"]
    refs = extract_file_refs(content, "propagation_map.md")
    broken = [r for r in refs if r not in all_files]
    return broken, []

def check_canonical_sources(all_files):
    """Check canonical_sources.yaml for broken references."""
    content = read_file("references/canonical_sources.yaml")
    if not content:
        return [], ["references/canonical_sources.yaml not found"]
    refs = extract_file_refs(content, "canonical_sources.yaml")
    broken = [r for r in refs if r not in all_files]
    return broken, []

def check_skill_registry(all_files):
    """Check skill_registry.md for broken skill paths."""
    content = read_file("skills/valoria-orchestrator/references/skill_registry.md")
    if not content:
        return [], []
    refs = set()
    for m in re.finditer(r'Path:\s*`([^`]+)`', content):
        path = m.group(1).strip()
        if "/" in path:
            refs.add(path)
    broken = [r for r in refs if r not in all_files]
    return broken, []

def check_editorial_ledger(all_files):
    """Check editorial_ledger.yaml propagation_targets for broken paths."""
    content = read_file("canon/editorial_ledger.yaml")
    if not content:
        return [], []
    refs = extract_file_refs(content, "editorial_ledger.yaml")
    broken = [r for r in refs if r not in all_files]
    return broken, []

def main():
    print("Fetching repository file tree...")
    all_files = get_all_repo_files()
    print(f"Found {len(all_files)} files in repo")

    broken = {}
    errors = []

    checks = [
        ("propagation_map.md",    check_propagation_map),
        ("canonical_sources.yaml", check_canonical_sources),
        ("skill_registry.md",     check_skill_registry),
        ("editorial_ledger.yaml", check_editorial_ledger),
    ]

    for name, fn in checks:
        b, e = fn(all_files)
        if b:
            broken[name] = b
        errors.extend(e)

    if errors:
        print("\nERRORS (files not accessible):")
        for e in errors:
            print(f"  [ERROR] {e}")

    if broken:
        print("\nBROKEN DEPENDENCIES:")
        total = 0
        for source, refs in broken.items():
            print(f"\n  In {source}:")
            for r in sorted(refs):
                print(f"    [BROKEN] {r}")
                total += 1
        print(f"\nTotal broken: {total}")
        sys.exit(1)
    else:
        print("\nAll dependencies verified. No broken links found.")
        sys.exit(0)

if __name__ == "__main__":
    main()
