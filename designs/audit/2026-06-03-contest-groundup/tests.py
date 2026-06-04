"""tests.py — unit + venue/win-condition/defeat + invariants + integration. Run: python3 tests.py"""
from math import isclose
import engine as E
from contract import A, B, other, Move, FaultState, Adjudicator, Panel
from primitives import (Stasis, Appeal, Standing, Reserve, Pool, SelfGating, Leverage, Room,
                        Resonance, Readiness, DefeatCatalogue)
from resolver import (ContestState, ThresholdRace, TallyAtClose, ProofBar, GraceThreshold, Venue)
from modes import ContestedMode, DyadicMode
from policy import (logos_spammer as LOG, demagogue as DEM, courtier as COU,
                    build_then_close as BTC, exploiter as EXP, overreacher as OV, staller as ST)
from collections import Counter

P = Fc = 0
def ck(n, c):
    global P, Fc
    if c: P += 1
    else: Fc += 1; print("  FAIL:", n)
def rate(venue, pa, pb, adj=None, N=2500, **kw):
    M = ContestedMode(venue, adjudicator=adj); w = Counter()
    for _ in range(N): w[M.play(4, 4, pa, pb, **kw)[0]] += 1
    return {k: v / N for k, v in w.items()}
def st(a_adv, b_adv):
    s = ContestState(); s.adv[A] = a_adv; s.adv[B] = b_adv; return s

NEUT = Adjudicator()
BOOK = Adjudicator(discipline=.9, char_ethos=.2, char_pathos=.1, char_logos=.7)
PATH = Adjudicator(discipline=.3, char_ethos=.2, char_pathos=.65, char_logos=.15)
LOWT = Adjudicator(discipline=.75, char_ethos=.2, char_pathos=.1, char_logos=.7)

print("== engine ==")
ck("sigma_N", isclose(E.sigma_N(16), 3.2))
ck("degree bands", (E.degree(0,3), E.degree(3,3), E.degree(6,3)) == (0,2,3))

print("== contract: Panel aggregation ==")
pan = Panel((Adjudicator(char_logos=.7, char_ethos=.2, char_pathos=.1, discipline=.8, learned=True),
             Adjudicator(char_pathos=.7, char_ethos=.2, char_logos=.1, discipline=.4, learned=False)))
ck("panel character averages", isclose(pan.character()["logos"], 0.4) and isclose(pan.character()["pathos"], 0.4))
ck("panel discipline averages", isclose(pan.discipline, 0.6))
ck("panel learned is majority", pan.learned is False)  # 1 of 2 → not majority

print("== primitives ==")
ck("Stasis ladder", Stasis.stronger_than("quality","fact") and Stasis.is_ground("fact"))
ck("Standing.frac", Standing(5).frac()==0.0 and Standing(10).frac()==1.0)
ck("Pool floor/term", Pool.size(-9)==5 and Pool.size(4)==11)
ck("Leverage N-collapsed (faculty+onground only)",
   isclose(Leverage.net(4, True), E.level("moderate")) and Leverage.net(5,True) > Leverage.net(4,True)
   and Leverage.net(4,False) < Leverage.net(4,True))
ck("SelfGating hard gated", (not SelfGating.licit("hard",5,5,True,False)) and SelfGating.licit("advance",5,5,True,False))
rm=Room(); rm.build(A,3); ck("Room.frac", 0 < rm.frac(A) <= 1.0)
ck("Resonance leak/effective/tension",
   Resonance.leak(.6,1.0) > Resonance.leak(.6,0.0)
   and isclose(Resonance.effective("logos",{"logos":.6},{"logos":.2},0.0),0.6)
   and isclose(Resonance.effective("logos",{"logos":.6},{"logos":.2},1.0),0.2)
   and Resonance.tension({"ethos":.5,"pathos":.3,"logos":.2},{"ethos":.5,"pathos":.3,"logos":.2}) == 0
   and Resonance.tension({"ethos":.8,"pathos":.1,"logos":.1},{"ethos":.1,"pathos":.1,"logos":.8}) > 0)
ck("Readiness floor/cap", isclose(Readiness.of(0,0),0.35) and isclose(Readiness.of(1,1),1.0))

print("== DefeatCatalogue is venue-configured ==")
fb = {A: FaultState(), B: FaultState(barred=True)}
ck("full catalogue clinches on barred", DefeatCatalogue().check(fb) == (B, "barred-device"))
ck("barred-disabled catalogue ignores it", DefeatCatalogue(barred=False).check(fb) is None)
ck("evasion disabled by 0", DefeatCatalogue(evasion_strikes=0).check({A:FaultState(evasion=5),B:FaultState()}) is None)

