"""
patch_propagation_checker.py — Valoria patch-to-params propagation validator.

Scans patch_register.yaml for patches that list params files in their
`files:` or `affects:` fields. Cross-checks whether each params file's
header comment includes that patch ID.

Usage:
    python3 tools/patch_propagation_checker.py              # check all
    python3 tools/patch_propagation_checker.py --from PP-200 # check PP-200+
    python3 tools/patch_propagation_checker.py --fix-report  # output fixable list

Requires: GITHUB_PAT environment variable
Exit codes:
    0 = all patches propagated to their listed params files
    1 = one or more patches missing from params headers
"""

import os, sys, re, json, base64, urllib.request, argparse

REPO_OWNER = "jordanelias"
REPO_NAME  = "ttrpg"
BRANCH     = "main"

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

def read_file(path):
    """Read a single file from GitHub via REST."""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{path}?ref={BRANCH}"
    req = urllib.request.Request(url, headers=_headers())
    try:
        with urllib.request.urlopen(req) as r:
            data = json.loads(r.read())
            return base64.b64decode(data["content"]).decode("utf-8")
    except Exception as e:
        print(f"[ERROR] Cannot read {path}: {e}")
        return None

# ── Parsing ────────────────────────────────────────────────────────────────────

def parse_patches(content, from_id=None):
    """
    Parse patch_register.yaml into list of dicts with keys:
    id, status, files (list of paths), description
    """
    patches = []
    current = {}
    for line in content.split("\n"):
        line_s = line.strip()

        # New patch block
        id_m = re.match(r'-?\s*id:\s*(PP-\d+)', line_s)
        if id_m:
            if current.get("id"):
                patches.append(current)
            current = {"id": id_m.group(1), "status": "applied", "files": [], "description": ""}
            continue

        if not current.get("id"):
            continue

        # Status
        status_m = re.match(r'status:\s*(\S+)', line_s)
        if status_m:
            current["status"] = status_m.group(1)
            continue

        # Description
        desc_m = re.match(r'description:\s*"?(.+?)"?\s*$', line_s)
        if desc_m:
            current["description"] = desc_m.group(1)
            continue

        # Files — YAML list
        files_m = re.match(r'files:\s*\[(.+)\]', line_s)
        if files_m:
            raw = files_m.group(1)
            current["files"] = [f.strip().strip("'\"") for f in raw.split(",")]
            continue

        # Files — YAML list item
        file_item_m = re.match(r'-\s*(references/params_\S+\.md)', line_s)
        if file_item_m:
            current["files"].append(file_item_m.group(1))
            continue

        # Affects field (alternate name)
        affects_m = re.match(r'affects:\s*\[(.+)\]', line_s)
        if affects_m:
            raw = affects_m.group(1)
            current["files"].extend([f.strip().strip("'\"") for f in raw.split(",")])

    if current.get("id"):
        patches.append(current)

    # Filter to params-affecting patches only
    params_patches = []
    for p in patches:
        params_files = [f for f in p["files"] if f.startswith("references/params_")]
        if params_files:
            p["params_files"] = params_files
            params_patches.append(p)

    # Apply --from filter
    if from_id:
        from_num = int(re.search(r'\d+', from_id).group())
        params_patches = [p for p in params_patches if int(re.search(r'\d+', p["id"]).group()) >= from_num]

    return params_patches

def check_params_header(params_content, patch_id):
    """Check if a params file mentions a patch ID — in header, range notation, or body sections."""
    if not params_content:
        return False

    # Direct mention anywhere in file (e.g. "### PP-203:" section)
    if patch_id in params_content:
        return True

    # Parse range notation in header (e.g. "PP-190–209" covers PP-190 through PP-209)
    patch_num = int(re.search(r'\d+', patch_id).group())
    header = "\n".join(params_content.split("\n")[:20])
    # Match ranges like PP-190–209, PP-190-209, PP-190–PP-209
    for m in re.finditer(r'PP-(\d+)[–\-]+(?:PP-)?(\d+)', header):
        lo, hi = int(m.group(1)), int(m.group(2))
        if lo <= patch_num <= hi:
            return True

    return False

# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Check patch propagation to params files")
    parser.add_argument("--from", dest="from_id", help="Check patches from this ID onward (e.g. PP-200)")
    parser.add_argument("--fix-report", action="store_true", help="Output machine-readable fix list")
    args = parser.parse_args()

    print("Loading patch_register.yaml...")
    pr_content = read_file("canon/patch_register.yaml")
    if not pr_content:
        print("[ERROR] Cannot read patch_register.yaml")
        sys.exit(1)

    patches = parse_patches(pr_content, from_id=args.from_id)
    print(f"Patches targeting params files: {len(patches)}")

    # Collect unique params files to read
    all_params = set()
    for p in patches:
        all_params.update(p["params_files"])

    print(f"Unique params files to check: {len(all_params)}")
    print()

    # Read all params files
    params_content = {}
    for pf in sorted(all_params):
        params_content[pf] = read_file(pf)

    # Check each patch
    missing = []  # (patch_id, status, params_file, description)
    found = 0

    for p in patches:
        for pf in p["params_files"]:
            content = params_content.get(pf)
            if content is None:
                missing.append((p["id"], p["status"], pf, f"FILE NOT FOUND — {p['description'][:60]}"))
            elif not check_params_header(content, p["id"]):
                missing.append((p["id"], p["status"], pf, p["description"][:80]))
            else:
                found += 1

    # Report
    print(f"{'='*70}")
    print(f"PATCH PROPAGATION CHECK")
    print(f"{'='*70}")
    print(f"  Propagated:     {found}")
    print(f"  Missing:        {len(missing)}")
    print()

    if missing:
        print("MISSING PROPAGATIONS:")
        print(f"{'Patch':<10} {'Status':<14} {'Params File':<40} Description")
        print(f"{'-'*10} {'-'*14} {'-'*40} {'-'*40}")
        for patch_id, status, pf, desc in sorted(missing):
            print(f"{patch_id:<10} {status:<14} {pf:<40} {desc}")

        if args.fix_report:
            print("\n\nFIX REPORT (machine-readable):")
            for patch_id, status, pf, desc in sorted(missing):
                print(f"FIX|{patch_id}|{status}|{pf}|{desc}")

        print(f"\n[FAILED] {len(missing)} patch(es) not reflected in params headers.")
        print("Run params propagation to fix.")
        sys.exit(1)
    else:
        print("[PASSED] All patches propagated to params files.")
        sys.exit(0)

if __name__ == "__main__":
    main()
