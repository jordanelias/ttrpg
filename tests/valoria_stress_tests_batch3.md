# VALORIA STRESS TESTS — BATCH 3
*Model: Sonnet 4.6 · Mode references: A=Isolation, B=Interaction, C=Full Scenario, D=Edge Case*
*Source: CP14 (canonical). Probability engine: TN7 d10 pool, net ≈ N×0.33 expected successes.*

---

## PREFLIGHT: P1 REPAIR LOG

### BUG-001 · Attribute Point Contradiction (P1)

| Location | Text | Correct |
|---|---|---|
| §2.2 (stage1_core_engine) | "31 points" | ✅ CORRECT |
| §12.1 Session Zero (stage12_campaign_modes) | "18 attribute points" | ❌ WRONG |
| §14.7 GM Checklist (stage14_gm_tools, line 15) | "18 attribute points" | ❌ WRONG |

**Fix required:** Replace "18 attribute points" with "31 points" in §12.1 and §14.7.

### BUG-002 · Thread Pool Attributes — Stage File vs CP14 Mismatch (P1)

Stage compilation files (stage3_thread_operations.md) use obsolete attribute names:
- Leap: "Cognition + Heart" → CP14: "Attunement + TPS"
- Weaving: "Cognition + Memory" → CP14: "Spirit + TPS"
- Pulling: "Cognition + Attunement" → CP14: "Spirit + TPS"
- Contact duration: "Heart score" → CP14: "Focus score"
- Composure glossary: "Poise + Heart" → CP14 main text: "Presence + 6"

"Heart" and "Poise" are not in the 10-attribute list (§2.1). Stage3 file is out of sync with CP14.
**Fix required:** Stage3 compilation file must be updated to match CP14. Character sheet note (§16.2) reads "confirm at final pass" — this must be resolved before CP15.

**Design Note:** Stage6 Domain Ob spec = stat ÷ 2 (round up). CP14 Domain Ob spec = direct stat value (1–7). CP14 is canonical. Stage6 must be updated.

---

## COVERAGE MATRIX

| Test ID | Mechanic(s) | Mode | Temporal | Tracks | Factions | NPCs | Archetypes | Status |
|---|---|---|---|---|---|---|---|---|
| BT3-01 | TPS scaling (all Thread ops) | A | PRES | TT, TS | Varfell | Vaynard | Practitioner | Complete |
| BT3-02 | Co-movement d10 | A+D | CROSS | TT, TS, CERT | Crown | Almud | Practitioner | Complete |
| BT3-03 | Knot/Call + Intelligibility strain | B | PRES/CROSS | TS, TD, CERT | Revolution | Maret Uln | Practitioner |Complete |
| BT3-04 | Rattled stacking + Composure reset | A | PRES | COMP | Church | Himlensendt | Devout |Complete |
| BT3-05 | Domain Ob + leadership pool | B | PRES | FSTAT | Hafenmark/Crown | Baralta | Faction Leader | Complete |
| BT3-06 | Renown × Debate interaction | B | PRES | CERT | Crown/Church | Almud/Himlensendt | Faction Leader | Complete |
| BT3-07 | Vaynard Ambition Track | A | FUT | FSTAT | Varfell | Vaynard | Faction Leader | Complete |
| BT3-08 | Niflhel Supremacy Mechanic | A+endgame | PRES/FUT | FSTAT | Niflhel | — | Faction Leader | Complete |
| BT3-09 | TC pause at Stability ≤ 4 | C | PRES/FUT | TC, FSTAT | Church/Crown | Himlensendt/Baralta | Faction Leader | Complete |
| BT3-10 | Seasonal Events S-16–S-20 | C | CROSS | TT, TC, IP, FSTAT | All | Multiple | Multiple | Complete |

---

## BT3-01 · TPS SCALING ACROSS ALL THREAD OPERATIONS

**Mode A — Isolation**
**Mechanic:** TPS = TS ÷ 10 (round down). Added to Leap, Weaving, Pulling, Locking/Snapping pools.
**Scenario:** Generic Practitioner (Vaynard archetype), Attunement 3, Spirit 3, History "Einhir Scholar" 2 pts.

### Input Space

| Variable | Range | Typical | Edge |
|---|---|---|---|
| TS | 30–100 | 50 | 30 (floor) / 100 (max) |
| TPS | 3–10 | 5 | 3 (TS 30) / 10 (TS 100) |
| Base pool (Attunement + History bonus) | 3 + 5 = 8 | 8 | 8 (static) |
| Leap total pool | 11–18 | 13 | 11/18 |
| Weaving/Pulling total pool | 11–18 | 13 | 11/18 |
| Leap Ob | 1–2 | 2 (TS 30–49) / 1 (TS 50+) | 2+wounds |
| Weaving Ob (Object/Personal) | 1–2 | 2 | 1/5 |

### Probability Table — Leap (primary bottleneck)

| TS (TPS) | Pool | Ob | P(Success) | P(Partial) | P(Failure) | Expected Net |
|---|---|---|---|---|---|---|
| 30 (TPS 3) | 11D | 2 | ~82% | ~10% | ~8% | 3.6 |
| 50 (TPS 5) | 13D | 1 | ~99% | ~0.5% | ~0.5% | 4.3 |
| 70 (TPS 7) | 15D | 1 | ~99% | ~0% | ~0% | 5.0 |
| 100 (TPS 10) | 18D | 1 | ~99% | ~0% | ~0% | 5.9 |

*With 2 Wounds (Ob +2): TS 30 Leap Ob becomes 4. Pool 11D vs Ob 4: P(Success) ≈ 57%. Failure rate non-trivial.*

### Probability Table — Weaving (Object scale, Ob 1)

| TS (TPS) | Pool | Ob | P(Overwhelming) | P(Success) | P(Partial) | P(Failure) |
|---|---|---|---|---|---|---|
| 30 (TPS 3) | 11D | 1 | ~71% (net≥2) | ~99% (net≥1) | — | ~1% |
| 50 (TPS 5) | 13D | 1 | ~80% | ~99% | — | ~0.5% |
| 70 (TPS 7) | 15D | 1 | ~86% | ~99% | — | ~0% |

*Note: Overwhelming fires when net ≥ 2×Ob. At Ob 1, net ≥ 2 = Overwhelming. Near-guaranteed Overwhelming at any TS for Object-scale Weaving.*

### Probability Table — Weaving (Structural scale, Ob 5)

| TS (TPS) | Pool | Ob | P(Success) | P(Partial) | P(Failure) |
|---|---|---|---|---|---|
| 70 (TPS 7) | 15D | 5 | ~74% (net≥5) | ~23% | ~3% |
| 90 (TPS 9) | 17D | 5 | ~83% | ~15% | ~2% |
| 70 + TT Rupturing (+2 Ob → Ob 7) | 15D | 7 | ~35% | ~40% | ~25% |

