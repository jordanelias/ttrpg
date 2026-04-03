# SIM-X-17: P-22 Paradox Window
## Date: 2026-04-02 | Modes: A (Isolation) + D (Edge Cases)
## Mechanic: Past-Oriented Pulling + actual d6=6 → paradox window (PP-193)
## Source: params_threadwork.md, PP-193

### 7-Dimension Tag
- Mechanics: POP, Mending, paradox window (PP-193)
- Mode: TTRPG
- Temporal: PAST
- Tracks: Coherence, RS, Temporal Disjunction
- Factions: None
- NPCs: Generic TS70 practitioner, Generic TS30+ opponent
- Archetypes: Veteran practitioner, adversary

---

## MODE A — ISOLATION

### Trigger Rate
- P(actual d6=6 on any POP) = 1/6 = 16.7%
- Expected windows per 10 POPs: 1.7

### Auto-Resolution (dominant when no TS30+ opponent present)
- E[window] = 2 scenes. No roll, no cost.
- Risk: exploitation window for TS30+ observers.

### Early Closure: Mending Ob3, pool 12D TN7 (Att4+Focus3+TPS5)
- P(Overwhelming / immediate closure): 25.8%
- P(Success / immediate closure):      38.9%
- P(Partial / duration halved):        20.9%
- P(Failure / persists + RS-2):        14.4%
- **P(closure on attempt): 85.6%**. Early closure reliable at standard pool.
- Failure rate 14.4% adds RS-2 — meaningful at RS<20, acceptable otherwise.

### Exploitation by Opponent (TS30+, +2 Ob)
- Weaving base Ob2 +2 = Ob4, pool 8D TN7:
  - P(Overwhelming+Success): 32.2% | P(Partial): 46.5% | P(Failure/window collapses): 21.3%
- **FINDING:** Exploitation has ~32% success rate. Real tactical option, not dominant.
  Failure penalty (op Failure consequences + window collapses) creates symmetric risk.

---

## MODE D — EDGE CASES

- **D1 (PASS):** Focus 1 practitioners ineligible for POP (0 op rounds). No paradox window possible. Gate correct.
- **D2 (PASS):** Window end coinciding with scene end: auto-resolves cleanly at scene transition.
- **D3 (GAP):** Sequential POPs on same thread within paradox window — no ruling. Recommend: second POP auto-fails (thread in indeterminate state).
- **D4 (PASS):** Practitioner Rendering Crisis during window — auto-resolution fires independently. No deadlock.
- **D5 (PASS):** Auto-resolution is correctly context-dependent (not degenerate). Opponent presence determines optimal strategy.

---

## FINDINGS
| ID | Sev | Finding |
|----|-----|---------|
| SIM-17-01 | P3 | Sequential POPs on same paradoxed thread — no ruling. Recommend: auto-fail second POP. |

## STATUS: COMPLETE
