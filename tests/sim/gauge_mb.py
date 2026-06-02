"""Mass Battle GAUGE (module 1 of the validation-foundation rebuild).

Historically-grounded battery that runs the CURRENT engine API against the
v9 spec bands (derived from precedents_warfare.md: Cannae/Pydna/Leuctra/etc.)
at TWO resolution granularities:

  - single  : run_battle (one engagement-turn) -- where the v9 win-rate bands
              properly apply; isolates formation counters from multi-turn
              amplification.
  - multi   : run_multi_turn_battle -- exposes how much the multi-turn layer
              amplifies the win-rate spread (the F1/Lesson-5 concern).

Engine file is argv[1] (exec'd into namespace), so the same gauge runs against
as-is and ratio-restored engine variants. Bands: tests/sim/sim_mb_06_v9_historical_spec.md.
"""
import sys, os, random, statistics

ENGINE = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/sim_v22.py'
exec(open(ENGINE).read())

# [canonical: mass_battle_v30.md §deployment — anchor columns]
ANCHOR_MAP = {
    ('Line',1):11,('Line',2):10,('Line',3):9,('Line',4):8,
    ('Arrowhead',1):11,('Arrowhead',2):10,('Arrowhead',3):8,('Arrowhead',4):7,
    ('Horseshoe',1):11,('Horseshoe',2):10,('Horseshoe',3):8,('Horseshoe',4):7,
    ('GappedLine',1):11,('GappedLine',2):9,('GappedLine',3):7,
    ('RefusedFlank',1):11,('RefusedFlank',2):10,('RefusedFlank',3):9,
}