*At TT 80–99, Structural Weaving becomes genuinely risky even at TS 90.*

### Findings

**F-01 · Object-scale operations are near-trivially safe (P2)**
At TS 50+, Object/Personal Weaving and Pulling at Ob 1–2 succeed overwhelmingly >90% of the time. For practitioners above TS 50, Object-scale Thread work is no longer a meaningful risk. The challenge evaporates. This may be intentional (competence should show) but it removes tension from routine Thread work at mid-tier play.
Proposed fix: Consider a "Practitioner's Trap" — overconfidence leads to skipping Diagnosis, not the dice themselves. Ensure GM uses Ob inflation (overweaving, environmental penalties) rather than relying on base Ob for tension.

**F-02 · TPS creates a non-linear power curve (P2)**
TPS jumps: TS 30→40 = TPS 3→4 (+1D). TS 40→50 = TPS 4→5 (+1D). But Leap Ob also drops from 2 to 1 at TS 50, which combines with the TPS gain to produce a step change rather than smooth scaling. At exactly TS 50, Leap goes from P(Success)≈88% (pool 12D, Ob 2) to P(Success)≈99% (pool 13D, Ob 1). This is the largest single jump in the system.
Severity: P2. No fix needed — the TS 50 threshold is narratively meaningful. Document as a design note.

**F-03 · TPS at TS 100 adds 10D — near-degenerate (P3)**
Pool of 18D at Ob 1 is mathematically degenerate — P(Failure) is effectively 0. At TS 100, Thread operations cannot fail on dice alone. Only Wound penalties (+Ob per Wound) provide counterweight.
Severity: P3. Resonant practitioners are meant to be extraordinary. No fix needed.

**F-04 · Wound penalty creates real tension (acceptable)**
At TS 30 (weakest practitioners), 3 Wounds increases Leap Ob to 5. Pool 11D vs Ob 5: P(Success) ≈ 42%. This is the system functioning as intended — wounded low-TS practitioners face genuine risk.

---

## BT3-02 · CO-MOVEMENT D10 — ISOLATION AND EDGE CASES

**Mode A + Mode D**
**Mechanic:** d10 rolled on every Thread operation. 10-entry consequence table. No supplements apply.

### Input Space

| Variable | Range |
|---|---|
| Roll | 1–10 (uniform, 10% each) |
| TT at time of operation | 20–100 |
| Practitioner TS | 30–100 |
| Non-practitioners present | 0–many |

### Consequence Analysis

| d10 | Consequence | Dimension | Frequency in 10 ops | Cumulative expected sessions to all outcomes |
|---|---|---|---|---|
| 1 | Knot strain +1 (GM choice) | Actual | 1× | ~10 ops |
| 2 | Object partial potentiality (1d3 days) | Actual | 1× | ~10 ops |
| 3 | Dissolution residue (TS 30+ detectable) | Actual | 1× | ~10 ops |
| 4 | Effect overshoot (GM determines direction) | Actual | 1× | ~10 ops |
| 5 | Environmental shift (TS 10+ detects) | Temporal | 1× | ~10 ops |
| 6 | Temporal echo (sensory impression of target past/future) | Temporal | 1× | ~10 ops |
| 7 | Epistemic bleed (witnesses disagree; investigation +1 Ob rest of session) | Epistemic | 1× | ~10 ops |
| 8 | Monstrous attention (consequence 1d3 sessions if TT≥40) | Temporal | 1× | ~10 ops |
| 9 | TS surge in witness (Discovery Event at scene end) | Epistemic | 1× | ~10 ops |
| 10 | Thread clarity (−1 Ob all Thread ops at site, 1 season) | Actual | 1× | ~10 ops |

*Expected: in any 10-operation sequence, all 10 outcomes appear approximately once. In a 4-season campaign with 2 practitioners averaging 3 ops/season: ~24 total ops → all outcomes fire at least twice.*

### Mode D — Edge Case Discovery

**Edge-1 · Result 8 (Monstrous Attention) + TT ≥ 40 interaction**
Setup: TT 42, practitioner performs 3 Thread operations in one scene. Three d10 rolls. P(at least one result 8) = 1 − 0.9³ = 27%. Each result 8 fires independently: 1d3 sessions until arrival.
Mechanism: Multiple concurrent monstrous attentions can stack, creating compounding incursion debt. Three stacked attentions = three separate 1d3-session countdown timers.
Severity: P2. No rule governs stacking resolution order or whether attentions merge. **Ambiguity — flag for mechanic-audit.**
Proposed fix: Clarify — monstrous attention timers refresh rather than stack (take the shortest timer, discard others). Or cap at one pending attention per practitioner.

**Edge-2 · Result 9 (TS surge) on Devout witness**
Setup: A Devout character with active essentialist theological Belief is present when a practitioner performs a Thread operation. d10 result 9: Discovery Event fires at scene end.
Mechanism: §4.4 states Devout Constraint forecloses TS growth checks "except Discovery Events which bypass this for the initial check (the experience is involuntary)." Result 9 triggers the Discovery Event procedure — the Devout character must check.
Finding: The co-movement d10 result 9 can trigger Devout characters into forced TS growth attempts regardless of their Belief. This is probably correct (involuntary exposure) but is not flagged in the co-movement table or the Devout Constraint rule as a connection.
Severity: P2. Cross-reference needed between §5.8 (result 9) and §4.4 (Devout Constraint). No mechanical fix needed; documentation fix needed.

**Edge-3 · Result 10 stacking (Thread clarity)**
Setup: Same site used for Thread operations multiple seasons. Each season: P(result 10) = 10% per operation.
Mechanism: "Thread clarity: all Thread operations here −1 Ob for one season." Does this stack with another result 10 in the same location?
Finding: No stacking rule exists. Without a minimum Ob floor per the effect, stacking result 10s could theoretically reduce Ob to 0 at a site. Ob minimum is always 1 (§1.3), so this is capped by core rules — but the per-operation rule says "one season" without clarifying whether a new result 10 refreshes or stacks.
Severity: P3. Core rules prevent degenerate result (Ob minimum 1). Document that Thread clarity refreshes duration, does not stack modifier.

**Edge-4 · Zero practitioners, result 9 fires**
Setup: A faction-scale Thread order is executed (board game mode). The roll is made but no personal practitioner is present in the scene.
Mechanism: Result 9 requires "one non-practitioner present with TS 10–29." In board game mode, no named characters are necessarily present.
Finding: Results 8 and 9 have no valid target in faction-scale abstract resolution. The co-movement table has no board-game exception.
Severity: P2. **Requires a rule clarification:** In board game mode, d10 results 8 and 9 default to faction-level equivalents (result 8: TT +1 this season; result 9: no effect).

