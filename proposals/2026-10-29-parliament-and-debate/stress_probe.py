"""Stress probe for the debate / social-contest surface of the season loop, with an audit log.

Reads only; changes nothing in the tree. It builds `build_realm(seed)` worlds, ticks them with the
shipped chooser, and writes ONE FLUSHED JSON LINE per event of the run to --log, so a killed run
leaves a trail: a `manifest` line first (HEAD sha, python, PYTHONHASHSEED, argv, UTC start), a
`seed_start` / `season` line per tick, an `error` line with the full traceback for any exception,
a `determinism` line for --determinism, and a closing `summary`. Nothing here is a gate.

NO CHOSEN HORIZON. Neither the number of seeds nor the number of seasons is fixed by this file. Seeds
run in order 0, 1, 2, ... and each world is ticked season after season until the FIRST of: an exception
(`crash`), a season in which the log gained no event at all (`quiescent`), or the caller's wall-clock
budget (`budget`). The log records the horizon each seed reached and which of those stopped it. The
only caller-supplied resource is --budget-s; --seeds / --seasons are optional ceilings and are absent
unless given. --determinism is the one mode that needs equal horizons, so it takes --seasons.

Usage (from the repo root):
  python proposals/2026-10-29-parliament-and-debate/stress_probe.py --label base --budget-s 3600 --log OUT.jsonl
  ... --rule all            sweeps question_aggregation_rule
  ... --bench-quorum 3      sweeps bench_quorum
  ... --determinism --seasons N   runs seed 0 twice for N seasons and compares event counts
"""
import argparse, json, os, subprocess, sys, time, traceback, datetime
from collections import Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, ROOT)
from engine.season.harness.populated import (build_realm, make_chooser, SeasonDriver,
                                             resolvable_verbs, H, draw_factory, P)

WATCH = ['date.scheduled', 'date.fired', 'case.opened', 'matter.determined', 'determine.refused',
         'commitment.made', 'commitment.refused', 'commitment.ended', 'duty.taken', 'duty.refused',
         'petition.filed', 'give.refused', 'rung.ceded', 'term.matured', 'convene.refused',
         'person.died']


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')


class Log:
    def __init__(self, path):
        self.f = open(path, 'a', encoding='utf-8', buffering=1)

    def w(self, kind, **kw):
        self.f.write(json.dumps({'t': utc(), 'kind': kind, **kw}, default=str) + '\n')
        self.f.flush()
        os.fsync(self.f.fileno())


def git(*a):
    try:
        return subprocess.run(['git', *a], cwd=ROOT, capture_output=True, text=True, timeout=30).stdout.strip()
    except Exception as e:  # the manifest must never stop the run
        return f'unavailable: {e}'


def make_world(seed, rule, quorum):
    w = build_realm(seed)
    if rule:
        w.fixtures = w.fixtures.sweep('question_aggregation_rule', rule)
    if quorum is not None:
        w.fixtures = w.fixtures.sweep('bench_quorum', quorum)
    d = SeasonDriver(w)
    mint = lambda pid, verb, subj, w=w: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                      draw=draw_factory(w.world_seed, lambda w=w: w.tick))
    return w, d, ch


def kind_counts(w):
    return Counter(e.kind for e in w.log)


def season_row(w, before, after, secs, seed, s):
    delta = {k: after.get(k, 0) - before.get(k, 0) for k in WATCH}
    arg = {k: v - before.get(k, 0) for k, v in after.items() if k.startswith('argument.') and v - before.get(k, 0)}
    docket = w.docket
    empty = sum(1 for x in docket if x.get('matter') is None)
    return {'seed': seed, 'season': s + 1, 'tick': w.tick, 'wall_s': round(secs, 2),
            'events_total': sum(after.values()), 'watch_delta': delta, 'argument_delta': arg,
            'dates': len(w.dates), 'docket': len(docket), 'docket_empty_slots': empty,
            'persons': len(w.persons)}


