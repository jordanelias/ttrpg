# Part 06 evidence: the 104-moment demand matrix scripts and the P2 probe, with their output

## Status: PROPOSED (2026-10-28 session; reconstructed 2026-10-30) — HELD BACK IN FULL. Reference under CLAUDE.md §0.05: not a mechanism; merging ratifies nothing.
## Lane: IN

## Provenance

The scripts and printed output behind part 06 and part 03's cell counts, recovered 2026-10-30 from the 2026-10-28 transcript (heredoc bodies and tool results, timestamps in each heading). The scripts ran in the session's scratchpad against the tree at `be24c71`; they are evidence of how the counts were made, not tools of this repository, and nothing here has been re-run. `matrix.py`'s moments are the analyst's own enumeration.

---
### matrix.py (06:39:12Z)

~~~
# Demand matrix: moment -> (subsystem, status, primary capacities, secondary capacities). [REASONED mapping]
# status: B = built season contest/graded; M = module code reads it (T2, off season path); D = designed (lexicon) draw
import itertools, collections
CAP = {'force':'STR','tough':'END','quick':'AGI','hand':'AGI','reason':'ACU','notice':'ATT','readp':'ATT',
       'presence':'CHA','warmth':'BON','resolve':'WIL','attend':'FOC','thread':'TS',
       'stealth':None,'lore':None}
M = [
# built season moments
('fight','PC','B',['force','quick','tough'],['readp','resolve','attend']),
('accept','PC','B',['force','quick','tough'],['resolve']),
('march','MB','B',['presence','reason'],[]),
('tell','SC','B',['presence'],['readp']),
('speak','SC','B',['presence','reason'],[]),
('argue','SC','B',['reason'],['presence']),
('determine','SC','B',['reason'],['readp']),
('arrest','GV','B',['presence'],['force']),
('research','FI','B',['reason'],['attend','lore']),
('examine','FI','B',['notice','reason'],[]),
('surveil','FI','B',['notice'],['attend','stealth']),
# module moments (T2 code)
('combat.impact/handling','PC','M',['force'],[]),
('combat.tempo/reflex/balance','PC','M',['quick'],['notice','force']),
('combat.durability/stamina','PC','M',['tough'],['resolve']),
('combat.reading','PC','M',['reason'],['notice']),
('combat.concentration/disrupt/poise','PC','M',['attend'],['resolve']),
('mb.derive_command','MB','M',['presence'],['reason']),
('tw.pool','TW','M',['resolve','thread'],[]),
('tw.leap_gate','TW','M',['thread'],[]),
('tw.collective_anchor','TW','M',['thread'],['reason']),
('knot.formation','TW','M',['warmth','resolve','thread'],[]),
# designed verbs (lexicons -09..-18), draws only
('assassinate','PC','D',['stealth','quick'],['force']),('capture','PC','D',['force','quick'],[]),
('ambush','PC','D',['stealth','notice'],[]),('shoot','PC','D',['hand'],['attend']),('guard','PC','D',['notice','tough'],[]),
('rescue','PC','D',['quick','force'],[]),('flee','PC','D',['quick','tough'],[]),('duel','PC','D',['force','quick'],['resolve']),
('rally','MB','D',['presence'],['resolve']),('marshal','MB','D',['presence','reason'],[]),('pursue','MB','D',['presence'],['reason']),
('reconnoitre','MB','D',['notice'],['stealth']),('withstand','MB','D',['presence'],['resolve']),('besiege','MB','D',['reason'],['tough']),
('drill','MB','D',['presence'],[]),('forage','WT','D',['notice','tough'],[]),
('persuade','SC','D',['presence'],['readp']),('threaten','SC','D',['presence'],['force']),('lie','SC','D',['readp'],['resolve']),
('interrogate','SC','D',['readp'],['presence']),('negotiate','SC','D',['readp','reason'],[]),('plead','SC','D',['warmth'],['presence']),
('flatter','SC','D',['warmth','readp'],[]),('preach','SC','D',['presence'],['thread']),('confront','SC','D',['presence'],['resolve']),
('counsel','SC','D',['reason'],['warmth']),('confide','SC','D',['warmth'],[]),('refute','SC','D',['reason'],[]),('mediate','SC','D',['readp','warmth'],[]),
('search','FI','D',['notice'],['attend']),('track','FI','D',['notice'],['tough']),('decipher','FI','D',['reason'],['lore']),
('shadow','FI','D',['stealth','notice'],[]),('eavesdrop','FI','D',['stealth','notice'],[]),('interview','FI','D',['readp'],[]),
('reconstruct','FI','D',['reason'],['lore']),('audit','FI','D',['reason'],['attend']),('scout','FI','D',['notice'],['stealth']),
('conceal','FI','D',['stealth'],['hand']),('disguise','FI','D',['stealth'],['readp']),('infiltrate','FI','D',['stealth'],['resolve']),
('forge','FI','D',['hand'],['lore']),('bribe','FI','D',['readp'],[]),('blackmail','FI','D',['readp'],['resolve']),('suborn','FA','D',['readp'],['warmth']),
('weave','TW','D',['resolve','thread'],['attend']),('pull','TW','D',['resolve','thread'],[]),('lock','TW','D',['resolve','thread'],[]),
('dissolve','TW','D',['resolve','thread'],[]),('mend','TW','D',['resolve','thread'],['attend']),('ward','TW','D',['resolve','thread'],[]),
('heal','NP','D',['hand'],['lore']),('thread_read','TW','D',['thread'],['attend']),
('assess','GV','D',['reason'],[]),('tax','GV','D',['reason'],['presence']),('ration','GV','D',['reason'],[]),('patrol','GV','D',['notice'],[]),
('depose','GV','D',['presence'],['readp']),('detain','GV','D',['presence'],['force']),
('craft','EC','D',['hand'],['lore']),('mint','EC','D',['hand'],[]),('cultivate','EC','D',['tough'],['lore']),('mine','EC','D',['force','tough'],[]),
('haul','EC','D',['force','tough'],[]),('smuggle','EC','D',['stealth'],['readp']),('bargain','EC','D',['readp'],['reason']),('appraise','EC','D',['reason'],['lore']),
('build','EC','D',['force'],['hand']),
('navigate','WT','D',['notice'],['lore']),('climb','WT','D',['quick','force'],[]),('swim','WT','D',['tough'],[]),('hunt','WT','D',['notice'],['stealth']),
('ride','WT','D',['quick'],[]),('travel','WT','D',['tough'],[]),('explore','WT','D',['notice'],['tough']),
('court','NP','D',['warmth'],['presence']),('reconcile','NP','D',['warmth'],[]),('teach','NP','D',['reason'],['warmth']),('study','NP','D',['reason'],['attend']),
('avenge','NP','D',['resolve'],[]),('hire','NP','D',['readp'],['warmth']),
('conspire','FA','D',['readp'],['stealth']),('coup','FA','D',['presence'],['stealth']),
]
def tally(rows, which='prim'):
    c=collections.defaultdict(lambda: {'n':0,'subs':set(),'B':0,'M':0,'D':0})
    for v,s,st,p,sec in rows:
        for cap in (p if which=='prim' else p+sec):
            a=CAP[cap] or 'GAP:'+cap
            c[a]['n']+=1; c[a]['subs'].add(s); c[a][st]+=1
    return c
