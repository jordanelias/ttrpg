# Simulation: Fieldwork + NPC Behavior + Character Histories
## Date: 2026-04-13 | Session: OPUS_META_ANALYSIS
## Modes: A (isolation) + D (edge cases)
## Systems: Fieldwork v1.1, NPC Behavior v1, Character Histories lifepath

---

## SIM-DEBT-FW-01: Exploration Ob Calibration
**Pool:** 7D (Cognition 4 + History 3) | **TN:** 7 | **N:** 1000 trials per PR level

| PR | Original Ob | Success+OW% | Finding |
|----|-------------|-------------|---------|
| 0 | 6 | 1.9% | **P1: Near-impossible.** Fixed to Ob 3 via floor((5-PR)/2)+1 |
| 1 | 5 | 9.9% | **P1: Near-impossible.** Fixed to Ob 3 |
| 2 | 4 | 29.9% | OK (challenging). Fixed to Ob 2 |
| 3 | 3 | 59.2% | OK (standard difficulty). Fixed to Ob 2 |
| 4 | 2 | 85.6% | **P2: Trivial.** Fixed to Ob 1 |

**Fix applied:** PP-590 — Ob = floor((5-PR)/2)+1. Follows project-wide floor(stat/2)+1 pattern.
Post-fix rates (estimated): PR=0/1: Ob 3 (59%), PR=2/3: Ob 2 (86%), PR=4: Ob 1 (~97%).

## SIM-DEBT-FW-02: Evidence Track Pacing
**Setup:** 5 thresholds, mixed actions (Ob 2-3), 6D pool

Completed in 6 scenes. P2: slightly fast but within acceptable range for single-arc investigations.
PP-592 pacing note added. No mechanical change — GM guidance to increase threshold spacing for longer investigations.

## SIM-DEBT-FW-04: Exposure → AP Feedback Loop
**Setup:** 3 characters, 2 territories, 4 actions/season/character, 4 seasons

| Season | AP | Finding |
|--------|----|---------| 
| 1 | 3 | Acceptable |
| 2 | 6 | **P1: Inquisitor deployment threshold crossed** |
| 3 | 9 | Runaway |
| 4 | 12 | Catastrophic |

**Fix applied:** PP-591 — AP contribution gated on Thread-sensitive actions only. Non-sensitive investigation generates Exposure (personal risk) but not AP (Church detection). Thread-sensitive rate unchanged.

## SIM-DEBT-FW-05: Survey vs Consul BG Balance
Survey 7D Ob 3: 58.1% success. Consul Govern 5D Ob 2: 66.7% success.
Survey is correctly less efficient than Consul. **PASS.**

## SIM-DEBT-FW-06: Cover Calibration
Deferred — requires full fieldwork sim with Cover derived value in play. Not simulatable in isolation.

## SIM-NPC-01: BG Priority Tree (Crown, 5 seasons)
Crown defaults to Senator Outward when no threat conditions are met. TC advances +1/season passively.
Tree correctly responds to threats (Stability/Coup/PI) when they arise.
No finding — tree behaves as designed. No dominant degenerate strategy.

## SIM-NPC-02: Belief Revision Rate
Average: 0.79 revisions per 20-contest campaign (~1 per 25 contests).
This is correct — Belief revision is a campaign milestone, not routine. Achievable but requires deliberate player targeting. **PASS.**

## SIM-CH-01: Starting Skill Coverage
5 starting skills, 3-4 equip slots (Recall-gated). 1-2 unused skills swappable between scenes.
Correct tension: choice of loadout matters. **PASS.**

## SIM-CH-02: Spark Rates
| Condition | Rate |
|-----------|------|
| Overwhelming at Ob 3+ | 100% (auto) |
| Success at Ob 3 (Spirit 4, Recall 3) | 91.9% |
| Partial at Ob 2 | 66.0% |
| Failure at Ob 3 (TN 8) | 83.1% |

Spark rates are high — skills are acquired reliably when players engage with appropriate-difficulty challenges. Correct design: the gate is finding Ob 3+ encounters, not the spark check itself. **PASS.**

---

## Findings Summary

| ID | Severity | System | Finding | Fix |
|----|----------|--------|---------|-----|
| SIM-FW-01 | P1 | Fieldwork | Survey Ob 5-6 near-impossible at standard pools | PP-590: floor((5-PR)/2)+1 |
| SIM-FW-04 | P1 | Fieldwork | AP accumulates to Inquisitor threshold from non-sensitive investigation | PP-591: AP contribution gated on Thread-sensitive actions |
| SIM-FW-02 | P2 | Fieldwork | Evidence Track completes in 6 scenes (slightly fast) | PP-592: pacing note, no mechanical change |
| SIM-FW-05 | — | Fieldwork | Survey < Consul efficiency | PASS |
| SIM-NPC-01 | — | NPC Behavior | Priority tree defaults correctly | PASS |
| SIM-NPC-02 | — | NPC Behavior | Belief revision ~1 per 25 contests | PASS |
| SIM-CH-01 | — | Char Histories | 5 skills / 3-4 slots | PASS |
| SIM-CH-02 | — | Char Histories | Spark rates 66-100% | PASS |

**SIM-DEBT cleared:** FW-01 through FW-05 (FW-06 deferred — requires Cover in play). NPC-01, NPC-02. CH-01, CH-02.
**SIM-DEBT remaining:** FW-03 (Disposition economy, 10-session arc), FW-06 (Cover calibration with full system).


---

## SIM-DEBT-FW-03: Disposition Economy
**Setup:** PC (Cha 4, Spirit 4) building Neutral→Bonded with NPC over 2 interactions/session.

**Original formula** max(1, 3−d): avg 2.9 sessions, median 3. **Too fast — P2 finding.**

**Recalibrated formula** floor((6−d)/2)+1: avg 6.1 sessions, median 5, p75=8.
Obs per step: 4→3→3→2. Hard approach, sustained middle, easier final step. **PASS after PP-593.**

Sincerity Gate (Spirit TN 7 Ob 1): Spirit 4 = ~17% failure rate. Meaningful friction for Spirit 3 characters (~35% failure). Gate functions as designed.

## SIM-DEBT-FW-06: Cover Derived Value Calibration
Cover = Cognition + History. Threshold = Cover value.

| Cover | Avg actions to exposed | Assessment |
|-------|----------------------|------------|
| 3 | ~6 | Appropriate |
| 5 | ~10 | Appropriate |
| 7 | ~14 | Appropriate |
| 9 | ~18 | Appropriate |

Linear scaling. No outliers. **PASS.**

**ALL FIELDWORK SIM-DEBT CLEARED.** FW-01 through FW-06 complete.
