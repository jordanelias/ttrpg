# VALORIA STRESS TESTS — NOVEL CONNECTIONS BATCH
## Simulator Skill · Sonnet 4.6 · 2026-03-27
### Focus: Unexplored mechanic intersections · Mode-switching · Scale escalation/descent

Tags: All tests use CROSS temporal dimension unless noted.

---

## ROUTING TABLE

| Test | Mechanics | Mode Start | Mode End | Scale | Type |
|------|-----------|-----------|---------|-------|------|
| T-01 | M-050 + M-049 + M-051 (Riskbreaker → Inquisitor CE → Devout Constraint collapse) | TTRPG | HYB | Character → Faction | Mode B interaction + D edge |
| T-02 | M-033 + M-038 (TT↔TC↔IP at triple threshold + seasonal accounting) | BG | BG | Global → Faction | Mode C scenario |
| T-03 | M-019 + M-009 + M-029 (Past-Oriented Pulling → Certainty collapse → The Forgetting) | TTRPG | TTRPG | Personal → Exploration | Mode B + D |
| T-04 | M-037 + M-031 + M-036 (Grand Debate → TC spike → Parliamentary Vote void) | HYB | BG | Faction → Global | Mode C |
| T-05 | M-046 + M-044 (Thread operation during Combat Manoeuvres — scale interrupt) | TTRPG | TTRPG | Personal combat → Thread | Mode B + D |
| T-06 | M-024 + M-025 + M-030 (Shifting Object → Gap creation → TT threshold) | TTRPG | HYB | Object → World | Mode D edge |
| T-07 | M-052 + M-008 + M-049 (Concealment vs. passive TS perception vs. Inquisitor CE) | TTRPG | TTRPG | Personal → Institutional | Mode B |
| T-08 | M-023 + M-055 + M-020 (Collective operations + Restoration community weaving → TD accumulation) | HYB | BG | Relational → Faction | Mode C |

---

## T-01: RISKBREAKER → INQUISITOR CE → DEVOUT CONSTRAINT COLLAPSE
**Mechanics:** M-050 (Riskbreakers), M-049 (Inquisitors), M-051 (Devout Constraint)
**Mode:** TTRPG → Hybrid handoff at faction level
**Temporal:** PAST (accumulated exposure) + PRES (collision scene)
**Tracks:** CE (both chars), TS, DD (Deniability Debt), TC, COMP
**Factions:** Crown, Church
**NPCs:** Ehrenwall (Löwenritter commanding Riskbreakers), Church Inquisitor (generic)
**Archetype:** Riskbreaker + Inquisitor + Devout Character

### Scenario Setup

Riskbreaker operative (call: Sorel) has been embedded near a practitioner network. Sorel's CE = 4 (2× direct Thread operation witness). She qualifies for TS growth check. She is also Devout — sincere Church believer, TS currently 0 (theologically foreclosed).

Church Inquisitor (Hadmar) is separately building a file on the same network. His CE = 3 (file building on Thread operation sites). He is at the CE 3 threshold — TS growth check triggers next confrontation.

The scenario: Sorel and Hadmar collide at the extraction site. Neither knows the other is present. A Thread operation fires in front of both simultaneously.

### Initial State

```
## State: Collision Scene
### Characters
Sorel (Riskbreaker) — CE 4, TS 0 (Devout Constraint active), DD 2
  Conditions: Devout Constraint, CE 3+ (qualifies for TS check), active covert operation
Hadmar (Inquisitor) — CE 3, TS 0 (threshold), Investigation Stage 2

### Tracks
TT 34 | TC 22 | IP 25 | DD 2 | PI 7

### Active Conditions
Devout Constraint (Sorel): TS growth checks blocked except Discovery Events
CE Threshold (Hadmar): TS growth check triggers on next confrontation
```

### Action 1: Thread Operation Fires (Practitioner uses Weaving, Relational scale)

Both Sorel and Hadmar witness directly: +2 CE each.

**Sorel:** CE 4 → 6. This is a qualifying **Discovery Event** — the Devout Constraint exception applies (involuntary experience). TS growth check fires.

**Sorel TS Growth Check:** Spirit TN 7 Ob 1.
Pool: Spirit 3D (baseline Riskbreaker, no History bonus for this).
P(≥1 net success at TN7, 3D): ~80%.

**Most likely outcome:** Sorel holds the confrontation. TS +5 → TS 5 (Inert tier, still).

Immediately: **Theological Dissonance Event** fires (she is Devout + Discovery Event).
Spirit TN 7 Ob 1.
P(success, 3D): ~80%.

**Most likely outcome (success):** Framework holds. Constraint re-engages. Certainty −1.

**Hadmar TS Growth Check** (CE 3, confrontation event): Cognition TN 7, Ob 2.
Pool: Cognition 4D (Inquisitor formation).
P(≥2 net at TN7, 4D): ~50%.

**Expected outcome:** ~50/50. On success: TS develops toward Dormant (TS 0 → 5). Hadmar is now at the CE 3 crisis — Doubling Down / Fracture / Conversion trajectory opens.

### State Delta After Action 1
```
Sorel — CE 6, TS 5, Certainty −1, Devout Constraint ACTIVE (held), Dissonance Marks: 0
Hadmar — CE 5, TS 0–5 (50% branch), Crisis trajectory: open
```

### Action 2: Sorel Recognises Hadmar as Church (Circles)

Sorel attempts to disengage without exposing her operation. Crown vs Church operational conflict.
Presence + Espionage History (3D) vs Ob 2 (neutral party, professional context).

**But:** Crown DD is currently 2. If Sorel's operation is exposed here → DD 3 → Crown Domain Actions vs non-Crown factions +1 Ob.

P(success 3D TN7 Ob 2): ~70%.

**Most likely outcome:** Sorel disengages cleanly. DD remains 2.
**Failure path:** Hadmar logs Crown operative presence. DD → 3. Parliament erosion begins.

### Interaction Finding

