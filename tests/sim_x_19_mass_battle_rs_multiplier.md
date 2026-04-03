# SIM-X-19: Mass Battle ×3 RS Multiplier
## Date: 2026-04-02 | Modes: A (Isolation) + B (Interaction Chain) + D (Edge Cases)
## Mechanic: PP-192 — all RS costs from mass battle Thread ops ×3
## Source: params_mass_combat.md, params_threadwork.md, PP-192

### 7-Dimension Tag
- Mechanics: Mass combat Thread ops, RS degradation table, ×3 multiplier
- Mode: TTRPG + Hybrid
- Temporal: PRES (battle turns)
- Tracks: RS, Coherence
- Factions: Generic (attacker/defender)
- NPCs: Generic TS70 practitioner
- Archetypes: Combat practitioner, battlefield commander

---

## MODE A — ISOLATION: RS Cost Table (×3)

| Operation | Normal RS | ×3 RS |
|-----------|-----------|-------|
| Weaving Success (Relational+) | 0 | 0 |
| Weaving Overwhelming | +1 | +3 |
| Pulling Failure | -2 | -6 |
| Locking Success | -1 | -3 |
| Locking Failure | -3 | -9 |
| Dissolution Overwhelming | -3 | -9 |
| Dissolution Success | -5 | -15 |
| Dissolution Partial | -6 | -18 |
| **Dissolution Failure** | **-8** | **-24** |
| Mending Success | +1 | +3 |
| Mending Overwhelming | +2 | +6 |
| Mending Failure | -2 | -6 |
| POP Success (min) | -3 | -9 |

### Dissolution Probability at TS70 (Spirit4+History5=9D, Ob5, TN7)
- P(Owh/-9RS): 0.4% | P(Suc/-15RS): 23.5% | P(Par/-18RS): 57.0% | P(Fail/-24RS): 19.2%
- **E[RS per Dissolution attempt]: -18.4**
- **FINDING:** Dissolution at mass battle is viable only when the battle outcome justifies ~18 RS cost. Expected.

### Mending Probability at TS70 (Att4+Focus3+TPS7=14D, Ob5 standard Gap, ×3)
- E[RS per Mending attempt]: +0.8
- **FINDING:** Mending is barely RS-positive at mass scale on average. Worth doing but not a strong recovery tool mid-battle.

---

## MODE B — INTERACTION CHAIN: 5-Turn Battle (3 Dissolution + 2 Mending)

| Metric | Value |
|--------|-------|
| Starting RS | 60 |
| E[RS from 3 Dissolution] | -55.2 |
| E[RS from 2 Mending] | +1.6 |
| E[Net RS] | -53.6 |
| E[RS after battle] | 6.4 (CRITICAL band) |
| Worst case | -84 RS (RUPTURE) |
| Best case | -15 RS → RS 45 |

**CRITICAL FINDING:** 3 Dissolution attempts in a single mass battle is functionally campaign-ending at RS 60 start. Expected RS result is Critical band (RS <10). This is the Einhir Catastrophe replicated in a single engagement. Dissolution at mass scale should be treated as a campaign-altering decision, not a tactical one.

---

## MODE D — EDGE CASES

- **D1 (INTENTIONAL):** RS <24 before battle + Dissolution Failure = Rupture risk in single action. Correct and by design. GMs must communicate this threshold.
- **D2 (PASS):** Seasonal cap provides no protection against mid-battle spikes. Correct per §5.3.
- **D3 (PASS — DESIGN GUIDANCE):** Safe ops: Weaving (E≈0 to +9), Mending (E≈+1). Risky: Lock/Pull. Dangerous: Dissolution. Correct incentive gradient.
- **D4 (PASS):** Coherence unaffected by ×3 (PP-192 correct). 5 ops → Coherence 5 (Dissonant). Not catastrophic. Systems correctly separated.

---

## FINDINGS
| ID | Sev | Finding |
|----|-----|---------|
| SIM-19-01 | P1 | 3 Dissolution attempts in one mass battle = E[RS after] = 6 (Critical). GMs need explicit guidance that mass-scale Dissolution is a campaign-altering decision. Add warning to §A.10 / mass battle Thread Integration section. |
| SIM-19-02 | P3 | RS <24 before battle = single Dissolution Failure triggers Rupture. Recommend: add explicit note to mass battle params: "If RS <24, Dissolution Failure = Rupture." |

## STATUS: COMPLETE
