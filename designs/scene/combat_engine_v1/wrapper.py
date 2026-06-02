"""CombatWrapper — owns the state graph and the A/B identity. The driver assigns aggressor/defender ONCE per
beat and passes Combatant objects to every subsystem. Initialization is the only toggle. This is the structural
cure for the role-inversion bug class: no subsystem and no resolution step ever indexes raw 'A'/'B'."""
import sys; sys.path.insert(0,'/home/claude/combat_engine')
from math import exp
import core, systems as S, tradition as TR
from config import CFG

def _init_live(c, cfg):
    c.stamina_max=S.stamina_max(c); c.stamina=float(c.stamina_max)
    c.conc_max=S.conc_max(c,cfg);   c.conc=c.conc_max
    c.ready=0.0

def engagement(A, B, first, cfg, rng):
    """One engagement (the exchange inside a bout). `first` is the initiating Combatant object. Returns the
    felled Combatant or None (separation). A and B are fixed objects throughout — never swapped."""
    aggressor = first; defender = B if first is A else A
    erA=S.reach_base(A,cfg); erB=S.reach_base(B,cfg)
    er={A:erA, B:erB}
    longer = A if erA>=erB else B; shorter = B if longer is A else A
    measure_gap=max(0.0, er[longer]-er[shorter]); closed=(measure_gap<=0.3)
    # tempo is CONDITIONAL (grip/stance/fatigue), recomputed per-beat below — not a static pre-loop property.
    ready={A:0.0,B:0.0}
    beats=0; exchanges=0; soft=8
    reopen_moment=False; push_avail=False   # distance-creating-moment state for re-opening (corrections 1+3)
    feint_streak=0                           # feints-in-a-row counter (capped at FEINT_MAX_STREAK)
    while beats < soft*3:
        beats+=1
        # CONDITIONAL TEMPO (correction 2): recompute each beat with current fatigue — grip/stance/fatigue change
        # cadence; it is not a static weapon property. Approach uses general cadence; closed uses close-cadence.
        ffat={A:max(0.0,1-A.stamina/max(1,A.stamina_max)), B:max(0.0,1-B.stamina/max(1,B.stamina_max))}
        if not closed: rate={c:S.weapon_tempo(c,cfg,ffat[c]) for c in (A,B)}
        else:          rate={c:S.close_tempo(c,cfg,ffat[c]) for c in (A,B)}
        for c in (A,B): ready[c]+=rate[c]
        # REACH RE-OPENING (corrections: a created moment, not just footwork+reach). The longer weapon can make
        # distance only when a MOMENT exists — the opponent over-committed (must recover balance), OR the longer
        # weapon won a defensive maneuver last exchange (bind/parry/deflect created the gap), OR it frees a hand to
        # shove (grappling-manual one-handed push at reach). Identifying the moment needs READING; executing the
        # withdrawal needs FOOTWORK; and the attempt is READABLE — the shorter weapon's own read can deny it.
        if closed and beats>1 and reopen_moment:
            base_gap=er[longer]-er[shorter]
            if base_gap>0.3 and rng.random()<S.reopen_prob(longer, shorter, base_gap, push_avail, cfg, TR):
                closed=False; measure_gap=base_gap; ready={A:0.0,B:0.0}
                reopen_moment=False; push_avail=False
                continue
        reopen_moment=False   # the moment is fleeting; consumed/expires each beat unless re-created below
        # ----- APPROACH: longer weapon threatens (stop-hits) while shorter closes -----
        if not closed:
            displ = S.approach_displace(shorter, longer, cfg)        # lever-arm: set aside a thrusting point on approach
            close_rate=cfg['CLOSE_RATE_K']*S.footwork_eff(shorter,0,cfg)/3 * S.weapon_tempo(shorter,cfg,ffat[shorter])/2
            close_rate *= (1+displ)                                  # displacing the point lets you close faster
            measure_gap=max(0.0, measure_gap-close_rate)
            just_closed = (measure_gap<=0.3)
            if just_closed:
                closed=True; ready={A:0.0,B:0.0}   # reset readiness: closed phase starts fair (no banked approach tempo)
            stophit_p = cfg['STOPHIT_CHANCE'] * min(1.0, measure_gap/cfg['STOPHIT_FULL_GAP']) * (1-displ)  # point set aside
            if rng.random() < stophit_p:
                pool=core.resolution_pool(longer.history)
                nsig=cfg['REACH_DISADV_K']*measure_gap + 0.4
                ob=core.effective_ob(pool, nsig); net=core.roll_net(pool, rng)
                deg=core.degree(net, ob)
                if deg in ('success','overwhelming'):
                    d=core.damage(deg, longer.weight, longer.head, longer.strength, shorter.armor, False, cfg['DAMAGE_SCALE'], cfg['CAP_END'], longer.w['gap'])
                    shorter.apply_wound(d); shorter.conc=max(0,shorter.conc-cfg['CONC_DRAIN_HIT'])
                    if shorter.felled: return shorter
            if not closed:
                if A.stamina<=-4 or B.stamina<=-4: return None
                continue
        # ----- CLOSED: tempo-gated exchange -----
        actors=[c for c in (A,B) if ready[c]>=cfg['ACT_THRESHOLD']]
        if not actors: continue
        if len(actors)==2:
            aggressor = max(actors, key=lambda c: ready[c]) if ready[A]!=ready[B] else actors[rng.integers(2)]
        else:
            aggressor = actors[0]
        defender = B if aggressor is A else A
        # half-sword auto-switch (mit dem kurzen Schwert): adopt the form fitting the current range/armour
        S.halfsword_switch(aggressor, closed, defender.armor, cfg)
        S.halfsword_switch(defender, closed, aggressor.armor, cfg)
        ready[aggressor]-=cfg['ACT_THRESHOLD']
        commit=int(rng.integers(2,6))
        aggressor.stamina-=S.act_cost(aggressor,commit,cfg)
        oob=cfg['OOB'] if aggressor.stamina<=0 else 0
        fat_a=max(0.0,1-aggressor.stamina/max(1,aggressor.stamina_max)); fat_d=max(0.0,1-defender.stamina/max(1,defender.stamina_max))
        cfrac_d=defender.conc/max(1,defender.conc_max)
        # concentration: mental-fatigue protection (fatigue-resistance) — defender's reading/technique
        mental_fat_d=fat_d*(1-cfg['FOCUS_MENTAL_K']*max(0,min(1,cfrac_d)))
        # tradition channel-weights (cognitive-mode biases over the shared substrate; neutral=1.0)
        ta=aggressor.tradition; td=defender.tradition
        # standing reach advantage (module): defender's reach lowers the attacker's net, falling with armour.
        reach_pen=S.reach_sigma(aggressor, defender, er, fat_a, fat_d, cfg, TR)
        # tempo emphasis (commitment-window exploitation): re-weights the aggressor's initiative
        init=cfg['INIT_K']*(aggressor.agi-defender.agi)*TR.channel_weight(ta,'tempo')
        consistency_a=cfg['FOCUS_CONSISTENCY_K']*(aggressor.focus-3)
        # feinting (module): wrapper applies the state changes the pure evaluator returns.
        fv=S.feint_eval(aggressor, defender, mental_fat_d, feint_streak, cfg, rng, TR)
        feint_debuff=fv['debuff']; feint_streak=fv['new_streak']
        if fv['do']:
            beats += fv['beat_cost']; aggressor.stamina -= fv['stamina_cost']
        # VISUAL read (pre-contact anticipation; temporal-spatial). Weighted by tradition's visual emphasis, DEGRADED
        # vs an unfamiliar aggressor (knowledge-of-others), and MODULATED BY MOVEMENT LEGIBILITY (correction 4):
        # large/lateral movement is easier to perceive than in-line motion. A thrust (in-line, point/high-gap) is
        # HARD to read; a swing/cut (lateral arc) is EASY; and a deeper commit / lunge = more biomechanical action =
        # more readable. So the defender's read rises vs swings/lunges and falls vs thrusts.
        fam = TR.familiarity(td, ta)
        legib=S.legibility(aggressor, commit, cfg)   # module: swings/lunges easy to read, thrusts hard
        read_d=reading(defender)*TR.channel_weight(td,'visual')*fam*legib*(1-0.4*mental_fat_d)*(1-feint_debuff)
        read_a=reading(aggressor)*TR.channel_weight(ta,'visual')+consistency_a
        read_win = rng.random() < 1/(1+exp(-(read_d-read_a)/1.0))
        modes=['parry','dodge','wind']
        msig={m:S.mode_sigma(m,aggressor,defender,commit,0.0,read_win,fat_d,cfg) for m in modes}
        mode=max(msig,key=msig.get) if read_win else modes[rng.integers(3)]
        dsig=msig[mode]*(1-0.3*mental_fat_d)*(1-feint_debuff) - S.handling_penalty(defender,fat_d,cfg) + S.stance_stability(defender,fat_d,cfg)
        atk_sig=cfg['COMMIT_SIGMA']*(commit-3) + init - oob*0.5 - S.handling_penalty(aggressor,fat_a,cfg) + consistency_a
        adef=S.armor_defeat_sigma(aggressor, defender, cfg)   # armour-defeat capability controls armoured exchanges
        net_sigma=atk_sig - dsig - reach_pen + adef
        pool=core.resolution_pool(aggressor.history)
        ob=core.effective_ob(pool, net_sigma); net=core.roll_net(pool, rng)
        deg=core.degree(net, ob)
        close = closed   # C-1: per-beat close-coupling follows the engagement measure-state (not raw reach alone)
        # anti_overcommit (D-1): a deep commit exposes the aggressor to the riposte; footwork-balance curbs it.
        overcommit_exposure = max(0.0, cfg['COMMIT_EXPOSE_K']*(commit-3)) - S.anti_overcommit(aggressor,fat_a,cfg)
        # ----- outcome mapping (deg = AGGRESSOR's degree; defender mode can neutralize) -----
        hit=0; riposte=False; bind=False
        # armour-defeat: slow heavy blunt (poleaxe/mace) lands few but plate-defeating blows; boost effective impact
        # vs armour (audit triad C). Applied as effective strength so it flows through coupling consistently.
        astr = aggressor.strength + S.armor_defeat_bonus(aggressor, defender, cfg)
        # neutralize is a FIXED mode-shape (parry deflects / dodge voids / wind binds) — NOT re-scaled by dsig,
        # which already shaped the roll via net_sigma (audit C-2: avoid double-counting defender skill).
        neutralize=cfg['NEUTRALIZE_PARRY'] if mode=='parry' else (cfg['NEUTRALIZE_DODGE'] if mode=='dodge' else cfg['NEUTRALIZE_WIND'])
        if deg=='fail':
            riposte=(rng.random() < min(0.95, cfg['RIPOSTE_ON_FAIL']+overcommit_exposure))
        elif deg=='partial':
            if mode=='dodge': hit=core.damage('graze',aggressor.weight,aggressor.head,astr,defender.armor,close,cfg['DAMAGE_SCALE'],cfg['CAP_END'],aggressor.w['gap']) if rng.random()<0.4 else 0
            elif mode=='parry': hit=core.damage('graze',aggressor.weight,aggressor.head,astr,defender.armor,close,cfg['DAMAGE_SCALE'],cfg['CAP_END'],aggressor.w['gap']) if rng.random()<0.30 else 0
            else: bind=True
        elif deg=='success':
            if mode=='wind' and rng.random()<0.55: bind=True
            elif rng.random()<neutralize: riposte=(rng.random() < min(0.95, 0.20+overcommit_exposure))
            else: hit=core.damage('success',aggressor.weight,aggressor.head,astr,defender.armor,close,cfg['DAMAGE_SCALE'],cfg['CAP_END'],aggressor.w['gap'])
        else:
            if rng.random()<max(0.0,neutralize-cfg['NEUTRALIZE_OVERWHELM_DROP']): hit=0
            else: hit=core.damage('overwhelming',aggressor.weight,aggressor.head,astr,defender.armor,close,cfg['DAMAGE_SCALE'],cfg['CAP_END'],aggressor.w['gap'])
        sim=(hit>0 and riposte)
        # DISPLACE-AND-STEP-INSIDE (manual technique): vs a COMMITTED THRUST (point head, deep commit), a defender
        # with a LEVERAGE advantage can set the point aside with grip+mass and step inside the reach while the
        # thruster is committed — collapsing measure in the defender's favour. CAVEAT (Jordan): the thruster's
        # pull-back/recovery can still graze. Needs the defender to win the read (already gated) and leverage edge.
        if (aggressor.w['head']=='point' and commit>=4 and not hit and read_win
                and S.leverage(defender,cfg) > S.leverage(aggressor,cfg)+cfg['DISPLACE_LEV_GAP']):
            if rng.random() < cfg['DISPLACE_P']:
                if not closed: closed=True; measure_gap=0.0; ready={A:0.0,B:0.0}
                # pull-back of the committed thrust can still graze the closing defender
                if rng.random() < cfg['DISPLACE_PULLBACK_GRAZE']:
                    d=core.damage('graze',aggressor.weight,aggressor.head,aggressor.strength,defender.armor,False,cfg['DAMAGE_SCALE'],cfg['CAP_END'],aggressor.w['gap'])
                    defender.apply_wound(d)
                    if defender.felled: return defender
                riposte=True   # defender now inside with initiative
        # ---- distance-creating moments for re-opening (corrections 1+3), benefiting the LONGER weapon ----
        # (a) opponent over-committed: a deep commit by the SHORTER weapon (the one who must stay close) leaves it
        #     recovering balance -> the longer weapon can make distance next beat.
        if closed and aggressor is shorter and commit>=4:
            reopen_moment=True
        # (b) the longer weapon, defending, won a defensive maneuver (bind/parry/deflect) this exchange -> a gap opens.
        if closed and defender is longer and (bind or (deg in ('fail','partial') and not hit)):
            reopen_moment=True
        # (c) freed-hand shove: a long TWO-HANDED weapon at the close can briefly free a hand to push (grappling
        #     manuals) -> a chance to create the moment itself. Available when the longer weapon is 2H and closed.
        if closed and longer.w['hands']==2 and rng.random()<cfg['PUSH_AVAIL_P']:
            push_avail=True; reopen_moment=True
        if hit>0:
            defender.apply_wound(hit); defender.conc=max(0,defender.conc-cfg['CONC_DRAIN_HIT'])
            if defender.felled: return defender
        if bind:
            for _ in range(3):
                beats+=1
                bsig = S.bind_sigma(aggressor, defender, cfg, TR)   # module: leverage + tactile (Fuhlen), Str minor
                if rng.random() < 1/(1+exp(-bsig)):
                    if rng.random()<0.4:
                        d=core.damage('success',aggressor.weight,aggressor.head,aggressor.strength,defender.armor,close,cfg['DAMAGE_SCALE'],cfg['CAP_END'],aggressor.w['gap'])
                        defender.apply_wound(d); defender.conc=max(0,defender.conc-cfg['CONC_DRAIN_HIT'])
                        if defender.felled: return defender
                        break
                else: riposte=True; break
        if riposte:
            if sim:
                # concentration disruption-resistance: focus lets aggressor still complete despite the blow
                if rng.random() > 1/(1+exp(-cfg['DISRUPT_K']*(aggressor.focus-3))):
                    d=core.damage('graze',defender.weight,defender.head,defender.strength,aggressor.armor,close,cfg['DAMAGE_SCALE'],cfg['CAP_END'],defender.w['gap'])
                    aggressor.apply_wound(d); aggressor.conc=max(0,aggressor.conc-cfg['CONC_DRAIN_HIT'])
                    if aggressor.felled: return aggressor
            defender.conc=max(0,defender.conc-cfg['CONC_DRAIN_LOSS'])
            aggressor, defender = defender, aggressor   # role flip — objects, frame-safe
        exchanges+=1
        if exchanges>=cfg['MAX_EXCHANGES_PER_BOUT']: return None
        if A.stamina<=-4 or B.stamina<=-4 or rng.random()<0.03: return None
    return None