**Edge-5 · Result 7 (Epistemic bleed) + Grand Debate in same session**
Setup: Thread operation fires result 7 ("investigation or Circles rolls +1 Ob rest of session"). A Grand Debate (5 exchanges) begins the same session.
Mechanism: Debate uses Poise/Presence pool, not investigation/Circles. Result 7's +1 Ob does not affect Debates. But if a Debate exchange involves an Evidence Style argument citing the scene's facts — does the "witnesses disagree" fiction apply?
Finding: No rule exists. The mechanical effect (investigation +1 Ob) doesn't affect Debates, but the narrative trigger (witnesses disagree on what happened) could logically affect Evidence Style arguments.
Severity: P3. Suggest: narrative only — result 7 gives GM permission to undercut Evidence Style arguments with witness contradiction, without a mechanical penalty. Purely GM discretion.

---

## BT3-03 · KNOT/CALL INTERACTION WITH INTELLIGIBILITY STRAIN

**Mode B — Interaction Chain**
**Chain:** Intelligibility decay → Knot strain accumulation → Knot reaches wrongness threshold → Call a Knot mechanics
**NPC/Archetype:** Maret Uln (Practitioner, Revolution), TS 40, Intelligibility starts at 10.

### Mechanic A → Mechanic B: Intelligibility → Knot Strain

**Intelligibility strain rates (§4.5):**
- Intelligibility 7–5: +1 strain to all Knots per 3 sessions
- Intelligibility 4–3: +1 strain per 2 sessions
- Intelligibility 2–1: +1 strain per session

**Maret Uln profile:**
- Bonds 3 → 3 Knots maximum
- Close Knot: wrongness threshold 3, crisis 6
- Regular Knot: wrongness threshold 5, crisis 10
- Distant Knot: wrongness threshold 8, crisis 16

**Intelligibility reduction triggers:** Each Relational+ operation: −1 Int. Past-Oriented Pulling: −1 additional.

### Chain Simulation — Campaign Arc (10 seasons, ~40 sessions)

**Assumption:** Maret Uln performs 1 Relational+ operation per season. 1 session = ~4 ops total.

| Season | Int | Knot strain rate | Strain added (per season = ~4 sessions) | Close Knot strain | Status |
|---|---|---|---|---|---|
| 1 | 10→9 | None (Int ≥ 8) | 0 | 0 | Clean |
| 2 | 9→8 | None | 0 | 0 | Clean |
| 3 | 8→7 | +1/3 sessions | ~1 | 1 | Strained |
| 4 | 7→6 | +1/3 sessions | ~1 | 2 | Strained |
| 5 | 6→5 | +1/3 sessions | ~1 | 3 | **Wrongness threshold reached** |
| 6 | 5→4 | +1/2 sessions | ~2 | 5 | Approaching crisis |
| 7 | 4→3 | +1/2 sessions | ~2 | 7 | **Crisis threshold crossed** |

At Season 7 (Int 3, ~28 sessions into campaign), Maret Uln's Close Knot is in Crisis. Cannot be Called. Entity takes action.

### Call a Knot — Probability Analysis

**Setup:** Maret Uln is at Intelligibility 7 (strain starting). Close Knot at strain 2 (approaching wrongness at 3). She considers calling it on an Ob 3 roll.
- Current pool: Spirit 3 + History 5 (Scholar 2pts) + TPS 4 = 12D
- Call bonus: +3D → 15D
- Expected net at TN7: 15 × 0.33 = 4.95
- P(net ≥ 3) = ~89%

**Cost:** +2 Knot strain. Brings Close Knot from 2 → 4 (past wrongness at 3 → Knot now in Wrongness state before Crisis).
**Result:** One Call on a strained Knot crosses from below-wrongness to wrongness in one action.

### Findings

**F-05 · Call a Knot accelerates Intelligibility-Knot cascade (P2)**
A practitioner who is already losing Intelligibility and Calling Knots will hit crisis state in both tracks simultaneously. By Season 7 in this scenario: Int 3, Close Knot in Crisis, Regular Knot in Wrongness. The combined pressure removes +3D from social rolls (Intelligibility 4–3: −1D to social; plus Rattled risk from Knot Crisis confrontations) and removes the Close Knot as a callable resource at exactly the point when the practitioner most needs it.
This is a reinforcing negative spiral. Severity: P2 (bad play experience at the extremes). The system appears to model intentional tragedy — the more you rely on Knots, the faster they deteriorate. Document explicitly as intended design.

**F-06 · Wrongness threshold has no mechanical description (P1)**
§4.7 defines wrongness as: "the connected entity begins perceiving something is off about the character." But there is no mechanical effect on the Knot until Crisis. A Knot in Wrongness can still be Called. The wrongness threshold is purely a narrative signal.
Finding: The Knot at wrongness threshold (strain 3 for Close) and at strain 4 (below Crisis at 6) functions identically mechanically. The graduated tension is narrative only.
This is not necessarily a problem, but it means: a GM who doesn't invoke the wrongness fiction loses the escalation signal entirely. No mechanical penalty reinforces the drama.
Severity: P2. Proposed fix: At wrongness threshold, add one mechanical trigger (e.g., the connected entity is now active — they will approach the practitioner this season; GM must use this). Makes the threshold a GM obligation, not an option.

**F-07 · Knot strain recovery rate is asymmetric with strain accumulation (P2)**
Close Knot recovery: −1 strain per season of active positive engagement. But Intelligibility decay at level 4–3 adds +1 strain per 2 sessions (~+2 per season). Recovery cannot outpace accumulation while Int ≤ 4. The Knot is trapped in perpetual deterioration regardless of what the character does relationally.
Severity: P2. This is a structural trap. Proposed fix: Intelligibility recovery should partially recover Knot strain rate. When Int rises (rest season: +1 Int), the strain rate should reduce. Currently, recovering Int 4→5 drops strain rate from +1/2 sessions to +1/3 sessions — this is functional but not labeled as Knot-affecting. Cross-reference note needed.

---

## BT3-04 · RATTLED STACKING WITH COMPOSURE RESET

**Mode A — Isolation**
**Mechanic:** Composure = Presence + 6. Strain accumulates; when strain ≥ Composure → +1 Rattled, −1D social, Composure resets to full.
**Scenario:** Himlensendt (Presence 4, Composure 10) in a 5-exchange Grand Debate.

### Input Space

| Variable | Range | Typical | Edge |
|---|---|---|---|
| Composure (Presence + 6) | 7–13 | 10 | 7 (Pres 1) / 13 (Pres 7) |
| Strain per losing exchange | +1 (normal loss) / +2 (overwhelming loss) | +1 | +2 |
| Rattled marks to incapacitation | 2 | 2 | 1 (if single 8+ strain hit) |
| Dice penalty per Rattled | −1D | −1D | stacking |

### Probability Table — Rattled Accumulation in Grand Debate (5 exchanges)

**Baseline:** Himlensendt (Composure 10). Losing +1 strain per exchange.

