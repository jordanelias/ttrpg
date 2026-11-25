"""wrapper.py — the personal-combat engine's orchestrator: `fight(A, B, ...)` runs a scene of up to `max_bouts`
engagements and returns +1 / -1 / 0 (A won / B won / unresolved); `engagement(...)` is one burst of beats inside it.
Inputs: two `combatant.Combatant` objects, `config.CFG` (or a `cfg` passed in) and the caller's `rng`; the host
reaches it through `fight.py`. Here `engagement`
assigns aggressor/defender ONCE per beat and passes Combatant objects to every subsystem (`combat_systems`, `core`,
`contact`, `tradition`), the structural cure for the role-inversion bug class: nothing ever indexes raw 'A'/'B'."""
import math
from types import SimpleNamespace
from engine.dice_engine import draw as KD   # the one keyed draw (`H2`, `seeded`): the per-blow coverage-gap draw below forms its key from the fight's own
from . import core, combat_systems as S, tradition as TR, contact as CT, attributes as ATTR
from . import vocabulary as V   # the token ALPHABET, owned once (ED-PC-0042)
from .config import CFG

# ── TRACE SEAM (workbench / branch-explorer hook) ──────────────────────────────────────────────
# _TRACE is None by default: every _emit() is a single is-None check, so the seam adds ~zero cost
# and CANNOT change behavior (no rng draw, no state mutation). `fight(..., trace=f)` binds _TRACE to the
# callable(event: dict) for the call and restores it after, so no caller assigns the module attribute (B14.11). Events carry the INPUTS each decision
# node consumed (read margins, the commit distribution, the roll's pool/net_sigma) so the narrator and
# the branch explorer can reconstruct the local probability of every alternate branch without re-deriving
# engine internals. The engine emits facts; probability math lives in the workbench (probabilities.py).
_TRACE = None
def _emit(kind, **data):
    if _TRACE is not None:
        _TRACE(dict(kind=kind, **data))

def _wound(source, by, victim, damage, bare=None):
    """The ONE damage site (PC-13): `victim.apply_wound(damage)` plus the `wound` trace event, nothing else. The event
    carries the APPLIED amount (`int(damage)`; the tracker adds `max(0, int(d))` and `apply_wound` skips `d <= 0`), so
    `sum(wound.damage per victim)` within one fight() is the tracker's `cumulative_damage` (fight() zeroes the
    tracker's damage at its start). `source` names the site (pursuit, stophit,
    displace_graze, exchange, bind); `by` is the striker. `bare` is the blow's coverage-gap draw (`core.bare_zone`: True a bare
    zone, False the harness, None no draw: against `none`); the event carries it as `bare: bool`. Draws nothing and keeps no
    state: concentration drain, stagger and every other per-site effect stay at their sites."""
    victim.apply_wound(damage)
    if _TRACE is not None and int(damage) > 0:
        _emit('wound', by=by.label, victim=victim.label, damage=int(damage), source=source,
              wounds=victim.wt.wounds, cumulative=victim.wt.cumulative_damage, felled=bool(victim.felled), bare=bare is True)

def _emit_outcome(agg0, def0, mode, deg, hit, bind, riposte, A, B):
    """The exchange's `outcome` event, emitted on the normal tail AND before each felling `return` in the exchange (PC-13)."""
    _emit('outcome', aggressor=agg0, defender=def0, mode=mode, degree=deg,
          hit=int(hit), bind=bool(bind), riposte=bool(riposte),
          A_wounds=A.wt.wounds, B_wounds=B.wt.wounds, A_felled=A.felled, B_felled=B.felled)

def _init_live(c, cfg):
    c.rederive(cfg)                      # the combatant re-derives its figures from its attributes (PC-14; keeps damage)
    c.stamina=float(c.stamina_max)       # reset live state from the combatant's own held maxima
    c.conc=c.conc_max
    c.initiative=0.0
    c.poise=1.0

def _select(c, opp, closed, cfg, measure_gap):
    """The ONE write of `S.select_mode`'s record onto `c` (the wrapper owns the mutation): the six `sel_*` fields by NAME (ED-PC-0042/I3),
    then the selected element's per-arm magnitudes (ED-PC-0037.1). Called at every beat's head AND after the half-sword swap: a partial
    thread leaves a post-swap `c.w` resolved against a pre-swap-selected element (R-7's object confusion)."""
    _sel = S.select_mode(c, opp.armor, closed, cfg, measure_gap=measure_gap)
    c.sel_dmg, c.sel_head, c.sel_gap, c.sel_perc, c.sel_pc, c.sel_eff = _sel.dm, _sel.head, _sel.gap, _sel.perc, _sel.pc, _sel.eff
    c.sel_eff_cut, c.sel_eff_thrust = S.selected_arm_magnitudes(c, c.sel_head, cfg)

def _carry(ready, cfg):
    """Phase-transition readiness: keep each fighter's RESIDUAL cadence phase, drop any banked whole action.

    [ED-PC-0037, F16] A hard zero of `ready` would RE-SYNCHRONISE the cadence race, and a synchronised race is won by
    the same fighter every single time, so a weapon with a 1.5% tempo edge would act FIRST always — a 2:1 action
    economy. Keeping the residual (ready mod ACT_THRESHOLD) means nobody carries a free completed action across the
    transition, while each fighter stays where their own cadence actually left them.
    A fighter mid-recovery when the measure closes is genuinely a beat behind one who had just recovered."""
    # [ED-PC-0037.1] max(0.0, r) BEFORE the modulo. Python's `%` maps a NEGATIVE readiness — recovery DEBT, which
    # overcommit can drive deeply negative (recoverability_factor spans 0.3-67.8) — onto a near-CREDIT: -1.0 % 2.5 = 1.5,
    # which would grant the most over-committed fighter a banked action at a phase transition and invert this
    # function's own contract ('a fighter mid-recovery is genuinely a beat behind'). Debt clamps to 0 — no banked
    # action, and no free one either.
    return {c: (max(0.0, r) % cfg['ACT_THRESHOLD']) for c, r in ready.items()}

def _pool_dice(c, cfg, addends=None):
    """THE POOL A COMBATANT ROLLS (B05.57, `UPR` §2 edit 3): `core.resolution_pool(c.score, c.pool_addends, add, floor)` at the
    three roll sites (the pursuit, the stop-hit, the exchange). `c.score` is his skill score; `c.pool_addends` his registered
    pool addends, set by the module entry (a `Combatant` built by the workbench has none and reads 0). `add` and `floor` are the
    record's `pool_add` and `pool_floor` when the entry carried them in `cfg` as `BASE_POOL` and `POOL_FLOOR`, else the owner's
    own defaults (the bounds are read nowhere else, so this spells no pool constant). `addends` overrides his registered ones
    (the yield roll (B15.10) takes none: the addends are the verb's, the roll is not a blow)."""
    kw = {k: cfg[name] for k, name in (("add", "BASE_POOL"), ("floor", "POOL_FLOOR")) if name in cfg}
    return core.resolution_pool(c.score, getattr(c, "pool_addends", 0) if addends is None else addends, **kw)