**P2 — Devout Riskbreaker at CE threshold is a double-keyed trigger.** The Devout Constraint exception (Discovery Event) fires simultaneously with the CE 3+ Riskbreaker TS check. The rules don't specify priority between the two. Both require Spirit checks in the same scene, with different Obs (Ob 1 for TS growth, Ob 1 for Dissonance, but these are sequential not parallel — order matters for Certainty budget).

**Fix needed:** Specify that TS growth check fires first, then Dissonance Event fires on that check's result. Currently silent.

### Mode Shift: TTRPG → Hybrid

At faction level: Sorel's CE 6 and Hadmar's CE 5 feed into faction accounting. In Hybrid mode:
- Crown DD 2 (held) must be tracked on the faction sheet
- Church gains CE data on a Crown operative — Intel +1D vs Crown for 1 season if Hadmar files successfully

**BG-mode implication:** Neither CE nor DD are BG-mode track. Gap confirmed.

### Findings Summary
| # | Severity | Finding |
|---|----------|---------|
| 1 | P2 | Devout Riskbreaker at CE threshold: simultaneous TS growth + Dissonance triggers — priority not specified |
| 2 | P2 | Certainty budget under simultaneous track deductions (both Dissonance Ob 1 and Certainty −1 on success) needs order-of-operations clarification |
| 3 | P3 | CE track has no BG-mode equivalent — hybrid handoff loses this state |

---

## T-02: TRIPLE CLOCK THRESHOLD + SEASONAL ACCOUNTING
**Mechanics:** M-033 (Clock Interactions), M-038 (Seasonal Accounting)
**Mode:** BG → BG (board game only — this is a BG-specific scenario)
**Temporal:** PRES + FUT
**Tracks:** TT, TC, IP — all at threshold simultaneously
**Factions:** All
**NPC:** Baralta (TC suppressor), Almud (Royal Decree)
**Archetype:** Faction Leader ×3

### Scenario: Three Clocks Hit Threshold Simultaneously at Accounting

Starting state: TT 48, TC 49, IP 49 (all one step from major thresholds — TT 50, TC 50, IP 50).

In BG mode, Domain Actions fire during the season, then Accounting resolves. Two factions take actions that each push one clock by +1. A third action triggers +1 TT from a failed Thread exposure event.

All three clocks cross threshold simultaneously at accounting.

### Initial State (BG mode)
```
### Tracks
TT 48 | TC 49 | IP 49
### Faction Stats
Crown — Mandate 5 / Reach 4 / Wealth 5 / Stability 6
Church — Mandate 6 / Reach 5 / Piety 5 / Stability 5
Hafenmark — Mandate 4 / Reach 4 / Wealth 4 / Stability 5
Baralta TC Suppression: ACTIVE (Mandate 4+)
```

### Accounting Trigger Sequence

At accounting, clocks update based on:
- Church Mandate 5+ → TC +1 (rule: §8.3)
- Himlensendt institutional driver active → TC +1
- Failed covert operation in Altonian-adjacent territory → IP +1
- TT base rate → +1/season (assumed background drift)

**Result:** All three clocks would hit threshold simultaneously.

### Clock Interaction Rule Check (M-033)

The ruleset specifies TT↔TC↔IP cross-effects but does **not** specify resolution order when multiple thresholds are crossed in the same accounting phase.

**TT 50 effect** (first major threshold): Thread operations in populated areas increase difficulty. TT 50 is a "visibility threshold" — Thread events become more common.

**TC 50 effect**: Templars become deployable without royal authorisation. Church Military actions lose the "royal authorisation" constraint.

**IP 50 effect**: Altonian delegation arrives with non-negotiable demands. One political action this season must be the IP response.

**Conflict:** TC 50 enables unilateral Templar deployment. IP 50 mandates a political response. If the Church deploys Templars as its IP-response action, that is legal under TC 50 but violates the IP response's implicit expectation of diplomatic engagement.

**Baralta's TC suppression** at Mandate 4+: suppresses TC at −1/season. But the threshold was crossed at accounting, *then* suppression would apply. Does suppression prevent the threshold effect? The rules are silent on whether suppression prevents threshold crossing vs. reduces the post-crossing value.

### Critical Ambiguity: Suppression Timing

| Interpretation A | TC grows to 50 → threshold fires → suppression reduces to 49 (threshold already fired) |
|---|---|
| **Interpretation B** | TC grows to 49 + Baralta suppresses to 48 → threshold does NOT fire |
| **Mechanical difference** | Templar autonomy either activates this season or doesn't |

**P1 finding.** In a high-stakes BG endgame, whether Interpretation A or B applies determines whether the Church can unilaterally deploy militarily this season. This is a decisive mechanical divergence with no rule text resolution.

### Probability Analysis: How Common Is This State?

Starting from TT 28, TC 15, IP 20 (Session Zero values), reaching all three at 48–49 simultaneously requires ≈ 20–25 seasons of campaign play. This is late-game, but the late game is where BG mode is decided. **Frequency: low but peak-stakes.**

### Further Interaction: Royal Decree at Triple Threshold

Almud has Royal Decree (once/season, bypasses Domain Action timing). At this junction:
- He could use it to push Church Reach −1 (weakening Templar deployment effectiveness)
- But this requires Mandate vs Ob 2 → Royal Decree Ob penalty for consecutive use applies

If he has used Royal Decree last season: Ob becomes 3. Pool: Mandate 5D, TN 7, Ob 3.
P(≥3 net, 5D): ~45%.

**P2:** Crown's primary counter to TC threshold crossing has only 45% success rate at exactly the moment it's most needed (consecutive use fatigue). This feels designed, but the interaction between Decree fatigue and threshold timing means the Crown's ability to suppress TC crossing is significantly worse in late-game than early-game — which may be intended as escalation design, but should be confirmed.