| Exchanges lost | Strain total | Rattled marks | Net D penalty | Social pool remaining |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | Full |
| 5 | 5 | 0 | 0 | Full (never reached Composure 10) |
| 5 of 5, each +2 (overwhelming) | 10 | 1 | −1D | Reduced |
| 5 of 5, +2 each, + one +2 spike | 12 | 1 | −1D | (Composure resets after first Rattled → 2 remaining strain) |

**Key finding:** With Composure 10 and standard +1 losses, a character can lose all 5 Grand Debate exchanges without becoming Rattled. Strain only reaches 5, never 10.

### Rattled Threshold to Incapacitation

| Composure | Strain needed for 1 Rattled | Strain needed for 2nd Rattled (incap) |
|---|---|---|
| 7 (Pres 1) | 7 strain total | 14 strain total |
| 10 (Pres 4) | 10 strain | 20 strain |
| 13 (Pres 7) | 13 strain | 26 strain |

*After first Rattled, Composure resets. So incapacitation (2 Rattled) requires the character to accumulate full Composure in strain TWICE.*

### Mode D — Edge Cases

**Edge-6 · Composure reset creates burst exploitation (P2)**
Setup: Attacker deliberately accumulates strain to just below Composure threshold, then delivers a single +2 (Overwhelming) hit.
Mechanism: At strain 9/10, one +2 hit → strain 11 → Composure exceeded → 1 Rattled, reset to full. Attacker achieves Rattled with one Overwhelming loss rather than grinding 10 exchanges.
Finding: The reset mechanic makes Rattled acquisition front-loadable. Two modes: (a) grind to Composure gradually; (b) get one Overwhelming hit near the threshold. Mode (b) takes 9 normal exchanges + 1 Overwhelming, which is more efficient at high Composure values. No rule prevents this.
Severity: P2. The Inspiration attack mechanic (§9.6) already requires Failure (net ≤ 0) to trigger, so burst exploitation requires both Overwhelming from attacker AND Failure from defender — not trivially achievable.

**Edge-7 · Unmask resets Rattled but voids the Debate**
Setup: Character takes 1 Rattled mid-Debate (exchanges 2 of 5). Considers Unmask.
Mechanism: "All Rattled clear on: Unmask, scene end, or rest." Unmask also: "current incomplete exchange voided; Subsequent direct action: Ob = exchange deficit + 1."
Finding: If character is 2 exchanges behind in a Grand Debate and Unmasked, they gain: Rattled cleared (+1D restored), but take: exchange deficit Ob (+3 minimum on subsequent actions). Plus the Debate ends. Unmask is never mechanically advantageous mid-losing-Debate from a pure dice perspective. It is a narrative tool only.
Severity: P3. This is correct — Unmask should not be a dominant strategy. No fix needed.

**Edge-8 · Multiple Rattled penalty and Debate viability (P1 — interaction gap)**
Setup: Character takes 2 Rattled (−2D all social rolls) before incapacitation threshold.
Mechanism: "At 2 Rattled marks, the character is socially incapacitated — they cannot participate in formal social scenes (Debates, Appeals) until recovered."
Finding: There is no rule for what happens to an ongoing Debate when one participant becomes incapacitated mid-exchange. Does the Debate immediately resolve in the opponent's favour? Does it pause? Does the incapacitated character's last stated position hold?
Severity: P1. The gap produces unresolvable table situations in a Grand Debate (5 exchanges). **Flag for mechanic-audit.**
Proposed fix: Incapacitation mid-Debate = concede. The incapacitated character's side loses all remaining exchanges. Opponent wins the Debate with the current exchange deficit.

---

## BT3-05 · DOMAIN OB + LEADERSHIP POOL

**Mode B — Interaction Chain**
**Mechanic:** Domain Ob = target faction's relevant stat (direct, 1–7 scale). Pool = personal attribute + History bonus + faction's relevant stat (if leader/officer).
**Scenario:** Baralta (Hafenmark Faction Leader) executing a Domain Action against the Church.

### Setup

**Baralta's profile (personal):** Presence 5, History "Constitutional Legalist" 3pts → social pool = 5 + 6 = 11D.
**Baralta holds Hafenmark leadership:** Hafenmark Mandate 4 → adds 4D to pool → total 15D.
**Target:** Church Mandate 5 → Domain Ob = 5.
**Ethical framework:** Action on constitutional precedent → −1 Ob → effective Ob 4.

| Pool | Ob | P(Success) | P(Partial) | P(Failure) | Expected Net |
|---|---|---|---|---|---|
| 15D (leader) | 4 | ~84% | ~12% | ~4% | 4.95 |
| 11D (no faction stat — non-leader) | 4 | ~57% | ~25% | ~18% | 3.6 |
| 15D | 5 (non-aligned action) | ~74% | ~18% | ~8% | 4.95 vs 5 |
| 15D | 7 (Church anti-Thread, max modifier) | ~35% | ~40% | ~25% | 4.95 vs 7 |

### Mode D — Edge Cases

**Edge-9 · Domain Ob = 7 is structurally valid (P2)**
The Ob range for Domain Actions is now 1–7 (direct stat). An Ob 7 Domain Action (targeting a faction with stat 7) is legal.
At 15D vs Ob 7: P(Success) ≈ 35%. At 11D: P(Success) ≈ 18%.
Finding: Ob 7 Domain Actions have ~18–35% success rates for typical characters. This is realistic for entrenched institutional opposition but creates large failure zones, especially for non-leaders.
Question: Prior ruleset used stat ÷ 2 (Ob 1–4 max). CP14 uses direct stat (Ob 1–7). This **doubles the maximum Ob** for Domain Actions. If this change is intentional, faction stats in the 6–7 range make Domain Actions against those factions extremely difficult even for experienced players.
Severity: P1 from an audit perspective — the change must be intentional and documented as such. The stage6 file (still showing ÷2) is out of sync. **Requires confirmation from editorial.**

**Edge-10 · Officer vs Leader qualification gap (P3)**
"Senior officer or trusted lieutenant at GM discretion." No definition of who counts. A PC who has taken one faction action may claim officer status; GM may deny it. The pool advantage (+faction stat dice) is significant (often +3 to +5 dice), making the qualification boundary a high-stakes table arbitration.
Severity: P2. Proposed fix: Define a minimum threshold — e.g., "a character who has successfully completed at least one Domain Action on behalf of a faction in the current or prior season qualifies as officer for that season."

---

## BT3-06 · RENOWN × DEBATE INTERACTION

**Mode B — Interaction Chain**
**Mechanic:** Renown grants social access and initial debate advantages. Debate uses Presence/Poise pools.
**Scenario:** Almud (Renown 6, Ducal) vs Himlensendt (Renown 7, Confessor) in a Grand Debate.

### Renown Table (CP14 lines 2928–2938)

