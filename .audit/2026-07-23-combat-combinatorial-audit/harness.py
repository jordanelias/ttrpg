"""Systematic isolation / combinatorial wiring audit of personal combat (ED-PC-0025).
Isolation: each FACTOR on-alone vs off -> FIRES? (event-divergence) + MOVES? (win-share delta) -> classify
WIRED-LIVE / WIRED-SITUATIONAL / DEAD. Combination: pairwise WITHIN each state-graph node (the factors that
actually interact) -> independent / masking / compounding. Grouping by state-graph node keeps it tractable."""
import os, sys, random
E=os.path.join(os.path.dirname(__file__),'..','..','systems','combat','combat_engine_v1')
sys.path.insert(0,E); sys.path.insert(0,os.path.join(E,'workbench'))
import combatant as C, wrapper as W
from config import CFG
from trace import run_traced_fight

def mk(spec):
    kw={k:spec[k] for k in ('strength','agi','end','cog','att','spirit','focus','history','disp') if k in spec}
    return C.Combatant(spec.get('label','x'), weapon=spec.get('weapon','arming'), armor=spec.get('armor','light'),
                       tradition=spec.get('tradition','none'), skills=spec.get('skills'), equipped=spec.get('equipped'), **kw)

def winshare(specA, specB, cfg=CFG, n=600, seed0=1):
    aw=dec=0
    for i in range(n):
        rng=random.Random(seed0+i); swap=i>=n//2
        X=mk(specB if swap else specA); Y=mk(specA if swap else specB)
        r=W.fight(X,Y,cfg,rng)
        if swap: r=-r
        if r==1: aw+=1;dec+=1
        elif r==-1: dec+=1
    return (aw/dec if dec else .5)

def sig(ev):
    o=[]
    for e in ev:
        k=e['kind']
        if k=='outcome': o.append(('H' if e['hit']>0 else '.')+('B' if e['bind'] else '')+('R' if e['riposte'] else ''))
        elif k=='contact': o.append('G:'+e['outcome'])
        elif k=='separation': o.append('s:'+e['reason'])
    return tuple(o)

def fires(base_spec, factor_spec, cfg_on=CFG, cfg_off=CFG, opp=None, n=60):
    """event-divergence: does turning the factor ON change how fights PLAY OUT at identical seeds?"""
    opp=opp or dict(base_spec); div=0
    for s in range(n):
        _,evon=run_traced_fight(mk(factor_spec), mk(opp), cfg=cfg_on, seed=s)
        _,evoff=run_traced_fight(mk(base_spec), mk(opp), cfg=cfg_off, seed=s)
        if sig(evon)!=sig(evoff): div+=1
    return div/n

# ---- FACTORS grouped by the STATE-GRAPH NODE they feed ----
# each: (name, node, base_spec, factor_spec, cfg_on, cfg_off, opp_spec)  — opp default = base
OFF=lambda **ov: dict(CFG,**ov)
ALLLEVERS_OFF=OFF(LEGIB_EDGELINE_K=0,BIND_SPINE_K=0,GRAB_EDGE_K=0,CHOKE_ACCURACY_K=0,FACING_REGIME_K=0)
B=lambda **kw: dict(dict(weapon='arming',armor='light'),**kw)  # base fighter builder

