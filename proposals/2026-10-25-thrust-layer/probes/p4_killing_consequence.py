"""P4 -- what a death does, read off REAL deaths in computed play (the shipped realm, no planting
needed: P1/P2 show 1-4 `person.died` per seed in two seasons). For each person removed in season s:
  * the seats he held at the start of s (live `hold` tenures);
  * claims in surviving ledgers whose subject is the dead man (by predicate), and the number of
    scene occasions after his death whose referents include him or whose `about` is such a claim;
  * claims whose subject is one of his seats, minted at or after s (vacancy claims, H-206);
  * the killer (actor of the act whose Event the `person.died` Event cites, if any) and the number of
    later scene occasions whose referents include the killer AND whose `about` is a claim about the
    dead man (a consequence question, H-209).
  PYTHONHASHSEED=0 python3 probes/p4_killing_consequence.py SEASONS SEED [SEED ...]
"""
import sys
from collections import Counter

sys.path.insert(0, "/home/user/ttrpg")

from engine.season.decision import make_chooser
from engine.season.loop.driver import SeasonDriver, resolvable_verbs
from engine.season.state.ids import H, draw_factory
from engine.season.harness import probes as P
from engine.season.harness.populated import build_realm

seasons = int(sys.argv[1])
TOT = Counter()
for seed in [int(s) for s in sys.argv[2:]]:
    w = build_realm(seed, None)
    d = SeasonDriver(w)
    mint = lambda pid, verb, sj: H(w.world_seed, w.tick, pid, f"act:{verb}:{sj}")
    ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                      draw=draw_factory(w.world_seed, lambda: w.tick))
    deaths = []
    scene_seen = set()
    for s in range(seasons):
        before = set(w.persons)
        holds = {}
        for t in w.tenures:
            if t.kind == "hold" and t.live and t.subject in before:
                holds.setdefault(t.subject, []).append(t.object)
        n0 = len(w.log)
        d.season(ch, question=None, subsistence=P.SUBSIST,
                 contest_max_depth=w.fixtures.get("contest_max_depth"))
        gone = before - set(w.persons)
        died_ev = [e for e in w.log[n0:] if e.kind == "person.died"]
        for v in sorted(gone):
            killer = None
            for e in died_ev:
                if v in repr(e.changes):
                    a = d.act_of.get(e.id)
                    killer = (a.actor, a.verb) if a is not None else ("<no act: MATTER/ENCOUNTER>", e.causes[:1])
            deaths.append({"v": v, "season": s, "seats": [o for o in holds.get(v, []) if o in w.offices],
                           "killer": killer, "scene_mark": len(d.scenes)})
    # read after the run
    claims = [c for p in w.persons.values() for c in p.ledger]
    by_id = {c.id: c for c in claims}
    later_scenes = list(d.scenes.values())
    for dd in deaths:
        v, s = dd["v"], dd["season"]
        about_v = [c for c in claims if c.subject == v]
        preds = Counter(c.predicate for c in about_v)
        seat_claims = [c for c in claims if c.subject in dd["seats"] and c.when >= s]
        seat_preds = Counter(c.predicate for c in seat_claims)
        occ_v = 0
        occ_killer = 0
        for sc in later_scenes[dd["scene_mark"]:]:
            q = getattr(sc, "occasion", None)
            if q is None:
                continue
            ab = by_id.get(q.about)
            if v in (q.referents or ()) or (ab is not None and ab.subject == v):
                occ_v += 1
                if dd["killer"] and dd["killer"][0] in (q.referents or ()):
                    occ_killer += 1
        print(f"seed={seed} dead={v} season={s} seats={dd['seats']} killer={dd['killer']} "
              f"claims_about_dead={len(about_v)} preds={dict(preds)} seat_claims_after={len(seat_claims)} "
              f"seat_claim_preds={dict(seat_preds)} occasions_after_naming_dead={occ_v} occasions_naming_killer_about_dead={occ_killer}")
        TOT["deaths"] += 1
        TOT["seat_holders"] += bool(dd["seats"])
        TOT["with_killer"] += bool(dd["killer"])
        TOT["claims_about_dead"] += len(about_v)
        TOT["occasions_naming_dead"] += occ_v
        TOT["seat_claims_after"] += len(seat_claims)
    print(f"seed={seed} log={len(w.log)} hash={w.content_hash()[:16]}", flush=True)
print("TOTAL", dict(TOT))
