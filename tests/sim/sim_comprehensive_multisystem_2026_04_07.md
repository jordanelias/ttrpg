# Valoria Comprehensive Multi-System Stress Test
<!-- SIM-DATE: 2026-04-07 | MODES: A, D, G1, G2, G3, B | EFFORT: 125 -->

---

## SIMULATION INDEX

| ID | System | Test | Finding Class |
|----|--------|------|--------------|
| SIM-BG-01 | Board Game | TC pacing: Church vs Hafenmark suppression, S1–S20 | P2 |
| SIM-BG-02 | Board Game | Church Seizure Ob range — territory immunity analysis | P1 |
| SIM-BG-03 | Board Game | Crown TCV 18 bottleneck — late-game victory feasibility | P1 |
| SIM-BG-04 | Board Game | PI collapse cascade — Löwenritter coup chain | P2 |
| SIM-BG-05 | Board Game | RS passive decay — time to Rupture without Warden Cooperation | P2 |
| SIM-HY-01 | Hybrid | Domain Echo stacking — same-scene multiple echoes | P1 |
| SIM-HY-02 | Hybrid | Zoom In at illegal phase entry | P2 |
| SIM-HY-03 | Hybrid | Scope shift Inspiration cost interaction | CLEAN |
| SIM-MC-01 | Mass Combat | Command cap degenerate — Size 7 Command 2 | P1 |
| SIM-MC-02 | Mass Combat | Heavy Infantry vs Light Infantry asymmetric engagement | P2 |
| SIM-MC-03 | Mass Combat | Morale cascade from general death | P2 |
| SIM-DB-01 | Debate | CLASH dominant strategy — Revealing vs Obscuring | P2 |
| SIM-DB-02 | Debate | AMPLIFY vs high-resistance audience — stalemate detection | P1 |
| SIM-DB-03 | Debate | Composure bleed rate — median pool concession threshold | CLEAN |
| SIM-PC-01 | Personal Combat | Weapon TN cliff — TN5 vs TN8 comparative analysis | P2 |
| SIM-PC-02 | Personal Combat | Initiative information value — flip probability | CLEAN |
| SIM-PC-03 | Personal Combat | Wound accumulation — non-functionality threshold | P2 |

---

## BOARD GAME MODE

---

### SIM-BG-01 — TC Pacing: Church vs Hafenmark Suppression (S1–S20)

```
Test ID: SIM-BG-01
Mechanics: TC generation formula, Conviction Yield, Hafenmark Structural Suppression
Mode: BG | Temporal: PRES/FUT
Tracks: TC | Factions: Church, Hafenmark
NPCs: Himlensendt, Baralta | Archetypes: Expansion vs Suppression
```

**Setup:** Church Mandate 5, Influence 6. Himmelenger (T14) = CV 5. No other Church-prominent territory initially. Baralta Mandate ≥ 4 (Hafenmark structural suppression active: TC −1/season). Church attempts Assert each season (Influence 6D, TN7, Ob2).

**TC Generation formula (per season):**
- Institutional Momentum: +1 (passive, Mandate 5+)
- Conviction Yield: CV 5 in T14 = +1; CV 4 in T14 = +0.5. Start: T14 CV = 5 (from memory: Himmelenger starts at 5). No other prominent territories initially.
- Assert: 6D TN7 Ob2. E[net] = 6×0.33 = 2.0. P(≥2) ≈ 70%. Expected contribution: 0.70×1 = +0.70/season
- Hafenmark suppression: −1/season (Baralta Mandate ≥ 4 active from start)

**Net TC per season (baseline, no second territory):**
= 1 (momentum) + 1 (T14 CV5) + 0.70 (Assert) − 1 (Hafenmark) = **+1.70/season**

**Seasons to TC 75 from start (TC=28, need +47):**
= 47 ÷ 1.70 = **~27.6 seasons**

**With Assert failing (pessimistic):** 1 + 1 − 1 = 1.0/season → 47 seasons (unacceptably slow)

**With second prominent territory at CV 5 (e.g. T14 seized in S10):**
= 1 + 2 + 0.70 − 1 = **2.70/season** → 47÷2.70 = **~17.4 seasons from game start**

**TC threshold crossings:**
| TC | Season (median play) |
|----|---------------------|
| 30 | ~S1 (already near; S1–2) |
| 50 | ~S12–S13 |
| 75 | ~S25–S28 |

**TC 50 effect trigger:** Church orders −1 Ob everywhere + mandatory Assert/Suppress each season. This locks in 2 forced actions per season and removes the optional Assert opportunity cost — no downside to Assert once mandatory.

**Post-TC 50 Assert pacing:**
Mandatory Assert removes the decision cost. TC gains increase: net now includes forced Assert at higher success rate (Mandate growing). If Mandate reaches 6 by TC 50: 7D TN7 Ob2, P(≥2) ≈ 80%. Assert contribution: +0.80.
Net at Mandate 6, 2 territories: 1 + 2 + 0.80 − 1 = **2.80/season** → TC 75 by ~S24.

**FINDING P2 — TC pace is slow but viable; Hafenmark suppression is mechanically significant:** Without suppression, TC reaches 75 ~6 seasons faster (S18 vs S24). Hafenmark suppression at Mandate ≥ 4 delays the Church by 6 seasons on average — a substantial, meaningful pressure. However: Hafenmark loses suppression if Baralta drops below Mandate 4. If Hafenmark is pressured militarily (Mandate −1 from combat losses), Church escapes suppression and accelerates to S18. **No P1. Mechanical interaction is working as designed. Flag for simulation: what Hafenmark Mandate level does Crown/Church pressure typically produce by S12?**

---

### SIM-BG-02 — Church Seizure Ob Range Analysis (Mode A: Isolation)

```
Test ID: SIM-BG-02
Mechanics: Church Seizure Ob formula, Prominence prerequisite, CV values
Mode: BG | Temporal: FUT (post-TC 75)
Tracks: TC, CV | Factions: Church | NPCs: Himlensendt
Archetypes: Territorial Expansion
```

**Seizure Ob formula:** Ob = 2 + Fort Level + max(0, 3 − CV)

**Church action pool for seizure:** Influence 6D TN7 (base). Church Mandate 5 required (check: "Church Mandate ≥ 4 required"). At TC 50–74: −1 Ob Church orders everywhere = effective Ob reduction. After TC 75 Ob reduction no longer applies (TC frozen, seizure protocol active — [GAP: does the −1 Ob Church-everywhere modifier from TC 50–69 carry through to TC 75+ seizure? Not explicitly stated in params.])

**Full Ob range (no ethical modifier, 6D pool):**

| Fort Level | CV=5 | CV=4 | CV=3 | CV=2 | CV=1 | CV=0 |
|-----------|------|------|------|------|------|------|
| 0 | 2 | 2 | 2 | 3 | 4 | 5 |
| 1 | 3 | 3 | 3 | 4 | 5 | 6 |
| 2 | 4 | 4 | 4 | 5 | 6 | 7 |
| 3 | 5 | 5 | 5 | 6 | 7 | 8 |

**Church seizure pool: 6D TN7. E[net] = 2.0.**
- Ob 2: P(Success+) ≈ 70% — viable
- Ob 3: P(Success+) ≈ 51% — contested
- Ob 4: P(Success+) ≈ 33% — difficult
- Ob 5: P(Success+) ≈ 20% — low odds
- Ob 6: P(Success+) ≈ 11% — near-impossible
- Ob 7: P(Success+) ≈ 5% — effectively blocked
- Ob 8: P(Success+) < 2% — **de facto immune**