print('moments',len(M), collections.Counter(r[2] for r in M), 'subsystems', sorted({r[1] for r in M}))
for which in ('prim','all'):
    print('\n== by attribute,',which)
    c=tally(M,which)
    for a,d in sorted(c.items(), key=lambda x:-x[1]['n']):
        print(f"{a:12} n={d['n']:3} B={d['B']} M={d['M']} D={d['D']} subs={len(d['subs'])} {sorted(d['subs'])}")
# co-demand Jaccard over moments (primary+secondary), attribute level
sets=collections.defaultdict(set)
for v,s,st,p,sec in M:
    for cap in p+sec: sets[CAP[cap] or 'GAP:'+cap].add(v)
print('\n== Jaccard >= .3')
for a,b in itertools.combinations(sorted(sets),2):
    j=len(sets[a]&sets[b])/len(sets[a]|sets[b])
    if j>=.3: print(a,b,round(j,2), len(sets[a]&sets[b]))
print('\n== top pairs')
pairs=sorted(((len(sets[a]&sets[b])/len(sets[a]|sets[b]),a,b) for a,b in itertools.combinations(sorted(sets),2)),reverse=True)[:8]
for j,a,b in pairs: print(a,b,round(j,2))
# dominance among contested (B + D) primaries: share of moments whose primary includes attr
contested=[r for r in M if r[2] in 'BD']
cc=collections.Counter(CAP[c] or 'GAP:'+c for r in contested for c in set(r[3]))
print('\n== primary share of',len(contested),'contested draws'); 
for a,n in cc.most_common(): print(a, n, f"{n/len(contested):.0%}")
# ATT split
for k in ('notice','readp'): print(k, sum(k in r[3] for r in M), sorted({r[1] for r in M if k in r[3]}))
for k in ('quick','hand'): print(k, sum(k in r[3] for r in M), sorted({r[1] for r in M if k in r[3]}))
~~~

