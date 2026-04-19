"""
Valoria — Provisional Mechanics Arc Test — Batch 2 (fixed)
Bugs fixed vs first run:
  - RM Inf only increments on genuine ctrl change (not RM→RM)
  - Same-season Consolidation race: seceeded_this_season set blocks Consolidation
  - Secession cooldown applies correctly: blocks Secession on that settlement for N seasons
"""

import random
from copy import deepcopy

SETTLEMENTS = {
    "S001": dict(name="Valorsplatz Palace",    prov="T1",  stype="Seat",     ctrl="Crown",      P=4, D=3, O=4, seat=True),
    "S002": dict(name="Valorsplatz Riverside", prov="T1",  stype="Port",     ctrl="Crown",      P=4, D=1, O=3, seat=False),
    "S003": dict(name="Valorsplatz Cathedral", prov="T1",  stype="Cathedral",ctrl="Church",     P=2, D=1, O=4, seat=False),
    "S004": dict(name="Kronmark",              prov="T2",  stype="Town",     ctrl="Crown",      P=3, D=1, O=3, seat=True),
    "S005": dict(name="Kronmark Watchtower",   prov="T2",  stype="Fortress", ctrl="Crown",      P=1, D=3, O=3, seat=False),
    "S006": dict(name="Lowenskyst Fortress",   prov="T3",  stype="Fortress", ctrl="Crown",      P=1, D=4, O=4, seat=True),
    "S007": dict(name="Lowenskyst Garrison",   prov="T3",  stype="Town",     ctrl="Crown",      P=2, D=1, O=3, seat=False),
    "S008": dict(name="Feldmark",              prov="T5",  stype="Town",     ctrl="Crown",      P=4, D=0, O=3, seat=True),
    "S009": dict(name="Feldmark Storehouse",   prov="T5",  stype="Mine",     ctrl="Crown",      P=3, D=0, O=2, seat=False),
    "S010": dict(name="Stillhelm",             prov="T6",  stype="Town",     ctrl="Crown",      P=2, D=0, O=2, seat=True),
    "S011": dict(name="Stillhelm Watch",       prov="T6",  stype="Outpost",  ctrl="Crown",      P=0, D=2, O=2, seat=False),
    "S012": dict(name="Ehrenfeld Citadel",     prov="T14", stype="Fortress", ctrl="Crown",      P=1, D=4, O=4, seat=True),
    "S013": dict(name="Ehrenfeld Market",      prov="T14", stype="City",     ctrl="Crown",      P=3, D=1, O=3, seat=False),
    "S014": dict(name="Ehrenfeld Barracks",    prov="T14", stype="Fortress", ctrl="Löwenritter",P=1, D=3, O=4, seat=False),
    "S015": dict(name="Gransol Parliament",    prov="T8",  stype="Seat",     ctrl="Hafenmark",  P=4, D=2, O=4, seat=True),
    "S016": dict(name="Gransol Harbor",        prov="T8",  stype="Port",     ctrl="Hafenmark",  P=4, D=1, O=3, seat=False),
    "S017": dict(name="Gransol Market Quarter",prov="T8",  stype="City",     ctrl="Guilds",     P=5, D=0, O=3, seat=False),
    "S018": dict(name="Rendstad",              prov="T7",  stype="Town",     ctrl="Hafenmark",  P=2, D=0, O=2, seat=True),
    "S019": dict(name="Spartfell Fortress",    prov="T10", stype="Fortress", ctrl="Hafenmark",  P=1, D=3, O=3, seat=True),
    "S020": dict(name="Spartfell Village",     prov="T10", stype="Town",     ctrl="Hafenmark",  P=2, D=1, O=2, seat=False),
    "S021": dict(name="Halvarshelm Mines",     prov="T17", stype="Mine",     ctrl="Hafenmark",  P=3, D=0, O=2, seat=True),
    "S022": dict(name="Halvarshelm Town",      prov="T17", stype="Town",     ctrl="Hafenmark",  P=2, D=0, O=3, seat=False),
    "S023": dict(name="Himmelenger Cathedral", prov="T9",  stype="Cathedral",ctrl="Church",     P=3, D=2, O=5, seat=True),
    "S024": dict(name="Himmelenger City",      prov="T9",  stype="City",     ctrl="Church",     P=3, D=1, O=4, seat=False),
    "S025": dict(name="Himmelenger Seminary",  prov="T9",  stype="Cathedral",ctrl="Church",     P=1, D=1, O=5, seat=False),
    "S026": dict(name="Sigurdshelm Keep",      prov="T12", stype="Seat",     ctrl="Varfell",    P=3, D=2, O=3, seat=True),
    "S027": dict(name="Sigurdshelm Cove",      prov="T12", stype="Port",     ctrl="Varfell",    P=2, D=1, O=2, seat=False),
    "S028": dict(name="Grauwald",              prov="T4",  stype="Town",     ctrl="Varfell",    P=2, D=0, O=2, seat=True),
    "S029": dict(name="Grauwald Lodge",        prov="T4",  stype="Outpost",  ctrl="RM",         P=1, D=0, O=2, seat=False),
    "S030": dict(name="Halvardshelm",          prov="T11", stype="Town",     ctrl="Varfell",    P=2, D=0, O=2, seat=True),
    "S031": dict(name="Oastad",                prov="T13", stype="Town",     ctrl="Varfell",    P=2, D=0, O=2, seat=True),
    "S032": dict(name="Oastad Shrine",         prov="T13", stype="Outpost",  ctrl="RM",         P=0, D=0, O=1, seat=False),
    "S033": dict(name="Askeheim Ruins",        prov="T15", stype="Outpost",  ctrl="Wardens",    P=0, D=1, O=1, seat=False),
    "S034": dict(name="Askeheim Gate",         prov="T15", stype="Outpost",  ctrl="None",       P=0, D=0, O=0, seat=False),
    "S035": dict(name="Schoenland City",       prov="T16", stype="City",     ctrl="Schoenland", P=4, D=2, O=4, seat=True),
    "S036": dict(name="Schoenland Harbor",     prov="T16", stype="Port",     ctrl="Schoenland", P=3, D=3, O=4, seat=False),
}