print("== WinConditions ==")
ck("ThresholdRace early + close + draw",
   ThresholdRace(5).resolve(st(6,3),False)==A and ThresholdRace(5).resolve(st(3,3),True)=="draw"
   and ThresholdRace(5).resolve(st(4,2),False) is None)
ck("TallyAtClose only at close",
   TallyAtClose().resolve(st(2,1),False) is None and TallyAtClose().resolve(st(2,1),True)==A)
ck("ProofBar asymmetric (burden on challenger)",
   ProofBar(4).resolve(st(6,1),False)==A and ProofBar(4).resolve(st(3,2),False) is None
   and ProofBar(4).resolve(st(3,2),True)==B)
ck("GraceThreshold (grant or deny)",
   GraceThreshold(5).resolve(st(6,0),False)==A and GraceThreshold(5).resolve(st(3,0),True)==B)

print("== invariants: fairness + modulation (preserved) ==")
w=rate("disputation",LOG,LOG,adj=NEUT,N=4000)
ck(f"SYMMETRY ~50/50 (a {w.get('a',0):.2f} b {w.get('b',0):.2f})", abs(w.get('a',0)-w.get('b',0))<0.06)
w=rate("disputation",LOG,DEM,adj=NEUT); ck(f"CONTEXT: logos venue → logos>pathos (a {w.get('a',0):.2f})", w.get('a',0)>0.7)
w=rate("assembly",LOG,DEM,adj=NEUT);    ck(f"CONTEXT: assembly → pathos>logos (b {w.get('b',0):.2f})", w.get('b',0)>0.7)
w=rate("court",LOG,DEM,adj=PATH);       ck(f"ADJUDICATOR: pathos judge flips court (b {w.get('b',0):.2f})", w.get('b',0)>0.7)
w=rate("disputation",EXP,LOG,adj=PATH); ck(f"TENSION: exploiter beats logos vs high-tension (a {w.get('a',0):.2f})", w.get('a',0)>0.7)
w=rate("disputation",EXP,LOG,adj=LOWT); ck(f"TENSION: logos beats exploiter, low-tension (b {w.get('b',0):.2f})", w.get('b',0)>0.7)
mod=Venue(proof_ethos=.225, proof_pathos=.225, proof_logos=.55, win=ThresholdRace(5.0))
w=rate(mod,BTC,LOG,adj=NEUT);            ck(f"F1: build-then-close pays in a MIXED venue (a {w.get('a',0):.2f})", w.get('a',0)>0.6)
w=rate("disputation",LOG,BTC,adj=NEUT);  ck(f"EXTREME venue → matched pure appeal wins (logos a {w.get('a',0):.2f})", w.get('a',0)>0.6)

print("== venue-determined win-condition: NEW behaviors ==")
w=rate("assembly",LOG,LOG,adj=NEUT,N=4000)   # the user's fix: tally resolves the mismatch
ck(f"TALLY resolves mismatch (draw {w.get('draw',0):.2f}, a {w.get('a',0):.2f} b {w.get('b',0):.2f})",
   w.get('draw',0) < 0.20 and abs(w.get('a',0)-w.get('b',0)) < 0.07)
w=rate("court",LOG,LOG,adj=NEUT,N=3000)       # proof-bar: burden of proof favours the defender
ck(f"PROOF-BAR favours defender on equal play (b {w.get('b',0):.2f})", w.get('b',0) > 0.6)

print("== venue-determined defeat-conditions (message 2) ==")
M_disp=ContestedMode("disputation"); M_asm=ContestedMode("assembly")
wn,why=M_disp.play(4,4,LOG,OV); ck("disputation: overreacher clinches out (barred)", wn=="a" and why=="clinch:barred-device")
wn,why=M_asm.play(4,4,LOG,OV);  ck("assembly: barred NOT fatal → not a barred clinch", why!="clinch:barred-device" and wn=="a")
ck("clean v clean no clinch (disputation)", sum(1 for _ in range(400) if M_disp.play(4,4,LOG,LOG)[1].startswith("clinch"))==0)

print("== adjudicator(s): panel aggregation in play ==")
wlogos=rate("court",LOG,DEM,adj=BOOK)                         # single by-the-book logos judge
wpanel=rate("court",LOG,DEM,adj=Panel((BOOK,PATH)))          # logos + pathos panel
ck(f"panel softens single-judge dominance (demagogue {wlogos.get('b',0):.2f}→{wpanel.get('b',0):.2f})",
   wpanel.get('b',0) > wlogos.get('b',0))

