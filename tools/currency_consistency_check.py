#!/usr/bin/env python3
"""
currency_consistency_check.py — the self-updating recency gate (ED-1087).

Watches the drift class that let the currency surfaces rot during 2026-06 (found by the
2026-07-01 month-overview consolidation): index stamps lagging their heads, ID ceilings
lagging the ledger, register headers lagging their bodies, and "maintained by" pointers
naming retired machinery. Every check is deterministic and reads only the working tree.

CHECKS
  1. CURRENT.md reconcile-stamp vs head freshness — any file named in CURRENT.md whose last
     commit postdates the "Last reconciled:" stamp means the index no longer reflects its
     heads (the PR #50 stale-merge-state failure class).
  2. ID-ceiling consistency — references/id_reservations.yaml `verified_live_max.ED`, every
     active block's bounds/next_free, and any literal "ED ceiling NNNN" in HANDOFF.md are
     compared to the ACTUAL max ED in registers/editorial_ledger.jsonl (the drift that overran
     reserved blocks A–C). Also covers the ED-<LANE>-NNNN namespace (2026-07-02, ED-IN-0001):
     each lane's `lane_ids.<LANE>.next_free` is compared to that lane's actual max in the
     ledger. The flat ED-NNNN sequence is FROZEN at cutover — no new flat allocations, so
     lane and flat ceilings never need reconciling against each other, only against their
     own ledger entries.
  3. Patch-register header vs body — "Next PP number: N" must exceed the register's max PP.
  4. Dead maintenance pointers — "maintained by <skill>" lines naming a skill that lives
     under deprecated/skills/ (unless the line itself says it is retired/former).
  5. CURRENT.md head-row existence — every path CURRENT.md names must exist in the tree
     (file or directory).
  6. HANDOFF.md must carry a "## Next…" heading — session_status.py's banner goes silently
     blank without one.

NOT re-implemented here (one rule, one home): SHA freshness -> tools/freshness_gate.py;
broken refs in registries/ledger -> tools/broken_dependency_checker.py; naming ->
tools/ci_naming_check.py. This tool imports broken_dependency_checker's tree walk rather
than re-deriving it.

WIRING: CI job "currency-consistency" (report-only first — names-drift graduation lane);
SessionStart banner (tools/session_status.py imports summary_line()); valoria_local.
Exit 1 on any drift so the blocking flip is a one-line CI change.

CLI:
    python tools/currency_consistency_check.py            # full report
    python tools/currency_consistency_check.py --summary  # one line (banner use)
"""
import json
import os
import re
import subprocess
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

try:
    import broken_dependency_checker as _bdc
except ImportError:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import broken_dependency_checker as _bdc


def _read(rel):
    try:
        with open(os.path.join(REPO_ROOT, rel), encoding='utf-8', errors='replace') as f:
            return f.read()
    except OSError:
        return None


def _git_last_commit_date(path):
    """YYYY-MM-DD of the last commit touching path ('' if untracked/never committed)."""
    r = subprocess.run(['git', 'log', '-1', '--format=%cs', '--', path],
                       capture_output=True, text=True, cwd=REPO_ROOT)
    return r.stdout.strip() if r.returncode == 0 else ''


def _current_md_paths(text):
    """Paths named in CURRENT.md (backticked); keeps trailing-slash package dirs.
    Glob patterns (engine/params/bg/*) are references to families, not checkable paths."""
    paths = re.findall(
        r'`((?:designs|systems|engine|params|references|canon|sim|tools|tests|skills)/[^`\s]*)`', text)
    return sorted({p for p in paths if '*' not in p and '?' not in p})


def _next_day(date_str):
    """YYYY-MM-DD + 1 day (string compare domain)."""
    import datetime
    d = datetime.date.fromisoformat(date_str)
    return (d + datetime.timedelta(days=1)).isoformat()


def _ledger_max_ed():
    text = _read('registers/editorial_ledger.jsonl') or ''
    ids = [int(m) for m in re.findall(r'"id":\s*"ED-(\d+)"', text)]
    return max(ids) if ids else 0


