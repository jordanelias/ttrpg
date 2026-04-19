"""
Valoria — Arc Test Batch 4
Systems under test:
  B4-1: PP-431-COR fix — Parliamentary Challenge replaces structural suppression (not supplements)
  B4-2: PI track dynamics — Parliamentary Manoeuvre, Crown erosion, PI≤2 state (Crown by decree)
  B4-3: RDT/TD track cascade — Reformed Doctrine as Seizure defence; can Hafenmark reach TD4-5 first?
  B4-4: Accord revolt cascade — Strain escalation from ungarrisoned territories
  B4-5: Löwenritter Coup — timing, board state aftermath, post-coup PI collapse

Canonical sources:
  params/bg/parliament.md — PI track, Parliamentary Manoeuvre, Challenge/structural interaction
  params/bg/tracks.md — RDT/TD tracks, AER
  params/bg/core.md — starting stats, Accord, Coup Counter, Strain thresholds, corrected PT values
  params/bg/phases.md — Phase 5 Accord checks, Strain update
  params/bg/ci_seizure.md — CI seasonal formula, Seizure
"""

import random

# ─── CANONICAL CONSTANTS ─────────────────────────────────────────────────────

STARTING_STATS = {
    "Crown":     dict(M=5, I=5, W=4, Mil=4, Stab=4),
    "Church":    dict(M=5, I=6, W=5, Mil=4, Stab=5),
    "Hafenmark": dict(M=4, I=4, W=5, Mil=3, Stab=4),
    "Varfell":   dict(M=4, I=4, W=4, Mil=4, Stab=4),
}

# Corrected canonical PT values (params/bg/core.md)
CANONICAL_PT = {
    "T1":3,"T2":3,"T3":3,"T4":2,"T5":3,"T6":1,"T7":3,"T8":3,
    "T9":5,"T10":3,"T11":2,"T12":2,"T13":1,"T14":3,"T15":0,"T17":3,
}

# Starting Accord: capitals=3, other home=2
STARTING_ACCORD = {
    "T1":3,  # Crown capital
    "T2":2,"T3":2,"T5":2,"T6":2,"T14":2,  # Crown home
    "T8":3,  # Hafenmark capital
    "T7":2,"T10":2,"T17":2,  # Hafenmark home
    "T9":3,  # Church capital
    "T12":3, # Varfell capital
    "T4":2,"T11":2,"T13":2,  # Varfell home
}

# Territory PV (from params/bg/victory.md)
TERRITORY_PV = {
    "T1":5,"T8":4,"T9":5,"T12":4,"T3":3,"T10":1,"T14":3,
    "T2":1,"T4":1,"T5":1,"T6":1,"T7":1,"T11":1,"T13":1,"T17":1,
}

# Strain threshold effects
STRAIN_EFFECTS = {
    (0,2): "Peace",
    (3,4): "Tension — Mandate check Ob1 each faction",
    (5,6): "Fracture — Accord−1 in one territory",
    (7,8): "Crisis — Accord−1 ALL non-capital territories; Mandate check Ob2",
    (9,10):"Collapse — non-capital Accord cap 2; Mandate check Ob3; RS−1/season extra",
}

def strain_band(strain):
    for (lo,hi), name in STRAIN_EFFECTS.items():
        if lo <= strain <= hi:
            return name
    return "Unknown"

# ─── DICE ─────────────────────────────────────────────────────────────────────

def roll(pool, ob, rng):
    pool = max(1, pool)
    net = sum((-1 if d==1 else 2 if d==10 else 1 if d>=7 else 0)
              for d in (rng.randint(1,10) for _ in range(pool)))
    net -= ob
    return ("Overwhelming" if net>=2 else "Success" if net>=0
            else "Partial" if net>=-1 else "Failure"), net

# ─── ARC LOG ──────────────────────────────────────────────────────────────────

class Log:
    def __init__(self): self.events = []
    def log(self, s, actor, event, detail=""):
        self.events.append((s, actor, event, detail))
    def print_arc(self, n=999):
        for s,a,e,d in self.events[:n]:
            print(f"  S{s:02d} [{a}] {e}" + (f" — {d}" if d else ""))
        if len(self.events) > n:
            print(f"  ... ({len(self.events)-n} more)")