| Renown | Tier | Debate Effect |
|---|---|---|
| 4 | Established | No combat advantage |
| 5 | Notable | +1D initial advantage vs lower Renown opponent |
| 6 | Ducal | Debate advantage vs Renown 5 or below |
| 7 | Confessor | +2D initial advantage vs lower Renown |
| 9 | Legendary | "Nearly insurmountable" advantage |

### Interaction Analysis

**Almud (Renown 6) vs Himlensendt (Renown 7):**
- Himlensendt has higher Renown → +2D initial advantage vs Almud on first exchange(s).
- "Initial advantage" — does +2D apply to all 5 Grand Debate exchanges or just Exchange 1?

**Finding:** The ruleset says "initial debate audience" (Renown 5 note) and "+2D initial advantage" (Renown 7 note). "Initial" is undefined. Does this mean:
(a) Exchange 1 only — after that, pools are equal?
(b) All exchanges — a permanent pool bonus for the duration?

This is unspecified and has large mechanical consequences.

**Probability impact — Exchange 1:**

| Scenario | Attacker Pool | Defender Pool | Ob context | P(Attacker wins exchange) |
|---|---|---|---|---|
| Equal Renown, equal skills | 10D | 10D | Higher net wins | ~50% |
| Renown 7 (+2D) vs Renown 6 | 12D vs 10D | — | — | ~62% |
| Renown 9 ("insurmountable") vs Renown 6 | 15D+ vs 10D | — | — | ~75%+ |

*If +2D applies to ALL exchanges: Renown 7 wins 62% of each exchange. Over 5 Grand Debate exchanges, they win ~3.4/5 on average — almost guaranteed to win 3-2 or better.*

**Severity:** P1. The scope of "initial advantage" must be defined for the Debate mechanic to be deterministic.
**Proposed fix:** Renown advantage applies to Exchange 1 only. After Exchange 1, all parties roll on equal pools. This maintains the flavour (social status opens doors) without making high Renown mechanically dominant over long Debates.

### Additional Finding

**F-08 · Renown grants Debate advantage without a social roll (P2)**
Renown bypasses the Reading Exchange. High-Renown characters don't need to perceive their opponent to gain initial advantage — it is status-based, not perception-based. A Renown 9 Legendary character gains "nearly insurmountable" advantage in Debates before a single exchange occurs, regardless of preparation.
This creates a dominant strategy: build Renown instead of Debate skills. Renown accumulates from public Belief resolution, not social skill.
Severity: P2. Renown advantage is narrative-appropriate but mechanically competes with the Debate pool system. Document as a known design tension — high-status characters may be mechanically better at Debates than skilled-but-unknown characters. This is probably intentional.

---

## BT3-07 · VAYNARD AMBITION TRACK — FULL RANGE

**Mode A — Isolation**
**Mechanic:** 0–100 track. +1/season baseline. +5 per blocked action. +10 per public humiliation.
**Thresholds:** 20/40/60/80/100.

### Input Space

| Variable | Range | Typical | Edge |
|---|---|---|---|
| Baseline rate | +1/season | +1 | +1 (constant) |
| Blocked actions per season | 0–3 | 1 | 0/3 |
| Humiliations per season | 0–2 | 0 | 0/2 |
| Total Ambition gain per season | 1–26 | 6 | 1 (ignored) / 26 (maximally opposed) |

### Threshold Crossing Analysis

**Passive trajectory (no opposition):** +1/season. Seasons to threshold:
- Threshold 20: Season 20
- Threshold 40: Season 40
- Threshold 60: Season 60
- Threshold 80: Season 80
- Threshold 100: Season 100

*At +1/season with no opposition, Vaynard never becomes militarily aggressive in a standard 10-season campaign. The threat is entirely latent.*

**Active trajectory (PCs actively oppose Varfell):** 1 blocked action + 0 humiliations = +6/season.
- Threshold 20: Season 3–4
- Threshold 40: Season 7
- Threshold 60: Season 10
- Threshold 80: Season 14
- Threshold 100: Season 17

**Maximally opposed (3 blocked + 2 humiliations per season = +26):**
- Threshold 20: Season 1 (within first season)
- Threshold 40: Season 2
- Threshold 60: Season 3
- Threshold 80: Season 4
- Threshold 100: Season 4–5

### Findings

**F-09 · Passive rate is non-threatening (P2)**
In a standard 10-season campaign, passive Ambition reaches 10. No threshold crossed. Vaynard is never triggered without active opposition. The track is entirely reactive.
This means: tables that actively ignore Varfell see no Ambition events. The track only matters if the PCs engage with it. This is a design choice — but it should be explicit in the GM tools section. Currently the track description doesn't mention that passive rate never crosses a threshold in a standard campaign.
Severity: P2. Add to §14.8 GM reference: "Vaynard's Ambition Track will not cross Threshold 20 through passive drift in a 10-season campaign. Active opposition by PCs is required to engage the track's mechanics."

**F-10 · No decrease mechanic exists (P2)**
Vaynard's Ambition can only increase. There is no mechanic to reduce it (unlike TT, TC, IP which all have decrease sources). Once Ambition crosses 100 (military campaign launches), there is no de-escalation path.
Finding: This makes the track a one-way ratchet. PCs who trigger high Ambition early cannot walk it back through diplomacy or other means.
Severity: P2. Proposed fix: Add one decrease trigger. Suggested: "Successful Diplomacy Domain Action representing a victory over Varfell that includes a concession from another faction (not merely defeating Vaynard): Ambition −5." This creates a diplomatic cost-benefit calculation.

**F-11 · Threshold 100 fires military campaign with no prior warning (P3)**
Threshold 80: "War declaration becomes available. Issues formal demands." Threshold 100: "Military campaign launches."
The jump from 80 to 100 at maximum opposition rate (+26/season) can happen in one season. PCs may have one season to respond to formal demands before war.
Severity: P3. Mechanically functional. The demands at 80 are the warning. No fix needed.

---

## BT3-08 · NIFLHEL SUPREMACY MECHANIC

**Mode A + Endgame**
**Mechanic:** Four networks (Sollvik, Hafenbund, Bernweg, Stiltsift) compete at seasonal accounting.
- Leading network: +1 Intel
- Weakest network: −1 Stability
- Stability 0: absorbed/destroyed
- One network eliminates all rivals → Partial Faction

### Starting State (confirmed in CP14)

| Network | Starting Stats | Alliance |
|---|---|---|
| Sollvik | Intel implied mid-range, Stability implied mid-range | Allied with Stiltsift |
| Hafenbund | Same | Opposed |
| Bernweg | Same | Opposed |
| Stiltsift | Same | Allied with Sollvik |

*No explicit starting stats are provided per network. The faction sheet shows Niflhel aggregate (Intel, Wealth, Stability only — no Mandate, no Military).*

### Simulation — Symmetric Starting State

**Assumption:** All four networks start at Intel 3, Stability 3 (equal distribution of aggregate).

