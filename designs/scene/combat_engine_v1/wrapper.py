"""CombatWrapper — owns the state graph and the A/B identity. The driver assigns aggressor/defender ONCE per
beat and passes Combatant objects to every subsystem. Initialization is the only toggle. This is the structural
cure for the role-inversion bug class: no subsystem and no resolution step ever indexes raw 'A'/'B'."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
import core, systems as S, tradition as TR
from config import CFG

# ── TRACE SEAM (workbench / branch-explorer hook) ──────────────────────────────────────────────
# _TRACE is None by default: every _emit() is a single is-None check, so the seam adds ~zero cost
# and CANNOT change behavior (no rng draw, no state mutation). The workbench sets wrapper._TRACE to a
# callable(event: dict) before a run and resets it to None after. Events carry the INPUTS each decision
# node consumed (read margins, the commit distribution, the roll's pool/net_sigma) so the narrator and
# the branch explorer can reconstruct the local probability of every alternate branch without re-deriving
# engine internals. The engine emits facts; probability math lives in the workbench (probabilities.py).
_TRACE = None
def _emit(kind, **data):
    if _TRACE is not None:
        _TRACE(dict(kind=kind, **data))

def _init_live(c, cfg):
    c.derive_stats(cfg)                  # the combatant computes its cfg-dependent figures (conc_max); stamina_max/health set at build
    c.stamina=float(c.stamina_max)       # reset live state from the combatant's own held maxima
    c.conc=c.conc_max
    c.ready=0.0
    c.initiative=0.0
    c.poise=1.0

def engagement(A, B, first, cfg, rng):
    """One engagement (the exchange inside a bout). `first` is the initiating Combatant object. Returns the
    felled Combatant or None (separation). A and B are fixed objects throughout — never swapped."""
    aggressor = first; defender = B if first is A else A
    erA=S.reach_base(A,cfg); erB=S.reach_base(B,cfg)
    er={A:erA, B:erB}
    # FAIRNESS: on EXACTLY equal reach the longer/shorter label is a coin-flip — not always A. The label feeds the
    # reopen-moment logic, so always-A on ties put a latent bias into every same-reach matchup (mirrors, armour, stat
    # matchups), which the attacker-favouring mechanics amplified. Different reach is deterministic as before.
    longer = A if erA>erB else (B if erB>erA else (A if rng.random()<0.5 else B)); shorter = B if longer is A else A
    measure_gap=max(0.0, er[longer]-er[shorter]); closed=(measure_gap<=0.3)
    # Pre-contact seizure CUT 2026-06-05 (Jordan; verified inert - ablation ~0, washed out by per-beat dynamics):
    # initiatives start even (0.0 from _init_live); the ongoing Vor (hit-gains/steals/decay) decides who holds it.
    A.initiative, B.initiative = 0.0, 0.0
    # tempo is CONDITIONAL (grip/stance/fatigue), recomputed per-beat below — not a static pre-loop property.
    ready={A:0.0,B:0.0}
    beats=0; exchanges=0; soft=8
    reopen_moment=False; push_avail=False   # distance-creating-moment state for re-opening (corrections 1+3)
    # (feint_streak removed — feint dissolved into the attack, WS-5)
    _emit('engagement_start', aggressor=first.label, defender=(B if first is A else A).label,
          longer=longer.label, shorter=shorter.label, weapon_A=A.weapon, weapon_B=B.weapon,
          reach_A=round(erA,2), reach_B=round(erB,2), measure_gap=round(measure_gap,2), closed=closed)
    while beats < soft*3:
        beats+=1
        # CONDITIONAL TEMPO (correction 2): recompute each beat with current fatigue — grip/stance/fatigue change
        # cadence; it is not a static weapon property. Approach uses general cadence; closed uses close-cadence.
        ffat={A:max(0.0,1-A.stamina/max(1,A.stamina_max)), B:max(0.0,1-B.stamina/max(1,B.stamina_max))}
        # INITIATIVE DECAY (damper) — per-tradition HOLD: high measure (destreza) decays slower, holding the Vor longer.
        A.initiative=S.clamp_initiative(A.initiative*S.init_hold_decay(A,cfg,TR), cfg)
        B.initiative=S.clamp_initiative(B.initiative*S.init_hold_decay(B,cfg,TR), cfg)
        # DISPOSITION (initiative lever): aggressive temperament drifts the Vor UP (pressing builds Vor), cautious DOWN
        # (cedes it) — the standing pressure that makes both poles cost. Neutral (lean 0) = no drift; bounded by clamp.
        A.initiative=S.clamp_initiative(A.initiative + cfg['DISP_INIT_K']*S.disp_lean(A), cfg)
        B.initiative=S.clamp_initiative(B.initiative + cfg['DISP_INIT_K']*S.disp_lean(B), cfg)
        # STRUCTURE recovery (the kuzushi damper): balance regathers toward 1.0 each beat.
        A.poise=S.clamp_poise(S.poise_regen(A,cfg), cfg)   # Focus speeds structure recovery (Jordan 2026-06-03); regen formula -> systems.poise_regen
        B.poise=S.clamp_poise(S.poise_regen(B,cfg), cfg)
        for c in (A,B):
            c.grip_position=S.grip_target(c, closed, cfg)   # GRIP/STANCE (The Approach): a closing pole GATHERS IN (grip_position 0->1) to fight the close; else 0 (full reach). CONTINUOUS, derived. The lunge is set at the attack below.
            c.lunge_depth=0.0                                # reset the body-extension each beat; a deep thrust re-sets it below
            opp = B if c is A else A
            c.sel_dmg, c.sel_head, c.sel_gap, c.sel_perc, c.sel_pc = S.select_mode(c, opp.armor, closed, cfg)   # USE-MODE: greedily pick the afforded head with the best damage-coupling vs the opponent's armour (a weapon that affords >1 mode, e.g. the poleaxe's blunt+spike, shifts with armour). Per-beat, DERIVED, pure; the wrapper owns the mutation (mirrors grip_position). Widened I2/D2b to the 5-tuple (sel_gap/sel_perc/sel_pc — R-7/capstone M2): the SELECTED element's own gap/percussion/point_concentration, the canonical source for core.strike/adef_cap/D5's arc-vs-thrust (M-02). Refreshed after the half-sword form-switch below.
            er[c]=S.reach_base(c,cfg)   # er REFRESH #1 (I3, D3, two-recompute contract — designs/audit/2026-07-02-scene-combat-closing-distance-redesign/): re-derives ONLY er[c] on the grip-aware CURRENT (pre-swap) form; NEVER measure_gap (the running approach decrement, below) or `closed` (latched); longer/shorter LABELS stay frozen at engagement start (JD-2 plan default). Feeds reopen (below) and close_tempo/tempo (next line) via reach-derived close_unwieldiness.
        if not closed: rate={c:S.weapon_tempo(c,cfg,ffat[c]) for c in (A,B)}
        else:          rate={c:S.close_tempo(c,cfg,ffat[c]) for c in (A,B)}
        for c in (A,B): ready[c]+=rate[c]
        # REACH RE-OPENING (corrections: a created moment, not just balance+reach). The longer weapon can make
        # distance only when a MOMENT exists — the opponent over-committed (must recover balance), OR the longer
        # weapon won a defensive maneuver last exchange (bind/parry/deflect created the gap), OR it frees a hand to
        # shove (grappling-manual one-handed push at reach). Identifying the moment needs READING; executing the
        # withdrawal needs FOOTWORK; and the attempt is READABLE — the shorter weapon's own read can deny it.
        if closed and beats>1 and reopen_moment:
            base_gap=er[longer]-er[shorter]
            if base_gap>0.3 and rng.random()<S.reopen_prob(longer, shorter, base_gap, ffat[longer], push_avail, cfg, TR)*S.reach_threat(longer, shorter, cfg):
                closed=False; measure_gap=base_gap; ready={A:0.0,B:0.0}
                reopen_moment=False; push_avail=False
                continue
        reopen_moment=False; push_avail=False   # the moment is fleeting; consumed/expires each beat unless re-created below (RR-01: push_avail no longer carries across beats)
        # ----- APPROACH: longer weapon threatens (stop-hits) while shorter closes -----
        if not closed:
            rt = S.reach_threat(longer, shorter, cfg)               # FIX-1: a long weapon that can't defeat the closer's armour loses its reach edge (1.0 unarmoured by construction)
            displ = S.approach_displace(shorter, longer, cfg)        # lever-arm: set aside a thrusting point on approach
            close_rate=S.close_rate(shorter, ffat[shorter], displ, rt, cfg)   # TA-02 fatigued closer + displace point + walk through un-threatening reach (FIX-1); assembled in systems.close_rate
            measure_gap=max(0.0, measure_gap-close_rate)
            just_closed = (measure_gap<=0.3)
            if just_closed:
                closed=True; ready={A:0.0,B:0.0}   # reset readiness: closed phase starts fair (no banked approach tempo)
            stophit_p = cfg['STOPHIT_CHANCE'] * min(1.0, measure_gap/cfg['STOPHIT_FULL_GAP']) * (1-displ) * rt  # FIX-1: a stop-hit that can't pierce the armour deters less
            _emit('approach', beat=beats, shorter=shorter.label, longer=longer.label, gap=round(measure_gap,2),
                  close_rate=round(close_rate,3), just_closed=just_closed, stophit_p=round(stophit_p,3))
            if rng.random() < stophit_p:
                pool=max(1, core.resolution_pool(longer.history))
                nsig=S.stophit_sigma(longer, shorter, measure_gap, cfg)
                deg, net = core.resolve(pool, nsig, rng)
                _emit('stophit', longer=longer.label, shorter=shorter.label, gap=round(measure_gap,2),
                      pool=pool, net_sigma=round(nsig,3), net=round(net,2), degree=deg)
                if deg in ('success','overwhelming'):
                    d=core.strike(longer, shorter, deg, False, cfg, net=net, pool=pool)
                    shorter.apply_wound(d); shorter.conc=max(0,shorter.conc-cfg['CONC_DRAIN_HIT'])
                    if shorter.felled: return shorter
            if not closed:
                if A.stamina<=-4 or B.stamina<=-4: _emit('separation', reason='collapse'); return None
                continue
        # ----- CLOSED: tempo-gated exchange -----
        actors=[c for c in (A,B) if ready[c]>=cfg['ACT_THRESHOLD']]
        if not actors: continue
        if len(actors)==2:
            aggressor = max(actors, key=lambda c: ready[c]) if ready[A]!=ready[B] else actors[rng.randrange(2)]   # stdlib uniform int (ED-1085)
        else:
            aggressor = actors[0]
        defender = B if aggressor is A else A
        _agg0=aggressor.label; _def0=defender.label   # frozen for the outcome emit (roles may flip on riposte)
        # half-sword auto-switch (mit dem kurzen Schwert): adopt the form fitting the current range/armour
        aggressor.weapon = S.halfsword_target(aggressor, closed, defender.armor)   # wrapper owns the mutation
        defender.weapon  = S.halfsword_target(defender, closed, aggressor.armor)
        # re-select the use-mode on the (possibly just-switched) form, so sel_* match the current weapon (I2/D2b:
        # BOTH call sites must write all five sel_* fields — c.w flips at :120 above, so a partial thread would
        # leave a post-swap c.w resolved against a pre-swap-selected element, the same object-confusion bug R-7
        # closed for select_mode's own return).
        aggressor.sel_dmg, aggressor.sel_head, aggressor.sel_gap, aggressor.sel_perc, aggressor.sel_pc = S.select_mode(aggressor, defender.armor, closed, cfg)
        defender.sel_dmg,  defender.sel_head,  defender.sel_gap,  defender.sel_perc,  defender.sel_pc  = S.select_mode(defender, aggressor.armor, closed, cfg)
        er[aggressor]=S.reach_base(aggressor,cfg); er[defender]=S.reach_base(defender,cfg)   # er REFRESH #2 (I3, D3): re-derives er for aggressor/defender on the grip+FORM-aware POST-SWAP weapon — so a half-sworded longsword reads its shorter reach everywhere in the closed exchange (reach_sigma below), not the frozen pre-swap #1 value. Consistency-proven: at open measure (grip=0, no swap) this equals #1 exactly.
        ready[aggressor]-=cfg['ACT_THRESHOLD']
        # COMMIT DEPTH — disposition lean + wariness skew a Beta over [2,5] (the commitment-recovery spectrum). The
        # draw + skew live in systems.commit_depth; the wrapper just sequences it and emits (orchestrator owns no formula).
        commit, _ba, _bb, _ln = S.commit_depth(aggressor, defender, cfg, rng, TR)
        _emit('commit', aggressor=_agg0, defender=_def0, commit=round(commit,2), beta_a=round(_ba,3), beta_b=round(_bb,3), stance_lean=round(_ln,3))
        if commit>=cfg['LUNGE_COMMIT'] and rng.random() < S.lunge_quality(aggressor, cfg):
            aggressor.lunge_depth = min(1.0, (commit-cfg['LUNGE_COMMIT'])/cfg['LUNGE_DEPTH_SCALE'])   # a deep thrust BECOMES a lunge (gated stochastically by lunge_quality: rapier readily, a cutter never) — its DEPTH scales with commit (CONTINUOUS); the extended body -> lower recovery (recoverability_factor) + more readable (legibility)
        aggressor.stamina-=S.act_cost(aggressor,commit,cfg)
        ready[aggressor]-=cfg['RECOVERY_TEMPO_K']*(commit-2.0)*S.recoverability_factor(aggressor,cfg)   # TEMPO is coupled to RECOVERY: a deep, hard-to-recover commit (a heavy or lunged blow) leaves you SLOWER to act again — the next action waits on the recovery; a feint (commit~2, full recovery) costs no tempo. Non-linear in weight via recoverability_factor.
        oob=cfg['OOB'] if aggressor.stamina<=0 else 0
        fat_a=max(0.0,1-aggressor.stamina/max(1,aggressor.stamina_max)); fat_d=max(0.0,1-defender.stamina/max(1,defender.stamina_max))
        # concentration: mental-fatigue protection (fatigue-resistance) — defender's reading/technique (systems.mental_fatigue)
        mental_fat_d=S.mental_fatigue(defender, fat_d, cfg)
        # tradition channel-weights (cognitive-mode biases over the shared substrate; neutral=1.0)
        ta=aggressor.tradition; td=defender.tradition
        # standing reach advantage (module): defender's reach lowers the attacker's net, falling with armour.
        reach_pen=S.reach_sigma(aggressor, defender, er, fat_a, fat_d, cfg, TR)
        # tempo emphasis (commitment-window exploitation): re-weights the aggressor's initiative
        init=S.init_emphasis_sigma(aggressor, defender, cfg, TR)   # tempo(Agi)+reading(Cog/Att)+experience(History), tempo-weighted (systems.init_emphasis_sigma)
        consistency_a=S.consistency(aggressor, cfg)   # Concentration tracker (3F+2S, depletes), not static Focus (Jordan #12)
        # FEINT DISSOLVED INTO THE ATTACK (WS-5): there is no separate feint maneuver. Deception is intrinsic to
        # HOW one attacks — the micro-read carried by commit-depth, head, grip and disguise — already modelled by
        # legibility() + the read contest below (the soccer-stepover principle: twitching the body/blade IS part of
        # attacking). Removes the old feint_eval double-machinery and its streak/triple-debuff bugs (RF-01/04).
        # VISUAL read (pre-contact anticipation; temporal-spatial). Weighted by tradition's visual emphasis, DEGRADED
        # vs an unfamiliar aggressor (knowledge-of-others), and MODULATED BY MOVEMENT LEGIBILITY (correction 4):
        # large/lateral movement is easier to perceive than in-line motion. A thrust (in-line, point/high-gap) is
        # HARD to read; a swing/cut (lateral arc) is EASY; and a deeper commit / lunge = more biomechanical action =
        # more readable. So the defender's read rises vs swings/lunges and falls vs thrusts.
        # READ CONTEST + mode selection — computed in systems.read_contest; the wrapper sequences + emits.
        _rc=S.read_contest(aggressor, defender, commit, consistency_a, mental_fat_d, fat_d, cfg, rng, TR)
        read_win=_rc['read_win']; read_d=_rc['read_d']; read_a=_rc['read_a']; mode=_rc['mode']; msig=_rc['msig']
        _emit('read', defender=_def0, read_d=round(read_d,3), read_a=round(read_a,3),
              p_read_win=round(_rc['p_read'],3), read_win=read_win)
        _emit('mode', defender=_def0, mode=mode, msig={m:round(v,3) for m,v in msig.items()}, chosen_by=('read' if read_win else 'random'))
        # poise (balance disruption) now reaches defence through its balance components (dodge mode_sigma, stance_stability)
        # via balance_eff — no separate blanket multiply here (would double-count the stance term).
        # net-σ ASSEMBLY — the wrapper SEQUENCES the contributions; systems owns the arithmetic (no formula in the orchestrator).
        dsig=S.defence_sigma(defender, msig[mode], mental_fat_d, fat_d, cfg)   # WS-5: feint_debuff removed (feint dissolved into the attack)
        atk_sig=S.attack_sigma(aggressor, commit, init, oob, fat_a, consistency_a, cfg)
        adef=S.armor_defeat_sigma(aggressor, defender, cfg)   # armour-defeat capability controls armoured exchanges
        init_edge=S.initiative_sigma(aggressor, defender, cfg)  # the Vor edge (bounded; +ve if aggressor holds initiative)
        net_sigma=S.assemble_net_sigma(atk_sig, dsig, reach_pen, adef, init_edge, aggressor, defender, cfg)
        # INDES / sen-no-sen STEAL (forced-to-Nach by READING): a defender who out-read a deeply-committed aggressor
        # steals the Vor. Per-tradition: in a bind (winding) German tactile+leverage steals hardest; open, Italian tempo.
        # INDES STEAL — systems computes the steal AMOUNT + the counter selection; the wrapper APPLIES the mutation.
        counter_attempt=False
        if read_win and commit>=4:
            steal=S.indes_steal_amount(defender, mode=='wind', commit, read_d, read_a, cfg, TR)
            defender.initiative=S.clamp_initiative(defender.initiative+steal, cfg)
            aggressor.initiative=S.clamp_initiative(aggressor.initiative-steal, cfg)
            counter_attempt=S.counter_select(defender, cfg, rng, TR)
        pool=max(1, core.resolution_pool(aggressor.history))
        deg, net = core.resolve(pool, net_sigma, rng)
        _emit('roll', aggressor=_agg0, pool=pool, net_sigma=round(net_sigma,3), net=round(net,2), degree=deg, mode=mode)
        close = closed   # C-1: per-beat close-coupling follows the engagement measure-state (not raw reach alone)
        # OVERCOMMIT EXPOSURE — systems computes it; the wrapper applies the initiative/poise loss.
        overcommit_exposure = S.overcommit_exposure(aggressor, commit, fat_a, cfg, TR)
        # forced-to-Nach by losing BALANCE/grip — per-tradition: tempo-disciplined (English true-times) lose less grip.
        if overcommit_exposure>0:
            aggressor.initiative=S.clamp_initiative(aggressor.initiative - S.init_overcommit_loss(aggressor,overcommit_exposure,cfg,TR), cfg)
            aggressor.poise=S.clamp_poise(aggressor.poise - cfg['POISE_BREAK_OVERCOMMIT']*overcommit_exposure, cfg)  # overextended = off-balance
        # ----- outcome mapping (deg = AGGRESSOR's degree; defender mode can neutralize) -----
        hit=0; riposte=False; bind=False
        # neutralize is a FIXED mode-shape (parry deflects / dodge voids / wind binds) — NOT re-scaled by dsig,
        # which already shaped the roll via net_sigma (audit C-2: avoid double-counting defender skill).
        neutralize=cfg['NEUTRALIZE_PARRY'] if mode=='parry' else (cfg['NEUTRALIZE_DODGE'] if mode=='dodge' else cfg['NEUTRALIZE_WIND'])
        if deg=='fail':
            riposte=(rng.random() < min(0.95, cfg['RIPOSTE_ON_FAIL']+overcommit_exposure))
        elif deg=='partial':
            if mode=='dodge': hit=core.strike(aggressor, defender, 'graze', close, cfg) if rng.random()<cfg['PARTIAL_DODGE_GRAZE'] else 0
            elif mode=='parry': hit=core.strike(aggressor, defender, 'graze', close, cfg) if rng.random()<cfg['PARTIAL_PARRY_GRAZE'] else 0
            else: bind=True
        elif deg=='success':
            if mode=='wind' and rng.random()<cfg['WIND_BIND_P']: bind=True
            elif rng.random()<neutralize: riposte=(rng.random() < min(0.95, cfg['RIPOSTE_ON_NEUTRALIZE']+overcommit_exposure))
            else: hit=core.strike(aggressor, defender, 'success', close, cfg)
        else:
            if rng.random()<max(0.0,neutralize-cfg['NEUTRALIZE_OVERWHELM_DROP']): hit=0
            else: hit=core.strike(aggressor, defender, 'overwhelming', close, cfg, net=net, pool=pool)
        if counter_attempt:
            # SUCCESS scales with training (history) + reflex; the untrained single-time counter mostly fails — a
            # desperate-idiot move. Tradition abilities will modulate this upward (added later). (systems.counter_success_prob)
            if rng.random() < S.counter_success_prob(defender, cfg, TR):
                hit=0; bind=False; riposte=True            # LANDS: committed attack voided in-tempo, defender ripostes (keeps the seized Vor)
            else:
                # MISS: the botched counter cedes the seized Vor and leaves the defender eating the attack UNDEFENDED
                # (no mode reduction); the hit-block below then applies the wound + further Vor/poise loss — the downside.
                defender.initiative=S.clamp_initiative(defender.initiative-steal, cfg)
                aggressor.initiative=S.clamp_initiative(aggressor.initiative+steal, cfg)
                bind=False; riposte=False
                hit=core.strike(aggressor, defender, 'overwhelming' if deg=='overwhelming' else 'success', close, cfg, net=net, pool=pool) if deg in ('partial','success','overwhelming') else 0
        if cfg.get('IMPOSITION_GATE'):   # WS-4/WS-5 section-C experiment (flag, default off): tradition imposes/refuses its node
            bind, riposte = S.impose_node(aggressor, defender, hit, bind, riposte, cfg, rng, TR)
        sim=(hit>0 and riposte)
        # DISPLACE-AND-STEP-INSIDE (manual technique): a COMMITTED THRUST (point head, deep commit) is exploitable by
        # TWO DISTINCT routes on DISTINCT primitives (M3 decoupling — the two were conflated under bind-leverage, so
        # the leverage re-grounding wrongly suppressed the short-fighter counter):
        #   (a) BEAT IT ASIDE — a strong-LEVERAGE weapon (poleaxe/staff/long-grip) sets the point offline with grip+mass.
        #   (b) SLIP INSIDE — a SHORTER, quicker fighter ducks inside the over-extended point: the close-fighter's
        #       canonical answer to a thrust (the dagger inside the rapier lunge). Driven by REACH (being shorter = having
        #       inside to step into) + REFLEX, NOT leverage. [Phase-5 contact axis elaborates this into the close.]
        # Either route needs the defender to win the read (gated) + the thruster committed deep; the thruster's
        # pull-back/recovery can still graze (commitment=recovery: the deep thrust IS the exposure).
        beat_aside  = S.leverage(defender,cfg) > S.leverage(aggressor,cfg)+cfg['DISPLACE_LEV_GAP']
        slip_inside = (S.reach_base(defender,cfg) < S.reach_base(aggressor,cfg)
                       and S.reflex(defender,cfg) >= S.reflex(aggressor,cfg))
        if (aggressor.w['head']=='point' and commit>=4 and not hit and read_win and (beat_aside or slip_inside)):
            if rng.random() < cfg['DISPLACE_P']:
                if not closed: closed=True; measure_gap=0.0; ready={A:0.0,B:0.0}
                # pull-back of the committed thrust can still graze the closing defender
                if rng.random() < cfg['DISPLACE_PULLBACK_GRAZE']:
                    d=core.strike(aggressor, defender, 'graze', False, cfg)
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
            # forced-to-Nach by DAMAGE: the aggressor presses the advantage (gains the Vor); the struck defender loses it.
            aggressor.initiative=S.clamp_initiative(aggressor.initiative+cfg['INIT_GAIN_HIT'], cfg)
            defender.initiative=S.clamp_initiative(defender.initiative-cfg['INIT_LOSS_WOUNDED'], cfg)
            defender.poise=S.clamp_poise(defender.poise - cfg['POISE_BREAK_HIT']*min(1.0, hit/cfg['POISE_SOLID_HIT']), cfg)  # solid blows stagger; chip damage barely
            if defender.felled: return defender
        if bind:
            # German Fühlen / Stärke-Schwäche: whoever DOMINATES the bind (bind_sigma sign) steals the Vor through the
            # contact — once, at bind entry, scaled by their tactile+leverage. Not gated on the visual read.
            bsig0 = S.bind_sigma(aggressor, defender, cfg, TR)
            bw, bl = (aggressor, defender) if bsig0>=0 else (defender, aggressor)
            g=cfg['INIT_STEAL_INDES']*S.init_steal_factor(bw, True, cfg, TR)
            bw.initiative=S.clamp_initiative(bw.initiative+g, cfg)
            bl.initiative=S.clamp_initiative(bl.initiative-g, cfg)
            # KUZUSHI: the bind winner breaks the loser's balance through the bind, scaled by leverage (Stärke-Schwäche).
            bl.poise=S.clamp_poise(bl.poise - cfg['POISE_BREAK_BIND']*TR.eff_cw(bw,'leverage'), cfg)
            for _ in range(3):
                beats+=1
                bsig = S.bind_sigma(aggressor, defender, cfg, TR)   # module: leverage + tactile (Fuhlen), Str minor
                if rng.random() < S.bind_dominance_p(bsig):
                    if rng.random()<cfg['BIND_HIT_P']:
                        d=core.strike(aggressor, defender, 'success', close, cfg)
                        defender.apply_wound(d); defender.conc=max(0,defender.conc-cfg['CONC_DRAIN_HIT'])
                        if defender.felled: return defender
                        break
                else: riposte=True; break
        if riposte:
            if sim:
                # concentration disruption-resistance: focus lets aggressor still complete despite the blow
                if rng.random() > S.disrupt_resist_p(aggressor, cfg):
                    d=core.strike(defender, aggressor, 'graze', close, cfg)
                    aggressor.apply_wound(d); aggressor.conc=max(0,aggressor.conc-cfg['CONC_DRAIN_HIT'])
                    if aggressor.felled: return aggressor
            defender.conc=max(0,defender.conc-cfg['CONC_DRAIN_LOSS'])
            aggressor, defender = defender, aggressor   # role flip — objects, frame-safe
        _emit('outcome', aggressor=_agg0, defender=_def0, mode=mode, degree=deg,
              hit=int(hit), bind=bool(bind), riposte=bool(riposte),
              A_wounds=A.wt.wounds, B_wounds=B.wt.wounds, A_felled=A.felled, B_felled=B.felled)
        exchanges+=1
        # TURN = one approach -> burst -> separation (Jordan 2026-06-03). The burst is a SMALL EMERGENT run of
        # exchanges, gated by TEMPO (who re-reaches ACT_THRESHOLD via close_tempo), NOT by ripostes: a faster fighter
        # can land SEVERAL hits in a single turn with no reply. It ends when (a) the ceiling BURST_MAX is reached, or
        # (b) an exchange resolves CLEANLY on defence -- a dodge/parry/miss with no hit, no riposte, no bind -- so the
        # measure breaks (the floor: one swing, one dodge, separate = 1 exchange). A landed hit, a riposte (role flip),
        # or a bind CONTINUES the pressing. Felling / stamina-collapse exits are handled above. Combat = many such
        # turns; wounds persist across them, so equal fighters take several turns to resolve (emergent, not enforced).
        if A.stamina<=-4 or B.stamina<=-4: _emit('separation', reason='collapse'); return None
        if exchanges >= cfg['BURST_MAX']: _emit('separation', reason='burst_ceiling'); return None
        if not (hit>0 or riposte or bind): _emit('separation', reason='clean_defence'); return None
    _emit('separation', reason='beat_exhaustion'); return None

def fight(A, B, cfg=None, rng=None, max_bouts=12):
    import random
    cfg=cfg or CFG; rng=rng or random.Random()   # stdlib RNG (ED-1085 numpy de-leak; pass random.Random(seed) for determinism)
    # reset wounds — must mirror Combatant.__init__'s tracker construction (combatant.py:71). WoundTracker.__init__
    # defaults spirit=3/strength=4, so re-init'ing with end alone silently reverts non-default fighters to those
    # defaults — corrupting wi, health_full, and every derived health value from bout 2 onward. Pass spirit/strength.
    A.wt.__init__(A.end, spirit=A.spirit, strength=A.strength); B.wt.__init__(B.end, spirit=B.spirit, strength=B.strength)
    _init_live(A,cfg); _init_live(B,cfg)
    _emit('fight_start', A=A.label, B=B.label, weapon_A=A.weapon, weapon_B=B.weapon,
          armor_A=A.armor, armor_B=B.armor, tradition_A=A.tradition, tradition_B=B.tradition)
    result=0
    for turn in range(max_bouts):   # each iteration = ONE engagement (~10s turn); victor emerges over MULTIPLE turns with persistent wounds/fatigue. fight() is the multi-turn SIM harness (runs to a decision for win-rates); the GAME calls one engagement per turn.
        first = A if rng.random()<0.5 else B
        _emit('turn_start', turn=turn+1, first=first.label)
        loser = engagement(A,B,first,cfg,rng)
        _emit('engagement_end', turn=turn+1, felled=(loser.label if loser is not None else None))
        if loser is not None:
            result = -1 if loser is A else 1   # +1 => A won
            break
        for c in (A,B):
            c.stamina=min(c.stamina_max, c.stamina+cfg['RECOVERY_FRAC']*(c.stamina_max-c.stamina)*(c.stamina_max/cfg['STAMINA_REF']))
            c.conc=max(0,min(c.conc_max, c.conc-cfg['CONC_DRAIN_BOUT']+cfg['CONC_RECOVER_FRAC']*(c.conc_max-c.conc)))
    # NO automatic tiebreak (Jordan 2026-06-02): if neither fighter is felled, the round ends UNRESOLVED (result 0).
    # We do not foreclose by awarding the round on wound-count — an undecided fight is a legitimate outcome.
    # 95% cap (videogame rule): no matchup is ever certain. With probability UPSET_FLOOR, the decided LOSER steals
    # the win — a "lucky blow"/critical-opening that the model otherwise suppresses. Applied only to decided fights,
    # symmetric in form, so an X% raw win-rate is clamped toward [UPSET_FLOOR, 1-UPSET_FLOOR].
    if result!=0 and rng.random()<cfg['UPSET_FLOOR']:
        result = -result
    _emit('fight_result', result=result, winner=(A.label if result==1 else B.label if result==-1 else None))
    return result
