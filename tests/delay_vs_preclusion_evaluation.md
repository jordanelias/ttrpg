# Arc Register — Delay vs Preclusion Evaluation

> **Date:** 2026-04-11
> **Purpose:** The v5/v6 branch simulation treated many failed rolls as creating divergent branches. This evaluation re-examines each: is the failure a delay (retry available, arc fires eventually) or a genuine preclusion (no retry, arc permanently blocked or altered)?

---

## Classification Framework

| Category | Definition | Example |
|----------|-----------|---------|
| **Pure Delay** | Failure imposes a time cost but the roll recurs. Arc fires eventually with statistical certainty. | Discovery Event (Spirit TN 7 Ob 1): each Private Collection use retriggers the check. Over 5 uses, P(at least one success) ≈ 99.97%. |
| **Costly Delay** | Failure imposes RS/Coherence/Stability costs in addition to time. The retry is available but the cost of failing accumulates and may close the window through secondary effects. | Ceiral Ritual failure: RS −8. Retry requires another preparation season. But RS is now 8 points lower — the retry may fire at a worse RS band, with higher Obs and more decay. |
| **Conditional Preclusion** | The roll itself can be retried, but the conditions enabling it may not persist. External factors can close the window permanently. | Klapp TS growth: the roll can recur on future Thread-significant object exposure. But if Klapp is killed, reassigned, or excommunicated before the next exposure, the arc is precluded by NPC removal, not by the failed roll. |
| **True Preclusion** | No retry. The roll resolves once. Failure produces a permanent state change. | Ehrenwall Medicine check (ARC-T05): one-turn window in Phase 5 of a Mass Battle. Failure = Ehrenwall dies. No retry. NPC-ARC-BRA fires permanently. |

---

## Roll-by-Roll Evaluation

### 1. Vaynard Discovery Event (Spirit TN 7 Ob 1)
**v6 classification:** "Fires eventually — failure delays 1–3 seasons."
**Evaluation:** **Pure Delay.** Correct. Each Private Collection use (once per season, Intel vs Ob 2) triggers TS +1. At TS 14+, each use triggers the Discovery Event check. Over N uses, P(no success) = 0.6^N → approaches 0. After 5 seasonal uses: P(still no Discovery Event) ≈ 7.8%.

**However:** The delay cost is not zero. Each season of delay is a season where:
- Vaynard's TK advances more slowly (no +2 TK jump from Discovery Event)
- TC acceleration from TK is delayed (TK 3 = +1, TK 4 = +2)
- ARC-S31 (Lock Distribution) is unavailable (requires TK 4)
- Other factions have more time to prepare for Varfell's intelligence programme

**Delay cost estimate:** 1–3 seasons of delayed TK/TC cascade. No permanent state change. Arcs S13, S31, T08 are deferred but never precluded. The branch simulation correctly identified this as a short divergence window.

**Correction to v6:** None needed. Delay classification was implicit but accurate.

---

### 2. Klapp TS Growth Check (Spirit TN 7 Ob 2)
**v6 classification:** "34% failure preserves Church structural integrity."
**Evaluation:** **Conditional Preclusion — but the condition is unlikely to close.**

The roll recurs. Klapp's ongoing archive work produces future exposures to Thread-significant objects. Each exposure is another check. The essentialist formation (Ob 2) persists but so does the exposure source (the archive contains originary Locks). Over 3 exposures: P(at least one success) ≈ 96%.

**Preclusion conditions:** Klapp's arc is precluded only if, before the next exposure:
- Klapp is killed (Cardinal death mechanic: TC +1, Cardinal mechanics suspended 1 season, replacement appointed)
- Klapp is reassigned away from the archive (requires Himmensendt decision — unlikely since Klapp is head of education and the archive IS his portfolio)
- The archive is destroyed or sealed (requires active player/faction action against Church infrastructure)
- Klapp voluntarily stops accessing Thread-significant objects (his SCHOLAR nature makes this unlikely — his CE accumulation is from sustained contact, not one-time events)

All preclusion conditions require deliberate intervention. Without intervention, the check recurs and fires within 1–3 seasons.

