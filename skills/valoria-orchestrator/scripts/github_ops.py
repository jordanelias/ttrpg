"""
github_ops.py — Valoria GitHub operations
Single source of truth for all GitHub reads/writes.
Uses GraphQL createCommitOnBranch for atomic multi-file commits.

PAT must be set as environment variable: GITHUB_PAT
"""

import os, sys, json, base64, urllib.request, urllib.error

REPO_OWNER = "jordanelias"
REPO_NAME = "ttrpg"
BRANCH = "main"
API_BASE = "https://api.github.com"
GRAPHQL_URL = "https://api.github.com/graphql"


def _get_pat():
    pat = os.environ.get("GITHUB_PAT", "")
    if not pat:
        raise RuntimeError("GITHUB_PAT environment variable not set")
    return pat


def _headers():
    return {
        "Authorization": f"token {_get_pat()}",
        "Content-Type": "application/json",
        "Accept": "application/vnd.github.v3+json",
    }


def _get(path):
    url = f"{API_BASE}/repos/{REPO_OWNER}/{REPO_NAME}/contents/{path}"
    req = urllib.request.Request(url, headers=_headers())
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())


def _graphql(query, variables=None):
    payload = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request(GRAPHQL_URL, data=payload, headers=_headers())
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())


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


def read_file(path: str) -> str:
    d = _get(path)
    return base64.b64decode(d["content"]).decode("utf-8")


def read_files(paths: list) -> dict:
    return {p: read_file(p) for p in paths}


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
        d = _get(path)
        return d.get("size", 0)
    except urllib.error.HTTPError:
        return -1


def list_directory(path: str) -> list:
    items = _get(path)
    return [item["name"] for item in items if isinstance(item, dict)]


def atomic_commit(
    additions: list,   # list of (path, content_str)
    deletions: list,   # list of path strings
    message: str,
    expected_oid: str = None,
) -> str:
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
                fresh_oid = get_head_oid()
                variables["input"]["expectedHeadOid"] = fresh_oid
                result = _graphql(mutation, variables)
                if "errors" in result:
                    raise RuntimeError(f"Atomic commit failed after retry: {result['errors']}")
            else:
                raise RuntimeError(f"Atomic commit failed: {errs}")
        commit = result["data"]["createCommitOnBranch"]["commit"]
        return commit["oid"]
    except Exception as e:
        raise RuntimeError(f"Atomic commit error: {e}")


if __name__ == "__main__":
    print("Head OID:", get_head_oid())
    print("session_log_current.md size:", file_size("session_log_current.md"))
    print("tools/ contents:", list_directory("tools"))


def read_files_graphql(paths: list) -> dict:
    """Batch-read multiple files in a single GraphQL request."""
    if not paths:
        return {}
    # Build aliased fields: alias must be valid GraphQL identifier
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
    return {
        aliases[alias]: (repo[alias]["text"] if repo[alias] else None)
        for alias in aliases
    }
