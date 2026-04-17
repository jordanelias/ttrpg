# VALORIA — Rendering Stability Budget
## Date: 2026-04-17
## Status: WORKING DESIGN — P0 rulings pending (flagged inline)
## Scope: Single authoritative document for all RS drain and restoration sources across all modes.
## [EDITORIAL: ED-629 — Thread stress test identified this document as missing. Six independent RS drain sources across six documents, never aggregated.]
## Cross-references: threadwork_v30.md §5.2, victory_v30.md §0.4, params_board_game.md §Accounting, peninsular_strain_v1.md §3, calamity_radiation_v30.md, tests/thread_stress/threadwork_audit_register.md §F

---

## §1 — Starting Values

| Mode | Starting RS | Source |
|------|-------------|--------|
| BG-only | 72 | params_board_game.md Starting Values |
| TTRPG-only | 72 | P-32, threadwork_v30 |
| Hybrid (start as BG) | 72 | Inherits from BG starting state |
| Hybrid (start as TTRPG) | 72 | P-32 |
| Hybrid (pure start) | 66 | P1-15 ruling: midpoint |

RS runs 100→0. Rupture at RS 0 = shared loss (all factions lose).

---

## §2 — Drain Sources

### §2.1 Persistent Drains (per-season at Accounting)

| Source | RS/Season | Mode | Canonical Source | Notes |
|--------|-----------|------|------------------|-------|
| Gap persistence | −4 each | ALL | threadwork_v30 §5.2 | Per active Gap at Accounting. Micro-Gaps close same scene (−1 if persisting to Accounting). |
| Lock chronic drift (slow-change, seasons 2–3) | −1 each | ALL | threadwork_v30 §3.3, R-63 | Slow-change domains: seasonal/yearly evolution. |
| Lock chronic drift (slow-change, 4+ seasons) | −2 each | ALL | threadwork_v30 §3.3 | Permanent Lock: drift ceases (substrate adapts). |
| Lock chronic drift (fast-change domain) | [PENDING RULING: P0-08] | ALL | — | Fast/standard/inert rates undefined. Every Lock RS calculation contains a hidden undefined variable. |
| Siege drain | −1 per province | ALL | threadwork_v30 §5.2, peninsular_strain_v1 §3 | Concentrated suffering. +1 additional if Einhir site under stress. [PENDING RULING: P0-04 — per-province or per-settlement? If per-settlement, Ehrenfeld (3 settlements) = 3× drain.] |
| Battle drain | −1 per battle on Valorian soil | ALL | victory_v30 §0.4 | Campaign/War scale: −2 per battle. **Was missing from all prior RS budgets.** |
| Winter annual drift | −1/year (−0.25/season) | ALL | threadwork_v30 §5.2 | Applied at Winter Accounting (every 4th season). |
| Thread Debt tokens | −1 per token (>1 season old) | BG/Hybrid | params_board_game.md §Accounting Step 6 | Serviced tokens: no drain, but permanent residual RS −0.5 recorded. |
| Peninsular Strain 9–10 (Collapse) | −1 additional | BG/Hybrid | peninsular_strain_v1 §3 | Non-capital territories: Accord cap 2, Mandate check Ob 3. |
| TS 90+ at Coherence 0 | −1 per scene of existence | TTRPG/Hybrid | P1-11 (audit register) | Resonant practitioner Rendering Crisis = campaign-level RS emergency. Fastest single-source drain: −30 RS/year. |
| Structural Lock persistence | −1 additional/season | ALL | threadwork_v30 §3.3 | Structural Lock obstructs substrate traffic; stacks with base Lock chronic drift. |

### §2.2 Event-Based Drains (per occurrence)

| Source | RS Cost | Mode | Canonical Source |
|--------|---------|------|------------------|
| Weaving/Pulling — Partial | −1 | ALL | threadwork_v30 degree table |
| Weaving/Pulling — Failure | −2 | ALL | threadwork_v30 degree table |
| Lock — Success | −1 | ALL | threadwork_v30 §3.3 |
| Lock — Partial | −2 | ALL | threadwork_v30 §3.3 |
| Lock — Failure | −3 | ALL | threadwork_v30 §3.3 |
| Dissolution — Overwhelming | −3 | ALL | threadwork_v30 §3.3 |
| Dissolution — Partial | −6 | ALL | threadwork_v30 §3.3 |
| Dissolution — Failure | −8 | ALL | threadwork_v30 §3.3 |
| Past-Oriented Pulling | −3 minimum | ALL | threadwork_v30 §2.8 |
| Overweaving collapse | −3 | ALL | threadwork_v30 §2.4 |
| Mending — Failure | −2 | ALL | threadwork_v30 §3.3 |
| Mass battle Thread ×3 multiplier | ×3 all costs | TTRPG/Hybrid | threadwork_v30, ST-TW-03 |
| Opposing ops lattice collapse (3+) | Gap at target scale | TTRPG/Hybrid | threadwork_v30 §3.1 |
| BG Weave order — Failure | −1 | BG/Hybrid | threadwork_v30 §7.1 |
| Anomaly POI discovery | −1 | BG/Hybrid | fieldwork_v30 §8.1 |

---

## §3 — Restoration Sources

