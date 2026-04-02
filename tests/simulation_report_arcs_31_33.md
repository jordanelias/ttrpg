# Valoria — Hybrid Simulation Report
## Arcs 31 + 33: "The Quaestio of Baralta" + "The Forgetting Road"
## Simulator skill: Mode C (Full Scenario) + G1 (Mass Combat) + G2 (Debate) + G3 (Threadwork) + G4 (Faction Seasonal)
## Date: 2026-04-01
## Params version: combat_params.md 2026-03-31 (v0.14 ✓)

---

# SIMULATION 1: ARC 31 — "THE QUAESTIO OF BARALTA"

## Test Tag
```
Test ID: SIM-ARC31-C01
Mechanics: M-036 (Parliamentary Vote), M-037 (Grand Debate/quaestio), M-045 (Mass Combat), M-046 (Thread in Combat), M-056 (Niflhel Destabilisation), debate_v1 (quaestio phases), mass_battle_v3
Mode: HYB | Temporal: CROSS
Tracks: TC, TT, IP, TS, COMP, CERT, FSTAT
Factions: Church, Hafenmark, Niflhel, Crown, Löwenritter
NPCs: Baralta, Himlensendt, Olafsson, Ehrenwall, Maret Uln
Archetypes: Faction-leader debater, Practitioner, Covert operative, Military commander
```

---

## Pre-Simulation State

```
## State: Season 0 / Pre-Arc Starting Position
Faction Stats:
  Crown:      Mandate 5 | Influence 5 | Wealth 4 | Military 4 | Stability 4
  Church:     Mandate 5 | Influence 6 | Wealth 5 | Military 4 | Stability 5
  Hafenmark:  Mandate 5 | Influence 4 | Wealth 5 | Military 3 | Stability 4
  Varfell:    Mandate 4 | Influence 4 | Wealth 4 | Military 4 | Stability 4
  Niflhel:    Influence 5 | Wealth 4 | Intel 5 | Stability 4
  Löwenritter: Influence 3 | Military 5 | Intel 3 | Stability 5

Clocks: TT=55 | TC=42 | IP=25
Ehrenwall Coup Counter: 2 (TC≥40 + no Crown action already marked)
Baralta Mandate: 5 (TC suppressor active; threshold is ≥4 per stage8 text... 
  STALE PARAMS NOTE: stage6_factions says "Mandate 4+" for suppressor; stage8_combat says 
  "Mandate 5+" at earlier section. Using stage6_factions §8.4: "Mandate remains 4+". 
  At Mandate 5, suppressor is ACTIVE.)
Baralta TC suppressor: −1/season ACTIVE
```

---

## Phase 1: Baralta's Domain Action

```
## Action: Baralta invokes Sovereign Authority Doctrine
## State: Season 1, Start
Roll: Mandate 5 (pool) vs Ob 4
Pool: 5D TN7
P(Overwhelming ≥8 net): ~8%
P(Success ≥4 net): ~35%
P(Partial 1–3 net): ~40%
P(Failure ≤0 net): ~17%
Expected net successes at TN7: 5 × 0.27 ≈ 1.35 (TN7 expected: 30% base - 1s penalty)

CORRECTION: Per dice model, TN7 net per die ≈ 0.27 (3/10 hit − 1/10 botch × correction for 
chains). At 5D: E[net] ≈ 1.35. Ob 4 is above expected — this roll fails slightly more often 
than it succeeds.

P(net ≥4) at 5D TN7: ≈ 17% (below expected)
P(net ≥2 × 4 = 8): ≈ 1% (Overwhelming extremely rare)
P(net 1–3): ≈ 45%
P(net ≤0): ≈ 38%

Most likely outcome: PARTIAL (net 1–3) at ~45%.
Partial result: TC −1. Heresy Investigation opens immediately. Church Influence +1.
```

**Finding F-ARC31-01 [P2]:** Baralta's Sovereign Authority Doctrine at Mandate 5 against Ob 4 is structurally unfavourable. Expected value produces a Partial most of the time. The design intent (Baralta as major TC brake) is undercut: TC −1 on Partial vs TC −2/−3 on success, with the Heresy Investigation as a guaranteed downside regardless of roll quality. Net TC effect on Partial: −1 now, but Heresy Investigation fires → if successful, TC +3. Expected net TC from invoking: negative in most runs.