### Findings Summary
| # | Severity | Finding |
|---|----------|---------|
| 1 | **P1** | Baralta TC suppression timing vs. threshold crossing: no rule specifies whether suppression prevents crossing or applies after. Decisive military consequence. |
| 2 | P2 | Triple threshold crossing has no resolution order — three simultaneous constraint activations with potential contradictions |
| 3 | P2 | TC 50 + IP 50 together allow Church to use Templar deployment as its mandatory IP response — diplomatically contradictory but mechanically legal |
| 4 | P3 | Royal Decree consecutive-use fatigue peaks exactly at late-game threshold moments — may be intentional escalation design; flag for confirmation |

---

## T-03: PAST-ORIENTED PULLING → CERTAINTY COLLAPSE → THE FORGETTING
**Mechanics:** M-019 (Past-Oriented Pulling), M-009 (Certainty Track), M-029 (The Forgetting)
**Mode:** TTRPG
**Temporal:** PAST + CROSS
**Tracks:** CERT, TD, INT, TS
**Factions:** Varfell, Niflhel
**NPC:** Vaynard (knowledge seeker), Maret Uln (practitioner guide)
**Archetype:** Practitioner + Non-TS Scholar

### Scenario: Scholar-Adjacent Practitioner Conducts Past-Oriented Pull in Southernmost

Maret Uln (TS 52 — Attuned, qualifies for Relational operations) conducts Past-Oriented Pulling to recover pre-Calamity memory of a Varfell territorial claim. Vaynard is present as observer (TK 3, TS 14 Dormant).

**Why this connection is novel:** Past-Oriented Pulling in the Southernmost interacts with The Forgetting (M-029) — the zone exit mechanic strips memory of what was experienced. If a Past Pull retrieves information, then the character exits the Southernmost, The Forgetting should theoretically erase the retrieved memory. The ruleset does not address this interaction.

### Initial State
```
### Characters
Maret Uln — TS 52, TD 6/20, Taint 2/10, Certainty 4/6, INT 7
Vaynard — TS 14 (Dormant), TK 3, Certainty 3/5

### Tracks
TT 36 | TC 22 | IP 28

### Zone
Southernmost active — Forgetting rules apply on exit
```

### Action 1: Past-Oriented Pulling (Maret Uln)

**Requirements:** TS 70+ for Past-Oriented Pulling (§4.4 table: "70–89 Sensitive — Past-Oriented Pulling"). 

**STOP.** Maret Uln at TS 52 (Attuned tier) does **NOT** qualify for Past-Oriented Pulling. Minimum TS is 70. This is itself a finding — the scenario as commonly imagined (experienced practitioner doing memory recovery) requires Sensitive tier, which is rare.

**Finding P2:** Players commonly conflate Attuned (full operations) with access to Past-Oriented Pulling. The TS 70 threshold is buried in the table — needs surfacing.

Assuming an adjusted scenario with Maret Uln at TS 72 (Sensitive):

**Roll:** Focus + relevant History (Memory History 3D) at TN 8 (Desperate equivalent per §1.2 — Past-Oriented Pulling is explicitly TN 8).
Pool: Focus 4 + Memory History 3 = 7D. TN 8. Ob (Relational scale): 3.
P(≥3 net at TN8, 7D): At TN8, P(success per die) = 0.3. Expected net = 7 × 0.2 = 1.4. 
P(≥3 at this rate): ~25%.

**This is hard.** Even a 7D pool has only ~25% success rate at Ob 3 TN 8.

**Most likely outcome: Partial** (~40%). Memory recovered with complication (distorted, fragmentary, costs extra).

### Cost Stack at Partial
- Past-Oriented Pulling: −1 Intelligibility (additional, per §4.5)
- Relational scale operation: −1 Intelligibility
- Each Thread operation at Relational+ scale: −1 INT
- Total INT cost this operation: −3

Maret Uln INT: 7 → 4. Now at **Fragmented state**: −1D to all social rolls, Close Knots at wrongness threshold.

Additionally: Certainty −1 (Leap cost, per §4.6). Certainty: 4 → 3.

### Action 2: Zone Exit — The Forgetting

The Forgetting (M-029) strips memory of what was experienced in the Southernmost on exit. The ruleset (from checkpoint 14) specifies this as a zone-exit mechanic.

**Critical interaction:** The Past-Oriented Pull retrieved a specific memory (pre-Calamity territorial record). This is now held knowledge. The Forgetting fires on exit.

**The Forgetting strips the retrieved memory.** The practitioner has spent INT 3 levels, a Certainty point, and likely taken Knot strain — for information that cannot exit the zone.

**But:** Does The Forgetting erase the practitioner's *awareness that they retrieved something*, or only the content? This distinction is mechanically significant:
- If content only: character knows "I found something important and lost it" — narrative tragedy
- If awareness: character exits not knowing they did a Pull — wasted resources with no narrative hook

The ruleset is silent on this distinction. **P1 finding** — this is the core experiential logic of the Southernmost mechanic and it's undefined.

### Vaynard's Observer Position

Vaynard (TS 14 Dormant) was present. He *observed* the Pull but cannot perceive Thread-level content. At TS 14 (Dormant): "Passive awareness; no Thread operations" — he perceives wrongness but not content.

