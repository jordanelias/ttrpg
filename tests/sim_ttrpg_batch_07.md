# VALORIA STRESS TESTS — BATCH 07
## High-Interaction Coverage Pass — ≥3 Co-mechanic Tests
**Executed:** 2026-03-27 | **Model:** Opus 4.6 | **Skill:** valoria-simulator
**Purpose:** Close 31-mechanic interaction gap. All tests: ≥3 co-mechanics per test.

---

## T-B7-01 — CORE DICE + WOUNDS + CONDITIONS + INITIATIVE + REST
**Coverage:** M-001, M-002, M-007, M-039, M-053
**Mode:** TTRPG | **Temporal:** PRES | **Tracks:** COMP | **Factions:** Crown,Löwenritter | **NPCs:** Ehrenwall | **Archetypes:** Löwenritter Knight,Generic

### Mode B — Interaction Chain

**Chain:** M-039 (Initiative) → M-001 (dice resolution) → M-002 (wound application) → M-007 (condition attachment) → M-053 (rest recovery)

**Character state — Sören, Löwenritter Knight (Coord 4, End 3, Health 5, Wounds 0, Composure 6)**

#### Step 1: Initiative (M-039)
Pool: Coord 4D, TN7, Ob 1
Expected net: 4 × 0.33 = 1.32 | P(≥1 net) ≈ 80%
Most likely: Success → acts in Position 1

#### Step 2: Attack roll (M-001 + M-041)
Pool: 6D (Coord 4 + weapon bonus 2), TN7, Ob 2
Expected net: 6 × 0.33 = 2.0 | P(≥2 net) ≈ 70% | P(Overwhelming) ≈ 32%
Most likely: Success

#### Step 3: Wound application (M-002)
Damage = weapon rating (3) + net successes above Ob − defender armour (2)
At net 2: raw damage = 3 + 0 − 2 = 1 Wound
At net 4 (Overwhelming): raw damage = 3 + 2 − 2 = 3 Wounds

**Wound threshold interaction:**
| Wounds | Effect on M-001 |
|--------|----------------|
| 0–1 | No modifier |
| 2 | TN shifts to 8 (Desperate) |
| 3 | TN 8 + Ob +1 on all physical rolls |
| 4 | Incapacitated — no actions |
| 5 | Dead |

At 2 Wounds: 6D TN8, Ob 2 → P(die success) drops to 0.3 → expected net = 6 × 0.2 = 1.2
P(≥2 net at TN8, 6D) ≈ 30% vs 70% at TN7. **Cliff effect: one wound threshold halves attack effectiveness.**

#### Step 4: Condition attachment (M-007)
Rattled fires at: partial success on a violent action, or any wound while Composure < 3.
At Composure 6: Rattled requires explicit trigger (partial + violence).
At partial success (net 1, Ob 2): Rattled attaches. Effect: −1D on all social rolls, cannot spend Inspiration for remainder of scene.

**M-007 + M-006 interaction confirmed:** Inspiration spend blocked by Rattled. Characters cannot use Inspiration to reroll when Rattled — this is the primary function of the condition.

Unmask condition: fires when TS practitioner is observed performing Thread operation. Non-practitioner receives Unmask — removes one layer of cover identity. No mechanical test yet for Unmask → Circles interaction. **GAP: Unmask should reduce Circles rating — not specified.**

#### Step 5: Quick Rest (M-053)
Clears: Rattled (if scene ended without further violence), 1 Wound (if not Serious)
Full Rest: Clears all Conditions, heals all non-permanent Wounds

**M-053 + M-002 interaction:**
- Quick Rest cannot clear Wounds at level 3+ (Serious Wounds require Full Rest)
- Full Rest requires safe location + 6 hours fictional time
- No mechanic specifies what "safe" means — **GAP: Safe rest definition absent**

### Findings

**F-B7-01** (P2) — Wound/TN cliff: Moving from 1→2 Wounds drops attack success rate from ~70% to ~30% at standard 6D pool. Intended as escalating danger, but creates a "death spiral entry point" — once wounded, probability of further wounds increases, accelerating to incapacitation. No mechanic interrupts this spiral except Quick Rest (which requires the scene to pause).

**F-B7-02** (P3) — Unmask/Circles interaction unspecified. Unmask removes cover identity but no rule states whether this reduces Circles rating with the exposed faction. Flag for mechanic-audit.

**F-B7-03** (P3) — Safe rest definition absent. "Safe location" for Full Rest has no mechanical criteria. In active conflict zones this creates GM arbitration dependency.

---

## T-B7-02 — HISTORIES + BELIEFS + INSPIRATIONS + GRAND DEBATE
**Coverage:** M-003, M-004, M-006, M-037
**Mode:** TTRPG | **Temporal:** PAST/PRES | **Tracks:** TC,FSTAT,COMP,CERT | **Factions:** Church,Crown,Hafenmark | **NPCs:** Baralta,Himlensendt,Elske | **Archetypes:** Faction Leader,Devout Character

### Mode C — Full Scenario

**Setup:** Grand Debate — Parliament session. Baralta (Hafenmark, constitutional legalist) vs Himlensendt (Church, TC driver). Elske (Crown, player character) must navigate.

**Initial State:**
```
Elske — Coord 3, End 2, Health 5, Wounds 0, Composure 5
  Histories: [Scholar of Canon Law — +2D on ecclesiastical argument] [Crown Ward — +1D social with nobility]
  Beliefs: "Altonia's advance must be stopped through legitimate means" (active)
  Inspirations: 2

Baralta — Coord 3, End 4, Health 5, Wounds 0, Composure 6
  Histories: [Constitutional scholar — +2D on procedural argument]
  Beliefs: "Divine authority cannot supersede the Compiled Constitution" (active)

Himlensendt — Coord 2, End 5, Health 5, Wounds 0, Composure 7
  Histories: [Devoted since birth — +2D on theological argument] [Institutional authority — +1D when invoking Church precedent]
  Beliefs: "The Confessor's mandate is absolute within Valoria" (active)

Tracks: TC 45 | TT 28 | IP 22 | PI (Parliament Integrity) 6/10
```

### Grand Debate Resolution (M-037)

**Phase 1 — Opening Statements**
Each party states position. No roll; establishes Argument Frame.
- Himlensendt frames: theological necessity (Ob +1 to counter without ecclesiastical expertise)
- Baralta frames: procedural (Ob +1 to counter without legal expertise)
- Elske must address both frames.

**Phase 2 — Argument rolls**

**Himlensendt's argument (M-037):**
Pool: End 5 + Histories 2 + institutional authority 1 = 8D, TN7, Ob 3
Expected net: 8 × 0.33 = 2.64 | P(≥3 net) ≈ 60%

M-003 (Histories) integration: Histories add dice directly. A History must be narratively invoked — cannot be used twice in same scene for same argument. This caps Histories benefit at one use per scene per History.

M-006 (Inspirations) integration: Himlensendt can spend 1 Inspiration to add 3D to any single roll. This pushes pool to 11D → expected net 3.63 → P(≥3 net) ≈ 83%.

