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
import ast
import glob
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

import yaml

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


# ── balance/victory data (real numbers, not just a verdict chip) ───────────
#
# Research finding (2026-07-11): there is no consistent convention for where
# balance/victory data lives — every subsystem does it differently, and most
# subsystems have NO structured (non-prose) balance data at all. Per this
# corpus's anti-fabrication discipline (CLAUDE.md §7), only surface what
# genuinely exists on disk; say so plainly where it doesn't, rather than
# leaving a section silently empty or inventing a placeholder.

MORPHOLOGY_REARCH_CUTOFF = '2026-07-02'  # designs/audit/2026-07-02-morphology-rearch-phase0/
                                          # added 40 weapons; any weapon matrix dated before
                                          # this is stale and needs regeneration.


def _latest_weapon_rebalance_file():
    candidates = sorted(glob.glob(os.path.join('designs', 'audit', '*', 'weapon_rebalance_data.json')))
    if not candidates:
        return None
    # designs/audit/YYYY-MM-DD-slug/weapon_rebalance_data.json — sort by the folder's date prefix
    candidates.sort(key=lambda p: p.split(os.sep)[2][:10])
    return candidates[-1]


def build_balance_personal_combat():
    path = _latest_weapon_rebalance_file()
    if not path:
        return {"available": False, "reason": "no weapon_rebalance_data.json found under designs/audit/"}
    with open(path, encoding='utf-8') as f:
        raw = json.load(f)
    as_of = path.split(os.sep)[2][:10]
    field = (raw.get('weapon_audit') or {}).get('field') or {}
    top_sorted = sorted(field.items(), key=lambda kv: kv[1], reverse=True)
    return {
        "available": True,
        "source": path.replace(os.sep, '/'),
        "as_of": as_of,
        "stale": as_of < MORPHOLOGY_REARCH_CUTOFF,
        "stale_reason": (
            f"predates the {MORPHOLOGY_REARCH_CUTOFF} 40-weapon morphology expansion "
            "(designs/audit/2026-07-02-morphology-rearch-phase0/) — no regenerated matrix "
            "exists since; treat as historical, not current balance"
        ) if as_of < MORPHOLOGY_REARCH_CUTOFF else None,
        "field_win_rate_pct": dict(top_sorted),
    }


def _extract_module_dict_const(pyfile, varname):
    """AST-parse (never exec/eval arbitrary code) a module-level `NAME = {...}`
    literal out of a .py file — used to read the sim regression suite's own
    pinned golden constants, which ARE the corpus's current CI-checked balance
    baseline, without re-running the simulation ourselves."""
    with open(pyfile, encoding='utf-8') as f:
        tree = ast.parse(f.read(), filename=pyfile)
    for node in tree.body:
        if (isinstance(node, ast.Assign) and len(node.targets) == 1
                and isinstance(node.targets[0], ast.Name) and node.targets[0].id == varname):
            return ast.literal_eval(node.value)
    return None


def build_balance_faction_political():
    specs = [
        (os.path.join('sim', 'tests', 'test_mc_v18_regression.py'), 'seed 0, n=2 (fast regression oracle)'),
        (os.path.join('sim', 'tests', 'test_f7_smoke_oracle.py'), 'seed 42, n=8 (F7 smoke oracle)'),
    ]
    goldens = []
    for path, label in specs:
        if not os.path.exists(path):
            continue
        win_share = _extract_module_dict_const(path, 'GOLDEN_WIN_SHARE')
        if win_share is None:
            continue
        goldens.append({
            "source": path.replace(os.sep, '/'),
            "label": label,
            "win_share_pct": win_share,
        })
    if not goldens:
        return {"available": False, "reason": "no GOLDEN_WIN_SHARE constant found in sim/tests/"}
    return {
        "available": True,
        "kind": "CI-pinned regression goldens (sim/tests, run by the sim-regression CI job) — "
                "not a persisted full-campaign run",
        "goldens": goldens,
        # Correction, not the original claim: the widely-cited "~87% degenerate win-share"
        # (CLAUDE.md §7) was itself found to be a small-N artifact of one unguarded
        # run_batch(8, seed=42) — see test_f7_smoke_oracle.py's own docstring, which
        # debunks it and replaces it with these two guarded goldens. Don't repeat the
        # debunked framing; both goldens below are regression guards, not balance signal.
        "note": (
            "No n≥100 full-campaign balance run is persisted anywhere in the repo — these "
            "two small-n (2 and 8) goldens are CI regression guards against unintended drift, "
            "not a balance verdict at true campaign scale."
        ),
    }


NO_BALANCE_DATA_REASON = "no structured (non-prose) balance data exists for this subsystem yet"


def build_balance():
    return {
        "available": True,
        "personal_combat": _safe('balance.personal_combat', build_balance_personal_combat),
        "faction_political": _safe('balance.faction_political', build_balance_faction_political),
        "mass_battle": {
            "available": False,
            "reason": "no structured balance-matrix file exists (prose-only audits + hardcoded "
                      "test-digest constants in tests/sim/mass_battle/, not a data file)",
        },
        "social_contest": {"available": False, "reason": NO_BALANCE_DATA_REASON},
        "threadwork": {"available": False, "reason": NO_BALANCE_DATA_REASON},
        "settlement_territory": {"available": False, "reason": NO_BALANCE_DATA_REASON},
    }


# ── registers (editorial ledger + patch register — "what needs tending") ───

LEDGER_LANES = ['fa', 'fi', 'in', 'mb', 'pc', 'sc', 'se', 'wr']  # ED-<LANE>-NNNN taxonomy


def build_registers():
    by_lane = {'flat': {"open": 0, "needs_jordan": 0}}
    for lane in LEDGER_LANES:
        by_lane[lane] = {"open": 0, "needs_jordan": 0}
    total_open = 0
    total_needs_jordan = 0

    for fn in sorted(glob.glob(os.path.join('canon', 'editorial_ledger*.jsonl'))):
        base = os.path.basename(fn)
        if 'archive' in base:
            continue  # settled history, not live debt
        lane = 'flat'
        for L in LEDGER_LANES:
            if base == f'editorial_ledger_{L}.jsonl':
                lane = L
                break
        with open(fn, encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    entry = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if entry.get('status') == 'open':
                    by_lane[lane]['open'] += 1
                    total_open += 1
                if entry.get('needs_jordan'):
                    by_lane[lane]['needs_jordan'] += 1
                    total_needs_jordan += 1

    patch_active = {"total": 0, "by_status": {}}
    patch_path = os.path.join('canon', 'patch_register_active.yaml')
    if os.path.exists(patch_path):
        with open(patch_path, encoding='utf-8') as f:
            d = yaml.safe_load(f) or {}
        patches = d.get('patches') or []
        patch_active['total'] = len(patches)
        for p in patches:
            s = p.get('status', 'unknown')
            patch_active['by_status'][s] = patch_active['by_status'].get(s, 0) + 1

    return {
        "available": True,
        "editorial_ledger": {
            "total_open": total_open,
            "total_needs_jordan": total_needs_jordan,
            "by_lane": by_lane,
        },
        "patch_register_active": patch_active,
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
        "balance": _safe('balance', build_balance),
        "registers": _safe('registers', build_registers),
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