print("== jitter: high-faculty exact-tie draws resolved ==")
Mdisp=ContestedMode("disputation"); dd=Counter()
for _ in range(2500): dd[Mdisp.play(7,7,LOG,LOG)[0]]+=1
ck(f"f7 matched resolves (draw {dd['draw']/2500:.2f})", dd['draw']/2500 < 0.10)

print("== evidence apparatus (hidden value, relevance, corroboration) ==")
from primitives import EvidenceItem, Dossier
from resolver import Bout, Contestant, Venue, ThresholdRace
from policy import advocate as ADV
EV=lambda: Dossier([EvidenceItem(Stasis.FACT,2.5),EvidenceItem(Stasis.FACT,2.0),EvidenceItem(Stasis.FACT,1.5)])
EVV=Venue(proof_ethos=.25,proof_pathos=.20,proof_logos=.55,start_ground=Stasis.FACT,win=ThresholdRace(5.0))
def evrate(da,db,N=2000):
    w=Counter()
    for _ in range(N): w[Bout(Contestant(4,dossier=da()),Contestant(4,dossier=db()),EVV,NEUT).resolve(ADV,ADV)[0]]+=1
    return {k:x/N for k,x in w.items()}
w=evrate(EV, lambda:Dossier([]));                               ck(f"holder beats non-holder (a {w.get('a',0):.2f})", w.get('a',0)>0.9)
w=evrate(EV, EV);                                               ck(f"holder vs holder symmetric (a {w.get('a',0):.2f})", abs(w.get('a',0)-w.get('b',0))<0.07)
w=evrate(lambda:Dossier([EvidenceItem(Stasis.FACT,2.5)]), EV);  ck(f"more relevant evidence wins (b {w.get('b',0):.2f})", w.get('b',0)>0.6)
w=evrate(lambda:Dossier([EvidenceItem(Stasis.QUALITY,3.0)]), lambda:Dossier([])); ck(f"irrelevant evidence = no edge (a {w.get('a',0):.2f})", abs(w.get('a',0)-w.get('b',0))<0.12)
bv=Bout(Contestant(4,dossier=EV()),Contestant(4),Venue(start_ground=Stasis.FACT),NEUT)
ck("view exposes COUNT, value hidden", bv._view(A,0).evidence_available==3 and not hasattr(bv._view(A,0),'weight'))
d=EV(); _,f1=d.present(d.best(Stasis.FACT)); _,f2=d.present(d.best(Stasis.FACT)); _,f3=d.present(d.best(Stasis.FACT))
ck("corroboration diminishes", f1>f2>f3)
wM=Counter()
for _ in range(2000): wM[ContestedMode("disputation").play(4,4,ADV,LOG, da=EV())[0]]+=1
ck(f"evidence reaches engine via ContestedMode facade (a {wM['a']/2000:.2f})", wM['a']/2000 > 0.8)
spec_reuse=Contestant(4, dossier=Dossier([EvidenceItem(Stasis.FACT,2.0)]))
_b1=Bout(spec_reuse, Contestant(4), Venue(start_ground=Stasis.FACT), NEUT); _av0=_b1._view(A,0).evidence_available; _b1.resolve(ADV,LOG)
_b2=Bout(spec_reuse, Contestant(4), Venue(start_ground=Stasis.FACT), NEUT); _av1=_b2._view(A,0).evidence_available
ck("Contestant spec reusable across bouts (runtime isolated)", _av0==1 and _av1==1)

print("== institutional / public pressure on the adjudicator ==")
from contract import Pressure
flat=dict(proof_ethos=.34,proof_pathos=.33,proof_logos=.33,win=ThresholdRace(5.0))
logos_role=dict(proof_ethos=.25,proof_pathos=.20,proof_logos=.55,start_ground=Stasis.FACT,win=ThresholdRace(5.0))
def prate(pr,adj,pa,pb,roles=None,N=2500):
    rr=roles or flat; w=Counter()
    for _ in range(N): w[Bout(Contestant(4),Contestant(4),Venue(**rr,pressure=pr),adj).resolve(pa,pb)[0]]+=1
    return {k:x/N for k,x in w.items()}
