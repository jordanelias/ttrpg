"""Interaction matrix: how each lever interacts with others (ED-PC-0025). For a pair (X,Y) measure winΔ(X),
winΔ(Y), winΔ(X+Y) vs an all-off baseline; classify INDEPENDENT (X+Y≈X+Y), MASKING (X+Y≈dominant, the weaker is
swallowed), SYNERGY (super-additive — degeneracy risk), ANTAGONISM (sub-either). Grouped by state-graph node."""
import os,sys,random
E=os.path.join(os.path.dirname(__file__),'..','..','systems','combat','combat_engine_v1')
sys.path.insert(0,E); sys.path.insert(0,os.path.join(E,'workbench'))
import combatant as C, wrapper as W
from config import CFG
def mk(s):
    kw={k:s[k] for k in ('strength','agi','end','cog','att','spirit','focus','history','disp') if k in s}
    return C.Combatant('x',weapon=s.get('weapon','arming'),armor=s.get('armor','light'),tradition=s.get('tradition','none'),skills=s.get('skills'),equipped=s.get('equipped'),**kw)
def ws(A,B,cfg=CFG,n=500,seed0=1):
    aw=dec=0
    for i in range(n):
        rng=random.Random(seed0+i);sw=i>=n//2
        r=W.fight(mk(B if sw else A),mk(A if sw else B),cfg,rng)
        if sw:r=-r
        if r==1:aw+=1;dec+=1
        elif r==-1:dec+=1
    return aw/dec if dec else .5
def merge(*ds):
    out={}
    for d in ds:
        for k,v in d.items():
            if k=='skills': out['skills']={**out.get('skills',{}),**v}
            elif k=='equipped': out['equipped']=(out.get('equipped',[]) or [])+list(v)
            else: out[k]=v
    return out
def cls(dx,dy,dxy):
    exp=dx+dy
    if abs(dxy-exp)<=0.02: return 'INDEPENDENT'
    if dxy>exp+0.02: return 'SYNERGY(super-additive)'
    dom=max(dx,dy,key=abs)
    if abs(dxy-dom)<=0.02 and abs(dxy)<abs(exp)-0.02: return 'MASKING(weaker swallowed)'
    if abs(dxy)<min(abs(dx),abs(dy))-0.02: return 'ANTAGONISM'
    return 'PARTIAL/sub-additive'

# node -> [(name, base_delta_spec, cfg?)] : a factor is applied to fighter A vs a plain opponent
KATANA=dict(weapon='katana'); ARM=dict(weapon='arming')
NODES={
 'Bind (vs arming)': (dict(weapon='katana'), dict(weapon='arming'), [
    ('spine_lever', {}, dict(CFG)),                 # lever is a cfg thing: compare CFG vs BIND_SPINE_K=0 -> handled specially below
    ('shinogi_L1', dict(tradition='japanese',equipped=['shinogi']), CFG),
    ('shinogi_L3', dict(tradition='japanese',equipped={'shinogi':3}), CFG),
    ('skill_bind2', dict(skills=dict(bind=2)), CFG),
    ('staerke(lev)', dict(tradition='german',equipped=['staerke_schwaeche']), CFG),
 ]),
 'Contact (dagger vs arming)': (dict(weapon='dagger'), dict(weapon='arming'), [
    ('ringen', dict(tradition='german',equipped=['ringen_am_schwert']), CFG),
    ('skill_grab2', dict(skills=dict(grab=2)), CFG),
    ('strength', dict(strength=6), CFG),
 ]),
 'Exchange (arming vs arming)': (dict(weapon='arming'), dict(weapon='arming'), [
    ('skill_bind2', dict(skills=dict(bind=2)), CFG),
    ('skill_parry2', dict(skills=dict(parry=2)), CFG),
    ('agi6', dict(agi=6), CFG),
    ('strength6', dict(strength=6), CFG),
    ('disp_agg', dict(disp=6), CFG),
 ]),
}
def delta(base,factor,opp,cfg):
    return ws(merge(base,factor),opp,cfg)-ws(base,opp,CFG)

for node,(base,opp,facs) in NODES.items():
    print(f"\n=== {node} — pairwise interaction ===")
    names=[f[0] for f in facs]
    # single deltas
    d={}
    for nm,spec,cfg in facs:
        d[nm]=delta(base,spec,opp,cfg)
    print("  singles: "+", ".join(f"{n}:{100*d[n]:+.1f}" for n in names))
    print(f"  {'pair':30}{'dX':>6}{'dY':>6}{'dXY':>7}{'exp':>7}  class")
    for i in range(len(facs)):
        for j in range(i+1,len(facs)):
            (nx,sx,cx),(ny,sy,cy)=facs[i],facs[j]
            dxy=ws(merge(base,sx,sy),opp,CFG)-ws(base,opp,CFG)
            print(f"  {nx+' x '+ny:30}{100*d[nx]:+6.1f}{100*d[ny]:+6.1f}{100*dxy:+7.1f}{100*(d[nx]+d[ny]):+7.1f}  {cls(d[nx],d[ny],dxy)}")