**[PATCH: SIM-ARC31-P01]**
Finding: Sovereign Authority Doctrine Partial result produces a net-negative TC expectation relative to not invoking, making the action strategically inadvisable in most cases. A P1 who can hold Mandate 5 does more TC work passively than by invoking.
Mechanic: §8.4 Sovereign Authority Doctrine / stage6_factions Hafenmark
Proposed change: Partial result: TC −1, Heresy Investigation opens but Hafenmark gains +1D to all social rolls against the investigation for the season (the partial invocation is still a legitimate legal claim, and Baralta's reputation provides a defensive bonus even on the imperfect invocation). This makes Partial still costly but not net-negative relative to passive suppression.
Expected effect: Increases Partial expected value to roughly neutral; Success and Overwhelming remain clearly better. Maintains risk gradient.
Canon risk: LOW — consistent with Baralta's structural dominance through her Mandate, not contradicting it.

---

## Phase 2: Grand Debate Simulation (Mode G2)

```
## State: Season 1, Parliament Chamber
Participants:
  Baralta (Proposer, Exchange 1): 
    Cognition 4, Memory 3, Presence 5, Poise [undetermined — ED-011 open]
    History: Court Law (1) → bonus +4D (1 pt + 3)
    Concentration: Focus 3 → Concentration = 3 + Court Law = 3+4=7
    Genre: Consequence (Hafenmark Categorical Imperative → Consequence is secondary resonance)
    
  Himlensendt (Objector, Exchange 1):
    Cognition 5, Memory 4, Presence 6
    History: Theology (3), Political Negotiation (2)
    Concentration: Focus [not specified in stage13] → STALE PARAMS: Focus not in NPC profiles
    Genre: Evidence (Church primary resonance)
    
  Audience: Parliament (mixed; Crown resonance = Character primary; Hafenmark = Consequence)
  Format: Grand Debate, 5 exchanges, roles alternate
```

**STALE PARAMS FLAG:** NPC Focus scores are not in stage13_npcs.md. Grand Debate simulation requires Focus for Concentration calculation. Using estimated values (Himlensendt Focus 3 based on "sustained institutional attention" profile; flagging as gap).

[GAP-ARC31-SIM-01] Focus attribute missing from all NPC profiles in stage13. Required for: Debate Concentration, Thread contact duration. P2 gap — needs NPC sheet completion pass.

```
## EXCHANGE 1: Baralta proposes, Himlensendt objects
## 5-Phase Quaestio

Phase 1 — Proposition (Baralta, Cognition):
  Pool: Cognition 4 + Court Law bonus (4D) = 8D TN7
  E[net] = 8 × 0.27 ≈ 2.2
  Ob: 1 (institutional default, uncontested opening)
  P(≥1): ~97%. Most likely net: 2.
  Thesis Strength = 2.

Phase 2 — Objection (Himlensendt, Memory):
  Pool: Memory 4 + Theology bonus (3pts → 3+3=6D) = 10D TN7
  E[net] = 10 × 0.27 ≈ 2.7
  Most likely net: 3.
  Objection Markers placed: 3.
  
Phase 3 — Sed Contra (Baralta, Presence):
  Pool: Presence 5 + Court Law (4D) = 9D TN7
  E[net] = 9 × 0.27 ≈ 2.4
  Genre: Baralta uses Consequence genre.
  Audience (Parliament): Hafenmark reps = Consequence primary (+1D), Crown = Character primary (no bonus for Consequence genre).
  Effective pool for Sed Contra against Parliament dominant faction: +1D (Hafenmark resonance) = 10D.
  E[net] = 10 × 0.27 ≈ 2.7 → removes 2–3 Objection Markers.
  Most likely: 3 markers removed → 0 Objection Markers remaining from 3. Clean Sed Contra.

Phase 4 — Respondeo (Baralta, Cognition):
  Pool: 8D TN7 (same as Phase 1)
  E[net] ≈ 2.2 → adds 2 to Thesis Strength.
  Running Thesis Strength: 2 (Phase 1) + 2 (Phase 4) = 4.
  Concentration depletion: −1 at end of exchange.

Phase 5 — Distinction (Himlensendt, Poise [ED-011 OPEN]):
  ED-011 not resolved: using Presence as proxy (poise-adjacent in NPC profile). 
  FLAG: Distinction uses Poise attribute which is not in the current 10-attribute list.
  CRITICAL GAP: The debate_v1 design uses "Poise" (Phase 5) but this attribute does not exist 
  in the current attribute set. The 10 attributes are: Agi, End, Str, Cog, Mem, Foc, Att, Bon, 
  Pres, Spi. "Poise" is not among them.
```

**Finding F-ARC31-02 [P1 — BLOCKER]:** The quaestio Phase 5 (Distinction) uses "Poise" as its attribute, but Poise is not in the current 10-attribute set. This is a design gap that blocks compilation of the debate system. The attribute either maps to an existing one or requires the attribute list to be amended.

**[EDITORIAL: ED-ARC31-SIM-01 — Distinction Phase attribute]**
Gap type: Missing mechanic — attribute mapping
Blocking: YES — blocks debate system compilation
Proposed direction: Map Poise → Focus (sustained precision under pressure, which is what Focus governs per §2.1) OR map Poise → Presence (composure as social attribute). Focus is more defensible mechanically (Phase 5 is about finding the precise flaw under full audience scrutiny — a concentration act). Presence would create a Presence-vs-Presence late-game dynamic that may be too symmetric. Recommend Focus mapping pending user decision.

```
## EXCHANGE 1 RESOLUTION (using Focus as Poise proxy):
Phase 5 — Distinction (Himlensendt, Focus [proxy]):
  Focus estimate: 3 (not in stage13; using median)
  Pool: Focus 3 + Theology (6D) = 9D TN7
  E[net] ≈ 2.4 → reduces Thesis Strength by 2.
  Remaining Thesis Strength: 4 − 2 = 2.

Exchange 1 winner: BARALTA (Thesis Strength 2 > 0)
Margin: 2. Himlensendt takes 2 Composure strain.
Unaddressed Objection Markers: 0 (all removed in Sed Contra). No additional strain.
Concentration: Baralta 6/7, Himlensendt est. 5/6.
Audience Disposition: Parliament shifts +1 toward Baralta (margin ≥ 2, borderline Overwhelming at margin 2; criterion is margin ≥ 3 for auto-shift... margin 2 = no auto-shift).

NOTE: Exchange 1 produces slight Baralta advantage but no audience capture yet.
```

```
## EXCHANGE 2: Roles reverse — Himlensendt proposes, Baralta objects

Phase 1 — Proposition (Himlensendt, Cognition 5 + Theology 6D = 11D):
  E[net] ≈ 11 × 0.27 = 2.97 ≈ 3.
  Thesis Strength = 3.

Phase 2 — Objection (Baralta, Memory 3 + Court Law 4D = 7D):
  E[net] ≈ 7 × 0.27 = 1.89 ≈ 2.
  Objection Markers: 2.

Phase 3 — Sed Contra (Himlensendt, Presence 6 + Theology 6D = 12D):
  Church genre: Evidence. Church primary resonance audience match.
  Church reps in Parliament: +1D (Evidence resonance).
  Effective pool: 13D. E[net] ≈ 13 × 0.27 = 3.5 → removes 3 markers.
  Markers available: 2. All removed. Clean Sed Contra again.

Phase 4 — Respondeo (Himlensendt, Cognition 5 + Theology 6D = 11D):
  E[net] ≈ 3. Thesis Strength: 3 + 3 = 6.

Phase 5 — Distinction (Baralta, Focus [proxy] 3 + Court Law 4D = 7D):
  E[net] ≈ 1.89 ≈ 2. Reduces Thesis Strength: 6 − 2 = 4.

Exchange 2 winner: HIMLENSENDT (TS 4 > 0)
Margin: 4. Baralta takes 4 Composure strain.
Baralta Composure: 11 − 4 = 7 (well above Rattled threshold; no crisis).
Concentration: Baralta 5/7, Himlensendt 4/6.
Score: 1–1.
```

**Finding F-ARC31-03 [P2]:** Exchange 2 is structurally favoured for Himlensendt. His Cognition 5 vs Baralta's Cognition 4 produces +1 expected net in both Proposition and Respondeo phases. The asymmetry compounds: his Theology History (3 pts → 6D bonus) vs her Court Law (1 pt → 4D bonus) adds another 2D differential on Memory and Presence phases. Baralta cannot match Himlensendt's raw power in a straight symmetric quaestio. Her advantage is the Sed Contra (Presence 5 + institutional resonance matching). This creates a well-differentiated matchup: Baralta is a Sed Contra specialist, Himlensendt is a Proposition/Respondeo engine.

This is a design success — the quaestio structure is producing meaningful archetype differentiation.

```
## NIFLHEL INTERRUPTION: After Exchange 2, Before Exchange 3

## Action: Niflhel Quiet Network — Assassination mode targeting Riskbreaker operative
Roll: Niflhel Intel 5 vs target Intel +2 = Ob 7. Pool: 5D TN7.
P(≥7 net at 5D TN7): NEAR ZERO. Expected net: 1.35. Max realistic net at 5D ≈ 4.
Assassination attempt at Ob 7 with 5D: functionally impossible under normal conditions.

FINDING: Niflhel cannot reliably execute a named assassination via Quiet Network at Ob 7. 
The Intel+2 formula makes assassinations against high-Intel targets structurally improbable.
```

**[PATCH: SIM-ARC31-P02]**
Finding: Niflhel Quiet Network Assassination mode (Intel vs Intel+2) is nearly impossible against any target with Intel ≥3. Expected to fail ~90%+ of the time against median targets. The Network's signature ability is structurally neutered as an assassination tool.
Mechanic: §8.7 Quiet Network / stage6_factions Niflhel
Proposed change: Assassination Ob = target's Intel (not Intel +2). The +2 applies only if the target has active counter-intelligence measures declared that season. Standard assassination: Intel vs Intel.
Expected effect: Ob goes from 7 (Intel 5 target) to 5, producing ~35% success rate at 5D. Remains risky but viable.
Canon risk: LOW. Niflhel is the game's premier covert actor; their signature assassination tool being near-impossible undermines faction identity.

```
## EXCHANGE 3 (mid-arc, after interruption):
Register Shift: discovery of operative's body → not Unmask (no participant physically involved)
Narrative: formal register strained but holds. Both orators take 1 Concentration loss from 
the disruption (proposed gap-fill rule: register disruption = −1 Concentration to both, 
no phase reset).

Score after Exchange 2: 1–1. Exchange 3 is decisive.

Baralta proposes. Expected Exchange 3 outcome:
  E[Baralta TS after Proposition + Respondeo] = 2 + 2 = 4
  E[Himlensendt Distinction] = 2 → TS 2 remaining
  BUT: Concentration. Baralta: 5 − 1 (disruption) = 4/7. 
  Himlensendt: 4 − 1 (disruption) = 3/6.
  
  Concentration depletion does not affect dice pool directly — affects when Spent fires.
  Neither reaches Spent in Exchange 3 (both have ≥3 Concentration remaining).

Exchange 3 most likely: BARALTA wins (margin ~2, consistent with Exchange 1 pattern)
Score: 2–1 Baralta.
```

```
## EXCHANGES 4–5 (abbreviated — roles alternate):
Exchange 4: Himlensendt proposes (as Exchange 2 pattern) → wins by margin 4
Score: 2–2.
Exchange 5: Baralta proposes. Final exchange. Extra proposition right.

Per ED-013 (unresolved): which side gets the Exchange 5 extra proposition?
Assuming initiator (Baralta invoked Sovereign Authority → she called the Debate):
Baralta proposes Exchange 5.

Himlensendt Concentration: 3 − 2 (exchanges 2+4 depletion) = 1. Near Spent.
Exchange 5: Himlensendt at Concentration 1 risks Spent on Exchange 6 if there were one. 
For Exchange 5 itself: Concentration doesn't affect Distinction dice pool directly, 
but at Concentration 0 the Spent condition would apply −2D to all phases.

Exchange 5 result: Baralta wins (same pattern as Exchanges 1+3)
Final score: 3–2 Baralta.

GRAND DEBATE WINNER: BARALTA
Exchange victory: 3–2. Audience Disposition: Baralta accumulated 3 exchange wins, each 
margin ~2. No single win reached margin ≥3 (Overwhelming threshold for Disposition shift).
Audience outcome: Neutral → slightly favorable toward Baralta.
Dual win-condition (ED-012 unresolved): If audience applies to Grand Debates, Baralta has 
exchange victory but not audience capture. Outcome = PROCEDURAL VICTORY.
```

```
## STATE DELTA: After Grand Debate

TC: −2 (§7.2: Successful Grand Debate ruling against Church civil authority claim)
Church Mandate: −1
Baralta Mandate: unchanged (Partial from Sovereign Authority earlier; Debate win restores 
  narrative standing but Mandate mechanically unchanged by Debate alone)
Ehrenwall Coup Counter: 2 → stays at 2 (TC dropped below 40: −2 → TC = 40. 
  TC is now exactly 40, not below 40. Counter does not decrement.)
```

**Finding F-ARC31-04 [P1]:** TC drops to exactly 40 after successful Grand Debate with −2 modifier. The Coup Counter condition is "TC reaches 40 while Crown took no action." TC is still AT 40, not below 40. The counter increment does not reverse. This means a successful Grand Debate that drops TC from 42 to 40 has not averted the Coup Counter condition — only a second −1 (from Baralta's passive suppressor, next season) would bring TC to 39 and address the threshold.

**[PATCH: SIM-ARC31-P03]**
Finding: Coup Counter condition "TC ≥40 without Crown action" is evaluated at seasonal accounting. A mid-season Grand Debate dropping TC to exactly 40 does not resolve the condition if TC was ≥40 at the START of that season. The counter fires on the accumulated season state, not on the mid-season adjusted value.
Mechanic: §8.9 Ehrenwall Coup Counter
Proposed change: Add explicit clause: "Counter increment 1 (TC ≥40 without Crown action) is evaluated at START of seasonal accounting. If TC was reduced below 41 by Domain Actions before seasonal accounting, the condition is considered avoided for that season."
Expected effect: Gives players a clear window (Domain Action to reduce TC mid-season) to avert the counter increment. Currently ambiguous — the "without Crown action" clause implies intent to allow avoidance via player agency.
Canon risk: NONE — clarification only.

---

## Phase 3: Mass Battle Simulation (Mode G1)

```
## State: Season 2 (Conditional — Coup Counter still at 2, but Templar repositioning fires)
## Scenario: Templar force moves toward Hafenmark border (not coup-triggered — Church 
## exercising Military Domain Action)

Unit A: Church Templars (elite)
  Size: 4 | CP: 5 (Military 4 → max CP 5 at Military 4... 
  STALE PARAMS: mass_battle_v3 Military→CP table shows Military 4 → max CP 4. 
  Templars are Church's elite. CP 5 requires Military 5. Church Military = 4 → max CP = 4.)
  
  CORRECTION: Templar CP = 4 (not 5). Specialist units cannot exceed Military ceiling.
  Cohesion: min(CR, Military ceiling) = min(Jarnstal CR4, 4) = 4
  Morale: CR4 + unit quality modifier. Elite = +1. Starting Morale: 5.
  Formation: Wedge (standard Church Templar aggressive posture)
  Armour: Heavy
  Weapon: Heavy Blunt (maces, pollaxes — standard Templar issue)
  Commander: Jarnstal (CR4, Presence 4, Cognition 4 → CR = ceil((4+4)/2) = 4)

Unit B: Hafenmark Garrison
  Size: 3 | CP: 3 (Hafenmark Military 3 → max CP 3)
  Cohesion: min(CR3, ceiling3) = 3
  Morale: 4 (CR3 garrison commander + standard)
  Formation: Shield Wall (defensive — correct play against Wedge)
  Armour: Medium
  Weapon: Heavy Cut (longswords + spears)
  Commander: Generic Hafenmark (CR3)

## Battle Turn 1

Phase 1 — Strategy Declaration:
  Church: Wedge vs Hafenmark + Envelopment (Ob 2, Fast speed not available — Templars are 
  Standard speed). Envelopment requires Fast → unavailable. 
  Church declares: Wedge + Concentration (all sub-units on one target, Ob 1)
  Hafenmark: Shield Wall + Refused Flank (Ob 1, anchor on terrain)

Phase 2 — Volley: No projectile units engaged. Skip.

Phase 3 — Manoeuvre:
  Envelopment not available. Both units Standard speed. Position unchanged.

Phase 4 — Engagement:
  Effective Pool (Church): min(CP4, Size4) = 4 − Cohesion 4 (no penalty) + Wedge +2D Off = 6D Off
  Effective Pool (Hafenmark): min(CP3, Size3) = 3 − Cohesion 3 (no penalty) + Shield Wall −1D Off, +2D Def = 2D Off, 5D Def
  
  NOTE: Shield Wall negates Wedge (per §8.8 formation table: "Wedge negated if opponent uses Shield Wall"). Church loses Wedge bonus: OFF pool = 4D (base, no formation bonus).
  
  Church attack: 4D TN6 (Heavy Blunt hit TN = 7 from weapons table. Wait — TN is weapon-specific. Heavy Blunt Hit TN: 7, Def TN: 8 per stage8.)
  
  STALE PARAMS CHECK: stage8 weapons table: HeavyBlunt Hit TN=7, Def TN=8. 
  Mass combat inherits personal combat table (mass_battle_v3 §A.2 confirms).
  
  Church OFF roll: 4D TN7 vs Hafenmark DEF 5D TN7 (Shield Wall Def)
  Church E[net Off] = 4 × 0.27 = 1.08
  Hafenmark E[net Def] = 5 × 0.27 = 1.35
  
  Hit determination: Church net Off (1.08) vs Hafenmark net Def (1.35). Expected: Hafenmark defends successfully.
  
  Hafenmark attack: 2D TN6 (HeavyCut Hit TN=6, Def TN=7) vs Church DEF [allocated]
  Church splits pool: 4D total. With 4D OFF already committed: Church must allocate to both.
  
  WAIT: Pool split in mass combat — per mass_battle_v3 Phase 4: both sides split their 
  Effective Pool simultaneously, same as personal combat. Church Effective Pool = 4D (base, 
  Wedge negated by Shield Wall).
  Church splits: 3D OFF / 1D DEF
  
  Church OFF: 3D TN7 E[net] = 0.81
  Church DEF: 1D TN7 E[net] = 0.27
  
  Hafenmark OFF: 2D TN6 (HeavyCut) E[net at TN6] = 2 × 0.40 ≈ 0.80
  Hafenmark DEF: 5D TN7 (Shield Wall) E[net] = 1.35
  
  Damage calculation (Church → Hafenmark):
  Church OFF net (0.81) vs Hafenmark DEF net (1.35): expected net HIT = negative → miss
  
  Damage calculation (Hafenmark → Church):
  Hafenmark OFF net (0.80) vs Church DEF net (0.27): expected net HIT = 0.53 → partial damage
  HeavyCut vs Heavy armour: DR 5. Damage = 0.53 excess + weapon modifier (HeavyCut +4) = 4.53 − 5 DR = 0. No damage.
  
  Turn 1 result: Neither side damages the other.
```

**Finding F-ARC31-05 [P1]:** Shield Wall + Heavy Armour defender against Heavy Cut attacker produces zero expected damage even on a partial hit. Heavy Cut modifier (+4) minus Heavy Armour DR (5) = −1, minimum 0. A defensive formation with heavy armour against a standard weapon type is effectively impenetrable. This is consistent with weapon system design intent (HeavyCut is weak against Heavy armour) but creates a mass combat stalemate scenario where neither side can breach the other's formation without matching weapon types.

This is not a bug — it is the weapon matchup problem at mass scale. But it creates a specific tactical deadlock that the battle system needs to resolve: how does a Church force with Heavy Blunt (correct tool for Heavy armour) avoid the Shield Wall negating its Wedge?

**[PATCH: SIM-ARC31-P04]**
Finding: A Heavy Blunt weapon Church force using Wedge vs Shield Wall (negation applies) is locked out of its offensive bonus, but a Heavy Cut force using Wedge is ineffective against Heavy armour. Church needs a combined-arms solution: ranged + melee, or a different formation.
Mechanic: §8.9 Mass Combat / Formation table
Proposed change: Add "Hammer & Anvil" as the counter to this deadlock (it already exists in the tactic table). Church should use Hammer & Anvil: Shield Wall holds (Templars take the anchor role) + Fast cavalry unit envelops. This is a design clarification, not a rules change — the tool exists. Needs explicit example in mass_combat section showing Church's correct counter to a Shield Wall defender.
Canon risk: NONE — example text only.

---

## Phase 4: Thread Operations in Mass Combat (Mode G3)

```
## State: Season 2, Battle Turn 2
## Maret Uln joins Hafenmark side as Thread support
## Declared: Phase 1. Resolves Phase 5 (Support Thread operation)

Maret Uln stats:
  TS: confirmed practitioner-level (exact TS not in stage13 → GAP-ARC31-SIM-01)
  Assuming TS 50 (narrative confirmed practitioner, not yet master)
  Focus: 3 (assumed; stage13 gap)
  Coherence: 8/10 (no prior operations this arc)
  
Operation: Weaving Hafenmark unit Cohesion (Territorial scale — formation of ~100 men)
Scale: Territorial (§11.3: "Weaving a unit's Cohesion is Territorial scale")
  Min TS: 50 ✓
  Ob: 4 (base Territorial), −1 if site-anchored (no site here → Ob 4)
  Coherence cost: −1/op (Territorial auto-cost)
  
Leap roll (Phase 5 timing):
  Pool: Attunement + History bonus + TPS (TS÷10 = 50÷10 = 5)
  Attunement: not in stage13 → GAP. Assuming Attunement 4.
  History: Einhir Scholar (3 pts → +6D)
  Pool: 4 + 6 + 5 = 15D TN7
  Ob: TS 50+ → Ob 1, +1 per Wound (no wounds) = Ob 1
  
  P(≥1 net at 15D TN7): ~99.9%
  P(Overwhelming, ≥2 net): ~99.5%
  Expected: Overwhelming Leap. +1 TS, next op Ob −1.
  
Weaving operation (following Leap):
  Pool: Attunement (4) + Einhir Scholar (6D) + TPS (5) = 15D TN7
  Ob: 4 (Territorial) − 1 (Overwhelming Leap bonus) = Ob 3
  P(≥3 net at 15D): ~99%
  Expected: Success or Overwhelming.
  
  Success: Hafenmark Cohesion +1 (from 3 → 4, removing −1D CP penalty)
  Overwhelming (net ≥6): Cohesion +2.
  Coherence: −1 → Maret Coherence 7/10.
  
Co-movement draw (Territorial Weave, P-01 compliance):
  Temporal: −d3 turns of contact perception available (automatic, §5.2)
  Epistemic: Maret experiences Hafenmark formation as a collective consciousness anchor
  Actual d6: roll range 1–6. On 1–2: equipment of 1 unit member affected (object-level co-movement)
```

**Finding F-ARC31-06 [P2]:** A TS 50+ practitioner with Focus 3 and Attunement 4 is near-deterministic in Territorial-scale operations after an Overwhelming Leap. Pool of 15D vs Ob 3 is effectively always successful. This is working as intended — senior practitioners are powerful. However, the Coherence −1 auto-cost is the only real constraint, and at Coherence 8/10 they have significant headroom. The Coherence track is the binding constraint on practitioner power at this tier, not the Leap or operation rolls. This is correct design.

```
## STATE DELTA: After Thread Support, Phase 5

Hafenmark unit: Cohesion 4 (from 3) → CP penalty removed
Battle dynamics shift: Hafenmark now operates at full CP 3 instead of penalised CP 2.
Effective Pool: 3D OFF + 3D DEF (split decision)

Battle Turn 2 damage reassessment:
  Hafenmark (boosted): 3D TN6 vs Church DEF 2D TN7
  E[net hit] = (3×0.40) − (2×0.27) = 1.2 − 0.54 = 0.66 excess
  Damage: 0.66 + Heavy Cut modifier 4 − Heavy DR 5 = 0.66 − 1 = 0.
  Still zero against Heavy Armour.

CONCLUSION: Weapon matchup problem persists even with Thread support. The Battle is a
stalemate until either: (a) Church deploys HeavyBlunt ranged support, or (b) Thread 
Dissolution targets Church formation directly.
```

**Finding F-ARC31-07 [P1]:** Thread support (Cohesion Weaving) addresses formation integrity but cannot address the fundamental weapon matchup problem. The battle remains a stalemate. **Domain Echo cannot fire from a stalemate** — there is no victory condition met, and no faction stat changes from a drawn battle. This is a systemic gap: the battle system may produce indefinite stalemates when weapon matchup and formation cancel each other out. Real battles are not indefinitely stalemate — fatigue, supply, and strategic context force resolution.

**[PATCH: SIM-ARC31-P05]**
Finding: Mass combat stalemate condition — no rule resolves a battle where neither side can deal damage due to weapon/armour/formation combinations. Expected to occur frequently (Light Cut vs Heavy armour, Heavy Cut vs Shield Wall + Heavy armour, formation negation on both sides).
Mechanic: mass_battle_v3 / §8.9
Proposed change: Add stalemate resolution rule: "If no Size damage is dealt to either unit for 2 consecutive battle turns, each general makes a CR check (Ob 2). Winner gains Feigned Retreat option without opponent CR counter-check. If both fail: battle ends in strategic withdrawal — both sides choose whether to hold position or retreat. No casualties, no morale loss, but 1 Wealth consumed by each faction for supply."
Expected effect: Gives a structured resolution path without requiring one side to be eliminated.
Canon risk: LOW — consistent with historical reality of defensive engagements.

---

# SIMULATION 2: ARC 33 — "THE FORGETTING ROAD"

## Test Tag
```
Test ID: SIM-ARC33-C01
Mechanics: §6.1–6.5 (Southernmost + Forgetting), threadwork_v25 (Ceiral Ritual, Leap, Coherence), §8 (personal combat, Mode 3 entities), §11.3 (Thread→Mass handoff), §7.2 (TC spike)
Mode: HYB | Temporal: CROSS
Tracks: TT, TC, Coherence, TS, COMP, CERT
Factions: Revolution, Church, Hafenmark
NPCs: Maret Uln, Baralta, Himlensendt
Archetypes: Practitioner (expedition lead), Exploration, Social (post-return)
```

---

## Southernmost Entry

```
## State: Expedition Start
Party: 3 practitioners (TS 30, 50, 50+). Non-Thread characters cannot enter (§6.1).
Forgetting boundary: Entry roll not required — it's not a barrier to physical movement.
  Forgetting mechanics: strip intelligibility of purpose, not physical passage.
  
Per §6.1: "TS <30 dissolve without awareness on entry." This is automatic — no roll. 
  Non-practitioners in the party cease to exist as coherent agents. No Wound, no save.
  
  FINDING F-ARC33-01 [P2]: §6.1 says non-Thread-sensitive individuals dissolve "without 
  awareness." This creates a practical guard/escort problem. A practitioner cannot bring 
  non-practitioner support into Southernmost. Any combat encounter inside requires 
  practitioner-only combat pools. This is clearly intended but has no narrative flag 
  in stage6_factions or stage12 — non-practitioner party members are simply removed without 
  a scene. A ruling is needed on whether this fires as a dramatic scene or silently.

[EDITORIAL: ED-ARC33-SIM-01 — Forgetting boundary dissolution: dramatic scene or silent removal?]
Proposed: Silent removal is canon (they don't know it's happening). But the practitioner 
DOES know they are about to lose anyone without TS 30. The scene before entry is the 
dramatic moment, not the dissolution itself. Practitioners must make the conscious 
choice to enter alone.
```

```
## Forgetting Mechanics — Inland Movement

Per §6.1 Forgetting rules:
  Object scale: clear trajectory
  Personal scale: directional only
  Territorial: near-opaque
  Structural: nothing
  
Purpose retention check (proposed gap-fill): GM applies +1 Ob to the next Thread operation 
per scene inside Southernmost without a tactile anchor to purpose (a physical object 
representing the goal). With anchor: no penalty. Without: purpose drift = +1 Ob/scene.
  
FINDING F-ARC33-02 [P2]: §6.1 describes the Forgetting stripping intelligibility but 
provides no mechanical rule for purpose tracking during multi-scene expeditions. The 
narrative says "you can hold the intention but not the content." No roll, no track, no 
counter. For simulation: the GM's judgment is the mechanic. This is functional but 
inconsistent with the game's design principle (mechanics express philosophy).

[EDITORIAL: ED-ARC33-SIM-02 — Purpose tracking in Southernmost: should there be a 
mechanical representation?] Proposed: a simple d3 countdown ("Clarity") per expedition, 
starting at 3. Each scene without a Belief-oriented action drains 1 Clarity. At 0, 
the practitioner cannot formulate new operations (purpose fully stripped). Restore via 
Knot scene. This makes the Forgetting a playable resource rather than purely GM-narrated.
```

```
## Mode 3 Entity Combat

Per §5.13: "Shifting Objects, Gaps, and Monstrous Entities."
Stage13 does not include stat blocks for Mode 3 entities.

GAP-ARC33-SIM-02: No Mode 3 entity stat blocks. Cannot run Mode C simulation without 
mechanical values. Using principled construction:

Entity: "Accumulated Co-Movement Mass" — a configuration that has been spooling without 
intelligibility anchor for 45 years (since the Ceiral network collapsed)
Scale: Personal (it occupies a recognisable spatial presence — one person-sized zone)
CP equivalent: 5 (configurations without intelligibility anchor are pure actuality — 
  they hit hard and have no defence strategy, only presence)
HP equivalent: Coherence 3 (at 0: the configuration collapses, not "dies")
Attack: Not a strike — a configuration-pressure. Forces Coherence check on hit 
  (Spirit TN7, Ob = damage margin)
Defence: None in the combat sense. It does not parry. It is not trying to survive.

Personal combat pool for practitioner vs Mode 3:
  Practitioner Agi: 3 (assumed). Weapon: none — combat is Thread-based.
  Thread combat vs Mode 3: use Thread pool (Attunement + History + TPS) instead of Combat pool
  Ob: 3 (personal scale entity, active)
  
TS 50 practitioner (Maret):
  Thread combat pool: 15D TN7 (per Simulation 1)
  E[net] ≈ 4. vs Mode 3 "Defence" (passive): no defence allocation → all net hits land.
  Damage: 4 excess → applies to entity's Coherence 3.
  Entity Coherence: 3 − 4 = −1 → Collapse. One operation.
  
  But: entity's attack triggered first (declared simultaneously per simultaneous resolution).
  Entity attack: 5D (CP equivalent) at TN7, no declared hit TN modifier.
  E[net attack] = 5 × 0.27 = 1.35.
  
  Maret's defence: he has no combat pool (Thread only). 
  GAP: Can a practitioner defend against a Thread-based attack using Thread pool?
  Proposed: Yes — Thread defence uses same pool as Thread attack (pool split applies: 
  allocate to Off or Def before resolution).
```

**Finding F-ARC33-03 [P1]:** No rule establishes how practitioners defend against Thread-based attacks (Mode 3 entities). Personal combat rules assume physical attack/defence. Thread pool rules assume operations, not combat. Gap: a practitioner in Thread contact against a Mode 3 entity has no defined defence mechanism.

**[EDITORIAL: ED-ARC33-SIM-03 — Thread combat vs Mode 3 entities: pool split or separate defence roll?]**
Proposed: Thread pool splits like Combat pool — allocate to Off (operation intent) and Def (maintaining contact suspension against the entity's configuration pressure) before simultaneous resolution. This is mechanically consistent with the combat system and philosophically grounded (you are splitting your suspended-rendering capacity between directed operation and protective orientation). Blocking: YES — needed before Southernmost encounter can be run.

```
## Ceiral Ritual Simulation

Per §6.5:
  Ritual: Collective Thread operation (all practitioners contributing)
  Requirement: minimum 3 practitioners, each TS ≥30
  Scale: Territorial (canonical — this is a peninsula-level ritual)
  Collective Pool: each practitioner contributes Attunement + Focus to shared pool 
    (collective operations per stage3/threadwork_v25 §5.14)
  Base Ob: 5 (Territorial scale + ritual complexity)
  Each site-anchor reduces Ob by 1. Nearest active site: Peripheral. −1 Ob → Ob 4.
  
Party: TS 30 (Att 3, Focus 2), TS 50 (Att 4, Focus 3), TS 50 (Att 4, Focus 3)
Collective pool: (3+4+4) = 11D (Attunement) + (2+3+3) = 8D (Focus) → combined under 
  collective rules (take the lead practitioner's pool + half of contributors')
  
  STALE PARAMS: §5.14 collective rules state "lead practitioner rolls their full pool; 
  each contributing practitioner adds their Focus ÷ 2 (round down) as additional dice."
  Lead: Maret (TS 50): 15D
  Contributor 1 (TS 50): Focus 3 ÷ 2 = +1D
  Contributor 2 (TS 30): Focus 2 ÷ 2 = +1D
  Total pool: 17D TN7, Ob 4.
  
  E[net] = 17 × 0.27 = 4.59
  P(≥4 net) ≈ ~75%
  P(Overwhelming ≥8 net) ≈ ~20%
  
  Most likely outcome: SUCCESS (75%)
  Coherence cost: −2 per participant (Territorial scale, collective = automatic per §5.2.3)
  Lead practitioner Coherence: −2 → 6/10
  Contributors: −2 each → 6/10, 7/10

Co-movement (Territorial collective operation, P-01 mandatory):
  Temporal: d3 turns of contact perception lost for all participants (Temporal auto-effect)
  Epistemic: All participants experience the collective rendering of the peninsula's 
    Thread substrate simultaneously. Spirit check TN7, Ob 1 or gain new Belief from the 
    experience.
  Actual d6: Result determines one tangible physical effect in Southernmost zone.

TT effect: −3 on ritual Success (§6.5: "sustained cycle")
TT: 55 → 52. Below 60 threshold. RS structural pressure reduced.
```

---

## Post-Return TC Spike

```
## State: Season 3, Post-Expedition Return
TC spike trigger: §7.2 one-time event "Practitioner-healed configuration at territorial scale"
TC: 42 → 45 (+3)

NOTE: No roll. Automatic. This fires regardless of player actions.
Ehrenwall Coup Counter: still 2 (TC 45 ≥ 40 with no Crown action → counter was already 
  marked for Season 2. Season 3: TC still ≥40, Crown still has no action → 
  Counter would increment again IF this is a new season's evaluation.)

FINDING F-ARC33-04 [P1]: TC spike from expedition return fires BEFORE seasonal accounting 
  evaluation of Coup Counter condition 1. If TC was at 40 and spikes to 43, the counter 
  fires for Season 3 even if it was NOT going to fire (TC was below 41 before the spike).
  The expedition's return can directly trigger the coup by pushing TC through the 40 threshold 
  at exactly the wrong moment in the seasonal calendar.

This is an unintended mechanical feedback loop: going to Southernmost to REDUCE TT 
  (beneficial for RS) causes TC spike (harmful) which can trigger Ehrenwall's coup 
  (catastrophic). The game is correctly pricing the cost of Thread knowledge — but GMs 
  and players need to know this cascade exists.
```

**[PATCH: SIM-ARC33-P06]**
Finding: Southernmost expedition reduces TT (good) but triggers TC spike on return (+3, automatic). TC spike may push TC above Coup Counter condition threshold. This is a coherent trade-off but it is undocumented — players have no way to anticipate it from the rules.
Mechanic: §7.2 TC spike event + §8.9 Coup Counter evaluation timing
Proposed change: Add to §7.2 (TC one-time events table): "Note: this event fires before seasonal accounting. GMs should inform players that expedition completion will trigger TC movement before the season's accounting phase."
Expected effect: Information transparency — no mechanical change, only player-facing documentation of the cascade.
Canon risk: NONE.

---

## Summary: Findings Register

| ID | Severity | Description | Type |
|---|---|---|---|
| F-ARC31-01 | P2 | Sovereign Authority Doctrine net-negative expected value on Partial | PATCH |
| F-ARC31-02 | P1-BLOCKER | "Poise" attribute in debate_v1 Phase 5 not in 10-attribute set | EDITORIAL |
| F-ARC31-03 | P2 | Himlensendt structurally favoured in Grand Debate — intended, well-differentiated | NOTED |
| F-ARC31-04 | P1 | Coup Counter evaluation timing vs mid-season TC reduction | PATCH |
| F-ARC31-05 | P1 | Mass combat stalemate — no resolution rule for weapon/armour/formation lock | PATCH |
| F-ARC31-06 | P2 | Senior practitioner near-deterministic at Territorial scale — Coherence is binding constraint | NOTED |
| F-ARC31-07 | P1 | Thread support cannot resolve weapon matchup stalemate; Domain Echo blocked | PATCH |
| F-ARC33-01 | P2 | Non-practitioner dissolution in Southernmost: no dramatic scene rule | EDITORIAL |
| F-ARC33-02 | P2 | Purpose tracking in Southernmost: no mechanical representation | EDITORIAL |
| F-ARC33-03 | P1 | Thread combat vs Mode 3 entities: no defence mechanism defined | EDITORIAL |
| F-ARC33-04 | P1 | TC spike from expedition return can trigger Coup Counter through threshold | PATCH |

## New Patches for Patch Register

PP-159: F-ARC31-01 — Sovereign Authority Doctrine Partial result (defensive social bonus)
PP-160: F-ARC31-04 — Coup Counter evaluation timing (mid-season reduction caveat)
PP-161: F-ARC31-05 — Mass combat stalemate resolution rule
PP-162: F-ARC31-07 — Thread support scope note (cannot address weapon matchup)
PP-163: F-ARC33-04 — TC spike documentation in §7.2 (player-facing note)

## New Editorial Decisions for Ledger

ED-ARC31-SIM-01: Distinction Phase attribute mapping (Poise → Focus or Presence) [P1-BLOCKER]
ED-ARC33-SIM-01: Forgetting dissolution — dramatic scene or silent removal
ED-ARC33-SIM-02: Purpose tracking mechanic in Southernmost (Clarity countdown or GM judgment)
ED-ARC33-SIM-03: Thread combat defence vs Mode 3 entities [P1-BLOCKER]

*Total new patches: 5 (PP-159–163). Total new editorial items: 4. Combined with arc-generation editorials: 9 new items this session.*

*Next simulation priority: Arc 34 (Ehrenwall's Count) for Coup execution mechanics + Martial Law Domain Action interaction. Arc 35 (Klapp Threshold) for Church Stability brake timing. Both blocked by ED-ARC31-SIM-01 (Poise attribute) until resolved.*