PROVINCE_BASE_PV = {
    "T1": 5, "T2": 3, "T3": 3, "T4": 2, "T5": 3, "T6": 2,
    "T7": 1, "T8": 4, "T9": 4, "T10": 2, "T11": 1, "T12": 3,
    "T13": 2, "T14": 4, "T15": 1, "T16": 2, "T17": 2,
}

# ─── DICE ─────────────────────────────────────────────────────────────────────

def roll(pool, ob, rng):
    pool = max(1, pool)
    hits = sum(1 for _ in range(pool) if rng.randint(1, 10) >= 7)
    m = hits - ob
    return "Overwhelming" if m>=2 else "Success" if m>=0 else "Partial" if m>=-1 else "Failure"

def net_hits(pool, ob, rng):
    pool = max(1, pool)
    return sum(1 for _ in range(pool) if rng.randint(1, 10) >= 7) - ob

# ─── PROVINCE HELPERS ─────────────────────────────────────────────────────────

def seat_ctrl(s, prov):
    return next((d['ctrl'] for d in s.values() if d['prov']==prov and d['seat']), None)

def alien_non_seat(s, prov):
    sc = seat_ctrl(s, prov)
    return [sid for sid, d in s.items()
            if d['prov']==prov and not d['seat'] and d['ctrl'] != sc]

def is_fractional(s, prov):
    return bool(alien_non_seat(s, prov))

def compute_pv_shares(s, prov):
    ps = {sid: d for sid, d in s.items() if d['prov']==prov}
    total_p = sum(d['P'] for d in ps.values()) or 1
    base = PROVINCE_BASE_PV.get(prov, 1)
    shares = {}
    for d in ps.values():
        shares[d['ctrl']] = round(shares.get(d['ctrl'],0) + (d['P']/total_p)*base, 2)
    return shares

# ─── ARC LOG ──────────────────────────────────────────────────────────────────

class ArcLog:
    def __init__(self): self.events = []
    def log(self, s, actor, event, detail=""):
        self.events.append((s, actor, event, detail))
    def print_arc(self, max_events=999):
        for i, (s, a, e, d) in enumerate(self.events[:max_events]):
            print(f"  S{s:02d} [{a}] {e}" + (f" — {d}" if d else ""))
        if len(self.events) > max_events:
            print(f"  ... ({len(self.events)-max_events} more)")

# ─── SIMULATION ───────────────────────────────────────────────────────────────