def engagement(A, B, first, cfg, rng, prev_closed=False, terms=None, turn=1, scene=0):
    """One round (A-101): the two close, exchange attempts to attack, and separate. `first` is the initiating Combatant
    object. `prev_closed` is the measure state the PREVIOUS engagement ended in (see the re-presentation gate below).
    Returns (felled Combatant or None, ended_closed, ended_by) — the second element threads forward as the next
    engagement's prev_closed; the third is how the round ended, a member of `vocabulary.ROUND_ENDS` ('felled' at each
    felling, else the reason of the `separation` event it emitted). A and B are fixed
    objects throughout — never swapped. `terms` is `fight`'s non-lethal duel terms (RS-25), or None under lethal
    ones: when set, the burst ends at the first beat that opens with `_terms_met` true, and `fight` reads the stop.
    `turn` is this round's index in the fight (1-based, the `turn_start` count) and `scene` the fight's `rng.n` where it began:
    with the blow's index within the round they key the coverage-gap draw of each landed blow (`_strike`)."""
    blow = 0
    def _strike(attacker, defender, deg, **kw):
        """`core.strike` with the blow's keyed coverage-gap draw (PC_D, A-30). Returns (damage, bare) for the caller to carry to
        `_wound`. The key is a sub-key of the fight's own `Draw`, `H2(rng.key, "gap:<scene>:<turn>:<blow>")`: a function of the
        fight's key and the blow's place in it, never of how many uniforms the stream has taken, so an unrelated draw added
        elsewhere does not move which blows find a bare zone. A defender in no armour takes no draw (`core.bare_zone`)."""
        nonlocal blow
        blow += 1
        bare = core.bare_zone(KD.seeded(KD.H2(rng.key, f"gap:{scene}:{turn}:{blow}")), defender.armor)
        return core.strike(attacker, defender, deg, cfg, bare=bare, **kw), bare
    drawn = False   # the round's one riposte draw is taken: a second felling in the same round (a counter's own) is final
    def _land(source, by, victim, d, bare=None):
        """`_wound` for a blow that may FELL: the ONE site of the riposte (`18_DET`, B15.09). A blow that would fell `victim` (his
        damage after it reaches his Health: a pure read of the tracker, nothing applied yet) draws once, before his tracker is
        final: a sub-key of the fight's own `Draw`, `H2(rng.key, "upset:<scene>:<round>")` (B15.05's form: a function of the fight's
        key and the round, never of how many uniforms the stream has taken, so it consumes no position of it). With probability
        `cfg['UPSET_FLOOR']` the blow is TURNED: it is not applied, so his tracker stays as it stood immediately before it (the felling
        undone, and every reader of the trace still sees the tracker as the sum of its `wound` events), `finalblow_riposte` is emitted,
        and he lands the damage the blow carried back on the striker through `_wound` (source `finalblow_riposte`). The fight goes on
        from that state, and the counter may itself fell. One draw a round: the key names the round, so a felling after a turned one in
        the same round (a counter's) is final and draws nothing.
        `source` names the site, as `_wound`'s does."""
        nonlocal drawn
        wt = victim.wt
        if not drawn and int(d) > 0 and wt.cumulative_damage + int(d) >= wt.health_full:
            drawn = True
            if KD.seeded(KD.H2(rng.key, f"upset:{scene}:{turn}")).random() < cfg['UPSET_FLOOR']:
                _emit('finalblow_riposte', round=turn, by=victim.label, source=source)
                _wound('finalblow_riposte', victim, by, d)
                return
        _wound(source, by, victim, d, bare)
    def _down():
        """The party the burst has felled, or None: after `_land` it is the victim, or the striker his counter felled."""
        return A if A.felled else B if B.felled else None
    aggressor = first; defender = B if first is A else A
    # OPEN-MEASURE RESET (ED-PC-0033): a NEW engagement begins at open measure — weapons at full extension, no lunge
    # committed. The per-beat transient geometry (grip_position, lunge_depth) is otherwise carried on the Combatant
    # object from the PRIOR engagement's final beat; without this reset a weapon that ended the last engagement choked
    # in (grip_position≈1) would UNDER-READ its own reach at THIS engagement's opening reach_base — corrupting the
    # frozen longer/shorter labels and measure_gap for the whole new engagement. Reset before the reach_base below so
    # the opening geometry is the honest open-measure one (grip_target re-derives per-beat inside the loop anyway).
    for c in (A, B):
        c.grip_position = 0.0; c.lunge_depth = 0.0
        c.weapon = S.base_form(c)   # B14.13 (F-PC-16): the half-sword form is the same kind of state; it is re-taken at the first closed exchange that calls for it
    erA=S.reach_base(A,cfg); erB=S.reach_base(B,cfg)
    er={A:erA, B:erB}
    # FAIRNESS: on EXACTLY equal reach the longer/shorter label is a coin-flip — not always A. The label feeds the
    # reopen-moment logic, so always-A on ties put a latent bias into every same-reach matchup (mirrors, armour, stat
    # matchups), which the attacker-favouring mechanics amplified. Different reach is deterministic as before.
    longer = A if erA>erB else (B if erB>erA else (A if rng.random()<0.5 else B)); shorter = B if longer is A else A
    measure_gap=max(0.0, er[longer]-er[shorter])
    # SOFT CLOSED-LATCH (ED-PC-0037, F17). A hard step `closed = measure_gap <= 0.3` would be a CLIFF: the latch
    # decides whether an APPROACH PHASE EXISTS AT ALL (stop-hits, arrest, true-time) rather than scaling anything.
    # Whether two fighters find themselves AT MEASURE or ALREADY ENGAGED when their reach differs marginally is
    # genuinely uncertain — it turns on the approach, the ground, who committed first — so the
    # latch is a probabilistic BAND: certainly closed well inside the threshold, certainly open well outside, and a
    # smooth ramp between.
    _lo, _hi = cfg['CLOSE_GAP_REF']-cfg['CLOSE_LATCH_BAND'], cfg['CLOSE_GAP_REF']+cfg['CLOSE_LATCH_BAND']
    if measure_gap<=_lo:   closed=True
    elif measure_gap>=_hi: closed=False
    else:                  closed = rng.random() < (_hi-measure_gap)/(_hi-_lo)
    # RE-PRESENTATION GATE (ED-PC-0033): the reset above restores the HONEST open-measure geometry, but a fresh
    # engagement does not always open at measure — it opens at measure only if the reach weapon can RE-PRESENT its
    # point against a (re-)closing opponent. An armoured closer who does not fear a point that cannot defeat his
    # harness crowds in and STAYS glued from the prior close, so if the previous engagement ended CLOSED and the longer
    # weapon fails its re-presentation roll (systems.represent_measure_p — armour-faded via reach_threat, footwork-
    # lifted), the shorter has crowded to grips: this engagement starts CLOSED, and the reach advantage never gets to
    # speak. UNARMOURED -> represent_p 1.0 -> always re-presents (reach dominates off-plate); PLATE -> floored -> crowded
    # almost every engagement (a spear cannot keep a determined plate-armoured man at the point — the honest physics the
    # naive always-reset would have violated, letting the spear field-win at heavy). First engagement (prev_closed=False)
    # always opens at measure — the initial approach is real.
    if prev_closed and not closed and measure_gap>cfg['CLOSE_GAP_REF']:
        _rep = S.represent_measure_p(longer, shorter, cfg, TR, measure_gap=measure_gap)
        if _rep < 1.0 and rng.random() >= _rep:   # short-circuit: represent_p==1.0 (none/light) draws NO rng — the gate is inert on the stream off-plate
            closed=True; measure_gap=0.0
    # No pre-contact seizure contest (Jordan 2026-06-05): initiatives start even (0.0 from _init_live); the ongoing
    # Vor (hit-gains/steals/decay) decides who holds it.
    A.initiative, B.initiative = 0.0, 0.0
    # tempo is CONDITIONAL (grip/stance/fatigue), recomputed per-beat below — not a static pre-loop property.
    # ARBITRARY CADENCE PHASE AT ENGAGEMENT START (ED-PC-0037, F16 — the first-actor monopoly).
    # Both fighters beginning in LOCKSTEP would let the same fighter act first every time (a synchronised race between
    # two metronomes is won by the same fighter), so a 1.5% cadence edge would buy a 2:1 action economy.
    # The fix is NOT noise on the physics: cadence stays exactly as derived. What is genuinely unknown is the INITIAL
    # CONDITION — where in his own rhythm each fighter happens to be at the instant the blades cross. Nobody enters a
    # measure on a shared downbeat. Drawing that phase uniformly across the cycle is the honest statement of that
    # ignorance, and it leaves tempo fully meaningful: over an exchange the faster weapon still acts proportionally
    # more often, it simply no longer owns the first action by construction. Who acts first FROM those phases is then
    # decided by cadence x anticipation (systems.tempo_pressure — the Vor and the read).
    ready={c: rng.random()*cfg['ACT_THRESHOLD'] for c in (A,B)}
    wounds0 = {A: A.wt.wounds, B: B.wt.wounds}   # the wounds each fighter has as the round opens: the line is crossed when he has more (B15.10)
    beats=0; exchanges=0
    reopen_moment=False; push_avail=False   # distance-creating-moment state for re-opening (corrections 1+3)
    # (feint_streak removed — feint dissolved into the attack, WS-5)
    _emit('engagement_start', aggressor=first.label, defender=(B if first is A else A).label,
          longer=longer.label, shorter=shorter.label, weapon_A=A.weapon, weapon_B=B.weapon,
          reach_A=round(erA,2), reach_B=round(erB,2), measure_gap=round(measure_gap,2), closed=closed)
    while beats < cfg['BEAT_BUDGET']:
        # DUEL TERMS (RS-25; B15.10 the BURST-BREAKER): checked at the head of every beat, so a wound gate taken in one beat cuts
        # the round before the NEXT beat opens -- the round then ends and the yield roll comes (`_fight`). It reads a NEW crossing,
        # the line crossed during THIS round (`wounds0`, taken at the round's start), never standing state: a man who fought on
        # past the line would otherwise end every later round at its first beat. Inside the beat that dealt it, the later draws still
        # run (the riposte graze, the bind loop, the contact axis), so both fighters can cross in one beat; the tie rule decides that.
        # A pure read of the trackers: no draw, and under lethal terms (`terms is None`) not even the read.
        if terms is not None and _terms_met(A, B, terms, cfg, wounds0):
            _emit('separation', reason='terms'); return None, closed, 'terms'
        beats+=1
        # CONDITIONAL TEMPO (correction 2): recompute each beat with current fatigue — grip/stance/fatigue change
        # cadence; it is not a static weapon property. Approach uses general cadence; closed uses close-cadence.
        ffat={A:max(0.0,1-A.stamina/max(1,A.stamina_max)), B:max(0.0,1-B.stamina/max(1,B.stamina_max))}
        for c in (A,B):
            # INITIATIVE DECAY (damper) — per-tradition HOLD: high measure (destreza) decays slower, holding the Vor longer.
            c.initiative=S.clamp_initiative(c.initiative*S.init_hold_decay(c,cfg,TR), cfg)
            # DISPOSITION (initiative lever): aggressive temperament drifts the Vor UP (pressing builds Vor), cautious DOWN
            # (cedes it) — the standing pressure that makes both poles cost. Neutral (lean 0) = no drift; bounded by clamp.
            c.initiative=S.clamp_initiative(c.initiative + cfg['DISP_INIT_K']*S.disp_lean(c), cfg)
            # STRUCTURE recovery (the kuzushi damper): balance regathers toward 1.0 each beat.
            c.poise=S.clamp_poise(S.poise_regen(c,cfg), cfg)   # Focus speeds structure recovery (Jordan 2026-06-03); regen formula -> systems.poise_regen
            c.grip_position=S.grip_target(c, closed, cfg)   # GRIP/STANCE (The Approach): a closing pole GATHERS IN (grip_position 0->1) to fight the close; else 0 (full reach). CONTINUOUS, derived. The lunge is set at the attack below.
            c.range_avail=S.range_utilization(c, measure_gap, cfg)   # SWING-ROOM (I5, D4): measure-derived, not form-derived — a single per-beat write suffices (no post-swap refresh needed, unlike er/sel_*). Shapes commit_depth's Beta window + the swing-room legibility term + the approach stop-hit; also threaded into THIS beat's select_mode/afforded_heads below (percussion's Phi_room).
            c.facing=S.facing_target(c, closed, cfg)   # FACING (I6, D6): near-neutral per-beat state, keyed ONLY on stance/measure/grip (C2 — never weapon class). Feeds the lateral-void close_rate term + reach_sigma's small profile term.
            c.lunge_depth=0.0                                # reset the body-extension each beat; a deep thrust re-sets it below
            _select(c, B if c is A else A, closed, cfg, measure_gap)   # USE-MODE: the afforded head with the best damage-coupling vs the opponent's armour (S.select_mode); refreshed after the half-sword form-switch below.
            er[c]=S.reach_base(c,cfg)   # er REFRESH #1 (I3, D3, two-recompute contract — the 2026-07-02-scene-combat-closing-distance-redesign audit): re-derives ONLY er[c] on the grip-aware CURRENT (pre-swap) form; NEVER measure_gap (the running approach decrement, below) or `closed` (latched); longer/shorter LABELS stay frozen at engagement start (JD-2 plan default). Feeds reopen (below) and close_tempo/tempo (next line) via reach-derived close_unwieldiness.
        if not closed: rate={c:S.weapon_tempo(c,cfg,ffat[c]) for c in (A,B)}
        else:          rate={c:S.close_tempo(c,cfg,ffat[c]) for c in (A,B)}
        # WHO ACTS FIRST = CADENCE x ANTICIPATION (ED-PC-0037, F16). Weapon cadence ALONE would decide the fight's most
        # important question deterministically: the marginally faster weapon would cross ACT_THRESHOLD first every time
        # (a 1.5% edge -> a 2:1 action economy). systems.tempo_pressure supplies the other half —
        # the VOR and the READ, i.e. anticipation. Cadence proposes; initiative and reading dispose.
        for c in (A,B): ready[c]+=rate[c]*S.tempo_pressure(c, (B if c is A else A), cfg, TR)
        # REACH RE-OPENING (corrections: a created moment, not just balance+reach). The longer weapon can make
        # distance only when a MOMENT exists — the opponent over-committed (must recover balance), OR the longer
        # weapon won a defensive maneuver last exchange (bind/parry/deflect created the gap), OR it frees a hand to
        # shove (grappling-manual one-handed push at reach). Identifying the moment needs READING; executing the
        # withdrawal needs FOOTWORK; and the attempt is READABLE — the shorter weapon's own read can deny it.
        if closed and beats>1 and reopen_moment:
            base_gap=er[longer]-er[shorter]
            if base_gap>cfg['CLOSE_GAP_REF'] and rng.random()<S.reopen_prob(longer, shorter, base_gap, ffat[longer], push_avail, cfg, TR)*S.reach_threat(longer, shorter, cfg):
                closed=False; measure_gap=base_gap; ready=_carry(ready,cfg)
                reopen_moment=False; push_avail=False
                _emit('separation', reason='reopen'); return None, False, 'reopen'
        reopen_moment=False; push_avail=False   # the moment is fleeting; consumed/expires each beat unless re-created below (RR-01: push_avail no longer carries across beats)
        # PROACTIVE FIGHTING WITHDRAWAL (ED-PC-0030): a reach weapon closed into a bind it LOSES does not have to
        # trade exchanges to a decision — it can REFUSE the bind, break measure with footwork, and re-present its
        # point at the measure where ED-PC-0029 makes it dominant (Silver's staff/spear keeps the swordsman at the
        # weapon's length). VOLUNTARY (any closed beat, unlike the reactive created-moment reopen above) and
        # READ-CONTESTED: the closer who reads it stays glued and PURSUES (HEMA Nachreisen — striking the
        # withdrawing weapon as it turns). EMERGENT gate lives in systems.disengage_attempt_p + systems.disengage_clean_p (fires only when the longer
        # weapon is OUT-LEVERAGED in the bind — a light spear out-bound by a rigid estoc; a bind-dominant poleaxe
        # stays and wins). This is the closed-phase lever for the reach-weapon-loses-the-bind residual: cycling
        # approach<->bind, the long weapon wins on accumulated stop-hits instead of a bind it cannot win.
        if closed and beats>1:
            base_gap=er[longer]-er[shorter]
            # ATTEMPT a withdrawal only per the inclination (out-leveraged + can threaten at range); no attempt -> no
            # pursuit (fixes the fade case, where 0 attempt-rate must NOT trigger a free pursuing strike every beat).
            if base_gap>cfg['CLOSE_GAP_REF'] and rng.random() < S.disengage_attempt_p(longer, shorter, base_gap, ffat[longer], cfg)*S.reach_threat(longer, shorter, cfg):
                if rng.random() < S.disengage_clean_p(longer, shorter, cfg, TR):
                    closed=False; measure_gap=base_gap; ready=_carry(ready,cfg)   # CLEAN break -> re-open to measure
                    _emit('disengage', longer=longer.label, shorter=shorter.label, ok=True, gap=round(base_gap,2))
                    _emit('separation', reason='disengage'); return None, False, 'disengage'
                else:                                            # READ -> the closer pursues into the withdrawal (Nachreisen)
                    pool=max(1, _pool_dice(shorter, cfg))
                    deg,net=core.resolve(pool, S.pursuit_sigma(shorter, longer, ffat[shorter], ffat[longer], cfg, TR), rng, core.ob_from_defender(longer, cfg))   # ED-PC-0036: systems.pursuit_sigma owns the formula (the whole sigma-assembly: armour, wounds, the withdrawer's attributes). Ob-from-defender (ED-PC-0058): `longer` is struck if the pursuit lands, so `longer` is the defender this roll is against.
                    _emit('disengage', longer=longer.label, shorter=shorter.label, ok=False, pursued=True, degree=deg)
                    if deg in ('success','overwhelming'):
                        d,_bare=_strike(shorter, longer, deg, net=net, pool=pool)
                        _land('pursuit', shorter, longer, d, _bare)
                        if d<=0 and _bare is False: _emit('turned', by=shorter.label, victim=longer.label, source='pursuit')
                        longer.conc=max(0,longer.conc-cfg['CONC_DRAIN_HIT'])
                        if _down() is not None: return _down(), closed, 'felled'
                    ready[shorter]=max(ready[shorter], cfg['ACT_THRESHOLD'])   # the pursuer seizes the tempo
        # ----- APPROACH: longer weapon threatens (stop-thrusts) while shorter closes -----
        if not closed:
            rt = S.reach_threat(longer, shorter, cfg)               # FIX-1: a long weapon that can't defeat the closer's armour loses its reach edge (1.0 unarmoured by construction)
            displ = S.approach_displace(shorter, longer, cfg)        # lever-arm: set aside a thrusting point on approach
            base_gap = er[longer]-er[shorter]
            # STOP-THRUST RESOLVES FIRST, AND A LANDED ONE ARRESTS THE CLOSE (ED-PC-0029, HEMA Nachreisen / the
            # stop-thrust against a step-in). The longer weapon threatens the point across the closing gap BEFORE the
            # shorter completes its entry; a landed stop-thrust both WOUNDS (core.strike -> apply_wound) and, distinctly,
            # delivers an ARREST that checks the closer's advance — the momentum a braced weapon transmits to a charging
            # body (systems.arrest_impulse), which depends on the weapon's reach + braceable structure, NOT on how much
            # it penetrates (a braced point halts a charge whether or not it draws blood — boar-spear lugs: penetration
            # != arrest). Armour has ALREADY entered once, via reach_threat (rt) in stophit_p below (a point that can't
            # threaten the harness lands fewer meaningful stop-hits); it is NOT re-counted in the arrest magnitude. The
            # beat's net movement is the closer's advance MINUS that arrest (systems.approach_step): a long braced pole
            # nets the closer backward (driven out -> reach controls); a short/whippy/cutting weapon arrests little and
            # the closer walks in. (Arrest is not keyed on damage: damage is wound, not impulse; keying it on damage
            # would crown big CUTTERS and strand the staff Silver's Paradoxes crowns.)
            close_rate=S.close_rate(shorter, ffat[shorter], displ, rt, cfg)   # TA-02 fatigued closer + displace point + walk through un-threatening reach (FIX-1)
            recoil = 0.0
            stophit_p = cfg['STOPHIT_CHANCE'] * min(1.0, measure_gap/cfg['STOPHIT_FULL_GAP']) * (1-displ) * rt  # FIX-1: a stop-hit that can't pierce the armour deters less
            if measure_gap > 0.0 and rng.random() < stophit_p:
                pool=max(1, _pool_dice(longer, cfg))
                nsig=S.stophit_sigma(longer, shorter, measure_gap, cfg)
                _ob=core.ob_from_defender(shorter, cfg)
                deg, net = core.resolve(pool, nsig, rng, _ob)   # Ob-from-defender (ED-PC-0058): `shorter` is struck if the stop-thrust lands.
                _emit('stophit', longer=longer.label, shorter=shorter.label, gap=round(measure_gap,2),
                      pool=pool, net_sigma=round(nsig,3), ob=_ob, net=round(net,2), degree=deg)   # `ob`: the workbench bands its distribution at it (PC-03)
                if deg in ('success','overwhelming'):
                    d,_bare=_strike(longer, shorter, deg, net=net, pool=pool)
                    _land('stophit', longer, shorter, d, _bare)
                    if d<=0 and _bare is False: _emit('turned', by=longer.label, victim=shorter.label, source='stophit')
                    shorter.conc=max(0,shorter.conc-cfg['CONC_DRAIN_HIT'])
                    _sd,_pb=S.percussion_stagger(longer, shorter, d, deg, cfg)   # ED-PC-0031: wind + stagger (armour-gated impulse), distinct from the wound
                    shorter.stamina-=_sd; shorter.poise=S.clamp_poise(shorter.poise-_pb, cfg)
                    if _down() is not None: return _down(), closed, 'felled'
                    recoil = S.arrest_impulse(longer, cfg)   # the ARREST: braced-weapon impulse vs the charge (reach+structure, not wound)
            measure_gap=S.approach_step(measure_gap, base_gap, close_rate, recoil)   # net advance − arrest (systems owns the arithmetic)
            just_closed = (measure_gap<=cfg['CLOSE_GAP_REF'])
            if just_closed:
                closed=True; ready=_carry(ready,cfg)   # carry the cadence RESIDUAL (ED-PC-0037): no banked whole action, but no re-synchronised restart either
            _emit('approach', beat=beats, shorter=shorter.label, longer=longer.label, gap=round(measure_gap,2),
                  close_rate=round(close_rate,3), just_closed=just_closed, stophit_p=round(stophit_p,3))
            if not closed:
                if A.stamina<=cfg['STAMINA_COLLAPSE'] or B.stamina<=cfg['STAMINA_COLLAPSE']: _emit('separation', reason='collapse'); return None, closed, 'collapse'
                continue
        # ----- CLOSED: tempo-gated exchange -----
        actors=[c for c in (A,B) if ready[c]>=cfg['ACT_THRESHOLD']]
        if not actors: continue
        if len(actors)==2:
            aggressor = max(actors, key=lambda c: ready[c]) if ready[A]!=ready[B] else actors[rng.below(2)]   # uniform int
        else:
            aggressor = actors[0]
        defender = B if aggressor is A else A
        _agg0=aggressor.label; _def0=defender.label   # frozen for the outcome emit (roles may flip on riposte)
        # half-sword auto-switch (mit dem kurzen Schwert): adopt the form fitting the current range/armour
        aggressor.weapon = S.halfsword_target(aggressor, closed, defender.armor)   # wrapper owns the mutation
        defender.weapon  = S.halfsword_target(defender, closed, aggressor.armor)
        # re-select the use-mode on the (possibly just-switched) form, so sel_* match the current weapon (aggressor resolved FIRST, as before)
        for _c, _opp in ((aggressor, defender), (defender, aggressor)):
            _select(_c, _opp, closed, cfg, measure_gap)
        er[aggressor]=S.reach_base(aggressor,cfg); er[defender]=S.reach_base(defender,cfg)   # er REFRESH #2 (I3, D3): re-derives er for aggressor/defender on the grip+FORM-aware POST-SWAP weapon — so a half-sworded longsword reads its shorter reach everywhere in the closed exchange (reach_sigma below), not the frozen pre-swap #1 value. Consistency-proven: at open measure (grip=0, no swap) this equals #1 exactly.
        ready[aggressor]-=cfg['ACT_THRESHOLD']
        # COMMIT DEPTH — disposition lean + wariness skew a Beta over [2,5] (the commitment-recovery spectrum). The
        # draw + skew live in systems.commit_depth; the wrapper just sequences it and emits (orchestrator owns no formula).
        commit, _ba, _bb, _ln = S.commit_depth(aggressor, defender, cfg, rng, TR)
        _emit('commit', aggressor=_agg0, defender=_def0, commit=round(commit,2), deep=round(S.deep_commit(aggressor, cfg),2), beta_a=round(_ba,3), beta_b=round(_bb,3), stance_lean=round(_ln,3))
        if commit>=S.lunge_commit(aggressor, cfg) and rng.random() < S.lunge_quality(aggressor, cfg):
            aggressor.lunge_depth = min(1.0, (commit-S.lunge_commit(aggressor, cfg))/cfg['LUNGE_DEPTH_SCALE'])   # a deep thrust BECOMES a lunge (gated stochastically by lunge_quality: rapier readily, a cutter never) — its DEPTH scales with commit (CONTINUOUS); the extended body -> lower recovery (recoverability_factor) + more readable (legibility)
        aggressor.stamina-=S.act_cost(aggressor,commit,cfg)
        ready[aggressor]-=cfg['RECOVERY_TEMPO_K']*(commit-2.0)*S.recoverability_factor(aggressor,cfg)   # TEMPO is coupled to RECOVERY: a deep, hard-to-recover commit (a heavy or lunged blow) leaves you SLOWER to act again — the next action waits on the recovery; a feint (commit~2, full recovery) costs no tempo. Non-linear in weight via recoverability_factor.
        oob=cfg['OOB'] if aggressor.stamina<=0 else 0
        fat_a=max(0.0,1-aggressor.stamina/max(1,aggressor.stamina_max)); fat_d=max(0.0,1-defender.stamina/max(1,defender.stamina_max))
        # concentration: mental-fatigue protection (fatigue-resistance) — defender's reading/technique (systems.mental_fatigue)
        mental_fat_d=S.mental_fatigue(defender, fat_d, cfg)
        # tradition channel-weights (cognitive-mode biases over the shared substrate; neutral=1.0)
        # standing reach advantage (module): defender's reach lowers the attacker's net, falling with armour.
        reach_pen=S.reach_sigma(aggressor, defender, er, fat_a, fat_d, cfg, TR)
        # tempo emphasis (commitment-window exploitation): the aggressor's initiative edge, plus the 'tempo' lever as a log-edge (PC-17)
        init=S.init_emphasis_sigma(aggressor, defender, cfg, TR)   # tempo(Agi)+reading(Att), plus the 'tempo' lever as an additive log-edge (systems.init_emphasis_sigma, PC-17)
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
        if read_win and commit>=S.deep_commit(aggressor, cfg):
            steal=S.indes_steal_amount(aggressor, defender, mode==V.DEF_WIND, commit, read_d, read_a, cfg, TR)
            defender.initiative=S.clamp_initiative(defender.initiative+steal, cfg)
            aggressor.initiative=S.clamp_initiative(aggressor.initiative-steal, cfg)
            counter_attempt=S.counter_select(defender, cfg, rng, TR)
        pool=max(1, _pool_dice(aggressor, cfg))
        _ob=core.ob_from_defender(defender, cfg)
        deg, net = core.resolve(pool, net_sigma, rng, _ob)   # Ob-from-defender (ED-PC-0058)
        _emit('roll', aggressor=_agg0, pool=pool, net_sigma=round(net_sigma,3), ob=_ob, net=round(net,2), degree=deg, mode=mode)   # `ob`: the workbench bands its distribution at it (PC-03)
        # OVERCOMMIT EXPOSURE — systems computes it; the wrapper applies the initiative/poise loss.
        overcommit_exposure = S.overcommit_exposure(aggressor, commit, fat_a, cfg, TR)
        # forced-to-Nach by losing BALANCE/grip — per-tradition: tempo-disciplined (English true-times) lose less grip.
        if overcommit_exposure>0:
            aggressor.initiative=S.clamp_initiative(aggressor.initiative - S.init_overcommit_loss(aggressor,overcommit_exposure,cfg,TR), cfg)
            aggressor.poise=S.clamp_poise(aggressor.poise - cfg['POISE_BREAK_OVERCOMMIT']*overcommit_exposure, cfg)  # overextended = off-balance
        # ----- outcome mapping (deg = AGGRESSOR's degree; defender mode can neutralize) -----
        hit=0; riposte=False; bind=False; hit_bare=None   # `hit_bare`: the coverage-gap draw of the blow `hit` carries (None where no blow was struck or none was drawn)
        # neutralize is a FIXED mode-shape (parry deflects / dodge voids / wind binds) — NOT re-scaled by dsig,
        # which already shaped the roll via net_sigma (audit C-2: avoid double-counting defender skill).
        neutralize=cfg['NEUTRALIZE_PARRY'] if mode==V.DEF_PARRY else (cfg['NEUTRALIZE_DODGE'] if mode==V.DEF_DODGE else cfg['NEUTRALIZE_WIND'])
        if deg=='fail':
            riposte=(rng.random() < min(cfg['RIPOSTE_CAP'], cfg['RIPOSTE_ON_FAIL']+overcommit_exposure))
        elif deg=='partial':
            if mode==V.DEF_DODGE: hit,hit_bare=_strike(aggressor, defender, 'graze') if rng.random()<cfg['PARTIAL_DODGE_GRAZE'] else (0,None)
            elif mode==V.DEF_PARRY: hit,hit_bare=_strike(aggressor, defender, 'graze') if rng.random()<cfg['PARTIAL_PARRY_GRAZE'] else (0,None)
            else: bind=True
        elif deg=='success':
            if mode==V.DEF_WIND and rng.random()<cfg['WIND_BIND_P']: bind=True
            elif rng.random()<neutralize: riposte=(rng.random() < min(cfg['RIPOSTE_CAP'], cfg['RIPOSTE_ON_NEUTRALIZE']+overcommit_exposure))
            else: hit,hit_bare=_strike(aggressor, defender, 'success')
        else:
            if rng.random()<max(0.0,neutralize-cfg['NEUTRALIZE_OVERWHELM_DROP']): hit=0
            else: hit,hit_bare=_strike(aggressor, defender, 'overwhelming', net=net, pool=pool)
        if counter_attempt:
            # SUCCESS scales with reflex (CR-85/ED-IN-0330); the untrained single-time counter mostly fails — a
            # desperate-idiot move. Tradition abilities will modulate this upward (added later). (systems.counter_success_prob)
            if rng.random() < S.counter_success_prob(defender, cfg, TR):
                hit=0; hit_bare=None; bind=False; riposte=True            # LANDS: committed attack voided in-tempo, defender ripostes (keeps the seized Vor)
            else:
                # MISS: the botched counter cedes the seized Vor and leaves the defender eating the attack UNDEFENDED
                # (no mode reduction); the hit-block below then applies the wound + further Vor/poise loss — the downside.
                defender.initiative=S.clamp_initiative(defender.initiative-steal, cfg)
                aggressor.initiative=S.clamp_initiative(aggressor.initiative+steal, cfg)
                bind=False; riposte=False
                hit,hit_bare=_strike(aggressor, defender, 'overwhelming' if deg=='overwhelming' else 'success', net=net, pool=pool) if deg in ('partial','success','overwhelming') else (0,None)
        # CONTACT AXIS (I7b, D8/D9): a unified opening_created flag, set by all three precondition sites below
        # (DISPLACE, deep-commit reopen, bind) — NOT three parallel grab checks. Consumed once, in THIS beat's
        # outcome tail (after riposte resolves, below); never carries across beats (unlike reopen_moment/push_avail).
        opening_created=False
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
        agg_head = getattr(aggressor,'sel_head',None) or aggressor.w['head']   # I4/D5: the SELECTED head, native fallback only when unset
        if (agg_head==V.HEAD_POINT and commit>=S.deep_commit(aggressor, cfg) and not hit and read_win and (beat_aside or slip_inside)):
            if rng.random() < cfg['DISPLACE_P']:
                opening_created=True   # CONTACT AXIS precondition site 1: the point set aside / the defender inside
                if not closed: closed=True; measure_gap=0.0; ready=_carry(ready,cfg)
                # pull-back of the committed thrust can still graze the closing defender
                if rng.random() < cfg['DISPLACE_PULLBACK_GRAZE']:
                    d,_bare=_strike(aggressor, defender, 'graze')
                    _land('displace_graze', aggressor, defender, d, _bare)
                    if d<=0 and _bare is False: _emit('turned', by=aggressor.label, victim=defender.label, source='displace_graze')
                    if _down() is not None:
                        _emit_outcome(_agg0, _def0, mode, deg, hit, bind, riposte, A, B); return _down(), closed, 'felled'
                riposte=True   # defender now inside with initiative
        # ---- distance-creating moments for re-opening (corrections 1+3), benefiting the LONGER weapon ----
        # (a) opponent over-committed: a deep commit by the SHORTER weapon (the one who must stay close) leaves it
        #     recovering balance -> the longer weapon can make distance next beat.
        if closed and aggressor is shorter and commit>=S.deep_commit(aggressor, cfg):
            reopen_moment=True; opening_created=True   # CONTACT AXIS precondition site 2: the over-committed shorter fighter is exposed
        # (b) the longer weapon, defending, won a defensive maneuver (bind/parry/deflect) this exchange -> a gap opens.
        if closed and defender is longer and (bind or (deg in ('fail','partial') and not hit)):
            reopen_moment=True; opening_created=True   # CONTACT AXIS precondition site 2 (cont.): the same defensive win opens contact
        # (c) freed-hand shove: a long TWO-HANDED weapon at the close can briefly free a hand to push (grappling
        #     manuals) -> a chance to create the moment itself. Available when the longer weapon is 2H and closed.
        if closed and longer.w['hands']==2 and rng.random()<cfg['PUSH_AVAIL_P']:
            push_avail=True; reopen_moment=True; opening_created=True   # a freed hand IS a contact precondition
        if hit>0:
            _land('exchange', aggressor, defender, hit, hit_bare); defender.conc=max(0,defender.conc-cfg['CONC_DRAIN_HIT'])
            # forced-to-Nach by DAMAGE: the aggressor presses the advantage (gains the Vor); the struck defender loses it.
            aggressor.initiative=S.clamp_initiative(aggressor.initiative+cfg['INIT_GAIN_HIT'], cfg)
            defender.initiative=S.clamp_initiative(defender.initiative-cfg['INIT_LOSS_WOUNDED'], cfg)
            defender.poise=S.clamp_poise(defender.poise - cfg['POISE_BREAK_HIT']*min(1.0, hit/cfg['POISE_SOLID_HIT']), cfg)  # solid blows stagger; chip damage barely
            _sd,_pb=S.percussion_stagger(aggressor, defender, hit, deg, cfg)   # ED-PC-0031: concussive wind + strong stagger (armour-gated; the blunt-through-plate path the wound-only break above cannot see)
            defender.stamina-=_sd; defender.poise=S.clamp_poise(defender.poise-_pb, cfg)
            if _down() is not None:
                _emit_outcome(_agg0, _def0, mode, deg, hit, bind, riposte, A, B); return _down(), closed, 'felled'
        elif hit_bare is False:   # a blow struck against the harness that dealt nothing: the blade was turned (PC_D)
            _emit('turned', by=aggressor.label, victim=defender.label, source='exchange')
        if bind:
            opening_created=True   # CONTACT AXIS precondition site 3: a bind IS a contact opening (Ringen am Schwert)
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
                        d,_bare=_strike(aggressor, defender, 'success')
                        _land('bind', aggressor, defender, d, _bare)
                        if d<=0 and _bare is False: _emit('turned', by=aggressor.label, victim=defender.label, source='bind')
                        defender.conc=max(0,defender.conc-cfg['CONC_DRAIN_HIT'])
                        _sd,_pb=S.percussion_stagger(aggressor, defender, d, 'success', cfg)   # ED-PC-0031: wind + stagger in the bind
                        defender.stamina-=_sd; defender.poise=S.clamp_poise(defender.poise-_pb, cfg)
                        if _down() is not None:
                            _emit_outcome(_agg0, _def0, mode, deg, hit, bind, riposte, A, B); return _down(), closed, 'felled'
                        break
                else: riposte=True; break
        if riposte:
            defender.conc=max(0,defender.conc-cfg['CONC_DRAIN_LOSS'])
            aggressor, defender = defender, aggressor   # role flip — objects, frame-safe
        # CONTACT AXIS (I7b, D8/D9): the ONE insertion point, after hit/bind/riposte all resolve — reads the
        # unified opening_created flag set above (NOT three parallel grab checks). grab_available itself gates
        # non-dagger/unarmed weapon-wielders on opening_created (no grapple path from open measure — this whole
        # tail only runs closed — and none without a real opening this beat); dagger/unarmed are open-contact
        # exempt. A single one-shot resolution (contact.grab_outcome never loops), so it cannot re-enter the
        # bind inner loop's `beats` mutation above.
        if CT.grab_available(aggressor, defender, opening_created, cfg):
            gsig = CT.grab_sigma(aggressor, defender, cfg)
            contact_outcome = CT.grab_outcome(gsig, rng, cfg)
            _emit('contact', aggressor=_agg0, defender=_def0, actor=aggressor.label, opponent=defender.label,
                  outcome=contact_outcome, gsig=round(gsig,3))
            # branch effects reuse the existing structure/initiative vocabulary (poise/initiative only — a
            # grapple is not a strike: no wound/stamina channel). 'escape' is a no-op (the attempt is voided).
            if contact_outcome=='disarm':
                defender.poise=S.clamp_poise(defender.poise - cfg['POISE_BREAK_BIND']*cfg['CONTACT_DISARM_POISE_K'], cfg)
            elif contact_outcome in ('throw','pin'):
                defender.poise=S.clamp_poise(defender.poise - cfg['POISE_BREAK_BIND']*cfg['CONTACT_THROW_POISE_K'], cfg)
                aggressor.initiative=S.clamp_initiative(aggressor.initiative + cfg['INIT_GAIN_HIT'], cfg)
            elif contact_outcome=='foot_pin':
                defender.poise=S.clamp_poise(defender.poise - cfg['POISE_BREAK_OVERCOMMIT'], cfg)
            elif contact_outcome=='control':
                aggressor.initiative=S.clamp_initiative(aggressor.initiative + cfg['INIT_STEAL_INDES']*cfg['CONTACT_CONTROL_VOR_K'], cfg)
        _emit_outcome(_agg0, _def0, mode, deg, hit, bind, riposte, A, B)
        exchanges+=1
        # ROUND = one approach -> burst -> separation (Jordan 2026-06-03; A-101). The burst is a SMALL EMERGENT run of
        # exchanges, gated by TEMPO (who re-reaches ACT_THRESHOLD via close_tempo), NOT by ripostes: a faster fighter
        # can land SEVERAL hits in a single round with no reply. It ends when (a) the ceiling BURST_MAX is reached, or
        # (b) an exchange resolves CLEANLY on defence -- a dodge/parry/miss with no hit, no riposte, no bind -- so the
        # measure breaks (the floor: one swing, one dodge, separate = 1 exchange). A landed hit, a riposte (role flip),
        # or a bind CONTINUES the pressing. Felling / stamina-collapse exits are handled above. Combat = many such
        # rounds; wounds persist across them, so equal fighters take several rounds to resolve (emergent, not enforced).
        if A.stamina<=cfg['STAMINA_COLLAPSE'] or B.stamina<=cfg['STAMINA_COLLAPSE']: _emit('separation', reason='collapse'); return None, closed, 'collapse'
        if exchanges >= cfg['BURST_MAX']: _emit('separation', reason='burst_ceiling'); return None, closed, 'burst_ceiling'
        if not (hit>0 or riposte or bind): _emit('separation', reason='clean_defence'); return None, closed, 'clean_defence'
    _emit('separation', reason='beat_exhaustion'); return None, closed, 'beat_exhaustion'

