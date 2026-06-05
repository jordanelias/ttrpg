"""tests.py — unit + venue/win-condition/defeat + invariants + integration. Run: python3 tests.py"""
from math import isclose
import engine as E
from contract import A, B, other, Move, FaultState, Adjudicator, Panel
from primitives import (Stasis, Appeal, Standing, Reserve, Pool, SelfGating, Leverage, Room,
                        Resonance, Readiness, DefeatCatalogue)
from resolver import (ContestState, ThresholdRace, TallyAtClose, ProofBar, GraceThreshold, Venue)
from engine import degree
from modes import ContestedMode, DyadicMode
from policy import (logos_spammer as LOG, demagogue as DEM, courtier as COU,
                    build_then_close as BTC, exploiter as EXP, overreacher as OV, staller as ST)
from collections import Counter
import random, sys
random.seed(20260603)   # audit: deterministic, reproducible suite (was unseeded)

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
wn,why=M_disp.play(4,4,LOG,OV); ck("disputation: overreacher clinches out (barred)", wn=="a" and why.startswith("clinch:barred-device"))
wn,why=M_asm.play(4,4,LOG,OV);  ck("assembly: barred NOT fatal → not a barred clinch", not why.startswith("clinch:barred-device") and wn=="a")
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
def _commfrac(pro,anti,nab,N=2000):
    body=[(_Fc("p",pro),'pro'),(_Fc("q",anti),'anti')]+[(_Fc(f"x{i}",6),'abstain') for i in range(nab)]
    return sum(1 for _ in range(N) if FX.coalition_vote(body)=='committee')/N
ck("R1: abstainer resistance pulls committee at SMALL pools", _commfrac(10,8,2) > _commfrac(10,8,0)+0.03)
ck("R1: abstainer resistance pulls committee at LARGE pools (was inert pre-fix)", _commfrac(30,28,2) > _commfrac(30,28,0)+0.03)

print("== temporal register: extended ground axis (forum weights past<->future) ==")
from resolver import Bout, Contestant, TallyAtClose
from modes import VENUES
# (1) calibration is a normalized tilt: court favours past, assembly future; a neutral venue is exactly 1.0
_ct=VENUES["court"]().tense_weight(); _as=VENUES["assembly"]().tense_weight(); _nt=Venue().tense_weight()
ck(f"court past-tilt > future ({_ct['past']:.2f}>{_ct['future']:.2f})", _ct['past'] > _ct['future'])
ck(f"assembly future-tilt > past ({_as['future']:.2f}>{_as['past']:.2f})", _as['future'] > _as['past'])
ck("neutral venue tense_weight == 1.0 (the no-regression guarantee)", all(isclose(_nt[k],1.0) for k in _nt))
# (2) argument: a venue rewards arguing in its register. Hold all else fixed; vary only the live register
#     (start_ground) and the venue's tense weights; measure A's accumulated advantage (TallyAtClose => full budget).
def _adv(start_ground, past, present, future, N=300):
    tot=0.0
    for _ in range(N):
        b=Bout(Contestant(4), Contestant(4),
               Venue(start_ground=start_ground, proof_ethos=.25, proof_pathos=.20, proof_logos=.55,
                     proof_past=past, proof_present=present, proof_future=future, win=TallyAtClose()), NEUT)
        b.resolve(LOG, LOG); tot += b.state.adv[A]
    return tot/N
_pf=_adv(Stasis.FACT,.60,.30,.10); _pc=_adv(Stasis.CONSEQUENCE,.60,.30,.10)
ck(f"past-weighted venue rewards past-ground argument ({_pf:.1f} > {_pc:.1f})", _pf > _pc*2.0)
_ff=_adv(Stasis.FACT,.10,.30,.60); _fc=_adv(Stasis.CONSEQUENCE,.10,.30,.60)
ck(f"future-weighted venue rewards future-ground argument ({_fc:.1f} > {_ff:.1f})", _fc > _ff*2.0)
# (3) evidence flows through the same temporal factor (logos-asymmetry resolution: forensic strength = evidence).
#     Same FACT-evidence, same live ground (FACT); only the venue's tense weighting differs.
_EVf=lambda: Dossier([EvidenceItem(Stasis.FACT,2.5), EvidenceItem(Stasis.FACT,2.0)])
def _adv_ev(past, present, future, N=300):
    tot=0.0
    for _ in range(N):
        b=Bout(Contestant(4, dossier=_EVf()), Contestant(4),
               Venue(start_ground=Stasis.FACT, proof_ethos=.25, proof_pathos=.20, proof_logos=.55,
                     proof_past=past, proof_present=present, proof_future=future, win=TallyAtClose()), NEUT)
        b.resolve(ADV, LOG); tot += b.state.adv[A]
    return tot/N
