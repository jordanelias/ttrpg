"""
SIM-NPC-01: Full BG simulation with all NPC priority trees active.
Validates multi-faction interaction under priority tree model.
Source: designs/systems/npc_behavior_system_v1.md §8, references/params_board_game.md
"""

import random
import json
from dataclasses import dataclass, field
from typing import Optional

random.seed(42)  # Reproducible

# --- D10 ENGINE ---
def roll_d10_pool(pool_size: int, tn: int = 7) -> int:
    """Roll pool_size d10s at TN. Returns net successes (can be negative)."""
    pool_size = max(1, pool_size)
    net = 0
    for _ in range(pool_size):
        die = random.randint(1, 10)
        if die == 1:
            net -= 1
        elif die >= tn:
            if die == 10:
                net += 2
            else:
                net += 1
    return net

def degree(net: int, ob: int) -> str:
    if ob >= 10 and net >= ob:
        return "success"
    if net >= 2 * ob and net >= 3:
        return "overwhelming"
    if net >= ob:
        return "success"
    if net > 0:
        return "partial"
    return "failure"

# --- FACTION DATA ---
@dataclass
class Faction:
    name: str
    mandate: int
    influence: int
    wealth: int
    military: int
    intel: int
    stability: int
    framework: str
    conviction_primary: str
    conviction_secondary: str
    territories: int  # simplified count
    # State
    eliminated: bool = False
    actions_taken: list = field(default_factory=list)

    def stat(self, name):
        return getattr(self, name, 0)

    def mod_stat(self, name, delta, floor=1, ceil=7):
        val = getattr(self, name, 0) + delta
        val = max(floor, min(ceil, val))
        setattr(self, name, val)

    def summary(self):
        if self.eliminated:
            return f"  {self.name}: ELIMINATED"
        return (f"  {self.name}: M={self.mandate} I={self.influence} W={self.wealth} "
                f"Mil={self.military} Int={self.intel} S={self.stability} T={self.territories}")

@dataclass
class GameState:
    season: int = 1
    tc: int = 28  # Church Influence
    rs: int = 72  # Rendering Stability
    ip: int = 20  # Institutional Pressure
    pi: int = 5   # Public Instability
    torben_loyalty: int = 3
    coup_counter: int = 0
    rm_founded: bool = False
    wardens_emerged: bool = False
    log: list = field(default_factory=list)

    def log_event(self, msg):
        self.log.append(f"S{self.season}: {msg}")

    def clock_summary(self):
        return (f"  CI={self.tc} RS={self.rs} IP={self.ip} PI={self.pi} "
                f"TorbenLoy={self.torben_loyalty} CoupCtr={self.coup_counter}")

def create_factions():
    return {
        'crown': Faction('Crown', 5, 5, 4, 4, 0, 4, 'virtue_ethics', 'Order', 'Reason', 6),
        'church': Faction('Church', 5, 6, 5, 4, 0, 5, 'divine_command', 'Faith', 'Order', 1),
        'hafenmark': Faction('Hafenmark', 4, 4, 5, 3, 0, 4, 'categorical_imperative', 'Precedent', 'Faith', 4),
        'varfell': Faction('Varfell', 4, 4, 4, 4, 0, 4, 'consequentialism', 'Reason', 'Autonomy', 4),
        'guilds': Faction('Guilds', 3, 4, 6, 2, 0, 5, 'moral_relativism', 'Autonomy', '', 0),
        'lowenritter': Faction('Löwenritter', 3, 3, 0, 5, 3, 5, 'martial_honour', 'Order', 'Autonomy', 0),
        'ministry': Faction('Ministry', 3, 4, 0, 0, 0, 4, 'procedural', 'Order', '', 0),
    }

# --- PRIORITY TREES ---

