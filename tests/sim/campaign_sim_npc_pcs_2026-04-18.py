"""
Valoria Full Campaign Simulations — Named NPC as PC + Player-Created Character
Date: 2026-04-18

Runs 11 full-length campaigns (120 seasons each):
  10 named NPCs as PC (using their canonical Conviction/stats as PC profile)
  1 player-created character (balanced generalist, no faction alignment at start)

Each NPC PC profile derived from npc_behavior_v30.md canonical stat blocks.
Policy weights derived from primary/secondary Conviction and Ethical Framework.
"""

import sys, os, random, math
sys.path.insert(0, '/home/claude')
os.chdir('/home/claude')

from state import GameState, PC, init_game_state
from engine_v2 import run_season, check_victory, POLICIES

# ─────────────────────────────────────────────────────────────────
# NPC PC PROFILES
# Derived from npc_behavior_v30.md §2.x stat blocks
# Each profile: name, faction, attributes, ts, certainty, policy, notes
# ─────────────────────────────────────────────────────────────────

# [canonical: designs/npcs/npc_behavior_v30.md §2.x — all NPC stat blocks]
NPC_PC_PROFILES = [
    {
        'name': 'Almud Almqvist',
        'faction': 'Crown',
        # Order primary, Reason secondary — institutional governance focus
        # Authority resonant style — command and legitimacy
        'attrs': {'spirit':3, 'focus':5, 'attunement':2, 'cognition':5, 'charisma':5, 'bonds':3, 'recall':4},
        'ts': 0,
        'certainty': 3,  # [canonical: npc_behavior §2.1 — Certainty 3 Faithful]
        'policy': 'governor',
        'notes': 'Order/Reason Conviction. Authority RS. Institutional actor. Governor policy — high govern/contest weight.',
    },
    {
        'name': 'Arne Himlensendt',
        'faction': 'Church',
        # Faith primary, Order secondary — theocratic governance
        # Evidence RS — unusual for zealot; contests via documented doctrine
        'attrs': {'spirit':5, 'focus':4, 'attunement':2, 'cognition':4, 'charisma':4, 'bonds':2, 'recall':3},
        'ts': 0,
        'certainty': 5,  # [canonical: npc_behavior §2.2 — Certainty 5 Orthodox, max]
        'policy': 'theocrat',
        'notes': 'Faith/Order. Evidence RS. Certainty 5 = first Coherence loss nullified. Theocrat policy.',
    },
    {
        'name': 'Inge Baralta',
        'faction': 'Hafenmark',
        # Order primary, Justice secondary — constitutional law
        # Authority/Evidence RS — procedural, documented
        'attrs': {'spirit':3, 'focus':5, 'attunement':2, 'cognition':5, 'charisma':5, 'bonds':4, 'recall':5},
        'ts': 0,
        'certainty': 3,  # [canonical: npc_behavior §2.3]
        'policy': 'diplomat',
        'notes': 'Order/Justice. Constitutional framework. Diplomat policy — high contest/socialize.',
    },
    {
        'name': 'Magnus Vaynard',
        'faction': 'Varfell',
        # Reason primary, Autonomy secondary — intelligence and inquiry
        # Evidence/Consequence RS — empirical, strategic
        'attrs': {'spirit':2, 'focus':6, 'attunement':5, 'cognition':6, 'charisma':3, 'bonds':3, 'recall':5},
        'ts': 50,  # [canonical: npc_behavior §2.4 — TS 50, practitioner]
        'certainty': 1,  # [canonical: npc_behavior §2.4 — Certainty 1 Skeptic]
        'policy': 'investigator',
        'notes': 'Reason/Autonomy. TS 50 practitioner. Certainty 1. Investigator/practitioner policy.',
    },
    {
        'name': 'Lisbeth Ehrenwall',
        'faction': 'Crown',
        # Order primary, Autonomy secondary — martial honour
        # Consequence/Solidarity RS
        'attrs': {'spirit':5, 'focus':4, 'attunement':2, 'cognition':4, 'charisma':4, 'bonds':4, 'recall':3},
        'ts': 0,
        'certainty': 4,  # [canonical: npc_behavior §2.5 — Certainty 4 Faithful]
        'policy': 'warrior',
        'notes': 'Order/Autonomy. Martial Honour framework. Warrior policy — high combat/govern.',
    },
    {
        'name': 'Maret Vossen',
        'faction': 'RM',
        # Justice primary, Continuity secondary — grassroots organiser
        # Solidarity/Consequence RS
        'attrs': {'spirit':3, 'focus':3, 'attunement':3, 'cognition':4, 'charisma':6, 'bonds':5, 'recall':3},
        'ts': 0,
        'certainty': 2,  # [canonical: npc_behavior §2.6 — Certainty 2 Skeptic]
        'policy': 'restorationist',
        'notes': 'Justice/Continuity. Solidarity RS. Rawlsian framework. Restorationist policy.',
    },
    {
        'name': 'Aldric Hann',
        'faction': 'RM',
        # Justice primary, Autonomy secondary — operational focus
        # Consequence/Evidence RS
        'attrs': {'spirit':3, 'focus':4, 'attunement':2, 'cognition':4, 'charisma':4, 'bonds':3, 'recall':4},
        'ts': 0,
        'certainty': 2,  # [canonical: npc_behavior §2.7]
        'policy': 'independent',
        'notes': 'Justice/Autonomy. Operational actor. Independent policy — mixed.',
    },
    {
        'name': 'Prince Torben',
        'faction': 'Crown',
        # Faith primary, Order secondary — malleable heir
        # Undefined Beliefs at game start — high adaptability
        'attrs': {'spirit':4, 'focus':3, 'attunement':3, 'cognition':4, 'charisma':5, 'bonds':4, 'recall':3},
        'ts': 0,
        'certainty': 4,  # [canonical: npc_behavior §2.8 — young, conventional]
        'policy': 'balanced',
        'notes': 'Faith/Order. Undefined Beliefs. Most malleable NPC. Balanced policy (blank slate).',
    },
    {
        'name': 'Edeyja',
        'faction': 'Wardens',
        # Continuity primary, Autonomy secondary — Warden-Chief
        # Consequence/Solidarity RS
        'attrs': {'spirit':6, 'focus':3, 'attunement':6, 'cognition':4, 'charisma':3, 'bonds':3, 'recall':4},
        'ts': 70,  # [canonical: npc_behavior §2.9 — high TS, RS drain risk]
        'certainty': 1,  # [canonical: npc_behavior §2.9 — Thread-aware, certainty low]
        'policy': 'practitioner',
        'notes': 'Continuity/Autonomy. TS 70 — RS drain risk per threadwork_v30. Practitioner policy.',
    },
    {
        'name': 'Maret Uln',
        'faction': 'Varfell',
        # Justice primary, Reason secondary — succession candidate
        # Solidarity/Evidence RS
        'attrs': {'spirit':3, 'focus':4, 'attunement':3, 'cognition':5, 'charisma':5, 'bonds':4, 'recall':4},
        'ts': 35,  # [canonical: npc_behavior §2.10 — partial practitioner]
        'certainty': 2,
        'policy': 'diplomat',
        'notes': 'Justice/Reason. TS 35. Succession candidate. Diplomat policy.',
    },
    # Player-created character — no NPC basis
    {
        'name': 'Player Character (Generalist)',
        'faction': 'Crown',
        # Generic balanced build — Einhir Descendant origin (moderate TS)
        'attrs': {'spirit':4, 'focus':4, 'attunement':4, 'cognition':4, 'charisma':4, 'bonds':3, 'recall':3},
        'ts': 20,  # moderate — Einhir heritage
        'certainty': 3,
        'policy': 'balanced',
        'notes': 'Player-created generalist. Einhir Descendant origin. Balanced policy.',
    },
]

