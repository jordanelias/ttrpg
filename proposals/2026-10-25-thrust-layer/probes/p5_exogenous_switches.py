"""P5 -- the dark exogenous-motion switches: each set to a TEST ARM named in its own fixture comment
(data/fixtures.py), one at a time, against the shipped control, same seed, 2 seasons. Reports the
content hash, log length, person.died, body.changed, site-condition events and executed restore/tend.
Arms are the comments' own sweep values, not chosen values.

  PYTHONHASHSEED=0 python3 probes/p5_exogenous_switches.py SEED
"""
import sys
from collections import Counter

sys.path.insert(0, "/home/user/ttrpg")

from engine.season.decision import make_chooser
from engine.season.loop.driver import SeasonDriver, resolvable_verbs
from engine.season.state.ids import H, draw_factory
from engine.season.harness import probes as P
from engine.season.harness.populated import build_realm

ARMS = [("control", {}),
        ("body_step=10", {"body_step": 10}),
        ("age_step=0.01", {"age_step": 0.01}),
        ("illness_rate=0.05", {"illness_rate": 0.05}),
        ("age_at_build=160,age_step=0.01", {"age_at_build": 160, "age_step": 0.01}),
        ("season_factor_draw=(0.5,1,2)x4", {"season_factor_draw": ((0.5, 1.0, 2.0),) * 4}),
        ("lattice_coupling=250", {"lattice_coupling": 250}),
        ("season_factor_draw=(0.5,)x4", {"season_factor_draw": ((0.5,),) * 4})]

seed = int(sys.argv[1])
only = sys.argv[2:]
for name, arm in ARMS:
    if only and name not in only:
        continue
    try:
        w = build_realm(seed, None)
        for k, v in arm.items():
            w.fixtures = w.fixtures.sweep(k, v)
        d = SeasonDriver(w)
        mint = lambda pid, verb, sj: H(w.world_seed, w.tick, pid, f"act:{verb}:{sj}")
        ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                          draw=draw_factory(w.world_seed, lambda: w.tick))
        for _ in range(2):
            d.season(ch, question=None, subsistence=P.SUBSIST,
                     contest_max_depth=w.fixtures.get("contest_max_depth"))
        k = Counter(e.kind for e in w.log)
        cond = sum(n for kk, n in k.items() if kk.startswith("site.") or "condition" in kk)
        vac = sum(1 for o in w.offices if not any(t.kind == "hold" and t.live and t.object == o
                                                  for t in w.tenures))
        print(f"{name:34s} hash={w.content_hash()[:12]} log={len(w.log)} persons={len(w.persons)} "
              f"died={k.get('person.died', 0)} body.changed={k.get('body.changed', 0)} site/condition_ev={cond} "
              f"vacant_offices={vac}", flush=True)
    except Exception as e:  # report, never hide
        print(f"{name:34s} RAISED {type(e).__name__}: {str(e)[:200]}", flush=True)