**Correction to v6:** The "34% failure preserves Church structural integrity" framing overstates the significance. Failure delays Church fracture by 1–2 seasons at most. The delay IS significant — those 1–2 seasons of intact Church Stability affect TC trajectory, Baralta suppression dynamics, and Collision A timing — but it is not a permanent branch. Reclassify as **Costly Delay** (the delay preserves TC baseline temporarily, which has real mechanical consequences for other arcs).

**The Ob 2 is still the most impactful Ob modifier:** it creates a 34% chance of 1–2 season delay on the Church's internal fracture. Without the essentialist formation (Ob 1), the delay chance drops to ~13%. The formation buys the Church an expected ~0.5 extra seasons of structural integrity. This is good design, not a permanent branch.

---

### 3. Ceiral Ritual (Lead Weaving Pool vs Ob 5)
**v6 classification:** "7% failure → endgame spiral (2–4 seasons to Rupture)."
**Evaluation:** **Costly Delay — with potentially terminal cost.**

The Ritual can be reattempted. Requirements: Ceiral Text (persistent item), Awareness 5+ (check), lead TS 60+ (persistent), 2× TS 20+ participants (persistent), preparation season (1 season cost), all in Askeheim T13 (travel/logistics).

**Retry cost:**
- 1 preparation season (minimum)
- Lead practitioner was incapacitated on failure — must recover first (1 season minimum via standard wound recovery). Total delay: 2 seasons.
- RS −8 from the failure. During the 2-season delay: RS declines further from Lock drift + Gap persistence + the Gap the failure created. Estimated RS decline during retry window: −8 (failure) −6 to −9 (2 seasons passive decline) = −14 to −17 total.
- From RS 50 starting: RS 33–36 after failure + delay. This is Fractured band (39–20) or borderline. Gaps forming spontaneously. Monstrous Incursion risk. Thread ops +1 Ob in affected territories.
- Retry Ob: still 5, but if RS has crossed into Fragile/Fractured, geographic graduation applies additional Obs in Askeheim-adjacent territories.

**Preclusion condition:** The Ritual is precluded if:
- Lead practitioner dies during incapacitation recovery (requires medical failure — possible but not default)
- RS reaches 0 before retry (2 seasons at −7 to −9/season from RS 33: RS reaches ~15–19. Not Rupture yet, but Critical. Retry at Critical is possible but +1 Ob worldwide.)
- Askeheim (T13) becomes inaccessible (requires territorial seizure by hostile faction — unlikely given location)
- A required participant is killed or incapacitated

**The endgame spiral framing in v6 was overstated.** Failure does not preclude the arc. It creates a 2-season delay with RS cost that pushes the campaign closer to Critical. The endgame spiral begins only if the delay pushes RS below 20 AND no Mending occurs during the delay. With active Mending (Edeyja at TS 75, Ob 5–6 for standard Gaps): RS decline partially offset.

**Correction to v6:** Reclassify as Costly Delay. The 7% failure is severe but recoverable. The "2–4 season countdown" fires only if the failure cascades with simultaneous Lock drift, Gap persistence, AND no Mending during the 2-season retry window. This compound probability is much lower than 7%.

---

### 4. Baralta Excommunication (Church Mandate 5d10 vs Ob 7)
**v6 classification:** "GAP-ARC-05 — mechanically impossible at game-start stats."
**Evaluation:** **Not a failed roll — it's a gated mechanic.** Correct analysis. The mechanic requires Baralta Mandate erosion to become viable. At Baralta Mandate 4: P(success) ≈ 32%. At Mandate 3: P ≈ 66%.

**However — Excommunication is itself retryable.** If Olafsson's files are complete (2 seasons building), the Excommunication can be declared any season. It consumes no unique resource. Failure: Church Mandate unchanged. This means:

At Baralta Mandate 4: P(success in 3 attempts) = 1 − (0.68)^3 ≈ 69%. Over a campaign arc (4 seasons), the Excommunication fires with high probability once the Mandate gate is cleared.

**The real preclusion condition is Baralta Mandate ≥ 5** (at game start: personal Mandate 7, faction Mandate 4). The mechanic gates on faction-level Mandate erosion, not on the roll itself.

**Correction to v6:** GAP-ARC-05 is valid but should note that the "gap" is intentional design — Excommunication of the peninsula's most legitimate secular ruler SHOULD be mechanically near-impossible at baseline. The mechanic activates as a late-campaign tool after political erosion. No structural fix needed.

---

