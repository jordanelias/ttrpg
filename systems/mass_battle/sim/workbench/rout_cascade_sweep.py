"""A8 (ED-MB-0067 Part A / ED-MB-0071) — choose ROUT_CASCADE_FRAC by its sweep, per config.py's own
rule (`config.py` — ROUT_CASCADE_FRAC's comment: "chosen on evidence rather than asserted -- the sweep
over candidate values is the experiment"; the value "is CALIBRATED-DEBT until something outside the
engine supports it"). Target: `tests/sim/gauge_mb.py`'s own historically-grounded
LOSER_CAS_BAND = (15.0, 30.0) as the PRIMARY criterion; the gauge's own win-share bands are read
alongside it only as a CONTROL, per CLAUDE.md Sec.0.1 pt 4 ("a number without a control is not a
measurement") — this sweep must not be allowed to fix casualty realism by silently breaking the
already-passing win-share dimension.

[CORRECTION, adversarial review round 1, 2026-09-27] The first version of this script hand-listed
six "multi-subunit" rows (H3/H4/H5/H6/H10/H11) and excluded C4/C7 on the unmeasured claim that their
LOSING side is always the single-subunit one, so the parameter "adds cost without adding signal"
there. That is false: C4/C7 build their `_envelop_army` side at `pin_frac=2/3` (a 400/100/100 split
of a 600-troop army), so if the 400-troop centre alone breaks, its share of SPAWN strength is
400/600 ≈ 0.667 — enough to rout the whole envelop force at 0.5 OR 0.6, where at 1.0 the wings fight
on. The exclusion criterion actually needed is "does either side have >1 subunit", not a hand-curated
guess about who typically loses — a lower threshold can turn a winning multi-subunit side's near-miss
into a rout, which is exactly the win-share-regression risk this sweep exists to catch as a control.
Fixed by deriving the row set PROGRAMMATICALLY (below) instead of hand-listing it, so this class of
omission cannot recur silently.

WHY NOT THE FULL BATTERY, restated correctly this time. `Unit.derive_rout`'s cascade condition
(`self._broken_share() >= ROUT_CASCADE_FRAC`) is evaluated per-Unit over that Unit's OWN subunits.
For a Unit with exactly one subunit, `_broken_share()` is a 0/1 step function (0 before that subunit
breaks, 1.0 after), so ANY threshold in (0, 1] clears at the same instant regardless of its value —
PROVABLY inert, not merely unmeasured. `_faction_to_unit` (`massbattle.py`, the only function
building Units for the live campaign) builds exactly one subunit per faction, so this sweep's choice
has ZERO effect on any campaign-reachable battle today, whatever it picks — disclosed, not hidden.
Every gauge/CAV row where AT LEAST ONE side is built via a callable army-builder
(`_envelop_army`/`_refused_army`/`_command_army`, per `gauge_mb.matchup`'s own `a_is_fn`/`b_is_fn`
convention) has >1 subunit on that side and is therefore in scope; a plain shape-string side
(`make_unit`, single subunit) is not, by the same construction argument, regardless of which side
wins.

Usage:
    python systems/mass_battle/sim/workbench/rout_cascade_sweep.py --out PATH   # full sweep, n=40 screen
    python systems/mass_battle/sim/workbench/rout_cascade_sweep.py --confirm 0.5 --n 60 --out PATH
    PYTHONPATH=. ROUT_CASCADE_FRAC=0.5 python systems/mass_battle/sim/workbench/rout_cascade_sweep.py --worker --n 60
"""
import argparse
import json
import os
import subprocess
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
# Needed in BOTH the driver process (main()'s own _multi_subunit_row_ids() call, to print the table
# header before any subprocess runs) and the worker (see _worker's own note on why it re-asserts this
# rather than trusting the caller alone) -- set once, here, for whichever role this process plays.
if REPO not in sys.path:
    sys.path.insert(0, REPO)
if os.path.join(REPO, 'tests', 'sim') not in sys.path:
    sys.path.insert(0, os.path.join(REPO, 'tests', 'sim'))