_ep=_adv_ev(.60,.30,.10); _ev=_adv_ev(.10,.30,.60)
ck(f"FACT-evidence is potent in a past venue, weak in a future venue ({_ep:.1f} > {_ev:.1f})", _ep > _ev*1.5)

print("== Standing split (PROTOTYPE flag): ascribed Rank vs earned Credit ==")
def _bth(v):  # build (ethos) for three turns, then attempt overreach
    return Move("advance","ethos",v.live_ground) if v.i < 3 else Move("hard","logos",v.live_ground)
_UNL = Adjudicator(learned=False)
_Vf = Venue(start_ground=Stasis.FACT, win=TallyAtClose(), split_standing=False)
_Vs = Venue(start_ground=Stasis.FACT, win=TallyAtClose(), split_standing=True)
ck("split flag defaults off (fused engine is the default)", Venue().split_standing is False)
# Texture 1 — under the split, earned credibility does NOT license overreach (rank-gated); fused, it does
def _barred_out(venue, N=250):
    n = 0
    for _ in range(N):
        wn, why = Bout(Contestant(4, standing_start=3), Contestant(4, standing_start=2), venue, _UNL).resolve(_bth, LOG)
        if wn == "b" and "barred" in why: n += 1
    return n / N
ck("split: ethos cannot buy hard-licence (low-born barred out)", _barred_out(_Vs) > 0.8)
ck("fused: ethos buys hard-licence (low-born not barred)",       _barred_out(_Vf) < 0.2)
# Texture 2 — fused, ascribed standing lends argument force; split, it lends none
def _awin(venue, N=400):
    return sum(1 for _ in range(N) if Bout(Contestant(4, standing_start=9), Contestant(4), venue, NEUT).resolve(LOG, LOG)[0] == "a") / N
ck("fused: ascribed standing lends force (high-born dominates)", _awin(_Vf) > 0.75)
ck("split: ascribed rank lends no force (high-born ~even)",      0.35 < _awin(_Vs) < 0.65)

# == narrative layer (post-bout chronicle: legibility + scenario classification) ==
import narrative as NAR
_trv = lambda: Venue(start_ground=Stasis.FACT, win=ThresholdRace(6.0))
# instrumentation is inert by default, records only when asked
ck("narrative: record=False leaves no log", Bout(Contestant(4), Contestant(4), _trv(), NEUT).log is None)
_rb = Bout(Contestant(4), Contestant(4), _trv(), NEUT, record=True); _rw, _rwhy = _rb.resolve(LOG, DEM)
ck("narrative: record=True captures a beat log", isinstance(_rb.log, list) and len(_rb.log) > 0)
ck("narrative: clean win names a decisive appeal", NAR.summarize(_rb.log, _rw, _rwhy).decisive_appeal in Appeal.ALL)
# a fault ends the bout as COLLAPSE, rendered as a fault, won by the non-faulter
_cb = Bout(Contestant(4), Contestant(4), VENUES["court"](), NEUT, record=True); _cw, _cwhy = _cb.resolve(OV, LOG)
_cc = NAR.summarize(_cb.log, _cw, _cwhy)
ck("narrative: overreach bout classifies COLLAPSE", _cc.shape == "COLLAPSE")
ck("narrative: COLLAPSE render reports a fault",    "faulted out" in _cc.render())
ck("narrative: COLLAPSE won by the non-faulter",    _cw == "b")
# the scenario taxonomy is live (reachable) and non-degenerate
def _shapes(ka, kb, adj, pa, pb, N=300):
    c = Counter()
    for _ in range(N):
        b = Bout(ka, kb, _trv(), adj, record=True); w, why = b.resolve(pa, pb)
        c[NAR.summarize(b.log, w, why).shape] += 1
    return c
