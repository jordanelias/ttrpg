"""tests.py — unit (per module) + wrapper-invariant + integration. Run: python3 tests.py"""
from math import isclose
import engine as E
import contract as K
from contract import A, B, other, Move, FaultState, Adjudicator
from primitives import Stasis, Appeal, Standing, Reserve, Pool, SelfGating, Leverage, Room, Merits, DefeatConditions
from modes import ContestedMode, DyadicMode
from policy import honest_advocate as H, tactician as TAC, pure_ethos as PE, fallback_ladder as FB, off_ground_chancer as OG, overreacher as OV, staller as ST
from collections import Counter

P = Fc = 0
def ck(n, c):
    global P, Fc
    if c: P += 1
    else: Fc += 1; print("  FAIL:", n)
def rates(fa, fb, pa, pb, N=2500, **cfg):
    M = ContestedMode("forensic", **cfg); w = Counter()
    for _ in range(N): w[M.play(fa, fb, pa, pb)[0]] += 1
    return {k: v / N for k, v in w.items()}

print("== engine ==")
ck("sigma_N", isclose(E.sigma_N(16), 3.2))
ck("eff_sigma→M_MAX", E.eff_sigma(50) <= 1.5 + 1e-9 and E.eff_sigma(50) > 1.49)
ck("effective_ob floor", E.effective_ob(2, 5, 16) == E.OB_MIN)
ck("degree bands", (E.degree(0,3), E.degree(2,3), E.degree(3,3), E.degree(6,3)) == (0,1,2,3))
ck("p_success monotone", E.p_success(11,2,0.0) < E.p_success(11,2,0.6))

print("== contract ==")
ck("side identity + other()", A=="a" and B=="b" and other(A)==B and other(B)==A)
ck("FaultState defaults clean", FaultState() == FaultState(0,0,False,False))
ck("Move optional appeal/ground", Move("support").appeal is None and Move("support").ground is None)

print("== primitives ==")
ck("Stasis.is_ground/ladder", Stasis.is_ground("fact") and not Stasis.is_ground("x") and Stasis.stronger_than("quality","fact"))
ck("Appeal.ALL", Appeal.ALL == ("ethos","pathos","logos"))
s=Standing(5.0); s.build(2); ck("Standing build cap", s.v==min(10,5+0.8*2))
s=Standing(1.0); s.strip(3); ck("Standing strip floor", s.v==max(0,1-0.8*3))
ck("Standing dsigma sign", Standing(8).dsigma()>0>Standing(2).dsigma())
r=Reserve(12); r.spend("hard"); ck("Reserve spend", r.cur==7 and not Reserve(2).can("hard"))
ck("Pool floor 5 + faculty term", Pool.size(-9)==5 and Pool.size(4)==11)
ck("SelfGating: hard gated, others licit", (not SelfGating.licit("hard",5,5,True,False))
   and SelfGating.licit("hard",7,3,False,False) and SelfGating.licit("advance",5,5,True,False))
ck("Leverage static + room/onground", isclose(Leverage.net(4,0,True,0.0), E.level("moderate"))
   and Leverage.net(4,0,True,1.0) > Leverage.net(4,0,True,0.0))
rm=Room(); rm.build(A,3); ck("Room builds, capped, dsigma>0", rm.dsigma(A)>0 and rm.r[A]<=Room.CAP)
m=Merits(4.0); m.advance(A,2); ck("Merits dict-keyed, leader at T", m.leader() is None and (m.advance(A,3) or m.leader()==A))
fa=FaultState(); fb=FaultState(); fb.barred=True
ck("DefeatConditions returns (side,reason)", DefeatConditions.check({A:fa,B:fb})==(B,"barred-device"))
fa2=FaultState(evasion=2); ck("evasion clinch", DefeatConditions.check({A:fa2,B:FaultState()})==(A,"evasion"))
ck("clean → None", DefeatConditions.check({A:FaultState(),B:FaultState()}) is None)

print("== wrapper invariants ==")
w = rates(4,4,H,H,N=4000)
ck(f"SYMMETRY: identical contestants ~50/50 (a {w.get('a',0):.2f} b {w.get('b',0):.2f})",
   abs(w.get('a',0)-w.get('b',0)) < 0.06)
w = rates(4,4,H,PE,N=2000)   # pure-ethos never advances the verdict → loses to logos
ck(f"APPEALS MATTER: logos beats pure-ethos (a {w.get('a',0):.2f})", w.get('a',0) > 0.9)
def bad(v): return Move("garbage")
try: ContestedMode("forensic").play(4,4,bad,H); ck("VALIDATION: bad kind raises", False)
except ValueError: ck("VALIDATION: bad kind raises", True)

print("== defeat-condition integration (deterministic clinches) ==")
for flavor in ("forensic","deliberative"):
    M=ContestedMode(flavor)
    w,why=M.play(4,4,H,OV); ck(f"{flavor}: honest beats overreacher (barred)", w=="a" and why=="clinch:barred-device")
    w,why=M.play(4,4,H,ST); ck(f"{flavor}: honest beats staller", w=="a")
    w,why=M.play(4,4,H,OG); ck(f"{flavor}: honest beats off-ground", w=="a")
M=ContestedMode("forensic")
ck("clean v clean never clinches", sum(1 for _ in range(400) if M.play(4,4,H,H)[1].startswith("clinch"))==0)
ck("legit fallback shift ≠ self-contradiction",
   sum(1 for _ in range(200) if M.play(3,5,FB,H)[1]=="clinch:self-contradiction")==0)

print("== scaffold honesty ==")
try: DyadicMode().play(); ck("scaffold raises", False)
except NotImplementedError: ck("scaffold raises", True)

print(f"\nRESULT: {P} passed, {Fc} failed")