class Yield:
    """§11.4 YIELD (PC-01, `ED-PC-0056`), a Phase-1 DECLARATION, not a fourth resolver and not a fourth band.

    `by` is the yielding Combatant; `turn` the 1-based turn at whose Phase 1 it is declared; `accepted` is the
    OPPONENT's choice (the engine has no decider for it, so the caller supplies it); `objective_contested` is the
    world fact the engine cannot see -- the yielder's faction objective is still contested in the same zone.
      - contested            -> the declaration is REFUSED ("cannot Yield while... contested") and the fight runs on,
                                untouched: no draw is taken by the refusal.
      - accepted             -> combat ENDS. No further rolls.
      - not accepted (refused by the opponent) -> the yielder is UNRESISTING, so no contest roll resolves anything
                                further either; what the opponent does with an unresisting man (execute, take
                                prisoner, release) is the CALLER's disposition, carried on the `yield` event.
    THE MAPPING (no fourth band): a yielder is STANDING, so the seam's existing walk reads him `Untouched`/`Wounded`
    off his own WoundTracker; the surrender rides on the result (the `yield` trace event), never in the band. A band
    would be a second reading of `felled`, which a yield does not set. No constant: the rule carries no number."""
    __slots__ = ('by', 'turn', 'accepted', 'objective_contested')

    def __init__(self, by, turn=1, accepted=True, objective_contested=False):
        self.by, self.turn, self.accepted, self.objective_contested = by, int(turn), bool(accepted), bool(objective_contested)