| Season | Sollvik (S+St allied) | Hafenbund | Bernweg | Stiltsift (allied S) | Leader | Weakest | Events |
|---|---|---|---|---|---|---|---|
| 1 | I3 Sta3 | I3 Sta3 | I3 Sta3 | I3 Sta3 | Tie | Tie (random) | One random −1 Stability |
| 2 | Advantage begins if random weakest avoided | — | — | — | — | — | — |

**Finding:** With symmetric starting values, the "leading network" is undefined in Season 1. No tiebreak rule is specified.
Severity: P1. **Ambiguity — tie condition has no resolution rule.**
Proposed fix: In ties for leading, all tied networks gain +1 Intel. In ties for weakest, one random network takes −1 Stability (GM roll or draw).

### Endgame: Partial Faction Achievement

**Scenario:** Sollvik-Stiltsift alliance successfully eliminates Hafenbund and Bernweg over 8 seasons.

**Seasonal accounting rate for elimination:**
- Weakest network loses −1 Stability per season.
- At Stability 3: takes 3 seasons to reach Stability 0 (unassisted).
- If targeted by Intel Domain Actions (sabotage): Stability −1/season additional.
- Realistic elimination timeline: 3–4 seasons per network.

**Total to Partial Faction:** 6–8 seasons for both rivals.

**Partial Faction capability:**
"No territory, no Mandate, but full Intel and Wealth. May manufacture a noble claim and attempt territory via casus belli."

Finding: No mechanics are given for how the Partial Faction manufactures a noble claim or what the Ob structure for casus belli → territory acquisition looks like. The endgame path is named but mechanically hollow.
Severity: P1. This is a significant endgame scenario (PC taking over Niflhel and pursuing aristocratic legitimacy) with no mechanical support.
Proposed fix: Define a 3-step procedure: (1) Manufacture claim — Intel Domain Action Ob 4 (fabricating genealogy, forging documents); (2) Casus belli — Parliament vote or Grand Debate; (3) Territory acquisition — standard military/diplomacy.

---

## BT3-09 · TC PAUSE AT CHURCH STABILITY ≤ 4

**Mode C — Full Scenario Simulation**
**Mechanic:** "When Church Stability falls to 5 or below at seasonal accounting, TC generation ceases that season regardless of Church Mandate."
*(Per §14.7 checklist: TC pauses if Church Stability ≤ 4. Per §8.3 text: "Stability ≤ 4: TC generation pauses." Cross-check: checklist uses ≤ 4; §8.3 uses ≤ 4. Consistent. Earlier version said "≤ 5" — CP14 has it at ≤ 4.)*

### Scenario Setup

**Season 5 of 10. Church under pressure.**

```
## State: Season 5, Pre-Accounting
### Clocks
TT 35 | TC 38 | IP 28

### Factions
Church — M5 I6 W5 Mil4 Stability: 5 (above pause threshold)
Crown — M5 I5 W4 Mil4 Stability: 4
Hafenmark — M4 I4 W5 Mil3 Stability: 4

### TC Sources This Season
Church Mandate 5 at accounting: +1/season
TT 35 (below 45): no TT-driven TC addition
Church Mandate ≥ 5 → +1/season
Total projected TC: +1 → TC 39

### Active Conditions
Baralta's Mandate ≥ 4: TC suppressor active (−1/season)
Net TC change: +1 − 1 = 0
```

### Action: PCs Trigger Cardinal Conflict

**PCs expose Klapp's Niflhel connection (Church Intel operation, Ob 3).**

```
## Action: Expose Klapp
Pool: 10D (Riskbreaker archetype, PC)
TN 7, Ob 3
P(Success): ~73% | P(Partial): ~18% | P(Failure): ~9%
Expected net: 3.3

### Most likely outcome: Success
Klapp exposed. Church internal politics: Cardinals openly compete.
Church Stability check Ob 3 (two active threats: exposure + succession fight).

## Action: Church Stability Check
Pool: 5D (Stability 5)
TN 7, Ob 3
P(Success/Overwhelming): ~25% | P(Partial — not applicable): — | P(Failure): ~75%
Expected net: 1.65

### Most likely outcome: Failure
Church Stability −1 → Stability 4.

### State Delta
Church Stability: 5 → 4
TC pause threshold: NOW AT BOUNDARY (≤ 4 = paused)
```

```
## State: End of Season 5 Accounting
### Clocks
TT 35 | TC 38 (unchanged — TC generation pauses at Church Stability 4)
IP 28

### Factions
Church — M5 I6 W5 Mil4 Stability: 4 (at threshold)
TC generation: PAUSED this season

### Findings
TC held at 38 rather than advancing to 39.
Church Mandate still 5 — if Stability recovers above 4 next season, TC generation resumes.
```

### Season 6 — Stability Recovery Path

```
## State: Season 6, Start
Church Stability: 4
No new threats declared.
Church Stability check: Ob 1 (quiet season)
Pool: 4D, TN7, Ob 1
P(Success): ~92% | P(Failure): ~8%
Expected: Stability recovers to 5.

### Most likely outcome: Church Stability returns to 5. TC generation resumes Season 6.
TC advance: +1 (Mandate 5) − 1 (Baralta suppressor) = 0. TC stays 38.
```

### Findings

**F-12 · TC pause is binary and recovers within one season (P2)**
The TC pause threshold (Stability ≤ 4) fires for exactly one season when Church Stability drops to 4. On a quiet season check, the Church recovers to 5 with 92% probability. The pause effect is therefore typically: one season of TC generation halted, then normal resumes.
To maintain TC pause pressure, PCs must keep Church Stability suppressed each season. This requires active Domain Action effort every season — sustainable only with dedicated anti-Church play.
Severity: P2. The mechanic works as intended but is weaker than it might appear. Inform tables: "One successful anti-Church operation does not permanently suppress TC. Sustained effort is required."

**F-13 · TC pause interacts with Baralta suppressor ambiguously (P1)**
§8.4 states: "While Baralta's Mandate remains 4+, she suppresses TC at −1/season." §8.3 (Church): "Stability ≤ 4: TC generation ceases."
When both are active simultaneously, TC generation ceases AND Baralta's −1 is also active. Does Baralta's modifier apply to a paused TC (i.e., does TC go to −1 this season)?
**No rule governs this interaction.** If TC generation ceases = the raw change is 0, and then Baralta's modifier applies: TC −1 in a season when TC would have paused anyway, creating a −1 effect without active Church generation.
Severity: P1. Proposed fix: Clarify that TC pause means TC change is set to 0 before modifiers. Negative modifiers (Baralta suppressor, Grand Debate victory) may still reduce TC below 0 (i.e., TC goes down even in a pause season). This is actually a beneficial player interaction — PCs who suppress Church Stability AND have Baralta active can actively reduce TC.

---

