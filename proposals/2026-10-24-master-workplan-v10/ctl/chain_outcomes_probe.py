import collections, sys
from engine.season.harness import storybar as SB, chronicle as CH, corpus_run as CR
seed=int(sys.argv[1]); seasons=int(sys.argv[2])
w,d,b = SB.drive(seed, seasons, "off")
rows = SB.read(w.log, d.act_of, b)["acts"]
attr = {a.id:(bool(m),bool(r)) for a,m,r in CR.attribute(w,d,seasons)}
st = lambda aid: ("made" if attr[aid]==(True,False) else "refused" if attr[aid]==(False,True) else "both" if attr[aid]==(True,True) else "neither") if aid in attr else "unk"
c = collections.Counter(st(a) for a in rows)
print("seed",seed,"seasons",seasons,"acts in log",len(rows),"outcome",dict(c))
# cross edges
edge = collections.Counter()
for aid,r in rows.items():
    for ant in r["cross"]:
        edge[(st(ant), st(aid))]+=1
tot=sum(edge.values())
print("cross-person edges",tot)
for k,v in sorted(edge.items(), key=lambda kv:-kv[1]): print("  antecedent=%-8s consequent=%-8s %5d  %.1f%%"%(k[0],k[1],v,100*v/tot))
ant_made = sum(v for (a,c_),v in edge.items() if a in("made","both"))
print("edges whose antecedent act succeeded (made or both):",ant_made, "%.1f%%"%(100*ant_made/tot))
# deepest chain
chain = CH.deepest_chain(rows)
print("deepest chain len",len(chain),[st(x) for x in chain])
# depth>=5 acts
deep=[a for a,r in rows.items() if r["depth"]>=5]
print("acts at depth>=5:",len(deep), dict(collections.Counter(st(a) for a in deep)))
# events census
k = collections.Counter(e.kind for e in w.log)
print("distinct event kinds",len(k),"events",len(w.log))
print(k.most_common(40))
print("persons at end",len(getattr(w,'persons',{})))