# Lane roster for the ED-<LANE>-NNNN namespace (2026-07-02) — mirrors
# validate_ed_citations.LANE_CODES / references/id_reservations.yaml.
LANE_CODES = ('MB', 'PC', 'FI', 'SC', 'FA', 'WR', 'IN', 'GO', 'SE')


def _ledger_lane_max():
    """{'MB': 3, 'SC': 1, ...} — max per-lane numeric suffix seen in the live ledger.
    A flat 'ED-NNNN' id never matches (no letters after the dash), so this is naturally
    disjoint from _ledger_max_ed() and requires no coordination with it."""
    text = _read('registers/editorial_ledger.jsonl') or ''
    out = {}
    for lane, num in re.findall(r'"id":\s*"ED-([A-Z]{2})-(\d+)"', text):
        if lane in LANE_CODES:
            out[lane] = max(out.get(lane, 0), int(num))
    return out


def check_current_stamp(drift):
    text = _read('CURRENT.md')
    if text is None:
        drift.append("CURRENT.md missing")
        return
    m = re.search(r'Last reconciled:\s*(\d{4}-\d{2}-\d{2})', text)
    if not m:
        drift.append("CURRENT.md: no 'Last reconciled: YYYY-MM-DD' stamp found")
        return
    stamp = m.group(1)
    # One-day grace: git %cs is UTC while stamps are authored in the operator's timezone —
    # a same-session commit can land "tomorrow" in UTC. The PR-#50 failure class (days of
    # unreconciled drift) still trips; a TZ-skewed same-day commit does not.
    grace = _next_day(stamp)
    for path in _current_md_paths(text):
        last = _git_last_commit_date(path.rstrip('/'))
        if last and last > grace:
            drift.append(f"CURRENT.md stamp {stamp} predates head {path} (last commit {last}) — re-reconcile")


def check_current_paths_exist(drift):
    text = _read('CURRENT.md') or ''
    all_files = _bdc.get_all_repo_files()
    for path in _current_md_paths(text):
        p = path.rstrip('/')
        if p in all_files:
            continue
        if os.path.isdir(os.path.join(REPO_ROOT, p)):
            continue
        drift.append(f"CURRENT.md names nonexistent path: {path}")


def check_id_ceilings(drift):
    live_max = _ledger_max_ed()
    res_text = _read('references/id_reservations.yaml')
    if res_text is None:
        drift.append("references/id_reservations.yaml missing")
        return
    m = re.search(r'^\s*ED:\s*(\d+)', res_text, re.M)
    if m and int(m.group(1)) < live_max:
        drift.append(f"id_reservations verified_live_max.ED {m.group(1)} < actual ledger max ED-{live_max} — re-verify (LB-21 protocol)")
    # every ED block: next_free must exceed live IDs *inside that block's range*
    for bm in re.finditer(r'ED:\s*\{\s*block:\s*"(\d+)-(\d+)",\s*next_free:\s*(\d+)', res_text):
        lo, hi, nxt = int(bm.group(1)), int(bm.group(2)), int(bm.group(3))
        if lo <= live_max <= hi and nxt <= live_max:
            drift.append(f"id_reservations block {lo}-{hi}: next_free {nxt} <= live max ED-{live_max} inside the block — bump before allocating")
    hand = _read('HANDOFF.md') or ''
    hm = re.search(r'ED ceiling\s+(\d+)', hand)
    if hm and int(hm.group(1)) < live_max:
        drift.append(f"HANDOFF.md quotes 'ED ceiling {hm.group(1)}' but ledger max is ED-{live_max}")


