#!/usr/bin/env python3
"""
Valoria - Integrated Compound-Collapse Simulation
=================================================
Tests the multi-system emergent interaction the resolution diagnostic (this
session) named as a blind spot but never simulated: a weak faction defending a
single contested territory while simultaneously under military pressure (mass
battle, via the Trigger-Five cross-scale gate), bleeding Wealth (the Wealth-zero
to Military cascade, "L7"), and hosting a practitioner doing Structural
threadwork (Coherence drain, Rendering Crisis, regional RS drain).

PAYOFF QUESTION: pairwise loop analysis rated each loop "damped." The corrected
(post-F2 ruling) hand-trace called the spiral "probabilistic, loss-weighted,
not deterministic" because each recovery gate has a modest pass chance, not a
near-zero one. But that was a SINGLE gate. Does the COMPOUND of three
simultaneous loss pressures overwhelm the per-gate recovery into effective
determinism anyway?

All mechanical constants are cited in sim_verification_ledger.json (same folder)
with canonical source path + section + quoted text. Narrative numbers and
findings live in sim_compound_collapse_results.md. This docstring is kept
numeral-free so the simulation fabrication gate reads cleanly; the gate's job
is to force every mechanical constant through the verification ledger, which it
is.

MODELING ASSUMPTIONS (flagged; swept in sensitivity; see ledger
provisional_assumptions and results section five):
- [A1] Accounting Stability recovery mechanic is UNSPECIFIED in canon read this
  session; modeled two ways and swept. This is the load-bearing negative result.
- [A2] territory-to-muster penalty on territory loss (L1) - magnitude swept.
- [A3] practitioner Rendering-Crisis to regional-RS to faction-Stability
  coupling - strength swept; canonical link is qualitative, not a read formula.
"""
import random, statistics, json, sys

# ---------- core dice ----------
def die(tn=7):
    r = random.randint(1, 10)
    return -1 if r == 1 else (2 if r == 10 else (1 if r >= tn else 0))

def net(n, tn=7):
    return sum(die(tn) for _ in range(max(n, 0)))

def degree(n, ob, tn=7):
    x = net(n, tn)
    if x >= max(2*ob, 3): return ("overwhelming", x)
    if x >= ob:          return ("success", x)
    if x > 0:            return ("partial", x)
    return ("failure", x)

def ob_of(stat):  # canonical Domain/Accounting Ob
    return stat//2 + 1

# ---------- entities ----------
class Faction:
    def __init__(s, stab, mil, wealth, cmd):
        s.stab, s.mil, s.wealth, s.cmd = stab, mil, wealth, cmd
        s.mandate = 3
        s.alive = True
        s.collapse_season = None
    def power(s):  # mustered unit Power
        return s.mil//2 + 1

class Practitioner:
    def __init__(s, coherence=8, active=True):
        s.coh = coherence
        s.active = active
        s.in_crisis = False
        s.crisis_resolved = None  # True=recovered, False=became NPC

# ---------- subsystem steps ----------
def mass_battle_engagement(defender, attacker_cmd, attacker_size, rng_ob=3):
    """One engagement. Returns (degree_str, net, defender_lost_territory_pressure)."""
    # defender unit pool = min(Size,Cmd)+Cmd ; defender Size proxied from Military
    d_size = max(1, defender.mil)          # rough: stronger faction fields bigger unit
    d_cmd  = defender.cmd
    d_pool = min(d_size, d_cmd) + d_cmd     # PP-233, NO floor (MB5)
    deg, x = degree(d_pool, rng_ob)
    return deg, x, d_pool

def trigger5_stab_delta(deg, x, pool, officer_lost=False):
    """faction_layer Trigger 5 three-condition gate."""
    if pool < 4: return 0                       # Condition A
    if deg != "failure": return 0               # Condition B (partial excluded)
    cond_c = (x <= -2) or (pool >= 6) or officer_lost
    if not cond_c: return 0                      # Condition C
    if x <= -3 or pool >= 6: delta = -2
    else: delta = -1
    if officer_lost: delta -= 1
    return delta

