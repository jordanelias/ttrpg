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
import glob
import re
import subprocess
import sys

# Primitives (repo root, lane roster, token estimate, ids, Status reader) are
# owned by tools/ci_common.py — plan G7, ED-IN-0159 §8.3. See its module docstring;
# the two lines below are the bootstrap, anchored on THIS file's directory.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402

REPO_ROOT = ci_common.REPO

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


# Trees that hold CANONICAL HEADS. The stamp answers one question — "has a canonical head moved
# since CURRENT.md was last reconciled?" — and only these trees can make its answer yes.
#
# WHY THIS SPLIT EXISTS (ED-IN-0089). The stamp check used every path CURRENT.md names, which
# includes 12 `tools/` and 3 `tests/` entries. Those are apparatus: editing a validator or a unit
# test cannot make a canonical-head index stale, but it tripped the stamp all the same, and the only
# way to clear it was a reflex date bump that reconciled nothing. MEASURED over the 57 commits since
# 2026-06-28: 51 would trip the stamp, and 12 of those (24%) touched a tracked `tools/` or `tests/`
# path and NO canonical head at all. Those 12 are pure false positives — a fifth of the signal.
# (The honest counter-number: 36 more trip via a canonical head TOO, so this narrows the noise, it
# does not eliminate the check. Reproduce with deprecated/tools/measure_stamp_false_positives.py,
# retired 2026-07-29 ED-IN-0097/OI-15 — zero invokers, still runnable from its retired home.)
#
# THE EXISTENCE CHECK IS DELIBERATELY *NOT* NARROWED. `check_current_paths_exist` still covers every
# path, `tools/` and `tests/` included: CURRENT.md naming a deleted validator is real drift and
# exactly the rot this session spent its time on. What changes is only the STALENESS half — the one
# that was asking a question apparatus cannot answer.
CANONICAL_HEAD_TREES = ('designs', 'systems', 'engine', 'params', 'references', 'canon', 'sim')


def _canonical_head_paths(text):
    return [p for p in _current_md_paths(text)
            if p.split('/')[0] in CANONICAL_HEAD_TREES]


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
# ONE OWNER: ci_common.LANE_CODES (plan G7, ED-IN-0159 §8.3). Was a verbatim
# copy of the 9-code tuple; obs_core's header records that one such copy once
# silently omitted GO, undercounting a whole lane.
LANE_CODES = ci_common.LANE_CODES


def _ledger_lane_max():
    """{'MB': 3, 'SC': 1, ...} — max per-lane numeric suffix seen across ALL ledger files.

    THIS RETURNED `{}` AND THE CHECK IT FEEDS COULD NEVER FIRE. It read only the flat
    `registers/editorial_ledger.jsonl`, which contains ZERO lane-tagged ids — every `ED-<LANE>-NNNN`
    entry lives in `registers/editorial_ledger_<lane>.jsonl` by the 2026-07-08 lane split
    (CLAUDE.md §3). So `check_lane_id_ceilings` hit its `if not lane_max: return` guard on every run
    and silently checked nothing, while its docstring explained the no-op as "no lane-tagged IDs
    exist yet". They exist; the reader was looking in the one file they are never written to.

    Measured at repair (2026-08-01): before, 0 lanes checked; after, 8 lanes checked and 0 new
    findings — every `next_free` is exactly `max + 1`. The gate agreed by luck, which is the whole
    hazard: a blind check and a passing check are indistinguishable from the outside, and this one
    guards ID allocation across nine concurrent lanes.

    Archives are INCLUDED on purpose: an archived `ED-IN-0058` still consumed that id, so excluding
    them would under-report the maximum and re-open the collision this check exists to prevent.

    NOT migrated to `obs_core.read_ledger_entries` here. CLAUDE.md §8 defers that specific migration
    as blocking-gate risk needing its own expected-delta test; this is the scoped repair of the read
    path, and the owner migration remains the filed item.
    """
    # Globbed against REPO_ROOT, not the CWD. A relative glob here would find nothing when the
    # tool is run from anywhere but the repo root and silently restore the exact blindness this
    # docstring describes — a cwd-dependent guard, the class an earlier gate batch already had to
    # correct in this repo (`cd / && pytest` turning 2 failures into 23 passes).
    out = {}
    for abs_path in sorted(glob.glob(os.path.join(REPO_ROOT, 'registers', 'editorial_ledger*.jsonl'))):
        path = os.path.relpath(abs_path, REPO_ROOT)
        text = _read(path) or ''
        for lane, num in re.findall(r'"id":\s*"ED-([A-Z]{2})-(\d+)"', text):
            if lane in LANE_CODES:
                out[lane] = max(out.get(lane, 0), int(num))
    return out