def run(name, setup_fn, seasons=24, seed=42,
        secession_cooldown=0,
        rm_order_threshold=1,
        splinter_mandate_floor=1,
        crown_suppression=False):

    rng = random.Random(seed)
    s = deepcopy(SETTLEMENTS)
    fi = {"Crown":5,"Hafenmark":5,"Varfell":4,"Church":4,"RM":2,
          "Eastern Varfell":2,"Southern Hafenmark":2}
    fm = {"Crown":4,"Hafenmark":4,"Varfell":4,"Church":3}
    leaders = {"Varfell":"Vaynard","Crown":"Almud","Hafenmark":"Baralta","Church":"Confessor"}
    rm_presence = {"_cooldown":{}}
    splinters = {}
    secession_blocks = {}  # sid → seasons remaining
    log = ArcLog()
    succession_triggers = {}

    setup_fn(s, fi, fm, leaders, log, succession_triggers)

    for season in range(1, seasons+1):
        seceeded_this_season = set()  # FIX: block Consolidation on same-season seceeded settlements

        # ── CROWN SUPPRESSION ──────────────────────────────────────────────
        crown_suppression_targets = set()
        if crown_suppression and fi.get("Crown",0) >= 1:
            candidates = [(p, compute_pv_shares(s,p)) for p in PROVINCE_BASE_PV
                          if is_fractional(s,p)]
            if candidates:
                target_prov = max(candidates, key=lambda x: PROVINCE_BASE_PV[x[0]])[0]
                crown_suppression_targets.add(target_prov)
                fi["Crown"] -= 1
                log.log(season,"Crown","Suppression",
                        f"{target_prov} Ob+1, Crown Inf→{fi['Crown']}")

        # ── FRAGMENTATION ─────────────────────────────────────────────────
        checked = set()
        for sid, sd in s.items():
            prov = sd['prov']
            if prov in checked or not is_fractional(s, prov):
                continue
            checked.add(prov)
            sc = seat_ctrl(s, prov)
            aliens = alien_non_seat(s, prov)
            ob = 2 + len(aliens) + (1 if prov in crown_suppression_targets else 0)
            pool = fi.get(sc, 2)
            result = roll(pool, ob, rng)

            if result == "Failure":
                # Only candidates not in secession_blocks
                candidates = [a for a in aliens if secession_blocks.get(a,0) == 0]
                if candidates:
                    target = rng.choice(candidates)
                    old_ctrl = s[target]['ctrl']
                    s[target]['ctrl'] = "RM"
                    seceeded_this_season.add(target)
                    # FIX: only +Inf if genuinely changing to RM
                    if old_ctrl != "RM":
                        rm_presence.setdefault('settlements',[]).append(target)
                        fi['RM'] = fi.get('RM',0) + 1
                    log.log(season,"Fragmentation","Secession",
                            f"{s[target]['name']} → RM (was {old_ctrl})")
            elif result == "Partial":
                if aliens:
                    target = rng.choice(aliens)
                    s[target]['O'] = max(0, s[target]['O']-1)
                    log.log(season,"Fragmentation","Order drop",
                            f"{s[target]['name']} O→{s[target]['O']}")

        # ── CONSOLIDATION ─────────────────────────────────────────────────
        for prov in PROVINCE_BASE_PV:
            sc = seat_ctrl(s, prov)
            if not sc:
                continue
            shares = compute_pv_shares(s, prov)
            total = sum(shares.values()) or 1
            if (shares.get(sc,0)/total) < 0.75:
                continue
            aliens = alien_non_seat(s, prov)
            for asid in aliens:
                if asid in seceeded_this_season:  # FIX: skip just-seceeded settlements
                    continue
                alien_ctrl = s[asid]['ctrl']
                resist = rng.randint(1,6) <= fm.get(alien_ctrl,1)
                if not resist:
                    s[asid]['ctrl'] = sc
                    s[asid]['O'] = max(0, s[asid]['O']-2)
                    if secession_cooldown > 0:
                        secession_blocks[asid] = secession_cooldown
                    log.log(season,"Consolidation","Submit",
                            f"{s[asid]['name']} → {sc}")
                else:
                    log.log(season,"Consolidation","Resist",
                            f"{s[asid]['name']} holds vs {sc}")

        # ── TICK COOLDOWNS ────────────────────────────────────────────────
        for sid in list(secession_blocks):
            if secession_blocks[sid] > 0:
                secession_blocks[sid] -= 1

        # ── RM EMERGENCE ──────────────────────────────────────────────────
        if season % 2 == 0:
            prov_cd = rm_presence.get('_cooldown',{})
            for sid, sd in s.items():
                if sd['ctrl'] not in ('Varfell','Eastern Varfell','Southern Hafenmark'):
                    continue
                threshold_met = (sd['O'] == 0) if rm_order_threshold == 0 else (sd['O'] <= rm_order_threshold)
                if not threshold_met:
                    continue
                prov2 = sd['prov']
                if prov_cd.get(prov2,0) > 0:
                    continue
                old_ctrl = sd['ctrl']
                s[sid]['ctrl'] = 'RM'
                rm_presence.setdefault('settlements',[]).append(sid)
                fi['RM'] = fi.get('RM',0)+1
                prov_cd[prov2] = 4
                log.log(season,"RM","Settlement Emergence",
                        f"{sd['name']} (was {old_ctrl}) Inf→{fi['RM']}")
            for p in list(prov_cd):
                if prov_cd[p] > 0: prov_cd[p] -= 1
            rm_presence['_cooldown'] = prov_cd

        # ── SUCCESSION ────────────────────────────────────────────────────
        for faction, trigger_s in succession_triggers.items():
            if season != trigger_s:
                continue
            if leaders.get(faction) in (None,"Regency"):
                continue
            log.log(season,faction,"Leader eliminated",f"{leaders[faction]} falls")
            leaders[faction] = None

            if faction == "Varfell":
                contenders = [
                    ("Maret Uln",      7, 2),
                    ("Tribune Captain",9, 4),
                    ("RM-candidate",   max(3,fi.get('RM',2)+2), 0),
                ]
            elif faction == "Hafenmark":
                contenders = [("Baralta Heir",6,3),("Guild-backed",5,0)]
            else:
                contenders = [("Heir A",6,2),("Heir B",5,1)]

            results = {nm: net_hits(pool,3,rng) for nm,pool,_ in contenders}
            ranked = sorted(results.items(),key=lambda x:-x[1])
            w_name,w_net = ranked[0]
            r_name,r_net = (ranked[1][0],ranked[1][1]) if len(ranked)>1 else (None,-99)
            margin = w_net - r_net

            if w_net <= 0:
                leaders[faction] = "Regency"
                log.log(season,faction,"Succession: Regency","no winner")
            elif margin >= 2:
                leaders[faction] = w_name
                fm[faction] = max(1,fm.get(faction,3)-1)
                log.log(season,faction,f"Succession: Clear → {w_name}",f"margin {margin}")
            else:
                leaders[faction] = w_name
                splinter_name = f"Eastern {faction}"
                faction_provs = list(set(d['prov'] for d in s.values() if d['ctrl']==faction))
                cap_prov = next((d['prov'] for d in s.values()
                                 if d['ctrl']==faction and d['seat'] and d['prov'] in faction_provs),None)
                splinter_provs = [p for p in faction_provs if p != cap_prov]
                for sp in splinter_provs:
                    for sid2 in s:
                        if s[sid2]['prov']==sp and s[sid2]['ctrl']==faction:
                            s[sid2]['ctrl'] = splinter_name
                old_m = fm.get(faction,3)
                splinter_m = max(splinter_mandate_floor, int(old_m*0.4))
                splinters[splinter_name] = {'leader':r_name,'mandate':splinter_m,'provs':splinter_provs}
                fm[faction]  = int(old_m*0.6)
                fm[splinter_name] = splinter_m
                fi[splinter_name] = fi.get(faction,3)
                log.log(season,faction,f"Succession: SPLIT → {w_name} vs {r_name}",
                        f"margin {margin} — {splinter_name} mandate={splinter_m} provs={splinter_provs}")
                rm_cand_net = results.get("RM-candidate",-99)
                if rm_cand_net > 0:
                    fi['RM'] = fi.get('RM',0)+1
                    log.log(season,"RM","Political momentum",f"Inf→{fi['RM']}")

    # Final state
    pv = {}
    for prov in PROVINCE_BASE_PV:
        for ctrl2,share in compute_pv_shares(s,prov).items():
            pv[ctrl2] = round(pv.get(ctrl2,0)+share,2)

    rm_count = sum(1 for d in s.values() if d['ctrl']=='RM')
    frac_end = [p for p in PROVINCE_BASE_PV if is_fractional(s,p)]

    return {
        "log":log, "pv":dict(sorted(pv.items(),key=lambda x:-x[1])),
        "rm_settlements":rm_count, "rm_inf":fi.get('RM',0),
        "splinters":splinters, "fractional_at_end":frac_end,
        "event_count":len(log.events),
        "secession_blocks_final":dict(secession_blocks),
    }

