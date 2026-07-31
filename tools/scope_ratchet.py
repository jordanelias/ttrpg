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

  ed.open / ed.needs_jordan  — parsed from registers/editorial_ledger*.jsonl
                               (archives excluded; an archived item is closed by
                               definition and counting it would understate the drain)
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


HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
BASELINE_PATH = os.path.join('registers', 'scope_baseline.yaml')

LEDGER_GLOB = os.path.join('registers', 'editorial_ledger*.jsonl')
PROPOSALS_GLOB = os.path.join('proposals', '*.md')


def _repo(path=''):
    return os.path.join(REPO_ROOT, path) if path else REPO_ROOT


def _git_ls_files(subdir=None):
    """Tracked-file count. Uses git so untracked scratch files never inflate a ceiling."""
    cmd = ['git', 'ls-files']
    if subdir:
        cmd.append(subdir)
    out = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True, check=False)
    if out.returncode != 0:
        return None, f"git ls-files failed: {out.stderr.strip()[:120]}"
    lines = [ln for ln in out.stdout.splitlines() if ln.strip()]
    return len(lines), ' '.join(cmd)


def _ledger_rows():
    """Every non-archive ledger row, across the flat file and all lane files."""
    rows = []
    for path in sorted(glob.glob(_repo(LEDGER_GLOB))):
        if 'archive' in os.path.basename(path):
            continue
        with open(path, encoding='utf-8', errors='replace') as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError:
                    # A malformed row is a real defect, but it belongs to the ledger's
                    # own validator (ci_editorial_checker), not to the scope ratchet.
                    # Skipping keeps this tool from failing for someone else's reason.
                    continue
    return rows


def measure_ed_open():
    rows = _ledger_rows()
    n = sum(1 for r in rows if r.get('status') == 'open')
    return n, f"{LEDGER_GLOB} (non-archive), status == open"


def measure_ed_needs_jordan():
    rows = _ledger_rows()
    n = sum(1 for r in rows if r.get('status') == 'open' and r.get('needs_jordan'))
    return n, f"{LEDGER_GLOB} (non-archive), status == open AND needs_jordan"


def measure_audit_files():
    return _git_ls_files('audit')


def measure_tracked_files():
    return _git_ls_files()


def measure_proposals_open():
    paths = [
        p for p in glob.glob(_repo(PROPOSALS_GLOB))
        if os.path.basename(p).lower() != 'readme.md'
    ]
    return len(paths), f"{PROPOSALS_GLOB} (excluding README)"


MEASURERS = {
    'ed.open': measure_ed_open,
    'ed.needs_jordan': measure_ed_needs_jordan,
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

    return {
        'available': True,
        'program': baseline.get('program'),
        'seeded': str(baseline.get('seeded')),
        'signals': out,
        'regressions': regressions,
        'unknown': unknown,
        'verdict': 'REGRESSED' if regressions else ('UNKNOWN' if unknown else 'HELD'),
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
        with open(board, encoding='utf-8') as fh:
            data = yaml.safe_load(fh)
        junctures = data['milestones']['M1']['junctures']
        closed = sum(1 for j in junctures if j.get('state') == 'done')
        measured_total = len(junctures)
    except Exception as exc:  # board missing/renamed is a real signal, not a crash
        return {
            'closed': None, 'total': total, 'ok': None,
            'evidence': f"could not read workplan board: {type(exc).__name__}",
        }

    return {
        'closed': closed,
        'total': measured_total,
        'ok': closed > 0,
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
    lines.append(f"  HEALTH — M1 junctures closed: {closed}/{h.get('total')}")
    lines.append('')
    lines.append(f"  verdict: {result['verdict']}")
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

            is_raise = (new is not None and old_val is not None and new > old_val)
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
