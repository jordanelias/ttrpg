"""Does the enveloper's wing wrap work in BOTH orientations? Report the defender-struck faces when the
enveloper is side A (advance_dir -1) vs side B (advance_dir +1). If as B the defender is only struck
FRONT, the wing wheel has a directional pathing bug. Run: python side_face_probe.py [n]"""
import os, sys, random
_HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, _HERE)
_SIM = os.path.abspath(os.path.join(_HERE, '..', '..', 'tests', 'sim')); sys.path.insert(0, _SIM)
import gauge_mb as g
import mass_battle.orchestration as O

def _mean_facing(atom):
    fv = getattr(atom, 'cell_facing_vec', None)
    if fv:
        rs = sum(v[0] for v in fv.values()); cs = sum(v[1] for v in fv.values())
        if rs or cs: return (rs, cs)
    return (atom.advance_dir, 0)

def _nearest_face(dcells, dfac, acen):
    n=len(dcells); cr=sum(r for r,c in dcells)/n; cc=sum(c for r,c in dcells)/n
    fm=(dfac[0]**2+dfac[1]**2)**0.5 or 1.0; fu=(dfac[0]/fm,dfac[1]/fm); pu=(-fu[1],fu[0])
    al=[(r-cr)*fu[0]+(c-cc)*fu[1] for r,c in dcells]; pp=[(r-cr)*pu[0]+(c-cc)*pu[1] for r,c in dcells]
    faces={'F':(cr+max(al)*fu[0],cc+max(al)*fu[1]),'B':(cr+min(al)*fu[0],cc+min(al)*fu[1]),
           'L':(cr+max(pp)*pu[0],cc+max(pp)*pu[1]),'R':(cr+min(pp)*pu[0],cc+min(pp)*pu[1])}
    return min(faces,key=lambda k:(faces[k][0]-acen[0])**2+(faces[k][1]-acen[1])**2)

STATS={}
_orig=O.resolve_engagements_cascading
DEF_SIDE=['B']
def _patched(ua,ub,pairs,t=None):
    for p in pairs:
        # only track faces on the DEFENDER (the command-line side)
        for datom,atk in ((p['atom_b'],p['a_cells']),(p['atom_a'],p['b_cells'])):
            if getattr(datom,'faction',None)!=DEF_SIDE[0]: continue
            dc=list(datom.cells()); ac=list(set(atk))
            if not dc or not ac: continue
            acen=(sum(r for r,c in ac)/len(ac),sum(c for r,c in ac)/len(ac))
            STATS.setdefault('faces',set()).add(_nearest_face(dc,_mean_facing(datom),acen))
    return _orig(ua,ub,pairs,t=t)
O.resolve_engagements_cascading=_patched
try:
    import mass_battle.engine as E
    if hasattr(E,'resolve_engagements_cascading'): E.resolve_engagements_cascading=_patched
except Exception: pass

def run(n, env_side):
    def_side='B' if env_side=='A' else 'A'; DEF_SIDE[0]=def_side; STATS.clear()
    ew=lw=d=0
    for s in range(n):
        random.seed(1_000_000+s)
        if env_side=='A': ua=g._envelop_army('A','A'); ub=g._command_army('Line')('B','B')
        else: ua=g._command_army('Line')('A','A'); ub=g._envelop_army('B','B')
        r=g.resolve_battle(ua,ub,'Line','Line',g.ANCHOR_MAP,kind='multi',max_battle_turns=20)
        w=r.get('winner','draw'); ew+=w==env_side; lw+=(w in('A','B') and w!=env_side); d+=w not in('A','B')
    dec=ew+lw
    print(f"  enveloper side {env_side}: env {ew:2} line {lw:2} draw {d:2} envwin {100.0*ew/dec if dec else 50:5.1f}%  defender struck faces: {sorted(STATS.get('faces',set()))}")

if __name__=='__main__':
    n=int(sys.argv[1]) if len(sys.argv)>1 else 30
    print(f"Wing-wrap face diagnostic per side, n={n}  [F-only => wings not wrapping]")
    run(n,'A'); run(n,'B')
