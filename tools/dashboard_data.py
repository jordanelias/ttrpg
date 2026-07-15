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


# ── reconciliation / drift panel ─────────────────────────────────────────────
#
# Deterministic aggregation of the repo's existing staleness detectors — the
# "which maintained surface has fallen behind the work?" view. DETECTION ONLY:
# this section never edits a surface; it reports which ones drifted and the
# refresh route for each. That division is deliberate (the roadmap_state.yaml
# lesson, ED-IN-0006): a derived state surface must not be auto-written by an
# unattended job — machines detect, an agent proposes via PR, Jordan ratifies
# on merge (ED-1094). Every probe is independently guarded so one failure
# yields a skipped row, not a broken section (the _safe contract, one level in).

CURRENT_MD = 'CURRENT.md'
_RECONCILED_RE = re.compile(r'_Last reconciled:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})')


def _days_since(date_str):
    try:
        d = datetime.strptime(date_str[:10], '%Y-%m-%d').replace(tzinfo=timezone.utc)
        return (datetime.now(timezone.utc) - d).days
    except Exception:
        return None


def _drift_workplan_board():
    import workplan_status as wps
    warn = wps.staleness()
    as_of = (wps._load() or {}).get('as_of') or {}
    return [{
        "surface": "Workplan progress board",
        "category": "workplan",
        "ref": f"as_of {as_of.get('sha', '?')} ({as_of.get('date', '?')})",
        "stale": bool(warn),
        "detail": warn or "current — no workplan-relevant file changed since the last refresh",
        "refresh": "valoria-workplan-navigator (refresh-on-use) · tools/workplan_status.py --check",
    }]


def _drift_audit_families():
    import audit_staleness as ast_
    rows = []
    for st in (ast_.report() or []):
        drift = st.get('drift')
        rows.append({
            "surface": f"Audit family: {st.get('name', '?')}",
            "category": "audit-family",
            "ref": f"base {st.get('base_sha', '?')} ({st.get('base_date', '?')})",
            "stale": bool(drift),
            "detail": (f"{drift} in-scope file(s) changed since last refresh"
                       if drift else "current"),
            "refresh": "the family's owning regenerator · tools/audit_staleness.py --full",
        })
    return rows


def _drift_audit_registry():
    import ci_audit_registry_check as arc
    registry = arc._registry_entries()
    known = {r.get('folder') for r in registry if r.get('folder')}
    max_date = max((r.get('date', '') for r in registry), default='')
    if not max_date:
        return []
    unregistered = [f for d, f in arc._audit_dir_entries()
                    if d > max_date and f not in known]
    names = ", ".join(os.path.basename(f.rstrip('/')) for f in unregistered[:4])
    detail = (f"{len(unregistered)} audit folder(s) newer than the registry with no record"
              + (f": {names}" + (" …" if len(unregistered) > 4 else "") if names else "")
              ) if unregistered else "current — every recent audit folder has a registry record"
    return [{
        "surface": "Audit registry ↔ designs/audit/ folders",
        "category": "registry",
        "ref": f"latest registered {max_date}",
        "stale": bool(unregistered),
        "detail": detail,
        "refresh": "the owning audit skill's registry-append step · tools/ci_audit_registry_check.py",
    }]


def _drift_current_index(threshold_days=7):
    if not os.path.exists(CURRENT_MD):
        return []
    with open(CURRENT_MD, encoding='utf-8', errors='replace') as f:
        m = _RECONCILED_RE.search(f.read())
    if not m:
        return []
    date = m.group(1)
    days = _days_since(date)
    stale = days is not None and days > threshold_days
    detail = (f"last hand-reconciled {days} day(s) ago" if days is not None
              else f"last reconciled {date}") + (" — past the weekly reconcile cadence" if stale else "")
    return [{
        "surface": "CURRENT.md canonical index",
        "category": "index",
        "ref": f"last reconciled {date}",
        "stale": bool(stale),
        "detail": detail,
        "refresh": "monthly/weekly reconcile (workplan v6 §6) — human-ratified, never auto-written",
    }]


def _handoff_last_updated():
    # Informational (deliberately NOT counted as drift): a lane not being touched
    # is a cold lane, not a rotted derived surface. Surfaced so the panel shows
    # which continuity notes are going stale alongside the genuine drift rows.
    out = []
    for path in _handoff_files():
        r = subprocess.run(['git', 'log', '-1', '--date=short', '--format=%ad', '--', path],
                           capture_output=True, text=True)
        date = r.stdout.strip() if r.returncode == 0 else ''
        out.append({
            "surface": os.path.basename(path),
            "last_updated": date or "unknown",
            "days_ago": _days_since(date) if date else None,
        })
    return out


