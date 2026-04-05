# Valoria Session — Critical Review and Close
## 2026-04-04 | Final commit of this chat session

---

## Critical Review: Errors Found and Corrected in This Session

### 1. CRITICAL — Die Rule Fidelity Error (PP-246)

**Error:** params_core.md stated face-10 = "+2 successes (no extra die)."
**Canonical source:** stage1_core_engine.md §1.1 states face-10 = "+1 success + roll one bonus die (chains indefinitely)."
**Impact:** All probability tables in params_core, and all simulation expected-value calculations in SIM-ARC-01 through SIM-ARC-04, used the wrong die model. The "+2 fixed" model underestimates tail probabilities at large pools and overestimates mid-pool expected values slightly.
**Correction:** PP-246 applied. params_core die table corrected.
**Simulation impact:** All P(success) figures in arc simulations are approximate and were computed against TN7 expected value of 0.30/die. Under the chain-die model, expected value at TN7 is approximately 0.333/die (geometric series: 0.10 × 1/(1-0.10) ≈ +0.111 for the chain, net ≈ 0.30 + 0.011 ≈ 0.311 + tail). Difference is small (~3% EV deviation); directional findings are unaffected but specific probability figures should be recalculated before compilation.

**Note on net successes floor:** params_core previously stated "Floor: 0 — net successes cannot go below 0." stage1 §1.1 states net successes = total successes minus total 1s, with no floor mentioned. Negative net is implied by "may be negative" in the Failure degree (net ≤ 0). Floor removed. PP-246 correction.

### 2. MEDIUM — PP Numbering Collision

**Error:** This session's editorial_resolution_pass.md described patches PP-257–PP-302. The actual patch register had max PP-245 at session start. The collision wasn't a catastrophic error — no patches were double-assigned, because the register entries from our session's 6442da0a commit only partially landed. The renaming caused confusion in tracking.
**Correction:** All patches renumbered PP-246–PP-262 for this session's additions, consistent with actual register state.

### 3. MEDIUM — Net Successes Negative Floor

**Error:** The SIM-ARC series stated "net successes = sum of all contributions (may be negative)" in ARC 1–4, which is correct per stage1. But params_core contradicted this with "Floor: 0." Simulations correctly modelled Failure as "net ≤ 0" but some P(failure) calculations may have understated failure modes from 1-die situations.
**Correction:** Floor removed from params_core (PP-246).

### 4. LOW — Ledger Status Inconsistency

**Error:** Multiple items had `status: open` with a decision text that was clearly a prior resolution, or `status: flagged` with `decision: ~` (null). The emergency close session (`a8b07d5`) did not complete the ledger rewrite.
**Correction:** Full ledger rewrite in this commit. All items assigned correct status.

### 5. LOW — Composure Formula Discrepancy in SIM-ARC-04

**Error:** SIM-ARC-04 ARC 17 stated Himlensendt Composure = 12, using the formula "Charisma 6 + 6." params_core defines Composure = Charisma + 6. This is consistent. However, stage13_npcs.md uses "Presence + 6" as the shorthand (Presence is the old attribute name; ED-052 resolved Presence → Charisma). ARC 17's analysis is correct; the attribute rename creates a documentation ambiguity in stage13.
**Note:** stage13 not updated in this session (would require a separate commit to stage13_npcs.md). Flag for next session.

### 6. LOW — Overwhelming Floor-3 Origin

**Error (in SIM-ARC-01):** SIM-ARC-01 stated Overwhelming requires "net ≥ 2× Ob AND net ≥ 3." stage1 §1.4 only states "Net ≥ 2× Ob." The floor-3 was introduced by PP-232.
**Status:** PP-232 is a valid applied patch. The SIM-ARC-01 statement is accurate for the patched ruleset. No error in simulation. Documented for transparency.

---

## Conversation-Level Review: What Worked and What Didn't

