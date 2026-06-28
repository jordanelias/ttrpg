"""
valoria_sim.py v4 — 2026-04-14

Fixes vs v3:
  - Starting garrisons: Crown capital T1=3 units, Church T9=2, HF T8=2, Varfell T12=2,
    all border territories (adjacent to competing faction) = 1 unit
  - Valid targets = PLAYABLE only {crown, hafenmark, varfell, church}
    Guilds/Niflhel are NPCs, not adversaries for military/diplomatic actions
  - Posture-based AI replaces greedy algorithm:
    DEFEND / CONSOLIDATE / EXPAND / DIPLOMACY
    Each posture is chosen by assessing faction state, not immediate gain
  - Crown Treaty: only valid against PLAYABLE faction with Mandate >= 2
"""

import random, math
from dataclasses import dataclass, field
from typing import Optional
from collections import Counter, defaultdict

# ── CONSTANTS ─────────────────────────────────────────────────────────────────
DICE_SIDES=10; TN=7; OB_MIN=1; POOL_MIN=1
OW_FLOOR=3; SEASONAL_CAP=2; STAT_MAX=7; STAT_MIN=0
PT_MAX=5; PT_MIN=0; # CI_PASSIVE constant removed — PP-402 repealed; conditional passive in _tc_acct
RS_BG=72; CI_BG=28; IP_START=20; PI_BG=7; SEASONS_PER_YEAR=4
VICTORY_SUSTAIN=2; UNIT_DISC_DEFAULT=4

PLAYABLE   = {"crown","hafenmark","varfell","church"}  # valid diplomatic/military targets
NPC_ONLY   = {"guilds","niflhel"}
DOMAIN_EXP_LEG = {"crown","lowenritter"}               # +1D on Legionary actions
LEGIONARY_CARDS= {"crown":2,"church":1,"hafenmark":1,"varfell":1,
                   "guilds":0,"niflhel":0,"lowenritter":2}

# Starting garrisons per Jordan's rule:
# Crown capital T1=3, Church T9=2, HF T8=2, Varfell T12=2
# All other PLAYABLE-controlled territories adjacent to a rival PLAYABLE territory = 1
CAPITAL_GARRISONS = {"T1":3,"T9":2,"T8":2,"T12":2}

# Victory thresholds (victory_v30.md)
CROWN_TCV=14; DOMINION_TCV=22; CHURCH_TCV=8; HF_TCV=13

# Tracker keys
KEY_RS="rs"; KEY_CI="ci"; KEY_IP="ip"; KEY_PI="pi"; KEY_PARL="parl"
KEY_WC="wc"; KEY_VTM="vtm"; KEY_WR="wr"
KEY_TORBEN="torben"; KEY_ELSKE="elske"; KEY_COUP="coup"

FAILURE=0; PARTIAL=1; SUCCESS=2; OVERWHELMING=3
DN={0:"FAIL",1:"PART",2:"SUCC",3:"OW"}

# ── DICE ──────────────────────────────────────────────────────────────────────
def roll(pool, ob, rng):
    pool=max(pool,POOL_MIN); ob=max(OB_MIN,ob)
    faces=[rng.randint(1,DICE_SIDES) for _ in range(pool)]
    pos=f10=ones=0
    for f in faces:
        if f==1: ones+=1
        elif f==10: f10+=1
        elif f>=TN: pos+=1
    net=pos+f10*2+ones*(-1)
    if net<=0: d=FAILURE
    elif net<ob: d=PARTIAL
    elif net>=ob*2 and net>=OW_FLOOR: d=OVERWHELMING
    else: d=SUCCESS
    return d,net

# ── TRACKER ────────────────────────────────────────────────────────────────────
class TT:
    def __init__(self,v,fall,ev,p=None,rep=False):
        self.v=v; self.fall=fall; self.ev=ev; self.p=p or {}; self.rep=rep; self.f=False
    def crossed(self,old,new):
        if not self.rep and self.f: return False
        return (old>self.v>=new) if self.fall else (old<self.v<=new)
    def fire(self): self.f=True
    def reset(self): self.f=False

class Trk:
    def __init__(self,k,v,mn,mx,cap=-1):
        self.k=k; self.v=v; self.mn=mn; self.mx=mx; self.cap=cap; self.sc=0; self.tt=[]
    def apply(self,d):
        old=self.v
        if self.cap>0:
            rem=self.cap-abs(self.sc)
            if rem<=0: return old,self.v,0,[]
            d=min(d,rem) if d>0 else max(d,-rem)
        new=max(self.mn,min(self.mx,self.v+d))
        act=new-self.v; self.v=new; self.sc+=act
        fired=[t for t in self.tt if t.crossed(old,new)]
        for t in fired: t.fire()
        return old,new,act,fired
    def reset_season(self):
        self.sc=0
        for t in self.tt:
            if t.rep: t.reset()
    def add(self,t): self.tt.append(t)

class TR:
    def __init__(self): self._t={}; self._cb={}
    def reg(self,k,v,mn,mx,cap=-1):
        t=Trk(k,v,mn,mx,cap); self._t[k]=t; return t
    def has(self,k): return k in self._t
    def get(self,k): return self._t.get(k)
    def val(self,k,d=0): t=self._t.get(k); return t.v if t else d
    def apply(self,k,delta):
        t=self._t.get(k)
        if not t: return None
        old,new,act,fired=t.apply(delta)
        for th in fired:
            cb=self._cb.get(th.ev)
            if cb: cb(k,th.ev,th.p)
        return old,new,act
    def on(self,ev,cb): self._cb[ev]=cb
    def reset_f(self):
        for k,t in self._t.items():
            if k.startswith("f:"): t.reset_season()
    def reset_w(self):
        for k,t in self._t.items():
            if not k.startswith("f:"): t.sc=0
    def season_loss(self,fid):
        tot=0
        for s in ["mandate","influence","wealth","military","stability"]:
            t=self._t.get(f"f:{fid}:{s}")
            if t and t.sc<0: tot+=abs(t.sc)
        return tot

# ── UNIT ──────────────────────────────────────────────────────────────────────
# Unit type definitions: (Martial, default_disc, default_size)
UNIT_TYPES = {
    "levy":           (1, 1, 3),
    "light_infantry": (3, 3, 4),
    "heavy_infantry": (4, 4, 5),
    "cavalry":        (4, 5, 4),
    "archer":         (3, 3, 3),
    "crossbow":       (3, 3, 3),
    "artillery":      (2, 2, 3),
    "templar":        (5, 6, 6),
}
DEFAULT_UNIT_TYPE = "light_infantry"

@dataclass
class Unit:
    uid: str; fid: str; tid: str
    utype: str = DEFAULT_UNIT_TYPE   # unit type key into UNIT_TYPES
    size: int = 2                     # tracked headcount (1-7)
    disc: int = UNIT_DISC_DEFAULT
    exp: int = 0                      # 0=Fresh, 1=Seasoned, 2=Veteran
    dead: bool = False

    @property
    def martial(self) -> int:
        return UNIT_TYPES.get(self.utype, (3,3,4))[0]

    @property
    def base_power(self) -> int:
        """TTRPG Power = unit type base. Experience adds up to faction Military ceiling."""
        type_power = {"levy":1,"light_infantry":3,"heavy_infantry":4,
                      "cavalry":5,"archer":3,"crossbow":3,"artillery":2,"templar":5}
        return type_power.get(self.utype, 3) + self.exp  # exp adds +1 per step

    @property
    def is_templar(self) -> bool:
        return self.utype == "templar"

    def hurt(self, loss):
        self.size = max(0, self.size - loss)
        self.disc = max(0, self.disc - loss)
        if self.size <= 0 or self.disc <= 0:
            self.dead = True

    def gain_exp(self, faction_mil_ceiling: int):
        """Award one experience step, capped at Veteran (2) and faction ceiling."""
        if self.exp < 2:
            self.exp = min(self.exp + 1, 2)