# ── DUEL TERMS (RS-25, plan position PC-10a; B15.10 the yield is a roll) ───────────────────────────────────────────
# Jordan 2026-10-14: "a duel doesn't have to be lethal". The terms are agreed BEFORE the scene, like `Yield`. Under every term a fighter
# who takes a wound gate in a round makes ONE YIELD ROLL at its end (`_yield_roll`, A-24): the term sets only how hard it is to fight on,
# `cfg['YIELD_OB'][terms]`; his Spirit and his wounds are levels on it and the host's `decisiveness` a σ. Failure: he yields, STANDING, through
# the `yield` trace event `fight._surrender` lifts (the opponent's result, no riposte: a lucky blow cannot turn a fight he has given up);
# Partial: he is shaken (`CONC_DRAIN_LOSS`) and fights on; Success: he fights on; Overwhelming: he rallies (Concentration full).
# [ASSUMPTION; medium; Jordan to correct -- the three terms, the roll, the bands and `YIELD_OB`'s values. Revert: no roll; the fighter who
# crosses the term's line yields, always, and `death` never yields.]
#   - 'death' : the fight runs to a felling or to UNRESOLVED, or until a yield roll fails. The default. It never cuts a round.
#   - 'blood' : the round is cut between beats when a fighter takes a wound gate (the burst-breaker).
#   - 'yield' : the round is cut between beats when a fighter takes a wound gate at or below `CFG['YIELD_HEALTH_FRAC']` of full Health.
# THE TERM'S LINE IS THE BURST-BREAKER'S, NEVER THE DECISION: it decides where a round is cut so the roll comes at the crossing, not after a
# further burst of blows; whether he stops is the roll's. Acceptance: under `blood` and `yield` the terms are the acceptance (`accepted=True`);
# under `death` the scene ends with the yielder standing and the event carries `accepted=None` -- what the other man does with an unresisting
# man is the host's. ⚠ What a term does NOT do: it does not reshape a blow. A strike that fells a fighter on the beat it lands is a felling
# under any term; the cut is read between beats, never inside a strike.
DUEL_TERMS = ('yield', 'blood', 'death')   # closed set, this module's: the season's `duel_terms` and `challenge_terms` rosters are checked against it through the composition row `combat.duel_terms`, never re-declared
LETHAL_TERMS = 'death'
_UNHURT = SimpleNamespace(wt=SimpleNamespace(wounds=0))   # the unwounded party `wound_impairment` is read against: his own wounds are the only term

