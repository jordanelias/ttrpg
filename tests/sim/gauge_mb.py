"""Mass Battle GAUGE v2 -- historically RECALIBRATED battery (bottom-up grounding).

Validates the current engine against win-rate bands derived bottom-up from historical
precedent and peer-reviewed academic military analysis -- NOT fitted to engine output.
The engine is validated AGAINST these bands; where it falls outside, the gauge flags the
divergence rather than lowering the band. The full grounding -- the metric change, the
source citations (with DOIs), the per-band rationale, and the validation report -- lives
in the companion reference:

    references/historical/mass_battle_gauge_grounding.md

Metric: the win-rate band is on the DECISIVE SPLIT  decA = A_wins / (A_wins + B_wins) --
"who wins WHEN a result is reached." The previous raw win-rate metric conflated the
win-split with the draw rate, so a symmetric mirror failed its band purely on draws. The
draw rate is therefore validated SEPARATELY (draw_exp), since near-parity forces produce
high draw rates by the quantitative combat-modelling literature (see grounding doc): even
matchups allow high draws; gross-asymmetry matchups (envelopment, cavalry vs braced or
shaken foot) are expected to resolve.

Two granularities: single (one engagement-turn) and multi (the resolving mode). Single
mode currently returns all-draws at the tick cap for every engine config -- a tick-cap
artifact, not a calibration issue -- so bands are evaluated in multi mode. The engine file
is argv[1], exec'd into namespace, so the same gauge runs against any engine variant.

Grounding + citations index: references/historical/mass_battle_gauge_grounding.md
"""
import sys, os, random, statistics

ENGINE = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/sim_v22.py'
exec(open(ENGINE).read())

ANCHOR_MAP = {  # [canonical: mass_battle_v30.md §deployment — anchor columns]
    ('Line',1):11,('Line',2):10,('Line',3):9,('Line',4):8,                       # [canonical: mass_battle_v30.md §deployment]
    ('Arrowhead',1):11,('Arrowhead',2):10,('Arrowhead',3):8,('Arrowhead',4):7,   # [canonical: mass_battle_v30.md §deployment]
    ('Horseshoe',1):11,('Horseshoe',2):10,('Horseshoe',3):8,('Horseshoe',4):7,   # [canonical: mass_battle_v30.md §deployment]
    ('GappedLine',1):11,('GappedLine',2):9,('GappedLine',3):7,                   # [canonical: mass_battle_v30.md §deployment]
    ('RefusedFlank',1):11,('RefusedFlank',2):10,('RefusedFlank',3):9,            # [canonical: mass_battle_v30.md §deployment]
}

def make_unit(shape, tier, name, faction, unit_type='melee', power=4, command=4,   # [canonical: sim_mb_06_v9_historical_spec.md — uniform T3 stats P4/C4]
              discipline=5, morale=6, stance='balanced',                          # [canonical: sim_mb_06_v9_historical_spec.md — uniform T3 stats D5/M6]
              troop_type='infantry', speed='Standard'):
    # troop_type/speed default to the historical infantry baseline so the original
    # 13 tests construct byte-identically; cavalry rows pass troop_type='cavalry',
    # speed='Fast' by kwargs. Cavalry charge mechanics (charge_pen,
    # PC_CAVALRY_SPEED_MULT) are PER_CELL=1-gated in the engine; under PER_CELL=0
    # cavalry == infantry (S1: speed is not yet wired into combat).
    advance_dir = -1 if faction == 'A' else 1
    start_row = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    anchor_col = ANCHOR_MAP.get((shape, tier), 10)
    su = Subunit(shape=shape, troop_type=troop_type, tier=tier,
                 starting_position=(start_row, anchor_col),
                 advance_dir=advance_dir, unit_type=unit_type)
    return Unit(name=name, faction=faction, power=power, command=command,
                discipline=discipline, discipline_start=discipline,
                morale=morale, morale_start=morale, subunits=[su], dr=1,
                stance=stance, speed=speed)