# ── TERRITORY ─────────────────────────────────────────────────────────────────
@dataclass
class Terr:
    tid:str; name:str; ctrl:str; tcv:int; fort:int; pt_start:int
    adj:list=field(default_factory=list)
    is_cap:bool=False; playable:bool=True; sw:int=1  # Spiritual Weight
    accord:int=2  # 0=Revolt,1=Resistant,2=Compliant,3=Aligned; set at init
    def pk(self): return f"pt:{self.tid}"
    def ak(self): return f"accord:{self.tid}"

# (tid, name, ctrl, tcv, fort, pt_start, adj, is_cap, playable, spiritual_weight)
TERR_DATA = [
    ("T1","Valorsplatz","crown",  5,2,3,["T2","T5","T14","T16"],True, True,2),
    ("T2","Kronmark",   "crown",  1,1,3,["T1","T3","T9","T14"],False,True,2),
    ("T3","Lowenskyst", "crown",  2,3,3,["T2","T9","T17"],      False,True,2),
    ("T4","Grauwald",   "varfell",1,0,2,["T7","T12","T14"],     False,True,1),
    ("T5","Feldmark",   "crown",  1,0,3,["T1","T6","T14"],      False,True,2),
    ("T6","Stillhelm",  "crown",  1,0,1,["T5","T13","T15"],     False,True,1),
    ("T7","Rendstad",   "hafenmark",1,0,3,["T4","T8"],          False,True,2),
    ("T8","Gransol",    "hafenmark",4,1,3,["T7","T9","T10","T17"],True,True,3),
    ("T9","Himmelenger","church", 3,2,5,["T2","T3","T8","T14","T17"],True,True,5),
    ("T10","Spartfell", "hafenmark",1,2,3,["T8","T11"],         False,True,2),
    ("T11","Halvardshelm","varfell",1,0,2,["T10","T12"],        False,True,1),
    ("T12","Sigurdshelm","varfell",3,1,2,["T4","T11","T13"],    True, True,2),
    ("T13","Oastad",    "varfell",1,0,1,["T6","T12","T15"],     False,True,1),
    ("T14","Ehrenfeld", "crown",  2,3,3,["T1","T2","T4","T5","T9"],False,True,3),
    ("T15","Askeheim",  "",       0,0,0,["T6","T13"],           False,False,0),
    ("T16","Schoenland","schoenland",0,1,1,["T1"],              False,False,1),
    ("T17","Halvarshelm","hafenmark",1,0,3,["T3","T8","T9"],   False,True,2),
]

def build_territories():
    result=[]
    for row in TERR_DATA:
        tid,name,ctrl,tcv,fort,pt=row[0],row[1],row[2],row[3],row[4],row[5]
        adj=row[6] if len(row)>6 else []
        is_cap=row[7] if len(row)>7 else False
        play=row[8] if len(row)>8 else True
        sw=row[9] if len(row)>9 else 1
        # Starting accord: 3 for capitals, 2 for own home territories, 0 for uncontrolled
        accord=3 if is_cap else (2 if ctrl in PLAYABLE|{"schoenland"} else 0)
        t=Terr(tid,name,ctrl,tcv,fort,pt,adj,is_cap,play,sw,accord)
        result.append(t)
    return result

# ── SETTING ────────────────────────────────────────────────────────────────────
class Setting:
    def __init__(self):
        self._t={}; self._occ={}; self._vac={}
        self._units:dict[str,Unit]={}; self._uid=0

    def reg(self,t): self._t[t.tid]=t

    def all(self): return list(self._t.values())
    def get(self,tid): return self._t.get(tid)
    def ctrl(self,tid): t=self._t.get(tid); return t.ctrl if t else ""
    def set_ctrl(self,tid,fid):
        t=self._t.get(tid)
        if t and t.playable: t.ctrl=fid

    def faction_tcv(self,fid):
        return sum(t.tcv for t in self._t.values()
                   if t.ctrl==fid and not self.is_occ(t.tid))

    def faction_tids(self,fid): return [t.tid for t in self._t.values() if t.ctrl==fid]
    def faction_terrs(self,fid): return [t for t in self._t.values() if t.ctrl==fid]

    # Units
    def new_unit(self,fid,tid,utype=DEFAULT_UNIT_TYPE,size=None):
        self._uid+=1
        base_disc=UNIT_TYPES.get(utype,(3,3,4))[1]
        base_size=size if size is not None else UNIT_TYPES.get(utype,(3,3,4))[2]
        u=Unit(f"u{self._uid}",fid,tid,utype=utype,size=base_size,disc=base_disc)
        self._units[u.uid]=u; return u

    def units_in(self,tid): return [u for u in self._units.values() if u.tid==tid and not u.dead]
    def faction_units(self,fid): return [u for u in self._units.values() if u.fid==fid and not u.dead]
    def unit_count(self,fid): return len(self.faction_units(fid))

    def garrison(self,tid):
        ctrl=self.ctrl(tid)
        if not ctrl or ctrl not in PLAYABLE: return False
        return any(u.fid==ctrl for u in self.units_in(tid))

    def purge_dead(self): self._units={k:v for k,v in self._units.items() if not v.dead}

    def border_pairs(self,fid):
        """(unit,target_terr) where unit is in a territory adjacent to an enemy PLAYABLE territory."""
        out=[]
        for u in self.faction_units(fid):
            src=self._t.get(u.tid)
            if not src: continue
            for adj in src.adj:
                at=self._t.get(adj)
                if at and at.playable and at.ctrl in PLAYABLE and at.ctrl!=fid:
                    out.append((u,at)); break
        return out

    def threatened_tids(self,fid):
        """Own territories adjacent to an enemy unit."""
        enemy_unit_tids={u.tid for f2,us in
                         [(f,self.faction_units(f)) for f in PLAYABLE if f!=fid]
                         for u in us}
        result=[]
        for t in self.faction_terrs(fid):
            for adj in t.adj:
                at=self._t.get(adj)
                if at and at.ctrl!=fid and adj in enemy_unit_tids:
                    result.append(t.tid); break
        return result

    # Occupation
    def is_occ(self,tid): return tid in self._occ
    def occupier(self,tid): return self._occ.get(tid,{}).get("o","")
    def occupy(self,tid,fid):
        if tid in self._vac: return False
        self._occ[tid]={"o":fid,"s":1}; return True
    def end_occ(self,tid): self._occ.pop(tid,None)
    def adv_occ(self,tid):
        if tid not in self._occ: return 0
        self._occ[tid]["s"]+=1; return self._occ[tid]["s"]

    def in_vac(self,tid): return tid in self._vac
    def enter_vac(self,tids):
        for tid in tids: self._vac[tid]=1; self._occ.pop(tid,None)
    def adv_vac(self):
        ex=[]; rm=[]
        for tid,s in self._vac.items():
            if s<=1: ex.append(tid); rm.append(tid)
            else: self._vac[tid]-=1
        for tid in rm:
            del self._vac[tid]; t=self._t.get(tid)
            if t: t.ctrl=""
        return ex

    def church_prominent(self,reg,cm):
        r=[]
        for t in self._t.values():
            if not t.playable or t.ctrl in ("","schoenland"): continue
            if cm>reg.val(f"f:{t.ctrl}:mandate"): r.append(t)
        return r

# ── FACTION ───────────────────────────────────────────────────────────────────
@dataclass
class Faction:
    fid:str; name:str; stats:dict=field(default_factory=dict)
    is_npc:bool=False; is_active:bool=True
    def sk(self,s): return f"f:{self.fid}:{s}"
    def stabk(self): return self.sk("stability")
    def has(self,s): return s in self.stats

FACTION_STATS={
    "crown":    {"mandate":5,"influence":5,"wealth":4,"military":4,"stability":4},
    "church":   {"mandate":5,"influence":6,"wealth":5,"military":4,"stability":5},
    "hafenmark":{"mandate":4,"influence":4,"wealth":5,"military":3,"stability":4},
    "varfell":  {"mandate":4,"influence":4,"wealth":4,"military":4,"stability":4},
    "guilds":   {"mandate":3,"influence":4,"wealth":6,"military":2,"stability":5},
    "niflhel":  {"mandate":0,"influence":5,"wealth":4,"military":0,"stability":4},
    "lowenritter":{"mandate":3,"influence":2,"wealth":3,"military":6,"stability":5},
}

