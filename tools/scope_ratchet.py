#!/usr/bin/env python3
"""scope_ratchet.py — the SCOPE ratchet for the M1 program (ED-IN-0112).

Companion to tools/review_core.py, which grades TECHNICAL debt against
registers/review_baseline.yaml. This grades SCOPE against
registers/scope_baseline.yaml.

Why a second ratchet rather than more rows on the first: review_core's signals are
all quality signals, and scope growth is not a quality regression. A repository can
be getting cleaner by every review_core measure while the amount of work in flight
doubles. That is exactly what happened here, and nothing saw it.

MEASUREMENT DISCIPLINE (CLAUDE.md §0.1). Every signal is measured from the working
tree, never estimated and never read from a cache:

  ed.stale / ed.needs_jordan_stale
                             — via obs_core (the ED-IN-0068 single owner), non-archive,
                               status == open AND older than STALE_DAYS. AGE-WEIGHTED on
                               purpose: a raw open-count punishes FILING, which CLAUDE.md
                               §2 expects of substantively every PR, instead of the rot it
                               meant to catch (ED-IN-0114).
  audit.files                — git ls-files audit/
  tracked.files              — git ls-files
  proposals.open             — proposals/*.md, excluding README

Each measurement returns (value, evidence) where evidence is the command or path
that produced it, so a disputed number is re-derivable without reading this file.

USAGE
  python3 tools/scope_ratchet.py --summary   human-readable table
  python3 tools/scope_ratchet.py --check     exit 1 on ANY regression (CI/hook use)
  python3 tools/scope_ratchet.py --json      machine-readable (dashboard_data.py)
"""

import argparse
import glob
import json
import os
import subprocess
import sys

try:
    import yaml
except ImportError:  # pragma: no cover - environment guard
    print("scope_ratchet: PyYAML required (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)


# Primitives (repo root, lane roster, token estimate, ids, Status reader) are
# owned by tools/ci_common.py — plan G7, ED-IN-0159 §8.3. See its module docstring;
# the two lines below are the bootstrap, anchored on THIS file's directory.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = ci_common.REPO   # ONE OWNER (plan G7, ED-IN-0159 §8.3)
BASELINE_PATH = os.path.join('registers', 'scope_baseline.yaml')

LEDGER_GLOB = os.path.join('registers', 'editorial_ledger*.jsonl')
PROPOSALS_GLOB = os.path.join('proposals', '*.md')


def _repo(path=''):
    return os.path.join(REPO_ROOT, path) if path else REPO_ROOT


def _git_ls_files(subdir=None):
    """Tracked-file count. Uses git so untracked scratch files never inflate a ceiling.

    An EMPTY result is UNKNOWN, not zero: `git ls-files <missing-pathspec>` exits 0 with
    no output, so deleting `audit/` outright would otherwise have graded 0 <= 1265 as a
    clean pass. Only a non-empty listing is a measurement.
    """
    if subdir and not os.path.isdir(os.path.join(REPO_ROOT, subdir)):
        return None, f"{subdir}/ missing (UNKNOWN, not 0)"
    cmd = ['git', 'ls-files']
    if subdir:
        cmd.append(subdir)
    out = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True, check=False)
    if out.returncode != 0:
        return None, f"git ls-files failed: {out.stderr.strip()[:120]}"
    lines = [ln for ln in out.stdout.splitlines() if ln.strip()]
    if not lines:
        return None, f"{' '.join(cmd)} returned nothing (UNKNOWN, not 0)"
    return len(lines), ' '.join(cmd)


def _ledger_rows():
    """Every non-archive ledger row — delegated to obs_core, the single owner.

    DELEGATED 2026-07-31 (ED-IN-0112, adversarial pass). This function previously
    re-implemented obs_core's read concept-for-concept: same glob, same archive skip,
    same tolerant JSON parse. CLAUDE.md §8 names `tools/observability/obs_core.py` the
    single owner of "editorial-ledger read" (ED-IN-0068), so that was a second owner.

    THE DIVERGENCE WAS NOT COSMETIC. obs_core computes needs_jordan as
    `bool(e["needs_jordan"]) or text_needs_jordan(description)` — a free-text rescue for
    pre-cutover flat rows that predate the boolean field (`id_reservations.yaml:224`
    records this moving a register count 79 -> 97). The bare `r.get('needs_jordan')` used
    here counted strictly fewer, so the dashboard would have published TWO different
    "needs Jordan" numbers from two cards on one page — exactly the outcome
    single-ownership exists to prevent.
    """
    sys.path.insert(0, os.path.join(HERE, 'observability'))
    from obs_core import read_ledger_entries  # single owner (ED-IN-0068)
    return read_ledger_entries()