def _gate_crossed(c, wounds0):
    """True when `c` has taken a wound gate since `wounds0[c]` (the round's start): his tracker's wound count is higher. A pure read."""
    return c.wt.wounds > wounds0[c]

def _terms_crossed(c, terms, cfg, wounds0):
    """True when Combatant `c` has crossed the non-lethal `terms` DURING THIS ROUND: he has taken a wound gate (`_gate_crossed`) and, under
    'yield', his Health is at or below `cfg['YIELD_HEALTH_FRAC']` of full (`wt.health_remaining`). A pure read of its tracker; no draw."""
    if terms == 'blood':
        return _gate_crossed(c, wounds0)
    if terms == 'yield':
        return _gate_crossed(c, wounds0) and c.wt.health_remaining <= cfg['YIELD_HEALTH_FRAC'] * c.wt.health_full
    raise ValueError(f"terms {terms!r} is not a non-lethal term")

def _terms_met(A, B, terms, cfg, wounds0):
    return _terms_crossed(A, terms, cfg, wounds0) or _terms_crossed(B, terms, cfg, wounds0)

def _terms_yielder(A, B, failed):
    """Which fighter yields once the rolls are made: the one who failed his; if both failed in the same round, the one with the smaller
    fraction of Health left; on an exact tie, nobody -- honour is even, and the fight ends UNRESOLVED (the ruled outcome, Jordan
    2026-06-02), with no yield. `failed` is the fighters whose yield roll failed, at least one."""
    if len(failed) == 1:
        return failed[0]
    fa, fb = (c.wt.health_remaining / c.wt.health_full for c in (A, B))
    return A if fa < fb else B if fb < fa else None

