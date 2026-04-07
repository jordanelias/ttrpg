# VALORIA — STRESS TEST BATCH 10
## Date: 2026-03-27 | Model: Sonnet 4.6
## Coverage targets: M-041–049, M-051–056, PP-081; interaction/scenario/edge gaps
## 7-dimension tagging enforced throughout
## Probability method: expected values (no random dice)

---

## STANDING CHARACTER SHEETS (batch reference)

**Maret** (Attuned practitioner, TS 66, post-Batch 09 state)
Str2 End3 Agi3 Cog5 Mem4 Foc4 Att4 Bon3 Pre3 Spi4
TD 6, Coherence 7 (Strained), Certainty 3
Leap pool: Cog5+Foc4+Thread7 = 16D (TN8 for advanced ops, TN7 standard)
Weaving pool: Cog5+Mem4+Thread7 = 16D
Pulling pool: Cog5+Att4+Thread7 = 16D
Combat pool: Agi3+Sword3 = 6D

**Ehrenwall** (Löwenritter Grandmaster, Knight archetype)
Str4 End4 Agi4 Cog3 Mem3 Foc4 Att3 Bon3 Pre4 Spi3
Combat pool: Agi4+Longsword5 = 9D (TN6 longsword)
Command pool: Cog3+Foc4+Military History4 = 11D
Poise: Pre4+6 = 10

**Himlensendt** (Devout Confessor, TS 0, Certainty 5)
Str2 End3 Agi2 Cog4 Mem4 Foc5 Att3 Bon4 Pre5 Spi4
Social pool: Pre5+Ecclesiastical History7 = 12D
Poise: Pre5+6 = 11
Devout Constraint active. Dissonance Marks: 0.

**Vaynard** (Varfell scholar, TS 14, Dormant)
Str2 End2 Agi2 Cog5 Mem5 Foc4 Att3 Bon3 Pre4 Spi3
Research pool: Cog5+Mem5+Research History6 = 16D
Poise: Pre4+6 = 10

**Generic Riskbreaker** (Niflhel operative archetype)
Str3 End3 Agi4 Cog4 Mem3 Foc3 Att4 Bon3 Pre3 Spi3
Stealth pool: Agi4+Covert History5 = 9D
Intel pool: Cog4+Att4+Intel History4 = 12D
DD: 3 (mid-operation)

**Generic Inquisitor** (Church archetype, TS 0 Devout)
Str3 End4 Agi3 Cog4 Mem4 Foc4 Att3 Bon3 Pre4 Spi4
Investigation pool: Cog4+Foc4+Investigation History5 = 13D
Poise: Pre4+6 = 10. CE: 2.

---

## T-B10-01: THREAD OPERATION IN ACTIVE COMBAT
### 7-Dim Tags: M-046, M-041, M-039 | TTRPG | PRES/CROSS | TT,TD,CERT,ThS | Crown,Löwenritter | Ehrenwall | Practitioner, Löwenritter Knight

**Setup:** Maret (1 Wound, Certainty 3) attempts to perform a Weaving during active combat with two Crown soldiers. Ehrenwall arrives mid-combat, observing. TT: 38.

**Phase 1 — Initiative:**
Priority at declaration. Maret declares Thread operation initiation (Priority 5 per PP-036). Soldiers declare Attack. Ehrenwall observes.

Round structure with PP-036 confirmed: Thread op initiation = Priority 5. Physical attacks = Priority 3. Therefore: Attacks resolve first, then Maret initiates Thread op at Priority 5.

**Phase 2 — Combat resolves first (Priority 3):**
Soldier A (pool 8D TN6): vs Maret defence allocation.
Maret has 6D combat pool. With Thread op pending, he must split between combat defence AND op initiation. Per PP-068: Split action available.
Split action: Thread initiation pool = Att4÷4 = 1D (rounded down). Defence pool = Agi3÷2 = 1D (rounded down). Total combat dice available for defence: 6D − reduced by split = effectively Maret fields 1D defence only (the rest of pool committed elsewhere? No.)

RULING CHECK on PP-068: "split action: Thread op pool = TS÷4 (rounded down); physical defence pool = Coord÷2 (rounded down). The Thread op still initiates at Priority 5." So the Thread op pool in split mode = TS66÷4 = 16D. Defence pool = Agi3÷2 = 1D. The Thread op uses a TS-derived pool, not the regular Weaving pool. This is a significant reduction but TS66÷4 = 16D is still the same as the full Weaving pool (Cog5+Mem4+Thread7 = 16D). This seems too powerful — no split penalty.

**FINDING F-B10-01 (P2):** PP-068 Thread split pool formula (TS÷4) accidentally equals the full Thread pool for high-TS practitioners. At TS 64+, TS÷4 ≥ 16D = full pool. No effective split penalty. Fix: Thread op split pool = (Cog + Mem) only (no History bonus), TN8 (increased difficulty). At Maret's stats: Cog5+Mem4 = 9D, TN8. Expected net at 9D TN8: ~9×0.2 = 1.8 net. Ob typically 3+. This produces ~30% success. Real split cost.

**Applying corrected formula:** Thread split pool = 9D TN8. Ob3 (standard Weaving). P(success at 9D TN8 Ob3): ~30%. P(Partial): ~25%. P(Failure): ~45%.

Defence in split: Agi3÷2 = 1D TN7 vs soldier attack.

Soldier A: 8D TN6 Ob1 (Maret 1D defence): Expected soldier net ~4.8. Maret's 1D defence: expected 0.3 net. Soldier hits by large margin. Damage: Str3+weapon2+margin(~4)−armour0 = ~9 health damage. Maret Health (End3+6=9). Takes 9: Wound threshold. **2nd Wound.** +1 Ob additional (now +2 Ob all rolls).

**Phase 3 — Maret's Thread op (Priority 5), now at 2 Wounds:**
+2 Ob from Wounds. Standard Weaving Ob3+2 = Ob5. Split pool: 9D TN8.
P(net≥5 at 9D TN8): Expected net 9×0.2=1.8. P(≥5): ~3%. Effectively impossible.

**Result:** Maret cannot perform Thread operations while at 2 Wounds using the split action mechanic. He must choose: stop the split (full defence, no Thread op) or accept near-certain Thread failure.

**FINDING F-B10-02 (P1→existing):** Thread ops in active combat at 2+ Wounds are mechanically locked out by Wound Ob stacking on an already-reduced split pool. This is CORRECT BEHAVIOUR — wounded practitioners shouldn't be Weaving in combat. PP-001 and PP-022 (Wound penalties) are functioning as intended. Not a new finding; confirms existing design intent.

**Phase 4 — Ehrenwall's observation:**
Maret (2 Wounds, attempting Thread op) is visible to Ehrenwall. She has CE 0 (Devout-adjacent military character). Observation of attempted Thread op: CE +1 check (was she close enough? Within zone). CE: 0→1. First CE threshold. No immediate mechanical effect beyond tagging.

**Co-movement (Thread op — attempted and failed):**
Failure result: Thread op fails (Partial at best given above). TT +1 (Partial attempt). TD: +1. Co-movement fires on attempt regardless of outcome (P-01): temporal auto-effect (CD+1), epistemic auto-effect (investigation Ob+1 in this location), actual d6.

**Ehrenwall CE 1 + Thread Exposure:** Standard — no TS growth check at CE 1.

**State after T-B10-01:**
Maret: 2 Wounds, Certainty 3, TD 7, CD 7 (Coherence 7 unchanged), TT 39.
Ehrenwall: CE 1.

**VERDICT:** CLEAN. Thread ops in combat create genuine tactical dilemmas. At 2 Wounds, split-action Thread ops are near-impossible (correct). PP-068 split pool formula needs fixing (F-B10-01, P2). Co-movement still fires on failed attempts (P-01 confirmed).

---

## T-B10-02: THREAD EVENT ERUPTION DURING GRAND DEBATE
### 7-Dim Tags: M-047, M-037, M-011 | TTRPG | CROSS | TT,TS,CERT,TC | Church,Crown | Himlensendt,Almud | Practitioner,Devout Character,Faction Leader

**Setup:** Almud's court. Grand Debate between Crown (represented by a Crown political operative, Presence 4, Social pool 13D) and Church (Himlensendt, Social pool 12D). Debate is at Exchange 3 (score 1-1). TT: 45 (Wakening threshold crossed).