### 5. Ehrenwall Medicine Check (Medicine Ob 2, one-turn window)
**v6 classification:** "Highest-impact roll that never retries. ~47% failure = permanent political shift."
**Evaluation:** **True Preclusion.** Correct.

One-turn window in Phase 5 of a specific Mass Battle. If failed, Ehrenwall dies. No retry. No resurrection mechanic. NPC-ARC-BRA fires permanently. Coup Counter threshold drops from 3 to 2 for the remainder of the campaign.

**This is the only True Preclusion roll in the seven tested.** Every other roll either recurs automatically (Discovery Events, TS growth checks) or can be reattempted with preparation cost (Ceiral Ritual, Excommunication). Ehrenwall's death is permanent and irreversible.

**Nuance:** The preclusion is not the Medicine check itself — it's the Mass Battle wound. Ehrenwall is only at risk of incapacitation during Mass Battle. If players keep Ehrenwall out of combat (strategic choice), the roll never fires. The True Preclusion is conditional on Ehrenwall being committed to battle. This is itself a player decision point.

**Correction to v6:** None. Analysis was accurate. Add note: the preclusion is conditional on player choice to commit Ehrenwall to battle.

---

### 6. Almud Discovery Event (Spirit TN 7 Ob 1)
**v6 classification:** "Fires eventually. Both branches produce 1-season governance pause."
**Evaluation:** **Pure Delay — but with a unique cost structure.**

Like Vaynard's Discovery Event, this fires on repeated exposure. P(success) ≈ 87–92% per attempt. Over 2 attempts: P(at least one success) ≈ 98%.

**Unique aspect:** The 1-season governance pause fires on BOTH success and failure. This means the pause is not a consequence of the roll's outcome — it is a consequence of the attempt itself. The register's ARC-T19 (Governance Pause) correctly captures this.

**The delay cost is the governance pause.** Each failed attempt costs 1 season of Crown passivity PLUS Almud's psychological processing of the failed surrender. The retry is available next season.

**Correction to v6:** None. Analysis was accurate. The "fires eventually" framing is correct. The governance pause on both branches was correctly identified as the important finding.

---

### 7. Collective Mending at RS Critical (endgame)
**v6 classification:** "Success buys 1–2 seasons. Failure accelerates by 1–2 seasons."
**Evaluation:** **Costly Delay with escalating costs.**

Mending can be reattempted. But each failed Mending:
- Costs Coherence −1 (regardless of outcome)
- Costs RS −2 (on Failure — the substrate was disturbed without repair)
- Does NOT close the Gap (persists, costing RS −4 next season)
- The practitioner's Coherence budget shrinks

The retry is available but the cost of retrying escalates: each failure makes the next attempt harder (Coherence lower → closer to crisis) and the world state worse (RS lower → closer to Rupture).

**At RS Critical (19–1):** The escalation curve is steep. A sequence of 2 Mending failures: RS −4 (failures) + −4 (Gap persists) + −1 (Winter) + −2 (Lock drift) = −11 in one season. From RS 15 → RS 4. One more season at this rate = Rupture.

**The v6 framing ("structurally insufficient without Lock/Gap elimination") was correct.** Individual Mending success or failure is less important than the structural question of whether decay sources are being eliminated. The rolls matter tactically; the strategy matters existentially.

**Correction to v6:** Reclassify from "both branches lead to same outcome" to "both branches converge IF AND ONLY IF decay sources are addressed. Without Lock resolution + Community Weaving + Warden Cooperation, success merely delays the Rupture. Failure accelerates it."

---

## Revised Arc Impact Table

| Roll | Category | Delay Length | Delay Cost | Permanent State Change? |
|------|----------|-------------|-----------|------------------------|
| Vaynard Discovery | Pure Delay | 1–3 seasons | TK/TC cascade deferred | No |
| Klapp TS Growth | Costly Delay | 1–2 seasons | TC baseline preserved temporarily; Church fracture deferred; Collision A timing shifted | No — fires within 1–3 exposures |
| Ceiral Ritual | Costly Delay | 2 seasons (recovery + prep) | RS −8 + 2 seasons passive decline (−14 to −17 total). Compounds toward Critical but recoverable with Mending. | No — retryable. Endgame spiral only if compounded with no Mending. |
| Excommunication | Gated Mechanic | N/A (gate is Mandate erosion, not roll failure) | N/A | Gate is structural, not roll-based |
| Ehrenwall Medicine | **True Preclusion** | **Permanent** | **Coup threshold 3 → 2. Brandt succession. Military redirect. Collision F dynamics shift.** | **Yes — only True Preclusion in the set** |
| Almud Discovery | Pure Delay | 1 season | Governance pause (fires on both branches) | No |
| Endgame Mending | Costly Delay (escalating) | 1 season per failure | RS −2 + Coherence −1 + Gap persistence (−4/season). Escalates toward Rupture if repeated. | No — but escalating costs can produce de facto preclusion if RS reaches 0 |