def _spirit_levels(c, cfg):
    """`(levels for, levels against)` the yield roll from his Spirit: the signed WHOLE steps of `c.spirit` from the attribute scale's mid-point
    (`attributes.NEUTRAL['spirit']`, the spec's centring value: this module reads no registry, A-25), each one `cfg['SPIRIT_LEVEL']` for him above it and
    against him below (a half step is no step)."""
    n = math.trunc(c.spirit - ATTR.NEUTRAL['spirit'])
    level = cfg['SPIRIT_LEVEL']
    return ([level] * n, []) if n > 0 else ([], [level] * -n)

def _yield_roll(c, terms, sigma, cfg, draw):
    """THE YIELD ROLL (B15.10, `PC_A`, A-24): one roll through `core.resolve` (the owner ladder), returning the degree; the caller applies
    the band. The pool is the one pool rule on his skill score and no addends (`_pool_dice`), the obstacle `cfg['YIELD_OB'][terms]`, the net σ
    his Spirit as levels (`_spirit_levels`) plus how hurt he is as a level against him (`S.wound_impairment`'s per-wound term, the channel the
    exchange uses, read against an unhurt man) plus `sigma`, the host's `decisiveness` for him. `draw` is the keyed `Draw` of
    `"yield:<scene>:<round>:<party>"`. Draws only from `draw`; mutates nothing."""
    pool = max(1, _pool_dice(c, cfg, addends=0))
    net_sigma = core.SL.levels_to_net_sigma(*_spirit_levels(c, cfg)) + S.wound_impairment(_UNHURT, c, cfg) + sigma
    deg, _net = core.resolve(pool, net_sigma, draw, cfg['YIELD_OB'][terms])
    return deg

