import collections
from engine.season.harness import storybar as SB
from engine.season.loop.driver import SeasonDriver
rec=collections.Counter(); byverb=collections.defaultdict(collections.Counter)
oe=SeasonDriver._eligible
def e(self,w,a,row):
    r=oe(self,w,a,row); rec[bool(r)]+=1; byverb[a.verb][bool(r)]+=1; return r
SeasonDriver._eligible=e
oa=SeasonDriver._admits
adm=collections.Counter()
def ad(self,w,a,row):
    r=oa(self,w,a,row)
    ok,kinds,v=r
    if not ok: adm[(a.verb, 'act.ineligible' in kinds, repr(v.value), len(v.observed or ()))]+=1
    return r
SeasonDriver._admits=ad
w,d,b=SB.drive(0,1,"off")
print("eligible calls",dict(rec))
print({v:dict(c) for v,c in byverb.items() if c[False]})
print([(k,n) for k,n in adm.most_common(40) if k[2]=="UNKNOWN"])