FACTORS=[
 # node, name, base, factor, cfg_on, cfg_off, opp
 ('Exchange.read','LEGIB_EDGELINE_K(edge_read lever)', B(weapon='arming'), B(weapon='arming'), CFG, OFF(LEGIB_EDGELINE_K=0), B(weapon='arming')),
 ('Exchange.read','zwerchhau ability', B(weapon='arming'), B(weapon='arming',tradition='german',equipped=['zwerchhau']), CFG, CFG, B(weapon='arming')),
 ('Exchange.read','skill(technique)', B(weapon='arming'), B(weapon='arming',skills=dict(technique=2)), CFG, CFG, B(weapon='arming')),
 ('Bind','BIND_SPINE_K(spine_press lever)', B(weapon='katana'), B(weapon='katana'), CFG, OFF(BIND_SPINE_K=0), B(weapon='arming')),
 ('Bind','shinogi ability(L1)', B(weapon='katana'), B(weapon='katana',tradition='japanese',equipped=['shinogi']), CFG, CFG, B(weapon='arming')),
 ('Bind','shinogi ability(L3)', B(weapon='katana'), B(weapon='katana',tradition='japanese',equipped={'shinogi':3}), CFG, CFG, B(weapon='arming')),
 ('Bind','skill(bind)', B(weapon='katana'), B(weapon='katana',skills=dict(bind=2)), CFG, CFG, B(weapon='arming')),
 ('Bind','staerke_schwaeche(leverage)', B(weapon='katana'), B(weapon='katana',tradition='german',equipped=['staerke_schwaeche']), CFG, CFG, B(weapon='arming')),
 ('Contact','GRAB_EDGE_K(edge_grab lever)', B(weapon='dagger'), B(weapon='dagger'), CFG, OFF(GRAB_EDGE_K=0), B(weapon='arming')),
 ('Contact','ringen ability', B(weapon='dagger'), B(weapon='dagger',tradition='german',equipped=['ringen_am_schwert']), CFG, CFG, B(weapon='arming')),
 ('Contact','skill(grab)', B(weapon='dagger'), B(weapon='dagger',skills=dict(grab=2)), CFG, CFG, B(weapon='arming')),
 ('Approach.facing','FACING_REGIME_K(facing lever)', B(weapon='sabre'), B(weapon='sabre'), CFG, OFF(FACING_REGIME_K=0), B(weapon='longsword')),
 ('Approach.facing','guardia ability', B(weapon='sabre'), B(weapon='sabre',tradition='italian',equipped=['guardia']), CFG, CFG, B(weapon='longsword')),
 ('Approach.facing','CHOKE_ACCURACY_K(choke lever)', B(weapon='poleaxe'), B(weapon='poleaxe'), CFG, OFF(CHOKE_ACCURACY_K=0), B(weapon='arming')),
 ('Riposte.counter','indes(counter_success)', B(weapon='arming'), B(weapon='arming',tradition='german',equipped=['indes']), CFG, CFG, B(weapon='arming')),
 ('Riposte.counter','mezzo_tempo(counter_select)', B(weapon='rapier'), B(weapon='rapier',tradition='italian',equipped=['mezzo_tempo']), CFG, CFG, B(weapon='arming')),
 ('Riposte.counter','true_times(anti_overcommit)', B(weapon='arming'), B(weapon='arming',tradition='english',equipped=['true_times']), CFG, CFG, B(weapon='arming')),
 ('Exchange.commit','disposition(disp aggressive)', B(weapon='arming',disp=4), B(weapon='arming',disp=6), CFG, CFG, B(weapon='arming',disp=4)),
 ('Exchange.mode','skill(parry)', B(weapon='arming'), B(weapon='arming',skills=dict(parry=2)), CFG, CFG, B(weapon='arming')),
 ('Exchange.mode','skill(dodge)', B(weapon='arming'), B(weapon='arming',skills=dict(dodge=2)), CFG, CFG, B(weapon='arming')),
 ('Damage','strength', B(weapon='arming',strength=4), B(weapon='arming',strength=6), CFG, CFG, B(weapon='arming',strength=4)),
 ('Tempo','agi', B(weapon='arming',agi=4), B(weapon='arming',agi=6), CFG, CFG, B(weapon='arming',agi=4)),
 # a KNOWN retired/vestigial one (control): the retired imposition — should now be DEAD
 ('(control)','tradition=german ALONE (no ability, post-imposition-retire)', B(weapon='arming'), B(weapon='arming',tradition='german'), CFG, CFG, B(weapon='arming')),
]

print(f"{'NODE':16}{'FACTOR':44}{'fires%':>7}{'winΔ':>8}  CLASS")
print('-'*90)
for node,name,base,fac,con,coff,opp in FACTORS:
    fr=fires(base,fac,con,coff,opp)
    w_on=winshare(fac,opp,con); w_off=winshare(base,opp,coff)
    dw=w_on-w_off
    if fr<0.03 and abs(dw)<0.02: cls='DEAD (never fires / no effect)'
    elif abs(dw)>=0.05: cls='WIRED-LIVE (moves outcome)'
    else: cls='WIRED-SITUATIONAL (fires, ~0 aggregate)'
    print(f"{node:16}{name:44}{100*fr:6.0f}%{100*dw:+7.1f}  {cls}")