### alt.py (06:41:09Z)

~~~
import collections, importlib.util, sys, io, contextlib
src=open('matrix.py').read().split("def tally")[0]
ns={}; exec(src,ns); M=ns['M']
SETS={
 'nine':{'force':'STR','tough':'END','quick':'AGI','hand':'AGI','reason':'ACU','notice':'ATT','readp':'ATT','presence':'CHA','warmth':'BON','resolve':'WIL','attend':'FOC','thread':'TS','stealth':'AGI*','lore':'ACU*'},
 'rec8':{'force':'STR','tough':'END','quick':'AGI','hand':'AGI','reason':'ACU','notice':'PER','readp':'INS','presence':'CHA','warmth':'CHA','resolve':'WIL','attend':'WIL','thread':'TS','stealth':'AGI*','lore':'ACU*'},
 'six505':{'force':'Body','tough':'Body','quick':'Hand','hand':'Hand','reason':'Wit','notice':'Sense','readp':'Sense','presence':'Presence','warmth':'Presence','resolve':'Nerve','attend':'Wit','thread':'TS','stealth':'Hand*','lore':'Wit*'},
}
contested=[r for r in M if r[2] in 'BD']
for name,cap in SETS.items():
    c=collections.Counter(); subs=collections.defaultdict(set); allc=collections.Counter()
    for v,s,st,p,sec in M:
        for a in {cap[x].rstrip('*') for x in p}: allc[a]+=1; subs[a].add(s)
    for v,s,st,p,sec in contested:
        for a in {cap[x].rstrip('*') for x in p}: c[a]+=1
    print(name, 'attrs',len(allc), ' '.join(f"{a}:{allc[a]}/{len(subs[a])}s" for a,_ in allc.most_common()), '| max contested share', max(c.values())/len(contested).__round__(3) if False else f"{max(c, key=c.get)} {max(c.values())/len(contested):.0%}", '| min', min(allc.values()))
~~~

### the session's `cat` of both scripts plus the printed tables (06:45:53Z)

~~~
# Demand matrix: moment -> (subsystem, status, primary capacities, secondary capacities). [REASONED mapping]
# status: B = built season contest/graded; M = module code reads it (T2, off season path); D = designed (lexicon) draw
import itertools, collections
CAP = {'force':'STR','tough':'END','quick':'AGI','hand':'AGI','reason':'ACU','notice':'ATT','readp':'ATT',
       'presence':'CHA','warmth':'BON','resolve':'WIL','attend':'FOC','thread':'TS',
       'stealth':None,'lore':None}