def build_drift():
    surfaces = []
    for probe in (_drift_workplan_board, _drift_audit_families,
                  _drift_audit_registry, _drift_current_index):
        try:
            surfaces.extend(probe() or [])
        except Exception as e:
            print(f"WARN dashboard_data: drift probe {probe.__name__} failed: {e}", file=sys.stderr)
    try:
        handoffs = _handoff_last_updated()
    except Exception:
        handoffs = []
    return {
        "available": True,
        "surfaces": surfaces,
        "stale_count": sum(1 for s in surfaces if s.get('stale')),
        "total": len(surfaces),
        "handoffs": handoffs,
        # Detection only — this panel never edits a surface; every refresh route
        # is a human/skill/PR action so the merge-ratifies gate stays in the loop.
        "note": "detection only — surfaces are refreshed by their owning skill/PR, never by this job",
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

# Lane roster — sourced from the shared observability core so every lane-aware
# surface agrees (fixes the prior GO omission that would misbucket editorial_ledger_go.jsonl).
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'observability'))
import obs_core as _obs_core  # noqa: E402  (distinct name — no sys.modules collision with combat's core.py)
LEDGER_LANES = list(_obs_core.LEDGER_LANE_CODES)  # ('mb','pc','fi','sc','fa','wr','in','go','se')


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


# ── categorized work queue (Claude-actionable vs needs-Jordan) ───────────────
#
# Deterministic read of the open editorial-ledger backlog, organized the way the
# North Star wants it: infrastructure → subsystem → simulation/testing → godot,
# each item split by whether it needs Jordan's ruling (needs_jordan) or is
# actionable without him. Lane comes free from the lane-split ledger filenames;
# the two cross-cutting overlays (sim/testing, godot) are keyword-detected.

LANE_NAMES = {
    'PC': 'personal combat', 'MB': 'mass battle', 'SC': 'social contest',
    'SE': 'settlement / territory', 'WR': 'world', 'FI': 'field investigation',
    'FA': 'faction / political', 'IN': 'infrastructure', 'GO': 'godot',
}
_SIM_RE = re.compile(r'\bsim/|sim_harness|mc_v18|\boracle\b|regression|\btests?/|harness', re.I)
_GODOT_RE = re.compile(r'godot|gdscript|\.gd\b|valoria-game', re.I)
CATEGORY_ORDER = ['infrastructure', 'subsystem', 'simulation', 'godot']
CATEGORY_LABELS = {
    'infrastructure': 'Infrastructure / cross-cutting',
    'subsystem': 'Subsystems',
    'simulation': 'Simulation & testing',
    'godot': 'Godot port',
}


def _ledger_open_entries():
    out = []
    for path in sorted(glob.glob('canon/editorial_ledger*.jsonl')):
        if 'archive' in path:
            continue
        m = re.search(r'editorial_ledger_([a-z]{2})\.jsonl$', path)
        lane = m.group(1).upper() if m else None
        with open(path, encoding='utf-8', errors='replace') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    e = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if e.get('status') != 'open':
                    continue
                out.append({
                    'id': e.get('id', '?'),
                    'lane': lane,
                    'desc': (e.get('description') or '').strip()[:240],
                    'source': e.get('source'),
                    'needs_jordan': bool(e.get('needs_jordan')),
                })
    return out


def _category_for(entry):
    text = f"{entry['desc']} {entry.get('source') or ''}"
    if entry['lane'] == 'GO' or _GODOT_RE.search(text):
        return 'godot'
    if entry['lane'] in ('PC', 'MB', 'SC', 'SE', 'WR', 'FI', 'FA'):
        return 'subsystem'
    if _SIM_RE.search(text):
        return 'simulation'
    return 'infrastructure'