def _no_rows_evidence():
    """A zero-row read is UNMEASURABLE, not zero.

    An empty ledger set means the registers are missing or unreadable, which must never
    grade as `0 <= ceiling` -> pass. Returning None routes it to the `ok=None` UNKNOWN
    path the module docstring promises.
    """
    return None, 'no ledger rows readable — registers/ missing or unparseable (UNKNOWN, not 0)'


# AGE THRESHOLD. An item younger than this is work in flight; older than it, work that
# rotted. 30 days is a deliberate round number, not a fitted one — see _is_stale.
STALE_DAYS = 30


def _today():
    """Reference date for staleness.

    Read from SCOPE_RATCHET_TODAY when set, so tests can pin a date without patching
    the clock globally. Otherwise the real date — this is a staleness measure, and a
    frozen clock would make it silently stop ageing.
    """
    import datetime
    override = os.environ.get('SCOPE_RATCHET_TODAY')
    if override:
        try:
            return datetime.date.fromisoformat(override)
        except ValueError:
            pass
    return datetime.date.today()


def _is_stale(row, today=None):
    """True when an open item has sat longer than STALE_DAYS.

    UNDATED COUNTS AS STALE, deliberately. An entry with no parseable date cannot be
    SHOWN to be fresh, and the alternative — treating unknown age as zero — is the
    same "absence of evidence reads as a pass" defect this module already fixed for
    unmeasurable signals. Four such rows exist today; counting them surfaces the
    data-quality gap instead of hiding it.
    """
    import datetime
    today = today or _today()
    raw = row.get('date')
    if not raw:
        return True
    try:
        return (today - datetime.date.fromisoformat(str(raw)[:10])).days > STALE_DAYS
    except (ValueError, TypeError):
        return True


def measure_ed_stale():
    """Open items older than STALE_DAYS.

    REPLACED the raw `ed.open` census (ED-IN-0114). That metric conflated work OPENED
    with work NOT CLOSED, so filing an ED — the behaviour CLAUDE.md §2 expects of
    substantively every PR — always regressed it. A gate that fires on the correct
    action is a gate that gets ignored, and its own baseline file said so while
    shipping it anyway. Staleness is the actual disease; a freshly-filed item adds
    nothing to this number, and one left to rot adds one.
    """
    rows = _ledger_rows()
    if not rows:
        return _no_rows_evidence()
    today = _today()
    n = sum(1 for r in rows if r.get('status') == 'open' and _is_stale(r, today))
    return n, (f'obs_core.read_ledger_entries (non-archive), status == open '
               f'AND older than {STALE_DAYS}d (undated counts as stale)')


def measure_ed_needs_jordan_stale():
    """The bottleneck signal, age-weighted for the same reason as ed.stale."""
    rows = _ledger_rows()
    if not rows:
        return _no_rows_evidence()
    today = _today()
    # obs_core has already normalized needs_jordan, INCLUDING the free-text rescue.
    n = sum(1 for r in rows
            if r.get('status') == 'open' and r.get('needs_jordan') and _is_stale(r, today))
    return n, (f'obs_core.read_ledger_entries (non-archive), open AND needs_jordan '
               f'AND older than {STALE_DAYS}d')


def measure_audit_files():
    return _git_ls_files('audit')


def measure_tracked_files():
    return _git_ls_files()


def measure_proposals_open():
    if not os.path.isdir(_repo('proposals')):
        # Absent directory is UNKNOWN, not zero — see _no_rows_evidence.
        return None, 'proposals/ missing (UNKNOWN, not 0)'
    paths = [
        p for p in glob.glob(_repo(PROPOSALS_GLOB))
        if os.path.basename(p).lower() != 'readme.md'
    ]
    return len(paths), f"{PROPOSALS_GLOB} (excluding README)"


MEASURERS = {
    'ed.stale': measure_ed_stale,
    'ed.needs_jordan_stale': measure_ed_needs_jordan_stale,
    'audit.files': measure_audit_files,
    'tracked.files': measure_tracked_files,
    'proposals.open': measure_proposals_open,
}