**Does The Forgetting affect him on exit?** He observed something he can't fully articulate. If The Forgetting strips his memory of the observation, his TK investment in this expedition is lost. If it doesn't (because he's not a practitioner), he exits with a vague memory of "something important happened" — potentially TK +1 (awareness of operational capacity without content).

**P2:** The Forgetting's applicability to Dormant/non-practitioners is unspecified.

### TD Cascade Check

Maret Uln's TD at 6/20 before this operation. Past-Oriented Pulling is a PAST temporal operation. Does it generate TD? The ruleset specifies TD increases from temporal operations but doesn't list Past-Oriented Pulling specifically in the TD accumulation table.

If it does: TD 6 → 8 (two temporal operations this scene). At TD 10: co-movement threshold. **P2** — clarify Past-Oriented Pulling's TD cost.

### Findings Summary
| # | Severity | Finding |
|---|----------|---------|
| 1 | **P1** | The Forgetting vs. retrieved memory: undefined whether content or awareness is stripped |
| 2 | P2 | The Forgetting applicability to non-/Dormant practitioners unspecified |
| 3 | P2 | Past-Oriented Pulling TS threshold (70+) likely to be missed — needs surfacing in operation descriptions, not just TS table |
| 4 | P2 | Past-Oriented Pulling's TD accumulation cost not specified in TD table |
| 5 | P3 | 7D pool at TN8 Ob3 = ~25% success — harsh but probably intentional for rare operation |

---

## T-04: GRAND DEBATE → TC SPIKE → PARLIAMENTARY VOTE VOID
**Mechanics:** M-037 (Grand Debate), M-031 (Theocracy Clock), M-036 (Parliamentary Vote)
**Mode:** Hybrid → Board Game
**Temporal:** PRES + FUT
**Tracks:** TC, PI (Parliament Integrity), FSTAT (Church Mandate, Crown Mandate)
**Factions:** Crown, Church, Hafenmark
**NPC:** Himlensendt (Confessor), Almud (King), Baralta (Duchess)
**Archetype:** Faction Leader × 3

### Scenario: Inquisition Conviction → TC Spike Damages Parliament

An Inquisitor investigation reaches Stage 3 (Conviction Hearing — Grand Debate). A practitioner PC is convicted. Per §13.6: Conviction → TC +2. Parliament Integrity is currently 5 (degraded from starting 7).

Following conviction: Church Mandate +1 (institutional victory). Himlensendt drives TC further per his TC generation rule: Church Mandate 5+ → TC +1/season at accounting.

### Grand Debate Mechanics

Grand Debate: 5 exchanges. Pool: Cognition + relevant History (accused) vs Church Reach-based pool (Inquisitor).

Accused PC: Cognition 4, History "Scholar of the Old Ways" 3 = 7D. TN 7.
Inquisitor: Church Reach 5D + Cognition 3 = 8D. TN 7.

**Per exchange expected:** Accused nets 7 × 0.33 = 2.3. Inquisitor nets 8 × 0.33 = 2.6. Church has slight edge per exchange.

Over 5 exchanges, expected Church wins: ~3/5 exchanges. Conviction is likely unless PC invests Momentum or Inspirations.

**Post-conviction:** TC +2. Current TC 22 → 24.

### TC Spike Into Parliament Integrity Interaction

At Parliament Integrity 5: Parliamentary Votes operate at standard Ob (per §14.1). But **what does TC 24 do to Parliamentary function?**

The TC threshold effects in the ruleset:
- TC 50: Templars deployable without royal auth
- TC 75: Forced prayer obligations
- TC 100: Full theocracy

TC 24 is mid-range. **No explicit PI degradation trigger from TC** is listed at this level.

**But:** The Church's post-conviction position (Mandate +1) means they can now use Excommunication more readily (requires Mandate ≥ 3 — they're at 5+). If they excommunicate a Crown-aligned Parliamentarian: that member loses "barred from public office" → effective removal from Parliament.

**Parliament Integrity interaction:** If excommunication removes a Parliamentarian, does PI drop? The ruleset specifies PI degrades through "events" but doesn't map excommunication specifically to PI loss.

**P2:** Excommunication of Parliamentarians has no specified PI consequence. This is an obvious use case in post-conviction political play.

### Mode Switch: TTRPG Conviction → BG Consequence

In Hybrid mode, the Grand Debate resolves in TTRPG (full exchange narration). The TC +2 and Church Mandate +1 feed forward into the BG faction sheet.

**BG accounting at next season:**
- Church Mandate 6 now (was 5 post-conviction +1)
- TC generation: Church Mandate 5+ → TC +1. With Mandate 6: does this apply twice? The rule says "Mandate 5+" not "Mandate 5 exactly." With Mandate 6, the base generation still fires once.
- Baralta TC suppression: −1/season if Mandate 4+. Her Mandate is 4 — suppression holds.

**Net TC movement per season:** +1 (Church base) − 1 (Baralta suppression) = net 0. TC stable at 24.

**P3:** A conviction that cost TC +2 and elevated Church Mandate is neutralised by Baralta's passive suppression within one season. This may feel anticlimactic — the narrative weight of conviction doesn't produce lasting TC movement if Baralta remains functional.

### Parliamentary Vote at PI 5

Faction attempts a Parliamentary Vote to expel the convicted practitioner's patron (Crown-aligned noble).

PI 5: "Standard Ob." Vote requires: Mandate contest (Crown vs Church vs Hafenmark coalition).

Crown Mandate 5, Church Mandate 6, Hafenmark Mandate 4. Church + Hafenmark coalition = 10 Mandate pool vs Crown 5.

Crown cannot win a straight Mandate contest here. Crown's only recourse: Royal Decree (bypasses timing, but cannot target Intel and is limited to one/season, already used).

**Deadlock detected:** Crown is outmanoeuvred in Parliament after conviction but has no procedural recourse if Royal Decree is spent. Crown can only wait for next season.

**P2:** Post-conviction political lockout for Crown has no emergency procedural exit. This may be intended (losing should have real costs) but should be confirmed as design intent rather than gap.

### Findings Summary
| # | Severity | Finding |
|---|----------|---------|
| 1 | P2 | Excommunication of Parliamentarians → no PI degradation rule |
| 2 | P2 | Post-conviction Crown lockout: no emergency procedural exit if Royal Decree spent |
| 3 | P3 | Baralta suppression neutralises conviction TC spike within 1 season — narrative/mechanical weight mismatch |
| 4 | P3 | TC 24 has no explicit Parliamentary effects — mid-range TC may need some friction effects below threshold |

---

## T-05: THREAD OPERATION DURING COMBAT MANOEUVRES — SCALE INTERRUPT
**Mechanics:** M-046 (Thread Ops in Combat), M-044 (Combat Manoeuvres)
**Mode:** TTRPG
**Temporal:** PRES
**Tracks:** COMP, Health, TS, TD, TT
**Factions:** Löwenritter, Revolution
**NPC:** Ehrenwall (Löwenritter Knight)
**Archetype:** Löwenritter Knight vs Practitioner