def build_queue():
    entries = _ledger_open_entries()
    cats = {c: {} for c in CATEGORY_ORDER}
    for e in entries:
        c = _category_for(e)
        if c == 'subsystem':
            group = LANE_NAMES.get(e['lane'] or '', 'other')
        else:
            group = CATEGORY_LABELS[c]
        bucket = cats[c].setdefault(group, {'needs_jordan': [], 'actionable': []})
        item = {'id': e['id'], 'desc': e['desc'], 'source': e.get('source')}
        (bucket['needs_jordan'] if e['needs_jordan'] else bucket['actionable']).append(item)
    return {
        "available": True,
        "categories": cats,
        "category_order": CATEGORY_ORDER,
        "category_labels": CATEGORY_LABELS,
        "totals": {
            "needs_jordan": sum(1 for e in entries if e['needs_jordan']),
            "actionable": sum(1 for e in entries if not e['needs_jordan']),
            "open": len(entries),
        },
        "note": ("Open editorial-ledger items. “Needs your decision” = needs_jordan:true; "
                 "“Claude can action” = the remaining open items. The ledger is the source "
                 "of truth; a merge ratifies (ED-1094)."),
    }


# ── proposals / provisional / awaiting ratification ──────────────────────────

def build_proposals():
    # Status parsing via the shared core (tolerant superset regex). designs/proposals/
    # docs are surfaced BY LOCATION even without a Status line — the gap that made all
    # 9 of them invisible here. Both this card and build_proposals.py call the same core,
    # so they agree without one reading the other's committed output.
    rows = []
    for path in glob.glob('designs/**/*.md', recursive=True):
        if '/deprecated/' in path or '/archives/' in path or '/archive/' in path:
            continue
        try:
            with open(path, encoding='utf-8', errors='replace') as f:
                head = f.read(4000)
        except OSError:
            continue
        status = _obs_core.first_status(head)
        in_proposals_dir = path.startswith('designs/proposals/')
        if in_proposals_dir:
            shown = status or '(no Status line — designs/proposals/)'
            rows.append({"path": path, "status": shown[:140], "group": 'proposals'})
        elif _obs_core.is_unratified_status(status):
            group = path.split('/')[1] if path.count('/') >= 2 else 'designs'
            rows.append({"path": path, "status": status[:140], "group": group})
    rows.sort(key=lambda r: (r['group'], r['path']))
    groups = {}
    for r in rows:
        groups.setdefault(r['group'], []).append({"path": r['path'], "status": r['status']})
    return {
        "available": True,
        "groups": groups,
        "count": len(rows),
        "note": ("Docs whose first “## Status:” line reads PROPOSED / PROVISIONAL / DRAFT, plus "
                 "every doc under designs/proposals/ (surfaced by location). Awaiting ratification "
                 "(a doc-PR merge ratifies by default, ED-1094). Excludes deprecated/ and archives/. "
                 "The full unified register is tools/observability/PROPOSALS.md."),
    }


# ── repository shape (mermaid) ───────────────────────────────────────────────

def build_repo_shape():
    subdirs = sorted(os.path.basename(d) for d in glob.glob('designs/*') if os.path.isdir(d))
    lines = [
        'graph TD',
        '  CANON["canon/ — philosophy P-01..P-14 · ledgers · mechanics index"]',
        '  REF["references/ — registries · module_contracts · indices"]',
        '  DESIGN["designs/ — subsystem design docs"]',
        '  PARAMS["params/ — mechanical parameter tables"]',
        '  SIM["sim/ — Python oracle · 1:1 port reference"]',
        '  TOOLS["tools/ — CI checks · validators · generators"]',
        '  GODOT["Godot port — valoria-game · frozen 2026-05-04"]',
        '  CANON --> DESIGN',
        '  DESIGN --> PARAMS',
        '  PARAMS --> SIM',
        '  SIM --> GODOT',
        '  REF -.-> DESIGN',
        '  TOOLS -.-> CANON',
        '  subgraph SS["designs/ subsystems"]',
    ]
    for i, d in enumerate(subdirs):
        lines.append(f'    D{i}["{d}"]')
    lines.append('  end')
    lines.append('  DESIGN --> SS')
    return {
        "available": True,
        "mermaid": '\n'.join(lines),
        "subsystem_count": len(subdirs),
        "note": ("High-level repo structure: the layer spine (canon → design → params → "
                 "sim → godot) plus the designs/ subsystem folders (generated from disk)."),
    }


# ── keys & substrates reference (curated snapshot + live cross-check) ─────────
#
# Reference content transcribed from the architecture docs (2026-07-14). The
# volatile bit — the live count of registered key types — is re-extracted every
# build and cross-checked against the snapshot, so drift shows instead of hiding.

_KEY_REGISTRY_DOC = 'designs/architecture/key_type_registry_v30.md'