def load_baseline(path=None):
    path = path or _repo(BASELINE_PATH)
    with open(path, encoding='utf-8') as fh:
        return yaml.safe_load(fh)


def collect(baseline=None):
    """Measure every signal and grade it against its ceiling.

    Returns a dict shaped for both the CLI and dashboard_data.py. A signal whose
    measurement failed is reported with ok=None (unknown), never ok=True — an
    unmeasurable signal must not read as a pass.
    """
    baseline = baseline or load_baseline()
    signals = baseline.get('signals') or {}
    out = []
    regressions = 0
    unknown = 0

    for name, spec in signals.items():
        measurer = MEASURERS.get(name)
        if measurer is None:
            out.append({
                'signal': name, 'ok': None, 'value': None,
                'baseline': spec.get('baseline'), 'target': spec.get('target'),
                'evidence': 'no measurer registered for this signal',
            })
            unknown += 1
            continue

        value, evidence = measurer()
        ceiling = spec.get('baseline')
        target = spec.get('target')

        if value is None or ceiling is None:
            ok = None
            unknown += 1
        else:
            ok = value <= ceiling
            if not ok:
                regressions += 1

        out.append({
            'signal': name,
            'ok': ok,
            'value': value,
            'baseline': ceiling,
            'target': target,
            'delta': (value - ceiling) if (value is not None and ceiling is not None) else None,
            'at_target': (value is not None and target is not None and value <= target),
            'evidence': evidence,
            'note': (spec.get('note') or '').strip(),
        })

    health = _measure_health(baseline)

    # ── G13 ACTIVITY CONTROL (ED-MB-0061 G13, added 2026-07-31) ──────────────────
    # "If doing nothing scores well on your metric, the metric cannot validate a
    # change. Every improvement number ships with an ACTIVITY control."
    #
    # As first shipped, this ratchet had exactly that defect: a session that did
    # NOTHING added no files, filed no EDs, and scored a clean `HELD`. The degenerate
    # solution won. `HELD` therefore cannot mean "healthy" on its own — it has to be
    # read against whether the program actually moved.
    #
    # The control is the health number, which is why it lives in the same file. A
    # `HELD` verdict with zero junctures closed is reported as HELD_INACTIVE: scope
    # did not grow, and neither did anything else. It is NOT a --check failure (an
    # infrastructure PR legitimately closes no juncture), but it must never render as
    # the same word as "held while shipping".
    # Movement = a juncture closed OR one in flight. See _measure_health's note: counting
    # only `done` made four in-progress junctures read as inactivity.
    moved = ((health.get('closed') or 0) > 0) or ((health.get('in_progress') or 0) > 0)
    if health.get('expired'):
        # The program the ceilings were seeded for has finished. Continuing to grade
        # against them silently measures the wrong program.
        verdict = 'EXPIRED'
    elif not regressions and not unknown:
        verdict = 'HELD' if moved else 'HELD_INACTIVE'
    elif regressions:
        verdict = 'REGRESSED'
    else:
        verdict = 'UNKNOWN'

    return {
        'available': True,
        'program': baseline.get('program'),
        'seeded': str(baseline.get('seeded')),
        'signals': out,
        'regressions': regressions,
        'unknown': unknown,
        'verdict': verdict,
        'activity': {
            'moved': moved,
            'closed': health.get('closed'),
            'in_progress': health.get('in_progress'),
            'control': 'G13 — scope held is only meaningful against whether the program moved',
        },
        'health': health,
    }


