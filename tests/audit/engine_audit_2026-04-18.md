# Engine Audit: engine_v2.py vs Canonical BG Mechanics
# Date: 2026-04-18
# Sources: params/bg/core.md, params/bg/phases.md, params/bg/victory.md,
#          params/bg/npc_priority_trees.md, params/bg/faction_actions.md,
#          params/core.md (dice), params/bg/clocks.md

---

## 1. DICE SYSTEM

### Canonical (params/core.md + params/bg/core.md)
- d10 pool. Face 1 = −1 success. Face 2–6 = 0. Face 7–9 = +1. Face 10 = +2.
- Net successes = sum of all contributions. May be negative.
- Degrees: Overwhelming = net ≥ 2×Ob AND net ≥ 3. Success = net ≥ Ob. Partial = 0 < net < Ob. Failure = net ≤ 0.
- TN 7 standard. TN 6 controlled. TN 8 desperate.
- Pool floor: 1D. Ob floor: 1.

### engine_v2.py implementation
```python
def roll_pool(pool, tn=7):
    return sum(1 for _ in range(pool) if random.randint(1,10) >= tn)

def check(pool, ob, tn=7):
    s = roll_pool(pool, tn)
    return s >= ob, s - ob, 'overwhelming' if s-ob>=3 else ('success' if s>=ob else ('partial' if s==ob-1 else 'failure'))
```

### Gaps
- G-DICE-01: `roll_pool` uses `randint(1,10) >= tn`. This counts faces ≥ 7 as +1 each. Face 10 is counted as +1 only, not +2. **Face 10 bonus missing.**
- G-DICE-02: Face 1 penalty (−1 success) not implemented. All faces 1–6 produce 0 successes. Net can never go negative from die rolls alone.
- G-DICE-03: Overwhelming condition is `s - ob >= 3`, i.e. margin ≥ 3. Canonical is net ≥ 2×Ob AND net ≥ 3. At Ob 1 these are equivalent. At Ob 2: canonical requires net ≥ 4 AND net ≥ 3 → net ≥ 4. Engine uses net ≥ 3 at Ob 2 → **Overwhelming fires too easily at Ob ≥ 2.**
- G-DICE-04: Partial is `s - ob == -1` (margin exactly −1). Canonical Partial is 0 < net < Ob. At Ob 3: canonical Partial = net 1 or 2. Engine Partial = net 2 only (margin −1 = successes = ob−1 = 2). **Partial range wrong at Ob > 2: net=1 becomes Failure in engine, Partial canonically.**

---

## 2. FACTION STARTING STATE

### Canonical (params/bg/core.md)
| Faction | Mandate | Influence | Wealth | Military | Stability | Starting TCV |
|---------|---------|-----------|--------|----------|-----------|-------------|
| Crown | 5 | 5 | 4 | 4 | 4 | 12 |
| Church | 5 | 6 | 5 | 4 | 5 | 3 |
| Hafenmark | 4 | 4 | 5 | 3 | 4 | 8 |
| Varfell | 4 | 4 | 4 | 4 | 4 | 6 |

### engine_v2.py / state.py
```python
'Crown':    Faction('Crown',    mandate=5, wealth=4, military=4, influence=5, stability=4)
'Church':   Faction('Church',   mandate=4, wealth=3, military=4, influence=6, stability=5)
'Hafenmark':Faction('Hafenmark',mandate=4, wealth=5, military=3, influence=4, stability=4)
'Varfell':  Faction('Varfell',  mandate=3, wealth=3, military=4, influence=3, stability=3)
```

### Gaps
- G-STAT-01: Church Mandate = 4 in engine, canonical = **5**.
- G-STAT-02: Church Wealth = 3 in engine, canonical = **5**.
- G-STAT-03: Varfell Mandate = 3 in engine, canonical = **4**.
- G-STAT-04: Varfell Wealth = 3 in engine, canonical = **4**.
- G-STAT-05: Varfell Influence = 3 in engine, canonical = **4**.
- G-STAT-06: Varfell Stability = 3 in engine, canonical = **4**.

**Note: Church and Varfell are both significantly undertuned. Church missing 1 Mandate + 2 Wealth. Varfell missing 1 each of Mandate/Wealth/Influence/Stability. This directly affects victory probability for both factions.**

---

## 3. STARTING TRACK VALUES

### Canonical (params/bg/core.md)
- RS = 72, TC = 28, IP = 20, PI = 7
- Torben Loyalty = 7, Elske Loyalty = 4
- Löwenritter Coup Counter = 0
- WC = 0, WR = 0, Peninsular Strain = 0
- AER = 2