def check_lane_id_ceilings(drift):
    """Per-lane counterpart to check_id_ceilings for the ED-<LANE>-NNNN namespace.
    No-ops cleanly if no lane-tagged IDs exist yet (nothing to check) or the
    lane_ids section is absent (id_reservations.yaml missing is already flagged
    by check_id_ceilings)."""
    lane_max = _ledger_lane_max()
    if not lane_max:
        return
    res_text = _read('references/id_reservations.yaml')
    if res_text is None:
        return
    for lane, live in sorted(lane_max.items()):
        m = re.search(rf'\b{lane}:\s*\{{[^}}]*next_free:\s*(\d+)', res_text)
        if not m:
            drift.append(f"id_reservations lane_ids has no entry for lane {lane}, but ED-{lane}-{live} exists in the ledger")
            continue
        if int(m.group(1)) <= live:
            drift.append(f"id_reservations lane_ids.{lane}.next_free {m.group(1)} <= actual ledger max ED-{lane}-{live} — bump before allocating")


def check_patch_register_header(drift):
    text = _read('registers/patch_register_active.yaml')
    if text is None:
        drift.append("registers/patch_register_active.yaml missing")
        return
    m = re.search(r'Next PP number:\s*(\d+)', text)
    body_max = max((int(x) for x in re.findall(r'\bPP-(\d+)', text)), default=0)
    if m and int(m.group(1)) <= body_max:
        drift.append(f"patch_register header 'Next PP number: {m.group(1)}' <= body max PP-{body_max}")


MAINTAINED_RE = re.compile(r'(?:auto-)?maintained(?:\s*[—-])?\s*(?:—\s*)?(?:appended\s+)?by[:\s]+([a-z][a-z0-9_-]{2,})', re.I)
RETIRED_MARKERS = ('retired', 'former', 'deprecated', 'hand')


def check_dead_maintainers(drift):
    dep_skills = set()
    dep_dir = os.path.join(REPO_ROOT, 'deprecated', 'skills')
    if os.path.isdir(dep_dir):
        dep_skills = {d for d in os.listdir(dep_dir)
                      if os.path.isdir(os.path.join(dep_dir, d))}
    if not dep_skills:
        return
    roots = ('references', 'designs', 'params', 'canon')
    for root in roots:
        base = os.path.join(REPO_ROOT, root)
        for dirpath, dirnames, filenames in os.walk(base):
            rel_dir = os.path.relpath(dirpath, REPO_ROOT).replace(os.sep, '/')
            if any(part in ('archives', 'deprecated', 'audit') for part in rel_dir.split('/')):
                dirnames[:] = []
                continue
            for name in filenames:
                if not name.endswith(('.md', '.yaml')):
                    continue
                rel = f"{rel_dir}/{name}"
                text = _read(rel) or ''
                for i, line in enumerate(text.splitlines(), 1):
                    m = MAINTAINED_RE.search(line)
                    if not m:
                        continue
                    owner = m.group(1).lower()
                    if owner in dep_skills and not any(k in line.lower() for k in RETIRED_MARKERS):
                        drift.append(f"{rel}:{i}: 'maintained by {owner}' — that skill is retired (deprecated/skills/)")


def check_handoff_heading(drift):
    text = _read('HANDOFF.md')
    if text is None:
        return  # session_status handles the missing-file case itself
    if not any(ln.strip().lower().startswith('## next') for ln in text.splitlines()):
        drift.append("HANDOFF.md has no '## Next…' heading — the SessionStart banner will be silently blank")


def run_checks():
    drift = []
    check_current_stamp(drift)
    check_current_paths_exist(drift)
    check_id_ceilings(drift)
    check_lane_id_ceilings(drift)
    check_patch_register_header(drift)
    check_dead_maintainers(drift)
    check_handoff_heading(drift)
    return drift


def summary_line():
    """One-line status for the SessionStart banner (never raises)."""
    try:
        n = len(run_checks())
    except Exception as e:  # the banner must never break session start
        return f"currency drift: check errored ({type(e).__name__})"
    return "currency drift: none" if n == 0 else \
        f"currency drift: {n} item(s) — run python tools/currency_consistency_check.py"


def main(argv):
    if '--summary' in argv:
        print(summary_line())
        return 0
    drift = run_checks()
    if drift:
        print(f"[CURRENCY DRIFT: {len(drift)}]")
        for d in drift:
            print(f"  {d}")
        return 1
    print("Currency consistency: stamps, ceilings, registers, and maintainers all current.")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