# CANDIDATE_VALUES is a 0.1-step screening grid from the inert legacy default (1.0) down to the
# concept's own candidate (0.5, config.py's own citation) — arbitrary screening resolution, not a
# fitted magnitude, and read only by this script's own driver, never by the engine, so it carries
# none of the engine's own CALIBRATED-DEBT status. [JUSTIFIED: a 0.1-step scan of the interval, not a fitted value]
CANDIDATE_VALUES = (1.0, 0.9, 0.8, 0.7, 0.6, 0.5)  # [JUSTIFIED: 0.1-step screening grid, see comment above]
# Half the gauge's own default n=60 (gauge_mb.py) — a screening pass over 6 candidates trades
# precision for the 6x runtime cost; --confirm re-runs the winner at the gauge's own n for the
# number actually reported. [JUSTIFIED: half of gauge_mb.py's own n=60 default]
_DEFAULT_SCREEN_N = 40  # [JUSTIFIED: half of gauge_mb.py's own default n=60]
# [JUSTIFIED: matches tools/ci_golden_modes_check.py's own per-mode subprocess timeout, same battery-of-battles workload]
_WORKER_TIMEOUT_S = 300  # [JUSTIFIED: matches ci_golden_modes_check.py's own per-mode timeout]


def _multi_subunit_row_ids():
    """Every TESTS/CAV_TESTS row (gauge_mb.py) with a multi-subunit side, derived procedurally from
    the SAME a_is_fn/b_is_fn test gauge_mb.matchup itself uses to decide callable-vs-plain-shape --
    not a hand-curated guess (see this module's own correction note above for why hand-curation
    silently dropped C4/C7 the first time)."""
    import gauge_mb
    ids = []
    for row in list(gauge_mb.TESTS) + list(gauge_mb.CAV_TESTS):
        tid, _label, sa, sb = row[0], row[1], row[2], row[3]
        if callable(sa) or callable(sb):
            ids.append(tid)
    return tuple(ids)


def _worker(n, expect_value=None):
    """Run in the SAME process ROUT_CASCADE_FRAC was set in (env var read at config-import time, so
    this must never run after another value has already been imported in this interpreter -- that is
    exactly why the sweep driver below uses one subprocess per candidate, matching bat.py's/
    ci_golden_modes_check.py's own established pattern for testing config toggles, rather than
    importlib.reload, which would need every transitively-affected module reloaded in dependency
    order to be trustworthy for a one-off script).

    [FIX, adversarial review round 1] REPO ROOT is on sys.path unconditionally at module level (see
    the top of this file) -- not only via the driver's subprocess PYTHONPATH. The first version
    relied ENTIRELY on that subprocess env, so this function's own documented direct-invocation usage
    (module docstring) would have raised ModuleNotFoundError exactly like bat.py's pre-ED-MB-0070
    bug. Fixed the same way: make the worker self-sufficient, don't rely on the caller's environment
    alone."""
    from systems.mass_battle.sim import config as _cfg
    import gauge_mb

    if expect_value is not None and _cfg.ROUT_CASCADE_FRAC != expect_value:
        # [N4a, adversarial review round 1] A silently-dropped env var would make this worker run at
        # whatever config.py's OWN default is instead of the requested candidate -- indistinguishable
        # from "identical to 1.0" without this check (CLAUDE.md Sec.0.1 pt 3 row 4: "a generator that
        # no-ops... each return 0"). Fail loud instead of reporting a wrong value as if it were right.
        raise RuntimeError(f"requested ROUT_CASCADE_FRAC={expect_value!r} but config resolved to "
                            f"{_cfg.ROUT_CASCADE_FRAC!r} -- the env var did not take effect")

    row_ids = _multi_subunit_row_ids()
    rows = [t for t in (list(gauge_mb.TESTS) + list(gauge_mb.CAV_TESTS)) if t[0] in row_ids]
    out = {'rout_cascade_frac': _cfg.ROUT_CASCADE_FRAC, 'n': n, 'row_ids': row_ids, 'rows': {}}
    for tid, label, sa, sb, ka, kb, lo, hi, dexp, *rest in rows:
        metric = rest[0] if rest else 'decA'
        r = gauge_mb.matchup(sa, sb, ka, kb, 'multi', n=n)
        ok, cflag, why = gauge_mb.casualty_verdict(r)
        out['rows'][tid] = {
            'label': label, 'metric': metric, 'decA': r['decA'], 'a_pct': r['a'], 'dec_n': r['dec_n'],
            'draw_pct': r['d'], 'win_band': [lo, hi],
            'win_cas': r['win_cas'], 'lose_cas': r['lose_cas'], 'capped_pct': r['capped'],
            'casualty_ok': ok, 'casualty_flag': cflag, 'casualty_why': why,
        }
    print(json.dumps(out))