### engine_v2.py / state.py
```python
rs: int = 72    # correct
tc: int = 28    # correct
ip: int = 5     # WRONG — canonical = 20
pi: int = 7     # correct
```

### Gaps
- G-TRACK-01: IP starts at 5 in engine. Canonical = **20**. IP governs Altonian pressure; understart delays Altonian intervention significantly.
- G-TRACK-02: Torben Loyalty not tracked in engine state. No `torben_loyalty` field.
- G-TRACK-03: Elske Loyalty not tracked.
- G-TRACK-04: Peninsular Strain not tracked as a separate field (embedded loosely in `strain: int = 0` but not driven by canonical Strain rules).
- G-TRACK-05: AER not tracked.
- G-TRACK-06: WR (Warden Recognition) not tracked separately from WC.
- G-TRACK-07: Löwenritter Coup Counter not tracked.
- G-TRACK-08: PT (Piety Track) per territory is tracked, but starting values partially wrong. Canonical T4=2, T6=1, T11=2, T12=2, T13=1. Engine sets T6=1, T13=1, T4=2, T11=2, T12=2 — **these match canonical**. T15 hard-fixed at 0 — **correct**.

---

## 4. PHASE RESOLUTION ORDER

### Canonical (params/bg/phases.md)
Phase 4 priority: 1=Intel/Covert, 2=Military/Battle, 3=Domain, 4=Social, 5=Thread, 6=Special, 7=Project.
Phase 5 Accounting: 13-step sequence including Stability checks, clock advances, Accord checks, Peninsular Strain update, Battle consequence accounting, Church Attention Pool, Thread Debt, Warden checks, Torben/Elske Loyalty events, Victory check.

### engine_v2.py
`run_season` executes: personal actions (random policy weights) → mass battle (random chance) → faction AI (simple stat adjustments) → accounting (income/legitimacy/cohesion) → RS drift → subsystem evaluations.

### Gaps
- G-PHASE-01: No Phase 4 priority ordering. Actions fire in arbitrary order from policy weights.
- G-PHASE-02: Card-hand economy absent entirely. No Legionary/Consul/Senator/Tribune/Pontifex/Recess cards. Faction actions are not constrained by hand composition.
- G-PHASE-03: Domain action Obs not computed. Govern Ob = floor(Prosperity/2)+1 canonically. Engine uses `resolve_governance` which likely uses a fixed Ob.
- G-PHASE-04: Accounting steps 1–13 not implemented. Engine does a simplified income/stat calculation only.
- G-PHASE-05: Accord checks (Phase 5 step 4c) not implemented. No garrison check, no Revolt resolution.
- G-PHASE-06: Peninsular Strain update (Phase 5 step 4d) not implemented canonically. No −1 for peaceful seasons, no Revolt contribution.
- G-PHASE-07: Church Attention Pool (Phase 5 step 5) not tracked.
- G-PHASE-08: Thread Debt (Phase 5 step 6) not tracked.
- G-PHASE-09: Warden Emergence check (Phase 5 step 9) absent.
- G-PHASE-10: Torben/Elske Loyalty events (Phase 5 step 10b) absent.
- G-PHASE-11: Year-End Accounting (every 4th season) not separated from seasonal accounting.

---

## 5. TC GENERATION

### Canonical (params/bg/tc_seizure.md — header: "TC Generation — Seasonal")
TC advances each season per the TC generation formula. At TC ≥ 75: Territorial Seizure phase begins, TC freezes.

### engine_v2.py
```python
if fname == 'Church':
    if gs.tc < 75 and f.mandate >= 4:
        gs.tc = min(100, gs.tc + 1)
```
Church faction AI adds TC +1/season if Mandate ≥ 4 and TC < 75.

### Gaps
- G-TC-01: TC generation formula not loaded from canonical source. Need to read params/bg/tc_seizure.md fully to confirm the formula. Engine uses a simplified +1/season from Church AI only.
- G-TC-02: TC contributions from other sources (Piety Assert action, territorial PT values, Church Seizure Domain Actions) not modelled.
- G-TC-03: TC freeze at 75 is checked (`gs.tc < 75`) but TC ceiling in engine is set to 100 (`min(100, gs.tc + 1)`). **TC should freeze at 75, not continue to 100.**

---

## 6. FACTION AI

### Canonical (params/bg/npc_priority_trees.md)
Each faction has a 7-priority tree with specific conditions and actions. Church P3: Assert (TC+1) if TC < 75 AND Mandate ≥ 4. Crown P2: Military response if 2+ territories changed OR Coup Counter = 2 OR PI ≥ 8. Etc.

