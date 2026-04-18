# SIM-THREAD-01: Temporal Axis Sessions — With and Without Threadworking
## Date: 2026-04-02
## Modes: C (full scenario) × 4 + G3 (threadwork) × 3 + G2 (debate) × 1 + D + J + L
## Status: COMPLETE

---

## 7-DIMENSION TAG

```
Test ID: SIM-THREAD-01
Mechanics: Weaving (Relational), Pulling (Normal), POP (Past-Oriented), Locking (Personal), Debate, Domain Echo, Register Shift, Co-movement (all three axes)
Mode: TTRPG (Sessions A-C), HYB (Session D)
Temporal: PAST (Session C), PRES (Sessions A-B), FUT (Session D)
Tracks: RS, Coherence, Composure, TC, Domain Echo queue, Wound
Factions: Crown, Church, Hafenmark, Varfell
NPCs: Almud (Crown archetype), Baralta (Hafenmark archetype), Klapp (Church archetype), Generic TS-52 Practitioner (Present), Generic TS-72 Practitioner (Past), Generic TS-55 Practitioner (Future)
Archetypes: Monarch, Legalist-constitutionalist, Institutional practitioner, Archivist-scholar
```

---

## SHARED STARTING STATE (all sessions)

```
TC: 36 | RS: 65 | IP: 24 | PI: 5
Crown: M5 I5 W4 Mil4 Sta4
Church: M4 I6 W5 Mil3 Sta5
Hafenmark: M4 I4 W5 Mil3 Sta4
Varfell: M3 I4 W3 Mil4 Sta4
```

---

## SESSION A — NO THREADWORKING: CROWN-HAFENMARK NEGOTIATION

**Seed:** Almud's envoy meets Baralta to negotiate terms on the Templar deployment into Varfell. No practitioners present. Pure social + faction resolution.

### State: Scene Opening

```
Almud's Envoy — Pre 4, Cog 4, Composure 12 | Debate pool: (4×2)+3 = 11D
   History (Crown Law): 3 | Primary genre: Present (Virtue Ethics — Crown)
   Belief: "The monarchy must hold. The Church is the price of that holding."

Baralta — Pre 4, Cog 5, Composure 12 | Debate pool: (4×2)+3 = 11D
   History (Categorical Imperative/Jurisprudence): 3 | Primary genre: Past (Kantian Categorical Imperative — Hafenmark)
   Belief: "The Templar deployment violates the constitutional settlement of 201 AG."
   Audience: Parliamentary observers (mixed, Stability avg 3 → resistance 2)
```

Conviction Track: Start 5 (neutral). Baralta argues for withdrawal (track ≥7 = Baralta wins). Crown argues for legitimacy of deployment (track ≤3 = Crown wins).

### Exchange 1 — Read Phase

Envoy (3D Attunement TN7 Ob1): E[net] = 0.90. P(≥1) ≈ 75%. **Most likely: Partial** — identifies Baralta's primary genre (Past) only.

Baralta (Attunement 4D TN7 Ob1): E[net] = 1.20. P(≥2) ≈ 70%. **Most likely: Success** — identifies Envoy's primary genre (Present) + orientation (Revealing).

### Exchange 1 — Argue

Baralta wins the Read. She knows the Envoy will use Present+Revealing. She chooses Past+Revealing → CLASH (same genre? No — Envoy: Present, Baralta: Past → DIVERGENCE).

DIVERGENCE: each evaluated independently.

Envoy Present+Revealing: 11D TN7. E[net] = 11×0.30 = 3.3. Genre weight: Present (Crown Virtue Ethics = +0.5) → 1.5. Effective margin = 3.3 × 1.5 × 1.0 = 4.95 ÷ 2 (Divergence ÷2) = 2.48. vs resistance 2. Δ = ⌊2.48 − 2⌋ = 0. **No track movement from Envoy.**

Baralta Past+Revealing: 11D TN7. E[net] = 3.3. Genre weight: Past (Hafenmark Categorical Imperative = +0.5) → 1.5. Effective margin = 3.3 × 1.5 × 1.0 = 4.95 ÷ 2 = 2.48. vs resistance 2. Δ = ⌊0.48⌋ = 0. **No track movement from Baralta either.**

