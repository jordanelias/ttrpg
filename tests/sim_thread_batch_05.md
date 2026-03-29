# THREADWEAVING v2.5 — STRESS TEST BATCH 5
**Date:** 2026-03-27  
**Method:** valoria-simulator Modes B/C/D  
**Focus:** Dissolution scenario · Locking chronic in live play · BG Thread orders under RS pressure · Hybrid Accounting cascade · Low-Coherence practitioner operating · Vaynard NPC · Southernmost multi-season Mending arc  
**Model:** Sonnet 4.6  

---

## COMBINATION MATRIX — BATCH 5

| Chain | Systems | Dimension tags |
|---|---|---|
| C-07 | Dissolution → Gap → Monstrous Incursion → combat + Mending | TTRPG · PRES · RS/CE · Crown/Church · Inquisitor/Practitioner |
| C-08 | Lock placed in live play → 4-season chronic → RS spiral in concurrent campaign | TTRPG/HYB · FUT · RS/CERT · Varfell · Faction Leader |
| C-09 | BG Thread orders under RS 30 (Fractured) | BG · PRES · RS/TC · All factions |
| C-10 | Hybrid Accounting cascade: Personal Phase + Strategic Phase RS changes | HYB · CROSS · RS · Crown/Revolution |
| C-11 | Fragmented practitioner (Coherence 4) performing Structural Weaving | TTRPG · PRES · RS/Coherence · Practitioner |
| C-12 | Vaynard: Private Collection depletion under campaign RS pressure | TTRPG · CROSS · RS/Coherence · Varfell · Vaynard |
| C-13 | Southernmost multi-season Mending arc | TTRPG · PAST/FUT · RS · Multiple factions |

---

## SIMULATION 23 — C-07: DISSOLUTION FULL SCENARIO (Mode C)

### Setup