**Elske's counter (M-004 + M-003):**
Belief activation: "Altonia's advance must be stopped through legitimate means" — directly relevant. Belief invocation adds +2D on roll where Belief is tested.
Pool: End 2 + Scholar of Canon Law 2 + Crown Ward 1 + Belief 2 = 7D, TN7, Ob 3 (Himlensendt's frame Ob penalty applied)
Expected net: 7 × 0.33 = 2.31 | P(≥3 net) ≈ 45%

**M-004 CP award interaction:**
- If Elske argues *against* Belief: gains 1 CP (Belief tested under pressure)
- If Elske argues *for* Belief and succeeds: gains 1 CP (Belief affirmed)
- If Elske's Belief is contradicted by outcome: gains 2 CP (Belief challenged by narrative)

**State Delta after Phase 2:**
```
Himlensendt argument: Most likely Success (60%) → Composure of opposition reduced by 1
Elske counter: Most likely Partial (net ~2 vs Ob 3) → Goal partially achieved + complication
If Elske spends Inspiration: Pool 10D → P(≥3) ≈ 73% → Success probable
  After spend: Inspirations 1 remaining
```

**Phase 3 — Parliamentary Vote (M-036) trigger**
Grand Debate outcome determines coalition state entering vote:
- Himlensendt Success + Elske Partial: Church faction +1 Composure, Crown −1 Composure
- Coalition calculation: TC 45 (moderate Church influence), PI 6
- Vote requires PI ≥ 5 to proceed — met.

**M-036 + M-037 interaction:**
Grand Debate outcome shifts faction Composure which feeds into vote pool. No rule specifies: does Composure loss reduce vote dice? **GAP (already F80): coalition mechanics absent. This test confirms the gap is load-bearing — Grand Debate output has nowhere to go mechanically.**

**TC interaction:**
Himlensendt's successful theological argument: triggers TC +2 (institutional expansion)
At TC 47: approaching threshold (50 = Synod convenes). This is M-037 → M-031 escalation.

**M-004 CP awards from this scene:**
- Elske: Belief tested and partially upheld → 1 CP
- Baralta: Belief "Divine authority cannot supersede Constitution" directly challenged by Himlensendt Success → 2 CP (Belief challenged by narrative)

### Findings

**F-B7-04** (P2) — Inspirations spend timing unspecified. M-006 allows Inspiration spend to add 3D. No rule states: must this be declared before or after rolling? If after, this is a retroactive reroll mechanism, not a pre-roll boost. Significant probability difference. Needs explicit timing rule.

**F-B7-05** (P2) — Histories double-dipping. Multiple Histories can apply to same roll if narratively invoked. At character creation a player could build 3–4 applicable Histories for their specialty (e.g., ecclesiastical scholar with 4 relevant Histories = +8D). No cap specified. **P(Overwhelming) at 15D, Ob 2 = ~73%** — trivialises specialist arguments.

**F-B7-06** (P1) — Grand Debate → Parliamentary Vote handoff broken. M-037 outcome has no mechanical path to M-036 resolution. CP awards and Composure shifts from Grand Debate are computed but the coalition formation step for M-036 is absent (F80 confirmed as blocking). A full Parliament session cannot be run to completion.

**F-B7-07** (P3) — CP accumulation rate. In a single Grand Debate scene: Elske gains 1 CP, Baralta gains 2 CP. If debates are frequent (weekly in-game), CP accumulation rate may be high relative to spend rate. No data yet on CP spend menu size — cannot evaluate balance. Flag for tracking.

---

## T-B7-03 — KNOTS + LEAP + DIAGNOSIS + PULLING CHAIN
**Coverage:** M-010, M-013, M-014, M-016
**Mode:** TTRPG | **Temporal:** PRES/CROSS | **Tracks:** TS,TD,CERT,TT | **Factions:** Varfell | **NPCs:** Vaynard | **Archetypes:** Practitioner

### Mode B — Interaction Chain

**Chain:** Diagnosis (M-014) → Leap (M-013) → Pulling (M-016) → Knot formation (M-010)

**Practitioner state — Vaynard:**
```
TS 14, TD 4/20, Taint 2/10, Certainty 7/10, Contact: none
TT 28
```

#### Step 1: Diagnosis (M-014)
Vaynard examines a target location to identify Thread structure.
Pool: TS 14 → dice pool derived from TS. Rule: pool = TS/2 rounded down = 7D, TN7, Ob 2
Expected net: 7 × 0.33 = 2.31 | P(≥2 net) ≈ 70%

Success output: identifies Thread connections at location, gains 1 free die on subsequent Leap roll.
Partial output: incomplete picture — one connection missed, no Leap bonus.

**Diagnosis + Certainty (M-009):**
Certainty 7 is above threshold (5). Above 5: Diagnosis bonus applies.
If Certainty ≤ 5: −1D on Diagnosis. If Certainty ≤ 2: Diagnosis unavailable (cannot perceive Thread clearly).
**Certainty acts as gating condition on M-014.**

#### Step 2: The Leap (M-013)
Vaynard moves Thread-side to interact directly with the structure identified.
Pool: TS/2 + Diagnosis bonus (1D if successful) = 8D, TN7, Ob 2
Expected net: 8 × 0.33 = 2.64 | P(≥2 net) ≈ 82%

TD accumulation on Leap: +1 TD per Leap regardless of success. At TD 4, moving to TD 5.
**TD 5: first threshold. Effect: +1 to all Ob while Thread-side.**

Leap success: Vaynard is Thread-side, in Contact. Contact = 3 rounds before Automatic Return.

#### Step 3: Pulling (M-016)
Vaynard attempts to Pull a Thread connection — altering a relationship/memory/causation.
Pool: TS/2 = 7D, TN7, Ob 3 (standard Pull) — Ob 4 if TD ≥ 5 (threshold effect applies here)
At TD 5, Ob becomes 4.

Expected net at 7D, TN7, Ob 4: P(≥4 net) ≈ 20%
Expected net at 7D, TN7, Ob 3: P(≥4 net) ≈ 35% for Success, P(≥3 net) ≈ 55%

**Leap→Pull chain consequence:** The act of leaping (necessary for pulling) accumulates TD which immediately penalises the pull. This is an intentional cost but creates a compounding difficulty curve:

| TD before Leap | TD after Leap | Pull Ob | P(Success, 7D) |
|---------------|--------------|---------|----------------|
| 0–4 | 1–5 | 3 (if ≤4) or 4 (if 5) | ~55% or ~20% |
| 5–9 | 6–10 | 4 | ~20% |
| 10–14 | 11–15 | 5 | ~8% |
| 15–19 | 16–20 | 6 | ~2% |
| 20 | — | Coherence collapse | — |

**Cliff at TD 4→5:** P(Pull success) drops from 55% to 20%. This is a severe cliff — a practitioner at TD 4 should strongly consider not leaping, but the only way to Pull is via Leap. **This may be intentional design (increasing risk = increasing consequence) but the 35-point probability cliff is abrupt.**

On Partial Pull (net > 0 but < Ob): Pull partially succeeds — Thread altered but with unintended consequence. Side effect is GM-determined. No mechanic constrains what the side effect can be. **GAP: Partial Pull side effect scope undefined.**

**F25 (existing P1) confirmed:** At TS 14, pool 7D, a practitioner can Pull against social relationships. No counter-roll from the target. Affected NPC has no mechanical defense. This test confirms the gap — there is no resistance roll for the target of a Pull.

#### Step 4: Knot formation (M-010)
Knots form when: (a) Thread operations conflict with existing Thread structures, (b) Partial results on Thread ops accumulate at same location, (c) Forced Resolution creates Knot as byproduct.

In this chain: Partial Pull at same location as prior Diagnosis = Knot formation trigger.
Knot rating: 1 (minor) to 5 (structural).

**Knot effect on subsequent operations:**
- Ob +1 per Knot rating on Thread operations at that location
- Knots persist until cleared (requires Weaving at Ob = Knot rating)
- Knots are visible to any Diagnosis at the location

**M-010 + M-016 loop risk:** Pull attempts at Knotted location → higher Ob → more Partial results → more Knots → even higher Ob. **Potential infinite difficulty escalation.** Counter: Knot clearing (Weaving) interrupts the loop, but requires a separate scene and Thread-side access.

**TD state after full chain:**
TD 4 → 5 (Leap) → +1 if Pull fails (Forced Return) = TD 6 on failure path.
TD 6 → next Leap at Ob 4, Pull at Ob 4. P(Pull success 7D, Ob 4) = ~20%.

### Findings

**F-B7-08** (P1) — TD/Pull probability cliff at threshold 5 is functionally prohibitive. A practitioner who has used Thread operations 5+ times (TD ≥ 5) has a ~20% Pull success rate at standard Ob 3. This may make mid-to-late campaign Thread operations nearly non-functional without TS advancement. No mechanic for TD recovery found. **If TD is permanent/session-persistent without recovery, practitioners become progressively useless. Requires mechanic-audit.**

**F-B7-09** (P2) — Partial Pull side effect scope undefined. GM has unlimited latitude on consequence. Inconsistent across GMs/tables. Should have a bounded effect list or severity framework.

**F-B7-10** (P2) — Knot escalation loop. Repeated failed operations at same location create a Knot spiral. Self-limiting in that practitioners will avoid the location, but if plot requires action at that location, the system may produce an impassable obstacle. Needs a maximum Knot rating cap or a Weaving shortcut mechanic.

**F-B7-11** (P3) — Diagnosis Certainty gate is not symmetric with other Thread ops. Diagnosis requires Certainty ≥ 3 to function. Leap and Pull have no Certainty gate. A practitioner with Certainty 2 can still Leap and Pull blind — arguably worse narratively than being unable to Diagnose.

---

## T-B7-04 — CIRCLES + RESOURCES + FACTION STATS + DOMAIN ACTIONS
**Coverage:** M-011, M-012, M-034, M-035
**Mode:** TTRPG/BG | **Temporal:** PRES/CROSS | **Tracks:** FSTAT,TT,IP | **Factions:** Guilds,Crown,Revolution | **NPCs:** — | **Archetypes:** Faction Leader

### Mode B — Interaction Chain

**Chain:** M-011 (Circles) → M-012 (Resources) → M-035 (Domain Actions) → M-034 (Faction Stats)

**Setup:** Guild Master Pieta attempts to leverage merchant network (Circles) to fund a covert Domain Action that improves Guild Wealth.

**Initial State:**
```
Pieta — Coord 3, End 3
  Circles: Merchant Network 4, Underworld 2
  Resources: 3

Guilds faction: M(Mandate) 5, I(Influence) 4, W(Wealth) 6, Mi(Military) 2, In(Intelligence) 3, S(Stability) 7
Tracks: TT 28 | IP 22
```

#### Step 1: Circles call (M-011)
Pieta contacts Merchant Network to identify a trade opportunity.
Pool: Circles rating 4 + End 3 = 7D, TN7, Ob 2
Expected net: 7 × 0.33 = 2.31 | P(≥2 net) ≈ 70%

Success: Contact established, +1D on related Domain Action roll this season.
Partial: Contact established, complication (cost, obligation, or rival awareness).
Failure: Contact burned — Circles rating drops by 1 for that network.

**Circles depletion mechanic:** Failed Circles roll reduces rating. At Circles 1, failure = network lost (rating 0). Recovery requires spending CP or fictional time. **Circles functions as a consumable resource, not a stable attribute.**

#### Step 2: Resources expenditure (M-012)
Funding the Domain Action requires Resources 2 spend.
Pieta has Resources 3 → after spend: Resources 1.
Resources 1 = constrained. Next Resources call: Ob increases by 1.

**M-012 + M-011 interaction:** If Circles call produced a complication (obligation), that obligation may manifest as Resources drain on future turns. No mechanic specifies when obligations resolve — **GAP: Circles obligation resolution timing absent.**

#### Step 3: Domain Action (M-035)
Action type: Covert Trade Expansion (Intelligence-assisted Wealth gain).
Pool: Guild Intelligence 3 + Circles bonus 1D (from Step 1 success) = 4D, TN7, Ob 2
Expected net: 4 × 0.33 = 1.32 | P(≥2 net) ≈ 50% | P(Partial) ≈ 30% | P(Failure) ≈ 20%

Success: Wealth +1. Intelligence stat used but not depleted.
Partial: Wealth +1, but rival faction (Crown or Revolution) gains awareness — IP effect.
Failure: Action fails, Resources spend wasted, potential exposure.

**Domain Action pool construction issue:** Pool is faction stat (Intelligence 3) + situational bonus (Circles 1D). No character attribute contributes. This means Domain Actions are entirely faction-stat-driven — individual character skill is irrelevant unless a Circles or Resources bonus applies. **GAP: No pathway for character advancement (TS, Histories, Beliefs) to meaningfully contribute to Domain Actions.**

#### Step 4: Faction Stat update (M-034)
Wealth 6 → 7 on success.
**Wealth 7 threshold check:** At Wealth ≥ 7, does any threshold fire? Matrix entry F112 addressed Church Stability/TC interaction. Checking Guild Wealth threshold: no threshold defined for Wealth 7. Thresholds documented for: TC (50, 75, 100), TT (30, 45, 60), IP (20, 40, 60). **GAP: Faction stat thresholds absent.** What happens when Wealth hits 10? When Military hits 0? No consequences defined.

**M-034 + M-035 compound action test (BG mode):**
In BG mode, Domain Actions are resolved at the faction card level without character involvement. Pool = faction stat only. This means BG mode Domain Actions have no situational modifiers — pure stat rolls. Circles and Resources mechanics are TTRPG-only constructs that don't translate to BG. **No BG equivalent for Circles or Resources mechanics confirmed.**

### Findings

**F-B7-12** (P1) — Faction stat thresholds absent. No mechanic defines consequences when faction stats reach extremes (0 or max). Wealth 10 should trigger something (monopoly? faction dominance?). Military 0 should trigger something (faction collapse? annexation?). Without thresholds, faction stats are inert numbers with no escalation function. This is a structural gap equivalent to F112 in scope.

**F-B7-13** (P2) — Character skill irrelevant to Domain Actions. Individual character abilities (Histories, TS, Beliefs) have no mechanical pathway to Domain Action pools. This decouples character play from faction play entirely — the GM can resolve all faction turns without any player character involvement. Likely unintended.

**F-B7-14** (P2) — Circles obligation resolution absent. Partial Circles results create obligations with no mechanic for when or how they resolve. Obligations accumulate with no discharge mechanic.

**F-B7-15** (P3) — BG/TTRPG translation gap for social capital. Circles and Resources are TTRPG character mechanics with no BG equivalent. In hybrid play, when the game shifts to BG mode, these assets vanish. No rule for converting Circles rating to faction stat contribution.

---

## T-B7-05 — PULLING + FR-LOCK + FR-DISSOLUTION + COHERENCE CASCADE
**Coverage:** M-016, M-017, M-018, M-021
**Mode:** TTRPG | **Temporal:** CROSS | **Tracks:** TS,TD,TT,CERT,ThS | **Factions:** Varfell,Crown | **NPCs:** Vaynard | **Archetypes:** Practitioner

### Mode B+D — Interaction Chain + Edge Cases

**Chain:** Pull (M-016) fails → FR-Lock (M-017) attempted as containment → FR-Lock fails → FR-Dissolution (M-018) as last resort → Coherence degradation (M-021)

**Practitioner state — Vaynard (advanced, high-TD scenario):**
```
TS 16, TD 12/20, Taint 4/10, Certainty 5/10
TT 35
```

#### Pull attempt (M-016) at high TD
Pool: TS/2 = 8D, TN7, Ob 3 → but TD 12: threshold passed (TD 10 = Ob +2)
Effective Ob: 5
P(≥5 net, 8D, TN7) ≈ 8%
Most likely: Failure.
Failure consequence: Uncontrolled Thread alteration. Thread structure destabilises. TT +2.

#### FR-Lock attempt (M-017)
Vaynard attempts to Lock the destabilised Thread structure before it propagates.
Pool: TS/2 = 8D, TN7, Ob 3 → TD threshold: Ob 5
P(≥5 net, 8D) ≈ 8%
Most likely: Failure.
**FR-Lock failure consequence:** Lock fails, Thread structure continues to unravel. TT +3 (lock failure is worse than non-attempt). Certainty −1 (5 → 4).

**Certainty 4 effect:** Below 5 → −1D on all Thread operations. Pool drops to 7D.

#### FR-Dissolution attempt (M-018)
Dissolution destroys the Thread structure entirely — preventing propagation at cost of permanent loss.
Pool: TS/2 − 1D (Certainty penalty) = 7D, TN7, Ob 4 → TD threshold: Ob 6
P(≥6 net, 7D, TN7) ≈ 2%
**Near-impossible.**

**Dissolution partial outcome:** Partial Dissolution = structure partially destroyed. Residue remains (M-022 triggered). TT +4.

**TT state after cascade:**
TT 35 → +2 (Pull fail) → +3 (Lock fail) → +4 (Dissolution partial) = TT 44
TT 44 approaches threshold 45. At TT 45: threshold fires (per existing test data from B3-005).

**Coherence track (M-021):**
Each failed Thread op at high TD: Coherence −1 per failure.
Starting Coherence: 7 (assumed)
After cascade: 7 → 6 (Pull fail) → 5 (Lock fail) → 4 (Dissolution partial) = Coherence 4
Coherence 4: approaching threshold 3 (Intelligibility degradation begins).

**TD state:**
TD 12 → 13 (attempted Leap for Pull) → 14 (Lock requires Thread-side) → 15 (Dissolution)
TD 15: threshold (TD 15 = Ob +3 total). All Ob now +3.
Next operation Ob = base Ob + 3. Even Ob 1 becomes Ob 4. P(≥4 net, 7D) = ~20%.

### Mode D — Edge Cases

**Edge Case — Terminal cascade:**
At TD 18+, Certainty ≤ 2, Coherence ≤ 2:
- All Thread ops at Ob 6+ (base 3 + threshold 3)
- P(success, 7D, Ob 6) ≈ 2%
- Certainty ≤ 2: Diagnosis unavailable
- Coherence ≤ 2: Intelligibility degraded (cannot communicate clearly)
- Practitioner is functionally locked out of Thread operations
- No mechanic for recovery from this state found

**Is there a recovery path from TD 18?** No TD recovery mechanic identified in any batch. This is a one-way ratchet. A practitioner who over-extends reaches an irrecoverable state. **Intended as permanent consequence? Or oversight?**

**Edge Case — TT spiral from cascade:**
A single 3-step cascade (Pull fail → Lock fail → Dissolution partial) adds TT +9.
If this occurs at TT 36, it pushes to TT 45 (threshold). At TT 45, what fires? Per B3 data: TT 45 = "Thread Tension critical — worldwide phenomena begin manifesting." This means a single practitioner's failed cascade can trigger a global threshold. **At TT 35+ (moderate campaign), one botched operation sequence = world crisis. Frequency: possible in any session with high-TD practitioners.**

### Findings

**F-B7-16** (P1) — No TD recovery mechanic. TD is a one-way accumulator with no discharge. A practitioner reaching TD 15+ is permanently impaired. If this is intentional (Thread use has permanent costs), it needs explicit statement. If not, a recovery mechanic is needed.

**F-B7-17** (P1) — Single practitioner cascade can trigger global TT threshold. TT +9 from one failed 3-op sequence at TT 36+ crosses TT 45 threshold. This gives a single practitioner the ability to trigger world-level consequences through failure alone — no intent required. Needs a TT gain cap per session or per practitioner.

**F-B7-18** (P2) — Coherence terminal state has no exit. Coherence ≤ 2 = Intelligibility degraded. No mechanic for recovering Coherence found. Like TD, appears to be a one-way ratchet. Confirm intent.

**F-B7-19** (P3) — FR-Lock failure penalty exceeds non-attempt. Attempting Lock and failing adds TT +3 vs TT +2 for not attempting. Perverse incentive: at low success probability, not attempting Lock is mechanically superior to attempting it. A rational practitioner at TD 12+ should never attempt FR-Lock. This removes the mechanic from high-TD play entirely.

---

## T-B7-06 — COHERENCE + DISSOLUTION RESIDUE + KNOTS + PULLING
**Coverage:** M-021, M-022, M-010, M-016
**Mode:** TTRPG | **Temporal:** CROSS/PRES | **Tracks:** TD,TS,TT,ThS,CERT | **Factions:** Niflhel,Varfell | **NPCs:** Vaynard | **Archetypes:** Practitioner

### Mode B — Interaction Chain

**Chain:** Dissolution (M-018) → Residue (M-022) → Knot formation (M-010) → Coherence degradation (M-021) → Pull attempt on Knotted structure (M-016)

**This test maps the aftermath state of T-B7-05 into subsequent operations.**

**State entering test:**
```
Vaynard — TS 16, TD 15, Taint 5/10, Certainty 4, Coherence 4
TT 44 | ThS 12
Location has: Dissolution Residue (rating 2), Knot (rating 2 from prior partial ops)
```

#### Dissolution Residue effect (M-022)
Residue at rating 2: all Thread ops at this location +1 Ob (stacks with TD threshold Ob).
Residue persists until: ThS drops at location (natural decay) or Weaving removes it.

**Residue + Knot stacking:**
Knot rating 2: +2 Ob on Thread ops at location.
Residue rating 2: +1 Ob.
TD 15 threshold: +3 Ob.
**Total effective Ob modifier at this location: +6 on top of base Ob.**
Pull at this location: base Ob 3 + 6 = Ob 9. P(≥9 net, 8D, TN7) ≈ 0%.

**This location is mechanically inaccessible to Vaynard.** Any operation here fails with ~100% probability.

**Coherence track at 4 (M-021):**
Coherence 4: no penalty yet (threshold at 3).
If any operation here produces another failure: Coherence −1 → 3 → Intelligibility threshold fires.
At Coherence 3: Vaynard begins losing ability to communicate Thread perceptions to others. Mechanically: −2D on any roll to explain, instruct, or coordinate Thread-related actions.

**ThS interaction (M-020):**
ThS 12 (world track). Location's local Thread Sensitivity is elevated due to Residue and Knots.
High local ThS: increases chance that non-practitioners at location notice something is wrong (TS passive detection check, Ob = 10 − local ThS/2 = 10 − 6 = Ob 4).
Non-practitioner detection at location: any character with TS ≥ 1 rolls TS/2 vs Ob 4 passively. Low probability but possible.

**Pull on Knotted structure — theoretical maximum:**
If Vaynard somehow cleared the Knot (Weaving, Ob 2, separate scene) and Residue (Weaving, Ob 2):
Effective Ob would drop back to 3 + TD modifier 3 = Ob 6. P(≥6 net, 8D) ≈ 2%. Still near-impossible.

**The only path forward for Vaynard at this location:**
1. Clear Knot (Weaving, separate scene, different location)
2. Clear Residue (Weaving, different location)
3. Allow TD to... not recover (no recovery mechanic)
4. Accept that this location is permanently inaccessible to this practitioner

**This constitutes a permanent geographic block on a specific practitioner.** Narratively meaningful but mechanically absolute. No partial access, no degraded access — binary inaccessibility.

### Findings

**F-B7-20** (P2) — Location accessibility is binary at high accumulated difficulty. Stacked Ob modifiers (TD + Knot + Residue) can make a location entirely inaccessible to a specific practitioner. This is absolute — there is no "attempt at extreme difficulty" option because the effective Ob exceeds any realistic pool. Locations can be permanently locked out for specific practitioners. Narratively interesting but may strand plot if a plot-critical location becomes inaccessible.

**F-B7-21** (P3) — Knot + Residue clearing requires separate location. To clear Knots/Residue at location X, Weaving must be performed Thread-side. But if reaching Thread-side at location X requires a Leap which has near-zero probability due to accumulated modifiers, the practitioner cannot clear the location. **Catch-22: clearing the location requires accessing the location which requires clearing it first.** Needs a mechanic for off-site Thread maintenance or proxy clearing.

---

## T-B7-07 — FACTION STATS + DOMAIN ACTIONS + SEASONAL ACCOUNTING + THEOCRACY CLOCK
**Coverage:** M-034, M-035, M-038, M-031
**Mode:** TTRPG/BG | **Temporal:** FUT/CROSS | **Tracks:** FSTAT,TC,TT,IP | **Factions:** Church,Crown,Hafenmark,Revolution | **NPCs:** Himlensendt | **Archetypes:** Faction Leader

### Mode C — Full Seasonal Cycle

**Setup:** End-of-season resolution. Four factions take Domain Actions; then Seasonal Accounting.

**Initial State:**
```
Church:    M 7, I 6, W 5, Mi 4, In 5, S 8
Crown:     M 6, I 7, W 6, Mi 5, In 4, S 6
Hafenmark: M 4, I 5, W 8, Mi 3, In 4, S 7
Revolution:M 3, I 4, W 3, Mi 4, In 6, S 4

Tracks: TC 48 | TT 32 | IP 18
```

#### Phase 1 — Domain Actions (M-035)

**Church — Theological Expansion (TC driver):**
Pool: Mandate 7, TN7, Ob 2 → Expected net: 7 × 0.33 = 2.31 | P(≥2) ≈ 70%
Success: Influence +1 (7), TC +3 (→ 51). TC 51 crosses threshold 50.
**TC 50 threshold fires: Synod convened.** Effect: Church gains +2 Mandate for duration of Synod (season). Church Mandate: 7 → 9.

**Crown — Intelligence Gathering on Revolution:**
Pool: Intelligence 4, TN7, Ob 2 → Expected net: 1.32 | P(≥2) ≈ 50%
Success: Revolution Intel exposed — Revolution Intelligence −1 (5). Crown gains awareness of Revolution network node.
Partial: Partial intelligence — Crown gains awareness but Revolution knows they're being watched. IP +2 (→ 20).

**Hafenmark — Trade Route Expansion:**
Pool: Wealth 8, TN7, Ob 2 → Expected net: 2.64 | P(≥2) ≈ 82%
Success: Wealth +1 (9). **Wealth 9 — no threshold defined (confirms F-B7-12).**
Also: IP −1 (→ 19) — trade routes reduce political tension.

**Revolution — Covert Recruitment:**
Pool: Intelligence 6, TN7, Ob 2 → Expected net: 1.98 | P(≥2) ≈ 70%
Success: Military +1 (5). Crown's intelligence action this season: does it counter?
**Simultaneous action conflict:** Crown's intel success revealed Revolution's network. Does this retroactively cancel Revolution's recruitment? No mechanic specifies simultaneous action ordering or interference. **GAP: Domain Action sequencing and interference rules absent.**

#### Phase 2 — Seasonal Accounting (M-038)

**Upkeep costs (all factions):**
Each faction pays upkeep = sum of all stats ÷ 6 (rounded down) in Resources equivalent.
Church: (7+6+5+4+5+8) = 35 ÷ 6 = 5 Wealth drain
Crown: (6+7+6+5+4+6) = 34 ÷ 6 = 5 Wealth drain
Hafenmark: (4+5+9+3+4+7) = 32 ÷ 6 = 5 Wealth drain
Revolution: (3+4+3+5+5+4) = 24 ÷ 6 = 4 Wealth drain

**Post-upkeep Wealth:**
Church: 5 − 5 = 0. **Church Wealth hits 0.**
**Wealth 0: faction cannot fund Domain Actions next season. Church is economically paralysed.**

**Anti-death-spiral mechanic (F83):** The anti-death-spiral floor raises Ob to 4 on recovery actions. Church attempting to recover Wealth: base Ob 2, floor Ob 4 — P(≥4 net, Mandate 9, TN7) = 9D → P(≥4) ≈ 55%. Functional but harsh. **F83 confirmed: the floor inverts intent by making recovery rolls harder than standard actions.** A faction at Wealth 0 trying to recover faces Ob 4 instead of Ob 2. This is counterproductive.

**Church Mandate 9 (Synod bonus):** Mandate 9 → Domain Action pools now 9D. But Church has Wealth 0 — cannot execute costly Domain Actions. Synod bonus is available but economically non-executable. **High Mandate + zero Wealth = mechanically constrained powerhouse.**

**Crown:** Wealth 6 − 5 = 1. Constrained but functional.
**Hafenmark:** Wealth 9 − 5 = 4. Healthy.
**Revolution:** Wealth 3 − 4 = −1. **Negative Wealth.** No rule for negative Wealth. Is this possible? Does it round to 0? Does it trigger something? **GAP: Negative faction stat behavior undefined.**

**M-038 + M-034 seasonal update:**
After accounting, faction stat floors need checking. No floor defined for stats (F-B7-12 confirmed). Stats can theoretically reach 0 (and below per Revolution Wealth above).

**TC post-threshold state:**
TC 51, Synod active. Duration of Synod: not specified. **GAP: Synod duration mechanics absent.** Does it last 1 season? Until TC drops below 50? Until player action resolves it?

### Findings

**F-B7-22** (P1) — Negative faction stat undefined. Revolution Wealth −1 is reachable in normal play (low Wealth faction with average upkeep). No rule for what happens. Stat floor of 0 is assumed but not stated. Needs explicit definition.

**F-B7-23** (P1) — Domain Action sequencing absent. Simultaneous Domain Actions from opposing factions with interfering effects have no priority or sequencing rule. Crown intel vs Revolution recruitment is a direct conflict with no resolution mechanic. In BG mode this is particularly acute — all factions act simultaneously.

**F-B7-24** (P2) — Synod duration undefined. TC threshold at 50 triggers Synod but no mechanic specifies duration or resolution conditions. Synod is a sustained state with no exit criteria.

**F-B7-25** (P2) — High upkeep creates structural Church poverty. At standard stat values, Church Wealth hits 0 after one seasonal cycle if Wealth starts at 5. Church is designed to have high Mandate/Influence (theological power) but low Wealth — this may be intentional faction design. However, economic paralysis on turn 1 of any campaign is a P2 play experience issue.

---

## T-B7-08 — DAMAGE FORMULA + EQUIPMENT + MANOEUVRES + WOUNDS + INITIATIVE
**Coverage:** M-042, M-043, M-044, M-002, M-039
**Mode:** TTRPG | **Temporal:** PRES | **Tracks:** — | **Factions:** Löwenritter,Crown | **NPCs:** Ehrenwall | **Archetypes:** Löwenritter Knight,Generic

### Mode C — Full Combat Resolution

**Setup:** Ehrenwall (Löwenritter, sword + plate) vs Church Knight Templar (mace + chainmail). Single combat, 3 rounds.

**Characters:**
```
Ehrenwall — Coord 5, End 4, Health 6, Wounds 0, Composure 5
  Weapon: Longsword (Dmg 3, Reach Long, TN7)
  Armour: Plate (Armour 3, Encumbrance 1)

Church Templar — Coord 4, End 3, Health 5, Wounds 0, Composure 5
  Weapon: Mace (Dmg 4, Reach Short, TN6 — Weapon TN)
  Armour: Chainmail (Armour 2, Encumbrance 1)
```

**Encumbrance effect (M-043):** Encumbrance 1 = −1D on Agility/Evasion rolls. Both fighters affected.

#### Round 1 — Initiative (M-039)
Ehrenwall: Coord 5D, TN7, Ob 1 → P(≥1) ≈ 93%
Templar: Coord 4D, TN7, Ob 1 → P(≥1) ≈ 88%
**Both likely succeed.** Tie resolution: no tiebreaker mechanic defined. **GAP: Initiative tie resolution absent.**

Assuming Ehrenwall wins initiative (higher Coord).

#### Round 1 — Ehrenwall attacks (M-041 + M-042)
**Reach interaction (M-043):** Ehrenwall Long reach vs Templar Short reach. Long vs Short: Long reach fighter gets +1D on first attack in engagement. Ehrenwall: Coord 5 + Long reach bonus 1 = 6D.
Pool: 6D, TN7 (Longsword TN), Ob 2 (vs armoured opponent)
P(Overwhelming): ~32% | P(Success): ~38% | P(Partial): ~24% | P(Failure): ~6%
Expected net: 1.98

**Damage calculation (M-042):**
Base formula: Weapon Dmg + net successes above Ob − target Armour
At net 2 (Success, Ob 2): 3 + 0 − 2 = 1 Wound to Templar
At net 4 (Overwhelming): 3 + 2 − 2 = 3 Wounds to Templar

**Manoeuvre option (M-044):** Instead of attacking, Ehrenwall could attempt Disarm.
Disarm: Ob 3, success = opponent drops weapon. Higher Ob than attack (Ob 2) but no counter-attack risk.
Pool: 6D, TN7, Ob 3 → P(≥3 net) ≈ 45%.
**Manoeuvre is suboptimal vs direct attack at similar probability.** Disarm only becomes optimal when you want to avoid killing (moral/political constraint) or when enemy Armour is high enough that damage is unreliable.

#### Round 1 — Templar counter (M-041)
Reach disadvantage (Short vs Long): −1D on first attack vs Long reach opponent.
Pool: Coord 4 − 1 = 3D, TN6 (Mace TN), Ob 2
P(die success at TN6) = 0.5, P(net success per die) ≈ 0.4
3D × 0.4 = expected net 1.2 | P(≥2 net) ≈ 45%

**Mace vs Plate armour:** Mace Dmg 4, Plate Armour 3.
At net 2 (Success): 4 + 0 − 3 = 1 Wound to Ehrenwall.
**Both fighters dealing 1 Wound per round at most likely outcome.**

#### Round 2 — State with 1 Wound each
```
Ehrenwall — Wounds 1 (no modifier yet, threshold at 2)
Templar — Wounds 1 (no modifier yet)
```
Same pools, same outcomes likely. After Round 2: Wounds 2 each.

#### Round 2 — Wounds 2 threshold fires
**Both fighters simultaneously hit threshold 2 → TN shifts to 8.**
Ehrenwall: 6D, TN8 → P(die success) = 0.3 → expected net 6 × 0.2 = 1.2 → P(≥2 net) ≈ 35%
Templar: 3D, TN8 → expected net 3 × 0.2 = 0.6 → P(≥2 net) ≈ 20%

**At TN8, Templar is frequently failing.** Damage output drops. At Failure, no wound dealt.
Ehrenwall maintains meaningful attack probability; Templar degrades faster.

#### Round 3 — Ehrenwall attacks at Wounds 2, TN8
If Ehrenwall Success (35%): 1 Wound → Templar at Wounds 3 (Ob +1 stacks).
Templar at Wounds 3: TN8 + Ob +1 → Attack pool 3D, TN8, Ob 3 → P(≥3 net) ≈ 5%.
**Templar is effectively non-functional at Wounds 3.** Fight is over.

**Average fight duration: ~3 rounds.** Ehrenwall wins with Wounds 2–3.

**Equipment edge cases (M-043):**
- Two Long-reach fighters: reach bonus cancels out, no modifier.
- Weapon TN vs armour: Mace TN6 vs Plate — higher hit chance but lower damage net due to high Armour. Sword TN7 vs Chainmail — lower hit chance but higher damage net. Math: both produce similar average wounds per round (~0.6). Equipment choice is preference/style, not dominant strategy. **Good design.**

### Findings

**F-B7-26** (P2) — Initiative tie resolution absent. Two fighters with same Coord or both succeeding initiative have no mechanic to determine order. High frequency gap — occurs in any symmetric combat.

**F-B7-27** (P3) — Manoeuvres are mechanically suboptimal vs attacks in almost all cases. Higher Ob, same pool, no direct damage. Only valuable in specific narrative constraints. May lead to Manoeuvres being unused in most play. Not a break but a design note.

**F-B7-28** (P3) — Death spiral symmetry in paired combat. When both fighters hit Wound threshold simultaneously (common at equal skill levels), both degrade at the same rate. The fight can last 2 more rounds with both fighters at near-failure probability. Creates a "last one standing" feel which may be intentional.

---

## T-B7-09 — MASS COMBAT + INITIATIVE + PRIORITY TABLE + WOUNDS
**Coverage:** M-045, M-039, M-040, M-002
**Mode:** BG/HYB | **Temporal:** PRES/FUT | **Tracks:** FSTAT,TT | **Factions:** Löwenritter,Crown,Church | **NPCs:** Ehrenwall | **Archetypes:** Löwenritter Knight,Faction Leader

### Mode C — Mass Combat Resolution

**Setup:** Löwenritter force (500 cavalry, Military 5) vs Church Templars (800 infantry, Military 6). Ehrenwall commands Löwenritter.

**Initial State:**
```
Löwenritter: Mi 5, casualties 0%, morale 8/10
Church:      Mi 6, casualties 0%, morale 8/10
TT 32
```

#### Mass Combat pool construction (M-045)
Per existing data (F100): mass combat damage formula not specified. This test confirms and attempts to reconstruct from surrounding mechanics.

**Reconstructed from context:**
Pool: Military stat + commander bonus (Ehrenwall Coord 5 → +2D in mass combat command)
Löwenritter pool: Mi 5 + command 2 = 7D, TN7, Ob 3 (vs fortified enemy, +1 Ob for Church defensive formation)
Church pool: Mi 6, TN7, Ob 2 (defending)
Expected net Löwenritter: 7 × 0.33 = 2.31 | P(≥3 net) ≈ 45%
Expected net Church: 6 × 0.33 = 1.98 | P(≥2 net) ≈ 70%

**Damage output (unspecified — F100):** Cannot calculate actual casualty numbers. Proceeding with structural analysis only.

#### Priority Table in Mass Combat (M-040)
Individual priority table: Speed → Reach → Weapon type → Ob modifier.
In mass combat: how does Priority Table apply? Unit type should determine who acts first.
Cavalry (Löwenritter): high Speed, Long Reach → should get Priority 1.
Infantry formation (Church Templars): lower Speed, Short Reach → Priority 2.

**M-040 + M-045 interaction:** No rule found specifying whether individual Priority Table maps to mass combat. In BG mode, this likely resolves at unit-type level, not individual level. **GAP: Mass combat priority/sequencing uses individual combat tables without BG-level adaptation.**

#### Initiative in Mass Combat (M-039)
Individual initiative = Coord roll.
Mass combat initiative: should be commander Coord + unit Speed modifier.
Ehrenwall Coord 5 → 5D, TN7, Ob 1 → P(success) ≈ 93%. Löwenritter likely acts first.

**M-039 + M-045 gap:** Initiative in mass combat is resolved by commander's individual roll, not unit stats. A high-Coord commander always wins initiative regardless of unit composition. **Cavalry commander vs slow infantry: Coord 5 vs 3. Ob 1 both. P(both succeed) high. No meaningful differentiation.**

#### Wounds in Mass Combat (M-002)
Individual Wounds track: 0–5 for a character.
Mass combat casualties: percentage-based? Absolute unit count? No mechanic found.
Ehrenwall in mass combat: takes Wounds if personally engaged. 1 Wound per successful enemy attack that penetrates.
**M-002 in mass combat: individual wound rules apply to commanders but there is no equivalent for unit degradation. Units either win or lose — no attrition modelled at the unit level.**

#### TT interaction
Decisive battle (either side achieves Overwhelming): TT −3 (violence concentrated and resolved).
Prolonged battle (multiple rounds, neither side achieving overwhelming): TT +1 per round.
At TT 32 + 3 rounds of prolonged combat: TT 35. Approaching threshold 36 (not defined in current data).

### Findings

**F-B7-29** (P1) — Mass combat damage formula absent (F100 confirmed). Cannot determine casualties, battle duration, or outcome probability without it. The mechanic exists as a name but has no resolution procedure. All mass combat outcomes are GM-determined until this is specified.

**F-B7-30** (P2) — Unit attrition mechanics absent. Mass combat has no modelling of gradual unit degradation. Units are at full strength until they lose, then eliminated. No morale failure cascade, no retreat mechanic, no partial victory. All-or-nothing resolution.

**F-B7-31** (P2) — Individual Priority Table not adapted for mass combat. BG mode presumably operates at unit level, but no unit-level priority table exists. Individual speed/reach doesn't translate to unit-type advantage.

---

## T-B7-10 — THREAD OPS IN COMBAT + MANOEUVRES + MASS COMBAT + INITIATIVE
**Coverage:** M-046, M-044, M-045, M-039
**Mode:** TTRPG/HYB | **Temporal:** CROSS | **Tracks:** TT,ThS,CERT,TS | **Factions:** Revolution,Löwenritter | **NPCs:** — | **Archetypes:** Practitioner,Löwenritter Knight

### Mode B — Interaction Chain

**Chain:** Initiative (M-039) → Thread operation during combat round (M-046) → Manoeuvre triggered by Thread effect (M-044) → Escalation to mass combat (M-045)

**Characters:**
```
Practitioner Rada — TS 10, TD 6, Certainty 7, Coord 3, End 3
Löwenritter Opponent — Coord 5, End 4, Wounds 0
TT 30 | ThS 10
```

#### Step 1: Initiative with Thread operation declared (M-039 + M-046)
Rada declares Thread operation instead of physical attack.
**Initiative priority:** Does a Thread operation occur before, during, or after physical actions in the round?
No rule found specifying Thread op timing relative to physical combat. **GAP: Thread operation timing in combat round absent.** Assuming Thread ops resolve at start of round (before physical).

#### Step 2: Thread operation — Weaving to create obstacle (M-046)
Rada attempts to Weave a Thread barrier disrupting the opponent's attack.
Pool: TS/2 = 5D, TN7, Ob 2 → TD 6 threshold (TD 5 = Ob +1) → Ob 3
P(≥3 net, 5D, TN7) ≈ 25%

On success: Opponent's attack Ob +1 this round (Woven obstacle).
On partial: Obstacle created but Rada exposed (opponent knows she's a practitioner → Unmask trigger).
On failure: No effect; Rada loses her combat action for the round.

**Thread op cost in combat:** TD +1 regardless of outcome. At TD 6 → 7 (threshold already crossed, no new threshold at 7).

**M-046 + M-044 interaction (Manoeuvre):**
If Thread Weaving succeeds, opponent attempts Disarm manoeuvre as counter (narratively: lunging through the Thread disruption).
Opponent pool: Coord 5D, TN7 (standard), Ob 3 (Disarm) → P(≥3 net) ≈ 45%. But Thread Weaving adds Ob +1 → Ob 4 → P(≥4 net, 5D) ≈ 25%.
**Thread Weave as combat modifier is meaningful but not dominant.** Reduces opponent success rate from 45% to 25%.

#### Step 3: Escalation to mass combat (M-045)
Scenario: Thread operation triggers wider conflict — practitioner reveals herself, both faction forces engage.
**Hybrid mode trigger:** Individual TTRPG scene escalates to BG-level mass combat.
- TTRPG round → BG turn: how does individual combat state carry over?
- Rada's active Thread operation: does it persist into mass combat? No rule found.
- **GAP: TTRPG individual state (wounds, conditions, active Thread ops) handoff to BG mass combat undefined.**

**TT interaction:**
Thread operation in combat: TT +1 (Thread op without Dissolution = ambient Thread activity).
Escalation to mass combat: no TT effect specified for battle initiation. TT effects from mass combat: per T-B7-09 findings.

ThS at location: ThS 10 → after Thread op: ThS +1 (11). Passive detection Ob for non-practitioners drops to Ob 4.5 → Ob 4. Increasing chance that Löwenritter troops detect something anomalous.

### Findings

**F-B7-32** (P2) — Thread operation timing in combat round undefined. No initiative priority for Thread ops vs physical actions. Ambiguity about whether Thread Weaving before an attack prevents or merely modifies the attack.

**F-B7-33** (P2) — TTRPG→BG state handoff undefined. When individual combat escalates to mass combat, no rule governs: what happens to character Wounds, Conditions, active Thread operations, or Certainty in the mass combat context.

---

## T-B7-11 — THREAD EVENTS IN SOCIAL + CIRCLES + GRAND DEBATE + THEOCRACY CLOCK
**Coverage:** M-047, M-011, M-037, M-031
**Mode:** TTRPG | **Temporal:** CROSS | **Tracks:** TT,TS,CERT,TC,FSTAT,IP | **Factions:** Church,Crown,Hafenmark | **NPCs:** Himlensendt,Almud,Baralta | **Archetypes:** Practitioner,Faction Leader,Devout Character

### Mode C — Full Scenario

**Setup:** Parliament debate (M-037) interrupted by spontaneous Thread event (M-047). Himlensendt interprets it as divine sign; Almud recognises it as Thread activity; Baralta is disturbed.

**Initial State:**
```
Almud — TS 8, Certainty 6, Coord 3, Composure 5
  Circles: Parliament 5, Crown Court 4
Himlensendt — TS 0 (Devout: no Thread perception), Composure 7
Baralta — TS 2 (constitutional legalist, minimal Thread sensitivity)
TC 48 | TT 30 | IP 17
```

#### Step 1: Grand Debate in progress (M-037)
Church motion: expand Confessor jurisdiction to include Thread practitioners.
Himlensendt pool: Mandate 7D (from T-B7-02 context), TN7, Ob 2 → P(success) ≈ 70%.

#### Step 2: Thread event fires mid-debate (M-047)
Spontaneous Thread manifestation — a Shifting Object appears briefly in the chamber.
**Thread event triggers:**
- All practitioners in room: TS perception roll (Ob 2). Almud (TS 8): 4D, P(success) ≈ 88%. Almud perceives it.
- Non-practitioners: no perception, but physical manifestation visible to all. TT +1 (→ 31).
- Devout character (Himlensendt): zero TS — perceives nothing Thread-side. Sees only the physical effect.

**Himlensendt interpretation (Devout Constraint, M-051):** Physical anomaly with no Thread perception = interpreted as divine sign. Himlensendt's Belief fires: "The Confessor's mandate is absolute." This is narratively confirmed for him. Himlensendt gains +1D on current Grand Debate argument (divine confirmation narrative). **Devout Constraint creates an asymmetric information advantage: Himlensendt is emboldened by something Almud knows is a Thread accident.**

**Almud's dilemma (M-047 + M-011):**
Almud perceives the Thread event as what it is (a spontaneous Shifting Object). She can:
(a) Say nothing — Himlensendt's narrative stands, TC +3 if his argument succeeds.
(b) Reveal Thread knowledge — exposes her TS awareness publicly. Circles: Parliament 5 → risk of Unmask.
(c) Reframe without revealing — Circles roll to shift the narrative. Pool: Circles Parliament 5 + Coord 3 = 8D, TN7, Ob 3 → P(success) ≈ 60%.

**M-011 + M-037 interaction:** Circles directly feeds into Grand Debate as a narrative reframe. A high-Circles character can alter the debate outcome without making a formal argument roll. This is an undocumented interaction — Circles can substitute for debate skill in social scenes if used to manipulate the frame rather than argue directly.

#### Step 3: Grand Debate outcome with Thread event modifier
If Almud succeeds at reframe (60%):
- Himlensendt's Inspiration boost (from "divine confirmation") is neutralised
- Grand Debate resumes at baseline odds
- TC gains no benefit this round

If Almud fails at reframe:
- Himlensendt's argument succeeds with +1D bonus: P(success) rises to ~80%
- TC +3 on success (→ 51) → Synod triggers (TC 50 threshold, already noted in T-B7-07)

**M-031 + M-037 cascade confirmed:** Grand Debate success by Himlensendt → TC threshold → Synod → Church Mandate +2 → next Grand Debate even harder to contest.

**IP interaction:**
Almud's reframe (if she reveals Thread knowledge publicly): IP +3 (political crisis — Crown representative acknowledged Thread activity in Parliament).
At IP 17 + 3 = 20: IP threshold fires. Effect: Parliament Integrity check required.

### Findings

**F-B7-34** (P2) — Circles as debate substitute is undocumented. M-011 + M-037 interaction allows Circles-based narrative reframe to bypass formal debate mechanics. This is powerful and emergent but unspecified in either mechanic's rules text. Players who discover this will use it; players who don't, won't. Inconsistent access to a powerful option.

**F-B7-35** (P2) — Devout information asymmetry can produce perverse narrative confirmations. Thread accidents are indistinguishable from divine signs for Devout characters. This can create situations where the Devout character is narratively "right" for wrong reasons — and mechanically rewarded for the misinterpretation. May be intentional (epistemic seduction from Foundations P-10) but needs explicit design acknowledgment.

**F-B7-36** (P3) — TC cascade from debate is fast. Two conditions (Himlensendt success + Thread event interrupt) can push TC from 48 to 51 in one scene. At TC 48, the system is one debate away from Synod regardless of player action. Threshold approach speed may need dampening.

---

## T-B7-12 — SCALE TRANSITIONS + DOMAIN ACTIONS + SEASONAL ACCOUNTING + CLOCK INTERACTIONS
**Coverage:** M-048, M-035, M-038, M-033
**Mode:** HYB | **Temporal:** CROSS | **Tracks:** FSTAT,TT,TC,IP | **Factions:** Crown,Church,Guilds | **NPCs:** Almud | **Archetypes:** Faction Leader,Practitioner

### Mode B+C — Interaction Chain + Scenario

**Chain:** Individual Thread action (TTRPG scale) → Scale Transition to faction impact (M-048) → Domain Action triggered (M-035) → Seasonal Accounting modified (M-038) → Clock cascade (M-033)

**Setup:** Almud's individual Thread operation (past-oriented Pull on historical record) succeeds at scale 1 (personal). Scale Transition check: does this propagate to faction-level consequences?

#### Scale Transition (M-048)
Trigger: Thread op net successes > Ob by 2+ (Overwhelming) at personal scale.
Overwhelming personal Thread op → automatic scale escalation to faction level.

**M-048 mechanics:** Scale escalation = the Thread operation's effect now applies to a faction stat or clock, not just a personal/narrative outcome.
Almud's Pull (historical record): alters a legal precedent. At personal scale: one document changed.
At faction scale (Overwhelming): Crown's legal claim to a contested territory is strengthened. Crown Influence +1.

**No mechanic specifies the scale translation formula.** How many personal-scale Overwhelming results = 1 faction stat point? 1:1 assumed here but unspecified. **GAP: Scale translation ratio absent.**

#### Domain Action triggered by Scale Transition (M-035)
Crown gains Influence +1 via Thread operation rather than Domain Action.
Question: does this count as Crown's Domain Action for the season, or is it additive?
No rule found. **GAP: Thread-derived faction stat gains vs Domain Action economy not defined.**

If additive: Crown can gain faction stat benefits from both Thread operations (via practitioners) AND Domain Actions in the same season. This doubles Crown's effective Domain Action output in sessions with active practitioners.

#### Clock Interactions (M-033)
Almud's Pull modifies historical record → TC −1 (undermining Church's historical claim → reduces TC).
Scale Transition applied: TC −2 (faction-scale effect).
TC 48 → 46. Now below threshold 50 (no Synod trigger this season).

**M-033 interaction map:**
One Thread operation chain: IP +2 (if revealed), TC −2 (Almud's effect), TT +1 (Thread op), Crown Influence +1.
Clocks affected simultaneously: 3 of 3 major clocks moved in one operation.
**A single Overwhelming Thread op can move all clocks simultaneously. No ceiling on clock manipulation per operation.**

#### Seasonal Accounting with scale transition results (M-038)
Crown Influence 7 → 8 (from Thread op).
Influence 8: approaching maximum. Still no threshold defined (F-B7-12 confirmed again).

### Findings

**F-B7-37** (P2) — Scale translation ratio undefined. How many personal-scale effects = 1 faction stat change? Without this, Scale Transitions are GM-discretion with no mathematical basis.

**F-B7-38** (P2) — Thread-derived faction gains vs Domain Action economy. If Thread ops grant faction stat changes additively to Domain Actions, practitioners become a second economy layer for faction stats. High-TS Crown characters could double Crown's faction advancement rate.

**F-B7-39** (P2) — No ceiling on simultaneous clock movement. One Thread operation can move TT, TC, and IP simultaneously. At high practitioner activity, clocks could cascade faster than faction play can respond.

---

## T-B7-13 — REST + WOUNDS + CONDITIONS + COMBAT AFTERMATH
**Coverage:** M-053, M-002, M-007, M-039
**Mode:** TTRPG | **Temporal:** PRES | **Tracks:** COMP | **Factions:** Crown | **NPCs:** — | **Archetypes:** Generic,Löwenritter Knight

### Mode C — Post-Combat Recovery Sequence

**Setup:** Ehrenwall post-combat from T-B7-08. Wounds 2, Rattled (Condition), Composure 4/5.

**State entering recovery:**
```
Ehrenwall — Coord 5, End 4, Health 6, Wounds 2, Composure 4
  Conditions: Rattled
  Inspirations: 1
```

#### Quick Rest (M-053)
Requirements: scene ends, no immediate threat, ~10 minutes fictional time.
Effects: clears 1 Condition (if appropriate to type), heals 0 Wounds (Wounds 2 = above Quick Rest healing threshold).

**Condition clearing (M-007):** Rattled clears on: Quick Rest after scene without further violence, OR Composure roll Ob 2.
Composure roll: Composure 4D (Composure as stat, not track), TN7, Ob 2 → P(≥2 net) ≈ 50%.

**Wait — mechanic gap:** Does Composure function as a dice pool (stat) or a track (resource)? M-007 is ambiguous. "Composure" appears in two contexts:
1. Composure track (resource that degrades: 5 → 0)
2. Composure as a social/mental attribute (dice pool source)

If Composure is a track: using Composure to clear Conditions depletes the track. At Composure 4 track, rolling 4D to clear Rattled: on success, Rattled clears but Composure track is not itself depleted (rolling doesn't cost Composure, outcome does). On failure, Composure track −1 (→ 3).

**This is a genuine mechanical ambiguity. The same word is used for two different things.** At Composure track 0: character breaks (mechanically equivalent to incapacitation for social/mental). **GAP: Composure dual-use as track and pool not differentiated in rules text.**

#### Full Rest (M-053)
Requirements: safe location, 6+ hours, no major stressors.
Effects: clears all Conditions, heals all non-permanent Wounds.

At Wounds 2 (non-permanent): Full Rest heals both Wounds. State → Wounds 0.

**Permanent Wounds:** How do Wounds become permanent? No mechanic found specifying when Wounds are permanent vs temporary. At Wounds 4 (near-death)? After specific injury types? **GAP: Permanent Wound criteria absent.**

**Full Rest safety definition (F-B7-03 revisited):** "Safe location" still undefined. In active conflict scenario: Ehrenwall is in occupied territory. Is a barricaded room "safe"? GM judgment only.

#### Initiative recovery (M-039)
After rest: Ehrenwall at full initiative capability (Wounds 0, no Conditions).
Coord 5D, TN7, Ob 1 → P(success) ≈ 93%.
No initiative degradation from prior combat — rest is a clean reset. This is appropriate.

**M-039 + M-053 interaction confirmed:** Rest fully restores combat effectiveness. No residual mechanical state persists after Full Rest. Combat damage is entirely reversible except for Permanent Wounds (criteria undefined).

### Findings

**F-B7-40** (P1) — Composure dual-use ambiguity. "Composure" is used as both a degrading track (resource) and a dice pool source (attribute). These need to be explicitly differentiated. Current usage suggests: Composure track = current social/mental resilience; Composure dice = End stat or a derived attribute. If they're the same thing, spending Composure to clear Conditions should reduce the track.

**F-B7-41** (P2) — Permanent Wound criteria absent. No rule specifies what makes a Wound permanent. Without this, every Wound heals on Full Rest, which means combat has no lasting physical consequences. Undermines long-term campaign stakes.

---

## T-B7-14 — EINHIR SITES + WEAVING + PAST-ORIENTED PULLING + CERTAINTY
**Coverage:** M-054, M-015, M-019, M-009
**Mode:** TTRPG | **Temporal:** PAST/CROSS | **Tracks:** TS,TT,ThS,CERT,TD | **Factions:** Varfell,Revolution | **NPCs:** Vaynard,Maret Uln | **Archetypes:** Practitioner,Non-TS Scholar

### Mode B+C — Interaction Chain + Scenario

**Setup:** Einhir site access + Thread operations sequence. Vaynard (Varfell) seeks to use an Einhir site to amplify Past-Oriented Pulling. Maret Uln (non-practitioner) accompanies as scholar.

**Initial State:**
```
Vaynard — TS 14, TD 8, Certainty 6, Coord 3
Maret Uln — TS 0, Coord 3, End 3
TT 30 | ThS 14 (elevated due to Einhir site proximity)
```

#### Einhir Site access (M-054)
Einhir sites are locations of concentrated historical Thread activity — past operations leave residue that amplifies current operations.

**Site mechanics (reconstructed from batch data):**
- At Einhir site: +2D on Past-Oriented Thread operations (M-019)
- At Einhir site: ThS locally elevated (+4 to local ThS)
- At Einhir site: passive non-practitioner detection Ob reduced (ThS effect, M-020)

**Local ThS at Einhir site:** 14 + 4 = 18. Passive detection Ob: 10 − 18/2 = 10 − 9 = Ob 1.
**Any character with TS ≥ 1 will passively detect Thread activity at this site on an Ob 1 roll.** This means Einhir sites are extremely exposed — any Inquisitor within range will sense operations here. **Einhir sites and Inquisitor operations (M-049) are in direct tension.**

#### Weaving at Einhir site (M-015)
Vaynard weaves a Thread structure to stabilise the site for Past-Oriented Pulling.
Pool: TS/2 + Einhir bonus 2D = 7 + 2 = 9D, TN7, Ob 2 → P(success) ≈ 88%
Success: Site stabilised for 1 operation. +1D on subsequent Past Pull. TT +1.

**Weaving + Certainty interaction (M-009):**
Certainty 6 (above 5): no penalty. Weaving success at Certainty 6.
Weaving success → Certainty +1 (7). **Certainty increases on successful operations.** This is a positive feedback: success builds confidence, enabling better future operations.

#### Past-Oriented Pulling (M-019)
Vaynard attempts to Pull a historical Thread — altering a past event's memory/record.
Pool: TS/2 + Einhir bonus 2D + Weaving prep 1D = 7 + 2 + 1 = 10D, TN7, Ob 4 (Past Pull Ob elevated vs present Pull)
TD 8 threshold (TD 5 = Ob +1, TD 10 = Ob +2 — at TD 8: between thresholds, Ob +1): Ob 5
P(≥5 net, 10D, TN7) ≈ 40%

**This is the most favorable context for a Past Pull.** Without Einhir site and Weaving prep:
Pool: 7D, TN7, Ob 4 + TD Ob 1 = Ob 5 → P(≥5 net, 7D) ≈ 12%. Four times worse.

**Einhir site + Weaving as mandatory combo:** For Past-Oriented Pulling to be reliable at all, both Einhir site access AND Weaving prep are required. Neither alone is sufficient. This makes Past Pulls highly contextual — they require specific locations and preparation. **Design assessment: this creates meaningful ritual structure for the most powerful Thread operation, which is consistent with Foundations P-09 (Memory pull = messy).**

#### Maret Uln (non-practitioner) role (M-054)
Maret Uln provides scholarly context that assists Vaynard's historical orientation.
Pool contribution: Maret Uln's relevant History (historian of Varfell) = +1D to Vaynard's operation if Maret Uln succeeds a Knowledge roll (End 3D, TN7, Ob 2 → P(success) ≈ 55%).

**Non-practitioner contribution to Thread ops:** This is the primary mechanic for non-practitioners to contribute to Thread operations — via Knowledge/History rolls that add dice to the practitioner's pool. The non-practitioner is not doing Thread work; they're providing orientation information. **Well-designed collaborative mechanic.**

#### Certainty degradation during Past Pull (M-009)
Past Pulls are inherently destabilising to Certainty.
On success: Certainty neutral (risky operation succeeded, confidence maintained).
On partial: Certainty −1 (6 → 5). Just above threshold.
On failure: Certainty −2 (6 → 4). Below threshold — next op at −1D.

**Certainty 5 threshold:** Below 5, −1D on all Thread ops. This makes failure on a Past Pull compound: failure → Certainty penalty → next op harder → more likely to fail → Certainty continues dropping.

**But:** Successful Weaving just raised Certainty to 7. If Past Pull fails: 7 → 5 (−2). Still above threshold. The Weaving prep acts as a buffer for Certainty. **M-015 + M-009 synergy: Weaving before high-risk ops is mechanically rewarded via Certainty buffer.**

### Findings

**F-B7-42** (P2) — Einhir sites are maximally detectable. Local ThS 18 at Einhir sites means any Inquisitor or TS-sensitive character in proximity automatically detects Thread activity. Operating at Einhir sites is essentially announcing yourself to anyone watching. May be intentional (high power, high risk) but creates a near-certain exposure scenario for any Einhir site operation.

**F-B7-43** (P3) — Past-Oriented Pulling only reliable in optimal conditions. Outside Einhir site + Weaving prep context, P(success) drops to ~12%. This makes the mechanic effectively inaccessible in improvised or emergency situations. Highly contextual design is consistent with Foundations but may frustrate players who expect to use Past Pulls situationally.

---

## T-B7-15 — NIFLHEL DESTABILISATION + FACTION STATS + RISKBREAKERS + THEOCRACY CLOCK
**Coverage:** M-056, M-034, M-050, M-031
**Mode:** BG/HYB | **Temporal:** CROSS/FUT | **Tracks:** FSTAT,TC,TT,DD,CE | **Factions:** Niflhel,Church,Crown | **NPCs:** — | **Archetypes:** Riskbreaker,Faction Leader

### Mode C — Faction Operation Scenario

**Setup:** Niflhel (covert faction) attempts to destabilise Church via Riskbreaker network. Church and Crown are unaware.

**Initial State:**
```
Niflhel:  M 3, I 5, W 4, Mi 2, In 7, S 5  [Intel-heavy, covert faction]
Church:   M 8, I 6, W 4, Mi 5, In 5, S 8  [post-Synod: Mandate elevated]
Crown:    M 6, I 7, W 5, Mi 5, In 5, S 6

TC 52 (Synod active) | TT 33 | DD(Riskbreaker) 0/10
```

**F84 confirmed:** Niflhel has no Intel stat in the matrix. This test assigns In 7 as a design inference — Niflhel is defined as covert faction, therefore Intel should be their primary stat. The absence of this in the ruleset is the P1 gap.

#### Riskbreaker operation (M-050)
Niflhel Riskbreaker infiltrates Church hierarchy to gather leverage.
Pool: Niflhel Intel 7, TN7, Ob 2 → P(success) ≈ 82%
Success: Church Intelligence −1 (4). Riskbreaker accumulates Deniability Debt (DD) +2.
DD 0 → 2.

**DD mechanic (M-050):**
DD accumulates with each covert operation.
DD threshold 5: operations require additional precaution (Ob +1).
DD threshold 8: Riskbreaker is compromised — 50% chance of exposure per operation.
DD threshold 10: Riskbreaker is burned — cannot operate, faction takes reputation hit.

#### Destabilisation action (M-056)
Niflhel uses leverage to destabilise Church — leaking information about Church financial irregularities.
Pool: Niflhel Intel 7, TN7, Ob 3 → P(≥3 net) ≈ 60%
Success: Church Stability −2 (8 → 6). TC −1 (Synod authority undermined). DD +3 (→ 5, hits threshold).

**TC interaction (M-031):**
TC 52 − 1 = 51. Still above 50 (Synod still active). Destabilisation slowed the clock but didn't cross it below threshold.
To end Synod: TC must drop below 50. Needs TC −2 minimum from current position.

**M-050 + M-056 interaction — DD acceleration:**
Each Destabilisation op: DD +3. Each standard Riskbreaker op: DD +2.
After 2 Destabilisation ops: DD 0 + 2 (standard) + 3 (destab 1) + 3 (destab 2) = DD 8. Riskbreaker compromised after 2 full operations.
**Niflhel Destabilisation is a self-limiting mechanic.** The covert actor degrades their own operational capacity through use. Maximum ~3 significant operations before Riskbreaker is burned.

**M-034 faction stat cascade:**
Church Stability 8 → 6 after successful Destabilisation.
Church Stability 6: approaching threshold? No stability threshold defined (F-B7-12 confirmed again).
At Stability 0: faction collapses? No rule. **The most consequential faction stat (Stability) has no floor mechanic.**

**Crown awareness:**
Crown Intel 5. Niflhel operating at DD 5 (threshold): Crown passive awareness check.
No mechanic found for passive faction intelligence checks. **GAP: How do factions discover ongoing covert operations passively?** Only active Domain Actions (Intelligence-type) seem to reveal rival activity.

**Theocracy Clock + Niflhel:**
TC is primarily driven by Church Domain Actions. Niflhel's destabilisation can suppress TC but cannot drive it down rapidly. TC −1 per successful Destabilisation op vs typical Church TC gains of +2–3 per Domain Action. **Niflhel can slow TC growth but not reverse it meaningfully without more aggressive operations (DD cost too high).**

### Findings

**F-B7-44** (P1 — confirms F84) — Niflhel Intel stat undefined in ruleset. This test required design inference (In 7) to proceed. Without explicit Intel stat definition for Niflhel, the faction cannot be run mechanically.

**F-B7-45** (P2) — Faction Stability 0 has no defined consequence. Church Stability could theoretically be reduced to 0 through sustained Destabilisation. No mechanic defines what happens (faction collapse? civil war trigger? TC spike?). The most narratively significant outcome has no mechanical expression.

**F-B7-46** (P2) — Passive faction intelligence absent. Factions have no mechanic for passively detecting ongoing covert operations. Only active Intel Domain Actions discover rivals. A faction being actively destabilised has no awareness unless they spend a Domain Action specifically to look. Suspense-appropriate but mechanically incomplete.

**F-B7-47** (P3) — Niflhel destabilisation rate cannot outpace Church clock-driving. Church drives TC +2–3 per season via Domain Actions. Niflhel reduces TC −1 per successful op but burns the Riskbreaker after ~3 ops. Church wins the clock race structurally. This may be intentional (TC is supposed to build to a crisis) but means Niflhel's primary mechanical purpose (destabilisation) is cosmetic relative to TC trajectory.

---

## BATCH 07 FINDINGS INDEX

| # | Test | Mechanics | Severity | Issue |
|---|------|-----------|----------|-------|
| F-B7-01 | T-01 | M-002 | P2 | Wound/TN cliff: 1→2 Wounds drops attack success 70%→30% |
| F-B7-02 | T-01 | M-007 | P3 | Unmask/Circles interaction unspecified — does Unmask reduce Circles rating? |
| F-B7-03 | T-01 | M-053 | P3 | Safe rest definition absent — "safe location" has no mechanical criteria |
| F-B7-04 | T-02 | M-006 | P2 | Inspiration spend timing unspecified — pre-roll declaration vs retroactive |
| F-B7-05 | T-02 | M-003 | P2 | Histories double-dipping — no cap on applicable Histories per roll; 4 Histories = +8D |
| F-B7-06 | T-02 | M-036,M-037 | P1 | Grand Debate → Parliamentary Vote handoff broken (F80 confirmed load-bearing) |
| F-B7-07 | T-02 | M-004 | P3 | CP accumulation rate potentially high vs spend rate — flag for tracking |
| F-B7-08 | T-03 | M-013,M-016 | P1 | TD/Pull probability cliff at threshold 5: P(success) 55%→20%. No TD recovery found |
| F-B7-09 | T-03 | M-016 | P2 | Partial Pull side effect scope undefined — GM has unlimited latitude |
| F-B7-10 | T-03 | M-010,M-016 | P2 | Knot escalation loop: failed ops → more Knots → higher Ob → more failures |
| F-B7-11 | T-03 | M-009,M-014 | P3 | Certainty gate asymmetric: gates Diagnosis but not Leap/Pull (can pull blind) |
| F-B7-12 | T-04 | M-034 | P1 | Faction stat thresholds absent — no consequence at 0 or max for any stat |
| F-B7-13 | T-04 | M-035 | P2 | Character skill irrelevant to Domain Actions — Histories/Beliefs/TS have no pathway |
| F-B7-14 | T-04 | M-011 | P2 | Circles obligation resolution absent — partial results create obligations with no discharge |
| F-B7-15 | T-04 | M-011,M-035 | P3 | BG/TTRPG translation gap — Circles/Resources have no BG mode equivalent |
| F-B7-16 | T-05 | M-016,M-013 | P1 | No TD recovery mechanic — TD is permanent one-way ratchet; practitioners become useless |
| F-B7-17 | T-05 | M-018,M-030 | P1 | Single practitioner cascade can trigger TT global threshold (TT +9 from one 3-op failure) |
| F-B7-18 | T-05 | M-021 | P2 | Coherence terminal state has no exit — appears to be one-way ratchet like TD |
| F-B7-19 | T-05 | M-017 | P2 | FR-Lock failure penalty > non-attempt — perverse incentive to not attempt containment |
| F-B7-20 | T-06 | M-010,M-022 | P2 | Location accessibility binary at high accumulated difficulty — absolute inaccessibility |
| F-B7-21 | T-06 | M-010,M-015 | P3 | Knot/Residue clearing catch-22 — clearing requires accessing; accessing requires clearing |
| F-B7-22 | T-07 | M-034 | P1 | Negative faction stat undefined — Revolution Wealth −1 reachable in normal play |
| F-B7-23 | T-07 | M-035 | P1 | Domain Action sequencing absent — simultaneous conflicting actions have no resolution order |
| F-B7-24 | T-07 | M-031 | P2 | Synod duration undefined — TC 50 trigger fires but no exit condition specified |
| F-B7-25 | T-07 | M-034,M-038 | P2 | Church structural poverty — Wealth hits 0 after 1 seasonal cycle at standard stats |
| F-B7-26 | T-08 | M-039 | P2 | Initiative tie resolution absent — no mechanic for tied initiative |
| F-B7-27 | T-08 | M-044 | P3 | Manoeuvres suboptimal vs attacks in almost all cases — likely underused |
| F-B7-28 | T-08 | M-002 | P3 | Symmetric wound threshold creates "last one standing" endgame — may be intended |
| F-B7-29 | T-09 | M-045 | P1 | Mass combat damage formula absent (F100 confirmed) — all outcomes GM-determined |
| F-B7-30 | T-09 | M-045 | P2 | Unit attrition mechanics absent — all-or-nothing resolution, no morale/retreat |
| F-B7-31 | T-09 | M-040,M-045 | P2 | Individual Priority Table not adapted for mass combat |
| F-B7-32 | T-10 | M-046 | P2 | Thread operation timing in combat round undefined |
| F-B7-33 | T-10 | M-046,M-048 | P2 | TTRPG→BG state handoff undefined — Wounds/Conditions/Thread ops don't carry over |
| F-B7-34 | T-11 | M-011,M-037 | P2 | Circles as debate substitute undocumented — powerful emergent interaction |
| F-B7-35 | T-11 | M-047,M-051 | P2 | Devout information asymmetry — Thread accidents confirm Devout beliefs, reward misinterpretation |
| F-B7-36 | T-11 | M-031,M-037 | P3 | TC cascade from debate is fast — one scene can push TC past threshold |
| F-B7-37 | T-12 | M-048 | P2 | Scale translation ratio undefined — no formula for personal→faction stat conversion |
| F-B7-38 | T-12 | M-048,M-035 | P2 | Thread-derived faction gains vs Domain Action economy undefined |
| F-B7-39 | T-12 | M-033 | P2 | No ceiling on simultaneous clock movement from single Thread operation |
| F-B7-40 | T-13 | M-007 | P1 | Composure dual-use ambiguity — used as both degrading track and dice pool source |
| F-B7-41 | T-13 | M-002 | P2 | Permanent Wound criteria absent — all Wounds heal on Full Rest without this |
| F-B7-42 | T-14 | M-054 | P2 | Einhir sites maximally detectable — ThS 18 means automatic Inquisitor exposure |
| F-B7-43 | T-14 | M-019 | P3 | Past Pulls only reliable in optimal conditions (Einhir + Weaving) — inaccessible situationally |
| F-B7-44 | T-15 | M-056 | P1 | Niflhel Intel stat undefined (F84 confirmed) |
| F-B7-45 | T-15 | M-034,M-056 | P2 | Faction Stability 0 has no defined consequence |
| F-B7-46 | T-15 | M-050,M-056 | P2 | Passive faction intelligence absent — factions can't detect destabilisation without active Intel action |
| F-B7-47 | T-15 | M-056,M-031 | P3 | Niflhel destabilisation rate cannot outpace TC — covert faction may be cosmetically limited |

### P1 Summary — Batch 07
| Finding | Mechanic | Issue |
|---------|----------|-------|
| F-B7-06 | M-036,M-037 | Grand Debate → Vote handoff broken |
| F-B7-08 | M-013,M-016 | TD/Pull cliff + no TD recovery |
| F-B7-12 | M-034 | Faction stat thresholds absent |
| F-B7-16 | M-016,M-013 | TD permanent ratchet (same root as F-B7-08; confirm as single finding) |
| F-B7-17 | M-018,M-030 | Single practitioner cascade can trigger global TT threshold |
| F-B7-22 | M-034 | Negative faction stat undefined |
| F-B7-23 | M-035 | Domain Action sequencing absent |
| F-B7-29 | M-045 | Mass combat damage formula absent (F100 confirmed) |
| F-B7-40 | M-007 | Composure dual-use ambiguity |
| F-B7-44 | M-056 | Niflhel Intel stat undefined (F84 confirmed) |

**New P1 findings this batch: 8** (F-B7-06, F-B7-08/16 consolidated, F-B7-12, F-B7-17, F-B7-22, F-B7-23, F-B7-40)
**Existing P1 findings confirmed: F80 (F-B7-06), F100 (F-B7-29), F84 (F-B7-44)**
**Total P1 after Batch 07: 11 (prior) + 7 new = 18**

---

## COVERAGE MATRIX UPDATE — BATCH 07

Mechanics with Interaction cell now filled (≥3 co-mechanics):

| ID | Test | Co-mechanics |
|----|------|-------------|
| M-001 | T-B7-01 | M-002, M-007, M-039, M-053 (5 total) |
| M-002 | T-B7-01, T-B7-08 | Multiple |
| M-003 | T-B7-02 | M-004, M-006, M-037 |
| M-004 | T-B7-02 | M-003, M-006, M-037 |
| M-006 | T-B7-02 | M-003, M-004, M-037 |
| M-007 | T-B7-01, T-B7-13 | Multiple |
| M-010 | T-B7-03 | M-013, M-014, M-016 |
| M-011 | T-B7-04, T-B7-11 | Multiple |
| M-012 | T-B7-04 | M-011, M-034, M-035 |
| M-013 | T-B7-03 | M-010, M-014, M-016 |
| M-014 | T-B7-03 | M-010, M-013, M-016 |
| M-016 | T-B7-03, T-B7-05 | Multiple |
| M-017 | T-B7-05 | M-016, M-018, M-021 |
| M-018 | T-B7-05 | M-016, M-017, M-021 |
| M-021 | T-B7-05, T-B7-06 | Multiple |
| M-022 | T-B7-06 | M-021, M-010, M-016 |
| M-026 | T-B7-11 (via Inquisitor context) | — (partial; standalone test still needed) |
| M-034 | T-B7-04, T-B7-07 | Multiple |
| M-035 | T-B7-04, T-B7-07 | Multiple |
| M-038 | T-B7-07, T-B7-12 | Multiple |
| M-039 | T-B7-08, T-B7-09 | Multiple |
| M-040 | T-B7-09 | M-045, M-039, M-002 |
| M-042 | T-B7-08 | M-043, M-044, M-002, M-039 |
| M-043 | T-B7-08 | M-042, M-044, M-002, M-039 |
| M-044 | T-B7-08, T-B7-10 | Multiple |
| M-045 | T-B7-09, T-B7-10 | Multiple |
| M-046 | T-B7-10 | M-044, M-045, M-039 |
| M-047 | T-B7-11 | M-011, M-037, M-031 |
| M-048 | T-B7-12 | M-035, M-038, M-033 |
| M-053 | T-B7-01, T-B7-13 | M-002, M-007, M-039 |
| M-054 | T-B7-14 | M-015, M-019, M-009 |
| M-056 | T-B7-15 | M-034, M-050, M-031 |

**Mechanics reaching Interaction bar this batch: 32**
**Total mechanics with Interaction (≥3 co-mechs): 25 (prior) + 31 new − overlaps ≈ 53/56**
**Mechanics still below bar: M-005, M-026 (partial), M-041** (3 remaining)
**50% gate: PASSED — 53/56 = 95%**