# (id, label, shape_a, shape_b, ka, kb, lo, hi, draw_exp)
#   (lo,hi)  = DECISIVE-split band: decA = A_wins/(A_wins+B_wins), %  [history-grounded]
#   draw_exp = 'high' (even matchup, high draws OK) | 'low' (decisive matchup, expect draw<30%)
# Bands are set by HISTORY. Where the engine falls outside a band, the test FAILS BY DESIGN
# (the gauge flags engine divergence; the band is NOT lowered to make the engine pass).
# Every band cites references/historical/mass_battle_gauge_grounding.md §3 (per-band rationale).
TESTS = [
    ('H1','Line vs Line (mirror)','Line','Line',{},{},42,58,'high'),                       # [canonical: mass_battle_gauge_grounding.md §3 — H1 mirror symmetry]
    ('H2','Arrowhead(wedge) vs Line','Arrowhead','Line',{},{},48,62,'high'),               # [canonical: mass_battle_gauge_grounding.md §3 — H2 modest wedge edge]
    ('H3','Horseshoe(envelop) vs Line','Horseshoe','Line',{},{},55,72,'high'),             # [canonical: mass_battle_gauge_grounding.md §3 — H3 full envelopment]
    ('H4','Horseshoe vs Arrowhead (Cannae)','Horseshoe','Arrowhead',{},{},45,62,'high'),   # [canonical: mass_battle_gauge_grounding.md §3 — H4 Cannae proper]
    ('H5','RefusedFlank vs Horseshoe','RefusedFlank','Horseshoe',{},{},48,62,'high'),       # [canonical: mass_battle_gauge_grounding.md §3 — H5 oblique counter]
    ('H6','RefusedFlank vs Line','RefusedFlank','Line',{},{},48,60,'high'),                 # [canonical: mass_battle_gauge_grounding.md §3 — H6 oblique order]
    ('H7','GappedLine(manip) vs Line','GappedLine','Line',{},{},48,62,'high'),              # [canonical: mass_battle_gauge_grounding.md §3 — H7 manipular flex]
    ('H8','GappedLine vs Arrowhead','GappedLine','Arrowhead',{},{},50,65,'high'),           # [canonical: mass_battle_gauge_grounding.md §3 — H8 maniples absorb wedge]
    ('H9','Line vs Arrowhead (rev H2)','Line','Arrowhead',{},{},38,52,'high'),              # [canonical: mass_battle_gauge_grounding.md §3 — H9 inverse H2]
    ('H10','Line vs Horseshoe (rev H3)','Line','Horseshoe',{},{},28,45,'high'),             # [canonical: mass_battle_gauge_grounding.md §3 — H10 inverse H3]
    ('H11','Arrowhead vs Horseshoe (rev H4)','Arrowhead','Horseshoe',{},{},38,55,'high'),   # [canonical: mass_battle_gauge_grounding.md §3 — H11 symmetric H4]
    ('R1','Ranged vs Line (open field)','Line','Line',
        {'unit_type':'ranged','stance':'hold'},{},0,30,'low'),                             # [canonical: mass_battle_gauge_grounding.md §3 — R1 ranged loses open field]
    ('R3','Ranged vs Ranged (mirror)','Line','Line',
        {'unit_type':'ranged','stance':'hold'},{'unit_type':'ranged','stance':'hold'},42,58,'high'),  # [canonical: mass_battle_gauge_grounding.md §3 — R3 ranged mirror]
]

CAV = {'troop_type':'cavalry','speed':'Fast'}
CAV_TESTS = [
    # C1: frontal shock cavalry vs STEADY close-order but UNBRACED foot, open ground. CONTESTED,
    # NOT a cavalry win -- a horse will not charge a solid formation, and cavalry's decisive work
    # was against BROKEN or FLANKED foot (Burkholder 2007). [REBASELINE: the old band encoded the
    # popular cavalry-beats-unprepared-infantry misconception this source debunks.]
    ('C1','Cav vs steady unbraced Line','Arrowhead','Line',dict(CAV),{},35,55,'high'),     # [canonical: mass_battle_gauge_grounding.md §3 — C1 contested frontal, rebaseline]
    # C2: frontal cavalry vs BRACED foot (hold + disc8 = the square / schiltron / pike block).
    # Braced infantry DEFEATS frontal cavalry; cavalry wins only rarely (Waterloo squares; Barua 2011).
    ('C2','Cav vs BRACED Line (frontal,hold+d8)','Arrowhead','Line',dict(CAV),{'stance':'hold','discipline':8},5,30,'low'),  # [canonical: mass_battle_gauge_grounding.md §3 — C2 braced repels]
    # C3: cavalry mirror -- side-symmetry control of the charge/momentum path. Even.
    ('C3','Cav vs Cav (mirror control)','Arrowhead','Arrowhead',dict(CAV),dict(CAV),42,58,'high'),  # [canonical: mass_battle_gauge_grounding.md §3 — C3 cav mirror]
    # C4: mounted ENVELOPMENT of a line -- flank/rear is devastating (Cannae; Adrianople; Boddy 2015).
    ('C4','Cav flank/envelopment vs Line','Horseshoe','Line',dict(CAV),{},75,95,'low'),    # [canonical: mass_battle_gauge_grounding.md §3 — C4 mounted envelopment]
    # C5: cavalry vs an already-SHAKEN line (morale 2) -- exploitation + pursuit (Boddy 2015; Hastings).
    ('C5','Cav vs SHAKEN Line (morale2)','Arrowhead','Line',dict(CAV),{'morale':2},65,90,'low'),  # [canonical: mass_battle_gauge_grounding.md §3 — C5 exploits shaken]
    # C6: cavalry vs BRACED-shallow foot (hold + disc8, no depth) -- a faced brace still repels. = C2.
    ('C6','Cav vs BRACED-shallow Line (hold+d8)','Arrowhead','Line',dict(CAV),{'stance':'hold','discipline':8},5,30,'low'),  # [canonical: mass_battle_gauge_grounding.md §3 — C6 = C2]
    # C7: cavalry ENVELOPS a braced line (Horseshoe vs hold+disc8) -- bracing bypassed from flank/rear.
    ('C7','Cav envelop vs BRACED Line (hold+d8)','Horseshoe','Line',dict(CAV),{'stance':'hold','discipline':8},65,90,'low'),  # [canonical: mass_battle_gauge_grounding.md §3 — C7 envelop bypasses brace]
]