M = [
# built season moments
('fight','PC','B',['force','quick','tough'],['readp','resolve','attend']),
('accept','PC','B',['force','quick','tough'],['resolve']),
('march','MB','B',['presence','reason'],[]),
('tell','SC','B',['presence'],['readp']),
('speak','SC','B',['presence','reason'],[]),
('argue','SC','B',['reason'],['presence']),
('determine','SC','B',['reason'],['readp']),
('arrest','GV','B',['presence'],['force']),
('research','FI','B',['reason'],['attend','lore']),
('examine','FI','B',['notice','reason'],[]),
('surveil','FI','B',['notice'],['attend','stealth']),
# module moments (T2 code)
('combat.impact/handling','PC','M',['force'],[]),
('combat.tempo/reflex/balance','PC','M',['quick'],['notice','force']),
('combat.durability/stamina','PC','M',['tough'],['resolve']),
('combat.reading','PC','M',['reason'],['notice']),
('combat.concentration/disrupt/poise','PC','M',['attend'],['resolve']),
('mb.derive_command','MB','M',['presence'],['reason']),
('tw.pool','TW','M',['resolve','thread'],[]),
('tw.leap_gate','TW','M',['thread'],[]),
('tw.collective_anchor','TW','M',['thread'],['reason']),
('knot.formation','TW','M',['warmth','resolve','thread'],[]),
# designed verbs (lexicons -09..-18), draws only
('assassinate','PC','D',['stealth','quick'],['force']),('capture','PC','D',['force','quick'],[]),
('ambush','PC','D',['stealth','notice'],[]),('shoot','PC','D',['hand'],['attend']),('guard','PC','D',['notice','tough'],[]),
('rescue','PC','D',['quick','force'],[]),('flee','PC','D',['quick','tough'],[]),('duel','PC','D',['force','quick'],['resolve']),
('rally','MB','D',['presence'],['resolve']),('marshal','MB','D',['presence','reason'],[]),('pursue','MB','D',['presence'],['reason']),
('reconnoitre','MB','D',['notice'],['stealth']),('withstand','MB','D',['presence'],['resolve']),('besiege','MB','D',['reason'],['tough']),
('drill','MB','D',['presence'],[]),('forage','WT','D',['notice','tough'],[]),
('persuade','SC','D',['presence'],['readp']),('threaten','SC','D',['presence'],['force']),('lie','SC','D',['readp'],['resolve']),
('interrogate','SC','D',['readp'],['presence']),('negotiate','SC','D',['readp','reason'],[]),('plead','SC','D',['warmth'],['presence']),
('flatter','SC','D',['warmth','readp'],[]),('preach','SC','D',['presence'],['thread']),('confront','SC','D',['presence'],['resolve']),
('counsel','SC','D',['reason'],['warmth']),('confide','SC','D',['warmth'],[]),('refute','SC','D',['reason'],[]),('mediate','SC','D',['readp','warmth'],[]),
('search','FI','D',['notice'],['attend']),('track','FI','D',['notice'],['tough']),('decipher','FI','D',['reason'],['lore']),
('shadow','FI','D',['stealth','notice'],[]),('eavesdrop','FI','D',['stealth','notice'],[]),('interview','FI','D',['readp'],[]),
('reconstruct','FI','D',['reason'],['lore']),('audit','FI','D',['reason'],['attend']),('scout','FI','D',['notice'],['stealth']),
('conceal','FI','D',['stealth'],['hand']),('disguise','FI','D',['stealth'],['readp']),('infiltrate','FI','D',['stealth'],['resolve']),
('forge','FI','D',['hand'],['lore']),('bribe','FI','D',['readp'],[]),('blackmail','FI','D',['readp'],['resolve']),('suborn','FA','D',['readp'],['warmth']),
('weave','TW','D',['resolve','thread'],['attend']),('pull','TW','D',['resolve','thread'],[]),('lock','TW','D',['resolve','thread'],[]),
('dissolve','TW','D',['resolve','thread'],[]),('mend','TW','D',['resolve','thread'],['attend']),('ward','TW','D',['resolve','thread'],[]),
('heal','NP','D',['hand'],['lore']),('thread_read','TW','D',['thread'],['attend']),
('assess','GV','D',['reason'],[]),('tax','GV','D',['reason'],['presence']),('ration','GV','D',['reason'],[]),('patrol','GV','D',['notice'],[]),
('depose','GV','D',['presence'],['readp']),('detain','GV','D',['presence'],['force']),
('craft','EC','D',['hand'],['lore']),('mint','EC','D',['hand'],[]),('cultivate','EC','D',['tough'],['lore']),('mine','EC','D',['force','tough'],[]),
('haul','EC','D',['force','tough'],[]),('smuggle','EC','D',['stealth'],['readp']),('bargain','EC','D',['readp'],['reason']),('appraise','EC','D',['reason'],['lore']),
('build','EC','D',['force'],['hand']),
('navigate','WT','D',['notice'],['lore']),('climb','WT','D',['quick','force'],[]),('swim','WT','D',['tough'],[]),('hunt','WT','D',['notice'],['stealth']),
('ride','WT','D',['quick'],[]),('travel','WT','D',['tough'],[]),('explore','WT','D',['notice'],['tough']),
('court','NP','D',['warmth'],['presence']),('reconcile','NP','D',['warmth'],[]),('teach','NP','D',['reason'],['warmth']),('study','NP','D',['reason'],['attend']),
('avenge','NP','D',['resolve'],[]),('hire','NP','D',['readp'],['warmth']),
('conspire','FA','D',['readp'],['stealth']),('coup','FA','D',['presence'],['stealth']),
]
def tally(rows, which='prim'):
    c=collections.defaultdict(lambda: {'n':0,'subs':set(),'B':0,'M':0,'D':0})
    for v,s,st,p,sec in rows:
        for cap in (p if which=='prim' else p+sec):
            a=CAP[cap] or 'GAP:'+cap
            c[a]['n']+=1; c[a]['subs'].add(s); c[a][st]+=1
    return c