### engine_v2.py
```python
if fname == 'Church':
    if f.stability <= 2: f.cohesion += 10
    elif gs.tc < 75 and f.mandate >= 4: gs.tc = min(100, gs.tc + 1)
elif fname == 'Crown':
    if f.stability > 2 and random.random() < 0.4:
        weakest = min(['mandate','wealth','military','influence','stability'], key=lambda a: getattr(f,a))
        setattr(f, weakest, min(7, getattr(f, weakest) + 1))
elif fname == 'Hafenmark':
    if gs.tc >= 50 and f.mandate >= 4: gs.tc = max(0, gs.tc - 1)
elif fname == 'Varfell':
    pass
```

### Gaps
- G-AI-01: Church only implements P1 (stability) and one P3 action. P2 (Heresy Investigation), P4 (Piety expand), P5 (AER), P6 (Templar) absent.
- G-AI-02: Crown only implements a random stat-boost. No P2 military response, no P3 Royal Decree, no P5 Torben Loyalty maintenance.
- G-AI-03: Hafenmark TC suppression is not a canonical action (no TC suppress action in Hafenmark's tree). Hafenmark P3 is "Suppress available: suppress TC" — but only if `Church M ≥ 4 AND Baralta M ≥ 4`. Engine fires on TC ≥ 50 regardless of Mandate conditions.
- G-AI-04: Varfell AI is a complete stub (`pass`). No intelligence gathering, no VTM advancement, no Patience Protocol.
- G-AI-05: NPC factions (Guilds, Niflhel, Löwenritter, Ministry, Schoenland, Altonian) have no AI at all.

---

## 7. VICTORY CONDITIONS

### Canonical (params/bg/victory.md)
- Crown: TCV ≥ 16 + suppress all rivals + IP < 60 + PI ≥ 3. Sustained 2 consecutive Accountings.
- Church: TCV ≥ 8 + PT ≥ 3 in all held territories. Sustained 2 consecutive.
- Hafenmark: TCV ≥ 12 + Mandate ≥ 4 + PI ≥ 5 + Crown Mandate ≤ 3. Sustained 2 consecutive.
- Varfell Path A: TCV ≥ 10 + VTM ≥ 3 + 2 rival stats revealed + 1 expansion territory.
- Varfell Path B: TCV ≥ 8 + VTM ≥ 3 + T13 + T15 presence + WA ≥ +1.
- Varfell Path C: TCV ≥ 10 + VTM = 5 + RS ≥ 50.
- All checked at Accounting Step 12. Shared loss checked first.

### engine_v2.py (subsystems.py — check_victory)
Not read yet. Need to audit separately.

---

## 8. RS DECAY

### Canonical (params/core.md)
- Baseline: −1 RS per in-game year (4 seasons). Applied at Year-End Accounting only.
- Board Game starting RS = 72.

### engine_v2.py
```python
gs.rs = max(0, gs.rs - random.choice([0, 0, 0, 1]))
```
RS decays by 0 or 1 each season, randomly. Over 120 seasons = 30 years, expected decay ≈ 30 (0.25/season × 120).

### Gaps
- G-RS-01: Canonical baseline decay is exactly −1/year at Year-End. Engine applies probabilistic −0 or −1 each season. Expected rate matches (0.25/season = 1/year) but **the mechanism is wrong**: decay should only fire at Year-End (season 4, 8, 12...), not probabilistically each season.
- G-RS-02: Thread operation RS contributions not modelled canonically. Thread Debt tokens not tracked.

---

## 9. TERRITORIAL / TCV TRACKING

### Canonical
TCV = sum of TCV values for controlled territories (Accord ≥ 2 required for TCV contribution). Total = 30.

### engine_v2.py / state.py
Faction territories stored as lists. No Accord per territory tracked on the faction object — Accord is computed from settlement Order scores. TCV not computed anywhere visible in engine_v2.py.

### Gaps
- G-TCV-01: TCV not computed as a tracked state variable. Victory conditions cannot be evaluated without it.
- G-TCV-02: Accord ≥ 2 gate for TCV contribution not enforced.
- G-TCV-03: Territory transfers (conquest, vacuum, revolt) not modelled in engine.

---

## SUMMARY: GAP CATEGORIES

| Category | Count | Severity |
|----------|-------|----------|
| Dice system | 4 | High — affects all roll outcomes |
| Faction starting stats | 6 | High — affects balance directly |
| Starting track values | 8 | High — IP especially |
| Phase resolution | 11 | High — entire turn structure wrong |
| TC generation | 3 | Medium — TC rate undertuned |
| Faction AI | 5 | High — Varfell complete stub |
| Victory conditions | TBD — subsystems.py unread | — |
| RS decay | 2 | Low — rate correct, mechanism wrong |
| TCV tracking | 3 | High — victory unreachable without it |

**Total confirmed gaps: 42+ (subsystems.py not yet read)**

---

## BRANCH POINTS FOR ALTERNATE SIMULATIONS

Before simulations can produce meaningful results for iterative testing, the following must be corrected:

1. **Dice (G-DICE-01/02/03/04)** — affects every roll in every system. Fix first.
2. **Starting stats (G-STAT-01 through 06)** — Church and Varfell undertuned; directly causes victory imbalance.
3. **IP starting value (G-TRACK-01)** — IP=5 vs canonical 20; delays Altonian pressure by many seasons.
4. **TCV tracking (G-TCV-01/02/03)** — required for any victory check.
5. **Varfell AI stub (G-AI-04)** — Varfell takes no actions. Cannot win.
6. **TC freeze at 75 (G-TC-03)** — TC advances past 75 in engine.

Items 2 and 5 alone explain the 0/11 victory result and equal-faction-probability failure: Varfell does nothing and Church/Varfell start undertuned.


---

## 10. VICTORY CONDITIONS — check_victory (subsystems.py)

### Implementation
```python
tcv = len(f.territories)  # counts territories, not TCV values

Crown: tcv >= 14 and mandate >= 4
Church: tc >= 75 and tcv >= 8
Hafenmark: tcv >= 13 and mandate >= 4
Varfell: flags 'varfell_path_check' unconditionally
```

### Gaps
- G-VIC-01: TCV = `len(f.territories)` — **territory count, not TCV value sum**. Crown has 6 starting territories (TCV=12). Engine Crown victory fires at 14 territories. Canonical Crown victory requires TCV ≥ 16 (a value sum). These are different conditions entirely.
- G-VIC-02: Crown canonical conditions also require IP < 60, PI ≥ 3, and suppression of all rivals. Engine checks only TCV proxy and Mandate. **Crown cannot win canonically per engine conditions.**
- G-VIC-03: Church canonical condition is TCV ≥ 8 + PT ≥ 3 in all held territories. Engine checks TC ≥ 75 + territory count ≥ 8. **PT condition absent.** Church can "win" with TC=75 regardless of PT state.
- G-VIC-04: Hafenmark canonical: TCV ≥ 12 + Mandate ≥ 4 + PI ≥ 5 + Crown Mandate ≤ 3. Engine checks territory count ≥ 13 + Mandate ≥ 4. **PI ≥ 5 and Crown Mandate ≤ 3 absent.**
- G-VIC-05: Varfell check fires `features_fired.add('varfell_path_check')` unconditionally every season. Not a victory check — a feature-coverage marker.
- G-VIC-06: 2-consecutive-Accounting requirement absent for all factions.
- G-VIC-07: Shared loss conditions (RS=0, IP≥100+AER≤1, all factions Stability 0) partially present but RS=0 not checked, AER not tracked.
- G-VIC-08: Co-victory check fires randomly (`random.random() < 0.02`) — not mechanically evaluated.

---

## REVISED SUMMARY

| Category | Gaps | Severity |
|----------|------|----------|
| Dice system | 4 | Critical |
| Faction starting stats | 6 | Critical |
| Starting track values (IP, Torben, Elske, Strain, AER, WR, Coup Counter) | 8 | High |
| Phase resolution (turn structure, card economy, Accounting steps) | 11 | Critical |
| TC generation | 3 | High |
| Faction AI (Varfell stub, Church/Crown/Hafenmark incomplete, NPC factions absent) | 5 | Critical |
| Victory conditions (TCV calculation, condition sets, 2-step requirement) | 8 | Critical |
| RS decay (mechanism wrong, Thread Debt absent) | 2 | Low |
| TCV tracking | 3 | Critical |
| **Total** | **50** | — |

## CONCLUSION

The previous 11 NPC PC simulations used an engine with 50 confirmed mechanical gaps against canonical sources. Results are not valid for iterative balance testing. The engine must be rebuilt against canonical params before NPC simulations can produce actionable data.

**Recommended rebuild order (each is a prerequisite for the next):**
1. Dice system (d10 with face 1/10 bonuses, correct degree table)
2. Game state (correct starting stats, all tracks)
3. TCV calculation from territory values and Accord gate
4. Victory condition checks (all canonical conditions, 2-step requirement)
5. TC generation from canonical formula
6. RS decay (Year-End only, Thread Debt)
7. Accord tracking and garrison rules
8. Faction AI priority trees (implement 7-level trees per faction)
9. Phase resolution order
10. Card-hand economy (Legionary/Consul/Senator/Tribune/Pontifex/Recess)

Items 1–6 are sufficient for a first meaningful simulation pass with simplified AI. Items 7–10 are required for full canonical fidelity.