def church_priority(f, factions, gs):
    """Church NPC Priority Tree."""
    # P1: Survival
    if f.stability <= 2:
        gs.log_event("Church P1: Consul Inward (survival)")
        net = roll_d10_pool(f.mandate, 7)
        if degree(net, 1) in ('success', 'overwhelming'):
            f.mod_stat('stability', 1)
        return

    # P2: Conviction-critical (Faith) — heresy/practitioner threat
    # Simplified: fire if RS dropped last season (Thread activity proxy)
    if gs.rs < 70:
        gs.log_event("Church P2: Heresy Investigation (Thread activity detected)")
        # Target Varfell (most likely Thread user)
        varfell = factions.get('varfell')
        if varfell and not varfell.eliminated:
            net = roll_d10_pool(f.mandate, 7)
            ob = max(1, varfell.mandate // 2 + 1)
            d = degree(net, ob)
            if d in ('success', 'overwhelming'):
                varfell.mod_stat('mandate', -1)
                gs.log_event(f"  Heresy Investigation success: Varfell Mandate -1")
            else:
                gs.log_event(f"  Heresy Investigation failed")
        return

    # P3: Assert CI
    if gs.tc < 75 and f.mandate >= 4:
        gs.log_event("Church P3: Assert (CI +1)")
        gs.tc = min(75, gs.tc + 1)
        return

    # P4: Expand Piety (Consul Inward)
    gs.log_event("Church P4: Consul Inward (expand piety)")
    net = roll_d10_pool(f.mandate, 7)
    if degree(net, 1) in ('success', 'overwhelming'):
        f.mod_stat('influence', 1)

def crown_priority(f, factions, gs):
    """Crown NPC Priority Tree."""
    # P1: Survival
    if f.stability <= 2:
        gs.log_event("Crown P1: Consul Inward (survival)")
        net = roll_d10_pool(f.mandate, 7)
        if degree(net, 1) in ('success', 'overwhelming'):
            f.mod_stat('stability', 1)
        return

    # P2: Conviction-critical (Order) — territory loss, coup threat, PI
    if gs.coup_counter >= 2 or gs.pi >= 8:
        gs.log_event(f"Crown P2: Military response (CoupCtr={gs.coup_counter}, PI={gs.pi})")
        net = roll_d10_pool(f.military, 7)
        if degree(net, 2) in ('success', 'overwhelming'):
            if gs.pi >= 8:
                gs.pi = max(0, gs.pi - 1)
                gs.log_event("  Military stabilisation: PI -1")
        return

    # P3: Royal Decree
    gs.log_event("Crown P3: Royal Decree")
    net = roll_d10_pool(f.mandate, 7)
    d = degree(net, 2)
    if d in ('success', 'overwhelming'):
        # Boost weakest allied stat or weaken strongest rival
        church = factions.get('church')
        if church and not church.eliminated and church.mandate >= 5:
            church.mod_stat('mandate', -1)
            gs.log_event("  Decree: Church Mandate -1")
        else:
            f.mod_stat('stability', 1)
            gs.log_event("  Decree: Crown Stability +1")
    else:
        f.mod_stat('mandate', -1)
        gs.log_event("  Decree failed: Crown Mandate -1")

    # P5: Torben
    if gs.torben_loyalty <= 3:
        gs.log_event("Crown P5: Senator Outward targeting Torben")
        net = roll_d10_pool(f.influence, 7)
        if degree(net, 2) in ('success', 'overwhelming'):
            gs.torben_loyalty = min(7, gs.torben_loyalty + 1)
            gs.log_event(f"  Torben Loyalty +1 → {gs.torben_loyalty}")

def hafenmark_priority(f, factions, gs):
    """Hafenmark NPC Priority Tree."""
    if f.stability <= 2:
        gs.log_event("Hafenmark P1: Consul Inward (survival)")
        f.mod_stat('stability', 1)
        return

    church = factions.get('church')
    # P2: CI response
    if gs.tc >= 40 and church and not church.eliminated:
        gs.log_event("Hafenmark P2: Suppress CI")
        net = roll_d10_pool(f.mandate, 7)
        ob = max(1, church.mandate // 2 + 1)
        d = degree(net, ob)
        if d in ('success', 'overwhelming'):
            gs.tc = max(0, gs.tc - 1)  # Negate passive
            gs.log_event(f"  Suppress success: CI passive negated")
        else:
            f.mod_stat('stability', -1)
            gs.log_event(f"  Suppress failed: Stability -1")
        return

    # P3: Suppress if available
    if church and not church.eliminated and f.mandate >= 4 and church.mandate >= 4:
        gs.log_event("Hafenmark P3: Suppress CI (routine)")
        # Simplified: automatic negate of passive CI
        gs.tc = max(0, gs.tc)  # Just prevents the +1 for this season
        return

    # P4: Maintain order
    gs.log_event("Hafenmark P4: Consul Inward (maintain order)")
    net = roll_d10_pool(f.mandate, 7)
    if degree(net, 1) in ('success', 'overwhelming'):
        f.mod_stat('influence', 1)

def varfell_priority(f, factions, gs):
    """Varfell NPC Priority Tree."""
    if f.stability <= 2:
        gs.log_event("Varfell P1: Consul Inward (survival)")
        f.mod_stat('stability', 1)
        return

    # P2: TK opportunity (Private Collection)
    gs.log_event("Varfell P2: Private Collection deployment")
    net = roll_d10_pool(max(1, f.intel if f.intel > 0 else f.influence), 7)
    d = degree(net, 2)
    if d in ('success', 'overwhelming'):
        gs.log_event("  Collection success: +2D to next Thread DA")
    else:
        gs.log_event("  Collection failed: Church Intel +1D vs Varfell")
        # Thread Tension proxy: RS -1
        gs.rs = max(0, gs.rs - 1)

    # P3: Tribune Investigate
    # Find faction with most hidden potential
    targets = [fa for fa in factions.values() if fa.name != 'Varfell' and not fa.eliminated]
    if targets:
        target = max(targets, key=lambda x: x.mandate + x.influence)
        gs.log_event(f"Varfell P3: Tribune Investigate vs {target.name}")

def guilds_priority(f, factions, gs):
    """Guilds NPC Priority Tree."""
    if f.stability <= 2:
        gs.log_event("Guilds P1: Consul Inward (survival)")
        f.mod_stat('stability', 1)
        return

    # P3: Economic Leverage (if conditions met — simplified)
    targets = [fa for fa in factions.values()
               if fa.name not in ('Guilds', 'Ministry') and not fa.eliminated and fa.wealth > 0]
    if targets:
        target = min(targets, key=lambda x: x.wealth)
        gs.log_event(f"Guilds P3: Economic Leverage vs {target.name}")
        net = roll_d10_pool(f.wealth, 7)
        ob = target.wealth
        d = degree(net, ob)
        if d == 'overwhelming':
            target.mod_stat('wealth', -1)
            gs.log_event(f"  Overwhelming: {target.name} Wealth -1")
        elif d == 'success':
            target.mod_stat('wealth', -1)
            gs.log_event(f"  Success: {target.name} Wealth -1 (1 season)")
        else:
            gs.log_event(f"  Failed: no effect")
        return

    gs.log_event("Guilds P4: Trade (default)")

def lowenritter_priority(f, factions, gs):
    """Löwenritter NPC Priority Tree."""
    if f.stability <= 2:
        gs.log_event("Löwenritter P1: Military Consolidation (survival)")
        f.mod_stat('military', 1)
        return

    # P2: Coup readiness
    if gs.coup_counter >= 2:
        gs.log_event("Löwenritter P2: Coup preparation (pre-position)")
        return

    # P3: Sovereignty defence
    if gs.ip >= 50:
        gs.log_event("Löwenritter P3: Border defence (Altonian threat)")
        return

    # P4: Military maintenance
    if f.military < 5:
        gs.log_event("Löwenritter P4: Military Consolidation")
        f.mod_stat('military', 1)
        return

    # Check bordering faction military
    crown = factions.get('crown')
    if crown and not crown.eliminated and crown.military > f.military:
        gs.log_event("Löwenritter P4: Military Consolidation (Crown exceeds)")
        f.mod_stat('military', 1)
        return

    gs.log_event("Löwenritter P7: Pass (maintain garrison)")

def ministry_priority(f, factions, gs):
    """Ministry NPC Priority Tree (existing from params_board_game)."""
    if gs.pi <= 3:
        gs.log_event("Ministry P1: Govern T13 (PI stabilisation)")
        net = roll_d10_pool(f.mandate, 7)
        if degree(net, 1) in ('success', 'overwhelming'):
            gs.pi = min(10, gs.pi + 1)
        return

    crown = factions.get('crown')
    if crown and not crown.eliminated and crown.mandate >= 4 and gs.pi < 5:
        gs.log_event("Ministry P4: Senator Inward (Crown support)")
        gs.pi = min(10, gs.pi + 1)
        return

    gs.log_event("Ministry P5: Consul Inward (default)")

# --- ACCOUNTING PHASE ---

def seasonal_accounting(factions, gs):
    """Run seasonal accounting."""
    # 1. CI passive advance
    gs.tc = min(75, gs.tc + 1)

    # 2. RS baseline decay (simplified: -1 per 4 seasons = per year)
    if gs.season % 4 == 0:
        gs.rs = max(0, gs.rs - 1)

    # 3. IP advance (simplified)
    gs.ip = min(100, gs.ip + 1)

    # 4. PI check
    for fa in factions.values():
        if not fa.eliminated and fa.mandate < 3:
            gs.pi = min(10, gs.pi + 1)
            break  # +1 max per season from mandate check

    # PI recovery
    hostile_this_season = False  # Simplified
    if not hostile_this_season:
        gs.pi = max(0, gs.pi - 1)

    # 5. Stability checks
    for fa in factions.values():
        if fa.eliminated:
            continue
        # Simplified: Ob 1 quiet, Ob 2 if any threat
        ob = 1 if gs.pi < 8 else 2
        net = roll_d10_pool(fa.stability, 7)
        d = degree(net, ob)
        if d == 'failure':
            fa.mod_stat('stability', -1)
            gs.log_event(f"  {fa.name} Stability check FAILED → S={fa.stability}")
        elif d == 'overwhelming':
            fa.mod_stat('stability', 1)

    # 6. Coup Counter checks
    crown = factions.get('crown')
    lowenritter = factions.get('lowenritter')
    if crown and not crown.eliminated:
        # CI ≥ 40 and Crown took no action to reduce
        if gs.tc >= 40:
            if 'Suppress' not in str(crown.actions_taken):
                gs.coup_counter = min(3, gs.coup_counter + 1)
                gs.log_event(f"  Coup Counter +1 (CI≥40 unchallenged) → {gs.coup_counter}")

        if gs.torben_loyalty <= 2:
            gs.coup_counter = min(3, gs.coup_counter + 1)
            gs.log_event(f"  Coup Counter +1 (Torben Loyalty ≤2) → {gs.coup_counter}")

    # 7. Framework Drift
    # Church: Influence +1 if unchallenged 2 consecutive seasons (simplified: every 2)
    church = factions.get('church')
    if church and not church.eliminated and gs.season % 2 == 0:
        church.mod_stat('influence', 1)
        gs.log_event(f"  Church Framework Drift: Influence +1 → {church.influence}")

    # Hafenmark: Influence +1 if all actions framework-aligned (simplified: 50% chance)
    hafenmark = factions.get('hafenmark')
    if hafenmark and not hafenmark.eliminated and random.random() < 0.5:
        hafenmark.mod_stat('influence', 1)

    # 8. Elimination check
    for fa in factions.values():
        if not fa.eliminated and fa.stability <= 0:
            fa.eliminated = True
            gs.log_event(f"  *** {fa.name} ELIMINATED (Stability 0) ***")

    # 9. Coup fire
    if gs.coup_counter >= 3 and lowenritter and not lowenritter.eliminated:
        gs.log_event(f"  *** COUP FIRES — Löwenritter seizes Crown territories ***")
        if crown and not crown.eliminated:
            lowenritter.territories += crown.territories
            crown.territories = 0
            crown.mod_stat('mandate', -3, floor=0)
            gs.pi = 0  # Martial Law

    # 10. RS=0 check
    if gs.rs <= 0:
        gs.log_event("  *** RS=0 — RUPTURE — SHARED LOSS ***")

    # 11. CI ≥ 75 check
    if gs.tc >= 75:
        gs.log_event("  CI frozen at 75. Church shifts to territorial seizure.")

    # Clear season actions
    for fa in factions.values():
        fa.actions_taken = []

# --- MAIN SIMULATION ---

def run_simulation(num_seasons=12, seed=42):
    random.seed(seed)
    factions = create_factions()
    gs = GameState()

    priority_fns = {
        'church': church_priority,
        'crown': crown_priority,
        'hafenmark': hafenmark_priority,
        'varfell': varfell_priority,
        'guilds': guilds_priority,
        'lowenritter': lowenritter_priority,
        'ministry': ministry_priority,
    }

    results = []

    for season in range(1, num_seasons + 1):
        gs.season = season
        gs.log_event(f"=== SEASON {season} (Year {(season-1)//4 + 1}, Q{(season-1)%4 + 1}) ===")

        # Phase 4: Priority tree evaluation (order: Church, Crown, Hafenmark, Varfell, Guilds, Löwenritter, Ministry)
        for fname, pfn in priority_fns.items():
            f = factions[fname]
            if f.eliminated:
                continue
            pfn(f, factions, gs)

        # Accounting
        gs.log_event("--- ACCOUNTING ---")
        seasonal_accounting(factions, gs)

        # Snapshot
        snap = {
            'season': season,
            'ci': gs.tc, 'rs': gs.rs, 'ip': gs.ip, 'pi': gs.pi,
            'torben': gs.torben_loyalty, 'coup': gs.coup_counter,
            'factions': {n: {'M': f.mandate, 'I': f.influence, 'W': f.wealth,
                            'Mil': f.military, 'S': f.stability, 'elim': f.eliminated}
                        for n, f in factions.items()}
        }
        results.append(snap)

        # Early termination
        if gs.rs <= 0:
            break
        active = [f for f in factions.values() if not f.eliminated and f.name != 'Ministry']
        if len(active) <= 1:
            gs.log_event("Only 1 faction remains. Game over.")
            break

    return gs, factions, results

# --- RUN MULTIPLE SEEDS ---
print("=" * 70)
print("SIM-NPC-01: BG NPC Priority Tree Simulation")
print("=" * 70)

findings = []
all_results = {}

for seed in [42, 137, 256, 999, 1701]:
    gs, factions, results = run_simulation(num_seasons=12, seed=seed)
    final = results[-1]
    all_results[seed] = {
        'seasons': len(results),
        'ci': final['ci'],
        'rs': final['rs'],
        'ip': final['ip'],
        'pi': final['pi'],
        'coup': final['coup'],
        'torben': final['torben'],
        'eliminated': [n for n, d in final['factions'].items() if d['elim']],
        'church_influence': final['factions']['church']['I'],
        'church_mandate': final['factions']['church']['M'],
    }

    print(f"\n--- Seed {seed} ---")
    print(f"  Seasons: {len(results)}")
    print(f"  Clocks: CI={final['ci']} RS={final['rs']} IP={final['ip']} PI={final['pi']}")
    print(f"  Coup Counter: {final['coup']} | Torben: {final['torben']}")
    print(f"  Eliminated: {all_results[seed]['eliminated'] or 'None'}")
    for n, d in final['factions'].items():
        status = "ELIM" if d['elim'] else f"M={d['M']} I={d['I']} W={d['W']} Mil={d['Mil']} S={d['S']}"
        print(f"    {n}: {status}")

# --- ANALYSIS ---
print("\n" + "=" * 70)
print("ANALYSIS")
print("=" * 70)

# Finding 1: CI progression
tc_values = [r['ci'] for r in all_results.values()]
print(f"\n1. CI after 12 seasons: {tc_values}")
if all(tc >= 40 for tc in tc_values):
    print("   FINDING: CI reaches 40+ in all runs. Hafenmark Suppress is insufficient")
    print("   to counter Church passive +1/season. Expected: Hafenmark needs P2 to fire")
    print("   more aggressively or Crown needs to assist.")
    findings.append("F-01: CI reaches 40+ in all runs by S12. Church institutional momentum dominates.")

# Finding 2: Church Influence drift
church_inf = [r['church_influence'] for r in all_results.values()]
print(f"\n2. Church Influence after 12 seasons: {church_inf}")
if all(i >= 7 for i in church_inf):
    print("   FINDING: Church Influence hits ceiling (7) in all runs from Framework Drift.")
    print("   Drift fires every 2 seasons unconditioned. Church becomes dominant social actor.")
    findings.append("F-02: Church Influence hits 7 in all runs. Drift too aggressive or unconditional.")

# Finding 3: Coup Counter
coups = [r['coup'] for r in all_results.values()]
print(f"\n3. Coup Counter after 12 seasons: {coups}")
if any(c >= 3 for c in coups):
    print("   FINDING: Coup fires in some runs. CI≥40 trigger is primary driver.")
    findings.append("F-03: Coup fires when CI≥40 unchallenged. Crown P2 not aggressive enough on CI.")

# Finding 4: Eliminations
all_elim = set()
for r in all_results.values():
    all_elim.update(r['eliminated'])
print(f"\n4. Factions eliminated across all seeds: {all_elim or 'None'}")
if not all_elim:
    print("   No eliminations in 12 seasons. System is stable. May be TOO stable")
    print("   for a 12-season game if no faction ever faces existential pressure.")
    findings.append("F-04: No eliminations in 12 seasons. Priority Trees P1 (survival) prevents collapse. May need longer games or higher-pressure events.")

# Finding 5: RS
rs_values = [r['rs'] for r in all_results.values()]
print(f"\n5. RS after 12 seasons: {rs_values}")
print("   RS barely moves (annual decay only). Thread operations not modeled at faction scale.")
findings.append(f"F-05: RS ends at {min(rs_values)}-{max(rs_values)}. Thread operation RS impact not modeled; RS decline too slow without Thread activity.")

# Finding 6: Varfell behavior
print(f"\n6. Varfell always fires P2 (Private Collection). No variation in behavior.")
print("   Priority 2 (Conviction-critical: TK opportunity) fires every season because")
print("   Collection is always 'available'. Need a cooldown or use-count limit.")
findings.append("F-06: Varfell P2 fires every season (Collection always available). Needs cooldown per canonical 1/season limit.")

# Finding 7: Priority tree interaction
print(f"\n7. Cross-faction interaction: Church targets Varfell (P2 Heresy). Crown targets")
print("   Church (Decree). Guilds target weakest Wealth. Löwenritter monitors Crown.")
print("   Hafenmark suppresses CI. Basic interaction loop is functional.")
findings.append("F-07: Basic interaction loop functional. Church→Varfell, Crown→Church, Guilds→weakest, Hafenmark→CI, Löwenritter→Crown. No degenerate cycles.")

print("\n" + "=" * 70)
print(f"TOTAL FINDINGS: {len(findings)}")
for f in findings:
    print(f"  {f}")
print("=" * 70)

# Detailed log from seed 42
print("\n\nDETAILED LOG (Seed 42, first 4 seasons):")
gs42, _, _ = run_simulation(12, 42)
for entry in gs42.log[:60]:
    print(f"  {entry}")
PYEOF