# ── THE PER-TURN CHOICE (v10 REM-31, IN-46: the grid mode's suspension) ──────────────────────────────────────────────
# A PLAYABLE fight hands each turn's choice to a DECIDER, a parameter (never a module attribute: the way `_TRACE` was
# rebound by its callers is the precedent not to follow; `fight`'s `trace` argument replaced it). `decide(turn)` is called at the top of each turn, before every draw of that turn and after
# a declared `Yield` of the same turn (the declaration is the earlier fact), and returns one member of this closed set:
#   - 'engage'   : the turn is fought. Today's loop engages every turn, so `decide=None` (the default, AUTOMATED) is
#                  exactly 'engage' every turn.
#   - 'withdraw' : the loop's existing UNRESOLVED exit, taken early -- no further turn, no riposte draw (the fight is
#                  undecided, result 0, the ruled outcome). A `withdraw` trace event names the turn.
# [ASSUMPTION; the set is {engage, withdraw}, Jordan's "you choose to attack" (#445 `05:8-11`); PC's Plan layer (M-4) may
# widen it, and whether `yield` joins it is #445 `05` §4.1 (J-15), not decided here.] The decider draws nothing from
# `rng` and mutates nothing, so equal choices produce the identical draw sequence: AUTOMATED and PLAYABLE replay equal.
ENGAGE, WITHDRAW = 'engage', 'withdraw'
TURN_CHOICES = (ENGAGE, WITHDRAW)   # closed set, this module's: the host's decider is checked against this tuple

