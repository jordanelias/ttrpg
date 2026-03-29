#!/usr/bin/env python3
"""
Valoria v11 — mass mismatch penalty
When Light weapon defender splits pool against Heavy weapon attack:
  -1 defensive success (minimum 0)
Full Guard: no penalty (voiding, not meeting force)
Long weapon at Close zone: no penalty (heavy weapon already compromised)
Testing variant B (wound reset, HP=End, armour=DR) as primary
"""
import math, numpy as np
from collections import defaultdict

WEAPONS = {
    'Short-LightCut':   ('Short','LightCut',  5,6,1,2,1),
    'Short-HeavyCut':   ('Short','HeavyCut',  6,7,4,5,3),
    'Short-LightBlunt': ('Short','LightBlunt',6,7,1,2,1),
    'Short-HeavyBlunt': ('Short','HeavyBlunt',7,8,4,5,4),
    'Long-LightCut':    ('Long', 'LightCut',  5,6,1,2,1),
    'Long-HeavyCut':    ('Long', 'HeavyCut',  6,7,4,5,3),
    'Long-LightBlunt':  ('Long', 'LightBlunt',6,7,1,2,1),
    'Long-HeavyBlunt':  ('Long', 'HeavyBlunt',7,8,4,5,4),
    'Unarmed':          ('Short','LightBlunt', 8,9,0,0,1),
}
ARMOUR_DR = {
    'None':  (0,0,0,0),
    'Light': (2,1,1,0),
    'Medium':(4,3,2,1),
    'Heavy': (6,5,3,1),
}
ARMOURS = {
    'None':  (0,0,0, 0),
    'Light': (2,2,1, 0),
    'Medium':(4,3,1,-1),
    'Heavy': (6,4,0,-2),
}
STR_MIN_W={'LightCut':1,'HeavyCut':3,'LightBlunt':1,'HeavyBlunt':4}
CRIT_THRESH=3
TYPE_IDX={'LightCut':0,'HeavyCut':1,'LightBlunt':2,'HeavyBlunt':3}
HEAVY_TYPES={'HeavyCut','HeavyBlunt'}
LIGHT_TYPES={'LightCut','LightBlunt'}
RNG=np.random.default_rng(42)

def calc_pool(agi,hist): return max(5,agi*2+hist+3)
def max_wounds(end): return 2 if end<=3 else (3 if end<=5 else 4)
def calc_stam(end,hist,ar): return max(1,end+hist+1+ARMOURS[ar][3])
def get_dr(wtype,ar): return ARMOUR_DR[ar][TYPE_IDX[wtype]]
def hp_variant(end,ar,v):
    if v=='base': return end+4+ARMOURS[ar][0]
    if v=='A':    return end+ARMOURS[ar][0]
    return end  # B

def build_pool(w,ar,agi,str_,hist):
    pool=calc_pool(agi,hist)
    wtype=WEAPONS[w][1]
    dw=STR_MIN_W[wtype]-str_
    if dw>=2: return None
    if dw==1: pool-=1
    da=ARMOURS[ar][1]-str_
    if da>=2: return None
    if da==1: pool-=ARMOURS[ar][2]
    return max(5,pool)

def vroll(N,n,tn):
    if n<=0: return np.zeros(N,dtype=np.int32)
    return (RNG.integers(1,11,size=(N,n))>=tn).sum(axis=1).astype(np.int32)

def gen_char(N):
    off_pct   =RNG.uniform(0.30,0.70,N)
    mano_ratio=RNG.uniform(0.00,0.40,N)
    init_resp =RNG.uniform(-0.20,0.20,N)
    raw=RNG.uniform(0,1,(N,3))
    mano_w=raw/raw.sum(axis=1,keepdims=True)
    return {'off_pct':off_pct,'mano_ratio':mano_ratio,
            'init_resp':init_resp,'mano_w':mano_w}

def decide(c,N,alive,oob,ok,matched,has_init,hf,hf_opp,stam,dis_self,dis_opp,rng_roll):
    act=np.zeros(N,np.int8); done=np.zeros(N,bool)
    act=np.where(oob&alive,5,act);            done|=oob&alive
    act=np.where(~done&alive&dis_self,7,act); done|=~done&alive&dis_self
    nd=~done&alive&(hf<0.15)
    act=np.where(nd,4,act);                   done|=nd
    wr=~done&alive&~ok
    act=np.where(wr,1,act);                   done|=wr
    opp_dis=~done&alive&dis_opp
    do_m=~done&alive&(rng_roll<c['mano_ratio'])&~opp_dis
    r2=RNG.random(N)
    wf=c['mano_w'][:,0]; wd=c['mano_w'][:,0]+c['mano_w'][:,1]
    ma=np.where(r2<wf,2,np.where(r2<wd,6,3))
    act=np.where(do_m,ma,act); done|=do_m
    act=np.where(~done&alive,0,act)
    act=np.where(alive&dis_opp&~(act==3)&~(act==5)&~(act==7),0,act)
    return act