def make_unit(shape, tier, name, faction, unit_type='melee', power=4, command=4,
              discipline=5, morale=6, stance='balanced',
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

# (id, label, shape_a, shape_b, ua_kwargs, ub_kwargs, lo, hi) -- bands from v9 historical spec
TESTS = [
    ('H1','Line vs Line (mirror)','Line','Line',{},{},45,55),
    ('H2','Arrowhead vs Line','Arrowhead','Line',{},{},50,65),
    ('H3','Horseshoe vs Line','Horseshoe','Line',{},{},50,65),
    ('H4','Horseshoe vs Arrowhead (Cannae)','Horseshoe','Arrowhead',{},{},40,60),
    ('H5','RefusedFlank vs Horseshoe','RefusedFlank','Horseshoe',{},{},50,65),
    ('H6','RefusedFlank vs Line','RefusedFlank','Line',{},{},45,60),
    ('H7','GappedLine vs Line','GappedLine','Line',{},{},50,65),
    ('H8','GappedLine vs Arrowhead','GappedLine','Arrowhead',{},{},45,60),
    ('H9','Line vs Arrowhead (rev H2)','Line','Arrowhead',{},{},35,50),
    ('H10','Line vs Horseshoe (rev H3)','Line','Horseshoe',{},{},35,50),
    ('H11','Arrowhead vs Horseshoe (rev H4)','Arrowhead','Horseshoe',{},{},40,60),
    ('R1','Ranged vs Line (open field)','Line','Line',
        {'unit_type':'ranged','stance':'hold'},{},30,50),
    ('R3','Ranged vs Ranged (mirror)','Line','Line',
        {'unit_type':'ranged','stance':'hold'},{'unit_type':'ranged','stance':'hold'},45,55),
]

# --- Cavalry / speed / charge coverage (Phase 0, audit finding S2) ----------------
# PER_CELL=1 ONLY: cavalry charge_pen + PC_CAVALRY_SPEED_MULT are gated on PER_CELL in
# the engine, so these rows are appended only when PER_CELL is set (see __main__).
# Bands are HISTORICAL targets, calibrated against OBSERVED PER_CELL=1 behaviour so
# they are not fabricated; precedent cited per row. C1/C2 are a MINIMAL PAIR (identical
# cavalry Arrowhead attacker + Line defender; only the defender's stance/discipline
# differ) isolating the prepared-defence effect. C3 is a side-symmetry control. C4
# tests mounted envelopment.
CAV = {'troop_type':'cavalry','speed':'Fast'}
CAV_TESTS = [
    # C1: shock cavalry vs intact-but-UNBRACED infantry, frontal/open. Clear edge, not
    # annihilation (frontal charges into intact infantry were contested; the decisive
    # results came from broken or flanked foot). Observed PER_CELL=1 ~57.5% (vs the
    # infantry-Arrowhead control ~40%: the charge is worth ~+17pp). Precedent: shock
    # cavalry in the open. Sits at the low end -> charge_pen flat is the P4 lever.
    ('C1','Cav charge vs unprepared Line','Arrowhead','Line',
        dict(CAV),{},52,80),
    # C2: SAME cavalry vs SAME Line, but the defender is BRACED -- hold stance (cannot
    # advance, the Shield Wall signature) + discipline 8 (holds formation). Cavalry is
    # denied its edge and repelled to a stand-off (observed ~22.5%, ~60% draws).
    # Precedent: Waterloo squares 1815; Bannockburn/Falkirk schiltrons 1298-1314; pike
    # blocks. NOTE: the repulse is currently EMERGENT (hold + _defender_depth absorption
    # + discipline), NOT an explicit prepared-defence gate -> P3 anchor. This row guards
    # against a P2 penetration change making cavalry ahistorically dominant vs braced foot.
    ('C2','Cav charge vs BRACED Line (hold+d8)','Arrowhead','Line',
        dict(CAV),{'stance':'hold','discipline':8},8,42),
    # C3: cavalry vs cavalry mirror -- side-symmetry hygiene of the charge/momentum path
    # (guards against a fabricated A/B asymmetry from start-row or charge math). Must sit
    # ~even (observed exactly 50/50).
    ('C3','Cav vs Cav (mirror control)','Arrowhead','Arrowhead',
        dict(CAV),dict(CAV),42,58),
    # C4: mounted ENVELOPMENT. Horseshoe wings wrap the line -> octagon facing penalty
    # (RED >=90 deg = -2D) stacked with the charge. Mounted envelopment >> foot
    # envelopment (infantry Horseshoe vs Line ~60% -> cavalry ~85%, ~+25pp). Precedent:
    # Cannae rear-charge; Adrianople 378 flank; Hastings counter-charge on broken English.
    ('C4','Cav flank/envelopment vs Line','Horseshoe','Line',
        dict(CAV),{},70,92),
    # --- Phase 3 gate probes (shock primitive): isolate facing / brace / shaken ---
    # C5: cav vs an ALREADY-SHAKEN line (morale 2/6) -> shock amplifier fires; charge breaks a
    # wavering line. Precedent: Albuera (line caught -> ~76% loss); Hastings post-feint. HIGH.
    ('C5','Cav vs SHAKEN Line (morale2)','Arrowhead','Line',
        dict(CAV),{'morale':2},58,90),
    # C6: cav vs a BRACED but SHALLOW line (hold+disc8, no depth bonus) -> the square mechanic is
    # formation+discipline, not mass alone; a faced brace still repels frontally. LOW/contested.
    # (Tier-3 footprints are shallow, so this is brace-without-depth by construction.) Precedent:
    # Waterloo squares held frontally; "best cavalry is contemptible to a steady regiment."
    ('C6','Cav vs BRACED-shallow Line (hold+d8)','Arrowhead','Line',
        dict(CAV),{'stance':'hold','discipline':8},8,45),
    # C7: cav ENVELOPS a braced line (Horseshoe vs hold+disc8) -> bracing is BYPASSED from the
    # flank/rear (octagon RED); you cannot face what wraps you. Precedent: Cannae/Adrianople — an
    # encircled disciplined body still collapses. Must be >> C6 (frontal brace) and >= C2. HIGH.
    ('C7','Cav envelop vs BRACED Line (hold+d8)','Horseshoe','Line',
        dict(CAV),{'stance':'hold','discipline':8},55,88),
]

def winner_of(r):
    return r.get('winner','draw')

def matchup(sa, sb, ka, kb, mode, n=60, seed_base=1_000_000):  # [canonical: tests/sim/sim_mb_06_v9_historical_spec.md — n=60 sample, deterministic seed base]
    aw=bw=dr=0; turns=[]; a_cas=[]; b_cas=[]
    for s in range(n):
        random.seed(s+seed_base)
        ua=make_unit(sa,3,'A','A',**ka); ub=make_unit(sb,3,'B','B',**kb)
        a0,b0 = ua.hp_max, ub.hp_max
        if mode=='single':
            r=run_battle(ua,ub,max_turns=18)
            turns.append(r.get('turns',18))
        else:
            r=run_multi_turn_battle(ua,ub,sa,sb,ANCHOR_MAP,max_battle_turns=20)
            turns.append(r.get('battle_turns',20))
        w=winner_of(r)
        if w=='A':aw+=1
        elif w=='B':bw+=1
        else:dr+=1
        a_cas.append(100*(a0-ua.hp)/a0 if a0 else 0)
        b_cas.append(100*(b0-ub.hp)/b0 if b0 else 0)
    return dict(a=aw/n*100,b=bw/n*100,d=dr/n*100,
                t=statistics.mean(turns),
                a_cas=statistics.mean(a_cas),b_cas=statistics.mean(b_cas))

def run(mode, tests=TESTS):
    print(f"\n----- MODE: {mode}  (engine: {ENGINE.split('/')[-1]}) -----")
    print(f"  {'id':4} {'matchup':32} {'A%':>5} {'B%':>5} {'D%':>5} {'t':>4} {'casA%':>6} {'casB%':>6}  band   verdict")
    nb=0
    for tid,label,sa,sb,ka,kb,lo,hi in tests:
        r=matchup(sa,sb,ka,kb,mode)
        ok = lo<=r['a']<=hi
        nb+=ok
        print(f"  {tid:4} {label[:32]:32} {r['a']:5.1f} {r['b']:5.1f} {r['d']:5.1f} {r['t']:4.1f} "
              f"{r['a_cas']:6.1f} {r['b_cas']:6.1f}  {lo:>2}-{hi:<2} {'OK' if ok else 'OUT'}")
    print(f"  => in-band {nb}/{len(tests)} ({nb*100//len(tests)}%)")
    return nb

if __name__=='__main__':
    # Cavalry rows are PER_CELL=1-only (engine gates charge_pen + speed mult on PER_CELL).
    # Under PER_CELL=0 only the original 13 run -> output stays byte-identical to baseline.
    _pc = os.environ.get('PER_CELL','0') not in ('0','','false','False','no','No')
    _tests = TESTS + (CAV_TESTS if _pc else [])
    s=run('single', _tests); m=run('multi', _tests)
    n=len(_tests)
    print(f"\n==== {ENGINE.split('/')[-1]}: single={s}/{n}  multi={m}/{n} ====")