**State Post-Exchange 1:** Track 5. Neither argument breaks through resistance 2. Both orators correctly identified the opposition genre. No strain (DIVERGENCE).

**Finding A-01 — Design feature confirmed:** With symmetric pools (11D vs 11D) and resistance ≥ 2, neither side moves the track in DIVERGENCE. High-resistance audiences absorb both arguments. This correctly models political deadlock between equals. ✓

### Exchange 2 — CLASH

Baralta changes strategy: Past+Revealing vs Envoy choosing Present+Revealing. Wait — Baralta now knows Envoy uses Present. She can choose CLASH by using Present+Obscuring (same genre, opposite orientation).

Baralta: Present+Obscuring. Envoy: Present+Revealing → **CLASH**.

CLASH: Baralta 11D vs Envoy 11D. E[margin] = 0 (symmetric). TIE fires (equal expected). Track +1 toward initiative holder (Baralta — higher Presence? Equal at 4. Both 4 → higher Cognition: Baralta 5 vs Envoy 4). Baralta has initiative.

Track: 5 → 6 (toward Baralta). Strain to neither (TIE = 1 strain each).

Envoy Composure: 12→11. Baralta Composure: 12→11.

**State Post-Exchange 2:** Track 6. Slight Baralta advantage. Envoy strain 1, Baralta strain 1.

### Exchange 3 — Register Shift: Baralta invokes faction scope

Baralta invokes "sufficient scope" — she is challenging Crown institutional authority (Templar deployment = sovereignty question). **Register Shift fires: Scene → Faction.**

Domain Echo queued: if Baralta's argument ultimately succeeds (track ≥7), Crown Mandate −1; Hafenmark Influence +1. Fires at next Accounting.

### Exchange 3 — Argue (post-Register Shift)

Baralta's faction scope invocation gives her a narrative advantage but no extra dice. Envoy, aware the stakes have elevated, invokes Memory Bonus (citing the 201 AG Constitutional Settlement's exact territorial exclusion clause). Memory Bonus: +2D → Envoy pool 13D.

