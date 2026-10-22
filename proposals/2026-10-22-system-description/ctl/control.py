import sys
from collections import Counter, defaultdict
sys.path.insert(0, "/home/user/ttrpg")
from engine.season.harness import probes as P
from engine.season.harness.populated import build_realm, SeasonDriver, make_chooser, resolvable_verbs, H, draw_factory
seed = int(sys.argv[1]); seasons = int(sys.argv[2])
w = build_realm(seed); d = SeasonDriver(w)
mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(), draw=draw_factory(w.world_seed, lambda: w.tick))
for s in range(seasons):
    d.season(ch, question=None, subsistence=P.SUBSIST, contest_max_depth=w.fixtures.get("contest_max_depth"))
verb_of = {a.id: a.verb for a in d.resolved}
REF = ("refused", "unavailable", "unauthorized", "unheard", "ineligible", "untold", "none", "blocked", "undecided")
ev = defaultdict(list)
for e in w.log:
    for c in e.causes[:1]:
        if c in verb_of: ev[c].append(e.kind)
att = Counter(verb_of.values())
ok = Counter(); 
for aid, kinds in ev.items():
    if any(not k.split(".")[-1] in REF for k in kinds): ok[verb_of[aid]] += 1
print(f"seed={seed} seasons={seasons} acts={len(d.resolved)} persons_alive={len(w.persons)}")
print("verb attempted ok(non-refusal event)")
for v in sorted(att): print(f"  {v:14s} {att[v]:4d} {ok[v]:4d}")
k = Counter(e.kind for e in w.log)
for kk in ["field.won","field.lost","field.unopposed","army.arrived","march.declared","march.refused","person.died","body.changed","contest.undecided","news.told","matter.turned","finding.made","claim.deposited","claim.decayed","stores.changed","yield.taken","person.individuated"]:
    print(" ", kk, k.get(kk,0))
print("live oblige", sum(1 for t in w.tenures if t.kind=="oblige" and t.live), "cap-200 ledgers", sum(1 for p in w.persons.values() if len(p.ledger)>=200), "of", len(w.persons))
print("capability nonempty", sum(1 for p in w.persons.values() if p.capability), "pursuits empty", sum(1 for p in w.persons.values() if not p.pursuits))
