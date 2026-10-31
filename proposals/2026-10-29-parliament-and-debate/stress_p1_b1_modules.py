"""P1 B1's own observable (section 6): 'sys.modules after a season holds no systems.social_contest; same-seed content_hash equal twice'.
Run INSIDE a worktree (cwd = worktree root): once on the unmodified control, once on the end-state of B1 applied.
  cd <worktree> && PYTHONPATH=. python <path>/stress_p1_b1_modules.py --label control|end-state --log <abs jsonl>"""
import argparse, datetime, json, os, sys, time, traceback
ap = argparse.ArgumentParser(); ap.add_argument('--label', required=True); ap.add_argument('--log', required=True); a = ap.parse_args()
sys.path.insert(0, os.getcwd())
f = open(os.path.abspath(a.log), 'a', encoding='utf-8', buffering=1)
def W(kind, **kw):
    f.write(json.dumps({'t': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'), 'kind': kind, 'label': a.label, **kw}, default=str) + '\n'); f.flush(); os.fsync(f.fileno())
W('manifest', cwd=os.getcwd(), python=sys.version.split()[0], pythonhashseed=os.environ.get('PYTHONHASHSEED'), what='B1 observable: sys.modules after one season; content_hash twice')
try:
    from engine.season.harness.populated import build_realm, make_chooser, SeasonDriver, resolvable_verbs, H, draw_factory, P
    hashes = []
    for rep in (1, 2):
        t0 = time.time()
        w = build_realm(0); d = SeasonDriver(w)
        mint = lambda pid, verb, subj, w=w: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
        ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(), draw=draw_factory(w.world_seed, lambda w=w: w.tick))
        d.season(ch, question=None, subsistence=P.SUBSIST, contest_max_depth=w.fixtures.get('contest_max_depth'))
        hashes.append(w.content_hash())
        mods = sorted(m for m in sys.modules if m.startswith('systems.social_contest'))
        W('trial', n=1, rep=rep, wall_s=round(time.time() - t0, 1), content_hash=hashes[-1], systems_social_contest_modules_loaded=mods)
    W('result', same_hash_twice=hashes[0] == hashes[1], systems_social_contest_loaded=bool(mods), loaded=mods[:6])
except BaseException:
    W('error', traceback=traceback.format_exc())
W('summary', stop='done or crash')