# ─── SETUPS ───────────────────────────────────────────────────────────────────

def setup_fracture(s, fi, fm, leaders, log, triggers):
    s['S017']['ctrl'] = 'Varfell'
    s['S030']['O'] = 1
    s['S031']['O'] = 1
    log.log(0,"Varfell","Captures S017","T8 fractional")
    triggers["Varfell"] = 10

def setup_mutual(s, fi, fm, leaders, log, triggers):
    s['S017']['ctrl'] = 'Varfell'   # T8 fractional (Varfell in Hafenmark province)
    s['S030']['ctrl'] = 'Hafenmark' # T11 fractional (Hafenmark in Varfell province)
    log.log(0,"Varfell",   "Captures S017","T8 fractional")
    log.log(0,"Hafenmark", "Captures S030","T11 fractional")

SEEDS = [42, 77, 99, 137, 201]

def sline(seed, r):
    sp = list(r['splinters'].keys())
    frac = r['fractional_at_end']
    top5 = dict(list(r['pv'].items())[:5])
    return (f"  seed={seed:3d} | PV: {top5} "
            f"| RM: {r['rm_settlements']}s/{r['rm_inf']}inf "
            f"| frac@end: {frac} | splinters: {sp or '—'}")

def hdr(t):  print(f"\n{'═'*68}\n  {t}\n{'═'*68}")
def sub(t):  print(f"\n{'─'*55}\n  {t}\n{'─'*55}")