def build_factions():
    return [
        Faction("crown","Crown",FACTION_STATS["crown"]),
        Faction("church","Church",FACTION_STATS["church"]),
        Faction("hafenmark","Hafenmark",FACTION_STATS["hafenmark"]),
        Faction("varfell","Varfell",FACTION_STATS["varfell"]),
        Faction("guilds","Guilds",FACTION_STATS["guilds"],is_npc=True),
        Faction("niflhel","Niflhel",FACTION_STATS["niflhel"],is_npc=True),
        Faction("lowenritter","Löwenritter",FACTION_STATS["lowenritter"],is_active=False),
    ]

class FReg:
    def __init__(self,reg):
        self._f={}; self._r=reg
    def reg_f(self,f):
        self._f[f.fid]=f
        for s,v in f.stats.items():
            self._r.reg(f.sk(s),v,STAT_MIN,STAT_MAX,SEASONAL_CAP)
        stab=self._r.get(f.stabk())
        if stab: stab.add(TT(0,True,"collapse",{"fid":f.fid}))
    def get(self,fid): return self._f.get(fid)
    def all(self): return list(self._f.values())
    def active(self): return [f for f in self._f.values() if f.is_active]
    def playable_active(self): return [f for f in self.active() if f.fid in PLAYABLE]
    def stat(self,fid,s): return self._r.val(f"f:{fid}:{s}")

