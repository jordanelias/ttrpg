"""Read-only probe: Event kinds and folded acts after N seasons of one seeded realm, shipped chooser.
Usage: python probe_event_kinds.py SEED SEASONS > out.json   (the shipped runs: 0 4 and 1 4).
After the run, only the sys.path line was made relative."""
import sys, json
from pathlib import Path
from collections import Counter
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # repo root
from engine.season.harness import populated as P
from engine.season.loop.driver import SeasonDriver, resolvable_verbs
from engine.season.decision import make_chooser
from engine.season.state.ids import H, draw_factory
seed = int(sys.argv[1]); N = int(sys.argv[2])
w = P.build_realm(seed)
d = SeasonDriver(w)
mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(), draw=draw_factory(w.world_seed, lambda: w.tick))
for s in range(N):
    d.season(ch, question=None, contest_max_depth=w.fixtures.get("contest_max_depth"))
ek = Counter(e.kind for e in w.log)
acts = Counter(a.verb for a in d.resolved)
print(json.dumps({"seed": seed, "seasons": N,
  "event_kinds": dict(sorted(ek.items(), key=lambda kv: -kv[1])),
  "resolved_acts_by_verb": dict(acts.most_common()),
  "docket": [{k: (v if k != 'matter' else v) for k, v in x.items()} for x in w.docket][:40],
  "dates": len(w.dates) if hasattr(w, 'dates') else None,
  "commits_live": sum(1 for t in w.tenures if t.live and t.kind=='commit'),
  "commit_objects_mood": dict(Counter(str(w.propositions[t.object].mood).upper() for t in w.tenures if t.live and t.kind=='commit' and t.object in w.propositions)),
  }, indent=1, default=str))