print('moments',len(M), collections.Counter(r[2] for r in M), 'subsystems', sorted({r[1] for r in M}))
for which in ('prim','all'):
    print('\n== by attribute,',which)
    c=tally(M,which)
    for a,d in sorted(c.items(), key=lambda x:-x[1]['n']):
        print(f"{a:12} n={d['n']:3} B={d['B']} M={d['M']} D={d['D']} subs={len(d['subs'])} {sorted(d['subs'])}")
# co-demand Jaccard over moments (primary+secondary), attribute level
sets=collections.defaultdict(set)
for v,s,st,p,sec in M:
    for cap in p+sec: sets[CAP[cap] or 'GAP:'+cap].add(v)
print('\n== Jaccard >= .3')
for a,b in itertools.combinations(sorted(sets),2):
    j=len(sets[a]&sets[b])/len(sets[a]|sets[b])
    if j>=.3: print(a,b,round(j,2), len(sets[a]&sets[b]))
print('\n== top pairs')
pairs=sorted(((len(sets[a]&sets[b])/len(sets[a]|sets[b]),a,b) for a,b in itertools.combinations(sorted(sets),2)),reverse=True)[:8]
for j,a,b in pairs: print(a,b,round(j,2))
# dominance among contested (B + D) primaries: share of moments whose primary includes attr
contested=[r for r in M if r[2] in 'BD']
cc=collections.Counter(CAP[c] or 'GAP:'+c for r in contested for c in set(r[3]))
print('\n== primary share of',len(contested),'contested draws'); 
for a,n in cc.most_common(): print(a, n, f"{n/len(contested):.0%}")
# ATT split
for k in ('notice','readp'): print(k, sum(k in r[3] for r in M), sorted({r[1] for r in M if k in r[3]}))
for k in ('quick','hand'): print(k, sum(k in r[3] for r in M), sorted({r[1] for r in M if k in r[3]}))
import collections, importlib.util, sys, io, contextlib
src=open('matrix.py').read().split("def tally")[0]
ns={}; exec(src,ns); M=ns['M']
SETS={
 'nine':{'force':'STR','tough':'END','quick':'AGI','hand':'AGI','reason':'ACU','notice':'ATT','readp':'ATT','presence':'CHA','warmth':'BON','resolve':'WIL','attend':'FOC','thread':'TS','stealth':'AGI*','lore':'ACU*'},
 'rec8':{'force':'STR','tough':'END','quick':'AGI','hand':'AGI','reason':'ACU','notice':'PER','readp':'INS','presence':'CHA','warmth':'CHA','resolve':'WIL','attend':'WIL','thread':'TS','stealth':'AGI*','lore':'ACU*'},
 'six505':{'force':'Body','tough':'Body','quick':'Hand','hand':'Hand','reason':'Wit','notice':'Sense','readp':'Sense','presence':'Presence','warmth':'Presence','resolve':'Nerve','attend':'Wit','thread':'TS','stealth':'Hand*','lore':'Wit*'},
}
contested=[r for r in M if r[2] in 'BD']
for name,cap in SETS.items():
    c=collections.Counter(); subs=collections.defaultdict(set); allc=collections.Counter()
    for v,s,st,p,sec in M:
        for a in {cap[x].rstrip('*') for x in p}: allc[a]+=1; subs[a].add(s)
    for v,s,st,p,sec in contested:
        for a in {cap[x].rstrip('*') for x in p}: c[a]+=1
    print(name, 'attrs',len(allc), ' '.join(f"{a}:{allc[a]}/{len(subs[a])}s" for a,_ in allc.most_common()), '| max contested share', max(c.values())/len(contested).__round__(3) if False else f"{max(c, key=c.get)} {max(c.values())/len(contested):.0%}", '| min', min(allc.values()))
moments 104 Counter({'D': 83, 'B': 11, 'M': 10}) subsystems ['EC', 'FA', 'FI', 'GV', 'MB', 'NP', 'PC', 'SC', 'TW', 'WT']