**Territory immunity thresholds:**
- Fort 3, CV ≤ 2 (Ob 6+): de facto immune at 6D Church pool
- Fort 2, CV = 0 (Ob 7): de facto immune
- Fort 3, CV = 0 (Ob 8): **absolute immunity** — cannot seize

**Practical immunity map:** Any well-fortified territory (Fort 2+) with low CV (≤ 1) is effectively immune to Church seizure. The implication: opponents who actively suppress CV and invest in fortification can create permanent seizure barriers even at TC 75+. This is intentional design — but:

**FINDING P1 — Seizure Ob formula creates a hard immunity wall at Fort 3 + CV 0:** Ob 8 means a 6D Church pool produces Overwhelming on ~2% of rolls, Success on another ~3%. In expectation, the Church would need ~14 attempts (14 seasons) to succeed once. Since the Church gets one seizure attempt per season and victory requires ≥10 TCV, a single Fort 3 CV-0 territory effectively walls off that region permanently. This means any faction that fortifies a buffer territory and maintains low CV can halt Church victory indefinitely. **No mechanic exists to break this wall except Prominence loss (if Church Mandate drops below target faction Mandate).**

**Additional finding:** Prominence prerequisite (Church Mandate > controlling faction Mandate) means if any faction maintains Mandate ≥ Church Mandate (currently 5), zero seizure attempts are legal. Crown at Mandate 5 = all Crown territories immune from seizure (tie = not prominent). Church must raise Mandate to 6 first, costing actions and Wealth.

**[EDITORIAL: P1 BLOCKER CANDIDATE] — Seizure immunity: does Church have any mechanic to reduce Fort level or raise CV in a target territory before seizure?** If not, Church victory requires opponents to neglect both fortification and CV management simultaneously. Consider: Assert action raising CV in adjacent territory (propaganda spread) as a pre-seizure softening mechanic.

---

### SIM-BG-03 — Crown TCV 18 Bottleneck: Late-Game Victory Feasibility

```
Test ID: SIM-BG-03
Mechanics: Crown victory conditions, TCV, territory control, IP/PI constraints
Mode: BG | Temporal: FUT (late game)
Tracks: TCV, IP, PI | Factions: Crown | NPCs: Generic Crown
Archetypes: Hegemonic expansion
```

**Crown victory requirements (all simultaneous, 2 consecutive Accounting):**
- TCV ≥ 18
- Suppress all rivals (all other playable factions: Mandate ≤ ?) [GAP: "suppress all rivals" definition — what is the suppression threshold? Mandate ≤ 2? Stability 0?]
- IP < 60
- PI ≥ 3

**TCV = 18:** The board has 17 territories total. Schoenland (T16) and Askeheim (T15) likely have special rules. [GAP: Schoenland and Askeheim TCV values not confirmed in params read.]

**If TCV counts only 15 territories:** 18/15 = Crown needs to hold all territories plus some multiplier. This implies TCV ≠ territory count — TCV must be a sum of territory values.

[GAP: TCV per-territory values not present in read params. TCV formula/table location unknown. Cannot complete TCV feasibility sim without per-territory TCV values.]

**Tractable sub-analysis: IP constraint.**
IP starts 20. Crown victory requires IP < 60. IP threshold for Altonian Vanguard deployment = 75. 
- IP rises from: Altonian pressure (autonomous), Trade Ob failures, AER decreasing.
- IP falls from: Schoenland trade success (−1D at IP < 30), diplomatic actions (AER-linked).
- Crown at high TCV (most territories) → fewer Trade opportunities to suppress IP (most territories already Crown; Trade outward targets non-Crown territory).

**If Crown holds 15+ territories by S20:** All Trade actions are inward or to Schoenland. IP management becomes primary action economy constraint — Crown must allocate Senator actions to IP suppression while simultaneously maintaining suppression of rival Mandates. **Action economy pressure is severe at TCV 15+.**

**FINDING P1 — "Suppress all rivals" definition gap:** Without a canonical definition of "suppress all rivals," Crown victory condition is unresolvable. Does it mean: all rivals at Stability 0? Mandate ≤ some threshold? Eliminated? This is not a simulation finding — it is a missing rule. **[EDITORIAL: suppress all rivals requires explicit threshold. Flagging as ED-candidate.]**

**FINDING P2 — Crown victory likely requires 20+ seasons and extreme board dominance:** Even at optimal play, Crown must simultaneously: hold TCV 18, manage IP < 60, maintain PI ≥ 3, and suppress all rivals across 2 consecutive Accounting steps. The 2-consecutive-step requirement means Crown must achieve this 2 seasons in a row — any disruption resets the clock. This is the hardest victory condition by design (BALANCE-001 P1-BLOCKER). Flagging to existing BALANCE-001.

---

### SIM-BG-04 — PI Collapse Cascade: Löwenritter Coup Chain

```
Test ID: SIM-BG-04
Mechanics: PI degradation triggers, Löwenritter Coup Counter, Crown Emergency Powers
Mode: BG | Temporal: MID (S8–S15)
Tracks: PI, Löwenritter Coup Counter, TC | Factions: Crown, Löwenritter, Church
NPCs: Ehrenwall, Almud | Archetypes: Institutional collapse
```

**Setup:** PI starts 7. Löwenritter Coup Counter starts 0.

**PI degradation sources:**
- Crown Emergency Powers: −1
- Church territorial seizure (post-TC 75): −1 per seizure
- Löwenritter coup: −3 (instant)

**Coup Counter threshold:** 4 = coup eligible. Counter triggers from: [GAP: Coup Counter increment triggers not in params read — need to read the Löwenritter faction mechanics.]

**Tractable cascade analysis (known triggers):**

**Scenario: TC reaches 75 by S20, Church seizes 3 territories in S21–S23:**
- Each seizure: PI −1. Three seizures: PI 7 → 4.
- PI 4 = "Degraded" (Parliamentary Manoeuvre +1 Ob, Crown Decree Ob reduced to 1).
- Crown responds with Emergency Powers (2× uses): PI 4 → 2.
- PI ≤ 2 = "Non-functional." Hafenmark loses Parliamentary Manoeuvre. Crown governs by decree. **TC +2** (new TC source from PI collapse).
- TC +2 adds to already-frozen TC? [GAP: PI ≤ 2 gives TC +2, but TC is frozen at 75 once Church reaches that threshold. Does TC +2 fire anyway? If TC is frozen, this TC+2 has no effect — or does it mean PI collapse bypasses the freeze?]