def fight(A, B, cfg, rng, max_bouts=12, yield_decl=None, terms=LETHAL_TERMS, decide=None, trace=None, decisiveness=(0.0, 0.0)):
    """One scene (`_fight`, below). `cfg` and `rng` take no default: a missing stream is a signature error at the call site,
    not a branch (B14.20); `cfg=None` is passed on purpose and means the engine's own `CFG`; pass a keyed
    `Draw` (`draw.seeded(...)`) for `rng`. `trace` is a callable(event: dict) the engine binds to `_TRACE` for the call and
    restores after it, on every exit; `None` leaves `_TRACE` as it stands (a caller that still holds it bound is not undone).
    `decisiveness` is the host's σ for each party's yield roll, `(A's, B's)` (B15.10; `PersonalCombatInput.decisiveness`)."""
    global _TRACE
    prev = _TRACE
    if trace is not None:
        _TRACE = trace
    try:
        return _fight(A, B, cfg, rng, max_bouts, yield_decl, terms, decide, decisiveness)
    finally:
        _TRACE = prev

def _fight(A, B, cfg, rng, max_bouts, yield_decl, terms, decide, decisiveness=(0.0, 0.0)):
    if terms not in DUEL_TERMS:
        raise ValueError(f"terms {terms!r} is not one of {DUEL_TERMS}")
    stop = None if terms == LETHAL_TERMS else terms   # None: the lethal fight never cuts a round (`engagement` takes no terms); the yield roll below reads `terms`
    if yield_decl is not None:
        if not (yield_decl.by is A or yield_decl.by is B):
            raise ValueError("Yield.by must be the A or B Combatant passed to fight (compared by identity)")
        if not (1 <= yield_decl.turn <= max_bouts):
            raise ValueError(f"Yield.turn {yield_decl.turn} is outside 1..max_bouts ({max_bouts}): it would never fire")
    cfg=cfg or CFG   # `None`: the engine's own CFG. The stream is the caller's keyed `Draw`; never built here
    # A FIGHT BEGINS UNWOUNDED: zero each tracker's damage here, at the fight's own start (PC-13's `wound` events sum to
    # the tracker within one fight). `_init_live` calls `Combatant.rederive(cfg)`, the one derivation path (PC-14),
    # which reads the fighter's attributes as they stand now (an attribute edited after construction is followed) and
    # itself never touches damage.
    A.wt.cumulative_damage = 0; B.wt.cumulative_damage = 0
    _init_live(A,cfg); _init_live(B,cfg)
    _emit('fight_start', A=A.label, B=B.label, weapon_A=A.weapon, weapon_B=B.weapon,
          armor_A=A.armor, armor_B=B.armor, tradition_A=A.tradition, tradition_B=B.tradition)
    result=0
    scene=rng.n   # the stream's ordinal where this fight begins: it keys the fight's per-blow coverage-gap draws (`engagement._strike`), its riposte and its yield rolls, so a caller that reuses one `Draw` for many fights (a workbench loop) gets a fresh gap sequence per fight; a host's per-fight key begins at 0
    prev_closed=False   # measure state threaded across engagements (ED-PC-0033): a reach weapon only re-presents at open measure if it can hold a crowding opponent off; the first engagement always opens at measure
    for turn in range(max_bouts):   # each iteration = ONE round (A-101); victor emerges over MULTIPLE turns with persistent wounds/fatigue. fight() is the multi-turn SIM harness (runs to a decision for win-rates); the GAME calls one engagement per turn.
        if yield_decl is not None and yield_decl.turn == turn+1:   # PHASE 1: the declaration precedes every draw of its turn
            _refused = 'objective_contested' if yield_decl.objective_contested else None
            _emit('yield', turn=turn+1, by=yield_decl.by.label, accepted=(yield_decl.accepted and _refused is None), refused=_refused)
            if _refused is None:
                # Combat ends with the yielder standing; the opponent holds the field. no riposte draw: that is a
                # roll, and §11.4 is "no further rolls" -- a lucky blow cannot turn a fight nobody is contesting.
                result, winner = (-1, B) if yield_decl.by is A else (1, A)
                _emit('fight_result', result=result, winner=winner.label)
                return result
        if decide is not None:   # THE PER-TURN CHOICE (REM-31): before every draw of the turn; draws nothing
            choice = decide(turn+1)
            if choice not in TURN_CHOICES:
                raise ValueError(f"the decider returned {choice!r}, which is not one of {TURN_CHOICES}")
            if choice == WITHDRAW:
                _emit('withdraw', turn=turn+1)
                break            # result is 0 here (a felling breaks with a result set): UNRESOLVED, no riposte draw
        first = A if rng.random()<0.5 else B
        _emit('turn_start', turn=turn+1, first=first.label)
        wounds0 = {A: A.wt.wounds, B: B.wt.wounds}   # the round's opening wounds: a wound gate crossed since is the yield roll's licence (B15.10)
        loser, prev_closed, ended_by = engagement(A,B,first,cfg,rng,prev_closed,terms=stop,turn=turn+1,scene=scene)
        _emit('engagement_end', turn=turn+1, felled=(loser.label if loser is not None else None), ended_by=ended_by)
        if loser is not None:
            result = -1 if loser is A else 1   # +1 => A won
            break
        failed = []
        for side, c in (('A', A), ('B', B)):
            if not _gate_crossed(c, wounds0):
                continue
            # THE YIELD ROLL (B15.10, A-24): at the end of the round in which he took a wound gate, once, the party's own keyed sub-draw (a function of the
            # fight's key, the round and the party, never of how many uniforms the stream has taken: B15.05's form).
            deg = _yield_roll(c, terms, decisiveness[0 if c is A else 1], cfg, KD.seeded(KD.H2(rng.key, f"yield:{scene}:{turn+1}:{side}")))
            if deg == 'fail':
                failed.append(c)
            elif deg == 'partial':
                c.conc = max(0, c.conc - cfg['CONC_DRAIN_LOSS']); _emit(V.EV_SHAKEN, turn=turn+1, by=c.label)
            elif deg == 'overwhelming':
                c.conc = c.conc_max; _emit(V.EV_RALLIED, turn=turn+1, by=c.label)
        if failed:
            # A FAILED ROLL ENDS THE SCENE with the yielder standing: the `yield` event `fight._surrender` lifts, the opponent's result (no felling, so no
            # riposte), read at the END of the round where a declared `Yield` is read at the start of its turn. Two failures in one round: the smaller fraction of
            # Health yields; an exact tie yields nobody and the fight ends UNRESOLVED.
            yielder = _terms_yielder(A, B, failed)
            if yielder is None:
                _emit('fight_result', result=0, winner=None)
                return 0
            _emit('yield', turn=turn+1, by=yielder.label, accepted=(None if terms == LETHAL_TERMS else True), refused=None, terms=terms, degree='fail')
            result, winner = (-1, B) if yielder is A else (1, A)
            _emit('fight_result', result=result, winner=winner.label)
            return result
        for c in (A,B):
            c.stamina=min(c.stamina_max, c.stamina+cfg['RECOVERY_FRAC']*(c.stamina_max-c.stamina)*(c.stamina_max/cfg['STAMINA_REF']))
            c.conc=max(0,min(c.conc_max, c.conc-cfg['CONC_DRAIN_BOUT']+cfg['CONC_RECOVER_FRAC']*(c.conc_max-c.conc)))
    # NO automatic tiebreak (Jordan 2026-06-02): if neither fighter is felled, the round ends UNRESOLVED (result 0).
    # We do not foreclose by awarding the round on wound-count — an undecided fight is a legitimate outcome.
    # No matchup is ever certain (`UPSET_FLOOR`) -- and that is a blow, not an edit of the result: at a felling the riposte
    # (`engagement`'s `_land`) may turn it, so `result` is whatever the fight, continued, ends with.
    _emit('fight_result', result=result, winner=(A.label if result==1 else B.label if result==-1 else None))
    return result