At TT 45+: "Monstrous Incursion in one territory, Church investigates." The incursion is in the adjacent Valorsplatz district. A Mode 1 entity configuration is active nearby.

**Thread Event Trigger:** At TT 45, Thread Events in Social scenes: per M-047, environmental Thread saturation can interrupt social scenes. With TT at 45 and a Mode 1 incursion in the same city: passive ThS check. ThS at 12 (elevated from Batch 09 operations). At ThS 12: Inquisitors detect passively (TS 10+, Ob 1).

Two Church Inquisitors are present as observers of the Debate. CE 2 each. TS 0 (Devout). Passive ThS check (TS 0 in a ThS 12 environment): no Thread perception (below TS 10 threshold). But CE 2 characters feel wrongness (per PP-017: CE 2 = "repeated exposure — feel wrongness near residue even without TS").

**Thread Event eruption mid-Debate:**
GM calls: Mode 1 entity destabilises, pushing into the Debate chamber. Physical manifestation: objects move, temperature drops. Non-practitioners in room: Spirit TN7 Ob1 Certainty checks.

Himlensendt (Certainty 5, Devout, +2D Devout bonus vs monstrous): Spirit4D+2D = 6D TN7 Ob1.
P(success with 6D TN7 Ob1): ~92%. Expected net: ~2.0. Success.
Certainty holds (5→5). Theological Dissonance check fires: Spirit4D TN7 Ob1. P(success): ~80%. Success. No Dissonance Mark.

Crown operative (non-Devout, Certainty 4): Spirit3D TN7 Ob1. P(success): ~68%. 
Expected result: Success (~68% of the time). Certainty holds.

Two Inquisitors (CE 2, Spirit4 each): 4D TN7 Ob1. P(success): ~80% each. 
Expected: both succeed (~64% both succeed). Certainty holds for both. But: CE 2 + direct entity exposure = CE growth check. CE 2→3.

At CE 3: TS growth check fires for Inquisitors. Spirit4D TN7 Ob1: P(success): ~80%. Success → +5 TS. Inquisitors go from TS 0 to TS 5 (Inert). Devout Constraint blocks growth check per standard rules — but CE 3 exposure BYPASSES Devout block (per T4 test, confirmed ruling). TS growth fires regardless.

Devout Inquisitors now at TS 5: Theological Dissonance Events fire for each. Both Spirit checks: ~80% success. Success → framework holds, Certainty −1 each (4→3 each). No Dissonance Marks.

**Debate interruption:**
Thread Event = scene disruption. Both Debate participants are shaken. Per M-047: Thread Events in Social scenes impose Ob +1 on the next Debate exchange for all participants (environmental destabilisation). 

Exchange 4 with +1 Ob:
Crown operative: 13D − 2D (mismatch, was already factored) + contextual, TN7, Ob 3+1=4. Expected net ~13×0.33=4.3. P(≥4): ~65%.
Himlensendt: 12D TN7, Ob 3+1=4. Expected net ~4.0. P(≥4): ~60%.

Near-equal exchange. Crown wins slightly by probability.

**TC consequence:** Public Thread event in Parliament context: TC +1 (39→40... wait, TT is 45, TC tracking separate). TC was at 22 (from B5). Now: TC +1 (23). Plus: two Inquisitors involuntarily gained TS — if this becomes known to Church leadership, TC +2 (Inquisitor contamination = institutional crisis). Not immediate — banked for next seasonal accounting.

**Co-movement from Mode 1 incursion:**
P-01: Mode 1 entity presence generates co-movement effects (the entity is a Thread-side configuration expressing into the rendered world). All three dimensions fire: temporal (local CD +1 for any Thread-sensitive in room — Inquisitors at TS5 now qualify), epistemic (social rolls Ob +1 for 1 scene — applied above), actual (d6 table: drawn toward Thread-side, environmental wrongness).

**FINDING F-B10-03 (P2):** The Devout bypass at CE 3 creates two Inquisitors with involuntary TS 5 mid-Debate. This is mechanically correct but will have major narrative consequences (Church must now investigate its own Inquisitors). The mechanic creates the intended paradox: the Church's investigative apparatus becomes contaminated by what it investigates. No mechanical issue — design confirmation.