Envoy: Past+Revealing (using Baralta's stronger genre to CLASH directly).
Baralta: Past+Revealing → **COMPETITION** (same genre, same orientation).

COMPETITION: same resolution as CLASH. Envoy 13D vs Baralta 11D. E[Envoy net] = 3.9, E[Baralta net] = 3.3. E[margin] = 0.6 toward Envoy.

Effective margin = ⌊0.6 × 1.5 (Past, Hafenmark boost — but audience is Parliamentary observers, not Hafenmark-specific; avg audience genre weight = 1.0 for Past) × 1.0⌋ = ⌊0.6⌋ = 0.

No track movement. Strain to Baralta (lost): margin+1+winner's Presence modifier... wait: Envoy Presence 4. Strain = margin(0)+1+winner Presence modifier... from params_debate: "Strain to loser: margin + 1 + winner's Presence modifier. Reduced by loser's Focus defence: floor(Focus/2)."

With margin 0 (expected), strain = 0+1+... hmm, margin 0 means effectively TIE rule fires (both take 1 strain). Let me apply TIE: track +1 toward initiative holder. Initiative: transferred to Envoy (won Exchange 3 by expected net). Track: 6→5.

Both take 1 strain. Envoy Composure 11→10. Baralta 11→10.

**State Post-Exchange 3:** Track 5 (back to neutral). 3 exchanges in, no resolution.

### Exchange 4 — Leverage: Baralta reveals the Olafsson-Niflhel connection

Baralta uses evidence leverage (ED-077, Cognition+History Ob2). She has circumstantial evidence of Church-Niflhel collusion; revealing it now shifts the stakes.

Roll: Cognition 5 + History 3 = 8D TN7 Ob2. E[net] = 2.4. P(≥2) ≈ 70%. **Most likely: Success.**

Effect: audience ethical mode shifts one step toward Baralta's genre (Past) for remaining debate. Past weight: 1.5 → 2.0 (capped at audience maximum).

Now Baralta's Past+Revealing arguments carry weight 2.0. Envoy's Present+Revealing carry 1.0.

### Exchange 4 — Argue

Envoy: Present+Revealing 13D. Baralta: Past+Revealing 11D → DIVERGENCE.

Baralta's contribution: 3.3 × 2.0 × 1.0 ÷ 2 = 3.3. vs resistance 2. Δ = ⌊3.3−2⌋ = 1 toward Baralta. Track 5→4.

Envoy's contribution: 3.9 × 1.0 × 1.0 ÷ 2 = 1.95. vs resistance 2. Δ = 0.

Net: Track 4. Baralta is gaining.

**State Post-Exchange 4:** Track 4. Baralta closing in on win threshold (≤3). Initiative stays with Baralta.

### Exchange 5 — Forced Conclusion

Track at 4, Envoy behind. Envoy invokes Concede a Point (step 5): forfeit exchange, take 1 strain, track +1 toward non-forfeiting side, gain +1D next exchange. Track 4→3. Baralta wins.

**DEBATE OUTCOME: Baralta wins. Track ≤3.**

### Post-Debate Resolution

- Domain Echo: Crown Mandate −1; Hafenmark Influence +1. Queues to next Accounting.
- Scene: Baralta publicly demands Templar withdrawal. Envoy cannot refuse a Parliament-scope commitment.
- TC consequence: No direct TC change from Baralta's win (Church was not a party to this debate). But: if Church learns of the Olafsson-Niflhel reveal, TC −2 (from ED-049 Stability brake activation path).

### Mode A Findings

**F-TH-A-01 (P2):** Evidence leverage (ED-077) has no stated cap on audience ethical mode shift. With one successful leverage roll, weight went from 1.5 to 2.0. Can subsequent leverage rolls push further (to 2.5, 3.0)? No maximum stated. **Patch: cap audience ethical mode shift at 2.0 via leverage mechanic.**

**F-TH-A-02 (design confirmed):** High-resistance audiences (resistance 2) absorb both sides' DIVERGENCE arguments at symmetric pools. Political deadlock between equals is mechanically stable. ✓

**F-TH-A-03 (P2):** Register Shift (Scene→Faction) fires mechanically when "sufficient scope" criteria met, but does not change the debate mechanics — it just queues Domain Echo. No visible in-scene effect. Players may not know it fired. **Flag for ED-074 refinement: Register Shift should produce a visible narrative signal (GM announces "this has become a matter of state").**

---

## SESSION B — PRESENT AXIS: WEAVING (RELATIONAL)

**Seed:** TC=36, accelerating. A TS-52 practitioner Weaves the Crown-Hafenmark alliance thread (Relational scale) to prevent it from fraying. The practitioner is at a private audience — no combat, no debate — pure Thread operation.

### Practitioner State

```
Practitioner — Spirit: 4, Attunement: 3, TPS: 5, TS: 52, TD: 5
Coherence: 10 | Focus: 4 | RS: 65
History (Diplomatic Relational): 2
Weaving pool: Spirit(4) + History(2) + TPS(5) = 11D, TN7
```

### Step 1: Leap

TS 52 ≥ 50 (Relational scale minimum). Not in melee. Ob 1 (TS 50+ = Ob 1).

Pool: Attunement(3) + History(2) + TPS(5) = 10D, TN7, Ob1.
E[net] = 3.0. P(Overwhelming, ≥2): ≈ 90%.

**Most likely: Overwhelming Leap.** Contact established. Next op Ob −1 (min 1 → stays 1). TS: 52→53. TPS stays 5.

### Step 2: Diagnosis

Mandatory before Weaving. GM describes: the Crown-Hafenmark thread (Relational scale) is firmly actualised — a long-standing diplomatic relationship. No Active Knot Crisis. Temporal weight: moderate (35 years of treaty history). Epistemic: high (both parties believe the alliance is real).

### Step 3: Weaving (Relational scale, Ob 3 standard, −1 from Overwhelming Leap = Ob 2)

Pool: 11D, TN7, Ob 2.
E[net] = 3.3. P(Overwhelming, ≥4): P(≥4, 11D TN7) ≈ 75%.
P(Success, ≥2): ≈ 98%.

**Most likely: Overwhelming.**

Weaving Overwhelming (Relational scale):
- RS: **+1** (Relational+ Overwhelming → RS 65→66)
- Coherence: 0 (Relational auto-cost applies at end of contact, not per-op)
- TS: 53→54. TPS stays 5.
- Over-actualisation: subsequent ops on this configuration +1 Ob for 1 season.

### Step 4: Co-Movement (P-01 — all three axes MUST fire)

**Temporal auto-effect (Relational scale = Coherence retention roll required):**
The Weaving of a 35-year treaty thread creates a temporal ripple. Automatic: the practitioner feels the weight of the alliance's history — specific moments (treaty signing, the ice-storm of 222 AG when Baralta's father upheld the terms against Crown pressure). This is narrative only at Relational scale — no Coherence cost from temporal auto-effect at Relational.