== by attribute, prim
ATT          n= 27 B=2 M=0 D=25 subs=9 ['EC', 'FA', 'FI', 'GV', 'MB', 'NP', 'PC', 'SC', 'WT']
ACU          n= 21 B=6 M=1 D=14 subs=7 ['EC', 'FI', 'GV', 'MB', 'NP', 'PC', 'SC']
CHA          n= 17 B=4 M=1 D=12 subs=4 ['FA', 'GV', 'MB', 'SC']
AGI          n= 15 B=2 M=1 D=12 subs=5 ['EC', 'FI', 'NP', 'PC', 'WT']
END          n= 11 B=2 M=1 D=8 subs=3 ['EC', 'PC', 'WT']
TS           n= 11 B=0 M=4 D=7 subs=1 ['TW']
STR          n= 10 B=2 M=1 D=7 subs=3 ['EC', 'PC', 'WT']
WIL          n=  9 B=0 M=2 D=7 subs=2 ['NP', 'TW']
GAP:stealth  n=  8 B=0 M=0 D=8 subs=3 ['EC', 'FI', 'PC']
BON          n=  7 B=0 M=1 D=6 subs=3 ['NP', 'SC', 'TW']
FOC          n=  1 B=0 M=1 D=0 subs=1 ['PC']

== by attribute, all
ATT          n= 36 B=5 M=2 D=29 subs=9 ['EC', 'FA', 'FI', 'GV', 'MB', 'NP', 'PC', 'SC', 'WT']
ACU          n= 25 B=6 M=3 D=16 subs=8 ['EC', 'FI', 'GV', 'MB', 'NP', 'PC', 'SC', 'TW']
CHA          n= 22 B=5 M=1 D=16 subs=5 ['FA', 'GV', 'MB', 'NP', 'SC']
WIL          n= 20 B=2 M=4 D=14 subs=6 ['FI', 'MB', 'NP', 'PC', 'SC', 'TW']
AGI          n= 17 B=2 M=1 D=14 subs=5 ['EC', 'FI', 'NP', 'PC', 'WT']
STR          n= 15 B=3 M=2 D=10 subs=5 ['EC', 'GV', 'PC', 'SC', 'WT']
END          n= 14 B=2 M=1 D=11 subs=5 ['EC', 'FI', 'MB', 'PC', 'WT']
GAP:stealth  n= 14 B=1 M=0 D=13 subs=6 ['EC', 'FA', 'FI', 'MB', 'PC', 'WT']
TS           n= 12 B=0 M=4 D=8 subs=2 ['SC', 'TW']
FOC          n= 11 B=3 M=1 D=7 subs=4 ['FI', 'NP', 'PC', 'TW']
BON          n= 11 B=0 M=1 D=10 subs=4 ['FA', 'NP', 'SC', 'TW']
GAP:lore     n=  9 B=1 M=0 D=8 subs=4 ['EC', 'FI', 'NP', 'WT']

== Jaccard >= .3
AGI STR 0.39 9
TS WIL 0.33 8

== top pairs
AGI STR 0.39
TS WIL 0.33
ATT GAP:stealth 0.25
ACU CHA 0.17
END STR 0.16
FOC TS 0.15
FOC WIL 0.15
ACU GAP:lore 0.13

== primary share of 94 contested draws
ATT 27 29%
ACU 20 21%
CHA 16 17%
AGI 14 15%
END 10 11%
STR 9 10%
GAP:stealth 8 9%
TS 7 7%
WIL 7 7%
BON 6 6%
notice 15 ['FI', 'GV', 'MB', 'PC', 'WT']
readp 12 ['EC', 'FA', 'FI', 'NP', 'SC']
quick 10 ['PC', 'WT']
hand 5 ['EC', 'FI', 'NP', 'PC']
~~~

### alt.py output (06:47:45Z)

