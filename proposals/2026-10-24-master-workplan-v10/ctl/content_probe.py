"""Counterfactual content probe: run the shipped season loop with content that exists or could be seated
switched on, and read what the engine does differently. Observation only.
usage: PYTHONPATH=<repo> python content_probe.py ARM SEED SEASONS OUT.json
ARM in: baseline | foreign | guards | foreign_guards | capability | exogenous | all"""
import sys, json, collections
from engine.season.harness import corpus_run as CR
from engine.season.harness.populated import build_realm
from engine.season.harness import probes as P
from engine.season.decision import make_chooser
from engine.season.state.ids import H, draw_factory
from engine.season.loop.driver import SeasonDriver, resolvable_verbs
arm, seed, seasons, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
kw = {}
if arm in ("foreign", "foreign_guards", "all"): kw["foreign"] = True
if arm in ("guards", "foreign_guards", "all"): kw["guards"] = True
w = build_realm(seed, None, **kw)
if arm in ("capability", "all"):
    for pid, p in sorted(w.persons.items()):
        p.capability = {"copying": 1 + sum(map(ord, str(pid))) % 3}
if arm in ("exogenous", "all"):
    w.fixtures._v["season_factor_draw"] = ((0.5, 1.0, 2.0),) * 4
persons0 = len(w.persons)
d = SeasonDriver(w)
mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(), draw=draw_factory(w.world_seed, lambda: w.tick))
for _ in range(seasons):
    d.season(ch, question=None, subsistence=P.SUBSIST, contest_max_depth=w.fixtures.get("contest_max_depth"))
fun = collections.defaultdict(collections.Counter)
for a, made, refused in CR.attribute(w, d, seasons):
    fun[a.verb]["made" if made else "x"] += 1
    fun[a.verb]["refused" if refused else "y"] += 1
ex = collections.Counter({v: c["made"] for v, c in fun.items() if c["made"]})
T = sum(ex.values())
H_ = sum((n / T) ** 2 for n in ex.values()) if T else 0
kinds = collections.Counter(e.kind for e in w.log)
res = {"arm": arm, "seed": seed, "seasons": seasons, "hash": w.content_hash()[:12], "persons_start": persons0, "persons_end": len(w.persons),
       "events": len(w.log), "resolved": len(d.resolved), "executed": T,
       "executed_verbs": len(ex), "effective_verbs": round(1 / H_, 1) if H_ else 0,
       "top3_share": round(sum(n for _, n in ex.most_common(3)) / T, 3) if T else 0,
       "event_kinds": len(kinds),
       "field_events": {k: n for k, n in kinds.items() if k.startswith(("field.", "army.", "battle.", "siege."))},
       "march": {k: kinds.get(k, 0) for k in ("march.declared", "march.refused", "army.arrived")},
       "deaths": kinds.get("person.died", 0), "decayed": kinds.get("claim.decayed", 0),
       "executed_by_verb": dict(ex.most_common(60))}
json.dump(res, open(out, "w"), indent=1)
print(json.dumps({k: v for k, v in res.items() if k != "executed_by_verb"}))