### Scenario: Practitioner Attempts Weaving During a Disarm Manoeuvre

Ehrenwall attempts a Disarm manoeuvre against a practitioner. The practitioner, anticipating the disarm, initiates a Thread operation (Object-scale Weaving on Ehrenwall's sword) during the same round.

### Combat Priority Question

Combat uses the Priority Table (M-040). Thread operations in combat (M-046) — where do they sit in priority?

The ruleset states Thread operations in combat use the same initiative structure. But Weaving at Object scale targets an object being actively used in a combat manoeuvre. **Both actions resolve on the same object (the sword) in the same round.**

**Resolution conflict:**
- Ehrenwall's Disarm resolves on Practitioner's weapon (targets practitioner).
- Practitioner's Weaving resolves on Ehrenwall's sword (targets Ehrenwall's weapon).
- These are simultaneous versus actions targeting different objects that affect the same exchange.

**No rule specifies simultaneous targeting of the same exchange's weapons.** Do they resolve simultaneously? Does the higher priority-table actor resolve first? Does the Thread operation interrupt the manoeuvre?

**P1 finding** — this situation will arise in any campaign with a Practitioner in combat against a melee opponent using manoeuvres.

### Resolution Attempt

**Option A (sequential, initiative order):** Ehrenwall has higher Initiative → Disarm resolves first → if Disarm succeeds, practitioner loses weapon before Weaving fires → Weaving targets are now disrupted.

**Option B (simultaneous):** Both resolve in parallel. Disarm result and Weaving result are calculated independently, then applied. Practitioner could successfully Weave Ehrenwall's sword *and* lose their own weapon in the same moment.

**Option B creates an interesting outcome:** Ehrenwall's sword has a Woven configuration applied to it mid-disarm. The Disarm still succeeds, but Ehrenwall is now wielding a Thread-modified weapon. Does he know? TS check? At TS 0 (Ehrenwall — no Thread perception): no awareness.

### Probability Snapshot

**Ehrenwall Disarm:** Coordination + Weapon History 3D + Combat 2D = 7D vs Ob (Practitioner Defence pool net successes). Assume Practitioner defends 4D net ~1.3 → Ob 2 effectively.

P(Ehrenwall Disarm ≥ 2 net, 7D): ~70%.

**Practitioner Weave (Object scale, TN 7, Ob 1):** Focus 3 + Thread History 2 = 5D.
P(≥1 net, 5D, TN7): ~92%.

**Most likely outcome (Option B):** Ehrenwall disarms practitioner (~70%) AND practitioner successfully Weaves Ehrenwall's sword (~92%). Both succeed. Combined probability: ~65%.

### Woven Sword State

Ehrenwall now holds a Thread-modified weapon with no awareness. The Weaving effect (Object scale) persists. In TTRPG mode: GM decides Weaving effect. In BG mode: there is no mechanism for carrying forward a "thread-modified object" state on a weapon card.

**BG gap confirmed:** No BG-mode mechanic handles Thread-modified objects in combat. **P2.**

### TT Consequence

Any Thread operation: TT accumulation. Object-scale Weaving in combat: +TT per standard operation rules. At TT 36: standard mid-game. No threshold crossed here.

### Findings Summary
| # | Severity | Finding |
|---|----------|---------|
| 1 | **P1** | Simultaneous Thread operation + combat manoeuvre targeting same exchange: resolution order unspecified |
| 2 | P2 | Thread-modified objects in combat have no BG-mode carry-forward state |
| 3 | P3 | Ehrenwall (TS 0) cannot perceive Woven sword — creates a persistent hidden condition with no detection path for that character |

---

## T-06: SHIFTING OBJECT → GAP CREATION → TT THRESHOLD CHAIN
**Mechanics:** M-024 (Shifting Objects), M-025 (Gaps), M-030 (Thread Tension)
**Mode:** TTRPG → Hybrid (zone management)
**Temporal:** CROSS (object exists in past/present simultaneously)
**Tracks:** TT, TD, TS
**Factions:** Varfell, Church (Inquisitor response)
**NPC:** Vaynard (as instigator), Almud (political consequence)
**Archetype:** Practitioner + Non-TS Scholar

### Scenario: Vaynard's Collection Triggers a Shifting Object Cascade

Vaynard uses The Private Collection (Intel Ob 2). Success. He deploys an Originary Lock for Thread-related Domain Action +2D. 

Each use: +1 TS (current TS 14 → 15). At TS 14+, each use triggers Spirit check TN 7 Ob 1 for Discovery Event.

**Spirit check:** Pool Spirit 2D (Vaynard is not a combat character). P(≥1 net, 2D, TN7): ~64%.

**Most likely outcome:** 64% Discovery Event. Assume it fires.

On Discovery Event: if TS reaches 30+ during the event, Spontaneous Breakthrough available. But TS 15 is still Dormant — no breakthrough. TS growth check (Spirit TN 7 Ob 1): 64% → TS 20.

TS 20 → still Dormant. Vaynard now *knows* something without vocabulary for it.

### The Originary Lock as a Shifting Object

An Originary Lock is a Thread-locked object. It is — by category — a Shifting Object (M-024). Shifting Objects have deterioration rates and stabilization requirements.

**How long has Vaynard's collection held these objects?** Each Shifting Object has a deterioration clock. If any have exceeded stability threshold without practitioner maintenance, they are degrading.

**Degrading Shifting Object → Gap risk (M-025):** A Shifting Object that deteriorates fully creates a Gap. A Gap in Varfell's collection — in a ducal archive in the capital — is a serious problem.

### Gap Formation at Political Site

Gap at Ob 1 (Object-scale Gap in enclosed space): TT +5 (immediate incursion risk). TT 36 → 41.

**TT 41:** No threshold crossed (TT 50 is next). But the Gap in the ducal archive triggers:
- All characters within Close range: TS growth check available (Gap = qualifying held confrontation event)
- Vaynard's archivists (non-practitioners, no TS): they experience wrongness → Circles complications in Varfell's network

### Church Intelligence Response

Gap at a ducal archive — this is *exactly* what Inquisitors track. Church Intel check vs Varfell Intel: Church 4D vs Varfell Intel 4D.

If Church detects the Gap: Investigation opens. Church Intel +1D vs Varfell for 1 season. TC +1 (heresy evidence in ducal possession).

**Interaction chain:** Vaynard uses Collection → Discovery Event → Shifting Object deteriorates → Gap forms → Church Intel detects → TC +1 → Vaynard's TK advances (he now knows what he has is dangerous) → TK 3 → 4 (TC +2).

**TC total from this chain:** TC 22 + 1 (detection) + 2 (TK 4 advancement) = TC 25.

**This is a single Collection use that produces a 3-step TC cascade.** The rules contain no warning about this interaction. A player deploying the Collection repeatedly in mid-game could inadvertently drive TC 15 points in a few seasons.

**P1 finding:** Private Collection → Shifting Object deterioration → Gap → Church detection → TC cascade is not modelled as a risk in the Collection's rules text. Players are warned only about "+1 TS per use" not about the structural risk of the objects themselves.

### Mode: Hybrid Gap Management

In Hybrid mode, the Gap exists as both a TTRPG scene location and a BG faction event. The BG mode needs:
- A Gap token placed in Varfell's territory
- TT updated on the global track
- Church Intel boost applied to faction sheet

**BG-mode Gap handling:** The checkpoint 14 ruleset includes Gap mechanics in TTRPG detail but does not specify BG-mode Gap token rules, placement procedures, or the BG consequence table for an unremediated Gap. **P2.**

### Findings Summary
| # | Severity | Finding |
|---|----------|---------|
| 1 | **P1** | Private Collection repeated use → Shifting Object deterioration → Gap → TC cascade not modelled as risk in Collection rules text |
| 2 | P2 | Gap mechanics have no BG-mode token placement or consequence table |
| 3 | P3 | Vaynard's archivists experiencing wrongness from a Gap: Circles complications are implied but not mechanically specified |

---

## T-07: CONCEALMENT VS. PASSIVE TS PERCEPTION VS. INQUISITOR CE
**Mechanics:** M-052 (Concealment), M-008 (Thread Sensitivity passive perception), M-049 (Inquisitors)
**Mode:** TTRPG
**Temporal:** PRES
**Tracks:** CE, TS, TD, DD
**Factions:** Church, Revolution (practitioner support)
**NPC:** Himlensendt (indirect — institutional), Inquisitor generic
**Archetype:** Practitioner + Inquisitor

### Scenario: Practitioner Uses Concealment Against an Inquisitor With TS 10

An Inquisitor (Hadmar, CE 3 from T-01, now TS 5 from that scenario — assume TS growth confirmed) encounters a practitioner conducting a Personal-scale Weaving. The practitioner uses Concealment (M-052) to hide the operation.

**Key question:** At TS 5 (Inert), the Inquisitor perceives nothing Thread-related. At TS 10 (Dormant threshold), passive perception activates: "Wrongness near Gaps, Shifting Objects, Intelligibility 3- practitioners." Personal-scale Weaving may not qualify as "wrongness" at this tier.

Hadmar is at TS 5. He doesn't passively perceive the operation. Concealment isn't tested against him because he can't detect what he can't perceive.

**But CE continues:** Hadmar is in the same space as the operation. CE +2 (direct witness, even without TS perception). CE 3 → 5.

At CE 5: Hadmar now qualifies for TS 10+ via growth exposure. Next confrontation event → TS growth check.

### Concealment Mechanic Check

M-052 rules: Concealment hides the operation from observers capable of detecting it. The Ob for Concealment scales with observer TS tier.

**Question:** Does Concealment apply when the observer lacks TS entirely (TS 0–9)? If the observer cannot detect the operation, Concealment may be unnecessary — and therefore not trackable.

**But:** Concealment also has a Certainty cost or pool spend component (rules pending verification). If a practitioner burns resources on Concealment against an Inert observer, that is resource waste.

**Gap:** The Concealment rules (as referenced in M-052) don't specify whether Concealment only operates against TS 10+ observers or applies universally. If a practitioner must assess observer TS before deciding to Conceal, that requires a perception check that itself might reveal something. **P2.**

### Inquisitor Investigation Procedure Integration

Hadmar is simultaneously running Investigation Stage 1 (File Building: Church Reach, Ob 3). His personal CE accumulation is separate from the institutional investigation.

**Parallel tracking problem:** Hadmar has:
- Personal CE track (5)
- Institutional Investigation Stage (1 of 3)
- TS development track (5, growing)
- Church faction Intel track (relevant to Reach roll)

In TTRPG mode: manageable. In BG mode: none of these individual NPC tracks exist. An Inquisitor NPC in BG mode has no personal CE, no individual TS, and investigation procedure collapses to a Reach vs Ob roll.

**Mode translation gap:** The Inquisitor is one of the most mechanically complex NPC types in TTRPG mode and essentially absent in BG mode. **P2.**

### Concealment vs. Passive Perception at TS Boundary

Assume Hadmar reaches TS 10 mid-investigation. He now passively perceives "wrongness near Shifting Objects, Intelligibility 3- practitioners."

**Intelligibility 3- practitioners:** A practitioner at INT 4 (Fragmented) — as Maret Uln was after T-03 — is now *automatically detectable* by a TS 10 Inquisitor via passive perception, **without any Concealment check.**

This means: Concealment (M-052) cannot protect a practitioner whose Intelligibility has degraded to 4 or below against any TS 10+ observer. Concealment protects against active detection of operations. Passive perception of *the practitioner's state* bypasses Concealment entirely.

**P1 finding:** A practitioner who accumulates INT damage (normal campaign arc) becomes passively detectable to any Dormant observer (including newly-awakened Inquisitors). Concealment does not address this. No rule tells practitioners they become visible in this way. This is both a significant play-experience surprise and a canon-interesting mechanic (rendering failure = perceptual exposure), but it needs to be explicit.

### Findings Summary
| # | Severity | Finding |
|---|----------|---------|
| 1 | **P1** | INT 4- practitioners are passively detectable by TS 10+ observers — Concealment does not protect against this; rule not surfaced to practitioners |
| 2 | P2 | Concealment applicability to TS 0–9 observers unspecified — potential resource waste with no rules guidance |
| 3 | P2 | Inquisitor NPC has no BG-mode equivalent for CE/TS/investigation procedure |

---

## T-08: COLLECTIVE THREAD OPERATIONS + RESTORATION WEAVING → TD CO-MOVEMENT
**Mechanics:** M-023 (Collective Thread Ops), M-055 (Restoration Community Weaving), M-020 (TD Track)
**Mode:** Hybrid → Board Game (Restoration faction action)
**Temporal:** CROSS (community operating on collective past/present)
**Tracks:** TD, TT, TC, TS (all participants), COMP, Knot strain
**Factions:** Revolution (Restoration), Church (counter)
**NPC:** Lenneth (scholar-adjacent), Maret Uln (practitioner lead)
**Archetype:** Practitioner × group, Faction Leader (Revolution)

### Scenario: Restoration Community Performs Large-Scale Collective Weaving at an Einhir Site

The Restoration community uses M-055 (Community Weaving) to perform a Structural-scale operation (Ob 6+) on an Einhir site. This requires collective Thread operations (M-023): multiple practitioners contribute their pools.

**Setup:** 3 practitioners (Lead: Maret Uln TS 72; Support 1: TS 50; Support 2: TS 40).

Collective operation rules (M-023): Lead practitioner directs. Each support practitioner contributes dice to the pool. Support contribution capped by their TS tier relative to the operation's scale.

Support 1 (TS 50, Attuned): Can contribute to Relational scale. Structural scale is one tier above. Contribution capped? Rules unclear. **P2 gap.**

Support 2 (TS 40, Stirring): Structural scale is two tiers above. Cannot contribute directly per TS table (max Object/Personal scale at Stirring). Participation as anchor only? Rules don't specify anchor mechanics for under-threshold practitioners. **P2 gap.**

### Pool Construction (Collective Ob 6 operation)

Lead: Focus 4 + Thread History 3 = 7D.
Support 1: contributes 3D (capped at Attuned contribution to above-tier op).
Support 2: anchor only — may provide +1D for shared presence and communal grounding.

Total pool: ~11D. TN 7. Ob 6.

Expected net (11D): 11 × 0.33 = 3.6. 

P(≥6 net, 11D): This requires sustained high rolls. Using binomial approximation: P(success) ≈ 15%. Structural-scale collective operations are very hard, as intended.

**Most likely: Partial** (~35%). Operation partially succeeds with complication.

### TD Accumulation (All Three Practitioners)

Structural-scale operation = major temporal engagement. TD cost:

| Participant | Scale Contribution | TD Gain |
|---|---|---|
| Lead (Maret Uln) | Full structural | +3 TD |
| Support 1 | Above-tier contribution | +2 TD (above normal relational) |
| Support 2 | Anchor only | +1 TD (passive exposure) |

**Maret Uln TD:** 6 → 9. At TD 10: co-movement threshold approaches.
**Support 1 TD:** Assume 4 → 6.
**Support 2 TD:** Assume 2 → 3.

**Co-movement check (M-020 + P-01 Inseparability):** If Maret Uln hits TD 10 during the operation, what fires? The co-movement procedure is described as a narrative/mechanical event requiring a response. Does it interrupt the operation mid-execution? Or does it resolve at operation completion?

**P1 finding:** Co-movement trigger mid-collective-operation is undefined. If the lead practitioner's TD crosses threshold mid-operation, the collective pool is already committed. Can the operation continue with a co-movement event running simultaneously? This is the most complex possible temporal state: a Structural-scale collective operation with a lead practitioner in TD co-movement.

### TT Consequence

Structural-scale operation: TT +5 (estimated for a Structural op). TT 36 → 41.

**Einhir site amplification:** The operation is conducted at an Einhir site. The ruleset specifies Einhir sites as Thread-dense locations. Does an Einhir site modify TT generation from operations conducted there?

The rules preserve the site (reduce deterioration) but don't specify TT modification for on-site operations. **P3** — gap in Einhir site operation rules.

### Church Response in BG Mode

This is a Restoration community action visible to Church Intel. In BG mode, the Church's response to a Structural-scale Thread operation is triggered via their Institutional Tendency (suppress heresy, accumulate intel).

**Church Intel check:** Church Intel 4D vs Revolution Stability 4 → Ob 2.
P(≥2 net, 4D, TN7): ~50%.

If Church detects: TC +2 (major practitioner operation in public space), TC 22 → 24. Investigation opened.

**BG-mode collective operation visibility:** In BG mode, does a Structural-scale operation automatically trigger Church detection, or is it a contested roll? The distinction matters: if automatic, Restoration can never do Structural work without a TC cost, which may make M-055 non-viable in BG. **P2.**

### Knot Strain from Collective Operation

All three practitioners are Knot-connected (the Restoration community is defined by relational bonds). The operation generates Knot strain through:
- INT decay: Maret Uln INT may drop
- Call a Knot (if any used for pool boost): +2 strain
- External events (the operation targets their shared community space)

If Support 2 (lowest TS, least equipped) accumulates Knot strain from the TD exposure: her Close Knots approach Wrongness threshold faster than the experienced practitioners. She may become a structural vulnerability in the community — her relationships deteriorate as the most sensitive members notice she's struggling.

**Canon resonance (P-12 Relational Contagion):** This is exactly the philosophical mechanic — Thread engagement propagates through relational bonds. The mechanical expression is correct but needs to be explicit in M-055 rules text. **P3 flag.**

### Findings Summary
| # | Severity | Finding |
|---|----------|---------|
| 1 | **P1** | Co-movement trigger mid-collective operation undefined — simultaneous Structural op + lead practitioner TD threshold crossing is highest-complexity Thread state |
| 2 | P2 | Collective operation contribution cap for above-tier practitioners unspecified |
| 3 | P2 | Anchor mechanic for under-threshold practitioners not defined |
| 4 | P2 | BG-mode Structural operation visibility: automatic Church detection vs. contested roll unspecified |
| 5 | P3 | Einhir site effect on TT generation from on-site operations unspecified |
| 6 | P3 | M-055 should explicitly reference P-12 (Relational Contagion) for Knot strain propagation |

---

# AGGREGATE FINDINGS REGISTER

## P1 Findings (Game-Breaking — Require Immediate Fix)

| ID | Test | Finding |
|----|------|---------|
| F-01 | T-02 | Baralta TC suppression timing vs. threshold crossing: no resolution — decisive military consequence |
| F-02 | T-03 | The Forgetting vs. retrieved Past-Pull memory: content vs. awareness distinction undefined |
| F-03 | T-05 | Simultaneous Thread operation + combat manoeuvre targeting same exchange: resolution order unspecified |
| F-04 | T-06 | Private Collection → Shifting Object decay → Gap → TC cascade: risk not modelled in Collection rules |
| F-05 | T-07 | INT 4- practitioners passively detectable by TS 10+ observers; Concealment does not cover this; not surfaced |
| F-06 | T-08 | Co-movement trigger mid-collective operation: undefined simultaneous state |

## P2 Findings (Bad Play Experience — Fix Before Phase 3)

| ID | Test | Finding |
|----|------|---------|
| F-07 | T-01 | Devout Riskbreaker at CE threshold: simultaneous TS growth + Dissonance Event — priority unspecified |
| F-08 | T-01 | Certainty deduction order under simultaneous triggers unspecified |
| F-09 | T-01 | CE track has no BG-mode equivalent |
| F-10 | T-02 | Triple threshold: no resolution order for simultaneous activations |
| F-11 | T-02 | TC 50 + IP 50: Templar deployment as mandatory IP response legally allowed but diplomatically contradictory |
| F-12 | T-02 | Royal Decree fatigue peaks at exactly the highest-stakes late-game moments |
| F-13 | T-03 | The Forgetting's applicability to non-/Dormant practitioners unspecified |
| F-14 | T-03 | Past-Oriented Pulling TS threshold (70+) not surfaced in operation descriptions |
| F-15 | T-03 | Past-Oriented Pulling TD accumulation cost not in TD table |
| F-16 | T-04 | Excommunication of Parliamentarians → no PI consequence |
| F-17 | T-04 | Post-conviction Crown lockout: no emergency procedural exit |
| F-18 | T-05 | Thread-modified objects in combat: no BG carry-forward state |
| F-19 | T-06 | Gap mechanics: no BG-mode token placement or consequence table |
| F-20 | T-07 | Concealment applicability to TS 0–9 observers unspecified |
| F-21 | T-07 | Inquisitor NPC has no BG-mode equivalent for individual CE/TS tracks |
| F-22 | T-08 | Collective op contribution cap for above-tier practitioners unspecified |
| F-23 | T-08 | Anchor mechanic for under-threshold practitioners not defined |
| F-24 | T-08 | BG-mode Structural operation Church detection: automatic vs. contested unspecified |

## P3 Findings (Minor Oddities)

| ID | Test | Finding |
|----|------|---------|
| F-25 | T-02 | TC 24 has no Parliamentary friction effects |
| F-26 | T-02 | Baralta suppression neutralises conviction TC spike in 1 season — weight mismatch |
| F-27 | T-04 | TC 24 below all named thresholds — mid-range clock may need some effects |
| F-28 | T-05 | Ehrenwall (TS 0) cannot perceive Woven sword — persistent hidden condition, no detection path |
| F-29 | T-06 | Vaynard archivists experiencing Gap wrongness: Circles complications implied but not specified |
| F-30 | T-03 | 7D pool at TN8 Ob3 ≈ 25% — harsh, possibly intentional |
| F-31 | T-08 | Einhir site TT generation for on-site operations unspecified |
| F-32 | T-08 | M-055 should reference P-12 explicitly for Knot strain propagation |

---

# COVERAGE MATRIX UPDATES

| Test ID | Mechanics | Isolation | Interaction | Scenario | Edge Cases | Status |
|---------|-----------|-----------|-------------|----------|------------|--------|
| T-01 | M-049, M-050, M-051 | ☐ | ✓ | ☐ | ✓ | Issues found |
| T-02 | M-033, M-038 | ☐ | ✓ | ✓ | ✓ | Issues found |
| T-03 | M-009, M-019, M-029 | ☐ | ✓ | ☐ | ✓ | Issues found |
| T-04 | M-031, M-036, M-037 | ☐ | ✓ | ✓ | ✓ | Issues found |
| T-05 | M-044, M-046 | ☐ | ✓ | ☐ | ✓ | Issues found |
| T-06 | M-024, M-025, M-030 | ☐ | ✓ | ☐ | ✓ | Issues found |
| T-07 | M-008, M-049, M-052 | ☐ | ✓ | ☐ | ✓ | Issues found |
| T-08 | M-020, M-023, M-055 | ☐ | ✓ | ✓ | ✓ | Issues found |

**Mechanics now with ≥1 test cell:** M-008, M-009, M-019, M-020, M-023, M-024, M-025, M-029, M-030, M-031, M-033, M-036, M-037, M-038, M-044, M-046, M-049, M-050, M-051, M-052, M-055 (21 mechanics)

**Running total:** 21/56 mechanics touched · 24/224 cells complete

---

*Generated by valoria-simulator · Sonnet 4.6 · 2026-03-27*
