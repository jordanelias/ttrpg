"""P3 -- WHY the closers refuse: wrap the driver instance's `_admits` (loop/resolve.py:196, the one
owner of eligibility + requires for both paths) and record, per act attempt of a closer verb:
eligible?, verdict value, the subject's collection kind, and the first failing Observation.

  PYTHONHASHSEED=0 python3 probes/p3_refusal_reasons.py SEASONS SEED [SEED ...]
"""
import sys
from collections import Counter, defaultdict

sys.path.insert(0, "/home/user/ttrpg")

from engine.season.decision import make_chooser
from engine.season.loop.driver import SeasonDriver, resolvable_verbs
from engine.season.loop import resolve as R
from engine.season.state.ids import H, draw_factory
from engine.season.state.carriers import subject_of
from engine.season.harness import probes as P
from engine.season.harness.populated import build_realm

CLOSERS = ["determine", "confer", "covenant", "open_case", "commit", "release", "oblige", "revoke",
           "arrest", "issue", "petition", "found", "build", "work", "give", "restore", "tend",
           "migrate", "research", "examine", "fight", "accept", "challenge"]


def kind_of(w, sid):
    if sid is None:
        return "NONE"
    for c in ("persons", "rungs", "offices", "sites", "records", "propositions", "dates"):
        if sid in getattr(w, c):
            return c
    return "absent"


seasons = int(sys.argv[1])
agg = defaultdict(Counter)
subj = defaultdict(Counter)
obs = defaultdict(Counter)
for seed in [int(s) for s in sys.argv[2:]]:
    w = build_realm(seed, None)
    d = SeasonDriver(w)
    orig = d._admits

    def admits(w_, a, row, _o=orig, _w=w):
        ok, kinds, verdict = _o(w_, a, row)
        if a.verb in CLOSERS:
            el = R._eligible(d, w_, a, row)
            tag = "ok" if ok else ("inelig" if not el else f"req:{verdict.value}")
            agg[a.verb][tag] += 1
            subj[a.verb][(kind_of(_w, subject_of(a)), "ok" if ok else "ref")] += 1
            if ok is False and el:
                for o in (verdict.observed or ())[:3]:
                    obs[a.verb][repr(o)[:110]] += 1
        return ok, kinds, verdict

    d._admits = admits
    mint = lambda pid, verb, sj: H(w.world_seed, w.tick, pid, f"act:{verb}:{sj}")
    ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                      draw=draw_factory(w.world_seed, lambda: w.tick))
    for _ in range(seasons):
        d.season(ch, question=None, subsistence=P.SUBSIST,
                 contest_max_depth=w.fixtures.get("contest_max_depth"))
    print(f"seed={seed} log={len(w.log)} hash={w.content_hash()[:16]}", flush=True)

for v in CLOSERS:
    print(f"{v:11s} {dict(agg[v])}")
    print(f"{'':11s} subject kinds: {dict(subj[v])}")
    for k, n in obs[v].most_common(3):
        print(f"{'':11s}   {n:4d} {k}")