ck("narrative: big skill gap reaches ROUT",                _shapes(Contestant(7), Contestant(2), NEUT, LOG, LOG)["ROUT"] > 0)
ck("narrative: balanced REVERSAL is a minority not default", _shapes(Contestant(4), Contestant(4), NEUT, LOG, DEM)["REVERSAL"] < 150)
# public pre-contest cue + graceful empty input
ck("narrative: venue_brief surfaces the court's logos reward", "logos" in NAR.venue_brief(VENUES["court"]()))
ck("narrative: empty log => DEADLOCK", NAR.summarize([], "draw", "draw").shape == "DEADLOCK")
# --- truth tests: hand-built logs with KNOWN trajectories => assert the chronicle is CORRECT, not just
# well-formed (closes critique-P1: nothing checked turning_point / decisive / margin against a known bout).
def _bt(i, side, gain, advA, advB, appeal="logos", ground="fact", kind="advance", fault=None):
    return dict(i=i, side=side, kind=kind, appeal=appeal, ground=ground, gain=gain,
                live=ground, advA=advA, advB=advB, fault=fault)
# (1) REVERSAL: A leads through ex3, B overtakes at ex4 and wins; B's gains are mostly pathos.
_rev = [_bt(0,A,2,2,0),_bt(0,B,0,2,0), _bt(1,A,1,3,0),_bt(1,B,0,3,0), _bt(2,A,1,4,0),_bt(2,B,2,4,2,"pathos"),
        _bt(3,A,0,4,2),_bt(3,B,1,4,3,"ethos"), _bt(4,A,0,4,3),_bt(4,B,3,4,6,"pathos"), _bt(5,A,0,4,6),_bt(5,B,2,4,8,"pathos")]
_cr = NAR.summarize(_rev, "b", "win")
ck("narrative truth: late comeback classifies REVERSAL",     _cr.shape == "REVERSAL")
ck("narrative truth: turning_point is the crossing exchange", _cr.turning_point == 4)
ck("narrative truth: decisive appeal = pathos (by realised gain)", _cr.decisive_appeal == "pathos")
ck("narrative truth: margin = |4-8|/12",                      isclose(_cr.margin, 4/12))
# (2) ROUT: A dominant, never behind, large margin.
_rt = [_bt(0,A,3,3,0),_bt(0,B,0,3,0), _bt(1,A,3,6,0),_bt(1,B,0,6,0), _bt(2,A,2,8,0),_bt(2,B,0,8,0)]
_ct = NAR.summarize(_rt, "a", "win")
ck("narrative truth: wire-to-wire dominance => ROUT", _ct.shape == "ROUT")
ck("narrative truth: ROUT decisive appeal = logos",   _ct.decisive_appeal == "logos")
ck("narrative truth: ROUT margin = 1.0",              isclose(_ct.margin, 1.0))
# (3) COLLAPSE: fault at ex1; turning_point is the clinch exchange, decisive factor is None (the win is the fault).
_co = [_bt(0,A,2,2,0),_bt(0,B,0,2,0), _bt(1,A,0,2,0,kind="hard",fault="overreach not licensed by standing (chala/jati)")]
_cco = NAR.summarize(_co, "b", "clinch:barred-device - overreach not licensed by standing (chala/jati)")
ck("narrative truth: fault end classifies COLLAPSE",        _cco.shape == "COLLAPSE")
ck("narrative truth: COLLAPSE turning_point = clinch exch", _cco.turning_point == 1)
ck("narrative truth: COLLAPSE decisive_appeal is None",     _cco.decisive_appeal is None)
ck("narrative truth: COLLAPSE render names the fault",      "faulted out" in _cco.render() and "overreach" in _cco.render())
# recording is provably inert: same seed, record off vs on => identical (winner, why) (substantiates P3).
def _same(seed):
    random.seed(seed); o1 = Bout(Contestant(4), Contestant(4), _trv(), NEUT).resolve(LOG, DEM)
    random.seed(seed); o2 = Bout(Contestant(4), Contestant(4), _trv(), NEUT, record=True).resolve(LOG, DEM)
    return o1 == o2
ck("narrative: recording is inert (same seed => same outcome)", all(_same(s) for s in range(50)))