Actually — checking params: "Temporal auto-effect: Object/Personal = narrative only (no Coherence). Relational+ = Coherence retention roll." A Coherence retention roll IS required.

**Coherence Retention Roll (Relational scale Weaving, end of contact):**
Pool: Spirit(4) + History(2) + TPS(5) = 11D, TN7.
Ob = sum of all operation Obs this contact = 2 (one Weaving at Ob 2).
E[net] = 3.3 >> Ob 2. P(pass): ≈ 99%.

**Coherence retained: 10 (no change).**

**Epistemic auto-effect (by degree, Overwhelming):**
"Genre + orientation + one specific detail." The practitioner now knows: the alliance has a hidden stress point — Baralta has privately promised three merchants' guilds in Hafenmark that she will not yield on the Templar question. This is a real epistemic consequence: the practitioner has learned a fact they could not otherwise know. This will shift social Ob in the scene by −1 (information advantage) on relevant rolls.

**Actual d6 auto-effect:**
Expected value: minor consequence. Using expected range (d6 = 1-6, narrative flavour): "A servant of Baralta's household feels briefly dizzy and drops a tray." No mechanical effect at Object level, narrative flourish.

**P-01 COMPLIANCE: All three dimensional auto-effects fired. ✓**

### Step 5: Second Operation (Focus 4 → 3 op rounds available after Leap)

Practitioner uses second op round for Diagnosis of the over-actualisation risk. No roll. Result: the alliance thread is now "over-actualised" — further Weaving this season adds +1 Ob. The practitioner wisely does not attempt a second Weaving.

### Contact End

Contact ends (used 2 of 4 rounds: Leap + Weave + Diagnosis + none). Focus not fully expended.

### BG/Hybrid Consequences

RS: 65→66. Queued at next Accounting: +1 RS (immediate per PP-107, but in this non-Hybrid scenario, RS updates immediately → RS = 66).

The Domain-equivalent consequence: no Domain Action was taken. The practitioner reinforced the existing relationship — it cannot now be easily frayed this season. In BG terms: any Domain Action targeting Crown-Hafenmark alliance this season faces +1 Ob (over-actualisation effect translates as thread resistance).

### Mode B Findings

**F-TH-B-01 (design confirmed):** Relational Weaving is the most accessible high-value operation. At Ob 3 (Ob 2 with Overwhelming Leap), an 11D pool produces Overwhelming ≈ 75% of the time. The over-actualisation counter limits repeated use. ✓

**F-TH-B-02 (P2):** Over-actualisation in BG layer is not defined. In TTRPG, over-actualisation adds +1 Ob to subsequent ops on the same configuration. In BG, there is no op-by-op Thread mechanic — just Co-Movement cards. **How does over-actualisation translate to BG layer?** Currently no rule. **Patch: over-actualisation in TTRPG scene → corresponding BG territory/faction card gets Thread Debt +1 token at Zoom Out. Thread Debt tokens add +1 Ob to any BG Thread order targeting that card.**