def fight(A, B, cfg=None, rng=None, max_bouts=12):
    import numpy as np
    cfg=cfg or CFG; rng=rng or np.random.default_rng()
    A.wt.__init__(A.end); B.wt.__init__(B.end)   # reset wounds
    _init_live(A,cfg); _init_live(B,cfg)
    result=0
    for bout in range(max_bouts):
        first = A if rng.random()<0.5 else B
        loser = engagement(A,B,first,cfg,rng)
        if loser is not None:
            result = -1 if loser is A else 1   # +1 => A won
            break
        for c in (A,B):
            c.stamina=min(c.stamina_max, c.stamina+cfg['RECOVERY_FRAC']*(c.stamina_max-c.stamina)*(c.stamina_max/cfg['STAMINA_REF']))
            c.conc=max(0,min(c.conc_max, c.conc-cfg['CONC_DRAIN_BOUT']+cfg['CONC_RECOVER_FRAC']*(c.conc_max-c.conc)))
    if result==0:
        result = 1 if B.wt.wounds>A.wt.wounds else (-1 if A.wt.wounds>B.wt.wounds else 0)
    # 95% cap (videogame rule): no matchup is ever certain. With probability UPSET_FLOOR, the decided LOSER steals
    # the win — a "lucky blow"/critical-opening that the model otherwise suppresses. Applied only to decided fights,
    # symmetric in form, so an X% raw win-rate is clamped toward [UPSET_FLOOR, 1-UPSET_FLOOR].
    if result!=0 and rng.random()<cfg['UPSET_FLOOR']:
        result = -result
    return result
def reading(c): return (c.cog+c.att)/2