w=prate(Pressure(),NEUT,LOG,LOG);                          ck(f"no pressure symmetric (a {w.get('a',0):.2f})", abs(w.get('a',0)-w.get('b',0))<0.06)
w=prate(Pressure(toward='a',institutional=0.5),NEUT,LOG,LOG); ck(f"institutional tilts the verdict (a {w.get('a',0):.2f})", w.get('a',0)>0.65)
crowd=Adjudicator(discipline=.85,char_pathos=.65,char_ethos=.2,char_logos=.15)
lo=prate(Pressure(public=0.0),crowd,DEM,LOG,roles=logos_role); hi=prate(Pressure(public=0.7),crowd,DEM,LOG,roles=logos_role)
ck(f"public pressure unlocks the crowd-judge ({lo.get('a',0):.2f}→{hi.get('a',0):.2f})", hi.get('a',0) > lo.get('a',0)+0.1)

print("== PersuasionTrack: banded two-pole outcome (committee/decisive/total) ==")
from resolver import PersuasionTrack as PT
def _bands(fa,fb,N=600):
    w=Counter()
    for _ in range(N):
        v=Venue(proof_logos=.5,proof_ethos=.3,proof_pathos=.2,start_ground=Stasis.QUALITY,win=PT())
        w[Bout(Contestant(fa),Contestant(fb),v,NEUT).resolve(LOG,LOG)[0]]+=1
    return w
_m=_bands(4,4); ck(f"matched → committee plurality ({_m['committee']/600:.2f})", _m['committee']/600 > 0.6)
_lop=_bands(6,2); _dec=(_lop['A_decisive']+_lop['A_total'])/600; ck(f"skill gap → decisive majority ({_dec:.2f})", _dec > 0.6)
ck("committee reachable (canon 4-6 zone)", _m['committee'] > 0)

print("== faction adapter: banded votes (committee) + succession (on PersuasionTrack) ==")
import faction as FX
from faction import Faction as FFac
ck("band_of clear pass", FX.band_of(0.70,0.50)=='pass')
ck("band_of clear fail", FX.band_of(0.30,0.50)=='fail')
ck("band_of near-threshold committee", FX.band_of(0.52,0.50)=='committee')
_prop=FFac("P",4,5,(.45,.2,.35)); _targ=FFac("T",2,3,(.2,.35,.45)); _oth=[FFac("H",3,4,(.2,.2,.6)),FFac("C",2,4,(.6,.2,.2)),FFac("G",2,3,(.2,.2,.6))]
_d,_=FX.rate_banded(_prop,_targ,[_prop,_targ]+_oth,"censure",LOG,DEM,N=300)
ck(f"strong proposer Censure pass-dominant ({_d.get('pass',0):.2f})", _d.get('pass',0) > 0.7)
_ms=FX.succession_rate(4,4,NEUT,N=300); ck(f"matched succession splits ({_ms.get('split',0):.2f})", _ms.get('split',0) > 0.6)
_os=FX.succession_rate(7,1,NEUT,N=300); ck(f"overwhelming succession decisive/unified ({_os.get('decisive',0)+_os.get('unified',0):.2f})", (_os.get('decisive',0)+_os.get('unified',0)) > 0.5)
_o=FX.succession(4,4,NEUT); ck("succession split ratio canonical (§7.2.1)", _o[0]!='split' or _o[2] in (0.50,0.55,0.60))
_Fc=lambda n,m: FFac(n,m,4,(.34,.33,.33))
_sp=[(_Fc("a",4),'pro'),(_Fc("b",3),'pro'),(_Fc("c",2),'anti'),(_Fc("d",2),'anti')]
_bal=[(_Fc("a",4),'pro'),(_Fc("b",2),'pro'),(_Fc("c",4),'anti'),(_Fc("d",2),'anti')]
_dp=FX.coalition_rate(_sp,N=400); ck(f"§10 strong-pro coalition leans pass ({_dp.get('pass',0):.2f}>{_dp.get('fail',0):.2f})", _dp.get('pass',0) > _dp.get('fail',0))
_db=FX.coalition_rate(_bal,N=400); ck(f"§10 balanced coalition symmetric ({abs(_db.get('pass',0)-_db.get('fail',0)):.2f})", abs(_db.get('pass',0)-_db.get('fail',0)) < 0.12)
ck("§10 committee reachable", _db.get('committee',0) > 0)
_dl=FX.coalition_rate(_bal,N=400,lobby=1.0); ck(f"§10 lobby tilts to pro ({_dl.get('pass',0):.2f}>{_db.get('pass',0):.2f})", _dl.get('pass',0) > _db.get('pass',0))

print("== validation + scaffolds ==")
def bad(v): return Move("garbage")
try: M_disp.play(4,4,bad,LOG); ck("validation raises", False)
except ValueError: ck("validation raises", True)
try: DyadicMode().play(); ck("scaffold raises", False)
except NotImplementedError: ck("scaffold raises", True)

print(f"\nRESULT: {P} passed, {Fc} failed")