def winner_of(r):
    return r.get('winner','draw')

def matchup(sa, sb, ka, kb, mode, n=120, seed_base=1_000_000):  # [canonical: mass_battle_gauge_grounding.md §1 — n sample (SE~5pp), deterministic seed]
    aw=bw=dr=0; turns=[]; a_cas=[]; b_cas=[]
    for s in range(n):
        random.seed(s+seed_base)
        ua=make_unit(sa,3,'A','A',**ka); ub=make_unit(sb,3,'B','B',**kb)  # [canonical: sim_mb_06_v9_historical_spec.md — T3 (tier-3) units]
        a0,b0 = ua.hp_max, ub.hp_max
        if mode=='single':
            r=run_battle(ua,ub,max_turns=18); turns.append(r.get('turns',18))  # [canonical: mass_battle_gauge_grounding.md §1 — single-mode tick cap]
        else:
            r=run_multi_turn_battle(ua,ub,sa,sb,ANCHOR_MAP,max_battle_turns=20); turns.append(r.get('battle_turns',20))  # [canonical: mass_battle_gauge_grounding.md §1 — multi-mode battle-turn cap]
        w=winner_of(r)
        if w=='A':aw+=1
        elif w=='B':bw+=1
        else:dr+=1
        a_cas.append(100*(a0-ua.hp)/a0 if a0 else 0); b_cas.append(100*(b0-ub.hp)/b0 if b0 else 0)
    dec = aw+bw
    return dict(a=aw/n*100, b=bw/n*100, d=dr/n*100,
                decA=(100*aw/dec if dec else 50.0), dec_n=dec,  # [canonical: mass_battle_gauge_grounding.md §1 — even-split fallback when no decisive result]
                t=statistics.mean(turns), a_cas=statistics.mean(a_cas), b_cas=statistics.mean(b_cas))

def run(mode, tests=TESTS, n=120):  # [canonical: mass_battle_gauge_grounding.md §1 — default sample]
    print(f"\n----- MODE: {mode}  (engine: {ENGINE.split('/')[-1]})  metric: DECISIVE split A/(A+B) -----")
    print(f"  {'id':4} {'matchup':30} {'A%':>5} {'B%':>5} {'D%':>5} {'decA':>5} {'band':>7} {'dexp':>4} verdict")
    nb=0
    for tid,label,sa,sb,ka,kb,lo,hi,dexp in tests:
        r=matchup(sa,sb,ka,kb,mode,n=n)
        win_ok = (r['dec_n']>0) and (lo<=r['decA']<=hi)
        draw_ok = (dexp!='low') or (r['d']<30.0)  # [canonical: mass_battle_gauge_grounding.md §1 — decisive matchups expect draw<30%]
        ok = win_ok and draw_ok
        nb+=ok
        flag = 'OK' if ok else ('WIN-OUT' if not win_ok else 'TOO-DRAWISH')
        if r['dec_n']==0: flag='UNRESOLVED'
        print(f"  {tid:4} {label[:30]:30} {r['a']:5.1f} {r['b']:5.1f} {r['d']:5.1f} {r['decA']:5.1f} {lo:>3}-{hi:<3} {dexp:>4} {flag}")
    print(f"  => pass {nb}/{len(tests)}  (bands are HISTORY-grounded; a fail flags engine divergence, not a band to lower)")
    return nb

if __name__=='__main__':
    # Cavalry rows are PER_CELL=1-only (engine gates charge_pen + speed mult on PER_CELL).
    _pc = os.environ.get('PER_CELL','0') not in ('0','','false','False','no','No')
    _tests = TESTS + (CAV_TESTS if _pc else [])
    s=run('single', _tests); m=run('multi', _tests)
    n=len(_tests)
    print(f"\n==== {ENGINE.split('/')[-1]}: single={s}/{n}  multi={m}/{n} (multi is the resolving mode) ====")