def _measure_health(baseline):
    """The program's single health number: M1 junctures closed.

    Measured live from the progress board rather than trusted from the baseline
    file, so the number cannot drift from the board it summarizes.
    """
    spec = ((baseline.get('health') or {}).get('m1_junctures_closed') or {})
    total = spec.get('total', 7)
    board = _repo(os.path.join('workplans', 'workplan_v6_progress.yaml'))
    try:
        data = ci_common.load_yaml(board)
        junctures = data['milestones']['M1']['junctures']
        closed = sum(1 for j in junctures if j.get('state') == 'done')
        measured_total = len(junctures)
    except Exception as exc:  # board missing/renamed is a real signal, not a crash
        return {
            'closed': None, 'total': total, 'ok': None,
            'evidence': f"could not read workplan board: {type(exc).__name__}",
        }

    # PARTIAL MOVEMENT IS MOVEMENT (ED-IN-0113 finding 3). Counting only `done`
    # made a session that advanced four junctures indistinguishable from one that
    # did nothing — the same blindness G13 exists to remove, one tier in. `closed`
    # remains the falsifier (a program ships junctures, not activity), but the
    # activity control now reads BOTH, so real progress stops rendering as inertia.
    in_progress = sum(1 for j in junctures if j.get('state') == 'in_progress')
    blocked = sum(1 for j in junctures if j.get('state') == 'blocked')

    # active_until, given a reader (ED-IN-0113 finding 5). It was prose: the stated
    # deactivation condition was enforced by nothing, so an expired ratchet would have
    # kept grading a program that had finished — a live failure mode, not a theoretical
    # one, since the ceilings are M1-scoped by their own header.
    expired = (measured_total > 0 and closed == measured_total)

    return {
        'closed': closed,
        'total': measured_total,
        'in_progress': in_progress,
        'blocked': blocked,
        'ok': closed > 0,
        'expired': expired,
        'active_until': str(baseline.get('active_until') or ''),
        'evidence': 'workplans/workplan_v6_progress.yaml milestones.M1.junctures state == done',
        'note': (spec.get('note') or '').strip(),
    }


def _fmt_summary(result):
    lines = []
    lines.append(f"scope ratchet — {result.get('program')} (seeded {result.get('seeded')})")
    lines.append('')
    lines.append(f"  {'signal':<20} {'now':>6} {'ceiling':>8} {'target':>7}  state")
    lines.append(f"  {'-' * 20} {'-' * 6} {'-' * 8} {'-' * 7}  {'-' * 10}")
    for s in result['signals']:
        if s['ok'] is None:
            state = 'UNKNOWN'
        elif not s['ok']:
            state = f"REGRESSED +{s['delta']}"
        elif s['baseline'] == s['target']:
            # A flat-hold row (audit.files, tracked.files): baseline == target means
            # "do not grow", NOT "goal achieved". Labelling it AT TARGET reads as an
            # accomplishment and invites exactly the complacency the row exists to prevent.
            state = 'holding (flat)'
        elif s['at_target']:
            state = 'AT TARGET'
        else:
            state = 'held'
        val = '?' if s['value'] is None else str(s['value'])
        lines.append(
            f"  {s['signal']:<20} {val:>6} {str(s['baseline']):>8} {str(s['target']):>7}  {state}"
        )
    h = result['health']
    lines.append('')
    closed = '?' if h.get('closed') is None else h['closed']
    prog = h.get('in_progress')
    extra = f" · {prog} in progress" if prog else ''
    lines.append(f"  HEALTH — M1 junctures closed: {closed}/{h.get('total')}{extra}")
    lines.append('')
    lines.append(f"  verdict: {result['verdict']}")
    if result['verdict'] == 'EXPIRED':
        lines.append('')
        lines.append(f"  The program these ceilings were seeded for is COMPLETE "
                     f"({h.get('closed')}/{h.get('total')}). `active_until: "
                     f"{h.get('active_until')}` is satisfied — re-seed against the post-M1")
        lines.append('  tree rather than carrying M1 ceilings forward as though nothing happened.')
    if result['verdict'] == 'HELD_INACTIVE':
        lines.append('')
        lines.append('  G13: scope did not grow — and neither did the program. "Held" by')
        lines.append('  inactivity is what a session that did nothing also scores, so this')
        lines.append('  verdict is not evidence that anything worked.')
    if result['regressions']:
        lines.append('')
        lines.append('  A regression means scope grew. Either retire the growth, or raise the')
        lines.append('  ceiling with an explicit ED and a loud call-out (ED-1094).')
    return '\n'.join(lines)


