import os, sys, random
_HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, _HERE)
_SIM = os.path.abspath(os.path.join(_HERE, '..', '..', 'tests', 'sim')); sys.path.insert(0, _SIM)
import gauge_mb as g
import cannae_calib as cc

def run(n, ba, bb, label):
    A=B=d=0
    for s in range(n):
        random.seed(1_000_000+s)
        ua=ba('A','A'); ub=bb('B','B')
        r=g.resolve_battle(ua,ub,'Line','Line',g.ANCHOR_MAP,kind='multi',max_battle_turns=20)
        w=r.get('winner','draw'); A+=w=='A'; B+=w=='B'; d+=w not in('A','B')
    dec=A+B; decA=100.0*A/dec if dec else 50.0
    print(f"  {label:46} A {A:2} B {B:2} draw {d:2}  decA={decA:5.1f}%")

if __name__=='__main__':
    n=int(sys.argv[1]) if len(sys.argv)>1 else 20
    thin=lambda nm,fc: g._envelop_army(nm,fc)
    print(f"H3 thin-enveloper(A) vs deep/granular Line(B), n={n}  band 55-72")
    for ns in (1,3,6):
        for dep in (1,2,3):
            wd=lambda nm,fc,ns=ns,dep=dep: cc.granular_line_wd(nm,fc,n_sub=ns,width=1 if dep>1 else None,depth=dep if dep>1 else None) if dep>1 else cc.granular_line(nm,fc,n_sub=ns)
            run(n, thin, wd, f'{ns}-subunit x depth~{dep}')