# == FORKS (opt-in prototypes): un-fused verdict (VoteAtClose) + bounded rebuttal + split-decision narrative ==
from resolver import VoteAtClose, REBUT_CAP
# Fork 1 — VoteAtClose: no-noise vote tracks momentum; with noise the verdict is genuinely separable from it
_stA = ContestState(); _stA.adv[A] = 5.0
ck("fork1: no-noise vote tracks the room",          VoteAtClose(jurors=7, noise=0.0).resolve(_stA, closing=True) == A)
ck("fork1: VoteAtClose is silent before close",     VoteAtClose().resolve(_stA, closing=False) is None)
_stS = ContestState(); _stS.adv[A] = 1.0
random.seed(7)
_vw = [VoteAtClose(jurors=7, sharpness=0.6, noise=1.5).resolve(_stS, closing=True) for _ in range(300)]
ck("fork1: noisy verdict can uphold the room", _vw.count(A) > 0)
ck("fork1: noisy verdict can upset the room",  _vw.count(B) > 0)     # the vote crosses momentum => genuinely un-fused
# Fork 3 — rebut: off by default (fault, opponent untouched); on, it erases bounded adv, floored at 0
_Vno = Venue(start_ground=Stasis.FACT, win=ThresholdRace(6.0))
_Vye = Venue(start_ground=Stasis.FACT, win=ThresholdRace(6.0), allow_rebuttal=True)
def _reb(venue, opp_start, seed):
    random.seed(seed); b = Bout(Contestant(5), Contestant(5), venue, NEUT)
    b.state.adv[B] = opp_start; b._apply(A, Move("rebut", ground="fact"))
    return b.state.adv[B], b.c[A].fault
_off_adv, _off_flt = _reb(_Vno, 10.0, 1)
ck("fork3: rebuttal off-limits leaves opponent intact", _off_adv == 10.0)
ck("fork3: rebuttal off-limits is a fault",             _off_flt.evasion >= 1)
random.seed(3); _bounded = True; _reduced = 0
for s in range(40):
    a2, _ = _reb(_Vye, 10.0, s)
    if not (0.0 <= a2 <= 10.0): _bounded = False
    if a2 < 10.0: _reduced += 1
ck("fork3: a landed rebuttal stays within [0, start]", _bounded)
ck("fork3: a rebuttal lands sometimes (reduces opp adv)", _reduced > 0)
ck("fork3: tiny opponent adv floors at 0, never negative", all(0.0 <= _reb(_Vye, 1.0, 100 + s)[0] <= 1.0 for s in range(40)))
ck("fork3: a single cut cannot exceed REBUT_CAP", REBUT_CAP <= 3.0 and all(10.0 - _reb(_Vye, 10.0, 200 + s)[0] <= REBUT_CAP for s in range(40)))
# Fork 2 — SPLIT_DECISION: verdict crosses the room; render contrasts room vs verdict
def _b2(i, s, g, a, b): return dict(i=i, side=s, kind="advance", appeal="logos", ground="fact", gain=g, live="fact", advA=a, advB=b, fault=None)
_split = [_b2(0,A,6,6,0),_b2(0,B,0,6,0), _b2(1,A,4,10,0),_b2(1,B,2,10,2)]   # A carried the room 10-2, vote went to B
_cs = NAR.summarize(_split, "b", "win")
ck("fork2: verdict crossing the room => SPLIT_DECISION", _cs.shape == "SPLIT_DECISION")
ck("fork2: room_leader is the momentum leader (A)",      _cs.room_leader == A)
ck("fork2: SPLIT render contrasts room and verdict",     "room" in _cs.render() and "verdict" in _cs.render())
ck("fork2: verdict matching the room is not a split",    NAR.summarize(_split, "a", "win").shape != "SPLIT_DECISION")
ck("fork2: classified shapes are declared SHAPES",       _cs.shape in NAR.SHAPES and NAR.summarize(_split, "a", "win").shape in NAR.SHAPES)
# Fork 1+2 end-to-end: a VoteAtClose bout can actually produce a split decision
_seen = False
for s in range(200):
    random.seed(1000 + s)
    vb = Bout(Contestant(5), Contestant(5), Venue(start_ground=Stasis.FACT, win=VoteAtClose(jurors=7, noise=1.5)), NEUT, record=True)
    vw, vy = vb.resolve(LOG, LOG)
    if NAR.summarize(vb.log, vw, vy).shape == "SPLIT_DECISION": _seen = True; break
ck("fork1+2: a VoteAtClose bout can yield a SPLIT_DECISION", _seen)