# ─── CI HELPERS (corrected from B3) ──────────────────────────────────────────

SW = {"T9":5,"T1":3,"T14":2,"T8":2,"T12":2,"T4":2,"T2":1,"T5":1,"T6":1,"T13":1}

def ci_delta(ci, church_m, church_stab, territory_pts, hf_mandate,
             hf_played_challenge, rng):
    """
    Canonical CI seasonal gain. Returns (delta, events, updated stab).
    PP-431-COR: if hf_played_challenge, structural suppression does NOT fire.
    """
    events = []
    delta = 0

    # Step 1: Conditional Passive — +1 if Church prominent in ≥2 territories
    prominent = sum(1 for pt in territory_pts.values() if pt >= 2)
    if prominent >= 2:
        delta += 1
        events.append("CondPassive+1")

    # Step 2: Piety Yield — Σ(PT × SW/5) floored, cap applies later
    py = sum(pt * SW.get(t,1) // 5 for t,pt in territory_pts.items() if pt >= 1)
    if py:
        delta += py
        events.append(f"PietyYield+{py}")

    # Step 5: Assert — Mandate vs Ob 2
    deg, _ = roll(church_m, 2, rng)
    if deg in ("Overwhelming","Success"):
        delta += 1
        events.append(f"Assert+1({deg})")
    elif deg == "Failure":
        church_stab = max(0, church_stab - 1)
        events.append(f"Assert FAIL Stab→{church_stab}")

    # Step 6/7: Hafenmark suppression
    if hf_mandate >= 4:
        ob_sup = (church_m // 2) + 1
        if not hf_played_challenge:
            # Structural suppression fires
            delta -= 1
            events.append("Structural−1")
            # Suppress roll: negate Conditional Passive on success
            sup_deg, _ = roll(hf_mandate, ob_sup, rng)
            if sup_deg in ("Overwhelming","Success") and "CondPassive+1" in events:
                delta -= 1
                events.append("Suppress negates CondPassive−1")
        else:
            # PP-431-COR: Challenge replaced structural — structural does NOT fire
            events.append("Structural suppressed by Challenge (PP-431-COR)")

    # ±5 season cap
    delta = max(-5, min(5, delta))
    return delta, events, church_stab

def seizure_prob(ci): return min(1.0, max(0.0, ((ci-60)/40)**3.3)) if ci>=60 else 0.0

# ─── B4-1: PP-431-COR FIX ────────────────────────────────────────────────────

def sim_b41(seasons=40, seed=42, hf_plays_challenge=True, target="T9") -> dict:
    """
    Corrected suppression race (PP-431-COR).
    When Challenge fires: CI effect from Challenge roll (−1 or −2), but structural −1 does NOT fire.
    When no Challenge: structural −1 fires + Suppress roll.
    """
    rng = random.Random(seed)
    church = dict(STARTING_STATS["Church"])
    hf = dict(STARTING_STATS["Hafenmark"])
    ci = 28
    pts = dict(CANONICAL_PT)
    church_stab = church['Stab']
    log = Log()
    seizure_s = None

    for season in range(1, seasons+1):
        # PT growth toward target each season (Piety Spread)
        if pts[target] < 5:
            deg, _ = roll(church['M'], 2, rng)
            if deg in ("Overwhelming","Success"):
                pts[target] = min(5, pts[target]+1)

        # Hafenmark Parliamentary Challenge this season?
        challenge_fired = False
        challenge_ci_effect = 0
        if hf_plays_challenge and hf['M'] >= 4:
            challenge_fired = True
            deg_ch, _ = roll(hf['M'], 2, rng)  # Ob2 (PI~5-7 range, Ob unchanged)
            if deg_ch == "Overwhelming":
                challenge_ci_effect = -2
            elif deg_ch == "Success":
                challenge_ci_effect = -1
            elif deg_ch in ("Partial","Failure"):
                hf['Stab'] = max(0, hf['Stab']-1)
            if challenge_ci_effect:
                ci = max(0, ci + challenge_ci_effect)
                log.log(season,"Hafenmark",f"Challenge {deg_ch} CI{challenge_ci_effect:+}",f"CI={ci}")

        # CI seasonal gain
        delta, events, church_stab = ci_delta(
            ci, church['M'], church_stab, pts, hf['M'], challenge_fired, rng)
        ci_before = ci
        ci = max(0, min(100, ci + delta))
        log.log(season,"CI",f"{ci_before}→{ci} (Δ{delta:+})","; ".join(events))

        # Seizure check
        if ci >= 60 and seizure_s is None:
            p = seizure_prob(ci)
            if rng.random() < p:
                pool = church['I'] + ci//15
                ob = max(1, 10 - pts[target])
                deg, _ = roll(pool, ob, rng)
                seizure_s = season
                log.log(season,"Church","MASS SEIZURE",
                        f"CI={ci} P={p:.0%} pool={pool} ob={ob} → {deg}")
                break

    return {"log":log,"ci":ci,"seizure_s":seizure_s,"pts":pts,"church_stab":church_stab}

# ─── B4-2: PI TRACK DYNAMICS ─────────────────────────────────────────────────

def sim_b42(seasons=30, seed=42,
            hf_manoeuvre_frequency=1,  # 1=every season, 2=every other
            crown_emergency_powers=False,
            church_seizures_per_10_seasons=2) -> dict:
    """
    Track PI dynamics over time.
    PI starts 7. Range 0-20.
    PI gains: Hafenmark Parliamentary Manoeuvre success +1; Crown Parliamentary Session +1
    PI losses: Crown Emergency Powers −1; Church territorial seizure −1; Coup −3
    PI effects by band:
      8-10: Full Parliament, Crown Policy requires M≥4
      5-7: Standard
      3-4: Degraded, HF Manoeuvre +1 Ob, Crown Decree Ob1
      ≤2: Non-functional, HF loses Manoeuvre, Crown governs by decree, CI+2
    """
    rng = random.Random(seed)
    pi = 7
    ci = 28
    log = Log()
    pi_history = [(0, pi)]
    ci_bonus_seasons = []

    for season in range(1, seasons+1):
        pi_before = pi

        # Hafenmark Parliamentary Manoeuvre
        if hf_manoeuvre_frequency > 0 and season % hf_manoeuvre_frequency == 0:
            if pi >= 3:  # Available at PI≥3 (degraded: +1 Ob)
                ob = 2 + (1 if pi <= 4 else 0)
                deg, _ = roll(4, ob, rng)  # Hafenmark Mandate 4
                if deg == "Overwhelming":
                    pi = min(20, pi+1)
                    ci = max(0, ci-1)
                    log.log(season,"Hafenmark",f"Manoeuvre Overwhelming PI+1/CI-1",f"PI={pi} CI={ci}")
                elif deg == "Success":
                    pi = min(20, pi+1)
                    log.log(season,"Hafenmark",f"Manoeuvre Success PI+1",f"PI={pi}")
                elif deg == "Failure":
                    log.log(season,"Hafenmark",f"Manoeuvre Failure",f"PI={pi}")
            else:
                log.log(season,"Hafenmark","Manoeuvre unavailable (PI≤2)","")

        # Crown Emergency Powers (if enabled, fires when Crown stability pressured)
        if crown_emergency_powers and season % 5 == 0:
            pi = max(0, pi-1)
            log.log(season,"Crown","Emergency Powers PI−1",f"PI={pi}")

        # Church territorial seizure (stochastic — based on CI growth)
        # Simplified: Church seizure fires ~every 10 seasons past CI60
        if ci >= 60 and season % (10 // max(1,church_seizures_per_10_seasons)) == 0:
            pi = max(0, pi-1)
            log.log(season,"Church","Territorial Seizure PI−1",f"PI={pi}")

        # CI growth (simplified — Piety Yield from T9 drives ~+4/season)
        ci_gain = 4 + rng.randint(-1,2)  # rough average
        if pi <= 2:
            ci_gain += 2  # PI≤2 bonus CI+2
            ci_bonus_seasons.append(season)
            log.log(season,"State","PI≤2 — Crown governs by decree; CI+2",f"PI={pi} CI={ci}")
        ci = min(100, ci + ci_gain)

        # Band change logging
        def band(p):
            if p >= 8: return "Full"
            elif p >= 5: return "Standard"
            elif p >= 3: return "Degraded"
            else: return "NonFunctional"
        if band(pi) != band(pi_before):
            log.log(season,"PI",f"Band → {band(pi)}",f"PI={pi}")

        pi_history.append((season, pi))

    return {"log":log,"pi_final":pi,"ci_final":ci,"pi_history":pi_history,
            "ci_bonus_seasons":ci_bonus_seasons}

# ─── B4-3: RDT/TD TRACK CASCADE ─────────────────────────────────────────────

def sim_b43(seasons=40, seed=42,
            hafenmark_pursues_rdt=True) -> dict:
    """
    RDT advances once per arc when conditions met (Hafenmark M≥3, PI≥4,
    controls territory where Church has parish/cathedral).
    TD activates at RDT2; advances each arc when RDT≥2 AND Church plays Assert.
    Test: does Hafenmark reach TD4 (Seizure Ob+2) before Church hits CI60?
    Seizure Ob at T8 (Hafenmark capital): 10 - PT - infra = 10 - 3 = 7 base;
    at TD4: +2 → Ob9. Pool at CI60: 10d. Almost certainly Failure.
    """
    rng = random.Random(seed)
    rdt = 0
    td = 0
    ci = 28
    pi = 7
    hf_m = 4
    hf_stab = 4
    church_m = 5
    log = Log()
    ci_history = []
    seizure_s = None

    for season in range(1, seasons+1):
        # Arc boundary (every 4 seasons = 1 arc in BG)
        arc = season // 4

        # RDT advancement (once per arc, conditions: HF M≥3, PI≥4, Church present in HF territory)
        # Conditions met if hafenmark pursues RDT and hasn't maxed
        if hafenmark_pursues_rdt and season % 4 == 0 and rdt < 5:
            conditions = hf_m >= 3 and pi >= 4
            if conditions:
                rdt = min(5, rdt+1)
                log.log(season,"Hafenmark",f"Reformed Settlement RDT→{rdt}","arc boundary")
                if rdt == 2:
                    td = 0  # TD activates
                    log.log(season,"Hafenmark","TD track activates","RDT2 threshold")
                # RDT3: Church Mandate−1
                if rdt == 3:
                    church_m = max(1, church_m-1)
                    log.log(season,"Hafenmark","RDT3: Church M−1",f"Church M={church_m}")

        # TD advancement (each arc when RDT≥2 AND Church played Assert)
        if rdt >= 2 and season % 4 == 0 and td < 5:
            # Church plays Assert every season; TD advances unless Church Accommodates
            td = min(5, td+1)
            log.log(season,"TD",f"TD→{td}","arc advance (Church asserted)")
            if td == 4:
                log.log(season,"TD","TD4: Church Seizure in HF territories Ob+2","")
            if td == 5:
                log.log(season,"TD","TD5: T8 Gransol PERMANENTLY unseizable","")

        # CI growth (simplified: ~+5/season average with suppression)
        # RDT4: CI suppression extends to HF M≥3
        suppression_threshold = 4 if rdt < 4 else 3
        hf_suppresses = hf_m >= suppression_threshold

        ci_gain = 5  # Piety Yield dominated
        if hf_suppresses:
            ci_gain -= 1  # structural suppression
        ci = min(100, ci + ci_gain)
        ci_history.append(ci)

        # Seizure check
        if ci >= 60 and seizure_s is None:
            p = ((ci-60)/40)**3.3
            if rng.random() < p:
                pt_t8 = CANONICAL_PT["T8"]  # =3
                ob_base = max(1, 10 - pt_t8)  # =7
                td4_bonus = 2 if td >= 4 else 0
                ob_final = min(ob_base + td4_bonus, 10)
                pool = 6 + ci//15  # Church I=6 + floor(CI/15)
                deg, _ = roll(pool, ob_final, rng)
                seizure_s = season
                log.log(season,"Church","MASS SEIZURE at T8",
                        f"CI={ci} ob={ob_final}(base{ob_base}+TD{td4_bonus}) pool={pool} → {deg}")

    return {"log":log,"rdt":rdt,"td":td,"ci_final":ci,"seizure_s":seizure_s,
            "ci_history":ci_history}

# ─── B4-4: ACCORD REVOLT CASCADE ─────────────────────────────────────────────

def sim_b44(seasons=20, seed=42,
            garrisoned_territories=5,   # how many Crown territories have garrisons
            battles_per_season=2,       # each battle → Strain+1, may drop Accord
            accord_recovery=True) -> dict:
    """
    Track Accord and Strain cascade.
    Crown holds T1,T2,T3,T5,T6,T14 (6 territories). garrisoned_territories = how many have units.
    Ungarrisoned at Accord1 → Accord0 at Accounting. Accord0 → Revolt (Mil vs Ob2) → if fail: Uncontrolled + Strain+1.
    Strain thresholds apply their effects each Accounting.
    """
    rng = random.Random(seed)
    crown_territories = ["T1","T2","T3","T5","T6","T14"]
    # Accord starts: T1=3 (capital), others=2
    accord = {t: (3 if t=="T1" else 2) for t in crown_territories}
    garrison = {t: (i < garrisoned_territories) for i,t in enumerate(crown_territories)}
    strain = 0
    crown_mil = 4
    uncontrolled = []
    log = Log()
    strain_history = []

    for season in range(1, seasons+1):
        # Battles drop Accord in contested territories
        if battles_per_season > 0:
            strain = min(10, strain + battles_per_season)  # each battle season +1 Strain

        # Strain threshold effects
        band_name = strain_band(strain)
        if strain >= 7:  # Crisis: Accord−1 in ALL non-capital territories
            for t in crown_territories:
                if t != "T1":
                    accord[t] = max(0, accord[t]-1)
                    if accord[t] == 0 and t not in uncontrolled:
                        log.log(season,"Strain",f"Crisis: {t} Accord→0","revolt pending")
        elif strain >= 5:  # Fracture: Accord−1 in one territory (lowest first)
            lowest = min((t for t in crown_territories if t not in uncontrolled),
                         key=lambda t: accord[t], default=None)
            if lowest:
                accord[lowest] = max(0, accord[lowest]-1)

        # Accord checks (Phase 5 step 4c)
        for t in crown_territories:
            if t in uncontrolled:
                continue
            if accord[t] == 1 and not garrison[t]:
                accord[t] = 0
                log.log(season,"Accord",f"{t} ungarrisoned Accord1→0","revolt triggers")
            if accord[t] == 0:
                # Revolt: garrison fights Popular Uprising
                if garrison[t]:
                    deg, _ = roll(crown_mil, 2, rng)
                    if deg in ("Overwhelming","Success"):
                        accord[t] = 1
                        log.log(season,"Revolt",f"{t} garrison holds",f"→{deg} Accord→1")
                    else:
                        uncontrolled.append(t)
                        garrison[t] = False
                        strain = min(10, strain+1)
                        log.log(season,"Revolt",f"{t} FALLS to Uncontrolled",f"→{deg} Strain→{strain}")
                else:
                    uncontrolled.append(t)
                    strain = min(10, strain+1)
                    log.log(season,"Revolt",f"{t} ungarrisoned Revolt→Uncontrolled",f"Strain→{strain}")

        # Strain decay (−1 if no battles and no revolts this season)
        if battles_per_season == 0 and len(uncontrolled) == 0:
            strain = max(0, strain-1)

        # Accord passive recovery (garrison + no hostile 2 seasons: +1, cap 2)
        if accord_recovery:
            for t in crown_territories:
                if t not in uncontrolled and garrison[t] and accord[t] < 2:
                    accord[t] = min(2, accord[t]+1)

        strain_history.append((season, strain, dict(accord), list(uncontrolled)))
        log.log(season,"State",f"Strain={strain} band={band_name[:8]}",
                f"uncontrolled={uncontrolled} accord={accord}")

    return {"log":log,"strain_final":strain,"accord_final":dict(accord),
            "uncontrolled":uncontrolled,"strain_history":strain_history}

# ─── B4-5: LÖWENRITTER COUP ──────────────────────────────────────────────────

def sim_b45(seasons=30, seed=42,
            coup_advance_rate=0.5) -> dict:
    """
    Coup Counter starts 0, threshold 4. Modeled advancement sources:
    - Crown Stability crises: +1/crisis (Stability≤2 events)
    - Church seizures creating instability: +0.5/seizure
    - PI degradation events: +0.5 per PI band drop
    - Crown Emergency Powers use: +0.5 each
    coup_advance_rate: expected advances per season (0.5 = moderate pressure)

    On Coup (Counter=4):
    - Löwenritter takes T14 (Fort3, Mil6)
    - PI−3
    - Crown loses Löwenritter Mandate support → Crown Mandate−1
    - Löwenritter becomes a faction with M3/I2/W3/Mil6/Stab5

    Test: when does Coup fire under different pressure levels?
    What does the board look like after?
    """
    rng = random.Random(seed)
    coup_counter = 0
    pi = 7
    ci = 28
    crown = dict(STARTING_STATS["Crown"])
    church = dict(STARTING_STATS["Church"])
    loewen = None  # not yet a faction
    coup_season = None
    log = Log()
    pi_history = []

    for season in range(1, seasons+1):
        if coup_season:
            # Post-coup: Löwenritter is active
            # PI degraded, Crown weakened
            # Simulate late-game: Church CI still growing
            ci = min(100, ci+4)
            pi = max(0, pi + rng.randint(-1,0))  # PI stabilizes/degrades slowly
            pi_history.append((season, pi))
            continue

        # Coup Counter advances stochastically
        advance_roll = rng.random()
        if advance_roll < coup_advance_rate:
            coup_counter = min(4, coup_counter+1)
            source = rng.choice(["Crown Stability crisis","Church seizure instability",
                                  "PI band drop","Crown Emergency Powers"])
            log.log(season,"Coup Counter",f"+1 from {source}",f"Counter={coup_counter}")

        # Coup fires at Counter=4
        if coup_counter >= 4 and coup_season is None:
            coup_season = season
            # Effects
            pi = max(0, pi-3)
            crown['M'] = max(1, crown['M']-1)
            loewen = dict(M=3, I=2, W=3, Mil=6, Stab=5)
            log.log(season,"COUP","Löwenritter Coup fires — T14 seized",
                    f"PI−3={pi} Crown M−1={crown['M']} Löwenritter Mil={loewen['Mil']}")
            log.log(season,"PI",f"Band → {'NonFunctional' if pi<=2 else 'Degraded' if pi<=4 else 'Standard'}",
                    f"PI={pi}")
            if pi <= 2:
                log.log(season,"State","PI≤2: Crown governs by decree; CI+2/season",f"CI boost starts")
                ci = min(100, ci+2)

        # Normal CI and PI dynamics
        ci = min(100, ci+4)
        if pi <= 2:
            ci = min(100, ci+2)  # PI≤2 bonus

        # Seizure check (simplified)
        if ci >= 60:
            p = ((ci-60)/40)**3.3
            if rng.random() < p:
                pi = max(0, pi-1)  # Church seizure → PI−1
                log.log(season,"Church","Seizure → PI−1",f"PI={pi} CI={ci}")

        pi_history.append((season, pi))

    return {"log":log,"coup_season":coup_season,"pi_final":pi,"ci_final":ci,
            "crown_m":crown['M'],"loewen":loewen,"pi_history":pi_history}

# ─── MAIN ─────────────────────────────────────────────────────────────────────

SEEDS = [42, 77, 99, 137, 201]

def hdr(t): print(f"\n{'═'*68}\n  {t}\n{'═'*68}")
def sub(t): print(f"\n{'─'*55}\n  {t}\n{'─'*55}")

if __name__ == "__main__":
    print("="*68)
    print("VALORIA — ARC TEST BATCH 4")
    print("PI track, RDT/TD, Accord revolt, Löwenritter Coup, PP-431-COR fix")
    print("="*68)

    # ── B4-1: PP-431-COR ─────────────────────────────────────────────────────
    hdr("B4-1: PP-431-COR — Challenge REPLACES structural suppression")
    sub("B3 model (WRONG): Challenge supplements structural")
    # Simulate the wrong model: both fire
    for seed in SEEDS:
        r = sim_b41(seasons=40, seed=seed, hf_plays_challenge=False)
        print(f"  seed={seed}: seizure S{r['seizure_s']} CI={r['ci']} stab={r['church_stab']}")

    sub("Structural only (no Challenge)")
    for seed in SEEDS:
        r = sim_b41(seasons=40, seed=seed, hf_plays_challenge=False, target="T9")
        print(f"  seed={seed}: seizure S{r['seizure_s']} CI={r['ci']}")

    sub("PP-431-COR correct: Challenge fires, structural replaced")
    for seed in SEEDS:
        r = sim_b41(seasons=40, seed=seed, hf_plays_challenge=True, target="T9")
        print(f"  seed={seed}: seizure S{r['seizure_s']} CI={r['ci']}")

    print("\n  CI comparison (seed 42, structural-only vs corrected Challenge):")
    r_s = sim_b41(40, 42, False, "T9")
    r_c = sim_b41(40, 42, True,  "T9")
    print("  [structural only]")
    r_s['log'].print_arc(20)
    print("  [with Challenge — structural replaced]")
    r_c['log'].print_arc(20)

    # ── B4-2: PI TRACK DYNAMICS ──────────────────────────────────────────────
    hdr("B4-2: PI TRACK DYNAMICS")
    configs = [
        ("Hafenmark manoeuvres every season, no Crown Emergency Powers", 1, False, 1),
        ("Hafenmark manoeuvres every other season", 2, False, 1),
        ("Crown uses Emergency Powers every 5 seasons", 1, True, 1),
        ("Church seizes 3x per 10 seasons (aggressive)", 1, False, 3),
    ]
    for label, freq, emp, seiz in configs:
        sub(label)
        for seed in SEEDS[:3]:
            r = sim_b42(30, seed, freq, emp, seiz)
            nf_seasons = [s for s,p in r['pi_history'] if p <= 2]
            print(f"  seed={seed}: PI_final={r['pi_final']} CI_final={r['ci_final']} "
                  f"PI≤2 seasons: {nf_seasons[:5]}")

    sub("Full log (seed 42, manoeuvre every season + Crown EPs)")
    r42 = sim_b42(30, 42, 1, True, 1)
    r42['log'].print_arc()

    sub("PI history (seed 42, Hafenmark manoeuvre only)")
    r_pi = sim_b42(30, 42, 1, False, 1)
    print("  Season: PI | Band")
    for s,p in r_pi['pi_history'][::3]:
        band = ("Full" if p>=8 else "Standard" if p>=5 else "Degraded" if p>=3 else "NonFunctional")
        print(f"  S{s:02d}:  {p:2d} | {band}")

    # ── B4-3: RDT/TD TRACK ───────────────────────────────────────────────────
    hdr("B4-3: RDT/TD TRACK — CAN HAFENMARK REACH TD4 BEFORE CHURCH HITS CI60?")
    sub("Hafenmark pursues RDT")
    for seed in SEEDS:
        r = sim_b43(40, seed, hafenmark_pursues_rdt=True)
        ci60_s = next((i+1 for i,c in enumerate(r['ci_history']) if c>=60), None)
        print(f"  seed={seed}: RDT={r['rdt']} TD={r['td']} CI60@S{ci60_s} seizure@S{r['seizure_s']} ob_bonus={2 if r['td']>=4 else 0}")

    sub("No RDT pursuit (baseline)")
    for seed in SEEDS:
        r = sim_b43(40, seed, hafenmark_pursues_rdt=False)
        ci60_s = next((i+1 for i,c in enumerate(r['ci_history']) if c>=60), None)
        print(f"  seed={seed}: RDT={r['rdt']} TD={r['td']} CI60@S{ci60_s} seizure@S{r['seizure_s']}")

    sub("Full log (seed 42, RDT pursuit)")
    sim_b43(40, 42, True)['log'].print_arc()

    # ── B4-4: ACCORD REVOLT ──────────────────────────────────────────────────
    hdr("B4-4: ACCORD REVOLT CASCADE")
    configs_ac = [
        ("All 6 territories garrisoned, 1 battle/s",  6, 1),
        ("4 garrisoned, 1 battle/s",                  4, 1),
        ("4 garrisoned, 2 battles/s",                 4, 2),
        ("2 garrisoned, 2 battles/s",                 2, 2),
    ]
    for label, garr, bps in configs_ac:
        sub(label)
        for seed in SEEDS[:3]:
            r = sim_b44(20, seed, garr, bps)
            print(f"  seed={seed}: Strain={r['strain_final']} "
                  f"uncontrolled={r['uncontrolled']} "
                  f"accord={r['accord_final']}")

    sub("Full log (seed 42, 4 garrisoned, 2 battles/s)")
    sim_b44(20, 42, 4, 2)['log'].print_arc()

    sub("Strain progression (seed 42, 4 garrisoned, 2 battles/s)")
    r_ac = sim_b44(20, 42, 4, 2)
    print("  S  | Strain | Band         | Uncontrolled")
    for s, strain, acc, unc in r_ac['strain_history'][::2]:
        print(f"  S{s:02d} | {strain:6d} | {strain_band(strain)[:12]:<12} | {unc}")

    # ── B4-5: LÖWENRITTER COUP ───────────────────────────────────────────────
    hdr("B4-5: LÖWENRITTER COUP — TIMING AND AFTERMATH")
    configs_coup = [
        ("Low pressure (0.25 advance/season)",   0.25),
        ("Moderate pressure (0.5 advance/season)",0.50),
        ("High pressure (0.75 advance/season)",  0.75),
    ]
    for label, rate in configs_coup:
        sub(label)
        for seed in SEEDS:
            r = sim_b45(30, seed, rate)
            cs = f"S{r['coup_season']}" if r['coup_season'] else "no coup"
            print(f"  seed={seed}: coup {cs} PI_final={r['pi_final']} "
                  f"CI_final={r['ci_final']} Crown_M={r['crown_m']}")

    sub("Full log (seed 42, moderate pressure)")
    r_coup = sim_b45(30, 42, 0.5)
    r_coup['log'].print_arc()
    sub("Post-coup board state (seed 42):")
    if r_coup['coup_season']:
        print(f"  Coup fired: S{r_coup['coup_season']}")
        print(f"  PI after coup: {r_coup['pi_final']} (PI≤2: Crown governs by decree, CI+2/season)")
        print(f"  Crown Mandate: {r_coup['crown_m']}")
        print(f"  Löwenritter: {r_coup['loewen']}")
        print(f"  CI at end: {r_coup['ci_final']}")
        nf = [s for s,p in r_coup['pi_history'] if p<=2]
        print(f"  PI≤2 (NonFunctional) seasons: {nf}")
    else:
        print("  No coup in 30 seasons.")

    # ── CROSS-SYSTEM SUMMARY ─────────────────────────────────────────────────
    hdr("CROSS-SYSTEM SUMMARY (seed 42)")
    r41 = sim_b41(40, 42, True,  "T9")
    r41s= sim_b41(40, 42, False, "T9")
    r42_ = sim_b42(30, 42, 1, False, 1)
    r43_ = sim_b43(40, 42, True)
    r44_ = sim_b44(20, 42, 4, 2)
    r45_ = sim_b45(30, 42, 0.5)
    ci60 = next((i+1 for i,c in enumerate(r43_['ci_history']) if c>=60), None)

    print(f"\n  {'System':<35} {'Key finding'}")
    print(f"  {'─'*68}")
    rows = [
        ("B4-1 Structural only",
         f"Seizure S{r41s['seizure_s']} CI={r41s['ci']}"),
        ("B4-1 PP-431-COR Challenge",
         f"Seizure S{r41['seizure_s']} CI={r41['ci']}"),
        ("B4-2 PI track (HF manoeuvre)",
         f"PI_final={r42_['pi_final']} CI_final={r42_['ci_final']}"),
        ("B4-3 RDT/TD (HF pursues RDT)",
         f"RDT={r43_['rdt']} TD={r43_['td']} CI60@S{ci60} Seizure@S{r43_['seizure_s']}"),
        ("B4-4 Accord revolt (4 garr, 2 bps)",
         f"Strain={r44_['strain_final']} uncontrolled={r44_['uncontrolled']}"),
        ("B4-5 Löwenritter Coup (moderate)",
         f"Coup S{r45_['coup_season']} PI={r45_['pi_final']}"),
    ]
    for label, finding in rows:
        print(f"  {label:<35} {finding}")