~~~
nine attrs 10 ATT:27/9s AGI:22/5s ACU:21/7s CHA:17/4s END:11/3s TS:11/1s STR:10/3s WIL:9/2s BON:7/3s FOC:1/1s | max contested share ATT 29% | min 1
rec8 attrs 9 CHA:24/6s AGI:22/5s ACU:21/7s PER:15/5s INS:12/5s END:11/3s TS:11/1s STR:10/3s WIL:10/3s | max contested share CHA 23% | min 10
six505 attrs 7 Sense:27/9s Presence:24/6s Hand:22/5s Wit:22/7s Body:17/3s TS:11/1s Nerve:9/2s | max contested share Sense 29% | min 9
## all 104 104
  nine(reg)                                n=10 max=ATT 29% min=1 | ATT:27/9 AGI:22/5 ACU:21/7 CHA:17/4 END:11/3 TS:11/1 STR:10/3 WIL:9/2 BON:7/3 FOC:1/1
  A6 eight                                 n=9 max=CHA 23% min=10 | CHA:24/6 AGI:22/5 ACU:21/7 PER:15/5 INS:12/5 END:11/3 TS:11/1 STR:10/3 WIL:10/3
  nine+TS=10 (keep BON)                    n=10 max=AGI 22% min=7 | AGI:22/5 ACU:21/7 CHA:17/4 PER:15/5 INS:12/5 END:11/3 TS:11/1 STR:10/3 WIL:10/3 BON:7/3
  505 six                                  n=7 max=Sense 29% min=9 | Sense:27/9 Pres:24/6 Hand:22/5 Wit:22/7 Body:17/3 TS:11/1 Nerve:9/2
  505 six, Nerve->Will-like split STR/END  n=8 max=Sense 29% min=10 | Sense:27/9 Pres:24/6 Hand:22/5 Wit:21/7 END:11/3 TS:11/1 STR:10/3 WIL:10/3
## built+module only (21) 21
  nine(reg)                                n=10 max=ACU 55% min=1 | ACU:7/4 CHA:5/3 TS:4/1 STR:3/1 END:3/1 AGI:3/1 ATT:2/1 WIL:2/1 FOC:1/1 BON:1/1
  A6 eight                                 n=8 max=ACU 55% min=2 | ACU:7/4 CHA:6/4 TS:4/1 STR:3/1 END:3/1 AGI:3/1 WIL:3/2 PER:2/1
  nine+TS=10 (keep BON)                    n=9 max=ACU 55% min=1 | ACU:7/4 CHA:5/3 TS:4/1 STR:3/1 END:3/1 AGI:3/1 WIL:3/2 PER:2/1 BON:1/1
  505 six                                  n=7 max=Wit 55% min=2 | Wit:8/4 Pres:6/4 Body:4/1 TS:4/1 Hand:3/1 Sense:2/1 Nerve:2/1
  505 six, Nerve->Will-like split STR/END  n=8 max=Wit 55% min=2 | Wit:7/4 Pres:6/4 TS:4/1 STR:3/1 Hand:3/1 END:3/1 WIL:3/2 Sense:2/1
## built season only (11) 11
  nine(reg)                                n=6 max=ACU 55% min=2 | ACU:6/3 CHA:4/3 STR:2/1 END:2/1 AGI:2/1 ATT:2/1
  A6 eight                                 n=6 max=ACU 55% min=2 | ACU:6/3 CHA:4/3 STR:2/1 END:2/1 AGI:2/1 PER:2/1
  nine+TS=10 (keep BON)                    n=6 max=ACU 55% min=2 | ACU:6/3 CHA:4/3 STR:2/1 END:2/1 AGI:2/1 PER:2/1
  505 six                                  n=5 max=Wit 55% min=2 | Wit:6/3 Pres:4/3 Body:2/1 Hand:2/1 Sense:2/1
  505 six, Nerve->Will-like split STR/END  n=6 max=Wit 55% min=2 | Wit:6/3 Pres:4/3 STR:2/1 Hand:2/1 END:2/1 Sense:2/1
~~~

### the P2 probe script (06:47:44Z)

~~~
import collections, sys
src=open(sys.argv[1]).read().split("def tally")[0]
ns={}; exec(src,ns); M=ns['M']
base={'force':'STR','tough':'END','quick':'AGI','hand':'AGI','reason':'ACU','presence':'CHA','resolve':'WIL','thread':'TS','stealth':'AGI','lore':'ACU'}
SETS={
 'nine(reg)':dict(base,notice='ATT',readp='ATT',warmth='BON',attend='FOC'),
 'A6 eight':dict(base,notice='PER',readp='INS',warmth='CHA',attend='WIL'),
 'nine+TS=10 (keep BON)':dict(base,notice='PER',readp='INS',warmth='BON',attend='WIL'),
 '505 six':dict(base,force='Body',tough='Body',quick='Hand',hand='Hand',reason='Wit',notice='Sense',readp='Sense',presence='Pres',warmth='Pres',resolve='Nerve',attend='Wit',stealth='Hand',lore='Wit'),
 '505 six, Nerve->Will-like split STR/END':dict(base,force='STR',tough='END',quick='Hand',hand='Hand',reason='Wit',notice='Sense',readp='Sense',presence='Pres',warmth='Pres',resolve='WIL',attend='WIL',stealth='Hand',lore='Wit'),
}
def run(rows,label):
  print('##',label,len(rows))
  contested=[r for r in rows if r[2] in 'BD']
  for name,cap in SETS.items():
    prim=collections.Counter(); subs=collections.defaultdict(set); cc=collections.Counter()
    for v,s,st,p,sec in rows:
        for a in {cap[x] for x in p}: prim[a]+=1; subs[a].add(s)
    for v,s,st,p,sec in contested:
        for a in {cap[x] for x in p}: cc[a]+=1
    top=max(cc,key=cc.get) if cc else '-'
    print(f"  {name:40} n={len(prim)} max={top} {cc[top]/max(1,len(contested)):.0%} min={min(prim.values())} | "+' '.join(f"{a}:{prim[a]}/{len(subs[a])}" for a,_ in prim.most_common()))