def seed(path=None, allow_raise=False):
    """Rewrite each baseline's ceiling to the CURRENTLY MEASURED value.

    WHY THIS EXISTS (found the hard way, 2026-07-31). The first version of
    scope_baseline.yaml was hand-transcribed from a measurement taken minutes earlier.
    Three commits merged in between and every ceiling was already stale — ed.open
    214->215, tracked.files 3090->3103 — so the ratchet would have failed on its own
    seeding commit, for reasons having nothing to do with scope.

    A ceiling is a MEASUREMENT, not a number someone typed. Seeding must therefore be
    an operation, mirroring `freshness_gate.py --update`. Hand-editing a baseline is
    how a ratchet acquires a value nobody verified.

    Only `baseline:` values are rewritten. `target:` is a design commitment and is
    never touched by an automated pass.

    THE RAISE GUARD. By default this LOWERS a ceiling freely (banking a shrink is the
    whole point of a ratchet) and REFUSES to raise one. A `--seed` that raises on every
    run is not a ratchet — it is a tool that reports the number back to itself and
    constrains nothing. Raising a scope ceiling is the project deciding to grow, which
    ED-1094 makes an explicit, ED-carrying, loudly-called-out act. `--allow-raise` is
    that act, and it exists so the raise is typed on purpose rather than absorbed.
    """
    path = path or _repo(BASELINE_PATH)
    with open(path, encoding='utf-8') as fh:
        lines = fh.readlines()

    measured = {}
    for name, fn in MEASURERS.items():
        value, _ev = fn()
        if value is not None:
            measured[name] = value

    out, current, changed, refused = [], None, [], []
    for line in lines:
        stripped = line.strip()
        if stripped.endswith(':') and not stripped.startswith('#'):
            key = stripped[:-1].strip()
            if key in MEASURERS:
                current = key
        if current and stripped.startswith('baseline:'):
            indent = line[:len(line) - len(line.lstrip())]
            old_raw = stripped.split(':', 1)[1].split('#')[0].strip()
            new = measured.get(current)
            try:
                old_val = int(old_raw)
            except ValueError:
                old_val = None

            # FAILS CLOSED, NOT OPEN (adversarial pass, ED-IN-0112). The first version
            # computed `is_raise` only when old_val parsed, so a ceiling written as a
            # float, a quoted string or `~` made is_raise False and the new value was
            # written WITHOUT --allow-raise — the guard silently absent on exactly the
            # malformed input most likely to hide a mistake. An unparseable ceiling is
            # now treated as a raise: refused unless the flag is explicit.
            is_raise = (new is not None and (old_val is None or new > old_val))
            if new is not None and (not is_raise or allow_raise):
                comment = line.split('#', 1)[1].rstrip() if '#' in line else ''
                out.append(f"{indent}baseline: {new}" + (f"  #{comment}" if comment else '') + "\n")
                if str(new) != old_raw:
                    changed.append((current, old_raw, new))
                current = None
                continue
            if is_raise:
                refused.append((current, old_val, new))
            current = None
        out.append(line)

    with open(path, 'w', encoding='utf-8') as fh:
        fh.writelines(out)
    return changed, refused


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--check', action='store_true',
                    help='exit 1 on any regression (CI / pre-commit use)')
    ap.add_argument('--json', action='store_true', help='machine-readable output')
    ap.add_argument('--summary', action='store_true', help='human-readable table (default)')
    ap.add_argument('--baseline', default=None, help='override baseline path (testing)')
    ap.add_argument('--seed', action='store_true',
                    help='rewrite ceilings to currently measured values (seeding only — '
                         'a ceiling is a measurement, never a transcription)')
    ap.add_argument('--allow-raise', action='store_true',
                    help='permit --seed to RAISE a ceiling; requires an ED and a loud '
                         'call-out per ED-1094. Without it, --seed lowers only.')
    args = ap.parse_args(argv)

    if args.seed:
        changed, refused = seed(args.baseline, allow_raise=args.allow_raise)
        for name, old, new in changed:
            print(f"  reseeded {name}: {old} -> {new}")
        for name, old, new in refused:
            print(f"  REFUSED to raise {name}: {old} -> {new} "
                  f"(+{new - old}) — scope grew.")
        if not changed and not refused:
            print("  baselines already match the working tree")
        if refused:
            print()
            print("  Raising a scope ceiling is a decision to grow the project, not")
            print("  housekeeping. Either retire the growth, or re-run with --allow-raise")
            print("  in a PR that carries an ED and says so loudly (CLAUDE.md §2, ED-1094).")
            return 1
        return 0

    baseline = load_baseline(args.baseline) if args.baseline else None
    result = collect(baseline)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(_fmt_summary(result))

    if args.check and result['regressions']:
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
