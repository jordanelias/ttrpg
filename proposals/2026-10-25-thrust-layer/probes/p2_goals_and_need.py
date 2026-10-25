"""P2 -- goals.yaml by object kind / org kind; what seed_goals minted; ambitions; and, over a run,
the occasion source of every Scene the driver built (d.scenes, the Scene's `occasion`, the reader
harness/soak.py::_occasion_row uses) plus news.told counts.

  PYTHONHASHSEED=0 python3 probes/p2_goals_and_need.py SEASONS SEED [SEED ...]
"""
import sys
from collections import Counter

sys.path.insert(0, "/home/user/ttrpg")

from engine.season.data import goals as G
from engine.season.decision import make_chooser
from engine.season.loop.driver import SeasonDriver, resolvable_verbs
from engine.season.state.ids import H, draw_factory
from engine.season.harness import probes as P
from engine.season.harness.populated import build_realm
from engine.season.queries import world_q as WQ

rows = G.goals()
print("GOAL ROWS", len(rows))
print(" by object kind", dict(Counter(g.object["kind"] for g in rows)))
print(" by org kind", dict(Counter(g.org_kind for g in rows)))
print(" seat rows", [(g.id, g.org) for g in rows if g.org_kind == "seat"])
print(" orientation ids", sorted(g.id for g in rows if g.object["kind"] == "orientation"))

seasons = int(sys.argv[1])
for seed in [int(s) for s in sys.argv[2:]]:
    w = build_realm(seed, None)
    minted = [g.id for g in rows if g.id in w.propositions]
    commits = Counter(t.object for t in w.tenures if t.kind == "commit" and t.live
                      and t.object in {g.id for g in rows})
    amb_persons = sum(1 for p in w.persons.values() if any(a in commits for a in WQ.ambitions(w, p)))
    with_need = 0
    for p in w.persons.values():
        if any(WQ.goal_referents(w, p, w.propositions[a]) for a in WQ.ambitions(w, p)):
            with_need += 1
    print(f"seed={seed} persons={len(w.persons)} goal_props_minted={len(minted)}/{len(rows)} "
          f"goal_commit_edges={sum(commits.values())} goals_with_committers={len(commits)} "
          f"persons_with_goal_ambition={amb_persons} persons_with_nonempty_need_at_t0={with_need}")
    print("  uncommitted non-orientation goals:",
          sorted(g.id for g in rows if g.object["kind"] != "orientation" and commits.get(g.id, 0) == 0))
    d = SeasonDriver(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                      draw=draw_factory(w.world_seed, lambda: w.tick))
    for _ in range(seasons):
        d.season(ch, question=None, subsistence=P.SUBSIST,
                 contest_max_depth=w.fixtures.get("contest_max_depth"))
    src = Counter()
    need_goal = Counter()
    for sc in d.scenes.values():
        q = getattr(sc, "occasion", None)
        src[q.source if q is not None else None] += 1
        if q is not None and q.source == "need":
            need_goal["goal" if G.goal(q.about) else "other"] += 1
    acts_src = Counter()
    for a in d.resolved:
        sc = d.scenes.get(a.scene) if a.scene else None
        q = getattr(sc, "occasion", None) if sc is not None else None
        acts_src[q.source if q is not None else None] += 1
    kinds = Counter(e.kind for e in w.log)
    print(f"  scenes={len(d.scenes)} by occasion source={dict(src)} need-about-goal={dict(need_goal)}")
    print(f"  resolved acts={len(d.resolved)} by occasion source={dict(acts_src)}")
    print(f"  log={len(w.log)} news.told={kinds.get('news.told', 0)} news.untold={kinds.get('news.untold', 0)} "
          f"person.died={kinds.get('person.died', 0)} hash={w.content_hash()[:16]}")