def _run_one(value, n):
    env = dict(os.environ)
    env['ROUT_CASCADE_FRAC'] = repr(value)
    env['PYTHONPATH'] = REPO + (os.pathsep + env['PYTHONPATH'] if env.get('PYTHONPATH') else '')
    r = subprocess.run([sys.executable, os.path.abspath(__file__), '--worker', '--n', str(n),
                        '--expect-value', repr(value)],
                        cwd=REPO, env=env, capture_output=True, text=True, timeout=_WORKER_TIMEOUT_S)
    if r.returncode != 0:
        raise RuntimeError(f"worker failed at ROUT_CASCADE_FRAC={value}:\n{r.stdout}\n{r.stderr}")
    return json.loads(r.stdout.strip().splitlines()[-1])


def _row_passes_win_band(row):
    if row['metric'] == 'rawA':
        return row['win_band'][0] <= row['a_pct'] <= row['win_band'][1]
    return row['dec_n'] > 0 and row['win_band'][0] <= row['decA'] <= row['win_band'][1]


def _print_table(results, row_ids):
    print(f"\n{'value':>7}  " + '  '.join(f"{tid:>16}" for tid in row_ids) + "   realism  win-share(ctrl)")
    for value, data in results:
        cells = []
        for tid in row_ids:
            row = data['rows'][tid]
            lc = row['lose_cas']
            cells.append(f"{'n/a':>16}" if lc is None else f"{lc:6.1f}%{('OK' if row['casualty_ok'] else 'no'):>8}")
        n_ok = sum(1 for tid in row_ids if data['rows'][tid]['casualty_ok'])
        win_ok = sum(1 for tid in row_ids if _row_passes_win_band(data['rows'][tid]))
        print(f"{value:>7.2f}  " + '  '.join(cells) + f"   {n_ok}/{len(row_ids)}      {win_ok}/{len(row_ids)}")
    print("\ncell = mean LOSER casualty % (target band 15-30%) + whether that row's casualty-realism check passes.")
    print("'win-share(ctrl)' = how many rows still land in the gauge's OWN win-share/rawA band -- the control:")
    print("this sweep must not be allowed to fix casualty realism by breaking the already-passing win-share")
    print("dimension (CLAUDE.md Sec.0.1 pt 4).")


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--worker', action='store_true', help=argparse.SUPPRESS)
    p.add_argument('--expect-value', type=float, default=None, help=argparse.SUPPRESS)
    p.add_argument('--n', type=int, default=_DEFAULT_SCREEN_N)
    p.add_argument('--confirm', type=float, default=None,
                    help='run a single value at the given n (use a larger n, e.g. 60, for the reported number)')
    p.add_argument('--out', default=None, help='write the full JSON results to this path')
    args = p.parse_args()

    if args.worker:
        _worker(args.n, expect_value=args.expect_value)
        return

    row_ids = _multi_subunit_row_ids()

    if args.confirm is not None:
        data = _run_one(args.confirm, args.n)
        _print_table([(args.confirm, data)], row_ids)
        if args.out:
            with open(args.out, 'w') as f:
                json.dump({'mode': 'confirm', 'value': args.confirm, 'n': args.n, 'row_ids': row_ids,
                           'data': data}, f, indent=2)
        return

    results = []
    for value in CANDIDATE_VALUES:
        print(f"... running ROUT_CASCADE_FRAC={value} (n={args.n})", file=sys.stderr)
        results.append((value, _run_one(value, args.n)))
    _print_table(results, row_ids)
    if args.out:
        with open(args.out, 'w') as f:
            json.dump({'mode': 'sweep', 'n': args.n, 'row_ids': row_ids,
                       'results': [{'value': v, 'data': d} for v, d in results]}, f, indent=2)


if __name__ == '__main__':
    main()