def _live_key_type_count():
    if not os.path.exists(_KEY_REGISTRY_DOC):
        return None
    n = 0
    with open(_KEY_REGISTRY_DOC, encoding='utf-8', errors='replace') as f:
        for line in f:
            if line.startswith('### ') and '.' in line:
                n += 1
    return n


def build_keys():
    families = [
        {"family": "scene_event", "count": 10,
         "types": "scene.dialogue, witness, gift, insult, threat, thread_operation*, draft_da*, displacement*, interaction, gossip"},
        {"family": "da_outcome", "count": 5,
         "types": "da.public_governance, covert_betrayal, diplomatic_alliance, antinomian_action, economic_intervention"},
        {"family": "mechanical_event", "count": 8,
         "types": "season_change, accounting, cascade_resolution, mission_shift, scene_entered/exited/skipped, project_advanced"},
        {"family": "state_transition", "count": 8,
         "types": "scar_acquired, standing_change, coup_attempted, succession, project_completed/failed, opinion_revised, concern_resolved"},
        {"family": "environmental", "count": 4,
         "types": "env.peninsular_strain_shock, crisis, disaster, population_change"},
        {"family": "scene_outcome", "count": 7,
         "types": "contest_resolved, battle_concluded, investigation_resolved, combat_resolved*, combat_strike*, combat_hit*, combat_felled*"},
        {"family": "system_meta", "count": 7,
         "types": "meta.knot_formed/ruptured, thread_woven, cascade_cluster_event, miraculous_event, belief_revised, legacy_event"},
    ]
    components = [
        {"name": "Key", "role": "The universal typed, validated, append-only event object (id/type/targets/scale_signature/symbolic_dimensions/…). No cascade_depth field."},
        {"name": "Target", "role": "One targets[] entry (actor, role, impact_vector, stat_deltas). Wide fan-out is ONE Key with N targets, never N Keys."},
        {"name": "KeyLog", "role": "The append-only canonical log — enforces all 8 universal invariants, deterministic serialize()/content_hash() for replay."},
        {"name": "TypeRegistry", "role": "Loads/validates against key_type_registry_v30.md at runtime (parses the markdown) instead of duplicating the roster in code."},
        {"name": "TickScheduler", "role": "The engine_clock-shaped emission seam — tick queue, cascade_depth re-entrancy meter, Level-B termination guard, deferred-apply at ACCOUNTING."},
        {"name": "TerminationBreach", "role": "Raised when a Level-B termination invariant is violated — never silently clamped."},
    ]
    propagation = [
        {"name": "Aggregate-up", "desc": "faction_stat has no setter: it is AGGREGATE(child stats) ⊕ Σ event-modifiers, a query over KEY_LOG. Domain Echoes defer-apply at the Accounting boundary (OF-7, ratified).", "source": "designs/architecture/propagation_spec_v1.md §2"},
        {"name": "Distribute-down", "desc": "A strategic/environmental Key reaching sub-scale actors must populate targets[] + scale_signature[] at emission. Fan-out is one Key, not N.", "source": "designs/architecture/propagation_spec_v1.md §3 (§12.3)"},
        {"name": "Termination", "desc": "Level A (per-tick fixpoint) and Level B (per-cascade bound) are PROVEN; cross-tick convergence is NOT — it waits on decay() (OF-3) and the D.6 disjointness ruling.", "source": "designs/architecture/propagation_spec_v1.md §4 (PROPOSED)"},
    ]
    live = _live_key_type_count()
    return {
        "available": True,
        "snapshot_date": "2026-07-14",
        "definition": ("Every consequential event is a Key — a typed, validated, append-only record. "
                       "One update rule consumes Keys and propagates effects. Save state = initial "
                       "conditions + Key log; replay = deterministic re-execution of the log."),
        "definition_source": "designs/architecture/key_substrate_v30.md §1",
        "families": families,
        "type_total": 49,
        "registry_source": _KEY_REGISTRY_DOC,
        "live_type_header_count": live,
        "count_check": ("current" if live in (None, 49) else f"registry now has {live} type headers vs snapshot 49 — refresh this section"),
        "components": components,
        "components_source": "sim/substrate/keys.py",
        "propagation": propagation,
        "conviction_axes": "hierarchical · sacred · instrumental · traditional (4-axis symbolic space)",
        "field_extension": {
            "name": "Field / Gauge (PROPOSED)",
            "desc": ("A Key is a one-shot emission — wrong for continuous VECTOR state (Legitimacy/PS, "
                     "Pressure Π, MS, Accord). The proposed Field primitive is a continuously-read/written "
                     "scale-tagged value with aggregate_fn / propagate_fn / decay_fn / derived_flags. Unblock = "
                     "Jordan ruling OF-3's decay() fork."),
            "source": "designs/architecture/governance_type_registry_v1.md §4.2",
        },
        "note": ("Reference snapshot (2026-07-14) with source links; the live key-type header count is "
                 "re-checked every build. See the source docs for canonical detail. Key substrate doc "
                 "carries a contradictory status marker (treat as IN FLUX)."),
    }