def _history_is_unusable():
    """True only when the checkout has ONE commit, so per-path dates are meaningless.

    THE DISCRIMINATOR IS COMMIT COUNT, NOT SHALLOWNESS — and getting that wrong is instructive.
    My first version asked `git rev-parse --is-shallow-repository`, which is `true` for ANY
    depth-limited clone. Measured on this very container: shallow=true, **76 commits**, and
    `git log -1 -- systems/world/` correctly returns 2026-07-29 against a HEAD of 2026-08-03 —
    history plainly usable. That guard would have disabled a working check on every developer
    machine that clones with `--depth 50`, trading a false-positive gate for a silently absent one,
    which is the worse trade (§0.1: a check that cannot fail is not a check).

    At depth 1 there is exactly one commit, so `git log -1 --format=%cs -- <path>` returns that
    commit's date for EVERY path and every canonical head falsely reads as touched today. That is
    the only case where the dates carry no information, and it is exactly what it detects.
    """
    out = subprocess.run(['git', 'rev-list', '--count', 'HEAD'],
                         cwd=REPO_ROOT, capture_output=True, text=True)
    if out.returncode != 0:
        return False              # no git at all: let the check run and fail loudly if it must
    try:
        return int(out.stdout.strip()) <= 1
    except ValueError:
        return False


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
    # SHALLOW-CLONE GUARD (ED-IN-0123, 2026-08-03). Under `actions/checkout` WITHOUT `fetch-depth: 0`
    # the repository has exactly ONE commit, so `git log -1 --format=%cs -- <path>` returns that
    # commit's date for EVERY path — every canonical head then looks touched today and this check
    # reports drift on all of them at once. MEASURED: this fired as `currency.stamps: fail` in the
    # compliance-check job (which sets no fetch-depth) while passing locally on full history, the
    # moment a commit landed more than one day after the stamp. A check whose verdict depends on
    # checkout depth is not measuring the tree; it is measuring the CI config. Detect and say so
    # rather than emit a page of false drift — the honest report is "cannot measure" (§0.1 point 4).
    # The notice goes to STDERR, not into `drift`. Putting it in the drift list was my first
    # version and it was wrong in a specific way: "cannot measure" and "measured, and it drifted"
    # are different verdicts, and every caller of run_checks() reads len(drift) as the second.
    # That turned the guard into a false positive in the unit-tests job (depth-1), which asserts a
    # tools-only change trips nothing. The job that GRADES this check (compliance-check, via
    # review_core) sets `fetch-depth: 0`, so the check still runs everywhere its verdict is used.
    if _history_is_unusable():
        print("[currency] CURRENT.md stamp check not run: this checkout has a single commit "
              "(depth-1), so per-path commit dates are all HEAD's date. Use `fetch-depth: 0`.",
              file=sys.stderr)
        return
    for path in _canonical_head_paths(text):   # apparatus cannot stale a canon index — ED-IN-0089
        last = _git_last_commit_date(path.rstrip('/'))
        if last and last > grace:
            drift.append(f"CURRENT.md stamp {stamp} predates head {path} (last commit {last}) — re-reconcile")


# ---------------------------------------------------------------------------
# STRUCTURAL VALIDATION OF THE RECONCILE-STAMP CHAIN (2026-08-14, ED-IN-0189).
#
# WHY THIS EXISTS. Every §1 authority in this repo was validated by METADATA and none by
# STRUCTURE: check_current_stamp above reads the LEADING date of CURRENT.md and nothing else, so
# the stamp paragraph was free to carry ~8 verbatim-duplicated blocks and a chronology running
# 08-12 -> 07-30 -> 08-10 -> 07-30 while this tool reported "currency drift: none". Three
# independent read-only lenses found that corruption by reading; no tool in the tree could see it
# (audit/2026-08-14-five-lens-repo-assessment, findings T1 and L2). The blob is deleted in this
# same commit; this is the guard that fails if the pattern comes back — CLAUDE.md §0.1 point 5,
# "if you cannot write the guard you have not understood the pattern".
#
# THE INVARIANT IS NON-INCREASING, NOT STRICTLY DESCENDING, and the difference is load-bearing.
# The remediation plan (ED-IN-0185 step A2) specified "strictly-descending dates"; the tree
# falsifies that. MEASURED on the pre-deletion file: four lanes (IN, MB, PC, SC) each reconciled
# on 2026-08-08 and wrote a stamp, so a strict rule would have failed on correct content and
# taught the next session to weaken it. What actually went wrong is an INVERSION — a link dated
# LATER than the link before it, in a chain that reads newest-first — and that is what is flagged.
#
# MEASURED BLIND SPOT, stated rather than left to be discovered: duplication is detected by
# whitespace-normalized EXACT match, so two blocks differing by a single character — a stray
# trailing underscore, a fixed typo — are two blocks. This is not hypothetical; it surfaced while
# writing the test fixture below. It is the right trade anyway: near-match detection on prose
# invites false positives on a gate, and the splice this guards against COPIES, so its output is
# byte-identical. Exact match found all 8 real duplicates on the pre-deletion file.
#
# BOTH RULES ARE VERIFIED AGAINST THE PRE-DELETION FILE, not just against synthetic input:
# tests/valoria/test_currency_consistency_check.py pins the real corrupted paragraph (recovered
# from git) and asserts this check reports both defects on it. A guard whose only evidence is a
# fixture its author wrote is measuring the fixture.
_RECON_MARKER = re.compile(
    r'(?:Last reconciled|Prior reconcile|\*\*Prior:\*\*)\s*:?\s*\d{4}-\d{2}-\d{2}')