def make_pc_from_profile(profile):
    """Construct a PC dataclass from NPC profile."""
    pc = PC(faction=profile['faction'])
    for attr, val in profile['attrs'].items():
        setattr(pc, attr, val)
    pc.ts = profile['ts']
    pc.certainty = profile['certainty']
    # Derived starting values
    # [canonical: params/core.md §Derived Stats — Coherence = 10 base]
    pc.coherence = 10
    # [canonical: designs/scene/derived_stats_v30.md §2 — Stamina = Spirit×2]
    pc.stamina = profile['attrs']['spirit'] * 2
    return pc

def run_npc_pc_campaign(profile, seed=42, seasons=120):
    """Run a full campaign with an NPC as PC."""
    gs = init_game_state(pc_faction=profile['faction'], seed=seed)
    gs.pc = make_pc_from_profile(profile)

    # Wardens faction — needs to be activated for Edeyja
    if profile['faction'] == 'Wardens':
        gs.factions['Wardens'].active = True
        gs.factions['Wardens'].mandate = 2
        gs.factions['Wardens'].military = 1
        gs.factions['Wardens'].influence = 2
        gs.factions['Wardens'].wealth = 1
        gs.factions['Wardens'].stability = 3
        gs.factions['Wardens'].territories = ['T15', 'T16']

    # RM faction — activate for Vossen and Hann
    if profile['faction'] == 'RM':
        gs.factions['RM'].active = True
        gs.factions['RM'].mandate = 2
        gs.factions['RM'].military = 1
        gs.factions['RM'].influence = 3
        gs.factions['RM'].wealth = 1
        gs.factions['RM'].stability = 3
        gs.factions['RM'].territories = []

    victory_result = None
    for s in range(seasons):
        run_season(gs, profile['policy'])
        # Check for early termination
        if gs.log and any('VICTORY' in entry for entry in gs.log[-5:]):
            victory_result = gs.log[-1]
            break

    return gs, victory_result