**If TC +2 bypasses the freeze:** Church at TC 77+ has an unsimulated state. The TC effects table caps at "75+" — no entry for TC > 75. **[FINDING P1 — TC 75 freeze + PI collapse TC +2 interaction undefined. Does PI ≤ 2 TC bonus apply when TC is already frozen? If it stacks: creates a TC value above 75 with no defined effect. If it doesn't apply: PI collapse has no TC consequence (which may understate institutional collapse severity).]**

**Löwenritter entry window:** PI 3–4 is the destabilized-but-functional zone where Löwenritter could plausibly win support (Mandate growing, Crown weakened). If PI drops to 2 before Löwenritter acts, PI recovery is nearly impossible (Hafenmark lost Parliamentary Manoeuvre, Crown Decree governs). **Coup window: PI 3–4 before Non-functional state.**

**FINDING P2 — Löwenritter has a narrow 1–2 season coup window at PI 3–4:** Once PI hits 2 (Non-functional), Crown governs by decree — which may paradoxically stabilize Crown military capacity (Decree Ob reduced to 1) even as institutional legitimacy collapses. Coup becomes harder, not easier, post-PI 2. Löwenritter must act during PI 3–4.

---

### SIM-BG-05 — RS Passive Decay: Time to Rupture Without Warden Cooperation

```
Test ID: SIM-BG-05
Mechanics: RS decay, Warden Cooperation effects, Thread Debt, Year-End accounting
Mode: BG | Temporal: FUT
Tracks: RS | Factions: All | NPCs: Generic
Archetypes: Passive/negligent play
```

**RS starts:** 72. RS = 0 = Rupture (shared loss).

**RS decay sources:**
- Year-End (Winter, every 4th season): RS −1 baseline
- Thread Debt > 1 season old: RS −1 per token
- Southernmost Surge (one-time, RS ≤ 10): one-band-worse for one season

**RS recovery:**
- WC 3: RS +2/season at Accounting
- No other passive recovery mechanic in params

**Minimum decay (no Thread Debt, WC = 0):** −1 per year = −1 per 4 seasons.
RS 72 → 0 = 72 seasons of pure Year-End decay alone = **72 years of game time** — negligible threat.

**Realistic decay (moderate Thread Debt, 1 debt token/year, WC = 0):**
- Year-End: −1/year
- Thread Debt: assume 1 token aging out per year = RS −1/year additional
- Total: −2/year
- 72÷2 = **36 years** — still extremely slow.

**Aggressive Thread use (3 debt tokens aging per year):**
- −1 (Year-End) + −3 (Debt) = −4/year
- 72÷4 = **18 years** (~72 seasons) — long-game threat

**FINDING P2 — RS rupture is not a credible early/mid-game threat under passive conditions:** RS decay is too slow to matter without sustained, heavy Thread Debt. However: the Southernmost/Askeheim mechanic (BALANCE-004) creates an RS incentive outside of Debt. Without WC engagement, RS drifts downward at −1/year minimum. In a 25–30 season game, RS reaches ~45–50 without intervention — well above Rupture but entering the RS 59–40 band where non-Thread Ob penalties (+2 Ob) begin. **The real threat is not Rupture but RS entering the 59–40 band mid-game and applying +2 Ob to all non-Thread actions, creating a systemic Ob penalty across all factions.** This is a meaningful consequence of neglecting Askeheim.

**RS 40 band entry time (no WC, 2 debt tokens/year):**
- Decay: −3/year. RS 72 → RS 40 = 32÷3 ≈ **10–11 years (40–44 seasons).**
- At S20 (5 years): RS ≈ 57 — approaching the 59 threshold but not yet there.
- **+2 Ob to all non-Thread orders fires around S40–S44 in a neglected game.** This is within a long-game campaign's arc.

---

## HYBRID MODE

---

### SIM-HY-01 — Domain Echo Stacking: Same-Scene Multiple Echoes

```
Test ID: SIM-HY-01
Mechanics: Domain Echo rules, cap ±2 per scene, timing
Mode: Hybrid | Temporal: CROSS
Tracks: Faction Mandate, Influence | Factions: Crown, Church
NPCs: Almud, Himlensendt | Archetypes: Politician, Churchman
```

**Rules (params_scale_transitions.md):**
- Domain Echo: +1 per degree above Partial (Success = +1, Overwhelming = +2)
- Cap: ±2 per scene [PROVISIONAL — ED-071]
- Multiple echoes in same scene: fire in occurrence order; cap resets per stat per Echo (not per scene total)
- Hybrid timing: queues; fires at next BG Seasonal Accounting

**Scenario: One scene with 3 Domain Echo triggers:**
1. Almud political speech (Overwhelming) → Crown Mandate +2
2. Himlensendt rebuttal (Success) → Church Mandate +1
3. Almud follow-up threat (Success, social scope) → Crown Influence +1

**Question: Does the ±2 cap apply per stat per echo, or per stat across all echoes in the scene?**

Current rule text: "cap resets per stat per Echo." This means:
- Echo 1: Crown Mandate +2 (cap = ±2 for this echo, cap met, no spillover)
- Echo 2: Church Mandate +1 (different stat, different faction — cap applies to Church separately)
- Echo 3: Crown Influence +1 (different stat from Echo 1 — new cap, +1 applies)

**Result: All three echoes apply fully.** Crown Mandate +2, Crown Influence +1, Church Mandate +1 queued for Accounting.

**FINDING P1 — "Cap resets per stat per Echo" creates a loophole:** A single scene with 3+ Overwhelming Domain Echoes targeting the same stat from different sources could stack: Echo 1 applies +2 to Crown Mandate, Echo 3 also applies +2 to Crown Mandate (new echo, new cap). Total: +4 Crown Mandate in one scene, from stat floor 5 to 7 (ceiling). This breaks the ±2 cap's intent.

**Example exploit:** Scene where Almud wins 2 debates (both Overwhelming) and a Crown Senator succeeds on an outreach action (also Overwhelming):
- Echo 1: Crown Mandate +2 (cap met for this echo)
- Echo 2: Crown Mandate +2 (cap resets for new echo)
- Echo 3: Crown Influence +2
- Net: Crown Mandate from 5 → 7 (ceiling) in one scene. **This is excessive and likely unintended.**

**Resolution needed:** Either (a) the ±2 cap applies per stat per scene total (not per echo), or (b) the cap resets per echo is intentional and the scene cap is not what prevents stacking. **[EDITORIAL: ED-071 must resolve this before Hybrid is playable. The provisional rule is ambiguous and exploitable.]**

---

### SIM-HY-02 — Zoom In at Illegal Phase Entry

```
Test ID: SIM-HY-02
Mechanics: Phase-Lock Protocol, Zoom In legal entry points
Mode: Hybrid | Temporal: PRES
Tracks: Phase state | Factions: Any | NPCs: Generic | Archetypes: Any
```

**Legal Zoom In entry points (PP-103):** After Phase 1, After Phase 3, After Phase 6 Step 1.

**Test: What happens if a player attempts Zoom In mid-Phase 2 (during Volley resolution)?**

No rule exists in params for handling illegal Zoom In attempts. The Phase-Lock Protocol defines legal entry but not the consequence of violation.

**FINDING P2 — No rule for illegal Zoom In attempt resolution:** The game has no defined consequence for an attempted Zoom In at an illegal phase. Options are: (a) attempt rejected — continue from current phase; (b) attempt queues to next legal entry point automatically; (c) GM discretion. Without a rule, GMs will rule inconsistently. **[EDITORIAL: ED-073 (non-battle Zoom In) is related; this also covers battle Zoom In violations. Needs one-line ruling.]**

**Additional edge case:** Zoom In entry After Phase 6 Step 1 — Steps 2–6 of Phase 6 are pending. The rule states "Phase 6 continuation: Steps 2–6 resolve after Zoom Out using updated state (PP-110)." But if the personal scene generates Domain Echoes affecting unit Discipline or Morale, do those echoes apply retroactively to Steps 2–6? **[GAP: Domain Echo affecting mass combat stats during a mid-Phase-6 Zoom In — resolution order undefined.]**

---

### SIM-HY-03 — Scope Shift Inspiration Cost

```
Test ID: SIM-HY-03
Mechanics: Scope shift rules, Inspiration spend
Mode: Hybrid | Temporal: PRES
Tracks: Inspiration | Factions: Any | NPCs: Generic | Archetypes: Any
```

**Rule:** Scope shift — once per round, declared at turn start, no roll. Second scope action in same round: +1 Inspiration spend.

**Test: Three scope shifts in one round.**
- Shift 1: free (once per round allowance)
- Shift 2: +1 Inspiration spend
- Shift 3: +1 Inspiration spend (additional)

**Cumulative cost for 3 shifts:** 0 + 1 + 1 = 2 Inspiration. Linear cost, no exponential.

**Test: Can a faction with 3+ Inspiration sustain multi-scope play indefinitely?**
Inspiration sources not confirmed in params read — [GAP: Inspiration generation rate not in read params]. If Inspiration generates ≥ 2/season, triple-scope play is effectively free. If Inspiration is scarce (≤ 1/season), triple-scope is a luxury.

**FINDING CLEAN:** The mechanic is internally coherent. Linear Inspiration cost for extra scope shifts is a well-designed pressure valve. The system works correctly provided Inspiration is balanced (existing BALANCE-NNN for Inspiration not found — flag for future sim if Inspiration generation rate is established).

---

## MASS COMBAT

---

### SIM-MC-01 — Command Cap Degenerate: Size 7 Command 2

```
Test ID: SIM-MC-01
Mechanics: Pool formula, Command cap, H calculation
Mode: TTRPG/BG | Temporal: PRES
Tracks: Unit Health, Discipline | Factions: Generic | NPCs: Generic General
Archetypes: Levy horde with poor leadership
```

**Unit stats:** Size 7, Command 2, Discipline 3, Power 1 (Levy), DR 0

**Formula application:**
- Pool = min(Size, Command) + Command = min(7,2) + 2 = **4D**
- H = min(Discipline, Command) + DR = min(3,2) + 0 = **2**
- Total Health = Size × H = 7 × 2 = **14**
- Damage/success = 1 + Power = 1 + 1 = **2**

**Opponent: Size 3, Command 3, Discipline 4, Power 3 (Professional), DR 2**
- Pool = min(3,3) + 3 = **6D**
- H = min(4,3) + 2 = **5**
- Total Health = 3 × 5 = **15**
- Damage/success = 4

**Round 1 (both 4D pool at E[net] ≈ 1.3, 6D at E[net] ≈ 2.0):**

Size 7 Command 2 unit: 4D → E[net] = 1.32 → E[damage] = 1.32 × 2 = **2.64**
Size 3 Professional: 6D → E[net] = 2.0 → E[damage] = 2.0 × 4 = **8.0**

After Round 1 (simultaneous):
- Horde: Health 14 − 8.0 = 6.0 → Size = ⌊6.0÷2⌋ = **3**
- Professional: Health 15 − 2.64 = 12.36 → Size = ⌊12.36÷5⌋ = **2**

**Round 2:** Horde still Size 3, but Command 2 → Pool unchanged at 4D (Size now ≤ Command cap). Professional now Size 2:
- Professional Pool = min(2,3) + 3 = **5D** → E[net] = 1.65 → E[damage] = 6.6
- Horde Pool = 4D → E[net] = 1.32 → E[damage] = 2.64

After Round 2:
- Horde: Health 6.0 − 6.6 = −0.6 → destroyed (Size 0)
- Professional: Health 12.36 − 2.64 = 9.72 → Size = ⌊9.72÷5⌋ = **1**

**FINDING P1 — Size 7 horde with Command 2 loses decisively to Size 3 professional unit:** The Command cap converts a 7:3 numerical advantage into a 4D:6D dice disadvantage. The horde deals only ~2.6 damage/round while absorbing ~8.0. This is mechanically coherent (bad leadership = poor unit), but produces a counterintuitive result: a 7-unit horde cannot defeat a 3-unit elite. The issue is whether this extreme is intended. At Size 7 Command 2, the horde is literally worse than a Size 2 Command 5 unit (7D vs 4D). **The Command cap means there is no benefit to fielding a Size > Command horde beyond total Health (survivability only, no offensive improvement).** This could create a valid "meat shield" role, but players fielding large levies likely expect offensive contribution — which is absent. **[EDITORIAL: should large low-Command units receive a secondary "weight of numbers" mechanic, e.g. bonus Morale check Ob for opponents, rather than direct damage contribution? Flag as ED-candidate.]**

---

### SIM-MC-02 — Heavy Infantry vs Light Infantry: Asymmetric Engagement

```
Test ID: SIM-MC-02
Mechanics: Unit combat formula, DR, Power, Discipline
Mode: TTRPG | Temporal: PRES
Tracks: Unit Health, Size | Factions: Generic | NPCs: Generic commanders
Archetypes: Matched force engagement
```

**Heavy Infantry (HI):** Size 5, Command 5, Discipline 5, Power 3, DR 2
- Pool = 10D | H = 7 | Total Health = 35 | Damage/success = 4

**Light Infantry (LI):** Size 5, Command 4, Discipline 3, Power 1, DR 0
- Pool = min(5,4)+4 = 9D | H = min(3,4)+0 = 3 | Total Health = 15 | Damage/success = 2

**Round 1 (E[net] at TN7: 10D≈3.3, 9D≈3.0):**
- HI deals: 3.3 × 4 = **13.2 damage**
- LI deals: 3.0 × 2 = **6.0 damage**

After Round 1:
- LI: Health 15 − 13.2 = 1.8 → Size = ⌊1.8÷3⌋ = **0 — destroyed**
- HI: Health 35 − 6.0 = 29 → Size = ⌊29÷7⌋ = **4**

**Light Infantry is destroyed in one round.** HI loses 1 Size.

**Test with equal Size 10 LI vs Size 5 HI:**

LI (Size 10): Pool = min(10,4)+4 = 8D, Total Health = 30
HI (Size 5): Pool = 10D, Total Health = 35

Round 1:
- LI: 8D → E[net] = 2.6 → damage = 5.2
- HI: 10D → E[net] = 3.3 → damage = 13.2

After:
- LI: 30 − 13.2 = 16.8 → Size ⌊16.8÷3⌋ = **5**
- HI: 35 − 5.2 = 29.8 → Size ⌊29.8÷7⌋ = **4**

Round 2 (LI Size 5, capped at Command 4):
- LI: min(5,4)+4 = 8D → damage 5.2 (unchanged — Size above Command cap, so cap still applies)
- HI: min(4,5)+5 = 9D → E[net] = 3.0 → damage = 12.0

After:
- LI: Health 16.8 − 12.0 = 4.8 → Size ⌊4.8÷3⌋ = **1**
- HI: Health 29.8 − 5.2 = 24.6 → Size ⌊24.6÷7⌋ = **3**

Round 3 (LI Size 1, now ≤ Command 4):
- LI: min(1,4)+4 = 5D → E[net] = 1.65 → damage = 3.3
- HI: min(3,5)+5 = 8D → E[net] = 2.6 → damage = 10.4

After:
- LI: Health 4.8 − 10.4 = −5.6 → **destroyed**
- HI: Health 24.6 − 3.3 = 21.3 → Size ⌊21.3÷7⌋ = **3**

**Result:** HI (Size 5) defeats LI (Size 10) in 3 rounds, finishing at Size 3. LI started with 2× the soldiers.

**FINDING P2 — Heavy Infantry overwhelming vs Light Infantry; ratio breakeven unclear:** A 2:1 LI numerical advantage cannot overcome HI. The Power differential (4× damage per success vs 2×) combined with DR 2 (reducing LI damage) creates a near-insurmountable gap. **This may be correct simulation of historical Heavy vs Light Infantry dynamics, but creates a dominant-strategy problem: any faction that can afford Heavy Infantry should always prefer it.** Cost difference (Muster Ob 2 vs 1, Prosperity ≥ 5) is a gate, but once cleared, HI strictly dominates. Light Infantry appears to have no tactical role against HI except flanking (Morale penalty on flanked HI — but no simulation of flanking mechanics here). **[GAP: Flanking Morale penalty mechanics — do they exist? If not, Light Infantry has no counter to Heavy.]**

---

### SIM-MC-03 — Morale Cascade from General Death

```
Test ID: SIM-MC-03
Mechanics: Morale degradation, general death trigger, rout contagion
Mode: TTRPG | Temporal: PRES
Tracks: Morale, Size | Factions: Generic | NPCs: Generic General (killed)
Archetypes: Command disruption
```

**Starting state:** 3 units — Unit A (Morale 5), Unit B (Morale 4, adjacent to A), Unit C (Morale 4, adjacent to B). General present. Phase 5 Cascade.

**General killed during Phase 5 (personal combat result):**
- All units: Morale −2 (general killed, uncapped per rules)
- Unit A: Morale 5 → 3
- Unit B: Morale 4 → 2
- Unit C: Morale 4 → 2

**Phase 5 cap: −3 per Cascade phase** — general death is stated as "not subject to phase cap." So −2 applies fully.

**Also firing this Cascade:** Unit A took 50% Size loss (trigger: Size < 50% max → Morale −1):
- Unit A: Morale 3 → 2 (capped at −3 total this phase: −2 + −1 = −3, exactly at cap)

**Rout check:** Morale 0 = rout. All units at Morale 2+. No immediate rout.

**But Unit B and C are now at Morale 2 — one more trigger routs them:**
- If any adjacent unit routs next phase: Morale −1 (contagion). B and C would hit Morale 1 (still no rout).
- If B takes further losses next round: Morale −1 (50% loss) → Morale 1 → still no rout.
- If B also loses Discipline this turn (Size loss > Discipline → Discipline −1): another potential Morale −1 next cascade.

**Round 2 cascade with Unit A routing (if it hits 0):**
- Unit A Morale 2, takes another loss: Morale −1 → 1. Another loss same phase: −1 → 0 → **rout**.
- Unit B (adjacent): contagion −1 → Morale 1. Unit C (adjacent to B): contagion −1 → Morale 1.
- Both B and C at Morale 1, floor removed (general is dead — floor 1 requires general present). **Morale 1 is now the rout-adjacent state.**

**Round 3:** Any further Morale trigger on B or C → rout.

**FINDING P2 — General death initiates a 2–3 round cascade to full rout, not immediate:** The −2 Morale from general death is significant but not instantly decisive at Morale 4+. Units with starting Morale 3 or below route immediately on general death. Units at 4+ survive 1–2 more rounds before cascading. **This is good design — death is decisive but not instantaneous, preserving tactical space for a Rally attempt by a secondary commander.** However: the floor "Morale = 1 while general present" disappearing on general death creates an asymmetry. Units at Morale 1 (which might have been held there by the general's presence) instantly become rout-eligible. **[GAP: Does a secondary commander (Command 2+) inherit the Morale floor? Not stated in params.]**

---

## DEBATE

---

### SIM-DB-01 — CLASH Dominant Strategy: Revealing vs Obscuring

```
Test ID: SIM-DB-01
Mechanics: CLASH resolution, genre weights, orientation weights, movement formula
Mode: TTRPG/Hybrid | Temporal: PRES
Tracks: Conviction Track | Factions: Crown vs Hafenmark | NPCs: Almud, Baralta
Archetypes: Politician (both sides)
```

**Orientation weights:** Revealing ×1.0 | Obscuring ×0.75

**CLASH: same genre, opposite orientations.** Movement = ⌊(margin × genre_weight × orientation_weight) − resistance⌋

**Which orientation wins a CLASH?**

In a CLASH, one side is Revealing, one is Obscuring (opposite orientations). The winner of the pool roll applies their orientation weight to movement.

**Scenario A: Almud (Revealing) wins CLASH by margin 2, Primary genre (×1.0), Crown audience (Present boosted: ×1.0+0.5 = effectively 1.5? No — boosted genre weight ×1.5 applies to the audience's primary genre, not the winner's genre.**

**Re-reading genre weight system:**
- Primary genre (audience's boosted genre): ×1.0 + 0.5 = ×1.5 effectively? No — table says: "Primary genre: ×1.0. Other two genres: ×0.5 base. One genre boosted +0.5 by audience ethical mode."
- So boosted genre = 1.0 + 0.5 = 1.5 max. Non-boosted primary = 1.0. Non-primary = 0.5.

**Crown audience (Virtue Ethics → Present boosted):**
| Genre | Weight |
|-------|--------|
| Present | 1.5 |
| Past | 0.5 |
| Future | 0.5 |

**CLASH: Almud chooses Present Revealing, Baralta chooses Present Obscuring.**
- Winner determined by pool comparison.
- If Almud wins by margin 2: movement = ⌊(2 × 1.5 × 1.0) − resistance⌋ = ⌊3.0 − resistance⌋
  - Resistance (Crown Hafenmark audience, Stability 4): ceil(4/4) = 1. Movement = ⌊3.0−1⌋ = **2 toward Almud**
- If Baralta wins by margin 2: movement = ⌊(2 × 1.5 × 0.75) − 1⌋ = ⌊2.25−1⌋ = ⌊1.25⌋ = **1 toward Baralta**

**Revealing generates 2× the Conviction Track movement of Obscuring at the same margin and primary genre.**

**Is Revealing always dominant?**

**FINDING P2 — Revealing orientation strictly dominates Obscuring in CLASH:** At equivalent margin, Revealing always generates more Conviction Track movement. The only rationale for Obscuring is:
1. Misdirection: if the opponent reads your genre correctly (Step 1 Appraise) and you want to deny the primary genre weight
2. Forced: if the mechanic requires opposite orientations for CLASH and you're assigned Obscuring

But in Choose step, players select their own orientation. If Revealing always wins CLASH more efficiently, rational players should always choose Revealing. This creates a dominant strategy where Obscuring is never voluntarily chosen in CLASH.

**Obscuring is only rational if:** it produces a DIVERGE or CROSS state rather than CLASH, which might be tactically preferable. But in a CLASH (same genre, opposite orientation — one side chose Revealing, the other Obscuring), someone is choosing Obscuring when they could have chosen Revealing. **Why would any player choose Obscuring if they know their opponent will choose Revealing?**

**Possible resolution: Obscuring in CROSS/AMPLIFY has tactical value.** In CROSS (different genres), each side is evaluated independently — orientation weight applies to movement for each independent evaluation. Obscuring's 0.75 weight reduces your opponent's CROSS movement against you, not your own. **[GAP: CROSS orientation weight application direction not confirmed — does each orator's orientation apply to their own movement or their opponent's defense?]**

**If Obscuring is only rational in CROSS, then CLASH always sees Revealing vs Revealing — no CLASH ever fires?** If both players choose Revealing, interaction type = same genre same orientation = AMPLIFY, not CLASH. **CLASH requires opposite orientations, meaning one player must choose Obscuring.** In competitive play, the player who ends up Obscuring is at a systematic disadvantage. **This is a structural imbalance in CLASH.**

---

### SIM-DB-02 — AMPLIFY vs High-Resistance Audience: Stalemate Detection

```
Test ID: SIM-DB-02
Mechanics: AMPLIFY, resistance, Conviction Track movement
Mode: TTRPG | Temporal: PRES
Tracks: Conviction Track, Composure | Factions: Church + Crown vs Hafenmark
NPCs: Himlensendt + Almud vs Baralta | Archetypes: Alliance debate
```

**AMPLIFY: same genre, same orientation. Combined pools vs Conviction Track resistance.**
Combined pool = Pool A + Pool B. Roll combined vs Ob 2 (base — [GAP: AMPLIFY Ob not confirmed. CLASH uses "Compare successes." AMPLIFY uses "Combined pools vs Conviction Track resistance." — the resistance IS the Ob?]).

**Reading the rule:** AMPLIFY → "Combined pools vs Conviction Track resistance." Resistance = ceil(Stability/4).

**Himlensendt (Church, Cognition 4, History 2):** Argue pool = (4×2)+2 = 10D
**Almud (Crown, Cognition 5, History 3):** Argue pool = (5×2)+3 = 13D
**Combined: 23D TN7**

**E[net] from 23D at TN7 = 23 × 0.33 = 7.6 net successes**

**Hafenmark audience (Categorical Imperative → Past boosted). Stability 4 → resistance = ceil(4/4) = 1.**

**AMPLIFY movement formula:** ⌊(net_successes × genre_weight × orientation_weight) − resistance⌋

Allied orators choose Past Revealing (Past = boosted for Hafenmark audience = ×1.5):
Movement = ⌊(7.6 × 1.5 × 1.0) − 1⌋ = ⌊11.4 − 1⌋ = ⌊10.4⌋ = **10 toward allied position**

Conviction Track is 0–10. If starting at neutral (5), one AMPLIFY from 23D pool combination moves it from 5 → **15 — far beyond the 10 ceiling.**

**Track ceiling = 10. Winner at ≥7. Starting neutral (5): AMPLIFY needs to move 2+ to win.**

**This 23D combined pool AMPLIFY wins in one exchange, at any starting position ≤ 3.**

**Stalemate condition check:**

**Scenario: Low-pool AMPLIFY vs high resistance.**
Almud alone (13D) + Baralta's ally (Cognition 3, History 1 = 7D) combined: 20D.
Guilds audience (Moral Relativism, GM picks boosted genre = GM picks Future): Stability 5 → resistance = ceil(5/4) = 2.

**Movement: ⌊(20 × 0.33 × [let's say non-boosted genre 0.5] × 1.0) − 2⌋ = ⌊3.3 − 2⌋ = ⌊1.3⌋ = 1**

One exchange moves track by 1. Conviction needs to move from 5 to 7 = 2 moves = **2 exchanges minimum.**

**Stalemate detection: minimum pool for movement?**
Movement > 0 requires: net × genre_weight × orientation_weight > resistance.
With resistance = 2, genre 0.5, Revealing 1.0: net must be > 4. E[net] ≈ 4 requires ~12D.
**Pool below 12D targeting a non-primary genre vs resistance 2 produces 0 movement.**

**FINDING P1 — AMPLIFY stalemate at low pool + non-primary genre:** A debate where both sides have pools below ~12D and target non-primary genres vs a resistance-2 audience produces **zero Conviction Track movement every exchange.** The debate cannot resolve. It terminates only via Composure depletion — but if both sides are using AMPLIFY (same genre, same orientation), no Composure damage rule is defined for AMPLIFY. **[GAP: Does AMPLIFY deal Composure damage? The rule only defines Conviction Track movement for AMPLIFY, not Composure damage. If AMPLIFY deals no Composure damage and produces no Track movement at low pools, the debate is a genuine stalemate with no resolution path.]**

This is a P1 structural gap. AMPLIFY needs either: (a) a minimum movement rule (at least 1 if any successes), or (b) Composure damage on AMPLIFY to provide a secondary resolution path.

---

### SIM-DB-03 — Composure Bleed Rate: Median Pool Concession Threshold

```
Test ID: SIM-DB-03
Mechanics: Composure, Conviction Track, CLASH margin → Composure
Mode: TTRPG | Temporal: PRES
Tracks: Composure, Conviction Track | Factions: Crown vs Varfell
NPCs: Almud vs Vaynard | Archetypes: Politician vs Epistemic Reasoner
```

**[GAP: Composure formula not established — ED-127 open. Composure track and wound-equivalent threshold design pending. Cannot run full Composure bleed sim without this formula. Partial sim only.]**

**Tractable analysis: Pool comparison (Almud vs Vaynard)**

Almud (Crown, Cognition 5, History 3): Pool = 13D
Vaynard (Varfell, Cognition 4, History 2): Pool = 10D

**Exchange 1: CLASH, Present genre (Crown boosted), Almud Revealing:**
Almud: 13D TN7. E[net] = 4.3
Vaynard: 10D TN7. E[net] = 3.3

E[margin] = 4.3 − 3.3 = 1.0 net successes in Almud's favor.

Movement (Crown audience, Stability 4, resistance 1, Present ×1.5, Revealing ×1.0):
= ⌊(1.0 × 1.5 × 1.0) − 1⌋ = ⌊0.5⌋ = **0**

**No movement despite Almud winning the exchange.** Margin of 1 fails to clear resistance.

**For movement to occur:** margin must exceed 1.0/1.5 = 0.67, then produce ≥ 1 net after resistance.
Minimum margin for movement = ceil(resistance / (genre × orientation)) = ceil(1/1.5) = 1 → margin ≥ 1.

But the formula is ⌊(margin × 1.5 × 1.0) − 1⌋. For margin = 1: ⌊1.5 − 1⌋ = ⌊0.5⌋ = 0.
For margin = 2: ⌊3.0 − 1⌋ = 2. So minimum moving margin = **2**, not 1.

**P(Almud margin ≥ 2):** Pool difference is 3D. P(13D net ≥ 10D net + 2):
Approximately P(13D − 10D ≥ 2) = P(3D pool advantage generates 2+ net): ~40%.

**Expected exchanges to move track from 5 to 7 (need 2 movement):**
- P(move 2+ per exchange) ≈ 40% → E[exchanges] = 1/0.4 = **2.5 exchanges**
- But movement is 0 on 60% of exchanges. On successful exchanges, E[movement] ≈ 2.
- E[exchanges] to reach track = 7: 2÷2 = **1 successful exchange** of movement ≈ **2.5 total exchanges**

**Debate duration at 13D vs 10D: 2–4 exchanges before Almud wins via Conviction Track.**

**FINDING CLEAN:** At the 13D vs 10D matchup, the debate resolves in 2–4 exchanges via Conviction Track movement. Not too fast (>3 rounds minimum at median), not too slow. Resistance = 1 acts as a meaningful friction mechanic that prevents single-margin victories from dominating. The debate system is calibrated correctly at this pool range. No finding.

---

## PERSONAL COMBAT

---

### SIM-PC-01 — Weapon TN Cliff: TN5 vs TN8 Comparative Analysis

```
Test ID: SIM-PC-01
Mechanics: Weapon TN matrix, hit probability, damage formula
Mode: TTRPG | Temporal: PRES
Tracks: Health | Factions: Generic | NPCs: Generic combatants
Archetypes: Duelist (both)
```

**Weapon TN range:** Short Light Blade (TN5) to Long Heavy Blunt (TN8). 3-point spread.

**Expected net successes per die at each TN:**
| TN | P(+2: roll 10) | P(+1: 7-9) | P(−1: roll 1) | E[per die] |
|----|----------------|------------|----------------|------------|
| 5 | 0.10 | 0.50 | 0.10 | +0.10×2 + 0.50×1 + 0.10×(−1) = 0.20+0.50−0.10 = **+0.60** |
| 6 | 0.10 | 0.40 | 0.10 | 0.20+0.40−0.10 = **+0.50** |
| 7 | 0.10 | 0.30 | 0.10 | 0.20+0.30−0.10 = **+0.40** |
| 8 | 0.10 | 0.20 | 0.10 | 0.20+0.20−0.10 = **+0.30** |

**Note:** TN 5 means faces 5–9 = success (5 faces), face 10 = +2, face 1 = −1, faces 2–4 = 0. Wait — the rule states "7–9 = +1 success, 10 = +2 successes, 1 = −1, 2–6 = 0." TN7 is the standard. When TN is modified, does the threshold shift?

**[GAP: Weapon TN modifier — does TN5 mean faces 5–9 = success, or does it mean faces 5–10 = success (i.e. the hit window expands)? The weapon table gives TN modifiers (−1, +0, +1) to "Hit TN = 7 + modifiers." If TN5 = hit on ≥5 (not ≥7), then 5-face success window instead of 3-face. This interpretation makes TN matter significantly.]**

**Assuming TN = minimum face for a success (standard d10 pool convention):**
| TN | Success faces | E[per die] |
|----|--------------|-----------|
| 5 | 5,6,7,8,9 (5 faces=+1, 10=+2, 1=−1) | 5×0.1 + 0.1×2 + 0.1×(−1) = 0.5+0.2−0.1 = **0.60** |
| 6 | 6,7,8,9 (4 faces=+1) | 4×0.1+0.2−0.1 = **0.50** |
| 7 | 7,8,9 (3 faces=+1) | 3×0.1+0.2−0.1 = **0.40** |
| 8 | 8,9 (2 faces=+1) | 2×0.1+0.2−0.1 = **0.30** |

**At 8D combat pool:**
| TN | E[net successes] |
|----|----------------|
| 5 | 8 × 0.60 = **4.8** |
| 6 | 8 × 0.50 = **4.0** |
| 7 | 8 × 0.40 = **3.2** |
| 8 | 8 × 0.30 = **2.4** |

**Vs Ob 2 (typical defence allocation 4D vs 4D offence):**
- Defender 4D TN7 → E[net defence] = 4 × 0.40 = 1.6
- Attacker net hits after defence = E[offence] − E[defence] = TN-dependent

| Attacker TN | E[offence net] | E[net hits after defence] |
|-------------|---------------|--------------------------|
| 5 | 4.8 | 4.8 − 1.6 = **3.2** |
| 7 | 3.2 | 3.2 − 1.6 = **1.6** |
| 8 | 2.4 | 2.4 − 1.6 = **0.8** |

**Damage at net hits:**
Short Light Blade (TN5): modifier vs no armour = +3. Total damage = 0.8 (net) + STR + 3 ≈ well, this needs full context. Let's use STR 3 (mid-range character).
- TN5 weapon: E[damage] = (3.2 net) + 3(STR) + 3(modifier vs None) = **9.2/round**
- TN8 weapon: E[damage] = (0.8 net) + 3(STR) + 5(Heavy Blunt vs None) = **8.8/round**

**Damage is nearly equal despite 3-point TN difference,** because Light Blade's +3 hits generate more damage than Heavy Blunt's +5 once expected hits are factored in. The weapon system is better balanced than the raw TN spread suggests.

**FINDING P2 — TN5 (Short Light Blade) is not decisively superior to TN8 (Long Heavy Blunt) in expected damage:** The damage modifiers partially compensate for hit probability differences. However: Critical Hit (net hits ≥ 3) probability is dramatically different — TN5 hits ≥ 3 much more frequently.

P(net offence ≥ 3 before defence) at 8D:
- TN5: P(net ≥ 3) ≈ 97%
- TN7: P(net ≥ 3) ≈ 73%
- TN8: P(net ≥ 3) ≈ 50%

TN5 achieves Critical Hit (net ≥ 3) nearly every round; TN8 achieves it half the time. Critical doubles the weapon modifier before armour reduction. **Critical Hit frequency gives Short Light Blade a consistent advantage over Long Heavy Blunt against unarmoured targets.** Against heavy armour, the relationship reverses — Heavy Blunt doubles +5 modifier vs heavy on a crit = +10 before DR, while Light Blade doubles +0 = no crit benefit. **Weapon choice is therefore armour-contextual: TN5 vs unarmoured, TN8+ vs heavy. This is good design.**

---

### SIM-PC-02 — Initiative Information Value

```
Test ID: SIM-PC-02
Mechanics: Initiative, declaration order, Attunement
Mode: TTRPG | Temporal: PRES
Tracks: Stamina/Health | Factions: Generic | NPCs: Generic
Archetypes: Duelist (Attunement advantage vs disadvantage)
```

**Declaration order:** Lower initiative declares split first. Higher initiative sees split, then declares own.

**Scenario: Attacker A (higher Attunement, higher initiative) vs Defender B (lower initiative).**

B declares: 4D offence / 4D defence (8D total pool).
A sees this, declares: 5D defence / 3D offence — maximising defence against B's 4D offence.

**B's offence (4D TN7) vs A's defence (5D TN7):**
B E[net] = 4×0.4 = 1.6
A E[defence] = 5×0.4 = 2.0
Net hits for B = 1.6 − 2.0 = −0.4 → 0 (Failure)

**A's offence (3D TN7) vs B's defence (4D TN7):**
A E[net] = 3×0.4 = 1.2
B E[defence] = 4×0.4 = 1.6
Net hits for A = 1.2 − 1.6 = −0.4 → 0 (Failure)

**Round 1: mutual Failure.** Initiative information allows A to match B's offence with superior defence, nullifying B's attack. But A's attack also fails — A is too conservative.

**If A sees 4D offence and counters with only 3D defence + 5D offence:**
A offence 5D vs B defence 4D: A E[net] = 2.0 − 1.6 = 0.4 net → Partial
A defence 3D vs B offence 4D: B E[net] = 1.6 − 1.2 = 0.4 net → Partial

Both take partial hits. The information advantage enables strategic choices but doesn't produce decisive asymmetry at equal pool sizes.

**FINDING CLEAN — Initiative is a tactical modifier, not a decisive advantage:** Initiative information is valuable for pool allocation optimization but doesn't produce dramatic win-probability swings at similar pool sizes. The higher-initiative combatant gains ~15–20% efficiency in pool use. This is correctly calibrated — initiative matters but doesn't determine outcomes unilaterally.

---

### SIM-PC-03 — Wound Accumulation: Non-Functionality Threshold

```
Test ID: SIM-PC-03
Mechanics: Wound penalty (−1D per wound), Health threshold, pool floor
Mode: TTRPG | Temporal: PRES
Tracks: Health, Wounds | Factions: Generic | NPCs: Generic combatant
Archetypes: Sustained fighter
```

**Representative fighter:** Agility 4, Endurance 3, History 2.
- Combat Pool = (4×2) + 2 + 3 = **13D**
- Stamina = 3 + 2 + 1 = 6 (no armour)
- Health = (3+6) × (wound_count + 1) = 9 × (wounds + 1)
- Wound threshold: every 9 Health points

**Pool floor = 5 (PP-232: minimum 5).**

**Wounds vs effective pool:**
| Wounds | Pool (13 − wounds, floor 5) | E[net at TN7] |
|--------|----------------------------|--------------|
| 0 | 13D | 5.2 |
| 1 | 12D | 4.8 |
| 2 | 11D | 4.4 |
| 3 | 10D | 4.0 |
| 4 | 9D | 3.6 |
| 5 | 8D | 3.2 |
| 6 | 7D | 2.8 |
| 7 | 6D | 2.4 |
| 8 | 5D (floor) | 2.0 |
| 8+ | 5D (floor — no further reduction) | 2.0 |

**Non-functionality = pool ≤ 5D (floor reached):** at 8 wounds.

**But Health at 8 wounds:** H = 9 × (8+1) = 81. A fighter must absorb 81 Health damage to reach 8 wounds. At typical E[net hits] ≈ 2 per exchange and moderate weapon damage (say 4 damage/hit): ~2×4 = 8 damage/round → **10 rounds to 8 wounds.** This is far too long.

**More realistic scenario:** fighter takes 2 wounds in a heavy exchange. Pool: 13 − 2 = 11D. Still highly functional (E[net] 4.4 vs 3.2 for 8D uninjured baseline). The −1D/wound penalty is noticeable but not crippling until 5+ wounds.

**FINDING P2 — Pool floor of 5 means any fighter remains tactically viable regardless of wound accumulation beyond 8:** A character with 13 wounds (if they survive that long) rolls the same 5D as a character with 8. The floor prevents wound accumulation from being punishing enough to force retreat at high wound counts. **The more impactful limiter is likely Health exhaustion (reaching the wound threshold) rather than pool reduction.** A fighter with H = 9 is taken out at ~5 wounds by an opponent dealing ~9 damage/wound-threshold (9 Health per threshold × 5 = 45 Health at Endurance 3 = incapacitation). At 2 damage hits/round and 4 damage/hit = 8 damage/round → ~6 rounds to incapacitation. This is appropriate combat pacing.

**Edge case: Pool floor = 5 creates a viable "zombie fighter" condition:** At 13 wounds, the fighter rolls 5D — the same as a fresh fighter with a 5D pool. The zombie fighter has very little Health remaining but is fully dangerous offensively. This is potentially exploitable in long fights. **[EDITORIAL: ED-candidate — should wound penalties include an Ob increase at high wound counts (e.g. +1 Ob at 5+ wounds) to represent impaired judgment, not just impaired strength?]**

---

## SUMMARY: ALL FINDINGS

| ID | Severity | System | Issue |
|----|----------|--------|-------|
| SIM-BG-01 | P2 | BG | TC pace viable; Hafenmark suppression worth 6 seasons |
| SIM-BG-02 | **P1** | BG | Fort 3 + CV 0 = de facto seizure immunity; no mechanic to break |
| SIM-BG-03 | **P1** | BG | "Suppress all rivals" undefined; Crown victory unresolvable |
| SIM-BG-04 | **P1** | BG | PI ≤ 2 TC +2 interaction with frozen TC undefined |
| SIM-BG-05 | P2 | BG | RS 40 band entry ~S40–44; RS Rupture not a near-term threat |
| SIM-HY-01 | **P1** | Hybrid | Domain Echo cap resets per-echo creates +4 stat stacking exploit |
| SIM-HY-02 | P2 | Hybrid | Illegal Zoom In — no rule for rejection/queuing; Domain Echo mid-Phase-6 undefined |
| SIM-HY-03 | CLEAN | Hybrid | Scope shift Inspiration cost coherent |
| SIM-MC-01 | **P1** | Mass Combat | Size 7 Command 2 horde loses to Size 3 elite; no weight-of-numbers contribution |
| SIM-MC-02 | P2 | Mass Combat | HI dominates LI at 2:1 ratio; LI has no confirmed counter |
| SIM-MC-03 | P2 | Mass Combat | General death cascades over 2–3 rounds; secondary commander inheritance undefined |
| SIM-DB-01 | P2 | Debate | Revealing dominates Obscuring in CLASH; Obscuring rationale unclear |
| SIM-DB-02 | **P1** | Debate | AMPLIFY at low pool + non-primary genre = zero movement and zero Composure damage = irresolvable stalemate |
| SIM-DB-03 | CLEAN | Debate | Conviction Track movement at 13D vs 10D correctly calibrated |
| SIM-PC-01 | P2 | Combat | TN5 dominates unarmoured targets via Critical frequency; TN8 dominates armoured — correct design |
| SIM-PC-02 | CLEAN | Combat | Initiative is tactical modifier not decisive advantage |
| SIM-PC-03 | P2 | Combat | Pool floor 5 creates zombie fighter at 8+ wounds; Ob penalty at high wound counts may be needed |

**P1 count: 6** | **P2 count: 8** | **CLEAN: 3**

---

## GAPS DISCOVERED

| ID | Gap | Affects |
|----|-----|---------|
| GAP-BG-01 | "Suppress all rivals" definition absent | Crown victory |
| GAP-BG-02 | TCV per-territory values not in params | Crown TCV 18 analysis |
| GAP-BG-03 | TC +2 from PI ≤ 2 interaction with frozen TC | PI collapse chain |
| GAP-BG-04 | Schoenland and Askeheim TCV values | Victory analysis |
| GAP-HY-01 | Domain Echo cap: per-echo vs per-scene-total | ED-071 |
| GAP-HY-02 | Illegal Zoom In consequence rule absent | Phase-Lock Protocol |
| GAP-HY-03 | Domain Echo affecting mid-Phase-6 mass combat stats | Hybrid/Mass cascade |
| GAP-MC-01 | Flanking Morale penalty — does it exist? | LI counter-tactics |
| GAP-MC-02 | Secondary commander inheriting Morale floor | General death cascade |
| GAP-DB-01 | AMPLIFY Ob structure — is resistance the Ob? | AMPLIFY resolution |
| GAP-DB-02 | AMPLIFY Composure damage rule absent | Stalemate detection |
| GAP-DB-03 | CROSS orientation weight application direction | Obscuring rationale |
| GAP-PC-01 | TN modifier convention — threshold shift or fixed? | Weapon TN analysis |
| GAP-PC-02 | Inspiration generation rate not in params | Scope shift sustainability |

---

## EDITORIAL CANDIDATES (new)

| Flag | Issue | Priority |
|------|-------|----------|
| ED-candidate-A | "Suppress all rivals" requires definition for Crown victory | P1-BLOCKER candidate |
| ED-candidate-B | PI ≤ 2 TC +2 interaction with frozen TC — rule needed | P1 |
| ED-candidate-C | Domain Echo cap: per-echo vs per-scene-total (resolve ED-071) | P1 |
| ED-candidate-D | Illegal Zoom In consequence — one-line ruling needed | P2 |
| ED-candidate-E | Weight-of-numbers: large low-Command units offensive contribution | P2 |
| ED-candidate-F | Wound penalty Ob increase at 5+ wounds for "zombie fighter" | P2 |
| ED-candidate-G | Church pre-seizure softening mechanic (Assert raising CV in adjacent territory) | P2 |
| ED-candidate-H | AMPLIFY Composure damage rule needed (stalemate resolution path) | P1 |

---

*Committed per Mode I protocol. Tests/coverage_matrix.md update required before this report is complete.*