**F-TH-B-03 (P1 — P-01 compliance):** The "Actual d6" auto-effect has no explicit resolution table in params_threadwork for TTRPG scenes. The params reference it exists but only provides examples from co-movement cards. Individual scene d6 resolution is undefined. **Patch: add d6 actual auto-effect table to params_threadwork for personal-scale operations.**

---

## SESSION C — PAST AXIS: PAST-ORIENTED PULLING (HISTORICAL CONFIGURATION)

**Seed:** TC=36. A TS-72 practitioner attempts POP to access the thread of the 218 AG Royal Assassination — to determine what actually happened (key campaign truth, ~27 years/108 seasons ago). High stakes, near-impossible mechanically.

### Practitioner State

```
Practitioner — Spirit: 5, Attunement: 4, TPS: 7, TS: 72, TD: 6
Coherence: 9 | Focus: 3 | RS: 58 (required ≤60 for POP ✓)
History (Historical Research): 3
POP pool: Spirit(5) + History(3) + TPS÷2(3) = 11D, TN7
```

### Recency Calculation

218 AG to 245 AG = 27 years. Assuming 1 campaign season = approximately 3 months → 27 years = 108 seasons. Category: **10+/generational → Ob 7**.

Active Knot Crisis on target (the assassination left an unresolved political thread): **+1 Ob → Ob 8.**

Wait — Foundational Ob is "Ob 7 + 2 surcharge = 9." Ob 8 is between generational (7) and foundational (9). With Active Knot Crisis: Ob 7 + 1 = 8. Valid — not foundational level.

### Leap

TS 72 ≥ 70 (POP requires TS 70+). RS 58 ≤ 60 (POP requires RS ≤ 60 ✓). Diagnosis mandatory.

Leap Pool: Attunement(4) + History(3) + TPS(7) = 14D, TN7, Ob1. E[net] = 4.2. P(Overwhelming) ≈ 99%.

**Overwhelming Leap. TS: 72→73. TPS: 7. Next op Ob −1 → Ob 8−1 = 7.**

### Diagnosis

Mandatory (POP without Diagnosis: +3 Ob + temporal Gap on Failure). GM: configuration is 27-year-old, heavily occluded. The assassination thread is "firmly actualised in the past" — significant emotional/political weight. Multiple observers rendered it differently (P-03: rendering = consciousness). Active Knot: the crown still rests on a political configuration built on this unresolved moment.

### POP Attempt (Ob 7 post-Leap bonus, TN7)

Pool: 11D, TN7, Ob7. E[net] = 3.3. P(net ≥ 7, 11D TN7) ≈ 8%.

**Probability breakdown:**
| Degree | Net threshold | P(≈) |
|--------|-------------|------|
| Overwhelming (≥14) | net ≥ 14 | <1% |
| Success (≥7) | net ≥ 7 | ~8% |
| Partial (>0 but <7) | 1 ≤ net ≤ 6 | ~40% |
| Failure (≤0) | net ≤ 0 | ~52% |

**Most likely: Failure (52%).**

**Failure consequences (POP):**
- Snap-back wound: 1 Wound (no armour). Practitioner Health reduced.
- RS minimum: −6. RS: 58→52.
- Coherence: −1. Coherence: 9→8.
- No information gained.

**Second most likely: Partial (40%).**

**Partial consequences (POP):**
- Emotional impressions only — "dread without content" (from emergent_scenarios). The practitioner feels the assassination but cannot extract specifics.
- RS: −1. RS: 58→57.
- Coherence: −1 (harder). Coherence: 9→8.

**Success (8%):**
- RS: −3 minimum. RS: 58→55.
- Full historical access: practitioner can Diagnose the perpetrator's thread signature. Not proof in the mundane world, but verifiable to TS 50+ witnesses.

### Co-Movement (fires regardless of outcome per P-01)

