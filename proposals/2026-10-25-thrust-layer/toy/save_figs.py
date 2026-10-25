# re-run, SAVED, the two toy figures that were only printed earlier (design v1 cited them from the terminal)
import random, regimes10 as R
N=300
def mean(ms,k): return sum(m[k] for m in ms)/len(ms)
CON=dict(death_p=0.01,gate_p=0.9,accuse=True,truce=True,conseq=True,lethal=False,tdr_kill=False)
print("== chain depth, constrained world (cross-person causal chain depth), N=300")
for reg in ('BU','HYg3','HYg3d','HYg3c'):
    ms=[R.run_metrics(R.simulate(s,reg,con=CON)[0]) for s in range(N)]
    print(f"{reg:7} depth {mean(ms,'depth'):.1f}")
print("== unconstrained world depth (the 62.5 vs 23.0 figure)")
for reg in ('BU','HYg3'):
    ms=[R.run_metrics(R.simulate(s,reg)[0]) for s in range(N)]
    print(f"{reg:7} depth {mean(ms,'depth'):.1f}")
print("== killing at season 10, HYg3d world, constrained, conseq on")
acts=[];actors=[];trib=[]
for s in range(N):
    ev1,_=R.simulate(s,'HYg3d',con=CON,killing_t=10)
    kill=[e for e in ev1 if e.get('death')]
    if not kill: continue
    k=kill[0]['actor']
    ag=[e for e in R.executed(ev1) if e['t']>10 and e.get('target')==k and e['verb'] in ('harm','accuse','claim')]
    acts.append(len(ag)); actors.append(len({e['actor'] for e in ag}))
    trib.append(sum(1 for e in ev1 if e['verb']=='rule' and e['t']>10 and (e['actor']==k or e.get('target')==k)))
print("acts against killer %.2f  distinct actors %.2f  tribunals naming killer %.2f  (n=%d)"%(sum(acts)/len(acts),sum(actors)/len(actors),sum(trib)/len(trib),len(acts)))
