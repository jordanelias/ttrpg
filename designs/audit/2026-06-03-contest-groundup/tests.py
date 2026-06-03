"""tests.py — unit (per module) + integration (per mode). Run: python3 tests.py"""
from math import isclose
import engine as E
from primitives import Stasis, Appeal, Standing, Reserve, SelfGating, Leverage, Merits, DefeatConditions
from modes import ContestedMode, DyadicMode
from policy import honest_advocate, fallback_ladder, off_ground_chancer, overreacher, staller

P = F = 0
def ck(name, cond):
    global P, F
    if cond: P += 1
    else: F += 1; print("  FAIL:", name)

print("== engine ==")
ck("sigma_N=0.8√pool", isclose(E.sigma_N(16), 3.2))
ck("eff_sigma→±M_MAX", E.eff_sigma(50) <= 1.5 + 1e-9 and E.eff_sigma(50) > 1.49)
ck("effective_ob floored ≥1", E.effective_ob(2, 5, 16) == E.OB_MIN)
ck("levels 0.25/0.5/0.75/1.0", [E.level(x) for x in("minor","moderate","strong","major")]==[.25,.5,.75,1.])
ck("degree bands", (E.degree(0,3),E.degree(2,3),E.degree(3,3),E.degree(6,3))==(0,1,2,3))
ck("p_success monotone in δσ", E.p_success(11,2,0.0) < E.p_success(11,2,0.6))

print("== Stasis ==")
ck("relevant on live ground", Stasis.relevant("fact","fact") and not Stasis.relevant("fact","quality"))
ck("ladder order fact<def<qual<juris", Stasis.stronger_than("quality","fact") and not Stasis.stronger_than("fact","quality"))

print("== Appeal / Standing / Reserve ==")
ck("three proofs", Appeal.ALL == ("ethos","pathos","logos"))
s = Standing(5.0); s.build(2); ck("standing builds capped", s.v == min(10, 5+0.8*2))
s = Standing(1.0); s.strip(3); ck("standing strips floored", s.v == max(0, 1-0.8*3))
ck("standing dsigma sign", Standing(8).dsigma() > 0 > Standing(2).dsigma())
r = Reserve(12); ck("reserve can/spend", r.can("advance") and (r.spend("advance") or r.cur==9))
r = Reserve(2); ck("reserve exhausts (can't afford hard)", not r.can("hard"))
r = Reserve(12); r.spend("hard"); r.spend("hard"); r.regroup(); ck("regroup restores capped", r.cur == min(12, 12-5-5+4))

print("== SelfGating ==")
ck("hard unlicensed vs equal/learned-fair", not SelfGating.hard_device_licensed(5,5,True,False))
ck("hard licensed vs weaker + ignorant", SelfGating.hard_device_licensed(7,3,False,False))
ck("hard licensed vs weaker + hostile", SelfGating.hard_device_licensed(7,3,True,True))

print("== Leverage / Merits ==")
lv = Leverage()
ck("on-ground adds moderate", isclose(lv.net(4,0,True), E.level("moderate")))
ck("faculty term (f−4)·coeff", isclose(lv.net(6,0,False), (6-4)*0.167))
m = Merits(4.0); m.advance("a",2); ck("merits accumulate", m.a == 0.9*2 and m.leader() is None)
m.advance("a",3); ck("merits leader at threshold", m.leader()=="a")

print("== DefeatConditions (each fault clinches the right side) ==")
base = lambda **k: {"a":{"evasion":0,"yields":0,"contradicted":False,"barred":False},
                    "b":{"evasion":0,"yields":0,"contradicted":False,"barred":False}}
st = base(); st["b"]["barred"]=True;        ck("barred → that side loses", DefeatConditions.check(st)=="b")
st = base(); st["a"]["contradicted"]=True;  ck("self-contradiction → loses", DefeatConditions.check(st)=="a")
st = base(); st["b"]["evasion"]=2;          ck("evasion strikes → loses", DefeatConditions.check(st)=="b")
st = base(); st["a"]["yields"]=2;           ck("silence (yields) → loses", DefeatConditions.check(st)=="a")
ck("clean state → no clinch", DefeatConditions.check(base()) is None)

print("== integration: ContestedMode (clinch paths are deterministic) ==")
for flavor in ("forensic","deliberative"):
    M = ContestedMode(flavor)
    w,why = M.play(4,4, honest_advocate, overreacher)
    ck(f"{flavor}: honest beats overreacher (barred-device clinch)", w=="a" and why=="clinch:barred-device")
    w,why = M.play(4,4, honest_advocate, staller)
    ck(f"{flavor}: honest beats staller", w=="a")
    w,why = M.play(4,4, honest_advocate, off_ground_chancer)
    ck(f"{flavor}: honest beats off-ground", w=="a")
# clean vs clean never clinches
M = ContestedMode("forensic")
clinches = sum(1 for _ in range(400) if M.play(4,4, honest_advocate, honest_advocate)[1].startswith("clinch"))
ck("honest vs honest never clinches (clean play incurs no fault)", clinches == 0)
# fallback ladder may legitimately shift ground without self-contradiction
shift_contra = sum(1 for _ in range(200)
                   if M.play(3,5, fallback_ladder, honest_advocate)[1]=="clinch:self-contradiction")
ck("legit fallback shift ≠ self-contradiction", shift_contra == 0)

print("== scaffolds are honest (not faked) ==")
try: DyadicMode().play(); ck("dyadic scaffold raises", False)
except NotImplementedError: ck("dyadic scaffold raises", True)

print(f"\nRESULT: {P} passed, {F} failed")