def alloc(c,dec,pool,has_init,N):
    adj=np.clip(c['off_pct']+np.where(has_init,c['init_resp'],-c['init_resp']),0.10,0.90)
    off=np.maximum(1,(pool*adj).astype(np.int32))
    off=np.where((dec==4)|(dec==5),0,
        np.where(dec==3,np.maximum(1,pool//3),off))
    off=np.minimum(off,pool-1)
    off=np.where((dec==4)|(dec==5),0,off)
    return off.astype(np.int32),(pool-off).astype(np.int32)

def sim(wA,arA,wB,arB,agi,str_,end,hist,N,MR,variant='B',mismatch=True):
    pA=build_pool(wA,arA,agi,str_,hist)
    pB=build_pool(wB,arB,agi,str_,hist)
    if pA is None or pB is None: return None

    rA,wtA,atnA,dtnA,dloA,dhiA,_=WEAPONS[wA]
    rB,wtB,atnB,dtnB,dloB,dhiB,_=WEAPONS[wB]
    dmgA=dhiA; dmgB=dhiB

    drA=get_dr(wtB,arA)  # A's armour vs B's weapon type
    drB=get_dr(wtA,arB)  # B's armour vs A's weapon type

    # Mass mismatch: does attacker's weapon outweigh defender's?
    # Heavy attacker vs Light defender: defender gets -1 def success (if split, not full guard)
    # Only when NOT at wrong range (long at close already handled)
    heavy_A=(wtA in HEAVY_TYPES); heavy_B=(wtB in HEAVY_TYPES)
    light_A=(wtA in LIGHT_TYPES); light_B=(wtB in LIGHT_TYPES)
    # mismatch_pen_on_B: A is heavy, B is light → B's defence -1 when split
    mismatch_pen_B = mismatch and heavy_A and light_B
    mismatch_pen_A = mismatch and heavy_B and light_A

    hpwA=hp_variant(end,arA,variant); hpwB=hp_variant(end,arB,variant)
    smA=calc_stam(end,hist,arA); smB=calc_stam(end,hist,arB)
    mw=max_wounds(end); use_wounds=(variant!='base')
    cA=gen_char(N); cB=gen_char(N)

    hA=np.full(N,hpwA,np.float32); hB=np.full(N,hpwB,np.float32)
    wcA=np.zeros(N,np.int32);       wcB=np.zeros(N,np.int32)
    sA=np.full(N,smA,np.int32);     sB=np.full(N,smB,np.int32)
    band=np.zeros(N,np.int8)
    incA=np.zeros(N,bool); incB=np.zeros(N,bool)
    init=np.zeros(N,np.int8); pend=np.full(N,-1,np.int8)
    rounds=np.full(N,MR,np.int32)
    disA=np.zeros(N,bool); disB=np.zeros(N,bool)
    ret_A=np.zeros(N,bool); ret_B=np.zeros(N,bool)

    for rnd in range(MR):
        alive=~incA&~incB
        if not alive.any(): break
        hp=pend>=0; init=np.where(hp&alive,pend,init); pend=np.where(alive,-1,pend)
        if ret_A.any():
            pw=0 if rA=='Short' else 1
            band=np.where(ret_A,pw,band); init=np.where(ret_A,1,init); ret_A[:]=False
        if ret_B.any():
            pw=0 if rB=='Short' else 1
            band=np.where(ret_B,pw,band); init=np.where(ret_B,0,init); ret_B[:]=False

        oobA=alive&(sA<=0); oobB=alive&(sB<=0)
        sA=np.where(oobA,smA,sA); sB=np.where(oobB,smB,sB)
        eA=np.where(oobA,np.maximum(1,(pA+1)//2),pA)
        eB=np.where(oobB,np.maximum(1,(pB+1)//2),pB)

        eff_atnA=np.where(disA,8,atnA); eff_dtnA=np.where(disA,9,dtnA)
        eff_dmgA=np.where(disA,0,dmgA).astype(float)
        eff_atnB=np.where(disB,8,atnB); eff_dtnB=np.where(disB,9,dtnB)
        eff_dmgB=np.where(disB,0,dmgB).astype(float)

        if rA=='Long': okA=(band==0)
        else:          okA=(band==1)
        if rB=='Long': okB=(band==0)
        else:          okB=(band==1)
        okA_e=np.where(disA,(band==1),okA)
        okB_e=np.where(disB,(band==1),okB)
        long_A_wrong=(rA=='Long')&(band==1)&~disA
        long_B_wrong=(rB=='Long')&(band==1)&~disB
        matched=okA_e&okB_e
        hfA=hA/hpwA; hfB=hB/hpwB
        has_iA=(init==0); has_iB=(init==1)
        rA_=RNG.random(N); rB_=RNG.random(N)

        decA=decide(cA,N,alive,oobA,okA_e,matched,
                    has_iA,hfA,hfB,sA,disA,disB,rA_)
        decB=decide(cB,N,alive,oobB,okB_e,matched,
                    has_iB,hfB,hfA,sB,disB,disA,rB_)

        offA,defA=alloc(cA,decA,eA,has_iA,N)
        offB,defB=alloc(cB,decB,eB,has_iB,N)
        offA=np.where(long_A_wrong&(decA==0),np.maximum(1,offA-1),offA)
        offB=np.where(long_B_wrong&(decB==0),np.maximum(1,offB-1),offB)

        bon_A=np.where((decB==4)|(decB==5),2,0)
        bon_B=np.where((decA==4)|(decA==5),2,0)

        sl=alive
        def med(arr,mask=None):
            m=mask if mask is not None else sl
            v=arr[m]; return int(np.median(v)) if len(v) else 4

        bA=med(offA+bon_A); bdB=med(defB)
        bB=med(offB+bon_B); bdA=med(defA)
        batnA=med(eff_atnA); bdtnA=med(eff_dtnA)
        batnB=med(eff_atnB); bdtnB=med(eff_dtnB)

        dmgB_=np.zeros(N,np.float32); dmgA_=np.zeros(N,np.float32)
        hit_A=np.zeros(N,bool); hit_B=np.zeros(N,bool)
        off_sA=np.zeros(N,np.int32); off_sB=np.zeros(N,np.int32)

        sA_=alive&(decA==0)&(okA_e|long_A_wrong)
        if sA_.any():
            a=vroll(N,bA,batnA); d=vroll(N,bdB,bdtnB)
            # Mismatch: A heavy, B light, B split (not full guard/oob)
            if mismatch_pen_B:
                is_split_B=~(decB==4)&~(decB==5)&~long_B_wrong
                d=np.where(is_split_B,np.maximum(0,d-1),d)
            h=sA_&(a>d); hit_A=h; off_sA=np.where(sA_,a,off_sA)
            excess=np.maximum(0.0,(a-d).astype(float))
            is_crit=h&(excess>=CRIT_THRESH)
            raw=np.where(is_crit,excess+str_+eff_dmgA*2,excess+str_+eff_dmgA)
            raw=np.maximum(0.0,raw-drB)
            raw=np.where(h&long_A_wrong,np.ceil(raw/2),raw)
            dmgB_=np.where(h,raw,0.0)

        sB_=alive&(decB==0)&(okB_e|long_B_wrong)
        if sB_.any():
            a=vroll(N,bB,batnB); d=vroll(N,bdA,bdtnA)
            if mismatch_pen_A:
                is_split_A=~(decA==4)&~(decA==5)&~long_A_wrong
                d=np.where(is_split_A,np.maximum(0,d-1),d)
            h=sB_&(a>d); hit_B=h; off_sB=np.where(sB_,a,off_sB)
            excess=np.maximum(0.0,(a-d).astype(float))
            is_crit=h&(excess>=CRIT_THRESH)
            raw=np.where(is_crit,excess+str_+eff_dmgB*2,excess+str_+eff_dmgB)
            raw=np.maximum(0.0,raw-drA)
            raw=np.where(h&long_B_wrong,np.ceil(raw/2),raw)
            dmgA_=np.where(h,raw,0.0)

        nb=band.copy(); ni=init.copy(); np_=pend.copy()

        dsA=alive&(decA==6)&(okA_e|long_A_wrong)&~hit_B
        if dsA.any():
            a=vroll(N,med(offA,dsA),atnA); d=vroll(N,med(defB,dsA),bdtnB)
            disB=np.where(dsA&(a>d),True,disB); off_sA=np.where(dsA,a,off_sA)
        dsB=alive&(decB==6)&(okB_e|long_B_wrong)&~hit_A
        if dsB.any():
            a=vroll(N,med(offB,dsB),atnB); d=vroll(N,med(defA,dsB),bdtnA)
            disA=np.where(dsB&(a>d),True,disA); off_sB=np.where(dsB,a,off_sB)

        rtA=alive&(decA==7)
        if rtA.any():
            es=vroll(N,med(offA,rtA),7); ok_r=rtA&(es>=off_sB)
            disA=np.where(ok_r,False,disA); ret_A=np.where(ok_r,True,ret_A)
        rtB=alive&(decB==7)
        if rtB.any():
            es=vroll(N,med(offB,rtB),7); ok_r=rtB&(es>=off_sA)
            disB=np.where(ok_r,False,disB); ret_B=np.where(ok_r,True,ret_B)

        fAvEB=alive&(decA==2)&(decB==1)&~hit_B
        if fAvEB.any():
            fs=vroll(N,med(offA,fAvEB),max(4,atnA-1))
            es=vroll(N,med(offB,fAvEB),7); fw=fAvEB&(fs>=es)
            nb=np.where(fAvEB&~fw,1 if rB=='Short' else 0,nb)
            ni=np.where(fAvEB&~fw,1,ni); np_=np.where(fw,0,np_)
        fBvEA=alive&(decB==2)&(decA==1)&~hit_A
        if fBvEA.any():
            fs=vroll(N,med(offB,fBvEA),max(4,atnB-1))
            es=vroll(N,med(offA,fBvEA),7); fw=fBvEA&(fs>=es)
            nb=np.where(fBvEA&~fw,0 if rA=='Short' else 1,nb)
            ni=np.where(fBvEA&~fw,0,ni); np_=np.where(fw,1,np_)
        fAn=alive&(decA==2)&(decB!=1)&~hit_B
        if fAn.any():
            fs=vroll(N,med(offA,fAn),max(4,atnA-1))
            fd=vroll(N,med(defB,fAn),bdtnB)
            np_=np.where(fAn&(fs>fd),0,np_)
        fBn=alive&(decB==2)&(decA!=1)&~hit_A
        if fBn.any():
            fs=vroll(N,med(offB,fBn),max(4,atnB-1))
            fd=vroll(N,med(defA,fBn),bdtnA)
            np_=np.where(fBn&(fs>fd),1,np_)

        eA_=alive&(decA==1)&(decB!=2)&~hit_B
        if eA_.any():
            es=vroll(N,med(offA,eA_),7); ok_e=eA_&(es>=off_sB)
            pref=1 if rA=='Short' else 0
            nb=np.where(ok_e,pref,nb); ni=np.where(ok_e,0,ni)
        eB_=alive&(decB==1)&(decA!=2)&~hit_A
        if eB_.any():
            es=vroll(N,med(offB,eB_),7); ok_e=eB_&(es>=off_sA)
            pref=1 if rB=='Short' else 0
            nb=np.where(ok_e,pref,nb); ni=np.where(ok_e,1,ni)

        brA=alive&(decA==3)&~hit_B
        if brA.any():
            br=vroll(N,med(offA,brA),7); sA=np.where(brA,np.minimum(smA,sA+br),sA)
        brB=alive&(decB==3)&~hit_A
        if brB.any():
            br=vroll(N,med(offB,brB),7); sB=np.where(brB,np.minimum(smB,sB+br),sB)

        ni=np.where(alive&okA_e&~okB_e&~long_A_wrong,0,ni)
        ni=np.where(alive&okB_e&~okA_e&~long_B_wrong,1,ni)
        ni=np.where(matched&hit_A&~hit_B,0,ni)
        ni=np.where(matched&hit_B&~hit_A,1,ni)
        bt=matched&alive&~((hit_A&~hit_B)|(hit_B&~hit_A))
        if bt.any():
            ra=vroll(N,agi,7); rb=vroll(N,agi,7)
            ni=np.where(bt&(ra>=2)&(rb<2),0,ni)
            ni=np.where(bt&(rb>=2)&(ra<2),1,ni)
            st=bt&((ra>=2)==(rb>=2))
            ni=np.where(st,RNG.integers(0,2,N).astype(np.int8),ni)

        band=nb; init=ni; pend=np_
        hA-=dmgA_; hB-=dmgB_
        sA=np.where(alive&(decA!=5),np.maximum(0,sA-1),sA)
        sB=np.where(alive&(decB!=5),np.maximum(0,sB-1),sB)

        if use_wounds:
            wA_=alive&(hA<=0); wB_=alive&(hB<=0)
            if wA_.any():
                wcA=np.where(wA_,wcA+1,wcA)
                incA=np.where(wA_,wcA>=mw,incA)
                hA=np.where(wA_&~incA,hpwA,hA)
            if wB_.any():
                wcB=np.where(wB_,wcB+1,wcB)
                incB=np.where(wB_,wcB>=mw,incB)
                hB=np.where(wB_&~incB,hpwB,hB)
        else:
            incA=np.where(alive&(hA<=0),True,incA)
            incB=np.where(alive&(hB<=0),True,incB)

        done=alive&(incA|incB)
        rounds=np.where(done&(rounds==MR),rnd+1,rounds)

    wAw=int((incB&~incA).sum()); wBw=int((incA&~incB).sum())
    res=rounds[rounds<MR]
    return {'rounds':res,'pct_res':len(res)/N,
            'pDraw':(rounds==MR).sum()/N,'pW':wAw/N,'pL':wBw/N}

def run_matrix(str_,end,agi,hist,N,MR,variant,mismatch,label):
    valid=[(w,ar) for w in WEAPONS for ar in ARMOURS
           if build_pool(w,ar,agi,str_,hist) is not None]
    results={}; seen=set()
    for wA,arA in valid:
        for wB,arB in valid:
            key=tuple(sorted([(wA,arA),(wB,arB)]))
            if key in seen: continue
            seen.add(key)
            (sA,saA),(sB,saB)=key
            r=sim(sA,saA,sB,saB,agi,str_,end,hist,N,MR,variant,mismatch)
            if r: results[key]=r

    all_r=np.concatenate([r['rounds'] for r in results.values() if len(r['rounds'])>0])
    pct=np.mean([r['pct_res'] for r in results.values()])
    to=np.mean([r['pDraw'] for r in results.values()])
    le10=(all_r<=10).mean()*100 if len(all_r) else 0

    wt_data=defaultdict(list)
    for k,r in results.items():
        (wA,arA),(wB,arB)=k
        wt_data[tuple(sorted([WEAPONS[wA][1],WEAPONS[wB][1]]))].extend(r['rounds'].tolist())

    build_wins=defaultdict(list)
    for (wA,arA),(wB,arB) in results:
        r=results[((wA,arA),(wB,arB))]
        build_wins[(wA,arA)].append(r['pW'])
        build_wins[(wB,arB)].append(r['pL'])
    avgs=sorted([(b,np.mean(v)) for b,v in build_wins.items()],key=lambda x:-x[1])

    print(f"\n{'='*72}")
    print(f"{label}")
    print(f"  Overall: res={pct*100:.0f}%  ≤10={le10:.0f}%  to={to*100:.0f}%  "
          f"med={np.median(all_r):.0f}  mean={np.mean(all_r):.1f}  "
          f"P10={np.percentile(all_r,10):.0f}  P90={np.percentile(all_r,90):.0f}")

    print(f"\n  Key weapon matchups (median / ≤10% / note):")
    pairs=[
        ('LightCut','LightCut','dagger vs dagger'),
        ('LightCut','HeavyCut','dagger vs longsword'),
        ('LightCut','HeavyBlunt','dagger vs war hammer'),
        ('HeavyCut','HeavyCut','longsword vs longsword'),
        ('HeavyCut','HeavyBlunt','longsword vs war hammer'),
        ('HeavyBlunt','HeavyBlunt','war hammer vs war hammer'),
        ('LightBlunt','HeavyBlunt','hand axe vs war hammer'),
    ]
    for wtA,wtB,note in pairs:
        k=tuple(sorted([wtA,wtB]))
        v=np.array(wt_data.get(k,[]))
        if len(v):
            print(f"    {note:<32}: med={np.median(v):.0f}  "
                  f"≤10={(v<=10).mean()*100:.0f}%")

    print(f"\n  Top 8:")
    for b,avg in avgs[:8]:
        print(f"    {b[0]+'/'+b[1]:<32} {avg*100:5.1f}%")
    print(f"  Bottom 6:")
    for b,avg in avgs[-6:]:
        print(f"    {b[0]+'/'+b[1]:<32} {avg*100:5.1f}%")

N=2000; MR=25; str_=3; end=3; agi=3; hist=2
run_matrix(str_,end,agi,hist,N,MR,'B',False,'Variant B — no mismatch penalty')
run_matrix(str_,end,agi,hist,N,MR,'B',True, 'Variant B — WITH mismatch penalty')
run_matrix(str_,end,agi,hist,N,MR,'base',False,'Baseline — no mismatch penalty')
run_matrix(str_,end,agi,hist,N,MR,'base',True, 'Baseline — WITH mismatch penalty')
print("\nDone.")