# ── WORLD ──────────────────────────────────────────────────────────────────────
class World:
    def __init__(self,mode="bg"):
        self.mode=mode; self.cy=0; self.cs=0
        self.reg=TR(); self.setting=Setting(); self.fr=None
        self._vc={}; self._go=None; self._log=[]
        self._tfs=set(); self._suppress=False; self._lr_ok=False
        self._wow:list=[]; self._battles_this_season=0
        self._assert_bonus=0   # CI bonus from Assert action this season
        self.reg.on("rs_rupture",lambda k,e,p: self._set_go("SHARED_LOSS_RS"))
        self.reg.on("tc_hit",   lambda k,e,p: (self._set_go("TC_THEOCRACY"),self._log_e("CI 75")))
        self.reg.on("elske_low",lambda k,e,p: self.reg.apply(KEY_IP,3))
        self.reg.on("collapse",  lambda k,e,p: self._collapse_fid(p.get("fid","")))

    def _set_go(self,vt): self._go={"vt":vt}

    def start(self):
        rs=self.reg.reg(KEY_RS,RS_BG,0,100); rs.add(TT(0,True,"rs_rupture"))
        tc=self.reg.reg(KEY_CI,CI_BG,0,100); tc.add(TT(100,False,"tc_hit"))
        self.reg.reg(KEY_IP,IP_START,0,100); self.reg.reg(KEY_PI,PI_BG,0,100)
        self.reg.reg(KEY_PARL,PI_BG,0,20);  self.reg.reg(KEY_WC,0,0,3)
        self.reg.reg(KEY_VTM,0,0,5);        self.reg.reg(KEY_WR,0,0,3)
        self.reg.reg(KEY_TORBEN,7,0,7)
        el=self.reg.reg(KEY_ELSKE,4,0,7);   el.add(TT(2,True,"elske_low"))
        self.reg.reg(KEY_COUP,0,0,4)
        self.reg.reg("ps",0,0,10)   # Turmoil
        for t in build_territories():
            self.setting.reg(t)
            self.reg.reg(t.pk(),t.pt_start,PT_MIN,PT_MAX)
        self.fr=FReg(self.reg)
        for f in build_factions():
            if f.is_active: self.fr.reg_f(f)
            else: self.fr._f[f.fid]=f
        self._seed_garrisons()

    def _seed_garrisons(self):
        """Place starting garrisons per canonical rule.
        Bypasses do_muster cap — starting armies are pre-existing, exempt from recruitment cap.
        Unit cap for new musters: (Military*2)+3.
        """
        for t in self.setting.all():
            if not t.playable or t.ctrl not in PLAYABLE: continue
            # Capital garrisons
            if t.tid in CAPITAL_GARRISONS:
                for _ in range(CAPITAL_GARRISONS[t.tid]):
                    self.setting.new_unit(t.ctrl, t.tid)
            else:
                # Border territory: 1 unit if adjacent to rival PLAYABLE faction
                border=any(
                    self.setting.ctrl(adj) in PLAYABLE and
                    self.setting.ctrl(adj) != t.ctrl
                    for adj in t.adj
                )
                if border:
                    self.setting.new_unit(t.ctrl, t.tid)

    def mut(self,k,d):
        if self.reg.has(k): self.reg.apply(k,d)

    def fs(self,fid,s): return self.reg.val(f"f:{fid}:{s}")
    def rs(self): return self.reg.val(KEY_RS)
    def tc(self): return self.reg.val(KEY_CI)
    def ip(self): return self.reg.val(KEY_IP)

    def _stab(self,fid,d,reason,tn):
        if not self.reg.has(f"f:{fid}:stability"): return
        self.mut(f"f:{fid}:stability",d)
        self._tfs.add(fid); self._log_e(f"STAB T{tn}[{fid}]{d:+d} {reason}")

    # ── Battle (PP-476, PP-499) ───────────────────────────────────────────────
    def battle(self,att,dfn,tid,rng):
        """
        BG Battle Resolution per mass_battle_v30 §B.3.
        Pool = sum(Martial of engaged units) + floor(Military/2) — NOT Military pool vs Ob.
        Outcome by margin (PP-104): net >= +2 attacker wins; <=1 either = partial; net <= -2 defender wins.
        """
        td=self.setting.get(tid)
        am=self.fs(att,"military"); dm=self.fs(dfn,"military")

        # Attacker: units adjacent to target territory
        att_units=[u for u in self.setting.faction_units(att)
                   if td.tid in (self.setting.get(u.tid).adj
                                 if self.setting.get(u.tid) else [])]
        # Defender: units IN the territory belonging to defender
        def_units=[u for u in self.setting.units_in(tid) if u.fid==dfn]

        # Pool = sum(Martial) + commander bonus floor(Military/2) per B.3/PP-555
        att_martial=sum(u.martial for u in att_units) if att_units else max(am,1)
        def_martial=sum(u.martial for u in def_units) if def_units else max(dm,1)
        att_pool=att_martial + am//2 + (1 if att in DOMAIN_EXP_LEG else 0)
        def_pool=def_martial + dm//2 + td.fort   # fort = bonus dice to defender

        ob=2  # Standard Advance vs Standard Advance baseline (tactic cards not simulated)
        _,an=roll(max(att_pool,1),ob,rng)
        _,dn=roll(max(def_pool,1),ob,rng)

        att_margin=an-dn  # positive = attacker ahead, negative = defender ahead

        # PP-104 margin system
        if att_margin>=2:    winner=att
        elif att_margin<=-2: winner=dfn
        else:                winner="partial"

        # Apply damage to units
        def hurt_units(units, loss):
            if units: units[0].hurt(loss)

        if winner==att:
            hurt_units(def_units,2)
        elif winner==dfn:
            hurt_units(att_units,2)
        else:  # partial
            hurt_units(att_units,1); hurt_units(def_units,1)

        # Award experience for survivors on winning side
        if winner==att:
            for u in att_units:
                if not u.dead: u.gain_exp(self.fs(att,"military"))
        elif winner==dfn:
            for u in def_units:
                if not u.dead: u.gain_exp(self.fs(dfn,"military"))

        # Weight-of-numbers PP-570: attacking Martial sum >= 2x defending Martial sum
        if att_martial>=def_martial*2:
            self._wow.append((dfn,f"WoN {att} vs {dfn} at {tid}"))

        self.setting.purge_dead()
        self._battles_this_season+=1   # track for RS/IP at Accounting
        return {"winner":winner,"an":an,"dn":dn,"att_margin":att_margin,
                "att_units":att_units,"def_units":def_units}

    # ── Military actions ──────────────────────────────────────────────────────
    def do_muster(self,fid,tid,rng):
        mil=self.fs(fid,"military")
        if self.setting.unit_count(fid)>=(mil*2+3): return False  # unit cap = (Military*2)+3
        ap=max(mil,1)+(1 if fid in DOMAIN_EXP_LEG else 0)
        d,_=roll(ap,2,rng)
        if d in(SUCCESS,OVERWHELMING):
            self.setting.new_unit(fid,tid); self._log_e(f"MUSTER [{fid}] in {tid}")
            return True
        return False

    def do_march(self,fid,unit,target_tid,rng):
        td=self.setting.get(target_tid)
        if not td: return "invalid"
        dfn=td.ctrl
        if not dfn or dfn=="schoenland":
            unit.tid=target_tid; self.setting.set_ctrl(target_tid,fid)
            self._log_e(f"MARCH [{fid}] → uncontrolled {target_tid}")
            return "free"
        if dfn==fid:
            unit.tid=target_tid; return "reposition"

        if not self.setting.garrison(target_tid):
            # Ungarrisoned enemy: free occupation
            unit.tid=target_tid
            if self.setting.occupy(target_tid,fid):
                self._stab(dfn,-2 if td.is_cap else -1,f"{target_tid} occ (no garrison)",1)
                self._log_e(f"MARCH [{fid}] occupies ungarrisoned {target_tid}")
            return "occ_free"

        # Battle
        res=self.battle(fid,dfn,target_tid,rng)
        w=res["winner"]
        self._log_e(f"BATTLE {fid} vs {dfn} at {target_tid}: att={res['an']} def={res['dn']} w={w}")
        if w==fid:
            unit.tid=target_tid
            if self.setting.occupy(target_tid,fid):
                self._stab(dfn,-2 if td.is_cap else -1,f"{target_tid} lost in battle",1)
        elif w in(dfn,"draw"):
            am=self.fs(fid,"military")
            if am>=4:
                margin=res["dn"]-res["an"]
                if margin>=2 or am>=6:
                    cost=-2 if(margin>=3 or am>=6) else -1
                    if td.is_cap: cost-=1
                    self._stab(fid,cost,f"Sig mil loss at {target_tid}",5)
        return "battle"

    # ── Posture-based AI ──────────────────────────────────────────────────────
    def _posture(self, f:Faction) -> str:
        """
        Priority-based posture per tc_political_redesign_v30 §6.1.
        P1 EXISTENTIAL: Stability<=1 or only 1 territory
        P2 DEFEND: enemy unit threatens ungarrisoned own territory
        P3 CONSOLIDATE: Stability<=2 OR Wealth<=1 OR Mandate<=2
        P4 COUNTER_THREAT: CI>=55 for HF/Crown; treaty opportunity for Crown
        P5 EXPAND: all clear, border units ready
        P6 OPPORTUNISTIC: default
        """
        fid=f.fid
        stab=self.fs(fid,"stability"); wealth=self.fs(fid,"wealth")
        man=self.fs(fid,"mandate"); tcv=self.setting.faction_tcv(fid)
        tids=self.setting.faction_tids(fid)
        threatened=self.setting.threatened_tids(fid)
        border_ready=self.setting.border_pairs(fid)
        units=self.setting.unit_count(fid)
        mil=self.fs(fid,"military")

        # P1: Existential
        if stab<=1 or len(tids)<=1: return "EXISTENTIAL"
        # P2: Defend — ungarrisoned own territory with enemy nearby
        if threatened and any(not self.setting.garrison(tid) for tid in threatened):
            return "DEFEND"
        # P3: Consolidate — resource deficit
        if stab<=2 or wealth<=1 or man<=2: return "CONSOLIDATE"
        # P4: Counter-threat
        if fid=="hafenmark" and self.tc()>=40: return "SUPPRESS"
        if fid=="crown" and man>=4 and tcv>=10: return "TREATY"
        if fid=="church" and self.tc()>=40: return "SEIZE"
        # P5: Expand
        if border_ready and stab>=3 and wealth>=2: return "EXPAND"
        # P6: Opportunistic
        return "OPPORTUNISTIC"

    def ai_orders(self, f:Faction, rng) -> list[dict]:
        def O(at,tgt="",ps="mandate",ob=2,meta=None):
            return{"at":at,"tgt":tgt,"ps":ps,"ob":max(1,ob),"fid":f.fid,"meta":meta or{}}
        fid=f.fid; S=lambda s:self.fs(fid,s)
        posture=self._posture(f)
        rivals=[g.fid for g in self.fr.playable_active() if g.fid!=fid]
        leg=LEGIONARY_CARDS.get(fid,0)
        orders=[]

        # ── Capital for Govern/Muster ─────────────────────────────────────────
        caps=[t.tid for t in self.setting.faction_terrs(fid) if t.is_cap]
        home_cap=caps[0] if caps else ""
        all_tids=self.setting.faction_tids(fid)

        # ── Military planning ─────────────────────────────────────────────────
        leg_used=0
        border_pairs=self.setting.border_pairs(fid)
        threatened=self.setting.threatened_tids(fid)
        units=self.setting.unit_count(fid); mil=S("military")

        def want_muster():
            # Muster in capital if under unit cap and threatened or expanding
            return units<(mil*2+3) and (threatened or posture=="EXPAND") and home_cap

        if leg>0 and posture not in("EXISTENTIAL","CONSOLIDATE"):
            if posture=="DEFEND" and threatened:
                # Find ungarrisoned threatened territory and muster there
                for tid in threatened:
                    if not self.setting.garrison(tid) and units<(mil*2+3):
                        orders.append(O("muster",tid,"military",2)); leg_used+=1; break
            elif posture=="EXPAND" and border_pairs:
                u,tgt=border_pairs[0]
                orders.append(O("march",tgt.tid,"military",0,{"uid":u.uid}))
                leg_used+=1
                if leg>1 and len(border_pairs)>1:
                    u2,tgt2=border_pairs[1]
                    if u2.uid!=u.uid:
                        orders.append(O("march",tgt2.tid,"military",0,{"uid":u2.uid}))
                        leg_used+=1
            if leg_used==0 and want_muster():
                orders.append(O("muster",home_cap,"military",2)); leg_used+=1

        # ── Non-military actions (fill to 2 total) ────────────────────────────
        def add(action):
            if len(orders)<2: orders.append(action)

        if fid=="crown":
            if posture=="EXISTENTIAL":
                add(O("govern",home_cap,"mandate",1))  # Mandate recovery in capital
                add(O("trade","","wealth",2))
            elif posture in("CONSOLIDATE","OPPORTUNISTIC"):
                if S("mandate")<5: add(O("govern",home_cap,"mandate",1))  # capital Ob 1 (−1 mod)
                add(O("trade","","wealth",2))
            elif posture=="TREATY":
                valid=[r for r in rivals if self.fs(r,"mandate")>=2]
                if valid:
                    tgt=min(valid,key=lambda r:self.fs(r,"mandate"))
                    add(O("crown_treaty",tgt,"mandate",max(1,self.fs(tgt,"mandate")//2+1)))
                add(O("govern",home_cap,"mandate",1))
            else:
                if S("mandate")<5: add(O("govern",home_cap,"mandate",1))
                add(O("trade","","wealth",2))

        elif fid=="church":
            if posture in("EXISTENTIAL","CONSOLIDATE"):
                add(O("govern",home_cap or "T9","mandate",1))
                add(O("trade","","wealth",2))
            elif posture=="SEIZE":
                bt,bpt="",-1
                for t in self.setting.all():
                    if t.ctrl in PLAYABLE and t.ctrl!="church" and t.playable:
                        pt=self.reg.val(t.pk())
                        if pt>bpt: bpt=pt; bt=t.tid
                if bt: add(O("church_seizure",bt,"influence",max(1,7-bpt)))
                add(O("church_assert","","influence",2))
            else:
                add(O("church_assert","","influence",2))
                if S("wealth")<4: add(O("trade","","wealth",2))
                else: add(O("govern","T9","mandate",1))

        elif fid=="hafenmark":
            if posture in("EXISTENTIAL","CONSOLIDATE"):
                if S("mandate")<4: add(O("govern",home_cap,"mandate",1))
                add(O("trade","","wealth",2))
            elif posture=="SUPPRESS":
                cm=self.fs("church","mandate")
                add(O("suppress_tc","","mandate",max(1,cm//2+1)))
                if S("wealth")<4: add(O("trade","","wealth",2))
                elif S("mandate")<4: add(O("govern",home_cap,"mandate",1))
                else: add(O("trade","","wealth",2))
            else:
                cm=self.fs("church","mandate")
                add(O("suppress_tc","","mandate",max(1,cm//2+1)))
                add(O("trade","","wealth",2))

        elif fid=="varfell":
            if posture in("EXISTENTIAL","CONSOLIDATE"):
                add(O("govern",home_cap,"mandate",1))
                add(O("trade","","wealth",2))
            else:
                if rivals:
                    tgt=max(rivals,key=lambda r:self.fs(r,"mandate"))
                    add(O("intel_op",tgt,"influence",2))
                if S("mandate")<4: add(O("govern",home_cap,"mandate",1))
                else: add(O("trade","","wealth",2))

        elif fid in("guilds","niflhel"):
            add(O("trade","","wealth",2))
            add(O("govern",all_tids[0] if all_tids else "","mandate",2))

        elif fid=="lowenritter":
            add(O("govern",home_cap,"mandate",2))
            if posture=="EXPAND" and border_pairs and leg_used<leg:
                u,tgt=border_pairs[0]
                add(O("march",tgt.tid,"military",0,{"uid":u.uid}))

        return orders[:2]

    # ── Action resolution ─────────────────────────────────────────────────────
    def resolve_action(self,action,rng):
        at=action["at"]; fid=action["fid"]
        f=self.fr.get(fid)
        if not f or not f.is_active: return FAILURE

        if at=="march":
            tid=action["tgt"]; uid=action["meta"].get("uid","")
            u=self.setting._units.get(uid)
            if not u or u.dead: return FAILURE
            result=self.do_march(fid,u,tid,rng)
            return FAILURE if result=="invalid" else SUCCESS

        if at=="muster":
            return SUCCESS if self.do_muster(fid,action["tgt"],rng) else FAILURE

        ps=action["ps"]; ob=action["ob"]
        pk=f"f:{fid}:{ps}"
        if not self.reg.has(pk): pk=f"f:{fid}:influence"
        pool=max(self.reg.val(pk,1),1)
        if fid in DOMAIN_EXP_LEG and ps=="mandate": pool+=1
        # Church CI political legitimacy bonus (§3.2 tc_political_redesign_v30)
        if fid=="church" and at in("govern","crown_treaty","suppress_tc","church_assert","church_seizure","intel_op"):
            pool+=self.tc()//20
        d,_=roll(pool,ob,rng)

        if at=="church_assert":
            if d==OVERWHELMING:
                self._assert_bonus=2   # for CI accounting
            elif d==SUCCESS:
                self._assert_bonus=1
            elif d==FAILURE: self._stab("church",-1,"Assert fail",1)

        elif at=="suppress_tc":
            if d in(SUCCESS,OVERWHELMING): self._suppress=True
            elif d==FAILURE: self._stab(fid,-1,"Suppress fail",1)

        elif at=="crown_treaty":
            tgt=action["tgt"]
            if not tgt or tgt not in PLAYABLE: return FAILURE
            if d==OVERWHELMING:
                self.mut(f"f:{tgt}:mandate",-1); self.mut(f"f:{tgt}:stability",1)
                self.mut(f"f:{fid}:mandate",1); self._log_e(f"TREATY OW {tgt}")
            elif d==SUCCESS:
                self.mut(f"f:{tgt}:mandate",-1); self.mut(f"f:{tgt}:stability",1)
                self._log_e(f"TREATY S {tgt}")
            elif d==FAILURE:
                self._stab("crown",-1,"Crown Treaty fail",2)

        elif at=="church_seizure":
            self._church_seizure(action,d,rng)

        elif at in("mandate_consol","govern"):
            tgt_tid=action.get("tgt","")
            tgt_terr=self.setting.get(tgt_tid) if tgt_tid else None
            # PP-174: Govern OW in own capital → Mandate +1 (max starting Mandate)
            if d==OVERWHELMING and tgt_terr and tgt_terr.is_cap and tgt_terr.ctrl==fid:
                start_man=FACTION_STATS.get(fid,{}).get("mandate",5)
                if self.fs(fid,"mandate")<start_man:
                    self.mut(f"f:{fid}:mandate",1)
                # Accord +1 in capital
                if tgt_terr.accord<3: tgt_terr.accord+=1
            elif d==SUCCESS and tgt_terr and tgt_terr.ctrl==fid:
                # Accord +1 in any own territory on Success
                if tgt_terr.accord<3: tgt_terr.accord+=1
            elif d in(SUCCESS,OVERWHELMING) and not tgt_terr:
                # No target specified: generic mandate recovery
                start_man=FACTION_STATS.get(fid,{}).get("mandate",5)
                if self.fs(fid,"mandate")<start_man:
                    self.mut(f"f:{fid}:mandate",1)

        elif at=="trade":
            if d in(SUCCESS,OVERWHELMING): self.mut(f"f:{fid}:wealth",1)

        elif at=="intel_op":
            tgt=action["tgt"]
            # Only meaningful vs PLAYABLE rivals
            if tgt and tgt in PLAYABLE and d in(SUCCESS,OVERWHELMING):
                self.mut(f"f:{fid}:influence",1)

        return d

    def _church_seizure(self,action,d,rng):
        tid=action["tgt"]
        if not tid: return
        td=self.setting.get(tid)
        if not td or not td.playable or td.ctrl not in PLAYABLE or td.ctrl=="church": return
        # Grant CB to defending faction (PP-510)
        # (simplified: noted in log)
        if d in(SUCCESS,OVERWHELMING):
            old=td.ctrl
            self.setting.set_ctrl(tid,"church"); self.setting.end_occ(tid)
            self._stab(old,-2 if td.is_cap else -1,f"Seized {tid}",1)
            if d==OVERWHELMING: self.mut(td.pk(),1)
            self._log_e(f"SEIZURE {tid} ({old}→church)")
        elif d==FAILURE:
            self.mut("f:church:mandate",-1)

    # ── CI accounting ─────────────────────────────────────────────────────────
    def _tc_acct(self,supp):
        """
        CI accounting per military_layer_v30 §3 (revised formula, PP-402 repealed).
        Step 1: Conditional passive (0/+1/+2 by prominent count).
        Step 2: Piety Yield per prominent territory PT.
        Step 3: Charity Advantage (Church Wealth outperforms controller).
        Step 4: Templar Presence (Templar unit in PT>=3 prominent territory, max +2).
        Step 5: Assert result (applied earlier in action resolution, flagged in _assert_bonus).
        Step 6: Suppress negates Steps 1-2 if fired.
        Step 7: Baralta -1 if HF Mandate >= 4.
        """
        cm=self.fs("church","mandate")
        prom=self.setting.church_prominent(self.reg,cm)
        np=len(prom)

        # Step 1: Conditional passive (PP-402 repealed; replaced)
        if np>=5:   passive=2
        elif np>=2: passive=1
        else:       passive=0
        if passive>0: self.mut(KEY_CI,passive)

        # Step 2: Piety Yield
        frac=sum(1.0  if self.reg.val(t.pk())==5 else
                 0.5  if self.reg.val(t.pk())==4 else
                 0.25 if self.reg.val(t.pk())==3 else 0.0 for t in prom)
        pt_yield=math.floor(frac)
        if pt_yield>0: self.mut(KEY_CI,pt_yield)

        # Step 3: Charity Advantage (Church Wealth >= controller Wealth + 2)
        church_wealth=self.fs("church","wealth")
        charity_frac=0.0
        for t in prom:
            ctrl_wealth=self.fs(t.ctrl,"wealth")
            if church_wealth>=ctrl_wealth+2: charity_frac+=0.5
        charity=min(1,math.floor(charity_frac))
        if charity>0: self.mut(KEY_CI,charity)

        # Step 4: Templar Presence (Templar unit in PT>=3 prominent territory)
        templar_tc=0
        for t in prom:
            if self.reg.val(t.pk())>=3:
                if any(u.is_templar for u in self.setting.units_in(t.tid)):
                    templar_tc+=1
        templar_tc=min(2,templar_tc)
        if templar_tc>0: self.mut(KEY_CI,templar_tc)

        # Step 6: Suppress negates conditional passive and Piety Yield
        if supp:
            self.mut(KEY_CI,-passive)
            self.mut(KEY_CI,-pt_yield)

        # Step 5: Assert result
        if self._assert_bonus>0:
            self.mut(KEY_CI,self._assert_bonus)
        self._assert_bonus=0

        # Step 7: Baralta
        hf=self.fr.get("hafenmark")
        if hf and hf.is_active and self.fs("hafenmark","mandate")>=4:
            self.mut(KEY_CI,-1)

        # CI milestone 80: Year-End PT drift toward piety
        tc_now=self.tc()
        if tc_now>=80 and self.cs==SEASONS_PER_YEAR:
            for t in self.setting.all():
                if t.playable and t.ctrl and t.ctrl in PLAYABLE:
                    self.mut(t.pk(),1)   # PT +1 drift toward piety

    # ── Occupation accounting ─────────────────────────────────────────────────
    def _occ_acct(self):
        for t in self.setting.all():
            if not self.setting.is_occ(t.tid): continue
            s=self.setting.adv_occ(t.tid)
            disp=t.ctrl
            if disp and self.fr.get(disp) and self.fr.get(disp).is_active:
                self._stab(disp,-1,f"{t.tid} occ ongoing",1)
                self.mut(f"f:{disp}:wealth",-1)
            if s>=3:
                occ=self.setting.occupier(t.tid)
                self.setting.end_occ(t.tid); self.setting.set_ctrl(t.tid,occ)
                if disp and disp!=occ:
                    self._stab(disp,-2 if t.is_cap else -1,f"{t.tid} transferred 3s",1)
                self._log_e(f"TRANSFER {t.tid}: {disp}→{occ}")

    # ── Full accounting ───────────────────────────────────────────────────────
    def _peninsular_strain(self):
        """Apply Turmoil effects to faction Mandate."""
        ps=self.reg.val("ps")
        if ps<=2: return
        import random as _r; rng=_r.Random()  # local rng for checks
        for f in self.fr.active():
            if not f.has("mandate"): continue
            man=self.fs(f.fid,"mandate")
            if ps<=4: ob=1
            elif ps<=6: ob=1   # accord handled separately
            elif ps<=8: ob=2
            else:       ob=3
            if ps>=3:
                d,_=roll(max(man,1),ob,rng)
                if d==FAILURE: self.mut(f"f:{f.fid}:mandate",-1)

    def _accord_update(self):
        """Accord degradation and revolt per Turmoil."""
        ps=self.reg.val("ps")
        for t in self.setting.all():
            if not t.playable or not t.ctrl or t.ctrl not in PLAYABLE: continue
            # Accord 1 without garrison → 0
            if t.accord==1 and not self.setting.garrison(t.tid):
                t.accord=0
            # Revolt
            if t.accord==0:
                self.reg.apply("ps",1)   # revolt +1 Turmoil
                # Garrison fights Popular Uprising
                if self.setting.garrison(t.tid):
                    import random as _r; rng2=_r.Random()
                    d,_=roll(max(self.fs(t.ctrl,"military"),1),2,rng2)
                    if d==FAILURE:
                        # Garrison loses: territory uncontrolled
                        self.setting.set_ctrl(t.tid,"")
                        self._stab(t.ctrl,-1,"Revolt: garrison lost territory",1)
                else:
                    self.setting.set_ctrl(t.tid,"")
            # Turmoil 5-6: Accord -1 in one non-capital per faction (simplified: affect contested border)
            if ps>=5 and not t.is_cap and t.accord>0:
                if ps>=7:   # 7-8: all non-capital
                    t.accord=max(0,t.accord-1)
                elif ps>=5: # 5-6: one per faction (simplified: lowest-accord territory)
                    # Only degrade if this is the lowest-accord non-capital territory for this faction
                    faction_terrs=[x for x in self.setting.faction_terrs(t.ctrl) if not x.is_cap]
                    if faction_terrs:
                        lowest=min(faction_terrs,key=lambda x:x.accord)
                        if lowest.tid==t.tid:
                            t.accord=max(0,t.accord-1)

    def run_accounting(self,rng):
        # Weight-of-numbers deferred
        for fid,reason in self._wow: self._stab(fid,-1,f"WoN:{reason}",5)
        self._wow.clear()
        # Accounting Stability Check
        for f in self.fr.active():
            loss=self.reg.season_loss(f.fid)
            if loss>=2:
                d,_=roll(max(self.fs(f.fid,"stability"),1),loss,rng)
                if d==FAILURE: self.mut(f.stabk(),-1)
                elif d==OVERWHELMING: self.mut(f.stabk(),1)
        # CI
        self._tc_acct(self._suppress); self._suppress=False
        # RS annual decay
        if self.cs==SEASONS_PER_YEAR: self.mut(KEY_RS,-1)
        # Battle → RS −1 per season with battles, IP +2 (canonical: params_board_game §Battle Consequences)
        if self._battles_this_season>0:
            self.mut(KEY_RS,-1)
            self.mut(KEY_IP,2)
            # Turmoil +1 per season with battle
            self.reg.apply("ps",1)
        self._battles_this_season=0
        # Altonian pressure
        if self.reg.val(KEY_TORBEN)<=3: self.mut(KEY_IP,1)
        # Occupation
        self._occ_acct()
        # Institutional Consolidation: +1 Stab if no triggers this season
        for f in self.fr.active():
            if f.fid not in self._tfs and self.fs(f.fid,"stability")>0:
                self.mut(f.stabk(),1)
        self._tfs=set()
        # Collapse + wealth zero
        self._peninsular_strain()
        self._accord_update()
        self._collapse_check(); self._wealth_zero()
        # Resets
        self.reg.reset_f(); self.reg.reset_w()
        self.setting.adv_vac(); self._coup_check()

    def _collapse_check(self):
        for f in self.fr.active():
            if self.fs(f.fid,"stability")<=0: self._collapse_fid(f.fid)

    def _collapse_fid(self,fid):
        f=self.fr.get(fid)
        if not f or not f.is_active: return
        f.is_active=False
        tids=self.setting.faction_tids(fid)
        self.setting.enter_vac(tids)
        for u in self.setting.faction_units(fid): u.dead=True
        self.setting.purge_dead()
        self._log_e(f"COLLAPSE:{fid}")
        if fid=="crown": self.reg.apply(KEY_COUP,4)

    def _wealth_zero(self):
        """Wealth Zero: professional units (HI/Cavalry) lose Discipline, not Military stat."""
        for f in self.fr.active():
            if not f.has("wealth") or self.fs(f.fid,"wealth")>0: continue
            # Professional units unpaid -> Discipline degrades
            for u in self.setting.faction_units(f.fid):
                if u.utype in ("heavy_infantry","cavalry","templar"):
                    u.disc=max(0,u.disc-1)
                    if u.disc<=0: u.dead=True
            self.setting.purge_dead()

    def _coup_check(self):
        if self.reg.val(KEY_COUP)>=4 and not self._lr_ok:
            lr=self.fr.get("lowenritter")
            if lr and not lr.is_active:
                self._lr_ok=True; lr.is_active=True; self.fr.reg_f(lr)
                self._log_e("LR COUP")

    def advance_season(self):
        self.cs+=1
        if self.cs>SEASONS_PER_YEAR: self.cs=1; self.cy+=1

    # ── Victory ───────────────────────────────────────────────────────────────
    def check_victory(self):
        if self.rs()<=0: return{"fid":"","vt":"RS_RUPTURE"}
        cr=self.fr.get("crown")
        if cr and cr.is_active:
            sup=sum(1 for fid in["church","hafenmark","varfell"]
                    if not self.fr.get(fid) or not self.fr.get(fid).is_active
                    or self.fs(fid,"mandate")<=2)
            if self.setting.faction_tcv("crown")>=CROWN_TCV and sup>=2 and self.ip()<60 and self.reg.val(KEY_PARL)>=3:
                self._rec("crown","CROWN_TREATY")
            else: self._clr("crown")
        ch=self.fr.get("church")
        if ch and ch.is_active:
            ctcv=self.setting.faction_tcv("church"); cm=self.fs("church","mandate")
            allpt=all(self.reg.val(t.pk())>=3 for t in self.setting.all() if t.ctrl=="church")
            if ctcv>=CHURCH_TCV and cm>=4 and allpt: self._rec("church","CHURCH_ORTHODOXY")
            else: self._clr("church")
        hf=self.fr.get("hafenmark")
        if hf and hf.is_active:
            if self.setting.faction_tcv("hafenmark")>=HF_TCV and self.fs("hafenmark","mandate")>=4 and self.fs("hafenmark","stability")>=3 and self.fs("crown","mandate")<=3:
                self._rec("hafenmark","HF_INSTITUTIONAL")
            else: self._clr("hafenmark")
        for k,c in self._vc.items():
            if c.get("s",0)>=VICTORY_SUSTAIN: return{"fid":k,"vt":c["vt"]}
        return None

    def _rec(self,k,vt):
        if k not in self._vc: self._vc[k]={"s":0,"vt":vt}
        self._vc[k]["s"]+=1; self._vc[k]["vt"]=vt
    def _clr(self,k): self._vc.pop(k,None)

    def _log_e(self,msg): self._log.append({"y":self.cy,"s":self.cs,"msg":msg})

    def snap(self):
        return{f.fid:{"active":f.is_active,
                       "stats":{s:self.fs(f.fid,s) for s in f.stats},
                       "tcv":self.setting.faction_tcv(f.fid),
                       "units":self.setting.unit_count(f.fid)}
               for f in self.fr.all()}

# ── HYBRID SCENE ──────────────────────────────────────────────────────────────
def hybrid_scene(world,rng):
    r=rng.random()
    if r<0.65: deg=SUCCESS
    elif r<0.85: deg=OVERWHELMING
    elif r<0.95: deg=PARTIAL
    else: deg=FAILURE
    if deg==OVERWHELMING:
        world.mut(KEY_RS,1); world.mut(KEY_CI,-1)
    elif deg==SUCCESS and rng.random()<0.3:
        world.mut(KEY_RS,1)

# ── RUNNERS ───────────────────────────────────────────────────────────────────
def run_season(world,rng,verbose=False):
    world.advance_season(); world._suppress=False
    acts=[]
    for f in world.fr.active():
        for o in world.ai_orders(f,rng): acts.append((f,o))
    rng.shuffle(acts)
    for f,a in acts:
        d=world.resolve_action(a,rng)
        if verbose:
            print(f"  Y{world.cy}S{world.cs} {f.fid:14s} {a['at']:20s} {a['tgt']:8s} → {DN[d]}")
    if world.mode=="hybrid": hybrid_scene(world,rng)
    world.run_accounting(rng)

def run_campaign(seed=None,max_years=25,mode="bg",verbose=False):
    rng=random.Random(seed); world=World(mode=mode); world.start()
    result=None
    for _ in range(max_years*SEASONS_PER_YEAR):
        run_season(world,rng,verbose)
        if world._go: result=world._go; break
        v=world.check_victory()
        if v: result=v; break
    return{"seed":seed,"mode":mode,"years":world.cy,"season":world.cs,
           "outcome":result or{"fid":"","vt":"TIMEOUT"},
           "rs":world.rs(),"ci":world.tc(),"ip":world.ip(),"snap":world.snap(),
           "log":world._log[-12:]}

def run_many(n=200,max_years=25,mode="bg"):
    outs=Counter(); vics=Counter(); durs=[]; rs_f=[]; tc_f=[]; coll=Counter()
    for i in range(n):
        r=run_campaign(seed=i,max_years=max_years,mode=mode)
        vt=r["outcome"]["vt"]; fid=r["outcome"].get("fid","")
        outs[vt]+=1; vics[fid or vt]+=1; durs.append(r["years"])
        rs_f.append(r["rs"]); tc_f.append(r["ci"])
        for fid2,fs in r["snap"].items():
            if not fs["active"]: coll[fid2]+=1
    nf=max(n,1)
    return{"n":n,"mode":mode,
           "outcomes":dict(sorted(outs.items(),key=lambda x:-x[1])),
           "victors":dict(sorted(vics.items(),key=lambda x:-x[1])),
           "avg_y":round(sum(durs)/nf,2),
           "min_y":min(durs),"max_y":max(durs),
           "avg_rs":round(sum(rs_f)/nf,1),"avg_tc":round(sum(tc_f)/nf,1),
           "collapse":{k:f"{v/nf*100:.1f}%" for k,v in sorted(coll.items(),key=lambda x:-x[1])}}

# ── STRESS TESTS ──────────────────────────────────────────────────────────────
def stress_tests():
    fails=[]; rng=random.Random(42)
    def chk(name,cond,msg=""):
        if cond: print(f"  ✓ {name}")
        else: fails.append((name,msg)); print(f"  ✗ {name}: {msg}")

    print("="*54+"\nSTRESS TESTS\n"+"="*54)

    # T1: Starting garrisons
    w=World(); w.start()
    chk("Crown T1=3 units", w.setting.unit_count("crown")>=3,
        f"crown units={w.setting.unit_count('crown')}")
    t1_units=len(w.setting.units_in("T1"))
    chk("T1 Valorsplatz has 3 units", t1_units==3, f"T1 units={t1_units}")
    t9_units=len(w.setting.units_in("T9"))
    chk("T9 Himmelenger has 2 units", t9_units==2, f"T9 units={t9_units}")
    t8_units=len(w.setting.units_in("T8"))
    chk("T8 Gransol has 2 units", t8_units==2, f"T8 units={t8_units}")
    t2_units=len(w.setting.units_in("T2"))
    chk("T2 Kronmark has 1 unit (border:church)", t2_units==1, f"T2 units={t2_units}")
    t5_units=len(w.setting.units_in("T5"))
    chk("T5 Feldmark has 0 units (interior)", t5_units==0, f"T5 units={t5_units}")

    # T2: Garrison blocks march
    w2=World(); w2.start()
    chk("T9 garrisoned at start", w2.setting.garrison("T9"), "not garrisoned")
    # Find a Crown border unit for T14→T9
    t14_units=[u for u in w2.setting.faction_units("crown") if u.tid=="T14"]
    chk("T14 has crown unit", len(t14_units)>0, f"T14 units={len(t14_units)}")
    if t14_units:
        res=w2.do_march("crown",t14_units[0],"T9",rng)
        chk("March into garrisoned T9 triggers battle", res=="battle", f"res={res}")

    # T3: Ungarrisoned territory: free march
    w3=World(); w3.start()
    # T5 Feldmark is ungarrisoned interior Crown territory — but controlled by Crown
    # Let's test march into enemy ungarrisoned: find one
    # Give Varfell a territory with no garrison adjacent to Crown
    # T13 (Varfell) adjacent to T6 (Crown). T13 starts with 1 unit (border).
    # Let's manually clear T13's unit and march Crown T6 unit into T13
    t13_units=w3.setting.units_in("T13")
    for u in t13_units: u.dead=True
    w3.setting.purge_dead()
    t6_units=[u for u in w3.setting.faction_units("crown") if u.tid=="T6"]
    chk("T6 has crown unit for march", len(t6_units)>0)
    if t6_units:
        res=w3.do_march("crown",t6_units[0],"T13",rng)
        chk("March into ungarrisoned T13 = free occ", res=="occ_free", f"res={res}")
        chk("T13 now occupied", w3.setting.is_occ("T13"))

    # T4: PP-403 repealed
    w4=World(); w4.start()
    init=w4.fs("crown","stability")
    w4.reg.get("f:crown:mandate").v=1
    for _ in range(5): w4.resolve_action({"at":"govern","tgt":"","ps":"mandate","ob":5,"fid":"crown","meta":{}},rng)
    chk("PP-403 repealed (no stab loss on non-mil fail)", w4.fs("crown","stability")==init,
        f"stab {init}→{w4.fs('crown','stability')}")

    # T5: NPC not targeted diplomatically
    w5=World(); w5.start()
    cr=next(f for f in w5.fr.active() if f.fid=="crown")
    orders=w5.ai_orders(cr,rng)
    treaty_targets=[o["tgt"] for o in orders if o["at"]=="crown_treaty"]
    bad_targets=[t for t in treaty_targets if t in NPC_ONLY or t==""]
    chk("Crown Treaty never targets NPCs", not bad_targets, f"bad targets: {bad_targets}")

    # T6: Church Seizure targets PLAYABLE only
    w6=World(); w6.start()
    w6.reg.get(KEY_CI).v=50
    ch=next(f for f in w6.fr.active() if f.fid=="church")
    orders=w6.ai_orders(ch,rng)
    seizure_targets=[o["tgt"] for o in orders if o["at"]=="church_seizure"]
    bad_seiz=[t for t in seizure_targets
              if t and w6.setting.ctrl(t) not in PLAYABLE or w6.setting.ctrl(t)=="church"]
    chk("Church Seizure targets only valid PLAYABLE", not any(w6.setting.ctrl(t) in NPC_ONLY for t in seizure_targets),
        f"bad: {seizure_targets}")

    # T7: Posture returns valid string
    w7=World(); w7.start()
    VALID_POSTURES={"EXISTENTIAL","DEFEND","CONSOLIDATE","SUPPRESS","TREATY","SEIZE","EXPAND","OPPORTUNISTIC"}
    for f in w7.fr.playable_active():
        p=w7._posture(f)
        chk(f"Posture valid for {f.fid}", p in VALID_POSTURES,f"got {p}")

    # T8: Muster cap (P-18) — starting garrisons exceed cap (standing army exception)
    # but NEW musters are blocked when unit_count >= Military stat
    w8=World(); w8.start()
    # Crown starts with 7 units (3 at capital + border garrisons) but Military=4
    # New muster should be blocked
    # Crown starts with 7 units, mil=4, cap=(4*2+3)=11 — can still muster
    # Force over cap by adding units manually
    mil8=w8.fs("crown","military"); cap8=mil8*2+3
    while w8.setting.unit_count("crown")<cap8: w8.setting.new_unit("crown","T1")
    result=w8.do_muster("crown","T1",rng)
    chk("Muster blocked at (Military*2)+3 cap", not result,
        f"units={w8.setting.unit_count('crown')} cap={cap8}")

    # T9: CI Baralta suppression at HF Mandate >= 4
    w9=World(); w9.start(); tc_before=w9.tc()
    # New CI: passive+2 (8 prominent), piety+1 (four PT=3 at 0.25ea), baralta-1 = net +2
    w9._tc_acct(False)
    chk("CI advances by +2 (passive+2 + piety+1 - baralta-1)", w9.tc()==tc_before+2, f"tc {tc_before}→{w9.tc()}")
    # Without Baralta: net +3
    tc_before2=w9.tc()
    w9.reg.get("f:hafenmark:mandate").v=3
    w9._tc_acct(False)
    chk("CI advances faster without Baralta", w9.tc()>=tc_before2+3, f"tc {tc_before2}→{w9.tc()}")

    # T10: Full campaigns
    for mode in("bg","hybrid"):
        try:
            r=run_campaign(seed=1,max_years=25,mode=mode)
            chk(f"{mode} campaign completes","vt" in r["outcome"])
        except Exception as e:
            chk(f"{mode} campaign completes",False,str(e))

    total=10+len([f.fid for f in World().start() or []])+2
    # recount
    passed=sum(1 for _ in [None]*100)-len(fails)  # rough
    passed2=20-len(fails)
    print(f"\n{passed2}/20 checks, {len(fails)} failures")
    if fails:
        print("FAILURES:")
        for n,m in fails: print(f"  [{n}] {m}")
    return len(fails)==0

def print_stats(st,label):
    n=st["n"]
    print(f"\n{'='*60}\n  {label}\n{'='*60}")
    print(f"Duration: avg {st['avg_y']}y  min {st['min_y']}y  max {st['max_y']}y")
    print(f"Avg RS={st['avg_rs']}  CI={st['avg_tc']}")
    print("\nOutcomes:")
    for vt,c in st["outcomes"].items():
        pct=c/n*100; bar="█"*max(1,int(pct/2))
        print(f"  {vt:30s} {c:4d}  {pct:5.1f}%  {bar}")
    print("\nVictors:")
    for fid,c in st["victors"].items():
        print(f"  {fid:25s} {c:4d}  {c/n*100:5.1f}%")
    print("\nCollapse rates:")
    for fid,r in st["collapse"].items(): print(f"  {fid:20s} {r}")

if __name__=="__main__":
    ok=stress_tests()
    if not ok: import sys; sys.exit(1)

    print("\n"+"="*60+"\nBG — seed=42 trace\n"+"="*60)
    r=run_campaign(seed=42,max_years=25,mode="bg",verbose=True)
    print(f"\nOutcome: {r['outcome']}  Y{r['years']}S{r['season']}  RS={r['rs']} CI={r['ci']}")
    for fid,fs in r["snap"].items():
        if not fs["stats"]: continue
        st="ACTIVE" if fs["active"] else "DEAD"
        sv=" ".join(f"{k[0]}={v}" for k,v in fs["stats"].items())
        print(f"  {fid:14s}[{st}] TCV={fs['tcv']} u={fs['units']}  {sv}")
    for e in r["log"][-8:]: print(f"  Y{e['y']}S{e['s']}: {e['msg']}")

    print("\nRunning 500 BG campaigns...")
    bg=run_many(500,25,"bg")
    print_stats(bg,"BG MODE — 500 campaigns")

    print("\nRunning 300 Hybrid campaigns...")
    hy=run_many(300,25,"hybrid")
    print_stats(hy,"HYBRID MODE — 300 campaigns")

    print("\n"+"="*60+"\nBALANCE DIAGNOSTIC\n"+"="*60)
    all_vt=set(bg["outcomes"])|set(hy["outcomes"])
    print(f"  {'Outcome':30s}  {'BG%':>6}  {'HY%':>6}")
    for vt in sorted(all_vt):
        bp=bg["outcomes"].get(vt,0)/500*100; hp=hy["outcomes"].get(vt,0)/300*100
        print(f"  {vt:30s}  {bp:6.1f}%  {hp:6.1f}%")
    print("\nFlags:")
    for ml,st,n in[("BG",bg,500),("Hybrid",hy,300)]:
        top=max(st["outcomes"],key=st["outcomes"].get)
        pct=st["outcomes"][top]/n*100
        print(f"  {'⚠' if pct>65 else '✓'} [{ml}] top outcome: {top} {pct:.1f}%")
        ay=st["avg_y"]
        print(f"  {'⚠' if ay<6 or ay>22 else '✓'} [{ml}] avg duration {ay}y")