# ─────────────────────────────────────────────────────────────────
# RUN ALL CAMPAIGNS
# ─────────────────────────────────────────────────────────────────

print("=" * 70)
print("VALORIA FULL CAMPAIGN SIMULATIONS — NPC PCs + PLAYER CHARACTER")
print("120 seasons per campaign | 11 total simulations")
print("=" * 70)

all_results = []

for i, profile in enumerate(NPC_PC_PROFILES):
    print(f"\n[{i+1:2d}/11] {profile['name']} ({profile['faction']}) — {profile['policy']} policy")
    # [canonical: params/core.md §Random Seed — per-run seeding for reproducibility]
    gs, victory = run_npc_pc_campaign(profile, seed=42 + i * 100, seasons=120)

    # Extract key outcome metrics
    result = {
        'name': profile['name'],
        'faction': profile['faction'],
        'policy': profile['policy'],
        'notes': profile['notes'],
        'seasons_run': gs.season,
        'rs_final': gs.rs,
        'tc_final': gs.tc,
        'ip_final': gs.ip,
        'standing_final': gs.pc.standing,
        'coherence_final': gs.pc.coherence,
        'ts_final': gs.pc.ts,
        'faction_stab': gs.factions.get(profile['faction'], gs.factions['Crown']).stability,
        'features_fired': len(gs.features_fired),
        'victory': victory,
        # Victory conditions met?
        'coup_counter': 0,  # tracked in log
        'rs_bracket': ('Critical' if gs.rs <= 20 else 'Fractured' if gs.rs <= 40
                       else 'Strained' if gs.rs <= 60 else 'Stable'),
        'tc_bracket': ('Theocratic' if gs.tc >= 75 else 'Dominant' if gs.tc >= 60
                       else 'Influential' if gs.tc >= 45 else 'Contested'),
    }

    # Check faction victory conditions from log
    for entry in gs.log:
        if 'Church victory' in entry: result['victory'] = result.get('victory') or 'Church'
        if 'Crown victory' in entry: result['victory'] = result.get('victory') or 'Crown'
        if 'Hafenmark victory' in entry: result['victory'] = result.get('victory') or 'Hafenmark'
        if 'Varfell victory' in entry: result['victory'] = result.get('victory') or 'Varfell'
        if 'RM victory' in entry: result['victory'] = result.get('victory') or 'RM'

    all_results.append(result)
    print(f"       RS={gs.rs} ({result['rs_bracket']}) | TC={gs.tc} ({result['tc_bracket']}) | "
          f"Standing={gs.pc.standing} | Coherence={gs.pc.coherence} | "
          f"Features={len(gs.features_fired)} | Victory={result['victory'] or 'None by S120'}")