**Temporal auto-effect:** POP always produces temporal consequence. The practitioner's consciousness has reached into a 27-season-old configuration. Temporal co-movement at Generational scale:
- Epistemic: any PC who witnesses the operation gains a Certainty −1 (confronting historical ontological truth). No roll required.
- RS consequence: the temporal weight of the pull exerts RS pressure independent of the operation outcome. RS −1 additional from temporal auto-effect (separate from operation RS cost).
- Actual d6: [EXPECTED: something breaks or shifts in the physical environment — a mirror cracks, a document falls open to a relevant page].

**Total RS change on Failure:** −6 (operation) + −1 (temporal auto-effect) = **RS −7. RS: 58→51.**

**P-01 compliance check:** All three auto-effects fired. ✓

### Mode C Findings

**F-TH-C-01 (P1):** Past-Oriented Pulling at generational recency (Ob 7-8) is mechanically near-impossible. Even with an 11D pool and Overwhelming Leap bonus: P(success) ≈ 8%, P(failure) ≈ 52%. Expected outcome is failure with RS −7. Running 3 POP attempts against the same target: expected RS loss = 3 × 7 × 0.52 = ~11 RS points from failures alone. This confirms: historical truth cannot be reached via Thread ops alone. Mundane methods (archives, witnesses, Niflhel intelligence) are the primary investigation path. Thread confirms, it does not discover.

**This is design-consistent with P-03 (rendering = consciousness).** The past configuration was rendered by multiple observers differently; it cannot be cleanly pulled by a single practitioner. ✓

**F-TH-C-02 (P2):** The temporal auto-effect RS cost (−1 additional at Generational scale) stacks with operation RS cost. At RS 58, two failures = RS 44. RS 40 triggers Shifting Objects. Three failures = RS 37 → approaching Gap threshold (RS 20). A practitioner who attempts POP three times against an Ob 8 target at RS 58 has a 14% chance of surviving all three attempts without RS dropping below 40. **This is extremely dangerous at campaign level.**

**F-TH-C-03 (P2 → design confirmed):** POP at personal scale yields personal-thread access (who did what to whom). POP at Relational scale (for group/political truth) requires TS 70+ AND Ob 8+. For generational political events, the operation is at the edge of what Thread practice can do. The past is largely sealed. ✓

**F-TH-C-04 (P1 — PARAMS GAP):** Temporal auto-effect RS cost at Generational scale is implied but not explicitly stated in params_threadwork. The params specify Coherence retention rolls at Relational+, but the RS cost from temporal auto-effect at high-recency POP is not in the table. **Patch needed: add temporal auto-effect RS cost table for POP by recency band.**

---

## SESSION D — FUTURE AXIS: LOCKING (HYBRID MODE)

**Seed:** TC=38 (approaching 40 threshold). A TS-55 practitioner Zooms In from a BG session (after Phase 3) to attempt Locking on the political-institutional configuration preventing Church TC-advance — specifically, Locking the Constitutional Settlement of 201 AG at Personal scale (one named clause) to make it harder to override.

**Why Personal scale (not Relational/Territorial):** Territorial Locking (Ob 7, TN8, pool = Spirit+History only, no TPS) is effectively impossible for any realistic practitioner. Personal scale Locking (Ob 5, TN8) gives P(success) ≈ 8% — still hard, but demonstrable.

### Practitioner State

```
Practitioner — Spirit: 4, History (Legal/Constitutional): 3, TS: 55, TPS: 5
Coherence: 10 | Focus: 3
Lock pool: Spirit(4) + History(3) = 7D (NO TPS for Locking)
TN: 8
RS (shared): 65
```

### Zoom In (Hybrid — from BG Phase 3)

Phase-Lock: Zoom In fires after Phase 3 (manoeuvre complete). State transfer per reference card: RS→65 (direct), TC→38 (suspended), all BG actions suspended.

### Leap (TS 55 ≥ 50 for Locking ✓)

Pool: Attunement(3) + History(3) + TPS(5) = 11D, TN7, Ob1.
E[net] = 3.3. P(Overwhelming) ≈ 90%.

**Overwhelming Leap. TS: 55→56. Contact established. Next op Ob −1 (Ob 5−1 = Ob 4).**