# == INSTITUTIONAL REGIMES (fork-enabled modes.py presets; mechanics only) ==
import modes as MOD
_arb = MOD.single_arbiter_mode(); _del = MOD.deliberative_body_mode(panel_size=7, noise=1.2); _sch = MOD.scholastic_disputation_mode()
ck("modes: fused_arbiter is fused (TallyAtClose), no rebuttal", isinstance(_arb.venue.win, TallyAtClose) and _arb.venue.allow_rebuttal is False)
ck("modes: fused_arbiter judged by a single adjudicator",       isinstance(_arb.adj, Adjudicator))
ck("modes: deliberative_body un-fuses verdict (VoteAtClose)",   isinstance(_del.venue.win, VoteAtClose))
ck("modes: deliberative_body permits rebuttal",                 _del.venue.allow_rebuttal is True)
ck("modes: deliberative_body judged by a Panel of n",           isinstance(_del.adj, Panel) and len(_del.adj.members) == 7)
ck("modes: scholastic_disputation is a clinch race + rebuttal", isinstance(_sch.venue.win, ThresholdRace) and _sch.venue.allow_rebuttal is True)
ck("modes: registry exposes exactly the three regimes",         set(MOD.INSTITUTIONAL_MODES) == {"fused_arbiter", "deliberative_body", "scholastic_disputation"})
for _m in (_arb, _del, _sch):
    random.seed(1); _w, _ = _m.play(5, 4, LOG, LOG)
    ck("modes: regime resolves to a valid verdict", _w in ("a", "b", "draw"))
ck("modes: baseline court untouched (ProofBar, no rebuttal)",        isinstance(MOD.court_venue().win, ProofBar) and MOD.court_venue().allow_rebuttal is False)
ck("modes: baseline assembly untouched (TallyAtClose, no rebuttal)", isinstance(MOD.assembly_venue().win, TallyAtClose) and MOD.assembly_venue().allow_rebuttal is False)
_dsplit = False
for s in range(300):
    random.seed(s)
    _mm = MOD.deliberative_body_mode(panel_size=7, noise=1.4)
    _bt = Bout(Contestant(5), Contestant(5), _mm.venue, _mm.adj, record=True)
    _ww, _wy = _bt.resolve(LOG, LOG)
    if NAR.summarize(_bt.log, _ww, _wy).shape == "SPLIT_DECISION": _dsplit = True; break
ck("modes: deliberative_body can yield a verdict that crosses the room", _dsplit)

# == σ-LEVERAGE ENGINE (regression guards for the two patches) ==
from primitives import Leverage
from engine import effective_ob as _eff_ob, sigma_N as _sN
_fac1_lev = Leverage.net(1, on_ground=True)
_fac1_ob  = max(1.0, _eff_ob(2.0, _fac1_lev, Pool.size(1)))
_fac2_ob  = max(1.0, _eff_ob(2.0, Leverage.net(2, on_ground=True), Pool.size(2)))
ck("sigma-leverage: READING_COEFF=1/6 gives lev=0 at fac=1 on-ground (no precision drift)", abs(_fac1_lev) < 1e-9)
ck("sigma-leverage: fac=1 ob is exactly 2.0 (no round() cliff)",                            abs(_fac1_ob - 2.0) < 1e-9)
ck("sigma-leverage: ob is a float, not int",                                                 isinstance(_fac1_ob, float))
ck("sigma-leverage: net=2 at fac=1 is SUCCESS, not partial",                                degree(2, _fac1_ob) == 2)
ck("sigma-leverage: net=1 at fac=2 is PARTIAL (float ob < 2 allows fractional threshold)",  degree(1, _fac2_ob) == 1)
ck("sigma-leverage: net=2 at fac=2 is SUCCESS (not partial)",                               degree(2, _fac2_ob) == 2)
ck("sigma-leverage: fac=7 on-ground ob hits the 1.0 floor",                                 max(1.0, _eff_ob(2.0, Leverage.net(7, True), Pool.size(7))) == 1.0)
ck("sigma-leverage: fac=7 off-ground ob also hits 1.0 (expert immune to ground penalty)",   max(1.0, _eff_ob(2.0, Leverage.net(7, False), Pool.size(7))) == 1.0)

print("== validation + scaffolds ==")
def bad(v): return Move("garbage")
try: M_disp.play(4,4,bad,LOG); ck("validation raises", False)
except ValueError: ck("validation raises", True)
try: DyadicMode().play(); ck("scaffold raises", False)
except NotImplementedError: ck("scaffold raises", True)

print(f"\nRESULT: {P} passed, {Fc} failed")
sys.exit(1 if Fc else 0)   # audit: CI can gate (was exit 0 on failure)