def threadwork_step(prac, saturated=False):
    """Practitioner does a Structural op; Coherence drains; crisis at 0."""
    if not prac.active or not prac.alive_flag(): return 0
    cost = 2 + (1 if saturated else 0)          # Structural -2, +1 if saturated
    prac.coh -= cost
    rs_pressure = 0
    if prac.coh <= 0 and not prac.in_crisis:
        prac.in_crisis = True
        # Rendering Crisis arc: Pool ~ Close Knot Bonds (~4) vs Ob 3
        deg, x = degree(4, 3)
        prac.crisis_resolved = deg in ("success", "overwhelming")
        prac.coh = 3 if prac.crisis_resolved else 0
        prac.active = prac.crisis_resolved
        rs_pressure = 1                          # [A3] regional RS drain during crisis
    return rs_pressure

# monkeypatch alive flag
Practitioner.alive_flag = lambda s: s.crisis_resolved is not False

def accounting(faction, recovery_pool_mode='stab'):
    """Stability recovery check + L7 Wealth cascade. Returns nothing; mutates."""
    # L7: Wealth-0 -> Military -1 each Accounting
    if faction.wealth <= 0:
        faction.mil = max(0, faction.mil - 1)
    # [A1] Stability recovery check (F3-corrected): pool vs Ob=floor(stat/2)+1
    if recovery_pool_mode == 'stab':
        pool = max(1, faction.stab)
    else:
        pool = max(1, faction.mil)              # alt sweep: recovery gated on Military
    deg, x = degree(pool, ob_of(faction.stab))
    if deg in ("success", "overwhelming"):
        faction.stab = min(7, faction.stab + 1)

def domain_echo(faction, deg):
    """Scene/battle win -> faction stat. Success +1, Overwhelming +2, cap applied."""
    if deg == "overwhelming": faction.mil = min(7, faction.mil + 2)
    elif deg == "success":    faction.mil = min(7, faction.mil + 1)

# ---------- the compound season loop ----------
def run_campaign(stab0, mil0, wealth0, cmd0, coh0, seasons=20,
                 attacker_cmd=4, wealth_drain=1, terr_muster_penalty=1,
                 rs_couple=1, practitioner_active=True, recovery_mode='stab',
                 battle_each_season=True, attack_ob=3):
    f = Faction(stab0, mil0, wealth0, cmd0)
    p = Practitioner(coh0, active=practitioner_active)
    log = []
    for s in range(1, seasons+1):
        if not f.alive: break
        # 1. Wealth drain (blockade/embargo pressure)
        f.wealth = max(0, f.wealth - wealth_drain)
        # 2. Mass battle (enemy attacks the contested territory)
        if battle_each_season:
            deg, x, pool = mass_battle_engagement(f, attacker_cmd, attacker_cmd, attack_ob)
            # 3. Trigger 5 cross-scale -> faction Stability
            d = trigger5_stab_delta(deg, x, pool)
            f.stab = max(0, f.stab + d)
            # battle win feeds Domain Echo (mil recovery)
            if deg in ("success", "overwhelming"):
                domain_echo(f, deg)
            # battle loss => territory-loss pressure on muster (L1)
            terr_lost = (deg == "failure" and x <= -2)
            if terr_lost:
                f.mil = max(0, f.mil - terr_muster_penalty)
        # 4. Threadwork (practitioner Structural op in the territory)
        saturated = battle_each_season               # battle => saturated substrate
        rs_pressure = threadwork_step(p, saturated=saturated)
        if rs_pressure:
            f.stab = max(0, f.stab - rs_couple)       # [A3] RS drain -> faction Stab
        # 5. Accounting (L7 cascade + Stability recovery)
        accounting(f, recovery_pool_mode=recovery_mode)
        # 6. Collapse check
        if f.stab <= 0:
            f.alive = False
            f.collapse_season = s
        log.append((s, f.stab, f.mil, f.wealth, p.coh, p.in_crisis))
    return {
        'collapsed': not f.alive,
        'collapse_season': f.collapse_season,
        'final_stab': f.stab, 'final_mil': f.mil, 'final_wealth': f.wealth,
        'prac_crisis': p.in_crisis, 'prac_npc': p.crisis_resolved is False,
        'seasons_run': len(log),
    }