---

## Implications for Arc Register

### Arcs reclassified:

**ARC-S13 (Duke Awakens):** Not "fires on Discovery Event success." Fires eventually through repeated Private Collection use. Classification: Pure Delay on failure. The arc is inevitable given continued Vaynard play. Timing varies 1–3 seasons.

**ARC-S08 (Faith that Destroys):** Not "fires on Klapp TS growth success." Fires eventually through repeated archive exposure. Classification: Costly Delay — each delay season preserves TC baseline. The essentialist Ob 2 creates a meaningful delay probability (34%) that buys the Church 1–2 seasons of structural integrity per check.

**ARC-S15 (Southernmost Spiral) / ARC-T04 (Ceiral Ritual):** Failure does not preclude the arc. Failure imposes RS cost and 2-season retry delay. The endgame spiral fires only if the delay compounds with no Mending and simultaneous Lock/Gap decay. Reclassify Collision C from "fires on Ceiral failure" to "fires on Ceiral failure IF Torben Loyalty ≤ 3 at the same time AND no Mending during 2-season delay."

**ARC-T05 (General Falls):** Correctly classified as True Preclusion. The only genuinely permanent roll outcome in the arc register. Conditional on player choice to commit Ehrenwall to battle.

**ARC-S34 (Edeyja Burnout):** Reframe. Edeyja's burnout is not a single-roll event — it is a Coherence budget over multiple seasons. Each Mending is a Costly Delay decision (spend Coherence now for RS recovery, or preserve Coherence for future Mendings). The "hidden fail state" framing is correct but the mechanism is cumulative decision-making, not a single roll.

**ARC-S32 (Mending Trap):** The trap is structural, not roll-dependent. Individual Mending rolls matter tactically (success = RS +1, failure = RS −2) but the trap is that even perfect Mending rolls cannot sustain RS indefinitely because Coherence is finite. Reframe from "roll consequence" to "resource exhaustion."

### New structural insight: Cost-of-delay as arc driver

Failed rolls that are Pure Delays impose no lasting cost. Failed rolls that are Costly Delays impose RS/Coherence/Stability costs that affect OTHER arcs' timing. The most important Costly Delay is the Ceiral Ritual: its failure cost (RS −8 + 2-season delay at −7/season) advances the RS timeline by ~3–4 seasons of passive decline. This doesn't preclude the Ritual — it advances every RS-dependent arc (ARC-P02, ARC-S05 Temporal Window, ARC-S15 Southernmost Spiral, ARC-S32 Mending Trap, ARC-S34 Edeyja Burnout) by 3–4 seasons simultaneously.

The arc register should capture this: failed Costly Delay rolls don't create new arcs. They accelerate existing arcs. The TC clock, RS clock, and IP clock don't branch on failed rolls — they accelerate.

---

## Corrections to Apply

1. **Branch simulation summary table:** Replace "Arcs Unlocked" column with "Delay Category" and "Delay Cost" columns.
2. **ARC-S08, ARC-S13:** Add note: "fires eventually through repeated checks. Failure = Costly Delay / Pure Delay, not preclusion."
3. **ARC-T04:** Add note: "retryable with 2-season delay + RS −8 cost. Endgame spiral only on compound failure (no Mending during delay)."
4. **ARC-T05:** Add note: "True Preclusion — conditional on player choice to commit Ehrenwall to battle. Only permanent roll outcome in register."
5. **GAP-ARC-05:** Add note: "Excommunication gate is intentional design — the mechanic activates after political erosion, not at baseline."
6. **ARC-S32, ARC-S34:** Reframe from roll-consequence arcs to resource-exhaustion arcs. The trap/burnout is cumulative, not single-event.