| Source | RS Gain | Mode | Canonical Source | Notes |
|--------|---------|------|------------------|-------|
| Mending — Overwhelming | +2 | ALL | threadwork_v30 Mending degree table | Multiple Mendings stack at Accounting. |
| Mending — Success | +1 | ALL | threadwork_v30 Mending degree table | |
| Weaving — Overwhelming (Relational+) | +1 | ALL | threadwork_v30 §2.4 degree table | Only Relational scale or above. |
| Community Weaving (RM) | +1 to +2 | ALL | threadwork_v30 §5.2 | Revolution success. |
| Southernmost expedition Mending | +2 permanent/season | ALL | threadwork_v30 §5.2 | Per successful expedition season. |
| BG Mend order — Success | +1 | BG/Hybrid | threadwork_v30 §7.1 | |
| BG Weave order — Success | +1 | BG/Hybrid | threadwork_v30 §7.1 | |
| Mass battle Mending ×3 | ×3 restoration | TTRPG/Hybrid | threadwork_v30, ST-TW-03 | Overwhelming = RS +6. |
| Lock release (Pulling) | +1/season persisted (max +5) | ALL | threadwork_v30 §3.3 | Clean Pulling only, not Dissolution. |
| WC 3 Edeyja Mending | +2/season | ALL | victory_v30 §6 | Requires Warden Cooperation ≥ 3. |
| Ceiral Ritual — Failure | +8 | ALL | threadwork_v30 | [PENDING RULING: P0-14 — confirm intentional or typo.] |
| BG RS stabilisation co-movement card | +1 at next Accounting | BG/Hybrid | params_board_game.md Co-Movement table | |

---

## §4 — WC Modifiers (Warden Cooperation Track)

| WC | Effect on RS Budget | Source |
|----|---------------------|--------|
| 0 | No modifier. All drain at full rate. | default |
| 1 | +1D Thread ops peninsula-wide. No direct RS effect. | victory_v30 §6 |
| 2 | **Gap and Lock RS drain halved.** Gap: −4→−2 each. Lock (slow): −1→−0.5 each. | victory_v30 §6, P0-07 |
| 3 | As WC 2, plus **RS +2/season** at Accounting (Edeyja Mending). | victory_v30 §6 |

[PENDING RULING: P0-07 — Confirm WC 2 halves Gap/Lock drain specifically.]

---

## §5 — Peak Drain Scenarios

### §5.1 Peak Military Period (Year 20–25, 30-year campaign)

| Source | WC 0 | WC 2 | WC 3 |
|--------|------|------|------|
| Gap persistence (3 active) | −12 | −6 | −6 |
| Lock chronic drift (2 active, 4+ seasons) | −4 | −2 | −2 |
| Siege drain (3 provinces) | −3 | −3 | −3 |
| Battle drain (2 Campaign-scale/season) | −4 | −4 | −4 |
| Winter baseline | −0.25 | −0.25 | −0.25 |
| **Total drain** | **−23.25** | **−15.25** | **−15.25** |
| WC 3 Edeyja Mending | — | — | +2 |
| **Net drain** | **−23.25** | **−15.25** | **−13.25** |

### §5.2 Time to Rupture (from RS 45)

| WC | Seasons to RS 0 | Survivable without mass Mending? |
|----|-----------------|----------------------------------|
| 0 | 1.9 | No |
| 2 | 2.9 | No (buys ~1 season) |
| 3 (no Mending) | 3.4 | No |
| 3 + 3 Overwhelming Mendings/season | Net +4.75/season | **Yes — only viable path** |

### §5.3 Design Implication

WC 3 + concentrated mass battle Mending is the singular viable endgame RS survival strategy. Three successful mass battle Mendings per season at WC 3: each Overwhelming = RS +6 (×3 multiplier). Total +18/season vs −13.25 drain = net +4.75/season recovery.

If the singular survival path is intentional design, it should be stated as a design axiom: the survival contest demands cross-faction cooperation toward the Wardens regardless of political outcome. If WC 3 is meant to be one of several viable paths, the RS budget needs rebalancing.

---

## §6 — Unresolved P0 Dependencies

| P0 | Variable | Impact |
|----|----------|--------|
| P0-04 | Per-province vs per-settlement siege drain | Per-settlement: Ehrenfeld = −3 not −1. Peak drain +6. |
| P0-07 | WC as variable in all calculations | Incorporated in §5. Confirm WC 2 halves Gap/Lock. |
| P0-08 | Fast-change Lock domain drift rates | If fast-change = −2/season: peak Lock drain doubles. |
| P0-14 | Ceiral Ritual Failure = RS +8 | If intentional: high-risk restoration path. If typo: remove. |
| P0-15 | Altonian Thread practitioners | If yes: all drain estimates are underestimates. |

---

## §7 — Mode-Specific Accounting

### §7.1 BG Accounting
RS changes at Phase 5 Accounting. Order: Thread Debt tokens (Step 6) → RS track update → threshold checks.

### §7.2 TTRPG Accounting
Event-based RS costs apply immediately on operation resolution. Persistent drains (Gaps, Locks, siege) at season end.

### §7.3 Hybrid Accounting
Personal Phase (immediate) + Strategic Phase (Cascade Phase Accounting) unified at Accounting. Seasonal cap: ±10 net RS.

---

*This document is the single authoritative RS budget. All RS drain and restoration values in other documents should be consistent with this document. Discrepancies: file editorial item referencing this document.*