if __name__ == "__main__":
    print("="*68)
    print("VALORIA — PROVISIONAL MECHANICS BATCH 2 (bugs fixed)")
    print("5 variants × 5 seeds × 24 seasons")
    print("="*68)

    # ── B2-1: SECESSION COOLDOWN ──────────────────────────────────────────
    hdr("B2-1: SECESSION COOLDOWN — 0 (original) vs 2-season fix")
    sub("No cooldown")
    no_cd = {s: run("B2-1-no",  setup_fracture, seed=s, secession_cooldown=0) for s in SEEDS}
    for s in SEEDS: print(sline(s, no_cd[s]))

    sub("2-season cooldown")
    cd2 = {s: run("B2-1-cd2", setup_fracture, seed=s, secession_cooldown=2) for s in SEEDS}
    for s in SEEDS: print(sline(s, cd2[s]))

    avg_ev_no = sum(no_cd[s]['event_count'] for s in SEEDS)/len(SEEDS)
    avg_ev_cd = sum(cd2[s]['event_count'] for s in SEEDS)/len(SEEDS)
    print(f"\n  Avg events — no cooldown: {avg_ev_no:.1f}  |  2s cooldown: {avg_ev_cd:.1f}")
    print(f"  Event reduction: {(1-avg_ev_cd/max(avg_ev_no,1))*100:.0f}%")
    # Show one run's log to verify oscillation is gone
    print("\n  No-cooldown event log (seed 42, first 30):")
    no_cd[42]['log'].print_arc(30)
    print("\n  2s-cooldown event log (seed 42, first 30):")
    cd2[42]['log'].print_arc(30)

    # ── B2-2: RM THRESHOLD ────────────────────────────────────────────────
    hdr("B2-2: RM EMERGENCE THRESHOLD — Order<=1 vs Order=0")
    sub("Order<=1 (original)")
    rm1 = {s: run("B2-2-l", setup_fracture, seed=s, rm_order_threshold=1) for s in SEEDS}
    for s in SEEDS: print(sline(s, rm1[s]))

    sub("Order=0 (strict)")
    rm0 = {s: run("B2-2-s", setup_fracture, seed=s, rm_order_threshold=0) for s in SEEDS}
    for s in SEEDS: print(sline(s, rm0[s]))

    print(f"\n  Avg RM settlements — loose: {sum(rm1[s]['rm_settlements'] for s in SEEDS)/len(SEEDS):.1f}"
          f"  |  strict: {sum(rm0[s]['rm_settlements'] for s in SEEDS)/len(SEEDS):.1f}")
    print(f"  Avg RM Inf — loose: {sum(rm1[s]['rm_inf'] for s in SEEDS)/len(SEEDS):.1f}"
          f"  |  strict: {sum(rm0[s]['rm_inf'] for s in SEEDS)/len(SEEDS):.1f}")

    # ── B2-3: SPLINTER MANDATE ────────────────────────────────────────────
    hdr("B2-3: SPLINTER MANDATE FLOOR — 1 vs 2")
    sub("Mandate floor 1")
    sp1 = {s: run("B2-3-m1", setup_fracture, seed=s, splinter_mandate_floor=1) for s in SEEDS}
    for s in SEEDS:
        print(sline(s, sp1[s]))
        for n,d in sp1[s]['splinters'].items():
            print(f"    {n}: mandate={d['mandate']} provs={d['provs']}")

    sub("Mandate floor 2")
    sp2 = {s: run("B2-3-m2", setup_fracture, seed=s, splinter_mandate_floor=2) for s in SEEDS}
    for s in SEEDS:
        print(sline(s, sp2[s]))
        for n,d in sp2[s]['splinters'].items():
            print(f"    {n}: mandate={d['mandate']} provs={d['provs']}")

    m1_ev_pv = [sp1[s]['pv'].get('Eastern Varfell',0) for s in SEEDS]
    m2_ev_pv = [sp2[s]['pv'].get('Eastern Varfell',0) for s in SEEDS]
    print(f"\n  Eastern Varfell PV at end — floor 1: {m1_ev_pv}  |  floor 2: {m2_ev_pv}")

    # ── B2-4: CROWN SUPPRESSION ───────────────────────────────────────────
    hdr("B2-4: CROWN SUPPRESSION — off vs on")
    sub("Off")
    cs0 = {s: run("B2-4-off", setup_fracture, seed=s, crown_suppression=False) for s in SEEDS}
    for s in SEEDS: print(sline(s, cs0[s]))

    sub("On")
    cs1 = {s: run("B2-4-on",  setup_fracture, seed=s, crown_suppression=True)  for s in SEEDS}
    for s in SEEDS: print(sline(s, cs1[s]))

    print(f"\n  Avg RM settlements — off: {sum(cs0[s]['rm_settlements'] for s in SEEDS)/len(SEEDS):.1f}"
          f"  |  on: {sum(cs1[s]['rm_settlements'] for s in SEEDS)/len(SEEDS):.1f}")
    print(f"  Avg frac@end — off: {sum(len(cs0[s]['fractional_at_end']) for s in SEEDS)/len(SEEDS):.1f}"
          f"  |  on: {sum(len(cs1[s]['fractional_at_end']) for s in SEEDS)/len(SEEDS):.1f}")
    print("\n  Crown suppression trace (seed 42, first 15 events):")
    for s2,actor,event,detail in cs1[42]['log'].events[:15]:
        print(f"    S{s2:02d} [{actor}] {event}" + (f" — {detail}" if detail else ""))

    # ── B2-5: MUTUAL FRACTIONALIZATION ───────────────────────────────────
    hdr("B2-5: MUTUAL FRACTIONALIZATION — T8 + T11 simultaneously")
    mut = {s: run("B2-5", setup_mutual, seed=s, secession_cooldown=2) for s in SEEDS}
    for s in SEEDS: print(sline(s, mut[s]))
    print("\n  Event log (seed 42):")
    mut[42]['log'].print_arc()

    # ── CROSS-VARIANT SUMMARY ─────────────────────────────────────────────
    hdr("CROSS-VARIANT SUMMARY (seed 42)")
    print(f"  {'Variant':<32} {'RM s':<6} {'RM inf':<8} {'Events':<8} {'Frac@end'}")
    print(f"  {'─'*70}")
    rows = [
        ("B2-1 no cooldown",      no_cd[42]),
        ("B2-1 2s cooldown",      cd2[42]),
        ("B2-2 Order<=1",         rm1[42]),
        ("B2-2 Order=0",          rm0[42]),
        ("B2-3 Mandate floor 1",  sp1[42]),
        ("B2-3 Mandate floor 2",  sp2[42]),
        ("B2-4 suppression off",  cs0[42]),
        ("B2-4 suppression on",   cs1[42]),
        ("B2-5 mutual frac",      mut[42]),
    ]
    for label,r in rows:
        frac = r['fractional_at_end'] or ['—']
        print(f"  {label:<32} {r['rm_settlements']:<6} {r['rm_inf']:<8} {r['event_count']:<8} {frac}")