## BT3-10 · SEASONAL EVENTS S-16–S-20

**Mode C — Full Scenario Simulation**
**Mechanics:** Five new seasonal events drawn from the BG event deck.

### S-16 · Niflhel Network Exposure

```
## State: Season 4
### Clocks
TT 30 | TC 25 | IP 22

### Factions
Niflhel — Hafenbund (public exposure of a smuggling operation)
```

**Trigger:** S-16 drawn. Hafenbund Intel −1 for 2 seasons. Any faction with active Intel order this season may learn one piece of information Hafenbund holds.

**Resolution:**
```
Hafenbund Intel: assume 3. → 2 for 2 seasons.
Factions with active Intel orders: Crown, Varfell (both had Intel orders active).
Crown learns: one piece of Hafenbund information.
Varfell learns: one piece of Hafenbund information.
```

**Findings:**

**F-14 · "One piece of information" is undefined (P1)**
The card says "one piece of information that network holds." No definition of what Niflhel networks hold as information, what format it takes, or how GMs adjudicate which piece is revealed.
Severity: P1. Proposed fix: Standardize as "one currently secret faction attribute, or one NPC's active Belief, or one pending Domain Action intent" — matching the Quiet Network's Intelligence mode format.

**F-15 · Two factions learning from the same source simultaneously (P2)**
Crown and Varfell both gain information from Hafenbund in the same season due to S-16. They may learn the same thing or different things. No rule governs which faction learns which piece, or whether multiple factions can learn the same piece.
Severity: P2. Proposed fix: GM distributes different pieces to different factions (first active Intel order picks, second gets a different piece). If only one piece available: first faction gets it; second gets "knowledge of the exposure only" (they know something was revealed but not the content).

### S-17 · Einhir Practitioner Surfaces

```
## State: Season 6
### Clocks
TT 42 | TC 32 | IP 24

### Factions
Church — Inquisition now active
Revolution — +1 Influence in affected territory
```

**Trigger:** S-17 drawn. Practitioner TS 40+ operating openly in Territory X (random). Church automatically opens Inquisition. Revolution +1 Influence in that territory. TT +1.

**State Delta:**
```
TT: 42 → 43
Revolution Influence in Territory X: +1
Church opens Inquisition in Territory X.
```

**Findings:**

**F-16 · "Automatically opens Inquisition" has no associated mechanic (P2)**
The Church's Inquisition is referenced but the specific mechanics of an active Inquisition (Ob effects, CE implications, how it escalates) are not consolidated in one location. The term appears in TC rise sources and NPC descriptions but no "Inquisition procedure" section exists in the compiled ruleset.
Severity: P2. The Inquisition is a central factional tool that players will encounter frequently. A procedural section is needed (or a cross-reference to wherever this is defined).

**F-17 · "Random territory" trigger has no defined procedure (P3)**
"One random territory" — no specified randomization method.
Severity: P3. In TTRPG mode, GM selects narratively appropriate territory. In board game, should use territory number draw or die roll. Add: "In BG mode, draw a territory number card or roll 1d15."

### S-18 · Border Skirmish

```
## State: Season 3
### Factions Affected
Two adjacent factions (GM or random): Church and Hafenmark
```

**Trigger:** Both factions −1 Stability. IP +1 if Crown is involved.

```
Church Stability: 5 → 4 (now at TC pause threshold — see BT3-09)
Hafenmark Stability: 4 → 3
IP: Crown not involved. No IP change.
```

**Compounding interaction:** S-18 drops Church Stability to 4, which (depending on season timing) may trigger the TC pause mechanic (BT3-09). A single event card can trigger a cascade: Church Stability drop → TC pause → Baralta suppressor active → TC potentially reduced by 1 this season.

**Findings:**

**F-18 · S-18 + TC pause cascade (P2)**
S-18 drawn in a season when Church Stability is already 5 → drop to 4 triggers TC pause. Combined with Baralta suppressor (−1), TC goes −1 this season. One random seasonal event card effectively generates TC reduction without any active PC play.
Severity: P2. This is not necessarily a problem — variance is expected. Note for GM: S-18 is more powerful than it appears when Church Stability is near threshold.

### S-19 · Debt Called

```
## State: Season 5
### Factions
Guilds call debt from faction with highest Wealth: Church (Wealth 5)
```

**Trigger:** Church chooses: pay (Wealth −1 this season) OR Guilds gain Influence +1 in one territory.

**Decision tree:**
- Church Wealth −1: 5→4. Still strong. Church likely pays.
- If Church refuses: Guilds Influence +1 in one territory. Church avoids economic damage, Guilds gain political foothold.

**Finding:**

**F-19 · No adversarial resolution if Church refuses (P3)**
The event gives the targeted faction a binary choice with no GM arbitration needed. The choice is always available to them. There is no rule for what happens if the targeted faction has Wealth 0 (cannot pay). Edge case: at Wealth 0, the faction must give Guilds the Influence.
Severity: P3. Degenerate case is handled implicitly. No fix needed.

### S-20 · Thread Quiet

```
## State: Season 7
### Clocks
TT 48 | TC 44 | IP 30

### Thread Operations This Season
Three practitioners plan operations.
```

**Trigger:** All Thread operations −1 Ob. TT −1 at seasonal accounting. Practitioners with TS 50+ sense it as "uncanny — the quiet is wrong."

**Ob effect:**
- A Leap at TS 30 (normally Ob 2) → Ob 1. P(Success): 11D vs Ob 1 → ~99%.
- Weaving at Territorial (normally Ob 4) → Ob 3. P(Success): 13D vs Ob 3 → ~80%.
- Past-Oriented Pulling (normally Ob 5 + additional) → Ob 4. P(Success): 15D vs Ob 4 → ~84%.

TT effect: −1 at accounting. TT 48 → 47 (below 45 for TT-driven TC effects).

**Findings:**

**F-20 · Thread Quiet drops TT below a cross-clock threshold (P2)**
If TT is at 46 or 47 when S-20 fires, the −1 reduction drops TT below 45. This removes the TT>45 cross-clock effect (TC +1/season; IP +1/season) for the following season, producing a double benefit: practitioners get −1 Ob AND two cross-clock effects pause.
Severity: P2. This is favourable compounding for PCs. Note for GM: when TT is near the 45 threshold, S-20 has outsized strategic value. No fix needed — this is emergent interaction, not a bug.

**F-21 · "The quiet is wrong" has no mechanical consequence (P3)**
TS 50+ practitioners sense the Thread Quiet as uncanny. The ruleset says this but provides no mechanical hook (Discovery Event, Certainty check, TS growth opportunity, etc.).
Severity: P3. This is a missed narrative opportunity. Proposed fix: Add: "Practitioners with TS 50+ who acknowledge the wrongness in-scene may make a Spirit check TN 7 Ob 1 to gain +1 TS (maximum one advance per campaign)."

