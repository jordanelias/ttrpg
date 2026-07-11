#!/usr/bin/env python3
"""
dashboard_data.py — assembles docs/dashboard/data.json for the Valoria GitHub
Pages dashboard (the mobile-friendly "what's been happening" view: workplan
progress, recent activity, audit/simulation verdicts, decisions needing Jordan,
CI health, open PR/issue counts).

Defensive by contract, mirroring workplan_status.py/session_status.py: each
section is wrapped independently (see `_safe`) so one bad parse produces an
"available: false" placeholder for that section instead of failing the whole
build — a partial dashboard beats a Pages deploy that silently freezes the last
successful build with no visible warning.

Local-only sections (workplan, audits, activity, currency, needs_decision) need
no network and run identically in CI or on a laptop. The `github`/`ci_health`
sections call the GitHub REST API directly via GITHUB_TOKEN (set by the Actions
step running this script — no actions/github-script needed, this stays plain
Python) and degrade to available:false when no token is present (e.g. local runs).

CLI: `python tools/dashboard_data.py [--out PATH]` writes the JSON and prints
the path. Importable: `from dashboard_data import build_all`.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

DEFAULT_OUT = os.path.join('docs', 'dashboard', 'data.json')
HANDOFF_ROOT = 'HANDOFF.md'
HANDOFFS_DIR = 'handoffs'
GITHUB_REPO_DEFAULT = 'jordanelias/ttrpg'

DECISION_MARKER_RE = re.compile(r'JORDAN RULING NEEDED|needs_jordan\s*[:=]\s*true', re.I)
COMMIT_SCOPE_RE = re.compile(r'^\[(\w+)\]')


def _safe(section_name, fn):
    try:
        return fn()
    except Exception as e:  # never let one section break the whole build
        print(f"WARN dashboard_data: section '{section_name}' failed: {e}", file=sys.stderr)
        return {"available": False, "error": str(e)}


# ── workplan ─────────────────────────────────────────────────────────────────

def build_workplan():
    import workplan_status as wps
    board = wps._load()
    if not board:
        return {"available": False, "reason": f"board missing/unreadable at {wps.BOARD}"}
    milestones = {}
    for mkey in ('M1', 'M2', 'M3'):
        ms = board.get('milestones', {}).get(mkey) or {}
        rows = wps._rows(ms)
        milestones[mkey] = {
            "label": ms.get('label', ''),
            "rows": [
                {
                    "key": str(r.get('n') or r.get('key') or ''),
                    "label": r.get('label', ''),
                    "state": r.get('state', 'not_started'),
                    "blocked_on": r.get('blocked_on'),
                    "next": r.get('next'),
                }
                for r in rows
            ],
        }
    return {
        "available": True,
        "as_of": board.get('as_of') or {},
        "summary_line": wps.summary_line(),
        "milestones": milestones,
        "decisions_t0_open": board.get('decisions_t0_open') or [],
        "last_progress": (board.get('last_progress') or [])[-5:],
        "staleness_warning": wps.staleness(),
    }


# ── audits/simulation-balance registry ──────────────────────────────────────

def build_audits():
    import audit_registry as ar
    entries = ar.summary()
    return {"available": True, "entries": entries, "count": len(entries)}


# ── recent activity (git log, grouped by [scope]) ───────────────────────────

def build_activity(limit=40):
    result = subprocess.run(
        ['git', 'log', f'-{limit}', '--date=short', '--pretty=format:%H|%ad|%an|%s'],
        capture_output=True, text=True, check=True,
    )
    commits = []
    for line in result.stdout.splitlines():
        parts = line.split('|', 3)
        if len(parts) != 4:
            continue
        sha, date, author, subject = parts
        m = COMMIT_SCOPE_RE.match(subject)
        commits.append({
            "sha": sha[:10],
            "date": date,
            "author": author,
            "subject": subject,
            "scope": m.group(1) if m else None,
        })
    return {"available": True, "commits": commits}


# ── currency drift ───────────────────────────────────────────────────────────

def build_currency():
    import currency_consistency_check as ccc
    return {"available": True, "summary": ccc.summary_line()}


# ── needs-your-decision inbox ────────────────────────────────────────────────

def _handoff_files():
    files = [HANDOFF_ROOT]
    if os.path.isdir(HANDOFFS_DIR):
        for fn in sorted(os.listdir(HANDOFFS_DIR)):
            if fn.startswith('HANDOFF_') and fn.endswith('.md'):
                files.append(os.path.join(HANDOFFS_DIR, fn))
    return [f for f in files if os.path.exists(f)]


def build_needs_decision():
    import workplan_status as wps
    board = wps._load() or {}
    items = [{"source": "workplan_t0", "line": None, "text": t}
             for t in (board.get('decisions_t0_open') or [])]

    for path in _handoff_files():
        with open(path, encoding='utf-8', errors='replace') as f:
            for lineno, line in enumerate(f, start=1):
                if DECISION_MARKER_RE.search(line):
                    items.append({"source": path, "line": lineno, "text": line.strip()[:300]})

    return {
        "available": True,
        "items": items,
        "count": len(items),
        # Heuristic prose scan, not a structured field read — a floor, not a
        # guarantee (see tools/audit_registry.py-adjacent plan notes). The UI
        # must surface this flag, not present the count as exhaustive.
        "heuristic": True,
    }


# ── GitHub API (network; only meaningful inside Actions with GITHUB_TOKEN) ──

def _gh_api(path, repo):
    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        raise RuntimeError('GITHUB_TOKEN not set (expected when running inside Actions)')
    req = urllib.request.Request(
        f'https://api.github.com/repos/{repo}{path}',
        headers={
            'Authorization': f'Bearer {token}',
            'Accept': 'application/vnd.github+json',
            'User-Agent': 'valoria-dashboard',
        },
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode('utf-8'))


def build_github():
    repo = os.environ.get('GITHUB_REPOSITORY', GITHUB_REPO_DEFAULT)
    prs = _gh_api('/pulls?state=open&per_page=100', repo)
    issues = _gh_api('/issues?state=open&per_page=100', repo)
    issue_only = [i for i in issues if 'pull_request' not in i]
    return {
        "available": True,
        "open_pr_count": len(prs),
        "open_issue_count": len(issue_only),
    }


# NOTE: matches job DISPLAY NAMES (the `name:` field), not the YAML job keys, since
# that's what the GitHub Actions "list jobs" API returns. If unit-tests/sim-regression/
# ci-summary's `name:` fields in .github/workflows/valoria-ci.yml are ever renamed,
# update JOB_NAME_* below in the same change — that workflow carries a matching
# cross-reference comment near those job definitions.
JOB_NAME_SUMMARY = 'All Gates Green'
JOB_NAME_UNIT_TESTS = 'Validator Unit Tests'
JOB_NAME_SIM_REGRESSION = 'Sim Reference Regression'


def build_ci_health():
    repo = os.environ.get('GITHUB_REPOSITORY', GITHUB_REPO_DEFAULT)
    runs = _gh_api(
        '/actions/workflows/valoria-ci.yml/runs?status=completed&per_page=1&branch=main', repo)
    workflow_runs = runs.get('workflow_runs') or []
    if not workflow_runs:
        return {"available": False, "reason": "no completed valoria-ci.yml runs found"}
    run = workflow_runs[0]
    jobs = _gh_api(f"/actions/runs/{run['id']}/jobs", repo)
    job_map = {j.get('name'): j.get('conclusion') for j in jobs.get('jobs', [])}
    return {
        "available": True,
        "run_id": run.get('id'),
        "commit_sha": (run.get('head_sha') or '')[:10],
        "run_html_url": run.get('html_url'),
        "conclusion_summary": job_map.get(JOB_NAME_SUMMARY),
        "conclusion_unit_tests": job_map.get(JOB_NAME_UNIT_TESTS),
        "conclusion_sim_regression": job_map.get(JOB_NAME_SIM_REGRESSION),
    }


# ── assembly ─────────────────────────────────────────────────────────────────

def _generated_at():
    sha = ''
    try:
        sha = subprocess.run(
            ['git', 'rev-parse', '--short', 'HEAD'],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    except Exception:
        pass
    return {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec='seconds'),
        "commit_sha": sha,
    }


def build_all():
    return {
        "generated_at": _generated_at(),
        "workplan": _safe('workplan', build_workplan),
        "audits": _safe('audits', build_audits),
        "activity": _safe('activity', build_activity),
        "currency": _safe('currency', build_currency),
        "needs_decision": _safe('needs_decision', build_needs_decision),
        "github": _safe('github', build_github),
        "ci_health": _safe('ci_health', build_ci_health),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', default=DEFAULT_OUT)
    args = parser.parse_args()

    data = build_all()
    os.makedirs(os.path.dirname(args.out) or '.', exist_ok=True)
    with open(args.out, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"wrote {args.out}")


if __name__ == '__main__':
    main()
