"""Read-only probe: what worldly matters reach a person's ledger and question set, and how far standpoints diverge.
Usage: python probe_matters_intake.py SEED SEASONS > out.json   (the shipped run: 0 4; about four minutes).
Builds the realm for one seed and ticks it with the shipped chooser. Writes nothing in the tree.
Note: the key `stamped_class_on_first_question` lists referent ids, not classes (a mislabel, left as run).
After the run, only the sys.path line was made relative and a no-op loop removed."""
import sys, json, statistics
from pathlib import Path
from collections import Counter, defaultdict
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # repo root
from engine.season.harness import populated as P
from engine.season.loop.driver import SeasonDriver, resolvable_verbs
from engine.season.decision import make_chooser
from engine.season.state.ids import H, draw_factory
from engine.season.queries import world_q, person_q
from engine.season.data import rosters

seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
N = int(sys.argv[2]) if len(sys.argv) > 2 else 4
w = P.build_realm(seed)
d = SeasonDriver(w)
mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(), draw=draw_factory(w.world_seed, lambda: w.tick))
out = {"seed": seed, "seasons": N, "persons": len(w.persons)}

qsrc, qcls, qfirst = Counter(), Counter(), Counter()
for s in range(N):
    # question projection a season would see at its start
    for p in w.persons.values():
        qs = world_q.questions_for(w, p)
        for q in qs:
            qsrc[q.source] += 1
        if qs:
            qfirst[qs[0].source] += 1
            for rc in qs[0].classes:
                qcls[rc[0] if isinstance(rc, tuple) else str(rc)] += 1
    d.season(ch, question=None, contest_max_depth=w.fixtures.get("contest_max_depth"))

out["questions_at_each_season_start_sum"] = dict(qsrc)
out["first_question_source"] = dict(qfirst)
out["stamped_class_on_first_question"] = dict(qcls)
pred = Counter(c.predicate.partition(":")[0] for p in w.persons.values() for c in p.ledger)
out["ledger_claims_by_predicate_stem"] = dict(pred.most_common(25))
out["ledger_claims_total"] = sum(pred.values())
out["claim_source"] = dict(Counter(c.source for p in w.persons.values() for c in p.ledger))
ek = Counter(e.kind for e in w.log)
out["event_kinds_top"] = dict(ek.most_common(40))
out["docket_items"] = len(w.docket)
out["docket_with_arrangement"] = sum(1 for x in w.docket if x.get("arrangement"))
out["records_by_kind"] = dict(Counter(r.kind for r in w.records.values()))
out["propositions_by_mood"] = dict(Counter(str(p.mood).upper() for p in w.propositions.values()))
tk = Counter(t.kind for t in w.tenures if t.live)
out["live_tenures_by_kind"] = dict(tk)
# standpoint divergence: opinion_of each faction across persons
div = {}
try:
    from engine.season.queries.world_q import FACTION_BY_PROP
except Exception:
    FACTION_BY_PROP = {}
for fprop, name in FACTION_BY_PROP.items():
    vals = []
    for p in w.persons.values():
        try: vals.append(world_q.opinion_of(w, p, fprop))
        except Exception as ex: pass
    if vals:
        div[name] = dict(n=len(vals), min=round(min(vals),2), max=round(max(vals),2),
                         mean=round(statistics.mean(vals),2), sd=round(statistics.pstdev(vals),2),
                         neg=sum(1 for v in vals if v<0), pos=sum(1 for v in vals if v>0))
out["opinion_of_faction_across_persons"] = div
# claims about the same subject held differently
bysubj = defaultdict(list)
for p in w.persons.values():
    for c in p.ledger:
        bysubj[(c.subject, c.predicate.partition(":")[0])].append((p.id, c.value, c.confidence, c.source))
multi = [(k, v) for k, v in bysubj.items() if len(v) >= 2]
differ_val = sum(1 for k, v in multi if len({repr(x[1]) for x in v}) > 1)
differ_conf = sum(1 for k, v in multi if len({x[2] for x in v}) > 1)
differ_src = sum(1 for k, v in multi if len({x[3] for x in v}) > 1)
out["subject_predicate_pairs_held_by_2plus"] = len(multi)
out["of_which_values_differ"] = differ_val
out["of_which_confidence_differs"] = differ_conf
out["of_which_source_differs"] = differ_src
# pursuit spread
pc = defaultdict(list)
for p in w.persons.values():
    for k, v in (p.pursuits or {}).items():
        pc[k].append(v)
out["pursuit_spread"] = {k: dict(n=len(v), min=round(min(v),2), max=round(max(v),2), sd=round(statistics.pstdev(v),2)) for k, v in pc.items()}
out["persons_with_capability"] = sum(1 for p in w.persons.values() if p.capability)
out["persons_with_conviction"] = sum(1 for p in w.persons.values() if p.conviction)
out["offices"] = len(w.offices)
print(json.dumps(out, indent=1, default=str))