### Diagnosis

Personal scale target: the Constitutional Settlement's "Parliamentary Mandate" clause (the text that limits Church TC-advance without Parliament's formal sanction). Loosely actualised (the clause exists but has been interpreted away by Church practice). Locking Ob: 5 (Personal) −1 (Leap) = **Ob 4.**

### Locking Attempt (Personal scale, Ob 4, TN8)

Pool: 7D, TN8. E[net TN8] = 7 × 0.20 = 1.4. P(net ≥ 4, 7D TN8):

Using the TN8 distribution: each die gives E[net] = 0.20. For P(≥4, 7D TN8):
Approximate: very low probability (~5%).

**Probability breakdown:**
| Degree | Threshold | P(≈) |
|--------|-----------|------|
| Overwhelming (≥8) | net ≥ 8 | <1% |
| Success (≥4) | net ≥ 4 | ~8% |
| Partial (>0 <4) | 1 ≤ net ≤ 3 | ~50% |
| Failure (≤0) | net ≤ 0 | ~42% |

**Most likely: Partial (50%).**

**Partial consequences (Locking):**
- Partial Lock: RS −2. RS: 65→63.
- Coherence: −1 (cap). Coherence: 10→9.
- The clause is partially locked — it creates an additional Ob +1 on any Domain Action attempting to override it this season, but the lock will degrade by next season.

**Second most likely: Failure (42%).**

**Failure consequences (Locking):**
- RS −3. RS: 65→62.
- Coherence: −1. 2 Wounds to practitioner (snap-back). Wound penalty: −1D to future pools per wound.
- Adjacent configurations destabilised: +1 Ob for the season on related Thread operations in this political sphere.

### Co-Movement (fires regardless per P-01)

**Temporal auto-effect (Personal scale):** Narrative only. "The practitioner feels the 201 AG settlement's weight — a room in the palace, men arguing about the exact word 'mandate.' No mechanical effect."

**Epistemic auto-effect (by degree, Partial):** Practitioner knows: the clause's partial lock is visible to any TS 30+ observer in the same building. One Church observer (assumed present in the palace: TS 31, Klapp's early sensitivity) will register "something shifted." This triggers: Church investigation check (+1 to TC at next Accounting if investigation proceeds).

**Actual auto-effect:** Expected d6 consequence — "A document in the palace archive opens to the 201 AG proceedings. A clerk notes it with mild curiosity."

**P-01 compliance: All three auto-effects fired. ✓**

### Zoom Out (Post-Locking)

Per state_transfer_spec PP-107:
- RS consequence: immediate. RS 65→63 (Partial) or 65→62 (Failure).
- No Strength changes (no combat).
- Domain Echo queued: Partial Lock → BG effect: Constitutional Settlement clause has +1 Ob on override Domain Actions for 1 season. This queues as a Domain Echo, fires at next Accounting.
- Epistemic auto-effect (TS 30+ Church observer): TC +1 queued to Accounting (investigation trigger).

BG session resumes from Phase 3.

### Mode D Findings

**F-TH-D-01 (P1):** Locking at Territorial scale is mechanically inaccessible. Ob 7, TN8, no TPS: P(success, 6D pool) <1%. Even TS 80+ practitioners with Spirit 5 + History 3 = 8D TN8: E[net] = 1.6, P(≥7) ≈ 2%. Future-axis Locking at strategic scale is essentially impossible. **This is either intentional design (the future cannot be locked at strategic scale) or a balance error.**

**Finding: Intentional per philosophical foundations.** P-06 (Threadcut beings "radically IS without becoming") implies practitioners CANNOT lock large configurations — the future exceeds Thread capacity at scale. Territorial+ Locking being near-impossible is philosophically consistent. **Flag as design feature, not error.** Add to params: "Territorial Locking (Ob 7) and above is designed as near-impossible. Practitioners who need strategic-level future constraint must use sustained Relational-scale Weaving over multiple seasons instead."