def run_seed(log, label, seed, seasons, rule, quorum, deadline=None):
    """Tick one world. `seasons` is an optional ceiling (None = unbounded). Returns (final counts, stop
    reason, seasons reached); counts is None on a crash."""
    log.w('seed_start', label=label, seed=seed, season_ceiling=seasons)
    t0 = time.time()
    s = 0
    reason = None
    try:
        w, d, ch = make_world(seed, rule, quorum)
        log.w('built', label=label, seed=seed, build_s=round(time.time() - t0, 2))
        while True:
            if seasons is not None and s >= seasons:
                reason = 'ceiling'
                break
            if deadline is not None and time.time() >= deadline:
                reason = 'budget'
                break
            before = kind_counts(w)
            t = time.time()
            d.season(ch, question=None, subsistence=P.SUBSIST, contest_max_depth=w.fixtures.get('contest_max_depth'))
            after = kind_counts(w)
            row = season_row(w, before, after, time.time() - t, seed, s)
            log.w('season', label=label, **row)
            s += 1
            if row['events_total'] == sum(before.values()):
                reason = 'quiescent'
                break
        final = kind_counts(w)
        h = getattr(w, 'content_hash', None)
        log.w('seed_end', label=label, seed=seed, stop=reason, seasons_reached=s, wall_s=round(time.time() - t0, 1),
              content_hash=(h() if callable(h) else None),
              watch_total={k: final.get(k, 0) for k in WATCH},
              argument_total={k: v for k, v in final.items() if k.startswith('argument.')})
        return final, reason, s
    except Exception as e:
        log.w('error', label=label, seed=seed, season_reached=s, stop='crash', type=type(e).__name__,
              message=str(e)[:400], traceback=traceback.format_exc())
        return None, 'crash', s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--label', required=True)
    ap.add_argument('--seeds', type=int, default=None, help='optional ceiling on seeds; absent = unbounded')
    ap.add_argument('--seasons', type=int, default=None, help='optional ceiling on seasons per seed')
    ap.add_argument('--budget-s', type=float, dest='budget', default=None,
                    help='wall-clock budget for the whole run; required unless --determinism')
    ap.add_argument('--rule')
    ap.add_argument('--bench-quorum', type=int, dest='quorum')
    ap.add_argument('--determinism', action='store_true')
    ap.add_argument('--log', required=True)
    a = ap.parse_args()
    log = Log(a.log)
    log.w('manifest', label=a.label, argv=sys.argv, head=git('rev-parse', 'HEAD'),
          branch=git('rev-parse', '--abbrev-ref', 'HEAD'), dirty=git('status', '--porcelain')[:400],
          python=sys.version.split()[0], platform=sys.platform,
          pythonhashseed=os.environ.get('PYTHONHASHSEED'), pythonutf8=os.environ.get('PYTHONUTF8'))
    t0 = time.time()
    totals, ok, bad, stops = Counter(), 0, 0, Counter()
    if a.determinism:
        if a.seasons is None:
            ap.error('--determinism needs --seasons (equal horizons)')
        res = []
        for rep in (1, 2):
            c, _, _ = run_seed(log, f'{a.label}-rep{rep}', 0, a.seasons, a.rule, a.quorum)
            res.append(c)
        same = res[0] is not None and res[1] is not None and res[0] == res[1]
        log.w('determinism', label=a.label, identical_event_counts=same,
              kinds_differing=sorted(k for k in set((res[0] or {}).keys()) | set((res[1] or {}).keys())
                                     if (res[0] or {}).get(k) != (res[1] or {}).get(k))[:40])
    else:
        if a.budget is None:
            ap.error('--budget-s is required (the only resource limit; no horizon is chosen here)')
        deadline = t0 + a.budget
        sd = 0
        while (a.seeds is None or sd < a.seeds) and time.time() < deadline:
            c, reason, reached = run_seed(log, a.label, sd, a.seasons, a.rule, a.quorum, deadline)
            stops[reason] += 1
            if c is None:
                bad += 1
            else:
                ok += 1
                for k in WATCH:
                    totals[k] += c.get(k, 0)
            sd += 1
    log.w('summary', label=a.label, seeds_ok=ok, seeds_failed=bad, stops=dict(stops),
          wall_s=round(time.time() - t0, 1), watch_total=dict(totals))


if __name__ == '__main__':
    main()