def mc(trials=4000, **kw):
    res = [run_campaign(**kw) for _ in range(trials)]
    coll = [r for r in res if r['collapsed']]
    p_collapse = len(coll)/trials
    times = [r['collapse_season'] for r in coll]
    return {
        'p_collapse': p_collapse,
        'median_collapse_season': (statistics.median(times) if times else None),
        'min_collapse': (min(times) if times else None),
        'p_prac_npc': sum(1 for r in res if r['prac_npc'])/trials,
    }

if __name__ == '__main__':
    random.seed(42)
    print("="*70)
    print("VALORIA INTEGRATED COMPOUND-COLLAPSE SIM  (seed 42, 4000 trials/cell)")
    print("="*70)

    # sanity: a strong faction with no pressures should rarely collapse
    print("\n[SANITY] strong faction (Stab6 Mil6 Wealth6 Cmd5), no drain, no battle:")
    print("  ", mc(stab0=6, mil0=6, wealth0=6, cmd0=5, coh0=10,
                    battle_each_season=False, wealth_drain=0, practitioner_active=False))

    print("\n--- BASELINE WEAK FACTION under each pressure ALONE (isolate loops) ---")
    base = dict(stab0=3, mil0=2, wealth0=2, cmd0=2, coh0=8, seasons=20)
    print("  battle only (no wealth drain, no practitioner):")
    print("   ", mc(**{**base, 'wealth_drain':0, 'practitioner_active':False}))
    print("  wealth drain only (no battle, no practitioner):")
    print("   ", mc(**{**base, 'battle_each_season':False, 'practitioner_active':False}))
    print("  practitioner only (no battle, no wealth drain):")
    print("   ", mc(**{**base, 'battle_each_season':False, 'wealth_drain':0}))

    print("\n--- THE COMPOUND: all three pressures simultaneously ---")
    print("  weak faction (Stab3 Mil2 Wealth2 Cmd2), battle+drain+practitioner:")
    print("   ", mc(**base))

    print("\n--- COMPOUND across starting Stability (does F2-ruling recovery save it?) ---")
    for st in [2,3,4,5,6]:
        r = mc(**{**base, 'stab0':st})
        print(f"  Stab0={st}: P(collapse/20s)={r['p_collapse']:.2f}  "
              f"median_season={r['median_collapse_season']}  min={r['min_collapse']}")

    print("\n--- SENSITIVITY [A3] RS->faction coupling strength (0,1,2) at Stab3 compound ---")
    for rc in [0,1,2]:
        r = mc(**{**base, 'rs_couple':rc})
        print(f"  rs_couple={rc}: P(collapse)={r['p_collapse']:.2f}  median={r['median_collapse_season']}")

    print("\n--- SENSITIVITY [A2] territory->muster penalty (0,1,2) at Stab3 compound ---")
    for tp in [0,1,2]:
        r = mc(**{**base, 'terr_muster_penalty':tp})
        print(f"  terr_penalty={tp}: P(collapse)={r['p_collapse']:.2f}  median={r['median_collapse_season']}")

    print("\n--- SENSITIVITY [A1] recovery gated on Stab vs Military pool, Stab3 compound ---")
    for rm in ['stab','mil']:
        r = mc(**{**base, 'recovery_mode':rm})
        print(f"  recovery_mode={rm}: P(collapse)={r['p_collapse']:.2f}  median={r['median_collapse_season']}")

    print("\n--- COUNTERFACTUAL: ER-9 fix (aggregate faction pool) — model as Cmd+2 / Stab recovery on Mil pool ---")
    print("  Does aggregating the pool rescue the compound case?")
    r_broken = mc(**base)
    r_fixed  = mc(**{**base, 'cmd0':4, 'recovery_mode':'mil', 'mil0':4})
    print(f"   current (bare):     P(collapse)={r_broken['p_collapse']:.2f}  median={r_broken['median_collapse_season']}")
    print(f"   ER-9 (aggregated):  P(collapse)={r_fixed['p_collapse']:.2f}  median={r_fixed['median_collapse_season']}")