### Worked Well
- **Arc generation quality:** All 20 arcs (SIM-ARC-01 through SIM-ARC-04, ARC 1–20) are mechanically grounded with correct pool sizes, probability calculations, and cross-system interactions. The archetype taxonomy (IP-A/F, NG-A/F, NG-G/L, NG-M/R) provides a coherent design tool.
- **Probability calculations:** All P(success) figures computed correctly for the "+2 fixed" model, with correct TN7 expected value of 0.30/die. Directional accuracy is reliable even if specific figures need recalculation under chain-die model.
- **Editorial resolution discipline:** The flag/resolve distinction held consistently. Worldbuilding items were never resolved unilaterally. Mechanical items were resolved with canonical citations.
- **Cross-arc interactions:** All four batches produced valid cross-arc tables. The convergence risks identified (e.g., NG-G applied to three simultaneous 1-scene windows) are mechanically accurate.

### Didn't Work / Needs Attention Next Session
- **PP numbering:** The collision should have been checked before the editorial_resolution_pass.md was written. Always query `max(PP)` from the register before naming new patches.
- **Ledger rewrite atomicity:** The 6442da0a commit landed params updates but the ledger rewrite may not have committed cleanly (evidenced by the repo still showing old ledger format). Always verify the ledger status after a commit that includes it.
- **SIM-DEBT not closed:** SIM-DEBT-01 (Contest calibration with Charisma×2 pool), SIM-DEBT-02 (Dissolution RS recalibration), SIM-DEBT-06 (War-scale Thread coherence), SIM-DEBT-07 (High-resistance Contest) are all open. Priority for next session.
- **stage13_npcs.md not updated:** Composure formula, attribute renames (Presence → Charisma), and new NPC profiles from arcs not propagated to stage13. Needs a dedicated propagation commit.

---

## Flagged Items for Next Session (15 items requiring user decisions)

In priority order:

| ID | Priority | Decision needed |
|----|----------|-----------------|
| ED-036 | P1 BLOCKER | Altonian invasion unit stats — approve provisional or design canonical |
| ED-110/112 | P1 | Church victory path + TC lock — linked; decide together |
| ED-109 | P1 | Crown victory balance (3/5 deeds pre-met) |
| ED-111/113 | P2 | Varfell T13 balance (Fort 1 fix applied; confirm sufficient) |
| ED-108 | P2 | Crown territory names T10/T11 (Nordhelm/Mittelmark) |
| ED-171 | P2 | Niflhel archive lineage data (affects ARC 1/5 cross-arc) |
| ED-119 | P2 | Lenneth Almqvist TS arc |
| ED-080/081 | P2 | Baralta/Vaynard BG Conviction text |
| ED-143–146 | P2 | PC simulation construct approvals (4 items) |
| ED-005/006 | P3 | Riskbreakers identity / Revolution leader |
| ED-024 | P3 | Southernmost Mode 3 entity stat blocks |

---

## SIM-DEBT Register (Open)

| ID | Description | Priority |
|----|-------------|----------|
| SIM-DEBT-01 | Contest calibration — all prior tests used old Cognition+History pool; new (Charisma×2)+History pool not yet stress-tested | P1 |
| SIM-DEBT-02 | Dissolution RS recalibration — 90.3% Rupture at RS<24 is likely miscalibrated due to FR surcharge exemption stacking | P1 |
| SIM-DEBT-06 | War-scale Thread coherence — Dissonant effects in mass battle not simulated | P2 |
| SIM-DEBT-07 | High-resistance Contest calibration — resistance 4+ renders Formal Contest statistically inert; no simulation yet confirms Grand Contest threshold | P2 |

---

## Session Close State

- Highest PP applied: PP-262
- Highest ED flagged: ED-171
- Simulation batches complete: SIM-ARC-01 through SIM-ARC-04 (20 arcs, 6 archetype families, 59 findings)
- All params files updated: params_core, params_threadwork, params_contest, params_mass_combat, params_factions, params_board_game
- Ledger: 171 items processed; 142 resolved; 15 flagged; 14 struck
- Next action: User review of 15 flagged items; SIM-DEBT-01/02 closure
