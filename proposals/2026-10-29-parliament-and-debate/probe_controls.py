"""Read-only controls for the claims in 2026-11-01-social-contest-matters-standpoints-and-fold.md.
Usage: python probe_controls.py SEED SEASONS > out.json   (the shipped run: 0 4; about four minutes).
Builds the realm for one seed, measures before the first season (tick 0), ticks it with the shipped chooser,
and measures again. Writes nothing in the tree. Controls:
  C1 what comply / evade-defy acts were formed on, and whether the actor held it;
  C2 who holds each forged sheet at the end;
  C3 whether any docket item holds both a date and a matter at any season end;
  C4 opinion_of spread at tick 0 against the end (exceptions counted, not dropped);
  C5 confidence differences between copies of one claim deposited in the same season."""
import sys, json, statistics
from pathlib import Path
from collections import Counter, defaultdict
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # repo root
from engine.season.harness import populated as P
from engine.season.loop.driver import SeasonDriver, resolvable_verbs
from engine.season.decision import make_chooser
from engine.season.state.ids import H, draw_factory
from engine.season.queries import world_q

seed = int(sys.argv[1]); N = int(sys.argv[2])
w = P.build_realm(seed)
d = SeasonDriver(w)
mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(), draw=draw_factory(w.world_seed, lambda: w.tick))

def opinions():
    out, errs = {}, Counter()
    for fprop, name in world_q.FACTION_BY_PROP.items():
        vals = []
        for p in w.persons.values():
            try: vals.append(world_q.opinion_of(w, p, fprop))
            except Exception as ex: errs[type(ex).__name__] += 1
        if vals:
            out[name] = dict(n=len(vals), neg=sum(v < 0 for v in vals), pos=sum(v > 0 for v in vals),
                             sd=round(statistics.pstdev(vals), 3), min=round(min(vals), 2), max=round(max(vals), 2))
    return out, dict(errs)

res = {"seed": seed, "seasons": N, "persons_at_build": len(w.persons)}
res["opinion_t0"], res["opinion_t0_exceptions"] = opinions()
res["stance_rows_t0"] = sum(len(p.stance) for p in w.persons.values())
filled_by_season = []
for s in range(N):
    d.season(ch, question=None, contest_max_depth=w.fixtures.get("contest_max_depth"))
    filled_by_season.append(sum(1 for x in w.docket if x.get("date") is not None and x.get("matter") is not None))
res["persons_at_end"] = len(w.persons)
res["C3_docket_items_with_date_and_matter_at_each_season_end"] = filled_by_season
res["opinion_end"], res["opinion_end_exceptions"] = opinions()

# C1: what the writ-answering acts were formed on
c1 = Counter(); held = Counter(); addressed = Counter()
for a in d.resolved:
    if a.verb not in ("comply", "evade / defy"): continue
    subj = (a.payload or {}).get("subject") if isinstance(a.payload, dict) else None
    rec = w.records.get(subj)
    kind = ("record:" + rec.kind) if rec is not None else ("person" if subj in w.persons else
            ("proposition" if subj in w.propositions else "other"))
    c1[(a.verb, kind)] += 1
    if rec is not None:
        holds = any(t.kind == "hold" and t.object == subj and t.subject == a.actor for t in w.tenures)
        held[(a.verb, kind, "actor_holds" if holds else "actor_does_not_hold")] += 1
        if rec.kind == "dispensation":
            to = (rec.subject_matter or {}).get("to") or []
            addressed[(a.verb, "actor_is_addressee" if a.actor in to else "actor_not_addressee")] += 1
res["C1_comply_evade_by_subject"] = {f"{v}|{k}": n for (v, k), n in c1.items()}
res["C1_held"] = {"|".join(k): n for k, n in held.items()}
res["C1_dispensation_addressee"] = {"|".join(k): n for k, n in addressed.items()}
res["C1_dispensations_in_world"] = sum(1 for r in w.records.values() if r.kind == "dispensation")

# C2: holders of forged records (a forgery carries quality > 0)
forged = [r for r in w.records.values() if getattr(r, "forgery_quality", 0)]
per = []
for r in forged:
    hs = [t.subject for t in w.tenures if t.live and t.kind == "hold" and t.object == r.id]
    per.append(len(set(hs)))
res["C2_forged_records"] = len(forged)
res["C2_holders_per_forged_record"] = dict(Counter(per))

# C5: copies of one claim (same subject, predicate, deposit season) held by 2+ persons
g = defaultdict(list)
for p in w.persons.values():
    for c in p.ledger:
        g[(c.subject, c.predicate, c.when)].append((p.id, c.confidence, c.source))
multi = [v for v in g.values() if len({x[0] for x in v}) >= 2]
res["C5_same_season_copy_groups"] = len(multi)
res["C5_of_which_confidence_differs"] = sum(1 for v in multi if len({x[1] for x in v}) > 1)
res["C5_of_which_source_differs"] = sum(1 for v in multi if len({x[2] for x in v}) > 1)
print(json.dumps(res, indent=1, default=str))