---

## MASTER FINDINGS REGISTER

| ID | Test | Severity | Type | Description | Status |
|---|---|---|---|---|---|
| BUG-001 | Preflight | P1 | Error | "18 attribute points" in §12.1 + §14.7 (correct: 31) | Fix required |
| BUG-002 | Preflight | P1 | Error | Stage3 file uses obsolete attribute names (Heart/Poise) vs CP14 | Fix required |
| BUG-003 | Preflight | P1 | Error | Stage6 Domain Ob spec (÷2) vs CP14 (direct stat) — confirm intentional | Editorial needed |
| F-01 | BT3-01 | P2 | Design | Object-scale Thread ops trivially safe at TS 50+ | Document as design note |
| F-02 | BT3-01 | P2 | Design | TPS creates step-change at TS 50 (Ob drop + TPS gain simultaneously) | Document as design note |
| F-03 | BT3-01 | P3 | Edge | TS 100 pool degenerate (near-zero failure rate) | No fix needed |
| F-04 | BT3-01 | OK | — | Wound penalties create real tension at TS 30 | Functioning as intended |
| Edge-1 | BT3-02 | P2 | Gap | Monstrous attention (d10-8) stacking: no rule | Mechanic-audit |
| Edge-2 | BT3-02 | P2 | Gap | d10-9 on Devout witness: connection not cross-referenced | Documentation fix |
| Edge-3 | BT3-02 | P3 | Gap | Thread clarity (d10-10) stacking: duration refresh rule needed | Minor clarification |
| Edge-4 | BT3-02 | P2 | Gap | d10-8/9 inapplicable in BG faction-scale Thread ops | BG fallback rule needed |
| Edge-5 | BT3-02 | P3 | Design | d10-7 epistemic bleed + Evidence Style Debate: narrative only | GM discretion, no fix |
| F-05 | BT3-03 | P2 | Design | Call-a-Knot + Intelligibility decay = reinforcing spiral | Document as intentional |
| F-06 | BT3-03 | P2 | Gap | Wrongness threshold: no mechanical effect, purely narrative | Add GM obligation trigger |
| F-07 | BT3-03 | P2 | Design | Knot recovery cannot outpace Int ≤ 4 decay rate | Cross-reference needed |
| Edge-6 | BT3-04 | P2 | Design | Composure reset allows burst Rattled acquisition near threshold | Expected; Inspiration attack gating limits this |
| Edge-7 | BT3-04 | P3 | Design | Unmask never mechanically advantageous mid-losing Debate | Correct — narrative tool only |
| Edge-8 | BT3-04 | P1 | Gap | Incapacitation mid-Debate: no resolution rule | Mechanic-audit: fix = concede all remaining exchanges |
| Edge-9 | BT3-05 | P1 | Editorial | Domain Ob = direct stat (1–7) vs old ÷2 — editorial confirmation needed | Editorial: confirm intentional |
| Edge-10 | BT3-05 | P2 | Gap | Officer qualification undefined — high-stakes GM arbitration | Define minimum threshold |
| F-08 | BT3-06 | P2 | Design | Renown builds Debate advantage without social skill investment | Known tension, document |
| F-09 (Renown) | BT3-06 | P1 | Gap | "Initial advantage" scope undefined: Exchange 1 only vs all exchanges | Mechanic-audit: define as Exchange 1 only |
| F-09 | BT3-07 | P2 | Gap | Passive Ambition (1/season) never crosses threshold in 10-season campaign | Add GM reference note |
| F-10 | BT3-07 | P2 | Gap | Vaynard Ambition: no decrease mechanic | Add diplomatic de-escalation option |
| F-11 | BT3-07 | P3 | Design | 80→100 jump possible in one season at max opposition | Functioning as intended |
| F-12 | BT3-08 | P1 | Gap | Niflhel Supremacy: no tiebreak for leading/weakest when equal | Add: all tied = all get +1 Intel; random weakest |
| F-13 | BT3-08 | P1 | Gap | Partial Faction endgame path mechanically undefined | Define 3-step procedure |
| F-12 (TC) | BT3-09 | P2 | Design | TC pause lasts 1 season and recovers with 92% probability — weaker than it appears | Document for GMs |
| F-13 (TC) | BT3-09 | P1 | Gap | TC pause + Baralta suppressor: interaction undefined (TC −1 in pause season?) | Clarify: modifiers still apply to paused baseline |
| F-14 | BT3-10 S-16 | P1 | Gap | "One piece of information" undefined | Standardize using Quiet Network format |
| F-15 | BT3-10 S-16 | P2 | Gap | Multiple factions learning from same source: no distribution rule | GM distributes different pieces |
| F-16 | BT3-10 S-17 | P2 | Gap | "Inquisition" referenced but no procedure defined in ruleset | Procedure section needed |
| F-17 | BT3-10 S-17 | P3 | Gap | "Random territory" has no BG randomization method | Add: 1d15 or territory draw |
| F-18 | BT3-10 S-18 | P2 | Design | S-18 can cascade into TC pause + Baralta suppressor | Note for GM, no fix |
| F-19 | BT3-10 S-19 | P3 | Edge | Wealth 0 faction cannot pay debt — implicit resolution | No fix needed |
| F-20 | BT3-10 S-20 | P2 | Design | Thread Quiet drops TT below 45: removes two cross-clock effects simultaneously | Note for GM, no fix |
| F-21 | BT3-10 S-20 | P3 | Gap | "Quiet is wrong" flavour text has no mechanical hook for TS 50+ practitioners | Optional: Spirit check TS growth opportunity |

---

## P1 FINDINGS SUMMARY (Requires Action Before CP15)

1. **BUG-001** — "18 attribute points" error in §12.1 + §14.7 → fix text to 31
2. **BUG-002** — Stage3 file obsolete attribute names → update stage3 to CP14 spec
3. **BUG-003** — Domain Ob formula discrepancy (stage6 vs CP14) → editorial confirmation
4. **Edge-8** — Mid-Debate incapacitation: no rule → fix: concede remaining exchanges
5. **Edge-9** — Domain Ob scope (direct stat = intentional?) → editorial confirmation
6. **Renown F-09** — "Initial advantage" scope undefined → fix: Exchange 1 only
7. **F-12 (Niflhel)** — Supremacy tiebreak missing → fix: tie = all +1 Intel, random weakest
8. **F-13 (Niflhel)** — Partial Faction endgame path undefined → define procedure
9. **F-13 (TC)** — TC pause + Baralta suppressor interaction undefined → clarify modifier order
10. **F-14 (S-16)** — "One piece of information" undefined → standardize

---

*End of Batch 3 stress tests. 10 mechanics tested. 10 P1 findings. 15 P2 findings. 7 P3 findings.*
*Next: Apply P1 text fixes (BUG-001, BUG-002) then push. Flag remaining P1s to gap register.*
