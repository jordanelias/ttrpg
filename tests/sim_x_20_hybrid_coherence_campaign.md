# SIM-X-20: Hybrid Coherence — 10-Session Campaign
## Date: 2026-04-02 | Modes: A (Isolation) + B (Interaction Chain) + D (Edge Cases)
## Mechanic: PP-198 Hybrid Coherence declaration rule; PP-196 FR surcharge
## Source: params_threadwork.md, PP-196, PP-198

### 7-Dimension Tag
- Mechanics: Hybrid Strategic Phase Coherence, FR surcharge, Personal Phase Coherence, recovery
- Mode: Hybrid
- Temporal: CROSS (10-session campaign)
- Tracks: Coherence, Thread Sensitivity
- Factions: All (generic Hybrid campaign)
- NPCs: 2 PC practitioners (A and B)
- Archetypes: Hybrid practitioner-strategist

---

## MODE A — ISOLATION: Calibration Scenarios

| Scenario | Personal cost/session | Strategic cost/session | Total | Fragmented by | Crisis by |
|----------|----------------------|----------------------|-------|--------------|-----------|
| Conservative (1 Personal, every-other Strategic) | 1.0 | 0.6 | 1.6 | S6 | S14 |
| **Moderate (1 Personal + 1 Strategic, 30% FR)** | 1.0 | 1.3 | 2.3 | **S5** | **S10** |
| Aggressive (2 Personal + 2 Strategic, 40% FR) | 2.0 | 2.8 | 4.8 | S3 | S5 |

**Design confirmation:** Moderate scenario (the intended play pattern) produces Rendering Crisis near session 10 — consistent with campaign-end arc. Mechanic is correctly calibrated. No patch needed.

**Initial simulation error:** Original SIM-X-20 modeled Aggressive scenario by accident. Corrected above.

---

## MODE B — INTERACTION CHAIN

- **Recovery mutual exclusion:** A PC who declares leadership in a season cannot take a non-practice recovery season that season. Leadership and recovery are mutually exclusive. Correct design incentive.
- **FR surcharge (PP-196):** FR leadership costs -2 vs -1 for standard. 3 consecutive FR orders = Fragmented in 4 ops vs 10 ops before PP-196. FR leadership now meaningfully costly. Correct.
- **Personal Phase baseline:** 2 Relational ops/session alone would cause Rendering Crisis by session 5 — consistent with non-Hybrid TTRPG pacing.
- **Rotation strategy:** 2 PCs alternating leadership, both still reach Fractured by session 10. Rotation extends range but doesn't prevent late-campaign degradation. Correct.

---

## MODE D — EDGE CASES

- **D1 (PASS):** No-declaration produces NPC-led orders. Clean strategic tradeoff. No deadlock.
- **D2 (GAP):** Simultaneous co-declaration — no tie-break specified. Recommend: highest TS declares; on tie, first declared at table.
- **D3 (PASS):** Severed PC as leader gains +2 Ob on Strategic Phase order roll. Coherence penalties propagate correctly.
- **D4 (PASS):** ×3 RS (PP-192) does not interact with Coherence. Systems correctly separated.
- **D5 (PASS):** Rotation is the intended optimal strategy. Outcome still produces late-campaign degradation. Correct.

---

## FINDINGS
| ID | Sev | Finding |
|----|-----|---------|
| SIM-20-01 | P2 | Simultaneous co-declaration tie-break unspecified. Recommend: highest TS declares; tie = first declared at table. [EDITORIAL ED-107] |
| SIM-20-02 | P3 | GM guidance needed: Hybrid Coherence design intent requires ~1 Personal Relational op + 1 Strategic declaration per session. Add to §7.2. |

## STATUS: COMPLETE