run(M,'all 104')
run([r for r in M if r[2] in 'BM'],'built+module only (21)')
run([r for r in M if r[2]=='B'],'built season only (11)')
~~~

### the P2 probe output (06:59:10Z)

~~~
## all 104 104
  nine(reg)                                n=10 max=ATT 29% min=1 | ATT:27/9 AGI:22/5 ACU:21/7 CHA:17/4 END:11/3 TS:11/1 STR:10/3 WIL:9/2 BON:7/3 FOC:1/1
  A6 eight                                 n=9 max=CHA 23% min=10 | CHA:24/6 AGI:22/5 ACU:21/7 PER:15/5 INS:12/5 END:11/3 TS:11/1 STR:10/3 WIL:10/3
  nine+TS=10 (keep BON)                    n=10 max=AGI 22% min=7 | AGI:22/5 ACU:21/7 CHA:17/4 PER:15/5 INS:12/5 END:11/3 TS:11/1 STR:10/3 WIL:10/3 BON:7/3
  505 six                                  n=7 max=Sense 29% min=9 | Sense:27/9 Pres:24/6 Hand:22/5 Wit:22/7 Body:17/3 TS:11/1 Nerve:9/2
  505 six, Nerve->Will-like split STR/END  n=8 max=Sense 29% min=10 | Sense:27/9 Pres:24/6 Hand:22/5 Wit:21/7 END:11/3 TS:11/1 STR:10/3 WIL:10/3
## built+module only (21) 21
  nine(reg)                                n=10 max=ACU 55% min=1 | ACU:7/4 CHA:5/3 TS:4/1 STR:3/1 END:3/1 AGI:3/1 ATT:2/1 WIL:2/1 FOC:1/1 BON:1/1
  A6 eight                                 n=8 max=ACU 55% min=2 | ACU:7/4 CHA:6/4 TS:4/1 STR:3/1 END:3/1 AGI:3/1 WIL:3/2 PER:2/1
  nine+TS=10 (keep BON)                    n=9 max=ACU 55% min=1 | ACU:7/4 CHA:5/3 TS:4/1 STR:3/1 END:3/1 AGI:3/1 WIL:3/2 PER:2/1 BON:1/1
  505 six                                  n=7 max=Wit 55% min=2 | Wit:8/4 Pres:6/4 Body:4/1 TS:4/1 Hand:3/1 Sense:2/1 Nerve:2/1
  505 six, Nerve->Will-like split STR/END  n=8 max=Wit 55% min=2 | Wit:7/4 Pres:6/4 TS:4/1 Hand:3/1 STR:3/1 END:3/1 WIL:3/2 Sense:2/1
## built season only (11) 11
  nine(reg)                                n=6 max=ACU 55% min=2 | ACU:6/3 CHA:4/3 STR:2/1 END:2/1 AGI:2/1 ATT:2/1
  A6 eight                                 n=6 max=ACU 55% min=2 | ACU:6/3 CHA:4/3 STR:2/1 END:2/1 AGI:2/1 PER:2/1
  nine+TS=10 (keep BON)                    n=6 max=ACU 55% min=2 | ACU:6/3 CHA:4/3 STR:2/1 END:2/1 AGI:2/1 PER:2/1
  505 six                                  n=5 max=Wit 55% min=2 | Wit:6/3 Pres:4/3 Hand:2/1 Body:2/1 Sense:2/1
  505 six, Nerve->Will-like split STR/END  n=6 max=Wit 55% min=2 | Wit:6/3 Pres:4/3 Hand:2/1 STR:2/1 END:2/1 Sense:2/1
~~~