**FINDING F-B10-04 (P3):** Thread Event Ob +1 interruption applies to the entire next exchange, not just one participant. The fairness of the Debate is disrupted equally for both sides. This is intentional (Thread events don't take sides) but should be explicit in M-047 text: "Ob +1 applies to all participants' next exchange, not just the participant most exposed."

**State after T-B10-02:**
TC: 23 (→ +2 at accounting if Inquisitor TS becomes known = TC 25).
Two Inquisitors: TS 5, Certainty 3, CE 3, Dissonance Marks 0.
Debate result: Exchange 4 slight Crown advantage. Score: Crown 2–1 Church.
TT: 45 (unchanged — entity was already counted at crossing).

**VERDICT:** CLEAN. M-047 works correctly. Thread events in social scenes: Certainty pressure, TS contamination pathway, and narrative consequence all function without crunch cascade.

---

## T-B10-03: SCALE TRANSITION — PERSONAL THREAD OP TO FACTION STAT CASCADE
### 7-Dim Tags: M-048, M-035, M-038 | HYB | CROSS | FSTAT,TT,TC,IP | Crown,Church | Almud | Faction Leader,Practitioner

**Setup:** Hybrid mode. Personal Phase: Maret (Certainty 3, post-B10-01: 2 Wounds, Coherence 7) performs a Weaving on the Crown's diplomatic correspondence before it reaches the Altonian ambassador. Relational scale, Ob 3. Domain Echo eligible: Overwhelming → Crown Influence +1 at Cascade Phase.

**Wound status check:** 2 Wounds = Ob+2 on all rolls. Weaving Ob3+2 = Ob5. Full Weaving pool 16D TN7.
Expected net: ~16×0.33=5.3. P(≥5): ~65%. P(≥10/Overwhelming): ~15%.

Most likely: **Success** (net ≥5, <10). Domain Echo: not triggered (requires Overwhelming).

**Scale transition — what does a Success on this Weaving do?**
Success: "full effect, standard duration." The Weaving alters the relational Thread-configuration of the correspondence — the Altonian ambassador's response will be shaped by this alteration, though they don't know it. This is not Overwhelming, so no Domain Echo to faction stats.

**What if Maret spends an Inspiration (Duty to Einhir, rating 3)?**
Stunt: 5 auto-successes (Spi4 = Pre? No — Stunt = relevant attribute auto-successes = Spirit4 = 4 auto-successes). Plus Spirit dice (4D chain on 10): expected 4×0.1×1.1/(1-0.1) ≈ 0.49 chain successes. Plus remaining Weaving pool: 16D normal.
Total: 4 + ~0.5 + 16×0.33(~5.3) = ~9.8 net. P(≥10): ~45% from the 16D portion alone.

**With Stunt:** P(Overwhelming ~45%). Domain Echo triggers ~45% of attempts with Stunt expenditure.

**Domain Echo mechanics (PP-039, M-048):**
Personal Overwhelming Thread op → Crown faction stat +1 (Influence) at Cascade Phase. Counts as Crown's Political Domain Action for this season (PP-040). Crown cannot also take a Political Domain Action in Strategic Phase.

**Scale transition test — information flow:**
At Strategic Phase, Crown player would normally take a Govern or Influence order. With the Domain Echo consuming the Political slot:
- Crown can still take Economic and Military orders (different tiers per PP-005)
- Crown's Political slot is consumed by Maret's personal Thread op
- This is the intended trade-off: personal-scale Thread work provides faction-level benefit at the cost of a faction-level action slot

**Timing check (R-ST-H1 confirmed):**
Domain Echo applies at Cascade Phase. Strategic Phase Crown orders use pre-Echo stats. If Crown Influence is currently 5: Cascade Phase → 5+1=6. Next season's Strategic Phase uses Influence 6. Clean timing.

**Seasonal cap check:** Crown Influence +1 from Echo. Seasonal cap ±2. If no other Influence changes: within cap. If Serena's social actions also generated an Influence +1 Echo earlier this season: total = +2 (at cap). A third Echo from a different source this season would be capped (PP-003 chronological priority rule applies).

**FINDING F-B10-05 (P3):** The Domain Echo Political slot consumption (PP-040) creates an invisible constraint: Crown player may not realize their Thread operative's action consumed their Strategic Phase political slot until Cascade Phase reveals it. Add explicit notification: "At Cascade Phase, announce which Domain Action slot each Echo consumes before Strategic Phase resolution of remaining orders."

**State after T-B10-03:**
Crown Influence: 5→6 (Cascade Phase, ~45% with Stunt).
Crown Political Domain Action: consumed this season.
Maret: Certainty 3−1 (Leap cost) = 2. 2 Wounds. TD 7→8.

**VERDICT:** CLEAN. Scale transition works. Domain Echo slot consumption is correct mechanic. Timing rules prevent laundering. One P3 notification gap.

---

## T-B10-04: FULL INQUISITOR INVESTIGATION CHAIN
### 7-Dim Tags: M-049, M-052, M-031 | TTRPG | CROSS | CE,TC,TS,CERT,DD | Church,Crown,Niflhel | Olafsson,Klapp | Inquisitor,Riskbreaker

**Setup:** Cardinal Olafsson has authorised an Inquisitorial investigation of suspected Thread activity in the docks district (Niflhel territory, ThS 8 from prior operations). Lead Inquisitor (CE 2, TS 0 Devout, Certainty 4). A Niflhel Riskbreaker (DD 3, Cover identity: Circles 2 with dock workers) is operating in the same area.

**Stage 1 — CE accumulation (M-049):**
Inquisitor enters ThS 8 environment. CE 2 → does environment trigger CE growth? Per PP-017: CE increments from specific exposure events, not ambient ThS. However, ThS 8 = passive detection at TS 10+. Inquisitor has TS 0 (Devout) — no passive detection. CE accumulation requires specific interaction.

Inquisitor investigates residue handling (dock workers moving Thread-affected goods, unknowingly). This is CE exposure qualifying event: CE 2→3 check.
Investigation pool: Cog4+Foc4+Investigation5 = 13D TN7 Ob2 (investigate).
Expected net: ~13×0.33=4.3. P(≥2): ~98%. Success easily.

Success: Inquisitor finds material evidence of Thread-affected goods. CE growth event confirmed. Spirit check (CE growth): 4D TN7 Ob1. P(≥1): ~80%. Success → CE 2→3. TS growth check fires (per PP-017).

**Devout bypass at CE 3:** TS growth check fires despite Devout. Spirit4D TN7 Ob1: P(success): ~80%. Success → TS: 0→5. Theological Dissonance Event: Spirit4D TN7 Ob1: P(success): ~80%. Success → framework holds, Certainty −1 (4→3). Dissonance Mark: 0.

**Stage 2 — Concealment (M-052) and Riskbreaker interaction:**
Riskbreaker's cover (Circles 2 with dock workers, DD 3). Exposure check this season: Ob = DD÷2 = 1.5 → Ob2. Roll: Agi4+Covert5 = 9D TN7 Ob2.
Expected net: ~9×0.33=3.0. P(≥2): ~86%. Cover maintained.

Inquisitor investigation intersects with Riskbreaker's operation? Inquisitor finds residue in dock location where Riskbreaker has been active. Does Inquisitor connect residue to a person?

Per PP-063 (Concealment): Inquisitor discovers the residue; Riskbreaker's cover identity insulates them. Inquisitor rolls Cog4+Investigation5 = 9D TN7 Ob = Riskbreaker's Circles(cover) rating = Ob2 (Circles 2).
P(success with 9D vs Ob2): ~86%. Inquisitor succeeds — they identify that someone with dock worker access has been handling the goods, but cannot name the Riskbreaker specifically (Circles cover = dock worker identity, not true identity).

Riskbreaker DD: +2 (standard op detected) → DD 3→5. Exposure check next season: Ob = 5÷2 = Ob3. Higher risk.

**Stage 3 — TC consequence (M-031):**
Inquisitorial investigation active (formal process): TC +2 per season while active (from §K per audit). TC: 23→25. Additional: Inquisitor has now personally gained TS 5 (contamination). If reported to Church hierarchy: TC +2 (Inquisitor contamination). But Devout Inquisitor will likely NOT report personal TS gain — it contradicts their theology. GM banks TC +2 as deferred: fires if/when Inquisitor's state is discovered (e.g., by Cardinal Klapp reviewing the investigation).

**Olafsson-Niflhel connection (from editorial authorship register — undecided):**
Olafsson has an outer-channel connection to Niflhel Dockworkers. If Olafsson knows the investigation is active: does he warn Niflhel? Per the register, this decision is pending (A/B/C options). Currently treating as Olafsson-unaware (option B: purely operational channel, Olafsson doesn't know this specific investigation is active). Riskbreaker receives no warning. Clean test of the mechanic without editorial dependency.

**FINDING F-B10-06 (P1→P2):** Inquisitor TS contamination at CE 3 creates a Devout character with TS 5 who CANNOT use that TS (Devout Constraint blocks active Thread practice) but IS perceived by other Thread-sensitive characters as Attuned. A practitioner (Maret, TS 66) encountering this Inquisitor would Diagnose TS 5 presence. The Inquisitor doesn't know. This creates an information asymmetry: practitioners see contamination that the Inquisitor cannot. Confirm this is intentional (it is: per P-10, epistemic seduction is a perceptual shift — the Devout character is the last to perceive their own transformation).

**State after T-B10-04:**
Inquisitor: CE 3, TS 5, Certainty 3.
Riskbreaker: DD 5, cover maintained.
TC: 25 (formal investigation active). Banked: TC +2 if contamination discovered.
TT: 45 (unchanged — investigation is a rendered-side process, not a Thread op).

**VERDICT:** CLEAN. Inquisitor investigation chain functions without cascade. The TS contamination pathway for Devout characters is mechanically elegant. Riskbreaker concealment holds correctly. TC accumulation from investigation is as expected.

---

## T-B10-05: DEVOUT CONSTRAINT — EDGE CASES AT CRITICAL THRESHOLDS
### 7-Dim Tags: M-051, M-047, M-009 | TTRPG | CROSS | CERT,TC,TS,TD | Church,Hafenmark | Himlensendt,Baralta | Devout Character

**Edge Case A — Devout at Certainty 1:**
Himlensendt (Certainty 5→3 from T-B10-02 via a further Thread exposure event, then −1 from Dissonance = 2). Now encounters a second Thread event (Mode 2: temporary Providence organisation, single scene). Spirit check TN7 Ob1 to maintain Certainty.

Himlensendt Spirit4D +2D Devout bonus = 6D TN7 Ob1. P(success): ~92%. Expected: success.
But what if he fails (8% probability)? Certainty 2→1. At Certainty 1: one more loss = Rendering Crisis.

**Certainty 1 + another Thread event (Mode 2):** 6D TN7 Ob1. P(failure): ~8%. If failure: Certainty 0 → Rendering Crisis.

**Rendering Crisis for Devout character:**
Standard Rendering Crisis = Belief revision required. For Himlensendt (sincere Devout, zero TS awareness): his Beliefs are:
1. "Solmund is the ground of being; the Arrogance is the supreme sin."
2. "The Church must expand to protect Valoria from spiritual contamination."

Rendering Crisis: he must revise one Belief. For a sincere Devout character at Certainty 0:
- The crisis cannot be framed as "Thread is real" — he has no framework for that interpretation
- Instead: the Crisis manifests as a profound theological crisis — his sense of Solmund's reality is shaken, not by Thread evidence, but by the visceral experience of something he cannot categorise
- Belief revision options: he could revise toward "The Calamity was not caused by human Arrogance — it came from outside human action" (a theological shift, not a Thread acknowledgement)
- +2 CP for revision; Certainty restores to 3 after revision scene

**RULING CONFIRMED:** Devout Rendering Crisis resolves as theological crisis (Belief revision within theological framework), not as Thread acknowledgement. The practitioner reads it through their own lens. P-08 (epistemological barrier = inaccessibility, not suppression) is confirmed: Himlensendt cannot interpret the experience as Thread-reality even in crisis.

**Edge Case B — Devout at 3 Dissonance Marks:**
Baralta (Devout, constitutional legalist, 2 Dissonance Marks from prior sessions). A third qualifying event: Maret performs Thread operation in Baralta's direct presence (Grand Debate scene, T-B10-02 scenario continued). Does this count as a qualifying confrontation event?

Per T4 ruling: Discovery Events bypass Devout block. Maret's operation in Baralta's presence = not a Discovery Event unless the Thread effect physically manifests on Baralta. If Maret succeeds at a standard Weaving (no blast radius): Baralta has no qualifying event. Only FR Dissolution generates blast radius.

If Maret performs FR Dissolution in Baralta's presence: blast radius fires. Spirit check (non-practitioner): Baralta Spirit4D TN7 Ob1: P(failure): ~20%. If fail: Certainty −1 (4→3). This qualifies as confrontation event. Theological Dissonance check: Spirit4D TN7 Ob1. P(failure): ~20%. If fail: Dissonance Mark (2→3). **Constraint collapse.**

**Constraint collapse at 3 Dissonance Marks:**
Baralta's Devout Constraint collapses. She can now attempt TS growth checks. Her existing TS is 0. First TS growth check (next qualifying confrontation): Spirit4D TN7 Ob1: P(success): ~80%. TS: 0→5.

**Mechanical consequence for Baralta's archetype:**
Baralta is described as a constitutional legalist whose faith places her above the Confessor. If her Devout Constraint collapses, she loses the Devout bonus (+2D Certainty checks vs monstrous) AND gains Thread perception capacity. This is a major character arc event. No new P1 findings — the mechanic works correctly. Flagging as: **NARRATIVE CONSEQUENCE** — GMs must prepare this arc if Baralta is a significant NPC.

**Edge Case C — Simultaneous Rendering Crisis (two Devout characters):**
From T-B10-02: both Inquisitors at CE 3, Certainty 3. If a third Thread event hits in the same scene: both make Certainty checks. P(both fail, 4D TN7 Ob1): ~4% each → ~0.16% simultaneous. Extremely rare.

If simultaneous: two Rendering Crises must each independently resolve. No mechanic prevents simultaneous crises. No interaction rule needed — they resolve independently in the same scene. **Clean.**

**VERDICT:** CLEAN. Devout Constraint edge cases all resolve cleanly. Rendering Crisis for Devout = theological revision (not Thread acknowledgement). Constraint collapse at 3 Marks functions. Baralta's potential collapse is a significant narrative landmark.

---

## T-B10-06: EINHIR SITES + WEAVING + PAST-ORIENTED PULLING CHAIN
### 7-Dim Tags: M-054, M-015, M-019 | TTRPG | PAST/CROSS | TT,TS,TC,ThS | Varfell,Revolution | Vaynard,Maret Uln | Non-TS Scholar,Practitioner

**Setup:** Vaynard (TS 14, Dormant) has located a functioning Einhir site (ThS 18 at site — fully active). Maret (TS 66) accompanies as practitioner consultant. Vaynard's research goal: understand the site's Thread-side configuration (he cannot perceive it directly at TS 14 — below TS 30 Diagnosis threshold... wait, TS 30 is required for passive detection at arm's reach per PP-017. Diagnosis: what's the TS requirement?

Per skill file: "Diagnosis: TS 10+ required (Dormant tier minimum)." Vaynard at TS 14: CAN perform Diagnosis. But his pool would be limited.

**Stage 1 — Einhir Site passive detection:**
At ThS 18: "Ob 1 passive detection for any TS ≥ 1 character." Both Maret (TS 66) and Vaynard (TS 14) detect the site passively upon entering. No roll required at Ob 1 with any pool. ThS 18 is extremely active.

Per PP-042: Dampening Weave option (TS ≥ 20, Ob 3) to reduce site's effective ThS by 8. Maret qualifies (TS 66). Dampening Weave: Weaving pool 16D TN7 Ob3. Expected net: ~5.3. P(≥3): ~87%. Expected: success. ThS 18→10. Detection threshold for TS 1+: Ob 1 still (ThS 10 ≥ detection threshold). Dampening insufficient to achieve full concealment — reduces exposure window only (detection by TS 30+ passerby now requires active investigation, not passive).

**Stage 2 — Vaynard's Diagnosis:**
Vaynard attempts Diagnosis of site configuration. TS 14, Diagnosis pool: TS÷10+Att+Mem = 1+3+5 = 9D? The Diagnosis pool formula needs checking against compiled rules. Standard Diagnosis pool from stress tests: "Cog+Att+Thread History" but for low-TS practitioners, the Thread History bonus is 0 (no Thread History). Vaynard has Research History6 (Cog5+Mem5+Research6 = relevant but not Thread-specific). At TS 14: no Thread History, no Attunement bonus from Thread ops.

**RULING NEEDED (R-B10-01):** Diagnosis pool for low-TS non-practitioners (TS 10–29): Att + Foc (awareness attributes) only, no History bonus. Ob 3 (standard Diagnosis). Pool: Att3+Foc4 = 7D. Expected net: 7×0.33=2.3. P(≥3): ~40%. Likely Partial.

Partial Diagnosis: "vague impression only" — Vaynard senses something active at the site but cannot identify the configuration type. He can record this as research data but not act on Thread-level precision.

**Stage 3 — Maret's Past-Oriented Pulling on site:**
Maret (TS 66 ≥ 70 threshold for Past-Oriented Pull? NO — TS 66 is in Attuned tier (50–69). Past-Oriented Pull requires TS 70+. Cannot proceed.

**FINDING F-B10-07 (P1):** Einhir site testing requires TS 70+ practitioner for Past-Oriented Pull testing. Maret at TS 66 cannot execute this op. The test must be deferred to a scenario where a TS 70+ character is available, or Maret must advance TS to 70+ first. FLAG: **gap in test coverage for M-019 (Past-Oriented Pulling) in Einhir Site context**. Requires dedicated test with high-TS character.

**Stage 3 (revised) — Standard Weaving on site:**
Maret performs Weaving instead. Einhir site provides: −1 Ob to Thread operations performed at site (existing design benefit). Weaving Ob3−1 = Ob2. Pool 16D TN7.
Expected net: ~5.3. P(≥2): ~99%. P(≥4/Overwhelming): ~85%.

Overwhelming result (85% chance): extended duration, TT −1. TT: 45→44. Plus standard Einhir site Weaving consequence: site's ThS −2 (Weaving absorbs local Thread energy). ThS 10→8.

Co-movement: CD+1 (Maret CD 7→8: entering −2D Memory-based tier). Epistemic: Weaving in Einhir site context — investigation of site +1 Ob for 1 session. Actual d6.

**Stage 4 — Vaynard observing active Weaving (Discovery Event):**
Vaynard witnesses Maret Weaving at an Einhir site. Does this qualify as a Discovery Event? Per T4: "Maret performs a Dissolution in Valdis's direct presence. The Certainty blast radius fires." Dissolution triggers blast radius. Standard Weaving does NOT (confirmed R-ST-H3). Vaynard: no Certainty check. No TS growth event from observation alone.

But: Vaynard is a "Sensitive scholar" type with active Thread research history. Research History at Einhir site = qualifying academic exposure event. CE +1 (Vaynard CE: 0→1, first exposure event). No immediate growth check at CE 1.

**VERDICT:** CLEAN with one gap. M-054 (Einhir sites) + M-015 (Weaving) work correctly. Low-TS Diagnosis produces Partial (correct). Past-Oriented Pull test deferred (M-019 gap with current character roster — needs TS 70+ character). Einhir site Ob reduction benefit confirmed. ThS depletion from active Weaving confirmed.

---

## T-B10-07: RESTORATION COMMUNITY WEAVING — COLLECTIVE OPERATION
### 7-Dim Tags: M-055, M-013, M-021 | TTRPG/HYB | PAST/PRES/CROSS | TT,ThS,CERT,TC,COH | Revolution,Church | Maret Uln | Practitioner,Faction Leader

**Setup:** Maret (Coherence 7, TD 8) participates in a Restoration Community Weaving with 3 Restoration community members (TS 25, 18, 22 — Dormant tier). Maret is the Anchor. Collective operation: Weaving at Relational scale aimed at a degraded Thread configuration in a Restoration village.

**Collective pool (PP-013 — confirmed):**
Anchor (Maret): full Weaving pool 16D. Helpers contribute primary attribute (Att) only.
Helper 1 (Att 3): +3D. Helper 2 (Att 3): +3D. Helper 3 (Att 4): +4D.
Total pool: 16+3+3+4 = 26D TN7 Ob4 (Relational scale, Territorial if all three Helpers push: Ob5).

At Ob4: Expected net 26×0.33=8.6. P(≥4): ~99%. P(≥8/Overwhelming Ob4): ~88%.

**Coherence recovery (PP-062 — approved):**
Restoration Community Weaving in Restoration context: on any success, Maret recovers Coherence +1.
Maret Coherence 7→8. Maximum recovery toward original (assume Coherence started at 10): 8/10.

**TT impact:**
Overwhelming collective Weaving: TT −1. TT: 44→43. But three Helpers add three additional auto-effects per PP-013: 3 additional co-movement effects fire (one per Helper beyond Anchor). Each effect rolls independently for actual d6 consequence.

3 additional actual d6 rolls: each could generate TT consequences (table results). Expected: 1-2 of 3 produce neutral or mildly positive results; 1 in 3 chance of a TT-positive event per roll. Expected total: TT −1 (from Overwhelming) + possible TT perturbations from d6 results. Net TT change likely −1 to 0.

**Epistemic auto-effects (3 additional fires):** Investigation of this area +1 Ob ×3 applications? Per PP-013: "Automatic effects fire once per participant beyond the Anchor." Three additional epistemic auto-effects: investigation of target area +1 Ob (stacking? or once?).

**FINDING F-B10-08 (P2):** PP-013 specifies "auto-effects fire once per participant beyond the Anchor" but doesn't specify whether same-type auto-effects STACK (e.g., 3× epistemic = investigation +3 Ob) or apply ONCE each (regardless of how many fires the same effect). Stacking would make large collective operations make areas nearly uninvestigatable. Ruling needed:
**RULING (R-B10-02):** Same-type auto-effects from collective operations do not stack. Each type fires once per collective op regardless of participant count. Participant count adds ADDITIONAL ROLLS on the actual d6 table (different result each time), but temporal and epistemic auto-effects are not multiplied. This prevents collective ops from producing absurd epistemic shutdowns.

**TD accumulation:**
All participants accrue TD. Maret: TD 8→9 (temporal auto-effect from Anchor's perspective + one additional from Helper contribution per R-B10-02 revised: temporal auto-effect fires once). Wait — if temporal auto-effect fires ONCE per collective op (R-B10-02), then TD cost is the same as a solo op for the Anchor. Helpers still accrue TD? Per PP-013: "Each Helper's contact window expires naturally per their own TD rules." Helpers accrue their own TD at their own rates. Maret (Anchor): standard TD +1 from temporal auto-effect. TD 8→9.

**Maret at TD 9 (approaching max of 20):**
At TD 9: Pull success probability = ? Per PP-001 audit: at TD 15, Pull ~2% success. At TD 9: still functional but degraded. The TD recovery mechanic (PP-001: −3 per zero-ops season) means Maret needs 3 zero-ops seasons to clear TD 9 back to 0. That's 3 full seasons of no Thread work. 

**Community connection outcome:**
Helpers' Knots to Maret: each participating Helper forms or strengthens a Knot with Maret (they've shared Thread contact). Per P-12 (relational contagion): transformation propagates through Knots. Maret at Coherence 7 (Strained): his Knot to each Helper gains +1 strain from relational contagion check. Three Helpers: three Knots at strain 1 (new). Maret's existing Knots unaffected (contagion propagates forward in new connections, not retroactively).

**VERDICT:** CLEAN. M-055 (Restoration Community Weaving) functions. Coherence recovery (+1) confirmed. TT reduction confirmed. PP-013 collective scaling applies. One P2 gap (F-B10-08: stacking of same-type auto-effects) resolved by R-B10-02.

---

## T-B10-08: NIFLHEL DESTABILISATION — FULL COVERT OPERATION CHAIN
### 7-Dim Tags: M-056, M-034, M-050 | BG | CROSS | FSTAT,TC,TT,DD | Niflhel,Church,Crown | — | Riskbreaker,Faction Leader

**Setup:** Board game mode. Season 6. Niflhel (Intel 6, Influence 5, Wealth 4, Stability 4 — confirmed stats). Church TC: 30. Niflhel's goal: slow TC accumulation.

**Niflhel Seasonal Actions (3 available):**
Action 1: Recruit Riskbreaker (PP-064). Wealth 2 cost + Intel Ob2.
Intel 6D TN7 Ob2: Expected net ~6×0.33=2.0. P(≥2): ~70%. Success.
New Riskbreaker: DD 0, Circles(cover) 1 in Church. Niflhel Wealth: 4→2.

Action 2: Destabilisation operation (M-056). Target: Church TC accumulation (reduce Church Stability to trigger TC brake per PP-080: brake fires at Stability ≤3).
Church Stability: 5. Niflhel needs to reduce it by 2. Standard destabilisation: Intel roll vs target faction Stability.

Niflhel Intel6D TN7 vs Church Stability5 (Ob5): Expected net ~2.0. P(≥5): ~8%. Near-impossible directly.
This is the problem: Niflhel cannot directly reduce Church Stability through a single Domain Action if Ob = target Stability. They need an intermediary approach.

**FINDING F-B10-09 (P2):** Niflhel Destabilisation targeting Church Stability (5) with Intel 6 pool faces Ob5 — ~8% success. Niflhel's covert operations are designed to be effective against their targets. Ob = raw Stability creates an asymmetry where Niflhel can barely affect stable factions. 

**PROPOSED RULING (R-B10-03):** Niflhel Destabilisation Ob = target Stability ÷ 2 (round up), not raw Stability. At Church Stability 5: Ob = 3. Niflhel 6D TN7 vs Ob3: P(≥3): ~68%. Much more functional. This aligns with PP-004's threshold formula (Mandate + Stability ÷ 4) which similarly scales Ob.

**Applying revised Ob:** Intel 6D TN7 Ob3: P(success): ~68%. Expected: Success.
Success: Church Stability −1 (5→4). Riskbreaker DD: 0→2 (standard op).

Action 3: Second Destabilisation on Church (Riskbreaker now inside).
+1D bonus from Riskbreaker inside target faction (PP-008 stat interaction: Intel 6+1D from embedded Riskbreaker = 7D).
7D TN7 Ob3 (Church Stability now 4 → Ob 4÷2=2): P(≥2): ~92%. 
Success: Church Stability −1 (4→3). Riskbreaker DD: 2→4. Now at DD4.

**Result:** Church Stability 3 = TC brake threshold (PP-080). TC accumulation this season: halved.

**Church passive detection (PP-044):** Church Intel? Not in standard Church stats. Church has Mandate/Influence/Wealth/Military/Stability. No Intel stat for Church. Therefore: Church gets no passive covert detection roll. 

**FINDING F-B10-10 (P2):** Not all factions have Intel stats. Church, Crown, Hafenmark, Varfell, Guilds, Revolution, Löwenritter may not have Intel. Only Niflhel is confirmed with Intel 6. Löwenritter has Intel 3 (from succession chat). The passive detection mechanic (PP-044: Intel ≥ 4 → detection check) only applies to factions with Intel. Church cannot detect Niflhel ops passively. This may be intentional (Church has no covert intelligence apparatus — only formal investigation processes). Document explicitly: passive Intel detection requires an Intel stat; factions without Intel cannot detect covert operations passively.

**TC accumulation with brake:**
Church TC this season: standard +2 (from M-031 seasonal accumulation) → halved by PP-080 brake = +1. TC: 30→31. Without Niflhel operation: TC 30→32. Net suppression: −1 TC from Niflhel's entire 3-action season.

**DESIGN CONCERN:** Niflhel's maximum seasonal TC suppression (−1 TC at best) vs Church's passive TC accumulation (+2/season base) means Niflhel can only slow TC, not reverse it. This is confirmed as intentional per PP-060: "Niflhel's role is to slow TC accumulation, not reverse it." But the Riskbreaker operation consumed 2 of 3 actions (Recruit + 2× Destabilisation) and spent Wealth 2 — significant resource cost for −1 TC. Is this cost-efficient?

Niflhel's alternative: spend the 3 actions on Intel gathering (learning Church plans) + 1 targeted Destabilisation. More flexible, similar TC effect. The 2-action Destabilisation chain is a high-commitment play.

**VERDICT:** CLEAN with two P2 gaps. Niflhel Destabilisation Ob formula needs standardising (F-B10-09, R-B10-03). Intel-less factions cannot detect covert ops (F-B10-10). TC suppression at expected scale (−1/season maximum). Riskbreaker embedded mechanic functions.

---

## T-B10-09: FULL COMBAT RESOLUTION CHAIN — EQUIPMENT + DAMAGE + MANOEUVRES
### 7-Dim Tags: M-041, M-042, M-043, M-044 | TTRPG | PRES | — | Löwenritter,Niflhel | Ehrenwall | Löwenritter Knight,Riskbreaker

**Setup:** Ehrenwall (Löwenritter Knight archetype) vs Generic Riskbreaker. Ehrenwall: full plate (AR 3), longsword (TN6 attack, Damage+3). Riskbreaker: light armour (AR 1), short sword (TN6, Damage+2) and thrown dagger (TN7, Damage+1, range throwing).

**Initiative (M-039):**
Ehrenwall Agi4 vs Riskbreaker Agi4: tie. Per PP-033: tied initiative → higher End stat acts first (Ehrenwall End4 = Riskbreaker End3). Ehrenwall wins initiative — declares last.

**Round 1 Declaration:**
Riskbreaker declares first: Manoeuvre — Disarm attempt (M-044).
Ehrenwall sees Disarm coming, declares Attack (commits 7D offence, 2D defence from pool of 9D).

**Pool split (M-041):**
Ehrenwall pool: 9D total (Agi4+Longsword5). Split: 7D Offence / 2D Defence.
Riskbreaker pool: 8D (Agi4+ShortSword4). Manoeuvre (Disarm): uses Offence dice, Ob = opponent's pool ÷ 2 = 9÷2 = 4.5 → Ob5. Riskbreaker commits 8D to Manoeuvre.

**Resolution (Priority 3 — both melee):**
Simultaneous resolution.

Riskbreaker Disarm: 8D TN6 vs Ob5. Expected net: 8×0.45=3.6. P(≥5): ~28%. Likely failure.
Ehrenwall Attack: 7D TN6 vs Riskbreaker Defence (Riskbreaker committed all dice to Manoeuvre, 0D Defence): 7D TN6 vs Ob0 (any success hits).
P(Ehrenwall hits): P(≥1 net from 7D TN6): ~98%. Ehrenwall hits reliably.

Damage (M-042): Ehrenwall Str4 + weapon bonus3 + net successes(~3.5 average) − Riskbreaker AR1 = ~9.5 health damage.
Riskbreaker Health (End3+6=9). Takes ~9.5: at or past Health threshold → **Wound**. Health resets (9), carries over ~0.5 (negligible). Riskbreaker takes 1 Wound. +1 Ob all rolls.

Riskbreaker Disarm: P(≥5 at 8D TN6): ~28%. If fails (72% chance): longsword not disarmed. Riskbreaker takes Wound and achieved nothing.

**Riskbreaker reconsiders (Round 2):**
1 Wound. +1 Ob. Riskbreaker switches: thrown dagger (range) before closing. But Ehrenwall is in melee range — no range advantage. Thrown dagger in melee: Ob +2 (range mismatch). Pool: 8D − 1 (Wound Ob) − 2 (range): effectively Ob+3 on the attack.

Expected thrown dagger: hits rarely. Better option: disengage.

**Disengagement (PP-048):**
Agility roll, Ob = Ehrenwall Cog3 (awareness). 8D TN7 Ob3: Expected net 8×0.33=2.6. P(≥3): ~55%. Coin-flip.

If success: Riskbreaker exits, takes Stamina→0 (per PP-048). Ehrenwall gets one free Priority 3 attack before exit.
Free attack: 9D TN6 Ob0 (Riskbreaker has no defence declared): ~98% hit. Damage: ~9.5 − 1 (AR): ~8.5 health damage. Riskbreaker 2nd Wound.

Riskbreaker exits at 2 Wounds, Stamina 0.

**Equipment test (M-043):**
Ehrenwall's full plate (AR 3): Riskbreaker's short sword (Damage+2) needs Str3+2+net successes > 3 (AR) to damage Ehrenwall. Riskbreaker Str3: minimum damage through plate = 3+2+0(net0)−3(AR) = 2. Only possible if Riskbreaker achieves net>0. With 1 Wound (+1 Ob): P(net>0 with 8D TN6 vs Ehrenwall 2D defence): P(≥1+2=3 net?). No — Ob isn't Ehrenwall's defence directly; in pool-split, it's net comparison. Riskbreaker attack net vs Ehrenwall defence net. Ehrenwall 2D defence: expected 2×0.45=0.9. Riskbreaker attack (8D−1Wound=effective Ob+1) net: ~3.6−1=2.6. Margin: ~1.7. Damage: 3+2+1.7−3(AR) = ~3.7. About 4 health damage through full plate.

Ehrenwall Health (End4+6=10): Takes 4. Health 10→6. Not a Wound threshold crossing (threshold at 0). Ehrenwall unimpaired.

**Manoeuvre — Disarm detailed resolution:**
When Disarm succeeds (28% chance): per PP-058 note: "Manoeuvres are suboptimal vs direct attacks in most cases — intended for scenarios where killing is not the goal." Disarm is specifically valuable when the goal is capture (not kill). Against Ehrenwall (full plate, high damage output), capture would only make sense if the Riskbreaker has backup. Confirmed: Manoeuvre mechanics work as intended — suboptimal in pure combat but narratively purposeful.

**VERDICT:** CLEAN. Full combat chain (M-041/042/043/044) resolves without cascade. Pool split handles Manoeuvre cleanly (Ob = opponent pool ÷ 2 formula works). Equipment (AR 3 plate) dramatically reduces Riskbreaker effectiveness. Disengagement is ~55% (reasonable risk). Combat produces expected outcomes.

---

## T-B10-10: THREE-CLOCK CONVERGENCE — ISOLATION OF INTERACTION RULES
### 7-Dim Tags: M-033, M-030, M-031, M-032 | TTRPG/BG/HYB | CROSS | TT,TC,IP,ThS,FSTAT | All | Multiple | Faction Leader

**Setup:** Testing M-033 (Clock Interactions) in isolation. All three clocks at critical threshold simultaneously. TT=62, TC=61, IP=58. (These values probe the documented rules for clock interaction at midpoints.)

**Known interaction rules (from compiled clock rules):**
- TT>45 → TC +1/season, IP +1/season (TT contribution to other clocks)
- TT>60 → Thread ops +1 Ob
- TC>50 → Church Domain Actions for expansion: −1 Ob (Church urgency driver)
- TC>60 → IP +1/season (additional TC-IP link at high TC)
- IP>60 → Löwenritter coup trigger review
- IP>75 → Altonian vanguard deployment

**At TT=62, TC=61, IP=58:**
- TT>60: Thread ops +1 Ob (confirmed)
- TT>45: TC +1/season from TT pressure (adds to standard TC seasonal gain)
- TC>60: IP +1/season from TC pressure
- Total seasonal IP gain: base +2 + TT contribution +1 + TC contribution +1 = **+4/season**
- Total seasonal TC gain: base +2 + TT contribution +1 (+ whatever Church Domain Actions add) = **+3/season minimum**
- TT: no direct acceleration from other clocks at this threshold. TT moves only from Thread ops and passive drift.

**Cascade rate at these levels:**
Season N: TT=62, TC=61, IP=58
Season N+1: TT≈63 (passive drift+2/BG or +1/TTRPG), TC≈64, IP≈62
Season N+2: TT≈64/65, TC≈67+, IP≈66+

At IP>60 (Season N+1): Löwenritter coup trigger review fires. Ehrenwall begins internal preparations (from succession design).
At IP>75 (Season N+4 approximately): Altonian vanguard. Campaign enters endgame.

**Acceleration confirmation:**
The three-clock system self-accelerates once all three exceed 50. This is intentional — the clocks are designed to create a convergent endgame timeline. Players have roughly 4-6 seasons from this state before IP hits 75.

**Deadlock check:** Is there any state where all three clocks can be simultaneously reduced?
- TT reduction: Overwhelming Weaving (−1), Community Weaving (−2/season), Einhir site preservation (−1/season)
- TC reduction: Grand Debate victory (−1 to −3), Baralta Sovereign Authority (−2 to −3), Church Stability suppression (brake)
- IP reduction: Crown demonstrates strength (Mandate at 5+ + alliance with Hafenmark + 2 other factions unified): IP −2/season (from succession chat: "Diplomatic Resolution requires Mandate >5, Church Mandate >5, TT <35")

**TT <35 is required for IP Diplomatic Resolution — but TT is currently 62.** The conditions for IP suppression are mutually exclusive with the current clock state. IP cannot be diplomatically reduced unless TT is first reduced to <35. TT reduction rate (maximum, all sources): −5/season (Overwhelming Weaving −1, Community Weaving −2, Einhir sites ×2 −2). At TT 62: 27 points to reduce below 35 = 5-6 seasons of maximum TT suppression WHILE simultaneously facing IP acceleration. 

**FINDING F-B10-11 (P2 — design concern):** At TT>60, the conditions for IP Diplomatic Resolution become effectively unreachable within the campaign timeline. The game transitions to a military resolution path. This may be intentional (the Rupture-approaching state should feel unwinnable through purely diplomatic means) but creates a hard binary: either TT is controlled early (before 60) or the campaign goes to military endgame. Flag for Phase 4 consolidation review.

**Threshold crossing interaction — simultaneous:**
What if TC crosses 80 and IP crosses 75 in the SAME season?
- TC 80: Church territorial seizure trigger fires (M-078)
- IP 75: Altonian vanguard deployment fires
- Both in same season: both fire. Resolution order per PP-005: Church seizure = political tier (5), Altonian deployment = military tier (4). Military resolves before political: Altonian vanguard arrives first, THEN Church attempts seizure. With Altonian vanguard in the field, Crown/Löwenritter are occupied militarily — Church seizure faces reduced counter-play.

**RULING (R-B10-04):** When TC 80 seizure and IP 75 vanguard fire in the same season, military actions (IP 75 response) resolve in tier 4, Church seizure in tier 5 — per PP-005 domain action sequence. Military engagement has priority.

**VERDICT:** CLEAN. Clock interaction rules stack additively and produce expected acceleration curves. Diplomatic Resolution locked out above TT 60 is a design concern (F-B10-11) not a mechanical error. Simultaneous threshold crossing resolved by PP-005 sequencing.

---

## T-B10-11: TRAJECTORY READING — NEW MECHANIC ISOLATION TEST (PP-081)
### 7-Dim Tags: PP-081, M-013, M-009 | TTRPG | FUT/CROSS | TT,TD,CERT,ThS | Varfell | Vaynard | Practitioner

**Note:** No current character roster has TS ≥ 70. For this test, use a hypothetical high-TS practitioner: **Elder Siv** (fictional character, TS 78, Transcendent tier) to test the mechanic in isolation. Certainty 4. TD 12.

**Stage 1 — Trajectory Reading requirements:**
TS 78 ≥ 70 ✓. Active Leap contact required first. Certainty 4 ≥ 2 ✓. Target: Thread configuration underlying Vaynard's research into Einhir artefacts (an active Thread connection between Vaynard and a specific artefact).

**Leap (prerequisite):**
Leap pool: Cog5+Foc5+Thread8 = 18D TN7 Ob1 (TS70+). Expected net: ~18×0.33=5.9. P(≥1): ~99%. Success. Certainty −1 (4→3). TD: +1 per co-movement (12→13). Contact established.

**Stage 2 — Trajectory Reading:**
Declared horizon: Medium (1 season). Ob5.
Reading pool: same as Leap pool? PP-081 doesn't specify a dedicated pool — uses standard Thread op pool.
Ruling: Trajectory Reading pool = Cog+Att+Thread History (perception-oriented attributes). Elder Siv: Cog5+Att4+Thread8 = 17D TN7 Ob5. (TN7 — Trajectory Reading is difficult but not at TN8 like Past-Oriented Pull.)

Expected net: 17×0.33=5.6. P(≥5): ~63%. P(≥10/Overwhelming): ~20%.

Most likely: **Success** (63%).

**Degrees applied:**
Success: 1 trajectory at Medium horizon (1 season lookahead). Confidence level revealed.

GM provides: "The Vaynard-artefact Thread connection is oriented toward severing. Within one season, the configuration will attempt to actualise: either Vaynard loses access to the artefact, or the artefact's Thread configuration becomes inaccessible to him through other means (external disruption, artefact degradation, or Vaynard's own TS growth making the connection unstable)."

Confidence: Medium (standard Success provides confidence level per PP-081 degree table).

**Costs:**
TD: +4 (13→17). Approaching TD cap (20). At TD 17: Pulling Ob+5 effectively. Elder Siv is deeply degraded from this operation.
Certainty: −2 (3→1). One step from Rendering Crisis. 
TT: +2 (45→47).

**Co-movement:**
Temporal: CD+2. History Resonance. Elder Siv: CD already high (not tracked in test, but significant).
Epistemic: Elder Siv's present-state perception filtered through Vaynard trajectory for 1 scene. GM introduces one perceptual ambiguity: "Did Vaynard just receive a message, or is Siv seeing the trajectory of him receiving a message?"
Actual d6: standard table.

**Failure case analysis:**
P(Failure, net<0): ~10%. On Failure: GM provides one plausible but false trajectory. Siv's Beliefs project: she might believe Vaynard will betray the Einhir cause (her fear) when in fact he won't. This is the "self-projection" mechanic: the false trajectory reflects the practitioner's psychological state, not Thread reality.

**FINDING F-B10-12 (P2):** At TD 17, Elder Siv is effectively non-functional for further Thread operations (Pulling Ob+5 = near-impossible at any useful Ob level). Trajectory Reading's TD+4 cost makes it self-limiting: a practitioner can perform at most 3-4 Trajectory Readings in a campaign arc before reaching TD cap. This is correct — the mechanic is designed as a rare, costly operation. No mechanical issue.

**FINDING F-B10-13 (P2 — pool specification):** PP-081 doesn't specify the Trajectory Reading pool. This must be defined: recommend Cog+Att+Thread History (perception/cognition attributes, same as Diagnosis) rather than the Weaving pool (Cog+Mem). Trajectory Reading is about reading Thread-state configuration, not shaping it.

**VERDICT:** CLEAN mechanically. Trajectory Reading functions. Costs are appropriately steep (TD+4, Certainty−2, TT+2). Self-projection failure mechanic is elegant. Two P2 gaps: pool specification needed (F-B10-13), TD cost self-limits the mechanic correctly (F-B10-12 — by design).

---

## T-B10-12: DOMAIN ACTIONS + FACTION STATS — MULTI-FACTION SIMULTANEOUS RESOLUTION
### 7-Dim Tags: M-035, M-034, M-038 | BG | PRES/FUT/CROSS | FSTAT,TT,TC,IP | Crown,Church,Niflhel | Almud,Himlensendt | Faction Leader,Riskbreaker

**Setup:** Season 7. Post-B10-08 state. Church Stability 3 (PP-080 brake active). Crown Mandate 5. Niflhel operating covertly (DD 4 Riskbreaker inside Church). All players place orders simultaneously.

**Crown:** Govern (Valorsplatz) → Stability +1.
**Church:** Expansion (Himmelstift) → Mandate +1.
**Niflhel:** Intel Domain Action (expose Church Riskbreaker? No — expose something about Church to another faction). Target: Crown. Pass intel on Church's Expansion plans.
**Revolution:** Weave (Sudwald). TT at 47 → Ob=47÷20=Ob3 (rounded up).

**PP-005 sequencing (tier order):**
Tier 1 (Defensive): Crown Govern = stabilisation (defensive tier? Or economic?). Govern = "Govern territory" = stabilisation of Mandate/Stability. Category: Defensive (stabilise own faction). Resolves first.
Tier 2 (Economic): None this round.
Tier 3 (Intelligence): Niflhel Intel action. Resolves third.
Tier 4 (Military): None.
Tier 5 (Political): Church Expansion = political assertion. Revolution Weave = TT reduction (not directly political but cross-tier). Category: Thread ops in BG mode = which tier? Not defined in PP-005.

**FINDING F-B10-14 (P2):** PP-005 domain action sequencing doesn't define which tier Thread operations (BG mode Weave orders) belong to. They're not defensive, economic, intelligence, or military. Recommend: Thread operations = Tier 2.5 (between Economic and Intelligence) OR Tier 5 (simultaneous with political, since Thread consequences are most unpredictable). Given P-01 (co-movement mandatory), Thread ops should resolve at a defined, consistent tier.

**RULING (R-B10-05):** Thread operations in BG mode resolve at Tier 2 (same as Economic actions). Rationale: Thread ops are resource expenditures (like economic investment) with unpredictable multiplied consequences. They resolve before intelligence and military actions so that co-movement effects are known before tactical decisions resolve.

**Applying sequencing:**

**Tier 1 — Crown Govern:**
Crown Mandate5D TN7 vs Ob=Crown Stability (4÷2+1? No — Govern Ob typically Ob2 fixed). Standard Govern Ob2: 5D TN7: P(≥2): ~82%. Success. Crown Stability +1 (4→5).

**Tier 2 — Revolution Weave:**
Influence3D TN7 Ob3 (47÷20=2.35, round up=3): P(≥3): ~35%. Partial (positive but <3).
Partial: TT unchanged. Stability check at next Accounting (R-ST-B3). Co-movement card drawn.

**Tier 3 — Niflhel Intel:**
Intel6D TN7 vs Ob= (Crown Intel? Crown has no Intel stat) → Ob = territory control difficulty? Standard Intel vs faction: Ob = target faction's Stability ÷ 2 (rounded up) = Crown Stability 5÷2=3 (now 5 after Govern = 5÷2=3).
6D TN7 Ob3: P(≥3): ~68%. Success. Niflhel passes Church Expansion plan intel to Crown. Crown player receives: "Church will attempt Expansion at Himmelstift this season." Riskbreaker DD: 4→6.

**Tier 5 — Church Expansion (Himmelstift):**
Church Mandate6D TN7 vs Ob = Crown Mandate5 ÷ 2 = Ob3 (Mandate5 at Himmelstift. Using PP-015 formula: target owner's Mandate ÷ 2, round up).
6D TN7 Ob3: P(≥3): ~68%. BUT: Crown received intel from Niflhel (Tier 3). Can Crown respond?

Per PP-005: same-tier conflicts resolved simultaneously; Crown cannot take an action this season (actions already declared). However, the intel allows Crown to prepare counter-play NEXT season. This season: Church Expansion proceeds as declared.

Church Expansion success (~68%): Church Mandate +1 in Himmelstift. Crown Mandate −1 in Himmelstift. TC +1 (seizure in major territory? No — Expansion, not TC80 seizure. TC +0 for standard Expansion at TC<80).

**Seasonal accounting (M-038):**
1. Stat changes apply: Crown Stability 5, Church Mandate +1 in Himmelstift, Revolution Stability check (from Partial Weave).
2. Revolution Stability check (R-ST-B3): 3D TN7 Ob1. P(≥1): ~70%. Expected: hold. Stability 3→3.
3. Clocks: TT 47 (no Thread op succeeded). TC: 25+3(seasonal acc)=28. IP: 58+4(B10-10 acceleration rate if TT>60—but TT=47 here; IP base +2) = 60. IP just crossed 60: Löwenritter coup trigger review.
4. Riskbreaker DD 6: exposure check Ob=6÷2=3. Niflhel rolls Riskbreaker concealment: 9D TN7 Ob3. Expected net ~3. P(≥3): ~68%. Success: cover maintained. DD 6→5 (natural decay per PP-073: no ops this season end, DD −1).

**VERDICT:** CLEAN. Multi-faction simultaneous resolution under PP-005 sequencing works. Niflhel intel reaching Crown before Church Expansion gives narrative value (counter-play next season) without disrupting same-season resolution. Riskbreaker exposure at DD6 is risky but sustainable (~68%). One P2 gap: Thread op tier assignment (F-B10-14, resolved R-B10-05).

---

## FINDINGS SUMMARY — BATCH 10

| ID | Severity | Mechanic | Description | Patch |
|----|----------|----------|-------------|-------|
| F-B10-01 | P2 | M-046, PP-068 | Thread split pool (TS÷4) accidentally equals full pool for TS 64+. Fix: split pool = Cog+Mem only (no History), TN8 | New patch needed |
| F-B10-03 | P2 | M-047 | Inquisitor TS contamination pathway confirmed as intentional. No fix needed. Narrative flag for GMs. | Design confirmation |
| F-B10-04 | P3 | M-047 | Thread Event Ob+1 applies to all participants equally — must be explicit in rules text | Text clarification |
| F-B10-05 | P3 | M-048 | Domain Echo slot consumption notification: announce which slot consumed at Cascade before Strategic Phase | Compilation note |
| F-B10-06 | Design | M-049 | Inquisitor TS contamination: practitioners see contamination Devout character cannot perceive. Confirmed intentional. | Design confirmation |
| F-B10-07 | Gap | M-019 | Past-Oriented Pull at Einhir Sites needs TS 70+ test character. Current roster max TS 66. Test deferred. | Coverage gap |
| F-B10-08 | P2 | M-055 | Same-type auto-effects from collective ops don't stack (R-B10-02 ruling). Must be explicit in PP-013 text. | Ruling to compile |
| F-B10-09 | P2 | M-056 | Niflhel Destabilisation Ob = raw Stability (too high). Fix: Ob = Stability ÷ 2 round up (R-B10-03) | New patch needed |
| F-B10-10 | P2 | M-056, M-034 | Factions without Intel stat cannot passively detect covert ops. Explicit in PP-044. | Text clarification |
| F-B10-11 | P2 | M-033 | Diplomatic IP Resolution locked out above TT 60 (TT<35 required). Hard military binary. Flag for Phase 4. | Consolidation review |
| F-B10-12 | P2 | PP-081 | Trajectory Reading TD+4 self-limits to 3-4 uses per campaign arc. By design, correct. | Design confirmation |
| F-B10-13 | P2 | PP-081 | Trajectory Reading pool not specified in PP-081. Recommend: Cog+Att+Thread History | Add to PP-081 |
| F-B10-14 | P2 | M-035 | Thread ops not assigned a tier in PP-005 BG sequencing. Fix: Tier 2 (R-B10-05) | Ruling to compile |

## RULINGS PRODUCED — BATCH 10

| ID | Ruling | Source |
|----|--------|--------|
| R-B10-01 | Low-TS Diagnosis pool (TS 10–29): Att + Foc only, no History, Ob3 | T-B10-06 |
| R-B10-02 | Same-type auto-effects from collective ops do not stack. Each type fires once. Additional participants add d6 table rolls only. | T-B10-07 |
| R-B10-03 | Niflhel Destabilisation Ob = target Stability ÷ 2 (round up), not raw Stability | T-B10-08 |
| R-B10-04 | When TC80 seizure + IP75 vanguard fire same season: military (tier 4) resolves before political (tier 5) per PP-005 | T-B10-10 |
| R-B10-05 | Thread operations in BG mode: Tier 2 in PP-005 sequencing | T-B10-12 |

## COVERAGE MATRIX UPDATES — BATCH 10

| Mechanic | Isolation | Interaction | Scenario | Edge Cases |
|----------|-----------|-------------|----------|-----------|
| M-041 (Attack/Defence) | ✓ (T-B10-09) | ✓ | ✓ | — |
| M-042 (Damage) | ✓ | ✓ (T-B10-09) | ✓ | — |
| M-043 (Equipment) | ✓ | ✓ (T-B10-09) | ✓ | — |
| M-044 (Manoeuvres) | ✓ | ✓ (T-B10-09) | ✓ | — |
| M-046 (Thread in Combat) | ✓ (T-B10-01) | ✓ | — | ✓ |
| M-047 (Thread in Social) | ✓ (T-B10-02) | ✓ | ✓ | — |
| M-048 (Scale Transitions) | ✓ (T-B10-03) | ✓ | — | — |
| M-049 (Inquisitor Ops) | ✓ (T-B10-04) | ✓ | — | — |
| M-051 (Devout Constraint) | ✓ (T-B10-05) | ✓ | — | ✓ |
| M-054 (Einhir Sites) | ✓ (T-B10-06) | ✓ | — | — |
| M-055 (Community Weaving) | ✓ (T-B10-07) | ✓ | — | — |
| M-056 (Niflhel Destabilisation) | ✓ (T-B10-08) | ✓ | — | ✓ |
| M-033 (Clock Interactions) | ✓ (T-B10-10) | ✓ | — | ✓ |
| M-035 (Domain Actions) | ✓ (T-B10-12) | ✓ | — | — |
| M-038 (Seasonal Accounting) | ✓ | ✓ (T-B10-12) | — | — |
| PP-081 (Trajectory Reading) | ✓ (T-B10-11) | — | — | — |