**Character:** Vaynard (TS 80, Spirit 5, Coherence 7) — Dissolution of a Locked personal configuration (a Löwenritter knight's Locked loyalty oath — Object/Personal scale Lock placed by Crown practitioner).

**State before:**
```
Vaynard — Spirit 5, Attunement 4, Focus 3, Coherence 7, Wounds 0
  Dissolution pool: Spirit 5 + History 3 + TPS 8 = 16D
  Target: Locked Personal configuration (loyalty oath)
  Lock age: 1 season (no chronic drift yet)
  Ob: Personal = 5 (Lock degree table base) + 0 (no over-actualisation) = 5

RS: 50 | TC: 5 | IP: 18
```

**Round 1: Diagnosis**
- Actualization: fully locked (Locking degree table: permanently locked)
- Prior work: Crown practitioner's Weaving/Locking visible
- Gap proximity: none
- Temporal weight: 1 season old, shallow

Declared intentionality: Dissolution of the Locked configuration.

**Round 2: Leap**
Pool: Att 4 + History 2 + TPS 8 = 14D, Ob 1. P(success): ~99%. ✓

**Round 3: Dissolution**
Pool: 16D, TN 7, Ob 5
P(≥5 net at 16D): ~83%

**Most likely outcome: Success (83%)**

Dissolution success consequences (Personal scale):
- Target dissolves. RS −5. Gap forms, lasts one scene, closes.
- Coherence −1 (cap) → 7→6
- Co-movement: Epistemic (settling, per degree); Temporal (Coherence −1, already counted); Actual d6

**RS: 50→45 (still Fragile band)**

Gap forms and closes within scene. Knight's loyalty oath is gone. The knight is free of the Lock — and free of the constraint. They may or may not honour prior commitments.

**Monstrous Incursion check:**
Gap lasts one scene. While open: Monstrous Incursion risk if RS ≤ 39 (Fractured). RS is 45 — Fragile. In Fragile band: no automatic Incursion risk from existing Gaps. The Gap closes before triggering the Fractured Incursion rule. ✓

**Partial outcome (13%):**
- Target becomes Shifting Object (Personal scale: character's loyalty flickers, oscillates between bound and free)
- RS −6 → 50→44
- Gap does not close without Mending
- Coherence −1 → 7→6

**Personal Shifting Object (§9.5):** The knight's rendering flickers — others perceive inconsistency, the person seems to be two things at once. Mechanically: unreliable. Social rolls involving the knight: GM may call opposed checks or impose Ob modifiers.

**Failure outcome (4%):**
- Full Gap. RS −8 → 50→42.
- Monstrous Incursion immediately (even in Fragile: failure-triggered, not threshold-triggered).
- Vaynard incapacitated.

**Finding: Dissolution at Personal scale is viable (83%) and manageable.** RS cost is steep (−5) but the operation succeeds reliably. The Partial outcome (Personal Shifting Object) is an interesting complication — not catastrophic but narratively rich. ✓

**New finding (SIM5-F-01, P2): Lock dissolving releases the Locked configuration — but the degree table doesn't specify what happens to the chronic effects.**
A 1-season Lock on a Personal configuration: no chronic drift yet. But the Locked Zone border interaction (§9.8: Permanent Lock = substrate adapts, RS drift ceases, permanent +1 Ob to adjacent ops) — does Dissolution of a young Lock produce any release consequence? The Pulling rules mention "Long-standing Lock release: RS +1 per season the Lock persisted (max +5)." This is for *Pulling* a Lock, not Dissolving it. Dissolution tears the configuration entirely — no clean release. Is there a release consequence for Dissolution of a Lock?

**Proposed rule:** Dissolution of a Lock produces no RS release bonus (unlike Pulling). The configuration was torn, not unwound. No relief to the substrate. At Permanent Lock tier: Dissolution fails automatically — the substrate has adapted around the Lock and the configuration no longer exists as a discrete target.

Flag as **SIM5-F-01 (P2)**.

---

## SIMULATION 24 — C-08: LOCK CHRONIC IN LIVE PLAY — VAYNARD AS FACTION LEADER (Mode C)

### Scenario: Varfell places a Territorial Lock on a Crown administrative configuration

**Setup:** Vaynard (TS 80) Locks a Crown territory's administrative coherence — a Territorial Lock intended to destabilise Crown governance over a key region.

**Round 3: Territorial Locking**
Pool: Spirit 5 + History 3 + TPS 8 = 16D, TN 7, Ob 7 (Territorial)
P(≥7 net at 16D): ~28%

**Most likely: Partial (let's say ~40%) or Failure (~32%)**

Actually recomputing:
- P(Success, ≥7): ~28%
- P(Overwhelming, very high surplus): ~8%
- P(Partial, 1–6 net): ~38%
- P(Failure, ≤0 net): ~26%

**Most likely outcome: Partial (~38%)**

Partial Lock consequences:
- Partial lock (GM sets scope — perhaps half the territory is affected)
- RS −2 → 50→48
- Coherence −1 (cap) → 7→6

**4-Season Chronic Drift Projection:**

| Season | Lock Age | Chronic RS Cost | Other RS | Season RS |
|---|---|---|---|---|
| S1 (Lock placed) | 0 | −2 immediate (Partial) | −3 (winter + ops) | 48→45 |
| S2 | 1 season | 0 (drift starts S2→S3) | −3 | 45→42 |
| S3 | 2 seasons | −1 (S2–3 tier) | −3 | 42→38 → Fractured |
| S4 | 3 seasons | −1 | −4 (Fractured: harder ops, more failures) | 38→33 |
| S5 | 4 seasons | −2 (crosses to 4+ season tier) | −5 | 33→26 |

**Crown response options:**

At S3 (RS 38, Fractured): Crown must Pull the Lock or RS deteriorates rapidly.

Pulling the Partial Lock: Ob = original TS ÷ 10 = 8 ÷ 1 = 8. Wait — Ob = original practitioner's TS ÷ 10, round up = 80 ÷ 10 = 8.

Crown practitioner pool (TS 55, Spirit 4, History 2, TPS 5): Spirit 4 + History 2 + TPS 5 = 11D vs Ob 8.
P(≥8 net at 11D): ~7%.

**P1 FLAG (SIM5-F-02): Lock removal Ob is tied to the original practitioner's TS, creating asymmetric warfare.**
A TS 80 practitioner (Vaynard) places a Lock. Removing it requires Ob 8. Crown's available TS 55 practitioner faces 7% success. Effectively, Vaynard can place Locks that only TS 80+ practitioners can remove — and Crown has no canon TS 80+ practitioner. This is either a design feature (high-TS practitioners as strategic assets) or a faction balance issue.

**Frequency:** High in factional play. Any faction with a high-TS practitioner can permanently deny Thread operations to lower-TS factions. ✓ Possibly intentional — flags for editorial attention.

**At S5 (RS 26):** If Lock persists: RS reaches 26. Now in severe Fractured territory. Spontaneous Gaps common. All Thread ops +1 Ob worldwide. Faction Stability checks at Ob 1 each season.

**Vaynard's Coherence across this arc:**
- Lock Partial: Coherence −1 → 7→6
- Each subsequent season of territorial operations (Weaving, Pulling): −1 per Relational+ op
- By S5: Vaynard at Coherence 3–4 (Fragmented) if operating 1–2 times per season

At Fragmented: −1D to all social rolls, +1 Ob on Thread operations, Memory-roll penalties. Vaynard's ability to manage the Lock's consequences degrades precisely as those consequences become most severe.

**Finding: Lock-as-weapon creates a self-defeating arc for the Lock-placer.** Vaynard's Coherence degrades; the RS damage from the Lock forces him into more operations to manage consequences; those operations degrade Coherence further. The Einhir trajectory in a faction conflict setting. ✓

---

## SIMULATION 25 — C-09: BOARD GAME THREAD ORDERS UNDER RS 30 (Mode C)

### Setup: RS 30 (Fractured band). Three factions with Thread capability considering orders.

**RS 30 effects in board game:**
- Spontaneous Gap risk: 1d10 per season at Accounting; on 1–2 = Gap in lowest-Prosperity territory
- Monstrous Incursion risk in territories with existing Gaps
- Non-practitioners: rendering failures (narrative only in BG mode)
- All Thread ops +1 Ob (stacks on BG order rolls)

**Faction options:**

**Revolution — Community Mending (Mend order):**
Ob = Gap category. Standard Gap in play: BG Ob 2 + RS penalty +1 = Ob 3. 
Revolution Influence 4 → 4D pool. P(≥3 net at 4D TN7): ~40%.
On Failure: RS −1. On Success: Gap closed, RS +1.

**P2 FLAG (SIM5-F-03): Board game Mend Ob doesn't explicitly include the RS threshold +1 Ob.**
The BG Mend order table (§9.12 patch) shows Ob by Gap category. The RS Fractured band imposes "+1 Ob to Thread operations in affected territories" (§5.3). Does this apply to BG Thread orders? The text says "all Thread operations" — BG orders are Thread operations. Yes, it should apply. But the BG order table doesn't reference it. Needs explicit statement.

**Varfell — Weave order:**
Ob = RS ÷ 20 (round up) = 30 ÷ 20 = 2 + RS penalty +1 = Ob 3.
Varfell Intelligence 5 → 5D. P(≥3 net at 5D): ~53%.
On Success: RS +1. On Failure: RS −1.

**Crown — Investigate Thread:**
Ob 3 + RS penalty +1 = Ob 4 (harder to investigate when the world is noisy).

**P2 FLAG (SIM5-F-04): Investigate Thread Ob under RS pressure not defined.**
The Investigate order doesn't specify an Ob modifier for RS conditions. At RS 30 (Fractured), the "Thread noise" should make investigation harder — but no rule exists for this. Proposed: Investigate Thread gains +1 Ob under RS Fractured and Critical conditions (consistent with all other Thread ops).

**Accounting phase at RS 30:**

Spontaneous Gap check: 1d10. P(Gap forms): 20%.
If Gap forms: RS −4 at next Accounting (Gap persisting).
Lock chronic drift (if any Locks in play): −1 to −2.
Winter drift: −1.
Net RS change without intervention: typically −5 to −8.
Net with successful Mending: −4 to −6.

**Finding: At RS 30, the board game enters a death spiral unless multiple factions coordinate Mending.** One faction's Mend order (+1 RS) cannot offset the seasonal drift (−5 to −8). Even with 3 successful Mend orders (+3 RS), net change is −2 to −5. The game at RS 30 requires near-universal Thread cooperation to stabilise, which is politically difficult given faction interests. ✓ Design confirmed — late-game RS pressure forces faction cooperation.

---

## SIMULATION 26 — C-10: HYBRID ACCOUNTING CASCADE (Mode C)

### Setup: One season of hybrid play. Personal Phase and Strategic Phase both produce RS changes.

**Personal Phase events:**
- PC practitioner (TS 65) performs Territorial Weaving (Success): RS unchanged
- PC practitioner performs Relational Lock (Partial): RS −2
- PC practitioner performs Mending on Shifting Object (Success): RS +1
- Net Personal Phase RS: −1

**Strategic Phase orders:**
- Revolution Mend order (Success): RS +1 (BG Ob 2, closed a Gap)
- Varfell Weave order (Failure): RS −1
- Crown Lock order (none — Crown has no BG Lock order)
- Net Strategic Phase RS: 0

**Cascade Phase Accounting:**
- Both phase changes applied: −1 + 0 = −1 net
- Lock chronic drift (2 seasons old): −1
- Winter: −1
- Spontaneous Gap check (RS 44, Fragile): 1d10, on 1 only = 10% chance
- Total net: −3 (no Gap) or −7 (Gap forms)
- Seasonal cap: ±10 net. Net −3 or −7 both within cap. ✓

**Finding: Hybrid Accounting is mechanically clean.** Personal and Strategic Phase changes stack at Accounting without conflict. The cap prevents extreme cascades. ✓

**New finding (SIM5-F-05, P2): No rule for which PC practitioner's operations count as "narratively leading" a Strategic Phase Thread order.**
§7.2: "Coherence tracked per PC practitioner during Personal Phase. Strategic Phase Thread orders: −1 Coherence only if PC practitioner narratively leads the operation (declared at Cascade Phase)."

If two PCs both claim to lead the Revolution's Mend order, do both pay Coherence? If neither claims leadership, does no one pay? The declaration mechanism is undefined.

**Proposed rule:** One PC declares leadership per Strategic Phase Thread order at the start of Cascade Phase. That PC pays Coherence if the order is at Relational+ scale. If no PC declares: no Coherence cost (the order was entirely NPC-led). Multiple PCs cannot co-lead a single order.

---

## SIMULATION 27 — C-11: FRAGMENTED PRACTITIONER PERFORMING STRUCTURAL WEAVING (Mode C)

### Setup: Late-campaign. Practitioner at Coherence 4 (Fragmented) must perform Structural Weaving to prevent catastrophic RS collapse.

**State before:**
```
Practitioner — Spirit 5, Coherence 4 (Fragmented), Wounds 1
  Active penalties: −1D to all social rolls, −1D to Memory rolls
  +1 Ob on all Thread operations (rendering reasserts aggressively)
  Fragmented Fallout: rolled this session (memory discrepancy, ongoing)

Structural Weaving pool: Spirit 5 + History 4 + TPS 9 = 18D
Ob: Structural = 5 + Wound +1 + Fragmented +1 = Ob 7
P(≥7 net at 18D): ~47%
```

**Leap eligibility check:**
- Approach Training ✓
- TS 90+ ✓ (assumed — Structural requires TS 70+)
- Not in melee ✓
- Wounds 1: not at incapacitation threshold ✓

**Leap roll:**
Pool: Att 5 + History 2 + TPS 9 = 16D, Ob 1 + Wound +1 + Fragmented +1 = Ob 3
P(≥3 net at 16D): ~97%. Leap succeeds. ✓

**Structural Weaving roll:**
Pool: 18D, Ob 7
P(Overwhelming, surplus 3+): ~20%
P(Success, surplus 1–2): ~27%
P(Partial, 0 net): ~22%
P(Failure): ~31%

**Most likely: Failure (31%) or Success (27%).** Roughly even odds. The Fragmented penalty (+1 Ob) is the tipping point — without it, P(Success+) at 18D Ob 6 ≈ 60%.

**Coherence interaction at Fragmented:**
Operation succeeds: Coherence −1 (Structural) → 4→3 (still Fragmented)
Operation fails: Coherence −1 (cap) → 4→3. Also RS −6 (Structural failure).

**Fragmented Fallout on entry** (already rolled this session). But Fractured Fallout hasn't triggered — Coherence 4→3 stays in Fragmented band, no new threshold crossed. ✓

**At Coherence 3:** Still Fragmented. +1 Ob persists on Thread operations. The practitioner cannot recover through operations — only through non-practice.

**Belief Co-Authorship trigger:** Coherence 2 (Fractured) — not yet reached. But approaching fast.

**Finding: A Fragmented practitioner performing Structural Weaving is a ~47% proposition.** This is the late-campaign emergency scenario: a damaged practitioner making a desperate attempt at scale. The system prices it honestly. The +1 Ob from Fragmented is the mechanic that differentiates "experienced but worn" from "fresh" — it matters precisely in the moments when scale is highest.

**New finding (SIM5-F-06, P2): +1 Ob from Fragmented stacks with all other Ob sources, but the Fragmented threshold table says "+1 Ob on all Thread operations" without clarifying whether this applies to the Leap roll as well.**

The Leap is a Thread operation (§2.3 calls it such implicitly). Fragmented's +1 Ob should apply to the Leap. This is included in the Leap calculation above. But the Fragmented table entry only says "Thread operations" — if Leap is considered separately from operations, the +1 Ob might not apply. Clarification needed.

**Proposed text:** In §3.3 Fragmented row: "All Thread operations, including the Leap roll." ✓ Minor text fix.

---

## SIMULATION 28 — C-12: VAYNARD — PRIVATE COLLECTION DEPLETION ARC (Mode C)

### Scenario: Vaynard depletes his Private Collection across a campaign under RS pressure.

**Private Collection:** 5 residue samples, Potency 1–3 (assumed distribution: 1×P3, 2×P2, 2×P1).

**Campaign arc (10 seasons):**

Vaynard uses residue when operations are critical (Ob 6+ operations, RS pressure seasons).

| Season | Operation | Residue Used | Potency | Coherence | Post-Op Coherence |
|---|---|---|---|---|---|
| S1 | Territorial Lock (Ob 7, success needed) | P3 | +3D | −1 (cap) | 9→8 |
| S3 | Dissolution (Ob 6, opponent Lock) | P2 | +2D | −1 (cap) | 8→7 |
| S5 | Structural Weaving (Ob 7, RS emergency) | P2 | +2D | −1 (cap) | 7→6 |
| S7 | Past-Oriented Pull (Ob 6, 3-season event) | P1 | +1D | −1 (cap) | 6→5 |
| S9 | Territorial Dissolution (Ob 7, crisis) | P1 | +1D | −1 (cap) | 5→4 → Fragmented |

**Potency depletion tracking:**
Each same-source use: +1 Ob. After 2 uses from the same sample: effectively depleted for high-Ob operations.

**Collection state by S9:** All 5 samples used (P3×1, P2×2, P1×2). Collection empty.

**Coherence trajectory with residue use:**
Because of the cap, residue use doesn't cost extra Coherence — it's still −1/operation. Without residue at these Obs, Vaynard would likely fail more often (more Partial/Failure outcomes) — and Partial/Failure also costs Coherence −1. Net result: residue doesn't change the Coherence trajectory, but it changes the success rate.

**Finding: Private Collection is a success-rate resource, not a Coherence resource.** Under the cap ruling, residue improves your odds without increasing Coherence cost. At Object/Personal scale, residue is free (base cost 0, cap 0). At Relational+, residue costs nothing additional — you'd pay −1 anyway. The Collection's value is entirely in the bonus dice.

**New finding (SIM5-F-07, P2): With the Coherence cap, Varfell's Private Collection becomes mechanically identical to "bonus dice with no cost" at all scales.** The original design intent was that residue use had a real Coherence cost that differentiated it from standard operations. The cap eliminates this differentiation. At Relational+: −1 with or without residue. At Object/Personal: −0 with or without residue. Residue is now strictly beneficial — no downside beyond depletion.

This may conflict with the philosophical framing (§3.4: "residue's proximity to the ground intensifies the practitioner's exposure during contact... each use pushes them deeper into the beyond-rendering state"). The philosophy says residue costs more. The cap says it doesn't.

**Decision needed:** Is residue use exempt from the Coherence cap? Options:
- **A: Cap applies (current):** Residue is pure upside (bonus dice). Simple, but undermines the philosophy.
- **B: Residue exempt from cap:** Residue always costs −1 additional on top of the capped operation cost. Total: −2 per operation when residue is used. Differentiated but reintroduces the cliff risk at some scale combinations.
- **C: Residue costs −1 only at Object/Personal scale (normally 0 base):** At Relational+, cap absorbs it. At Object/Personal, residue user pays −1. Residue has a real cost at low scale where it's otherwise free, but not at high scale where you'd pay anyway.

Flag as **SIM5-F-07 (P1)** — the philosophical framing and the mechanical cap directly contradict each other. Editorial decision required.

---

## SIMULATION 29 — C-13: SOUTHERNMOST MULTI-SEASON MENDING ARC (Mode C)

### Setup: Expedition to Southernmost. 4-season Mending arc. RS starts at 35 (Fractured).

**Expedition team:**
- Lead Mender (TS 75, Att 5, Focus 4, TPS 7): Mending pool = 5+4+7 = 16D
- Support Practitioner (TS 60, Weaving support): Weaving pool = Spirit 4 + History 2 + TPS 6 = 12D
- Scholar (non-practitioner, Einhir Texts researcher)

**Einhir Ritual Framework requirements (§9.15):**
1. Knowledge: Prior Diagnosis of Locked Zone structure ✓ (expedition S1 includes Diagnosis scene)
2. Technique: Einhir Text technique (Scholar provides) ✓
3. Location: Einhir site-network node ✓ (at Southernmost)

All three met by S2. Locked Zone Mending available from S2 onward.

**S1: Exploration + Diagnosis**

Zone 1 (Border): Shifting Object encounter. Agility Ob 2 or Thread op. Team uses Object-scale Weaving: pool 12D, Ob 1. Near-certain success. RS +0 (no RS cost on Object Weaving success without co-movement).

Zone 2 (Inner): Gap incursion. Mode 1 monstrous entity. Combat or Thread. Team attempts communication (P-04): possible if entity is willing.

Zone 3 (Core): Configuration instability. Non-practitioners: Spirit Ob 2 or Certainty −1 per round. Scholar at Spirit 3: P(pass per round) ≈ 73%. 3 rounds in Core: P(no Certainty loss) ≈ 0.73³ ≈ 39%. Scholar likely loses 1 Certainty. Contact duration halved for practitioners.

**Diagnosis of primary site (S1 climax):**
TS 75 practitioner: no roll needed (TS 50+ Diagnosis automatically reveals nature of damage at Southernmost per §batch_bc_designs.md expedition rules). Gap structure understood. ✓

**S2: First Mending attempt — Catastrophic Gap (Ob 7, Einhir framework required)**

With Einhir framework: eligible.
Pool: 16D, Ob 7 (Catastrophic — at Ob ceiling since Mending Ob cap = 8, and Catastrophic Gap = 7, no additional modifiers push past 7 here since RS is already factored into "Catastrophic" categorisation).

Wait — RS Fractured adds +1 Ob to Thread operations in affected territories. Does this apply at the Southernmost?

**P2 FLAG (SIM5-F-08): RS threshold +1 Ob applicability at Southernmost.**
The Southernmost is a specific location with its own Thread conditions. The RS threshold penalty is "in affected territories" — the Southernmost is presumably a specific territory. At RS 35 (Fractured), all territories are affected. So yes: +1 Ob applies. Locked Zone Mending Ob 8 + RS Fractured +1 = Ob 9, but Mending Ob ceiling = 8 (SIM4-F-01 patch). **Cap triggers.** Ob 8 total.

P(≥8 net at 16D): ~34%

**Most likely outcome: Failure or Partial (~66% combined)**

Failure: Gap unchanged. RS −2 → 35→33. Coherence −1. No Wound (patched). Second attempt possible next round.

**S2 repeat attempt (sequential failure +1 Ob → but Mending ceiling 8 absorbs it — cap still 8).**

The sequential failure penalty is absorbed by the ceiling. P stays at ~34%.

**P3 FLAG (SIM5-F-09): Mending Ob ceiling makes sequential failure penalty irrelevant at high-Ob operations.**
When the total Ob would exceed 8 without the ceiling, the ceiling absorbs the sequential failure penalty — failed attempts don't make the next attempt harder (Ob is already at ceiling). This is mechanically clean but means that a practitioner at a Catastrophic/Locked Zone site can retry indefinitely without accumulating Ob. Only the Coherence cost (−1 per attempt) and RS degradation from failures act as retry deterrents.

**S2 probability of at least one success across multiple attempts (Focus 4 = 3 operation rounds):**
Assuming 3 attempts in S2 contact window (Focus 4 → 3 ops):
P(at least one success in 3 attempts at 34% each): 1 − (0.66)³ ≈ 71%

**S3–S5: Subsequent seasons**

Each successful Mending: Catastrophic Gap → Entrenched Gap → Standard Gap → Micro-Gap → closed. 4 severity steps at Ob 8 → 6 → 5 → 3 (Mending table).

| Season | Gap State | Mending Ob (ceiling) | P(Success per attempt, 16D) | Expected attempts |
|---|---|---|---|---|
| S2 | Catastrophic | 8 (ceiling) | ~34% | ~3 |
| S3 | Entrenched | 7 (no ceiling needed) | ~47% | ~2 |
| S4 | Standard | 6 | ~62% | ~2 |
| S5 | Micro-Gap | 4 | ~86% | ~1 |

**RS recovery per successful Mending:**
Southernmost expedition: RS +2 permanent per successful season (§5.2).

| Season | RS change (Mending success) | RS change (Mending failure) | Running RS (success path) |
|---|---|---|---|
| S2 | +2 − winter −1 − other −2 = −1 | −2 − winter −1 − other −2 = −5 | 34 |
| S3 | +2 −1 −2 = −1 | −5 | 33 |
| S4 | +2 −1 −2 = −1 | −5 | 32 |
| S5 | +2 −1 −1 = 0 | −4 | 32 |

**Finding: Even successful Southernmost Mending barely offsets campaign RS degradation.** The expedition produces +2 RS per season, which is consumed by winter drift (−1) and other operations (−2 typical). Net: approximately RS-neutral at best on the success path. The expedition prevents the Rupture from accelerating but does not reverse the campaign's RS trajectory without simultaneous Lock removal and Gap Mending elsewhere.

**This is the correct design:** The Southernmost is a long-term project, not a solution. It contributes meaningfully over many seasons but requires parallel action across all factions to actually stabilise the world. ✓

---

## AGGREGATE FINDINGS — BATCH 5

| ID | Category | Description | Severity | Frequency |
|---|---|---|---|---|
| SIM5-F-01 | Gap | Dissolution of a Lock: no release consequence rule; Permanent Lock Dissolution undefined | P2 | Low |
| SIM5-F-02 | Optimal Play | Lock removal Ob = original TS ÷ 10 creates asymmetric warfare; high-TS practitioners place near-irremovable Locks | P1 | High |
| SIM5-F-03 | Gap | BG Mend order table doesn't reference RS threshold +1 Ob penalty | P2 | Medium |
| SIM5-F-04 | Gap | Investigate Thread Ob under RS pressure not defined | P2 | Medium |
| SIM5-F-05 | Gap | Hybrid Strategic Phase Thread order Coherence leadership: declaration rule absent | P2 | Medium |
| SIM5-F-06 | Ambiguity | Fragmented +1 Ob: applies to Leap? Table says "Thread operations" — clarify | P2 | Medium |
| SIM5-F-07 | Incoherence | Coherence cap makes residue use free at all scales — contradicts philosophical framing | P1 | High |
| SIM5-F-08 | Ambiguity | RS threshold +1 Ob at Southernmost: applies or location-exempt? | P2 | Low |
| SIM5-F-09 | Incoherence | Mending Ob ceiling absorbs sequential failure penalty at high-Ob sites — retry cost = 0 Ob | P3 | Low |

**P1: 2 (SIM5-F-02, SIM5-F-07)**  
**P2: 6**  
**P3: 1**

---

## DECISIONS REQUIRED

**SIM5-F-07 (P1) — Residue + Coherence cap conflict:**

| Option | Effect |
|---|---|
| A: Cap applies (current) | Residue = pure bonus dice, no cost at any scale. Simple. Contradicts philosophy. |
| B: Residue exempt from cap | Residue always costs −1 additional. Total −2/operation when used. Reintroduces cliff risk. |
| C: Residue costs −1 at Object/Personal only | Real cost when otherwise free; absorbed at Relational+ where you'd pay anyway. |

**SIM5-F-02 (P1) — Lock removal asymmetry:**
Lock removal Ob = original TS ÷ 10. A TS 80 Lock costs Ob 8 to Pull. Confirm this is intentional (high-TS practitioners as strategic deterrents) or cap the Lock removal Ob (e.g., max Ob 6 for Lock removal regardless of original TS)?

---

## CUMULATIVE OPEN FINDINGS (all batches)

**P1 open (3):**
- SIM5-F-02: Lock removal asymmetry
- SIM5-F-07: Residue + cap contradiction
- SIM4-F-01: ✓ Patched (Mending ceiling)

**P2 open (19):**
SIM2-F-01, F-05, F-08, F-10, F-11 · SIM3-F-02, F-03, F-06 · SIM4-F-02, F-03, F-04, F-06, F-07 · SIM5-F-01, F-03, F-04, F-05, F-06, F-08

**P3 open (4):**
SIM2-F-06 · SIM4-F-05 · SIM3-F-05 · SIM5-F-09