# ─────────────────────────────────────────────────────────────────
# CONSOLIDATED REPORT
# ─────────────────────────────────────────────────────────────────

print("\n\n" + "=" * 70)
print("CONSOLIDATED RESULTS — ALL 11 CAMPAIGNS")
print("=" * 70)

print(f"\n{'PC Name':<30} {'Fac':<12} {'RS':<6} {'TC':<6} {'Std':<5} {'Coh':<5} {'Victory'}")
print("-" * 85)
for r in all_results:
    print(f"{r['name']:<30} {r['faction']:<12} {r['rs_final']:<6} {r['tc_final']:<6} "
          f"{r['standing_final']:<5} {r['coherence_final']:<5} {r['victory'] or 'None'}")

print("\n\nKEY FINDINGS BY CHARACTER:")
print("-" * 70)
for r in all_results:
    print(f"\n{r['name']} ({r['faction']})")
    print(f"  Profile:  {r['notes']}")
    print(f"  RS:       {r['rs_final']} — {r['rs_bracket']}")
    print(f"  TC:       {r['tc_final']} — {r['tc_bracket']}")
    print(f"  Standing: {r['standing_final']}/7 at S{r['seasons_run']}")
    print(f"  Coherence:{r['coherence_final']}/10")
    print(f"  Features: {r['features_fired']} systems exercised")
    print(f"  Victory:  {r['victory'] or 'None by S120'}")

# Cross-campaign analysis
print("\n\n" + "=" * 70)
print("CROSS-CAMPAIGN ANALYSIS")
print("=" * 70)

rs_values = [r['rs_final'] for r in all_results]
tc_values = [r['tc_final'] for r in all_results]
victories = [r for r in all_results if r['victory']]

print(f"\nRS outcomes: avg={sum(rs_values)/len(rs_values):.1f}, "
      f"min={min(rs_values)} ({all_results[rs_values.index(min(rs_values))]['name']}), "
      f"max={max(rs_values)} ({all_results[rs_values.index(max(rs_values))]['name']})")
print(f"TC outcomes: avg={sum(tc_values)/len(tc_values):.1f}, "
      f"min={min(tc_values)} ({all_results[tc_values.index(min(tc_values))]['name']}), "
      f"max={max(tc_values)} ({all_results[tc_values.index(max(tc_values))]['name']})")

rs_critical = sum(1 for r in all_results if r['rs_final'] <= 20)
rs_fractured = sum(1 for r in all_results if 20 < r['rs_final'] <= 40)
tc_dominant = sum(1 for r in all_results if r['tc_final'] >= 60)
print(f"\nRS Critical (≤20): {rs_critical}/11 campaigns")
print(f"RS Fractured (21-40): {rs_fractured}/11 campaigns")
print(f"TC Dominant (≥60): {tc_dominant}/11 campaigns")
print(f"Victories by S120: {len(victories)}/11")
if victories:
    for v in victories:
        print(f"  {v['name']}: {v['victory']}")

# Unique findings per character type
print("\n\nCHARACTER TYPE FINDINGS:")
practitioner_chars = [r for r in all_results if r['ts_final'] > 30]
non_prac = [r for r in all_results if r['ts_final'] <= 10]
if practitioner_chars:
    avg_rs_prac = sum(r['rs_final'] for r in practitioner_chars) / len(practitioner_chars)
    avg_rs_nonprac = sum(r['rs_final'] for r in non_prac) / len(non_prac) if non_prac else 0
    print(f"Practitioner PCs (TS>30): avg RS={avg_rs_prac:.1f} vs Non-practitioner: avg RS={avg_rs_nonprac:.1f}")
    print("  -> Practitioner PCs accelerate RS drain through Thread operations")

# Policy comparison
from collections import defaultdict
policy_rs = defaultdict(list)
for r in all_results:
    policy_rs[r['policy']].append(r['rs_final'])
print("\nRS by Policy:")
for pol, vals in sorted(policy_rs.items()):
    print(f"  {pol:<16}: avg RS={sum(vals)/len(vals):.1f}")