# ── character actions & interactions per subsystem (curated snapshot) ─────────

def build_actions():
    S = lambda name, avail, head, actions, caveat=None: {
        "name": name, "availability": avail, "source_head": head,
        "actions": [{"name": a, "desc": d, "source": s} for a, d, s in actions],
        "caveat": caveat}
    subsystems = [
        S("Personal combat", "partial (legacy menu)", "designs/scene/combat_engine_v1/",
          [("Strike", "Allocate pool split, roll, apply damage", "designs/scene/combat_v30.md §4"),
           ("Feint", "Commit dice to bait a pool-reduction contest", "designs/scene/combat_v30.md §4"),
           ("Establish Distance", "Move to preferred range, contested", "designs/scene/combat_v30.md §4"),
           ("Take a Breath", "Forfeit action to recover Stamina", "designs/scene/combat_v30.md §4"),
           ("Full Guard", "All dice to Defence, cannot Attack", "designs/scene/combat_v30.md §4"),
           ("Disarm", "Offence roll to force a weapon drop at Close", "designs/scene/combat_v30.md §4"),
           ("Tie Up / Escape", "Close grapple that blocks escape; Agility to break free", "designs/scene/combat_v30.md §4"),
           ("Rescue", "Reactive action redirecting an attack onto yourself", "designs/scene/combat_v30.md §4"),
           ("Dodge", "Forfeit offence, full pool as passive ranged defence", "designs/scene/combat_v30.md §4"),
           ("Stunt", "+dice to a Strike from environment/position", "designs/scene/combat_v30.md §4")],
          caveat="The current head (combat_engine_v1/) auto-resolves via a sigma state-machine — no player menu. The list above is the legacy combat_v30 §4 TTRPG menu (dice-math superseded); shown as the only enumerable player-facing set."),
        S("Social contest", "yes", "designs/scene/social_contest_v30.md",
          [("Appraise", "Read the audience/adjudicator before arguing", "designs/scene/social_contest_v30.md §4"),
           ("Choose Style", "Pick Precedent / Suppression / Vision / Insinuation", "designs/scene/social_contest_v30.md §4"),
           ("Corroborate", "A coalition member declares support for +1D", "designs/scene/social_contest_v30.md §4"),
           ("Argue", "Roll the Argue pool; CLASH / REINFORCE / CROSS / TIE", "designs/scene/social_contest_v30.md §4"),
           ("Regroup", "Forfeit exchange to restore Concentration", "designs/scene/social_contest_v30.md §4"),
           ("Concede a Point", "Forfeit, take strain, gain +1D next exchange", "designs/scene/social_contest_v30.md §4"),
           ("Pre-Contest Preparation", "Prepare for +1D on Exchange 1", "designs/scene/social_contest_v30.md §9.1"),
           ("Practitioner Weaving", "A Thread-sensitive orator adds bonus dice", "designs/scene/social_contest_v30.md §9.3")]),
        S("Mass battle", "yes", "designs/provincial/mass_battle_v30.md",
          [("Tactics", "Envelopment · Feigned Retreat · Ambush · Concentration · Refused Flank · Hammer & Anvil", "designs/provincial/mass_battle_v30.md §A.8"),
           ("General's turn action", "Rally · Reinforce Discipline · Support Threadweave · Personal combat · Stabilise general", "designs/provincial/mass_battle_v30.md §A.7"),
           ("Formations", "Line · Shield Wall · Wedge · Skirmish · Column · Feigned Retreat · Reserve", "designs/provincial/mass_battle_v30.md §A.6")]),
        S("Faction / domain actions", "yes (across 3 layers)", "params/factions/stats_1_7_scale.md",
          [("Domain Actions", "Assert · Reconstitute · Govern · Claim Masterless · Suppress · Parliamentary Rebuttal · Treaty · Accounting Stability Check", "params/factions/stats_1_7_scale.md"),
           ("Faction Unique Action", "One signature verb per faction (Royal Decree, Excommunication, Economic Leverage, …)", "params/factions/stats_1_7_scale.md"),
           ("Parliamentary motions", "Censure · Embargo · Blockade · Outlawry · Subsidy · War Authorisation · Treaty Ratification · Recognition Challenge · Succession Endorsement", "designs/provincial/faction_layer_v30.md §5.4")],
          caveat="The live sim (sim/provincial/faction_action.py) dispatches unique → Conquest → Muster → Govern each season; some code verbs (Crown Royal Progress/Great Work) are PROVISIONAL and differ from the ratified Royal Decree."),
        S("Settlements / territory", "yes (baseline + PROPOSED redesign)", "designs/territory/settlement_layer_v30.md",
          [("Governor (baseline)", "Develop · Fortify · Pacify · Administer", "designs/territory/settlement_layer_v30.md §3.2"),
           ("Governance verbs (PROPOSED)", "Develop · Fortify · Keep Order · Hold Court · Sponsor · Treat · Levy · Investigate", "designs/territory/governance_play_redesign_v1.md §1.3"),
           ("Petition / Defy", "Respond to the Provincial Authority's seasonal Directive", "designs/territory/governance_play_redesign_v1.md §1.4")],
          caveat="The 8-verb menu is a PROPOSAL (governance_play_redesign_v1) not yet ratified; the baseline §3.2 four-verb set is current."),
        S("Threadwork", "yes", "designs/threadwork/threadwork_v30.md",
          [("The Leap", "Suspend rendering to enter Thread contact (prerequisite)", "designs/threadwork/threadwork_v30.md §2.3"),
           ("Weaving", "“Things cohere” — stabilise/reinforce a configuration", "designs/threadwork/threadwork_v30.md §2.4"),
           ("Pulling", "“Things open” — loosen or reopen a configuration", "designs/threadwork/threadwork_v30.md §2.4"),
           ("Locking", "“Unable to become” — freeze a configuration", "designs/threadwork/threadwork_v30.md §2.4"),
           ("Dissolution", "“Unable to be” — tear a configuration apart", "designs/threadwork/threadwork_v30.md §2.4"),
           ("Mending", "Repair the substrate — the only Coherence-free operation", "designs/threadwork/threadwork_v30.md §2.4")]),
        S("Field investigation", "yes", "designs/scene/fieldwork_v30.md",
          [("Examine", "Study physical evidence, documents, objects", "designs/scene/fieldwork_v30.md §4.2"),
           ("Interview", "Question a witness — now routed via the Dialogue Lattice (ED-FI-0004)", "designs/scene/fieldwork_v30.md §4.2"),
           ("Research", "Consult archives, oral histories, records", "designs/scene/fieldwork_v30.md §4.2"),
           ("Surveil", "Observe a location/person/faction over time", "designs/scene/fieldwork_v30.md §4.2"),
           ("Thread-Read", "Perceive Thread configurations via a perceptive Leap", "designs/scene/fieldwork_v30.md §4.2"),
           ("Reconstruct", "Synthesise gathered evidence into a picture", "designs/scene/fieldwork_v30.md §4.2"),
           ("Social (non-contest)", "Read · Converse · Connect · Impress · Rumour · Negotiate · Gift/Bribe", "designs/scene/fieldwork_v30.md §5.2")]),
    ]
    return {
        "available": True,
        "snapshot_date": "2026-07-14",
        "subsystems": subsystems,
        "note": ("Player/character action vocabulary per subsystem — a reference snapshot (2026-07-14) "
                 "with source links. See each source doc (resolved via CURRENT.md) for canonical detail."),
    }


def build_all():
    return {
        "generated_at": _generated_at(),
        "workplan": _safe('workplan', build_workplan),
        "audits": _safe('audits', build_audits),
        "activity": _safe('activity', build_activity),
        "currency": _safe('currency', build_currency),
        "needs_decision": _safe('needs_decision', build_needs_decision),
        "drift": _safe('drift', build_drift),
        "queue": _safe('queue', build_queue),
        "proposals": _safe('proposals', build_proposals),
        "repo_shape": _safe('repo_shape', build_repo_shape),
        "keys": _safe('keys', build_keys),
        "actions": _safe('actions', build_actions),
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