_RECON_DATE = re.compile(
    r'(?:Last reconciled|Prior reconcile|\*\*Prior:\*\*)\s*:?\s*(\d{4}-\d{2}-\d{2})')

# A duplicated stamp BODY is the splice signature. The floor exists so that short connective
# fragments — which can legitimately recur — are not read as splices. MEASURED on the pre-deletion
# paragraph: the genuine duplicate bodies ran 1,600-8,700 chars and the longest innocent repeat was
# under 200, so 400 separates them with room on both sides and is not tuned to a single case.
_DUP_BLOCK_MIN_CHARS = 400


def _reconcile_paragraph(text):
    """The reconcile-stamp block: the one blank-line-delimited paragraph holding the stamp."""
    for para in text.split('\n\n'):
        if 'Last reconciled:' in para:
            return para
    return None


def _norm_ws(s):
    return ' '.join(s.split())


def check_current_stamp_structure(drift):
    text = _read('CURRENT.md')
    if text is None:
        return                      # check_current_stamp already reported the missing file
    para = _reconcile_paragraph(text)
    if para is None:
        return                      # ditto for the missing stamp

    dates = _RECON_DATE.findall(para)
    for i in range(1, len(dates)):
        if dates[i] > dates[i - 1]:
            drift.append(
                f"CURRENT.md reconcile chain is non-monotonic: link {i + 1} ({dates[i]}) is newer "
                f"than the link before it ({dates[i - 1]}) — the chain reads newest-first, so a "
                f"date that climbs is a splice, not a reconcile")
            break                   # one report; the whole chain needs a human either way

    seen, reported = {}, set()
    for block in _RECON_MARKER.split(para):
        norm = _norm_ws(block)
        if len(norm) < _DUP_BLOCK_MIN_CHARS:
            continue
        seen[norm] = seen.get(norm, 0) + 1
        if seen[norm] == 2 and norm not in reported:
            reported.add(norm)
            drift.append(
                f"CURRENT.md reconcile chain repeats a {len(norm)}-char stamp body verbatim "
                f"({norm[:70]}…) — duplicated blocks are the signature of a mid-chain splice")


# A TOMBSTONE IS NOT A HEAD CLAIM (2026-08-05, the evacuation).
# CURRENT.md's job is to name the LIVE canonical head per subsystem, and this check exists to stop
# it naming something that does not exist. But after the evacuation, the honest CURRENT.md row for
# an evacuated subsystem NAMES the old path in order to say it is gone and where the capture is —
# "⚠️ EVACUATED 2026-08-05 → captured in engine/engine_params/params_tables.yaml (fork ref …)".
# The checker cannot distinguish "this is the head" from "this is where the head used to be", so it
# read four tombstones as four drift items.
#
# The discriminator is deliberately a LINE-LOCAL marker, not a global allowlist: the exemption
# applies only on a line that says the path is gone, so a genuinely stale head reference elsewhere
# in the file still fails. This is the small half of the FORKED-status mechanism that
# broken_dependency_checker needs for ledger evidence; the same idea, one file, no new format.
_TOMBSTONE = re.compile(r'EVACUATED|FORKED|fork ref', re.I)


def _tombstoned_paths(text):
    """Paths named on a line that declares them evacuated — mentioned, not claimed as live."""
    out = set()
    for line in text.splitlines():
        if not _TOMBSTONE.search(line):
            continue
        out.update(re.findall(
            r'`((?:designs|systems|engine|params|references|canon|sim|tools|tests|skills)/[^`\s]*)`',
            line))
    return out


def check_current_paths_exist(drift):
    text = _read('CURRENT.md') or ''
    all_files = _bdc.get_all_repo_files()
    tombstoned = _tombstoned_paths(text)
    for path in _current_md_paths(text):
        if path in tombstoned:
            continue
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
    check_current_stamp_structure(drift)
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