**F-TH-D-02 (P2):** Partial Lock has no stated duration in params_threadwork. Success Lock: "chronic drift begins RS −1/season from season 2." Partial Lock: nothing stated for duration or degradation. **Patch: Partial Lock = degrades after 1 season (same as volatile Weave). Effective Ob reduction (+1 Ob on override) applies this season only.**

**F-TH-D-03 (P1):** Epistemic auto-effect from Locking (Church observer gains TS 31 awareness of Thread operation) triggers TC. This creates a feedback loop: every Thread op in a Church-observed location increases TC. At TC=38 approaching critical threshold, even Partial Lock attempts can accelerate the crisis. **This is mechanically correct per design — Thread operations have political consequences — but the TC trigger rate from epistemic auto-effects is not stated.** Params say epistemic auto-effect produces "social Ob shifts" — what is the TC trigger formula? Not defined.

**Patch: Epistemic auto-effect TC trigger: a TS 30+ Church observer witnessing a Thread op → TC +1 only if the Church initiates an investigation (requires a Church Domain Action to pursue). Observation alone does not trigger TC. This prevents automatic TC escalation from all observed ops.**

**F-TH-D-04 (P2 — Hybrid-specific):** Domain Echo from Thread op (Partial Lock creates +1 Ob on override Domain Actions) has no BG-layer mechanic for representing this. A "+1 Ob on Domain Actions" is a TTRPG mechanic — BG uses Martial rolls, not Ob. **Patch: Thread Lock Domain Echo → BG: flagged territory/card gets Thread Debt token (from PP-106 scope). Thread Debt +1 means that BG-layer political Domain Actions targeting this area roll −1D for 1 season.**

---

## FINDINGS SUMMARY

### P1

| ID | Session | Description | Action |
|----|---------|-------------|--------|
| F-TH-B-03 | B | Actual d6 auto-effect table missing for personal-scale ops | PP-181 |
| F-TH-C-04 | C | Temporal auto-effect RS cost at generational POP not in params | PP-181 |
| F-TH-D-03 | D | TC trigger formula for epistemic auto-effect not defined | PP-182 |

### P2

| ID | Session | Description | Action |
|----|---------|-------------|--------|
| F-TH-A-01 | A | Evidence leverage audience shift uncapped | PP-183 |
| F-TH-A-03 | A | Register Shift needs visible narrative signal | ED-087 |
| F-TH-B-02 | B | Over-actualisation BG translation undefined | PP-184 |
| F-TH-D-01 | D | Territorial Locking near-impossible — document as feature | PP-181 scope |
| F-TH-D-02 | D | Partial Lock duration not stated | PP-182 scope |
| F-TH-D-04 | D | Thread Lock Domain Echo → BG representation | PP-184 scope |

### Design confirmed (not bugs)

- High-resistance debates produce political deadlock between equals ✓
- Historical POP is near-impossible — mundane investigation is primary path ✓
- Territorial Locking inaccessible — philosophically consistent with P-06 ✓
- P-01: All three dimensional auto-effects fired in all sessions (B, C, D confirmed; A: no Thread ops — N/A) ✓

---

## PATCHES REQUIRED

### PP-181: Threadwork missing tables (P1 + P2)
1. Add d6 Actual auto-effect table for personal-scale Thread operations
2. Add temporal auto-effect RS cost table for POP by recency band
3. Document Territorial Locking as near-impossible by design (P-06 consistent)
4. Partial Lock duration: 1 season only

### PP-182: TC trigger and Partial Lock clarification (P1)
1. Epistemic auto-effect TC trigger: observation alone does not trigger TC; Church Domain Action investigation required
2. Partial Lock: degrades after 1 season

### PP-183: Evidence leverage audience shift cap (P2)
1. Cap audience ethical mode shift from ED-077 leverage at weight 2.0 (cannot exceed)

### PP-184: BG Thread consequence representation (P2)
1. Over-actualisation in TTRPG scene → Thread Debt +1 token on corresponding BG territory/faction card at Zoom Out
2. Thread Lock Domain Echo → BG: Thread Debt token. Thread Debt −1D on BG political Domain Actions targeting that card for 1 season
